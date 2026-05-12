import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    esper2Maude_SelectEntry,
    esper2Maude_Field,
    esper2Maude_ComparisonOperator,
    esper2Maude_LogicalOperator,
    esper2Maude_FollowedBy,
    esper2Maude_FilterPart,
    esper2Maude_Every,
    esper2Maude_SubFilterFollowedBy,
    esper2Maude_EventProperty,
    esper2Maude_Pattern,
    esper2Maude_Schema,
    esper2Maude_Model,
    esper2Maude_FilterOperator,
    esper2Maude_FilterEvent,
    esper2Maude_WhereFilter,
    esper2Maude_Window,
    esper2Maude_FilterFrom,
    esper2Maude_LastSelectEntry,
    esper2Maude_NonLastSelectEntry,
    esper2Maude_Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esper2maude_selectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_SelectEntry)


def test_esper2maude_selectentry_constructor_exists():
    assert callable(esper2Maude_SelectEntry.__init__)


def test_esper2maude_selectentry_constructor_args():
    sig = inspect.signature(esper2Maude_SelectEntry.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "groupOp" in params, "Missing parameter 'groupOp'"

def test_esper2maude_selectentry_has_alias():
    assert hasattr(esper2Maude_SelectEntry, "alias")
    descriptor = None
    for klass in esper2Maude_SelectEntry.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_selectentry_has_groupOp():
    assert hasattr(esper2Maude_SelectEntry, "groupOp")
    descriptor = None
    for klass in esper2Maude_SelectEntry.__mro__:
        if "groupOp" in klass.__dict__:
            descriptor = klass.__dict__["groupOp"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_field_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Field)


def test_esper2maude_field_constructor_exists():
    assert callable(esper2Maude_Field.__init__)


def test_esper2maude_field_constructor_args():
    sig = inspect.signature(esper2Maude_Field.__init__)
    params = list(sig.parameters.keys())
    assert "star" in params, "Missing parameter 'star'"
    assert "eventPropName" in params, "Missing parameter 'eventPropName'"
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"

def test_esper2maude_field_has_star():
    assert hasattr(esper2Maude_Field, "star")
    descriptor = None
    for klass in esper2Maude_Field.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_field_has_eventPropName():
    assert hasattr(esper2Maude_Field, "eventPropName")
    descriptor = None
    for klass in esper2Maude_Field.__mro__:
        if "eventPropName" in klass.__dict__:
            descriptor = klass.__dict__["eventPropName"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_field_has_eventVariable():
    assert hasattr(esper2Maude_Field, "eventVariable")
    descriptor = None
    for klass in esper2Maude_Field.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_ComparisonOperator)


def test_esper2maude_comparisonoperator_constructor_exists():
    assert callable(esper2Maude_ComparisonOperator.__init__)


def test_esper2maude_comparisonoperator_constructor_args():
    sig = inspect.signature(esper2Maude_ComparisonOperator.__init__)
    params = list(sig.parameters.keys())
    assert "eq" in params, "Missing parameter 'eq'"
    assert "ge" in params, "Missing parameter 'ge'"
    assert "lt" in params, "Missing parameter 'lt'"
    assert "le" in params, "Missing parameter 'le'"
    assert "neq" in params, "Missing parameter 'neq'"
    assert "gt" in params, "Missing parameter 'gt'"

def test_esper2maude_comparisonoperator_has_eq():
    assert hasattr(esper2Maude_ComparisonOperator, "eq")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_comparisonoperator_has_ge():
    assert hasattr(esper2Maude_ComparisonOperator, "ge")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "ge" in klass.__dict__:
            descriptor = klass.__dict__["ge"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_comparisonoperator_has_lt():
    assert hasattr(esper2Maude_ComparisonOperator, "lt")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "lt" in klass.__dict__:
            descriptor = klass.__dict__["lt"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_comparisonoperator_has_le():
    assert hasattr(esper2Maude_ComparisonOperator, "le")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "le" in klass.__dict__:
            descriptor = klass.__dict__["le"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_comparisonoperator_has_neq():
    assert hasattr(esper2Maude_ComparisonOperator, "neq")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "neq" in klass.__dict__:
            descriptor = klass.__dict__["neq"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_comparisonoperator_has_gt():
    assert hasattr(esper2Maude_ComparisonOperator, "gt")
    descriptor = None
    for klass in esper2Maude_ComparisonOperator.__mro__:
        if "gt" in klass.__dict__:
            descriptor = klass.__dict__["gt"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_logicaloperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_LogicalOperator)


def test_esper2maude_logicaloperator_constructor_exists():
    assert callable(esper2Maude_LogicalOperator.__init__)


def test_esper2maude_logicaloperator_constructor_args():
    sig = inspect.signature(esper2Maude_LogicalOperator.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"
    assert "and_" in params, "Missing parameter 'and_'"

def test_esper2maude_logicaloperator_has_or_():
    assert hasattr(esper2Maude_LogicalOperator, "or_")
    descriptor = None
    for klass in esper2Maude_LogicalOperator.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_logicaloperator_has_and_():
    assert hasattr(esper2Maude_LogicalOperator, "and_")
    descriptor = None
    for klass in esper2Maude_LogicalOperator.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_followedby_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_FollowedBy)


def test_esper2maude_followedby_constructor_exists():
    assert callable(esper2Maude_FollowedBy.__init__)


def test_esper2maude_followedby_constructor_args():
    sig = inspect.signature(esper2Maude_FollowedBy.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_filterpart_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_FilterPart)


def test_esper2maude_filterpart_constructor_exists():
    assert callable(esper2Maude_FilterPart.__init__)


def test_esper2maude_filterpart_constructor_args():
    sig = inspect.signature(esper2Maude_FilterPart.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "dec" in params, "Missing parameter 'dec'"
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "str" in params, "Missing parameter 'str'"
    assert "neg" in params, "Missing parameter 'neg'"
    assert "f" in params, "Missing parameter 'f'"
    assert "t" in params, "Missing parameter 't'"
    assert "eventPropName" in params, "Missing parameter 'eventPropName'"

def test_esper2maude_filterpart_has_num():
    assert hasattr(esper2Maude_FilterPart, "num")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_dec():
    assert hasattr(esper2Maude_FilterPart, "dec")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "dec" in klass.__dict__:
            descriptor = klass.__dict__["dec"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_eventVariable():
    assert hasattr(esper2Maude_FilterPart, "eventVariable")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_str():
    assert hasattr(esper2Maude_FilterPart, "str")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_neg():
    assert hasattr(esper2Maude_FilterPart, "neg")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_f():
    assert hasattr(esper2Maude_FilterPart, "f")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_t():
    assert hasattr(esper2Maude_FilterPart, "t")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "t" in klass.__dict__:
            descriptor = klass.__dict__["t"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterpart_has_eventPropName():
    assert hasattr(esper2Maude_FilterPart, "eventPropName")
    descriptor = None
    for klass in esper2Maude_FilterPart.__mro__:
        if "eventPropName" in klass.__dict__:
            descriptor = klass.__dict__["eventPropName"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_every_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Every)


def test_esper2maude_every_constructor_exists():
    assert callable(esper2Maude_Every.__init__)


def test_esper2maude_every_constructor_args():
    sig = inspect.signature(esper2Maude_Every.__init__)
    params = list(sig.parameters.keys())
    assert "eventName" in params, "Missing parameter 'eventName'"
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"

def test_esper2maude_every_has_eventName():
    assert hasattr(esper2Maude_Every, "eventName")
    descriptor = None
    for klass in esper2Maude_Every.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_every_has_eventVariable():
    assert hasattr(esper2Maude_Every, "eventVariable")
    descriptor = None
    for klass in esper2Maude_Every.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_subfilterfollowedby_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_SubFilterFollowedBy)


def test_esper2maude_subfilterfollowedby_constructor_exists():
    assert callable(esper2Maude_SubFilterFollowedBy.__init__)


def test_esper2maude_subfilterfollowedby_constructor_args():
    sig = inspect.signature(esper2Maude_SubFilterFollowedBy.__init__)
    params = list(sig.parameters.keys())
    assert "eventName" in params, "Missing parameter 'eventName'"
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"

def test_esper2maude_subfilterfollowedby_has_eventName():
    assert hasattr(esper2Maude_SubFilterFollowedBy, "eventName")
    descriptor = None
    for klass in esper2Maude_SubFilterFollowedBy.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_subfilterfollowedby_has_eventVariable():
    assert hasattr(esper2Maude_SubFilterFollowedBy, "eventVariable")
    descriptor = None
    for klass in esper2Maude_SubFilterFollowedBy.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_eventproperty_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_EventProperty)


def test_esper2maude_eventproperty_constructor_exists():
    assert callable(esper2Maude_EventProperty.__init__)


def test_esper2maude_eventproperty_constructor_args():
    sig = inspect.signature(esper2Maude_EventProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_esper2maude_eventproperty_has_name():
    assert hasattr(esper2Maude_EventProperty, "name")
    descriptor = None
    for klass in esper2Maude_EventProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_eventproperty_has_type():
    assert hasattr(esper2Maude_EventProperty, "type")
    descriptor = None
    for klass in esper2Maude_EventProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_pattern_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Pattern)


def test_esper2maude_pattern_constructor_exists():
    assert callable(esper2Maude_Pattern.__init__)


def test_esper2maude_pattern_constructor_args():
    sig = inspect.signature(esper2Maude_Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "num" in params, "Missing parameter 'num'"

def test_esper2maude_pattern_has_name():
    assert hasattr(esper2Maude_Pattern, "name")
    descriptor = None
    for klass in esper2Maude_Pattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_pattern_has_num():
    assert hasattr(esper2Maude_Pattern, "num")
    descriptor = None
    for klass in esper2Maude_Pattern.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_schema_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Schema)


def test_esper2maude_schema_constructor_exists():
    assert callable(esper2Maude_Schema.__init__)


def test_esper2maude_schema_constructor_args():
    sig = inspect.signature(esper2Maude_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude_schema_has_name():
    assert hasattr(esper2Maude_Schema, "name")
    descriptor = None
    for klass in esper2Maude_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_model_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Model)


def test_esper2maude_model_constructor_exists():
    assert callable(esper2Maude_Model.__init__)


def test_esper2maude_model_constructor_args():
    sig = inspect.signature(esper2Maude_Model.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_filteroperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_FilterOperator)


def test_esper2maude_filteroperator_constructor_exists():
    assert callable(esper2Maude_FilterOperator.__init__)


def test_esper2maude_filteroperator_constructor_args():
    sig = inspect.signature(esper2Maude_FilterOperator.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_filterevent_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_FilterEvent)


def test_esper2maude_filterevent_constructor_exists():
    assert callable(esper2Maude_FilterEvent.__init__)


def test_esper2maude_filterevent_constructor_args():
    sig = inspect.signature(esper2Maude_FilterEvent.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_wherefilter_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_WhereFilter)


def test_esper2maude_wherefilter_constructor_exists():
    assert callable(esper2Maude_WhereFilter.__init__)


def test_esper2maude_wherefilter_constructor_args():
    sig = inspect.signature(esper2Maude_WhereFilter.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "timer" in params, "Missing parameter 'timer'"

def test_esper2maude_wherefilter_has_num():
    assert hasattr(esper2Maude_WhereFilter, "num")
    descriptor = None
    for klass in esper2Maude_WhereFilter.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_wherefilter_has_timer():
    assert hasattr(esper2Maude_WhereFilter, "timer")
    descriptor = None
    for klass in esper2Maude_WhereFilter.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_window_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Window)


def test_esper2maude_window_constructor_exists():
    assert callable(esper2Maude_Window.__init__)


def test_esper2maude_window_constructor_args():
    sig = inspect.signature(esper2Maude_Window.__init__)
    params = list(sig.parameters.keys())
    assert "typeBatch" in params, "Missing parameter 'typeBatch'"
    assert "num" in params, "Missing parameter 'num'"
    assert "typeTime" in params, "Missing parameter 'typeTime'"

def test_esper2maude_window_has_typeBatch():
    assert hasattr(esper2Maude_Window, "typeBatch")
    descriptor = None
    for klass in esper2Maude_Window.__mro__:
        if "typeBatch" in klass.__dict__:
            descriptor = klass.__dict__["typeBatch"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_window_has_num():
    assert hasattr(esper2Maude_Window, "num")
    descriptor = None
    for klass in esper2Maude_Window.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_window_has_typeTime():
    assert hasattr(esper2Maude_Window, "typeTime")
    descriptor = None
    for klass in esper2Maude_Window.__mro__:
        if "typeTime" in klass.__dict__:
            descriptor = klass.__dict__["typeTime"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_filterfrom_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_FilterFrom)


def test_esper2maude_filterfrom_constructor_exists():
    assert callable(esper2Maude_FilterFrom.__init__)


def test_esper2maude_filterfrom_constructor_args():
    sig = inspect.signature(esper2Maude_FilterFrom.__init__)
    params = list(sig.parameters.keys())
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "eventName" in params, "Missing parameter 'eventName'"

def test_esper2maude_filterfrom_has_eventVariable():
    assert hasattr(esper2Maude_FilterFrom, "eventVariable")
    descriptor = None
    for klass in esper2Maude_FilterFrom.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude_filterfrom_has_eventName():
    assert hasattr(esper2Maude_FilterFrom, "eventName")
    descriptor = None
    for klass in esper2Maude_FilterFrom.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude_lastselectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_LastSelectEntry)


def test_esper2maude_lastselectentry_constructor_exists():
    assert callable(esper2Maude_LastSelectEntry.__init__)


def test_esper2maude_lastselectentry_constructor_args():
    sig = inspect.signature(esper2Maude_LastSelectEntry.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_nonlastselectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_NonLastSelectEntry)


def test_esper2maude_nonlastselectentry_constructor_exists():
    assert callable(esper2Maude_NonLastSelectEntry.__init__)


def test_esper2maude_nonlastselectentry_constructor_args():
    sig = inspect.signature(esper2Maude_NonLastSelectEntry.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude_event_is_not_abstract():
    assert not inspect.isabstract(esper2Maude_Event)


def test_esper2maude_event_constructor_exists():
    assert callable(esper2Maude_Event.__init__)


def test_esper2maude_event_constructor_args():
    sig = inspect.signature(esper2Maude_Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude_event_has_name():
    assert hasattr(esper2Maude_Event, "name")
    descriptor = None
    for klass in esper2Maude_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
esper2Maude_SelectEntry_strategy = st.builds(
    esper2Maude_SelectEntry,
    alias=
        safe_text,
    groupOp=
        safe_text
)
esper2Maude_Field_strategy = st.builds(
    esper2Maude_Field,
    star=
        safe_text,
    eventPropName=
        safe_text,
    eventVariable=
        safe_text
)
esper2Maude_ComparisonOperator_strategy = st.builds(
    esper2Maude_ComparisonOperator,
    eq=
        safe_text,
    ge=
        safe_text,
    lt=
        safe_text,
    le=
        safe_text,
    neq=
        safe_text,
    gt=
        safe_text
)
esper2Maude_LogicalOperator_strategy = st.builds(
    esper2Maude_LogicalOperator,
    or_=
        safe_text,
    and_=
        safe_text
)
esper2Maude_FollowedBy_strategy = st.builds(
    esper2Maude_FollowedBy,
)
esper2Maude_FilterPart_strategy = st.builds(
    esper2Maude_FilterPart,
    num=
        st.integers(),
    dec=
        st.integers(),
    eventVariable=
        safe_text,
    str=
        safe_text,
    neg=
        safe_text,
    f=
        safe_text,
    t=
        safe_text,
    eventPropName=
        safe_text
)
esper2Maude_Every_strategy = st.builds(
    esper2Maude_Every,
    eventName=
        safe_text,
    eventVariable=
        safe_text
)
esper2Maude_SubFilterFollowedBy_strategy = st.builds(
    esper2Maude_SubFilterFollowedBy,
    eventName=
        safe_text,
    eventVariable=
        safe_text
)
esper2Maude_EventProperty_strategy = st.builds(
    esper2Maude_EventProperty,
    name=
        safe_text,
    type=
        safe_text
)
esper2Maude_Pattern_strategy = st.builds(
    esper2Maude_Pattern,
    name=
        safe_text,
    num=
        st.integers()
)
esper2Maude_Schema_strategy = st.builds(
    esper2Maude_Schema,
    name=
        safe_text
)
esper2Maude_Model_strategy = st.builds(
    esper2Maude_Model,
)
esper2Maude_FilterOperator_strategy = st.builds(
    esper2Maude_FilterOperator,
)
esper2Maude_FilterEvent_strategy = st.builds(
    esper2Maude_FilterEvent,
)
esper2Maude_WhereFilter_strategy = st.builds(
    esper2Maude_WhereFilter,
    num=
        st.integers(),
    timer=
        safe_text
)
esper2Maude_Window_strategy = st.builds(
    esper2Maude_Window,
    typeBatch=
        safe_text,
    num=
        st.integers(),
    typeTime=
        safe_text
)
esper2Maude_FilterFrom_strategy = st.builds(
    esper2Maude_FilterFrom,
    eventVariable=
        safe_text,
    eventName=
        safe_text
)
esper2Maude_LastSelectEntry_strategy = st.builds(
    esper2Maude_LastSelectEntry,
)
esper2Maude_NonLastSelectEntry_strategy = st.builds(
    esper2Maude_NonLastSelectEntry,
)
esper2Maude_Event_strategy = st.builds(
    esper2Maude_Event,
    name=
        safe_text
)

@given(instance=esper2Maude_SelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude_selectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude_SelectEntry)



@given(instance=esper2Maude_SelectEntry_strategy)
def test_esper2maude_selectentry_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=esper2Maude_SelectEntry_strategy)
def test_esper2maude_selectentry_groupOp_setter(instance):
    original = instance.groupOp
    instance.groupOp = original
    assert instance.groupOp == original

@given(instance=esper2Maude_Field_strategy)
@settings(max_examples=50)
def test_esper2maude_field_instantiation(instance):
    assert isinstance(instance, esper2Maude_Field)



@given(instance=esper2Maude_Field_strategy)
def test_esper2maude_field_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original



@given(instance=esper2Maude_Field_strategy)
def test_esper2maude_field_eventPropName_setter(instance):
    original = instance.eventPropName
    instance.eventPropName = original
    assert instance.eventPropName == original



@given(instance=esper2Maude_Field_strategy)
def test_esper2maude_field_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude_ComparisonOperator_strategy)
@settings(max_examples=50)
def test_esper2maude_comparisonoperator_instantiation(instance):
    assert isinstance(instance, esper2Maude_ComparisonOperator)



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_ge_setter(instance):
    original = instance.ge
    instance.ge = original
    assert instance.ge == original



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_lt_setter(instance):
    original = instance.lt
    instance.lt = original
    assert instance.lt == original



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_le_setter(instance):
    original = instance.le
    instance.le = original
    assert instance.le == original



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_neq_setter(instance):
    original = instance.neq
    instance.neq = original
    assert instance.neq == original



@given(instance=esper2Maude_ComparisonOperator_strategy)
def test_esper2maude_comparisonoperator_gt_setter(instance):
    original = instance.gt
    instance.gt = original
    assert instance.gt == original

@given(instance=esper2Maude_LogicalOperator_strategy)
@settings(max_examples=50)
def test_esper2maude_logicaloperator_instantiation(instance):
    assert isinstance(instance, esper2Maude_LogicalOperator)



@given(instance=esper2Maude_LogicalOperator_strategy)
def test_esper2maude_logicaloperator_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original



@given(instance=esper2Maude_LogicalOperator_strategy)
def test_esper2maude_logicaloperator_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=esper2Maude_FollowedBy_strategy)
@settings(max_examples=50)
def test_esper2maude_followedby_instantiation(instance):
    assert isinstance(instance, esper2Maude_FollowedBy)

@given(instance=esper2Maude_FilterPart_strategy)
@settings(max_examples=50)
def test_esper2maude_filterpart_instantiation(instance):
    assert isinstance(instance, esper2Maude_FilterPart)



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_dec_setter(instance):
    original = instance.dec
    instance.dec = original
    assert instance.dec == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original



@given(instance=esper2Maude_FilterPart_strategy)
def test_esper2maude_filterpart_eventPropName_setter(instance):
    original = instance.eventPropName
    instance.eventPropName = original
    assert instance.eventPropName == original

@given(instance=esper2Maude_Every_strategy)
@settings(max_examples=50)
def test_esper2maude_every_instantiation(instance):
    assert isinstance(instance, esper2Maude_Every)



@given(instance=esper2Maude_Every_strategy)
def test_esper2maude_every_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original



@given(instance=esper2Maude_Every_strategy)
def test_esper2maude_every_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude_SubFilterFollowedBy_strategy)
@settings(max_examples=50)
def test_esper2maude_subfilterfollowedby_instantiation(instance):
    assert isinstance(instance, esper2Maude_SubFilterFollowedBy)



@given(instance=esper2Maude_SubFilterFollowedBy_strategy)
def test_esper2maude_subfilterfollowedby_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original



@given(instance=esper2Maude_SubFilterFollowedBy_strategy)
def test_esper2maude_subfilterfollowedby_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude_EventProperty_strategy)
@settings(max_examples=50)
def test_esper2maude_eventproperty_instantiation(instance):
    assert isinstance(instance, esper2Maude_EventProperty)



@given(instance=esper2Maude_EventProperty_strategy)
def test_esper2maude_eventproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esper2Maude_EventProperty_strategy)
def test_esper2maude_eventproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=esper2Maude_Pattern_strategy)
@settings(max_examples=50)
def test_esper2maude_pattern_instantiation(instance):
    assert isinstance(instance, esper2Maude_Pattern)



@given(instance=esper2Maude_Pattern_strategy)
def test_esper2maude_pattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=esper2Maude_Pattern_strategy)
def test_esper2maude_pattern_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=esper2Maude_Schema_strategy)
@settings(max_examples=50)
def test_esper2maude_schema_instantiation(instance):
    assert isinstance(instance, esper2Maude_Schema)



@given(instance=esper2Maude_Schema_strategy)
def test_esper2maude_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper2Maude_Model_strategy)
@settings(max_examples=50)
def test_esper2maude_model_instantiation(instance):
    assert isinstance(instance, esper2Maude_Model)

@given(instance=esper2Maude_FilterOperator_strategy)
@settings(max_examples=50)
def test_esper2maude_filteroperator_instantiation(instance):
    assert isinstance(instance, esper2Maude_FilterOperator)

@given(instance=esper2Maude_FilterEvent_strategy)
@settings(max_examples=50)
def test_esper2maude_filterevent_instantiation(instance):
    assert isinstance(instance, esper2Maude_FilterEvent)

@given(instance=esper2Maude_WhereFilter_strategy)
@settings(max_examples=50)
def test_esper2maude_wherefilter_instantiation(instance):
    assert isinstance(instance, esper2Maude_WhereFilter)



@given(instance=esper2Maude_WhereFilter_strategy)
def test_esper2maude_wherefilter_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=esper2Maude_WhereFilter_strategy)
def test_esper2maude_wherefilter_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original

@given(instance=esper2Maude_Window_strategy)
@settings(max_examples=50)
def test_esper2maude_window_instantiation(instance):
    assert isinstance(instance, esper2Maude_Window)



@given(instance=esper2Maude_Window_strategy)
def test_esper2maude_window_typeBatch_setter(instance):
    original = instance.typeBatch
    instance.typeBatch = original
    assert instance.typeBatch == original



@given(instance=esper2Maude_Window_strategy)
def test_esper2maude_window_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=esper2Maude_Window_strategy)
def test_esper2maude_window_typeTime_setter(instance):
    original = instance.typeTime
    instance.typeTime = original
    assert instance.typeTime == original

@given(instance=esper2Maude_FilterFrom_strategy)
@settings(max_examples=50)
def test_esper2maude_filterfrom_instantiation(instance):
    assert isinstance(instance, esper2Maude_FilterFrom)



@given(instance=esper2Maude_FilterFrom_strategy)
def test_esper2maude_filterfrom_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original



@given(instance=esper2Maude_FilterFrom_strategy)
def test_esper2maude_filterfrom_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=esper2Maude_LastSelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude_lastselectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude_LastSelectEntry)

@given(instance=esper2Maude_NonLastSelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude_nonlastselectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude_NonLastSelectEntry)

@given(instance=esper2Maude_Event_strategy)
@settings(max_examples=50)
def test_esper2maude_event_instantiation(instance):
    assert isinstance(instance, esper2Maude_Event)



@given(instance=esper2Maude_Event_strategy)
def test_esper2maude_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
