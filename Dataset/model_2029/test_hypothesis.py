import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    uisut_UISUTElement,
    UITrigger,
    uisut_ComponentTrigger,
    uisut_UserTrigger,
    AbstractState,
    uisut_FinalState,
    uisut_InitialState,
    uisut_UIState,
    UISUTElement,
    uisut_ApplicationSystem,
    uisut_UICondition,
    uisut_UIControl,
    uisut_AbstractState,
    uisut_UIStatemachine,
    uisut_Action,
    uisut_UITrigger,
    uisut_UITransition,
    uisut_UIDataVariable,
    uisut_UISUT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_uisut_uisutelement_is_not_abstract():
    assert not inspect.isabstract(uisut_UISUTElement)


def test_uisut_uisutelement_constructor_exists():
    assert callable(uisut_UISUTElement.__init__)


def test_uisut_uisutelement_constructor_args():
    sig = inspect.signature(uisut_UISUTElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_uisut_uisutelement_has_description():
    assert hasattr(uisut_UISUTElement, "description")
    descriptor = None
    for klass in uisut_UISUTElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uisutelement_has_name():
    assert hasattr(uisut_UISUTElement, "name")
    descriptor = None
    for klass in uisut_UISUTElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uisutelement_has_id():
    assert hasattr(uisut_UISUTElement, "id")
    descriptor = None
    for klass in uisut_UISUTElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_uitrigger_is_not_abstract():
    assert not inspect.isabstract(UITrigger)


def test_uitrigger_constructor_exists():
    assert callable(UITrigger.__init__)


def test_uitrigger_constructor_args():
    sig = inspect.signature(UITrigger.__init__)
    params = list(sig.parameters.keys())



def test_uisut_componenttrigger_is_not_abstract():
    assert not inspect.isabstract(uisut_ComponentTrigger)


def test_uisut_componenttrigger_constructor_exists():
    assert callable(uisut_ComponentTrigger.__init__)


def test_uisut_componenttrigger_constructor_args():
    sig = inspect.signature(uisut_ComponentTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uisut_usertrigger_is_not_abstract():
    assert not inspect.isabstract(uisut_UserTrigger)


def test_uisut_usertrigger_constructor_exists():
    assert callable(uisut_UserTrigger.__init__)


def test_uisut_usertrigger_constructor_args():
    sig = inspect.signature(uisut_UserTrigger.__init__)
    params = list(sig.parameters.keys())



def test_abstractstate_is_not_abstract():
    assert not inspect.isabstract(AbstractState)


def test_abstractstate_constructor_exists():
    assert callable(AbstractState.__init__)


def test_abstractstate_constructor_args():
    sig = inspect.signature(AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_uisut_finalstate_is_not_abstract():
    assert not inspect.isabstract(uisut_FinalState)


def test_uisut_finalstate_constructor_exists():
    assert callable(uisut_FinalState.__init__)


def test_uisut_finalstate_constructor_args():
    sig = inspect.signature(uisut_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_uisut_initialstate_is_not_abstract():
    assert not inspect.isabstract(uisut_InitialState)


def test_uisut_initialstate_constructor_exists():
    assert callable(uisut_InitialState.__init__)


def test_uisut_initialstate_constructor_args():
    sig = inspect.signature(uisut_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uistate_is_not_abstract():
    assert not inspect.isabstract(uisut_UIState)


def test_uisut_uistate_constructor_exists():
    assert callable(uisut_UIState.__init__)


def test_uisut_uistate_constructor_args():
    sig = inspect.signature(uisut_UIState.__init__)
    params = list(sig.parameters.keys())
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "pic" in params, "Missing parameter 'pic'"

def test_uisut_uistate_has_isInitial():
    assert hasattr(uisut_UIState, "isInitial")
    descriptor = None
    for klass in uisut_UIState.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uistate_has_pic():
    assert hasattr(uisut_UIState, "pic")
    descriptor = None
    for klass in uisut_UIState.__mro__:
        if "pic" in klass.__dict__:
            descriptor = klass.__dict__["pic"]
            break
    assert isinstance(descriptor, property)



def test_uisutelement_is_not_abstract():
    assert not inspect.isabstract(UISUTElement)


def test_uisutelement_constructor_exists():
    assert callable(UISUTElement.__init__)


def test_uisutelement_constructor_args():
    sig = inspect.signature(UISUTElement.__init__)
    params = list(sig.parameters.keys())



def test_uisut_applicationsystem_is_not_abstract():
    assert not inspect.isabstract(uisut_ApplicationSystem)


def test_uisut_applicationsystem_constructor_exists():
    assert callable(uisut_ApplicationSystem.__init__)


def test_uisut_applicationsystem_constructor_args():
    sig = inspect.signature(uisut_ApplicationSystem.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uicondition_is_not_abstract():
    assert not inspect.isabstract(uisut_UICondition)


def test_uisut_uicondition_constructor_exists():
    assert callable(uisut_UICondition.__init__)


def test_uisut_uicondition_constructor_args():
    sig = inspect.signature(uisut_UICondition.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uicontrol_is_not_abstract():
    assert not inspect.isabstract(uisut_UIControl)


def test_uisut_uicontrol_constructor_exists():
    assert callable(uisut_UIControl.__init__)


def test_uisut_uicontrol_constructor_args():
    sig = inspect.signature(uisut_UIControl.__init__)
    params = list(sig.parameters.keys())
    assert "variableName" in params, "Missing parameter 'variableName'"
    assert "valueExpression" in params, "Missing parameter 'valueExpression'"

def test_uisut_uicontrol_has_variableName():
    assert hasattr(uisut_UIControl, "variableName")
    descriptor = None
    for klass in uisut_UIControl.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uicontrol_has_valueExpression():
    assert hasattr(uisut_UIControl, "valueExpression")
    descriptor = None
    for klass in uisut_UIControl.__mro__:
        if "valueExpression" in klass.__dict__:
            descriptor = klass.__dict__["valueExpression"]
            break
    assert isinstance(descriptor, property)



def test_uisut_abstractstate_is_not_abstract():
    assert not inspect.isabstract(uisut_AbstractState)


def test_uisut_abstractstate_constructor_exists():
    assert callable(uisut_AbstractState.__init__)


def test_uisut_abstractstate_constructor_args():
    sig = inspect.signature(uisut_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uistatemachine_is_not_abstract():
    assert not inspect.isabstract(uisut_UIStatemachine)


def test_uisut_uistatemachine_constructor_exists():
    assert callable(uisut_UIStatemachine.__init__)


def test_uisut_uistatemachine_constructor_args():
    sig = inspect.signature(uisut_UIStatemachine.__init__)
    params = list(sig.parameters.keys())



def test_uisut_action_is_not_abstract():
    assert not inspect.isabstract(uisut_Action)


def test_uisut_action_constructor_exists():
    assert callable(uisut_Action.__init__)


def test_uisut_action_constructor_args():
    sig = inspect.signature(uisut_Action.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uitrigger_is_not_abstract():
    assert not inspect.isabstract(uisut_UITrigger)


def test_uisut_uitrigger_constructor_exists():
    assert callable(uisut_UITrigger.__init__)


def test_uisut_uitrigger_constructor_args():
    sig = inspect.signature(uisut_UITrigger.__init__)
    params = list(sig.parameters.keys())



def test_uisut_uitransition_is_not_abstract():
    assert not inspect.isabstract(uisut_UITransition)


def test_uisut_uitransition_constructor_exists():
    assert callable(uisut_UITransition.__init__)


def test_uisut_uitransition_constructor_args():
    sig = inspect.signature(uisut_UITransition.__init__)
    params = list(sig.parameters.keys())
    assert "scriptStr" in params, "Missing parameter 'scriptStr'"
    assert "guardStr" in params, "Missing parameter 'guardStr'"
    assert "triggerStr" in params, "Missing parameter 'triggerStr'"
    assert "actionStr" in params, "Missing parameter 'actionStr'"

def test_uisut_uitransition_has_scriptStr():
    assert hasattr(uisut_UITransition, "scriptStr")
    descriptor = None
    for klass in uisut_UITransition.__mro__:
        if "scriptStr" in klass.__dict__:
            descriptor = klass.__dict__["scriptStr"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uitransition_has_guardStr():
    assert hasattr(uisut_UITransition, "guardStr")
    descriptor = None
    for klass in uisut_UITransition.__mro__:
        if "guardStr" in klass.__dict__:
            descriptor = klass.__dict__["guardStr"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uitransition_has_triggerStr():
    assert hasattr(uisut_UITransition, "triggerStr")
    descriptor = None
    for klass in uisut_UITransition.__mro__:
        if "triggerStr" in klass.__dict__:
            descriptor = klass.__dict__["triggerStr"]
            break
    assert isinstance(descriptor, property)

def test_uisut_uitransition_has_actionStr():
    assert hasattr(uisut_UITransition, "actionStr")
    descriptor = None
    for klass in uisut_UITransition.__mro__:
        if "actionStr" in klass.__dict__:
            descriptor = klass.__dict__["actionStr"]
            break
    assert isinstance(descriptor, property)



def test_uisut_uidatavariable_is_not_abstract():
    assert not inspect.isabstract(uisut_UIDataVariable)


def test_uisut_uidatavariable_constructor_exists():
    assert callable(uisut_UIDataVariable.__init__)


def test_uisut_uidatavariable_constructor_args():
    sig = inspect.signature(uisut_UIDataVariable.__init__)
    params = list(sig.parameters.keys())
    assert "constraintRE" in params, "Missing parameter 'constraintRE'"

def test_uisut_uidatavariable_has_constraintRE():
    assert hasattr(uisut_UIDataVariable, "constraintRE")
    descriptor = None
    for klass in uisut_UIDataVariable.__mro__:
        if "constraintRE" in klass.__dict__:
            descriptor = klass.__dict__["constraintRE"]
            break
    assert isinstance(descriptor, property)



def test_uisut_uisut_is_not_abstract():
    assert not inspect.isabstract(uisut_UISUT)


def test_uisut_uisut_constructor_exists():
    assert callable(uisut_UISUT.__init__)


def test_uisut_uisut_constructor_args():
    sig = inspect.signature(uisut_UISUT.__init__)
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
uisut_UISUTElement_strategy = st.builds(
    uisut_UISUTElement,
    description=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
UITrigger_strategy = st.builds(
    UITrigger,
)
uisut_ComponentTrigger_strategy = st.builds(
    uisut_ComponentTrigger,
)
uisut_UserTrigger_strategy = st.builds(
    uisut_UserTrigger,
)
AbstractState_strategy = st.builds(
    AbstractState,
)
uisut_FinalState_strategy = st.builds(
    uisut_FinalState,
)
uisut_InitialState_strategy = st.builds(
    uisut_InitialState,
)
uisut_UIState_strategy = st.builds(
    uisut_UIState,
    isInitial=
        st.booleans(),
    pic=
        safe_text
)
UISUTElement_strategy = st.builds(
    UISUTElement,
)
uisut_ApplicationSystem_strategy = st.builds(
    uisut_ApplicationSystem,
)
uisut_UICondition_strategy = st.builds(
    uisut_UICondition,
)
uisut_UIControl_strategy = st.builds(
    uisut_UIControl,
    variableName=
        safe_text,
    valueExpression=
        safe_text
)
uisut_AbstractState_strategy = st.builds(
    uisut_AbstractState,
)
uisut_UIStatemachine_strategy = st.builds(
    uisut_UIStatemachine,
)
uisut_Action_strategy = st.builds(
    uisut_Action,
)
uisut_UITrigger_strategy = st.builds(
    uisut_UITrigger,
)
uisut_UITransition_strategy = st.builds(
    uisut_UITransition,
    scriptStr=
        safe_text,
    guardStr=
        safe_text,
    triggerStr=
        safe_text,
    actionStr=
        safe_text
)
uisut_UIDataVariable_strategy = st.builds(
    uisut_UIDataVariable,
    constraintRE=
        safe_text
)
uisut_UISUT_strategy = st.builds(
    uisut_UISUT,
)

@given(instance=uisut_UISUTElement_strategy)
@settings(max_examples=50)
def test_uisut_uisutelement_instantiation(instance):
    assert isinstance(instance, uisut_UISUTElement)



@given(instance=uisut_UISUTElement_strategy)
def test_uisut_uisutelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=uisut_UISUTElement_strategy)
def test_uisut_uisutelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=uisut_UISUTElement_strategy)
def test_uisut_uisutelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=UITrigger_strategy)
@settings(max_examples=50)
def test_uitrigger_instantiation(instance):
    assert isinstance(instance, UITrigger)

@given(instance=uisut_ComponentTrigger_strategy)
@settings(max_examples=50)
def test_uisut_componenttrigger_instantiation(instance):
    assert isinstance(instance, uisut_ComponentTrigger)

@given(instance=uisut_UserTrigger_strategy)
@settings(max_examples=50)
def test_uisut_usertrigger_instantiation(instance):
    assert isinstance(instance, uisut_UserTrigger)

@given(instance=AbstractState_strategy)
@settings(max_examples=50)
def test_abstractstate_instantiation(instance):
    assert isinstance(instance, AbstractState)

@given(instance=uisut_FinalState_strategy)
@settings(max_examples=50)
def test_uisut_finalstate_instantiation(instance):
    assert isinstance(instance, uisut_FinalState)

@given(instance=uisut_InitialState_strategy)
@settings(max_examples=50)
def test_uisut_initialstate_instantiation(instance):
    assert isinstance(instance, uisut_InitialState)

@given(instance=uisut_UIState_strategy)
@settings(max_examples=50)
def test_uisut_uistate_instantiation(instance):
    assert isinstance(instance, uisut_UIState)



@given(instance=uisut_UIState_strategy)
def test_uisut_uistate_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original



@given(instance=uisut_UIState_strategy)
def test_uisut_uistate_pic_setter(instance):
    original = instance.pic
    instance.pic = original
    assert instance.pic == original

@given(instance=UISUTElement_strategy)
@settings(max_examples=50)
def test_uisutelement_instantiation(instance):
    assert isinstance(instance, UISUTElement)

@given(instance=uisut_ApplicationSystem_strategy)
@settings(max_examples=50)
def test_uisut_applicationsystem_instantiation(instance):
    assert isinstance(instance, uisut_ApplicationSystem)

@given(instance=uisut_UICondition_strategy)
@settings(max_examples=50)
def test_uisut_uicondition_instantiation(instance):
    assert isinstance(instance, uisut_UICondition)

@given(instance=uisut_UIControl_strategy)
@settings(max_examples=50)
def test_uisut_uicontrol_instantiation(instance):
    assert isinstance(instance, uisut_UIControl)



@given(instance=uisut_UIControl_strategy)
def test_uisut_uicontrol_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original



@given(instance=uisut_UIControl_strategy)
def test_uisut_uicontrol_valueExpression_setter(instance):
    original = instance.valueExpression
    instance.valueExpression = original
    assert instance.valueExpression == original

@given(instance=uisut_AbstractState_strategy)
@settings(max_examples=50)
def test_uisut_abstractstate_instantiation(instance):
    assert isinstance(instance, uisut_AbstractState)

@given(instance=uisut_UIStatemachine_strategy)
@settings(max_examples=50)
def test_uisut_uistatemachine_instantiation(instance):
    assert isinstance(instance, uisut_UIStatemachine)

@given(instance=uisut_Action_strategy)
@settings(max_examples=50)
def test_uisut_action_instantiation(instance):
    assert isinstance(instance, uisut_Action)

@given(instance=uisut_UITrigger_strategy)
@settings(max_examples=50)
def test_uisut_uitrigger_instantiation(instance):
    assert isinstance(instance, uisut_UITrigger)

@given(instance=uisut_UITransition_strategy)
@settings(max_examples=50)
def test_uisut_uitransition_instantiation(instance):
    assert isinstance(instance, uisut_UITransition)



@given(instance=uisut_UITransition_strategy)
def test_uisut_uitransition_scriptStr_setter(instance):
    original = instance.scriptStr
    instance.scriptStr = original
    assert instance.scriptStr == original



@given(instance=uisut_UITransition_strategy)
def test_uisut_uitransition_guardStr_setter(instance):
    original = instance.guardStr
    instance.guardStr = original
    assert instance.guardStr == original



@given(instance=uisut_UITransition_strategy)
def test_uisut_uitransition_triggerStr_setter(instance):
    original = instance.triggerStr
    instance.triggerStr = original
    assert instance.triggerStr == original



@given(instance=uisut_UITransition_strategy)
def test_uisut_uitransition_actionStr_setter(instance):
    original = instance.actionStr
    instance.actionStr = original
    assert instance.actionStr == original

@given(instance=uisut_UIDataVariable_strategy)
@settings(max_examples=50)
def test_uisut_uidatavariable_instantiation(instance):
    assert isinstance(instance, uisut_UIDataVariable)



@given(instance=uisut_UIDataVariable_strategy)
def test_uisut_uidatavariable_constraintRE_setter(instance):
    original = instance.constraintRE
    instance.constraintRE = original
    assert instance.constraintRE == original

@given(instance=uisut_UISUT_strategy)
@settings(max_examples=50)
def test_uisut_uisut_instantiation(instance):
    assert isinstance(instance, uisut_UISUT)
