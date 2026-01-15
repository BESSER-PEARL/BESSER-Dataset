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
            EnumerationLiteral(name="Left"),
			EnumerationLiteral(name="Right")
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

PseudostateKind: Enumeration = Enumeration(
    name="PseudostateKind",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="deepHistory"),
			EnumerationLiteral(name="shallowHistory"),
			EnumerationLiteral(name="join"),
			EnumerationLiteral(name="entryPoint"),
			EnumerationLiteral(name="exitPoint"),
			EnumerationLiteral(name="terminate"),
			EnumerationLiteral(name="fork"),
			EnumerationLiteral(name="junction"),
			EnumerationLiteral(name="choice")
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
pivot_Annotation = Class(name="pivot::Annotation")
NamedElement = Class(name="NamedElement")
pivot_AnyType = Class(name="pivot::AnyType")
Class_ = Class(name="Class")
pivot_AssociationClass = Class(name="pivot::AssociationClass")
pivot_Property = Class(name="pivot::Property")
pivot_AssociationClassCallExp = Class(name="pivot::AssociationClassCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
pivot_BagType = Class(name="pivot::BagType")
CollectionType = Class(name="CollectionType")
pivot_Behavior = Class(name="pivot::Behavior", is_abstract=True)
pivot_BooleanLiteralExp = Class(name="pivot::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
pivot_Element = Class(name="pivot::Element", is_abstract=True)
pivot_Detail = Class(name="pivot::Detail")
pivot_CallOperationAction = Class(name="pivot::CallOperationAction")
pivot_Operation = Class(name="pivot::Operation")
pivot_Class = Class(name="pivot::Class")
Type = Class(name="Type")
Namespace = Class(name="Namespace")
pivot_CallExp = Class(name="pivot::CallExp", is_abstract=True)
OCLExpression = Class(name="OCLExpression")
pivot_OCLExpression = Class(name="pivot::OCLExpression", is_abstract=True)
pivot_CollectionItem = Class(name="pivot::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
pivot_CollectionLiteralExp = Class(name="pivot::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
pivot_CollectionLiteralPart = Class(name="pivot::CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
pivot_CollectionRange = Class(name="pivot::CollectionRange")
pivot_Type = Class(name="pivot::Type")
pivot_Comment = Class(name="pivot::Comment")
Element = Class(name="Element")
pivot_ConnectionPointReference = Class(name="pivot::ConnectionPointReference")
Vertex = Class(name="Vertex")
pivot_Pseudostate = Class(name="pivot::Pseudostate")
pivot_CollectionType = Class(name="pivot::CollectionType")
DataType = Class(name="DataType")
pivot_Constraint = Class(name="pivot::Constraint")
pivot_OpaqueExpression = Class(name="pivot::OpaqueExpression")
pivot_Namespace = Class(name="pivot::Namespace", is_abstract=True)
pivot_State = Class(name="pivot::State")
pivot_DataType = Class(name="pivot::DataType")
pivot_DynamicElement = Class(name="pivot::DynamicElement")
pivot_DynamicProperty = Class(name="pivot::DynamicProperty")
pivot_ConstructorExp = Class(name="pivot::ConstructorExp")
pivot_ConstructorPart = Class(name="pivot::ConstructorPart")
Visitable = Class(name="Visitable")
pivot_ElementExtension = Class(name="pivot::ElementExtension")
pivot_DynamicType = Class(name="pivot::DynamicType")
DynamicElement = Class(name="DynamicElement")
pivot_EnumerationLiteral = Class(name="pivot::EnumerationLiteral")
pivot_Enumeration = Class(name="pivot::Enumeration")
pivot_EnumLiteralExp = Class(name="pivot::EnumLiteralExp")
pivot_Feature = Class(name="pivot::Feature", is_abstract=True)
TypedMultiplicityElement = Class(name="TypedMultiplicityElement")
pivot_FeatureCallExp = Class(name="pivot::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
pivot_FinalState = Class(name="pivot::FinalState")
State = Class(name="State")
pivot_ExpressionInOCL = Class(name="pivot::ExpressionInOCL")
OpaqueExpression = Class(name="OpaqueExpression")
pivot_Variable = Class(name="pivot::Variable")
pivot_Import = Class(name="pivot::Import")
pivot_IntegerLiteralExp = Class(name="pivot::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
pivot_IfExp = Class(name="pivot::IfExp")
pivot_Iteration = Class(name="pivot::Iteration")
Operation = Class(name="Operation")
pivot_InvalidLiteralExp = Class(name="pivot::InvalidLiteralExp")
pivot_InvalidType = Class(name="pivot::InvalidType")
pivot_IterateExp = Class(name="pivot::IterateExp")
LoopExp = Class(name="LoopExp")
ReferringElement = Class(name="ReferringElement")
pivot_Parameter = Class(name="pivot::Parameter")
pivot_IteratorExp = Class(name="pivot::IteratorExp")
pivot_LambdaType = Class(name="pivot::LambdaType")
pivot_LetExp = Class(name="pivot::LetExp")
pivot_Library = Class(name="pivot::Library")
Package = Class(name="Package")
pivot_Precedence = Class(name="pivot::Precedence")
pivot_LiteralExp = Class(name="pivot::LiteralExp", is_abstract=True)
pivot_LoopExp = Class(name="pivot::LoopExp", is_abstract=True)
pivot_MessageExp = Class(name="pivot::MessageExp")
pivot_SendSignalAction = Class(name="pivot::SendSignalAction")
pivot_MessageType = Class(name="pivot::MessageType")
pivot_Signal = Class(name="pivot::Signal")
pivot_Metaclass = Class(name="pivot::Metaclass")
pivot_MorePivotable = Class(name="pivot::MorePivotable", is_abstract=True)
pivot_Nameable = Class(name="pivot::Nameable", is_abstract=True)
pivot_NamedElement = Class(name="pivot::NamedElement", is_abstract=True)
Nameable = Class(name="Nameable")
pivot_NavigationCallExp = Class(name="pivot::NavigationCallExp", is_abstract=True)
FeatureCallExp = Class(name="FeatureCallExp")
pivot_NullLiteralExp = Class(name="pivot::NullLiteralExp")
pivot_NumericLiteralExp = Class(name="pivot::NumericLiteralExp", is_abstract=True)
ValueSpecification = Class(name="ValueSpecification")
Feature = Class(name="Feature")
TemplateableElement = Class(name="TemplateableElement")
ParameterableElement = Class(name="ParameterableElement")
pivot_OperationCallExp = Class(name="pivot::OperationCallExp")
pivot_OperationTemplateParameter = Class(name="pivot::OperationTemplateParameter")
TemplateParameter = Class(name="TemplateParameter")
pivot_OrderedSetType = Class(name="pivot::OrderedSetType")
pivot_Package = Class(name="pivot::Package")
pivot_PackageableElement = Class(name="pivot::PackageableElement", is_abstract=True)
VariableDeclaration = Class(name="VariableDeclaration")
pivot_ParameterableElement = Class(name="pivot::ParameterableElement", is_abstract=True)
pivot_TemplateParameter = Class(name="pivot::TemplateParameter")
pivot_Pivotable = Class(name="pivot::Pivotable", is_abstract=True)
pivot_PrimitiveLiteralExp = Class(name="pivot::PrimitiveLiteralExp", is_abstract=True)
pivot_PrimitiveType = Class(name="pivot::PrimitiveType")
pivot_Profile = Class(name="pivot::Profile")
pivot_PropertyCallExp = Class(name="pivot::PropertyCallExp")
pivot_RealLiteralExp = Class(name="pivot::RealLiteralExp")
pivot_StateMachine = Class(name="pivot::StateMachine")
pivot_Root = Class(name="pivot::Root")
pivot_ReferringElement = Class(name="pivot::ReferringElement", is_abstract=True)
pivot_Region = Class(name="pivot::Region")
pivot_Transition = Class(name="pivot::Transition")
pivot_Vertex = Class(name="pivot::Vertex", is_abstract=True)
pivot_SelfType = Class(name="pivot::SelfType")
pivot_SequenceType = Class(name="pivot::SequenceType")
pivot_SetType = Class(name="pivot::SetType")
pivot_Trigger = Class(name="pivot::Trigger")
Behavior = Class(name="Behavior")
pivot_StateExp = Class(name="pivot::StateExp")
pivot_StringLiteralExp = Class(name="pivot::StringLiteralExp")
pivot_TemplateBinding = Class(name="pivot::TemplateBinding")
pivot_TemplateSignature = Class(name="pivot::TemplateSignature")
pivot_TemplateParameterSubstitution = Class(name="pivot::TemplateParameterSubstitution")
pivot_TemplateableElement = Class(name="pivot::TemplateableElement", is_abstract=True)
pivot_Stereotype = Class(name="pivot::Stereotype")
pivot_TemplateParameterType = Class(name="pivot::TemplateParameterType")
pivot_TupleLiteralPart = Class(name="pivot::TupleLiteralPart")
pivot_TupleType = Class(name="pivot::TupleType")
pivot_TupleLiteralExp = Class(name="pivot::TupleLiteralExp")
pivot_TypeExp = Class(name="pivot::TypeExp")
pivot_TypedElement = Class(name="pivot::TypedElement", is_abstract=True)
pivot_TypedMultiplicityElement = Class(name="pivot::TypedMultiplicityElement", is_abstract=True)
pivot_TypeTemplateParameter = Class(name="pivot::TypeTemplateParameter")
pivot_UnlimitedNaturalLiteralExp = Class(name="pivot::UnlimitedNaturalLiteralExp")
pivot_UnspecifiedType = Class(name="pivot::UnspecifiedType")
pivot_UnspecifiedValueExp = Class(name="pivot::UnspecifiedValueExp")
pivot_ValueSpecification = Class(name="pivot::ValueSpecification", is_abstract=True)
pivot_VariableDeclaration = Class(name="pivot::VariableDeclaration", is_abstract=True)
pivot_VariableExp = Class(name="pivot::VariableExp")
pivot_Visitable = Class(name="pivot::Visitable", is_abstract=True)
pivot_Visitor = Class(name="pivot::Visitor", is_abstract=True)
pivot_VoidType = Class(name="pivot::VoidType")

# pivot_Annotation class attributes and methods

# NamedElement class attributes and methods

# pivot_AnyType class attributes and methods

# Class class attributes and methods

# pivot_AssociationClass class attributes and methods

# pivot_Property class attributes and methods
pivot_Property_isID: Property = Property(name="isID", type=StringType)
pivot_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
pivot_Property_default: Property = Property(name="default", type=StringType)
pivot_Property_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_Property_isDerived: Property = Property(name="isDerived", type=StringType)
pivot_Property_implicit: Property = Property(name="implicit", type=StringType)
pivot_Property_isResolveProxies: Property = Property(name="isResolveProxies", type=StringType)
pivot_Property_isTransient: Property = Property(name="isTransient", type=StringType)
pivot_Property_isUnsettable: Property = Property(name="isUnsettable", type=StringType)
pivot_Property_isVolatile: Property = Property(name="isVolatile", type=StringType)
pivot_Property_m_isAttribute: Method = Method(name="isAttribute", parameters={Parameter(name='p')}, type=StringType)
pivot_Property_m_CompatibleDefaultExpression: Method = Method(name="CompatibleDefaultExpression", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Property.attributes={pivot_Property_default, pivot_Property_isTransient, pivot_Property_isVolatile, pivot_Property_isUnsettable, pivot_Property_isDerived, pivot_Property_isReadOnly, pivot_Property_isComposite, pivot_Property_implicit, pivot_Property_isID, pivot_Property_isResolveProxies}
pivot_Property.methods={pivot_Property_m_isAttribute, pivot_Property_m_CompatibleDefaultExpression}

# pivot_AssociationClassCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# pivot_BagType class attributes and methods

# CollectionType class attributes and methods

# pivot_Behavior class attributes and methods

# pivot_BooleanLiteralExp class attributes and methods
pivot_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
pivot_BooleanLiteralExp_m_TypeIsBoolean: Method = Method(name="TypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_BooleanLiteralExp.attributes={pivot_BooleanLiteralExp_booleanSymbol}
pivot_BooleanLiteralExp.methods={pivot_BooleanLiteralExp_m_TypeIsBoolean}

# PrimitiveLiteralExp class attributes and methods

# pivot_Element class attributes and methods
pivot_Element_m_allOwnedElements: Method = Method(name="allOwnedElements", parameters={}, type=Element)
pivot_Element_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='stereotype'), Parameter(name='propertyName')}, type=Element)
pivot_Element.methods={pivot_Element_m_allOwnedElements, pivot_Element_m_getValue}

# pivot_Detail class attributes and methods
pivot_Detail_value: Property = Property(name="value", type=StringType)
pivot_Detail.attributes={pivot_Detail_value}

# pivot_CallOperationAction class attributes and methods

# pivot_Operation class attributes and methods
pivot_Operation_isInvalidating: Property = Property(name="isInvalidating", type=StringType)
pivot_Operation_isValidating: Property = Property(name="isValidating", type=StringType)
pivot_Operation_m_CompatibleReturn: Method = Method(name="CompatibleReturn", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_LoadableImplementation: Method = Method(name="LoadableImplementation", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_UniquePreconditionName: Method = Method(name="UniquePreconditionName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation_m_UniquePostconditionName: Method = Method(name="UniquePostconditionName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Operation.attributes={pivot_Operation_isValidating, pivot_Operation_isInvalidating}
pivot_Operation.methods={pivot_Operation_m_CompatibleReturn, pivot_Operation_m_UniquePreconditionName, pivot_Operation_m_LoadableImplementation, pivot_Operation_m_UniquePostconditionName}

# pivot_Class class attributes and methods
pivot_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
pivot_Class_isInterface: Property = Property(name="isInterface", type=StringType)
pivot_Class.attributes={pivot_Class_isInterface, pivot_Class_isAbstract}

# Type class attributes and methods

# Namespace class attributes and methods

# pivot_CallExp class attributes and methods
pivot_CallExp_implicit: Property = Property(name="implicit", type=StringType)
pivot_CallExp.attributes={pivot_CallExp_implicit}

# OCLExpression class attributes and methods

# pivot_OCLExpression class attributes and methods

# pivot_CollectionItem class attributes and methods
pivot_CollectionItem_m_TypeIsItemType: Method = Method(name="TypeIsItemType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionItem.methods={pivot_CollectionItem_m_TypeIsItemType}

# CollectionLiteralPart class attributes and methods

# pivot_CollectionLiteralExp class attributes and methods
pivot_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
pivot_CollectionLiteralExp_m_CollectionKindIsConcrete: Method = Method(name="CollectionKindIsConcrete", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_SetKindIsSet: Method = Method(name="SetKindIsSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_SequenceKindIsSequence: Method = Method(name="SequenceKindIsSequence", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_CollectionLiteralExp_m_BagKindIsBag: Method = Method(name="BagKindIsBag", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp_m_OrderedSetKindIsOrderedSet: Method = Method(name="OrderedSetKindIsOrderedSet", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_CollectionLiteralExp.attributes={pivot_CollectionLiteralExp_kind}
pivot_CollectionLiteralExp.methods={pivot_CollectionLiteralExp_m_BagKindIsBag, pivot_CollectionLiteralExp_m_OrderedSetKindIsOrderedSet, pivot_CollectionLiteralExp_m_SequenceKindIsSequence, pivot_CollectionLiteralExp_m_CollectionKindIsConcrete, pivot_CollectionLiteralExp_m_SetKindIsSet}

# LiteralExp class attributes and methods

# pivot_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# pivot_CollectionRange class attributes and methods

# pivot_Type class attributes and methods
pivot_Type_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
pivot_Type_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='expr'), Parameter(name='selfType')}, type=Type)
pivot_Type_m_UniqueInvariantName: Method = Method(name="UniqueInvariantName", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_Type.attributes={pivot_Type_instanceClassName}
pivot_Type.methods={pivot_Type_m_specializeIn, pivot_Type_m_UniqueInvariantName}

# pivot_Comment class attributes and methods
pivot_Comment_body: Property = Property(name="body", type=StringType)
pivot_Comment.attributes={pivot_Comment_body}

# Element class attributes and methods

# pivot_ConnectionPointReference class attributes and methods

# Vertex class attributes and methods

# pivot_Pseudostate class attributes and methods
pivot_Pseudostate_kind: Property = Property(name="kind", type=StringType)
pivot_Pseudostate.attributes={pivot_Pseudostate_kind}

# pivot_CollectionType class attributes and methods
pivot_CollectionType_lower: Property = Property(name="lower", type=StringType)
pivot_CollectionType_upper: Property = Property(name="upper", type=StringType)
pivot_CollectionType.attributes={pivot_CollectionType_lower, pivot_CollectionType_upper}

# DataType class attributes and methods

# pivot_Constraint class attributes and methods
pivot_Constraint_isCallable: Property = Property(name="isCallable", type=StringType)
pivot_Constraint_m_UniqueName: Method = Method(name="UniqueName", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_Constraint.attributes={pivot_Constraint_isCallable}
pivot_Constraint.methods={pivot_Constraint_m_UniqueName}

# pivot_OpaqueExpression class attributes and methods
pivot_OpaqueExpression_body: Property = Property(name="body", type=StringType)
pivot_OpaqueExpression_language: Property = Property(name="language", type=StringType)
pivot_OpaqueExpression_message: Property = Property(name="message", type=StringType)
pivot_OpaqueExpression.attributes={pivot_OpaqueExpression_language, pivot_OpaqueExpression_message, pivot_OpaqueExpression_body}

# pivot_Namespace class attributes and methods

# pivot_State class attributes and methods
pivot_State_isComposite: Property = Property(name="isComposite", type=StringType)
pivot_State_isOrthogonal: Property = Property(name="isOrthogonal", type=StringType)
pivot_State_isSimple: Property = Property(name="isSimple", type=StringType)
pivot_State_isSubmachineState: Property = Property(name="isSubmachineState", type=StringType)
pivot_State.attributes={pivot_State_isSimple, pivot_State_isComposite, pivot_State_isSubmachineState, pivot_State_isOrthogonal}

# pivot_DataType class attributes and methods
pivot_DataType_isSerializable: Property = Property(name="isSerializable", type=StringType)
pivot_DataType.attributes={pivot_DataType_isSerializable}

# pivot_DynamicElement class attributes and methods

# pivot_DynamicProperty class attributes and methods
pivot_DynamicProperty_default: Property = Property(name="default", type=StringType)
pivot_DynamicProperty.attributes={pivot_DynamicProperty_default}

# pivot_ConstructorExp class attributes and methods
pivot_ConstructorExp_value: Property = Property(name="value", type=StringType)
pivot_ConstructorExp.attributes={pivot_ConstructorExp_value}

# pivot_ConstructorPart class attributes and methods

# Visitable class attributes and methods

# pivot_ElementExtension class attributes and methods

# pivot_DynamicType class attributes and methods

# DynamicElement class attributes and methods

# pivot_EnumerationLiteral class attributes and methods
pivot_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
pivot_EnumerationLiteral.attributes={pivot_EnumerationLiteral_value}

# pivot_Enumeration class attributes and methods

# pivot_EnumLiteralExp class attributes and methods
pivot_EnumLiteralExp_m_TypeIsEnumerationType: Method = Method(name="TypeIsEnumerationType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_EnumLiteralExp.methods={pivot_EnumLiteralExp_m_TypeIsEnumerationType}

# pivot_Feature class attributes and methods
pivot_Feature_implementationClass: Property = Property(name="implementationClass", type=StringType)
pivot_Feature_implementation: Property = Property(name="implementation", type=StringType)
pivot_Feature.attributes={pivot_Feature_implementationClass, pivot_Feature_implementation}

# TypedMultiplicityElement class attributes and methods

# pivot_FeatureCallExp class attributes and methods
pivot_FeatureCallExp_isPre: Property = Property(name="isPre", type=StringType)
pivot_FeatureCallExp.attributes={pivot_FeatureCallExp_isPre}

# CallExp class attributes and methods

# pivot_FinalState class attributes and methods

# State class attributes and methods

# pivot_ExpressionInOCL class attributes and methods

# OpaqueExpression class attributes and methods

# pivot_Variable class attributes and methods
pivot_Variable_implicit: Property = Property(name="implicit", type=StringType)
pivot_Variable.attributes={pivot_Variable_implicit}

# pivot_Import class attributes and methods

# pivot_IntegerLiteralExp class attributes and methods
pivot_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
pivot_IntegerLiteralExp_m_TypeIsInteger: Method = Method(name="TypeIsInteger", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IntegerLiteralExp.attributes={pivot_IntegerLiteralExp_integerSymbol}
pivot_IntegerLiteralExp.methods={pivot_IntegerLiteralExp_m_TypeIsInteger}

# NumericLiteralExp class attributes and methods

# pivot_IfExp class attributes and methods
pivot_IfExp_m_ConditionTypeIsBoolean: Method = Method(name="ConditionTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IfExp.methods={pivot_IfExp_m_ConditionTypeIsBoolean}

# pivot_Iteration class attributes and methods

# Operation class attributes and methods

# pivot_InvalidLiteralExp class attributes and methods

# pivot_InvalidType class attributes and methods

# pivot_IterateExp class attributes and methods
pivot_IterateExp_m_BodyTypeConformsToResultType: Method = Method(name="BodyTypeConformsToResultType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp_m_TypeIsResultType: Method = Method(name="TypeIsResultType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IterateExp_m_OneInitializer: Method = Method(name="OneInitializer", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IterateExp.methods={pivot_IterateExp_m_TypeIsResultType, pivot_IterateExp_m_BodyTypeConformsToResultType, pivot_IterateExp_m_OneInitializer}

# LoopExp class attributes and methods

# ReferringElement class attributes and methods

# pivot_Parameter class attributes and methods

# pivot_IteratorExp class attributes and methods
pivot_IteratorExp_m_ExistsBodyTypeIsBoolean: Method = Method(name="ExistsBodyTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedHasOneIterator: Method = Method(name="CollectNestedHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ClosureSourceElementTypeIsBodyElementType: Method = Method(name="ClosureSourceElementTypeIsBodyElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ExistsTypeIsBoolean: Method = Method(name="ExistsTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ClosureTypeIsUniqueCollection: Method = Method(name="ClosureTypeIsUniqueCollection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectTypeIsSourceType: Method = Method(name="RejectOrSelectTypeIsSourceType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_SortedByIsOrderedIfSourceIsOrdered: Method = Method(name="SortedByIsOrderedIfSourceIsOrdered", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_AnyTypeIsSourceElementType: Method = Method(name="AnyTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectTypeIsUnordered: Method = Method(name="CollectTypeIsUnordered", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_IteratorTypeIsSourceElementType: Method = Method(name="IteratorTypeIsSourceElementType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_OneBodyTypeIsBoolean: Method = Method(name="OneBodyTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedTypeIsBag: Method = Method(name="CollectNestedTypeIsBag", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_AnyHasOneIterator: Method = Method(name="AnyHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_SortedByHasOneIterator: Method = Method(name="SortedByHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectTypeIsBoolean: Method = Method(name="RejectOrSelectTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_OneHasOneIterator: Method = Method(name="OneHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_OneTypeIsBoolean: Method = Method(name="OneTypeIsBoolean", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_SortedByElementTypeIsSourceElementType: Method = Method(name="SortedByElementTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_AnyBodyTypeIsBoolean: Method = Method(name="AnyBodyTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ForAllTypeIsBoolean: Method = Method(name="ForAllTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_CollectHasOneIterator: Method = Method(name="CollectHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ClosureElementTypeIsSourceElementType: Method = Method(name="ClosureElementTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectElementTypeIsSourceElementType: Method = Method(name="CollectElementTypeIsSourceElementType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ClosureHasOneIterator: Method = Method(name="ClosureHasOneIterator", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_ClosureBodyTypeIsConformanttoIteratorType: Method = Method(name="ClosureBodyTypeIsConformanttoIteratorType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_SortedByIteratorTypeIsComparable: Method = Method(name="SortedByIteratorTypeIsComparable", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_CollectNestedTypeIsBodyType: Method = Method(name="CollectNestedTypeIsBodyType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_IsUniqueHasOneIterator: Method = Method(name="IsUniqueHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_RejectOrSelectHasOneIterator: Method = Method(name="RejectOrSelectHasOneIterator", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_IteratorExp_m_ForAllBodyTypeIsBoolean: Method = Method(name="ForAllBodyTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp_m_IsUniqueTypeIsBoolean: Method = Method(name="IsUniqueTypeIsBoolean", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_IteratorExp.methods={pivot_IteratorExp_m_ExistsBodyTypeIsBoolean, pivot_IteratorExp_m_OneTypeIsBoolean, pivot_IteratorExp_m_AnyBodyTypeIsBoolean, pivot_IteratorExp_m_IsUniqueTypeIsBoolean, pivot_IteratorExp_m_CollectTypeIsUnordered, pivot_IteratorExp_m_SortedByIteratorTypeIsComparable, pivot_IteratorExp_m_CollectNestedTypeIsBag, pivot_IteratorExp_m_OneHasOneIterator, pivot_IteratorExp_m_RejectOrSelectTypeIsSourceType, pivot_IteratorExp_m_ForAllBodyTypeIsBoolean, pivot_IteratorExp_m_RejectOrSelectTypeIsBoolean, pivot_IteratorExp_m_CollectNestedHasOneIterator, pivot_IteratorExp_m_ClosureTypeIsUniqueCollection, pivot_IteratorExp_m_CollectNestedTypeIsBodyType, pivot_IteratorExp_m_RejectOrSelectHasOneIterator, pivot_IteratorExp_m_IteratorTypeIsSourceElementType, pivot_IteratorExp_m_ClosureElementTypeIsSourceElementType, pivot_IteratorExp_m_ExistsTypeIsBoolean, pivot_IteratorExp_m_SortedByIsOrderedIfSourceIsOrdered, pivot_IteratorExp_m_ForAllTypeIsBoolean, pivot_IteratorExp_m_CollectElementTypeIsSourceElementType, pivot_IteratorExp_m_OneBodyTypeIsBoolean, pivot_IteratorExp_m_ClosureHasOneIterator, pivot_IteratorExp_m_ClosureSourceElementTypeIsBodyElementType, pivot_IteratorExp_m_AnyHasOneIterator, pivot_IteratorExp_m_SortedByElementTypeIsSourceElementType, pivot_IteratorExp_m_IsUniqueHasOneIterator, pivot_IteratorExp_m_SortedByHasOneIterator, pivot_IteratorExp_m_ClosureBodyTypeIsConformanttoIteratorType, pivot_IteratorExp_m_AnyTypeIsSourceElementType, pivot_IteratorExp_m_CollectHasOneIterator}

# pivot_LambdaType class attributes and methods

# pivot_LetExp class attributes and methods
pivot_LetExp_m_TypeIsInType: Method = Method(name="TypeIsInType", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_LetExp.methods={pivot_LetExp_m_TypeIsInType}

# pivot_Library class attributes and methods

# Package class attributes and methods

# pivot_Precedence class attributes and methods
pivot_Precedence_associativity: Property = Property(name="associativity", type=StringType)
pivot_Precedence_order: Property = Property(name="order", type=StringType)
pivot_Precedence.attributes={pivot_Precedence_order, pivot_Precedence_associativity}

# pivot_LiteralExp class attributes and methods

# pivot_LoopExp class attributes and methods
pivot_LoopExp_m_SourceIsCollection: Method = Method(name="SourceIsCollection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_LoopExp_m_NoInitializers: Method = Method(name="NoInitializers", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_LoopExp.methods={pivot_LoopExp_m_NoInitializers, pivot_LoopExp_m_SourceIsCollection}

# pivot_MessageExp class attributes and methods
pivot_MessageExp_m_OneCallOrOneSend: Method = Method(name="OneCallOrOneSend", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_MessageExp_m_TargetIsNotACollection: Method = Method(name="TargetIsNotACollection", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_MessageExp.methods={pivot_MessageExp_m_OneCallOrOneSend, pivot_MessageExp_m_TargetIsNotACollection}

# pivot_SendSignalAction class attributes and methods

# pivot_MessageType class attributes and methods

# pivot_Signal class attributes and methods

# pivot_Metaclass class attributes and methods

# pivot_MorePivotable class attributes and methods

# pivot_Nameable class attributes and methods

# pivot_NamedElement class attributes and methods
pivot_NamedElement_name: Property = Property(name="name", type=StringType)
pivot_NamedElement_isStatic: Property = Property(name="isStatic", type=StringType)
pivot_NamedElement.attributes={pivot_NamedElement_isStatic, pivot_NamedElement_name}

# Nameable class attributes and methods

# pivot_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# pivot_NullLiteralExp class attributes and methods

# pivot_NumericLiteralExp class attributes and methods

# ValueSpecification class attributes and methods

# Feature class attributes and methods

# TemplateableElement class attributes and methods

# ParameterableElement class attributes and methods

# pivot_OperationCallExp class attributes and methods
pivot_OperationCallExp_m_ArgumentCount: Method = Method(name="ArgumentCount", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
pivot_OperationCallExp_m_ArgumentTypeIsConformant: Method = Method(name="ArgumentTypeIsConformant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_OperationCallExp.methods={pivot_OperationCallExp_m_ArgumentCount, pivot_OperationCallExp_m_ArgumentTypeIsConformant}

# pivot_OperationTemplateParameter class attributes and methods

# TemplateParameter class attributes and methods

# pivot_OrderedSetType class attributes and methods

# pivot_Package class attributes and methods
pivot_Package_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
pivot_Package_nsURI: Property = Property(name="nsURI", type=StringType)
pivot_Package.attributes={pivot_Package_nsPrefix, pivot_Package_nsURI}

# pivot_PackageableElement class attributes and methods

# VariableDeclaration class attributes and methods

# pivot_ParameterableElement class attributes and methods
pivot_ParameterableElement_m_isTemplateParameter: Method = Method(name="isTemplateParameter", parameters={}, type=StringType)
pivot_ParameterableElement_m_isCompatibleWith: Method = Method(name="isCompatibleWith", parameters={Parameter(name='p')}, type=StringType)
pivot_ParameterableElement.methods={pivot_ParameterableElement_m_isCompatibleWith, pivot_ParameterableElement_m_isTemplateParameter}

# pivot_TemplateParameter class attributes and methods

# pivot_Pivotable class attributes and methods

# pivot_PrimitiveLiteralExp class attributes and methods

# pivot_PrimitiveType class attributes and methods

# pivot_Profile class attributes and methods

# pivot_PropertyCallExp class attributes and methods
pivot_PropertyCallExp_m_NonStaticSourceTypeIsConformant: Method = Method(name="NonStaticSourceTypeIsConformant", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType: Method = Method(name="getSpecializedReferredPropertyOwningType", parameters={}, type=Type)
pivot_PropertyCallExp_m_getSpecializedReferredPropertyType: Method = Method(name="getSpecializedReferredPropertyType", parameters={}, type=Type)
pivot_PropertyCallExp_m_CompatibleResultType: Method = Method(name="CompatibleResultType", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
pivot_PropertyCallExp.methods={pivot_PropertyCallExp_m_NonStaticSourceTypeIsConformant, pivot_PropertyCallExp_m_getSpecializedReferredPropertyOwningType, pivot_PropertyCallExp_m_CompatibleResultType, pivot_PropertyCallExp_m_getSpecializedReferredPropertyType}

# pivot_RealLiteralExp class attributes and methods
pivot_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
pivot_RealLiteralExp.attributes={pivot_RealLiteralExp_realSymbol}

# pivot_StateMachine class attributes and methods

# pivot_Root class attributes and methods
pivot_Root_externalURI: Property = Property(name="externalURI", type=StringType)
pivot_Root.attributes={pivot_Root_externalURI}

# pivot_ReferringElement class attributes and methods
pivot_ReferringElement_m_getReferredElement: Method = Method(name="getReferredElement", parameters={}, type=Element)
pivot_ReferringElement.methods={pivot_ReferringElement_m_getReferredElement}

# pivot_Region class attributes and methods

# pivot_Transition class attributes and methods
pivot_Transition_kind: Property = Property(name="kind", type=StringType)
pivot_Transition.attributes={pivot_Transition_kind}

# pivot_Vertex class attributes and methods

# pivot_SelfType class attributes and methods
pivot_SelfType_m_specializeIn: Method = Method(name="specializeIn", parameters={Parameter(name='expr'), Parameter(name='selfType')}, type=Type)
pivot_SelfType.methods={pivot_SelfType_m_specializeIn}

# pivot_SequenceType class attributes and methods

# pivot_SetType class attributes and methods

# pivot_Trigger class attributes and methods

# Behavior class attributes and methods

# pivot_StateExp class attributes and methods

# pivot_StringLiteralExp class attributes and methods
pivot_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
pivot_StringLiteralExp.attributes={pivot_StringLiteralExp_stringSymbol}

# pivot_TemplateBinding class attributes and methods

# pivot_TemplateSignature class attributes and methods

# pivot_TemplateParameterSubstitution class attributes and methods

# pivot_TemplateableElement class attributes and methods
pivot_TemplateableElement_m_parameterableElements: Method = Method(name="parameterableElements", parameters={}, type=ParameterableElement)
pivot_TemplateableElement_m_isTemplate: Method = Method(name="isTemplate", parameters={}, type=StringType)
pivot_TemplateableElement.methods={pivot_TemplateableElement_m_isTemplate, pivot_TemplateableElement_m_parameterableElements}

# pivot_Stereotype class attributes and methods

# pivot_TemplateParameterType class attributes and methods
pivot_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
pivot_TemplateParameterType.attributes={pivot_TemplateParameterType_specification}

# pivot_TupleLiteralPart class attributes and methods

# pivot_TupleType class attributes and methods

# pivot_TupleLiteralExp class attributes and methods

# pivot_TypeExp class attributes and methods

# pivot_TypedElement class attributes and methods
pivot_TypedElement_isRequired: Property = Property(name="isRequired", type=StringType)
pivot_TypedElement.attributes={pivot_TypedElement_isRequired}

# pivot_TypedMultiplicityElement class attributes and methods
pivot_TypedMultiplicityElement_m_CompatibleBody: Method = Method(name="CompatibleBody", parameters={Parameter(name='bodySpecification')}, type=StringType)
pivot_TypedMultiplicityElement_m_makeParameter: Method = Method(name="makeParameter", parameters={}, type=StringType)
pivot_TypedMultiplicityElement.methods={pivot_TypedMultiplicityElement_m_CompatibleBody, pivot_TypedMultiplicityElement_m_makeParameter}

# pivot_TypeTemplateParameter class attributes and methods
pivot_TypeTemplateParameter_allowSubstitutable: Property = Property(name="allowSubstitutable", type=StringType)
pivot_TypeTemplateParameter.attributes={pivot_TypeTemplateParameter_allowSubstitutable}

# pivot_UnlimitedNaturalLiteralExp class attributes and methods
pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol: Property = Property(name="unlimitedNaturalSymbol", type=StringType)
pivot_UnlimitedNaturalLiteralExp.attributes={pivot_UnlimitedNaturalLiteralExp_unlimitedNaturalSymbol}

# pivot_UnspecifiedType class attributes and methods

# pivot_UnspecifiedValueExp class attributes and methods

# pivot_ValueSpecification class attributes and methods
pivot_ValueSpecification_m_isComputable: Method = Method(name="isComputable", parameters={}, type=StringType)
pivot_ValueSpecification_m_integerValue: Method = Method(name="integerValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_booleanValue: Method = Method(name="booleanValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_unlimitedValue: Method = Method(name="unlimitedValue", parameters={}, type=StringType)
pivot_ValueSpecification_m_isNull: Method = Method(name="isNull", parameters={}, type=StringType)
pivot_ValueSpecification_m_stringValue: Method = Method(name="stringValue", parameters={}, type=StringType)
pivot_ValueSpecification.methods={pivot_ValueSpecification_m_stringValue, pivot_ValueSpecification_m_unlimitedValue, pivot_ValueSpecification_m_integerValue, pivot_ValueSpecification_m_booleanValue, pivot_ValueSpecification_m_isNull, pivot_ValueSpecification_m_isComputable}

# pivot_VariableDeclaration class attributes and methods

# pivot_VariableExp class attributes and methods
pivot_VariableExp_implicit: Property = Property(name="implicit", type=StringType)
pivot_VariableExp.attributes={pivot_VariableExp_implicit}

# pivot_Visitable class attributes and methods

# pivot_Visitor class attributes and methods

# pivot_VoidType class attributes and methods

# Relationships
unownedAttribute6: BinaryAssociation = BinaryAssociation(
    name="unownedAttribute6",
    ends={
        Property(name="Property", type=pivot_AssociationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
referredAssociationClass7: BinaryAssociation = BinaryAssociation(
    name="referredAssociationClass7",
    ends={
        Property(name="pivot_AssociationClass", type=pivot_AssociationClassCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_AssociationClassCallExp", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
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
operation9: BinaryAssociation = BinaryAssociation(
    name="operation9",
    ends={
        Property(name="pivot_Operation", type=pivot_CallOperationAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallOperationAction", type=pivot_Operation, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="pivot_OCLExpression", type=pivot_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item11: BinaryAssociation = BinaryAssociation(
    name="item11",
    ends={
        Property(name="pivot_OCLExpression12", type=pivot_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionItem", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedBehavior10: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior10",
    ends={
        Property(name="pivot_Behavior", type=pivot_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Class", type=pivot_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part13: BinaryAssociation = BinaryAssociation(
    name="part13",
    ends={
        Property(name="pivot_CollectionLiteralPart", type=pivot_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionLiteralExp", type=pivot_CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first14: BinaryAssociation = BinaryAssociation(
    name="first14",
    ends={
        Property(name="pivot_OCLExpression15", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType19: BinaryAssociation = BinaryAssociation(
    name="elementType19",
    ends={
        Property(name="pivot_Type", type=pivot_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
annotatedElement20: BinaryAssociation = BinaryAssociation(
    name="annotatedElement20",
    ends={
        Property(name="pivot_Element21", type=pivot_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Comment", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
entry22: BinaryAssociation = BinaryAssociation(
    name="entry22",
    ends={
        Property(name="pivot_Pseudostate", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
last16: BinaryAssociation = BinaryAssociation(
    name="last16",
    ends={
        Property(name="pivot_OCLExpression18", type=pivot_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_CollectionRange17", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedElement28: BinaryAssociation = BinaryAssociation(
    name="constrainedElement28",
    ends={
        Property(name="pivot_Element29", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint", type=pivot_Element, multiplicity=Multiplicity(0, 9999))
    }
)
specification30: BinaryAssociation = BinaryAssociation(
    name="specification30",
    ends={
        Property(name="pivot_OpaqueExpression", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint31", type=pivot_OpaqueExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context32: BinaryAssociation = BinaryAssociation(
    name="context32",
    ends={
        Property(name="pivot_Namespace", type=pivot_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Constraint33", type=pivot_Namespace, multiplicity=Multiplicity(0, 1))
    }
)
state23: BinaryAssociation = BinaryAssociation(
    name="state23",
    ends={
        Property(name="pivot_State", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference24", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
exit25: BinaryAssociation = BinaryAssociation(
    name="exit25",
    ends={
        Property(name="pivot_Pseudostate27", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConnectionPointReference26", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999))
    }
)
referredProperty35: BinaryAssociation = BinaryAssociation(
    name="referredProperty35",
    ends={
        Property(name="pivot_Property", type=pivot_ConstructorPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorPart36", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
initExpression37: BinaryAssociation = BinaryAssociation(
    name="initExpression37",
    ends={
        Property(name="pivot_OCLExpression39", type=pivot_ConstructorPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorPart38", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
behavioralType40: BinaryAssociation = BinaryAssociation(
    name="behavioralType40",
    ends={
        Property(name="pivot_Type41", type=pivot_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DataType", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
metaType42: BinaryAssociation = BinaryAssociation(
    name="metaType42",
    ends={
        Property(name="pivot_Type43", type=pivot_DynamicElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicElement", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
part34: BinaryAssociation = BinaryAssociation(
    name="part34",
    ends={
        Property(name="pivot_ConstructorPart", type=pivot_ConstructorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ConstructorExp", type=pivot_ConstructorPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedProperty46: BinaryAssociation = BinaryAssociation(
    name="ownedProperty46",
    ends={
        Property(name="pivot_DynamicProperty47", type=pivot_DynamicType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicType", type=pivot_DynamicProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComment48: BinaryAssociation = BinaryAssociation(
    name="ownedComment48",
    ends={
        Property(name="pivot_Comment50", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Element49", type=pivot_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension51: BinaryAssociation = BinaryAssociation(
    name="extension51",
    ends={
        Property(name="ElementExtension", type=pivot_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=pivot_ElementExtension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredProperty44: BinaryAssociation = BinaryAssociation(
    name="referredProperty44",
    ends={
        Property(name="pivot_Property45", type=pivot_DynamicProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_DynamicProperty", type=pivot_Property, multiplicity=Multiplicity(1, 1))
    }
)
referredEnumLiteral55: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral55",
    ends={
        Property(name="pivot_EnumerationLiteral", type=pivot_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_EnumLiteralExp", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral56: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral56",
    ends={
        Property(name="EnumerationLiteral", type=pivot_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration57: BinaryAssociation = BinaryAssociation(
    name="enumeration57",
    ends={
        Property(name="Enumeration", type=pivot_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=pivot_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
stereotype52: BinaryAssociation = BinaryAssociation(
    name="stereotype52",
    ends={
        Property(name="pivot_Type53", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ElementExtension", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
base54: BinaryAssociation = BinaryAssociation(
    name="base54",
    ends={
        Property(name="Element", type=pivot_ElementExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=pivot_Element, multiplicity=Multiplicity(1, 1))
    }
)
contextVariable60: BinaryAssociation = BinaryAssociation(
    name="contextVariable60",
    ends={
        Property(name="pivot_ExpressionInOCL61", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pivot_Variable", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1))
    }
)
resultVariable62: BinaryAssociation = BinaryAssociation(
    name="resultVariable62",
    ends={
        Property(name="pivot_Variable64", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL63", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable65: BinaryAssociation = BinaryAssociation(
    name="parameterVariable65",
    ends={
        Property(name="pivot_Variable67", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL66", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messageExpression68: BinaryAssociation = BinaryAssociation(
    name="messageExpression68",
    ends={
        Property(name="pivot_OCLExpression70", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL69", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExpression58: BinaryAssociation = BinaryAssociation(
    name="bodyExpression58",
    ends={
        Property(name="pivot_OCLExpression59", type=pivot_ExpressionInOCL, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_ExpressionInOCL", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition71: BinaryAssociation = BinaryAssociation(
    name="condition71",
    ends={
        Property(name="pivot_OCLExpression72", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression73: BinaryAssociation = BinaryAssociation(
    name="thenExpression73",
    ends={
        Property(name="pivot_OCLExpression75", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp74", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression76: BinaryAssociation = BinaryAssociation(
    name="elseExpression76",
    ends={
        Property(name="pivot_OCLExpression78", type=pivot_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IfExp77", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
importedNamespace79: BinaryAssociation = BinaryAssociation(
    name="importedNamespace79",
    ends={
        Property(name="pivot_Namespace80", type=pivot_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Import", type=pivot_Namespace, multiplicity=Multiplicity(1, 1))
    }
)
result81: BinaryAssociation = BinaryAssociation(
    name="result81",
    ends={
        Property(name="pivot_Variable82", type=pivot_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_IterateExp", type=pivot_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedIterator83: BinaryAssociation = BinaryAssociation(
    name="ownedIterator83",
    ends={
        Property(name="pivot_Parameter", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAccumulator84: BinaryAssociation = BinaryAssociation(
    name="ownedAccumulator84",
    ends={
        Property(name="pivot_Parameter86", type=pivot_Iteration, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Iteration85", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextType87: BinaryAssociation = BinaryAssociation(
    name="contextType87",
    ends={
        Property(name="pivot_Type88", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
parameterType89: BinaryAssociation = BinaryAssociation(
    name="parameterType89",
    ends={
        Property(name="pivot_Type91", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType90", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
resultType92: BinaryAssociation = BinaryAssociation(
    name="resultType92",
    ends={
        Property(name="pivot_Type94", type=pivot_LambdaType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LambdaType93", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
in95: BinaryAssociation = BinaryAssociation(
    name="in95",
    ends={
        Property(name="pivot_OCLExpression96", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable97: BinaryAssociation = BinaryAssociation(
    name="variable97",
    ends={
        Property(name="pivot_Variable99", type=pivot_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LetExp98", type=pivot_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ownedPrecedence100: BinaryAssociation = BinaryAssociation(
    name="ownedPrecedence100",
    ends={
        Property(name="pivot_Precedence", type=pivot_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Library", type=pivot_Precedence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body101: BinaryAssociation = BinaryAssociation(
    name="body101",
    ends={
        Property(name="pivot_OCLExpression102", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator103: BinaryAssociation = BinaryAssociation(
    name="iterator103",
    ends={
        Property(name="pivot_Variable105", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp104", type=pivot_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredIteration106: BinaryAssociation = BinaryAssociation(
    name="referredIteration106",
    ends={
        Property(name="pivot_Iteration108", type=pivot_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_LoopExp107", type=pivot_Iteration, multiplicity=Multiplicity(0, 1))
    }
)
target109: BinaryAssociation = BinaryAssociation(
    name="target109",
    ends={
        Property(name="pivot_OCLExpression110", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp", type=pivot_OCLExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument111: BinaryAssociation = BinaryAssociation(
    name="argument111",
    ends={
        Property(name="pivot_OCLExpression113", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp112", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
calledOperation114: BinaryAssociation = BinaryAssociation(
    name="calledOperation114",
    ends={
        Property(name="pivot_CallOperationAction116", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp115", type=pivot_CallOperationAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentSignal117: BinaryAssociation = BinaryAssociation(
    name="sentSignal117",
    ends={
        Property(name="pivot_SendSignalAction", type=pivot_MessageExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageExp118", type=pivot_SendSignalAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredSignal119: BinaryAssociation = BinaryAssociation(
    name="referredSignal119",
    ends={
        Property(name="pivot_Signal", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType", type=pivot_Signal, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation120: BinaryAssociation = BinaryAssociation(
    name="referredOperation120",
    ends={
        Property(name="pivot_Operation122", type=pivot_MessageType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_MessageType121", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
instanceType123: BinaryAssociation = BinaryAssociation(
    name="instanceType123",
    ends={
        Property(name="pivot_Type124", type=pivot_Metaclass, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Metaclass", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
ownedAnnotation125: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotation125",
    ends={
        Property(name="pivot_Annotation126", type=pivot_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NamedElement", type=pivot_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedRule127: BinaryAssociation = BinaryAssociation(
    name="ownedRule127",
    ends={
        Property(name="pivot_Constraint129", type=pivot_Namespace, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Namespace128", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier130: BinaryAssociation = BinaryAssociation(
    name="qualifier130",
    ends={
        Property(name="pivot_OCLExpression131", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999))
    }
)
navigationSource132: BinaryAssociation = BinaryAssociation(
    name="navigationSource132",
    ends={
        Property(name="pivot_Property134", type=pivot_NavigationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_NavigationCallExp133", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression146: BinaryAssociation = BinaryAssociation(
    name="bodyExpression146",
    ends={
        Property(name="pivot_Operation147", type=pivot_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="pivot_OpaqueExpression148", type=pivot_Operation, multiplicity=Multiplicity(1, 1))
    }
)
raisedException135: BinaryAssociation = BinaryAssociation(
    name="raisedException135",
    ends={
        Property(name="pivot_Type137", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation136", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter138: BinaryAssociation = BinaryAssociation(
    name="ownedParameter138",
    ends={
        Property(name="Parameter", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=pivot_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningType139: BinaryAssociation = BinaryAssociation(
    name="owningType139",
    ends={
        Property(name="Type", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
precondition140: BinaryAssociation = BinaryAssociation(
    name="precondition140",
    ends={
        Property(name="pivot_Constraint142", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation141", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postcondition143: BinaryAssociation = BinaryAssociation(
    name="postcondition143",
    ends={
        Property(name="pivot_Constraint145", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation144", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
precedence149: BinaryAssociation = BinaryAssociation(
    name="precedence149",
    ends={
        Property(name="pivot_Precedence151", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation150", type=pivot_Precedence, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation153: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation153",
    ends={
        Property(name="pivot_Operation154", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation152", type=pivot_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
class155: BinaryAssociation = BinaryAssociation(
    name="class155",
    ends={
        Property(name="pivot_Class157", type=pivot_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Operation156", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
importedPackage169: BinaryAssociation = BinaryAssociation(
    name="importedPackage169",
    ends={
        Property(name="pivot_Package168", type=pivot_Package, multiplicity=Multiplicity(0, 9999)),
        Property(name="pivot_Package", type=pivot_Package, multiplicity=Multiplicity(1, 1))
    }
)
argument158: BinaryAssociation = BinaryAssociation(
    name="argument158",
    ends={
        Property(name="pivot_OCLExpression159", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation160: BinaryAssociation = BinaryAssociation(
    name="referredOperation160",
    ends={
        Property(name="pivot_Operation162", type=pivot_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_OperationCallExp161", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage164: BinaryAssociation = BinaryAssociation(
    name="nestedPackage164",
    ends={
        Property(name="Package", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestingPackage", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage166: BinaryAssociation = BinaryAssociation(
    name="nestingPackage166",
    ends={
        Property(name="Package167", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="nestedPackage", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType170: BinaryAssociation = BinaryAssociation(
    name="ownedType170",
    ends={
        Property(name="Type171", type=pivot_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=pivot_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation172: BinaryAssociation = BinaryAssociation(
    name="operation172",
    ends={
        Property(name="Operation", type=pivot_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=pivot_Operation, multiplicity=Multiplicity(0, 1))
    }
)
owningTemplateParameter173: BinaryAssociation = BinaryAssociation(
    name="owningTemplateParameter173",
    ends={
        Property(name="TemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameteredElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
templateParameter174: BinaryAssociation = BinaryAssociation(
    name="templateParameter174",
    ends={
        Property(name="TemplateParameter175", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameteredElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(0, 1))
    }
)
class176: BinaryAssociation = BinaryAssociation(
    name="class176",
    ends={
        Property(name="pivot_Class178", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property177", type=pivot_Class, multiplicity=Multiplicity(0, 1))
    }
)
opposite180: BinaryAssociation = BinaryAssociation(
    name="opposite180",
    ends={
        Property(name="pivot_Property181", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property179", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
association182: BinaryAssociation = BinaryAssociation(
    name="association182",
    ends={
        Property(name="AssociationClass", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="unownedAttribute", type=pivot_AssociationClass, multiplicity=Multiplicity(0, 1))
    }
)
defaultExpression183: BinaryAssociation = BinaryAssociation(
    name="defaultExpression183",
    ends={
        Property(name="pivot_OpaqueExpression185", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property184", type=pivot_OpaqueExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keys187: BinaryAssociation = BinaryAssociation(
    name="keys187",
    ends={
        Property(name="pivot_Property188", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property186", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
redefinedProperty190: BinaryAssociation = BinaryAssociation(
    name="redefinedProperty190",
    ends={
        Property(name="pivot_Property191", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property189", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
subsettedProperty193: BinaryAssociation = BinaryAssociation(
    name="subsettedProperty193",
    ends={
        Property(name="pivot_Property194", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property192", type=pivot_Property, multiplicity=Multiplicity(0, 9999))
    }
)
referredProperty196: BinaryAssociation = BinaryAssociation(
    name="referredProperty196",
    ends={
        Property(name="pivot_Property197", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Property195", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
owningType198: BinaryAssociation = BinaryAssociation(
    name="owningType198",
    ends={
        Property(name="Type199", type=pivot_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty200: BinaryAssociation = BinaryAssociation(
    name="referredProperty200",
    ends={
        Property(name="pivot_Property201", type=pivot_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_PropertyCallExp", type=pivot_Property, multiplicity=Multiplicity(0, 1))
    }
)
stateMachine202: BinaryAssociation = BinaryAssociation(
    name="stateMachine202",
    ends={
        Property(name="pivot_StateMachine", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Pseudostate203", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state204: BinaryAssociation = BinaryAssociation(
    name="state204",
    ends={
        Property(name="pivot_State206", type=pivot_Pseudostate, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Pseudostate205", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage218: BinaryAssociation = BinaryAssociation(
    name="nestedPackage218",
    ends={
        Property(name="pivot_Package219", type=pivot_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Root", type=pivot_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition207: BinaryAssociation = BinaryAssociation(
    name="transition207",
    ends={
        Property(name="Transition", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=pivot_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateMachine208: BinaryAssociation = BinaryAssociation(
    name="stateMachine208",
    ends={
        Property(name="pivot_StateMachine209", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Region", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
state210: BinaryAssociation = BinaryAssociation(
    name="state210",
    ends={
        Property(name="pivot_State212", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Region211", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
extendedRegion214: BinaryAssociation = BinaryAssociation(
    name="extendedRegion214",
    ends={
        Property(name="pivot_Region215", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Region213", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
subvertex216: BinaryAssociation = BinaryAssociation(
    name="subvertex216",
    ends={
        Property(name="Vertex", type=pivot_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="container217", type=pivot_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports220: BinaryAssociation = BinaryAssociation(
    name="imports220",
    ends={
        Property(name="pivot_Import222", type=pivot_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Root221", type=pivot_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signal223: BinaryAssociation = BinaryAssociation(
    name="signal223",
    ends={
        Property(name="pivot_Signal225", type=pivot_SendSignalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_SendSignalAction224", type=pivot_Signal, multiplicity=Multiplicity(1, 1))
    }
)
submachine226: BinaryAssociation = BinaryAssociation(
    name="submachine226",
    ends={
        Property(name="StateMachine", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="submachineState", type=pivot_StateMachine, multiplicity=Multiplicity(0, 1))
    }
)
connection227: BinaryAssociation = BinaryAssociation(
    name="connection227",
    ends={
        Property(name="pivot_ConnectionPointReference229", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State228", type=pivot_ConnectionPointReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateInvariant236: BinaryAssociation = BinaryAssociation(
    name="stateInvariant236",
    ends={
        Property(name="pivot_Constraint238", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State237", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entry239: BinaryAssociation = BinaryAssociation(
    name="entry239",
    ends={
        Property(name="pivot_Behavior241", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State240", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit242: BinaryAssociation = BinaryAssociation(
    name="exit242",
    ends={
        Property(name="pivot_Behavior244", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State243", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doActivity245: BinaryAssociation = BinaryAssociation(
    name="doActivity245",
    ends={
        Property(name="pivot_Behavior247", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State246", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connectionPoint248: BinaryAssociation = BinaryAssociation(
    name="connectionPoint248",
    ends={
        Property(name="pivot_Pseudostate250", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State249", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
redefinedState231: BinaryAssociation = BinaryAssociation(
    name="redefinedState231",
    ends={
        Property(name="pivot_State232", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State230", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
deferrableTrigger251: BinaryAssociation = BinaryAssociation(
    name="deferrableTrigger251",
    ends={
        Property(name="pivot_Trigger", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State252", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region233: BinaryAssociation = BinaryAssociation(
    name="region233",
    ends={
        Property(name="pivot_Region235", type=pivot_State, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_State234", type=pivot_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredState253: BinaryAssociation = BinaryAssociation(
    name="referredState253",
    ends={
        Property(name="pivot_State254", type=pivot_StateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateExp", type=pivot_State, multiplicity=Multiplicity(0, 1))
    }
)
region255: BinaryAssociation = BinaryAssociation(
    name="region255",
    ends={
        Property(name="pivot_Region257", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine256", type=pivot_Region, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
connectionPoint258: BinaryAssociation = BinaryAssociation(
    name="connectionPoint258",
    ends={
        Property(name="pivot_Pseudostate260", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine259", type=pivot_Pseudostate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submachineState261: BinaryAssociation = BinaryAssociation(
    name="submachineState261",
    ends={
        Property(name="State", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="submachine", type=pivot_State, multiplicity=Multiplicity(0, 9999))
    }
)
extendedStateMachine263: BinaryAssociation = BinaryAssociation(
    name="extendedStateMachine263",
    ends={
        Property(name="pivot_StateMachine264", type=pivot_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_StateMachine262", type=pivot_StateMachine, multiplicity=Multiplicity(0, 9999))
    }
)
signature265: BinaryAssociation = BinaryAssociation(
    name="signature265",
    ends={
        Property(name="pivot_TemplateSignature", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateBinding", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameterSubstitution266: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution266",
    ends={
        Property(name="TemplateParameterSubstitution", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundElement267: BinaryAssociation = BinaryAssociation(
    name="boundElement267",
    ends={
        Property(name="TemplateableElement", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="templateBinding268", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
signature269: BinaryAssociation = BinaryAssociation(
    name="signature269",
    ends={
        Property(name="TemplateSignature", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter270", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1))
    }
)
parameteredElement271: BinaryAssociation = BinaryAssociation(
    name="parameteredElement271",
    ends={
        Property(name="ParameterableElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="templateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameteredElement272: BinaryAssociation = BinaryAssociation(
    name="ownedParameteredElement272",
    ends={
        Property(name="ParameterableElement273", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default274: BinaryAssociation = BinaryAssociation(
    name="default274",
    ends={
        Property(name="pivot_ParameterableElement", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameter", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1))
    }
)
ownedDefault275: BinaryAssociation = BinaryAssociation(
    name="ownedDefault275",
    ends={
        Property(name="pivot_ParameterableElement277", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameter276", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual280: BinaryAssociation = BinaryAssociation(
    name="actual280",
    ends={
        Property(name="pivot_ParameterableElement282", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution281", type=pivot_ParameterableElement, multiplicity=Multiplicity(1, 1))
    }
)
ownedActual283: BinaryAssociation = BinaryAssociation(
    name="ownedActual283",
    ends={
        Property(name="pivot_ParameterableElement285", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution284", type=pivot_ParameterableElement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding286: BinaryAssociation = BinaryAssociation(
    name="templateBinding286",
    ends={
        Property(name="TemplateBinding", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterSubstitution", type=pivot_TemplateBinding, multiplicity=Multiplicity(1, 1))
    }
)
parameter287: BinaryAssociation = BinaryAssociation(
    name="parameter287",
    ends={
        Property(name="pivot_TemplateParameter289", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateSignature288", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 9999))
    }
)
ownedParameter290: BinaryAssociation = BinaryAssociation(
    name="ownedParameter290",
    ends={
        Property(name="TemplateParameter291", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=pivot_TemplateParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formal278: BinaryAssociation = BinaryAssociation(
    name="formal278",
    ends={
        Property(name="pivot_TemplateParameter279", type=pivot_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateParameterSubstitution", type=pivot_TemplateParameter, multiplicity=Multiplicity(1, 1))
    }
)
template292: BinaryAssociation = BinaryAssociation(
    name="template292",
    ends={
        Property(name="TemplateableElement293", type=pivot_TemplateSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTemplateSignature", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1))
    }
)
templateBinding294: BinaryAssociation = BinaryAssociation(
    name="templateBinding294",
    ends={
        Property(name="TemplateBinding295", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="boundElement", type=pivot_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTemplateSignature296: BinaryAssociation = BinaryAssociation(
    name="ownedTemplateSignature296",
    ends={
        Property(name="TemplateSignature297", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="template", type=pivot_TemplateSignature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unspecializedElement299: BinaryAssociation = BinaryAssociation(
    name="unspecializedElement299",
    ends={
        Property(name="pivot_TemplateableElement", type=pivot_TemplateableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TemplateableElement298", type=pivot_TemplateableElement, multiplicity=Multiplicity(0, 1))
    }
)
source300: BinaryAssociation = BinaryAssociation(
    name="source300",
    ends={
        Property(name="Vertex301", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
target302: BinaryAssociation = BinaryAssociation(
    name="target302",
    ends={
        Property(name="Vertex303", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=pivot_Vertex, multiplicity=Multiplicity(1, 1))
    }
)
guard304: BinaryAssociation = BinaryAssociation(
    name="guard304",
    ends={
        Property(name="pivot_Constraint305", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Transition", type=pivot_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
effect306: BinaryAssociation = BinaryAssociation(
    name="effect306",
    ends={
        Property(name="pivot_Behavior308", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Transition307", type=pivot_Behavior, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger309: BinaryAssociation = BinaryAssociation(
    name="trigger309",
    ends={
        Property(name="pivot_Trigger311", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Transition310", type=pivot_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container312: BinaryAssociation = BinaryAssociation(
    name="container312",
    ends={
        Property(name="Region", type=pivot_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=pivot_Region, multiplicity=Multiplicity(1, 1))
    }
)
part313: BinaryAssociation = BinaryAssociation(
    name="part313",
    ends={
        Property(name="pivot_TupleLiteralPart", type=pivot_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralExp", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initExpression314: BinaryAssociation = BinaryAssociation(
    name="initExpression314",
    ends={
        Property(name="pivot_OCLExpression316", type=pivot_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TupleLiteralPart315", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package317: BinaryAssociation = BinaryAssociation(
    name="package317",
    ends={
        Property(name="Package318", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=pivot_Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute319: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute319",
    ends={
        Property(name="Property320", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType", type=pivot_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation321: BinaryAssociation = BinaryAssociation(
    name="ownedOperation321",
    ends={
        Property(name="Operation323", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="owningType322", type=pivot_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass325: BinaryAssociation = BinaryAssociation(
    name="superClass325",
    ends={
        Property(name="pivot_Type326", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Type324", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedInvariant327: BinaryAssociation = BinaryAssociation(
    name="ownedInvariant327",
    ends={
        Property(name="pivot_Constraint329", type=pivot_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Type328", type=pivot_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainingType332: BinaryAssociation = BinaryAssociation(
    name="constrainingType332",
    ends={
        Property(name="pivot_Type333", type=pivot_TypeTemplateParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypeTemplateParameter", type=pivot_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type334: BinaryAssociation = BinaryAssociation(
    name="type334",
    ends={
        Property(name="pivot_Type335", type=pivot_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypedElement", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
referredType330: BinaryAssociation = BinaryAssociation(
    name="referredType330",
    ends={
        Property(name="pivot_Type331", type=pivot_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_TypeExp", type=pivot_Type, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound336: BinaryAssociation = BinaryAssociation(
    name="lowerBound336",
    ends={
        Property(name="pivot_Type337", type=pivot_UnspecifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_UnspecifiedType", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
upperBound338: BinaryAssociation = BinaryAssociation(
    name="upperBound338",
    ends={
        Property(name="pivot_Type340", type=pivot_UnspecifiedType, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_UnspecifiedType339", type=pivot_Type, multiplicity=Multiplicity(1, 1))
    }
)
initExpression341: BinaryAssociation = BinaryAssociation(
    name="initExpression341",
    ends={
        Property(name="pivot_OCLExpression343", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable342", type=pivot_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
representedParameter344: BinaryAssociation = BinaryAssociation(
    name="representedParameter344",
    ends={
        Property(name="pivot_Parameter346", type=pivot_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_Variable345", type=pivot_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable347: BinaryAssociation = BinaryAssociation(
    name="referredVariable347",
    ends={
        Property(name="pivot_VariableDeclaration", type=pivot_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="pivot_VariableExp", type=pivot_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
container348: BinaryAssociation = BinaryAssociation(
    name="container348",
    ends={
        Property(name="Region349", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="subvertex", type=pivot_Region, multiplicity=Multiplicity(0, 1))
    }
)
outgoing350: BinaryAssociation = BinaryAssociation(
    name="outgoing350",
    ends={
        Property(name="Transition351", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incoming352: BinaryAssociation = BinaryAssociation(
    name="incoming352",
    ends={
        Property(name="Transition353", type=pivot_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=pivot_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_pivot_Annotation_NamedElement = Generalization(general=NamedElement, specific=pivot_Annotation)
gen_pivot_AnyType_Class = Generalization(general=Class_, specific=pivot_AnyType)
gen_pivot_AssociationClass_Class = Generalization(general=Class_, specific=pivot_AssociationClass)
gen_pivot_AssociationClassCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_AssociationClassCallExp)
gen_pivot_BagType_CollectionType = Generalization(general=CollectionType, specific=pivot_BagType)
gen_pivot_Behavior_Class = Generalization(general=Class_, specific=pivot_Behavior)
gen_pivot_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_BooleanLiteralExp)
gen_pivot_CallOperationAction_NamedElement = Generalization(general=NamedElement, specific=pivot_CallOperationAction)
gen_pivot_Class_Type = Generalization(general=Type, specific=pivot_Class)
gen_pivot_Class_Namespace = Generalization(general=Namespace, specific=pivot_Class)
gen_pivot_CallExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_CallExp)
gen_pivot_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionItem)
gen_pivot_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_CollectionLiteralExp)
gen_pivot_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=pivot_CollectionLiteralPart)
gen_pivot_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=pivot_CollectionRange)
gen_pivot_Comment_Element = Generalization(general=Element, specific=pivot_Comment)
gen_pivot_ConnectionPointReference_Vertex = Generalization(general=Vertex, specific=pivot_ConnectionPointReference)
gen_pivot_CollectionType_DataType = Generalization(general=DataType, specific=pivot_CollectionType)
gen_pivot_Constraint_NamedElement = Generalization(general=NamedElement, specific=pivot_Constraint)
gen_pivot_ConstructorPart_TypedElement = Generalization(general=TypedElement, specific=pivot_ConstructorPart)
gen_pivot_DataType_Class = Generalization(general=Class_, specific=pivot_DataType)
gen_pivot_Detail_NamedElement = Generalization(general=NamedElement, specific=pivot_Detail)
gen_pivot_DynamicElement_Element = Generalization(general=Element, specific=pivot_DynamicElement)
gen_pivot_DynamicProperty_Element = Generalization(general=Element, specific=pivot_DynamicProperty)
gen_pivot_ConstructorExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_ConstructorExp)
gen_pivot_Element_Visitable = Generalization(general=Visitable, specific=pivot_Element)
gen_pivot_DynamicType_Type = Generalization(general=Type, specific=pivot_DynamicType)
gen_pivot_DynamicType_DynamicElement = Generalization(general=DynamicElement, specific=pivot_DynamicType)
gen_pivot_Enumeration_DataType = Generalization(general=DataType, specific=pivot_Enumeration)
gen_pivot_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=pivot_EnumerationLiteral)
gen_pivot_ElementExtension_Type = Generalization(general=Type, specific=pivot_ElementExtension)
gen_pivot_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_EnumLiteralExp)
gen_pivot_Feature_TypedMultiplicityElement = Generalization(general=TypedMultiplicityElement, specific=pivot_Feature)
gen_pivot_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=pivot_FeatureCallExp)
gen_pivot_FinalState_State = Generalization(general=State, specific=pivot_FinalState)
gen_pivot_ExpressionInOCL_OpaqueExpression = Generalization(general=OpaqueExpression, specific=pivot_ExpressionInOCL)
gen_pivot_Import_NamedElement = Generalization(general=NamedElement, specific=pivot_Import)
gen_pivot_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_IntegerLiteralExp)
gen_pivot_IfExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_IfExp)
gen_pivot_Iteration_Operation = Generalization(general=Operation, specific=pivot_Iteration)
gen_pivot_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_InvalidLiteralExp)
gen_pivot_InvalidType_Class = Generalization(general=Class_, specific=pivot_InvalidType)
gen_pivot_IterateExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IterateExp)
gen_pivot_IterateExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IterateExp)
gen_pivot_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=pivot_IteratorExp)
gen_pivot_IteratorExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_IteratorExp)
gen_pivot_LambdaType_DataType = Generalization(general=DataType, specific=pivot_LambdaType)
gen_pivot_LetExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LetExp)
gen_pivot_Library_Package = Generalization(general=Package, specific=pivot_Library)
gen_pivot_LiteralExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_LiteralExp)
gen_pivot_LoopExp_CallExp = Generalization(general=CallExp, specific=pivot_LoopExp)
gen_pivot_MessageExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_MessageExp)
gen_pivot_MessageType_Type = Generalization(general=Type, specific=pivot_MessageType)
gen_pivot_Metaclass_Class = Generalization(general=Class_, specific=pivot_Metaclass)
gen_pivot_NamedElement_Element = Generalization(general=Element, specific=pivot_NamedElement)
gen_pivot_NamedElement_Nameable = Generalization(general=Nameable, specific=pivot_NamedElement)
gen_pivot_Namespace_NamedElement = Generalization(general=NamedElement, specific=pivot_Namespace)
gen_pivot_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_NavigationCallExp)
gen_pivot_NullLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NullLiteralExp)
gen_pivot_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_NumericLiteralExp)
gen_pivot_OCLExpression_TypedElement = Generalization(general=TypedElement, specific=pivot_OCLExpression)
gen_pivot_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=pivot_OpaqueExpression)
gen_pivot_Operation_Feature = Generalization(general=Feature, specific=pivot_Operation)
gen_pivot_Operation_Namespace = Generalization(general=Namespace, specific=pivot_Operation)
gen_pivot_Operation_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Operation)
gen_pivot_Operation_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Operation)
gen_pivot_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=pivot_OperationCallExp)
gen_pivot_OperationCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_OperationCallExp)
gen_pivot_OperationTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=pivot_OperationTemplateParameter)
gen_pivot_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=pivot_OrderedSetType)
gen_pivot_Package_Namespace = Generalization(general=Namespace, specific=pivot_Package)
gen_pivot_Package_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Package)
gen_pivot_PackageableElement_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_PackageableElement)
gen_pivot_Parameter_TypedMultiplicityElement = Generalization(general=TypedMultiplicityElement, specific=pivot_Parameter)
gen_pivot_Parameter_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Parameter)
gen_pivot_ParameterableElement_Element = Generalization(general=Element, specific=pivot_ParameterableElement)
gen_pivot_Precedence_NamedElement = Generalization(general=NamedElement, specific=pivot_Precedence)
gen_pivot_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_PrimitiveLiteralExp)
gen_pivot_PrimitiveType_DataType = Generalization(general=DataType, specific=pivot_PrimitiveType)
gen_pivot_Profile_Package = Generalization(general=Package, specific=pivot_Profile)
gen_pivot_Property_Feature = Generalization(general=Feature, specific=pivot_Property)
gen_pivot_Property_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Property)
gen_pivot_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=pivot_PropertyCallExp)
gen_pivot_PropertyCallExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_PropertyCallExp)
gen_pivot_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_RealLiteralExp)
gen_pivot_Pseudostate_Vertex = Generalization(general=Vertex, specific=pivot_Pseudostate)
gen_pivot_Root_Namespace = Generalization(general=Namespace, specific=pivot_Root)
gen_pivot_Region_Namespace = Generalization(general=Namespace, specific=pivot_Region)
gen_pivot_SelfType_Class = Generalization(general=Class_, specific=pivot_SelfType)
gen_pivot_SendSignalAction_NamedElement = Generalization(general=NamedElement, specific=pivot_SendSignalAction)
gen_pivot_SequenceType_CollectionType = Generalization(general=CollectionType, specific=pivot_SequenceType)
gen_pivot_SetType_CollectionType = Generalization(general=CollectionType, specific=pivot_SetType)
gen_pivot_Signal_NamedElement = Generalization(general=NamedElement, specific=pivot_Signal)
gen_pivot_State_Vertex = Generalization(general=Vertex, specific=pivot_State)
gen_pivot_State_Namespace = Generalization(general=Namespace, specific=pivot_State)
gen_pivot_StateMachine_Behavior = Generalization(general=Behavior, specific=pivot_StateMachine)
gen_pivot_StateExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_StateExp)
gen_pivot_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=pivot_StringLiteralExp)
gen_pivot_TemplateBinding_Element = Generalization(general=Element, specific=pivot_TemplateBinding)
gen_pivot_Stereotype_Class = Generalization(general=Class_, specific=pivot_Stereotype)
gen_pivot_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=pivot_TemplateParameterSubstitution)
gen_pivot_TemplateParameter_Element = Generalization(general=Element, specific=pivot_TemplateParameter)
gen_pivot_TemplateParameterType_Type = Generalization(general=Type, specific=pivot_TemplateParameterType)
gen_pivot_TemplateSignature_Element = Generalization(general=Element, specific=pivot_TemplateSignature)
gen_pivot_TemplateableElement_Element = Generalization(general=Element, specific=pivot_TemplateableElement)
gen_pivot_Transition_Namespace = Generalization(general=Namespace, specific=pivot_Transition)
gen_pivot_TupleLiteralPart_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_TupleLiteralPart)
gen_pivot_TupleType_DataType = Generalization(general=DataType, specific=pivot_TupleType)
gen_pivot_Type_NamedElement = Generalization(general=NamedElement, specific=pivot_Type)
gen_pivot_Type_TemplateableElement = Generalization(general=TemplateableElement, specific=pivot_Type)
gen_pivot_Type_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_Type)
gen_pivot_Trigger_NamedElement = Generalization(general=NamedElement, specific=pivot_Trigger)
gen_pivot_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=pivot_TupleLiteralExp)
gen_pivot_TypeExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_TypeExp)
gen_pivot_TypeExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_TypeExp)
gen_pivot_TypeTemplateParameter_TemplateParameter = Generalization(general=TemplateParameter, specific=pivot_TypeTemplateParameter)
gen_pivot_TypedElement_NamedElement = Generalization(general=NamedElement, specific=pivot_TypedElement)
gen_pivot_TypedMultiplicityElement_TypedElement = Generalization(general=TypedElement, specific=pivot_TypedMultiplicityElement)
gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=pivot_UnlimitedNaturalLiteralExp)
gen_pivot_UnspecifiedType_Class = Generalization(general=Class_, specific=pivot_UnspecifiedType)
gen_pivot_UnspecifiedValueExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_UnspecifiedValueExp)
gen_pivot_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=pivot_ValueSpecification)
gen_pivot_ValueSpecification_ParameterableElement = Generalization(general=ParameterableElement, specific=pivot_ValueSpecification)
gen_pivot_Variable_VariableDeclaration = Generalization(general=VariableDeclaration, specific=pivot_Variable)
gen_pivot_VariableDeclaration_TypedElement = Generalization(general=TypedElement, specific=pivot_VariableDeclaration)
gen_pivot_VariableExp_OCLExpression = Generalization(general=OCLExpression, specific=pivot_VariableExp)
gen_pivot_VariableExp_ReferringElement = Generalization(general=ReferringElement, specific=pivot_VariableExp)
gen_pivot_Vertex_NamedElement = Generalization(general=NamedElement, specific=pivot_Vertex)
gen_pivot_VoidType_Class = Generalization(general=Class_, specific=pivot_VoidType)

# Domain Model
domain_model = DomainModel(
    name="pivot",
    types={pivot_Annotation, NamedElement, pivot_AnyType, Class_, pivot_AssociationClass, pivot_Property, pivot_AssociationClassCallExp, NavigationCallExp, pivot_BagType, CollectionType, pivot_Behavior, pivot_BooleanLiteralExp, PrimitiveLiteralExp, pivot_Element, pivot_Detail, pivot_CallOperationAction, pivot_Operation, pivot_Class, Type, Namespace, pivot_CallExp, OCLExpression, pivot_OCLExpression, pivot_CollectionItem, CollectionLiteralPart, pivot_CollectionLiteralExp, LiteralExp, pivot_CollectionLiteralPart, TypedElement, pivot_CollectionRange, pivot_Type, pivot_Comment, Element, pivot_ConnectionPointReference, Vertex, pivot_Pseudostate, pivot_CollectionType, DataType, pivot_Constraint, pivot_OpaqueExpression, pivot_Namespace, pivot_State, pivot_DataType, pivot_DynamicElement, pivot_DynamicProperty, pivot_ConstructorExp, pivot_ConstructorPart, Visitable, pivot_ElementExtension, pivot_DynamicType, DynamicElement, pivot_EnumerationLiteral, pivot_Enumeration, pivot_EnumLiteralExp, pivot_Feature, TypedMultiplicityElement, pivot_FeatureCallExp, CallExp, pivot_FinalState, State, pivot_ExpressionInOCL, OpaqueExpression, pivot_Variable, pivot_Import, pivot_IntegerLiteralExp, NumericLiteralExp, pivot_IfExp, pivot_Iteration, Operation, pivot_InvalidLiteralExp, pivot_InvalidType, pivot_IterateExp, LoopExp, ReferringElement, pivot_Parameter, pivot_IteratorExp, pivot_LambdaType, pivot_LetExp, pivot_Library, Package, pivot_Precedence, pivot_LiteralExp, pivot_LoopExp, pivot_MessageExp, pivot_SendSignalAction, pivot_MessageType, pivot_Signal, pivot_Metaclass, pivot_MorePivotable, pivot_Nameable, pivot_NamedElement, Nameable, pivot_NavigationCallExp, FeatureCallExp, pivot_NullLiteralExp, pivot_NumericLiteralExp, ValueSpecification, Feature, TemplateableElement, ParameterableElement, pivot_OperationCallExp, pivot_OperationTemplateParameter, TemplateParameter, pivot_OrderedSetType, pivot_Package, pivot_PackageableElement, VariableDeclaration, pivot_ParameterableElement, pivot_TemplateParameter, pivot_Pivotable, pivot_PrimitiveLiteralExp, pivot_PrimitiveType, pivot_Profile, pivot_PropertyCallExp, pivot_RealLiteralExp, pivot_StateMachine, pivot_Root, pivot_ReferringElement, pivot_Region, pivot_Transition, pivot_Vertex, pivot_SelfType, pivot_SequenceType, pivot_SetType, pivot_Trigger, Behavior, pivot_StateExp, pivot_StringLiteralExp, pivot_TemplateBinding, pivot_TemplateSignature, pivot_TemplateParameterSubstitution, pivot_TemplateableElement, pivot_Stereotype, pivot_TemplateParameterType, pivot_TupleLiteralPart, pivot_TupleType, pivot_TupleLiteralExp, pivot_TypeExp, pivot_TypedElement, pivot_TypedMultiplicityElement, pivot_TypeTemplateParameter, pivot_UnlimitedNaturalLiteralExp, pivot_UnspecifiedType, pivot_UnspecifiedValueExp, pivot_ValueSpecification, pivot_VariableDeclaration, pivot_VariableExp, pivot_Visitable, pivot_Visitor, pivot_VoidType, AssociativityKind, CollectionKind, PseudostateKind, TransitionKind},
    associations={unownedAttribute6, referredAssociationClass7, ownedContent0, ownedDetail1, reference3, operation9, source8, item11, ownedBehavior10, part13, first14, elementType19, annotatedElement20, entry22, last16, constrainedElement28, specification30, context32, state23, exit25, referredProperty35, initExpression37, behavioralType40, metaType42, part34, ownedProperty46, ownedComment48, extension51, referredProperty44, referredEnumLiteral55, ownedLiteral56, enumeration57, stereotype52, base54, contextVariable60, resultVariable62, parameterVariable65, messageExpression68, bodyExpression58, condition71, thenExpression73, elseExpression76, importedNamespace79, result81, ownedIterator83, ownedAccumulator84, contextType87, parameterType89, resultType92, in95, variable97, ownedPrecedence100, body101, iterator103, referredIteration106, target109, argument111, calledOperation114, sentSignal117, referredSignal119, referredOperation120, instanceType123, ownedAnnotation125, ownedRule127, qualifier130, navigationSource132, bodyExpression146, raisedException135, ownedParameter138, owningType139, precondition140, postcondition143, precedence149, redefinedOperation153, class155, importedPackage169, argument158, referredOperation160, nestedPackage164, nestingPackage166, ownedType170, operation172, owningTemplateParameter173, templateParameter174, class176, opposite180, association182, defaultExpression183, keys187, redefinedProperty190, subsettedProperty193, referredProperty196, owningType198, referredProperty200, stateMachine202, state204, nestedPackage218, transition207, stateMachine208, state210, extendedRegion214, subvertex216, imports220, signal223, submachine226, connection227, stateInvariant236, entry239, exit242, doActivity245, connectionPoint248, redefinedState231, deferrableTrigger251, region233, referredState253, region255, connectionPoint258, submachineState261, extendedStateMachine263, signature265, parameterSubstitution266, boundElement267, signature269, parameteredElement271, ownedParameteredElement272, default274, ownedDefault275, actual280, ownedActual283, templateBinding286, parameter287, ownedParameter290, formal278, template292, templateBinding294, ownedTemplateSignature296, unspecializedElement299, source300, target302, guard304, effect306, trigger309, container312, part313, initExpression314, package317, ownedAttribute319, ownedOperation321, superClass325, ownedInvariant327, constrainingType332, type334, referredType330, lowerBound336, upperBound338, initExpression341, representedParameter344, referredVariable347, container348, outgoing350, incoming352},
    generalizations={gen_pivot_Annotation_NamedElement, gen_pivot_AnyType_Class, gen_pivot_AssociationClass_Class, gen_pivot_AssociationClassCallExp_NavigationCallExp, gen_pivot_BagType_CollectionType, gen_pivot_Behavior_Class, gen_pivot_BooleanLiteralExp_PrimitiveLiteralExp, gen_pivot_CallOperationAction_NamedElement, gen_pivot_Class_Type, gen_pivot_Class_Namespace, gen_pivot_CallExp_OCLExpression, gen_pivot_CollectionItem_CollectionLiteralPart, gen_pivot_CollectionLiteralExp_LiteralExp, gen_pivot_CollectionLiteralPart_TypedElement, gen_pivot_CollectionRange_CollectionLiteralPart, gen_pivot_Comment_Element, gen_pivot_ConnectionPointReference_Vertex, gen_pivot_CollectionType_DataType, gen_pivot_Constraint_NamedElement, gen_pivot_ConstructorPart_TypedElement, gen_pivot_DataType_Class, gen_pivot_Detail_NamedElement, gen_pivot_DynamicElement_Element, gen_pivot_DynamicProperty_Element, gen_pivot_ConstructorExp_OCLExpression, gen_pivot_Element_Visitable, gen_pivot_DynamicType_Type, gen_pivot_DynamicType_DynamicElement, gen_pivot_Enumeration_DataType, gen_pivot_EnumerationLiteral_NamedElement, gen_pivot_ElementExtension_Type, gen_pivot_EnumLiteralExp_LiteralExp, gen_pivot_Feature_TypedMultiplicityElement, gen_pivot_FeatureCallExp_CallExp, gen_pivot_FinalState_State, gen_pivot_ExpressionInOCL_OpaqueExpression, gen_pivot_Import_NamedElement, gen_pivot_IntegerLiteralExp_NumericLiteralExp, gen_pivot_IfExp_OCLExpression, gen_pivot_Iteration_Operation, gen_pivot_InvalidLiteralExp_LiteralExp, gen_pivot_InvalidType_Class, gen_pivot_IterateExp_LoopExp, gen_pivot_IterateExp_ReferringElement, gen_pivot_IteratorExp_LoopExp, gen_pivot_IteratorExp_ReferringElement, gen_pivot_LambdaType_DataType, gen_pivot_LetExp_OCLExpression, gen_pivot_Library_Package, gen_pivot_LiteralExp_OCLExpression, gen_pivot_LoopExp_CallExp, gen_pivot_MessageExp_OCLExpression, gen_pivot_MessageType_Type, gen_pivot_Metaclass_Class, gen_pivot_NamedElement_Element, gen_pivot_NamedElement_Nameable, gen_pivot_Namespace_NamedElement, gen_pivot_NavigationCallExp_FeatureCallExp, gen_pivot_NullLiteralExp_PrimitiveLiteralExp, gen_pivot_NumericLiteralExp_PrimitiveLiteralExp, gen_pivot_OCLExpression_TypedElement, gen_pivot_OpaqueExpression_ValueSpecification, gen_pivot_Operation_Feature, gen_pivot_Operation_Namespace, gen_pivot_Operation_TemplateableElement, gen_pivot_Operation_ParameterableElement, gen_pivot_OperationCallExp_FeatureCallExp, gen_pivot_OperationCallExp_ReferringElement, gen_pivot_OperationTemplateParameter_TemplateParameter, gen_pivot_OrderedSetType_CollectionType, gen_pivot_Package_Namespace, gen_pivot_Package_TemplateableElement, gen_pivot_PackageableElement_ParameterableElement, gen_pivot_Parameter_TypedMultiplicityElement, gen_pivot_Parameter_VariableDeclaration, gen_pivot_ParameterableElement_Element, gen_pivot_Precedence_NamedElement, gen_pivot_PrimitiveLiteralExp_LiteralExp, gen_pivot_PrimitiveType_DataType, gen_pivot_Profile_Package, gen_pivot_Property_Feature, gen_pivot_Property_ParameterableElement, gen_pivot_PropertyCallExp_NavigationCallExp, gen_pivot_PropertyCallExp_ReferringElement, gen_pivot_RealLiteralExp_NumericLiteralExp, gen_pivot_Pseudostate_Vertex, gen_pivot_Root_Namespace, gen_pivot_Region_Namespace, gen_pivot_SelfType_Class, gen_pivot_SendSignalAction_NamedElement, gen_pivot_SequenceType_CollectionType, gen_pivot_SetType_CollectionType, gen_pivot_Signal_NamedElement, gen_pivot_State_Vertex, gen_pivot_State_Namespace, gen_pivot_StateMachine_Behavior, gen_pivot_StateExp_OCLExpression, gen_pivot_StringLiteralExp_PrimitiveLiteralExp, gen_pivot_TemplateBinding_Element, gen_pivot_Stereotype_Class, gen_pivot_TemplateParameterSubstitution_Element, gen_pivot_TemplateParameter_Element, gen_pivot_TemplateParameterType_Type, gen_pivot_TemplateSignature_Element, gen_pivot_TemplateableElement_Element, gen_pivot_Transition_Namespace, gen_pivot_TupleLiteralPart_VariableDeclaration, gen_pivot_TupleType_DataType, gen_pivot_Type_NamedElement, gen_pivot_Type_TemplateableElement, gen_pivot_Type_ParameterableElement, gen_pivot_Trigger_NamedElement, gen_pivot_TupleLiteralExp_LiteralExp, gen_pivot_TypeExp_OCLExpression, gen_pivot_TypeExp_ReferringElement, gen_pivot_TypeTemplateParameter_TemplateParameter, gen_pivot_TypedElement_NamedElement, gen_pivot_TypedMultiplicityElement_TypedElement, gen_pivot_UnlimitedNaturalLiteralExp_NumericLiteralExp, gen_pivot_UnspecifiedType_Class, gen_pivot_UnspecifiedValueExp_OCLExpression, gen_pivot_ValueSpecification_TypedElement, gen_pivot_ValueSpecification_ParameterableElement, gen_pivot_Variable_VariableDeclaration, gen_pivot_VariableDeclaration_TypedElement, gen_pivot_VariableExp_OCLExpression, gen_pivot_VariableExp_ReferringElement, gen_pivot_Vertex_NamedElement, gen_pivot_VoidType_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)