import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ShellCmd,
    kbuild_Include,
    BuildEntry,
    kbuild_HostProgram,
    kbuild_Ifndef,
    kbuild_Object,
    kbuild_IfNEq,
    kbuild_IfEq,
    Value,
    kbuild_ObjectSingleFile,
    kbuild_ObjectVariable,
    kbuild_ObjectShellChar,
    kbuild_ObjectString,
    kbuild_ObjectDir,
    kbuild_ObjectShellCmd,
    kbuild_ObjectFile,
    Object_M,
    kbuild_Obj_m,
    Object_Y,
    kbuild_Obj_y,
    kbuild_MyVariable,
    kbuild_Target,
    kbuild_ShellCmd,
    kbuild_If,
    kbuild_AssignExtra,
    kbuild_Entry,
    kbuild_EObject,
    kbuild_BuildEntry,
    kbuild_VarSlashSym,
    kbuild_ShellPart,
    VarSlashSym,
    If,
    kbuild_Variable,
    kbuild_Value,
    Assign,
    kbuild_Values,
    AssignExtra,
    kbuild_Assign,
    kbuild_Object_M,
    kbuild_Object_Y,
    kbuild_Model,
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



def test_kbuild_include_is_not_abstract():
    assert not inspect.isabstract(kbuild_Include)


def test_kbuild_include_constructor_exists():
    assert callable(kbuild_Include.__init__)


def test_kbuild_include_constructor_args():
    sig = inspect.signature(kbuild_Include.__init__)
    params = list(sig.parameters.keys())



def test_buildentry_is_not_abstract():
    assert not inspect.isabstract(BuildEntry)


def test_buildentry_constructor_exists():
    assert callable(BuildEntry.__init__)


def test_buildentry_constructor_args():
    sig = inspect.signature(BuildEntry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_hostprogram_is_not_abstract():
    assert not inspect.isabstract(kbuild_HostProgram)


def test_kbuild_hostprogram_constructor_exists():
    assert callable(kbuild_HostProgram.__init__)


def test_kbuild_hostprogram_constructor_args():
    sig = inspect.signature(kbuild_HostProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_hostprogram_has_name():
    assert hasattr(kbuild_HostProgram, "name")
    descriptor = None
    for klass in kbuild_HostProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_ifndef_is_not_abstract():
    assert not inspect.isabstract(kbuild_Ifndef)


def test_kbuild_ifndef_constructor_exists():
    assert callable(kbuild_Ifndef.__init__)


def test_kbuild_ifndef_constructor_args():
    sig = inspect.signature(kbuild_Ifndef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_ifndef_has_name():
    assert hasattr(kbuild_Ifndef, "name")
    descriptor = None
    for klass in kbuild_Ifndef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_object_is_not_abstract():
    assert not inspect.isabstract(kbuild_Object)


def test_kbuild_object_constructor_exists():
    assert callable(kbuild_Object.__init__)


def test_kbuild_object_constructor_args():
    sig = inspect.signature(kbuild_Object.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_ifneq_is_not_abstract():
    assert not inspect.isabstract(kbuild_IfNEq)


def test_kbuild_ifneq_constructor_exists():
    assert callable(kbuild_IfNEq.__init__)


def test_kbuild_ifneq_constructor_args():
    sig = inspect.signature(kbuild_IfNEq.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_ifeq_is_not_abstract():
    assert not inspect.isabstract(kbuild_IfEq)


def test_kbuild_ifeq_constructor_exists():
    assert callable(kbuild_IfEq.__init__)


def test_kbuild_ifeq_constructor_args():
    sig = inspect.signature(kbuild_IfEq.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_objectsinglefile_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectSingleFile)


def test_kbuild_objectsinglefile_constructor_exists():
    assert callable(kbuild_ObjectSingleFile.__init__)


def test_kbuild_objectsinglefile_constructor_args():
    sig = inspect.signature(kbuild_ObjectSingleFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_objectsinglefile_has_name():
    assert hasattr(kbuild_ObjectSingleFile, "name")
    descriptor = None
    for klass in kbuild_ObjectSingleFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_objectvariable_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectVariable)


def test_kbuild_objectvariable_constructor_exists():
    assert callable(kbuild_ObjectVariable.__init__)


def test_kbuild_objectvariable_constructor_args():
    sig = inspect.signature(kbuild_ObjectVariable.__init__)
    params = list(sig.parameters.keys())
    assert "additional" in params, "Missing parameter 'additional'"

def test_kbuild_objectvariable_has_additional():
    assert hasattr(kbuild_ObjectVariable, "additional")
    descriptor = None
    for klass in kbuild_ObjectVariable.__mro__:
        if "additional" in klass.__dict__:
            descriptor = klass.__dict__["additional"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_objectshellchar_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectShellChar)


def test_kbuild_objectshellchar_constructor_exists():
    assert callable(kbuild_ObjectShellChar.__init__)


def test_kbuild_objectshellchar_constructor_args():
    sig = inspect.signature(kbuild_ObjectShellChar.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_kbuild_objectshellchar_has_value():
    assert hasattr(kbuild_ObjectShellChar, "value")
    descriptor = None
    for klass in kbuild_ObjectShellChar.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_objectstring_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectString)


def test_kbuild_objectstring_constructor_exists():
    assert callable(kbuild_ObjectString.__init__)


def test_kbuild_objectstring_constructor_args():
    sig = inspect.signature(kbuild_ObjectString.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_objectdir_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectDir)


def test_kbuild_objectdir_constructor_exists():
    assert callable(kbuild_ObjectDir.__init__)


def test_kbuild_objectdir_constructor_args():
    sig = inspect.signature(kbuild_ObjectDir.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_objectshellcmd_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectShellCmd)


def test_kbuild_objectshellcmd_constructor_exists():
    assert callable(kbuild_ObjectShellCmd.__init__)


def test_kbuild_objectshellcmd_constructor_args():
    sig = inspect.signature(kbuild_ObjectShellCmd.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_objectfile_is_not_abstract():
    assert not inspect.isabstract(kbuild_ObjectFile)


def test_kbuild_objectfile_constructor_exists():
    assert callable(kbuild_ObjectFile.__init__)


def test_kbuild_objectfile_constructor_args():
    sig = inspect.signature(kbuild_ObjectFile.__init__)
    params = list(sig.parameters.keys())



def test_object_m_is_not_abstract():
    assert not inspect.isabstract(Object_M)


def test_object_m_constructor_exists():
    assert callable(Object_M.__init__)


def test_object_m_constructor_args():
    sig = inspect.signature(Object_M.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_obj_m_is_not_abstract():
    assert not inspect.isabstract(kbuild_Obj_m)


def test_kbuild_obj_m_constructor_exists():
    assert callable(kbuild_Obj_m.__init__)


def test_kbuild_obj_m_constructor_args():
    sig = inspect.signature(kbuild_Obj_m.__init__)
    params = list(sig.parameters.keys())



def test_object_y_is_not_abstract():
    assert not inspect.isabstract(Object_Y)


def test_object_y_constructor_exists():
    assert callable(Object_Y.__init__)


def test_object_y_constructor_args():
    sig = inspect.signature(Object_Y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_obj_y_is_not_abstract():
    assert not inspect.isabstract(kbuild_Obj_y)


def test_kbuild_obj_y_constructor_exists():
    assert callable(kbuild_Obj_y.__init__)


def test_kbuild_obj_y_constructor_args():
    sig = inspect.signature(kbuild_Obj_y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_myvariable_is_not_abstract():
    assert not inspect.isabstract(kbuild_MyVariable)


def test_kbuild_myvariable_constructor_exists():
    assert callable(kbuild_MyVariable.__init__)


def test_kbuild_myvariable_constructor_args():
    sig = inspect.signature(kbuild_MyVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_myvariable_has_name():
    assert hasattr(kbuild_MyVariable, "name")
    descriptor = None
    for klass in kbuild_MyVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_target_is_not_abstract():
    assert not inspect.isabstract(kbuild_Target)


def test_kbuild_target_constructor_exists():
    assert callable(kbuild_Target.__init__)


def test_kbuild_target_constructor_args():
    sig = inspect.signature(kbuild_Target.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_shellcmd_is_not_abstract():
    assert not inspect.isabstract(kbuild_ShellCmd)


def test_kbuild_shellcmd_constructor_exists():
    assert callable(kbuild_ShellCmd.__init__)


def test_kbuild_shellcmd_constructor_args():
    sig = inspect.signature(kbuild_ShellCmd.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_shellcmd_has_name():
    assert hasattr(kbuild_ShellCmd, "name")
    descriptor = None
    for klass in kbuild_ShellCmd.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_if_is_not_abstract():
    assert not inspect.isabstract(kbuild_If)


def test_kbuild_if_constructor_exists():
    assert callable(kbuild_If.__init__)


def test_kbuild_if_constructor_args():
    sig = inspect.signature(kbuild_If.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_assignextra_is_not_abstract():
    assert not inspect.isabstract(kbuild_AssignExtra)


def test_kbuild_assignextra_constructor_exists():
    assert callable(kbuild_AssignExtra.__init__)


def test_kbuild_assignextra_constructor_args():
    sig = inspect.signature(kbuild_AssignExtra.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_entry_is_not_abstract():
    assert not inspect.isabstract(kbuild_Entry)


def test_kbuild_entry_constructor_exists():
    assert callable(kbuild_Entry.__init__)


def test_kbuild_entry_constructor_args():
    sig = inspect.signature(kbuild_Entry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_eobject_is_not_abstract():
    assert not inspect.isabstract(kbuild_EObject)


def test_kbuild_eobject_constructor_exists():
    assert callable(kbuild_EObject.__init__)


def test_kbuild_eobject_constructor_args():
    sig = inspect.signature(kbuild_EObject.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_buildentry_is_not_abstract():
    assert not inspect.isabstract(kbuild_BuildEntry)


def test_kbuild_buildentry_constructor_exists():
    assert callable(kbuild_BuildEntry.__init__)


def test_kbuild_buildentry_constructor_args():
    sig = inspect.signature(kbuild_BuildEntry.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_varslashsym_is_not_abstract():
    assert not inspect.isabstract(kbuild_VarSlashSym)


def test_kbuild_varslashsym_constructor_exists():
    assert callable(kbuild_VarSlashSym.__init__)


def test_kbuild_varslashsym_constructor_args():
    sig = inspect.signature(kbuild_VarSlashSym.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kbuild_varslashsym_has_name():
    assert hasattr(kbuild_VarSlashSym, "name")
    descriptor = None
    for klass in kbuild_VarSlashSym.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kbuild_shellpart_is_not_abstract():
    assert not inspect.isabstract(kbuild_ShellPart)


def test_kbuild_shellpart_constructor_exists():
    assert callable(kbuild_ShellPart.__init__)


def test_kbuild_shellpart_constructor_args():
    sig = inspect.signature(kbuild_ShellPart.__init__)
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



def test_kbuild_variable_is_not_abstract():
    assert not inspect.isabstract(kbuild_Variable)


def test_kbuild_variable_constructor_exists():
    assert callable(kbuild_Variable.__init__)


def test_kbuild_variable_constructor_args():
    sig = inspect.signature(kbuild_Variable.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_value_is_not_abstract():
    assert not inspect.isabstract(kbuild_Value)


def test_kbuild_value_constructor_exists():
    assert callable(kbuild_Value.__init__)


def test_kbuild_value_constructor_args():
    sig = inspect.signature(kbuild_Value.__init__)
    params = list(sig.parameters.keys())



def test_assign_is_not_abstract():
    assert not inspect.isabstract(Assign)


def test_assign_constructor_exists():
    assert callable(Assign.__init__)


def test_assign_constructor_args():
    sig = inspect.signature(Assign.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_values_is_not_abstract():
    assert not inspect.isabstract(kbuild_Values)


def test_kbuild_values_constructor_exists():
    assert callable(kbuild_Values.__init__)


def test_kbuild_values_constructor_args():
    sig = inspect.signature(kbuild_Values.__init__)
    params = list(sig.parameters.keys())



def test_assignextra_is_not_abstract():
    assert not inspect.isabstract(AssignExtra)


def test_assignextra_constructor_exists():
    assert callable(AssignExtra.__init__)


def test_assignextra_constructor_args():
    sig = inspect.signature(AssignExtra.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_assign_is_not_abstract():
    assert not inspect.isabstract(kbuild_Assign)


def test_kbuild_assign_constructor_exists():
    assert callable(kbuild_Assign.__init__)


def test_kbuild_assign_constructor_args():
    sig = inspect.signature(kbuild_Assign.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_object_m_is_not_abstract():
    assert not inspect.isabstract(kbuild_Object_M)


def test_kbuild_object_m_constructor_exists():
    assert callable(kbuild_Object_M.__init__)


def test_kbuild_object_m_constructor_args():
    sig = inspect.signature(kbuild_Object_M.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_object_y_is_not_abstract():
    assert not inspect.isabstract(kbuild_Object_Y)


def test_kbuild_object_y_constructor_exists():
    assert callable(kbuild_Object_Y.__init__)


def test_kbuild_object_y_constructor_args():
    sig = inspect.signature(kbuild_Object_Y.__init__)
    params = list(sig.parameters.keys())



def test_kbuild_model_is_not_abstract():
    assert not inspect.isabstract(kbuild_Model)


def test_kbuild_model_constructor_exists():
    assert callable(kbuild_Model.__init__)


def test_kbuild_model_constructor_args():
    sig = inspect.signature(kbuild_Model.__init__)
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
kbuild_Include_strategy = st.builds(
    kbuild_Include,
)
BuildEntry_strategy = st.builds(
    BuildEntry,
)
kbuild_HostProgram_strategy = st.builds(
    kbuild_HostProgram,
    name=
        safe_text
)
kbuild_Ifndef_strategy = st.builds(
    kbuild_Ifndef,
    name=
        safe_text
)
kbuild_Object_strategy = st.builds(
    kbuild_Object,
)
kbuild_IfNEq_strategy = st.builds(
    kbuild_IfNEq,
)
kbuild_IfEq_strategy = st.builds(
    kbuild_IfEq,
)
Value_strategy = st.builds(
    Value,
)
kbuild_ObjectSingleFile_strategy = st.builds(
    kbuild_ObjectSingleFile,
    name=
        safe_text
)
kbuild_ObjectVariable_strategy = st.builds(
    kbuild_ObjectVariable,
    additional=
        safe_text
)
kbuild_ObjectShellChar_strategy = st.builds(
    kbuild_ObjectShellChar,
    value=
        safe_text
)
kbuild_ObjectString_strategy = st.builds(
    kbuild_ObjectString,
)
kbuild_ObjectDir_strategy = st.builds(
    kbuild_ObjectDir,
)
kbuild_ObjectShellCmd_strategy = st.builds(
    kbuild_ObjectShellCmd,
)
kbuild_ObjectFile_strategy = st.builds(
    kbuild_ObjectFile,
)
Object_M_strategy = st.builds(
    Object_M,
)
kbuild_Obj_m_strategy = st.builds(
    kbuild_Obj_m,
)
Object_Y_strategy = st.builds(
    Object_Y,
)
kbuild_Obj_y_strategy = st.builds(
    kbuild_Obj_y,
)
kbuild_MyVariable_strategy = st.builds(
    kbuild_MyVariable,
    name=
        safe_text
)
kbuild_Target_strategy = st.builds(
    kbuild_Target,
)
kbuild_ShellCmd_strategy = st.builds(
    kbuild_ShellCmd,
    name=
        safe_text
)
kbuild_If_strategy = st.builds(
    kbuild_If,
)
kbuild_AssignExtra_strategy = st.builds(
    kbuild_AssignExtra,
)
kbuild_Entry_strategy = st.builds(
    kbuild_Entry,
)
kbuild_EObject_strategy = st.builds(
    kbuild_EObject,
)
kbuild_BuildEntry_strategy = st.builds(
    kbuild_BuildEntry,
)
kbuild_VarSlashSym_strategy = st.builds(
    kbuild_VarSlashSym,
    name=
        safe_text
)
kbuild_ShellPart_strategy = st.builds(
    kbuild_ShellPart,
)
VarSlashSym_strategy = st.builds(
    VarSlashSym,
)
If_strategy = st.builds(
    If,
)
kbuild_Variable_strategy = st.builds(
    kbuild_Variable,
)
kbuild_Value_strategy = st.builds(
    kbuild_Value,
)
Assign_strategy = st.builds(
    Assign,
)
kbuild_Values_strategy = st.builds(
    kbuild_Values,
)
AssignExtra_strategy = st.builds(
    AssignExtra,
)
kbuild_Assign_strategy = st.builds(
    kbuild_Assign,
)
kbuild_Object_M_strategy = st.builds(
    kbuild_Object_M,
)
kbuild_Object_Y_strategy = st.builds(
    kbuild_Object_Y,
)
kbuild_Model_strategy = st.builds(
    kbuild_Model,
)

@given(instance=ShellCmd_strategy)
@settings(max_examples=50)
def test_shellcmd_instantiation(instance):
    assert isinstance(instance, ShellCmd)

@given(instance=kbuild_Include_strategy)
@settings(max_examples=50)
def test_kbuild_include_instantiation(instance):
    assert isinstance(instance, kbuild_Include)

@given(instance=BuildEntry_strategy)
@settings(max_examples=50)
def test_buildentry_instantiation(instance):
    assert isinstance(instance, BuildEntry)

@given(instance=kbuild_HostProgram_strategy)
@settings(max_examples=50)
def test_kbuild_hostprogram_instantiation(instance):
    assert isinstance(instance, kbuild_HostProgram)



@given(instance=kbuild_HostProgram_strategy)
def test_kbuild_hostprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_Ifndef_strategy)
@settings(max_examples=50)
def test_kbuild_ifndef_instantiation(instance):
    assert isinstance(instance, kbuild_Ifndef)



@given(instance=kbuild_Ifndef_strategy)
def test_kbuild_ifndef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_Object_strategy)
@settings(max_examples=50)
def test_kbuild_object_instantiation(instance):
    assert isinstance(instance, kbuild_Object)

@given(instance=kbuild_IfNEq_strategy)
@settings(max_examples=50)
def test_kbuild_ifneq_instantiation(instance):
    assert isinstance(instance, kbuild_IfNEq)

@given(instance=kbuild_IfEq_strategy)
@settings(max_examples=50)
def test_kbuild_ifeq_instantiation(instance):
    assert isinstance(instance, kbuild_IfEq)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=kbuild_ObjectSingleFile_strategy)
@settings(max_examples=50)
def test_kbuild_objectsinglefile_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectSingleFile)



@given(instance=kbuild_ObjectSingleFile_strategy)
def test_kbuild_objectsinglefile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_ObjectVariable_strategy)
@settings(max_examples=50)
def test_kbuild_objectvariable_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectVariable)



@given(instance=kbuild_ObjectVariable_strategy)
def test_kbuild_objectvariable_additional_setter(instance):
    original = instance.additional
    instance.additional = original
    assert instance.additional == original

@given(instance=kbuild_ObjectShellChar_strategy)
@settings(max_examples=50)
def test_kbuild_objectshellchar_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectShellChar)



@given(instance=kbuild_ObjectShellChar_strategy)
def test_kbuild_objectshellchar_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=kbuild_ObjectString_strategy)
@settings(max_examples=50)
def test_kbuild_objectstring_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectString)

@given(instance=kbuild_ObjectDir_strategy)
@settings(max_examples=50)
def test_kbuild_objectdir_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectDir)

@given(instance=kbuild_ObjectShellCmd_strategy)
@settings(max_examples=50)
def test_kbuild_objectshellcmd_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectShellCmd)

@given(instance=kbuild_ObjectFile_strategy)
@settings(max_examples=50)
def test_kbuild_objectfile_instantiation(instance):
    assert isinstance(instance, kbuild_ObjectFile)

@given(instance=Object_M_strategy)
@settings(max_examples=50)
def test_object_m_instantiation(instance):
    assert isinstance(instance, Object_M)

@given(instance=kbuild_Obj_m_strategy)
@settings(max_examples=50)
def test_kbuild_obj_m_instantiation(instance):
    assert isinstance(instance, kbuild_Obj_m)

@given(instance=Object_Y_strategy)
@settings(max_examples=50)
def test_object_y_instantiation(instance):
    assert isinstance(instance, Object_Y)

@given(instance=kbuild_Obj_y_strategy)
@settings(max_examples=50)
def test_kbuild_obj_y_instantiation(instance):
    assert isinstance(instance, kbuild_Obj_y)

@given(instance=kbuild_MyVariable_strategy)
@settings(max_examples=50)
def test_kbuild_myvariable_instantiation(instance):
    assert isinstance(instance, kbuild_MyVariable)



@given(instance=kbuild_MyVariable_strategy)
def test_kbuild_myvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_Target_strategy)
@settings(max_examples=50)
def test_kbuild_target_instantiation(instance):
    assert isinstance(instance, kbuild_Target)

@given(instance=kbuild_ShellCmd_strategy)
@settings(max_examples=50)
def test_kbuild_shellcmd_instantiation(instance):
    assert isinstance(instance, kbuild_ShellCmd)



@given(instance=kbuild_ShellCmd_strategy)
def test_kbuild_shellcmd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_If_strategy)
@settings(max_examples=50)
def test_kbuild_if_instantiation(instance):
    assert isinstance(instance, kbuild_If)

@given(instance=kbuild_AssignExtra_strategy)
@settings(max_examples=50)
def test_kbuild_assignextra_instantiation(instance):
    assert isinstance(instance, kbuild_AssignExtra)

@given(instance=kbuild_Entry_strategy)
@settings(max_examples=50)
def test_kbuild_entry_instantiation(instance):
    assert isinstance(instance, kbuild_Entry)

@given(instance=kbuild_EObject_strategy)
@settings(max_examples=50)
def test_kbuild_eobject_instantiation(instance):
    assert isinstance(instance, kbuild_EObject)

@given(instance=kbuild_BuildEntry_strategy)
@settings(max_examples=50)
def test_kbuild_buildentry_instantiation(instance):
    assert isinstance(instance, kbuild_BuildEntry)

@given(instance=kbuild_VarSlashSym_strategy)
@settings(max_examples=50)
def test_kbuild_varslashsym_instantiation(instance):
    assert isinstance(instance, kbuild_VarSlashSym)



@given(instance=kbuild_VarSlashSym_strategy)
def test_kbuild_varslashsym_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kbuild_ShellPart_strategy)
@settings(max_examples=50)
def test_kbuild_shellpart_instantiation(instance):
    assert isinstance(instance, kbuild_ShellPart)

@given(instance=VarSlashSym_strategy)
@settings(max_examples=50)
def test_varslashsym_instantiation(instance):
    assert isinstance(instance, VarSlashSym)

@given(instance=If_strategy)
@settings(max_examples=50)
def test_if_instantiation(instance):
    assert isinstance(instance, If)

@given(instance=kbuild_Variable_strategy)
@settings(max_examples=50)
def test_kbuild_variable_instantiation(instance):
    assert isinstance(instance, kbuild_Variable)

@given(instance=kbuild_Value_strategy)
@settings(max_examples=50)
def test_kbuild_value_instantiation(instance):
    assert isinstance(instance, kbuild_Value)

@given(instance=Assign_strategy)
@settings(max_examples=50)
def test_assign_instantiation(instance):
    assert isinstance(instance, Assign)

@given(instance=kbuild_Values_strategy)
@settings(max_examples=50)
def test_kbuild_values_instantiation(instance):
    assert isinstance(instance, kbuild_Values)

@given(instance=AssignExtra_strategy)
@settings(max_examples=50)
def test_assignextra_instantiation(instance):
    assert isinstance(instance, AssignExtra)

@given(instance=kbuild_Assign_strategy)
@settings(max_examples=50)
def test_kbuild_assign_instantiation(instance):
    assert isinstance(instance, kbuild_Assign)

@given(instance=kbuild_Object_M_strategy)
@settings(max_examples=50)
def test_kbuild_object_m_instantiation(instance):
    assert isinstance(instance, kbuild_Object_M)

@given(instance=kbuild_Object_Y_strategy)
@settings(max_examples=50)
def test_kbuild_object_y_instantiation(instance):
    assert isinstance(instance, kbuild_Object_Y)

@given(instance=kbuild_Model_strategy)
@settings(max_examples=50)
def test_kbuild_model_instantiation(instance):
    assert isinstance(instance, kbuild_Model)
