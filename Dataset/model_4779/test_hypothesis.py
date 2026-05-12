import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    types_AnnotatableElement,
    types_MetaComposite,
    types_EObject,
    TypeSpecifier,
    types_ArrayTypeSpecifier,
    types_Annotation,
    types_Domain,
    ComplexType,
    types_EnumerationType,
    Type,
    types_AnnotationType,
    types_TypeParameter,
    types_PrimitiveType,
    GenericElement,
    types_ComplexType,
    TypedDeclaration,
    types_TypeAlias,
    types_Event,
    types_Enumerator,
    types_Operation,
    MetaComposite,
    AnnotatableElement,
    NamedElement,
    types_GenericElement,
    types_TypeSpecifier,
    types_TypedElement,
    TypedElement,
    types_Expression,
    types_Property,
    types_Parameter,
    types_Declaration,
    DomainElement,
    Declaration,
    types_Package,
    types_Type,
    types_TypedDeclaration,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_types_annotatableelement_is_not_abstract():
    assert not inspect.isabstract(types_AnnotatableElement)


def test_types_annotatableelement_constructor_exists():
    assert callable(types_AnnotatableElement.__init__)


def test_types_annotatableelement_constructor_args():
    sig = inspect.signature(types_AnnotatableElement.__init__)
    params = list(sig.parameters.keys())



def test_types_metacomposite_is_not_abstract():
    assert not inspect.isabstract(types_MetaComposite)


def test_types_metacomposite_constructor_exists():
    assert callable(types_MetaComposite.__init__)


def test_types_metacomposite_constructor_args():
    sig = inspect.signature(types_MetaComposite.__init__)
    params = list(sig.parameters.keys())



def test_types_eobject_is_not_abstract():
    assert not inspect.isabstract(types_EObject)


def test_types_eobject_constructor_exists():
    assert callable(types_EObject.__init__)


def test_types_eobject_constructor_args():
    sig = inspect.signature(types_EObject.__init__)
    params = list(sig.parameters.keys())



def test_typespecifier_is_not_abstract():
    assert not inspect.isabstract(TypeSpecifier)


def test_typespecifier_constructor_exists():
    assert callable(TypeSpecifier.__init__)


def test_typespecifier_constructor_args():
    sig = inspect.signature(TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_types_arraytypespecifier_is_not_abstract():
    assert not inspect.isabstract(types_ArrayTypeSpecifier)


def test_types_arraytypespecifier_constructor_exists():
    assert callable(types_ArrayTypeSpecifier.__init__)


def test_types_arraytypespecifier_constructor_args():
    sig = inspect.signature(types_ArrayTypeSpecifier.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_types_arraytypespecifier_has_size():
    assert hasattr(types_ArrayTypeSpecifier, "size")
    descriptor = None
    for klass in types_ArrayTypeSpecifier.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_types_annotation_is_not_abstract():
    assert not inspect.isabstract(types_Annotation)


def test_types_annotation_constructor_exists():
    assert callable(types_Annotation.__init__)


def test_types_annotation_constructor_args():
    sig = inspect.signature(types_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_types_domain_is_not_abstract():
    assert not inspect.isabstract(types_Domain)


def test_types_domain_constructor_exists():
    assert callable(types_Domain.__init__)


def test_types_domain_constructor_args():
    sig = inspect.signature(types_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "domainID" in params, "Missing parameter 'domainID'"

def test_types_domain_has_domainID():
    assert hasattr(types_Domain, "domainID")
    descriptor = None
    for klass in types_Domain.__mro__:
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



def test_types_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(types_EnumerationType)


def test_types_enumerationtype_constructor_exists():
    assert callable(types_EnumerationType.__init__)


def test_types_enumerationtype_constructor_args():
    sig = inspect.signature(types_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_types_annotationtype_is_not_abstract():
    assert not inspect.isabstract(types_AnnotationType)


def test_types_annotationtype_constructor_exists():
    assert callable(types_AnnotationType.__init__)


def test_types_annotationtype_constructor_args():
    sig = inspect.signature(types_AnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_types_typeparameter_is_not_abstract():
    assert not inspect.isabstract(types_TypeParameter)


def test_types_typeparameter_constructor_exists():
    assert callable(types_TypeParameter.__init__)


def test_types_typeparameter_constructor_args():
    sig = inspect.signature(types_TypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_types_primitivetype_is_not_abstract():
    assert not inspect.isabstract(types_PrimitiveType)


def test_types_primitivetype_constructor_exists():
    assert callable(types_PrimitiveType.__init__)


def test_types_primitivetype_constructor_args():
    sig = inspect.signature(types_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_genericelement_is_not_abstract():
    assert not inspect.isabstract(GenericElement)


def test_genericelement_constructor_exists():
    assert callable(GenericElement.__init__)


def test_genericelement_constructor_args():
    sig = inspect.signature(GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_types_complextype_is_not_abstract():
    assert not inspect.isabstract(types_ComplexType)


def test_types_complextype_constructor_exists():
    assert callable(types_ComplexType.__init__)


def test_types_complextype_constructor_args():
    sig = inspect.signature(types_ComplexType.__init__)
    params = list(sig.parameters.keys())



def test_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(TypedDeclaration)


def test_typeddeclaration_constructor_exists():
    assert callable(TypedDeclaration.__init__)


def test_typeddeclaration_constructor_args():
    sig = inspect.signature(TypedDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_types_typealias_is_not_abstract():
    assert not inspect.isabstract(types_TypeAlias)


def test_types_typealias_constructor_exists():
    assert callable(types_TypeAlias.__init__)


def test_types_typealias_constructor_args():
    sig = inspect.signature(types_TypeAlias.__init__)
    params = list(sig.parameters.keys())



def test_types_event_is_not_abstract():
    assert not inspect.isabstract(types_Event)


def test_types_event_constructor_exists():
    assert callable(types_Event.__init__)


def test_types_event_constructor_args():
    sig = inspect.signature(types_Event.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_types_event_has_direction():
    assert hasattr(types_Event, "direction")
    descriptor = None
    for klass in types_Event.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_types_enumerator_is_not_abstract():
    assert not inspect.isabstract(types_Enumerator)


def test_types_enumerator_constructor_exists():
    assert callable(types_Enumerator.__init__)


def test_types_enumerator_constructor_args():
    sig = inspect.signature(types_Enumerator.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_types_enumerator_has_literalValue():
    assert hasattr(types_Enumerator, "literalValue")
    descriptor = None
    for klass in types_Enumerator.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_types_operation_is_not_abstract():
    assert not inspect.isabstract(types_Operation)


def test_types_operation_constructor_exists():
    assert callable(types_Operation.__init__)


def test_types_operation_constructor_args():
    sig = inspect.signature(types_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "variadic" in params, "Missing parameter 'variadic'"

def test_types_operation_has_variadic():
    assert hasattr(types_Operation, "variadic")
    descriptor = None
    for klass in types_Operation.__mro__:
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



def test_types_genericelement_is_not_abstract():
    assert not inspect.isabstract(types_GenericElement)


def test_types_genericelement_constructor_exists():
    assert callable(types_GenericElement.__init__)


def test_types_genericelement_constructor_args():
    sig = inspect.signature(types_GenericElement.__init__)
    params = list(sig.parameters.keys())



def test_types_typespecifier_is_not_abstract():
    assert not inspect.isabstract(types_TypeSpecifier)


def test_types_typespecifier_constructor_exists():
    assert callable(types_TypeSpecifier.__init__)


def test_types_typespecifier_constructor_args():
    sig = inspect.signature(types_TypeSpecifier.__init__)
    params = list(sig.parameters.keys())



def test_types_typedelement_is_not_abstract():
    assert not inspect.isabstract(types_TypedElement)


def test_types_typedelement_constructor_exists():
    assert callable(types_TypedElement.__init__)


def test_types_typedelement_constructor_args():
    sig = inspect.signature(types_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types_expression_is_not_abstract():
    assert not inspect.isabstract(types_Expression)


def test_types_expression_constructor_exists():
    assert callable(types_Expression.__init__)


def test_types_expression_constructor_args():
    sig = inspect.signature(types_Expression.__init__)
    params = list(sig.parameters.keys())



def test_types_property_is_not_abstract():
    assert not inspect.isabstract(types_Property)


def test_types_property_constructor_exists():
    assert callable(types_Property.__init__)


def test_types_property_constructor_args():
    sig = inspect.signature(types_Property.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_types_property_has_const():
    assert hasattr(types_Property, "const")
    descriptor = None
    for klass in types_Property.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)

def test_types_property_has_readonly():
    assert hasattr(types_Property, "readonly")
    descriptor = None
    for klass in types_Property.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_types_parameter_is_not_abstract():
    assert not inspect.isabstract(types_Parameter)


def test_types_parameter_constructor_exists():
    assert callable(types_Parameter.__init__)


def test_types_parameter_constructor_args():
    sig = inspect.signature(types_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "varArgs" in params, "Missing parameter 'varArgs'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_types_parameter_has_varArgs():
    assert hasattr(types_Parameter, "varArgs")
    descriptor = None
    for klass in types_Parameter.__mro__:
        if "varArgs" in klass.__dict__:
            descriptor = klass.__dict__["varArgs"]
            break
    assert isinstance(descriptor, property)

def test_types_parameter_has_optional():
    assert hasattr(types_Parameter, "optional")
    descriptor = None
    for klass in types_Parameter.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_types_declaration_is_not_abstract():
    assert not inspect.isabstract(types_Declaration)


def test_types_declaration_constructor_exists():
    assert callable(types_Declaration.__init__)


def test_types_declaration_constructor_args():
    sig = inspect.signature(types_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "id" in params, "Missing parameter 'id'"

def test_types_declaration_has_static():
    assert hasattr(types_Declaration, "static")
    descriptor = None
    for klass in types_Declaration.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_types_declaration_has_id():
    assert hasattr(types_Declaration, "id")
    descriptor = None
    for klass in types_Declaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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



def test_types_package_is_not_abstract():
    assert not inspect.isabstract(types_Package)


def test_types_package_constructor_exists():
    assert callable(types_Package.__init__)


def test_types_package_constructor_args():
    sig = inspect.signature(types_Package.__init__)
    params = list(sig.parameters.keys())



def test_types_type_is_not_abstract():
    assert not inspect.isabstract(types_Type)


def test_types_type_constructor_exists():
    assert callable(types_Type.__init__)


def test_types_type_constructor_args():
    sig = inspect.signature(types_Type.__init__)
    params = list(sig.parameters.keys())
    assert "visible" in params, "Missing parameter 'visible'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_types_type_has_visible():
    assert hasattr(types_Type, "visible")
    descriptor = None
    for klass in types_Type.__mro__:
        if "visible" in klass.__dict__:
            descriptor = klass.__dict__["visible"]
            break
    assert isinstance(descriptor, property)

def test_types_type_has_abstract():
    assert hasattr(types_Type, "abstract")
    descriptor = None
    for klass in types_Type.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_types_typeddeclaration_is_not_abstract():
    assert not inspect.isabstract(types_TypedDeclaration)


def test_types_typeddeclaration_constructor_exists():
    assert callable(types_TypedDeclaration.__init__)


def test_types_typeddeclaration_constructor_args():
    sig = inspect.signature(types_TypedDeclaration.__init__)
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
types_AnnotatableElement_strategy = st.builds(
    types_AnnotatableElement,
)
types_MetaComposite_strategy = st.builds(
    types_MetaComposite,
)
types_EObject_strategy = st.builds(
    types_EObject,
)
TypeSpecifier_strategy = st.builds(
    TypeSpecifier,
)
types_ArrayTypeSpecifier_strategy = st.builds(
    types_ArrayTypeSpecifier,
    size=
        st.integers()
)
types_Annotation_strategy = st.builds(
    types_Annotation,
)
types_Domain_strategy = st.builds(
    types_Domain,
    domainID=
        safe_text
)
ComplexType_strategy = st.builds(
    ComplexType,
)
types_EnumerationType_strategy = st.builds(
    types_EnumerationType,
)
Type_strategy = st.builds(
    Type,
)
types_AnnotationType_strategy = st.builds(
    types_AnnotationType,
)
types_TypeParameter_strategy = st.builds(
    types_TypeParameter,
)
types_PrimitiveType_strategy = st.builds(
    types_PrimitiveType,
)
GenericElement_strategy = st.builds(
    GenericElement,
)
types_ComplexType_strategy = st.builds(
    types_ComplexType,
)
TypedDeclaration_strategy = st.builds(
    TypedDeclaration,
)
types_TypeAlias_strategy = st.builds(
    types_TypeAlias,
)
types_Event_strategy = st.builds(
    types_Event,
    direction=
        safe_text
)
types_Enumerator_strategy = st.builds(
    types_Enumerator,
    literalValue=
        st.integers()
)
types_Operation_strategy = st.builds(
    types_Operation,
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
types_GenericElement_strategy = st.builds(
    types_GenericElement,
)
types_TypeSpecifier_strategy = st.builds(
    types_TypeSpecifier,
)
types_TypedElement_strategy = st.builds(
    types_TypedElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
types_Expression_strategy = st.builds(
    types_Expression,
)
types_Property_strategy = st.builds(
    types_Property,
    const=
        st.booleans(),
    readonly=
        st.booleans()
)
types_Parameter_strategy = st.builds(
    types_Parameter,
    varArgs=
        st.booleans(),
    optional=
        st.booleans()
)
types_Declaration_strategy = st.builds(
    types_Declaration,
    static=
        st.booleans(),
    id=
        safe_text
)
DomainElement_strategy = st.builds(
    DomainElement,
)
Declaration_strategy = st.builds(
    Declaration,
)
types_Package_strategy = st.builds(
    types_Package,
)
types_Type_strategy = st.builds(
    types_Type,
    visible=
        st.booleans(),
    abstract=
        st.booleans()
)
types_TypedDeclaration_strategy = st.builds(
    types_TypedDeclaration,
)

@given(instance=types_AnnotatableElement_strategy)
@settings(max_examples=50)
def test_types_annotatableelement_instantiation(instance):
    assert isinstance(instance, types_AnnotatableElement)

@given(instance=types_MetaComposite_strategy)
@settings(max_examples=50)
def test_types_metacomposite_instantiation(instance):
    assert isinstance(instance, types_MetaComposite)

@given(instance=types_EObject_strategy)
@settings(max_examples=50)
def test_types_eobject_instantiation(instance):
    assert isinstance(instance, types_EObject)

@given(instance=TypeSpecifier_strategy)
@settings(max_examples=50)
def test_typespecifier_instantiation(instance):
    assert isinstance(instance, TypeSpecifier)

@given(instance=types_ArrayTypeSpecifier_strategy)
@settings(max_examples=50)
def test_types_arraytypespecifier_instantiation(instance):
    assert isinstance(instance, types_ArrayTypeSpecifier)



@given(instance=types_ArrayTypeSpecifier_strategy)
def test_types_arraytypespecifier_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=types_Annotation_strategy)
@settings(max_examples=50)
def test_types_annotation_instantiation(instance):
    assert isinstance(instance, types_Annotation)

@given(instance=types_Domain_strategy)
@settings(max_examples=50)
def test_types_domain_instantiation(instance):
    assert isinstance(instance, types_Domain)



@given(instance=types_Domain_strategy)
def test_types_domain_domainID_setter(instance):
    original = instance.domainID
    instance.domainID = original
    assert instance.domainID == original

@given(instance=ComplexType_strategy)
@settings(max_examples=50)
def test_complextype_instantiation(instance):
    assert isinstance(instance, ComplexType)

@given(instance=types_EnumerationType_strategy)
@settings(max_examples=50)
def test_types_enumerationtype_instantiation(instance):
    assert isinstance(instance, types_EnumerationType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=types_AnnotationType_strategy)
@settings(max_examples=50)
def test_types_annotationtype_instantiation(instance):
    assert isinstance(instance, types_AnnotationType)

@given(instance=types_TypeParameter_strategy)
@settings(max_examples=50)
def test_types_typeparameter_instantiation(instance):
    assert isinstance(instance, types_TypeParameter)

@given(instance=types_PrimitiveType_strategy)
@settings(max_examples=50)
def test_types_primitivetype_instantiation(instance):
    assert isinstance(instance, types_PrimitiveType)

@given(instance=GenericElement_strategy)
@settings(max_examples=50)
def test_genericelement_instantiation(instance):
    assert isinstance(instance, GenericElement)

@given(instance=types_ComplexType_strategy)
@settings(max_examples=50)
def test_types_complextype_instantiation(instance):
    assert isinstance(instance, types_ComplexType)

@given(instance=TypedDeclaration_strategy)
@settings(max_examples=50)
def test_typeddeclaration_instantiation(instance):
    assert isinstance(instance, TypedDeclaration)

@given(instance=types_TypeAlias_strategy)
@settings(max_examples=50)
def test_types_typealias_instantiation(instance):
    assert isinstance(instance, types_TypeAlias)

@given(instance=types_Event_strategy)
@settings(max_examples=50)
def test_types_event_instantiation(instance):
    assert isinstance(instance, types_Event)



@given(instance=types_Event_strategy)
def test_types_event_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=types_Enumerator_strategy)
@settings(max_examples=50)
def test_types_enumerator_instantiation(instance):
    assert isinstance(instance, types_Enumerator)



@given(instance=types_Enumerator_strategy)
def test_types_enumerator_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=types_Operation_strategy)
@settings(max_examples=50)
def test_types_operation_instantiation(instance):
    assert isinstance(instance, types_Operation)



@given(instance=types_Operation_strategy)
def test_types_operation_variadic_setter(instance):
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

@given(instance=types_GenericElement_strategy)
@settings(max_examples=50)
def test_types_genericelement_instantiation(instance):
    assert isinstance(instance, types_GenericElement)

@given(instance=types_TypeSpecifier_strategy)
@settings(max_examples=50)
def test_types_typespecifier_instantiation(instance):
    assert isinstance(instance, types_TypeSpecifier)

@given(instance=types_TypedElement_strategy)
@settings(max_examples=50)
def test_types_typedelement_instantiation(instance):
    assert isinstance(instance, types_TypedElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=types_Expression_strategy)
@settings(max_examples=50)
def test_types_expression_instantiation(instance):
    assert isinstance(instance, types_Expression)

@given(instance=types_Property_strategy)
@settings(max_examples=50)
def test_types_property_instantiation(instance):
    assert isinstance(instance, types_Property)



@given(instance=types_Property_strategy)
def test_types_property_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original



@given(instance=types_Property_strategy)
def test_types_property_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=types_Parameter_strategy)
@settings(max_examples=50)
def test_types_parameter_instantiation(instance):
    assert isinstance(instance, types_Parameter)



@given(instance=types_Parameter_strategy)
def test_types_parameter_varArgs_setter(instance):
    original = instance.varArgs
    instance.varArgs = original
    assert instance.varArgs == original



@given(instance=types_Parameter_strategy)
def test_types_parameter_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=types_Declaration_strategy)
@settings(max_examples=50)
def test_types_declaration_instantiation(instance):
    assert isinstance(instance, types_Declaration)



@given(instance=types_Declaration_strategy)
def test_types_declaration_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=types_Declaration_strategy)
def test_types_declaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=DomainElement_strategy)
@settings(max_examples=50)
def test_domainelement_instantiation(instance):
    assert isinstance(instance, DomainElement)

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=types_Package_strategy)
@settings(max_examples=50)
def test_types_package_instantiation(instance):
    assert isinstance(instance, types_Package)

@given(instance=types_Type_strategy)
@settings(max_examples=50)
def test_types_type_instantiation(instance):
    assert isinstance(instance, types_Type)



@given(instance=types_Type_strategy)
def test_types_type_visible_setter(instance):
    original = instance.visible
    instance.visible = original
    assert instance.visible == original



@given(instance=types_Type_strategy)
def test_types_type_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=types_TypedDeclaration_strategy)
@settings(max_examples=50)
def test_types_typeddeclaration_instantiation(instance):
    assert isinstance(instance, types_TypedDeclaration)
