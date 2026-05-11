import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OperatorExp,
    FPath::BinaryOperatorExp,
    Test,
    FPath::NameTest,
    FPath::WildcardTest,
    FPath::UnaryOperatorExp,
    Expression,
    FPath::OperatorExp,
    FPath::StringExp,
    FPath::NumberExp,
    FPath::VariableExp,
    FPath::FunctionCallExp,
    FPath::PathExp,
    FPath::ContextExp,
    LocatedElement,
    FPath::Step,
    FPath::Test,
    FPath::Expression,
    FPath::LocatedElement,
    Axis,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_operatorexp_is_not_abstract():
    assert not inspect.isabstract(OperatorExp)


def test_operatorexp_constructor_exists():
    assert callable(OperatorExp.__init__)


def test_operatorexp_constructor_args():
    sig = inspect.signature(OperatorExp.__init__)
    params = list(sig.parameters.keys())



def test_fpath::binaryoperatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath::BinaryOperatorExp)


def test_fpath::binaryoperatorexp_constructor_exists():
    assert callable(FPath::BinaryOperatorExp.__init__)


def test_fpath::binaryoperatorexp_constructor_args():
    sig = inspect.signature(FPath::BinaryOperatorExp.__init__)
    params = list(sig.parameters.keys())



def test_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_test_constructor_exists():
    assert callable(Test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())



def test_fpath::nametest_is_not_abstract():
    assert not inspect.isabstract(FPath::NameTest)


def test_fpath::nametest_constructor_exists():
    assert callable(FPath::NameTest.__init__)


def test_fpath::nametest_constructor_args():
    sig = inspect.signature(FPath::NameTest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath::nametest_has_name():
    assert hasattr(FPath::NameTest, "name")
    descriptor = None
    for klass in FPath::NameTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath::wildcardtest_is_not_abstract():
    assert not inspect.isabstract(FPath::WildcardTest)


def test_fpath::wildcardtest_constructor_exists():
    assert callable(FPath::WildcardTest.__init__)


def test_fpath::wildcardtest_constructor_args():
    sig = inspect.signature(FPath::WildcardTest.__init__)
    params = list(sig.parameters.keys())



def test_fpath::unaryoperatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath::UnaryOperatorExp)


def test_fpath::unaryoperatorexp_constructor_exists():
    assert callable(FPath::UnaryOperatorExp.__init__)


def test_fpath::unaryoperatorexp_constructor_args():
    sig = inspect.signature(FPath::UnaryOperatorExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_fpath::operatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath::OperatorExp)


def test_fpath::operatorexp_constructor_exists():
    assert callable(FPath::OperatorExp.__init__)


def test_fpath::operatorexp_constructor_args():
    sig = inspect.signature(FPath::OperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fpath::operatorexp_has_operator():
    assert hasattr(FPath::OperatorExp, "operator")
    descriptor = None
    for klass in FPath::OperatorExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fpath::stringexp_is_not_abstract():
    assert not inspect.isabstract(FPath::StringExp)


def test_fpath::stringexp_constructor_exists():
    assert callable(FPath::StringExp.__init__)


def test_fpath::stringexp_constructor_args():
    sig = inspect.signature(FPath::StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fpath::stringexp_has_value():
    assert hasattr(FPath::StringExp, "value")
    descriptor = None
    for klass in FPath::StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fpath::numberexp_is_not_abstract():
    assert not inspect.isabstract(FPath::NumberExp)


def test_fpath::numberexp_constructor_exists():
    assert callable(FPath::NumberExp.__init__)


def test_fpath::numberexp_constructor_args():
    sig = inspect.signature(FPath::NumberExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fpath::numberexp_has_value():
    assert hasattr(FPath::NumberExp, "value")
    descriptor = None
    for klass in FPath::NumberExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fpath::variableexp_is_not_abstract():
    assert not inspect.isabstract(FPath::VariableExp)


def test_fpath::variableexp_constructor_exists():
    assert callable(FPath::VariableExp.__init__)


def test_fpath::variableexp_constructor_args():
    sig = inspect.signature(FPath::VariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath::variableexp_has_name():
    assert hasattr(FPath::VariableExp, "name")
    descriptor = None
    for klass in FPath::VariableExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath::functioncallexp_is_not_abstract():
    assert not inspect.isabstract(FPath::FunctionCallExp)


def test_fpath::functioncallexp_constructor_exists():
    assert callable(FPath::FunctionCallExp.__init__)


def test_fpath::functioncallexp_constructor_args():
    sig = inspect.signature(FPath::FunctionCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath::functioncallexp_has_name():
    assert hasattr(FPath::FunctionCallExp, "name")
    descriptor = None
    for klass in FPath::FunctionCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath::pathexp_is_not_abstract():
    assert not inspect.isabstract(FPath::PathExp)


def test_fpath::pathexp_constructor_exists():
    assert callable(FPath::PathExp.__init__)


def test_fpath::pathexp_constructor_args():
    sig = inspect.signature(FPath::PathExp.__init__)
    params = list(sig.parameters.keys())



def test_fpath::contextexp_is_not_abstract():
    assert not inspect.isabstract(FPath::ContextExp)


def test_fpath::contextexp_constructor_exists():
    assert callable(FPath::ContextExp.__init__)


def test_fpath::contextexp_constructor_args():
    sig = inspect.signature(FPath::ContextExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_fpath::step_is_not_abstract():
    assert not inspect.isabstract(FPath::Step)


def test_fpath::step_constructor_exists():
    assert callable(FPath::Step.__init__)


def test_fpath::step_constructor_args():
    sig = inspect.signature(FPath::Step.__init__)
    params = list(sig.parameters.keys())
    assert "axis" in params, "Missing parameter 'axis'"

def test_fpath::step_has_axis():
    assert hasattr(FPath::Step, "axis")
    descriptor = None
    for klass in FPath::Step.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)



def test_fpath::test_is_not_abstract():
    assert not inspect.isabstract(FPath::Test)


def test_fpath::test_constructor_exists():
    assert callable(FPath::Test.__init__)


def test_fpath::test_constructor_args():
    sig = inspect.signature(FPath::Test.__init__)
    params = list(sig.parameters.keys())



def test_fpath::expression_is_not_abstract():
    assert not inspect.isabstract(FPath::Expression)


def test_fpath::expression_constructor_exists():
    assert callable(FPath::Expression.__init__)


def test_fpath::expression_constructor_args():
    sig = inspect.signature(FPath::Expression.__init__)
    params = list(sig.parameters.keys())



def test_fpath::locatedelement_is_not_abstract():
    assert not inspect.isabstract(FPath::LocatedElement)


def test_fpath::locatedelement_constructor_exists():
    assert callable(FPath::LocatedElement.__init__)


def test_fpath::locatedelement_constructor_args():
    sig = inspect.signature(FPath::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "location" in params, "Missing parameter 'location'"

def test_fpath::locatedelement_has_commentsAfter():
    assert hasattr(FPath::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in FPath::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_fpath::locatedelement_has_commentsBefore():
    assert hasattr(FPath::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in FPath::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_fpath::locatedelement_has_location():
    assert hasattr(FPath::LocatedElement, "location")
    descriptor = None
    for klass in FPath::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_axis_exists():
    # Check that the Enumeration exists
    assert Axis is not None

def test_axis_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Axis]
    expected_literals = [
        "parent",
        "attribute",
        "interface",
        "ancestor",
        "siblingorself",
        "ancestororself",
        "component",
        "child",
        "descendant",
        "sibling",
        "descendantorself",
        "internalinterface",
        "binding",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Axis"


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
OperatorExp_strategy = st.builds(
    OperatorExp,
)
FPath::BinaryOperatorExp_strategy = st.builds(
    FPath::BinaryOperatorExp,
)
Test_strategy = st.builds(
    Test,
)
FPath::NameTest_strategy = st.builds(
    FPath::NameTest,
    name=
        safe_text
)
FPath::WildcardTest_strategy = st.builds(
    FPath::WildcardTest,
)
FPath::UnaryOperatorExp_strategy = st.builds(
    FPath::UnaryOperatorExp,
)
Expression_strategy = st.builds(
    Expression,
)
FPath::OperatorExp_strategy = st.builds(
    FPath::OperatorExp,
    operator=
        safe_text
)
FPath::StringExp_strategy = st.builds(
    FPath::StringExp,
    value=
        safe_text
)
FPath::NumberExp_strategy = st.builds(
    FPath::NumberExp,
    value=
        safe_text
)
FPath::VariableExp_strategy = st.builds(
    FPath::VariableExp,
    name=
        safe_text
)
FPath::FunctionCallExp_strategy = st.builds(
    FPath::FunctionCallExp,
    name=
        safe_text
)
FPath::PathExp_strategy = st.builds(
    FPath::PathExp,
)
FPath::ContextExp_strategy = st.builds(
    FPath::ContextExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
FPath::Step_strategy = st.builds(
    FPath::Step,
    axis=
        safe_text
)
FPath::Test_strategy = st.builds(
    FPath::Test,
)
FPath::Expression_strategy = st.builds(
    FPath::Expression,
)
FPath::LocatedElement_strategy = st.builds(
    FPath::LocatedElement,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text,
    location=
        safe_text
)

@given(instance=OperatorExp_strategy)
@settings(max_examples=50)
def test_operatorexp_instantiation(instance):
    assert isinstance(instance, OperatorExp)

@given(instance=FPath::BinaryOperatorExp_strategy)
@settings(max_examples=50)
def test_fpath::binaryoperatorexp_instantiation(instance):
    assert isinstance(instance, FPath::BinaryOperatorExp)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)

@given(instance=FPath::NameTest_strategy)
@settings(max_examples=50)
def test_fpath::nametest_instantiation(instance):
    assert isinstance(instance, FPath::NameTest)

@given(instance=FPath::NameTest_strategy)
def test_fpath::nametest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FPath::NameTest_strategy)
def test_fpath::nametest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath::WildcardTest_strategy)
@settings(max_examples=50)
def test_fpath::wildcardtest_instantiation(instance):
    assert isinstance(instance, FPath::WildcardTest)

@given(instance=FPath::UnaryOperatorExp_strategy)
@settings(max_examples=50)
def test_fpath::unaryoperatorexp_instantiation(instance):
    assert isinstance(instance, FPath::UnaryOperatorExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=FPath::OperatorExp_strategy)
@settings(max_examples=50)
def test_fpath::operatorexp_instantiation(instance):
    assert isinstance(instance, FPath::OperatorExp)

@given(instance=FPath::OperatorExp_strategy)
def test_fpath::operatorexp_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=FPath::OperatorExp_strategy)
def test_fpath::operatorexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=FPath::StringExp_strategy)
@settings(max_examples=50)
def test_fpath::stringexp_instantiation(instance):
    assert isinstance(instance, FPath::StringExp)

@given(instance=FPath::StringExp_strategy)
def test_fpath::stringexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=FPath::StringExp_strategy)
def test_fpath::stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FPath::NumberExp_strategy)
@settings(max_examples=50)
def test_fpath::numberexp_instantiation(instance):
    assert isinstance(instance, FPath::NumberExp)

@given(instance=FPath::NumberExp_strategy)
def test_fpath::numberexp_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=FPath::NumberExp_strategy)
def test_fpath::numberexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FPath::VariableExp_strategy)
@settings(max_examples=50)
def test_fpath::variableexp_instantiation(instance):
    assert isinstance(instance, FPath::VariableExp)

@given(instance=FPath::VariableExp_strategy)
def test_fpath::variableexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FPath::VariableExp_strategy)
def test_fpath::variableexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath::FunctionCallExp_strategy)
@settings(max_examples=50)
def test_fpath::functioncallexp_instantiation(instance):
    assert isinstance(instance, FPath::FunctionCallExp)

@given(instance=FPath::FunctionCallExp_strategy)
def test_fpath::functioncallexp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=FPath::FunctionCallExp_strategy)
def test_fpath::functioncallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath::PathExp_strategy)
@settings(max_examples=50)
def test_fpath::pathexp_instantiation(instance):
    assert isinstance(instance, FPath::PathExp)

@given(instance=FPath::ContextExp_strategy)
@settings(max_examples=50)
def test_fpath::contextexp_instantiation(instance):
    assert isinstance(instance, FPath::ContextExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=FPath::Step_strategy)
@settings(max_examples=50)
def test_fpath::step_instantiation(instance):
    assert isinstance(instance, FPath::Step)

@given(instance=FPath::Step_strategy)
def test_fpath::step_axis_type(instance):
    assert isinstance(instance.axis, str)


@given(instance=FPath::Step_strategy)
def test_fpath::step_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original

@given(instance=FPath::Test_strategy)
@settings(max_examples=50)
def test_fpath::test_instantiation(instance):
    assert isinstance(instance, FPath::Test)

@given(instance=FPath::Expression_strategy)
@settings(max_examples=50)
def test_fpath::expression_instantiation(instance):
    assert isinstance(instance, FPath::Expression)

@given(instance=FPath::LocatedElement_strategy)
@settings(max_examples=50)
def test_fpath::locatedelement_instantiation(instance):
    assert isinstance(instance, FPath::LocatedElement)

@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=FPath::LocatedElement_strategy)
def test_fpath::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
