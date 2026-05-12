import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    clinicasaudeperfeita_Consulta_UseCase,
    clinicasaudeperfeita_Medico_Actor,
    clinicasaudeperfeita_Marca_consulta_UseCase,
    clinicasaudeperfeita_Recepcionista_Actor,
    clinicasaudeperfeita_Analisa_consulta_UseCase,
    clinicasaudeperfeita_Paciente_Actor,
    Exame,
    clinicasaudeperfeita_Medico,
    clinicasaudeperfeita_Recepcionista,
    clinicasaudeperfeita_Medicamento,
    clinicasaudeperfeita_Exame,
    clinicasaudeperfeita_Consulta,
    clinicasaudeperfeita_Compromisso,
    clinicasaudeperfeita_Paciente,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_clinicasaudeperfeita_consulta_usecase_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Consulta_UseCase)


def test_clinicasaudeperfeita_consulta_usecase_constructor_exists():
    assert callable(clinicasaudeperfeita_Consulta_UseCase.__init__)


def test_clinicasaudeperfeita_consulta_usecase_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Consulta_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_medico_actor_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Medico_Actor)


def test_clinicasaudeperfeita_medico_actor_constructor_exists():
    assert callable(clinicasaudeperfeita_Medico_Actor.__init__)


def test_clinicasaudeperfeita_medico_actor_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Medico_Actor.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_marca_consulta_usecase_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Marca_consulta_UseCase)


def test_clinicasaudeperfeita_marca_consulta_usecase_constructor_exists():
    assert callable(clinicasaudeperfeita_Marca_consulta_UseCase.__init__)


def test_clinicasaudeperfeita_marca_consulta_usecase_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Marca_consulta_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_recepcionista_actor_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Recepcionista_Actor)


def test_clinicasaudeperfeita_recepcionista_actor_constructor_exists():
    assert callable(clinicasaudeperfeita_Recepcionista_Actor.__init__)


def test_clinicasaudeperfeita_recepcionista_actor_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Recepcionista_Actor.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_analisa_consulta_usecase_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Analisa_consulta_UseCase)


def test_clinicasaudeperfeita_analisa_consulta_usecase_constructor_exists():
    assert callable(clinicasaudeperfeita_Analisa_consulta_UseCase.__init__)


def test_clinicasaudeperfeita_analisa_consulta_usecase_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Analisa_consulta_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_paciente_actor_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Paciente_Actor)


def test_clinicasaudeperfeita_paciente_actor_constructor_exists():
    assert callable(clinicasaudeperfeita_Paciente_Actor.__init__)


def test_clinicasaudeperfeita_paciente_actor_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Paciente_Actor.__init__)
    params = list(sig.parameters.keys())



def test_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())



def test_clinicasaudeperfeita_medico_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Medico)


def test_clinicasaudeperfeita_medico_constructor_exists():
    assert callable(clinicasaudeperfeita_Medico.__init__)


def test_clinicasaudeperfeita_medico_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Medico.__init__)
    params = list(sig.parameters.keys())
    assert "idade" in params, "Missing parameter 'idade'"
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "agenda" in params, "Missing parameter 'agenda'"
    assert "nome" in params, "Missing parameter 'nome'"

def test_clinicasaudeperfeita_medico_has_idade():
    assert hasattr(clinicasaudeperfeita_Medico, "idade")
    descriptor = None
    for klass in clinicasaudeperfeita_Medico.__mro__:
        if "idade" in klass.__dict__:
            descriptor = klass.__dict__["idade"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_medico_has_cpf():
    assert hasattr(clinicasaudeperfeita_Medico, "cpf")
    descriptor = None
    for klass in clinicasaudeperfeita_Medico.__mro__:
        if "cpf" in klass.__dict__:
            descriptor = klass.__dict__["cpf"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_medico_has_agenda():
    assert hasattr(clinicasaudeperfeita_Medico, "agenda")
    descriptor = None
    for klass in clinicasaudeperfeita_Medico.__mro__:
        if "agenda" in klass.__dict__:
            descriptor = klass.__dict__["agenda"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_medico_has_nome():
    assert hasattr(clinicasaudeperfeita_Medico, "nome")
    descriptor = None
    for klass in clinicasaudeperfeita_Medico.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_recepcionista_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Recepcionista)


def test_clinicasaudeperfeita_recepcionista_constructor_exists():
    assert callable(clinicasaudeperfeita_Recepcionista.__init__)


def test_clinicasaudeperfeita_recepcionista_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Recepcionista.__init__)
    params = list(sig.parameters.keys())
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "idade" in params, "Missing parameter 'idade'"

def test_clinicasaudeperfeita_recepcionista_has_cpf():
    assert hasattr(clinicasaudeperfeita_Recepcionista, "cpf")
    descriptor = None
    for klass in clinicasaudeperfeita_Recepcionista.__mro__:
        if "cpf" in klass.__dict__:
            descriptor = klass.__dict__["cpf"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_recepcionista_has_nome():
    assert hasattr(clinicasaudeperfeita_Recepcionista, "nome")
    descriptor = None
    for klass in clinicasaudeperfeita_Recepcionista.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_recepcionista_has_idade():
    assert hasattr(clinicasaudeperfeita_Recepcionista, "idade")
    descriptor = None
    for klass in clinicasaudeperfeita_Recepcionista.__mro__:
        if "idade" in klass.__dict__:
            descriptor = klass.__dict__["idade"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_medicamento_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Medicamento)


def test_clinicasaudeperfeita_medicamento_constructor_exists():
    assert callable(clinicasaudeperfeita_Medicamento.__init__)


def test_clinicasaudeperfeita_medicamento_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Medicamento.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_clinicasaudeperfeita_medicamento_has_nome():
    assert hasattr(clinicasaudeperfeita_Medicamento, "nome")
    descriptor = None
    for klass in clinicasaudeperfeita_Medicamento.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_exame_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Exame)


def test_clinicasaudeperfeita_exame_constructor_exists():
    assert callable(clinicasaudeperfeita_Exame.__init__)


def test_clinicasaudeperfeita_exame_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Exame.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_clinicasaudeperfeita_exame_has_nome():
    assert hasattr(clinicasaudeperfeita_Exame, "nome")
    descriptor = None
    for klass in clinicasaudeperfeita_Exame.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_consulta_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Consulta)


def test_clinicasaudeperfeita_consulta_constructor_exists():
    assert callable(clinicasaudeperfeita_Consulta.__init__)


def test_clinicasaudeperfeita_consulta_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "medico" in params, "Missing parameter 'medico'"
    assert "medicamentos" in params, "Missing parameter 'medicamentos'"
    assert "data" in params, "Missing parameter 'data'"
    assert "problemasPaciente" in params, "Missing parameter 'problemasPaciente'"
    assert "orientacoesMedicas" in params, "Missing parameter 'orientacoesMedicas'"
    assert "paciente" in params, "Missing parameter 'paciente'"
    assert "exame" in params, "Missing parameter 'exame'"
    assert "marcada" in params, "Missing parameter 'marcada'"
    assert "realizada" in params, "Missing parameter 'realizada'"
    assert "hora" in params, "Missing parameter 'hora'"

def test_clinicasaudeperfeita_consulta_has_medico():
    assert hasattr(clinicasaudeperfeita_Consulta, "medico")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "medico" in klass.__dict__:
            descriptor = klass.__dict__["medico"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_medicamentos():
    assert hasattr(clinicasaudeperfeita_Consulta, "medicamentos")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "medicamentos" in klass.__dict__:
            descriptor = klass.__dict__["medicamentos"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_data():
    assert hasattr(clinicasaudeperfeita_Consulta, "data")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_problemasPaciente():
    assert hasattr(clinicasaudeperfeita_Consulta, "problemasPaciente")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "problemasPaciente" in klass.__dict__:
            descriptor = klass.__dict__["problemasPaciente"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_orientacoesMedicas():
    assert hasattr(clinicasaudeperfeita_Consulta, "orientacoesMedicas")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "orientacoesMedicas" in klass.__dict__:
            descriptor = klass.__dict__["orientacoesMedicas"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_paciente():
    assert hasattr(clinicasaudeperfeita_Consulta, "paciente")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "paciente" in klass.__dict__:
            descriptor = klass.__dict__["paciente"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_exame():
    assert hasattr(clinicasaudeperfeita_Consulta, "exame")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "exame" in klass.__dict__:
            descriptor = klass.__dict__["exame"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_marcada():
    assert hasattr(clinicasaudeperfeita_Consulta, "marcada")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "marcada" in klass.__dict__:
            descriptor = klass.__dict__["marcada"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_realizada():
    assert hasattr(clinicasaudeperfeita_Consulta, "realizada")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "realizada" in klass.__dict__:
            descriptor = klass.__dict__["realizada"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_consulta_has_hora():
    assert hasattr(clinicasaudeperfeita_Consulta, "hora")
    descriptor = None
    for klass in clinicasaudeperfeita_Consulta.__mro__:
        if "hora" in klass.__dict__:
            descriptor = klass.__dict__["hora"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_compromisso_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Compromisso)


def test_clinicasaudeperfeita_compromisso_constructor_exists():
    assert callable(clinicasaudeperfeita_Compromisso.__init__)


def test_clinicasaudeperfeita_compromisso_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Compromisso.__init__)
    params = list(sig.parameters.keys())
    assert "hora" in params, "Missing parameter 'hora'"
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "data" in params, "Missing parameter 'data'"

def test_clinicasaudeperfeita_compromisso_has_hora():
    assert hasattr(clinicasaudeperfeita_Compromisso, "hora")
    descriptor = None
    for klass in clinicasaudeperfeita_Compromisso.__mro__:
        if "hora" in klass.__dict__:
            descriptor = klass.__dict__["hora"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_compromisso_has_descricao():
    assert hasattr(clinicasaudeperfeita_Compromisso, "descricao")
    descriptor = None
    for klass in clinicasaudeperfeita_Compromisso.__mro__:
        if "descricao" in klass.__dict__:
            descriptor = klass.__dict__["descricao"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_compromisso_has_data():
    assert hasattr(clinicasaudeperfeita_Compromisso, "data")
    descriptor = None
    for klass in clinicasaudeperfeita_Compromisso.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_clinicasaudeperfeita_paciente_is_not_abstract():
    assert not inspect.isabstract(clinicasaudeperfeita_Paciente)


def test_clinicasaudeperfeita_paciente_constructor_exists():
    assert callable(clinicasaudeperfeita_Paciente.__init__)


def test_clinicasaudeperfeita_paciente_constructor_args():
    sig = inspect.signature(clinicasaudeperfeita_Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "idade" in params, "Missing parameter 'idade'"
    assert "cSus" in params, "Missing parameter 'cSus'"

def test_clinicasaudeperfeita_paciente_has_cpf():
    assert hasattr(clinicasaudeperfeita_Paciente, "cpf")
    descriptor = None
    for klass in clinicasaudeperfeita_Paciente.__mro__:
        if "cpf" in klass.__dict__:
            descriptor = klass.__dict__["cpf"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_paciente_has_nome():
    assert hasattr(clinicasaudeperfeita_Paciente, "nome")
    descriptor = None
    for klass in clinicasaudeperfeita_Paciente.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_paciente_has_idade():
    assert hasattr(clinicasaudeperfeita_Paciente, "idade")
    descriptor = None
    for klass in clinicasaudeperfeita_Paciente.__mro__:
        if "idade" in klass.__dict__:
            descriptor = klass.__dict__["idade"]
            break
    assert isinstance(descriptor, property)

def test_clinicasaudeperfeita_paciente_has_cSus():
    assert hasattr(clinicasaudeperfeita_Paciente, "cSus")
    descriptor = None
    for klass in clinicasaudeperfeita_Paciente.__mro__:
        if "cSus" in klass.__dict__:
            descriptor = klass.__dict__["cSus"]
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
clinicasaudeperfeita_Consulta_UseCase_strategy = st.builds(
    clinicasaudeperfeita_Consulta_UseCase,
)
clinicasaudeperfeita_Medico_Actor_strategy = st.builds(
    clinicasaudeperfeita_Medico_Actor,
)
clinicasaudeperfeita_Marca_consulta_UseCase_strategy = st.builds(
    clinicasaudeperfeita_Marca_consulta_UseCase,
)
clinicasaudeperfeita_Recepcionista_Actor_strategy = st.builds(
    clinicasaudeperfeita_Recepcionista_Actor,
)
clinicasaudeperfeita_Analisa_consulta_UseCase_strategy = st.builds(
    clinicasaudeperfeita_Analisa_consulta_UseCase,
)
clinicasaudeperfeita_Paciente_Actor_strategy = st.builds(
    clinicasaudeperfeita_Paciente_Actor,
)
Exame_strategy = st.builds(
    Exame,
)
clinicasaudeperfeita_Medico_strategy = st.builds(
    clinicasaudeperfeita_Medico,
    idade=
        st.integers(),
    cpf=
        safe_text,
    agenda=
        st.none(),
    nome=
        safe_text
)
clinicasaudeperfeita_Recepcionista_strategy = st.builds(
    clinicasaudeperfeita_Recepcionista,
    cpf=
        safe_text,
    nome=
        safe_text,
    idade=
        st.integers()
)
clinicasaudeperfeita_Medicamento_strategy = st.builds(
    clinicasaudeperfeita_Medicamento,
    nome=
        safe_text
)
clinicasaudeperfeita_Exame_strategy = st.builds(
    clinicasaudeperfeita_Exame,
    nome=
        safe_text
)
clinicasaudeperfeita_Consulta_strategy = st.builds(
    clinicasaudeperfeita_Consulta,
    medico=
        st.none(),
    medicamentos=
        st.none(),
    data=
        safe_text,
    problemasPaciente=
        safe_text,
    orientacoesMedicas=
        safe_text,
    paciente=
        st.none(),
    exame=
        st.none(),
    marcada=
        st.booleans(),
    realizada=
        st.booleans(),
    hora=
        safe_text
)
clinicasaudeperfeita_Compromisso_strategy = st.builds(
    clinicasaudeperfeita_Compromisso,
    hora=
        safe_text,
    descricao=
        safe_text,
    data=
        safe_text
)
clinicasaudeperfeita_Paciente_strategy = st.builds(
    clinicasaudeperfeita_Paciente,
    cpf=
        safe_text,
    nome=
        safe_text,
    idade=
        st.integers(),
    cSus=
        safe_text
)

@given(instance=clinicasaudeperfeita_Consulta_UseCase_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_consulta_usecase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Consulta_UseCase)

@given(instance=clinicasaudeperfeita_Medico_Actor_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_medico_actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Medico_Actor)

@given(instance=clinicasaudeperfeita_Marca_consulta_UseCase_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_marca_consulta_usecase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Marca_consulta_UseCase)

@given(instance=clinicasaudeperfeita_Recepcionista_Actor_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_recepcionista_actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Recepcionista_Actor)

@given(instance=clinicasaudeperfeita_Analisa_consulta_UseCase_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_analisa_consulta_usecase_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Analisa_consulta_UseCase)

@given(instance=clinicasaudeperfeita_Paciente_Actor_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_paciente_actor_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Paciente_Actor)

@given(instance=Exame_strategy)
@settings(max_examples=50)
def test_exame_instantiation(instance):
    assert isinstance(instance, Exame)

@given(instance=clinicasaudeperfeita_Medico_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_medico_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Medico)



@given(instance=clinicasaudeperfeita_Medico_strategy)
def test_clinicasaudeperfeita_medico_idade_setter(instance):
    original = instance.idade
    instance.idade = original
    assert instance.idade == original



@given(instance=clinicasaudeperfeita_Medico_strategy)
def test_clinicasaudeperfeita_medico_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=clinicasaudeperfeita_Medico_strategy)
def test_clinicasaudeperfeita_medico_agenda_setter(instance):
    original = instance.agenda
    instance.agenda = original
    assert instance.agenda == original



@given(instance=clinicasaudeperfeita_Medico_strategy)
def test_clinicasaudeperfeita_medico_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=clinicasaudeperfeita_Recepcionista_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_recepcionista_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Recepcionista)



@given(instance=clinicasaudeperfeita_Recepcionista_strategy)
def test_clinicasaudeperfeita_recepcionista_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=clinicasaudeperfeita_Recepcionista_strategy)
def test_clinicasaudeperfeita_recepcionista_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=clinicasaudeperfeita_Recepcionista_strategy)
def test_clinicasaudeperfeita_recepcionista_idade_setter(instance):
    original = instance.idade
    instance.idade = original
    assert instance.idade == original

@given(instance=clinicasaudeperfeita_Medicamento_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_medicamento_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Medicamento)



@given(instance=clinicasaudeperfeita_Medicamento_strategy)
def test_clinicasaudeperfeita_medicamento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=clinicasaudeperfeita_Exame_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_exame_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Exame)



@given(instance=clinicasaudeperfeita_Exame_strategy)
def test_clinicasaudeperfeita_exame_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=clinicasaudeperfeita_Consulta_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_consulta_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Consulta)



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_medico_setter(instance):
    original = instance.medico
    instance.medico = original
    assert instance.medico == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_medicamentos_setter(instance):
    original = instance.medicamentos
    instance.medicamentos = original
    assert instance.medicamentos == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_problemasPaciente_setter(instance):
    original = instance.problemasPaciente
    instance.problemasPaciente = original
    assert instance.problemasPaciente == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_orientacoesMedicas_setter(instance):
    original = instance.orientacoesMedicas
    instance.orientacoesMedicas = original
    assert instance.orientacoesMedicas == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_paciente_setter(instance):
    original = instance.paciente
    instance.paciente = original
    assert instance.paciente == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_exame_setter(instance):
    original = instance.exame
    instance.exame = original
    assert instance.exame == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_marcada_setter(instance):
    original = instance.marcada
    instance.marcada = original
    assert instance.marcada == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_realizada_setter(instance):
    original = instance.realizada
    instance.realizada = original
    assert instance.realizada == original



@given(instance=clinicasaudeperfeita_Consulta_strategy)
def test_clinicasaudeperfeita_consulta_hora_setter(instance):
    original = instance.hora
    instance.hora = original
    assert instance.hora == original

@given(instance=clinicasaudeperfeita_Compromisso_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_compromisso_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Compromisso)



@given(instance=clinicasaudeperfeita_Compromisso_strategy)
def test_clinicasaudeperfeita_compromisso_hora_setter(instance):
    original = instance.hora
    instance.hora = original
    assert instance.hora == original



@given(instance=clinicasaudeperfeita_Compromisso_strategy)
def test_clinicasaudeperfeita_compromisso_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=clinicasaudeperfeita_Compromisso_strategy)
def test_clinicasaudeperfeita_compromisso_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=clinicasaudeperfeita_Paciente_strategy)
@settings(max_examples=50)
def test_clinicasaudeperfeita_paciente_instantiation(instance):
    assert isinstance(instance, clinicasaudeperfeita_Paciente)



@given(instance=clinicasaudeperfeita_Paciente_strategy)
def test_clinicasaudeperfeita_paciente_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=clinicasaudeperfeita_Paciente_strategy)
def test_clinicasaudeperfeita_paciente_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=clinicasaudeperfeita_Paciente_strategy)
def test_clinicasaudeperfeita_paciente_idade_setter(instance):
    original = instance.idade
    instance.idade = original
    assert instance.idade == original



@given(instance=clinicasaudeperfeita_Paciente_strategy)
def test_clinicasaudeperfeita_paciente_cSus_setter(instance):
    original = instance.cSus
    instance.cSus = original
    assert instance.cSus == original
