import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    To_Author,
    From_Author,
    message,
    Deleted,
    Sent,
    Inbox,
    View_Patient_Clinical_info_UseCase,
    Update_Patient_Mental_Info_UseCase,
    View_Patient_Mental_Info_UseCase,
    Doctor_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_to_author_is_not_abstract():
    assert not inspect.isabstract(To_Author)


def test_to_author_constructor_exists():
    assert callable(To_Author.__init__)


def test_to_author_constructor_args():
    sig = inspect.signature(To_Author.__init__)
    params = list(sig.parameters.keys())



def test_from_author_is_not_abstract():
    assert not inspect.isabstract(From_Author)


def test_from_author_constructor_exists():
    assert callable(From_Author.__init__)


def test_from_author_constructor_args():
    sig = inspect.signature(From_Author.__init__)
    params = list(sig.parameters.keys())



def test_message_is_not_abstract():
    assert not inspect.isabstract(message)


def test_message_constructor_exists():
    assert callable(message.__init__)


def test_message_constructor_args():
    sig = inspect.signature(message.__init__)
    params = list(sig.parameters.keys())



def test_deleted_is_not_abstract():
    assert not inspect.isabstract(Deleted)


def test_deleted_constructor_exists():
    assert callable(Deleted.__init__)


def test_deleted_constructor_args():
    sig = inspect.signature(Deleted.__init__)
    params = list(sig.parameters.keys())



def test_sent_is_not_abstract():
    assert not inspect.isabstract(Sent)


def test_sent_constructor_exists():
    assert callable(Sent.__init__)


def test_sent_constructor_args():
    sig = inspect.signature(Sent.__init__)
    params = list(sig.parameters.keys())



def test_inbox_is_not_abstract():
    assert not inspect.isabstract(Inbox)


def test_inbox_constructor_exists():
    assert callable(Inbox.__init__)


def test_inbox_constructor_args():
    sig = inspect.signature(Inbox.__init__)
    params = list(sig.parameters.keys())



def test_view_patient_clinical_info_usecase_is_not_abstract():
    assert not inspect.isabstract(View_Patient_Clinical_info_UseCase)


def test_view_patient_clinical_info_usecase_constructor_exists():
    assert callable(View_Patient_Clinical_info_UseCase.__init__)


def test_view_patient_clinical_info_usecase_constructor_args():
    sig = inspect.signature(View_Patient_Clinical_info_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_update_patient_mental_info_usecase_is_not_abstract():
    assert not inspect.isabstract(Update_Patient_Mental_Info_UseCase)


def test_update_patient_mental_info_usecase_constructor_exists():
    assert callable(Update_Patient_Mental_Info_UseCase.__init__)


def test_update_patient_mental_info_usecase_constructor_args():
    sig = inspect.signature(Update_Patient_Mental_Info_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_view_patient_mental_info_usecase_is_not_abstract():
    assert not inspect.isabstract(View_Patient_Mental_Info_UseCase)


def test_view_patient_mental_info_usecase_constructor_exists():
    assert callable(View_Patient_Mental_Info_UseCase.__init__)


def test_view_patient_mental_info_usecase_constructor_args():
    sig = inspect.signature(View_Patient_Mental_Info_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_doctor_actor_is_not_abstract():
    assert not inspect.isabstract(Doctor_Actor)


def test_doctor_actor_constructor_exists():
    assert callable(Doctor_Actor.__init__)


def test_doctor_actor_constructor_args():
    sig = inspect.signature(Doctor_Actor.__init__)
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
To_Author_strategy = st.builds(
    To_Author,
)
From_Author_strategy = st.builds(
    From_Author,
)
message_strategy = st.builds(
    message,
)
Deleted_strategy = st.builds(
    Deleted,
)
Sent_strategy = st.builds(
    Sent,
)
Inbox_strategy = st.builds(
    Inbox,
)
View_Patient_Clinical_info_UseCase_strategy = st.builds(
    View_Patient_Clinical_info_UseCase,
)
Update_Patient_Mental_Info_UseCase_strategy = st.builds(
    Update_Patient_Mental_Info_UseCase,
)
View_Patient_Mental_Info_UseCase_strategy = st.builds(
    View_Patient_Mental_Info_UseCase,
)
Doctor_Actor_strategy = st.builds(
    Doctor_Actor,
)

@given(instance=To_Author_strategy)
@settings(max_examples=50)
def test_to_author_instantiation(instance):
    assert isinstance(instance, To_Author)

@given(instance=From_Author_strategy)
@settings(max_examples=50)
def test_from_author_instantiation(instance):
    assert isinstance(instance, From_Author)

@given(instance=message_strategy)
@settings(max_examples=50)
def test_message_instantiation(instance):
    assert isinstance(instance, message)

@given(instance=Deleted_strategy)
@settings(max_examples=50)
def test_deleted_instantiation(instance):
    assert isinstance(instance, Deleted)

@given(instance=Sent_strategy)
@settings(max_examples=50)
def test_sent_instantiation(instance):
    assert isinstance(instance, Sent)

@given(instance=Inbox_strategy)
@settings(max_examples=50)
def test_inbox_instantiation(instance):
    assert isinstance(instance, Inbox)

@given(instance=View_Patient_Clinical_info_UseCase_strategy)
@settings(max_examples=50)
def test_view_patient_clinical_info_usecase_instantiation(instance):
    assert isinstance(instance, View_Patient_Clinical_info_UseCase)

@given(instance=Update_Patient_Mental_Info_UseCase_strategy)
@settings(max_examples=50)
def test_update_patient_mental_info_usecase_instantiation(instance):
    assert isinstance(instance, Update_Patient_Mental_Info_UseCase)

@given(instance=View_Patient_Mental_Info_UseCase_strategy)
@settings(max_examples=50)
def test_view_patient_mental_info_usecase_instantiation(instance):
    assert isinstance(instance, View_Patient_Mental_Info_UseCase)

@given(instance=Doctor_Actor_strategy)
@settings(max_examples=50)
def test_doctor_actor_instantiation(instance):
    assert isinstance(instance, Doctor_Actor)
