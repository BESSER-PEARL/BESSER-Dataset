import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MessageQueue,
    ReportResult,
    JobReport,
    Report,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_messagequeue_is_not_abstract():
    assert not inspect.isabstract(MessageQueue)


def test_messagequeue_constructor_exists():
    assert callable(MessageQueue.__init__)


def test_messagequeue_constructor_args():
    sig = inspect.signature(MessageQueue.__init__)
    params = list(sig.parameters.keys())



def test_reportresult_is_not_abstract():
    assert not inspect.isabstract(ReportResult)


def test_reportresult_constructor_exists():
    assert callable(ReportResult.__init__)


def test_reportresult_constructor_args():
    sig = inspect.signature(ReportResult.__init__)
    params = list(sig.parameters.keys())



def test_jobreport_is_not_abstract():
    assert not inspect.isabstract(JobReport)


def test_jobreport_constructor_exists():
    assert callable(JobReport.__init__)


def test_jobreport_constructor_args():
    sig = inspect.signature(JobReport.__init__)
    params = list(sig.parameters.keys())



def test_report_is_not_abstract():
    assert not inspect.isabstract(Report)


def test_report_constructor_exists():
    assert callable(Report.__init__)


def test_report_constructor_args():
    sig = inspect.signature(Report.__init__)
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
MessageQueue_strategy = st.builds(
    MessageQueue,
)
ReportResult_strategy = st.builds(
    ReportResult,
)
JobReport_strategy = st.builds(
    JobReport,
)
Report_strategy = st.builds(
    Report,
)

@given(instance=MessageQueue_strategy)
@settings(max_examples=50)
def test_messagequeue_instantiation(instance):
    assert isinstance(instance, MessageQueue)

@given(instance=ReportResult_strategy)
@settings(max_examples=50)
def test_reportresult_instantiation(instance):
    assert isinstance(instance, ReportResult)

@given(instance=JobReport_strategy)
@settings(max_examples=50)
def test_jobreport_instantiation(instance):
    assert isinstance(instance, JobReport)

@given(instance=Report_strategy)
@settings(max_examples=50)
def test_report_instantiation(instance):
    assert isinstance(instance, Report)
