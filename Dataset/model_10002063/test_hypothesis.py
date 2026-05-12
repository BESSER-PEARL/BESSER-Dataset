import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    float,
    Exame,
    Medico,
    Pedido_Exame,
    UF,
    Cidade,
    Paciente,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_float_is_not_abstract():
    assert not inspect.isabstract(float)


def test_float_constructor_exists():
    assert callable(float.__init__)


def test_float_constructor_args():
    sig = inspect.signature(float.__init__)
    params = list(sig.parameters.keys())



def test_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "valor" in params, "Missing parameter 'valor'"
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "procedimentos" in params, "Missing parameter 'procedimentos'"

def test_exame_has_codigo():
    assert hasattr(Exame, "codigo")
    descriptor = None
    for klass in Exame.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_valor():
    assert hasattr(Exame, "valor")
    descriptor = None
    for klass in Exame.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_descricao():
    assert hasattr(Exame, "descricao")
    descriptor = None
    for klass in Exame.__mro__:
        if "descricao" in klass.__dict__:
            descriptor = klass.__dict__["descricao"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_procedimentos():
    assert hasattr(Exame, "procedimentos")
    descriptor = None
    for klass in Exame.__mro__:
        if "procedimentos" in klass.__dict__:
            descriptor = klass.__dict__["procedimentos"]
            break
    assert isinstance(descriptor, property)



def test_medico_is_not_abstract():
    assert not inspect.isabstract(Medico)


def test_medico_constructor_exists():
    assert callable(Medico.__init__)


def test_medico_constructor_args():
    sig = inspect.signature(Medico.__init__)
    params = list(sig.parameters.keys())
    assert "crm" in params, "Missing parameter 'crm'"
    assert "nome" in params, "Missing parameter 'nome'"

def test_medico_has_crm():
    assert hasattr(Medico, "crm")
    descriptor = None
    for klass in Medico.__mro__:
        if "crm" in klass.__dict__:
            descriptor = klass.__dict__["crm"]
            break
    assert isinstance(descriptor, property)

def test_medico_has_nome():
    assert hasattr(Medico, "nome")
    descriptor = None
    for klass in Medico.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_pedido_exame_is_not_abstract():
    assert not inspect.isabstract(Pedido_Exame)


def test_pedido_exame_constructor_exists():
    assert callable(Pedido_Exame.__init__)


def test_pedido_exame_constructor_args():
    sig = inspect.signature(Pedido_Exame.__init__)
    params = list(sig.parameters.keys())
    assert "codigo" in params, "Missing parameter 'codigo'"

def test_pedido_exame_has_codigo():
    assert hasattr(Pedido_Exame, "codigo")
    descriptor = None
    for klass in Pedido_Exame.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)



def test_uf_is_not_abstract():
    assert not inspect.isabstract(UF)


def test_uf_constructor_exists():
    assert callable(UF.__init__)


def test_uf_constructor_args():
    sig = inspect.signature(UF.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"
    assert "sigla" in params, "Missing parameter 'sigla'"

def test_uf_has_nome():
    assert hasattr(UF, "nome")
    descriptor = None
    for klass in UF.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_uf_has_sigla():
    assert hasattr(UF, "sigla")
    descriptor = None
    for klass in UF.__mro__:
        if "sigla" in klass.__dict__:
            descriptor = klass.__dict__["sigla"]
            break
    assert isinstance(descriptor, property)



def test_cidade_is_not_abstract():
    assert not inspect.isabstract(Cidade)


def test_cidade_constructor_exists():
    assert callable(Cidade.__init__)


def test_cidade_constructor_args():
    sig = inspect.signature(Cidade.__init__)
    params = list(sig.parameters.keys())
    assert "ddd" in params, "Missing parameter 'ddd'"
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "nome" in params, "Missing parameter 'nome'"

def test_cidade_has_ddd():
    assert hasattr(Cidade, "ddd")
    descriptor = None
    for klass in Cidade.__mro__:
        if "ddd" in klass.__dict__:
            descriptor = klass.__dict__["ddd"]
            break
    assert isinstance(descriptor, property)

def test_cidade_has_codigo():
    assert hasattr(Cidade, "codigo")
    descriptor = None
    for klass in Cidade.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_cidade_has_nome():
    assert hasattr(Cidade, "nome")
    descriptor = None
    for klass in Cidade.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "cep" in params, "Missing parameter 'cep'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "rg" in params, "Missing parameter 'rg'"
    assert "dataNascimento" in params, "Missing parameter 'dataNascimento'"
    assert "codigo" in params, "Missing parameter 'codigo'"
    assert "endereco" in params, "Missing parameter 'endereco'"
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "telefone" in params, "Missing parameter 'telefone'"

def test_paciente_has_cep():
    assert hasattr(Paciente, "cep")
    descriptor = None
    for klass in Paciente.__mro__:
        if "cep" in klass.__dict__:
            descriptor = klass.__dict__["cep"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_nome():
    assert hasattr(Paciente, "nome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_rg():
    assert hasattr(Paciente, "rg")
    descriptor = None
    for klass in Paciente.__mro__:
        if "rg" in klass.__dict__:
            descriptor = klass.__dict__["rg"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_dataNascimento():
    assert hasattr(Paciente, "dataNascimento")
    descriptor = None
    for klass in Paciente.__mro__:
        if "dataNascimento" in klass.__dict__:
            descriptor = klass.__dict__["dataNascimento"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_codigo():
    assert hasattr(Paciente, "codigo")
    descriptor = None
    for klass in Paciente.__mro__:
        if "codigo" in klass.__dict__:
            descriptor = klass.__dict__["codigo"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_endereco():
    assert hasattr(Paciente, "endereco")
    descriptor = None
    for klass in Paciente.__mro__:
        if "endereco" in klass.__dict__:
            descriptor = klass.__dict__["endereco"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_cpf():
    assert hasattr(Paciente, "cpf")
    descriptor = None
    for klass in Paciente.__mro__:
        if "cpf" in klass.__dict__:
            descriptor = klass.__dict__["cpf"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_telefone():
    assert hasattr(Paciente, "telefone")
    descriptor = None
    for klass in Paciente.__mro__:
        if "telefone" in klass.__dict__:
            descriptor = klass.__dict__["telefone"]
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
float_strategy = st.builds(
    float,
)
Exame_strategy = st.builds(
    Exame,
    codigo=
        st.integers(),
    valor=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    descricao=
        safe_text,
    procedimentos=
        safe_text
)
Medico_strategy = st.builds(
    Medico,
    crm=
        st.integers(),
    nome=
        safe_text
)
Pedido_Exame_strategy = st.builds(
    Pedido_Exame,
    codigo=
        st.integers()
)
UF_strategy = st.builds(
    UF,
    nome=
        safe_text,
    sigla=
        safe_text
)
Cidade_strategy = st.builds(
    Cidade,
    ddd=
        st.integers(),
    codigo=
        st.integers(),
    nome=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    cep=
        safe_text,
    nome=
        safe_text,
    rg=
        safe_text,
    dataNascimento=
        safe_text,
    codigo=
        st.integers(),
    endereco=
        safe_text,
    cpf=
        safe_text,
    telefone=
        safe_text
)

@given(instance=float_strategy)
@settings(max_examples=50)
def test_float_instantiation(instance):
    assert isinstance(instance, float)

@given(instance=Exame_strategy)
@settings(max_examples=50)
def test_exame_instantiation(instance):
    assert isinstance(instance, Exame)



@given(instance=Exame_strategy)
def test_exame_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Exame_strategy)
def test_exame_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=Exame_strategy)
def test_exame_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=Exame_strategy)
def test_exame_procedimentos_setter(instance):
    original = instance.procedimentos
    instance.procedimentos = original
    assert instance.procedimentos == original

@given(instance=Medico_strategy)
@settings(max_examples=50)
def test_medico_instantiation(instance):
    assert isinstance(instance, Medico)



@given(instance=Medico_strategy)
def test_medico_crm_setter(instance):
    original = instance.crm
    instance.crm = original
    assert instance.crm == original



@given(instance=Medico_strategy)
def test_medico_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=Pedido_Exame_strategy)
@settings(max_examples=50)
def test_pedido_exame_instantiation(instance):
    assert isinstance(instance, Pedido_Exame)



@given(instance=Pedido_Exame_strategy)
def test_pedido_exame_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original

@given(instance=UF_strategy)
@settings(max_examples=50)
def test_uf_instantiation(instance):
    assert isinstance(instance, UF)



@given(instance=UF_strategy)
def test_uf_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=UF_strategy)
def test_uf_sigla_setter(instance):
    original = instance.sigla
    instance.sigla = original
    assert instance.sigla == original

@given(instance=Cidade_strategy)
@settings(max_examples=50)
def test_cidade_instantiation(instance):
    assert isinstance(instance, Cidade)



@given(instance=Cidade_strategy)
def test_cidade_ddd_setter(instance):
    original = instance.ddd
    instance.ddd = original
    assert instance.ddd == original



@given(instance=Cidade_strategy)
def test_cidade_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Cidade_strategy)
def test_cidade_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_paciente_cep_setter(instance):
    original = instance.cep
    instance.cep = original
    assert instance.cep == original



@given(instance=Paciente_strategy)
def test_paciente_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Paciente_strategy)
def test_paciente_rg_setter(instance):
    original = instance.rg
    instance.rg = original
    assert instance.rg == original



@given(instance=Paciente_strategy)
def test_paciente_dataNascimento_setter(instance):
    original = instance.dataNascimento
    instance.dataNascimento = original
    assert instance.dataNascimento == original



@given(instance=Paciente_strategy)
def test_paciente_codigo_setter(instance):
    original = instance.codigo
    instance.codigo = original
    assert instance.codigo == original



@given(instance=Paciente_strategy)
def test_paciente_endereco_setter(instance):
    original = instance.endereco
    instance.endereco = original
    assert instance.endereco == original



@given(instance=Paciente_strategy)
def test_paciente_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=Paciente_strategy)
def test_paciente_telefone_setter(instance):
    original = instance.telefone
    instance.telefone = original
    assert instance.telefone == original
