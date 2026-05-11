import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Parameter,
    soopl::ComplexTypeParameter,
    soopl::SimpleTypeParameter,
    soopl::Guard,
    soopl::Action,
    soopl::Transition,
    Method,
    soopl::TransitionMethod,
    soopl::ParameterBinding,
    Action,
    soopl::CallMethodAction,
    Class,
    soopl::StateClass,
    soopl::StateImplementationClass,
    soopl::StatefulClass,
    NamedElement,
    soopl::Method,
    soopl::Parameter,
    soopl::Class,
    soopl::Property,
    soopl::Package,
    soopl::NamedElement,
    Property,
    soopl::ComplexTypeProperty,
    soopl::SimpleTypeProperty,
    soopl::AssignProperty,
    CallMethodAction,
    soopl::CallMethodOfParameter,
    soopl::CallMethodOfProperty,
    IsInStateCondition,
    soopl::ParameterIsInState,
    soopl::PropertyIsInState,
    Guard,
    soopl::IsInStateCondition,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_soopl::complextypeparameter_is_not_abstract():
    assert not inspect.isabstract(soopl::ComplexTypeParameter)


def test_soopl::complextypeparameter_constructor_exists():
    assert callable(soopl::ComplexTypeParameter.__init__)


def test_soopl::complextypeparameter_constructor_args():
    sig = inspect.signature(soopl::ComplexTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_soopl::simpletypeparameter_is_not_abstract():
    assert not inspect.isabstract(soopl::SimpleTypeParameter)


def test_soopl::simpletypeparameter_constructor_exists():
    assert callable(soopl::SimpleTypeParameter.__init__)


def test_soopl::simpletypeparameter_constructor_args():
    sig = inspect.signature(soopl::SimpleTypeParameter.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_soopl::simpletypeparameter_has_dataType():
    assert hasattr(soopl::SimpleTypeParameter, "dataType")
    descriptor = None
    for klass in soopl::SimpleTypeParameter.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_soopl::guard_is_not_abstract():
    assert not inspect.isabstract(soopl::Guard)


def test_soopl::guard_constructor_exists():
    assert callable(soopl::Guard.__init__)


def test_soopl::guard_constructor_args():
    sig = inspect.signature(soopl::Guard.__init__)
    params = list(sig.parameters.keys())



def test_soopl::action_is_not_abstract():
    assert not inspect.isabstract(soopl::Action)


def test_soopl::action_constructor_exists():
    assert callable(soopl::Action.__init__)


def test_soopl::action_constructor_args():
    sig = inspect.signature(soopl::Action.__init__)
    params = list(sig.parameters.keys())



def test_soopl::transition_is_not_abstract():
    assert not inspect.isabstract(soopl::Transition)


def test_soopl::transition_constructor_exists():
    assert callable(soopl::Transition.__init__)


def test_soopl::transition_constructor_args():
    sig = inspect.signature(soopl::Transition.__init__)
    params = list(sig.parameters.keys())



def test_method_is_not_abstract():
    assert not inspect.isabstract(Method)


def test_method_constructor_exists():
    assert callable(Method.__init__)


def test_method_constructor_args():
    sig = inspect.signature(Method.__init__)
    params = list(sig.parameters.keys())



def test_soopl::transitionmethod_is_not_abstract():
    assert not inspect.isabstract(soopl::TransitionMethod)


def test_soopl::transitionmethod_constructor_exists():
    assert callable(soopl::TransitionMethod.__init__)


def test_soopl::transitionmethod_constructor_args():
    sig = inspect.signature(soopl::TransitionMethod.__init__)
    params = list(sig.parameters.keys())



def test_soopl::parameterbinding_is_not_abstract():
    assert not inspect.isabstract(soopl::ParameterBinding)


def test_soopl::parameterbinding_constructor_exists():
    assert callable(soopl::ParameterBinding.__init__)


def test_soopl::parameterbinding_constructor_args():
    sig = inspect.signature(soopl::ParameterBinding.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_soopl::callmethodaction_is_not_abstract():
    assert not inspect.isabstract(soopl::CallMethodAction)


def test_soopl::callmethodaction_constructor_exists():
    assert callable(soopl::CallMethodAction.__init__)


def test_soopl::callmethodaction_constructor_args():
    sig = inspect.signature(soopl::CallMethodAction.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_soopl::stateclass_is_not_abstract():
    assert not inspect.isabstract(soopl::StateClass)


def test_soopl::stateclass_constructor_exists():
    assert callable(soopl::StateClass.__init__)


def test_soopl::stateclass_constructor_args():
    sig = inspect.signature(soopl::StateClass.__init__)
    params = list(sig.parameters.keys())



def test_soopl::stateimplementationclass_is_not_abstract():
    assert not inspect.isabstract(soopl::StateImplementationClass)


def test_soopl::stateimplementationclass_constructor_exists():
    assert callable(soopl::StateImplementationClass.__init__)


def test_soopl::stateimplementationclass_constructor_args():
    sig = inspect.signature(soopl::StateImplementationClass.__init__)
    params = list(sig.parameters.keys())



def test_soopl::statefulclass_is_not_abstract():
    assert not inspect.isabstract(soopl::StatefulClass)


def test_soopl::statefulclass_constructor_exists():
    assert callable(soopl::StatefulClass.__init__)


def test_soopl::statefulclass_constructor_args():
    sig = inspect.signature(soopl::StatefulClass.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_soopl::method_is_not_abstract():
    assert not inspect.isabstract(soopl::Method)


def test_soopl::method_constructor_exists():
    assert callable(soopl::Method.__init__)


def test_soopl::method_constructor_args():
    sig = inspect.signature(soopl::Method.__init__)
    params = list(sig.parameters.keys())



def test_soopl::parameter_is_not_abstract():
    assert not inspect.isabstract(soopl::Parameter)


def test_soopl::parameter_constructor_exists():
    assert callable(soopl::Parameter.__init__)


def test_soopl::parameter_constructor_args():
    sig = inspect.signature(soopl::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_soopl::class_is_not_abstract():
    assert not inspect.isabstract(soopl::Class)


def test_soopl::class_constructor_exists():
    assert callable(soopl::Class.__init__)


def test_soopl::class_constructor_args():
    sig = inspect.signature(soopl::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_soopl::class_has_isAbstract():
    assert hasattr(soopl::Class, "isAbstract")
    descriptor = None
    for klass in soopl::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_soopl::property_is_not_abstract():
    assert not inspect.isabstract(soopl::Property)


def test_soopl::property_constructor_exists():
    assert callable(soopl::Property.__init__)


def test_soopl::property_constructor_args():
    sig = inspect.signature(soopl::Property.__init__)
    params = list(sig.parameters.keys())
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "multiValued" in params, "Missing parameter 'multiValued'"

def test_soopl::property_has_upperBound():
    assert hasattr(soopl::Property, "upperBound")
    descriptor = None
    for klass in soopl::Property.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_soopl::property_has_lowerBound():
    assert hasattr(soopl::Property, "lowerBound")
    descriptor = None
    for klass in soopl::Property.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_soopl::property_has_multiValued():
    assert hasattr(soopl::Property, "multiValued")
    descriptor = None
    for klass in soopl::Property.__mro__:
        if "multiValued" in klass.__dict__:
            descriptor = klass.__dict__["multiValued"]
            break
    assert isinstance(descriptor, property)



def test_soopl::package_is_not_abstract():
    assert not inspect.isabstract(soopl::Package)


def test_soopl::package_constructor_exists():
    assert callable(soopl::Package.__init__)


def test_soopl::package_constructor_args():
    sig = inspect.signature(soopl::Package.__init__)
    params = list(sig.parameters.keys())



def test_soopl::namedelement_is_not_abstract():
    assert not inspect.isabstract(soopl::NamedElement)


def test_soopl::namedelement_constructor_exists():
    assert callable(soopl::NamedElement.__init__)


def test_soopl::namedelement_constructor_args():
    sig = inspect.signature(soopl::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_soopl::namedelement_has_name():
    assert hasattr(soopl::NamedElement, "name")
    descriptor = None
    for klass in soopl::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_soopl::complextypeproperty_is_not_abstract():
    assert not inspect.isabstract(soopl::ComplexTypeProperty)


def test_soopl::complextypeproperty_constructor_exists():
    assert callable(soopl::ComplexTypeProperty.__init__)


def test_soopl::complextypeproperty_constructor_args():
    sig = inspect.signature(soopl::ComplexTypeProperty.__init__)
    params = list(sig.parameters.keys())



def test_soopl::simpletypeproperty_is_not_abstract():
    assert not inspect.isabstract(soopl::SimpleTypeProperty)


def test_soopl::simpletypeproperty_constructor_exists():
    assert callable(soopl::SimpleTypeProperty.__init__)


def test_soopl::simpletypeproperty_constructor_args():
    sig = inspect.signature(soopl::SimpleTypeProperty.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_soopl::simpletypeproperty_has_dataType():
    assert hasattr(soopl::SimpleTypeProperty, "dataType")
    descriptor = None
    for klass in soopl::SimpleTypeProperty.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_soopl::assignproperty_is_not_abstract():
    assert not inspect.isabstract(soopl::AssignProperty)


def test_soopl::assignproperty_constructor_exists():
    assert callable(soopl::AssignProperty.__init__)


def test_soopl::assignproperty_constructor_args():
    sig = inspect.signature(soopl::AssignProperty.__init__)
    params = list(sig.parameters.keys())



def test_callmethodaction_is_not_abstract():
    assert not inspect.isabstract(CallMethodAction)


def test_callmethodaction_constructor_exists():
    assert callable(CallMethodAction.__init__)


def test_callmethodaction_constructor_args():
    sig = inspect.signature(CallMethodAction.__init__)
    params = list(sig.parameters.keys())



def test_soopl::callmethodofparameter_is_not_abstract():
    assert not inspect.isabstract(soopl::CallMethodOfParameter)


def test_soopl::callmethodofparameter_constructor_exists():
    assert callable(soopl::CallMethodOfParameter.__init__)


def test_soopl::callmethodofparameter_constructor_args():
    sig = inspect.signature(soopl::CallMethodOfParameter.__init__)
    params = list(sig.parameters.keys())



def test_soopl::callmethodofproperty_is_not_abstract():
    assert not inspect.isabstract(soopl::CallMethodOfProperty)


def test_soopl::callmethodofproperty_constructor_exists():
    assert callable(soopl::CallMethodOfProperty.__init__)


def test_soopl::callmethodofproperty_constructor_args():
    sig = inspect.signature(soopl::CallMethodOfProperty.__init__)
    params = list(sig.parameters.keys())



def test_isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(IsInStateCondition)


def test_isinstatecondition_constructor_exists():
    assert callable(IsInStateCondition.__init__)


def test_isinstatecondition_constructor_args():
    sig = inspect.signature(IsInStateCondition.__init__)
    params = list(sig.parameters.keys())



def test_soopl::parameterisinstate_is_not_abstract():
    assert not inspect.isabstract(soopl::ParameterIsInState)


def test_soopl::parameterisinstate_constructor_exists():
    assert callable(soopl::ParameterIsInState.__init__)


def test_soopl::parameterisinstate_constructor_args():
    sig = inspect.signature(soopl::ParameterIsInState.__init__)
    params = list(sig.parameters.keys())



def test_soopl::propertyisinstate_is_not_abstract():
    assert not inspect.isabstract(soopl::PropertyIsInState)


def test_soopl::propertyisinstate_constructor_exists():
    assert callable(soopl::PropertyIsInState.__init__)


def test_soopl::propertyisinstate_constructor_args():
    sig = inspect.signature(soopl::PropertyIsInState.__init__)
    params = list(sig.parameters.keys())



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_soopl::isinstatecondition_is_not_abstract():
    assert not inspect.isabstract(soopl::IsInStateCondition)


def test_soopl::isinstatecondition_constructor_exists():
    assert callable(soopl::IsInStateCondition.__init__)


def test_soopl::isinstatecondition_constructor_args():
    sig = inspect.signature(soopl::IsInStateCondition.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "Integer",
        "Boolean",
        "String",
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
Parameter_strategy = st.builds(
    Parameter,
)
soopl::ComplexTypeParameter_strategy = st.builds(
    soopl::ComplexTypeParameter,
)
soopl::SimpleTypeParameter_strategy = st.builds(
    soopl::SimpleTypeParameter,
    dataType=
        safe_text
)
soopl::Guard_strategy = st.builds(
    soopl::Guard,
)
soopl::Action_strategy = st.builds(
    soopl::Action,
)
soopl::Transition_strategy = st.builds(
    soopl::Transition,
)
Method_strategy = st.builds(
    Method,
)
soopl::TransitionMethod_strategy = st.builds(
    soopl::TransitionMethod,
)
soopl::ParameterBinding_strategy = st.builds(
    soopl::ParameterBinding,
)
Action_strategy = st.builds(
    Action,
)
soopl::CallMethodAction_strategy = st.builds(
    soopl::CallMethodAction,
)
Class_strategy = st.builds(
    Class,
)
soopl::StateClass_strategy = st.builds(
    soopl::StateClass,
)
soopl::StateImplementationClass_strategy = st.builds(
    soopl::StateImplementationClass,
)
soopl::StatefulClass_strategy = st.builds(
    soopl::StatefulClass,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
soopl::Method_strategy = st.builds(
    soopl::Method,
)
soopl::Parameter_strategy = st.builds(
    soopl::Parameter,
)
soopl::Class_strategy = st.builds(
    soopl::Class,
    isAbstract=
        st.booleans()
)
soopl::Property_strategy = st.builds(
    soopl::Property,
    upperBound=
        st.integers(),
    lowerBound=
        st.integers(),
    multiValued=
        st.booleans()
)
soopl::Package_strategy = st.builds(
    soopl::Package,
)
soopl::NamedElement_strategy = st.builds(
    soopl::NamedElement,
    name=
        safe_text
)
Property_strategy = st.builds(
    Property,
)
soopl::ComplexTypeProperty_strategy = st.builds(
    soopl::ComplexTypeProperty,
)
soopl::SimpleTypeProperty_strategy = st.builds(
    soopl::SimpleTypeProperty,
    dataType=
        safe_text
)
soopl::AssignProperty_strategy = st.builds(
    soopl::AssignProperty,
)
CallMethodAction_strategy = st.builds(
    CallMethodAction,
)
soopl::CallMethodOfParameter_strategy = st.builds(
    soopl::CallMethodOfParameter,
)
soopl::CallMethodOfProperty_strategy = st.builds(
    soopl::CallMethodOfProperty,
)
IsInStateCondition_strategy = st.builds(
    IsInStateCondition,
)
soopl::ParameterIsInState_strategy = st.builds(
    soopl::ParameterIsInState,
)
soopl::PropertyIsInState_strategy = st.builds(
    soopl::PropertyIsInState,
)
Guard_strategy = st.builds(
    Guard,
)
soopl::IsInStateCondition_strategy = st.builds(
    soopl::IsInStateCondition,
)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=soopl::ComplexTypeParameter_strategy)
@settings(max_examples=50)
def test_soopl::complextypeparameter_instantiation(instance):
    assert isinstance(instance, soopl::ComplexTypeParameter)

@given(instance=soopl::SimpleTypeParameter_strategy)
@settings(max_examples=50)
def test_soopl::simpletypeparameter_instantiation(instance):
    assert isinstance(instance, soopl::SimpleTypeParameter)

@given(instance=soopl::SimpleTypeParameter_strategy)
def test_soopl::simpletypeparameter_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=soopl::SimpleTypeParameter_strategy)
def test_soopl::simpletypeparameter_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=soopl::Guard_strategy)
@settings(max_examples=50)
def test_soopl::guard_instantiation(instance):
    assert isinstance(instance, soopl::Guard)

@given(instance=soopl::Action_strategy)
@settings(max_examples=50)
def test_soopl::action_instantiation(instance):
    assert isinstance(instance, soopl::Action)

@given(instance=soopl::Transition_strategy)
@settings(max_examples=50)
def test_soopl::transition_instantiation(instance):
    assert isinstance(instance, soopl::Transition)

@given(instance=Method_strategy)
@settings(max_examples=50)
def test_method_instantiation(instance):
    assert isinstance(instance, Method)

@given(instance=soopl::TransitionMethod_strategy)
@settings(max_examples=50)
def test_soopl::transitionmethod_instantiation(instance):
    assert isinstance(instance, soopl::TransitionMethod)

@given(instance=soopl::ParameterBinding_strategy)
@settings(max_examples=50)
def test_soopl::parameterbinding_instantiation(instance):
    assert isinstance(instance, soopl::ParameterBinding)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=soopl::CallMethodAction_strategy)
@settings(max_examples=50)
def test_soopl::callmethodaction_instantiation(instance):
    assert isinstance(instance, soopl::CallMethodAction)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=soopl::StateClass_strategy)
@settings(max_examples=50)
def test_soopl::stateclass_instantiation(instance):
    assert isinstance(instance, soopl::StateClass)

@given(instance=soopl::StateImplementationClass_strategy)
@settings(max_examples=50)
def test_soopl::stateimplementationclass_instantiation(instance):
    assert isinstance(instance, soopl::StateImplementationClass)

@given(instance=soopl::StatefulClass_strategy)
@settings(max_examples=50)
def test_soopl::statefulclass_instantiation(instance):
    assert isinstance(instance, soopl::StatefulClass)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=soopl::Method_strategy)
@settings(max_examples=50)
def test_soopl::method_instantiation(instance):
    assert isinstance(instance, soopl::Method)

@given(instance=soopl::Parameter_strategy)
@settings(max_examples=50)
def test_soopl::parameter_instantiation(instance):
    assert isinstance(instance, soopl::Parameter)

@given(instance=soopl::Class_strategy)
@settings(max_examples=50)
def test_soopl::class_instantiation(instance):
    assert isinstance(instance, soopl::Class)

@given(instance=soopl::Class_strategy)
def test_soopl::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=soopl::Class_strategy)
def test_soopl::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=soopl::Property_strategy)
@settings(max_examples=50)
def test_soopl::property_instantiation(instance):
    assert isinstance(instance, soopl::Property)

@given(instance=soopl::Property_strategy)
def test_soopl::property_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=soopl::Property_strategy)
def test_soopl::property_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=soopl::Property_strategy)
def test_soopl::property_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=soopl::Property_strategy)
def test_soopl::property_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=soopl::Property_strategy)
def test_soopl::property_multiValued_type(instance):
    assert isinstance(instance.multiValued, bool)


@given(instance=soopl::Property_strategy)
def test_soopl::property_multiValued_setter(instance):
    original = instance.multiValued
    instance.multiValued = original
    assert instance.multiValued == original

@given(instance=soopl::Package_strategy)
@settings(max_examples=50)
def test_soopl::package_instantiation(instance):
    assert isinstance(instance, soopl::Package)

@given(instance=soopl::NamedElement_strategy)
@settings(max_examples=50)
def test_soopl::namedelement_instantiation(instance):
    assert isinstance(instance, soopl::NamedElement)

@given(instance=soopl::NamedElement_strategy)
def test_soopl::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=soopl::NamedElement_strategy)
def test_soopl::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=soopl::ComplexTypeProperty_strategy)
@settings(max_examples=50)
def test_soopl::complextypeproperty_instantiation(instance):
    assert isinstance(instance, soopl::ComplexTypeProperty)

@given(instance=soopl::SimpleTypeProperty_strategy)
@settings(max_examples=50)
def test_soopl::simpletypeproperty_instantiation(instance):
    assert isinstance(instance, soopl::SimpleTypeProperty)

@given(instance=soopl::SimpleTypeProperty_strategy)
def test_soopl::simpletypeproperty_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=soopl::SimpleTypeProperty_strategy)
def test_soopl::simpletypeproperty_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=soopl::AssignProperty_strategy)
@settings(max_examples=50)
def test_soopl::assignproperty_instantiation(instance):
    assert isinstance(instance, soopl::AssignProperty)

@given(instance=CallMethodAction_strategy)
@settings(max_examples=50)
def test_callmethodaction_instantiation(instance):
    assert isinstance(instance, CallMethodAction)

@given(instance=soopl::CallMethodOfParameter_strategy)
@settings(max_examples=50)
def test_soopl::callmethodofparameter_instantiation(instance):
    assert isinstance(instance, soopl::CallMethodOfParameter)

@given(instance=soopl::CallMethodOfProperty_strategy)
@settings(max_examples=50)
def test_soopl::callmethodofproperty_instantiation(instance):
    assert isinstance(instance, soopl::CallMethodOfProperty)

@given(instance=IsInStateCondition_strategy)
@settings(max_examples=50)
def test_isinstatecondition_instantiation(instance):
    assert isinstance(instance, IsInStateCondition)

@given(instance=soopl::ParameterIsInState_strategy)
@settings(max_examples=50)
def test_soopl::parameterisinstate_instantiation(instance):
    assert isinstance(instance, soopl::ParameterIsInState)

@given(instance=soopl::PropertyIsInState_strategy)
@settings(max_examples=50)
def test_soopl::propertyisinstate_instantiation(instance):
    assert isinstance(instance, soopl::PropertyIsInState)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=soopl::IsInStateCondition_strategy)
@settings(max_examples=50)
def test_soopl::isinstatecondition_instantiation(instance):
    assert isinstance(instance, soopl::IsInStateCondition)
