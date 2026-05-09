import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    LogExp,
    AnonymousTupleLiteralPart,
    essentialocl::LoopExp,
    DictLiteralPart,
    ImperativeLoopExp,
    JTLMM::imperativeocl::ForExp,
    JTLMM::imperativeocl::CollectorExp,
    JTLMM::imperativeocl::ImperativeIterateExp,
    ObjectTemplateExp,
    AltExp,
    imperativeocl::ImperativeExpression,
    JTLMM::imperativeocl::ImperativeLoopExp,
    ImperativeExpression,
    JTLMM::imperativeocl::TryExp,
    JTLMM::imperativeocl::ComputeExp,
    JTLMM::imperativeocl::BlockExp,
    JTLMM::imperativeocl::AltExp,
    JTLMM::imperativeocl::RaiseExp,
    JTLMM::imperativeocl::UnpackExp,
    JTLMM::imperativeocl::TupleExp,
    JTLMM::imperativeocl::ReturnExp,
    JTLMM::imperativeocl::ContinueExp,
    JTLMM::imperativeocl::AssertExp,
    JTLMM::imperativeocl::LogExp,
    JTLMM::imperativeocl::InstantiationExp,
    JTLMM::imperativeocl::BreakExp,
    JTLMM::imperativeocl::VariableInitExp,
    JTLMM::imperativeocl::WhileExp,
    JTLMM::imperativeocl::UnlinkExp,
    JTLMM::imperativeocl::AssignExp,
    CollectionType,
    JTLMM::imperativeocl::ListType,
    JTLMM::imperativeocl::DictionaryType,
    JTLMM::essentialocl::BagType,
    TupleLiteralExp,
    CallExp,
    JTLMM::essentialocl::FeaturePropertyCall,
    JTLMM::essentialocl::OpaqueExpression,
    AssignExp,
    PropertyTemplateItem,
    emof::Type,
    emof::DataType,
    JTLMM::essentialocl::SetType,
    JTLMM::essentialocl::SequenceType,
    JTLMM::essentialocl::OrderedSetType,
    OpaqueExpression,
    JTLMM::essentialocl::ExpressionInOcl,
    TupleLiteralPart,
    CollectionLiteralExp,
    CollectionLiteralPart,
    JTLMM::essentialocl::CollectionRange,
    JTLMM::essentialocl::CollectionItem,
    LiteralExp,
    JTLMM::essentialocl::EnumLiteralExp,
    JTLMM::essentialocl::TupleLiteralExp,
    JTLMM::template::TemplateExp,
    JTLMM::essentialocl::InvalidLiteralExp,
    JTLMM::imperativeocl::AnonymousTupleLiteralExp,
    JTLMM::essentialocl::NullLiteralExp,
    JTLMM::essentialocl::CollectionLiteralExp,
    JTLMM::imperativeocl::DictLiteralExp,
    JTLMM::essentialocl::PrimitiveLiteralExp,
    ComputeExp,
    LetExp,
    LoopExp,
    JTLMM::essentialocl::IterateExp,
    JTLMM::essentialocl::IteratorExp,
    essentialocl::OclExpression,
    essentialocl::CallExp,
    JTLMM::imperativeocl::SwitchExp,
    JTLMM::essentialocl::LoopExp,
    FeaturePropertyCall,
    JTLMM::essentialocl::OperationCallExp,
    JTLMM::essentialocl::PropertyCallExp,
    PrimitiveLiteralExp,
    JTLMM::essentialocl::StringLiteralExp,
    JTLMM::essentialocl::NumericLiteralExp,
    JTLMM::essentialocl::BooleanLiteralExp,
    OclExpression,
    JTLMM::essentialocl::TypeExp,
    JTLMM::imperativeocl::ImperativeExpression,
    JTLMM::essentialocl::CallExp,
    JTLMM::essentialocl::LetExp,
    JTLMM::essentialocl::LiteralExp,
    JTLMM::essentialocl::VariableExp,
    TemplateExp,
    JTLMM::template::CollectionTemplateExp,
    JTLMM::template::ObjectTemplateExp,
    Predicate,
    JTLMM::essentialocl::IfExp,
    NumericLiteralExp,
    JTLMM::essentialocl::RealLiteralExp,
    JTLMM::essentialocl::IntegerLiteralExp,
    JTLMM::essentialocl::UnlimitedNaturalExp,
    TryExp,
    TypedElement,
    JTLMM::essentialocl::Variable,
    JTLMM::essentialocl::CollectionLiteralPart,
    JTLMM::essentialocl::TupleLiteralPart,
    JTLMM::essentialocl::OclExpression,
    Pattern,
    Domain,
    Transformation,
    Relation,
    Model,
    emof::Package,
    emof::Class,
    JTLMM::essentialocl::AnyType,
    JTLMM::essentialocl::TupleType,
    JTLMM::JTL::Transformation,
    Extent,
    JTLMM::emof::URIExtent,
    Variable,
    Package,
    NamedElement,
    JTLMM::emof::TypedElement,
    JTLMM::emof::Type,
    JTLMM::JTL::Relation,
    JTLMM::JTL::Domain,
    JTLMM::JTL::Model,
    JTLMM::emof::Package,
    JTLMM::emof::MultiplicityElement,
    Parameter,
    emof::TypedElement,
    emof::MultiplicityElement,
    JTLMM::emof::Operation,
    JTLMM::emof::Object,
    EnumerationLiteral,
    DataType,
    JTLMM::emof::PrimitiveType,
    JTLMM::essentialocl::CollectionType,
    JTLMM::emof::Enumeration,
    JTLMM::emof::Property,
    Enumeration,
    JTLMM::emof::EnumerationLiteral,
    JTLMM::emof::Parameter,
    Element,
    JTLMM::template::PropertyTemplateItem,
    JTLMM::imperativeocl::AnonymousTupleLiteralPart,
    JTLMM::emof::Comment,
    JTLMM::JTL::Predicate,
    JTLMM::emof::NamedElement,
    JTLMM::JTL::Pattern,
    JTLMM::imperativeocl::DictLiteralPart,
    JTLMM::emof::Tag,
    Comment,
    Tag,
    Object,
    JTLMM::emof::Extent,
    JTLMM::emof::Element,
    Class,
    JTLMM::imperativeocl::AnonymousTupleType,
    JTLMM::imperativeocl::Typedef,
    Operation,
    Property,
    Type,
    JTLMM::imperativeocl::TemplateParameterType,
    JTLMM::essentialocl::InvalidType,
    JTLMM::essentialocl::VoidType,
    JTLMM::emof::DataType,
    JTLMM::emof::Class,
    CollectionKind,
    SeverityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(essentialocl::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ForExp)


def test_jtlmm::imperativeocl::forexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ForExp.__init__)


def test_jtlmm::imperativeocl::forexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::collectorexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::CollectorExp)


def test_jtlmm::imperativeocl::collectorexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::CollectorExp.__init__)


def test_jtlmm::imperativeocl::collectorexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ImperativeIterateExp)


def test_jtlmm::imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ImperativeIterateExp.__init__)


def test_jtlmm::imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_altexp_is_not_abstract():
    assert not inspect.isabstract(AltExp)


def test_altexp_constructor_exists():
    assert callable(AltExp.__init__)


def test_altexp_constructor_args():
    sig = inspect.signature(AltExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(imperativeocl::ImperativeExpression)


def test_imperativeocl::imperativeexpression_constructor_exists():
    assert callable(imperativeocl::ImperativeExpression.__init__)


def test_imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ImperativeLoopExp)


def test_jtlmm::imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ImperativeLoopExp.__init__)


def test_jtlmm::imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::TryExp)


def test_jtlmm::imperativeocl::tryexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::TryExp.__init__)


def test_jtlmm::imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ComputeExp)


def test_jtlmm::imperativeocl::computeexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ComputeExp.__init__)


def test_jtlmm::imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::BlockExp)


def test_jtlmm::imperativeocl::blockexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::BlockExp.__init__)


def test_jtlmm::imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AltExp)


def test_jtlmm::imperativeocl::altexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::AltExp.__init__)


def test_jtlmm::imperativeocl::altexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AltExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::RaiseExp)


def test_jtlmm::imperativeocl::raiseexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::RaiseExp.__init__)


def test_jtlmm::imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::UnpackExp)


def test_jtlmm::imperativeocl::unpackexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::UnpackExp.__init__)


def test_jtlmm::imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::TupleExp)


def test_jtlmm::imperativeocl::tupleexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::TupleExp.__init__)


def test_jtlmm::imperativeocl::tupleexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ReturnExp)


def test_jtlmm::imperativeocl::returnexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ReturnExp.__init__)


def test_jtlmm::imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ContinueExp)


def test_jtlmm::imperativeocl::continueexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::ContinueExp.__init__)


def test_jtlmm::imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AssertExp)


def test_jtlmm::imperativeocl::assertexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::AssertExp.__init__)


def test_jtlmm::imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_jtlmm::imperativeocl::assertexp_has_severity():
    assert hasattr(JTLMM::imperativeocl::AssertExp, "severity")
    descriptor = None
    for klass in JTLMM::imperativeocl::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::LogExp)


def test_jtlmm::imperativeocl::logexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::LogExp.__init__)


def test_jtlmm::imperativeocl::logexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "level" in params, "Missing parameter 'level'"

def test_jtlmm::imperativeocl::logexp_has_text():
    assert hasattr(JTLMM::imperativeocl::LogExp, "text")
    descriptor = None
    for klass in JTLMM::imperativeocl::LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::imperativeocl::logexp_has_level():
    assert hasattr(JTLMM::imperativeocl::LogExp, "level")
    descriptor = None
    for klass in JTLMM::imperativeocl::LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::InstantiationExp)


def test_jtlmm::imperativeocl::instantiationexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::InstantiationExp.__init__)


def test_jtlmm::imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::BreakExp)


def test_jtlmm::imperativeocl::breakexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::BreakExp.__init__)


def test_jtlmm::imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::VariableInitExp)


def test_jtlmm::imperativeocl::variableinitexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::VariableInitExp.__init__)


def test_jtlmm::imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_jtlmm::imperativeocl::variableinitexp_has_withResult():
    assert hasattr(JTLMM::imperativeocl::VariableInitExp, "withResult")
    descriptor = None
    for klass in JTLMM::imperativeocl::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::WhileExp)


def test_jtlmm::imperativeocl::whileexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::WhileExp.__init__)


def test_jtlmm::imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::UnlinkExp)


def test_jtlmm::imperativeocl::unlinkexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::UnlinkExp.__init__)


def test_jtlmm::imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AssignExp)


def test_jtlmm::imperativeocl::assignexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::AssignExp.__init__)


def test_jtlmm::imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_jtlmm::imperativeocl::assignexp_has_isReset():
    assert hasattr(JTLMM::imperativeocl::AssignExp, "isReset")
    descriptor = None
    for klass in JTLMM::imperativeocl::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ListType)


def test_jtlmm::imperativeocl::listtype_constructor_exists():
    assert callable(JTLMM::imperativeocl::ListType.__init__)


def test_jtlmm::imperativeocl::listtype_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::DictionaryType)


def test_jtlmm::imperativeocl::dictionarytype_constructor_exists():
    assert callable(JTLMM::imperativeocl::DictionaryType.__init__)


def test_jtlmm::imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::BagType)


def test_jtlmm::essentialocl::bagtype_constructor_exists():
    assert callable(JTLMM::essentialocl::BagType.__init__)


def test_jtlmm::essentialocl::bagtype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::BagType.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralExp)


def test_tupleliteralexp_constructor_exists():
    assert callable(TupleLiteralExp.__init__)


def test_tupleliteralexp_constructor_args():
    sig = inspect.signature(TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::FeaturePropertyCall)


def test_jtlmm::essentialocl::featurepropertycall_constructor_exists():
    assert callable(JTLMM::essentialocl::FeaturePropertyCall.__init__)


def test_jtlmm::essentialocl::featurepropertycall_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::OpaqueExpression)


def test_jtlmm::essentialocl::opaqueexpression_constructor_exists():
    assert callable(JTLMM::essentialocl::OpaqueExpression.__init__)


def test_jtlmm::essentialocl::opaqueexpression_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignexp_is_not_abstract():
    assert not inspect.isabstract(AssignExp)


def test_assignexp_constructor_exists():
    assert callable(AssignExp.__init__)


def test_assignexp_constructor_args():
    sig = inspect.signature(AssignExp.__init__)
    params = list(sig.parameters.keys())



def test_propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(PropertyTemplateItem)


def test_propertytemplateitem_constructor_exists():
    assert callable(PropertyTemplateItem.__init__)


def test_propertytemplateitem_constructor_args():
    sig = inspect.signature(PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_emof::type_is_not_abstract():
    assert not inspect.isabstract(emof::Type)


def test_emof::type_constructor_exists():
    assert callable(emof::Type.__init__)


def test_emof::type_constructor_args():
    sig = inspect.signature(emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_emof::datatype_is_not_abstract():
    assert not inspect.isabstract(emof::DataType)


def test_emof::datatype_constructor_exists():
    assert callable(emof::DataType.__init__)


def test_emof::datatype_constructor_args():
    sig = inspect.signature(emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::SetType)


def test_jtlmm::essentialocl::settype_constructor_exists():
    assert callable(JTLMM::essentialocl::SetType.__init__)


def test_jtlmm::essentialocl::settype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::SequenceType)


def test_jtlmm::essentialocl::sequencetype_constructor_exists():
    assert callable(JTLMM::essentialocl::SequenceType.__init__)


def test_jtlmm::essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::OrderedSetType)


def test_jtlmm::essentialocl::orderedsettype_constructor_exists():
    assert callable(JTLMM::essentialocl::OrderedSetType.__init__)


def test_jtlmm::essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::ExpressionInOcl)


def test_jtlmm::essentialocl::expressioninocl_constructor_exists():
    assert callable(JTLMM::essentialocl::ExpressionInOcl.__init__)


def test_jtlmm::essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CollectionRange)


def test_jtlmm::essentialocl::collectionrange_constructor_exists():
    assert callable(JTLMM::essentialocl::CollectionRange.__init__)


def test_jtlmm::essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CollectionItem)


def test_jtlmm::essentialocl::collectionitem_constructor_exists():
    assert callable(JTLMM::essentialocl::CollectionItem.__init__)


def test_jtlmm::essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::EnumLiteralExp)


def test_jtlmm::essentialocl::enumliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::EnumLiteralExp.__init__)


def test_jtlmm::essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::TupleLiteralExp)


def test_jtlmm::essentialocl::tupleliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::TupleLiteralExp.__init__)


def test_jtlmm::essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::template::templateexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::template::TemplateExp)


def test_jtlmm::template::templateexp_constructor_exists():
    assert callable(JTLMM::template::TemplateExp.__init__)


def test_jtlmm::template::templateexp_constructor_args():
    sig = inspect.signature(JTLMM::template::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::InvalidLiteralExp)


def test_jtlmm::essentialocl::invalidliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::InvalidLiteralExp.__init__)


def test_jtlmm::essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AnonymousTupleLiteralExp)


def test_jtlmm::imperativeocl::anonymoustupleliteralexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::AnonymousTupleLiteralExp.__init__)


def test_jtlmm::imperativeocl::anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::NullLiteralExp)


def test_jtlmm::essentialocl::nullliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::NullLiteralExp.__init__)


def test_jtlmm::essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CollectionLiteralExp)


def test_jtlmm::essentialocl::collectionliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::CollectionLiteralExp.__init__)


def test_jtlmm::essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtlmm::essentialocl::collectionliteralexp_has_kind():
    assert hasattr(JTLMM::essentialocl::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in JTLMM::essentialocl::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::DictLiteralExp)


def test_jtlmm::imperativeocl::dictliteralexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::DictLiteralExp.__init__)


def test_jtlmm::imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::PrimitiveLiteralExp)


def test_jtlmm::essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::PrimitiveLiteralExp.__init__)


def test_jtlmm::essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_computeexp_is_not_abstract():
    assert not inspect.isabstract(ComputeExp)


def test_computeexp_constructor_exists():
    assert callable(ComputeExp.__init__)


def test_computeexp_constructor_args():
    sig = inspect.signature(ComputeExp.__init__)
    params = list(sig.parameters.keys())



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::IterateExp)


def test_jtlmm::essentialocl::iterateexp_constructor_exists():
    assert callable(JTLMM::essentialocl::IterateExp.__init__)


def test_jtlmm::essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::IteratorExp)


def test_jtlmm::essentialocl::iteratorexp_constructor_exists():
    assert callable(JTLMM::essentialocl::IteratorExp.__init__)


def test_jtlmm::essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(essentialocl::OclExpression)


def test_essentialocl::oclexpression_constructor_exists():
    assert callable(essentialocl::OclExpression.__init__)


def test_essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::CallExp)


def test_essentialocl::callexp_constructor_exists():
    assert callable(essentialocl::CallExp.__init__)


def test_essentialocl::callexp_constructor_args():
    sig = inspect.signature(essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::SwitchExp)


def test_jtlmm::imperativeocl::switchexp_constructor_exists():
    assert callable(JTLMM::imperativeocl::SwitchExp.__init__)


def test_jtlmm::imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::LoopExp)


def test_jtlmm::essentialocl::loopexp_constructor_exists():
    assert callable(JTLMM::essentialocl::LoopExp.__init__)


def test_jtlmm::essentialocl::loopexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::OperationCallExp)


def test_jtlmm::essentialocl::operationcallexp_constructor_exists():
    assert callable(JTLMM::essentialocl::OperationCallExp.__init__)


def test_jtlmm::essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::PropertyCallExp)


def test_jtlmm::essentialocl::propertycallexp_constructor_exists():
    assert callable(JTLMM::essentialocl::PropertyCallExp.__init__)


def test_jtlmm::essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::StringLiteralExp)


def test_jtlmm::essentialocl::stringliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::StringLiteralExp.__init__)


def test_jtlmm::essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_jtlmm::essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(JTLMM::essentialocl::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in JTLMM::essentialocl::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::NumericLiteralExp)


def test_jtlmm::essentialocl::numericliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::NumericLiteralExp.__init__)


def test_jtlmm::essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::BooleanLiteralExp)


def test_jtlmm::essentialocl::booleanliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::BooleanLiteralExp.__init__)


def test_jtlmm::essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_jtlmm::essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(JTLMM::essentialocl::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in JTLMM::essentialocl::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::TypeExp)


def test_jtlmm::essentialocl::typeexp_constructor_exists():
    assert callable(JTLMM::essentialocl::TypeExp.__init__)


def test_jtlmm::essentialocl::typeexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::ImperativeExpression)


def test_jtlmm::imperativeocl::imperativeexpression_constructor_exists():
    assert callable(JTLMM::imperativeocl::ImperativeExpression.__init__)


def test_jtlmm::imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CallExp)


def test_jtlmm::essentialocl::callexp_constructor_exists():
    assert callable(JTLMM::essentialocl::CallExp.__init__)


def test_jtlmm::essentialocl::callexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::LetExp)


def test_jtlmm::essentialocl::letexp_constructor_exists():
    assert callable(JTLMM::essentialocl::LetExp.__init__)


def test_jtlmm::essentialocl::letexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::LiteralExp)


def test_jtlmm::essentialocl::literalexp_constructor_exists():
    assert callable(JTLMM::essentialocl::LiteralExp.__init__)


def test_jtlmm::essentialocl::literalexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::VariableExp)


def test_jtlmm::essentialocl::variableexp_constructor_exists():
    assert callable(JTLMM::essentialocl::VariableExp.__init__)


def test_jtlmm::essentialocl::variableexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::template::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::template::CollectionTemplateExp)


def test_jtlmm::template::collectiontemplateexp_constructor_exists():
    assert callable(JTLMM::template::CollectionTemplateExp.__init__)


def test_jtlmm::template::collectiontemplateexp_constructor_args():
    sig = inspect.signature(JTLMM::template::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtlmm::template::collectiontemplateexp_has_kind():
    assert hasattr(JTLMM::template::CollectionTemplateExp, "kind")
    descriptor = None
    for klass in JTLMM::template::CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::template::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::template::ObjectTemplateExp)


def test_jtlmm::template::objecttemplateexp_constructor_exists():
    assert callable(JTLMM::template::ObjectTemplateExp.__init__)


def test_jtlmm::template::objecttemplateexp_constructor_args():
    sig = inspect.signature(JTLMM::template::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredClass" in params, "Missing parameter 'referredClass'"

def test_jtlmm::template::objecttemplateexp_has_referredClass():
    assert hasattr(JTLMM::template::ObjectTemplateExp, "referredClass")
    descriptor = None
    for klass in JTLMM::template::ObjectTemplateExp.__mro__:
        if "referredClass" in klass.__dict__:
            descriptor = klass.__dict__["referredClass"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::IfExp)


def test_jtlmm::essentialocl::ifexp_constructor_exists():
    assert callable(JTLMM::essentialocl::IfExp.__init__)


def test_jtlmm::essentialocl::ifexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::RealLiteralExp)


def test_jtlmm::essentialocl::realliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::RealLiteralExp.__init__)


def test_jtlmm::essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_jtlmm::essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(JTLMM::essentialocl::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in JTLMM::essentialocl::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::IntegerLiteralExp)


def test_jtlmm::essentialocl::integerliteralexp_constructor_exists():
    assert callable(JTLMM::essentialocl::IntegerLiteralExp.__init__)


def test_jtlmm::essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_jtlmm::essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(JTLMM::essentialocl::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in JTLMM::essentialocl::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::UnlimitedNaturalExp)


def test_jtlmm::essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(JTLMM::essentialocl::UnlimitedNaturalExp.__init__)


def test_jtlmm::essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_jtlmm::essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(JTLMM::essentialocl::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in JTLMM::essentialocl::UnlimitedNaturalExp.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_tryexp_is_not_abstract():
    assert not inspect.isabstract(TryExp)


def test_tryexp_constructor_exists():
    assert callable(TryExp.__init__)


def test_tryexp_constructor_args():
    sig = inspect.signature(TryExp.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::Variable)


def test_jtlmm::essentialocl::variable_constructor_exists():
    assert callable(JTLMM::essentialocl::Variable.__init__)


def test_jtlmm::essentialocl::variable_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CollectionLiteralPart)


def test_jtlmm::essentialocl::collectionliteralpart_constructor_exists():
    assert callable(JTLMM::essentialocl::CollectionLiteralPart.__init__)


def test_jtlmm::essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::TupleLiteralPart)


def test_jtlmm::essentialocl::tupleliteralpart_constructor_exists():
    assert callable(JTLMM::essentialocl::TupleLiteralPart.__init__)


def test_jtlmm::essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::OclExpression)


def test_jtlmm::essentialocl::oclexpression_constructor_exists():
    assert callable(JTLMM::essentialocl::OclExpression.__init__)


def test_jtlmm::essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_transformation_is_not_abstract():
    assert not inspect.isabstract(Transformation)


def test_transformation_constructor_exists():
    assert callable(Transformation.__init__)


def test_transformation_constructor_args():
    sig = inspect.signature(Transformation.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())



def test_emof::package_is_not_abstract():
    assert not inspect.isabstract(emof::Package)


def test_emof::package_constructor_exists():
    assert callable(emof::Package.__init__)


def test_emof::package_constructor_args():
    sig = inspect.signature(emof::Package.__init__)
    params = list(sig.parameters.keys())



def test_emof::class_is_not_abstract():
    assert not inspect.isabstract(emof::Class)


def test_emof::class_constructor_exists():
    assert callable(emof::Class.__init__)


def test_emof::class_constructor_args():
    sig = inspect.signature(emof::Class.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::AnyType)


def test_jtlmm::essentialocl::anytype_constructor_exists():
    assert callable(JTLMM::essentialocl::AnyType.__init__)


def test_jtlmm::essentialocl::anytype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::TupleType)


def test_jtlmm::essentialocl::tupletype_constructor_exists():
    assert callable(JTLMM::essentialocl::TupleType.__init__)


def test_jtlmm::essentialocl::tupletype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::jtl::transformation_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Transformation)


def test_jtlmm::jtl::transformation_constructor_exists():
    assert callable(JTLMM::JTL::Transformation.__init__)


def test_jtlmm::jtl::transformation_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::URIExtent)


def test_jtlmm::emof::uriextent_constructor_exists():
    assert callable(JTLMM::emof::URIExtent.__init__)


def test_jtlmm::emof::uriextent_constructor_args():
    sig = inspect.signature(JTLMM::emof::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::TypedElement)


def test_jtlmm::emof::typedelement_constructor_exists():
    assert callable(JTLMM::emof::TypedElement.__init__)


def test_jtlmm::emof::typedelement_constructor_args():
    sig = inspect.signature(JTLMM::emof::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jtlmm::emof::typedelement_has_type():
    assert hasattr(JTLMM::emof::TypedElement, "type")
    descriptor = None
    for klass in JTLMM::emof::TypedElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::emof::type_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Type)


def test_jtlmm::emof::type_constructor_exists():
    assert callable(JTLMM::emof::Type.__init__)


def test_jtlmm::emof::type_constructor_args():
    sig = inspect.signature(JTLMM::emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::jtl::relation_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Relation)


def test_jtlmm::jtl::relation_constructor_exists():
    assert callable(JTLMM::JTL::Relation.__init__)


def test_jtlmm::jtl::relation_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_jtlmm::jtl::relation_has_isTopLevel():
    assert hasattr(JTLMM::JTL::Relation, "isTopLevel")
    descriptor = None
    for klass in JTLMM::JTL::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::jtl::domain_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Domain)


def test_jtlmm::jtl::domain_constructor_exists():
    assert callable(JTLMM::JTL::Domain.__init__)


def test_jtlmm::jtl::domain_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"

def test_jtlmm::jtl::domain_has_isEnforceable():
    assert hasattr(JTLMM::JTL::Domain, "isEnforceable")
    descriptor = None
    for klass in JTLMM::JTL::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::jtl::domain_has_isCheckable():
    assert hasattr(JTLMM::JTL::Domain, "isCheckable")
    descriptor = None
    for klass in JTLMM::JTL::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::jtl::model_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Model)


def test_jtlmm::jtl::model_constructor_exists():
    assert callable(JTLMM::JTL::Model.__init__)


def test_jtlmm::jtl::model_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Model.__init__)
    params = list(sig.parameters.keys())
    assert "usedPackage" in params, "Missing parameter 'usedPackage'"

def test_jtlmm::jtl::model_has_usedPackage():
    assert hasattr(JTLMM::JTL::Model, "usedPackage")
    descriptor = None
    for klass in JTLMM::JTL::Model.__mro__:
        if "usedPackage" in klass.__dict__:
            descriptor = klass.__dict__["usedPackage"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::emof::package_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Package)


def test_jtlmm::emof::package_constructor_exists():
    assert callable(JTLMM::emof::Package.__init__)


def test_jtlmm::emof::package_constructor_args():
    sig = inspect.signature(JTLMM::emof::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_jtlmm::emof::package_has_uri():
    assert hasattr(JTLMM::emof::Package, "uri")
    descriptor = None
    for klass in JTLMM::emof::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::MultiplicityElement)


def test_jtlmm::emof::multiplicityelement_constructor_exists():
    assert callable(JTLMM::emof::MultiplicityElement.__init__)


def test_jtlmm::emof::multiplicityelement_constructor_args():
    sig = inspect.signature(JTLMM::emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_jtlmm::emof::multiplicityelement_has_isUnique():
    assert hasattr(JTLMM::emof::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in JTLMM::emof::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::multiplicityelement_has_lower():
    assert hasattr(JTLMM::emof::MultiplicityElement, "lower")
    descriptor = None
    for klass in JTLMM::emof::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::multiplicityelement_has_isOrdered():
    assert hasattr(JTLMM::emof::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in JTLMM::emof::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::multiplicityelement_has_upper():
    assert hasattr(JTLMM::emof::MultiplicityElement, "upper")
    descriptor = None
    for klass in JTLMM::emof::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(emof::TypedElement)


def test_emof::typedelement_constructor_exists():
    assert callable(emof::TypedElement.__init__)


def test_emof::typedelement_constructor_args():
    sig = inspect.signature(emof::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(emof::MultiplicityElement)


def test_emof::multiplicityelement_constructor_exists():
    assert callable(emof::MultiplicityElement.__init__)


def test_emof::multiplicityelement_constructor_args():
    sig = inspect.signature(emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::operation_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Operation)


def test_jtlmm::emof::operation_constructor_exists():
    assert callable(JTLMM::emof::Operation.__init__)


def test_jtlmm::emof::operation_constructor_args():
    sig = inspect.signature(JTLMM::emof::Operation.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::object_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Object)


def test_jtlmm::emof::object_constructor_exists():
    assert callable(JTLMM::emof::Object.__init__)


def test_jtlmm::emof::object_constructor_args():
    sig = inspect.signature(JTLMM::emof::Object.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::PrimitiveType)


def test_jtlmm::emof::primitivetype_constructor_exists():
    assert callable(JTLMM::emof::PrimitiveType.__init__)


def test_jtlmm::emof::primitivetype_constructor_args():
    sig = inspect.signature(JTLMM::emof::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::CollectionType)


def test_jtlmm::essentialocl::collectiontype_constructor_exists():
    assert callable(JTLMM::essentialocl::CollectionType.__init__)


def test_jtlmm::essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Enumeration)


def test_jtlmm::emof::enumeration_constructor_exists():
    assert callable(JTLMM::emof::Enumeration.__init__)


def test_jtlmm::emof::enumeration_constructor_args():
    sig = inspect.signature(JTLMM::emof::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::property_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Property)


def test_jtlmm::emof::property_constructor_exists():
    assert callable(JTLMM::emof::Property.__init__)


def test_jtlmm::emof::property_constructor_args():
    sig = inspect.signature(JTLMM::emof::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_jtlmm::emof::property_has_isDerived():
    assert hasattr(JTLMM::emof::Property, "isDerived")
    descriptor = None
    for klass in JTLMM::emof::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::property_has_default():
    assert hasattr(JTLMM::emof::Property, "default")
    descriptor = None
    for klass in JTLMM::emof::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::property_has_isComposite():
    assert hasattr(JTLMM::emof::Property, "isComposite")
    descriptor = None
    for klass in JTLMM::emof::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::property_has_isId():
    assert hasattr(JTLMM::emof::Property, "isId")
    descriptor = None
    for klass in JTLMM::emof::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::property_has_isReadOnly():
    assert hasattr(JTLMM::emof::Property, "isReadOnly")
    descriptor = None
    for klass in JTLMM::emof::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::EnumerationLiteral)


def test_jtlmm::emof::enumerationliteral_constructor_exists():
    assert callable(JTLMM::emof::EnumerationLiteral.__init__)


def test_jtlmm::emof::enumerationliteral_constructor_args():
    sig = inspect.signature(JTLMM::emof::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::parameter_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Parameter)


def test_jtlmm::emof::parameter_constructor_exists():
    assert callable(JTLMM::emof::Parameter.__init__)


def test_jtlmm::emof::parameter_constructor_args():
    sig = inspect.signature(JTLMM::emof::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::template::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(JTLMM::template::PropertyTemplateItem)


def test_jtlmm::template::propertytemplateitem_constructor_exists():
    assert callable(JTLMM::template::PropertyTemplateItem.__init__)


def test_jtlmm::template::propertytemplateitem_constructor_args():
    sig = inspect.signature(JTLMM::template::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AnonymousTupleLiteralPart)


def test_jtlmm::imperativeocl::anonymoustupleliteralpart_constructor_exists():
    assert callable(JTLMM::imperativeocl::AnonymousTupleLiteralPart.__init__)


def test_jtlmm::imperativeocl::anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::comment_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Comment)


def test_jtlmm::emof::comment_constructor_exists():
    assert callable(JTLMM::emof::Comment.__init__)


def test_jtlmm::emof::comment_constructor_args():
    sig = inspect.signature(JTLMM::emof::Comment.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::jtl::predicate_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Predicate)


def test_jtlmm::jtl::predicate_constructor_exists():
    assert callable(JTLMM::JTL::Predicate.__init__)


def test_jtlmm::jtl::predicate_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::NamedElement)


def test_jtlmm::emof::namedelement_constructor_exists():
    assert callable(JTLMM::emof::NamedElement.__init__)


def test_jtlmm::emof::namedelement_constructor_args():
    sig = inspect.signature(JTLMM::emof::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jtlmm::emof::namedelement_has_name():
    assert hasattr(JTLMM::emof::NamedElement, "name")
    descriptor = None
    for klass in JTLMM::emof::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::jtl::pattern_is_not_abstract():
    assert not inspect.isabstract(JTLMM::JTL::Pattern)


def test_jtlmm::jtl::pattern_constructor_exists():
    assert callable(JTLMM::JTL::Pattern.__init__)


def test_jtlmm::jtl::pattern_constructor_args():
    sig = inspect.signature(JTLMM::JTL::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::DictLiteralPart)


def test_jtlmm::imperativeocl::dictliteralpart_constructor_exists():
    assert callable(JTLMM::imperativeocl::DictLiteralPart.__init__)


def test_jtlmm::imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::tag_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Tag)


def test_jtlmm::emof::tag_constructor_exists():
    assert callable(JTLMM::emof::Tag.__init__)


def test_jtlmm::emof::tag_constructor_args():
    sig = inspect.signature(JTLMM::emof::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_jtlmm::emof::tag_has_value():
    assert hasattr(JTLMM::emof::Tag, "value")
    descriptor = None
    for klass in JTLMM::emof::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_jtlmm::emof::tag_has_name():
    assert hasattr(JTLMM::emof::Tag, "name")
    descriptor = None
    for klass in JTLMM::emof::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_comment_is_not_abstract():
    assert not inspect.isabstract(Comment)


def test_comment_constructor_exists():
    assert callable(Comment.__init__)


def test_comment_constructor_args():
    sig = inspect.signature(Comment.__init__)
    params = list(sig.parameters.keys())



def test_tag_is_not_abstract():
    assert not inspect.isabstract(Tag)


def test_tag_constructor_exists():
    assert callable(Tag.__init__)


def test_tag_constructor_args():
    sig = inspect.signature(Tag.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::extent_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Extent)


def test_jtlmm::emof::extent_constructor_exists():
    assert callable(JTLMM::emof::Extent.__init__)


def test_jtlmm::emof::extent_constructor_args():
    sig = inspect.signature(JTLMM::emof::Extent.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::element_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Element)


def test_jtlmm::emof::element_constructor_exists():
    assert callable(JTLMM::emof::Element.__init__)


def test_jtlmm::emof::element_constructor_args():
    sig = inspect.signature(JTLMM::emof::Element.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::AnonymousTupleType)


def test_jtlmm::imperativeocl::anonymoustupletype_constructor_exists():
    assert callable(JTLMM::imperativeocl::AnonymousTupleType.__init__)


def test_jtlmm::imperativeocl::anonymoustupletype_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::Typedef)


def test_jtlmm::imperativeocl::typedef_constructor_exists():
    assert callable(JTLMM::imperativeocl::Typedef.__init__)


def test_jtlmm::imperativeocl::typedef_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::imperativeocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::imperativeocl::TemplateParameterType)


def test_jtlmm::imperativeocl::templateparametertype_constructor_exists():
    assert callable(JTLMM::imperativeocl::TemplateParameterType.__init__)


def test_jtlmm::imperativeocl::templateparametertype_constructor_args():
    sig = inspect.signature(JTLMM::imperativeocl::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_jtlmm::imperativeocl::templateparametertype_has_specification():
    assert hasattr(JTLMM::imperativeocl::TemplateParameterType, "specification")
    descriptor = None
    for klass in JTLMM::imperativeocl::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_jtlmm::essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::InvalidType)


def test_jtlmm::essentialocl::invalidtype_constructor_exists():
    assert callable(JTLMM::essentialocl::InvalidType.__init__)


def test_jtlmm::essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::essentialocl::VoidType)


def test_jtlmm::essentialocl::voidtype_constructor_exists():
    assert callable(JTLMM::essentialocl::VoidType.__init__)


def test_jtlmm::essentialocl::voidtype_constructor_args():
    sig = inspect.signature(JTLMM::essentialocl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::datatype_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::DataType)


def test_jtlmm::emof::datatype_constructor_exists():
    assert callable(JTLMM::emof::DataType.__init__)


def test_jtlmm::emof::datatype_constructor_args():
    sig = inspect.signature(JTLMM::emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_jtlmm::emof::class_is_not_abstract():
    assert not inspect.isabstract(JTLMM::emof::Class)


def test_jtlmm::emof::class_constructor_exists():
    assert callable(JTLMM::emof::Class.__init__)


def test_jtlmm::emof::class_constructor_args():
    sig = inspect.signature(JTLMM::emof::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_jtlmm::emof::class_has_isAbstract():
    assert hasattr(JTLMM::emof::Class, "isAbstract")
    descriptor = None
    for klass in JTLMM::emof::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Sequence",
        "OrderedSet",
        "Bag",
        "Set",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"

def test_severitykind_exists():
    # Check that the Enumeration exists
    assert SeverityKind is not None

def test_severitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SeverityKind]
    expected_literals = [
        "fatal",
        "error",
        "warning",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SeverityKind"


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
LogExp_strategy = st.builds(
    LogExp,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
essentialocl::LoopExp_strategy = st.builds(
    essentialocl::LoopExp,
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
JTLMM::imperativeocl::ForExp_strategy = st.builds(
    JTLMM::imperativeocl::ForExp,
)
JTLMM::imperativeocl::CollectorExp_strategy = st.builds(
    JTLMM::imperativeocl::CollectorExp,
)
JTLMM::imperativeocl::ImperativeIterateExp_strategy = st.builds(
    JTLMM::imperativeocl::ImperativeIterateExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
JTLMM::imperativeocl::ImperativeLoopExp_strategy = st.builds(
    JTLMM::imperativeocl::ImperativeLoopExp,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
JTLMM::imperativeocl::TryExp_strategy = st.builds(
    JTLMM::imperativeocl::TryExp,
)
JTLMM::imperativeocl::ComputeExp_strategy = st.builds(
    JTLMM::imperativeocl::ComputeExp,
)
JTLMM::imperativeocl::BlockExp_strategy = st.builds(
    JTLMM::imperativeocl::BlockExp,
)
JTLMM::imperativeocl::AltExp_strategy = st.builds(
    JTLMM::imperativeocl::AltExp,
)
JTLMM::imperativeocl::RaiseExp_strategy = st.builds(
    JTLMM::imperativeocl::RaiseExp,
)
JTLMM::imperativeocl::UnpackExp_strategy = st.builds(
    JTLMM::imperativeocl::UnpackExp,
)
JTLMM::imperativeocl::TupleExp_strategy = st.builds(
    JTLMM::imperativeocl::TupleExp,
)
JTLMM::imperativeocl::ReturnExp_strategy = st.builds(
    JTLMM::imperativeocl::ReturnExp,
)
JTLMM::imperativeocl::ContinueExp_strategy = st.builds(
    JTLMM::imperativeocl::ContinueExp,
)
JTLMM::imperativeocl::AssertExp_strategy = st.builds(
    JTLMM::imperativeocl::AssertExp,
    severity=
        safe_text
)
JTLMM::imperativeocl::LogExp_strategy = st.builds(
    JTLMM::imperativeocl::LogExp,
    text=
        safe_text,
    level=
        st.integers()
)
JTLMM::imperativeocl::InstantiationExp_strategy = st.builds(
    JTLMM::imperativeocl::InstantiationExp,
)
JTLMM::imperativeocl::BreakExp_strategy = st.builds(
    JTLMM::imperativeocl::BreakExp,
)
JTLMM::imperativeocl::VariableInitExp_strategy = st.builds(
    JTLMM::imperativeocl::VariableInitExp,
    withResult=
        st.booleans()
)
JTLMM::imperativeocl::WhileExp_strategy = st.builds(
    JTLMM::imperativeocl::WhileExp,
)
JTLMM::imperativeocl::UnlinkExp_strategy = st.builds(
    JTLMM::imperativeocl::UnlinkExp,
)
JTLMM::imperativeocl::AssignExp_strategy = st.builds(
    JTLMM::imperativeocl::AssignExp,
    isReset=
        st.booleans()
)
CollectionType_strategy = st.builds(
    CollectionType,
)
JTLMM::imperativeocl::ListType_strategy = st.builds(
    JTLMM::imperativeocl::ListType,
)
JTLMM::imperativeocl::DictionaryType_strategy = st.builds(
    JTLMM::imperativeocl::DictionaryType,
)
JTLMM::essentialocl::BagType_strategy = st.builds(
    JTLMM::essentialocl::BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
JTLMM::essentialocl::FeaturePropertyCall_strategy = st.builds(
    JTLMM::essentialocl::FeaturePropertyCall,
)
JTLMM::essentialocl::OpaqueExpression_strategy = st.builds(
    JTLMM::essentialocl::OpaqueExpression,
)
AssignExp_strategy = st.builds(
    AssignExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
emof::Type_strategy = st.builds(
    emof::Type,
)
emof::DataType_strategy = st.builds(
    emof::DataType,
)
JTLMM::essentialocl::SetType_strategy = st.builds(
    JTLMM::essentialocl::SetType,
)
JTLMM::essentialocl::SequenceType_strategy = st.builds(
    JTLMM::essentialocl::SequenceType,
)
JTLMM::essentialocl::OrderedSetType_strategy = st.builds(
    JTLMM::essentialocl::OrderedSetType,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
JTLMM::essentialocl::ExpressionInOcl_strategy = st.builds(
    JTLMM::essentialocl::ExpressionInOcl,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
JTLMM::essentialocl::CollectionRange_strategy = st.builds(
    JTLMM::essentialocl::CollectionRange,
)
JTLMM::essentialocl::CollectionItem_strategy = st.builds(
    JTLMM::essentialocl::CollectionItem,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
JTLMM::essentialocl::EnumLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::EnumLiteralExp,
)
JTLMM::essentialocl::TupleLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::TupleLiteralExp,
)
JTLMM::template::TemplateExp_strategy = st.builds(
    JTLMM::template::TemplateExp,
)
JTLMM::essentialocl::InvalidLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::InvalidLiteralExp,
)
JTLMM::imperativeocl::AnonymousTupleLiteralExp_strategy = st.builds(
    JTLMM::imperativeocl::AnonymousTupleLiteralExp,
)
JTLMM::essentialocl::NullLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::NullLiteralExp,
)
JTLMM::essentialocl::CollectionLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::CollectionLiteralExp,
    kind=
        safe_text
)
JTLMM::imperativeocl::DictLiteralExp_strategy = st.builds(
    JTLMM::imperativeocl::DictLiteralExp,
)
JTLMM::essentialocl::PrimitiveLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::PrimitiveLiteralExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
JTLMM::essentialocl::IterateExp_strategy = st.builds(
    JTLMM::essentialocl::IterateExp,
)
JTLMM::essentialocl::IteratorExp_strategy = st.builds(
    JTLMM::essentialocl::IteratorExp,
)
essentialocl::OclExpression_strategy = st.builds(
    essentialocl::OclExpression,
)
essentialocl::CallExp_strategy = st.builds(
    essentialocl::CallExp,
)
JTLMM::imperativeocl::SwitchExp_strategy = st.builds(
    JTLMM::imperativeocl::SwitchExp,
)
JTLMM::essentialocl::LoopExp_strategy = st.builds(
    JTLMM::essentialocl::LoopExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
JTLMM::essentialocl::OperationCallExp_strategy = st.builds(
    JTLMM::essentialocl::OperationCallExp,
)
JTLMM::essentialocl::PropertyCallExp_strategy = st.builds(
    JTLMM::essentialocl::PropertyCallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
JTLMM::essentialocl::StringLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::StringLiteralExp,
    stringSymbol=
        safe_text
)
JTLMM::essentialocl::NumericLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::NumericLiteralExp,
)
JTLMM::essentialocl::BooleanLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::BooleanLiteralExp,
    booleanSymbol=
        st.booleans()
)
OclExpression_strategy = st.builds(
    OclExpression,
)
JTLMM::essentialocl::TypeExp_strategy = st.builds(
    JTLMM::essentialocl::TypeExp,
)
JTLMM::imperativeocl::ImperativeExpression_strategy = st.builds(
    JTLMM::imperativeocl::ImperativeExpression,
)
JTLMM::essentialocl::CallExp_strategy = st.builds(
    JTLMM::essentialocl::CallExp,
)
JTLMM::essentialocl::LetExp_strategy = st.builds(
    JTLMM::essentialocl::LetExp,
)
JTLMM::essentialocl::LiteralExp_strategy = st.builds(
    JTLMM::essentialocl::LiteralExp,
)
JTLMM::essentialocl::VariableExp_strategy = st.builds(
    JTLMM::essentialocl::VariableExp,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
JTLMM::template::CollectionTemplateExp_strategy = st.builds(
    JTLMM::template::CollectionTemplateExp,
    kind=
        safe_text
)
JTLMM::template::ObjectTemplateExp_strategy = st.builds(
    JTLMM::template::ObjectTemplateExp,
    referredClass=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
JTLMM::essentialocl::IfExp_strategy = st.builds(
    JTLMM::essentialocl::IfExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
JTLMM::essentialocl::RealLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
JTLMM::essentialocl::IntegerLiteralExp_strategy = st.builds(
    JTLMM::essentialocl::IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
JTLMM::essentialocl::UnlimitedNaturalExp_strategy = st.builds(
    JTLMM::essentialocl::UnlimitedNaturalExp,
    symbol=
        safe_text
)
TryExp_strategy = st.builds(
    TryExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JTLMM::essentialocl::Variable_strategy = st.builds(
    JTLMM::essentialocl::Variable,
)
JTLMM::essentialocl::CollectionLiteralPart_strategy = st.builds(
    JTLMM::essentialocl::CollectionLiteralPart,
)
JTLMM::essentialocl::TupleLiteralPart_strategy = st.builds(
    JTLMM::essentialocl::TupleLiteralPart,
)
JTLMM::essentialocl::OclExpression_strategy = st.builds(
    JTLMM::essentialocl::OclExpression,
)
Pattern_strategy = st.builds(
    Pattern,
)
Domain_strategy = st.builds(
    Domain,
)
Transformation_strategy = st.builds(
    Transformation,
)
Relation_strategy = st.builds(
    Relation,
)
Model_strategy = st.builds(
    Model,
)
emof::Package_strategy = st.builds(
    emof::Package,
)
emof::Class_strategy = st.builds(
    emof::Class,
)
JTLMM::essentialocl::AnyType_strategy = st.builds(
    JTLMM::essentialocl::AnyType,
)
JTLMM::essentialocl::TupleType_strategy = st.builds(
    JTLMM::essentialocl::TupleType,
)
JTLMM::JTL::Transformation_strategy = st.builds(
    JTLMM::JTL::Transformation,
)
Extent_strategy = st.builds(
    Extent,
)
JTLMM::emof::URIExtent_strategy = st.builds(
    JTLMM::emof::URIExtent,
)
Variable_strategy = st.builds(
    Variable,
)
Package_strategy = st.builds(
    Package,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JTLMM::emof::TypedElement_strategy = st.builds(
    JTLMM::emof::TypedElement,
    type=
        safe_text
)
JTLMM::emof::Type_strategy = st.builds(
    JTLMM::emof::Type,
)
JTLMM::JTL::Relation_strategy = st.builds(
    JTLMM::JTL::Relation,
    isTopLevel=
        st.booleans()
)
JTLMM::JTL::Domain_strategy = st.builds(
    JTLMM::JTL::Domain,
    isEnforceable=
        st.booleans(),
    isCheckable=
        st.booleans()
)
JTLMM::JTL::Model_strategy = st.builds(
    JTLMM::JTL::Model,
    usedPackage=
        safe_text
)
JTLMM::emof::Package_strategy = st.builds(
    JTLMM::emof::Package,
    uri=
        safe_text
)
JTLMM::emof::MultiplicityElement_strategy = st.builds(
    JTLMM::emof::MultiplicityElement,
    isUnique=
        safe_text,
    lower=
        st.integers(),
    isOrdered=
        safe_text,
    upper=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
emof::TypedElement_strategy = st.builds(
    emof::TypedElement,
)
emof::MultiplicityElement_strategy = st.builds(
    emof::MultiplicityElement,
)
JTLMM::emof::Operation_strategy = st.builds(
    JTLMM::emof::Operation,
)
JTLMM::emof::Object_strategy = st.builds(
    JTLMM::emof::Object,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
JTLMM::emof::PrimitiveType_strategy = st.builds(
    JTLMM::emof::PrimitiveType,
)
JTLMM::essentialocl::CollectionType_strategy = st.builds(
    JTLMM::essentialocl::CollectionType,
)
JTLMM::emof::Enumeration_strategy = st.builds(
    JTLMM::emof::Enumeration,
)
JTLMM::emof::Property_strategy = st.builds(
    JTLMM::emof::Property,
    isDerived=
        st.booleans(),
    default=
        safe_text,
    isComposite=
        st.booleans(),
    isId=
        st.booleans(),
    isReadOnly=
        st.booleans()
)
Enumeration_strategy = st.builds(
    Enumeration,
)
JTLMM::emof::EnumerationLiteral_strategy = st.builds(
    JTLMM::emof::EnumerationLiteral,
)
JTLMM::emof::Parameter_strategy = st.builds(
    JTLMM::emof::Parameter,
)
Element_strategy = st.builds(
    Element,
)
JTLMM::template::PropertyTemplateItem_strategy = st.builds(
    JTLMM::template::PropertyTemplateItem,
)
JTLMM::imperativeocl::AnonymousTupleLiteralPart_strategy = st.builds(
    JTLMM::imperativeocl::AnonymousTupleLiteralPart,
)
JTLMM::emof::Comment_strategy = st.builds(
    JTLMM::emof::Comment,
)
JTLMM::JTL::Predicate_strategy = st.builds(
    JTLMM::JTL::Predicate,
)
JTLMM::emof::NamedElement_strategy = st.builds(
    JTLMM::emof::NamedElement,
    name=
        safe_text
)
JTLMM::JTL::Pattern_strategy = st.builds(
    JTLMM::JTL::Pattern,
)
JTLMM::imperativeocl::DictLiteralPart_strategy = st.builds(
    JTLMM::imperativeocl::DictLiteralPart,
)
JTLMM::emof::Tag_strategy = st.builds(
    JTLMM::emof::Tag,
    value=
        safe_text,
    name=
        safe_text
)
Comment_strategy = st.builds(
    Comment,
)
Tag_strategy = st.builds(
    Tag,
)
Object_strategy = st.builds(
    Object,
)
JTLMM::emof::Extent_strategy = st.builds(
    JTLMM::emof::Extent,
)
JTLMM::emof::Element_strategy = st.builds(
    JTLMM::emof::Element,
)
Class_strategy = st.builds(
    Class,
)
JTLMM::imperativeocl::AnonymousTupleType_strategy = st.builds(
    JTLMM::imperativeocl::AnonymousTupleType,
)
JTLMM::imperativeocl::Typedef_strategy = st.builds(
    JTLMM::imperativeocl::Typedef,
)
Operation_strategy = st.builds(
    Operation,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
JTLMM::imperativeocl::TemplateParameterType_strategy = st.builds(
    JTLMM::imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
JTLMM::essentialocl::InvalidType_strategy = st.builds(
    JTLMM::essentialocl::InvalidType,
)
JTLMM::essentialocl::VoidType_strategy = st.builds(
    JTLMM::essentialocl::VoidType,
)
JTLMM::emof::DataType_strategy = st.builds(
    JTLMM::emof::DataType,
)
JTLMM::emof::Class_strategy = st.builds(
    JTLMM::emof::Class,
    isAbstract=
        st.booleans()
)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LoopExp)

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=JTLMM::imperativeocl::ForExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ForExp)

@given(instance=JTLMM::imperativeocl::CollectorExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::collectorexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::CollectorExp)

@given(instance=JTLMM::imperativeocl::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ImperativeIterateExp)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=JTLMM::imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ImperativeLoopExp)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=JTLMM::imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::TryExp)

@given(instance=JTLMM::imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ComputeExp)

@given(instance=JTLMM::imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::BlockExp)

@given(instance=JTLMM::imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AltExp)

@given(instance=JTLMM::imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::RaiseExp)

@given(instance=JTLMM::imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::UnpackExp)

@given(instance=JTLMM::imperativeocl::TupleExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::tupleexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::TupleExp)

@given(instance=JTLMM::imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ReturnExp)

@given(instance=JTLMM::imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ContinueExp)

@given(instance=JTLMM::imperativeocl::AssertExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AssertExp)

@given(instance=JTLMM::imperativeocl::AssertExp_strategy)
def test_jtlmm::imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=JTLMM::imperativeocl::AssertExp_strategy)
def test_jtlmm::imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=JTLMM::imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::LogExp)

@given(instance=JTLMM::imperativeocl::LogExp_strategy)
def test_jtlmm::imperativeocl::logexp_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=JTLMM::imperativeocl::LogExp_strategy)
def test_jtlmm::imperativeocl::logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=JTLMM::imperativeocl::LogExp_strategy)
def test_jtlmm::imperativeocl::logexp_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=JTLMM::imperativeocl::LogExp_strategy)
def test_jtlmm::imperativeocl::logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=JTLMM::imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::InstantiationExp)

@given(instance=JTLMM::imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::BreakExp)

@given(instance=JTLMM::imperativeocl::VariableInitExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::VariableInitExp)

@given(instance=JTLMM::imperativeocl::VariableInitExp_strategy)
def test_jtlmm::imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, bool)


@given(instance=JTLMM::imperativeocl::VariableInitExp_strategy)
def test_jtlmm::imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=JTLMM::imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::WhileExp)

@given(instance=JTLMM::imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::UnlinkExp)

@given(instance=JTLMM::imperativeocl::AssignExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AssignExp)

@given(instance=JTLMM::imperativeocl::AssignExp_strategy)
def test_jtlmm::imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, bool)


@given(instance=JTLMM::imperativeocl::AssignExp_strategy)
def test_jtlmm::imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=JTLMM::imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ListType)

@given(instance=JTLMM::imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::DictionaryType)

@given(instance=JTLMM::essentialocl::BagType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::BagType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=JTLMM::essentialocl::FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::featurepropertycall_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::FeaturePropertyCall)

@given(instance=JTLMM::essentialocl::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::opaqueexpression_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::OpaqueExpression)

@given(instance=AssignExp_strategy)
@settings(max_examples=50)
def test_assignexp_instantiation(instance):
    assert isinstance(instance, AssignExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=emof::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, emof::Type)

@given(instance=emof::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, emof::DataType)

@given(instance=JTLMM::essentialocl::SetType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::settype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::SetType)

@given(instance=JTLMM::essentialocl::SequenceType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::SequenceType)

@given(instance=JTLMM::essentialocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::OrderedSetType)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=JTLMM::essentialocl::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::ExpressionInOcl)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=JTLMM::essentialocl::CollectionRange_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CollectionRange)

@given(instance=JTLMM::essentialocl::CollectionItem_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CollectionItem)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=JTLMM::essentialocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::EnumLiteralExp)

@given(instance=JTLMM::essentialocl::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::TupleLiteralExp)

@given(instance=JTLMM::template::TemplateExp_strategy)
@settings(max_examples=50)
def test_jtlmm::template::templateexp_instantiation(instance):
    assert isinstance(instance, JTLMM::template::TemplateExp)

@given(instance=JTLMM::essentialocl::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::InvalidLiteralExp)

@given(instance=JTLMM::imperativeocl::AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AnonymousTupleLiteralExp)

@given(instance=JTLMM::essentialocl::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::NullLiteralExp)

@given(instance=JTLMM::essentialocl::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CollectionLiteralExp)

@given(instance=JTLMM::essentialocl::CollectionLiteralExp_strategy)
def test_jtlmm::essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=JTLMM::essentialocl::CollectionLiteralExp_strategy)
def test_jtlmm::essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=JTLMM::imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::DictLiteralExp)

@given(instance=JTLMM::essentialocl::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::PrimitiveLiteralExp)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=JTLMM::essentialocl::IterateExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::IterateExp)

@given(instance=JTLMM::essentialocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::IteratorExp)

@given(instance=essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl::OclExpression)

@given(instance=essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, essentialocl::CallExp)

@given(instance=JTLMM::imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::SwitchExp)

@given(instance=JTLMM::essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::LoopExp)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=JTLMM::essentialocl::OperationCallExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::OperationCallExp)

@given(instance=JTLMM::essentialocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::PropertyCallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=JTLMM::essentialocl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::StringLiteralExp)

@given(instance=JTLMM::essentialocl::StringLiteralExp_strategy)
def test_jtlmm::essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=JTLMM::essentialocl::StringLiteralExp_strategy)
def test_jtlmm::essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=JTLMM::essentialocl::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::NumericLiteralExp)

@given(instance=JTLMM::essentialocl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::BooleanLiteralExp)

@given(instance=JTLMM::essentialocl::BooleanLiteralExp_strategy)
def test_jtlmm::essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, bool)


@given(instance=JTLMM::essentialocl::BooleanLiteralExp_strategy)
def test_jtlmm::essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=JTLMM::essentialocl::TypeExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::TypeExp)

@given(instance=JTLMM::imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::ImperativeExpression)

@given(instance=JTLMM::essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CallExp)

@given(instance=JTLMM::essentialocl::LetExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::LetExp)

@given(instance=JTLMM::essentialocl::LiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::LiteralExp)

@given(instance=JTLMM::essentialocl::VariableExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::VariableExp)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=JTLMM::template::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_jtlmm::template::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, JTLMM::template::CollectionTemplateExp)

@given(instance=JTLMM::template::CollectionTemplateExp_strategy)
def test_jtlmm::template::collectiontemplateexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=JTLMM::template::CollectionTemplateExp_strategy)
def test_jtlmm::template::collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=JTLMM::template::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_jtlmm::template::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, JTLMM::template::ObjectTemplateExp)

@given(instance=JTLMM::template::ObjectTemplateExp_strategy)
def test_jtlmm::template::objecttemplateexp_referredClass_type(instance):
    assert isinstance(instance.referredClass, str)


@given(instance=JTLMM::template::ObjectTemplateExp_strategy)
def test_jtlmm::template::objecttemplateexp_referredClass_setter(instance):
    original = instance.referredClass
    instance.referredClass = original
    assert instance.referredClass == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=JTLMM::essentialocl::IfExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::IfExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=JTLMM::essentialocl::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::RealLiteralExp)

@given(instance=JTLMM::essentialocl::RealLiteralExp_strategy)
def test_jtlmm::essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, float)


@given(instance=JTLMM::essentialocl::RealLiteralExp_strategy)
def test_jtlmm::essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=JTLMM::essentialocl::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::IntegerLiteralExp)

@given(instance=JTLMM::essentialocl::IntegerLiteralExp_strategy)
def test_jtlmm::essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, int)


@given(instance=JTLMM::essentialocl::IntegerLiteralExp_strategy)
def test_jtlmm::essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=JTLMM::essentialocl::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::UnlimitedNaturalExp)

@given(instance=JTLMM::essentialocl::UnlimitedNaturalExp_strategy)
def test_jtlmm::essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=JTLMM::essentialocl::UnlimitedNaturalExp_strategy)
def test_jtlmm::essentialocl::unlimitednaturalexp_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=TryExp_strategy)
@settings(max_examples=50)
def test_tryexp_instantiation(instance):
    assert isinstance(instance, TryExp)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=JTLMM::essentialocl::Variable_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::variable_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::Variable)

@given(instance=JTLMM::essentialocl::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CollectionLiteralPart)

@given(instance=JTLMM::essentialocl::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::TupleLiteralPart)

@given(instance=JTLMM::essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::OclExpression)

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)

@given(instance=emof::Package_strategy)
@settings(max_examples=50)
def test_emof::package_instantiation(instance):
    assert isinstance(instance, emof::Package)

@given(instance=emof::Class_strategy)
@settings(max_examples=50)
def test_emof::class_instantiation(instance):
    assert isinstance(instance, emof::Class)

@given(instance=JTLMM::essentialocl::AnyType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::AnyType)

@given(instance=JTLMM::essentialocl::TupleType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::TupleType)

@given(instance=JTLMM::JTL::Transformation_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::transformation_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Transformation)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=JTLMM::emof::URIExtent_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::uriextent_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::URIExtent)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JTLMM::emof::TypedElement_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::typedelement_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::TypedElement)

@given(instance=JTLMM::emof::TypedElement_strategy)
def test_jtlmm::emof::typedelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JTLMM::emof::TypedElement_strategy)
def test_jtlmm::emof::typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JTLMM::emof::Type_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::type_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Type)

@given(instance=JTLMM::JTL::Relation_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::relation_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Relation)

@given(instance=JTLMM::JTL::Relation_strategy)
def test_jtlmm::jtl::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, bool)


@given(instance=JTLMM::JTL::Relation_strategy)
def test_jtlmm::jtl::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=JTLMM::JTL::Domain_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::domain_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Domain)

@given(instance=JTLMM::JTL::Domain_strategy)
def test_jtlmm::jtl::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, bool)


@given(instance=JTLMM::JTL::Domain_strategy)
def test_jtlmm::jtl::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=JTLMM::JTL::Domain_strategy)
def test_jtlmm::jtl::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, bool)


@given(instance=JTLMM::JTL::Domain_strategy)
def test_jtlmm::jtl::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=JTLMM::JTL::Model_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::model_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Model)

@given(instance=JTLMM::JTL::Model_strategy)
def test_jtlmm::jtl::model_usedPackage_type(instance):
    assert isinstance(instance.usedPackage, str)


@given(instance=JTLMM::JTL::Model_strategy)
def test_jtlmm::jtl::model_usedPackage_setter(instance):
    original = instance.usedPackage
    instance.usedPackage = original
    assert instance.usedPackage == original

@given(instance=JTLMM::emof::Package_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::package_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Package)

@given(instance=JTLMM::emof::Package_strategy)
def test_jtlmm::emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=JTLMM::emof::Package_strategy)
def test_jtlmm::emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=JTLMM::emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::MultiplicityElement)

@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=JTLMM::emof::MultiplicityElement_strategy)
def test_jtlmm::emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=emof::TypedElement_strategy)
@settings(max_examples=50)
def test_emof::typedelement_instantiation(instance):
    assert isinstance(instance, emof::TypedElement)

@given(instance=emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, emof::MultiplicityElement)

@given(instance=JTLMM::emof::Operation_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::operation_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Operation)

@given(instance=JTLMM::emof::Object_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::object_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Object)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=JTLMM::emof::PrimitiveType_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::primitivetype_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::PrimitiveType)

@given(instance=JTLMM::essentialocl::CollectionType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::CollectionType)

@given(instance=JTLMM::emof::Enumeration_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::enumeration_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Enumeration)

@given(instance=JTLMM::emof::Property_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::property_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Property)

@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isId_type(instance):
    assert isinstance(instance.isId, bool)


@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=JTLMM::emof::Property_strategy)
def test_jtlmm::emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=JTLMM::emof::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::EnumerationLiteral)

@given(instance=JTLMM::emof::Parameter_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::parameter_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Parameter)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=JTLMM::template::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_jtlmm::template::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, JTLMM::template::PropertyTemplateItem)

@given(instance=JTLMM::imperativeocl::AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AnonymousTupleLiteralPart)

@given(instance=JTLMM::emof::Comment_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::comment_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Comment)

@given(instance=JTLMM::JTL::Predicate_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::predicate_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Predicate)

@given(instance=JTLMM::emof::NamedElement_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::namedelement_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::NamedElement)

@given(instance=JTLMM::emof::NamedElement_strategy)
def test_jtlmm::emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JTLMM::emof::NamedElement_strategy)
def test_jtlmm::emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JTLMM::JTL::Pattern_strategy)
@settings(max_examples=50)
def test_jtlmm::jtl::pattern_instantiation(instance):
    assert isinstance(instance, JTLMM::JTL::Pattern)

@given(instance=JTLMM::imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::DictLiteralPart)

@given(instance=JTLMM::emof::Tag_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::tag_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Tag)

@given(instance=JTLMM::emof::Tag_strategy)
def test_jtlmm::emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=JTLMM::emof::Tag_strategy)
def test_jtlmm::emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=JTLMM::emof::Tag_strategy)
def test_jtlmm::emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JTLMM::emof::Tag_strategy)
def test_jtlmm::emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Comment_strategy)
@settings(max_examples=50)
def test_comment_instantiation(instance):
    assert isinstance(instance, Comment)

@given(instance=Tag_strategy)
@settings(max_examples=50)
def test_tag_instantiation(instance):
    assert isinstance(instance, Tag)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=JTLMM::emof::Extent_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::extent_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Extent)

@given(instance=JTLMM::emof::Element_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::element_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Element)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=JTLMM::imperativeocl::AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::anonymoustupletype_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::AnonymousTupleType)

@given(instance=JTLMM::imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::Typedef)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JTLMM::imperativeocl::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_jtlmm::imperativeocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, JTLMM::imperativeocl::TemplateParameterType)

@given(instance=JTLMM::imperativeocl::TemplateParameterType_strategy)
def test_jtlmm::imperativeocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=JTLMM::imperativeocl::TemplateParameterType_strategy)
def test_jtlmm::imperativeocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=JTLMM::essentialocl::InvalidType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::InvalidType)

@given(instance=JTLMM::essentialocl::VoidType_strategy)
@settings(max_examples=50)
def test_jtlmm::essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, JTLMM::essentialocl::VoidType)

@given(instance=JTLMM::emof::DataType_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::datatype_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::DataType)

@given(instance=JTLMM::emof::Class_strategy)
@settings(max_examples=50)
def test_jtlmm::emof::class_instantiation(instance):
    assert isinstance(instance, JTLMM::emof::Class)

@given(instance=JTLMM::emof::Class_strategy)
def test_jtlmm::emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=JTLMM::emof::Class_strategy)
def test_jtlmm::emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original
