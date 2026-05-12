import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Deposito,
    Transferencia,
    Cofre,
    Emprestimo,
    Conta_Normal,
    Conta_Conjunta,
    Remover_Conta,
    CRUD,
    Conta_Poupan_a,
    Conta_Corrente,
    Class,
    Autenticavel,
    IAutenticavel,
    SistemaInterno,
    FixedAccount,
    SalvarConta,
    ContaBancaria,
    Banco,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_deposito_is_not_abstract():
    assert not inspect.isabstract(Deposito)


def test_deposito_constructor_exists():
    assert callable(Deposito.__init__)


def test_deposito_constructor_args():
    sig = inspect.signature(Deposito.__init__)
    params = list(sig.parameters.keys())
    assert "Valor" in params, "Missing parameter 'Valor'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_deposito_has_Valor():
    assert hasattr(Deposito, "Valor")
    descriptor = None
    for klass in Deposito.__mro__:
        if "Valor" in klass.__dict__:
            descriptor = klass.__dict__["Valor"]
            break
    assert isinstance(descriptor, property)

def test_deposito_has_Nome():
    assert hasattr(Deposito, "Nome")
    descriptor = None
    for klass in Deposito.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_transferencia_is_not_abstract():
    assert not inspect.isabstract(Transferencia)


def test_transferencia_constructor_exists():
    assert callable(Transferencia.__init__)


def test_transferencia_constructor_args():
    sig = inspect.signature(Transferencia.__init__)
    params = list(sig.parameters.keys())
    assert "Valor" in params, "Missing parameter 'Valor'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_transferencia_has_Valor():
    assert hasattr(Transferencia, "Valor")
    descriptor = None
    for klass in Transferencia.__mro__:
        if "Valor" in klass.__dict__:
            descriptor = klass.__dict__["Valor"]
            break
    assert isinstance(descriptor, property)

def test_transferencia_has_Nome():
    assert hasattr(Transferencia, "Nome")
    descriptor = None
    for klass in Transferencia.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_cofre_is_not_abstract():
    assert not inspect.isabstract(Cofre)


def test_cofre_constructor_exists():
    assert callable(Cofre.__init__)


def test_cofre_constructor_args():
    sig = inspect.signature(Cofre.__init__)
    params = list(sig.parameters.keys())
    assert "Dinheiro_Armazenado" in params, "Missing parameter 'Dinheiro_Armazenado'"
    assert "Emprestimo_Total" in params, "Missing parameter 'Emprestimo_Total'"

def test_cofre_has_Dinheiro_Armazenado():
    assert hasattr(Cofre, "Dinheiro_Armazenado")
    descriptor = None
    for klass in Cofre.__mro__:
        if "Dinheiro_Armazenado" in klass.__dict__:
            descriptor = klass.__dict__["Dinheiro_Armazenado"]
            break
    assert isinstance(descriptor, property)

def test_cofre_has_Emprestimo_Total():
    assert hasattr(Cofre, "Emprestimo_Total")
    descriptor = None
    for klass in Cofre.__mro__:
        if "Emprestimo_Total" in klass.__dict__:
            descriptor = klass.__dict__["Emprestimo_Total"]
            break
    assert isinstance(descriptor, property)



def test_emprestimo_is_not_abstract():
    assert not inspect.isabstract(Emprestimo)


def test_emprestimo_constructor_exists():
    assert callable(Emprestimo.__init__)


def test_emprestimo_constructor_args():
    sig = inspect.signature(Emprestimo.__init__)
    params = list(sig.parameters.keys())
    assert "Valor" in params, "Missing parameter 'Valor'"

def test_emprestimo_has_Valor():
    assert hasattr(Emprestimo, "Valor")
    descriptor = None
    for klass in Emprestimo.__mro__:
        if "Valor" in klass.__dict__:
            descriptor = klass.__dict__["Valor"]
            break
    assert isinstance(descriptor, property)



def test_conta_normal_is_not_abstract():
    assert not inspect.isabstract(Conta_Normal)


def test_conta_normal_constructor_exists():
    assert callable(Conta_Normal.__init__)


def test_conta_normal_constructor_args():
    sig = inspect.signature(Conta_Normal.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_conta_normal_has_id():
    assert hasattr(Conta_Normal, "id")
    descriptor = None
    for klass in Conta_Normal.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_conta_conjunta_is_not_abstract():
    assert not inspect.isabstract(Conta_Conjunta)


def test_conta_conjunta_constructor_exists():
    assert callable(Conta_Conjunta.__init__)


def test_conta_conjunta_constructor_args():
    sig = inspect.signature(Conta_Conjunta.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_conta_conjunta_has_id():
    assert hasattr(Conta_Conjunta, "id")
    descriptor = None
    for klass in Conta_Conjunta.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_remover_conta_is_not_abstract():
    assert not inspect.isabstract(Remover_Conta)


def test_remover_conta_constructor_exists():
    assert callable(Remover_Conta.__init__)


def test_remover_conta_constructor_args():
    sig = inspect.signature(Remover_Conta.__init__)
    params = list(sig.parameters.keys())



def test_crud_is_not_abstract():
    assert not inspect.isabstract(CRUD)


def test_crud_constructor_exists():
    assert callable(CRUD.__init__)


def test_crud_constructor_args():
    sig = inspect.signature(CRUD.__init__)
    params = list(sig.parameters.keys())
    assert "Adicionar_Conta" in params, "Missing parameter 'Adicionar_Conta'"
    assert "Remover_Conta" in params, "Missing parameter 'Remover_Conta'"

def test_crud_has_Adicionar_Conta():
    assert hasattr(CRUD, "Adicionar_Conta")
    descriptor = None
    for klass in CRUD.__mro__:
        if "Adicionar_Conta" in klass.__dict__:
            descriptor = klass.__dict__["Adicionar_Conta"]
            break
    assert isinstance(descriptor, property)

def test_crud_has_Remover_Conta():
    assert hasattr(CRUD, "Remover_Conta")
    descriptor = None
    for klass in CRUD.__mro__:
        if "Remover_Conta" in klass.__dict__:
            descriptor = klass.__dict__["Remover_Conta"]
            break
    assert isinstance(descriptor, property)



def test_conta_poupan_a_is_not_abstract():
    assert not inspect.isabstract(Conta_Poupan_a)


def test_conta_poupan_a_constructor_exists():
    assert callable(Conta_Poupan_a.__init__)


def test_conta_poupan_a_constructor_args():
    sig = inspect.signature(Conta_Poupan_a.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Senha" in params, "Missing parameter 'Senha'"
    assert "CPF" in params, "Missing parameter 'CPF'"

def test_conta_poupan_a_has_Nome():
    assert hasattr(Conta_Poupan_a, "Nome")
    descriptor = None
    for klass in Conta_Poupan_a.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_conta_poupan_a_has_Senha():
    assert hasattr(Conta_Poupan_a, "Senha")
    descriptor = None
    for klass in Conta_Poupan_a.__mro__:
        if "Senha" in klass.__dict__:
            descriptor = klass.__dict__["Senha"]
            break
    assert isinstance(descriptor, property)

def test_conta_poupan_a_has_CPF():
    assert hasattr(Conta_Poupan_a, "CPF")
    descriptor = None
    for klass in Conta_Poupan_a.__mro__:
        if "CPF" in klass.__dict__:
            descriptor = klass.__dict__["CPF"]
            break
    assert isinstance(descriptor, property)



def test_conta_corrente_is_not_abstract():
    assert not inspect.isabstract(Conta_Corrente)


def test_conta_corrente_constructor_exists():
    assert callable(Conta_Corrente.__init__)


def test_conta_corrente_constructor_args():
    sig = inspect.signature(Conta_Corrente.__init__)
    params = list(sig.parameters.keys())
    assert "Senha" in params, "Missing parameter 'Senha'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "CPF" in params, "Missing parameter 'CPF'"
    assert "Taxa_de_Movimenta__o" in params, "Missing parameter 'Taxa_de_Movimenta__o'"

def test_conta_corrente_has_Senha():
    assert hasattr(Conta_Corrente, "Senha")
    descriptor = None
    for klass in Conta_Corrente.__mro__:
        if "Senha" in klass.__dict__:
            descriptor = klass.__dict__["Senha"]
            break
    assert isinstance(descriptor, property)

def test_conta_corrente_has_Nome():
    assert hasattr(Conta_Corrente, "Nome")
    descriptor = None
    for klass in Conta_Corrente.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_conta_corrente_has_CPF():
    assert hasattr(Conta_Corrente, "CPF")
    descriptor = None
    for klass in Conta_Corrente.__mro__:
        if "CPF" in klass.__dict__:
            descriptor = klass.__dict__["CPF"]
            break
    assert isinstance(descriptor, property)

def test_conta_corrente_has_Taxa_de_Movimenta__o():
    assert hasattr(Conta_Corrente, "Taxa_de_Movimenta__o")
    descriptor = None
    for klass in Conta_Corrente.__mro__:
        if "Taxa_de_Movimenta__o" in klass.__dict__:
            descriptor = klass.__dict__["Taxa_de_Movimenta__o"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_autenticavel_is_not_abstract():
    assert not inspect.isabstract(Autenticavel)


def test_autenticavel_constructor_exists():
    assert callable(Autenticavel.__init__)


def test_autenticavel_constructor_args():
    sig = inspect.signature(Autenticavel.__init__)
    params = list(sig.parameters.keys())
    assert "Autenticar" in params, "Missing parameter 'Autenticar'"
    assert "Senha" in params, "Missing parameter 'Senha'"

def test_autenticavel_has_Autenticar():
    assert hasattr(Autenticavel, "Autenticar")
    descriptor = None
    for klass in Autenticavel.__mro__:
        if "Autenticar" in klass.__dict__:
            descriptor = klass.__dict__["Autenticar"]
            break
    assert isinstance(descriptor, property)

def test_autenticavel_has_Senha():
    assert hasattr(Autenticavel, "Senha")
    descriptor = None
    for klass in Autenticavel.__mro__:
        if "Senha" in klass.__dict__:
            descriptor = klass.__dict__["Senha"]
            break
    assert isinstance(descriptor, property)



def test_iautenticavel_is_not_abstract():
    assert not inspect.isabstract(IAutenticavel)


def test_iautenticavel_constructor_exists():
    assert callable(IAutenticavel.__init__)


def test_iautenticavel_constructor_args():
    sig = inspect.signature(IAutenticavel.__init__)
    params = list(sig.parameters.keys())
    assert "Autenticar" in params, "Missing parameter 'Autenticar'"

def test_iautenticavel_has_Autenticar():
    assert hasattr(IAutenticavel, "Autenticar")
    descriptor = None
    for klass in IAutenticavel.__mro__:
        if "Autenticar" in klass.__dict__:
            descriptor = klass.__dict__["Autenticar"]
            break
    assert isinstance(descriptor, property)



def test_sistemainterno_is_not_abstract():
    assert not inspect.isabstract(SistemaInterno)


def test_sistemainterno_constructor_exists():
    assert callable(SistemaInterno.__init__)


def test_sistemainterno_constructor_args():
    sig = inspect.signature(SistemaInterno.__init__)
    params = list(sig.parameters.keys())
    assert "Entrar" in params, "Missing parameter 'Entrar'"
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "_attr1" in params, "Missing parameter '_attr1'"

def test_sistemainterno_has_Entrar():
    assert hasattr(SistemaInterno, "Entrar")
    descriptor = None
    for klass in SistemaInterno.__mro__:
        if "Entrar" in klass.__dict__:
            descriptor = klass.__dict__["Entrar"]
            break
    assert isinstance(descriptor, property)

def test_sistemainterno_has__attr():
    assert hasattr(SistemaInterno, "_attr")
    descriptor = None
    for klass in SistemaInterno.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)

def test_sistemainterno_has__attr1():
    assert hasattr(SistemaInterno, "_attr1")
    descriptor = None
    for klass in SistemaInterno.__mro__:
        if "_attr1" in klass.__dict__:
            descriptor = klass.__dict__["_attr1"]
            break
    assert isinstance(descriptor, property)



def test_fixedaccount_is_not_abstract():
    assert not inspect.isabstract(FixedAccount)


def test_fixedaccount_constructor_exists():
    assert callable(FixedAccount.__init__)


def test_fixedaccount_constructor_args():
    sig = inspect.signature(FixedAccount.__init__)
    params = list(sig.parameters.keys())
    assert "chequeBookNo" in params, "Missing parameter 'chequeBookNo'"

def test_fixedaccount_has_chequeBookNo():
    assert hasattr(FixedAccount, "chequeBookNo")
    descriptor = None
    for klass in FixedAccount.__mro__:
        if "chequeBookNo" in klass.__dict__:
            descriptor = klass.__dict__["chequeBookNo"]
            break
    assert isinstance(descriptor, property)



def test_salvarconta_is_not_abstract():
    assert not inspect.isabstract(SalvarConta)


def test_salvarconta_constructor_exists():
    assert callable(SalvarConta.__init__)


def test_salvarconta_constructor_args():
    sig = inspect.signature(SalvarConta.__init__)
    params = list(sig.parameters.keys())
    assert "noticeGiven" in params, "Missing parameter 'noticeGiven'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_salvarconta_has_noticeGiven():
    assert hasattr(SalvarConta, "noticeGiven")
    descriptor = None
    for klass in SalvarConta.__mro__:
        if "noticeGiven" in klass.__dict__:
            descriptor = klass.__dict__["noticeGiven"]
            break
    assert isinstance(descriptor, property)

def test_salvarconta_has_interestRate():
    assert hasattr(SalvarConta, "interestRate")
    descriptor = None
    for klass in SalvarConta.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_contabancaria_is_not_abstract():
    assert not inspect.isabstract(ContaBancaria)


def test_contabancaria_constructor_exists():
    assert callable(ContaBancaria.__init__)


def test_contabancaria_constructor_args():
    sig = inspect.signature(ContaBancaria.__init__)
    params = list(sig.parameters.keys())
    assert "NomeConta" in params, "Missing parameter 'NomeConta'"
    assert "Saldo" in params, "Missing parameter 'Saldo'"
    assert "NumeroConta" in params, "Missing parameter 'NumeroConta'"

def test_contabancaria_has_NomeConta():
    assert hasattr(ContaBancaria, "NomeConta")
    descriptor = None
    for klass in ContaBancaria.__mro__:
        if "NomeConta" in klass.__dict__:
            descriptor = klass.__dict__["NomeConta"]
            break
    assert isinstance(descriptor, property)

def test_contabancaria_has_Saldo():
    assert hasattr(ContaBancaria, "Saldo")
    descriptor = None
    for klass in ContaBancaria.__mro__:
        if "Saldo" in klass.__dict__:
            descriptor = klass.__dict__["Saldo"]
            break
    assert isinstance(descriptor, property)

def test_contabancaria_has_NumeroConta():
    assert hasattr(ContaBancaria, "NumeroConta")
    descriptor = None
    for klass in ContaBancaria.__mro__:
        if "NumeroConta" in klass.__dict__:
            descriptor = klass.__dict__["NumeroConta"]
            break
    assert isinstance(descriptor, property)



def test_banco_is_not_abstract():
    assert not inspect.isabstract(Banco)


def test_banco_constructor_exists():
    assert callable(Banco.__init__)


def test_banco_constructor_args():
    sig = inspect.signature(Banco.__init__)
    params = list(sig.parameters.keys())
    assert "NomeBanco" in params, "Missing parameter 'NomeBanco'"

def test_banco_has_NomeBanco():
    assert hasattr(Banco, "NomeBanco")
    descriptor = None
    for klass in Banco.__mro__:
        if "NomeBanco" in klass.__dict__:
            descriptor = klass.__dict__["NomeBanco"]
            break
    assert isinstance(descriptor, property)

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Deposito_strategy = st.builds(
    Deposito,
    Valor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Nome=
        safe_text
)
Transferencia_strategy = st.builds(
    Transferencia,
    Valor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Nome=
        safe_text
)
Cofre_strategy = st.builds(
    Cofre,
    Dinheiro_Armazenado=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Emprestimo_Total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Emprestimo_strategy = st.builds(
    Emprestimo,
    Valor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Conta_Normal_strategy = st.builds(
    Conta_Normal,
    id=
        st.integers()
)
Conta_Conjunta_strategy = st.builds(
    Conta_Conjunta,
    id=
        st.integers()
)
Remover_Conta_strategy = st.builds(
    Remover_Conta,
)
CRUD_strategy = st.builds(
    CRUD,
    Adicionar_Conta=
        safe_text,
    Remover_Conta=
        safe_text
)
Conta_Poupan_a_strategy = st.builds(
    Conta_Poupan_a,
    Nome=
        safe_text,
    Senha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    CPF=
        st.integers()
)
Conta_Corrente_strategy = st.builds(
    Conta_Corrente,
    Senha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Nome=
        safe_text,
    CPF=
        st.integers(),
    Taxa_de_Movimenta__o=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Class_strategy = st.builds(
    Class,
)
Autenticavel_strategy = st.builds(
    Autenticavel,
    Autenticar=
        safe_text,
    Senha=
        safe_text
)
IAutenticavel_strategy = st.builds(
    IAutenticavel,
    Autenticar=
        safe_text
)
SistemaInterno_strategy = st.builds(
    SistemaInterno,
    Entrar=
        st.none(),
    _attr=
        st.none(),
    _attr1=
        safe_text
)
FixedAccount_strategy = st.builds(
    FixedAccount,
    chequeBookNo=
        safe_text
)
SalvarConta_strategy = st.builds(
    SalvarConta,
    noticeGiven=
        st.booleans(),
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ContaBancaria_strategy = st.builds(
    ContaBancaria,
    NomeConta=
        safe_text,
    Saldo=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    NumeroConta=
        st.integers()
)
Banco_strategy = st.builds(
    Banco,
    NomeBanco=
        safe_text
)

@given(instance=Deposito_strategy)
@settings(max_examples=50)
def test_deposito_instantiation(instance):
    assert isinstance(instance, Deposito)



@given(instance=Deposito_strategy)
def test_deposito_Valor_setter(instance):
    original = instance.Valor
    instance.Valor = original
    assert instance.Valor == original



@given(instance=Deposito_strategy)
def test_deposito_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=Transferencia_strategy)
@settings(max_examples=50)
def test_transferencia_instantiation(instance):
    assert isinstance(instance, Transferencia)



@given(instance=Transferencia_strategy)
def test_transferencia_Valor_setter(instance):
    original = instance.Valor
    instance.Valor = original
    assert instance.Valor == original



@given(instance=Transferencia_strategy)
def test_transferencia_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=Cofre_strategy)
@settings(max_examples=50)
def test_cofre_instantiation(instance):
    assert isinstance(instance, Cofre)



@given(instance=Cofre_strategy)
def test_cofre_Dinheiro_Armazenado_setter(instance):
    original = instance.Dinheiro_Armazenado
    instance.Dinheiro_Armazenado = original
    assert instance.Dinheiro_Armazenado == original



@given(instance=Cofre_strategy)
def test_cofre_Emprestimo_Total_setter(instance):
    original = instance.Emprestimo_Total
    instance.Emprestimo_Total = original
    assert instance.Emprestimo_Total == original

@given(instance=Emprestimo_strategy)
@settings(max_examples=50)
def test_emprestimo_instantiation(instance):
    assert isinstance(instance, Emprestimo)



@given(instance=Emprestimo_strategy)
def test_emprestimo_Valor_setter(instance):
    original = instance.Valor
    instance.Valor = original
    assert instance.Valor == original

@given(instance=Conta_Normal_strategy)
@settings(max_examples=50)
def test_conta_normal_instantiation(instance):
    assert isinstance(instance, Conta_Normal)



@given(instance=Conta_Normal_strategy)
def test_conta_normal_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Conta_Conjunta_strategy)
@settings(max_examples=50)
def test_conta_conjunta_instantiation(instance):
    assert isinstance(instance, Conta_Conjunta)



@given(instance=Conta_Conjunta_strategy)
def test_conta_conjunta_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Remover_Conta_strategy)
@settings(max_examples=50)
def test_remover_conta_instantiation(instance):
    assert isinstance(instance, Remover_Conta)

@given(instance=CRUD_strategy)
@settings(max_examples=50)
def test_crud_instantiation(instance):
    assert isinstance(instance, CRUD)



@given(instance=CRUD_strategy)
def test_crud_Adicionar_Conta_setter(instance):
    original = instance.Adicionar_Conta
    instance.Adicionar_Conta = original
    assert instance.Adicionar_Conta == original



@given(instance=CRUD_strategy)
def test_crud_Remover_Conta_setter(instance):
    original = instance.Remover_Conta
    instance.Remover_Conta = original
    assert instance.Remover_Conta == original

@given(instance=Conta_Poupan_a_strategy)
@settings(max_examples=50)
def test_conta_poupan_a_instantiation(instance):
    assert isinstance(instance, Conta_Poupan_a)



@given(instance=Conta_Poupan_a_strategy)
def test_conta_poupan_a_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Conta_Poupan_a_strategy)
def test_conta_poupan_a_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original



@given(instance=Conta_Poupan_a_strategy)
def test_conta_poupan_a_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original

@given(instance=Conta_Corrente_strategy)
@settings(max_examples=50)
def test_conta_corrente_instantiation(instance):
    assert isinstance(instance, Conta_Corrente)



@given(instance=Conta_Corrente_strategy)
def test_conta_corrente_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original



@given(instance=Conta_Corrente_strategy)
def test_conta_corrente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Conta_Corrente_strategy)
def test_conta_corrente_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original



@given(instance=Conta_Corrente_strategy)
def test_conta_corrente_Taxa_de_Movimenta__o_setter(instance):
    original = instance.Taxa_de_Movimenta__o
    instance.Taxa_de_Movimenta__o = original
    assert instance.Taxa_de_Movimenta__o == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Autenticavel_strategy)
@settings(max_examples=50)
def test_autenticavel_instantiation(instance):
    assert isinstance(instance, Autenticavel)



@given(instance=Autenticavel_strategy)
def test_autenticavel_Autenticar_setter(instance):
    original = instance.Autenticar
    instance.Autenticar = original
    assert instance.Autenticar == original



@given(instance=Autenticavel_strategy)
def test_autenticavel_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original

@given(instance=IAutenticavel_strategy)
@settings(max_examples=50)
def test_iautenticavel_instantiation(instance):
    assert isinstance(instance, IAutenticavel)



@given(instance=IAutenticavel_strategy)
def test_iautenticavel_Autenticar_setter(instance):
    original = instance.Autenticar
    instance.Autenticar = original
    assert instance.Autenticar == original

@given(instance=SistemaInterno_strategy)
@settings(max_examples=50)
def test_sistemainterno_instantiation(instance):
    assert isinstance(instance, SistemaInterno)



@given(instance=SistemaInterno_strategy)
def test_sistemainterno_Entrar_setter(instance):
    original = instance.Entrar
    instance.Entrar = original
    assert instance.Entrar == original



@given(instance=SistemaInterno_strategy)
def test_sistemainterno__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=SistemaInterno_strategy)
def test_sistemainterno__attr1_setter(instance):
    original = instance._attr1
    instance._attr1 = original
    assert instance._attr1 == original

@given(instance=FixedAccount_strategy)
@settings(max_examples=50)
def test_fixedaccount_instantiation(instance):
    assert isinstance(instance, FixedAccount)



@given(instance=FixedAccount_strategy)
def test_fixedaccount_chequeBookNo_setter(instance):
    original = instance.chequeBookNo
    instance.chequeBookNo = original
    assert instance.chequeBookNo == original

@given(instance=SalvarConta_strategy)
@settings(max_examples=50)
def test_salvarconta_instantiation(instance):
    assert isinstance(instance, SalvarConta)



@given(instance=SalvarConta_strategy)
def test_salvarconta_noticeGiven_setter(instance):
    original = instance.noticeGiven
    instance.noticeGiven = original
    assert instance.noticeGiven == original



@given(instance=SalvarConta_strategy)
def test_salvarconta_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=ContaBancaria_strategy)
@settings(max_examples=50)
def test_contabancaria_instantiation(instance):
    assert isinstance(instance, ContaBancaria)



@given(instance=ContaBancaria_strategy)
def test_contabancaria_NomeConta_setter(instance):
    original = instance.NomeConta
    instance.NomeConta = original
    assert instance.NomeConta == original



@given(instance=ContaBancaria_strategy)
def test_contabancaria_Saldo_setter(instance):
    original = instance.Saldo
    instance.Saldo = original
    assert instance.Saldo == original



@given(instance=ContaBancaria_strategy)
def test_contabancaria_NumeroConta_setter(instance):
    original = instance.NumeroConta
    instance.NumeroConta = original
    assert instance.NumeroConta == original

@given(instance=Banco_strategy)
@settings(max_examples=50)
def test_banco_instantiation(instance):
    assert isinstance(instance, Banco)



@given(instance=Banco_strategy)
def test_banco_NomeBanco_setter(instance):
    original = instance.NomeBanco
    instance.NomeBanco = original
    assert instance.NomeBanco == original
