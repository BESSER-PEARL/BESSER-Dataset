import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MultiplicityElement,
    UML2_ConnectorEnd,
    Property,
    UML2_Port,
    UML2_ExtensionEnd,
    InputPin,
    UML2_ValuePin,
    UML2_StructuralFeature,
    UML2_Pin,
    UML2_MultiplicityElement,
    UML2_Variable,
    UML2_Operation,
    UML2_Parameter,
    Pin,
    UML2_OutputPin,
    UML2_InputPin,
    StructuralFeature,
    UML2_Property,
    ParameterDirectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connectorend_is_not_abstract():
    assert not inspect.isabstract(UML2_ConnectorEnd)


def test_uml2_connectorend_constructor_exists():
    assert callable(UML2_ConnectorEnd.__init__)


def test_uml2_connectorend_constructor_args():
    sig = inspect.signature(UML2_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2_ValuePin)


def test_uml2_valuepin_constructor_exists():
    assert callable(UML2_ValuePin.__init__)


def test_uml2_valuepin_constructor_args():
    sig = inspect.signature(UML2_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeature)


def test_uml2_structuralfeature_constructor_exists():
    assert callable(UML2_StructuralFeature.__init__)


def test_uml2_structuralfeature_constructor_args():
    sig = inspect.signature(UML2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_pin_is_not_abstract():
    assert not inspect.isabstract(UML2_Pin)


def test_uml2_pin_constructor_exists():
    assert callable(UML2_Pin.__init__)


def test_uml2_pin_constructor_args():
    sig = inspect.signature(UML2_Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UML2_MultiplicityElement)


def test_uml2_multiplicityelement_constructor_exists():
    assert callable(UML2_MultiplicityElement.__init__)


def test_uml2_multiplicityelement_constructor_args():
    sig = inspect.signature(UML2_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_uml2_multiplicityelement_has_isUnique():
    assert hasattr(UML2_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in UML2_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_uml2_variable_is_not_abstract():
    assert not inspect.isabstract(UML2_Variable)


def test_uml2_variable_constructor_exists():
    assert callable(UML2_Variable.__init__)


def test_uml2_variable_constructor_args():
    sig = inspect.signature(UML2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operation_is_not_abstract():
    assert not inspect.isabstract(UML2_Operation)


def test_uml2_operation_constructor_exists():
    assert callable(UML2_Operation.__init__)


def test_uml2_operation_constructor_args():
    sig = inspect.signature(UML2_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2_Parameter)


def test_uml2_parameter_constructor_exists():
    assert callable(UML2_Parameter.__init__)


def test_uml2_parameter_constructor_args():
    sig = inspect.signature(UML2_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2_parameter_has_direction():
    assert hasattr(UML2_Parameter, "direction")
    descriptor = None
    for klass in UML2_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_OutputPin)


def test_uml2_outputpin_constructor_exists():
    assert callable(UML2_OutputPin.__init__)


def test_uml2_outputpin_constructor_args():
    sig = inspect.signature(UML2_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_InputPin)


def test_uml2_inputpin_constructor_exists():
    assert callable(UML2_InputPin.__init__)


def test_uml2_inputpin_constructor_args():
    sig = inspect.signature(UML2_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "inout",
        "return_",
        "out",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"


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
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UML2_ConnectorEnd_strategy = st.builds(
    UML2_ConnectorEnd,
)
Property_strategy = st.builds(
    Property,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2_ValuePin_strategy = st.builds(
    UML2_ValuePin,
)
UML2_StructuralFeature_strategy = st.builds(
    UML2_StructuralFeature,
)
UML2_Pin_strategy = st.builds(
    UML2_Pin,
)
UML2_MultiplicityElement_strategy = st.builds(
    UML2_MultiplicityElement,
    isUnique=
        st.booleans()
)
UML2_Variable_strategy = st.builds(
    UML2_Variable,
)
UML2_Operation_strategy = st.builds(
    UML2_Operation,
)
UML2_Parameter_strategy = st.builds(
    UML2_Parameter,
    direction=
        safe_text
)
Pin_strategy = st.builds(
    Pin,
)
UML2_OutputPin_strategy = st.builds(
    UML2_OutputPin,
)
UML2_InputPin_strategy = st.builds(
    UML2_InputPin,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UML2_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml2_connectorend_instantiation(instance):
    assert isinstance(instance, UML2_ConnectorEnd)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2_ValuePin_strategy)
@settings(max_examples=50)
def test_uml2_valuepin_instantiation(instance):
    assert isinstance(instance, UML2_ValuePin)

@given(instance=UML2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeature)

@given(instance=UML2_Pin_strategy)
@settings(max_examples=50)
def test_uml2_pin_instantiation(instance):
    assert isinstance(instance, UML2_Pin)

@given(instance=UML2_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml2_multiplicityelement_instantiation(instance):
    assert isinstance(instance, UML2_MultiplicityElement)



@given(instance=UML2_MultiplicityElement_strategy)
def test_uml2_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=UML2_Variable_strategy)
@settings(max_examples=50)
def test_uml2_variable_instantiation(instance):
    assert isinstance(instance, UML2_Variable)

@given(instance=UML2_Operation_strategy)
@settings(max_examples=50)
def test_uml2_operation_instantiation(instance):
    assert isinstance(instance, UML2_Operation)

@given(instance=UML2_Parameter_strategy)
@settings(max_examples=50)
def test_uml2_parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)



@given(instance=UML2_Parameter_strategy)
def test_uml2_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2_OutputPin_strategy)
@settings(max_examples=50)
def test_uml2_outputpin_instantiation(instance):
    assert isinstance(instance, UML2_OutputPin)

@given(instance=UML2_InputPin_strategy)
@settings(max_examples=50)
def test_uml2_inputpin_instantiation(instance):
    assert isinstance(instance, UML2_InputPin)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)
