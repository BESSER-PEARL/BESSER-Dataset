import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    LinhaCuidado,
    Mensagem,
    ProfissionalSaude,
    Naturalidade,
    Medicamento,
    Paciente,
    Telefone,
    Pessoa,
    Endereco,
    Exame,
    LocalExame,
    TipoMedicamento,
    TipoSanguineo,
    Interacao,
    enu,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_linhacuidado_is_not_abstract():
    assert not inspect.isabstract(LinhaCuidado)


def test_linhacuidado_constructor_exists():
    assert callable(LinhaCuidado.__init__)


def test_linhacuidado_constructor_args():
    sig = inspect.signature(LinhaCuidado.__init__)
    params = list(sig.parameters.keys())
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "nome" in params, "Missing parameter 'nome'"

def test_linhacuidado_has_descricao():
    assert hasattr(LinhaCuidado, "descricao")
    descriptor = None
    for klass in LinhaCuidado.__mro__:
        if "descricao" in klass.__dict__:
            descriptor = klass.__dict__["descricao"]
            break
    assert isinstance(descriptor, property)

def test_linhacuidado_has_nome():
    assert hasattr(LinhaCuidado, "nome")
    descriptor = None
    for klass in LinhaCuidado.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_mensagem_is_not_abstract():
    assert not inspect.isabstract(Mensagem)


def test_mensagem_constructor_exists():
    assert callable(Mensagem.__init__)


def test_mensagem_constructor_args():
    sig = inspect.signature(Mensagem.__init__)
    params = list(sig.parameters.keys())
    assert "mensagem" in params, "Missing parameter 'mensagem'"
    assert "dataEnvio" in params, "Missing parameter 'dataEnvio'"
    assert "geral" in params, "Missing parameter 'geral'"
    assert "assunto" in params, "Missing parameter 'assunto'"

def test_mensagem_has_mensagem():
    assert hasattr(Mensagem, "mensagem")
    descriptor = None
    for klass in Mensagem.__mro__:
        if "mensagem" in klass.__dict__:
            descriptor = klass.__dict__["mensagem"]
            break
    assert isinstance(descriptor, property)

def test_mensagem_has_dataEnvio():
    assert hasattr(Mensagem, "dataEnvio")
    descriptor = None
    for klass in Mensagem.__mro__:
        if "dataEnvio" in klass.__dict__:
            descriptor = klass.__dict__["dataEnvio"]
            break
    assert isinstance(descriptor, property)

def test_mensagem_has_geral():
    assert hasattr(Mensagem, "geral")
    descriptor = None
    for klass in Mensagem.__mro__:
        if "geral" in klass.__dict__:
            descriptor = klass.__dict__["geral"]
            break
    assert isinstance(descriptor, property)

def test_mensagem_has_assunto():
    assert hasattr(Mensagem, "assunto")
    descriptor = None
    for klass in Mensagem.__mro__:
        if "assunto" in klass.__dict__:
            descriptor = klass.__dict__["assunto"]
            break
    assert isinstance(descriptor, property)



def test_profissionalsaude_is_not_abstract():
    assert not inspect.isabstract(ProfissionalSaude)


def test_profissionalsaude_constructor_exists():
    assert callable(ProfissionalSaude.__init__)


def test_profissionalsaude_constructor_args():
    sig = inspect.signature(ProfissionalSaude.__init__)
    params = list(sig.parameters.keys())



def test_naturalidade_is_not_abstract():
    assert not inspect.isabstract(Naturalidade)


def test_naturalidade_constructor_exists():
    assert callable(Naturalidade.__init__)


def test_naturalidade_constructor_args():
    sig = inspect.signature(Naturalidade.__init__)
    params = list(sig.parameters.keys())
    assert "naturalidade" in params, "Missing parameter 'naturalidade'"

def test_naturalidade_has_naturalidade():
    assert hasattr(Naturalidade, "naturalidade")
    descriptor = None
    for klass in Naturalidade.__mro__:
        if "naturalidade" in klass.__dict__:
            descriptor = klass.__dict__["naturalidade"]
            break
    assert isinstance(descriptor, property)



def test_medicamento_is_not_abstract():
    assert not inspect.isabstract(Medicamento)


def test_medicamento_constructor_exists():
    assert callable(Medicamento.__init__)


def test_medicamento_constructor_args():
    sig = inspect.signature(Medicamento.__init__)
    params = list(sig.parameters.keys())
    assert "ativo" in params, "Missing parameter 'ativo'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "intervaloTempo" in params, "Missing parameter 'intervaloTempo'"
    assert "horaInicial" in params, "Missing parameter 'horaInicial'"
    assert "dataFim" in params, "Missing parameter 'dataFim'"
    assert "descricao" in params, "Missing parameter 'descricao'"
    assert "dataInicio" in params, "Missing parameter 'dataInicio'"

def test_medicamento_has_ativo():
    assert hasattr(Medicamento, "ativo")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "ativo" in klass.__dict__:
            descriptor = klass.__dict__["ativo"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_nome():
    assert hasattr(Medicamento, "nome")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_intervaloTempo():
    assert hasattr(Medicamento, "intervaloTempo")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "intervaloTempo" in klass.__dict__:
            descriptor = klass.__dict__["intervaloTempo"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_horaInicial():
    assert hasattr(Medicamento, "horaInicial")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "horaInicial" in klass.__dict__:
            descriptor = klass.__dict__["horaInicial"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_dataFim():
    assert hasattr(Medicamento, "dataFim")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "dataFim" in klass.__dict__:
            descriptor = klass.__dict__["dataFim"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_descricao():
    assert hasattr(Medicamento, "descricao")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "descricao" in klass.__dict__:
            descriptor = klass.__dict__["descricao"]
            break
    assert isinstance(descriptor, property)

def test_medicamento_has_dataInicio():
    assert hasattr(Medicamento, "dataInicio")
    descriptor = None
    for klass in Medicamento.__mro__:
        if "dataInicio" in klass.__dict__:
            descriptor = klass.__dict__["dataInicio"]
            break
    assert isinstance(descriptor, property)



def test_paciente_is_not_abstract():
    assert not inspect.isabstract(Paciente)


def test_paciente_constructor_exists():
    assert callable(Paciente.__init__)


def test_paciente_constructor_args():
    sig = inspect.signature(Paciente.__init__)
    params = list(sig.parameters.keys())



def test_telefone_is_not_abstract():
    assert not inspect.isabstract(Telefone)


def test_telefone_constructor_exists():
    assert callable(Telefone.__init__)


def test_telefone_constructor_args():
    sig = inspect.signature(Telefone.__init__)
    params = list(sig.parameters.keys())
    assert "ddd" in params, "Missing parameter 'ddd'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "tipo" in params, "Missing parameter 'tipo'"

def test_telefone_has_ddd():
    assert hasattr(Telefone, "ddd")
    descriptor = None
    for klass in Telefone.__mro__:
        if "ddd" in klass.__dict__:
            descriptor = klass.__dict__["ddd"]
            break
    assert isinstance(descriptor, property)

def test_telefone_has_numero():
    assert hasattr(Telefone, "numero")
    descriptor = None
    for klass in Telefone.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_telefone_has_tipo():
    assert hasattr(Telefone, "tipo")
    descriptor = None
    for klass in Telefone.__mro__:
        if "tipo" in klass.__dict__:
            descriptor = klass.__dict__["tipo"]
            break
    assert isinstance(descriptor, property)



def test_pessoa_is_not_abstract():
    assert not inspect.isabstract(Pessoa)


def test_pessoa_constructor_exists():
    assert callable(Pessoa.__init__)


def test_pessoa_constructor_args():
    sig = inspect.signature(Pessoa.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "sexo" in params, "Missing parameter 'sexo'"
    assert "dataInclusao" in params, "Missing parameter 'dataInclusao'"
    assert "cpf" in params, "Missing parameter 'cpf'"
    assert "ultimoAcesso" in params, "Missing parameter 'ultimoAcesso'"
    assert "senha" in params, "Missing parameter 'senha'"
    assert "dataNascimento" in params, "Missing parameter 'dataNascimento'"

def test_pessoa_has_email():
    assert hasattr(Pessoa, "email")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
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

def test_pessoa_has_dataInclusao():
    assert hasattr(Pessoa, "dataInclusao")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "dataInclusao" in klass.__dict__:
            descriptor = klass.__dict__["dataInclusao"]
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

def test_pessoa_has_ultimoAcesso():
    assert hasattr(Pessoa, "ultimoAcesso")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "ultimoAcesso" in klass.__dict__:
            descriptor = klass.__dict__["ultimoAcesso"]
            break
    assert isinstance(descriptor, property)

def test_pessoa_has_senha():
    assert hasattr(Pessoa, "senha")
    descriptor = None
    for klass in Pessoa.__mro__:
        if "senha" in klass.__dict__:
            descriptor = klass.__dict__["senha"]
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



def test_endereco_is_not_abstract():
    assert not inspect.isabstract(Endereco)


def test_endereco_constructor_exists():
    assert callable(Endereco.__init__)


def test_endereco_constructor_args():
    sig = inspect.signature(Endereco.__init__)
    params = list(sig.parameters.keys())
    assert "logradouro" in params, "Missing parameter 'logradouro'"
    assert "cep" in params, "Missing parameter 'cep'"
    assert "numero" in params, "Missing parameter 'numero'"
    assert "bairro" in params, "Missing parameter 'bairro'"
    assert "cidade" in params, "Missing parameter 'cidade'"

def test_endereco_has_logradouro():
    assert hasattr(Endereco, "logradouro")
    descriptor = None
    for klass in Endereco.__mro__:
        if "logradouro" in klass.__dict__:
            descriptor = klass.__dict__["logradouro"]
            break
    assert isinstance(descriptor, property)

def test_endereco_has_cep():
    assert hasattr(Endereco, "cep")
    descriptor = None
    for klass in Endereco.__mro__:
        if "cep" in klass.__dict__:
            descriptor = klass.__dict__["cep"]
            break
    assert isinstance(descriptor, property)

def test_endereco_has_numero():
    assert hasattr(Endereco, "numero")
    descriptor = None
    for klass in Endereco.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_endereco_has_bairro():
    assert hasattr(Endereco, "bairro")
    descriptor = None
    for klass in Endereco.__mro__:
        if "bairro" in klass.__dict__:
            descriptor = klass.__dict__["bairro"]
            break
    assert isinstance(descriptor, property)

def test_endereco_has_cidade():
    assert hasattr(Endereco, "cidade")
    descriptor = None
    for klass in Endereco.__mro__:
        if "cidade" in klass.__dict__:
            descriptor = klass.__dict__["cidade"]
            break
    assert isinstance(descriptor, property)



def test_exame_is_not_abstract():
    assert not inspect.isabstract(Exame)


def test_exame_constructor_exists():
    assert callable(Exame.__init__)


def test_exame_constructor_args():
    sig = inspect.signature(Exame.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "nome" in params, "Missing parameter 'nome'"
    assert "descricao" in params, "Missing parameter 'descricao'"

def test_exame_has_data():
    assert hasattr(Exame, "data")
    descriptor = None
    for klass in Exame.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_exame_has_nome():
    assert hasattr(Exame, "nome")
    descriptor = None
    for klass in Exame.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
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



def test_localexame_is_not_abstract():
    assert not inspect.isabstract(LocalExame)


def test_localexame_constructor_exists():
    assert callable(LocalExame.__init__)


def test_localexame_constructor_args():
    sig = inspect.signature(LocalExame.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_localexame_has_nome():
    assert hasattr(LocalExame, "nome")
    descriptor = None
    for klass in LocalExame.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_tipomedicamento_is_not_abstract():
    assert not inspect.isabstract(TipoMedicamento)


def test_tipomedicamento_constructor_exists():
    assert callable(TipoMedicamento.__init__)


def test_tipomedicamento_constructor_args():
    sig = inspect.signature(TipoMedicamento.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_tipomedicamento_has_nome():
    assert hasattr(TipoMedicamento, "nome")
    descriptor = None
    for klass in TipoMedicamento.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_tiposanguineo_is_not_abstract():
    assert not inspect.isabstract(TipoSanguineo)


def test_tiposanguineo_constructor_exists():
    assert callable(TipoSanguineo.__init__)


def test_tiposanguineo_constructor_args():
    sig = inspect.signature(TipoSanguineo.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_tiposanguineo_has_nome():
    assert hasattr(TipoSanguineo, "nome")
    descriptor = None
    for klass in TipoSanguineo.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_interacao_is_not_abstract():
    assert not inspect.isabstract(Interacao)


def test_interacao_constructor_exists():
    assert callable(Interacao.__init__)


def test_interacao_constructor_args():
    sig = inspect.signature(Interacao.__init__)
    params = list(sig.parameters.keys())

def test_enu_exists():
    # Check that the Enumeration exists
    assert enu is not None

def test_enu_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in enu]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in enu"


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
LinhaCuidado_strategy = st.builds(
    LinhaCuidado,
    descricao=
        st.integers(),
    nome=
        safe_text
)
Mensagem_strategy = st.builds(
    Mensagem,
    mensagem=
        safe_text,
    dataEnvio=
        safe_text,
    geral=
        st.booleans(),
    assunto=
        safe_text
)
ProfissionalSaude_strategy = st.builds(
    ProfissionalSaude,
)
Naturalidade_strategy = st.builds(
    Naturalidade,
    naturalidade=
        safe_text
)
Medicamento_strategy = st.builds(
    Medicamento,
    ativo=
        st.booleans(),
    nome=
        safe_text,
    intervaloTempo=
        st.integers(),
    horaInicial=
        safe_text,
    dataFim=
        safe_text,
    descricao=
        safe_text,
    dataInicio=
        safe_text
)
Paciente_strategy = st.builds(
    Paciente,
)
Telefone_strategy = st.builds(
    Telefone,
    ddd=
        st.integers(),
    numero=
        safe_text,
    tipo=
        safe_text
)
Pessoa_strategy = st.builds(
    Pessoa,
    email=
        safe_text,
    sexo=
        safe_text,
    dataInclusao=
        safe_text,
    cpf=
        safe_text,
    ultimoAcesso=
        safe_text,
    senha=
        safe_text,
    dataNascimento=
        safe_text
)
Endereco_strategy = st.builds(
    Endereco,
    logradouro=
        safe_text,
    cep=
        safe_text,
    numero=
        st.integers(),
    bairro=
        safe_text,
    cidade=
        safe_text
)
Exame_strategy = st.builds(
    Exame,
    data=
        safe_text,
    nome=
        safe_text,
    descricao=
        safe_text
)
LocalExame_strategy = st.builds(
    LocalExame,
    nome=
        safe_text
)
TipoMedicamento_strategy = st.builds(
    TipoMedicamento,
    nome=
        safe_text
)
TipoSanguineo_strategy = st.builds(
    TipoSanguineo,
    nome=
        safe_text
)
Interacao_strategy = st.builds(
    Interacao,
)

@given(instance=LinhaCuidado_strategy)
@settings(max_examples=50)
def test_linhacuidado_instantiation(instance):
    assert isinstance(instance, LinhaCuidado)



@given(instance=LinhaCuidado_strategy)
def test_linhacuidado_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=LinhaCuidado_strategy)
def test_linhacuidado_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=Mensagem_strategy)
@settings(max_examples=50)
def test_mensagem_instantiation(instance):
    assert isinstance(instance, Mensagem)



@given(instance=Mensagem_strategy)
def test_mensagem_mensagem_setter(instance):
    original = instance.mensagem
    instance.mensagem = original
    assert instance.mensagem == original



@given(instance=Mensagem_strategy)
def test_mensagem_dataEnvio_setter(instance):
    original = instance.dataEnvio
    instance.dataEnvio = original
    assert instance.dataEnvio == original



@given(instance=Mensagem_strategy)
def test_mensagem_geral_setter(instance):
    original = instance.geral
    instance.geral = original
    assert instance.geral == original



@given(instance=Mensagem_strategy)
def test_mensagem_assunto_setter(instance):
    original = instance.assunto
    instance.assunto = original
    assert instance.assunto == original

@given(instance=ProfissionalSaude_strategy)
@settings(max_examples=50)
def test_profissionalsaude_instantiation(instance):
    assert isinstance(instance, ProfissionalSaude)

@given(instance=Naturalidade_strategy)
@settings(max_examples=50)
def test_naturalidade_instantiation(instance):
    assert isinstance(instance, Naturalidade)



@given(instance=Naturalidade_strategy)
def test_naturalidade_naturalidade_setter(instance):
    original = instance.naturalidade
    instance.naturalidade = original
    assert instance.naturalidade == original

@given(instance=Medicamento_strategy)
@settings(max_examples=50)
def test_medicamento_instantiation(instance):
    assert isinstance(instance, Medicamento)



@given(instance=Medicamento_strategy)
def test_medicamento_ativo_setter(instance):
    original = instance.ativo
    instance.ativo = original
    assert instance.ativo == original



@given(instance=Medicamento_strategy)
def test_medicamento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Medicamento_strategy)
def test_medicamento_intervaloTempo_setter(instance):
    original = instance.intervaloTempo
    instance.intervaloTempo = original
    assert instance.intervaloTempo == original



@given(instance=Medicamento_strategy)
def test_medicamento_horaInicial_setter(instance):
    original = instance.horaInicial
    instance.horaInicial = original
    assert instance.horaInicial == original



@given(instance=Medicamento_strategy)
def test_medicamento_dataFim_setter(instance):
    original = instance.dataFim
    instance.dataFim = original
    assert instance.dataFim == original



@given(instance=Medicamento_strategy)
def test_medicamento_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original



@given(instance=Medicamento_strategy)
def test_medicamento_dataInicio_setter(instance):
    original = instance.dataInicio
    instance.dataInicio = original
    assert instance.dataInicio == original

@given(instance=Paciente_strategy)
@settings(max_examples=50)
def test_paciente_instantiation(instance):
    assert isinstance(instance, Paciente)

@given(instance=Telefone_strategy)
@settings(max_examples=50)
def test_telefone_instantiation(instance):
    assert isinstance(instance, Telefone)



@given(instance=Telefone_strategy)
def test_telefone_ddd_setter(instance):
    original = instance.ddd
    instance.ddd = original
    assert instance.ddd == original



@given(instance=Telefone_strategy)
def test_telefone_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Telefone_strategy)
def test_telefone_tipo_setter(instance):
    original = instance.tipo
    instance.tipo = original
    assert instance.tipo == original

@given(instance=Pessoa_strategy)
@settings(max_examples=50)
def test_pessoa_instantiation(instance):
    assert isinstance(instance, Pessoa)



@given(instance=Pessoa_strategy)
def test_pessoa_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Pessoa_strategy)
def test_pessoa_sexo_setter(instance):
    original = instance.sexo
    instance.sexo = original
    assert instance.sexo == original



@given(instance=Pessoa_strategy)
def test_pessoa_dataInclusao_setter(instance):
    original = instance.dataInclusao
    instance.dataInclusao = original
    assert instance.dataInclusao == original



@given(instance=Pessoa_strategy)
def test_pessoa_cpf_setter(instance):
    original = instance.cpf
    instance.cpf = original
    assert instance.cpf == original



@given(instance=Pessoa_strategy)
def test_pessoa_ultimoAcesso_setter(instance):
    original = instance.ultimoAcesso
    instance.ultimoAcesso = original
    assert instance.ultimoAcesso == original



@given(instance=Pessoa_strategy)
def test_pessoa_senha_setter(instance):
    original = instance.senha
    instance.senha = original
    assert instance.senha == original



@given(instance=Pessoa_strategy)
def test_pessoa_dataNascimento_setter(instance):
    original = instance.dataNascimento
    instance.dataNascimento = original
    assert instance.dataNascimento == original

@given(instance=Endereco_strategy)
@settings(max_examples=50)
def test_endereco_instantiation(instance):
    assert isinstance(instance, Endereco)



@given(instance=Endereco_strategy)
def test_endereco_logradouro_setter(instance):
    original = instance.logradouro
    instance.logradouro = original
    assert instance.logradouro == original



@given(instance=Endereco_strategy)
def test_endereco_cep_setter(instance):
    original = instance.cep
    instance.cep = original
    assert instance.cep == original



@given(instance=Endereco_strategy)
def test_endereco_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=Endereco_strategy)
def test_endereco_bairro_setter(instance):
    original = instance.bairro
    instance.bairro = original
    assert instance.bairro == original



@given(instance=Endereco_strategy)
def test_endereco_cidade_setter(instance):
    original = instance.cidade
    instance.cidade = original
    assert instance.cidade == original

@given(instance=Exame_strategy)
@settings(max_examples=50)
def test_exame_instantiation(instance):
    assert isinstance(instance, Exame)



@given(instance=Exame_strategy)
def test_exame_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=Exame_strategy)
def test_exame_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original



@given(instance=Exame_strategy)
def test_exame_descricao_setter(instance):
    original = instance.descricao
    instance.descricao = original
    assert instance.descricao == original

@given(instance=LocalExame_strategy)
@settings(max_examples=50)
def test_localexame_instantiation(instance):
    assert isinstance(instance, LocalExame)



@given(instance=LocalExame_strategy)
def test_localexame_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=TipoMedicamento_strategy)
@settings(max_examples=50)
def test_tipomedicamento_instantiation(instance):
    assert isinstance(instance, TipoMedicamento)



@given(instance=TipoMedicamento_strategy)
def test_tipomedicamento_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=TipoSanguineo_strategy)
@settings(max_examples=50)
def test_tiposanguineo_instantiation(instance):
    assert isinstance(instance, TipoSanguineo)



@given(instance=TipoSanguineo_strategy)
def test_tiposanguineo_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=Interacao_strategy)
@settings(max_examples=50)
def test_interacao_instantiation(instance):
    assert isinstance(instance, Interacao)
