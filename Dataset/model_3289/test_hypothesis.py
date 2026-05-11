import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Literal,
    base::BooleanLiteral,
    base::LiteralArray,
    base::StringLiteral,
    NumberLiteral,
    base::IntLiteral,
    base::RealLiteral,
    base::NumberLiteral,
    base::AnnotationAttribute,
    base::Documentation,
    base::Literal,
    base::Import,
    AnnotationAttribute,
    base::EnumAnnotationAttribute,
    base::SimpleAnnotationAttribute,
    base::KeyValue,
    base::AnnotationType,
    base::Annotation,
    LiteralType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_base::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(base::BooleanLiteral)


def test_base::booleanliteral_constructor_exists():
    assert callable(base::BooleanLiteral.__init__)


def test_base::booleanliteral_constructor_args():
    sig = inspect.signature(base::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_base::booleanliteral_has_isTrue():
    assert hasattr(base::BooleanLiteral, "isTrue")
    descriptor = None
    for klass in base::BooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_base::literalarray_is_not_abstract():
    assert not inspect.isabstract(base::LiteralArray)


def test_base::literalarray_constructor_exists():
    assert callable(base::LiteralArray.__init__)


def test_base::literalarray_constructor_args():
    sig = inspect.signature(base::LiteralArray.__init__)
    params = list(sig.parameters.keys())



def test_base::stringliteral_is_not_abstract():
    assert not inspect.isabstract(base::StringLiteral)


def test_base::stringliteral_constructor_exists():
    assert callable(base::StringLiteral.__init__)


def test_base::stringliteral_constructor_args():
    sig = inspect.signature(base::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base::stringliteral_has_value():
    assert hasattr(base::StringLiteral, "value")
    descriptor = None
    for klass in base::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_numberliteral_is_not_abstract():
    assert not inspect.isabstract(NumberLiteral)


def test_numberliteral_constructor_exists():
    assert callable(NumberLiteral.__init__)


def test_numberliteral_constructor_args():
    sig = inspect.signature(NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_base::intliteral_is_not_abstract():
    assert not inspect.isabstract(base::IntLiteral)


def test_base::intliteral_constructor_exists():
    assert callable(base::IntLiteral.__init__)


def test_base::intliteral_constructor_args():
    sig = inspect.signature(base::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base::intliteral_has_value():
    assert hasattr(base::IntLiteral, "value")
    descriptor = None
    for klass in base::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_base::realliteral_is_not_abstract():
    assert not inspect.isabstract(base::RealLiteral)


def test_base::realliteral_constructor_exists():
    assert callable(base::RealLiteral.__init__)


def test_base::realliteral_constructor_args():
    sig = inspect.signature(base::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base::realliteral_has_value():
    assert hasattr(base::RealLiteral, "value")
    descriptor = None
    for klass in base::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_base::numberliteral_is_not_abstract():
    assert not inspect.isabstract(base::NumberLiteral)


def test_base::numberliteral_constructor_exists():
    assert callable(base::NumberLiteral.__init__)


def test_base::numberliteral_constructor_args():
    sig = inspect.signature(base::NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_base::annotationattribute_is_not_abstract():
    assert not inspect.isabstract(base::AnnotationAttribute)


def test_base::annotationattribute_constructor_exists():
    assert callable(base::AnnotationAttribute.__init__)


def test_base::annotationattribute_constructor_args():
    sig = inspect.signature(base::AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_base::annotationattribute_has_optional():
    assert hasattr(base::AnnotationAttribute, "optional")
    descriptor = None
    for klass in base::AnnotationAttribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_base::annotationattribute_has_name():
    assert hasattr(base::AnnotationAttribute, "name")
    descriptor = None
    for klass in base::AnnotationAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_base::documentation_is_not_abstract():
    assert not inspect.isabstract(base::Documentation)


def test_base::documentation_constructor_exists():
    assert callable(base::Documentation.__init__)


def test_base::documentation_constructor_args():
    sig = inspect.signature(base::Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "lines" in params, "Missing parameter 'lines'"

def test_base::documentation_has_lines():
    assert hasattr(base::Documentation, "lines")
    descriptor = None
    for klass in base::Documentation.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)



def test_base::literal_is_not_abstract():
    assert not inspect.isabstract(base::Literal)


def test_base::literal_constructor_exists():
    assert callable(base::Literal.__init__)


def test_base::literal_constructor_args():
    sig = inspect.signature(base::Literal.__init__)
    params = list(sig.parameters.keys())



def test_base::import_is_not_abstract():
    assert not inspect.isabstract(base::Import)


def test_base::import_constructor_exists():
    assert callable(base::Import.__init__)


def test_base::import_constructor_args():
    sig = inspect.signature(base::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_base::import_has_importedNamespace():
    assert hasattr(base::Import, "importedNamespace")
    descriptor = None
    for klass in base::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_base::import_has_importURI():
    assert hasattr(base::Import, "importURI")
    descriptor = None
    for klass in base::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_annotationattribute_is_not_abstract():
    assert not inspect.isabstract(AnnotationAttribute)


def test_annotationattribute_constructor_exists():
    assert callable(AnnotationAttribute.__init__)


def test_annotationattribute_constructor_args():
    sig = inspect.signature(AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())



def test_base::enumannotationattribute_is_not_abstract():
    assert not inspect.isabstract(base::EnumAnnotationAttribute)


def test_base::enumannotationattribute_constructor_exists():
    assert callable(base::EnumAnnotationAttribute.__init__)


def test_base::enumannotationattribute_constructor_args():
    sig = inspect.signature(base::EnumAnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_base::enumannotationattribute_has_values():
    assert hasattr(base::EnumAnnotationAttribute, "values")
    descriptor = None
    for klass in base::EnumAnnotationAttribute.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_base::simpleannotationattribute_is_not_abstract():
    assert not inspect.isabstract(base::SimpleAnnotationAttribute)


def test_base::simpleannotationattribute_constructor_exists():
    assert callable(base::SimpleAnnotationAttribute.__init__)


def test_base::simpleannotationattribute_constructor_args():
    sig = inspect.signature(base::SimpleAnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_base::simpleannotationattribute_has_type():
    assert hasattr(base::SimpleAnnotationAttribute, "type")
    descriptor = None
    for klass in base::SimpleAnnotationAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_base::keyvalue_is_not_abstract():
    assert not inspect.isabstract(base::KeyValue)


def test_base::keyvalue_constructor_exists():
    assert callable(base::KeyValue.__init__)


def test_base::keyvalue_constructor_args():
    sig = inspect.signature(base::KeyValue.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_base::keyvalue_has_key():
    assert hasattr(base::KeyValue, "key")
    descriptor = None
    for klass in base::KeyValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_base::annotationtype_is_not_abstract():
    assert not inspect.isabstract(base::AnnotationType)


def test_base::annotationtype_constructor_exists():
    assert callable(base::AnnotationType.__init__)


def test_base::annotationtype_constructor_args():
    sig = inspect.signature(base::AnnotationType.__init__)
    params = list(sig.parameters.keys())
    assert "targets" in params, "Missing parameter 'targets'"
    assert "name" in params, "Missing parameter 'name'"

def test_base::annotationtype_has_targets():
    assert hasattr(base::AnnotationType, "targets")
    descriptor = None
    for klass in base::AnnotationType.__mro__:
        if "targets" in klass.__dict__:
            descriptor = klass.__dict__["targets"]
            break
    assert isinstance(descriptor, property)

def test_base::annotationtype_has_name():
    assert hasattr(base::AnnotationType, "name")
    descriptor = None
    for klass in base::AnnotationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_base::annotation_is_not_abstract():
    assert not inspect.isabstract(base::Annotation)


def test_base::annotation_constructor_exists():
    assert callable(base::Annotation.__init__)


def test_base::annotation_constructor_args():
    sig = inspect.signature(base::Annotation.__init__)
    params = list(sig.parameters.keys())

def test_literaltype_exists():
    # Check that the Enumeration exists
    assert LiteralType is not None

def test_literaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralType]
    expected_literals = [
        "INT",
        "REAL",
        "CHAR",
        "BOOL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LiteralType"


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
Literal_strategy = st.builds(
    Literal,
)
base::BooleanLiteral_strategy = st.builds(
    base::BooleanLiteral,
    isTrue=
        st.booleans()
)
base::LiteralArray_strategy = st.builds(
    base::LiteralArray,
)
base::StringLiteral_strategy = st.builds(
    base::StringLiteral,
    value=
        safe_text
)
NumberLiteral_strategy = st.builds(
    NumberLiteral,
)
base::IntLiteral_strategy = st.builds(
    base::IntLiteral,
    value=
        safe_text
)
base::RealLiteral_strategy = st.builds(
    base::RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
base::NumberLiteral_strategy = st.builds(
    base::NumberLiteral,
)
base::AnnotationAttribute_strategy = st.builds(
    base::AnnotationAttribute,
    optional=
        st.booleans(),
    name=
        safe_text
)
base::Documentation_strategy = st.builds(
    base::Documentation,
    lines=
        safe_text
)
base::Literal_strategy = st.builds(
    base::Literal,
)
base::Import_strategy = st.builds(
    base::Import,
    importedNamespace=
        safe_text,
    importURI=
        safe_text
)
AnnotationAttribute_strategy = st.builds(
    AnnotationAttribute,
)
base::EnumAnnotationAttribute_strategy = st.builds(
    base::EnumAnnotationAttribute,
    values=
        safe_text
)
base::SimpleAnnotationAttribute_strategy = st.builds(
    base::SimpleAnnotationAttribute,
    type=
        safe_text
)
base::KeyValue_strategy = st.builds(
    base::KeyValue,
    key=
        safe_text
)
base::AnnotationType_strategy = st.builds(
    base::AnnotationType,
    targets=
        safe_text,
    name=
        safe_text
)
base::Annotation_strategy = st.builds(
    base::Annotation,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=base::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_base::booleanliteral_instantiation(instance):
    assert isinstance(instance, base::BooleanLiteral)

@given(instance=base::BooleanLiteral_strategy)
def test_base::booleanliteral_isTrue_type(instance):
    assert isinstance(instance.isTrue, bool)


@given(instance=base::BooleanLiteral_strategy)
def test_base::booleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=base::LiteralArray_strategy)
@settings(max_examples=50)
def test_base::literalarray_instantiation(instance):
    assert isinstance(instance, base::LiteralArray)

@given(instance=base::StringLiteral_strategy)
@settings(max_examples=50)
def test_base::stringliteral_instantiation(instance):
    assert isinstance(instance, base::StringLiteral)

@given(instance=base::StringLiteral_strategy)
def test_base::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=base::StringLiteral_strategy)
def test_base::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberLiteral_strategy)
@settings(max_examples=50)
def test_numberliteral_instantiation(instance):
    assert isinstance(instance, NumberLiteral)

@given(instance=base::IntLiteral_strategy)
@settings(max_examples=50)
def test_base::intliteral_instantiation(instance):
    assert isinstance(instance, base::IntLiteral)

@given(instance=base::IntLiteral_strategy)
def test_base::intliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=base::IntLiteral_strategy)
def test_base::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=base::RealLiteral_strategy)
@settings(max_examples=50)
def test_base::realliteral_instantiation(instance):
    assert isinstance(instance, base::RealLiteral)

@given(instance=base::RealLiteral_strategy)
def test_base::realliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=base::RealLiteral_strategy)
def test_base::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=base::NumberLiteral_strategy)
@settings(max_examples=50)
def test_base::numberliteral_instantiation(instance):
    assert isinstance(instance, base::NumberLiteral)

@given(instance=base::AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base::annotationattribute_instantiation(instance):
    assert isinstance(instance, base::AnnotationAttribute)

@given(instance=base::AnnotationAttribute_strategy)
def test_base::annotationattribute_optional_type(instance):
    assert isinstance(instance.optional, bool)


@given(instance=base::AnnotationAttribute_strategy)
def test_base::annotationattribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=base::AnnotationAttribute_strategy)
def test_base::annotationattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=base::AnnotationAttribute_strategy)
def test_base::annotationattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=base::Documentation_strategy)
@settings(max_examples=50)
def test_base::documentation_instantiation(instance):
    assert isinstance(instance, base::Documentation)

@given(instance=base::Documentation_strategy)
def test_base::documentation_lines_type(instance):
    assert isinstance(instance.lines, str)


@given(instance=base::Documentation_strategy)
def test_base::documentation_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=base::Literal_strategy)
@settings(max_examples=50)
def test_base::literal_instantiation(instance):
    assert isinstance(instance, base::Literal)

@given(instance=base::Import_strategy)
@settings(max_examples=50)
def test_base::import_instantiation(instance):
    assert isinstance(instance, base::Import)

@given(instance=base::Import_strategy)
def test_base::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=base::Import_strategy)
def test_base::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=base::Import_strategy)
def test_base::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=base::Import_strategy)
def test_base::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_annotationattribute_instantiation(instance):
    assert isinstance(instance, AnnotationAttribute)

@given(instance=base::EnumAnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base::enumannotationattribute_instantiation(instance):
    assert isinstance(instance, base::EnumAnnotationAttribute)

@given(instance=base::EnumAnnotationAttribute_strategy)
def test_base::enumannotationattribute_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=base::EnumAnnotationAttribute_strategy)
def test_base::enumannotationattribute_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=base::SimpleAnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base::simpleannotationattribute_instantiation(instance):
    assert isinstance(instance, base::SimpleAnnotationAttribute)

@given(instance=base::SimpleAnnotationAttribute_strategy)
def test_base::simpleannotationattribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=base::SimpleAnnotationAttribute_strategy)
def test_base::simpleannotationattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=base::KeyValue_strategy)
@settings(max_examples=50)
def test_base::keyvalue_instantiation(instance):
    assert isinstance(instance, base::KeyValue)

@given(instance=base::KeyValue_strategy)
def test_base::keyvalue_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=base::KeyValue_strategy)
def test_base::keyvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=base::AnnotationType_strategy)
@settings(max_examples=50)
def test_base::annotationtype_instantiation(instance):
    assert isinstance(instance, base::AnnotationType)

@given(instance=base::AnnotationType_strategy)
def test_base::annotationtype_targets_type(instance):
    assert isinstance(instance.targets, str)


@given(instance=base::AnnotationType_strategy)
def test_base::annotationtype_targets_setter(instance):
    original = instance.targets
    instance.targets = original
    assert instance.targets == original

@given(instance=base::AnnotationType_strategy)
def test_base::annotationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=base::AnnotationType_strategy)
def test_base::annotationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=base::Annotation_strategy)
@settings(max_examples=50)
def test_base::annotation_instantiation(instance):
    assert isinstance(instance, base::Annotation)
