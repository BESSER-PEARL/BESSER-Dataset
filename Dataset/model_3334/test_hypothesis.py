import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    JParameter,
    javaMetaModel::JReferenceTypePar,
    javaMetaModel::JPrimitiveTypePar,
    JField,
    javaMetaModel::JReference,
    javaMetaModel::JAttribute,
    JElement,
    javaMetaModel::JPackage,
    javaMetaModel::JFeature,
    javaMetaModel::JClass,
    javaMetaModel::JParameter,
    JFeature,
    javaMetaModel::JField,
    javaMetaModel::JMethod,
    javaMetaModel::JElement,
    Vis,
    ReferenceType,
    Direction,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jparameter_is_not_abstract():
    assert not inspect.isabstract(JParameter)


def test_jparameter_constructor_exists():
    assert callable(JParameter.__init__)


def test_jparameter_constructor_args():
    sig = inspect.signature(JParameter.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jreferencetypepar_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JReferenceTypePar)


def test_javametamodel::jreferencetypepar_constructor_exists():
    assert callable(javaMetaModel::JReferenceTypePar.__init__)


def test_javametamodel::jreferencetypepar_constructor_args():
    sig = inspect.signature(javaMetaModel::JReferenceTypePar.__init__)
    params = list(sig.parameters.keys())
    assert "refType" in params, "Missing parameter 'refType'"

def test_javametamodel::jreferencetypepar_has_refType():
    assert hasattr(javaMetaModel::JReferenceTypePar, "refType")
    descriptor = None
    for klass in javaMetaModel::JReferenceTypePar.__mro__:
        if "refType" in klass.__dict__:
            descriptor = klass.__dict__["refType"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel::jprimitivetypepar_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JPrimitiveTypePar)


def test_javametamodel::jprimitivetypepar_constructor_exists():
    assert callable(javaMetaModel::JPrimitiveTypePar.__init__)


def test_javametamodel::jprimitivetypepar_constructor_args():
    sig = inspect.signature(javaMetaModel::JPrimitiveTypePar.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_javametamodel::jprimitivetypepar_has_primitiveType():
    assert hasattr(javaMetaModel::JPrimitiveTypePar, "primitiveType")
    descriptor = None
    for klass in javaMetaModel::JPrimitiveTypePar.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_jfield_is_not_abstract():
    assert not inspect.isabstract(JField)


def test_jfield_constructor_exists():
    assert callable(JField.__init__)


def test_jfield_constructor_args():
    sig = inspect.signature(JField.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jreference_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JReference)


def test_javametamodel::jreference_constructor_exists():
    assert callable(javaMetaModel::JReference.__init__)


def test_javametamodel::jreference_constructor_args():
    sig = inspect.signature(javaMetaModel::JReference.__init__)
    params = list(sig.parameters.keys())
    assert "refType" in params, "Missing parameter 'refType'"

def test_javametamodel::jreference_has_refType():
    assert hasattr(javaMetaModel::JReference, "refType")
    descriptor = None
    for klass in javaMetaModel::JReference.__mro__:
        if "refType" in klass.__dict__:
            descriptor = klass.__dict__["refType"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel::jattribute_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JAttribute)


def test_javametamodel::jattribute_constructor_exists():
    assert callable(javaMetaModel::JAttribute.__init__)


def test_javametamodel::jattribute_constructor_args():
    sig = inspect.signature(javaMetaModel::JAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_javametamodel::jattribute_has_primitiveType():
    assert hasattr(javaMetaModel::JAttribute, "primitiveType")
    descriptor = None
    for klass in javaMetaModel::JAttribute.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_jelement_is_not_abstract():
    assert not inspect.isabstract(JElement)


def test_jelement_constructor_exists():
    assert callable(JElement.__init__)


def test_jelement_constructor_args():
    sig = inspect.signature(JElement.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jpackage_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JPackage)


def test_javametamodel::jpackage_constructor_exists():
    assert callable(javaMetaModel::JPackage.__init__)


def test_javametamodel::jpackage_constructor_args():
    sig = inspect.signature(javaMetaModel::JPackage.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jfeature_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JFeature)


def test_javametamodel::jfeature_constructor_exists():
    assert callable(javaMetaModel::JFeature.__init__)


def test_javametamodel::jfeature_constructor_args():
    sig = inspect.signature(javaMetaModel::JFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javametamodel::jfeature_has_isStatic():
    assert hasattr(javaMetaModel::JFeature, "isStatic")
    descriptor = None
    for klass in javaMetaModel::JFeature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_javametamodel::jfeature_has_visibility():
    assert hasattr(javaMetaModel::JFeature, "visibility")
    descriptor = None
    for klass in javaMetaModel::JFeature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel::jclass_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JClass)


def test_javametamodel::jclass_constructor_exists():
    assert callable(javaMetaModel::JClass.__init__)


def test_javametamodel::jclass_constructor_args():
    sig = inspect.signature(javaMetaModel::JClass.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_javametamodel::jclass_has_isAbstract():
    assert hasattr(javaMetaModel::JClass, "isAbstract")
    descriptor = None
    for klass in javaMetaModel::JClass.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_javametamodel::jclass_has_isFinal():
    assert hasattr(javaMetaModel::JClass, "isFinal")
    descriptor = None
    for klass in javaMetaModel::JClass.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel::jparameter_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JParameter)


def test_javametamodel::jparameter_constructor_exists():
    assert callable(javaMetaModel::JParameter.__init__)


def test_javametamodel::jparameter_constructor_args():
    sig = inspect.signature(javaMetaModel::JParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_javametamodel::jparameter_has_direction():
    assert hasattr(javaMetaModel::JParameter, "direction")
    descriptor = None
    for klass in javaMetaModel::JParameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_jfeature_is_not_abstract():
    assert not inspect.isabstract(JFeature)


def test_jfeature_constructor_exists():
    assert callable(JFeature.__init__)


def test_jfeature_constructor_args():
    sig = inspect.signature(JFeature.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jfield_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JField)


def test_javametamodel::jfield_constructor_exists():
    assert callable(javaMetaModel::JField.__init__)


def test_javametamodel::jfield_constructor_args():
    sig = inspect.signature(javaMetaModel::JField.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jmethod_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JMethod)


def test_javametamodel::jmethod_constructor_exists():
    assert callable(javaMetaModel::JMethod.__init__)


def test_javametamodel::jmethod_constructor_args():
    sig = inspect.signature(javaMetaModel::JMethod.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel::jelement_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel::JElement)


def test_javametamodel::jelement_constructor_exists():
    assert callable(javaMetaModel::JElement.__init__)


def test_javametamodel::jelement_constructor_args():
    sig = inspect.signature(javaMetaModel::JElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javametamodel::jelement_has_name():
    assert hasattr(javaMetaModel::JElement, "name")
    descriptor = None
    for klass in javaMetaModel::JElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vis_exists():
    # Check that the Enumeration exists
    assert Vis is not None

def test_vis_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Vis]
    expected_literals = [
        "protected",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Vis"

def test_referencetype_exists():
    # Check that the Enumeration exists
    assert ReferenceType is not None

def test_referencetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferenceType]
    expected_literals = [
        "JInterfaceType",
        "JArrayType",
        "JClassType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "input",
        "return_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "JChar",
        "JInt",
        "JFloat",
        "JDouble",
        "JShort",
        "JLong",
        "JBoolean",
        "JByte",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
JParameter_strategy = st.builds(
    JParameter,
)
javaMetaModel::JReferenceTypePar_strategy = st.builds(
    javaMetaModel::JReferenceTypePar,
    refType=
        safe_text
)
javaMetaModel::JPrimitiveTypePar_strategy = st.builds(
    javaMetaModel::JPrimitiveTypePar,
    primitiveType=
        safe_text
)
JField_strategy = st.builds(
    JField,
)
javaMetaModel::JReference_strategy = st.builds(
    javaMetaModel::JReference,
    refType=
        safe_text
)
javaMetaModel::JAttribute_strategy = st.builds(
    javaMetaModel::JAttribute,
    primitiveType=
        safe_text
)
JElement_strategy = st.builds(
    JElement,
)
javaMetaModel::JPackage_strategy = st.builds(
    javaMetaModel::JPackage,
)
javaMetaModel::JFeature_strategy = st.builds(
    javaMetaModel::JFeature,
    isStatic=
        st.booleans(),
    visibility=
        safe_text
)
javaMetaModel::JClass_strategy = st.builds(
    javaMetaModel::JClass,
    isAbstract=
        st.booleans(),
    isFinal=
        st.booleans()
)
javaMetaModel::JParameter_strategy = st.builds(
    javaMetaModel::JParameter,
    direction=
        safe_text
)
JFeature_strategy = st.builds(
    JFeature,
)
javaMetaModel::JField_strategy = st.builds(
    javaMetaModel::JField,
)
javaMetaModel::JMethod_strategy = st.builds(
    javaMetaModel::JMethod,
)
javaMetaModel::JElement_strategy = st.builds(
    javaMetaModel::JElement,
    name=
        safe_text
)

@given(instance=JParameter_strategy)
@settings(max_examples=50)
def test_jparameter_instantiation(instance):
    assert isinstance(instance, JParameter)

@given(instance=javaMetaModel::JReferenceTypePar_strategy)
@settings(max_examples=50)
def test_javametamodel::jreferencetypepar_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JReferenceTypePar)

@given(instance=javaMetaModel::JReferenceTypePar_strategy)
def test_javametamodel::jreferencetypepar_refType_type(instance):
    assert isinstance(instance.refType, str)


@given(instance=javaMetaModel::JReferenceTypePar_strategy)
def test_javametamodel::jreferencetypepar_refType_setter(instance):
    original = instance.refType
    instance.refType = original
    assert instance.refType == original

@given(instance=javaMetaModel::JPrimitiveTypePar_strategy)
@settings(max_examples=50)
def test_javametamodel::jprimitivetypepar_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JPrimitiveTypePar)

@given(instance=javaMetaModel::JPrimitiveTypePar_strategy)
def test_javametamodel::jprimitivetypepar_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=javaMetaModel::JPrimitiveTypePar_strategy)
def test_javametamodel::jprimitivetypepar_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=JField_strategy)
@settings(max_examples=50)
def test_jfield_instantiation(instance):
    assert isinstance(instance, JField)

@given(instance=javaMetaModel::JReference_strategy)
@settings(max_examples=50)
def test_javametamodel::jreference_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JReference)

@given(instance=javaMetaModel::JReference_strategy)
def test_javametamodel::jreference_refType_type(instance):
    assert isinstance(instance.refType, str)


@given(instance=javaMetaModel::JReference_strategy)
def test_javametamodel::jreference_refType_setter(instance):
    original = instance.refType
    instance.refType = original
    assert instance.refType == original

@given(instance=javaMetaModel::JAttribute_strategy)
@settings(max_examples=50)
def test_javametamodel::jattribute_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JAttribute)

@given(instance=javaMetaModel::JAttribute_strategy)
def test_javametamodel::jattribute_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=javaMetaModel::JAttribute_strategy)
def test_javametamodel::jattribute_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=JElement_strategy)
@settings(max_examples=50)
def test_jelement_instantiation(instance):
    assert isinstance(instance, JElement)

@given(instance=javaMetaModel::JPackage_strategy)
@settings(max_examples=50)
def test_javametamodel::jpackage_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JPackage)

@given(instance=javaMetaModel::JFeature_strategy)
@settings(max_examples=50)
def test_javametamodel::jfeature_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JFeature)

@given(instance=javaMetaModel::JFeature_strategy)
def test_javametamodel::jfeature_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=javaMetaModel::JFeature_strategy)
def test_javametamodel::jfeature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=javaMetaModel::JFeature_strategy)
def test_javametamodel::jfeature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=javaMetaModel::JFeature_strategy)
def test_javametamodel::jfeature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=javaMetaModel::JClass_strategy)
@settings(max_examples=50)
def test_javametamodel::jclass_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JClass)

@given(instance=javaMetaModel::JClass_strategy)
def test_javametamodel::jclass_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=javaMetaModel::JClass_strategy)
def test_javametamodel::jclass_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=javaMetaModel::JClass_strategy)
def test_javametamodel::jclass_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=javaMetaModel::JClass_strategy)
def test_javametamodel::jclass_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=javaMetaModel::JParameter_strategy)
@settings(max_examples=50)
def test_javametamodel::jparameter_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JParameter)

@given(instance=javaMetaModel::JParameter_strategy)
def test_javametamodel::jparameter_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=javaMetaModel::JParameter_strategy)
def test_javametamodel::jparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=JFeature_strategy)
@settings(max_examples=50)
def test_jfeature_instantiation(instance):
    assert isinstance(instance, JFeature)

@given(instance=javaMetaModel::JField_strategy)
@settings(max_examples=50)
def test_javametamodel::jfield_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JField)

@given(instance=javaMetaModel::JMethod_strategy)
@settings(max_examples=50)
def test_javametamodel::jmethod_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JMethod)

@given(instance=javaMetaModel::JElement_strategy)
@settings(max_examples=50)
def test_javametamodel::jelement_instantiation(instance):
    assert isinstance(instance, javaMetaModel::JElement)

@given(instance=javaMetaModel::JElement_strategy)
def test_javametamodel::jelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javaMetaModel::JElement_strategy)
def test_javametamodel::jelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
