import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IsInStateCondition,
    sooml::ParameterIsInStateCondition,
    sooml::ReferenceIsInStateCondition,
    Guard,
    sooml::IsInStateCondition,
    sooml::ParameterBinding,
    Action,
    sooml::ReferenceAssignmentAction,
    sooml::CallOperationAction,
    CallOperationAction,
    sooml::CallParameterOperationAction,
    sooml::CallReferenceOperationAction,
    sooml::Transition,
    StructuralFeature,
    sooml::Reference,
    sooml::Attribute,
    sooml::Event,
    sooml::Guard,
    sooml::Action,
    sooml::EntryOperation,
    NamedElement,
    sooml::State,
    sooml::Parameter,
    sooml::StructuralFeature,
    sooml::Package,
    sooml::Operation,
    sooml::StateMachine,
    sooml::NamedElement,
    sooml::Class,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(IsInStateCondition)


def test_isinstatecondition_constructor_exists():
    assert callable(IsInStateCondition.__init__)


def test_isinstatecondition_constructor_args():
    sig = inspect.signature(IsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_sooml::parameterisinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml::ParameterIsInStateCondition)


def test_sooml::parameterisinstatecondition_constructor_exists():
    assert callable(sooml::ParameterIsInStateCondition.__init__)


def test_sooml::parameterisinstatecondition_constructor_args():
    sig = inspect.signature(sooml::ParameterIsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_sooml::referenceisinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml::ReferenceIsInStateCondition)


def test_sooml::referenceisinstatecondition_constructor_exists():
    assert callable(sooml::ReferenceIsInStateCondition.__init__)


def test_sooml::referenceisinstatecondition_constructor_args():
    sig = inspect.signature(sooml::ReferenceIsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_sooml::isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(sooml::IsInStateCondition)


def test_sooml::isinstatecondition_constructor_exists():
    assert callable(sooml::IsInStateCondition.__init__)


def test_sooml::isinstatecondition_constructor_args():
    sig = inspect.signature(sooml::IsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_sooml::parameterbinding_is_not_abstract():
    assert not inspect.isabstract(sooml::ParameterBinding)


def test_sooml::parameterbinding_constructor_exists():
    assert callable(sooml::ParameterBinding.__init__)


def test_sooml::parameterbinding_constructor_args():
    sig = inspect.signature(sooml::ParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_sooml::referenceassignmentaction_is_not_abstract():
    assert not inspect.isabstract(sooml::ReferenceAssignmentAction)


def test_sooml::referenceassignmentaction_constructor_exists():
    assert callable(sooml::ReferenceAssignmentAction.__init__)


def test_sooml::referenceassignmentaction_constructor_args():
    sig = inspect.signature(sooml::ReferenceAssignmentAction.__init__)
    params = list(sig.parameters.keys())



def test_sooml::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml::CallOperationAction)


def test_sooml::calloperationaction_constructor_exists():
    assert callable(sooml::CallOperationAction.__init__)


def test_sooml::calloperationaction_constructor_args():
    sig = inspect.signature(sooml::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CallOperationAction)


def test_calloperationaction_constructor_exists():
    assert callable(CallOperationAction.__init__)


def test_calloperationaction_constructor_args():
    sig = inspect.signature(CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_sooml::callparameteroperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml::CallParameterOperationAction)


def test_sooml::callparameteroperationaction_constructor_exists():
    assert callable(sooml::CallParameterOperationAction.__init__)


def test_sooml::callparameteroperationaction_constructor_args():
    sig = inspect.signature(sooml::CallParameterOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_sooml::callreferenceoperationaction_is_not_abstract():
    assert not inspect.isabstract(sooml::CallReferenceOperationAction)


def test_sooml::callreferenceoperationaction_constructor_exists():
    assert callable(sooml::CallReferenceOperationAction.__init__)


def test_sooml::callreferenceoperationaction_constructor_args():
    sig = inspect.signature(sooml::CallReferenceOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_sooml::transition_is_not_abstract():
    assert not inspect.isabstract(sooml::Transition)


def test_sooml::transition_constructor_exists():
    assert callable(sooml::Transition.__init__)


def test_sooml::transition_constructor_args():
    sig = inspect.signature(sooml::Transition.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_sooml::reference_is_not_abstract():
    assert not inspect.isabstract(sooml::Reference)


def test_sooml::reference_constructor_exists():
    assert callable(sooml::Reference.__init__)


def test_sooml::reference_constructor_args():
    sig = inspect.signature(sooml::Reference.__init__)
    params = list(sig.parameters.keys())



def test_sooml::attribute_is_not_abstract():
    assert not inspect.isabstract(sooml::Attribute)


def test_sooml::attribute_constructor_exists():
    assert callable(sooml::Attribute.__init__)


def test_sooml::attribute_constructor_args():
    sig = inspect.signature(sooml::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sooml::attribute_has_dataType():
    assert hasattr(sooml::Attribute, "dataType")
    descriptor = None
    for klass in sooml::Attribute.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sooml::event_is_not_abstract():
    assert not inspect.isabstract(sooml::Event)


def test_sooml::event_constructor_exists():
    assert callable(sooml::Event.__init__)


def test_sooml::event_constructor_args():
    sig = inspect.signature(sooml::Event.__init__)
    params = list(sig.parameters.keys())



def test_sooml::guard_is_not_abstract():
    assert not inspect.isabstract(sooml::Guard)


def test_sooml::guard_constructor_exists():
    assert callable(sooml::Guard.__init__)


def test_sooml::guard_constructor_args():
    sig = inspect.signature(sooml::Guard.__init__)
    params = list(sig.parameters.keys())



def test_sooml::action_is_not_abstract():
    assert not inspect.isabstract(sooml::Action)


def test_sooml::action_constructor_exists():
    assert callable(sooml::Action.__init__)


def test_sooml::action_constructor_args():
    sig = inspect.signature(sooml::Action.__init__)
    params = list(sig.parameters.keys())



def test_sooml::entryoperation_is_not_abstract():
    assert not inspect.isabstract(sooml::EntryOperation)


def test_sooml::entryoperation_constructor_exists():
    assert callable(sooml::EntryOperation.__init__)


def test_sooml::entryoperation_constructor_args():
    sig = inspect.signature(sooml::EntryOperation.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_sooml::state_is_not_abstract():
    assert not inspect.isabstract(sooml::State)


def test_sooml::state_constructor_exists():
    assert callable(sooml::State.__init__)


def test_sooml::state_constructor_args():
    sig = inspect.signature(sooml::State.__init__)
    params = list(sig.parameters.keys())



def test_sooml::parameter_is_not_abstract():
    assert not inspect.isabstract(sooml::Parameter)


def test_sooml::parameter_constructor_exists():
    assert callable(sooml::Parameter.__init__)


def test_sooml::parameter_constructor_args():
    sig = inspect.signature(sooml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sooml::parameter_has_dataType():
    assert hasattr(sooml::Parameter, "dataType")
    descriptor = None
    for klass in sooml::Parameter.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sooml::structuralfeature_is_not_abstract():
    assert not inspect.isabstract(sooml::StructuralFeature)


def test_sooml::structuralfeature_constructor_exists():
    assert callable(sooml::StructuralFeature.__init__)


def test_sooml::structuralfeature_constructor_args():
    sig = inspect.signature(sooml::StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"

def test_sooml::structuralfeature_has_upperBound():
    assert hasattr(sooml::StructuralFeature, "upperBound")
    descriptor = None
    for klass in sooml::StructuralFeature.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_sooml::structuralfeature_has_lowerBound():
    assert hasattr(sooml::StructuralFeature, "lowerBound")
    descriptor = None
    for klass in sooml::StructuralFeature.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)



def test_sooml::package_is_not_abstract():
    assert not inspect.isabstract(sooml::Package)


def test_sooml::package_constructor_exists():
    assert callable(sooml::Package.__init__)


def test_sooml::package_constructor_args():
    sig = inspect.signature(sooml::Package.__init__)
    params = list(sig.parameters.keys())



def test_sooml::operation_is_not_abstract():
    assert not inspect.isabstract(sooml::Operation)


def test_sooml::operation_constructor_exists():
    assert callable(sooml::Operation.__init__)


def test_sooml::operation_constructor_args():
    sig = inspect.signature(sooml::Operation.__init__)
    params = list(sig.parameters.keys())



def test_sooml::statemachine_is_not_abstract():
    assert not inspect.isabstract(sooml::StateMachine)


def test_sooml::statemachine_constructor_exists():
    assert callable(sooml::StateMachine.__init__)


def test_sooml::statemachine_constructor_args():
    sig = inspect.signature(sooml::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sooml::namedelement_is_not_abstract():
    assert not inspect.isabstract(sooml::NamedElement)


def test_sooml::namedelement_constructor_exists():
    assert callable(sooml::NamedElement.__init__)


def test_sooml::namedelement_constructor_args():
    sig = inspect.signature(sooml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sooml::namedelement_has_name():
    assert hasattr(sooml::NamedElement, "name")
    descriptor = None
    for klass in sooml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sooml::class_is_not_abstract():
    assert not inspect.isabstract(sooml::Class)


def test_sooml::class_constructor_exists():
    assert callable(sooml::Class.__init__)


def test_sooml::class_constructor_args():
    sig = inspect.signature(sooml::Class.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "String",
        "Boolean",
        "Integer",
        "Complex",
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
IsInStateCondition_strategy = st.builds(
    IsInStateCondition,
)
sooml::ParameterIsInStateCondition_strategy = st.builds(
    sooml::ParameterIsInStateCondition,
)
sooml::ReferenceIsInStateCondition_strategy = st.builds(
    sooml::ReferenceIsInStateCondition,
)
Guard_strategy = st.builds(
    Guard,
)
sooml::IsInStateCondition_strategy = st.builds(
    sooml::IsInStateCondition,
)
sooml::ParameterBinding_strategy = st.builds(
    sooml::ParameterBinding,
)
Action_strategy = st.builds(
    Action,
)
sooml::ReferenceAssignmentAction_strategy = st.builds(
    sooml::ReferenceAssignmentAction,
)
sooml::CallOperationAction_strategy = st.builds(
    sooml::CallOperationAction,
)
CallOperationAction_strategy = st.builds(
    CallOperationAction,
)
sooml::CallParameterOperationAction_strategy = st.builds(
    sooml::CallParameterOperationAction,
)
sooml::CallReferenceOperationAction_strategy = st.builds(
    sooml::CallReferenceOperationAction,
)
sooml::Transition_strategy = st.builds(
    sooml::Transition,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
sooml::Reference_strategy = st.builds(
    sooml::Reference,
)
sooml::Attribute_strategy = st.builds(
    sooml::Attribute,
    dataType=
        safe_text
)
sooml::Event_strategy = st.builds(
    sooml::Event,
)
sooml::Guard_strategy = st.builds(
    sooml::Guard,
)
sooml::Action_strategy = st.builds(
    sooml::Action,
)
sooml::EntryOperation_strategy = st.builds(
    sooml::EntryOperation,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
sooml::State_strategy = st.builds(
    sooml::State,
)
sooml::Parameter_strategy = st.builds(
    sooml::Parameter,
    dataType=
        safe_text
)
sooml::StructuralFeature_strategy = st.builds(
    sooml::StructuralFeature,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers()
)
sooml::Package_strategy = st.builds(
    sooml::Package,
)
sooml::Operation_strategy = st.builds(
    sooml::Operation,
)
sooml::StateMachine_strategy = st.builds(
    sooml::StateMachine,
)
sooml::NamedElement_strategy = st.builds(
    sooml::NamedElement,
    name=
        safe_text
)
sooml::Class_strategy = st.builds(
    sooml::Class,
)

@given(instance=IsInStateCondition_strategy)
@settings(max_examples=50)
def test_isinstatecondition_instantiation(instance):
    assert isinstance(instance, IsInStateCondition)

@given(instance=sooml::ParameterIsInStateCondition_strategy)
@settings(max_examples=50)
def test_sooml::parameterisinstatecondition_instantiation(instance):
    assert isinstance(instance, sooml::ParameterIsInStateCondition)

@given(instance=sooml::ReferenceIsInStateCondition_strategy)
@settings(max_examples=50)
def test_sooml::referenceisinstatecondition_instantiation(instance):
    assert isinstance(instance, sooml::ReferenceIsInStateCondition)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=sooml::IsInStateCondition_strategy)
@settings(max_examples=50)
def test_sooml::isinstatecondition_instantiation(instance):
    assert isinstance(instance, sooml::IsInStateCondition)

@given(instance=sooml::ParameterBinding_strategy)
@settings(max_examples=50)
def test_sooml::parameterbinding_instantiation(instance):
    assert isinstance(instance, sooml::ParameterBinding)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=sooml::ReferenceAssignmentAction_strategy)
@settings(max_examples=50)
def test_sooml::referenceassignmentaction_instantiation(instance):
    assert isinstance(instance, sooml::ReferenceAssignmentAction)

@given(instance=sooml::CallOperationAction_strategy)
@settings(max_examples=50)
def test_sooml::calloperationaction_instantiation(instance):
    assert isinstance(instance, sooml::CallOperationAction)

@given(instance=CallOperationAction_strategy)
@settings(max_examples=50)
def test_calloperationaction_instantiation(instance):
    assert isinstance(instance, CallOperationAction)

@given(instance=sooml::CallParameterOperationAction_strategy)
@settings(max_examples=50)
def test_sooml::callparameteroperationaction_instantiation(instance):
    assert isinstance(instance, sooml::CallParameterOperationAction)

@given(instance=sooml::CallReferenceOperationAction_strategy)
@settings(max_examples=50)
def test_sooml::callreferenceoperationaction_instantiation(instance):
    assert isinstance(instance, sooml::CallReferenceOperationAction)

@given(instance=sooml::Transition_strategy)
@settings(max_examples=50)
def test_sooml::transition_instantiation(instance):
    assert isinstance(instance, sooml::Transition)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=sooml::Reference_strategy)
@settings(max_examples=50)
def test_sooml::reference_instantiation(instance):
    assert isinstance(instance, sooml::Reference)

@given(instance=sooml::Attribute_strategy)
@settings(max_examples=50)
def test_sooml::attribute_instantiation(instance):
    assert isinstance(instance, sooml::Attribute)

@given(instance=sooml::Attribute_strategy)
def test_sooml::attribute_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=sooml::Attribute_strategy)
def test_sooml::attribute_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sooml::Event_strategy)
@settings(max_examples=50)
def test_sooml::event_instantiation(instance):
    assert isinstance(instance, sooml::Event)

@given(instance=sooml::Guard_strategy)
@settings(max_examples=50)
def test_sooml::guard_instantiation(instance):
    assert isinstance(instance, sooml::Guard)

@given(instance=sooml::Action_strategy)
@settings(max_examples=50)
def test_sooml::action_instantiation(instance):
    assert isinstance(instance, sooml::Action)

@given(instance=sooml::EntryOperation_strategy)
@settings(max_examples=50)
def test_sooml::entryoperation_instantiation(instance):
    assert isinstance(instance, sooml::EntryOperation)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=sooml::State_strategy)
@settings(max_examples=50)
def test_sooml::state_instantiation(instance):
    assert isinstance(instance, sooml::State)

@given(instance=sooml::Parameter_strategy)
@settings(max_examples=50)
def test_sooml::parameter_instantiation(instance):
    assert isinstance(instance, sooml::Parameter)

@given(instance=sooml::Parameter_strategy)
def test_sooml::parameter_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=sooml::Parameter_strategy)
def test_sooml::parameter_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sooml::StructuralFeature_strategy)
@settings(max_examples=50)
def test_sooml::structuralfeature_instantiation(instance):
    assert isinstance(instance, sooml::StructuralFeature)

@given(instance=sooml::StructuralFeature_strategy)
def test_sooml::structuralfeature_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=sooml::StructuralFeature_strategy)
def test_sooml::structuralfeature_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=sooml::StructuralFeature_strategy)
def test_sooml::structuralfeature_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=sooml::StructuralFeature_strategy)
def test_sooml::structuralfeature_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=sooml::Package_strategy)
@settings(max_examples=50)
def test_sooml::package_instantiation(instance):
    assert isinstance(instance, sooml::Package)

@given(instance=sooml::Operation_strategy)
@settings(max_examples=50)
def test_sooml::operation_instantiation(instance):
    assert isinstance(instance, sooml::Operation)

@given(instance=sooml::StateMachine_strategy)
@settings(max_examples=50)
def test_sooml::statemachine_instantiation(instance):
    assert isinstance(instance, sooml::StateMachine)

@given(instance=sooml::NamedElement_strategy)
@settings(max_examples=50)
def test_sooml::namedelement_instantiation(instance):
    assert isinstance(instance, sooml::NamedElement)

@given(instance=sooml::NamedElement_strategy)
def test_sooml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sooml::NamedElement_strategy)
def test_sooml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sooml::Class_strategy)
@settings(max_examples=50)
def test_sooml::class_instantiation(instance):
    assert isinstance(instance, sooml::Class)
