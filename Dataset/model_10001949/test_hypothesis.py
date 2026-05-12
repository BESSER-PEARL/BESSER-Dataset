import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ServiceProviderImpl,
    FiberTailProviderImpl,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_serviceproviderimpl_is_not_abstract():
    assert not inspect.isabstract(ServiceProviderImpl)


def test_serviceproviderimpl_constructor_exists():
    assert callable(ServiceProviderImpl.__init__)


def test_serviceproviderimpl_constructor_args():
    sig = inspect.signature(ServiceProviderImpl.__init__)
    params = list(sig.parameters.keys())



def test_fibertailproviderimpl_is_not_abstract():
    assert not inspect.isabstract(FiberTailProviderImpl)


def test_fibertailproviderimpl_constructor_exists():
    assert callable(FiberTailProviderImpl.__init__)


def test_fibertailproviderimpl_constructor_args():
    sig = inspect.signature(FiberTailProviderImpl.__init__)
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
ServiceProviderImpl_strategy = st.builds(
    ServiceProviderImpl,
)
FiberTailProviderImpl_strategy = st.builds(
    FiberTailProviderImpl,
)

@given(instance=ServiceProviderImpl_strategy)
@settings(max_examples=50)
def test_serviceproviderimpl_instantiation(instance):
    assert isinstance(instance, ServiceProviderImpl)

@given(instance=FiberTailProviderImpl_strategy)
@settings(max_examples=50)
def test_fibertailproviderimpl_instantiation(instance):
    assert isinstance(instance, FiberTailProviderImpl)
