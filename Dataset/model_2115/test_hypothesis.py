import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xtextTest::ReplacePatterns,
    xtextTest::Inner,
    xtextTest::MyTokens,
    xtextTest::CodeCall,
    xtextTest::Import,
    xtextTest::After,
    xtextTest::Before,
    xtextTest::Generator,
    xtextTest::Element,
    xtextTest::Tokens,
    xtextTest::Input,
    xtextTest::EmfTest,
    xtextTest::XtextTest,
    xtextTest::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xtexttest::replacepatterns_is_not_abstract():
    assert not inspect.isabstract(xtextTest::ReplacePatterns)


def test_xtexttest::replacepatterns_constructor_exists():
    assert callable(xtextTest::ReplacePatterns.__init__)


def test_xtexttest::replacepatterns_constructor_args():
    sig = inspect.signature(xtextTest::ReplacePatterns.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"
    assert "replace" in params, "Missing parameter 'replace'"

def test_xtexttest::replacepatterns_has_regex():
    assert hasattr(xtextTest::ReplacePatterns, "regex")
    descriptor = None
    for klass in xtextTest::ReplacePatterns.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::replacepatterns_has_replace():
    assert hasattr(xtextTest::ReplacePatterns, "replace")
    descriptor = None
    for klass in xtextTest::ReplacePatterns.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::inner_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Inner)


def test_xtexttest::inner_constructor_exists():
    assert callable(xtextTest::Inner.__init__)


def test_xtexttest::inner_constructor_args():
    sig = inspect.signature(xtextTest::Inner.__init__)
    params = list(sig.parameters.keys())
    assert "isNull" in params, "Missing parameter 'isNull'"
    assert "value" in params, "Missing parameter 'value'"
    assert "assignAsBool" in params, "Missing parameter 'assignAsBool'"
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "isEmpty" in params, "Missing parameter 'isEmpty'"
    assert "assignAsData" in params, "Missing parameter 'assignAsData'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"

def test_xtexttest::inner_has_isNull():
    assert hasattr(xtextTest::Inner, "isNull")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "isNull" in klass.__dict__:
            descriptor = klass.__dict__["isNull"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_value():
    assert hasattr(xtextTest::Inner, "value")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_assignAsBool():
    assert hasattr(xtextTest::Inner, "assignAsBool")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "assignAsBool" in klass.__dict__:
            descriptor = klass.__dict__["assignAsBool"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_parameter():
    assert hasattr(xtextTest::Inner, "parameter")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_isEmpty():
    assert hasattr(xtextTest::Inner, "isEmpty")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "isEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isEmpty"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_assignAsData():
    assert hasattr(xtextTest::Inner, "assignAsData")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "assignAsData" in klass.__dict__:
            descriptor = klass.__dict__["assignAsData"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::inner_has_isNotNull():
    assert hasattr(xtextTest::Inner, "isNotNull")
    descriptor = None
    for klass in xtextTest::Inner.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::mytokens_is_not_abstract():
    assert not inspect.isabstract(xtextTest::MyTokens)


def test_xtexttest::mytokens_constructor_exists():
    assert callable(xtextTest::MyTokens.__init__)


def test_xtexttest::mytokens_constructor_args():
    sig = inspect.signature(xtextTest::MyTokens.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "token" in params, "Missing parameter 'token'"
    assert "string" in params, "Missing parameter 'string'"

def test_xtexttest::mytokens_has_count():
    assert hasattr(xtextTest::MyTokens, "count")
    descriptor = None
    for klass in xtextTest::MyTokens.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::mytokens_has_token():
    assert hasattr(xtextTest::MyTokens, "token")
    descriptor = None
    for klass in xtextTest::MyTokens.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::mytokens_has_string():
    assert hasattr(xtextTest::MyTokens, "string")
    descriptor = None
    for klass in xtextTest::MyTokens.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::codecall_is_not_abstract():
    assert not inspect.isabstract(xtextTest::CodeCall)


def test_xtexttest::codecall_constructor_exists():
    assert callable(xtextTest::CodeCall.__init__)


def test_xtexttest::codecall_constructor_args():
    sig = inspect.signature(xtextTest::CodeCall.__init__)
    params = list(sig.parameters.keys())
    assert "myclass" in params, "Missing parameter 'myclass'"
    assert "method" in params, "Missing parameter 'method'"
    assert "params" in params, "Missing parameter 'params'"

def test_xtexttest::codecall_has_myclass():
    assert hasattr(xtextTest::CodeCall, "myclass")
    descriptor = None
    for klass in xtextTest::CodeCall.__mro__:
        if "myclass" in klass.__dict__:
            descriptor = klass.__dict__["myclass"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::codecall_has_method():
    assert hasattr(xtextTest::CodeCall, "method")
    descriptor = None
    for klass in xtextTest::CodeCall.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::codecall_has_params():
    assert hasattr(xtextTest::CodeCall, "params")
    descriptor = None
    for klass in xtextTest::CodeCall.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::import_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Import)


def test_xtexttest::import_constructor_exists():
    assert callable(xtextTest::Import.__init__)


def test_xtexttest::import_constructor_args():
    sig = inspect.signature(xtextTest::Import.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "id" in params, "Missing parameter 'id'"

def test_xtexttest::import_has_alias():
    assert hasattr(xtextTest::Import, "alias")
    descriptor = None
    for klass in xtextTest::Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::import_has_id():
    assert hasattr(xtextTest::Import, "id")
    descriptor = None
    for klass in xtextTest::Import.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::after_is_not_abstract():
    assert not inspect.isabstract(xtextTest::After)


def test_xtexttest::after_constructor_exists():
    assert callable(xtextTest::After.__init__)


def test_xtexttest::after_constructor_args():
    sig = inspect.signature(xtextTest::After.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest::before_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Before)


def test_xtexttest::before_constructor_exists():
    assert callable(xtextTest::Before.__init__)


def test_xtexttest::before_constructor_args():
    sig = inspect.signature(xtextTest::Before.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest::generator_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Generator)


def test_xtexttest::generator_constructor_exists():
    assert callable(xtextTest::Generator.__init__)


def test_xtexttest::generator_constructor_args():
    sig = inspect.signature(xtextTest::Generator.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "patternFile" in params, "Missing parameter 'patternFile'"
    assert "expected" in params, "Missing parameter 'expected'"
    assert "exception" in params, "Missing parameter 'exception'"
    assert "isSameAsInputFile" in params, "Missing parameter 'isSameAsInputFile'"

def test_xtexttest::generator_has_output():
    assert hasattr(xtextTest::Generator, "output")
    descriptor = None
    for klass in xtextTest::Generator.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::generator_has_patternFile():
    assert hasattr(xtextTest::Generator, "patternFile")
    descriptor = None
    for klass in xtextTest::Generator.__mro__:
        if "patternFile" in klass.__dict__:
            descriptor = klass.__dict__["patternFile"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::generator_has_expected():
    assert hasattr(xtextTest::Generator, "expected")
    descriptor = None
    for klass in xtextTest::Generator.__mro__:
        if "expected" in klass.__dict__:
            descriptor = klass.__dict__["expected"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::generator_has_exception():
    assert hasattr(xtextTest::Generator, "exception")
    descriptor = None
    for klass in xtextTest::Generator.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::generator_has_isSameAsInputFile():
    assert hasattr(xtextTest::Generator, "isSameAsInputFile")
    descriptor = None
    for klass in xtextTest::Generator.__mro__:
        if "isSameAsInputFile" in klass.__dict__:
            descriptor = klass.__dict__["isSameAsInputFile"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::element_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Element)


def test_xtexttest::element_constructor_exists():
    assert callable(xtextTest::Element.__init__)


def test_xtexttest::element_constructor_args():
    sig = inspect.signature(xtextTest::Element.__init__)
    params = list(sig.parameters.keys())
    assert "importing" in params, "Missing parameter 'importing'"
    assert "name" in params, "Missing parameter 'name'"

def test_xtexttest::element_has_importing():
    assert hasattr(xtextTest::Element, "importing")
    descriptor = None
    for klass in xtextTest::Element.__mro__:
        if "importing" in klass.__dict__:
            descriptor = klass.__dict__["importing"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::element_has_name():
    assert hasattr(xtextTest::Element, "name")
    descriptor = None
    for klass in xtextTest::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::tokens_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Tokens)


def test_xtexttest::tokens_constructor_exists():
    assert callable(xtextTest::Tokens.__init__)


def test_xtexttest::tokens_constructor_args():
    sig = inspect.signature(xtextTest::Tokens.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest::input_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Input)


def test_xtexttest::input_constructor_exists():
    assert callable(xtextTest::Input.__init__)


def test_xtexttest::input_constructor_args():
    sig = inspect.signature(xtextTest::Input.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "file" in params, "Missing parameter 'file'"

def test_xtexttest::input_has_text():
    assert hasattr(xtextTest::Input, "text")
    descriptor = None
    for klass in xtextTest::Input.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::input_has_file():
    assert hasattr(xtextTest::Input, "file")
    descriptor = None
    for klass in xtextTest::Input.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::emftest_is_not_abstract():
    assert not inspect.isabstract(xtextTest::EmfTest)


def test_xtexttest::emftest_constructor_exists():
    assert callable(xtextTest::EmfTest.__init__)


def test_xtexttest::emftest_constructor_args():
    sig = inspect.signature(xtextTest::EmfTest.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"
    assert "mydefault" in params, "Missing parameter 'mydefault'"
    assert "file" in params, "Missing parameter 'file'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"

def test_xtexttest::emftest_has_package():
    assert hasattr(xtextTest::EmfTest, "package")
    descriptor = None
    for klass in xtextTest::EmfTest.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::emftest_has_mydefault():
    assert hasattr(xtextTest::EmfTest, "mydefault")
    descriptor = None
    for klass in xtextTest::EmfTest.__mro__:
        if "mydefault" in klass.__dict__:
            descriptor = klass.__dict__["mydefault"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::emftest_has_file():
    assert hasattr(xtextTest::EmfTest, "file")
    descriptor = None
    for klass in xtextTest::EmfTest.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::emftest_has_timeOut():
    assert hasattr(xtextTest::EmfTest, "timeOut")
    descriptor = None
    for klass in xtextTest::EmfTest.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::xtexttest_is_not_abstract():
    assert not inspect.isabstract(xtextTest::XtextTest)


def test_xtexttest::xtexttest_constructor_exists():
    assert callable(xtextTest::XtextTest.__init__)


def test_xtexttest::xtexttest_constructor_args():
    sig = inspect.signature(xtextTest::XtextTest.__init__)
    params = list(sig.parameters.keys())
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "package" in params, "Missing parameter 'package'"
    assert "imports" in params, "Missing parameter 'imports'"

def test_xtexttest::xtexttest_has_boolean():
    assert hasattr(xtextTest::XtextTest, "boolean")
    descriptor = None
    for klass in xtextTest::XtextTest.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::xtexttest_has_timeOut():
    assert hasattr(xtextTest::XtextTest, "timeOut")
    descriptor = None
    for klass in xtextTest::XtextTest.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::xtexttest_has_lang():
    assert hasattr(xtextTest::XtextTest, "lang")
    descriptor = None
    for klass in xtextTest::XtextTest.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::xtexttest_has_package():
    assert hasattr(xtextTest::XtextTest, "package")
    descriptor = None
    for klass in xtextTest::XtextTest.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest::xtexttest_has_imports():
    assert hasattr(xtextTest::XtextTest, "imports")
    descriptor = None
    for klass in xtextTest::XtextTest.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest::model_is_not_abstract():
    assert not inspect.isabstract(xtextTest::Model)


def test_xtexttest::model_constructor_exists():
    assert callable(xtextTest::Model.__init__)


def test_xtexttest::model_constructor_args():
    sig = inspect.signature(xtextTest::Model.__init__)
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
xtextTest::ReplacePatterns_strategy = st.builds(
    xtextTest::ReplacePatterns,
    regex=
        safe_text,
    replace=
        safe_text
)
xtextTest::Inner_strategy = st.builds(
    xtextTest::Inner,
    isNull=
        st.booleans(),
    value=
        safe_text,
    assignAsBool=
        safe_text,
    parameter=
        safe_text,
    isEmpty=
        st.booleans(),
    assignAsData=
        safe_text,
    isNotNull=
        st.booleans()
)
xtextTest::MyTokens_strategy = st.builds(
    xtextTest::MyTokens,
    count=
        st.integers(),
    token=
        safe_text,
    string=
        safe_text
)
xtextTest::CodeCall_strategy = st.builds(
    xtextTest::CodeCall,
    myclass=
        safe_text,
    method=
        safe_text,
    params=
        safe_text
)
xtextTest::Import_strategy = st.builds(
    xtextTest::Import,
    alias=
        safe_text,
    id=
        safe_text
)
xtextTest::After_strategy = st.builds(
    xtextTest::After,
)
xtextTest::Before_strategy = st.builds(
    xtextTest::Before,
)
xtextTest::Generator_strategy = st.builds(
    xtextTest::Generator,
    output=
        safe_text,
    patternFile=
        safe_text,
    expected=
        safe_text,
    exception=
        safe_text,
    isSameAsInputFile=
        st.booleans()
)
xtextTest::Element_strategy = st.builds(
    xtextTest::Element,
    importing=
        safe_text,
    name=
        safe_text
)
xtextTest::Tokens_strategy = st.builds(
    xtextTest::Tokens,
)
xtextTest::Input_strategy = st.builds(
    xtextTest::Input,
    text=
        safe_text,
    file=
        safe_text
)
xtextTest::EmfTest_strategy = st.builds(
    xtextTest::EmfTest,
    package=
        safe_text,
    mydefault=
        safe_text,
    file=
        safe_text,
    timeOut=
        st.integers()
)
xtextTest::XtextTest_strategy = st.builds(
    xtextTest::XtextTest,
    boolean=
        safe_text,
    timeOut=
        st.integers(),
    lang=
        safe_text,
    package=
        safe_text,
    imports=
        safe_text
)
xtextTest::Model_strategy = st.builds(
    xtextTest::Model,
)

@given(instance=xtextTest::ReplacePatterns_strategy)
@settings(max_examples=50)
def test_xtexttest::replacepatterns_instantiation(instance):
    assert isinstance(instance, xtextTest::ReplacePatterns)

@given(instance=xtextTest::ReplacePatterns_strategy)
def test_xtexttest::replacepatterns_regex_type(instance):
    assert isinstance(instance.regex, str)


@given(instance=xtextTest::ReplacePatterns_strategy)
def test_xtexttest::replacepatterns_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original

@given(instance=xtextTest::ReplacePatterns_strategy)
def test_xtexttest::replacepatterns_replace_type(instance):
    assert isinstance(instance.replace, str)


@given(instance=xtextTest::ReplacePatterns_strategy)
def test_xtexttest::replacepatterns_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original

@given(instance=xtextTest::Inner_strategy)
@settings(max_examples=50)
def test_xtexttest::inner_instantiation(instance):
    assert isinstance(instance, xtextTest::Inner)

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isNull_type(instance):
    assert isinstance(instance.isNull, bool)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isNull_setter(instance):
    original = instance.isNull
    instance.isNull = original
    assert instance.isNull == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_assignAsBool_type(instance):
    assert isinstance(instance.assignAsBool, str)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_assignAsBool_setter(instance):
    original = instance.assignAsBool
    instance.assignAsBool = original
    assert instance.assignAsBool == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_parameter_type(instance):
    assert isinstance(instance.parameter, str)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isEmpty_type(instance):
    assert isinstance(instance.isEmpty, bool)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isEmpty_setter(instance):
    original = instance.isEmpty
    instance.isEmpty = original
    assert instance.isEmpty == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_assignAsData_type(instance):
    assert isinstance(instance.assignAsData, str)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_assignAsData_setter(instance):
    original = instance.assignAsData
    instance.assignAsData = original
    assert instance.assignAsData == original

@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isNotNull_type(instance):
    assert isinstance(instance.isNotNull, bool)


@given(instance=xtextTest::Inner_strategy)
def test_xtexttest::inner_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original

@given(instance=xtextTest::MyTokens_strategy)
@settings(max_examples=50)
def test_xtexttest::mytokens_instantiation(instance):
    assert isinstance(instance, xtextTest::MyTokens)

@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=xtextTest::MyTokens_strategy)
def test_xtexttest::mytokens_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=xtextTest::CodeCall_strategy)
@settings(max_examples=50)
def test_xtexttest::codecall_instantiation(instance):
    assert isinstance(instance, xtextTest::CodeCall)

@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_myclass_type(instance):
    assert isinstance(instance.myclass, str)


@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_myclass_setter(instance):
    original = instance.myclass
    instance.myclass = original
    assert instance.myclass == original

@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=xtextTest::CodeCall_strategy)
def test_xtexttest::codecall_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=xtextTest::Import_strategy)
@settings(max_examples=50)
def test_xtexttest::import_instantiation(instance):
    assert isinstance(instance, xtextTest::Import)

@given(instance=xtextTest::Import_strategy)
def test_xtexttest::import_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=xtextTest::Import_strategy)
def test_xtexttest::import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=xtextTest::Import_strategy)
def test_xtexttest::import_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xtextTest::Import_strategy)
def test_xtexttest::import_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xtextTest::After_strategy)
@settings(max_examples=50)
def test_xtexttest::after_instantiation(instance):
    assert isinstance(instance, xtextTest::After)

@given(instance=xtextTest::Before_strategy)
@settings(max_examples=50)
def test_xtexttest::before_instantiation(instance):
    assert isinstance(instance, xtextTest::Before)

@given(instance=xtextTest::Generator_strategy)
@settings(max_examples=50)
def test_xtexttest::generator_instantiation(instance):
    assert isinstance(instance, xtextTest::Generator)

@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_patternFile_type(instance):
    assert isinstance(instance.patternFile, str)


@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_patternFile_setter(instance):
    original = instance.patternFile
    instance.patternFile = original
    assert instance.patternFile == original

@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_expected_type(instance):
    assert isinstance(instance.expected, str)


@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_expected_setter(instance):
    original = instance.expected
    instance.expected = original
    assert instance.expected == original

@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_exception_type(instance):
    assert isinstance(instance.exception, str)


@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original

@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_isSameAsInputFile_type(instance):
    assert isinstance(instance.isSameAsInputFile, bool)


@given(instance=xtextTest::Generator_strategy)
def test_xtexttest::generator_isSameAsInputFile_setter(instance):
    original = instance.isSameAsInputFile
    instance.isSameAsInputFile = original
    assert instance.isSameAsInputFile == original

@given(instance=xtextTest::Element_strategy)
@settings(max_examples=50)
def test_xtexttest::element_instantiation(instance):
    assert isinstance(instance, xtextTest::Element)

@given(instance=xtextTest::Element_strategy)
def test_xtexttest::element_importing_type(instance):
    assert isinstance(instance.importing, str)


@given(instance=xtextTest::Element_strategy)
def test_xtexttest::element_importing_setter(instance):
    original = instance.importing
    instance.importing = original
    assert instance.importing == original

@given(instance=xtextTest::Element_strategy)
def test_xtexttest::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xtextTest::Element_strategy)
def test_xtexttest::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xtextTest::Tokens_strategy)
@settings(max_examples=50)
def test_xtexttest::tokens_instantiation(instance):
    assert isinstance(instance, xtextTest::Tokens)

@given(instance=xtextTest::Input_strategy)
@settings(max_examples=50)
def test_xtexttest::input_instantiation(instance):
    assert isinstance(instance, xtextTest::Input)

@given(instance=xtextTest::Input_strategy)
def test_xtexttest::input_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=xtextTest::Input_strategy)
def test_xtexttest::input_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xtextTest::Input_strategy)
def test_xtexttest::input_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=xtextTest::Input_strategy)
def test_xtexttest::input_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=xtextTest::EmfTest_strategy)
@settings(max_examples=50)
def test_xtexttest::emftest_instantiation(instance):
    assert isinstance(instance, xtextTest::EmfTest)

@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_mydefault_type(instance):
    assert isinstance(instance.mydefault, str)


@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_mydefault_setter(instance):
    original = instance.mydefault
    instance.mydefault = original
    assert instance.mydefault == original

@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_timeOut_type(instance):
    assert isinstance(instance.timeOut, int)


@given(instance=xtextTest::EmfTest_strategy)
def test_xtexttest::emftest_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original

@given(instance=xtextTest::XtextTest_strategy)
@settings(max_examples=50)
def test_xtexttest::xtexttest_instantiation(instance):
    assert isinstance(instance, xtextTest::XtextTest)

@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_boolean_type(instance):
    assert isinstance(instance.boolean, str)


@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original

@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_timeOut_type(instance):
    assert isinstance(instance.timeOut, int)


@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original

@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_imports_type(instance):
    assert isinstance(instance.imports, str)


@given(instance=xtextTest::XtextTest_strategy)
def test_xtexttest::xtexttest_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original

@given(instance=xtextTest::Model_strategy)
@settings(max_examples=50)
def test_xtexttest::model_instantiation(instance):
    assert isinstance(instance, xtextTest::Model)
