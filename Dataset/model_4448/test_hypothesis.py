import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Function,
    pycom_ModuleFunction,
    pycom_FunctionName,
    ModuleType,
    pycom_SensorType,
    pycom_ActuatorType,
    pycom_PinName,
    pycom_Pin,
    pycom_Expression,
    pycom_ComparisonExp,
    pycom_Boolean,
    pycom_LogicExp,
    pycom_BoardMember,
    pycom_Host,
    pycom_Connection,
    pycom_Server,
    pycom_ModuleType,
    BoardMember,
    pycom_Communication,
    pycom_Actuator,
    pycom_Sensor,
    pycom_Board,
    pycom_ExpMember,
    pycom_System,
    pycom_Condition,
    ExpMember,
    pycom_ConditionalAction,
    pycom_Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_pycom_modulefunction_is_not_abstract():
    assert not inspect.isabstract(pycom_ModuleFunction)


def test_pycom_modulefunction_constructor_exists():
    assert callable(pycom_ModuleFunction.__init__)


def test_pycom_modulefunction_constructor_args():
    sig = inspect.signature(pycom_ModuleFunction.__init__)
    params = list(sig.parameters.keys())



def test_pycom_functionname_is_not_abstract():
    assert not inspect.isabstract(pycom_FunctionName)


def test_pycom_functionname_constructor_exists():
    assert callable(pycom_FunctionName.__init__)


def test_pycom_functionname_constructor_args():
    sig = inspect.signature(pycom_FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pycom_functionname_has_name():
    assert hasattr(pycom_FunctionName, "name")
    descriptor = None
    for klass in pycom_FunctionName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moduletype_is_not_abstract():
    assert not inspect.isabstract(ModuleType)


def test_moduletype_constructor_exists():
    assert callable(ModuleType.__init__)


def test_moduletype_constructor_args():
    sig = inspect.signature(ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_pycom_sensortype_is_not_abstract():
    assert not inspect.isabstract(pycom_SensorType)


def test_pycom_sensortype_constructor_exists():
    assert callable(pycom_SensorType.__init__)


def test_pycom_sensortype_constructor_args():
    sig = inspect.signature(pycom_SensorType.__init__)
    params = list(sig.parameters.keys())



def test_pycom_actuatortype_is_not_abstract():
    assert not inspect.isabstract(pycom_ActuatorType)


def test_pycom_actuatortype_constructor_exists():
    assert callable(pycom_ActuatorType.__init__)


def test_pycom_actuatortype_constructor_args():
    sig = inspect.signature(pycom_ActuatorType.__init__)
    params = list(sig.parameters.keys())



def test_pycom_pinname_is_not_abstract():
    assert not inspect.isabstract(pycom_PinName)


def test_pycom_pinname_constructor_exists():
    assert callable(pycom_PinName.__init__)


def test_pycom_pinname_constructor_args():
    sig = inspect.signature(pycom_PinName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pycom_pinname_has_name():
    assert hasattr(pycom_PinName, "name")
    descriptor = None
    for klass in pycom_PinName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pycom_pin_is_not_abstract():
    assert not inspect.isabstract(pycom_Pin)


def test_pycom_pin_constructor_exists():
    assert callable(pycom_Pin.__init__)


def test_pycom_pin_constructor_args():
    sig = inspect.signature(pycom_Pin.__init__)
    params = list(sig.parameters.keys())



def test_pycom_expression_is_not_abstract():
    assert not inspect.isabstract(pycom_Expression)


def test_pycom_expression_constructor_exists():
    assert callable(pycom_Expression.__init__)


def test_pycom_expression_constructor_args():
    sig = inspect.signature(pycom_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "outputValue" in params, "Missing parameter 'outputValue'"

def test_pycom_expression_has_outputValue():
    assert hasattr(pycom_Expression, "outputValue")
    descriptor = None
    for klass in pycom_Expression.__mro__:
        if "outputValue" in klass.__dict__:
            descriptor = klass.__dict__["outputValue"]
            break
    assert isinstance(descriptor, property)



def test_pycom_comparisonexp_is_not_abstract():
    assert not inspect.isabstract(pycom_ComparisonExp)


def test_pycom_comparisonexp_constructor_exists():
    assert callable(pycom_ComparisonExp.__init__)


def test_pycom_comparisonexp_constructor_args():
    sig = inspect.signature(pycom_ComparisonExp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_pycom_comparisonexp_has_op():
    assert hasattr(pycom_ComparisonExp, "op")
    descriptor = None
    for klass in pycom_ComparisonExp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_pycom_boolean_is_not_abstract():
    assert not inspect.isabstract(pycom_Boolean)


def test_pycom_boolean_constructor_exists():
    assert callable(pycom_Boolean.__init__)


def test_pycom_boolean_constructor_args():
    sig = inspect.signature(pycom_Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_pycom_boolean_has_value():
    assert hasattr(pycom_Boolean, "value")
    descriptor = None
    for klass in pycom_Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_pycom_logicexp_is_not_abstract():
    assert not inspect.isabstract(pycom_LogicExp)


def test_pycom_logicexp_constructor_exists():
    assert callable(pycom_LogicExp.__init__)


def test_pycom_logicexp_constructor_args():
    sig = inspect.signature(pycom_LogicExp.__init__)
    params = list(sig.parameters.keys())



def test_pycom_boardmember_is_not_abstract():
    assert not inspect.isabstract(pycom_BoardMember)


def test_pycom_boardmember_constructor_exists():
    assert callable(pycom_BoardMember.__init__)


def test_pycom_boardmember_constructor_args():
    sig = inspect.signature(pycom_BoardMember.__init__)
    params = list(sig.parameters.keys())



def test_pycom_host_is_not_abstract():
    assert not inspect.isabstract(pycom_Host)


def test_pycom_host_constructor_exists():
    assert callable(pycom_Host.__init__)


def test_pycom_host_constructor_args():
    sig = inspect.signature(pycom_Host.__init__)
    params = list(sig.parameters.keys())
    assert "ipAdr" in params, "Missing parameter 'ipAdr'"
    assert "website" in params, "Missing parameter 'website'"

def test_pycom_host_has_ipAdr():
    assert hasattr(pycom_Host, "ipAdr")
    descriptor = None
    for klass in pycom_Host.__mro__:
        if "ipAdr" in klass.__dict__:
            descriptor = klass.__dict__["ipAdr"]
            break
    assert isinstance(descriptor, property)

def test_pycom_host_has_website():
    assert hasattr(pycom_Host, "website")
    descriptor = None
    for klass in pycom_Host.__mro__:
        if "website" in klass.__dict__:
            descriptor = klass.__dict__["website"]
            break
    assert isinstance(descriptor, property)



def test_pycom_connection_is_not_abstract():
    assert not inspect.isabstract(pycom_Connection)


def test_pycom_connection_constructor_exists():
    assert callable(pycom_Connection.__init__)


def test_pycom_connection_constructor_args():
    sig = inspect.signature(pycom_Connection.__init__)
    params = list(sig.parameters.keys())
    assert "portnumber" in params, "Missing parameter 'portnumber'"

def test_pycom_connection_has_portnumber():
    assert hasattr(pycom_Connection, "portnumber")
    descriptor = None
    for klass in pycom_Connection.__mro__:
        if "portnumber" in klass.__dict__:
            descriptor = klass.__dict__["portnumber"]
            break
    assert isinstance(descriptor, property)



def test_pycom_server_is_not_abstract():
    assert not inspect.isabstract(pycom_Server)


def test_pycom_server_constructor_exists():
    assert callable(pycom_Server.__init__)


def test_pycom_server_constructor_args():
    sig = inspect.signature(pycom_Server.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pycom_server_has_name():
    assert hasattr(pycom_Server, "name")
    descriptor = None
    for klass in pycom_Server.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pycom_moduletype_is_not_abstract():
    assert not inspect.isabstract(pycom_ModuleType)


def test_pycom_moduletype_constructor_exists():
    assert callable(pycom_ModuleType.__init__)


def test_pycom_moduletype_constructor_args():
    sig = inspect.signature(pycom_ModuleType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_pycom_moduletype_has_name():
    assert hasattr(pycom_ModuleType, "name")
    descriptor = None
    for klass in pycom_ModuleType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pycom_moduletype_has_typeName():
    assert hasattr(pycom_ModuleType, "typeName")
    descriptor = None
    for klass in pycom_ModuleType.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_boardmember_is_not_abstract():
    assert not inspect.isabstract(BoardMember)


def test_boardmember_constructor_exists():
    assert callable(BoardMember.__init__)


def test_boardmember_constructor_args():
    sig = inspect.signature(BoardMember.__init__)
    params = list(sig.parameters.keys())



def test_pycom_communication_is_not_abstract():
    assert not inspect.isabstract(pycom_Communication)


def test_pycom_communication_constructor_exists():
    assert callable(pycom_Communication.__init__)


def test_pycom_communication_constructor_args():
    sig = inspect.signature(pycom_Communication.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_pycom_communication_has_type():
    assert hasattr(pycom_Communication, "type")
    descriptor = None
    for klass in pycom_Communication.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pycom_actuator_is_not_abstract():
    assert not inspect.isabstract(pycom_Actuator)


def test_pycom_actuator_constructor_exists():
    assert callable(pycom_Actuator.__init__)


def test_pycom_actuator_constructor_args():
    sig = inspect.signature(pycom_Actuator.__init__)
    params = list(sig.parameters.keys())



def test_pycom_sensor_is_not_abstract():
    assert not inspect.isabstract(pycom_Sensor)


def test_pycom_sensor_constructor_exists():
    assert callable(pycom_Sensor.__init__)


def test_pycom_sensor_constructor_args():
    sig = inspect.signature(pycom_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_pycom_board_is_not_abstract():
    assert not inspect.isabstract(pycom_Board)


def test_pycom_board_constructor_exists():
    assert callable(pycom_Board.__init__)


def test_pycom_board_constructor_args():
    sig = inspect.signature(pycom_Board.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pycom_board_has_name():
    assert hasattr(pycom_Board, "name")
    descriptor = None
    for klass in pycom_Board.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pycom_expmember_is_not_abstract():
    assert not inspect.isabstract(pycom_ExpMember)


def test_pycom_expmember_constructor_exists():
    assert callable(pycom_ExpMember.__init__)


def test_pycom_expmember_constructor_args():
    sig = inspect.signature(pycom_ExpMember.__init__)
    params = list(sig.parameters.keys())



def test_pycom_system_is_not_abstract():
    assert not inspect.isabstract(pycom_System)


def test_pycom_system_constructor_exists():
    assert callable(pycom_System.__init__)


def test_pycom_system_constructor_args():
    sig = inspect.signature(pycom_System.__init__)
    params = list(sig.parameters.keys())



def test_pycom_condition_is_not_abstract():
    assert not inspect.isabstract(pycom_Condition)


def test_pycom_condition_constructor_exists():
    assert callable(pycom_Condition.__init__)


def test_pycom_condition_constructor_args():
    sig = inspect.signature(pycom_Condition.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_pycom_condition_has_operator():
    assert hasattr(pycom_Condition, "operator")
    descriptor = None
    for klass in pycom_Condition.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expmember_is_not_abstract():
    assert not inspect.isabstract(ExpMember)


def test_expmember_constructor_exists():
    assert callable(ExpMember.__init__)


def test_expmember_constructor_args():
    sig = inspect.signature(ExpMember.__init__)
    params = list(sig.parameters.keys())



def test_pycom_conditionalaction_is_not_abstract():
    assert not inspect.isabstract(pycom_ConditionalAction)


def test_pycom_conditionalaction_constructor_exists():
    assert callable(pycom_ConditionalAction.__init__)


def test_pycom_conditionalaction_constructor_args():
    sig = inspect.signature(pycom_ConditionalAction.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_pycom_conditionalaction_has_type():
    assert hasattr(pycom_ConditionalAction, "type")
    descriptor = None
    for klass in pycom_ConditionalAction.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pycom_function_is_not_abstract():
    assert not inspect.isabstract(pycom_Function)


def test_pycom_function_constructor_exists():
    assert callable(pycom_Function.__init__)


def test_pycom_function_constructor_args():
    sig = inspect.signature(pycom_Function.__init__)
    params = list(sig.parameters.keys())


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
Function_strategy = st.builds(
    Function,
)
pycom_ModuleFunction_strategy = st.builds(
    pycom_ModuleFunction,
)
pycom_FunctionName_strategy = st.builds(
    pycom_FunctionName,
    name=
        safe_text
)
ModuleType_strategy = st.builds(
    ModuleType,
)
pycom_SensorType_strategy = st.builds(
    pycom_SensorType,
)
pycom_ActuatorType_strategy = st.builds(
    pycom_ActuatorType,
)
pycom_PinName_strategy = st.builds(
    pycom_PinName,
    name=
        safe_text
)
pycom_Pin_strategy = st.builds(
    pycom_Pin,
)
pycom_Expression_strategy = st.builds(
    pycom_Expression,
    outputValue=
        st.integers()
)
pycom_ComparisonExp_strategy = st.builds(
    pycom_ComparisonExp,
    op=
        safe_text
)
pycom_Boolean_strategy = st.builds(
    pycom_Boolean,
    value=
        safe_text
)
pycom_LogicExp_strategy = st.builds(
    pycom_LogicExp,
)
pycom_BoardMember_strategy = st.builds(
    pycom_BoardMember,
)
pycom_Host_strategy = st.builds(
    pycom_Host,
    ipAdr=
        safe_text,
    website=
        safe_text
)
pycom_Connection_strategy = st.builds(
    pycom_Connection,
    portnumber=
        safe_text
)
pycom_Server_strategy = st.builds(
    pycom_Server,
    name=
        safe_text
)
pycom_ModuleType_strategy = st.builds(
    pycom_ModuleType,
    name=
        safe_text,
    typeName=
        safe_text
)
BoardMember_strategy = st.builds(
    BoardMember,
)
pycom_Communication_strategy = st.builds(
    pycom_Communication,
    type=
        safe_text
)
pycom_Actuator_strategy = st.builds(
    pycom_Actuator,
)
pycom_Sensor_strategy = st.builds(
    pycom_Sensor,
)
pycom_Board_strategy = st.builds(
    pycom_Board,
    name=
        safe_text
)
pycom_ExpMember_strategy = st.builds(
    pycom_ExpMember,
)
pycom_System_strategy = st.builds(
    pycom_System,
)
pycom_Condition_strategy = st.builds(
    pycom_Condition,
    operator=
        safe_text
)
ExpMember_strategy = st.builds(
    ExpMember,
)
pycom_ConditionalAction_strategy = st.builds(
    pycom_ConditionalAction,
    type=
        safe_text
)
pycom_Function_strategy = st.builds(
    pycom_Function,
)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=pycom_ModuleFunction_strategy)
@settings(max_examples=50)
def test_pycom_modulefunction_instantiation(instance):
    assert isinstance(instance, pycom_ModuleFunction)

@given(instance=pycom_FunctionName_strategy)
@settings(max_examples=50)
def test_pycom_functionname_instantiation(instance):
    assert isinstance(instance, pycom_FunctionName)



@given(instance=pycom_FunctionName_strategy)
def test_pycom_functionname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleType_strategy)
@settings(max_examples=50)
def test_moduletype_instantiation(instance):
    assert isinstance(instance, ModuleType)

@given(instance=pycom_SensorType_strategy)
@settings(max_examples=50)
def test_pycom_sensortype_instantiation(instance):
    assert isinstance(instance, pycom_SensorType)

@given(instance=pycom_ActuatorType_strategy)
@settings(max_examples=50)
def test_pycom_actuatortype_instantiation(instance):
    assert isinstance(instance, pycom_ActuatorType)

@given(instance=pycom_PinName_strategy)
@settings(max_examples=50)
def test_pycom_pinname_instantiation(instance):
    assert isinstance(instance, pycom_PinName)



@given(instance=pycom_PinName_strategy)
def test_pycom_pinname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pycom_Pin_strategy)
@settings(max_examples=50)
def test_pycom_pin_instantiation(instance):
    assert isinstance(instance, pycom_Pin)

@given(instance=pycom_Expression_strategy)
@settings(max_examples=50)
def test_pycom_expression_instantiation(instance):
    assert isinstance(instance, pycom_Expression)



@given(instance=pycom_Expression_strategy)
def test_pycom_expression_outputValue_setter(instance):
    original = instance.outputValue
    instance.outputValue = original
    assert instance.outputValue == original

@given(instance=pycom_ComparisonExp_strategy)
@settings(max_examples=50)
def test_pycom_comparisonexp_instantiation(instance):
    assert isinstance(instance, pycom_ComparisonExp)



@given(instance=pycom_ComparisonExp_strategy)
def test_pycom_comparisonexp_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=pycom_Boolean_strategy)
@settings(max_examples=50)
def test_pycom_boolean_instantiation(instance):
    assert isinstance(instance, pycom_Boolean)



@given(instance=pycom_Boolean_strategy)
def test_pycom_boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=pycom_LogicExp_strategy)
@settings(max_examples=50)
def test_pycom_logicexp_instantiation(instance):
    assert isinstance(instance, pycom_LogicExp)

@given(instance=pycom_BoardMember_strategy)
@settings(max_examples=50)
def test_pycom_boardmember_instantiation(instance):
    assert isinstance(instance, pycom_BoardMember)

@given(instance=pycom_Host_strategy)
@settings(max_examples=50)
def test_pycom_host_instantiation(instance):
    assert isinstance(instance, pycom_Host)



@given(instance=pycom_Host_strategy)
def test_pycom_host_ipAdr_setter(instance):
    original = instance.ipAdr
    instance.ipAdr = original
    assert instance.ipAdr == original



@given(instance=pycom_Host_strategy)
def test_pycom_host_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original

@given(instance=pycom_Connection_strategy)
@settings(max_examples=50)
def test_pycom_connection_instantiation(instance):
    assert isinstance(instance, pycom_Connection)



@given(instance=pycom_Connection_strategy)
def test_pycom_connection_portnumber_setter(instance):
    original = instance.portnumber
    instance.portnumber = original
    assert instance.portnumber == original

@given(instance=pycom_Server_strategy)
@settings(max_examples=50)
def test_pycom_server_instantiation(instance):
    assert isinstance(instance, pycom_Server)



@given(instance=pycom_Server_strategy)
def test_pycom_server_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pycom_ModuleType_strategy)
@settings(max_examples=50)
def test_pycom_moduletype_instantiation(instance):
    assert isinstance(instance, pycom_ModuleType)



@given(instance=pycom_ModuleType_strategy)
def test_pycom_moduletype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pycom_ModuleType_strategy)
def test_pycom_moduletype_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=BoardMember_strategy)
@settings(max_examples=50)
def test_boardmember_instantiation(instance):
    assert isinstance(instance, BoardMember)

@given(instance=pycom_Communication_strategy)
@settings(max_examples=50)
def test_pycom_communication_instantiation(instance):
    assert isinstance(instance, pycom_Communication)



@given(instance=pycom_Communication_strategy)
def test_pycom_communication_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=pycom_Actuator_strategy)
@settings(max_examples=50)
def test_pycom_actuator_instantiation(instance):
    assert isinstance(instance, pycom_Actuator)

@given(instance=pycom_Sensor_strategy)
@settings(max_examples=50)
def test_pycom_sensor_instantiation(instance):
    assert isinstance(instance, pycom_Sensor)

@given(instance=pycom_Board_strategy)
@settings(max_examples=50)
def test_pycom_board_instantiation(instance):
    assert isinstance(instance, pycom_Board)



@given(instance=pycom_Board_strategy)
def test_pycom_board_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pycom_ExpMember_strategy)
@settings(max_examples=50)
def test_pycom_expmember_instantiation(instance):
    assert isinstance(instance, pycom_ExpMember)

@given(instance=pycom_System_strategy)
@settings(max_examples=50)
def test_pycom_system_instantiation(instance):
    assert isinstance(instance, pycom_System)

@given(instance=pycom_Condition_strategy)
@settings(max_examples=50)
def test_pycom_condition_instantiation(instance):
    assert isinstance(instance, pycom_Condition)



@given(instance=pycom_Condition_strategy)
def test_pycom_condition_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ExpMember_strategy)
@settings(max_examples=50)
def test_expmember_instantiation(instance):
    assert isinstance(instance, ExpMember)

@given(instance=pycom_ConditionalAction_strategy)
@settings(max_examples=50)
def test_pycom_conditionalaction_instantiation(instance):
    assert isinstance(instance, pycom_ConditionalAction)



@given(instance=pycom_ConditionalAction_strategy)
def test_pycom_conditionalaction_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=pycom_Function_strategy)
@settings(max_examples=50)
def test_pycom_function_instantiation(instance):
    assert isinstance(instance, pycom_Function)
