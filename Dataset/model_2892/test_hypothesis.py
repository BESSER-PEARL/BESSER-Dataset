import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    typedef::TypeLanguageBinding,
    typedef::EnumLiteral,
    typedef::TDAnnotationDetail,
    Type,
    typedef::EnumVal,
    typedef::Entity,
    typedef::PrimitiveType,
    typedef::Exception,
    typedef::TypedArray,
    typedef::CSIDatatype,
    typedef::TDDocumentation,
    typedef::Feature,
    typedef::TypeAnnotation,
    typedef::Type,
    typedef::DocumentRoot,
    CSIExceptionTypes,
    CSIDatatypeCodes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typedef::typelanguagebinding_is_not_abstract():
    assert not inspect.isabstract(typedef::TypeLanguageBinding)


def test_typedef::typelanguagebinding_constructor_exists():
    assert callable(typedef::TypeLanguageBinding.__init__)


def test_typedef::typelanguagebinding_constructor_args():
    sig = inspect.signature(typedef::TypeLanguageBinding.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"
    assert "langSpecificType" in params, "Missing parameter 'langSpecificType'"
    assert "langSpecificNS" in params, "Missing parameter 'langSpecificNS'"
    assert "defaultInitValue" in params, "Missing parameter 'defaultInitValue'"
    assert "nullValueLiteral" in params, "Missing parameter 'nullValueLiteral'"

def test_typedef::typelanguagebinding_has_lang():
    assert hasattr(typedef::TypeLanguageBinding, "lang")
    descriptor = None
    for klass in typedef::TypeLanguageBinding.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_typedef::typelanguagebinding_has_langSpecificType():
    assert hasattr(typedef::TypeLanguageBinding, "langSpecificType")
    descriptor = None
    for klass in typedef::TypeLanguageBinding.__mro__:
        if "langSpecificType" in klass.__dict__:
            descriptor = klass.__dict__["langSpecificType"]
            break
    assert isinstance(descriptor, property)

def test_typedef::typelanguagebinding_has_langSpecificNS():
    assert hasattr(typedef::TypeLanguageBinding, "langSpecificNS")
    descriptor = None
    for klass in typedef::TypeLanguageBinding.__mro__:
        if "langSpecificNS" in klass.__dict__:
            descriptor = klass.__dict__["langSpecificNS"]
            break
    assert isinstance(descriptor, property)

def test_typedef::typelanguagebinding_has_defaultInitValue():
    assert hasattr(typedef::TypeLanguageBinding, "defaultInitValue")
    descriptor = None
    for klass in typedef::TypeLanguageBinding.__mro__:
        if "defaultInitValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultInitValue"]
            break
    assert isinstance(descriptor, property)

def test_typedef::typelanguagebinding_has_nullValueLiteral():
    assert hasattr(typedef::TypeLanguageBinding, "nullValueLiteral")
    descriptor = None
    for klass in typedef::TypeLanguageBinding.__mro__:
        if "nullValueLiteral" in klass.__dict__:
            descriptor = klass.__dict__["nullValueLiteral"]
            break
    assert isinstance(descriptor, property)



def test_typedef::enumliteral_is_not_abstract():
    assert not inspect.isabstract(typedef::EnumLiteral)


def test_typedef::enumliteral_constructor_exists():
    assert callable(typedef::EnumLiteral.__init__)


def test_typedef::enumliteral_constructor_args():
    sig = inspect.signature(typedef::EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_typedef::enumliteral_has_name():
    assert hasattr(typedef::EnumLiteral, "name")
    descriptor = None
    for klass in typedef::EnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_typedef::enumliteral_has_value():
    assert hasattr(typedef::EnumLiteral, "value")
    descriptor = None
    for klass in typedef::EnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_typedef::tdannotationdetail_is_not_abstract():
    assert not inspect.isabstract(typedef::TDAnnotationDetail)


def test_typedef::tdannotationdetail_constructor_exists():
    assert callable(typedef::TDAnnotationDetail.__init__)


def test_typedef::tdannotationdetail_constructor_args():
    sig = inspect.signature(typedef::TDAnnotationDetail.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_typedef::tdannotationdetail_has_key():
    assert hasattr(typedef::TDAnnotationDetail, "key")
    descriptor = None
    for klass in typedef::TDAnnotationDetail.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_typedef::tdannotationdetail_has_value():
    assert hasattr(typedef::TDAnnotationDetail, "value")
    descriptor = None
    for klass in typedef::TDAnnotationDetail.__mro__:
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



def test_typedef::enumval_is_not_abstract():
    assert not inspect.isabstract(typedef::EnumVal)


def test_typedef::enumval_constructor_exists():
    assert callable(typedef::EnumVal.__init__)


def test_typedef::enumval_constructor_args():
    sig = inspect.signature(typedef::EnumVal.__init__)
    params = list(sig.parameters.keys())



def test_typedef::entity_is_not_abstract():
    assert not inspect.isabstract(typedef::Entity)


def test_typedef::entity_constructor_exists():
    assert callable(typedef::Entity.__init__)


def test_typedef::entity_constructor_args():
    sig = inspect.signature(typedef::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "versionuid" in params, "Missing parameter 'versionuid'"

def test_typedef::entity_has_versionuid():
    assert hasattr(typedef::Entity, "versionuid")
    descriptor = None
    for klass in typedef::Entity.__mro__:
        if "versionuid" in klass.__dict__:
            descriptor = klass.__dict__["versionuid"]
            break
    assert isinstance(descriptor, property)



def test_typedef::primitivetype_is_not_abstract():
    assert not inspect.isabstract(typedef::PrimitiveType)


def test_typedef::primitivetype_constructor_exists():
    assert callable(typedef::PrimitiveType.__init__)


def test_typedef::primitivetype_constructor_args():
    sig = inspect.signature(typedef::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "typesetName" in params, "Missing parameter 'typesetName'"
    assert "nillable" in params, "Missing parameter 'nillable'"

def test_typedef::primitivetype_has_typesetName():
    assert hasattr(typedef::PrimitiveType, "typesetName")
    descriptor = None
    for klass in typedef::PrimitiveType.__mro__:
        if "typesetName" in klass.__dict__:
            descriptor = klass.__dict__["typesetName"]
            break
    assert isinstance(descriptor, property)

def test_typedef::primitivetype_has_nillable():
    assert hasattr(typedef::PrimitiveType, "nillable")
    descriptor = None
    for klass in typedef::PrimitiveType.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)



def test_typedef::exception_is_not_abstract():
    assert not inspect.isabstract(typedef::Exception)


def test_typedef::exception_constructor_exists():
    assert callable(typedef::Exception.__init__)


def test_typedef::exception_constructor_args():
    sig = inspect.signature(typedef::Exception.__init__)
    params = list(sig.parameters.keys())
    assert "exceptionType" in params, "Missing parameter 'exceptionType'"

def test_typedef::exception_has_exceptionType():
    assert hasattr(typedef::Exception, "exceptionType")
    descriptor = None
    for klass in typedef::Exception.__mro__:
        if "exceptionType" in klass.__dict__:
            descriptor = klass.__dict__["exceptionType"]
            break
    assert isinstance(descriptor, property)



def test_typedef::typedarray_is_not_abstract():
    assert not inspect.isabstract(typedef::TypedArray)


def test_typedef::typedarray_constructor_exists():
    assert callable(typedef::TypedArray.__init__)


def test_typedef::typedarray_constructor_args():
    sig = inspect.signature(typedef::TypedArray.__init__)
    params = list(sig.parameters.keys())



def test_typedef::csidatatype_is_not_abstract():
    assert not inspect.isabstract(typedef::CSIDatatype)


def test_typedef::csidatatype_constructor_exists():
    assert callable(typedef::CSIDatatype.__init__)


def test_typedef::csidatatype_constructor_args():
    sig = inspect.signature(typedef::CSIDatatype.__init__)
    params = list(sig.parameters.keys())
    assert "nillable" in params, "Missing parameter 'nillable'"
    assert "code" in params, "Missing parameter 'code'"

def test_typedef::csidatatype_has_nillable():
    assert hasattr(typedef::CSIDatatype, "nillable")
    descriptor = None
    for klass in typedef::CSIDatatype.__mro__:
        if "nillable" in klass.__dict__:
            descriptor = klass.__dict__["nillable"]
            break
    assert isinstance(descriptor, property)

def test_typedef::csidatatype_has_code():
    assert hasattr(typedef::CSIDatatype, "code")
    descriptor = None
    for klass in typedef::CSIDatatype.__mro__:
        if "code" in klass.__dict__:
            descriptor = klass.__dict__["code"]
            break
    assert isinstance(descriptor, property)



def test_typedef::tddocumentation_is_not_abstract():
    assert not inspect.isabstract(typedef::TDDocumentation)


def test_typedef::tddocumentation_constructor_exists():
    assert callable(typedef::TDDocumentation.__init__)


def test_typedef::tddocumentation_constructor_args():
    sig = inspect.signature(typedef::TDDocumentation.__init__)
    params = list(sig.parameters.keys())
    assert "doc" in params, "Missing parameter 'doc'"

def test_typedef::tddocumentation_has_doc():
    assert hasattr(typedef::TDDocumentation, "doc")
    descriptor = None
    for klass in typedef::TDDocumentation.__mro__:
        if "doc" in klass.__dict__:
            descriptor = klass.__dict__["doc"]
            break
    assert isinstance(descriptor, property)



def test_typedef::feature_is_not_abstract():
    assert not inspect.isabstract(typedef::Feature)


def test_typedef::feature_constructor_exists():
    assert callable(typedef::Feature.__init__)


def test_typedef::feature_constructor_args():
    sig = inspect.signature(typedef::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typedef::feature_has_name():
    assert hasattr(typedef::Feature, "name")
    descriptor = None
    for klass in typedef::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedef::typeannotation_is_not_abstract():
    assert not inspect.isabstract(typedef::TypeAnnotation)


def test_typedef::typeannotation_constructor_exists():
    assert callable(typedef::TypeAnnotation.__init__)


def test_typedef::typeannotation_constructor_args():
    sig = inspect.signature(typedef::TypeAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_typedef::typeannotation_has_source():
    assert hasattr(typedef::TypeAnnotation, "source")
    descriptor = None
    for klass in typedef::TypeAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_typedef::type_is_not_abstract():
    assert not inspect.isabstract(typedef::Type)


def test_typedef::type_constructor_exists():
    assert callable(typedef::Type.__init__)


def test_typedef::type_constructor_args():
    sig = inspect.signature(typedef::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_typedef::type_has_name():
    assert hasattr(typedef::Type, "name")
    descriptor = None
    for klass in typedef::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typedef::documentroot_is_not_abstract():
    assert not inspect.isabstract(typedef::DocumentRoot)


def test_typedef::documentroot_constructor_exists():
    assert callable(typedef::DocumentRoot.__init__)


def test_typedef::documentroot_constructor_args():
    sig = inspect.signature(typedef::DocumentRoot.__init__)
    params = list(sig.parameters.keys())

def test_csiexceptiontypes_exists():
    # Check that the Enumeration exists
    assert CSIExceptionTypes is not None

def test_csiexceptiontypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSIExceptionTypes]
    expected_literals = [
        "USER",
        "UNRECOVERABLE",
        "SYSTEM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSIExceptionTypes"

def test_csidatatypecodes_exists():
    # Check that the Enumeration exists
    assert CSIDatatypeCodes is not None

def test_csidatatypecodes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSIDatatypeCodes]
    expected_literals = [
        "CSIBoolean",
        "CSIInteger",
        "CSIByte",
        "CSIString",
        "CSIDate",
        "CSILong",
        "CSIDouble",
        "CSIFloat",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSIDatatypeCodes"


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
typedef::TypeLanguageBinding_strategy = st.builds(
    typedef::TypeLanguageBinding,
    lang=
        safe_text,
    langSpecificType=
        safe_text,
    langSpecificNS=
        safe_text,
    defaultInitValue=
        safe_text,
    nullValueLiteral=
        safe_text
)
typedef::EnumLiteral_strategy = st.builds(
    typedef::EnumLiteral,
    name=
        safe_text,
    value=
        safe_text
)
typedef::TDAnnotationDetail_strategy = st.builds(
    typedef::TDAnnotationDetail,
    key=
        safe_text,
    value=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
typedef::EnumVal_strategy = st.builds(
    typedef::EnumVal,
)
typedef::Entity_strategy = st.builds(
    typedef::Entity,
    versionuid=
        st.integers()
)
typedef::PrimitiveType_strategy = st.builds(
    typedef::PrimitiveType,
    typesetName=
        safe_text,
    nillable=
        st.booleans()
)
typedef::Exception_strategy = st.builds(
    typedef::Exception,
    exceptionType=
        safe_text
)
typedef::TypedArray_strategy = st.builds(
    typedef::TypedArray,
)
typedef::CSIDatatype_strategy = st.builds(
    typedef::CSIDatatype,
    nillable=
        st.booleans(),
    code=
        safe_text
)
typedef::TDDocumentation_strategy = st.builds(
    typedef::TDDocumentation,
    doc=
        safe_text
)
typedef::Feature_strategy = st.builds(
    typedef::Feature,
    name=
        safe_text
)
typedef::TypeAnnotation_strategy = st.builds(
    typedef::TypeAnnotation,
    source=
        safe_text
)
typedef::Type_strategy = st.builds(
    typedef::Type,
    name=
        safe_text
)
typedef::DocumentRoot_strategy = st.builds(
    typedef::DocumentRoot,
)

@given(instance=typedef::TypeLanguageBinding_strategy)
@settings(max_examples=50)
def test_typedef::typelanguagebinding_instantiation(instance):
    assert isinstance(instance, typedef::TypeLanguageBinding)

@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_langSpecificType_type(instance):
    assert isinstance(instance.langSpecificType, str)


@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_langSpecificType_setter(instance):
    original = instance.langSpecificType
    instance.langSpecificType = original
    assert instance.langSpecificType == original

@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_langSpecificNS_type(instance):
    assert isinstance(instance.langSpecificNS, str)


@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_langSpecificNS_setter(instance):
    original = instance.langSpecificNS
    instance.langSpecificNS = original
    assert instance.langSpecificNS == original

@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_defaultInitValue_type(instance):
    assert isinstance(instance.defaultInitValue, str)


@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_defaultInitValue_setter(instance):
    original = instance.defaultInitValue
    instance.defaultInitValue = original
    assert instance.defaultInitValue == original

@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_nullValueLiteral_type(instance):
    assert isinstance(instance.nullValueLiteral, str)


@given(instance=typedef::TypeLanguageBinding_strategy)
def test_typedef::typelanguagebinding_nullValueLiteral_setter(instance):
    original = instance.nullValueLiteral
    instance.nullValueLiteral = original
    assert instance.nullValueLiteral == original

@given(instance=typedef::EnumLiteral_strategy)
@settings(max_examples=50)
def test_typedef::enumliteral_instantiation(instance):
    assert isinstance(instance, typedef::EnumLiteral)

@given(instance=typedef::EnumLiteral_strategy)
def test_typedef::enumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typedef::EnumLiteral_strategy)
def test_typedef::enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef::EnumLiteral_strategy)
def test_typedef::enumliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=typedef::EnumLiteral_strategy)
def test_typedef::enumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=typedef::TDAnnotationDetail_strategy)
@settings(max_examples=50)
def test_typedef::tdannotationdetail_instantiation(instance):
    assert isinstance(instance, typedef::TDAnnotationDetail)

@given(instance=typedef::TDAnnotationDetail_strategy)
def test_typedef::tdannotationdetail_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=typedef::TDAnnotationDetail_strategy)
def test_typedef::tdannotationdetail_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=typedef::TDAnnotationDetail_strategy)
def test_typedef::tdannotationdetail_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=typedef::TDAnnotationDetail_strategy)
def test_typedef::tdannotationdetail_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=typedef::EnumVal_strategy)
@settings(max_examples=50)
def test_typedef::enumval_instantiation(instance):
    assert isinstance(instance, typedef::EnumVal)

@given(instance=typedef::Entity_strategy)
@settings(max_examples=50)
def test_typedef::entity_instantiation(instance):
    assert isinstance(instance, typedef::Entity)

@given(instance=typedef::Entity_strategy)
def test_typedef::entity_versionuid_type(instance):
    assert isinstance(instance.versionuid, int)


@given(instance=typedef::Entity_strategy)
def test_typedef::entity_versionuid_setter(instance):
    original = instance.versionuid
    instance.versionuid = original
    assert instance.versionuid == original

@given(instance=typedef::PrimitiveType_strategy)
@settings(max_examples=50)
def test_typedef::primitivetype_instantiation(instance):
    assert isinstance(instance, typedef::PrimitiveType)

@given(instance=typedef::PrimitiveType_strategy)
def test_typedef::primitivetype_typesetName_type(instance):
    assert isinstance(instance.typesetName, str)


@given(instance=typedef::PrimitiveType_strategy)
def test_typedef::primitivetype_typesetName_setter(instance):
    original = instance.typesetName
    instance.typesetName = original
    assert instance.typesetName == original

@given(instance=typedef::PrimitiveType_strategy)
def test_typedef::primitivetype_nillable_type(instance):
    assert isinstance(instance.nillable, bool)


@given(instance=typedef::PrimitiveType_strategy)
def test_typedef::primitivetype_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original

@given(instance=typedef::Exception_strategy)
@settings(max_examples=50)
def test_typedef::exception_instantiation(instance):
    assert isinstance(instance, typedef::Exception)

@given(instance=typedef::Exception_strategy)
def test_typedef::exception_exceptionType_type(instance):
    assert isinstance(instance.exceptionType, str)


@given(instance=typedef::Exception_strategy)
def test_typedef::exception_exceptionType_setter(instance):
    original = instance.exceptionType
    instance.exceptionType = original
    assert instance.exceptionType == original

@given(instance=typedef::TypedArray_strategy)
@settings(max_examples=50)
def test_typedef::typedarray_instantiation(instance):
    assert isinstance(instance, typedef::TypedArray)

@given(instance=typedef::CSIDatatype_strategy)
@settings(max_examples=50)
def test_typedef::csidatatype_instantiation(instance):
    assert isinstance(instance, typedef::CSIDatatype)

@given(instance=typedef::CSIDatatype_strategy)
def test_typedef::csidatatype_nillable_type(instance):
    assert isinstance(instance.nillable, bool)


@given(instance=typedef::CSIDatatype_strategy)
def test_typedef::csidatatype_nillable_setter(instance):
    original = instance.nillable
    instance.nillable = original
    assert instance.nillable == original

@given(instance=typedef::CSIDatatype_strategy)
def test_typedef::csidatatype_code_type(instance):
    assert isinstance(instance.code, str)


@given(instance=typedef::CSIDatatype_strategy)
def test_typedef::csidatatype_code_setter(instance):
    original = instance.code
    instance.code = original
    assert instance.code == original

@given(instance=typedef::TDDocumentation_strategy)
@settings(max_examples=50)
def test_typedef::tddocumentation_instantiation(instance):
    assert isinstance(instance, typedef::TDDocumentation)

@given(instance=typedef::TDDocumentation_strategy)
def test_typedef::tddocumentation_doc_type(instance):
    assert isinstance(instance.doc, str)


@given(instance=typedef::TDDocumentation_strategy)
def test_typedef::tddocumentation_doc_setter(instance):
    original = instance.doc
    instance.doc = original
    assert instance.doc == original

@given(instance=typedef::Feature_strategy)
@settings(max_examples=50)
def test_typedef::feature_instantiation(instance):
    assert isinstance(instance, typedef::Feature)

@given(instance=typedef::Feature_strategy)
def test_typedef::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typedef::Feature_strategy)
def test_typedef::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef::TypeAnnotation_strategy)
@settings(max_examples=50)
def test_typedef::typeannotation_instantiation(instance):
    assert isinstance(instance, typedef::TypeAnnotation)

@given(instance=typedef::TypeAnnotation_strategy)
def test_typedef::typeannotation_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=typedef::TypeAnnotation_strategy)
def test_typedef::typeannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=typedef::Type_strategy)
@settings(max_examples=50)
def test_typedef::type_instantiation(instance):
    assert isinstance(instance, typedef::Type)

@given(instance=typedef::Type_strategy)
def test_typedef::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=typedef::Type_strategy)
def test_typedef::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=typedef::DocumentRoot_strategy)
@settings(max_examples=50)
def test_typedef::documentroot_instantiation(instance):
    assert isinstance(instance, typedef::DocumentRoot)
