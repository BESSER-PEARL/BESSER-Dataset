import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    amazoninformational::Payment,
    amazoninformational::Product,
    amazoninformational::Order,
    amazoninformational::Package,
    amazoninformational::Invoice,
    amazoninformational::Shipment,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_amazoninformational::payment_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Payment)


def test_amazoninformational::payment_constructor_exists():
    assert callable(amazoninformational::Payment.__init__)


def test_amazoninformational::payment_constructor_args():
    sig = inspect.signature(amazoninformational::Payment.__init__)
    params = list(sig.parameters.keys())



def test_amazoninformational::product_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Product)


def test_amazoninformational::product_constructor_exists():
    assert callable(amazoninformational::Product.__init__)


def test_amazoninformational::product_constructor_args():
    sig = inspect.signature(amazoninformational::Product.__init__)
    params = list(sig.parameters.keys())
    assert "onHand" in params, "Missing parameter 'onHand'"

def test_amazoninformational::product_has_onHand():
    assert hasattr(amazoninformational::Product, "onHand")
    descriptor = None
    for klass in amazoninformational::Product.__mro__:
        if "onHand" in klass.__dict__:
            descriptor = klass.__dict__["onHand"]
            break
    assert isinstance(descriptor, property)



def test_amazoninformational::order_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Order)


def test_amazoninformational::order_constructor_exists():
    assert callable(amazoninformational::Order.__init__)


def test_amazoninformational::order_constructor_args():
    sig = inspect.signature(amazoninformational::Order.__init__)
    params = list(sig.parameters.keys())



def test_amazoninformational::package_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Package)


def test_amazoninformational::package_constructor_exists():
    assert callable(amazoninformational::Package.__init__)


def test_amazoninformational::package_constructor_args():
    sig = inspect.signature(amazoninformational::Package.__init__)
    params = list(sig.parameters.keys())



def test_amazoninformational::invoice_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Invoice)


def test_amazoninformational::invoice_constructor_exists():
    assert callable(amazoninformational::Invoice.__init__)


def test_amazoninformational::invoice_constructor_args():
    sig = inspect.signature(amazoninformational::Invoice.__init__)
    params = list(sig.parameters.keys())



def test_amazoninformational::shipment_is_not_abstract():
    assert not inspect.isabstract(amazoninformational::Shipment)


def test_amazoninformational::shipment_constructor_exists():
    assert callable(amazoninformational::Shipment.__init__)


def test_amazoninformational::shipment_constructor_args():
    sig = inspect.signature(amazoninformational::Shipment.__init__)
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
amazoninformational::Payment_strategy = st.builds(
    amazoninformational::Payment,
)
amazoninformational::Product_strategy = st.builds(
    amazoninformational::Product,
    onHand=
        st.integers()
)
amazoninformational::Order_strategy = st.builds(
    amazoninformational::Order,
)
amazoninformational::Package_strategy = st.builds(
    amazoninformational::Package,
)
amazoninformational::Invoice_strategy = st.builds(
    amazoninformational::Invoice,
)
amazoninformational::Shipment_strategy = st.builds(
    amazoninformational::Shipment,
)

@given(instance=amazoninformational::Payment_strategy)
@settings(max_examples=50)
def test_amazoninformational::payment_instantiation(instance):
    assert isinstance(instance, amazoninformational::Payment)

@given(instance=amazoninformational::Product_strategy)
@settings(max_examples=50)
def test_amazoninformational::product_instantiation(instance):
    assert isinstance(instance, amazoninformational::Product)

@given(instance=amazoninformational::Product_strategy)
def test_amazoninformational::product_onHand_type(instance):
    assert isinstance(instance.onHand, int)


@given(instance=amazoninformational::Product_strategy)
def test_amazoninformational::product_onHand_setter(instance):
    original = instance.onHand
    instance.onHand = original
    assert instance.onHand == original

@given(instance=amazoninformational::Order_strategy)
@settings(max_examples=50)
def test_amazoninformational::order_instantiation(instance):
    assert isinstance(instance, amazoninformational::Order)

@given(instance=amazoninformational::Package_strategy)
@settings(max_examples=50)
def test_amazoninformational::package_instantiation(instance):
    assert isinstance(instance, amazoninformational::Package)

@given(instance=amazoninformational::Invoice_strategy)
@settings(max_examples=50)
def test_amazoninformational::invoice_instantiation(instance):
    assert isinstance(instance, amazoninformational::Invoice)

@given(instance=amazoninformational::Shipment_strategy)
@settings(max_examples=50)
def test_amazoninformational::shipment_instantiation(instance):
    assert isinstance(instance, amazoninformational::Shipment)
