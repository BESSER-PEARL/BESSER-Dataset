import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Withdraw_Cash_Dispense_the_cash_UseCase,
    Withdraw_Cash_Display_error_else_UseCase,
    Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase,
    Withdraw_Cash__Verify_check_the_available_balance_UseCase,
    Withdraw_Cash_Display_amount_UseCase,
    Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase,
    Withdraw_Cash_Display_MENU_ATM__UseCase,
    Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase,
    Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase,
    Withdraw_Cash_Verify_the_PIN_UseCase,
    Withdraw_Cash__Verify_the_card___UseCase,
    Withdraw_Cash_Display_the_PIN_screen_UseCase,
    Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase,
    Withdraw_Cash__Block_the_card_UseCase,
    Withdraw_Cash__15____Take_print_out_UseCase,
    Withdraw_Cash_Collect_Cash_UseCase,
    Withdraw_Cash_Enter_Amount_UseCase,
    Withdraw_Cash_Select_Account_UseCase,
    Withdraw_Cash_Withdraw_Cash_UseCase,
    Withdraw_Cash__Display_MENU_ATM___UseCase,
    Withdraw_Cash__Enter_the_PIN_UseCase,
    Withdraw_Cash_Insert_the_Card____UseCase,
    Withdraw_Cash_Go_to_ATM_UseCase,
    Withdraw_Cash_Bank_Server_Actor,
    Withdraw_Cash_Customer_Actor,
    Withdraw_Cash_Interface_Interface,
    ATM_transactions,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_withdraw_cash_dispense_the_cash_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Dispense_the_cash_UseCase)


def test_withdraw_cash_dispense_the_cash_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Dispense_the_cash_UseCase.__init__)


def test_withdraw_cash_dispense_the_cash_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Dispense_the_cash_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_error_else_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_error_else_UseCase)


def test_withdraw_cash_display_error_else_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_error_else_UseCase.__init__)


def test_withdraw_cash_display_error_else_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_error_else_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__if_the_balance_is_insufficient_then_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase)


def test_withdraw_cash__if_the_balance_is_insufficient_then_usecase_constructor_exists():
    assert callable(Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase.__init__)


def test_withdraw_cash__if_the_balance_is_insufficient_then_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__verify_check_the_available_balance_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__Verify_check_the_available_balance_UseCase)


def test_withdraw_cash__verify_check_the_available_balance_usecase_constructor_exists():
    assert callable(Withdraw_Cash__Verify_check_the_available_balance_UseCase.__init__)


def test_withdraw_cash__verify_check_the_available_balance_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__Verify_check_the_available_balance_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_amount_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_amount_UseCase)


def test_withdraw_cash_display_amount_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_amount_UseCase.__init__)


def test_withdraw_cash_display_amount_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_amount_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_the_account_type__saving_checking__usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase)


def test_withdraw_cash_display_the_account_type__saving_checking__usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase.__init__)


def test_withdraw_cash_display_the_account_type__saving_checking__usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_menu_atm__usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_MENU_ATM__UseCase)


def test_withdraw_cash_display_menu_atm__usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_MENU_ATM__UseCase.__init__)


def test_withdraw_cash_display_menu_atm__usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_MENU_ATM__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash___if_more_than_3_attempts_for_wrong_pin_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase)


def test_withdraw_cash___if_more_than_3_attempts_for_wrong_pin_usecase_constructor_exists():
    assert callable(Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase.__init__)


def test_withdraw_cash___if_more_than_3_attempts_for_wrong_pin_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_error_if_the_pin_is_invalid_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase)


def test_withdraw_cash_display_error_if_the_pin_is_invalid_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase.__init__)


def test_withdraw_cash_display_error_if_the_pin_is_invalid_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_verify_the_pin_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Verify_the_PIN_UseCase)


def test_withdraw_cash_verify_the_pin_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Verify_the_PIN_UseCase.__init__)


def test_withdraw_cash_verify_the_pin_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Verify_the_PIN_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__verify_the_card___usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__Verify_the_card___UseCase)


def test_withdraw_cash__verify_the_card___usecase_constructor_exists():
    assert callable(Withdraw_Cash__Verify_the_card___UseCase.__init__)


def test_withdraw_cash__verify_the_card___usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__Verify_the_card___UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_the_pin_screen_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_the_PIN_screen_UseCase)


def test_withdraw_cash_display_the_pin_screen_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_the_PIN_screen_UseCase.__init__)


def test_withdraw_cash_display_the_pin_screen_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_the_PIN_screen_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_display_error_if_the_card_is_invalid_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase)


def test_withdraw_cash_display_error_if_the_card_is_invalid_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase.__init__)


def test_withdraw_cash_display_error_if_the_card_is_invalid_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__block_the_card_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__Block_the_card_UseCase)


def test_withdraw_cash__block_the_card_usecase_constructor_exists():
    assert callable(Withdraw_Cash__Block_the_card_UseCase.__init__)


def test_withdraw_cash__block_the_card_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__Block_the_card_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__15____take_print_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__15____Take_print_out_UseCase)


def test_withdraw_cash__15____take_print_out_usecase_constructor_exists():
    assert callable(Withdraw_Cash__15____Take_print_out_UseCase.__init__)


def test_withdraw_cash__15____take_print_out_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__15____Take_print_out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_collect_cash_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Collect_Cash_UseCase)


def test_withdraw_cash_collect_cash_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Collect_Cash_UseCase.__init__)


def test_withdraw_cash_collect_cash_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Collect_Cash_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_enter_amount_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Enter_Amount_UseCase)


def test_withdraw_cash_enter_amount_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Enter_Amount_UseCase.__init__)


def test_withdraw_cash_enter_amount_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Enter_Amount_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_select_account_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Select_Account_UseCase)


def test_withdraw_cash_select_account_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Select_Account_UseCase.__init__)


def test_withdraw_cash_select_account_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Select_Account_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_withdraw_cash_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Withdraw_Cash_UseCase)


def test_withdraw_cash_withdraw_cash_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Withdraw_Cash_UseCase.__init__)


def test_withdraw_cash_withdraw_cash_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Withdraw_Cash_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__display_menu_atm___usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__Display_MENU_ATM___UseCase)


def test_withdraw_cash__display_menu_atm___usecase_constructor_exists():
    assert callable(Withdraw_Cash__Display_MENU_ATM___UseCase.__init__)


def test_withdraw_cash__display_menu_atm___usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__Display_MENU_ATM___UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash__enter_the_pin_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash__Enter_the_PIN_UseCase)


def test_withdraw_cash__enter_the_pin_usecase_constructor_exists():
    assert callable(Withdraw_Cash__Enter_the_PIN_UseCase.__init__)


def test_withdraw_cash__enter_the_pin_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash__Enter_the_PIN_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_insert_the_card____usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Insert_the_Card____UseCase)


def test_withdraw_cash_insert_the_card____usecase_constructor_exists():
    assert callable(Withdraw_Cash_Insert_the_Card____UseCase.__init__)


def test_withdraw_cash_insert_the_card____usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Insert_the_Card____UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_go_to_atm_usecase_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Go_to_ATM_UseCase)


def test_withdraw_cash_go_to_atm_usecase_constructor_exists():
    assert callable(Withdraw_Cash_Go_to_ATM_UseCase.__init__)


def test_withdraw_cash_go_to_atm_usecase_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Go_to_ATM_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_bank_server_actor_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Bank_Server_Actor)


def test_withdraw_cash_bank_server_actor_constructor_exists():
    assert callable(Withdraw_Cash_Bank_Server_Actor.__init__)


def test_withdraw_cash_bank_server_actor_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Bank_Server_Actor.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_customer_actor_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Customer_Actor)


def test_withdraw_cash_customer_actor_constructor_exists():
    assert callable(Withdraw_Cash_Customer_Actor.__init__)


def test_withdraw_cash_customer_actor_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Customer_Actor.__init__)
    params = list(sig.parameters.keys())



def test_withdraw_cash_interface_interface_is_not_abstract():
    assert not inspect.isabstract(Withdraw_Cash_Interface_Interface)


def test_withdraw_cash_interface_interface_constructor_exists():
    assert callable(Withdraw_Cash_Interface_Interface.__init__)


def test_withdraw_cash_interface_interface_constructor_args():
    sig = inspect.signature(Withdraw_Cash_Interface_Interface.__init__)
    params = list(sig.parameters.keys())



def test_atm_transactions_is_not_abstract():
    assert not inspect.isabstract(ATM_transactions)


def test_atm_transactions_constructor_exists():
    assert callable(ATM_transactions.__init__)


def test_atm_transactions_constructor_args():
    sig = inspect.signature(ATM_transactions.__init__)
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
Withdraw_Cash_Dispense_the_cash_UseCase_strategy = st.builds(
    Withdraw_Cash_Dispense_the_cash_UseCase,
)
Withdraw_Cash_Display_error_else_UseCase_strategy = st.builds(
    Withdraw_Cash_Display_error_else_UseCase,
)
Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase_strategy = st.builds(
    Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase,
)
Withdraw_Cash__Verify_check_the_available_balance_UseCase_strategy = st.builds(
    Withdraw_Cash__Verify_check_the_available_balance_UseCase,
)
Withdraw_Cash_Display_amount_UseCase_strategy = st.builds(
    Withdraw_Cash_Display_amount_UseCase,
)
Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase_strategy = st.builds(
    Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase,
)
Withdraw_Cash_Display_MENU_ATM__UseCase_strategy = st.builds(
    Withdraw_Cash_Display_MENU_ATM__UseCase,
)
Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase_strategy = st.builds(
    Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase,
)
Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase_strategy = st.builds(
    Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase,
)
Withdraw_Cash_Verify_the_PIN_UseCase_strategy = st.builds(
    Withdraw_Cash_Verify_the_PIN_UseCase,
)
Withdraw_Cash__Verify_the_card___UseCase_strategy = st.builds(
    Withdraw_Cash__Verify_the_card___UseCase,
)
Withdraw_Cash_Display_the_PIN_screen_UseCase_strategy = st.builds(
    Withdraw_Cash_Display_the_PIN_screen_UseCase,
)
Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase_strategy = st.builds(
    Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase,
)
Withdraw_Cash__Block_the_card_UseCase_strategy = st.builds(
    Withdraw_Cash__Block_the_card_UseCase,
)
Withdraw_Cash__15____Take_print_out_UseCase_strategy = st.builds(
    Withdraw_Cash__15____Take_print_out_UseCase,
)
Withdraw_Cash_Collect_Cash_UseCase_strategy = st.builds(
    Withdraw_Cash_Collect_Cash_UseCase,
)
Withdraw_Cash_Enter_Amount_UseCase_strategy = st.builds(
    Withdraw_Cash_Enter_Amount_UseCase,
)
Withdraw_Cash_Select_Account_UseCase_strategy = st.builds(
    Withdraw_Cash_Select_Account_UseCase,
)
Withdraw_Cash_Withdraw_Cash_UseCase_strategy = st.builds(
    Withdraw_Cash_Withdraw_Cash_UseCase,
)
Withdraw_Cash__Display_MENU_ATM___UseCase_strategy = st.builds(
    Withdraw_Cash__Display_MENU_ATM___UseCase,
)
Withdraw_Cash__Enter_the_PIN_UseCase_strategy = st.builds(
    Withdraw_Cash__Enter_the_PIN_UseCase,
)
Withdraw_Cash_Insert_the_Card____UseCase_strategy = st.builds(
    Withdraw_Cash_Insert_the_Card____UseCase,
)
Withdraw_Cash_Go_to_ATM_UseCase_strategy = st.builds(
    Withdraw_Cash_Go_to_ATM_UseCase,
)
Withdraw_Cash_Bank_Server_Actor_strategy = st.builds(
    Withdraw_Cash_Bank_Server_Actor,
)
Withdraw_Cash_Customer_Actor_strategy = st.builds(
    Withdraw_Cash_Customer_Actor,
)
Withdraw_Cash_Interface_Interface_strategy = st.builds(
    Withdraw_Cash_Interface_Interface,
)
ATM_transactions_strategy = st.builds(
    ATM_transactions,
)

@given(instance=Withdraw_Cash_Dispense_the_cash_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_dispense_the_cash_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Dispense_the_cash_UseCase)

@given(instance=Withdraw_Cash_Display_error_else_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_error_else_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_error_else_UseCase)

@given(instance=Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__if_the_balance_is_insufficient_then_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__If_the_balance_is_insufficient_then_UseCase)

@given(instance=Withdraw_Cash__Verify_check_the_available_balance_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__verify_check_the_available_balance_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__Verify_check_the_available_balance_UseCase)

@given(instance=Withdraw_Cash_Display_amount_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_amount_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_amount_UseCase)

@given(instance=Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_the_account_type__saving_checking__usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_the_account_Type__Saving_checking__UseCase)

@given(instance=Withdraw_Cash_Display_MENU_ATM__UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_menu_atm__usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_MENU_ATM__UseCase)

@given(instance=Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash___if_more_than_3_attempts_for_wrong_pin_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash___If_more_than_3_attempts_for_wrong_PIN_UseCase)

@given(instance=Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_error_if_the_pin_is_invalid_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_error_if_the_PIN_is_invalid_UseCase)

@given(instance=Withdraw_Cash_Verify_the_PIN_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_verify_the_pin_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Verify_the_PIN_UseCase)

@given(instance=Withdraw_Cash__Verify_the_card___UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__verify_the_card___usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__Verify_the_card___UseCase)

@given(instance=Withdraw_Cash_Display_the_PIN_screen_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_the_pin_screen_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_the_PIN_screen_UseCase)

@given(instance=Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_display_error_if_the_card_is_invalid_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Display_error_if_the_card_is_invalid_UseCase)

@given(instance=Withdraw_Cash__Block_the_card_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__block_the_card_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__Block_the_card_UseCase)

@given(instance=Withdraw_Cash__15____Take_print_out_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__15____take_print_out_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__15____Take_print_out_UseCase)

@given(instance=Withdraw_Cash_Collect_Cash_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_collect_cash_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Collect_Cash_UseCase)

@given(instance=Withdraw_Cash_Enter_Amount_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_enter_amount_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Enter_Amount_UseCase)

@given(instance=Withdraw_Cash_Select_Account_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_select_account_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Select_Account_UseCase)

@given(instance=Withdraw_Cash_Withdraw_Cash_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_withdraw_cash_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Withdraw_Cash_UseCase)

@given(instance=Withdraw_Cash__Display_MENU_ATM___UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__display_menu_atm___usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__Display_MENU_ATM___UseCase)

@given(instance=Withdraw_Cash__Enter_the_PIN_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash__enter_the_pin_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash__Enter_the_PIN_UseCase)

@given(instance=Withdraw_Cash_Insert_the_Card____UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_insert_the_card____usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Insert_the_Card____UseCase)

@given(instance=Withdraw_Cash_Go_to_ATM_UseCase_strategy)
@settings(max_examples=50)
def test_withdraw_cash_go_to_atm_usecase_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Go_to_ATM_UseCase)

@given(instance=Withdraw_Cash_Bank_Server_Actor_strategy)
@settings(max_examples=50)
def test_withdraw_cash_bank_server_actor_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Bank_Server_Actor)

@given(instance=Withdraw_Cash_Customer_Actor_strategy)
@settings(max_examples=50)
def test_withdraw_cash_customer_actor_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Customer_Actor)

@given(instance=Withdraw_Cash_Interface_Interface_strategy)
@settings(max_examples=50)
def test_withdraw_cash_interface_interface_instantiation(instance):
    assert isinstance(instance, Withdraw_Cash_Interface_Interface)

@given(instance=ATM_transactions_strategy)
@settings(max_examples=50)
def test_atm_transactions_instantiation(instance):
    assert isinstance(instance, ATM_transactions)
