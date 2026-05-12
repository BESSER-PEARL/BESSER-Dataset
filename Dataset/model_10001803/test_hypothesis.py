import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    M_dico,
    Agendamento,
    Funcion_rio,
    Consulta,
    Paciente,
    Exame,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_m_dico_is_not_abstract():
    assert not inspect.isabstract(M_dico)


def test_m_dico_constructor_exists():
    assert callable(M_dico.__init__)


def test_m_dico_constructor_args():
    sig = inspect.signature(M_dico.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "CPF" in params, "Missing parameter 'CPF'"
    assert "Especialidade" in params, "Missing parameter 'Especialidade'"

def test_m_dico_has_Nome():
    assert hasattr(M_dico, "Nome")
    descriptor = None
    for klass in M_dico.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_m_dico_has_CPF():
    assert hasattr(M_dico, "CPF")
    descriptor = None
    for klass in M_dico.__mro__:
        if "CPF" in klass.__dict__:
            descriptor = klass.__dict__["CPF"]
            break
    assert isinstance(descriptor, property)

def test_m_dico_has_Especialidade():
    assert hasattr(M_dico, "Especialidade")
    descriptor = None
    for klass in M_dico.__mro__:
        if "Especialidade" in klass.__dict__:
            descriptor = klass.__dict__["Especialidade"]
            break
    assert isinstance(descriptor, property)



def test_agendamento_is_not_abstract():
    assert not inspect.isabstract(Agendamento)


def test_agendamento_constructor_exists():
    assert callable(Agendamento.__init__)


def test_agendamento_constructor_args():
    sig = inspect.signature(Agendamento.__init__)
    params = list(sig.parameters.keys())
    assert "Dia_e_Horario" in params, "Missing parameter 'Dia_e_Horario'"
    assert "TipoAgendamento" in params, "Missing parameter 'TipoAgendamento'"
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "Medico" in params, "Missing parameter 'Medico'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"

def test_agendamento_has_Dia_e_Horario():
    assert hasattr(Agendamento, "Dia_e_Horario")
    descriptor = None
    for klass in Agendamento.__mro__:
        if "Dia_e_Horario" in klass.__dict__:
            descriptor = klass.__dict__["Dia_e_Horario"]
            break
    assert isinstance(descriptor, property)

def test_agendamento_has_TipoAgendamento():
    assert hasattr(Agendamento, "TipoAgendamento")
    descriptor = None
    for klass in Agendamento.__mro__:
        if "TipoAgendamento" in klass.__dict__:
            descriptor = klass.__dict__["TipoAgendamento"]
            break
    assert isinstance(descriptor, property)

def test_agendamento_has_Sede():
    assert hasattr(Agendamento, "Sede")
    descriptor = None
    for klass in Agendamento.__mro__:
        if "Sede" in klass.__dict__:
            descriptor = klass.__dict__["Sede"]
            break
    assert isinstance(descriptor, property)

def test_agendamento_has_Medico():
    assert hasattr(Agendamento, "Medico")
    descriptor = None
    for klass in Agendamento.__mro__:
        if "Medico" in klass.__dict__:
            descriptor = klass.__dict__["Medico"]
            break
    assert isinstance(descriptor, property)

def test_agendamento_has_Especialista():
    assert hasattr(Agendamento, "Especialista")
    descriptor = None
    for klass in Agendamento.__mro__:
        if "Especialista" in klass.__dict__:
            descriptor = klass.__dict__["Especialista"]
            break
    assert isinstance(descriptor, property)



def test_funcion_rio_is_not_abstract():
    assert not inspect.isabstract(Funcion_rio)


def test_funcion_rio_constructor_exists():
    assert callable(Funcion_rio.__init__)


def test_funcion_rio_constructor_args():
    sig = inspect.signature(Funcion_rio.__init__)
    params = list(sig.parameters.keys())
    assert "Usuario" in params, "Missing parameter 'Usuario'"
    assert "Senha" in params, "Missing parameter 'Senha'"

def test_funcion_rio_has_Usuario():
    assert hasattr(Funcion_rio, "Usuario")
    descriptor = None
    for klass in Funcion_rio.__mro__:
        if "Usuario" in klass.__dict__:
            descriptor = klass.__dict__["Usuario"]
            break
    assert isinstance(descriptor, property)

def test_funcion_rio_has_Senha():
    assert hasattr(Funcion_rio, "Senha")
    descriptor = None
    for klass in Funcion_rio.__mro__:
        if "Senha" in klass.__dict__:
            descriptor = klass.__dict__["Senha"]
            break
    assert isinstance(descriptor, property)



def test_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "TipoConsulta" in params, "Missing parameter 'TipoConsulta'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"
    assert "Medico" in params, "Missing parameter 'Medico'"

def test_consulta_has_Sede():
    assert hasattr(Consulta, "Sede")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Sede" in klass.__dict__:
            descriptor = klass.__dict__["Sede"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_TipoConsulta():
    assert hasattr(Consulta, "TipoConsulta")
    descriptor = None
    for klass in Consulta.__mro__:
        if "TipoConsulta" in klass.__dict__:
            descriptor = klass.__dict__["TipoConsulta"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_Especialista():
    assert hasattr(Consulta, "Especialista")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Especialista" in klass.__dict__:
            descriptor = klass.__dict__["Especialista"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_Medico():
    assert hasattr(Consulta, "Medico")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Medico" in klass.__dict__:
            descriptor = klass.__dict__["Medico"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "Endereco" in params, "Missing parameter 'Endereco'"
    assert "DataNascimento" in params, "Missing parameter 'DataNascimento'"
    assert "CPF" in params, "Missing parameter 'CPF'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "RG" in params, "Missing parameter 'RG'"
    assert "Telefone" in params, "Missing parameter 'Telefone'"
    assert "Sobrenome" in params, "Missing parameter 'Sobrenome'"
    assert "Estado" in params, "Missing parameter 'Estado'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "EstadoCivil" in params, "Missing parameter 'EstadoCivil'"
    assert "ConvenioMedico" in params, "Missing parameter 'ConvenioMedico'"
    assert "Nacionalidade" in params, "Missing parameter 'Nacionalidade'"
    assert "Celular" in params, "Missing parameter 'Celular'"
    assert "Cidade" in params, "Missing parameter 'Cidade'"
    assert "Sexo" in params, "Missing parameter 'Sexo'"
    assert "CEP" in params, "Missing parameter 'CEP'"
    assert "CPF1" in params, "Missing parameter 'CPF1'"

def test_paciente_has_Endereco():
    assert hasattr(Paciente, "Endereco")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Endereco" in klass.__dict__:
            descriptor = klass.__dict__["Endereco"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_DataNascimento():
    assert hasattr(Paciente, "DataNascimento")
    descriptor = None
    for klass in Paciente.__mro__:
        if "DataNascimento" in klass.__dict__:
            descriptor = klass.__dict__["DataNascimento"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_CPF():
    assert hasattr(Paciente, "CPF")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CPF" in klass.__dict__:
            descriptor = klass.__dict__["CPF"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Email():
    assert hasattr(Paciente, "Email")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_RG():
    assert hasattr(Paciente, "RG")
    descriptor = None
    for klass in Paciente.__mro__:
        if "RG" in klass.__dict__:
            descriptor = klass.__dict__["RG"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Telefone():
    assert hasattr(Paciente, "Telefone")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Telefone" in klass.__dict__:
            descriptor = klass.__dict__["Telefone"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Sobrenome():
    assert hasattr(Paciente, "Sobrenome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Sobrenome" in klass.__dict__:
            descriptor = klass.__dict__["Sobrenome"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Estado():
    assert hasattr(Paciente, "Estado")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Estado" in klass.__dict__:
            descriptor = klass.__dict__["Estado"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Nome():
    assert hasattr(Paciente, "Nome")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_EstadoCivil():
    assert hasattr(Paciente, "EstadoCivil")
    descriptor = None
    for klass in Paciente.__mro__:
        if "EstadoCivil" in klass.__dict__:
            descriptor = klass.__dict__["EstadoCivil"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_ConvenioMedico():
    assert hasattr(Paciente, "ConvenioMedico")
    descriptor = None
    for klass in Paciente.__mro__:
        if "ConvenioMedico" in klass.__dict__:
            descriptor = klass.__dict__["ConvenioMedico"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Nacionalidade():
    assert hasattr(Paciente, "Nacionalidade")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Nacionalidade" in klass.__dict__:
            descriptor = klass.__dict__["Nacionalidade"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Celular():
    assert hasattr(Paciente, "Celular")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Celular" in klass.__dict__:
            descriptor = klass.__dict__["Celular"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Cidade():
    assert hasattr(Paciente, "Cidade")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Cidade" in klass.__dict__:
            descriptor = klass.__dict__["Cidade"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_Sexo():
    assert hasattr(Paciente, "Sexo")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Sexo" in klass.__dict__:
            descriptor = klass.__dict__["Sexo"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_CEP():
    assert hasattr(Paciente, "CEP")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CEP" in klass.__dict__:
            descriptor = klass.__dict__["CEP"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_CPF1():
    assert hasattr(Paciente, "CPF1")
    descriptor = None
    for klass in Paciente.__mro__:
        if "CPF1" in klass.__dict__:
            descriptor = klass.__dict__["CPF1"]
            break
    assert isinstance(descriptor, property)



def test_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "TipoExame" in params, "Missing parameter 'TipoExame'"
    assert "Sede" in params, "Missing parameter 'Sede'"
    assert "Especialista" in params, "Missing parameter 'Especialista'"
    assert "Medico" in params, "Missing parameter 'Medico'"

def test_exame_has_TipoExame():
    assert hasattr(Exame, "TipoExame")
    descriptor = None
    for klass in Exame.__mro__:
        if "TipoExame" in klass.__dict__:
            descriptor = klass.__dict__["TipoExame"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_Sede():
    assert hasattr(Exame, "Sede")
    descriptor = None
    for klass in Exame.__mro__:
        if "Sede" in klass.__dict__:
            descriptor = klass.__dict__["Sede"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_Especialista():
    assert hasattr(Exame, "Especialista")
    descriptor = None
    for klass in Exame.__mro__:
        if "Especialista" in klass.__dict__:
            descriptor = klass.__dict__["Especialista"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_Medico():
    assert hasattr(Exame, "Medico")
    descriptor = None
    for klass in Exame.__mro__:
        if "Medico" in klass.__dict__:
            descriptor = klass.__dict__["Medico"]
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
M_dico_strategy = st.builds(
    M_dico,
    Nome=
        safe_text,
    CPF=
        st.integers(),
    Especialidade=
        safe_text
)
Agendamento_strategy = st.builds(
    Agendamento,
    Dia_e_Horario=
        safe_text,
    TipoAgendamento=
        safe_text,
    Sede=
        safe_text,
    Medico=
        safe_text,
    Especialista=
        safe_text
)
Funcion_rio_strategy = st.builds(
    Funcion_rio,
    Usuario=
        safe_text,
    Senha=
        safe_text
)
Consulta_strategy = st.builds(
    Consulta,
    Sede=
        safe_text,
    TipoConsulta=
        safe_text,
    Especialista=
        safe_text,
    Medico=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    Endereco=
        safe_text,
    DataNascimento=
        safe_text,
    CPF=
        st.none(),
    Email=
        safe_text,
    RG=
        st.integers(),
    Telefone=
        st.integers(),
    Sobrenome=
        safe_text,
    Estado=
        safe_text,
    Nome=
        safe_text,
    EstadoCivil=
        safe_text,
    ConvenioMedico=
        safe_text,
    Nacionalidade=
        safe_text,
    Celular=
        st.integers(),
    Cidade=
        safe_text,
    Sexo=
        safe_text,
    CEP=
        st.integers(),
    CPF1=
        st.integers()
)
Exame_strategy = st.builds(
    Exame,
    TipoExame=
        safe_text,
    Sede=
        safe_text,
    Especialista=
        safe_text,
    Medico=
        safe_text
)

@given(instance=M_dico_strategy)
@settings(max_examples=50)
def test_m_dico_instantiation(instance):
    assert isinstance(instance, M_dico)



@given(instance=M_dico_strategy)
def test_m_dico_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=M_dico_strategy)
def test_m_dico_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original



@given(instance=M_dico_strategy)
def test_m_dico_Especialidade_setter(instance):
    original = instance.Especialidade
    instance.Especialidade = original
    assert instance.Especialidade == original

@given(instance=Agendamento_strategy)
@settings(max_examples=50)
def test_agendamento_instantiation(instance):
    assert isinstance(instance, Agendamento)



@given(instance=Agendamento_strategy)
def test_agendamento_Dia_e_Horario_setter(instance):
    original = instance.Dia_e_Horario
    instance.Dia_e_Horario = original
    assert instance.Dia_e_Horario == original



@given(instance=Agendamento_strategy)
def test_agendamento_TipoAgendamento_setter(instance):
    original = instance.TipoAgendamento
    instance.TipoAgendamento = original
    assert instance.TipoAgendamento == original



@given(instance=Agendamento_strategy)
def test_agendamento_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Agendamento_strategy)
def test_agendamento_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original



@given(instance=Agendamento_strategy)
def test_agendamento_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original

@given(instance=Funcion_rio_strategy)
@settings(max_examples=50)
def test_funcion_rio_instantiation(instance):
    assert isinstance(instance, Funcion_rio)



@given(instance=Funcion_rio_strategy)
def test_funcion_rio_Usuario_setter(instance):
    original = instance.Usuario
    instance.Usuario = original
    assert instance.Usuario == original



@given(instance=Funcion_rio_strategy)
def test_funcion_rio_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original

@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_consulta_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Consulta_strategy)
def test_consulta_TipoConsulta_setter(instance):
    original = instance.TipoConsulta
    instance.TipoConsulta = original
    assert instance.TipoConsulta == original



@given(instance=Consulta_strategy)
def test_consulta_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original



@given(instance=Consulta_strategy)
def test_consulta_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_paciente_Endereco_setter(instance):
    original = instance.Endereco
    instance.Endereco = original
    assert instance.Endereco == original



@given(instance=Paciente_strategy)
def test_paciente_DataNascimento_setter(instance):
    original = instance.DataNascimento
    instance.DataNascimento = original
    assert instance.DataNascimento == original



@given(instance=Paciente_strategy)
def test_paciente_CPF_setter(instance):
    original = instance.CPF
    instance.CPF = original
    assert instance.CPF == original



@given(instance=Paciente_strategy)
def test_paciente_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Paciente_strategy)
def test_paciente_RG_setter(instance):
    original = instance.RG
    instance.RG = original
    assert instance.RG == original



@given(instance=Paciente_strategy)
def test_paciente_Telefone_setter(instance):
    original = instance.Telefone
    instance.Telefone = original
    assert instance.Telefone == original



@given(instance=Paciente_strategy)
def test_paciente_Sobrenome_setter(instance):
    original = instance.Sobrenome
    instance.Sobrenome = original
    assert instance.Sobrenome == original



@given(instance=Paciente_strategy)
def test_paciente_Estado_setter(instance):
    original = instance.Estado
    instance.Estado = original
    assert instance.Estado == original



@given(instance=Paciente_strategy)
def test_paciente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Paciente_strategy)
def test_paciente_EstadoCivil_setter(instance):
    original = instance.EstadoCivil
    instance.EstadoCivil = original
    assert instance.EstadoCivil == original



@given(instance=Paciente_strategy)
def test_paciente_ConvenioMedico_setter(instance):
    original = instance.ConvenioMedico
    instance.ConvenioMedico = original
    assert instance.ConvenioMedico == original



@given(instance=Paciente_strategy)
def test_paciente_Nacionalidade_setter(instance):
    original = instance.Nacionalidade
    instance.Nacionalidade = original
    assert instance.Nacionalidade == original



@given(instance=Paciente_strategy)
def test_paciente_Celular_setter(instance):
    original = instance.Celular
    instance.Celular = original
    assert instance.Celular == original



@given(instance=Paciente_strategy)
def test_paciente_Cidade_setter(instance):
    original = instance.Cidade
    instance.Cidade = original
    assert instance.Cidade == original



@given(instance=Paciente_strategy)
def test_paciente_Sexo_setter(instance):
    original = instance.Sexo
    instance.Sexo = original
    assert instance.Sexo == original



@given(instance=Paciente_strategy)
def test_paciente_CEP_setter(instance):
    original = instance.CEP
    instance.CEP = original
    assert instance.CEP == original



@given(instance=Paciente_strategy)
def test_paciente_CPF1_setter(instance):
    original = instance.CPF1
    instance.CPF1 = original
    assert instance.CPF1 == original

@given(instance=Exame_strategy)
@settings(max_examples=50)
def test_exame_instantiation(instance):
    assert isinstance(instance, Exame)



@given(instance=Exame_strategy)
def test_exame_TipoExame_setter(instance):
    original = instance.TipoExame
    instance.TipoExame = original
    assert instance.TipoExame == original



@given(instance=Exame_strategy)
def test_exame_Sede_setter(instance):
    original = instance.Sede
    instance.Sede = original
    assert instance.Sede == original



@given(instance=Exame_strategy)
def test_exame_Especialista_setter(instance):
    original = instance.Especialista
    instance.Especialista = original
    assert instance.Especialista == original



@given(instance=Exame_strategy)
def test_exame_Medico_setter(instance):
    original = instance.Medico
    instance.Medico = original
    assert instance.Medico == original
