import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    Login_admin_UseCase,
    Input_data_kerusakan_UseCase,
    Cetak_SPK_UseCase,
    Mekanik_UseCase,
    laporan_service_UseCase,
    Input_data_service_UseCase,
    Input_data_mekanik_UseCase,
    Input_data_kendaraan_UseCase,
    Input_data_pengemudi_UseCase,
    Admin_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_login_admin_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_admin_UseCase)


def test_login_admin_usecase_constructor_exists():
    assert callable(Login_admin_UseCase.__init__)


def test_login_admin_usecase_constructor_args():
    sig = inspect.signature(Login_admin_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_input_data_kerusakan_usecase_is_not_abstract():
    assert not inspect.isabstract(Input_data_kerusakan_UseCase)


def test_input_data_kerusakan_usecase_constructor_exists():
    assert callable(Input_data_kerusakan_UseCase.__init__)


def test_input_data_kerusakan_usecase_constructor_args():
    sig = inspect.signature(Input_data_kerusakan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cetak_spk_usecase_is_not_abstract():
    assert not inspect.isabstract(Cetak_SPK_UseCase)


def test_cetak_spk_usecase_constructor_exists():
    assert callable(Cetak_SPK_UseCase.__init__)


def test_cetak_spk_usecase_constructor_args():
    sig = inspect.signature(Cetak_SPK_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_mekanik_usecase_is_not_abstract():
    assert not inspect.isabstract(Mekanik_UseCase)


def test_mekanik_usecase_constructor_exists():
    assert callable(Mekanik_UseCase.__init__)


def test_mekanik_usecase_constructor_args():
    sig = inspect.signature(Mekanik_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_laporan_service_usecase_is_not_abstract():
    assert not inspect.isabstract(laporan_service_UseCase)


def test_laporan_service_usecase_constructor_exists():
    assert callable(laporan_service_UseCase.__init__)


def test_laporan_service_usecase_constructor_args():
    sig = inspect.signature(laporan_service_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_input_data_service_usecase_is_not_abstract():
    assert not inspect.isabstract(Input_data_service_UseCase)


def test_input_data_service_usecase_constructor_exists():
    assert callable(Input_data_service_UseCase.__init__)


def test_input_data_service_usecase_constructor_args():
    sig = inspect.signature(Input_data_service_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_input_data_mekanik_usecase_is_not_abstract():
    assert not inspect.isabstract(Input_data_mekanik_UseCase)


def test_input_data_mekanik_usecase_constructor_exists():
    assert callable(Input_data_mekanik_UseCase.__init__)


def test_input_data_mekanik_usecase_constructor_args():
    sig = inspect.signature(Input_data_mekanik_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_input_data_kendaraan_usecase_is_not_abstract():
    assert not inspect.isabstract(Input_data_kendaraan_UseCase)


def test_input_data_kendaraan_usecase_constructor_exists():
    assert callable(Input_data_kendaraan_UseCase.__init__)


def test_input_data_kendaraan_usecase_constructor_args():
    sig = inspect.signature(Input_data_kendaraan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_input_data_pengemudi_usecase_is_not_abstract():
    assert not inspect.isabstract(Input_data_pengemudi_UseCase)


def test_input_data_pengemudi_usecase_constructor_exists():
    assert callable(Input_data_pengemudi_UseCase.__init__)


def test_input_data_pengemudi_usecase_constructor_args():
    sig = inspect.signature(Input_data_pengemudi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
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
Class_strategy = st.builds(
    Class,
)
Login_admin_UseCase_strategy = st.builds(
    Login_admin_UseCase,
)
Input_data_kerusakan_UseCase_strategy = st.builds(
    Input_data_kerusakan_UseCase,
)
Cetak_SPK_UseCase_strategy = st.builds(
    Cetak_SPK_UseCase,
)
Mekanik_UseCase_strategy = st.builds(
    Mekanik_UseCase,
)
laporan_service_UseCase_strategy = st.builds(
    laporan_service_UseCase,
)
Input_data_service_UseCase_strategy = st.builds(
    Input_data_service_UseCase,
)
Input_data_mekanik_UseCase_strategy = st.builds(
    Input_data_mekanik_UseCase,
)
Input_data_kendaraan_UseCase_strategy = st.builds(
    Input_data_kendaraan_UseCase,
)
Input_data_pengemudi_UseCase_strategy = st.builds(
    Input_data_pengemudi_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Login_admin_UseCase_strategy)
@settings(max_examples=50)
def test_login_admin_usecase_instantiation(instance):
    assert isinstance(instance, Login_admin_UseCase)

@given(instance=Input_data_kerusakan_UseCase_strategy)
@settings(max_examples=50)
def test_input_data_kerusakan_usecase_instantiation(instance):
    assert isinstance(instance, Input_data_kerusakan_UseCase)

@given(instance=Cetak_SPK_UseCase_strategy)
@settings(max_examples=50)
def test_cetak_spk_usecase_instantiation(instance):
    assert isinstance(instance, Cetak_SPK_UseCase)

@given(instance=Mekanik_UseCase_strategy)
@settings(max_examples=50)
def test_mekanik_usecase_instantiation(instance):
    assert isinstance(instance, Mekanik_UseCase)

@given(instance=laporan_service_UseCase_strategy)
@settings(max_examples=50)
def test_laporan_service_usecase_instantiation(instance):
    assert isinstance(instance, laporan_service_UseCase)

@given(instance=Input_data_service_UseCase_strategy)
@settings(max_examples=50)
def test_input_data_service_usecase_instantiation(instance):
    assert isinstance(instance, Input_data_service_UseCase)

@given(instance=Input_data_mekanik_UseCase_strategy)
@settings(max_examples=50)
def test_input_data_mekanik_usecase_instantiation(instance):
    assert isinstance(instance, Input_data_mekanik_UseCase)

@given(instance=Input_data_kendaraan_UseCase_strategy)
@settings(max_examples=50)
def test_input_data_kendaraan_usecase_instantiation(instance):
    assert isinstance(instance, Input_data_kendaraan_UseCase)

@given(instance=Input_data_pengemudi_UseCase_strategy)
@settings(max_examples=50)
def test_input_data_pengemudi_usecase_instantiation(instance):
    assert isinstance(instance, Input_data_pengemudi_UseCase)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)
