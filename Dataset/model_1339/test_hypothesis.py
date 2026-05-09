import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mutatorenvironment::miniOCL::NavigationPathCS,
    NavigationPathCS,
    mutatorenvironment::miniOCL::NavigationPathElementCS,
    mutatorenvironment::miniOCL::NavigationPathVariableCS,
    mutatorenvironment::miniOCL::NavigationPathNameCS,
    NavigationPathNameCS,
    mutatorenvironment::miniOCL::IteratorVarCS,
    LoopExpCS,
    mutatorenvironment::miniOCL::ForAllExpCS,
    mutatorenvironment::miniOCL::IterateExpCS,
    mutatorenvironment::miniOCL::CollectExpCS,
    IteratorVarCS,
    mutatorenvironment::miniOCL::ExistsExpCS,
    BooleanLiteralExpCS,
    mutatorenvironment::miniOCL::BooleanExpCS,
    miniOCL::mutatorenvironment::EStructuralFeature,
    mutatorenvironment::miniOCL::PathCS,
    PathCS,
    mutatorenvironment::miniOCL::PathElementCS,
    mutatorenvironment::miniOCL::PathVariableCS,
    mutatorenvironment::miniOCL::PathNameCS,
    LiteralExpCS,
    mutatorenvironment::miniOCL::StringLiteralExpCS,
    mutatorenvironment::miniOCL::BooleanLiteralExpCS,
    mutatorenvironment::miniOCL::IntLiteralExpCS,
    mutatorenvironment::miniOCL::RoundedBracketClauseCS,
    mutatorenvironment::miniOCL::AccVarCS,
    AccVarCS,
    ExpCS,
    ParameterCS,
    mutatorenvironment::miniOCL::OperationCS,
    mutatorenvironment::miniOCL::PropertyCS,
    OperationCS,
    PropertyCS,
    RoundedBracketClauseCS,
    PrimaryExpCS,
    mutatorenvironment::miniOCL::LiteralExpCS,
    mutatorenvironment::miniOCL::NavigationExpCS,
    NavigationExpCS,
    mutatorenvironment::miniOCL::LoopExpCS,
    mutatorenvironment::miniOCL::NameExpCS,
    mutatorenvironment::miniOCL::NavigationNameExpCS,
    CallExpCS,
    mutatorenvironment::miniOCL::PrimaryExpCS,
    LogicExpCS,
    mutatorenvironment::miniOCL::CallExpCS,
    mutatorenvironment::miniOCL::LogicExpCS,
    mutatorenvironment::miniOCL::ExpCS,
    mutatorenvironment::miniOCL::InvariantCS,
    mutatorenvironment::miniOCL::ConstraintCS,
    mutatorenvironment::miniOCL::ParameterCS,
    mutatorenvironment::EStructuralFeature,
    PathNameCS,
    mutatorenvironment::miniOCL::ClassCS,
    ClassCS,
    mutatorenvironment::miniOCL::PackageCS,
    ConstraintCS,
    PackageCS,
    mutatorenvironment::miniOCL::RootCS,
    mutatorenvironment::EObject,
    RandomNumberType,
    mutatorenvironment::RandomIntegerNumberType,
    mutatorenvironment::RandomDoubleNumberType,
    mutatorenvironment::BinaryOperator,
    InvariantCS,
    ReferenceSet,
    mutatorenvironment::ReferenceAtt,
    mutatorenvironment::ReferenceRemove,
    mutatorenvironment::ReferenceSwap,
    mutatorenvironment::ReferenceAdd,
    mutatorenvironment::ReferenceInit,
    mutatorenvironment::AttributeEvaluationType,
    Evaluation,
    mutatorenvironment::AttributeEvaluation,
    mutatorenvironment::Evaluation,
    mutatorenvironment::ReferenceEvaluation,
    mutatorenvironment::EAttribute,
    OtherSelection,
    mutatorenvironment::OtherTypeSelection,
    CompleteSelection,
    mutatorenvironment::CompleteTypeSelection,
    RemoveReferenceMutator,
    mutatorenvironment::RemoveSpecificReferenceMutator,
    mutatorenvironment::RemoveCompleteReferenceMutator,
    mutatorenvironment::RemoveRandomReferenceMutator,
    BooleanType,
    mutatorenvironment::RandomBooleanType,
    mutatorenvironment::SpecificBooleanType,
    AttributeType,
    mutatorenvironment::ListType,
    mutatorenvironment::StringType,
    mutatorenvironment::RandomType,
    mutatorenvironment::ListStringType,
    mutatorenvironment::NumberType,
    mutatorenvironment::BooleanType,
    AttributeEvaluationType,
    mutatorenvironment::ObjectAttributeType,
    mutatorenvironment::AttributeType,
    AttributeSet,
    mutatorenvironment::AttributeUnset,
    mutatorenvironment::AttributeSwap,
    mutatorenvironment::AttributeOperation,
    mutatorenvironment::AttributeCopy,
    mutatorenvironment::AttributeReverse,
    mutatorenvironment::AttributeScalar,
    SpecificSelection,
    mutatorenvironment::SpecificClosureSelection,
    mutatorenvironment::SpecificObjectSelection,
    RandomSelection,
    mutatorenvironment::RandomTypeSelection,
    mutatorenvironment::SpecificReferenceSelection,
    DoubleType,
    mutatorenvironment::RandomDoubleType,
    mutatorenvironment::SpecificDoubleType,
    IntegerType,
    mutatorenvironment::RandomIntegerType,
    mutatorenvironment::SpecificIntegerType,
    NumberType,
    mutatorenvironment::MinValueType,
    mutatorenvironment::RandomNumberType,
    mutatorenvironment::DoubleType,
    mutatorenvironment::MaxValueType,
    mutatorenvironment::IntegerType,
    StringType,
    mutatorenvironment::ReplaceStringType,
    mutatorenvironment::RandomStringNumberType,
    mutatorenvironment::CatEndStringType,
    mutatorenvironment::CatStartStringType,
    mutatorenvironment::UpperStringType,
    mutatorenvironment::RandomStringType,
    mutatorenvironment::LowerStringType,
    mutatorenvironment::SpecificStringType,
    mutatorenvironment::ObjectEmitter,
    mutatorenvironment::Source,
    Definition,
    mutatorenvironment::Program,
    mutatorenvironment::Resource,
    mutatorenvironment::Library,
    mutatorenvironment::Constraint,
    mutatorenvironment::Block,
    ObSelectionStrategy,
    mutatorenvironment::CompleteSelection,
    mutatorenvironment::TypedSelection,
    mutatorenvironment::SpecificSelection,
    mutatorenvironment::OtherSelection,
    mutatorenvironment::RandomSelection,
    mutatorenvironment::Expression,
    mutatorenvironment::EReference,
    mutatorenvironment::ReferenceSet,
    mutatorenvironment::AttributeSet,
    Mutator,
    mutatorenvironment::ModifyTargetReferenceMutator,
    mutatorenvironment::ModifySourceReferenceMutator,
    mutatorenvironment::CreateReferenceMutator,
    mutatorenvironment::RemoveObjectMutator,
    mutatorenvironment::RetypeObjectMutator,
    mutatorenvironment::SelectObjectMutator,
    mutatorenvironment::CreateObjectMutator,
    mutatorenvironment::ModifyInformationMutator,
    mutatorenvironment::CloneObjectMutator,
    mutatorenvironment::RemoveReferenceMutator,
    mutatorenvironment::SelectSampleMutator,
    mutatorenvironment::CompositeMutator,
    ObjectEmitter,
    mutatorenvironment::ObSelectionStrategy,
    mutatorenvironment::EClass,
    mutatorenvironment::Load,
    mutatorenvironment::Mutator,
    mutatorenvironment::Definition,
    mutatorenvironment::MutatorEnvironment,
    LogicOperator,
    ArithmeticOperator,
    SampleClause,
    Repeat,
    Operator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mutatorenvironment::miniocl::navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationPathCS)


def test_mutatorenvironment::miniocl::navigationpathcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationPathCS.__init__)


def test_mutatorenvironment::miniocl::navigationpathcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationPathElementCS)


def test_mutatorenvironment::miniocl::navigationpathelementcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationPathElementCS.__init__)


def test_mutatorenvironment::miniocl::navigationpathelementcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationPathVariableCS)


def test_mutatorenvironment::miniocl::navigationpathvariablecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationPathVariableCS.__init__)


def test_mutatorenvironment::miniocl::navigationpathvariablecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_mutatorenvironment::miniocl::navigationpathvariablecs_has_varName():
    assert hasattr(mutatorenvironment::miniOCL::NavigationPathVariableCS, "varName")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::NavigationPathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationPathNameCS)


def test_mutatorenvironment::miniocl::navigationpathnamecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationPathNameCS.__init__)


def test_mutatorenvironment::miniocl::navigationpathnamecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathNameCS)


def test_navigationpathnamecs_constructor_exists():
    assert callable(NavigationPathNameCS.__init__)


def test_navigationpathnamecs_constructor_args():
    sig = inspect.signature(NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::IteratorVarCS)


def test_mutatorenvironment::miniocl::iteratorvarcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::IteratorVarCS.__init__)


def test_mutatorenvironment::miniocl::iteratorvarcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_mutatorenvironment::miniocl::iteratorvarcs_has_itName():
    assert hasattr(mutatorenvironment::miniOCL::IteratorVarCS, "itName")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::forallexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ForAllExpCS)


def test_mutatorenvironment::miniocl::forallexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ForAllExpCS.__init__)


def test_mutatorenvironment::miniocl::forallexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::IterateExpCS)


def test_mutatorenvironment::miniocl::iterateexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::IterateExpCS.__init__)


def test_mutatorenvironment::miniocl::iterateexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::collectexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::CollectExpCS)


def test_mutatorenvironment::miniocl::collectexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::CollectExpCS.__init__)


def test_mutatorenvironment::miniocl::collectexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(IteratorVarCS)


def test_iteratorvarcs_constructor_exists():
    assert callable(IteratorVarCS.__init__)


def test_iteratorvarcs_constructor_args():
    sig = inspect.signature(IteratorVarCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::existsexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ExistsExpCS)


def test_mutatorenvironment::miniocl::existsexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ExistsExpCS.__init__)


def test_mutatorenvironment::miniocl::existsexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::BooleanExpCS)


def test_mutatorenvironment::miniocl::booleanexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::BooleanExpCS.__init__)


def test_mutatorenvironment::miniocl::booleanexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_mutatorenvironment::miniocl::booleanexpcs_has_boolSymbol():
    assert hasattr(mutatorenvironment::miniOCL::BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::mutatorenvironment::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(miniOCL::mutatorenvironment::EStructuralFeature)


def test_miniocl::mutatorenvironment::estructuralfeature_constructor_exists():
    assert callable(miniOCL::mutatorenvironment::EStructuralFeature.__init__)


def test_miniocl::mutatorenvironment::estructuralfeature_constructor_args():
    sig = inspect.signature(miniOCL::mutatorenvironment::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::pathcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PathCS)


def test_mutatorenvironment::miniocl::pathcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PathCS.__init__)


def test_mutatorenvironment::miniocl::pathcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PathCS.__init__)
    params = list(sig.parameters.keys())



def test_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PathElementCS)


def test_mutatorenvironment::miniocl::pathelementcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PathElementCS.__init__)


def test_mutatorenvironment::miniocl::pathelementcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PathVariableCS)


def test_mutatorenvironment::miniocl::pathvariablecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PathVariableCS.__init__)


def test_mutatorenvironment::miniocl::pathvariablecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_mutatorenvironment::miniocl::pathvariablecs_has_varName():
    assert hasattr(mutatorenvironment::miniOCL::PathVariableCS, "varName")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::PathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PathNameCS)


def test_mutatorenvironment::miniocl::pathnamecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PathNameCS.__init__)


def test_mutatorenvironment::miniocl::pathnamecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::StringLiteralExpCS)


def test_mutatorenvironment::miniocl::stringliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::StringLiteralExpCS.__init__)


def test_mutatorenvironment::miniocl::stringliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_mutatorenvironment::miniocl::stringliteralexpcs_has_stringSymbol():
    assert hasattr(mutatorenvironment::miniOCL::StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::BooleanLiteralExpCS)


def test_mutatorenvironment::miniocl::booleanliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::BooleanLiteralExpCS.__init__)


def test_mutatorenvironment::miniocl::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::IntLiteralExpCS)


def test_mutatorenvironment::miniocl::intliteralexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::IntLiteralExpCS.__init__)


def test_mutatorenvironment::miniocl::intliteralexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_mutatorenvironment::miniocl::intliteralexpcs_has_intSymbol():
    assert hasattr(mutatorenvironment::miniOCL::IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::RoundedBracketClauseCS)


def test_mutatorenvironment::miniocl::roundedbracketclausecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::RoundedBracketClauseCS.__init__)


def test_mutatorenvironment::miniocl::roundedbracketclausecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::accvarcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::AccVarCS)


def test_mutatorenvironment::miniocl::accvarcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::AccVarCS.__init__)


def test_mutatorenvironment::miniocl::accvarcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"

def test_mutatorenvironment::miniocl::accvarcs_has_accVarName():
    assert hasattr(mutatorenvironment::miniOCL::AccVarCS, "accVarName")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::AccVarCS.__mro__:
        if "accVarName" in klass.__dict__:
            descriptor = klass.__dict__["accVarName"]
            break
    assert isinstance(descriptor, property)



def test_accvarcs_is_not_abstract():
    assert not inspect.isabstract(AccVarCS)


def test_accvarcs_constructor_exists():
    assert callable(AccVarCS.__init__)


def test_accvarcs_constructor_args():
    sig = inspect.signature(AccVarCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_parametercs_is_not_abstract():
    assert not inspect.isabstract(ParameterCS)


def test_parametercs_constructor_exists():
    assert callable(ParameterCS.__init__)


def test_parametercs_constructor_args():
    sig = inspect.signature(ParameterCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::operationcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::OperationCS)


def test_mutatorenvironment::miniocl::operationcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::OperationCS.__init__)


def test_mutatorenvironment::miniocl::operationcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::miniocl::operationcs_has_name():
    assert hasattr(mutatorenvironment::miniOCL::OperationCS, "name")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::propertycs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PropertyCS)


def test_mutatorenvironment::miniocl::propertycs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PropertyCS.__init__)


def test_mutatorenvironment::miniocl::propertycs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::miniocl::propertycs_has_name():
    assert hasattr(mutatorenvironment::miniOCL::PropertyCS, "name")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_operationcs_is_not_abstract():
    assert not inspect.isabstract(OperationCS)


def test_operationcs_constructor_exists():
    assert callable(OperationCS.__init__)


def test_operationcs_constructor_args():
    sig = inspect.signature(OperationCS.__init__)
    params = list(sig.parameters.keys())



def test_propertycs_is_not_abstract():
    assert not inspect.isabstract(PropertyCS)


def test_propertycs_constructor_exists():
    assert callable(PropertyCS.__init__)


def test_propertycs_constructor_args():
    sig = inspect.signature(PropertyCS.__init__)
    params = list(sig.parameters.keys())



def test_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(RoundedBracketClauseCS)


def test_roundedbracketclausecs_constructor_exists():
    assert callable(RoundedBracketClauseCS.__init__)


def test_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::LiteralExpCS)


def test_mutatorenvironment::miniocl::literalexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::LiteralExpCS.__init__)


def test_mutatorenvironment::miniocl::literalexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationExpCS)


def test_mutatorenvironment::miniocl::navigationexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationExpCS.__init__)


def test_mutatorenvironment::miniocl::navigationexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::loopexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::LoopExpCS)


def test_mutatorenvironment::miniocl::loopexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::LoopExpCS.__init__)


def test_mutatorenvironment::miniocl::loopexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"

def test_mutatorenvironment::miniocl::loopexpcs_has_logicOp():
    assert hasattr(mutatorenvironment::miniOCL::LoopExpCS, "logicOp")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::LoopExpCS.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NameExpCS)


def test_mutatorenvironment::miniocl::nameexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NameExpCS.__init__)


def test_mutatorenvironment::miniocl::nameexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::NavigationNameExpCS)


def test_mutatorenvironment::miniocl::navigationnameexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::NavigationNameExpCS.__init__)


def test_mutatorenvironment::miniocl::navigationnameexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PrimaryExpCS)


def test_mutatorenvironment::miniocl::primaryexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PrimaryExpCS.__init__)


def test_mutatorenvironment::miniocl::primaryexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::callexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::CallExpCS)


def test_mutatorenvironment::miniocl::callexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::CallExpCS.__init__)


def test_mutatorenvironment::miniocl::callexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::logicexpcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::LogicExpCS)


def test_mutatorenvironment::miniocl::logicexpcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::LogicExpCS.__init__)


def test_mutatorenvironment::miniocl::logicexpcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mutatorenvironment::miniocl::logicexpcs_has_op():
    assert hasattr(mutatorenvironment::miniOCL::LogicExpCS, "op")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::miniocl::expcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ExpCS)


def test_mutatorenvironment::miniocl::expcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ExpCS.__init__)


def test_mutatorenvironment::miniocl::expcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::invariantcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::InvariantCS)


def test_mutatorenvironment::miniocl::invariantcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::InvariantCS.__init__)


def test_mutatorenvironment::miniocl::invariantcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::constraintcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ConstraintCS)


def test_mutatorenvironment::miniocl::constraintcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ConstraintCS.__init__)


def test_mutatorenvironment::miniocl::constraintcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::parametercs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ParameterCS)


def test_mutatorenvironment::miniocl::parametercs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ParameterCS.__init__)


def test_mutatorenvironment::miniocl::parametercs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::miniocl::parametercs_has_name():
    assert hasattr(mutatorenvironment::miniOCL::ParameterCS, "name")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::EStructuralFeature)


def test_mutatorenvironment::estructuralfeature_constructor_exists():
    assert callable(mutatorenvironment::EStructuralFeature.__init__)


def test_mutatorenvironment::estructuralfeature_constructor_args():
    sig = inspect.signature(mutatorenvironment::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::classcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::ClassCS)


def test_mutatorenvironment::miniocl::classcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::ClassCS.__init__)


def test_mutatorenvironment::miniocl::classcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::miniocl::classcs_has_name():
    assert hasattr(mutatorenvironment::miniOCL::ClassCS, "name")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_classcs_is_not_abstract():
    assert not inspect.isabstract(ClassCS)


def test_classcs_constructor_exists():
    assert callable(ClassCS.__init__)


def test_classcs_constructor_args():
    sig = inspect.signature(ClassCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::packagecs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::PackageCS)


def test_mutatorenvironment::miniocl::packagecs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::PackageCS.__init__)


def test_mutatorenvironment::miniocl::packagecs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::miniocl::packagecs_has_name():
    assert hasattr(mutatorenvironment::miniOCL::PackageCS, "name")
    descriptor = None
    for klass in mutatorenvironment::miniOCL::PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_constraintcs_is_not_abstract():
    assert not inspect.isabstract(ConstraintCS)


def test_constraintcs_constructor_exists():
    assert callable(ConstraintCS.__init__)


def test_constraintcs_constructor_args():
    sig = inspect.signature(ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_packagecs_is_not_abstract():
    assert not inspect.isabstract(PackageCS)


def test_packagecs_constructor_exists():
    assert callable(PackageCS.__init__)


def test_packagecs_constructor_args():
    sig = inspect.signature(PackageCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::miniocl::rootcs_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::miniOCL::RootCS)


def test_mutatorenvironment::miniocl::rootcs_constructor_exists():
    assert callable(mutatorenvironment::miniOCL::RootCS.__init__)


def test_mutatorenvironment::miniocl::rootcs_constructor_args():
    sig = inspect.signature(mutatorenvironment::miniOCL::RootCS.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::eobject_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::EObject)


def test_mutatorenvironment::eobject_constructor_exists():
    assert callable(mutatorenvironment::EObject.__init__)


def test_mutatorenvironment::eobject_constructor_args():
    sig = inspect.signature(mutatorenvironment::EObject.__init__)
    params = list(sig.parameters.keys())



def test_randomnumbertype_is_not_abstract():
    assert not inspect.isabstract(RandomNumberType)


def test_randomnumbertype_constructor_exists():
    assert callable(RandomNumberType.__init__)


def test_randomnumbertype_constructor_args():
    sig = inspect.signature(RandomNumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomintegernumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomIntegerNumberType)


def test_mutatorenvironment::randomintegernumbertype_constructor_exists():
    assert callable(mutatorenvironment::RandomIntegerNumberType.__init__)


def test_mutatorenvironment::randomintegernumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomIntegerNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"

def test_mutatorenvironment::randomintegernumbertype_has_min():
    assert hasattr(mutatorenvironment::RandomIntegerNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomIntegerNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::randomdoublenumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomDoubleNumberType)


def test_mutatorenvironment::randomdoublenumbertype_constructor_exists():
    assert callable(mutatorenvironment::RandomDoubleNumberType.__init__)


def test_mutatorenvironment::randomdoublenumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomDoubleNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"

def test_mutatorenvironment::randomdoublenumbertype_has_min():
    assert hasattr(mutatorenvironment::RandomDoubleNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomDoubleNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::BinaryOperator)


def test_mutatorenvironment::binaryoperator_constructor_exists():
    assert callable(mutatorenvironment::BinaryOperator.__init__)


def test_mutatorenvironment::binaryoperator_constructor_args():
    sig = inspect.signature(mutatorenvironment::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_mutatorenvironment::binaryoperator_has_type():
    assert hasattr(mutatorenvironment::BinaryOperator, "type")
    descriptor = None
    for klass in mutatorenvironment::BinaryOperator.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_invariantcs_is_not_abstract():
    assert not inspect.isabstract(InvariantCS)


def test_invariantcs_constructor_exists():
    assert callable(InvariantCS.__init__)


def test_invariantcs_constructor_args():
    sig = inspect.signature(InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_referenceset_is_not_abstract():
    assert not inspect.isabstract(ReferenceSet)


def test_referenceset_constructor_exists():
    assert callable(ReferenceSet.__init__)


def test_referenceset_constructor_args():
    sig = inspect.signature(ReferenceSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceatt_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceAtt)


def test_mutatorenvironment::referenceatt_constructor_exists():
    assert callable(mutatorenvironment::ReferenceAtt.__init__)


def test_mutatorenvironment::referenceatt_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceAtt.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceremove_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceRemove)


def test_mutatorenvironment::referenceremove_constructor_exists():
    assert callable(mutatorenvironment::ReferenceRemove.__init__)


def test_mutatorenvironment::referenceremove_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceRemove.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceswap_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceSwap)


def test_mutatorenvironment::referenceswap_constructor_exists():
    assert callable(mutatorenvironment::ReferenceSwap.__init__)


def test_mutatorenvironment::referenceswap_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceSwap.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceadd_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceAdd)


def test_mutatorenvironment::referenceadd_constructor_exists():
    assert callable(mutatorenvironment::ReferenceAdd.__init__)


def test_mutatorenvironment::referenceadd_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceAdd.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceinit_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceInit)


def test_mutatorenvironment::referenceinit_constructor_exists():
    assert callable(mutatorenvironment::ReferenceInit.__init__)


def test_mutatorenvironment::referenceinit_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceInit.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeevaluationtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeEvaluationType)


def test_mutatorenvironment::attributeevaluationtype_constructor_exists():
    assert callable(mutatorenvironment::AttributeEvaluationType.__init__)


def test_mutatorenvironment::attributeevaluationtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeEvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_evaluation_is_not_abstract():
    assert not inspect.isabstract(Evaluation)


def test_evaluation_constructor_exists():
    assert callable(Evaluation.__init__)


def test_evaluation_constructor_args():
    sig = inspect.signature(Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeevaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeEvaluation)


def test_mutatorenvironment::attributeevaluation_constructor_exists():
    assert callable(mutatorenvironment::AttributeEvaluation.__init__)


def test_mutatorenvironment::attributeevaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::evaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Evaluation)


def test_mutatorenvironment::evaluation_constructor_exists():
    assert callable(mutatorenvironment::Evaluation.__init__)


def test_mutatorenvironment::evaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment::Evaluation.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceevaluation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceEvaluation)


def test_mutatorenvironment::referenceevaluation_constructor_exists():
    assert callable(mutatorenvironment::ReferenceEvaluation.__init__)


def test_mutatorenvironment::referenceevaluation_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment::referenceevaluation_has_container():
    assert hasattr(mutatorenvironment::ReferenceEvaluation, "container")
    descriptor = None
    for klass in mutatorenvironment::ReferenceEvaluation.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::referenceevaluation_has_operator():
    assert hasattr(mutatorenvironment::ReferenceEvaluation, "operator")
    descriptor = None
    for klass in mutatorenvironment::ReferenceEvaluation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::eattribute_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::EAttribute)


def test_mutatorenvironment::eattribute_constructor_exists():
    assert callable(mutatorenvironment::EAttribute.__init__)


def test_mutatorenvironment::eattribute_constructor_args():
    sig = inspect.signature(mutatorenvironment::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_otherselection_is_not_abstract():
    assert not inspect.isabstract(OtherSelection)


def test_otherselection_constructor_exists():
    assert callable(OtherSelection.__init__)


def test_otherselection_constructor_args():
    sig = inspect.signature(OtherSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::othertypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::OtherTypeSelection)


def test_mutatorenvironment::othertypeselection_constructor_exists():
    assert callable(mutatorenvironment::OtherTypeSelection.__init__)


def test_mutatorenvironment::othertypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::OtherTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_completeselection_is_not_abstract():
    assert not inspect.isabstract(CompleteSelection)


def test_completeselection_constructor_exists():
    assert callable(CompleteSelection.__init__)


def test_completeselection_constructor_args():
    sig = inspect.signature(CompleteSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::completetypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CompleteTypeSelection)


def test_mutatorenvironment::completetypeselection_constructor_exists():
    assert callable(mutatorenvironment::CompleteTypeSelection.__init__)


def test_mutatorenvironment::completetypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::CompleteTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_removereferencemutator_is_not_abstract():
    assert not inspect.isabstract(RemoveReferenceMutator)


def test_removereferencemutator_constructor_exists():
    assert callable(RemoveReferenceMutator.__init__)


def test_removereferencemutator_constructor_args():
    sig = inspect.signature(RemoveReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::removespecificreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RemoveSpecificReferenceMutator)


def test_mutatorenvironment::removespecificreferencemutator_constructor_exists():
    assert callable(mutatorenvironment::RemoveSpecificReferenceMutator.__init__)


def test_mutatorenvironment::removespecificreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RemoveSpecificReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::removecompletereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RemoveCompleteReferenceMutator)


def test_mutatorenvironment::removecompletereferencemutator_constructor_exists():
    assert callable(mutatorenvironment::RemoveCompleteReferenceMutator.__init__)


def test_mutatorenvironment::removecompletereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RemoveCompleteReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::removerandomreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RemoveRandomReferenceMutator)


def test_mutatorenvironment::removerandomreferencemutator_constructor_exists():
    assert callable(mutatorenvironment::RemoveRandomReferenceMutator.__init__)


def test_mutatorenvironment::removerandomreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RemoveRandomReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_booleantype_is_not_abstract():
    assert not inspect.isabstract(BooleanType)


def test_booleantype_constructor_exists():
    assert callable(BooleanType.__init__)


def test_booleantype_constructor_args():
    sig = inspect.signature(BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randombooleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomBooleanType)


def test_mutatorenvironment::randombooleantype_constructor_exists():
    assert callable(mutatorenvironment::RandomBooleanType.__init__)


def test_mutatorenvironment::randombooleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomBooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment::randombooleantype_has_allowsNull():
    assert hasattr(mutatorenvironment::RandomBooleanType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment::RandomBooleanType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::specificbooleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificBooleanType)


def test_mutatorenvironment::specificbooleantype_constructor_exists():
    assert callable(mutatorenvironment::SpecificBooleanType.__init__)


def test_mutatorenvironment::specificbooleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificBooleanType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::specificbooleantype_has_value():
    assert hasattr(mutatorenvironment::SpecificBooleanType, "value")
    descriptor = None
    for klass in mutatorenvironment::SpecificBooleanType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_attributetype_is_not_abstract():
    assert not inspect.isabstract(AttributeType)


def test_attributetype_constructor_exists():
    assert callable(AttributeType.__init__)


def test_attributetype_constructor_args():
    sig = inspect.signature(AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::listtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ListType)


def test_mutatorenvironment::listtype_constructor_exists():
    assert callable(mutatorenvironment::ListType.__init__)


def test_mutatorenvironment::listtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::ListType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::stringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::StringType)


def test_mutatorenvironment::stringtype_constructor_exists():
    assert callable(mutatorenvironment::StringType.__init__)


def test_mutatorenvironment::stringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::StringType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomType)


def test_mutatorenvironment::randomtype_constructor_exists():
    assert callable(mutatorenvironment::RandomType.__init__)


def test_mutatorenvironment::randomtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::liststringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ListStringType)


def test_mutatorenvironment::liststringtype_constructor_exists():
    assert callable(mutatorenvironment::ListStringType.__init__)


def test_mutatorenvironment::liststringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::ListStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::liststringtype_has_value():
    assert hasattr(mutatorenvironment::ListStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::ListStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::numbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::NumberType)


def test_mutatorenvironment::numbertype_constructor_exists():
    assert callable(mutatorenvironment::NumberType.__init__)


def test_mutatorenvironment::numbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::NumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::booleantype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::BooleanType)


def test_mutatorenvironment::booleantype_constructor_exists():
    assert callable(mutatorenvironment::BooleanType.__init__)


def test_mutatorenvironment::booleantype_constructor_args():
    sig = inspect.signature(mutatorenvironment::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_attributeevaluationtype_is_not_abstract():
    assert not inspect.isabstract(AttributeEvaluationType)


def test_attributeevaluationtype_constructor_exists():
    assert callable(AttributeEvaluationType.__init__)


def test_attributeevaluationtype_constructor_args():
    sig = inspect.signature(AttributeEvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::objectattributetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ObjectAttributeType)


def test_mutatorenvironment::objectattributetype_constructor_exists():
    assert callable(mutatorenvironment::ObjectAttributeType.__init__)


def test_mutatorenvironment::objectattributetype_constructor_args():
    sig = inspect.signature(mutatorenvironment::ObjectAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment::objectattributetype_has_operator():
    assert hasattr(mutatorenvironment::ObjectAttributeType, "operator")
    descriptor = None
    for klass in mutatorenvironment::ObjectAttributeType.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::attributetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeType)


def test_mutatorenvironment::attributetype_constructor_exists():
    assert callable(mutatorenvironment::AttributeType.__init__)


def test_mutatorenvironment::attributetype_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment::attributetype_has_operator():
    assert hasattr(mutatorenvironment::AttributeType, "operator")
    descriptor = None
    for klass in mutatorenvironment::AttributeType.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_attributeset_is_not_abstract():
    assert not inspect.isabstract(AttributeSet)


def test_attributeset_constructor_exists():
    assert callable(AttributeSet.__init__)


def test_attributeset_constructor_args():
    sig = inspect.signature(AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeunset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeUnset)


def test_mutatorenvironment::attributeunset_constructor_exists():
    assert callable(mutatorenvironment::AttributeUnset.__init__)


def test_mutatorenvironment::attributeunset_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeUnset.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeswap_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeSwap)


def test_mutatorenvironment::attributeswap_constructor_exists():
    assert callable(mutatorenvironment::AttributeSwap.__init__)


def test_mutatorenvironment::attributeswap_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeSwap.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeoperation_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeOperation)


def test_mutatorenvironment::attributeoperation_constructor_exists():
    assert callable(mutatorenvironment::AttributeOperation.__init__)


def test_mutatorenvironment::attributeoperation_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_mutatorenvironment::attributeoperation_has_operator():
    assert hasattr(mutatorenvironment::AttributeOperation, "operator")
    descriptor = None
    for klass in mutatorenvironment::AttributeOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::attributecopy_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeCopy)


def test_mutatorenvironment::attributecopy_constructor_exists():
    assert callable(mutatorenvironment::AttributeCopy.__init__)


def test_mutatorenvironment::attributecopy_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeCopy.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributereverse_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeReverse)


def test_mutatorenvironment::attributereverse_constructor_exists():
    assert callable(mutatorenvironment::AttributeReverse.__init__)


def test_mutatorenvironment::attributereverse_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeReverse.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributescalar_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeScalar)


def test_mutatorenvironment::attributescalar_constructor_exists():
    assert callable(mutatorenvironment::AttributeScalar.__init__)


def test_mutatorenvironment::attributescalar_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeScalar.__init__)
    params = list(sig.parameters.keys())



def test_specificselection_is_not_abstract():
    assert not inspect.isabstract(SpecificSelection)


def test_specificselection_constructor_exists():
    assert callable(SpecificSelection.__init__)


def test_specificselection_constructor_args():
    sig = inspect.signature(SpecificSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::specificclosureselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificClosureSelection)


def test_mutatorenvironment::specificclosureselection_constructor_exists():
    assert callable(mutatorenvironment::SpecificClosureSelection.__init__)


def test_mutatorenvironment::specificclosureselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificClosureSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::specificobjectselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificObjectSelection)


def test_mutatorenvironment::specificobjectselection_constructor_exists():
    assert callable(mutatorenvironment::SpecificObjectSelection.__init__)


def test_mutatorenvironment::specificobjectselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificObjectSelection.__init__)
    params = list(sig.parameters.keys())



def test_randomselection_is_not_abstract():
    assert not inspect.isabstract(RandomSelection)


def test_randomselection_constructor_exists():
    assert callable(RandomSelection.__init__)


def test_randomselection_constructor_args():
    sig = inspect.signature(RandomSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomtypeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomTypeSelection)


def test_mutatorenvironment::randomtypeselection_constructor_exists():
    assert callable(mutatorenvironment::RandomTypeSelection.__init__)


def test_mutatorenvironment::randomtypeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomTypeSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::specificreferenceselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificReferenceSelection)


def test_mutatorenvironment::specificreferenceselection_constructor_exists():
    assert callable(mutatorenvironment::SpecificReferenceSelection.__init__)


def test_mutatorenvironment::specificreferenceselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificReferenceSelection.__init__)
    params = list(sig.parameters.keys())



def test_doubletype_is_not_abstract():
    assert not inspect.isabstract(DoubleType)


def test_doubletype_constructor_exists():
    assert callable(DoubleType.__init__)


def test_doubletype_constructor_args():
    sig = inspect.signature(DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomdoubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomDoubleType)


def test_mutatorenvironment::randomdoubletype_constructor_exists():
    assert callable(mutatorenvironment::RandomDoubleType.__init__)


def test_mutatorenvironment::randomdoubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomDoubleType.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment::randomdoubletype_has_min():
    assert hasattr(mutatorenvironment::RandomDoubleType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomDoubleType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomdoubletype_has_max():
    assert hasattr(mutatorenvironment::RandomDoubleType, "max")
    descriptor = None
    for klass in mutatorenvironment::RandomDoubleType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomdoubletype_has_allowsNull():
    assert hasattr(mutatorenvironment::RandomDoubleType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment::RandomDoubleType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::specificdoubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificDoubleType)


def test_mutatorenvironment::specificdoubletype_constructor_exists():
    assert callable(mutatorenvironment::SpecificDoubleType.__init__)


def test_mutatorenvironment::specificdoubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificDoubleType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::specificdoubletype_has_value():
    assert hasattr(mutatorenvironment::SpecificDoubleType, "value")
    descriptor = None
    for klass in mutatorenvironment::SpecificDoubleType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomintegertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomIntegerType)


def test_mutatorenvironment::randomintegertype_constructor_exists():
    assert callable(mutatorenvironment::RandomIntegerType.__init__)


def test_mutatorenvironment::randomintegertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomIntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment::randomintegertype_has_max():
    assert hasattr(mutatorenvironment::RandomIntegerType, "max")
    descriptor = None
    for klass in mutatorenvironment::RandomIntegerType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomintegertype_has_min():
    assert hasattr(mutatorenvironment::RandomIntegerType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomIntegerType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomintegertype_has_allowsNull():
    assert hasattr(mutatorenvironment::RandomIntegerType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment::RandomIntegerType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::specificintegertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificIntegerType)


def test_mutatorenvironment::specificintegertype_constructor_exists():
    assert callable(mutatorenvironment::SpecificIntegerType.__init__)


def test_mutatorenvironment::specificintegertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificIntegerType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::specificintegertype_has_value():
    assert hasattr(mutatorenvironment::SpecificIntegerType, "value")
    descriptor = None
    for klass in mutatorenvironment::SpecificIntegerType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numbertype_is_not_abstract():
    assert not inspect.isabstract(NumberType)


def test_numbertype_constructor_exists():
    assert callable(NumberType.__init__)


def test_numbertype_constructor_args():
    sig = inspect.signature(NumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::minvaluetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::MinValueType)


def test_mutatorenvironment::minvaluetype_constructor_exists():
    assert callable(mutatorenvironment::MinValueType.__init__)


def test_mutatorenvironment::minvaluetype_constructor_args():
    sig = inspect.signature(mutatorenvironment::MinValueType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomnumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomNumberType)


def test_mutatorenvironment::randomnumbertype_constructor_exists():
    assert callable(mutatorenvironment::RandomNumberType.__init__)


def test_mutatorenvironment::randomnumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomNumberType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::doubletype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::DoubleType)


def test_mutatorenvironment::doubletype_constructor_exists():
    assert callable(mutatorenvironment::DoubleType.__init__)


def test_mutatorenvironment::doubletype_constructor_args():
    sig = inspect.signature(mutatorenvironment::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::maxvaluetype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::MaxValueType)


def test_mutatorenvironment::maxvaluetype_constructor_exists():
    assert callable(mutatorenvironment::MaxValueType.__init__)


def test_mutatorenvironment::maxvaluetype_constructor_args():
    sig = inspect.signature(mutatorenvironment::MaxValueType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::integertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::IntegerType)


def test_mutatorenvironment::integertype_constructor_exists():
    assert callable(mutatorenvironment::IntegerType.__init__)


def test_mutatorenvironment::integertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_stringtype_is_not_abstract():
    assert not inspect.isabstract(StringType)


def test_stringtype_constructor_exists():
    assert callable(StringType.__init__)


def test_stringtype_constructor_args():
    sig = inspect.signature(StringType.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::replacestringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReplaceStringType)


def test_mutatorenvironment::replacestringtype_constructor_exists():
    assert callable(mutatorenvironment::ReplaceStringType.__init__)


def test_mutatorenvironment::replacestringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReplaceStringType.__init__)
    params = list(sig.parameters.keys())
    assert "oldstring" in params, "Missing parameter 'oldstring'"
    assert "newstring" in params, "Missing parameter 'newstring'"

def test_mutatorenvironment::replacestringtype_has_oldstring():
    assert hasattr(mutatorenvironment::ReplaceStringType, "oldstring")
    descriptor = None
    for klass in mutatorenvironment::ReplaceStringType.__mro__:
        if "oldstring" in klass.__dict__:
            descriptor = klass.__dict__["oldstring"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::replacestringtype_has_newstring():
    assert hasattr(mutatorenvironment::ReplaceStringType, "newstring")
    descriptor = None
    for klass in mutatorenvironment::ReplaceStringType.__mro__:
        if "newstring" in klass.__dict__:
            descriptor = klass.__dict__["newstring"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::randomstringnumbertype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomStringNumberType)


def test_mutatorenvironment::randomstringnumbertype_constructor_exists():
    assert callable(mutatorenvironment::RandomStringNumberType.__init__)


def test_mutatorenvironment::randomstringnumbertype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomStringNumberType.__init__)
    params = list(sig.parameters.keys())
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_mutatorenvironment::randomstringnumbertype_has_allowsNull():
    assert hasattr(mutatorenvironment::RandomStringNumberType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment::RandomStringNumberType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomstringnumbertype_has_min():
    assert hasattr(mutatorenvironment::RandomStringNumberType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomStringNumberType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomstringnumbertype_has_max():
    assert hasattr(mutatorenvironment::RandomStringNumberType, "max")
    descriptor = None
    for klass in mutatorenvironment::RandomStringNumberType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::catendstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CatEndStringType)


def test_mutatorenvironment::catendstringtype_constructor_exists():
    assert callable(mutatorenvironment::CatEndStringType.__init__)


def test_mutatorenvironment::catendstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::CatEndStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::catendstringtype_has_value():
    assert hasattr(mutatorenvironment::CatEndStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::CatEndStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::catstartstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CatStartStringType)


def test_mutatorenvironment::catstartstringtype_constructor_exists():
    assert callable(mutatorenvironment::CatStartStringType.__init__)


def test_mutatorenvironment::catstartstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::CatStartStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::catstartstringtype_has_value():
    assert hasattr(mutatorenvironment::CatStartStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::CatStartStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::upperstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::UpperStringType)


def test_mutatorenvironment::upperstringtype_constructor_exists():
    assert callable(mutatorenvironment::UpperStringType.__init__)


def test_mutatorenvironment::upperstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::UpperStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::upperstringtype_has_value():
    assert hasattr(mutatorenvironment::UpperStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::UpperStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::randomstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomStringType)


def test_mutatorenvironment::randomstringtype_constructor_exists():
    assert callable(mutatorenvironment::RandomStringType.__init__)


def test_mutatorenvironment::randomstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomStringType.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "allowsNull" in params, "Missing parameter 'allowsNull'"

def test_mutatorenvironment::randomstringtype_has_max():
    assert hasattr(mutatorenvironment::RandomStringType, "max")
    descriptor = None
    for klass in mutatorenvironment::RandomStringType.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomstringtype_has_min():
    assert hasattr(mutatorenvironment::RandomStringType, "min")
    descriptor = None
    for klass in mutatorenvironment::RandomStringType.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::randomstringtype_has_allowsNull():
    assert hasattr(mutatorenvironment::RandomStringType, "allowsNull")
    descriptor = None
    for klass in mutatorenvironment::RandomStringType.__mro__:
        if "allowsNull" in klass.__dict__:
            descriptor = klass.__dict__["allowsNull"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::lowerstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::LowerStringType)


def test_mutatorenvironment::lowerstringtype_constructor_exists():
    assert callable(mutatorenvironment::LowerStringType.__init__)


def test_mutatorenvironment::lowerstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::LowerStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::lowerstringtype_has_value():
    assert hasattr(mutatorenvironment::LowerStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::LowerStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::specificstringtype_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificStringType)


def test_mutatorenvironment::specificstringtype_constructor_exists():
    assert callable(mutatorenvironment::SpecificStringType.__init__)


def test_mutatorenvironment::specificstringtype_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificStringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mutatorenvironment::specificstringtype_has_value():
    assert hasattr(mutatorenvironment::SpecificStringType, "value")
    descriptor = None
    for klass in mutatorenvironment::SpecificStringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::objectemitter_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ObjectEmitter)


def test_mutatorenvironment::objectemitter_constructor_exists():
    assert callable(mutatorenvironment::ObjectEmitter.__init__)


def test_mutatorenvironment::objectemitter_constructor_args():
    sig = inspect.signature(mutatorenvironment::ObjectEmitter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::objectemitter_has_name():
    assert hasattr(mutatorenvironment::ObjectEmitter, "name")
    descriptor = None
    for klass in mutatorenvironment::ObjectEmitter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::source_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Source)


def test_mutatorenvironment::source_constructor_exists():
    assert callable(mutatorenvironment::Source.__init__)


def test_mutatorenvironment::source_constructor_args():
    sig = inspect.signature(mutatorenvironment::Source.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"

def test_mutatorenvironment::source_has_path():
    assert hasattr(mutatorenvironment::Source, "path")
    descriptor = None
    for klass in mutatorenvironment::Source.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::program_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Program)


def test_mutatorenvironment::program_constructor_exists():
    assert callable(mutatorenvironment::Program.__init__)


def test_mutatorenvironment::program_constructor_args():
    sig = inspect.signature(mutatorenvironment::Program.__init__)
    params = list(sig.parameters.keys())
    assert "exhaustive" in params, "Missing parameter 'exhaustive'"
    assert "num" in params, "Missing parameter 'num'"
    assert "description" in params, "Missing parameter 'description'"
    assert "output" in params, "Missing parameter 'output'"

def test_mutatorenvironment::program_has_exhaustive():
    assert hasattr(mutatorenvironment::Program, "exhaustive")
    descriptor = None
    for klass in mutatorenvironment::Program.__mro__:
        if "exhaustive" in klass.__dict__:
            descriptor = klass.__dict__["exhaustive"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::program_has_num():
    assert hasattr(mutatorenvironment::Program, "num")
    descriptor = None
    for klass in mutatorenvironment::Program.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::program_has_description():
    assert hasattr(mutatorenvironment::Program, "description")
    descriptor = None
    for klass in mutatorenvironment::Program.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::program_has_output():
    assert hasattr(mutatorenvironment::Program, "output")
    descriptor = None
    for klass in mutatorenvironment::Program.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::resource_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Resource)


def test_mutatorenvironment::resource_constructor_exists():
    assert callable(mutatorenvironment::Resource.__init__)


def test_mutatorenvironment::resource_constructor_args():
    sig = inspect.signature(mutatorenvironment::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::resource_has_name():
    assert hasattr(mutatorenvironment::Resource, "name")
    descriptor = None
    for klass in mutatorenvironment::Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::library_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Library)


def test_mutatorenvironment::library_constructor_exists():
    assert callable(mutatorenvironment::Library.__init__)


def test_mutatorenvironment::library_constructor_args():
    sig = inspect.signature(mutatorenvironment::Library.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::constraint_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Constraint)


def test_mutatorenvironment::constraint_constructor_exists():
    assert callable(mutatorenvironment::Constraint.__init__)


def test_mutatorenvironment::constraint_constructor_args():
    sig = inspect.signature(mutatorenvironment::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "rules" in params, "Missing parameter 'rules'"

def test_mutatorenvironment::constraint_has_id():
    assert hasattr(mutatorenvironment::Constraint, "id")
    descriptor = None
    for klass in mutatorenvironment::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::constraint_has_rules():
    assert hasattr(mutatorenvironment::Constraint, "rules")
    descriptor = None
    for klass in mutatorenvironment::Constraint.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::block_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Block)


def test_mutatorenvironment::block_constructor_exists():
    assert callable(mutatorenvironment::Block.__init__)


def test_mutatorenvironment::block_constructor_args():
    sig = inspect.signature(mutatorenvironment::Block.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "description" in params, "Missing parameter 'description'"
    assert "min" in params, "Missing parameter 'min'"
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "repeat" in params, "Missing parameter 'repeat'"
    assert "name" in params, "Missing parameter 'name'"

def test_mutatorenvironment::block_has_max():
    assert hasattr(mutatorenvironment::Block, "max")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::block_has_description():
    assert hasattr(mutatorenvironment::Block, "description")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::block_has_min():
    assert hasattr(mutatorenvironment::Block, "min")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::block_has_fixed():
    assert hasattr(mutatorenvironment::Block, "fixed")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::block_has_repeat():
    assert hasattr(mutatorenvironment::Block, "repeat")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "repeat" in klass.__dict__:
            descriptor = klass.__dict__["repeat"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::block_has_name():
    assert hasattr(mutatorenvironment::Block, "name")
    descriptor = None
    for klass in mutatorenvironment::Block.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_obselectionstrategy_is_not_abstract():
    assert not inspect.isabstract(ObSelectionStrategy)


def test_obselectionstrategy_constructor_exists():
    assert callable(ObSelectionStrategy.__init__)


def test_obselectionstrategy_constructor_args():
    sig = inspect.signature(ObSelectionStrategy.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::completeselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CompleteSelection)


def test_mutatorenvironment::completeselection_constructor_exists():
    assert callable(mutatorenvironment::CompleteSelection.__init__)


def test_mutatorenvironment::completeselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::CompleteSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::typedselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::TypedSelection)


def test_mutatorenvironment::typedselection_constructor_exists():
    assert callable(mutatorenvironment::TypedSelection.__init__)


def test_mutatorenvironment::typedselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::TypedSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::specificselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SpecificSelection)


def test_mutatorenvironment::specificselection_constructor_exists():
    assert callable(mutatorenvironment::SpecificSelection.__init__)


def test_mutatorenvironment::specificselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::SpecificSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::otherselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::OtherSelection)


def test_mutatorenvironment::otherselection_constructor_exists():
    assert callable(mutatorenvironment::OtherSelection.__init__)


def test_mutatorenvironment::otherselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::OtherSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::randomselection_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RandomSelection)


def test_mutatorenvironment::randomselection_constructor_exists():
    assert callable(mutatorenvironment::RandomSelection.__init__)


def test_mutatorenvironment::randomselection_constructor_args():
    sig = inspect.signature(mutatorenvironment::RandomSelection.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::expression_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Expression)


def test_mutatorenvironment::expression_constructor_exists():
    assert callable(mutatorenvironment::Expression.__init__)


def test_mutatorenvironment::expression_constructor_args():
    sig = inspect.signature(mutatorenvironment::Expression.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::ereference_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::EReference)


def test_mutatorenvironment::ereference_constructor_exists():
    assert callable(mutatorenvironment::EReference.__init__)


def test_mutatorenvironment::ereference_constructor_args():
    sig = inspect.signature(mutatorenvironment::EReference.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::referenceset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ReferenceSet)


def test_mutatorenvironment::referenceset_constructor_exists():
    assert callable(mutatorenvironment::ReferenceSet.__init__)


def test_mutatorenvironment::referenceset_constructor_args():
    sig = inspect.signature(mutatorenvironment::ReferenceSet.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::attributeset_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::AttributeSet)


def test_mutatorenvironment::attributeset_constructor_exists():
    assert callable(mutatorenvironment::AttributeSet.__init__)


def test_mutatorenvironment::attributeset_constructor_args():
    sig = inspect.signature(mutatorenvironment::AttributeSet.__init__)
    params = list(sig.parameters.keys())



def test_mutator_is_not_abstract():
    assert not inspect.isabstract(Mutator)


def test_mutator_constructor_exists():
    assert callable(Mutator.__init__)


def test_mutator_constructor_args():
    sig = inspect.signature(Mutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::modifytargetreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ModifyTargetReferenceMutator)


def test_mutatorenvironment::modifytargetreferencemutator_constructor_exists():
    assert callable(mutatorenvironment::ModifyTargetReferenceMutator.__init__)


def test_mutatorenvironment::modifytargetreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::ModifyTargetReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::modifysourcereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ModifySourceReferenceMutator)


def test_mutatorenvironment::modifysourcereferencemutator_constructor_exists():
    assert callable(mutatorenvironment::ModifySourceReferenceMutator.__init__)


def test_mutatorenvironment::modifysourcereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::ModifySourceReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::createreferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CreateReferenceMutator)


def test_mutatorenvironment::createreferencemutator_constructor_exists():
    assert callable(mutatorenvironment::CreateReferenceMutator.__init__)


def test_mutatorenvironment::createreferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::CreateReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::removeobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RemoveObjectMutator)


def test_mutatorenvironment::removeobjectmutator_constructor_exists():
    assert callable(mutatorenvironment::RemoveObjectMutator.__init__)


def test_mutatorenvironment::removeobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RemoveObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::retypeobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RetypeObjectMutator)


def test_mutatorenvironment::retypeobjectmutator_constructor_exists():
    assert callable(mutatorenvironment::RetypeObjectMutator.__init__)


def test_mutatorenvironment::retypeobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RetypeObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::selectobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SelectObjectMutator)


def test_mutatorenvironment::selectobjectmutator_constructor_exists():
    assert callable(mutatorenvironment::SelectObjectMutator.__init__)


def test_mutatorenvironment::selectobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::SelectObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::createobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CreateObjectMutator)


def test_mutatorenvironment::createobjectmutator_constructor_exists():
    assert callable(mutatorenvironment::CreateObjectMutator.__init__)


def test_mutatorenvironment::createobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::CreateObjectMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::modifyinformationmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ModifyInformationMutator)


def test_mutatorenvironment::modifyinformationmutator_constructor_exists():
    assert callable(mutatorenvironment::ModifyInformationMutator.__init__)


def test_mutatorenvironment::modifyinformationmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::ModifyInformationMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::cloneobjectmutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CloneObjectMutator)


def test_mutatorenvironment::cloneobjectmutator_constructor_exists():
    assert callable(mutatorenvironment::CloneObjectMutator.__init__)


def test_mutatorenvironment::cloneobjectmutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::CloneObjectMutator.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_mutatorenvironment::cloneobjectmutator_has_contents():
    assert hasattr(mutatorenvironment::CloneObjectMutator, "contents")
    descriptor = None
    for klass in mutatorenvironment::CloneObjectMutator.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::removereferencemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::RemoveReferenceMutator)


def test_mutatorenvironment::removereferencemutator_constructor_exists():
    assert callable(mutatorenvironment::RemoveReferenceMutator.__init__)


def test_mutatorenvironment::removereferencemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::RemoveReferenceMutator.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::selectsamplemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::SelectSampleMutator)


def test_mutatorenvironment::selectsamplemutator_constructor_exists():
    assert callable(mutatorenvironment::SelectSampleMutator.__init__)


def test_mutatorenvironment::selectsamplemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::SelectSampleMutator.__init__)
    params = list(sig.parameters.keys())
    assert "clause" in params, "Missing parameter 'clause'"

def test_mutatorenvironment::selectsamplemutator_has_clause():
    assert hasattr(mutatorenvironment::SelectSampleMutator, "clause")
    descriptor = None
    for klass in mutatorenvironment::SelectSampleMutator.__mro__:
        if "clause" in klass.__dict__:
            descriptor = klass.__dict__["clause"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::compositemutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::CompositeMutator)


def test_mutatorenvironment::compositemutator_constructor_exists():
    assert callable(mutatorenvironment::CompositeMutator.__init__)


def test_mutatorenvironment::compositemutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::CompositeMutator.__init__)
    params = list(sig.parameters.keys())



def test_objectemitter_is_not_abstract():
    assert not inspect.isabstract(ObjectEmitter)


def test_objectemitter_constructor_exists():
    assert callable(ObjectEmitter.__init__)


def test_objectemitter_constructor_args():
    sig = inspect.signature(ObjectEmitter.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::obselectionstrategy_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::ObSelectionStrategy)


def test_mutatorenvironment::obselectionstrategy_constructor_exists():
    assert callable(mutatorenvironment::ObSelectionStrategy.__init__)


def test_mutatorenvironment::obselectionstrategy_constructor_args():
    sig = inspect.signature(mutatorenvironment::ObSelectionStrategy.__init__)
    params = list(sig.parameters.keys())
    assert "resource" in params, "Missing parameter 'resource'"

def test_mutatorenvironment::obselectionstrategy_has_resource():
    assert hasattr(mutatorenvironment::ObSelectionStrategy, "resource")
    descriptor = None
    for klass in mutatorenvironment::ObSelectionStrategy.__mro__:
        if "resource" in klass.__dict__:
            descriptor = klass.__dict__["resource"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::eclass_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::EClass)


def test_mutatorenvironment::eclass_constructor_exists():
    assert callable(mutatorenvironment::EClass.__init__)


def test_mutatorenvironment::eclass_constructor_args():
    sig = inspect.signature(mutatorenvironment::EClass.__init__)
    params = list(sig.parameters.keys())



def test_mutatorenvironment::load_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Load)


def test_mutatorenvironment::load_constructor_exists():
    assert callable(mutatorenvironment::Load.__init__)


def test_mutatorenvironment::load_constructor_args():
    sig = inspect.signature(mutatorenvironment::Load.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mutatorenvironment::load_has_file():
    assert hasattr(mutatorenvironment::Load, "file")
    descriptor = None
    for klass in mutatorenvironment::Load.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::mutator_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Mutator)


def test_mutatorenvironment::mutator_constructor_exists():
    assert callable(mutatorenvironment::Mutator.__init__)


def test_mutatorenvironment::mutator_constructor_args():
    sig = inspect.signature(mutatorenvironment::Mutator.__init__)
    params = list(sig.parameters.keys())
    assert "fixed" in params, "Missing parameter 'fixed'"
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_mutatorenvironment::mutator_has_fixed():
    assert hasattr(mutatorenvironment::Mutator, "fixed")
    descriptor = None
    for klass in mutatorenvironment::Mutator.__mro__:
        if "fixed" in klass.__dict__:
            descriptor = klass.__dict__["fixed"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::mutator_has_min():
    assert hasattr(mutatorenvironment::Mutator, "min")
    descriptor = None
    for klass in mutatorenvironment::Mutator.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_mutatorenvironment::mutator_has_max():
    assert hasattr(mutatorenvironment::Mutator, "max")
    descriptor = None
    for klass in mutatorenvironment::Mutator.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::definition_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::Definition)


def test_mutatorenvironment::definition_constructor_exists():
    assert callable(mutatorenvironment::Definition.__init__)


def test_mutatorenvironment::definition_constructor_args():
    sig = inspect.signature(mutatorenvironment::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"

def test_mutatorenvironment::definition_has_metamodel():
    assert hasattr(mutatorenvironment::Definition, "metamodel")
    descriptor = None
    for klass in mutatorenvironment::Definition.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)



def test_mutatorenvironment::mutatorenvironment_is_not_abstract():
    assert not inspect.isabstract(mutatorenvironment::MutatorEnvironment)


def test_mutatorenvironment::mutatorenvironment_constructor_exists():
    assert callable(mutatorenvironment::MutatorEnvironment.__init__)


def test_mutatorenvironment::mutatorenvironment_constructor_args():
    sig = inspect.signature(mutatorenvironment::MutatorEnvironment.__init__)
    params = list(sig.parameters.keys())

def test_logicoperator_exists():
    # Check that the Enumeration exists
    assert LogicOperator is not None

def test_logicoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicOperator]
    expected_literals = [
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicOperator"

def test_arithmeticoperator_exists():
    # Check that the Enumeration exists
    assert ArithmeticOperator is not None

def test_arithmeticoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArithmeticOperator]
    expected_literals = [
        "module",
        "multiply",
        "subtract",
        "add",
        "divide",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArithmeticOperator"

def test_sampleclause_exists():
    # Check that the Enumeration exists
    assert SampleClause is not None

def test_sampleclause_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SampleClause]
    expected_literals = [
        "equals",
        "distinct",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SampleClause"

def test_repeat_exists():
    # Check that the Enumeration exists
    assert Repeat is not None

def test_repeat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Repeat]
    expected_literals = [
        "yes",
        "no",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Repeat"

def test_operator_exists():
    # Check that the Enumeration exists
    assert Operator is not None

def test_operator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operator]
    expected_literals = [
        "in_",
        "is_",
        "gt",
        "lte",
        "not_",
        "different",
        "equals",
        "gte",
        "lt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operator"


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
mutatorenvironment::miniOCL::NavigationPathCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationPathCS,
)
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
mutatorenvironment::miniOCL::NavigationPathElementCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationPathElementCS,
)
mutatorenvironment::miniOCL::NavigationPathVariableCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationPathVariableCS,
    varName=
        st.none()
)
mutatorenvironment::miniOCL::NavigationPathNameCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationPathNameCS,
)
NavigationPathNameCS_strategy = st.builds(
    NavigationPathNameCS,
)
mutatorenvironment::miniOCL::IteratorVarCS_strategy = st.builds(
    mutatorenvironment::miniOCL::IteratorVarCS,
    itName=
        st.none()
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
mutatorenvironment::miniOCL::ForAllExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ForAllExpCS,
)
mutatorenvironment::miniOCL::IterateExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::IterateExpCS,
)
mutatorenvironment::miniOCL::CollectExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::CollectExpCS,
)
IteratorVarCS_strategy = st.builds(
    IteratorVarCS,
)
mutatorenvironment::miniOCL::ExistsExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ExistsExpCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
mutatorenvironment::miniOCL::BooleanExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::BooleanExpCS,
    boolSymbol=
        st.none()
)
miniOCL::mutatorenvironment::EStructuralFeature_strategy = st.builds(
    miniOCL::mutatorenvironment::EStructuralFeature,
)
mutatorenvironment::miniOCL::PathCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PathCS,
)
PathCS_strategy = st.builds(
    PathCS,
)
mutatorenvironment::miniOCL::PathElementCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PathElementCS,
)
mutatorenvironment::miniOCL::PathVariableCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PathVariableCS,
    varName=
        st.none()
)
mutatorenvironment::miniOCL::PathNameCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PathNameCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
mutatorenvironment::miniOCL::StringLiteralExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::StringLiteralExpCS,
    stringSymbol=
        st.none()
)
mutatorenvironment::miniOCL::BooleanLiteralExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::BooleanLiteralExpCS,
)
mutatorenvironment::miniOCL::IntLiteralExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::IntLiteralExpCS,
    intSymbol=
        st.none()
)
mutatorenvironment::miniOCL::RoundedBracketClauseCS_strategy = st.builds(
    mutatorenvironment::miniOCL::RoundedBracketClauseCS,
)
mutatorenvironment::miniOCL::AccVarCS_strategy = st.builds(
    mutatorenvironment::miniOCL::AccVarCS,
    accVarName=
        st.none()
)
AccVarCS_strategy = st.builds(
    AccVarCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
ParameterCS_strategy = st.builds(
    ParameterCS,
)
mutatorenvironment::miniOCL::OperationCS_strategy = st.builds(
    mutatorenvironment::miniOCL::OperationCS,
    name=
        st.none()
)
mutatorenvironment::miniOCL::PropertyCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PropertyCS,
    name=
        st.none()
)
OperationCS_strategy = st.builds(
    OperationCS,
)
PropertyCS_strategy = st.builds(
    PropertyCS,
)
RoundedBracketClauseCS_strategy = st.builds(
    RoundedBracketClauseCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
mutatorenvironment::miniOCL::LiteralExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::LiteralExpCS,
)
mutatorenvironment::miniOCL::NavigationExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationExpCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
mutatorenvironment::miniOCL::LoopExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::LoopExpCS,
    logicOp=
        st.none()
)
mutatorenvironment::miniOCL::NameExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NameExpCS,
)
mutatorenvironment::miniOCL::NavigationNameExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::NavigationNameExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
mutatorenvironment::miniOCL::PrimaryExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PrimaryExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
mutatorenvironment::miniOCL::CallExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::CallExpCS,
)
mutatorenvironment::miniOCL::LogicExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::LogicExpCS,
    op=
        st.none()
)
mutatorenvironment::miniOCL::ExpCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ExpCS,
)
mutatorenvironment::miniOCL::InvariantCS_strategy = st.builds(
    mutatorenvironment::miniOCL::InvariantCS,
)
mutatorenvironment::miniOCL::ConstraintCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ConstraintCS,
)
mutatorenvironment::miniOCL::ParameterCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ParameterCS,
    name=
        st.none()
)
mutatorenvironment::EStructuralFeature_strategy = st.builds(
    mutatorenvironment::EStructuralFeature,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
mutatorenvironment::miniOCL::ClassCS_strategy = st.builds(
    mutatorenvironment::miniOCL::ClassCS,
    name=
        st.none()
)
ClassCS_strategy = st.builds(
    ClassCS,
)
mutatorenvironment::miniOCL::PackageCS_strategy = st.builds(
    mutatorenvironment::miniOCL::PackageCS,
    name=
        st.none()
)
ConstraintCS_strategy = st.builds(
    ConstraintCS,
)
PackageCS_strategy = st.builds(
    PackageCS,
)
mutatorenvironment::miniOCL::RootCS_strategy = st.builds(
    mutatorenvironment::miniOCL::RootCS,
)
mutatorenvironment::EObject_strategy = st.builds(
    mutatorenvironment::EObject,
)
RandomNumberType_strategy = st.builds(
    RandomNumberType,
)
mutatorenvironment::RandomIntegerNumberType_strategy = st.builds(
    mutatorenvironment::RandomIntegerNumberType,
    min=
        st.none()
)
mutatorenvironment::RandomDoubleNumberType_strategy = st.builds(
    mutatorenvironment::RandomDoubleNumberType,
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mutatorenvironment::BinaryOperator_strategy = st.builds(
    mutatorenvironment::BinaryOperator,
    type=
        st.none()
)
InvariantCS_strategy = st.builds(
    InvariantCS,
)
ReferenceSet_strategy = st.builds(
    ReferenceSet,
)
mutatorenvironment::ReferenceAtt_strategy = st.builds(
    mutatorenvironment::ReferenceAtt,
)
mutatorenvironment::ReferenceRemove_strategy = st.builds(
    mutatorenvironment::ReferenceRemove,
)
mutatorenvironment::ReferenceSwap_strategy = st.builds(
    mutatorenvironment::ReferenceSwap,
)
mutatorenvironment::ReferenceAdd_strategy = st.builds(
    mutatorenvironment::ReferenceAdd,
)
mutatorenvironment::ReferenceInit_strategy = st.builds(
    mutatorenvironment::ReferenceInit,
)
mutatorenvironment::AttributeEvaluationType_strategy = st.builds(
    mutatorenvironment::AttributeEvaluationType,
)
Evaluation_strategy = st.builds(
    Evaluation,
)
mutatorenvironment::AttributeEvaluation_strategy = st.builds(
    mutatorenvironment::AttributeEvaluation,
)
mutatorenvironment::Evaluation_strategy = st.builds(
    mutatorenvironment::Evaluation,
)
mutatorenvironment::ReferenceEvaluation_strategy = st.builds(
    mutatorenvironment::ReferenceEvaluation,
    container=
        st.none(),
    operator=
        st.none()
)
mutatorenvironment::EAttribute_strategy = st.builds(
    mutatorenvironment::EAttribute,
)
OtherSelection_strategy = st.builds(
    OtherSelection,
)
mutatorenvironment::OtherTypeSelection_strategy = st.builds(
    mutatorenvironment::OtherTypeSelection,
)
CompleteSelection_strategy = st.builds(
    CompleteSelection,
)
mutatorenvironment::CompleteTypeSelection_strategy = st.builds(
    mutatorenvironment::CompleteTypeSelection,
)
RemoveReferenceMutator_strategy = st.builds(
    RemoveReferenceMutator,
)
mutatorenvironment::RemoveSpecificReferenceMutator_strategy = st.builds(
    mutatorenvironment::RemoveSpecificReferenceMutator,
)
mutatorenvironment::RemoveCompleteReferenceMutator_strategy = st.builds(
    mutatorenvironment::RemoveCompleteReferenceMutator,
)
mutatorenvironment::RemoveRandomReferenceMutator_strategy = st.builds(
    mutatorenvironment::RemoveRandomReferenceMutator,
)
BooleanType_strategy = st.builds(
    BooleanType,
)
mutatorenvironment::RandomBooleanType_strategy = st.builds(
    mutatorenvironment::RandomBooleanType,
    allowsNull=
        st.none()
)
mutatorenvironment::SpecificBooleanType_strategy = st.builds(
    mutatorenvironment::SpecificBooleanType,
    value=
        st.none()
)
AttributeType_strategy = st.builds(
    AttributeType,
)
mutatorenvironment::ListType_strategy = st.builds(
    mutatorenvironment::ListType,
)
mutatorenvironment::StringType_strategy = st.builds(
    mutatorenvironment::StringType,
)
mutatorenvironment::RandomType_strategy = st.builds(
    mutatorenvironment::RandomType,
)
mutatorenvironment::ListStringType_strategy = st.builds(
    mutatorenvironment::ListStringType,
    value=
        st.none()
)
mutatorenvironment::NumberType_strategy = st.builds(
    mutatorenvironment::NumberType,
)
mutatorenvironment::BooleanType_strategy = st.builds(
    mutatorenvironment::BooleanType,
)
AttributeEvaluationType_strategy = st.builds(
    AttributeEvaluationType,
)
mutatorenvironment::ObjectAttributeType_strategy = st.builds(
    mutatorenvironment::ObjectAttributeType,
    operator=
        st.none()
)
mutatorenvironment::AttributeType_strategy = st.builds(
    mutatorenvironment::AttributeType,
    operator=
        st.none()
)
AttributeSet_strategy = st.builds(
    AttributeSet,
)
mutatorenvironment::AttributeUnset_strategy = st.builds(
    mutatorenvironment::AttributeUnset,
)
mutatorenvironment::AttributeSwap_strategy = st.builds(
    mutatorenvironment::AttributeSwap,
)
mutatorenvironment::AttributeOperation_strategy = st.builds(
    mutatorenvironment::AttributeOperation,
    operator=
        st.none()
)
mutatorenvironment::AttributeCopy_strategy = st.builds(
    mutatorenvironment::AttributeCopy,
)
mutatorenvironment::AttributeReverse_strategy = st.builds(
    mutatorenvironment::AttributeReverse,
)
mutatorenvironment::AttributeScalar_strategy = st.builds(
    mutatorenvironment::AttributeScalar,
)
SpecificSelection_strategy = st.builds(
    SpecificSelection,
)
mutatorenvironment::SpecificClosureSelection_strategy = st.builds(
    mutatorenvironment::SpecificClosureSelection,
)
mutatorenvironment::SpecificObjectSelection_strategy = st.builds(
    mutatorenvironment::SpecificObjectSelection,
)
RandomSelection_strategy = st.builds(
    RandomSelection,
)
mutatorenvironment::RandomTypeSelection_strategy = st.builds(
    mutatorenvironment::RandomTypeSelection,
)
mutatorenvironment::SpecificReferenceSelection_strategy = st.builds(
    mutatorenvironment::SpecificReferenceSelection,
)
DoubleType_strategy = st.builds(
    DoubleType,
)
mutatorenvironment::RandomDoubleType_strategy = st.builds(
    mutatorenvironment::RandomDoubleType,
    min=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    max=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    allowsNull=
        st.none()
)
mutatorenvironment::SpecificDoubleType_strategy = st.builds(
    mutatorenvironment::SpecificDoubleType,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
IntegerType_strategy = st.builds(
    IntegerType,
)
mutatorenvironment::RandomIntegerType_strategy = st.builds(
    mutatorenvironment::RandomIntegerType,
    max=
        st.none(),
    min=
        st.none(),
    allowsNull=
        st.none()
)
mutatorenvironment::SpecificIntegerType_strategy = st.builds(
    mutatorenvironment::SpecificIntegerType,
    value=
        st.none()
)
NumberType_strategy = st.builds(
    NumberType,
)
mutatorenvironment::MinValueType_strategy = st.builds(
    mutatorenvironment::MinValueType,
)
mutatorenvironment::RandomNumberType_strategy = st.builds(
    mutatorenvironment::RandomNumberType,
)
mutatorenvironment::DoubleType_strategy = st.builds(
    mutatorenvironment::DoubleType,
)
mutatorenvironment::MaxValueType_strategy = st.builds(
    mutatorenvironment::MaxValueType,
)
mutatorenvironment::IntegerType_strategy = st.builds(
    mutatorenvironment::IntegerType,
)
StringType_strategy = st.builds(
    StringType,
)
mutatorenvironment::ReplaceStringType_strategy = st.builds(
    mutatorenvironment::ReplaceStringType,
    oldstring=
        st.none(),
    newstring=
        st.none()
)
mutatorenvironment::RandomStringNumberType_strategy = st.builds(
    mutatorenvironment::RandomStringNumberType,
    allowsNull=
        st.none(),
    min=
        st.none(),
    max=
        st.none()
)
mutatorenvironment::CatEndStringType_strategy = st.builds(
    mutatorenvironment::CatEndStringType,
    value=
        st.none()
)
mutatorenvironment::CatStartStringType_strategy = st.builds(
    mutatorenvironment::CatStartStringType,
    value=
        st.none()
)
mutatorenvironment::UpperStringType_strategy = st.builds(
    mutatorenvironment::UpperStringType,
    value=
        st.none()
)
mutatorenvironment::RandomStringType_strategy = st.builds(
    mutatorenvironment::RandomStringType,
    max=
        st.none(),
    min=
        st.none(),
    allowsNull=
        st.none()
)
mutatorenvironment::LowerStringType_strategy = st.builds(
    mutatorenvironment::LowerStringType,
    value=
        st.none()
)
mutatorenvironment::SpecificStringType_strategy = st.builds(
    mutatorenvironment::SpecificStringType,
    value=
        st.none()
)
mutatorenvironment::ObjectEmitter_strategy = st.builds(
    mutatorenvironment::ObjectEmitter,
    name=
        st.none()
)
mutatorenvironment::Source_strategy = st.builds(
    mutatorenvironment::Source,
    path=
        st.none()
)
Definition_strategy = st.builds(
    Definition,
)
mutatorenvironment::Program_strategy = st.builds(
    mutatorenvironment::Program,
    exhaustive=
        st.none(),
    num=
        st.none(),
    description=
        st.none(),
    output=
        st.none()
)
mutatorenvironment::Resource_strategy = st.builds(
    mutatorenvironment::Resource,
    name=
        st.none()
)
mutatorenvironment::Library_strategy = st.builds(
    mutatorenvironment::Library,
)
mutatorenvironment::Constraint_strategy = st.builds(
    mutatorenvironment::Constraint,
    id=
        st.none(),
    rules=
        st.none()
)
mutatorenvironment::Block_strategy = st.builds(
    mutatorenvironment::Block,
    max=
        st.none(),
    description=
        st.none(),
    min=
        st.none(),
    fixed=
        st.none(),
    repeat=
        st.none(),
    name=
        st.none()
)
ObSelectionStrategy_strategy = st.builds(
    ObSelectionStrategy,
)
mutatorenvironment::CompleteSelection_strategy = st.builds(
    mutatorenvironment::CompleteSelection,
)
mutatorenvironment::TypedSelection_strategy = st.builds(
    mutatorenvironment::TypedSelection,
)
mutatorenvironment::SpecificSelection_strategy = st.builds(
    mutatorenvironment::SpecificSelection,
)
mutatorenvironment::OtherSelection_strategy = st.builds(
    mutatorenvironment::OtherSelection,
)
mutatorenvironment::RandomSelection_strategy = st.builds(
    mutatorenvironment::RandomSelection,
)
mutatorenvironment::Expression_strategy = st.builds(
    mutatorenvironment::Expression,
)
mutatorenvironment::EReference_strategy = st.builds(
    mutatorenvironment::EReference,
)
mutatorenvironment::ReferenceSet_strategy = st.builds(
    mutatorenvironment::ReferenceSet,
)
mutatorenvironment::AttributeSet_strategy = st.builds(
    mutatorenvironment::AttributeSet,
)
Mutator_strategy = st.builds(
    Mutator,
)
mutatorenvironment::ModifyTargetReferenceMutator_strategy = st.builds(
    mutatorenvironment::ModifyTargetReferenceMutator,
)
mutatorenvironment::ModifySourceReferenceMutator_strategy = st.builds(
    mutatorenvironment::ModifySourceReferenceMutator,
)
mutatorenvironment::CreateReferenceMutator_strategy = st.builds(
    mutatorenvironment::CreateReferenceMutator,
)
mutatorenvironment::RemoveObjectMutator_strategy = st.builds(
    mutatorenvironment::RemoveObjectMutator,
)
mutatorenvironment::RetypeObjectMutator_strategy = st.builds(
    mutatorenvironment::RetypeObjectMutator,
)
mutatorenvironment::SelectObjectMutator_strategy = st.builds(
    mutatorenvironment::SelectObjectMutator,
)
mutatorenvironment::CreateObjectMutator_strategy = st.builds(
    mutatorenvironment::CreateObjectMutator,
)
mutatorenvironment::ModifyInformationMutator_strategy = st.builds(
    mutatorenvironment::ModifyInformationMutator,
)
mutatorenvironment::CloneObjectMutator_strategy = st.builds(
    mutatorenvironment::CloneObjectMutator,
    contents=
        st.none()
)
mutatorenvironment::RemoveReferenceMutator_strategy = st.builds(
    mutatorenvironment::RemoveReferenceMutator,
)
mutatorenvironment::SelectSampleMutator_strategy = st.builds(
    mutatorenvironment::SelectSampleMutator,
    clause=
        st.none()
)
mutatorenvironment::CompositeMutator_strategy = st.builds(
    mutatorenvironment::CompositeMutator,
)
ObjectEmitter_strategy = st.builds(
    ObjectEmitter,
)
mutatorenvironment::ObSelectionStrategy_strategy = st.builds(
    mutatorenvironment::ObSelectionStrategy,
    resource=
        st.none()
)
mutatorenvironment::EClass_strategy = st.builds(
    mutatorenvironment::EClass,
)
mutatorenvironment::Load_strategy = st.builds(
    mutatorenvironment::Load,
    file=
        st.none()
)
mutatorenvironment::Mutator_strategy = st.builds(
    mutatorenvironment::Mutator,
    fixed=
        st.none(),
    min=
        st.none(),
    max=
        st.none()
)
mutatorenvironment::Definition_strategy = st.builds(
    mutatorenvironment::Definition,
    metamodel=
        st.none()
)
mutatorenvironment::MutatorEnvironment_strategy = st.builds(
    mutatorenvironment::MutatorEnvironment,
)

@given(instance=mutatorenvironment::miniOCL::NavigationPathCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationpathcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationPathCS)

@given(instance=NavigationPathCS_strategy)
@settings(max_examples=50)
def test_navigationpathcs_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)

@given(instance=mutatorenvironment::miniOCL::NavigationPathElementCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationpathelementcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationPathElementCS)

@given(instance=mutatorenvironment::miniOCL::NavigationPathVariableCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationpathvariablecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationPathVariableCS)

@given(instance=mutatorenvironment::miniOCL::NavigationPathVariableCS_strategy)
def test_mutatorenvironment::miniocl::navigationpathvariablecs_varName_type(instance):
    assert isinstance(instance.varName, stringtype)


@given(instance=mutatorenvironment::miniOCL::NavigationPathVariableCS_strategy)
def test_mutatorenvironment::miniocl::navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=mutatorenvironment::miniOCL::NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationPathNameCS)

@given(instance=NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, NavigationPathNameCS)

@given(instance=mutatorenvironment::miniOCL::IteratorVarCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::iteratorvarcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::IteratorVarCS)

@given(instance=mutatorenvironment::miniOCL::IteratorVarCS_strategy)
def test_mutatorenvironment::miniocl::iteratorvarcs_itName_type(instance):
    assert isinstance(instance.itName, stringtype)


@given(instance=mutatorenvironment::miniOCL::IteratorVarCS_strategy)
def test_mutatorenvironment::miniocl::iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=mutatorenvironment::miniOCL::ForAllExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::forallexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ForAllExpCS)

@given(instance=mutatorenvironment::miniOCL::IterateExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::iterateexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::IterateExpCS)

@given(instance=mutatorenvironment::miniOCL::CollectExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::collectexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::CollectExpCS)

@given(instance=IteratorVarCS_strategy)
@settings(max_examples=50)
def test_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, IteratorVarCS)

@given(instance=mutatorenvironment::miniOCL::ExistsExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::existsexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ExistsExpCS)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::BooleanExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::booleanexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::BooleanExpCS)

@given(instance=mutatorenvironment::miniOCL::BooleanExpCS_strategy)
def test_mutatorenvironment::miniocl::booleanexpcs_boolSymbol_type(instance):
    assert isinstance(instance.boolSymbol, booleantype)


@given(instance=mutatorenvironment::miniOCL::BooleanExpCS_strategy)
def test_mutatorenvironment::miniocl::booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=miniOCL::mutatorenvironment::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_miniocl::mutatorenvironment::estructuralfeature_instantiation(instance):
    assert isinstance(instance, miniOCL::mutatorenvironment::EStructuralFeature)

@given(instance=mutatorenvironment::miniOCL::PathCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::pathcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PathCS)

@given(instance=PathCS_strategy)
@settings(max_examples=50)
def test_pathcs_instantiation(instance):
    assert isinstance(instance, PathCS)

@given(instance=mutatorenvironment::miniOCL::PathElementCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::pathelementcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PathElementCS)

@given(instance=mutatorenvironment::miniOCL::PathVariableCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::pathvariablecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PathVariableCS)

@given(instance=mutatorenvironment::miniOCL::PathVariableCS_strategy)
def test_mutatorenvironment::miniocl::pathvariablecs_varName_type(instance):
    assert isinstance(instance.varName, stringtype)


@given(instance=mutatorenvironment::miniOCL::PathVariableCS_strategy)
def test_mutatorenvironment::miniocl::pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=mutatorenvironment::miniOCL::PathNameCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::pathnamecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PathNameCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::StringLiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::StringLiteralExpCS_strategy)
def test_mutatorenvironment::miniocl::stringliteralexpcs_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, stringtype)


@given(instance=mutatorenvironment::miniOCL::StringLiteralExpCS_strategy)
def test_mutatorenvironment::miniocl::stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=mutatorenvironment::miniOCL::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::BooleanLiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::intliteralexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::IntLiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::IntLiteralExpCS_strategy)
def test_mutatorenvironment::miniocl::intliteralexpcs_intSymbol_type(instance):
    assert isinstance(instance.intSymbol, integertype)


@given(instance=mutatorenvironment::miniOCL::IntLiteralExpCS_strategy)
def test_mutatorenvironment::miniocl::intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=mutatorenvironment::miniOCL::RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::RoundedBracketClauseCS)

@given(instance=mutatorenvironment::miniOCL::AccVarCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::accvarcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::AccVarCS)

@given(instance=mutatorenvironment::miniOCL::AccVarCS_strategy)
def test_mutatorenvironment::miniocl::accvarcs_accVarName_type(instance):
    assert isinstance(instance.accVarName, stringtype)


@given(instance=mutatorenvironment::miniOCL::AccVarCS_strategy)
def test_mutatorenvironment::miniocl::accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original

@given(instance=AccVarCS_strategy)
@settings(max_examples=50)
def test_accvarcs_instantiation(instance):
    assert isinstance(instance, AccVarCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=ParameterCS_strategy)
@settings(max_examples=50)
def test_parametercs_instantiation(instance):
    assert isinstance(instance, ParameterCS)

@given(instance=mutatorenvironment::miniOCL::OperationCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::operationcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::OperationCS)

@given(instance=mutatorenvironment::miniOCL::OperationCS_strategy)
def test_mutatorenvironment::miniocl::operationcs_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::miniOCL::OperationCS_strategy)
def test_mutatorenvironment::miniocl::operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment::miniOCL::PropertyCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::propertycs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PropertyCS)

@given(instance=mutatorenvironment::miniOCL::PropertyCS_strategy)
def test_mutatorenvironment::miniocl::propertycs_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::miniOCL::PropertyCS_strategy)
def test_mutatorenvironment::miniocl::propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OperationCS_strategy)
@settings(max_examples=50)
def test_operationcs_instantiation(instance):
    assert isinstance(instance, OperationCS)

@given(instance=PropertyCS_strategy)
@settings(max_examples=50)
def test_propertycs_instantiation(instance):
    assert isinstance(instance, PropertyCS)

@given(instance=RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, RoundedBracketClauseCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=mutatorenvironment::miniOCL::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::literalexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::LiteralExpCS)

@given(instance=mutatorenvironment::miniOCL::NavigationExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationExpCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=mutatorenvironment::miniOCL::LoopExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::loopexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::LoopExpCS)

@given(instance=mutatorenvironment::miniOCL::LoopExpCS_strategy)
def test_mutatorenvironment::miniocl::loopexpcs_logicOp_type(instance):
    assert isinstance(instance.logicOp, stringtype)


@given(instance=mutatorenvironment::miniOCL::LoopExpCS_strategy)
def test_mutatorenvironment::miniocl::loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=mutatorenvironment::miniOCL::NameExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::nameexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NameExpCS)

@given(instance=mutatorenvironment::miniOCL::NavigationNameExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::navigationnameexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::NavigationNameExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=mutatorenvironment::miniOCL::PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::primaryexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PrimaryExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=mutatorenvironment::miniOCL::CallExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::callexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::CallExpCS)

@given(instance=mutatorenvironment::miniOCL::LogicExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::logicexpcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::LogicExpCS)

@given(instance=mutatorenvironment::miniOCL::LogicExpCS_strategy)
def test_mutatorenvironment::miniocl::logicexpcs_op_type(instance):
    assert isinstance(instance.op, stringtype)


@given(instance=mutatorenvironment::miniOCL::LogicExpCS_strategy)
def test_mutatorenvironment::miniocl::logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=mutatorenvironment::miniOCL::ExpCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::expcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ExpCS)

@given(instance=mutatorenvironment::miniOCL::InvariantCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::invariantcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::InvariantCS)

@given(instance=mutatorenvironment::miniOCL::ConstraintCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::constraintcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ConstraintCS)

@given(instance=mutatorenvironment::miniOCL::ParameterCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::parametercs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ParameterCS)

@given(instance=mutatorenvironment::miniOCL::ParameterCS_strategy)
def test_mutatorenvironment::miniocl::parametercs_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::miniOCL::ParameterCS_strategy)
def test_mutatorenvironment::miniocl::parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::estructuralfeature_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::EStructuralFeature)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=mutatorenvironment::miniOCL::ClassCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::classcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::ClassCS)

@given(instance=mutatorenvironment::miniOCL::ClassCS_strategy)
def test_mutatorenvironment::miniocl::classcs_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::miniOCL::ClassCS_strategy)
def test_mutatorenvironment::miniocl::classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ClassCS_strategy)
@settings(max_examples=50)
def test_classcs_instantiation(instance):
    assert isinstance(instance, ClassCS)

@given(instance=mutatorenvironment::miniOCL::PackageCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::packagecs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::PackageCS)

@given(instance=mutatorenvironment::miniOCL::PackageCS_strategy)
def test_mutatorenvironment::miniocl::packagecs_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::miniOCL::PackageCS_strategy)
def test_mutatorenvironment::miniocl::packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ConstraintCS_strategy)
@settings(max_examples=50)
def test_constraintcs_instantiation(instance):
    assert isinstance(instance, ConstraintCS)

@given(instance=PackageCS_strategy)
@settings(max_examples=50)
def test_packagecs_instantiation(instance):
    assert isinstance(instance, PackageCS)

@given(instance=mutatorenvironment::miniOCL::RootCS_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::miniocl::rootcs_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::miniOCL::RootCS)

@given(instance=mutatorenvironment::EObject_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::eobject_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::EObject)

@given(instance=RandomNumberType_strategy)
@settings(max_examples=50)
def test_randomnumbertype_instantiation(instance):
    assert isinstance(instance, RandomNumberType)

@given(instance=mutatorenvironment::RandomIntegerNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomintegernumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomIntegerNumberType)

@given(instance=mutatorenvironment::RandomIntegerNumberType_strategy)
def test_mutatorenvironment::randomintegernumbertype_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::RandomIntegerNumberType_strategy)
def test_mutatorenvironment::randomintegernumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::RandomDoubleNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomdoublenumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomDoubleNumberType)

@given(instance=mutatorenvironment::RandomDoubleNumberType_strategy)
def test_mutatorenvironment::randomdoublenumbertype_min_type(instance):
    assert isinstance(instance.min, float)


@given(instance=mutatorenvironment::RandomDoubleNumberType_strategy)
def test_mutatorenvironment::randomdoublenumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::BinaryOperator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::binaryoperator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::BinaryOperator)

@given(instance=mutatorenvironment::BinaryOperator_strategy)
def test_mutatorenvironment::binaryoperator_type_type(instance):
    assert isinstance(instance.type, stringtype)


@given(instance=mutatorenvironment::BinaryOperator_strategy)
def test_mutatorenvironment::binaryoperator_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=InvariantCS_strategy)
@settings(max_examples=50)
def test_invariantcs_instantiation(instance):
    assert isinstance(instance, InvariantCS)

@given(instance=ReferenceSet_strategy)
@settings(max_examples=50)
def test_referenceset_instantiation(instance):
    assert isinstance(instance, ReferenceSet)

@given(instance=mutatorenvironment::ReferenceAtt_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceatt_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceAtt)

@given(instance=mutatorenvironment::ReferenceRemove_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceremove_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceRemove)

@given(instance=mutatorenvironment::ReferenceSwap_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceswap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceSwap)

@given(instance=mutatorenvironment::ReferenceAdd_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceadd_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceAdd)

@given(instance=mutatorenvironment::ReferenceInit_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceinit_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceInit)

@given(instance=mutatorenvironment::AttributeEvaluationType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeevaluationtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeEvaluationType)

@given(instance=Evaluation_strategy)
@settings(max_examples=50)
def test_evaluation_instantiation(instance):
    assert isinstance(instance, Evaluation)

@given(instance=mutatorenvironment::AttributeEvaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeevaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeEvaluation)

@given(instance=mutatorenvironment::Evaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::evaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Evaluation)

@given(instance=mutatorenvironment::ReferenceEvaluation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceevaluation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceEvaluation)

@given(instance=mutatorenvironment::ReferenceEvaluation_strategy)
def test_mutatorenvironment::referenceevaluation_container_type(instance):
    assert isinstance(instance.container, booleantype)


@given(instance=mutatorenvironment::ReferenceEvaluation_strategy)
def test_mutatorenvironment::referenceevaluation_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=mutatorenvironment::ReferenceEvaluation_strategy)
def test_mutatorenvironment::referenceevaluation_operator_type(instance):
    assert isinstance(instance.operator, stringtype)


@given(instance=mutatorenvironment::ReferenceEvaluation_strategy)
def test_mutatorenvironment::referenceevaluation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mutatorenvironment::EAttribute_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::eattribute_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::EAttribute)

@given(instance=OtherSelection_strategy)
@settings(max_examples=50)
def test_otherselection_instantiation(instance):
    assert isinstance(instance, OtherSelection)

@given(instance=mutatorenvironment::OtherTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::othertypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::OtherTypeSelection)

@given(instance=CompleteSelection_strategy)
@settings(max_examples=50)
def test_completeselection_instantiation(instance):
    assert isinstance(instance, CompleteSelection)

@given(instance=mutatorenvironment::CompleteTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::completetypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CompleteTypeSelection)

@given(instance=RemoveReferenceMutator_strategy)
@settings(max_examples=50)
def test_removereferencemutator_instantiation(instance):
    assert isinstance(instance, RemoveReferenceMutator)

@given(instance=mutatorenvironment::RemoveSpecificReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::removespecificreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RemoveSpecificReferenceMutator)

@given(instance=mutatorenvironment::RemoveCompleteReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::removecompletereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RemoveCompleteReferenceMutator)

@given(instance=mutatorenvironment::RemoveRandomReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::removerandomreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RemoveRandomReferenceMutator)

@given(instance=BooleanType_strategy)
@settings(max_examples=50)
def test_booleantype_instantiation(instance):
    assert isinstance(instance, BooleanType)

@given(instance=mutatorenvironment::RandomBooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randombooleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomBooleanType)

@given(instance=mutatorenvironment::RandomBooleanType_strategy)
def test_mutatorenvironment::randombooleantype_allowsNull_type(instance):
    assert isinstance(instance.allowsNull, booleantype)


@given(instance=mutatorenvironment::RandomBooleanType_strategy)
def test_mutatorenvironment::randombooleantype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment::SpecificBooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificbooleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificBooleanType)

@given(instance=mutatorenvironment::SpecificBooleanType_strategy)
def test_mutatorenvironment::specificbooleantype_value_type(instance):
    assert isinstance(instance.value, booleantype)


@given(instance=mutatorenvironment::SpecificBooleanType_strategy)
def test_mutatorenvironment::specificbooleantype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AttributeType_strategy)
@settings(max_examples=50)
def test_attributetype_instantiation(instance):
    assert isinstance(instance, AttributeType)

@given(instance=mutatorenvironment::ListType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::listtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ListType)

@given(instance=mutatorenvironment::StringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::stringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::StringType)

@given(instance=mutatorenvironment::RandomType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomType)

@given(instance=mutatorenvironment::ListStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::liststringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ListStringType)

@given(instance=mutatorenvironment::ListStringType_strategy)
def test_mutatorenvironment::liststringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::ListStringType_strategy)
def test_mutatorenvironment::liststringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::NumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::numbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::NumberType)

@given(instance=mutatorenvironment::BooleanType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::booleantype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::BooleanType)

@given(instance=AttributeEvaluationType_strategy)
@settings(max_examples=50)
def test_attributeevaluationtype_instantiation(instance):
    assert isinstance(instance, AttributeEvaluationType)

@given(instance=mutatorenvironment::ObjectAttributeType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::objectattributetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ObjectAttributeType)

@given(instance=mutatorenvironment::ObjectAttributeType_strategy)
def test_mutatorenvironment::objectattributetype_operator_type(instance):
    assert isinstance(instance.operator, stringtype)


@given(instance=mutatorenvironment::ObjectAttributeType_strategy)
def test_mutatorenvironment::objectattributetype_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mutatorenvironment::AttributeType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeType)

@given(instance=mutatorenvironment::AttributeType_strategy)
def test_mutatorenvironment::attributetype_operator_type(instance):
    assert isinstance(instance.operator, stringtype)


@given(instance=mutatorenvironment::AttributeType_strategy)
def test_mutatorenvironment::attributetype_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=AttributeSet_strategy)
@settings(max_examples=50)
def test_attributeset_instantiation(instance):
    assert isinstance(instance, AttributeSet)

@given(instance=mutatorenvironment::AttributeUnset_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeunset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeUnset)

@given(instance=mutatorenvironment::AttributeSwap_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeswap_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeSwap)

@given(instance=mutatorenvironment::AttributeOperation_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeoperation_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeOperation)

@given(instance=mutatorenvironment::AttributeOperation_strategy)
def test_mutatorenvironment::attributeoperation_operator_type(instance):
    assert isinstance(instance.operator, stringtype)


@given(instance=mutatorenvironment::AttributeOperation_strategy)
def test_mutatorenvironment::attributeoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mutatorenvironment::AttributeCopy_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributecopy_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeCopy)

@given(instance=mutatorenvironment::AttributeReverse_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributereverse_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeReverse)

@given(instance=mutatorenvironment::AttributeScalar_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributescalar_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeScalar)

@given(instance=SpecificSelection_strategy)
@settings(max_examples=50)
def test_specificselection_instantiation(instance):
    assert isinstance(instance, SpecificSelection)

@given(instance=mutatorenvironment::SpecificClosureSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificclosureselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificClosureSelection)

@given(instance=mutatorenvironment::SpecificObjectSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificobjectselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificObjectSelection)

@given(instance=RandomSelection_strategy)
@settings(max_examples=50)
def test_randomselection_instantiation(instance):
    assert isinstance(instance, RandomSelection)

@given(instance=mutatorenvironment::RandomTypeSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomtypeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomTypeSelection)

@given(instance=mutatorenvironment::SpecificReferenceSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificreferenceselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificReferenceSelection)

@given(instance=DoubleType_strategy)
@settings(max_examples=50)
def test_doubletype_instantiation(instance):
    assert isinstance(instance, DoubleType)

@given(instance=mutatorenvironment::RandomDoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomdoubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomDoubleType)

@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_min_type(instance):
    assert isinstance(instance.min, float)


@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_max_type(instance):
    assert isinstance(instance.max, float)


@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_allowsNull_type(instance):
    assert isinstance(instance.allowsNull, booleantype)


@given(instance=mutatorenvironment::RandomDoubleType_strategy)
def test_mutatorenvironment::randomdoubletype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment::SpecificDoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificdoubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificDoubleType)

@given(instance=mutatorenvironment::SpecificDoubleType_strategy)
def test_mutatorenvironment::specificdoubletype_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=mutatorenvironment::SpecificDoubleType_strategy)
def test_mutatorenvironment::specificdoubletype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=mutatorenvironment::RandomIntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomintegertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomIntegerType)

@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_max_type(instance):
    assert isinstance(instance.max, integertype)


@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_allowsNull_type(instance):
    assert isinstance(instance.allowsNull, booleantype)


@given(instance=mutatorenvironment::RandomIntegerType_strategy)
def test_mutatorenvironment::randomintegertype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment::SpecificIntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificintegertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificIntegerType)

@given(instance=mutatorenvironment::SpecificIntegerType_strategy)
def test_mutatorenvironment::specificintegertype_value_type(instance):
    assert isinstance(instance.value, integertype)


@given(instance=mutatorenvironment::SpecificIntegerType_strategy)
def test_mutatorenvironment::specificintegertype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberType_strategy)
@settings(max_examples=50)
def test_numbertype_instantiation(instance):
    assert isinstance(instance, NumberType)

@given(instance=mutatorenvironment::MinValueType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::minvaluetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::MinValueType)

@given(instance=mutatorenvironment::RandomNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomnumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomNumberType)

@given(instance=mutatorenvironment::DoubleType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::doubletype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::DoubleType)

@given(instance=mutatorenvironment::MaxValueType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::maxvaluetype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::MaxValueType)

@given(instance=mutatorenvironment::IntegerType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::integertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::IntegerType)

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=mutatorenvironment::ReplaceStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::replacestringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReplaceStringType)

@given(instance=mutatorenvironment::ReplaceStringType_strategy)
def test_mutatorenvironment::replacestringtype_oldstring_type(instance):
    assert isinstance(instance.oldstring, stringtype)


@given(instance=mutatorenvironment::ReplaceStringType_strategy)
def test_mutatorenvironment::replacestringtype_oldstring_setter(instance):
    original = instance.oldstring
    instance.oldstring = original
    assert instance.oldstring == original

@given(instance=mutatorenvironment::ReplaceStringType_strategy)
def test_mutatorenvironment::replacestringtype_newstring_type(instance):
    assert isinstance(instance.newstring, stringtype)


@given(instance=mutatorenvironment::ReplaceStringType_strategy)
def test_mutatorenvironment::replacestringtype_newstring_setter(instance):
    original = instance.newstring
    instance.newstring = original
    assert instance.newstring == original

@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomstringnumbertype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomStringNumberType)

@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_allowsNull_type(instance):
    assert isinstance(instance.allowsNull, booleantype)


@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_max_type(instance):
    assert isinstance(instance.max, integertype)


@given(instance=mutatorenvironment::RandomStringNumberType_strategy)
def test_mutatorenvironment::randomstringnumbertype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::CatEndStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::catendstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CatEndStringType)

@given(instance=mutatorenvironment::CatEndStringType_strategy)
def test_mutatorenvironment::catendstringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::CatEndStringType_strategy)
def test_mutatorenvironment::catendstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::CatStartStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::catstartstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CatStartStringType)

@given(instance=mutatorenvironment::CatStartStringType_strategy)
def test_mutatorenvironment::catstartstringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::CatStartStringType_strategy)
def test_mutatorenvironment::catstartstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::UpperStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::upperstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::UpperStringType)

@given(instance=mutatorenvironment::UpperStringType_strategy)
def test_mutatorenvironment::upperstringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::UpperStringType_strategy)
def test_mutatorenvironment::upperstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::RandomStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomStringType)

@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_max_type(instance):
    assert isinstance(instance.max, integertype)


@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_allowsNull_type(instance):
    assert isinstance(instance.allowsNull, booleantype)


@given(instance=mutatorenvironment::RandomStringType_strategy)
def test_mutatorenvironment::randomstringtype_allowsNull_setter(instance):
    original = instance.allowsNull
    instance.allowsNull = original
    assert instance.allowsNull == original

@given(instance=mutatorenvironment::LowerStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::lowerstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::LowerStringType)

@given(instance=mutatorenvironment::LowerStringType_strategy)
def test_mutatorenvironment::lowerstringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::LowerStringType_strategy)
def test_mutatorenvironment::lowerstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::SpecificStringType_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificstringtype_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificStringType)

@given(instance=mutatorenvironment::SpecificStringType_strategy)
def test_mutatorenvironment::specificstringtype_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=mutatorenvironment::SpecificStringType_strategy)
def test_mutatorenvironment::specificstringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mutatorenvironment::ObjectEmitter_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::objectemitter_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ObjectEmitter)

@given(instance=mutatorenvironment::ObjectEmitter_strategy)
def test_mutatorenvironment::objectemitter_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::ObjectEmitter_strategy)
def test_mutatorenvironment::objectemitter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment::Source_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::source_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Source)

@given(instance=mutatorenvironment::Source_strategy)
def test_mutatorenvironment::source_path_type(instance):
    assert isinstance(instance.path, stringtype)


@given(instance=mutatorenvironment::Source_strategy)
def test_mutatorenvironment::source_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=mutatorenvironment::Program_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::program_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Program)

@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_exhaustive_type(instance):
    assert isinstance(instance.exhaustive, booleantype)


@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_exhaustive_setter(instance):
    original = instance.exhaustive
    instance.exhaustive = original
    assert instance.exhaustive == original

@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_num_type(instance):
    assert isinstance(instance.num, integertype)


@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_description_type(instance):
    assert isinstance(instance.description, stringtype)


@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_output_type(instance):
    assert isinstance(instance.output, stringtype)


@given(instance=mutatorenvironment::Program_strategy)
def test_mutatorenvironment::program_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=mutatorenvironment::Resource_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::resource_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Resource)

@given(instance=mutatorenvironment::Resource_strategy)
def test_mutatorenvironment::resource_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::Resource_strategy)
def test_mutatorenvironment::resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mutatorenvironment::Library_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::library_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Library)

@given(instance=mutatorenvironment::Constraint_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::constraint_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Constraint)

@given(instance=mutatorenvironment::Constraint_strategy)
def test_mutatorenvironment::constraint_id_type(instance):
    assert isinstance(instance.id, stringtype)


@given(instance=mutatorenvironment::Constraint_strategy)
def test_mutatorenvironment::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=mutatorenvironment::Constraint_strategy)
def test_mutatorenvironment::constraint_rules_type(instance):
    assert isinstance(instance.rules, stringtype)


@given(instance=mutatorenvironment::Constraint_strategy)
def test_mutatorenvironment::constraint_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=mutatorenvironment::Block_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::block_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Block)

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_max_type(instance):
    assert isinstance(instance.max, integertype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_description_type(instance):
    assert isinstance(instance.description, stringtype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_fixed_type(instance):
    assert isinstance(instance.fixed, integertype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_repeat_type(instance):
    assert isinstance(instance.repeat, stringtype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_repeat_setter(instance):
    original = instance.repeat
    instance.repeat = original
    assert instance.repeat == original

@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=mutatorenvironment::Block_strategy)
def test_mutatorenvironment::block_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ObSelectionStrategy_strategy)
@settings(max_examples=50)
def test_obselectionstrategy_instantiation(instance):
    assert isinstance(instance, ObSelectionStrategy)

@given(instance=mutatorenvironment::CompleteSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::completeselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CompleteSelection)

@given(instance=mutatorenvironment::TypedSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::typedselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::TypedSelection)

@given(instance=mutatorenvironment::SpecificSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::specificselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SpecificSelection)

@given(instance=mutatorenvironment::OtherSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::otherselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::OtherSelection)

@given(instance=mutatorenvironment::RandomSelection_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::randomselection_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RandomSelection)

@given(instance=mutatorenvironment::Expression_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::expression_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Expression)

@given(instance=mutatorenvironment::EReference_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::ereference_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::EReference)

@given(instance=mutatorenvironment::ReferenceSet_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::referenceset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ReferenceSet)

@given(instance=mutatorenvironment::AttributeSet_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::attributeset_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::AttributeSet)

@given(instance=Mutator_strategy)
@settings(max_examples=50)
def test_mutator_instantiation(instance):
    assert isinstance(instance, Mutator)

@given(instance=mutatorenvironment::ModifyTargetReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::modifytargetreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ModifyTargetReferenceMutator)

@given(instance=mutatorenvironment::ModifySourceReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::modifysourcereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ModifySourceReferenceMutator)

@given(instance=mutatorenvironment::CreateReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::createreferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CreateReferenceMutator)

@given(instance=mutatorenvironment::RemoveObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::removeobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RemoveObjectMutator)

@given(instance=mutatorenvironment::RetypeObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::retypeobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RetypeObjectMutator)

@given(instance=mutatorenvironment::SelectObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::selectobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SelectObjectMutator)

@given(instance=mutatorenvironment::CreateObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::createobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CreateObjectMutator)

@given(instance=mutatorenvironment::ModifyInformationMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::modifyinformationmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ModifyInformationMutator)

@given(instance=mutatorenvironment::CloneObjectMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::cloneobjectmutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CloneObjectMutator)

@given(instance=mutatorenvironment::CloneObjectMutator_strategy)
def test_mutatorenvironment::cloneobjectmutator_contents_type(instance):
    assert isinstance(instance.contents, booleantype)


@given(instance=mutatorenvironment::CloneObjectMutator_strategy)
def test_mutatorenvironment::cloneobjectmutator_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=mutatorenvironment::RemoveReferenceMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::removereferencemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::RemoveReferenceMutator)

@given(instance=mutatorenvironment::SelectSampleMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::selectsamplemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::SelectSampleMutator)

@given(instance=mutatorenvironment::SelectSampleMutator_strategy)
def test_mutatorenvironment::selectsamplemutator_clause_type(instance):
    assert isinstance(instance.clause, stringtype)


@given(instance=mutatorenvironment::SelectSampleMutator_strategy)
def test_mutatorenvironment::selectsamplemutator_clause_setter(instance):
    original = instance.clause
    instance.clause = original
    assert instance.clause == original

@given(instance=mutatorenvironment::CompositeMutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::compositemutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::CompositeMutator)

@given(instance=ObjectEmitter_strategy)
@settings(max_examples=50)
def test_objectemitter_instantiation(instance):
    assert isinstance(instance, ObjectEmitter)

@given(instance=mutatorenvironment::ObSelectionStrategy_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::obselectionstrategy_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::ObSelectionStrategy)

@given(instance=mutatorenvironment::ObSelectionStrategy_strategy)
def test_mutatorenvironment::obselectionstrategy_resource_type(instance):
    assert isinstance(instance.resource, stringtype)


@given(instance=mutatorenvironment::ObSelectionStrategy_strategy)
def test_mutatorenvironment::obselectionstrategy_resource_setter(instance):
    original = instance.resource
    instance.resource = original
    assert instance.resource == original

@given(instance=mutatorenvironment::EClass_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::eclass_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::EClass)

@given(instance=mutatorenvironment::Load_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::load_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Load)

@given(instance=mutatorenvironment::Load_strategy)
def test_mutatorenvironment::load_file_type(instance):
    assert isinstance(instance.file, stringtype)


@given(instance=mutatorenvironment::Load_strategy)
def test_mutatorenvironment::load_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=mutatorenvironment::Mutator_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::mutator_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Mutator)

@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_fixed_type(instance):
    assert isinstance(instance.fixed, integertype)


@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_fixed_setter(instance):
    original = instance.fixed
    instance.fixed = original
    assert instance.fixed == original

@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_min_type(instance):
    assert isinstance(instance.min, integertype)


@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_max_type(instance):
    assert isinstance(instance.max, integertype)


@given(instance=mutatorenvironment::Mutator_strategy)
def test_mutatorenvironment::mutator_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=mutatorenvironment::Definition_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::definition_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::Definition)

@given(instance=mutatorenvironment::Definition_strategy)
def test_mutatorenvironment::definition_metamodel_type(instance):
    assert isinstance(instance.metamodel, stringtype)


@given(instance=mutatorenvironment::Definition_strategy)
def test_mutatorenvironment::definition_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original

@given(instance=mutatorenvironment::MutatorEnvironment_strategy)
@settings(max_examples=50)
def test_mutatorenvironment::mutatorenvironment_instantiation(instance):
    assert isinstance(instance, mutatorenvironment::MutatorEnvironment)
