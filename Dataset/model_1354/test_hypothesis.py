import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbstractState,
    statemachine_State,
    statemachine_FinalState,
    statemachine_InitialState,
    statemachine_StateChange,
    statemachine_Named,
    Named,
    statemachine_AbstractState,
    statemachine_AbstractTransition,
    statemachine_Statemachine,
    AbstractCondition,
    statemachine_AttributeCondition,
    statemachine_FieldCondition,
    statemachine_AbstractCondition,
    statemachine_ConditionalState,
    statemachine_StateAttribute,
    statemachine_StateValue,
    AbstractTransition,
    statemachine_Transition,
    statemachine_ConditionalTransition,
    StateAttributeType,
    StateValueType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_state_is_not_abstract():
    assert not inspect.isabstract(statemachine_State)


def test_statemachine_state_constructor_exists():
    assert callable(statemachine_State.__init__)


def test_statemachine_state_constructor_args():
    sig = inspect.signature(statemachine_State.__init__)
    params = list(sig.parameters.keys())
    assert "stateColor" in params, "Missing parameter 'stateColor'"

def test_statemachine_state_has_stateColor():
    assert hasattr(statemachine_State, "stateColor")
    descriptor = None
    for klass in statemachine_State.__mro__:
        if "stateColor" in klass.__dict__:
            descriptor = klass.__dict__["stateColor"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_finalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_FinalState)


def test_statemachine_finalstate_constructor_exists():
    assert callable(statemachine_FinalState.__init__)


def test_statemachine_finalstate_constructor_args():
    sig = inspect.signature(statemachine_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_initialstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_InitialState)


def test_statemachine_initialstate_constructor_exists():
    assert callable(statemachine_InitialState.__init__)


def test_statemachine_initialstate_constructor_args():
    sig = inspect.signature(statemachine_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statechange_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateChange)


def test_statemachine_statechange_constructor_exists():
    assert callable(statemachine_StateChange.__init__)


def test_statemachine_statechange_constructor_args():
    sig = inspect.signature(statemachine_StateChange.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_named_is_not_abstract():
    assert not inspect.isabstract(statemachine_Named)


def test_statemachine_named_constructor_exists():
    assert callable(statemachine_Named.__init__)


def test_statemachine_named_constructor_args():
    sig = inspect.signature(statemachine_Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_statemachine_named_has_name():
    assert hasattr(statemachine_Named, "name")
    descriptor = None
    for klass in statemachine_Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_abstractstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractState)


def test_statemachine_abstractstate_constructor_exists():
    assert callable(statemachine_AbstractState.__init__)


def test_statemachine_abstractstate_constructor_args():
    sig = inspect.signature(statemachine_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractTransition)


def test_statemachine_abstracttransition_constructor_exists():
    assert callable(statemachine_AbstractTransition.__init__)


def test_statemachine_abstracttransition_constructor_args():
    sig = inspect.signature(statemachine_AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(statemachine_Statemachine)


def test_statemachine_statemachine_constructor_exists():
    assert callable(statemachine_Statemachine.__init__)


def test_statemachine_statemachine_constructor_args():
    sig = inspect.signature(statemachine_Statemachine.__init__)
    params = list(sig.parameters.keys())
    assert "associatedTree" in params, "Missing parameter 'associatedTree'"
    assert "associatedAttribute" in params, "Missing parameter 'associatedAttribute'"

def test_statemachine_statemachine_has_associatedTree():
    assert hasattr(statemachine_Statemachine, "associatedTree")
    descriptor = None
    for klass in statemachine_Statemachine.__mro__:
        if "associatedTree" in klass.__dict__:
            descriptor = klass.__dict__["associatedTree"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_statemachine_has_associatedAttribute():
    assert hasattr(statemachine_Statemachine, "associatedAttribute")
    descriptor = None
    for klass in statemachine_Statemachine.__mro__:
        if "associatedAttribute" in klass.__dict__:
            descriptor = klass.__dict__["associatedAttribute"]
            break
    assert isinstance(descriptor, property)



def test_abstractcondition_is_not_abstract():
    assert not inspect.isabstract(AbstractCondition)


def test_abstractcondition_constructor_exists():
    assert callable(AbstractCondition.__init__)


def test_abstractcondition_constructor_args():
    sig = inspect.signature(AbstractCondition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_attributecondition_is_not_abstract():
    assert not inspect.isabstract(statemachine_AttributeCondition)


def test_statemachine_attributecondition_constructor_exists():
    assert callable(statemachine_AttributeCondition.__init__)


def test_statemachine_attributecondition_constructor_args():
    sig = inspect.signature(statemachine_AttributeCondition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_fieldcondition_is_not_abstract():
    assert not inspect.isabstract(statemachine_FieldCondition)


def test_statemachine_fieldcondition_constructor_exists():
    assert callable(statemachine_FieldCondition.__init__)


def test_statemachine_fieldcondition_constructor_args():
    sig = inspect.signature(statemachine_FieldCondition.__init__)
    params = list(sig.parameters.keys())
    assert "fieldName" in params, "Missing parameter 'fieldName'"

def test_statemachine_fieldcondition_has_fieldName():
    assert hasattr(statemachine_FieldCondition, "fieldName")
    descriptor = None
    for klass in statemachine_FieldCondition.__mro__:
        if "fieldName" in klass.__dict__:
            descriptor = klass.__dict__["fieldName"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_abstractcondition_is_not_abstract():
    assert not inspect.isabstract(statemachine_AbstractCondition)


def test_statemachine_abstractcondition_constructor_exists():
    assert callable(statemachine_AbstractCondition.__init__)


def test_statemachine_abstractcondition_constructor_args():
    sig = inspect.signature(statemachine_AbstractCondition.__init__)
    params = list(sig.parameters.keys())
    assert "isNotCondition" in params, "Missing parameter 'isNotCondition'"

def test_statemachine_abstractcondition_has_isNotCondition():
    assert hasattr(statemachine_AbstractCondition, "isNotCondition")
    descriptor = None
    for klass in statemachine_AbstractCondition.__mro__:
        if "isNotCondition" in klass.__dict__:
            descriptor = klass.__dict__["isNotCondition"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_conditionalstate_is_not_abstract():
    assert not inspect.isabstract(statemachine_ConditionalState)


def test_statemachine_conditionalstate_constructor_exists():
    assert callable(statemachine_ConditionalState.__init__)


def test_statemachine_conditionalstate_constructor_args():
    sig = inspect.signature(statemachine_ConditionalState.__init__)
    params = list(sig.parameters.keys())
    assert "conditionsOrganization" in params, "Missing parameter 'conditionsOrganization'"
    assert "andExpression" in params, "Missing parameter 'andExpression'"

def test_statemachine_conditionalstate_has_conditionsOrganization():
    assert hasattr(statemachine_ConditionalState, "conditionsOrganization")
    descriptor = None
    for klass in statemachine_ConditionalState.__mro__:
        if "conditionsOrganization" in klass.__dict__:
            descriptor = klass.__dict__["conditionsOrganization"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_conditionalstate_has_andExpression():
    assert hasattr(statemachine_ConditionalState, "andExpression")
    descriptor = None
    for klass in statemachine_ConditionalState.__mro__:
        if "andExpression" in klass.__dict__:
            descriptor = klass.__dict__["andExpression"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_stateattribute_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateAttribute)


def test_statemachine_stateattribute_constructor_exists():
    assert callable(statemachine_StateAttribute.__init__)


def test_statemachine_stateattribute_constructor_args():
    sig = inspect.signature(statemachine_StateAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"

def test_statemachine_stateattribute_has_value():
    assert hasattr(statemachine_StateAttribute, "value")
    descriptor = None
    for klass in statemachine_StateAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_stateattribute_has_type():
    assert hasattr(statemachine_StateAttribute, "type")
    descriptor = None
    for klass in statemachine_StateAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_statevalue_is_not_abstract():
    assert not inspect.isabstract(statemachine_StateValue)


def test_statemachine_statevalue_constructor_exists():
    assert callable(statemachine_StateValue.__init__)


def test_statemachine_statevalue_constructor_args():
    sig = inspect.signature(statemachine_StateValue.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_statemachine_statevalue_has_type():
    assert hasattr(statemachine_StateValue, "type")
    descriptor = None
    for klass in statemachine_StateValue.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_statemachine_statevalue_has_value():
    assert hasattr(statemachine_StateValue, "value")
    descriptor = None
    for klass in statemachine_StateValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_abstracttransition_is_not_abstract():
    assert not inspect.isabstract(AbstractTransition)


def test_abstracttransition_constructor_exists():
    assert callable(AbstractTransition.__init__)


def test_abstracttransition_constructor_args():
    sig = inspect.signature(AbstractTransition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_transition_is_not_abstract():
    assert not inspect.isabstract(statemachine_Transition)


def test_statemachine_transition_constructor_exists():
    assert callable(statemachine_Transition.__init__)


def test_statemachine_transition_constructor_args():
    sig = inspect.signature(statemachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_conditionaltransition_is_not_abstract():
    assert not inspect.isabstract(statemachine_ConditionalTransition)


def test_statemachine_conditionaltransition_constructor_exists():
    assert callable(statemachine_ConditionalTransition.__init__)


def test_statemachine_conditionaltransition_constructor_args():
    sig = inspect.signature(statemachine_ConditionalTransition.__init__)
    params = list(sig.parameters.keys())

def test_stateattributetype_exists():
    # Check that the Enumeration exists
    assert StateAttributeType is not None

def test_stateattributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateAttributeType]
    expected_literals = [
        "query",
        "constant",
        "eventField",
        "location",
        "null",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateAttributeType"

def test_statevaluetype_exists():
    # Check that the Enumeration exists
    assert StateValueType is not None

def test_statevaluetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StateValueType]
    expected_literals = [
        "string",
        "eventField",
        "long",
        "query",
        "null",
        "int",
        "definedState",
        "eventName",
        "delete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StateValueType"


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
AbstractState_strategy = st.builds(
    AbstractState,
)
statemachine_State_strategy = st.builds(
    statemachine_State,
    stateColor=
        safe_text
)
statemachine_FinalState_strategy = st.builds(
    statemachine_FinalState,
)
statemachine_InitialState_strategy = st.builds(
    statemachine_InitialState,
)
statemachine_StateChange_strategy = st.builds(
    statemachine_StateChange,
)
statemachine_Named_strategy = st.builds(
    statemachine_Named,
    name=
        safe_text
)
Named_strategy = st.builds(
    Named,
)
statemachine_AbstractState_strategy = st.builds(
    statemachine_AbstractState,
)
statemachine_AbstractTransition_strategy = st.builds(
    statemachine_AbstractTransition,
)
statemachine_Statemachine_strategy = st.builds(
    statemachine_Statemachine,
    associatedTree=
        safe_text,
    associatedAttribute=
        safe_text
)
AbstractCondition_strategy = st.builds(
    AbstractCondition,
)
statemachine_AttributeCondition_strategy = st.builds(
    statemachine_AttributeCondition,
)
statemachine_FieldCondition_strategy = st.builds(
    statemachine_FieldCondition,
    fieldName=
        safe_text
)
statemachine_AbstractCondition_strategy = st.builds(
    statemachine_AbstractCondition,
    isNotCondition=
        st.booleans()
)
statemachine_ConditionalState_strategy = st.builds(
    statemachine_ConditionalState,
    conditionsOrganization=
        safe_text,
    andExpression=
        st.booleans()
)
statemachine_StateAttribute_strategy = st.builds(
    statemachine_StateAttribute,
    value=
        safe_text,
    type=
        safe_text
)
statemachine_StateValue_strategy = st.builds(
    statemachine_StateValue,
    type=
        safe_text,
    value=
        safe_text
)
AbstractTransition_strategy = st.builds(
    AbstractTransition,
)
statemachine_Transition_strategy = st.builds(
    statemachine_Transition,
)
statemachine_ConditionalTransition_strategy = st.builds(
    statemachine_ConditionalTransition,
)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=statemachine_State_strategy)
@settings(max_examples=50)
def test_statemachine_state_instantiation(instance):
    assert isinstance(instance, statemachine_State)



@given(instance=statemachine_State_strategy)
def test_statemachine_state_stateColor_setter(instance):
    original = instance.stateColor
    instance.stateColor = original
    assert instance.stateColor == original

@given(instance=statemachine_FinalState_strategy)
@settings(max_examples=50)
def test_statemachine_finalstate_instantiation(instance):
    assert isinstance(instance, statemachine_FinalState)

@given(instance=statemachine_InitialState_strategy)
@settings(max_examples=50)
def test_statemachine_initialstate_instantiation(instance):
    assert isinstance(instance, statemachine_InitialState)

@given(instance=statemachine_StateChange_strategy)
@settings(max_examples=50)
def test_statemachine_statechange_instantiation(instance):
    assert isinstance(instance, statemachine_StateChange)

@given(instance=statemachine_Named_strategy)
@settings(max_examples=50)
def test_statemachine_named_instantiation(instance):
    assert isinstance(instance, statemachine_Named)



@given(instance=statemachine_Named_strategy)
def test_statemachine_named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=statemachine_AbstractState_strategy)
@settings(max_examples=50)
def test_statemachine_abstractstate_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractState)

@given(instance=statemachine_AbstractTransition_strategy)
@settings(max_examples=50)
def test_statemachine_abstracttransition_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractTransition)

@given(instance=statemachine_Statemachine_strategy)
@settings(max_examples=50)
def test_statemachine_statemachine_instantiation(instance):
    assert isinstance(instance, statemachine_Statemachine)



@given(instance=statemachine_Statemachine_strategy)
def test_statemachine_statemachine_associatedTree_setter(instance):
    original = instance.associatedTree
    instance.associatedTree = original
    assert instance.associatedTree == original



@given(instance=statemachine_Statemachine_strategy)
def test_statemachine_statemachine_associatedAttribute_setter(instance):
    original = instance.associatedAttribute
    instance.associatedAttribute = original
    assert instance.associatedAttribute == original

@given(instance=AbstractCondition_strategy)
@settings(max_examples=50)
def test_abstractcondition_instantiation(instance):
    assert isinstance(instance, AbstractCondition)

@given(instance=statemachine_AttributeCondition_strategy)
@settings(max_examples=50)
def test_statemachine_attributecondition_instantiation(instance):
    assert isinstance(instance, statemachine_AttributeCondition)

@given(instance=statemachine_FieldCondition_strategy)
@settings(max_examples=50)
def test_statemachine_fieldcondition_instantiation(instance):
    assert isinstance(instance, statemachine_FieldCondition)



@given(instance=statemachine_FieldCondition_strategy)
def test_statemachine_fieldcondition_fieldName_setter(instance):
    original = instance.fieldName
    instance.fieldName = original
    assert instance.fieldName == original

@given(instance=statemachine_AbstractCondition_strategy)
@settings(max_examples=50)
def test_statemachine_abstractcondition_instantiation(instance):
    assert isinstance(instance, statemachine_AbstractCondition)



@given(instance=statemachine_AbstractCondition_strategy)
def test_statemachine_abstractcondition_isNotCondition_setter(instance):
    original = instance.isNotCondition
    instance.isNotCondition = original
    assert instance.isNotCondition == original

@given(instance=statemachine_ConditionalState_strategy)
@settings(max_examples=50)
def test_statemachine_conditionalstate_instantiation(instance):
    assert isinstance(instance, statemachine_ConditionalState)



@given(instance=statemachine_ConditionalState_strategy)
def test_statemachine_conditionalstate_conditionsOrganization_setter(instance):
    original = instance.conditionsOrganization
    instance.conditionsOrganization = original
    assert instance.conditionsOrganization == original



@given(instance=statemachine_ConditionalState_strategy)
def test_statemachine_conditionalstate_andExpression_setter(instance):
    original = instance.andExpression
    instance.andExpression = original
    assert instance.andExpression == original

@given(instance=statemachine_StateAttribute_strategy)
@settings(max_examples=50)
def test_statemachine_stateattribute_instantiation(instance):
    assert isinstance(instance, statemachine_StateAttribute)



@given(instance=statemachine_StateAttribute_strategy)
def test_statemachine_stateattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=statemachine_StateAttribute_strategy)
def test_statemachine_stateattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=statemachine_StateValue_strategy)
@settings(max_examples=50)
def test_statemachine_statevalue_instantiation(instance):
    assert isinstance(instance, statemachine_StateValue)



@given(instance=statemachine_StateValue_strategy)
def test_statemachine_statevalue_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=statemachine_StateValue_strategy)
def test_statemachine_statevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AbstractTransition_strategy)
@settings(max_examples=50)
def test_abstracttransition_instantiation(instance):
    assert isinstance(instance, AbstractTransition)

@given(instance=statemachine_Transition_strategy)
@settings(max_examples=50)
def test_statemachine_transition_instantiation(instance):
    assert isinstance(instance, statemachine_Transition)

@given(instance=statemachine_ConditionalTransition_strategy)
@settings(max_examples=50)
def test_statemachine_conditionaltransition_instantiation(instance):
    assert isinstance(instance, statemachine_ConditionalTransition)
