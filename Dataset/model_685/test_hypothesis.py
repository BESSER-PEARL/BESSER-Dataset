import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AssignExp,
    PropertyTemplateItem,
    ImperativeExpression,
    JTL::imperativeocl::WhileExp,
    JTL::imperativeocl::AssignExp,
    ImperativeLoopExp,
    JTL::imperativeocl::ImperativeIterateExp,
    ObjectTemplateExp,
    CollectionType,
    JTL::essentialocl::BagType,
    TupleLiteralExp,
    CallExp,
    JTL::essentialocl::FeaturePropertyCall,
    JTL::essentialocl::OpaqueExpression,
    emof::Type,
    emof::DataType,
    JTL::essentialocl::SetType,
    JTL::essentialocl::SequenceType,
    JTL::essentialocl::OrderedSetType,
    CollectionLiteralExp,
    CollectionLiteralPart,
    LiteralExp,
    JTL::essentialocl::CollectionLiteralExp,
    JTL::essentialocl::InvalidLiteralExp,
    JTL::template::TemplateExp,
    JTL::essentialocl::EnumLiteralExp,
    JTL::essentialocl::PrimitiveLiteralExp,
    OpaqueExpression,
    JTL::essentialocl::ExpressionInOcl,
    JTL::essentialocl::NullLiteralExp,
    TupleLiteralPart,
    JTL::essentialocl::TupleLiteralExp,
    JTL::essentialocl::CollectionRange,
    JTL::essentialocl::CollectionItem,
    FeaturePropertyCall,
    JTL::essentialocl::PropertyCallExp,
    ComputeExp,
    LetExp,
    JTL::essentialocl::OperationCallExp,
    LoopExp,
    JTL::essentialocl::IterateExp,
    JTL::essentialocl::IteratorExp,
    essentialocl::OclExpression,
    essentialocl::CallExp,
    JTL::essentialocl::LoopExp,
    JTL::imperativeocl::ListType,
    AnonymousTupleLiteralPart,
    JTL::imperativeocl::AnonymousTupleLiteralExp,
    JTL::imperativeocl::LogExp,
    DictLiteralPart,
    JTL::imperativeocl::DictLiteralExp,
    JTL::imperativeocl::DictionaryType,
    JTL::imperativeocl::UnpackExp,
    JTL::imperativeocl::CollectorExp,
    essentialocl::LoopExp,
    LogExp,
    JTL::imperativeocl::AssertExp,
    JTL::imperativeocl::TryExp,
    JTL::imperativeocl::BreakExp,
    JTL::imperativeocl::ReturnExp,
    JTL::imperativeocl::InstantiationExp,
    JTL::imperativeocl::TupleExp,
    JTL::imperativeocl::ForExp,
    JTL::imperativeocl::ContinueExp,
    Enumeration,
    JTL::imperativeocl::RaiseExp,
    JTL::imperativeocl::VariableInitExp,
    AltExp,
    imperativeocl::ImperativeExpression,
    JTL::imperativeocl::ImperativeLoopExp,
    JTL::imperativeocl::SwitchExp,
    Package,
    JTL::imperativeocl::BlockExp,
    JTL::imperativeocl::UnlinkExp,
    NamedElement,
    JTL::emof::EnumerationLiteral,
    JTL::emof::Type,
    JTL::imperativeocl::AltExp,
    JTL::emof::Package,
    JTL::imperativeocl::ComputeExp,
    Property,
    Type,
    JTL::essentialocl::InvalidType,
    JTL::imperativeocl::TemplateParameterType,
    JTL::essentialocl::VoidType,
    JTL::emof::Class,
    EnumerationLiteral,
    DataType,
    JTL::essentialocl::CollectionType,
    JTL::emof::Enumeration,
    Element,
    JTL::imperativeocl::AnonymousTupleLiteralPart,
    JTL::emof::NamedElement,
    JTL::template::PropertyTemplateItem,
    JTL::imperativeocl::DictLiteralPart,
    JTL::emof::Tag,
    Comment,
    Tag,
    Object,
    JTL::emof::Element,
    JTL::emof::DataType,
    Class,
    JTL::imperativeocl::Typedef,
    JTL::imperativeocl::AnonymousTupleType,
    Operation,
    OclExpression,
    JTL::essentialocl::LiteralExp,
    JTL::essentialocl::TypeExp,
    JTL::essentialocl::VariableExp,
    JTL::imperativeocl::ImperativeExpression,
    JTL::essentialocl::LetExp,
    JTL::JTL::Predicate,
    TemplateExp,
    JTL::template::ObjectTemplateExp,
    JTL::template::CollectionTemplateExp,
    Predicate,
    JTL::JTL::Pattern,
    JTL::essentialocl::IfExp,
    NumericLiteralExp,
    JTL::essentialocl::IntegerLiteralExp,
    JTL::essentialocl::RealLiteralExp,
    JTL::essentialocl::UnlimitedNaturalExp,
    TryExp,
    TypedElement,
    JTL::essentialocl::CollectionLiteralPart,
    JTL::essentialocl::TupleLiteralPart,
    JTL::essentialocl::Variable,
    JTL::essentialocl::OclExpression,
    JTL::essentialocl::CallExp,
    PrimitiveLiteralExp,
    JTL::essentialocl::StringLiteralExp,
    JTL::essentialocl::NumericLiteralExp,
    JTL::essentialocl::BooleanLiteralExp,
    Relation,
    Model,
    emof::Package,
    emof::Class,
    JTL::essentialocl::TupleType,
    JTL::essentialocl::AnyType,
    JTL::JTL::Transformation,
    JTL::emof::Comment,
    Extent,
    JTL::emof::URIExtent,
    JTL::emof::PrimitiveType,
    JTL::emof::TypedElement,
    JTL::JTL::Model,
    Pattern,
    JTL::JTL::Where,
    JTL::JTL::When,
    JTL::JTL::Domain,
    Variable,
    When,
    Where,
    Domain,
    Transformation,
    JTL::JTL::Relation,
    JTL::emof::MultiplicityElement,
    Parameter,
    emof::TypedElement,
    emof::MultiplicityElement,
    JTL::emof::Property,
    JTL::emof::Parameter,
    JTL::emof::Operation,
    JTL::emof::Object,
    JTL::emof::Extent,
    SeverityKind,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(ImperativeExpression)


def test_imperativeexpression_constructor_exists():
    assert callable(ImperativeExpression.__init__)


def test_imperativeexpression_constructor_args():
    sig = inspect.signature(ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::whileexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::WhileExp)


def test_jtl::imperativeocl::whileexp_constructor_exists():
    assert callable(JTL::imperativeocl::WhileExp.__init__)


def test_jtl::imperativeocl::whileexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::WhileExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::assignexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AssignExp)


def test_jtl::imperativeocl::assignexp_constructor_exists():
    assert callable(JTL::imperativeocl::AssignExp.__init__)


def test_jtl::imperativeocl::assignexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AssignExp.__init__)
    params = list(sig.parameters.keys())
    assert "isReset" in params, "Missing parameter 'isReset'"

def test_jtl::imperativeocl::assignexp_has_isReset():
    assert hasattr(JTL::imperativeocl::AssignExp, "isReset")
    descriptor = None
    for klass in JTL::imperativeocl::AssignExp.__mro__:
        if "isReset" in klass.__dict__:
            descriptor = klass.__dict__["isReset"]
            break
    assert isinstance(descriptor, property)



def test_imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(ImperativeLoopExp)


def test_imperativeloopexp_constructor_exists():
    assert callable(ImperativeLoopExp.__init__)


def test_imperativeloopexp_constructor_args():
    sig = inspect.signature(ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::imperativeiterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ImperativeIterateExp)


def test_jtl::imperativeocl::imperativeiterateexp_constructor_exists():
    assert callable(JTL::imperativeocl::ImperativeIterateExp.__init__)


def test_jtl::imperativeocl::imperativeiterateexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ImperativeIterateExp.__init__)
    params = list(sig.parameters.keys())



def test_objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(ObjectTemplateExp)


def test_objecttemplateexp_constructor_exists():
    assert callable(ObjectTemplateExp.__init__)


def test_objecttemplateexp_constructor_args():
    sig = inspect.signature(ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::bagtype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::BagType)


def test_jtl::essentialocl::bagtype_constructor_exists():
    assert callable(JTL::essentialocl::BagType.__init__)


def test_jtl::essentialocl::bagtype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::BagType.__init__)
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



def test_jtl::essentialocl::featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::FeaturePropertyCall)


def test_jtl::essentialocl::featurepropertycall_constructor_exists():
    assert callable(JTL::essentialocl::FeaturePropertyCall.__init__)


def test_jtl::essentialocl::featurepropertycall_constructor_args():
    sig = inspect.signature(JTL::essentialocl::FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::OpaqueExpression)


def test_jtl::essentialocl::opaqueexpression_constructor_exists():
    assert callable(JTL::essentialocl::OpaqueExpression.__init__)


def test_jtl::essentialocl::opaqueexpression_constructor_args():
    sig = inspect.signature(JTL::essentialocl::OpaqueExpression.__init__)
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



def test_jtl::essentialocl::settype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::SetType)


def test_jtl::essentialocl::settype_constructor_exists():
    assert callable(JTL::essentialocl::SetType.__init__)


def test_jtl::essentialocl::settype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::SetType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::SequenceType)


def test_jtl::essentialocl::sequencetype_constructor_exists():
    assert callable(JTL::essentialocl::SequenceType.__init__)


def test_jtl::essentialocl::sequencetype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::OrderedSetType)


def test_jtl::essentialocl::orderedsettype_constructor_exists():
    assert callable(JTL::essentialocl::OrderedSetType.__init__)


def test_jtl::essentialocl::orderedsettype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::OrderedSetType.__init__)
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



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CollectionLiteralExp)


def test_jtl::essentialocl::collectionliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::CollectionLiteralExp.__init__)


def test_jtl::essentialocl::collectionliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtl::essentialocl::collectionliteralexp_has_kind():
    assert hasattr(JTL::essentialocl::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in JTL::essentialocl::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_jtl::essentialocl::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::InvalidLiteralExp)


def test_jtl::essentialocl::invalidliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::InvalidLiteralExp.__init__)


def test_jtl::essentialocl::invalidliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::template::templateexp_is_not_abstract():
    assert not inspect.isabstract(JTL::template::TemplateExp)


def test_jtl::template::templateexp_constructor_exists():
    assert callable(JTL::template::TemplateExp.__init__)


def test_jtl::template::templateexp_constructor_args():
    sig = inspect.signature(JTL::template::TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::EnumLiteralExp)


def test_jtl::essentialocl::enumliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::EnumLiteralExp.__init__)


def test_jtl::essentialocl::enumliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::PrimitiveLiteralExp)


def test_jtl::essentialocl::primitiveliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::PrimitiveLiteralExp.__init__)


def test_jtl::essentialocl::primitiveliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::ExpressionInOcl)


def test_jtl::essentialocl::expressioninocl_constructor_exists():
    assert callable(JTL::essentialocl::ExpressionInOcl.__init__)


def test_jtl::essentialocl::expressioninocl_constructor_args():
    sig = inspect.signature(JTL::essentialocl::ExpressionInOcl.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::NullLiteralExp)


def test_jtl::essentialocl::nullliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::NullLiteralExp.__init__)


def test_jtl::essentialocl::nullliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::TupleLiteralExp)


def test_jtl::essentialocl::tupleliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::TupleLiteralExp.__init__)


def test_jtl::essentialocl::tupleliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::collectionrange_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CollectionRange)


def test_jtl::essentialocl::collectionrange_constructor_exists():
    assert callable(JTL::essentialocl::CollectionRange.__init__)


def test_jtl::essentialocl::collectionrange_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::collectionitem_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CollectionItem)


def test_jtl::essentialocl::collectionitem_constructor_exists():
    assert callable(JTL::essentialocl::CollectionItem.__init__)


def test_jtl::essentialocl::collectionitem_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::PropertyCallExp)


def test_jtl::essentialocl::propertycallexp_constructor_exists():
    assert callable(JTL::essentialocl::PropertyCallExp.__init__)


def test_jtl::essentialocl::propertycallexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::PropertyCallExp.__init__)
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



def test_jtl::essentialocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::OperationCallExp)


def test_jtl::essentialocl::operationcallexp_constructor_exists():
    assert callable(JTL::essentialocl::OperationCallExp.__init__)


def test_jtl::essentialocl::operationcallexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::iterateexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::IterateExp)


def test_jtl::essentialocl::iterateexp_constructor_exists():
    assert callable(JTL::essentialocl::IterateExp.__init__)


def test_jtl::essentialocl::iterateexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::IteratorExp)


def test_jtl::essentialocl::iteratorexp_constructor_exists():
    assert callable(JTL::essentialocl::IteratorExp.__init__)


def test_jtl::essentialocl::iteratorexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::IteratorExp.__init__)
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



def test_jtl::essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::LoopExp)


def test_jtl::essentialocl::loopexp_constructor_exists():
    assert callable(JTL::essentialocl::LoopExp.__init__)


def test_jtl::essentialocl::loopexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::listtype_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ListType)


def test_jtl::imperativeocl::listtype_constructor_exists():
    assert callable(JTL::imperativeocl::ListType.__init__)


def test_jtl::imperativeocl::listtype_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ListType.__init__)
    params = list(sig.parameters.keys())



def test_anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(AnonymousTupleLiteralPart)


def test_anonymoustupleliteralpart_constructor_exists():
    assert callable(AnonymousTupleLiteralPart.__init__)


def test_anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::anonymoustupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AnonymousTupleLiteralExp)


def test_jtl::imperativeocl::anonymoustupleliteralexp_constructor_exists():
    assert callable(JTL::imperativeocl::AnonymousTupleLiteralExp.__init__)


def test_jtl::imperativeocl::anonymoustupleliteralexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AnonymousTupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::logexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::LogExp)


def test_jtl::imperativeocl::logexp_constructor_exists():
    assert callable(JTL::imperativeocl::LogExp.__init__)


def test_jtl::imperativeocl::logexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::LogExp.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "text" in params, "Missing parameter 'text'"

def test_jtl::imperativeocl::logexp_has_level():
    assert hasattr(JTL::imperativeocl::LogExp, "level")
    descriptor = None
    for klass in JTL::imperativeocl::LogExp.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_jtl::imperativeocl::logexp_has_text():
    assert hasattr(JTL::imperativeocl::LogExp, "text")
    descriptor = None
    for klass in JTL::imperativeocl::LogExp.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(DictLiteralPart)


def test_dictliteralpart_constructor_exists():
    assert callable(DictLiteralPart.__init__)


def test_dictliteralpart_constructor_args():
    sig = inspect.signature(DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::dictliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::DictLiteralExp)


def test_jtl::imperativeocl::dictliteralexp_constructor_exists():
    assert callable(JTL::imperativeocl::DictLiteralExp.__init__)


def test_jtl::imperativeocl::dictliteralexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::DictLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::dictionarytype_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::DictionaryType)


def test_jtl::imperativeocl::dictionarytype_constructor_exists():
    assert callable(JTL::imperativeocl::DictionaryType.__init__)


def test_jtl::imperativeocl::dictionarytype_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::DictionaryType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::unpackexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::UnpackExp)


def test_jtl::imperativeocl::unpackexp_constructor_exists():
    assert callable(JTL::imperativeocl::UnpackExp.__init__)


def test_jtl::imperativeocl::unpackexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::UnpackExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::collectorexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::CollectorExp)


def test_jtl::imperativeocl::collectorexp_constructor_exists():
    assert callable(JTL::imperativeocl::CollectorExp.__init__)


def test_jtl::imperativeocl::collectorexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::CollectorExp.__init__)
    params = list(sig.parameters.keys())



def test_essentialocl::loopexp_is_not_abstract():
    assert not inspect.isabstract(essentialocl::LoopExp)


def test_essentialocl::loopexp_constructor_exists():
    assert callable(essentialocl::LoopExp.__init__)


def test_essentialocl::loopexp_constructor_args():
    sig = inspect.signature(essentialocl::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_logexp_is_not_abstract():
    assert not inspect.isabstract(LogExp)


def test_logexp_constructor_exists():
    assert callable(LogExp.__init__)


def test_logexp_constructor_args():
    sig = inspect.signature(LogExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::assertexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AssertExp)


def test_jtl::imperativeocl::assertexp_constructor_exists():
    assert callable(JTL::imperativeocl::AssertExp.__init__)


def test_jtl::imperativeocl::assertexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AssertExp.__init__)
    params = list(sig.parameters.keys())
    assert "severity" in params, "Missing parameter 'severity'"

def test_jtl::imperativeocl::assertexp_has_severity():
    assert hasattr(JTL::imperativeocl::AssertExp, "severity")
    descriptor = None
    for klass in JTL::imperativeocl::AssertExp.__mro__:
        if "severity" in klass.__dict__:
            descriptor = klass.__dict__["severity"]
            break
    assert isinstance(descriptor, property)



def test_jtl::imperativeocl::tryexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::TryExp)


def test_jtl::imperativeocl::tryexp_constructor_exists():
    assert callable(JTL::imperativeocl::TryExp.__init__)


def test_jtl::imperativeocl::tryexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::TryExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::breakexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::BreakExp)


def test_jtl::imperativeocl::breakexp_constructor_exists():
    assert callable(JTL::imperativeocl::BreakExp.__init__)


def test_jtl::imperativeocl::breakexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::BreakExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::returnexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ReturnExp)


def test_jtl::imperativeocl::returnexp_constructor_exists():
    assert callable(JTL::imperativeocl::ReturnExp.__init__)


def test_jtl::imperativeocl::returnexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ReturnExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::instantiationexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::InstantiationExp)


def test_jtl::imperativeocl::instantiationexp_constructor_exists():
    assert callable(JTL::imperativeocl::InstantiationExp.__init__)


def test_jtl::imperativeocl::instantiationexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::InstantiationExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::tupleexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::TupleExp)


def test_jtl::imperativeocl::tupleexp_constructor_exists():
    assert callable(JTL::imperativeocl::TupleExp.__init__)


def test_jtl::imperativeocl::tupleexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::forexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ForExp)


def test_jtl::imperativeocl::forexp_constructor_exists():
    assert callable(JTL::imperativeocl::ForExp.__init__)


def test_jtl::imperativeocl::forexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ForExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::continueexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ContinueExp)


def test_jtl::imperativeocl::continueexp_constructor_exists():
    assert callable(JTL::imperativeocl::ContinueExp.__init__)


def test_jtl::imperativeocl::continueexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ContinueExp.__init__)
    params = list(sig.parameters.keys())



def test_enumeration_is_not_abstract():
    assert not inspect.isabstract(Enumeration)


def test_enumeration_constructor_exists():
    assert callable(Enumeration.__init__)


def test_enumeration_constructor_args():
    sig = inspect.signature(Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::raiseexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::RaiseExp)


def test_jtl::imperativeocl::raiseexp_constructor_exists():
    assert callable(JTL::imperativeocl::RaiseExp.__init__)


def test_jtl::imperativeocl::raiseexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::RaiseExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::variableinitexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::VariableInitExp)


def test_jtl::imperativeocl::variableinitexp_constructor_exists():
    assert callable(JTL::imperativeocl::VariableInitExp.__init__)


def test_jtl::imperativeocl::variableinitexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::VariableInitExp.__init__)
    params = list(sig.parameters.keys())
    assert "withResult" in params, "Missing parameter 'withResult'"

def test_jtl::imperativeocl::variableinitexp_has_withResult():
    assert hasattr(JTL::imperativeocl::VariableInitExp, "withResult")
    descriptor = None
    for klass in JTL::imperativeocl::VariableInitExp.__mro__:
        if "withResult" in klass.__dict__:
            descriptor = klass.__dict__["withResult"]
            break
    assert isinstance(descriptor, property)



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



def test_jtl::imperativeocl::imperativeloopexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ImperativeLoopExp)


def test_jtl::imperativeocl::imperativeloopexp_constructor_exists():
    assert callable(JTL::imperativeocl::ImperativeLoopExp.__init__)


def test_jtl::imperativeocl::imperativeloopexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ImperativeLoopExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::switchexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::SwitchExp)


def test_jtl::imperativeocl::switchexp_constructor_exists():
    assert callable(JTL::imperativeocl::SwitchExp.__init__)


def test_jtl::imperativeocl::switchexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::SwitchExp.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::blockexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::BlockExp)


def test_jtl::imperativeocl::blockexp_constructor_exists():
    assert callable(JTL::imperativeocl::BlockExp.__init__)


def test_jtl::imperativeocl::blockexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::BlockExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::unlinkexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::UnlinkExp)


def test_jtl::imperativeocl::unlinkexp_constructor_exists():
    assert callable(JTL::imperativeocl::UnlinkExp.__init__)


def test_jtl::imperativeocl::unlinkexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::UnlinkExp.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::EnumerationLiteral)


def test_jtl::emof::enumerationliteral_constructor_exists():
    assert callable(JTL::emof::EnumerationLiteral.__init__)


def test_jtl::emof::enumerationliteral_constructor_args():
    sig = inspect.signature(JTL::emof::EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::type_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Type)


def test_jtl::emof::type_constructor_exists():
    assert callable(JTL::emof::Type.__init__)


def test_jtl::emof::type_constructor_args():
    sig = inspect.signature(JTL::emof::Type.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::altexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AltExp)


def test_jtl::imperativeocl::altexp_constructor_exists():
    assert callable(JTL::imperativeocl::AltExp.__init__)


def test_jtl::imperativeocl::altexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AltExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::package_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Package)


def test_jtl::emof::package_constructor_exists():
    assert callable(JTL::emof::Package.__init__)


def test_jtl::emof::package_constructor_args():
    sig = inspect.signature(JTL::emof::Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_jtl::emof::package_has_uri():
    assert hasattr(JTL::emof::Package, "uri")
    descriptor = None
    for klass in JTL::emof::Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_jtl::imperativeocl::computeexp_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ComputeExp)


def test_jtl::imperativeocl::computeexp_constructor_exists():
    assert callable(JTL::imperativeocl::ComputeExp.__init__)


def test_jtl::imperativeocl::computeexp_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ComputeExp.__init__)
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



def test_jtl::essentialocl::invalidtype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::InvalidType)


def test_jtl::essentialocl::invalidtype_constructor_exists():
    assert callable(JTL::essentialocl::InvalidType.__init__)


def test_jtl::essentialocl::invalidtype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::TemplateParameterType)


def test_jtl::imperativeocl::templateparametertype_constructor_exists():
    assert callable(JTL::imperativeocl::TemplateParameterType.__init__)


def test_jtl::imperativeocl::templateparametertype_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_jtl::imperativeocl::templateparametertype_has_specification():
    assert hasattr(JTL::imperativeocl::TemplateParameterType, "specification")
    descriptor = None
    for klass in JTL::imperativeocl::TemplateParameterType.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_jtl::essentialocl::voidtype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::VoidType)


def test_jtl::essentialocl::voidtype_constructor_exists():
    assert callable(JTL::essentialocl::VoidType.__init__)


def test_jtl::essentialocl::voidtype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::class_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Class)


def test_jtl::emof::class_constructor_exists():
    assert callable(JTL::emof::Class.__init__)


def test_jtl::emof::class_constructor_args():
    sig = inspect.signature(JTL::emof::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_jtl::emof::class_has_isAbstract():
    assert hasattr(JTL::emof::Class, "isAbstract")
    descriptor = None
    for klass in JTL::emof::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



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



def test_jtl::essentialocl::collectiontype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CollectionType)


def test_jtl::essentialocl::collectiontype_constructor_exists():
    assert callable(JTL::essentialocl::CollectionType.__init__)


def test_jtl::essentialocl::collectiontype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::enumeration_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Enumeration)


def test_jtl::emof::enumeration_constructor_exists():
    assert callable(JTL::emof::Enumeration.__init__)


def test_jtl::emof::enumeration_constructor_args():
    sig = inspect.signature(JTL::emof::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::anonymoustupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AnonymousTupleLiteralPart)


def test_jtl::imperativeocl::anonymoustupleliteralpart_constructor_exists():
    assert callable(JTL::imperativeocl::AnonymousTupleLiteralPart.__init__)


def test_jtl::imperativeocl::anonymoustupleliteralpart_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AnonymousTupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::namedelement_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::NamedElement)


def test_jtl::emof::namedelement_constructor_exists():
    assert callable(JTL::emof::NamedElement.__init__)


def test_jtl::emof::namedelement_constructor_args():
    sig = inspect.signature(JTL::emof::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_jtl::emof::namedelement_has_name():
    assert hasattr(JTL::emof::NamedElement, "name")
    descriptor = None
    for klass in JTL::emof::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_jtl::template::propertytemplateitem_is_not_abstract():
    assert not inspect.isabstract(JTL::template::PropertyTemplateItem)


def test_jtl::template::propertytemplateitem_constructor_exists():
    assert callable(JTL::template::PropertyTemplateItem.__init__)


def test_jtl::template::propertytemplateitem_constructor_args():
    sig = inspect.signature(JTL::template::PropertyTemplateItem.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::dictliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::DictLiteralPart)


def test_jtl::imperativeocl::dictliteralpart_constructor_exists():
    assert callable(JTL::imperativeocl::DictLiteralPart.__init__)


def test_jtl::imperativeocl::dictliteralpart_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::DictLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::tag_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Tag)


def test_jtl::emof::tag_constructor_exists():
    assert callable(JTL::emof::Tag.__init__)


def test_jtl::emof::tag_constructor_args():
    sig = inspect.signature(JTL::emof::Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_jtl::emof::tag_has_name():
    assert hasattr(JTL::emof::Tag, "name")
    descriptor = None
    for klass in JTL::emof::Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::tag_has_value():
    assert hasattr(JTL::emof::Tag, "value")
    descriptor = None
    for klass in JTL::emof::Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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



def test_jtl::emof::element_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Element)


def test_jtl::emof::element_constructor_exists():
    assert callable(JTL::emof::Element.__init__)


def test_jtl::emof::element_constructor_args():
    sig = inspect.signature(JTL::emof::Element.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::datatype_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::DataType)


def test_jtl::emof::datatype_constructor_exists():
    assert callable(JTL::emof::DataType.__init__)


def test_jtl::emof::datatype_constructor_args():
    sig = inspect.signature(JTL::emof::DataType.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::typedef_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::Typedef)


def test_jtl::imperativeocl::typedef_constructor_exists():
    assert callable(JTL::imperativeocl::Typedef.__init__)


def test_jtl::imperativeocl::typedef_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::Typedef.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::anonymoustupletype_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::AnonymousTupleType)


def test_jtl::imperativeocl::anonymoustupletype_constructor_exists():
    assert callable(JTL::imperativeocl::AnonymousTupleType.__init__)


def test_jtl::imperativeocl::anonymoustupletype_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::AnonymousTupleType.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::literalexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::LiteralExp)


def test_jtl::essentialocl::literalexp_constructor_exists():
    assert callable(JTL::essentialocl::LiteralExp.__init__)


def test_jtl::essentialocl::literalexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::typeexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::TypeExp)


def test_jtl::essentialocl::typeexp_constructor_exists():
    assert callable(JTL::essentialocl::TypeExp.__init__)


def test_jtl::essentialocl::typeexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::variableexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::VariableExp)


def test_jtl::essentialocl::variableexp_constructor_exists():
    assert callable(JTL::essentialocl::VariableExp.__init__)


def test_jtl::essentialocl::variableexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::imperativeocl::imperativeexpression_is_not_abstract():
    assert not inspect.isabstract(JTL::imperativeocl::ImperativeExpression)


def test_jtl::imperativeocl::imperativeexpression_constructor_exists():
    assert callable(JTL::imperativeocl::ImperativeExpression.__init__)


def test_jtl::imperativeocl::imperativeexpression_constructor_args():
    sig = inspect.signature(JTL::imperativeocl::ImperativeExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::letexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::LetExp)


def test_jtl::essentialocl::letexp_constructor_exists():
    assert callable(JTL::essentialocl::LetExp.__init__)


def test_jtl::essentialocl::letexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::predicate_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Predicate)


def test_jtl::jtl::predicate_constructor_exists():
    assert callable(JTL::JTL::Predicate.__init__)


def test_jtl::jtl::predicate_constructor_args():
    sig = inspect.signature(JTL::JTL::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_templateexp_is_not_abstract():
    assert not inspect.isabstract(TemplateExp)


def test_templateexp_constructor_exists():
    assert callable(TemplateExp.__init__)


def test_templateexp_constructor_args():
    sig = inspect.signature(TemplateExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::template::objecttemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL::template::ObjectTemplateExp)


def test_jtl::template::objecttemplateexp_constructor_exists():
    assert callable(JTL::template::ObjectTemplateExp.__init__)


def test_jtl::template::objecttemplateexp_constructor_args():
    sig = inspect.signature(JTL::template::ObjectTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "referredClass" in params, "Missing parameter 'referredClass'"

def test_jtl::template::objecttemplateexp_has_referredClass():
    assert hasattr(JTL::template::ObjectTemplateExp, "referredClass")
    descriptor = None
    for klass in JTL::template::ObjectTemplateExp.__mro__:
        if "referredClass" in klass.__dict__:
            descriptor = klass.__dict__["referredClass"]
            break
    assert isinstance(descriptor, property)



def test_jtl::template::collectiontemplateexp_is_not_abstract():
    assert not inspect.isabstract(JTL::template::CollectionTemplateExp)


def test_jtl::template::collectiontemplateexp_constructor_exists():
    assert callable(JTL::template::CollectionTemplateExp.__init__)


def test_jtl::template::collectiontemplateexp_constructor_args():
    sig = inspect.signature(JTL::template::CollectionTemplateExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_jtl::template::collectiontemplateexp_has_kind():
    assert hasattr(JTL::template::CollectionTemplateExp, "kind")
    descriptor = None
    for klass in JTL::template::CollectionTemplateExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_predicate_is_not_abstract():
    assert not inspect.isabstract(Predicate)


def test_predicate_constructor_exists():
    assert callable(Predicate.__init__)


def test_predicate_constructor_args():
    sig = inspect.signature(Predicate.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::pattern_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Pattern)


def test_jtl::jtl::pattern_constructor_exists():
    assert callable(JTL::JTL::Pattern.__init__)


def test_jtl::jtl::pattern_constructor_args():
    sig = inspect.signature(JTL::JTL::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::ifexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::IfExp)


def test_jtl::essentialocl::ifexp_constructor_exists():
    assert callable(JTL::essentialocl::IfExp.__init__)


def test_jtl::essentialocl::ifexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::IntegerLiteralExp)


def test_jtl::essentialocl::integerliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::IntegerLiteralExp.__init__)


def test_jtl::essentialocl::integerliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_jtl::essentialocl::integerliteralexp_has_integerSymbol():
    assert hasattr(JTL::essentialocl::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in JTL::essentialocl::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtl::essentialocl::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::RealLiteralExp)


def test_jtl::essentialocl::realliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::RealLiteralExp.__init__)


def test_jtl::essentialocl::realliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_jtl::essentialocl::realliteralexp_has_realSymbol():
    assert hasattr(JTL::essentialocl::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in JTL::essentialocl::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtl::essentialocl::unlimitednaturalexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::UnlimitedNaturalExp)


def test_jtl::essentialocl::unlimitednaturalexp_constructor_exists():
    assert callable(JTL::essentialocl::UnlimitedNaturalExp.__init__)


def test_jtl::essentialocl::unlimitednaturalexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::UnlimitedNaturalExp.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_jtl::essentialocl::unlimitednaturalexp_has_symbol():
    assert hasattr(JTL::essentialocl::UnlimitedNaturalExp, "symbol")
    descriptor = None
    for klass in JTL::essentialocl::UnlimitedNaturalExp.__mro__:
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



def test_jtl::essentialocl::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CollectionLiteralPart)


def test_jtl::essentialocl::collectionliteralpart_constructor_exists():
    assert callable(JTL::essentialocl::CollectionLiteralPart.__init__)


def test_jtl::essentialocl::collectionliteralpart_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::TupleLiteralPart)


def test_jtl::essentialocl::tupleliteralpart_constructor_exists():
    assert callable(JTL::essentialocl::TupleLiteralPart.__init__)


def test_jtl::essentialocl::tupleliteralpart_constructor_args():
    sig = inspect.signature(JTL::essentialocl::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::variable_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::Variable)


def test_jtl::essentialocl::variable_constructor_exists():
    assert callable(JTL::essentialocl::Variable.__init__)


def test_jtl::essentialocl::variable_constructor_args():
    sig = inspect.signature(JTL::essentialocl::Variable.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::OclExpression)


def test_jtl::essentialocl::oclexpression_constructor_exists():
    assert callable(JTL::essentialocl::OclExpression.__init__)


def test_jtl::essentialocl::oclexpression_constructor_args():
    sig = inspect.signature(JTL::essentialocl::OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::callexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::CallExp)


def test_jtl::essentialocl::callexp_constructor_exists():
    assert callable(JTL::essentialocl::CallExp.__init__)


def test_jtl::essentialocl::callexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::StringLiteralExp)


def test_jtl::essentialocl::stringliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::StringLiteralExp.__init__)


def test_jtl::essentialocl::stringliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_jtl::essentialocl::stringliteralexp_has_stringSymbol():
    assert hasattr(JTL::essentialocl::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in JTL::essentialocl::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_jtl::essentialocl::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::NumericLiteralExp)


def test_jtl::essentialocl::numericliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::NumericLiteralExp.__init__)


def test_jtl::essentialocl::numericliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::BooleanLiteralExp)


def test_jtl::essentialocl::booleanliteralexp_constructor_exists():
    assert callable(JTL::essentialocl::BooleanLiteralExp.__init__)


def test_jtl::essentialocl::booleanliteralexp_constructor_args():
    sig = inspect.signature(JTL::essentialocl::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_jtl::essentialocl::booleanliteralexp_has_booleanSymbol():
    assert hasattr(JTL::essentialocl::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in JTL::essentialocl::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



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



def test_jtl::essentialocl::tupletype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::TupleType)


def test_jtl::essentialocl::tupletype_constructor_exists():
    assert callable(JTL::essentialocl::TupleType.__init__)


def test_jtl::essentialocl::tupletype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::essentialocl::anytype_is_not_abstract():
    assert not inspect.isabstract(JTL::essentialocl::AnyType)


def test_jtl::essentialocl::anytype_constructor_exists():
    assert callable(JTL::essentialocl::AnyType.__init__)


def test_jtl::essentialocl::anytype_constructor_args():
    sig = inspect.signature(JTL::essentialocl::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::transformation_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Transformation)


def test_jtl::jtl::transformation_constructor_exists():
    assert callable(JTL::JTL::Transformation.__init__)


def test_jtl::jtl::transformation_constructor_args():
    sig = inspect.signature(JTL::JTL::Transformation.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::comment_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Comment)


def test_jtl::emof::comment_constructor_exists():
    assert callable(JTL::emof::Comment.__init__)


def test_jtl::emof::comment_constructor_args():
    sig = inspect.signature(JTL::emof::Comment.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::uriextent_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::URIExtent)


def test_jtl::emof::uriextent_constructor_exists():
    assert callable(JTL::emof::URIExtent.__init__)


def test_jtl::emof::uriextent_constructor_args():
    sig = inspect.signature(JTL::emof::URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::primitivetype_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::PrimitiveType)


def test_jtl::emof::primitivetype_constructor_exists():
    assert callable(JTL::emof::PrimitiveType.__init__)


def test_jtl::emof::primitivetype_constructor_args():
    sig = inspect.signature(JTL::emof::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::typedelement_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::TypedElement)


def test_jtl::emof::typedelement_constructor_exists():
    assert callable(JTL::emof::TypedElement.__init__)


def test_jtl::emof::typedelement_constructor_args():
    sig = inspect.signature(JTL::emof::TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_jtl::emof::typedelement_has_type():
    assert hasattr(JTL::emof::TypedElement, "type")
    descriptor = None
    for klass in JTL::emof::TypedElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_jtl::jtl::model_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Model)


def test_jtl::jtl::model_constructor_exists():
    assert callable(JTL::JTL::Model.__init__)


def test_jtl::jtl::model_constructor_args():
    sig = inspect.signature(JTL::JTL::Model.__init__)
    params = list(sig.parameters.keys())
    assert "usedPackage" in params, "Missing parameter 'usedPackage'"

def test_jtl::jtl::model_has_usedPackage():
    assert hasattr(JTL::JTL::Model, "usedPackage")
    descriptor = None
    for klass in JTL::JTL::Model.__mro__:
        if "usedPackage" in klass.__dict__:
            descriptor = klass.__dict__["usedPackage"]
            break
    assert isinstance(descriptor, property)



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::where_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Where)


def test_jtl::jtl::where_constructor_exists():
    assert callable(JTL::JTL::Where.__init__)


def test_jtl::jtl::where_constructor_args():
    sig = inspect.signature(JTL::JTL::Where.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::when_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::When)


def test_jtl::jtl::when_constructor_exists():
    assert callable(JTL::JTL::When.__init__)


def test_jtl::jtl::when_constructor_args():
    sig = inspect.signature(JTL::JTL::When.__init__)
    params = list(sig.parameters.keys())



def test_jtl::jtl::domain_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Domain)


def test_jtl::jtl::domain_constructor_exists():
    assert callable(JTL::JTL::Domain.__init__)


def test_jtl::jtl::domain_constructor_args():
    sig = inspect.signature(JTL::JTL::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "isCheckable" in params, "Missing parameter 'isCheckable'"
    assert "isEnforceable" in params, "Missing parameter 'isEnforceable'"

def test_jtl::jtl::domain_has_isCheckable():
    assert hasattr(JTL::JTL::Domain, "isCheckable")
    descriptor = None
    for klass in JTL::JTL::Domain.__mro__:
        if "isCheckable" in klass.__dict__:
            descriptor = klass.__dict__["isCheckable"]
            break
    assert isinstance(descriptor, property)

def test_jtl::jtl::domain_has_isEnforceable():
    assert hasattr(JTL::JTL::Domain, "isEnforceable")
    descriptor = None
    for klass in JTL::JTL::Domain.__mro__:
        if "isEnforceable" in klass.__dict__:
            descriptor = klass.__dict__["isEnforceable"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_when_is_not_abstract():
    assert not inspect.isabstract(When)


def test_when_constructor_exists():
    assert callable(When.__init__)


def test_when_constructor_args():
    sig = inspect.signature(When.__init__)
    params = list(sig.parameters.keys())



def test_where_is_not_abstract():
    assert not inspect.isabstract(Where)


def test_where_constructor_exists():
    assert callable(Where.__init__)


def test_where_constructor_args():
    sig = inspect.signature(Where.__init__)
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



def test_jtl::jtl::relation_is_not_abstract():
    assert not inspect.isabstract(JTL::JTL::Relation)


def test_jtl::jtl::relation_constructor_exists():
    assert callable(JTL::JTL::Relation.__init__)


def test_jtl::jtl::relation_constructor_args():
    sig = inspect.signature(JTL::JTL::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopLevel" in params, "Missing parameter 'isTopLevel'"

def test_jtl::jtl::relation_has_isTopLevel():
    assert hasattr(JTL::JTL::Relation, "isTopLevel")
    descriptor = None
    for klass in JTL::JTL::Relation.__mro__:
        if "isTopLevel" in klass.__dict__:
            descriptor = klass.__dict__["isTopLevel"]
            break
    assert isinstance(descriptor, property)



def test_jtl::emof::multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::MultiplicityElement)


def test_jtl::emof::multiplicityelement_constructor_exists():
    assert callable(JTL::emof::MultiplicityElement.__init__)


def test_jtl::emof::multiplicityelement_constructor_args():
    sig = inspect.signature(JTL::emof::MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_jtl::emof::multiplicityelement_has_lower():
    assert hasattr(JTL::emof::MultiplicityElement, "lower")
    descriptor = None
    for klass in JTL::emof::MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::multiplicityelement_has_upper():
    assert hasattr(JTL::emof::MultiplicityElement, "upper")
    descriptor = None
    for klass in JTL::emof::MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::multiplicityelement_has_isOrdered():
    assert hasattr(JTL::emof::MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in JTL::emof::MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::multiplicityelement_has_isUnique():
    assert hasattr(JTL::emof::MultiplicityElement, "isUnique")
    descriptor = None
    for klass in JTL::emof::MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
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



def test_jtl::emof::property_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Property)


def test_jtl::emof::property_constructor_exists():
    assert callable(JTL::emof::Property.__init__)


def test_jtl::emof::property_constructor_args():
    sig = inspect.signature(JTL::emof::Property.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isId" in params, "Missing parameter 'isId'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"

def test_jtl::emof::property_has_isReadOnly():
    assert hasattr(JTL::emof::Property, "isReadOnly")
    descriptor = None
    for klass in JTL::emof::Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::property_has_isId():
    assert hasattr(JTL::emof::Property, "isId")
    descriptor = None
    for klass in JTL::emof::Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::property_has_isComposite():
    assert hasattr(JTL::emof::Property, "isComposite")
    descriptor = None
    for klass in JTL::emof::Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::property_has_isDerived():
    assert hasattr(JTL::emof::Property, "isDerived")
    descriptor = None
    for klass in JTL::emof::Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_jtl::emof::property_has_default():
    assert hasattr(JTL::emof::Property, "default")
    descriptor = None
    for klass in JTL::emof::Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_jtl::emof::parameter_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Parameter)


def test_jtl::emof::parameter_constructor_exists():
    assert callable(JTL::emof::Parameter.__init__)


def test_jtl::emof::parameter_constructor_args():
    sig = inspect.signature(JTL::emof::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::operation_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Operation)


def test_jtl::emof::operation_constructor_exists():
    assert callable(JTL::emof::Operation.__init__)


def test_jtl::emof::operation_constructor_args():
    sig = inspect.signature(JTL::emof::Operation.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::object_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Object)


def test_jtl::emof::object_constructor_exists():
    assert callable(JTL::emof::Object.__init__)


def test_jtl::emof::object_constructor_args():
    sig = inspect.signature(JTL::emof::Object.__init__)
    params = list(sig.parameters.keys())



def test_jtl::emof::extent_is_not_abstract():
    assert not inspect.isabstract(JTL::emof::Extent)


def test_jtl::emof::extent_constructor_exists():
    assert callable(JTL::emof::Extent.__init__)


def test_jtl::emof::extent_constructor_args():
    sig = inspect.signature(JTL::emof::Extent.__init__)
    params = list(sig.parameters.keys())

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

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "OrderedSet",
        "Set",
        "Bag",
        "Sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
AssignExp_strategy = st.builds(
    AssignExp,
)
PropertyTemplateItem_strategy = st.builds(
    PropertyTemplateItem,
)
ImperativeExpression_strategy = st.builds(
    ImperativeExpression,
)
JTL::imperativeocl::WhileExp_strategy = st.builds(
    JTL::imperativeocl::WhileExp,
)
JTL::imperativeocl::AssignExp_strategy = st.builds(
    JTL::imperativeocl::AssignExp,
    isReset=
        st.booleans()
)
ImperativeLoopExp_strategy = st.builds(
    ImperativeLoopExp,
)
JTL::imperativeocl::ImperativeIterateExp_strategy = st.builds(
    JTL::imperativeocl::ImperativeIterateExp,
)
ObjectTemplateExp_strategy = st.builds(
    ObjectTemplateExp,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
JTL::essentialocl::BagType_strategy = st.builds(
    JTL::essentialocl::BagType,
)
TupleLiteralExp_strategy = st.builds(
    TupleLiteralExp,
)
CallExp_strategy = st.builds(
    CallExp,
)
JTL::essentialocl::FeaturePropertyCall_strategy = st.builds(
    JTL::essentialocl::FeaturePropertyCall,
)
JTL::essentialocl::OpaqueExpression_strategy = st.builds(
    JTL::essentialocl::OpaqueExpression,
)
emof::Type_strategy = st.builds(
    emof::Type,
)
emof::DataType_strategy = st.builds(
    emof::DataType,
)
JTL::essentialocl::SetType_strategy = st.builds(
    JTL::essentialocl::SetType,
)
JTL::essentialocl::SequenceType_strategy = st.builds(
    JTL::essentialocl::SequenceType,
)
JTL::essentialocl::OrderedSetType_strategy = st.builds(
    JTL::essentialocl::OrderedSetType,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
JTL::essentialocl::CollectionLiteralExp_strategy = st.builds(
    JTL::essentialocl::CollectionLiteralExp,
    kind=
        safe_text
)
JTL::essentialocl::InvalidLiteralExp_strategy = st.builds(
    JTL::essentialocl::InvalidLiteralExp,
)
JTL::template::TemplateExp_strategy = st.builds(
    JTL::template::TemplateExp,
)
JTL::essentialocl::EnumLiteralExp_strategy = st.builds(
    JTL::essentialocl::EnumLiteralExp,
)
JTL::essentialocl::PrimitiveLiteralExp_strategy = st.builds(
    JTL::essentialocl::PrimitiveLiteralExp,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
JTL::essentialocl::ExpressionInOcl_strategy = st.builds(
    JTL::essentialocl::ExpressionInOcl,
)
JTL::essentialocl::NullLiteralExp_strategy = st.builds(
    JTL::essentialocl::NullLiteralExp,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
JTL::essentialocl::TupleLiteralExp_strategy = st.builds(
    JTL::essentialocl::TupleLiteralExp,
)
JTL::essentialocl::CollectionRange_strategy = st.builds(
    JTL::essentialocl::CollectionRange,
)
JTL::essentialocl::CollectionItem_strategy = st.builds(
    JTL::essentialocl::CollectionItem,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
JTL::essentialocl::PropertyCallExp_strategy = st.builds(
    JTL::essentialocl::PropertyCallExp,
)
ComputeExp_strategy = st.builds(
    ComputeExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
JTL::essentialocl::OperationCallExp_strategy = st.builds(
    JTL::essentialocl::OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
JTL::essentialocl::IterateExp_strategy = st.builds(
    JTL::essentialocl::IterateExp,
)
JTL::essentialocl::IteratorExp_strategy = st.builds(
    JTL::essentialocl::IteratorExp,
)
essentialocl::OclExpression_strategy = st.builds(
    essentialocl::OclExpression,
)
essentialocl::CallExp_strategy = st.builds(
    essentialocl::CallExp,
)
JTL::essentialocl::LoopExp_strategy = st.builds(
    JTL::essentialocl::LoopExp,
)
JTL::imperativeocl::ListType_strategy = st.builds(
    JTL::imperativeocl::ListType,
)
AnonymousTupleLiteralPart_strategy = st.builds(
    AnonymousTupleLiteralPart,
)
JTL::imperativeocl::AnonymousTupleLiteralExp_strategy = st.builds(
    JTL::imperativeocl::AnonymousTupleLiteralExp,
)
JTL::imperativeocl::LogExp_strategy = st.builds(
    JTL::imperativeocl::LogExp,
    level=
        st.integers(),
    text=
        safe_text
)
DictLiteralPart_strategy = st.builds(
    DictLiteralPart,
)
JTL::imperativeocl::DictLiteralExp_strategy = st.builds(
    JTL::imperativeocl::DictLiteralExp,
)
JTL::imperativeocl::DictionaryType_strategy = st.builds(
    JTL::imperativeocl::DictionaryType,
)
JTL::imperativeocl::UnpackExp_strategy = st.builds(
    JTL::imperativeocl::UnpackExp,
)
JTL::imperativeocl::CollectorExp_strategy = st.builds(
    JTL::imperativeocl::CollectorExp,
)
essentialocl::LoopExp_strategy = st.builds(
    essentialocl::LoopExp,
)
LogExp_strategy = st.builds(
    LogExp,
)
JTL::imperativeocl::AssertExp_strategy = st.builds(
    JTL::imperativeocl::AssertExp,
    severity=
        safe_text
)
JTL::imperativeocl::TryExp_strategy = st.builds(
    JTL::imperativeocl::TryExp,
)
JTL::imperativeocl::BreakExp_strategy = st.builds(
    JTL::imperativeocl::BreakExp,
)
JTL::imperativeocl::ReturnExp_strategy = st.builds(
    JTL::imperativeocl::ReturnExp,
)
JTL::imperativeocl::InstantiationExp_strategy = st.builds(
    JTL::imperativeocl::InstantiationExp,
)
JTL::imperativeocl::TupleExp_strategy = st.builds(
    JTL::imperativeocl::TupleExp,
)
JTL::imperativeocl::ForExp_strategy = st.builds(
    JTL::imperativeocl::ForExp,
)
JTL::imperativeocl::ContinueExp_strategy = st.builds(
    JTL::imperativeocl::ContinueExp,
)
Enumeration_strategy = st.builds(
    Enumeration,
)
JTL::imperativeocl::RaiseExp_strategy = st.builds(
    JTL::imperativeocl::RaiseExp,
)
JTL::imperativeocl::VariableInitExp_strategy = st.builds(
    JTL::imperativeocl::VariableInitExp,
    withResult=
        st.booleans()
)
AltExp_strategy = st.builds(
    AltExp,
)
imperativeocl::ImperativeExpression_strategy = st.builds(
    imperativeocl::ImperativeExpression,
)
JTL::imperativeocl::ImperativeLoopExp_strategy = st.builds(
    JTL::imperativeocl::ImperativeLoopExp,
)
JTL::imperativeocl::SwitchExp_strategy = st.builds(
    JTL::imperativeocl::SwitchExp,
)
Package_strategy = st.builds(
    Package,
)
JTL::imperativeocl::BlockExp_strategy = st.builds(
    JTL::imperativeocl::BlockExp,
)
JTL::imperativeocl::UnlinkExp_strategy = st.builds(
    JTL::imperativeocl::UnlinkExp,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
JTL::emof::EnumerationLiteral_strategy = st.builds(
    JTL::emof::EnumerationLiteral,
)
JTL::emof::Type_strategy = st.builds(
    JTL::emof::Type,
)
JTL::imperativeocl::AltExp_strategy = st.builds(
    JTL::imperativeocl::AltExp,
)
JTL::emof::Package_strategy = st.builds(
    JTL::emof::Package,
    uri=
        safe_text
)
JTL::imperativeocl::ComputeExp_strategy = st.builds(
    JTL::imperativeocl::ComputeExp,
)
Property_strategy = st.builds(
    Property,
)
Type_strategy = st.builds(
    Type,
)
JTL::essentialocl::InvalidType_strategy = st.builds(
    JTL::essentialocl::InvalidType,
)
JTL::imperativeocl::TemplateParameterType_strategy = st.builds(
    JTL::imperativeocl::TemplateParameterType,
    specification=
        safe_text
)
JTL::essentialocl::VoidType_strategy = st.builds(
    JTL::essentialocl::VoidType,
)
JTL::emof::Class_strategy = st.builds(
    JTL::emof::Class,
    isAbstract=
        st.booleans()
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
JTL::essentialocl::CollectionType_strategy = st.builds(
    JTL::essentialocl::CollectionType,
)
JTL::emof::Enumeration_strategy = st.builds(
    JTL::emof::Enumeration,
)
Element_strategy = st.builds(
    Element,
)
JTL::imperativeocl::AnonymousTupleLiteralPart_strategy = st.builds(
    JTL::imperativeocl::AnonymousTupleLiteralPart,
)
JTL::emof::NamedElement_strategy = st.builds(
    JTL::emof::NamedElement,
    name=
        safe_text
)
JTL::template::PropertyTemplateItem_strategy = st.builds(
    JTL::template::PropertyTemplateItem,
)
JTL::imperativeocl::DictLiteralPart_strategy = st.builds(
    JTL::imperativeocl::DictLiteralPart,
)
JTL::emof::Tag_strategy = st.builds(
    JTL::emof::Tag,
    name=
        safe_text,
    value=
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
JTL::emof::Element_strategy = st.builds(
    JTL::emof::Element,
)
JTL::emof::DataType_strategy = st.builds(
    JTL::emof::DataType,
)
Class_strategy = st.builds(
    Class,
)
JTL::imperativeocl::Typedef_strategy = st.builds(
    JTL::imperativeocl::Typedef,
)
JTL::imperativeocl::AnonymousTupleType_strategy = st.builds(
    JTL::imperativeocl::AnonymousTupleType,
)
Operation_strategy = st.builds(
    Operation,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
JTL::essentialocl::LiteralExp_strategy = st.builds(
    JTL::essentialocl::LiteralExp,
)
JTL::essentialocl::TypeExp_strategy = st.builds(
    JTL::essentialocl::TypeExp,
)
JTL::essentialocl::VariableExp_strategy = st.builds(
    JTL::essentialocl::VariableExp,
)
JTL::imperativeocl::ImperativeExpression_strategy = st.builds(
    JTL::imperativeocl::ImperativeExpression,
)
JTL::essentialocl::LetExp_strategy = st.builds(
    JTL::essentialocl::LetExp,
)
JTL::JTL::Predicate_strategy = st.builds(
    JTL::JTL::Predicate,
)
TemplateExp_strategy = st.builds(
    TemplateExp,
)
JTL::template::ObjectTemplateExp_strategy = st.builds(
    JTL::template::ObjectTemplateExp,
    referredClass=
        safe_text
)
JTL::template::CollectionTemplateExp_strategy = st.builds(
    JTL::template::CollectionTemplateExp,
    kind=
        safe_text
)
Predicate_strategy = st.builds(
    Predicate,
)
JTL::JTL::Pattern_strategy = st.builds(
    JTL::JTL::Pattern,
)
JTL::essentialocl::IfExp_strategy = st.builds(
    JTL::essentialocl::IfExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
JTL::essentialocl::IntegerLiteralExp_strategy = st.builds(
    JTL::essentialocl::IntegerLiteralExp,
    integerSymbol=
        st.integers()
)
JTL::essentialocl::RealLiteralExp_strategy = st.builds(
    JTL::essentialocl::RealLiteralExp,
    realSymbol=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
JTL::essentialocl::UnlimitedNaturalExp_strategy = st.builds(
    JTL::essentialocl::UnlimitedNaturalExp,
    symbol=
        safe_text
)
TryExp_strategy = st.builds(
    TryExp,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
JTL::essentialocl::CollectionLiteralPart_strategy = st.builds(
    JTL::essentialocl::CollectionLiteralPart,
)
JTL::essentialocl::TupleLiteralPart_strategy = st.builds(
    JTL::essentialocl::TupleLiteralPart,
)
JTL::essentialocl::Variable_strategy = st.builds(
    JTL::essentialocl::Variable,
)
JTL::essentialocl::OclExpression_strategy = st.builds(
    JTL::essentialocl::OclExpression,
)
JTL::essentialocl::CallExp_strategy = st.builds(
    JTL::essentialocl::CallExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
JTL::essentialocl::StringLiteralExp_strategy = st.builds(
    JTL::essentialocl::StringLiteralExp,
    stringSymbol=
        safe_text
)
JTL::essentialocl::NumericLiteralExp_strategy = st.builds(
    JTL::essentialocl::NumericLiteralExp,
)
JTL::essentialocl::BooleanLiteralExp_strategy = st.builds(
    JTL::essentialocl::BooleanLiteralExp,
    booleanSymbol=
        st.booleans()
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
JTL::essentialocl::TupleType_strategy = st.builds(
    JTL::essentialocl::TupleType,
)
JTL::essentialocl::AnyType_strategy = st.builds(
    JTL::essentialocl::AnyType,
)
JTL::JTL::Transformation_strategy = st.builds(
    JTL::JTL::Transformation,
)
JTL::emof::Comment_strategy = st.builds(
    JTL::emof::Comment,
)
Extent_strategy = st.builds(
    Extent,
)
JTL::emof::URIExtent_strategy = st.builds(
    JTL::emof::URIExtent,
)
JTL::emof::PrimitiveType_strategy = st.builds(
    JTL::emof::PrimitiveType,
)
JTL::emof::TypedElement_strategy = st.builds(
    JTL::emof::TypedElement,
    type=
        safe_text
)
JTL::JTL::Model_strategy = st.builds(
    JTL::JTL::Model,
    usedPackage=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
JTL::JTL::Where_strategy = st.builds(
    JTL::JTL::Where,
)
JTL::JTL::When_strategy = st.builds(
    JTL::JTL::When,
)
JTL::JTL::Domain_strategy = st.builds(
    JTL::JTL::Domain,
    isCheckable=
        st.booleans(),
    isEnforceable=
        st.booleans()
)
Variable_strategy = st.builds(
    Variable,
)
When_strategy = st.builds(
    When,
)
Where_strategy = st.builds(
    Where,
)
Domain_strategy = st.builds(
    Domain,
)
Transformation_strategy = st.builds(
    Transformation,
)
JTL::JTL::Relation_strategy = st.builds(
    JTL::JTL::Relation,
    isTopLevel=
        st.booleans()
)
JTL::emof::MultiplicityElement_strategy = st.builds(
    JTL::emof::MultiplicityElement,
    lower=
        st.integers(),
    upper=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
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
JTL::emof::Property_strategy = st.builds(
    JTL::emof::Property,
    isReadOnly=
        st.booleans(),
    isId=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerived=
        st.booleans(),
    default=
        safe_text
)
JTL::emof::Parameter_strategy = st.builds(
    JTL::emof::Parameter,
)
JTL::emof::Operation_strategy = st.builds(
    JTL::emof::Operation,
)
JTL::emof::Object_strategy = st.builds(
    JTL::emof::Object,
)
JTL::emof::Extent_strategy = st.builds(
    JTL::emof::Extent,
)

@given(instance=AssignExp_strategy)
@settings(max_examples=50)
def test_assignexp_instantiation(instance):
    assert isinstance(instance, AssignExp)

@given(instance=PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_propertytemplateitem_instantiation(instance):
    assert isinstance(instance, PropertyTemplateItem)

@given(instance=ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeexpression_instantiation(instance):
    assert isinstance(instance, ImperativeExpression)

@given(instance=JTL::imperativeocl::WhileExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::whileexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::WhileExp)

@given(instance=JTL::imperativeocl::AssignExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::assignexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AssignExp)

@given(instance=JTL::imperativeocl::AssignExp_strategy)
def test_jtl::imperativeocl::assignexp_isReset_type(instance):
    assert isinstance(instance.isReset, bool)


@given(instance=JTL::imperativeocl::AssignExp_strategy)
def test_jtl::imperativeocl::assignexp_isReset_setter(instance):
    original = instance.isReset
    instance.isReset = original
    assert instance.isReset == original

@given(instance=ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_imperativeloopexp_instantiation(instance):
    assert isinstance(instance, ImperativeLoopExp)

@given(instance=JTL::imperativeocl::ImperativeIterateExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::imperativeiterateexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ImperativeIterateExp)

@given(instance=ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_objecttemplateexp_instantiation(instance):
    assert isinstance(instance, ObjectTemplateExp)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=JTL::essentialocl::BagType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::bagtype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::BagType)

@given(instance=TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, TupleLiteralExp)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=JTL::essentialocl::FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::featurepropertycall_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::FeaturePropertyCall)

@given(instance=JTL::essentialocl::OpaqueExpression_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::opaqueexpression_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::OpaqueExpression)

@given(instance=emof::Type_strategy)
@settings(max_examples=50)
def test_emof::type_instantiation(instance):
    assert isinstance(instance, emof::Type)

@given(instance=emof::DataType_strategy)
@settings(max_examples=50)
def test_emof::datatype_instantiation(instance):
    assert isinstance(instance, emof::DataType)

@given(instance=JTL::essentialocl::SetType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::settype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::SetType)

@given(instance=JTL::essentialocl::SequenceType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::sequencetype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::SequenceType)

@given(instance=JTL::essentialocl::OrderedSetType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::orderedsettype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::OrderedSetType)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=JTL::essentialocl::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CollectionLiteralExp)

@given(instance=JTL::essentialocl::CollectionLiteralExp_strategy)
def test_jtl::essentialocl::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=JTL::essentialocl::CollectionLiteralExp_strategy)
def test_jtl::essentialocl::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=JTL::essentialocl::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::InvalidLiteralExp)

@given(instance=JTL::template::TemplateExp_strategy)
@settings(max_examples=50)
def test_jtl::template::templateexp_instantiation(instance):
    assert isinstance(instance, JTL::template::TemplateExp)

@given(instance=JTL::essentialocl::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::enumliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::EnumLiteralExp)

@given(instance=JTL::essentialocl::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::PrimitiveLiteralExp)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=JTL::essentialocl::ExpressionInOcl_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::expressioninocl_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::ExpressionInOcl)

@given(instance=JTL::essentialocl::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::nullliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::NullLiteralExp)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=JTL::essentialocl::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::TupleLiteralExp)

@given(instance=JTL::essentialocl::CollectionRange_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::collectionrange_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CollectionRange)

@given(instance=JTL::essentialocl::CollectionItem_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::collectionitem_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CollectionItem)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=JTL::essentialocl::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::PropertyCallExp)

@given(instance=ComputeExp_strategy)
@settings(max_examples=50)
def test_computeexp_instantiation(instance):
    assert isinstance(instance, ComputeExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=JTL::essentialocl::OperationCallExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::OperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=JTL::essentialocl::IterateExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::iterateexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::IterateExp)

@given(instance=JTL::essentialocl::IteratorExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::iteratorexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::IteratorExp)

@given(instance=essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, essentialocl::OclExpression)

@given(instance=essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, essentialocl::CallExp)

@given(instance=JTL::essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::LoopExp)

@given(instance=JTL::imperativeocl::ListType_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::listtype_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ListType)

@given(instance=AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, AnonymousTupleLiteralPart)

@given(instance=JTL::imperativeocl::AnonymousTupleLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::anonymoustupleliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AnonymousTupleLiteralExp)

@given(instance=JTL::imperativeocl::LogExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::logexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::LogExp)

@given(instance=JTL::imperativeocl::LogExp_strategy)
def test_jtl::imperativeocl::logexp_level_type(instance):
    assert isinstance(instance.level, int)


@given(instance=JTL::imperativeocl::LogExp_strategy)
def test_jtl::imperativeocl::logexp_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=JTL::imperativeocl::LogExp_strategy)
def test_jtl::imperativeocl::logexp_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=JTL::imperativeocl::LogExp_strategy)
def test_jtl::imperativeocl::logexp_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=DictLiteralPart_strategy)
@settings(max_examples=50)
def test_dictliteralpart_instantiation(instance):
    assert isinstance(instance, DictLiteralPart)

@given(instance=JTL::imperativeocl::DictLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::dictliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::DictLiteralExp)

@given(instance=JTL::imperativeocl::DictionaryType_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::dictionarytype_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::DictionaryType)

@given(instance=JTL::imperativeocl::UnpackExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::unpackexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::UnpackExp)

@given(instance=JTL::imperativeocl::CollectorExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::collectorexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::CollectorExp)

@given(instance=essentialocl::LoopExp_strategy)
@settings(max_examples=50)
def test_essentialocl::loopexp_instantiation(instance):
    assert isinstance(instance, essentialocl::LoopExp)

@given(instance=LogExp_strategy)
@settings(max_examples=50)
def test_logexp_instantiation(instance):
    assert isinstance(instance, LogExp)

@given(instance=JTL::imperativeocl::AssertExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::assertexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AssertExp)

@given(instance=JTL::imperativeocl::AssertExp_strategy)
def test_jtl::imperativeocl::assertexp_severity_type(instance):
    assert isinstance(instance.severity, str)


@given(instance=JTL::imperativeocl::AssertExp_strategy)
def test_jtl::imperativeocl::assertexp_severity_setter(instance):
    original = instance.severity
    instance.severity = original
    assert instance.severity == original

@given(instance=JTL::imperativeocl::TryExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::tryexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::TryExp)

@given(instance=JTL::imperativeocl::BreakExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::breakexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::BreakExp)

@given(instance=JTL::imperativeocl::ReturnExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::returnexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ReturnExp)

@given(instance=JTL::imperativeocl::InstantiationExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::instantiationexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::InstantiationExp)

@given(instance=JTL::imperativeocl::TupleExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::tupleexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::TupleExp)

@given(instance=JTL::imperativeocl::ForExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::forexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ForExp)

@given(instance=JTL::imperativeocl::ContinueExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::continueexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ContinueExp)

@given(instance=Enumeration_strategy)
@settings(max_examples=50)
def test_enumeration_instantiation(instance):
    assert isinstance(instance, Enumeration)

@given(instance=JTL::imperativeocl::RaiseExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::raiseexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::RaiseExp)

@given(instance=JTL::imperativeocl::VariableInitExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::variableinitexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::VariableInitExp)

@given(instance=JTL::imperativeocl::VariableInitExp_strategy)
def test_jtl::imperativeocl::variableinitexp_withResult_type(instance):
    assert isinstance(instance.withResult, bool)


@given(instance=JTL::imperativeocl::VariableInitExp_strategy)
def test_jtl::imperativeocl::variableinitexp_withResult_setter(instance):
    original = instance.withResult
    instance.withResult = original
    assert instance.withResult == original

@given(instance=AltExp_strategy)
@settings(max_examples=50)
def test_altexp_instantiation(instance):
    assert isinstance(instance, AltExp)

@given(instance=imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, imperativeocl::ImperativeExpression)

@given(instance=JTL::imperativeocl::ImperativeLoopExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::imperativeloopexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ImperativeLoopExp)

@given(instance=JTL::imperativeocl::SwitchExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::switchexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::SwitchExp)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=JTL::imperativeocl::BlockExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::blockexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::BlockExp)

@given(instance=JTL::imperativeocl::UnlinkExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::unlinkexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::UnlinkExp)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=JTL::emof::EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_jtl::emof::enumerationliteral_instantiation(instance):
    assert isinstance(instance, JTL::emof::EnumerationLiteral)

@given(instance=JTL::emof::Type_strategy)
@settings(max_examples=50)
def test_jtl::emof::type_instantiation(instance):
    assert isinstance(instance, JTL::emof::Type)

@given(instance=JTL::imperativeocl::AltExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::altexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AltExp)

@given(instance=JTL::emof::Package_strategy)
@settings(max_examples=50)
def test_jtl::emof::package_instantiation(instance):
    assert isinstance(instance, JTL::emof::Package)

@given(instance=JTL::emof::Package_strategy)
def test_jtl::emof::package_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=JTL::emof::Package_strategy)
def test_jtl::emof::package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=JTL::imperativeocl::ComputeExp_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::computeexp_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ComputeExp)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=JTL::essentialocl::InvalidType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::invalidtype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::InvalidType)

@given(instance=JTL::imperativeocl::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::templateparametertype_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::TemplateParameterType)

@given(instance=JTL::imperativeocl::TemplateParameterType_strategy)
def test_jtl::imperativeocl::templateparametertype_specification_type(instance):
    assert isinstance(instance.specification, str)


@given(instance=JTL::imperativeocl::TemplateParameterType_strategy)
def test_jtl::imperativeocl::templateparametertype_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=JTL::essentialocl::VoidType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::voidtype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::VoidType)

@given(instance=JTL::emof::Class_strategy)
@settings(max_examples=50)
def test_jtl::emof::class_instantiation(instance):
    assert isinstance(instance, JTL::emof::Class)

@given(instance=JTL::emof::Class_strategy)
def test_jtl::emof::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=JTL::emof::Class_strategy)
def test_jtl::emof::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=JTL::essentialocl::CollectionType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::collectiontype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CollectionType)

@given(instance=JTL::emof::Enumeration_strategy)
@settings(max_examples=50)
def test_jtl::emof::enumeration_instantiation(instance):
    assert isinstance(instance, JTL::emof::Enumeration)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=JTL::imperativeocl::AnonymousTupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::anonymoustupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AnonymousTupleLiteralPart)

@given(instance=JTL::emof::NamedElement_strategy)
@settings(max_examples=50)
def test_jtl::emof::namedelement_instantiation(instance):
    assert isinstance(instance, JTL::emof::NamedElement)

@given(instance=JTL::emof::NamedElement_strategy)
def test_jtl::emof::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JTL::emof::NamedElement_strategy)
def test_jtl::emof::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JTL::template::PropertyTemplateItem_strategy)
@settings(max_examples=50)
def test_jtl::template::propertytemplateitem_instantiation(instance):
    assert isinstance(instance, JTL::template::PropertyTemplateItem)

@given(instance=JTL::imperativeocl::DictLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::dictliteralpart_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::DictLiteralPart)

@given(instance=JTL::emof::Tag_strategy)
@settings(max_examples=50)
def test_jtl::emof::tag_instantiation(instance):
    assert isinstance(instance, JTL::emof::Tag)

@given(instance=JTL::emof::Tag_strategy)
def test_jtl::emof::tag_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=JTL::emof::Tag_strategy)
def test_jtl::emof::tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=JTL::emof::Tag_strategy)
def test_jtl::emof::tag_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=JTL::emof::Tag_strategy)
def test_jtl::emof::tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=JTL::emof::Element_strategy)
@settings(max_examples=50)
def test_jtl::emof::element_instantiation(instance):
    assert isinstance(instance, JTL::emof::Element)

@given(instance=JTL::emof::DataType_strategy)
@settings(max_examples=50)
def test_jtl::emof::datatype_instantiation(instance):
    assert isinstance(instance, JTL::emof::DataType)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=JTL::imperativeocl::Typedef_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::typedef_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::Typedef)

@given(instance=JTL::imperativeocl::AnonymousTupleType_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::anonymoustupletype_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::AnonymousTupleType)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=JTL::essentialocl::LiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::literalexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::LiteralExp)

@given(instance=JTL::essentialocl::TypeExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::typeexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::TypeExp)

@given(instance=JTL::essentialocl::VariableExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::variableexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::VariableExp)

@given(instance=JTL::imperativeocl::ImperativeExpression_strategy)
@settings(max_examples=50)
def test_jtl::imperativeocl::imperativeexpression_instantiation(instance):
    assert isinstance(instance, JTL::imperativeocl::ImperativeExpression)

@given(instance=JTL::essentialocl::LetExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::letexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::LetExp)

@given(instance=JTL::JTL::Predicate_strategy)
@settings(max_examples=50)
def test_jtl::jtl::predicate_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Predicate)

@given(instance=TemplateExp_strategy)
@settings(max_examples=50)
def test_templateexp_instantiation(instance):
    assert isinstance(instance, TemplateExp)

@given(instance=JTL::template::ObjectTemplateExp_strategy)
@settings(max_examples=50)
def test_jtl::template::objecttemplateexp_instantiation(instance):
    assert isinstance(instance, JTL::template::ObjectTemplateExp)

@given(instance=JTL::template::ObjectTemplateExp_strategy)
def test_jtl::template::objecttemplateexp_referredClass_type(instance):
    assert isinstance(instance.referredClass, str)


@given(instance=JTL::template::ObjectTemplateExp_strategy)
def test_jtl::template::objecttemplateexp_referredClass_setter(instance):
    original = instance.referredClass
    instance.referredClass = original
    assert instance.referredClass == original

@given(instance=JTL::template::CollectionTemplateExp_strategy)
@settings(max_examples=50)
def test_jtl::template::collectiontemplateexp_instantiation(instance):
    assert isinstance(instance, JTL::template::CollectionTemplateExp)

@given(instance=JTL::template::CollectionTemplateExp_strategy)
def test_jtl::template::collectiontemplateexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=JTL::template::CollectionTemplateExp_strategy)
def test_jtl::template::collectiontemplateexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=Predicate_strategy)
@settings(max_examples=50)
def test_predicate_instantiation(instance):
    assert isinstance(instance, Predicate)

@given(instance=JTL::JTL::Pattern_strategy)
@settings(max_examples=50)
def test_jtl::jtl::pattern_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Pattern)

@given(instance=JTL::essentialocl::IfExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::ifexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::IfExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=JTL::essentialocl::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::integerliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::IntegerLiteralExp)

@given(instance=JTL::essentialocl::IntegerLiteralExp_strategy)
def test_jtl::essentialocl::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, int)


@given(instance=JTL::essentialocl::IntegerLiteralExp_strategy)
def test_jtl::essentialocl::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=JTL::essentialocl::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::realliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::RealLiteralExp)

@given(instance=JTL::essentialocl::RealLiteralExp_strategy)
def test_jtl::essentialocl::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, float)


@given(instance=JTL::essentialocl::RealLiteralExp_strategy)
def test_jtl::essentialocl::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=JTL::essentialocl::UnlimitedNaturalExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::unlimitednaturalexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::UnlimitedNaturalExp)

@given(instance=JTL::essentialocl::UnlimitedNaturalExp_strategy)
def test_jtl::essentialocl::unlimitednaturalexp_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=JTL::essentialocl::UnlimitedNaturalExp_strategy)
def test_jtl::essentialocl::unlimitednaturalexp_symbol_setter(instance):
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

@given(instance=JTL::essentialocl::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CollectionLiteralPart)

@given(instance=JTL::essentialocl::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::TupleLiteralPart)

@given(instance=JTL::essentialocl::Variable_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::variable_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::Variable)

@given(instance=JTL::essentialocl::OclExpression_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::oclexpression_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::OclExpression)

@given(instance=JTL::essentialocl::CallExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::callexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::CallExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=JTL::essentialocl::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::stringliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::StringLiteralExp)

@given(instance=JTL::essentialocl::StringLiteralExp_strategy)
def test_jtl::essentialocl::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=JTL::essentialocl::StringLiteralExp_strategy)
def test_jtl::essentialocl::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=JTL::essentialocl::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::numericliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::NumericLiteralExp)

@given(instance=JTL::essentialocl::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::BooleanLiteralExp)

@given(instance=JTL::essentialocl::BooleanLiteralExp_strategy)
def test_jtl::essentialocl::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, bool)


@given(instance=JTL::essentialocl::BooleanLiteralExp_strategy)
def test_jtl::essentialocl::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

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

@given(instance=JTL::essentialocl::TupleType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::tupletype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::TupleType)

@given(instance=JTL::essentialocl::AnyType_strategy)
@settings(max_examples=50)
def test_jtl::essentialocl::anytype_instantiation(instance):
    assert isinstance(instance, JTL::essentialocl::AnyType)

@given(instance=JTL::JTL::Transformation_strategy)
@settings(max_examples=50)
def test_jtl::jtl::transformation_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Transformation)

@given(instance=JTL::emof::Comment_strategy)
@settings(max_examples=50)
def test_jtl::emof::comment_instantiation(instance):
    assert isinstance(instance, JTL::emof::Comment)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=JTL::emof::URIExtent_strategy)
@settings(max_examples=50)
def test_jtl::emof::uriextent_instantiation(instance):
    assert isinstance(instance, JTL::emof::URIExtent)

@given(instance=JTL::emof::PrimitiveType_strategy)
@settings(max_examples=50)
def test_jtl::emof::primitivetype_instantiation(instance):
    assert isinstance(instance, JTL::emof::PrimitiveType)

@given(instance=JTL::emof::TypedElement_strategy)
@settings(max_examples=50)
def test_jtl::emof::typedelement_instantiation(instance):
    assert isinstance(instance, JTL::emof::TypedElement)

@given(instance=JTL::emof::TypedElement_strategy)
def test_jtl::emof::typedelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=JTL::emof::TypedElement_strategy)
def test_jtl::emof::typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=JTL::JTL::Model_strategy)
@settings(max_examples=50)
def test_jtl::jtl::model_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Model)

@given(instance=JTL::JTL::Model_strategy)
def test_jtl::jtl::model_usedPackage_type(instance):
    assert isinstance(instance.usedPackage, str)


@given(instance=JTL::JTL::Model_strategy)
def test_jtl::jtl::model_usedPackage_setter(instance):
    original = instance.usedPackage
    instance.usedPackage = original
    assert instance.usedPackage == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=JTL::JTL::Where_strategy)
@settings(max_examples=50)
def test_jtl::jtl::where_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Where)

@given(instance=JTL::JTL::When_strategy)
@settings(max_examples=50)
def test_jtl::jtl::when_instantiation(instance):
    assert isinstance(instance, JTL::JTL::When)

@given(instance=JTL::JTL::Domain_strategy)
@settings(max_examples=50)
def test_jtl::jtl::domain_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Domain)

@given(instance=JTL::JTL::Domain_strategy)
def test_jtl::jtl::domain_isCheckable_type(instance):
    assert isinstance(instance.isCheckable, bool)


@given(instance=JTL::JTL::Domain_strategy)
def test_jtl::jtl::domain_isCheckable_setter(instance):
    original = instance.isCheckable
    instance.isCheckable = original
    assert instance.isCheckable == original

@given(instance=JTL::JTL::Domain_strategy)
def test_jtl::jtl::domain_isEnforceable_type(instance):
    assert isinstance(instance.isEnforceable, bool)


@given(instance=JTL::JTL::Domain_strategy)
def test_jtl::jtl::domain_isEnforceable_setter(instance):
    original = instance.isEnforceable
    instance.isEnforceable = original
    assert instance.isEnforceable == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=When_strategy)
@settings(max_examples=50)
def test_when_instantiation(instance):
    assert isinstance(instance, When)

@given(instance=Where_strategy)
@settings(max_examples=50)
def test_where_instantiation(instance):
    assert isinstance(instance, Where)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Transformation_strategy)
@settings(max_examples=50)
def test_transformation_instantiation(instance):
    assert isinstance(instance, Transformation)

@given(instance=JTL::JTL::Relation_strategy)
@settings(max_examples=50)
def test_jtl::jtl::relation_instantiation(instance):
    assert isinstance(instance, JTL::JTL::Relation)

@given(instance=JTL::JTL::Relation_strategy)
def test_jtl::jtl::relation_isTopLevel_type(instance):
    assert isinstance(instance.isTopLevel, bool)


@given(instance=JTL::JTL::Relation_strategy)
def test_jtl::jtl::relation_isTopLevel_setter(instance):
    original = instance.isTopLevel
    instance.isTopLevel = original
    assert instance.isTopLevel == original

@given(instance=JTL::emof::MultiplicityElement_strategy)
@settings(max_examples=50)
def test_jtl::emof::multiplicityelement_instantiation(instance):
    assert isinstance(instance, JTL::emof::MultiplicityElement)

@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_isOrdered_type(instance):
    assert isinstance(instance.isOrdered, str)


@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_isUnique_type(instance):
    assert isinstance(instance.isUnique, str)


@given(instance=JTL::emof::MultiplicityElement_strategy)
def test_jtl::emof::multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

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

@given(instance=JTL::emof::Property_strategy)
@settings(max_examples=50)
def test_jtl::emof::property_instantiation(instance):
    assert isinstance(instance, JTL::emof::Property)

@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isId_type(instance):
    assert isinstance(instance.isId, bool)


@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isComposite_type(instance):
    assert isinstance(instance.isComposite, bool)


@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isDerived_type(instance):
    assert isinstance(instance.isDerived, bool)


@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_default_type(instance):
    assert isinstance(instance.default, str)


@given(instance=JTL::emof::Property_strategy)
def test_jtl::emof::property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=JTL::emof::Parameter_strategy)
@settings(max_examples=50)
def test_jtl::emof::parameter_instantiation(instance):
    assert isinstance(instance, JTL::emof::Parameter)

@given(instance=JTL::emof::Operation_strategy)
@settings(max_examples=50)
def test_jtl::emof::operation_instantiation(instance):
    assert isinstance(instance, JTL::emof::Operation)

@given(instance=JTL::emof::Object_strategy)
@settings(max_examples=50)
def test_jtl::emof::object_instantiation(instance):
    assert isinstance(instance, JTL::emof::Object)

@given(instance=JTL::emof::Extent_strategy)
@settings(max_examples=50)
def test_jtl::emof::extent_instantiation(instance):
    assert isinstance(instance, JTL::emof::Extent)
