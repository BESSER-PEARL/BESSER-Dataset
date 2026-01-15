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

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="choice"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction")
    }
)

AssociativityKind: Enumeration = Enumeration(
    name="AssociativityKind",
    literals={
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right")
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

# Classes
pivot_Detail = Class(name="pivot::Detail")
pivot_AnyType = Class(name="pivot::AnyType")
Class_ = Class(name="Class")
pivot_AssociationClass = Class(name="pivot::AssociationClass")
pivot_Property = Class(name="pivot::Property")
pivot_AssociationClassCallExp = Class(name="pivot::AssociationClassCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
pivot_Annotation = Class(name="pivot::Annotation")
NamedElement = Class(name="NamedElement")
pivot_Element = Class(name="pivot::Element", is_abstract=True)
pivot_Transition = Class(name="pivot::Transition")
pivot_BooleanLiteralExp = Class(name="pivot::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
pivot_CallExp = Class(name="pivot::CallExp", is_abstract=True)
OCLExpression = Class(name="OCLExpression")
pivot_BagType = Class(name="pivot::BagType")
CollectionType = Class(name="CollectionType")
pivot_Behavior = Class(name="pivot::Behavior", is_abstract=True)
pivot_Class = Class(name="pivot::Class")
Type = Class(name="Type")
Namespace = Class(name="Namespace")
pivot_OCLExpression = Class(name="pivot::OCLExpression", is_abstract=True)
pivot_CallOperationAction = Class(name="pivot::CallOperationAction")
pivot_Operation = Class(name="pivot::Operation")
pivot_CollectionLiteralExp = Class(name="pivot::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
pivot_CollectionItem = Class(name="pivot::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
pivot_CollectionRange = Class(name="pivot::CollectionRange")
pivot_CollectionType = Class(name="pivot::CollectionType")
DataType = Class(name="DataType")
pivot_Type = Class(name="pivot::Type")
pivot_Comment = Class(name="pivot::Comment")
Element = Class(name="Element")
pivot_CollectionLiteralPart = Class(name="pivot::CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
pivot_ConnectionPointReference = Class(name="pivot::ConnectionPointReference")
Vertex = Class(name="Vertex")
pivot_Pseudostate = Class(name="pivot::Pseudostate")
pivot_Constraint = Class(name="pivot::Constraint")
pivot_Namespace = Class(name="pivot::Namespace", is_abstract=True)
pivot_State = Class(name="pivot::State")
pivot_OpaqueExpression = Class(name="pivot::OpaqueExpression")
pivot_ConstructorExp = Class(name="pivot::ConstructorExp")
pivot_ConstructorPart = Class(name="pivot::ConstructorPart")
pivot_DynamicElement = Class(name="pivot::DynamicElement")
pivot_DynamicProperty = Class(name="pivot::DynamicProperty")
pivot_DataType = Class(name="pivot::DataType")
Visitable = Class(name="Visitable")
pivot_ElementExtension = Class(name="pivot::ElementExtension")
pivot_DynamicType = Class(name="pivot::DynamicType")
DynamicElement = Class(name="DynamicElement")
pivot_Stereotype = Class(name="pivot::Stereotype")
pivot_EnumLiteralExp = Class(name="pivot::EnumLiteralExp")
pivot_EnumerationLiteral = Class(name="pivot::EnumerationLiteral")
pivot_ExpressionInOCL = Class(name="pivot::ExpressionInOCL")
OpaqueExpression = Class(name="OpaqueExpression")
pivot_Variable = Class(name="pivot::Variable")
pivot_Enumeration = Class(name="pivot::Enumeration")
pivot_Feature = Class(name="pivot::Feature", is_abstract=True)
TypedMultiplicityElement = Class(name="TypedMultiplicityElement")
pivot_FeatureCallExp = Class(name="pivot::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
pivot_FinalState = Class(name="pivot::FinalState")
State = Class(name="State")
pivot_IfExp = Class(name="pivot::IfExp")
pivot_Import = Class(name="pivot::Import")
pivot_IntegerLiteralExp = Class(name="pivot::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
pivot_InvalidLiteralExp = Class(name="pivot::InvalidLiteralExp")
pivot_InvalidType = Class(name="pivot::InvalidType")
pivot_IterateExp = Class(name="pivot::IterateExp")
LoopExp = Class(name="LoopExp")
ReferringElement = Class(name="ReferringElement")
pivot_Parameter = Class(name="pivot::Parameter")
pivot_IteratorExp = Class(name="pivot::IteratorExp")
pivot_Iteration = Class(name="pivot::Iteration")
Operation = Class(name="Operation")
pivot_LambdaType = Class(name="pivot::LambdaType")
pivot_LetExp = Class(name="pivot::LetExp")
pivot_Library = Class(name="pivot::Library")
Package = Class(name="Package")
pivot_Precedence = Class(name="pivot::Precedence")
pivot_LiteralExp = Class(name="pivot::LiteralExp", is_abstract=True)
pivot_LoopExp = Class(name="pivot::LoopExp", is_abstract=True)
pivot_SendSignalAction = Class(name="pivot::SendSignalAction")
pivot_MessageType = Class(name="pivot::MessageType")
pivot_Signal = Class(name="pivot::Signal")
pivot_Metaclass = Class(name="pivot::Metaclass")
pivot_MessageExp = Class(name="pivot::MessageExp")
pivot_NavigationCallExp = Class(name="pivot::NavigationCallExp", is_abstract=True)
FeatureCallExp = Class(name="FeatureCallExp")
pivot_NullLiteralExp = Class(name="pivot::NullLiteralExp")
pivot_NumericLiteralExp = Class(name="pivot::NumericLiteralExp", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
pivot_MorePivotable = Class(name="pivot::MorePivotable", is_abstract=True)
pivot_Nameable = Class(name="pivot::Nameable", is_abstract=True)
pivot_NamedElement = Class(name="pivot::NamedElement", is_abstract=True)
Nameable = Class(name="Nameable")
Feature = Class(name="Feature")
TemplateableElement = Class(name="TemplateableElement")
ParameterableElement = Class(name="ParameterableElement")
pivot_OperationCallExp = Class(name="pivot::OperationCallExp")
pivot_OperationTemplateParameter = Class(name="pivot::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
pivot_OppositePropertyCallExp = Class(name="pivot::OppositePropertyCallExp")
pivot_OrderedSetType = Class(name="pivot::OrderedSetType")
pivot_Package = Class(name="pivot::Package")
VariableDeclaration = Class(name="VariableDeclaration")
pivot_ParameterableElement = Class(name="pivot::ParameterableElement", is_abstract=True)
pivot_TemplateParameter = Class(name="pivot::TemplateParameter")
pivot_Pivotable = Class(name="pivot::Pivotable", is_abstract=True)
pivot_PrimitiveLiteralExp = Class(name="pivot::PrimitiveLiteralExp", is_abstract=True)
pivot_ProfileApplication = Class(name="pivot::ProfileApplication")
pivot_PackageableElement = Class(name="pivot::PackageableElement", is_abstract=True)
pivot_PrimitiveType = Class(name="pivot::PrimitiveType")
pivot_Profile = Class(name="pivot::Profile")
pivot_PropertyCallExp = Class(name="pivot::PropertyCallExp")
pivot_StateMachine = Class(name="pivot::StateMachine")
pivot_RealLiteralExp = Class(name="pivot::RealLiteralExp")
pivot_ReferringElement = Class(name="pivot::ReferringElement", is_abstract=True)
pivot_Region = Class(name="pivot::Region")
pivot_Vertex = Class(name="pivot::Vertex", is_abstract=True)
pivot_Root = Class(name="pivot::Root")
pivot_SelfType = Class(name="pivot::SelfType")
pivot_SequenceType = Class(name="pivot::SequenceType")
pivot_SetType = Class(name="pivot::SetType")
pivot_Trigger = Class(name="pivot::Trigger")
pivot_StateExp = Class(name="pivot::StateExp")
Behavior = Class(name="Behavior")
pivot_TypeExtension = Class(name="pivot::TypeExtension")
pivot_StringLiteralExp = Class(name="pivot::StringLiteralExp")
pivot_TemplateBinding = Class(name="pivot::TemplateBinding")
pivot_TemplateableElement = Class(name="pivot::TemplateableElement", is_abstract=True)
pivot_TemplateParameterSubstitution = Class(name="pivot::TemplateParameterSubstitution")
pivot_TemplateSignature = Class(name="pivot::TemplateSignature")
pivot_TemplateParameterType = Class(name="pivot::TemplateParameterType")
pivot_TupleLiteralExp = Class(name="pivot::TupleLiteralExp")
pivot_TupleLiteralPart = Class(name="pivot::TupleLiteralPart")
pivot_TupleType = Class(name="pivot::TupleType")
pivot_TypeExp = Class(name="pivot::TypeExp")
pivot_TypeTemplateParameter = Class(name="pivot::TypeTemplateParameter")
pivot_TypedElement = Class(name="pivot::TypedElement", is_abstract=True)
pivot_UnlimitedNaturalLiteralExp = Class(name="pivot::UnlimitedNaturalLiteralExp")
pivot_UnspecifiedType = Class(name="pivot::UnspecifiedType")
pivot_UnspecifiedValueExp = Class(name="pivot::UnspecifiedValueExp")
pivot_ValueSpecification = Class(name="pivot::ValueSpecification", is_abstract=True)
pivot_TypedMultiplicityElement = Class(name="pivot::TypedMultiplicityElement", is_abstract=True)
pivot_Visitable = Class(name="pivot::Visitable", is_abstract=True)
pivot_Visitor = Class(name="pivot::Visitor", is_abstract=True)
pivot_VoidType = Class(name="pivot::VoidType")
pivot_VariableDeclaration = Class(name="pivot::VariableDeclaration", is_abstract=True)
pivot_VariableExp = Class(name="pivot::VariableExp")

# pivot_Detail class attributes and methods
pivot_Detail_value: Property = Property(name="value", type=StringType)
pivot_Detail.attributes={pivot_Detail_value}

# pivot_AnyType class attributes and methods

# Class class attributes and methods

# pivot_AssociationClass class attributes and methods

# pivot_Property class attributes and methods
pivot_Property_default: Property = Property(name="default", type=StringType)
pivot_Property_implicit: Property = Property(name="implicit", type=StringType)
pivot_Property_isDerived: Property = Property(name="isDerived", type=StringType)
pivot_Property_isID: Property = Property(name="isID", type=StringType)
pivot_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
pivot_Property_isResolveProxies: Property = Property(name="isResolveProxies", type=StringType)
pivot_Property_isTransient: Property = Property(name="isTransient", type=StringType)
pivot_Property_isUnsettable: Property = Property(name="isUnsettable", type=StringType)
pivot_Property_isVolatile: Property = Property(name="isVolatile", type=StringType)
pivot_Property_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_Property_m_CompatibleDefaultExpression: Method = Method(name="CompatibleDefaultExpression", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
pivot_Property.attributes={pivot_Property_isComposite, pivot_Property_isDerived, pivot_Property_isTransient, pivot_Property_isReadOnly, pivot_Property_implicit, pivot_Property_isID, pivot_Property_default, pivot_Property_isVolatile, pivot_Property_isResolveProxies, pivot_Property_isUnsettable}
pivot_Property.methods={pivot_Property_m_CompatibleDefaultExpression, pivot_Property_m_isAttribute}

# pivot_AssociationClassCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# pivot_Annotation class attributes and methods

# NamedElement class attributes and methods

# pivot_Element class attributes and methods
pivot_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
pivot_Element_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='propertyName'), Parameter(name='stereotype')}, type=Element)
pivot_Element.methods={pivot_Element_m_getValue, pivot_Element_m_allOwnedElements}

# pivot_Transition class attributes and methods
pivot_Transition_kind: Property = Property(name="kind", type=StringType)
pivot_Transition.attributes={pivot_Transition_kind}

# pivot_BooleanLiteralExp class attributes and methods
pivot_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
pivot_BooleanLiteralExp_m_TypeIsBoolean: Method = Method(name="TypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_BooleanLiteralExp.attributes={pivot_BooleanLiteralExp_booleanSymbol}
pivot_BooleanLiteralExp.methods={pivot_BooleanLiteralExp_m_TypeIsBoolean}

# PrimitiveLiteralExp class attributes and methods

# pivot_CallExp class attributes and methods
pivot_CallExp_implicit: Property = Property(name="implicit", type=StringType)
pivot_CallExp.attributes={pivot_CallExp_implicit}

# OCLExpression class attributes and methods

# pivot_BagType class attributes and methods

# CollectionType class attributes and methods

# pivot_Behavior class attributes and methods

# pivot_Class class attributes and methods
pivot_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
pivot_Class_isActive: Property = Property(name="isActive", type=StringType)
pivot_Class_isInterface: Property = Property(name="isInterface", type=StringType)
pivot_Class.attributes={pivot_Class_isAbstract, pivot_Class_isActive, pivot_Class_isInterface}

# Type class attributes and methods

# Namespace class attributes and methods

# pivot_OCLExpression class attributes and methods

# pivot_CallOperationAction class attributes and methods

# pivot_Operation class attributes and methods
pivot_Operation_isInvalidating: Property = Property(name="isInvalidating", type=StringType)
pivot_Operation_isValidating: Property = Property(name="isValidating", type=StringType)
pivot_Operation_m_LoadableImplementation: Method = Method(name="LoadableImplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_UniquePostconditionName: Method = Method(name="UniquePostconditionName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Operation_m_UniquePreconditionName: Method = Method(name="UniquePreconditionName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_CompatibleReturn: Method = Method(name="CompatibleReturn", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation.attributes={pivot_Operation_isInvalidating, pivot_Operation_isValidating}
pivot_Operation.methods={pivot_Operation_m_UniquePreconditionName, pivot_Operation_m_CompatibleReturn, pivot_Operation_m_UniquePostconditionName, pivot_Operation_m_LoadableImplementation}

# pivot_CollectionLiteralExp class attributes and methods
pivot_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
pivot_CollectionLiteralExp_m_BagKindIsBag: Method = Method(name="BagKindIsBag", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_CollectionKindIsConcrete: Method = Method(name="CollectionKindIsConcrete", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_SequenceKindIsSequence: Method = Method(name="SequenceKindIsSequence", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_SetKindIsSet: Method = Method(name="SetKindIsSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_OrderedSetKindIsOrderedSet: Method = Method(name="OrderedSetKindIsOrderedSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp.attributes={pivot_CollectionLiteralExp_kind}
pivot_CollectionLiteralExp.methods={pivot_CollectionLiteralExp_m_SequenceKindIsSequence, pivot_CollectionLiteralExp_m_CollectionKindIsConcrete, pivot_CollectionLiteralExp_m_BagKindIsBag, pivot_CollectionLiteralExp_m_OrderedSetKindIsOrderedSet, pivot_CollectionLiteralExp_m_SetKindIsSet}

# LiteralExp class attributes and methods

# pivot_CollectionItem class attributes and methods
pivot_CollectionItem_m_TypeIsItemType: Method = Method(name="TypeIsItemType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionItem.methods={pivot_CollectionItem_m_TypeIsItemType}

# CollectionLiteralPart class attributes and methods

# pivot_CollectionRange class attributes and methods

# pivot_CollectionType class attributes and methods
pivot_CollectionType_lower: Property = Property(name="lower", type=StringType)
pivot_CollectionType_upper: Property = Property(name="upper", type=StringType)
pivot_CollectionType.attributes={pivot_CollectionType_upper, pivot_CollectionType_lower}

# DataType class attributes and methods

# pivot_Type class attributes and methods
pivot_Type_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
pivot_Type_m_UniqueInvariantName: Method = Method(name="UniqueInvariantName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Type_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='expr'), Parameter(name='selfType')}, type=Type)
pivot_Type.attributes={pivot_Type_instanceClassName}
pivot_Type.methods={pivot_Type_m_specializeIn, pivot_Type_m_UniqueInvariantName}

# pivot_Comment class attributes and methods
pivot_Comment_body: Property = Property(name="body", type=StringType)
pivot_Comment.attributes={pivot_Comment_body}

# Element class attributes and methods

# pivot_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# pivot_ConnectionPointReference class attributes and methods

# Vertex class attributes and methods

# pivot_Pseudostate class attributes and methods
pivot_Pseudostate_kind: Property = Property(name="kind", type=StringType)
pivot_Pseudostate.attributes={pivot_Pseudostate_kind}

# pivot_Constraint class attributes and methods
pivot_Constraint_isCallable: Property = Property(name="isCallable", type=StringType)
pivot_Constraint_m_UniqueName: Method = Method(name="UniqueName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Constraint.attributes={pivot_Constraint_isCallable}
pivot_Constraint.methods={pivot_Constraint_m_UniqueName}

# pivot_Namespace class attributes and methods

# pivot_State class attributes and methods
pivot_State_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
pivot_State_isSimple: Property = Property(name="isSimple", type=StringType)
pivot_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
pivot_State.attributes={pivot_State_isSubmachineState, pivot_State_isSimple, pivot_State_isOrthogonal, pivot_State_isComposite}

# pivot_OpaqueExpression class attributes and methods
pivot_OpaqueExpression_body: Property = Property(name="body", type=StringType)
pivot_OpaqueExpression_language: Property = Property(name="language", type=StringType)
pivot_OpaqueExpression.attributes={pivot_OpaqueExpression_body, pivot_OpaqueExpression_language}

# pivot_ConstructorExp class attributes and methods
pivot_ConstructorExp_value: Property = Property(name="value", type=StringType)
pivot_ConstructorExp.attributes={pivot_ConstructorExp_value}

# pivot_ConstructorPart class attributes and methods

# pivot_DynamicElement class attributes and methods

# pivot_DynamicProperty class attributes and methods
pivot_DynamicProperty_default: Property = Property(name="default", type=StringType)
pivot_DynamicProperty.attributes={pivot_DynamicProperty_default}

# pivot_DataType class attributes and methods
pivot_DataType_isSerializable: Property = Property(name="isSerializable", type=StringType)
pivot_DataType.attributes={pivot_DataType_isSerializable}

# Visitable class attributes and methods

# pivot_ElementExtension class attributes and methods
pivot_ElementExtension_isApplied: Property = Property(name="isApplied", type=StringType)
pivot_ElementExtension_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_ElementExtension.attributes={pivot_ElementExtension_isApplied, pivot_ElementExtension_isRequired}

# pivot_DynamicType class attributes and methods

# DynamicElement class attributes and methods

# pivot_Stereotype class attributes and methods

# pivot_EnumLiteralExp class attributes and methods
pivot_EnumLiteralExp_m_TypeIsEnumerationType: Method = Method(name="TypeIsEnumerationType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_EnumLiteralExp.methods={pivot_EnumLiteralExp_m_TypeIsEnumerationType}

# pivot_EnumerationLiteral class attributes and methods
pivot_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
pivot_EnumerationLiteral.attributes={pivot_EnumerationLiteral_value}

# pivot_ExpressionInOCL class attributes and methods

# OpaqueExpression class attributes and methods

# pivot_Variable class attributes and methods
pivot_Variable_implicit: Property = Property(name="implicit", type=StringType)
pivot_Variable_m_CompatibleInitialiserType: Method = Method(name="CompatibleInitialiserType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Variable.attributes={pivot_Variable_implicit}
pivot_Variable.methods={pivot_Variable_m_CompatibleInitialiserType}

# pivot_Enumeration class attributes and methods

# pivot_Feature class attributes and methods
pivot_Feature_implementation: Property = Property(name="implementation", type=StringType)
pivot_Feature_implementationClass: Property = Property(name="implementationClass", type=StringType)
pivot_Feature.attributes={pivot_Feature_implementationClass, pivot_Feature_implementation}

# TypedMultiplicityElement class attributes and methods

# pivot_FeatureCallExp class attributes and methods
pivot_FeatureCallExp_isPre: Property = Property(name="isPre", type=StringType)
pivot_FeatureCallExp.attributes={pivot_FeatureCallExp_isPre}

# CallExp class attributes and methods

# pivot_FinalState class attributes and methods

# State class attributes and methods

# pivot_IfExp class attributes and methods
pivot_IfExp_m_ConditionTypeIsBoolean: Method = Method(name="ConditionTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IfExp.methods={pivot_IfExp_m_ConditionTypeIsBoolean}

# pivot_Import class attributes and methods

# pivot_IntegerLiteralExp class attributes and methods
pivot_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
pivot_IntegerLiteralExp_m_TypeIsInteger: Method = Method(name="TypeIsInteger", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IntegerLiteralExp.attributes={pivot_IntegerLiteralExp_integerSymbol}
pivot_IntegerLiteralExp.methods={pivot_IntegerLiteralExp_m_TypeIsInteger}

# NumericLiteralExp class attributes and methods

# pivot_InvalidLiteralExp class attributes and methods

# pivot_InvalidType class attributes and methods

# pivot_IterateExp class attributes and methods
pivot_IterateExp_m_BodyTypeConformsToResultType: Method = Method(name="BodyTypeConformsToResultType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp_m_OneInitializer: Method = Method(name="OneInitializer", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IterateExp_m_TypeIsResultType: Method = Method(name="TypeIsResultType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp.methods={pivot_IterateExp_m_BodyTypeConformsToResultType, pivot_IterateExp_m_TypeIsResultType, pivot_IterateExp_m_OneInitializer}

# LoopExp class attributes and methods

# ReferringElement class attributes and methods

# pivot_Parameter class attributes and methods

# pivot_IteratorExp class attributes and methods
pivot_IteratorExp_m_AnyBodyTypeIsBoolean: Method = Method(name="AnyBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_AnyHasOneIterator: Method = Method(name="AnyHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ClosureBodyTypeIsConformanttoIteratorType: Method = Method(name="ClosureBodyTypeIsConformanttoIteratorType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ClosureElementTypeIsSourceElementType: Method = Method(name="ClosureElementTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ClosureHasOneIterator: Method = Method(name="ClosureHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_AnyTypeIsSourceElementType: Method = Method(name="AnyTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ClosureTypeIsUniqueCollection: Method = Method(name="ClosureTypeIsUniqueCollection", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectElementTypeIsSourceElementType: Method = Method(name="CollectElementTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectHasOneIterator: Method = Method(name="CollectHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ClosureSourceElementTypeIsBodyElementType: Method = Method(name="ClosureSourceElementTypeIsBodyElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedTypeIsBag: Method = Method(name="CollectNestedTypeIsBag", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedTypeIsBodyType: Method = Method(name="CollectNestedTypeIsBodyType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectTypeIsUnordered: Method = Method(name="CollectTypeIsUnordered", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedHasOneIterator: Method = Method(name="CollectNestedHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ExistsTypeIsBoolean: Method = Method(name="ExistsTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ForAllBodyTypeIsBoolean: Method = Method(name="ForAllBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ForAllTypeIsBoolean: Method = Method(name="ForAllTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ExistsBodyTypeIsBoolean: Method = Method(name="ExistsBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_IsUniqueHasOneIterator: Method = Method(name="IsUniqueHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_IsUniqueTypeIsBoolean: Method = Method(name="IsUniqueTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_IteratorTypeIsSourceElementType: Method = Method(name="IteratorTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_OneHasOneIterator: Method = Method(name="OneHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_OneTypeIsBoolean: Method = Method(name="OneTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectHasOneIterator: Method = Method(name="RejectOrSelectHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectTypeIsBoolean: Method = Method(name="RejectOrSelectTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectTypeIsSourceType: Method = Method(name="RejectOrSelectTypeIsSourceType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_SortedByElementTypeIsSourceElementType: Method = Method(name="SortedByElementTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_OneBodyTypeIsBoolean: Method = Method(name="OneBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_SortedByIteratorTypeIsComparable: Method = Method(name="SortedByIteratorTypeIsComparable", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_SortedByHasOneIterator: Method = Method(name="SortedByHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_SortedByIsOrderedIfSourceIsOrdered: Method = Method(name="SortedByIsOrderedIfSourceIsOrdered", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp.methods={pivot_IteratorExp_m_CollectElementTypeIsSourceElementType, pivot_IteratorExp_m_IsUniqueTypeIsBoolean, pivot_IteratorExp_m_RejectOrSelectTypeIsBoolean, pivot_IteratorExp_m_ClosureHasOneIterator, pivot_IteratorExp_m_CollectNestedHasOneIterator, pivot_IteratorExp_m_SortedByIteratorTypeIsComparable, pivot_IteratorExp_m_ExistsTypeIsBoolean, pivot_IteratorExp_m_AnyBodyTypeIsBoolean, pivot_IteratorExp_m_IsUniqueHasOneIterator, pivot_IteratorExp_m_OneBodyTypeIsBoolean, pivot_IteratorExp_m_RejectOrSelectHasOneIterator, pivot_IteratorExp_m_CollectTypeIsUnordered, pivot_IteratorExp_m_OneTypeIsBoolean, pivot_IteratorExp_m_SortedByIsOrderedIfSourceIsOrdered, pivot_IteratorExp_m_IteratorTypeIsSourceElementType, pivot_IteratorExp_m_CollectHasOneIterator, pivot_IteratorExp_m_OneHasOneIterator, pivot_IteratorExp_m_ForAllBodyTypeIsBoolean, pivot_IteratorExp_m_AnyHasOneIterator, pivot_IteratorExp_m_CollectNestedTypeIsBodyType, pivot_IteratorExp_m_SortedByElementTypeIsSourceElementType, pivot_IteratorExp_m_ExistsBodyTypeIsBoolean, pivot_IteratorExp_m_ForAllTypeIsBoolean, pivot_IteratorExp_m_ClosureElementTypeIsSourceElementType, pivot_IteratorExp_m_ClosureTypeIsUniqueCollection, pivot_IteratorExp_m_ClosureBodyTypeIsConformanttoIteratorType, pivot_IteratorExp_m_ClosureSourceElementTypeIsBodyElementType, pivot_IteratorExp_m_CollectNestedTypeIsBag, pivot_IteratorExp_m_RejectOrSelectTypeIsSourceType, pivot_IteratorExp_m_AnyTypeIsSourceElementType, pivot_IteratorExp_m_SortedByHasOneIterator}

# pivot_Iteration class attributes and methods

# Operation class attributes and methods

# pivot_LambdaType class attributes and methods

# pivot_LetExp class attributes and methods
pivot_LetExp_m_TypeIsInType: Method = Method(name="TypeIsInType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LetExp.methods={pivot_LetExp_m_TypeIsInType}

# pivot_Library class attributes and methods

# Package class attributes and methods

# pivot_Precedence class attributes and methods
pivot_Precedence_associativity: Property = Property(name="associativity", type=StringType)
pivot_Precedence_order: Property = Property(name="order", type=IntegerType)
pivot_Precedence.attributes={pivot_Precedence_order, pivot_Precedence_associativity}

# pivot_LiteralExp class attributes and methods

# pivot_LoopExp class attributes and methods
pivot_LoopExp_m_NoInitializers: Method = Method(name="NoInitializers", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LoopExp_m_SourceIsCollection: Method = Method(name="SourceIsCollection", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LoopExp.methods={pivot_LoopExp_m_NoInitializers, pivot_LoopExp_m_SourceIsCollection}

# pivot_SendSignalAction class attributes and methods

# pivot_MessageType class attributes and methods

# pivot_Signal class attributes and methods

# pivot_Metaclass class attributes and methods

# pivot_MessageExp class attributes and methods
pivot_MessageExp_m_TargetIsNotACollection: Method = Method(name="TargetIsNotACollection", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_MessageExp_m_OneCallOrOneSend: Method = Method(name="OneCallOrOneSend", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_MessageExp.methods={pivot_MessageExp_m_TargetIsNotACollection, pivot_MessageExp_m_OneCallOrOneSend}

# pivot_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# pivot_NullLiteralExp class attributes and methods

# pivot_NumericLiteralExp class attributes and methods

# ValueSpecification class attributes and methods

# pivot_MorePivotable class attributes and methods

# pivot_Nameable class attributes and methods

# pivot_NamedElement class attributes and methods
pivot_NamedElement_isStatic: Property = Property(name="isStatic", type=StringType)
pivot_NamedElement_name: Property = Property(name="name", type=StringType)
pivot_NamedElement.attributes={pivot_NamedElement_name, pivot_NamedElement_isStatic}

# Nameable class attributes and methods

# Feature class attributes and methods

# TemplateableElement class attributes and methods

# ParameterableElement class attributes and methods

# pivot_OperationCallExp class attributes and methods
pivot_OperationCallExp_m_ArgumentCount: Method = Method(name="ArgumentCount", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_OperationCallExp_m_ArgumentTypeIsConformant: Method = Method(name="ArgumentTypeIsConformant", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_OperationCallExp.methods={pivot_OperationCallExp_m_ArgumentCount, pivot_OperationCallExp_m_ArgumentTypeIsConformant}

# pivot_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# pivot_OppositePropertyCallExp class attributes and methods

# pivot_OrderedSetType class attributes and methods

# pivot_Package class attributes and methods
pivot_Package_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
pivot_Package_nsURI: Property = Property(name="nsURI", type=StringType)
pivot_Package.attributes={pivot_Package_nsPrefix, pivot_Package_nsURI}

# VariableDeclaration class attributes and methods

# pivot_ParameterableElement class attributes and methods
pivot_ParameterableElement_m_isCompatibleWith: Method = Method(name="isCompatibleWith", parameters={Parameter(name='p')}, type=StringType)
pivot_ParameterableElement_m_isTemplateParameter: Method = Method(name="isTemplateParameter", parameters={}, type=StringType)
pivot_ParameterableElement.methods={pivot_ParameterableElement_m_isCompatibleWith, pivot_ParameterableElement_m_isTemplateParameter}

# pivot_TemplateParameter class attributes and methods

# pivot_Pivotable class attributes and methods

# pivot_PrimitiveLiteralExp class attributes and methods

# pivot_ProfileApplication class attributes and methods
pivot_ProfileApplication_isStrict: Property = Property(name="isStrict", type=StringType)
pivot_ProfileApplication.attributes={pivot_ProfileApplication_isStrict}

# pivot_PackageableElement class attributes and methods

# pivot_PrimitiveType class attributes and methods

# pivot_Profile class attributes and methods

# pivot_PropertyCallExp class attributes and methods
pivot_PropertyCallExp_m_CompatibleResultType: Method = Method(name="CompatibleResultType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_PropertyCallExp_m_NonStaticSourceTypeIsConformant: Method = Method(name="NonStaticSourceTypeIsConformant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType: Method = Method(name="getSpecializedReferredPropertyOwningType", parameters={}, type=Type)
pivot_PropertyCallExp_m_getSpecializedReferredPropertyType: Method = Method(name="getSpecializedReferredPropertyType", parameters={}, type=Type)
pivot_PropertyCallExp.methods={pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType, pivot_PropertyCallExp_m_getSpecializedReferredPropertyType, pivot_PropertyCallExp_m_NonStaticSourceTypeIsConformant, pivot_PropertyCallExp_m_CompatibleResultType}

# pivot_StateMachine class attributes and methods

# pivot_RealLiteralExp class attributes and methods
pivot_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
pivot_RealLiteralExp.attributes={pivot_RealLiteralExp_realSymbol}

# pivot_ReferringElement class attributes and methods
pivot_ReferringElement_m_getReferredElement: Method = Method(name="getReferredElement", parameters={}, type=Element)
pivot_ReferringElement.methods={pivot_ReferringElement_m_getReferredElement}

# pivot_Region class attributes and methods

# pivot_Vertex class attributes and methods

# pivot_Root class attributes and methods
pivot_Root_externalURI: Property = Property(name="externalURI", type=StringType)
pivot_Root.attributes={pivot_Root_externalURI}

# pivot_SelfType class attributes and methods
pivot_SelfType_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='expr'), Parameter(name='selfType')}, type=Type)
pivot_SelfType.methods={pivot_SelfType_m_specializeIn}

# pivot_SequenceType class attributes and methods

# pivot_SetType class attributes and methods

# pivot_Trigger class attributes and methods

# pivot_StateExp class attributes and methods

# Behavior class attributes and methods

# pivot_TypeExtension class attributes and methods
pivot_TypeExtension_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_TypeExtension.attributes={pivot_TypeExtension_isRequired}

# pivot_StringLiteralExp class attributes and methods
pivot_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
pivot_StringLiteralExp.attributes={pivot_StringLiteralExp_stringSymbol}

# pivot_TemplateBinding class attributes and methods

# pivot_TemplateableElement class attributes and methods
pivot_TemplateableElement_m_isTemplate: Method = Method(name="isTemplate", parameters={}, type=StringType)
pivot_TemplateableElement_m_parameterableElements: Method = Method(name="parameterableElements", parameters={}, type=ParameterableElement)
pivot_TemplateableElement.methods={pivot_TemplateableElement_m_parameterableElements, pivot_TemplateableElement_m_isTemplate}

# pivot_TemplateParameterSubstitution class attributes and methods

# pivot_TemplateSignature class attributes and methods

# pivot_TemplateParameterType class attributes and methods
pivot_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
pivot_TemplateParameterType.attributes={pivot_TemplateParameterType_specification}

# pivot_TupleLiteralExp class attributes and methods

# pivot_TupleLiteralPart class attributes and methods

# pivot_TupleType class attributes and methods

# pivot_TypeExp class attributes and methods

# pivot_TypeTemplateParameter class attributes and methods
pivot_TypeTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=StringType)
pivot_TypeTemplateParameter.attributes={pivot_TypeTemplateParameter_allowSubstitutable}

# pivot_TypedElement class attributes and methods
pivot_TypedElement_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_TypedElement.attributes={pivot_TypedElement_isRequired}

# pivot_UnlimitedNaturalLiteralExp class attributes and methods
pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol: Property = Property(name="unlimitedNaturalSymbol", type=StringType)
pivot_UnlimitedNaturalLiteralExp.attributes={pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol}

# pivot_UnspecifiedType class attributes and methods

# pivot_UnspecifiedValueExp class attributes and methods

# pivot_ValueSpecification class attributes and methods
pivot_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
pivot_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
pivot_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
pivot_ValueSpecification.methods={pivot_ValueSpecification_m_booleanValue, pivot_ValueSpecification_m_stringValue, pivot_ValueSpecification_m_unlimitedValue, pivot_ValueSpecification_m_isComputable, pivot_ValueSpecification_m_integerValue, pivot_ValueSpecification_m_isNull}

# pivot_TypedMultiplicityElement class attributes and methods
pivot_TypedMultiplicityElement_m_CompatibleBody: Method = Method(name="CompatibleBody", parameters={Parameter(name='bodySpecification')}, type=StringType)
pivot_TypedMultiplicityElement_m_makeParameter: Method = Method(name="makeParameter", parameters={}, type=StringType)
pivot_TypedMultiplicityElement.methods={pivot_TypedMultiplicityElement_m_CompatibleBody, pivot_TypedMultiplicityElement_m_makeParameter}

# pivot_Visitable class attributes and methods

# pivot_Visitor class attributes and methods

# pivot_VoidType class attributes and methods

# pivot_VariableDeclaration class attributes and methods

# pivot_VariableExp class attributes and methods
pivot_VariableExp_implicit: Property = Property(name="implicit", type=StringType)
pivot_VariableExp.attributes={pivot_VariableExp_implicit}

# Relationships
ownedContent0: BinaryAssociation = BinaryAssociation(
    name="ownedContent0",
    ends={
        Property(name="pivot_Element", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation", type=pivot_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedDetail1: BinaryAssociation = BinaryAssociation(
    name="ownedDetail1",
    ends={
        Property(name="pivot_Detail", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation2", type=pivot_Detail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference3: BinaryAssociation = BinaryAssociation(
    name="reference3",
    ends={
        Property(name="pivot_Element5", type=pivot_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Annotation4", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
unownedAttribute6: BinaryAssociation = BinaryAssociation(
    name="unownedAttribute6",
    ends={
        Property(name="Property", type=pivot_AssociationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="associationClass", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="Transition", type=pivot_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="effect", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
referredAssociationClass7: BinaryAssociation = BinaryAssociation(
    name="referredAssociationClass7",
    ends={
        Property(name="pivot_AssociationClass", type=pivot_AssociationClassCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_AssociationClassCallExp", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
operation10: BinaryAssociation = BinaryAssociation(
    name="operation10",
    ends={
        Property(name="pivot_Operation", type=pivot_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallOperationAction", type=pivot_Operation, multiplicity=Multiplicity(1, 1))
    }
)
nestedType12: BinaryAssociation = BinaryAssociation(
    name="nestedType12",
    ends={
        Property(name="pivot_Class", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class11", type=pivot_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source9: BinaryAssociation = BinaryAssociation(
    name="source9",
    ends={
        Property(name="pivot_OCLExpression", type=pivot_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item15: BinaryAssociation = BinaryAssociation(
    name="item15",
    ends={
        Property(name="pivot_OCLExpression16", type=pivot_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionItem", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedBehavior13: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior13",
    ends={
        Property(name="pivot_Behavior", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class14", type=pivot_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first18: BinaryAssociation = BinaryAssociation(
    name="first18",
    ends={
        Property(name="pivot_OCLExpression19", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last20: BinaryAssociation = BinaryAssociation(
    name="last20",
    ends={
        Property(name="pivot_OCLExpression22", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange21", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType23: BinaryAssociation = BinaryAssociation(
    name="elementType23",
    ends={
        Property(name="pivot_Type", type=pivot_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
part17: BinaryAssociation = BinaryAssociation(
    name="part17",
    ends={
        Property(name="pivot_CollectionLiteralPart", type=pivot_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionLiteralExp", type=pivot_CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry26: BinaryAssociation = BinaryAssociation(
    name="entry26",
    ends={
        Property(name="pivot_Pseudostate", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
exit27: BinaryAssociation = BinaryAssociation(
    name="exit27",
    ends={
        Property(name="pivot_Pseudostate29", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference28", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement24: BinaryAssociation = BinaryAssociation(
    name="annotatedElement24",
    ends={
        Property(name="pivot_Element25", type=pivot_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Comment", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedElement31: BinaryAssociation = BinaryAssociation(
    name="constrainedElement31",
    ends={
        Property(name="pivot_Element32", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
context33: BinaryAssociation = BinaryAssociation(
    name="context33",
    ends={
        Property(name="pivot_Namespace", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint34", type=pivot_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
state30: BinaryAssociation = BinaryAssociation(
    name="state30",
    ends={
        Property(name="State", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
specification40: BinaryAssociation = BinaryAssociation(
    name="specification40",
    ends={
        Property(name="pivot_OpaqueExpression", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint41", type=pivot_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transition42: BinaryAssociation = BinaryAssociation(
    name="transition42",
    ends={
        Property(name="Transition43", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="guard", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
part44: BinaryAssociation = BinaryAssociation(
    name="part44",
    ends={
        Property(name="pivot_ConstructorPart", type=pivot_ConstructorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorExp", type=pivot_ConstructorPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningState35: BinaryAssociation = BinaryAssociation(
    name="owningState35",
    ends={
        Property(name="State36", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="stateInvariant", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
redefinedConstraint38: BinaryAssociation = BinaryAssociation(
    name="redefinedConstraint38",
    ends={
        Property(name="pivot_Constraint39", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint37", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999))
    }
)
behavioralType50: BinaryAssociation = BinaryAssociation(
    name="behavioralType50",
    ends={
        Property(name="pivot_Type51", type=pivot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DataType", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
metaType52: BinaryAssociation = BinaryAssociation(
    name="metaType52",
    ends={
        Property(name="pivot_Type53", type=pivot_DynamicElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicElement", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
referredProperty54: BinaryAssociation = BinaryAssociation(
    name="referredProperty54",
    ends={
        Property(name="pivot_Property55", type=pivot_DynamicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicProperty", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
initExpression45: BinaryAssociation = BinaryAssociation(
    name="initExpression45",
    ends={
        Property(name="pivot_OCLExpression47", type=pivot_ConstructorPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorPart46", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty48: BinaryAssociation = BinaryAssociation(
    name="referredProperty48",
    ends={
        Property(name="pivot_Property", type=pivot_ConstructorPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorPart49", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
extension58: BinaryAssociation = BinaryAssociation(
    name="extension58",
    ends={
        Property(name="ElementExtension", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=pivot_ElementExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAnnotation60: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotation60",
    ends={
        Property(name="pivot_Element61", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Element59", type=pivot_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty56: BinaryAssociation = BinaryAssociation(
    name="ownedProperty56",
    ends={
        Property(name="pivot_DynamicProperty57", type=pivot_DynamicType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicType", type=pivot_DynamicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
base65: BinaryAssociation = BinaryAssociation(
    name="base65",
    ends={
        Property(name="Element", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=pivot_Element, multiplicity=Multiplicity(1, 1))
    }
)
stereotype66: BinaryAssociation = BinaryAssociation(
    name="stereotype66",
    ends={
        Property(name="pivot_Stereotype", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ElementExtension", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
ownedComment62: BinaryAssociation = BinaryAssociation(
    name="ownedComment62",
    ends={
        Property(name="pivot_Comment64", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Element63", type=pivot_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration69: BinaryAssociation = BinaryAssociation(
    name="enumeration69",
    ends={
        Property(name="Enumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=pivot_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression70: BinaryAssociation = BinaryAssociation(
    name="bodyExpression70",
    ends={
        Property(name="pivot_OCLExpression71", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextVariable72: BinaryAssociation = BinaryAssociation(
    name="contextVariable72",
    ends={
        Property(name="pivot_Variable", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL73", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredEnumLiteral67: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral67",
    ends={
        Property(name="pivot_EnumerationLiteral", type=pivot_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_EnumLiteralExp", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral68: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral68",
    ends={
        Property(name="EnumerationLiteral", type=pivot_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterVariable74: BinaryAssociation = BinaryAssociation(
    name="parameterVariable74",
    ends={
        Property(name="pivot_Variable76", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL75", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable77: BinaryAssociation = BinaryAssociation(
    name="resultVariable77",
    ends={
        Property(name="pivot_Variable79", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL78", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression82: BinaryAssociation = BinaryAssociation(
    name="elseExpression82",
    ends={
        Property(name="pivot_OCLExpression84", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp83", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression85: BinaryAssociation = BinaryAssociation(
    name="thenExpression85",
    ends={
        Property(name="pivot_OCLExpression87", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp86", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importedNamespace88: BinaryAssociation = BinaryAssociation(
    name="importedNamespace88",
    ends={
        Property(name="pivot_Namespace89", type=pivot_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Import", type=pivot_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
condition80: BinaryAssociation = BinaryAssociation(
    name="condition80",
    ends={
        Property(name="pivot_OCLExpression81", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedAccumulator92: BinaryAssociation = BinaryAssociation(
    name="ownedAccumulator92",
    ends={
        Property(name="pivot_Parameter", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedIterator93: BinaryAssociation = BinaryAssociation(
    name="ownedIterator93",
    ends={
        Property(name="pivot_Parameter95", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration94", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result90: BinaryAssociation = BinaryAssociation(
    name="result90",
    ends={
        Property(name="pivot_Variable91", type=pivot_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IterateExp", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextType96: BinaryAssociation = BinaryAssociation(
    name="contextType96",
    ends={
        Property(name="pivot_Type97", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterType98: BinaryAssociation = BinaryAssociation(
    name="parameterType98",
    ends={
        Property(name="pivot_Type100", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType99", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
resultType101: BinaryAssociation = BinaryAssociation(
    name="resultType101",
    ends={
        Property(name="pivot_Type103", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType102", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
in104: BinaryAssociation = BinaryAssociation(
    name="in104",
    ends={
        Property(name="pivot_OCLExpression105", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable106: BinaryAssociation = BinaryAssociation(
    name="variable106",
    ends={
        Property(name="pivot_Variable108", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp107", type=pivot_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedPrecedence109: BinaryAssociation = BinaryAssociation(
    name="ownedPrecedence109",
    ends={
        Property(name="pivot_Library", type=pivot_Precedence, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="pivot_Precedence", type=pivot_Library, multiplicity=Multiplicity(1, 1))
    }
)
body110: BinaryAssociation = BinaryAssociation(
    name="body110",
    ends={
        Property(name="pivot_OCLExpression111", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument118: BinaryAssociation = BinaryAssociation(
    name="argument118",
    ends={
        Property(name="pivot_OCLExpression119", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledOperation120: BinaryAssociation = BinaryAssociation(
    name="calledOperation120",
    ends={
        Property(name="pivot_CallOperationAction122", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp121", type=pivot_CallOperationAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentSignal123: BinaryAssociation = BinaryAssociation(
    name="sentSignal123",
    ends={
        Property(name="pivot_SendSignalAction", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp124", type=pivot_SendSignalAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target125: BinaryAssociation = BinaryAssociation(
    name="target125",
    ends={
        Property(name="pivot_OCLExpression127", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp126", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredOperation128: BinaryAssociation = BinaryAssociation(
    name="referredOperation128",
    ends={
        Property(name="pivot_Operation129", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
referredSignal130: BinaryAssociation = BinaryAssociation(
    name="referredSignal130",
    ends={
        Property(name="pivot_Signal", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType131", type=pivot_Signal, multiplicity=Multiplicity(0, 1))
    }
)
instanceType132: BinaryAssociation = BinaryAssociation(
    name="instanceType132",
    ends={
        Property(name="pivot_Type133", type=pivot_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Metaclass", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
iterator112: BinaryAssociation = BinaryAssociation(
    name="iterator112",
    ends={
        Property(name="pivot_Variable114", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp113", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredIteration115: BinaryAssociation = BinaryAssociation(
    name="referredIteration115",
    ends={
        Property(name="pivot_Iteration117", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp116", type=pivot_Iteration, multiplicity=Multiplicity(0, 1))
    }
)
ownedRule134: BinaryAssociation = BinaryAssociation(
    name="ownedRule134",
    ends={
        Property(name="pivot_Constraint136", type=pivot_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Namespace135", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
navigationSource137: BinaryAssociation = BinaryAssociation(
    name="navigationSource137",
    ends={
        Property(name="pivot_Property138", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
qualifier139: BinaryAssociation = BinaryAssociation(
    name="qualifier139",
    ends={
        Property(name="pivot_OCLExpression141", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp140", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999))
    }
)
expressionInOCL142: BinaryAssociation = BinaryAssociation(
    name="expressionInOCL142",
    ends={
        Property(name="pivot_ExpressionInOCL144", type=pivot_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OpaqueExpression143", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExpression145: BinaryAssociation = BinaryAssociation(
    name="bodyExpression145",
    ends={
        Property(name="pivot_OpaqueExpression147", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation146", type=pivot_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class148: BinaryAssociation = BinaryAssociation(
    name="class148",
    ends={
        Property(name="pivot_Class150", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation149", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
postcondition153: BinaryAssociation = BinaryAssociation(
    name="postcondition153",
    ends={
        Property(name="pivot_Constraint155", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation154", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precedence156: BinaryAssociation = BinaryAssociation(
    name="precedence156",
    ends={
        Property(name="pivot_Precedence158", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation157", type=pivot_Precedence, multiplicity=Multiplicity(0, 1))
    }
)
precondition159: BinaryAssociation = BinaryAssociation(
    name="precondition159",
    ends={
        Property(name="pivot_Constraint161", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation160", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException162: BinaryAssociation = BinaryAssociation(
    name="raisedException162",
    ends={
        Property(name="pivot_Type164", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation163", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedOperation166: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation166",
    ends={
        Property(name="pivot_Operation167", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation165", type=pivot_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter151: BinaryAssociation = BinaryAssociation(
    name="ownedParameter151",
    ends={
        Property(name="Parameter", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningType152: BinaryAssociation = BinaryAssociation(
    name="owningType152",
    ends={
        Property(name="Type", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty173: BinaryAssociation = BinaryAssociation(
    name="referredProperty173",
    ends={
        Property(name="pivot_Property174", type=pivot_OppositePropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OppositePropertyCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
importedPackage176: BinaryAssociation = BinaryAssociation(
    name="importedPackage176",
    ends={
        Property(name="pivot_Package", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Package175", type=pivot_Package, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage178: BinaryAssociation = BinaryAssociation(
    name="nestedPackage178",
    ends={
        Property(name="Package", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage180: BinaryAssociation = BinaryAssociation(
    name="nestingPackage180",
    ends={
        Property(name="Package181", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType182: BinaryAssociation = BinaryAssociation(
    name="ownedType182",
    ends={
        Property(name="Type183", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=pivot_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument168: BinaryAssociation = BinaryAssociation(
    name="argument168",
    ends={
        Property(name="pivot_OCLExpression169", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation170: BinaryAssociation = BinaryAssociation(
    name="referredOperation170",
    ends={
        Property(name="pivot_Operation172", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp171", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
operation185: BinaryAssociation = BinaryAssociation(
    name="operation185",
    ends={
        Property(name="Operation", type=pivot_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
owningTemplateParameter186: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter186",
    ends={
        Property(name="TemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameteredElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter187: BinaryAssociation = BinaryAssociation(
    name="templateParameter187",
    ends={
        Property(name="TemplateParameter188", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
profileApplication184: BinaryAssociation = BinaryAssociation(
    name="profileApplication184",
    ends={
        Property(name="ProfileApplication", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="applyingPackage", type=pivot_ProfileApplication, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appliedProfile191: BinaryAssociation = BinaryAssociation(
    name="appliedProfile191",
    ends={
        Property(name="Profile", type=pivot_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="application", type=pivot_Profile, multiplicity=Multiplicity(1, 1))
    }
)
applyingPackage192: BinaryAssociation = BinaryAssociation(
    name="applyingPackage192",
    ends={
        Property(name="Package193", type=pivot_ProfileApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="profileApplication", type=pivot_Package, multiplicity=Multiplicity(1, 1))
    }
)
associationClass194: BinaryAssociation = BinaryAssociation(
    name="associationClass194",
    ends={
        Property(name="AssociationClass", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="unownedAttribute", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
class195: BinaryAssociation = BinaryAssociation(
    name="class195",
    ends={
        Property(name="pivot_Class197", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property196", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
defaultExpression198: BinaryAssociation = BinaryAssociation(
    name="defaultExpression198",
    ends={
        Property(name="pivot_OpaqueExpression200", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property199", type=pivot_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
application189: BinaryAssociation = BinaryAssociation(
    name="application189",
    ends={
        Property(name="ProfileApplication190", type=pivot_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="appliedProfile", type=pivot_ProfileApplication, multiplicity=Multiplicity(0, 9999))
    }
)
keys202: BinaryAssociation = BinaryAssociation(
    name="keys202",
    ends={
        Property(name="pivot_Property203", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property201", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
opposite205: BinaryAssociation = BinaryAssociation(
    name="opposite205",
    ends={
        Property(name="pivot_Property206", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property204", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningType207: BinaryAssociation = BinaryAssociation(
    name="owningType207",
    ends={
        Property(name="Type208", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
redefinedProperty210: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty210",
    ends={
        Property(name="pivot_Property211", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property209", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
referredProperty213: BinaryAssociation = BinaryAssociation(
    name="referredProperty213",
    ends={
        Property(name="pivot_Property214", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property212", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
subsettedProperty216: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty216",
    ends={
        Property(name="pivot_Property217", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property215", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
referredProperty218: BinaryAssociation = BinaryAssociation(
    name="referredProperty218",
    ends={
        Property(name="pivot_Property219", type=pivot_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_PropertyCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
state220: BinaryAssociation = BinaryAssociation(
    name="state220",
    ends={
        Property(name="State221", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="connectionPoint", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine222: BinaryAssociation = BinaryAssociation(
    name="stateMachine222",
    ends={
        Property(name="pivot_StateMachine", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Pseudostate223", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion225: BinaryAssociation = BinaryAssociation(
    name="extendedRegion225",
    ends={
        Property(name="pivot_Region", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Region224", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
state226: BinaryAssociation = BinaryAssociation(
    name="state226",
    ends={
        Property(name="State227", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine228: BinaryAssociation = BinaryAssociation(
    name="stateMachine228",
    ends={
        Property(name="StateMachine", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="region229", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
subvertex230: BinaryAssociation = BinaryAssociation(
    name="subvertex230",
    ends={
        Property(name="Vertex", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=pivot_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition231: BinaryAssociation = BinaryAssociation(
    name="transition231",
    ends={
        Property(name="Transition233", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container232", type=pivot_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports234: BinaryAssociation = BinaryAssociation(
    name="imports234",
    ends={
        Property(name="pivot_Import235", type=pivot_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Root", type=pivot_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage236: BinaryAssociation = BinaryAssociation(
    name="nestedPackage236",
    ends={
        Property(name="pivot_Package238", type=pivot_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Root237", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal239: BinaryAssociation = BinaryAssociation(
    name="signal239",
    ends={
        Property(name="pivot_Signal241", type=pivot_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_SendSignalAction240", type=pivot_Signal, multiplicity=Multiplicity(1, 1))
    }
)
connection242: BinaryAssociation = BinaryAssociation(
    name="connection242",
    ends={
        Property(name="ConnectionPointReference", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectionPoint243: BinaryAssociation = BinaryAssociation(
    name="connectionPoint243",
    ends={
        Property(name="Pseudostate", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state244", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deferrableTrigger245: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger245",
    ends={
        Property(name="Trigger", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state246", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doActivity247: BinaryAssociation = BinaryAssociation(
    name="doActivity247",
    ends={
        Property(name="pivot_Behavior248", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit252: BinaryAssociation = BinaryAssociation(
    name="exit252",
    ends={
        Property(name="pivot_Behavior254", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State253", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
redefinedState256: BinaryAssociation = BinaryAssociation(
    name="redefinedState256",
    ends={
        Property(name="pivot_State257", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State255", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
region258: BinaryAssociation = BinaryAssociation(
    name="region258",
    ends={
        Property(name="Region", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state259", type=pivot_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateInvariant260: BinaryAssociation = BinaryAssociation(
    name="stateInvariant260",
    ends={
        Property(name="Constraint", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="owningState", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
submachine261: BinaryAssociation = BinaryAssociation(
    name="submachine261",
    ends={
        Property(name="StateMachine262", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
entry249: BinaryAssociation = BinaryAssociation(
    name="entry249",
    ends={
        Property(name="pivot_Behavior251", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State250", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredState263: BinaryAssociation = BinaryAssociation(
    name="referredState263",
    ends={
        Property(name="pivot_State264", type=pivot_StateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateExp", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
connectionPoint265: BinaryAssociation = BinaryAssociation(
    name="connectionPoint265",
    ends={
        Property(name="pivot_Pseudostate267", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine266", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedStateMachine269: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine269",
    ends={
        Property(name="pivot_StateMachine270", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine268", type=pivot_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
region271: BinaryAssociation = BinaryAssociation(
    name="region271",
    ends={
        Property(name="Region272", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine", type=pivot_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
submachineState273: BinaryAssociation = BinaryAssociation(
    name="submachineState273",
    ends={
        Property(name="State274", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=pivot_State, multiplicity=Multiplicity(0, 9999))
    }
)
extensionOfs275: BinaryAssociation = BinaryAssociation(
    name="extensionOfs275",
    ends={
        Property(name="TypeExtension", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotype", type=pivot_TypeExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundElement276: BinaryAssociation = BinaryAssociation(
    name="boundElement276",
    ends={
        Property(name="TemplateableElement", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution277: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution277",
    ends={
        Property(name="TemplateParameterSubstitution", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding278", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature279: BinaryAssociation = BinaryAssociation(
    name="signature279",
    ends={
        Property(name="pivot_TemplateSignature", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateBinding", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
default280: BinaryAssociation = BinaryAssociation(
    name="default280",
    ends={
        Property(name="pivot_ParameterableElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameteredElement284: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement284",
    ends={
        Property(name="ParameterableElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameteredElement285: BinaryAssociation = BinaryAssociation(
    name="parameteredElement285",
    ends={
        Property(name="ParameterableElement286", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature287: BinaryAssociation = BinaryAssociation(
    name="signature287",
    ends={
        Property(name="TemplateSignature", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter288", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
actual289: BinaryAssociation = BinaryAssociation(
    name="actual289",
    ends={
        Property(name="pivot_ParameterableElement290", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
formal291: BinaryAssociation = BinaryAssociation(
    name="formal291",
    ends={
        Property(name="pivot_TemplateParameter293", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution292", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual294: BinaryAssociation = BinaryAssociation(
    name="ownedActual294",
    ends={
        Property(name="pivot_ParameterableElement296", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution295", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding297: BinaryAssociation = BinaryAssociation(
    name="templateBinding297",
    ends={
        Property(name="TemplateBinding", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter298: BinaryAssociation = BinaryAssociation(
    name="ownedParameter298",
    ends={
        Property(name="TemplateParameter299", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
template300: BinaryAssociation = BinaryAssociation(
    name="template300",
    ends={
        Property(name="TemplateableElement301", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedDefault281: BinaryAssociation = BinaryAssociation(
    name="ownedDefault281",
    ends={
        Property(name="pivot_ParameterableElement283", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameter282", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedTemplateSignature302: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature302",
    ends={
        Property(name="TemplateSignature303", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=pivot_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding304: BinaryAssociation = BinaryAssociation(
    name="templateBinding304",
    ends={
        Property(name="TemplateBinding305", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=pivot_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unspecializedElement307: BinaryAssociation = BinaryAssociation(
    name="unspecializedElement307",
    ends={
        Property(name="pivot_TemplateableElement", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateableElement306", type=pivot_TemplateableElement, multiplicity=Multiplicity(0, 1))
    }
)
container308: BinaryAssociation = BinaryAssociation(
    name="container308",
    ends={
        Property(name="Region309", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=pivot_Region, multiplicity=Multiplicity(1, 1))
    }
)
effect310: BinaryAssociation = BinaryAssociation(
    name="effect310",
    ends={
        Property(name="Behavior", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition311", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard312: BinaryAssociation = BinaryAssociation(
    name="guard312",
    ends={
        Property(name="Constraint314", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition313", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source315: BinaryAssociation = BinaryAssociation(
    name="source315",
    ends={
        Property(name="Vertex316", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target317: BinaryAssociation = BinaryAssociation(
    name="target317",
    ends={
        Property(name="Vertex318", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
trigger319: BinaryAssociation = BinaryAssociation(
    name="trigger319",
    ends={
        Property(name="Trigger321", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition320", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state322: BinaryAssociation = BinaryAssociation(
    name="state322",
    ends={
        Property(name="State323", type=pivot_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="deferrableTrigger", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
transition324: BinaryAssociation = BinaryAssociation(
    name="transition324",
    ends={
        Property(name="Transition325", type=pivot_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="trigger", type=pivot_Transition, multiplicity=Multiplicity(0, 1))
    }
)
part326: BinaryAssociation = BinaryAssociation(
    name="part326",
    ends={
        Property(name="pivot_TupleLiteralPart", type=pivot_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralExp", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExpression327: BinaryAssociation = BinaryAssociation(
    name="initExpression327",
    ends={
        Property(name="pivot_OCLExpression329", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralPart328", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedBys330: BinaryAssociation = BinaryAssociation(
    name="extendedBys330",
    ends={
        Property(name="TypeExtension331", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=pivot_TypeExtension, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute332: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute332",
    ends={
        Property(name="Property333", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=pivot_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedInvariant334: BinaryAssociation = BinaryAssociation(
    name="ownedInvariant334",
    ends={
        Property(name="pivot_Constraint336", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Type335", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation337: BinaryAssociation = BinaryAssociation(
    name="ownedOperation337",
    ends={
        Property(name="Operation339", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType338", type=pivot_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package340: BinaryAssociation = BinaryAssociation(
    name="package340",
    ends={
        Property(name="Package341", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
superClass343: BinaryAssociation = BinaryAssociation(
    name="superClass343",
    ends={
        Property(name="pivot_Type344", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Type342", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
stereotype347: BinaryAssociation = BinaryAssociation(
    name="stereotype347",
    ends={
        Property(name="Stereotype", type=pivot_TypeExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionOfs", type=pivot_Stereotype, multiplicity=Multiplicity(1, 1))
    }
)
type348: BinaryAssociation = BinaryAssociation(
    name="type348",
    ends={
        Property(name="Type349", type=pivot_TypeExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extendedBys", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
constrainingType350: BinaryAssociation = BinaryAssociation(
    name="constrainingType350",
    ends={
        Property(name="pivot_Type351", type=pivot_TypeTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypeTemplateParameter", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type352: BinaryAssociation = BinaryAssociation(
    name="type352",
    ends={
        Property(name="pivot_Type353", type=pivot_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypedElement", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
referredType345: BinaryAssociation = BinaryAssociation(
    name="referredType345",
    ends={
        Property(name="pivot_Type346", type=pivot_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypeExp", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound354: BinaryAssociation = BinaryAssociation(
    name="lowerBound354",
    ends={
        Property(name="pivot_Type355", type=pivot_UnspecifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_UnspecifiedType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
upperBound356: BinaryAssociation = BinaryAssociation(
    name="upperBound356",
    ends={
        Property(name="pivot_Type358", type=pivot_UnspecifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_UnspecifiedType357", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
outgoing370: BinaryAssociation = BinaryAssociation(
    name="outgoing370",
    ends={
        Property(name="Transition371", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
initExpression359: BinaryAssociation = BinaryAssociation(
    name="initExpression359",
    ends={
        Property(name="pivot_OCLExpression361", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable360", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
representedParameter362: BinaryAssociation = BinaryAssociation(
    name="representedParameter362",
    ends={
        Property(name="pivot_Parameter364", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable363", type=pivot_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable365: BinaryAssociation = BinaryAssociation(
    name="referredVariable365",
    ends={
        Property(name="pivot_VariableDeclaration", type=pivot_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_VariableExp", type=pivot_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
container366: BinaryAssociation = BinaryAssociation(
    name="container366",
    ends={
        Property(name="Region367", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
incoming368: BinaryAssociation = BinaryAssociation(
    name="incoming368",
    ends={
        Property(name="Transition369", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
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
gen_pivot_Class_Type = Generalization(general=Type, specific=pivot_Class)
gen_pivot_Class_Namespace = Generalization(general=Namespace, specific=pivot_Class)
gen_pivot_CallOperationAction_NamedElement = Generalization(general=NamedElement, specific=pivot_CallOperationAction)
gen_pivot_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_CollectionLiteralExp)
gen_pivot_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionItem)
gen_pivot_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionRange)
gen_pivot_CollectionType_DataType = Generalization(general=DataType, specific=pivot_CollectionType)
gen_pivot_Comment_Element = Generalization(general=Element, specific=pivot_Comment)
gen_pivot_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=pivot_CollectionLiteralPart)
gen_pivot_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=pivot_ConnectionPointReference)
gen_pivot_Constraint_NamedElement = Generalization(general=NamedElement, specific=pivot_Constraint)
gen_pivot_ConstructorExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_ConstructorExp)
gen_pivot_ConstructorPart_TypedElement = Generalization(general=TypedElement, specific=pivot_ConstructorPart)
gen_pivot_Detail_NamedElement = Generalization(general=NamedElement, specific=pivot_Detail)
gen_pivot_DynamicElement_Element = Generalization(general=Element, specific=pivot_DynamicElement)
gen_pivot_DynamicProperty_Element = Generalization(general=Element, specific=pivot_DynamicProperty)
gen_pivot_DataType_Class = Generalization(general=Class_, specific=pivot_DataType)
gen_pivot_Element_Visitable = Generalization(general=Visitable, specific=pivot_Element)
gen_pivot_DynamicType_Type = Generalization(general=Type, specific=pivot_DynamicType)
gen_pivot_DynamicType_DynamicElement = Generalization(general=DynamicElement, specific=pivot_DynamicType)
gen_pivot_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_EnumLiteralExp)
gen_pivot_ElementExtension_Type = Generalization(general=Type, specific=pivot_ElementExtension)
gen_pivot_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=pivot_EnumerationLiteral)
gen_pivot_ExpressionInOCL_OpaqueExpression = Generalization(general=OpaqueExpression, specific=pivot_ExpressionInOCL)
gen_pivot_Enumeration_DataType = Generalization(general=DataType, specific=pivot_Enumeration)
gen_pivot_Feature_TypedMultiplicityElement = Generalization(general=TypedMultiplicityElement, specific=pivot_Feature)
gen_pivot_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=pivot_FeatureCallExp)
gen_pivot_FinalState_State = Generalization(general=State, specific=pivot_FinalState)
gen_pivot_IfExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_IfExp)
gen_pivot_Import_NamedElement = Generalization(general=NamedElement, specific=pivot_Import)
gen_pivot_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_IntegerLiteralExp)
gen_pivot_IterateExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IterateExp)
gen_pivot_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_InvalidLiteralExp)
gen_pivot_InvalidType_Class = Generalization(general=Class_, specific=pivot_InvalidType)
gen_pivot_IterateExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IterateExp)
gen_pivot_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IteratorExp)
gen_pivot_IteratorExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IteratorExp)
gen_pivot_Iteration_Operation = Generalization(general=Operation, specific=pivot_Iteration)
gen_pivot_LambdaType_DataType = Generalization(general=DataType, specific=pivot_LambdaType)
gen_pivot_LetExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LetExp)
gen_pivot_Library_Package = Generalization(general=Package, specific=pivot_Library)
gen_pivot_LiteralExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LiteralExp)
gen_pivot_LoopExp_CallExp = Generalization(general=CallExp, specific=pivot_LoopExp)
gen_pivot_MessageType_Type = Generalization(general=Type, specific=pivot_MessageType)
gen_pivot_Metaclass_Class = Generalization(general=Class_, specific=pivot_Metaclass)
gen_pivot_MessageExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_MessageExp)
gen_pivot_Namespace_NamedElement = Generalization(general=NamedElement, specific=pivot_Namespace)
gen_pivot_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_NavigationCallExp)
gen_pivot_NullLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NullLiteralExp)
gen_pivot_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NumericLiteralExp)
gen_pivot_OCLExpression_TypedElement = Generalization(general=TypedElement, specific=pivot_OCLExpression)
gen_pivot_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=pivot_OpaqueExpression)
gen_pivot_NamedElement_Element = Generalization(general=Element, specific=pivot_NamedElement)
gen_pivot_NamedElement_Nameable = Generalization(general=Nameable, specific=pivot_NamedElement)
gen_pivot_Operation_Feature = Generalization(general=Feature, specific=pivot_Operation)
gen_pivot_Operation_Namespace = Generalization(general=Namespace, specific=pivot_Operation)
gen_pivot_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Operation)
gen_pivot_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Operation)
gen_pivot_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_OperationCallExp)
gen_pivot_OperationCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_OperationCallExp)
gen_pivot_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=pivot_OperationTemplateParameter)
gen_pivot_OppositePropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_OppositePropertyCallExp)
gen_pivot_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=pivot_OrderedSetType)
gen_pivot_Package_Namespace = Generalization(general=Namespace, specific=pivot_Package)
gen_pivot_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Package)
gen_pivot_Parameter_TypedMultiplicityElement = Generalization(general=TypedMultiplicityElement, specific=pivot_Parameter)
gen_pivot_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Parameter)
gen_pivot_ParameterableElement_Element = Generalization(general=Element, specific=pivot_ParameterableElement)
gen_pivot_Precedence_NamedElement = Generalization(general=NamedElement, specific=pivot_Precedence)
gen_pivot_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_PrimitiveLiteralExp)
gen_pivot_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_PackageableElement)
gen_pivot_ProfileApplication_Element = Generalization(general=Element, specific=pivot_ProfileApplication)
gen_pivot_Property_Feature = Generalization(general=Feature, specific=pivot_Property)
gen_pivot_Property_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Property)
gen_pivot_PrimitiveType_DataType = Generalization(general=DataType, specific=pivot_PrimitiveType)
gen_pivot_Profile_Package = Generalization(general=Package, specific=pivot_Profile)
gen_pivot_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_PropertyCallExp)
gen_pivot_PropertyCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_PropertyCallExp)
gen_pivot_Pseudostate_Vertex = Generalization(general=Vertex, specific=pivot_Pseudostate)
gen_pivot_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_RealLiteralExp)
gen_pivot_Region_Namespace = Generalization(general=Namespace, specific=pivot_Region)
gen_pivot_Root_Namespace = Generalization(general=Namespace, specific=pivot_Root)
gen_pivot_SelfType_Class = Generalization(general=Class_, specific=pivot_SelfType)
gen_pivot_SendSignalAction_NamedElement = Generalization(general=NamedElement, specific=pivot_SendSignalAction)
gen_pivot_SequenceType_CollectionType = Generalization(general=CollectionType, specific=pivot_SequenceType)
gen_pivot_SetType_CollectionType = Generalization(general=CollectionType, specific=pivot_SetType)
gen_pivot_Signal_NamedElement = Generalization(general=NamedElement, specific=pivot_Signal)
gen_pivot_State_Vertex = Generalization(general=Vertex, specific=pivot_State)
gen_pivot_State_Namespace = Generalization(general=Namespace, specific=pivot_State)
gen_pivot_StateExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_StateExp)
gen_pivot_StateMachine_Behavior = Generalization(general=Behavior, specific=pivot_StateMachine)
gen_pivot_Stereotype_Class = Generalization(general=Class_, specific=pivot_Stereotype)
gen_pivot_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_StringLiteralExp)
gen_pivot_TemplateBinding_Element = Generalization(general=Element, specific=pivot_TemplateBinding)
gen_pivot_TemplateParameter_Element = Generalization(general=Element, specific=pivot_TemplateParameter)
gen_pivot_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=pivot_TemplateParameterSubstitution)
gen_pivot_TemplateParameterType_Type = Generalization(general=Type, specific=pivot_TemplateParameterType)
gen_pivot_TemplateSignature_Element = Generalization(general=Element, specific=pivot_TemplateSignature)
gen_pivot_TemplateableElement_Element = Generalization(general=Element, specific=pivot_TemplateableElement)
gen_pivot_Transition_Namespace = Generalization(general=Namespace, specific=pivot_Transition)
gen_pivot_Trigger_NamedElement = Generalization(general=NamedElement, specific=pivot_Trigger)
gen_pivot_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_TupleLiteralExp)
gen_pivot_TupleLiteralPart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_TupleLiteralPart)
gen_pivot_TupleType_DataType = Generalization(general=DataType, specific=pivot_TupleType)
gen_pivot_Type_NamedElement = Generalization(general=NamedElement, specific=pivot_Type)
gen_pivot_Type_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Type)
gen_pivot_Type_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Type)
gen_pivot_TypeExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_TypeExp)
gen_pivot_TypeExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_TypeExp)
gen_pivot_TypeExtension_Element = Generalization(general=Element, specific=pivot_TypeExtension)
gen_pivot_TypeTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=pivot_TypeTemplateParameter)
gen_pivot_TypedElement_NamedElement = Generalization(general=NamedElement, specific=pivot_TypedElement)
gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_UnlimitedNaturalLiteralExp)
gen_pivot_UnspecifiedType_Class = Generalization(general=Class_, specific=pivot_UnspecifiedType)
gen_pivot_UnspecifiedValueExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_UnspecifiedValueExp)
gen_pivot_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=pivot_ValueSpecification)
gen_pivot_ValueSpecification_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_ValueSpecification)
gen_pivot_TypedMultiplicityElement_TypedElement = Generalization(general=TypedElement, specific=pivot_TypedMultiplicityElement)
gen_pivot_Variable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Variable)
gen_pivot_VoidType_Class = Generalization(general=Class_, specific=pivot_VoidType)
gen_pivot_VariableDeclaration_TypedElement = Generalization(general=TypedElement, specific=pivot_VariableDeclaration)
gen_pivot_VariableExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_VariableExp)
gen_pivot_VariableExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_VariableExp)
gen_pivot_Vertex_NamedElement = Generalization(general=NamedElement, specific=pivot_Vertex)

# Domain Model
domain_model = DomainModel(
    name="pivot",
    types={pivot_Detail, pivot_AnyType, Class_, pivot_AssociationClass, pivot_Property, pivot_AssociationClassCallExp, NavigationCallExp, pivot_Annotation, NamedElement, pivot_Element, pivot_Transition, pivot_BooleanLiteralExp, PrimitiveLiteralExp, pivot_CallExp, OCLExpression, pivot_BagType, CollectionType, pivot_Behavior, pivot_Class, Type, Namespace, pivot_OCLExpression, pivot_CallOperationAction, pivot_Operation, pivot_CollectionLiteralExp, LiteralExp, pivot_CollectionItem, CollectionLiteralPart, pivot_CollectionRange, pivot_CollectionType, DataType, pivot_Type, pivot_Comment, Element, pivot_CollectionLiteralPart, TypedElement, pivot_ConnectionPointReference, Vertex, pivot_Pseudostate, pivot_Constraint, pivot_Namespace, pivot_State, pivot_OpaqueExpression, pivot_ConstructorExp, pivot_ConstructorPart, pivot_DynamicElement, pivot_DynamicProperty, pivot_DataType, Visitable, pivot_ElementExtension, pivot_DynamicType, DynamicElement, pivot_Stereotype, pivot_EnumLiteralExp, pivot_EnumerationLiteral, pivot_ExpressionInOCL, OpaqueExpression, pivot_Variable, pivot_Enumeration, pivot_Feature, TypedMultiplicityElement, pivot_FeatureCallExp, CallExp, pivot_FinalState, State, pivot_IfExp, pivot_Import, pivot_IntegerLiteralExp, NumericLiteralExp, pivot_InvalidLiteralExp, pivot_InvalidType, pivot_IterateExp, LoopExp, ReferringElement, pivot_Parameter, pivot_IteratorExp, pivot_Iteration, Operation, pivot_LambdaType, pivot_LetExp, pivot_Library, Package, pivot_Precedence, pivot_LiteralExp, pivot_LoopExp, pivot_SendSignalAction, pivot_MessageType, pivot_Signal, pivot_Metaclass, pivot_MessageExp, pivot_NavigationCallExp, FeatureCallExp, pivot_NullLiteralExp, pivot_NumericLiteralExp, ValueSpecification, pivot_MorePivotable, pivot_Nameable, pivot_NamedElement, Nameable, Feature, TemplateableElement, ParameterableElement, pivot_OperationCallExp, pivot_OperationTemplateParameter, TemplateParameter, pivot_OppositePropertyCallExp, pivot_OrderedSetType, pivot_Package, VariableDeclaration, pivot_ParameterableElement, pivot_TemplateParameter, pivot_Pivotable, pivot_PrimitiveLiteralExp, pivot_ProfileApplication, pivot_PackageableElement, pivot_PrimitiveType, pivot_Profile, pivot_PropertyCallExp, pivot_StateMachine, pivot_RealLiteralExp, pivot_ReferringElement, pivot_Region, pivot_Vertex, pivot_Root, pivot_SelfType, pivot_SequenceType, pivot_SetType, pivot_Trigger, pivot_StateExp, Behavior, pivot_TypeExtension, pivot_StringLiteralExp, pivot_TemplateBinding, pivot_TemplateableElement, pivot_TemplateParameterSubstitution, pivot_TemplateSignature, pivot_TemplateParameterType, pivot_TupleLiteralExp, pivot_TupleLiteralPart, pivot_TupleType, pivot_TypeExp, pivot_TypeTemplateParameter, pivot_TypedElement, pivot_UnlimitedNaturalLiteralExp, pivot_UnspecifiedType, pivot_UnspecifiedValueExp, pivot_ValueSpecification, pivot_TypedMultiplicityElement, pivot_Visitable, pivot_Visitor, pivot_VoidType, pivot_VariableDeclaration, pivot_VariableExp, CollectionKind, PseudostateKind, AssociativityKind, TransitionKind},
    associations={ownedContent0, ownedDetail1, reference3, unownedAttribute6, transition8, referredAssociationClass7, operation10, nestedType12, source9, item15, ownedBehavior13, first18, last20, elementType23, part17, entry26, exit27, annotatedElement24, constrainedElement31, context33, state30, specification40, transition42, part44, owningState35, redefinedConstraint38, behavioralType50, metaType52, referredProperty54, initExpression45, referredProperty48, extension58, ownedAnnotation60, ownedProperty56, base65, stereotype66, ownedComment62, enumeration69, bodyExpression70, contextVariable72, referredEnumLiteral67, ownedLiteral68, parameterVariable74, resultVariable77, elseExpression82, thenExpression85, importedNamespace88, condition80, ownedAccumulator92, ownedIterator93, result90, contextType96, parameterType98, resultType101, in104, variable106, ownedPrecedence109, body110, argument118, calledOperation120, sentSignal123, target125, referredOperation128, referredSignal130, instanceType132, iterator112, referredIteration115, ownedRule134, navigationSource137, qualifier139, expressionInOCL142, bodyExpression145, class148, postcondition153, precedence156, precondition159, raisedException162, redefinedOperation166, ownedParameter151, owningType152, referredProperty173, importedPackage176, nestedPackage178, nestingPackage180, ownedType182, argument168, referredOperation170, operation185, owningTemplateParameter186, templateParameter187, profileApplication184, appliedProfile191, applyingPackage192, associationClass194, class195, defaultExpression198, application189, keys202, opposite205, owningType207, redefinedProperty210, referredProperty213, subsettedProperty216, referredProperty218, state220, stateMachine222, extendedRegion225, state226, stateMachine228, subvertex230, transition231, imports234, nestedPackage236, signal239, connection242, connectionPoint243, deferrableTrigger245, doActivity247, exit252, redefinedState256, region258, stateInvariant260, submachine261, entry249, referredState263, connectionPoint265, extendedStateMachine269, region271, submachineState273, extensionOfs275, boundElement276, parameterSubstitution277, signature279, default280, ownedParameteredElement284, parameteredElement285, signature287, actual289, formal291, ownedActual294, templateBinding297, ownedParameter298, template300, ownedDefault281, ownedTemplateSignature302, templateBinding304, unspecializedElement307, container308, effect310, guard312, source315, target317, trigger319, state322, transition324, part326, initExpression327, extendedBys330, ownedAttribute332, ownedInvariant334, ownedOperation337, package340, superClass343, stereotype347, type348, constrainingType350, type352, referredType345, lowerBound354, upperBound356, outgoing370, initExpression359, representedParameter362, referredVariable365, container366, incoming368},
    generalizations={gen_pivot_AnyType_Class, gen_pivot_AssociationClass_Class, gen_pivot_AssociationClassCallExp_NavigationCallExp, gen_pivot_Annotation_NamedElement, gen_pivot_BooleanLiteralExp_PrimitiveLiteralExp, gen_pivot_CallExp_OCLExpression, gen_pivot_BagType_CollectionType, gen_pivot_Behavior_Class, gen_pivot_Class_Type, gen_pivot_Class_Namespace, gen_pivot_CallOperationAction_NamedElement, gen_pivot_CollectionLiteralExp_LiteralExp, gen_pivot_CollectionItem_CollectionLiteralPart, gen_pivot_CollectionRange_CollectionLiteralPart, gen_pivot_CollectionType_DataType, gen_pivot_Comment_Element, gen_pivot_CollectionLiteralPart_TypedElement, gen_pivot_ConnectionPointReference_Vertex, gen_pivot_Constraint_NamedElement, gen_pivot_ConstructorExp_OCLExpression, gen_pivot_ConstructorPart_TypedElement, gen_pivot_Detail_NamedElement, gen_pivot_DynamicElement_Element, gen_pivot_DynamicProperty_Element, gen_pivot_DataType_Class, gen_pivot_Element_Visitable, gen_pivot_DynamicType_Type, gen_pivot_DynamicType_DynamicElement, gen_pivot_EnumLiteralExp_LiteralExp, gen_pivot_ElementExtension_Type, gen_pivot_EnumerationLiteral_NamedElement, gen_pivot_ExpressionInOCL_OpaqueExpression, gen_pivot_Enumeration_DataType, gen_pivot_Feature_TypedMultiplicityElement, gen_pivot_FeatureCallExp_CallExp, gen_pivot_FinalState_State, gen_pivot_IfExp_OCLExpression, gen_pivot_Import_NamedElement, gen_pivot_IntegerLiteralExp_NumericLiteralExp, gen_pivot_IterateExp_ReferringElement, gen_pivot_InvalidLiteralExp_LiteralExp, gen_pivot_InvalidType_Class, gen_pivot_IterateExp_LoopExp, gen_pivot_IteratorExp_LoopExp, gen_pivot_IteratorExp_ReferringElement, gen_pivot_Iteration_Operation, gen_pivot_LambdaType_DataType, gen_pivot_LetExp_OCLExpression, gen_pivot_Library_Package, gen_pivot_LiteralExp_OCLExpression, gen_pivot_LoopExp_CallExp, gen_pivot_MessageType_Type, gen_pivot_Metaclass_Class, gen_pivot_MessageExp_OCLExpression, gen_pivot_Namespace_NamedElement, gen_pivot_NavigationCallExp_FeatureCallExp, gen_pivot_NullLiteralExp_PrimitiveLiteralExp, gen_pivot_NumericLiteralExp_PrimitiveLiteralExp, gen_pivot_OCLExpression_TypedElement, gen_pivot_OpaqueExpression_ValueSpecification, gen_pivot_NamedElement_Element, gen_pivot_NamedElement_Nameable, gen_pivot_Operation_Feature, gen_pivot_Operation_Namespace, gen_pivot_Operation_TemplateableElement, gen_pivot_Operation_ParameterableElement, gen_pivot_OperationCallExp_FeatureCallExp, gen_pivot_OperationCallExp_ReferringElement, gen_pivot_OperationTemplateParameter_TemplateParameter, gen_pivot_OppositePropertyCallExp_NavigationCallExp, gen_pivot_OrderedSetType_CollectionType, gen_pivot_Package_Namespace, gen_pivot_Package_TemplateableElement, gen_pivot_Parameter_TypedMultiplicityElement, gen_pivot_Parameter_VariableDeclaration, gen_pivot_ParameterableElement_Element, gen_pivot_Precedence_NamedElement, gen_pivot_PrimitiveLiteralExp_LiteralExp, gen_pivot_PackageableElement_ParameterableElement, gen_pivot_ProfileApplication_Element, gen_pivot_Property_Feature, gen_pivot_Property_ParameterableElement, gen_pivot_PrimitiveType_DataType, gen_pivot_Profile_Package, gen_pivot_PropertyCallExp_NavigationCallExp, gen_pivot_PropertyCallExp_ReferringElement, gen_pivot_Pseudostate_Vertex, gen_pivot_RealLiteralExp_NumericLiteralExp, gen_pivot_Region_Namespace, gen_pivot_Root_Namespace, gen_pivot_SelfType_Class, gen_pivot_SendSignalAction_NamedElement, gen_pivot_SequenceType_CollectionType, gen_pivot_SetType_CollectionType, gen_pivot_Signal_NamedElement, gen_pivot_State_Vertex, gen_pivot_State_Namespace, gen_pivot_StateExp_OCLExpression, gen_pivot_StateMachine_Behavior, gen_pivot_Stereotype_Class, gen_pivot_StringLiteralExp_PrimitiveLiteralExp, gen_pivot_TemplateBinding_Element, gen_pivot_TemplateParameter_Element, gen_pivot_TemplateParameterSubstitution_Element, gen_pivot_TemplateParameterType_Type, gen_pivot_TemplateSignature_Element, gen_pivot_TemplateableElement_Element, gen_pivot_Transition_Namespace, gen_pivot_Trigger_NamedElement, gen_pivot_TupleLiteralExp_LiteralExp, gen_pivot_TupleLiteralPart_VariableDeclaration, gen_pivot_TupleType_DataType, gen_pivot_Type_NamedElement, gen_pivot_Type_TemplateableElement, gen_pivot_Type_ParameterableElement, gen_pivot_TypeExp_OCLExpression, gen_pivot_TypeExp_ReferringElement, gen_pivot_TypeExtension_Element, gen_pivot_TypeTemplateParameter_TemplateParameter, gen_pivot_TypedElement_NamedElement, gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp, gen_pivot_UnspecifiedType_Class, gen_pivot_UnspecifiedValueExp_OCLExpression, gen_pivot_ValueSpecification_TypedElement, gen_pivot_ValueSpecification_ParameterableElement, gen_pivot_TypedMultiplicityElement_TypedElement, gen_pivot_Variable_VariableDeclaration, gen_pivot_VoidType_Class, gen_pivot_VariableDeclaration_TypedElement, gen_pivot_VariableExp_OCLExpression, gen_pivot_VariableExp_ReferringElement, gen_pivot_Vertex_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)