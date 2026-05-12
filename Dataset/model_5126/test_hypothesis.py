import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    junitresult_JunitResult,
    JunitResult,
    junitresult_AbstractAggregatedTest,
    junitresult_NegativeResult,
    NegativeResult,
    junitresult_Error,
    junitresult_Failure,
    junitresult_Skipped,
    junitresult_Testcase,
    AbstractAggregatedTest,
    junitresult_Testrun,
    junitresult_Testsuites,
    junitresult_Testsuite,
    junitresult_Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_junitresult_junitresult_is_not_abstract():
    assert not inspect.isabstract(junitresult_JunitResult)


def test_junitresult_junitresult_constructor_exists():
    assert callable(junitresult_JunitResult.__init__)


def test_junitresult_junitresult_constructor_args():
    sig = inspect.signature(junitresult_JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_is_not_abstract():
    assert not inspect.isabstract(JunitResult)


def test_junitresult_constructor_exists():
    assert callable(JunitResult.__init__)


def test_junitresult_constructor_args():
    sig = inspect.signature(JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(junitresult_AbstractAggregatedTest)


def test_junitresult_abstractaggregatedtest_constructor_exists():
    assert callable(junitresult_AbstractAggregatedTest.__init__)


def test_junitresult_abstractaggregatedtest_constructor_args():
    sig = inspect.signature(junitresult_AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())
    assert "tests" in params, "Missing parameter 'tests'"
    assert "failures" in params, "Missing parameter 'failures'"
    assert "name" in params, "Missing parameter 'name'"
    assert "errors" in params, "Missing parameter 'errors'"

def test_junitresult_abstractaggregatedtest_has_tests():
    assert hasattr(junitresult_AbstractAggregatedTest, "tests")
    descriptor = None
    for klass in junitresult_AbstractAggregatedTest.__mro__:
        if "tests" in klass.__dict__:
            descriptor = klass.__dict__["tests"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_abstractaggregatedtest_has_failures():
    assert hasattr(junitresult_AbstractAggregatedTest, "failures")
    descriptor = None
    for klass in junitresult_AbstractAggregatedTest.__mro__:
        if "failures" in klass.__dict__:
            descriptor = klass.__dict__["failures"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_abstractaggregatedtest_has_name():
    assert hasattr(junitresult_AbstractAggregatedTest, "name")
    descriptor = None
    for klass in junitresult_AbstractAggregatedTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_abstractaggregatedtest_has_errors():
    assert hasattr(junitresult_AbstractAggregatedTest, "errors")
    descriptor = None
    for klass in junitresult_AbstractAggregatedTest.__mro__:
        if "errors" in klass.__dict__:
            descriptor = klass.__dict__["errors"]
            break
    assert isinstance(descriptor, property)



def test_junitresult_negativeresult_is_not_abstract():
    assert not inspect.isabstract(junitresult_NegativeResult)


def test_junitresult_negativeresult_constructor_exists():
    assert callable(junitresult_NegativeResult.__init__)


def test_junitresult_negativeresult_constructor_args():
    sig = inspect.signature(junitresult_NegativeResult.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "type" in params, "Missing parameter 'type'"
    assert "value" in params, "Missing parameter 'value'"

def test_junitresult_negativeresult_has_message():
    assert hasattr(junitresult_NegativeResult, "message")
    descriptor = None
    for klass in junitresult_NegativeResult.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_negativeresult_has_type():
    assert hasattr(junitresult_NegativeResult, "type")
    descriptor = None
    for klass in junitresult_NegativeResult.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_negativeresult_has_value():
    assert hasattr(junitresult_NegativeResult, "value")
    descriptor = None
    for klass in junitresult_NegativeResult.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_negativeresult_is_not_abstract():
    assert not inspect.isabstract(NegativeResult)


def test_negativeresult_constructor_exists():
    assert callable(NegativeResult.__init__)


def test_negativeresult_constructor_args():
    sig = inspect.signature(NegativeResult.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_error_is_not_abstract():
    assert not inspect.isabstract(junitresult_Error)


def test_junitresult_error_constructor_exists():
    assert callable(junitresult_Error.__init__)


def test_junitresult_error_constructor_args():
    sig = inspect.signature(junitresult_Error.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_failure_is_not_abstract():
    assert not inspect.isabstract(junitresult_Failure)


def test_junitresult_failure_constructor_exists():
    assert callable(junitresult_Failure.__init__)


def test_junitresult_failure_constructor_args():
    sig = inspect.signature(junitresult_Failure.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_skipped_is_not_abstract():
    assert not inspect.isabstract(junitresult_Skipped)


def test_junitresult_skipped_constructor_exists():
    assert callable(junitresult_Skipped.__init__)


def test_junitresult_skipped_constructor_args():
    sig = inspect.signature(junitresult_Skipped.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_testcase_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testcase)


def test_junitresult_testcase_constructor_exists():
    assert callable(junitresult_Testcase.__init__)


def test_junitresult_testcase_constructor_args():
    sig = inspect.signature(junitresult_Testcase.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "system_out" in params, "Missing parameter 'system_out'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "time" in params, "Missing parameter 'time'"
    assert "status" in params, "Missing parameter 'status'"
    assert "assertions" in params, "Missing parameter 'assertions'"

def test_junitresult_testcase_has_name():
    assert hasattr(junitresult_Testcase, "name")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_classname():
    assert hasattr(junitresult_Testcase, "classname")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_system_out():
    assert hasattr(junitresult_Testcase, "system_out")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "system_out" in klass.__dict__:
            descriptor = klass.__dict__["system_out"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_system_err():
    assert hasattr(junitresult_Testcase, "system_err")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "system_err" in klass.__dict__:
            descriptor = klass.__dict__["system_err"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_time():
    assert hasattr(junitresult_Testcase, "time")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_status():
    assert hasattr(junitresult_Testcase, "status")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testcase_has_assertions():
    assert hasattr(junitresult_Testcase, "assertions")
    descriptor = None
    for klass in junitresult_Testcase.__mro__:
        if "assertions" in klass.__dict__:
            descriptor = klass.__dict__["assertions"]
            break
    assert isinstance(descriptor, property)



def test_abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(AbstractAggregatedTest)


def test_abstractaggregatedtest_constructor_exists():
    assert callable(AbstractAggregatedTest.__init__)


def test_abstractaggregatedtest_constructor_args():
    sig = inspect.signature(AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_testrun_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testrun)


def test_junitresult_testrun_constructor_exists():
    assert callable(junitresult_Testrun.__init__)


def test_junitresult_testrun_constructor_args():
    sig = inspect.signature(junitresult_Testrun.__init__)
    params = list(sig.parameters.keys())
    assert "started" in params, "Missing parameter 'started'"
    assert "project" in params, "Missing parameter 'project'"
    assert "ignored" in params, "Missing parameter 'ignored'"

def test_junitresult_testrun_has_started():
    assert hasattr(junitresult_Testrun, "started")
    descriptor = None
    for klass in junitresult_Testrun.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testrun_has_project():
    assert hasattr(junitresult_Testrun, "project")
    descriptor = None
    for klass in junitresult_Testrun.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testrun_has_ignored():
    assert hasattr(junitresult_Testrun, "ignored")
    descriptor = None
    for klass in junitresult_Testrun.__mro__:
        if "ignored" in klass.__dict__:
            descriptor = klass.__dict__["ignored"]
            break
    assert isinstance(descriptor, property)



def test_junitresult_testsuites_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testsuites)


def test_junitresult_testsuites_constructor_exists():
    assert callable(junitresult_Testsuites.__init__)


def test_junitresult_testsuites_constructor_args():
    sig = inspect.signature(junitresult_Testsuites.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_junitresult_testsuites_has_time():
    assert hasattr(junitresult_Testsuites, "time")
    descriptor = None
    for klass in junitresult_Testsuites.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuites_has_disabled():
    assert hasattr(junitresult_Testsuites, "disabled")
    descriptor = None
    for klass in junitresult_Testsuites.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_junitresult_testsuite_is_not_abstract():
    assert not inspect.isabstract(junitresult_Testsuite)


def test_junitresult_testsuite_constructor_exists():
    assert callable(junitresult_Testsuite.__init__)


def test_junitresult_testsuite_constructor_args():
    sig = inspect.signature(junitresult_Testsuite.__init__)
    params = list(sig.parameters.keys())
    assert "skipped" in params, "Missing parameter 'skipped'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "id" in params, "Missing parameter 'id'"
    assert "time" in params, "Missing parameter 'time'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "package" in params, "Missing parameter 'package'"
    assert "hostname" in params, "Missing parameter 'hostname'"
    assert "system_out" in params, "Missing parameter 'system_out'"

def test_junitresult_testsuite_has_skipped():
    assert hasattr(junitresult_Testsuite, "skipped")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "skipped" in klass.__dict__:
            descriptor = klass.__dict__["skipped"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_disabled():
    assert hasattr(junitresult_Testsuite, "disabled")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_id():
    assert hasattr(junitresult_Testsuite, "id")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_time():
    assert hasattr(junitresult_Testsuite, "time")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_timestamp():
    assert hasattr(junitresult_Testsuite, "timestamp")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_system_err():
    assert hasattr(junitresult_Testsuite, "system_err")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "system_err" in klass.__dict__:
            descriptor = klass.__dict__["system_err"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_package():
    assert hasattr(junitresult_Testsuite, "package")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_hostname():
    assert hasattr(junitresult_Testsuite, "hostname")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "hostname" in klass.__dict__:
            descriptor = klass.__dict__["hostname"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_testsuite_has_system_out():
    assert hasattr(junitresult_Testsuite, "system_out")
    descriptor = None
    for klass in junitresult_Testsuite.__mro__:
        if "system_out" in klass.__dict__:
            descriptor = klass.__dict__["system_out"]
            break
    assert isinstance(descriptor, property)



def test_junitresult_property_is_not_abstract():
    assert not inspect.isabstract(junitresult_Property)


def test_junitresult_property_constructor_exists():
    assert callable(junitresult_Property.__init__)


def test_junitresult_property_constructor_args():
    sig = inspect.signature(junitresult_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_junitresult_property_has_name():
    assert hasattr(junitresult_Property, "name")
    descriptor = None
    for klass in junitresult_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_junitresult_property_has_value():
    assert hasattr(junitresult_Property, "value")
    descriptor = None
    for klass in junitresult_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
junitresult_JunitResult_strategy = st.builds(
    junitresult_JunitResult,
)
JunitResult_strategy = st.builds(
    JunitResult,
)
junitresult_AbstractAggregatedTest_strategy = st.builds(
    junitresult_AbstractAggregatedTest,
    tests=
        st.integers(),
    failures=
        st.integers(),
    name=
        safe_text,
    errors=
        st.integers()
)
junitresult_NegativeResult_strategy = st.builds(
    junitresult_NegativeResult,
    message=
        safe_text,
    type=
        safe_text,
    value=
        safe_text
)
NegativeResult_strategy = st.builds(
    NegativeResult,
)
junitresult_Error_strategy = st.builds(
    junitresult_Error,
)
junitresult_Failure_strategy = st.builds(
    junitresult_Failure,
)
junitresult_Skipped_strategy = st.builds(
    junitresult_Skipped,
)
junitresult_Testcase_strategy = st.builds(
    junitresult_Testcase,
    name=
        safe_text,
    classname=
        safe_text,
    system_out=
        safe_text,
    system_err=
        safe_text,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    status=
        safe_text,
    assertions=
        safe_text
)
AbstractAggregatedTest_strategy = st.builds(
    AbstractAggregatedTest,
)
junitresult_Testrun_strategy = st.builds(
    junitresult_Testrun,
    started=
        st.integers(),
    project=
        safe_text,
    ignored=
        st.integers()
)
junitresult_Testsuites_strategy = st.builds(
    junitresult_Testsuites,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    disabled=
        st.integers()
)
junitresult_Testsuite_strategy = st.builds(
    junitresult_Testsuite,
    skipped=
        st.integers(),
    disabled=
        st.integers(),
    id=
        st.integers(),
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    timestamp=
        st.dates(),
    system_err=
        safe_text,
    package=
        safe_text,
    hostname=
        safe_text,
    system_out=
        safe_text
)
junitresult_Property_strategy = st.builds(
    junitresult_Property,
    name=
        safe_text,
    value=
        safe_text
)

@given(instance=junitresult_JunitResult_strategy)
@settings(max_examples=50)
def test_junitresult_junitresult_instantiation(instance):
    assert isinstance(instance, junitresult_JunitResult)

@given(instance=JunitResult_strategy)
@settings(max_examples=50)
def test_junitresult_instantiation(instance):
    assert isinstance(instance, JunitResult)

@given(instance=junitresult_AbstractAggregatedTest_strategy)
@settings(max_examples=50)
def test_junitresult_abstractaggregatedtest_instantiation(instance):
    assert isinstance(instance, junitresult_AbstractAggregatedTest)



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_junitresult_abstractaggregatedtest_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_junitresult_abstractaggregatedtest_failures_setter(instance):
    original = instance.failures
    instance.failures = original
    assert instance.failures == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_junitresult_abstractaggregatedtest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=junitresult_AbstractAggregatedTest_strategy)
def test_junitresult_abstractaggregatedtest_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original

@given(instance=junitresult_NegativeResult_strategy)
@settings(max_examples=50)
def test_junitresult_negativeresult_instantiation(instance):
    assert isinstance(instance, junitresult_NegativeResult)



@given(instance=junitresult_NegativeResult_strategy)
def test_junitresult_negativeresult_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=junitresult_NegativeResult_strategy)
def test_junitresult_negativeresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=junitresult_NegativeResult_strategy)
def test_junitresult_negativeresult_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NegativeResult_strategy)
@settings(max_examples=50)
def test_negativeresult_instantiation(instance):
    assert isinstance(instance, NegativeResult)

@given(instance=junitresult_Error_strategy)
@settings(max_examples=50)
def test_junitresult_error_instantiation(instance):
    assert isinstance(instance, junitresult_Error)

@given(instance=junitresult_Failure_strategy)
@settings(max_examples=50)
def test_junitresult_failure_instantiation(instance):
    assert isinstance(instance, junitresult_Failure)

@given(instance=junitresult_Skipped_strategy)
@settings(max_examples=50)
def test_junitresult_skipped_instantiation(instance):
    assert isinstance(instance, junitresult_Skipped)

@given(instance=junitresult_Testcase_strategy)
@settings(max_examples=50)
def test_junitresult_testcase_instantiation(instance):
    assert isinstance(instance, junitresult_Testcase)



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=junitresult_Testcase_strategy)
def test_junitresult_testcase_assertions_setter(instance):
    original = instance.assertions
    instance.assertions = original
    assert instance.assertions == original

@given(instance=AbstractAggregatedTest_strategy)
@settings(max_examples=50)
def test_abstractaggregatedtest_instantiation(instance):
    assert isinstance(instance, AbstractAggregatedTest)

@given(instance=junitresult_Testrun_strategy)
@settings(max_examples=50)
def test_junitresult_testrun_instantiation(instance):
    assert isinstance(instance, junitresult_Testrun)



@given(instance=junitresult_Testrun_strategy)
def test_junitresult_testrun_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original



@given(instance=junitresult_Testrun_strategy)
def test_junitresult_testrun_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original



@given(instance=junitresult_Testrun_strategy)
def test_junitresult_testrun_ignored_setter(instance):
    original = instance.ignored
    instance.ignored = original
    assert instance.ignored == original

@given(instance=junitresult_Testsuites_strategy)
@settings(max_examples=50)
def test_junitresult_testsuites_instantiation(instance):
    assert isinstance(instance, junitresult_Testsuites)



@given(instance=junitresult_Testsuites_strategy)
def test_junitresult_testsuites_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testsuites_strategy)
def test_junitresult_testsuites_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=junitresult_Testsuite_strategy)
@settings(max_examples=50)
def test_junitresult_testsuite_instantiation(instance):
    assert isinstance(instance, junitresult_Testsuite)



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_skipped_setter(instance):
    original = instance.skipped
    instance.skipped = original
    assert instance.skipped == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original



@given(instance=junitresult_Testsuite_strategy)
def test_junitresult_testsuite_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original

@given(instance=junitresult_Property_strategy)
@settings(max_examples=50)
def test_junitresult_property_instantiation(instance):
    assert isinstance(instance, junitresult_Property)



@given(instance=junitresult_Property_strategy)
def test_junitresult_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=junitresult_Property_strategy)
def test_junitresult_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
