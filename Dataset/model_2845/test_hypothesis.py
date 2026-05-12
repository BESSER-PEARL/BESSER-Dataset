import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RecordComponentAssociation,
    adb_UninitializedComponents,
    adb_InitializedComponents,
    adb_ParameterAssociation,
    adb_RecordComponentAssociation,
    RecordAggregate,
    adb_RecordComponentAssociationList,
    Aggregate,
    adb_ExtensionAggregate,
    adb_RecordAggregate,
    Qualifier,
    ParenthesizedExpression,
    adb_Aggregate,
    adb_ComponentChoiceList,
    adb_DiscriminantSelectors,
    adb_DiscriminantAssociation,
    CompositeConstraint,
    adb_IndexConstraint,
    adb_DiscriminantConstraint,
    adb_CompositeConstraint,
    adb_OptConstraint,
    DiscreteRange,
    DiscreteSubtypeDefinition,
    adb_DiscreteRange,
    adb_Qualifier,
    Primary,
    adb_QualifiedName,
    adb_StringLiteral,
    adb_Allocator,
    adb_Null,
    adb_ParenthesizedExpression,
    adb_NumericLiteral,
    Range,
    adb_ExplicitRange,
    adb_EntityRange,
    RangeConstraint,
    adb_ParameterEffectiveValue,
    adb_AttributeDesignator,
    adb_PrimaryName,
    Interval,
    adb_ArrayComponentAssociation,
    ArrayAggregate,
    adb_NamedArrayAggregate,
    adb_PositionalArrayAggregate,
    adb_ArrayAggregate,
    adb_AncestorPart,
    ScalarConstraint,
    adb_RangeConstraint,
    adb_DeltaConstraint,
    adb_DigitsConstraint,
    adb_ScalarConstraint,
    adb_EObject,
    adb_Factor,
    adb_Term,
    adb_Interval,
    adb_Membership,
    adb_Relation,
    ParameterEffectiveValue,
    AncestorPart,
    DiscreteChoice,
    adb_Range,
    ExplicitGenericActualParameter,
    EntryIndex,
    adb_Primary,
    adb_RealRangeSpecification,
    adb_DiscreteChoice,
    adb_Variant,
    adb_ComponentClause,
    adb_ModClause,
    RealTypeDefinition,
    adb_FixedPointDefinition,
    adb_FloatingPointDefinition,
    ComponentItem,
    adb_VariantPart,
    adb_OptVariantPart,
    adb_ComponentItem,
    adb_ComponentList,
    adb_SimpleExpression,
    IntegerTypeDefinition,
    adb_ModularTypeDefinition,
    adb_SignedIntegerTypeDefinition,
    adb_ParameterSpecification,
    ReturnSubtypeIndication,
    ArrayIndexes,
    adb_ConstrainedIndexes,
    adb_UnconstrainedIndexes,
    adb_ComponentDefinition,
    adb_ArrayIndexes,
    NotNullAccessDefinition,
    AccessSpecification,
    adb_AccessToDataDefinition,
    adb_AccessToSubprogramDefinition,
    adb_AccessSpecification,
    adb_AccessToDataInstance,
    TypeDefinition,
    adb_IntegerTypeDefinition,
    adb_RealTypeDefinition,
    adb_RecordTypeDefinition,
    adb_DerivedTypeDefinition,
    adb_EnumerationTypeDefinition,
    adb_NotNullAccessDefinition,
    adb_DiscriminantSpecification,
    adb_RecordDefinition,
    adb_RecordExtensionPart,
    DiscriminantPart,
    adb_UnknownDiscriminantPart,
    adb_ExplicitGenericActualParameter,
    AbortStatement,
    adb_TaskNames,
    adb_EntryCallAlternative,
    SelectAlternative,
    adb_DelayAlternative,
    adb_AcceptAlternative,
    adb_GuardedAlternative,
    adb_SelectAlternative,
    adb_Guard,
    SelectStatement,
    adb_ConditionalEntryCall,
    adb_TimedEntryCall,
    adb_SelectiveAccept,
    adb_TriggeringStatement,
    adb_AbortablePart,
    adb_TriggeringAlternative,
    adb_AsynchronousSelect,
    adb_EntryIndexSpecification,
    adb_EntryBarrier,
    adb_EntryBodyFormalPart,
    adb_EntryIndex,
    adb_ProtectedOperationItem,
    adb_ReturnSubtypeIndication,
    TriggeringStatement,
    adb_LoopParameterSpecification,
    adb_IterationScheme,
    CompoundStatement,
    adb_ExtendedReturnStatement,
    adb_AcceptStatement,
    adb_SelectStatement,
    adb_LoopStatement,
    adb_IfStatement,
    adb_PragmaArgumentAssociation,
    adb_DiscreteChoiceList,
    adb_CaseStatementAlternative,
    adb_CaseStatement,
    ObjectDeclaration,
    adb_DataInstanceDeclaration,
    adb_GenericAssociation,
    adb_FormalPackageAssociation,
    adb_FormalPackageActualPart,
    adb_SubprogramDefault,
    adb_Expression,
    adb_AnonymousAccessDefinition,
    adb_OptNullExclusion,
    adb_SingleProtectedDeclaration,
    adb_Mode,
    adb_DefiningIdentifierList,
    FormalTypeDefinition,
    adb_InterfaceTypeDefinition,
    adb_ArrayTypeDefinition,
    adb_AccessTypeDefinition,
    adb_FormalDerivedTypeDefinition,
    GenericFormalParameterDeclaration,
    adb_FormalTypeDeclaration,
    adb_FormalPackageDeclaration,
    adb_FormalSubprogramDeclaration,
    adb_FormalObjectDeclaration,
    adb_FormalPrivateTypeDefinition,
    adb_FormalTypeDefinition,
    adb_ExceptionHandler,
    adb_GenericItem,
    SimpleStatement,
    adb_SimpleReturnStatement,
    adb_GotoStatement,
    adb_AbortStatement,
    adb_ExitStatement,
    adb_AssignmentStatement,
    adb_DelayStatement,
    adb_ProcedureOrEntryCallStatement,
    adb_RaiseStatement,
    adb_RequeueStatement,
    adb_NullStatement,
    Statement,
    adb_CompoundStatement,
    adb_SimpleStatement,
    adb_Statement,
    adb_LabelisableStatement,
    AbortablePart,
    HandledSequenceOfStatements,
    adb_SequenceOfStatements,
    adb_Label,
    Body,
    adb_ProperBody,
    adb_BodyStub,
    ProtectedElementDeclaration,
    adb_ComponentDeclaration,
    adb_ProtectedOperationDeclaration,
    adb_ProtectedElementDeclaration,
    adb_ProtectedDefinition,
    adb_FormalPart,
    adb_DiscreteSubtypeDefinition,
    adb_Name,
    adb_ExceptionChoice,
    adb_ParameterAndResultProfile,
    SubprogramSpecification,
    adb_FunctionSpecification,
    adb_ProcedureSpecification,
    BodyStub,
    adb_TaskBodyStub,
    adb_PackageBodyStub,
    adb_ProtectedBodyStub,
    NewTypeDeclaration,
    adb_FullTypeDeclaration,
    TypeDeclaration,
    adb_SubtypeDeclaration,
    adb_NewTypeDeclaration,
    adb_TaskDefinition,
    adb_InterfaceList,
    adb_KnownDiscriminantPart,
    DeclarativeItem,
    adb_Body,
    ProtectedOperationDeclaration,
    TaskItem,
    adb_EntryDeclaration,
    adb_TaskItem,
    adb_SubtypeIndication,
    adb_PrivateExtensionDeclaration,
    adb_PrivateTypeDeclaration,
    adb_DiscriminantPart,
    adb_IncompleteTypeDeclaration,
    adb_TypeDefinition,
    FullTypeDeclaration,
    adb_ProtectedTypeDeclaration,
    adb_FullDataTypeDeclaration,
    adb_PackageSpecification,
    LibrarySpecification,
    PackageDeclaration,
    adb_Renaming,
    adb_PackageDefinition,
    BasicDeclaration,
    adb_ExceptionDeclaration,
    adb_NumberDeclaration,
    adb_ObjectDeclaration,
    adb_TaskDeclaration,
    adb_TypeDeclaration,
    LibraryUnitSpecification,
    adb_PackageDeclaration,
    adb_LibraryUnitSpecification,
    Unit,
    adb_SeparateSubunit,
    adb_HandledSequenceOfStatements,
    adb_DeclarativeItem,
    adb_DeclarativeBlock,
    adb_SubprogramSpecification,
    ProtectedOperationItem,
    adb_SubprogramDeclaration,
    ProperBody,
    adb_ProtectedBody,
    DeclarativeBlock,
    adb_TaskBody,
    adb_EntryBody,
    adb_PackageBody,
    adb_BlockStatement,
    adb_SubprogramBody,
    adb_BasicDeclarativeItem,
    adb_GenericActualPart,
    adb_OverridingIndicator,
    adb_GenericInstantiation,
    adb_LibrarySpecification,
    adb_GenericItems,
    adb_GenericDeclaration,
    UseClause,
    adb_UseTypeClause,
    adb_UsePackageClause,
    GenericItem,
    adb_GenericFormalParameterDeclaration,
    BasicDeclarativeItem,
    adb_BasicDeclaration,
    adb_AspectClause,
    adb_LibraryUnitDeclaration,
    ContextItem,
    adb_UseClause,
    adb_WithClause,
    adb_ContextItem,
    adb_Pragma,
    adb_Unit,
    adb_ContextClause,
    adb_CompilationUnit,
    adb_Compilation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_recordcomponentassociation_is_not_abstract():
    assert not inspect.isabstract(RecordComponentAssociation)


def test_recordcomponentassociation_constructor_exists():
    assert callable(RecordComponentAssociation.__init__)


def test_recordcomponentassociation_constructor_args():
    sig = inspect.signature(RecordComponentAssociation.__init__)
    params = list(sig.parameters.keys())



def test_adb_uninitializedcomponents_is_not_abstract():
    assert not inspect.isabstract(adb_UninitializedComponents)


def test_adb_uninitializedcomponents_constructor_exists():
    assert callable(adb_UninitializedComponents.__init__)


def test_adb_uninitializedcomponents_constructor_args():
    sig = inspect.signature(adb_UninitializedComponents.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb_uninitializedcomponents_has_box():
    assert hasattr(adb_UninitializedComponents, "box")
    descriptor = None
    for klass in adb_UninitializedComponents.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb_initializedcomponents_is_not_abstract():
    assert not inspect.isabstract(adb_InitializedComponents)


def test_adb_initializedcomponents_constructor_exists():
    assert callable(adb_InitializedComponents.__init__)


def test_adb_initializedcomponents_constructor_args():
    sig = inspect.signature(adb_InitializedComponents.__init__)
    params = list(sig.parameters.keys())



def test_adb_parameterassociation_is_not_abstract():
    assert not inspect.isabstract(adb_ParameterAssociation)


def test_adb_parameterassociation_constructor_exists():
    assert callable(adb_ParameterAssociation.__init__)


def test_adb_parameterassociation_constructor_args():
    sig = inspect.signature(adb_ParameterAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "selectorName" in params, "Missing parameter 'selectorName'"

def test_adb_parameterassociation_has_selectorName():
    assert hasattr(adb_ParameterAssociation, "selectorName")
    descriptor = None
    for klass in adb_ParameterAssociation.__mro__:
        if "selectorName" in klass.__dict__:
            descriptor = klass.__dict__["selectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb_recordcomponentassociation_is_not_abstract():
    assert not inspect.isabstract(adb_RecordComponentAssociation)


def test_adb_recordcomponentassociation_constructor_exists():
    assert callable(adb_RecordComponentAssociation.__init__)


def test_adb_recordcomponentassociation_constructor_args():
    sig = inspect.signature(adb_RecordComponentAssociation.__init__)
    params = list(sig.parameters.keys())



def test_recordaggregate_is_not_abstract():
    assert not inspect.isabstract(RecordAggregate)


def test_recordaggregate_constructor_exists():
    assert callable(RecordAggregate.__init__)


def test_recordaggregate_constructor_args():
    sig = inspect.signature(RecordAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_recordcomponentassociationlist_is_not_abstract():
    assert not inspect.isabstract(adb_RecordComponentAssociationList)


def test_adb_recordcomponentassociationlist_constructor_exists():
    assert callable(adb_RecordComponentAssociationList.__init__)


def test_adb_recordcomponentassociationlist_constructor_args():
    sig = inspect.signature(adb_RecordComponentAssociationList.__init__)
    params = list(sig.parameters.keys())
    assert "nullRecord" in params, "Missing parameter 'nullRecord'"

def test_adb_recordcomponentassociationlist_has_nullRecord():
    assert hasattr(adb_RecordComponentAssociationList, "nullRecord")
    descriptor = None
    for klass in adb_RecordComponentAssociationList.__mro__:
        if "nullRecord" in klass.__dict__:
            descriptor = klass.__dict__["nullRecord"]
            break
    assert isinstance(descriptor, property)



def test_aggregate_is_not_abstract():
    assert not inspect.isabstract(Aggregate)


def test_aggregate_constructor_exists():
    assert callable(Aggregate.__init__)


def test_aggregate_constructor_args():
    sig = inspect.signature(Aggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_extensionaggregate_is_not_abstract():
    assert not inspect.isabstract(adb_ExtensionAggregate)


def test_adb_extensionaggregate_constructor_exists():
    assert callable(adb_ExtensionAggregate.__init__)


def test_adb_extensionaggregate_constructor_args():
    sig = inspect.signature(adb_ExtensionAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_recordaggregate_is_not_abstract():
    assert not inspect.isabstract(adb_RecordAggregate)


def test_adb_recordaggregate_constructor_exists():
    assert callable(adb_RecordAggregate.__init__)


def test_adb_recordaggregate_constructor_args():
    sig = inspect.signature(adb_RecordAggregate.__init__)
    params = list(sig.parameters.keys())



def test_qualifier_is_not_abstract():
    assert not inspect.isabstract(Qualifier)


def test_qualifier_constructor_exists():
    assert callable(Qualifier.__init__)


def test_qualifier_constructor_args():
    sig = inspect.signature(Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(ParenthesizedExpression)


def test_parenthesizedexpression_constructor_exists():
    assert callable(ParenthesizedExpression.__init__)


def test_parenthesizedexpression_constructor_args():
    sig = inspect.signature(ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_adb_aggregate_is_not_abstract():
    assert not inspect.isabstract(adb_Aggregate)


def test_adb_aggregate_constructor_exists():
    assert callable(adb_Aggregate.__init__)


def test_adb_aggregate_constructor_args():
    sig = inspect.signature(adb_Aggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentchoicelist_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentChoiceList)


def test_adb_componentchoicelist_constructor_exists():
    assert callable(adb_ComponentChoiceList.__init__)


def test_adb_componentchoicelist_constructor_args():
    sig = inspect.signature(adb_ComponentChoiceList.__init__)
    params = list(sig.parameters.keys())
    assert "others" in params, "Missing parameter 'others'"
    assert "componentSelectorName" in params, "Missing parameter 'componentSelectorName'"

def test_adb_componentchoicelist_has_others():
    assert hasattr(adb_ComponentChoiceList, "others")
    descriptor = None
    for klass in adb_ComponentChoiceList.__mro__:
        if "others" in klass.__dict__:
            descriptor = klass.__dict__["others"]
            break
    assert isinstance(descriptor, property)

def test_adb_componentchoicelist_has_componentSelectorName():
    assert hasattr(adb_ComponentChoiceList, "componentSelectorName")
    descriptor = None
    for klass in adb_ComponentChoiceList.__mro__:
        if "componentSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["componentSelectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb_discriminantselectors_is_not_abstract():
    assert not inspect.isabstract(adb_DiscriminantSelectors)


def test_adb_discriminantselectors_constructor_exists():
    assert callable(adb_DiscriminantSelectors.__init__)


def test_adb_discriminantselectors_constructor_args():
    sig = inspect.signature(adb_DiscriminantSelectors.__init__)
    params = list(sig.parameters.keys())
    assert "discriminantSelectorName" in params, "Missing parameter 'discriminantSelectorName'"

def test_adb_discriminantselectors_has_discriminantSelectorName():
    assert hasattr(adb_DiscriminantSelectors, "discriminantSelectorName")
    descriptor = None
    for klass in adb_DiscriminantSelectors.__mro__:
        if "discriminantSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["discriminantSelectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb_discriminantassociation_is_not_abstract():
    assert not inspect.isabstract(adb_DiscriminantAssociation)


def test_adb_discriminantassociation_constructor_exists():
    assert callable(adb_DiscriminantAssociation.__init__)


def test_adb_discriminantassociation_constructor_args():
    sig = inspect.signature(adb_DiscriminantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_compositeconstraint_is_not_abstract():
    assert not inspect.isabstract(CompositeConstraint)


def test_compositeconstraint_constructor_exists():
    assert callable(CompositeConstraint.__init__)


def test_compositeconstraint_constructor_args():
    sig = inspect.signature(CompositeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_indexconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_IndexConstraint)


def test_adb_indexconstraint_constructor_exists():
    assert callable(adb_IndexConstraint.__init__)


def test_adb_indexconstraint_constructor_args():
    sig = inspect.signature(adb_IndexConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_discriminantconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_DiscriminantConstraint)


def test_adb_discriminantconstraint_constructor_exists():
    assert callable(adb_DiscriminantConstraint.__init__)


def test_adb_discriminantconstraint_constructor_args():
    sig = inspect.signature(adb_DiscriminantConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_compositeconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_CompositeConstraint)


def test_adb_compositeconstraint_constructor_exists():
    assert callable(adb_CompositeConstraint.__init__)


def test_adb_compositeconstraint_constructor_args():
    sig = inspect.signature(adb_CompositeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_optconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_OptConstraint)


def test_adb_optconstraint_constructor_exists():
    assert callable(adb_OptConstraint.__init__)


def test_adb_optconstraint_constructor_args():
    sig = inspect.signature(adb_OptConstraint.__init__)
    params = list(sig.parameters.keys())



def test_discreterange_is_not_abstract():
    assert not inspect.isabstract(DiscreteRange)


def test_discreterange_constructor_exists():
    assert callable(DiscreteRange.__init__)


def test_discreterange_constructor_args():
    sig = inspect.signature(DiscreteRange.__init__)
    params = list(sig.parameters.keys())



def test_discretesubtypedefinition_is_not_abstract():
    assert not inspect.isabstract(DiscreteSubtypeDefinition)


def test_discretesubtypedefinition_constructor_exists():
    assert callable(DiscreteSubtypeDefinition.__init__)


def test_discretesubtypedefinition_constructor_args():
    sig = inspect.signature(DiscreteSubtypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_discreterange_is_not_abstract():
    assert not inspect.isabstract(adb_DiscreteRange)


def test_adb_discreterange_constructor_exists():
    assert callable(adb_DiscreteRange.__init__)


def test_adb_discreterange_constructor_args():
    sig = inspect.signature(adb_DiscreteRange.__init__)
    params = list(sig.parameters.keys())



def test_adb_qualifier_is_not_abstract():
    assert not inspect.isabstract(adb_Qualifier)


def test_adb_qualifier_constructor_exists():
    assert callable(adb_Qualifier.__init__)


def test_adb_qualifier_constructor_args():
    sig = inspect.signature(adb_Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_adb_qualifiedname_is_not_abstract():
    assert not inspect.isabstract(adb_QualifiedName)


def test_adb_qualifiedname_constructor_exists():
    assert callable(adb_QualifiedName.__init__)


def test_adb_qualifiedname_constructor_args():
    sig = inspect.signature(adb_QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_adb_stringliteral_is_not_abstract():
    assert not inspect.isabstract(adb_StringLiteral)


def test_adb_stringliteral_constructor_exists():
    assert callable(adb_StringLiteral.__init__)


def test_adb_stringliteral_constructor_args():
    sig = inspect.signature(adb_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb_stringliteral_has_value():
    assert hasattr(adb_StringLiteral, "value")
    descriptor = None
    for klass in adb_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adb_allocator_is_not_abstract():
    assert not inspect.isabstract(adb_Allocator)


def test_adb_allocator_constructor_exists():
    assert callable(adb_Allocator.__init__)


def test_adb_allocator_constructor_args():
    sig = inspect.signature(adb_Allocator.__init__)
    params = list(sig.parameters.keys())



def test_adb_null_is_not_abstract():
    assert not inspect.isabstract(adb_Null)


def test_adb_null_constructor_exists():
    assert callable(adb_Null.__init__)


def test_adb_null_constructor_args():
    sig = inspect.signature(adb_Null.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb_null_has_value():
    assert hasattr(adb_Null, "value")
    descriptor = None
    for klass in adb_Null.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adb_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(adb_ParenthesizedExpression)


def test_adb_parenthesizedexpression_constructor_exists():
    assert callable(adb_ParenthesizedExpression.__init__)


def test_adb_parenthesizedexpression_constructor_args():
    sig = inspect.signature(adb_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_adb_numericliteral_is_not_abstract():
    assert not inspect.isabstract(adb_NumericLiteral)


def test_adb_numericliteral_constructor_exists():
    assert callable(adb_NumericLiteral.__init__)


def test_adb_numericliteral_constructor_args():
    sig = inspect.signature(adb_NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb_numericliteral_has_value():
    assert hasattr(adb_NumericLiteral, "value")
    descriptor = None
    for klass in adb_NumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_range_is_not_abstract():
    assert not inspect.isabstract(Range)


def test_range_constructor_exists():
    assert callable(Range.__init__)


def test_range_constructor_args():
    sig = inspect.signature(Range.__init__)
    params = list(sig.parameters.keys())



def test_adb_explicitrange_is_not_abstract():
    assert not inspect.isabstract(adb_ExplicitRange)


def test_adb_explicitrange_constructor_exists():
    assert callable(adb_ExplicitRange.__init__)


def test_adb_explicitrange_constructor_args():
    sig = inspect.signature(adb_ExplicitRange.__init__)
    params = list(sig.parameters.keys())



def test_adb_entityrange_is_not_abstract():
    assert not inspect.isabstract(adb_EntityRange)


def test_adb_entityrange_constructor_exists():
    assert callable(adb_EntityRange.__init__)


def test_adb_entityrange_constructor_args():
    sig = inspect.signature(adb_EntityRange.__init__)
    params = list(sig.parameters.keys())



def test_rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(RangeConstraint)


def test_rangeconstraint_constructor_exists():
    assert callable(RangeConstraint.__init__)


def test_rangeconstraint_constructor_args():
    sig = inspect.signature(RangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_parametereffectivevalue_is_not_abstract():
    assert not inspect.isabstract(adb_ParameterEffectiveValue)


def test_adb_parametereffectivevalue_constructor_exists():
    assert callable(adb_ParameterEffectiveValue.__init__)


def test_adb_parametereffectivevalue_constructor_args():
    sig = inspect.signature(adb_ParameterEffectiveValue.__init__)
    params = list(sig.parameters.keys())



def test_adb_attributedesignator_is_not_abstract():
    assert not inspect.isabstract(adb_AttributeDesignator)


def test_adb_attributedesignator_constructor_exists():
    assert callable(adb_AttributeDesignator.__init__)


def test_adb_attributedesignator_constructor_args():
    sig = inspect.signature(adb_AttributeDesignator.__init__)
    params = list(sig.parameters.keys())



def test_adb_primaryname_is_not_abstract():
    assert not inspect.isabstract(adb_PrimaryName)


def test_adb_primaryname_constructor_exists():
    assert callable(adb_PrimaryName.__init__)


def test_adb_primaryname_constructor_args():
    sig = inspect.signature(adb_PrimaryName.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_adb_arraycomponentassociation_is_not_abstract():
    assert not inspect.isabstract(adb_ArrayComponentAssociation)


def test_adb_arraycomponentassociation_constructor_exists():
    assert callable(adb_ArrayComponentAssociation.__init__)


def test_adb_arraycomponentassociation_constructor_args():
    sig = inspect.signature(adb_ArrayComponentAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb_arraycomponentassociation_has_box():
    assert hasattr(adb_ArrayComponentAssociation, "box")
    descriptor = None
    for klass in adb_ArrayComponentAssociation.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_arrayaggregate_is_not_abstract():
    assert not inspect.isabstract(ArrayAggregate)


def test_arrayaggregate_constructor_exists():
    assert callable(ArrayAggregate.__init__)


def test_arrayaggregate_constructor_args():
    sig = inspect.signature(ArrayAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_namedarrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb_NamedArrayAggregate)


def test_adb_namedarrayaggregate_constructor_exists():
    assert callable(adb_NamedArrayAggregate.__init__)


def test_adb_namedarrayaggregate_constructor_args():
    sig = inspect.signature(adb_NamedArrayAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_positionalarrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb_PositionalArrayAggregate)


def test_adb_positionalarrayaggregate_constructor_exists():
    assert callable(adb_PositionalArrayAggregate.__init__)


def test_adb_positionalarrayaggregate_constructor_args():
    sig = inspect.signature(adb_PositionalArrayAggregate.__init__)
    params = list(sig.parameters.keys())
    assert "othersBox" in params, "Missing parameter 'othersBox'"

def test_adb_positionalarrayaggregate_has_othersBox():
    assert hasattr(adb_PositionalArrayAggregate, "othersBox")
    descriptor = None
    for klass in adb_PositionalArrayAggregate.__mro__:
        if "othersBox" in klass.__dict__:
            descriptor = klass.__dict__["othersBox"]
            break
    assert isinstance(descriptor, property)



def test_adb_arrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb_ArrayAggregate)


def test_adb_arrayaggregate_constructor_exists():
    assert callable(adb_ArrayAggregate.__init__)


def test_adb_arrayaggregate_constructor_args():
    sig = inspect.signature(adb_ArrayAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb_ancestorpart_is_not_abstract():
    assert not inspect.isabstract(adb_AncestorPart)


def test_adb_ancestorpart_constructor_exists():
    assert callable(adb_AncestorPart.__init__)


def test_adb_ancestorpart_constructor_args():
    sig = inspect.signature(adb_AncestorPart.__init__)
    params = list(sig.parameters.keys())



def test_scalarconstraint_is_not_abstract():
    assert not inspect.isabstract(ScalarConstraint)


def test_scalarconstraint_constructor_exists():
    assert callable(ScalarConstraint.__init__)


def test_scalarconstraint_constructor_args():
    sig = inspect.signature(ScalarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_RangeConstraint)


def test_adb_rangeconstraint_constructor_exists():
    assert callable(adb_RangeConstraint.__init__)


def test_adb_rangeconstraint_constructor_args():
    sig = inspect.signature(adb_RangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_deltaconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_DeltaConstraint)


def test_adb_deltaconstraint_constructor_exists():
    assert callable(adb_DeltaConstraint.__init__)


def test_adb_deltaconstraint_constructor_args():
    sig = inspect.signature(adb_DeltaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_digitsconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_DigitsConstraint)


def test_adb_digitsconstraint_constructor_exists():
    assert callable(adb_DigitsConstraint.__init__)


def test_adb_digitsconstraint_constructor_args():
    sig = inspect.signature(adb_DigitsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_scalarconstraint_is_not_abstract():
    assert not inspect.isabstract(adb_ScalarConstraint)


def test_adb_scalarconstraint_constructor_exists():
    assert callable(adb_ScalarConstraint.__init__)


def test_adb_scalarconstraint_constructor_args():
    sig = inspect.signature(adb_ScalarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb_eobject_is_not_abstract():
    assert not inspect.isabstract(adb_EObject)


def test_adb_eobject_constructor_exists():
    assert callable(adb_EObject.__init__)


def test_adb_eobject_constructor_args():
    sig = inspect.signature(adb_EObject.__init__)
    params = list(sig.parameters.keys())



def test_adb_factor_is_not_abstract():
    assert not inspect.isabstract(adb_Factor)


def test_adb_factor_constructor_exists():
    assert callable(adb_Factor.__init__)


def test_adb_factor_constructor_args():
    sig = inspect.signature(adb_Factor.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"
    assert "abs" in params, "Missing parameter 'abs'"

def test_adb_factor_has_not_():
    assert hasattr(adb_Factor, "not_")
    descriptor = None
    for klass in adb_Factor.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)

def test_adb_factor_has_abs():
    assert hasattr(adb_Factor, "abs")
    descriptor = None
    for klass in adb_Factor.__mro__:
        if "abs" in klass.__dict__:
            descriptor = klass.__dict__["abs"]
            break
    assert isinstance(descriptor, property)



def test_adb_term_is_not_abstract():
    assert not inspect.isabstract(adb_Term)


def test_adb_term_constructor_exists():
    assert callable(adb_Term.__init__)


def test_adb_term_constructor_args():
    sig = inspect.signature(adb_Term.__init__)
    params = list(sig.parameters.keys())
    assert "multiplyingOperators" in params, "Missing parameter 'multiplyingOperators'"

def test_adb_term_has_multiplyingOperators():
    assert hasattr(adb_Term, "multiplyingOperators")
    descriptor = None
    for klass in adb_Term.__mro__:
        if "multiplyingOperators" in klass.__dict__:
            descriptor = klass.__dict__["multiplyingOperators"]
            break
    assert isinstance(descriptor, property)



def test_adb_interval_is_not_abstract():
    assert not inspect.isabstract(adb_Interval)


def test_adb_interval_constructor_exists():
    assert callable(adb_Interval.__init__)


def test_adb_interval_constructor_args():
    sig = inspect.signature(adb_Interval.__init__)
    params = list(sig.parameters.keys())



def test_adb_membership_is_not_abstract():
    assert not inspect.isabstract(adb_Membership)


def test_adb_membership_constructor_exists():
    assert callable(adb_Membership.__init__)


def test_adb_membership_constructor_args():
    sig = inspect.signature(adb_Membership.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_adb_membership_has_not_():
    assert hasattr(adb_Membership, "not_")
    descriptor = None
    for klass in adb_Membership.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_adb_relation_is_not_abstract():
    assert not inspect.isabstract(adb_Relation)


def test_adb_relation_constructor_exists():
    assert callable(adb_Relation.__init__)


def test_adb_relation_constructor_args():
    sig = inspect.signature(adb_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_adb_relation_has_relationalOperator():
    assert hasattr(adb_Relation, "relationalOperator")
    descriptor = None
    for klass in adb_Relation.__mro__:
        if "relationalOperator" in klass.__dict__:
            descriptor = klass.__dict__["relationalOperator"]
            break
    assert isinstance(descriptor, property)



def test_parametereffectivevalue_is_not_abstract():
    assert not inspect.isabstract(ParameterEffectiveValue)


def test_parametereffectivevalue_constructor_exists():
    assert callable(ParameterEffectiveValue.__init__)


def test_parametereffectivevalue_constructor_args():
    sig = inspect.signature(ParameterEffectiveValue.__init__)
    params = list(sig.parameters.keys())



def test_ancestorpart_is_not_abstract():
    assert not inspect.isabstract(AncestorPart)


def test_ancestorpart_constructor_exists():
    assert callable(AncestorPart.__init__)


def test_ancestorpart_constructor_args():
    sig = inspect.signature(AncestorPart.__init__)
    params = list(sig.parameters.keys())



def test_discretechoice_is_not_abstract():
    assert not inspect.isabstract(DiscreteChoice)


def test_discretechoice_constructor_exists():
    assert callable(DiscreteChoice.__init__)


def test_discretechoice_constructor_args():
    sig = inspect.signature(DiscreteChoice.__init__)
    params = list(sig.parameters.keys())



def test_adb_range_is_not_abstract():
    assert not inspect.isabstract(adb_Range)


def test_adb_range_constructor_exists():
    assert callable(adb_Range.__init__)


def test_adb_range_constructor_args():
    sig = inspect.signature(adb_Range.__init__)
    params = list(sig.parameters.keys())



def test_explicitgenericactualparameter_is_not_abstract():
    assert not inspect.isabstract(ExplicitGenericActualParameter)


def test_explicitgenericactualparameter_constructor_exists():
    assert callable(ExplicitGenericActualParameter.__init__)


def test_explicitgenericactualparameter_constructor_args():
    sig = inspect.signature(ExplicitGenericActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_entryindex_is_not_abstract():
    assert not inspect.isabstract(EntryIndex)


def test_entryindex_constructor_exists():
    assert callable(EntryIndex.__init__)


def test_entryindex_constructor_args():
    sig = inspect.signature(EntryIndex.__init__)
    params = list(sig.parameters.keys())



def test_adb_primary_is_not_abstract():
    assert not inspect.isabstract(adb_Primary)


def test_adb_primary_constructor_exists():
    assert callable(adb_Primary.__init__)


def test_adb_primary_constructor_args():
    sig = inspect.signature(adb_Primary.__init__)
    params = list(sig.parameters.keys())



def test_adb_realrangespecification_is_not_abstract():
    assert not inspect.isabstract(adb_RealRangeSpecification)


def test_adb_realrangespecification_constructor_exists():
    assert callable(adb_RealRangeSpecification.__init__)


def test_adb_realrangespecification_constructor_args():
    sig = inspect.signature(adb_RealRangeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_discretechoice_is_not_abstract():
    assert not inspect.isabstract(adb_DiscreteChoice)


def test_adb_discretechoice_constructor_exists():
    assert callable(adb_DiscreteChoice.__init__)


def test_adb_discretechoice_constructor_args():
    sig = inspect.signature(adb_DiscreteChoice.__init__)
    params = list(sig.parameters.keys())



def test_adb_variant_is_not_abstract():
    assert not inspect.isabstract(adb_Variant)


def test_adb_variant_constructor_exists():
    assert callable(adb_Variant.__init__)


def test_adb_variant_constructor_args():
    sig = inspect.signature(adb_Variant.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentclause_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentClause)


def test_adb_componentclause_constructor_exists():
    assert callable(adb_ComponentClause.__init__)


def test_adb_componentclause_constructor_args():
    sig = inspect.signature(adb_ComponentClause.__init__)
    params = list(sig.parameters.keys())
    assert "localName" in params, "Missing parameter 'localName'"

def test_adb_componentclause_has_localName():
    assert hasattr(adb_ComponentClause, "localName")
    descriptor = None
    for klass in adb_ComponentClause.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)



def test_adb_modclause_is_not_abstract():
    assert not inspect.isabstract(adb_ModClause)


def test_adb_modclause_constructor_exists():
    assert callable(adb_ModClause.__init__)


def test_adb_modclause_constructor_args():
    sig = inspect.signature(adb_ModClause.__init__)
    params = list(sig.parameters.keys())



def test_realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(RealTypeDefinition)


def test_realtypedefinition_constructor_exists():
    assert callable(RealTypeDefinition.__init__)


def test_realtypedefinition_constructor_args():
    sig = inspect.signature(RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_fixedpointdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_FixedPointDefinition)


def test_adb_fixedpointdefinition_constructor_exists():
    assert callable(adb_FixedPointDefinition.__init__)


def test_adb_fixedpointdefinition_constructor_args():
    sig = inspect.signature(adb_FixedPointDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_floatingpointdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_FloatingPointDefinition)


def test_adb_floatingpointdefinition_constructor_exists():
    assert callable(adb_FloatingPointDefinition.__init__)


def test_adb_floatingpointdefinition_constructor_args():
    sig = inspect.signature(adb_FloatingPointDefinition.__init__)
    params = list(sig.parameters.keys())



def test_componentitem_is_not_abstract():
    assert not inspect.isabstract(ComponentItem)


def test_componentitem_constructor_exists():
    assert callable(ComponentItem.__init__)


def test_componentitem_constructor_args():
    sig = inspect.signature(ComponentItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_variantpart_is_not_abstract():
    assert not inspect.isabstract(adb_VariantPart)


def test_adb_variantpart_constructor_exists():
    assert callable(adb_VariantPart.__init__)


def test_adb_variantpart_constructor_args():
    sig = inspect.signature(adb_VariantPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_variantpart_has_name():
    assert hasattr(adb_VariantPart, "name")
    descriptor = None
    for klass in adb_VariantPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_optvariantpart_is_not_abstract():
    assert not inspect.isabstract(adb_OptVariantPart)


def test_adb_optvariantpart_constructor_exists():
    assert callable(adb_OptVariantPart.__init__)


def test_adb_optvariantpart_constructor_args():
    sig = inspect.signature(adb_OptVariantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentitem_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentItem)


def test_adb_componentitem_constructor_exists():
    assert callable(adb_ComponentItem.__init__)


def test_adb_componentitem_constructor_args():
    sig = inspect.signature(adb_ComponentItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentlist_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentList)


def test_adb_componentlist_constructor_exists():
    assert callable(adb_ComponentList.__init__)


def test_adb_componentlist_constructor_args():
    sig = inspect.signature(adb_ComponentList.__init__)
    params = list(sig.parameters.keys())



def test_adb_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(adb_SimpleExpression)


def test_adb_simpleexpression_constructor_exists():
    assert callable(adb_SimpleExpression.__init__)


def test_adb_simpleexpression_constructor_args():
    sig = inspect.signature(adb_SimpleExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryAddingOperator" in params, "Missing parameter 'unaryAddingOperator'"
    assert "binaryAddingOperators" in params, "Missing parameter 'binaryAddingOperators'"

def test_adb_simpleexpression_has_unaryAddingOperator():
    assert hasattr(adb_SimpleExpression, "unaryAddingOperator")
    descriptor = None
    for klass in adb_SimpleExpression.__mro__:
        if "unaryAddingOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryAddingOperator"]
            break
    assert isinstance(descriptor, property)

def test_adb_simpleexpression_has_binaryAddingOperators():
    assert hasattr(adb_SimpleExpression, "binaryAddingOperators")
    descriptor = None
    for klass in adb_SimpleExpression.__mro__:
        if "binaryAddingOperators" in klass.__dict__:
            descriptor = klass.__dict__["binaryAddingOperators"]
            break
    assert isinstance(descriptor, property)



def test_integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(IntegerTypeDefinition)


def test_integertypedefinition_constructor_exists():
    assert callable(IntegerTypeDefinition.__init__)


def test_integertypedefinition_constructor_args():
    sig = inspect.signature(IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_modulartypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_ModularTypeDefinition)


def test_adb_modulartypedefinition_constructor_exists():
    assert callable(adb_ModularTypeDefinition.__init__)


def test_adb_modulartypedefinition_constructor_args():
    sig = inspect.signature(adb_ModularTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_signedintegertypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_SignedIntegerTypeDefinition)


def test_adb_signedintegertypedefinition_constructor_exists():
    assert callable(adb_SignedIntegerTypeDefinition.__init__)


def test_adb_signedintegertypedefinition_constructor_args():
    sig = inspect.signature(adb_SignedIntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_parameterspecification_is_not_abstract():
    assert not inspect.isabstract(adb_ParameterSpecification)


def test_adb_parameterspecification_constructor_exists():
    assert callable(adb_ParameterSpecification.__init__)


def test_adb_parameterspecification_constructor_args():
    sig = inspect.signature(adb_ParameterSpecification.__init__)
    params = list(sig.parameters.keys())



def test_returnsubtypeindication_is_not_abstract():
    assert not inspect.isabstract(ReturnSubtypeIndication)


def test_returnsubtypeindication_constructor_exists():
    assert callable(ReturnSubtypeIndication.__init__)


def test_returnsubtypeindication_constructor_args():
    sig = inspect.signature(ReturnSubtypeIndication.__init__)
    params = list(sig.parameters.keys())



def test_arrayindexes_is_not_abstract():
    assert not inspect.isabstract(ArrayIndexes)


def test_arrayindexes_constructor_exists():
    assert callable(ArrayIndexes.__init__)


def test_arrayindexes_constructor_args():
    sig = inspect.signature(ArrayIndexes.__init__)
    params = list(sig.parameters.keys())



def test_adb_constrainedindexes_is_not_abstract():
    assert not inspect.isabstract(adb_ConstrainedIndexes)


def test_adb_constrainedindexes_constructor_exists():
    assert callable(adb_ConstrainedIndexes.__init__)


def test_adb_constrainedindexes_constructor_args():
    sig = inspect.signature(adb_ConstrainedIndexes.__init__)
    params = list(sig.parameters.keys())



def test_adb_unconstrainedindexes_is_not_abstract():
    assert not inspect.isabstract(adb_UnconstrainedIndexes)


def test_adb_unconstrainedindexes_constructor_exists():
    assert callable(adb_UnconstrainedIndexes.__init__)


def test_adb_unconstrainedindexes_constructor_args():
    sig = inspect.signature(adb_UnconstrainedIndexes.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentDefinition)


def test_adb_componentdefinition_constructor_exists():
    assert callable(adb_ComponentDefinition.__init__)


def test_adb_componentdefinition_constructor_args():
    sig = inspect.signature(adb_ComponentDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "aliased" in params, "Missing parameter 'aliased'"

def test_adb_componentdefinition_has_aliased():
    assert hasattr(adb_ComponentDefinition, "aliased")
    descriptor = None
    for klass in adb_ComponentDefinition.__mro__:
        if "aliased" in klass.__dict__:
            descriptor = klass.__dict__["aliased"]
            break
    assert isinstance(descriptor, property)



def test_adb_arrayindexes_is_not_abstract():
    assert not inspect.isabstract(adb_ArrayIndexes)


def test_adb_arrayindexes_constructor_exists():
    assert callable(adb_ArrayIndexes.__init__)


def test_adb_arrayindexes_constructor_args():
    sig = inspect.signature(adb_ArrayIndexes.__init__)
    params = list(sig.parameters.keys())



def test_notnullaccessdefinition_is_not_abstract():
    assert not inspect.isabstract(NotNullAccessDefinition)


def test_notnullaccessdefinition_constructor_exists():
    assert callable(NotNullAccessDefinition.__init__)


def test_notnullaccessdefinition_constructor_args():
    sig = inspect.signature(NotNullAccessDefinition.__init__)
    params = list(sig.parameters.keys())



def test_accessspecification_is_not_abstract():
    assert not inspect.isabstract(AccessSpecification)


def test_accessspecification_constructor_exists():
    assert callable(AccessSpecification.__init__)


def test_accessspecification_constructor_args():
    sig = inspect.signature(AccessSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_accesstodatadefinition_is_not_abstract():
    assert not inspect.isabstract(adb_AccessToDataDefinition)


def test_adb_accesstodatadefinition_constructor_exists():
    assert callable(adb_AccessToDataDefinition.__init__)


def test_adb_accesstodatadefinition_constructor_args():
    sig = inspect.signature(adb_AccessToDataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "generalAccessModifier" in params, "Missing parameter 'generalAccessModifier'"

def test_adb_accesstodatadefinition_has_generalAccessModifier():
    assert hasattr(adb_AccessToDataDefinition, "generalAccessModifier")
    descriptor = None
    for klass in adb_AccessToDataDefinition.__mro__:
        if "generalAccessModifier" in klass.__dict__:
            descriptor = klass.__dict__["generalAccessModifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_accesstosubprogramdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_AccessToSubprogramDefinition)


def test_adb_accesstosubprogramdefinition_constructor_exists():
    assert callable(adb_AccessToSubprogramDefinition.__init__)


def test_adb_accesstosubprogramdefinition_constructor_args():
    sig = inspect.signature(adb_AccessToSubprogramDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"

def test_adb_accesstosubprogramdefinition_has_protected():
    assert hasattr(adb_AccessToSubprogramDefinition, "protected")
    descriptor = None
    for klass in adb_AccessToSubprogramDefinition.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_adb_accessspecification_is_not_abstract():
    assert not inspect.isabstract(adb_AccessSpecification)


def test_adb_accessspecification_constructor_exists():
    assert callable(adb_AccessSpecification.__init__)


def test_adb_accessspecification_constructor_args():
    sig = inspect.signature(adb_AccessSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_accesstodatainstance_is_not_abstract():
    assert not inspect.isabstract(adb_AccessToDataInstance)


def test_adb_accesstodatainstance_constructor_exists():
    assert callable(adb_AccessToDataInstance.__init__)


def test_adb_accesstodatainstance_constructor_args():
    sig = inspect.signature(adb_AccessToDataInstance.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_adb_accesstodatainstance_has_constant():
    assert hasattr(adb_AccessToDataInstance, "constant")
    descriptor = None
    for klass in adb_AccessToDataInstance.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_IntegerTypeDefinition)


def test_adb_integertypedefinition_constructor_exists():
    assert callable(adb_IntegerTypeDefinition.__init__)


def test_adb_integertypedefinition_constructor_args():
    sig = inspect.signature(adb_IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_RealTypeDefinition)


def test_adb_realtypedefinition_constructor_exists():
    assert callable(adb_RealTypeDefinition.__init__)


def test_adb_realtypedefinition_constructor_args():
    sig = inspect.signature(adb_RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_RecordTypeDefinition)


def test_adb_recordtypedefinition_constructor_exists():
    assert callable(adb_RecordTypeDefinition.__init__)


def test_adb_recordtypedefinition_constructor_args():
    sig = inspect.signature(adb_RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "limited" in params, "Missing parameter 'limited'"
    assert "tagged" in params, "Missing parameter 'tagged'"

def test_adb_recordtypedefinition_has_abstract():
    assert hasattr(adb_RecordTypeDefinition, "abstract")
    descriptor = None
    for klass in adb_RecordTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb_recordtypedefinition_has_limited():
    assert hasattr(adb_RecordTypeDefinition, "limited")
    descriptor = None
    for klass in adb_RecordTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_recordtypedefinition_has_tagged():
    assert hasattr(adb_RecordTypeDefinition, "tagged")
    descriptor = None
    for klass in adb_RecordTypeDefinition.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)



def test_adb_derivedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_DerivedTypeDefinition)


def test_adb_derivedtypedefinition_constructor_exists():
    assert callable(adb_DerivedTypeDefinition.__init__)


def test_adb_derivedtypedefinition_constructor_args():
    sig = inspect.signature(adb_DerivedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_adb_derivedtypedefinition_has_limited():
    assert hasattr(adb_DerivedTypeDefinition, "limited")
    descriptor = None
    for klass in adb_DerivedTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_derivedtypedefinition_has_abstract():
    assert hasattr(adb_DerivedTypeDefinition, "abstract")
    descriptor = None
    for klass in adb_DerivedTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_adb_enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_EnumerationTypeDefinition)


def test_adb_enumerationtypedefinition_constructor_exists():
    assert callable(adb_EnumerationTypeDefinition.__init__)


def test_adb_enumerationtypedefinition_constructor_args():
    sig = inspect.signature(adb_EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "enumerationliteralspecifications" in params, "Missing parameter 'enumerationliteralspecifications'"

def test_adb_enumerationtypedefinition_has_enumerationliteralspecifications():
    assert hasattr(adb_EnumerationTypeDefinition, "enumerationliteralspecifications")
    descriptor = None
    for klass in adb_EnumerationTypeDefinition.__mro__:
        if "enumerationliteralspecifications" in klass.__dict__:
            descriptor = klass.__dict__["enumerationliteralspecifications"]
            break
    assert isinstance(descriptor, property)



def test_adb_notnullaccessdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_NotNullAccessDefinition)


def test_adb_notnullaccessdefinition_constructor_exists():
    assert callable(adb_NotNullAccessDefinition.__init__)


def test_adb_notnullaccessdefinition_constructor_args():
    sig = inspect.signature(adb_NotNullAccessDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_discriminantspecification_is_not_abstract():
    assert not inspect.isabstract(adb_DiscriminantSpecification)


def test_adb_discriminantspecification_constructor_exists():
    assert callable(adb_DiscriminantSpecification.__init__)


def test_adb_discriminantspecification_constructor_args():
    sig = inspect.signature(adb_DiscriminantSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_recorddefinition_is_not_abstract():
    assert not inspect.isabstract(adb_RecordDefinition)


def test_adb_recorddefinition_constructor_exists():
    assert callable(adb_RecordDefinition.__init__)


def test_adb_recorddefinition_constructor_args():
    sig = inspect.signature(adb_RecordDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_adb_recorddefinition_has_null():
    assert hasattr(adb_RecordDefinition, "null")
    descriptor = None
    for klass in adb_RecordDefinition.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_adb_recordextensionpart_is_not_abstract():
    assert not inspect.isabstract(adb_RecordExtensionPart)


def test_adb_recordextensionpart_constructor_exists():
    assert callable(adb_RecordExtensionPart.__init__)


def test_adb_recordextensionpart_constructor_args():
    sig = inspect.signature(adb_RecordExtensionPart.__init__)
    params = list(sig.parameters.keys())



def test_discriminantpart_is_not_abstract():
    assert not inspect.isabstract(DiscriminantPart)


def test_discriminantpart_constructor_exists():
    assert callable(DiscriminantPart.__init__)


def test_discriminantpart_constructor_args():
    sig = inspect.signature(DiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_unknowndiscriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb_UnknownDiscriminantPart)


def test_adb_unknowndiscriminantpart_constructor_exists():
    assert callable(adb_UnknownDiscriminantPart.__init__)


def test_adb_unknowndiscriminantpart_constructor_args():
    sig = inspect.signature(adb_UnknownDiscriminantPart.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb_unknowndiscriminantpart_has_box():
    assert hasattr(adb_UnknownDiscriminantPart, "box")
    descriptor = None
    for klass in adb_UnknownDiscriminantPart.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb_explicitgenericactualparameter_is_not_abstract():
    assert not inspect.isabstract(adb_ExplicitGenericActualParameter)


def test_adb_explicitgenericactualparameter_constructor_exists():
    assert callable(adb_ExplicitGenericActualParameter.__init__)


def test_adb_explicitgenericactualparameter_constructor_args():
    sig = inspect.signature(adb_ExplicitGenericActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_abortstatement_is_not_abstract():
    assert not inspect.isabstract(AbortStatement)


def test_abortstatement_constructor_exists():
    assert callable(AbortStatement.__init__)


def test_abortstatement_constructor_args():
    sig = inspect.signature(AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_tasknames_is_not_abstract():
    assert not inspect.isabstract(adb_TaskNames)


def test_adb_tasknames_constructor_exists():
    assert callable(adb_TaskNames.__init__)


def test_adb_tasknames_constructor_args():
    sig = inspect.signature(adb_TaskNames.__init__)
    params = list(sig.parameters.keys())



def test_adb_entrycallalternative_is_not_abstract():
    assert not inspect.isabstract(adb_EntryCallAlternative)


def test_adb_entrycallalternative_constructor_exists():
    assert callable(adb_EntryCallAlternative.__init__)


def test_adb_entrycallalternative_constructor_args():
    sig = inspect.signature(adb_EntryCallAlternative.__init__)
    params = list(sig.parameters.keys())



def test_selectalternative_is_not_abstract():
    assert not inspect.isabstract(SelectAlternative)


def test_selectalternative_constructor_exists():
    assert callable(SelectAlternative.__init__)


def test_selectalternative_constructor_args():
    sig = inspect.signature(SelectAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_delayalternative_is_not_abstract():
    assert not inspect.isabstract(adb_DelayAlternative)


def test_adb_delayalternative_constructor_exists():
    assert callable(adb_DelayAlternative.__init__)


def test_adb_delayalternative_constructor_args():
    sig = inspect.signature(adb_DelayAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_acceptalternative_is_not_abstract():
    assert not inspect.isabstract(adb_AcceptAlternative)


def test_adb_acceptalternative_constructor_exists():
    assert callable(adb_AcceptAlternative.__init__)


def test_adb_acceptalternative_constructor_args():
    sig = inspect.signature(adb_AcceptAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_guardedalternative_is_not_abstract():
    assert not inspect.isabstract(adb_GuardedAlternative)


def test_adb_guardedalternative_constructor_exists():
    assert callable(adb_GuardedAlternative.__init__)


def test_adb_guardedalternative_constructor_args():
    sig = inspect.signature(adb_GuardedAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_selectalternative_is_not_abstract():
    assert not inspect.isabstract(adb_SelectAlternative)


def test_adb_selectalternative_constructor_exists():
    assert callable(adb_SelectAlternative.__init__)


def test_adb_selectalternative_constructor_args():
    sig = inspect.signature(adb_SelectAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_guard_is_not_abstract():
    assert not inspect.isabstract(adb_Guard)


def test_adb_guard_constructor_exists():
    assert callable(adb_Guard.__init__)


def test_adb_guard_constructor_args():
    sig = inspect.signature(adb_Guard.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_conditionalentrycall_is_not_abstract():
    assert not inspect.isabstract(adb_ConditionalEntryCall)


def test_adb_conditionalentrycall_constructor_exists():
    assert callable(adb_ConditionalEntryCall.__init__)


def test_adb_conditionalentrycall_constructor_args():
    sig = inspect.signature(adb_ConditionalEntryCall.__init__)
    params = list(sig.parameters.keys())



def test_adb_timedentrycall_is_not_abstract():
    assert not inspect.isabstract(adb_TimedEntryCall)


def test_adb_timedentrycall_constructor_exists():
    assert callable(adb_TimedEntryCall.__init__)


def test_adb_timedentrycall_constructor_args():
    sig = inspect.signature(adb_TimedEntryCall.__init__)
    params = list(sig.parameters.keys())



def test_adb_selectiveaccept_is_not_abstract():
    assert not inspect.isabstract(adb_SelectiveAccept)


def test_adb_selectiveaccept_constructor_exists():
    assert callable(adb_SelectiveAccept.__init__)


def test_adb_selectiveaccept_constructor_args():
    sig = inspect.signature(adb_SelectiveAccept.__init__)
    params = list(sig.parameters.keys())



def test_adb_triggeringstatement_is_not_abstract():
    assert not inspect.isabstract(adb_TriggeringStatement)


def test_adb_triggeringstatement_constructor_exists():
    assert callable(adb_TriggeringStatement.__init__)


def test_adb_triggeringstatement_constructor_args():
    sig = inspect.signature(adb_TriggeringStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_abortablepart_is_not_abstract():
    assert not inspect.isabstract(adb_AbortablePart)


def test_adb_abortablepart_constructor_exists():
    assert callable(adb_AbortablePart.__init__)


def test_adb_abortablepart_constructor_args():
    sig = inspect.signature(adb_AbortablePart.__init__)
    params = list(sig.parameters.keys())



def test_adb_triggeringalternative_is_not_abstract():
    assert not inspect.isabstract(adb_TriggeringAlternative)


def test_adb_triggeringalternative_constructor_exists():
    assert callable(adb_TriggeringAlternative.__init__)


def test_adb_triggeringalternative_constructor_args():
    sig = inspect.signature(adb_TriggeringAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_asynchronousselect_is_not_abstract():
    assert not inspect.isabstract(adb_AsynchronousSelect)


def test_adb_asynchronousselect_constructor_exists():
    assert callable(adb_AsynchronousSelect.__init__)


def test_adb_asynchronousselect_constructor_args():
    sig = inspect.signature(adb_AsynchronousSelect.__init__)
    params = list(sig.parameters.keys())



def test_adb_entryindexspecification_is_not_abstract():
    assert not inspect.isabstract(adb_EntryIndexSpecification)


def test_adb_entryindexspecification_constructor_exists():
    assert callable(adb_EntryIndexSpecification.__init__)


def test_adb_entryindexspecification_constructor_args():
    sig = inspect.signature(adb_EntryIndexSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_entryindexspecification_has_name():
    assert hasattr(adb_EntryIndexSpecification, "name")
    descriptor = None
    for klass in adb_EntryIndexSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_entrybarrier_is_not_abstract():
    assert not inspect.isabstract(adb_EntryBarrier)


def test_adb_entrybarrier_constructor_exists():
    assert callable(adb_EntryBarrier.__init__)


def test_adb_entrybarrier_constructor_args():
    sig = inspect.signature(adb_EntryBarrier.__init__)
    params = list(sig.parameters.keys())



def test_adb_entrybodyformalpart_is_not_abstract():
    assert not inspect.isabstract(adb_EntryBodyFormalPart)


def test_adb_entrybodyformalpart_constructor_exists():
    assert callable(adb_EntryBodyFormalPart.__init__)


def test_adb_entrybodyformalpart_constructor_args():
    sig = inspect.signature(adb_EntryBodyFormalPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_entryindex_is_not_abstract():
    assert not inspect.isabstract(adb_EntryIndex)


def test_adb_entryindex_constructor_exists():
    assert callable(adb_EntryIndex.__init__)


def test_adb_entryindex_constructor_args():
    sig = inspect.signature(adb_EntryIndex.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedoperationitem_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedOperationItem)


def test_adb_protectedoperationitem_constructor_exists():
    assert callable(adb_ProtectedOperationItem.__init__)


def test_adb_protectedoperationitem_constructor_args():
    sig = inspect.signature(adb_ProtectedOperationItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_returnsubtypeindication_is_not_abstract():
    assert not inspect.isabstract(adb_ReturnSubtypeIndication)


def test_adb_returnsubtypeindication_constructor_exists():
    assert callable(adb_ReturnSubtypeIndication.__init__)


def test_adb_returnsubtypeindication_constructor_args():
    sig = inspect.signature(adb_ReturnSubtypeIndication.__init__)
    params = list(sig.parameters.keys())



def test_triggeringstatement_is_not_abstract():
    assert not inspect.isabstract(TriggeringStatement)


def test_triggeringstatement_constructor_exists():
    assert callable(TriggeringStatement.__init__)


def test_triggeringstatement_constructor_args():
    sig = inspect.signature(TriggeringStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_loopparameterspecification_is_not_abstract():
    assert not inspect.isabstract(adb_LoopParameterSpecification)


def test_adb_loopparameterspecification_constructor_exists():
    assert callable(adb_LoopParameterSpecification.__init__)


def test_adb_loopparameterspecification_constructor_args():
    sig = inspect.signature(adb_LoopParameterSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb_loopparameterspecification_has_identifier():
    assert hasattr(adb_LoopParameterSpecification, "identifier")
    descriptor = None
    for klass in adb_LoopParameterSpecification.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_iterationscheme_is_not_abstract():
    assert not inspect.isabstract(adb_IterationScheme)


def test_adb_iterationscheme_constructor_exists():
    assert callable(adb_IterationScheme.__init__)


def test_adb_iterationscheme_constructor_args():
    sig = inspect.signature(adb_IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_compoundstatement_is_not_abstract():
    assert not inspect.isabstract(CompoundStatement)


def test_compoundstatement_constructor_exists():
    assert callable(CompoundStatement.__init__)


def test_compoundstatement_constructor_args():
    sig = inspect.signature(CompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_extendedreturnstatement_is_not_abstract():
    assert not inspect.isabstract(adb_ExtendedReturnStatement)


def test_adb_extendedreturnstatement_constructor_exists():
    assert callable(adb_ExtendedReturnStatement.__init__)


def test_adb_extendedreturnstatement_constructor_args():
    sig = inspect.signature(adb_ExtendedReturnStatement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb_extendedreturnstatement_has_identifier():
    assert hasattr(adb_ExtendedReturnStatement, "identifier")
    descriptor = None
    for klass in adb_ExtendedReturnStatement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_acceptstatement_is_not_abstract():
    assert not inspect.isabstract(adb_AcceptStatement)


def test_adb_acceptstatement_constructor_exists():
    assert callable(adb_AcceptStatement.__init__)


def test_adb_acceptstatement_constructor_args():
    sig = inspect.signature(adb_AcceptStatement.__init__)
    params = list(sig.parameters.keys())
    assert "entryidentifier" in params, "Missing parameter 'entryidentifier'"

def test_adb_acceptstatement_has_entryidentifier():
    assert hasattr(adb_AcceptStatement, "entryidentifier")
    descriptor = None
    for klass in adb_AcceptStatement.__mro__:
        if "entryidentifier" in klass.__dict__:
            descriptor = klass.__dict__["entryidentifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_selectstatement_is_not_abstract():
    assert not inspect.isabstract(adb_SelectStatement)


def test_adb_selectstatement_constructor_exists():
    assert callable(adb_SelectStatement.__init__)


def test_adb_selectstatement_constructor_args():
    sig = inspect.signature(adb_SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_loopstatement_is_not_abstract():
    assert not inspect.isabstract(adb_LoopStatement)


def test_adb_loopstatement_constructor_exists():
    assert callable(adb_LoopStatement.__init__)


def test_adb_loopstatement_constructor_args():
    sig = inspect.signature(adb_LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "sameName" in params, "Missing parameter 'sameName'"
    assert "name" in params, "Missing parameter 'name'"

def test_adb_loopstatement_has_sameName():
    assert hasattr(adb_LoopStatement, "sameName")
    descriptor = None
    for klass in adb_LoopStatement.__mro__:
        if "sameName" in klass.__dict__:
            descriptor = klass.__dict__["sameName"]
            break
    assert isinstance(descriptor, property)

def test_adb_loopstatement_has_name():
    assert hasattr(adb_LoopStatement, "name")
    descriptor = None
    for klass in adb_LoopStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_ifstatement_is_not_abstract():
    assert not inspect.isabstract(adb_IfStatement)


def test_adb_ifstatement_constructor_exists():
    assert callable(adb_IfStatement.__init__)


def test_adb_ifstatement_constructor_args():
    sig = inspect.signature(adb_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_pragmaargumentassociation_is_not_abstract():
    assert not inspect.isabstract(adb_PragmaArgumentAssociation)


def test_adb_pragmaargumentassociation_constructor_exists():
    assert callable(adb_PragmaArgumentAssociation.__init__)


def test_adb_pragmaargumentassociation_constructor_args():
    sig = inspect.signature(adb_PragmaArgumentAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_pragmaargumentassociation_has_name():
    assert hasattr(adb_PragmaArgumentAssociation, "name")
    descriptor = None
    for klass in adb_PragmaArgumentAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_discretechoicelist_is_not_abstract():
    assert not inspect.isabstract(adb_DiscreteChoiceList)


def test_adb_discretechoicelist_constructor_exists():
    assert callable(adb_DiscreteChoiceList.__init__)


def test_adb_discretechoicelist_constructor_args():
    sig = inspect.signature(adb_DiscreteChoiceList.__init__)
    params = list(sig.parameters.keys())



def test_adb_casestatementalternative_is_not_abstract():
    assert not inspect.isabstract(adb_CaseStatementAlternative)


def test_adb_casestatementalternative_constructor_exists():
    assert callable(adb_CaseStatementAlternative.__init__)


def test_adb_casestatementalternative_constructor_args():
    sig = inspect.signature(adb_CaseStatementAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb_casestatement_is_not_abstract():
    assert not inspect.isabstract(adb_CaseStatement)


def test_adb_casestatement_constructor_exists():
    assert callable(adb_CaseStatement.__init__)


def test_adb_casestatement_constructor_args():
    sig = inspect.signature(adb_CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_objectdeclaration_is_not_abstract():
    assert not inspect.isabstract(ObjectDeclaration)


def test_objectdeclaration_constructor_exists():
    assert callable(ObjectDeclaration.__init__)


def test_objectdeclaration_constructor_args():
    sig = inspect.signature(ObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_datainstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_DataInstanceDeclaration)


def test_adb_datainstancedeclaration_constructor_exists():
    assert callable(adb_DataInstanceDeclaration.__init__)


def test_adb_datainstancedeclaration_constructor_args():
    sig = inspect.signature(adb_DataInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "aliased" in params, "Missing parameter 'aliased'"

def test_adb_datainstancedeclaration_has_constant():
    assert hasattr(adb_DataInstanceDeclaration, "constant")
    descriptor = None
    for klass in adb_DataInstanceDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_adb_datainstancedeclaration_has_aliased():
    assert hasattr(adb_DataInstanceDeclaration, "aliased")
    descriptor = None
    for klass in adb_DataInstanceDeclaration.__mro__:
        if "aliased" in klass.__dict__:
            descriptor = klass.__dict__["aliased"]
            break
    assert isinstance(descriptor, property)



def test_adb_genericassociation_is_not_abstract():
    assert not inspect.isabstract(adb_GenericAssociation)


def test_adb_genericassociation_constructor_exists():
    assert callable(adb_GenericAssociation.__init__)


def test_adb_genericassociation_constructor_args():
    sig = inspect.signature(adb_GenericAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "selectorName" in params, "Missing parameter 'selectorName'"

def test_adb_genericassociation_has_selectorName():
    assert hasattr(adb_GenericAssociation, "selectorName")
    descriptor = None
    for klass in adb_GenericAssociation.__mro__:
        if "selectorName" in klass.__dict__:
            descriptor = klass.__dict__["selectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb_formalpackageassociation_is_not_abstract():
    assert not inspect.isabstract(adb_FormalPackageAssociation)


def test_adb_formalpackageassociation_constructor_exists():
    assert callable(adb_FormalPackageAssociation.__init__)


def test_adb_formalpackageassociation_constructor_args():
    sig = inspect.signature(adb_FormalPackageAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "genericFormalParameterSelectorName" in params, "Missing parameter 'genericFormalParameterSelectorName'"

def test_adb_formalpackageassociation_has_genericFormalParameterSelectorName():
    assert hasattr(adb_FormalPackageAssociation, "genericFormalParameterSelectorName")
    descriptor = None
    for klass in adb_FormalPackageAssociation.__mro__:
        if "genericFormalParameterSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["genericFormalParameterSelectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb_formalpackageactualpart_is_not_abstract():
    assert not inspect.isabstract(adb_FormalPackageActualPart)


def test_adb_formalpackageactualpart_constructor_exists():
    assert callable(adb_FormalPackageActualPart.__init__)


def test_adb_formalpackageactualpart_constructor_args():
    sig = inspect.signature(adb_FormalPackageActualPart.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb_formalpackageactualpart_has_box():
    assert hasattr(adb_FormalPackageActualPart, "box")
    descriptor = None
    for klass in adb_FormalPackageActualPart.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb_subprogramdefault_is_not_abstract():
    assert not inspect.isabstract(adb_SubprogramDefault)


def test_adb_subprogramdefault_constructor_exists():
    assert callable(adb_SubprogramDefault.__init__)


def test_adb_subprogramdefault_constructor_args():
    sig = inspect.signature(adb_SubprogramDefault.__init__)
    params = list(sig.parameters.keys())
    assert "defaultName" in params, "Missing parameter 'defaultName'"

def test_adb_subprogramdefault_has_defaultName():
    assert hasattr(adb_SubprogramDefault, "defaultName")
    descriptor = None
    for klass in adb_SubprogramDefault.__mro__:
        if "defaultName" in klass.__dict__:
            descriptor = klass.__dict__["defaultName"]
            break
    assert isinstance(descriptor, property)



def test_adb_expression_is_not_abstract():
    assert not inspect.isabstract(adb_Expression)


def test_adb_expression_constructor_exists():
    assert callable(adb_Expression.__init__)


def test_adb_expression_constructor_args():
    sig = inspect.signature(adb_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"

def test_adb_expression_has_booleanOperator():
    assert hasattr(adb_Expression, "booleanOperator")
    descriptor = None
    for klass in adb_Expression.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)



def test_adb_anonymousaccessdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_AnonymousAccessDefinition)


def test_adb_anonymousaccessdefinition_constructor_exists():
    assert callable(adb_AnonymousAccessDefinition.__init__)


def test_adb_anonymousaccessdefinition_constructor_args():
    sig = inspect.signature(adb_AnonymousAccessDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_optnullexclusion_is_not_abstract():
    assert not inspect.isabstract(adb_OptNullExclusion)


def test_adb_optnullexclusion_constructor_exists():
    assert callable(adb_OptNullExclusion.__init__)


def test_adb_optnullexclusion_constructor_args():
    sig = inspect.signature(adb_OptNullExclusion.__init__)
    params = list(sig.parameters.keys())
    assert "not_null" in params, "Missing parameter 'not_null'"

def test_adb_optnullexclusion_has_not_null():
    assert hasattr(adb_OptNullExclusion, "not_null")
    descriptor = None
    for klass in adb_OptNullExclusion.__mro__:
        if "not_null" in klass.__dict__:
            descriptor = klass.__dict__["not_null"]
            break
    assert isinstance(descriptor, property)



def test_adb_singleprotecteddeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_SingleProtectedDeclaration)


def test_adb_singleprotecteddeclaration_constructor_exists():
    assert callable(adb_SingleProtectedDeclaration.__init__)


def test_adb_singleprotecteddeclaration_constructor_args():
    sig = inspect.signature(adb_SingleProtectedDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_singleprotecteddeclaration_has_name():
    assert hasattr(adb_SingleProtectedDeclaration, "name")
    descriptor = None
    for klass in adb_SingleProtectedDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_mode_is_not_abstract():
    assert not inspect.isabstract(adb_Mode)


def test_adb_mode_constructor_exists():
    assert callable(adb_Mode.__init__)


def test_adb_mode_constructor_args():
    sig = inspect.signature(adb_Mode.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_adb_mode_has_out():
    assert hasattr(adb_Mode, "out")
    descriptor = None
    for klass in adb_Mode.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_adb_mode_has_in_():
    assert hasattr(adb_Mode, "in_")
    descriptor = None
    for klass in adb_Mode.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_adb_definingidentifierlist_is_not_abstract():
    assert not inspect.isabstract(adb_DefiningIdentifierList)


def test_adb_definingidentifierlist_constructor_exists():
    assert callable(adb_DefiningIdentifierList.__init__)


def test_adb_definingidentifierlist_constructor_args():
    sig = inspect.signature(adb_DefiningIdentifierList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_definingidentifierlist_has_name():
    assert hasattr(adb_DefiningIdentifierList, "name")
    descriptor = None
    for klass in adb_DefiningIdentifierList.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_formaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(FormalTypeDefinition)


def test_formaltypedefinition_constructor_exists():
    assert callable(FormalTypeDefinition.__init__)


def test_formaltypedefinition_constructor_args():
    sig = inspect.signature(FormalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_interfacetypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_InterfaceTypeDefinition)


def test_adb_interfacetypedefinition_constructor_exists():
    assert callable(adb_InterfaceTypeDefinition.__init__)


def test_adb_interfacetypedefinition_constructor_args():
    sig = inspect.signature(adb_InterfaceTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "synchro" in params, "Missing parameter 'synchro'"
    assert "protected" in params, "Missing parameter 'protected'"
    assert "task" in params, "Missing parameter 'task'"
    assert "limited" in params, "Missing parameter 'limited'"

def test_adb_interfacetypedefinition_has_synchro():
    assert hasattr(adb_InterfaceTypeDefinition, "synchro")
    descriptor = None
    for klass in adb_InterfaceTypeDefinition.__mro__:
        if "synchro" in klass.__dict__:
            descriptor = klass.__dict__["synchro"]
            break
    assert isinstance(descriptor, property)

def test_adb_interfacetypedefinition_has_protected():
    assert hasattr(adb_InterfaceTypeDefinition, "protected")
    descriptor = None
    for klass in adb_InterfaceTypeDefinition.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)

def test_adb_interfacetypedefinition_has_task():
    assert hasattr(adb_InterfaceTypeDefinition, "task")
    descriptor = None
    for klass in adb_InterfaceTypeDefinition.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)

def test_adb_interfacetypedefinition_has_limited():
    assert hasattr(adb_InterfaceTypeDefinition, "limited")
    descriptor = None
    for klass in adb_InterfaceTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)



def test_adb_arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_ArrayTypeDefinition)


def test_adb_arraytypedefinition_constructor_exists():
    assert callable(adb_ArrayTypeDefinition.__init__)


def test_adb_arraytypedefinition_constructor_args():
    sig = inspect.signature(adb_ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_AccessTypeDefinition)


def test_adb_accesstypedefinition_constructor_exists():
    assert callable(adb_AccessTypeDefinition.__init__)


def test_adb_accesstypedefinition_constructor_args():
    sig = inspect.signature(adb_AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_formalderivedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_FormalDerivedTypeDefinition)


def test_adb_formalderivedtypedefinition_constructor_exists():
    assert callable(adb_FormalDerivedTypeDefinition.__init__)


def test_adb_formalderivedtypedefinition_constructor_args():
    sig = inspect.signature(adb_FormalDerivedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "absract" in params, "Missing parameter 'absract'"
    assert "limited" in params, "Missing parameter 'limited'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_adb_formalderivedtypedefinition_has_absract():
    assert hasattr(adb_FormalDerivedTypeDefinition, "absract")
    descriptor = None
    for klass in adb_FormalDerivedTypeDefinition.__mro__:
        if "absract" in klass.__dict__:
            descriptor = klass.__dict__["absract"]
            break
    assert isinstance(descriptor, property)

def test_adb_formalderivedtypedefinition_has_limited():
    assert hasattr(adb_FormalDerivedTypeDefinition, "limited")
    descriptor = None
    for klass in adb_FormalDerivedTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_formalderivedtypedefinition_has_synchronized():
    assert hasattr(adb_FormalDerivedTypeDefinition, "synchronized")
    descriptor = None
    for klass in adb_FormalDerivedTypeDefinition.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_genericformalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(GenericFormalParameterDeclaration)


def test_genericformalparameterdeclaration_constructor_exists():
    assert callable(GenericFormalParameterDeclaration.__init__)


def test_genericformalparameterdeclaration_constructor_args():
    sig = inspect.signature(GenericFormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_formaltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FormalTypeDeclaration)


def test_adb_formaltypedeclaration_constructor_exists():
    assert callable(adb_FormalTypeDeclaration.__init__)


def test_adb_formaltypedeclaration_constructor_args():
    sig = inspect.signature(adb_FormalTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb_formaltypedeclaration_has_identifier():
    assert hasattr(adb_FormalTypeDeclaration, "identifier")
    descriptor = None
    for klass in adb_FormalTypeDeclaration.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_formalpackagedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FormalPackageDeclaration)


def test_adb_formalpackagedeclaration_constructor_exists():
    assert callable(adb_FormalPackageDeclaration.__init__)


def test_adb_formalpackagedeclaration_constructor_args():
    sig = inspect.signature(adb_FormalPackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "genericPackageName" in params, "Missing parameter 'genericPackageName'"

def test_adb_formalpackagedeclaration_has_name():
    assert hasattr(adb_FormalPackageDeclaration, "name")
    descriptor = None
    for klass in adb_FormalPackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adb_formalpackagedeclaration_has_genericPackageName():
    assert hasattr(adb_FormalPackageDeclaration, "genericPackageName")
    descriptor = None
    for klass in adb_FormalPackageDeclaration.__mro__:
        if "genericPackageName" in klass.__dict__:
            descriptor = klass.__dict__["genericPackageName"]
            break
    assert isinstance(descriptor, property)



def test_adb_formalsubprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FormalSubprogramDeclaration)


def test_adb_formalsubprogramdeclaration_constructor_exists():
    assert callable(adb_FormalSubprogramDeclaration.__init__)


def test_adb_formalsubprogramdeclaration_constructor_args():
    sig = inspect.signature(adb_FormalSubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_adb_formalsubprogramdeclaration_has_abstract():
    assert hasattr(adb_FormalSubprogramDeclaration, "abstract")
    descriptor = None
    for klass in adb_FormalSubprogramDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_adb_formalobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FormalObjectDeclaration)


def test_adb_formalobjectdeclaration_constructor_exists():
    assert callable(adb_FormalObjectDeclaration.__init__)


def test_adb_formalobjectdeclaration_constructor_args():
    sig = inspect.signature(adb_FormalObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_formalprivatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_FormalPrivateTypeDefinition)


def test_adb_formalprivatetypedefinition_constructor_exists():
    assert callable(adb_FormalPrivateTypeDefinition.__init__)


def test_adb_formalprivatetypedefinition_constructor_args():
    sig = inspect.signature(adb_FormalPrivateTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "tagged" in params, "Missing parameter 'tagged'"

def test_adb_formalprivatetypedefinition_has_limited():
    assert hasattr(adb_FormalPrivateTypeDefinition, "limited")
    descriptor = None
    for klass in adb_FormalPrivateTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_formalprivatetypedefinition_has_abstract():
    assert hasattr(adb_FormalPrivateTypeDefinition, "abstract")
    descriptor = None
    for klass in adb_FormalPrivateTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb_formalprivatetypedefinition_has_tagged():
    assert hasattr(adb_FormalPrivateTypeDefinition, "tagged")
    descriptor = None
    for klass in adb_FormalPrivateTypeDefinition.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)



def test_adb_formaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_FormalTypeDefinition)


def test_adb_formaltypedefinition_constructor_exists():
    assert callable(adb_FormalTypeDefinition.__init__)


def test_adb_formaltypedefinition_constructor_args():
    sig = inspect.signature(adb_FormalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(adb_ExceptionHandler)


def test_adb_exceptionhandler_constructor_exists():
    assert callable(adb_ExceptionHandler.__init__)


def test_adb_exceptionhandler_constructor_args():
    sig = inspect.signature(adb_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_exceptionhandler_has_name():
    assert hasattr(adb_ExceptionHandler, "name")
    descriptor = None
    for klass in adb_ExceptionHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_genericitem_is_not_abstract():
    assert not inspect.isabstract(adb_GenericItem)


def test_adb_genericitem_constructor_exists():
    assert callable(adb_GenericItem.__init__)


def test_adb_genericitem_constructor_args():
    sig = inspect.signature(adb_GenericItem.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_simplereturnstatement_is_not_abstract():
    assert not inspect.isabstract(adb_SimpleReturnStatement)


def test_adb_simplereturnstatement_constructor_exists():
    assert callable(adb_SimpleReturnStatement.__init__)


def test_adb_simplereturnstatement_constructor_args():
    sig = inspect.signature(adb_SimpleReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_gotostatement_is_not_abstract():
    assert not inspect.isabstract(adb_GotoStatement)


def test_adb_gotostatement_constructor_exists():
    assert callable(adb_GotoStatement.__init__)


def test_adb_gotostatement_constructor_args():
    sig = inspect.signature(adb_GotoStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelId" in params, "Missing parameter 'labelId'"

def test_adb_gotostatement_has_labelId():
    assert hasattr(adb_GotoStatement, "labelId")
    descriptor = None
    for klass in adb_GotoStatement.__mro__:
        if "labelId" in klass.__dict__:
            descriptor = klass.__dict__["labelId"]
            break
    assert isinstance(descriptor, property)



def test_adb_abortstatement_is_not_abstract():
    assert not inspect.isabstract(adb_AbortStatement)


def test_adb_abortstatement_constructor_exists():
    assert callable(adb_AbortStatement.__init__)


def test_adb_abortstatement_constructor_args():
    sig = inspect.signature(adb_AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_exitstatement_is_not_abstract():
    assert not inspect.isabstract(adb_ExitStatement)


def test_adb_exitstatement_constructor_exists():
    assert callable(adb_ExitStatement.__init__)


def test_adb_exitstatement_constructor_args():
    sig = inspect.signature(adb_ExitStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(adb_AssignmentStatement)


def test_adb_assignmentstatement_constructor_exists():
    assert callable(adb_AssignmentStatement.__init__)


def test_adb_assignmentstatement_constructor_args():
    sig = inspect.signature(adb_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_delaystatement_is_not_abstract():
    assert not inspect.isabstract(adb_DelayStatement)


def test_adb_delaystatement_constructor_exists():
    assert callable(adb_DelayStatement.__init__)


def test_adb_delaystatement_constructor_args():
    sig = inspect.signature(adb_DelayStatement.__init__)
    params = list(sig.parameters.keys())
    assert "until" in params, "Missing parameter 'until'"

def test_adb_delaystatement_has_until():
    assert hasattr(adb_DelayStatement, "until")
    descriptor = None
    for klass in adb_DelayStatement.__mro__:
        if "until" in klass.__dict__:
            descriptor = klass.__dict__["until"]
            break
    assert isinstance(descriptor, property)



def test_adb_procedureorentrycallstatement_is_not_abstract():
    assert not inspect.isabstract(adb_ProcedureOrEntryCallStatement)


def test_adb_procedureorentrycallstatement_constructor_exists():
    assert callable(adb_ProcedureOrEntryCallStatement.__init__)


def test_adb_procedureorentrycallstatement_constructor_args():
    sig = inspect.signature(adb_ProcedureOrEntryCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_raisestatement_is_not_abstract():
    assert not inspect.isabstract(adb_RaiseStatement)


def test_adb_raisestatement_constructor_exists():
    assert callable(adb_RaiseStatement.__init__)


def test_adb_raisestatement_constructor_args():
    sig = inspect.signature(adb_RaiseStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_requeuestatement_is_not_abstract():
    assert not inspect.isabstract(adb_RequeueStatement)


def test_adb_requeuestatement_constructor_exists():
    assert callable(adb_RequeueStatement.__init__)


def test_adb_requeuestatement_constructor_args():
    sig = inspect.signature(adb_RequeueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "abort" in params, "Missing parameter 'abort'"

def test_adb_requeuestatement_has_abort():
    assert hasattr(adb_RequeueStatement, "abort")
    descriptor = None
    for klass in adb_RequeueStatement.__mro__:
        if "abort" in klass.__dict__:
            descriptor = klass.__dict__["abort"]
            break
    assert isinstance(descriptor, property)



def test_adb_nullstatement_is_not_abstract():
    assert not inspect.isabstract(adb_NullStatement)


def test_adb_nullstatement_constructor_exists():
    assert callable(adb_NullStatement.__init__)


def test_adb_nullstatement_constructor_args():
    sig = inspect.signature(adb_NullStatement.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_adb_nullstatement_has_null():
    assert hasattr(adb_NullStatement, "null")
    descriptor = None
    for klass in adb_NullStatement.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_adb_compoundstatement_is_not_abstract():
    assert not inspect.isabstract(adb_CompoundStatement)


def test_adb_compoundstatement_constructor_exists():
    assert callable(adb_CompoundStatement.__init__)


def test_adb_compoundstatement_constructor_args():
    sig = inspect.signature(adb_CompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_simplestatement_is_not_abstract():
    assert not inspect.isabstract(adb_SimpleStatement)


def test_adb_simplestatement_constructor_exists():
    assert callable(adb_SimpleStatement.__init__)


def test_adb_simplestatement_constructor_args():
    sig = inspect.signature(adb_SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb_statement_is_not_abstract():
    assert not inspect.isabstract(adb_Statement)


def test_adb_statement_constructor_exists():
    assert callable(adb_Statement.__init__)


def test_adb_statement_constructor_args():
    sig = inspect.signature(adb_Statement.__init__)
    params = list(sig.parameters.keys())



def test_adb_labelisablestatement_is_not_abstract():
    assert not inspect.isabstract(adb_LabelisableStatement)


def test_adb_labelisablestatement_constructor_exists():
    assert callable(adb_LabelisableStatement.__init__)


def test_adb_labelisablestatement_constructor_args():
    sig = inspect.signature(adb_LabelisableStatement.__init__)
    params = list(sig.parameters.keys())



def test_abortablepart_is_not_abstract():
    assert not inspect.isabstract(AbortablePart)


def test_abortablepart_constructor_exists():
    assert callable(AbortablePart.__init__)


def test_abortablepart_constructor_args():
    sig = inspect.signature(AbortablePart.__init__)
    params = list(sig.parameters.keys())



def test_handledsequenceofstatements_is_not_abstract():
    assert not inspect.isabstract(HandledSequenceOfStatements)


def test_handledsequenceofstatements_constructor_exists():
    assert callable(HandledSequenceOfStatements.__init__)


def test_handledsequenceofstatements_constructor_args():
    sig = inspect.signature(HandledSequenceOfStatements.__init__)
    params = list(sig.parameters.keys())



def test_adb_sequenceofstatements_is_not_abstract():
    assert not inspect.isabstract(adb_SequenceOfStatements)


def test_adb_sequenceofstatements_constructor_exists():
    assert callable(adb_SequenceOfStatements.__init__)


def test_adb_sequenceofstatements_constructor_args():
    sig = inspect.signature(adb_SequenceOfStatements.__init__)
    params = list(sig.parameters.keys())



def test_adb_label_is_not_abstract():
    assert not inspect.isabstract(adb_Label)


def test_adb_label_constructor_exists():
    assert callable(adb_Label.__init__)


def test_adb_label_constructor_args():
    sig = inspect.signature(adb_Label.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb_label_has_identifier():
    assert hasattr(adb_Label, "identifier")
    descriptor = None
    for klass in adb_Label.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_adb_properbody_is_not_abstract():
    assert not inspect.isabstract(adb_ProperBody)


def test_adb_properbody_constructor_exists():
    assert callable(adb_ProperBody.__init__)


def test_adb_properbody_constructor_args():
    sig = inspect.signature(adb_ProperBody.__init__)
    params = list(sig.parameters.keys())



def test_adb_bodystub_is_not_abstract():
    assert not inspect.isabstract(adb_BodyStub)


def test_adb_bodystub_constructor_exists():
    assert callable(adb_BodyStub.__init__)


def test_adb_bodystub_constructor_args():
    sig = inspect.signature(adb_BodyStub.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_bodystub_has_name():
    assert hasattr(adb_BodyStub, "name")
    descriptor = None
    for klass in adb_BodyStub.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_protectedelementdeclaration_is_not_abstract():
    assert not inspect.isabstract(ProtectedElementDeclaration)


def test_protectedelementdeclaration_constructor_exists():
    assert callable(ProtectedElementDeclaration.__init__)


def test_protectedelementdeclaration_constructor_args():
    sig = inspect.signature(ProtectedElementDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_componentdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ComponentDeclaration)


def test_adb_componentdeclaration_constructor_exists():
    assert callable(adb_ComponentDeclaration.__init__)


def test_adb_componentdeclaration_constructor_args():
    sig = inspect.signature(adb_ComponentDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedoperationdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedOperationDeclaration)


def test_adb_protectedoperationdeclaration_constructor_exists():
    assert callable(adb_ProtectedOperationDeclaration.__init__)


def test_adb_protectedoperationdeclaration_constructor_args():
    sig = inspect.signature(adb_ProtectedOperationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedelementdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedElementDeclaration)


def test_adb_protectedelementdeclaration_constructor_exists():
    assert callable(adb_ProtectedElementDeclaration.__init__)


def test_adb_protectedelementdeclaration_constructor_args():
    sig = inspect.signature(adb_ProtectedElementDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_protecteddefinition_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedDefinition)


def test_adb_protecteddefinition_constructor_exists():
    assert callable(adb_ProtectedDefinition.__init__)


def test_adb_protecteddefinition_constructor_args():
    sig = inspect.signature(adb_ProtectedDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_formalpart_is_not_abstract():
    assert not inspect.isabstract(adb_FormalPart)


def test_adb_formalpart_constructor_exists():
    assert callable(adb_FormalPart.__init__)


def test_adb_formalpart_constructor_args():
    sig = inspect.signature(adb_FormalPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_discretesubtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_DiscreteSubtypeDefinition)


def test_adb_discretesubtypedefinition_constructor_exists():
    assert callable(adb_DiscreteSubtypeDefinition.__init__)


def test_adb_discretesubtypedefinition_constructor_args():
    sig = inspect.signature(adb_DiscreteSubtypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_name_is_not_abstract():
    assert not inspect.isabstract(adb_Name)


def test_adb_name_constructor_exists():
    assert callable(adb_Name.__init__)


def test_adb_name_constructor_args():
    sig = inspect.signature(adb_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_name_has_name():
    assert hasattr(adb_Name, "name")
    descriptor = None
    for klass in adb_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_exceptionchoice_is_not_abstract():
    assert not inspect.isabstract(adb_ExceptionChoice)


def test_adb_exceptionchoice_constructor_exists():
    assert callable(adb_ExceptionChoice.__init__)


def test_adb_exceptionchoice_constructor_args():
    sig = inspect.signature(adb_ExceptionChoice.__init__)
    params = list(sig.parameters.keys())
    assert "others" in params, "Missing parameter 'others'"

def test_adb_exceptionchoice_has_others():
    assert hasattr(adb_ExceptionChoice, "others")
    descriptor = None
    for klass in adb_ExceptionChoice.__mro__:
        if "others" in klass.__dict__:
            descriptor = klass.__dict__["others"]
            break
    assert isinstance(descriptor, property)



def test_adb_parameterandresultprofile_is_not_abstract():
    assert not inspect.isabstract(adb_ParameterAndResultProfile)


def test_adb_parameterandresultprofile_constructor_exists():
    assert callable(adb_ParameterAndResultProfile.__init__)


def test_adb_parameterandresultprofile_constructor_args():
    sig = inspect.signature(adb_ParameterAndResultProfile.__init__)
    params = list(sig.parameters.keys())



def test_subprogramspecification_is_not_abstract():
    assert not inspect.isabstract(SubprogramSpecification)


def test_subprogramspecification_constructor_exists():
    assert callable(SubprogramSpecification.__init__)


def test_subprogramspecification_constructor_args():
    sig = inspect.signature(SubprogramSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_functionspecification_is_not_abstract():
    assert not inspect.isabstract(adb_FunctionSpecification)


def test_adb_functionspecification_constructor_exists():
    assert callable(adb_FunctionSpecification.__init__)


def test_adb_functionspecification_constructor_args():
    sig = inspect.signature(adb_FunctionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_procedurespecification_is_not_abstract():
    assert not inspect.isabstract(adb_ProcedureSpecification)


def test_adb_procedurespecification_constructor_exists():
    assert callable(adb_ProcedureSpecification.__init__)


def test_adb_procedurespecification_constructor_args():
    sig = inspect.signature(adb_ProcedureSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bodystub_is_not_abstract():
    assert not inspect.isabstract(BodyStub)


def test_bodystub_constructor_exists():
    assert callable(BodyStub.__init__)


def test_bodystub_constructor_args():
    sig = inspect.signature(BodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb_taskbodystub_is_not_abstract():
    assert not inspect.isabstract(adb_TaskBodyStub)


def test_adb_taskbodystub_constructor_exists():
    assert callable(adb_TaskBodyStub.__init__)


def test_adb_taskbodystub_constructor_args():
    sig = inspect.signature(adb_TaskBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb_packagebodystub_is_not_abstract():
    assert not inspect.isabstract(adb_PackageBodyStub)


def test_adb_packagebodystub_constructor_exists():
    assert callable(adb_PackageBodyStub.__init__)


def test_adb_packagebodystub_constructor_args():
    sig = inspect.signature(adb_PackageBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedbodystub_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedBodyStub)


def test_adb_protectedbodystub_constructor_exists():
    assert callable(adb_ProtectedBodyStub.__init__)


def test_adb_protectedbodystub_constructor_args():
    sig = inspect.signature(adb_ProtectedBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_newtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(NewTypeDeclaration)


def test_newtypedeclaration_constructor_exists():
    assert callable(NewTypeDeclaration.__init__)


def test_newtypedeclaration_constructor_args():
    sig = inspect.signature(NewTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_fulltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FullTypeDeclaration)


def test_adb_fulltypedeclaration_constructor_exists():
    assert callable(adb_FullTypeDeclaration.__init__)


def test_adb_fulltypedeclaration_constructor_args():
    sig = inspect.signature(adb_FullTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_SubtypeDeclaration)


def test_adb_subtypedeclaration_constructor_exists():
    assert callable(adb_SubtypeDeclaration.__init__)


def test_adb_subtypedeclaration_constructor_args():
    sig = inspect.signature(adb_SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_newtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_NewTypeDeclaration)


def test_adb_newtypedeclaration_constructor_exists():
    assert callable(adb_NewTypeDeclaration.__init__)


def test_adb_newtypedeclaration_constructor_args():
    sig = inspect.signature(adb_NewTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_taskdefinition_is_not_abstract():
    assert not inspect.isabstract(adb_TaskDefinition)


def test_adb_taskdefinition_constructor_exists():
    assert callable(adb_TaskDefinition.__init__)


def test_adb_taskdefinition_constructor_args():
    sig = inspect.signature(adb_TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb_interfacelist_is_not_abstract():
    assert not inspect.isabstract(adb_InterfaceList)


def test_adb_interfacelist_constructor_exists():
    assert callable(adb_InterfaceList.__init__)


def test_adb_interfacelist_constructor_args():
    sig = inspect.signature(adb_InterfaceList.__init__)
    params = list(sig.parameters.keys())



def test_adb_knowndiscriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb_KnownDiscriminantPart)


def test_adb_knowndiscriminantpart_constructor_exists():
    assert callable(adb_KnownDiscriminantPart.__init__)


def test_adb_knowndiscriminantpart_constructor_args():
    sig = inspect.signature(adb_KnownDiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_declarativeitem_is_not_abstract():
    assert not inspect.isabstract(DeclarativeItem)


def test_declarativeitem_constructor_exists():
    assert callable(DeclarativeItem.__init__)


def test_declarativeitem_constructor_args():
    sig = inspect.signature(DeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_body_is_not_abstract():
    assert not inspect.isabstract(adb_Body)


def test_adb_body_constructor_exists():
    assert callable(adb_Body.__init__)


def test_adb_body_constructor_args():
    sig = inspect.signature(adb_Body.__init__)
    params = list(sig.parameters.keys())



def test_protectedoperationdeclaration_is_not_abstract():
    assert not inspect.isabstract(ProtectedOperationDeclaration)


def test_protectedoperationdeclaration_constructor_exists():
    assert callable(ProtectedOperationDeclaration.__init__)


def test_protectedoperationdeclaration_constructor_args():
    sig = inspect.signature(ProtectedOperationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_taskitem_is_not_abstract():
    assert not inspect.isabstract(TaskItem)


def test_taskitem_constructor_exists():
    assert callable(TaskItem.__init__)


def test_taskitem_constructor_args():
    sig = inspect.signature(TaskItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_entrydeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_EntryDeclaration)


def test_adb_entrydeclaration_constructor_exists():
    assert callable(adb_EntryDeclaration.__init__)


def test_adb_entrydeclaration_constructor_args():
    sig = inspect.signature(adb_EntryDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_entrydeclaration_has_name():
    assert hasattr(adb_EntryDeclaration, "name")
    descriptor = None
    for klass in adb_EntryDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_taskitem_is_not_abstract():
    assert not inspect.isabstract(adb_TaskItem)


def test_adb_taskitem_constructor_exists():
    assert callable(adb_TaskItem.__init__)


def test_adb_taskitem_constructor_args():
    sig = inspect.signature(adb_TaskItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_subtypeindication_is_not_abstract():
    assert not inspect.isabstract(adb_SubtypeIndication)


def test_adb_subtypeindication_constructor_exists():
    assert callable(adb_SubtypeIndication.__init__)


def test_adb_subtypeindication_constructor_args():
    sig = inspect.signature(adb_SubtypeIndication.__init__)
    params = list(sig.parameters.keys())
    assert "subtypeMark" in params, "Missing parameter 'subtypeMark'"

def test_adb_subtypeindication_has_subtypeMark():
    assert hasattr(adb_SubtypeIndication, "subtypeMark")
    descriptor = None
    for klass in adb_SubtypeIndication.__mro__:
        if "subtypeMark" in klass.__dict__:
            descriptor = klass.__dict__["subtypeMark"]
            break
    assert isinstance(descriptor, property)



def test_adb_privateextensiondeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_PrivateExtensionDeclaration)


def test_adb_privateextensiondeclaration_constructor_exists():
    assert callable(adb_PrivateExtensionDeclaration.__init__)


def test_adb_privateextensiondeclaration_constructor_args():
    sig = inspect.signature(adb_PrivateExtensionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_adb_privateextensiondeclaration_has_limited():
    assert hasattr(adb_PrivateExtensionDeclaration, "limited")
    descriptor = None
    for klass in adb_PrivateExtensionDeclaration.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_privateextensiondeclaration_has_abstract():
    assert hasattr(adb_PrivateExtensionDeclaration, "abstract")
    descriptor = None
    for klass in adb_PrivateExtensionDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb_privateextensiondeclaration_has_synchronized():
    assert hasattr(adb_PrivateExtensionDeclaration, "synchronized")
    descriptor = None
    for klass in adb_PrivateExtensionDeclaration.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_adb_privatetypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_PrivateTypeDeclaration)


def test_adb_privatetypedeclaration_constructor_exists():
    assert callable(adb_PrivateTypeDeclaration.__init__)


def test_adb_privatetypedeclaration_constructor_args():
    sig = inspect.signature(adb_PrivateTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "tagged" in params, "Missing parameter 'tagged'"
    assert "limited" in params, "Missing parameter 'limited'"

def test_adb_privatetypedeclaration_has_abstract():
    assert hasattr(adb_PrivateTypeDeclaration, "abstract")
    descriptor = None
    for klass in adb_PrivateTypeDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb_privatetypedeclaration_has_tagged():
    assert hasattr(adb_PrivateTypeDeclaration, "tagged")
    descriptor = None
    for klass in adb_PrivateTypeDeclaration.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)

def test_adb_privatetypedeclaration_has_limited():
    assert hasattr(adb_PrivateTypeDeclaration, "limited")
    descriptor = None
    for klass in adb_PrivateTypeDeclaration.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)



def test_adb_discriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb_DiscriminantPart)


def test_adb_discriminantpart_constructor_exists():
    assert callable(adb_DiscriminantPart.__init__)


def test_adb_discriminantpart_constructor_args():
    sig = inspect.signature(adb_DiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_incompletetypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_IncompleteTypeDeclaration)


def test_adb_incompletetypedeclaration_constructor_exists():
    assert callable(adb_IncompleteTypeDeclaration.__init__)


def test_adb_incompletetypedeclaration_constructor_args():
    sig = inspect.signature(adb_IncompleteTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "tagged" in params, "Missing parameter 'tagged'"

def test_adb_incompletetypedeclaration_has_tagged():
    assert hasattr(adb_IncompleteTypeDeclaration, "tagged")
    descriptor = None
    for klass in adb_IncompleteTypeDeclaration.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)



def test_adb_typedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_TypeDefinition)


def test_adb_typedefinition_constructor_exists():
    assert callable(adb_TypeDefinition.__init__)


def test_adb_typedefinition_constructor_args():
    sig = inspect.signature(adb_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_fulltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(FullTypeDeclaration)


def test_fulltypedeclaration_constructor_exists():
    assert callable(FullTypeDeclaration.__init__)


def test_fulltypedeclaration_constructor_args():
    sig = inspect.signature(FullTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedTypeDeclaration)


def test_adb_protectedtypedeclaration_constructor_exists():
    assert callable(adb_ProtectedTypeDeclaration.__init__)


def test_adb_protectedtypedeclaration_constructor_args():
    sig = inspect.signature(adb_ProtectedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_fulldatatypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_FullDataTypeDeclaration)


def test_adb_fulldatatypedeclaration_constructor_exists():
    assert callable(adb_FullDataTypeDeclaration.__init__)


def test_adb_fulldatatypedeclaration_constructor_args():
    sig = inspect.signature(adb_FullDataTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_packagespecification_is_not_abstract():
    assert not inspect.isabstract(adb_PackageSpecification)


def test_adb_packagespecification_constructor_exists():
    assert callable(adb_PackageSpecification.__init__)


def test_adb_packagespecification_constructor_args():
    sig = inspect.signature(adb_PackageSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "endname" in params, "Missing parameter 'endname'"

def test_adb_packagespecification_has_endname():
    assert hasattr(adb_PackageSpecification, "endname")
    descriptor = None
    for klass in adb_PackageSpecification.__mro__:
        if "endname" in klass.__dict__:
            descriptor = klass.__dict__["endname"]
            break
    assert isinstance(descriptor, property)



def test_libraryspecification_is_not_abstract():
    assert not inspect.isabstract(LibrarySpecification)


def test_libraryspecification_constructor_exists():
    assert callable(LibrarySpecification.__init__)


def test_libraryspecification_constructor_args():
    sig = inspect.signature(LibrarySpecification.__init__)
    params = list(sig.parameters.keys())



def test_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(PackageDeclaration)


def test_packagedeclaration_constructor_exists():
    assert callable(PackageDeclaration.__init__)


def test_packagedeclaration_constructor_args():
    sig = inspect.signature(PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_renaming_is_not_abstract():
    assert not inspect.isabstract(adb_Renaming)


def test_adb_renaming_constructor_exists():
    assert callable(adb_Renaming.__init__)


def test_adb_renaming_constructor_args():
    sig = inspect.signature(adb_Renaming.__init__)
    params = list(sig.parameters.keys())
    assert "renamed" in params, "Missing parameter 'renamed'"

def test_adb_renaming_has_renamed():
    assert hasattr(adb_Renaming, "renamed")
    descriptor = None
    for klass in adb_Renaming.__mro__:
        if "renamed" in klass.__dict__:
            descriptor = klass.__dict__["renamed"]
            break
    assert isinstance(descriptor, property)



def test_adb_packagedefinition_is_not_abstract():
    assert not inspect.isabstract(adb_PackageDefinition)


def test_adb_packagedefinition_constructor_exists():
    assert callable(adb_PackageDefinition.__init__)


def test_adb_packagedefinition_constructor_args():
    sig = inspect.signature(adb_PackageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_basicdeclaration_is_not_abstract():
    assert not inspect.isabstract(BasicDeclaration)


def test_basicdeclaration_constructor_exists():
    assert callable(BasicDeclaration.__init__)


def test_basicdeclaration_constructor_args():
    sig = inspect.signature(BasicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_exceptiondeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ExceptionDeclaration)


def test_adb_exceptiondeclaration_constructor_exists():
    assert callable(adb_ExceptionDeclaration.__init__)


def test_adb_exceptiondeclaration_constructor_args():
    sig = inspect.signature(adb_ExceptionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_numberdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_NumberDeclaration)


def test_adb_numberdeclaration_constructor_exists():
    assert callable(adb_NumberDeclaration.__init__)


def test_adb_numberdeclaration_constructor_args():
    sig = inspect.signature(adb_NumberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_objectdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_ObjectDeclaration)


def test_adb_objectdeclaration_constructor_exists():
    assert callable(adb_ObjectDeclaration.__init__)


def test_adb_objectdeclaration_constructor_args():
    sig = inspect.signature(adb_ObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_taskdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_TaskDeclaration)


def test_adb_taskdeclaration_constructor_exists():
    assert callable(adb_TaskDeclaration.__init__)


def test_adb_taskdeclaration_constructor_args():
    sig = inspect.signature(adb_TaskDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_taskdeclaration_has_name():
    assert hasattr(adb_TaskDeclaration, "name")
    descriptor = None
    for klass in adb_TaskDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_TypeDeclaration)


def test_adb_typedeclaration_constructor_exists():
    assert callable(adb_TypeDeclaration.__init__)


def test_adb_typedeclaration_constructor_args():
    sig = inspect.signature(adb_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_typedeclaration_has_name():
    assert hasattr(adb_TypeDeclaration, "name")
    descriptor = None
    for klass in adb_TypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_libraryunitspecification_is_not_abstract():
    assert not inspect.isabstract(LibraryUnitSpecification)


def test_libraryunitspecification_constructor_exists():
    assert callable(LibraryUnitSpecification.__init__)


def test_libraryunitspecification_constructor_args():
    sig = inspect.signature(LibraryUnitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_PackageDeclaration)


def test_adb_packagedeclaration_constructor_exists():
    assert callable(adb_PackageDeclaration.__init__)


def test_adb_packagedeclaration_constructor_args():
    sig = inspect.signature(adb_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_packagedeclaration_has_name():
    assert hasattr(adb_PackageDeclaration, "name")
    descriptor = None
    for klass in adb_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_libraryunitspecification_is_not_abstract():
    assert not inspect.isabstract(adb_LibraryUnitSpecification)


def test_adb_libraryunitspecification_constructor_exists():
    assert callable(adb_LibraryUnitSpecification.__init__)


def test_adb_libraryunitspecification_constructor_args():
    sig = inspect.signature(adb_LibraryUnitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_adb_separatesubunit_is_not_abstract():
    assert not inspect.isabstract(adb_SeparateSubunit)


def test_adb_separatesubunit_constructor_exists():
    assert callable(adb_SeparateSubunit.__init__)


def test_adb_separatesubunit_constructor_args():
    sig = inspect.signature(adb_SeparateSubunit.__init__)
    params = list(sig.parameters.keys())
    assert "parentUnitName" in params, "Missing parameter 'parentUnitName'"

def test_adb_separatesubunit_has_parentUnitName():
    assert hasattr(adb_SeparateSubunit, "parentUnitName")
    descriptor = None
    for klass in adb_SeparateSubunit.__mro__:
        if "parentUnitName" in klass.__dict__:
            descriptor = klass.__dict__["parentUnitName"]
            break
    assert isinstance(descriptor, property)



def test_adb_handledsequenceofstatements_is_not_abstract():
    assert not inspect.isabstract(adb_HandledSequenceOfStatements)


def test_adb_handledsequenceofstatements_constructor_exists():
    assert callable(adb_HandledSequenceOfStatements.__init__)


def test_adb_handledsequenceofstatements_constructor_args():
    sig = inspect.signature(adb_HandledSequenceOfStatements.__init__)
    params = list(sig.parameters.keys())



def test_adb_declarativeitem_is_not_abstract():
    assert not inspect.isabstract(adb_DeclarativeItem)


def test_adb_declarativeitem_constructor_exists():
    assert callable(adb_DeclarativeItem.__init__)


def test_adb_declarativeitem_constructor_args():
    sig = inspect.signature(adb_DeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_declarativeblock_is_not_abstract():
    assert not inspect.isabstract(adb_DeclarativeBlock)


def test_adb_declarativeblock_constructor_exists():
    assert callable(adb_DeclarativeBlock.__init__)


def test_adb_declarativeblock_constructor_args():
    sig = inspect.signature(adb_DeclarativeBlock.__init__)
    params = list(sig.parameters.keys())



def test_adb_subprogramspecification_is_not_abstract():
    assert not inspect.isabstract(adb_SubprogramSpecification)


def test_adb_subprogramspecification_constructor_exists():
    assert callable(adb_SubprogramSpecification.__init__)


def test_adb_subprogramspecification_constructor_args():
    sig = inspect.signature(adb_SubprogramSpecification.__init__)
    params = list(sig.parameters.keys())



def test_protectedoperationitem_is_not_abstract():
    assert not inspect.isabstract(ProtectedOperationItem)


def test_protectedoperationitem_constructor_exists():
    assert callable(ProtectedOperationItem.__init__)


def test_protectedoperationitem_constructor_args():
    sig = inspect.signature(ProtectedOperationItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_SubprogramDeclaration)


def test_adb_subprogramdeclaration_constructor_exists():
    assert callable(adb_SubprogramDeclaration.__init__)


def test_adb_subprogramdeclaration_constructor_args():
    sig = inspect.signature(adb_SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "renamedName" in params, "Missing parameter 'renamedName'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "null" in params, "Missing parameter 'null'"

def test_adb_subprogramdeclaration_has_renamedName():
    assert hasattr(adb_SubprogramDeclaration, "renamedName")
    descriptor = None
    for klass in adb_SubprogramDeclaration.__mro__:
        if "renamedName" in klass.__dict__:
            descriptor = klass.__dict__["renamedName"]
            break
    assert isinstance(descriptor, property)

def test_adb_subprogramdeclaration_has_abstract():
    assert hasattr(adb_SubprogramDeclaration, "abstract")
    descriptor = None
    for klass in adb_SubprogramDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb_subprogramdeclaration_has_null():
    assert hasattr(adb_SubprogramDeclaration, "null")
    descriptor = None
    for klass in adb_SubprogramDeclaration.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_properbody_is_not_abstract():
    assert not inspect.isabstract(ProperBody)


def test_properbody_constructor_exists():
    assert callable(ProperBody.__init__)


def test_properbody_constructor_args():
    sig = inspect.signature(ProperBody.__init__)
    params = list(sig.parameters.keys())



def test_adb_protectedbody_is_not_abstract():
    assert not inspect.isabstract(adb_ProtectedBody)


def test_adb_protectedbody_constructor_exists():
    assert callable(adb_ProtectedBody.__init__)


def test_adb_protectedbody_constructor_args():
    sig = inspect.signature(adb_ProtectedBody.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"
    assert "idTask" in params, "Missing parameter 'idTask'"

def test_adb_protectedbody_has_identifier():
    assert hasattr(adb_ProtectedBody, "identifier")
    descriptor = None
    for klass in adb_ProtectedBody.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)

def test_adb_protectedbody_has_idTask():
    assert hasattr(adb_ProtectedBody, "idTask")
    descriptor = None
    for klass in adb_ProtectedBody.__mro__:
        if "idTask" in klass.__dict__:
            descriptor = klass.__dict__["idTask"]
            break
    assert isinstance(descriptor, property)



def test_declarativeblock_is_not_abstract():
    assert not inspect.isabstract(DeclarativeBlock)


def test_declarativeblock_constructor_exists():
    assert callable(DeclarativeBlock.__init__)


def test_declarativeblock_constructor_args():
    sig = inspect.signature(DeclarativeBlock.__init__)
    params = list(sig.parameters.keys())



def test_adb_taskbody_is_not_abstract():
    assert not inspect.isabstract(adb_TaskBody)


def test_adb_taskbody_constructor_exists():
    assert callable(adb_TaskBody.__init__)


def test_adb_taskbody_constructor_args():
    sig = inspect.signature(adb_TaskBody.__init__)
    params = list(sig.parameters.keys())



def test_adb_entrybody_is_not_abstract():
    assert not inspect.isabstract(adb_EntryBody)


def test_adb_entrybody_constructor_exists():
    assert callable(adb_EntryBody.__init__)


def test_adb_entrybody_constructor_args():
    sig = inspect.signature(adb_EntryBody.__init__)
    params = list(sig.parameters.keys())
    assert "endid" in params, "Missing parameter 'endid'"

def test_adb_entrybody_has_endid():
    assert hasattr(adb_EntryBody, "endid")
    descriptor = None
    for klass in adb_EntryBody.__mro__:
        if "endid" in klass.__dict__:
            descriptor = klass.__dict__["endid"]
            break
    assert isinstance(descriptor, property)



def test_adb_packagebody_is_not_abstract():
    assert not inspect.isabstract(adb_PackageBody)


def test_adb_packagebody_constructor_exists():
    assert callable(adb_PackageBody.__init__)


def test_adb_packagebody_constructor_args():
    sig = inspect.signature(adb_PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_adb_blockstatement_is_not_abstract():
    assert not inspect.isabstract(adb_BlockStatement)


def test_adb_blockstatement_constructor_exists():
    assert callable(adb_BlockStatement.__init__)


def test_adb_blockstatement_constructor_args():
    sig = inspect.signature(adb_BlockStatement.__init__)
    params = list(sig.parameters.keys())
    assert "blockStatementIdentifier" in params, "Missing parameter 'blockStatementIdentifier'"

def test_adb_blockstatement_has_blockStatementIdentifier():
    assert hasattr(adb_BlockStatement, "blockStatementIdentifier")
    descriptor = None
    for klass in adb_BlockStatement.__mro__:
        if "blockStatementIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["blockStatementIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_adb_subprogrambody_is_not_abstract():
    assert not inspect.isabstract(adb_SubprogramBody)


def test_adb_subprogrambody_constructor_exists():
    assert callable(adb_SubprogramBody.__init__)


def test_adb_subprogrambody_constructor_args():
    sig = inspect.signature(adb_SubprogramBody.__init__)
    params = list(sig.parameters.keys())
    assert "endname" in params, "Missing parameter 'endname'"

def test_adb_subprogrambody_has_endname():
    assert hasattr(adb_SubprogramBody, "endname")
    descriptor = None
    for klass in adb_SubprogramBody.__mro__:
        if "endname" in klass.__dict__:
            descriptor = klass.__dict__["endname"]
            break
    assert isinstance(descriptor, property)



def test_adb_basicdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(adb_BasicDeclarativeItem)


def test_adb_basicdeclarativeitem_constructor_exists():
    assert callable(adb_BasicDeclarativeItem.__init__)


def test_adb_basicdeclarativeitem_constructor_args():
    sig = inspect.signature(adb_BasicDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_genericactualpart_is_not_abstract():
    assert not inspect.isabstract(adb_GenericActualPart)


def test_adb_genericactualpart_constructor_exists():
    assert callable(adb_GenericActualPart.__init__)


def test_adb_genericactualpart_constructor_args():
    sig = inspect.signature(adb_GenericActualPart.__init__)
    params = list(sig.parameters.keys())



def test_adb_overridingindicator_is_not_abstract():
    assert not inspect.isabstract(adb_OverridingIndicator)


def test_adb_overridingindicator_constructor_exists():
    assert callable(adb_OverridingIndicator.__init__)


def test_adb_overridingindicator_constructor_args():
    sig = inspect.signature(adb_OverridingIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_adb_overridingindicator_has_not_():
    assert hasattr(adb_OverridingIndicator, "not_")
    descriptor = None
    for klass in adb_OverridingIndicator.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_adb_genericinstantiation_is_not_abstract():
    assert not inspect.isabstract(adb_GenericInstantiation)


def test_adb_genericinstantiation_constructor_exists():
    assert callable(adb_GenericInstantiation.__init__)


def test_adb_genericinstantiation_constructor_args():
    sig = inspect.signature(adb_GenericInstantiation.__init__)
    params = list(sig.parameters.keys())
    assert "genericName" in params, "Missing parameter 'genericName'"
    assert "name" in params, "Missing parameter 'name'"

def test_adb_genericinstantiation_has_genericName():
    assert hasattr(adb_GenericInstantiation, "genericName")
    descriptor = None
    for klass in adb_GenericInstantiation.__mro__:
        if "genericName" in klass.__dict__:
            descriptor = klass.__dict__["genericName"]
            break
    assert isinstance(descriptor, property)

def test_adb_genericinstantiation_has_name():
    assert hasattr(adb_GenericInstantiation, "name")
    descriptor = None
    for klass in adb_GenericInstantiation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_libraryspecification_is_not_abstract():
    assert not inspect.isabstract(adb_LibrarySpecification)


def test_adb_libraryspecification_constructor_exists():
    assert callable(adb_LibrarySpecification.__init__)


def test_adb_libraryspecification_constructor_args():
    sig = inspect.signature(adb_LibrarySpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb_genericitems_is_not_abstract():
    assert not inspect.isabstract(adb_GenericItems)


def test_adb_genericitems_constructor_exists():
    assert callable(adb_GenericItems.__init__)


def test_adb_genericitems_constructor_args():
    sig = inspect.signature(adb_GenericItems.__init__)
    params = list(sig.parameters.keys())



def test_adb_genericdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_GenericDeclaration)


def test_adb_genericdeclaration_constructor_exists():
    assert callable(adb_GenericDeclaration.__init__)


def test_adb_genericdeclaration_constructor_args():
    sig = inspect.signature(adb_GenericDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_useclause_is_not_abstract():
    assert not inspect.isabstract(UseClause)


def test_useclause_constructor_exists():
    assert callable(UseClause.__init__)


def test_useclause_constructor_args():
    sig = inspect.signature(UseClause.__init__)
    params = list(sig.parameters.keys())



def test_adb_usetypeclause_is_not_abstract():
    assert not inspect.isabstract(adb_UseTypeClause)


def test_adb_usetypeclause_constructor_exists():
    assert callable(adb_UseTypeClause.__init__)


def test_adb_usetypeclause_constructor_args():
    sig = inspect.signature(adb_UseTypeClause.__init__)
    params = list(sig.parameters.keys())
    assert "useTypeRefs" in params, "Missing parameter 'useTypeRefs'"
    assert "typesNames" in params, "Missing parameter 'typesNames'"

def test_adb_usetypeclause_has_useTypeRefs():
    assert hasattr(adb_UseTypeClause, "useTypeRefs")
    descriptor = None
    for klass in adb_UseTypeClause.__mro__:
        if "useTypeRefs" in klass.__dict__:
            descriptor = klass.__dict__["useTypeRefs"]
            break
    assert isinstance(descriptor, property)

def test_adb_usetypeclause_has_typesNames():
    assert hasattr(adb_UseTypeClause, "typesNames")
    descriptor = None
    for klass in adb_UseTypeClause.__mro__:
        if "typesNames" in klass.__dict__:
            descriptor = klass.__dict__["typesNames"]
            break
    assert isinstance(descriptor, property)



def test_adb_usepackageclause_is_not_abstract():
    assert not inspect.isabstract(adb_UsePackageClause)


def test_adb_usepackageclause_constructor_exists():
    assert callable(adb_UsePackageClause.__init__)


def test_adb_usepackageclause_constructor_args():
    sig = inspect.signature(adb_UsePackageClause.__init__)
    params = list(sig.parameters.keys())



def test_genericitem_is_not_abstract():
    assert not inspect.isabstract(GenericItem)


def test_genericitem_constructor_exists():
    assert callable(GenericItem.__init__)


def test_genericitem_constructor_args():
    sig = inspect.signature(GenericItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_genericformalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_GenericFormalParameterDeclaration)


def test_adb_genericformalparameterdeclaration_constructor_exists():
    assert callable(adb_GenericFormalParameterDeclaration.__init__)


def test_adb_genericformalparameterdeclaration_constructor_args():
    sig = inspect.signature(adb_GenericFormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_basicdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(BasicDeclarativeItem)


def test_basicdeclarativeitem_constructor_exists():
    assert callable(BasicDeclarativeItem.__init__)


def test_basicdeclarativeitem_constructor_args():
    sig = inspect.signature(BasicDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_basicdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_BasicDeclaration)


def test_adb_basicdeclaration_constructor_exists():
    assert callable(adb_BasicDeclaration.__init__)


def test_adb_basicdeclaration_constructor_args():
    sig = inspect.signature(adb_BasicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb_aspectclause_is_not_abstract():
    assert not inspect.isabstract(adb_AspectClause)


def test_adb_aspectclause_constructor_exists():
    assert callable(adb_AspectClause.__init__)


def test_adb_aspectclause_constructor_args():
    sig = inspect.signature(adb_AspectClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_aspectclause_has_name():
    assert hasattr(adb_AspectClause, "name")
    descriptor = None
    for klass in adb_AspectClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_libraryunitdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb_LibraryUnitDeclaration)


def test_adb_libraryunitdeclaration_constructor_exists():
    assert callable(adb_LibraryUnitDeclaration.__init__)


def test_adb_libraryunitdeclaration_constructor_args():
    sig = inspect.signature(adb_LibraryUnitDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "private" in params, "Missing parameter 'private'"

def test_adb_libraryunitdeclaration_has_private():
    assert hasattr(adb_LibraryUnitDeclaration, "private")
    descriptor = None
    for klass in adb_LibraryUnitDeclaration.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)



def test_contextitem_is_not_abstract():
    assert not inspect.isabstract(ContextItem)


def test_contextitem_constructor_exists():
    assert callable(ContextItem.__init__)


def test_contextitem_constructor_args():
    sig = inspect.signature(ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_useclause_is_not_abstract():
    assert not inspect.isabstract(adb_UseClause)


def test_adb_useclause_constructor_exists():
    assert callable(adb_UseClause.__init__)


def test_adb_useclause_constructor_args():
    sig = inspect.signature(adb_UseClause.__init__)
    params = list(sig.parameters.keys())



def test_adb_withclause_is_not_abstract():
    assert not inspect.isabstract(adb_WithClause)


def test_adb_withclause_constructor_exists():
    assert callable(adb_WithClause.__init__)


def test_adb_withclause_constructor_args():
    sig = inspect.signature(adb_WithClause.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "private" in params, "Missing parameter 'private'"

def test_adb_withclause_has_limited():
    assert hasattr(adb_WithClause, "limited")
    descriptor = None
    for klass in adb_WithClause.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb_withclause_has_private():
    assert hasattr(adb_WithClause, "private")
    descriptor = None
    for klass in adb_WithClause.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)



def test_adb_contextitem_is_not_abstract():
    assert not inspect.isabstract(adb_ContextItem)


def test_adb_contextitem_constructor_exists():
    assert callable(adb_ContextItem.__init__)


def test_adb_contextitem_constructor_args():
    sig = inspect.signature(adb_ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_adb_pragma_is_not_abstract():
    assert not inspect.isabstract(adb_Pragma)


def test_adb_pragma_constructor_exists():
    assert callable(adb_Pragma.__init__)


def test_adb_pragma_constructor_args():
    sig = inspect.signature(adb_Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb_pragma_has_name():
    assert hasattr(adb_Pragma, "name")
    descriptor = None
    for klass in adb_Pragma.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb_unit_is_not_abstract():
    assert not inspect.isabstract(adb_Unit)


def test_adb_unit_constructor_exists():
    assert callable(adb_Unit.__init__)


def test_adb_unit_constructor_args():
    sig = inspect.signature(adb_Unit.__init__)
    params = list(sig.parameters.keys())



def test_adb_contextclause_is_not_abstract():
    assert not inspect.isabstract(adb_ContextClause)


def test_adb_contextclause_constructor_exists():
    assert callable(adb_ContextClause.__init__)


def test_adb_contextclause_constructor_args():
    sig = inspect.signature(adb_ContextClause.__init__)
    params = list(sig.parameters.keys())



def test_adb_compilationunit_is_not_abstract():
    assert not inspect.isabstract(adb_CompilationUnit)


def test_adb_compilationunit_constructor_exists():
    assert callable(adb_CompilationUnit.__init__)


def test_adb_compilationunit_constructor_args():
    sig = inspect.signature(adb_CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_adb_compilation_is_not_abstract():
    assert not inspect.isabstract(adb_Compilation)


def test_adb_compilation_constructor_exists():
    assert callable(adb_Compilation.__init__)


def test_adb_compilation_constructor_args():
    sig = inspect.signature(adb_Compilation.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
RecordComponentAssociation_strategy = st.builds(
    RecordComponentAssociation,
)
adb_UninitializedComponents_strategy = st.builds(
    adb_UninitializedComponents,
    box=
        st.booleans()
)
adb_InitializedComponents_strategy = st.builds(
    adb_InitializedComponents,
)
adb_ParameterAssociation_strategy = st.builds(
    adb_ParameterAssociation,
    selectorName=
        safe_text
)
adb_RecordComponentAssociation_strategy = st.builds(
    adb_RecordComponentAssociation,
)
RecordAggregate_strategy = st.builds(
    RecordAggregate,
)
adb_RecordComponentAssociationList_strategy = st.builds(
    adb_RecordComponentAssociationList,
    nullRecord=
        st.booleans()
)
Aggregate_strategy = st.builds(
    Aggregate,
)
adb_ExtensionAggregate_strategy = st.builds(
    adb_ExtensionAggregate,
)
adb_RecordAggregate_strategy = st.builds(
    adb_RecordAggregate,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
ParenthesizedExpression_strategy = st.builds(
    ParenthesizedExpression,
)
adb_Aggregate_strategy = st.builds(
    adb_Aggregate,
)
adb_ComponentChoiceList_strategy = st.builds(
    adb_ComponentChoiceList,
    others=
        st.booleans(),
    componentSelectorName=
        safe_text
)
adb_DiscriminantSelectors_strategy = st.builds(
    adb_DiscriminantSelectors,
    discriminantSelectorName=
        safe_text
)
adb_DiscriminantAssociation_strategy = st.builds(
    adb_DiscriminantAssociation,
)
CompositeConstraint_strategy = st.builds(
    CompositeConstraint,
)
adb_IndexConstraint_strategy = st.builds(
    adb_IndexConstraint,
)
adb_DiscriminantConstraint_strategy = st.builds(
    adb_DiscriminantConstraint,
)
adb_CompositeConstraint_strategy = st.builds(
    adb_CompositeConstraint,
)
adb_OptConstraint_strategy = st.builds(
    adb_OptConstraint,
)
DiscreteRange_strategy = st.builds(
    DiscreteRange,
)
DiscreteSubtypeDefinition_strategy = st.builds(
    DiscreteSubtypeDefinition,
)
adb_DiscreteRange_strategy = st.builds(
    adb_DiscreteRange,
)
adb_Qualifier_strategy = st.builds(
    adb_Qualifier,
)
Primary_strategy = st.builds(
    Primary,
)
adb_QualifiedName_strategy = st.builds(
    adb_QualifiedName,
)
adb_StringLiteral_strategy = st.builds(
    adb_StringLiteral,
    value=
        safe_text
)
adb_Allocator_strategy = st.builds(
    adb_Allocator,
)
adb_Null_strategy = st.builds(
    adb_Null,
    value=
        safe_text
)
adb_ParenthesizedExpression_strategy = st.builds(
    adb_ParenthesizedExpression,
)
adb_NumericLiteral_strategy = st.builds(
    adb_NumericLiteral,
    value=
        safe_text
)
Range_strategy = st.builds(
    Range,
)
adb_ExplicitRange_strategy = st.builds(
    adb_ExplicitRange,
)
adb_EntityRange_strategy = st.builds(
    adb_EntityRange,
)
RangeConstraint_strategy = st.builds(
    RangeConstraint,
)
adb_ParameterEffectiveValue_strategy = st.builds(
    adb_ParameterEffectiveValue,
)
adb_AttributeDesignator_strategy = st.builds(
    adb_AttributeDesignator,
)
adb_PrimaryName_strategy = st.builds(
    adb_PrimaryName,
)
Interval_strategy = st.builds(
    Interval,
)
adb_ArrayComponentAssociation_strategy = st.builds(
    adb_ArrayComponentAssociation,
    box=
        st.booleans()
)
ArrayAggregate_strategy = st.builds(
    ArrayAggregate,
)
adb_NamedArrayAggregate_strategy = st.builds(
    adb_NamedArrayAggregate,
)
adb_PositionalArrayAggregate_strategy = st.builds(
    adb_PositionalArrayAggregate,
    othersBox=
        st.booleans()
)
adb_ArrayAggregate_strategy = st.builds(
    adb_ArrayAggregate,
)
adb_AncestorPart_strategy = st.builds(
    adb_AncestorPart,
)
ScalarConstraint_strategy = st.builds(
    ScalarConstraint,
)
adb_RangeConstraint_strategy = st.builds(
    adb_RangeConstraint,
)
adb_DeltaConstraint_strategy = st.builds(
    adb_DeltaConstraint,
)
adb_DigitsConstraint_strategy = st.builds(
    adb_DigitsConstraint,
)
adb_ScalarConstraint_strategy = st.builds(
    adb_ScalarConstraint,
)
adb_EObject_strategy = st.builds(
    adb_EObject,
)
adb_Factor_strategy = st.builds(
    adb_Factor,
    not_=
        st.booleans(),
    abs=
        st.booleans()
)
adb_Term_strategy = st.builds(
    adb_Term,
    multiplyingOperators=
        safe_text
)
adb_Interval_strategy = st.builds(
    adb_Interval,
)
adb_Membership_strategy = st.builds(
    adb_Membership,
    not_=
        st.booleans()
)
adb_Relation_strategy = st.builds(
    adb_Relation,
    relationalOperator=
        safe_text
)
ParameterEffectiveValue_strategy = st.builds(
    ParameterEffectiveValue,
)
AncestorPart_strategy = st.builds(
    AncestorPart,
)
DiscreteChoice_strategy = st.builds(
    DiscreteChoice,
)
adb_Range_strategy = st.builds(
    adb_Range,
)
ExplicitGenericActualParameter_strategy = st.builds(
    ExplicitGenericActualParameter,
)
EntryIndex_strategy = st.builds(
    EntryIndex,
)
adb_Primary_strategy = st.builds(
    adb_Primary,
)
adb_RealRangeSpecification_strategy = st.builds(
    adb_RealRangeSpecification,
)
adb_DiscreteChoice_strategy = st.builds(
    adb_DiscreteChoice,
)
adb_Variant_strategy = st.builds(
    adb_Variant,
)
adb_ComponentClause_strategy = st.builds(
    adb_ComponentClause,
    localName=
        safe_text
)
adb_ModClause_strategy = st.builds(
    adb_ModClause,
)
RealTypeDefinition_strategy = st.builds(
    RealTypeDefinition,
)
adb_FixedPointDefinition_strategy = st.builds(
    adb_FixedPointDefinition,
)
adb_FloatingPointDefinition_strategy = st.builds(
    adb_FloatingPointDefinition,
)
ComponentItem_strategy = st.builds(
    ComponentItem,
)
adb_VariantPart_strategy = st.builds(
    adb_VariantPart,
    name=
        safe_text
)
adb_OptVariantPart_strategy = st.builds(
    adb_OptVariantPart,
)
adb_ComponentItem_strategy = st.builds(
    adb_ComponentItem,
)
adb_ComponentList_strategy = st.builds(
    adb_ComponentList,
)
adb_SimpleExpression_strategy = st.builds(
    adb_SimpleExpression,
    unaryAddingOperator=
        safe_text,
    binaryAddingOperators=
        safe_text
)
IntegerTypeDefinition_strategy = st.builds(
    IntegerTypeDefinition,
)
adb_ModularTypeDefinition_strategy = st.builds(
    adb_ModularTypeDefinition,
)
adb_SignedIntegerTypeDefinition_strategy = st.builds(
    adb_SignedIntegerTypeDefinition,
)
adb_ParameterSpecification_strategy = st.builds(
    adb_ParameterSpecification,
)
ReturnSubtypeIndication_strategy = st.builds(
    ReturnSubtypeIndication,
)
ArrayIndexes_strategy = st.builds(
    ArrayIndexes,
)
adb_ConstrainedIndexes_strategy = st.builds(
    adb_ConstrainedIndexes,
)
adb_UnconstrainedIndexes_strategy = st.builds(
    adb_UnconstrainedIndexes,
)
adb_ComponentDefinition_strategy = st.builds(
    adb_ComponentDefinition,
    aliased=
        st.booleans()
)
adb_ArrayIndexes_strategy = st.builds(
    adb_ArrayIndexes,
)
NotNullAccessDefinition_strategy = st.builds(
    NotNullAccessDefinition,
)
AccessSpecification_strategy = st.builds(
    AccessSpecification,
)
adb_AccessToDataDefinition_strategy = st.builds(
    adb_AccessToDataDefinition,
    generalAccessModifier=
        safe_text
)
adb_AccessToSubprogramDefinition_strategy = st.builds(
    adb_AccessToSubprogramDefinition,
    protected=
        st.booleans()
)
adb_AccessSpecification_strategy = st.builds(
    adb_AccessSpecification,
)
adb_AccessToDataInstance_strategy = st.builds(
    adb_AccessToDataInstance,
    constant=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
adb_IntegerTypeDefinition_strategy = st.builds(
    adb_IntegerTypeDefinition,
)
adb_RealTypeDefinition_strategy = st.builds(
    adb_RealTypeDefinition,
)
adb_RecordTypeDefinition_strategy = st.builds(
    adb_RecordTypeDefinition,
    abstract=
        st.booleans(),
    limited=
        st.booleans(),
    tagged=
        st.booleans()
)
adb_DerivedTypeDefinition_strategy = st.builds(
    adb_DerivedTypeDefinition,
    limited=
        safe_text,
    abstract=
        safe_text
)
adb_EnumerationTypeDefinition_strategy = st.builds(
    adb_EnumerationTypeDefinition,
    enumerationliteralspecifications=
        safe_text
)
adb_NotNullAccessDefinition_strategy = st.builds(
    adb_NotNullAccessDefinition,
)
adb_DiscriminantSpecification_strategy = st.builds(
    adb_DiscriminantSpecification,
)
adb_RecordDefinition_strategy = st.builds(
    adb_RecordDefinition,
    null=
        safe_text
)
adb_RecordExtensionPart_strategy = st.builds(
    adb_RecordExtensionPart,
)
DiscriminantPart_strategy = st.builds(
    DiscriminantPart,
)
adb_UnknownDiscriminantPart_strategy = st.builds(
    adb_UnknownDiscriminantPart,
    box=
        st.booleans()
)
adb_ExplicitGenericActualParameter_strategy = st.builds(
    adb_ExplicitGenericActualParameter,
)
AbortStatement_strategy = st.builds(
    AbortStatement,
)
adb_TaskNames_strategy = st.builds(
    adb_TaskNames,
)
adb_EntryCallAlternative_strategy = st.builds(
    adb_EntryCallAlternative,
)
SelectAlternative_strategy = st.builds(
    SelectAlternative,
)
adb_DelayAlternative_strategy = st.builds(
    adb_DelayAlternative,
)
adb_AcceptAlternative_strategy = st.builds(
    adb_AcceptAlternative,
)
adb_GuardedAlternative_strategy = st.builds(
    adb_GuardedAlternative,
)
adb_SelectAlternative_strategy = st.builds(
    adb_SelectAlternative,
)
adb_Guard_strategy = st.builds(
    adb_Guard,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
adb_ConditionalEntryCall_strategy = st.builds(
    adb_ConditionalEntryCall,
)
adb_TimedEntryCall_strategy = st.builds(
    adb_TimedEntryCall,
)
adb_SelectiveAccept_strategy = st.builds(
    adb_SelectiveAccept,
)
adb_TriggeringStatement_strategy = st.builds(
    adb_TriggeringStatement,
)
adb_AbortablePart_strategy = st.builds(
    adb_AbortablePart,
)
adb_TriggeringAlternative_strategy = st.builds(
    adb_TriggeringAlternative,
)
adb_AsynchronousSelect_strategy = st.builds(
    adb_AsynchronousSelect,
)
adb_EntryIndexSpecification_strategy = st.builds(
    adb_EntryIndexSpecification,
    name=
        safe_text
)
adb_EntryBarrier_strategy = st.builds(
    adb_EntryBarrier,
)
adb_EntryBodyFormalPart_strategy = st.builds(
    adb_EntryBodyFormalPart,
)
adb_EntryIndex_strategy = st.builds(
    adb_EntryIndex,
)
adb_ProtectedOperationItem_strategy = st.builds(
    adb_ProtectedOperationItem,
)
adb_ReturnSubtypeIndication_strategy = st.builds(
    adb_ReturnSubtypeIndication,
)
TriggeringStatement_strategy = st.builds(
    TriggeringStatement,
)
adb_LoopParameterSpecification_strategy = st.builds(
    adb_LoopParameterSpecification,
    identifier=
        safe_text
)
adb_IterationScheme_strategy = st.builds(
    adb_IterationScheme,
)
CompoundStatement_strategy = st.builds(
    CompoundStatement,
)
adb_ExtendedReturnStatement_strategy = st.builds(
    adb_ExtendedReturnStatement,
    identifier=
        safe_text
)
adb_AcceptStatement_strategy = st.builds(
    adb_AcceptStatement,
    entryidentifier=
        safe_text
)
adb_SelectStatement_strategy = st.builds(
    adb_SelectStatement,
)
adb_LoopStatement_strategy = st.builds(
    adb_LoopStatement,
    sameName=
        safe_text,
    name=
        safe_text
)
adb_IfStatement_strategy = st.builds(
    adb_IfStatement,
)
adb_PragmaArgumentAssociation_strategy = st.builds(
    adb_PragmaArgumentAssociation,
    name=
        safe_text
)
adb_DiscreteChoiceList_strategy = st.builds(
    adb_DiscreteChoiceList,
)
adb_CaseStatementAlternative_strategy = st.builds(
    adb_CaseStatementAlternative,
)
adb_CaseStatement_strategy = st.builds(
    adb_CaseStatement,
)
ObjectDeclaration_strategy = st.builds(
    ObjectDeclaration,
)
adb_DataInstanceDeclaration_strategy = st.builds(
    adb_DataInstanceDeclaration,
    constant=
        st.booleans(),
    aliased=
        st.booleans()
)
adb_GenericAssociation_strategy = st.builds(
    adb_GenericAssociation,
    selectorName=
        safe_text
)
adb_FormalPackageAssociation_strategy = st.builds(
    adb_FormalPackageAssociation,
    genericFormalParameterSelectorName=
        safe_text
)
adb_FormalPackageActualPart_strategy = st.builds(
    adb_FormalPackageActualPart,
    box=
        st.booleans()
)
adb_SubprogramDefault_strategy = st.builds(
    adb_SubprogramDefault,
    defaultName=
        safe_text
)
adb_Expression_strategy = st.builds(
    adb_Expression,
    booleanOperator=
        safe_text
)
adb_AnonymousAccessDefinition_strategy = st.builds(
    adb_AnonymousAccessDefinition,
)
adb_OptNullExclusion_strategy = st.builds(
    adb_OptNullExclusion,
    not_null=
        safe_text
)
adb_SingleProtectedDeclaration_strategy = st.builds(
    adb_SingleProtectedDeclaration,
    name=
        safe_text
)
adb_Mode_strategy = st.builds(
    adb_Mode,
    out=
        st.booleans(),
    in_=
        st.booleans()
)
adb_DefiningIdentifierList_strategy = st.builds(
    adb_DefiningIdentifierList,
    name=
        safe_text
)
FormalTypeDefinition_strategy = st.builds(
    FormalTypeDefinition,
)
adb_InterfaceTypeDefinition_strategy = st.builds(
    adb_InterfaceTypeDefinition,
    synchro=
        st.booleans(),
    protected=
        st.booleans(),
    task=
        st.booleans(),
    limited=
        st.booleans()
)
adb_ArrayTypeDefinition_strategy = st.builds(
    adb_ArrayTypeDefinition,
)
adb_AccessTypeDefinition_strategy = st.builds(
    adb_AccessTypeDefinition,
)
adb_FormalDerivedTypeDefinition_strategy = st.builds(
    adb_FormalDerivedTypeDefinition,
    absract=
        safe_text,
    limited=
        st.booleans(),
    synchronized=
        st.booleans()
)
GenericFormalParameterDeclaration_strategy = st.builds(
    GenericFormalParameterDeclaration,
)
adb_FormalTypeDeclaration_strategy = st.builds(
    adb_FormalTypeDeclaration,
    identifier=
        safe_text
)
adb_FormalPackageDeclaration_strategy = st.builds(
    adb_FormalPackageDeclaration,
    name=
        safe_text,
    genericPackageName=
        safe_text
)
adb_FormalSubprogramDeclaration_strategy = st.builds(
    adb_FormalSubprogramDeclaration,
    abstract=
        safe_text
)
adb_FormalObjectDeclaration_strategy = st.builds(
    adb_FormalObjectDeclaration,
)
adb_FormalPrivateTypeDefinition_strategy = st.builds(
    adb_FormalPrivateTypeDefinition,
    limited=
        st.booleans(),
    abstract=
        st.booleans(),
    tagged=
        st.booleans()
)
adb_FormalTypeDefinition_strategy = st.builds(
    adb_FormalTypeDefinition,
)
adb_ExceptionHandler_strategy = st.builds(
    adb_ExceptionHandler,
    name=
        safe_text
)
adb_GenericItem_strategy = st.builds(
    adb_GenericItem,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
adb_SimpleReturnStatement_strategy = st.builds(
    adb_SimpleReturnStatement,
)
adb_GotoStatement_strategy = st.builds(
    adb_GotoStatement,
    labelId=
        safe_text
)
adb_AbortStatement_strategy = st.builds(
    adb_AbortStatement,
)
adb_ExitStatement_strategy = st.builds(
    adb_ExitStatement,
)
adb_AssignmentStatement_strategy = st.builds(
    adb_AssignmentStatement,
)
adb_DelayStatement_strategy = st.builds(
    adb_DelayStatement,
    until=
        safe_text
)
adb_ProcedureOrEntryCallStatement_strategy = st.builds(
    adb_ProcedureOrEntryCallStatement,
)
adb_RaiseStatement_strategy = st.builds(
    adb_RaiseStatement,
)
adb_RequeueStatement_strategy = st.builds(
    adb_RequeueStatement,
    abort=
        st.booleans()
)
adb_NullStatement_strategy = st.builds(
    adb_NullStatement,
    null=
        st.booleans()
)
Statement_strategy = st.builds(
    Statement,
)
adb_CompoundStatement_strategy = st.builds(
    adb_CompoundStatement,
)
adb_SimpleStatement_strategy = st.builds(
    adb_SimpleStatement,
)
adb_Statement_strategy = st.builds(
    adb_Statement,
)
adb_LabelisableStatement_strategy = st.builds(
    adb_LabelisableStatement,
)
AbortablePart_strategy = st.builds(
    AbortablePart,
)
HandledSequenceOfStatements_strategy = st.builds(
    HandledSequenceOfStatements,
)
adb_SequenceOfStatements_strategy = st.builds(
    adb_SequenceOfStatements,
)
adb_Label_strategy = st.builds(
    adb_Label,
    identifier=
        safe_text
)
Body_strategy = st.builds(
    Body,
)
adb_ProperBody_strategy = st.builds(
    adb_ProperBody,
)
adb_BodyStub_strategy = st.builds(
    adb_BodyStub,
    name=
        safe_text
)
ProtectedElementDeclaration_strategy = st.builds(
    ProtectedElementDeclaration,
)
adb_ComponentDeclaration_strategy = st.builds(
    adb_ComponentDeclaration,
)
adb_ProtectedOperationDeclaration_strategy = st.builds(
    adb_ProtectedOperationDeclaration,
)
adb_ProtectedElementDeclaration_strategy = st.builds(
    adb_ProtectedElementDeclaration,
)
adb_ProtectedDefinition_strategy = st.builds(
    adb_ProtectedDefinition,
)
adb_FormalPart_strategy = st.builds(
    adb_FormalPart,
)
adb_DiscreteSubtypeDefinition_strategy = st.builds(
    adb_DiscreteSubtypeDefinition,
)
adb_Name_strategy = st.builds(
    adb_Name,
    name=
        safe_text
)
adb_ExceptionChoice_strategy = st.builds(
    adb_ExceptionChoice,
    others=
        st.booleans()
)
adb_ParameterAndResultProfile_strategy = st.builds(
    adb_ParameterAndResultProfile,
)
SubprogramSpecification_strategy = st.builds(
    SubprogramSpecification,
)
adb_FunctionSpecification_strategy = st.builds(
    adb_FunctionSpecification,
)
adb_ProcedureSpecification_strategy = st.builds(
    adb_ProcedureSpecification,
)
BodyStub_strategy = st.builds(
    BodyStub,
)
adb_TaskBodyStub_strategy = st.builds(
    adb_TaskBodyStub,
)
adb_PackageBodyStub_strategy = st.builds(
    adb_PackageBodyStub,
)
adb_ProtectedBodyStub_strategy = st.builds(
    adb_ProtectedBodyStub,
)
NewTypeDeclaration_strategy = st.builds(
    NewTypeDeclaration,
)
adb_FullTypeDeclaration_strategy = st.builds(
    adb_FullTypeDeclaration,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
adb_SubtypeDeclaration_strategy = st.builds(
    adb_SubtypeDeclaration,
)
adb_NewTypeDeclaration_strategy = st.builds(
    adb_NewTypeDeclaration,
)
adb_TaskDefinition_strategy = st.builds(
    adb_TaskDefinition,
)
adb_InterfaceList_strategy = st.builds(
    adb_InterfaceList,
)
adb_KnownDiscriminantPart_strategy = st.builds(
    adb_KnownDiscriminantPart,
)
DeclarativeItem_strategy = st.builds(
    DeclarativeItem,
)
adb_Body_strategy = st.builds(
    adb_Body,
)
ProtectedOperationDeclaration_strategy = st.builds(
    ProtectedOperationDeclaration,
)
TaskItem_strategy = st.builds(
    TaskItem,
)
adb_EntryDeclaration_strategy = st.builds(
    adb_EntryDeclaration,
    name=
        safe_text
)
adb_TaskItem_strategy = st.builds(
    adb_TaskItem,
)
adb_SubtypeIndication_strategy = st.builds(
    adb_SubtypeIndication,
    subtypeMark=
        safe_text
)
adb_PrivateExtensionDeclaration_strategy = st.builds(
    adb_PrivateExtensionDeclaration,
    limited=
        st.booleans(),
    abstract=
        st.booleans(),
    synchronized=
        st.booleans()
)
adb_PrivateTypeDeclaration_strategy = st.builds(
    adb_PrivateTypeDeclaration,
    abstract=
        st.booleans(),
    tagged=
        st.booleans(),
    limited=
        st.booleans()
)
adb_DiscriminantPart_strategy = st.builds(
    adb_DiscriminantPart,
)
adb_IncompleteTypeDeclaration_strategy = st.builds(
    adb_IncompleteTypeDeclaration,
    tagged=
        st.booleans()
)
adb_TypeDefinition_strategy = st.builds(
    adb_TypeDefinition,
)
FullTypeDeclaration_strategy = st.builds(
    FullTypeDeclaration,
)
adb_ProtectedTypeDeclaration_strategy = st.builds(
    adb_ProtectedTypeDeclaration,
)
adb_FullDataTypeDeclaration_strategy = st.builds(
    adb_FullDataTypeDeclaration,
)
adb_PackageSpecification_strategy = st.builds(
    adb_PackageSpecification,
    endname=
        safe_text
)
LibrarySpecification_strategy = st.builds(
    LibrarySpecification,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
adb_Renaming_strategy = st.builds(
    adb_Renaming,
    renamed=
        safe_text
)
adb_PackageDefinition_strategy = st.builds(
    adb_PackageDefinition,
)
BasicDeclaration_strategy = st.builds(
    BasicDeclaration,
)
adb_ExceptionDeclaration_strategy = st.builds(
    adb_ExceptionDeclaration,
)
adb_NumberDeclaration_strategy = st.builds(
    adb_NumberDeclaration,
)
adb_ObjectDeclaration_strategy = st.builds(
    adb_ObjectDeclaration,
)
adb_TaskDeclaration_strategy = st.builds(
    adb_TaskDeclaration,
    name=
        safe_text
)
adb_TypeDeclaration_strategy = st.builds(
    adb_TypeDeclaration,
    name=
        safe_text
)
LibraryUnitSpecification_strategy = st.builds(
    LibraryUnitSpecification,
)
adb_PackageDeclaration_strategy = st.builds(
    adb_PackageDeclaration,
    name=
        safe_text
)
adb_LibraryUnitSpecification_strategy = st.builds(
    adb_LibraryUnitSpecification,
)
Unit_strategy = st.builds(
    Unit,
)
adb_SeparateSubunit_strategy = st.builds(
    adb_SeparateSubunit,
    parentUnitName=
        safe_text
)
adb_HandledSequenceOfStatements_strategy = st.builds(
    adb_HandledSequenceOfStatements,
)
adb_DeclarativeItem_strategy = st.builds(
    adb_DeclarativeItem,
)
adb_DeclarativeBlock_strategy = st.builds(
    adb_DeclarativeBlock,
)
adb_SubprogramSpecification_strategy = st.builds(
    adb_SubprogramSpecification,
)
ProtectedOperationItem_strategy = st.builds(
    ProtectedOperationItem,
)
adb_SubprogramDeclaration_strategy = st.builds(
    adb_SubprogramDeclaration,
    renamedName=
        safe_text,
    abstract=
        st.booleans(),
    null=
        st.booleans()
)
ProperBody_strategy = st.builds(
    ProperBody,
)
adb_ProtectedBody_strategy = st.builds(
    adb_ProtectedBody,
    identifier=
        safe_text,
    idTask=
        safe_text
)
DeclarativeBlock_strategy = st.builds(
    DeclarativeBlock,
)
adb_TaskBody_strategy = st.builds(
    adb_TaskBody,
)
adb_EntryBody_strategy = st.builds(
    adb_EntryBody,
    endid=
        safe_text
)
adb_PackageBody_strategy = st.builds(
    adb_PackageBody,
)
adb_BlockStatement_strategy = st.builds(
    adb_BlockStatement,
    blockStatementIdentifier=
        safe_text
)
adb_SubprogramBody_strategy = st.builds(
    adb_SubprogramBody,
    endname=
        safe_text
)
adb_BasicDeclarativeItem_strategy = st.builds(
    adb_BasicDeclarativeItem,
)
adb_GenericActualPart_strategy = st.builds(
    adb_GenericActualPart,
)
adb_OverridingIndicator_strategy = st.builds(
    adb_OverridingIndicator,
    not_=
        st.booleans()
)
adb_GenericInstantiation_strategy = st.builds(
    adb_GenericInstantiation,
    genericName=
        safe_text,
    name=
        safe_text
)
adb_LibrarySpecification_strategy = st.builds(
    adb_LibrarySpecification,
)
adb_GenericItems_strategy = st.builds(
    adb_GenericItems,
)
adb_GenericDeclaration_strategy = st.builds(
    adb_GenericDeclaration,
)
UseClause_strategy = st.builds(
    UseClause,
)
adb_UseTypeClause_strategy = st.builds(
    adb_UseTypeClause,
    useTypeRefs=
        safe_text,
    typesNames=
        safe_text
)
adb_UsePackageClause_strategy = st.builds(
    adb_UsePackageClause,
)
GenericItem_strategy = st.builds(
    GenericItem,
)
adb_GenericFormalParameterDeclaration_strategy = st.builds(
    adb_GenericFormalParameterDeclaration,
)
BasicDeclarativeItem_strategy = st.builds(
    BasicDeclarativeItem,
)
adb_BasicDeclaration_strategy = st.builds(
    adb_BasicDeclaration,
)
adb_AspectClause_strategy = st.builds(
    adb_AspectClause,
    name=
        safe_text
)
adb_LibraryUnitDeclaration_strategy = st.builds(
    adb_LibraryUnitDeclaration,
    private=
        st.booleans()
)
ContextItem_strategy = st.builds(
    ContextItem,
)
adb_UseClause_strategy = st.builds(
    adb_UseClause,
)
adb_WithClause_strategy = st.builds(
    adb_WithClause,
    limited=
        st.booleans(),
    private=
        st.booleans()
)
adb_ContextItem_strategy = st.builds(
    adb_ContextItem,
)
adb_Pragma_strategy = st.builds(
    adb_Pragma,
    name=
        safe_text
)
adb_Unit_strategy = st.builds(
    adb_Unit,
)
adb_ContextClause_strategy = st.builds(
    adb_ContextClause,
)
adb_CompilationUnit_strategy = st.builds(
    adb_CompilationUnit,
)
adb_Compilation_strategy = st.builds(
    adb_Compilation,
)

@given(instance=RecordComponentAssociation_strategy)
@settings(max_examples=50)
def test_recordcomponentassociation_instantiation(instance):
    assert isinstance(instance, RecordComponentAssociation)

@given(instance=adb_UninitializedComponents_strategy)
@settings(max_examples=50)
def test_adb_uninitializedcomponents_instantiation(instance):
    assert isinstance(instance, adb_UninitializedComponents)



@given(instance=adb_UninitializedComponents_strategy)
def test_adb_uninitializedcomponents_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb_InitializedComponents_strategy)
@settings(max_examples=50)
def test_adb_initializedcomponents_instantiation(instance):
    assert isinstance(instance, adb_InitializedComponents)

@given(instance=adb_ParameterAssociation_strategy)
@settings(max_examples=50)
def test_adb_parameterassociation_instantiation(instance):
    assert isinstance(instance, adb_ParameterAssociation)



@given(instance=adb_ParameterAssociation_strategy)
def test_adb_parameterassociation_selectorName_setter(instance):
    original = instance.selectorName
    instance.selectorName = original
    assert instance.selectorName == original

@given(instance=adb_RecordComponentAssociation_strategy)
@settings(max_examples=50)
def test_adb_recordcomponentassociation_instantiation(instance):
    assert isinstance(instance, adb_RecordComponentAssociation)

@given(instance=RecordAggregate_strategy)
@settings(max_examples=50)
def test_recordaggregate_instantiation(instance):
    assert isinstance(instance, RecordAggregate)

@given(instance=adb_RecordComponentAssociationList_strategy)
@settings(max_examples=50)
def test_adb_recordcomponentassociationlist_instantiation(instance):
    assert isinstance(instance, adb_RecordComponentAssociationList)



@given(instance=adb_RecordComponentAssociationList_strategy)
def test_adb_recordcomponentassociationlist_nullRecord_setter(instance):
    original = instance.nullRecord
    instance.nullRecord = original
    assert instance.nullRecord == original

@given(instance=Aggregate_strategy)
@settings(max_examples=50)
def test_aggregate_instantiation(instance):
    assert isinstance(instance, Aggregate)

@given(instance=adb_ExtensionAggregate_strategy)
@settings(max_examples=50)
def test_adb_extensionaggregate_instantiation(instance):
    assert isinstance(instance, adb_ExtensionAggregate)

@given(instance=adb_RecordAggregate_strategy)
@settings(max_examples=50)
def test_adb_recordaggregate_instantiation(instance):
    assert isinstance(instance, adb_RecordAggregate)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ParenthesizedExpression)

@given(instance=adb_Aggregate_strategy)
@settings(max_examples=50)
def test_adb_aggregate_instantiation(instance):
    assert isinstance(instance, adb_Aggregate)

@given(instance=adb_ComponentChoiceList_strategy)
@settings(max_examples=50)
def test_adb_componentchoicelist_instantiation(instance):
    assert isinstance(instance, adb_ComponentChoiceList)



@given(instance=adb_ComponentChoiceList_strategy)
def test_adb_componentchoicelist_others_setter(instance):
    original = instance.others
    instance.others = original
    assert instance.others == original



@given(instance=adb_ComponentChoiceList_strategy)
def test_adb_componentchoicelist_componentSelectorName_setter(instance):
    original = instance.componentSelectorName
    instance.componentSelectorName = original
    assert instance.componentSelectorName == original

@given(instance=adb_DiscriminantSelectors_strategy)
@settings(max_examples=50)
def test_adb_discriminantselectors_instantiation(instance):
    assert isinstance(instance, adb_DiscriminantSelectors)



@given(instance=adb_DiscriminantSelectors_strategy)
def test_adb_discriminantselectors_discriminantSelectorName_setter(instance):
    original = instance.discriminantSelectorName
    instance.discriminantSelectorName = original
    assert instance.discriminantSelectorName == original

@given(instance=adb_DiscriminantAssociation_strategy)
@settings(max_examples=50)
def test_adb_discriminantassociation_instantiation(instance):
    assert isinstance(instance, adb_DiscriminantAssociation)

@given(instance=CompositeConstraint_strategy)
@settings(max_examples=50)
def test_compositeconstraint_instantiation(instance):
    assert isinstance(instance, CompositeConstraint)

@given(instance=adb_IndexConstraint_strategy)
@settings(max_examples=50)
def test_adb_indexconstraint_instantiation(instance):
    assert isinstance(instance, adb_IndexConstraint)

@given(instance=adb_DiscriminantConstraint_strategy)
@settings(max_examples=50)
def test_adb_discriminantconstraint_instantiation(instance):
    assert isinstance(instance, adb_DiscriminantConstraint)

@given(instance=adb_CompositeConstraint_strategy)
@settings(max_examples=50)
def test_adb_compositeconstraint_instantiation(instance):
    assert isinstance(instance, adb_CompositeConstraint)

@given(instance=adb_OptConstraint_strategy)
@settings(max_examples=50)
def test_adb_optconstraint_instantiation(instance):
    assert isinstance(instance, adb_OptConstraint)

@given(instance=DiscreteRange_strategy)
@settings(max_examples=50)
def test_discreterange_instantiation(instance):
    assert isinstance(instance, DiscreteRange)

@given(instance=DiscreteSubtypeDefinition_strategy)
@settings(max_examples=50)
def test_discretesubtypedefinition_instantiation(instance):
    assert isinstance(instance, DiscreteSubtypeDefinition)

@given(instance=adb_DiscreteRange_strategy)
@settings(max_examples=50)
def test_adb_discreterange_instantiation(instance):
    assert isinstance(instance, adb_DiscreteRange)

@given(instance=adb_Qualifier_strategy)
@settings(max_examples=50)
def test_adb_qualifier_instantiation(instance):
    assert isinstance(instance, adb_Qualifier)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=adb_QualifiedName_strategy)
@settings(max_examples=50)
def test_adb_qualifiedname_instantiation(instance):
    assert isinstance(instance, adb_QualifiedName)

@given(instance=adb_StringLiteral_strategy)
@settings(max_examples=50)
def test_adb_stringliteral_instantiation(instance):
    assert isinstance(instance, adb_StringLiteral)



@given(instance=adb_StringLiteral_strategy)
def test_adb_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adb_Allocator_strategy)
@settings(max_examples=50)
def test_adb_allocator_instantiation(instance):
    assert isinstance(instance, adb_Allocator)

@given(instance=adb_Null_strategy)
@settings(max_examples=50)
def test_adb_null_instantiation(instance):
    assert isinstance(instance, adb_Null)



@given(instance=adb_Null_strategy)
def test_adb_null_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adb_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_adb_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, adb_ParenthesizedExpression)

@given(instance=adb_NumericLiteral_strategy)
@settings(max_examples=50)
def test_adb_numericliteral_instantiation(instance):
    assert isinstance(instance, adb_NumericLiteral)



@given(instance=adb_NumericLiteral_strategy)
def test_adb_numericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Range_strategy)
@settings(max_examples=50)
def test_range_instantiation(instance):
    assert isinstance(instance, Range)

@given(instance=adb_ExplicitRange_strategy)
@settings(max_examples=50)
def test_adb_explicitrange_instantiation(instance):
    assert isinstance(instance, adb_ExplicitRange)

@given(instance=adb_EntityRange_strategy)
@settings(max_examples=50)
def test_adb_entityrange_instantiation(instance):
    assert isinstance(instance, adb_EntityRange)

@given(instance=RangeConstraint_strategy)
@settings(max_examples=50)
def test_rangeconstraint_instantiation(instance):
    assert isinstance(instance, RangeConstraint)

@given(instance=adb_ParameterEffectiveValue_strategy)
@settings(max_examples=50)
def test_adb_parametereffectivevalue_instantiation(instance):
    assert isinstance(instance, adb_ParameterEffectiveValue)

@given(instance=adb_AttributeDesignator_strategy)
@settings(max_examples=50)
def test_adb_attributedesignator_instantiation(instance):
    assert isinstance(instance, adb_AttributeDesignator)

@given(instance=adb_PrimaryName_strategy)
@settings(max_examples=50)
def test_adb_primaryname_instantiation(instance):
    assert isinstance(instance, adb_PrimaryName)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=adb_ArrayComponentAssociation_strategy)
@settings(max_examples=50)
def test_adb_arraycomponentassociation_instantiation(instance):
    assert isinstance(instance, adb_ArrayComponentAssociation)



@given(instance=adb_ArrayComponentAssociation_strategy)
def test_adb_arraycomponentassociation_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=ArrayAggregate_strategy)
@settings(max_examples=50)
def test_arrayaggregate_instantiation(instance):
    assert isinstance(instance, ArrayAggregate)

@given(instance=adb_NamedArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb_namedarrayaggregate_instantiation(instance):
    assert isinstance(instance, adb_NamedArrayAggregate)

@given(instance=adb_PositionalArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb_positionalarrayaggregate_instantiation(instance):
    assert isinstance(instance, adb_PositionalArrayAggregate)



@given(instance=adb_PositionalArrayAggregate_strategy)
def test_adb_positionalarrayaggregate_othersBox_setter(instance):
    original = instance.othersBox
    instance.othersBox = original
    assert instance.othersBox == original

@given(instance=adb_ArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb_arrayaggregate_instantiation(instance):
    assert isinstance(instance, adb_ArrayAggregate)

@given(instance=adb_AncestorPart_strategy)
@settings(max_examples=50)
def test_adb_ancestorpart_instantiation(instance):
    assert isinstance(instance, adb_AncestorPart)

@given(instance=ScalarConstraint_strategy)
@settings(max_examples=50)
def test_scalarconstraint_instantiation(instance):
    assert isinstance(instance, ScalarConstraint)

@given(instance=adb_RangeConstraint_strategy)
@settings(max_examples=50)
def test_adb_rangeconstraint_instantiation(instance):
    assert isinstance(instance, adb_RangeConstraint)

@given(instance=adb_DeltaConstraint_strategy)
@settings(max_examples=50)
def test_adb_deltaconstraint_instantiation(instance):
    assert isinstance(instance, adb_DeltaConstraint)

@given(instance=adb_DigitsConstraint_strategy)
@settings(max_examples=50)
def test_adb_digitsconstraint_instantiation(instance):
    assert isinstance(instance, adb_DigitsConstraint)

@given(instance=adb_ScalarConstraint_strategy)
@settings(max_examples=50)
def test_adb_scalarconstraint_instantiation(instance):
    assert isinstance(instance, adb_ScalarConstraint)

@given(instance=adb_EObject_strategy)
@settings(max_examples=50)
def test_adb_eobject_instantiation(instance):
    assert isinstance(instance, adb_EObject)

@given(instance=adb_Factor_strategy)
@settings(max_examples=50)
def test_adb_factor_instantiation(instance):
    assert isinstance(instance, adb_Factor)



@given(instance=adb_Factor_strategy)
def test_adb_factor_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original



@given(instance=adb_Factor_strategy)
def test_adb_factor_abs_setter(instance):
    original = instance.abs
    instance.abs = original
    assert instance.abs == original

@given(instance=adb_Term_strategy)
@settings(max_examples=50)
def test_adb_term_instantiation(instance):
    assert isinstance(instance, adb_Term)



@given(instance=adb_Term_strategy)
def test_adb_term_multiplyingOperators_setter(instance):
    original = instance.multiplyingOperators
    instance.multiplyingOperators = original
    assert instance.multiplyingOperators == original

@given(instance=adb_Interval_strategy)
@settings(max_examples=50)
def test_adb_interval_instantiation(instance):
    assert isinstance(instance, adb_Interval)

@given(instance=adb_Membership_strategy)
@settings(max_examples=50)
def test_adb_membership_instantiation(instance):
    assert isinstance(instance, adb_Membership)



@given(instance=adb_Membership_strategy)
def test_adb_membership_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=adb_Relation_strategy)
@settings(max_examples=50)
def test_adb_relation_instantiation(instance):
    assert isinstance(instance, adb_Relation)



@given(instance=adb_Relation_strategy)
def test_adb_relation_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=ParameterEffectiveValue_strategy)
@settings(max_examples=50)
def test_parametereffectivevalue_instantiation(instance):
    assert isinstance(instance, ParameterEffectiveValue)

@given(instance=AncestorPart_strategy)
@settings(max_examples=50)
def test_ancestorpart_instantiation(instance):
    assert isinstance(instance, AncestorPart)

@given(instance=DiscreteChoice_strategy)
@settings(max_examples=50)
def test_discretechoice_instantiation(instance):
    assert isinstance(instance, DiscreteChoice)

@given(instance=adb_Range_strategy)
@settings(max_examples=50)
def test_adb_range_instantiation(instance):
    assert isinstance(instance, adb_Range)

@given(instance=ExplicitGenericActualParameter_strategy)
@settings(max_examples=50)
def test_explicitgenericactualparameter_instantiation(instance):
    assert isinstance(instance, ExplicitGenericActualParameter)

@given(instance=EntryIndex_strategy)
@settings(max_examples=50)
def test_entryindex_instantiation(instance):
    assert isinstance(instance, EntryIndex)

@given(instance=adb_Primary_strategy)
@settings(max_examples=50)
def test_adb_primary_instantiation(instance):
    assert isinstance(instance, adb_Primary)

@given(instance=adb_RealRangeSpecification_strategy)
@settings(max_examples=50)
def test_adb_realrangespecification_instantiation(instance):
    assert isinstance(instance, adb_RealRangeSpecification)

@given(instance=adb_DiscreteChoice_strategy)
@settings(max_examples=50)
def test_adb_discretechoice_instantiation(instance):
    assert isinstance(instance, adb_DiscreteChoice)

@given(instance=adb_Variant_strategy)
@settings(max_examples=50)
def test_adb_variant_instantiation(instance):
    assert isinstance(instance, adb_Variant)

@given(instance=adb_ComponentClause_strategy)
@settings(max_examples=50)
def test_adb_componentclause_instantiation(instance):
    assert isinstance(instance, adb_ComponentClause)



@given(instance=adb_ComponentClause_strategy)
def test_adb_componentclause_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original

@given(instance=adb_ModClause_strategy)
@settings(max_examples=50)
def test_adb_modclause_instantiation(instance):
    assert isinstance(instance, adb_ModClause)

@given(instance=RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_realtypedefinition_instantiation(instance):
    assert isinstance(instance, RealTypeDefinition)

@given(instance=adb_FixedPointDefinition_strategy)
@settings(max_examples=50)
def test_adb_fixedpointdefinition_instantiation(instance):
    assert isinstance(instance, adb_FixedPointDefinition)

@given(instance=adb_FloatingPointDefinition_strategy)
@settings(max_examples=50)
def test_adb_floatingpointdefinition_instantiation(instance):
    assert isinstance(instance, adb_FloatingPointDefinition)

@given(instance=ComponentItem_strategy)
@settings(max_examples=50)
def test_componentitem_instantiation(instance):
    assert isinstance(instance, ComponentItem)

@given(instance=adb_VariantPart_strategy)
@settings(max_examples=50)
def test_adb_variantpart_instantiation(instance):
    assert isinstance(instance, adb_VariantPart)



@given(instance=adb_VariantPart_strategy)
def test_adb_variantpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_OptVariantPart_strategy)
@settings(max_examples=50)
def test_adb_optvariantpart_instantiation(instance):
    assert isinstance(instance, adb_OptVariantPart)

@given(instance=adb_ComponentItem_strategy)
@settings(max_examples=50)
def test_adb_componentitem_instantiation(instance):
    assert isinstance(instance, adb_ComponentItem)

@given(instance=adb_ComponentList_strategy)
@settings(max_examples=50)
def test_adb_componentlist_instantiation(instance):
    assert isinstance(instance, adb_ComponentList)

@given(instance=adb_SimpleExpression_strategy)
@settings(max_examples=50)
def test_adb_simpleexpression_instantiation(instance):
    assert isinstance(instance, adb_SimpleExpression)



@given(instance=adb_SimpleExpression_strategy)
def test_adb_simpleexpression_unaryAddingOperator_setter(instance):
    original = instance.unaryAddingOperator
    instance.unaryAddingOperator = original
    assert instance.unaryAddingOperator == original



@given(instance=adb_SimpleExpression_strategy)
def test_adb_simpleexpression_binaryAddingOperators_setter(instance):
    original = instance.binaryAddingOperators
    instance.binaryAddingOperators = original
    assert instance.binaryAddingOperators == original

@given(instance=IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_integertypedefinition_instantiation(instance):
    assert isinstance(instance, IntegerTypeDefinition)

@given(instance=adb_ModularTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_modulartypedefinition_instantiation(instance):
    assert isinstance(instance, adb_ModularTypeDefinition)

@given(instance=adb_SignedIntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_signedintegertypedefinition_instantiation(instance):
    assert isinstance(instance, adb_SignedIntegerTypeDefinition)

@given(instance=adb_ParameterSpecification_strategy)
@settings(max_examples=50)
def test_adb_parameterspecification_instantiation(instance):
    assert isinstance(instance, adb_ParameterSpecification)

@given(instance=ReturnSubtypeIndication_strategy)
@settings(max_examples=50)
def test_returnsubtypeindication_instantiation(instance):
    assert isinstance(instance, ReturnSubtypeIndication)

@given(instance=ArrayIndexes_strategy)
@settings(max_examples=50)
def test_arrayindexes_instantiation(instance):
    assert isinstance(instance, ArrayIndexes)

@given(instance=adb_ConstrainedIndexes_strategy)
@settings(max_examples=50)
def test_adb_constrainedindexes_instantiation(instance):
    assert isinstance(instance, adb_ConstrainedIndexes)

@given(instance=adb_UnconstrainedIndexes_strategy)
@settings(max_examples=50)
def test_adb_unconstrainedindexes_instantiation(instance):
    assert isinstance(instance, adb_UnconstrainedIndexes)

@given(instance=adb_ComponentDefinition_strategy)
@settings(max_examples=50)
def test_adb_componentdefinition_instantiation(instance):
    assert isinstance(instance, adb_ComponentDefinition)



@given(instance=adb_ComponentDefinition_strategy)
def test_adb_componentdefinition_aliased_setter(instance):
    original = instance.aliased
    instance.aliased = original
    assert instance.aliased == original

@given(instance=adb_ArrayIndexes_strategy)
@settings(max_examples=50)
def test_adb_arrayindexes_instantiation(instance):
    assert isinstance(instance, adb_ArrayIndexes)

@given(instance=NotNullAccessDefinition_strategy)
@settings(max_examples=50)
def test_notnullaccessdefinition_instantiation(instance):
    assert isinstance(instance, NotNullAccessDefinition)

@given(instance=AccessSpecification_strategy)
@settings(max_examples=50)
def test_accessspecification_instantiation(instance):
    assert isinstance(instance, AccessSpecification)

@given(instance=adb_AccessToDataDefinition_strategy)
@settings(max_examples=50)
def test_adb_accesstodatadefinition_instantiation(instance):
    assert isinstance(instance, adb_AccessToDataDefinition)



@given(instance=adb_AccessToDataDefinition_strategy)
def test_adb_accesstodatadefinition_generalAccessModifier_setter(instance):
    original = instance.generalAccessModifier
    instance.generalAccessModifier = original
    assert instance.generalAccessModifier == original

@given(instance=adb_AccessToSubprogramDefinition_strategy)
@settings(max_examples=50)
def test_adb_accesstosubprogramdefinition_instantiation(instance):
    assert isinstance(instance, adb_AccessToSubprogramDefinition)



@given(instance=adb_AccessToSubprogramDefinition_strategy)
def test_adb_accesstosubprogramdefinition_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=adb_AccessSpecification_strategy)
@settings(max_examples=50)
def test_adb_accessspecification_instantiation(instance):
    assert isinstance(instance, adb_AccessSpecification)

@given(instance=adb_AccessToDataInstance_strategy)
@settings(max_examples=50)
def test_adb_accesstodatainstance_instantiation(instance):
    assert isinstance(instance, adb_AccessToDataInstance)



@given(instance=adb_AccessToDataInstance_strategy)
def test_adb_accesstodatainstance_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=adb_IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_integertypedefinition_instantiation(instance):
    assert isinstance(instance, adb_IntegerTypeDefinition)

@given(instance=adb_RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_realtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_RealTypeDefinition)

@given(instance=adb_RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_recordtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_RecordTypeDefinition)



@given(instance=adb_RecordTypeDefinition_strategy)
def test_adb_recordtypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=adb_RecordTypeDefinition_strategy)
def test_adb_recordtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_RecordTypeDefinition_strategy)
def test_adb_recordtypedefinition_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb_DerivedTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_derivedtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_DerivedTypeDefinition)



@given(instance=adb_DerivedTypeDefinition_strategy)
def test_adb_derivedtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_DerivedTypeDefinition_strategy)
def test_adb_derivedtypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb_EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_EnumerationTypeDefinition)



@given(instance=adb_EnumerationTypeDefinition_strategy)
def test_adb_enumerationtypedefinition_enumerationliteralspecifications_setter(instance):
    original = instance.enumerationliteralspecifications
    instance.enumerationliteralspecifications = original
    assert instance.enumerationliteralspecifications == original

@given(instance=adb_NotNullAccessDefinition_strategy)
@settings(max_examples=50)
def test_adb_notnullaccessdefinition_instantiation(instance):
    assert isinstance(instance, adb_NotNullAccessDefinition)

@given(instance=adb_DiscriminantSpecification_strategy)
@settings(max_examples=50)
def test_adb_discriminantspecification_instantiation(instance):
    assert isinstance(instance, adb_DiscriminantSpecification)

@given(instance=adb_RecordDefinition_strategy)
@settings(max_examples=50)
def test_adb_recorddefinition_instantiation(instance):
    assert isinstance(instance, adb_RecordDefinition)



@given(instance=adb_RecordDefinition_strategy)
def test_adb_recorddefinition_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=adb_RecordExtensionPart_strategy)
@settings(max_examples=50)
def test_adb_recordextensionpart_instantiation(instance):
    assert isinstance(instance, adb_RecordExtensionPart)

@given(instance=DiscriminantPart_strategy)
@settings(max_examples=50)
def test_discriminantpart_instantiation(instance):
    assert isinstance(instance, DiscriminantPart)

@given(instance=adb_UnknownDiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb_unknowndiscriminantpart_instantiation(instance):
    assert isinstance(instance, adb_UnknownDiscriminantPart)



@given(instance=adb_UnknownDiscriminantPart_strategy)
def test_adb_unknowndiscriminantpart_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb_ExplicitGenericActualParameter_strategy)
@settings(max_examples=50)
def test_adb_explicitgenericactualparameter_instantiation(instance):
    assert isinstance(instance, adb_ExplicitGenericActualParameter)

@given(instance=AbortStatement_strategy)
@settings(max_examples=50)
def test_abortstatement_instantiation(instance):
    assert isinstance(instance, AbortStatement)

@given(instance=adb_TaskNames_strategy)
@settings(max_examples=50)
def test_adb_tasknames_instantiation(instance):
    assert isinstance(instance, adb_TaskNames)

@given(instance=adb_EntryCallAlternative_strategy)
@settings(max_examples=50)
def test_adb_entrycallalternative_instantiation(instance):
    assert isinstance(instance, adb_EntryCallAlternative)

@given(instance=SelectAlternative_strategy)
@settings(max_examples=50)
def test_selectalternative_instantiation(instance):
    assert isinstance(instance, SelectAlternative)

@given(instance=adb_DelayAlternative_strategy)
@settings(max_examples=50)
def test_adb_delayalternative_instantiation(instance):
    assert isinstance(instance, adb_DelayAlternative)

@given(instance=adb_AcceptAlternative_strategy)
@settings(max_examples=50)
def test_adb_acceptalternative_instantiation(instance):
    assert isinstance(instance, adb_AcceptAlternative)

@given(instance=adb_GuardedAlternative_strategy)
@settings(max_examples=50)
def test_adb_guardedalternative_instantiation(instance):
    assert isinstance(instance, adb_GuardedAlternative)

@given(instance=adb_SelectAlternative_strategy)
@settings(max_examples=50)
def test_adb_selectalternative_instantiation(instance):
    assert isinstance(instance, adb_SelectAlternative)

@given(instance=adb_Guard_strategy)
@settings(max_examples=50)
def test_adb_guard_instantiation(instance):
    assert isinstance(instance, adb_Guard)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=adb_ConditionalEntryCall_strategy)
@settings(max_examples=50)
def test_adb_conditionalentrycall_instantiation(instance):
    assert isinstance(instance, adb_ConditionalEntryCall)

@given(instance=adb_TimedEntryCall_strategy)
@settings(max_examples=50)
def test_adb_timedentrycall_instantiation(instance):
    assert isinstance(instance, adb_TimedEntryCall)

@given(instance=adb_SelectiveAccept_strategy)
@settings(max_examples=50)
def test_adb_selectiveaccept_instantiation(instance):
    assert isinstance(instance, adb_SelectiveAccept)

@given(instance=adb_TriggeringStatement_strategy)
@settings(max_examples=50)
def test_adb_triggeringstatement_instantiation(instance):
    assert isinstance(instance, adb_TriggeringStatement)

@given(instance=adb_AbortablePart_strategy)
@settings(max_examples=50)
def test_adb_abortablepart_instantiation(instance):
    assert isinstance(instance, adb_AbortablePart)

@given(instance=adb_TriggeringAlternative_strategy)
@settings(max_examples=50)
def test_adb_triggeringalternative_instantiation(instance):
    assert isinstance(instance, adb_TriggeringAlternative)

@given(instance=adb_AsynchronousSelect_strategy)
@settings(max_examples=50)
def test_adb_asynchronousselect_instantiation(instance):
    assert isinstance(instance, adb_AsynchronousSelect)

@given(instance=adb_EntryIndexSpecification_strategy)
@settings(max_examples=50)
def test_adb_entryindexspecification_instantiation(instance):
    assert isinstance(instance, adb_EntryIndexSpecification)



@given(instance=adb_EntryIndexSpecification_strategy)
def test_adb_entryindexspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_EntryBarrier_strategy)
@settings(max_examples=50)
def test_adb_entrybarrier_instantiation(instance):
    assert isinstance(instance, adb_EntryBarrier)

@given(instance=adb_EntryBodyFormalPart_strategy)
@settings(max_examples=50)
def test_adb_entrybodyformalpart_instantiation(instance):
    assert isinstance(instance, adb_EntryBodyFormalPart)

@given(instance=adb_EntryIndex_strategy)
@settings(max_examples=50)
def test_adb_entryindex_instantiation(instance):
    assert isinstance(instance, adb_EntryIndex)

@given(instance=adb_ProtectedOperationItem_strategy)
@settings(max_examples=50)
def test_adb_protectedoperationitem_instantiation(instance):
    assert isinstance(instance, adb_ProtectedOperationItem)

@given(instance=adb_ReturnSubtypeIndication_strategy)
@settings(max_examples=50)
def test_adb_returnsubtypeindication_instantiation(instance):
    assert isinstance(instance, adb_ReturnSubtypeIndication)

@given(instance=TriggeringStatement_strategy)
@settings(max_examples=50)
def test_triggeringstatement_instantiation(instance):
    assert isinstance(instance, TriggeringStatement)

@given(instance=adb_LoopParameterSpecification_strategy)
@settings(max_examples=50)
def test_adb_loopparameterspecification_instantiation(instance):
    assert isinstance(instance, adb_LoopParameterSpecification)



@given(instance=adb_LoopParameterSpecification_strategy)
def test_adb_loopparameterspecification_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb_IterationScheme_strategy)
@settings(max_examples=50)
def test_adb_iterationscheme_instantiation(instance):
    assert isinstance(instance, adb_IterationScheme)

@given(instance=CompoundStatement_strategy)
@settings(max_examples=50)
def test_compoundstatement_instantiation(instance):
    assert isinstance(instance, CompoundStatement)

@given(instance=adb_ExtendedReturnStatement_strategy)
@settings(max_examples=50)
def test_adb_extendedreturnstatement_instantiation(instance):
    assert isinstance(instance, adb_ExtendedReturnStatement)



@given(instance=adb_ExtendedReturnStatement_strategy)
def test_adb_extendedreturnstatement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb_AcceptStatement_strategy)
@settings(max_examples=50)
def test_adb_acceptstatement_instantiation(instance):
    assert isinstance(instance, adb_AcceptStatement)



@given(instance=adb_AcceptStatement_strategy)
def test_adb_acceptstatement_entryidentifier_setter(instance):
    original = instance.entryidentifier
    instance.entryidentifier = original
    assert instance.entryidentifier == original

@given(instance=adb_SelectStatement_strategy)
@settings(max_examples=50)
def test_adb_selectstatement_instantiation(instance):
    assert isinstance(instance, adb_SelectStatement)

@given(instance=adb_LoopStatement_strategy)
@settings(max_examples=50)
def test_adb_loopstatement_instantiation(instance):
    assert isinstance(instance, adb_LoopStatement)



@given(instance=adb_LoopStatement_strategy)
def test_adb_loopstatement_sameName_setter(instance):
    original = instance.sameName
    instance.sameName = original
    assert instance.sameName == original



@given(instance=adb_LoopStatement_strategy)
def test_adb_loopstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_IfStatement_strategy)
@settings(max_examples=50)
def test_adb_ifstatement_instantiation(instance):
    assert isinstance(instance, adb_IfStatement)

@given(instance=adb_PragmaArgumentAssociation_strategy)
@settings(max_examples=50)
def test_adb_pragmaargumentassociation_instantiation(instance):
    assert isinstance(instance, adb_PragmaArgumentAssociation)



@given(instance=adb_PragmaArgumentAssociation_strategy)
def test_adb_pragmaargumentassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_DiscreteChoiceList_strategy)
@settings(max_examples=50)
def test_adb_discretechoicelist_instantiation(instance):
    assert isinstance(instance, adb_DiscreteChoiceList)

@given(instance=adb_CaseStatementAlternative_strategy)
@settings(max_examples=50)
def test_adb_casestatementalternative_instantiation(instance):
    assert isinstance(instance, adb_CaseStatementAlternative)

@given(instance=adb_CaseStatement_strategy)
@settings(max_examples=50)
def test_adb_casestatement_instantiation(instance):
    assert isinstance(instance, adb_CaseStatement)

@given(instance=ObjectDeclaration_strategy)
@settings(max_examples=50)
def test_objectdeclaration_instantiation(instance):
    assert isinstance(instance, ObjectDeclaration)

@given(instance=adb_DataInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_adb_datainstancedeclaration_instantiation(instance):
    assert isinstance(instance, adb_DataInstanceDeclaration)



@given(instance=adb_DataInstanceDeclaration_strategy)
def test_adb_datainstancedeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=adb_DataInstanceDeclaration_strategy)
def test_adb_datainstancedeclaration_aliased_setter(instance):
    original = instance.aliased
    instance.aliased = original
    assert instance.aliased == original

@given(instance=adb_GenericAssociation_strategy)
@settings(max_examples=50)
def test_adb_genericassociation_instantiation(instance):
    assert isinstance(instance, adb_GenericAssociation)



@given(instance=adb_GenericAssociation_strategy)
def test_adb_genericassociation_selectorName_setter(instance):
    original = instance.selectorName
    instance.selectorName = original
    assert instance.selectorName == original

@given(instance=adb_FormalPackageAssociation_strategy)
@settings(max_examples=50)
def test_adb_formalpackageassociation_instantiation(instance):
    assert isinstance(instance, adb_FormalPackageAssociation)



@given(instance=adb_FormalPackageAssociation_strategy)
def test_adb_formalpackageassociation_genericFormalParameterSelectorName_setter(instance):
    original = instance.genericFormalParameterSelectorName
    instance.genericFormalParameterSelectorName = original
    assert instance.genericFormalParameterSelectorName == original

@given(instance=adb_FormalPackageActualPart_strategy)
@settings(max_examples=50)
def test_adb_formalpackageactualpart_instantiation(instance):
    assert isinstance(instance, adb_FormalPackageActualPart)



@given(instance=adb_FormalPackageActualPart_strategy)
def test_adb_formalpackageactualpart_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb_SubprogramDefault_strategy)
@settings(max_examples=50)
def test_adb_subprogramdefault_instantiation(instance):
    assert isinstance(instance, adb_SubprogramDefault)



@given(instance=adb_SubprogramDefault_strategy)
def test_adb_subprogramdefault_defaultName_setter(instance):
    original = instance.defaultName
    instance.defaultName = original
    assert instance.defaultName == original

@given(instance=adb_Expression_strategy)
@settings(max_examples=50)
def test_adb_expression_instantiation(instance):
    assert isinstance(instance, adb_Expression)



@given(instance=adb_Expression_strategy)
def test_adb_expression_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=adb_AnonymousAccessDefinition_strategy)
@settings(max_examples=50)
def test_adb_anonymousaccessdefinition_instantiation(instance):
    assert isinstance(instance, adb_AnonymousAccessDefinition)

@given(instance=adb_OptNullExclusion_strategy)
@settings(max_examples=50)
def test_adb_optnullexclusion_instantiation(instance):
    assert isinstance(instance, adb_OptNullExclusion)



@given(instance=adb_OptNullExclusion_strategy)
def test_adb_optnullexclusion_not_null_setter(instance):
    original = instance.not_null
    instance.not_null = original
    assert instance.not_null == original

@given(instance=adb_SingleProtectedDeclaration_strategy)
@settings(max_examples=50)
def test_adb_singleprotecteddeclaration_instantiation(instance):
    assert isinstance(instance, adb_SingleProtectedDeclaration)



@given(instance=adb_SingleProtectedDeclaration_strategy)
def test_adb_singleprotecteddeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_Mode_strategy)
@settings(max_examples=50)
def test_adb_mode_instantiation(instance):
    assert isinstance(instance, adb_Mode)



@given(instance=adb_Mode_strategy)
def test_adb_mode_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=adb_Mode_strategy)
def test_adb_mode_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=adb_DefiningIdentifierList_strategy)
@settings(max_examples=50)
def test_adb_definingidentifierlist_instantiation(instance):
    assert isinstance(instance, adb_DefiningIdentifierList)



@given(instance=adb_DefiningIdentifierList_strategy)
def test_adb_definingidentifierlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FormalTypeDefinition_strategy)
@settings(max_examples=50)
def test_formaltypedefinition_instantiation(instance):
    assert isinstance(instance, FormalTypeDefinition)

@given(instance=adb_InterfaceTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_interfacetypedefinition_instantiation(instance):
    assert isinstance(instance, adb_InterfaceTypeDefinition)



@given(instance=adb_InterfaceTypeDefinition_strategy)
def test_adb_interfacetypedefinition_synchro_setter(instance):
    original = instance.synchro
    instance.synchro = original
    assert instance.synchro == original



@given(instance=adb_InterfaceTypeDefinition_strategy)
def test_adb_interfacetypedefinition_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original



@given(instance=adb_InterfaceTypeDefinition_strategy)
def test_adb_interfacetypedefinition_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original



@given(instance=adb_InterfaceTypeDefinition_strategy)
def test_adb_interfacetypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb_ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_arraytypedefinition_instantiation(instance):
    assert isinstance(instance, adb_ArrayTypeDefinition)

@given(instance=adb_AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_accesstypedefinition_instantiation(instance):
    assert isinstance(instance, adb_AccessTypeDefinition)

@given(instance=adb_FormalDerivedTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_formalderivedtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_FormalDerivedTypeDefinition)



@given(instance=adb_FormalDerivedTypeDefinition_strategy)
def test_adb_formalderivedtypedefinition_absract_setter(instance):
    original = instance.absract
    instance.absract = original
    assert instance.absract == original



@given(instance=adb_FormalDerivedTypeDefinition_strategy)
def test_adb_formalderivedtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_FormalDerivedTypeDefinition_strategy)
def test_adb_formalderivedtypedefinition_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=GenericFormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_genericformalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, GenericFormalParameterDeclaration)

@given(instance=adb_FormalTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_formaltypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_FormalTypeDeclaration)



@given(instance=adb_FormalTypeDeclaration_strategy)
def test_adb_formaltypedeclaration_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb_FormalPackageDeclaration_strategy)
@settings(max_examples=50)
def test_adb_formalpackagedeclaration_instantiation(instance):
    assert isinstance(instance, adb_FormalPackageDeclaration)



@given(instance=adb_FormalPackageDeclaration_strategy)
def test_adb_formalpackagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=adb_FormalPackageDeclaration_strategy)
def test_adb_formalpackagedeclaration_genericPackageName_setter(instance):
    original = instance.genericPackageName
    instance.genericPackageName = original
    assert instance.genericPackageName == original

@given(instance=adb_FormalSubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_adb_formalsubprogramdeclaration_instantiation(instance):
    assert isinstance(instance, adb_FormalSubprogramDeclaration)



@given(instance=adb_FormalSubprogramDeclaration_strategy)
def test_adb_formalsubprogramdeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb_FormalObjectDeclaration_strategy)
@settings(max_examples=50)
def test_adb_formalobjectdeclaration_instantiation(instance):
    assert isinstance(instance, adb_FormalObjectDeclaration)

@given(instance=adb_FormalPrivateTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_formalprivatetypedefinition_instantiation(instance):
    assert isinstance(instance, adb_FormalPrivateTypeDefinition)



@given(instance=adb_FormalPrivateTypeDefinition_strategy)
def test_adb_formalprivatetypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_FormalPrivateTypeDefinition_strategy)
def test_adb_formalprivatetypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=adb_FormalPrivateTypeDefinition_strategy)
def test_adb_formalprivatetypedefinition_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb_FormalTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_formaltypedefinition_instantiation(instance):
    assert isinstance(instance, adb_FormalTypeDefinition)

@given(instance=adb_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_adb_exceptionhandler_instantiation(instance):
    assert isinstance(instance, adb_ExceptionHandler)



@given(instance=adb_ExceptionHandler_strategy)
def test_adb_exceptionhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_GenericItem_strategy)
@settings(max_examples=50)
def test_adb_genericitem_instantiation(instance):
    assert isinstance(instance, adb_GenericItem)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=adb_SimpleReturnStatement_strategy)
@settings(max_examples=50)
def test_adb_simplereturnstatement_instantiation(instance):
    assert isinstance(instance, adb_SimpleReturnStatement)

@given(instance=adb_GotoStatement_strategy)
@settings(max_examples=50)
def test_adb_gotostatement_instantiation(instance):
    assert isinstance(instance, adb_GotoStatement)



@given(instance=adb_GotoStatement_strategy)
def test_adb_gotostatement_labelId_setter(instance):
    original = instance.labelId
    instance.labelId = original
    assert instance.labelId == original

@given(instance=adb_AbortStatement_strategy)
@settings(max_examples=50)
def test_adb_abortstatement_instantiation(instance):
    assert isinstance(instance, adb_AbortStatement)

@given(instance=adb_ExitStatement_strategy)
@settings(max_examples=50)
def test_adb_exitstatement_instantiation(instance):
    assert isinstance(instance, adb_ExitStatement)

@given(instance=adb_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_adb_assignmentstatement_instantiation(instance):
    assert isinstance(instance, adb_AssignmentStatement)

@given(instance=adb_DelayStatement_strategy)
@settings(max_examples=50)
def test_adb_delaystatement_instantiation(instance):
    assert isinstance(instance, adb_DelayStatement)



@given(instance=adb_DelayStatement_strategy)
def test_adb_delaystatement_until_setter(instance):
    original = instance.until
    instance.until = original
    assert instance.until == original

@given(instance=adb_ProcedureOrEntryCallStatement_strategy)
@settings(max_examples=50)
def test_adb_procedureorentrycallstatement_instantiation(instance):
    assert isinstance(instance, adb_ProcedureOrEntryCallStatement)

@given(instance=adb_RaiseStatement_strategy)
@settings(max_examples=50)
def test_adb_raisestatement_instantiation(instance):
    assert isinstance(instance, adb_RaiseStatement)

@given(instance=adb_RequeueStatement_strategy)
@settings(max_examples=50)
def test_adb_requeuestatement_instantiation(instance):
    assert isinstance(instance, adb_RequeueStatement)



@given(instance=adb_RequeueStatement_strategy)
def test_adb_requeuestatement_abort_setter(instance):
    original = instance.abort
    instance.abort = original
    assert instance.abort == original

@given(instance=adb_NullStatement_strategy)
@settings(max_examples=50)
def test_adb_nullstatement_instantiation(instance):
    assert isinstance(instance, adb_NullStatement)



@given(instance=adb_NullStatement_strategy)
def test_adb_nullstatement_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=adb_CompoundStatement_strategy)
@settings(max_examples=50)
def test_adb_compoundstatement_instantiation(instance):
    assert isinstance(instance, adb_CompoundStatement)

@given(instance=adb_SimpleStatement_strategy)
@settings(max_examples=50)
def test_adb_simplestatement_instantiation(instance):
    assert isinstance(instance, adb_SimpleStatement)

@given(instance=adb_Statement_strategy)
@settings(max_examples=50)
def test_adb_statement_instantiation(instance):
    assert isinstance(instance, adb_Statement)

@given(instance=adb_LabelisableStatement_strategy)
@settings(max_examples=50)
def test_adb_labelisablestatement_instantiation(instance):
    assert isinstance(instance, adb_LabelisableStatement)

@given(instance=AbortablePart_strategy)
@settings(max_examples=50)
def test_abortablepart_instantiation(instance):
    assert isinstance(instance, AbortablePart)

@given(instance=HandledSequenceOfStatements_strategy)
@settings(max_examples=50)
def test_handledsequenceofstatements_instantiation(instance):
    assert isinstance(instance, HandledSequenceOfStatements)

@given(instance=adb_SequenceOfStatements_strategy)
@settings(max_examples=50)
def test_adb_sequenceofstatements_instantiation(instance):
    assert isinstance(instance, adb_SequenceOfStatements)

@given(instance=adb_Label_strategy)
@settings(max_examples=50)
def test_adb_label_instantiation(instance):
    assert isinstance(instance, adb_Label)



@given(instance=adb_Label_strategy)
def test_adb_label_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=adb_ProperBody_strategy)
@settings(max_examples=50)
def test_adb_properbody_instantiation(instance):
    assert isinstance(instance, adb_ProperBody)

@given(instance=adb_BodyStub_strategy)
@settings(max_examples=50)
def test_adb_bodystub_instantiation(instance):
    assert isinstance(instance, adb_BodyStub)



@given(instance=adb_BodyStub_strategy)
def test_adb_bodystub_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ProtectedElementDeclaration_strategy)
@settings(max_examples=50)
def test_protectedelementdeclaration_instantiation(instance):
    assert isinstance(instance, ProtectedElementDeclaration)

@given(instance=adb_ComponentDeclaration_strategy)
@settings(max_examples=50)
def test_adb_componentdeclaration_instantiation(instance):
    assert isinstance(instance, adb_ComponentDeclaration)

@given(instance=adb_ProtectedOperationDeclaration_strategy)
@settings(max_examples=50)
def test_adb_protectedoperationdeclaration_instantiation(instance):
    assert isinstance(instance, adb_ProtectedOperationDeclaration)

@given(instance=adb_ProtectedElementDeclaration_strategy)
@settings(max_examples=50)
def test_adb_protectedelementdeclaration_instantiation(instance):
    assert isinstance(instance, adb_ProtectedElementDeclaration)

@given(instance=adb_ProtectedDefinition_strategy)
@settings(max_examples=50)
def test_adb_protecteddefinition_instantiation(instance):
    assert isinstance(instance, adb_ProtectedDefinition)

@given(instance=adb_FormalPart_strategy)
@settings(max_examples=50)
def test_adb_formalpart_instantiation(instance):
    assert isinstance(instance, adb_FormalPart)

@given(instance=adb_DiscreteSubtypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_discretesubtypedefinition_instantiation(instance):
    assert isinstance(instance, adb_DiscreteSubtypeDefinition)

@given(instance=adb_Name_strategy)
@settings(max_examples=50)
def test_adb_name_instantiation(instance):
    assert isinstance(instance, adb_Name)



@given(instance=adb_Name_strategy)
def test_adb_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_ExceptionChoice_strategy)
@settings(max_examples=50)
def test_adb_exceptionchoice_instantiation(instance):
    assert isinstance(instance, adb_ExceptionChoice)



@given(instance=adb_ExceptionChoice_strategy)
def test_adb_exceptionchoice_others_setter(instance):
    original = instance.others
    instance.others = original
    assert instance.others == original

@given(instance=adb_ParameterAndResultProfile_strategy)
@settings(max_examples=50)
def test_adb_parameterandresultprofile_instantiation(instance):
    assert isinstance(instance, adb_ParameterAndResultProfile)

@given(instance=SubprogramSpecification_strategy)
@settings(max_examples=50)
def test_subprogramspecification_instantiation(instance):
    assert isinstance(instance, SubprogramSpecification)

@given(instance=adb_FunctionSpecification_strategy)
@settings(max_examples=50)
def test_adb_functionspecification_instantiation(instance):
    assert isinstance(instance, adb_FunctionSpecification)

@given(instance=adb_ProcedureSpecification_strategy)
@settings(max_examples=50)
def test_adb_procedurespecification_instantiation(instance):
    assert isinstance(instance, adb_ProcedureSpecification)

@given(instance=BodyStub_strategy)
@settings(max_examples=50)
def test_bodystub_instantiation(instance):
    assert isinstance(instance, BodyStub)

@given(instance=adb_TaskBodyStub_strategy)
@settings(max_examples=50)
def test_adb_taskbodystub_instantiation(instance):
    assert isinstance(instance, adb_TaskBodyStub)

@given(instance=adb_PackageBodyStub_strategy)
@settings(max_examples=50)
def test_adb_packagebodystub_instantiation(instance):
    assert isinstance(instance, adb_PackageBodyStub)

@given(instance=adb_ProtectedBodyStub_strategy)
@settings(max_examples=50)
def test_adb_protectedbodystub_instantiation(instance):
    assert isinstance(instance, adb_ProtectedBodyStub)

@given(instance=NewTypeDeclaration_strategy)
@settings(max_examples=50)
def test_newtypedeclaration_instantiation(instance):
    assert isinstance(instance, NewTypeDeclaration)

@given(instance=adb_FullTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_fulltypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_FullTypeDeclaration)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=adb_SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_subtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_SubtypeDeclaration)

@given(instance=adb_NewTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_newtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_NewTypeDeclaration)

@given(instance=adb_TaskDefinition_strategy)
@settings(max_examples=50)
def test_adb_taskdefinition_instantiation(instance):
    assert isinstance(instance, adb_TaskDefinition)

@given(instance=adb_InterfaceList_strategy)
@settings(max_examples=50)
def test_adb_interfacelist_instantiation(instance):
    assert isinstance(instance, adb_InterfaceList)

@given(instance=adb_KnownDiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb_knowndiscriminantpart_instantiation(instance):
    assert isinstance(instance, adb_KnownDiscriminantPart)

@given(instance=DeclarativeItem_strategy)
@settings(max_examples=50)
def test_declarativeitem_instantiation(instance):
    assert isinstance(instance, DeclarativeItem)

@given(instance=adb_Body_strategy)
@settings(max_examples=50)
def test_adb_body_instantiation(instance):
    assert isinstance(instance, adb_Body)

@given(instance=ProtectedOperationDeclaration_strategy)
@settings(max_examples=50)
def test_protectedoperationdeclaration_instantiation(instance):
    assert isinstance(instance, ProtectedOperationDeclaration)

@given(instance=TaskItem_strategy)
@settings(max_examples=50)
def test_taskitem_instantiation(instance):
    assert isinstance(instance, TaskItem)

@given(instance=adb_EntryDeclaration_strategy)
@settings(max_examples=50)
def test_adb_entrydeclaration_instantiation(instance):
    assert isinstance(instance, adb_EntryDeclaration)



@given(instance=adb_EntryDeclaration_strategy)
def test_adb_entrydeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_TaskItem_strategy)
@settings(max_examples=50)
def test_adb_taskitem_instantiation(instance):
    assert isinstance(instance, adb_TaskItem)

@given(instance=adb_SubtypeIndication_strategy)
@settings(max_examples=50)
def test_adb_subtypeindication_instantiation(instance):
    assert isinstance(instance, adb_SubtypeIndication)



@given(instance=adb_SubtypeIndication_strategy)
def test_adb_subtypeindication_subtypeMark_setter(instance):
    original = instance.subtypeMark
    instance.subtypeMark = original
    assert instance.subtypeMark == original

@given(instance=adb_PrivateExtensionDeclaration_strategy)
@settings(max_examples=50)
def test_adb_privateextensiondeclaration_instantiation(instance):
    assert isinstance(instance, adb_PrivateExtensionDeclaration)



@given(instance=adb_PrivateExtensionDeclaration_strategy)
def test_adb_privateextensiondeclaration_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_PrivateExtensionDeclaration_strategy)
def test_adb_privateextensiondeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=adb_PrivateExtensionDeclaration_strategy)
def test_adb_privateextensiondeclaration_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=adb_PrivateTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_privatetypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_PrivateTypeDeclaration)



@given(instance=adb_PrivateTypeDeclaration_strategy)
def test_adb_privatetypedeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=adb_PrivateTypeDeclaration_strategy)
def test_adb_privatetypedeclaration_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original



@given(instance=adb_PrivateTypeDeclaration_strategy)
def test_adb_privatetypedeclaration_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb_DiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb_discriminantpart_instantiation(instance):
    assert isinstance(instance, adb_DiscriminantPart)

@given(instance=adb_IncompleteTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_incompletetypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_IncompleteTypeDeclaration)



@given(instance=adb_IncompleteTypeDeclaration_strategy)
def test_adb_incompletetypedeclaration_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb_TypeDefinition_strategy)
@settings(max_examples=50)
def test_adb_typedefinition_instantiation(instance):
    assert isinstance(instance, adb_TypeDefinition)

@given(instance=FullTypeDeclaration_strategy)
@settings(max_examples=50)
def test_fulltypedeclaration_instantiation(instance):
    assert isinstance(instance, FullTypeDeclaration)

@given(instance=adb_ProtectedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_protectedtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_ProtectedTypeDeclaration)

@given(instance=adb_FullDataTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_fulldatatypedeclaration_instantiation(instance):
    assert isinstance(instance, adb_FullDataTypeDeclaration)

@given(instance=adb_PackageSpecification_strategy)
@settings(max_examples=50)
def test_adb_packagespecification_instantiation(instance):
    assert isinstance(instance, adb_PackageSpecification)



@given(instance=adb_PackageSpecification_strategy)
def test_adb_packagespecification_endname_setter(instance):
    original = instance.endname
    instance.endname = original
    assert instance.endname == original

@given(instance=LibrarySpecification_strategy)
@settings(max_examples=50)
def test_libraryspecification_instantiation(instance):
    assert isinstance(instance, LibrarySpecification)

@given(instance=PackageDeclaration_strategy)
@settings(max_examples=50)
def test_packagedeclaration_instantiation(instance):
    assert isinstance(instance, PackageDeclaration)

@given(instance=adb_Renaming_strategy)
@settings(max_examples=50)
def test_adb_renaming_instantiation(instance):
    assert isinstance(instance, adb_Renaming)



@given(instance=adb_Renaming_strategy)
def test_adb_renaming_renamed_setter(instance):
    original = instance.renamed
    instance.renamed = original
    assert instance.renamed == original

@given(instance=adb_PackageDefinition_strategy)
@settings(max_examples=50)
def test_adb_packagedefinition_instantiation(instance):
    assert isinstance(instance, adb_PackageDefinition)

@given(instance=BasicDeclaration_strategy)
@settings(max_examples=50)
def test_basicdeclaration_instantiation(instance):
    assert isinstance(instance, BasicDeclaration)

@given(instance=adb_ExceptionDeclaration_strategy)
@settings(max_examples=50)
def test_adb_exceptiondeclaration_instantiation(instance):
    assert isinstance(instance, adb_ExceptionDeclaration)

@given(instance=adb_NumberDeclaration_strategy)
@settings(max_examples=50)
def test_adb_numberdeclaration_instantiation(instance):
    assert isinstance(instance, adb_NumberDeclaration)

@given(instance=adb_ObjectDeclaration_strategy)
@settings(max_examples=50)
def test_adb_objectdeclaration_instantiation(instance):
    assert isinstance(instance, adb_ObjectDeclaration)

@given(instance=adb_TaskDeclaration_strategy)
@settings(max_examples=50)
def test_adb_taskdeclaration_instantiation(instance):
    assert isinstance(instance, adb_TaskDeclaration)



@given(instance=adb_TaskDeclaration_strategy)
def test_adb_taskdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb_typedeclaration_instantiation(instance):
    assert isinstance(instance, adb_TypeDeclaration)



@given(instance=adb_TypeDeclaration_strategy)
def test_adb_typedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LibraryUnitSpecification_strategy)
@settings(max_examples=50)
def test_libraryunitspecification_instantiation(instance):
    assert isinstance(instance, LibraryUnitSpecification)

@given(instance=adb_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_adb_packagedeclaration_instantiation(instance):
    assert isinstance(instance, adb_PackageDeclaration)



@given(instance=adb_PackageDeclaration_strategy)
def test_adb_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_LibraryUnitSpecification_strategy)
@settings(max_examples=50)
def test_adb_libraryunitspecification_instantiation(instance):
    assert isinstance(instance, adb_LibraryUnitSpecification)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=adb_SeparateSubunit_strategy)
@settings(max_examples=50)
def test_adb_separatesubunit_instantiation(instance):
    assert isinstance(instance, adb_SeparateSubunit)



@given(instance=adb_SeparateSubunit_strategy)
def test_adb_separatesubunit_parentUnitName_setter(instance):
    original = instance.parentUnitName
    instance.parentUnitName = original
    assert instance.parentUnitName == original

@given(instance=adb_HandledSequenceOfStatements_strategy)
@settings(max_examples=50)
def test_adb_handledsequenceofstatements_instantiation(instance):
    assert isinstance(instance, adb_HandledSequenceOfStatements)

@given(instance=adb_DeclarativeItem_strategy)
@settings(max_examples=50)
def test_adb_declarativeitem_instantiation(instance):
    assert isinstance(instance, adb_DeclarativeItem)

@given(instance=adb_DeclarativeBlock_strategy)
@settings(max_examples=50)
def test_adb_declarativeblock_instantiation(instance):
    assert isinstance(instance, adb_DeclarativeBlock)

@given(instance=adb_SubprogramSpecification_strategy)
@settings(max_examples=50)
def test_adb_subprogramspecification_instantiation(instance):
    assert isinstance(instance, adb_SubprogramSpecification)

@given(instance=ProtectedOperationItem_strategy)
@settings(max_examples=50)
def test_protectedoperationitem_instantiation(instance):
    assert isinstance(instance, ProtectedOperationItem)

@given(instance=adb_SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_adb_subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, adb_SubprogramDeclaration)



@given(instance=adb_SubprogramDeclaration_strategy)
def test_adb_subprogramdeclaration_renamedName_setter(instance):
    original = instance.renamedName
    instance.renamedName = original
    assert instance.renamedName == original



@given(instance=adb_SubprogramDeclaration_strategy)
def test_adb_subprogramdeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=adb_SubprogramDeclaration_strategy)
def test_adb_subprogramdeclaration_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=ProperBody_strategy)
@settings(max_examples=50)
def test_properbody_instantiation(instance):
    assert isinstance(instance, ProperBody)

@given(instance=adb_ProtectedBody_strategy)
@settings(max_examples=50)
def test_adb_protectedbody_instantiation(instance):
    assert isinstance(instance, adb_ProtectedBody)



@given(instance=adb_ProtectedBody_strategy)
def test_adb_protectedbody_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original



@given(instance=adb_ProtectedBody_strategy)
def test_adb_protectedbody_idTask_setter(instance):
    original = instance.idTask
    instance.idTask = original
    assert instance.idTask == original

@given(instance=DeclarativeBlock_strategy)
@settings(max_examples=50)
def test_declarativeblock_instantiation(instance):
    assert isinstance(instance, DeclarativeBlock)

@given(instance=adb_TaskBody_strategy)
@settings(max_examples=50)
def test_adb_taskbody_instantiation(instance):
    assert isinstance(instance, adb_TaskBody)

@given(instance=adb_EntryBody_strategy)
@settings(max_examples=50)
def test_adb_entrybody_instantiation(instance):
    assert isinstance(instance, adb_EntryBody)



@given(instance=adb_EntryBody_strategy)
def test_adb_entrybody_endid_setter(instance):
    original = instance.endid
    instance.endid = original
    assert instance.endid == original

@given(instance=adb_PackageBody_strategy)
@settings(max_examples=50)
def test_adb_packagebody_instantiation(instance):
    assert isinstance(instance, adb_PackageBody)

@given(instance=adb_BlockStatement_strategy)
@settings(max_examples=50)
def test_adb_blockstatement_instantiation(instance):
    assert isinstance(instance, adb_BlockStatement)



@given(instance=adb_BlockStatement_strategy)
def test_adb_blockstatement_blockStatementIdentifier_setter(instance):
    original = instance.blockStatementIdentifier
    instance.blockStatementIdentifier = original
    assert instance.blockStatementIdentifier == original

@given(instance=adb_SubprogramBody_strategy)
@settings(max_examples=50)
def test_adb_subprogrambody_instantiation(instance):
    assert isinstance(instance, adb_SubprogramBody)



@given(instance=adb_SubprogramBody_strategy)
def test_adb_subprogrambody_endname_setter(instance):
    original = instance.endname
    instance.endname = original
    assert instance.endname == original

@given(instance=adb_BasicDeclarativeItem_strategy)
@settings(max_examples=50)
def test_adb_basicdeclarativeitem_instantiation(instance):
    assert isinstance(instance, adb_BasicDeclarativeItem)

@given(instance=adb_GenericActualPart_strategy)
@settings(max_examples=50)
def test_adb_genericactualpart_instantiation(instance):
    assert isinstance(instance, adb_GenericActualPart)

@given(instance=adb_OverridingIndicator_strategy)
@settings(max_examples=50)
def test_adb_overridingindicator_instantiation(instance):
    assert isinstance(instance, adb_OverridingIndicator)



@given(instance=adb_OverridingIndicator_strategy)
def test_adb_overridingindicator_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=adb_GenericInstantiation_strategy)
@settings(max_examples=50)
def test_adb_genericinstantiation_instantiation(instance):
    assert isinstance(instance, adb_GenericInstantiation)



@given(instance=adb_GenericInstantiation_strategy)
def test_adb_genericinstantiation_genericName_setter(instance):
    original = instance.genericName
    instance.genericName = original
    assert instance.genericName == original



@given(instance=adb_GenericInstantiation_strategy)
def test_adb_genericinstantiation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_LibrarySpecification_strategy)
@settings(max_examples=50)
def test_adb_libraryspecification_instantiation(instance):
    assert isinstance(instance, adb_LibrarySpecification)

@given(instance=adb_GenericItems_strategy)
@settings(max_examples=50)
def test_adb_genericitems_instantiation(instance):
    assert isinstance(instance, adb_GenericItems)

@given(instance=adb_GenericDeclaration_strategy)
@settings(max_examples=50)
def test_adb_genericdeclaration_instantiation(instance):
    assert isinstance(instance, adb_GenericDeclaration)

@given(instance=UseClause_strategy)
@settings(max_examples=50)
def test_useclause_instantiation(instance):
    assert isinstance(instance, UseClause)

@given(instance=adb_UseTypeClause_strategy)
@settings(max_examples=50)
def test_adb_usetypeclause_instantiation(instance):
    assert isinstance(instance, adb_UseTypeClause)



@given(instance=adb_UseTypeClause_strategy)
def test_adb_usetypeclause_useTypeRefs_setter(instance):
    original = instance.useTypeRefs
    instance.useTypeRefs = original
    assert instance.useTypeRefs == original



@given(instance=adb_UseTypeClause_strategy)
def test_adb_usetypeclause_typesNames_setter(instance):
    original = instance.typesNames
    instance.typesNames = original
    assert instance.typesNames == original

@given(instance=adb_UsePackageClause_strategy)
@settings(max_examples=50)
def test_adb_usepackageclause_instantiation(instance):
    assert isinstance(instance, adb_UsePackageClause)

@given(instance=GenericItem_strategy)
@settings(max_examples=50)
def test_genericitem_instantiation(instance):
    assert isinstance(instance, GenericItem)

@given(instance=adb_GenericFormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_adb_genericformalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, adb_GenericFormalParameterDeclaration)

@given(instance=BasicDeclarativeItem_strategy)
@settings(max_examples=50)
def test_basicdeclarativeitem_instantiation(instance):
    assert isinstance(instance, BasicDeclarativeItem)

@given(instance=adb_BasicDeclaration_strategy)
@settings(max_examples=50)
def test_adb_basicdeclaration_instantiation(instance):
    assert isinstance(instance, adb_BasicDeclaration)

@given(instance=adb_AspectClause_strategy)
@settings(max_examples=50)
def test_adb_aspectclause_instantiation(instance):
    assert isinstance(instance, adb_AspectClause)



@given(instance=adb_AspectClause_strategy)
def test_adb_aspectclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_LibraryUnitDeclaration_strategy)
@settings(max_examples=50)
def test_adb_libraryunitdeclaration_instantiation(instance):
    assert isinstance(instance, adb_LibraryUnitDeclaration)



@given(instance=adb_LibraryUnitDeclaration_strategy)
def test_adb_libraryunitdeclaration_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=ContextItem_strategy)
@settings(max_examples=50)
def test_contextitem_instantiation(instance):
    assert isinstance(instance, ContextItem)

@given(instance=adb_UseClause_strategy)
@settings(max_examples=50)
def test_adb_useclause_instantiation(instance):
    assert isinstance(instance, adb_UseClause)

@given(instance=adb_WithClause_strategy)
@settings(max_examples=50)
def test_adb_withclause_instantiation(instance):
    assert isinstance(instance, adb_WithClause)



@given(instance=adb_WithClause_strategy)
def test_adb_withclause_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original



@given(instance=adb_WithClause_strategy)
def test_adb_withclause_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=adb_ContextItem_strategy)
@settings(max_examples=50)
def test_adb_contextitem_instantiation(instance):
    assert isinstance(instance, adb_ContextItem)

@given(instance=adb_Pragma_strategy)
@settings(max_examples=50)
def test_adb_pragma_instantiation(instance):
    assert isinstance(instance, adb_Pragma)



@given(instance=adb_Pragma_strategy)
def test_adb_pragma_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb_Unit_strategy)
@settings(max_examples=50)
def test_adb_unit_instantiation(instance):
    assert isinstance(instance, adb_Unit)

@given(instance=adb_ContextClause_strategy)
@settings(max_examples=50)
def test_adb_contextclause_instantiation(instance):
    assert isinstance(instance, adb_ContextClause)

@given(instance=adb_CompilationUnit_strategy)
@settings(max_examples=50)
def test_adb_compilationunit_instantiation(instance):
    assert isinstance(instance, adb_CompilationUnit)

@given(instance=adb_Compilation_strategy)
@settings(max_examples=50)
def test_adb_compilation_instantiation(instance):
    assert isinstance(instance, adb_Compilation)
