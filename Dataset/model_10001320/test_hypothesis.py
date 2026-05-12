import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Especialidade,
    ConsultaExame,
    ConsultaMedicamento,
    ConsultaCid,
    Consulta,
    Paciente,
    Medicamento,
    Exame,
    Cid,
    Agenda,
    Funcionario,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_especialidade_is_not_abstract():
    assert not inspect.isabstract(Especialidade)


def test_especialidade_constructor_exists():
    assert callable(Especialidade.__init__)


def test_especialidade_constructor_args():
    sig = inspect.signature(Especialidade.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"

def test_especialidade_has_Id():
    assert hasattr(Especialidade, "Id")
    descriptor = None
    for klass in Especialidade.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_especialidade_has_Descricao():
    assert hasattr(Especialidade, "Descricao")
    descriptor = None
    for klass in Especialidade.__mro__:
        if "Descricao" in klass.__dict__:
            descriptor = klass.__dict__["Descricao"]
            break
    assert isinstance(descriptor, property)



def test_consultaexame_is_not_abstract():
    assert not inspect.isabstract(ConsultaExame)


def test_consultaexame_constructor_exists():
    assert callable(ConsultaExame.__init__)


def test_consultaexame_constructor_args():
    sig = inspect.signature(ConsultaExame.__init__)
    params = list(sig.parameters.keys())
    assert "Entregue" in params, "Missing parameter 'Entregue'"

def test_consultaexame_has_Entregue():
    assert hasattr(ConsultaExame, "Entregue")
    descriptor = None
    for klass in ConsultaExame.__mro__:
        if "Entregue" in klass.__dict__:
            descriptor = klass.__dict__["Entregue"]
            break
    assert isinstance(descriptor, property)



def test_consultamedicamento_is_not_abstract():
    assert not inspect.isabstract(ConsultaMedicamento)


def test_consultamedicamento_constructor_exists():
    assert callable(ConsultaMedicamento.__init__)


def test_consultamedicamento_constructor_args():
    sig = inspect.signature(ConsultaMedicamento.__init__)
    params = list(sig.parameters.keys())
    assert "MedicamentoId" in params, "Missing parameter 'MedicamentoId'"
    assert "Posologia" in params, "Missing parameter 'Posologia'"

def test_consultamedicamento_has_MedicamentoId():
    assert hasattr(ConsultaMedicamento, "MedicamentoId")
    descriptor = None
    for klass in ConsultaMedicamento.__mro__:
        if "MedicamentoId" in klass.__dict__:
            descriptor = klass.__dict__["MedicamentoId"]
            break
    assert isinstance(descriptor, property)

def test_consultamedicamento_has_Posologia():
    assert hasattr(ConsultaMedicamento, "Posologia")
    descriptor = None
    for klass in ConsultaMedicamento.__mro__:
        if "Posologia" in klass.__dict__:
            descriptor = klass.__dict__["Posologia"]
            break
    assert isinstance(descriptor, property)



def test_consultacid_is_not_abstract():
    assert not inspect.isabstract(ConsultaCid)


def test_consultacid_constructor_exists():
    assert callable(ConsultaCid.__init__)


def test_consultacid_constructor_args():
    sig = inspect.signature(ConsultaCid.__init__)
    params = list(sig.parameters.keys())
    assert "ConsultaId" in params, "Missing parameter 'ConsultaId'"
    assert "CidId" in params, "Missing parameter 'CidId'"

def test_consultacid_has_ConsultaId():
    assert hasattr(ConsultaCid, "ConsultaId")
    descriptor = None
    for klass in ConsultaCid.__mro__:
        if "ConsultaId" in klass.__dict__:
            descriptor = klass.__dict__["ConsultaId"]
            break
    assert isinstance(descriptor, property)

def test_consultacid_has_CidId():
    assert hasattr(ConsultaCid, "CidId")
    descriptor = None
    for klass in ConsultaCid.__mro__:
        if "CidId" in klass.__dict__:
            descriptor = klass.__dict__["CidId"]
            break
    assert isinstance(descriptor, property)



def test_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "MedicoId" in params, "Missing parameter 'MedicoId'"
    assert "Queixas" in params, "Missing parameter 'Queixas'"
    assert "PacienteId" in params, "Missing parameter 'PacienteId'"
    assert "DataHora" in params, "Missing parameter 'DataHora'"

def test_consulta_has_MedicoId():
    assert hasattr(Consulta, "MedicoId")
    descriptor = None
    for klass in Consulta.__mro__:
        if "MedicoId" in klass.__dict__:
            descriptor = klass.__dict__["MedicoId"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_Queixas():
    assert hasattr(Consulta, "Queixas")
    descriptor = None
    for klass in Consulta.__mro__:
        if "Queixas" in klass.__dict__:
            descriptor = klass.__dict__["Queixas"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_PacienteId():
    assert hasattr(Consulta, "PacienteId")
    descriptor = None
    for klass in Consulta.__mro__:
        if "PacienteId" in klass.__dict__:
            descriptor = klass.__dict__["PacienteId"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_DataHora():
    assert hasattr(Consulta, "DataHora")
    descriptor = None
    for klass in Consulta.__mro__:
        if "DataHora" in klass.__dict__:
            descriptor = klass.__dict__["DataHora"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "NomeMae" in params, "Missing parameter 'NomeMae'"
    assert "DataNascimento" in params, "Missing parameter 'DataNascimento'"
    assert "CPF" in params, "Missing parameter 'CPF'"

def test_paciente_has_Id():
    assert hasattr(Paciente, "Id")
    descriptor = None
    for klass in Paciente.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
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

def test_paciente_has_NomeMae():
    assert hasattr(Paciente, "NomeMae")
    descriptor = None
    for klass in Paciente.__mro__:
        if "NomeMae" in klass.__dict__:
            descriptor = klass.__dict__["NomeMae"]
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



def test_medicamento_is_not_abstract():
    assert not inspect.isabstract(Medicamento)


def test_medicamento_constructor_exists():
    assert callable(Medicamento.__init__)


def test_medicamento_constructor_args():
    sig = inspect.signature(Medicamento.__init__)
    params = list(sig.parameters.keys())
    assert "Fabricante" in params, "Missing parameter 'Fabricante'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "NomeGenerico" in params, "Missing parameter 'NomeGenerico'"
    assert "NomeComercial" in params, "Missing parameter 'NomeComercial'"

def test_medicamento_has_Fabricante():
    assert hasattr(Medicamento, "Fabricante")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "Fabricante" in klass.__dict__:
            descriptor = klass.__dict__["Fabricante"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_Id():
    assert hasattr(Medicamento, "Id")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_NomeGenerico():
    assert hasattr(Medicamento, "NomeGenerico")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "NomeGenerico" in klass.__dict__:
            descriptor = klass.__dict__["NomeGenerico"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_NomeComercial():
    assert hasattr(Medicamento, "NomeComercial")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "NomeComercial" in klass.__dict__:
            descriptor = klass.__dict__["NomeComercial"]
            break
    assert isinstance(descriptor, property)



def test_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"
    assert "Codigo" in params, "Missing parameter 'Codigo'"

def test_exame_has_Id():
    assert hasattr(Exame, "Id")
    descriptor = None
    for klass in Exame.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_Descricao():
    assert hasattr(Exame, "Descricao")
    descriptor = None
    for klass in Exame.__mro__:
        if "Descricao" in klass.__dict__:
            descriptor = klass.__dict__["Descricao"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_Codigo():
    assert hasattr(Exame, "Codigo")
    descriptor = None
    for klass in Exame.__mro__:
        if "Codigo" in klass.__dict__:
            descriptor = klass.__dict__["Codigo"]
            break
    assert isinstance(descriptor, property)



def test_cid_is_not_abstract():
    assert not inspect.isabstract(Cid)


def test_cid_constructor_exists():
    assert callable(Cid.__init__)


def test_cid_constructor_args():
    sig = inspect.signature(Cid.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Codigo" in params, "Missing parameter 'Codigo'"
    assert "Descricao" in params, "Missing parameter 'Descricao'"

def test_cid_has_Id():
    assert hasattr(Cid, "Id")
    descriptor = None
    for klass in Cid.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_cid_has_Codigo():
    assert hasattr(Cid, "Codigo")
    descriptor = None
    for klass in Cid.__mro__:
        if "Codigo" in klass.__dict__:
            descriptor = klass.__dict__["Codigo"]
            break
    assert isinstance(descriptor, property)

def test_cid_has_Descricao():
    assert hasattr(Cid, "Descricao")
    descriptor = None
    for klass in Cid.__mro__:
        if "Descricao" in klass.__dict__:
            descriptor = klass.__dict__["Descricao"]
            break
    assert isinstance(descriptor, property)



def test_agenda_is_not_abstract():
    assert not inspect.isabstract(Agenda)


def test_agenda_constructor_exists():
    assert callable(Agenda.__init__)


def test_agenda_constructor_args():
    sig = inspect.signature(Agenda.__init__)
    params = list(sig.parameters.keys())



def test_funcionario_is_not_abstract():
    assert not inspect.isabstract(Funcionario)


def test_funcionario_constructor_exists():
    assert callable(Funcionario.__init__)


def test_funcionario_constructor_args():
    sig = inspect.signature(Funcionario.__init__)
    params = list(sig.parameters.keys())
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Login" in params, "Missing parameter 'Login'"
    assert "Senha" in params, "Missing parameter 'Senha'"
    assert "Perfil" in params, "Missing parameter 'Perfil'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_funcionario_has_Id():
    assert hasattr(Funcionario, "Id")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_funcionario_has_Login():
    assert hasattr(Funcionario, "Login")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "Login" in klass.__dict__:
            descriptor = klass.__dict__["Login"]
            break
    assert isinstance(descriptor, property)

def test_funcionario_has_Senha():
    assert hasattr(Funcionario, "Senha")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "Senha" in klass.__dict__:
            descriptor = klass.__dict__["Senha"]
            break
    assert isinstance(descriptor, property)

def test_funcionario_has_Perfil():
    assert hasattr(Funcionario, "Perfil")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "Perfil" in klass.__dict__:
            descriptor = klass.__dict__["Perfil"]
            break
    assert isinstance(descriptor, property)

def test_funcionario_has_Nome():
    assert hasattr(Funcionario, "Nome")
    descriptor = None
    for klass in Funcionario.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
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
Especialidade_strategy = st.builds(
    Especialidade,
    Id=
        st.integers(),
    Descricao=
        safe_text
)
ConsultaExame_strategy = st.builds(
    ConsultaExame,
    Entregue=
        st.booleans()
)
ConsultaMedicamento_strategy = st.builds(
    ConsultaMedicamento,
    MedicamentoId=
        st.none(),
    Posologia=
        safe_text
)
ConsultaCid_strategy = st.builds(
    ConsultaCid,
    ConsultaId=
        st.integers(),
    CidId=
        st.integers()
)
Consulta_strategy = st.builds(
    Consulta,
    MedicoId=
        st.none(),
    Queixas=
        safe_text,
    PacienteId=
        st.none(),
    DataHora=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    Id=
        st.integers(),
    Nome=
        safe_text,
    NomeMae=
        safe_text,
    DataNascimento=
        safe_text,
    CPF=
        safe_text
)
Medicamento_strategy = st.builds(
    Medicamento,
    Fabricante=
        safe_text,
    Id=
        st.integers(),
    NomeGenerico=
        safe_text,
    NomeComercial=
        safe_text
)
Exame_strategy = st.builds(
    Exame,
    Id=
        st.integers(),
    Descricao=
        safe_text,
    Codigo=
        safe_text
)
Cid_strategy = st.builds(
    Cid,
    Id=
        st.integers(),
    Codigo=
        safe_text,
    Descricao=
        safe_text
)
Agenda_strategy = st.builds(
    Agenda,
)
Funcionario_strategy = st.builds(
    Funcionario,
    Id=
        st.integers(),
    Login=
        safe_text,
    Senha=
        safe_text,
    Perfil=
        st.integers(),
    Nome=
        safe_text
)

@given(instance=Especialidade_strategy)
@settings(max_examples=50)
def test_especialidade_instantiation(instance):
    assert isinstance(instance, Especialidade)



@given(instance=Especialidade_strategy)
def test_especialidade_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Especialidade_strategy)
def test_especialidade_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original

@given(instance=ConsultaExame_strategy)
@settings(max_examples=50)
def test_consultaexame_instantiation(instance):
    assert isinstance(instance, ConsultaExame)



@given(instance=ConsultaExame_strategy)
def test_consultaexame_Entregue_setter(instance):
    original = instance.Entregue
    instance.Entregue = original
    assert instance.Entregue == original

@given(instance=ConsultaMedicamento_strategy)
@settings(max_examples=50)
def test_consultamedicamento_instantiation(instance):
    assert isinstance(instance, ConsultaMedicamento)



@given(instance=ConsultaMedicamento_strategy)
def test_consultamedicamento_MedicamentoId_setter(instance):
    original = instance.MedicamentoId
    instance.MedicamentoId = original
    assert instance.MedicamentoId == original



@given(instance=ConsultaMedicamento_strategy)
def test_consultamedicamento_Posologia_setter(instance):
    original = instance.Posologia
    instance.Posologia = original
    assert instance.Posologia == original

@given(instance=ConsultaCid_strategy)
@settings(max_examples=50)
def test_consultacid_instantiation(instance):
    assert isinstance(instance, ConsultaCid)



@given(instance=ConsultaCid_strategy)
def test_consultacid_ConsultaId_setter(instance):
    original = instance.ConsultaId
    instance.ConsultaId = original
    assert instance.ConsultaId == original



@given(instance=ConsultaCid_strategy)
def test_consultacid_CidId_setter(instance):
    original = instance.CidId
    instance.CidId = original
    assert instance.CidId == original

@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_consulta_MedicoId_setter(instance):
    original = instance.MedicoId
    instance.MedicoId = original
    assert instance.MedicoId == original



@given(instance=Consulta_strategy)
def test_consulta_Queixas_setter(instance):
    original = instance.Queixas
    instance.Queixas = original
    assert instance.Queixas == original



@given(instance=Consulta_strategy)
def test_consulta_PacienteId_setter(instance):
    original = instance.PacienteId
    instance.PacienteId = original
    assert instance.PacienteId == original



@given(instance=Consulta_strategy)
def test_consulta_DataHora_setter(instance):
    original = instance.DataHora
    instance.DataHora = original
    assert instance.DataHora == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_paciente_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Paciente_strategy)
def test_paciente_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original



@given(instance=Paciente_strategy)
def test_paciente_NomeMae_setter(instance):
    original = instance.NomeMae
    instance.NomeMae = original
    assert instance.NomeMae == original



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

@given(instance=Medicamento_strategy)
@settings(max_examples=50)
def test_medicamento_instantiation(instance):
    assert isinstance(instance, Medicamento)



@given(instance=Medicamento_strategy)
def test_medicamento_Fabricante_setter(instance):
    original = instance.Fabricante
    instance.Fabricante = original
    assert instance.Fabricante == original



@given(instance=Medicamento_strategy)
def test_medicamento_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Medicamento_strategy)
def test_medicamento_NomeGenerico_setter(instance):
    original = instance.NomeGenerico
    instance.NomeGenerico = original
    assert instance.NomeGenerico == original



@given(instance=Medicamento_strategy)
def test_medicamento_NomeComercial_setter(instance):
    original = instance.NomeComercial
    instance.NomeComercial = original
    assert instance.NomeComercial == original

@given(instance=Exame_strategy)
@settings(max_examples=50)
def test_exame_instantiation(instance):
    assert isinstance(instance, Exame)



@given(instance=Exame_strategy)
def test_exame_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Exame_strategy)
def test_exame_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original



@given(instance=Exame_strategy)
def test_exame_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original

@given(instance=Cid_strategy)
@settings(max_examples=50)
def test_cid_instantiation(instance):
    assert isinstance(instance, Cid)



@given(instance=Cid_strategy)
def test_cid_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Cid_strategy)
def test_cid_Codigo_setter(instance):
    original = instance.Codigo
    instance.Codigo = original
    assert instance.Codigo == original



@given(instance=Cid_strategy)
def test_cid_Descricao_setter(instance):
    original = instance.Descricao
    instance.Descricao = original
    assert instance.Descricao == original

@given(instance=Agenda_strategy)
@settings(max_examples=50)
def test_agenda_instantiation(instance):
    assert isinstance(instance, Agenda)

@given(instance=Funcionario_strategy)
@settings(max_examples=50)
def test_funcionario_instantiation(instance):
    assert isinstance(instance, Funcionario)



@given(instance=Funcionario_strategy)
def test_funcionario_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Funcionario_strategy)
def test_funcionario_Login_setter(instance):
    original = instance.Login
    instance.Login = original
    assert instance.Login == original



@given(instance=Funcionario_strategy)
def test_funcionario_Senha_setter(instance):
    original = instance.Senha
    instance.Senha = original
    assert instance.Senha == original



@given(instance=Funcionario_strategy)
def test_funcionario_Perfil_setter(instance):
    original = instance.Perfil
    instance.Perfil = original
    assert instance.Perfil == original



@given(instance=Funcionario_strategy)
def test_funcionario_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original
