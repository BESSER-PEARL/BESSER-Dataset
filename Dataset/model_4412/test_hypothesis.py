import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Parameter,
    Value,
    ModuleInstruction,
    arduino::Level,
    arduino::Status,
    arduino::Connector,
    NamedElement,
    arduino::Platform,
    arduino::Module,
    arduino::Hardware,
    arduino::Project,
    arduino::Function,
    arduino::Instruction,
    Instruction,
    arduino::ModuleInstruction,
    arduino::Value,
    arduino::Sketch,
    arduino::Pin,
    Pin,
    arduino::AnalogPin,
    arduino::DigitalPin,
    arduino::Constant,
    MathOperator,
    arduino::NumericalOperator,
    arduino::Set,
    arduino::Variable,
    arduino::ParameterCall,
    arduino::FunctionCall,
    arduino::Parameter,
    arduino::ParameterDefinition,
    BooleanOperator,
    arduino::Sensor,
    Control,
    arduino::If,
    arduino::Repeat,
    arduino::NamedElement,
    Module,
    arduino::OutputModule,
    arduino::InputModule,
    Utilities,
    arduino::Delay,
    arduino::IO,
    arduino::Utilities,
    arduino::MathOperator,
    arduino::BooleanOperator,
    arduino::While,
    arduino::Control,
    Time,
    Library,
    OperatorKind,
    ModuleKind,
    ParameterType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_moduleinstruction_is_not_abstract():
    assert not inspect.isabstract(ModuleInstruction)


def test_moduleinstruction_constructor_exists():
    assert callable(ModuleInstruction.__init__)


def test_moduleinstruction_constructor_args():
    sig = inspect.signature(ModuleInstruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::level_is_not_abstract():
    assert not inspect.isabstract(arduino::Level)


def test_arduino::level_constructor_exists():
    assert callable(arduino::Level.__init__)


def test_arduino::level_constructor_args():
    sig = inspect.signature(arduino::Level.__init__)
    params = list(sig.parameters.keys())



def test_arduino::status_is_not_abstract():
    assert not inspect.isabstract(arduino::Status)


def test_arduino::status_constructor_exists():
    assert callable(arduino::Status.__init__)


def test_arduino::status_constructor_args():
    sig = inspect.signature(arduino::Status.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_arduino::status_has_status():
    assert hasattr(arduino::Status, "status")
    descriptor = None
    for klass in arduino::Status.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_arduino::connector_is_not_abstract():
    assert not inspect.isabstract(arduino::Connector)


def test_arduino::connector_constructor_exists():
    assert callable(arduino::Connector.__init__)


def test_arduino::connector_constructor_args():
    sig = inspect.signature(arduino::Connector.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_arduino::platform_is_not_abstract():
    assert not inspect.isabstract(arduino::Platform)


def test_arduino::platform_constructor_exists():
    assert callable(arduino::Platform.__init__)


def test_arduino::platform_constructor_args():
    sig = inspect.signature(arduino::Platform.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_arduino::platform_has_image():
    assert hasattr(arduino::Platform, "image")
    descriptor = None
    for klass in arduino::Platform.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_arduino::module_is_not_abstract():
    assert not inspect.isabstract(arduino::Module)


def test_arduino::module_constructor_exists():
    assert callable(arduino::Module.__init__)


def test_arduino::module_constructor_args():
    sig = inspect.signature(arduino::Module.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "image" in params, "Missing parameter 'image'"
    assert "library" in params, "Missing parameter 'library'"

def test_arduino::module_has_level():
    assert hasattr(arduino::Module, "level")
    descriptor = None
    for klass in arduino::Module.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_arduino::module_has_kind():
    assert hasattr(arduino::Module, "kind")
    descriptor = None
    for klass in arduino::Module.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_arduino::module_has_image():
    assert hasattr(arduino::Module, "image")
    descriptor = None
    for klass in arduino::Module.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_arduino::module_has_library():
    assert hasattr(arduino::Module, "library")
    descriptor = None
    for klass in arduino::Module.__mro__:
        if "library" in klass.__dict__:
            descriptor = klass.__dict__["library"]
            break
    assert isinstance(descriptor, property)



def test_arduino::hardware_is_not_abstract():
    assert not inspect.isabstract(arduino::Hardware)


def test_arduino::hardware_constructor_exists():
    assert callable(arduino::Hardware.__init__)


def test_arduino::hardware_constructor_args():
    sig = inspect.signature(arduino::Hardware.__init__)
    params = list(sig.parameters.keys())



def test_arduino::project_is_not_abstract():
    assert not inspect.isabstract(arduino::Project)


def test_arduino::project_constructor_exists():
    assert callable(arduino::Project.__init__)


def test_arduino::project_constructor_args():
    sig = inspect.signature(arduino::Project.__init__)
    params = list(sig.parameters.keys())



def test_arduino::function_is_not_abstract():
    assert not inspect.isabstract(arduino::Function)


def test_arduino::function_constructor_exists():
    assert callable(arduino::Function.__init__)


def test_arduino::function_constructor_args():
    sig = inspect.signature(arduino::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::function_has_name():
    assert hasattr(arduino::Function, "name")
    descriptor = None
    for klass in arduino::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::instruction_is_not_abstract():
    assert not inspect.isabstract(arduino::Instruction)


def test_arduino::instruction_constructor_exists():
    assert callable(arduino::Instruction.__init__)


def test_arduino::instruction_constructor_args():
    sig = inspect.signature(arduino::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::moduleinstruction_is_not_abstract():
    assert not inspect.isabstract(arduino::ModuleInstruction)


def test_arduino::moduleinstruction_constructor_exists():
    assert callable(arduino::ModuleInstruction.__init__)


def test_arduino::moduleinstruction_constructor_args():
    sig = inspect.signature(arduino::ModuleInstruction.__init__)
    params = list(sig.parameters.keys())



def test_arduino::value_is_not_abstract():
    assert not inspect.isabstract(arduino::Value)


def test_arduino::value_constructor_exists():
    assert callable(arduino::Value.__init__)


def test_arduino::value_constructor_args():
    sig = inspect.signature(arduino::Value.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_arduino::value_has_value():
    assert hasattr(arduino::Value, "value")
    descriptor = None
    for klass in arduino::Value.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_arduino::sketch_is_not_abstract():
    assert not inspect.isabstract(arduino::Sketch)


def test_arduino::sketch_constructor_exists():
    assert callable(arduino::Sketch.__init__)


def test_arduino::sketch_constructor_args():
    sig = inspect.signature(arduino::Sketch.__init__)
    params = list(sig.parameters.keys())



def test_arduino::pin_is_not_abstract():
    assert not inspect.isabstract(arduino::Pin)


def test_arduino::pin_constructor_exists():
    assert callable(arduino::Pin.__init__)


def test_arduino::pin_constructor_args():
    sig = inspect.signature(arduino::Pin.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_arduino::pin_has_id():
    assert hasattr(arduino::Pin, "id")
    descriptor = None
    for klass in arduino::Pin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_arduino::analogpin_is_not_abstract():
    assert not inspect.isabstract(arduino::AnalogPin)


def test_arduino::analogpin_constructor_exists():
    assert callable(arduino::AnalogPin.__init__)


def test_arduino::analogpin_constructor_args():
    sig = inspect.signature(arduino::AnalogPin.__init__)
    params = list(sig.parameters.keys())



def test_arduino::digitalpin_is_not_abstract():
    assert not inspect.isabstract(arduino::DigitalPin)


def test_arduino::digitalpin_constructor_exists():
    assert callable(arduino::DigitalPin.__init__)


def test_arduino::digitalpin_constructor_args():
    sig = inspect.signature(arduino::DigitalPin.__init__)
    params = list(sig.parameters.keys())



def test_arduino::constant_is_not_abstract():
    assert not inspect.isabstract(arduino::Constant)


def test_arduino::constant_constructor_exists():
    assert callable(arduino::Constant.__init__)


def test_arduino::constant_constructor_args():
    sig = inspect.signature(arduino::Constant.__init__)
    params = list(sig.parameters.keys())



def test_mathoperator_is_not_abstract():
    assert not inspect.isabstract(MathOperator)


def test_mathoperator_constructor_exists():
    assert callable(MathOperator.__init__)


def test_mathoperator_constructor_args():
    sig = inspect.signature(MathOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduino::numericaloperator_is_not_abstract():
    assert not inspect.isabstract(arduino::NumericalOperator)


def test_arduino::numericaloperator_constructor_exists():
    assert callable(arduino::NumericalOperator.__init__)


def test_arduino::numericaloperator_constructor_args():
    sig = inspect.signature(arduino::NumericalOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduino::set_is_not_abstract():
    assert not inspect.isabstract(arduino::Set)


def test_arduino::set_constructor_exists():
    assert callable(arduino::Set.__init__)


def test_arduino::set_constructor_args():
    sig = inspect.signature(arduino::Set.__init__)
    params = list(sig.parameters.keys())



def test_arduino::variable_is_not_abstract():
    assert not inspect.isabstract(arduino::Variable)


def test_arduino::variable_constructor_exists():
    assert callable(arduino::Variable.__init__)


def test_arduino::variable_constructor_args():
    sig = inspect.signature(arduino::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::variable_has_name():
    assert hasattr(arduino::Variable, "name")
    descriptor = None
    for klass in arduino::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arduino::parametercall_is_not_abstract():
    assert not inspect.isabstract(arduino::ParameterCall)


def test_arduino::parametercall_constructor_exists():
    assert callable(arduino::ParameterCall.__init__)


def test_arduino::parametercall_constructor_args():
    sig = inspect.signature(arduino::ParameterCall.__init__)
    params = list(sig.parameters.keys())



def test_arduino::functioncall_is_not_abstract():
    assert not inspect.isabstract(arduino::FunctionCall)


def test_arduino::functioncall_constructor_exists():
    assert callable(arduino::FunctionCall.__init__)


def test_arduino::functioncall_constructor_args():
    sig = inspect.signature(arduino::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_arduino::parameter_is_not_abstract():
    assert not inspect.isabstract(arduino::Parameter)


def test_arduino::parameter_constructor_exists():
    assert callable(arduino::Parameter.__init__)


def test_arduino::parameter_constructor_args():
    sig = inspect.signature(arduino::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_arduino::parameterdefinition_is_not_abstract():
    assert not inspect.isabstract(arduino::ParameterDefinition)


def test_arduino::parameterdefinition_constructor_exists():
    assert callable(arduino::ParameterDefinition.__init__)


def test_arduino::parameterdefinition_constructor_args():
    sig = inspect.signature(arduino::ParameterDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::parameterdefinition_has_type():
    assert hasattr(arduino::ParameterDefinition, "type")
    descriptor = None
    for klass in arduino::ParameterDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_arduino::parameterdefinition_has_name():
    assert hasattr(arduino::ParameterDefinition, "name")
    descriptor = None
    for klass in arduino::ParameterDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_booleanoperator_is_not_abstract():
    assert not inspect.isabstract(BooleanOperator)


def test_booleanoperator_constructor_exists():
    assert callable(BooleanOperator.__init__)


def test_booleanoperator_constructor_args():
    sig = inspect.signature(BooleanOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduino::sensor_is_not_abstract():
    assert not inspect.isabstract(arduino::Sensor)


def test_arduino::sensor_constructor_exists():
    assert callable(arduino::Sensor.__init__)


def test_arduino::sensor_constructor_args():
    sig = inspect.signature(arduino::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_arduino::if_is_not_abstract():
    assert not inspect.isabstract(arduino::If)


def test_arduino::if_constructor_exists():
    assert callable(arduino::If.__init__)


def test_arduino::if_constructor_args():
    sig = inspect.signature(arduino::If.__init__)
    params = list(sig.parameters.keys())



def test_arduino::repeat_is_not_abstract():
    assert not inspect.isabstract(arduino::Repeat)


def test_arduino::repeat_constructor_exists():
    assert callable(arduino::Repeat.__init__)


def test_arduino::repeat_constructor_args():
    sig = inspect.signature(arduino::Repeat.__init__)
    params = list(sig.parameters.keys())
    assert "iteration" in params, "Missing parameter 'iteration'"

def test_arduino::repeat_has_iteration():
    assert hasattr(arduino::Repeat, "iteration")
    descriptor = None
    for klass in arduino::Repeat.__mro__:
        if "iteration" in klass.__dict__:
            descriptor = klass.__dict__["iteration"]
            break
    assert isinstance(descriptor, property)



def test_arduino::namedelement_is_not_abstract():
    assert not inspect.isabstract(arduino::NamedElement)


def test_arduino::namedelement_constructor_exists():
    assert callable(arduino::NamedElement.__init__)


def test_arduino::namedelement_constructor_args():
    sig = inspect.signature(arduino::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_arduino::namedelement_has_name():
    assert hasattr(arduino::NamedElement, "name")
    descriptor = None
    for klass in arduino::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_module_is_not_abstract():
    assert not inspect.isabstract(Module)


def test_module_constructor_exists():
    assert callable(Module.__init__)


def test_module_constructor_args():
    sig = inspect.signature(Module.__init__)
    params = list(sig.parameters.keys())



def test_arduino::outputmodule_is_not_abstract():
    assert not inspect.isabstract(arduino::OutputModule)


def test_arduino::outputmodule_constructor_exists():
    assert callable(arduino::OutputModule.__init__)


def test_arduino::outputmodule_constructor_args():
    sig = inspect.signature(arduino::OutputModule.__init__)
    params = list(sig.parameters.keys())



def test_arduino::inputmodule_is_not_abstract():
    assert not inspect.isabstract(arduino::InputModule)


def test_arduino::inputmodule_constructor_exists():
    assert callable(arduino::InputModule.__init__)


def test_arduino::inputmodule_constructor_args():
    sig = inspect.signature(arduino::InputModule.__init__)
    params = list(sig.parameters.keys())



def test_utilities_is_not_abstract():
    assert not inspect.isabstract(Utilities)


def test_utilities_constructor_exists():
    assert callable(Utilities.__init__)


def test_utilities_constructor_args():
    sig = inspect.signature(Utilities.__init__)
    params = list(sig.parameters.keys())



def test_arduino::delay_is_not_abstract():
    assert not inspect.isabstract(arduino::Delay)


def test_arduino::delay_constructor_exists():
    assert callable(arduino::Delay.__init__)


def test_arduino::delay_constructor_args():
    sig = inspect.signature(arduino::Delay.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_arduino::delay_has_value():
    assert hasattr(arduino::Delay, "value")
    descriptor = None
    for klass in arduino::Delay.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_arduino::delay_has_unit():
    assert hasattr(arduino::Delay, "unit")
    descriptor = None
    for klass in arduino::Delay.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_arduino::io_is_not_abstract():
    assert not inspect.isabstract(arduino::IO)


def test_arduino::io_constructor_exists():
    assert callable(arduino::IO.__init__)


def test_arduino::io_constructor_args():
    sig = inspect.signature(arduino::IO.__init__)
    params = list(sig.parameters.keys())



def test_arduino::utilities_is_not_abstract():
    assert not inspect.isabstract(arduino::Utilities)


def test_arduino::utilities_constructor_exists():
    assert callable(arduino::Utilities.__init__)


def test_arduino::utilities_constructor_args():
    sig = inspect.signature(arduino::Utilities.__init__)
    params = list(sig.parameters.keys())



def test_arduino::mathoperator_is_not_abstract():
    assert not inspect.isabstract(arduino::MathOperator)


def test_arduino::mathoperator_constructor_exists():
    assert callable(arduino::MathOperator.__init__)


def test_arduino::mathoperator_constructor_args():
    sig = inspect.signature(arduino::MathOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_arduino::mathoperator_has_operator():
    assert hasattr(arduino::MathOperator, "operator")
    descriptor = None
    for klass in arduino::MathOperator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_arduino::booleanoperator_is_not_abstract():
    assert not inspect.isabstract(arduino::BooleanOperator)


def test_arduino::booleanoperator_constructor_exists():
    assert callable(arduino::BooleanOperator.__init__)


def test_arduino::booleanoperator_constructor_args():
    sig = inspect.signature(arduino::BooleanOperator.__init__)
    params = list(sig.parameters.keys())



def test_arduino::while_is_not_abstract():
    assert not inspect.isabstract(arduino::While)


def test_arduino::while_constructor_exists():
    assert callable(arduino::While.__init__)


def test_arduino::while_constructor_args():
    sig = inspect.signature(arduino::While.__init__)
    params = list(sig.parameters.keys())



def test_arduino::control_is_not_abstract():
    assert not inspect.isabstract(arduino::Control)


def test_arduino::control_constructor_exists():
    assert callable(arduino::Control.__init__)


def test_arduino::control_constructor_args():
    sig = inspect.signature(arduino::Control.__init__)
    params = list(sig.parameters.keys())

def test_time_exists():
    # Check that the Enumeration exists
    assert Time is not None

def test_time_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Time]
    expected_literals = [
        "MilliSecond",
        "MicroSecond",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Time"

def test_library_exists():
    # Check that the Enumeration exists
    assert Library is not None

def test_library_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Library]
    expected_literals = [
        "music",
        "servo",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Library"

def test_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "equal",
        "diff",
        "plus",
        "minus",
        "min",
        "pourcent",
        "max",
        "lowerOrEqual",
        "upperOrEqual",
        "mul",
        "lower",
        "div",
        "not_",
        "upper",
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"

def test_modulekind_exists():
    # Check that the Enumeration exists
    assert ModuleKind is not None

def test_modulekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModuleKind]
    expected_literals = [
        "analog",
        "digital",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModuleKind"

def test_parametertype_exists():
    # Check that the Enumeration exists
    assert ParameterType is not None

def test_parametertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterType]
    expected_literals = [
        "Constant",
        "Delay",
        "Sensor",
        "Status",
        "Level",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterType"


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
Parameter_strategy = st.builds(
    Parameter,
)
Value_strategy = st.builds(
    Value,
)
ModuleInstruction_strategy = st.builds(
    ModuleInstruction,
)
arduino::Level_strategy = st.builds(
    arduino::Level,
)
arduino::Status_strategy = st.builds(
    arduino::Status,
    status=
        st.booleans()
)
arduino::Connector_strategy = st.builds(
    arduino::Connector,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
arduino::Platform_strategy = st.builds(
    arduino::Platform,
    image=
        safe_text
)
arduino::Module_strategy = st.builds(
    arduino::Module,
    level=
        st.booleans(),
    kind=
        safe_text,
    image=
        safe_text,
    library=
        safe_text
)
arduino::Hardware_strategy = st.builds(
    arduino::Hardware,
)
arduino::Project_strategy = st.builds(
    arduino::Project,
)
arduino::Function_strategy = st.builds(
    arduino::Function,
    name=
        safe_text
)
arduino::Instruction_strategy = st.builds(
    arduino::Instruction,
)
Instruction_strategy = st.builds(
    Instruction,
)
arduino::ModuleInstruction_strategy = st.builds(
    arduino::ModuleInstruction,
)
arduino::Value_strategy = st.builds(
    arduino::Value,
    value=
        safe_text
)
arduino::Sketch_strategy = st.builds(
    arduino::Sketch,
)
arduino::Pin_strategy = st.builds(
    arduino::Pin,
    id=
        st.integers()
)
Pin_strategy = st.builds(
    Pin,
)
arduino::AnalogPin_strategy = st.builds(
    arduino::AnalogPin,
)
arduino::DigitalPin_strategy = st.builds(
    arduino::DigitalPin,
)
arduino::Constant_strategy = st.builds(
    arduino::Constant,
)
MathOperator_strategy = st.builds(
    MathOperator,
)
arduino::NumericalOperator_strategy = st.builds(
    arduino::NumericalOperator,
)
arduino::Set_strategy = st.builds(
    arduino::Set,
)
arduino::Variable_strategy = st.builds(
    arduino::Variable,
    name=
        safe_text
)
arduino::ParameterCall_strategy = st.builds(
    arduino::ParameterCall,
)
arduino::FunctionCall_strategy = st.builds(
    arduino::FunctionCall,
)
arduino::Parameter_strategy = st.builds(
    arduino::Parameter,
)
arduino::ParameterDefinition_strategy = st.builds(
    arduino::ParameterDefinition,
    type=
        safe_text,
    name=
        safe_text
)
BooleanOperator_strategy = st.builds(
    BooleanOperator,
)
arduino::Sensor_strategy = st.builds(
    arduino::Sensor,
)
Control_strategy = st.builds(
    Control,
)
arduino::If_strategy = st.builds(
    arduino::If,
)
arduino::Repeat_strategy = st.builds(
    arduino::Repeat,
    iteration=
        st.integers()
)
arduino::NamedElement_strategy = st.builds(
    arduino::NamedElement,
    name=
        safe_text
)
Module_strategy = st.builds(
    Module,
)
arduino::OutputModule_strategy = st.builds(
    arduino::OutputModule,
)
arduino::InputModule_strategy = st.builds(
    arduino::InputModule,
)
Utilities_strategy = st.builds(
    Utilities,
)
arduino::Delay_strategy = st.builds(
    arduino::Delay,
    value=
        st.integers(),
    unit=
        safe_text
)
arduino::IO_strategy = st.builds(
    arduino::IO,
)
arduino::Utilities_strategy = st.builds(
    arduino::Utilities,
)
arduino::MathOperator_strategy = st.builds(
    arduino::MathOperator,
    operator=
        safe_text
)
arduino::BooleanOperator_strategy = st.builds(
    arduino::BooleanOperator,
)
arduino::While_strategy = st.builds(
    arduino::While,
)
arduino::Control_strategy = st.builds(
    arduino::Control,
)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=ModuleInstruction_strategy)
@settings(max_examples=50)
def test_moduleinstruction_instantiation(instance):
    assert isinstance(instance, ModuleInstruction)

@given(instance=arduino::Level_strategy)
@settings(max_examples=50)
def test_arduino::level_instantiation(instance):
    assert isinstance(instance, arduino::Level)

@given(instance=arduino::Status_strategy)
@settings(max_examples=50)
def test_arduino::status_instantiation(instance):
    assert isinstance(instance, arduino::Status)

@given(instance=arduino::Status_strategy)
def test_arduino::status_status_type(instance):
    assert isinstance(instance.status, bool)


@given(instance=arduino::Status_strategy)
def test_arduino::status_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=arduino::Connector_strategy)
@settings(max_examples=50)
def test_arduino::connector_instantiation(instance):
    assert isinstance(instance, arduino::Connector)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=arduino::Platform_strategy)
@settings(max_examples=50)
def test_arduino::platform_instantiation(instance):
    assert isinstance(instance, arduino::Platform)

@given(instance=arduino::Platform_strategy)
def test_arduino::platform_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=arduino::Platform_strategy)
def test_arduino::platform_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=arduino::Module_strategy)
@settings(max_examples=50)
def test_arduino::module_instantiation(instance):
    assert isinstance(instance, arduino::Module)

@given(instance=arduino::Module_strategy)
def test_arduino::module_level_type(instance):
    assert isinstance(instance.level, bool)


@given(instance=arduino::Module_strategy)
def test_arduino::module_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=arduino::Module_strategy)
def test_arduino::module_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=arduino::Module_strategy)
def test_arduino::module_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=arduino::Module_strategy)
def test_arduino::module_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=arduino::Module_strategy)
def test_arduino::module_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=arduino::Module_strategy)
def test_arduino::module_library_type(instance):
    assert isinstance(instance.library, str)


@given(instance=arduino::Module_strategy)
def test_arduino::module_library_setter(instance):
    original = instance.library
    instance.library = original
    assert instance.library == original

@given(instance=arduino::Hardware_strategy)
@settings(max_examples=50)
def test_arduino::hardware_instantiation(instance):
    assert isinstance(instance, arduino::Hardware)

@given(instance=arduino::Project_strategy)
@settings(max_examples=50)
def test_arduino::project_instantiation(instance):
    assert isinstance(instance, arduino::Project)

@given(instance=arduino::Function_strategy)
@settings(max_examples=50)
def test_arduino::function_instantiation(instance):
    assert isinstance(instance, arduino::Function)

@given(instance=arduino::Function_strategy)
def test_arduino::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Function_strategy)
def test_arduino::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::Instruction_strategy)
@settings(max_examples=50)
def test_arduino::instruction_instantiation(instance):
    assert isinstance(instance, arduino::Instruction)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=arduino::ModuleInstruction_strategy)
@settings(max_examples=50)
def test_arduino::moduleinstruction_instantiation(instance):
    assert isinstance(instance, arduino::ModuleInstruction)

@given(instance=arduino::Value_strategy)
@settings(max_examples=50)
def test_arduino::value_instantiation(instance):
    assert isinstance(instance, arduino::Value)

@given(instance=arduino::Value_strategy)
def test_arduino::value_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=arduino::Value_strategy)
def test_arduino::value_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduino::Sketch_strategy)
@settings(max_examples=50)
def test_arduino::sketch_instantiation(instance):
    assert isinstance(instance, arduino::Sketch)

@given(instance=arduino::Pin_strategy)
@settings(max_examples=50)
def test_arduino::pin_instantiation(instance):
    assert isinstance(instance, arduino::Pin)

@given(instance=arduino::Pin_strategy)
def test_arduino::pin_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=arduino::Pin_strategy)
def test_arduino::pin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=arduino::AnalogPin_strategy)
@settings(max_examples=50)
def test_arduino::analogpin_instantiation(instance):
    assert isinstance(instance, arduino::AnalogPin)

@given(instance=arduino::DigitalPin_strategy)
@settings(max_examples=50)
def test_arduino::digitalpin_instantiation(instance):
    assert isinstance(instance, arduino::DigitalPin)

@given(instance=arduino::Constant_strategy)
@settings(max_examples=50)
def test_arduino::constant_instantiation(instance):
    assert isinstance(instance, arduino::Constant)

@given(instance=MathOperator_strategy)
@settings(max_examples=50)
def test_mathoperator_instantiation(instance):
    assert isinstance(instance, MathOperator)

@given(instance=arduino::NumericalOperator_strategy)
@settings(max_examples=50)
def test_arduino::numericaloperator_instantiation(instance):
    assert isinstance(instance, arduino::NumericalOperator)

@given(instance=arduino::Set_strategy)
@settings(max_examples=50)
def test_arduino::set_instantiation(instance):
    assert isinstance(instance, arduino::Set)

@given(instance=arduino::Variable_strategy)
@settings(max_examples=50)
def test_arduino::variable_instantiation(instance):
    assert isinstance(instance, arduino::Variable)

@given(instance=arduino::Variable_strategy)
def test_arduino::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::Variable_strategy)
def test_arduino::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=arduino::ParameterCall_strategy)
@settings(max_examples=50)
def test_arduino::parametercall_instantiation(instance):
    assert isinstance(instance, arduino::ParameterCall)

@given(instance=arduino::FunctionCall_strategy)
@settings(max_examples=50)
def test_arduino::functioncall_instantiation(instance):
    assert isinstance(instance, arduino::FunctionCall)

@given(instance=arduino::Parameter_strategy)
@settings(max_examples=50)
def test_arduino::parameter_instantiation(instance):
    assert isinstance(instance, arduino::Parameter)

@given(instance=arduino::ParameterDefinition_strategy)
@settings(max_examples=50)
def test_arduino::parameterdefinition_instantiation(instance):
    assert isinstance(instance, arduino::ParameterDefinition)

@given(instance=arduino::ParameterDefinition_strategy)
def test_arduino::parameterdefinition_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=arduino::ParameterDefinition_strategy)
def test_arduino::parameterdefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=arduino::ParameterDefinition_strategy)
def test_arduino::parameterdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::ParameterDefinition_strategy)
def test_arduino::parameterdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BooleanOperator_strategy)
@settings(max_examples=50)
def test_booleanoperator_instantiation(instance):
    assert isinstance(instance, BooleanOperator)

@given(instance=arduino::Sensor_strategy)
@settings(max_examples=50)
def test_arduino::sensor_instantiation(instance):
    assert isinstance(instance, arduino::Sensor)

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=arduino::If_strategy)
@settings(max_examples=50)
def test_arduino::if_instantiation(instance):
    assert isinstance(instance, arduino::If)

@given(instance=arduino::Repeat_strategy)
@settings(max_examples=50)
def test_arduino::repeat_instantiation(instance):
    assert isinstance(instance, arduino::Repeat)

@given(instance=arduino::Repeat_strategy)
def test_arduino::repeat_iteration_type(instance):
    assert isinstance(instance.iteration, int)


@given(instance=arduino::Repeat_strategy)
def test_arduino::repeat_iteration_setter(instance):
    original = instance.iteration
    instance.iteration = original
    assert instance.iteration == original

@given(instance=arduino::NamedElement_strategy)
@settings(max_examples=50)
def test_arduino::namedelement_instantiation(instance):
    assert isinstance(instance, arduino::NamedElement)

@given(instance=arduino::NamedElement_strategy)
def test_arduino::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=arduino::NamedElement_strategy)
def test_arduino::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Module_strategy)
@settings(max_examples=50)
def test_module_instantiation(instance):
    assert isinstance(instance, Module)

@given(instance=arduino::OutputModule_strategy)
@settings(max_examples=50)
def test_arduino::outputmodule_instantiation(instance):
    assert isinstance(instance, arduino::OutputModule)

@given(instance=arduino::InputModule_strategy)
@settings(max_examples=50)
def test_arduino::inputmodule_instantiation(instance):
    assert isinstance(instance, arduino::InputModule)

@given(instance=Utilities_strategy)
@settings(max_examples=50)
def test_utilities_instantiation(instance):
    assert isinstance(instance, Utilities)

@given(instance=arduino::Delay_strategy)
@settings(max_examples=50)
def test_arduino::delay_instantiation(instance):
    assert isinstance(instance, arduino::Delay)

@given(instance=arduino::Delay_strategy)
def test_arduino::delay_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=arduino::Delay_strategy)
def test_arduino::delay_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=arduino::Delay_strategy)
def test_arduino::delay_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=arduino::Delay_strategy)
def test_arduino::delay_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=arduino::IO_strategy)
@settings(max_examples=50)
def test_arduino::io_instantiation(instance):
    assert isinstance(instance, arduino::IO)

@given(instance=arduino::Utilities_strategy)
@settings(max_examples=50)
def test_arduino::utilities_instantiation(instance):
    assert isinstance(instance, arduino::Utilities)

@given(instance=arduino::MathOperator_strategy)
@settings(max_examples=50)
def test_arduino::mathoperator_instantiation(instance):
    assert isinstance(instance, arduino::MathOperator)

@given(instance=arduino::MathOperator_strategy)
def test_arduino::mathoperator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=arduino::MathOperator_strategy)
def test_arduino::mathoperator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=arduino::BooleanOperator_strategy)
@settings(max_examples=50)
def test_arduino::booleanoperator_instantiation(instance):
    assert isinstance(instance, arduino::BooleanOperator)

@given(instance=arduino::While_strategy)
@settings(max_examples=50)
def test_arduino::while_instantiation(instance):
    assert isinstance(instance, arduino::While)

@given(instance=arduino::Control_strategy)
@settings(max_examples=50)
def test_arduino::control_instantiation(instance):
    assert isinstance(instance, arduino::Control)
