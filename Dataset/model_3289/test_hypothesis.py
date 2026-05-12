import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    base_BooleanLiteral,
    base_LiteralArray,
    base_StringLiteral,
    NumberLiteral,
    base_IntLiteral,
    base_RealLiteral,
    base_NumberLiteral,
    base_AnnotationAttribute,
    base_Documentation,
    base_Literal,
    base_Import,
    AnnotationAttribute,
    base_EnumAnnotationAttribute,
    base_SimpleAnnotationAttribute,
    base_KeyValue,
    base_AnnotationType,
    base_Annotation,
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



def test_base_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(base_BooleanLiteral)


def test_base_booleanliteral_constructor_exists():
    assert callable(base_BooleanLiteral.__init__)


def test_base_booleanliteral_constructor_args():
    sig = inspect.signature(base_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "isTrue" in params, "Missing parameter 'isTrue'"

def test_base_booleanliteral_has_isTrue():
    assert hasattr(base_BooleanLiteral, "isTrue")
    descriptor = None
    for klass in base_BooleanLiteral.__mro__:
        if "isTrue" in klass.__dict__:
            descriptor = klass.__dict__["isTrue"]
            break
    assert isinstance(descriptor, property)



def test_base_literalarray_is_not_abstract():
    assert not inspect.isabstract(base_LiteralArray)


def test_base_literalarray_constructor_exists():
    assert callable(base_LiteralArray.__init__)


def test_base_literalarray_constructor_args():
    sig = inspect.signature(base_LiteralArray.__init__)
    params = list(sig.parameters.keys())



def test_base_stringliteral_is_not_abstract():
    assert not inspect.isabstract(base_StringLiteral)


def test_base_stringliteral_constructor_exists():
    assert callable(base_StringLiteral.__init__)


def test_base_stringliteral_constructor_args():
    sig = inspect.signature(base_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base_stringliteral_has_value():
    assert hasattr(base_StringLiteral, "value")
    descriptor = None
    for klass in base_StringLiteral.__mro__:
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



def test_base_intliteral_is_not_abstract():
    assert not inspect.isabstract(base_IntLiteral)


def test_base_intliteral_constructor_exists():
    assert callable(base_IntLiteral.__init__)


def test_base_intliteral_constructor_args():
    sig = inspect.signature(base_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base_intliteral_has_value():
    assert hasattr(base_IntLiteral, "value")
    descriptor = None
    for klass in base_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_base_realliteral_is_not_abstract():
    assert not inspect.isabstract(base_RealLiteral)


def test_base_realliteral_constructor_exists():
    assert callable(base_RealLiteral.__init__)


def test_base_realliteral_constructor_args():
    sig = inspect.signature(base_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_base_realliteral_has_value():
    assert hasattr(base_RealLiteral, "value")
    descriptor = None
    for klass in base_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_base_numberliteral_is_not_abstract():
    assert not inspect.isabstract(base_NumberLiteral)


def test_base_numberliteral_constructor_exists():
    assert callable(base_NumberLiteral.__init__)


def test_base_numberliteral_constructor_args():
    sig = inspect.signature(base_NumberLiteral.__init__)
    params = list(sig.parameters.keys())



def test_base_annotationattribute_is_not_abstract():
    assert not inspect.isabstract(base_AnnotationAttribute)


def test_base_annotationattribute_constructor_exists():
    assert callable(base_AnnotationAttribute.__init__)


def test_base_annotationattribute_constructor_args():
    sig = inspect.signature(base_AnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_base_annotationattribute_has_optional():
    assert hasattr(base_AnnotationAttribute, "optional")
    descriptor = None
    for klass in base_AnnotationAttribute.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_base_annotationattribute_has_name():
    assert hasattr(base_AnnotationAttribute, "name")
    descriptor = None
    for klass in base_AnnotationAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_base_documentation_is_not_abstract():
    assert not inspect.isabstract(base_Documentation)


def test_base_documentation_constructor_exists():
    assert callable(base_Documentation.__init__)


def test_base_documentation_constructor_args():
    sig = inspect.signature(base_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "lines" in params, "Missing parameter 'lines'"

def test_base_documentation_has_lines():
    assert hasattr(base_Documentation, "lines")
    descriptor = None
    for klass in base_Documentation.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)



def test_base_literal_is_not_abstract():
    assert not inspect.isabstract(base_Literal)


def test_base_literal_constructor_exists():
    assert callable(base_Literal.__init__)


def test_base_literal_constructor_args():
    sig = inspect.signature(base_Literal.__init__)
    params = list(sig.parameters.keys())



def test_base_import_is_not_abstract():
    assert not inspect.isabstract(base_Import)


def test_base_import_constructor_exists():
    assert callable(base_Import.__init__)


def test_base_import_constructor_args():
    sig = inspect.signature(base_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_base_import_has_importedNamespace():
    assert hasattr(base_Import, "importedNamespace")
    descriptor = None
    for klass in base_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_base_import_has_importURI():
    assert hasattr(base_Import, "importURI")
    descriptor = None
    for klass in base_Import.__mro__:
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



def test_base_enumannotationattribute_is_not_abstract():
    assert not inspect.isabstract(base_EnumAnnotationAttribute)


def test_base_enumannotationattribute_constructor_exists():
    assert callable(base_EnumAnnotationAttribute.__init__)


def test_base_enumannotationattribute_constructor_args():
    sig = inspect.signature(base_EnumAnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_base_enumannotationattribute_has_values():
    assert hasattr(base_EnumAnnotationAttribute, "values")
    descriptor = None
    for klass in base_EnumAnnotationAttribute.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_base_simpleannotationattribute_is_not_abstract():
    assert not inspect.isabstract(base_SimpleAnnotationAttribute)


def test_base_simpleannotationattribute_constructor_exists():
    assert callable(base_SimpleAnnotationAttribute.__init__)


def test_base_simpleannotationattribute_constructor_args():
    sig = inspect.signature(base_SimpleAnnotationAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_base_simpleannotationattribute_has_type():
    assert hasattr(base_SimpleAnnotationAttribute, "type")
    descriptor = None
    for klass in base_SimpleAnnotationAttribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_base_keyvalue_is_not_abstract():
    assert not inspect.isabstract(base_KeyValue)


def test_base_keyvalue_constructor_exists():
    assert callable(base_KeyValue.__init__)


def test_base_keyvalue_constructor_args():
    sig = inspect.signature(base_KeyValue.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_base_keyvalue_has_key():
    assert hasattr(base_KeyValue, "key")
    descriptor = None
    for klass in base_KeyValue.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_base_annotationtype_is_not_abstract():
    assert not inspect.isabstract(base_AnnotationType)


def test_base_annotationtype_constructor_exists():
    assert callable(base_AnnotationType.__init__)


def test_base_annotationtype_constructor_args():
    sig = inspect.signature(base_AnnotationType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "targets" in params, "Missing parameter 'targets'"

def test_base_annotationtype_has_name():
    assert hasattr(base_AnnotationType, "name")
    descriptor = None
    for klass in base_AnnotationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_base_annotationtype_has_targets():
    assert hasattr(base_AnnotationType, "targets")
    descriptor = None
    for klass in base_AnnotationType.__mro__:
        if "targets" in klass.__dict__:
            descriptor = klass.__dict__["targets"]
            break
    assert isinstance(descriptor, property)



def test_base_annotation_is_not_abstract():
    assert not inspect.isabstract(base_Annotation)


def test_base_annotation_constructor_exists():
    assert callable(base_Annotation.__init__)


def test_base_annotation_constructor_args():
    sig = inspect.signature(base_Annotation.__init__)
    params = list(sig.parameters.keys())

def test_literaltype_exists():
    # Check that the Enumeration exists
    assert LiteralType is not None

def test_literaltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LiteralType]
    expected_literals = [
        "BOOL",
        "CHAR",
        "REAL",
        "INT",
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
base_BooleanLiteral_strategy = st.builds(
    base_BooleanLiteral,
    isTrue=
        st.booleans()
)
base_LiteralArray_strategy = st.builds(
    base_LiteralArray,
)
base_StringLiteral_strategy = st.builds(
    base_StringLiteral,
    value=
        safe_text
)
NumberLiteral_strategy = st.builds(
    NumberLiteral,
)
base_IntLiteral_strategy = st.builds(
    base_IntLiteral,
    value=
        safe_text
)
base_RealLiteral_strategy = st.builds(
    base_RealLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
base_NumberLiteral_strategy = st.builds(
    base_NumberLiteral,
)
base_AnnotationAttribute_strategy = st.builds(
    base_AnnotationAttribute,
    optional=
        st.booleans(),
    name=
        safe_text
)
base_Documentation_strategy = st.builds(
    base_Documentation,
    lines=
        safe_text
)
base_Literal_strategy = st.builds(
    base_Literal,
)
base_Import_strategy = st.builds(
    base_Import,
    importedNamespace=
        safe_text,
    importURI=
        safe_text
)
AnnotationAttribute_strategy = st.builds(
    AnnotationAttribute,
)
base_EnumAnnotationAttribute_strategy = st.builds(
    base_EnumAnnotationAttribute,
    values=
        safe_text
)
base_SimpleAnnotationAttribute_strategy = st.builds(
    base_SimpleAnnotationAttribute,
    type=
        safe_text
)
base_KeyValue_strategy = st.builds(
    base_KeyValue,
    key=
        safe_text
)
base_AnnotationType_strategy = st.builds(
    base_AnnotationType,
    name=
        safe_text,
    targets=
        safe_text
)
base_Annotation_strategy = st.builds(
    base_Annotation,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=base_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_base_booleanliteral_instantiation(instance):
    assert isinstance(instance, base_BooleanLiteral)



@given(instance=base_BooleanLiteral_strategy)
def test_base_booleanliteral_isTrue_setter(instance):
    original = instance.isTrue
    instance.isTrue = original
    assert instance.isTrue == original

@given(instance=base_LiteralArray_strategy)
@settings(max_examples=50)
def test_base_literalarray_instantiation(instance):
    assert isinstance(instance, base_LiteralArray)

@given(instance=base_StringLiteral_strategy)
@settings(max_examples=50)
def test_base_stringliteral_instantiation(instance):
    assert isinstance(instance, base_StringLiteral)



@given(instance=base_StringLiteral_strategy)
def test_base_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NumberLiteral_strategy)
@settings(max_examples=50)
def test_numberliteral_instantiation(instance):
    assert isinstance(instance, NumberLiteral)

@given(instance=base_IntLiteral_strategy)
@settings(max_examples=50)
def test_base_intliteral_instantiation(instance):
    assert isinstance(instance, base_IntLiteral)



@given(instance=base_IntLiteral_strategy)
def test_base_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=base_RealLiteral_strategy)
@settings(max_examples=50)
def test_base_realliteral_instantiation(instance):
    assert isinstance(instance, base_RealLiteral)



@given(instance=base_RealLiteral_strategy)
def test_base_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=base_NumberLiteral_strategy)
@settings(max_examples=50)
def test_base_numberliteral_instantiation(instance):
    assert isinstance(instance, base_NumberLiteral)

@given(instance=base_AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base_annotationattribute_instantiation(instance):
    assert isinstance(instance, base_AnnotationAttribute)



@given(instance=base_AnnotationAttribute_strategy)
def test_base_annotationattribute_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=base_AnnotationAttribute_strategy)
def test_base_annotationattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=base_Documentation_strategy)
@settings(max_examples=50)
def test_base_documentation_instantiation(instance):
    assert isinstance(instance, base_Documentation)



@given(instance=base_Documentation_strategy)
def test_base_documentation_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=base_Literal_strategy)
@settings(max_examples=50)
def test_base_literal_instantiation(instance):
    assert isinstance(instance, base_Literal)

@given(instance=base_Import_strategy)
@settings(max_examples=50)
def test_base_import_instantiation(instance):
    assert isinstance(instance, base_Import)



@given(instance=base_Import_strategy)
def test_base_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original



@given(instance=base_Import_strategy)
def test_base_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=AnnotationAttribute_strategy)
@settings(max_examples=50)
def test_annotationattribute_instantiation(instance):
    assert isinstance(instance, AnnotationAttribute)

@given(instance=base_EnumAnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base_enumannotationattribute_instantiation(instance):
    assert isinstance(instance, base_EnumAnnotationAttribute)



@given(instance=base_EnumAnnotationAttribute_strategy)
def test_base_enumannotationattribute_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=base_SimpleAnnotationAttribute_strategy)
@settings(max_examples=50)
def test_base_simpleannotationattribute_instantiation(instance):
    assert isinstance(instance, base_SimpleAnnotationAttribute)



@given(instance=base_SimpleAnnotationAttribute_strategy)
def test_base_simpleannotationattribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=base_KeyValue_strategy)
@settings(max_examples=50)
def test_base_keyvalue_instantiation(instance):
    assert isinstance(instance, base_KeyValue)



@given(instance=base_KeyValue_strategy)
def test_base_keyvalue_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=base_AnnotationType_strategy)
@settings(max_examples=50)
def test_base_annotationtype_instantiation(instance):
    assert isinstance(instance, base_AnnotationType)



@given(instance=base_AnnotationType_strategy)
def test_base_annotationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=base_AnnotationType_strategy)
def test_base_annotationtype_targets_setter(instance):
    original = instance.targets
    instance.targets = original
    assert instance.targets == original

@given(instance=base_Annotation_strategy)
@settings(max_examples=50)
def test_base_annotation_instantiation(instance):
    assert isinstance(instance, base_Annotation)
