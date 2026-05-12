import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OperatorExp,
    FPath_BinaryOperatorExp,
    Test,
    FPath_NameTest,
    FPath_WildcardTest,
    FPath_UnaryOperatorExp,
    Expression,
    FPath_FunctionCallExp,
    FPath_NumberExp,
    FPath_OperatorExp,
    FPath_VariableExp,
    FPath_StringExp,
    FPath_PathExp,
    FPath_ContextExp,
    LocatedElement,
    FPath_Test,
    FPath_Step,
    FPath_Expression,
    FPath_LocatedElement,
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



def test_fpath_binaryoperatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath_BinaryOperatorExp)


def test_fpath_binaryoperatorexp_constructor_exists():
    assert callable(FPath_BinaryOperatorExp.__init__)


def test_fpath_binaryoperatorexp_constructor_args():
    sig = inspect.signature(FPath_BinaryOperatorExp.__init__)
    params = list(sig.parameters.keys())



def test_test_is_not_abstract():
    assert not inspect.isabstract(Test)


def test_test_constructor_exists():
    assert callable(Test.__init__)


def test_test_constructor_args():
    sig = inspect.signature(Test.__init__)
    params = list(sig.parameters.keys())



def test_fpath_nametest_is_not_abstract():
    assert not inspect.isabstract(FPath_NameTest)


def test_fpath_nametest_constructor_exists():
    assert callable(FPath_NameTest.__init__)


def test_fpath_nametest_constructor_args():
    sig = inspect.signature(FPath_NameTest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath_nametest_has_name():
    assert hasattr(FPath_NameTest, "name")
    descriptor = None
    for klass in FPath_NameTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath_wildcardtest_is_not_abstract():
    assert not inspect.isabstract(FPath_WildcardTest)


def test_fpath_wildcardtest_constructor_exists():
    assert callable(FPath_WildcardTest.__init__)


def test_fpath_wildcardtest_constructor_args():
    sig = inspect.signature(FPath_WildcardTest.__init__)
    params = list(sig.parameters.keys())



def test_fpath_unaryoperatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath_UnaryOperatorExp)


def test_fpath_unaryoperatorexp_constructor_exists():
    assert callable(FPath_UnaryOperatorExp.__init__)


def test_fpath_unaryoperatorexp_constructor_args():
    sig = inspect.signature(FPath_UnaryOperatorExp.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_fpath_functioncallexp_is_not_abstract():
    assert not inspect.isabstract(FPath_FunctionCallExp)


def test_fpath_functioncallexp_constructor_exists():
    assert callable(FPath_FunctionCallExp.__init__)


def test_fpath_functioncallexp_constructor_args():
    sig = inspect.signature(FPath_FunctionCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath_functioncallexp_has_name():
    assert hasattr(FPath_FunctionCallExp, "name")
    descriptor = None
    for klass in FPath_FunctionCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath_numberexp_is_not_abstract():
    assert not inspect.isabstract(FPath_NumberExp)


def test_fpath_numberexp_constructor_exists():
    assert callable(FPath_NumberExp.__init__)


def test_fpath_numberexp_constructor_args():
    sig = inspect.signature(FPath_NumberExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fpath_numberexp_has_value():
    assert hasattr(FPath_NumberExp, "value")
    descriptor = None
    for klass in FPath_NumberExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fpath_operatorexp_is_not_abstract():
    assert not inspect.isabstract(FPath_OperatorExp)


def test_fpath_operatorexp_constructor_exists():
    assert callable(FPath_OperatorExp.__init__)


def test_fpath_operatorexp_constructor_args():
    sig = inspect.signature(FPath_OperatorExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_fpath_operatorexp_has_operator():
    assert hasattr(FPath_OperatorExp, "operator")
    descriptor = None
    for klass in FPath_OperatorExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_fpath_variableexp_is_not_abstract():
    assert not inspect.isabstract(FPath_VariableExp)


def test_fpath_variableexp_constructor_exists():
    assert callable(FPath_VariableExp.__init__)


def test_fpath_variableexp_constructor_args():
    sig = inspect.signature(FPath_VariableExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fpath_variableexp_has_name():
    assert hasattr(FPath_VariableExp, "name")
    descriptor = None
    for klass in FPath_VariableExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fpath_stringexp_is_not_abstract():
    assert not inspect.isabstract(FPath_StringExp)


def test_fpath_stringexp_constructor_exists():
    assert callable(FPath_StringExp.__init__)


def test_fpath_stringexp_constructor_args():
    sig = inspect.signature(FPath_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_fpath_stringexp_has_value():
    assert hasattr(FPath_StringExp, "value")
    descriptor = None
    for klass in FPath_StringExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fpath_pathexp_is_not_abstract():
    assert not inspect.isabstract(FPath_PathExp)


def test_fpath_pathexp_constructor_exists():
    assert callable(FPath_PathExp.__init__)


def test_fpath_pathexp_constructor_args():
    sig = inspect.signature(FPath_PathExp.__init__)
    params = list(sig.parameters.keys())



def test_fpath_contextexp_is_not_abstract():
    assert not inspect.isabstract(FPath_ContextExp)


def test_fpath_contextexp_constructor_exists():
    assert callable(FPath_ContextExp.__init__)


def test_fpath_contextexp_constructor_args():
    sig = inspect.signature(FPath_ContextExp.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_fpath_test_is_not_abstract():
    assert not inspect.isabstract(FPath_Test)


def test_fpath_test_constructor_exists():
    assert callable(FPath_Test.__init__)


def test_fpath_test_constructor_args():
    sig = inspect.signature(FPath_Test.__init__)
    params = list(sig.parameters.keys())



def test_fpath_step_is_not_abstract():
    assert not inspect.isabstract(FPath_Step)


def test_fpath_step_constructor_exists():
    assert callable(FPath_Step.__init__)


def test_fpath_step_constructor_args():
    sig = inspect.signature(FPath_Step.__init__)
    params = list(sig.parameters.keys())
    assert "axis" in params, "Missing parameter 'axis'"

def test_fpath_step_has_axis():
    assert hasattr(FPath_Step, "axis")
    descriptor = None
    for klass in FPath_Step.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)



def test_fpath_expression_is_not_abstract():
    assert not inspect.isabstract(FPath_Expression)


def test_fpath_expression_constructor_exists():
    assert callable(FPath_Expression.__init__)


def test_fpath_expression_constructor_args():
    sig = inspect.signature(FPath_Expression.__init__)
    params = list(sig.parameters.keys())



def test_fpath_locatedelement_is_not_abstract():
    assert not inspect.isabstract(FPath_LocatedElement)


def test_fpath_locatedelement_constructor_exists():
    assert callable(FPath_LocatedElement.__init__)


def test_fpath_locatedelement_constructor_args():
    sig = inspect.signature(FPath_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_fpath_locatedelement_has_location():
    assert hasattr(FPath_LocatedElement, "location")
    descriptor = None
    for klass in FPath_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_fpath_locatedelement_has_commentsAfter():
    assert hasattr(FPath_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in FPath_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_fpath_locatedelement_has_commentsBefore():
    assert hasattr(FPath_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in FPath_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_axis_exists():
    # Check that the Enumeration exists
    assert Axis is not None

def test_axis_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Axis]
    expected_literals = [
        "sibling",
        "binding",
        "parent",
        "attribute",
        "interface",
        "siblingorself",
        "descendantorself",
        "ancestororself",
        "descendant",
        "ancestor",
        "internalinterface",
        "child",
        "component",
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
FPath_BinaryOperatorExp_strategy = st.builds(
    FPath_BinaryOperatorExp,
)
Test_strategy = st.builds(
    Test,
)
FPath_NameTest_strategy = st.builds(
    FPath_NameTest,
    name=
        safe_text
)
FPath_WildcardTest_strategy = st.builds(
    FPath_WildcardTest,
)
FPath_UnaryOperatorExp_strategy = st.builds(
    FPath_UnaryOperatorExp,
)
Expression_strategy = st.builds(
    Expression,
)
FPath_FunctionCallExp_strategy = st.builds(
    FPath_FunctionCallExp,
    name=
        safe_text
)
FPath_NumberExp_strategy = st.builds(
    FPath_NumberExp,
    value=
        safe_text
)
FPath_OperatorExp_strategy = st.builds(
    FPath_OperatorExp,
    operator=
        safe_text
)
FPath_VariableExp_strategy = st.builds(
    FPath_VariableExp,
    name=
        safe_text
)
FPath_StringExp_strategy = st.builds(
    FPath_StringExp,
    value=
        safe_text
)
FPath_PathExp_strategy = st.builds(
    FPath_PathExp,
)
FPath_ContextExp_strategy = st.builds(
    FPath_ContextExp,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
FPath_Test_strategy = st.builds(
    FPath_Test,
)
FPath_Step_strategy = st.builds(
    FPath_Step,
    axis=
        safe_text
)
FPath_Expression_strategy = st.builds(
    FPath_Expression,
)
FPath_LocatedElement_strategy = st.builds(
    FPath_LocatedElement,
    location=
        safe_text,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=OperatorExp_strategy)
@settings(max_examples=50)
def test_operatorexp_instantiation(instance):
    assert isinstance(instance, OperatorExp)

@given(instance=FPath_BinaryOperatorExp_strategy)
@settings(max_examples=50)
def test_fpath_binaryoperatorexp_instantiation(instance):
    assert isinstance(instance, FPath_BinaryOperatorExp)

@given(instance=Test_strategy)
@settings(max_examples=50)
def test_test_instantiation(instance):
    assert isinstance(instance, Test)

@given(instance=FPath_NameTest_strategy)
@settings(max_examples=50)
def test_fpath_nametest_instantiation(instance):
    assert isinstance(instance, FPath_NameTest)



@given(instance=FPath_NameTest_strategy)
def test_fpath_nametest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath_WildcardTest_strategy)
@settings(max_examples=50)
def test_fpath_wildcardtest_instantiation(instance):
    assert isinstance(instance, FPath_WildcardTest)

@given(instance=FPath_UnaryOperatorExp_strategy)
@settings(max_examples=50)
def test_fpath_unaryoperatorexp_instantiation(instance):
    assert isinstance(instance, FPath_UnaryOperatorExp)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=FPath_FunctionCallExp_strategy)
@settings(max_examples=50)
def test_fpath_functioncallexp_instantiation(instance):
    assert isinstance(instance, FPath_FunctionCallExp)



@given(instance=FPath_FunctionCallExp_strategy)
def test_fpath_functioncallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath_NumberExp_strategy)
@settings(max_examples=50)
def test_fpath_numberexp_instantiation(instance):
    assert isinstance(instance, FPath_NumberExp)



@given(instance=FPath_NumberExp_strategy)
def test_fpath_numberexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FPath_OperatorExp_strategy)
@settings(max_examples=50)
def test_fpath_operatorexp_instantiation(instance):
    assert isinstance(instance, FPath_OperatorExp)



@given(instance=FPath_OperatorExp_strategy)
def test_fpath_operatorexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=FPath_VariableExp_strategy)
@settings(max_examples=50)
def test_fpath_variableexp_instantiation(instance):
    assert isinstance(instance, FPath_VariableExp)



@given(instance=FPath_VariableExp_strategy)
def test_fpath_variableexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FPath_StringExp_strategy)
@settings(max_examples=50)
def test_fpath_stringexp_instantiation(instance):
    assert isinstance(instance, FPath_StringExp)



@given(instance=FPath_StringExp_strategy)
def test_fpath_stringexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=FPath_PathExp_strategy)
@settings(max_examples=50)
def test_fpath_pathexp_instantiation(instance):
    assert isinstance(instance, FPath_PathExp)

@given(instance=FPath_ContextExp_strategy)
@settings(max_examples=50)
def test_fpath_contextexp_instantiation(instance):
    assert isinstance(instance, FPath_ContextExp)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=FPath_Test_strategy)
@settings(max_examples=50)
def test_fpath_test_instantiation(instance):
    assert isinstance(instance, FPath_Test)

@given(instance=FPath_Step_strategy)
@settings(max_examples=50)
def test_fpath_step_instantiation(instance):
    assert isinstance(instance, FPath_Step)



@given(instance=FPath_Step_strategy)
def test_fpath_step_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original

@given(instance=FPath_Expression_strategy)
@settings(max_examples=50)
def test_fpath_expression_instantiation(instance):
    assert isinstance(instance, FPath_Expression)

@given(instance=FPath_LocatedElement_strategy)
@settings(max_examples=50)
def test_fpath_locatedelement_instantiation(instance):
    assert isinstance(instance, FPath_LocatedElement)



@given(instance=FPath_LocatedElement_strategy)
def test_fpath_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=FPath_LocatedElement_strategy)
def test_fpath_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=FPath_LocatedElement_strategy)
def test_fpath_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
