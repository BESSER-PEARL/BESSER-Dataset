import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    types::AnnotatableElement,
    types::MetaComposite,
    types::EObject,
    TypeSpecifier,
    types::ArrayTypeSpecifier,
    types::Annotation,
    types::Domain,
    ComplexType,
    types::EnumerationType,
    Type,
    types::TypeParameter,
    types::AnnotationType,
    types::PrimitiveType,
    GenericElement,
    types::ComplexType,
    TypedDeclaration,
    types::Event,
    types::TypeAlias,
    types::Enumerator,
    types::Operation,
    MetaComposite,
    AnnotatableElement,
    NamedElement,
    types::GenericElement,
    types::TypeSpecifier,
    types::TypedElement,
    TypedElement,
    types::Expression,
    types::Property,
    types::Parameter,
    types::Declaration,
    DomainElement,
    Declaration,
    types::Type,
    types::Package,
    types::TypedDeclaration,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types::annotatableelement_is_not_abstract():
    assert not inspect.isabstract(types::AnnotatableElement)


def test_types::annotatableelement_constructor_exists():
    assert callable(types::AnnotatableElement.__init__)


def test_types::annotatableelement_constructor_args():
    sig = inspect.signature(types::AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_types::metacomposite_is_not_abstract():
    assert not inspect.isabstract(types::MetaComposite)


def test_types::metacomposite_constructor_exists():
    assert callable(types::MetaComposite.__init__)


def test_types::metacomposite_constructor_args():
    sig = inspect.signature(types::MetaComposite.__init__)
    params = list(sig.parameters.keys())



def test_types::eobject_is_not_abstract():
    assert not inspect.isabstract(types::EObject)


def test_types::eobject_constructor_exists():
    assert callable(types::EObject.__init__)


def test_types::eobject_constructor_args():
    sig = inspect.signature(types::EObject.__init__)
    params = list(sig.parameters.keys())



def test_typespecifier_is_not_abstract():
    assert not inspect.isabstract(TypeSpecifier)


def test_typespecifier_constructor_exists():
    assert callable(TypeSpecifier.__init__)


def test_typespecifier_constructor_args():
    sig = inspect.signature(TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_types::arraytypespecifier_is_not_abstract():
    assert not inspect.isabstract(types::ArrayTypeSpecifier)


def test_types::arraytypespecifier_constructor_exists():
    assert callable(types::ArrayTypeSpecifier.__init__)


def test_types::arraytypespecifier_constructor_args():
    sig = inspect.signature(types::ArrayTypeSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types::arraytypespecifier_has_size():
    assert hasattr(types::ArrayTypeSpecifier, "size")
    descriptor = None
    for klass in types::ArrayTypeSpecifier.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types::annotation_is_not_abstract():
    assert not inspect.isabstract(types::Annotation)


def test_types::annotation_constructor_exists():
    assert callable(types::Annotation.__init__)


def test_types::annotation_constructor_args():
    sig = inspect.signature(types::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_types::domain_is_not_abstract():
    assert not inspect.isabstract(types::Domain)


def test_types::domain_constructor_exists():
    assert callable(types::Domain.__init__)


def test_types::domain_constructor_args():
    sig = inspect.signature(types::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "domainID" in params, "Missing parameter 'domainID'"

def test_types::domain_has_domainID():
    assert hasattr(types::Domain, "domainID")
    descriptor = None
    for klass in types::Domain.__mro__:
        if "domainID" in klass.__dict__:
            descriptor = klass.__dict__["domainID"]
            break
    assert isinstance(descriptor, property)



def test_complextype_is_not_abstract():
    assert not inspect.isabstract(ComplexType)


def test_complextype_constructor_exists():
    assert callable(ComplexType.__init__)


def test_complextype_constructor_args():
    sig = inspect.signature(ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_types::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumerationType)


def test_types::enumerationtype_constructor_exists():
    assert callable(types::EnumerationType.__init__)


def test_types::enumerationtype_constructor_args():
    sig = inspect.signature(types::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types::typeparameter_is_not_abstract():
    assert not inspect.isabstract(types::TypeParameter)


def test_types::typeparameter_constructor_exists():
    assert callable(types::TypeParameter.__init__)


def test_types::typeparameter_constructor_args():
    sig = inspect.signature(types::TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_types::annotationtype_is_not_abstract():
    assert not inspect.isabstract(types::AnnotationType)


def test_types::annotationtype_constructor_exists():
    assert callable(types::AnnotationType.__init__)


def test_types::annotationtype_constructor_args():
    sig = inspect.signature(types::AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_genericelement_is_not_abstract():
    assert not inspect.isabstract(GenericElement)


def test_genericelement_constructor_exists():
    assert callable(GenericElement.__init__)


def test_genericelement_constructor_args():
    sig = inspect.signature(GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_types::complextype_is_not_abstract():
    assert not inspect.isabstract(types::ComplexType)


def test_types::complextype_constructor_exists():
    assert callable(types::ComplexType.__init__)


def test_types::complextype_constructor_args():
    sig = inspect.signature(types::ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_types::event_is_not_abstract():
    assert not inspect.isabstract(types::Event)


def test_types::event_constructor_exists():
    assert callable(types::Event.__init__)


def test_types::event_constructor_args():
    sig = inspect.signature(types::Event.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_types::event_has_direction():
    assert hasattr(types::Event, "direction")
    descriptor = None
    for klass in types::Event.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_types::typealias_is_not_abstract():
    assert not inspect.isabstract(types::TypeAlias)


def test_types::typealias_constructor_exists():
    assert callable(types::TypeAlias.__init__)


def test_types::typealias_constructor_args():
    sig = inspect.signature(types::TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_types::enumerator_is_not_abstract():
    assert not inspect.isabstract(types::Enumerator)


def test_types::enumerator_constructor_exists():
    assert callable(types::Enumerator.__init__)


def test_types::enumerator_constructor_args():
    sig = inspect.signature(types::Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_types::enumerator_has_literalValue():
    assert hasattr(types::Enumerator, "literalValue")
    descriptor = None
    for klass in types::Enumerator.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_types::operation_is_not_abstract():
    assert not inspect.isabstract(types::Operation)


def test_types::operation_constructor_exists():
    assert callable(types::Operation.__init__)


def test_types::operation_constructor_args():
    sig = inspect.signature(types::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "variadic" in params, "Missing parameter 'variadic'"

def test_types::operation_has_variadic():
    assert hasattr(types::Operation, "variadic")
    descriptor = None
    for klass in types::Operation.__mro__:
        if "variadic" in klass.__dict__:
            descriptor = klass.__dict__["variadic"]
            break
    assert isinstance(descriptor, property)



def test_metacomposite_is_not_abstract():
    assert not inspect.isabstract(MetaComposite)


def test_metacomposite_constructor_exists():
    assert callable(MetaComposite.__init__)


def test_metacomposite_constructor_args():
    sig = inspect.signature(MetaComposite.__init__)
    params = list(sig.parameters.keys())



def test_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(AnnotatableElement)


def test_annotatableelement_constructor_exists():
    assert callable(AnnotatableElement.__init__)


def test_annotatableelement_constructor_args():
    sig = inspect.signature(AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::genericelement_is_not_abstract():
    assert not inspect.isabstract(types::GenericElement)


def test_types::genericelement_constructor_exists():
    assert callable(types::GenericElement.__init__)


def test_types::genericelement_constructor_args():
    sig = inspect.signature(types::GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_types::typespecifier_is_not_abstract():
    assert not inspect.isabstract(types::TypeSpecifier)


def test_types::typespecifier_constructor_exists():
    assert callable(types::TypeSpecifier.__init__)


def test_types::typespecifier_constructor_args():
    sig = inspect.signature(types::TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_types::typedelement_is_not_abstract():
    assert not inspect.isabstract(types::TypedElement)


def test_types::typedelement_constructor_exists():
    assert callable(types::TypedElement.__init__)


def test_types::typedelement_constructor_args():
    sig = inspect.signature(types::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::expression_is_not_abstract():
    assert not inspect.isabstract(types::Expression)


def test_types::expression_constructor_exists():
    assert callable(types::Expression.__init__)


def test_types::expression_constructor_args():
    sig = inspect.signature(types::Expression.__init__)
    params = list(sig.parameters.keys())



def test_types::property_is_not_abstract():
    assert not inspect.isabstract(types::Property)


def test_types::property_constructor_exists():
    assert callable(types::Property.__init__)


def test_types::property_constructor_args():
    sig = inspect.signature(types::Property.__init__)
    params = list(sig.parameters.keys())
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "const" in params, "Missing parameter 'const'"

def test_types::property_has_readonly():
    assert hasattr(types::Property, "readonly")
    descriptor = None
    for klass in types::Property.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_types::property_has_const():
    assert hasattr(types::Property, "const")
    descriptor = None
    for klass in types::Property.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_types::parameter_is_not_abstract():
    assert not inspect.isabstract(types::Parameter)


def test_types::parameter_constructor_exists():
    assert callable(types::Parameter.__init__)


def test_types::parameter_constructor_args():
    sig = inspect.signature(types::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_types::parameter_has_varArgs():
    assert hasattr(types::Parameter, "varArgs")
    descriptor = None
    for klass in types::Parameter.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_types::parameter_has_optional():
    assert hasattr(types::Parameter, "optional")
    descriptor = None
    for klass in types::Parameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_types::declaration_is_not_abstract():
    assert not inspect.isabstract(types::Declaration)


def test_types::declaration_constructor_exists():
    assert callable(types::Declaration.__init__)


def test_types::declaration_constructor_args():
    sig = inspect.signature(types::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "static" in params, "Missing parameter 'static'"

def test_types::declaration_has_id():
    assert hasattr(types::Declaration, "id")
    descriptor = None
    for klass in types::Declaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_types::declaration_has_static():
    assert hasattr(types::Declaration, "static")
    descriptor = None
    for klass in types::Declaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)



def test_domainelement_is_not_abstract():
    assert not inspect.isabstract(DomainElement)


def test_domainelement_constructor_exists():
    assert callable(DomainElement.__init__)


def test_domainelement_constructor_args():
    sig = inspect.signature(DomainElement.__init__)
    params = list(sig.parameters.keys())



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_types::type_is_not_abstract():
    assert not inspect.isabstract(types::Type)


def test_types::type_constructor_exists():
    assert callable(types::Type.__init__)


def test_types::type_constructor_args():
    sig = inspect.signature(types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_types::type_has_visible():
    assert hasattr(types::Type, "visible")
    descriptor = None
    for klass in types::Type.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_types::type_has_abstract():
    assert hasattr(types::Type, "abstract")
    descriptor = None
    for klass in types::Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_types::package_is_not_abstract():
    assert not inspect.isabstract(types::Package)


def test_types::package_constructor_exists():
    assert callable(types::Package.__init__)


def test_types::package_constructor_args():
    sig = inspect.signature(types::Package.__init__)
    params = list(sig.parameters.keys())



def test_types::typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(types::TypedDeclaration)


def test_types::typeddeclaration_constructor_exists():
    assert callable(types::TypedDeclaration.__init__)


def test_types::typeddeclaration_constructor_args():
    sig = inspect.signature(types::TypedDeclaration.__init__)
    params = list(sig.parameters.keys())

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "OUT",
        "IN",
        "LOCAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
types::AnnotatableElement_strategy = st.builds(
    types::AnnotatableElement,
)
types::MetaComposite_strategy = st.builds(
    types::MetaComposite,
)
types::EObject_strategy = st.builds(
    types::EObject,
)
TypeSpecifier_strategy = st.builds(
    TypeSpecifier,
)
types::ArrayTypeSpecifier_strategy = st.builds(
    types::ArrayTypeSpecifier,
    size=
        st.integers()
)
types::Annotation_strategy = st.builds(
    types::Annotation,
)
types::Domain_strategy = st.builds(
    types::Domain,
    domainID=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
types::EnumerationType_strategy = st.builds(
    types::EnumerationType,
)
Type_strategy = st.builds(
    Type,
)
types::TypeParameter_strategy = st.builds(
    types::TypeParameter,
)
types::AnnotationType_strategy = st.builds(
    types::AnnotationType,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
GenericElement_strategy = st.builds(
    GenericElement,
)
types::ComplexType_strategy = st.builds(
    types::ComplexType,
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
types::Event_strategy = st.builds(
    types::Event,
    direction=
        safe_text
)
types::TypeAlias_strategy = st.builds(
    types::TypeAlias,
)
types::Enumerator_strategy = st.builds(
    types::Enumerator,
    literalValue=
        st.integers()
)
types::Operation_strategy = st.builds(
    types::Operation,
    variadic=
        st.booleans()
)
MetaComposite_strategy = st.builds(
    MetaComposite,
)
AnnotatableElement_strategy = st.builds(
    AnnotatableElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
types::GenericElement_strategy = st.builds(
    types::GenericElement,
)
types::TypeSpecifier_strategy = st.builds(
    types::TypeSpecifier,
)
types::TypedElement_strategy = st.builds(
    types::TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
types::Expression_strategy = st.builds(
    types::Expression,
)
types::Property_strategy = st.builds(
    types::Property,
    readonly=
        st.booleans(),
    const=
        st.booleans()
)
types::Parameter_strategy = st.builds(
    types::Parameter,
    varArgs=
        st.booleans(),
    optional=
        st.booleans()
)
types::Declaration_strategy = st.builds(
    types::Declaration,
    id=
        safe_text,
    static=
        st.booleans()
)
DomainElement_strategy = st.builds(
    DomainElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
types::Type_strategy = st.builds(
    types::Type,
    visible=
        st.booleans(),
    abstract=
        st.booleans()
)
types::Package_strategy = st.builds(
    types::Package,
)
types::TypedDeclaration_strategy = st.builds(
    types::TypedDeclaration,
)

@given(instance=types::AnnotatableElement_strategy)
@settings(max_examples=50)
def test_types::annotatableelement_instantiation(instance):
    assert isinstance(instance, types::AnnotatableElement)

@given(instance=types::MetaComposite_strategy)
@settings(max_examples=50)
def test_types::metacomposite_instantiation(instance):
    assert isinstance(instance, types::MetaComposite)

@given(instance=types::EObject_strategy)
@settings(max_examples=50)
def test_types::eobject_instantiation(instance):
    assert isinstance(instance, types::EObject)

@given(instance=TypeSpecifier_strategy)
@settings(max_examples=50)
def test_typespecifier_instantiation(instance):
    assert isinstance(instance, TypeSpecifier)

@given(instance=types::ArrayTypeSpecifier_strategy)
@settings(max_examples=50)
def test_types::arraytypespecifier_instantiation(instance):
    assert isinstance(instance, types::ArrayTypeSpecifier)

@given(instance=types::ArrayTypeSpecifier_strategy)
def test_types::arraytypespecifier_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=types::ArrayTypeSpecifier_strategy)
def test_types::arraytypespecifier_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types::Annotation_strategy)
@settings(max_examples=50)
def test_types::annotation_instantiation(instance):
    assert isinstance(instance, types::Annotation)

@given(instance=types::Domain_strategy)
@settings(max_examples=50)
def test_types::domain_instantiation(instance):
    assert isinstance(instance, types::Domain)

@given(instance=types::Domain_strategy)
def test_types::domain_domainID_type(instance):
    assert isinstance(instance.domainID, str)


@given(instance=types::Domain_strategy)
def test_types::domain_domainID_setter(instance):
    original = instance.domainID
    instance.domainID = original
    assert instance.domainID == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=types::EnumerationType_strategy)
@settings(max_examples=50)
def test_types::enumerationtype_instantiation(instance):
    assert isinstance(instance, types::EnumerationType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types::TypeParameter_strategy)
@settings(max_examples=50)
def test_types::typeparameter_instantiation(instance):
    assert isinstance(instance, types::TypeParameter)

@given(instance=types::AnnotationType_strategy)
@settings(max_examples=50)
def test_types::annotationtype_instantiation(instance):
    assert isinstance(instance, types::AnnotationType)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=GenericElement_strategy)
@settings(max_examples=50)
def test_genericelement_instantiation(instance):
    assert isinstance(instance, GenericElement)

@given(instance=types::ComplexType_strategy)
@settings(max_examples=50)
def test_types::complextype_instantiation(instance):
    assert isinstance(instance, types::ComplexType)

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=types::Event_strategy)
@settings(max_examples=50)
def test_types::event_instantiation(instance):
    assert isinstance(instance, types::Event)

@given(instance=types::Event_strategy)
def test_types::event_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=types::Event_strategy)
def test_types::event_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=types::TypeAlias_strategy)
@settings(max_examples=50)
def test_types::typealias_instantiation(instance):
    assert isinstance(instance, types::TypeAlias)

@given(instance=types::Enumerator_strategy)
@settings(max_examples=50)
def test_types::enumerator_instantiation(instance):
    assert isinstance(instance, types::Enumerator)

@given(instance=types::Enumerator_strategy)
def test_types::enumerator_literalValue_type(instance):
    assert isinstance(instance.literalValue, int)


@given(instance=types::Enumerator_strategy)
def test_types::enumerator_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=types::Operation_strategy)
@settings(max_examples=50)
def test_types::operation_instantiation(instance):
    assert isinstance(instance, types::Operation)

@given(instance=types::Operation_strategy)
def test_types::operation_variadic_type(instance):
    assert isinstance(instance.variadic, bool)


@given(instance=types::Operation_strategy)
def test_types::operation_variadic_setter(instance):
    original = instance.variadic
    instance.variadic = original
    assert instance.variadic == original

@given(instance=MetaComposite_strategy)
@settings(max_examples=50)
def test_metacomposite_instantiation(instance):
    assert isinstance(instance, MetaComposite)

@given(instance=AnnotatableElement_strategy)
@settings(max_examples=50)
def test_annotatableelement_instantiation(instance):
    assert isinstance(instance, AnnotatableElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=types::GenericElement_strategy)
@settings(max_examples=50)
def test_types::genericelement_instantiation(instance):
    assert isinstance(instance, types::GenericElement)

@given(instance=types::TypeSpecifier_strategy)
@settings(max_examples=50)
def test_types::typespecifier_instantiation(instance):
    assert isinstance(instance, types::TypeSpecifier)

@given(instance=types::TypedElement_strategy)
@settings(max_examples=50)
def test_types::typedelement_instantiation(instance):
    assert isinstance(instance, types::TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=types::Expression_strategy)
@settings(max_examples=50)
def test_types::expression_instantiation(instance):
    assert isinstance(instance, types::Expression)

@given(instance=types::Property_strategy)
@settings(max_examples=50)
def test_types::property_instantiation(instance):
    assert isinstance(instance, types::Property)

@given(instance=types::Property_strategy)
def test_types::property_readonly_type(instance):
    assert isinstance(instance.readonly, bool)


@given(instance=types::Property_strategy)
def test_types::property_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=types::Property_strategy)
def test_types::property_const_type(instance):
    assert isinstance(instance.const, bool)


@given(instance=types::Property_strategy)
def test_types::property_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=types::Parameter_strategy)
@settings(max_examples=50)
def test_types::parameter_instantiation(instance):
    assert isinstance(instance, types::Parameter)

@given(instance=types::Parameter_strategy)
def test_types::parameter_varArgs_type(instance):
    assert isinstance(instance.varArgs, bool)


@given(instance=types::Parameter_strategy)
def test_types::parameter_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original

@given(instance=types::Parameter_strategy)
def test_types::parameter_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=types::Parameter_strategy)
def test_types::parameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=types::Declaration_strategy)
@settings(max_examples=50)
def test_types::declaration_instantiation(instance):
    assert isinstance(instance, types::Declaration)

@given(instance=types::Declaration_strategy)
def test_types::declaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=types::Declaration_strategy)
def test_types::declaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=types::Declaration_strategy)
def test_types::declaration_static_type(instance):
    assert isinstance(instance.static, bool)


@given(instance=types::Declaration_strategy)
def test_types::declaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original

@given(instance=DomainElement_strategy)
@settings(max_examples=50)
def test_domainelement_instantiation(instance):
    assert isinstance(instance, DomainElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=types::Type_strategy)
@settings(max_examples=50)
def test_types::type_instantiation(instance):
    assert isinstance(instance, types::Type)

@given(instance=types::Type_strategy)
def test_types::type_visible_type(instance):
    assert isinstance(instance.visible, bool)


@given(instance=types::Type_strategy)
def test_types::type_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original

@given(instance=types::Type_strategy)
def test_types::type_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=types::Type_strategy)
def test_types::type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types::Package_strategy)
@settings(max_examples=50)
def test_types::package_instantiation(instance):
    assert isinstance(instance, types::Package)

@given(instance=types::TypedDeclaration_strategy)
@settings(max_examples=50)
def test_types::typeddeclaration_instantiation(instance):
    assert isinstance(instance, types::TypedDeclaration)
