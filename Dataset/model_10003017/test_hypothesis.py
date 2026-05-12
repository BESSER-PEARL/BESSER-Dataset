import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RAM1,
    CPU1,
    Hardware,
    FastCard,
    ExtensionBoard,
    Vendor2Sound,
    Vendor1Sound,
    Vendor2Adapter,
    Vendor1Adapter,
    GenericSound,
    Sound,
    Card,
    DeviceCard,
    Memory_Interface,
    Instruction,
    Program,
    Machine,
    RAM,
    Cache,
    AcceleratorCard,
    Processor,
    CPU,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ram1_is_not_abstract():
    assert not inspect.isabstract(RAM1)


def test_ram1_constructor_exists():
    assert callable(RAM1.__init__)


def test_ram1_constructor_args():
    sig = inspect.signature(RAM1.__init__)
    params = list(sig.parameters.keys())
    assert "mb" in params, "Missing parameter 'mb'"

def test_ram1_has_mb():
    assert hasattr(RAM1, "mb")
    descriptor = None
    for klass in RAM1.__mro__:
        if "mb" in klass.__dict__:
            descriptor = klass.__dict__["mb"]
            break
    assert isinstance(descriptor, property)



def test_cpu1_is_not_abstract():
    assert not inspect.isabstract(CPU1)


def test_cpu1_constructor_exists():
    assert callable(CPU1.__init__)


def test_cpu1_constructor_args():
    sig = inspect.signature(CPU1.__init__)
    params = list(sig.parameters.keys())
    assert "mhz" in params, "Missing parameter 'mhz'"

def test_cpu1_has_mhz():
    assert hasattr(CPU1, "mhz")
    descriptor = None
    for klass in CPU1.__mro__:
        if "mhz" in klass.__dict__:
            descriptor = klass.__dict__["mhz"]
            break
    assert isinstance(descriptor, property)



def test_hardware_is_not_abstract():
    assert not inspect.isabstract(Hardware)


def test_hardware_constructor_exists():
    assert callable(Hardware.__init__)


def test_hardware_constructor_args():
    sig = inspect.signature(Hardware.__init__)
    params = list(sig.parameters.keys())
    assert "manufacturer" in params, "Missing parameter 'manufacturer'"
    assert "serialNo" in params, "Missing parameter 'serialNo'"

def test_hardware_has_manufacturer():
    assert hasattr(Hardware, "manufacturer")
    descriptor = None
    for klass in Hardware.__mro__:
        if "manufacturer" in klass.__dict__:
            descriptor = klass.__dict__["manufacturer"]
            break
    assert isinstance(descriptor, property)

def test_hardware_has_serialNo():
    assert hasattr(Hardware, "serialNo")
    descriptor = None
    for klass in Hardware.__mro__:
        if "serialNo" in klass.__dict__:
            descriptor = klass.__dict__["serialNo"]
            break
    assert isinstance(descriptor, property)



def test_fastcard_is_not_abstract():
    assert not inspect.isabstract(FastCard)


def test_fastcard_constructor_exists():
    assert callable(FastCard.__init__)


def test_fastcard_constructor_args():
    sig = inspect.signature(FastCard.__init__)
    params = list(sig.parameters.keys())



def test_extensionboard_is_not_abstract():
    assert not inspect.isabstract(ExtensionBoard)


def test_extensionboard_constructor_exists():
    assert callable(ExtensionBoard.__init__)


def test_extensionboard_constructor_args():
    sig = inspect.signature(ExtensionBoard.__init__)
    params = list(sig.parameters.keys())



def test_vendor2sound_is_not_abstract():
    assert not inspect.isabstract(Vendor2Sound)


def test_vendor2sound_constructor_exists():
    assert callable(Vendor2Sound.__init__)


def test_vendor2sound_constructor_args():
    sig = inspect.signature(Vendor2Sound.__init__)
    params = list(sig.parameters.keys())



def test_vendor1sound_is_not_abstract():
    assert not inspect.isabstract(Vendor1Sound)


def test_vendor1sound_constructor_exists():
    assert callable(Vendor1Sound.__init__)


def test_vendor1sound_constructor_args():
    sig = inspect.signature(Vendor1Sound.__init__)
    params = list(sig.parameters.keys())



def test_vendor2adapter_is_not_abstract():
    assert not inspect.isabstract(Vendor2Adapter)


def test_vendor2adapter_constructor_exists():
    assert callable(Vendor2Adapter.__init__)


def test_vendor2adapter_constructor_args():
    sig = inspect.signature(Vendor2Adapter.__init__)
    params = list(sig.parameters.keys())



def test_vendor1adapter_is_not_abstract():
    assert not inspect.isabstract(Vendor1Adapter)


def test_vendor1adapter_constructor_exists():
    assert callable(Vendor1Adapter.__init__)


def test_vendor1adapter_constructor_args():
    sig = inspect.signature(Vendor1Adapter.__init__)
    params = list(sig.parameters.keys())



def test_genericsound_is_not_abstract():
    assert not inspect.isabstract(GenericSound)


def test_genericsound_constructor_exists():
    assert callable(GenericSound.__init__)


def test_genericsound_constructor_args():
    sig = inspect.signature(GenericSound.__init__)
    params = list(sig.parameters.keys())



def test_sound_is_not_abstract():
    assert not inspect.isabstract(Sound)


def test_sound_constructor_exists():
    assert callable(Sound.__init__)


def test_sound_constructor_args():
    sig = inspect.signature(Sound.__init__)
    params = list(sig.parameters.keys())



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())



def test_devicecard_is_not_abstract():
    assert not inspect.isabstract(DeviceCard)


def test_devicecard_constructor_exists():
    assert callable(DeviceCard.__init__)


def test_devicecard_constructor_args():
    sig = inspect.signature(DeviceCard.__init__)
    params = list(sig.parameters.keys())



def test_memory_interface_is_not_abstract():
    assert not inspect.isabstract(Memory_Interface)


def test_memory_interface_constructor_exists():
    assert callable(Memory_Interface.__init__)


def test_memory_interface_constructor_args():
    sig = inspect.signature(Memory_Interface.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_program_is_not_abstract():
    assert not inspect.isabstract(Program)


def test_program_constructor_exists():
    assert callable(Program.__init__)


def test_program_constructor_args():
    sig = inspect.signature(Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_program_has_name():
    assert hasattr(Program, "name")
    descriptor = None
    for klass in Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_machine_is_not_abstract():
    assert not inspect.isabstract(Machine)


def test_machine_constructor_exists():
    assert callable(Machine.__init__)


def test_machine_constructor_args():
    sig = inspect.signature(Machine.__init__)
    params = list(sig.parameters.keys())



def test_ram_is_not_abstract():
    assert not inspect.isabstract(RAM)


def test_ram_constructor_exists():
    assert callable(RAM.__init__)


def test_ram_constructor_args():
    sig = inspect.signature(RAM.__init__)
    params = list(sig.parameters.keys())



def test_cache_is_not_abstract():
    assert not inspect.isabstract(Cache)


def test_cache_constructor_exists():
    assert callable(Cache.__init__)


def test_cache_constructor_args():
    sig = inspect.signature(Cache.__init__)
    params = list(sig.parameters.keys())
    assert "chunck" in params, "Missing parameter 'chunck'"

def test_cache_has_chunck():
    assert hasattr(Cache, "chunck")
    descriptor = None
    for klass in Cache.__mro__:
        if "chunck" in klass.__dict__:
            descriptor = klass.__dict__["chunck"]
            break
    assert isinstance(descriptor, property)



def test_acceleratorcard_is_not_abstract():
    assert not inspect.isabstract(AcceleratorCard)


def test_acceleratorcard_constructor_exists():
    assert callable(AcceleratorCard.__init__)


def test_acceleratorcard_constructor_args():
    sig = inspect.signature(AcceleratorCard.__init__)
    params = list(sig.parameters.keys())



def test_processor_is_not_abstract():
    assert not inspect.isabstract(Processor)


def test_processor_constructor_exists():
    assert callable(Processor.__init__)


def test_processor_constructor_args():
    sig = inspect.signature(Processor.__init__)
    params = list(sig.parameters.keys())



def test_cpu_is_not_abstract():
    assert not inspect.isabstract(CPU)


def test_cpu_constructor_exists():
    assert callable(CPU.__init__)


def test_cpu_constructor_args():
    sig = inspect.signature(CPU.__init__)
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
RAM1_strategy = st.builds(
    RAM1,
    mb=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
CPU1_strategy = st.builds(
    CPU1,
    mhz=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Hardware_strategy = st.builds(
    Hardware,
    manufacturer=
        safe_text,
    serialNo=
        safe_text
)
FastCard_strategy = st.builds(
    FastCard,
)
ExtensionBoard_strategy = st.builds(
    ExtensionBoard,
)
Vendor2Sound_strategy = st.builds(
    Vendor2Sound,
)
Vendor1Sound_strategy = st.builds(
    Vendor1Sound,
)
Vendor2Adapter_strategy = st.builds(
    Vendor2Adapter,
)
Vendor1Adapter_strategy = st.builds(
    Vendor1Adapter,
)
GenericSound_strategy = st.builds(
    GenericSound,
)
Sound_strategy = st.builds(
    Sound,
)
Card_strategy = st.builds(
    Card,
)
DeviceCard_strategy = st.builds(
    DeviceCard,
)
Memory_Interface_strategy = st.builds(
    Memory_Interface,
)
Instruction_strategy = st.builds(
    Instruction,
)
Program_strategy = st.builds(
    Program,
    name=
        safe_text
)
Machine_strategy = st.builds(
    Machine,
)
RAM_strategy = st.builds(
    RAM,
)
Cache_strategy = st.builds(
    Cache,
    chunck=
        safe_text
)
AcceleratorCard_strategy = st.builds(
    AcceleratorCard,
)
Processor_strategy = st.builds(
    Processor,
)
CPU_strategy = st.builds(
    CPU,
)

@given(instance=RAM1_strategy)
@settings(max_examples=50)
def test_ram1_instantiation(instance):
    assert isinstance(instance, RAM1)



@given(instance=RAM1_strategy)
def test_ram1_mb_setter(instance):
    original = instance.mb
    instance.mb = original
    assert instance.mb == original

@given(instance=CPU1_strategy)
@settings(max_examples=50)
def test_cpu1_instantiation(instance):
    assert isinstance(instance, CPU1)



@given(instance=CPU1_strategy)
def test_cpu1_mhz_setter(instance):
    original = instance.mhz
    instance.mhz = original
    assert instance.mhz == original

@given(instance=Hardware_strategy)
@settings(max_examples=50)
def test_hardware_instantiation(instance):
    assert isinstance(instance, Hardware)



@given(instance=Hardware_strategy)
def test_hardware_manufacturer_setter(instance):
    original = instance.manufacturer
    instance.manufacturer = original
    assert instance.manufacturer == original



@given(instance=Hardware_strategy)
def test_hardware_serialNo_setter(instance):
    original = instance.serialNo
    instance.serialNo = original
    assert instance.serialNo == original

@given(instance=FastCard_strategy)
@settings(max_examples=50)
def test_fastcard_instantiation(instance):
    assert isinstance(instance, FastCard)

@given(instance=ExtensionBoard_strategy)
@settings(max_examples=50)
def test_extensionboard_instantiation(instance):
    assert isinstance(instance, ExtensionBoard)

@given(instance=Vendor2Sound_strategy)
@settings(max_examples=50)
def test_vendor2sound_instantiation(instance):
    assert isinstance(instance, Vendor2Sound)

@given(instance=Vendor1Sound_strategy)
@settings(max_examples=50)
def test_vendor1sound_instantiation(instance):
    assert isinstance(instance, Vendor1Sound)

@given(instance=Vendor2Adapter_strategy)
@settings(max_examples=50)
def test_vendor2adapter_instantiation(instance):
    assert isinstance(instance, Vendor2Adapter)

@given(instance=Vendor1Adapter_strategy)
@settings(max_examples=50)
def test_vendor1adapter_instantiation(instance):
    assert isinstance(instance, Vendor1Adapter)

@given(instance=GenericSound_strategy)
@settings(max_examples=50)
def test_genericsound_instantiation(instance):
    assert isinstance(instance, GenericSound)

@given(instance=Sound_strategy)
@settings(max_examples=50)
def test_sound_instantiation(instance):
    assert isinstance(instance, Sound)

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)

@given(instance=DeviceCard_strategy)
@settings(max_examples=50)
def test_devicecard_instantiation(instance):
    assert isinstance(instance, DeviceCard)

@given(instance=Memory_Interface_strategy)
@settings(max_examples=50)
def test_memory_interface_instantiation(instance):
    assert isinstance(instance, Memory_Interface)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=Program_strategy)
@settings(max_examples=50)
def test_program_instantiation(instance):
    assert isinstance(instance, Program)



@given(instance=Program_strategy)
def test_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Machine_strategy)
@settings(max_examples=50)
def test_machine_instantiation(instance):
    assert isinstance(instance, Machine)

@given(instance=RAM_strategy)
@settings(max_examples=50)
def test_ram_instantiation(instance):
    assert isinstance(instance, RAM)

@given(instance=Cache_strategy)
@settings(max_examples=50)
def test_cache_instantiation(instance):
    assert isinstance(instance, Cache)



@given(instance=Cache_strategy)
def test_cache_chunck_setter(instance):
    original = instance.chunck
    instance.chunck = original
    assert instance.chunck == original

@given(instance=AcceleratorCard_strategy)
@settings(max_examples=50)
def test_acceleratorcard_instantiation(instance):
    assert isinstance(instance, AcceleratorCard)

@given(instance=Processor_strategy)
@settings(max_examples=50)
def test_processor_instantiation(instance):
    assert isinstance(instance, Processor)

@given(instance=CPU_strategy)
@settings(max_examples=50)
def test_cpu_instantiation(instance):
    assert isinstance(instance, CPU)
