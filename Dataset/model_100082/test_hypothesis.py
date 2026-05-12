import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ShellCmd,
    kbuild::Include,
    BuildEntry,
    kbuild::Ifndef,
    kbuild::Object,
    kbuild::IfNEq,
    kbuild::HostProgram,
    kbuild::IfEq,
    Value,
    kbuild::ObjectDir,
    kbuild::ObjectShellCmd,
    kbuild::ObjectShellChar,
    kbuild::ObjectSingleFile,
    kbuild::ObjectVariable,
    kbuild::ObjectString,
    kbuild::ObjectFile,
    Object::M,
    kbuild::Obj::m,
    Object::Y,
    kbuild::Obj::y,
    kbuild::MyVariable,
    kbuild::Target,
    kbuild::ShellCmd,
    kbuild::If,
    kbuild::AssignExtra,
    kbuild::Entry,
    kbuild::EObject,
    kbuild::BuildEntry,
    kbuild::VarSlashSym,
    kbuild::ShellPart,
    VarSlashSym,
    If,
    kbuild::Variable,
    kbuild::Value,
    Assign,
    kbuild::Values,
    AssignExtra,
    kbuild::Assign,
    kbuild::Object::M,
    kbuild::Object::Y,
    kbuild::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shellcmd_is_not_abstract():
    assert not inspect.isabstract(ShellCmd)


def test_shellcmd_constructor_exists():
    assert callable(ShellCmd.__init__)


def test_shellcmd_constructor_args():
    sig = inspect.signature(ShellCmd.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::include_is_not_abstract():
    assert not inspect.isabstract(kbuild::Include)


def test_kbuild::include_constructor_exists():
    assert callable(kbuild::Include.__init__)


def test_kbuild::include_constructor_args():
    sig = inspect.signature(kbuild::Include.__init__)
    params = list(sig.parameters.keys())



def test_buildentry_is_not_abstract():
    assert not inspect.isabstract(BuildEntry)


def test_buildentry_constructor_exists():
    assert callable(BuildEntry.__init__)


def test_buildentry_constructor_args():
    sig = inspect.signature(BuildEntry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::ifndef_is_not_abstract():
    assert not inspect.isabstract(kbuild::Ifndef)


def test_kbuild::ifndef_constructor_exists():
    assert callable(kbuild::Ifndef.__init__)


def test_kbuild::ifndef_constructor_args():
    sig = inspect.signature(kbuild::Ifndef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::ifndef_has_name():
    assert hasattr(kbuild::Ifndef, "name")
    descriptor = None
    for klass in kbuild::Ifndef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::object_is_not_abstract():
    assert not inspect.isabstract(kbuild::Object)


def test_kbuild::object_constructor_exists():
    assert callable(kbuild::Object.__init__)


def test_kbuild::object_constructor_args():
    sig = inspect.signature(kbuild::Object.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::ifneq_is_not_abstract():
    assert not inspect.isabstract(kbuild::IfNEq)


def test_kbuild::ifneq_constructor_exists():
    assert callable(kbuild::IfNEq.__init__)


def test_kbuild::ifneq_constructor_args():
    sig = inspect.signature(kbuild::IfNEq.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::hostprogram_is_not_abstract():
    assert not inspect.isabstract(kbuild::HostProgram)


def test_kbuild::hostprogram_constructor_exists():
    assert callable(kbuild::HostProgram.__init__)


def test_kbuild::hostprogram_constructor_args():
    sig = inspect.signature(kbuild::HostProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::hostprogram_has_name():
    assert hasattr(kbuild::HostProgram, "name")
    descriptor = None
    for klass in kbuild::HostProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::ifeq_is_not_abstract():
    assert not inspect.isabstract(kbuild::IfEq)


def test_kbuild::ifeq_constructor_exists():
    assert callable(kbuild::IfEq.__init__)


def test_kbuild::ifeq_constructor_args():
    sig = inspect.signature(kbuild::IfEq.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::objectdir_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectDir)


def test_kbuild::objectdir_constructor_exists():
    assert callable(kbuild::ObjectDir.__init__)


def test_kbuild::objectdir_constructor_args():
    sig = inspect.signature(kbuild::ObjectDir.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::objectshellcmd_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectShellCmd)


def test_kbuild::objectshellcmd_constructor_exists():
    assert callable(kbuild::ObjectShellCmd.__init__)


def test_kbuild::objectshellcmd_constructor_args():
    sig = inspect.signature(kbuild::ObjectShellCmd.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::objectshellchar_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectShellChar)


def test_kbuild::objectshellchar_constructor_exists():
    assert callable(kbuild::ObjectShellChar.__init__)


def test_kbuild::objectshellchar_constructor_args():
    sig = inspect.signature(kbuild::ObjectShellChar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kbuild::objectshellchar_has_value():
    assert hasattr(kbuild::ObjectShellChar, "value")
    descriptor = None
    for klass in kbuild::ObjectShellChar.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::objectsinglefile_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectSingleFile)


def test_kbuild::objectsinglefile_constructor_exists():
    assert callable(kbuild::ObjectSingleFile.__init__)


def test_kbuild::objectsinglefile_constructor_args():
    sig = inspect.signature(kbuild::ObjectSingleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::objectsinglefile_has_name():
    assert hasattr(kbuild::ObjectSingleFile, "name")
    descriptor = None
    for klass in kbuild::ObjectSingleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::objectvariable_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectVariable)


def test_kbuild::objectvariable_constructor_exists():
    assert callable(kbuild::ObjectVariable.__init__)


def test_kbuild::objectvariable_constructor_args():
    sig = inspect.signature(kbuild::ObjectVariable.__init__)
    params = list(sig.parameters.keys())
    assert "additional" in params, "Missing parameter 'additional'"

def test_kbuild::objectvariable_has_additional():
    assert hasattr(kbuild::ObjectVariable, "additional")
    descriptor = None
    for klass in kbuild::ObjectVariable.__mro__:
        if "additional" in klass.__dict__:
            descriptor = klass.__dict__["additional"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::objectstring_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectString)


def test_kbuild::objectstring_constructor_exists():
    assert callable(kbuild::ObjectString.__init__)


def test_kbuild::objectstring_constructor_args():
    sig = inspect.signature(kbuild::ObjectString.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::objectfile_is_not_abstract():
    assert not inspect.isabstract(kbuild::ObjectFile)


def test_kbuild::objectfile_constructor_exists():
    assert callable(kbuild::ObjectFile.__init__)


def test_kbuild::objectfile_constructor_args():
    sig = inspect.signature(kbuild::ObjectFile.__init__)
    params = list(sig.parameters.keys())



def test_object::m_is_not_abstract():
    assert not inspect.isabstract(Object::M)


def test_object::m_constructor_exists():
    assert callable(Object::M.__init__)


def test_object::m_constructor_args():
    sig = inspect.signature(Object::M.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::obj::m_is_not_abstract():
    assert not inspect.isabstract(kbuild::Obj::m)


def test_kbuild::obj::m_constructor_exists():
    assert callable(kbuild::Obj::m.__init__)


def test_kbuild::obj::m_constructor_args():
    sig = inspect.signature(kbuild::Obj::m.__init__)
    params = list(sig.parameters.keys())



def test_object::y_is_not_abstract():
    assert not inspect.isabstract(Object::Y)


def test_object::y_constructor_exists():
    assert callable(Object::Y.__init__)


def test_object::y_constructor_args():
    sig = inspect.signature(Object::Y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::obj::y_is_not_abstract():
    assert not inspect.isabstract(kbuild::Obj::y)


def test_kbuild::obj::y_constructor_exists():
    assert callable(kbuild::Obj::y.__init__)


def test_kbuild::obj::y_constructor_args():
    sig = inspect.signature(kbuild::Obj::y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::myvariable_is_not_abstract():
    assert not inspect.isabstract(kbuild::MyVariable)


def test_kbuild::myvariable_constructor_exists():
    assert callable(kbuild::MyVariable.__init__)


def test_kbuild::myvariable_constructor_args():
    sig = inspect.signature(kbuild::MyVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::myvariable_has_name():
    assert hasattr(kbuild::MyVariable, "name")
    descriptor = None
    for klass in kbuild::MyVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::target_is_not_abstract():
    assert not inspect.isabstract(kbuild::Target)


def test_kbuild::target_constructor_exists():
    assert callable(kbuild::Target.__init__)


def test_kbuild::target_constructor_args():
    sig = inspect.signature(kbuild::Target.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::shellcmd_is_not_abstract():
    assert not inspect.isabstract(kbuild::ShellCmd)


def test_kbuild::shellcmd_constructor_exists():
    assert callable(kbuild::ShellCmd.__init__)


def test_kbuild::shellcmd_constructor_args():
    sig = inspect.signature(kbuild::ShellCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::shellcmd_has_name():
    assert hasattr(kbuild::ShellCmd, "name")
    descriptor = None
    for klass in kbuild::ShellCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::if_is_not_abstract():
    assert not inspect.isabstract(kbuild::If)


def test_kbuild::if_constructor_exists():
    assert callable(kbuild::If.__init__)


def test_kbuild::if_constructor_args():
    sig = inspect.signature(kbuild::If.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::assignextra_is_not_abstract():
    assert not inspect.isabstract(kbuild::AssignExtra)


def test_kbuild::assignextra_constructor_exists():
    assert callable(kbuild::AssignExtra.__init__)


def test_kbuild::assignextra_constructor_args():
    sig = inspect.signature(kbuild::AssignExtra.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::entry_is_not_abstract():
    assert not inspect.isabstract(kbuild::Entry)


def test_kbuild::entry_constructor_exists():
    assert callable(kbuild::Entry.__init__)


def test_kbuild::entry_constructor_args():
    sig = inspect.signature(kbuild::Entry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::eobject_is_not_abstract():
    assert not inspect.isabstract(kbuild::EObject)


def test_kbuild::eobject_constructor_exists():
    assert callable(kbuild::EObject.__init__)


def test_kbuild::eobject_constructor_args():
    sig = inspect.signature(kbuild::EObject.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::buildentry_is_not_abstract():
    assert not inspect.isabstract(kbuild::BuildEntry)


def test_kbuild::buildentry_constructor_exists():
    assert callable(kbuild::BuildEntry.__init__)


def test_kbuild::buildentry_constructor_args():
    sig = inspect.signature(kbuild::BuildEntry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::varslashsym_is_not_abstract():
    assert not inspect.isabstract(kbuild::VarSlashSym)


def test_kbuild::varslashsym_constructor_exists():
    assert callable(kbuild::VarSlashSym.__init__)


def test_kbuild::varslashsym_constructor_args():
    sig = inspect.signature(kbuild::VarSlashSym.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild::varslashsym_has_name():
    assert hasattr(kbuild::VarSlashSym, "name")
    descriptor = None
    for klass in kbuild::VarSlashSym.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild::shellpart_is_not_abstract():
    assert not inspect.isabstract(kbuild::ShellPart)


def test_kbuild::shellpart_constructor_exists():
    assert callable(kbuild::ShellPart.__init__)


def test_kbuild::shellpart_constructor_args():
    sig = inspect.signature(kbuild::ShellPart.__init__)
    params = list(sig.parameters.keys())



def test_varslashsym_is_not_abstract():
    assert not inspect.isabstract(VarSlashSym)


def test_varslashsym_constructor_exists():
    assert callable(VarSlashSym.__init__)


def test_varslashsym_constructor_args():
    sig = inspect.signature(VarSlashSym.__init__)
    params = list(sig.parameters.keys())



def test_if_is_not_abstract():
    assert not inspect.isabstract(If)


def test_if_constructor_exists():
    assert callable(If.__init__)


def test_if_constructor_args():
    sig = inspect.signature(If.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::variable_is_not_abstract():
    assert not inspect.isabstract(kbuild::Variable)


def test_kbuild::variable_constructor_exists():
    assert callable(kbuild::Variable.__init__)


def test_kbuild::variable_constructor_args():
    sig = inspect.signature(kbuild::Variable.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::value_is_not_abstract():
    assert not inspect.isabstract(kbuild::Value)


def test_kbuild::value_constructor_exists():
    assert callable(kbuild::Value.__init__)


def test_kbuild::value_constructor_args():
    sig = inspect.signature(kbuild::Value.__init__)
    params = list(sig.parameters.keys())



def test_assign_is_not_abstract():
    assert not inspect.isabstract(Assign)


def test_assign_constructor_exists():
    assert callable(Assign.__init__)


def test_assign_constructor_args():
    sig = inspect.signature(Assign.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::values_is_not_abstract():
    assert not inspect.isabstract(kbuild::Values)


def test_kbuild::values_constructor_exists():
    assert callable(kbuild::Values.__init__)


def test_kbuild::values_constructor_args():
    sig = inspect.signature(kbuild::Values.__init__)
    params = list(sig.parameters.keys())



def test_assignextra_is_not_abstract():
    assert not inspect.isabstract(AssignExtra)


def test_assignextra_constructor_exists():
    assert callable(AssignExtra.__init__)


def test_assignextra_constructor_args():
    sig = inspect.signature(AssignExtra.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::assign_is_not_abstract():
    assert not inspect.isabstract(kbuild::Assign)


def test_kbuild::assign_constructor_exists():
    assert callable(kbuild::Assign.__init__)


def test_kbuild::assign_constructor_args():
    sig = inspect.signature(kbuild::Assign.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::object::m_is_not_abstract():
    assert not inspect.isabstract(kbuild::Object::M)


def test_kbuild::object::m_constructor_exists():
    assert callable(kbuild::Object::M.__init__)


def test_kbuild::object::m_constructor_args():
    sig = inspect.signature(kbuild::Object::M.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::object::y_is_not_abstract():
    assert not inspect.isabstract(kbuild::Object::Y)


def test_kbuild::object::y_constructor_exists():
    assert callable(kbuild::Object::Y.__init__)


def test_kbuild::object::y_constructor_args():
    sig = inspect.signature(kbuild::Object::Y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild::model_is_not_abstract():
    assert not inspect.isabstract(kbuild::Model)


def test_kbuild::model_constructor_exists():
    assert callable(kbuild::Model.__init__)


def test_kbuild::model_constructor_args():
    sig = inspect.signature(kbuild::Model.__init__)
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
ShellCmd_strategy = st.builds(
    ShellCmd,
)
kbuild::Include_strategy = st.builds(
    kbuild::Include,
)
BuildEntry_strategy = st.builds(
    BuildEntry,
)
kbuild::Ifndef_strategy = st.builds(
    kbuild::Ifndef,
    name=
        safe_text
)
kbuild::Object_strategy = st.builds(
    kbuild::Object,
)
kbuild::IfNEq_strategy = st.builds(
    kbuild::IfNEq,
)
kbuild::HostProgram_strategy = st.builds(
    kbuild::HostProgram,
    name=
        safe_text
)
kbuild::IfEq_strategy = st.builds(
    kbuild::IfEq,
)
Value_strategy = st.builds(
    Value,
)
kbuild::ObjectDir_strategy = st.builds(
    kbuild::ObjectDir,
)
kbuild::ObjectShellCmd_strategy = st.builds(
    kbuild::ObjectShellCmd,
)
kbuild::ObjectShellChar_strategy = st.builds(
    kbuild::ObjectShellChar,
    value=
        safe_text
)
kbuild::ObjectSingleFile_strategy = st.builds(
    kbuild::ObjectSingleFile,
    name=
        safe_text
)
kbuild::ObjectVariable_strategy = st.builds(
    kbuild::ObjectVariable,
    additional=
        safe_text
)
kbuild::ObjectString_strategy = st.builds(
    kbuild::ObjectString,
)
kbuild::ObjectFile_strategy = st.builds(
    kbuild::ObjectFile,
)
Object::M_strategy = st.builds(
    Object::M,
)
kbuild::Obj::m_strategy = st.builds(
    kbuild::Obj::m,
)
Object::Y_strategy = st.builds(
    Object::Y,
)
kbuild::Obj::y_strategy = st.builds(
    kbuild::Obj::y,
)
kbuild::MyVariable_strategy = st.builds(
    kbuild::MyVariable,
    name=
        safe_text
)
kbuild::Target_strategy = st.builds(
    kbuild::Target,
)
kbuild::ShellCmd_strategy = st.builds(
    kbuild::ShellCmd,
    name=
        safe_text
)
kbuild::If_strategy = st.builds(
    kbuild::If,
)
kbuild::AssignExtra_strategy = st.builds(
    kbuild::AssignExtra,
)
kbuild::Entry_strategy = st.builds(
    kbuild::Entry,
)
kbuild::EObject_strategy = st.builds(
    kbuild::EObject,
)
kbuild::BuildEntry_strategy = st.builds(
    kbuild::BuildEntry,
)
kbuild::VarSlashSym_strategy = st.builds(
    kbuild::VarSlashSym,
    name=
        safe_text
)
kbuild::ShellPart_strategy = st.builds(
    kbuild::ShellPart,
)
VarSlashSym_strategy = st.builds(
    VarSlashSym,
)
If_strategy = st.builds(
    If,
)
kbuild::Variable_strategy = st.builds(
    kbuild::Variable,
)
kbuild::Value_strategy = st.builds(
    kbuild::Value,
)
Assign_strategy = st.builds(
    Assign,
)
kbuild::Values_strategy = st.builds(
    kbuild::Values,
)
AssignExtra_strategy = st.builds(
    AssignExtra,
)
kbuild::Assign_strategy = st.builds(
    kbuild::Assign,
)
kbuild::Object::M_strategy = st.builds(
    kbuild::Object::M,
)
kbuild::Object::Y_strategy = st.builds(
    kbuild::Object::Y,
)
kbuild::Model_strategy = st.builds(
    kbuild::Model,
)

@given(instance=ShellCmd_strategy)
@settings(max_examples=50)
def test_shellcmd_instantiation(instance):
    assert isinstance(instance, ShellCmd)

@given(instance=kbuild::Include_strategy)
@settings(max_examples=50)
def test_kbuild::include_instantiation(instance):
    assert isinstance(instance, kbuild::Include)

@given(instance=BuildEntry_strategy)
@settings(max_examples=50)
def test_buildentry_instantiation(instance):
    assert isinstance(instance, BuildEntry)

@given(instance=kbuild::Ifndef_strategy)
@settings(max_examples=50)
def test_kbuild::ifndef_instantiation(instance):
    assert isinstance(instance, kbuild::Ifndef)

@given(instance=kbuild::Ifndef_strategy)
def test_kbuild::ifndef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::Ifndef_strategy)
def test_kbuild::ifndef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::Object_strategy)
@settings(max_examples=50)
def test_kbuild::object_instantiation(instance):
    assert isinstance(instance, kbuild::Object)

@given(instance=kbuild::IfNEq_strategy)
@settings(max_examples=50)
def test_kbuild::ifneq_instantiation(instance):
    assert isinstance(instance, kbuild::IfNEq)

@given(instance=kbuild::HostProgram_strategy)
@settings(max_examples=50)
def test_kbuild::hostprogram_instantiation(instance):
    assert isinstance(instance, kbuild::HostProgram)

@given(instance=kbuild::HostProgram_strategy)
def test_kbuild::hostprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::HostProgram_strategy)
def test_kbuild::hostprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::IfEq_strategy)
@settings(max_examples=50)
def test_kbuild::ifeq_instantiation(instance):
    assert isinstance(instance, kbuild::IfEq)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=kbuild::ObjectDir_strategy)
@settings(max_examples=50)
def test_kbuild::objectdir_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectDir)

@given(instance=kbuild::ObjectShellCmd_strategy)
@settings(max_examples=50)
def test_kbuild::objectshellcmd_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectShellCmd)

@given(instance=kbuild::ObjectShellChar_strategy)
@settings(max_examples=50)
def test_kbuild::objectshellchar_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectShellChar)

@given(instance=kbuild::ObjectShellChar_strategy)
def test_kbuild::objectshellchar_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=kbuild::ObjectShellChar_strategy)
def test_kbuild::objectshellchar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kbuild::ObjectSingleFile_strategy)
@settings(max_examples=50)
def test_kbuild::objectsinglefile_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectSingleFile)

@given(instance=kbuild::ObjectSingleFile_strategy)
def test_kbuild::objectsinglefile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::ObjectSingleFile_strategy)
def test_kbuild::objectsinglefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::ObjectVariable_strategy)
@settings(max_examples=50)
def test_kbuild::objectvariable_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectVariable)

@given(instance=kbuild::ObjectVariable_strategy)
def test_kbuild::objectvariable_additional_type(instance):
    assert isinstance(instance.additional, str)


@given(instance=kbuild::ObjectVariable_strategy)
def test_kbuild::objectvariable_additional_setter(instance):
    original = instance.additional
    instance.additional = original
    assert instance.additional == original

@given(instance=kbuild::ObjectString_strategy)
@settings(max_examples=50)
def test_kbuild::objectstring_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectString)

@given(instance=kbuild::ObjectFile_strategy)
@settings(max_examples=50)
def test_kbuild::objectfile_instantiation(instance):
    assert isinstance(instance, kbuild::ObjectFile)

@given(instance=Object::M_strategy)
@settings(max_examples=50)
def test_object::m_instantiation(instance):
    assert isinstance(instance, Object::M)

@given(instance=kbuild::Obj::m_strategy)
@settings(max_examples=50)
def test_kbuild::obj::m_instantiation(instance):
    assert isinstance(instance, kbuild::Obj::m)

@given(instance=Object::Y_strategy)
@settings(max_examples=50)
def test_object::y_instantiation(instance):
    assert isinstance(instance, Object::Y)

@given(instance=kbuild::Obj::y_strategy)
@settings(max_examples=50)
def test_kbuild::obj::y_instantiation(instance):
    assert isinstance(instance, kbuild::Obj::y)

@given(instance=kbuild::MyVariable_strategy)
@settings(max_examples=50)
def test_kbuild::myvariable_instantiation(instance):
    assert isinstance(instance, kbuild::MyVariable)

@given(instance=kbuild::MyVariable_strategy)
def test_kbuild::myvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::MyVariable_strategy)
def test_kbuild::myvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::Target_strategy)
@settings(max_examples=50)
def test_kbuild::target_instantiation(instance):
    assert isinstance(instance, kbuild::Target)

@given(instance=kbuild::ShellCmd_strategy)
@settings(max_examples=50)
def test_kbuild::shellcmd_instantiation(instance):
    assert isinstance(instance, kbuild::ShellCmd)

@given(instance=kbuild::ShellCmd_strategy)
def test_kbuild::shellcmd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::ShellCmd_strategy)
def test_kbuild::shellcmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::If_strategy)
@settings(max_examples=50)
def test_kbuild::if_instantiation(instance):
    assert isinstance(instance, kbuild::If)

@given(instance=kbuild::AssignExtra_strategy)
@settings(max_examples=50)
def test_kbuild::assignextra_instantiation(instance):
    assert isinstance(instance, kbuild::AssignExtra)

@given(instance=kbuild::Entry_strategy)
@settings(max_examples=50)
def test_kbuild::entry_instantiation(instance):
    assert isinstance(instance, kbuild::Entry)

@given(instance=kbuild::EObject_strategy)
@settings(max_examples=50)
def test_kbuild::eobject_instantiation(instance):
    assert isinstance(instance, kbuild::EObject)

@given(instance=kbuild::BuildEntry_strategy)
@settings(max_examples=50)
def test_kbuild::buildentry_instantiation(instance):
    assert isinstance(instance, kbuild::BuildEntry)

@given(instance=kbuild::VarSlashSym_strategy)
@settings(max_examples=50)
def test_kbuild::varslashsym_instantiation(instance):
    assert isinstance(instance, kbuild::VarSlashSym)

@given(instance=kbuild::VarSlashSym_strategy)
def test_kbuild::varslashsym_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kbuild::VarSlashSym_strategy)
def test_kbuild::varslashsym_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild::ShellPart_strategy)
@settings(max_examples=50)
def test_kbuild::shellpart_instantiation(instance):
    assert isinstance(instance, kbuild::ShellPart)

@given(instance=VarSlashSym_strategy)
@settings(max_examples=50)
def test_varslashsym_instantiation(instance):
    assert isinstance(instance, VarSlashSym)

@given(instance=If_strategy)
@settings(max_examples=50)
def test_if_instantiation(instance):
    assert isinstance(instance, If)

@given(instance=kbuild::Variable_strategy)
@settings(max_examples=50)
def test_kbuild::variable_instantiation(instance):
    assert isinstance(instance, kbuild::Variable)

@given(instance=kbuild::Value_strategy)
@settings(max_examples=50)
def test_kbuild::value_instantiation(instance):
    assert isinstance(instance, kbuild::Value)

@given(instance=Assign_strategy)
@settings(max_examples=50)
def test_assign_instantiation(instance):
    assert isinstance(instance, Assign)

@given(instance=kbuild::Values_strategy)
@settings(max_examples=50)
def test_kbuild::values_instantiation(instance):
    assert isinstance(instance, kbuild::Values)

@given(instance=AssignExtra_strategy)
@settings(max_examples=50)
def test_assignextra_instantiation(instance):
    assert isinstance(instance, AssignExtra)

@given(instance=kbuild::Assign_strategy)
@settings(max_examples=50)
def test_kbuild::assign_instantiation(instance):
    assert isinstance(instance, kbuild::Assign)

@given(instance=kbuild::Object::M_strategy)
@settings(max_examples=50)
def test_kbuild::object::m_instantiation(instance):
    assert isinstance(instance, kbuild::Object::M)

@given(instance=kbuild::Object::Y_strategy)
@settings(max_examples=50)
def test_kbuild::object::y_instantiation(instance):
    assert isinstance(instance, kbuild::Object::Y)

@given(instance=kbuild::Model_strategy)
@settings(max_examples=50)
def test_kbuild::model_instantiation(instance):
    assert isinstance(instance, kbuild::Model)
