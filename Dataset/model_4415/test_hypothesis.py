import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Bloques,
    arduino_While,
    arduino_If,
    arduino_Actuadores,
    arduino_Sensores,
    Instrucciones,
    arduino_Encender,
    arduino_Esperar,
    arduino_Variar,
    arduino_Apagar,
    Sensores,
    arduino_Boton,
    arduino_PIR,
    arduino_Temperatura,
    arduino_Potenciometro,
    arduino_LDR,
    Actuadores,
    arduino_Servo,
    arduino_Buzzer,
    arduino_Led,
    arduino_Bloques,
    arduino_Instrucciones,
    arduino_Sketch,
    operandos,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bloques_is_not_abstract():
    assert not inspect.isabstract(Bloques)


def test_bloques_constructor_exists():
    assert callable(Bloques.__init__)


def test_bloques_constructor_args():
    sig = inspect.signature(Bloques.__init__)
    params = list(sig.parameters.keys())



def test_arduino_while_is_not_abstract():
    assert not inspect.isabstract(arduino_While)


def test_arduino_while_constructor_exists():
    assert callable(arduino_While.__init__)


def test_arduino_while_constructor_args():
    sig = inspect.signature(arduino_While.__init__)
    params = list(sig.parameters.keys())
    assert "referencia" in params, "Missing parameter 'referencia'"
    assert "valor" in params, "Missing parameter 'valor'"
    assert "operando" in params, "Missing parameter 'operando'"

def test_arduino_while_has_referencia():
    assert hasattr(arduino_While, "referencia")
    descriptor = None
    for klass in arduino_While.__mro__:
        if "referencia" in klass.__dict__:
            descriptor = klass.__dict__["referencia"]
            break
    assert isinstance(descriptor, property)

def test_arduino_while_has_valor():
    assert hasattr(arduino_While, "valor")
    descriptor = None
    for klass in arduino_While.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
            break
    assert isinstance(descriptor, property)

def test_arduino_while_has_operando():
    assert hasattr(arduino_While, "operando")
    descriptor = None
    for klass in arduino_While.__mro__:
        if "operando" in klass.__dict__:
            descriptor = klass.__dict__["operando"]
            break
    assert isinstance(descriptor, property)



def test_arduino_if_is_not_abstract():
    assert not inspect.isabstract(arduino_If)


def test_arduino_if_constructor_exists():
    assert callable(arduino_If.__init__)


def test_arduino_if_constructor_args():
    sig = inspect.signature(arduino_If.__init__)
    params = list(sig.parameters.keys())
    assert "valor" in params, "Missing parameter 'valor'"
    assert "referencia" in params, "Missing parameter 'referencia'"
    assert "operando" in params, "Missing parameter 'operando'"

def test_arduino_if_has_valor():
    assert hasattr(arduino_If, "valor")
    descriptor = None
    for klass in arduino_If.__mro__:
        if "valor" in klass.__dict__:
            descriptor = klass.__dict__["valor"]
            break
    assert isinstance(descriptor, property)

def test_arduino_if_has_referencia():
    assert hasattr(arduino_If, "referencia")
    descriptor = None
    for klass in arduino_If.__mro__:
        if "referencia" in klass.__dict__:
            descriptor = klass.__dict__["referencia"]
            break
    assert isinstance(descriptor, property)

def test_arduino_if_has_operando():
    assert hasattr(arduino_If, "operando")
    descriptor = None
    for klass in arduino_If.__mro__:
        if "operando" in klass.__dict__:
            descriptor = klass.__dict__["operando"]
            break
    assert isinstance(descriptor, property)



def test_arduino_actuadores_is_not_abstract():
    assert not inspect.isabstract(arduino_Actuadores)


def test_arduino_actuadores_constructor_exists():
    assert callable(arduino_Actuadores.__init__)


def test_arduino_actuadores_constructor_args():
    sig = inspect.signature(arduino_Actuadores.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"

def test_arduino_actuadores_has_pin():
    assert hasattr(arduino_Actuadores, "pin")
    descriptor = None
    for klass in arduino_Actuadores.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)



def test_arduino_sensores_is_not_abstract():
    assert not inspect.isabstract(arduino_Sensores)


def test_arduino_sensores_constructor_exists():
    assert callable(arduino_Sensores.__init__)


def test_arduino_sensores_constructor_args():
    sig = inspect.signature(arduino_Sensores.__init__)
    params = list(sig.parameters.keys())
    assert "pin" in params, "Missing parameter 'pin'"
    assert "med" in params, "Missing parameter 'med'"

def test_arduino_sensores_has_pin():
    assert hasattr(arduino_Sensores, "pin")
    descriptor = None
    for klass in arduino_Sensores.__mro__:
        if "pin" in klass.__dict__:
            descriptor = klass.__dict__["pin"]
            break
    assert isinstance(descriptor, property)

def test_arduino_sensores_has_med():
    assert hasattr(arduino_Sensores, "med")
    descriptor = None
    for klass in arduino_Sensores.__mro__:
        if "med" in klass.__dict__:
            descriptor = klass.__dict__["med"]
            break
    assert isinstance(descriptor, property)



def test_instrucciones_is_not_abstract():
    assert not inspect.isabstract(Instrucciones)


def test_instrucciones_constructor_exists():
    assert callable(Instrucciones.__init__)


def test_instrucciones_constructor_args():
    sig = inspect.signature(Instrucciones.__init__)
    params = list(sig.parameters.keys())



def test_arduino_encender_is_not_abstract():
    assert not inspect.isabstract(arduino_Encender)


def test_arduino_encender_constructor_exists():
    assert callable(arduino_Encender.__init__)


def test_arduino_encender_constructor_args():
    sig = inspect.signature(arduino_Encender.__init__)
    params = list(sig.parameters.keys())



def test_arduino_esperar_is_not_abstract():
    assert not inspect.isabstract(arduino_Esperar)


def test_arduino_esperar_constructor_exists():
    assert callable(arduino_Esperar.__init__)


def test_arduino_esperar_constructor_args():
    sig = inspect.signature(arduino_Esperar.__init__)
    params = list(sig.parameters.keys())
    assert "miliseg" in params, "Missing parameter 'miliseg'"

def test_arduino_esperar_has_miliseg():
    assert hasattr(arduino_Esperar, "miliseg")
    descriptor = None
    for klass in arduino_Esperar.__mro__:
        if "miliseg" in klass.__dict__:
            descriptor = klass.__dict__["miliseg"]
            break
    assert isinstance(descriptor, property)



def test_arduino_variar_is_not_abstract():
    assert not inspect.isabstract(arduino_Variar)


def test_arduino_variar_constructor_exists():
    assert callable(arduino_Variar.__init__)


def test_arduino_variar_constructor_args():
    sig = inspect.signature(arduino_Variar.__init__)
    params = list(sig.parameters.keys())
    assert "pwm" in params, "Missing parameter 'pwm'"

def test_arduino_variar_has_pwm():
    assert hasattr(arduino_Variar, "pwm")
    descriptor = None
    for klass in arduino_Variar.__mro__:
        if "pwm" in klass.__dict__:
            descriptor = klass.__dict__["pwm"]
            break
    assert isinstance(descriptor, property)



def test_arduino_apagar_is_not_abstract():
    assert not inspect.isabstract(arduino_Apagar)


def test_arduino_apagar_constructor_exists():
    assert callable(arduino_Apagar.__init__)


def test_arduino_apagar_constructor_args():
    sig = inspect.signature(arduino_Apagar.__init__)
    params = list(sig.parameters.keys())



def test_sensores_is_not_abstract():
    assert not inspect.isabstract(Sensores)


def test_sensores_constructor_exists():
    assert callable(Sensores.__init__)


def test_sensores_constructor_args():
    sig = inspect.signature(Sensores.__init__)
    params = list(sig.parameters.keys())



def test_arduino_boton_is_not_abstract():
    assert not inspect.isabstract(arduino_Boton)


def test_arduino_boton_constructor_exists():
    assert callable(arduino_Boton.__init__)


def test_arduino_boton_constructor_args():
    sig = inspect.signature(arduino_Boton.__init__)
    params = list(sig.parameters.keys())



def test_arduino_pir_is_not_abstract():
    assert not inspect.isabstract(arduino_PIR)


def test_arduino_pir_constructor_exists():
    assert callable(arduino_PIR.__init__)


def test_arduino_pir_constructor_args():
    sig = inspect.signature(arduino_PIR.__init__)
    params = list(sig.parameters.keys())



def test_arduino_temperatura_is_not_abstract():
    assert not inspect.isabstract(arduino_Temperatura)


def test_arduino_temperatura_constructor_exists():
    assert callable(arduino_Temperatura.__init__)


def test_arduino_temperatura_constructor_args():
    sig = inspect.signature(arduino_Temperatura.__init__)
    params = list(sig.parameters.keys())
    assert "temperatura" in params, "Missing parameter 'temperatura'"

def test_arduino_temperatura_has_temperatura():
    assert hasattr(arduino_Temperatura, "temperatura")
    descriptor = None
    for klass in arduino_Temperatura.__mro__:
        if "temperatura" in klass.__dict__:
            descriptor = klass.__dict__["temperatura"]
            break
    assert isinstance(descriptor, property)



def test_arduino_potenciometro_is_not_abstract():
    assert not inspect.isabstract(arduino_Potenciometro)


def test_arduino_potenciometro_constructor_exists():
    assert callable(arduino_Potenciometro.__init__)


def test_arduino_potenciometro_constructor_args():
    sig = inspect.signature(arduino_Potenciometro.__init__)
    params = list(sig.parameters.keys())



def test_arduino_ldr_is_not_abstract():
    assert not inspect.isabstract(arduino_LDR)


def test_arduino_ldr_constructor_exists():
    assert callable(arduino_LDR.__init__)


def test_arduino_ldr_constructor_args():
    sig = inspect.signature(arduino_LDR.__init__)
    params = list(sig.parameters.keys())



def test_actuadores_is_not_abstract():
    assert not inspect.isabstract(Actuadores)


def test_actuadores_constructor_exists():
    assert callable(Actuadores.__init__)


def test_actuadores_constructor_args():
    sig = inspect.signature(Actuadores.__init__)
    params = list(sig.parameters.keys())



def test_arduino_servo_is_not_abstract():
    assert not inspect.isabstract(arduino_Servo)


def test_arduino_servo_constructor_exists():
    assert callable(arduino_Servo.__init__)


def test_arduino_servo_constructor_args():
    sig = inspect.signature(arduino_Servo.__init__)
    params = list(sig.parameters.keys())
    assert "libreria" in params, "Missing parameter 'libreria'"
    assert "angulo" in params, "Missing parameter 'angulo'"

def test_arduino_servo_has_libreria():
    assert hasattr(arduino_Servo, "libreria")
    descriptor = None
    for klass in arduino_Servo.__mro__:
        if "libreria" in klass.__dict__:
            descriptor = klass.__dict__["libreria"]
            break
    assert isinstance(descriptor, property)

def test_arduino_servo_has_angulo():
    assert hasattr(arduino_Servo, "angulo")
    descriptor = None
    for klass in arduino_Servo.__mro__:
        if "angulo" in klass.__dict__:
            descriptor = klass.__dict__["angulo"]
            break
    assert isinstance(descriptor, property)



def test_arduino_buzzer_is_not_abstract():
    assert not inspect.isabstract(arduino_Buzzer)


def test_arduino_buzzer_constructor_exists():
    assert callable(arduino_Buzzer.__init__)


def test_arduino_buzzer_constructor_args():
    sig = inspect.signature(arduino_Buzzer.__init__)
    params = list(sig.parameters.keys())



def test_arduino_led_is_not_abstract():
    assert not inspect.isabstract(arduino_Led)


def test_arduino_led_constructor_exists():
    assert callable(arduino_Led.__init__)


def test_arduino_led_constructor_args():
    sig = inspect.signature(arduino_Led.__init__)
    params = list(sig.parameters.keys())



def test_arduino_bloques_is_not_abstract():
    assert not inspect.isabstract(arduino_Bloques)


def test_arduino_bloques_constructor_exists():
    assert callable(arduino_Bloques.__init__)


def test_arduino_bloques_constructor_args():
    sig = inspect.signature(arduino_Bloques.__init__)
    params = list(sig.parameters.keys())



def test_arduino_instrucciones_is_not_abstract():
    assert not inspect.isabstract(arduino_Instrucciones)


def test_arduino_instrucciones_constructor_exists():
    assert callable(arduino_Instrucciones.__init__)


def test_arduino_instrucciones_constructor_args():
    sig = inspect.signature(arduino_Instrucciones.__init__)
    params = list(sig.parameters.keys())



def test_arduino_sketch_is_not_abstract():
    assert not inspect.isabstract(arduino_Sketch)


def test_arduino_sketch_constructor_exists():
    assert callable(arduino_Sketch.__init__)


def test_arduino_sketch_constructor_args():
    sig = inspect.signature(arduino_Sketch.__init__)
    params = list(sig.parameters.keys())
    assert "Nombre" in params, "Missing parameter 'Nombre'"

def test_arduino_sketch_has_Nombre():
    assert hasattr(arduino_Sketch, "Nombre")
    descriptor = None
    for klass in arduino_Sketch.__mro__:
        if "Nombre" in klass.__dict__:
            descriptor = klass.__dict__["Nombre"]
            break
    assert isinstance(descriptor, property)

def test_operandos_exists():
    # Check that the Enumeration exists
    assert operandos is not None

def test_operandos_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in operandos]
    expected_literals = [
        "menorigual",
        "igual",
        "menor",
        "mayorigual",
        "mayor",
        "diferente",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in operandos"


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
Bloques_strategy = st.builds(
    Bloques,
)
arduino_While_strategy = st.builds(
    arduino_While,
    referencia=
        safe_text,
    valor=
        safe_text,
    operando=
        safe_text
)
arduino_If_strategy = st.builds(
    arduino_If,
    valor=
        safe_text,
    referencia=
        safe_text,
    operando=
        safe_text
)
arduino_Actuadores_strategy = st.builds(
    arduino_Actuadores,
    pin=
        safe_text
)
arduino_Sensores_strategy = st.builds(
    arduino_Sensores,
    pin=
        safe_text,
    med=
        safe_text
)
Instrucciones_strategy = st.builds(
    Instrucciones,
)
arduino_Encender_strategy = st.builds(
    arduino_Encender,
)
arduino_Esperar_strategy = st.builds(
    arduino_Esperar,
    miliseg=
        safe_text
)
arduino_Variar_strategy = st.builds(
    arduino_Variar,
    pwm=
        safe_text
)
arduino_Apagar_strategy = st.builds(
    arduino_Apagar,
)
Sensores_strategy = st.builds(
    Sensores,
)
arduino_Boton_strategy = st.builds(
    arduino_Boton,
)
arduino_PIR_strategy = st.builds(
    arduino_PIR,
)
arduino_Temperatura_strategy = st.builds(
    arduino_Temperatura,
    temperatura=
        safe_text
)
arduino_Potenciometro_strategy = st.builds(
    arduino_Potenciometro,
)
arduino_LDR_strategy = st.builds(
    arduino_LDR,
)
Actuadores_strategy = st.builds(
    Actuadores,
)
arduino_Servo_strategy = st.builds(
    arduino_Servo,
    libreria=
        safe_text,
    angulo=
        safe_text
)
arduino_Buzzer_strategy = st.builds(
    arduino_Buzzer,
)
arduino_Led_strategy = st.builds(
    arduino_Led,
)
arduino_Bloques_strategy = st.builds(
    arduino_Bloques,
)
arduino_Instrucciones_strategy = st.builds(
    arduino_Instrucciones,
)
arduino_Sketch_strategy = st.builds(
    arduino_Sketch,
    Nombre=
        safe_text
)

@given(instance=Bloques_strategy)
@settings(max_examples=50)
def test_bloques_instantiation(instance):
    assert isinstance(instance, Bloques)

@given(instance=arduino_While_strategy)
@settings(max_examples=50)
def test_arduino_while_instantiation(instance):
    assert isinstance(instance, arduino_While)



@given(instance=arduino_While_strategy)
def test_arduino_while_referencia_setter(instance):
    original = instance.referencia
    instance.referencia = original
    assert instance.referencia == original



@given(instance=arduino_While_strategy)
def test_arduino_while_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=arduino_While_strategy)
def test_arduino_while_operando_setter(instance):
    original = instance.operando
    instance.operando = original
    assert instance.operando == original

@given(instance=arduino_If_strategy)
@settings(max_examples=50)
def test_arduino_if_instantiation(instance):
    assert isinstance(instance, arduino_If)



@given(instance=arduino_If_strategy)
def test_arduino_if_valor_setter(instance):
    original = instance.valor
    instance.valor = original
    assert instance.valor == original



@given(instance=arduino_If_strategy)
def test_arduino_if_referencia_setter(instance):
    original = instance.referencia
    instance.referencia = original
    assert instance.referencia == original



@given(instance=arduino_If_strategy)
def test_arduino_if_operando_setter(instance):
    original = instance.operando
    instance.operando = original
    assert instance.operando == original

@given(instance=arduino_Actuadores_strategy)
@settings(max_examples=50)
def test_arduino_actuadores_instantiation(instance):
    assert isinstance(instance, arduino_Actuadores)



@given(instance=arduino_Actuadores_strategy)
def test_arduino_actuadores_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original

@given(instance=arduino_Sensores_strategy)
@settings(max_examples=50)
def test_arduino_sensores_instantiation(instance):
    assert isinstance(instance, arduino_Sensores)



@given(instance=arduino_Sensores_strategy)
def test_arduino_sensores_pin_setter(instance):
    original = instance.pin
    instance.pin = original
    assert instance.pin == original



@given(instance=arduino_Sensores_strategy)
def test_arduino_sensores_med_setter(instance):
    original = instance.med
    instance.med = original
    assert instance.med == original

@given(instance=Instrucciones_strategy)
@settings(max_examples=50)
def test_instrucciones_instantiation(instance):
    assert isinstance(instance, Instrucciones)

@given(instance=arduino_Encender_strategy)
@settings(max_examples=50)
def test_arduino_encender_instantiation(instance):
    assert isinstance(instance, arduino_Encender)

@given(instance=arduino_Esperar_strategy)
@settings(max_examples=50)
def test_arduino_esperar_instantiation(instance):
    assert isinstance(instance, arduino_Esperar)



@given(instance=arduino_Esperar_strategy)
def test_arduino_esperar_miliseg_setter(instance):
    original = instance.miliseg
    instance.miliseg = original
    assert instance.miliseg == original

@given(instance=arduino_Variar_strategy)
@settings(max_examples=50)
def test_arduino_variar_instantiation(instance):
    assert isinstance(instance, arduino_Variar)



@given(instance=arduino_Variar_strategy)
def test_arduino_variar_pwm_setter(instance):
    original = instance.pwm
    instance.pwm = original
    assert instance.pwm == original

@given(instance=arduino_Apagar_strategy)
@settings(max_examples=50)
def test_arduino_apagar_instantiation(instance):
    assert isinstance(instance, arduino_Apagar)

@given(instance=Sensores_strategy)
@settings(max_examples=50)
def test_sensores_instantiation(instance):
    assert isinstance(instance, Sensores)

@given(instance=arduino_Boton_strategy)
@settings(max_examples=50)
def test_arduino_boton_instantiation(instance):
    assert isinstance(instance, arduino_Boton)

@given(instance=arduino_PIR_strategy)
@settings(max_examples=50)
def test_arduino_pir_instantiation(instance):
    assert isinstance(instance, arduino_PIR)

@given(instance=arduino_Temperatura_strategy)
@settings(max_examples=50)
def test_arduino_temperatura_instantiation(instance):
    assert isinstance(instance, arduino_Temperatura)



@given(instance=arduino_Temperatura_strategy)
def test_arduino_temperatura_temperatura_setter(instance):
    original = instance.temperatura
    instance.temperatura = original
    assert instance.temperatura == original

@given(instance=arduino_Potenciometro_strategy)
@settings(max_examples=50)
def test_arduino_potenciometro_instantiation(instance):
    assert isinstance(instance, arduino_Potenciometro)

@given(instance=arduino_LDR_strategy)
@settings(max_examples=50)
def test_arduino_ldr_instantiation(instance):
    assert isinstance(instance, arduino_LDR)

@given(instance=Actuadores_strategy)
@settings(max_examples=50)
def test_actuadores_instantiation(instance):
    assert isinstance(instance, Actuadores)

@given(instance=arduino_Servo_strategy)
@settings(max_examples=50)
def test_arduino_servo_instantiation(instance):
    assert isinstance(instance, arduino_Servo)



@given(instance=arduino_Servo_strategy)
def test_arduino_servo_libreria_setter(instance):
    original = instance.libreria
    instance.libreria = original
    assert instance.libreria == original



@given(instance=arduino_Servo_strategy)
def test_arduino_servo_angulo_setter(instance):
    original = instance.angulo
    instance.angulo = original
    assert instance.angulo == original

@given(instance=arduino_Buzzer_strategy)
@settings(max_examples=50)
def test_arduino_buzzer_instantiation(instance):
    assert isinstance(instance, arduino_Buzzer)

@given(instance=arduino_Led_strategy)
@settings(max_examples=50)
def test_arduino_led_instantiation(instance):
    assert isinstance(instance, arduino_Led)

@given(instance=arduino_Bloques_strategy)
@settings(max_examples=50)
def test_arduino_bloques_instantiation(instance):
    assert isinstance(instance, arduino_Bloques)

@given(instance=arduino_Instrucciones_strategy)
@settings(max_examples=50)
def test_arduino_instrucciones_instantiation(instance):
    assert isinstance(instance, arduino_Instrucciones)

@given(instance=arduino_Sketch_strategy)
@settings(max_examples=50)
def test_arduino_sketch_instantiation(instance):
    assert isinstance(instance, arduino_Sketch)



@given(instance=arduino_Sketch_strategy)
def test_arduino_sketch_Nombre_setter(instance):
    original = instance.Nombre
    instance.Nombre = original
    assert instance.Nombre == original
