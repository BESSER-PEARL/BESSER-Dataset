import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Atestado,
    Consulta,
    String_Interface,
    Triagem,
    Enfermeira,
    Medico,
    Paciente,
    Pessoa,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atestado_is_not_abstract():
    assert not inspect.isabstract(Atestado)


def test_atestado_constructor_exists():
    assert callable(Atestado.__init__)


def test_atestado_constructor_args():
    sig = inspect.signature(Atestado.__init__)
    params = list(sig.parameters.keys())
    assert "quantidadeDias" in params, "Missing parameter 'quantidadeDias'"
    assert "dataFimDoAtestado" in params, "Missing parameter 'dataFimDoAtestado'"
    assert "dataInicioDoAtestado" in params, "Missing parameter 'dataInicioDoAtestado'"
    assert "consulta" in params, "Missing parameter 'consulta'"

def test_atestado_has_quantidadeDias():
    assert hasattr(Atestado, "quantidadeDias")
    descriptor = None
    for klass in Atestado.__mro__:
        if "quantidadeDias" in klass.__dict__:
            descriptor = klass.__dict__["quantidadeDias"]
            break
    assert isinstance(descriptor, property)

def test_atestado_has_dataFimDoAtestado():
    assert hasattr(Atestado, "dataFimDoAtestado")
    descriptor = None
    for klass in Atestado.__mro__:
        if "dataFimDoAtestado" in klass.__dict__:
            descriptor = klass.__dict__["dataFimDoAtestado"]
            break
    assert isinstance(descriptor, property)

def test_atestado_has_dataInicioDoAtestado():
    assert hasattr(Atestado, "dataInicioDoAtestado")
    descriptor = None
    for klass in Atestado.__mro__:
        if "dataInicioDoAtestado" in klass.__dict__:
            descriptor = klass.__dict__["dataInicioDoAtestado"]
            break
    assert isinstance(descriptor, property)

def test_atestado_has_consulta():
    assert hasattr(Atestado, "consulta")
    descriptor = None
    for klass in Atestado.__mro__:
        if "consulta" in klass.__dict__:
            descriptor = klass.__dict__["consulta"]
            break
    assert isinstance(descriptor, property)



def test_consulta_is_not_abstract():
    assert not inspect.isabstract(Consulta)


def test_consulta_constructor_exists():
    assert callable(Consulta.__init__)


def test_consulta_constructor_args():
    sig = inspect.signature(Consulta.__init__)
    params = list(sig.parameters.keys())
    assert "codigoDiagnostico" in params, "Missing parameter 'codigoDiagnostico'"
    assert "medicamentos" in params, "Missing parameter 'medicamentos'"
    assert "medico" in params, "Missing parameter 'medico'"
    assert "triagem" in params, "Missing parameter 'triagem'"
    assert "diagnostico" in params, "Missing parameter 'diagnostico'"
    assert "atestado" in params, "Missing parameter 'atestado'"

def test_consulta_has_codigoDiagnostico():
    assert hasattr(Consulta, "codigoDiagnostico")
    descriptor = None
    for klass in Consulta.__mro__:
        if "codigoDiagnostico" in klass.__dict__:
            descriptor = klass.__dict__["codigoDiagnostico"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_medicamentos():
    assert hasattr(Consulta, "medicamentos")
    descriptor = None
    for klass in Consulta.__mro__:
        if "medicamentos" in klass.__dict__:
            descriptor = klass.__dict__["medicamentos"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_medico():
    assert hasattr(Consulta, "medico")
    descriptor = None
    for klass in Consulta.__mro__:
        if "medico" in klass.__dict__:
            descriptor = klass.__dict__["medico"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_triagem():
    assert hasattr(Consulta, "triagem")
    descriptor = None
    for klass in Consulta.__mro__:
        if "triagem" in klass.__dict__:
            descriptor = klass.__dict__["triagem"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_diagnostico():
    assert hasattr(Consulta, "diagnostico")
    descriptor = None
    for klass in Consulta.__mro__:
        if "diagnostico" in klass.__dict__:
            descriptor = klass.__dict__["diagnostico"]
            break
    assert isinstance(descriptor, property)

def test_consulta_has_atestado():
    assert hasattr(Consulta, "atestado")
    descriptor = None
    for klass in Consulta.__mro__:
        if "atestado" in klass.__dict__:
            descriptor = klass.__dict__["atestado"]
            break
    assert isinstance(descriptor, property)



def test_string_interface_is_not_abstract():
    assert not inspect.isabstract(String_Interface)


def test_string_interface_constructor_exists():
    assert callable(String_Interface.__init__)


def test_string_interface_constructor_args():
    sig = inspect.signature(String_Interface.__init__)
    params = list(sig.parameters.keys())



def test_triagem_is_not_abstract():
    assert not inspect.isabstract(Triagem)


def test_triagem_constructor_exists():
    assert callable(Triagem.__init__)


def test_triagem_constructor_args():
    sig = inspect.signature(Triagem.__init__)
    params = list(sig.parameters.keys())
    assert "IMC" in params, "Missing parameter 'IMC'"
    assert "febre" in params, "Missing parameter 'febre'"
    assert "paciente" in params, "Missing parameter 'paciente'"
    assert "altura" in params, "Missing parameter 'altura'"
    assert "enfermeira" in params, "Missing parameter 'enfermeira'"
    assert "alergias" in params, "Missing parameter 'alergias'"
    assert "temperatura" in params, "Missing parameter 'temperatura'"
    assert "pressao" in params, "Missing parameter 'pressao'"
    assert "sintoma" in params, "Missing parameter 'sintoma'"
    assert "peso" in params, "Missing parameter 'peso'"

def test_triagem_has_IMC():
    assert hasattr(Triagem, "IMC")
    descriptor = None
    for klass in Triagem.__mro__:
        if "IMC" in klass.__dict__:
            descriptor = klass.__dict__["IMC"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_febre():
    assert hasattr(Triagem, "febre")
    descriptor = None
    for klass in Triagem.__mro__:
        if "febre" in klass.__dict__:
            descriptor = klass.__dict__["febre"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_paciente():
    assert hasattr(Triagem, "paciente")
    descriptor = None
    for klass in Triagem.__mro__:
        if "paciente" in klass.__dict__:
            descriptor = klass.__dict__["paciente"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_altura():
    assert hasattr(Triagem, "altura")
    descriptor = None
    for klass in Triagem.__mro__:
        if "altura" in klass.__dict__:
            descriptor = klass.__dict__["altura"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_enfermeira():
    assert hasattr(Triagem, "enfermeira")
    descriptor = None
    for klass in Triagem.__mro__:
        if "enfermeira" in klass.__dict__:
            descriptor = klass.__dict__["enfermeira"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_alergias():
    assert hasattr(Triagem, "alergias")
    descriptor = None
    for klass in Triagem.__mro__:
        if "alergias" in klass.__dict__:
            descriptor = klass.__dict__["alergias"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_temperatura():
    assert hasattr(Triagem, "temperatura")
    descriptor = None
    for klass in Triagem.__mro__:
        if "temperatura" in klass.__dict__:
            descriptor = klass.__dict__["temperatura"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_pressao():
    assert hasattr(Triagem, "pressao")
    descriptor = None
    for klass in Triagem.__mro__:
        if "pressao" in klass.__dict__:
            descriptor = klass.__dict__["pressao"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_sintoma():
    assert hasattr(Triagem, "sintoma")
    descriptor = None
    for klass in Triagem.__mro__:
        if "sintoma" in klass.__dict__:
            descriptor = klass.__dict__["sintoma"]
            break
    assert isinstance(descriptor, property)

def test_triagem_has_peso():
    assert hasattr(Triagem, "peso")
    descriptor = None
    for klass in Triagem.__mro__:
        if "peso" in klass.__dict__:
            descriptor = klass.__dict__["peso"]
            break
    assert isinstance(descriptor, property)



def test_enfermeira_is_not_abstract():
    assert not inspect.isabstract(Enfermeira)


def test_enfermeira_constructor_exists():
    assert callable(Enfermeira.__init__)


def test_enfermeira_constructor_args():
    sig = inspect.signature(Enfermeira.__init__)
    params = list(sig.parameters.keys())
    assert "cofen" in params, "Missing parameter 'cofen'"
    assert "setor" in params, "Missing parameter 'setor'"

def test_enfermeira_has_cofen():
    assert hasattr(Enfermeira, "cofen")
    descriptor = None
    for klass in Enfermeira.__mro__:
        if "cofen" in klass.__dict__:
            descriptor = klass.__dict__["cofen"]
            break
    assert isinstance(descriptor, property)

def test_enfermeira_has_setor():
    assert hasattr(Enfermeira, "setor")
    descriptor = None
    for klass in Enfermeira.__mro__:
        if "setor" in klass.__dict__:
            descriptor = klass.__dict__["setor"]
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
    assert "especialidade" in params, "Missing parameter 'especialidade'"
    assert "setor" in params, "Missing parameter 'setor'"

def test_medico_has_crm():
    assert hasattr(Medico, "crm")
    descriptor = None
    for klass in Medico.__mro__:
        if "crm" in klass.__dict__:
            descriptor = klass.__dict__["crm"]
            break
    assert isinstance(descriptor, property)

def test_medico_has_especialidade():
    assert hasattr(Medico, "especialidade")
    descriptor = None
    for klass in Medico.__mro__:
        if "especialidade" in klass.__dict__:
            descriptor = klass.__dict__["especialidade"]
            break
    assert isinstance(descriptor, property)

def test_medico_has_setor():
    assert hasattr(Medico, "setor")
    descriptor = None
    for klass in Medico.__mro__:
        if "setor" in klass.__dict__:
            descriptor = klass.__dict__["setor"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())
    assert "responsavel" in params, "Missing parameter 'responsavel'"
    assert "numeroSus" in params, "Missing parameter 'numeroSus'"
    assert "id" in params, "Missing parameter 'id'"

def test_paciente_has_responsavel():
    assert hasattr(Paciente, "responsavel")
    descriptor = None
    for klass in Paciente.__mro__:
        if "responsavel" in klass.__dict__:
            descriptor = klass.__dict__["responsavel"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_numeroSus():
    assert hasattr(Paciente, "numeroSus")
    descriptor = None
    for klass in Paciente.__mro__:
        if "numeroSus" in klass.__dict__:
            descriptor = klass.__dict__["numeroSus"]
            break
    assert isinstance(descriptor, property)

def test_paciente_has_id():
    assert hasattr(Paciente, "id")
    descriptor = None
    for klass in Paciente.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pessoa_is_not_abstract():
    assert not inspect.isabstract(Pessoa)


def test_pessoa_constructor_exists():
    assert callable(Pessoa.__init__)


def test_pessoa_constructor_args():
    sig = inspect.signature(Pessoa.__init__)
    params = list(sig.parameters.keys())
    assert "rg" in params, "Missing parameter 'rg'"
    assert "telefone" in params, "Missing parameter 'telefone'"
    assert "estadoCivil" in params, "Missing parameter 'estadoCivil'"
    assert "sexo" in params, "Missing parameter 'sexo'"
    assert "endereco" in params, "Missing parameter 'endereco'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "dataNascimento" in params, "Missing parameter 'dataNascimento'"

def test_pessoa_has_rg():
    assert hasattr(Pessoa, "rg")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "rg" in klass.__dict__:
            descriptor = klass.__dict__["rg"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_telefone():
    assert hasattr(Pessoa, "telefone")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "telefone" in klass.__dict__:
            descriptor = klass.__dict__["telefone"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_estadoCivil():
    assert hasattr(Pessoa, "estadoCivil")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "estadoCivil" in klass.__dict__:
            descriptor = klass.__dict__["estadoCivil"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_sexo():
    assert hasattr(Pessoa, "sexo")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "sexo" in klass.__dict__:
            descriptor = klass.__dict__["sexo"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_endereco():
    assert hasattr(Pessoa, "endereco")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "endereco" in klass.__dict__:
            descriptor = klass.__dict__["endereco"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_nome():
    assert hasattr(Pessoa, "nome")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_cpf():
    assert hasattr(Pessoa, "cpf")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "cpf" in klass.__dict__:
            descriptor = klass.__dict__["cpf"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_dataNascimento():
    assert hasattr(Pessoa, "dataNascimento")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "dataNascimento" in klass.__dict__:
            descriptor = klass.__dict__["dataNascimento"]
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
Atestado_strategy = st.builds(
    Atestado,
    quantidadeDias=
        safe_text,
    dataFimDoAtestado=
        safe_text,
    dataInicioDoAtestado=
        safe_text,
    consulta=
        st.none()
)
Consulta_strategy = st.builds(
    Consulta,
    codigoDiagnostico=
        safe_text,
    medicamentos=
        safe_text,
    medico=
        st.none(),
    triagem=
        st.none(),
    diagnostico=
        safe_text,
    atestado=
        st.booleans()
)
String_Interface_strategy = st.builds(
    String_Interface,
)
Triagem_strategy = st.builds(
    Triagem,
    IMC=
        safe_text,
    febre=
        st.booleans(),
    paciente=
        st.none(),
    altura=
        safe_text,
    enfermeira=
        st.none(),
    alergias=
        safe_text,
    temperatura=
        safe_text,
    pressao=
        st.none(),
    sintoma=
        safe_text,
    peso=
        safe_text
)
Enfermeira_strategy = st.builds(
    Enfermeira,
    cofen=
        safe_text,
    setor=
        safe_text
)
Medico_strategy = st.builds(
    Medico,
    crm=
        safe_text,
    especialidade=
        safe_text,
    setor=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
    responsavel=
        st.none(),
    numeroSus=
        safe_text,
    id=
        safe_text
)
Pessoa_strategy = st.builds(
    Pessoa,
    rg=
        safe_text,
    telefone=
        safe_text,
    estadoCivil=
        safe_text,
    sexo=
        safe_text,
    endereco=
        safe_text,
    nome=
        safe_text,
    cpf=
        safe_text,
    dataNascimento=
        safe_text
)

@given(instance=Atestado_strategy)
@settings(max_examples=50)
def test_atestado_instantiation(instance):
    assert isinstance(instance, Atestado)



@given(instance=Atestado_strategy)
def test_atestado_quantidadeDias_setter(instance):
    original = instance.quantidadeDias
    instance.quantidadeDias = original
    assert instance.quantidadeDias == original



@given(instance=Atestado_strategy)
def test_atestado_dataFimDoAtestado_setter(instance):
    original = instance.dataFimDoAtestado
    instance.dataFimDoAtestado = original
    assert instance.dataFimDoAtestado == original



@given(instance=Atestado_strategy)
def test_atestado_dataInicioDoAtestado_setter(instance):
    original = instance.dataInicioDoAtestado
    instance.dataInicioDoAtestado = original
    assert instance.dataInicioDoAtestado == original



@given(instance=Atestado_strategy)
def test_atestado_consulta_setter(instance):
    original = instance.consulta
    instance.consulta = original
    assert instance.consulta == original

@given(instance=Consulta_strategy)
@settings(max_examples=50)
def test_consulta_instantiation(instance):
    assert isinstance(instance, Consulta)



@given(instance=Consulta_strategy)
def test_consulta_codigoDiagnostico_setter(instance):
    original = instance.codigoDiagnostico
    instance.codigoDiagnostico = original
    assert instance.codigoDiagnostico == original



@given(instance=Consulta_strategy)
def test_consulta_medicamentos_setter(instance):
    original = instance.medicamentos
    instance.medicamentos = original
    assert instance.medicamentos == original



@given(instance=Consulta_strategy)
def test_consulta_medico_setter(instance):
    original = instance.medico
    instance.medico = original
    assert instance.medico == original



@given(instance=Consulta_strategy)
def test_consulta_triagem_setter(instance):
    original = instance.triagem
    instance.triagem = original
    assert instance.triagem == original



@given(instance=Consulta_strategy)
def test_consulta_diagnostico_setter(instance):
    original = instance.diagnostico
    instance.diagnostico = original
    assert instance.diagnostico == original



@given(instance=Consulta_strategy)
def test_consulta_atestado_setter(instance):
    original = instance.atestado
    instance.atestado = original
    assert instance.atestado == original

@given(instance=String_Interface_strategy)
@settings(max_examples=50)
def test_string_interface_instantiation(instance):
    assert isinstance(instance, String_Interface)

@given(instance=Triagem_strategy)
@settings(max_examples=50)
def test_triagem_instantiation(instance):
    assert isinstance(instance, Triagem)



@given(instance=Triagem_strategy)
def test_triagem_IMC_setter(instance):
    original = instance.IMC
    instance.IMC = original
    assert instance.IMC == original



@given(instance=Triagem_strategy)
def test_triagem_febre_setter(instance):
    original = instance.febre
    instance.febre = original
    assert instance.febre == original



@given(instance=Triagem_strategy)
def test_triagem_paciente_setter(instance):
    original = instance.paciente
    instance.paciente = original
    assert instance.paciente == original



@given(instance=Triagem_strategy)
def test_triagem_altura_setter(instance):
    original = instance.altura
    instance.altura = original
    assert instance.altura == original



@given(instance=Triagem_strategy)
def test_triagem_enfermeira_setter(instance):
    original = instance.enfermeira
    instance.enfermeira = original
    assert instance.enfermeira == original



@given(instance=Triagem_strategy)
def test_triagem_alergias_setter(instance):
    original = instance.alergias
    instance.alergias = original
    assert instance.alergias == original



@given(instance=Triagem_strategy)
def test_triagem_temperatura_setter(instance):
    original = instance.temperatura
    instance.temperatura = original
    assert instance.temperatura == original



@given(instance=Triagem_strategy)
def test_triagem_pressao_setter(instance):
    original = instance.pressao
    instance.pressao = original
    assert instance.pressao == original



@given(instance=Triagem_strategy)
def test_triagem_sintoma_setter(instance):
    original = instance.sintoma
    instance.sintoma = original
    assert instance.sintoma == original



@given(instance=Triagem_strategy)
def test_triagem_peso_setter(instance):
    original = instance.peso
    instance.peso = original
    assert instance.peso == original

@given(instance=Enfermeira_strategy)
@settings(max_examples=50)
def test_enfermeira_instantiation(instance):
    assert isinstance(instance, Enfermeira)



@given(instance=Enfermeira_strategy)
def test_enfermeira_cofen_setter(instance):
    original = instance.cofen
    instance.cofen = original
    assert instance.cofen == original



@given(instance=Enfermeira_strategy)
def test_enfermeira_setor_setter(instance):
    original = instance.setor
    instance.setor = original
    assert instance.setor == original

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
def test_medico_especialidade_setter(instance):
    original = instance.especialidade
    instance.especialidade = original
    assert instance.especialidade == original



@given(instance=Medico_strategy)
def test_medico_setor_setter(instance):
    original = instance.setor
    instance.setor = original
    assert instance.setor == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)



@given(instance=Paciente_strategy)
def test_paciente_responsavel_setter(instance):
    original = instance.responsavel
    instance.responsavel = original
    assert instance.responsavel == original



@given(instance=Paciente_strategy)
def test_paciente_numeroSus_setter(instance):
    original = instance.numeroSus
    instance.numeroSus = original
    assert instance.numeroSus == original



@given(instance=Paciente_strategy)
def test_paciente_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Pessoa_strategy)
@settings(max_examples=50)
def test_pessoa_instantiation(instance):
    assert isinstance(instance, Pessoa)



@given(instance=Pessoa_strategy)
def test_pessoa_rg_setter(instance):
    original = instance.rg
    instance.rg = original
    assert instance.rg == original



@given(instance=Pessoa_strategy)
def test_pessoa_telefone_setter(instance):
    original = instance.telefone
    instance.telefone = original
    assert instance.telefone == original



@given(instance=Pessoa_strategy)
def test_pessoa_estadoCivil_setter(instance):
    original = instance.estadoCivil
    instance.estadoCivil = original
    assert instance.estadoCivil == original



@given(instance=Pessoa_strategy)
def test_pessoa_sexo_setter(instance):
    original = instance.sexo
    instance.sexo = original
    assert instance.sexo == original



@given(instance=Pessoa_strategy)
def test_pessoa_endereco_setter(instance):
    original = instance.endereco
    instance.endereco = original
    assert instance.endereco == original



@given(instance=Pessoa_strategy)
def test_pessoa_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Pessoa_strategy)
def test_pessoa_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=Pessoa_strategy)
def test_pessoa_dataNascimento_setter(instance):
    original = instance.dataNascimento
    instance.dataNascimento = original
    assert instance.dataNascimento == original
