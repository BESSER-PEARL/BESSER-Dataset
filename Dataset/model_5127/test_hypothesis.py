import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    junitresult::NegativeResult,
    NegativeResult,
    junitresult::JunitResult,
    JunitResult,
    junitresult::AbstractAggregatedTest,
    junitresult::Property,
    AbstractAggregatedTest,
    junitresult::Testrun,
    junitresult::Testsuites,
    junitresult::Testsuite,
    junitresult::Error,
    junitresult::Failure,
    junitresult::Skipped,
    junitresult::Testcase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_junitresult::negativeresult_is_not_abstract():
    assert not inspect.isabstract(junitresult::NegativeResult)


def test_junitresult::negativeresult_constructor_exists():
    assert callable(junitresult::NegativeResult.__init__)


def test_junitresult::negativeresult_constructor_args():
    sig = inspect.signature(junitresult::NegativeResult.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "message" in params, "Missing parameter 'message'"
    assert "value" in params, "Missing parameter 'value'"

def test_junitresult::negativeresult_has_type():
    assert hasattr(junitresult::NegativeResult, "type")
    descriptor = None
    for klass in junitresult::NegativeResult.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::negativeresult_has_message():
    assert hasattr(junitresult::NegativeResult, "message")
    descriptor = None
    for klass in junitresult::NegativeResult.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::negativeresult_has_value():
    assert hasattr(junitresult::NegativeResult, "value")
    descriptor = None
    for klass in junitresult::NegativeResult.__mro__:
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



def test_junitresult::junitresult_is_not_abstract():
    assert not inspect.isabstract(junitresult::JunitResult)


def test_junitresult::junitresult_constructor_exists():
    assert callable(junitresult::JunitResult.__init__)


def test_junitresult::junitresult_constructor_args():
    sig = inspect.signature(junitresult::JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_junitresult_is_not_abstract():
    assert not inspect.isabstract(JunitResult)


def test_junitresult_constructor_exists():
    assert callable(JunitResult.__init__)


def test_junitresult_constructor_args():
    sig = inspect.signature(JunitResult.__init__)
    params = list(sig.parameters.keys())



def test_junitresult::abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(junitresult::AbstractAggregatedTest)


def test_junitresult::abstractaggregatedtest_constructor_exists():
    assert callable(junitresult::AbstractAggregatedTest.__init__)


def test_junitresult::abstractaggregatedtest_constructor_args():
    sig = inspect.signature(junitresult::AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "failures" in params, "Missing parameter 'failures'"
    assert "errors" in params, "Missing parameter 'errors'"
    assert "tests" in params, "Missing parameter 'tests'"

def test_junitresult::abstractaggregatedtest_has_name():
    assert hasattr(junitresult::AbstractAggregatedTest, "name")
    descriptor = None
    for klass in junitresult::AbstractAggregatedTest.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::abstractaggregatedtest_has_failures():
    assert hasattr(junitresult::AbstractAggregatedTest, "failures")
    descriptor = None
    for klass in junitresult::AbstractAggregatedTest.__mro__:
        if "failures" in klass.__dict__:
            descriptor = klass.__dict__["failures"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::abstractaggregatedtest_has_errors():
    assert hasattr(junitresult::AbstractAggregatedTest, "errors")
    descriptor = None
    for klass in junitresult::AbstractAggregatedTest.__mro__:
        if "errors" in klass.__dict__:
            descriptor = klass.__dict__["errors"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::abstractaggregatedtest_has_tests():
    assert hasattr(junitresult::AbstractAggregatedTest, "tests")
    descriptor = None
    for klass in junitresult::AbstractAggregatedTest.__mro__:
        if "tests" in klass.__dict__:
            descriptor = klass.__dict__["tests"]
            break
    assert isinstance(descriptor, property)



def test_junitresult::property_is_not_abstract():
    assert not inspect.isabstract(junitresult::Property)


def test_junitresult::property_constructor_exists():
    assert callable(junitresult::Property.__init__)


def test_junitresult::property_constructor_args():
    sig = inspect.signature(junitresult::Property.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_junitresult::property_has_value():
    assert hasattr(junitresult::Property, "value")
    descriptor = None
    for klass in junitresult::Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::property_has_name():
    assert hasattr(junitresult::Property, "name")
    descriptor = None
    for klass in junitresult::Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstractaggregatedtest_is_not_abstract():
    assert not inspect.isabstract(AbstractAggregatedTest)


def test_abstractaggregatedtest_constructor_exists():
    assert callable(AbstractAggregatedTest.__init__)


def test_abstractaggregatedtest_constructor_args():
    sig = inspect.signature(AbstractAggregatedTest.__init__)
    params = list(sig.parameters.keys())



def test_junitresult::testrun_is_not_abstract():
    assert not inspect.isabstract(junitresult::Testrun)


def test_junitresult::testrun_constructor_exists():
    assert callable(junitresult::Testrun.__init__)


def test_junitresult::testrun_constructor_args():
    sig = inspect.signature(junitresult::Testrun.__init__)
    params = list(sig.parameters.keys())
    assert "project" in params, "Missing parameter 'project'"
    assert "ignored" in params, "Missing parameter 'ignored'"
    assert "started" in params, "Missing parameter 'started'"

def test_junitresult::testrun_has_project():
    assert hasattr(junitresult::Testrun, "project")
    descriptor = None
    for klass in junitresult::Testrun.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testrun_has_ignored():
    assert hasattr(junitresult::Testrun, "ignored")
    descriptor = None
    for klass in junitresult::Testrun.__mro__:
        if "ignored" in klass.__dict__:
            descriptor = klass.__dict__["ignored"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testrun_has_started():
    assert hasattr(junitresult::Testrun, "started")
    descriptor = None
    for klass in junitresult::Testrun.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)



def test_junitresult::testsuites_is_not_abstract():
    assert not inspect.isabstract(junitresult::Testsuites)


def test_junitresult::testsuites_constructor_exists():
    assert callable(junitresult::Testsuites.__init__)


def test_junitresult::testsuites_constructor_args():
    sig = inspect.signature(junitresult::Testsuites.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "time" in params, "Missing parameter 'time'"

def test_junitresult::testsuites_has_disabled():
    assert hasattr(junitresult::Testsuites, "disabled")
    descriptor = None
    for klass in junitresult::Testsuites.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuites_has_time():
    assert hasattr(junitresult::Testsuites, "time")
    descriptor = None
    for klass in junitresult::Testsuites.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_junitresult::testsuite_is_not_abstract():
    assert not inspect.isabstract(junitresult::Testsuite)


def test_junitresult::testsuite_constructor_exists():
    assert callable(junitresult::Testsuite.__init__)


def test_junitresult::testsuite_constructor_args():
    sig = inspect.signature(junitresult::Testsuite.__init__)
    params = list(sig.parameters.keys())
    assert "system_out" in params, "Missing parameter 'system_out'"
    assert "timestamp" in params, "Missing parameter 'timestamp'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "time" in params, "Missing parameter 'time'"
    assert "hostname" in params, "Missing parameter 'hostname'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "skipped" in params, "Missing parameter 'skipped'"
    assert "package" in params, "Missing parameter 'package'"
    assert "id" in params, "Missing parameter 'id'"

def test_junitresult::testsuite_has_system_out():
    assert hasattr(junitresult::Testsuite, "system_out")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "system_out" in klass.__dict__:
            descriptor = klass.__dict__["system_out"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_timestamp():
    assert hasattr(junitresult::Testsuite, "timestamp")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "timestamp" in klass.__dict__:
            descriptor = klass.__dict__["timestamp"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_system_err():
    assert hasattr(junitresult::Testsuite, "system_err")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "system_err" in klass.__dict__:
            descriptor = klass.__dict__["system_err"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_time():
    assert hasattr(junitresult::Testsuite, "time")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_hostname():
    assert hasattr(junitresult::Testsuite, "hostname")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "hostname" in klass.__dict__:
            descriptor = klass.__dict__["hostname"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_disabled():
    assert hasattr(junitresult::Testsuite, "disabled")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_skipped():
    assert hasattr(junitresult::Testsuite, "skipped")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "skipped" in klass.__dict__:
            descriptor = klass.__dict__["skipped"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_package():
    assert hasattr(junitresult::Testsuite, "package")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testsuite_has_id():
    assert hasattr(junitresult::Testsuite, "id")
    descriptor = None
    for klass in junitresult::Testsuite.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_junitresult::error_is_not_abstract():
    assert not inspect.isabstract(junitresult::Error)


def test_junitresult::error_constructor_exists():
    assert callable(junitresult::Error.__init__)


def test_junitresult::error_constructor_args():
    sig = inspect.signature(junitresult::Error.__init__)
    params = list(sig.parameters.keys())



def test_junitresult::failure_is_not_abstract():
    assert not inspect.isabstract(junitresult::Failure)


def test_junitresult::failure_constructor_exists():
    assert callable(junitresult::Failure.__init__)


def test_junitresult::failure_constructor_args():
    sig = inspect.signature(junitresult::Failure.__init__)
    params = list(sig.parameters.keys())



def test_junitresult::skipped_is_not_abstract():
    assert not inspect.isabstract(junitresult::Skipped)


def test_junitresult::skipped_constructor_exists():
    assert callable(junitresult::Skipped.__init__)


def test_junitresult::skipped_constructor_args():
    sig = inspect.signature(junitresult::Skipped.__init__)
    params = list(sig.parameters.keys())



def test_junitresult::testcase_is_not_abstract():
    assert not inspect.isabstract(junitresult::Testcase)


def test_junitresult::testcase_constructor_exists():
    assert callable(junitresult::Testcase.__init__)


def test_junitresult::testcase_constructor_args():
    sig = inspect.signature(junitresult::Testcase.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "assertions" in params, "Missing parameter 'assertions'"
    assert "system_err" in params, "Missing parameter 'system_err'"
    assert "time" in params, "Missing parameter 'time'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "system_out" in params, "Missing parameter 'system_out'"
    assert "name" in params, "Missing parameter 'name'"

def test_junitresult::testcase_has_status():
    assert hasattr(junitresult::Testcase, "status")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_assertions():
    assert hasattr(junitresult::Testcase, "assertions")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "assertions" in klass.__dict__:
            descriptor = klass.__dict__["assertions"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_system_err():
    assert hasattr(junitresult::Testcase, "system_err")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "system_err" in klass.__dict__:
            descriptor = klass.__dict__["system_err"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_time():
    assert hasattr(junitresult::Testcase, "time")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_classname():
    assert hasattr(junitresult::Testcase, "classname")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_system_out():
    assert hasattr(junitresult::Testcase, "system_out")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "system_out" in klass.__dict__:
            descriptor = klass.__dict__["system_out"]
            break
    assert isinstance(descriptor, property)

def test_junitresult::testcase_has_name():
    assert hasattr(junitresult::Testcase, "name")
    descriptor = None
    for klass in junitresult::Testcase.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
junitresult::NegativeResult_strategy = st.builds(
    junitresult::NegativeResult,
    type=
        safe_text,
    message=
        safe_text,
    value=
        safe_text
)
NegativeResult_strategy = st.builds(
    NegativeResult,
)
junitresult::JunitResult_strategy = st.builds(
    junitresult::JunitResult,
)
JunitResult_strategy = st.builds(
    JunitResult,
)
junitresult::AbstractAggregatedTest_strategy = st.builds(
    junitresult::AbstractAggregatedTest,
    name=
        safe_text,
    failures=
        st.integers(),
    errors=
        st.integers(),
    tests=
        st.integers()
)
junitresult::Property_strategy = st.builds(
    junitresult::Property,
    value=
        safe_text,
    name=
        safe_text
)
AbstractAggregatedTest_strategy = st.builds(
    AbstractAggregatedTest,
)
junitresult::Testrun_strategy = st.builds(
    junitresult::Testrun,
    project=
        safe_text,
    ignored=
        st.integers(),
    started=
        st.integers()
)
junitresult::Testsuites_strategy = st.builds(
    junitresult::Testsuites,
    disabled=
        st.integers(),
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
junitresult::Testsuite_strategy = st.builds(
    junitresult::Testsuite,
    system_out=
        safe_text,
    timestamp=
        st.dates(),
    system_err=
        safe_text,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    hostname=
        safe_text,
    disabled=
        st.integers(),
    skipped=
        st.integers(),
    package=
        safe_text,
    id=
        st.integers()
)
junitresult::Error_strategy = st.builds(
    junitresult::Error,
)
junitresult::Failure_strategy = st.builds(
    junitresult::Failure,
)
junitresult::Skipped_strategy = st.builds(
    junitresult::Skipped,
)
junitresult::Testcase_strategy = st.builds(
    junitresult::Testcase,
    status=
        safe_text,
    assertions=
        safe_text,
    system_err=
        safe_text,
    time=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    classname=
        safe_text,
    system_out=
        safe_text,
    name=
        safe_text
)

@given(instance=junitresult::NegativeResult_strategy)
@settings(max_examples=50)
def test_junitresult::negativeresult_instantiation(instance):
    assert isinstance(instance, junitresult::NegativeResult)

@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=junitresult::NegativeResult_strategy)
def test_junitresult::negativeresult_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NegativeResult_strategy)
@settings(max_examples=50)
def test_negativeresult_instantiation(instance):
    assert isinstance(instance, NegativeResult)

@given(instance=junitresult::JunitResult_strategy)
@settings(max_examples=50)
def test_junitresult::junitresult_instantiation(instance):
    assert isinstance(instance, junitresult::JunitResult)

@given(instance=JunitResult_strategy)
@settings(max_examples=50)
def test_junitresult_instantiation(instance):
    assert isinstance(instance, JunitResult)

@given(instance=junitresult::AbstractAggregatedTest_strategy)
@settings(max_examples=50)
def test_junitresult::abstractaggregatedtest_instantiation(instance):
    assert isinstance(instance, junitresult::AbstractAggregatedTest)

@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_failures_type(instance):
    assert isinstance(instance.failures, int)


@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_failures_setter(instance):
    original = instance.failures
    instance.failures = original
    assert instance.failures == original

@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_errors_type(instance):
    assert isinstance(instance.errors, int)


@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_errors_setter(instance):
    original = instance.errors
    instance.errors = original
    assert instance.errors == original

@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_tests_type(instance):
    assert isinstance(instance.tests, int)


@given(instance=junitresult::AbstractAggregatedTest_strategy)
def test_junitresult::abstractaggregatedtest_tests_setter(instance):
    original = instance.tests
    instance.tests = original
    assert instance.tests == original

@given(instance=junitresult::Property_strategy)
@settings(max_examples=50)
def test_junitresult::property_instantiation(instance):
    assert isinstance(instance, junitresult::Property)

@given(instance=junitresult::Property_strategy)
def test_junitresult::property_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=junitresult::Property_strategy)
def test_junitresult::property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=junitresult::Property_strategy)
def test_junitresult::property_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=junitresult::Property_strategy)
def test_junitresult::property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractAggregatedTest_strategy)
@settings(max_examples=50)
def test_abstractaggregatedtest_instantiation(instance):
    assert isinstance(instance, AbstractAggregatedTest)

@given(instance=junitresult::Testrun_strategy)
@settings(max_examples=50)
def test_junitresult::testrun_instantiation(instance):
    assert isinstance(instance, junitresult::Testrun)

@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_project_type(instance):
    assert isinstance(instance.project, str)


@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_ignored_type(instance):
    assert isinstance(instance.ignored, int)


@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_ignored_setter(instance):
    original = instance.ignored
    instance.ignored = original
    assert instance.ignored == original

@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_started_type(instance):
    assert isinstance(instance.started, int)


@given(instance=junitresult::Testrun_strategy)
def test_junitresult::testrun_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original

@given(instance=junitresult::Testsuites_strategy)
@settings(max_examples=50)
def test_junitresult::testsuites_instantiation(instance):
    assert isinstance(instance, junitresult::Testsuites)

@given(instance=junitresult::Testsuites_strategy)
def test_junitresult::testsuites_disabled_type(instance):
    assert isinstance(instance.disabled, int)


@given(instance=junitresult::Testsuites_strategy)
def test_junitresult::testsuites_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=junitresult::Testsuites_strategy)
def test_junitresult::testsuites_time_type(instance):
    assert isinstance(instance.time, float)


@given(instance=junitresult::Testsuites_strategy)
def test_junitresult::testsuites_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=junitresult::Testsuite_strategy)
@settings(max_examples=50)
def test_junitresult::testsuite_instantiation(instance):
    assert isinstance(instance, junitresult::Testsuite)

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_system_out_type(instance):
    assert isinstance(instance.system_out, str)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_timestamp_type(instance):
    assert isinstance(instance.timestamp, date)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_timestamp_setter(instance):
    original = instance.timestamp
    instance.timestamp = original
    assert instance.timestamp == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_system_err_type(instance):
    assert isinstance(instance.system_err, str)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_time_type(instance):
    assert isinstance(instance.time, float)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_hostname_type(instance):
    assert isinstance(instance.hostname, str)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_hostname_setter(instance):
    original = instance.hostname
    instance.hostname = original
    assert instance.hostname == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_disabled_type(instance):
    assert isinstance(instance.disabled, int)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_skipped_type(instance):
    assert isinstance(instance.skipped, int)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_skipped_setter(instance):
    original = instance.skipped
    instance.skipped = original
    assert instance.skipped == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=junitresult::Testsuite_strategy)
def test_junitresult::testsuite_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=junitresult::Error_strategy)
@settings(max_examples=50)
def test_junitresult::error_instantiation(instance):
    assert isinstance(instance, junitresult::Error)

@given(instance=junitresult::Failure_strategy)
@settings(max_examples=50)
def test_junitresult::failure_instantiation(instance):
    assert isinstance(instance, junitresult::Failure)

@given(instance=junitresult::Skipped_strategy)
@settings(max_examples=50)
def test_junitresult::skipped_instantiation(instance):
    assert isinstance(instance, junitresult::Skipped)

@given(instance=junitresult::Testcase_strategy)
@settings(max_examples=50)
def test_junitresult::testcase_instantiation(instance):
    assert isinstance(instance, junitresult::Testcase)

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_assertions_type(instance):
    assert isinstance(instance.assertions, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_assertions_setter(instance):
    original = instance.assertions
    instance.assertions = original
    assert instance.assertions == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_system_err_type(instance):
    assert isinstance(instance.system_err, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_system_err_setter(instance):
    original = instance.system_err
    instance.system_err = original
    assert instance.system_err == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_time_type(instance):
    assert isinstance(instance.time, float)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_system_out_type(instance):
    assert isinstance(instance.system_out, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_system_out_setter(instance):
    original = instance.system_out
    instance.system_out = original
    assert instance.system_out == original

@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=junitresult::Testcase_strategy)
def test_junitresult::testcase_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
