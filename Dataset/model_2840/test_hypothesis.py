import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    backtrackingContentAssistTest::Init,
    backtrackingContentAssistTest::PackageRef,
    backtrackingContentAssistTest::Post,
    backtrackingContentAssistTest::Body,
    backtrackingContentAssistTest::ContextDecl,
    backtrackingContentAssistTest::PackageDeclaration,
    backtrackingContentAssistTest::Document,
    backtrackingContentAssistTest::Der,
    backtrackingContentAssistTest::Parameter,
    backtrackingContentAssistTest::Definition,
    backtrackingContentAssistTest::Invariant,
    backtrackingContentAssistTest::ClassifierRef,
    ContextDecl,
    backtrackingContentAssistTest::ClassifierContextDecl,
    backtrackingContentAssistTest::PropertyContextDecl,
    NameExp,
    backtrackingContentAssistTest::SimpleNameExp,
    backtrackingContentAssistTest::PathNameExp,
    backtrackingContentAssistTest::LetVariable,
    backtrackingContentAssistTest::iteratorAccumulator,
    backtrackingContentAssistTest::iteratorVariable,
    PrimitiveLiteralExp,
    backtrackingContentAssistTest::NullLiteralExp,
    backtrackingContentAssistTest::BooleanLiteralExp,
    backtrackingContentAssistTest::InvalidLiteralExp,
    backtrackingContentAssistTest::StringLiteralExp,
    backtrackingContentAssistTest::NumberLiteralExp,
    backtrackingContentAssistTest::EObject,
    backtrackingContentAssistTest::CollectionLiteralPart,
    backtrackingContentAssistTest::tuplePart,
    CollectionLiteralExp,
    Expression,
    backtrackingContentAssistTest::NestedExp,
    backtrackingContentAssistTest::LetExp,
    backtrackingContentAssistTest::PreExp,
    backtrackingContentAssistTest::TypeExp,
    backtrackingContentAssistTest::OclMessage,
    backtrackingContentAssistTest::CollectionLiteralExp,
    backtrackingContentAssistTest::InfixExp,
    backtrackingContentAssistTest::IfExp,
    backtrackingContentAssistTest::SelfExp,
    backtrackingContentAssistTest::SquareBracketExp,
    backtrackingContentAssistTest::PrefixExp,
    backtrackingContentAssistTest::RoundBracketExp,
    TypeExp,
    backtrackingContentAssistTest::TupleType,
    backtrackingContentAssistTest::CollectionType,
    backtrackingContentAssistTest::NameExp,
    backtrackingContentAssistTest::PrimitiveType,
    backtrackingContentAssistTest::TupleLiteralPart,
    backtrackingContentAssistTest::TupleLiteralExp,
    backtrackingContentAssistTest::PrimitiveLiteralExp,
    PropertyRef,
    backtrackingContentAssistTest::QualifiedPropertyRef,
    OperationRef,
    backtrackingContentAssistTest::QualifiedOperationRef,
    ClassifierRef,
    backtrackingContentAssistTest::QualifiedClassifierRef,
    backtrackingContentAssistTest::PropertyRef,
    backtrackingContentAssistTest::OclMessageArg,
    backtrackingContentAssistTest::NavigatingExp,
    OclMessageArg,
    NavigatingExp,
    backtrackingContentAssistTest::Expression,
    backtrackingContentAssistTest::SimplePropertyRef,
    backtrackingContentAssistTest::SimpleOperationRef,
    backtrackingContentAssistTest::SimpleClassifierRef,
    PackageRef,
    backtrackingContentAssistTest::SimplePackageRef,
    backtrackingContentAssistTest::QualifiedPackageRef,
    backtrackingContentAssistTest::Pre,
    backtrackingContentAssistTest::OperationRef,
    backtrackingContentAssistTest::OperationContextDecl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_backtrackingcontentassisttest::init_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Init)


def test_backtrackingcontentassisttest::init_constructor_exists():
    assert callable(backtrackingContentAssistTest::Init.__init__)


def test_backtrackingcontentassisttest::init_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Init.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::packageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PackageRef)


def test_backtrackingcontentassisttest::packageref_constructor_exists():
    assert callable(backtrackingContentAssistTest::PackageRef.__init__)


def test_backtrackingcontentassisttest::packageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PackageRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::post_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Post)


def test_backtrackingcontentassisttest::post_constructor_exists():
    assert callable(backtrackingContentAssistTest::Post.__init__)


def test_backtrackingcontentassisttest::post_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Post.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest::post_has_constraintName():
    assert hasattr(backtrackingContentAssistTest::Post, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Post.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::body_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Body)


def test_backtrackingcontentassisttest::body_constructor_exists():
    assert callable(backtrackingContentAssistTest::Body.__init__)


def test_backtrackingcontentassisttest::body_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Body.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest::body_has_constraintName():
    assert hasattr(backtrackingContentAssistTest::Body, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Body.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::contextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::ContextDecl)


def test_backtrackingcontentassisttest::contextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest::ContextDecl.__init__)


def test_backtrackingcontentassisttest::contextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::ContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PackageDeclaration)


def test_backtrackingcontentassisttest::packagedeclaration_constructor_exists():
    assert callable(backtrackingContentAssistTest::PackageDeclaration.__init__)


def test_backtrackingcontentassisttest::packagedeclaration_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::document_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Document)


def test_backtrackingcontentassisttest::document_constructor_exists():
    assert callable(backtrackingContentAssistTest::Document.__init__)


def test_backtrackingcontentassisttest::document_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Document.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::der_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Der)


def test_backtrackingcontentassisttest::der_constructor_exists():
    assert callable(backtrackingContentAssistTest::Der.__init__)


def test_backtrackingcontentassisttest::der_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Der.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::parameter_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Parameter)


def test_backtrackingcontentassisttest::parameter_constructor_exists():
    assert callable(backtrackingContentAssistTest::Parameter.__init__)


def test_backtrackingcontentassisttest::parameter_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::parameter_has_name():
    assert hasattr(backtrackingContentAssistTest::Parameter, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::definition_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Definition)


def test_backtrackingcontentassisttest::definition_constructor_exists():
    assert callable(backtrackingContentAssistTest::Definition.__init__)


def test_backtrackingcontentassisttest::definition_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Definition.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "constraintName" in params, "Missing parameter 'constraintName'"
    assert "constrainedName" in params, "Missing parameter 'constrainedName'"

def test_backtrackingcontentassisttest::definition_has_static():
    assert hasattr(backtrackingContentAssistTest::Definition, "static")
    descriptor = None
    for klass in backtrackingContentAssistTest::Definition.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest::definition_has_constraintName():
    assert hasattr(backtrackingContentAssistTest::Definition, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Definition.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest::definition_has_constrainedName():
    assert hasattr(backtrackingContentAssistTest::Definition, "constrainedName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Definition.__mro__:
        if "constrainedName" in klass.__dict__:
            descriptor = klass.__dict__["constrainedName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::invariant_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Invariant)


def test_backtrackingcontentassisttest::invariant_constructor_exists():
    assert callable(backtrackingContentAssistTest::Invariant.__init__)


def test_backtrackingcontentassisttest::invariant_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Invariant.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest::invariant_has_constraintName():
    assert hasattr(backtrackingContentAssistTest::Invariant, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Invariant.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::classifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::ClassifierRef)


def test_backtrackingcontentassisttest::classifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest::ClassifierRef.__init__)


def test_backtrackingcontentassisttest::classifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_contextdecl_is_not_abstract():
    assert not inspect.isabstract(ContextDecl)


def test_contextdecl_constructor_exists():
    assert callable(ContextDecl.__init__)


def test_contextdecl_constructor_args():
    sig = inspect.signature(ContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::classifiercontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::ClassifierContextDecl)


def test_backtrackingcontentassisttest::classifiercontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest::ClassifierContextDecl.__init__)


def test_backtrackingcontentassisttest::classifiercontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::ClassifierContextDecl.__init__)
    params = list(sig.parameters.keys())
    assert "selfName" in params, "Missing parameter 'selfName'"

def test_backtrackingcontentassisttest::classifiercontextdecl_has_selfName():
    assert hasattr(backtrackingContentAssistTest::ClassifierContextDecl, "selfName")
    descriptor = None
    for klass in backtrackingContentAssistTest::ClassifierContextDecl.__mro__:
        if "selfName" in klass.__dict__:
            descriptor = klass.__dict__["selfName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::propertycontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PropertyContextDecl)


def test_backtrackingcontentassisttest::propertycontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest::PropertyContextDecl.__init__)


def test_backtrackingcontentassisttest::propertycontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PropertyContextDecl.__init__)
    params = list(sig.parameters.keys())



def test_nameexp_is_not_abstract():
    assert not inspect.isabstract(NameExp)


def test_nameexp_constructor_exists():
    assert callable(NameExp.__init__)


def test_nameexp_constructor_args():
    sig = inspect.signature(NameExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::simplenameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SimpleNameExp)


def test_backtrackingcontentassisttest::simplenameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::SimpleNameExp.__init__)


def test_backtrackingcontentassisttest::simplenameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SimpleNameExp.__init__)
    params = list(sig.parameters.keys())
    assert "element" in params, "Missing parameter 'element'"

def test_backtrackingcontentassisttest::simplenameexp_has_element():
    assert hasattr(backtrackingContentAssistTest::SimpleNameExp, "element")
    descriptor = None
    for klass in backtrackingContentAssistTest::SimpleNameExp.__mro__:
        if "element" in klass.__dict__:
            descriptor = klass.__dict__["element"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::pathnameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PathNameExp)


def test_backtrackingcontentassisttest::pathnameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::PathNameExp.__init__)


def test_backtrackingcontentassisttest::pathnameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PathNameExp.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest::pathnameexp_has_namespace():
    assert hasattr(backtrackingContentAssistTest::PathNameExp, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest::PathNameExp.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::letvariable_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::LetVariable)


def test_backtrackingcontentassisttest::letvariable_constructor_exists():
    assert callable(backtrackingContentAssistTest::LetVariable.__init__)


def test_backtrackingcontentassisttest::letvariable_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::LetVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::letvariable_has_name():
    assert hasattr(backtrackingContentAssistTest::LetVariable, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::LetVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::iteratoraccumulator_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::iteratorAccumulator)


def test_backtrackingcontentassisttest::iteratoraccumulator_constructor_exists():
    assert callable(backtrackingContentAssistTest::iteratorAccumulator.__init__)


def test_backtrackingcontentassisttest::iteratoraccumulator_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::iteratorAccumulator.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::iteratoraccumulator_has_name():
    assert hasattr(backtrackingContentAssistTest::iteratorAccumulator, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::iteratorAccumulator.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::iteratorvariable_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::iteratorVariable)


def test_backtrackingcontentassisttest::iteratorvariable_constructor_exists():
    assert callable(backtrackingContentAssistTest::iteratorVariable.__init__)


def test_backtrackingcontentassisttest::iteratorvariable_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::iteratorVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::iteratorvariable_has_name():
    assert hasattr(backtrackingContentAssistTest::iteratorVariable, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::iteratorVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::NullLiteralExp)


def test_backtrackingcontentassisttest::nullliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::NullLiteralExp.__init__)


def test_backtrackingcontentassisttest::nullliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::BooleanLiteralExp)


def test_backtrackingcontentassisttest::booleanliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::BooleanLiteralExp.__init__)


def test_backtrackingcontentassisttest::booleanliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_backtrackingcontentassisttest::booleanliteralexp_has_isTrue():
    assert hasattr(backtrackingContentAssistTest::BooleanLiteralExp, "isTrue")
    descriptor = None
    for klass in backtrackingContentAssistTest::BooleanLiteralExp.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::InvalidLiteralExp)


def test_backtrackingcontentassisttest::invalidliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::InvalidLiteralExp.__init__)


def test_backtrackingcontentassisttest::invalidliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::StringLiteralExp)


def test_backtrackingcontentassisttest::stringliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::StringLiteralExp.__init__)


def test_backtrackingcontentassisttest::stringliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_backtrackingcontentassisttest::stringliteralexp_has_values():
    assert hasattr(backtrackingContentAssistTest::StringLiteralExp, "values")
    descriptor = None
    for klass in backtrackingContentAssistTest::StringLiteralExp.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::numberliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::NumberLiteralExp)


def test_backtrackingcontentassisttest::numberliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::NumberLiteralExp.__init__)


def test_backtrackingcontentassisttest::numberliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::NumberLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::numberliteralexp_has_name():
    assert hasattr(backtrackingContentAssistTest::NumberLiteralExp, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::NumberLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::eobject_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::EObject)


def test_backtrackingcontentassisttest::eobject_constructor_exists():
    assert callable(backtrackingContentAssistTest::EObject.__init__)


def test_backtrackingcontentassisttest::eobject_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::EObject.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::CollectionLiteralPart)


def test_backtrackingcontentassisttest::collectionliteralpart_constructor_exists():
    assert callable(backtrackingContentAssistTest::CollectionLiteralPart.__init__)


def test_backtrackingcontentassisttest::collectionliteralpart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::tuplepart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::tuplePart)


def test_backtrackingcontentassisttest::tuplepart_constructor_exists():
    assert callable(backtrackingContentAssistTest::tuplePart.__init__)


def test_backtrackingcontentassisttest::tuplepart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::tuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::tuplepart_has_name():
    assert hasattr(backtrackingContentAssistTest::tuplePart, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::tuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::nestedexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::NestedExp)


def test_backtrackingcontentassisttest::nestedexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::NestedExp.__init__)


def test_backtrackingcontentassisttest::nestedexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::NestedExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::letexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::LetExp)


def test_backtrackingcontentassisttest::letexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::LetExp.__init__)


def test_backtrackingcontentassisttest::letexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::preexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PreExp)


def test_backtrackingcontentassisttest::preexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::PreExp.__init__)


def test_backtrackingcontentassisttest::preexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PreExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::typeexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::TypeExp)


def test_backtrackingcontentassisttest::typeexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::TypeExp.__init__)


def test_backtrackingcontentassisttest::typeexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::oclmessage_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::OclMessage)


def test_backtrackingcontentassisttest::oclmessage_constructor_exists():
    assert callable(backtrackingContentAssistTest::OclMessage.__init__)


def test_backtrackingcontentassisttest::oclmessage_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::OclMessage.__init__)
    params = list(sig.parameters.keys())
    assert "messageName" in params, "Missing parameter 'messageName'"
    assert "op" in params, "Missing parameter 'op'"

def test_backtrackingcontentassisttest::oclmessage_has_messageName():
    assert hasattr(backtrackingContentAssistTest::OclMessage, "messageName")
    descriptor = None
    for klass in backtrackingContentAssistTest::OclMessage.__mro__:
        if "messageName" in klass.__dict__:
            descriptor = klass.__dict__["messageName"]
            break
    assert isinstance(descriptor, property)

def test_backtrackingcontentassisttest::oclmessage_has_op():
    assert hasattr(backtrackingContentAssistTest::OclMessage, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest::OclMessage.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::CollectionLiteralExp)


def test_backtrackingcontentassisttest::collectionliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::CollectionLiteralExp.__init__)


def test_backtrackingcontentassisttest::collectionliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::infixexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::InfixExp)


def test_backtrackingcontentassisttest::infixexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::InfixExp.__init__)


def test_backtrackingcontentassisttest::infixexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::InfixExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_backtrackingcontentassisttest::infixexp_has_op():
    assert hasattr(backtrackingContentAssistTest::InfixExp, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest::InfixExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::ifexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::IfExp)


def test_backtrackingcontentassisttest::ifexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::IfExp.__init__)


def test_backtrackingcontentassisttest::ifexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::selfexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SelfExp)


def test_backtrackingcontentassisttest::selfexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::SelfExp.__init__)


def test_backtrackingcontentassisttest::selfexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SelfExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::squarebracketexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SquareBracketExp)


def test_backtrackingcontentassisttest::squarebracketexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::SquareBracketExp.__init__)


def test_backtrackingcontentassisttest::squarebracketexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SquareBracketExp.__init__)
    params = list(sig.parameters.keys())
    assert "pre" in params, "Missing parameter 'pre'"

def test_backtrackingcontentassisttest::squarebracketexp_has_pre():
    assert hasattr(backtrackingContentAssistTest::SquareBracketExp, "pre")
    descriptor = None
    for klass in backtrackingContentAssistTest::SquareBracketExp.__mro__:
        if "pre" in klass.__dict__:
            descriptor = klass.__dict__["pre"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::prefixexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PrefixExp)


def test_backtrackingcontentassisttest::prefixexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::PrefixExp.__init__)


def test_backtrackingcontentassisttest::prefixexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PrefixExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_backtrackingcontentassisttest::prefixexp_has_op():
    assert hasattr(backtrackingContentAssistTest::PrefixExp, "op")
    descriptor = None
    for klass in backtrackingContentAssistTest::PrefixExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::roundbracketexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::RoundBracketExp)


def test_backtrackingcontentassisttest::roundbracketexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::RoundBracketExp.__init__)


def test_backtrackingcontentassisttest::roundbracketexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::RoundBracketExp.__init__)
    params = list(sig.parameters.keys())
    assert "pre" in params, "Missing parameter 'pre'"

def test_backtrackingcontentassisttest::roundbracketexp_has_pre():
    assert hasattr(backtrackingContentAssistTest::RoundBracketExp, "pre")
    descriptor = None
    for klass in backtrackingContentAssistTest::RoundBracketExp.__mro__:
        if "pre" in klass.__dict__:
            descriptor = klass.__dict__["pre"]
            break
    assert isinstance(descriptor, property)



def test_typeexp_is_not_abstract():
    assert not inspect.isabstract(TypeExp)


def test_typeexp_constructor_exists():
    assert callable(TypeExp.__init__)


def test_typeexp_constructor_args():
    sig = inspect.signature(TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::tupletype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::TupleType)


def test_backtrackingcontentassisttest::tupletype_constructor_exists():
    assert callable(backtrackingContentAssistTest::TupleType.__init__)


def test_backtrackingcontentassisttest::tupletype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::TupleType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::tupletype_has_name():
    assert hasattr(backtrackingContentAssistTest::TupleType, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::TupleType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::collectiontype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::CollectionType)


def test_backtrackingcontentassisttest::collectiontype_constructor_exists():
    assert callable(backtrackingContentAssistTest::CollectionType.__init__)


def test_backtrackingcontentassisttest::collectiontype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "typeIdentifier" in params, "Missing parameter 'typeIdentifier'"

def test_backtrackingcontentassisttest::collectiontype_has_typeIdentifier():
    assert hasattr(backtrackingContentAssistTest::CollectionType, "typeIdentifier")
    descriptor = None
    for klass in backtrackingContentAssistTest::CollectionType.__mro__:
        if "typeIdentifier" in klass.__dict__:
            descriptor = klass.__dict__["typeIdentifier"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::nameexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::NameExp)


def test_backtrackingcontentassisttest::nameexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::NameExp.__init__)


def test_backtrackingcontentassisttest::nameexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::NameExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::primitivetype_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PrimitiveType)


def test_backtrackingcontentassisttest::primitivetype_constructor_exists():
    assert callable(backtrackingContentAssistTest::PrimitiveType.__init__)


def test_backtrackingcontentassisttest::primitivetype_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::primitivetype_has_name():
    assert hasattr(backtrackingContentAssistTest::PrimitiveType, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::PrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::TupleLiteralPart)


def test_backtrackingcontentassisttest::tupleliteralpart_constructor_exists():
    assert callable(backtrackingContentAssistTest::TupleLiteralPart.__init__)


def test_backtrackingcontentassisttest::tupleliteralpart_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_backtrackingcontentassisttest::tupleliteralpart_has_name():
    assert hasattr(backtrackingContentAssistTest::TupleLiteralPart, "name")
    descriptor = None
    for klass in backtrackingContentAssistTest::TupleLiteralPart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::TupleLiteralExp)


def test_backtrackingcontentassisttest::tupleliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::TupleLiteralExp.__init__)


def test_backtrackingcontentassisttest::tupleliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PrimitiveLiteralExp)


def test_backtrackingcontentassisttest::primitiveliteralexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::PrimitiveLiteralExp.__init__)


def test_backtrackingcontentassisttest::primitiveliteralexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_propertyref_is_not_abstract():
    assert not inspect.isabstract(PropertyRef)


def test_propertyref_constructor_exists():
    assert callable(PropertyRef.__init__)


def test_propertyref_constructor_args():
    sig = inspect.signature(PropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::qualifiedpropertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::QualifiedPropertyRef)


def test_backtrackingcontentassisttest::qualifiedpropertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest::QualifiedPropertyRef.__init__)


def test_backtrackingcontentassisttest::qualifiedpropertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::QualifiedPropertyRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest::qualifiedpropertyref_has_namespace():
    assert hasattr(backtrackingContentAssistTest::QualifiedPropertyRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest::QualifiedPropertyRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_operationref_is_not_abstract():
    assert not inspect.isabstract(OperationRef)


def test_operationref_constructor_exists():
    assert callable(OperationRef.__init__)


def test_operationref_constructor_args():
    sig = inspect.signature(OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::qualifiedoperationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::QualifiedOperationRef)


def test_backtrackingcontentassisttest::qualifiedoperationref_constructor_exists():
    assert callable(backtrackingContentAssistTest::QualifiedOperationRef.__init__)


def test_backtrackingcontentassisttest::qualifiedoperationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::QualifiedOperationRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest::qualifiedoperationref_has_namespace():
    assert hasattr(backtrackingContentAssistTest::QualifiedOperationRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest::QualifiedOperationRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_classifierref_is_not_abstract():
    assert not inspect.isabstract(ClassifierRef)


def test_classifierref_constructor_exists():
    assert callable(ClassifierRef.__init__)


def test_classifierref_constructor_args():
    sig = inspect.signature(ClassifierRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::qualifiedclassifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::QualifiedClassifierRef)


def test_backtrackingcontentassisttest::qualifiedclassifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest::QualifiedClassifierRef.__init__)


def test_backtrackingcontentassisttest::qualifiedclassifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::QualifiedClassifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest::qualifiedclassifierref_has_namespace():
    assert hasattr(backtrackingContentAssistTest::QualifiedClassifierRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest::QualifiedClassifierRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::propertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::PropertyRef)


def test_backtrackingcontentassisttest::propertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest::PropertyRef.__init__)


def test_backtrackingcontentassisttest::propertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::PropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::oclmessagearg_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::OclMessageArg)


def test_backtrackingcontentassisttest::oclmessagearg_constructor_exists():
    assert callable(backtrackingContentAssistTest::OclMessageArg.__init__)


def test_backtrackingcontentassisttest::oclmessagearg_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::OclMessageArg.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::navigatingexp_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::NavigatingExp)


def test_backtrackingcontentassisttest::navigatingexp_constructor_exists():
    assert callable(backtrackingContentAssistTest::NavigatingExp.__init__)


def test_backtrackingcontentassisttest::navigatingexp_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::NavigatingExp.__init__)
    params = list(sig.parameters.keys())



def test_oclmessagearg_is_not_abstract():
    assert not inspect.isabstract(OclMessageArg)


def test_oclmessagearg_constructor_exists():
    assert callable(OclMessageArg.__init__)


def test_oclmessagearg_constructor_args():
    sig = inspect.signature(OclMessageArg.__init__)
    params = list(sig.parameters.keys())



def test_navigatingexp_is_not_abstract():
    assert not inspect.isabstract(NavigatingExp)


def test_navigatingexp_constructor_exists():
    assert callable(NavigatingExp.__init__)


def test_navigatingexp_constructor_args():
    sig = inspect.signature(NavigatingExp.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::expression_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Expression)


def test_backtrackingcontentassisttest::expression_constructor_exists():
    assert callable(backtrackingContentAssistTest::Expression.__init__)


def test_backtrackingcontentassisttest::expression_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Expression.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::simplepropertyref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SimplePropertyRef)


def test_backtrackingcontentassisttest::simplepropertyref_constructor_exists():
    assert callable(backtrackingContentAssistTest::SimplePropertyRef.__init__)


def test_backtrackingcontentassisttest::simplepropertyref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SimplePropertyRef.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"

def test_backtrackingcontentassisttest::simplepropertyref_has_feature():
    assert hasattr(backtrackingContentAssistTest::SimplePropertyRef, "feature")
    descriptor = None
    for klass in backtrackingContentAssistTest::SimplePropertyRef.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::simpleoperationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SimpleOperationRef)


def test_backtrackingcontentassisttest::simpleoperationref_constructor_exists():
    assert callable(backtrackingContentAssistTest::SimpleOperationRef.__init__)


def test_backtrackingcontentassisttest::simpleoperationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SimpleOperationRef.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_backtrackingcontentassisttest::simpleoperationref_has_operation():
    assert hasattr(backtrackingContentAssistTest::SimpleOperationRef, "operation")
    descriptor = None
    for klass in backtrackingContentAssistTest::SimpleOperationRef.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::simpleclassifierref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SimpleClassifierRef)


def test_backtrackingcontentassisttest::simpleclassifierref_constructor_exists():
    assert callable(backtrackingContentAssistTest::SimpleClassifierRef.__init__)


def test_backtrackingcontentassisttest::simpleclassifierref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SimpleClassifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_backtrackingcontentassisttest::simpleclassifierref_has_classifier():
    assert hasattr(backtrackingContentAssistTest::SimpleClassifierRef, "classifier")
    descriptor = None
    for klass in backtrackingContentAssistTest::SimpleClassifierRef.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_packageref_is_not_abstract():
    assert not inspect.isabstract(PackageRef)


def test_packageref_constructor_exists():
    assert callable(PackageRef.__init__)


def test_packageref_constructor_args():
    sig = inspect.signature(PackageRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::simplepackageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::SimplePackageRef)


def test_backtrackingcontentassisttest::simplepackageref_constructor_exists():
    assert callable(backtrackingContentAssistTest::SimplePackageRef.__init__)


def test_backtrackingcontentassisttest::simplepackageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::SimplePackageRef.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_backtrackingcontentassisttest::simplepackageref_has_package():
    assert hasattr(backtrackingContentAssistTest::SimplePackageRef, "package")
    descriptor = None
    for klass in backtrackingContentAssistTest::SimplePackageRef.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::qualifiedpackageref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::QualifiedPackageRef)


def test_backtrackingcontentassisttest::qualifiedpackageref_constructor_exists():
    assert callable(backtrackingContentAssistTest::QualifiedPackageRef.__init__)


def test_backtrackingcontentassisttest::qualifiedpackageref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::QualifiedPackageRef.__init__)
    params = list(sig.parameters.keys())
    assert "namespace" in params, "Missing parameter 'namespace'"

def test_backtrackingcontentassisttest::qualifiedpackageref_has_namespace():
    assert hasattr(backtrackingContentAssistTest::QualifiedPackageRef, "namespace")
    descriptor = None
    for klass in backtrackingContentAssistTest::QualifiedPackageRef.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::pre_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::Pre)


def test_backtrackingcontentassisttest::pre_constructor_exists():
    assert callable(backtrackingContentAssistTest::Pre.__init__)


def test_backtrackingcontentassisttest::pre_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::Pre.__init__)
    params = list(sig.parameters.keys())
    assert "constraintName" in params, "Missing parameter 'constraintName'"

def test_backtrackingcontentassisttest::pre_has_constraintName():
    assert hasattr(backtrackingContentAssistTest::Pre, "constraintName")
    descriptor = None
    for klass in backtrackingContentAssistTest::Pre.__mro__:
        if "constraintName" in klass.__dict__:
            descriptor = klass.__dict__["constraintName"]
            break
    assert isinstance(descriptor, property)



def test_backtrackingcontentassisttest::operationref_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::OperationRef)


def test_backtrackingcontentassisttest::operationref_constructor_exists():
    assert callable(backtrackingContentAssistTest::OperationRef.__init__)


def test_backtrackingcontentassisttest::operationref_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::OperationRef.__init__)
    params = list(sig.parameters.keys())



def test_backtrackingcontentassisttest::operationcontextdecl_is_not_abstract():
    assert not inspect.isabstract(backtrackingContentAssistTest::OperationContextDecl)


def test_backtrackingcontentassisttest::operationcontextdecl_constructor_exists():
    assert callable(backtrackingContentAssistTest::OperationContextDecl.__init__)


def test_backtrackingcontentassisttest::operationcontextdecl_constructor_args():
    sig = inspect.signature(backtrackingContentAssistTest::OperationContextDecl.__init__)
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
backtrackingContentAssistTest::Init_strategy = st.builds(
    backtrackingContentAssistTest::Init,
)
backtrackingContentAssistTest::PackageRef_strategy = st.builds(
    backtrackingContentAssistTest::PackageRef,
)
backtrackingContentAssistTest::Post_strategy = st.builds(
    backtrackingContentAssistTest::Post,
    constraintName=
        safe_text
)
backtrackingContentAssistTest::Body_strategy = st.builds(
    backtrackingContentAssistTest::Body,
    constraintName=
        safe_text
)
backtrackingContentAssistTest::ContextDecl_strategy = st.builds(
    backtrackingContentAssistTest::ContextDecl,
)
backtrackingContentAssistTest::PackageDeclaration_strategy = st.builds(
    backtrackingContentAssistTest::PackageDeclaration,
)
backtrackingContentAssistTest::Document_strategy = st.builds(
    backtrackingContentAssistTest::Document,
)
backtrackingContentAssistTest::Der_strategy = st.builds(
    backtrackingContentAssistTest::Der,
)
backtrackingContentAssistTest::Parameter_strategy = st.builds(
    backtrackingContentAssistTest::Parameter,
    name=
        safe_text
)
backtrackingContentAssistTest::Definition_strategy = st.builds(
    backtrackingContentAssistTest::Definition,
    static=
        st.booleans(),
    constraintName=
        safe_text,
    constrainedName=
        safe_text
)
backtrackingContentAssistTest::Invariant_strategy = st.builds(
    backtrackingContentAssistTest::Invariant,
    constraintName=
        safe_text
)
backtrackingContentAssistTest::ClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest::ClassifierRef,
)
ContextDecl_strategy = st.builds(
    ContextDecl,
)
backtrackingContentAssistTest::ClassifierContextDecl_strategy = st.builds(
    backtrackingContentAssistTest::ClassifierContextDecl,
    selfName=
        safe_text
)
backtrackingContentAssistTest::PropertyContextDecl_strategy = st.builds(
    backtrackingContentAssistTest::PropertyContextDecl,
)
NameExp_strategy = st.builds(
    NameExp,
)
backtrackingContentAssistTest::SimpleNameExp_strategy = st.builds(
    backtrackingContentAssistTest::SimpleNameExp,
    element=
        safe_text
)
backtrackingContentAssistTest::PathNameExp_strategy = st.builds(
    backtrackingContentAssistTest::PathNameExp,
    namespace=
        safe_text
)
backtrackingContentAssistTest::LetVariable_strategy = st.builds(
    backtrackingContentAssistTest::LetVariable,
    name=
        safe_text
)
backtrackingContentAssistTest::iteratorAccumulator_strategy = st.builds(
    backtrackingContentAssistTest::iteratorAccumulator,
    name=
        safe_text
)
backtrackingContentAssistTest::iteratorVariable_strategy = st.builds(
    backtrackingContentAssistTest::iteratorVariable,
    name=
        safe_text
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
backtrackingContentAssistTest::NullLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::NullLiteralExp,
)
backtrackingContentAssistTest::BooleanLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::BooleanLiteralExp,
    isTrue=
        st.booleans()
)
backtrackingContentAssistTest::InvalidLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::InvalidLiteralExp,
)
backtrackingContentAssistTest::StringLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::StringLiteralExp,
    values=
        safe_text
)
backtrackingContentAssistTest::NumberLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::NumberLiteralExp,
    name=
        safe_text
)
backtrackingContentAssistTest::EObject_strategy = st.builds(
    backtrackingContentAssistTest::EObject,
)
backtrackingContentAssistTest::CollectionLiteralPart_strategy = st.builds(
    backtrackingContentAssistTest::CollectionLiteralPart,
)
backtrackingContentAssistTest::tuplePart_strategy = st.builds(
    backtrackingContentAssistTest::tuplePart,
    name=
        safe_text
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
Expression_strategy = st.builds(
    Expression,
)
backtrackingContentAssistTest::NestedExp_strategy = st.builds(
    backtrackingContentAssistTest::NestedExp,
)
backtrackingContentAssistTest::LetExp_strategy = st.builds(
    backtrackingContentAssistTest::LetExp,
)
backtrackingContentAssistTest::PreExp_strategy = st.builds(
    backtrackingContentAssistTest::PreExp,
)
backtrackingContentAssistTest::TypeExp_strategy = st.builds(
    backtrackingContentAssistTest::TypeExp,
)
backtrackingContentAssistTest::OclMessage_strategy = st.builds(
    backtrackingContentAssistTest::OclMessage,
    messageName=
        safe_text,
    op=
        safe_text
)
backtrackingContentAssistTest::CollectionLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::CollectionLiteralExp,
)
backtrackingContentAssistTest::InfixExp_strategy = st.builds(
    backtrackingContentAssistTest::InfixExp,
    op=
        safe_text
)
backtrackingContentAssistTest::IfExp_strategy = st.builds(
    backtrackingContentAssistTest::IfExp,
)
backtrackingContentAssistTest::SelfExp_strategy = st.builds(
    backtrackingContentAssistTest::SelfExp,
)
backtrackingContentAssistTest::SquareBracketExp_strategy = st.builds(
    backtrackingContentAssistTest::SquareBracketExp,
    pre=
        st.booleans()
)
backtrackingContentAssistTest::PrefixExp_strategy = st.builds(
    backtrackingContentAssistTest::PrefixExp,
    op=
        safe_text
)
backtrackingContentAssistTest::RoundBracketExp_strategy = st.builds(
    backtrackingContentAssistTest::RoundBracketExp,
    pre=
        st.booleans()
)
TypeExp_strategy = st.builds(
    TypeExp,
)
backtrackingContentAssistTest::TupleType_strategy = st.builds(
    backtrackingContentAssistTest::TupleType,
    name=
        safe_text
)
backtrackingContentAssistTest::CollectionType_strategy = st.builds(
    backtrackingContentAssistTest::CollectionType,
    typeIdentifier=
        safe_text
)
backtrackingContentAssistTest::NameExp_strategy = st.builds(
    backtrackingContentAssistTest::NameExp,
)
backtrackingContentAssistTest::PrimitiveType_strategy = st.builds(
    backtrackingContentAssistTest::PrimitiveType,
    name=
        safe_text
)
backtrackingContentAssistTest::TupleLiteralPart_strategy = st.builds(
    backtrackingContentAssistTest::TupleLiteralPart,
    name=
        safe_text
)
backtrackingContentAssistTest::TupleLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::TupleLiteralExp,
)
backtrackingContentAssistTest::PrimitiveLiteralExp_strategy = st.builds(
    backtrackingContentAssistTest::PrimitiveLiteralExp,
)
PropertyRef_strategy = st.builds(
    PropertyRef,
)
backtrackingContentAssistTest::QualifiedPropertyRef_strategy = st.builds(
    backtrackingContentAssistTest::QualifiedPropertyRef,
    namespace=
        safe_text
)
OperationRef_strategy = st.builds(
    OperationRef,
)
backtrackingContentAssistTest::QualifiedOperationRef_strategy = st.builds(
    backtrackingContentAssistTest::QualifiedOperationRef,
    namespace=
        safe_text
)
ClassifierRef_strategy = st.builds(
    ClassifierRef,
)
backtrackingContentAssistTest::QualifiedClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest::QualifiedClassifierRef,
    namespace=
        safe_text
)
backtrackingContentAssistTest::PropertyRef_strategy = st.builds(
    backtrackingContentAssistTest::PropertyRef,
)
backtrackingContentAssistTest::OclMessageArg_strategy = st.builds(
    backtrackingContentAssistTest::OclMessageArg,
)
backtrackingContentAssistTest::NavigatingExp_strategy = st.builds(
    backtrackingContentAssistTest::NavigatingExp,
)
OclMessageArg_strategy = st.builds(
    OclMessageArg,
)
NavigatingExp_strategy = st.builds(
    NavigatingExp,
)
backtrackingContentAssistTest::Expression_strategy = st.builds(
    backtrackingContentAssistTest::Expression,
)
backtrackingContentAssistTest::SimplePropertyRef_strategy = st.builds(
    backtrackingContentAssistTest::SimplePropertyRef,
    feature=
        safe_text
)
backtrackingContentAssistTest::SimpleOperationRef_strategy = st.builds(
    backtrackingContentAssistTest::SimpleOperationRef,
    operation=
        safe_text
)
backtrackingContentAssistTest::SimpleClassifierRef_strategy = st.builds(
    backtrackingContentAssistTest::SimpleClassifierRef,
    classifier=
        safe_text
)
PackageRef_strategy = st.builds(
    PackageRef,
)
backtrackingContentAssistTest::SimplePackageRef_strategy = st.builds(
    backtrackingContentAssistTest::SimplePackageRef,
    package=
        safe_text
)
backtrackingContentAssistTest::QualifiedPackageRef_strategy = st.builds(
    backtrackingContentAssistTest::QualifiedPackageRef,
    namespace=
        safe_text
)
backtrackingContentAssistTest::Pre_strategy = st.builds(
    backtrackingContentAssistTest::Pre,
    constraintName=
        safe_text
)
backtrackingContentAssistTest::OperationRef_strategy = st.builds(
    backtrackingContentAssistTest::OperationRef,
)
backtrackingContentAssistTest::OperationContextDecl_strategy = st.builds(
    backtrackingContentAssistTest::OperationContextDecl,
)

@given(instance=backtrackingContentAssistTest::Init_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::init_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Init)

@given(instance=backtrackingContentAssistTest::PackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::packageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PackageRef)

@given(instance=backtrackingContentAssistTest::Post_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::post_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Post)

@given(instance=backtrackingContentAssistTest::Post_strategy)
def test_backtrackingcontentassisttest::post_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=backtrackingContentAssistTest::Post_strategy)
def test_backtrackingcontentassisttest::post_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest::Body_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::body_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Body)

@given(instance=backtrackingContentAssistTest::Body_strategy)
def test_backtrackingcontentassisttest::body_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=backtrackingContentAssistTest::Body_strategy)
def test_backtrackingcontentassisttest::body_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest::ContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::contextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::ContextDecl)

@given(instance=backtrackingContentAssistTest::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::packagedeclaration_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PackageDeclaration)

@given(instance=backtrackingContentAssistTest::Document_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::document_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Document)

@given(instance=backtrackingContentAssistTest::Der_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::der_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Der)

@given(instance=backtrackingContentAssistTest::Parameter_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::parameter_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Parameter)

@given(instance=backtrackingContentAssistTest::Parameter_strategy)
def test_backtrackingcontentassisttest::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::Parameter_strategy)
def test_backtrackingcontentassisttest::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::Definition_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::definition_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Definition)

@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_constrainedName_type(instance):
    assert isinstance(instance.constrainedName, str)


@given(instance=backtrackingContentAssistTest::Definition_strategy)
def test_backtrackingcontentassisttest::definition_constrainedName_setter(instance):
    original = instance.constrainedName
    instance.constrainedName = original
    assert instance.constrainedName == original

@given(instance=backtrackingContentAssistTest::Invariant_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::invariant_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Invariant)

@given(instance=backtrackingContentAssistTest::Invariant_strategy)
def test_backtrackingcontentassisttest::invariant_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=backtrackingContentAssistTest::Invariant_strategy)
def test_backtrackingcontentassisttest::invariant_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest::ClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::classifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::ClassifierRef)

@given(instance=ContextDecl_strategy)
@settings(max_examples=50)
def test_contextdecl_instantiation(instance):
    assert isinstance(instance, ContextDecl)

@given(instance=backtrackingContentAssistTest::ClassifierContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::classifiercontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::ClassifierContextDecl)

@given(instance=backtrackingContentAssistTest::ClassifierContextDecl_strategy)
def test_backtrackingcontentassisttest::classifiercontextdecl_selfName_type(instance):
    assert isinstance(instance.selfName, str)


@given(instance=backtrackingContentAssistTest::ClassifierContextDecl_strategy)
def test_backtrackingcontentassisttest::classifiercontextdecl_selfName_setter(instance):
    original = instance.selfName
    instance.selfName = original
    assert instance.selfName == original

@given(instance=backtrackingContentAssistTest::PropertyContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::propertycontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PropertyContextDecl)

@given(instance=NameExp_strategy)
@settings(max_examples=50)
def test_nameexp_instantiation(instance):
    assert isinstance(instance, NameExp)

@given(instance=backtrackingContentAssistTest::SimpleNameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::simplenameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SimpleNameExp)

@given(instance=backtrackingContentAssistTest::SimpleNameExp_strategy)
def test_backtrackingcontentassisttest::simplenameexp_element_type(instance):
    assert isinstance(instance.element, str)


@given(instance=backtrackingContentAssistTest::SimpleNameExp_strategy)
def test_backtrackingcontentassisttest::simplenameexp_element_setter(instance):
    original = instance.element
    instance.element = original
    assert instance.element == original

@given(instance=backtrackingContentAssistTest::PathNameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::pathnameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PathNameExp)

@given(instance=backtrackingContentAssistTest::PathNameExp_strategy)
def test_backtrackingcontentassisttest::pathnameexp_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=backtrackingContentAssistTest::PathNameExp_strategy)
def test_backtrackingcontentassisttest::pathnameexp_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest::LetVariable_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::letvariable_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::LetVariable)

@given(instance=backtrackingContentAssistTest::LetVariable_strategy)
def test_backtrackingcontentassisttest::letvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::LetVariable_strategy)
def test_backtrackingcontentassisttest::letvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::iteratorAccumulator_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::iteratoraccumulator_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::iteratorAccumulator)

@given(instance=backtrackingContentAssistTest::iteratorAccumulator_strategy)
def test_backtrackingcontentassisttest::iteratoraccumulator_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::iteratorAccumulator_strategy)
def test_backtrackingcontentassisttest::iteratoraccumulator_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::iteratorVariable_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::iteratorvariable_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::iteratorVariable)

@given(instance=backtrackingContentAssistTest::iteratorVariable_strategy)
def test_backtrackingcontentassisttest::iteratorvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::iteratorVariable_strategy)
def test_backtrackingcontentassisttest::iteratorvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=backtrackingContentAssistTest::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::nullliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::NullLiteralExp)

@given(instance=backtrackingContentAssistTest::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::BooleanLiteralExp)

@given(instance=backtrackingContentAssistTest::BooleanLiteralExp_strategy)
def test_backtrackingcontentassisttest::booleanliteralexp_isTrue_type(instance):
    assert isinstance(instance.isTrue, bool)


@given(instance=backtrackingContentAssistTest::BooleanLiteralExp_strategy)
def test_backtrackingcontentassisttest::booleanliteralexp_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=backtrackingContentAssistTest::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::InvalidLiteralExp)

@given(instance=backtrackingContentAssistTest::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::stringliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::StringLiteralExp)

@given(instance=backtrackingContentAssistTest::StringLiteralExp_strategy)
def test_backtrackingcontentassisttest::stringliteralexp_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=backtrackingContentAssistTest::StringLiteralExp_strategy)
def test_backtrackingcontentassisttest::stringliteralexp_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=backtrackingContentAssistTest::NumberLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::numberliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::NumberLiteralExp)

@given(instance=backtrackingContentAssistTest::NumberLiteralExp_strategy)
def test_backtrackingcontentassisttest::numberliteralexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::NumberLiteralExp_strategy)
def test_backtrackingcontentassisttest::numberliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::EObject_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::eobject_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::EObject)

@given(instance=backtrackingContentAssistTest::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::CollectionLiteralPart)

@given(instance=backtrackingContentAssistTest::tuplePart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::tuplepart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::tuplePart)

@given(instance=backtrackingContentAssistTest::tuplePart_strategy)
def test_backtrackingcontentassisttest::tuplepart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::tuplePart_strategy)
def test_backtrackingcontentassisttest::tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=backtrackingContentAssistTest::NestedExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::nestedexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::NestedExp)

@given(instance=backtrackingContentAssistTest::LetExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::letexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::LetExp)

@given(instance=backtrackingContentAssistTest::PreExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::preexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PreExp)

@given(instance=backtrackingContentAssistTest::TypeExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::typeexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::TypeExp)

@given(instance=backtrackingContentAssistTest::OclMessage_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::oclmessage_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::OclMessage)

@given(instance=backtrackingContentAssistTest::OclMessage_strategy)
def test_backtrackingcontentassisttest::oclmessage_messageName_type(instance):
    assert isinstance(instance.messageName, str)


@given(instance=backtrackingContentAssistTest::OclMessage_strategy)
def test_backtrackingcontentassisttest::oclmessage_messageName_setter(instance):
    original = instance.messageName
    instance.messageName = original
    assert instance.messageName == original

@given(instance=backtrackingContentAssistTest::OclMessage_strategy)
def test_backtrackingcontentassisttest::oclmessage_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=backtrackingContentAssistTest::OclMessage_strategy)
def test_backtrackingcontentassisttest::oclmessage_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=backtrackingContentAssistTest::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::CollectionLiteralExp)

@given(instance=backtrackingContentAssistTest::InfixExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::infixexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::InfixExp)

@given(instance=backtrackingContentAssistTest::InfixExp_strategy)
def test_backtrackingcontentassisttest::infixexp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=backtrackingContentAssistTest::InfixExp_strategy)
def test_backtrackingcontentassisttest::infixexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=backtrackingContentAssistTest::IfExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::ifexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::IfExp)

@given(instance=backtrackingContentAssistTest::SelfExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::selfexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SelfExp)

@given(instance=backtrackingContentAssistTest::SquareBracketExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::squarebracketexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SquareBracketExp)

@given(instance=backtrackingContentAssistTest::SquareBracketExp_strategy)
def test_backtrackingcontentassisttest::squarebracketexp_pre_type(instance):
    assert isinstance(instance.pre, bool)


@given(instance=backtrackingContentAssistTest::SquareBracketExp_strategy)
def test_backtrackingcontentassisttest::squarebracketexp_pre_setter(instance):
    original = instance.pre
    instance.pre = original
    assert instance.pre == original

@given(instance=backtrackingContentAssistTest::PrefixExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::prefixexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PrefixExp)

@given(instance=backtrackingContentAssistTest::PrefixExp_strategy)
def test_backtrackingcontentassisttest::prefixexp_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=backtrackingContentAssistTest::PrefixExp_strategy)
def test_backtrackingcontentassisttest::prefixexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=backtrackingContentAssistTest::RoundBracketExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::roundbracketexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::RoundBracketExp)

@given(instance=backtrackingContentAssistTest::RoundBracketExp_strategy)
def test_backtrackingcontentassisttest::roundbracketexp_pre_type(instance):
    assert isinstance(instance.pre, bool)


@given(instance=backtrackingContentAssistTest::RoundBracketExp_strategy)
def test_backtrackingcontentassisttest::roundbracketexp_pre_setter(instance):
    original = instance.pre
    instance.pre = original
    assert instance.pre == original

@given(instance=TypeExp_strategy)
@settings(max_examples=50)
def test_typeexp_instantiation(instance):
    assert isinstance(instance, TypeExp)

@given(instance=backtrackingContentAssistTest::TupleType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::tupletype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::TupleType)

@given(instance=backtrackingContentAssistTest::TupleType_strategy)
def test_backtrackingcontentassisttest::tupletype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::TupleType_strategy)
def test_backtrackingcontentassisttest::tupletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::CollectionType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::collectiontype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::CollectionType)

@given(instance=backtrackingContentAssistTest::CollectionType_strategy)
def test_backtrackingcontentassisttest::collectiontype_typeIdentifier_type(instance):
    assert isinstance(instance.typeIdentifier, str)


@given(instance=backtrackingContentAssistTest::CollectionType_strategy)
def test_backtrackingcontentassisttest::collectiontype_typeIdentifier_setter(instance):
    original = instance.typeIdentifier
    instance.typeIdentifier = original
    assert instance.typeIdentifier == original

@given(instance=backtrackingContentAssistTest::NameExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::nameexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::NameExp)

@given(instance=backtrackingContentAssistTest::PrimitiveType_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::primitivetype_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PrimitiveType)

@given(instance=backtrackingContentAssistTest::PrimitiveType_strategy)
def test_backtrackingcontentassisttest::primitivetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::PrimitiveType_strategy)
def test_backtrackingcontentassisttest::primitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::TupleLiteralPart)

@given(instance=backtrackingContentAssistTest::TupleLiteralPart_strategy)
def test_backtrackingcontentassisttest::tupleliteralpart_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=backtrackingContentAssistTest::TupleLiteralPart_strategy)
def test_backtrackingcontentassisttest::tupleliteralpart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=backtrackingContentAssistTest::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::TupleLiteralExp)

@given(instance=backtrackingContentAssistTest::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PrimitiveLiteralExp)

@given(instance=PropertyRef_strategy)
@settings(max_examples=50)
def test_propertyref_instantiation(instance):
    assert isinstance(instance, PropertyRef)

@given(instance=backtrackingContentAssistTest::QualifiedPropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::qualifiedpropertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::QualifiedPropertyRef)

@given(instance=backtrackingContentAssistTest::QualifiedPropertyRef_strategy)
def test_backtrackingcontentassisttest::qualifiedpropertyref_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=backtrackingContentAssistTest::QualifiedPropertyRef_strategy)
def test_backtrackingcontentassisttest::qualifiedpropertyref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=OperationRef_strategy)
@settings(max_examples=50)
def test_operationref_instantiation(instance):
    assert isinstance(instance, OperationRef)

@given(instance=backtrackingContentAssistTest::QualifiedOperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::qualifiedoperationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::QualifiedOperationRef)

@given(instance=backtrackingContentAssistTest::QualifiedOperationRef_strategy)
def test_backtrackingcontentassisttest::qualifiedoperationref_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=backtrackingContentAssistTest::QualifiedOperationRef_strategy)
def test_backtrackingcontentassisttest::qualifiedoperationref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=ClassifierRef_strategy)
@settings(max_examples=50)
def test_classifierref_instantiation(instance):
    assert isinstance(instance, ClassifierRef)

@given(instance=backtrackingContentAssistTest::QualifiedClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::qualifiedclassifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::QualifiedClassifierRef)

@given(instance=backtrackingContentAssistTest::QualifiedClassifierRef_strategy)
def test_backtrackingcontentassisttest::qualifiedclassifierref_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=backtrackingContentAssistTest::QualifiedClassifierRef_strategy)
def test_backtrackingcontentassisttest::qualifiedclassifierref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest::PropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::propertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::PropertyRef)

@given(instance=backtrackingContentAssistTest::OclMessageArg_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::oclmessagearg_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::OclMessageArg)

@given(instance=backtrackingContentAssistTest::NavigatingExp_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::navigatingexp_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::NavigatingExp)

@given(instance=OclMessageArg_strategy)
@settings(max_examples=50)
def test_oclmessagearg_instantiation(instance):
    assert isinstance(instance, OclMessageArg)

@given(instance=NavigatingExp_strategy)
@settings(max_examples=50)
def test_navigatingexp_instantiation(instance):
    assert isinstance(instance, NavigatingExp)

@given(instance=backtrackingContentAssistTest::Expression_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::expression_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Expression)

@given(instance=backtrackingContentAssistTest::SimplePropertyRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::simplepropertyref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SimplePropertyRef)

@given(instance=backtrackingContentAssistTest::SimplePropertyRef_strategy)
def test_backtrackingcontentassisttest::simplepropertyref_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=backtrackingContentAssistTest::SimplePropertyRef_strategy)
def test_backtrackingcontentassisttest::simplepropertyref_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=backtrackingContentAssistTest::SimpleOperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::simpleoperationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SimpleOperationRef)

@given(instance=backtrackingContentAssistTest::SimpleOperationRef_strategy)
def test_backtrackingcontentassisttest::simpleoperationref_operation_type(instance):
    assert isinstance(instance.operation, str)


@given(instance=backtrackingContentAssistTest::SimpleOperationRef_strategy)
def test_backtrackingcontentassisttest::simpleoperationref_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=backtrackingContentAssistTest::SimpleClassifierRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::simpleclassifierref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SimpleClassifierRef)

@given(instance=backtrackingContentAssistTest::SimpleClassifierRef_strategy)
def test_backtrackingcontentassisttest::simpleclassifierref_classifier_type(instance):
    assert isinstance(instance.classifier, str)


@given(instance=backtrackingContentAssistTest::SimpleClassifierRef_strategy)
def test_backtrackingcontentassisttest::simpleclassifierref_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=PackageRef_strategy)
@settings(max_examples=50)
def test_packageref_instantiation(instance):
    assert isinstance(instance, PackageRef)

@given(instance=backtrackingContentAssistTest::SimplePackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::simplepackageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::SimplePackageRef)

@given(instance=backtrackingContentAssistTest::SimplePackageRef_strategy)
def test_backtrackingcontentassisttest::simplepackageref_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=backtrackingContentAssistTest::SimplePackageRef_strategy)
def test_backtrackingcontentassisttest::simplepackageref_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=backtrackingContentAssistTest::QualifiedPackageRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::qualifiedpackageref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::QualifiedPackageRef)

@given(instance=backtrackingContentAssistTest::QualifiedPackageRef_strategy)
def test_backtrackingcontentassisttest::qualifiedpackageref_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=backtrackingContentAssistTest::QualifiedPackageRef_strategy)
def test_backtrackingcontentassisttest::qualifiedpackageref_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=backtrackingContentAssistTest::Pre_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::pre_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::Pre)

@given(instance=backtrackingContentAssistTest::Pre_strategy)
def test_backtrackingcontentassisttest::pre_constraintName_type(instance):
    assert isinstance(instance.constraintName, str)


@given(instance=backtrackingContentAssistTest::Pre_strategy)
def test_backtrackingcontentassisttest::pre_constraintName_setter(instance):
    original = instance.constraintName
    instance.constraintName = original
    assert instance.constraintName == original

@given(instance=backtrackingContentAssistTest::OperationRef_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::operationref_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::OperationRef)

@given(instance=backtrackingContentAssistTest::OperationContextDecl_strategy)
@settings(max_examples=50)
def test_backtrackingcontentassisttest::operationcontextdecl_instantiation(instance):
    assert isinstance(instance, backtrackingContentAssistTest::OperationContextDecl)
