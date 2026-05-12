import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xtextTest_ReplacePatterns,
    xtextTest_Inner,
    xtextTest_MyTokens,
    xtextTest_CodeCall,
    xtextTest_Import,
    xtextTest_After,
    xtextTest_Before,
    xtextTest_Generator,
    xtextTest_Element,
    xtextTest_Tokens,
    xtextTest_Input,
    xtextTest_EmfTest,
    xtextTest_XtextTest,
    xtextTest_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xtexttest_replacepatterns_is_not_abstract():
    assert not inspect.isabstract(xtextTest_ReplacePatterns)


def test_xtexttest_replacepatterns_constructor_exists():
    assert callable(xtextTest_ReplacePatterns.__init__)


def test_xtexttest_replacepatterns_constructor_args():
    sig = inspect.signature(xtextTest_ReplacePatterns.__init__)
    params = list(sig.parameters.keys())
    assert "regex" in params, "Missing parameter 'regex'"
    assert "replace" in params, "Missing parameter 'replace'"

def test_xtexttest_replacepatterns_has_regex():
    assert hasattr(xtextTest_ReplacePatterns, "regex")
    descriptor = None
    for klass in xtextTest_ReplacePatterns.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_replacepatterns_has_replace():
    assert hasattr(xtextTest_ReplacePatterns, "replace")
    descriptor = None
    for klass in xtextTest_ReplacePatterns.__mro__:
        if "replace" in klass.__dict__:
            descriptor = klass.__dict__["replace"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_inner_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Inner)


def test_xtexttest_inner_constructor_exists():
    assert callable(xtextTest_Inner.__init__)


def test_xtexttest_inner_constructor_args():
    sig = inspect.signature(xtextTest_Inner.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "isNotNull" in params, "Missing parameter 'isNotNull'"
    assert "isEmpty" in params, "Missing parameter 'isEmpty'"
    assert "assignAsData" in params, "Missing parameter 'assignAsData'"
    assert "isNull" in params, "Missing parameter 'isNull'"
    assert "assignAsBool" in params, "Missing parameter 'assignAsBool'"
    assert "value" in params, "Missing parameter 'value'"

def test_xtexttest_inner_has_parameter():
    assert hasattr(xtextTest_Inner, "parameter")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_isNotNull():
    assert hasattr(xtextTest_Inner, "isNotNull")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "isNotNull" in klass.__dict__:
            descriptor = klass.__dict__["isNotNull"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_isEmpty():
    assert hasattr(xtextTest_Inner, "isEmpty")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "isEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isEmpty"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_assignAsData():
    assert hasattr(xtextTest_Inner, "assignAsData")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "assignAsData" in klass.__dict__:
            descriptor = klass.__dict__["assignAsData"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_isNull():
    assert hasattr(xtextTest_Inner, "isNull")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "isNull" in klass.__dict__:
            descriptor = klass.__dict__["isNull"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_assignAsBool():
    assert hasattr(xtextTest_Inner, "assignAsBool")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "assignAsBool" in klass.__dict__:
            descriptor = klass.__dict__["assignAsBool"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_inner_has_value():
    assert hasattr(xtextTest_Inner, "value")
    descriptor = None
    for klass in xtextTest_Inner.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_mytokens_is_not_abstract():
    assert not inspect.isabstract(xtextTest_MyTokens)


def test_xtexttest_mytokens_constructor_exists():
    assert callable(xtextTest_MyTokens.__init__)


def test_xtexttest_mytokens_constructor_args():
    sig = inspect.signature(xtextTest_MyTokens.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "string" in params, "Missing parameter 'string'"
    assert "token" in params, "Missing parameter 'token'"

def test_xtexttest_mytokens_has_count():
    assert hasattr(xtextTest_MyTokens, "count")
    descriptor = None
    for klass in xtextTest_MyTokens.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_mytokens_has_string():
    assert hasattr(xtextTest_MyTokens, "string")
    descriptor = None
    for klass in xtextTest_MyTokens.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_mytokens_has_token():
    assert hasattr(xtextTest_MyTokens, "token")
    descriptor = None
    for klass in xtextTest_MyTokens.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_codecall_is_not_abstract():
    assert not inspect.isabstract(xtextTest_CodeCall)


def test_xtexttest_codecall_constructor_exists():
    assert callable(xtextTest_CodeCall.__init__)


def test_xtexttest_codecall_constructor_args():
    sig = inspect.signature(xtextTest_CodeCall.__init__)
    params = list(sig.parameters.keys())
    assert "myclass" in params, "Missing parameter 'myclass'"
    assert "method" in params, "Missing parameter 'method'"
    assert "params" in params, "Missing parameter 'params'"

def test_xtexttest_codecall_has_myclass():
    assert hasattr(xtextTest_CodeCall, "myclass")
    descriptor = None
    for klass in xtextTest_CodeCall.__mro__:
        if "myclass" in klass.__dict__:
            descriptor = klass.__dict__["myclass"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_codecall_has_method():
    assert hasattr(xtextTest_CodeCall, "method")
    descriptor = None
    for klass in xtextTest_CodeCall.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_codecall_has_params():
    assert hasattr(xtextTest_CodeCall, "params")
    descriptor = None
    for klass in xtextTest_CodeCall.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_import_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Import)


def test_xtexttest_import_constructor_exists():
    assert callable(xtextTest_Import.__init__)


def test_xtexttest_import_constructor_args():
    sig = inspect.signature(xtextTest_Import.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_xtexttest_import_has_id():
    assert hasattr(xtextTest_Import, "id")
    descriptor = None
    for klass in xtextTest_Import.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_import_has_alias():
    assert hasattr(xtextTest_Import, "alias")
    descriptor = None
    for klass in xtextTest_Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_after_is_not_abstract():
    assert not inspect.isabstract(xtextTest_After)


def test_xtexttest_after_constructor_exists():
    assert callable(xtextTest_After.__init__)


def test_xtexttest_after_constructor_args():
    sig = inspect.signature(xtextTest_After.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest_before_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Before)


def test_xtexttest_before_constructor_exists():
    assert callable(xtextTest_Before.__init__)


def test_xtexttest_before_constructor_args():
    sig = inspect.signature(xtextTest_Before.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest_generator_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Generator)


def test_xtexttest_generator_constructor_exists():
    assert callable(xtextTest_Generator.__init__)


def test_xtexttest_generator_constructor_args():
    sig = inspect.signature(xtextTest_Generator.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "isSameAsInputFile" in params, "Missing parameter 'isSameAsInputFile'"
    assert "expected" in params, "Missing parameter 'expected'"
    assert "exception" in params, "Missing parameter 'exception'"
    assert "patternFile" in params, "Missing parameter 'patternFile'"

def test_xtexttest_generator_has_output():
    assert hasattr(xtextTest_Generator, "output")
    descriptor = None
    for klass in xtextTest_Generator.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_generator_has_isSameAsInputFile():
    assert hasattr(xtextTest_Generator, "isSameAsInputFile")
    descriptor = None
    for klass in xtextTest_Generator.__mro__:
        if "isSameAsInputFile" in klass.__dict__:
            descriptor = klass.__dict__["isSameAsInputFile"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_generator_has_expected():
    assert hasattr(xtextTest_Generator, "expected")
    descriptor = None
    for klass in xtextTest_Generator.__mro__:
        if "expected" in klass.__dict__:
            descriptor = klass.__dict__["expected"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_generator_has_exception():
    assert hasattr(xtextTest_Generator, "exception")
    descriptor = None
    for klass in xtextTest_Generator.__mro__:
        if "exception" in klass.__dict__:
            descriptor = klass.__dict__["exception"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_generator_has_patternFile():
    assert hasattr(xtextTest_Generator, "patternFile")
    descriptor = None
    for klass in xtextTest_Generator.__mro__:
        if "patternFile" in klass.__dict__:
            descriptor = klass.__dict__["patternFile"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_element_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Element)


def test_xtexttest_element_constructor_exists():
    assert callable(xtextTest_Element.__init__)


def test_xtexttest_element_constructor_args():
    sig = inspect.signature(xtextTest_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "importing" in params, "Missing parameter 'importing'"

def test_xtexttest_element_has_name():
    assert hasattr(xtextTest_Element, "name")
    descriptor = None
    for klass in xtextTest_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_element_has_importing():
    assert hasattr(xtextTest_Element, "importing")
    descriptor = None
    for klass in xtextTest_Element.__mro__:
        if "importing" in klass.__dict__:
            descriptor = klass.__dict__["importing"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_tokens_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Tokens)


def test_xtexttest_tokens_constructor_exists():
    assert callable(xtextTest_Tokens.__init__)


def test_xtexttest_tokens_constructor_args():
    sig = inspect.signature(xtextTest_Tokens.__init__)
    params = list(sig.parameters.keys())



def test_xtexttest_input_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Input)


def test_xtexttest_input_constructor_exists():
    assert callable(xtextTest_Input.__init__)


def test_xtexttest_input_constructor_args():
    sig = inspect.signature(xtextTest_Input.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "file" in params, "Missing parameter 'file'"

def test_xtexttest_input_has_text():
    assert hasattr(xtextTest_Input, "text")
    descriptor = None
    for klass in xtextTest_Input.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_input_has_file():
    assert hasattr(xtextTest_Input, "file")
    descriptor = None
    for klass in xtextTest_Input.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_emftest_is_not_abstract():
    assert not inspect.isabstract(xtextTest_EmfTest)


def test_xtexttest_emftest_constructor_exists():
    assert callable(xtextTest_EmfTest.__init__)


def test_xtexttest_emftest_constructor_args():
    sig = inspect.signature(xtextTest_EmfTest.__init__)
    params = list(sig.parameters.keys())
    assert "mydefault" in params, "Missing parameter 'mydefault'"
    assert "file" in params, "Missing parameter 'file'"
    assert "package" in params, "Missing parameter 'package'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"

def test_xtexttest_emftest_has_mydefault():
    assert hasattr(xtextTest_EmfTest, "mydefault")
    descriptor = None
    for klass in xtextTest_EmfTest.__mro__:
        if "mydefault" in klass.__dict__:
            descriptor = klass.__dict__["mydefault"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_emftest_has_file():
    assert hasattr(xtextTest_EmfTest, "file")
    descriptor = None
    for klass in xtextTest_EmfTest.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_emftest_has_package():
    assert hasattr(xtextTest_EmfTest, "package")
    descriptor = None
    for klass in xtextTest_EmfTest.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_emftest_has_timeOut():
    assert hasattr(xtextTest_EmfTest, "timeOut")
    descriptor = None
    for klass in xtextTest_EmfTest.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_xtexttest_is_not_abstract():
    assert not inspect.isabstract(xtextTest_XtextTest)


def test_xtexttest_xtexttest_constructor_exists():
    assert callable(xtextTest_XtextTest.__init__)


def test_xtexttest_xtexttest_constructor_args():
    sig = inspect.signature(xtextTest_XtextTest.__init__)
    params = list(sig.parameters.keys())
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "timeOut" in params, "Missing parameter 'timeOut'"
    assert "lang" in params, "Missing parameter 'lang'"
    assert "imports" in params, "Missing parameter 'imports'"
    assert "package" in params, "Missing parameter 'package'"

def test_xtexttest_xtexttest_has_boolean():
    assert hasattr(xtextTest_XtextTest, "boolean")
    descriptor = None
    for klass in xtextTest_XtextTest.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_xtexttest_has_timeOut():
    assert hasattr(xtextTest_XtextTest, "timeOut")
    descriptor = None
    for klass in xtextTest_XtextTest.__mro__:
        if "timeOut" in klass.__dict__:
            descriptor = klass.__dict__["timeOut"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_xtexttest_has_lang():
    assert hasattr(xtextTest_XtextTest, "lang")
    descriptor = None
    for klass in xtextTest_XtextTest.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_xtexttest_has_imports():
    assert hasattr(xtextTest_XtextTest, "imports")
    descriptor = None
    for klass in xtextTest_XtextTest.__mro__:
        if "imports" in klass.__dict__:
            descriptor = klass.__dict__["imports"]
            break
    assert isinstance(descriptor, property)

def test_xtexttest_xtexttest_has_package():
    assert hasattr(xtextTest_XtextTest, "package")
    descriptor = None
    for klass in xtextTest_XtextTest.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_xtexttest_model_is_not_abstract():
    assert not inspect.isabstract(xtextTest_Model)


def test_xtexttest_model_constructor_exists():
    assert callable(xtextTest_Model.__init__)


def test_xtexttest_model_constructor_args():
    sig = inspect.signature(xtextTest_Model.__init__)
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
xtextTest_ReplacePatterns_strategy = st.builds(
    xtextTest_ReplacePatterns,
    regex=
        safe_text,
    replace=
        safe_text
)
xtextTest_Inner_strategy = st.builds(
    xtextTest_Inner,
    parameter=
        safe_text,
    isNotNull=
        st.booleans(),
    isEmpty=
        st.booleans(),
    assignAsData=
        safe_text,
    isNull=
        st.booleans(),
    assignAsBool=
        safe_text,
    value=
        safe_text
)
xtextTest_MyTokens_strategy = st.builds(
    xtextTest_MyTokens,
    count=
        st.integers(),
    string=
        safe_text,
    token=
        safe_text
)
xtextTest_CodeCall_strategy = st.builds(
    xtextTest_CodeCall,
    myclass=
        safe_text,
    method=
        safe_text,
    params=
        safe_text
)
xtextTest_Import_strategy = st.builds(
    xtextTest_Import,
    id=
        safe_text,
    alias=
        safe_text
)
xtextTest_After_strategy = st.builds(
    xtextTest_After,
)
xtextTest_Before_strategy = st.builds(
    xtextTest_Before,
)
xtextTest_Generator_strategy = st.builds(
    xtextTest_Generator,
    output=
        safe_text,
    isSameAsInputFile=
        st.booleans(),
    expected=
        safe_text,
    exception=
        safe_text,
    patternFile=
        safe_text
)
xtextTest_Element_strategy = st.builds(
    xtextTest_Element,
    name=
        safe_text,
    importing=
        safe_text
)
xtextTest_Tokens_strategy = st.builds(
    xtextTest_Tokens,
)
xtextTest_Input_strategy = st.builds(
    xtextTest_Input,
    text=
        safe_text,
    file=
        safe_text
)
xtextTest_EmfTest_strategy = st.builds(
    xtextTest_EmfTest,
    mydefault=
        safe_text,
    file=
        safe_text,
    package=
        safe_text,
    timeOut=
        st.integers()
)
xtextTest_XtextTest_strategy = st.builds(
    xtextTest_XtextTest,
    boolean=
        safe_text,
    timeOut=
        st.integers(),
    lang=
        safe_text,
    imports=
        safe_text,
    package=
        safe_text
)
xtextTest_Model_strategy = st.builds(
    xtextTest_Model,
)

@given(instance=xtextTest_ReplacePatterns_strategy)
@settings(max_examples=50)
def test_xtexttest_replacepatterns_instantiation(instance):
    assert isinstance(instance, xtextTest_ReplacePatterns)



@given(instance=xtextTest_ReplacePatterns_strategy)
def test_xtexttest_replacepatterns_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original



@given(instance=xtextTest_ReplacePatterns_strategy)
def test_xtexttest_replacepatterns_replace_setter(instance):
    original = instance.replace
    instance.replace = original
    assert instance.replace == original

@given(instance=xtextTest_Inner_strategy)
@settings(max_examples=50)
def test_xtexttest_inner_instantiation(instance):
    assert isinstance(instance, xtextTest_Inner)



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_isNotNull_setter(instance):
    original = instance.isNotNull
    instance.isNotNull = original
    assert instance.isNotNull == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_isEmpty_setter(instance):
    original = instance.isEmpty
    instance.isEmpty = original
    assert instance.isEmpty == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_assignAsData_setter(instance):
    original = instance.assignAsData
    instance.assignAsData = original
    assert instance.assignAsData == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_isNull_setter(instance):
    original = instance.isNull
    instance.isNull = original
    assert instance.isNull == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_assignAsBool_setter(instance):
    original = instance.assignAsBool
    instance.assignAsBool = original
    assert instance.assignAsBool == original



@given(instance=xtextTest_Inner_strategy)
def test_xtexttest_inner_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xtextTest_MyTokens_strategy)
@settings(max_examples=50)
def test_xtexttest_mytokens_instantiation(instance):
    assert isinstance(instance, xtextTest_MyTokens)



@given(instance=xtextTest_MyTokens_strategy)
def test_xtexttest_mytokens_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=xtextTest_MyTokens_strategy)
def test_xtexttest_mytokens_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=xtextTest_MyTokens_strategy)
def test_xtexttest_mytokens_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=xtextTest_CodeCall_strategy)
@settings(max_examples=50)
def test_xtexttest_codecall_instantiation(instance):
    assert isinstance(instance, xtextTest_CodeCall)



@given(instance=xtextTest_CodeCall_strategy)
def test_xtexttest_codecall_myclass_setter(instance):
    original = instance.myclass
    instance.myclass = original
    assert instance.myclass == original



@given(instance=xtextTest_CodeCall_strategy)
def test_xtexttest_codecall_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original



@given(instance=xtextTest_CodeCall_strategy)
def test_xtexttest_codecall_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=xtextTest_Import_strategy)
@settings(max_examples=50)
def test_xtexttest_import_instantiation(instance):
    assert isinstance(instance, xtextTest_Import)



@given(instance=xtextTest_Import_strategy)
def test_xtexttest_import_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xtextTest_Import_strategy)
def test_xtexttest_import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=xtextTest_After_strategy)
@settings(max_examples=50)
def test_xtexttest_after_instantiation(instance):
    assert isinstance(instance, xtextTest_After)

@given(instance=xtextTest_Before_strategy)
@settings(max_examples=50)
def test_xtexttest_before_instantiation(instance):
    assert isinstance(instance, xtextTest_Before)

@given(instance=xtextTest_Generator_strategy)
@settings(max_examples=50)
def test_xtexttest_generator_instantiation(instance):
    assert isinstance(instance, xtextTest_Generator)



@given(instance=xtextTest_Generator_strategy)
def test_xtexttest_generator_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=xtextTest_Generator_strategy)
def test_xtexttest_generator_isSameAsInputFile_setter(instance):
    original = instance.isSameAsInputFile
    instance.isSameAsInputFile = original
    assert instance.isSameAsInputFile == original



@given(instance=xtextTest_Generator_strategy)
def test_xtexttest_generator_expected_setter(instance):
    original = instance.expected
    instance.expected = original
    assert instance.expected == original



@given(instance=xtextTest_Generator_strategy)
def test_xtexttest_generator_exception_setter(instance):
    original = instance.exception
    instance.exception = original
    assert instance.exception == original



@given(instance=xtextTest_Generator_strategy)
def test_xtexttest_generator_patternFile_setter(instance):
    original = instance.patternFile
    instance.patternFile = original
    assert instance.patternFile == original

@given(instance=xtextTest_Element_strategy)
@settings(max_examples=50)
def test_xtexttest_element_instantiation(instance):
    assert isinstance(instance, xtextTest_Element)



@given(instance=xtextTest_Element_strategy)
def test_xtexttest_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xtextTest_Element_strategy)
def test_xtexttest_element_importing_setter(instance):
    original = instance.importing
    instance.importing = original
    assert instance.importing == original

@given(instance=xtextTest_Tokens_strategy)
@settings(max_examples=50)
def test_xtexttest_tokens_instantiation(instance):
    assert isinstance(instance, xtextTest_Tokens)

@given(instance=xtextTest_Input_strategy)
@settings(max_examples=50)
def test_xtexttest_input_instantiation(instance):
    assert isinstance(instance, xtextTest_Input)



@given(instance=xtextTest_Input_strategy)
def test_xtexttest_input_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=xtextTest_Input_strategy)
def test_xtexttest_input_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=xtextTest_EmfTest_strategy)
@settings(max_examples=50)
def test_xtexttest_emftest_instantiation(instance):
    assert isinstance(instance, xtextTest_EmfTest)



@given(instance=xtextTest_EmfTest_strategy)
def test_xtexttest_emftest_mydefault_setter(instance):
    original = instance.mydefault
    instance.mydefault = original
    assert instance.mydefault == original



@given(instance=xtextTest_EmfTest_strategy)
def test_xtexttest_emftest_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=xtextTest_EmfTest_strategy)
def test_xtexttest_emftest_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=xtextTest_EmfTest_strategy)
def test_xtexttest_emftest_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original

@given(instance=xtextTest_XtextTest_strategy)
@settings(max_examples=50)
def test_xtexttest_xtexttest_instantiation(instance):
    assert isinstance(instance, xtextTest_XtextTest)



@given(instance=xtextTest_XtextTest_strategy)
def test_xtexttest_xtexttest_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=xtextTest_XtextTest_strategy)
def test_xtexttest_xtexttest_timeOut_setter(instance):
    original = instance.timeOut
    instance.timeOut = original
    assert instance.timeOut == original



@given(instance=xtextTest_XtextTest_strategy)
def test_xtexttest_xtexttest_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original



@given(instance=xtextTest_XtextTest_strategy)
def test_xtexttest_xtexttest_imports_setter(instance):
    original = instance.imports
    instance.imports = original
    assert instance.imports == original



@given(instance=xtextTest_XtextTest_strategy)
def test_xtexttest_xtexttest_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=xtextTest_Model_strategy)
@settings(max_examples=50)
def test_xtexttest_model_instantiation(instance):
    assert isinstance(instance, xtextTest_Model)
