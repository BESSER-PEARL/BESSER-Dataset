import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    classes::Visitable,
    CallExp,
    classes::OperationCallExp,
    classes::PropertyCallExp,
    Namespace,
    NamedElement,
    classes::Argument,
    classes::Parameter,
    classes::Package,
    TypedElement,
    classes::Operation,
    classes::Property,
    classes::CallExp,
    classes::Class,
    Element,
    classes::TypedElement,
    classes::Namespace,
    classes::Root,
    classes::NamedElement,
    Visitable,
    classes::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_classes::visitable_is_not_abstract():
    assert not inspect.isabstract(classes::Visitable)


def test_classes::visitable_constructor_exists():
    assert callable(classes::Visitable.__init__)


def test_classes::visitable_constructor_args():
    sig = inspect.signature(classes::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_classes::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(classes::OperationCallExp)


def test_classes::operationcallexp_constructor_exists():
    assert callable(classes::OperationCallExp.__init__)


def test_classes::operationcallexp_constructor_args():
    sig = inspect.signature(classes::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_classes::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(classes::PropertyCallExp)


def test_classes::propertycallexp_constructor_exists():
    assert callable(classes::PropertyCallExp.__init__)


def test_classes::propertycallexp_constructor_args():
    sig = inspect.signature(classes::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::argument_is_not_abstract():
    assert not inspect.isabstract(classes::Argument)


def test_classes::argument_constructor_exists():
    assert callable(classes::Argument.__init__)


def test_classes::argument_constructor_args():
    sig = inspect.signature(classes::Argument.__init__)
    params = list(sig.parameters.keys())



def test_classes::parameter_is_not_abstract():
    assert not inspect.isabstract(classes::Parameter)


def test_classes::parameter_constructor_exists():
    assert callable(classes::Parameter.__init__)


def test_classes::parameter_constructor_args():
    sig = inspect.signature(classes::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_classes::package_is_not_abstract():
    assert not inspect.isabstract(classes::Package)


def test_classes::package_constructor_exists():
    assert callable(classes::Package.__init__)


def test_classes::package_constructor_args():
    sig = inspect.signature(classes::Package.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::operation_is_not_abstract():
    assert not inspect.isabstract(classes::Operation)


def test_classes::operation_constructor_exists():
    assert callable(classes::Operation.__init__)


def test_classes::operation_constructor_args():
    sig = inspect.signature(classes::Operation.__init__)
    params = list(sig.parameters.keys())



def test_classes::property_is_not_abstract():
    assert not inspect.isabstract(classes::Property)


def test_classes::property_constructor_exists():
    assert callable(classes::Property.__init__)


def test_classes::property_constructor_args():
    sig = inspect.signature(classes::Property.__init__)
    params = list(sig.parameters.keys())



def test_classes::callexp_is_not_abstract():
    assert not inspect.isabstract(classes::CallExp)


def test_classes::callexp_constructor_exists():
    assert callable(classes::CallExp.__init__)


def test_classes::callexp_constructor_args():
    sig = inspect.signature(classes::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_classes::class_is_not_abstract():
    assert not inspect.isabstract(classes::Class)


def test_classes::class_constructor_exists():
    assert callable(classes::Class.__init__)


def test_classes::class_constructor_args():
    sig = inspect.signature(classes::Class.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_classes::typedelement_is_not_abstract():
    assert not inspect.isabstract(classes::TypedElement)


def test_classes::typedelement_constructor_exists():
    assert callable(classes::TypedElement.__init__)


def test_classes::typedelement_constructor_args():
    sig = inspect.signature(classes::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_classes::namespace_is_not_abstract():
    assert not inspect.isabstract(classes::Namespace)


def test_classes::namespace_constructor_exists():
    assert callable(classes::Namespace.__init__)


def test_classes::namespace_constructor_args():
    sig = inspect.signature(classes::Namespace.__init__)
    params = list(sig.parameters.keys())



def test_classes::root_is_not_abstract():
    assert not inspect.isabstract(classes::Root)


def test_classes::root_constructor_exists():
    assert callable(classes::Root.__init__)


def test_classes::root_constructor_args():
    sig = inspect.signature(classes::Root.__init__)
    params = list(sig.parameters.keys())



def test_classes::namedelement_is_not_abstract():
    assert not inspect.isabstract(classes::NamedElement)


def test_classes::namedelement_constructor_exists():
    assert callable(classes::NamedElement.__init__)


def test_classes::namedelement_constructor_args():
    sig = inspect.signature(classes::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_classes::namedelement_has_name():
    assert hasattr(classes::NamedElement, "name")
    descriptor = None
    for klass in classes::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_visitable_is_not_abstract():
    assert not inspect.isabstract(Visitable)


def test_visitable_constructor_exists():
    assert callable(Visitable.__init__)


def test_visitable_constructor_args():
    sig = inspect.signature(Visitable.__init__)
    params = list(sig.parameters.keys())



def test_classes::element_is_not_abstract():
    assert not inspect.isabstract(classes::Element)


def test_classes::element_constructor_exists():
    assert callable(classes::Element.__init__)


def test_classes::element_constructor_args():
    sig = inspect.signature(classes::Element.__init__)
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
classes::Visitable_strategy = st.builds(
    classes::Visitable,
)
CallExp_strategy = st.builds(
    CallExp,
)
classes::OperationCallExp_strategy = st.builds(
    classes::OperationCallExp,
)
classes::PropertyCallExp_strategy = st.builds(
    classes::PropertyCallExp,
)
Namespace_strategy = st.builds(
    Namespace,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
classes::Argument_strategy = st.builds(
    classes::Argument,
)
classes::Parameter_strategy = st.builds(
    classes::Parameter,
)
classes::Package_strategy = st.builds(
    classes::Package,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
classes::Operation_strategy = st.builds(
    classes::Operation,
)
classes::Property_strategy = st.builds(
    classes::Property,
)
classes::CallExp_strategy = st.builds(
    classes::CallExp,
)
classes::Class_strategy = st.builds(
    classes::Class,
)
Element_strategy = st.builds(
    Element,
)
classes::TypedElement_strategy = st.builds(
    classes::TypedElement,
)
classes::Namespace_strategy = st.builds(
    classes::Namespace,
)
classes::Root_strategy = st.builds(
    classes::Root,
)
classes::NamedElement_strategy = st.builds(
    classes::NamedElement,
    name=
        safe_text
)
Visitable_strategy = st.builds(
    Visitable,
)
classes::Element_strategy = st.builds(
    classes::Element,
)

@given(instance=classes::Visitable_strategy)
@settings(max_examples=50)
def test_classes::visitable_instantiation(instance):
    assert isinstance(instance, classes::Visitable)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=classes::OperationCallExp_strategy)
@settings(max_examples=50)
def test_classes::operationcallexp_instantiation(instance):
    assert isinstance(instance, classes::OperationCallExp)

@given(instance=classes::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_classes::propertycallexp_instantiation(instance):
    assert isinstance(instance, classes::PropertyCallExp)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=classes::Argument_strategy)
@settings(max_examples=50)
def test_classes::argument_instantiation(instance):
    assert isinstance(instance, classes::Argument)

@given(instance=classes::Parameter_strategy)
@settings(max_examples=50)
def test_classes::parameter_instantiation(instance):
    assert isinstance(instance, classes::Parameter)

@given(instance=classes::Package_strategy)
@settings(max_examples=50)
def test_classes::package_instantiation(instance):
    assert isinstance(instance, classes::Package)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=classes::Operation_strategy)
@settings(max_examples=50)
def test_classes::operation_instantiation(instance):
    assert isinstance(instance, classes::Operation)

@given(instance=classes::Property_strategy)
@settings(max_examples=50)
def test_classes::property_instantiation(instance):
    assert isinstance(instance, classes::Property)

@given(instance=classes::CallExp_strategy)
@settings(max_examples=50)
def test_classes::callexp_instantiation(instance):
    assert isinstance(instance, classes::CallExp)

@given(instance=classes::Class_strategy)
@settings(max_examples=50)
def test_classes::class_instantiation(instance):
    assert isinstance(instance, classes::Class)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=classes::TypedElement_strategy)
@settings(max_examples=50)
def test_classes::typedelement_instantiation(instance):
    assert isinstance(instance, classes::TypedElement)

@given(instance=classes::Namespace_strategy)
@settings(max_examples=50)
def test_classes::namespace_instantiation(instance):
    assert isinstance(instance, classes::Namespace)

@given(instance=classes::Root_strategy)
@settings(max_examples=50)
def test_classes::root_instantiation(instance):
    assert isinstance(instance, classes::Root)

@given(instance=classes::NamedElement_strategy)
@settings(max_examples=50)
def test_classes::namedelement_instantiation(instance):
    assert isinstance(instance, classes::NamedElement)

@given(instance=classes::NamedElement_strategy)
def test_classes::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=classes::NamedElement_strategy)
def test_classes::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Visitable_strategy)
@settings(max_examples=50)
def test_visitable_instantiation(instance):
    assert isinstance(instance, Visitable)

@given(instance=classes::Element_strategy)
@settings(max_examples=50)
def test_classes::element_instantiation(instance):
    assert isinstance(instance, classes::Element)
