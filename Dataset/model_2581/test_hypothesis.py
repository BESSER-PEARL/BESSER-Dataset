import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    esper::ExtraParenthesisRule,
    esper::Win,
    esper::JoinFollowBy,
    ExtraParenthesisRule,
    esper::Timer,
    esper::KindOfEvent,
    esper::TerminalExpression,
    esper::FollowByWhere,
    esper::FollowBy,
    esper::AbstractFollowBy,
    esper::Pattern,
    esper::Anything,
    esper::SingleDefinition,
    esper::DefaultMethods,
    esper::SingleSelectDefinition,
    esper::KindSelectAttributesDefinition,
    esper::SelectAttributesDefinition,
    esper::Having,
    esper::GroupBy,
    esper::From,
    esper::Select,
    esper::Priority,
    esper::Name,
    esper::AttributesDefinition,
    esper::Attributes,
    KindOfEvent,
    esper::Insert,
    esper::Event,
    esper::RuleParts,
    esper::Domainmodel,
    Operators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esper::extraparenthesisrule_is_not_abstract():
    assert not inspect.isabstract(esper::ExtraParenthesisRule)


def test_esper::extraparenthesisrule_constructor_exists():
    assert callable(esper::ExtraParenthesisRule.__init__)


def test_esper::extraparenthesisrule_constructor_args():
    sig = inspect.signature(esper::ExtraParenthesisRule.__init__)
    params = list(sig.parameters.keys())



def test_esper::win_is_not_abstract():
    assert not inspect.isabstract(esper::Win)


def test_esper::win_constructor_exists():
    assert callable(esper::Win.__init__)


def test_esper::win_constructor_args():
    sig = inspect.signature(esper::Win.__init__)
    params = list(sig.parameters.keys())



def test_esper::joinfollowby_is_not_abstract():
    assert not inspect.isabstract(esper::JoinFollowBy)


def test_esper::joinfollowby_constructor_exists():
    assert callable(esper::JoinFollowBy.__init__)


def test_esper::joinfollowby_constructor_args():
    sig = inspect.signature(esper::JoinFollowBy.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper::joinfollowby_has_operator():
    assert hasattr(esper::JoinFollowBy, "operator")
    descriptor = None
    for klass in esper::JoinFollowBy.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_extraparenthesisrule_is_not_abstract():
    assert not inspect.isabstract(ExtraParenthesisRule)


def test_extraparenthesisrule_constructor_exists():
    assert callable(ExtraParenthesisRule.__init__)


def test_extraparenthesisrule_constructor_args():
    sig = inspect.signature(ExtraParenthesisRule.__init__)
    params = list(sig.parameters.keys())



def test_esper::timer_is_not_abstract():
    assert not inspect.isabstract(esper::Timer)


def test_esper::timer_constructor_exists():
    assert callable(esper::Timer.__init__)


def test_esper::timer_constructor_args():
    sig = inspect.signature(esper::Timer.__init__)
    params = list(sig.parameters.keys())



def test_esper::kindofevent_is_not_abstract():
    assert not inspect.isabstract(esper::KindOfEvent)


def test_esper::kindofevent_constructor_exists():
    assert callable(esper::KindOfEvent.__init__)


def test_esper::kindofevent_constructor_args():
    sig = inspect.signature(esper::KindOfEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper::kindofevent_has_name():
    assert hasattr(esper::KindOfEvent, "name")
    descriptor = None
    for klass in esper::KindOfEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper::terminalexpression_is_not_abstract():
    assert not inspect.isabstract(esper::TerminalExpression)


def test_esper::terminalexpression_constructor_exists():
    assert callable(esper::TerminalExpression.__init__)


def test_esper::terminalexpression_constructor_args():
    sig = inspect.signature(esper::TerminalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "every" in params, "Missing parameter 'every'"
    assert "parenthesis" in params, "Missing parameter 'parenthesis'"

def test_esper::terminalexpression_has_every():
    assert hasattr(esper::TerminalExpression, "every")
    descriptor = None
    for klass in esper::TerminalExpression.__mro__:
        if "every" in klass.__dict__:
            descriptor = klass.__dict__["every"]
            break
    assert isinstance(descriptor, property)

def test_esper::terminalexpression_has_parenthesis():
    assert hasattr(esper::TerminalExpression, "parenthesis")
    descriptor = None
    for klass in esper::TerminalExpression.__mro__:
        if "parenthesis" in klass.__dict__:
            descriptor = klass.__dict__["parenthesis"]
            break
    assert isinstance(descriptor, property)



def test_esper::followbywhere_is_not_abstract():
    assert not inspect.isabstract(esper::FollowByWhere)


def test_esper::followbywhere_constructor_exists():
    assert callable(esper::FollowByWhere.__init__)


def test_esper::followbywhere_constructor_args():
    sig = inspect.signature(esper::FollowByWhere.__init__)
    params = list(sig.parameters.keys())



def test_esper::followby_is_not_abstract():
    assert not inspect.isabstract(esper::FollowBy)


def test_esper::followby_constructor_exists():
    assert callable(esper::FollowBy.__init__)


def test_esper::followby_constructor_args():
    sig = inspect.signature(esper::FollowBy.__init__)
    params = list(sig.parameters.keys())



def test_esper::abstractfollowby_is_not_abstract():
    assert not inspect.isabstract(esper::AbstractFollowBy)


def test_esper::abstractfollowby_constructor_exists():
    assert callable(esper::AbstractFollowBy.__init__)


def test_esper::abstractfollowby_constructor_args():
    sig = inspect.signature(esper::AbstractFollowBy.__init__)
    params = list(sig.parameters.keys())



def test_esper::pattern_is_not_abstract():
    assert not inspect.isabstract(esper::Pattern)


def test_esper::pattern_constructor_exists():
    assert callable(esper::Pattern.__init__)


def test_esper::pattern_constructor_args():
    sig = inspect.signature(esper::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_esper::anything_is_not_abstract():
    assert not inspect.isabstract(esper::Anything)


def test_esper::anything_constructor_exists():
    assert callable(esper::Anything.__init__)


def test_esper::anything_constructor_args():
    sig = inspect.signature(esper::Anything.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper::anything_has_operator():
    assert hasattr(esper::Anything, "operator")
    descriptor = None
    for klass in esper::Anything.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper::singledefinition_is_not_abstract():
    assert not inspect.isabstract(esper::SingleDefinition)


def test_esper::singledefinition_constructor_exists():
    assert callable(esper::SingleDefinition.__init__)


def test_esper::singledefinition_constructor_args():
    sig = inspect.signature(esper::SingleDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper::singledefinition_has_name():
    assert hasattr(esper::SingleDefinition, "name")
    descriptor = None
    for klass in esper::SingleDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper::defaultmethods_is_not_abstract():
    assert not inspect.isabstract(esper::DefaultMethods)


def test_esper::defaultmethods_constructor_exists():
    assert callable(esper::DefaultMethods.__init__)


def test_esper::defaultmethods_constructor_args():
    sig = inspect.signature(esper::DefaultMethods.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper::defaultmethods_has_name():
    assert hasattr(esper::DefaultMethods, "name")
    descriptor = None
    for klass in esper::DefaultMethods.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper::singleselectdefinition_is_not_abstract():
    assert not inspect.isabstract(esper::SingleSelectDefinition)


def test_esper::singleselectdefinition_constructor_exists():
    assert callable(esper::SingleSelectDefinition.__init__)


def test_esper::singleselectdefinition_constructor_args():
    sig = inspect.signature(esper::SingleSelectDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_esper::singleselectdefinition_has_attribute():
    assert hasattr(esper::SingleSelectDefinition, "attribute")
    descriptor = None
    for klass in esper::SingleSelectDefinition.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_esper::kindselectattributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper::KindSelectAttributesDefinition)


def test_esper::kindselectattributesdefinition_constructor_exists():
    assert callable(esper::KindSelectAttributesDefinition.__init__)


def test_esper::kindselectattributesdefinition_constructor_args():
    sig = inspect.signature(esper::KindSelectAttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "int" in params, "Missing parameter 'int'"

def test_esper::kindselectattributesdefinition_has_string():
    assert hasattr(esper::KindSelectAttributesDefinition, "string")
    descriptor = None
    for klass in esper::KindSelectAttributesDefinition.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_esper::kindselectattributesdefinition_has_int():
    assert hasattr(esper::KindSelectAttributesDefinition, "int")
    descriptor = None
    for klass in esper::KindSelectAttributesDefinition.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_esper::selectattributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper::SelectAttributesDefinition)


def test_esper::selectattributesdefinition_constructor_exists():
    assert callable(esper::SelectAttributesDefinition.__init__)


def test_esper::selectattributesdefinition_constructor_args():
    sig = inspect.signature(esper::SelectAttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper::selectattributesdefinition_has_operator():
    assert hasattr(esper::SelectAttributesDefinition, "operator")
    descriptor = None
    for klass in esper::SelectAttributesDefinition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper::having_is_not_abstract():
    assert not inspect.isabstract(esper::Having)


def test_esper::having_constructor_exists():
    assert callable(esper::Having.__init__)


def test_esper::having_constructor_args():
    sig = inspect.signature(esper::Having.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper::having_has_operator():
    assert hasattr(esper::Having, "operator")
    descriptor = None
    for klass in esper::Having.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper::groupby_is_not_abstract():
    assert not inspect.isabstract(esper::GroupBy)


def test_esper::groupby_constructor_exists():
    assert callable(esper::GroupBy.__init__)


def test_esper::groupby_constructor_args():
    sig = inspect.signature(esper::GroupBy.__init__)
    params = list(sig.parameters.keys())



def test_esper::from_is_not_abstract():
    assert not inspect.isabstract(esper::From)


def test_esper::from_constructor_exists():
    assert callable(esper::From.__init__)


def test_esper::from_constructor_args():
    sig = inspect.signature(esper::From.__init__)
    params = list(sig.parameters.keys())



def test_esper::select_is_not_abstract():
    assert not inspect.isabstract(esper::Select)


def test_esper::select_constructor_exists():
    assert callable(esper::Select.__init__)


def test_esper::select_constructor_args():
    sig = inspect.signature(esper::Select.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "asterisk" in params, "Missing parameter 'asterisk'"

def test_esper::select_has_alias():
    assert hasattr(esper::Select, "alias")
    descriptor = None
    for klass in esper::Select.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_esper::select_has_asterisk():
    assert hasattr(esper::Select, "asterisk")
    descriptor = None
    for klass in esper::Select.__mro__:
        if "asterisk" in klass.__dict__:
            descriptor = klass.__dict__["asterisk"]
            break
    assert isinstance(descriptor, property)



def test_esper::priority_is_not_abstract():
    assert not inspect.isabstract(esper::Priority)


def test_esper::priority_constructor_exists():
    assert callable(esper::Priority.__init__)


def test_esper::priority_constructor_args():
    sig = inspect.signature(esper::Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priorityInt" in params, "Missing parameter 'priorityInt'"

def test_esper::priority_has_priorityInt():
    assert hasattr(esper::Priority, "priorityInt")
    descriptor = None
    for klass in esper::Priority.__mro__:
        if "priorityInt" in klass.__dict__:
            descriptor = klass.__dict__["priorityInt"]
            break
    assert isinstance(descriptor, property)



def test_esper::name_is_not_abstract():
    assert not inspect.isabstract(esper::Name)


def test_esper::name_constructor_exists():
    assert callable(esper::Name.__init__)


def test_esper::name_constructor_args():
    sig = inspect.signature(esper::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper::name_has_name():
    assert hasattr(esper::Name, "name")
    descriptor = None
    for klass in esper::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper::attributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper::AttributesDefinition)


def test_esper::attributesdefinition_constructor_exists():
    assert callable(esper::AttributesDefinition.__init__)


def test_esper::attributesdefinition_constructor_args():
    sig = inspect.signature(esper::AttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_esper::attributesdefinition_has_name():
    assert hasattr(esper::AttributesDefinition, "name")
    descriptor = None
    for klass in esper::AttributesDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esper::attributesdefinition_has_type():
    assert hasattr(esper::AttributesDefinition, "type")
    descriptor = None
    for klass in esper::AttributesDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_esper::attributes_is_not_abstract():
    assert not inspect.isabstract(esper::Attributes)


def test_esper::attributes_constructor_exists():
    assert callable(esper::Attributes.__init__)


def test_esper::attributes_constructor_args():
    sig = inspect.signature(esper::Attributes.__init__)
    params = list(sig.parameters.keys())



def test_kindofevent_is_not_abstract():
    assert not inspect.isabstract(KindOfEvent)


def test_kindofevent_constructor_exists():
    assert callable(KindOfEvent.__init__)


def test_kindofevent_constructor_args():
    sig = inspect.signature(KindOfEvent.__init__)
    params = list(sig.parameters.keys())



def test_esper::insert_is_not_abstract():
    assert not inspect.isabstract(esper::Insert)


def test_esper::insert_constructor_exists():
    assert callable(esper::Insert.__init__)


def test_esper::insert_constructor_args():
    sig = inspect.signature(esper::Insert.__init__)
    params = list(sig.parameters.keys())



def test_esper::event_is_not_abstract():
    assert not inspect.isabstract(esper::Event)


def test_esper::event_constructor_exists():
    assert callable(esper::Event.__init__)


def test_esper::event_constructor_args():
    sig = inspect.signature(esper::Event.__init__)
    params = list(sig.parameters.keys())



def test_esper::ruleparts_is_not_abstract():
    assert not inspect.isabstract(esper::RuleParts)


def test_esper::ruleparts_constructor_exists():
    assert callable(esper::RuleParts.__init__)


def test_esper::ruleparts_constructor_args():
    sig = inspect.signature(esper::RuleParts.__init__)
    params = list(sig.parameters.keys())



def test_esper::domainmodel_is_not_abstract():
    assert not inspect.isabstract(esper::Domainmodel)


def test_esper::domainmodel_constructor_exists():
    assert callable(esper::Domainmodel.__init__)


def test_esper::domainmodel_constructor_args():
    sig = inspect.signature(esper::Domainmodel.__init__)
    params = list(sig.parameters.keys())

def test_operators_exists():
    # Check that the Enumeration exists
    assert Operators is not None

def test_operators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operators]
    expected_literals = [
        "between",
        "or_",
        "lessThan",
        "and_",
        "plus",
        "moreEqualThan",
        "not_",
        "in_",
        "notIn",
        "moreThan",
        "isnot",
        "multiplication",
        "equal",
        "lessEqualThan",
        "minus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Operators"


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
esper::ExtraParenthesisRule_strategy = st.builds(
    esper::ExtraParenthesisRule,
)
esper::Win_strategy = st.builds(
    esper::Win,
)
esper::JoinFollowBy_strategy = st.builds(
    esper::JoinFollowBy,
    operator=
        safe_text
)
ExtraParenthesisRule_strategy = st.builds(
    ExtraParenthesisRule,
)
esper::Timer_strategy = st.builds(
    esper::Timer,
)
esper::KindOfEvent_strategy = st.builds(
    esper::KindOfEvent,
    name=
        safe_text
)
esper::TerminalExpression_strategy = st.builds(
    esper::TerminalExpression,
    every=
        st.booleans(),
    parenthesis=
        st.booleans()
)
esper::FollowByWhere_strategy = st.builds(
    esper::FollowByWhere,
)
esper::FollowBy_strategy = st.builds(
    esper::FollowBy,
)
esper::AbstractFollowBy_strategy = st.builds(
    esper::AbstractFollowBy,
)
esper::Pattern_strategy = st.builds(
    esper::Pattern,
)
esper::Anything_strategy = st.builds(
    esper::Anything,
    operator=
        safe_text
)
esper::SingleDefinition_strategy = st.builds(
    esper::SingleDefinition,
    name=
        safe_text
)
esper::DefaultMethods_strategy = st.builds(
    esper::DefaultMethods,
    name=
        safe_text
)
esper::SingleSelectDefinition_strategy = st.builds(
    esper::SingleSelectDefinition,
    attribute=
        safe_text
)
esper::KindSelectAttributesDefinition_strategy = st.builds(
    esper::KindSelectAttributesDefinition,
    string=
        safe_text,
    int=
        st.integers()
)
esper::SelectAttributesDefinition_strategy = st.builds(
    esper::SelectAttributesDefinition,
    operator=
        safe_text
)
esper::Having_strategy = st.builds(
    esper::Having,
    operator=
        safe_text
)
esper::GroupBy_strategy = st.builds(
    esper::GroupBy,
)
esper::From_strategy = st.builds(
    esper::From,
)
esper::Select_strategy = st.builds(
    esper::Select,
    alias=
        safe_text,
    asterisk=
        st.booleans()
)
esper::Priority_strategy = st.builds(
    esper::Priority,
    priorityInt=
        st.integers()
)
esper::Name_strategy = st.builds(
    esper::Name,
    name=
        safe_text
)
esper::AttributesDefinition_strategy = st.builds(
    esper::AttributesDefinition,
    name=
        safe_text,
    type=
        safe_text
)
esper::Attributes_strategy = st.builds(
    esper::Attributes,
)
KindOfEvent_strategy = st.builds(
    KindOfEvent,
)
esper::Insert_strategy = st.builds(
    esper::Insert,
)
esper::Event_strategy = st.builds(
    esper::Event,
)
esper::RuleParts_strategy = st.builds(
    esper::RuleParts,
)
esper::Domainmodel_strategy = st.builds(
    esper::Domainmodel,
)

@given(instance=esper::ExtraParenthesisRule_strategy)
@settings(max_examples=50)
def test_esper::extraparenthesisrule_instantiation(instance):
    assert isinstance(instance, esper::ExtraParenthesisRule)

@given(instance=esper::Win_strategy)
@settings(max_examples=50)
def test_esper::win_instantiation(instance):
    assert isinstance(instance, esper::Win)

@given(instance=esper::JoinFollowBy_strategy)
@settings(max_examples=50)
def test_esper::joinfollowby_instantiation(instance):
    assert isinstance(instance, esper::JoinFollowBy)

@given(instance=esper::JoinFollowBy_strategy)
def test_esper::joinfollowby_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=esper::JoinFollowBy_strategy)
def test_esper::joinfollowby_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ExtraParenthesisRule_strategy)
@settings(max_examples=50)
def test_extraparenthesisrule_instantiation(instance):
    assert isinstance(instance, ExtraParenthesisRule)

@given(instance=esper::Timer_strategy)
@settings(max_examples=50)
def test_esper::timer_instantiation(instance):
    assert isinstance(instance, esper::Timer)

@given(instance=esper::KindOfEvent_strategy)
@settings(max_examples=50)
def test_esper::kindofevent_instantiation(instance):
    assert isinstance(instance, esper::KindOfEvent)

@given(instance=esper::KindOfEvent_strategy)
def test_esper::kindofevent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper::KindOfEvent_strategy)
def test_esper::kindofevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper::TerminalExpression_strategy)
@settings(max_examples=50)
def test_esper::terminalexpression_instantiation(instance):
    assert isinstance(instance, esper::TerminalExpression)

@given(instance=esper::TerminalExpression_strategy)
def test_esper::terminalexpression_every_type(instance):
    assert isinstance(instance.every, bool)


@given(instance=esper::TerminalExpression_strategy)
def test_esper::terminalexpression_every_setter(instance):
    original = instance.every
    instance.every = original
    assert instance.every == original

@given(instance=esper::TerminalExpression_strategy)
def test_esper::terminalexpression_parenthesis_type(instance):
    assert isinstance(instance.parenthesis, bool)


@given(instance=esper::TerminalExpression_strategy)
def test_esper::terminalexpression_parenthesis_setter(instance):
    original = instance.parenthesis
    instance.parenthesis = original
    assert instance.parenthesis == original

@given(instance=esper::FollowByWhere_strategy)
@settings(max_examples=50)
def test_esper::followbywhere_instantiation(instance):
    assert isinstance(instance, esper::FollowByWhere)

@given(instance=esper::FollowBy_strategy)
@settings(max_examples=50)
def test_esper::followby_instantiation(instance):
    assert isinstance(instance, esper::FollowBy)

@given(instance=esper::AbstractFollowBy_strategy)
@settings(max_examples=50)
def test_esper::abstractfollowby_instantiation(instance):
    assert isinstance(instance, esper::AbstractFollowBy)

@given(instance=esper::Pattern_strategy)
@settings(max_examples=50)
def test_esper::pattern_instantiation(instance):
    assert isinstance(instance, esper::Pattern)

@given(instance=esper::Anything_strategy)
@settings(max_examples=50)
def test_esper::anything_instantiation(instance):
    assert isinstance(instance, esper::Anything)

@given(instance=esper::Anything_strategy)
def test_esper::anything_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=esper::Anything_strategy)
def test_esper::anything_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper::SingleDefinition_strategy)
@settings(max_examples=50)
def test_esper::singledefinition_instantiation(instance):
    assert isinstance(instance, esper::SingleDefinition)

@given(instance=esper::SingleDefinition_strategy)
def test_esper::singledefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper::SingleDefinition_strategy)
def test_esper::singledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper::DefaultMethods_strategy)
@settings(max_examples=50)
def test_esper::defaultmethods_instantiation(instance):
    assert isinstance(instance, esper::DefaultMethods)

@given(instance=esper::DefaultMethods_strategy)
def test_esper::defaultmethods_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper::DefaultMethods_strategy)
def test_esper::defaultmethods_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper::SingleSelectDefinition_strategy)
@settings(max_examples=50)
def test_esper::singleselectdefinition_instantiation(instance):
    assert isinstance(instance, esper::SingleSelectDefinition)

@given(instance=esper::SingleSelectDefinition_strategy)
def test_esper::singleselectdefinition_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=esper::SingleSelectDefinition_strategy)
def test_esper::singleselectdefinition_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=esper::KindSelectAttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper::kindselectattributesdefinition_instantiation(instance):
    assert isinstance(instance, esper::KindSelectAttributesDefinition)

@given(instance=esper::KindSelectAttributesDefinition_strategy)
def test_esper::kindselectattributesdefinition_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=esper::KindSelectAttributesDefinition_strategy)
def test_esper::kindselectattributesdefinition_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=esper::KindSelectAttributesDefinition_strategy)
def test_esper::kindselectattributesdefinition_int_type(instance):
    assert isinstance(instance.int, int)


@given(instance=esper::KindSelectAttributesDefinition_strategy)
def test_esper::kindselectattributesdefinition_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=esper::SelectAttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper::selectattributesdefinition_instantiation(instance):
    assert isinstance(instance, esper::SelectAttributesDefinition)

@given(instance=esper::SelectAttributesDefinition_strategy)
def test_esper::selectattributesdefinition_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=esper::SelectAttributesDefinition_strategy)
def test_esper::selectattributesdefinition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper::Having_strategy)
@settings(max_examples=50)
def test_esper::having_instantiation(instance):
    assert isinstance(instance, esper::Having)

@given(instance=esper::Having_strategy)
def test_esper::having_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=esper::Having_strategy)
def test_esper::having_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper::GroupBy_strategy)
@settings(max_examples=50)
def test_esper::groupby_instantiation(instance):
    assert isinstance(instance, esper::GroupBy)

@given(instance=esper::From_strategy)
@settings(max_examples=50)
def test_esper::from_instantiation(instance):
    assert isinstance(instance, esper::From)

@given(instance=esper::Select_strategy)
@settings(max_examples=50)
def test_esper::select_instantiation(instance):
    assert isinstance(instance, esper::Select)

@given(instance=esper::Select_strategy)
def test_esper::select_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=esper::Select_strategy)
def test_esper::select_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=esper::Select_strategy)
def test_esper::select_asterisk_type(instance):
    assert isinstance(instance.asterisk, bool)


@given(instance=esper::Select_strategy)
def test_esper::select_asterisk_setter(instance):
    original = instance.asterisk
    instance.asterisk = original
    assert instance.asterisk == original

@given(instance=esper::Priority_strategy)
@settings(max_examples=50)
def test_esper::priority_instantiation(instance):
    assert isinstance(instance, esper::Priority)

@given(instance=esper::Priority_strategy)
def test_esper::priority_priorityInt_type(instance):
    assert isinstance(instance.priorityInt, int)


@given(instance=esper::Priority_strategy)
def test_esper::priority_priorityInt_setter(instance):
    original = instance.priorityInt
    instance.priorityInt = original
    assert instance.priorityInt == original

@given(instance=esper::Name_strategy)
@settings(max_examples=50)
def test_esper::name_instantiation(instance):
    assert isinstance(instance, esper::Name)

@given(instance=esper::Name_strategy)
def test_esper::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper::Name_strategy)
def test_esper::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper::AttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper::attributesdefinition_instantiation(instance):
    assert isinstance(instance, esper::AttributesDefinition)

@given(instance=esper::AttributesDefinition_strategy)
def test_esper::attributesdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper::AttributesDefinition_strategy)
def test_esper::attributesdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper::AttributesDefinition_strategy)
def test_esper::attributesdefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=esper::AttributesDefinition_strategy)
def test_esper::attributesdefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=esper::Attributes_strategy)
@settings(max_examples=50)
def test_esper::attributes_instantiation(instance):
    assert isinstance(instance, esper::Attributes)

@given(instance=KindOfEvent_strategy)
@settings(max_examples=50)
def test_kindofevent_instantiation(instance):
    assert isinstance(instance, KindOfEvent)

@given(instance=esper::Insert_strategy)
@settings(max_examples=50)
def test_esper::insert_instantiation(instance):
    assert isinstance(instance, esper::Insert)

@given(instance=esper::Event_strategy)
@settings(max_examples=50)
def test_esper::event_instantiation(instance):
    assert isinstance(instance, esper::Event)

@given(instance=esper::RuleParts_strategy)
@settings(max_examples=50)
def test_esper::ruleparts_instantiation(instance):
    assert isinstance(instance, esper::RuleParts)

@given(instance=esper::Domainmodel_strategy)
@settings(max_examples=50)
def test_esper::domainmodel_instantiation(instance):
    assert isinstance(instance, esper::Domainmodel)
