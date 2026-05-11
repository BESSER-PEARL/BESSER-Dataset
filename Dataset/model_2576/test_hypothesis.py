import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    esper2Maude::SelectEntry,
    esper2Maude::Field,
    esper2Maude::ComparisonOperator,
    esper2Maude::LogicalOperator,
    esper2Maude::FollowedBy,
    esper2Maude::FilterPart,
    esper2Maude::Every,
    esper2Maude::SubFilterFollowedBy,
    esper2Maude::EventProperty,
    esper2Maude::Pattern,
    esper2Maude::Schema,
    esper2Maude::Model,
    esper2Maude::FilterOperator,
    esper2Maude::FilterEvent,
    esper2Maude::WhereFilter,
    esper2Maude::Window,
    esper2Maude::FilterFrom,
    esper2Maude::LastSelectEntry,
    esper2Maude::NonLastSelectEntry,
    esper2Maude::Event,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_esper2maude::selectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::SelectEntry)


def test_esper2maude::selectentry_constructor_exists():
    assert callable(esper2Maude::SelectEntry.__init__)


def test_esper2maude::selectentry_constructor_args():
    sig = inspect.signature(esper2Maude::SelectEntry.__init__)
    params = list(sig.parameters.keys())
    assert "groupOp" in params, "Missing parameter 'groupOp'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_esper2maude::selectentry_has_groupOp():
    assert hasattr(esper2Maude::SelectEntry, "groupOp")
    descriptor = None
    for klass in esper2Maude::SelectEntry.__mro__:
        if "groupOp" in klass.__dict__:
            descriptor = klass.__dict__["groupOp"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::selectentry_has_alias():
    assert hasattr(esper2Maude::SelectEntry, "alias")
    descriptor = None
    for klass in esper2Maude::SelectEntry.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::field_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Field)


def test_esper2maude::field_constructor_exists():
    assert callable(esper2Maude::Field.__init__)


def test_esper2maude::field_constructor_args():
    sig = inspect.signature(esper2Maude::Field.__init__)
    params = list(sig.parameters.keys())
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "eventPropName" in params, "Missing parameter 'eventPropName'"
    assert "star" in params, "Missing parameter 'star'"

def test_esper2maude::field_has_eventVariable():
    assert hasattr(esper2Maude::Field, "eventVariable")
    descriptor = None
    for klass in esper2Maude::Field.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::field_has_eventPropName():
    assert hasattr(esper2Maude::Field, "eventPropName")
    descriptor = None
    for klass in esper2Maude::Field.__mro__:
        if "eventPropName" in klass.__dict__:
            descriptor = klass.__dict__["eventPropName"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::field_has_star():
    assert hasattr(esper2Maude::Field, "star")
    descriptor = None
    for klass in esper2Maude::Field.__mro__:
        if "star" in klass.__dict__:
            descriptor = klass.__dict__["star"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::ComparisonOperator)


def test_esper2maude::comparisonoperator_constructor_exists():
    assert callable(esper2Maude::ComparisonOperator.__init__)


def test_esper2maude::comparisonoperator_constructor_args():
    sig = inspect.signature(esper2Maude::ComparisonOperator.__init__)
    params = list(sig.parameters.keys())
    assert "ge" in params, "Missing parameter 'ge'"
    assert "le" in params, "Missing parameter 'le'"
    assert "lt" in params, "Missing parameter 'lt'"
    assert "neq" in params, "Missing parameter 'neq'"
    assert "eq" in params, "Missing parameter 'eq'"
    assert "gt" in params, "Missing parameter 'gt'"

def test_esper2maude::comparisonoperator_has_ge():
    assert hasattr(esper2Maude::ComparisonOperator, "ge")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "ge" in klass.__dict__:
            descriptor = klass.__dict__["ge"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::comparisonoperator_has_le():
    assert hasattr(esper2Maude::ComparisonOperator, "le")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "le" in klass.__dict__:
            descriptor = klass.__dict__["le"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::comparisonoperator_has_lt():
    assert hasattr(esper2Maude::ComparisonOperator, "lt")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "lt" in klass.__dict__:
            descriptor = klass.__dict__["lt"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::comparisonoperator_has_neq():
    assert hasattr(esper2Maude::ComparisonOperator, "neq")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "neq" in klass.__dict__:
            descriptor = klass.__dict__["neq"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::comparisonoperator_has_eq():
    assert hasattr(esper2Maude::ComparisonOperator, "eq")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::comparisonoperator_has_gt():
    assert hasattr(esper2Maude::ComparisonOperator, "gt")
    descriptor = None
    for klass in esper2Maude::ComparisonOperator.__mro__:
        if "gt" in klass.__dict__:
            descriptor = klass.__dict__["gt"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::logicaloperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::LogicalOperator)


def test_esper2maude::logicaloperator_constructor_exists():
    assert callable(esper2Maude::LogicalOperator.__init__)


def test_esper2maude::logicaloperator_constructor_args():
    sig = inspect.signature(esper2Maude::LogicalOperator.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"
    assert "and_" in params, "Missing parameter 'and_'"

def test_esper2maude::logicaloperator_has_or_():
    assert hasattr(esper2Maude::LogicalOperator, "or_")
    descriptor = None
    for klass in esper2Maude::LogicalOperator.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::logicaloperator_has_and_():
    assert hasattr(esper2Maude::LogicalOperator, "and_")
    descriptor = None
    for klass in esper2Maude::LogicalOperator.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::followedby_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::FollowedBy)


def test_esper2maude::followedby_constructor_exists():
    assert callable(esper2Maude::FollowedBy.__init__)


def test_esper2maude::followedby_constructor_args():
    sig = inspect.signature(esper2Maude::FollowedBy.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::filterpart_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::FilterPart)


def test_esper2maude::filterpart_constructor_exists():
    assert callable(esper2Maude::FilterPart.__init__)


def test_esper2maude::filterpart_constructor_args():
    sig = inspect.signature(esper2Maude::FilterPart.__init__)
    params = list(sig.parameters.keys())
    assert "t" in params, "Missing parameter 't'"
    assert "eventPropName" in params, "Missing parameter 'eventPropName'"
    assert "neg" in params, "Missing parameter 'neg'"
    assert "num" in params, "Missing parameter 'num'"
    assert "str" in params, "Missing parameter 'str'"
    assert "dec" in params, "Missing parameter 'dec'"
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "f" in params, "Missing parameter 'f'"

def test_esper2maude::filterpart_has_t():
    assert hasattr(esper2Maude::FilterPart, "t")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "t" in klass.__dict__:
            descriptor = klass.__dict__["t"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_eventPropName():
    assert hasattr(esper2Maude::FilterPart, "eventPropName")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "eventPropName" in klass.__dict__:
            descriptor = klass.__dict__["eventPropName"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_neg():
    assert hasattr(esper2Maude::FilterPart, "neg")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_num():
    assert hasattr(esper2Maude::FilterPart, "num")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_str():
    assert hasattr(esper2Maude::FilterPart, "str")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_dec():
    assert hasattr(esper2Maude::FilterPart, "dec")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "dec" in klass.__dict__:
            descriptor = klass.__dict__["dec"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_eventVariable():
    assert hasattr(esper2Maude::FilterPart, "eventVariable")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterpart_has_f():
    assert hasattr(esper2Maude::FilterPart, "f")
    descriptor = None
    for klass in esper2Maude::FilterPart.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::every_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Every)


def test_esper2maude::every_constructor_exists():
    assert callable(esper2Maude::Every.__init__)


def test_esper2maude::every_constructor_args():
    sig = inspect.signature(esper2Maude::Every.__init__)
    params = list(sig.parameters.keys())
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "eventName" in params, "Missing parameter 'eventName'"

def test_esper2maude::every_has_eventVariable():
    assert hasattr(esper2Maude::Every, "eventVariable")
    descriptor = None
    for klass in esper2Maude::Every.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::every_has_eventName():
    assert hasattr(esper2Maude::Every, "eventName")
    descriptor = None
    for klass in esper2Maude::Every.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::subfilterfollowedby_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::SubFilterFollowedBy)


def test_esper2maude::subfilterfollowedby_constructor_exists():
    assert callable(esper2Maude::SubFilterFollowedBy.__init__)


def test_esper2maude::subfilterfollowedby_constructor_args():
    sig = inspect.signature(esper2Maude::SubFilterFollowedBy.__init__)
    params = list(sig.parameters.keys())
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "eventName" in params, "Missing parameter 'eventName'"

def test_esper2maude::subfilterfollowedby_has_eventVariable():
    assert hasattr(esper2Maude::SubFilterFollowedBy, "eventVariable")
    descriptor = None
    for klass in esper2Maude::SubFilterFollowedBy.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::subfilterfollowedby_has_eventName():
    assert hasattr(esper2Maude::SubFilterFollowedBy, "eventName")
    descriptor = None
    for klass in esper2Maude::SubFilterFollowedBy.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::eventproperty_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::EventProperty)


def test_esper2maude::eventproperty_constructor_exists():
    assert callable(esper2Maude::EventProperty.__init__)


def test_esper2maude::eventproperty_constructor_args():
    sig = inspect.signature(esper2Maude::EventProperty.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude::eventproperty_has_type():
    assert hasattr(esper2Maude::EventProperty, "type")
    descriptor = None
    for klass in esper2Maude::EventProperty.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::eventproperty_has_name():
    assert hasattr(esper2Maude::EventProperty, "name")
    descriptor = None
    for klass in esper2Maude::EventProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::pattern_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Pattern)


def test_esper2maude::pattern_constructor_exists():
    assert callable(esper2Maude::Pattern.__init__)


def test_esper2maude::pattern_constructor_args():
    sig = inspect.signature(esper2Maude::Pattern.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude::pattern_has_num():
    assert hasattr(esper2Maude::Pattern, "num")
    descriptor = None
    for klass in esper2Maude::Pattern.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::pattern_has_name():
    assert hasattr(esper2Maude::Pattern, "name")
    descriptor = None
    for klass in esper2Maude::Pattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::schema_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Schema)


def test_esper2maude::schema_constructor_exists():
    assert callable(esper2Maude::Schema.__init__)


def test_esper2maude::schema_constructor_args():
    sig = inspect.signature(esper2Maude::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude::schema_has_name():
    assert hasattr(esper2Maude::Schema, "name")
    descriptor = None
    for klass in esper2Maude::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::model_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Model)


def test_esper2maude::model_constructor_exists():
    assert callable(esper2Maude::Model.__init__)


def test_esper2maude::model_constructor_args():
    sig = inspect.signature(esper2Maude::Model.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::filteroperator_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::FilterOperator)


def test_esper2maude::filteroperator_constructor_exists():
    assert callable(esper2Maude::FilterOperator.__init__)


def test_esper2maude::filteroperator_constructor_args():
    sig = inspect.signature(esper2Maude::FilterOperator.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::filterevent_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::FilterEvent)


def test_esper2maude::filterevent_constructor_exists():
    assert callable(esper2Maude::FilterEvent.__init__)


def test_esper2maude::filterevent_constructor_args():
    sig = inspect.signature(esper2Maude::FilterEvent.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::wherefilter_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::WhereFilter)


def test_esper2maude::wherefilter_constructor_exists():
    assert callable(esper2Maude::WhereFilter.__init__)


def test_esper2maude::wherefilter_constructor_args():
    sig = inspect.signature(esper2Maude::WhereFilter.__init__)
    params = list(sig.parameters.keys())
    assert "timer" in params, "Missing parameter 'timer'"
    assert "num" in params, "Missing parameter 'num'"

def test_esper2maude::wherefilter_has_timer():
    assert hasattr(esper2Maude::WhereFilter, "timer")
    descriptor = None
    for klass in esper2Maude::WhereFilter.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::wherefilter_has_num():
    assert hasattr(esper2Maude::WhereFilter, "num")
    descriptor = None
    for klass in esper2Maude::WhereFilter.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::window_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Window)


def test_esper2maude::window_constructor_exists():
    assert callable(esper2Maude::Window.__init__)


def test_esper2maude::window_constructor_args():
    sig = inspect.signature(esper2Maude::Window.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "typeTime" in params, "Missing parameter 'typeTime'"
    assert "typeBatch" in params, "Missing parameter 'typeBatch'"

def test_esper2maude::window_has_num():
    assert hasattr(esper2Maude::Window, "num")
    descriptor = None
    for klass in esper2Maude::Window.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::window_has_typeTime():
    assert hasattr(esper2Maude::Window, "typeTime")
    descriptor = None
    for klass in esper2Maude::Window.__mro__:
        if "typeTime" in klass.__dict__:
            descriptor = klass.__dict__["typeTime"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::window_has_typeBatch():
    assert hasattr(esper2Maude::Window, "typeBatch")
    descriptor = None
    for klass in esper2Maude::Window.__mro__:
        if "typeBatch" in klass.__dict__:
            descriptor = klass.__dict__["typeBatch"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::filterfrom_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::FilterFrom)


def test_esper2maude::filterfrom_constructor_exists():
    assert callable(esper2Maude::FilterFrom.__init__)


def test_esper2maude::filterfrom_constructor_args():
    sig = inspect.signature(esper2Maude::FilterFrom.__init__)
    params = list(sig.parameters.keys())
    assert "eventVariable" in params, "Missing parameter 'eventVariable'"
    assert "eventName" in params, "Missing parameter 'eventName'"

def test_esper2maude::filterfrom_has_eventVariable():
    assert hasattr(esper2Maude::FilterFrom, "eventVariable")
    descriptor = None
    for klass in esper2Maude::FilterFrom.__mro__:
        if "eventVariable" in klass.__dict__:
            descriptor = klass.__dict__["eventVariable"]
            break
    assert isinstance(descriptor, property)

def test_esper2maude::filterfrom_has_eventName():
    assert hasattr(esper2Maude::FilterFrom, "eventName")
    descriptor = None
    for klass in esper2Maude::FilterFrom.__mro__:
        if "eventName" in klass.__dict__:
            descriptor = klass.__dict__["eventName"]
            break
    assert isinstance(descriptor, property)



def test_esper2maude::lastselectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::LastSelectEntry)


def test_esper2maude::lastselectentry_constructor_exists():
    assert callable(esper2Maude::LastSelectEntry.__init__)


def test_esper2maude::lastselectentry_constructor_args():
    sig = inspect.signature(esper2Maude::LastSelectEntry.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::nonlastselectentry_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::NonLastSelectEntry)


def test_esper2maude::nonlastselectentry_constructor_exists():
    assert callable(esper2Maude::NonLastSelectEntry.__init__)


def test_esper2maude::nonlastselectentry_constructor_args():
    sig = inspect.signature(esper2Maude::NonLastSelectEntry.__init__)
    params = list(sig.parameters.keys())



def test_esper2maude::event_is_not_abstract():
    assert not inspect.isabstract(esper2Maude::Event)


def test_esper2maude::event_constructor_exists():
    assert callable(esper2Maude::Event.__init__)


def test_esper2maude::event_constructor_args():
    sig = inspect.signature(esper2Maude::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_esper2maude::event_has_name():
    assert hasattr(esper2Maude::Event, "name")
    descriptor = None
    for klass in esper2Maude::Event.__mro__:
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
esper2Maude::SelectEntry_strategy = st.builds(
    esper2Maude::SelectEntry,
    groupOp=
        safe_text,
    alias=
        safe_text
)
esper2Maude::Field_strategy = st.builds(
    esper2Maude::Field,
    eventVariable=
        safe_text,
    eventPropName=
        safe_text,
    star=
        safe_text
)
esper2Maude::ComparisonOperator_strategy = st.builds(
    esper2Maude::ComparisonOperator,
    ge=
        safe_text,
    le=
        safe_text,
    lt=
        safe_text,
    neq=
        safe_text,
    eq=
        safe_text,
    gt=
        safe_text
)
esper2Maude::LogicalOperator_strategy = st.builds(
    esper2Maude::LogicalOperator,
    or_=
        safe_text,
    and_=
        safe_text
)
esper2Maude::FollowedBy_strategy = st.builds(
    esper2Maude::FollowedBy,
)
esper2Maude::FilterPart_strategy = st.builds(
    esper2Maude::FilterPart,
    t=
        safe_text,
    eventPropName=
        safe_text,
    neg=
        safe_text,
    num=
        st.integers(),
    str=
        safe_text,
    dec=
        st.integers(),
    eventVariable=
        safe_text,
    f=
        safe_text
)
esper2Maude::Every_strategy = st.builds(
    esper2Maude::Every,
    eventVariable=
        safe_text,
    eventName=
        safe_text
)
esper2Maude::SubFilterFollowedBy_strategy = st.builds(
    esper2Maude::SubFilterFollowedBy,
    eventVariable=
        safe_text,
    eventName=
        safe_text
)
esper2Maude::EventProperty_strategy = st.builds(
    esper2Maude::EventProperty,
    type=
        safe_text,
    name=
        safe_text
)
esper2Maude::Pattern_strategy = st.builds(
    esper2Maude::Pattern,
    num=
        st.integers(),
    name=
        safe_text
)
esper2Maude::Schema_strategy = st.builds(
    esper2Maude::Schema,
    name=
        safe_text
)
esper2Maude::Model_strategy = st.builds(
    esper2Maude::Model,
)
esper2Maude::FilterOperator_strategy = st.builds(
    esper2Maude::FilterOperator,
)
esper2Maude::FilterEvent_strategy = st.builds(
    esper2Maude::FilterEvent,
)
esper2Maude::WhereFilter_strategy = st.builds(
    esper2Maude::WhereFilter,
    timer=
        safe_text,
    num=
        st.integers()
)
esper2Maude::Window_strategy = st.builds(
    esper2Maude::Window,
    num=
        st.integers(),
    typeTime=
        safe_text,
    typeBatch=
        safe_text
)
esper2Maude::FilterFrom_strategy = st.builds(
    esper2Maude::FilterFrom,
    eventVariable=
        safe_text,
    eventName=
        safe_text
)
esper2Maude::LastSelectEntry_strategy = st.builds(
    esper2Maude::LastSelectEntry,
)
esper2Maude::NonLastSelectEntry_strategy = st.builds(
    esper2Maude::NonLastSelectEntry,
)
esper2Maude::Event_strategy = st.builds(
    esper2Maude::Event,
    name=
        safe_text
)

@given(instance=esper2Maude::SelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude::selectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude::SelectEntry)

@given(instance=esper2Maude::SelectEntry_strategy)
def test_esper2maude::selectentry_groupOp_type(instance):
    assert isinstance(instance.groupOp, str)


@given(instance=esper2Maude::SelectEntry_strategy)
def test_esper2maude::selectentry_groupOp_setter(instance):
    original = instance.groupOp
    instance.groupOp = original
    assert instance.groupOp == original

@given(instance=esper2Maude::SelectEntry_strategy)
def test_esper2maude::selectentry_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=esper2Maude::SelectEntry_strategy)
def test_esper2maude::selectentry_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=esper2Maude::Field_strategy)
@settings(max_examples=50)
def test_esper2maude::field_instantiation(instance):
    assert isinstance(instance, esper2Maude::Field)

@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_eventVariable_type(instance):
    assert isinstance(instance.eventVariable, str)


@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_eventPropName_type(instance):
    assert isinstance(instance.eventPropName, str)


@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_eventPropName_setter(instance):
    original = instance.eventPropName
    instance.eventPropName = original
    assert instance.eventPropName == original

@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_star_type(instance):
    assert isinstance(instance.star, str)


@given(instance=esper2Maude::Field_strategy)
def test_esper2maude::field_star_setter(instance):
    original = instance.star
    instance.star = original
    assert instance.star == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
@settings(max_examples=50)
def test_esper2maude::comparisonoperator_instantiation(instance):
    assert isinstance(instance, esper2Maude::ComparisonOperator)

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_ge_type(instance):
    assert isinstance(instance.ge, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_ge_setter(instance):
    original = instance.ge
    instance.ge = original
    assert instance.ge == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_le_type(instance):
    assert isinstance(instance.le, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_le_setter(instance):
    original = instance.le
    instance.le = original
    assert instance.le == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_lt_type(instance):
    assert isinstance(instance.lt, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_lt_setter(instance):
    original = instance.lt
    instance.lt = original
    assert instance.lt == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_neq_type(instance):
    assert isinstance(instance.neq, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_neq_setter(instance):
    original = instance.neq
    instance.neq = original
    assert instance.neq == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_gt_type(instance):
    assert isinstance(instance.gt, str)


@given(instance=esper2Maude::ComparisonOperator_strategy)
def test_esper2maude::comparisonoperator_gt_setter(instance):
    original = instance.gt
    instance.gt = original
    assert instance.gt == original

@given(instance=esper2Maude::LogicalOperator_strategy)
@settings(max_examples=50)
def test_esper2maude::logicaloperator_instantiation(instance):
    assert isinstance(instance, esper2Maude::LogicalOperator)

@given(instance=esper2Maude::LogicalOperator_strategy)
def test_esper2maude::logicaloperator_or__type(instance):
    assert isinstance(instance.or_, str)


@given(instance=esper2Maude::LogicalOperator_strategy)
def test_esper2maude::logicaloperator_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=esper2Maude::LogicalOperator_strategy)
def test_esper2maude::logicaloperator_and__type(instance):
    assert isinstance(instance.and_, str)


@given(instance=esper2Maude::LogicalOperator_strategy)
def test_esper2maude::logicaloperator_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=esper2Maude::FollowedBy_strategy)
@settings(max_examples=50)
def test_esper2maude::followedby_instantiation(instance):
    assert isinstance(instance, esper2Maude::FollowedBy)

@given(instance=esper2Maude::FilterPart_strategy)
@settings(max_examples=50)
def test_esper2maude::filterpart_instantiation(instance):
    assert isinstance(instance, esper2Maude::FilterPart)

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_t_type(instance):
    assert isinstance(instance.t, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_eventPropName_type(instance):
    assert isinstance(instance.eventPropName, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_eventPropName_setter(instance):
    original = instance.eventPropName
    instance.eventPropName = original
    assert instance.eventPropName == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_neg_type(instance):
    assert isinstance(instance.neg, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_dec_type(instance):
    assert isinstance(instance.dec, int)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_dec_setter(instance):
    original = instance.dec
    instance.dec = original
    assert instance.dec == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_eventVariable_type(instance):
    assert isinstance(instance.eventVariable, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_f_type(instance):
    assert isinstance(instance.f, str)


@given(instance=esper2Maude::FilterPart_strategy)
def test_esper2maude::filterpart_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=esper2Maude::Every_strategy)
@settings(max_examples=50)
def test_esper2maude::every_instantiation(instance):
    assert isinstance(instance, esper2Maude::Every)

@given(instance=esper2Maude::Every_strategy)
def test_esper2maude::every_eventVariable_type(instance):
    assert isinstance(instance.eventVariable, str)


@given(instance=esper2Maude::Every_strategy)
def test_esper2maude::every_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude::Every_strategy)
def test_esper2maude::every_eventName_type(instance):
    assert isinstance(instance.eventName, str)


@given(instance=esper2Maude::Every_strategy)
def test_esper2maude::every_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=esper2Maude::SubFilterFollowedBy_strategy)
@settings(max_examples=50)
def test_esper2maude::subfilterfollowedby_instantiation(instance):
    assert isinstance(instance, esper2Maude::SubFilterFollowedBy)

@given(instance=esper2Maude::SubFilterFollowedBy_strategy)
def test_esper2maude::subfilterfollowedby_eventVariable_type(instance):
    assert isinstance(instance.eventVariable, str)


@given(instance=esper2Maude::SubFilterFollowedBy_strategy)
def test_esper2maude::subfilterfollowedby_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude::SubFilterFollowedBy_strategy)
def test_esper2maude::subfilterfollowedby_eventName_type(instance):
    assert isinstance(instance.eventName, str)


@given(instance=esper2Maude::SubFilterFollowedBy_strategy)
def test_esper2maude::subfilterfollowedby_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=esper2Maude::EventProperty_strategy)
@settings(max_examples=50)
def test_esper2maude::eventproperty_instantiation(instance):
    assert isinstance(instance, esper2Maude::EventProperty)

@given(instance=esper2Maude::EventProperty_strategy)
def test_esper2maude::eventproperty_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=esper2Maude::EventProperty_strategy)
def test_esper2maude::eventproperty_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=esper2Maude::EventProperty_strategy)
def test_esper2maude::eventproperty_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper2Maude::EventProperty_strategy)
def test_esper2maude::eventproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper2Maude::Pattern_strategy)
@settings(max_examples=50)
def test_esper2maude::pattern_instantiation(instance):
    assert isinstance(instance, esper2Maude::Pattern)

@given(instance=esper2Maude::Pattern_strategy)
def test_esper2maude::pattern_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=esper2Maude::Pattern_strategy)
def test_esper2maude::pattern_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=esper2Maude::Pattern_strategy)
def test_esper2maude::pattern_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper2Maude::Pattern_strategy)
def test_esper2maude::pattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper2Maude::Schema_strategy)
@settings(max_examples=50)
def test_esper2maude::schema_instantiation(instance):
    assert isinstance(instance, esper2Maude::Schema)

@given(instance=esper2Maude::Schema_strategy)
def test_esper2maude::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper2Maude::Schema_strategy)
def test_esper2maude::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=esper2Maude::Model_strategy)
@settings(max_examples=50)
def test_esper2maude::model_instantiation(instance):
    assert isinstance(instance, esper2Maude::Model)

@given(instance=esper2Maude::FilterOperator_strategy)
@settings(max_examples=50)
def test_esper2maude::filteroperator_instantiation(instance):
    assert isinstance(instance, esper2Maude::FilterOperator)

@given(instance=esper2Maude::FilterEvent_strategy)
@settings(max_examples=50)
def test_esper2maude::filterevent_instantiation(instance):
    assert isinstance(instance, esper2Maude::FilterEvent)

@given(instance=esper2Maude::WhereFilter_strategy)
@settings(max_examples=50)
def test_esper2maude::wherefilter_instantiation(instance):
    assert isinstance(instance, esper2Maude::WhereFilter)

@given(instance=esper2Maude::WhereFilter_strategy)
def test_esper2maude::wherefilter_timer_type(instance):
    assert isinstance(instance.timer, str)


@given(instance=esper2Maude::WhereFilter_strategy)
def test_esper2maude::wherefilter_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original

@given(instance=esper2Maude::WhereFilter_strategy)
def test_esper2maude::wherefilter_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=esper2Maude::WhereFilter_strategy)
def test_esper2maude::wherefilter_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=esper2Maude::Window_strategy)
@settings(max_examples=50)
def test_esper2maude::window_instantiation(instance):
    assert isinstance(instance, esper2Maude::Window)

@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_num_type(instance):
    assert isinstance(instance.num, int)


@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_typeTime_type(instance):
    assert isinstance(instance.typeTime, str)


@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_typeTime_setter(instance):
    original = instance.typeTime
    instance.typeTime = original
    assert instance.typeTime == original

@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_typeBatch_type(instance):
    assert isinstance(instance.typeBatch, str)


@given(instance=esper2Maude::Window_strategy)
def test_esper2maude::window_typeBatch_setter(instance):
    original = instance.typeBatch
    instance.typeBatch = original
    assert instance.typeBatch == original

@given(instance=esper2Maude::FilterFrom_strategy)
@settings(max_examples=50)
def test_esper2maude::filterfrom_instantiation(instance):
    assert isinstance(instance, esper2Maude::FilterFrom)

@given(instance=esper2Maude::FilterFrom_strategy)
def test_esper2maude::filterfrom_eventVariable_type(instance):
    assert isinstance(instance.eventVariable, str)


@given(instance=esper2Maude::FilterFrom_strategy)
def test_esper2maude::filterfrom_eventVariable_setter(instance):
    original = instance.eventVariable
    instance.eventVariable = original
    assert instance.eventVariable == original

@given(instance=esper2Maude::FilterFrom_strategy)
def test_esper2maude::filterfrom_eventName_type(instance):
    assert isinstance(instance.eventName, str)


@given(instance=esper2Maude::FilterFrom_strategy)
def test_esper2maude::filterfrom_eventName_setter(instance):
    original = instance.eventName
    instance.eventName = original
    assert instance.eventName == original

@given(instance=esper2Maude::LastSelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude::lastselectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude::LastSelectEntry)

@given(instance=esper2Maude::NonLastSelectEntry_strategy)
@settings(max_examples=50)
def test_esper2maude::nonlastselectentry_instantiation(instance):
    assert isinstance(instance, esper2Maude::NonLastSelectEntry)

@given(instance=esper2Maude::Event_strategy)
@settings(max_examples=50)
def test_esper2maude::event_instantiation(instance):
    assert isinstance(instance, esper2Maude::Event)

@given(instance=esper2Maude::Event_strategy)
def test_esper2maude::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=esper2Maude::Event_strategy)
def test_esper2maude::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
