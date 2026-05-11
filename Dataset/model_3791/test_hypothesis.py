import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TraceStackframe,
    junitmodel::JUnitTraceStackframe,
    ComparisonProblem,
    JUnitProblem,
    junitmodel::JUnitComparisonProblem,
    TestProblem,
    junitmodel::JUnitProblem,
    TestRoot,
    junitmodel::JUnitRoot,
    TestContainer,
    junitmodel::JUnitTestSuite,
    TestCaseElement,
    junitmodel::JUnitTestCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tracestackframe_is_not_abstract():
    assert not inspect.isabstract(TraceStackframe)


def test_tracestackframe_constructor_exists():
    assert callable(TraceStackframe.__init__)


def test_tracestackframe_constructor_args():
    sig = inspect.signature(TraceStackframe.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junittracestackframe_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitTraceStackframe)


def test_junitmodel::junittracestackframe_constructor_exists():
    assert callable(junitmodel::JUnitTraceStackframe.__init__)


def test_junitmodel::junittracestackframe_constructor_args():
    sig = inspect.signature(junitmodel::JUnitTraceStackframe.__init__)
    params = list(sig.parameters.keys())



def test_comparisonproblem_is_not_abstract():
    assert not inspect.isabstract(ComparisonProblem)


def test_comparisonproblem_constructor_exists():
    assert callable(ComparisonProblem.__init__)


def test_comparisonproblem_constructor_args():
    sig = inspect.signature(ComparisonProblem.__init__)
    params = list(sig.parameters.keys())



def test_junitproblem_is_not_abstract():
    assert not inspect.isabstract(JUnitProblem)


def test_junitproblem_constructor_exists():
    assert callable(JUnitProblem.__init__)


def test_junitproblem_constructor_args():
    sig = inspect.signature(JUnitProblem.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junitcomparisonproblem_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitComparisonProblem)


def test_junitmodel::junitcomparisonproblem_constructor_exists():
    assert callable(junitmodel::JUnitComparisonProblem.__init__)


def test_junitmodel::junitcomparisonproblem_constructor_args():
    sig = inspect.signature(junitmodel::JUnitComparisonProblem.__init__)
    params = list(sig.parameters.keys())



def test_testproblem_is_not_abstract():
    assert not inspect.isabstract(TestProblem)


def test_testproblem_constructor_exists():
    assert callable(TestProblem.__init__)


def test_testproblem_constructor_args():
    sig = inspect.signature(TestProblem.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junitproblem_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitProblem)


def test_junitmodel::junitproblem_constructor_exists():
    assert callable(junitmodel::JUnitProblem.__init__)


def test_junitmodel::junitproblem_constructor_args():
    sig = inspect.signature(junitmodel::JUnitProblem.__init__)
    params = list(sig.parameters.keys())
    assert "lastTraceWasFiltered" in params, "Missing parameter 'lastTraceWasFiltered'"

def test_junitmodel::junitproblem_has_lastTraceWasFiltered():
    assert hasattr(junitmodel::JUnitProblem, "lastTraceWasFiltered")
    descriptor = None
    for klass in junitmodel::JUnitProblem.__mro__:
        if "lastTraceWasFiltered" in klass.__dict__:
            descriptor = klass.__dict__["lastTraceWasFiltered"]
            break
    assert isinstance(descriptor, property)



def test_testroot_is_not_abstract():
    assert not inspect.isabstract(TestRoot)


def test_testroot_constructor_exists():
    assert callable(TestRoot.__init__)


def test_testroot_constructor_args():
    sig = inspect.signature(TestRoot.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junitroot_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitRoot)


def test_junitmodel::junitroot_constructor_exists():
    assert callable(junitmodel::JUnitRoot.__init__)


def test_junitmodel::junitroot_constructor_args():
    sig = inspect.signature(junitmodel::JUnitRoot.__init__)
    params = list(sig.parameters.keys())



def test_testcontainer_is_not_abstract():
    assert not inspect.isabstract(TestContainer)


def test_testcontainer_constructor_exists():
    assert callable(TestContainer.__init__)


def test_testcontainer_constructor_args():
    sig = inspect.signature(TestContainer.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junittestsuite_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitTestSuite)


def test_junitmodel::junittestsuite_constructor_exists():
    assert callable(junitmodel::JUnitTestSuite.__init__)


def test_junitmodel::junittestsuite_constructor_args():
    sig = inspect.signature(junitmodel::JUnitTestSuite.__init__)
    params = list(sig.parameters.keys())



def test_testcaseelement_is_not_abstract():
    assert not inspect.isabstract(TestCaseElement)


def test_testcaseelement_constructor_exists():
    assert callable(TestCaseElement.__init__)


def test_testcaseelement_constructor_args():
    sig = inspect.signature(TestCaseElement.__init__)
    params = list(sig.parameters.keys())



def test_junitmodel::junittestcase_is_not_abstract():
    assert not inspect.isabstract(junitmodel::JUnitTestCase)


def test_junitmodel::junittestcase_constructor_exists():
    assert callable(junitmodel::JUnitTestCase.__init__)


def test_junitmodel::junittestcase_constructor_args():
    sig = inspect.signature(junitmodel::JUnitTestCase.__init__)
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
TraceStackframe_strategy = st.builds(
    TraceStackframe,
)
junitmodel::JUnitTraceStackframe_strategy = st.builds(
    junitmodel::JUnitTraceStackframe,
)
ComparisonProblem_strategy = st.builds(
    ComparisonProblem,
)
JUnitProblem_strategy = st.builds(
    JUnitProblem,
)
junitmodel::JUnitComparisonProblem_strategy = st.builds(
    junitmodel::JUnitComparisonProblem,
)
TestProblem_strategy = st.builds(
    TestProblem,
)
junitmodel::JUnitProblem_strategy = st.builds(
    junitmodel::JUnitProblem,
    lastTraceWasFiltered=
        st.booleans()
)
TestRoot_strategy = st.builds(
    TestRoot,
)
junitmodel::JUnitRoot_strategy = st.builds(
    junitmodel::JUnitRoot,
)
TestContainer_strategy = st.builds(
    TestContainer,
)
junitmodel::JUnitTestSuite_strategy = st.builds(
    junitmodel::JUnitTestSuite,
)
TestCaseElement_strategy = st.builds(
    TestCaseElement,
)
junitmodel::JUnitTestCase_strategy = st.builds(
    junitmodel::JUnitTestCase,
)

@given(instance=TraceStackframe_strategy)
@settings(max_examples=50)
def test_tracestackframe_instantiation(instance):
    assert isinstance(instance, TraceStackframe)

@given(instance=junitmodel::JUnitTraceStackframe_strategy)
@settings(max_examples=50)
def test_junitmodel::junittracestackframe_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitTraceStackframe)

@given(instance=ComparisonProblem_strategy)
@settings(max_examples=50)
def test_comparisonproblem_instantiation(instance):
    assert isinstance(instance, ComparisonProblem)

@given(instance=JUnitProblem_strategy)
@settings(max_examples=50)
def test_junitproblem_instantiation(instance):
    assert isinstance(instance, JUnitProblem)

@given(instance=junitmodel::JUnitComparisonProblem_strategy)
@settings(max_examples=50)
def test_junitmodel::junitcomparisonproblem_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitComparisonProblem)

@given(instance=TestProblem_strategy)
@settings(max_examples=50)
def test_testproblem_instantiation(instance):
    assert isinstance(instance, TestProblem)

@given(instance=junitmodel::JUnitProblem_strategy)
@settings(max_examples=50)
def test_junitmodel::junitproblem_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitProblem)

@given(instance=junitmodel::JUnitProblem_strategy)
def test_junitmodel::junitproblem_lastTraceWasFiltered_type(instance):
    assert isinstance(instance.lastTraceWasFiltered, bool)


@given(instance=junitmodel::JUnitProblem_strategy)
def test_junitmodel::junitproblem_lastTraceWasFiltered_setter(instance):
    original = instance.lastTraceWasFiltered
    instance.lastTraceWasFiltered = original
    assert instance.lastTraceWasFiltered == original

@given(instance=TestRoot_strategy)
@settings(max_examples=50)
def test_testroot_instantiation(instance):
    assert isinstance(instance, TestRoot)

@given(instance=junitmodel::JUnitRoot_strategy)
@settings(max_examples=50)
def test_junitmodel::junitroot_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitRoot)

@given(instance=TestContainer_strategy)
@settings(max_examples=50)
def test_testcontainer_instantiation(instance):
    assert isinstance(instance, TestContainer)

@given(instance=junitmodel::JUnitTestSuite_strategy)
@settings(max_examples=50)
def test_junitmodel::junittestsuite_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitTestSuite)

@given(instance=TestCaseElement_strategy)
@settings(max_examples=50)
def test_testcaseelement_instantiation(instance):
    assert isinstance(instance, TestCaseElement)

@given(instance=junitmodel::JUnitTestCase_strategy)
@settings(max_examples=50)
def test_junitmodel::junittestcase_instantiation(instance):
    assert isinstance(instance, junitmodel::JUnitTestCase)
