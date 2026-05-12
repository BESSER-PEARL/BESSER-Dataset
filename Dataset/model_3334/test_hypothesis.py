import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    JParameter,
    javaMetaModel_JReferenceTypePar,
    javaMetaModel_JPrimitiveTypePar,
    JField,
    javaMetaModel_JReference,
    javaMetaModel_JAttribute,
    JElement,
    javaMetaModel_JPackage,
    javaMetaModel_JFeature,
    javaMetaModel_JClass,
    javaMetaModel_JParameter,
    JFeature,
    javaMetaModel_JField,
    javaMetaModel_JMethod,
    javaMetaModel_JElement,
    Vis,
    ReferenceType,
    PrimitiveType,
    Direction,
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



def test_javametamodel_jreferencetypepar_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JReferenceTypePar)


def test_javametamodel_jreferencetypepar_constructor_exists():
    assert callable(javaMetaModel_JReferenceTypePar.__init__)


def test_javametamodel_jreferencetypepar_constructor_args():
    sig = inspect.signature(javaMetaModel_JReferenceTypePar.__init__)
    params = list(sig.parameters.keys())
    assert "refType" in params, "Missing parameter 'refType'"

def test_javametamodel_jreferencetypepar_has_refType():
    assert hasattr(javaMetaModel_JReferenceTypePar, "refType")
    descriptor = None
    for klass in javaMetaModel_JReferenceTypePar.__mro__:
        if "refType" in klass.__dict__:
            descriptor = klass.__dict__["refType"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel_jprimitivetypepar_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JPrimitiveTypePar)


def test_javametamodel_jprimitivetypepar_constructor_exists():
    assert callable(javaMetaModel_JPrimitiveTypePar.__init__)


def test_javametamodel_jprimitivetypepar_constructor_args():
    sig = inspect.signature(javaMetaModel_JPrimitiveTypePar.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_javametamodel_jprimitivetypepar_has_primitiveType():
    assert hasattr(javaMetaModel_JPrimitiveTypePar, "primitiveType")
    descriptor = None
    for klass in javaMetaModel_JPrimitiveTypePar.__mro__:
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



def test_javametamodel_jreference_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JReference)


def test_javametamodel_jreference_constructor_exists():
    assert callable(javaMetaModel_JReference.__init__)


def test_javametamodel_jreference_constructor_args():
    sig = inspect.signature(javaMetaModel_JReference.__init__)
    params = list(sig.parameters.keys())
    assert "refType" in params, "Missing parameter 'refType'"

def test_javametamodel_jreference_has_refType():
    assert hasattr(javaMetaModel_JReference, "refType")
    descriptor = None
    for klass in javaMetaModel_JReference.__mro__:
        if "refType" in klass.__dict__:
            descriptor = klass.__dict__["refType"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel_jattribute_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JAttribute)


def test_javametamodel_jattribute_constructor_exists():
    assert callable(javaMetaModel_JAttribute.__init__)


def test_javametamodel_jattribute_constructor_args():
    sig = inspect.signature(javaMetaModel_JAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_javametamodel_jattribute_has_primitiveType():
    assert hasattr(javaMetaModel_JAttribute, "primitiveType")
    descriptor = None
    for klass in javaMetaModel_JAttribute.__mro__:
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



def test_javametamodel_jpackage_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JPackage)


def test_javametamodel_jpackage_constructor_exists():
    assert callable(javaMetaModel_JPackage.__init__)


def test_javametamodel_jpackage_constructor_args():
    sig = inspect.signature(javaMetaModel_JPackage.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel_jfeature_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JFeature)


def test_javametamodel_jfeature_constructor_exists():
    assert callable(javaMetaModel_JFeature.__init__)


def test_javametamodel_jfeature_constructor_args():
    sig = inspect.signature(javaMetaModel_JFeature.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_javametamodel_jfeature_has_visibility():
    assert hasattr(javaMetaModel_JFeature, "visibility")
    descriptor = None
    for klass in javaMetaModel_JFeature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_javametamodel_jfeature_has_isStatic():
    assert hasattr(javaMetaModel_JFeature, "isStatic")
    descriptor = None
    for klass in javaMetaModel_JFeature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel_jclass_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JClass)


def test_javametamodel_jclass_constructor_exists():
    assert callable(javaMetaModel_JClass.__init__)


def test_javametamodel_jclass_constructor_args():
    sig = inspect.signature(javaMetaModel_JClass.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_javametamodel_jclass_has_isFinal():
    assert hasattr(javaMetaModel_JClass, "isFinal")
    descriptor = None
    for klass in javaMetaModel_JClass.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_javametamodel_jclass_has_isAbstract():
    assert hasattr(javaMetaModel_JClass, "isAbstract")
    descriptor = None
    for klass in javaMetaModel_JClass.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_javametamodel_jparameter_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JParameter)


def test_javametamodel_jparameter_constructor_exists():
    assert callable(javaMetaModel_JParameter.__init__)


def test_javametamodel_jparameter_constructor_args():
    sig = inspect.signature(javaMetaModel_JParameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_javametamodel_jparameter_has_direction():
    assert hasattr(javaMetaModel_JParameter, "direction")
    descriptor = None
    for klass in javaMetaModel_JParameter.__mro__:
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



def test_javametamodel_jfield_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JField)


def test_javametamodel_jfield_constructor_exists():
    assert callable(javaMetaModel_JField.__init__)


def test_javametamodel_jfield_constructor_args():
    sig = inspect.signature(javaMetaModel_JField.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel_jmethod_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JMethod)


def test_javametamodel_jmethod_constructor_exists():
    assert callable(javaMetaModel_JMethod.__init__)


def test_javametamodel_jmethod_constructor_args():
    sig = inspect.signature(javaMetaModel_JMethod.__init__)
    params = list(sig.parameters.keys())



def test_javametamodel_jelement_is_not_abstract():
    assert not inspect.isabstract(javaMetaModel_JElement)


def test_javametamodel_jelement_constructor_exists():
    assert callable(javaMetaModel_JElement.__init__)


def test_javametamodel_jelement_constructor_args():
    sig = inspect.signature(javaMetaModel_JElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javametamodel_jelement_has_name():
    assert hasattr(javaMetaModel_JElement, "name")
    descriptor = None
    for klass in javaMetaModel_JElement.__mro__:
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
        "private",
        "public",
        "protected",
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
        "JClassType",
        "JInterfaceType",
        "JArrayType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferenceType"

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "JInt",
        "JChar",
        "JShort",
        "JDouble",
        "JByte",
        "JBoolean",
        "JLong",
        "JFloat",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

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
javaMetaModel_JReferenceTypePar_strategy = st.builds(
    javaMetaModel_JReferenceTypePar,
    refType=
        safe_text
)
javaMetaModel_JPrimitiveTypePar_strategy = st.builds(
    javaMetaModel_JPrimitiveTypePar,
    primitiveType=
        safe_text
)
JField_strategy = st.builds(
    JField,
)
javaMetaModel_JReference_strategy = st.builds(
    javaMetaModel_JReference,
    refType=
        safe_text
)
javaMetaModel_JAttribute_strategy = st.builds(
    javaMetaModel_JAttribute,
    primitiveType=
        safe_text
)
JElement_strategy = st.builds(
    JElement,
)
javaMetaModel_JPackage_strategy = st.builds(
    javaMetaModel_JPackage,
)
javaMetaModel_JFeature_strategy = st.builds(
    javaMetaModel_JFeature,
    visibility=
        safe_text,
    isStatic=
        st.booleans()
)
javaMetaModel_JClass_strategy = st.builds(
    javaMetaModel_JClass,
    isFinal=
        st.booleans(),
    isAbstract=
        st.booleans()
)
javaMetaModel_JParameter_strategy = st.builds(
    javaMetaModel_JParameter,
    direction=
        safe_text
)
JFeature_strategy = st.builds(
    JFeature,
)
javaMetaModel_JField_strategy = st.builds(
    javaMetaModel_JField,
)
javaMetaModel_JMethod_strategy = st.builds(
    javaMetaModel_JMethod,
)
javaMetaModel_JElement_strategy = st.builds(
    javaMetaModel_JElement,
    name=
        safe_text
)

@given(instance=JParameter_strategy)
@settings(max_examples=50)
def test_jparameter_instantiation(instance):
    assert isinstance(instance, JParameter)

@given(instance=javaMetaModel_JReferenceTypePar_strategy)
@settings(max_examples=50)
def test_javametamodel_jreferencetypepar_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JReferenceTypePar)



@given(instance=javaMetaModel_JReferenceTypePar_strategy)
def test_javametamodel_jreferencetypepar_refType_setter(instance):
    original = instance.refType
    instance.refType = original
    assert instance.refType == original

@given(instance=javaMetaModel_JPrimitiveTypePar_strategy)
@settings(max_examples=50)
def test_javametamodel_jprimitivetypepar_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JPrimitiveTypePar)



@given(instance=javaMetaModel_JPrimitiveTypePar_strategy)
def test_javametamodel_jprimitivetypepar_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=JField_strategy)
@settings(max_examples=50)
def test_jfield_instantiation(instance):
    assert isinstance(instance, JField)

@given(instance=javaMetaModel_JReference_strategy)
@settings(max_examples=50)
def test_javametamodel_jreference_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JReference)



@given(instance=javaMetaModel_JReference_strategy)
def test_javametamodel_jreference_refType_setter(instance):
    original = instance.refType
    instance.refType = original
    assert instance.refType == original

@given(instance=javaMetaModel_JAttribute_strategy)
@settings(max_examples=50)
def test_javametamodel_jattribute_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JAttribute)



@given(instance=javaMetaModel_JAttribute_strategy)
def test_javametamodel_jattribute_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=JElement_strategy)
@settings(max_examples=50)
def test_jelement_instantiation(instance):
    assert isinstance(instance, JElement)

@given(instance=javaMetaModel_JPackage_strategy)
@settings(max_examples=50)
def test_javametamodel_jpackage_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JPackage)

@given(instance=javaMetaModel_JFeature_strategy)
@settings(max_examples=50)
def test_javametamodel_jfeature_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JFeature)



@given(instance=javaMetaModel_JFeature_strategy)
def test_javametamodel_jfeature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=javaMetaModel_JFeature_strategy)
def test_javametamodel_jfeature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=javaMetaModel_JClass_strategy)
@settings(max_examples=50)
def test_javametamodel_jclass_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JClass)



@given(instance=javaMetaModel_JClass_strategy)
def test_javametamodel_jclass_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=javaMetaModel_JClass_strategy)
def test_javametamodel_jclass_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=javaMetaModel_JParameter_strategy)
@settings(max_examples=50)
def test_javametamodel_jparameter_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JParameter)



@given(instance=javaMetaModel_JParameter_strategy)
def test_javametamodel_jparameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=JFeature_strategy)
@settings(max_examples=50)
def test_jfeature_instantiation(instance):
    assert isinstance(instance, JFeature)

@given(instance=javaMetaModel_JField_strategy)
@settings(max_examples=50)
def test_javametamodel_jfield_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JField)

@given(instance=javaMetaModel_JMethod_strategy)
@settings(max_examples=50)
def test_javametamodel_jmethod_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JMethod)

@given(instance=javaMetaModel_JElement_strategy)
@settings(max_examples=50)
def test_javametamodel_jelement_instantiation(instance):
    assert isinstance(instance, javaMetaModel_JElement)



@given(instance=javaMetaModel_JElement_strategy)
def test_javametamodel_jelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
