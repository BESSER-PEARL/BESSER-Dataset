import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dcmddandroid_EVisibility,
    Association,
    dcmddandroid_Composition,
    dcmddandroid_Agregation,
    ClassElement,
    NamedElement,
    dcmddandroid_ModelElement,
    dcmddandroid_Parameter,
    dcmddandroid_EnumValue,
    dcmddandroid_Diagram,
    AbstractClass,
    dcmddandroid_CycleClass,
    dcmddandroid_Class,
    dcmddandroid_Method,
    dcmddandroid_Attribute,
    dcmddandroid_PersistentClass,
    EVisibility,
    dcmddandroid_ClassElement,
    ModelElement,
    dcmddandroid_Interface,
    dcmddandroid_Association,
    dcmddandroid_Implements,
    dcmddandroid_Enum,
    dcmddandroid_AbstractClass,
    dcmddandroid_NamedElement,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dcmddandroid_evisibility_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_EVisibility)


def test_dcmddandroid_evisibility_constructor_exists():
    assert callable(dcmddandroid_EVisibility.__init__)


def test_dcmddandroid_evisibility_constructor_args():
    sig = inspect.signature(dcmddandroid_EVisibility.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_dcmddandroid_evisibility_has_visibility():
    assert hasattr(dcmddandroid_EVisibility, "visibility")
    descriptor = None
    for klass in dcmddandroid_EVisibility.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_composition_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Composition)


def test_dcmddandroid_composition_constructor_exists():
    assert callable(dcmddandroid_Composition.__init__)


def test_dcmddandroid_composition_constructor_args():
    sig = inspect.signature(dcmddandroid_Composition.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_agregation_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Agregation)


def test_dcmddandroid_agregation_constructor_exists():
    assert callable(dcmddandroid_Agregation.__init__)


def test_dcmddandroid_agregation_constructor_args():
    sig = inspect.signature(dcmddandroid_Agregation.__init__)
    params = list(sig.parameters.keys())



def test_classelement_is_not_abstract():
    assert not inspect.isabstract(ClassElement)


def test_classelement_constructor_exists():
    assert callable(ClassElement.__init__)


def test_classelement_constructor_args():
    sig = inspect.signature(ClassElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_modelelement_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_ModelElement)


def test_dcmddandroid_modelelement_constructor_exists():
    assert callable(dcmddandroid_ModelElement.__init__)


def test_dcmddandroid_modelelement_constructor_args():
    sig = inspect.signature(dcmddandroid_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_parameter_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Parameter)


def test_dcmddandroid_parameter_constructor_exists():
    assert callable(dcmddandroid_Parameter.__init__)


def test_dcmddandroid_parameter_constructor_args():
    sig = inspect.signature(dcmddandroid_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dcmddandroid_parameter_has_type():
    assert hasattr(dcmddandroid_Parameter, "type")
    descriptor = None
    for klass in dcmddandroid_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_enumvalue_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_EnumValue)


def test_dcmddandroid_enumvalue_constructor_exists():
    assert callable(dcmddandroid_EnumValue.__init__)


def test_dcmddandroid_enumvalue_constructor_args():
    sig = inspect.signature(dcmddandroid_EnumValue.__init__)
    params = list(sig.parameters.keys())
    assert "intValue" in params, "Missing parameter 'intValue'"

def test_dcmddandroid_enumvalue_has_intValue():
    assert hasattr(dcmddandroid_EnumValue, "intValue")
    descriptor = None
    for klass in dcmddandroid_EnumValue.__mro__:
        if "intValue" in klass.__dict__:
            descriptor = klass.__dict__["intValue"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_diagram_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Diagram)


def test_dcmddandroid_diagram_constructor_exists():
    assert callable(dcmddandroid_Diagram.__init__)


def test_dcmddandroid_diagram_constructor_args():
    sig = inspect.signature(dcmddandroid_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_abstractclass_is_not_abstract():
    assert not inspect.isabstract(AbstractClass)


def test_abstractclass_constructor_exists():
    assert callable(AbstractClass.__init__)


def test_abstractclass_constructor_args():
    sig = inspect.signature(AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_cycleclass_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_CycleClass)


def test_dcmddandroid_cycleclass_constructor_exists():
    assert callable(dcmddandroid_CycleClass.__init__)


def test_dcmddandroid_cycleclass_constructor_args():
    sig = inspect.signature(dcmddandroid_CycleClass.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_class_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Class)


def test_dcmddandroid_class_constructor_exists():
    assert callable(dcmddandroid_Class.__init__)


def test_dcmddandroid_class_constructor_args():
    sig = inspect.signature(dcmddandroid_Class.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_method_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Method)


def test_dcmddandroid_method_constructor_exists():
    assert callable(dcmddandroid_Method.__init__)


def test_dcmddandroid_method_constructor_args():
    sig = inspect.signature(dcmddandroid_Method.__init__)
    params = list(sig.parameters.keys())
    assert "returns" in params, "Missing parameter 'returns'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_dcmddandroid_method_has_returns():
    assert hasattr(dcmddandroid_Method, "returns")
    descriptor = None
    for klass in dcmddandroid_Method.__mro__:
        if "returns" in klass.__dict__:
            descriptor = klass.__dict__["returns"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_method_has_isAbstract():
    assert hasattr(dcmddandroid_Method, "isAbstract")
    descriptor = None
    for klass in dcmddandroid_Method.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_attribute_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Attribute)


def test_dcmddandroid_attribute_constructor_exists():
    assert callable(dcmddandroid_Attribute.__init__)


def test_dcmddandroid_attribute_constructor_args():
    sig = inspect.signature(dcmddandroid_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "secured" in params, "Missing parameter 'secured'"

def test_dcmddandroid_attribute_has_type():
    assert hasattr(dcmddandroid_Attribute, "type")
    descriptor = None
    for klass in dcmddandroid_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_attribute_has_defaultValue():
    assert hasattr(dcmddandroid_Attribute, "defaultValue")
    descriptor = None
    for klass in dcmddandroid_Attribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_attribute_has_secured():
    assert hasattr(dcmddandroid_Attribute, "secured")
    descriptor = None
    for klass in dcmddandroid_Attribute.__mro__:
        if "secured" in klass.__dict__:
            descriptor = klass.__dict__["secured"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_persistentclass_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_PersistentClass)


def test_dcmddandroid_persistentclass_constructor_exists():
    assert callable(dcmddandroid_PersistentClass.__init__)


def test_dcmddandroid_persistentclass_constructor_args():
    sig = inspect.signature(dcmddandroid_PersistentClass.__init__)
    params = list(sig.parameters.keys())



def test_evisibility_is_not_abstract():
    assert not inspect.isabstract(EVisibility)


def test_evisibility_constructor_exists():
    assert callable(EVisibility.__init__)


def test_evisibility_constructor_args():
    sig = inspect.signature(EVisibility.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_classelement_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_ClassElement)


def test_dcmddandroid_classelement_constructor_exists():
    assert callable(dcmddandroid_ClassElement.__init__)


def test_dcmddandroid_classelement_constructor_args():
    sig = inspect.signature(dcmddandroid_ClassElement.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"

def test_dcmddandroid_classelement_has_static():
    assert hasattr(dcmddandroid_ClassElement, "static")
    descriptor = None
    for klass in dcmddandroid_ClassElement.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_classelement_has_final():
    assert hasattr(dcmddandroid_ClassElement, "final")
    descriptor = None
    for klass in dcmddandroid_ClassElement.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_interface_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Interface)


def test_dcmddandroid_interface_constructor_exists():
    assert callable(dcmddandroid_Interface.__init__)


def test_dcmddandroid_interface_constructor_args():
    sig = inspect.signature(dcmddandroid_Interface.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_association_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Association)


def test_dcmddandroid_association_constructor_exists():
    assert callable(dcmddandroid_Association.__init__)


def test_dcmddandroid_association_constructor_args():
    sig = inspect.signature(dcmddandroid_Association.__init__)
    params = list(sig.parameters.keys())
    assert "rolSource" in params, "Missing parameter 'rolSource'"
    assert "minMultiplicitySource" in params, "Missing parameter 'minMultiplicitySource'"
    assert "maxMultiplicityTarget" in params, "Missing parameter 'maxMultiplicityTarget'"
    assert "maxMultiplicitySource" in params, "Missing parameter 'maxMultiplicitySource'"
    assert "rolTarget" in params, "Missing parameter 'rolTarget'"
    assert "minMultiplicityTarget" in params, "Missing parameter 'minMultiplicityTarget'"

def test_dcmddandroid_association_has_rolSource():
    assert hasattr(dcmddandroid_Association, "rolSource")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "rolSource" in klass.__dict__:
            descriptor = klass.__dict__["rolSource"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_association_has_minMultiplicitySource():
    assert hasattr(dcmddandroid_Association, "minMultiplicitySource")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "minMultiplicitySource" in klass.__dict__:
            descriptor = klass.__dict__["minMultiplicitySource"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_association_has_maxMultiplicityTarget():
    assert hasattr(dcmddandroid_Association, "maxMultiplicityTarget")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "maxMultiplicityTarget" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicityTarget"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_association_has_maxMultiplicitySource():
    assert hasattr(dcmddandroid_Association, "maxMultiplicitySource")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "maxMultiplicitySource" in klass.__dict__:
            descriptor = klass.__dict__["maxMultiplicitySource"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_association_has_rolTarget():
    assert hasattr(dcmddandroid_Association, "rolTarget")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "rolTarget" in klass.__dict__:
            descriptor = klass.__dict__["rolTarget"]
            break
    assert isinstance(descriptor, property)

def test_dcmddandroid_association_has_minMultiplicityTarget():
    assert hasattr(dcmddandroid_Association, "minMultiplicityTarget")
    descriptor = None
    for klass in dcmddandroid_Association.__mro__:
        if "minMultiplicityTarget" in klass.__dict__:
            descriptor = klass.__dict__["minMultiplicityTarget"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_implements_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Implements)


def test_dcmddandroid_implements_constructor_exists():
    assert callable(dcmddandroid_Implements.__init__)


def test_dcmddandroid_implements_constructor_args():
    sig = inspect.signature(dcmddandroid_Implements.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_enum_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_Enum)


def test_dcmddandroid_enum_constructor_exists():
    assert callable(dcmddandroid_Enum.__init__)


def test_dcmddandroid_enum_constructor_args():
    sig = inspect.signature(dcmddandroid_Enum.__init__)
    params = list(sig.parameters.keys())



def test_dcmddandroid_abstractclass_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_AbstractClass)


def test_dcmddandroid_abstractclass_constructor_exists():
    assert callable(dcmddandroid_AbstractClass.__init__)


def test_dcmddandroid_abstractclass_constructor_args():
    sig = inspect.signature(dcmddandroid_AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_dcmddandroid_abstractclass_has_isAbstract():
    assert hasattr(dcmddandroid_AbstractClass, "isAbstract")
    descriptor = None
    for klass in dcmddandroid_AbstractClass.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_dcmddandroid_namedelement_is_not_abstract():
    assert not inspect.isabstract(dcmddandroid_NamedElement)


def test_dcmddandroid_namedelement_constructor_exists():
    assert callable(dcmddandroid_NamedElement.__init__)


def test_dcmddandroid_namedelement_constructor_args():
    sig = inspect.signature(dcmddandroid_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dcmddandroid_namedelement_has_name():
    assert hasattr(dcmddandroid_NamedElement, "name")
    descriptor = None
    for klass in dcmddandroid_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "protected",
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
dcmddandroid_EVisibility_strategy = st.builds(
    dcmddandroid_EVisibility,
    visibility=
        safe_text
)
Association_strategy = st.builds(
    Association,
)
dcmddandroid_Composition_strategy = st.builds(
    dcmddandroid_Composition,
)
dcmddandroid_Agregation_strategy = st.builds(
    dcmddandroid_Agregation,
)
ClassElement_strategy = st.builds(
    ClassElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
dcmddandroid_ModelElement_strategy = st.builds(
    dcmddandroid_ModelElement,
)
dcmddandroid_Parameter_strategy = st.builds(
    dcmddandroid_Parameter,
    type=
        safe_text
)
dcmddandroid_EnumValue_strategy = st.builds(
    dcmddandroid_EnumValue,
    intValue=
        st.integers()
)
dcmddandroid_Diagram_strategy = st.builds(
    dcmddandroid_Diagram,
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
dcmddandroid_CycleClass_strategy = st.builds(
    dcmddandroid_CycleClass,
)
dcmddandroid_Class_strategy = st.builds(
    dcmddandroid_Class,
)
dcmddandroid_Method_strategy = st.builds(
    dcmddandroid_Method,
    returns=
        safe_text,
    isAbstract=
        st.booleans()
)
dcmddandroid_Attribute_strategy = st.builds(
    dcmddandroid_Attribute,
    type=
        safe_text,
    defaultValue=
        safe_text,
    secured=
        safe_text
)
dcmddandroid_PersistentClass_strategy = st.builds(
    dcmddandroid_PersistentClass,
)
EVisibility_strategy = st.builds(
    EVisibility,
)
dcmddandroid_ClassElement_strategy = st.builds(
    dcmddandroid_ClassElement,
    static=
        st.booleans(),
    final=
        st.booleans()
)
ModelElement_strategy = st.builds(
    ModelElement,
)
dcmddandroid_Interface_strategy = st.builds(
    dcmddandroid_Interface,
)
dcmddandroid_Association_strategy = st.builds(
    dcmddandroid_Association,
    rolSource=
        safe_text,
    minMultiplicitySource=
        st.integers(),
    maxMultiplicityTarget=
        st.integers(),
    maxMultiplicitySource=
        st.integers(),
    rolTarget=
        safe_text,
    minMultiplicityTarget=
        st.integers()
)
dcmddandroid_Implements_strategy = st.builds(
    dcmddandroid_Implements,
)
dcmddandroid_Enum_strategy = st.builds(
    dcmddandroid_Enum,
)
dcmddandroid_AbstractClass_strategy = st.builds(
    dcmddandroid_AbstractClass,
    isAbstract=
        st.booleans()
)
dcmddandroid_NamedElement_strategy = st.builds(
    dcmddandroid_NamedElement,
    name=
        safe_text
)

@given(instance=dcmddandroid_EVisibility_strategy)
@settings(max_examples=50)
def test_dcmddandroid_evisibility_instantiation(instance):
    assert isinstance(instance, dcmddandroid_EVisibility)



@given(instance=dcmddandroid_EVisibility_strategy)
def test_dcmddandroid_evisibility_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=dcmddandroid_Composition_strategy)
@settings(max_examples=50)
def test_dcmddandroid_composition_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Composition)

@given(instance=dcmddandroid_Agregation_strategy)
@settings(max_examples=50)
def test_dcmddandroid_agregation_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Agregation)

@given(instance=ClassElement_strategy)
@settings(max_examples=50)
def test_classelement_instantiation(instance):
    assert isinstance(instance, ClassElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=dcmddandroid_ModelElement_strategy)
@settings(max_examples=50)
def test_dcmddandroid_modelelement_instantiation(instance):
    assert isinstance(instance, dcmddandroid_ModelElement)

@given(instance=dcmddandroid_Parameter_strategy)
@settings(max_examples=50)
def test_dcmddandroid_parameter_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Parameter)



@given(instance=dcmddandroid_Parameter_strategy)
def test_dcmddandroid_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dcmddandroid_EnumValue_strategy)
@settings(max_examples=50)
def test_dcmddandroid_enumvalue_instantiation(instance):
    assert isinstance(instance, dcmddandroid_EnumValue)



@given(instance=dcmddandroid_EnumValue_strategy)
def test_dcmddandroid_enumvalue_intValue_setter(instance):
    original = instance.intValue
    instance.intValue = original
    assert instance.intValue == original

@given(instance=dcmddandroid_Diagram_strategy)
@settings(max_examples=50)
def test_dcmddandroid_diagram_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Diagram)

@given(instance=AbstractClass_strategy)
@settings(max_examples=50)
def test_abstractclass_instantiation(instance):
    assert isinstance(instance, AbstractClass)

@given(instance=dcmddandroid_CycleClass_strategy)
@settings(max_examples=50)
def test_dcmddandroid_cycleclass_instantiation(instance):
    assert isinstance(instance, dcmddandroid_CycleClass)

@given(instance=dcmddandroid_Class_strategy)
@settings(max_examples=50)
def test_dcmddandroid_class_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Class)

@given(instance=dcmddandroid_Method_strategy)
@settings(max_examples=50)
def test_dcmddandroid_method_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Method)



@given(instance=dcmddandroid_Method_strategy)
def test_dcmddandroid_method_returns_setter(instance):
    original = instance.returns
    instance.returns = original
    assert instance.returns == original



@given(instance=dcmddandroid_Method_strategy)
def test_dcmddandroid_method_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=dcmddandroid_Attribute_strategy)
@settings(max_examples=50)
def test_dcmddandroid_attribute_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Attribute)



@given(instance=dcmddandroid_Attribute_strategy)
def test_dcmddandroid_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=dcmddandroid_Attribute_strategy)
def test_dcmddandroid_attribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=dcmddandroid_Attribute_strategy)
def test_dcmddandroid_attribute_secured_setter(instance):
    original = instance.secured
    instance.secured = original
    assert instance.secured == original

@given(instance=dcmddandroid_PersistentClass_strategy)
@settings(max_examples=50)
def test_dcmddandroid_persistentclass_instantiation(instance):
    assert isinstance(instance, dcmddandroid_PersistentClass)

@given(instance=EVisibility_strategy)
@settings(max_examples=50)
def test_evisibility_instantiation(instance):
    assert isinstance(instance, EVisibility)

@given(instance=dcmddandroid_ClassElement_strategy)
@settings(max_examples=50)
def test_dcmddandroid_classelement_instantiation(instance):
    assert isinstance(instance, dcmddandroid_ClassElement)



@given(instance=dcmddandroid_ClassElement_strategy)
def test_dcmddandroid_classelement_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=dcmddandroid_ClassElement_strategy)
def test_dcmddandroid_classelement_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=dcmddandroid_Interface_strategy)
@settings(max_examples=50)
def test_dcmddandroid_interface_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Interface)

@given(instance=dcmddandroid_Association_strategy)
@settings(max_examples=50)
def test_dcmddandroid_association_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Association)



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_rolSource_setter(instance):
    original = instance.rolSource
    instance.rolSource = original
    assert instance.rolSource == original



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_minMultiplicitySource_setter(instance):
    original = instance.minMultiplicitySource
    instance.minMultiplicitySource = original
    assert instance.minMultiplicitySource == original



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_maxMultiplicityTarget_setter(instance):
    original = instance.maxMultiplicityTarget
    instance.maxMultiplicityTarget = original
    assert instance.maxMultiplicityTarget == original



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_maxMultiplicitySource_setter(instance):
    original = instance.maxMultiplicitySource
    instance.maxMultiplicitySource = original
    assert instance.maxMultiplicitySource == original



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_rolTarget_setter(instance):
    original = instance.rolTarget
    instance.rolTarget = original
    assert instance.rolTarget == original



@given(instance=dcmddandroid_Association_strategy)
def test_dcmddandroid_association_minMultiplicityTarget_setter(instance):
    original = instance.minMultiplicityTarget
    instance.minMultiplicityTarget = original
    assert instance.minMultiplicityTarget == original

@given(instance=dcmddandroid_Implements_strategy)
@settings(max_examples=50)
def test_dcmddandroid_implements_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Implements)

@given(instance=dcmddandroid_Enum_strategy)
@settings(max_examples=50)
def test_dcmddandroid_enum_instantiation(instance):
    assert isinstance(instance, dcmddandroid_Enum)

@given(instance=dcmddandroid_AbstractClass_strategy)
@settings(max_examples=50)
def test_dcmddandroid_abstractclass_instantiation(instance):
    assert isinstance(instance, dcmddandroid_AbstractClass)



@given(instance=dcmddandroid_AbstractClass_strategy)
def test_dcmddandroid_abstractclass_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=dcmddandroid_NamedElement_strategy)
@settings(max_examples=50)
def test_dcmddandroid_namedelement_instantiation(instance):
    assert isinstance(instance, dcmddandroid_NamedElement)



@given(instance=dcmddandroid_NamedElement_strategy)
def test_dcmddandroid_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
