import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NewClass,
    Login,
    conta,
    conta_Conta,
    conta_CheckingAccount,
    conta_Poupan_a,
    conta_investimento,
    transacao_Class,
    transacao_transferencia,
    transacao_saque,
    transacao_deposito,
    transacao_transacao,
    cliente_Customer,
    transacao_TransactionType,
    conta_AccountType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_newclass_is_not_abstract():
    assert not inspect.isabstract(NewClass)


def test_newclass_constructor_exists():
    assert callable(NewClass.__init__)


def test_newclass_constructor_args():
    sig = inspect.signature(NewClass.__init__)
    params = list(sig.parameters.keys())



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "lastLoginTime" in params, "Missing parameter 'lastLoginTime'"

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_lastLoginTime():
    assert hasattr(Login, "lastLoginTime")
    descriptor = None
    for klass in Login.__mro__:
        if "lastLoginTime" in klass.__dict__:
            descriptor = klass.__dict__["lastLoginTime"]
            break
    assert isinstance(descriptor, property)



def test_conta_is_not_abstract():
    assert not inspect.isabstract(conta)


def test_conta_constructor_exists():
    assert callable(conta.__init__)


def test_conta_constructor_args():
    sig = inspect.signature(conta.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"

def test_conta_has__attr():
    assert hasattr(conta, "_attr")
    descriptor = None
    for klass in conta.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)



def test_conta_conta_is_not_abstract():
    assert not inspect.isabstract(conta_Conta)


def test_conta_conta_constructor_exists():
    assert callable(conta_Conta.__init__)


def test_conta_conta_constructor_args():
    sig = inspect.signature(conta_Conta.__init__)
    params = list(sig.parameters.keys())
    assert "tipo" in params, "Missing parameter 'tipo'"
    assert "saldo" in params, "Missing parameter 'saldo'"

def test_conta_conta_has_tipo():
    assert hasattr(conta_Conta, "tipo")
    descriptor = None
    for klass in conta_Conta.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)

def test_conta_conta_has_saldo():
    assert hasattr(conta_Conta, "saldo")
    descriptor = None
    for klass in conta_Conta.__mro__:
        if "saldo" in klass.__dict__:
            descriptor = klass.__dict__["saldo"]
            break
    assert isinstance(descriptor, property)



def test_conta_checkingaccount_is_not_abstract():
    assert not inspect.isabstract(conta_CheckingAccount)


def test_conta_checkingaccount_constructor_exists():
    assert callable(conta_CheckingAccount.__init__)


def test_conta_checkingaccount_constructor_args():
    sig = inspect.signature(conta_CheckingAccount.__init__)
    params = list(sig.parameters.keys())



def test_conta_poupan_a_is_not_abstract():
    assert not inspect.isabstract(conta_Poupan_a)


def test_conta_poupan_a_constructor_exists():
    assert callable(conta_Poupan_a.__init__)


def test_conta_poupan_a_constructor_args():
    sig = inspect.signature(conta_Poupan_a.__init__)
    params = list(sig.parameters.keys())
    assert "tempo" in params, "Missing parameter 'tempo'"
    assert "juros" in params, "Missing parameter 'juros'"

def test_conta_poupan_a_has_tempo():
    assert hasattr(conta_Poupan_a, "tempo")
    descriptor = None
    for klass in conta_Poupan_a.__mro__:
        if "tempo" in klass.__dict__:
            descriptor = klass.__dict__["tempo"]
            break
    assert isinstance(descriptor, property)

def test_conta_poupan_a_has_juros():
    assert hasattr(conta_Poupan_a, "juros")
    descriptor = None
    for klass in conta_Poupan_a.__mro__:
        if "juros" in klass.__dict__:
            descriptor = klass.__dict__["juros"]
            break
    assert isinstance(descriptor, property)



def test_conta_investimento_is_not_abstract():
    assert not inspect.isabstract(conta_investimento)


def test_conta_investimento_constructor_exists():
    assert callable(conta_investimento.__init__)


def test_conta_investimento_constructor_args():
    sig = inspect.signature(conta_investimento.__init__)
    params = list(sig.parameters.keys())
    assert "taxaDeJuros" in params, "Missing parameter 'taxaDeJuros'"

def test_conta_investimento_has_taxaDeJuros():
    assert hasattr(conta_investimento, "taxaDeJuros")
    descriptor = None
    for klass in conta_investimento.__mro__:
        if "taxaDeJuros" in klass.__dict__:
            descriptor = klass.__dict__["taxaDeJuros"]
            break
    assert isinstance(descriptor, property)



def test_transacao_class_is_not_abstract():
    assert not inspect.isabstract(transacao_Class)


def test_transacao_class_constructor_exists():
    assert callable(transacao_Class.__init__)


def test_transacao_class_constructor_args():
    sig = inspect.signature(transacao_Class.__init__)
    params = list(sig.parameters.keys())



def test_transacao_transferencia_is_not_abstract():
    assert not inspect.isabstract(transacao_transferencia)


def test_transacao_transferencia_constructor_exists():
    assert callable(transacao_transferencia.__init__)


def test_transacao_transferencia_constructor_args():
    sig = inspect.signature(transacao_transferencia.__init__)
    params = list(sig.parameters.keys())
    assert "contaOrigem" in params, "Missing parameter 'contaOrigem'"
    assert "contaAlvo" in params, "Missing parameter 'contaAlvo'"

def test_transacao_transferencia_has_contaOrigem():
    assert hasattr(transacao_transferencia, "contaOrigem")
    descriptor = None
    for klass in transacao_transferencia.__mro__:
        if "contaOrigem" in klass.__dict__:
            descriptor = klass.__dict__["contaOrigem"]
            break
    assert isinstance(descriptor, property)

def test_transacao_transferencia_has_contaAlvo():
    assert hasattr(transacao_transferencia, "contaAlvo")
    descriptor = None
    for klass in transacao_transferencia.__mro__:
        if "contaAlvo" in klass.__dict__:
            descriptor = klass.__dict__["contaAlvo"]
            break
    assert isinstance(descriptor, property)



def test_transacao_saque_is_not_abstract():
    assert not inspect.isabstract(transacao_saque)


def test_transacao_saque_constructor_exists():
    assert callable(transacao_saque.__init__)


def test_transacao_saque_constructor_args():
    sig = inspect.signature(transacao_saque.__init__)
    params = list(sig.parameters.keys())
    assert "valor" in params, "Missing parameter 'valor'"

def test_transacao_saque_has_valor():
    assert hasattr(transacao_saque, "valor")
    descriptor = None
    for klass in transacao_saque.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
            break
    assert isinstance(descriptor, property)



def test_transacao_deposito_is_not_abstract():
    assert not inspect.isabstract(transacao_deposito)


def test_transacao_deposito_constructor_exists():
    assert callable(transacao_deposito.__init__)


def test_transacao_deposito_constructor_args():
    sig = inspect.signature(transacao_deposito.__init__)
    params = list(sig.parameters.keys())
    assert "valor" in params, "Missing parameter 'valor'"

def test_transacao_deposito_has_valor():
    assert hasattr(transacao_deposito, "valor")
    descriptor = None
    for klass in transacao_deposito.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
            break
    assert isinstance(descriptor, property)



def test_transacao_transacao_is_not_abstract():
    assert not inspect.isabstract(transacao_transacao)


def test_transacao_transacao_constructor_exists():
    assert callable(transacao_transacao.__init__)


def test_transacao_transacao_constructor_args():
    sig = inspect.signature(transacao_transacao.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_transacao_transacao_has_type():
    assert hasattr(transacao_transacao, "type")
    descriptor = None
    for klass in transacao_transacao.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_transacao_transacao_has_id():
    assert hasattr(transacao_transacao, "id")
    descriptor = None
    for klass in transacao_transacao.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_transacao_transacao_has_amount():
    assert hasattr(transacao_transacao, "amount")
    descriptor = None
    for klass in transacao_transacao.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_cliente_customer_is_not_abstract():
    assert not inspect.isabstract(cliente_Customer)


def test_cliente_customer_constructor_exists():
    assert callable(cliente_Customer.__init__)


def test_cliente_customer_constructor_args():
    sig = inspect.signature(cliente_Customer.__init__)
    params = list(sig.parameters.keys())
    assert "numeroTel" in params, "Missing parameter 'numeroTel'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "endere_o" in params, "Missing parameter 'endere_o'"
    assert "email" in params, "Missing parameter 'email'"
    assert "dataNascimento" in params, "Missing parameter 'dataNascimento'"

def test_cliente_customer_has_numeroTel():
    assert hasattr(cliente_Customer, "numeroTel")
    descriptor = None
    for klass in cliente_Customer.__mro__:
        if "numeroTel" in klass.__dict__:
            descriptor = klass.__dict__["numeroTel"]
            break
    assert isinstance(descriptor, property)

def test_cliente_customer_has_nome():
    assert hasattr(cliente_Customer, "nome")
    descriptor = None
    for klass in cliente_Customer.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_cliente_customer_has_endere_o():
    assert hasattr(cliente_Customer, "endere_o")
    descriptor = None
    for klass in cliente_Customer.__mro__:
        if "endere_o" in klass.__dict__:
            descriptor = klass.__dict__["endere_o"]
            break
    assert isinstance(descriptor, property)

def test_cliente_customer_has_email():
    assert hasattr(cliente_Customer, "email")
    descriptor = None
    for klass in cliente_Customer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_cliente_customer_has_dataNascimento():
    assert hasattr(cliente_Customer, "dataNascimento")
    descriptor = None
    for klass in cliente_Customer.__mro__:
        if "dataNascimento" in klass.__dict__:
            descriptor = klass.__dict__["dataNascimento"]
            break
    assert isinstance(descriptor, property)

def test_transacao_transactiontype_exists():
    # Check that the Enumeration exists
    assert transacao_TransactionType is not None

def test_transacao_transactiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in transacao_TransactionType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in transacao_TransactionType"

def test_conta_accounttype_exists():
    # Check that the Enumeration exists
    assert conta_AccountType is not None

def test_conta_accounttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in conta_AccountType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in conta_AccountType"


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
NewClass_strategy = st.builds(
    NewClass,
)
Login_strategy = st.builds(
    Login,
    username=
        safe_text,
    password=
        safe_text,
    lastLoginTime=
        st.dates()
)
conta_strategy = st.builds(
    conta,
    _attr=
        safe_text
)
conta_Conta_strategy = st.builds(
    conta_Conta,
    tipo=
        st.none(),
    saldo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
conta_CheckingAccount_strategy = st.builds(
    conta_CheckingAccount,
)
conta_Poupan_a_strategy = st.builds(
    conta_Poupan_a,
    tempo=
        st.integers(),
    juros=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
conta_investimento_strategy = st.builds(
    conta_investimento,
    taxaDeJuros=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
transacao_Class_strategy = st.builds(
    transacao_Class,
)
transacao_transferencia_strategy = st.builds(
    transacao_transferencia,
    contaOrigem=
        st.none(),
    contaAlvo=
        st.none()
)
transacao_saque_strategy = st.builds(
    transacao_saque,
    valor=
        safe_text
)
transacao_deposito_strategy = st.builds(
    transacao_deposito,
    valor=
        safe_text
)
transacao_transacao_strategy = st.builds(
    transacao_transacao,
    type=
        safe_text,
    id=
        st.integers(),
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cliente_Customer_strategy = st.builds(
    cliente_Customer,
    numeroTel=
        safe_text,
    nome=
        safe_text,
    endere_o=
        safe_text,
    email=
        safe_text,
    dataNascimento=
        st.dates()
)

@given(instance=NewClass_strategy)
@settings(max_examples=50)
def test_newclass_instantiation(instance):
    assert isinstance(instance, NewClass)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_lastLoginTime_setter(instance):
    original = instance.lastLoginTime
    instance.lastLoginTime = original
    assert instance.lastLoginTime == original

@given(instance=conta_strategy)
@settings(max_examples=50)
def test_conta_instantiation(instance):
    assert isinstance(instance, conta)



@given(instance=conta_strategy)
def test_conta__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original

@given(instance=conta_Conta_strategy)
@settings(max_examples=50)
def test_conta_conta_instantiation(instance):
    assert isinstance(instance, conta_Conta)



@given(instance=conta_Conta_strategy)
def test_conta_conta_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original



@given(instance=conta_Conta_strategy)
def test_conta_conta_saldo_setter(instance):
    original = instance.saldo
    instance.saldo = original
    assert instance.saldo == original

@given(instance=conta_CheckingAccount_strategy)
@settings(max_examples=50)
def test_conta_checkingaccount_instantiation(instance):
    assert isinstance(instance, conta_CheckingAccount)

@given(instance=conta_Poupan_a_strategy)
@settings(max_examples=50)
def test_conta_poupan_a_instantiation(instance):
    assert isinstance(instance, conta_Poupan_a)



@given(instance=conta_Poupan_a_strategy)
def test_conta_poupan_a_tempo_setter(instance):
    original = instance.tempo
    instance.tempo = original
    assert instance.tempo == original



@given(instance=conta_Poupan_a_strategy)
def test_conta_poupan_a_juros_setter(instance):
    original = instance.juros
    instance.juros = original
    assert instance.juros == original

@given(instance=conta_investimento_strategy)
@settings(max_examples=50)
def test_conta_investimento_instantiation(instance):
    assert isinstance(instance, conta_investimento)



@given(instance=conta_investimento_strategy)
def test_conta_investimento_taxaDeJuros_setter(instance):
    original = instance.taxaDeJuros
    instance.taxaDeJuros = original
    assert instance.taxaDeJuros == original

@given(instance=transacao_Class_strategy)
@settings(max_examples=50)
def test_transacao_class_instantiation(instance):
    assert isinstance(instance, transacao_Class)

@given(instance=transacao_transferencia_strategy)
@settings(max_examples=50)
def test_transacao_transferencia_instantiation(instance):
    assert isinstance(instance, transacao_transferencia)



@given(instance=transacao_transferencia_strategy)
def test_transacao_transferencia_contaOrigem_setter(instance):
    original = instance.contaOrigem
    instance.contaOrigem = original
    assert instance.contaOrigem == original



@given(instance=transacao_transferencia_strategy)
def test_transacao_transferencia_contaAlvo_setter(instance):
    original = instance.contaAlvo
    instance.contaAlvo = original
    assert instance.contaAlvo == original

@given(instance=transacao_saque_strategy)
@settings(max_examples=50)
def test_transacao_saque_instantiation(instance):
    assert isinstance(instance, transacao_saque)



@given(instance=transacao_saque_strategy)
def test_transacao_saque_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original

@given(instance=transacao_deposito_strategy)
@settings(max_examples=50)
def test_transacao_deposito_instantiation(instance):
    assert isinstance(instance, transacao_deposito)



@given(instance=transacao_deposito_strategy)
def test_transacao_deposito_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original

@given(instance=transacao_transacao_strategy)
@settings(max_examples=50)
def test_transacao_transacao_instantiation(instance):
    assert isinstance(instance, transacao_transacao)



@given(instance=transacao_transacao_strategy)
def test_transacao_transacao_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=transacao_transacao_strategy)
def test_transacao_transacao_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=transacao_transacao_strategy)
def test_transacao_transacao_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=cliente_Customer_strategy)
@settings(max_examples=50)
def test_cliente_customer_instantiation(instance):
    assert isinstance(instance, cliente_Customer)



@given(instance=cliente_Customer_strategy)
def test_cliente_customer_numeroTel_setter(instance):
    original = instance.numeroTel
    instance.numeroTel = original
    assert instance.numeroTel == original



@given(instance=cliente_Customer_strategy)
def test_cliente_customer_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=cliente_Customer_strategy)
def test_cliente_customer_endere_o_setter(instance):
    original = instance.endere_o
    instance.endere_o = original
    assert instance.endere_o == original



@given(instance=cliente_Customer_strategy)
def test_cliente_customer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=cliente_Customer_strategy)
def test_cliente_customer_dataNascimento_setter(instance):
    original = instance.dataNascimento
    instance.dataNascimento = original
    assert instance.dataNascimento == original
