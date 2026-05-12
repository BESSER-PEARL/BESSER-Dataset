import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Consulta,
    Especialidade,
    Paciente,
    Medico,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "pre_o" in params, "Missing parameter 'pre_o'"
    assert "data" in params, "Missing parameter 'data'"

def test_consulta_has_pre_o():
    assert hasattr(Consulta, "pre_o")
    descriptor = None
    for klass in Consulta.__mro__:
        if "pre_o" in klass.__dict__:
            descriptor = klass.__dict__["pre_o"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_data():
    assert hasattr(Consulta, "data")
    descriptor = None
    for klass in Consulta.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_especialidade_is_not_abstract():
    assert not inspect.isabstract(Especialidade)


def test_especialidade_constructor_exists():
    assert callable(Especialidade.__init__)


def test_especialidade_constructor_args():
    sig = inspect.signature(Especialidade.__init__)
    params = list(sig.parameters.keys())
    assert "descricao" in params, "Missing parameter 'descricao'"

def test_especialidade_has_descricao():
    assert hasattr(Especialidade, "descricao")
    descriptor = None
    for klass in Especialidade.__mro__:
        if "descricao" in klass.__dict__:
            descriptor = klass.__dict__["descricao"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"
    assert "endere_o" in params, "Missing parameter 'endere_o'"
    assert "celular" in params, "Missing parameter 'celular'"

def test_paciente_has_nome():
    assert hasattr(Paciente, "nome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_endere_o():
    assert hasattr(Paciente, "endere_o")
    descriptor = None
    for klass in Paciente.__mro__:
        if "endere_o" in klass.__dict__:
            descriptor = klass.__dict__["endere_o"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_celular():
    assert hasattr(Paciente, "celular")
    descriptor = None
    for klass in Paciente.__mro__:
        if "celular" in klass.__dict__:
            descriptor = klass.__dict__["celular"]
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
    assert "endereco" in params, "Missing parameter 'endereco'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "foto" in params, "Missing parameter 'foto'"

def test_medico_has_crm():
    assert hasattr(Medico, "crm")
    descriptor = None
    for klass in Medico.__mro__:
        if "crm" in klass.__dict__:
            descriptor = klass.__dict__["crm"]
            break
    assert isinstance(descriptor, property)

def test_medico_has_endereco():
    assert hasattr(Medico, "endereco")
    descriptor = None
    for klass in Medico.__mro__:
        if "endereco" in klass.__dict__:
            descriptor = klass.__dict__["endereco"]
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

def test_medico_has_foto():
    assert hasattr(Medico, "foto")
    descriptor = None
    for klass in Medico.__mro__:
        if "foto" in klass.__dict__:
            descriptor = klass.__dict__["foto"]
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
Consulta_strategy = st.builds(
    Consulta,
    pre_o=
        safe_text,
    data=
        safe_text
)
Especialidade_strategy = st.builds(
    Especialidade,
    descricao=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    nome=
        safe_text,
    endere_o=
        safe_text,
    celular=
        safe_text
)
Medico_strategy = st.builds(
    Medico,
    crm=
        safe_text,
    endereco=
        safe_text,
    nome=
        safe_text,
    foto=
        safe_text
)

@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_consulta_pre_o_setter(instance):
    original = instance.pre_o
    instance.pre_o = original
    assert instance.pre_o == original



@given(instance=Consulta_strategy)
def test_consulta_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=Especialidade_strategy)
@settings(max_examples=50)
def test_especialidade_instantiation(instance):
    assert isinstance(instance, Especialidade)



@given(instance=Especialidade_strategy)
def test_especialidade_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_paciente_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Paciente_strategy)
def test_paciente_endere_o_setter(instance):
    original = instance.endere_o
    instance.endere_o = original
    assert instance.endere_o == original



@given(instance=Paciente_strategy)
def test_paciente_celular_setter(instance):
    original = instance.celular
    instance.celular = original
    assert instance.celular == original

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
def test_medico_endereco_setter(instance):
    original = instance.endereco
    instance.endereco = original
    assert instance.endereco == original



@given(instance=Medico_strategy)
def test_medico_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Medico_strategy)
def test_medico_foto_setter(instance):
    original = instance.foto
    instance.foto = original
    assert instance.foto == original
