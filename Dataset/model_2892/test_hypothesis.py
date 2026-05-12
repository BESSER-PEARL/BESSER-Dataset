import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    typedef_TypeLanguageBinding,
    typedef_EnumLiteral,
    typedef_TDAnnotationDetail,
    Type,
    typedef_Entity,
    typedef_EnumVal,
    typedef_TypedArray,
    typedef_PrimitiveType,
    typedef_Exception,
    typedef_CSIDatatype,
    typedef_TDDocumentation,
    typedef_Feature,
    typedef_TypeAnnotation,
    typedef_Type,
    typedef_DocumentRoot,
    CSIDatatypeCodes,
    CSIExceptionTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typedef_typelanguagebinding_is_not_abstract():
    assert not inspect.isabstract(typedef_TypeLanguageBinding)


def test_typedef_typelanguagebinding_constructor_exists():
    assert callable(typedef_TypeLanguageBinding.__init__)


def test_typedef_typelanguagebinding_constructor_args():
    sig = inspect.signature(typedef_TypeLanguageBinding.__init__)
    params = list(sig.parameters.keys())
    assert "defaultInitValue" in params, "Missing parameter 'defaultInitValue'"
    assert "langSpecificType" in params, "Missing parameter 'langSpecificType'"
    assert "nullValueLiteral" in params, "Missing parameter 'nullValueLiteral'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "langSpecificNS" in params, "Missing parameter 'langSpecificNS'"

def test_typedef_typelanguagebinding_has_defaultInitValue():
    assert hasattr(typedef_TypeLanguageBinding, "defaultInitValue")
    descriptor = None
    for klass in typedef_TypeLanguageBinding.__mro__:
        if "defaultInitValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultInitValue"]
            break
    assert isinstance(descriptor, property)

def test_typedef_typelanguagebinding_has_langSpecificType():
    assert hasattr(typedef_TypeLanguageBinding, "langSpecificType")
    descriptor = None
    for klass in typedef_TypeLanguageBinding.__mro__:
        if "langSpecificType" in klass.__dict__:
            descriptor = klass.__dict__["langSpecificType"]
            break
    assert isinstance(descriptor, property)

def test_typedef_typelanguagebinding_has_nullValueLiteral():
    assert hasattr(typedef_TypeLanguageBinding, "nullValueLiteral")
    descriptor = None
    for klass in typedef_TypeLanguageBinding.__mro__:
        if "nullValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["nullValueLiteral"]
            break
    assert isinstance(descriptor, property)

def test_typedef_typelanguagebinding_has_lang():
    assert hasattr(typedef_TypeLanguageBinding, "lang")
    descriptor = None
    for klass in typedef_TypeLanguageBinding.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_typedef_typelanguagebinding_has_langSpecificNS():
    assert hasattr(typedef_TypeLanguageBinding, "langSpecificNS")
    descriptor = None
    for klass in typedef_TypeLanguageBinding.__mro__:
        if "langSpecificNS" in klass.__dict__:
            descriptor = klass.__dict__["langSpecificNS"]
            break
    assert isinstance(descriptor, property)



def test_typedef_enumliteral_is_not_abstract():
    assert not inspect.isabstract(typedef_EnumLiteral)


def test_typedef_enumliteral_constructor_exists():
    assert callable(typedef_EnumLiteral.__init__)


def test_typedef_enumliteral_constructor_args():
    sig = inspect.signature(typedef_EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_typedef_enumliteral_has_value():
    assert hasattr(typedef_EnumLiteral, "value")
    descriptor = None
    for klass in typedef_EnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_typedef_enumliteral_has_name():
    assert hasattr(typedef_EnumLiteral, "name")
    descriptor = None
    for klass in typedef_EnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedef_tdannotationdetail_is_not_abstract():
    assert not inspect.isabstract(typedef_TDAnnotationDetail)


def test_typedef_tdannotationdetail_constructor_exists():
    assert callable(typedef_TDAnnotationDetail.__init__)


def test_typedef_tdannotationdetail_constructor_args():
    sig = inspect.signature(typedef_TDAnnotationDetail.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_typedef_tdannotationdetail_has_key():
    assert hasattr(typedef_TDAnnotationDetail, "key")
    descriptor = None
    for klass in typedef_TDAnnotationDetail.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_typedef_tdannotationdetail_has_value():
    assert hasattr(typedef_TDAnnotationDetail, "value")
    descriptor = None
    for klass in typedef_TDAnnotationDetail.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_typedef_entity_is_not_abstract():
    assert not inspect.isabstract(typedef_Entity)


def test_typedef_entity_constructor_exists():
    assert callable(typedef_Entity.__init__)


def test_typedef_entity_constructor_args():
    sig = inspect.signature(typedef_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "versionuid" in params, "Missing parameter 'versionuid'"

def test_typedef_entity_has_versionuid():
    assert hasattr(typedef_Entity, "versionuid")
    descriptor = None
    for klass in typedef_Entity.__mro__:
        if "versionuid" in klass.__dict__:
            descriptor = klass.__dict__["versionuid"]
            break
    assert isinstance(descriptor, property)



def test_typedef_enumval_is_not_abstract():
    assert not inspect.isabstract(typedef_EnumVal)


def test_typedef_enumval_constructor_exists():
    assert callable(typedef_EnumVal.__init__)


def test_typedef_enumval_constructor_args():
    sig = inspect.signature(typedef_EnumVal.__init__)
    params = list(sig.parameters.keys())



def test_typedef_typedarray_is_not_abstract():
    assert not inspect.isabstract(typedef_TypedArray)


def test_typedef_typedarray_constructor_exists():
    assert callable(typedef_TypedArray.__init__)


def test_typedef_typedarray_constructor_args():
    sig = inspect.signature(typedef_TypedArray.__init__)
    params = list(sig.parameters.keys())



def test_typedef_primitivetype_is_not_abstract():
    assert not inspect.isabstract(typedef_PrimitiveType)


def test_typedef_primitivetype_constructor_exists():
    assert callable(typedef_PrimitiveType.__init__)


def test_typedef_primitivetype_constructor_args():
    sig = inspect.signature(typedef_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "typesetName" in params, "Missing parameter 'typesetName'"
    assert "nillable" in params, "Missing parameter 'nillable'"

def test_typedef_primitivetype_has_typesetName():
    assert hasattr(typedef_PrimitiveType, "typesetName")
    descriptor = None
    for klass in typedef_PrimitiveType.__mro__:
        if "typesetName" in klass.__dict__:
            descriptor = klass.__dict__["typesetName"]
            break
    assert isinstance(descriptor, property)

def test_typedef_primitivetype_has_nillable():
    assert hasattr(typedef_PrimitiveType, "nillable")
    descriptor = None
    for klass in typedef_PrimitiveType.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)



def test_typedef_exception_is_not_abstract():
    assert not inspect.isabstract(typedef_Exception)


def test_typedef_exception_constructor_exists():
    assert callable(typedef_Exception.__init__)


def test_typedef_exception_constructor_args():
    sig = inspect.signature(typedef_Exception.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionType" in params, "Missing parameter 'exceptionType'"

def test_typedef_exception_has_exceptionType():
    assert hasattr(typedef_Exception, "exceptionType")
    descriptor = None
    for klass in typedef_Exception.__mro__:
        if "exceptionType" in klass.__dict__:
            descriptor = klass.__dict__["exceptionType"]
            break
    assert isinstance(descriptor, property)



def test_typedef_csidatatype_is_not_abstract():
    assert not inspect.isabstract(typedef_CSIDatatype)


def test_typedef_csidatatype_constructor_exists():
    assert callable(typedef_CSIDatatype.__init__)


def test_typedef_csidatatype_constructor_args():
    sig = inspect.signature(typedef_CSIDatatype.__init__)
    params = list(sig.parameters.keys())
    assert "nillable" in params, "Missing parameter 'nillable'"
    assert "code" in params, "Missing parameter 'code'"

def test_typedef_csidatatype_has_nillable():
    assert hasattr(typedef_CSIDatatype, "nillable")
    descriptor = None
    for klass in typedef_CSIDatatype.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)

def test_typedef_csidatatype_has_code():
    assert hasattr(typedef_CSIDatatype, "code")
    descriptor = None
    for klass in typedef_CSIDatatype.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_typedef_tddocumentation_is_not_abstract():
    assert not inspect.isabstract(typedef_TDDocumentation)


def test_typedef_tddocumentation_constructor_exists():
    assert callable(typedef_TDDocumentation.__init__)


def test_typedef_tddocumentation_constructor_args():
    sig = inspect.signature(typedef_TDDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_typedef_tddocumentation_has_doc():
    assert hasattr(typedef_TDDocumentation, "doc")
    descriptor = None
    for klass in typedef_TDDocumentation.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_typedef_feature_is_not_abstract():
    assert not inspect.isabstract(typedef_Feature)


def test_typedef_feature_constructor_exists():
    assert callable(typedef_Feature.__init__)


def test_typedef_feature_constructor_args():
    sig = inspect.signature(typedef_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typedef_feature_has_name():
    assert hasattr(typedef_Feature, "name")
    descriptor = None
    for klass in typedef_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedef_typeannotation_is_not_abstract():
    assert not inspect.isabstract(typedef_TypeAnnotation)


def test_typedef_typeannotation_constructor_exists():
    assert callable(typedef_TypeAnnotation.__init__)


def test_typedef_typeannotation_constructor_args():
    sig = inspect.signature(typedef_TypeAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_typedef_typeannotation_has_source():
    assert hasattr(typedef_TypeAnnotation, "source")
    descriptor = None
    for klass in typedef_TypeAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_typedef_type_is_not_abstract():
    assert not inspect.isabstract(typedef_Type)


def test_typedef_type_constructor_exists():
    assert callable(typedef_Type.__init__)


def test_typedef_type_constructor_args():
    sig = inspect.signature(typedef_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typedef_type_has_name():
    assert hasattr(typedef_Type, "name")
    descriptor = None
    for klass in typedef_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedef_documentroot_is_not_abstract():
    assert not inspect.isabstract(typedef_DocumentRoot)


def test_typedef_documentroot_constructor_exists():
    assert callable(typedef_DocumentRoot.__init__)


def test_typedef_documentroot_constructor_args():
    sig = inspect.signature(typedef_DocumentRoot.__init__)
    params = list(sig.parameters.keys())

def test_csidatatypecodes_exists():
    # Check that the Enumeration exists
    assert CSIDatatypeCodes is not None

def test_csidatatypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSIDatatypeCodes]
    expected_literals = [
        "CSIByte",
        "CSILong",
        "CSIDouble",
        "CSIBoolean",
        "CSIDate",
        "CSIFloat",
        "CSIString",
        "CSIInteger",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSIDatatypeCodes"

def test_csiexceptiontypes_exists():
    # Check that the Enumeration exists
    assert CSIExceptionTypes is not None

def test_csiexceptiontypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSIExceptionTypes]
    expected_literals = [
        "UNRECOVERABLE",
        "SYSTEM",
        "USER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSIExceptionTypes"


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
typedef_TypeLanguageBinding_strategy = st.builds(
    typedef_TypeLanguageBinding,
    defaultInitValue=
        safe_text,
    langSpecificType=
        safe_text,
    nullValueLiteral=
        safe_text,
    lang=
        safe_text,
    langSpecificNS=
        safe_text
)
typedef_EnumLiteral_strategy = st.builds(
    typedef_EnumLiteral,
    value=
        safe_text,
    name=
        safe_text
)
typedef_TDAnnotationDetail_strategy = st.builds(
    typedef_TDAnnotationDetail,
    key=
        safe_text,
    value=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
typedef_Entity_strategy = st.builds(
    typedef_Entity,
    versionuid=
        st.integers()
)
typedef_EnumVal_strategy = st.builds(
    typedef_EnumVal,
)
typedef_TypedArray_strategy = st.builds(
    typedef_TypedArray,
)
typedef_PrimitiveType_strategy = st.builds(
    typedef_PrimitiveType,
    typesetName=
        safe_text,
    nillable=
        st.booleans()
)
typedef_Exception_strategy = st.builds(
    typedef_Exception,
    exceptionType=
        safe_text
)
typedef_CSIDatatype_strategy = st.builds(
    typedef_CSIDatatype,
    nillable=
        st.booleans(),
    code=
        safe_text
)
typedef_TDDocumentation_strategy = st.builds(
    typedef_TDDocumentation,
    doc=
        safe_text
)
typedef_Feature_strategy = st.builds(
    typedef_Feature,
    name=
        safe_text
)
typedef_TypeAnnotation_strategy = st.builds(
    typedef_TypeAnnotation,
    source=
        safe_text
)
typedef_Type_strategy = st.builds(
    typedef_Type,
    name=
        safe_text
)
typedef_DocumentRoot_strategy = st.builds(
    typedef_DocumentRoot,
)

@given(instance=typedef_TypeLanguageBinding_strategy)
@settings(max_examples=50)
def test_typedef_typelanguagebinding_instantiation(instance):
    assert isinstance(instance, typedef_TypeLanguageBinding)



@given(instance=typedef_TypeLanguageBinding_strategy)
def test_typedef_typelanguagebinding_defaultInitValue_setter(instance):
    original = instance.defaultInitValue
    instance.defaultInitValue = original
    assert instance.defaultInitValue == original



@given(instance=typedef_TypeLanguageBinding_strategy)
def test_typedef_typelanguagebinding_langSpecificType_setter(instance):
    original = instance.langSpecificType
    instance.langSpecificType = original
    assert instance.langSpecificType == original



@given(instance=typedef_TypeLanguageBinding_strategy)
def test_typedef_typelanguagebinding_nullValueLiteral_setter(instance):
    original = instance.nullValueLiteral
    instance.nullValueLiteral = original
    assert instance.nullValueLiteral == original



@given(instance=typedef_TypeLanguageBinding_strategy)
def test_typedef_typelanguagebinding_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=typedef_TypeLanguageBinding_strategy)
def test_typedef_typelanguagebinding_langSpecificNS_setter(instance):
    original = instance.langSpecificNS
    instance.langSpecificNS = original
    assert instance.langSpecificNS == original

@given(instance=typedef_EnumLiteral_strategy)
@settings(max_examples=50)
def test_typedef_enumliteral_instantiation(instance):
    assert isinstance(instance, typedef_EnumLiteral)



@given(instance=typedef_EnumLiteral_strategy)
def test_typedef_enumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=typedef_EnumLiteral_strategy)
def test_typedef_enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef_TDAnnotationDetail_strategy)
@settings(max_examples=50)
def test_typedef_tdannotationdetail_instantiation(instance):
    assert isinstance(instance, typedef_TDAnnotationDetail)



@given(instance=typedef_TDAnnotationDetail_strategy)
def test_typedef_tdannotationdetail_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=typedef_TDAnnotationDetail_strategy)
def test_typedef_tdannotationdetail_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=typedef_Entity_strategy)
@settings(max_examples=50)
def test_typedef_entity_instantiation(instance):
    assert isinstance(instance, typedef_Entity)



@given(instance=typedef_Entity_strategy)
def test_typedef_entity_versionuid_setter(instance):
    original = instance.versionuid
    instance.versionuid = original
    assert instance.versionuid == original

@given(instance=typedef_EnumVal_strategy)
@settings(max_examples=50)
def test_typedef_enumval_instantiation(instance):
    assert isinstance(instance, typedef_EnumVal)

@given(instance=typedef_TypedArray_strategy)
@settings(max_examples=50)
def test_typedef_typedarray_instantiation(instance):
    assert isinstance(instance, typedef_TypedArray)

@given(instance=typedef_PrimitiveType_strategy)
@settings(max_examples=50)
def test_typedef_primitivetype_instantiation(instance):
    assert isinstance(instance, typedef_PrimitiveType)



@given(instance=typedef_PrimitiveType_strategy)
def test_typedef_primitivetype_typesetName_setter(instance):
    original = instance.typesetName
    instance.typesetName = original
    assert instance.typesetName == original



@given(instance=typedef_PrimitiveType_strategy)
def test_typedef_primitivetype_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original

@given(instance=typedef_Exception_strategy)
@settings(max_examples=50)
def test_typedef_exception_instantiation(instance):
    assert isinstance(instance, typedef_Exception)



@given(instance=typedef_Exception_strategy)
def test_typedef_exception_exceptionType_setter(instance):
    original = instance.exceptionType
    instance.exceptionType = original
    assert instance.exceptionType == original

@given(instance=typedef_CSIDatatype_strategy)
@settings(max_examples=50)
def test_typedef_csidatatype_instantiation(instance):
    assert isinstance(instance, typedef_CSIDatatype)



@given(instance=typedef_CSIDatatype_strategy)
def test_typedef_csidatatype_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original



@given(instance=typedef_CSIDatatype_strategy)
def test_typedef_csidatatype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=typedef_TDDocumentation_strategy)
@settings(max_examples=50)
def test_typedef_tddocumentation_instantiation(instance):
    assert isinstance(instance, typedef_TDDocumentation)



@given(instance=typedef_TDDocumentation_strategy)
def test_typedef_tddocumentation_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=typedef_Feature_strategy)
@settings(max_examples=50)
def test_typedef_feature_instantiation(instance):
    assert isinstance(instance, typedef_Feature)



@given(instance=typedef_Feature_strategy)
def test_typedef_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef_TypeAnnotation_strategy)
@settings(max_examples=50)
def test_typedef_typeannotation_instantiation(instance):
    assert isinstance(instance, typedef_TypeAnnotation)



@given(instance=typedef_TypeAnnotation_strategy)
def test_typedef_typeannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=typedef_Type_strategy)
@settings(max_examples=50)
def test_typedef_type_instantiation(instance):
    assert isinstance(instance, typedef_Type)



@given(instance=typedef_Type_strategy)
def test_typedef_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef_DocumentRoot_strategy)
@settings(max_examples=50)
def test_typedef_documentroot_instantiation(instance):
    assert isinstance(instance, typedef_DocumentRoot)
