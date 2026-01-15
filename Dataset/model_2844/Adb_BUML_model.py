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
adb_Compilation = Class(name="adb::Compilation")
adb_CompilationUnit = Class(name="adb::CompilationUnit")
adb_LibraryUnitDeclaration = Class(name="adb::LibraryUnitDeclaration")
adb_UseClause = Class(name="adb::UseClause")
BasicDeclarativeItem = Class(name="BasicDeclarativeItem")
GenericItem = Class(name="GenericItem")
adb_UsePackageClause = Class(name="adb::UsePackageClause")
UseClause = Class(name="UseClause")
adb_ContextClause = Class(name="adb::ContextClause")
adb_Unit = Class(name="adb::Unit")
adb_Pragma = Class(name="adb::Pragma")
adb_ContextItem = Class(name="adb::ContextItem")
adb_WithClause = Class(name="adb::WithClause")
ContextItem = Class(name="ContextItem")
adb_PackageDefinition = Class(name="adb::PackageDefinition")
PackageDeclaration = Class(name="PackageDeclaration")
LibrarySpecification = Class(name="LibrarySpecification")
adb_PackageSpecification = Class(name="adb::PackageSpecification")
adb_Renaming = Class(name="adb::Renaming")
adb_GenericDeclaration = Class(name="adb::GenericDeclaration")
adb_GenericItems = Class(name="adb::GenericItems")
adb_UseTypeClause = Class(name="adb::UseTypeClause")
Unit = Class(name="Unit")
adb_LibraryUnitSpecification = Class(name="adb::LibraryUnitSpecification")
adb_PackageDeclaration = Class(name="adb::PackageDeclaration")
LibraryUnitSpecification = Class(name="LibraryUnitSpecification")
BasicDeclaration = Class(name="BasicDeclaration")
adb_SubprogramBody = Class(name="adb::SubprogramBody")
DeclarativeBlock = Class(name="DeclarativeBlock")
ProperBody = Class(name="ProperBody")
ProtectedOperationItem = Class(name="ProtectedOperationItem")
adb_SubprogramSpecification = Class(name="adb::SubprogramSpecification")
adb_LibrarySpecification = Class(name="adb::LibrarySpecification")
adb_GenericInstantiation = Class(name="adb::GenericInstantiation")
adb_OverridingIndicator = Class(name="adb::OverridingIndicator")
adb_GenericActualPart = Class(name="adb::GenericActualPart")
adb_BasicDeclarativeItem = Class(name="adb::BasicDeclarativeItem")
adb_InterfaceList = Class(name="adb::InterfaceList")
adb_TaskDefinition = Class(name="adb::TaskDefinition")
adb_TypeDeclaration = Class(name="adb::TypeDeclaration")
adb_DeclarativeBlock = Class(name="adb::DeclarativeBlock")
adb_DeclarativeItem = Class(name="adb::DeclarativeItem")
adb_HandledSequenceOfStatements = Class(name="adb::HandledSequenceOfStatements")
DeclarativeItem = Class(name="DeclarativeItem")
adb_BasicDeclaration = Class(name="adb::BasicDeclaration")
adb_TaskDeclaration = Class(name="adb::TaskDeclaration")
adb_KnownDiscriminantPart = Class(name="adb::KnownDiscriminantPart")
adb_PrivateExtensionDeclaration = Class(name="adb::PrivateExtensionDeclaration")
adb_NewTypeDeclaration = Class(name="adb::NewTypeDeclaration")
TypeDeclaration = Class(name="TypeDeclaration")
adb_FullTypeDeclaration = Class(name="adb::FullTypeDeclaration")
NewTypeDeclaration = Class(name="NewTypeDeclaration")
adb_FullDataTypeDeclaration = Class(name="adb::FullDataTypeDeclaration")
FullTypeDeclaration = Class(name="FullTypeDeclaration")
adb_TypeDefinition = Class(name="adb::TypeDefinition")
adb_IncompleteTypeDeclaration = Class(name="adb::IncompleteTypeDeclaration")
adb_DiscriminantPart = Class(name="adb::DiscriminantPart")
adb_PrivateTypeDeclaration = Class(name="adb::PrivateTypeDeclaration")
adb_ProtectedTypeDeclaration = Class(name="adb::ProtectedTypeDeclaration")
adb_ProtectedDefinition = Class(name="adb::ProtectedDefinition")
adb_SubtypeIndication = Class(name="adb::SubtypeIndication")
adb_TaskItem = Class(name="adb::TaskItem")
adb_EntryDeclaration = Class(name="adb::EntryDeclaration")
TaskItem = Class(name="TaskItem")
ProtectedOperationDeclaration = Class(name="ProtectedOperationDeclaration")
adb_DiscreteSubtypeDefinition = Class(name="adb::DiscreteSubtypeDefinition")
adb_FormalPart = Class(name="adb::FormalPart")
adb_ProcedureSpecification = Class(name="adb::ProcedureSpecification")
SubprogramSpecification = Class(name="SubprogramSpecification")
adb_FunctionSpecification = Class(name="adb::FunctionSpecification")
adb_ParameterAndResultProfile = Class(name="adb::ParameterAndResultProfile")
adb_ExceptionChoice = Class(name="adb::ExceptionChoice")
adb_Name = Class(name="adb::Name")
adb_ProtectedElementDeclaration = Class(name="adb::ProtectedElementDeclaration")
adb_ProtectedOperationDeclaration = Class(name="adb::ProtectedOperationDeclaration")
ProtectedElementDeclaration = Class(name="ProtectedElementDeclaration")
adb_SubprogramDeclaration = Class(name="adb::SubprogramDeclaration")
BodyStub = Class(name="BodyStub")
adb_LabelisableStatement = Class(name="adb::LabelisableStatement")
adb_Statement = Class(name="adb::Statement")
adb_SimpleStatement = Class(name="adb::SimpleStatement")
Statement = Class(name="Statement")
adb_ExceptionHandler = Class(name="adb::ExceptionHandler")
adb_SequenceOfStatements = Class(name="adb::SequenceOfStatements")
adb_Body = Class(name="adb::Body")
adb_ProperBody = Class(name="adb::ProperBody")
Body = Class(name="Body")
adb_Label = Class(name="adb::Label")
HandledSequenceOfStatements = Class(name="HandledSequenceOfStatements")
AbortablePart = Class(name="AbortablePart")
adb_Mode = Class(name="adb::Mode")
adb_OptNullExclusion = Class(name="adb::OptNullExclusion")
adb_AnonymousAccessDefinition = Class(name="adb::AnonymousAccessDefinition")
adb_Expression = Class(name="adb::Expression")
adb_CompoundStatement = Class(name="adb::CompoundStatement")
adb_NullStatement = Class(name="adb::NullStatement")
SimpleStatement = Class(name="SimpleStatement")
adb_GenericItem = Class(name="adb::GenericItem")
adb_GenericFormalParameterDeclaration = Class(name="adb::GenericFormalParameterDeclaration")
adb_FormalObjectDeclaration = Class(name="adb::FormalObjectDeclaration")
GenericFormalParameterDeclaration = Class(name="GenericFormalParameterDeclaration")
adb_DefiningIdentifierList = Class(name="adb::DefiningIdentifierList")
adb_FormalSubprogramDeclaration = Class(name="adb::FormalSubprogramDeclaration")
adb_SubprogramDefault = Class(name="adb::SubprogramDefault")
adb_FormalTypeDeclaration = Class(name="adb::FormalTypeDeclaration")
adb_FormalTypeDefinition = Class(name="adb::FormalTypeDefinition")
adb_FormalPrivateTypeDefinition = Class(name="adb::FormalPrivateTypeDefinition")
FormalTypeDefinition = Class(name="FormalTypeDefinition")
adb_FormalDerivedTypeDefinition = Class(name="adb::FormalDerivedTypeDefinition")
adb_FormalPackageAssociation = Class(name="adb::FormalPackageAssociation")
adb_GenericAssociation = Class(name="adb::GenericAssociation")
adb_ExceptionDeclaration = Class(name="adb::ExceptionDeclaration")
adb_ObjectDeclaration = Class(name="adb::ObjectDeclaration")
adb_DataInstanceDeclaration = Class(name="adb::DataInstanceDeclaration")
adb_FormalPackageDeclaration = Class(name="adb::FormalPackageDeclaration")
adb_FormalPackageActualPart = Class(name="adb::FormalPackageActualPart")
adb_ArrayTypeDefinition = Class(name="adb::ArrayTypeDefinition")
adb_SingleProtectedDeclaration = Class(name="adb::SingleProtectedDeclaration")
ObjectDeclaration = Class(name="ObjectDeclaration")
adb_NumberDeclaration = Class(name="adb::NumberDeclaration")
adb_AssignmentStatement = Class(name="adb::AssignmentStatement")
adb_PragmaArgumentAssociation = Class(name="adb::PragmaArgumentAssociation")
adb_SubtypeDeclaration = Class(name="adb::SubtypeDeclaration")
adb_CaseStatement = Class(name="adb::CaseStatement")
adb_CaseStatementAlternative = Class(name="adb::CaseStatementAlternative")
adb_DiscreteChoiceList = Class(name="adb::DiscreteChoiceList")
adb_LoopStatement = Class(name="adb::LoopStatement")
adb_IfStatement = Class(name="adb::IfStatement")
CompoundStatement = Class(name="CompoundStatement")
adb_IterationScheme = Class(name="adb::IterationScheme")
adb_BlockStatement = Class(name="adb::BlockStatement")
adb_ExitStatement = Class(name="adb::ExitStatement")
adb_GotoStatement = Class(name="adb::GotoStatement")
adb_LoopParameterSpecification = Class(name="adb::LoopParameterSpecification")
adb_ReturnSubtypeIndication = Class(name="adb::ReturnSubtypeIndication")
adb_PackageBody = Class(name="adb::PackageBody")
adb_ProcedureOrEntryCallStatement = Class(name="adb::ProcedureOrEntryCallStatement")
TriggeringStatement = Class(name="TriggeringStatement")
adb_SimpleReturnStatement = Class(name="adb::SimpleReturnStatement")
adb_ExtendedReturnStatement = Class(name="adb::ExtendedReturnStatement")
adb_ProtectedOperationItem = Class(name="adb::ProtectedOperationItem")
adb_AcceptStatement = Class(name="adb::AcceptStatement")
adb_EntryIndex = Class(name="adb::EntryIndex")
adb_TaskBody = Class(name="adb::TaskBody")
adb_ProtectedBody = Class(name="adb::ProtectedBody")
adb_EntryIndexSpecification = Class(name="adb::EntryIndexSpecification")
adb_EntryBody = Class(name="adb::EntryBody")
adb_EntryBodyFormalPart = Class(name="adb::EntryBodyFormalPart")
adb_SelectiveAccept = Class(name="adb::SelectiveAccept")
adb_EntryBarrier = Class(name="adb::EntryBarrier")
SelectStatement = Class(name="SelectStatement")
adb_Guard = Class(name="adb::Guard")
adb_SelectAlternative = Class(name="adb::SelectAlternative")
adb_GuardedAlternative = Class(name="adb::GuardedAlternative")
adb_RequeueStatement = Class(name="adb::RequeueStatement")
adb_DelayStatement = Class(name="adb::DelayStatement")
adb_SelectStatement = Class(name="adb::SelectStatement")
adb_DelayAlternative = Class(name="adb::DelayAlternative")
adb_TimedEntryCall = Class(name="adb::TimedEntryCall")
adb_EntryCallAlternative = Class(name="adb::EntryCallAlternative")
adb_AcceptAlternative = Class(name="adb::AcceptAlternative")
SelectAlternative = Class(name="SelectAlternative")
adb_AsynchronousSelect = Class(name="adb::AsynchronousSelect")
adb_TriggeringAlternative = Class(name="adb::TriggeringAlternative")
adb_AbortablePart = Class(name="adb::AbortablePart")
adb_TriggeringStatement = Class(name="adb::TriggeringStatement")
adb_ConditionalEntryCall = Class(name="adb::ConditionalEntryCall")
adb_RaiseStatement = Class(name="adb::RaiseStatement")
adb_AbortStatement = Class(name="adb::AbortStatement")
adb_TaskNames = Class(name="adb::TaskNames")
AbortStatement = Class(name="AbortStatement")
adb_BodyStub = Class(name="adb::BodyStub")
adb_PackageBodyStub = Class(name="adb::PackageBodyStub")
adb_TaskBodyStub = Class(name="adb::TaskBodyStub")
adb_ProtectedBodyStub = Class(name="adb::ProtectedBodyStub")
adb_SeparateSubunit = Class(name="adb::SeparateSubunit")
adb_NotNullAccessDefinition = Class(name="adb::NotNullAccessDefinition")
adb_ExplicitGenericActualParameter = Class(name="adb::ExplicitGenericActualParameter")
adb_UnknownDiscriminantPart = Class(name="adb::UnknownDiscriminantPart")
DiscriminantPart = Class(name="DiscriminantPart")
adb_DiscriminantSpecification = Class(name="adb::DiscriminantSpecification")
adb_RecordExtensionPart = Class(name="adb::RecordExtensionPart")
adb_RecordDefinition = Class(name="adb::RecordDefinition")
adb_AccessTypeDefinition = Class(name="adb::AccessTypeDefinition")
adb_InterfaceTypeDefinition = Class(name="adb::InterfaceTypeDefinition")
adb_AccessSpecification = Class(name="adb::AccessSpecification")
TypeDefinition = Class(name="TypeDefinition")
adb_AccessToSubprogramDefinition = Class(name="adb::AccessToSubprogramDefinition")
AccessSpecification = Class(name="AccessSpecification")
NotNullAccessDefinition = Class(name="NotNullAccessDefinition")
adb_DerivedTypeDefinition = Class(name="adb::DerivedTypeDefinition")
adb_AccessToDataDefinition = Class(name="adb::AccessToDataDefinition")
ReturnSubtypeIndication = Class(name="ReturnSubtypeIndication")
adb_ArrayIndexes = Class(name="adb::ArrayIndexes")
adb_ComponentDefinition = Class(name="adb::ComponentDefinition")
adb_UnconstrainedIndexes = Class(name="adb::UnconstrainedIndexes")
ArrayIndexes = Class(name="ArrayIndexes")
adb_ConstrainedIndexes = Class(name="adb::ConstrainedIndexes")
adb_AccessToDataInstance = Class(name="adb::AccessToDataInstance")
adb_ParameterSpecification = Class(name="adb::ParameterSpecification")
adb_ModularTypeDefinition = Class(name="adb::ModularTypeDefinition")
adb_IntegerTypeDefinition = Class(name="adb::IntegerTypeDefinition")
adb_SignedIntegerTypeDefinition = Class(name="adb::SignedIntegerTypeDefinition")
IntegerTypeDefinition = Class(name="IntegerTypeDefinition")
adb_SimpleExpression = Class(name="adb::SimpleExpression")
adb_OptVariantPart = Class(name="adb::OptVariantPart")
adb_VariantPart = Class(name="adb::VariantPart")
adb_EnumerationTypeDefinition = Class(name="adb::EnumerationTypeDefinition")
adb_RecordTypeDefinition = Class(name="adb::RecordTypeDefinition")
adb_ComponentList = Class(name="adb::ComponentList")
adb_ComponentItem = Class(name="adb::ComponentItem")
adb_ComponentClause = Class(name="adb::ComponentClause")
adb_ComponentDeclaration = Class(name="adb::ComponentDeclaration")
ComponentItem = Class(name="ComponentItem")
adb_AspectClause = Class(name="adb::AspectClause")
adb_ModClause = Class(name="adb::ModClause")
adb_Variant = Class(name="adb::Variant")
ExplicitGenericActualParameter = Class(name="ExplicitGenericActualParameter")
DiscreteChoice = Class(name="DiscreteChoice")
adb_DiscreteChoice = Class(name="adb::DiscreteChoice")
adb_RealTypeDefinition = Class(name="adb::RealTypeDefinition")
adb_RealRangeSpecification = Class(name="adb::RealRangeSpecification")
adb_FloatingPointDefinition = Class(name="adb::FloatingPointDefinition")
RealTypeDefinition = Class(name="RealTypeDefinition")
adb_FixedPointDefinition = Class(name="adb::FixedPointDefinition")
EntryIndex = Class(name="EntryIndex")
adb_Term = Class(name="adb::Term")
AncestorPart = Class(name="AncestorPart")
ParameterEffectiveValue = Class(name="ParameterEffectiveValue")
adb_Relation = Class(name="adb::Relation")
adb_Membership = Class(name="adb::Membership")
adb_Interval = Class(name="adb::Interval")
adb_Factor = Class(name="adb::Factor")
adb_Primary = Class(name="adb::Primary")
adb_NumericLiteral = Class(name="adb::NumericLiteral")
Primary = Class(name="Primary")
adb_Null = Class(name="adb::Null")
adb_StringLiteral = Class(name="adb::StringLiteral")
adb_EObject = Class(name="adb::EObject")
adb_QualifiedName = Class(name="adb::QualifiedName")
adb_Qualifier = Class(name="adb::Qualifier")
adb_ParenthesizedExpression = Class(name="adb::ParenthesizedExpression")
adb_Allocator = Class(name="adb::Allocator")
DiscreteSubtypeDefinition = Class(name="DiscreteSubtypeDefinition")
DiscreteRange = Class(name="DiscreteRange")
adb_OptConstraint = Class(name="adb::OptConstraint")
adb_IndexConstraint = Class(name="adb::IndexConstraint")
adb_DiscreteRange = Class(name="adb::DiscreteRange")
adb_ScalarConstraint = Class(name="adb::ScalarConstraint")
adb_DigitsConstraint = Class(name="adb::DigitsConstraint")
ScalarConstraint = Class(name="ScalarConstraint")
adb_RangeConstraint = Class(name="adb::RangeConstraint")
adb_DeltaConstraint = Class(name="adb::DeltaConstraint")
adb_CompositeConstraint = Class(name="adb::CompositeConstraint")
adb_DiscriminantConstraint = Class(name="adb::DiscriminantConstraint")
CompositeConstraint = Class(name="CompositeConstraint")
adb_DiscriminantAssociation = Class(name="adb::DiscriminantAssociation")
adb_RecordAggregate = Class(name="adb::RecordAggregate")
Aggregate = Class(name="Aggregate")
adb_RecordComponentAssociationList = Class(name="adb::RecordComponentAssociationList")
RecordAggregate = Class(name="RecordAggregate")
adb_DiscriminantSelectors = Class(name="adb::DiscriminantSelectors")
adb_ComponentChoiceList = Class(name="adb::ComponentChoiceList")
adb_Aggregate = Class(name="adb::Aggregate")
ParenthesizedExpression = Class(name="ParenthesizedExpression")
Qualifier = Class(name="Qualifier")
adb_ArrayAggregate = Class(name="adb::ArrayAggregate")
adb_PositionalArrayAggregate = Class(name="adb::PositionalArrayAggregate")
ArrayAggregate = Class(name="ArrayAggregate")
adb_RecordComponentAssociation = Class(name="adb::RecordComponentAssociation")
adb_InitializedComponents = Class(name="adb::InitializedComponents")
RecordComponentAssociation = Class(name="RecordComponentAssociation")
adb_UninitializedComponents = Class(name="adb::UninitializedComponents")
adb_ExtensionAggregate = Class(name="adb::ExtensionAggregate")
adb_AncestorPart = Class(name="adb::AncestorPart")
adb_PrimaryName = Class(name="adb::PrimaryName")
adb_ParameterAssociation = Class(name="adb::ParameterAssociation")
adb_NamedArrayAggregate = Class(name="adb::NamedArrayAggregate")
adb_ArrayComponentAssociation = Class(name="adb::ArrayComponentAssociation")
Interval = Class(name="Interval")
adb_EntityRange = Class(name="adb::EntityRange")
Range = Class(name="Range")
adb_AttributeDesignator = Class(name="adb::AttributeDesignator")
adb_ParameterEffectiveValue = Class(name="adb::ParameterEffectiveValue")
adb_Range = Class(name="adb::Range")
RangeConstraint = Class(name="RangeConstraint")
adb_ExplicitRange = Class(name="adb::ExplicitRange")

# adb_Compilation class attributes and methods

# adb_CompilationUnit class attributes and methods

# adb_LibraryUnitDeclaration class attributes and methods
adb_LibraryUnitDeclaration_private: Property = Property(name="private", type=BooleanType)
adb_LibraryUnitDeclaration.attributes={adb_LibraryUnitDeclaration_private}

# adb_UseClause class attributes and methods

# BasicDeclarativeItem class attributes and methods

# GenericItem class attributes and methods

# adb_UsePackageClause class attributes and methods

# UseClause class attributes and methods

# adb_ContextClause class attributes and methods

# adb_Unit class attributes and methods

# adb_Pragma class attributes and methods
adb_Pragma_name: Property = Property(name="name", type=StringType)
adb_Pragma.attributes={adb_Pragma_name}

# adb_ContextItem class attributes and methods

# adb_WithClause class attributes and methods
adb_WithClause_limited: Property = Property(name="limited", type=BooleanType)
adb_WithClause_private: Property = Property(name="private", type=BooleanType)
adb_WithClause.attributes={adb_WithClause_limited, adb_WithClause_private}

# ContextItem class attributes and methods

# adb_PackageDefinition class attributes and methods

# PackageDeclaration class attributes and methods

# LibrarySpecification class attributes and methods

# adb_PackageSpecification class attributes and methods
adb_PackageSpecification_endname: Property = Property(name="endname", type=StringType)
adb_PackageSpecification.attributes={adb_PackageSpecification_endname}

# adb_Renaming class attributes and methods
adb_Renaming_renamed: Property = Property(name="renamed", type=StringType)
adb_Renaming.attributes={adb_Renaming_renamed}

# adb_GenericDeclaration class attributes and methods

# adb_GenericItems class attributes and methods

# adb_UseTypeClause class attributes and methods
adb_UseTypeClause_typesNames: Property = Property(name="typesNames", type=StringType)
adb_UseTypeClause_useTypeRefs: Property = Property(name="useTypeRefs", type=StringType)
adb_UseTypeClause.attributes={adb_UseTypeClause_typesNames, adb_UseTypeClause_useTypeRefs}

# Unit class attributes and methods

# adb_LibraryUnitSpecification class attributes and methods

# adb_PackageDeclaration class attributes and methods
adb_PackageDeclaration_name: Property = Property(name="name", type=StringType)
adb_PackageDeclaration.attributes={adb_PackageDeclaration_name}

# LibraryUnitSpecification class attributes and methods

# BasicDeclaration class attributes and methods

# adb_SubprogramBody class attributes and methods
adb_SubprogramBody_endname: Property = Property(name="endname", type=StringType)
adb_SubprogramBody.attributes={adb_SubprogramBody_endname}

# DeclarativeBlock class attributes and methods

# ProperBody class attributes and methods

# ProtectedOperationItem class attributes and methods

# adb_SubprogramSpecification class attributes and methods

# adb_LibrarySpecification class attributes and methods

# adb_GenericInstantiation class attributes and methods
adb_GenericInstantiation_name: Property = Property(name="name", type=StringType)
adb_GenericInstantiation_genericName: Property = Property(name="genericName", type=StringType)
adb_GenericInstantiation.attributes={adb_GenericInstantiation_name, adb_GenericInstantiation_genericName}

# adb_OverridingIndicator class attributes and methods
adb_OverridingIndicator_not: Property = Property(name="not", type=BooleanType)
adb_OverridingIndicator.attributes={adb_OverridingIndicator_not}

# adb_GenericActualPart class attributes and methods

# adb_BasicDeclarativeItem class attributes and methods

# adb_InterfaceList class attributes and methods

# adb_TaskDefinition class attributes and methods

# adb_TypeDeclaration class attributes and methods
adb_TypeDeclaration_name: Property = Property(name="name", type=StringType)
adb_TypeDeclaration.attributes={adb_TypeDeclaration_name}

# adb_DeclarativeBlock class attributes and methods

# adb_DeclarativeItem class attributes and methods

# adb_HandledSequenceOfStatements class attributes and methods

# DeclarativeItem class attributes and methods

# adb_BasicDeclaration class attributes and methods

# adb_TaskDeclaration class attributes and methods
adb_TaskDeclaration_name: Property = Property(name="name", type=StringType)
adb_TaskDeclaration.attributes={adb_TaskDeclaration_name}

# adb_KnownDiscriminantPart class attributes and methods

# adb_PrivateExtensionDeclaration class attributes and methods
adb_PrivateExtensionDeclaration_abstract: Property = Property(name="abstract", type=BooleanType)
adb_PrivateExtensionDeclaration_limited: Property = Property(name="limited", type=BooleanType)
adb_PrivateExtensionDeclaration_synchronized: Property = Property(name="synchronized", type=BooleanType)
adb_PrivateExtensionDeclaration.attributes={adb_PrivateExtensionDeclaration_limited, adb_PrivateExtensionDeclaration_synchronized, adb_PrivateExtensionDeclaration_abstract}

# adb_NewTypeDeclaration class attributes and methods

# TypeDeclaration class attributes and methods

# adb_FullTypeDeclaration class attributes and methods

# NewTypeDeclaration class attributes and methods

# adb_FullDataTypeDeclaration class attributes and methods

# FullTypeDeclaration class attributes and methods

# adb_TypeDefinition class attributes and methods

# adb_IncompleteTypeDeclaration class attributes and methods
adb_IncompleteTypeDeclaration_tagged: Property = Property(name="tagged", type=BooleanType)
adb_IncompleteTypeDeclaration.attributes={adb_IncompleteTypeDeclaration_tagged}

# adb_DiscriminantPart class attributes and methods

# adb_PrivateTypeDeclaration class attributes and methods
adb_PrivateTypeDeclaration_abstract: Property = Property(name="abstract", type=BooleanType)
adb_PrivateTypeDeclaration_tagged: Property = Property(name="tagged", type=BooleanType)
adb_PrivateTypeDeclaration_limited: Property = Property(name="limited", type=BooleanType)
adb_PrivateTypeDeclaration.attributes={adb_PrivateTypeDeclaration_tagged, adb_PrivateTypeDeclaration_abstract, adb_PrivateTypeDeclaration_limited}

# adb_ProtectedTypeDeclaration class attributes and methods

# adb_ProtectedDefinition class attributes and methods

# adb_SubtypeIndication class attributes and methods
adb_SubtypeIndication_subtypeMark: Property = Property(name="subtypeMark", type=StringType)
adb_SubtypeIndication.attributes={adb_SubtypeIndication_subtypeMark}

# adb_TaskItem class attributes and methods

# adb_EntryDeclaration class attributes and methods
adb_EntryDeclaration_name: Property = Property(name="name", type=StringType)
adb_EntryDeclaration.attributes={adb_EntryDeclaration_name}

# TaskItem class attributes and methods

# ProtectedOperationDeclaration class attributes and methods

# adb_DiscreteSubtypeDefinition class attributes and methods

# adb_FormalPart class attributes and methods

# adb_ProcedureSpecification class attributes and methods

# SubprogramSpecification class attributes and methods

# adb_FunctionSpecification class attributes and methods

# adb_ParameterAndResultProfile class attributes and methods

# adb_ExceptionChoice class attributes and methods
adb_ExceptionChoice_others: Property = Property(name="others", type=BooleanType)
adb_ExceptionChoice.attributes={adb_ExceptionChoice_others}

# adb_Name class attributes and methods
adb_Name_name: Property = Property(name="name", type=StringType)
adb_Name.attributes={adb_Name_name}

# adb_ProtectedElementDeclaration class attributes and methods

# adb_ProtectedOperationDeclaration class attributes and methods

# ProtectedElementDeclaration class attributes and methods

# adb_SubprogramDeclaration class attributes and methods
adb_SubprogramDeclaration_abstract: Property = Property(name="abstract", type=BooleanType)
adb_SubprogramDeclaration_renamedName: Property = Property(name="renamedName", type=StringType)
adb_SubprogramDeclaration_null: Property = Property(name="null", type=BooleanType)
adb_SubprogramDeclaration.attributes={adb_SubprogramDeclaration_abstract, adb_SubprogramDeclaration_renamedName, adb_SubprogramDeclaration_null}

# BodyStub class attributes and methods

# adb_LabelisableStatement class attributes and methods

# adb_Statement class attributes and methods

# adb_SimpleStatement class attributes and methods

# Statement class attributes and methods

# adb_ExceptionHandler class attributes and methods
adb_ExceptionHandler_name: Property = Property(name="name", type=StringType)
adb_ExceptionHandler.attributes={adb_ExceptionHandler_name}

# adb_SequenceOfStatements class attributes and methods

# adb_Body class attributes and methods

# adb_ProperBody class attributes and methods

# Body class attributes and methods

# adb_Label class attributes and methods
adb_Label_identifier: Property = Property(name="identifier", type=StringType)
adb_Label.attributes={adb_Label_identifier}

# HandledSequenceOfStatements class attributes and methods

# AbortablePart class attributes and methods

# adb_Mode class attributes and methods
adb_Mode_in: Property = Property(name="in", type=BooleanType)
adb_Mode_out: Property = Property(name="out", type=BooleanType)
adb_Mode.attributes={adb_Mode_out, adb_Mode_in}

# adb_OptNullExclusion class attributes and methods
adb_OptNullExclusion_not_null: Property = Property(name="not_null", type=StringType)
adb_OptNullExclusion.attributes={adb_OptNullExclusion_not_null}

# adb_AnonymousAccessDefinition class attributes and methods

# adb_Expression class attributes and methods
adb_Expression_booleanOperator: Property = Property(name="booleanOperator", type=StringType)
adb_Expression.attributes={adb_Expression_booleanOperator}

# adb_CompoundStatement class attributes and methods

# adb_NullStatement class attributes and methods
adb_NullStatement_null: Property = Property(name="null", type=BooleanType)
adb_NullStatement.attributes={adb_NullStatement_null}

# SimpleStatement class attributes and methods

# adb_GenericItem class attributes and methods

# adb_GenericFormalParameterDeclaration class attributes and methods

# adb_FormalObjectDeclaration class attributes and methods

# GenericFormalParameterDeclaration class attributes and methods

# adb_DefiningIdentifierList class attributes and methods
adb_DefiningIdentifierList_name: Property = Property(name="name", type=StringType)
adb_DefiningIdentifierList.attributes={adb_DefiningIdentifierList_name}

# adb_FormalSubprogramDeclaration class attributes and methods
adb_FormalSubprogramDeclaration_abstract: Property = Property(name="abstract", type=StringType)
adb_FormalSubprogramDeclaration.attributes={adb_FormalSubprogramDeclaration_abstract}

# adb_SubprogramDefault class attributes and methods
adb_SubprogramDefault_defaultName: Property = Property(name="defaultName", type=StringType)
adb_SubprogramDefault.attributes={adb_SubprogramDefault_defaultName}

# adb_FormalTypeDeclaration class attributes and methods
adb_FormalTypeDeclaration_identifier: Property = Property(name="identifier", type=StringType)
adb_FormalTypeDeclaration.attributes={adb_FormalTypeDeclaration_identifier}

# adb_FormalTypeDefinition class attributes and methods

# adb_FormalPrivateTypeDefinition class attributes and methods
adb_FormalPrivateTypeDefinition_abstract: Property = Property(name="abstract", type=BooleanType)
adb_FormalPrivateTypeDefinition_tagged: Property = Property(name="tagged", type=BooleanType)
adb_FormalPrivateTypeDefinition_limited: Property = Property(name="limited", type=BooleanType)
adb_FormalPrivateTypeDefinition.attributes={adb_FormalPrivateTypeDefinition_abstract, adb_FormalPrivateTypeDefinition_limited, adb_FormalPrivateTypeDefinition_tagged}

# FormalTypeDefinition class attributes and methods

# adb_FormalDerivedTypeDefinition class attributes and methods
adb_FormalDerivedTypeDefinition_absract: Property = Property(name="absract", type=StringType)
adb_FormalDerivedTypeDefinition_limited: Property = Property(name="limited", type=BooleanType)
adb_FormalDerivedTypeDefinition_synchronized: Property = Property(name="synchronized", type=BooleanType)
adb_FormalDerivedTypeDefinition.attributes={adb_FormalDerivedTypeDefinition_limited, adb_FormalDerivedTypeDefinition_synchronized, adb_FormalDerivedTypeDefinition_absract}

# adb_FormalPackageAssociation class attributes and methods
adb_FormalPackageAssociation_genericFormalParameterSelectorName: Property = Property(name="genericFormalParameterSelectorName", type=StringType)
adb_FormalPackageAssociation.attributes={adb_FormalPackageAssociation_genericFormalParameterSelectorName}

# adb_GenericAssociation class attributes and methods
adb_GenericAssociation_selectorName: Property = Property(name="selectorName", type=StringType)
adb_GenericAssociation.attributes={adb_GenericAssociation_selectorName}

# adb_ExceptionDeclaration class attributes and methods

# adb_ObjectDeclaration class attributes and methods

# adb_DataInstanceDeclaration class attributes and methods
adb_DataInstanceDeclaration_aliased: Property = Property(name="aliased", type=BooleanType)
adb_DataInstanceDeclaration_constant: Property = Property(name="constant", type=BooleanType)
adb_DataInstanceDeclaration.attributes={adb_DataInstanceDeclaration_aliased, adb_DataInstanceDeclaration_constant}

# adb_FormalPackageDeclaration class attributes and methods
adb_FormalPackageDeclaration_name: Property = Property(name="name", type=StringType)
adb_FormalPackageDeclaration_genericPackageName: Property = Property(name="genericPackageName", type=StringType)
adb_FormalPackageDeclaration.attributes={adb_FormalPackageDeclaration_name, adb_FormalPackageDeclaration_genericPackageName}

# adb_FormalPackageActualPart class attributes and methods
adb_FormalPackageActualPart_box: Property = Property(name="box", type=BooleanType)
adb_FormalPackageActualPart.attributes={adb_FormalPackageActualPart_box}

# adb_ArrayTypeDefinition class attributes and methods

# adb_SingleProtectedDeclaration class attributes and methods
adb_SingleProtectedDeclaration_name: Property = Property(name="name", type=StringType)
adb_SingleProtectedDeclaration.attributes={adb_SingleProtectedDeclaration_name}

# ObjectDeclaration class attributes and methods

# adb_NumberDeclaration class attributes and methods

# adb_AssignmentStatement class attributes and methods

# adb_PragmaArgumentAssociation class attributes and methods
adb_PragmaArgumentAssociation_name: Property = Property(name="name", type=StringType)
adb_PragmaArgumentAssociation.attributes={adb_PragmaArgumentAssociation_name}

# adb_SubtypeDeclaration class attributes and methods

# adb_CaseStatement class attributes and methods

# adb_CaseStatementAlternative class attributes and methods

# adb_DiscreteChoiceList class attributes and methods

# adb_LoopStatement class attributes and methods
adb_LoopStatement_name: Property = Property(name="name", type=StringType)
adb_LoopStatement_sameName: Property = Property(name="sameName", type=StringType)
adb_LoopStatement.attributes={adb_LoopStatement_sameName, adb_LoopStatement_name}

# adb_IfStatement class attributes and methods

# CompoundStatement class attributes and methods

# adb_IterationScheme class attributes and methods

# adb_BlockStatement class attributes and methods
adb_BlockStatement_blockStatementIdentifier: Property = Property(name="blockStatementIdentifier", type=StringType)
adb_BlockStatement.attributes={adb_BlockStatement_blockStatementIdentifier}

# adb_ExitStatement class attributes and methods

# adb_GotoStatement class attributes and methods
adb_GotoStatement_labelId: Property = Property(name="labelId", type=StringType)
adb_GotoStatement.attributes={adb_GotoStatement_labelId}

# adb_LoopParameterSpecification class attributes and methods
adb_LoopParameterSpecification_identifier: Property = Property(name="identifier", type=StringType)
adb_LoopParameterSpecification.attributes={adb_LoopParameterSpecification_identifier}

# adb_ReturnSubtypeIndication class attributes and methods

# adb_PackageBody class attributes and methods

# adb_ProcedureOrEntryCallStatement class attributes and methods

# TriggeringStatement class attributes and methods

# adb_SimpleReturnStatement class attributes and methods

# adb_ExtendedReturnStatement class attributes and methods
adb_ExtendedReturnStatement_identifier: Property = Property(name="identifier", type=StringType)
adb_ExtendedReturnStatement.attributes={adb_ExtendedReturnStatement_identifier}

# adb_ProtectedOperationItem class attributes and methods

# adb_AcceptStatement class attributes and methods
adb_AcceptStatement_entryidentifier: Property = Property(name="entryidentifier", type=StringType)
adb_AcceptStatement.attributes={adb_AcceptStatement_entryidentifier}

# adb_EntryIndex class attributes and methods

# adb_TaskBody class attributes and methods

# adb_ProtectedBody class attributes and methods
adb_ProtectedBody_identifier: Property = Property(name="identifier", type=StringType)
adb_ProtectedBody_idTask: Property = Property(name="idTask", type=StringType)
adb_ProtectedBody.attributes={adb_ProtectedBody_idTask, adb_ProtectedBody_identifier}

# adb_EntryIndexSpecification class attributes and methods
adb_EntryIndexSpecification_name: Property = Property(name="name", type=StringType)
adb_EntryIndexSpecification.attributes={adb_EntryIndexSpecification_name}

# adb_EntryBody class attributes and methods
adb_EntryBody_endid: Property = Property(name="endid", type=StringType)
adb_EntryBody.attributes={adb_EntryBody_endid}

# adb_EntryBodyFormalPart class attributes and methods

# adb_SelectiveAccept class attributes and methods

# adb_EntryBarrier class attributes and methods

# SelectStatement class attributes and methods

# adb_Guard class attributes and methods

# adb_SelectAlternative class attributes and methods

# adb_GuardedAlternative class attributes and methods

# adb_RequeueStatement class attributes and methods
adb_RequeueStatement_abort: Property = Property(name="abort", type=BooleanType)
adb_RequeueStatement.attributes={adb_RequeueStatement_abort}

# adb_DelayStatement class attributes and methods
adb_DelayStatement_until: Property = Property(name="until", type=StringType)
adb_DelayStatement.attributes={adb_DelayStatement_until}

# adb_SelectStatement class attributes and methods

# adb_DelayAlternative class attributes and methods

# adb_TimedEntryCall class attributes and methods

# adb_EntryCallAlternative class attributes and methods

# adb_AcceptAlternative class attributes and methods

# SelectAlternative class attributes and methods

# adb_AsynchronousSelect class attributes and methods

# adb_TriggeringAlternative class attributes and methods

# adb_AbortablePart class attributes and methods

# adb_TriggeringStatement class attributes and methods

# adb_ConditionalEntryCall class attributes and methods

# adb_RaiseStatement class attributes and methods

# adb_AbortStatement class attributes and methods

# adb_TaskNames class attributes and methods

# AbortStatement class attributes and methods

# adb_BodyStub class attributes and methods
adb_BodyStub_name: Property = Property(name="name", type=StringType)
adb_BodyStub.attributes={adb_BodyStub_name}

# adb_PackageBodyStub class attributes and methods

# adb_TaskBodyStub class attributes and methods

# adb_ProtectedBodyStub class attributes and methods

# adb_SeparateSubunit class attributes and methods
adb_SeparateSubunit_parentUnitName: Property = Property(name="parentUnitName", type=StringType)
adb_SeparateSubunit.attributes={adb_SeparateSubunit_parentUnitName}

# adb_NotNullAccessDefinition class attributes and methods

# adb_ExplicitGenericActualParameter class attributes and methods

# adb_UnknownDiscriminantPart class attributes and methods
adb_UnknownDiscriminantPart_box: Property = Property(name="box", type=BooleanType)
adb_UnknownDiscriminantPart.attributes={adb_UnknownDiscriminantPart_box}

# DiscriminantPart class attributes and methods

# adb_DiscriminantSpecification class attributes and methods

# adb_RecordExtensionPart class attributes and methods

# adb_RecordDefinition class attributes and methods
adb_RecordDefinition_null: Property = Property(name="null", type=StringType)
adb_RecordDefinition.attributes={adb_RecordDefinition_null}

# adb_AccessTypeDefinition class attributes and methods

# adb_InterfaceTypeDefinition class attributes and methods
adb_InterfaceTypeDefinition_limited: Property = Property(name="limited", type=BooleanType)
adb_InterfaceTypeDefinition_task: Property = Property(name="task", type=BooleanType)
adb_InterfaceTypeDefinition_protected: Property = Property(name="protected", type=BooleanType)
adb_InterfaceTypeDefinition_synchro: Property = Property(name="synchro", type=BooleanType)
adb_InterfaceTypeDefinition.attributes={adb_InterfaceTypeDefinition_task, adb_InterfaceTypeDefinition_protected, adb_InterfaceTypeDefinition_synchro, adb_InterfaceTypeDefinition_limited}

# adb_AccessSpecification class attributes and methods

# TypeDefinition class attributes and methods

# adb_AccessToSubprogramDefinition class attributes and methods
adb_AccessToSubprogramDefinition_protected: Property = Property(name="protected", type=BooleanType)
adb_AccessToSubprogramDefinition.attributes={adb_AccessToSubprogramDefinition_protected}

# AccessSpecification class attributes and methods

# NotNullAccessDefinition class attributes and methods

# adb_DerivedTypeDefinition class attributes and methods
adb_DerivedTypeDefinition_abstract: Property = Property(name="abstract", type=StringType)
adb_DerivedTypeDefinition_limited: Property = Property(name="limited", type=StringType)
adb_DerivedTypeDefinition.attributes={adb_DerivedTypeDefinition_limited, adb_DerivedTypeDefinition_abstract}

# adb_AccessToDataDefinition class attributes and methods
adb_AccessToDataDefinition_generalAccessModifier: Property = Property(name="generalAccessModifier", type=StringType)
adb_AccessToDataDefinition.attributes={adb_AccessToDataDefinition_generalAccessModifier}

# ReturnSubtypeIndication class attributes and methods

# adb_ArrayIndexes class attributes and methods

# adb_ComponentDefinition class attributes and methods
adb_ComponentDefinition_aliased: Property = Property(name="aliased", type=BooleanType)
adb_ComponentDefinition.attributes={adb_ComponentDefinition_aliased}

# adb_UnconstrainedIndexes class attributes and methods

# ArrayIndexes class attributes and methods

# adb_ConstrainedIndexes class attributes and methods

# adb_AccessToDataInstance class attributes and methods
adb_AccessToDataInstance_constant: Property = Property(name="constant", type=StringType)
adb_AccessToDataInstance.attributes={adb_AccessToDataInstance_constant}

# adb_ParameterSpecification class attributes and methods

# adb_ModularTypeDefinition class attributes and methods

# adb_IntegerTypeDefinition class attributes and methods

# adb_SignedIntegerTypeDefinition class attributes and methods

# IntegerTypeDefinition class attributes and methods

# adb_SimpleExpression class attributes and methods
adb_SimpleExpression_unaryAddingOperator: Property = Property(name="unaryAddingOperator", type=StringType)
adb_SimpleExpression_binaryAddingOperators: Property = Property(name="binaryAddingOperators", type=StringType)
adb_SimpleExpression.attributes={adb_SimpleExpression_binaryAddingOperators, adb_SimpleExpression_unaryAddingOperator}

# adb_OptVariantPart class attributes and methods

# adb_VariantPart class attributes and methods
adb_VariantPart_name: Property = Property(name="name", type=StringType)
adb_VariantPart.attributes={adb_VariantPart_name}

# adb_EnumerationTypeDefinition class attributes and methods
adb_EnumerationTypeDefinition_enumerationliteralspecifications: Property = Property(name="enumerationliteralspecifications", type=StringType)
adb_EnumerationTypeDefinition.attributes={adb_EnumerationTypeDefinition_enumerationliteralspecifications}

# adb_RecordTypeDefinition class attributes and methods
adb_RecordTypeDefinition_abstract: Property = Property(name="abstract", type=BooleanType)
adb_RecordTypeDefinition_tagged: Property = Property(name="tagged", type=BooleanType)
adb_RecordTypeDefinition_limited: Property = Property(name="limited", type=BooleanType)
adb_RecordTypeDefinition.attributes={adb_RecordTypeDefinition_abstract, adb_RecordTypeDefinition_tagged, adb_RecordTypeDefinition_limited}

# adb_ComponentList class attributes and methods

# adb_ComponentItem class attributes and methods

# adb_ComponentClause class attributes and methods
adb_ComponentClause_localName: Property = Property(name="localName", type=StringType)
adb_ComponentClause.attributes={adb_ComponentClause_localName}

# adb_ComponentDeclaration class attributes and methods

# ComponentItem class attributes and methods

# adb_AspectClause class attributes and methods
adb_AspectClause_name: Property = Property(name="name", type=StringType)
adb_AspectClause.attributes={adb_AspectClause_name}

# adb_ModClause class attributes and methods

# adb_Variant class attributes and methods

# ExplicitGenericActualParameter class attributes and methods

# DiscreteChoice class attributes and methods

# adb_DiscreteChoice class attributes and methods

# adb_RealTypeDefinition class attributes and methods

# adb_RealRangeSpecification class attributes and methods

# adb_FloatingPointDefinition class attributes and methods

# RealTypeDefinition class attributes and methods

# adb_FixedPointDefinition class attributes and methods

# EntryIndex class attributes and methods

# adb_Term class attributes and methods
adb_Term_multiplyingOperators: Property = Property(name="multiplyingOperators", type=StringType)
adb_Term.attributes={adb_Term_multiplyingOperators}

# AncestorPart class attributes and methods

# ParameterEffectiveValue class attributes and methods

# adb_Relation class attributes and methods
adb_Relation_relationalOperator: Property = Property(name="relationalOperator", type=StringType)
adb_Relation.attributes={adb_Relation_relationalOperator}

# adb_Membership class attributes and methods
adb_Membership_not: Property = Property(name="not", type=BooleanType)
adb_Membership.attributes={adb_Membership_not}

# adb_Interval class attributes and methods

# adb_Factor class attributes and methods
adb_Factor_abs: Property = Property(name="abs", type=BooleanType)
adb_Factor_not: Property = Property(name="not", type=BooleanType)
adb_Factor.attributes={adb_Factor_not, adb_Factor_abs}

# adb_Primary class attributes and methods

# adb_NumericLiteral class attributes and methods
adb_NumericLiteral_value: Property = Property(name="value", type=StringType)
adb_NumericLiteral.attributes={adb_NumericLiteral_value}

# Primary class attributes and methods

# adb_Null class attributes and methods
adb_Null_value: Property = Property(name="value", type=StringType)
adb_Null.attributes={adb_Null_value}

# adb_StringLiteral class attributes and methods
adb_StringLiteral_value: Property = Property(name="value", type=StringType)
adb_StringLiteral.attributes={adb_StringLiteral_value}

# adb_EObject class attributes and methods

# adb_QualifiedName class attributes and methods

# adb_Qualifier class attributes and methods

# adb_ParenthesizedExpression class attributes and methods

# adb_Allocator class attributes and methods

# DiscreteSubtypeDefinition class attributes and methods

# DiscreteRange class attributes and methods

# adb_OptConstraint class attributes and methods

# adb_IndexConstraint class attributes and methods

# adb_DiscreteRange class attributes and methods

# adb_ScalarConstraint class attributes and methods

# adb_DigitsConstraint class attributes and methods

# ScalarConstraint class attributes and methods

# adb_RangeConstraint class attributes and methods

# adb_DeltaConstraint class attributes and methods

# adb_CompositeConstraint class attributes and methods

# adb_DiscriminantConstraint class attributes and methods

# CompositeConstraint class attributes and methods

# adb_DiscriminantAssociation class attributes and methods

# adb_RecordAggregate class attributes and methods

# Aggregate class attributes and methods

# adb_RecordComponentAssociationList class attributes and methods
adb_RecordComponentAssociationList_nullRecord: Property = Property(name="nullRecord", type=BooleanType)
adb_RecordComponentAssociationList.attributes={adb_RecordComponentAssociationList_nullRecord}

# RecordAggregate class attributes and methods

# adb_DiscriminantSelectors class attributes and methods
adb_DiscriminantSelectors_discriminantSelectorName: Property = Property(name="discriminantSelectorName", type=StringType)
adb_DiscriminantSelectors.attributes={adb_DiscriminantSelectors_discriminantSelectorName}

# adb_ComponentChoiceList class attributes and methods
adb_ComponentChoiceList_componentSelectorName: Property = Property(name="componentSelectorName", type=StringType)
adb_ComponentChoiceList_others: Property = Property(name="others", type=BooleanType)
adb_ComponentChoiceList.attributes={adb_ComponentChoiceList_others, adb_ComponentChoiceList_componentSelectorName}

# adb_Aggregate class attributes and methods

# ParenthesizedExpression class attributes and methods

# Qualifier class attributes and methods

# adb_ArrayAggregate class attributes and methods

# adb_PositionalArrayAggregate class attributes and methods
adb_PositionalArrayAggregate_othersBox: Property = Property(name="othersBox", type=BooleanType)
adb_PositionalArrayAggregate.attributes={adb_PositionalArrayAggregate_othersBox}

# ArrayAggregate class attributes and methods

# adb_RecordComponentAssociation class attributes and methods

# adb_InitializedComponents class attributes and methods

# RecordComponentAssociation class attributes and methods

# adb_UninitializedComponents class attributes and methods
adb_UninitializedComponents_box: Property = Property(name="box", type=BooleanType)
adb_UninitializedComponents.attributes={adb_UninitializedComponents_box}

# adb_ExtensionAggregate class attributes and methods

# adb_AncestorPart class attributes and methods

# adb_PrimaryName class attributes and methods

# adb_ParameterAssociation class attributes and methods
adb_ParameterAssociation_selectorName: Property = Property(name="selectorName", type=StringType)
adb_ParameterAssociation.attributes={adb_ParameterAssociation_selectorName}

# adb_NamedArrayAggregate class attributes and methods

# adb_ArrayComponentAssociation class attributes and methods
adb_ArrayComponentAssociation_box: Property = Property(name="box", type=BooleanType)
adb_ArrayComponentAssociation.attributes={adb_ArrayComponentAssociation_box}

# Interval class attributes and methods

# adb_EntityRange class attributes and methods

# Range class attributes and methods

# adb_AttributeDesignator class attributes and methods

# adb_ParameterEffectiveValue class attributes and methods

# adb_Range class attributes and methods

# RangeConstraint class attributes and methods

# adb_ExplicitRange class attributes and methods

# Relationships
importURI9: BinaryAssociation = BinaryAssociation(
    name="importURI9",
    ends={
        Property(name="adb_LibraryUnitDeclaration", type=adb_WithClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_WithClause", type=adb_LibraryUnitDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
compilationUnits0: BinaryAssociation = BinaryAssociation(
    name="compilationUnits0",
    ends={
        Property(name="adb_CompilationUnit", type=adb_Compilation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Compilation", type=adb_CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importedNamespace10: BinaryAssociation = BinaryAssociation(
    name="importedNamespace10",
    ends={
        Property(name="adb_LibraryUnitDeclaration11", type=adb_UsePackageClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_UsePackageClause", type=adb_LibraryUnitDeclaration, multiplicity=Multiplicity(0, 9999))
    }
)
contextClause1: BinaryAssociation = BinaryAssociation(
    name="contextClause1",
    ends={
        Property(name="adb_ContextClause", type=adb_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CompilationUnit2", type=adb_ContextClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unit3: BinaryAssociation = BinaryAssociation(
    name="unit3",
    ends={
        Property(name="adb_Unit", type=adb_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CompilationUnit4", type=adb_Unit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pragmas5: BinaryAssociation = BinaryAssociation(
    name="pragmas5",
    ends={
        Property(name="adb_Pragma", type=adb_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CompilationUnit6", type=adb_Pragma, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contextItems7: BinaryAssociation = BinaryAssociation(
    name="contextItems7",
    ends={
        Property(name="adb_ContextItem", type=adb_ContextClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ContextClause8", type=adb_ContextItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packageSpecification14: BinaryAssociation = BinaryAssociation(
    name="packageSpecification14",
    ends={
        Property(name="adb_PackageSpecification", type=adb_PackageDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PackageDefinition", type=adb_PackageSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericItems15: BinaryAssociation = BinaryAssociation(
    name="genericItems15",
    ends={
        Property(name="adb_GenericItems", type=adb_GenericDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericDeclaration", type=adb_GenericItems, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
libraryUnitSpecification12: BinaryAssociation = BinaryAssociation(
    name="libraryUnitSpecification12",
    ends={
        Property(name="adb_LibraryUnitSpecification", type=adb_LibraryUnitDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LibraryUnitDeclaration13", type=adb_LibraryUnitSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publicBasicDeclarativeItems21: BinaryAssociation = BinaryAssociation(
    name="publicBasicDeclarativeItems21",
    ends={
        Property(name="adb_BasicDeclarativeItem", type=adb_PackageSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PackageSpecification22", type=adb_BasicDeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
privateBasicDeclarativeItems23: BinaryAssociation = BinaryAssociation(
    name="privateBasicDeclarativeItems23",
    ends={
        Property(name="adb_BasicDeclarativeItem25", type=adb_PackageSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PackageSpecification24", type=adb_BasicDeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subprogramSpecification26: BinaryAssociation = BinaryAssociation(
    name="subprogramSpecification26",
    ends={
        Property(name="adb_SubprogramSpecification", type=adb_SubprogramBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubprogramBody", type=adb_SubprogramSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
librarySpecification16: BinaryAssociation = BinaryAssociation(
    name="librarySpecification16",
    ends={
        Property(name="adb_LibrarySpecification", type=adb_GenericDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericDeclaration17", type=adb_LibrarySpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overriding18: BinaryAssociation = BinaryAssociation(
    name="overriding18",
    ends={
        Property(name="adb_OverridingIndicator", type=adb_GenericInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericInstantiation", type=adb_OverridingIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericActualPart19: BinaryAssociation = BinaryAssociation(
    name="genericActualPart19",
    ends={
        Property(name="adb_GenericActualPart", type=adb_GenericInstantiation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericInstantiation20", type=adb_GenericActualPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList31: BinaryAssociation = BinaryAssociation(
    name="interfaceList31",
    ends={
        Property(name="adb_InterfaceList", type=adb_TaskDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskDeclaration32", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
taskDefinition33: BinaryAssociation = BinaryAssociation(
    name="taskDefinition33",
    ends={
        Property(name="adb_TaskDefinition", type=adb_TaskDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskDeclaration34", type=adb_TaskDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endid36: BinaryAssociation = BinaryAssociation(
    name="endid36",
    ends={
        Property(name="adb_TaskDeclaration37", type=adb_TaskDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskDeclaration35", type=adb_TaskDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
declarativeItems27: BinaryAssociation = BinaryAssociation(
    name="declarativeItems27",
    ends={
        Property(name="adb_DeclarativeItem", type=adb_DeclarativeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DeclarativeBlock", type=adb_DeclarativeItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handledSequenceOfStatements28: BinaryAssociation = BinaryAssociation(
    name="handledSequenceOfStatements28",
    ends={
        Property(name="adb_HandledSequenceOfStatements", type=adb_DeclarativeBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DeclarativeBlock29", type=adb_HandledSequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
knownDiscriminantPart30: BinaryAssociation = BinaryAssociation(
    name="knownDiscriminantPart30",
    ends={
        Property(name="adb_KnownDiscriminantPart", type=adb_TaskDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskDeclaration", type=adb_KnownDiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantPart42: BinaryAssociation = BinaryAssociation(
    name="discriminantPart42",
    ends={
        Property(name="adb_DiscriminantPart43", type=adb_PrivateTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrivateTypeDeclaration", type=adb_DiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantPart44: BinaryAssociation = BinaryAssociation(
    name="discriminantPart44",
    ends={
        Property(name="adb_DiscriminantPart45", type=adb_PrivateExtensionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrivateExtensionDeclaration", type=adb_DiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
knownDiscriminantPart38: BinaryAssociation = BinaryAssociation(
    name="knownDiscriminantPart38",
    ends={
        Property(name="adb_KnownDiscriminantPart39", type=adb_FullTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FullTypeDeclaration", type=adb_KnownDiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDefinition40: BinaryAssociation = BinaryAssociation(
    name="typeDefinition40",
    ends={
        Property(name="adb_TypeDefinition", type=adb_FullDataTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FullDataTypeDeclaration", type=adb_TypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantPart41: BinaryAssociation = BinaryAssociation(
    name="discriminantPart41",
    ends={
        Property(name="adb_DiscriminantPart", type=adb_IncompleteTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IncompleteTypeDeclaration", type=adb_DiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart55: BinaryAssociation = BinaryAssociation(
    name="formalPart55",
    ends={
        Property(name="adb_EntryDeclaration56", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="adb_FormalPart", type=adb_EntryDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
interfaceList57: BinaryAssociation = BinaryAssociation(
    name="interfaceList57",
    ends={
        Property(name="adb_InterfaceList58", type=adb_ProtectedTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProtectedTypeDeclaration", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protectedDefinition59: BinaryAssociation = BinaryAssociation(
    name="protectedDefinition59",
    ends={
        Property(name="adb_ProtectedDefinition", type=adb_ProtectedTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProtectedTypeDeclaration60", type=adb_ProtectedDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ancestorSubtypeIndication46: BinaryAssociation = BinaryAssociation(
    name="ancestorSubtypeIndication46",
    ends={
        Property(name="adb_SubtypeIndication", type=adb_PrivateExtensionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrivateExtensionDeclaration47", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList48: BinaryAssociation = BinaryAssociation(
    name="interfaceList48",
    ends={
        Property(name="adb_InterfaceList50", type=adb_PrivateExtensionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrivateExtensionDeclaration49", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overriding51: BinaryAssociation = BinaryAssociation(
    name="overriding51",
    ends={
        Property(name="adb_OverridingIndicator52", type=adb_EntryDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryDeclaration", type=adb_OverridingIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discreteSubtypeDefinition53: BinaryAssociation = BinaryAssociation(
    name="discreteSubtypeDefinition53",
    ends={
        Property(name="adb_DiscreteSubtypeDefinition", type=adb_EntryDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryDeclaration54", type=adb_DiscreteSubtypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart68: BinaryAssociation = BinaryAssociation(
    name="formalPart68",
    ends={
        Property(name="adb_FormalPart69", type=adb_ProcedureSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProcedureSpecification", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterAndResultProfile70: BinaryAssociation = BinaryAssociation(
    name="parameterAndResultProfile70",
    ends={
        Property(name="adb_ParameterAndResultProfile", type=adb_FunctionSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FunctionSpecification", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name71: BinaryAssociation = BinaryAssociation(
    name="name71",
    ends={
        Property(name="adb_Name", type=adb_ExceptionChoice, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExceptionChoice", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protectedOperationDeclaration61: BinaryAssociation = BinaryAssociation(
    name="protectedOperationDeclaration61",
    ends={
        Property(name="adb_ProtectedElementDeclaration", type=adb_ProtectedDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProtectedDefinition62", type=adb_ProtectedElementDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subprogramSpecification63: BinaryAssociation = BinaryAssociation(
    name="subprogramSpecification63",
    ends={
        Property(name="adb_SubprogramSpecification64", type=adb_SubprogramDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubprogramDeclaration", type=adb_SubprogramSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridingIndicator65: BinaryAssociation = BinaryAssociation(
    name="overridingIndicator65",
    ends={
        Property(name="adb_OverridingIndicator67", type=adb_SubprogramSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubprogramSpecification66", type=adb_OverridingIndicator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionHandler76: BinaryAssociation = BinaryAssociation(
    name="exceptionHandler76",
    ends={
        Property(name="adb_ExceptionHandler78", type=adb_SequenceOfStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SequenceOfStatements77", type=adb_ExceptionHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements79: BinaryAssociation = BinaryAssociation(
    name="statements79",
    ends={
        Property(name="adb_LabelisableStatement", type=adb_SequenceOfStatements, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SequenceOfStatements80", type=adb_LabelisableStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels81: BinaryAssociation = BinaryAssociation(
    name="labels81",
    ends={
        Property(name="adb_Label", type=adb_LabelisableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LabelisableStatement82", type=adb_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement83: BinaryAssociation = BinaryAssociation(
    name="statement83",
    ends={
        Property(name="adb_Statement", type=adb_LabelisableStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LabelisableStatement84", type=adb_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionChoice72: BinaryAssociation = BinaryAssociation(
    name="exceptionChoice72",
    ends={
        Property(name="adb_ExceptionChoice73", type=adb_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExceptionHandler", type=adb_ExceptionChoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceOfStatements74: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements74",
    ends={
        Property(name="adb_SequenceOfStatements", type=adb_ExceptionHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExceptionHandler75", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mode88: BinaryAssociation = BinaryAssociation(
    name="mode88",
    ends={
        Property(name="adb_Mode", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration89", type=adb_Mode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optNullExclusion90: BinaryAssociation = BinaryAssociation(
    name="optNullExclusion90",
    ends={
        Property(name="adb_OptNullExclusion", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration91", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark92: BinaryAssociation = BinaryAssociation(
    name="subtypeMark92",
    ends={
        Property(name="adb_Name94", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration93", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousAccessDefinition95: BinaryAssociation = BinaryAssociation(
    name="anonymousAccessDefinition95",
    ends={
        Property(name="adb_AnonymousAccessDefinition", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration96", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpression97: BinaryAssociation = BinaryAssociation(
    name="defaultExpression97",
    ends={
        Property(name="adb_Expression", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration98", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericItems85: BinaryAssociation = BinaryAssociation(
    name="genericItems85",
    ends={
        Property(name="adb_GenericItem", type=adb_GenericItems, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericItems86", type=adb_GenericItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idList87: BinaryAssociation = BinaryAssociation(
    name="idList87",
    ends={
        Property(name="adb_DefiningIdentifierList", type=adb_FormalObjectDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalObjectDeclaration", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark103: BinaryAssociation = BinaryAssociation(
    name="subtypeMark103",
    ends={
        Property(name="adb_Name104", type=adb_FormalDerivedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalDerivedTypeDefinition", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList105: BinaryAssociation = BinaryAssociation(
    name="interfaceList105",
    ends={
        Property(name="adb_InterfaceList107", type=adb_FormalDerivedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalDerivedTypeDefinition106", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subprogramSpecification108: BinaryAssociation = BinaryAssociation(
    name="subprogramSpecification108",
    ends={
        Property(name="adb_SubprogramSpecification109", type=adb_FormalSubprogramDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalSubprogramDeclaration", type=adb_SubprogramSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subprogramDefault110: BinaryAssociation = BinaryAssociation(
    name="subprogramDefault110",
    ends={
        Property(name="adb_SubprogramDefault", type=adb_FormalSubprogramDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalSubprogramDeclaration111", type=adb_SubprogramDefault, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantPart99: BinaryAssociation = BinaryAssociation(
    name="discriminantPart99",
    ends={
        Property(name="adb_DiscriminantPart100", type=adb_FormalTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalTypeDeclaration", type=adb_DiscriminantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalTypeDefinition101: BinaryAssociation = BinaryAssociation(
    name="formalTypeDefinition101",
    ends={
        Property(name="adb_FormalTypeDefinition", type=adb_FormalTypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalTypeDeclaration102", type=adb_FormalTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPackageAssociation116: BinaryAssociation = BinaryAssociation(
    name="formalPackageAssociation116",
    ends={
        Property(name="adb_FormalPackageAssociation", type=adb_FormalPackageActualPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalPackageActualPart117", type=adb_FormalPackageAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
genericAssociation118: BinaryAssociation = BinaryAssociation(
    name="genericAssociation118",
    ends={
        Property(name="adb_GenericAssociation", type=adb_FormalPackageAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalPackageAssociation119", type=adb_GenericAssociation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList120: BinaryAssociation = BinaryAssociation(
    name="idList120",
    ends={
        Property(name="adb_DefiningIdentifierList121", type=adb_ExceptionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExceptionDeclaration", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
renamedName122: BinaryAssociation = BinaryAssociation(
    name="renamedName122",
    ends={
        Property(name="adb_Name124", type=adb_ExceptionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExceptionDeclaration123", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPackageActualPart112: BinaryAssociation = BinaryAssociation(
    name="formalPackageActualPart112",
    ends={
        Property(name="adb_FormalPackageActualPart", type=adb_FormalPackageDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalPackageDeclaration", type=adb_FormalPackageActualPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericActualPart113: BinaryAssociation = BinaryAssociation(
    name="genericActualPart113",
    ends={
        Property(name="adb_GenericActualPart115", type=adb_FormalPackageActualPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FormalPackageActualPart114", type=adb_GenericActualPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousAccessDefinition136: BinaryAssociation = BinaryAssociation(
    name="anonymousAccessDefinition136",
    ends={
        Property(name="adb_AnonymousAccessDefinition138", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration137", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayTypeDefinition139: BinaryAssociation = BinaryAssociation(
    name="arrayTypeDefinition139",
    ends={
        Property(name="adb_ArrayTypeDefinition", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration140", type=adb_ArrayTypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList141: BinaryAssociation = BinaryAssociation(
    name="interfaceList141",
    ends={
        Property(name="adb_InterfaceList142", type=adb_SingleProtectedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SingleProtectedDeclaration", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protectedDefinition143: BinaryAssociation = BinaryAssociation(
    name="protectedDefinition143",
    ends={
        Property(name="adb_ProtectedDefinition145", type=adb_SingleProtectedDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SingleProtectedDeclaration144", type=adb_ProtectedDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingIdentifierList125: BinaryAssociation = BinaryAssociation(
    name="definingIdentifierList125",
    ends={
        Property(name="adb_DefiningIdentifierList126", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeIndication127: BinaryAssociation = BinaryAssociation(
    name="subtypeIndication127",
    ends={
        Property(name="adb_SubtypeIndication129", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration128", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression130: BinaryAssociation = BinaryAssociation(
    name="expression130",
    ends={
        Property(name="adb_Expression132", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration131", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objectName133: BinaryAssociation = BinaryAssociation(
    name="objectName133",
    ends={
        Property(name="adb_Name135", type=adb_DataInstanceDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DataInstanceDeclaration134", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
idList153: BinaryAssociation = BinaryAssociation(
    name="idList153",
    ends={
        Property(name="adb_DefiningIdentifierList154", type=adb_NumberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_NumberDeclaration", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticExpression155: BinaryAssociation = BinaryAssociation(
    name="staticExpression155",
    ends={
        Property(name="adb_Expression157", type=adb_NumberDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_NumberDeclaration156", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableName158: BinaryAssociation = BinaryAssociation(
    name="variableName158",
    ends={
        Property(name="adb_Name159", type=adb_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AssignmentStatement", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue160: BinaryAssociation = BinaryAssociation(
    name="initialValue160",
    ends={
        Property(name="adb_Expression162", type=adb_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AssignmentStatement161", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pragmaArgumentAssociation146: BinaryAssociation = BinaryAssociation(
    name="pragmaArgumentAssociation146",
    ends={
        Property(name="adb_PragmaArgumentAssociation", type=adb_Pragma, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Pragma147", type=adb_PragmaArgumentAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
effectiveArgument148: BinaryAssociation = BinaryAssociation(
    name="effectiveArgument148",
    ends={
        Property(name="adb_Expression150", type=adb_PragmaArgumentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PragmaArgumentAssociation149", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeIndication151: BinaryAssociation = BinaryAssociation(
    name="subtypeIndication151",
    ends={
        Property(name="adb_SubtypeIndication152", type=adb_SubtypeDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubtypeDeclaration", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseValue177: BinaryAssociation = BinaryAssociation(
    name="caseValue177",
    ends={
        Property(name="adb_Expression178", type=adb_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CaseStatement", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseStatementAlternatives179: BinaryAssociation = BinaryAssociation(
    name="caseStatementAlternatives179",
    ends={
        Property(name="adb_CaseStatementAlternative", type=adb_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CaseStatement180", type=adb_CaseStatementAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discreteChoiceList181: BinaryAssociation = BinaryAssociation(
    name="discreteChoiceList181",
    ends={
        Property(name="adb_DiscreteChoiceList", type=adb_CaseStatementAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CaseStatementAlternative182", type=adb_DiscreteChoiceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOfStatements183: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements183",
    ends={
        Property(name="adb_SequenceOfStatements185", type=adb_CaseStatementAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_CaseStatementAlternative184", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifCondition163: BinaryAssociation = BinaryAssociation(
    name="ifCondition163",
    ends={
        Property(name="adb_Expression164", type=adb_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IfStatement", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenStatements165: BinaryAssociation = BinaryAssociation(
    name="thenStatements165",
    ends={
        Property(name="adb_SequenceOfStatements167", type=adb_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IfStatement166", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsifConditions168: BinaryAssociation = BinaryAssociation(
    name="elsifConditions168",
    ends={
        Property(name="adb_Expression170", type=adb_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IfStatement169", type=adb_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsifStatements171: BinaryAssociation = BinaryAssociation(
    name="elsifStatements171",
    ends={
        Property(name="adb_SequenceOfStatements173", type=adb_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IfStatement172", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements174: BinaryAssociation = BinaryAssociation(
    name="elseStatements174",
    ends={
        Property(name="adb_SequenceOfStatements176", type=adb_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IfStatement175", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discreteSubtypeDefinition195: BinaryAssociation = BinaryAssociation(
    name="discreteSubtypeDefinition195",
    ends={
        Property(name="adb_DiscreteSubtypeDefinition197", type=adb_LoopParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LoopParameterSpecification196", type=adb_DiscreteSubtypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name198: BinaryAssociation = BinaryAssociation(
    name="name198",
    ends={
        Property(name="adb_LoopStatement199", type=adb_ExitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExitStatement", type=adb_LoopStatement, multiplicity=Multiplicity(0, 1))
    }
)
condition200: BinaryAssociation = BinaryAssociation(
    name="condition200",
    ends={
        Property(name="adb_Expression202", type=adb_ExitStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExitStatement201", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationScheme186: BinaryAssociation = BinaryAssociation(
    name="iterationScheme186",
    ends={
        Property(name="adb_IterationScheme", type=adb_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LoopStatement", type=adb_IterationScheme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOfStatements187: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements187",
    ends={
        Property(name="adb_SequenceOfStatements189", type=adb_LoopStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_LoopStatement188", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition190: BinaryAssociation = BinaryAssociation(
    name="condition190",
    ends={
        Property(name="adb_Expression192", type=adb_IterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IterationScheme191", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
iterationSpecification193: BinaryAssociation = BinaryAssociation(
    name="iterationSpecification193",
    ends={
        Property(name="adb_LoopParameterSpecification", type=adb_IterationScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IterationScheme194", type=adb_LoopParameterSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnSubtype207: BinaryAssociation = BinaryAssociation(
    name="returnSubtype207",
    ends={
        Property(name="adb_ReturnSubtypeIndication", type=adb_ExtendedReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExtendedReturnStatement", type=adb_ReturnSubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression208: BinaryAssociation = BinaryAssociation(
    name="expression208",
    ends={
        Property(name="adb_Expression210", type=adb_ExtendedReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExtendedReturnStatement209", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
handledSequenceOfStatements211: BinaryAssociation = BinaryAssociation(
    name="handledSequenceOfStatements211",
    ends={
        Property(name="adb_HandledSequenceOfStatements213", type=adb_ExtendedReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExtendedReturnStatement212", type=adb_HandledSequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name214: BinaryAssociation = BinaryAssociation(
    name="name214",
    ends={
        Property(name="adb_PackageDeclaration", type=adb_PackageBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PackageBody", type=adb_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
endName215: BinaryAssociation = BinaryAssociation(
    name="endName215",
    ends={
        Property(name="adb_PackageDeclaration217", type=adb_PackageBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PackageBody216", type=adb_PackageDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
callee203: BinaryAssociation = BinaryAssociation(
    name="callee203",
    ends={
        Property(name="adb_Name204", type=adb_ProcedureOrEntryCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProcedureOrEntryCallStatement", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnValue205: BinaryAssociation = BinaryAssociation(
    name="returnValue205",
    ends={
        Property(name="adb_Expression206", type=adb_SimpleReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SimpleReturnStatement", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
protectedOperationItem225: BinaryAssociation = BinaryAssociation(
    name="protectedOperationItem225",
    ends={
        Property(name="adb_ProtectedOperationItem", type=adb_ProtectedBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ProtectedBody", type=adb_ProtectedOperationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryName226: BinaryAssociation = BinaryAssociation(
    name="entryName226",
    ends={
        Property(name="adb_EntryDeclaration227", type=adb_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AcceptStatement", type=adb_EntryDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
entryIndex228: BinaryAssociation = BinaryAssociation(
    name="entryIndex228",
    ends={
        Property(name="adb_EntryIndex", type=adb_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AcceptStatement229", type=adb_EntryIndex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart230: BinaryAssociation = BinaryAssociation(
    name="formalPart230",
    ends={
        Property(name="adb_FormalPart232", type=adb_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AcceptStatement231", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
handledSequenceOfStatements233: BinaryAssociation = BinaryAssociation(
    name="handledSequenceOfStatements233",
    ends={
        Property(name="adb_HandledSequenceOfStatements235", type=adb_AcceptStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AcceptStatement234", type=adb_HandledSequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
taskItems218: BinaryAssociation = BinaryAssociation(
    name="taskItems218",
    ends={
        Property(name="adb_TaskItem", type=adb_TaskDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskDefinition219", type=adb_TaskItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name220: BinaryAssociation = BinaryAssociation(
    name="name220",
    ends={
        Property(name="adb_TaskDeclaration221", type=adb_TaskBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskBody", type=adb_TaskDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
endId222: BinaryAssociation = BinaryAssociation(
    name="endId222",
    ends={
        Property(name="adb_TaskDeclaration224", type=adb_TaskBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskBody223", type=adb_TaskDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
entryIndexSpecification242: BinaryAssociation = BinaryAssociation(
    name="entryIndexSpecification242",
    ends={
        Property(name="adb_EntryIndexSpecification", type=adb_EntryBodyFormalPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBodyFormalPart243", type=adb_EntryIndexSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart244: BinaryAssociation = BinaryAssociation(
    name="formalPart244",
    ends={
        Property(name="adb_FormalPart246", type=adb_EntryBodyFormalPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBodyFormalPart245", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition247: BinaryAssociation = BinaryAssociation(
    name="condition247",
    ends={
        Property(name="adb_Expression249", type=adb_EntryBarrier, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBarrier248", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name236: BinaryAssociation = BinaryAssociation(
    name="name236",
    ends={
        Property(name="adb_EntryDeclaration237", type=adb_EntryBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBody", type=adb_EntryDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
entryBodyFormalPart238: BinaryAssociation = BinaryAssociation(
    name="entryBodyFormalPart238",
    ends={
        Property(name="adb_EntryBodyFormalPart", type=adb_EntryBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBody239", type=adb_EntryBodyFormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryBarrier240: BinaryAssociation = BinaryAssociation(
    name="entryBarrier240",
    ends={
        Property(name="adb_EntryBarrier", type=adb_EntryBody, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryBody241", type=adb_EntryBarrier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectguard257: BinaryAssociation = BinaryAssociation(
    name="selectguard257",
    ends={
        Property(name="adb_Guard", type=adb_SelectiveAccept, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SelectiveAccept", type=adb_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectAlternative258: BinaryAssociation = BinaryAssociation(
    name="selectAlternative258",
    ends={
        Property(name="adb_SelectAlternative", type=adb_SelectiveAccept, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SelectiveAccept259", type=adb_SelectAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guardedAlternatives260: BinaryAssociation = BinaryAssociation(
    name="guardedAlternatives260",
    ends={
        Property(name="adb_GuardedAlternative", type=adb_SelectiveAccept, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SelectiveAccept261", type=adb_GuardedAlternative, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements262: BinaryAssociation = BinaryAssociation(
    name="elseStatements262",
    ends={
        Property(name="adb_SequenceOfStatements264", type=adb_SelectiveAccept, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SelectiveAccept263", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discreteSubtypeDefinition250: BinaryAssociation = BinaryAssociation(
    name="discreteSubtypeDefinition250",
    ends={
        Property(name="adb_DiscreteSubtypeDefinition252", type=adb_EntryIndexSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryIndexSpecification251", type=adb_DiscreteSubtypeDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name253: BinaryAssociation = BinaryAssociation(
    name="name253",
    ends={
        Property(name="adb_Name254", type=adb_RequeueStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RequeueStatement", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delay255: BinaryAssociation = BinaryAssociation(
    name="delay255",
    ends={
        Property(name="adb_Expression256", type=adb_DelayStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DelayStatement", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
acceptStatement277: BinaryAssociation = BinaryAssociation(
    name="acceptStatement277",
    ends={
        Property(name="adb_AcceptStatement278", type=adb_AcceptAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AcceptAlternative", type=adb_AcceptStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delayStatement279: BinaryAssociation = BinaryAssociation(
    name="delayStatement279",
    ends={
        Property(name="adb_DelayStatement280", type=adb_DelayAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DelayAlternative", type=adb_DelayStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryCallAlternative281: BinaryAssociation = BinaryAssociation(
    name="entryCallAlternative281",
    ends={
        Property(name="adb_EntryCallAlternative", type=adb_TimedEntryCall, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TimedEntryCall", type=adb_EntryCallAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard265: BinaryAssociation = BinaryAssociation(
    name="guard265",
    ends={
        Property(name="adb_Guard267", type=adb_GuardedAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GuardedAlternative266", type=adb_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternative268: BinaryAssociation = BinaryAssociation(
    name="alternative268",
    ends={
        Property(name="adb_SelectAlternative270", type=adb_GuardedAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GuardedAlternative269", type=adb_SelectAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition271: BinaryAssociation = BinaryAssociation(
    name="condition271",
    ends={
        Property(name="adb_Expression273", type=adb_Guard, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Guard272", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOfStatements274: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements274",
    ends={
        Property(name="adb_SequenceOfStatements276", type=adb_SelectAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SelectAlternative275", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggeringAlternative296: BinaryAssociation = BinaryAssociation(
    name="triggeringAlternative296",
    ends={
        Property(name="adb_TriggeringAlternative", type=adb_AsynchronousSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AsynchronousSelect", type=adb_TriggeringAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
abortablePart297: BinaryAssociation = BinaryAssociation(
    name="abortablePart297",
    ends={
        Property(name="adb_AbortablePart", type=adb_AsynchronousSelect, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AsynchronousSelect298", type=adb_AbortablePart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
triggeringStatement299: BinaryAssociation = BinaryAssociation(
    name="triggeringStatement299",
    ends={
        Property(name="adb_TriggeringStatement", type=adb_TriggeringAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TriggeringAlternative300", type=adb_TriggeringStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOfStatements301: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements301",
    ends={
        Property(name="adb_SequenceOfStatements303", type=adb_TriggeringAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TriggeringAlternative302", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delayAlternative282: BinaryAssociation = BinaryAssociation(
    name="delayAlternative282",
    ends={
        Property(name="adb_DelayAlternative284", type=adb_TimedEntryCall, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TimedEntryCall283", type=adb_DelayAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call285: BinaryAssociation = BinaryAssociation(
    name="call285",
    ends={
        Property(name="adb_ProcedureOrEntryCallStatement287", type=adb_EntryCallAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryCallAlternative286", type=adb_ProcedureOrEntryCallStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceOfStatements288: BinaryAssociation = BinaryAssociation(
    name="sequenceOfStatements288",
    ends={
        Property(name="adb_SequenceOfStatements290", type=adb_EntryCallAlternative, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntryCallAlternative289", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entryCallAlternative291: BinaryAssociation = BinaryAssociation(
    name="entryCallAlternative291",
    ends={
        Property(name="adb_EntryCallAlternative292", type=adb_ConditionalEntryCall, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ConditionalEntryCall", type=adb_EntryCallAlternative, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseSequenceOfStatements293: BinaryAssociation = BinaryAssociation(
    name="elseSequenceOfStatements293",
    ends={
        Property(name="adb_SequenceOfStatements295", type=adb_ConditionalEntryCall, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ConditionalEntryCall294", type=adb_SequenceOfStatements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properBody306: BinaryAssociation = BinaryAssociation(
    name="properBody306",
    ends={
        Property(name="adb_ProperBody", type=adb_SeparateSubunit, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SeparateSubunit", type=adb_ProperBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptionName307: BinaryAssociation = BinaryAssociation(
    name="exceptionName307",
    ends={
        Property(name="adb_Name308", type=adb_RaiseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RaiseStatement", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withExpression309: BinaryAssociation = BinaryAssociation(
    name="withExpression309",
    ends={
        Property(name="adb_Expression311", type=adb_RaiseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RaiseStatement310", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
genericAssociation312: BinaryAssociation = BinaryAssociation(
    name="genericAssociation312",
    ends={
        Property(name="adb_GenericAssociation314", type=adb_GenericActualPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericActualPart313", type=adb_GenericAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskNames304: BinaryAssociation = BinaryAssociation(
    name="taskNames304",
    ends={
        Property(name="adb_Name305", type=adb_TaskNames, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_TaskNames", type=adb_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definingIdentifiers319: BinaryAssociation = BinaryAssociation(
    name="definingIdentifiers319",
    ends={
        Property(name="adb_DefiningIdentifierList321", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantSpecification320", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optNullExclusion322: BinaryAssociation = BinaryAssociation(
    name="optNullExclusion322",
    ends={
        Property(name="adb_OptNullExclusion324", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantSpecification323", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessDefinition325: BinaryAssociation = BinaryAssociation(
    name="accessDefinition325",
    ends={
        Property(name="adb_NotNullAccessDefinition", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantSpecification326", type=adb_NotNullAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark327: BinaryAssociation = BinaryAssociation(
    name="subtypeMark327",
    ends={
        Property(name="adb_Name329", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantSpecification328", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue330: BinaryAssociation = BinaryAssociation(
    name="defaultValue330",
    ends={
        Property(name="adb_Expression332", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantSpecification331", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expplicitGenericActualParam315: BinaryAssociation = BinaryAssociation(
    name="expplicitGenericActualParam315",
    ends={
        Property(name="adb_ExplicitGenericActualParameter", type=adb_GenericAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_GenericAssociation316", type=adb_ExplicitGenericActualParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantsSpecification317: BinaryAssociation = BinaryAssociation(
    name="discriminantsSpecification317",
    ends={
        Property(name="adb_DiscriminantSpecification", type=adb_KnownDiscriminantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_KnownDiscriminantPart318", type=adb_DiscriminantSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterAndResultProfile353: BinaryAssociation = BinaryAssociation(
    name="parameterAndResultProfile353",
    ends={
        Property(name="adb_ParameterAndResultProfile355", type=adb_AccessToSubprogramDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessToSubprogramDefinition354", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeIndication338: BinaryAssociation = BinaryAssociation(
    name="subtypeIndication338",
    ends={
        Property(name="adb_SubtypeIndication339", type=adb_DerivedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DerivedTypeDefinition", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList340: BinaryAssociation = BinaryAssociation(
    name="interfaceList340",
    ends={
        Property(name="adb_InterfaceList342", type=adb_DerivedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DerivedTypeDefinition341", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordExtentionPart343: BinaryAssociation = BinaryAssociation(
    name="recordExtentionPart343",
    ends={
        Property(name="adb_RecordExtensionPart", type=adb_DerivedTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DerivedTypeDefinition344", type=adb_RecordExtensionPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordDefinition345: BinaryAssociation = BinaryAssociation(
    name="recordDefinition345",
    ends={
        Property(name="adb_RecordDefinition", type=adb_RecordExtensionPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RecordExtensionPart346", type=adb_RecordDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceSubtypeMark333: BinaryAssociation = BinaryAssociation(
    name="interfaceSubtypeMark333",
    ends={
        Property(name="adb_Name335", type=adb_InterfaceList, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_InterfaceList334", type=adb_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optNullExclusion347: BinaryAssociation = BinaryAssociation(
    name="optNullExclusion347",
    ends={
        Property(name="adb_OptNullExclusion348", type=adb_AccessTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessTypeDefinition", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessDefinition349: BinaryAssociation = BinaryAssociation(
    name="accessDefinition349",
    ends={
        Property(name="adb_AccessSpecification", type=adb_AccessTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessTypeDefinition350", type=adb_AccessSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceList336: BinaryAssociation = BinaryAssociation(
    name="interfaceList336",
    ends={
        Property(name="adb_InterfaceList337", type=adb_InterfaceTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_InterfaceTypeDefinition", type=adb_InterfaceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart351: BinaryAssociation = BinaryAssociation(
    name="formalPart351",
    ends={
        Property(name="adb_FormalPart352", type=adb_AccessToSubprogramDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessToSubprogramDefinition", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousAccessDefinition369: BinaryAssociation = BinaryAssociation(
    name="anonymousAccessDefinition369",
    ends={
        Property(name="adb_AnonymousAccessDefinition371", type=adb_ComponentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentDefinition370", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeIndication356: BinaryAssociation = BinaryAssociation(
    name="subtypeIndication356",
    ends={
        Property(name="adb_SubtypeIndication357", type=adb_AccessToDataDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessToDataDefinition", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayIndexes358: BinaryAssociation = BinaryAssociation(
    name="arrayIndexes358",
    ends={
        Property(name="adb_ArrayIndexes", type=adb_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ArrayTypeDefinition359", type=adb_ArrayIndexes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentDefinition360: BinaryAssociation = BinaryAssociation(
    name="componentDefinition360",
    ends={
        Property(name="adb_ComponentDefinition", type=adb_ArrayTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ArrayTypeDefinition361", type=adb_ComponentDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark362: BinaryAssociation = BinaryAssociation(
    name="subtypeMark362",
    ends={
        Property(name="adb_Name363", type=adb_UnconstrainedIndexes, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_UnconstrainedIndexes", type=adb_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainedIndex364: BinaryAssociation = BinaryAssociation(
    name="constrainedIndex364",
    ends={
        Property(name="adb_DiscreteSubtypeDefinition365", type=adb_ConstrainedIndexes, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ConstrainedIndexes", type=adb_DiscreteSubtypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subtypeIndication366: BinaryAssociation = BinaryAssociation(
    name="subtypeIndication366",
    ends={
        Property(name="adb_SubtypeIndication368", type=adb_ComponentDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentDefinition367", type=adb_SubtypeIndication, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterSpecifications392: BinaryAssociation = BinaryAssociation(
    name="parameterSpecifications392",
    ends={
        Property(name="adb_FormalPart393", type=adb_ParameterSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="adb_ParameterSpecification", type=adb_FormalPart, multiplicity=Multiplicity(1, 1))
    }
)
definingIdentifiers394: BinaryAssociation = BinaryAssociation(
    name="definingIdentifiers394",
    ends={
        Property(name="adb_DefiningIdentifierList396", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification395", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optNullExclusion372: BinaryAssociation = BinaryAssociation(
    name="optNullExclusion372",
    ends={
        Property(name="adb_OptNullExclusion374", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AnonymousAccessDefinition373", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessDef375: BinaryAssociation = BinaryAssociation(
    name="accessDef375",
    ends={
        Property(name="adb_NotNullAccessDefinition377", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AnonymousAccessDefinition376", type=adb_NotNullAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name378: BinaryAssociation = BinaryAssociation(
    name="name378",
    ends={
        Property(name="adb_Name379", type=adb_AccessToDataInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AccessToDataInstance", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalPart380: BinaryAssociation = BinaryAssociation(
    name="formalPart380",
    ends={
        Property(name="adb_FormalPart382", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterAndResultProfile381", type=adb_FormalPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opt_nullExclusion383: BinaryAssociation = BinaryAssociation(
    name="opt_nullExclusion383",
    ends={
        Property(name="adb_OptNullExclusion385", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterAndResultProfile384", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark386: BinaryAssociation = BinaryAssociation(
    name="subtypeMark386",
    ends={
        Property(name="adb_Name388", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterAndResultProfile387", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousAccessDefinition389: BinaryAssociation = BinaryAssociation(
    name="anonymousAccessDefinition389",
    ends={
        Property(name="adb_AnonymousAccessDefinition391", type=adb_ParameterAndResultProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterAndResultProfile390", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last413: BinaryAssociation = BinaryAssociation(
    name="last413",
    ends={
        Property(name="adb_SimpleExpression415", type=adb_SignedIntegerTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SignedIntegerTypeDefinition414", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mode397: BinaryAssociation = BinaryAssociation(
    name="mode397",
    ends={
        Property(name="adb_Mode399", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification398", type=adb_Mode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optNullExclusion400: BinaryAssociation = BinaryAssociation(
    name="optNullExclusion400",
    ends={
        Property(name="adb_OptNullExclusion402", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification401", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypeMark403: BinaryAssociation = BinaryAssociation(
    name="subtypeMark403",
    ends={
        Property(name="adb_Name405", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification404", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonymousAccessDefinition406: BinaryAssociation = BinaryAssociation(
    name="anonymousAccessDefinition406",
    ends={
        Property(name="adb_AnonymousAccessDefinition408", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification407", type=adb_AnonymousAccessDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpression409: BinaryAssociation = BinaryAssociation(
    name="defaultExpression409",
    ends={
        Property(name="adb_Expression411", type=adb_ParameterSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterSpecification410", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first412: BinaryAssociation = BinaryAssociation(
    name="first412",
    ends={
        Property(name="adb_SimpleExpression", type=adb_SignedIntegerTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SignedIntegerTypeDefinition", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optVariantPart424: BinaryAssociation = BinaryAssociation(
    name="optVariantPart424",
    ends={
        Property(name="adb_OptVariantPart", type=adb_ComponentList, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentList425", type=adb_OptVariantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variantPart426: BinaryAssociation = BinaryAssociation(
    name="variantPart426",
    ends={
        Property(name="adb_VariantPart", type=adb_OptVariantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_OptVariantPart427", type=adb_VariantPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticExpression416: BinaryAssociation = BinaryAssociation(
    name="staticExpression416",
    ends={
        Property(name="adb_Expression417", type=adb_ModularTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ModularTypeDefinition", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordDefinition418: BinaryAssociation = BinaryAssociation(
    name="recordDefinition418",
    ends={
        Property(name="adb_RecordDefinition419", type=adb_RecordTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RecordTypeDefinition", type=adb_RecordDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentList420: BinaryAssociation = BinaryAssociation(
    name="componentList420",
    ends={
        Property(name="adb_ComponentList", type=adb_RecordDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RecordDefinition421", type=adb_ComponentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentItems422: BinaryAssociation = BinaryAssociation(
    name="componentItems422",
    ends={
        Property(name="adb_ComponentItem", type=adb_ComponentList, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentList423", type=adb_ComponentItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mod438: BinaryAssociation = BinaryAssociation(
    name="mod438",
    ends={
        Property(name="adb_ModClause", type=adb_AspectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AspectClause439", type=adb_ModClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingIdentifiers428: BinaryAssociation = BinaryAssociation(
    name="definingIdentifiers428",
    ends={
        Property(name="adb_DefiningIdentifierList429", type=adb_ComponentDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentDeclaration", type=adb_DefiningIdentifierList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentDefinition430: BinaryAssociation = BinaryAssociation(
    name="componentDefinition430",
    ends={
        Property(name="adb_ComponentDefinition432", type=adb_ComponentDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentDeclaration431", type=adb_ComponentDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultExpression433: BinaryAssociation = BinaryAssociation(
    name="defaultExpression433",
    ends={
        Property(name="adb_Expression435", type=adb_ComponentDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentDeclaration434", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression436: BinaryAssociation = BinaryAssociation(
    name="expression436",
    ends={
        Property(name="adb_Expression437", type=adb_AspectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AspectClause", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentList459: BinaryAssociation = BinaryAssociation(
    name="componentList459",
    ends={
        Property(name="adb_ComponentList461", type=adb_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Variant460", type=adb_ComponentList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentClause440: BinaryAssociation = BinaryAssociation(
    name="componentClause440",
    ends={
        Property(name="adb_ComponentClause", type=adb_AspectClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AspectClause441", type=adb_ComponentClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mod442: BinaryAssociation = BinaryAssociation(
    name="mod442",
    ends={
        Property(name="adb_Expression444", type=adb_ModClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ModClause443", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
position445: BinaryAssociation = BinaryAssociation(
    name="position445",
    ends={
        Property(name="adb_Expression447", type=adb_ComponentClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentClause446", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstBit448: BinaryAssociation = BinaryAssociation(
    name="firstBit448",
    ends={
        Property(name="adb_SimpleExpression450", type=adb_ComponentClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentClause449", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastBit451: BinaryAssociation = BinaryAssociation(
    name="lastBit451",
    ends={
        Property(name="adb_SimpleExpression453", type=adb_ComponentClause, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ComponentClause452", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variants454: BinaryAssociation = BinaryAssociation(
    name="variants454",
    ends={
        Property(name="adb_Variant", type=adb_VariantPart, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_VariantPart455", type=adb_Variant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discreteChoiceList456: BinaryAssociation = BinaryAssociation(
    name="discreteChoiceList456",
    ends={
        Property(name="adb_DiscreteChoiceList458", type=adb_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Variant457", type=adb_DiscreteChoiceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discreteChoiceList462: BinaryAssociation = BinaryAssociation(
    name="discreteChoiceList462",
    ends={
        Property(name="adb_DiscreteChoice", type=adb_DiscreteChoiceList, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscreteChoiceList463", type=adb_DiscreteChoice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
digits464: BinaryAssociation = BinaryAssociation(
    name="digits464",
    ends={
        Property(name="adb_Expression465", type=adb_RealTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RealTypeDefinition", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
realRangeSpecification466: BinaryAssociation = BinaryAssociation(
    name="realRangeSpecification466",
    ends={
        Property(name="adb_RealRangeSpecification", type=adb_RealTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RealTypeDefinition467", type=adb_RealRangeSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerBound468: BinaryAssociation = BinaryAssociation(
    name="lowerBound468",
    ends={
        Property(name="adb_SimpleExpression470", type=adb_RealRangeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RealRangeSpecification469", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperBound471: BinaryAssociation = BinaryAssociation(
    name="upperBound471",
    ends={
        Property(name="adb_SimpleExpression473", type=adb_RealRangeSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RealRangeSpecification472", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delta474: BinaryAssociation = BinaryAssociation(
    name="delta474",
    ends={
        Property(name="adb_Expression475", type=adb_FixedPointDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_FixedPointDefinition", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
terms488: BinaryAssociation = BinaryAssociation(
    name="terms488",
    ends={
        Property(name="adb_Term", type=adb_SimpleExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SimpleExpression489", type=adb_Term, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations476: BinaryAssociation = BinaryAssociation(
    name="relations476",
    ends={
        Property(name="adb_Relation", type=adb_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Expression477", type=adb_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleExpression478: BinaryAssociation = BinaryAssociation(
    name="simpleExpression478",
    ends={
        Property(name="adb_SimpleExpression480", type=adb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Relation479", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subSimpleExpression481: BinaryAssociation = BinaryAssociation(
    name="subSimpleExpression481",
    ends={
        Property(name="adb_SimpleExpression483", type=adb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Relation482", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
membership484: BinaryAssociation = BinaryAssociation(
    name="membership484",
    ends={
        Property(name="adb_Membership", type=adb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Relation485", type=adb_Membership, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interval486: BinaryAssociation = BinaryAssociation(
    name="interval486",
    ends={
        Property(name="adb_Interval", type=adb_Membership, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Membership487", type=adb_Interval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name497: BinaryAssociation = BinaryAssociation(
    name="name497",
    ends={
        Property(name="adb_Name498", type=adb_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_QualifiedName", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
factors490: BinaryAssociation = BinaryAssociation(
    name="factors490",
    ends={
        Property(name="adb_Factor", type=adb_Term, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Term491", type=adb_Factor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary492: BinaryAssociation = BinaryAssociation(
    name="primary492",
    ends={
        Property(name="adb_Primary", type=adb_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Factor493", type=adb_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exponent494: BinaryAssociation = BinaryAssociation(
    name="exponent494",
    ends={
        Property(name="adb_Primary496", type=adb_Factor, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Factor495", type=adb_Primary, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
optConstraint511: BinaryAssociation = BinaryAssociation(
    name="optConstraint511",
    ends={
        Property(name="adb_EObject", type=adb_OptConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_OptConstraint512", type=adb_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier499: BinaryAssociation = BinaryAssociation(
    name="qualifier499",
    ends={
        Property(name="adb_Qualifier", type=adb_QualifiedName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_QualifiedName500", type=adb_Qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeName501: BinaryAssociation = BinaryAssociation(
    name="typeName501",
    ends={
        Property(name="adb_Name502", type=adb_Allocator, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Allocator", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier503: BinaryAssociation = BinaryAssociation(
    name="qualifier503",
    ends={
        Property(name="adb_Qualifier505", type=adb_Allocator, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Allocator504", type=adb_Qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opt_nullExclusion506: BinaryAssociation = BinaryAssociation(
    name="opt_nullExclusion506",
    ends={
        Property(name="adb_OptNullExclusion508", type=adb_SubtypeIndication, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubtypeIndication507", type=adb_OptNullExclusion, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
opt_constraint509: BinaryAssociation = BinaryAssociation(
    name="opt_constraint509",
    ends={
        Property(name="adb_OptConstraint", type=adb_SubtypeIndication, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_SubtypeIndication510", type=adb_OptConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
digits513: BinaryAssociation = BinaryAssociation(
    name="digits513",
    ends={
        Property(name="adb_SimpleExpression514", type=adb_DigitsConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DigitsConstraint", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangeConstraint515: BinaryAssociation = BinaryAssociation(
    name="rangeConstraint515",
    ends={
        Property(name="adb_RangeConstraint", type=adb_DigitsConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DigitsConstraint516", type=adb_RangeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delta517: BinaryAssociation = BinaryAssociation(
    name="delta517",
    ends={
        Property(name="adb_SimpleExpression518", type=adb_DeltaConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DeltaConstraint", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rangeConstraint519: BinaryAssociation = BinaryAssociation(
    name="rangeConstraint519",
    ends={
        Property(name="adb_RangeConstraint521", type=adb_DeltaConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DeltaConstraint520", type=adb_RangeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
discriminantAssociation522: BinaryAssociation = BinaryAssociation(
    name="discriminantAssociation522",
    ends={
        Property(name="adb_DiscriminantAssociation", type=adb_DiscriminantConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantConstraint", type=adb_DiscriminantAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discreteRange523: BinaryAssociation = BinaryAssociation(
    name="discreteRange523",
    ends={
        Property(name="adb_DiscreteRange", type=adb_IndexConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_IndexConstraint", type=adb_DiscreteRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discriminantSelectors524: BinaryAssociation = BinaryAssociation(
    name="discriminantSelectors524",
    ends={
        Property(name="adb_DiscriminantSelectors", type=adb_DiscriminantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantAssociation525", type=adb_DiscriminantSelectors, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actualParameter526: BinaryAssociation = BinaryAssociation(
    name="actualParameter526",
    ends={
        Property(name="adb_Expression528", type=adb_DiscriminantAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_DiscriminantAssociation527", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordComponentAssociation529: BinaryAssociation = BinaryAssociation(
    name="recordComponentAssociation529",
    ends={
        Property(name="adb_RecordComponentAssociation", type=adb_RecordComponentAssociationList, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RecordComponentAssociationList", type=adb_RecordComponentAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentChoiceList530: BinaryAssociation = BinaryAssociation(
    name="componentChoiceList530",
    ends={
        Property(name="adb_ComponentChoiceList", type=adb_RecordComponentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_RecordComponentAssociation531", type=adb_ComponentChoiceList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value532: BinaryAssociation = BinaryAssociation(
    name="value532",
    ends={
        Property(name="adb_Expression533", type=adb_InitializedComponents, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_InitializedComponents", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ancestorPart534: BinaryAssociation = BinaryAssociation(
    name="ancestorPart534",
    ends={
        Property(name="adb_AncestorPart", type=adb_ExtensionAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExtensionAggregate", type=adb_AncestorPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
recordComponentAssociationList535: BinaryAssociation = BinaryAssociation(
    name="recordComponentAssociationList535",
    ends={
        Property(name="adb_RecordComponentAssociationList537", type=adb_ExtensionAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExtensionAggregate536", type=adb_RecordComponentAssociationList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryName550: BinaryAssociation = BinaryAssociation(
    name="primaryName550",
    ends={
        Property(name="adb_PrimaryName", type=adb_Name, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_Name551", type=adb_PrimaryName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValues538: BinaryAssociation = BinaryAssociation(
    name="initialValues538",
    ends={
        Property(name="adb_Expression539", type=adb_PositionalArrayAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PositionalArrayAggregate", type=adb_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
othersValue540: BinaryAssociation = BinaryAssociation(
    name="othersValue540",
    ends={
        Property(name="adb_Expression542", type=adb_PositionalArrayAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PositionalArrayAggregate541", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arrayComponentAssociation543: BinaryAssociation = BinaryAssociation(
    name="arrayComponentAssociation543",
    ends={
        Property(name="adb_ArrayComponentAssociation", type=adb_NamedArrayAggregate, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_NamedArrayAggregate", type=adb_ArrayComponentAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
discreteChoiceList544: BinaryAssociation = BinaryAssociation(
    name="discreteChoiceList544",
    ends={
        Property(name="adb_DiscreteChoiceList546", type=adb_ArrayComponentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ArrayComponentAssociation545", type=adb_DiscreteChoiceList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression547: BinaryAssociation = BinaryAssociation(
    name="expression547",
    ends={
        Property(name="adb_Expression549", type=adb_ArrayComponentAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ArrayComponentAssociation548", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name566: BinaryAssociation = BinaryAssociation(
    name="name566",
    ends={
        Property(name="adb_Name567", type=adb_EntityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntityRange", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterAssociation552: BinaryAssociation = BinaryAssociation(
    name="parameterAssociation552",
    ends={
        Property(name="adb_ParameterAssociation", type=adb_PrimaryName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrimaryName553", type=adb_ParameterAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryName555: BinaryAssociation = BinaryAssociation(
    name="primaryName555",
    ends={
        Property(name="adb_PrimaryName556", type=adb_PrimaryName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrimaryName554", type=adb_PrimaryName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name557: BinaryAssociation = BinaryAssociation(
    name="name557",
    ends={
        Property(name="adb_Name559", type=adb_PrimaryName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrimaryName558", type=adb_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeDesignator560: BinaryAssociation = BinaryAssociation(
    name="attributeDesignator560",
    ends={
        Property(name="adb_AttributeDesignator", type=adb_PrimaryName, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_PrimaryName561", type=adb_AttributeDesignator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterEffectiveValue562: BinaryAssociation = BinaryAssociation(
    name="parameterEffectiveValue562",
    ends={
        Property(name="adb_ParameterEffectiveValue", type=adb_ParameterAssociation, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ParameterAssociation563", type=adb_ParameterEffectiveValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
staticExpression564: BinaryAssociation = BinaryAssociation(
    name="staticExpression564",
    ends={
        Property(name="adb_ParenthesizedExpression", type=adb_AttributeDesignator, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_AttributeDesignator565", type=adb_ParenthesizedExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index568: BinaryAssociation = BinaryAssociation(
    name="index568",
    ends={
        Property(name="adb_Expression570", type=adb_EntityRange, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_EntityRange569", type=adb_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
first571: BinaryAssociation = BinaryAssociation(
    name="first571",
    ends={
        Property(name="adb_SimpleExpression572", type=adb_ExplicitRange, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExplicitRange", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last573: BinaryAssociation = BinaryAssociation(
    name="last573",
    ends={
        Property(name="adb_SimpleExpression575", type=adb_ExplicitRange, multiplicity=Multiplicity(1, 1)),
        Property(name="adb_ExplicitRange574", type=adb_SimpleExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_adb_UseClause_ContextItem = Generalization(general=ContextItem, specific=adb_UseClause)
gen_adb_UseClause_BasicDeclarativeItem = Generalization(general=BasicDeclarativeItem, specific=adb_UseClause)
gen_adb_UseClause_GenericItem = Generalization(general=GenericItem, specific=adb_UseClause)
gen_adb_UsePackageClause_UseClause = Generalization(general=UseClause, specific=adb_UsePackageClause)
gen_adb_WithClause_ContextItem = Generalization(general=ContextItem, specific=adb_WithClause)
gen_adb_PackageDefinition_PackageDeclaration = Generalization(general=PackageDeclaration, specific=adb_PackageDefinition)
gen_adb_PackageDefinition_LibrarySpecification = Generalization(general=LibrarySpecification, specific=adb_PackageDefinition)
gen_adb_Renaming_PackageDeclaration = Generalization(general=PackageDeclaration, specific=adb_Renaming)
gen_adb_GenericDeclaration_LibraryUnitSpecification = Generalization(general=LibraryUnitSpecification, specific=adb_GenericDeclaration)
gen_adb_GenericDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_GenericDeclaration)
gen_adb_UseTypeClause_UseClause = Generalization(general=UseClause, specific=adb_UseTypeClause)
gen_adb_LibraryUnitDeclaration_Unit = Generalization(general=Unit, specific=adb_LibraryUnitDeclaration)
gen_adb_PackageDeclaration_LibraryUnitSpecification = Generalization(general=LibraryUnitSpecification, specific=adb_PackageDeclaration)
gen_adb_PackageDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_PackageDeclaration)
gen_adb_SubprogramBody_Unit = Generalization(general=Unit, specific=adb_SubprogramBody)
gen_adb_SubprogramBody_DeclarativeBlock = Generalization(general=DeclarativeBlock, specific=adb_SubprogramBody)
gen_adb_SubprogramBody_ProperBody = Generalization(general=ProperBody, specific=adb_SubprogramBody)
gen_adb_SubprogramBody_ProtectedOperationItem = Generalization(general=ProtectedOperationItem, specific=adb_SubprogramBody)
gen_adb_GenericInstantiation_LibraryUnitSpecification = Generalization(general=LibraryUnitSpecification, specific=adb_GenericInstantiation)
gen_adb_GenericInstantiation_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_GenericInstantiation)
gen_adb_TypeDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_TypeDeclaration)
gen_adb_BasicDeclarativeItem_DeclarativeItem = Generalization(general=DeclarativeItem, specific=adb_BasicDeclarativeItem)
gen_adb_BasicDeclaration_BasicDeclarativeItem = Generalization(general=BasicDeclarativeItem, specific=adb_BasicDeclaration)
gen_adb_TaskDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_TaskDeclaration)
gen_adb_PrivateTypeDeclaration_NewTypeDeclaration = Generalization(general=NewTypeDeclaration, specific=adb_PrivateTypeDeclaration)
gen_adb_PrivateExtensionDeclaration_NewTypeDeclaration = Generalization(general=NewTypeDeclaration, specific=adb_PrivateExtensionDeclaration)
gen_adb_NewTypeDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=adb_NewTypeDeclaration)
gen_adb_FullTypeDeclaration_NewTypeDeclaration = Generalization(general=NewTypeDeclaration, specific=adb_FullTypeDeclaration)
gen_adb_FullDataTypeDeclaration_FullTypeDeclaration = Generalization(general=FullTypeDeclaration, specific=adb_FullDataTypeDeclaration)
gen_adb_IncompleteTypeDeclaration_NewTypeDeclaration = Generalization(general=NewTypeDeclaration, specific=adb_IncompleteTypeDeclaration)
gen_adb_ProtectedTypeDeclaration_FullTypeDeclaration = Generalization(general=FullTypeDeclaration, specific=adb_ProtectedTypeDeclaration)
gen_adb_EntryDeclaration_TaskItem = Generalization(general=TaskItem, specific=adb_EntryDeclaration)
gen_adb_EntryDeclaration_ProtectedOperationDeclaration = Generalization(general=ProtectedOperationDeclaration, specific=adb_EntryDeclaration)
gen_adb_ProcedureSpecification_SubprogramSpecification = Generalization(general=SubprogramSpecification, specific=adb_ProcedureSpecification)
gen_adb_FunctionSpecification_SubprogramSpecification = Generalization(general=SubprogramSpecification, specific=adb_FunctionSpecification)
gen_adb_ProtectedOperationDeclaration_ProtectedElementDeclaration = Generalization(general=ProtectedElementDeclaration, specific=adb_ProtectedOperationDeclaration)
gen_adb_SubprogramDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_SubprogramDeclaration)
gen_adb_SubprogramDeclaration_ProtectedOperationDeclaration = Generalization(general=ProtectedOperationDeclaration, specific=adb_SubprogramDeclaration)
gen_adb_SubprogramDeclaration_ProtectedOperationItem = Generalization(general=ProtectedOperationItem, specific=adb_SubprogramDeclaration)
gen_adb_SubprogramSpecification_LibraryUnitSpecification = Generalization(general=LibraryUnitSpecification, specific=adb_SubprogramSpecification)
gen_adb_SubprogramSpecification_LibrarySpecification = Generalization(general=LibrarySpecification, specific=adb_SubprogramSpecification)
gen_adb_SubprogramSpecification_BodyStub = Generalization(general=BodyStub, specific=adb_SubprogramSpecification)
gen_adb_Body_DeclarativeItem = Generalization(general=DeclarativeItem, specific=adb_Body)
gen_adb_ProperBody_Body = Generalization(general=Body, specific=adb_ProperBody)
gen_adb_SequenceOfStatements_HandledSequenceOfStatements = Generalization(general=HandledSequenceOfStatements, specific=adb_SequenceOfStatements)
gen_adb_SequenceOfStatements_AbortablePart = Generalization(general=AbortablePart, specific=adb_SequenceOfStatements)
gen_adb_SimpleStatement_Statement = Generalization(general=Statement, specific=adb_SimpleStatement)
gen_adb_CompoundStatement_Statement = Generalization(general=Statement, specific=adb_CompoundStatement)
gen_adb_NullStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_NullStatement)
gen_adb_GenericFormalParameterDeclaration_GenericItem = Generalization(general=GenericItem, specific=adb_GenericFormalParameterDeclaration)
gen_adb_FormalObjectDeclaration_GenericFormalParameterDeclaration = Generalization(general=GenericFormalParameterDeclaration, specific=adb_FormalObjectDeclaration)
gen_adb_FormalSubprogramDeclaration_GenericFormalParameterDeclaration = Generalization(general=GenericFormalParameterDeclaration, specific=adb_FormalSubprogramDeclaration)
gen_adb_FormalTypeDeclaration_GenericFormalParameterDeclaration = Generalization(general=GenericFormalParameterDeclaration, specific=adb_FormalTypeDeclaration)
gen_adb_FormalPrivateTypeDefinition_FormalTypeDefinition = Generalization(general=FormalTypeDefinition, specific=adb_FormalPrivateTypeDefinition)
gen_adb_FormalDerivedTypeDefinition_FormalTypeDefinition = Generalization(general=FormalTypeDefinition, specific=adb_FormalDerivedTypeDefinition)
gen_adb_ExceptionDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_ExceptionDeclaration)
gen_adb_ObjectDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_ObjectDeclaration)
gen_adb_FormalPackageDeclaration_GenericFormalParameterDeclaration = Generalization(general=GenericFormalParameterDeclaration, specific=adb_FormalPackageDeclaration)
gen_adb_SingleProtectedDeclaration_ObjectDeclaration = Generalization(general=ObjectDeclaration, specific=adb_SingleProtectedDeclaration)
gen_adb_Pragma_ContextItem = Generalization(general=ContextItem, specific=adb_Pragma)
gen_adb_Pragma_BasicDeclarativeItem = Generalization(general=BasicDeclarativeItem, specific=adb_Pragma)
gen_adb_Pragma_Statement = Generalization(general=Statement, specific=adb_Pragma)
gen_adb_DataInstanceDeclaration_ObjectDeclaration = Generalization(general=ObjectDeclaration, specific=adb_DataInstanceDeclaration)
gen_adb_NumberDeclaration_BasicDeclaration = Generalization(general=BasicDeclaration, specific=adb_NumberDeclaration)
gen_adb_AssignmentStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_AssignmentStatement)
gen_adb_SubtypeDeclaration_TypeDeclaration = Generalization(general=TypeDeclaration, specific=adb_SubtypeDeclaration)
gen_adb_CaseStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_CaseStatement)
gen_adb_LoopStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_LoopStatement)
gen_adb_IfStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_IfStatement)
gen_adb_BlockStatement_DeclarativeBlock = Generalization(general=DeclarativeBlock, specific=adb_BlockStatement)
gen_adb_BlockStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_BlockStatement)
gen_adb_ExitStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_ExitStatement)
gen_adb_GotoStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_GotoStatement)
gen_adb_PackageBody_Unit = Generalization(general=Unit, specific=adb_PackageBody)
gen_adb_PackageBody_DeclarativeBlock = Generalization(general=DeclarativeBlock, specific=adb_PackageBody)
gen_adb_PackageBody_ProperBody = Generalization(general=ProperBody, specific=adb_PackageBody)
gen_adb_ProcedureOrEntryCallStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_ProcedureOrEntryCallStatement)
gen_adb_ProcedureOrEntryCallStatement_TriggeringStatement = Generalization(general=TriggeringStatement, specific=adb_ProcedureOrEntryCallStatement)
gen_adb_SimpleReturnStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_SimpleReturnStatement)
gen_adb_ExtendedReturnStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_ExtendedReturnStatement)
gen_adb_AcceptStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_AcceptStatement)
gen_adb_TaskBody_DeclarativeBlock = Generalization(general=DeclarativeBlock, specific=adb_TaskBody)
gen_adb_TaskBody_ProperBody = Generalization(general=ProperBody, specific=adb_TaskBody)
gen_adb_ProtectedBody_ProperBody = Generalization(general=ProperBody, specific=adb_ProtectedBody)
gen_adb_EntryBody_DeclarativeBlock = Generalization(general=DeclarativeBlock, specific=adb_EntryBody)
gen_adb_EntryBody_ProtectedOperationItem = Generalization(general=ProtectedOperationItem, specific=adb_EntryBody)
gen_adb_SelectiveAccept_SelectStatement = Generalization(general=SelectStatement, specific=adb_SelectiveAccept)
gen_adb_RequeueStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_RequeueStatement)
gen_adb_DelayStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_DelayStatement)
gen_adb_DelayStatement_TriggeringStatement = Generalization(general=TriggeringStatement, specific=adb_DelayStatement)
gen_adb_SelectStatement_CompoundStatement = Generalization(general=CompoundStatement, specific=adb_SelectStatement)
gen_adb_DelayAlternative_SelectAlternative = Generalization(general=SelectAlternative, specific=adb_DelayAlternative)
gen_adb_TimedEntryCall_SelectStatement = Generalization(general=SelectStatement, specific=adb_TimedEntryCall)
gen_adb_AcceptAlternative_SelectAlternative = Generalization(general=SelectAlternative, specific=adb_AcceptAlternative)
gen_adb_AsynchronousSelect_SelectStatement = Generalization(general=SelectStatement, specific=adb_AsynchronousSelect)
gen_adb_ConditionalEntryCall_SelectStatement = Generalization(general=SelectStatement, specific=adb_ConditionalEntryCall)
gen_adb_RaiseStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_RaiseStatement)
gen_adb_AbortStatement_SimpleStatement = Generalization(general=SimpleStatement, specific=adb_AbortStatement)
gen_adb_TaskNames_AbortStatement = Generalization(general=AbortStatement, specific=adb_TaskNames)
gen_adb_BodyStub_Body = Generalization(general=Body, specific=adb_BodyStub)
gen_adb_PackageBodyStub_BodyStub = Generalization(general=BodyStub, specific=adb_PackageBodyStub)
gen_adb_TaskBodyStub_BodyStub = Generalization(general=BodyStub, specific=adb_TaskBodyStub)
gen_adb_ProtectedBodyStub_BodyStub = Generalization(general=BodyStub, specific=adb_ProtectedBodyStub)
gen_adb_SeparateSubunit_Unit = Generalization(general=Unit, specific=adb_SeparateSubunit)
gen_adb_UnknownDiscriminantPart_DiscriminantPart = Generalization(general=DiscriminantPart, specific=adb_UnknownDiscriminantPart)
gen_adb_KnownDiscriminantPart_DiscriminantPart = Generalization(general=DiscriminantPart, specific=adb_KnownDiscriminantPart)
gen_adb_AccessTypeDefinition_FormalTypeDefinition = Generalization(general=FormalTypeDefinition, specific=adb_AccessTypeDefinition)
gen_adb_AccessTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_AccessTypeDefinition)
gen_adb_InterfaceTypeDefinition_FormalTypeDefinition = Generalization(general=FormalTypeDefinition, specific=adb_InterfaceTypeDefinition)
gen_adb_InterfaceTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_InterfaceTypeDefinition)
gen_adb_AccessToSubprogramDefinition_AccessSpecification = Generalization(general=AccessSpecification, specific=adb_AccessToSubprogramDefinition)
gen_adb_AccessToSubprogramDefinition_NotNullAccessDefinition = Generalization(general=NotNullAccessDefinition, specific=adb_AccessToSubprogramDefinition)
gen_adb_DerivedTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_DerivedTypeDefinition)
gen_adb_AccessToDataDefinition_AccessSpecification = Generalization(general=AccessSpecification, specific=adb_AccessToDataDefinition)
gen_adb_AnonymousAccessDefinition_ReturnSubtypeIndication = Generalization(general=ReturnSubtypeIndication, specific=adb_AnonymousAccessDefinition)
gen_adb_ArrayTypeDefinition_FormalTypeDefinition = Generalization(general=FormalTypeDefinition, specific=adb_ArrayTypeDefinition)
gen_adb_ArrayTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_ArrayTypeDefinition)
gen_adb_UnconstrainedIndexes_ArrayIndexes = Generalization(general=ArrayIndexes, specific=adb_UnconstrainedIndexes)
gen_adb_ConstrainedIndexes_ArrayIndexes = Generalization(general=ArrayIndexes, specific=adb_ConstrainedIndexes)
gen_adb_AccessToDataInstance_NotNullAccessDefinition = Generalization(general=NotNullAccessDefinition, specific=adb_AccessToDataInstance)
gen_adb_ModularTypeDefinition_IntegerTypeDefinition = Generalization(general=IntegerTypeDefinition, specific=adb_ModularTypeDefinition)
gen_adb_IntegerTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_IntegerTypeDefinition)
gen_adb_SignedIntegerTypeDefinition_IntegerTypeDefinition = Generalization(general=IntegerTypeDefinition, specific=adb_SignedIntegerTypeDefinition)
gen_adb_EnumerationTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_EnumerationTypeDefinition)
gen_adb_RecordTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_RecordTypeDefinition)
gen_adb_ComponentDeclaration_ProtectedElementDeclaration = Generalization(general=ProtectedElementDeclaration, specific=adb_ComponentDeclaration)
gen_adb_ComponentDeclaration_ComponentItem = Generalization(general=ComponentItem, specific=adb_ComponentDeclaration)
gen_adb_AspectClause_BasicDeclarativeItem = Generalization(general=BasicDeclarativeItem, specific=adb_AspectClause)
gen_adb_AspectClause_TaskItem = Generalization(general=TaskItem, specific=adb_AspectClause)
gen_adb_AspectClause_ProtectedOperationDeclaration = Generalization(general=ProtectedOperationDeclaration, specific=adb_AspectClause)
gen_adb_AspectClause_ProtectedOperationItem = Generalization(general=ProtectedOperationItem, specific=adb_AspectClause)
gen_adb_AspectClause_ComponentItem = Generalization(general=ComponentItem, specific=adb_AspectClause)
gen_adb_Expression_ExplicitGenericActualParameter = Generalization(general=ExplicitGenericActualParameter, specific=adb_Expression)
gen_adb_Expression_DiscreteChoice = Generalization(general=DiscreteChoice, specific=adb_Expression)
gen_adb_RealTypeDefinition_TypeDefinition = Generalization(general=TypeDefinition, specific=adb_RealTypeDefinition)
gen_adb_FloatingPointDefinition_RealTypeDefinition = Generalization(general=RealTypeDefinition, specific=adb_FloatingPointDefinition)
gen_adb_FixedPointDefinition_RealTypeDefinition = Generalization(general=RealTypeDefinition, specific=adb_FixedPointDefinition)
gen_adb_Expression_EntryIndex = Generalization(general=EntryIndex, specific=adb_Expression)
gen_adb_Expression_AncestorPart = Generalization(general=AncestorPart, specific=adb_Expression)
gen_adb_Expression_ParameterEffectiveValue = Generalization(general=ParameterEffectiveValue, specific=adb_Expression)
gen_adb_NumericLiteral_Primary = Generalization(general=Primary, specific=adb_NumericLiteral)
gen_adb_Null_Primary = Generalization(general=Primary, specific=adb_Null)
gen_adb_StringLiteral_Primary = Generalization(general=Primary, specific=adb_StringLiteral)
gen_adb_QualifiedName_Primary = Generalization(general=Primary, specific=adb_QualifiedName)
gen_adb_ParenthesizedExpression_Primary = Generalization(general=Primary, specific=adb_ParenthesizedExpression)
gen_adb_Allocator_Primary = Generalization(general=Primary, specific=adb_Allocator)
gen_adb_SubtypeIndication_ReturnSubtypeIndication = Generalization(general=ReturnSubtypeIndication, specific=adb_SubtypeIndication)
gen_adb_SubtypeIndication_DiscreteSubtypeDefinition = Generalization(general=DiscreteSubtypeDefinition, specific=adb_SubtypeIndication)
gen_adb_SubtypeIndication_DiscreteRange = Generalization(general=DiscreteRange, specific=adb_SubtypeIndication)
gen_adb_SubtypeIndication_DiscreteChoice = Generalization(general=DiscreteChoice, specific=adb_SubtypeIndication)
gen_adb_IndexConstraint_CompositeConstraint = Generalization(general=CompositeConstraint, specific=adb_IndexConstraint)
gen_adb_DigitsConstraint_ScalarConstraint = Generalization(general=ScalarConstraint, specific=adb_DigitsConstraint)
gen_adb_DeltaConstraint_ScalarConstraint = Generalization(general=ScalarConstraint, specific=adb_DeltaConstraint)
gen_adb_RangeConstraint_ScalarConstraint = Generalization(general=ScalarConstraint, specific=adb_RangeConstraint)
gen_adb_DiscriminantConstraint_CompositeConstraint = Generalization(general=CompositeConstraint, specific=adb_DiscriminantConstraint)
gen_adb_RecordAggregate_Aggregate = Generalization(general=Aggregate, specific=adb_RecordAggregate)
gen_adb_RecordComponentAssociationList_RecordAggregate = Generalization(general=RecordAggregate, specific=adb_RecordComponentAssociationList)
gen_adb_DiscreteRange_DiscreteSubtypeDefinition = Generalization(general=DiscreteSubtypeDefinition, specific=adb_DiscreteRange)
gen_adb_Aggregate_ParenthesizedExpression = Generalization(general=ParenthesizedExpression, specific=adb_Aggregate)
gen_adb_Aggregate_Qualifier = Generalization(general=Qualifier, specific=adb_Aggregate)
gen_adb_ArrayAggregate_Aggregate = Generalization(general=Aggregate, specific=adb_ArrayAggregate)
gen_adb_PositionalArrayAggregate_ArrayAggregate = Generalization(general=ArrayAggregate, specific=adb_PositionalArrayAggregate)
gen_adb_InitializedComponents_RecordComponentAssociation = Generalization(general=RecordComponentAssociation, specific=adb_InitializedComponents)
gen_adb_UninitializedComponents_RecordComponentAssociation = Generalization(general=RecordComponentAssociation, specific=adb_UninitializedComponents)
gen_adb_ExtensionAggregate_Aggregate = Generalization(general=Aggregate, specific=adb_ExtensionAggregate)
gen_adb_NamedArrayAggregate_ArrayAggregate = Generalization(general=ArrayAggregate, specific=adb_NamedArrayAggregate)
gen_adb_Name_Interval = Generalization(general=Interval, specific=adb_Name)
gen_adb_EntityRange_Range = Generalization(general=Range, specific=adb_EntityRange)
gen_adb_Range_Interval = Generalization(general=Interval, specific=adb_Range)
gen_adb_Range_RangeConstraint = Generalization(general=RangeConstraint, specific=adb_Range)
gen_adb_Range_DiscreteRange = Generalization(general=DiscreteRange, specific=adb_Range)
gen_adb_Range_DiscreteChoice = Generalization(general=DiscreteChoice, specific=adb_Range)
gen_adb_Range_ParameterEffectiveValue = Generalization(general=ParameterEffectiveValue, specific=adb_Range)
gen_adb_ExplicitRange_Range = Generalization(general=Range, specific=adb_ExplicitRange)

# Domain Model
domain_model = DomainModel(
    name="adb",
    types={adb_Compilation, adb_CompilationUnit, adb_LibraryUnitDeclaration, adb_UseClause, BasicDeclarativeItem, GenericItem, adb_UsePackageClause, UseClause, adb_ContextClause, adb_Unit, adb_Pragma, adb_ContextItem, adb_WithClause, ContextItem, adb_PackageDefinition, PackageDeclaration, LibrarySpecification, adb_PackageSpecification, adb_Renaming, adb_GenericDeclaration, adb_GenericItems, adb_UseTypeClause, Unit, adb_LibraryUnitSpecification, adb_PackageDeclaration, LibraryUnitSpecification, BasicDeclaration, adb_SubprogramBody, DeclarativeBlock, ProperBody, ProtectedOperationItem, adb_SubprogramSpecification, adb_LibrarySpecification, adb_GenericInstantiation, adb_OverridingIndicator, adb_GenericActualPart, adb_BasicDeclarativeItem, adb_InterfaceList, adb_TaskDefinition, adb_TypeDeclaration, adb_DeclarativeBlock, adb_DeclarativeItem, adb_HandledSequenceOfStatements, DeclarativeItem, adb_BasicDeclaration, adb_TaskDeclaration, adb_KnownDiscriminantPart, adb_PrivateExtensionDeclaration, adb_NewTypeDeclaration, TypeDeclaration, adb_FullTypeDeclaration, NewTypeDeclaration, adb_FullDataTypeDeclaration, FullTypeDeclaration, adb_TypeDefinition, adb_IncompleteTypeDeclaration, adb_DiscriminantPart, adb_PrivateTypeDeclaration, adb_ProtectedTypeDeclaration, adb_ProtectedDefinition, adb_SubtypeIndication, adb_TaskItem, adb_EntryDeclaration, TaskItem, ProtectedOperationDeclaration, adb_DiscreteSubtypeDefinition, adb_FormalPart, adb_ProcedureSpecification, SubprogramSpecification, adb_FunctionSpecification, adb_ParameterAndResultProfile, adb_ExceptionChoice, adb_Name, adb_ProtectedElementDeclaration, adb_ProtectedOperationDeclaration, ProtectedElementDeclaration, adb_SubprogramDeclaration, BodyStub, adb_LabelisableStatement, adb_Statement, adb_SimpleStatement, Statement, adb_ExceptionHandler, adb_SequenceOfStatements, adb_Body, adb_ProperBody, Body, adb_Label, HandledSequenceOfStatements, AbortablePart, adb_Mode, adb_OptNullExclusion, adb_AnonymousAccessDefinition, adb_Expression, adb_CompoundStatement, adb_NullStatement, SimpleStatement, adb_GenericItem, adb_GenericFormalParameterDeclaration, adb_FormalObjectDeclaration, GenericFormalParameterDeclaration, adb_DefiningIdentifierList, adb_FormalSubprogramDeclaration, adb_SubprogramDefault, adb_FormalTypeDeclaration, adb_FormalTypeDefinition, adb_FormalPrivateTypeDefinition, FormalTypeDefinition, adb_FormalDerivedTypeDefinition, adb_FormalPackageAssociation, adb_GenericAssociation, adb_ExceptionDeclaration, adb_ObjectDeclaration, adb_DataInstanceDeclaration, adb_FormalPackageDeclaration, adb_FormalPackageActualPart, adb_ArrayTypeDefinition, adb_SingleProtectedDeclaration, ObjectDeclaration, adb_NumberDeclaration, adb_AssignmentStatement, adb_PragmaArgumentAssociation, adb_SubtypeDeclaration, adb_CaseStatement, adb_CaseStatementAlternative, adb_DiscreteChoiceList, adb_LoopStatement, adb_IfStatement, CompoundStatement, adb_IterationScheme, adb_BlockStatement, adb_ExitStatement, adb_GotoStatement, adb_LoopParameterSpecification, adb_ReturnSubtypeIndication, adb_PackageBody, adb_ProcedureOrEntryCallStatement, TriggeringStatement, adb_SimpleReturnStatement, adb_ExtendedReturnStatement, adb_ProtectedOperationItem, adb_AcceptStatement, adb_EntryIndex, adb_TaskBody, adb_ProtectedBody, adb_EntryIndexSpecification, adb_EntryBody, adb_EntryBodyFormalPart, adb_SelectiveAccept, adb_EntryBarrier, SelectStatement, adb_Guard, adb_SelectAlternative, adb_GuardedAlternative, adb_RequeueStatement, adb_DelayStatement, adb_SelectStatement, adb_DelayAlternative, adb_TimedEntryCall, adb_EntryCallAlternative, adb_AcceptAlternative, SelectAlternative, adb_AsynchronousSelect, adb_TriggeringAlternative, adb_AbortablePart, adb_TriggeringStatement, adb_ConditionalEntryCall, adb_RaiseStatement, adb_AbortStatement, adb_TaskNames, AbortStatement, adb_BodyStub, adb_PackageBodyStub, adb_TaskBodyStub, adb_ProtectedBodyStub, adb_SeparateSubunit, adb_NotNullAccessDefinition, adb_ExplicitGenericActualParameter, adb_UnknownDiscriminantPart, DiscriminantPart, adb_DiscriminantSpecification, adb_RecordExtensionPart, adb_RecordDefinition, adb_AccessTypeDefinition, adb_InterfaceTypeDefinition, adb_AccessSpecification, TypeDefinition, adb_AccessToSubprogramDefinition, AccessSpecification, NotNullAccessDefinition, adb_DerivedTypeDefinition, adb_AccessToDataDefinition, ReturnSubtypeIndication, adb_ArrayIndexes, adb_ComponentDefinition, adb_UnconstrainedIndexes, ArrayIndexes, adb_ConstrainedIndexes, adb_AccessToDataInstance, adb_ParameterSpecification, adb_ModularTypeDefinition, adb_IntegerTypeDefinition, adb_SignedIntegerTypeDefinition, IntegerTypeDefinition, adb_SimpleExpression, adb_OptVariantPart, adb_VariantPart, adb_EnumerationTypeDefinition, adb_RecordTypeDefinition, adb_ComponentList, adb_ComponentItem, adb_ComponentClause, adb_ComponentDeclaration, ComponentItem, adb_AspectClause, adb_ModClause, adb_Variant, ExplicitGenericActualParameter, DiscreteChoice, adb_DiscreteChoice, adb_RealTypeDefinition, adb_RealRangeSpecification, adb_FloatingPointDefinition, RealTypeDefinition, adb_FixedPointDefinition, EntryIndex, adb_Term, AncestorPart, ParameterEffectiveValue, adb_Relation, adb_Membership, adb_Interval, adb_Factor, adb_Primary, adb_NumericLiteral, Primary, adb_Null, adb_StringLiteral, adb_EObject, adb_QualifiedName, adb_Qualifier, adb_ParenthesizedExpression, adb_Allocator, DiscreteSubtypeDefinition, DiscreteRange, adb_OptConstraint, adb_IndexConstraint, adb_DiscreteRange, adb_ScalarConstraint, adb_DigitsConstraint, ScalarConstraint, adb_RangeConstraint, adb_DeltaConstraint, adb_CompositeConstraint, adb_DiscriminantConstraint, CompositeConstraint, adb_DiscriminantAssociation, adb_RecordAggregate, Aggregate, adb_RecordComponentAssociationList, RecordAggregate, adb_DiscriminantSelectors, adb_ComponentChoiceList, adb_Aggregate, ParenthesizedExpression, Qualifier, adb_ArrayAggregate, adb_PositionalArrayAggregate, ArrayAggregate, adb_RecordComponentAssociation, adb_InitializedComponents, RecordComponentAssociation, adb_UninitializedComponents, adb_ExtensionAggregate, adb_AncestorPart, adb_PrimaryName, adb_ParameterAssociation, adb_NamedArrayAggregate, adb_ArrayComponentAssociation, Interval, adb_EntityRange, Range, adb_AttributeDesignator, adb_ParameterEffectiveValue, adb_Range, RangeConstraint, adb_ExplicitRange},
    associations={importURI9, compilationUnits0, importedNamespace10, contextClause1, unit3, pragmas5, contextItems7, packageSpecification14, genericItems15, libraryUnitSpecification12, publicBasicDeclarativeItems21, privateBasicDeclarativeItems23, subprogramSpecification26, librarySpecification16, overriding18, genericActualPart19, interfaceList31, taskDefinition33, endid36, declarativeItems27, handledSequenceOfStatements28, knownDiscriminantPart30, discriminantPart42, discriminantPart44, knownDiscriminantPart38, typeDefinition40, discriminantPart41, formalPart55, interfaceList57, protectedDefinition59, ancestorSubtypeIndication46, interfaceList48, overriding51, discreteSubtypeDefinition53, formalPart68, parameterAndResultProfile70, name71, protectedOperationDeclaration61, subprogramSpecification63, overridingIndicator65, exceptionHandler76, statements79, labels81, statement83, exceptionChoice72, sequenceOfStatements74, mode88, optNullExclusion90, subtypeMark92, anonymousAccessDefinition95, defaultExpression97, genericItems85, idList87, subtypeMark103, interfaceList105, subprogramSpecification108, subprogramDefault110, discriminantPart99, formalTypeDefinition101, formalPackageAssociation116, genericAssociation118, idList120, renamedName122, formalPackageActualPart112, genericActualPart113, anonymousAccessDefinition136, arrayTypeDefinition139, interfaceList141, protectedDefinition143, definingIdentifierList125, subtypeIndication127, expression130, objectName133, idList153, staticExpression155, variableName158, initialValue160, pragmaArgumentAssociation146, effectiveArgument148, subtypeIndication151, caseValue177, caseStatementAlternatives179, discreteChoiceList181, sequenceOfStatements183, ifCondition163, thenStatements165, elsifConditions168, elsifStatements171, elseStatements174, discreteSubtypeDefinition195, name198, condition200, iterationScheme186, sequenceOfStatements187, condition190, iterationSpecification193, returnSubtype207, expression208, handledSequenceOfStatements211, name214, endName215, callee203, returnValue205, protectedOperationItem225, entryName226, entryIndex228, formalPart230, handledSequenceOfStatements233, taskItems218, name220, endId222, entryIndexSpecification242, formalPart244, condition247, name236, entryBodyFormalPart238, entryBarrier240, selectguard257, selectAlternative258, guardedAlternatives260, elseStatements262, discreteSubtypeDefinition250, name253, delay255, acceptStatement277, delayStatement279, entryCallAlternative281, guard265, alternative268, condition271, sequenceOfStatements274, triggeringAlternative296, abortablePart297, triggeringStatement299, sequenceOfStatements301, delayAlternative282, call285, sequenceOfStatements288, entryCallAlternative291, elseSequenceOfStatements293, properBody306, exceptionName307, withExpression309, genericAssociation312, taskNames304, definingIdentifiers319, optNullExclusion322, accessDefinition325, subtypeMark327, defaultValue330, expplicitGenericActualParam315, discriminantsSpecification317, parameterAndResultProfile353, subtypeIndication338, interfaceList340, recordExtentionPart343, recordDefinition345, interfaceSubtypeMark333, optNullExclusion347, accessDefinition349, interfaceList336, formalPart351, anonymousAccessDefinition369, subtypeIndication356, arrayIndexes358, componentDefinition360, subtypeMark362, constrainedIndex364, subtypeIndication366, parameterSpecifications392, definingIdentifiers394, optNullExclusion372, accessDef375, name378, formalPart380, opt_nullExclusion383, subtypeMark386, anonymousAccessDefinition389, last413, mode397, optNullExclusion400, subtypeMark403, anonymousAccessDefinition406, defaultExpression409, first412, optVariantPart424, variantPart426, staticExpression416, recordDefinition418, componentList420, componentItems422, mod438, definingIdentifiers428, componentDefinition430, defaultExpression433, expression436, componentList459, componentClause440, mod442, position445, firstBit448, lastBit451, variants454, discreteChoiceList456, discreteChoiceList462, digits464, realRangeSpecification466, lowerBound468, upperBound471, delta474, terms488, relations476, simpleExpression478, subSimpleExpression481, membership484, interval486, name497, factors490, primary492, exponent494, optConstraint511, qualifier499, typeName501, qualifier503, opt_nullExclusion506, opt_constraint509, digits513, rangeConstraint515, delta517, rangeConstraint519, discriminantAssociation522, discreteRange523, discriminantSelectors524, actualParameter526, recordComponentAssociation529, componentChoiceList530, value532, ancestorPart534, recordComponentAssociationList535, primaryName550, initialValues538, othersValue540, arrayComponentAssociation543, discreteChoiceList544, expression547, name566, parameterAssociation552, primaryName555, name557, attributeDesignator560, parameterEffectiveValue562, staticExpression564, index568, first571, last573},
    generalizations={gen_adb_UseClause_ContextItem, gen_adb_UseClause_BasicDeclarativeItem, gen_adb_UseClause_GenericItem, gen_adb_UsePackageClause_UseClause, gen_adb_WithClause_ContextItem, gen_adb_PackageDefinition_PackageDeclaration, gen_adb_PackageDefinition_LibrarySpecification, gen_adb_Renaming_PackageDeclaration, gen_adb_GenericDeclaration_LibraryUnitSpecification, gen_adb_GenericDeclaration_BasicDeclaration, gen_adb_UseTypeClause_UseClause, gen_adb_LibraryUnitDeclaration_Unit, gen_adb_PackageDeclaration_LibraryUnitSpecification, gen_adb_PackageDeclaration_BasicDeclaration, gen_adb_SubprogramBody_Unit, gen_adb_SubprogramBody_DeclarativeBlock, gen_adb_SubprogramBody_ProperBody, gen_adb_SubprogramBody_ProtectedOperationItem, gen_adb_GenericInstantiation_LibraryUnitSpecification, gen_adb_GenericInstantiation_BasicDeclaration, gen_adb_TypeDeclaration_BasicDeclaration, gen_adb_BasicDeclarativeItem_DeclarativeItem, gen_adb_BasicDeclaration_BasicDeclarativeItem, gen_adb_TaskDeclaration_BasicDeclaration, gen_adb_PrivateTypeDeclaration_NewTypeDeclaration, gen_adb_PrivateExtensionDeclaration_NewTypeDeclaration, gen_adb_NewTypeDeclaration_TypeDeclaration, gen_adb_FullTypeDeclaration_NewTypeDeclaration, gen_adb_FullDataTypeDeclaration_FullTypeDeclaration, gen_adb_IncompleteTypeDeclaration_NewTypeDeclaration, gen_adb_ProtectedTypeDeclaration_FullTypeDeclaration, gen_adb_EntryDeclaration_TaskItem, gen_adb_EntryDeclaration_ProtectedOperationDeclaration, gen_adb_ProcedureSpecification_SubprogramSpecification, gen_adb_FunctionSpecification_SubprogramSpecification, gen_adb_ProtectedOperationDeclaration_ProtectedElementDeclaration, gen_adb_SubprogramDeclaration_BasicDeclaration, gen_adb_SubprogramDeclaration_ProtectedOperationDeclaration, gen_adb_SubprogramDeclaration_ProtectedOperationItem, gen_adb_SubprogramSpecification_LibraryUnitSpecification, gen_adb_SubprogramSpecification_LibrarySpecification, gen_adb_SubprogramSpecification_BodyStub, gen_adb_Body_DeclarativeItem, gen_adb_ProperBody_Body, gen_adb_SequenceOfStatements_HandledSequenceOfStatements, gen_adb_SequenceOfStatements_AbortablePart, gen_adb_SimpleStatement_Statement, gen_adb_CompoundStatement_Statement, gen_adb_NullStatement_SimpleStatement, gen_adb_GenericFormalParameterDeclaration_GenericItem, gen_adb_FormalObjectDeclaration_GenericFormalParameterDeclaration, gen_adb_FormalSubprogramDeclaration_GenericFormalParameterDeclaration, gen_adb_FormalTypeDeclaration_GenericFormalParameterDeclaration, gen_adb_FormalPrivateTypeDefinition_FormalTypeDefinition, gen_adb_FormalDerivedTypeDefinition_FormalTypeDefinition, gen_adb_ExceptionDeclaration_BasicDeclaration, gen_adb_ObjectDeclaration_BasicDeclaration, gen_adb_FormalPackageDeclaration_GenericFormalParameterDeclaration, gen_adb_SingleProtectedDeclaration_ObjectDeclaration, gen_adb_Pragma_ContextItem, gen_adb_Pragma_BasicDeclarativeItem, gen_adb_Pragma_Statement, gen_adb_DataInstanceDeclaration_ObjectDeclaration, gen_adb_NumberDeclaration_BasicDeclaration, gen_adb_AssignmentStatement_SimpleStatement, gen_adb_SubtypeDeclaration_TypeDeclaration, gen_adb_CaseStatement_CompoundStatement, gen_adb_LoopStatement_CompoundStatement, gen_adb_IfStatement_CompoundStatement, gen_adb_BlockStatement_DeclarativeBlock, gen_adb_BlockStatement_CompoundStatement, gen_adb_ExitStatement_SimpleStatement, gen_adb_GotoStatement_SimpleStatement, gen_adb_PackageBody_Unit, gen_adb_PackageBody_DeclarativeBlock, gen_adb_PackageBody_ProperBody, gen_adb_ProcedureOrEntryCallStatement_SimpleStatement, gen_adb_ProcedureOrEntryCallStatement_TriggeringStatement, gen_adb_SimpleReturnStatement_SimpleStatement, gen_adb_ExtendedReturnStatement_CompoundStatement, gen_adb_AcceptStatement_CompoundStatement, gen_adb_TaskBody_DeclarativeBlock, gen_adb_TaskBody_ProperBody, gen_adb_ProtectedBody_ProperBody, gen_adb_EntryBody_DeclarativeBlock, gen_adb_EntryBody_ProtectedOperationItem, gen_adb_SelectiveAccept_SelectStatement, gen_adb_RequeueStatement_SimpleStatement, gen_adb_DelayStatement_SimpleStatement, gen_adb_DelayStatement_TriggeringStatement, gen_adb_SelectStatement_CompoundStatement, gen_adb_DelayAlternative_SelectAlternative, gen_adb_TimedEntryCall_SelectStatement, gen_adb_AcceptAlternative_SelectAlternative, gen_adb_AsynchronousSelect_SelectStatement, gen_adb_ConditionalEntryCall_SelectStatement, gen_adb_RaiseStatement_SimpleStatement, gen_adb_AbortStatement_SimpleStatement, gen_adb_TaskNames_AbortStatement, gen_adb_BodyStub_Body, gen_adb_PackageBodyStub_BodyStub, gen_adb_TaskBodyStub_BodyStub, gen_adb_ProtectedBodyStub_BodyStub, gen_adb_SeparateSubunit_Unit, gen_adb_UnknownDiscriminantPart_DiscriminantPart, gen_adb_KnownDiscriminantPart_DiscriminantPart, gen_adb_AccessTypeDefinition_FormalTypeDefinition, gen_adb_AccessTypeDefinition_TypeDefinition, gen_adb_InterfaceTypeDefinition_FormalTypeDefinition, gen_adb_InterfaceTypeDefinition_TypeDefinition, gen_adb_AccessToSubprogramDefinition_AccessSpecification, gen_adb_AccessToSubprogramDefinition_NotNullAccessDefinition, gen_adb_DerivedTypeDefinition_TypeDefinition, gen_adb_AccessToDataDefinition_AccessSpecification, gen_adb_AnonymousAccessDefinition_ReturnSubtypeIndication, gen_adb_ArrayTypeDefinition_FormalTypeDefinition, gen_adb_ArrayTypeDefinition_TypeDefinition, gen_adb_UnconstrainedIndexes_ArrayIndexes, gen_adb_ConstrainedIndexes_ArrayIndexes, gen_adb_AccessToDataInstance_NotNullAccessDefinition, gen_adb_ModularTypeDefinition_IntegerTypeDefinition, gen_adb_IntegerTypeDefinition_TypeDefinition, gen_adb_SignedIntegerTypeDefinition_IntegerTypeDefinition, gen_adb_EnumerationTypeDefinition_TypeDefinition, gen_adb_RecordTypeDefinition_TypeDefinition, gen_adb_ComponentDeclaration_ProtectedElementDeclaration, gen_adb_ComponentDeclaration_ComponentItem, gen_adb_AspectClause_BasicDeclarativeItem, gen_adb_AspectClause_TaskItem, gen_adb_AspectClause_ProtectedOperationDeclaration, gen_adb_AspectClause_ProtectedOperationItem, gen_adb_AspectClause_ComponentItem, gen_adb_Expression_ExplicitGenericActualParameter, gen_adb_Expression_DiscreteChoice, gen_adb_RealTypeDefinition_TypeDefinition, gen_adb_FloatingPointDefinition_RealTypeDefinition, gen_adb_FixedPointDefinition_RealTypeDefinition, gen_adb_Expression_EntryIndex, gen_adb_Expression_AncestorPart, gen_adb_Expression_ParameterEffectiveValue, gen_adb_NumericLiteral_Primary, gen_adb_Null_Primary, gen_adb_StringLiteral_Primary, gen_adb_QualifiedName_Primary, gen_adb_ParenthesizedExpression_Primary, gen_adb_Allocator_Primary, gen_adb_SubtypeIndication_ReturnSubtypeIndication, gen_adb_SubtypeIndication_DiscreteSubtypeDefinition, gen_adb_SubtypeIndication_DiscreteRange, gen_adb_SubtypeIndication_DiscreteChoice, gen_adb_IndexConstraint_CompositeConstraint, gen_adb_DigitsConstraint_ScalarConstraint, gen_adb_DeltaConstraint_ScalarConstraint, gen_adb_RangeConstraint_ScalarConstraint, gen_adb_DiscriminantConstraint_CompositeConstraint, gen_adb_RecordAggregate_Aggregate, gen_adb_RecordComponentAssociationList_RecordAggregate, gen_adb_DiscreteRange_DiscreteSubtypeDefinition, gen_adb_Aggregate_ParenthesizedExpression, gen_adb_Aggregate_Qualifier, gen_adb_ArrayAggregate_Aggregate, gen_adb_PositionalArrayAggregate_ArrayAggregate, gen_adb_InitializedComponents_RecordComponentAssociation, gen_adb_UninitializedComponents_RecordComponentAssociation, gen_adb_ExtensionAggregate_Aggregate, gen_adb_NamedArrayAggregate_ArrayAggregate, gen_adb_Name_Interval, gen_adb_EntityRange_Range, gen_adb_Range_Interval, gen_adb_Range_RangeConstraint, gen_adb_Range_DiscreteRange, gen_adb_Range_DiscreteChoice, gen_adb_Range_ParameterEffectiveValue, gen_adb_ExplicitRange_Range},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)