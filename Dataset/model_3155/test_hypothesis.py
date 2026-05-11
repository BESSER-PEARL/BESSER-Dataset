import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sadl::ValueRow,
    sadl::ValueTable,
    sadl::IntervalValue,
    sadl::GraphPattern,
    sadl::OrderElement,
    sadl::OrderList,
    Expression,
    sadl::BinaryOpExpression,
    sadl::AskQueryExpression,
    sadl::JunctionExpression,
    sadl::UnaryOpExpression,
    sadl::ConstructExpression,
    sadl::SelectExpression,
    sadl::Expression,
    sadl::ElementSet,
    sadl::Object,
    sadl::VariableList,
    GraphPattern,
    sadl::InstAttrPSV,
    sadl::SubjProp,
    sadl::PropOfSubj,
    sadl::ExistentialNegation,
    sadl::SubTypeOf,
    sadl::InstAttrSPV,
    sadl::MergedTriples,
    sadl::EmbeddedInstanceDeclaration,
    sadl::WithPhrase,
    sadl::WithChain,
    sadl::OfPhrase,
    sadl::TypeDeclaration,
    EmbeddedInstanceDeclaration,
    InstanceDeclarationStatement,
    sadl::InstanceDeclaration,
    sadl::OfPatternReturningValues,
    sadl::PropValPartialTriple,
    sadl::IsInverseOf,
    sadl::AdditionalPropertyInfo,
    sadl::TypedBNode,
    sadl::ExplicitValue,
    sadl::EObject,
    Condition,
    sadl::CardCondition,
    sadl::MaxCardCondition,
    sadl::MinCardCondition,
    sadl::HasValueCondition,
    sadl::SomeValuesCondition,
    sadl::AllValuesCondition,
    sadl::PropertyOfClass,
    sadl::Facets,
    sadl::DataTypeRestriction,
    Statement,
    sadl::TransitiveProperty,
    sadl::NecessaryAndSufficient,
    sadl::SomeValuesFrom,
    sadl::InstanceDeclarationStatement,
    sadl::EnumeratedAllValuesFrom,
    sadl::InstancesAllDifferent,
    sadl::HasValue,
    sadl::DefaultValue,
    sadl::InstanceDifferentFrom,
    sadl::DisjointClasses,
    sadl::EquivalentConcepts,
    sadl::InverseProperty,
    sadl::PropertyDeclaration,
    sadl::ExistingInstanceAttribution,
    sadl::SymmetricalProperty,
    sadl::InverseFunctionalProperty,
    sadl::ComplementOfClass,
    sadl::AllValuesFrom,
    sadl::EnumeratedAllAndSomeValuesFrom,
    sadl::Cardinality,
    sadl::MaxCardinality,
    sadl::MinCardinality,
    sadl::FunctionalProperty,
    sadl::ClassDeclaration,
    sadl::UserDefinedDataType,
    ResourceBySetOp,
    sadl::IntersectionResource,
    sadl::UnionResource,
    sadl::RangeType,
    sadl::Range,
    sadl::AddlClassInfo,
    sadl::EnumeratedInstances,
    ModelElement,
    sadl::Explanation,
    sadl::Rule,
    sadl::Test,
    sadl::Display,
    sadl::Expr,
    sadl::Query,
    sadl::Statement,
    sadl::Condition,
    sadl::ResourceIdentifier,
    sadl::ExistingResourceList,
    ResourceIdentifier,
    sadl::ResourceBySetOp,
    sadl::ResourceByRestriction,
    sadl::ResourceByName,
    sadl::LiteralValue,
    sadl::LiteralList,
    sadl::ResourceList,
    sadl::ResourceName,
    sadl::ContentList,
    sadl::ModelElement,
    sadl::Import,
    sadl::ModelName,
    sadl::Model,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sadl::valuerow_is_not_abstract():
    assert not inspect.isabstract(sadl::ValueRow)


def test_sadl::valuerow_constructor_exists():
    assert callable(sadl::ValueRow.__init__)


def test_sadl::valuerow_constructor_args():
    sig = inspect.signature(sadl::ValueRow.__init__)
    params = list(sig.parameters.keys())



def test_sadl::valuetable_is_not_abstract():
    assert not inspect.isabstract(sadl::ValueTable)


def test_sadl::valuetable_constructor_exists():
    assert callable(sadl::ValueTable.__init__)


def test_sadl::valuetable_constructor_args():
    sig = inspect.signature(sadl::ValueTable.__init__)
    params = list(sig.parameters.keys())



def test_sadl::intervalvalue_is_not_abstract():
    assert not inspect.isabstract(sadl::IntervalValue)


def test_sadl::intervalvalue_constructor_exists():
    assert callable(sadl::IntervalValue.__init__)


def test_sadl::intervalvalue_constructor_args():
    sig = inspect.signature(sadl::IntervalValue.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::intervalvalue_has_op():
    assert hasattr(sadl::IntervalValue, "op")
    descriptor = None
    for klass in sadl::IntervalValue.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::graphpattern_is_not_abstract():
    assert not inspect.isabstract(sadl::GraphPattern)


def test_sadl::graphpattern_constructor_exists():
    assert callable(sadl::GraphPattern.__init__)


def test_sadl::graphpattern_constructor_args():
    sig = inspect.signature(sadl::GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sadl::orderelement_is_not_abstract():
    assert not inspect.isabstract(sadl::OrderElement)


def test_sadl::orderelement_constructor_exists():
    assert callable(sadl::OrderElement.__init__)


def test_sadl::orderelement_constructor_args():
    sig = inspect.signature(sadl::OrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_sadl::orderelement_has_order():
    assert hasattr(sadl::OrderElement, "order")
    descriptor = None
    for klass in sadl::OrderElement.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_sadl::orderlist_is_not_abstract():
    assert not inspect.isabstract(sadl::OrderList)


def test_sadl::orderlist_constructor_exists():
    assert callable(sadl::OrderList.__init__)


def test_sadl::orderlist_constructor_args():
    sig = inspect.signature(sadl::OrderList.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sadl::binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::BinaryOpExpression)


def test_sadl::binaryopexpression_constructor_exists():
    assert callable(sadl::BinaryOpExpression.__init__)


def test_sadl::binaryopexpression_constructor_args():
    sig = inspect.signature(sadl::BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::binaryopexpression_has_op():
    assert hasattr(sadl::BinaryOpExpression, "op")
    descriptor = None
    for klass in sadl::BinaryOpExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::askqueryexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::AskQueryExpression)


def test_sadl::askqueryexpression_constructor_exists():
    assert callable(sadl::AskQueryExpression.__init__)


def test_sadl::askqueryexpression_constructor_args():
    sig = inspect.signature(sadl::AskQueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl::junctionexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::JunctionExpression)


def test_sadl::junctionexpression_constructor_exists():
    assert callable(sadl::JunctionExpression.__init__)


def test_sadl::junctionexpression_constructor_args():
    sig = inspect.signature(sadl::JunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::junctionexpression_has_op():
    assert hasattr(sadl::JunctionExpression, "op")
    descriptor = None
    for klass in sadl::JunctionExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::unaryopexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::UnaryOpExpression)


def test_sadl::unaryopexpression_constructor_exists():
    assert callable(sadl::UnaryOpExpression.__init__)


def test_sadl::unaryopexpression_constructor_args():
    sig = inspect.signature(sadl::UnaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl::unaryopexpression_has_op():
    assert hasattr(sadl::UnaryOpExpression, "op")
    descriptor = None
    for klass in sadl::UnaryOpExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl::constructexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::ConstructExpression)


def test_sadl::constructexpression_constructor_exists():
    assert callable(sadl::ConstructExpression.__init__)


def test_sadl::constructexpression_constructor_args():
    sig = inspect.signature(sadl::ConstructExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl::selectexpression_is_not_abstract():
    assert not inspect.isabstract(sadl::SelectExpression)


def test_sadl::selectexpression_constructor_exists():
    assert callable(sadl::SelectExpression.__init__)


def test_sadl::selectexpression_constructor_args():
    sig = inspect.signature(sadl::SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "allVars" in params, "Missing parameter 'allVars'"
    assert "orderby" in params, "Missing parameter 'orderby'"

def test_sadl::selectexpression_has_distinct():
    assert hasattr(sadl::SelectExpression, "distinct")
    descriptor = None
    for klass in sadl::SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_sadl::selectexpression_has_allVars():
    assert hasattr(sadl::SelectExpression, "allVars")
    descriptor = None
    for klass in sadl::SelectExpression.__mro__:
        if "allVars" in klass.__dict__:
            descriptor = klass.__dict__["allVars"]
            break
    assert isinstance(descriptor, property)

def test_sadl::selectexpression_has_orderby():
    assert hasattr(sadl::SelectExpression, "orderby")
    descriptor = None
    for klass in sadl::SelectExpression.__mro__:
        if "orderby" in klass.__dict__:
            descriptor = klass.__dict__["orderby"]
            break
    assert isinstance(descriptor, property)



def test_sadl::expression_is_not_abstract():
    assert not inspect.isabstract(sadl::Expression)


def test_sadl::expression_constructor_exists():
    assert callable(sadl::Expression.__init__)


def test_sadl::expression_constructor_args():
    sig = inspect.signature(sadl::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_sadl::expression_has_func():
    assert hasattr(sadl::Expression, "func")
    descriptor = None
    for klass in sadl::Expression.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_sadl::elementset_is_not_abstract():
    assert not inspect.isabstract(sadl::ElementSet)


def test_sadl::elementset_constructor_exists():
    assert callable(sadl::ElementSet.__init__)


def test_sadl::elementset_constructor_args():
    sig = inspect.signature(sadl::ElementSet.__init__)
    params = list(sig.parameters.keys())



def test_sadl::object_is_not_abstract():
    assert not inspect.isabstract(sadl::Object)


def test_sadl::object_constructor_exists():
    assert callable(sadl::Object.__init__)


def test_sadl::object_constructor_args():
    sig = inspect.signature(sadl::Object.__init__)
    params = list(sig.parameters.keys())



def test_sadl::variablelist_is_not_abstract():
    assert not inspect.isabstract(sadl::VariableList)


def test_sadl::variablelist_constructor_exists():
    assert callable(sadl::VariableList.__init__)


def test_sadl::variablelist_constructor_args():
    sig = inspect.signature(sadl::VariableList.__init__)
    params = list(sig.parameters.keys())



def test_graphpattern_is_not_abstract():
    assert not inspect.isabstract(GraphPattern)


def test_graphpattern_constructor_exists():
    assert callable(GraphPattern.__init__)


def test_graphpattern_constructor_args():
    sig = inspect.signature(GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sadl::instattrpsv_is_not_abstract():
    assert not inspect.isabstract(sadl::InstAttrPSV)


def test_sadl::instattrpsv_constructor_exists():
    assert callable(sadl::InstAttrPSV.__init__)


def test_sadl::instattrpsv_constructor_args():
    sig = inspect.signature(sadl::InstAttrPSV.__init__)
    params = list(sig.parameters.keys())



def test_sadl::subjprop_is_not_abstract():
    assert not inspect.isabstract(sadl::SubjProp)


def test_sadl::subjprop_constructor_exists():
    assert callable(sadl::SubjProp.__init__)


def test_sadl::subjprop_constructor_args():
    sig = inspect.signature(sadl::SubjProp.__init__)
    params = list(sig.parameters.keys())



def test_sadl::propofsubj_is_not_abstract():
    assert not inspect.isabstract(sadl::PropOfSubj)


def test_sadl::propofsubj_constructor_exists():
    assert callable(sadl::PropOfSubj.__init__)


def test_sadl::propofsubj_constructor_args():
    sig = inspect.signature(sadl::PropOfSubj.__init__)
    params = list(sig.parameters.keys())



def test_sadl::existentialnegation_is_not_abstract():
    assert not inspect.isabstract(sadl::ExistentialNegation)


def test_sadl::existentialnegation_constructor_exists():
    assert callable(sadl::ExistentialNegation.__init__)


def test_sadl::existentialnegation_constructor_args():
    sig = inspect.signature(sadl::ExistentialNegation.__init__)
    params = list(sig.parameters.keys())



def test_sadl::subtypeof_is_not_abstract():
    assert not inspect.isabstract(sadl::SubTypeOf)


def test_sadl::subtypeof_constructor_exists():
    assert callable(sadl::SubTypeOf.__init__)


def test_sadl::subtypeof_constructor_args():
    sig = inspect.signature(sadl::SubTypeOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl::instattrspv_is_not_abstract():
    assert not inspect.isabstract(sadl::InstAttrSPV)


def test_sadl::instattrspv_constructor_exists():
    assert callable(sadl::InstAttrSPV.__init__)


def test_sadl::instattrspv_constructor_args():
    sig = inspect.signature(sadl::InstAttrSPV.__init__)
    params = list(sig.parameters.keys())



def test_sadl::mergedtriples_is_not_abstract():
    assert not inspect.isabstract(sadl::MergedTriples)


def test_sadl::mergedtriples_constructor_exists():
    assert callable(sadl::MergedTriples.__init__)


def test_sadl::mergedtriples_constructor_args():
    sig = inspect.signature(sadl::MergedTriples.__init__)
    params = list(sig.parameters.keys())



def test_sadl::embeddedinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl::EmbeddedInstanceDeclaration)


def test_sadl::embeddedinstancedeclaration_constructor_exists():
    assert callable(sadl::EmbeddedInstanceDeclaration.__init__)


def test_sadl::embeddedinstancedeclaration_constructor_args():
    sig = inspect.signature(sadl::EmbeddedInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl::withphrase_is_not_abstract():
    assert not inspect.isabstract(sadl::WithPhrase)


def test_sadl::withphrase_constructor_exists():
    assert callable(sadl::WithPhrase.__init__)


def test_sadl::withphrase_constructor_args():
    sig = inspect.signature(sadl::WithPhrase.__init__)
    params = list(sig.parameters.keys())



def test_sadl::withchain_is_not_abstract():
    assert not inspect.isabstract(sadl::WithChain)


def test_sadl::withchain_constructor_exists():
    assert callable(sadl::WithChain.__init__)


def test_sadl::withchain_constructor_args():
    sig = inspect.signature(sadl::WithChain.__init__)
    params = list(sig.parameters.keys())



def test_sadl::ofphrase_is_not_abstract():
    assert not inspect.isabstract(sadl::OfPhrase)


def test_sadl::ofphrase_constructor_exists():
    assert callable(sadl::OfPhrase.__init__)


def test_sadl::ofphrase_constructor_args():
    sig = inspect.signature(sadl::OfPhrase.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::ofphrase_has_article():
    assert hasattr(sadl::OfPhrase, "article")
    descriptor = None
    for klass in sadl::OfPhrase.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl::TypeDeclaration)


def test_sadl::typedeclaration_constructor_exists():
    assert callable(sadl::TypeDeclaration.__init__)


def test_sadl::typedeclaration_constructor_args():
    sig = inspect.signature(sadl::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_embeddedinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(EmbeddedInstanceDeclaration)


def test_embeddedinstancedeclaration_constructor_exists():
    assert callable(EmbeddedInstanceDeclaration.__init__)


def test_embeddedinstancedeclaration_constructor_args():
    sig = inspect.signature(EmbeddedInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_instancedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(InstanceDeclarationStatement)


def test_instancedeclarationstatement_constructor_exists():
    assert callable(InstanceDeclarationStatement.__init__)


def test_instancedeclarationstatement_constructor_args():
    sig = inspect.signature(InstanceDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::instancedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl::InstanceDeclaration)


def test_sadl::instancedeclaration_constructor_exists():
    assert callable(sadl::InstanceDeclaration.__init__)


def test_sadl::instancedeclaration_constructor_args():
    sig = inspect.signature(sadl::InstanceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::instancedeclaration_has_article():
    assert hasattr(sadl::InstanceDeclaration, "article")
    descriptor = None
    for klass in sadl::InstanceDeclaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::ofpatternreturningvalues_is_not_abstract():
    assert not inspect.isabstract(sadl::OfPatternReturningValues)


def test_sadl::ofpatternreturningvalues_constructor_exists():
    assert callable(sadl::OfPatternReturningValues.__init__)


def test_sadl::ofpatternreturningvalues_constructor_args():
    sig = inspect.signature(sadl::OfPatternReturningValues.__init__)
    params = list(sig.parameters.keys())



def test_sadl::propvalpartialtriple_is_not_abstract():
    assert not inspect.isabstract(sadl::PropValPartialTriple)


def test_sadl::propvalpartialtriple_constructor_exists():
    assert callable(sadl::PropValPartialTriple.__init__)


def test_sadl::propvalpartialtriple_constructor_args():
    sig = inspect.signature(sadl::PropValPartialTriple.__init__)
    params = list(sig.parameters.keys())



def test_sadl::isinverseof_is_not_abstract():
    assert not inspect.isabstract(sadl::IsInverseOf)


def test_sadl::isinverseof_constructor_exists():
    assert callable(sadl::IsInverseOf.__init__)


def test_sadl::isinverseof_constructor_args():
    sig = inspect.signature(sadl::IsInverseOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl::additionalpropertyinfo_is_not_abstract():
    assert not inspect.isabstract(sadl::AdditionalPropertyInfo)


def test_sadl::additionalpropertyinfo_constructor_exists():
    assert callable(sadl::AdditionalPropertyInfo.__init__)


def test_sadl::additionalpropertyinfo_constructor_args():
    sig = inspect.signature(sadl::AdditionalPropertyInfo.__init__)
    params = list(sig.parameters.keys())
    assert "isTrans" in params, "Missing parameter 'isTrans'"
    assert "isfunc" in params, "Missing parameter 'isfunc'"
    assert "isinvfunc" in params, "Missing parameter 'isinvfunc'"
    assert "isSym" in params, "Missing parameter 'isSym'"

def test_sadl::additionalpropertyinfo_has_isTrans():
    assert hasattr(sadl::AdditionalPropertyInfo, "isTrans")
    descriptor = None
    for klass in sadl::AdditionalPropertyInfo.__mro__:
        if "isTrans" in klass.__dict__:
            descriptor = klass.__dict__["isTrans"]
            break
    assert isinstance(descriptor, property)

def test_sadl::additionalpropertyinfo_has_isfunc():
    assert hasattr(sadl::AdditionalPropertyInfo, "isfunc")
    descriptor = None
    for klass in sadl::AdditionalPropertyInfo.__mro__:
        if "isfunc" in klass.__dict__:
            descriptor = klass.__dict__["isfunc"]
            break
    assert isinstance(descriptor, property)

def test_sadl::additionalpropertyinfo_has_isinvfunc():
    assert hasattr(sadl::AdditionalPropertyInfo, "isinvfunc")
    descriptor = None
    for klass in sadl::AdditionalPropertyInfo.__mro__:
        if "isinvfunc" in klass.__dict__:
            descriptor = klass.__dict__["isinvfunc"]
            break
    assert isinstance(descriptor, property)

def test_sadl::additionalpropertyinfo_has_isSym():
    assert hasattr(sadl::AdditionalPropertyInfo, "isSym")
    descriptor = None
    for klass in sadl::AdditionalPropertyInfo.__mro__:
        if "isSym" in klass.__dict__:
            descriptor = klass.__dict__["isSym"]
            break
    assert isinstance(descriptor, property)



def test_sadl::typedbnode_is_not_abstract():
    assert not inspect.isabstract(sadl::TypedBNode)


def test_sadl::typedbnode_constructor_exists():
    assert callable(sadl::TypedBNode.__init__)


def test_sadl::typedbnode_constructor_args():
    sig = inspect.signature(sadl::TypedBNode.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::typedbnode_has_article():
    assert hasattr(sadl::TypedBNode, "article")
    descriptor = None
    for klass in sadl::TypedBNode.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::explicitvalue_is_not_abstract():
    assert not inspect.isabstract(sadl::ExplicitValue)


def test_sadl::explicitvalue_constructor_exists():
    assert callable(sadl::ExplicitValue.__init__)


def test_sadl::explicitvalue_constructor_args():
    sig = inspect.signature(sadl::ExplicitValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueList" in params, "Missing parameter 'valueList'"
    assert "term" in params, "Missing parameter 'term'"

def test_sadl::explicitvalue_has_valueList():
    assert hasattr(sadl::ExplicitValue, "valueList")
    descriptor = None
    for klass in sadl::ExplicitValue.__mro__:
        if "valueList" in klass.__dict__:
            descriptor = klass.__dict__["valueList"]
            break
    assert isinstance(descriptor, property)

def test_sadl::explicitvalue_has_term():
    assert hasattr(sadl::ExplicitValue, "term")
    descriptor = None
    for klass in sadl::ExplicitValue.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)



def test_sadl::eobject_is_not_abstract():
    assert not inspect.isabstract(sadl::EObject)


def test_sadl::eobject_constructor_exists():
    assert callable(sadl::EObject.__init__)


def test_sadl::eobject_constructor_args():
    sig = inspect.signature(sadl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::cardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl::CardCondition)


def test_sadl::cardcondition_constructor_exists():
    assert callable(sadl::CardCondition.__init__)


def test_sadl::cardcondition_constructor_args():
    sig = inspect.signature(sadl::CardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl::cardcondition_has_card():
    assert hasattr(sadl::CardCondition, "card")
    descriptor = None
    for klass in sadl::CardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl::maxcardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl::MaxCardCondition)


def test_sadl::maxcardcondition_constructor_exists():
    assert callable(sadl::MaxCardCondition.__init__)


def test_sadl::maxcardcondition_constructor_args():
    sig = inspect.signature(sadl::MaxCardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl::maxcardcondition_has_card():
    assert hasattr(sadl::MaxCardCondition, "card")
    descriptor = None
    for klass in sadl::MaxCardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl::mincardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl::MinCardCondition)


def test_sadl::mincardcondition_constructor_exists():
    assert callable(sadl::MinCardCondition.__init__)


def test_sadl::mincardcondition_constructor_args():
    sig = inspect.signature(sadl::MinCardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl::mincardcondition_has_card():
    assert hasattr(sadl::MinCardCondition, "card")
    descriptor = None
    for klass in sadl::MinCardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl::hasvaluecondition_is_not_abstract():
    assert not inspect.isabstract(sadl::HasValueCondition)


def test_sadl::hasvaluecondition_constructor_exists():
    assert callable(sadl::HasValueCondition.__init__)


def test_sadl::hasvaluecondition_constructor_args():
    sig = inspect.signature(sadl::HasValueCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::somevaluescondition_is_not_abstract():
    assert not inspect.isabstract(sadl::SomeValuesCondition)


def test_sadl::somevaluescondition_constructor_exists():
    assert callable(sadl::SomeValuesCondition.__init__)


def test_sadl::somevaluescondition_constructor_args():
    sig = inspect.signature(sadl::SomeValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::allvaluescondition_is_not_abstract():
    assert not inspect.isabstract(sadl::AllValuesCondition)


def test_sadl::allvaluescondition_constructor_exists():
    assert callable(sadl::AllValuesCondition.__init__)


def test_sadl::allvaluescondition_constructor_args():
    sig = inspect.signature(sadl::AllValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::propertyofclass_is_not_abstract():
    assert not inspect.isabstract(sadl::PropertyOfClass)


def test_sadl::propertyofclass_constructor_exists():
    assert callable(sadl::PropertyOfClass.__init__)


def test_sadl::propertyofclass_constructor_args():
    sig = inspect.signature(sadl::PropertyOfClass.__init__)
    params = list(sig.parameters.keys())



def test_sadl::facets_is_not_abstract():
    assert not inspect.isabstract(sadl::Facets)


def test_sadl::facets_constructor_exists():
    assert callable(sadl::Facets.__init__)


def test_sadl::facets_constructor_args():
    sig = inspect.signature(sadl::Facets.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"
    assert "min" in params, "Missing parameter 'min'"
    assert "minlen" in params, "Missing parameter 'minlen'"
    assert "max" in params, "Missing parameter 'max'"
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "values" in params, "Missing parameter 'values'"
    assert "maxexin" in params, "Missing parameter 'maxexin'"
    assert "minexin" in params, "Missing parameter 'minexin'"
    assert "len" in params, "Missing parameter 'len'"

def test_sadl::facets_has_regex():
    assert hasattr(sadl::Facets, "regex")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_min():
    assert hasattr(sadl::Facets, "min")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_minlen():
    assert hasattr(sadl::Facets, "minlen")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "minlen" in klass.__dict__:
            descriptor = klass.__dict__["minlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_max():
    assert hasattr(sadl::Facets, "max")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_maxlen():
    assert hasattr(sadl::Facets, "maxlen")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_values():
    assert hasattr(sadl::Facets, "values")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_maxexin():
    assert hasattr(sadl::Facets, "maxexin")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "maxexin" in klass.__dict__:
            descriptor = klass.__dict__["maxexin"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_minexin():
    assert hasattr(sadl::Facets, "minexin")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "minexin" in klass.__dict__:
            descriptor = klass.__dict__["minexin"]
            break
    assert isinstance(descriptor, property)

def test_sadl::facets_has_len():
    assert hasattr(sadl::Facets, "len")
    descriptor = None
    for klass in sadl::Facets.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)



def test_sadl::datatyperestriction_is_not_abstract():
    assert not inspect.isabstract(sadl::DataTypeRestriction)


def test_sadl::datatyperestriction_constructor_exists():
    assert callable(sadl::DataTypeRestriction.__init__)


def test_sadl::datatyperestriction_constructor_args():
    sig = inspect.signature(sadl::DataTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "basetype" in params, "Missing parameter 'basetype'"
    assert "basetypes" in params, "Missing parameter 'basetypes'"

def test_sadl::datatyperestriction_has_basetype():
    assert hasattr(sadl::DataTypeRestriction, "basetype")
    descriptor = None
    for klass in sadl::DataTypeRestriction.__mro__:
        if "basetype" in klass.__dict__:
            descriptor = klass.__dict__["basetype"]
            break
    assert isinstance(descriptor, property)

def test_sadl::datatyperestriction_has_basetypes():
    assert hasattr(sadl::DataTypeRestriction, "basetypes")
    descriptor = None
    for klass in sadl::DataTypeRestriction.__mro__:
        if "basetypes" in klass.__dict__:
            descriptor = klass.__dict__["basetypes"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::transitiveproperty_is_not_abstract():
    assert not inspect.isabstract(sadl::TransitiveProperty)


def test_sadl::transitiveproperty_constructor_exists():
    assert callable(sadl::TransitiveProperty.__init__)


def test_sadl::transitiveproperty_constructor_args():
    sig = inspect.signature(sadl::TransitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl::necessaryandsufficient_is_not_abstract():
    assert not inspect.isabstract(sadl::NecessaryAndSufficient)


def test_sadl::necessaryandsufficient_constructor_exists():
    assert callable(sadl::NecessaryAndSufficient.__init__)


def test_sadl::necessaryandsufficient_constructor_args():
    sig = inspect.signature(sadl::NecessaryAndSufficient.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::necessaryandsufficient_has_article():
    assert hasattr(sadl::NecessaryAndSufficient, "article")
    descriptor = None
    for klass in sadl::NecessaryAndSufficient.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::somevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl::SomeValuesFrom)


def test_sadl::somevaluesfrom_constructor_exists():
    assert callable(sadl::SomeValuesFrom.__init__)


def test_sadl::somevaluesfrom_constructor_args():
    sig = inspect.signature(sadl::SomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl::instancedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(sadl::InstanceDeclarationStatement)


def test_sadl::instancedeclarationstatement_constructor_exists():
    assert callable(sadl::InstanceDeclarationStatement.__init__)


def test_sadl::instancedeclarationstatement_constructor_args():
    sig = inspect.signature(sadl::InstanceDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::enumeratedallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl::EnumeratedAllValuesFrom)


def test_sadl::enumeratedallvaluesfrom_constructor_exists():
    assert callable(sadl::EnumeratedAllValuesFrom.__init__)


def test_sadl::enumeratedallvaluesfrom_constructor_args():
    sig = inspect.signature(sadl::EnumeratedAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl::instancesalldifferent_is_not_abstract():
    assert not inspect.isabstract(sadl::InstancesAllDifferent)


def test_sadl::instancesalldifferent_constructor_exists():
    assert callable(sadl::InstancesAllDifferent.__init__)


def test_sadl::instancesalldifferent_constructor_args():
    sig = inspect.signature(sadl::InstancesAllDifferent.__init__)
    params = list(sig.parameters.keys())



def test_sadl::hasvalue_is_not_abstract():
    assert not inspect.isabstract(sadl::HasValue)


def test_sadl::hasvalue_constructor_exists():
    assert callable(sadl::HasValue.__init__)


def test_sadl::hasvalue_constructor_args():
    sig = inspect.signature(sadl::HasValue.__init__)
    params = list(sig.parameters.keys())



def test_sadl::defaultvalue_is_not_abstract():
    assert not inspect.isabstract(sadl::DefaultValue)


def test_sadl::defaultvalue_constructor_exists():
    assert callable(sadl::DefaultValue.__init__)


def test_sadl::defaultvalue_constructor_args():
    sig = inspect.signature(sadl::DefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_sadl::defaultvalue_has_level():
    assert hasattr(sadl::DefaultValue, "level")
    descriptor = None
    for klass in sadl::DefaultValue.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_sadl::instancedifferentfrom_is_not_abstract():
    assert not inspect.isabstract(sadl::InstanceDifferentFrom)


def test_sadl::instancedifferentfrom_constructor_exists():
    assert callable(sadl::InstanceDifferentFrom.__init__)


def test_sadl::instancedifferentfrom_constructor_args():
    sig = inspect.signature(sadl::InstanceDifferentFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl::disjointclasses_is_not_abstract():
    assert not inspect.isabstract(sadl::DisjointClasses)


def test_sadl::disjointclasses_constructor_exists():
    assert callable(sadl::DisjointClasses.__init__)


def test_sadl::disjointclasses_constructor_args():
    sig = inspect.signature(sadl::DisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sadl::equivalentconcepts_is_not_abstract():
    assert not inspect.isabstract(sadl::EquivalentConcepts)


def test_sadl::equivalentconcepts_constructor_exists():
    assert callable(sadl::EquivalentConcepts.__init__)


def test_sadl::equivalentconcepts_constructor_args():
    sig = inspect.signature(sadl::EquivalentConcepts.__init__)
    params = list(sig.parameters.keys())



def test_sadl::inverseproperty_is_not_abstract():
    assert not inspect.isabstract(sadl::InverseProperty)


def test_sadl::inverseproperty_constructor_exists():
    assert callable(sadl::InverseProperty.__init__)


def test_sadl::inverseproperty_constructor_args():
    sig = inspect.signature(sadl::InverseProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl::propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl::PropertyDeclaration)


def test_sadl::propertydeclaration_constructor_exists():
    assert callable(sadl::PropertyDeclaration.__init__)


def test_sadl::propertydeclaration_constructor_args():
    sig = inspect.signature(sadl::PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl::propertydeclaration_has_article():
    assert hasattr(sadl::PropertyDeclaration, "article")
    descriptor = None
    for klass in sadl::PropertyDeclaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl::existinginstanceattribution_is_not_abstract():
    assert not inspect.isabstract(sadl::ExistingInstanceAttribution)


def test_sadl::existinginstanceattribution_constructor_exists():
    assert callable(sadl::ExistingInstanceAttribution.__init__)


def test_sadl::existinginstanceattribution_constructor_args():
    sig = inspect.signature(sadl::ExistingInstanceAttribution.__init__)
    params = list(sig.parameters.keys())



def test_sadl::symmetricalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl::SymmetricalProperty)


def test_sadl::symmetricalproperty_constructor_exists():
    assert callable(sadl::SymmetricalProperty.__init__)


def test_sadl::symmetricalproperty_constructor_args():
    sig = inspect.signature(sadl::SymmetricalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl::inversefunctionalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl::InverseFunctionalProperty)


def test_sadl::inversefunctionalproperty_constructor_exists():
    assert callable(sadl::InverseFunctionalProperty.__init__)


def test_sadl::inversefunctionalproperty_constructor_args():
    sig = inspect.signature(sadl::InverseFunctionalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl::complementofclass_is_not_abstract():
    assert not inspect.isabstract(sadl::ComplementOfClass)


def test_sadl::complementofclass_constructor_exists():
    assert callable(sadl::ComplementOfClass.__init__)


def test_sadl::complementofclass_constructor_args():
    sig = inspect.signature(sadl::ComplementOfClass.__init__)
    params = list(sig.parameters.keys())



def test_sadl::allvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl::AllValuesFrom)


def test_sadl::allvaluesfrom_constructor_exists():
    assert callable(sadl::AllValuesFrom.__init__)


def test_sadl::allvaluesfrom_constructor_args():
    sig = inspect.signature(sadl::AllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl::enumeratedallandsomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl::EnumeratedAllAndSomeValuesFrom)


def test_sadl::enumeratedallandsomevaluesfrom_constructor_exists():
    assert callable(sadl::EnumeratedAllAndSomeValuesFrom.__init__)


def test_sadl::enumeratedallandsomevaluesfrom_constructor_args():
    sig = inspect.signature(sadl::EnumeratedAllAndSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl::cardinality_is_not_abstract():
    assert not inspect.isabstract(sadl::Cardinality)


def test_sadl::cardinality_constructor_exists():
    assert callable(sadl::Cardinality.__init__)


def test_sadl::cardinality_constructor_args():
    sig = inspect.signature(sadl::Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl::maxcardinality_is_not_abstract():
    assert not inspect.isabstract(sadl::MaxCardinality)


def test_sadl::maxcardinality_constructor_exists():
    assert callable(sadl::MaxCardinality.__init__)


def test_sadl::maxcardinality_constructor_args():
    sig = inspect.signature(sadl::MaxCardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl::mincardinality_is_not_abstract():
    assert not inspect.isabstract(sadl::MinCardinality)


def test_sadl::mincardinality_constructor_exists():
    assert callable(sadl::MinCardinality.__init__)


def test_sadl::mincardinality_constructor_args():
    sig = inspect.signature(sadl::MinCardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl::functionalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl::FunctionalProperty)


def test_sadl::functionalproperty_constructor_exists():
    assert callable(sadl::FunctionalProperty.__init__)


def test_sadl::functionalproperty_constructor_args():
    sig = inspect.signature(sadl::FunctionalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl::classdeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl::ClassDeclaration)


def test_sadl::classdeclaration_constructor_exists():
    assert callable(sadl::ClassDeclaration.__init__)


def test_sadl::classdeclaration_constructor_args():
    sig = inspect.signature(sadl::ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl::userdefineddatatype_is_not_abstract():
    assert not inspect.isabstract(sadl::UserDefinedDataType)


def test_sadl::userdefineddatatype_constructor_exists():
    assert callable(sadl::UserDefinedDataType.__init__)


def test_sadl::userdefineddatatype_constructor_args():
    sig = inspect.signature(sadl::UserDefinedDataType.__init__)
    params = list(sig.parameters.keys())



def test_resourcebysetop_is_not_abstract():
    assert not inspect.isabstract(ResourceBySetOp)


def test_resourcebysetop_constructor_exists():
    assert callable(ResourceBySetOp.__init__)


def test_resourcebysetop_constructor_args():
    sig = inspect.signature(ResourceBySetOp.__init__)
    params = list(sig.parameters.keys())



def test_sadl::intersectionresource_is_not_abstract():
    assert not inspect.isabstract(sadl::IntersectionResource)


def test_sadl::intersectionresource_constructor_exists():
    assert callable(sadl::IntersectionResource.__init__)


def test_sadl::intersectionresource_constructor_args():
    sig = inspect.signature(sadl::IntersectionResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl::unionresource_is_not_abstract():
    assert not inspect.isabstract(sadl::UnionResource)


def test_sadl::unionresource_constructor_exists():
    assert callable(sadl::UnionResource.__init__)


def test_sadl::unionresource_constructor_args():
    sig = inspect.signature(sadl::UnionResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl::rangetype_is_not_abstract():
    assert not inspect.isabstract(sadl::RangeType)


def test_sadl::rangetype_constructor_exists():
    assert callable(sadl::RangeType.__init__)


def test_sadl::rangetype_constructor_args():
    sig = inspect.signature(sadl::RangeType.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sadl::rangetype_has_dataType():
    assert hasattr(sadl::RangeType, "dataType")
    descriptor = None
    for klass in sadl::RangeType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sadl::range_is_not_abstract():
    assert not inspect.isabstract(sadl::Range)


def test_sadl::range_constructor_exists():
    assert callable(sadl::Range.__init__)


def test_sadl::range_constructor_args():
    sig = inspect.signature(sadl::Range.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "list" in params, "Missing parameter 'list'"
    assert "lists" in params, "Missing parameter 'lists'"

def test_sadl::range_has_single():
    assert hasattr(sadl::Range, "single")
    descriptor = None
    for klass in sadl::Range.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_sadl::range_has_list():
    assert hasattr(sadl::Range, "list")
    descriptor = None
    for klass in sadl::Range.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)

def test_sadl::range_has_lists():
    assert hasattr(sadl::Range, "lists")
    descriptor = None
    for klass in sadl::Range.__mro__:
        if "lists" in klass.__dict__:
            descriptor = klass.__dict__["lists"]
            break
    assert isinstance(descriptor, property)



def test_sadl::addlclassinfo_is_not_abstract():
    assert not inspect.isabstract(sadl::AddlClassInfo)


def test_sadl::addlclassinfo_constructor_exists():
    assert callable(sadl::AddlClassInfo.__init__)


def test_sadl::addlclassinfo_constructor_args():
    sig = inspect.signature(sadl::AddlClassInfo.__init__)
    params = list(sig.parameters.keys())



def test_sadl::enumeratedinstances_is_not_abstract():
    assert not inspect.isabstract(sadl::EnumeratedInstances)


def test_sadl::enumeratedinstances_constructor_exists():
    assert callable(sadl::EnumeratedInstances.__init__)


def test_sadl::enumeratedinstances_constructor_args():
    sig = inspect.signature(sadl::EnumeratedInstances.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::explanation_is_not_abstract():
    assert not inspect.isabstract(sadl::Explanation)


def test_sadl::explanation_constructor_exists():
    assert callable(sadl::Explanation.__init__)


def test_sadl::explanation_constructor_args():
    sig = inspect.signature(sadl::Explanation.__init__)
    params = list(sig.parameters.keys())
    assert "rulename" in params, "Missing parameter 'rulename'"

def test_sadl::explanation_has_rulename():
    assert hasattr(sadl::Explanation, "rulename")
    descriptor = None
    for klass in sadl::Explanation.__mro__:
        if "rulename" in klass.__dict__:
            descriptor = klass.__dict__["rulename"]
            break
    assert isinstance(descriptor, property)



def test_sadl::rule_is_not_abstract():
    assert not inspect.isabstract(sadl::Rule)


def test_sadl::rule_constructor_exists():
    assert callable(sadl::Rule.__init__)


def test_sadl::rule_constructor_args():
    sig = inspect.signature(sadl::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sadl::rule_has_name():
    assert hasattr(sadl::Rule, "name")
    descriptor = None
    for klass in sadl::Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sadl::test_is_not_abstract():
    assert not inspect.isabstract(sadl::Test)


def test_sadl::test_constructor_exists():
    assert callable(sadl::Test.__init__)


def test_sadl::test_constructor_args():
    sig = inspect.signature(sadl::Test.__init__)
    params = list(sig.parameters.keys())



def test_sadl::display_is_not_abstract():
    assert not inspect.isabstract(sadl::Display)


def test_sadl::display_constructor_exists():
    assert callable(sadl::Display.__init__)


def test_sadl::display_constructor_args():
    sig = inspect.signature(sadl::Display.__init__)
    params = list(sig.parameters.keys())
    assert "displayString" in params, "Missing parameter 'displayString'"
    assert "model" in params, "Missing parameter 'model'"

def test_sadl::display_has_displayString():
    assert hasattr(sadl::Display, "displayString")
    descriptor = None
    for klass in sadl::Display.__mro__:
        if "displayString" in klass.__dict__:
            descriptor = klass.__dict__["displayString"]
            break
    assert isinstance(descriptor, property)

def test_sadl::display_has_model():
    assert hasattr(sadl::Display, "model")
    descriptor = None
    for klass in sadl::Display.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_sadl::expr_is_not_abstract():
    assert not inspect.isabstract(sadl::Expr)


def test_sadl::expr_constructor_exists():
    assert callable(sadl::Expr.__init__)


def test_sadl::expr_constructor_args():
    sig = inspect.signature(sadl::Expr.__init__)
    params = list(sig.parameters.keys())



def test_sadl::query_is_not_abstract():
    assert not inspect.isabstract(sadl::Query)


def test_sadl::query_constructor_exists():
    assert callable(sadl::Query.__init__)


def test_sadl::query_constructor_args():
    sig = inspect.signature(sadl::Query.__init__)
    params = list(sig.parameters.keys())



def test_sadl::statement_is_not_abstract():
    assert not inspect.isabstract(sadl::Statement)


def test_sadl::statement_constructor_exists():
    assert callable(sadl::Statement.__init__)


def test_sadl::statement_constructor_args():
    sig = inspect.signature(sadl::Statement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::condition_is_not_abstract():
    assert not inspect.isabstract(sadl::Condition)


def test_sadl::condition_constructor_exists():
    assert callable(sadl::Condition.__init__)


def test_sadl::condition_constructor_args():
    sig = inspect.signature(sadl::Condition.__init__)
    params = list(sig.parameters.keys())



def test_sadl::resourceidentifier_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceIdentifier)


def test_sadl::resourceidentifier_constructor_exists():
    assert callable(sadl::ResourceIdentifier.__init__)


def test_sadl::resourceidentifier_constructor_args():
    sig = inspect.signature(sadl::ResourceIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sadl::existingresourcelist_is_not_abstract():
    assert not inspect.isabstract(sadl::ExistingResourceList)


def test_sadl::existingresourcelist_constructor_exists():
    assert callable(sadl::ExistingResourceList.__init__)


def test_sadl::existingresourcelist_constructor_args():
    sig = inspect.signature(sadl::ExistingResourceList.__init__)
    params = list(sig.parameters.keys())



def test_resourceidentifier_is_not_abstract():
    assert not inspect.isabstract(ResourceIdentifier)


def test_resourceidentifier_constructor_exists():
    assert callable(ResourceIdentifier.__init__)


def test_resourceidentifier_constructor_args():
    sig = inspect.signature(ResourceIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sadl::resourcebysetop_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceBySetOp)


def test_sadl::resourcebysetop_constructor_exists():
    assert callable(sadl::ResourceBySetOp.__init__)


def test_sadl::resourcebysetop_constructor_args():
    sig = inspect.signature(sadl::ResourceBySetOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl::resourcebysetop_has_op():
    assert hasattr(sadl::ResourceBySetOp, "op")
    descriptor = None
    for klass in sadl::ResourceBySetOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_sadl::resourcebysetop_has_annType():
    assert hasattr(sadl::ResourceBySetOp, "annType")
    descriptor = None
    for klass in sadl::ResourceBySetOp.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl::resourcebyrestriction_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceByRestriction)


def test_sadl::resourcebyrestriction_constructor_exists():
    assert callable(sadl::ResourceByRestriction.__init__)


def test_sadl::resourcebyrestriction_constructor_args():
    sig = inspect.signature(sadl::ResourceByRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl::resourcebyrestriction_has_annType():
    assert hasattr(sadl::ResourceByRestriction, "annType")
    descriptor = None
    for klass in sadl::ResourceByRestriction.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl::resourcebyname_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceByName)


def test_sadl::resourcebyname_constructor_exists():
    assert callable(sadl::ResourceByName.__init__)


def test_sadl::resourcebyname_constructor_args():
    sig = inspect.signature(sadl::ResourceByName.__init__)
    params = list(sig.parameters.keys())



def test_sadl::literalvalue_is_not_abstract():
    assert not inspect.isabstract(sadl::LiteralValue)


def test_sadl::literalvalue_constructor_exists():
    assert callable(sadl::LiteralValue.__init__)


def test_sadl::literalvalue_constructor_args():
    sig = inspect.signature(sadl::LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "literalString" in params, "Missing parameter 'literalString'"
    assert "literalNumber" in params, "Missing parameter 'literalNumber'"
    assert "literalBoolean" in params, "Missing parameter 'literalBoolean'"

def test_sadl::literalvalue_has_literalString():
    assert hasattr(sadl::LiteralValue, "literalString")
    descriptor = None
    for klass in sadl::LiteralValue.__mro__:
        if "literalString" in klass.__dict__:
            descriptor = klass.__dict__["literalString"]
            break
    assert isinstance(descriptor, property)

def test_sadl::literalvalue_has_literalNumber():
    assert hasattr(sadl::LiteralValue, "literalNumber")
    descriptor = None
    for klass in sadl::LiteralValue.__mro__:
        if "literalNumber" in klass.__dict__:
            descriptor = klass.__dict__["literalNumber"]
            break
    assert isinstance(descriptor, property)

def test_sadl::literalvalue_has_literalBoolean():
    assert hasattr(sadl::LiteralValue, "literalBoolean")
    descriptor = None
    for klass in sadl::LiteralValue.__mro__:
        if "literalBoolean" in klass.__dict__:
            descriptor = klass.__dict__["literalBoolean"]
            break
    assert isinstance(descriptor, property)



def test_sadl::literallist_is_not_abstract():
    assert not inspect.isabstract(sadl::LiteralList)


def test_sadl::literallist_constructor_exists():
    assert callable(sadl::LiteralList.__init__)


def test_sadl::literallist_constructor_args():
    sig = inspect.signature(sadl::LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_sadl::resourcelist_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceList)


def test_sadl::resourcelist_constructor_exists():
    assert callable(sadl::ResourceList.__init__)


def test_sadl::resourcelist_constructor_args():
    sig = inspect.signature(sadl::ResourceList.__init__)
    params = list(sig.parameters.keys())



def test_sadl::resourcename_is_not_abstract():
    assert not inspect.isabstract(sadl::ResourceName)


def test_sadl::resourcename_constructor_exists():
    assert callable(sadl::ResourceName.__init__)


def test_sadl::resourcename_constructor_args():
    sig = inspect.signature(sadl::ResourceName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl::resourcename_has_name():
    assert hasattr(sadl::ResourceName, "name")
    descriptor = None
    for klass in sadl::ResourceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sadl::resourcename_has_annType():
    assert hasattr(sadl::ResourceName, "annType")
    descriptor = None
    for klass in sadl::ResourceName.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl::contentlist_is_not_abstract():
    assert not inspect.isabstract(sadl::ContentList)


def test_sadl::contentlist_constructor_exists():
    assert callable(sadl::ContentList.__init__)


def test_sadl::contentlist_constructor_args():
    sig = inspect.signature(sadl::ContentList.__init__)
    params = list(sig.parameters.keys())
    assert "annContent" in params, "Missing parameter 'annContent'"

def test_sadl::contentlist_has_annContent():
    assert hasattr(sadl::ContentList, "annContent")
    descriptor = None
    for klass in sadl::ContentList.__mro__:
        if "annContent" in klass.__dict__:
            descriptor = klass.__dict__["annContent"]
            break
    assert isinstance(descriptor, property)



def test_sadl::modelelement_is_not_abstract():
    assert not inspect.isabstract(sadl::ModelElement)


def test_sadl::modelelement_constructor_exists():
    assert callable(sadl::ModelElement.__init__)


def test_sadl::modelelement_constructor_args():
    sig = inspect.signature(sadl::ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl::import_is_not_abstract():
    assert not inspect.isabstract(sadl::Import)


def test_sadl::import_constructor_exists():
    assert callable(sadl::Import.__init__)


def test_sadl::import_constructor_args():
    sig = inspect.signature(sadl::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_sadl::import_has_importURI():
    assert hasattr(sadl::Import, "importURI")
    descriptor = None
    for klass in sadl::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)

def test_sadl::import_has_alias():
    assert hasattr(sadl::Import, "alias")
    descriptor = None
    for klass in sadl::Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sadl::modelname_is_not_abstract():
    assert not inspect.isabstract(sadl::ModelName)


def test_sadl::modelname_constructor_exists():
    assert callable(sadl::ModelName.__init__)


def test_sadl::modelname_constructor_args():
    sig = inspect.signature(sadl::ModelName.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "annType" in params, "Missing parameter 'annType'"
    assert "alias" in params, "Missing parameter 'alias'"
    assert "baseUri" in params, "Missing parameter 'baseUri'"

def test_sadl::modelname_has_version():
    assert hasattr(sadl::ModelName, "version")
    descriptor = None
    for klass in sadl::ModelName.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sadl::modelname_has_annType():
    assert hasattr(sadl::ModelName, "annType")
    descriptor = None
    for klass in sadl::ModelName.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)

def test_sadl::modelname_has_alias():
    assert hasattr(sadl::ModelName, "alias")
    descriptor = None
    for klass in sadl::ModelName.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_sadl::modelname_has_baseUri():
    assert hasattr(sadl::ModelName, "baseUri")
    descriptor = None
    for klass in sadl::ModelName.__mro__:
        if "baseUri" in klass.__dict__:
            descriptor = klass.__dict__["baseUri"]
            break
    assert isinstance(descriptor, property)



def test_sadl::model_is_not_abstract():
    assert not inspect.isabstract(sadl::Model)


def test_sadl::model_constructor_exists():
    assert callable(sadl::Model.__init__)


def test_sadl::model_constructor_args():
    sig = inspect.signature(sadl::Model.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "string",
        "double",
        "boolean",
        "long",
        "data",
        "float",
        "dateTime",
        "decimal",
        "hexBinary",
        "base64Binary",
        "anyURI",
        "gDay",
        "int",
        "gMonth",
        "date",
        "duration",
        "time",
        "gMonthDay",
        "gYearMonth",
        "gYear",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
sadl::ValueRow_strategy = st.builds(
    sadl::ValueRow,
)
sadl::ValueTable_strategy = st.builds(
    sadl::ValueTable,
)
sadl::IntervalValue_strategy = st.builds(
    sadl::IntervalValue,
    op=
        safe_text
)
sadl::GraphPattern_strategy = st.builds(
    sadl::GraphPattern,
)
sadl::OrderElement_strategy = st.builds(
    sadl::OrderElement,
    order=
        safe_text
)
sadl::OrderList_strategy = st.builds(
    sadl::OrderList,
)
Expression_strategy = st.builds(
    Expression,
)
sadl::BinaryOpExpression_strategy = st.builds(
    sadl::BinaryOpExpression,
    op=
        safe_text
)
sadl::AskQueryExpression_strategy = st.builds(
    sadl::AskQueryExpression,
)
sadl::JunctionExpression_strategy = st.builds(
    sadl::JunctionExpression,
    op=
        safe_text
)
sadl::UnaryOpExpression_strategy = st.builds(
    sadl::UnaryOpExpression,
    op=
        safe_text
)
sadl::ConstructExpression_strategy = st.builds(
    sadl::ConstructExpression,
)
sadl::SelectExpression_strategy = st.builds(
    sadl::SelectExpression,
    distinct=
        safe_text,
    allVars=
        safe_text,
    orderby=
        safe_text
)
sadl::Expression_strategy = st.builds(
    sadl::Expression,
    func=
        safe_text
)
sadl::ElementSet_strategy = st.builds(
    sadl::ElementSet,
)
sadl::Object_strategy = st.builds(
    sadl::Object,
)
sadl::VariableList_strategy = st.builds(
    sadl::VariableList,
)
GraphPattern_strategy = st.builds(
    GraphPattern,
)
sadl::InstAttrPSV_strategy = st.builds(
    sadl::InstAttrPSV,
)
sadl::SubjProp_strategy = st.builds(
    sadl::SubjProp,
)
sadl::PropOfSubj_strategy = st.builds(
    sadl::PropOfSubj,
)
sadl::ExistentialNegation_strategy = st.builds(
    sadl::ExistentialNegation,
)
sadl::SubTypeOf_strategy = st.builds(
    sadl::SubTypeOf,
)
sadl::InstAttrSPV_strategy = st.builds(
    sadl::InstAttrSPV,
)
sadl::MergedTriples_strategy = st.builds(
    sadl::MergedTriples,
)
sadl::EmbeddedInstanceDeclaration_strategy = st.builds(
    sadl::EmbeddedInstanceDeclaration,
)
sadl::WithPhrase_strategy = st.builds(
    sadl::WithPhrase,
)
sadl::WithChain_strategy = st.builds(
    sadl::WithChain,
)
sadl::OfPhrase_strategy = st.builds(
    sadl::OfPhrase,
    article=
        safe_text
)
sadl::TypeDeclaration_strategy = st.builds(
    sadl::TypeDeclaration,
)
EmbeddedInstanceDeclaration_strategy = st.builds(
    EmbeddedInstanceDeclaration,
)
InstanceDeclarationStatement_strategy = st.builds(
    InstanceDeclarationStatement,
)
sadl::InstanceDeclaration_strategy = st.builds(
    sadl::InstanceDeclaration,
    article=
        safe_text
)
sadl::OfPatternReturningValues_strategy = st.builds(
    sadl::OfPatternReturningValues,
)
sadl::PropValPartialTriple_strategy = st.builds(
    sadl::PropValPartialTriple,
)
sadl::IsInverseOf_strategy = st.builds(
    sadl::IsInverseOf,
)
sadl::AdditionalPropertyInfo_strategy = st.builds(
    sadl::AdditionalPropertyInfo,
    isTrans=
        safe_text,
    isfunc=
        safe_text,
    isinvfunc=
        safe_text,
    isSym=
        safe_text
)
sadl::TypedBNode_strategy = st.builds(
    sadl::TypedBNode,
    article=
        safe_text
)
sadl::ExplicitValue_strategy = st.builds(
    sadl::ExplicitValue,
    valueList=
        safe_text,
    term=
        safe_text
)
sadl::EObject_strategy = st.builds(
    sadl::EObject,
)
Condition_strategy = st.builds(
    Condition,
)
sadl::CardCondition_strategy = st.builds(
    sadl::CardCondition,
    card=
        safe_text
)
sadl::MaxCardCondition_strategy = st.builds(
    sadl::MaxCardCondition,
    card=
        safe_text
)
sadl::MinCardCondition_strategy = st.builds(
    sadl::MinCardCondition,
    card=
        safe_text
)
sadl::HasValueCondition_strategy = st.builds(
    sadl::HasValueCondition,
)
sadl::SomeValuesCondition_strategy = st.builds(
    sadl::SomeValuesCondition,
)
sadl::AllValuesCondition_strategy = st.builds(
    sadl::AllValuesCondition,
)
sadl::PropertyOfClass_strategy = st.builds(
    sadl::PropertyOfClass,
)
sadl::Facets_strategy = st.builds(
    sadl::Facets,
    regex=
        safe_text,
    min=
        safe_text,
    minlen=
        safe_text,
    max=
        safe_text,
    maxlen=
        safe_text,
    values=
        safe_text,
    maxexin=
        safe_text,
    minexin=
        safe_text,
    len=
        safe_text
)
sadl::DataTypeRestriction_strategy = st.builds(
    sadl::DataTypeRestriction,
    basetype=
        safe_text,
    basetypes=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
sadl::TransitiveProperty_strategy = st.builds(
    sadl::TransitiveProperty,
)
sadl::NecessaryAndSufficient_strategy = st.builds(
    sadl::NecessaryAndSufficient,
    article=
        safe_text
)
sadl::SomeValuesFrom_strategy = st.builds(
    sadl::SomeValuesFrom,
)
sadl::InstanceDeclarationStatement_strategy = st.builds(
    sadl::InstanceDeclarationStatement,
)
sadl::EnumeratedAllValuesFrom_strategy = st.builds(
    sadl::EnumeratedAllValuesFrom,
)
sadl::InstancesAllDifferent_strategy = st.builds(
    sadl::InstancesAllDifferent,
)
sadl::HasValue_strategy = st.builds(
    sadl::HasValue,
)
sadl::DefaultValue_strategy = st.builds(
    sadl::DefaultValue,
    level=
        safe_text
)
sadl::InstanceDifferentFrom_strategy = st.builds(
    sadl::InstanceDifferentFrom,
)
sadl::DisjointClasses_strategy = st.builds(
    sadl::DisjointClasses,
)
sadl::EquivalentConcepts_strategy = st.builds(
    sadl::EquivalentConcepts,
)
sadl::InverseProperty_strategy = st.builds(
    sadl::InverseProperty,
)
sadl::PropertyDeclaration_strategy = st.builds(
    sadl::PropertyDeclaration,
    article=
        safe_text
)
sadl::ExistingInstanceAttribution_strategy = st.builds(
    sadl::ExistingInstanceAttribution,
)
sadl::SymmetricalProperty_strategy = st.builds(
    sadl::SymmetricalProperty,
)
sadl::InverseFunctionalProperty_strategy = st.builds(
    sadl::InverseFunctionalProperty,
)
sadl::ComplementOfClass_strategy = st.builds(
    sadl::ComplementOfClass,
)
sadl::AllValuesFrom_strategy = st.builds(
    sadl::AllValuesFrom,
)
sadl::EnumeratedAllAndSomeValuesFrom_strategy = st.builds(
    sadl::EnumeratedAllAndSomeValuesFrom,
)
sadl::Cardinality_strategy = st.builds(
    sadl::Cardinality,
)
sadl::MaxCardinality_strategy = st.builds(
    sadl::MaxCardinality,
)
sadl::MinCardinality_strategy = st.builds(
    sadl::MinCardinality,
)
sadl::FunctionalProperty_strategy = st.builds(
    sadl::FunctionalProperty,
)
sadl::ClassDeclaration_strategy = st.builds(
    sadl::ClassDeclaration,
)
sadl::UserDefinedDataType_strategy = st.builds(
    sadl::UserDefinedDataType,
)
ResourceBySetOp_strategy = st.builds(
    ResourceBySetOp,
)
sadl::IntersectionResource_strategy = st.builds(
    sadl::IntersectionResource,
)
sadl::UnionResource_strategy = st.builds(
    sadl::UnionResource,
)
sadl::RangeType_strategy = st.builds(
    sadl::RangeType,
    dataType=
        safe_text
)
sadl::Range_strategy = st.builds(
    sadl::Range,
    single=
        safe_text,
    list=
        safe_text,
    lists=
        safe_text
)
sadl::AddlClassInfo_strategy = st.builds(
    sadl::AddlClassInfo,
)
sadl::EnumeratedInstances_strategy = st.builds(
    sadl::EnumeratedInstances,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
sadl::Explanation_strategy = st.builds(
    sadl::Explanation,
    rulename=
        safe_text
)
sadl::Rule_strategy = st.builds(
    sadl::Rule,
    name=
        safe_text
)
sadl::Test_strategy = st.builds(
    sadl::Test,
)
sadl::Display_strategy = st.builds(
    sadl::Display,
    displayString=
        safe_text,
    model=
        safe_text
)
sadl::Expr_strategy = st.builds(
    sadl::Expr,
)
sadl::Query_strategy = st.builds(
    sadl::Query,
)
sadl::Statement_strategy = st.builds(
    sadl::Statement,
)
sadl::Condition_strategy = st.builds(
    sadl::Condition,
)
sadl::ResourceIdentifier_strategy = st.builds(
    sadl::ResourceIdentifier,
)
sadl::ExistingResourceList_strategy = st.builds(
    sadl::ExistingResourceList,
)
ResourceIdentifier_strategy = st.builds(
    ResourceIdentifier,
)
sadl::ResourceBySetOp_strategy = st.builds(
    sadl::ResourceBySetOp,
    op=
        safe_text,
    annType=
        safe_text
)
sadl::ResourceByRestriction_strategy = st.builds(
    sadl::ResourceByRestriction,
    annType=
        safe_text
)
sadl::ResourceByName_strategy = st.builds(
    sadl::ResourceByName,
)
sadl::LiteralValue_strategy = st.builds(
    sadl::LiteralValue,
    literalString=
        safe_text,
    literalNumber=
        safe_text,
    literalBoolean=
        safe_text
)
sadl::LiteralList_strategy = st.builds(
    sadl::LiteralList,
)
sadl::ResourceList_strategy = st.builds(
    sadl::ResourceList,
)
sadl::ResourceName_strategy = st.builds(
    sadl::ResourceName,
    name=
        safe_text,
    annType=
        safe_text
)
sadl::ContentList_strategy = st.builds(
    sadl::ContentList,
    annContent=
        safe_text
)
sadl::ModelElement_strategy = st.builds(
    sadl::ModelElement,
)
sadl::Import_strategy = st.builds(
    sadl::Import,
    importURI=
        safe_text,
    alias=
        safe_text
)
sadl::ModelName_strategy = st.builds(
    sadl::ModelName,
    version=
        safe_text,
    annType=
        safe_text,
    alias=
        safe_text,
    baseUri=
        safe_text
)
sadl::Model_strategy = st.builds(
    sadl::Model,
)

@given(instance=sadl::ValueRow_strategy)
@settings(max_examples=50)
def test_sadl::valuerow_instantiation(instance):
    assert isinstance(instance, sadl::ValueRow)

@given(instance=sadl::ValueTable_strategy)
@settings(max_examples=50)
def test_sadl::valuetable_instantiation(instance):
    assert isinstance(instance, sadl::ValueTable)

@given(instance=sadl::IntervalValue_strategy)
@settings(max_examples=50)
def test_sadl::intervalvalue_instantiation(instance):
    assert isinstance(instance, sadl::IntervalValue)

@given(instance=sadl::IntervalValue_strategy)
def test_sadl::intervalvalue_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sadl::IntervalValue_strategy)
def test_sadl::intervalvalue_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl::GraphPattern_strategy)
@settings(max_examples=50)
def test_sadl::graphpattern_instantiation(instance):
    assert isinstance(instance, sadl::GraphPattern)

@given(instance=sadl::OrderElement_strategy)
@settings(max_examples=50)
def test_sadl::orderelement_instantiation(instance):
    assert isinstance(instance, sadl::OrderElement)

@given(instance=sadl::OrderElement_strategy)
def test_sadl::orderelement_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=sadl::OrderElement_strategy)
def test_sadl::orderelement_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=sadl::OrderList_strategy)
@settings(max_examples=50)
def test_sadl::orderlist_instantiation(instance):
    assert isinstance(instance, sadl::OrderList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sadl::BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_sadl::binaryopexpression_instantiation(instance):
    assert isinstance(instance, sadl::BinaryOpExpression)

@given(instance=sadl::BinaryOpExpression_strategy)
def test_sadl::binaryopexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sadl::BinaryOpExpression_strategy)
def test_sadl::binaryopexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl::AskQueryExpression_strategy)
@settings(max_examples=50)
def test_sadl::askqueryexpression_instantiation(instance):
    assert isinstance(instance, sadl::AskQueryExpression)

@given(instance=sadl::JunctionExpression_strategy)
@settings(max_examples=50)
def test_sadl::junctionexpression_instantiation(instance):
    assert isinstance(instance, sadl::JunctionExpression)

@given(instance=sadl::JunctionExpression_strategy)
def test_sadl::junctionexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sadl::JunctionExpression_strategy)
def test_sadl::junctionexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl::UnaryOpExpression_strategy)
@settings(max_examples=50)
def test_sadl::unaryopexpression_instantiation(instance):
    assert isinstance(instance, sadl::UnaryOpExpression)

@given(instance=sadl::UnaryOpExpression_strategy)
def test_sadl::unaryopexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sadl::UnaryOpExpression_strategy)
def test_sadl::unaryopexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl::ConstructExpression_strategy)
@settings(max_examples=50)
def test_sadl::constructexpression_instantiation(instance):
    assert isinstance(instance, sadl::ConstructExpression)

@given(instance=sadl::SelectExpression_strategy)
@settings(max_examples=50)
def test_sadl::selectexpression_instantiation(instance):
    assert isinstance(instance, sadl::SelectExpression)

@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_distinct_type(instance):
    assert isinstance(instance.distinct, str)


@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original

@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_allVars_type(instance):
    assert isinstance(instance.allVars, str)


@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_allVars_setter(instance):
    original = instance.allVars
    instance.allVars = original
    assert instance.allVars == original

@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_orderby_type(instance):
    assert isinstance(instance.orderby, str)


@given(instance=sadl::SelectExpression_strategy)
def test_sadl::selectexpression_orderby_setter(instance):
    original = instance.orderby
    instance.orderby = original
    assert instance.orderby == original

@given(instance=sadl::Expression_strategy)
@settings(max_examples=50)
def test_sadl::expression_instantiation(instance):
    assert isinstance(instance, sadl::Expression)

@given(instance=sadl::Expression_strategy)
def test_sadl::expression_func_type(instance):
    assert isinstance(instance.func, str)


@given(instance=sadl::Expression_strategy)
def test_sadl::expression_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=sadl::ElementSet_strategy)
@settings(max_examples=50)
def test_sadl::elementset_instantiation(instance):
    assert isinstance(instance, sadl::ElementSet)

@given(instance=sadl::Object_strategy)
@settings(max_examples=50)
def test_sadl::object_instantiation(instance):
    assert isinstance(instance, sadl::Object)

@given(instance=sadl::VariableList_strategy)
@settings(max_examples=50)
def test_sadl::variablelist_instantiation(instance):
    assert isinstance(instance, sadl::VariableList)

@given(instance=GraphPattern_strategy)
@settings(max_examples=50)
def test_graphpattern_instantiation(instance):
    assert isinstance(instance, GraphPattern)

@given(instance=sadl::InstAttrPSV_strategy)
@settings(max_examples=50)
def test_sadl::instattrpsv_instantiation(instance):
    assert isinstance(instance, sadl::InstAttrPSV)

@given(instance=sadl::SubjProp_strategy)
@settings(max_examples=50)
def test_sadl::subjprop_instantiation(instance):
    assert isinstance(instance, sadl::SubjProp)

@given(instance=sadl::PropOfSubj_strategy)
@settings(max_examples=50)
def test_sadl::propofsubj_instantiation(instance):
    assert isinstance(instance, sadl::PropOfSubj)

@given(instance=sadl::ExistentialNegation_strategy)
@settings(max_examples=50)
def test_sadl::existentialnegation_instantiation(instance):
    assert isinstance(instance, sadl::ExistentialNegation)

@given(instance=sadl::SubTypeOf_strategy)
@settings(max_examples=50)
def test_sadl::subtypeof_instantiation(instance):
    assert isinstance(instance, sadl::SubTypeOf)

@given(instance=sadl::InstAttrSPV_strategy)
@settings(max_examples=50)
def test_sadl::instattrspv_instantiation(instance):
    assert isinstance(instance, sadl::InstAttrSPV)

@given(instance=sadl::MergedTriples_strategy)
@settings(max_examples=50)
def test_sadl::mergedtriples_instantiation(instance):
    assert isinstance(instance, sadl::MergedTriples)

@given(instance=sadl::EmbeddedInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::embeddedinstancedeclaration_instantiation(instance):
    assert isinstance(instance, sadl::EmbeddedInstanceDeclaration)

@given(instance=sadl::WithPhrase_strategy)
@settings(max_examples=50)
def test_sadl::withphrase_instantiation(instance):
    assert isinstance(instance, sadl::WithPhrase)

@given(instance=sadl::WithChain_strategy)
@settings(max_examples=50)
def test_sadl::withchain_instantiation(instance):
    assert isinstance(instance, sadl::WithChain)

@given(instance=sadl::OfPhrase_strategy)
@settings(max_examples=50)
def test_sadl::ofphrase_instantiation(instance):
    assert isinstance(instance, sadl::OfPhrase)

@given(instance=sadl::OfPhrase_strategy)
def test_sadl::ofphrase_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sadl::OfPhrase_strategy)
def test_sadl::ofphrase_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::typedeclaration_instantiation(instance):
    assert isinstance(instance, sadl::TypeDeclaration)

@given(instance=EmbeddedInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_embeddedinstancedeclaration_instantiation(instance):
    assert isinstance(instance, EmbeddedInstanceDeclaration)

@given(instance=InstanceDeclarationStatement_strategy)
@settings(max_examples=50)
def test_instancedeclarationstatement_instantiation(instance):
    assert isinstance(instance, InstanceDeclarationStatement)

@given(instance=sadl::InstanceDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::instancedeclaration_instantiation(instance):
    assert isinstance(instance, sadl::InstanceDeclaration)

@given(instance=sadl::InstanceDeclaration_strategy)
def test_sadl::instancedeclaration_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sadl::InstanceDeclaration_strategy)
def test_sadl::instancedeclaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl::OfPatternReturningValues_strategy)
@settings(max_examples=50)
def test_sadl::ofpatternreturningvalues_instantiation(instance):
    assert isinstance(instance, sadl::OfPatternReturningValues)

@given(instance=sadl::PropValPartialTriple_strategy)
@settings(max_examples=50)
def test_sadl::propvalpartialtriple_instantiation(instance):
    assert isinstance(instance, sadl::PropValPartialTriple)

@given(instance=sadl::IsInverseOf_strategy)
@settings(max_examples=50)
def test_sadl::isinverseof_instantiation(instance):
    assert isinstance(instance, sadl::IsInverseOf)

@given(instance=sadl::AdditionalPropertyInfo_strategy)
@settings(max_examples=50)
def test_sadl::additionalpropertyinfo_instantiation(instance):
    assert isinstance(instance, sadl::AdditionalPropertyInfo)

@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isTrans_type(instance):
    assert isinstance(instance.isTrans, str)


@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isTrans_setter(instance):
    original = instance.isTrans
    instance.isTrans = original
    assert instance.isTrans == original

@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isfunc_type(instance):
    assert isinstance(instance.isfunc, str)


@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isfunc_setter(instance):
    original = instance.isfunc
    instance.isfunc = original
    assert instance.isfunc == original

@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isinvfunc_type(instance):
    assert isinstance(instance.isinvfunc, str)


@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isinvfunc_setter(instance):
    original = instance.isinvfunc
    instance.isinvfunc = original
    assert instance.isinvfunc == original

@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isSym_type(instance):
    assert isinstance(instance.isSym, str)


@given(instance=sadl::AdditionalPropertyInfo_strategy)
def test_sadl::additionalpropertyinfo_isSym_setter(instance):
    original = instance.isSym
    instance.isSym = original
    assert instance.isSym == original

@given(instance=sadl::TypedBNode_strategy)
@settings(max_examples=50)
def test_sadl::typedbnode_instantiation(instance):
    assert isinstance(instance, sadl::TypedBNode)

@given(instance=sadl::TypedBNode_strategy)
def test_sadl::typedbnode_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sadl::TypedBNode_strategy)
def test_sadl::typedbnode_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl::ExplicitValue_strategy)
@settings(max_examples=50)
def test_sadl::explicitvalue_instantiation(instance):
    assert isinstance(instance, sadl::ExplicitValue)

@given(instance=sadl::ExplicitValue_strategy)
def test_sadl::explicitvalue_valueList_type(instance):
    assert isinstance(instance.valueList, str)


@given(instance=sadl::ExplicitValue_strategy)
def test_sadl::explicitvalue_valueList_setter(instance):
    original = instance.valueList
    instance.valueList = original
    assert instance.valueList == original

@given(instance=sadl::ExplicitValue_strategy)
def test_sadl::explicitvalue_term_type(instance):
    assert isinstance(instance.term, str)


@given(instance=sadl::ExplicitValue_strategy)
def test_sadl::explicitvalue_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=sadl::EObject_strategy)
@settings(max_examples=50)
def test_sadl::eobject_instantiation(instance):
    assert isinstance(instance, sadl::EObject)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sadl::CardCondition_strategy)
@settings(max_examples=50)
def test_sadl::cardcondition_instantiation(instance):
    assert isinstance(instance, sadl::CardCondition)

@given(instance=sadl::CardCondition_strategy)
def test_sadl::cardcondition_card_type(instance):
    assert isinstance(instance.card, str)


@given(instance=sadl::CardCondition_strategy)
def test_sadl::cardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl::MaxCardCondition_strategy)
@settings(max_examples=50)
def test_sadl::maxcardcondition_instantiation(instance):
    assert isinstance(instance, sadl::MaxCardCondition)

@given(instance=sadl::MaxCardCondition_strategy)
def test_sadl::maxcardcondition_card_type(instance):
    assert isinstance(instance.card, str)


@given(instance=sadl::MaxCardCondition_strategy)
def test_sadl::maxcardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl::MinCardCondition_strategy)
@settings(max_examples=50)
def test_sadl::mincardcondition_instantiation(instance):
    assert isinstance(instance, sadl::MinCardCondition)

@given(instance=sadl::MinCardCondition_strategy)
def test_sadl::mincardcondition_card_type(instance):
    assert isinstance(instance.card, str)


@given(instance=sadl::MinCardCondition_strategy)
def test_sadl::mincardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl::HasValueCondition_strategy)
@settings(max_examples=50)
def test_sadl::hasvaluecondition_instantiation(instance):
    assert isinstance(instance, sadl::HasValueCondition)

@given(instance=sadl::SomeValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl::somevaluescondition_instantiation(instance):
    assert isinstance(instance, sadl::SomeValuesCondition)

@given(instance=sadl::AllValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl::allvaluescondition_instantiation(instance):
    assert isinstance(instance, sadl::AllValuesCondition)

@given(instance=sadl::PropertyOfClass_strategy)
@settings(max_examples=50)
def test_sadl::propertyofclass_instantiation(instance):
    assert isinstance(instance, sadl::PropertyOfClass)

@given(instance=sadl::Facets_strategy)
@settings(max_examples=50)
def test_sadl::facets_instantiation(instance):
    assert isinstance(instance, sadl::Facets)

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_regex_type(instance):
    assert isinstance(instance.regex, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_minlen_type(instance):
    assert isinstance(instance.minlen, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_minlen_setter(instance):
    original = instance.minlen
    instance.minlen = original
    assert instance.minlen == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_max_type(instance):
    assert isinstance(instance.max, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_maxlen_type(instance):
    assert isinstance(instance.maxlen, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_maxexin_type(instance):
    assert isinstance(instance.maxexin, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_maxexin_setter(instance):
    original = instance.maxexin
    instance.maxexin = original
    assert instance.maxexin == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_minexin_type(instance):
    assert isinstance(instance.minexin, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_minexin_setter(instance):
    original = instance.minexin
    instance.minexin = original
    assert instance.minexin == original

@given(instance=sadl::Facets_strategy)
def test_sadl::facets_len_type(instance):
    assert isinstance(instance.len, str)


@given(instance=sadl::Facets_strategy)
def test_sadl::facets_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original

@given(instance=sadl::DataTypeRestriction_strategy)
@settings(max_examples=50)
def test_sadl::datatyperestriction_instantiation(instance):
    assert isinstance(instance, sadl::DataTypeRestriction)

@given(instance=sadl::DataTypeRestriction_strategy)
def test_sadl::datatyperestriction_basetype_type(instance):
    assert isinstance(instance.basetype, str)


@given(instance=sadl::DataTypeRestriction_strategy)
def test_sadl::datatyperestriction_basetype_setter(instance):
    original = instance.basetype
    instance.basetype = original
    assert instance.basetype == original

@given(instance=sadl::DataTypeRestriction_strategy)
def test_sadl::datatyperestriction_basetypes_type(instance):
    assert isinstance(instance.basetypes, str)


@given(instance=sadl::DataTypeRestriction_strategy)
def test_sadl::datatyperestriction_basetypes_setter(instance):
    original = instance.basetypes
    instance.basetypes = original
    assert instance.basetypes == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sadl::TransitiveProperty_strategy)
@settings(max_examples=50)
def test_sadl::transitiveproperty_instantiation(instance):
    assert isinstance(instance, sadl::TransitiveProperty)

@given(instance=sadl::NecessaryAndSufficient_strategy)
@settings(max_examples=50)
def test_sadl::necessaryandsufficient_instantiation(instance):
    assert isinstance(instance, sadl::NecessaryAndSufficient)

@given(instance=sadl::NecessaryAndSufficient_strategy)
def test_sadl::necessaryandsufficient_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sadl::NecessaryAndSufficient_strategy)
def test_sadl::necessaryandsufficient_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl::SomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl::somevaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl::SomeValuesFrom)

@given(instance=sadl::InstanceDeclarationStatement_strategy)
@settings(max_examples=50)
def test_sadl::instancedeclarationstatement_instantiation(instance):
    assert isinstance(instance, sadl::InstanceDeclarationStatement)

@given(instance=sadl::EnumeratedAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl::enumeratedallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl::EnumeratedAllValuesFrom)

@given(instance=sadl::InstancesAllDifferent_strategy)
@settings(max_examples=50)
def test_sadl::instancesalldifferent_instantiation(instance):
    assert isinstance(instance, sadl::InstancesAllDifferent)

@given(instance=sadl::HasValue_strategy)
@settings(max_examples=50)
def test_sadl::hasvalue_instantiation(instance):
    assert isinstance(instance, sadl::HasValue)

@given(instance=sadl::DefaultValue_strategy)
@settings(max_examples=50)
def test_sadl::defaultvalue_instantiation(instance):
    assert isinstance(instance, sadl::DefaultValue)

@given(instance=sadl::DefaultValue_strategy)
def test_sadl::defaultvalue_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=sadl::DefaultValue_strategy)
def test_sadl::defaultvalue_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=sadl::InstanceDifferentFrom_strategy)
@settings(max_examples=50)
def test_sadl::instancedifferentfrom_instantiation(instance):
    assert isinstance(instance, sadl::InstanceDifferentFrom)

@given(instance=sadl::DisjointClasses_strategy)
@settings(max_examples=50)
def test_sadl::disjointclasses_instantiation(instance):
    assert isinstance(instance, sadl::DisjointClasses)

@given(instance=sadl::EquivalentConcepts_strategy)
@settings(max_examples=50)
def test_sadl::equivalentconcepts_instantiation(instance):
    assert isinstance(instance, sadl::EquivalentConcepts)

@given(instance=sadl::InverseProperty_strategy)
@settings(max_examples=50)
def test_sadl::inverseproperty_instantiation(instance):
    assert isinstance(instance, sadl::InverseProperty)

@given(instance=sadl::PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::propertydeclaration_instantiation(instance):
    assert isinstance(instance, sadl::PropertyDeclaration)

@given(instance=sadl::PropertyDeclaration_strategy)
def test_sadl::propertydeclaration_article_type(instance):
    assert isinstance(instance.article, str)


@given(instance=sadl::PropertyDeclaration_strategy)
def test_sadl::propertydeclaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl::ExistingInstanceAttribution_strategy)
@settings(max_examples=50)
def test_sadl::existinginstanceattribution_instantiation(instance):
    assert isinstance(instance, sadl::ExistingInstanceAttribution)

@given(instance=sadl::SymmetricalProperty_strategy)
@settings(max_examples=50)
def test_sadl::symmetricalproperty_instantiation(instance):
    assert isinstance(instance, sadl::SymmetricalProperty)

@given(instance=sadl::InverseFunctionalProperty_strategy)
@settings(max_examples=50)
def test_sadl::inversefunctionalproperty_instantiation(instance):
    assert isinstance(instance, sadl::InverseFunctionalProperty)

@given(instance=sadl::ComplementOfClass_strategy)
@settings(max_examples=50)
def test_sadl::complementofclass_instantiation(instance):
    assert isinstance(instance, sadl::ComplementOfClass)

@given(instance=sadl::AllValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl::allvaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl::AllValuesFrom)

@given(instance=sadl::EnumeratedAllAndSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl::enumeratedallandsomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl::EnumeratedAllAndSomeValuesFrom)

@given(instance=sadl::Cardinality_strategy)
@settings(max_examples=50)
def test_sadl::cardinality_instantiation(instance):
    assert isinstance(instance, sadl::Cardinality)

@given(instance=sadl::MaxCardinality_strategy)
@settings(max_examples=50)
def test_sadl::maxcardinality_instantiation(instance):
    assert isinstance(instance, sadl::MaxCardinality)

@given(instance=sadl::MinCardinality_strategy)
@settings(max_examples=50)
def test_sadl::mincardinality_instantiation(instance):
    assert isinstance(instance, sadl::MinCardinality)

@given(instance=sadl::FunctionalProperty_strategy)
@settings(max_examples=50)
def test_sadl::functionalproperty_instantiation(instance):
    assert isinstance(instance, sadl::FunctionalProperty)

@given(instance=sadl::ClassDeclaration_strategy)
@settings(max_examples=50)
def test_sadl::classdeclaration_instantiation(instance):
    assert isinstance(instance, sadl::ClassDeclaration)

@given(instance=sadl::UserDefinedDataType_strategy)
@settings(max_examples=50)
def test_sadl::userdefineddatatype_instantiation(instance):
    assert isinstance(instance, sadl::UserDefinedDataType)

@given(instance=ResourceBySetOp_strategy)
@settings(max_examples=50)
def test_resourcebysetop_instantiation(instance):
    assert isinstance(instance, ResourceBySetOp)

@given(instance=sadl::IntersectionResource_strategy)
@settings(max_examples=50)
def test_sadl::intersectionresource_instantiation(instance):
    assert isinstance(instance, sadl::IntersectionResource)

@given(instance=sadl::UnionResource_strategy)
@settings(max_examples=50)
def test_sadl::unionresource_instantiation(instance):
    assert isinstance(instance, sadl::UnionResource)

@given(instance=sadl::RangeType_strategy)
@settings(max_examples=50)
def test_sadl::rangetype_instantiation(instance):
    assert isinstance(instance, sadl::RangeType)

@given(instance=sadl::RangeType_strategy)
def test_sadl::rangetype_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=sadl::RangeType_strategy)
def test_sadl::rangetype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sadl::Range_strategy)
@settings(max_examples=50)
def test_sadl::range_instantiation(instance):
    assert isinstance(instance, sadl::Range)

@given(instance=sadl::Range_strategy)
def test_sadl::range_single_type(instance):
    assert isinstance(instance.single, str)


@given(instance=sadl::Range_strategy)
def test_sadl::range_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original

@given(instance=sadl::Range_strategy)
def test_sadl::range_list_type(instance):
    assert isinstance(instance.list, str)


@given(instance=sadl::Range_strategy)
def test_sadl::range_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sadl::Range_strategy)
def test_sadl::range_lists_type(instance):
    assert isinstance(instance.lists, str)


@given(instance=sadl::Range_strategy)
def test_sadl::range_lists_setter(instance):
    original = instance.lists
    instance.lists = original
    assert instance.lists == original

@given(instance=sadl::AddlClassInfo_strategy)
@settings(max_examples=50)
def test_sadl::addlclassinfo_instantiation(instance):
    assert isinstance(instance, sadl::AddlClassInfo)

@given(instance=sadl::EnumeratedInstances_strategy)
@settings(max_examples=50)
def test_sadl::enumeratedinstances_instantiation(instance):
    assert isinstance(instance, sadl::EnumeratedInstances)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=sadl::Explanation_strategy)
@settings(max_examples=50)
def test_sadl::explanation_instantiation(instance):
    assert isinstance(instance, sadl::Explanation)

@given(instance=sadl::Explanation_strategy)
def test_sadl::explanation_rulename_type(instance):
    assert isinstance(instance.rulename, str)


@given(instance=sadl::Explanation_strategy)
def test_sadl::explanation_rulename_setter(instance):
    original = instance.rulename
    instance.rulename = original
    assert instance.rulename == original

@given(instance=sadl::Rule_strategy)
@settings(max_examples=50)
def test_sadl::rule_instantiation(instance):
    assert isinstance(instance, sadl::Rule)

@given(instance=sadl::Rule_strategy)
def test_sadl::rule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sadl::Rule_strategy)
def test_sadl::rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sadl::Test_strategy)
@settings(max_examples=50)
def test_sadl::test_instantiation(instance):
    assert isinstance(instance, sadl::Test)

@given(instance=sadl::Display_strategy)
@settings(max_examples=50)
def test_sadl::display_instantiation(instance):
    assert isinstance(instance, sadl::Display)

@given(instance=sadl::Display_strategy)
def test_sadl::display_displayString_type(instance):
    assert isinstance(instance.displayString, str)


@given(instance=sadl::Display_strategy)
def test_sadl::display_displayString_setter(instance):
    original = instance.displayString
    instance.displayString = original
    assert instance.displayString == original

@given(instance=sadl::Display_strategy)
def test_sadl::display_model_type(instance):
    assert isinstance(instance.model, str)


@given(instance=sadl::Display_strategy)
def test_sadl::display_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=sadl::Expr_strategy)
@settings(max_examples=50)
def test_sadl::expr_instantiation(instance):
    assert isinstance(instance, sadl::Expr)

@given(instance=sadl::Query_strategy)
@settings(max_examples=50)
def test_sadl::query_instantiation(instance):
    assert isinstance(instance, sadl::Query)

@given(instance=sadl::Statement_strategy)
@settings(max_examples=50)
def test_sadl::statement_instantiation(instance):
    assert isinstance(instance, sadl::Statement)

@given(instance=sadl::Condition_strategy)
@settings(max_examples=50)
def test_sadl::condition_instantiation(instance):
    assert isinstance(instance, sadl::Condition)

@given(instance=sadl::ResourceIdentifier_strategy)
@settings(max_examples=50)
def test_sadl::resourceidentifier_instantiation(instance):
    assert isinstance(instance, sadl::ResourceIdentifier)

@given(instance=sadl::ExistingResourceList_strategy)
@settings(max_examples=50)
def test_sadl::existingresourcelist_instantiation(instance):
    assert isinstance(instance, sadl::ExistingResourceList)

@given(instance=ResourceIdentifier_strategy)
@settings(max_examples=50)
def test_resourceidentifier_instantiation(instance):
    assert isinstance(instance, ResourceIdentifier)

@given(instance=sadl::ResourceBySetOp_strategy)
@settings(max_examples=50)
def test_sadl::resourcebysetop_instantiation(instance):
    assert isinstance(instance, sadl::ResourceBySetOp)

@given(instance=sadl::ResourceBySetOp_strategy)
def test_sadl::resourcebysetop_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=sadl::ResourceBySetOp_strategy)
def test_sadl::resourcebysetop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl::ResourceBySetOp_strategy)
def test_sadl::resourcebysetop_annType_type(instance):
    assert isinstance(instance.annType, str)


@given(instance=sadl::ResourceBySetOp_strategy)
def test_sadl::resourcebysetop_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl::ResourceByRestriction_strategy)
@settings(max_examples=50)
def test_sadl::resourcebyrestriction_instantiation(instance):
    assert isinstance(instance, sadl::ResourceByRestriction)

@given(instance=sadl::ResourceByRestriction_strategy)
def test_sadl::resourcebyrestriction_annType_type(instance):
    assert isinstance(instance.annType, str)


@given(instance=sadl::ResourceByRestriction_strategy)
def test_sadl::resourcebyrestriction_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl::ResourceByName_strategy)
@settings(max_examples=50)
def test_sadl::resourcebyname_instantiation(instance):
    assert isinstance(instance, sadl::ResourceByName)

@given(instance=sadl::LiteralValue_strategy)
@settings(max_examples=50)
def test_sadl::literalvalue_instantiation(instance):
    assert isinstance(instance, sadl::LiteralValue)

@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalString_type(instance):
    assert isinstance(instance.literalString, str)


@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalString_setter(instance):
    original = instance.literalString
    instance.literalString = original
    assert instance.literalString == original

@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalNumber_type(instance):
    assert isinstance(instance.literalNumber, str)


@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalNumber_setter(instance):
    original = instance.literalNumber
    instance.literalNumber = original
    assert instance.literalNumber == original

@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalBoolean_type(instance):
    assert isinstance(instance.literalBoolean, str)


@given(instance=sadl::LiteralValue_strategy)
def test_sadl::literalvalue_literalBoolean_setter(instance):
    original = instance.literalBoolean
    instance.literalBoolean = original
    assert instance.literalBoolean == original

@given(instance=sadl::LiteralList_strategy)
@settings(max_examples=50)
def test_sadl::literallist_instantiation(instance):
    assert isinstance(instance, sadl::LiteralList)

@given(instance=sadl::ResourceList_strategy)
@settings(max_examples=50)
def test_sadl::resourcelist_instantiation(instance):
    assert isinstance(instance, sadl::ResourceList)

@given(instance=sadl::ResourceName_strategy)
@settings(max_examples=50)
def test_sadl::resourcename_instantiation(instance):
    assert isinstance(instance, sadl::ResourceName)

@given(instance=sadl::ResourceName_strategy)
def test_sadl::resourcename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sadl::ResourceName_strategy)
def test_sadl::resourcename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sadl::ResourceName_strategy)
def test_sadl::resourcename_annType_type(instance):
    assert isinstance(instance.annType, str)


@given(instance=sadl::ResourceName_strategy)
def test_sadl::resourcename_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl::ContentList_strategy)
@settings(max_examples=50)
def test_sadl::contentlist_instantiation(instance):
    assert isinstance(instance, sadl::ContentList)

@given(instance=sadl::ContentList_strategy)
def test_sadl::contentlist_annContent_type(instance):
    assert isinstance(instance.annContent, str)


@given(instance=sadl::ContentList_strategy)
def test_sadl::contentlist_annContent_setter(instance):
    original = instance.annContent
    instance.annContent = original
    assert instance.annContent == original

@given(instance=sadl::ModelElement_strategy)
@settings(max_examples=50)
def test_sadl::modelelement_instantiation(instance):
    assert isinstance(instance, sadl::ModelElement)

@given(instance=sadl::Import_strategy)
@settings(max_examples=50)
def test_sadl::import_instantiation(instance):
    assert isinstance(instance, sadl::Import)

@given(instance=sadl::Import_strategy)
def test_sadl::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=sadl::Import_strategy)
def test_sadl::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=sadl::Import_strategy)
def test_sadl::import_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sadl::Import_strategy)
def test_sadl::import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sadl::ModelName_strategy)
@settings(max_examples=50)
def test_sadl::modelname_instantiation(instance):
    assert isinstance(instance, sadl::ModelName)

@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_annType_type(instance):
    assert isinstance(instance.annType, str)


@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_baseUri_type(instance):
    assert isinstance(instance.baseUri, str)


@given(instance=sadl::ModelName_strategy)
def test_sadl::modelname_baseUri_setter(instance):
    original = instance.baseUri
    instance.baseUri = original
    assert instance.baseUri == original

@given(instance=sadl::Model_strategy)
@settings(max_examples=50)
def test_sadl::model_instantiation(instance):
    assert isinstance(instance, sadl::Model)
