import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Condition,
    farrusco::Distancia,
    Action,
    farrusco::Condition,
    Actuate,
    farrusco::Servo,
    farrusco::LED,
    farrusco::Motor,
    farrusco::Actuate,
    farrusco::Espera,
    farrusco::Bumpers,
    Behavior,
    farrusco::Paralelo,
    farrusco::Sequencial,
    farrusco::AlterarEstado,
    farrusco::Prioridade,
    Node,
    farrusco::Action,
    farrusco::Behavior,
    farrusco::Irmao,
    farrusco::Filho,
    farrusco::Node,
    farrusco::Robot,
    EstadoFalha,
    EstadoDecorrer,
    EstadoSucesso,
    EscolhaBumper,
    TipoDistancia,
    EstadoDaLuz,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::distancia_is_not_abstract():
    assert not inspect.isabstract(farrusco::Distancia)


def test_farrusco::distancia_constructor_exists():
    assert callable(farrusco::Distancia.__init__)


def test_farrusco::distancia_constructor_args():
    sig = inspect.signature(farrusco::Distancia.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Menor_Maior" in params, "Missing parameter 'Menor_Maior'"
    assert "distancia" in params, "Missing parameter 'distancia'"

def test_farrusco::distancia_has_Nome():
    assert hasattr(farrusco::Distancia, "Nome")
    descriptor = None
    for klass in farrusco::Distancia.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::distancia_has_Menor_Maior():
    assert hasattr(farrusco::Distancia, "Menor_Maior")
    descriptor = None
    for klass in farrusco::Distancia.__mro__:
        if "Menor_Maior" in klass.__dict__:
            descriptor = klass.__dict__["Menor_Maior"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::distancia_has_distancia():
    assert hasattr(farrusco::Distancia, "distancia")
    descriptor = None
    for klass in farrusco::Distancia.__mro__:
        if "distancia" in klass.__dict__:
            descriptor = klass.__dict__["distancia"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::condition_is_not_abstract():
    assert not inspect.isabstract(farrusco::Condition)


def test_farrusco::condition_constructor_exists():
    assert callable(farrusco::Condition.__init__)


def test_farrusco::condition_constructor_args():
    sig = inspect.signature(farrusco::Condition.__init__)
    params = list(sig.parameters.keys())



def test_actuate_is_not_abstract():
    assert not inspect.isabstract(Actuate)


def test_actuate_constructor_exists():
    assert callable(Actuate.__init__)


def test_actuate_constructor_args():
    sig = inspect.signature(Actuate.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::servo_is_not_abstract():
    assert not inspect.isabstract(farrusco::Servo)


def test_farrusco::servo_constructor_exists():
    assert callable(farrusco::Servo.__init__)


def test_farrusco::servo_constructor_args():
    sig = inspect.signature(farrusco::Servo.__init__)
    params = list(sig.parameters.keys())
    assert "Passo_a_Passo" in params, "Missing parameter 'Passo_a_Passo'"
    assert "Posicao_Maxima" in params, "Missing parameter 'Posicao_Maxima'"
    assert "Posicao_Minima" in params, "Missing parameter 'Posicao_Minima'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::servo_has_Passo_a_Passo():
    assert hasattr(farrusco::Servo, "Passo_a_Passo")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "Passo_a_Passo" in klass.__dict__:
            descriptor = klass.__dict__["Passo_a_Passo"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::servo_has_Posicao_Maxima():
    assert hasattr(farrusco::Servo, "Posicao_Maxima")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "Posicao_Maxima" in klass.__dict__:
            descriptor = klass.__dict__["Posicao_Maxima"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::servo_has_Posicao_Minima():
    assert hasattr(farrusco::Servo, "Posicao_Minima")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "Posicao_Minima" in klass.__dict__:
            descriptor = klass.__dict__["Posicao_Minima"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::servo_has_Nome():
    assert hasattr(farrusco::Servo, "Nome")
    descriptor = None
    for klass in farrusco::Servo.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::led_is_not_abstract():
    assert not inspect.isabstract(farrusco::LED)


def test_farrusco::led_constructor_exists():
    assert callable(farrusco::LED.__init__)


def test_farrusco::led_constructor_args():
    sig = inspect.signature(farrusco::LED.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Ligado_ou_Desligado" in params, "Missing parameter 'Ligado_ou_Desligado'"

def test_farrusco::led_has_Nome():
    assert hasattr(farrusco::LED, "Nome")
    descriptor = None
    for klass in farrusco::LED.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::led_has_Ligado_ou_Desligado():
    assert hasattr(farrusco::LED, "Ligado_ou_Desligado")
    descriptor = None
    for klass in farrusco::LED.__mro__:
        if "Ligado_ou_Desligado" in klass.__dict__:
            descriptor = klass.__dict__["Ligado_ou_Desligado"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::motor_is_not_abstract():
    assert not inspect.isabstract(farrusco::Motor)


def test_farrusco::motor_constructor_exists():
    assert callable(farrusco::Motor.__init__)


def test_farrusco::motor_constructor_args():
    sig = inspect.signature(farrusco::Motor.__init__)
    params = list(sig.parameters.keys())
    assert "Motor_Esquerdo" in params, "Missing parameter 'Motor_Esquerdo'"
    assert "Motor_Direito" in params, "Missing parameter 'Motor_Direito'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::motor_has_Motor_Esquerdo():
    assert hasattr(farrusco::Motor, "Motor_Esquerdo")
    descriptor = None
    for klass in farrusco::Motor.__mro__:
        if "Motor_Esquerdo" in klass.__dict__:
            descriptor = klass.__dict__["Motor_Esquerdo"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::motor_has_Motor_Direito():
    assert hasattr(farrusco::Motor, "Motor_Direito")
    descriptor = None
    for klass in farrusco::Motor.__mro__:
        if "Motor_Direito" in klass.__dict__:
            descriptor = klass.__dict__["Motor_Direito"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::motor_has_Nome():
    assert hasattr(farrusco::Motor, "Nome")
    descriptor = None
    for klass in farrusco::Motor.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::actuate_is_not_abstract():
    assert not inspect.isabstract(farrusco::Actuate)


def test_farrusco::actuate_constructor_exists():
    assert callable(farrusco::Actuate.__init__)


def test_farrusco::actuate_constructor_args():
    sig = inspect.signature(farrusco::Actuate.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::espera_is_not_abstract():
    assert not inspect.isabstract(farrusco::Espera)


def test_farrusco::espera_constructor_exists():
    assert callable(farrusco::Espera.__init__)


def test_farrusco::espera_constructor_args():
    sig = inspect.signature(farrusco::Espera.__init__)
    params = list(sig.parameters.keys())
    assert "Tempo" in params, "Missing parameter 'Tempo'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::espera_has_Tempo():
    assert hasattr(farrusco::Espera, "Tempo")
    descriptor = None
    for klass in farrusco::Espera.__mro__:
        if "Tempo" in klass.__dict__:
            descriptor = klass.__dict__["Tempo"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::espera_has_Nome():
    assert hasattr(farrusco::Espera, "Nome")
    descriptor = None
    for klass in farrusco::Espera.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::bumpers_is_not_abstract():
    assert not inspect.isabstract(farrusco::Bumpers)


def test_farrusco::bumpers_constructor_exists():
    assert callable(farrusco::Bumpers.__init__)


def test_farrusco::bumpers_constructor_args():
    sig = inspect.signature(farrusco::Bumpers.__init__)
    params = list(sig.parameters.keys())
    assert "Bumper_Esquerdo_ou_Direito" in params, "Missing parameter 'Bumper_Esquerdo_ou_Direito'"
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::bumpers_has_Bumper_Esquerdo_ou_Direito():
    assert hasattr(farrusco::Bumpers, "Bumper_Esquerdo_ou_Direito")
    descriptor = None
    for klass in farrusco::Bumpers.__mro__:
        if "Bumper_Esquerdo_ou_Direito" in klass.__dict__:
            descriptor = klass.__dict__["Bumper_Esquerdo_ou_Direito"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::bumpers_has_Nome():
    assert hasattr(farrusco::Bumpers, "Nome")
    descriptor = None
    for klass in farrusco::Bumpers.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::paralelo_is_not_abstract():
    assert not inspect.isabstract(farrusco::Paralelo)


def test_farrusco::paralelo_constructor_exists():
    assert callable(farrusco::Paralelo.__init__)


def test_farrusco::paralelo_constructor_args():
    sig = inspect.signature(farrusco::Paralelo.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::paralelo_has_Nome():
    assert hasattr(farrusco::Paralelo, "Nome")
    descriptor = None
    for klass in farrusco::Paralelo.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::sequencial_is_not_abstract():
    assert not inspect.isabstract(farrusco::Sequencial)


def test_farrusco::sequencial_constructor_exists():
    assert callable(farrusco::Sequencial.__init__)


def test_farrusco::sequencial_constructor_args():
    sig = inspect.signature(farrusco::Sequencial.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::sequencial_has_Nome():
    assert hasattr(farrusco::Sequencial, "Nome")
    descriptor = None
    for klass in farrusco::Sequencial.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::alterarestado_is_not_abstract():
    assert not inspect.isabstract(farrusco::AlterarEstado)


def test_farrusco::alterarestado_constructor_exists():
    assert callable(farrusco::AlterarEstado.__init__)


def test_farrusco::alterarestado_constructor_args():
    sig = inspect.signature(farrusco::AlterarEstado.__init__)
    params = list(sig.parameters.keys())
    assert "Alterar_Falha" in params, "Missing parameter 'Alterar_Falha'"
    assert "Alterar_Decorrer" in params, "Missing parameter 'Alterar_Decorrer'"
    assert "Nome" in params, "Missing parameter 'Nome'"
    assert "Alterar_Sucesso" in params, "Missing parameter 'Alterar_Sucesso'"

def test_farrusco::alterarestado_has_Alterar_Falha():
    assert hasattr(farrusco::AlterarEstado, "Alterar_Falha")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "Alterar_Falha" in klass.__dict__:
            descriptor = klass.__dict__["Alterar_Falha"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::alterarestado_has_Alterar_Decorrer():
    assert hasattr(farrusco::AlterarEstado, "Alterar_Decorrer")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "Alterar_Decorrer" in klass.__dict__:
            descriptor = klass.__dict__["Alterar_Decorrer"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::alterarestado_has_Nome():
    assert hasattr(farrusco::AlterarEstado, "Nome")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_farrusco::alterarestado_has_Alterar_Sucesso():
    assert hasattr(farrusco::AlterarEstado, "Alterar_Sucesso")
    descriptor = None
    for klass in farrusco::AlterarEstado.__mro__:
        if "Alterar_Sucesso" in klass.__dict__:
            descriptor = klass.__dict__["Alterar_Sucesso"]
            break
    assert isinstance(descriptor, property)



def test_farrusco::prioridade_is_not_abstract():
    assert not inspect.isabstract(farrusco::Prioridade)


def test_farrusco::prioridade_constructor_exists():
    assert callable(farrusco::Prioridade.__init__)


def test_farrusco::prioridade_constructor_args():
    sig = inspect.signature(farrusco::Prioridade.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::prioridade_has_Nome():
    assert hasattr(farrusco::Prioridade, "Nome")
    descriptor = None
    for klass in farrusco::Prioridade.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::action_is_not_abstract():
    assert not inspect.isabstract(farrusco::Action)


def test_farrusco::action_constructor_exists():
    assert callable(farrusco::Action.__init__)


def test_farrusco::action_constructor_args():
    sig = inspect.signature(farrusco::Action.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::behavior_is_not_abstract():
    assert not inspect.isabstract(farrusco::Behavior)


def test_farrusco::behavior_constructor_exists():
    assert callable(farrusco::Behavior.__init__)


def test_farrusco::behavior_constructor_args():
    sig = inspect.signature(farrusco::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::irmao_is_not_abstract():
    assert not inspect.isabstract(farrusco::Irmao)


def test_farrusco::irmao_constructor_exists():
    assert callable(farrusco::Irmao.__init__)


def test_farrusco::irmao_constructor_args():
    sig = inspect.signature(farrusco::Irmao.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::filho_is_not_abstract():
    assert not inspect.isabstract(farrusco::Filho)


def test_farrusco::filho_constructor_exists():
    assert callable(farrusco::Filho.__init__)


def test_farrusco::filho_constructor_args():
    sig = inspect.signature(farrusco::Filho.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::node_is_not_abstract():
    assert not inspect.isabstract(farrusco::Node)


def test_farrusco::node_constructor_exists():
    assert callable(farrusco::Node.__init__)


def test_farrusco::node_constructor_args():
    sig = inspect.signature(farrusco::Node.__init__)
    params = list(sig.parameters.keys())



def test_farrusco::robot_is_not_abstract():
    assert not inspect.isabstract(farrusco::Robot)


def test_farrusco::robot_constructor_exists():
    assert callable(farrusco::Robot.__init__)


def test_farrusco::robot_constructor_args():
    sig = inspect.signature(farrusco::Robot.__init__)
    params = list(sig.parameters.keys())
    assert "Nome" in params, "Missing parameter 'Nome'"

def test_farrusco::robot_has_Nome():
    assert hasattr(farrusco::Robot, "Nome")
    descriptor = None
    for klass in farrusco::Robot.__mro__:
        if "Nome" in klass.__dict__:
            descriptor = klass.__dict__["Nome"]
            break
    assert isinstance(descriptor, property)

def test_estadofalha_exists():
    # Check that the Enumeration exists
    assert EstadoFalha is not None

def test_estadofalha_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoFalha]
    expected_literals = [
        "Decorrer",
        "Sucesso",
        "Falha",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoFalha"

def test_estadodecorrer_exists():
    # Check that the Enumeration exists
    assert EstadoDecorrer is not None

def test_estadodecorrer_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoDecorrer]
    expected_literals = [
        "Sucesso",
        "Decorrer",
        "Falha",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoDecorrer"

def test_estadosucesso_exists():
    # Check that the Enumeration exists
    assert EstadoSucesso is not None

def test_estadosucesso_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoSucesso]
    expected_literals = [
        "Falha",
        "Decorrer",
        "Sucesso",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoSucesso"

def test_escolhabumper_exists():
    # Check that the Enumeration exists
    assert EscolhaBumper is not None

def test_escolhabumper_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EscolhaBumper]
    expected_literals = [
        "Direito",
        "Esquerdo",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EscolhaBumper"

def test_tipodistancia_exists():
    # Check that the Enumeration exists
    assert TipoDistancia is not None

def test_tipodistancia_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TipoDistancia]
    expected_literals = [
        "Menor",
        "Maior",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TipoDistancia"

def test_estadodaluz_exists():
    # Check that the Enumeration exists
    assert EstadoDaLuz is not None

def test_estadodaluz_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EstadoDaLuz]
    expected_literals = [
        "Desligado",
        "Ligado",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EstadoDaLuz"


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
Condition_strategy = st.builds(
    Condition,
)
farrusco::Distancia_strategy = st.builds(
    farrusco::Distancia,
    Nome=
        safe_text,
    Menor_Maior=
        safe_text,
    distancia=
        st.integers()
)
Action_strategy = st.builds(
    Action,
)
farrusco::Condition_strategy = st.builds(
    farrusco::Condition,
)
Actuate_strategy = st.builds(
    Actuate,
)
farrusco::Servo_strategy = st.builds(
    farrusco::Servo,
    Passo_a_Passo=
        st.integers(),
    Posicao_Maxima=
        st.integers(),
    Posicao_Minima=
        st.integers(),
    Nome=
        safe_text
)
farrusco::LED_strategy = st.builds(
    farrusco::LED,
    Nome=
        safe_text,
    Ligado_ou_Desligado=
        safe_text
)
farrusco::Motor_strategy = st.builds(
    farrusco::Motor,
    Motor_Esquerdo=
        st.integers(),
    Motor_Direito=
        st.integers(),
    Nome=
        safe_text
)
farrusco::Actuate_strategy = st.builds(
    farrusco::Actuate,
)
farrusco::Espera_strategy = st.builds(
    farrusco::Espera,
    Tempo=
        st.integers(),
    Nome=
        safe_text
)
farrusco::Bumpers_strategy = st.builds(
    farrusco::Bumpers,
    Bumper_Esquerdo_ou_Direito=
        safe_text,
    Nome=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
farrusco::Paralelo_strategy = st.builds(
    farrusco::Paralelo,
    Nome=
        safe_text
)
farrusco::Sequencial_strategy = st.builds(
    farrusco::Sequencial,
    Nome=
        safe_text
)
farrusco::AlterarEstado_strategy = st.builds(
    farrusco::AlterarEstado,
    Alterar_Falha=
        safe_text,
    Alterar_Decorrer=
        safe_text,
    Nome=
        safe_text,
    Alterar_Sucesso=
        safe_text
)
farrusco::Prioridade_strategy = st.builds(
    farrusco::Prioridade,
    Nome=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
farrusco::Action_strategy = st.builds(
    farrusco::Action,
)
farrusco::Behavior_strategy = st.builds(
    farrusco::Behavior,
)
farrusco::Irmao_strategy = st.builds(
    farrusco::Irmao,
)
farrusco::Filho_strategy = st.builds(
    farrusco::Filho,
)
farrusco::Node_strategy = st.builds(
    farrusco::Node,
)
farrusco::Robot_strategy = st.builds(
    farrusco::Robot,
    Nome=
        safe_text
)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=farrusco::Distancia_strategy)
@settings(max_examples=50)
def test_farrusco::distancia_instantiation(instance):
    assert isinstance(instance, farrusco::Distancia)

@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_Menor_Maior_type(instance):
    assert isinstance(instance.Menor_Maior, str)


@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_Menor_Maior_setter(instance):
    original = instance.Menor_Maior
    instance.Menor_Maior = original
    assert instance.Menor_Maior == original

@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_distancia_type(instance):
    assert isinstance(instance.distancia, int)


@given(instance=farrusco::Distancia_strategy)
def test_farrusco::distancia_distancia_setter(instance):
    original = instance.distancia
    instance.distancia = original
    assert instance.distancia == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=farrusco::Condition_strategy)
@settings(max_examples=50)
def test_farrusco::condition_instantiation(instance):
    assert isinstance(instance, farrusco::Condition)

@given(instance=Actuate_strategy)
@settings(max_examples=50)
def test_actuate_instantiation(instance):
    assert isinstance(instance, Actuate)

@given(instance=farrusco::Servo_strategy)
@settings(max_examples=50)
def test_farrusco::servo_instantiation(instance):
    assert isinstance(instance, farrusco::Servo)

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Passo_a_Passo_type(instance):
    assert isinstance(instance.Passo_a_Passo, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Passo_a_Passo_setter(instance):
    original = instance.Passo_a_Passo
    instance.Passo_a_Passo = original
    assert instance.Passo_a_Passo == original

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Posicao_Maxima_type(instance):
    assert isinstance(instance.Posicao_Maxima, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Posicao_Maxima_setter(instance):
    original = instance.Posicao_Maxima
    instance.Posicao_Maxima = original
    assert instance.Posicao_Maxima == original

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Posicao_Minima_type(instance):
    assert isinstance(instance.Posicao_Minima, int)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Posicao_Minima_setter(instance):
    original = instance.Posicao_Minima
    instance.Posicao_Minima = original
    assert instance.Posicao_Minima == original

@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Servo_strategy)
def test_farrusco::servo_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::LED_strategy)
@settings(max_examples=50)
def test_farrusco::led_instantiation(instance):
    assert isinstance(instance, farrusco::LED)

@given(instance=farrusco::LED_strategy)
def test_farrusco::led_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::LED_strategy)
def test_farrusco::led_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::LED_strategy)
def test_farrusco::led_Ligado_ou_Desligado_type(instance):
    assert isinstance(instance.Ligado_ou_Desligado, str)


@given(instance=farrusco::LED_strategy)
def test_farrusco::led_Ligado_ou_Desligado_setter(instance):
    original = instance.Ligado_ou_Desligado
    instance.Ligado_ou_Desligado = original
    assert instance.Ligado_ou_Desligado == original

@given(instance=farrusco::Motor_strategy)
@settings(max_examples=50)
def test_farrusco::motor_instantiation(instance):
    assert isinstance(instance, farrusco::Motor)

@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Motor_Esquerdo_type(instance):
    assert isinstance(instance.Motor_Esquerdo, int)


@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Motor_Esquerdo_setter(instance):
    original = instance.Motor_Esquerdo
    instance.Motor_Esquerdo = original
    assert instance.Motor_Esquerdo == original

@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Motor_Direito_type(instance):
    assert isinstance(instance.Motor_Direito, int)


@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Motor_Direito_setter(instance):
    original = instance.Motor_Direito
    instance.Motor_Direito = original
    assert instance.Motor_Direito == original

@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Motor_strategy)
def test_farrusco::motor_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::Actuate_strategy)
@settings(max_examples=50)
def test_farrusco::actuate_instantiation(instance):
    assert isinstance(instance, farrusco::Actuate)

@given(instance=farrusco::Espera_strategy)
@settings(max_examples=50)
def test_farrusco::espera_instantiation(instance):
    assert isinstance(instance, farrusco::Espera)

@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_Tempo_type(instance):
    assert isinstance(instance.Tempo, int)


@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_Tempo_setter(instance):
    original = instance.Tempo
    instance.Tempo = original
    assert instance.Tempo == original

@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Espera_strategy)
def test_farrusco::espera_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::Bumpers_strategy)
@settings(max_examples=50)
def test_farrusco::bumpers_instantiation(instance):
    assert isinstance(instance, farrusco::Bumpers)

@given(instance=farrusco::Bumpers_strategy)
def test_farrusco::bumpers_Bumper_Esquerdo_ou_Direito_type(instance):
    assert isinstance(instance.Bumper_Esquerdo_ou_Direito, str)


@given(instance=farrusco::Bumpers_strategy)
def test_farrusco::bumpers_Bumper_Esquerdo_ou_Direito_setter(instance):
    original = instance.Bumper_Esquerdo_ou_Direito
    instance.Bumper_Esquerdo_ou_Direito = original
    assert instance.Bumper_Esquerdo_ou_Direito == original

@given(instance=farrusco::Bumpers_strategy)
def test_farrusco::bumpers_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Bumpers_strategy)
def test_farrusco::bumpers_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=farrusco::Paralelo_strategy)
@settings(max_examples=50)
def test_farrusco::paralelo_instantiation(instance):
    assert isinstance(instance, farrusco::Paralelo)

@given(instance=farrusco::Paralelo_strategy)
def test_farrusco::paralelo_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Paralelo_strategy)
def test_farrusco::paralelo_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::Sequencial_strategy)
@settings(max_examples=50)
def test_farrusco::sequencial_instantiation(instance):
    assert isinstance(instance, farrusco::Sequencial)

@given(instance=farrusco::Sequencial_strategy)
def test_farrusco::sequencial_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Sequencial_strategy)
def test_farrusco::sequencial_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::AlterarEstado_strategy)
@settings(max_examples=50)
def test_farrusco::alterarestado_instantiation(instance):
    assert isinstance(instance, farrusco::AlterarEstado)

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Falha_type(instance):
    assert isinstance(instance.Alterar_Falha, str)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Falha_setter(instance):
    original = instance.Alterar_Falha
    instance.Alterar_Falha = original
    assert instance.Alterar_Falha == original

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Decorrer_type(instance):
    assert isinstance(instance.Alterar_Decorrer, str)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Decorrer_setter(instance):
    original = instance.Alterar_Decorrer
    instance.Alterar_Decorrer = original
    assert instance.Alterar_Decorrer == original

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Sucesso_type(instance):
    assert isinstance(instance.Alterar_Sucesso, str)


@given(instance=farrusco::AlterarEstado_strategy)
def test_farrusco::alterarestado_Alterar_Sucesso_setter(instance):
    original = instance.Alterar_Sucesso
    instance.Alterar_Sucesso = original
    assert instance.Alterar_Sucesso == original

@given(instance=farrusco::Prioridade_strategy)
@settings(max_examples=50)
def test_farrusco::prioridade_instantiation(instance):
    assert isinstance(instance, farrusco::Prioridade)

@given(instance=farrusco::Prioridade_strategy)
def test_farrusco::prioridade_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Prioridade_strategy)
def test_farrusco::prioridade_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=farrusco::Action_strategy)
@settings(max_examples=50)
def test_farrusco::action_instantiation(instance):
    assert isinstance(instance, farrusco::Action)

@given(instance=farrusco::Behavior_strategy)
@settings(max_examples=50)
def test_farrusco::behavior_instantiation(instance):
    assert isinstance(instance, farrusco::Behavior)

@given(instance=farrusco::Irmao_strategy)
@settings(max_examples=50)
def test_farrusco::irmao_instantiation(instance):
    assert isinstance(instance, farrusco::Irmao)

@given(instance=farrusco::Filho_strategy)
@settings(max_examples=50)
def test_farrusco::filho_instantiation(instance):
    assert isinstance(instance, farrusco::Filho)

@given(instance=farrusco::Node_strategy)
@settings(max_examples=50)
def test_farrusco::node_instantiation(instance):
    assert isinstance(instance, farrusco::Node)

@given(instance=farrusco::Robot_strategy)
@settings(max_examples=50)
def test_farrusco::robot_instantiation(instance):
    assert isinstance(instance, farrusco::Robot)

@given(instance=farrusco::Robot_strategy)
def test_farrusco::robot_Nome_type(instance):
    assert isinstance(instance.Nome, str)


@given(instance=farrusco::Robot_strategy)
def test_farrusco::robot_Nome_setter(instance):
    original = instance.Nome
    instance.Nome = original
    assert instance.Nome == original
