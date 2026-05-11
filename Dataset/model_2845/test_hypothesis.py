import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DiscreteChoice,
    ExplicitGenericActualParameter,
    EntryIndex,
    adb::Primary,
    adb::RealRangeSpecification,
    adb::DiscreteChoice,
    adb::Variant,
    adb::ComponentClause,
    adb::ModClause,
    RealTypeDefinition,
    adb::FixedPointDefinition,
    adb::FloatingPointDefinition,
    ComponentItem,
    adb::VariantPart,
    adb::OptVariantPart,
    adb::ComponentItem,
    adb::ComponentList,
    adb::SimpleExpression,
    IntegerTypeDefinition,
    adb::ModularTypeDefinition,
    adb::SignedIntegerTypeDefinition,
    adb::ParameterSpecification,
    ReturnSubtypeIndication,
    ArrayIndexes,
    adb::ConstrainedIndexes,
    adb::UnconstrainedIndexes,
    adb::ComponentDefinition,
    adb::ArrayIndexes,
    NotNullAccessDefinition,
    AccessSpecification,
    adb::AccessToDataDefinition,
    adb::AccessToSubprogramDefinition,
    adb::AccessSpecification,
    adb::AccessToDataInstance,
    TypeDefinition,
    adb::IntegerTypeDefinition,
    adb::EnumerationTypeDefinition,
    adb::DerivedTypeDefinition,
    adb::RecordTypeDefinition,
    adb::RealTypeDefinition,
    adb::NotNullAccessDefinition,
    adb::DiscriminantSpecification,
    adb::RecordDefinition,
    adb::RecordExtensionPart,
    DiscriminantPart,
    adb::UnknownDiscriminantPart,
    adb::ExplicitGenericActualParameter,
    AbortStatement,
    adb::TaskNames,
    adb::EntryCallAlternative,
    SelectAlternative,
    adb::DelayAlternative,
    adb::AcceptAlternative,
    adb::GuardedAlternative,
    adb::SelectAlternative,
    adb::Guard,
    SelectStatement,
    adb::ConditionalEntryCall,
    adb::TimedEntryCall,
    adb::SelectiveAccept,
    adb::TriggeringStatement,
    adb::AbortablePart,
    adb::TriggeringAlternative,
    adb::AsynchronousSelect,
    adb::EntryIndexSpecification,
    adb::EntryBarrier,
    adb::EntryBodyFormalPart,
    adb::EntryIndex,
    adb::ProtectedOperationItem,
    adb::ReturnSubtypeIndication,
    TriggeringStatement,
    adb::LoopParameterSpecification,
    adb::IterationScheme,
    CompoundStatement,
    adb::ExtendedReturnStatement,
    adb::SelectStatement,
    adb::AcceptStatement,
    adb::LoopStatement,
    adb::IfStatement,
    adb::PragmaArgumentAssociation,
    adb::DiscreteChoiceList,
    adb::CaseStatementAlternative,
    adb::CaseStatement,
    ObjectDeclaration,
    adb::DataInstanceDeclaration,
    adb::GenericAssociation,
    adb::FormalPackageAssociation,
    adb::FormalPackageActualPart,
    adb::SubprogramDefault,
    adb::AnonymousAccessDefinition,
    adb::OptNullExclusion,
    adb::SingleProtectedDeclaration,
    adb::Mode,
    adb::DefiningIdentifierList,
    FormalTypeDefinition,
    adb::FormalDerivedTypeDefinition,
    adb::AccessTypeDefinition,
    adb::InterfaceTypeDefinition,
    adb::ArrayTypeDefinition,
    GenericFormalParameterDeclaration,
    adb::FormalSubprogramDeclaration,
    adb::FormalPackageDeclaration,
    adb::FormalTypeDeclaration,
    adb::FormalObjectDeclaration,
    adb::FormalPrivateTypeDefinition,
    adb::FormalTypeDefinition,
    Range,
    adb::ExplicitRange,
    adb::EntityRange,
    RangeConstraint,
    adb::ParameterEffectiveValue,
    adb::AttributeDesignator,
    adb::PrimaryName,
    Interval,
    adb::ArrayComponentAssociation,
    ArrayAggregate,
    adb::NamedArrayAggregate,
    adb::PositionalArrayAggregate,
    adb::AncestorPart,
    RecordComponentAssociation,
    adb::UninitializedComponents,
    adb::InitializedComponents,
    adb::ParameterAssociation,
    adb::RecordComponentAssociation,
    RecordAggregate,
    adb::RecordComponentAssociationList,
    Aggregate,
    adb::ArrayAggregate,
    adb::ExtensionAggregate,
    adb::RecordAggregate,
    Qualifier,
    ParenthesizedExpression,
    adb::Aggregate,
    adb::ComponentChoiceList,
    adb::DiscriminantSelectors,
    adb::DiscriminantAssociation,
    CompositeConstraint,
    adb::IndexConstraint,
    adb::DiscriminantConstraint,
    adb::CompositeConstraint,
    adb::OptConstraint,
    DiscreteRange,
    DiscreteSubtypeDefinition,
    adb::DiscreteRange,
    adb::Qualifier,
    Primary,
    adb::Allocator,
    adb::Null,
    adb::QualifiedName,
    adb::StringLiteral,
    adb::ParenthesizedExpression,
    adb::NumericLiteral,
    ScalarConstraint,
    adb::DeltaConstraint,
    adb::RangeConstraint,
    adb::DigitsConstraint,
    adb::ScalarConstraint,
    adb::EObject,
    adb::Factor,
    adb::Term,
    adb::Interval,
    adb::Membership,
    adb::Relation,
    ParameterEffectiveValue,
    adb::Range,
    AncestorPart,
    adb::Expression,
    adb::ExceptionHandler,
    adb::GenericItem,
    SimpleStatement,
    adb::AbortStatement,
    adb::SimpleReturnStatement,
    adb::GotoStatement,
    adb::ProcedureOrEntryCallStatement,
    adb::DelayStatement,
    adb::RaiseStatement,
    adb::AssignmentStatement,
    adb::RequeueStatement,
    adb::ExitStatement,
    adb::NullStatement,
    Statement,
    adb::CompoundStatement,
    adb::SimpleStatement,
    adb::Statement,
    adb::LabelisableStatement,
    AbortablePart,
    HandledSequenceOfStatements,
    adb::SequenceOfStatements,
    adb::Label,
    Body,
    adb::BodyStub,
    adb::ProperBody,
    ProtectedElementDeclaration,
    adb::ComponentDeclaration,
    adb::ProtectedOperationDeclaration,
    adb::ProtectedElementDeclaration,
    adb::ProtectedDefinition,
    adb::FormalPart,
    adb::DiscreteSubtypeDefinition,
    adb::Name,
    adb::ExceptionChoice,
    adb::ParameterAndResultProfile,
    SubprogramSpecification,
    adb::FunctionSpecification,
    adb::ProcedureSpecification,
    BodyStub,
    adb::ProtectedBodyStub,
    adb::PackageBodyStub,
    adb::TaskBodyStub,
    NewTypeDeclaration,
    adb::FullTypeDeclaration,
    TypeDeclaration,
    adb::SubtypeDeclaration,
    adb::NewTypeDeclaration,
    adb::TaskDefinition,
    adb::InterfaceList,
    adb::KnownDiscriminantPart,
    DeclarativeItem,
    adb::Body,
    ProtectedOperationDeclaration,
    TaskItem,
    adb::EntryDeclaration,
    adb::TaskItem,
    adb::SubtypeIndication,
    adb::PrivateExtensionDeclaration,
    adb::PrivateTypeDeclaration,
    adb::DiscriminantPart,
    adb::IncompleteTypeDeclaration,
    adb::TypeDefinition,
    FullTypeDeclaration,
    adb::ProtectedTypeDeclaration,
    adb::FullDataTypeDeclaration,
    adb::PackageSpecification,
    LibrarySpecification,
    PackageDeclaration,
    adb::Renaming,
    adb::PackageDefinition,
    BasicDeclaration,
    adb::NumberDeclaration,
    adb::TaskDeclaration,
    adb::TypeDeclaration,
    adb::ExceptionDeclaration,
    adb::ObjectDeclaration,
    LibraryUnitSpecification,
    adb::PackageDeclaration,
    adb::LibraryUnitSpecification,
    Unit,
    adb::SeparateSubunit,
    adb::HandledSequenceOfStatements,
    adb::DeclarativeItem,
    adb::DeclarativeBlock,
    adb::SubprogramSpecification,
    ProtectedOperationItem,
    adb::SubprogramDeclaration,
    ProperBody,
    adb::ProtectedBody,
    DeclarativeBlock,
    adb::EntryBody,
    adb::TaskBody,
    adb::BlockStatement,
    adb::PackageBody,
    adb::SubprogramBody,
    adb::BasicDeclarativeItem,
    adb::GenericActualPart,
    adb::OverridingIndicator,
    adb::GenericInstantiation,
    adb::LibrarySpecification,
    adb::GenericItems,
    adb::GenericDeclaration,
    UseClause,
    adb::UseTypeClause,
    adb::UsePackageClause,
    GenericItem,
    adb::GenericFormalParameterDeclaration,
    BasicDeclarativeItem,
    adb::AspectClause,
    adb::BasicDeclaration,
    adb::LibraryUnitDeclaration,
    ContextItem,
    adb::UseClause,
    adb::WithClause,
    adb::ContextItem,
    adb::Pragma,
    adb::Unit,
    adb::ContextClause,
    adb::CompilationUnit,
    adb::Compilation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_discretechoice_is_not_abstract():
    assert not inspect.isabstract(DiscreteChoice)


def test_discretechoice_constructor_exists():
    assert callable(DiscreteChoice.__init__)


def test_discretechoice_constructor_args():
    sig = inspect.signature(DiscreteChoice.__init__)
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



def test_adb::primary_is_not_abstract():
    assert not inspect.isabstract(adb::Primary)


def test_adb::primary_constructor_exists():
    assert callable(adb::Primary.__init__)


def test_adb::primary_constructor_args():
    sig = inspect.signature(adb::Primary.__init__)
    params = list(sig.parameters.keys())



def test_adb::realrangespecification_is_not_abstract():
    assert not inspect.isabstract(adb::RealRangeSpecification)


def test_adb::realrangespecification_constructor_exists():
    assert callable(adb::RealRangeSpecification.__init__)


def test_adb::realrangespecification_constructor_args():
    sig = inspect.signature(adb::RealRangeSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::discretechoice_is_not_abstract():
    assert not inspect.isabstract(adb::DiscreteChoice)


def test_adb::discretechoice_constructor_exists():
    assert callable(adb::DiscreteChoice.__init__)


def test_adb::discretechoice_constructor_args():
    sig = inspect.signature(adb::DiscreteChoice.__init__)
    params = list(sig.parameters.keys())



def test_adb::variant_is_not_abstract():
    assert not inspect.isabstract(adb::Variant)


def test_adb::variant_constructor_exists():
    assert callable(adb::Variant.__init__)


def test_adb::variant_constructor_args():
    sig = inspect.signature(adb::Variant.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentclause_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentClause)


def test_adb::componentclause_constructor_exists():
    assert callable(adb::ComponentClause.__init__)


def test_adb::componentclause_constructor_args():
    sig = inspect.signature(adb::ComponentClause.__init__)
    params = list(sig.parameters.keys())
    assert "localName" in params, "Missing parameter 'localName'"

def test_adb::componentclause_has_localName():
    assert hasattr(adb::ComponentClause, "localName")
    descriptor = None
    for klass in adb::ComponentClause.__mro__:
        if "localName" in klass.__dict__:
            descriptor = klass.__dict__["localName"]
            break
    assert isinstance(descriptor, property)



def test_adb::modclause_is_not_abstract():
    assert not inspect.isabstract(adb::ModClause)


def test_adb::modclause_constructor_exists():
    assert callable(adb::ModClause.__init__)


def test_adb::modclause_constructor_args():
    sig = inspect.signature(adb::ModClause.__init__)
    params = list(sig.parameters.keys())



def test_realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(RealTypeDefinition)


def test_realtypedefinition_constructor_exists():
    assert callable(RealTypeDefinition.__init__)


def test_realtypedefinition_constructor_args():
    sig = inspect.signature(RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::fixedpointdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::FixedPointDefinition)


def test_adb::fixedpointdefinition_constructor_exists():
    assert callable(adb::FixedPointDefinition.__init__)


def test_adb::fixedpointdefinition_constructor_args():
    sig = inspect.signature(adb::FixedPointDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::floatingpointdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::FloatingPointDefinition)


def test_adb::floatingpointdefinition_constructor_exists():
    assert callable(adb::FloatingPointDefinition.__init__)


def test_adb::floatingpointdefinition_constructor_args():
    sig = inspect.signature(adb::FloatingPointDefinition.__init__)
    params = list(sig.parameters.keys())



def test_componentitem_is_not_abstract():
    assert not inspect.isabstract(ComponentItem)


def test_componentitem_constructor_exists():
    assert callable(ComponentItem.__init__)


def test_componentitem_constructor_args():
    sig = inspect.signature(ComponentItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::variantpart_is_not_abstract():
    assert not inspect.isabstract(adb::VariantPart)


def test_adb::variantpart_constructor_exists():
    assert callable(adb::VariantPart.__init__)


def test_adb::variantpart_constructor_args():
    sig = inspect.signature(adb::VariantPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::variantpart_has_name():
    assert hasattr(adb::VariantPart, "name")
    descriptor = None
    for klass in adb::VariantPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::optvariantpart_is_not_abstract():
    assert not inspect.isabstract(adb::OptVariantPart)


def test_adb::optvariantpart_constructor_exists():
    assert callable(adb::OptVariantPart.__init__)


def test_adb::optvariantpart_constructor_args():
    sig = inspect.signature(adb::OptVariantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentitem_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentItem)


def test_adb::componentitem_constructor_exists():
    assert callable(adb::ComponentItem.__init__)


def test_adb::componentitem_constructor_args():
    sig = inspect.signature(adb::ComponentItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentlist_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentList)


def test_adb::componentlist_constructor_exists():
    assert callable(adb::ComponentList.__init__)


def test_adb::componentlist_constructor_args():
    sig = inspect.signature(adb::ComponentList.__init__)
    params = list(sig.parameters.keys())



def test_adb::simpleexpression_is_not_abstract():
    assert not inspect.isabstract(adb::SimpleExpression)


def test_adb::simpleexpression_constructor_exists():
    assert callable(adb::SimpleExpression.__init__)


def test_adb::simpleexpression_constructor_args():
    sig = inspect.signature(adb::SimpleExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unaryAddingOperator" in params, "Missing parameter 'unaryAddingOperator'"
    assert "binaryAddingOperators" in params, "Missing parameter 'binaryAddingOperators'"

def test_adb::simpleexpression_has_unaryAddingOperator():
    assert hasattr(adb::SimpleExpression, "unaryAddingOperator")
    descriptor = None
    for klass in adb::SimpleExpression.__mro__:
        if "unaryAddingOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryAddingOperator"]
            break
    assert isinstance(descriptor, property)

def test_adb::simpleexpression_has_binaryAddingOperators():
    assert hasattr(adb::SimpleExpression, "binaryAddingOperators")
    descriptor = None
    for klass in adb::SimpleExpression.__mro__:
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



def test_adb::modulartypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::ModularTypeDefinition)


def test_adb::modulartypedefinition_constructor_exists():
    assert callable(adb::ModularTypeDefinition.__init__)


def test_adb::modulartypedefinition_constructor_args():
    sig = inspect.signature(adb::ModularTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::signedintegertypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::SignedIntegerTypeDefinition)


def test_adb::signedintegertypedefinition_constructor_exists():
    assert callable(adb::SignedIntegerTypeDefinition.__init__)


def test_adb::signedintegertypedefinition_constructor_args():
    sig = inspect.signature(adb::SignedIntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::parameterspecification_is_not_abstract():
    assert not inspect.isabstract(adb::ParameterSpecification)


def test_adb::parameterspecification_constructor_exists():
    assert callable(adb::ParameterSpecification.__init__)


def test_adb::parameterspecification_constructor_args():
    sig = inspect.signature(adb::ParameterSpecification.__init__)
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



def test_adb::constrainedindexes_is_not_abstract():
    assert not inspect.isabstract(adb::ConstrainedIndexes)


def test_adb::constrainedindexes_constructor_exists():
    assert callable(adb::ConstrainedIndexes.__init__)


def test_adb::constrainedindexes_constructor_args():
    sig = inspect.signature(adb::ConstrainedIndexes.__init__)
    params = list(sig.parameters.keys())



def test_adb::unconstrainedindexes_is_not_abstract():
    assert not inspect.isabstract(adb::UnconstrainedIndexes)


def test_adb::unconstrainedindexes_constructor_exists():
    assert callable(adb::UnconstrainedIndexes.__init__)


def test_adb::unconstrainedindexes_constructor_args():
    sig = inspect.signature(adb::UnconstrainedIndexes.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentDefinition)


def test_adb::componentdefinition_constructor_exists():
    assert callable(adb::ComponentDefinition.__init__)


def test_adb::componentdefinition_constructor_args():
    sig = inspect.signature(adb::ComponentDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "aliased" in params, "Missing parameter 'aliased'"

def test_adb::componentdefinition_has_aliased():
    assert hasattr(adb::ComponentDefinition, "aliased")
    descriptor = None
    for klass in adb::ComponentDefinition.__mro__:
        if "aliased" in klass.__dict__:
            descriptor = klass.__dict__["aliased"]
            break
    assert isinstance(descriptor, property)



def test_adb::arrayindexes_is_not_abstract():
    assert not inspect.isabstract(adb::ArrayIndexes)


def test_adb::arrayindexes_constructor_exists():
    assert callable(adb::ArrayIndexes.__init__)


def test_adb::arrayindexes_constructor_args():
    sig = inspect.signature(adb::ArrayIndexes.__init__)
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



def test_adb::accesstodatadefinition_is_not_abstract():
    assert not inspect.isabstract(adb::AccessToDataDefinition)


def test_adb::accesstodatadefinition_constructor_exists():
    assert callable(adb::AccessToDataDefinition.__init__)


def test_adb::accesstodatadefinition_constructor_args():
    sig = inspect.signature(adb::AccessToDataDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "generalAccessModifier" in params, "Missing parameter 'generalAccessModifier'"

def test_adb::accesstodatadefinition_has_generalAccessModifier():
    assert hasattr(adb::AccessToDataDefinition, "generalAccessModifier")
    descriptor = None
    for klass in adb::AccessToDataDefinition.__mro__:
        if "generalAccessModifier" in klass.__dict__:
            descriptor = klass.__dict__["generalAccessModifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::accesstosubprogramdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::AccessToSubprogramDefinition)


def test_adb::accesstosubprogramdefinition_constructor_exists():
    assert callable(adb::AccessToSubprogramDefinition.__init__)


def test_adb::accesstosubprogramdefinition_constructor_args():
    sig = inspect.signature(adb::AccessToSubprogramDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "protected" in params, "Missing parameter 'protected'"

def test_adb::accesstosubprogramdefinition_has_protected():
    assert hasattr(adb::AccessToSubprogramDefinition, "protected")
    descriptor = None
    for klass in adb::AccessToSubprogramDefinition.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_adb::accessspecification_is_not_abstract():
    assert not inspect.isabstract(adb::AccessSpecification)


def test_adb::accessspecification_constructor_exists():
    assert callable(adb::AccessSpecification.__init__)


def test_adb::accessspecification_constructor_args():
    sig = inspect.signature(adb::AccessSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::accesstodatainstance_is_not_abstract():
    assert not inspect.isabstract(adb::AccessToDataInstance)


def test_adb::accesstodatainstance_constructor_exists():
    assert callable(adb::AccessToDataInstance.__init__)


def test_adb::accesstodatainstance_constructor_args():
    sig = inspect.signature(adb::AccessToDataInstance.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_adb::accesstodatainstance_has_constant():
    assert hasattr(adb::AccessToDataInstance, "constant")
    descriptor = None
    for klass in adb::AccessToDataInstance.__mro__:
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



def test_adb::integertypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::IntegerTypeDefinition)


def test_adb::integertypedefinition_constructor_exists():
    assert callable(adb::IntegerTypeDefinition.__init__)


def test_adb::integertypedefinition_constructor_args():
    sig = inspect.signature(adb::IntegerTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::enumerationtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::EnumerationTypeDefinition)


def test_adb::enumerationtypedefinition_constructor_exists():
    assert callable(adb::EnumerationTypeDefinition.__init__)


def test_adb::enumerationtypedefinition_constructor_args():
    sig = inspect.signature(adb::EnumerationTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "enumerationliteralspecifications" in params, "Missing parameter 'enumerationliteralspecifications'"

def test_adb::enumerationtypedefinition_has_enumerationliteralspecifications():
    assert hasattr(adb::EnumerationTypeDefinition, "enumerationliteralspecifications")
    descriptor = None
    for klass in adb::EnumerationTypeDefinition.__mro__:
        if "enumerationliteralspecifications" in klass.__dict__:
            descriptor = klass.__dict__["enumerationliteralspecifications"]
            break
    assert isinstance(descriptor, property)



def test_adb::derivedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::DerivedTypeDefinition)


def test_adb::derivedtypedefinition_constructor_exists():
    assert callable(adb::DerivedTypeDefinition.__init__)


def test_adb::derivedtypedefinition_constructor_args():
    sig = inspect.signature(adb::DerivedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_adb::derivedtypedefinition_has_limited():
    assert hasattr(adb::DerivedTypeDefinition, "limited")
    descriptor = None
    for klass in adb::DerivedTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb::derivedtypedefinition_has_abstract():
    assert hasattr(adb::DerivedTypeDefinition, "abstract")
    descriptor = None
    for klass in adb::DerivedTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_adb::recordtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::RecordTypeDefinition)


def test_adb::recordtypedefinition_constructor_exists():
    assert callable(adb::RecordTypeDefinition.__init__)


def test_adb::recordtypedefinition_constructor_args():
    sig = inspect.signature(adb::RecordTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "tagged" in params, "Missing parameter 'tagged'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "limited" in params, "Missing parameter 'limited'"

def test_adb::recordtypedefinition_has_tagged():
    assert hasattr(adb::RecordTypeDefinition, "tagged")
    descriptor = None
    for klass in adb::RecordTypeDefinition.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)

def test_adb::recordtypedefinition_has_abstract():
    assert hasattr(adb::RecordTypeDefinition, "abstract")
    descriptor = None
    for klass in adb::RecordTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb::recordtypedefinition_has_limited():
    assert hasattr(adb::RecordTypeDefinition, "limited")
    descriptor = None
    for klass in adb::RecordTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)



def test_adb::realtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::RealTypeDefinition)


def test_adb::realtypedefinition_constructor_exists():
    assert callable(adb::RealTypeDefinition.__init__)


def test_adb::realtypedefinition_constructor_args():
    sig = inspect.signature(adb::RealTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::notnullaccessdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::NotNullAccessDefinition)


def test_adb::notnullaccessdefinition_constructor_exists():
    assert callable(adb::NotNullAccessDefinition.__init__)


def test_adb::notnullaccessdefinition_constructor_args():
    sig = inspect.signature(adb::NotNullAccessDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::discriminantspecification_is_not_abstract():
    assert not inspect.isabstract(adb::DiscriminantSpecification)


def test_adb::discriminantspecification_constructor_exists():
    assert callable(adb::DiscriminantSpecification.__init__)


def test_adb::discriminantspecification_constructor_args():
    sig = inspect.signature(adb::DiscriminantSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::recorddefinition_is_not_abstract():
    assert not inspect.isabstract(adb::RecordDefinition)


def test_adb::recorddefinition_constructor_exists():
    assert callable(adb::RecordDefinition.__init__)


def test_adb::recorddefinition_constructor_args():
    sig = inspect.signature(adb::RecordDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_adb::recorddefinition_has_null():
    assert hasattr(adb::RecordDefinition, "null")
    descriptor = None
    for klass in adb::RecordDefinition.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_adb::recordextensionpart_is_not_abstract():
    assert not inspect.isabstract(adb::RecordExtensionPart)


def test_adb::recordextensionpart_constructor_exists():
    assert callable(adb::RecordExtensionPart.__init__)


def test_adb::recordextensionpart_constructor_args():
    sig = inspect.signature(adb::RecordExtensionPart.__init__)
    params = list(sig.parameters.keys())



def test_discriminantpart_is_not_abstract():
    assert not inspect.isabstract(DiscriminantPart)


def test_discriminantpart_constructor_exists():
    assert callable(DiscriminantPart.__init__)


def test_discriminantpart_constructor_args():
    sig = inspect.signature(DiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::unknowndiscriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb::UnknownDiscriminantPart)


def test_adb::unknowndiscriminantpart_constructor_exists():
    assert callable(adb::UnknownDiscriminantPart.__init__)


def test_adb::unknowndiscriminantpart_constructor_args():
    sig = inspect.signature(adb::UnknownDiscriminantPart.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb::unknowndiscriminantpart_has_box():
    assert hasattr(adb::UnknownDiscriminantPart, "box")
    descriptor = None
    for klass in adb::UnknownDiscriminantPart.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb::explicitgenericactualparameter_is_not_abstract():
    assert not inspect.isabstract(adb::ExplicitGenericActualParameter)


def test_adb::explicitgenericactualparameter_constructor_exists():
    assert callable(adb::ExplicitGenericActualParameter.__init__)


def test_adb::explicitgenericactualparameter_constructor_args():
    sig = inspect.signature(adb::ExplicitGenericActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_abortstatement_is_not_abstract():
    assert not inspect.isabstract(AbortStatement)


def test_abortstatement_constructor_exists():
    assert callable(AbortStatement.__init__)


def test_abortstatement_constructor_args():
    sig = inspect.signature(AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::tasknames_is_not_abstract():
    assert not inspect.isabstract(adb::TaskNames)


def test_adb::tasknames_constructor_exists():
    assert callable(adb::TaskNames.__init__)


def test_adb::tasknames_constructor_args():
    sig = inspect.signature(adb::TaskNames.__init__)
    params = list(sig.parameters.keys())



def test_adb::entrycallalternative_is_not_abstract():
    assert not inspect.isabstract(adb::EntryCallAlternative)


def test_adb::entrycallalternative_constructor_exists():
    assert callable(adb::EntryCallAlternative.__init__)


def test_adb::entrycallalternative_constructor_args():
    sig = inspect.signature(adb::EntryCallAlternative.__init__)
    params = list(sig.parameters.keys())



def test_selectalternative_is_not_abstract():
    assert not inspect.isabstract(SelectAlternative)


def test_selectalternative_constructor_exists():
    assert callable(SelectAlternative.__init__)


def test_selectalternative_constructor_args():
    sig = inspect.signature(SelectAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::delayalternative_is_not_abstract():
    assert not inspect.isabstract(adb::DelayAlternative)


def test_adb::delayalternative_constructor_exists():
    assert callable(adb::DelayAlternative.__init__)


def test_adb::delayalternative_constructor_args():
    sig = inspect.signature(adb::DelayAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::acceptalternative_is_not_abstract():
    assert not inspect.isabstract(adb::AcceptAlternative)


def test_adb::acceptalternative_constructor_exists():
    assert callable(adb::AcceptAlternative.__init__)


def test_adb::acceptalternative_constructor_args():
    sig = inspect.signature(adb::AcceptAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::guardedalternative_is_not_abstract():
    assert not inspect.isabstract(adb::GuardedAlternative)


def test_adb::guardedalternative_constructor_exists():
    assert callable(adb::GuardedAlternative.__init__)


def test_adb::guardedalternative_constructor_args():
    sig = inspect.signature(adb::GuardedAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::selectalternative_is_not_abstract():
    assert not inspect.isabstract(adb::SelectAlternative)


def test_adb::selectalternative_constructor_exists():
    assert callable(adb::SelectAlternative.__init__)


def test_adb::selectalternative_constructor_args():
    sig = inspect.signature(adb::SelectAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::guard_is_not_abstract():
    assert not inspect.isabstract(adb::Guard)


def test_adb::guard_constructor_exists():
    assert callable(adb::Guard.__init__)


def test_adb::guard_constructor_args():
    sig = inspect.signature(adb::Guard.__init__)
    params = list(sig.parameters.keys())



def test_selectstatement_is_not_abstract():
    assert not inspect.isabstract(SelectStatement)


def test_selectstatement_constructor_exists():
    assert callable(SelectStatement.__init__)


def test_selectstatement_constructor_args():
    sig = inspect.signature(SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::conditionalentrycall_is_not_abstract():
    assert not inspect.isabstract(adb::ConditionalEntryCall)


def test_adb::conditionalentrycall_constructor_exists():
    assert callable(adb::ConditionalEntryCall.__init__)


def test_adb::conditionalentrycall_constructor_args():
    sig = inspect.signature(adb::ConditionalEntryCall.__init__)
    params = list(sig.parameters.keys())



def test_adb::timedentrycall_is_not_abstract():
    assert not inspect.isabstract(adb::TimedEntryCall)


def test_adb::timedentrycall_constructor_exists():
    assert callable(adb::TimedEntryCall.__init__)


def test_adb::timedentrycall_constructor_args():
    sig = inspect.signature(adb::TimedEntryCall.__init__)
    params = list(sig.parameters.keys())



def test_adb::selectiveaccept_is_not_abstract():
    assert not inspect.isabstract(adb::SelectiveAccept)


def test_adb::selectiveaccept_constructor_exists():
    assert callable(adb::SelectiveAccept.__init__)


def test_adb::selectiveaccept_constructor_args():
    sig = inspect.signature(adb::SelectiveAccept.__init__)
    params = list(sig.parameters.keys())



def test_adb::triggeringstatement_is_not_abstract():
    assert not inspect.isabstract(adb::TriggeringStatement)


def test_adb::triggeringstatement_constructor_exists():
    assert callable(adb::TriggeringStatement.__init__)


def test_adb::triggeringstatement_constructor_args():
    sig = inspect.signature(adb::TriggeringStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::abortablepart_is_not_abstract():
    assert not inspect.isabstract(adb::AbortablePart)


def test_adb::abortablepart_constructor_exists():
    assert callable(adb::AbortablePart.__init__)


def test_adb::abortablepart_constructor_args():
    sig = inspect.signature(adb::AbortablePart.__init__)
    params = list(sig.parameters.keys())



def test_adb::triggeringalternative_is_not_abstract():
    assert not inspect.isabstract(adb::TriggeringAlternative)


def test_adb::triggeringalternative_constructor_exists():
    assert callable(adb::TriggeringAlternative.__init__)


def test_adb::triggeringalternative_constructor_args():
    sig = inspect.signature(adb::TriggeringAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::asynchronousselect_is_not_abstract():
    assert not inspect.isabstract(adb::AsynchronousSelect)


def test_adb::asynchronousselect_constructor_exists():
    assert callable(adb::AsynchronousSelect.__init__)


def test_adb::asynchronousselect_constructor_args():
    sig = inspect.signature(adb::AsynchronousSelect.__init__)
    params = list(sig.parameters.keys())



def test_adb::entryindexspecification_is_not_abstract():
    assert not inspect.isabstract(adb::EntryIndexSpecification)


def test_adb::entryindexspecification_constructor_exists():
    assert callable(adb::EntryIndexSpecification.__init__)


def test_adb::entryindexspecification_constructor_args():
    sig = inspect.signature(adb::EntryIndexSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::entryindexspecification_has_name():
    assert hasattr(adb::EntryIndexSpecification, "name")
    descriptor = None
    for klass in adb::EntryIndexSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::entrybarrier_is_not_abstract():
    assert not inspect.isabstract(adb::EntryBarrier)


def test_adb::entrybarrier_constructor_exists():
    assert callable(adb::EntryBarrier.__init__)


def test_adb::entrybarrier_constructor_args():
    sig = inspect.signature(adb::EntryBarrier.__init__)
    params = list(sig.parameters.keys())



def test_adb::entrybodyformalpart_is_not_abstract():
    assert not inspect.isabstract(adb::EntryBodyFormalPart)


def test_adb::entrybodyformalpart_constructor_exists():
    assert callable(adb::EntryBodyFormalPart.__init__)


def test_adb::entrybodyformalpart_constructor_args():
    sig = inspect.signature(adb::EntryBodyFormalPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::entryindex_is_not_abstract():
    assert not inspect.isabstract(adb::EntryIndex)


def test_adb::entryindex_constructor_exists():
    assert callable(adb::EntryIndex.__init__)


def test_adb::entryindex_constructor_args():
    sig = inspect.signature(adb::EntryIndex.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedoperationitem_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedOperationItem)


def test_adb::protectedoperationitem_constructor_exists():
    assert callable(adb::ProtectedOperationItem.__init__)


def test_adb::protectedoperationitem_constructor_args():
    sig = inspect.signature(adb::ProtectedOperationItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::returnsubtypeindication_is_not_abstract():
    assert not inspect.isabstract(adb::ReturnSubtypeIndication)


def test_adb::returnsubtypeindication_constructor_exists():
    assert callable(adb::ReturnSubtypeIndication.__init__)


def test_adb::returnsubtypeindication_constructor_args():
    sig = inspect.signature(adb::ReturnSubtypeIndication.__init__)
    params = list(sig.parameters.keys())



def test_triggeringstatement_is_not_abstract():
    assert not inspect.isabstract(TriggeringStatement)


def test_triggeringstatement_constructor_exists():
    assert callable(TriggeringStatement.__init__)


def test_triggeringstatement_constructor_args():
    sig = inspect.signature(TriggeringStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::loopparameterspecification_is_not_abstract():
    assert not inspect.isabstract(adb::LoopParameterSpecification)


def test_adb::loopparameterspecification_constructor_exists():
    assert callable(adb::LoopParameterSpecification.__init__)


def test_adb::loopparameterspecification_constructor_args():
    sig = inspect.signature(adb::LoopParameterSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb::loopparameterspecification_has_identifier():
    assert hasattr(adb::LoopParameterSpecification, "identifier")
    descriptor = None
    for klass in adb::LoopParameterSpecification.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::iterationscheme_is_not_abstract():
    assert not inspect.isabstract(adb::IterationScheme)


def test_adb::iterationscheme_constructor_exists():
    assert callable(adb::IterationScheme.__init__)


def test_adb::iterationscheme_constructor_args():
    sig = inspect.signature(adb::IterationScheme.__init__)
    params = list(sig.parameters.keys())



def test_compoundstatement_is_not_abstract():
    assert not inspect.isabstract(CompoundStatement)


def test_compoundstatement_constructor_exists():
    assert callable(CompoundStatement.__init__)


def test_compoundstatement_constructor_args():
    sig = inspect.signature(CompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::extendedreturnstatement_is_not_abstract():
    assert not inspect.isabstract(adb::ExtendedReturnStatement)


def test_adb::extendedreturnstatement_constructor_exists():
    assert callable(adb::ExtendedReturnStatement.__init__)


def test_adb::extendedreturnstatement_constructor_args():
    sig = inspect.signature(adb::ExtendedReturnStatement.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb::extendedreturnstatement_has_identifier():
    assert hasattr(adb::ExtendedReturnStatement, "identifier")
    descriptor = None
    for klass in adb::ExtendedReturnStatement.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::selectstatement_is_not_abstract():
    assert not inspect.isabstract(adb::SelectStatement)


def test_adb::selectstatement_constructor_exists():
    assert callable(adb::SelectStatement.__init__)


def test_adb::selectstatement_constructor_args():
    sig = inspect.signature(adb::SelectStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::acceptstatement_is_not_abstract():
    assert not inspect.isabstract(adb::AcceptStatement)


def test_adb::acceptstatement_constructor_exists():
    assert callable(adb::AcceptStatement.__init__)


def test_adb::acceptstatement_constructor_args():
    sig = inspect.signature(adb::AcceptStatement.__init__)
    params = list(sig.parameters.keys())
    assert "entryidentifier" in params, "Missing parameter 'entryidentifier'"

def test_adb::acceptstatement_has_entryidentifier():
    assert hasattr(adb::AcceptStatement, "entryidentifier")
    descriptor = None
    for klass in adb::AcceptStatement.__mro__:
        if "entryidentifier" in klass.__dict__:
            descriptor = klass.__dict__["entryidentifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::loopstatement_is_not_abstract():
    assert not inspect.isabstract(adb::LoopStatement)


def test_adb::loopstatement_constructor_exists():
    assert callable(adb::LoopStatement.__init__)


def test_adb::loopstatement_constructor_args():
    sig = inspect.signature(adb::LoopStatement.__init__)
    params = list(sig.parameters.keys())
    assert "sameName" in params, "Missing parameter 'sameName'"
    assert "name" in params, "Missing parameter 'name'"

def test_adb::loopstatement_has_sameName():
    assert hasattr(adb::LoopStatement, "sameName")
    descriptor = None
    for klass in adb::LoopStatement.__mro__:
        if "sameName" in klass.__dict__:
            descriptor = klass.__dict__["sameName"]
            break
    assert isinstance(descriptor, property)

def test_adb::loopstatement_has_name():
    assert hasattr(adb::LoopStatement, "name")
    descriptor = None
    for klass in adb::LoopStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::ifstatement_is_not_abstract():
    assert not inspect.isabstract(adb::IfStatement)


def test_adb::ifstatement_constructor_exists():
    assert callable(adb::IfStatement.__init__)


def test_adb::ifstatement_constructor_args():
    sig = inspect.signature(adb::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::pragmaargumentassociation_is_not_abstract():
    assert not inspect.isabstract(adb::PragmaArgumentAssociation)


def test_adb::pragmaargumentassociation_constructor_exists():
    assert callable(adb::PragmaArgumentAssociation.__init__)


def test_adb::pragmaargumentassociation_constructor_args():
    sig = inspect.signature(adb::PragmaArgumentAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::pragmaargumentassociation_has_name():
    assert hasattr(adb::PragmaArgumentAssociation, "name")
    descriptor = None
    for klass in adb::PragmaArgumentAssociation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::discretechoicelist_is_not_abstract():
    assert not inspect.isabstract(adb::DiscreteChoiceList)


def test_adb::discretechoicelist_constructor_exists():
    assert callable(adb::DiscreteChoiceList.__init__)


def test_adb::discretechoicelist_constructor_args():
    sig = inspect.signature(adb::DiscreteChoiceList.__init__)
    params = list(sig.parameters.keys())



def test_adb::casestatementalternative_is_not_abstract():
    assert not inspect.isabstract(adb::CaseStatementAlternative)


def test_adb::casestatementalternative_constructor_exists():
    assert callable(adb::CaseStatementAlternative.__init__)


def test_adb::casestatementalternative_constructor_args():
    sig = inspect.signature(adb::CaseStatementAlternative.__init__)
    params = list(sig.parameters.keys())



def test_adb::casestatement_is_not_abstract():
    assert not inspect.isabstract(adb::CaseStatement)


def test_adb::casestatement_constructor_exists():
    assert callable(adb::CaseStatement.__init__)


def test_adb::casestatement_constructor_args():
    sig = inspect.signature(adb::CaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_objectdeclaration_is_not_abstract():
    assert not inspect.isabstract(ObjectDeclaration)


def test_objectdeclaration_constructor_exists():
    assert callable(ObjectDeclaration.__init__)


def test_objectdeclaration_constructor_args():
    sig = inspect.signature(ObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::datainstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::DataInstanceDeclaration)


def test_adb::datainstancedeclaration_constructor_exists():
    assert callable(adb::DataInstanceDeclaration.__init__)


def test_adb::datainstancedeclaration_constructor_args():
    sig = inspect.signature(adb::DataInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "aliased" in params, "Missing parameter 'aliased'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_adb::datainstancedeclaration_has_aliased():
    assert hasattr(adb::DataInstanceDeclaration, "aliased")
    descriptor = None
    for klass in adb::DataInstanceDeclaration.__mro__:
        if "aliased" in klass.__dict__:
            descriptor = klass.__dict__["aliased"]
            break
    assert isinstance(descriptor, property)

def test_adb::datainstancedeclaration_has_constant():
    assert hasattr(adb::DataInstanceDeclaration, "constant")
    descriptor = None
    for klass in adb::DataInstanceDeclaration.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_adb::genericassociation_is_not_abstract():
    assert not inspect.isabstract(adb::GenericAssociation)


def test_adb::genericassociation_constructor_exists():
    assert callable(adb::GenericAssociation.__init__)


def test_adb::genericassociation_constructor_args():
    sig = inspect.signature(adb::GenericAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "selectorName" in params, "Missing parameter 'selectorName'"

def test_adb::genericassociation_has_selectorName():
    assert hasattr(adb::GenericAssociation, "selectorName")
    descriptor = None
    for klass in adb::GenericAssociation.__mro__:
        if "selectorName" in klass.__dict__:
            descriptor = klass.__dict__["selectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb::formalpackageassociation_is_not_abstract():
    assert not inspect.isabstract(adb::FormalPackageAssociation)


def test_adb::formalpackageassociation_constructor_exists():
    assert callable(adb::FormalPackageAssociation.__init__)


def test_adb::formalpackageassociation_constructor_args():
    sig = inspect.signature(adb::FormalPackageAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "genericFormalParameterSelectorName" in params, "Missing parameter 'genericFormalParameterSelectorName'"

def test_adb::formalpackageassociation_has_genericFormalParameterSelectorName():
    assert hasattr(adb::FormalPackageAssociation, "genericFormalParameterSelectorName")
    descriptor = None
    for klass in adb::FormalPackageAssociation.__mro__:
        if "genericFormalParameterSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["genericFormalParameterSelectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb::formalpackageactualpart_is_not_abstract():
    assert not inspect.isabstract(adb::FormalPackageActualPart)


def test_adb::formalpackageactualpart_constructor_exists():
    assert callable(adb::FormalPackageActualPart.__init__)


def test_adb::formalpackageactualpart_constructor_args():
    sig = inspect.signature(adb::FormalPackageActualPart.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb::formalpackageactualpart_has_box():
    assert hasattr(adb::FormalPackageActualPart, "box")
    descriptor = None
    for klass in adb::FormalPackageActualPart.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb::subprogramdefault_is_not_abstract():
    assert not inspect.isabstract(adb::SubprogramDefault)


def test_adb::subprogramdefault_constructor_exists():
    assert callable(adb::SubprogramDefault.__init__)


def test_adb::subprogramdefault_constructor_args():
    sig = inspect.signature(adb::SubprogramDefault.__init__)
    params = list(sig.parameters.keys())
    assert "defaultName" in params, "Missing parameter 'defaultName'"

def test_adb::subprogramdefault_has_defaultName():
    assert hasattr(adb::SubprogramDefault, "defaultName")
    descriptor = None
    for klass in adb::SubprogramDefault.__mro__:
        if "defaultName" in klass.__dict__:
            descriptor = klass.__dict__["defaultName"]
            break
    assert isinstance(descriptor, property)



def test_adb::anonymousaccessdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::AnonymousAccessDefinition)


def test_adb::anonymousaccessdefinition_constructor_exists():
    assert callable(adb::AnonymousAccessDefinition.__init__)


def test_adb::anonymousaccessdefinition_constructor_args():
    sig = inspect.signature(adb::AnonymousAccessDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::optnullexclusion_is_not_abstract():
    assert not inspect.isabstract(adb::OptNullExclusion)


def test_adb::optnullexclusion_constructor_exists():
    assert callable(adb::OptNullExclusion.__init__)


def test_adb::optnullexclusion_constructor_args():
    sig = inspect.signature(adb::OptNullExclusion.__init__)
    params = list(sig.parameters.keys())
    assert "not_null" in params, "Missing parameter 'not_null'"

def test_adb::optnullexclusion_has_not_null():
    assert hasattr(adb::OptNullExclusion, "not_null")
    descriptor = None
    for klass in adb::OptNullExclusion.__mro__:
        if "not_null" in klass.__dict__:
            descriptor = klass.__dict__["not_null"]
            break
    assert isinstance(descriptor, property)



def test_adb::singleprotecteddeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::SingleProtectedDeclaration)


def test_adb::singleprotecteddeclaration_constructor_exists():
    assert callable(adb::SingleProtectedDeclaration.__init__)


def test_adb::singleprotecteddeclaration_constructor_args():
    sig = inspect.signature(adb::SingleProtectedDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::singleprotecteddeclaration_has_name():
    assert hasattr(adb::SingleProtectedDeclaration, "name")
    descriptor = None
    for klass in adb::SingleProtectedDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::mode_is_not_abstract():
    assert not inspect.isabstract(adb::Mode)


def test_adb::mode_constructor_exists():
    assert callable(adb::Mode.__init__)


def test_adb::mode_constructor_args():
    sig = inspect.signature(adb::Mode.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "in_" in params, "Missing parameter 'in_'"

def test_adb::mode_has_out():
    assert hasattr(adb::Mode, "out")
    descriptor = None
    for klass in adb::Mode.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_adb::mode_has_in_():
    assert hasattr(adb::Mode, "in_")
    descriptor = None
    for klass in adb::Mode.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_adb::definingidentifierlist_is_not_abstract():
    assert not inspect.isabstract(adb::DefiningIdentifierList)


def test_adb::definingidentifierlist_constructor_exists():
    assert callable(adb::DefiningIdentifierList.__init__)


def test_adb::definingidentifierlist_constructor_args():
    sig = inspect.signature(adb::DefiningIdentifierList.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::definingidentifierlist_has_name():
    assert hasattr(adb::DefiningIdentifierList, "name")
    descriptor = None
    for klass in adb::DefiningIdentifierList.__mro__:
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



def test_adb::formalderivedtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::FormalDerivedTypeDefinition)


def test_adb::formalderivedtypedefinition_constructor_exists():
    assert callable(adb::FormalDerivedTypeDefinition.__init__)


def test_adb::formalderivedtypedefinition_constructor_args():
    sig = inspect.signature(adb::FormalDerivedTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "absract" in params, "Missing parameter 'absract'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "limited" in params, "Missing parameter 'limited'"

def test_adb::formalderivedtypedefinition_has_absract():
    assert hasattr(adb::FormalDerivedTypeDefinition, "absract")
    descriptor = None
    for klass in adb::FormalDerivedTypeDefinition.__mro__:
        if "absract" in klass.__dict__:
            descriptor = klass.__dict__["absract"]
            break
    assert isinstance(descriptor, property)

def test_adb::formalderivedtypedefinition_has_synchronized():
    assert hasattr(adb::FormalDerivedTypeDefinition, "synchronized")
    descriptor = None
    for klass in adb::FormalDerivedTypeDefinition.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_adb::formalderivedtypedefinition_has_limited():
    assert hasattr(adb::FormalDerivedTypeDefinition, "limited")
    descriptor = None
    for klass in adb::FormalDerivedTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)



def test_adb::accesstypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::AccessTypeDefinition)


def test_adb::accesstypedefinition_constructor_exists():
    assert callable(adb::AccessTypeDefinition.__init__)


def test_adb::accesstypedefinition_constructor_args():
    sig = inspect.signature(adb::AccessTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::interfacetypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::InterfaceTypeDefinition)


def test_adb::interfacetypedefinition_constructor_exists():
    assert callable(adb::InterfaceTypeDefinition.__init__)


def test_adb::interfacetypedefinition_constructor_args():
    sig = inspect.signature(adb::InterfaceTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "synchro" in params, "Missing parameter 'synchro'"
    assert "limited" in params, "Missing parameter 'limited'"
    assert "task" in params, "Missing parameter 'task'"
    assert "protected" in params, "Missing parameter 'protected'"

def test_adb::interfacetypedefinition_has_synchro():
    assert hasattr(adb::InterfaceTypeDefinition, "synchro")
    descriptor = None
    for klass in adb::InterfaceTypeDefinition.__mro__:
        if "synchro" in klass.__dict__:
            descriptor = klass.__dict__["synchro"]
            break
    assert isinstance(descriptor, property)

def test_adb::interfacetypedefinition_has_limited():
    assert hasattr(adb::InterfaceTypeDefinition, "limited")
    descriptor = None
    for klass in adb::InterfaceTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb::interfacetypedefinition_has_task():
    assert hasattr(adb::InterfaceTypeDefinition, "task")
    descriptor = None
    for klass in adb::InterfaceTypeDefinition.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)

def test_adb::interfacetypedefinition_has_protected():
    assert hasattr(adb::InterfaceTypeDefinition, "protected")
    descriptor = None
    for klass in adb::InterfaceTypeDefinition.__mro__:
        if "protected" in klass.__dict__:
            descriptor = klass.__dict__["protected"]
            break
    assert isinstance(descriptor, property)



def test_adb::arraytypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::ArrayTypeDefinition)


def test_adb::arraytypedefinition_constructor_exists():
    assert callable(adb::ArrayTypeDefinition.__init__)


def test_adb::arraytypedefinition_constructor_args():
    sig = inspect.signature(adb::ArrayTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_genericformalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(GenericFormalParameterDeclaration)


def test_genericformalparameterdeclaration_constructor_exists():
    assert callable(GenericFormalParameterDeclaration.__init__)


def test_genericformalparameterdeclaration_constructor_args():
    sig = inspect.signature(GenericFormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::formalsubprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FormalSubprogramDeclaration)


def test_adb::formalsubprogramdeclaration_constructor_exists():
    assert callable(adb::FormalSubprogramDeclaration.__init__)


def test_adb::formalsubprogramdeclaration_constructor_args():
    sig = inspect.signature(adb::FormalSubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_adb::formalsubprogramdeclaration_has_abstract():
    assert hasattr(adb::FormalSubprogramDeclaration, "abstract")
    descriptor = None
    for klass in adb::FormalSubprogramDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_adb::formalpackagedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FormalPackageDeclaration)


def test_adb::formalpackagedeclaration_constructor_exists():
    assert callable(adb::FormalPackageDeclaration.__init__)


def test_adb::formalpackagedeclaration_constructor_args():
    sig = inspect.signature(adb::FormalPackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "genericPackageName" in params, "Missing parameter 'genericPackageName'"

def test_adb::formalpackagedeclaration_has_name():
    assert hasattr(adb::FormalPackageDeclaration, "name")
    descriptor = None
    for klass in adb::FormalPackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_adb::formalpackagedeclaration_has_genericPackageName():
    assert hasattr(adb::FormalPackageDeclaration, "genericPackageName")
    descriptor = None
    for klass in adb::FormalPackageDeclaration.__mro__:
        if "genericPackageName" in klass.__dict__:
            descriptor = klass.__dict__["genericPackageName"]
            break
    assert isinstance(descriptor, property)



def test_adb::formaltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FormalTypeDeclaration)


def test_adb::formaltypedeclaration_constructor_exists():
    assert callable(adb::FormalTypeDeclaration.__init__)


def test_adb::formaltypedeclaration_constructor_args():
    sig = inspect.signature(adb::FormalTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb::formaltypedeclaration_has_identifier():
    assert hasattr(adb::FormalTypeDeclaration, "identifier")
    descriptor = None
    for klass in adb::FormalTypeDeclaration.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::formalobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FormalObjectDeclaration)


def test_adb::formalobjectdeclaration_constructor_exists():
    assert callable(adb::FormalObjectDeclaration.__init__)


def test_adb::formalobjectdeclaration_constructor_args():
    sig = inspect.signature(adb::FormalObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::formalprivatetypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::FormalPrivateTypeDefinition)


def test_adb::formalprivatetypedefinition_constructor_exists():
    assert callable(adb::FormalPrivateTypeDefinition.__init__)


def test_adb::formalprivatetypedefinition_constructor_args():
    sig = inspect.signature(adb::FormalPrivateTypeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "tagged" in params, "Missing parameter 'tagged'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "limited" in params, "Missing parameter 'limited'"

def test_adb::formalprivatetypedefinition_has_tagged():
    assert hasattr(adb::FormalPrivateTypeDefinition, "tagged")
    descriptor = None
    for klass in adb::FormalPrivateTypeDefinition.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)

def test_adb::formalprivatetypedefinition_has_abstract():
    assert hasattr(adb::FormalPrivateTypeDefinition, "abstract")
    descriptor = None
    for klass in adb::FormalPrivateTypeDefinition.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb::formalprivatetypedefinition_has_limited():
    assert hasattr(adb::FormalPrivateTypeDefinition, "limited")
    descriptor = None
    for klass in adb::FormalPrivateTypeDefinition.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)



def test_adb::formaltypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::FormalTypeDefinition)


def test_adb::formaltypedefinition_constructor_exists():
    assert callable(adb::FormalTypeDefinition.__init__)


def test_adb::formaltypedefinition_constructor_args():
    sig = inspect.signature(adb::FormalTypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_range_is_not_abstract():
    assert not inspect.isabstract(Range)


def test_range_constructor_exists():
    assert callable(Range.__init__)


def test_range_constructor_args():
    sig = inspect.signature(Range.__init__)
    params = list(sig.parameters.keys())



def test_adb::explicitrange_is_not_abstract():
    assert not inspect.isabstract(adb::ExplicitRange)


def test_adb::explicitrange_constructor_exists():
    assert callable(adb::ExplicitRange.__init__)


def test_adb::explicitrange_constructor_args():
    sig = inspect.signature(adb::ExplicitRange.__init__)
    params = list(sig.parameters.keys())



def test_adb::entityrange_is_not_abstract():
    assert not inspect.isabstract(adb::EntityRange)


def test_adb::entityrange_constructor_exists():
    assert callable(adb::EntityRange.__init__)


def test_adb::entityrange_constructor_args():
    sig = inspect.signature(adb::EntityRange.__init__)
    params = list(sig.parameters.keys())



def test_rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(RangeConstraint)


def test_rangeconstraint_constructor_exists():
    assert callable(RangeConstraint.__init__)


def test_rangeconstraint_constructor_args():
    sig = inspect.signature(RangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::parametereffectivevalue_is_not_abstract():
    assert not inspect.isabstract(adb::ParameterEffectiveValue)


def test_adb::parametereffectivevalue_constructor_exists():
    assert callable(adb::ParameterEffectiveValue.__init__)


def test_adb::parametereffectivevalue_constructor_args():
    sig = inspect.signature(adb::ParameterEffectiveValue.__init__)
    params = list(sig.parameters.keys())



def test_adb::attributedesignator_is_not_abstract():
    assert not inspect.isabstract(adb::AttributeDesignator)


def test_adb::attributedesignator_constructor_exists():
    assert callable(adb::AttributeDesignator.__init__)


def test_adb::attributedesignator_constructor_args():
    sig = inspect.signature(adb::AttributeDesignator.__init__)
    params = list(sig.parameters.keys())



def test_adb::primaryname_is_not_abstract():
    assert not inspect.isabstract(adb::PrimaryName)


def test_adb::primaryname_constructor_exists():
    assert callable(adb::PrimaryName.__init__)


def test_adb::primaryname_constructor_args():
    sig = inspect.signature(adb::PrimaryName.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_adb::arraycomponentassociation_is_not_abstract():
    assert not inspect.isabstract(adb::ArrayComponentAssociation)


def test_adb::arraycomponentassociation_constructor_exists():
    assert callable(adb::ArrayComponentAssociation.__init__)


def test_adb::arraycomponentassociation_constructor_args():
    sig = inspect.signature(adb::ArrayComponentAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb::arraycomponentassociation_has_box():
    assert hasattr(adb::ArrayComponentAssociation, "box")
    descriptor = None
    for klass in adb::ArrayComponentAssociation.__mro__:
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



def test_adb::namedarrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb::NamedArrayAggregate)


def test_adb::namedarrayaggregate_constructor_exists():
    assert callable(adb::NamedArrayAggregate.__init__)


def test_adb::namedarrayaggregate_constructor_args():
    sig = inspect.signature(adb::NamedArrayAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb::positionalarrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb::PositionalArrayAggregate)


def test_adb::positionalarrayaggregate_constructor_exists():
    assert callable(adb::PositionalArrayAggregate.__init__)


def test_adb::positionalarrayaggregate_constructor_args():
    sig = inspect.signature(adb::PositionalArrayAggregate.__init__)
    params = list(sig.parameters.keys())
    assert "othersBox" in params, "Missing parameter 'othersBox'"

def test_adb::positionalarrayaggregate_has_othersBox():
    assert hasattr(adb::PositionalArrayAggregate, "othersBox")
    descriptor = None
    for klass in adb::PositionalArrayAggregate.__mro__:
        if "othersBox" in klass.__dict__:
            descriptor = klass.__dict__["othersBox"]
            break
    assert isinstance(descriptor, property)



def test_adb::ancestorpart_is_not_abstract():
    assert not inspect.isabstract(adb::AncestorPart)


def test_adb::ancestorpart_constructor_exists():
    assert callable(adb::AncestorPart.__init__)


def test_adb::ancestorpart_constructor_args():
    sig = inspect.signature(adb::AncestorPart.__init__)
    params = list(sig.parameters.keys())



def test_recordcomponentassociation_is_not_abstract():
    assert not inspect.isabstract(RecordComponentAssociation)


def test_recordcomponentassociation_constructor_exists():
    assert callable(RecordComponentAssociation.__init__)


def test_recordcomponentassociation_constructor_args():
    sig = inspect.signature(RecordComponentAssociation.__init__)
    params = list(sig.parameters.keys())



def test_adb::uninitializedcomponents_is_not_abstract():
    assert not inspect.isabstract(adb::UninitializedComponents)


def test_adb::uninitializedcomponents_constructor_exists():
    assert callable(adb::UninitializedComponents.__init__)


def test_adb::uninitializedcomponents_constructor_args():
    sig = inspect.signature(adb::UninitializedComponents.__init__)
    params = list(sig.parameters.keys())
    assert "box" in params, "Missing parameter 'box'"

def test_adb::uninitializedcomponents_has_box():
    assert hasattr(adb::UninitializedComponents, "box")
    descriptor = None
    for klass in adb::UninitializedComponents.__mro__:
        if "box" in klass.__dict__:
            descriptor = klass.__dict__["box"]
            break
    assert isinstance(descriptor, property)



def test_adb::initializedcomponents_is_not_abstract():
    assert not inspect.isabstract(adb::InitializedComponents)


def test_adb::initializedcomponents_constructor_exists():
    assert callable(adb::InitializedComponents.__init__)


def test_adb::initializedcomponents_constructor_args():
    sig = inspect.signature(adb::InitializedComponents.__init__)
    params = list(sig.parameters.keys())



def test_adb::parameterassociation_is_not_abstract():
    assert not inspect.isabstract(adb::ParameterAssociation)


def test_adb::parameterassociation_constructor_exists():
    assert callable(adb::ParameterAssociation.__init__)


def test_adb::parameterassociation_constructor_args():
    sig = inspect.signature(adb::ParameterAssociation.__init__)
    params = list(sig.parameters.keys())
    assert "selectorName" in params, "Missing parameter 'selectorName'"

def test_adb::parameterassociation_has_selectorName():
    assert hasattr(adb::ParameterAssociation, "selectorName")
    descriptor = None
    for klass in adb::ParameterAssociation.__mro__:
        if "selectorName" in klass.__dict__:
            descriptor = klass.__dict__["selectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb::recordcomponentassociation_is_not_abstract():
    assert not inspect.isabstract(adb::RecordComponentAssociation)


def test_adb::recordcomponentassociation_constructor_exists():
    assert callable(adb::RecordComponentAssociation.__init__)


def test_adb::recordcomponentassociation_constructor_args():
    sig = inspect.signature(adb::RecordComponentAssociation.__init__)
    params = list(sig.parameters.keys())



def test_recordaggregate_is_not_abstract():
    assert not inspect.isabstract(RecordAggregate)


def test_recordaggregate_constructor_exists():
    assert callable(RecordAggregate.__init__)


def test_recordaggregate_constructor_args():
    sig = inspect.signature(RecordAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb::recordcomponentassociationlist_is_not_abstract():
    assert not inspect.isabstract(adb::RecordComponentAssociationList)


def test_adb::recordcomponentassociationlist_constructor_exists():
    assert callable(adb::RecordComponentAssociationList.__init__)


def test_adb::recordcomponentassociationlist_constructor_args():
    sig = inspect.signature(adb::RecordComponentAssociationList.__init__)
    params = list(sig.parameters.keys())
    assert "nullRecord" in params, "Missing parameter 'nullRecord'"

def test_adb::recordcomponentassociationlist_has_nullRecord():
    assert hasattr(adb::RecordComponentAssociationList, "nullRecord")
    descriptor = None
    for klass in adb::RecordComponentAssociationList.__mro__:
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



def test_adb::arrayaggregate_is_not_abstract():
    assert not inspect.isabstract(adb::ArrayAggregate)


def test_adb::arrayaggregate_constructor_exists():
    assert callable(adb::ArrayAggregate.__init__)


def test_adb::arrayaggregate_constructor_args():
    sig = inspect.signature(adb::ArrayAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb::extensionaggregate_is_not_abstract():
    assert not inspect.isabstract(adb::ExtensionAggregate)


def test_adb::extensionaggregate_constructor_exists():
    assert callable(adb::ExtensionAggregate.__init__)


def test_adb::extensionaggregate_constructor_args():
    sig = inspect.signature(adb::ExtensionAggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb::recordaggregate_is_not_abstract():
    assert not inspect.isabstract(adb::RecordAggregate)


def test_adb::recordaggregate_constructor_exists():
    assert callable(adb::RecordAggregate.__init__)


def test_adb::recordaggregate_constructor_args():
    sig = inspect.signature(adb::RecordAggregate.__init__)
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



def test_adb::aggregate_is_not_abstract():
    assert not inspect.isabstract(adb::Aggregate)


def test_adb::aggregate_constructor_exists():
    assert callable(adb::Aggregate.__init__)


def test_adb::aggregate_constructor_args():
    sig = inspect.signature(adb::Aggregate.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentchoicelist_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentChoiceList)


def test_adb::componentchoicelist_constructor_exists():
    assert callable(adb::ComponentChoiceList.__init__)


def test_adb::componentchoicelist_constructor_args():
    sig = inspect.signature(adb::ComponentChoiceList.__init__)
    params = list(sig.parameters.keys())
    assert "componentSelectorName" in params, "Missing parameter 'componentSelectorName'"
    assert "others" in params, "Missing parameter 'others'"

def test_adb::componentchoicelist_has_componentSelectorName():
    assert hasattr(adb::ComponentChoiceList, "componentSelectorName")
    descriptor = None
    for klass in adb::ComponentChoiceList.__mro__:
        if "componentSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["componentSelectorName"]
            break
    assert isinstance(descriptor, property)

def test_adb::componentchoicelist_has_others():
    assert hasattr(adb::ComponentChoiceList, "others")
    descriptor = None
    for klass in adb::ComponentChoiceList.__mro__:
        if "others" in klass.__dict__:
            descriptor = klass.__dict__["others"]
            break
    assert isinstance(descriptor, property)



def test_adb::discriminantselectors_is_not_abstract():
    assert not inspect.isabstract(adb::DiscriminantSelectors)


def test_adb::discriminantselectors_constructor_exists():
    assert callable(adb::DiscriminantSelectors.__init__)


def test_adb::discriminantselectors_constructor_args():
    sig = inspect.signature(adb::DiscriminantSelectors.__init__)
    params = list(sig.parameters.keys())
    assert "discriminantSelectorName" in params, "Missing parameter 'discriminantSelectorName'"

def test_adb::discriminantselectors_has_discriminantSelectorName():
    assert hasattr(adb::DiscriminantSelectors, "discriminantSelectorName")
    descriptor = None
    for klass in adb::DiscriminantSelectors.__mro__:
        if "discriminantSelectorName" in klass.__dict__:
            descriptor = klass.__dict__["discriminantSelectorName"]
            break
    assert isinstance(descriptor, property)



def test_adb::discriminantassociation_is_not_abstract():
    assert not inspect.isabstract(adb::DiscriminantAssociation)


def test_adb::discriminantassociation_constructor_exists():
    assert callable(adb::DiscriminantAssociation.__init__)


def test_adb::discriminantassociation_constructor_args():
    sig = inspect.signature(adb::DiscriminantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_compositeconstraint_is_not_abstract():
    assert not inspect.isabstract(CompositeConstraint)


def test_compositeconstraint_constructor_exists():
    assert callable(CompositeConstraint.__init__)


def test_compositeconstraint_constructor_args():
    sig = inspect.signature(CompositeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::indexconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::IndexConstraint)


def test_adb::indexconstraint_constructor_exists():
    assert callable(adb::IndexConstraint.__init__)


def test_adb::indexconstraint_constructor_args():
    sig = inspect.signature(adb::IndexConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::discriminantconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::DiscriminantConstraint)


def test_adb::discriminantconstraint_constructor_exists():
    assert callable(adb::DiscriminantConstraint.__init__)


def test_adb::discriminantconstraint_constructor_args():
    sig = inspect.signature(adb::DiscriminantConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::compositeconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::CompositeConstraint)


def test_adb::compositeconstraint_constructor_exists():
    assert callable(adb::CompositeConstraint.__init__)


def test_adb::compositeconstraint_constructor_args():
    sig = inspect.signature(adb::CompositeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::optconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::OptConstraint)


def test_adb::optconstraint_constructor_exists():
    assert callable(adb::OptConstraint.__init__)


def test_adb::optconstraint_constructor_args():
    sig = inspect.signature(adb::OptConstraint.__init__)
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



def test_adb::discreterange_is_not_abstract():
    assert not inspect.isabstract(adb::DiscreteRange)


def test_adb::discreterange_constructor_exists():
    assert callable(adb::DiscreteRange.__init__)


def test_adb::discreterange_constructor_args():
    sig = inspect.signature(adb::DiscreteRange.__init__)
    params = list(sig.parameters.keys())



def test_adb::qualifier_is_not_abstract():
    assert not inspect.isabstract(adb::Qualifier)


def test_adb::qualifier_constructor_exists():
    assert callable(adb::Qualifier.__init__)


def test_adb::qualifier_constructor_args():
    sig = inspect.signature(adb::Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_primary_is_not_abstract():
    assert not inspect.isabstract(Primary)


def test_primary_constructor_exists():
    assert callable(Primary.__init__)


def test_primary_constructor_args():
    sig = inspect.signature(Primary.__init__)
    params = list(sig.parameters.keys())



def test_adb::allocator_is_not_abstract():
    assert not inspect.isabstract(adb::Allocator)


def test_adb::allocator_constructor_exists():
    assert callable(adb::Allocator.__init__)


def test_adb::allocator_constructor_args():
    sig = inspect.signature(adb::Allocator.__init__)
    params = list(sig.parameters.keys())



def test_adb::null_is_not_abstract():
    assert not inspect.isabstract(adb::Null)


def test_adb::null_constructor_exists():
    assert callable(adb::Null.__init__)


def test_adb::null_constructor_args():
    sig = inspect.signature(adb::Null.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb::null_has_value():
    assert hasattr(adb::Null, "value")
    descriptor = None
    for klass in adb::Null.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adb::qualifiedname_is_not_abstract():
    assert not inspect.isabstract(adb::QualifiedName)


def test_adb::qualifiedname_constructor_exists():
    assert callable(adb::QualifiedName.__init__)


def test_adb::qualifiedname_constructor_args():
    sig = inspect.signature(adb::QualifiedName.__init__)
    params = list(sig.parameters.keys())



def test_adb::stringliteral_is_not_abstract():
    assert not inspect.isabstract(adb::StringLiteral)


def test_adb::stringliteral_constructor_exists():
    assert callable(adb::StringLiteral.__init__)


def test_adb::stringliteral_constructor_args():
    sig = inspect.signature(adb::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb::stringliteral_has_value():
    assert hasattr(adb::StringLiteral, "value")
    descriptor = None
    for klass in adb::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_adb::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(adb::ParenthesizedExpression)


def test_adb::parenthesizedexpression_constructor_exists():
    assert callable(adb::ParenthesizedExpression.__init__)


def test_adb::parenthesizedexpression_constructor_args():
    sig = inspect.signature(adb::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_adb::numericliteral_is_not_abstract():
    assert not inspect.isabstract(adb::NumericLiteral)


def test_adb::numericliteral_constructor_exists():
    assert callable(adb::NumericLiteral.__init__)


def test_adb::numericliteral_constructor_args():
    sig = inspect.signature(adb::NumericLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_adb::numericliteral_has_value():
    assert hasattr(adb::NumericLiteral, "value")
    descriptor = None
    for klass in adb::NumericLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_scalarconstraint_is_not_abstract():
    assert not inspect.isabstract(ScalarConstraint)


def test_scalarconstraint_constructor_exists():
    assert callable(ScalarConstraint.__init__)


def test_scalarconstraint_constructor_args():
    sig = inspect.signature(ScalarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::deltaconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::DeltaConstraint)


def test_adb::deltaconstraint_constructor_exists():
    assert callable(adb::DeltaConstraint.__init__)


def test_adb::deltaconstraint_constructor_args():
    sig = inspect.signature(adb::DeltaConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::rangeconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::RangeConstraint)


def test_adb::rangeconstraint_constructor_exists():
    assert callable(adb::RangeConstraint.__init__)


def test_adb::rangeconstraint_constructor_args():
    sig = inspect.signature(adb::RangeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::digitsconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::DigitsConstraint)


def test_adb::digitsconstraint_constructor_exists():
    assert callable(adb::DigitsConstraint.__init__)


def test_adb::digitsconstraint_constructor_args():
    sig = inspect.signature(adb::DigitsConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::scalarconstraint_is_not_abstract():
    assert not inspect.isabstract(adb::ScalarConstraint)


def test_adb::scalarconstraint_constructor_exists():
    assert callable(adb::ScalarConstraint.__init__)


def test_adb::scalarconstraint_constructor_args():
    sig = inspect.signature(adb::ScalarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_adb::eobject_is_not_abstract():
    assert not inspect.isabstract(adb::EObject)


def test_adb::eobject_constructor_exists():
    assert callable(adb::EObject.__init__)


def test_adb::eobject_constructor_args():
    sig = inspect.signature(adb::EObject.__init__)
    params = list(sig.parameters.keys())



def test_adb::factor_is_not_abstract():
    assert not inspect.isabstract(adb::Factor)


def test_adb::factor_constructor_exists():
    assert callable(adb::Factor.__init__)


def test_adb::factor_constructor_args():
    sig = inspect.signature(adb::Factor.__init__)
    params = list(sig.parameters.keys())
    assert "abs" in params, "Missing parameter 'abs'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_adb::factor_has_abs():
    assert hasattr(adb::Factor, "abs")
    descriptor = None
    for klass in adb::Factor.__mro__:
        if "abs" in klass.__dict__:
            descriptor = klass.__dict__["abs"]
            break
    assert isinstance(descriptor, property)

def test_adb::factor_has_not_():
    assert hasattr(adb::Factor, "not_")
    descriptor = None
    for klass in adb::Factor.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_adb::term_is_not_abstract():
    assert not inspect.isabstract(adb::Term)


def test_adb::term_constructor_exists():
    assert callable(adb::Term.__init__)


def test_adb::term_constructor_args():
    sig = inspect.signature(adb::Term.__init__)
    params = list(sig.parameters.keys())
    assert "multiplyingOperators" in params, "Missing parameter 'multiplyingOperators'"

def test_adb::term_has_multiplyingOperators():
    assert hasattr(adb::Term, "multiplyingOperators")
    descriptor = None
    for klass in adb::Term.__mro__:
        if "multiplyingOperators" in klass.__dict__:
            descriptor = klass.__dict__["multiplyingOperators"]
            break
    assert isinstance(descriptor, property)



def test_adb::interval_is_not_abstract():
    assert not inspect.isabstract(adb::Interval)


def test_adb::interval_constructor_exists():
    assert callable(adb::Interval.__init__)


def test_adb::interval_constructor_args():
    sig = inspect.signature(adb::Interval.__init__)
    params = list(sig.parameters.keys())



def test_adb::membership_is_not_abstract():
    assert not inspect.isabstract(adb::Membership)


def test_adb::membership_constructor_exists():
    assert callable(adb::Membership.__init__)


def test_adb::membership_constructor_args():
    sig = inspect.signature(adb::Membership.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_adb::membership_has_not_():
    assert hasattr(adb::Membership, "not_")
    descriptor = None
    for klass in adb::Membership.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_adb::relation_is_not_abstract():
    assert not inspect.isabstract(adb::Relation)


def test_adb::relation_constructor_exists():
    assert callable(adb::Relation.__init__)


def test_adb::relation_constructor_args():
    sig = inspect.signature(adb::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "relationalOperator" in params, "Missing parameter 'relationalOperator'"

def test_adb::relation_has_relationalOperator():
    assert hasattr(adb::Relation, "relationalOperator")
    descriptor = None
    for klass in adb::Relation.__mro__:
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



def test_adb::range_is_not_abstract():
    assert not inspect.isabstract(adb::Range)


def test_adb::range_constructor_exists():
    assert callable(adb::Range.__init__)


def test_adb::range_constructor_args():
    sig = inspect.signature(adb::Range.__init__)
    params = list(sig.parameters.keys())



def test_ancestorpart_is_not_abstract():
    assert not inspect.isabstract(AncestorPart)


def test_ancestorpart_constructor_exists():
    assert callable(AncestorPart.__init__)


def test_ancestorpart_constructor_args():
    sig = inspect.signature(AncestorPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::expression_is_not_abstract():
    assert not inspect.isabstract(adb::Expression)


def test_adb::expression_constructor_exists():
    assert callable(adb::Expression.__init__)


def test_adb::expression_constructor_args():
    sig = inspect.signature(adb::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "booleanOperator" in params, "Missing parameter 'booleanOperator'"

def test_adb::expression_has_booleanOperator():
    assert hasattr(adb::Expression, "booleanOperator")
    descriptor = None
    for klass in adb::Expression.__mro__:
        if "booleanOperator" in klass.__dict__:
            descriptor = klass.__dict__["booleanOperator"]
            break
    assert isinstance(descriptor, property)



def test_adb::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(adb::ExceptionHandler)


def test_adb::exceptionhandler_constructor_exists():
    assert callable(adb::ExceptionHandler.__init__)


def test_adb::exceptionhandler_constructor_args():
    sig = inspect.signature(adb::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::exceptionhandler_has_name():
    assert hasattr(adb::ExceptionHandler, "name")
    descriptor = None
    for klass in adb::ExceptionHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::genericitem_is_not_abstract():
    assert not inspect.isabstract(adb::GenericItem)


def test_adb::genericitem_constructor_exists():
    assert callable(adb::GenericItem.__init__)


def test_adb::genericitem_constructor_args():
    sig = inspect.signature(adb::GenericItem.__init__)
    params = list(sig.parameters.keys())



def test_simplestatement_is_not_abstract():
    assert not inspect.isabstract(SimpleStatement)


def test_simplestatement_constructor_exists():
    assert callable(SimpleStatement.__init__)


def test_simplestatement_constructor_args():
    sig = inspect.signature(SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::abortstatement_is_not_abstract():
    assert not inspect.isabstract(adb::AbortStatement)


def test_adb::abortstatement_constructor_exists():
    assert callable(adb::AbortStatement.__init__)


def test_adb::abortstatement_constructor_args():
    sig = inspect.signature(adb::AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::simplereturnstatement_is_not_abstract():
    assert not inspect.isabstract(adb::SimpleReturnStatement)


def test_adb::simplereturnstatement_constructor_exists():
    assert callable(adb::SimpleReturnStatement.__init__)


def test_adb::simplereturnstatement_constructor_args():
    sig = inspect.signature(adb::SimpleReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::gotostatement_is_not_abstract():
    assert not inspect.isabstract(adb::GotoStatement)


def test_adb::gotostatement_constructor_exists():
    assert callable(adb::GotoStatement.__init__)


def test_adb::gotostatement_constructor_args():
    sig = inspect.signature(adb::GotoStatement.__init__)
    params = list(sig.parameters.keys())
    assert "labelId" in params, "Missing parameter 'labelId'"

def test_adb::gotostatement_has_labelId():
    assert hasattr(adb::GotoStatement, "labelId")
    descriptor = None
    for klass in adb::GotoStatement.__mro__:
        if "labelId" in klass.__dict__:
            descriptor = klass.__dict__["labelId"]
            break
    assert isinstance(descriptor, property)



def test_adb::procedureorentrycallstatement_is_not_abstract():
    assert not inspect.isabstract(adb::ProcedureOrEntryCallStatement)


def test_adb::procedureorentrycallstatement_constructor_exists():
    assert callable(adb::ProcedureOrEntryCallStatement.__init__)


def test_adb::procedureorentrycallstatement_constructor_args():
    sig = inspect.signature(adb::ProcedureOrEntryCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::delaystatement_is_not_abstract():
    assert not inspect.isabstract(adb::DelayStatement)


def test_adb::delaystatement_constructor_exists():
    assert callable(adb::DelayStatement.__init__)


def test_adb::delaystatement_constructor_args():
    sig = inspect.signature(adb::DelayStatement.__init__)
    params = list(sig.parameters.keys())
    assert "until" in params, "Missing parameter 'until'"

def test_adb::delaystatement_has_until():
    assert hasattr(adb::DelayStatement, "until")
    descriptor = None
    for klass in adb::DelayStatement.__mro__:
        if "until" in klass.__dict__:
            descriptor = klass.__dict__["until"]
            break
    assert isinstance(descriptor, property)



def test_adb::raisestatement_is_not_abstract():
    assert not inspect.isabstract(adb::RaiseStatement)


def test_adb::raisestatement_constructor_exists():
    assert callable(adb::RaiseStatement.__init__)


def test_adb::raisestatement_constructor_args():
    sig = inspect.signature(adb::RaiseStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(adb::AssignmentStatement)


def test_adb::assignmentstatement_constructor_exists():
    assert callable(adb::AssignmentStatement.__init__)


def test_adb::assignmentstatement_constructor_args():
    sig = inspect.signature(adb::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::requeuestatement_is_not_abstract():
    assert not inspect.isabstract(adb::RequeueStatement)


def test_adb::requeuestatement_constructor_exists():
    assert callable(adb::RequeueStatement.__init__)


def test_adb::requeuestatement_constructor_args():
    sig = inspect.signature(adb::RequeueStatement.__init__)
    params = list(sig.parameters.keys())
    assert "abort" in params, "Missing parameter 'abort'"

def test_adb::requeuestatement_has_abort():
    assert hasattr(adb::RequeueStatement, "abort")
    descriptor = None
    for klass in adb::RequeueStatement.__mro__:
        if "abort" in klass.__dict__:
            descriptor = klass.__dict__["abort"]
            break
    assert isinstance(descriptor, property)



def test_adb::exitstatement_is_not_abstract():
    assert not inspect.isabstract(adb::ExitStatement)


def test_adb::exitstatement_constructor_exists():
    assert callable(adb::ExitStatement.__init__)


def test_adb::exitstatement_constructor_args():
    sig = inspect.signature(adb::ExitStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::nullstatement_is_not_abstract():
    assert not inspect.isabstract(adb::NullStatement)


def test_adb::nullstatement_constructor_exists():
    assert callable(adb::NullStatement.__init__)


def test_adb::nullstatement_constructor_args():
    sig = inspect.signature(adb::NullStatement.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_adb::nullstatement_has_null():
    assert hasattr(adb::NullStatement, "null")
    descriptor = None
    for klass in adb::NullStatement.__mro__:
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



def test_adb::compoundstatement_is_not_abstract():
    assert not inspect.isabstract(adb::CompoundStatement)


def test_adb::compoundstatement_constructor_exists():
    assert callable(adb::CompoundStatement.__init__)


def test_adb::compoundstatement_constructor_args():
    sig = inspect.signature(adb::CompoundStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::simplestatement_is_not_abstract():
    assert not inspect.isabstract(adb::SimpleStatement)


def test_adb::simplestatement_constructor_exists():
    assert callable(adb::SimpleStatement.__init__)


def test_adb::simplestatement_constructor_args():
    sig = inspect.signature(adb::SimpleStatement.__init__)
    params = list(sig.parameters.keys())



def test_adb::statement_is_not_abstract():
    assert not inspect.isabstract(adb::Statement)


def test_adb::statement_constructor_exists():
    assert callable(adb::Statement.__init__)


def test_adb::statement_constructor_args():
    sig = inspect.signature(adb::Statement.__init__)
    params = list(sig.parameters.keys())



def test_adb::labelisablestatement_is_not_abstract():
    assert not inspect.isabstract(adb::LabelisableStatement)


def test_adb::labelisablestatement_constructor_exists():
    assert callable(adb::LabelisableStatement.__init__)


def test_adb::labelisablestatement_constructor_args():
    sig = inspect.signature(adb::LabelisableStatement.__init__)
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



def test_adb::sequenceofstatements_is_not_abstract():
    assert not inspect.isabstract(adb::SequenceOfStatements)


def test_adb::sequenceofstatements_constructor_exists():
    assert callable(adb::SequenceOfStatements.__init__)


def test_adb::sequenceofstatements_constructor_args():
    sig = inspect.signature(adb::SequenceOfStatements.__init__)
    params = list(sig.parameters.keys())



def test_adb::label_is_not_abstract():
    assert not inspect.isabstract(adb::Label)


def test_adb::label_constructor_exists():
    assert callable(adb::Label.__init__)


def test_adb::label_constructor_args():
    sig = inspect.signature(adb::Label.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb::label_has_identifier():
    assert hasattr(adb::Label, "identifier")
    descriptor = None
    for klass in adb::Label.__mro__:
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



def test_adb::bodystub_is_not_abstract():
    assert not inspect.isabstract(adb::BodyStub)


def test_adb::bodystub_constructor_exists():
    assert callable(adb::BodyStub.__init__)


def test_adb::bodystub_constructor_args():
    sig = inspect.signature(adb::BodyStub.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::bodystub_has_name():
    assert hasattr(adb::BodyStub, "name")
    descriptor = None
    for klass in adb::BodyStub.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::properbody_is_not_abstract():
    assert not inspect.isabstract(adb::ProperBody)


def test_adb::properbody_constructor_exists():
    assert callable(adb::ProperBody.__init__)


def test_adb::properbody_constructor_args():
    sig = inspect.signature(adb::ProperBody.__init__)
    params = list(sig.parameters.keys())



def test_protectedelementdeclaration_is_not_abstract():
    assert not inspect.isabstract(ProtectedElementDeclaration)


def test_protectedelementdeclaration_constructor_exists():
    assert callable(ProtectedElementDeclaration.__init__)


def test_protectedelementdeclaration_constructor_args():
    sig = inspect.signature(ProtectedElementDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::componentdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ComponentDeclaration)


def test_adb::componentdeclaration_constructor_exists():
    assert callable(adb::ComponentDeclaration.__init__)


def test_adb::componentdeclaration_constructor_args():
    sig = inspect.signature(adb::ComponentDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedoperationdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedOperationDeclaration)


def test_adb::protectedoperationdeclaration_constructor_exists():
    assert callable(adb::ProtectedOperationDeclaration.__init__)


def test_adb::protectedoperationdeclaration_constructor_args():
    sig = inspect.signature(adb::ProtectedOperationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedelementdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedElementDeclaration)


def test_adb::protectedelementdeclaration_constructor_exists():
    assert callable(adb::ProtectedElementDeclaration.__init__)


def test_adb::protectedelementdeclaration_constructor_args():
    sig = inspect.signature(adb::ProtectedElementDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::protecteddefinition_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedDefinition)


def test_adb::protecteddefinition_constructor_exists():
    assert callable(adb::ProtectedDefinition.__init__)


def test_adb::protecteddefinition_constructor_args():
    sig = inspect.signature(adb::ProtectedDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::formalpart_is_not_abstract():
    assert not inspect.isabstract(adb::FormalPart)


def test_adb::formalpart_constructor_exists():
    assert callable(adb::FormalPart.__init__)


def test_adb::formalpart_constructor_args():
    sig = inspect.signature(adb::FormalPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::discretesubtypedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::DiscreteSubtypeDefinition)


def test_adb::discretesubtypedefinition_constructor_exists():
    assert callable(adb::DiscreteSubtypeDefinition.__init__)


def test_adb::discretesubtypedefinition_constructor_args():
    sig = inspect.signature(adb::DiscreteSubtypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::name_is_not_abstract():
    assert not inspect.isabstract(adb::Name)


def test_adb::name_constructor_exists():
    assert callable(adb::Name.__init__)


def test_adb::name_constructor_args():
    sig = inspect.signature(adb::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::name_has_name():
    assert hasattr(adb::Name, "name")
    descriptor = None
    for klass in adb::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::exceptionchoice_is_not_abstract():
    assert not inspect.isabstract(adb::ExceptionChoice)


def test_adb::exceptionchoice_constructor_exists():
    assert callable(adb::ExceptionChoice.__init__)


def test_adb::exceptionchoice_constructor_args():
    sig = inspect.signature(adb::ExceptionChoice.__init__)
    params = list(sig.parameters.keys())
    assert "others" in params, "Missing parameter 'others'"

def test_adb::exceptionchoice_has_others():
    assert hasattr(adb::ExceptionChoice, "others")
    descriptor = None
    for klass in adb::ExceptionChoice.__mro__:
        if "others" in klass.__dict__:
            descriptor = klass.__dict__["others"]
            break
    assert isinstance(descriptor, property)



def test_adb::parameterandresultprofile_is_not_abstract():
    assert not inspect.isabstract(adb::ParameterAndResultProfile)


def test_adb::parameterandresultprofile_constructor_exists():
    assert callable(adb::ParameterAndResultProfile.__init__)


def test_adb::parameterandresultprofile_constructor_args():
    sig = inspect.signature(adb::ParameterAndResultProfile.__init__)
    params = list(sig.parameters.keys())



def test_subprogramspecification_is_not_abstract():
    assert not inspect.isabstract(SubprogramSpecification)


def test_subprogramspecification_constructor_exists():
    assert callable(SubprogramSpecification.__init__)


def test_subprogramspecification_constructor_args():
    sig = inspect.signature(SubprogramSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::functionspecification_is_not_abstract():
    assert not inspect.isabstract(adb::FunctionSpecification)


def test_adb::functionspecification_constructor_exists():
    assert callable(adb::FunctionSpecification.__init__)


def test_adb::functionspecification_constructor_args():
    sig = inspect.signature(adb::FunctionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::procedurespecification_is_not_abstract():
    assert not inspect.isabstract(adb::ProcedureSpecification)


def test_adb::procedurespecification_constructor_exists():
    assert callable(adb::ProcedureSpecification.__init__)


def test_adb::procedurespecification_constructor_args():
    sig = inspect.signature(adb::ProcedureSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bodystub_is_not_abstract():
    assert not inspect.isabstract(BodyStub)


def test_bodystub_constructor_exists():
    assert callable(BodyStub.__init__)


def test_bodystub_constructor_args():
    sig = inspect.signature(BodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedbodystub_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedBodyStub)


def test_adb::protectedbodystub_constructor_exists():
    assert callable(adb::ProtectedBodyStub.__init__)


def test_adb::protectedbodystub_constructor_args():
    sig = inspect.signature(adb::ProtectedBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb::packagebodystub_is_not_abstract():
    assert not inspect.isabstract(adb::PackageBodyStub)


def test_adb::packagebodystub_constructor_exists():
    assert callable(adb::PackageBodyStub.__init__)


def test_adb::packagebodystub_constructor_args():
    sig = inspect.signature(adb::PackageBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_adb::taskbodystub_is_not_abstract():
    assert not inspect.isabstract(adb::TaskBodyStub)


def test_adb::taskbodystub_constructor_exists():
    assert callable(adb::TaskBodyStub.__init__)


def test_adb::taskbodystub_constructor_args():
    sig = inspect.signature(adb::TaskBodyStub.__init__)
    params = list(sig.parameters.keys())



def test_newtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(NewTypeDeclaration)


def test_newtypedeclaration_constructor_exists():
    assert callable(NewTypeDeclaration.__init__)


def test_newtypedeclaration_constructor_args():
    sig = inspect.signature(NewTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::fulltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FullTypeDeclaration)


def test_adb::fulltypedeclaration_constructor_exists():
    assert callable(adb::FullTypeDeclaration.__init__)


def test_adb::fulltypedeclaration_constructor_args():
    sig = inspect.signature(adb::FullTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(TypeDeclaration)


def test_typedeclaration_constructor_exists():
    assert callable(TypeDeclaration.__init__)


def test_typedeclaration_constructor_args():
    sig = inspect.signature(TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::subtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::SubtypeDeclaration)


def test_adb::subtypedeclaration_constructor_exists():
    assert callable(adb::SubtypeDeclaration.__init__)


def test_adb::subtypedeclaration_constructor_args():
    sig = inspect.signature(adb::SubtypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::newtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::NewTypeDeclaration)


def test_adb::newtypedeclaration_constructor_exists():
    assert callable(adb::NewTypeDeclaration.__init__)


def test_adb::newtypedeclaration_constructor_args():
    sig = inspect.signature(adb::NewTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::taskdefinition_is_not_abstract():
    assert not inspect.isabstract(adb::TaskDefinition)


def test_adb::taskdefinition_constructor_exists():
    assert callable(adb::TaskDefinition.__init__)


def test_adb::taskdefinition_constructor_args():
    sig = inspect.signature(adb::TaskDefinition.__init__)
    params = list(sig.parameters.keys())



def test_adb::interfacelist_is_not_abstract():
    assert not inspect.isabstract(adb::InterfaceList)


def test_adb::interfacelist_constructor_exists():
    assert callable(adb::InterfaceList.__init__)


def test_adb::interfacelist_constructor_args():
    sig = inspect.signature(adb::InterfaceList.__init__)
    params = list(sig.parameters.keys())



def test_adb::knowndiscriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb::KnownDiscriminantPart)


def test_adb::knowndiscriminantpart_constructor_exists():
    assert callable(adb::KnownDiscriminantPart.__init__)


def test_adb::knowndiscriminantpart_constructor_args():
    sig = inspect.signature(adb::KnownDiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_declarativeitem_is_not_abstract():
    assert not inspect.isabstract(DeclarativeItem)


def test_declarativeitem_constructor_exists():
    assert callable(DeclarativeItem.__init__)


def test_declarativeitem_constructor_args():
    sig = inspect.signature(DeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::body_is_not_abstract():
    assert not inspect.isabstract(adb::Body)


def test_adb::body_constructor_exists():
    assert callable(adb::Body.__init__)


def test_adb::body_constructor_args():
    sig = inspect.signature(adb::Body.__init__)
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



def test_adb::entrydeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::EntryDeclaration)


def test_adb::entrydeclaration_constructor_exists():
    assert callable(adb::EntryDeclaration.__init__)


def test_adb::entrydeclaration_constructor_args():
    sig = inspect.signature(adb::EntryDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::entrydeclaration_has_name():
    assert hasattr(adb::EntryDeclaration, "name")
    descriptor = None
    for klass in adb::EntryDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::taskitem_is_not_abstract():
    assert not inspect.isabstract(adb::TaskItem)


def test_adb::taskitem_constructor_exists():
    assert callable(adb::TaskItem.__init__)


def test_adb::taskitem_constructor_args():
    sig = inspect.signature(adb::TaskItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::subtypeindication_is_not_abstract():
    assert not inspect.isabstract(adb::SubtypeIndication)


def test_adb::subtypeindication_constructor_exists():
    assert callable(adb::SubtypeIndication.__init__)


def test_adb::subtypeindication_constructor_args():
    sig = inspect.signature(adb::SubtypeIndication.__init__)
    params = list(sig.parameters.keys())
    assert "subtypeMark" in params, "Missing parameter 'subtypeMark'"

def test_adb::subtypeindication_has_subtypeMark():
    assert hasattr(adb::SubtypeIndication, "subtypeMark")
    descriptor = None
    for klass in adb::SubtypeIndication.__mro__:
        if "subtypeMark" in klass.__dict__:
            descriptor = klass.__dict__["subtypeMark"]
            break
    assert isinstance(descriptor, property)



def test_adb::privateextensiondeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::PrivateExtensionDeclaration)


def test_adb::privateextensiondeclaration_constructor_exists():
    assert callable(adb::PrivateExtensionDeclaration.__init__)


def test_adb::privateextensiondeclaration_constructor_args():
    sig = inspect.signature(adb::PrivateExtensionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "synchronized" in params, "Missing parameter 'synchronized'"
    assert "limited" in params, "Missing parameter 'limited'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_adb::privateextensiondeclaration_has_synchronized():
    assert hasattr(adb::PrivateExtensionDeclaration, "synchronized")
    descriptor = None
    for klass in adb::PrivateExtensionDeclaration.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)

def test_adb::privateextensiondeclaration_has_limited():
    assert hasattr(adb::PrivateExtensionDeclaration, "limited")
    descriptor = None
    for klass in adb::PrivateExtensionDeclaration.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb::privateextensiondeclaration_has_abstract():
    assert hasattr(adb::PrivateExtensionDeclaration, "abstract")
    descriptor = None
    for klass in adb::PrivateExtensionDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_adb::privatetypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::PrivateTypeDeclaration)


def test_adb::privatetypedeclaration_constructor_exists():
    assert callable(adb::PrivateTypeDeclaration.__init__)


def test_adb::privatetypedeclaration_constructor_args():
    sig = inspect.signature(adb::PrivateTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "limited" in params, "Missing parameter 'limited'"
    assert "tagged" in params, "Missing parameter 'tagged'"

def test_adb::privatetypedeclaration_has_abstract():
    assert hasattr(adb::PrivateTypeDeclaration, "abstract")
    descriptor = None
    for klass in adb::PrivateTypeDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb::privatetypedeclaration_has_limited():
    assert hasattr(adb::PrivateTypeDeclaration, "limited")
    descriptor = None
    for klass in adb::PrivateTypeDeclaration.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb::privatetypedeclaration_has_tagged():
    assert hasattr(adb::PrivateTypeDeclaration, "tagged")
    descriptor = None
    for klass in adb::PrivateTypeDeclaration.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)



def test_adb::discriminantpart_is_not_abstract():
    assert not inspect.isabstract(adb::DiscriminantPart)


def test_adb::discriminantpart_constructor_exists():
    assert callable(adb::DiscriminantPart.__init__)


def test_adb::discriminantpart_constructor_args():
    sig = inspect.signature(adb::DiscriminantPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::incompletetypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::IncompleteTypeDeclaration)


def test_adb::incompletetypedeclaration_constructor_exists():
    assert callable(adb::IncompleteTypeDeclaration.__init__)


def test_adb::incompletetypedeclaration_constructor_args():
    sig = inspect.signature(adb::IncompleteTypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "tagged" in params, "Missing parameter 'tagged'"

def test_adb::incompletetypedeclaration_has_tagged():
    assert hasattr(adb::IncompleteTypeDeclaration, "tagged")
    descriptor = None
    for klass in adb::IncompleteTypeDeclaration.__mro__:
        if "tagged" in klass.__dict__:
            descriptor = klass.__dict__["tagged"]
            break
    assert isinstance(descriptor, property)



def test_adb::typedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::TypeDefinition)


def test_adb::typedefinition_constructor_exists():
    assert callable(adb::TypeDefinition.__init__)


def test_adb::typedefinition_constructor_args():
    sig = inspect.signature(adb::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_fulltypedeclaration_is_not_abstract():
    assert not inspect.isabstract(FullTypeDeclaration)


def test_fulltypedeclaration_constructor_exists():
    assert callable(FullTypeDeclaration.__init__)


def test_fulltypedeclaration_constructor_args():
    sig = inspect.signature(FullTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedtypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedTypeDeclaration)


def test_adb::protectedtypedeclaration_constructor_exists():
    assert callable(adb::ProtectedTypeDeclaration.__init__)


def test_adb::protectedtypedeclaration_constructor_args():
    sig = inspect.signature(adb::ProtectedTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::fulldatatypedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::FullDataTypeDeclaration)


def test_adb::fulldatatypedeclaration_constructor_exists():
    assert callable(adb::FullDataTypeDeclaration.__init__)


def test_adb::fulldatatypedeclaration_constructor_args():
    sig = inspect.signature(adb::FullDataTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::packagespecification_is_not_abstract():
    assert not inspect.isabstract(adb::PackageSpecification)


def test_adb::packagespecification_constructor_exists():
    assert callable(adb::PackageSpecification.__init__)


def test_adb::packagespecification_constructor_args():
    sig = inspect.signature(adb::PackageSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "endname" in params, "Missing parameter 'endname'"

def test_adb::packagespecification_has_endname():
    assert hasattr(adb::PackageSpecification, "endname")
    descriptor = None
    for klass in adb::PackageSpecification.__mro__:
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



def test_adb::renaming_is_not_abstract():
    assert not inspect.isabstract(adb::Renaming)


def test_adb::renaming_constructor_exists():
    assert callable(adb::Renaming.__init__)


def test_adb::renaming_constructor_args():
    sig = inspect.signature(adb::Renaming.__init__)
    params = list(sig.parameters.keys())
    assert "renamed" in params, "Missing parameter 'renamed'"

def test_adb::renaming_has_renamed():
    assert hasattr(adb::Renaming, "renamed")
    descriptor = None
    for klass in adb::Renaming.__mro__:
        if "renamed" in klass.__dict__:
            descriptor = klass.__dict__["renamed"]
            break
    assert isinstance(descriptor, property)



def test_adb::packagedefinition_is_not_abstract():
    assert not inspect.isabstract(adb::PackageDefinition)


def test_adb::packagedefinition_constructor_exists():
    assert callable(adb::PackageDefinition.__init__)


def test_adb::packagedefinition_constructor_args():
    sig = inspect.signature(adb::PackageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_basicdeclaration_is_not_abstract():
    assert not inspect.isabstract(BasicDeclaration)


def test_basicdeclaration_constructor_exists():
    assert callable(BasicDeclaration.__init__)


def test_basicdeclaration_constructor_args():
    sig = inspect.signature(BasicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::numberdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::NumberDeclaration)


def test_adb::numberdeclaration_constructor_exists():
    assert callable(adb::NumberDeclaration.__init__)


def test_adb::numberdeclaration_constructor_args():
    sig = inspect.signature(adb::NumberDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::taskdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::TaskDeclaration)


def test_adb::taskdeclaration_constructor_exists():
    assert callable(adb::TaskDeclaration.__init__)


def test_adb::taskdeclaration_constructor_args():
    sig = inspect.signature(adb::TaskDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::taskdeclaration_has_name():
    assert hasattr(adb::TaskDeclaration, "name")
    descriptor = None
    for klass in adb::TaskDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::TypeDeclaration)


def test_adb::typedeclaration_constructor_exists():
    assert callable(adb::TypeDeclaration.__init__)


def test_adb::typedeclaration_constructor_args():
    sig = inspect.signature(adb::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::typedeclaration_has_name():
    assert hasattr(adb::TypeDeclaration, "name")
    descriptor = None
    for klass in adb::TypeDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::exceptiondeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ExceptionDeclaration)


def test_adb::exceptiondeclaration_constructor_exists():
    assert callable(adb::ExceptionDeclaration.__init__)


def test_adb::exceptiondeclaration_constructor_args():
    sig = inspect.signature(adb::ExceptionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::objectdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::ObjectDeclaration)


def test_adb::objectdeclaration_constructor_exists():
    assert callable(adb::ObjectDeclaration.__init__)


def test_adb::objectdeclaration_constructor_args():
    sig = inspect.signature(adb::ObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_libraryunitspecification_is_not_abstract():
    assert not inspect.isabstract(LibraryUnitSpecification)


def test_libraryunitspecification_constructor_exists():
    assert callable(LibraryUnitSpecification.__init__)


def test_libraryunitspecification_constructor_args():
    sig = inspect.signature(LibraryUnitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::PackageDeclaration)


def test_adb::packagedeclaration_constructor_exists():
    assert callable(adb::PackageDeclaration.__init__)


def test_adb::packagedeclaration_constructor_args():
    sig = inspect.signature(adb::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::packagedeclaration_has_name():
    assert hasattr(adb::PackageDeclaration, "name")
    descriptor = None
    for klass in adb::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::libraryunitspecification_is_not_abstract():
    assert not inspect.isabstract(adb::LibraryUnitSpecification)


def test_adb::libraryunitspecification_constructor_exists():
    assert callable(adb::LibraryUnitSpecification.__init__)


def test_adb::libraryunitspecification_constructor_args():
    sig = inspect.signature(adb::LibraryUnitSpecification.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_adb::separatesubunit_is_not_abstract():
    assert not inspect.isabstract(adb::SeparateSubunit)


def test_adb::separatesubunit_constructor_exists():
    assert callable(adb::SeparateSubunit.__init__)


def test_adb::separatesubunit_constructor_args():
    sig = inspect.signature(adb::SeparateSubunit.__init__)
    params = list(sig.parameters.keys())
    assert "parentUnitName" in params, "Missing parameter 'parentUnitName'"

def test_adb::separatesubunit_has_parentUnitName():
    assert hasattr(adb::SeparateSubunit, "parentUnitName")
    descriptor = None
    for klass in adb::SeparateSubunit.__mro__:
        if "parentUnitName" in klass.__dict__:
            descriptor = klass.__dict__["parentUnitName"]
            break
    assert isinstance(descriptor, property)



def test_adb::handledsequenceofstatements_is_not_abstract():
    assert not inspect.isabstract(adb::HandledSequenceOfStatements)


def test_adb::handledsequenceofstatements_constructor_exists():
    assert callable(adb::HandledSequenceOfStatements.__init__)


def test_adb::handledsequenceofstatements_constructor_args():
    sig = inspect.signature(adb::HandledSequenceOfStatements.__init__)
    params = list(sig.parameters.keys())



def test_adb::declarativeitem_is_not_abstract():
    assert not inspect.isabstract(adb::DeclarativeItem)


def test_adb::declarativeitem_constructor_exists():
    assert callable(adb::DeclarativeItem.__init__)


def test_adb::declarativeitem_constructor_args():
    sig = inspect.signature(adb::DeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::declarativeblock_is_not_abstract():
    assert not inspect.isabstract(adb::DeclarativeBlock)


def test_adb::declarativeblock_constructor_exists():
    assert callable(adb::DeclarativeBlock.__init__)


def test_adb::declarativeblock_constructor_args():
    sig = inspect.signature(adb::DeclarativeBlock.__init__)
    params = list(sig.parameters.keys())



def test_adb::subprogramspecification_is_not_abstract():
    assert not inspect.isabstract(adb::SubprogramSpecification)


def test_adb::subprogramspecification_constructor_exists():
    assert callable(adb::SubprogramSpecification.__init__)


def test_adb::subprogramspecification_constructor_args():
    sig = inspect.signature(adb::SubprogramSpecification.__init__)
    params = list(sig.parameters.keys())



def test_protectedoperationitem_is_not_abstract():
    assert not inspect.isabstract(ProtectedOperationItem)


def test_protectedoperationitem_constructor_exists():
    assert callable(ProtectedOperationItem.__init__)


def test_protectedoperationitem_constructor_args():
    sig = inspect.signature(ProtectedOperationItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::subprogramdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::SubprogramDeclaration)


def test_adb::subprogramdeclaration_constructor_exists():
    assert callable(adb::SubprogramDeclaration.__init__)


def test_adb::subprogramdeclaration_constructor_args():
    sig = inspect.signature(adb::SubprogramDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "null" in params, "Missing parameter 'null'"
    assert "renamedName" in params, "Missing parameter 'renamedName'"

def test_adb::subprogramdeclaration_has_abstract():
    assert hasattr(adb::SubprogramDeclaration, "abstract")
    descriptor = None
    for klass in adb::SubprogramDeclaration.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_adb::subprogramdeclaration_has_null():
    assert hasattr(adb::SubprogramDeclaration, "null")
    descriptor = None
    for klass in adb::SubprogramDeclaration.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)

def test_adb::subprogramdeclaration_has_renamedName():
    assert hasattr(adb::SubprogramDeclaration, "renamedName")
    descriptor = None
    for klass in adb::SubprogramDeclaration.__mro__:
        if "renamedName" in klass.__dict__:
            descriptor = klass.__dict__["renamedName"]
            break
    assert isinstance(descriptor, property)



def test_properbody_is_not_abstract():
    assert not inspect.isabstract(ProperBody)


def test_properbody_constructor_exists():
    assert callable(ProperBody.__init__)


def test_properbody_constructor_args():
    sig = inspect.signature(ProperBody.__init__)
    params = list(sig.parameters.keys())



def test_adb::protectedbody_is_not_abstract():
    assert not inspect.isabstract(adb::ProtectedBody)


def test_adb::protectedbody_constructor_exists():
    assert callable(adb::ProtectedBody.__init__)


def test_adb::protectedbody_constructor_args():
    sig = inspect.signature(adb::ProtectedBody.__init__)
    params = list(sig.parameters.keys())
    assert "idTask" in params, "Missing parameter 'idTask'"
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_adb::protectedbody_has_idTask():
    assert hasattr(adb::ProtectedBody, "idTask")
    descriptor = None
    for klass in adb::ProtectedBody.__mro__:
        if "idTask" in klass.__dict__:
            descriptor = klass.__dict__["idTask"]
            break
    assert isinstance(descriptor, property)

def test_adb::protectedbody_has_identifier():
    assert hasattr(adb::ProtectedBody, "identifier")
    descriptor = None
    for klass in adb::ProtectedBody.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_declarativeblock_is_not_abstract():
    assert not inspect.isabstract(DeclarativeBlock)


def test_declarativeblock_constructor_exists():
    assert callable(DeclarativeBlock.__init__)


def test_declarativeblock_constructor_args():
    sig = inspect.signature(DeclarativeBlock.__init__)
    params = list(sig.parameters.keys())



def test_adb::entrybody_is_not_abstract():
    assert not inspect.isabstract(adb::EntryBody)


def test_adb::entrybody_constructor_exists():
    assert callable(adb::EntryBody.__init__)


def test_adb::entrybody_constructor_args():
    sig = inspect.signature(adb::EntryBody.__init__)
    params = list(sig.parameters.keys())
    assert "endid" in params, "Missing parameter 'endid'"

def test_adb::entrybody_has_endid():
    assert hasattr(adb::EntryBody, "endid")
    descriptor = None
    for klass in adb::EntryBody.__mro__:
        if "endid" in klass.__dict__:
            descriptor = klass.__dict__["endid"]
            break
    assert isinstance(descriptor, property)



def test_adb::taskbody_is_not_abstract():
    assert not inspect.isabstract(adb::TaskBody)


def test_adb::taskbody_constructor_exists():
    assert callable(adb::TaskBody.__init__)


def test_adb::taskbody_constructor_args():
    sig = inspect.signature(adb::TaskBody.__init__)
    params = list(sig.parameters.keys())



def test_adb::blockstatement_is_not_abstract():
    assert not inspect.isabstract(adb::BlockStatement)


def test_adb::blockstatement_constructor_exists():
    assert callable(adb::BlockStatement.__init__)


def test_adb::blockstatement_constructor_args():
    sig = inspect.signature(adb::BlockStatement.__init__)
    params = list(sig.parameters.keys())
    assert "blockStatementIdentifier" in params, "Missing parameter 'blockStatementIdentifier'"

def test_adb::blockstatement_has_blockStatementIdentifier():
    assert hasattr(adb::BlockStatement, "blockStatementIdentifier")
    descriptor = None
    for klass in adb::BlockStatement.__mro__:
        if "blockStatementIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["blockStatementIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_adb::packagebody_is_not_abstract():
    assert not inspect.isabstract(adb::PackageBody)


def test_adb::packagebody_constructor_exists():
    assert callable(adb::PackageBody.__init__)


def test_adb::packagebody_constructor_args():
    sig = inspect.signature(adb::PackageBody.__init__)
    params = list(sig.parameters.keys())



def test_adb::subprogrambody_is_not_abstract():
    assert not inspect.isabstract(adb::SubprogramBody)


def test_adb::subprogrambody_constructor_exists():
    assert callable(adb::SubprogramBody.__init__)


def test_adb::subprogrambody_constructor_args():
    sig = inspect.signature(adb::SubprogramBody.__init__)
    params = list(sig.parameters.keys())
    assert "endname" in params, "Missing parameter 'endname'"

def test_adb::subprogrambody_has_endname():
    assert hasattr(adb::SubprogramBody, "endname")
    descriptor = None
    for klass in adb::SubprogramBody.__mro__:
        if "endname" in klass.__dict__:
            descriptor = klass.__dict__["endname"]
            break
    assert isinstance(descriptor, property)



def test_adb::basicdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(adb::BasicDeclarativeItem)


def test_adb::basicdeclarativeitem_constructor_exists():
    assert callable(adb::BasicDeclarativeItem.__init__)


def test_adb::basicdeclarativeitem_constructor_args():
    sig = inspect.signature(adb::BasicDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::genericactualpart_is_not_abstract():
    assert not inspect.isabstract(adb::GenericActualPart)


def test_adb::genericactualpart_constructor_exists():
    assert callable(adb::GenericActualPart.__init__)


def test_adb::genericactualpart_constructor_args():
    sig = inspect.signature(adb::GenericActualPart.__init__)
    params = list(sig.parameters.keys())



def test_adb::overridingindicator_is_not_abstract():
    assert not inspect.isabstract(adb::OverridingIndicator)


def test_adb::overridingindicator_constructor_exists():
    assert callable(adb::OverridingIndicator.__init__)


def test_adb::overridingindicator_constructor_args():
    sig = inspect.signature(adb::OverridingIndicator.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_adb::overridingindicator_has_not_():
    assert hasattr(adb::OverridingIndicator, "not_")
    descriptor = None
    for klass in adb::OverridingIndicator.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_adb::genericinstantiation_is_not_abstract():
    assert not inspect.isabstract(adb::GenericInstantiation)


def test_adb::genericinstantiation_constructor_exists():
    assert callable(adb::GenericInstantiation.__init__)


def test_adb::genericinstantiation_constructor_args():
    sig = inspect.signature(adb::GenericInstantiation.__init__)
    params = list(sig.parameters.keys())
    assert "genericName" in params, "Missing parameter 'genericName'"
    assert "name" in params, "Missing parameter 'name'"

def test_adb::genericinstantiation_has_genericName():
    assert hasattr(adb::GenericInstantiation, "genericName")
    descriptor = None
    for klass in adb::GenericInstantiation.__mro__:
        if "genericName" in klass.__dict__:
            descriptor = klass.__dict__["genericName"]
            break
    assert isinstance(descriptor, property)

def test_adb::genericinstantiation_has_name():
    assert hasattr(adb::GenericInstantiation, "name")
    descriptor = None
    for klass in adb::GenericInstantiation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::libraryspecification_is_not_abstract():
    assert not inspect.isabstract(adb::LibrarySpecification)


def test_adb::libraryspecification_constructor_exists():
    assert callable(adb::LibrarySpecification.__init__)


def test_adb::libraryspecification_constructor_args():
    sig = inspect.signature(adb::LibrarySpecification.__init__)
    params = list(sig.parameters.keys())



def test_adb::genericitems_is_not_abstract():
    assert not inspect.isabstract(adb::GenericItems)


def test_adb::genericitems_constructor_exists():
    assert callable(adb::GenericItems.__init__)


def test_adb::genericitems_constructor_args():
    sig = inspect.signature(adb::GenericItems.__init__)
    params = list(sig.parameters.keys())



def test_adb::genericdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::GenericDeclaration)


def test_adb::genericdeclaration_constructor_exists():
    assert callable(adb::GenericDeclaration.__init__)


def test_adb::genericdeclaration_constructor_args():
    sig = inspect.signature(adb::GenericDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_useclause_is_not_abstract():
    assert not inspect.isabstract(UseClause)


def test_useclause_constructor_exists():
    assert callable(UseClause.__init__)


def test_useclause_constructor_args():
    sig = inspect.signature(UseClause.__init__)
    params = list(sig.parameters.keys())



def test_adb::usetypeclause_is_not_abstract():
    assert not inspect.isabstract(adb::UseTypeClause)


def test_adb::usetypeclause_constructor_exists():
    assert callable(adb::UseTypeClause.__init__)


def test_adb::usetypeclause_constructor_args():
    sig = inspect.signature(adb::UseTypeClause.__init__)
    params = list(sig.parameters.keys())
    assert "typesNames" in params, "Missing parameter 'typesNames'"
    assert "useTypeRefs" in params, "Missing parameter 'useTypeRefs'"

def test_adb::usetypeclause_has_typesNames():
    assert hasattr(adb::UseTypeClause, "typesNames")
    descriptor = None
    for klass in adb::UseTypeClause.__mro__:
        if "typesNames" in klass.__dict__:
            descriptor = klass.__dict__["typesNames"]
            break
    assert isinstance(descriptor, property)

def test_adb::usetypeclause_has_useTypeRefs():
    assert hasattr(adb::UseTypeClause, "useTypeRefs")
    descriptor = None
    for klass in adb::UseTypeClause.__mro__:
        if "useTypeRefs" in klass.__dict__:
            descriptor = klass.__dict__["useTypeRefs"]
            break
    assert isinstance(descriptor, property)



def test_adb::usepackageclause_is_not_abstract():
    assert not inspect.isabstract(adb::UsePackageClause)


def test_adb::usepackageclause_constructor_exists():
    assert callable(adb::UsePackageClause.__init__)


def test_adb::usepackageclause_constructor_args():
    sig = inspect.signature(adb::UsePackageClause.__init__)
    params = list(sig.parameters.keys())



def test_genericitem_is_not_abstract():
    assert not inspect.isabstract(GenericItem)


def test_genericitem_constructor_exists():
    assert callable(GenericItem.__init__)


def test_genericitem_constructor_args():
    sig = inspect.signature(GenericItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::genericformalparameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::GenericFormalParameterDeclaration)


def test_adb::genericformalparameterdeclaration_constructor_exists():
    assert callable(adb::GenericFormalParameterDeclaration.__init__)


def test_adb::genericformalparameterdeclaration_constructor_args():
    sig = inspect.signature(adb::GenericFormalParameterDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_basicdeclarativeitem_is_not_abstract():
    assert not inspect.isabstract(BasicDeclarativeItem)


def test_basicdeclarativeitem_constructor_exists():
    assert callable(BasicDeclarativeItem.__init__)


def test_basicdeclarativeitem_constructor_args():
    sig = inspect.signature(BasicDeclarativeItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::aspectclause_is_not_abstract():
    assert not inspect.isabstract(adb::AspectClause)


def test_adb::aspectclause_constructor_exists():
    assert callable(adb::AspectClause.__init__)


def test_adb::aspectclause_constructor_args():
    sig = inspect.signature(adb::AspectClause.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::aspectclause_has_name():
    assert hasattr(adb::AspectClause, "name")
    descriptor = None
    for klass in adb::AspectClause.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::basicdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::BasicDeclaration)


def test_adb::basicdeclaration_constructor_exists():
    assert callable(adb::BasicDeclaration.__init__)


def test_adb::basicdeclaration_constructor_args():
    sig = inspect.signature(adb::BasicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_adb::libraryunitdeclaration_is_not_abstract():
    assert not inspect.isabstract(adb::LibraryUnitDeclaration)


def test_adb::libraryunitdeclaration_constructor_exists():
    assert callable(adb::LibraryUnitDeclaration.__init__)


def test_adb::libraryunitdeclaration_constructor_args():
    sig = inspect.signature(adb::LibraryUnitDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "private" in params, "Missing parameter 'private'"

def test_adb::libraryunitdeclaration_has_private():
    assert hasattr(adb::LibraryUnitDeclaration, "private")
    descriptor = None
    for klass in adb::LibraryUnitDeclaration.__mro__:
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



def test_adb::useclause_is_not_abstract():
    assert not inspect.isabstract(adb::UseClause)


def test_adb::useclause_constructor_exists():
    assert callable(adb::UseClause.__init__)


def test_adb::useclause_constructor_args():
    sig = inspect.signature(adb::UseClause.__init__)
    params = list(sig.parameters.keys())



def test_adb::withclause_is_not_abstract():
    assert not inspect.isabstract(adb::WithClause)


def test_adb::withclause_constructor_exists():
    assert callable(adb::WithClause.__init__)


def test_adb::withclause_constructor_args():
    sig = inspect.signature(adb::WithClause.__init__)
    params = list(sig.parameters.keys())
    assert "limited" in params, "Missing parameter 'limited'"
    assert "private" in params, "Missing parameter 'private'"

def test_adb::withclause_has_limited():
    assert hasattr(adb::WithClause, "limited")
    descriptor = None
    for klass in adb::WithClause.__mro__:
        if "limited" in klass.__dict__:
            descriptor = klass.__dict__["limited"]
            break
    assert isinstance(descriptor, property)

def test_adb::withclause_has_private():
    assert hasattr(adb::WithClause, "private")
    descriptor = None
    for klass in adb::WithClause.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)



def test_adb::contextitem_is_not_abstract():
    assert not inspect.isabstract(adb::ContextItem)


def test_adb::contextitem_constructor_exists():
    assert callable(adb::ContextItem.__init__)


def test_adb::contextitem_constructor_args():
    sig = inspect.signature(adb::ContextItem.__init__)
    params = list(sig.parameters.keys())



def test_adb::pragma_is_not_abstract():
    assert not inspect.isabstract(adb::Pragma)


def test_adb::pragma_constructor_exists():
    assert callable(adb::Pragma.__init__)


def test_adb::pragma_constructor_args():
    sig = inspect.signature(adb::Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_adb::pragma_has_name():
    assert hasattr(adb::Pragma, "name")
    descriptor = None
    for klass in adb::Pragma.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_adb::unit_is_not_abstract():
    assert not inspect.isabstract(adb::Unit)


def test_adb::unit_constructor_exists():
    assert callable(adb::Unit.__init__)


def test_adb::unit_constructor_args():
    sig = inspect.signature(adb::Unit.__init__)
    params = list(sig.parameters.keys())



def test_adb::contextclause_is_not_abstract():
    assert not inspect.isabstract(adb::ContextClause)


def test_adb::contextclause_constructor_exists():
    assert callable(adb::ContextClause.__init__)


def test_adb::contextclause_constructor_args():
    sig = inspect.signature(adb::ContextClause.__init__)
    params = list(sig.parameters.keys())



def test_adb::compilationunit_is_not_abstract():
    assert not inspect.isabstract(adb::CompilationUnit)


def test_adb::compilationunit_constructor_exists():
    assert callable(adb::CompilationUnit.__init__)


def test_adb::compilationunit_constructor_args():
    sig = inspect.signature(adb::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_adb::compilation_is_not_abstract():
    assert not inspect.isabstract(adb::Compilation)


def test_adb::compilation_constructor_exists():
    assert callable(adb::Compilation.__init__)


def test_adb::compilation_constructor_args():
    sig = inspect.signature(adb::Compilation.__init__)
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
DiscreteChoice_strategy = st.builds(
    DiscreteChoice,
)
ExplicitGenericActualParameter_strategy = st.builds(
    ExplicitGenericActualParameter,
)
EntryIndex_strategy = st.builds(
    EntryIndex,
)
adb::Primary_strategy = st.builds(
    adb::Primary,
)
adb::RealRangeSpecification_strategy = st.builds(
    adb::RealRangeSpecification,
)
adb::DiscreteChoice_strategy = st.builds(
    adb::DiscreteChoice,
)
adb::Variant_strategy = st.builds(
    adb::Variant,
)
adb::ComponentClause_strategy = st.builds(
    adb::ComponentClause,
    localName=
        safe_text
)
adb::ModClause_strategy = st.builds(
    adb::ModClause,
)
RealTypeDefinition_strategy = st.builds(
    RealTypeDefinition,
)
adb::FixedPointDefinition_strategy = st.builds(
    adb::FixedPointDefinition,
)
adb::FloatingPointDefinition_strategy = st.builds(
    adb::FloatingPointDefinition,
)
ComponentItem_strategy = st.builds(
    ComponentItem,
)
adb::VariantPart_strategy = st.builds(
    adb::VariantPart,
    name=
        safe_text
)
adb::OptVariantPart_strategy = st.builds(
    adb::OptVariantPart,
)
adb::ComponentItem_strategy = st.builds(
    adb::ComponentItem,
)
adb::ComponentList_strategy = st.builds(
    adb::ComponentList,
)
adb::SimpleExpression_strategy = st.builds(
    adb::SimpleExpression,
    unaryAddingOperator=
        safe_text,
    binaryAddingOperators=
        safe_text
)
IntegerTypeDefinition_strategy = st.builds(
    IntegerTypeDefinition,
)
adb::ModularTypeDefinition_strategy = st.builds(
    adb::ModularTypeDefinition,
)
adb::SignedIntegerTypeDefinition_strategy = st.builds(
    adb::SignedIntegerTypeDefinition,
)
adb::ParameterSpecification_strategy = st.builds(
    adb::ParameterSpecification,
)
ReturnSubtypeIndication_strategy = st.builds(
    ReturnSubtypeIndication,
)
ArrayIndexes_strategy = st.builds(
    ArrayIndexes,
)
adb::ConstrainedIndexes_strategy = st.builds(
    adb::ConstrainedIndexes,
)
adb::UnconstrainedIndexes_strategy = st.builds(
    adb::UnconstrainedIndexes,
)
adb::ComponentDefinition_strategy = st.builds(
    adb::ComponentDefinition,
    aliased=
        st.booleans()
)
adb::ArrayIndexes_strategy = st.builds(
    adb::ArrayIndexes,
)
NotNullAccessDefinition_strategy = st.builds(
    NotNullAccessDefinition,
)
AccessSpecification_strategy = st.builds(
    AccessSpecification,
)
adb::AccessToDataDefinition_strategy = st.builds(
    adb::AccessToDataDefinition,
    generalAccessModifier=
        safe_text
)
adb::AccessToSubprogramDefinition_strategy = st.builds(
    adb::AccessToSubprogramDefinition,
    protected=
        st.booleans()
)
adb::AccessSpecification_strategy = st.builds(
    adb::AccessSpecification,
)
adb::AccessToDataInstance_strategy = st.builds(
    adb::AccessToDataInstance,
    constant=
        safe_text
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
adb::IntegerTypeDefinition_strategy = st.builds(
    adb::IntegerTypeDefinition,
)
adb::EnumerationTypeDefinition_strategy = st.builds(
    adb::EnumerationTypeDefinition,
    enumerationliteralspecifications=
        safe_text
)
adb::DerivedTypeDefinition_strategy = st.builds(
    adb::DerivedTypeDefinition,
    limited=
        safe_text,
    abstract=
        safe_text
)
adb::RecordTypeDefinition_strategy = st.builds(
    adb::RecordTypeDefinition,
    tagged=
        st.booleans(),
    abstract=
        st.booleans(),
    limited=
        st.booleans()
)
adb::RealTypeDefinition_strategy = st.builds(
    adb::RealTypeDefinition,
)
adb::NotNullAccessDefinition_strategy = st.builds(
    adb::NotNullAccessDefinition,
)
adb::DiscriminantSpecification_strategy = st.builds(
    adb::DiscriminantSpecification,
)
adb::RecordDefinition_strategy = st.builds(
    adb::RecordDefinition,
    null=
        safe_text
)
adb::RecordExtensionPart_strategy = st.builds(
    adb::RecordExtensionPart,
)
DiscriminantPart_strategy = st.builds(
    DiscriminantPart,
)
adb::UnknownDiscriminantPart_strategy = st.builds(
    adb::UnknownDiscriminantPart,
    box=
        st.booleans()
)
adb::ExplicitGenericActualParameter_strategy = st.builds(
    adb::ExplicitGenericActualParameter,
)
AbortStatement_strategy = st.builds(
    AbortStatement,
)
adb::TaskNames_strategy = st.builds(
    adb::TaskNames,
)
adb::EntryCallAlternative_strategy = st.builds(
    adb::EntryCallAlternative,
)
SelectAlternative_strategy = st.builds(
    SelectAlternative,
)
adb::DelayAlternative_strategy = st.builds(
    adb::DelayAlternative,
)
adb::AcceptAlternative_strategy = st.builds(
    adb::AcceptAlternative,
)
adb::GuardedAlternative_strategy = st.builds(
    adb::GuardedAlternative,
)
adb::SelectAlternative_strategy = st.builds(
    adb::SelectAlternative,
)
adb::Guard_strategy = st.builds(
    adb::Guard,
)
SelectStatement_strategy = st.builds(
    SelectStatement,
)
adb::ConditionalEntryCall_strategy = st.builds(
    adb::ConditionalEntryCall,
)
adb::TimedEntryCall_strategy = st.builds(
    adb::TimedEntryCall,
)
adb::SelectiveAccept_strategy = st.builds(
    adb::SelectiveAccept,
)
adb::TriggeringStatement_strategy = st.builds(
    adb::TriggeringStatement,
)
adb::AbortablePart_strategy = st.builds(
    adb::AbortablePart,
)
adb::TriggeringAlternative_strategy = st.builds(
    adb::TriggeringAlternative,
)
adb::AsynchronousSelect_strategy = st.builds(
    adb::AsynchronousSelect,
)
adb::EntryIndexSpecification_strategy = st.builds(
    adb::EntryIndexSpecification,
    name=
        safe_text
)
adb::EntryBarrier_strategy = st.builds(
    adb::EntryBarrier,
)
adb::EntryBodyFormalPart_strategy = st.builds(
    adb::EntryBodyFormalPart,
)
adb::EntryIndex_strategy = st.builds(
    adb::EntryIndex,
)
adb::ProtectedOperationItem_strategy = st.builds(
    adb::ProtectedOperationItem,
)
adb::ReturnSubtypeIndication_strategy = st.builds(
    adb::ReturnSubtypeIndication,
)
TriggeringStatement_strategy = st.builds(
    TriggeringStatement,
)
adb::LoopParameterSpecification_strategy = st.builds(
    adb::LoopParameterSpecification,
    identifier=
        safe_text
)
adb::IterationScheme_strategy = st.builds(
    adb::IterationScheme,
)
CompoundStatement_strategy = st.builds(
    CompoundStatement,
)
adb::ExtendedReturnStatement_strategy = st.builds(
    adb::ExtendedReturnStatement,
    identifier=
        safe_text
)
adb::SelectStatement_strategy = st.builds(
    adb::SelectStatement,
)
adb::AcceptStatement_strategy = st.builds(
    adb::AcceptStatement,
    entryidentifier=
        safe_text
)
adb::LoopStatement_strategy = st.builds(
    adb::LoopStatement,
    sameName=
        safe_text,
    name=
        safe_text
)
adb::IfStatement_strategy = st.builds(
    adb::IfStatement,
)
adb::PragmaArgumentAssociation_strategy = st.builds(
    adb::PragmaArgumentAssociation,
    name=
        safe_text
)
adb::DiscreteChoiceList_strategy = st.builds(
    adb::DiscreteChoiceList,
)
adb::CaseStatementAlternative_strategy = st.builds(
    adb::CaseStatementAlternative,
)
adb::CaseStatement_strategy = st.builds(
    adb::CaseStatement,
)
ObjectDeclaration_strategy = st.builds(
    ObjectDeclaration,
)
adb::DataInstanceDeclaration_strategy = st.builds(
    adb::DataInstanceDeclaration,
    aliased=
        st.booleans(),
    constant=
        st.booleans()
)
adb::GenericAssociation_strategy = st.builds(
    adb::GenericAssociation,
    selectorName=
        safe_text
)
adb::FormalPackageAssociation_strategy = st.builds(
    adb::FormalPackageAssociation,
    genericFormalParameterSelectorName=
        safe_text
)
adb::FormalPackageActualPart_strategy = st.builds(
    adb::FormalPackageActualPart,
    box=
        st.booleans()
)
adb::SubprogramDefault_strategy = st.builds(
    adb::SubprogramDefault,
    defaultName=
        safe_text
)
adb::AnonymousAccessDefinition_strategy = st.builds(
    adb::AnonymousAccessDefinition,
)
adb::OptNullExclusion_strategy = st.builds(
    adb::OptNullExclusion,
    not_null=
        safe_text
)
adb::SingleProtectedDeclaration_strategy = st.builds(
    adb::SingleProtectedDeclaration,
    name=
        safe_text
)
adb::Mode_strategy = st.builds(
    adb::Mode,
    out=
        st.booleans(),
    in_=
        st.booleans()
)
adb::DefiningIdentifierList_strategy = st.builds(
    adb::DefiningIdentifierList,
    name=
        safe_text
)
FormalTypeDefinition_strategy = st.builds(
    FormalTypeDefinition,
)
adb::FormalDerivedTypeDefinition_strategy = st.builds(
    adb::FormalDerivedTypeDefinition,
    absract=
        safe_text,
    synchronized=
        st.booleans(),
    limited=
        st.booleans()
)
adb::AccessTypeDefinition_strategy = st.builds(
    adb::AccessTypeDefinition,
)
adb::InterfaceTypeDefinition_strategy = st.builds(
    adb::InterfaceTypeDefinition,
    synchro=
        st.booleans(),
    limited=
        st.booleans(),
    task=
        st.booleans(),
    protected=
        st.booleans()
)
adb::ArrayTypeDefinition_strategy = st.builds(
    adb::ArrayTypeDefinition,
)
GenericFormalParameterDeclaration_strategy = st.builds(
    GenericFormalParameterDeclaration,
)
adb::FormalSubprogramDeclaration_strategy = st.builds(
    adb::FormalSubprogramDeclaration,
    abstract=
        safe_text
)
adb::FormalPackageDeclaration_strategy = st.builds(
    adb::FormalPackageDeclaration,
    name=
        safe_text,
    genericPackageName=
        safe_text
)
adb::FormalTypeDeclaration_strategy = st.builds(
    adb::FormalTypeDeclaration,
    identifier=
        safe_text
)
adb::FormalObjectDeclaration_strategy = st.builds(
    adb::FormalObjectDeclaration,
)
adb::FormalPrivateTypeDefinition_strategy = st.builds(
    adb::FormalPrivateTypeDefinition,
    tagged=
        st.booleans(),
    abstract=
        st.booleans(),
    limited=
        st.booleans()
)
adb::FormalTypeDefinition_strategy = st.builds(
    adb::FormalTypeDefinition,
)
Range_strategy = st.builds(
    Range,
)
adb::ExplicitRange_strategy = st.builds(
    adb::ExplicitRange,
)
adb::EntityRange_strategy = st.builds(
    adb::EntityRange,
)
RangeConstraint_strategy = st.builds(
    RangeConstraint,
)
adb::ParameterEffectiveValue_strategy = st.builds(
    adb::ParameterEffectiveValue,
)
adb::AttributeDesignator_strategy = st.builds(
    adb::AttributeDesignator,
)
adb::PrimaryName_strategy = st.builds(
    adb::PrimaryName,
)
Interval_strategy = st.builds(
    Interval,
)
adb::ArrayComponentAssociation_strategy = st.builds(
    adb::ArrayComponentAssociation,
    box=
        st.booleans()
)
ArrayAggregate_strategy = st.builds(
    ArrayAggregate,
)
adb::NamedArrayAggregate_strategy = st.builds(
    adb::NamedArrayAggregate,
)
adb::PositionalArrayAggregate_strategy = st.builds(
    adb::PositionalArrayAggregate,
    othersBox=
        st.booleans()
)
adb::AncestorPart_strategy = st.builds(
    adb::AncestorPart,
)
RecordComponentAssociation_strategy = st.builds(
    RecordComponentAssociation,
)
adb::UninitializedComponents_strategy = st.builds(
    adb::UninitializedComponents,
    box=
        st.booleans()
)
adb::InitializedComponents_strategy = st.builds(
    adb::InitializedComponents,
)
adb::ParameterAssociation_strategy = st.builds(
    adb::ParameterAssociation,
    selectorName=
        safe_text
)
adb::RecordComponentAssociation_strategy = st.builds(
    adb::RecordComponentAssociation,
)
RecordAggregate_strategy = st.builds(
    RecordAggregate,
)
adb::RecordComponentAssociationList_strategy = st.builds(
    adb::RecordComponentAssociationList,
    nullRecord=
        st.booleans()
)
Aggregate_strategy = st.builds(
    Aggregate,
)
adb::ArrayAggregate_strategy = st.builds(
    adb::ArrayAggregate,
)
adb::ExtensionAggregate_strategy = st.builds(
    adb::ExtensionAggregate,
)
adb::RecordAggregate_strategy = st.builds(
    adb::RecordAggregate,
)
Qualifier_strategy = st.builds(
    Qualifier,
)
ParenthesizedExpression_strategy = st.builds(
    ParenthesizedExpression,
)
adb::Aggregate_strategy = st.builds(
    adb::Aggregate,
)
adb::ComponentChoiceList_strategy = st.builds(
    adb::ComponentChoiceList,
    componentSelectorName=
        safe_text,
    others=
        st.booleans()
)
adb::DiscriminantSelectors_strategy = st.builds(
    adb::DiscriminantSelectors,
    discriminantSelectorName=
        safe_text
)
adb::DiscriminantAssociation_strategy = st.builds(
    adb::DiscriminantAssociation,
)
CompositeConstraint_strategy = st.builds(
    CompositeConstraint,
)
adb::IndexConstraint_strategy = st.builds(
    adb::IndexConstraint,
)
adb::DiscriminantConstraint_strategy = st.builds(
    adb::DiscriminantConstraint,
)
adb::CompositeConstraint_strategy = st.builds(
    adb::CompositeConstraint,
)
adb::OptConstraint_strategy = st.builds(
    adb::OptConstraint,
)
DiscreteRange_strategy = st.builds(
    DiscreteRange,
)
DiscreteSubtypeDefinition_strategy = st.builds(
    DiscreteSubtypeDefinition,
)
adb::DiscreteRange_strategy = st.builds(
    adb::DiscreteRange,
)
adb::Qualifier_strategy = st.builds(
    adb::Qualifier,
)
Primary_strategy = st.builds(
    Primary,
)
adb::Allocator_strategy = st.builds(
    adb::Allocator,
)
adb::Null_strategy = st.builds(
    adb::Null,
    value=
        safe_text
)
adb::QualifiedName_strategy = st.builds(
    adb::QualifiedName,
)
adb::StringLiteral_strategy = st.builds(
    adb::StringLiteral,
    value=
        safe_text
)
adb::ParenthesizedExpression_strategy = st.builds(
    adb::ParenthesizedExpression,
)
adb::NumericLiteral_strategy = st.builds(
    adb::NumericLiteral,
    value=
        safe_text
)
ScalarConstraint_strategy = st.builds(
    ScalarConstraint,
)
adb::DeltaConstraint_strategy = st.builds(
    adb::DeltaConstraint,
)
adb::RangeConstraint_strategy = st.builds(
    adb::RangeConstraint,
)
adb::DigitsConstraint_strategy = st.builds(
    adb::DigitsConstraint,
)
adb::ScalarConstraint_strategy = st.builds(
    adb::ScalarConstraint,
)
adb::EObject_strategy = st.builds(
    adb::EObject,
)
adb::Factor_strategy = st.builds(
    adb::Factor,
    abs=
        st.booleans(),
    not_=
        st.booleans()
)
adb::Term_strategy = st.builds(
    adb::Term,
    multiplyingOperators=
        safe_text
)
adb::Interval_strategy = st.builds(
    adb::Interval,
)
adb::Membership_strategy = st.builds(
    adb::Membership,
    not_=
        st.booleans()
)
adb::Relation_strategy = st.builds(
    adb::Relation,
    relationalOperator=
        safe_text
)
ParameterEffectiveValue_strategy = st.builds(
    ParameterEffectiveValue,
)
adb::Range_strategy = st.builds(
    adb::Range,
)
AncestorPart_strategy = st.builds(
    AncestorPart,
)
adb::Expression_strategy = st.builds(
    adb::Expression,
    booleanOperator=
        safe_text
)
adb::ExceptionHandler_strategy = st.builds(
    adb::ExceptionHandler,
    name=
        safe_text
)
adb::GenericItem_strategy = st.builds(
    adb::GenericItem,
)
SimpleStatement_strategy = st.builds(
    SimpleStatement,
)
adb::AbortStatement_strategy = st.builds(
    adb::AbortStatement,
)
adb::SimpleReturnStatement_strategy = st.builds(
    adb::SimpleReturnStatement,
)
adb::GotoStatement_strategy = st.builds(
    adb::GotoStatement,
    labelId=
        safe_text
)
adb::ProcedureOrEntryCallStatement_strategy = st.builds(
    adb::ProcedureOrEntryCallStatement,
)
adb::DelayStatement_strategy = st.builds(
    adb::DelayStatement,
    until=
        safe_text
)
adb::RaiseStatement_strategy = st.builds(
    adb::RaiseStatement,
)
adb::AssignmentStatement_strategy = st.builds(
    adb::AssignmentStatement,
)
adb::RequeueStatement_strategy = st.builds(
    adb::RequeueStatement,
    abort=
        st.booleans()
)
adb::ExitStatement_strategy = st.builds(
    adb::ExitStatement,
)
adb::NullStatement_strategy = st.builds(
    adb::NullStatement,
    null=
        st.booleans()
)
Statement_strategy = st.builds(
    Statement,
)
adb::CompoundStatement_strategy = st.builds(
    adb::CompoundStatement,
)
adb::SimpleStatement_strategy = st.builds(
    adb::SimpleStatement,
)
adb::Statement_strategy = st.builds(
    adb::Statement,
)
adb::LabelisableStatement_strategy = st.builds(
    adb::LabelisableStatement,
)
AbortablePart_strategy = st.builds(
    AbortablePart,
)
HandledSequenceOfStatements_strategy = st.builds(
    HandledSequenceOfStatements,
)
adb::SequenceOfStatements_strategy = st.builds(
    adb::SequenceOfStatements,
)
adb::Label_strategy = st.builds(
    adb::Label,
    identifier=
        safe_text
)
Body_strategy = st.builds(
    Body,
)
adb::BodyStub_strategy = st.builds(
    adb::BodyStub,
    name=
        safe_text
)
adb::ProperBody_strategy = st.builds(
    adb::ProperBody,
)
ProtectedElementDeclaration_strategy = st.builds(
    ProtectedElementDeclaration,
)
adb::ComponentDeclaration_strategy = st.builds(
    adb::ComponentDeclaration,
)
adb::ProtectedOperationDeclaration_strategy = st.builds(
    adb::ProtectedOperationDeclaration,
)
adb::ProtectedElementDeclaration_strategy = st.builds(
    adb::ProtectedElementDeclaration,
)
adb::ProtectedDefinition_strategy = st.builds(
    adb::ProtectedDefinition,
)
adb::FormalPart_strategy = st.builds(
    adb::FormalPart,
)
adb::DiscreteSubtypeDefinition_strategy = st.builds(
    adb::DiscreteSubtypeDefinition,
)
adb::Name_strategy = st.builds(
    adb::Name,
    name=
        safe_text
)
adb::ExceptionChoice_strategy = st.builds(
    adb::ExceptionChoice,
    others=
        st.booleans()
)
adb::ParameterAndResultProfile_strategy = st.builds(
    adb::ParameterAndResultProfile,
)
SubprogramSpecification_strategy = st.builds(
    SubprogramSpecification,
)
adb::FunctionSpecification_strategy = st.builds(
    adb::FunctionSpecification,
)
adb::ProcedureSpecification_strategy = st.builds(
    adb::ProcedureSpecification,
)
BodyStub_strategy = st.builds(
    BodyStub,
)
adb::ProtectedBodyStub_strategy = st.builds(
    adb::ProtectedBodyStub,
)
adb::PackageBodyStub_strategy = st.builds(
    adb::PackageBodyStub,
)
adb::TaskBodyStub_strategy = st.builds(
    adb::TaskBodyStub,
)
NewTypeDeclaration_strategy = st.builds(
    NewTypeDeclaration,
)
adb::FullTypeDeclaration_strategy = st.builds(
    adb::FullTypeDeclaration,
)
TypeDeclaration_strategy = st.builds(
    TypeDeclaration,
)
adb::SubtypeDeclaration_strategy = st.builds(
    adb::SubtypeDeclaration,
)
adb::NewTypeDeclaration_strategy = st.builds(
    adb::NewTypeDeclaration,
)
adb::TaskDefinition_strategy = st.builds(
    adb::TaskDefinition,
)
adb::InterfaceList_strategy = st.builds(
    adb::InterfaceList,
)
adb::KnownDiscriminantPart_strategy = st.builds(
    adb::KnownDiscriminantPart,
)
DeclarativeItem_strategy = st.builds(
    DeclarativeItem,
)
adb::Body_strategy = st.builds(
    adb::Body,
)
ProtectedOperationDeclaration_strategy = st.builds(
    ProtectedOperationDeclaration,
)
TaskItem_strategy = st.builds(
    TaskItem,
)
adb::EntryDeclaration_strategy = st.builds(
    adb::EntryDeclaration,
    name=
        safe_text
)
adb::TaskItem_strategy = st.builds(
    adb::TaskItem,
)
adb::SubtypeIndication_strategy = st.builds(
    adb::SubtypeIndication,
    subtypeMark=
        safe_text
)
adb::PrivateExtensionDeclaration_strategy = st.builds(
    adb::PrivateExtensionDeclaration,
    synchronized=
        st.booleans(),
    limited=
        st.booleans(),
    abstract=
        st.booleans()
)
adb::PrivateTypeDeclaration_strategy = st.builds(
    adb::PrivateTypeDeclaration,
    abstract=
        st.booleans(),
    limited=
        st.booleans(),
    tagged=
        st.booleans()
)
adb::DiscriminantPart_strategy = st.builds(
    adb::DiscriminantPart,
)
adb::IncompleteTypeDeclaration_strategy = st.builds(
    adb::IncompleteTypeDeclaration,
    tagged=
        st.booleans()
)
adb::TypeDefinition_strategy = st.builds(
    adb::TypeDefinition,
)
FullTypeDeclaration_strategy = st.builds(
    FullTypeDeclaration,
)
adb::ProtectedTypeDeclaration_strategy = st.builds(
    adb::ProtectedTypeDeclaration,
)
adb::FullDataTypeDeclaration_strategy = st.builds(
    adb::FullDataTypeDeclaration,
)
adb::PackageSpecification_strategy = st.builds(
    adb::PackageSpecification,
    endname=
        safe_text
)
LibrarySpecification_strategy = st.builds(
    LibrarySpecification,
)
PackageDeclaration_strategy = st.builds(
    PackageDeclaration,
)
adb::Renaming_strategy = st.builds(
    adb::Renaming,
    renamed=
        safe_text
)
adb::PackageDefinition_strategy = st.builds(
    adb::PackageDefinition,
)
BasicDeclaration_strategy = st.builds(
    BasicDeclaration,
)
adb::NumberDeclaration_strategy = st.builds(
    adb::NumberDeclaration,
)
adb::TaskDeclaration_strategy = st.builds(
    adb::TaskDeclaration,
    name=
        safe_text
)
adb::TypeDeclaration_strategy = st.builds(
    adb::TypeDeclaration,
    name=
        safe_text
)
adb::ExceptionDeclaration_strategy = st.builds(
    adb::ExceptionDeclaration,
)
adb::ObjectDeclaration_strategy = st.builds(
    adb::ObjectDeclaration,
)
LibraryUnitSpecification_strategy = st.builds(
    LibraryUnitSpecification,
)
adb::PackageDeclaration_strategy = st.builds(
    adb::PackageDeclaration,
    name=
        safe_text
)
adb::LibraryUnitSpecification_strategy = st.builds(
    adb::LibraryUnitSpecification,
)
Unit_strategy = st.builds(
    Unit,
)
adb::SeparateSubunit_strategy = st.builds(
    adb::SeparateSubunit,
    parentUnitName=
        safe_text
)
adb::HandledSequenceOfStatements_strategy = st.builds(
    adb::HandledSequenceOfStatements,
)
adb::DeclarativeItem_strategy = st.builds(
    adb::DeclarativeItem,
)
adb::DeclarativeBlock_strategy = st.builds(
    adb::DeclarativeBlock,
)
adb::SubprogramSpecification_strategy = st.builds(
    adb::SubprogramSpecification,
)
ProtectedOperationItem_strategy = st.builds(
    ProtectedOperationItem,
)
adb::SubprogramDeclaration_strategy = st.builds(
    adb::SubprogramDeclaration,
    abstract=
        st.booleans(),
    null=
        st.booleans(),
    renamedName=
        safe_text
)
ProperBody_strategy = st.builds(
    ProperBody,
)
adb::ProtectedBody_strategy = st.builds(
    adb::ProtectedBody,
    idTask=
        safe_text,
    identifier=
        safe_text
)
DeclarativeBlock_strategy = st.builds(
    DeclarativeBlock,
)
adb::EntryBody_strategy = st.builds(
    adb::EntryBody,
    endid=
        safe_text
)
adb::TaskBody_strategy = st.builds(
    adb::TaskBody,
)
adb::BlockStatement_strategy = st.builds(
    adb::BlockStatement,
    blockStatementIdentifier=
        safe_text
)
adb::PackageBody_strategy = st.builds(
    adb::PackageBody,
)
adb::SubprogramBody_strategy = st.builds(
    adb::SubprogramBody,
    endname=
        safe_text
)
adb::BasicDeclarativeItem_strategy = st.builds(
    adb::BasicDeclarativeItem,
)
adb::GenericActualPart_strategy = st.builds(
    adb::GenericActualPart,
)
adb::OverridingIndicator_strategy = st.builds(
    adb::OverridingIndicator,
    not_=
        st.booleans()
)
adb::GenericInstantiation_strategy = st.builds(
    adb::GenericInstantiation,
    genericName=
        safe_text,
    name=
        safe_text
)
adb::LibrarySpecification_strategy = st.builds(
    adb::LibrarySpecification,
)
adb::GenericItems_strategy = st.builds(
    adb::GenericItems,
)
adb::GenericDeclaration_strategy = st.builds(
    adb::GenericDeclaration,
)
UseClause_strategy = st.builds(
    UseClause,
)
adb::UseTypeClause_strategy = st.builds(
    adb::UseTypeClause,
    typesNames=
        safe_text,
    useTypeRefs=
        safe_text
)
adb::UsePackageClause_strategy = st.builds(
    adb::UsePackageClause,
)
GenericItem_strategy = st.builds(
    GenericItem,
)
adb::GenericFormalParameterDeclaration_strategy = st.builds(
    adb::GenericFormalParameterDeclaration,
)
BasicDeclarativeItem_strategy = st.builds(
    BasicDeclarativeItem,
)
adb::AspectClause_strategy = st.builds(
    adb::AspectClause,
    name=
        safe_text
)
adb::BasicDeclaration_strategy = st.builds(
    adb::BasicDeclaration,
)
adb::LibraryUnitDeclaration_strategy = st.builds(
    adb::LibraryUnitDeclaration,
    private=
        st.booleans()
)
ContextItem_strategy = st.builds(
    ContextItem,
)
adb::UseClause_strategy = st.builds(
    adb::UseClause,
)
adb::WithClause_strategy = st.builds(
    adb::WithClause,
    limited=
        st.booleans(),
    private=
        st.booleans()
)
adb::ContextItem_strategy = st.builds(
    adb::ContextItem,
)
adb::Pragma_strategy = st.builds(
    adb::Pragma,
    name=
        safe_text
)
adb::Unit_strategy = st.builds(
    adb::Unit,
)
adb::ContextClause_strategy = st.builds(
    adb::ContextClause,
)
adb::CompilationUnit_strategy = st.builds(
    adb::CompilationUnit,
)
adb::Compilation_strategy = st.builds(
    adb::Compilation,
)

@given(instance=DiscreteChoice_strategy)
@settings(max_examples=50)
def test_discretechoice_instantiation(instance):
    assert isinstance(instance, DiscreteChoice)

@given(instance=ExplicitGenericActualParameter_strategy)
@settings(max_examples=50)
def test_explicitgenericactualparameter_instantiation(instance):
    assert isinstance(instance, ExplicitGenericActualParameter)

@given(instance=EntryIndex_strategy)
@settings(max_examples=50)
def test_entryindex_instantiation(instance):
    assert isinstance(instance, EntryIndex)

@given(instance=adb::Primary_strategy)
@settings(max_examples=50)
def test_adb::primary_instantiation(instance):
    assert isinstance(instance, adb::Primary)

@given(instance=adb::RealRangeSpecification_strategy)
@settings(max_examples=50)
def test_adb::realrangespecification_instantiation(instance):
    assert isinstance(instance, adb::RealRangeSpecification)

@given(instance=adb::DiscreteChoice_strategy)
@settings(max_examples=50)
def test_adb::discretechoice_instantiation(instance):
    assert isinstance(instance, adb::DiscreteChoice)

@given(instance=adb::Variant_strategy)
@settings(max_examples=50)
def test_adb::variant_instantiation(instance):
    assert isinstance(instance, adb::Variant)

@given(instance=adb::ComponentClause_strategy)
@settings(max_examples=50)
def test_adb::componentclause_instantiation(instance):
    assert isinstance(instance, adb::ComponentClause)

@given(instance=adb::ComponentClause_strategy)
def test_adb::componentclause_localName_type(instance):
    assert isinstance(instance.localName, str)


@given(instance=adb::ComponentClause_strategy)
def test_adb::componentclause_localName_setter(instance):
    original = instance.localName
    instance.localName = original
    assert instance.localName == original

@given(instance=adb::ModClause_strategy)
@settings(max_examples=50)
def test_adb::modclause_instantiation(instance):
    assert isinstance(instance, adb::ModClause)

@given(instance=RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_realtypedefinition_instantiation(instance):
    assert isinstance(instance, RealTypeDefinition)

@given(instance=adb::FixedPointDefinition_strategy)
@settings(max_examples=50)
def test_adb::fixedpointdefinition_instantiation(instance):
    assert isinstance(instance, adb::FixedPointDefinition)

@given(instance=adb::FloatingPointDefinition_strategy)
@settings(max_examples=50)
def test_adb::floatingpointdefinition_instantiation(instance):
    assert isinstance(instance, adb::FloatingPointDefinition)

@given(instance=ComponentItem_strategy)
@settings(max_examples=50)
def test_componentitem_instantiation(instance):
    assert isinstance(instance, ComponentItem)

@given(instance=adb::VariantPart_strategy)
@settings(max_examples=50)
def test_adb::variantpart_instantiation(instance):
    assert isinstance(instance, adb::VariantPart)

@given(instance=adb::VariantPart_strategy)
def test_adb::variantpart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::VariantPart_strategy)
def test_adb::variantpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::OptVariantPart_strategy)
@settings(max_examples=50)
def test_adb::optvariantpart_instantiation(instance):
    assert isinstance(instance, adb::OptVariantPart)

@given(instance=adb::ComponentItem_strategy)
@settings(max_examples=50)
def test_adb::componentitem_instantiation(instance):
    assert isinstance(instance, adb::ComponentItem)

@given(instance=adb::ComponentList_strategy)
@settings(max_examples=50)
def test_adb::componentlist_instantiation(instance):
    assert isinstance(instance, adb::ComponentList)

@given(instance=adb::SimpleExpression_strategy)
@settings(max_examples=50)
def test_adb::simpleexpression_instantiation(instance):
    assert isinstance(instance, adb::SimpleExpression)

@given(instance=adb::SimpleExpression_strategy)
def test_adb::simpleexpression_unaryAddingOperator_type(instance):
    assert isinstance(instance.unaryAddingOperator, str)


@given(instance=adb::SimpleExpression_strategy)
def test_adb::simpleexpression_unaryAddingOperator_setter(instance):
    original = instance.unaryAddingOperator
    instance.unaryAddingOperator = original
    assert instance.unaryAddingOperator == original

@given(instance=adb::SimpleExpression_strategy)
def test_adb::simpleexpression_binaryAddingOperators_type(instance):
    assert isinstance(instance.binaryAddingOperators, str)


@given(instance=adb::SimpleExpression_strategy)
def test_adb::simpleexpression_binaryAddingOperators_setter(instance):
    original = instance.binaryAddingOperators
    instance.binaryAddingOperators = original
    assert instance.binaryAddingOperators == original

@given(instance=IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_integertypedefinition_instantiation(instance):
    assert isinstance(instance, IntegerTypeDefinition)

@given(instance=adb::ModularTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::modulartypedefinition_instantiation(instance):
    assert isinstance(instance, adb::ModularTypeDefinition)

@given(instance=adb::SignedIntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::signedintegertypedefinition_instantiation(instance):
    assert isinstance(instance, adb::SignedIntegerTypeDefinition)

@given(instance=adb::ParameterSpecification_strategy)
@settings(max_examples=50)
def test_adb::parameterspecification_instantiation(instance):
    assert isinstance(instance, adb::ParameterSpecification)

@given(instance=ReturnSubtypeIndication_strategy)
@settings(max_examples=50)
def test_returnsubtypeindication_instantiation(instance):
    assert isinstance(instance, ReturnSubtypeIndication)

@given(instance=ArrayIndexes_strategy)
@settings(max_examples=50)
def test_arrayindexes_instantiation(instance):
    assert isinstance(instance, ArrayIndexes)

@given(instance=adb::ConstrainedIndexes_strategy)
@settings(max_examples=50)
def test_adb::constrainedindexes_instantiation(instance):
    assert isinstance(instance, adb::ConstrainedIndexes)

@given(instance=adb::UnconstrainedIndexes_strategy)
@settings(max_examples=50)
def test_adb::unconstrainedindexes_instantiation(instance):
    assert isinstance(instance, adb::UnconstrainedIndexes)

@given(instance=adb::ComponentDefinition_strategy)
@settings(max_examples=50)
def test_adb::componentdefinition_instantiation(instance):
    assert isinstance(instance, adb::ComponentDefinition)

@given(instance=adb::ComponentDefinition_strategy)
def test_adb::componentdefinition_aliased_type(instance):
    assert isinstance(instance.aliased, bool)


@given(instance=adb::ComponentDefinition_strategy)
def test_adb::componentdefinition_aliased_setter(instance):
    original = instance.aliased
    instance.aliased = original
    assert instance.aliased == original

@given(instance=adb::ArrayIndexes_strategy)
@settings(max_examples=50)
def test_adb::arrayindexes_instantiation(instance):
    assert isinstance(instance, adb::ArrayIndexes)

@given(instance=NotNullAccessDefinition_strategy)
@settings(max_examples=50)
def test_notnullaccessdefinition_instantiation(instance):
    assert isinstance(instance, NotNullAccessDefinition)

@given(instance=AccessSpecification_strategy)
@settings(max_examples=50)
def test_accessspecification_instantiation(instance):
    assert isinstance(instance, AccessSpecification)

@given(instance=adb::AccessToDataDefinition_strategy)
@settings(max_examples=50)
def test_adb::accesstodatadefinition_instantiation(instance):
    assert isinstance(instance, adb::AccessToDataDefinition)

@given(instance=adb::AccessToDataDefinition_strategy)
def test_adb::accesstodatadefinition_generalAccessModifier_type(instance):
    assert isinstance(instance.generalAccessModifier, str)


@given(instance=adb::AccessToDataDefinition_strategy)
def test_adb::accesstodatadefinition_generalAccessModifier_setter(instance):
    original = instance.generalAccessModifier
    instance.generalAccessModifier = original
    assert instance.generalAccessModifier == original

@given(instance=adb::AccessToSubprogramDefinition_strategy)
@settings(max_examples=50)
def test_adb::accesstosubprogramdefinition_instantiation(instance):
    assert isinstance(instance, adb::AccessToSubprogramDefinition)

@given(instance=adb::AccessToSubprogramDefinition_strategy)
def test_adb::accesstosubprogramdefinition_protected_type(instance):
    assert isinstance(instance.protected, bool)


@given(instance=adb::AccessToSubprogramDefinition_strategy)
def test_adb::accesstosubprogramdefinition_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=adb::AccessSpecification_strategy)
@settings(max_examples=50)
def test_adb::accessspecification_instantiation(instance):
    assert isinstance(instance, adb::AccessSpecification)

@given(instance=adb::AccessToDataInstance_strategy)
@settings(max_examples=50)
def test_adb::accesstodatainstance_instantiation(instance):
    assert isinstance(instance, adb::AccessToDataInstance)

@given(instance=adb::AccessToDataInstance_strategy)
def test_adb::accesstodatainstance_constant_type(instance):
    assert isinstance(instance.constant, str)


@given(instance=adb::AccessToDataInstance_strategy)
def test_adb::accesstodatainstance_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=adb::IntegerTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::integertypedefinition_instantiation(instance):
    assert isinstance(instance, adb::IntegerTypeDefinition)

@given(instance=adb::EnumerationTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::enumerationtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::EnumerationTypeDefinition)

@given(instance=adb::EnumerationTypeDefinition_strategy)
def test_adb::enumerationtypedefinition_enumerationliteralspecifications_type(instance):
    assert isinstance(instance.enumerationliteralspecifications, str)


@given(instance=adb::EnumerationTypeDefinition_strategy)
def test_adb::enumerationtypedefinition_enumerationliteralspecifications_setter(instance):
    original = instance.enumerationliteralspecifications
    instance.enumerationliteralspecifications = original
    assert instance.enumerationliteralspecifications == original

@given(instance=adb::DerivedTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::derivedtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::DerivedTypeDefinition)

@given(instance=adb::DerivedTypeDefinition_strategy)
def test_adb::derivedtypedefinition_limited_type(instance):
    assert isinstance(instance.limited, str)


@given(instance=adb::DerivedTypeDefinition_strategy)
def test_adb::derivedtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::DerivedTypeDefinition_strategy)
def test_adb::derivedtypedefinition_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=adb::DerivedTypeDefinition_strategy)
def test_adb::derivedtypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::RecordTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::recordtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::RecordTypeDefinition)

@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_tagged_type(instance):
    assert isinstance(instance.tagged, bool)


@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::RecordTypeDefinition_strategy)
def test_adb::recordtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::RealTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::realtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::RealTypeDefinition)

@given(instance=adb::NotNullAccessDefinition_strategy)
@settings(max_examples=50)
def test_adb::notnullaccessdefinition_instantiation(instance):
    assert isinstance(instance, adb::NotNullAccessDefinition)

@given(instance=adb::DiscriminantSpecification_strategy)
@settings(max_examples=50)
def test_adb::discriminantspecification_instantiation(instance):
    assert isinstance(instance, adb::DiscriminantSpecification)

@given(instance=adb::RecordDefinition_strategy)
@settings(max_examples=50)
def test_adb::recorddefinition_instantiation(instance):
    assert isinstance(instance, adb::RecordDefinition)

@given(instance=adb::RecordDefinition_strategy)
def test_adb::recorddefinition_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=adb::RecordDefinition_strategy)
def test_adb::recorddefinition_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=adb::RecordExtensionPart_strategy)
@settings(max_examples=50)
def test_adb::recordextensionpart_instantiation(instance):
    assert isinstance(instance, adb::RecordExtensionPart)

@given(instance=DiscriminantPart_strategy)
@settings(max_examples=50)
def test_discriminantpart_instantiation(instance):
    assert isinstance(instance, DiscriminantPart)

@given(instance=adb::UnknownDiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb::unknowndiscriminantpart_instantiation(instance):
    assert isinstance(instance, adb::UnknownDiscriminantPart)

@given(instance=adb::UnknownDiscriminantPart_strategy)
def test_adb::unknowndiscriminantpart_box_type(instance):
    assert isinstance(instance.box, bool)


@given(instance=adb::UnknownDiscriminantPart_strategy)
def test_adb::unknowndiscriminantpart_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb::ExplicitGenericActualParameter_strategy)
@settings(max_examples=50)
def test_adb::explicitgenericactualparameter_instantiation(instance):
    assert isinstance(instance, adb::ExplicitGenericActualParameter)

@given(instance=AbortStatement_strategy)
@settings(max_examples=50)
def test_abortstatement_instantiation(instance):
    assert isinstance(instance, AbortStatement)

@given(instance=adb::TaskNames_strategy)
@settings(max_examples=50)
def test_adb::tasknames_instantiation(instance):
    assert isinstance(instance, adb::TaskNames)

@given(instance=adb::EntryCallAlternative_strategy)
@settings(max_examples=50)
def test_adb::entrycallalternative_instantiation(instance):
    assert isinstance(instance, adb::EntryCallAlternative)

@given(instance=SelectAlternative_strategy)
@settings(max_examples=50)
def test_selectalternative_instantiation(instance):
    assert isinstance(instance, SelectAlternative)

@given(instance=adb::DelayAlternative_strategy)
@settings(max_examples=50)
def test_adb::delayalternative_instantiation(instance):
    assert isinstance(instance, adb::DelayAlternative)

@given(instance=adb::AcceptAlternative_strategy)
@settings(max_examples=50)
def test_adb::acceptalternative_instantiation(instance):
    assert isinstance(instance, adb::AcceptAlternative)

@given(instance=adb::GuardedAlternative_strategy)
@settings(max_examples=50)
def test_adb::guardedalternative_instantiation(instance):
    assert isinstance(instance, adb::GuardedAlternative)

@given(instance=adb::SelectAlternative_strategy)
@settings(max_examples=50)
def test_adb::selectalternative_instantiation(instance):
    assert isinstance(instance, adb::SelectAlternative)

@given(instance=adb::Guard_strategy)
@settings(max_examples=50)
def test_adb::guard_instantiation(instance):
    assert isinstance(instance, adb::Guard)

@given(instance=SelectStatement_strategy)
@settings(max_examples=50)
def test_selectstatement_instantiation(instance):
    assert isinstance(instance, SelectStatement)

@given(instance=adb::ConditionalEntryCall_strategy)
@settings(max_examples=50)
def test_adb::conditionalentrycall_instantiation(instance):
    assert isinstance(instance, adb::ConditionalEntryCall)

@given(instance=adb::TimedEntryCall_strategy)
@settings(max_examples=50)
def test_adb::timedentrycall_instantiation(instance):
    assert isinstance(instance, adb::TimedEntryCall)

@given(instance=adb::SelectiveAccept_strategy)
@settings(max_examples=50)
def test_adb::selectiveaccept_instantiation(instance):
    assert isinstance(instance, adb::SelectiveAccept)

@given(instance=adb::TriggeringStatement_strategy)
@settings(max_examples=50)
def test_adb::triggeringstatement_instantiation(instance):
    assert isinstance(instance, adb::TriggeringStatement)

@given(instance=adb::AbortablePart_strategy)
@settings(max_examples=50)
def test_adb::abortablepart_instantiation(instance):
    assert isinstance(instance, adb::AbortablePart)

@given(instance=adb::TriggeringAlternative_strategy)
@settings(max_examples=50)
def test_adb::triggeringalternative_instantiation(instance):
    assert isinstance(instance, adb::TriggeringAlternative)

@given(instance=adb::AsynchronousSelect_strategy)
@settings(max_examples=50)
def test_adb::asynchronousselect_instantiation(instance):
    assert isinstance(instance, adb::AsynchronousSelect)

@given(instance=adb::EntryIndexSpecification_strategy)
@settings(max_examples=50)
def test_adb::entryindexspecification_instantiation(instance):
    assert isinstance(instance, adb::EntryIndexSpecification)

@given(instance=adb::EntryIndexSpecification_strategy)
def test_adb::entryindexspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::EntryIndexSpecification_strategy)
def test_adb::entryindexspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::EntryBarrier_strategy)
@settings(max_examples=50)
def test_adb::entrybarrier_instantiation(instance):
    assert isinstance(instance, adb::EntryBarrier)

@given(instance=adb::EntryBodyFormalPart_strategy)
@settings(max_examples=50)
def test_adb::entrybodyformalpart_instantiation(instance):
    assert isinstance(instance, adb::EntryBodyFormalPart)

@given(instance=adb::EntryIndex_strategy)
@settings(max_examples=50)
def test_adb::entryindex_instantiation(instance):
    assert isinstance(instance, adb::EntryIndex)

@given(instance=adb::ProtectedOperationItem_strategy)
@settings(max_examples=50)
def test_adb::protectedoperationitem_instantiation(instance):
    assert isinstance(instance, adb::ProtectedOperationItem)

@given(instance=adb::ReturnSubtypeIndication_strategy)
@settings(max_examples=50)
def test_adb::returnsubtypeindication_instantiation(instance):
    assert isinstance(instance, adb::ReturnSubtypeIndication)

@given(instance=TriggeringStatement_strategy)
@settings(max_examples=50)
def test_triggeringstatement_instantiation(instance):
    assert isinstance(instance, TriggeringStatement)

@given(instance=adb::LoopParameterSpecification_strategy)
@settings(max_examples=50)
def test_adb::loopparameterspecification_instantiation(instance):
    assert isinstance(instance, adb::LoopParameterSpecification)

@given(instance=adb::LoopParameterSpecification_strategy)
def test_adb::loopparameterspecification_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=adb::LoopParameterSpecification_strategy)
def test_adb::loopparameterspecification_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb::IterationScheme_strategy)
@settings(max_examples=50)
def test_adb::iterationscheme_instantiation(instance):
    assert isinstance(instance, adb::IterationScheme)

@given(instance=CompoundStatement_strategy)
@settings(max_examples=50)
def test_compoundstatement_instantiation(instance):
    assert isinstance(instance, CompoundStatement)

@given(instance=adb::ExtendedReturnStatement_strategy)
@settings(max_examples=50)
def test_adb::extendedreturnstatement_instantiation(instance):
    assert isinstance(instance, adb::ExtendedReturnStatement)

@given(instance=adb::ExtendedReturnStatement_strategy)
def test_adb::extendedreturnstatement_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=adb::ExtendedReturnStatement_strategy)
def test_adb::extendedreturnstatement_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb::SelectStatement_strategy)
@settings(max_examples=50)
def test_adb::selectstatement_instantiation(instance):
    assert isinstance(instance, adb::SelectStatement)

@given(instance=adb::AcceptStatement_strategy)
@settings(max_examples=50)
def test_adb::acceptstatement_instantiation(instance):
    assert isinstance(instance, adb::AcceptStatement)

@given(instance=adb::AcceptStatement_strategy)
def test_adb::acceptstatement_entryidentifier_type(instance):
    assert isinstance(instance.entryidentifier, str)


@given(instance=adb::AcceptStatement_strategy)
def test_adb::acceptstatement_entryidentifier_setter(instance):
    original = instance.entryidentifier
    instance.entryidentifier = original
    assert instance.entryidentifier == original

@given(instance=adb::LoopStatement_strategy)
@settings(max_examples=50)
def test_adb::loopstatement_instantiation(instance):
    assert isinstance(instance, adb::LoopStatement)

@given(instance=adb::LoopStatement_strategy)
def test_adb::loopstatement_sameName_type(instance):
    assert isinstance(instance.sameName, str)


@given(instance=adb::LoopStatement_strategy)
def test_adb::loopstatement_sameName_setter(instance):
    original = instance.sameName
    instance.sameName = original
    assert instance.sameName == original

@given(instance=adb::LoopStatement_strategy)
def test_adb::loopstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::LoopStatement_strategy)
def test_adb::loopstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::IfStatement_strategy)
@settings(max_examples=50)
def test_adb::ifstatement_instantiation(instance):
    assert isinstance(instance, adb::IfStatement)

@given(instance=adb::PragmaArgumentAssociation_strategy)
@settings(max_examples=50)
def test_adb::pragmaargumentassociation_instantiation(instance):
    assert isinstance(instance, adb::PragmaArgumentAssociation)

@given(instance=adb::PragmaArgumentAssociation_strategy)
def test_adb::pragmaargumentassociation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::PragmaArgumentAssociation_strategy)
def test_adb::pragmaargumentassociation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::DiscreteChoiceList_strategy)
@settings(max_examples=50)
def test_adb::discretechoicelist_instantiation(instance):
    assert isinstance(instance, adb::DiscreteChoiceList)

@given(instance=adb::CaseStatementAlternative_strategy)
@settings(max_examples=50)
def test_adb::casestatementalternative_instantiation(instance):
    assert isinstance(instance, adb::CaseStatementAlternative)

@given(instance=adb::CaseStatement_strategy)
@settings(max_examples=50)
def test_adb::casestatement_instantiation(instance):
    assert isinstance(instance, adb::CaseStatement)

@given(instance=ObjectDeclaration_strategy)
@settings(max_examples=50)
def test_objectdeclaration_instantiation(instance):
    assert isinstance(instance, ObjectDeclaration)

@given(instance=adb::DataInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_adb::datainstancedeclaration_instantiation(instance):
    assert isinstance(instance, adb::DataInstanceDeclaration)

@given(instance=adb::DataInstanceDeclaration_strategy)
def test_adb::datainstancedeclaration_aliased_type(instance):
    assert isinstance(instance.aliased, bool)


@given(instance=adb::DataInstanceDeclaration_strategy)
def test_adb::datainstancedeclaration_aliased_setter(instance):
    original = instance.aliased
    instance.aliased = original
    assert instance.aliased == original

@given(instance=adb::DataInstanceDeclaration_strategy)
def test_adb::datainstancedeclaration_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=adb::DataInstanceDeclaration_strategy)
def test_adb::datainstancedeclaration_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=adb::GenericAssociation_strategy)
@settings(max_examples=50)
def test_adb::genericassociation_instantiation(instance):
    assert isinstance(instance, adb::GenericAssociation)

@given(instance=adb::GenericAssociation_strategy)
def test_adb::genericassociation_selectorName_type(instance):
    assert isinstance(instance.selectorName, str)


@given(instance=adb::GenericAssociation_strategy)
def test_adb::genericassociation_selectorName_setter(instance):
    original = instance.selectorName
    instance.selectorName = original
    assert instance.selectorName == original

@given(instance=adb::FormalPackageAssociation_strategy)
@settings(max_examples=50)
def test_adb::formalpackageassociation_instantiation(instance):
    assert isinstance(instance, adb::FormalPackageAssociation)

@given(instance=adb::FormalPackageAssociation_strategy)
def test_adb::formalpackageassociation_genericFormalParameterSelectorName_type(instance):
    assert isinstance(instance.genericFormalParameterSelectorName, str)


@given(instance=adb::FormalPackageAssociation_strategy)
def test_adb::formalpackageassociation_genericFormalParameterSelectorName_setter(instance):
    original = instance.genericFormalParameterSelectorName
    instance.genericFormalParameterSelectorName = original
    assert instance.genericFormalParameterSelectorName == original

@given(instance=adb::FormalPackageActualPart_strategy)
@settings(max_examples=50)
def test_adb::formalpackageactualpart_instantiation(instance):
    assert isinstance(instance, adb::FormalPackageActualPart)

@given(instance=adb::FormalPackageActualPart_strategy)
def test_adb::formalpackageactualpart_box_type(instance):
    assert isinstance(instance.box, bool)


@given(instance=adb::FormalPackageActualPart_strategy)
def test_adb::formalpackageactualpart_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb::SubprogramDefault_strategy)
@settings(max_examples=50)
def test_adb::subprogramdefault_instantiation(instance):
    assert isinstance(instance, adb::SubprogramDefault)

@given(instance=adb::SubprogramDefault_strategy)
def test_adb::subprogramdefault_defaultName_type(instance):
    assert isinstance(instance.defaultName, str)


@given(instance=adb::SubprogramDefault_strategy)
def test_adb::subprogramdefault_defaultName_setter(instance):
    original = instance.defaultName
    instance.defaultName = original
    assert instance.defaultName == original

@given(instance=adb::AnonymousAccessDefinition_strategy)
@settings(max_examples=50)
def test_adb::anonymousaccessdefinition_instantiation(instance):
    assert isinstance(instance, adb::AnonymousAccessDefinition)

@given(instance=adb::OptNullExclusion_strategy)
@settings(max_examples=50)
def test_adb::optnullexclusion_instantiation(instance):
    assert isinstance(instance, adb::OptNullExclusion)

@given(instance=adb::OptNullExclusion_strategy)
def test_adb::optnullexclusion_not_null_type(instance):
    assert isinstance(instance.not_null, str)


@given(instance=adb::OptNullExclusion_strategy)
def test_adb::optnullexclusion_not_null_setter(instance):
    original = instance.not_null
    instance.not_null = original
    assert instance.not_null == original

@given(instance=adb::SingleProtectedDeclaration_strategy)
@settings(max_examples=50)
def test_adb::singleprotecteddeclaration_instantiation(instance):
    assert isinstance(instance, adb::SingleProtectedDeclaration)

@given(instance=adb::SingleProtectedDeclaration_strategy)
def test_adb::singleprotecteddeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::SingleProtectedDeclaration_strategy)
def test_adb::singleprotecteddeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::Mode_strategy)
@settings(max_examples=50)
def test_adb::mode_instantiation(instance):
    assert isinstance(instance, adb::Mode)

@given(instance=adb::Mode_strategy)
def test_adb::mode_out_type(instance):
    assert isinstance(instance.out, bool)


@given(instance=adb::Mode_strategy)
def test_adb::mode_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original

@given(instance=adb::Mode_strategy)
def test_adb::mode_in__type(instance):
    assert isinstance(instance.in_, bool)


@given(instance=adb::Mode_strategy)
def test_adb::mode_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=adb::DefiningIdentifierList_strategy)
@settings(max_examples=50)
def test_adb::definingidentifierlist_instantiation(instance):
    assert isinstance(instance, adb::DefiningIdentifierList)

@given(instance=adb::DefiningIdentifierList_strategy)
def test_adb::definingidentifierlist_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::DefiningIdentifierList_strategy)
def test_adb::definingidentifierlist_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FormalTypeDefinition_strategy)
@settings(max_examples=50)
def test_formaltypedefinition_instantiation(instance):
    assert isinstance(instance, FormalTypeDefinition)

@given(instance=adb::FormalDerivedTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::formalderivedtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::FormalDerivedTypeDefinition)

@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_absract_type(instance):
    assert isinstance(instance.absract, str)


@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_absract_setter(instance):
    original = instance.absract
    instance.absract = original
    assert instance.absract == original

@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::FormalDerivedTypeDefinition_strategy)
def test_adb::formalderivedtypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::AccessTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::accesstypedefinition_instantiation(instance):
    assert isinstance(instance, adb::AccessTypeDefinition)

@given(instance=adb::InterfaceTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::interfacetypedefinition_instantiation(instance):
    assert isinstance(instance, adb::InterfaceTypeDefinition)

@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_synchro_type(instance):
    assert isinstance(instance.synchro, bool)


@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_synchro_setter(instance):
    original = instance.synchro
    instance.synchro = original
    assert instance.synchro == original

@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_task_type(instance):
    assert isinstance(instance.task, bool)


@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original

@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_protected_type(instance):
    assert isinstance(instance.protected, bool)


@given(instance=adb::InterfaceTypeDefinition_strategy)
def test_adb::interfacetypedefinition_protected_setter(instance):
    original = instance.protected
    instance.protected = original
    assert instance.protected == original

@given(instance=adb::ArrayTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::arraytypedefinition_instantiation(instance):
    assert isinstance(instance, adb::ArrayTypeDefinition)

@given(instance=GenericFormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_genericformalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, GenericFormalParameterDeclaration)

@given(instance=adb::FormalSubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_adb::formalsubprogramdeclaration_instantiation(instance):
    assert isinstance(instance, adb::FormalSubprogramDeclaration)

@given(instance=adb::FormalSubprogramDeclaration_strategy)
def test_adb::formalsubprogramdeclaration_abstract_type(instance):
    assert isinstance(instance.abstract, str)


@given(instance=adb::FormalSubprogramDeclaration_strategy)
def test_adb::formalsubprogramdeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::FormalPackageDeclaration_strategy)
@settings(max_examples=50)
def test_adb::formalpackagedeclaration_instantiation(instance):
    assert isinstance(instance, adb::FormalPackageDeclaration)

@given(instance=adb::FormalPackageDeclaration_strategy)
def test_adb::formalpackagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::FormalPackageDeclaration_strategy)
def test_adb::formalpackagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::FormalPackageDeclaration_strategy)
def test_adb::formalpackagedeclaration_genericPackageName_type(instance):
    assert isinstance(instance.genericPackageName, str)


@given(instance=adb::FormalPackageDeclaration_strategy)
def test_adb::formalpackagedeclaration_genericPackageName_setter(instance):
    original = instance.genericPackageName
    instance.genericPackageName = original
    assert instance.genericPackageName == original

@given(instance=adb::FormalTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::formaltypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::FormalTypeDeclaration)

@given(instance=adb::FormalTypeDeclaration_strategy)
def test_adb::formaltypedeclaration_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=adb::FormalTypeDeclaration_strategy)
def test_adb::formaltypedeclaration_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=adb::FormalObjectDeclaration_strategy)
@settings(max_examples=50)
def test_adb::formalobjectdeclaration_instantiation(instance):
    assert isinstance(instance, adb::FormalObjectDeclaration)

@given(instance=adb::FormalPrivateTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::formalprivatetypedefinition_instantiation(instance):
    assert isinstance(instance, adb::FormalPrivateTypeDefinition)

@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_tagged_type(instance):
    assert isinstance(instance.tagged, bool)


@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::FormalPrivateTypeDefinition_strategy)
def test_adb::formalprivatetypedefinition_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::FormalTypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::formaltypedefinition_instantiation(instance):
    assert isinstance(instance, adb::FormalTypeDefinition)

@given(instance=Range_strategy)
@settings(max_examples=50)
def test_range_instantiation(instance):
    assert isinstance(instance, Range)

@given(instance=adb::ExplicitRange_strategy)
@settings(max_examples=50)
def test_adb::explicitrange_instantiation(instance):
    assert isinstance(instance, adb::ExplicitRange)

@given(instance=adb::EntityRange_strategy)
@settings(max_examples=50)
def test_adb::entityrange_instantiation(instance):
    assert isinstance(instance, adb::EntityRange)

@given(instance=RangeConstraint_strategy)
@settings(max_examples=50)
def test_rangeconstraint_instantiation(instance):
    assert isinstance(instance, RangeConstraint)

@given(instance=adb::ParameterEffectiveValue_strategy)
@settings(max_examples=50)
def test_adb::parametereffectivevalue_instantiation(instance):
    assert isinstance(instance, adb::ParameterEffectiveValue)

@given(instance=adb::AttributeDesignator_strategy)
@settings(max_examples=50)
def test_adb::attributedesignator_instantiation(instance):
    assert isinstance(instance, adb::AttributeDesignator)

@given(instance=adb::PrimaryName_strategy)
@settings(max_examples=50)
def test_adb::primaryname_instantiation(instance):
    assert isinstance(instance, adb::PrimaryName)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=adb::ArrayComponentAssociation_strategy)
@settings(max_examples=50)
def test_adb::arraycomponentassociation_instantiation(instance):
    assert isinstance(instance, adb::ArrayComponentAssociation)

@given(instance=adb::ArrayComponentAssociation_strategy)
def test_adb::arraycomponentassociation_box_type(instance):
    assert isinstance(instance.box, bool)


@given(instance=adb::ArrayComponentAssociation_strategy)
def test_adb::arraycomponentassociation_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=ArrayAggregate_strategy)
@settings(max_examples=50)
def test_arrayaggregate_instantiation(instance):
    assert isinstance(instance, ArrayAggregate)

@given(instance=adb::NamedArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb::namedarrayaggregate_instantiation(instance):
    assert isinstance(instance, adb::NamedArrayAggregate)

@given(instance=adb::PositionalArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb::positionalarrayaggregate_instantiation(instance):
    assert isinstance(instance, adb::PositionalArrayAggregate)

@given(instance=adb::PositionalArrayAggregate_strategy)
def test_adb::positionalarrayaggregate_othersBox_type(instance):
    assert isinstance(instance.othersBox, bool)


@given(instance=adb::PositionalArrayAggregate_strategy)
def test_adb::positionalarrayaggregate_othersBox_setter(instance):
    original = instance.othersBox
    instance.othersBox = original
    assert instance.othersBox == original

@given(instance=adb::AncestorPart_strategy)
@settings(max_examples=50)
def test_adb::ancestorpart_instantiation(instance):
    assert isinstance(instance, adb::AncestorPart)

@given(instance=RecordComponentAssociation_strategy)
@settings(max_examples=50)
def test_recordcomponentassociation_instantiation(instance):
    assert isinstance(instance, RecordComponentAssociation)

@given(instance=adb::UninitializedComponents_strategy)
@settings(max_examples=50)
def test_adb::uninitializedcomponents_instantiation(instance):
    assert isinstance(instance, adb::UninitializedComponents)

@given(instance=adb::UninitializedComponents_strategy)
def test_adb::uninitializedcomponents_box_type(instance):
    assert isinstance(instance.box, bool)


@given(instance=adb::UninitializedComponents_strategy)
def test_adb::uninitializedcomponents_box_setter(instance):
    original = instance.box
    instance.box = original
    assert instance.box == original

@given(instance=adb::InitializedComponents_strategy)
@settings(max_examples=50)
def test_adb::initializedcomponents_instantiation(instance):
    assert isinstance(instance, adb::InitializedComponents)

@given(instance=adb::ParameterAssociation_strategy)
@settings(max_examples=50)
def test_adb::parameterassociation_instantiation(instance):
    assert isinstance(instance, adb::ParameterAssociation)

@given(instance=adb::ParameterAssociation_strategy)
def test_adb::parameterassociation_selectorName_type(instance):
    assert isinstance(instance.selectorName, str)


@given(instance=adb::ParameterAssociation_strategy)
def test_adb::parameterassociation_selectorName_setter(instance):
    original = instance.selectorName
    instance.selectorName = original
    assert instance.selectorName == original

@given(instance=adb::RecordComponentAssociation_strategy)
@settings(max_examples=50)
def test_adb::recordcomponentassociation_instantiation(instance):
    assert isinstance(instance, adb::RecordComponentAssociation)

@given(instance=RecordAggregate_strategy)
@settings(max_examples=50)
def test_recordaggregate_instantiation(instance):
    assert isinstance(instance, RecordAggregate)

@given(instance=adb::RecordComponentAssociationList_strategy)
@settings(max_examples=50)
def test_adb::recordcomponentassociationlist_instantiation(instance):
    assert isinstance(instance, adb::RecordComponentAssociationList)

@given(instance=adb::RecordComponentAssociationList_strategy)
def test_adb::recordcomponentassociationlist_nullRecord_type(instance):
    assert isinstance(instance.nullRecord, bool)


@given(instance=adb::RecordComponentAssociationList_strategy)
def test_adb::recordcomponentassociationlist_nullRecord_setter(instance):
    original = instance.nullRecord
    instance.nullRecord = original
    assert instance.nullRecord == original

@given(instance=Aggregate_strategy)
@settings(max_examples=50)
def test_aggregate_instantiation(instance):
    assert isinstance(instance, Aggregate)

@given(instance=adb::ArrayAggregate_strategy)
@settings(max_examples=50)
def test_adb::arrayaggregate_instantiation(instance):
    assert isinstance(instance, adb::ArrayAggregate)

@given(instance=adb::ExtensionAggregate_strategy)
@settings(max_examples=50)
def test_adb::extensionaggregate_instantiation(instance):
    assert isinstance(instance, adb::ExtensionAggregate)

@given(instance=adb::RecordAggregate_strategy)
@settings(max_examples=50)
def test_adb::recordaggregate_instantiation(instance):
    assert isinstance(instance, adb::RecordAggregate)

@given(instance=Qualifier_strategy)
@settings(max_examples=50)
def test_qualifier_instantiation(instance):
    assert isinstance(instance, Qualifier)

@given(instance=ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, ParenthesizedExpression)

@given(instance=adb::Aggregate_strategy)
@settings(max_examples=50)
def test_adb::aggregate_instantiation(instance):
    assert isinstance(instance, adb::Aggregate)

@given(instance=adb::ComponentChoiceList_strategy)
@settings(max_examples=50)
def test_adb::componentchoicelist_instantiation(instance):
    assert isinstance(instance, adb::ComponentChoiceList)

@given(instance=adb::ComponentChoiceList_strategy)
def test_adb::componentchoicelist_componentSelectorName_type(instance):
    assert isinstance(instance.componentSelectorName, str)


@given(instance=adb::ComponentChoiceList_strategy)
def test_adb::componentchoicelist_componentSelectorName_setter(instance):
    original = instance.componentSelectorName
    instance.componentSelectorName = original
    assert instance.componentSelectorName == original

@given(instance=adb::ComponentChoiceList_strategy)
def test_adb::componentchoicelist_others_type(instance):
    assert isinstance(instance.others, bool)


@given(instance=adb::ComponentChoiceList_strategy)
def test_adb::componentchoicelist_others_setter(instance):
    original = instance.others
    instance.others = original
    assert instance.others == original

@given(instance=adb::DiscriminantSelectors_strategy)
@settings(max_examples=50)
def test_adb::discriminantselectors_instantiation(instance):
    assert isinstance(instance, adb::DiscriminantSelectors)

@given(instance=adb::DiscriminantSelectors_strategy)
def test_adb::discriminantselectors_discriminantSelectorName_type(instance):
    assert isinstance(instance.discriminantSelectorName, str)


@given(instance=adb::DiscriminantSelectors_strategy)
def test_adb::discriminantselectors_discriminantSelectorName_setter(instance):
    original = instance.discriminantSelectorName
    instance.discriminantSelectorName = original
    assert instance.discriminantSelectorName == original

@given(instance=adb::DiscriminantAssociation_strategy)
@settings(max_examples=50)
def test_adb::discriminantassociation_instantiation(instance):
    assert isinstance(instance, adb::DiscriminantAssociation)

@given(instance=CompositeConstraint_strategy)
@settings(max_examples=50)
def test_compositeconstraint_instantiation(instance):
    assert isinstance(instance, CompositeConstraint)

@given(instance=adb::IndexConstraint_strategy)
@settings(max_examples=50)
def test_adb::indexconstraint_instantiation(instance):
    assert isinstance(instance, adb::IndexConstraint)

@given(instance=adb::DiscriminantConstraint_strategy)
@settings(max_examples=50)
def test_adb::discriminantconstraint_instantiation(instance):
    assert isinstance(instance, adb::DiscriminantConstraint)

@given(instance=adb::CompositeConstraint_strategy)
@settings(max_examples=50)
def test_adb::compositeconstraint_instantiation(instance):
    assert isinstance(instance, adb::CompositeConstraint)

@given(instance=adb::OptConstraint_strategy)
@settings(max_examples=50)
def test_adb::optconstraint_instantiation(instance):
    assert isinstance(instance, adb::OptConstraint)

@given(instance=DiscreteRange_strategy)
@settings(max_examples=50)
def test_discreterange_instantiation(instance):
    assert isinstance(instance, DiscreteRange)

@given(instance=DiscreteSubtypeDefinition_strategy)
@settings(max_examples=50)
def test_discretesubtypedefinition_instantiation(instance):
    assert isinstance(instance, DiscreteSubtypeDefinition)

@given(instance=adb::DiscreteRange_strategy)
@settings(max_examples=50)
def test_adb::discreterange_instantiation(instance):
    assert isinstance(instance, adb::DiscreteRange)

@given(instance=adb::Qualifier_strategy)
@settings(max_examples=50)
def test_adb::qualifier_instantiation(instance):
    assert isinstance(instance, adb::Qualifier)

@given(instance=Primary_strategy)
@settings(max_examples=50)
def test_primary_instantiation(instance):
    assert isinstance(instance, Primary)

@given(instance=adb::Allocator_strategy)
@settings(max_examples=50)
def test_adb::allocator_instantiation(instance):
    assert isinstance(instance, adb::Allocator)

@given(instance=adb::Null_strategy)
@settings(max_examples=50)
def test_adb::null_instantiation(instance):
    assert isinstance(instance, adb::Null)

@given(instance=adb::Null_strategy)
def test_adb::null_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adb::Null_strategy)
def test_adb::null_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adb::QualifiedName_strategy)
@settings(max_examples=50)
def test_adb::qualifiedname_instantiation(instance):
    assert isinstance(instance, adb::QualifiedName)

@given(instance=adb::StringLiteral_strategy)
@settings(max_examples=50)
def test_adb::stringliteral_instantiation(instance):
    assert isinstance(instance, adb::StringLiteral)

@given(instance=adb::StringLiteral_strategy)
def test_adb::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adb::StringLiteral_strategy)
def test_adb::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=adb::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_adb::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, adb::ParenthesizedExpression)

@given(instance=adb::NumericLiteral_strategy)
@settings(max_examples=50)
def test_adb::numericliteral_instantiation(instance):
    assert isinstance(instance, adb::NumericLiteral)

@given(instance=adb::NumericLiteral_strategy)
def test_adb::numericliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=adb::NumericLiteral_strategy)
def test_adb::numericliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ScalarConstraint_strategy)
@settings(max_examples=50)
def test_scalarconstraint_instantiation(instance):
    assert isinstance(instance, ScalarConstraint)

@given(instance=adb::DeltaConstraint_strategy)
@settings(max_examples=50)
def test_adb::deltaconstraint_instantiation(instance):
    assert isinstance(instance, adb::DeltaConstraint)

@given(instance=adb::RangeConstraint_strategy)
@settings(max_examples=50)
def test_adb::rangeconstraint_instantiation(instance):
    assert isinstance(instance, adb::RangeConstraint)

@given(instance=adb::DigitsConstraint_strategy)
@settings(max_examples=50)
def test_adb::digitsconstraint_instantiation(instance):
    assert isinstance(instance, adb::DigitsConstraint)

@given(instance=adb::ScalarConstraint_strategy)
@settings(max_examples=50)
def test_adb::scalarconstraint_instantiation(instance):
    assert isinstance(instance, adb::ScalarConstraint)

@given(instance=adb::EObject_strategy)
@settings(max_examples=50)
def test_adb::eobject_instantiation(instance):
    assert isinstance(instance, adb::EObject)

@given(instance=adb::Factor_strategy)
@settings(max_examples=50)
def test_adb::factor_instantiation(instance):
    assert isinstance(instance, adb::Factor)

@given(instance=adb::Factor_strategy)
def test_adb::factor_abs_type(instance):
    assert isinstance(instance.abs, bool)


@given(instance=adb::Factor_strategy)
def test_adb::factor_abs_setter(instance):
    original = instance.abs
    instance.abs = original
    assert instance.abs == original

@given(instance=adb::Factor_strategy)
def test_adb::factor_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=adb::Factor_strategy)
def test_adb::factor_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=adb::Term_strategy)
@settings(max_examples=50)
def test_adb::term_instantiation(instance):
    assert isinstance(instance, adb::Term)

@given(instance=adb::Term_strategy)
def test_adb::term_multiplyingOperators_type(instance):
    assert isinstance(instance.multiplyingOperators, str)


@given(instance=adb::Term_strategy)
def test_adb::term_multiplyingOperators_setter(instance):
    original = instance.multiplyingOperators
    instance.multiplyingOperators = original
    assert instance.multiplyingOperators == original

@given(instance=adb::Interval_strategy)
@settings(max_examples=50)
def test_adb::interval_instantiation(instance):
    assert isinstance(instance, adb::Interval)

@given(instance=adb::Membership_strategy)
@settings(max_examples=50)
def test_adb::membership_instantiation(instance):
    assert isinstance(instance, adb::Membership)

@given(instance=adb::Membership_strategy)
def test_adb::membership_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=adb::Membership_strategy)
def test_adb::membership_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=adb::Relation_strategy)
@settings(max_examples=50)
def test_adb::relation_instantiation(instance):
    assert isinstance(instance, adb::Relation)

@given(instance=adb::Relation_strategy)
def test_adb::relation_relationalOperator_type(instance):
    assert isinstance(instance.relationalOperator, str)


@given(instance=adb::Relation_strategy)
def test_adb::relation_relationalOperator_setter(instance):
    original = instance.relationalOperator
    instance.relationalOperator = original
    assert instance.relationalOperator == original

@given(instance=ParameterEffectiveValue_strategy)
@settings(max_examples=50)
def test_parametereffectivevalue_instantiation(instance):
    assert isinstance(instance, ParameterEffectiveValue)

@given(instance=adb::Range_strategy)
@settings(max_examples=50)
def test_adb::range_instantiation(instance):
    assert isinstance(instance, adb::Range)

@given(instance=AncestorPart_strategy)
@settings(max_examples=50)
def test_ancestorpart_instantiation(instance):
    assert isinstance(instance, AncestorPart)

@given(instance=adb::Expression_strategy)
@settings(max_examples=50)
def test_adb::expression_instantiation(instance):
    assert isinstance(instance, adb::Expression)

@given(instance=adb::Expression_strategy)
def test_adb::expression_booleanOperator_type(instance):
    assert isinstance(instance.booleanOperator, str)


@given(instance=adb::Expression_strategy)
def test_adb::expression_booleanOperator_setter(instance):
    original = instance.booleanOperator
    instance.booleanOperator = original
    assert instance.booleanOperator == original

@given(instance=adb::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_adb::exceptionhandler_instantiation(instance):
    assert isinstance(instance, adb::ExceptionHandler)

@given(instance=adb::ExceptionHandler_strategy)
def test_adb::exceptionhandler_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::ExceptionHandler_strategy)
def test_adb::exceptionhandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::GenericItem_strategy)
@settings(max_examples=50)
def test_adb::genericitem_instantiation(instance):
    assert isinstance(instance, adb::GenericItem)

@given(instance=SimpleStatement_strategy)
@settings(max_examples=50)
def test_simplestatement_instantiation(instance):
    assert isinstance(instance, SimpleStatement)

@given(instance=adb::AbortStatement_strategy)
@settings(max_examples=50)
def test_adb::abortstatement_instantiation(instance):
    assert isinstance(instance, adb::AbortStatement)

@given(instance=adb::SimpleReturnStatement_strategy)
@settings(max_examples=50)
def test_adb::simplereturnstatement_instantiation(instance):
    assert isinstance(instance, adb::SimpleReturnStatement)

@given(instance=adb::GotoStatement_strategy)
@settings(max_examples=50)
def test_adb::gotostatement_instantiation(instance):
    assert isinstance(instance, adb::GotoStatement)

@given(instance=adb::GotoStatement_strategy)
def test_adb::gotostatement_labelId_type(instance):
    assert isinstance(instance.labelId, str)


@given(instance=adb::GotoStatement_strategy)
def test_adb::gotostatement_labelId_setter(instance):
    original = instance.labelId
    instance.labelId = original
    assert instance.labelId == original

@given(instance=adb::ProcedureOrEntryCallStatement_strategy)
@settings(max_examples=50)
def test_adb::procedureorentrycallstatement_instantiation(instance):
    assert isinstance(instance, adb::ProcedureOrEntryCallStatement)

@given(instance=adb::DelayStatement_strategy)
@settings(max_examples=50)
def test_adb::delaystatement_instantiation(instance):
    assert isinstance(instance, adb::DelayStatement)

@given(instance=adb::DelayStatement_strategy)
def test_adb::delaystatement_until_type(instance):
    assert isinstance(instance.until, str)


@given(instance=adb::DelayStatement_strategy)
def test_adb::delaystatement_until_setter(instance):
    original = instance.until
    instance.until = original
    assert instance.until == original

@given(instance=adb::RaiseStatement_strategy)
@settings(max_examples=50)
def test_adb::raisestatement_instantiation(instance):
    assert isinstance(instance, adb::RaiseStatement)

@given(instance=adb::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_adb::assignmentstatement_instantiation(instance):
    assert isinstance(instance, adb::AssignmentStatement)

@given(instance=adb::RequeueStatement_strategy)
@settings(max_examples=50)
def test_adb::requeuestatement_instantiation(instance):
    assert isinstance(instance, adb::RequeueStatement)

@given(instance=adb::RequeueStatement_strategy)
def test_adb::requeuestatement_abort_type(instance):
    assert isinstance(instance.abort, bool)


@given(instance=adb::RequeueStatement_strategy)
def test_adb::requeuestatement_abort_setter(instance):
    original = instance.abort
    instance.abort = original
    assert instance.abort == original

@given(instance=adb::ExitStatement_strategy)
@settings(max_examples=50)
def test_adb::exitstatement_instantiation(instance):
    assert isinstance(instance, adb::ExitStatement)

@given(instance=adb::NullStatement_strategy)
@settings(max_examples=50)
def test_adb::nullstatement_instantiation(instance):
    assert isinstance(instance, adb::NullStatement)

@given(instance=adb::NullStatement_strategy)
def test_adb::nullstatement_null_type(instance):
    assert isinstance(instance.null, bool)


@given(instance=adb::NullStatement_strategy)
def test_adb::nullstatement_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=adb::CompoundStatement_strategy)
@settings(max_examples=50)
def test_adb::compoundstatement_instantiation(instance):
    assert isinstance(instance, adb::CompoundStatement)

@given(instance=adb::SimpleStatement_strategy)
@settings(max_examples=50)
def test_adb::simplestatement_instantiation(instance):
    assert isinstance(instance, adb::SimpleStatement)

@given(instance=adb::Statement_strategy)
@settings(max_examples=50)
def test_adb::statement_instantiation(instance):
    assert isinstance(instance, adb::Statement)

@given(instance=adb::LabelisableStatement_strategy)
@settings(max_examples=50)
def test_adb::labelisablestatement_instantiation(instance):
    assert isinstance(instance, adb::LabelisableStatement)

@given(instance=AbortablePart_strategy)
@settings(max_examples=50)
def test_abortablepart_instantiation(instance):
    assert isinstance(instance, AbortablePart)

@given(instance=HandledSequenceOfStatements_strategy)
@settings(max_examples=50)
def test_handledsequenceofstatements_instantiation(instance):
    assert isinstance(instance, HandledSequenceOfStatements)

@given(instance=adb::SequenceOfStatements_strategy)
@settings(max_examples=50)
def test_adb::sequenceofstatements_instantiation(instance):
    assert isinstance(instance, adb::SequenceOfStatements)

@given(instance=adb::Label_strategy)
@settings(max_examples=50)
def test_adb::label_instantiation(instance):
    assert isinstance(instance, adb::Label)

@given(instance=adb::Label_strategy)
def test_adb::label_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=adb::Label_strategy)
def test_adb::label_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=adb::BodyStub_strategy)
@settings(max_examples=50)
def test_adb::bodystub_instantiation(instance):
    assert isinstance(instance, adb::BodyStub)

@given(instance=adb::BodyStub_strategy)
def test_adb::bodystub_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::BodyStub_strategy)
def test_adb::bodystub_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::ProperBody_strategy)
@settings(max_examples=50)
def test_adb::properbody_instantiation(instance):
    assert isinstance(instance, adb::ProperBody)

@given(instance=ProtectedElementDeclaration_strategy)
@settings(max_examples=50)
def test_protectedelementdeclaration_instantiation(instance):
    assert isinstance(instance, ProtectedElementDeclaration)

@given(instance=adb::ComponentDeclaration_strategy)
@settings(max_examples=50)
def test_adb::componentdeclaration_instantiation(instance):
    assert isinstance(instance, adb::ComponentDeclaration)

@given(instance=adb::ProtectedOperationDeclaration_strategy)
@settings(max_examples=50)
def test_adb::protectedoperationdeclaration_instantiation(instance):
    assert isinstance(instance, adb::ProtectedOperationDeclaration)

@given(instance=adb::ProtectedElementDeclaration_strategy)
@settings(max_examples=50)
def test_adb::protectedelementdeclaration_instantiation(instance):
    assert isinstance(instance, adb::ProtectedElementDeclaration)

@given(instance=adb::ProtectedDefinition_strategy)
@settings(max_examples=50)
def test_adb::protecteddefinition_instantiation(instance):
    assert isinstance(instance, adb::ProtectedDefinition)

@given(instance=adb::FormalPart_strategy)
@settings(max_examples=50)
def test_adb::formalpart_instantiation(instance):
    assert isinstance(instance, adb::FormalPart)

@given(instance=adb::DiscreteSubtypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::discretesubtypedefinition_instantiation(instance):
    assert isinstance(instance, adb::DiscreteSubtypeDefinition)

@given(instance=adb::Name_strategy)
@settings(max_examples=50)
def test_adb::name_instantiation(instance):
    assert isinstance(instance, adb::Name)

@given(instance=adb::Name_strategy)
def test_adb::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::Name_strategy)
def test_adb::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::ExceptionChoice_strategy)
@settings(max_examples=50)
def test_adb::exceptionchoice_instantiation(instance):
    assert isinstance(instance, adb::ExceptionChoice)

@given(instance=adb::ExceptionChoice_strategy)
def test_adb::exceptionchoice_others_type(instance):
    assert isinstance(instance.others, bool)


@given(instance=adb::ExceptionChoice_strategy)
def test_adb::exceptionchoice_others_setter(instance):
    original = instance.others
    instance.others = original
    assert instance.others == original

@given(instance=adb::ParameterAndResultProfile_strategy)
@settings(max_examples=50)
def test_adb::parameterandresultprofile_instantiation(instance):
    assert isinstance(instance, adb::ParameterAndResultProfile)

@given(instance=SubprogramSpecification_strategy)
@settings(max_examples=50)
def test_subprogramspecification_instantiation(instance):
    assert isinstance(instance, SubprogramSpecification)

@given(instance=adb::FunctionSpecification_strategy)
@settings(max_examples=50)
def test_adb::functionspecification_instantiation(instance):
    assert isinstance(instance, adb::FunctionSpecification)

@given(instance=adb::ProcedureSpecification_strategy)
@settings(max_examples=50)
def test_adb::procedurespecification_instantiation(instance):
    assert isinstance(instance, adb::ProcedureSpecification)

@given(instance=BodyStub_strategy)
@settings(max_examples=50)
def test_bodystub_instantiation(instance):
    assert isinstance(instance, BodyStub)

@given(instance=adb::ProtectedBodyStub_strategy)
@settings(max_examples=50)
def test_adb::protectedbodystub_instantiation(instance):
    assert isinstance(instance, adb::ProtectedBodyStub)

@given(instance=adb::PackageBodyStub_strategy)
@settings(max_examples=50)
def test_adb::packagebodystub_instantiation(instance):
    assert isinstance(instance, adb::PackageBodyStub)

@given(instance=adb::TaskBodyStub_strategy)
@settings(max_examples=50)
def test_adb::taskbodystub_instantiation(instance):
    assert isinstance(instance, adb::TaskBodyStub)

@given(instance=NewTypeDeclaration_strategy)
@settings(max_examples=50)
def test_newtypedeclaration_instantiation(instance):
    assert isinstance(instance, NewTypeDeclaration)

@given(instance=adb::FullTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::fulltypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::FullTypeDeclaration)

@given(instance=TypeDeclaration_strategy)
@settings(max_examples=50)
def test_typedeclaration_instantiation(instance):
    assert isinstance(instance, TypeDeclaration)

@given(instance=adb::SubtypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::subtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::SubtypeDeclaration)

@given(instance=adb::NewTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::newtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::NewTypeDeclaration)

@given(instance=adb::TaskDefinition_strategy)
@settings(max_examples=50)
def test_adb::taskdefinition_instantiation(instance):
    assert isinstance(instance, adb::TaskDefinition)

@given(instance=adb::InterfaceList_strategy)
@settings(max_examples=50)
def test_adb::interfacelist_instantiation(instance):
    assert isinstance(instance, adb::InterfaceList)

@given(instance=adb::KnownDiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb::knowndiscriminantpart_instantiation(instance):
    assert isinstance(instance, adb::KnownDiscriminantPart)

@given(instance=DeclarativeItem_strategy)
@settings(max_examples=50)
def test_declarativeitem_instantiation(instance):
    assert isinstance(instance, DeclarativeItem)

@given(instance=adb::Body_strategy)
@settings(max_examples=50)
def test_adb::body_instantiation(instance):
    assert isinstance(instance, adb::Body)

@given(instance=ProtectedOperationDeclaration_strategy)
@settings(max_examples=50)
def test_protectedoperationdeclaration_instantiation(instance):
    assert isinstance(instance, ProtectedOperationDeclaration)

@given(instance=TaskItem_strategy)
@settings(max_examples=50)
def test_taskitem_instantiation(instance):
    assert isinstance(instance, TaskItem)

@given(instance=adb::EntryDeclaration_strategy)
@settings(max_examples=50)
def test_adb::entrydeclaration_instantiation(instance):
    assert isinstance(instance, adb::EntryDeclaration)

@given(instance=adb::EntryDeclaration_strategy)
def test_adb::entrydeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::EntryDeclaration_strategy)
def test_adb::entrydeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::TaskItem_strategy)
@settings(max_examples=50)
def test_adb::taskitem_instantiation(instance):
    assert isinstance(instance, adb::TaskItem)

@given(instance=adb::SubtypeIndication_strategy)
@settings(max_examples=50)
def test_adb::subtypeindication_instantiation(instance):
    assert isinstance(instance, adb::SubtypeIndication)

@given(instance=adb::SubtypeIndication_strategy)
def test_adb::subtypeindication_subtypeMark_type(instance):
    assert isinstance(instance.subtypeMark, str)


@given(instance=adb::SubtypeIndication_strategy)
def test_adb::subtypeindication_subtypeMark_setter(instance):
    original = instance.subtypeMark
    instance.subtypeMark = original
    assert instance.subtypeMark == original

@given(instance=adb::PrivateExtensionDeclaration_strategy)
@settings(max_examples=50)
def test_adb::privateextensiondeclaration_instantiation(instance):
    assert isinstance(instance, adb::PrivateExtensionDeclaration)

@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_synchronized_type(instance):
    assert isinstance(instance.synchronized, bool)


@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=adb::PrivateExtensionDeclaration_strategy)
def test_adb::privateextensiondeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::PrivateTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::privatetypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::PrivateTypeDeclaration)

@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_tagged_type(instance):
    assert isinstance(instance.tagged, bool)


@given(instance=adb::PrivateTypeDeclaration_strategy)
def test_adb::privatetypedeclaration_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb::DiscriminantPart_strategy)
@settings(max_examples=50)
def test_adb::discriminantpart_instantiation(instance):
    assert isinstance(instance, adb::DiscriminantPart)

@given(instance=adb::IncompleteTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::incompletetypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::IncompleteTypeDeclaration)

@given(instance=adb::IncompleteTypeDeclaration_strategy)
def test_adb::incompletetypedeclaration_tagged_type(instance):
    assert isinstance(instance.tagged, bool)


@given(instance=adb::IncompleteTypeDeclaration_strategy)
def test_adb::incompletetypedeclaration_tagged_setter(instance):
    original = instance.tagged
    instance.tagged = original
    assert instance.tagged == original

@given(instance=adb::TypeDefinition_strategy)
@settings(max_examples=50)
def test_adb::typedefinition_instantiation(instance):
    assert isinstance(instance, adb::TypeDefinition)

@given(instance=FullTypeDeclaration_strategy)
@settings(max_examples=50)
def test_fulltypedeclaration_instantiation(instance):
    assert isinstance(instance, FullTypeDeclaration)

@given(instance=adb::ProtectedTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::protectedtypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::ProtectedTypeDeclaration)

@given(instance=adb::FullDataTypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::fulldatatypedeclaration_instantiation(instance):
    assert isinstance(instance, adb::FullDataTypeDeclaration)

@given(instance=adb::PackageSpecification_strategy)
@settings(max_examples=50)
def test_adb::packagespecification_instantiation(instance):
    assert isinstance(instance, adb::PackageSpecification)

@given(instance=adb::PackageSpecification_strategy)
def test_adb::packagespecification_endname_type(instance):
    assert isinstance(instance.endname, str)


@given(instance=adb::PackageSpecification_strategy)
def test_adb::packagespecification_endname_setter(instance):
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

@given(instance=adb::Renaming_strategy)
@settings(max_examples=50)
def test_adb::renaming_instantiation(instance):
    assert isinstance(instance, adb::Renaming)

@given(instance=adb::Renaming_strategy)
def test_adb::renaming_renamed_type(instance):
    assert isinstance(instance.renamed, str)


@given(instance=adb::Renaming_strategy)
def test_adb::renaming_renamed_setter(instance):
    original = instance.renamed
    instance.renamed = original
    assert instance.renamed == original

@given(instance=adb::PackageDefinition_strategy)
@settings(max_examples=50)
def test_adb::packagedefinition_instantiation(instance):
    assert isinstance(instance, adb::PackageDefinition)

@given(instance=BasicDeclaration_strategy)
@settings(max_examples=50)
def test_basicdeclaration_instantiation(instance):
    assert isinstance(instance, BasicDeclaration)

@given(instance=adb::NumberDeclaration_strategy)
@settings(max_examples=50)
def test_adb::numberdeclaration_instantiation(instance):
    assert isinstance(instance, adb::NumberDeclaration)

@given(instance=adb::TaskDeclaration_strategy)
@settings(max_examples=50)
def test_adb::taskdeclaration_instantiation(instance):
    assert isinstance(instance, adb::TaskDeclaration)

@given(instance=adb::TaskDeclaration_strategy)
def test_adb::taskdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::TaskDeclaration_strategy)
def test_adb::taskdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_adb::typedeclaration_instantiation(instance):
    assert isinstance(instance, adb::TypeDeclaration)

@given(instance=adb::TypeDeclaration_strategy)
def test_adb::typedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::TypeDeclaration_strategy)
def test_adb::typedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::ExceptionDeclaration_strategy)
@settings(max_examples=50)
def test_adb::exceptiondeclaration_instantiation(instance):
    assert isinstance(instance, adb::ExceptionDeclaration)

@given(instance=adb::ObjectDeclaration_strategy)
@settings(max_examples=50)
def test_adb::objectdeclaration_instantiation(instance):
    assert isinstance(instance, adb::ObjectDeclaration)

@given(instance=LibraryUnitSpecification_strategy)
@settings(max_examples=50)
def test_libraryunitspecification_instantiation(instance):
    assert isinstance(instance, LibraryUnitSpecification)

@given(instance=adb::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_adb::packagedeclaration_instantiation(instance):
    assert isinstance(instance, adb::PackageDeclaration)

@given(instance=adb::PackageDeclaration_strategy)
def test_adb::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::PackageDeclaration_strategy)
def test_adb::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::LibraryUnitSpecification_strategy)
@settings(max_examples=50)
def test_adb::libraryunitspecification_instantiation(instance):
    assert isinstance(instance, adb::LibraryUnitSpecification)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=adb::SeparateSubunit_strategy)
@settings(max_examples=50)
def test_adb::separatesubunit_instantiation(instance):
    assert isinstance(instance, adb::SeparateSubunit)

@given(instance=adb::SeparateSubunit_strategy)
def test_adb::separatesubunit_parentUnitName_type(instance):
    assert isinstance(instance.parentUnitName, str)


@given(instance=adb::SeparateSubunit_strategy)
def test_adb::separatesubunit_parentUnitName_setter(instance):
    original = instance.parentUnitName
    instance.parentUnitName = original
    assert instance.parentUnitName == original

@given(instance=adb::HandledSequenceOfStatements_strategy)
@settings(max_examples=50)
def test_adb::handledsequenceofstatements_instantiation(instance):
    assert isinstance(instance, adb::HandledSequenceOfStatements)

@given(instance=adb::DeclarativeItem_strategy)
@settings(max_examples=50)
def test_adb::declarativeitem_instantiation(instance):
    assert isinstance(instance, adb::DeclarativeItem)

@given(instance=adb::DeclarativeBlock_strategy)
@settings(max_examples=50)
def test_adb::declarativeblock_instantiation(instance):
    assert isinstance(instance, adb::DeclarativeBlock)

@given(instance=adb::SubprogramSpecification_strategy)
@settings(max_examples=50)
def test_adb::subprogramspecification_instantiation(instance):
    assert isinstance(instance, adb::SubprogramSpecification)

@given(instance=ProtectedOperationItem_strategy)
@settings(max_examples=50)
def test_protectedoperationitem_instantiation(instance):
    assert isinstance(instance, ProtectedOperationItem)

@given(instance=adb::SubprogramDeclaration_strategy)
@settings(max_examples=50)
def test_adb::subprogramdeclaration_instantiation(instance):
    assert isinstance(instance, adb::SubprogramDeclaration)

@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_null_type(instance):
    assert isinstance(instance.null, bool)


@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_renamedName_type(instance):
    assert isinstance(instance.renamedName, str)


@given(instance=adb::SubprogramDeclaration_strategy)
def test_adb::subprogramdeclaration_renamedName_setter(instance):
    original = instance.renamedName
    instance.renamedName = original
    assert instance.renamedName == original

@given(instance=ProperBody_strategy)
@settings(max_examples=50)
def test_properbody_instantiation(instance):
    assert isinstance(instance, ProperBody)

@given(instance=adb::ProtectedBody_strategy)
@settings(max_examples=50)
def test_adb::protectedbody_instantiation(instance):
    assert isinstance(instance, adb::ProtectedBody)

@given(instance=adb::ProtectedBody_strategy)
def test_adb::protectedbody_idTask_type(instance):
    assert isinstance(instance.idTask, str)


@given(instance=adb::ProtectedBody_strategy)
def test_adb::protectedbody_idTask_setter(instance):
    original = instance.idTask
    instance.idTask = original
    assert instance.idTask == original

@given(instance=adb::ProtectedBody_strategy)
def test_adb::protectedbody_identifier_type(instance):
    assert isinstance(instance.identifier, str)


@given(instance=adb::ProtectedBody_strategy)
def test_adb::protectedbody_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=DeclarativeBlock_strategy)
@settings(max_examples=50)
def test_declarativeblock_instantiation(instance):
    assert isinstance(instance, DeclarativeBlock)

@given(instance=adb::EntryBody_strategy)
@settings(max_examples=50)
def test_adb::entrybody_instantiation(instance):
    assert isinstance(instance, adb::EntryBody)

@given(instance=adb::EntryBody_strategy)
def test_adb::entrybody_endid_type(instance):
    assert isinstance(instance.endid, str)


@given(instance=adb::EntryBody_strategy)
def test_adb::entrybody_endid_setter(instance):
    original = instance.endid
    instance.endid = original
    assert instance.endid == original

@given(instance=adb::TaskBody_strategy)
@settings(max_examples=50)
def test_adb::taskbody_instantiation(instance):
    assert isinstance(instance, adb::TaskBody)

@given(instance=adb::BlockStatement_strategy)
@settings(max_examples=50)
def test_adb::blockstatement_instantiation(instance):
    assert isinstance(instance, adb::BlockStatement)

@given(instance=adb::BlockStatement_strategy)
def test_adb::blockstatement_blockStatementIdentifier_type(instance):
    assert isinstance(instance.blockStatementIdentifier, str)


@given(instance=adb::BlockStatement_strategy)
def test_adb::blockstatement_blockStatementIdentifier_setter(instance):
    original = instance.blockStatementIdentifier
    instance.blockStatementIdentifier = original
    assert instance.blockStatementIdentifier == original

@given(instance=adb::PackageBody_strategy)
@settings(max_examples=50)
def test_adb::packagebody_instantiation(instance):
    assert isinstance(instance, adb::PackageBody)

@given(instance=adb::SubprogramBody_strategy)
@settings(max_examples=50)
def test_adb::subprogrambody_instantiation(instance):
    assert isinstance(instance, adb::SubprogramBody)

@given(instance=adb::SubprogramBody_strategy)
def test_adb::subprogrambody_endname_type(instance):
    assert isinstance(instance.endname, str)


@given(instance=adb::SubprogramBody_strategy)
def test_adb::subprogrambody_endname_setter(instance):
    original = instance.endname
    instance.endname = original
    assert instance.endname == original

@given(instance=adb::BasicDeclarativeItem_strategy)
@settings(max_examples=50)
def test_adb::basicdeclarativeitem_instantiation(instance):
    assert isinstance(instance, adb::BasicDeclarativeItem)

@given(instance=adb::GenericActualPart_strategy)
@settings(max_examples=50)
def test_adb::genericactualpart_instantiation(instance):
    assert isinstance(instance, adb::GenericActualPart)

@given(instance=adb::OverridingIndicator_strategy)
@settings(max_examples=50)
def test_adb::overridingindicator_instantiation(instance):
    assert isinstance(instance, adb::OverridingIndicator)

@given(instance=adb::OverridingIndicator_strategy)
def test_adb::overridingindicator_not__type(instance):
    assert isinstance(instance.not_, bool)


@given(instance=adb::OverridingIndicator_strategy)
def test_adb::overridingindicator_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=adb::GenericInstantiation_strategy)
@settings(max_examples=50)
def test_adb::genericinstantiation_instantiation(instance):
    assert isinstance(instance, adb::GenericInstantiation)

@given(instance=adb::GenericInstantiation_strategy)
def test_adb::genericinstantiation_genericName_type(instance):
    assert isinstance(instance.genericName, str)


@given(instance=adb::GenericInstantiation_strategy)
def test_adb::genericinstantiation_genericName_setter(instance):
    original = instance.genericName
    instance.genericName = original
    assert instance.genericName == original

@given(instance=adb::GenericInstantiation_strategy)
def test_adb::genericinstantiation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::GenericInstantiation_strategy)
def test_adb::genericinstantiation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::LibrarySpecification_strategy)
@settings(max_examples=50)
def test_adb::libraryspecification_instantiation(instance):
    assert isinstance(instance, adb::LibrarySpecification)

@given(instance=adb::GenericItems_strategy)
@settings(max_examples=50)
def test_adb::genericitems_instantiation(instance):
    assert isinstance(instance, adb::GenericItems)

@given(instance=adb::GenericDeclaration_strategy)
@settings(max_examples=50)
def test_adb::genericdeclaration_instantiation(instance):
    assert isinstance(instance, adb::GenericDeclaration)

@given(instance=UseClause_strategy)
@settings(max_examples=50)
def test_useclause_instantiation(instance):
    assert isinstance(instance, UseClause)

@given(instance=adb::UseTypeClause_strategy)
@settings(max_examples=50)
def test_adb::usetypeclause_instantiation(instance):
    assert isinstance(instance, adb::UseTypeClause)

@given(instance=adb::UseTypeClause_strategy)
def test_adb::usetypeclause_typesNames_type(instance):
    assert isinstance(instance.typesNames, str)


@given(instance=adb::UseTypeClause_strategy)
def test_adb::usetypeclause_typesNames_setter(instance):
    original = instance.typesNames
    instance.typesNames = original
    assert instance.typesNames == original

@given(instance=adb::UseTypeClause_strategy)
def test_adb::usetypeclause_useTypeRefs_type(instance):
    assert isinstance(instance.useTypeRefs, str)


@given(instance=adb::UseTypeClause_strategy)
def test_adb::usetypeclause_useTypeRefs_setter(instance):
    original = instance.useTypeRefs
    instance.useTypeRefs = original
    assert instance.useTypeRefs == original

@given(instance=adb::UsePackageClause_strategy)
@settings(max_examples=50)
def test_adb::usepackageclause_instantiation(instance):
    assert isinstance(instance, adb::UsePackageClause)

@given(instance=GenericItem_strategy)
@settings(max_examples=50)
def test_genericitem_instantiation(instance):
    assert isinstance(instance, GenericItem)

@given(instance=adb::GenericFormalParameterDeclaration_strategy)
@settings(max_examples=50)
def test_adb::genericformalparameterdeclaration_instantiation(instance):
    assert isinstance(instance, adb::GenericFormalParameterDeclaration)

@given(instance=BasicDeclarativeItem_strategy)
@settings(max_examples=50)
def test_basicdeclarativeitem_instantiation(instance):
    assert isinstance(instance, BasicDeclarativeItem)

@given(instance=adb::AspectClause_strategy)
@settings(max_examples=50)
def test_adb::aspectclause_instantiation(instance):
    assert isinstance(instance, adb::AspectClause)

@given(instance=adb::AspectClause_strategy)
def test_adb::aspectclause_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::AspectClause_strategy)
def test_adb::aspectclause_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::BasicDeclaration_strategy)
@settings(max_examples=50)
def test_adb::basicdeclaration_instantiation(instance):
    assert isinstance(instance, adb::BasicDeclaration)

@given(instance=adb::LibraryUnitDeclaration_strategy)
@settings(max_examples=50)
def test_adb::libraryunitdeclaration_instantiation(instance):
    assert isinstance(instance, adb::LibraryUnitDeclaration)

@given(instance=adb::LibraryUnitDeclaration_strategy)
def test_adb::libraryunitdeclaration_private_type(instance):
    assert isinstance(instance.private, bool)


@given(instance=adb::LibraryUnitDeclaration_strategy)
def test_adb::libraryunitdeclaration_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=ContextItem_strategy)
@settings(max_examples=50)
def test_contextitem_instantiation(instance):
    assert isinstance(instance, ContextItem)

@given(instance=adb::UseClause_strategy)
@settings(max_examples=50)
def test_adb::useclause_instantiation(instance):
    assert isinstance(instance, adb::UseClause)

@given(instance=adb::WithClause_strategy)
@settings(max_examples=50)
def test_adb::withclause_instantiation(instance):
    assert isinstance(instance, adb::WithClause)

@given(instance=adb::WithClause_strategy)
def test_adb::withclause_limited_type(instance):
    assert isinstance(instance.limited, bool)


@given(instance=adb::WithClause_strategy)
def test_adb::withclause_limited_setter(instance):
    original = instance.limited
    instance.limited = original
    assert instance.limited == original

@given(instance=adb::WithClause_strategy)
def test_adb::withclause_private_type(instance):
    assert isinstance(instance.private, bool)


@given(instance=adb::WithClause_strategy)
def test_adb::withclause_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=adb::ContextItem_strategy)
@settings(max_examples=50)
def test_adb::contextitem_instantiation(instance):
    assert isinstance(instance, adb::ContextItem)

@given(instance=adb::Pragma_strategy)
@settings(max_examples=50)
def test_adb::pragma_instantiation(instance):
    assert isinstance(instance, adb::Pragma)

@given(instance=adb::Pragma_strategy)
def test_adb::pragma_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=adb::Pragma_strategy)
def test_adb::pragma_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=adb::Unit_strategy)
@settings(max_examples=50)
def test_adb::unit_instantiation(instance):
    assert isinstance(instance, adb::Unit)

@given(instance=adb::ContextClause_strategy)
@settings(max_examples=50)
def test_adb::contextclause_instantiation(instance):
    assert isinstance(instance, adb::ContextClause)

@given(instance=adb::CompilationUnit_strategy)
@settings(max_examples=50)
def test_adb::compilationunit_instantiation(instance):
    assert isinstance(instance, adb::CompilationUnit)

@given(instance=adb::Compilation_strategy)
@settings(max_examples=50)
def test_adb::compilation_instantiation(instance):
    assert isinstance(instance, adb::Compilation)
