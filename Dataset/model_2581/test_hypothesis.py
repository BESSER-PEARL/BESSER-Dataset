import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    esper_ExtraParenthesisRule,
    esper_Win,
    esper_JoinFollowBy,
    ExtraParenthesisRule,
    esper_Timer,
    esper_KindOfEvent,
    esper_TerminalExpression,
    esper_FollowByWhere,
    esper_FollowBy,
    esper_AbstractFollowBy,
    esper_Pattern,
    esper_Anything,
    esper_SingleDefinition,
    esper_DefaultMethods,
    esper_SingleSelectDefinition,
    esper_KindSelectAttributesDefinition,
    esper_SelectAttributesDefinition,
    esper_Having,
    esper_GroupBy,
    esper_From,
    esper_Select,
    esper_Priority,
    esper_Name,
    esper_AttributesDefinition,
    esper_Attributes,
    KindOfEvent,
    esper_Insert,
    esper_Event,
    esper_RuleParts,
    esper_Domainmodel,
    Operators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esper_extraparenthesisrule_is_not_abstract():
    assert not inspect.isabstract(esper_ExtraParenthesisRule)


def test_esper_extraparenthesisrule_constructor_exists():
    assert callable(esper_ExtraParenthesisRule.__init__)


def test_esper_extraparenthesisrule_constructor_args():
    sig = inspect.signature(esper_ExtraParenthesisRule.__init__)
    params = list(sig.parameters.keys())



def test_esper_win_is_not_abstract():
    assert not inspect.isabstract(esper_Win)


def test_esper_win_constructor_exists():
    assert callable(esper_Win.__init__)


def test_esper_win_constructor_args():
    sig = inspect.signature(esper_Win.__init__)
    params = list(sig.parameters.keys())



def test_esper_joinfollowby_is_not_abstract():
    assert not inspect.isabstract(esper_JoinFollowBy)


def test_esper_joinfollowby_constructor_exists():
    assert callable(esper_JoinFollowBy.__init__)


def test_esper_joinfollowby_constructor_args():
    sig = inspect.signature(esper_JoinFollowBy.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper_joinfollowby_has_operator():
    assert hasattr(esper_JoinFollowBy, "operator")
    descriptor = None
    for klass in esper_JoinFollowBy.__mro__:
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



def test_esper_timer_is_not_abstract():
    assert not inspect.isabstract(esper_Timer)


def test_esper_timer_constructor_exists():
    assert callable(esper_Timer.__init__)


def test_esper_timer_constructor_args():
    sig = inspect.signature(esper_Timer.__init__)
    params = list(sig.parameters.keys())



def test_esper_kindofevent_is_not_abstract():
    assert not inspect.isabstract(esper_KindOfEvent)


def test_esper_kindofevent_constructor_exists():
    assert callable(esper_KindOfEvent.__init__)


def test_esper_kindofevent_constructor_args():
    sig = inspect.signature(esper_KindOfEvent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper_kindofevent_has_name():
    assert hasattr(esper_KindOfEvent, "name")
    descriptor = None
    for klass in esper_KindOfEvent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper_terminalexpression_is_not_abstract():
    assert not inspect.isabstract(esper_TerminalExpression)


def test_esper_terminalexpression_constructor_exists():
    assert callable(esper_TerminalExpression.__init__)


def test_esper_terminalexpression_constructor_args():
    sig = inspect.signature(esper_TerminalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "parenthesis" in params, "Missing parameter 'parenthesis'"
    assert "every" in params, "Missing parameter 'every'"

def test_esper_terminalexpression_has_parenthesis():
    assert hasattr(esper_TerminalExpression, "parenthesis")
    descriptor = None
    for klass in esper_TerminalExpression.__mro__:
        if "parenthesis" in klass.__dict__:
            descriptor = klass.__dict__["parenthesis"]
            break
    assert isinstance(descriptor, property)

def test_esper_terminalexpression_has_every():
    assert hasattr(esper_TerminalExpression, "every")
    descriptor = None
    for klass in esper_TerminalExpression.__mro__:
        if "every" in klass.__dict__:
            descriptor = klass.__dict__["every"]
            break
    assert isinstance(descriptor, property)



def test_esper_followbywhere_is_not_abstract():
    assert not inspect.isabstract(esper_FollowByWhere)


def test_esper_followbywhere_constructor_exists():
    assert callable(esper_FollowByWhere.__init__)


def test_esper_followbywhere_constructor_args():
    sig = inspect.signature(esper_FollowByWhere.__init__)
    params = list(sig.parameters.keys())



def test_esper_followby_is_not_abstract():
    assert not inspect.isabstract(esper_FollowBy)


def test_esper_followby_constructor_exists():
    assert callable(esper_FollowBy.__init__)


def test_esper_followby_constructor_args():
    sig = inspect.signature(esper_FollowBy.__init__)
    params = list(sig.parameters.keys())



def test_esper_abstractfollowby_is_not_abstract():
    assert not inspect.isabstract(esper_AbstractFollowBy)


def test_esper_abstractfollowby_constructor_exists():
    assert callable(esper_AbstractFollowBy.__init__)


def test_esper_abstractfollowby_constructor_args():
    sig = inspect.signature(esper_AbstractFollowBy.__init__)
    params = list(sig.parameters.keys())



def test_esper_pattern_is_not_abstract():
    assert not inspect.isabstract(esper_Pattern)


def test_esper_pattern_constructor_exists():
    assert callable(esper_Pattern.__init__)


def test_esper_pattern_constructor_args():
    sig = inspect.signature(esper_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_esper_anything_is_not_abstract():
    assert not inspect.isabstract(esper_Anything)


def test_esper_anything_constructor_exists():
    assert callable(esper_Anything.__init__)


def test_esper_anything_constructor_args():
    sig = inspect.signature(esper_Anything.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper_anything_has_operator():
    assert hasattr(esper_Anything, "operator")
    descriptor = None
    for klass in esper_Anything.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper_singledefinition_is_not_abstract():
    assert not inspect.isabstract(esper_SingleDefinition)


def test_esper_singledefinition_constructor_exists():
    assert callable(esper_SingleDefinition.__init__)


def test_esper_singledefinition_constructor_args():
    sig = inspect.signature(esper_SingleDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper_singledefinition_has_name():
    assert hasattr(esper_SingleDefinition, "name")
    descriptor = None
    for klass in esper_SingleDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper_defaultmethods_is_not_abstract():
    assert not inspect.isabstract(esper_DefaultMethods)


def test_esper_defaultmethods_constructor_exists():
    assert callable(esper_DefaultMethods.__init__)


def test_esper_defaultmethods_constructor_args():
    sig = inspect.signature(esper_DefaultMethods.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper_defaultmethods_has_name():
    assert hasattr(esper_DefaultMethods, "name")
    descriptor = None
    for klass in esper_DefaultMethods.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper_singleselectdefinition_is_not_abstract():
    assert not inspect.isabstract(esper_SingleSelectDefinition)


def test_esper_singleselectdefinition_constructor_exists():
    assert callable(esper_SingleSelectDefinition.__init__)


def test_esper_singleselectdefinition_constructor_args():
    sig = inspect.signature(esper_SingleSelectDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_esper_singleselectdefinition_has_attribute():
    assert hasattr(esper_SingleSelectDefinition, "attribute")
    descriptor = None
    for klass in esper_SingleSelectDefinition.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_esper_kindselectattributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper_KindSelectAttributesDefinition)


def test_esper_kindselectattributesdefinition_constructor_exists():
    assert callable(esper_KindSelectAttributesDefinition.__init__)


def test_esper_kindselectattributesdefinition_constructor_args():
    sig = inspect.signature(esper_KindSelectAttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "int" in params, "Missing parameter 'int'"

def test_esper_kindselectattributesdefinition_has_string():
    assert hasattr(esper_KindSelectAttributesDefinition, "string")
    descriptor = None
    for klass in esper_KindSelectAttributesDefinition.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_esper_kindselectattributesdefinition_has_int():
    assert hasattr(esper_KindSelectAttributesDefinition, "int")
    descriptor = None
    for klass in esper_KindSelectAttributesDefinition.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_esper_selectattributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper_SelectAttributesDefinition)


def test_esper_selectattributesdefinition_constructor_exists():
    assert callable(esper_SelectAttributesDefinition.__init__)


def test_esper_selectattributesdefinition_constructor_args():
    sig = inspect.signature(esper_SelectAttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper_selectattributesdefinition_has_operator():
    assert hasattr(esper_SelectAttributesDefinition, "operator")
    descriptor = None
    for klass in esper_SelectAttributesDefinition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper_having_is_not_abstract():
    assert not inspect.isabstract(esper_Having)


def test_esper_having_constructor_exists():
    assert callable(esper_Having.__init__)


def test_esper_having_constructor_args():
    sig = inspect.signature(esper_Having.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_esper_having_has_operator():
    assert hasattr(esper_Having, "operator")
    descriptor = None
    for klass in esper_Having.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_esper_groupby_is_not_abstract():
    assert not inspect.isabstract(esper_GroupBy)


def test_esper_groupby_constructor_exists():
    assert callable(esper_GroupBy.__init__)


def test_esper_groupby_constructor_args():
    sig = inspect.signature(esper_GroupBy.__init__)
    params = list(sig.parameters.keys())



def test_esper_from_is_not_abstract():
    assert not inspect.isabstract(esper_From)


def test_esper_from_constructor_exists():
    assert callable(esper_From.__init__)


def test_esper_from_constructor_args():
    sig = inspect.signature(esper_From.__init__)
    params = list(sig.parameters.keys())



def test_esper_select_is_not_abstract():
    assert not inspect.isabstract(esper_Select)


def test_esper_select_constructor_exists():
    assert callable(esper_Select.__init__)


def test_esper_select_constructor_args():
    sig = inspect.signature(esper_Select.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "asterisk" in params, "Missing parameter 'asterisk'"

def test_esper_select_has_alias():
    assert hasattr(esper_Select, "alias")
    descriptor = None
    for klass in esper_Select.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_esper_select_has_asterisk():
    assert hasattr(esper_Select, "asterisk")
    descriptor = None
    for klass in esper_Select.__mro__:
        if "asterisk" in klass.__dict__:
            descriptor = klass.__dict__["asterisk"]
            break
    assert isinstance(descriptor, property)



def test_esper_priority_is_not_abstract():
    assert not inspect.isabstract(esper_Priority)


def test_esper_priority_constructor_exists():
    assert callable(esper_Priority.__init__)


def test_esper_priority_constructor_args():
    sig = inspect.signature(esper_Priority.__init__)
    params = list(sig.parameters.keys())
    assert "priorityInt" in params, "Missing parameter 'priorityInt'"

def test_esper_priority_has_priorityInt():
    assert hasattr(esper_Priority, "priorityInt")
    descriptor = None
    for klass in esper_Priority.__mro__:
        if "priorityInt" in klass.__dict__:
            descriptor = klass.__dict__["priorityInt"]
            break
    assert isinstance(descriptor, property)



def test_esper_name_is_not_abstract():
    assert not inspect.isabstract(esper_Name)


def test_esper_name_constructor_exists():
    assert callable(esper_Name.__init__)


def test_esper_name_constructor_args():
    sig = inspect.signature(esper_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper_name_has_name():
    assert hasattr(esper_Name, "name")
    descriptor = None
    for klass in esper_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper_attributesdefinition_is_not_abstract():
    assert not inspect.isabstract(esper_AttributesDefinition)


def test_esper_attributesdefinition_constructor_exists():
    assert callable(esper_AttributesDefinition.__init__)


def test_esper_attributesdefinition_constructor_args():
    sig = inspect.signature(esper_AttributesDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_esper_attributesdefinition_has_type():
    assert hasattr(esper_AttributesDefinition, "type")
    descriptor = None
    for klass in esper_AttributesDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_esper_attributesdefinition_has_name():
    assert hasattr(esper_AttributesDefinition, "name")
    descriptor = None
    for klass in esper_AttributesDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper_attributes_is_not_abstract():
    assert not inspect.isabstract(esper_Attributes)


def test_esper_attributes_constructor_exists():
    assert callable(esper_Attributes.__init__)


def test_esper_attributes_constructor_args():
    sig = inspect.signature(esper_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_kindofevent_is_not_abstract():
    assert not inspect.isabstract(KindOfEvent)


def test_kindofevent_constructor_exists():
    assert callable(KindOfEvent.__init__)


def test_kindofevent_constructor_args():
    sig = inspect.signature(KindOfEvent.__init__)
    params = list(sig.parameters.keys())



def test_esper_insert_is_not_abstract():
    assert not inspect.isabstract(esper_Insert)


def test_esper_insert_constructor_exists():
    assert callable(esper_Insert.__init__)


def test_esper_insert_constructor_args():
    sig = inspect.signature(esper_Insert.__init__)
    params = list(sig.parameters.keys())



def test_esper_event_is_not_abstract():
    assert not inspect.isabstract(esper_Event)


def test_esper_event_constructor_exists():
    assert callable(esper_Event.__init__)


def test_esper_event_constructor_args():
    sig = inspect.signature(esper_Event.__init__)
    params = list(sig.parameters.keys())



def test_esper_ruleparts_is_not_abstract():
    assert not inspect.isabstract(esper_RuleParts)


def test_esper_ruleparts_constructor_exists():
    assert callable(esper_RuleParts.__init__)


def test_esper_ruleparts_constructor_args():
    sig = inspect.signature(esper_RuleParts.__init__)
    params = list(sig.parameters.keys())



def test_esper_domainmodel_is_not_abstract():
    assert not inspect.isabstract(esper_Domainmodel)


def test_esper_domainmodel_constructor_exists():
    assert callable(esper_Domainmodel.__init__)


def test_esper_domainmodel_constructor_args():
    sig = inspect.signature(esper_Domainmodel.__init__)
    params = list(sig.parameters.keys())

def test_operators_exists():
    # Check that the Enumeration exists
    assert Operators is not None

def test_operators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Operators]
    expected_literals = [
        "notIn",
        "or_",
        "between",
        "minus",
        "multiplication",
        "moreEqualThan",
        "moreThan",
        "equal",
        "and_",
        "not_",
        "lessEqualThan",
        "plus",
        "lessThan",
        "in_",
        "isnot",
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
esper_ExtraParenthesisRule_strategy = st.builds(
    esper_ExtraParenthesisRule,
)
esper_Win_strategy = st.builds(
    esper_Win,
)
esper_JoinFollowBy_strategy = st.builds(
    esper_JoinFollowBy,
    operator=
        safe_text
)
ExtraParenthesisRule_strategy = st.builds(
    ExtraParenthesisRule,
)
esper_Timer_strategy = st.builds(
    esper_Timer,
)
esper_KindOfEvent_strategy = st.builds(
    esper_KindOfEvent,
    name=
        safe_text
)
esper_TerminalExpression_strategy = st.builds(
    esper_TerminalExpression,
    parenthesis=
        st.booleans(),
    every=
        st.booleans()
)
esper_FollowByWhere_strategy = st.builds(
    esper_FollowByWhere,
)
esper_FollowBy_strategy = st.builds(
    esper_FollowBy,
)
esper_AbstractFollowBy_strategy = st.builds(
    esper_AbstractFollowBy,
)
esper_Pattern_strategy = st.builds(
    esper_Pattern,
)
esper_Anything_strategy = st.builds(
    esper_Anything,
    operator=
        safe_text
)
esper_SingleDefinition_strategy = st.builds(
    esper_SingleDefinition,
    name=
        safe_text
)
esper_DefaultMethods_strategy = st.builds(
    esper_DefaultMethods,
    name=
        safe_text
)
esper_SingleSelectDefinition_strategy = st.builds(
    esper_SingleSelectDefinition,
    attribute=
        safe_text
)
esper_KindSelectAttributesDefinition_strategy = st.builds(
    esper_KindSelectAttributesDefinition,
    string=
        safe_text,
    int=
        st.integers()
)
esper_SelectAttributesDefinition_strategy = st.builds(
    esper_SelectAttributesDefinition,
    operator=
        safe_text
)
esper_Having_strategy = st.builds(
    esper_Having,
    operator=
        safe_text
)
esper_GroupBy_strategy = st.builds(
    esper_GroupBy,
)
esper_From_strategy = st.builds(
    esper_From,
)
esper_Select_strategy = st.builds(
    esper_Select,
    alias=
        safe_text,
    asterisk=
        st.booleans()
)
esper_Priority_strategy = st.builds(
    esper_Priority,
    priorityInt=
        st.integers()
)
esper_Name_strategy = st.builds(
    esper_Name,
    name=
        safe_text
)
esper_AttributesDefinition_strategy = st.builds(
    esper_AttributesDefinition,
    type=
        safe_text,
    name=
        safe_text
)
esper_Attributes_strategy = st.builds(
    esper_Attributes,
)
KindOfEvent_strategy = st.builds(
    KindOfEvent,
)
esper_Insert_strategy = st.builds(
    esper_Insert,
)
esper_Event_strategy = st.builds(
    esper_Event,
)
esper_RuleParts_strategy = st.builds(
    esper_RuleParts,
)
esper_Domainmodel_strategy = st.builds(
    esper_Domainmodel,
)

@given(instance=esper_ExtraParenthesisRule_strategy)
@settings(max_examples=50)
def test_esper_extraparenthesisrule_instantiation(instance):
    assert isinstance(instance, esper_ExtraParenthesisRule)

@given(instance=esper_Win_strategy)
@settings(max_examples=50)
def test_esper_win_instantiation(instance):
    assert isinstance(instance, esper_Win)

@given(instance=esper_JoinFollowBy_strategy)
@settings(max_examples=50)
def test_esper_joinfollowby_instantiation(instance):
    assert isinstance(instance, esper_JoinFollowBy)



@given(instance=esper_JoinFollowBy_strategy)
def test_esper_joinfollowby_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ExtraParenthesisRule_strategy)
@settings(max_examples=50)
def test_extraparenthesisrule_instantiation(instance):
    assert isinstance(instance, ExtraParenthesisRule)

@given(instance=esper_Timer_strategy)
@settings(max_examples=50)
def test_esper_timer_instantiation(instance):
    assert isinstance(instance, esper_Timer)

@given(instance=esper_KindOfEvent_strategy)
@settings(max_examples=50)
def test_esper_kindofevent_instantiation(instance):
    assert isinstance(instance, esper_KindOfEvent)



@given(instance=esper_KindOfEvent_strategy)
def test_esper_kindofevent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper_TerminalExpression_strategy)
@settings(max_examples=50)
def test_esper_terminalexpression_instantiation(instance):
    assert isinstance(instance, esper_TerminalExpression)



@given(instance=esper_TerminalExpression_strategy)
def test_esper_terminalexpression_parenthesis_setter(instance):
    original = instance.parenthesis
    instance.parenthesis = original
    assert instance.parenthesis == original



@given(instance=esper_TerminalExpression_strategy)
def test_esper_terminalexpression_every_setter(instance):
    original = instance.every
    instance.every = original
    assert instance.every == original

@given(instance=esper_FollowByWhere_strategy)
@settings(max_examples=50)
def test_esper_followbywhere_instantiation(instance):
    assert isinstance(instance, esper_FollowByWhere)

@given(instance=esper_FollowBy_strategy)
@settings(max_examples=50)
def test_esper_followby_instantiation(instance):
    assert isinstance(instance, esper_FollowBy)

@given(instance=esper_AbstractFollowBy_strategy)
@settings(max_examples=50)
def test_esper_abstractfollowby_instantiation(instance):
    assert isinstance(instance, esper_AbstractFollowBy)

@given(instance=esper_Pattern_strategy)
@settings(max_examples=50)
def test_esper_pattern_instantiation(instance):
    assert isinstance(instance, esper_Pattern)

@given(instance=esper_Anything_strategy)
@settings(max_examples=50)
def test_esper_anything_instantiation(instance):
    assert isinstance(instance, esper_Anything)



@given(instance=esper_Anything_strategy)
def test_esper_anything_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper_SingleDefinition_strategy)
@settings(max_examples=50)
def test_esper_singledefinition_instantiation(instance):
    assert isinstance(instance, esper_SingleDefinition)



@given(instance=esper_SingleDefinition_strategy)
def test_esper_singledefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper_DefaultMethods_strategy)
@settings(max_examples=50)
def test_esper_defaultmethods_instantiation(instance):
    assert isinstance(instance, esper_DefaultMethods)



@given(instance=esper_DefaultMethods_strategy)
def test_esper_defaultmethods_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper_SingleSelectDefinition_strategy)
@settings(max_examples=50)
def test_esper_singleselectdefinition_instantiation(instance):
    assert isinstance(instance, esper_SingleSelectDefinition)



@given(instance=esper_SingleSelectDefinition_strategy)
def test_esper_singleselectdefinition_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=esper_KindSelectAttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper_kindselectattributesdefinition_instantiation(instance):
    assert isinstance(instance, esper_KindSelectAttributesDefinition)



@given(instance=esper_KindSelectAttributesDefinition_strategy)
def test_esper_kindselectattributesdefinition_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=esper_KindSelectAttributesDefinition_strategy)
def test_esper_kindselectattributesdefinition_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=esper_SelectAttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper_selectattributesdefinition_instantiation(instance):
    assert isinstance(instance, esper_SelectAttributesDefinition)



@given(instance=esper_SelectAttributesDefinition_strategy)
def test_esper_selectattributesdefinition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper_Having_strategy)
@settings(max_examples=50)
def test_esper_having_instantiation(instance):
    assert isinstance(instance, esper_Having)



@given(instance=esper_Having_strategy)
def test_esper_having_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=esper_GroupBy_strategy)
@settings(max_examples=50)
def test_esper_groupby_instantiation(instance):
    assert isinstance(instance, esper_GroupBy)

@given(instance=esper_From_strategy)
@settings(max_examples=50)
def test_esper_from_instantiation(instance):
    assert isinstance(instance, esper_From)

@given(instance=esper_Select_strategy)
@settings(max_examples=50)
def test_esper_select_instantiation(instance):
    assert isinstance(instance, esper_Select)



@given(instance=esper_Select_strategy)
def test_esper_select_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=esper_Select_strategy)
def test_esper_select_asterisk_setter(instance):
    original = instance.asterisk
    instance.asterisk = original
    assert instance.asterisk == original

@given(instance=esper_Priority_strategy)
@settings(max_examples=50)
def test_esper_priority_instantiation(instance):
    assert isinstance(instance, esper_Priority)



@given(instance=esper_Priority_strategy)
def test_esper_priority_priorityInt_setter(instance):
    original = instance.priorityInt
    instance.priorityInt = original
    assert instance.priorityInt == original

@given(instance=esper_Name_strategy)
@settings(max_examples=50)
def test_esper_name_instantiation(instance):
    assert isinstance(instance, esper_Name)



@given(instance=esper_Name_strategy)
def test_esper_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper_AttributesDefinition_strategy)
@settings(max_examples=50)
def test_esper_attributesdefinition_instantiation(instance):
    assert isinstance(instance, esper_AttributesDefinition)



@given(instance=esper_AttributesDefinition_strategy)
def test_esper_attributesdefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=esper_AttributesDefinition_strategy)
def test_esper_attributesdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper_Attributes_strategy)
@settings(max_examples=50)
def test_esper_attributes_instantiation(instance):
    assert isinstance(instance, esper_Attributes)

@given(instance=KindOfEvent_strategy)
@settings(max_examples=50)
def test_kindofevent_instantiation(instance):
    assert isinstance(instance, KindOfEvent)

@given(instance=esper_Insert_strategy)
@settings(max_examples=50)
def test_esper_insert_instantiation(instance):
    assert isinstance(instance, esper_Insert)

@given(instance=esper_Event_strategy)
@settings(max_examples=50)
def test_esper_event_instantiation(instance):
    assert isinstance(instance, esper_Event)

@given(instance=esper_RuleParts_strategy)
@settings(max_examples=50)
def test_esper_ruleparts_instantiation(instance):
    assert isinstance(instance, esper_RuleParts)

@given(instance=esper_Domainmodel_strategy)
@settings(max_examples=50)
def test_esper_domainmodel_instantiation(instance):
    assert isinstance(instance, esper_Domainmodel)
