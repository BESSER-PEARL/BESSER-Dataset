import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    javaz_JavaElement,
    javaz_Block,
    JavaElement,
    javaz_JavaClass,
    javaz_Method,
    javaz_JavaPackageX,
    javaz_Field,
    javaz_JavaParameter,
    javaz_Javaz,
    JavaVisibilityKind,
    JavaKind,
    JavaParameterKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_javaz_javaelement_is_not_abstract():
    assert not inspect.isabstract(javaz_JavaElement)


def test_javaz_javaelement_constructor_exists():
    assert callable(javaz_JavaElement.__init__)


def test_javaz_javaelement_constructor_args():
    sig = inspect.signature(javaz_JavaElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javaz_javaelement_has_name():
    assert hasattr(javaz_JavaElement, "name")
    descriptor = None
    for klass in javaz_JavaElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javaz_block_is_not_abstract():
    assert not inspect.isabstract(javaz_Block)


def test_javaz_block_constructor_exists():
    assert callable(javaz_Block.__init__)


def test_javaz_block_constructor_args():
    sig = inspect.signature(javaz_Block.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_javaz_block_has_content():
    assert hasattr(javaz_Block, "content")
    descriptor = None
    for klass in javaz_Block.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_javaelement_is_not_abstract():
    assert not inspect.isabstract(JavaElement)


def test_javaelement_constructor_exists():
    assert callable(JavaElement.__init__)


def test_javaelement_constructor_args():
    sig = inspect.signature(JavaElement.__init__)
    params = list(sig.parameters.keys())



def test_javaz_javaclass_is_not_abstract():
    assert not inspect.isabstract(javaz_JavaClass)


def test_javaz_javaclass_constructor_exists():
    assert callable(javaz_JavaClass.__init__)


def test_javaz_javaclass_constructor_args():
    sig = inspect.signature(javaz_JavaClass.__init__)
    params = list(sig.parameters.keys())
    assert "needToGenerate" in params, "Missing parameter 'needToGenerate'"
    assert "final" in params, "Missing parameter 'final'"
    assert "rewritable" in params, "Missing parameter 'rewritable'"
    assert "public" in params, "Missing parameter 'public'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_javaz_javaclass_has_needToGenerate():
    assert hasattr(javaz_JavaClass, "needToGenerate")
    descriptor = None
    for klass in javaz_JavaClass.__mro__:
        if "needToGenerate" in klass.__dict__:
            descriptor = klass.__dict__["needToGenerate"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaclass_has_final():
    assert hasattr(javaz_JavaClass, "final")
    descriptor = None
    for klass in javaz_JavaClass.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaclass_has_rewritable():
    assert hasattr(javaz_JavaClass, "rewritable")
    descriptor = None
    for klass in javaz_JavaClass.__mro__:
        if "rewritable" in klass.__dict__:
            descriptor = klass.__dict__["rewritable"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaclass_has_public():
    assert hasattr(javaz_JavaClass, "public")
    descriptor = None
    for klass in javaz_JavaClass.__mro__:
        if "public" in klass.__dict__:
            descriptor = klass.__dict__["public"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaclass_has_kind():
    assert hasattr(javaz_JavaClass, "kind")
    descriptor = None
    for klass in javaz_JavaClass.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_javaz_method_is_not_abstract():
    assert not inspect.isabstract(javaz_Method)


def test_javaz_method_constructor_exists():
    assert callable(javaz_Method.__init__)


def test_javaz_method_constructor_args():
    sig = inspect.signature(javaz_Method.__init__)
    params = list(sig.parameters.keys())
    assert "static" in params, "Missing parameter 'static'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "native" in params, "Missing parameter 'native'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "constructor" in params, "Missing parameter 'constructor'"
    assert "final" in params, "Missing parameter 'final'"
    assert "synchronized" in params, "Missing parameter 'synchronized'"

def test_javaz_method_has_static():
    assert hasattr(javaz_Method, "static")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_visibility():
    assert hasattr(javaz_Method, "visibility")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_native():
    assert hasattr(javaz_Method, "native")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "native" in klass.__dict__:
            descriptor = klass.__dict__["native"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_abstract():
    assert hasattr(javaz_Method, "abstract")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_constructor():
    assert hasattr(javaz_Method, "constructor")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "constructor" in klass.__dict__:
            descriptor = klass.__dict__["constructor"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_final():
    assert hasattr(javaz_Method, "final")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_javaz_method_has_synchronized():
    assert hasattr(javaz_Method, "synchronized")
    descriptor = None
    for klass in javaz_Method.__mro__:
        if "synchronized" in klass.__dict__:
            descriptor = klass.__dict__["synchronized"]
            break
    assert isinstance(descriptor, property)



def test_javaz_javapackagex_is_not_abstract():
    assert not inspect.isabstract(javaz_JavaPackageX)


def test_javaz_javapackagex_constructor_exists():
    assert callable(javaz_JavaPackageX.__init__)


def test_javaz_javapackagex_constructor_args():
    sig = inspect.signature(javaz_JavaPackageX.__init__)
    params = list(sig.parameters.keys())
    assert "needToGenerate" in params, "Missing parameter 'needToGenerate'"

def test_javaz_javapackagex_has_needToGenerate():
    assert hasattr(javaz_JavaPackageX, "needToGenerate")
    descriptor = None
    for klass in javaz_JavaPackageX.__mro__:
        if "needToGenerate" in klass.__dict__:
            descriptor = klass.__dict__["needToGenerate"]
            break
    assert isinstance(descriptor, property)



def test_javaz_field_is_not_abstract():
    assert not inspect.isabstract(javaz_Field)


def test_javaz_field_constructor_exists():
    assert callable(javaz_Field.__init__)


def test_javaz_field_constructor_args():
    sig = inspect.signature(javaz_Field.__init__)
    params = list(sig.parameters.keys())
    assert "volatile" in params, "Missing parameter 'volatile'"
    assert "transient" in params, "Missing parameter 'transient'"
    assert "type" in params, "Missing parameter 'type'"
    assert "static" in params, "Missing parameter 'static'"
    assert "final" in params, "Missing parameter 'final'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javaz_field_has_volatile():
    assert hasattr(javaz_Field, "volatile")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "volatile" in klass.__dict__:
            descriptor = klass.__dict__["volatile"]
            break
    assert isinstance(descriptor, property)

def test_javaz_field_has_transient():
    assert hasattr(javaz_Field, "transient")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "transient" in klass.__dict__:
            descriptor = klass.__dict__["transient"]
            break
    assert isinstance(descriptor, property)

def test_javaz_field_has_type():
    assert hasattr(javaz_Field, "type")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_javaz_field_has_static():
    assert hasattr(javaz_Field, "static")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "static" in klass.__dict__:
            descriptor = klass.__dict__["static"]
            break
    assert isinstance(descriptor, property)

def test_javaz_field_has_final():
    assert hasattr(javaz_Field, "final")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)

def test_javaz_field_has_visibility():
    assert hasattr(javaz_Field, "visibility")
    descriptor = None
    for klass in javaz_Field.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_javaz_javaparameter_is_not_abstract():
    assert not inspect.isabstract(javaz_JavaParameter)


def test_javaz_javaparameter_constructor_exists():
    assert callable(javaz_JavaParameter.__init__)


def test_javaz_javaparameter_constructor_args():
    sig = inspect.signature(javaz_JavaParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterKind" in params, "Missing parameter 'parameterKind'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "type" in params, "Missing parameter 'type'"
    assert "final" in params, "Missing parameter 'final'"

def test_javaz_javaparameter_has_parameterKind():
    assert hasattr(javaz_JavaParameter, "parameterKind")
    descriptor = None
    for klass in javaz_JavaParameter.__mro__:
        if "parameterKind" in klass.__dict__:
            descriptor = klass.__dict__["parameterKind"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaparameter_has_kind():
    assert hasattr(javaz_JavaParameter, "kind")
    descriptor = None
    for klass in javaz_JavaParameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaparameter_has_type():
    assert hasattr(javaz_JavaParameter, "type")
    descriptor = None
    for klass in javaz_JavaParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_javaz_javaparameter_has_final():
    assert hasattr(javaz_JavaParameter, "final")
    descriptor = None
    for klass in javaz_JavaParameter.__mro__:
        if "final" in klass.__dict__:
            descriptor = klass.__dict__["final"]
            break
    assert isinstance(descriptor, property)



def test_javaz_javaz_is_not_abstract():
    assert not inspect.isabstract(javaz_Javaz)


def test_javaz_javaz_constructor_exists():
    assert callable(javaz_Javaz.__init__)


def test_javaz_javaz_constructor_args():
    sig = inspect.signature(javaz_Javaz.__init__)
    params = list(sig.parameters.keys())

def test_javavisibilitykind_exists():
    # Check that the Enumeration exists
    assert JavaVisibilityKind is not None

def test_javavisibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JavaVisibilityKind]
    expected_literals = [
        "PACKAGE",
        "PRIVATE",
        "PROTECTED",
        "PUBLIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JavaVisibilityKind"

def test_javakind_exists():
    # Check that the Enumeration exists
    assert JavaKind is not None

def test_javakind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JavaKind]
    expected_literals = [
        "EXCEPTION",
        "CLASS",
        "INTERFACE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JavaKind"

def test_javaparameterkind_exists():
    # Check that the Enumeration exists
    assert JavaParameterKind is not None

def test_javaparameterkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JavaParameterKind]
    expected_literals = [
        "INOUT",
        "IN",
        "RETURN",
        "OUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JavaParameterKind"


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
javaz_JavaElement_strategy = st.builds(
    javaz_JavaElement,
    name=
        safe_text
)
javaz_Block_strategy = st.builds(
    javaz_Block,
    content=
        safe_text
)
JavaElement_strategy = st.builds(
    JavaElement,
)
javaz_JavaClass_strategy = st.builds(
    javaz_JavaClass,
    needToGenerate=
        st.booleans(),
    final=
        st.booleans(),
    rewritable=
        st.booleans(),
    public=
        st.booleans(),
    kind=
        safe_text
)
javaz_Method_strategy = st.builds(
    javaz_Method,
    static=
        st.booleans(),
    visibility=
        safe_text,
    native=
        st.booleans(),
    abstract=
        st.booleans(),
    constructor=
        st.booleans(),
    final=
        st.booleans(),
    synchronized=
        st.booleans()
)
javaz_JavaPackageX_strategy = st.builds(
    javaz_JavaPackageX,
    needToGenerate=
        st.booleans()
)
javaz_Field_strategy = st.builds(
    javaz_Field,
    volatile=
        st.booleans(),
    transient=
        st.booleans(),
    type=
        safe_text,
    static=
        st.booleans(),
    final=
        st.booleans(),
    visibility=
        safe_text
)
javaz_JavaParameter_strategy = st.builds(
    javaz_JavaParameter,
    parameterKind=
        safe_text,
    kind=
        safe_text,
    type=
        safe_text,
    final=
        st.booleans()
)
javaz_Javaz_strategy = st.builds(
    javaz_Javaz,
)

@given(instance=javaz_JavaElement_strategy)
@settings(max_examples=50)
def test_javaz_javaelement_instantiation(instance):
    assert isinstance(instance, javaz_JavaElement)



@given(instance=javaz_JavaElement_strategy)
def test_javaz_javaelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javaz_Block_strategy)
@settings(max_examples=50)
def test_javaz_block_instantiation(instance):
    assert isinstance(instance, javaz_Block)



@given(instance=javaz_Block_strategy)
def test_javaz_block_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=JavaElement_strategy)
@settings(max_examples=50)
def test_javaelement_instantiation(instance):
    assert isinstance(instance, JavaElement)

@given(instance=javaz_JavaClass_strategy)
@settings(max_examples=50)
def test_javaz_javaclass_instantiation(instance):
    assert isinstance(instance, javaz_JavaClass)



@given(instance=javaz_JavaClass_strategy)
def test_javaz_javaclass_needToGenerate_setter(instance):
    original = instance.needToGenerate
    instance.needToGenerate = original
    assert instance.needToGenerate == original



@given(instance=javaz_JavaClass_strategy)
def test_javaz_javaclass_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=javaz_JavaClass_strategy)
def test_javaz_javaclass_rewritable_setter(instance):
    original = instance.rewritable
    instance.rewritable = original
    assert instance.rewritable == original



@given(instance=javaz_JavaClass_strategy)
def test_javaz_javaclass_public_setter(instance):
    original = instance.public
    instance.public = original
    assert instance.public == original



@given(instance=javaz_JavaClass_strategy)
def test_javaz_javaclass_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=javaz_Method_strategy)
@settings(max_examples=50)
def test_javaz_method_instantiation(instance):
    assert isinstance(instance, javaz_Method)



@given(instance=javaz_Method_strategy)
def test_javaz_method_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_native_setter(instance):
    original = instance.native
    instance.native = original
    assert instance.native == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_constructor_setter(instance):
    original = instance.constructor
    instance.constructor = original
    assert instance.constructor == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=javaz_Method_strategy)
def test_javaz_method_synchronized_setter(instance):
    original = instance.synchronized
    instance.synchronized = original
    assert instance.synchronized == original

@given(instance=javaz_JavaPackageX_strategy)
@settings(max_examples=50)
def test_javaz_javapackagex_instantiation(instance):
    assert isinstance(instance, javaz_JavaPackageX)



@given(instance=javaz_JavaPackageX_strategy)
def test_javaz_javapackagex_needToGenerate_setter(instance):
    original = instance.needToGenerate
    instance.needToGenerate = original
    assert instance.needToGenerate == original

@given(instance=javaz_Field_strategy)
@settings(max_examples=50)
def test_javaz_field_instantiation(instance):
    assert isinstance(instance, javaz_Field)



@given(instance=javaz_Field_strategy)
def test_javaz_field_volatile_setter(instance):
    original = instance.volatile
    instance.volatile = original
    assert instance.volatile == original



@given(instance=javaz_Field_strategy)
def test_javaz_field_transient_setter(instance):
    original = instance.transient
    instance.transient = original
    assert instance.transient == original



@given(instance=javaz_Field_strategy)
def test_javaz_field_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=javaz_Field_strategy)
def test_javaz_field_static_setter(instance):
    original = instance.static
    instance.static = original
    assert instance.static == original



@given(instance=javaz_Field_strategy)
def test_javaz_field_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original



@given(instance=javaz_Field_strategy)
def test_javaz_field_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=javaz_JavaParameter_strategy)
@settings(max_examples=50)
def test_javaz_javaparameter_instantiation(instance):
    assert isinstance(instance, javaz_JavaParameter)



@given(instance=javaz_JavaParameter_strategy)
def test_javaz_javaparameter_parameterKind_setter(instance):
    original = instance.parameterKind
    instance.parameterKind = original
    assert instance.parameterKind == original



@given(instance=javaz_JavaParameter_strategy)
def test_javaz_javaparameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=javaz_JavaParameter_strategy)
def test_javaz_javaparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=javaz_JavaParameter_strategy)
def test_javaz_javaparameter_final_setter(instance):
    original = instance.final
    instance.final = original
    assert instance.final == original

@given(instance=javaz_Javaz_strategy)
@settings(max_examples=50)
def test_javaz_javaz_instantiation(instance):
    assert isinstance(instance, javaz_Javaz)
