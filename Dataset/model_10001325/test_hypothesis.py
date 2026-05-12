import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_C21,
    genmymodelreverse_C12,
    genmymodelreverse_java_util_Map_Interface,
    genmymodelreverse_C11,
    genmymodelreverse_java_util_Vector,
    genmymodelreverse_C2,
    genmymodelreverse_C1,
    genmymodelreverse_java_util_HashMap,
    genmymodelreverse_java_io_IOException,
    genmymodelreverse_java_util_Scanner,
    interpreter_VirtualMachine,
    interpreter_RunTimeStack,
    interpreter_Program,
    interpreter_Interpreter,
    interpreter_CodeTable,
    interpreter_ByteCodeLoader,
    bytecode_WriteByteCode,
    bytecode_StoreByteCode,
    bytecode_ReturnByteCode,
    bytecode_ReadByteCode,
    bytecode_PopByteCode,
    bytecode_LoadByteCode,
    bytecode_LitByteCode,
    bytecode_LabelByteCode,
    bytecode_HaltByteCode,
    bytecode_GoToByteCode,
    bytecode_FalseBranchByteCode,
    bytecode_DumpByteCode,
    bytecode_CallByteCode,
    bytecode_ByteCode,
    bytecode_BopByteCode,
    bytecode_ArgsByteCode,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_c21_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C21)


def test_genmymodelreverse_c21_constructor_exists():
    assert callable(genmymodelreverse_C21.__init__)


def test_genmymodelreverse_c21_constructor_args():
    sig = inspect.signature(genmymodelreverse_C21.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c12_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C12)


def test_genmymodelreverse_c12_constructor_exists():
    assert callable(genmymodelreverse_C12.__init__)


def test_genmymodelreverse_c12_constructor_args():
    sig = inspect.signature(genmymodelreverse_C12.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_map_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Map_Interface)


def test_genmymodelreverse_java_util_map_interface_constructor_exists():
    assert callable(genmymodelreverse_java_util_Map_Interface.__init__)


def test_genmymodelreverse_java_util_map_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Map_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c11_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C11)


def test_genmymodelreverse_c11_constructor_exists():
    assert callable(genmymodelreverse_C11.__init__)


def test_genmymodelreverse_c11_constructor_args():
    sig = inspect.signature(genmymodelreverse_C11.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_vector_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Vector)


def test_genmymodelreverse_java_util_vector_constructor_exists():
    assert callable(genmymodelreverse_java_util_Vector.__init__)


def test_genmymodelreverse_java_util_vector_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Vector.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c2_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C2)


def test_genmymodelreverse_c2_constructor_exists():
    assert callable(genmymodelreverse_C2.__init__)


def test_genmymodelreverse_c2_constructor_args():
    sig = inspect.signature(genmymodelreverse_C2.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_c1_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_C1)


def test_genmymodelreverse_c1_constructor_exists():
    assert callable(genmymodelreverse_C1.__init__)


def test_genmymodelreverse_c1_constructor_args():
    sig = inspect.signature(genmymodelreverse_C1.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_hashmap_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_HashMap)


def test_genmymodelreverse_java_util_hashmap_constructor_exists():
    assert callable(genmymodelreverse_java_util_HashMap.__init__)


def test_genmymodelreverse_java_util_hashmap_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_HashMap.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_io_ioexception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_io_IOException)


def test_genmymodelreverse_java_io_ioexception_constructor_exists():
    assert callable(genmymodelreverse_java_io_IOException.__init__)


def test_genmymodelreverse_java_io_ioexception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_io_IOException.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_scanner_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Scanner)


def test_genmymodelreverse_java_util_scanner_constructor_exists():
    assert callable(genmymodelreverse_java_util_Scanner.__init__)


def test_genmymodelreverse_java_util_scanner_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Scanner.__init__)
    params = list(sig.parameters.keys())



def test_interpreter_virtualmachine_is_not_abstract():
    assert not inspect.isabstract(interpreter_VirtualMachine)


def test_interpreter_virtualmachine_constructor_exists():
    assert callable(interpreter_VirtualMachine.__init__)


def test_interpreter_virtualmachine_constructor_args():
    sig = inspect.signature(interpreter_VirtualMachine.__init__)
    params = list(sig.parameters.keys())
    assert "pc" in params, "Missing parameter 'pc'"
    assert "isRunning" in params, "Missing parameter 'isRunning'"
    assert "dumpState" in params, "Missing parameter 'dumpState'"
    assert "returnAddrs" in params, "Missing parameter 'returnAddrs'"

def test_interpreter_virtualmachine_has_pc():
    assert hasattr(interpreter_VirtualMachine, "pc")
    descriptor = None
    for klass in interpreter_VirtualMachine.__mro__:
        if "pc" in klass.__dict__:
            descriptor = klass.__dict__["pc"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_virtualmachine_has_isRunning():
    assert hasattr(interpreter_VirtualMachine, "isRunning")
    descriptor = None
    for klass in interpreter_VirtualMachine.__mro__:
        if "isRunning" in klass.__dict__:
            descriptor = klass.__dict__["isRunning"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_virtualmachine_has_dumpState():
    assert hasattr(interpreter_VirtualMachine, "dumpState")
    descriptor = None
    for klass in interpreter_VirtualMachine.__mro__:
        if "dumpState" in klass.__dict__:
            descriptor = klass.__dict__["dumpState"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_virtualmachine_has_returnAddrs():
    assert hasattr(interpreter_VirtualMachine, "returnAddrs")
    descriptor = None
    for klass in interpreter_VirtualMachine.__mro__:
        if "returnAddrs" in klass.__dict__:
            descriptor = klass.__dict__["returnAddrs"]
            break
    assert isinstance(descriptor, property)



def test_interpreter_runtimestack_is_not_abstract():
    assert not inspect.isabstract(interpreter_RunTimeStack)


def test_interpreter_runtimestack_constructor_exists():
    assert callable(interpreter_RunTimeStack.__init__)


def test_interpreter_runtimestack_constructor_args():
    sig = inspect.signature(interpreter_RunTimeStack.__init__)
    params = list(sig.parameters.keys())
    assert "framePointers" in params, "Missing parameter 'framePointers'"
    assert "runStack" in params, "Missing parameter 'runStack'"

def test_interpreter_runtimestack_has_framePointers():
    assert hasattr(interpreter_RunTimeStack, "framePointers")
    descriptor = None
    for klass in interpreter_RunTimeStack.__mro__:
        if "framePointers" in klass.__dict__:
            descriptor = klass.__dict__["framePointers"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_runtimestack_has_runStack():
    assert hasattr(interpreter_RunTimeStack, "runStack")
    descriptor = None
    for klass in interpreter_RunTimeStack.__mro__:
        if "runStack" in klass.__dict__:
            descriptor = klass.__dict__["runStack"]
            break
    assert isinstance(descriptor, property)



def test_interpreter_program_is_not_abstract():
    assert not inspect.isabstract(interpreter_Program)


def test_interpreter_program_constructor_exists():
    assert callable(interpreter_Program.__init__)


def test_interpreter_program_constructor_args():
    sig = inspect.signature(interpreter_Program.__init__)
    params = list(sig.parameters.keys())
    assert "programMap" in params, "Missing parameter 'programMap'"
    assert "byteCodeVector" in params, "Missing parameter 'byteCodeVector'"

def test_interpreter_program_has_programMap():
    assert hasattr(interpreter_Program, "programMap")
    descriptor = None
    for klass in interpreter_Program.__mro__:
        if "programMap" in klass.__dict__:
            descriptor = klass.__dict__["programMap"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_program_has_byteCodeVector():
    assert hasattr(interpreter_Program, "byteCodeVector")
    descriptor = None
    for klass in interpreter_Program.__mro__:
        if "byteCodeVector" in klass.__dict__:
            descriptor = klass.__dict__["byteCodeVector"]
            break
    assert isinstance(descriptor, property)



def test_interpreter_interpreter_is_not_abstract():
    assert not inspect.isabstract(interpreter_Interpreter)


def test_interpreter_interpreter_constructor_exists():
    assert callable(interpreter_Interpreter.__init__)


def test_interpreter_interpreter_constructor_args():
    sig = inspect.signature(interpreter_Interpreter.__init__)
    params = list(sig.parameters.keys())



def test_interpreter_codetable_is_not_abstract():
    assert not inspect.isabstract(interpreter_CodeTable)


def test_interpreter_codetable_constructor_exists():
    assert callable(interpreter_CodeTable.__init__)


def test_interpreter_codetable_constructor_args():
    sig = inspect.signature(interpreter_CodeTable.__init__)
    params = list(sig.parameters.keys())
    assert "byteCodesTXT" in params, "Missing parameter 'byteCodesTXT'"
    assert "codeMap" in params, "Missing parameter 'codeMap'"

def test_interpreter_codetable_has_byteCodesTXT():
    assert hasattr(interpreter_CodeTable, "byteCodesTXT")
    descriptor = None
    for klass in interpreter_CodeTable.__mro__:
        if "byteCodesTXT" in klass.__dict__:
            descriptor = klass.__dict__["byteCodesTXT"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_codetable_has_codeMap():
    assert hasattr(interpreter_CodeTable, "codeMap")
    descriptor = None
    for klass in interpreter_CodeTable.__mro__:
        if "codeMap" in klass.__dict__:
            descriptor = klass.__dict__["codeMap"]
            break
    assert isinstance(descriptor, property)



def test_interpreter_bytecodeloader_is_not_abstract():
    assert not inspect.isabstract(interpreter_ByteCodeLoader)


def test_interpreter_bytecodeloader_constructor_exists():
    assert callable(interpreter_ByteCodeLoader.__init__)


def test_interpreter_bytecodeloader_constructor_args():
    sig = inspect.signature(interpreter_ByteCodeLoader.__init__)
    params = list(sig.parameters.keys())
    assert "lineCount" in params, "Missing parameter 'lineCount'"
    assert "programMap" in params, "Missing parameter 'programMap'"
    assert "input" in params, "Missing parameter 'input'"

def test_interpreter_bytecodeloader_has_lineCount():
    assert hasattr(interpreter_ByteCodeLoader, "lineCount")
    descriptor = None
    for klass in interpreter_ByteCodeLoader.__mro__:
        if "lineCount" in klass.__dict__:
            descriptor = klass.__dict__["lineCount"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_bytecodeloader_has_programMap():
    assert hasattr(interpreter_ByteCodeLoader, "programMap")
    descriptor = None
    for klass in interpreter_ByteCodeLoader.__mro__:
        if "programMap" in klass.__dict__:
            descriptor = klass.__dict__["programMap"]
            break
    assert isinstance(descriptor, property)

def test_interpreter_bytecodeloader_has_input():
    assert hasattr(interpreter_ByteCodeLoader, "input")
    descriptor = None
    for klass in interpreter_ByteCodeLoader.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_writebytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_WriteByteCode)


def test_bytecode_writebytecode_constructor_exists():
    assert callable(bytecode_WriteByteCode.__init__)


def test_bytecode_writebytecode_constructor_args():
    sig = inspect.signature(bytecode_WriteByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_writebytecode_has_byteCode():
    assert hasattr(bytecode_WriteByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_WriteByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_storebytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_StoreByteCode)


def test_bytecode_storebytecode_constructor_exists():
    assert callable(bytecode_StoreByteCode.__init__)


def test_bytecode_storebytecode_constructor_args():
    sig = inspect.signature(bytecode_StoreByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "storeValue" in params, "Missing parameter 'storeValue'"
    assert "storeID" in params, "Missing parameter 'storeID'"
    assert "theArg" in params, "Missing parameter 'theArg'"

def test_bytecode_storebytecode_has_byteCode():
    assert hasattr(bytecode_StoreByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_StoreByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_storebytecode_has_storeValue():
    assert hasattr(bytecode_StoreByteCode, "storeValue")
    descriptor = None
    for klass in bytecode_StoreByteCode.__mro__:
        if "storeValue" in klass.__dict__:
            descriptor = klass.__dict__["storeValue"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_storebytecode_has_storeID():
    assert hasattr(bytecode_StoreByteCode, "storeID")
    descriptor = None
    for klass in bytecode_StoreByteCode.__mro__:
        if "storeID" in klass.__dict__:
            descriptor = klass.__dict__["storeID"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_storebytecode_has_theArg():
    assert hasattr(bytecode_StoreByteCode, "theArg")
    descriptor = None
    for klass in bytecode_StoreByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_returnbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_ReturnByteCode)


def test_bytecode_returnbytecode_constructor_exists():
    assert callable(bytecode_ReturnByteCode.__init__)


def test_bytecode_returnbytecode_constructor_args():
    sig = inspect.signature(bytecode_ReturnByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_returnbytecode_has_byteCode():
    assert hasattr(bytecode_ReturnByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_ReturnByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_readbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_ReadByteCode)


def test_bytecode_readbytecode_constructor_exists():
    assert callable(bytecode_ReadByteCode.__init__)


def test_bytecode_readbytecode_constructor_args():
    sig = inspect.signature(bytecode_ReadByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_readbytecode_has_byteCode():
    assert hasattr(bytecode_ReadByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_ReadByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_popbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_PopByteCode)


def test_bytecode_popbytecode_constructor_exists():
    assert callable(bytecode_PopByteCode.__init__)


def test_bytecode_popbytecode_constructor_args():
    sig = inspect.signature(bytecode_PopByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "count" in params, "Missing parameter 'count'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "theArg" in params, "Missing parameter 'theArg'"

def test_bytecode_popbytecode_has_count():
    assert hasattr(bytecode_PopByteCode, "count")
    descriptor = None
    for klass in bytecode_PopByteCode.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_popbytecode_has_byteCode():
    assert hasattr(bytecode_PopByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_PopByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_popbytecode_has_theArg():
    assert hasattr(bytecode_PopByteCode, "theArg")
    descriptor = None
    for klass in bytecode_PopByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_loadbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_LoadByteCode)


def test_bytecode_loadbytecode_constructor_exists():
    assert callable(bytecode_LoadByteCode.__init__)


def test_bytecode_loadbytecode_constructor_args():
    sig = inspect.signature(bytecode_LoadByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "loadOffset" in params, "Missing parameter 'loadOffset'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "loadID" in params, "Missing parameter 'loadID'"

def test_bytecode_loadbytecode_has_loadOffset():
    assert hasattr(bytecode_LoadByteCode, "loadOffset")
    descriptor = None
    for klass in bytecode_LoadByteCode.__mro__:
        if "loadOffset" in klass.__dict__:
            descriptor = klass.__dict__["loadOffset"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_loadbytecode_has_byteCode():
    assert hasattr(bytecode_LoadByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_LoadByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_loadbytecode_has_loadID():
    assert hasattr(bytecode_LoadByteCode, "loadID")
    descriptor = None
    for klass in bytecode_LoadByteCode.__mro__:
        if "loadID" in klass.__dict__:
            descriptor = klass.__dict__["loadID"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_litbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_LitByteCode)


def test_bytecode_litbytecode_constructor_exists():
    assert callable(bytecode_LitByteCode.__init__)


def test_bytecode_litbytecode_constructor_args():
    sig = inspect.signature(bytecode_LitByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "litID" in params, "Missing parameter 'litID'"
    assert "litValue" in params, "Missing parameter 'litValue'"

def test_bytecode_litbytecode_has_byteCode():
    assert hasattr(bytecode_LitByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_LitByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_litbytecode_has_litID():
    assert hasattr(bytecode_LitByteCode, "litID")
    descriptor = None
    for klass in bytecode_LitByteCode.__mro__:
        if "litID" in klass.__dict__:
            descriptor = klass.__dict__["litID"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_litbytecode_has_litValue():
    assert hasattr(bytecode_LitByteCode, "litValue")
    descriptor = None
    for klass in bytecode_LitByteCode.__mro__:
        if "litValue" in klass.__dict__:
            descriptor = klass.__dict__["litValue"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_labelbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_LabelByteCode)


def test_bytecode_labelbytecode_constructor_exists():
    assert callable(bytecode_LabelByteCode.__init__)


def test_bytecode_labelbytecode_constructor_args():
    sig = inspect.signature(bytecode_LabelByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "theArg" in params, "Missing parameter 'theArg'"
    assert "lineNO" in params, "Missing parameter 'lineNO'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_labelbytecode_has_theArg():
    assert hasattr(bytecode_LabelByteCode, "theArg")
    descriptor = None
    for klass in bytecode_LabelByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_labelbytecode_has_lineNO():
    assert hasattr(bytecode_LabelByteCode, "lineNO")
    descriptor = None
    for klass in bytecode_LabelByteCode.__mro__:
        if "lineNO" in klass.__dict__:
            descriptor = klass.__dict__["lineNO"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_labelbytecode_has_byteCode():
    assert hasattr(bytecode_LabelByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_LabelByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_haltbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_HaltByteCode)


def test_bytecode_haltbytecode_constructor_exists():
    assert callable(bytecode_HaltByteCode.__init__)


def test_bytecode_haltbytecode_constructor_args():
    sig = inspect.signature(bytecode_HaltByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_haltbytecode_has_byteCode():
    assert hasattr(bytecode_HaltByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_HaltByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_gotobytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_GoToByteCode)


def test_bytecode_gotobytecode_constructor_exists():
    assert callable(bytecode_GoToByteCode.__init__)


def test_bytecode_gotobytecode_constructor_args():
    sig = inspect.signature(bytecode_GoToByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "lineNO" in params, "Missing parameter 'lineNO'"
    assert "theArg" in params, "Missing parameter 'theArg'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_gotobytecode_has_lineNO():
    assert hasattr(bytecode_GoToByteCode, "lineNO")
    descriptor = None
    for klass in bytecode_GoToByteCode.__mro__:
        if "lineNO" in klass.__dict__:
            descriptor = klass.__dict__["lineNO"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_gotobytecode_has_theArg():
    assert hasattr(bytecode_GoToByteCode, "theArg")
    descriptor = None
    for klass in bytecode_GoToByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_gotobytecode_has_byteCode():
    assert hasattr(bytecode_GoToByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_GoToByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_falsebranchbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_FalseBranchByteCode)


def test_bytecode_falsebranchbytecode_constructor_exists():
    assert callable(bytecode_FalseBranchByteCode.__init__)


def test_bytecode_falsebranchbytecode_constructor_args():
    sig = inspect.signature(bytecode_FalseBranchByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "theArg" in params, "Missing parameter 'theArg'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "lineNO" in params, "Missing parameter 'lineNO'"

def test_bytecode_falsebranchbytecode_has_theArg():
    assert hasattr(bytecode_FalseBranchByteCode, "theArg")
    descriptor = None
    for klass in bytecode_FalseBranchByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_falsebranchbytecode_has_byteCode():
    assert hasattr(bytecode_FalseBranchByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_FalseBranchByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_falsebranchbytecode_has_lineNO():
    assert hasattr(bytecode_FalseBranchByteCode, "lineNO")
    descriptor = None
    for klass in bytecode_FalseBranchByteCode.__mro__:
        if "lineNO" in klass.__dict__:
            descriptor = klass.__dict__["lineNO"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_dumpbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_DumpByteCode)


def test_bytecode_dumpbytecode_constructor_exists():
    assert callable(bytecode_DumpByteCode.__init__)


def test_bytecode_dumpbytecode_constructor_args():
    sig = inspect.signature(bytecode_DumpByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "theArg" in params, "Missing parameter 'theArg'"
    assert "byteCode" in params, "Missing parameter 'byteCode'"

def test_bytecode_dumpbytecode_has_theArg():
    assert hasattr(bytecode_DumpByteCode, "theArg")
    descriptor = None
    for klass in bytecode_DumpByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_dumpbytecode_has_byteCode():
    assert hasattr(bytecode_DumpByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_DumpByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_callbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_CallByteCode)


def test_bytecode_callbytecode_constructor_exists():
    assert callable(bytecode_CallByteCode.__init__)


def test_bytecode_callbytecode_constructor_args():
    sig = inspect.signature(bytecode_CallByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "lineNO" in params, "Missing parameter 'lineNO'"
    assert "theArg" in params, "Missing parameter 'theArg'"

def test_bytecode_callbytecode_has_byteCode():
    assert hasattr(bytecode_CallByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_CallByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_callbytecode_has_lineNO():
    assert hasattr(bytecode_CallByteCode, "lineNO")
    descriptor = None
    for klass in bytecode_CallByteCode.__mro__:
        if "lineNO" in klass.__dict__:
            descriptor = klass.__dict__["lineNO"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_callbytecode_has_theArg():
    assert hasattr(bytecode_CallByteCode, "theArg")
    descriptor = None
    for klass in bytecode_CallByteCode.__mro__:
        if "theArg" in klass.__dict__:
            descriptor = klass.__dict__["theArg"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_bytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_ByteCode)


def test_bytecode_bytecode_constructor_exists():
    assert callable(bytecode_ByteCode.__init__)


def test_bytecode_bytecode_constructor_args():
    sig = inspect.signature(bytecode_ByteCode.__init__)
    params = list(sig.parameters.keys())



def test_bytecode_bopbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_BopByteCode)


def test_bytecode_bopbytecode_constructor_exists():
    assert callable(bytecode_BopByteCode.__init__)


def test_bytecode_bopbytecode_constructor_args():
    sig = inspect.signature(bytecode_BopByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "theOperator" in params, "Missing parameter 'theOperator'"

def test_bytecode_bopbytecode_has_byteCode():
    assert hasattr(bytecode_BopByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_BopByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_bopbytecode_has_theOperator():
    assert hasattr(bytecode_BopByteCode, "theOperator")
    descriptor = None
    for klass in bytecode_BopByteCode.__mro__:
        if "theOperator" in klass.__dict__:
            descriptor = klass.__dict__["theOperator"]
            break
    assert isinstance(descriptor, property)



def test_bytecode_argsbytecode_is_not_abstract():
    assert not inspect.isabstract(bytecode_ArgsByteCode)


def test_bytecode_argsbytecode_constructor_exists():
    assert callable(bytecode_ArgsByteCode.__init__)


def test_bytecode_argsbytecode_constructor_args():
    sig = inspect.signature(bytecode_ArgsByteCode.__init__)
    params = list(sig.parameters.keys())
    assert "byteCode" in params, "Missing parameter 'byteCode'"
    assert "argCount" in params, "Missing parameter 'argCount'"

def test_bytecode_argsbytecode_has_byteCode():
    assert hasattr(bytecode_ArgsByteCode, "byteCode")
    descriptor = None
    for klass in bytecode_ArgsByteCode.__mro__:
        if "byteCode" in klass.__dict__:
            descriptor = klass.__dict__["byteCode"]
            break
    assert isinstance(descriptor, property)

def test_bytecode_argsbytecode_has_argCount():
    assert hasattr(bytecode_ArgsByteCode, "argCount")
    descriptor = None
    for klass in bytecode_ArgsByteCode.__mro__:
        if "argCount" in klass.__dict__:
            descriptor = klass.__dict__["argCount"]
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
genmymodelreverse_C21_strategy = st.builds(
    genmymodelreverse_C21,
)
genmymodelreverse_C12_strategy = st.builds(
    genmymodelreverse_C12,
)
genmymodelreverse_java_util_Map_Interface_strategy = st.builds(
    genmymodelreverse_java_util_Map_Interface,
)
genmymodelreverse_C11_strategy = st.builds(
    genmymodelreverse_C11,
)
genmymodelreverse_java_util_Vector_strategy = st.builds(
    genmymodelreverse_java_util_Vector,
)
genmymodelreverse_C2_strategy = st.builds(
    genmymodelreverse_C2,
)
genmymodelreverse_C1_strategy = st.builds(
    genmymodelreverse_C1,
)
genmymodelreverse_java_util_HashMap_strategy = st.builds(
    genmymodelreverse_java_util_HashMap,
)
genmymodelreverse_java_io_IOException_strategy = st.builds(
    genmymodelreverse_java_io_IOException,
)
genmymodelreverse_java_util_Scanner_strategy = st.builds(
    genmymodelreverse_java_util_Scanner,
)
interpreter_VirtualMachine_strategy = st.builds(
    interpreter_VirtualMachine,
    pc=
        st.integers(),
    isRunning=
        st.booleans(),
    dumpState=
        st.booleans(),
    returnAddrs=
        st.integers()
)
interpreter_RunTimeStack_strategy = st.builds(
    interpreter_RunTimeStack,
    framePointers=
        st.integers(),
    runStack=
        safe_text
)
interpreter_Program_strategy = st.builds(
    interpreter_Program,
    programMap=
        safe_text,
    byteCodeVector=
        safe_text
)
interpreter_Interpreter_strategy = st.builds(
    interpreter_Interpreter,
)
interpreter_CodeTable_strategy = st.builds(
    interpreter_CodeTable,
    byteCodesTXT=
        safe_text,
    codeMap=
        safe_text
)
interpreter_ByteCodeLoader_strategy = st.builds(
    interpreter_ByteCodeLoader,
    lineCount=
        st.integers(),
    programMap=
        safe_text,
    input=
        st.none()
)
bytecode_WriteByteCode_strategy = st.builds(
    bytecode_WriteByteCode,
    byteCode=
        safe_text
)
bytecode_StoreByteCode_strategy = st.builds(
    bytecode_StoreByteCode,
    byteCode=
        safe_text,
    storeValue=
        st.integers(),
    storeID=
        safe_text,
    theArg=
        safe_text
)
bytecode_ReturnByteCode_strategy = st.builds(
    bytecode_ReturnByteCode,
    byteCode=
        safe_text
)
bytecode_ReadByteCode_strategy = st.builds(
    bytecode_ReadByteCode,
    byteCode=
        safe_text
)
bytecode_PopByteCode_strategy = st.builds(
    bytecode_PopByteCode,
    count=
        st.integers(),
    byteCode=
        safe_text,
    theArg=
        safe_text
)
bytecode_LoadByteCode_strategy = st.builds(
    bytecode_LoadByteCode,
    loadOffset=
        st.integers(),
    byteCode=
        safe_text,
    loadID=
        safe_text
)
bytecode_LitByteCode_strategy = st.builds(
    bytecode_LitByteCode,
    byteCode=
        safe_text,
    litID=
        safe_text,
    litValue=
        st.integers()
)
bytecode_LabelByteCode_strategy = st.builds(
    bytecode_LabelByteCode,
    theArg=
        safe_text,
    lineNO=
        st.integers(),
    byteCode=
        safe_text
)
bytecode_HaltByteCode_strategy = st.builds(
    bytecode_HaltByteCode,
    byteCode=
        safe_text
)
bytecode_GoToByteCode_strategy = st.builds(
    bytecode_GoToByteCode,
    lineNO=
        st.integers(),
    theArg=
        safe_text,
    byteCode=
        safe_text
)
bytecode_FalseBranchByteCode_strategy = st.builds(
    bytecode_FalseBranchByteCode,
    theArg=
        safe_text,
    byteCode=
        safe_text,
    lineNO=
        st.integers()
)
bytecode_DumpByteCode_strategy = st.builds(
    bytecode_DumpByteCode,
    theArg=
        safe_text,
    byteCode=
        safe_text
)
bytecode_CallByteCode_strategy = st.builds(
    bytecode_CallByteCode,
    byteCode=
        safe_text,
    lineNO=
        st.integers(),
    theArg=
        safe_text
)
bytecode_ByteCode_strategy = st.builds(
    bytecode_ByteCode,
)
bytecode_BopByteCode_strategy = st.builds(
    bytecode_BopByteCode,
    byteCode=
        safe_text,
    theOperator=
        safe_text
)
bytecode_ArgsByteCode_strategy = st.builds(
    bytecode_ArgsByteCode,
    byteCode=
        safe_text,
    argCount=
        st.integers()
)

@given(instance=genmymodelreverse_C21_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c21_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C21)

@given(instance=genmymodelreverse_C12_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c12_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C12)

@given(instance=genmymodelreverse_java_util_Map_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_map_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Map_Interface)

@given(instance=genmymodelreverse_C11_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c11_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C11)

@given(instance=genmymodelreverse_java_util_Vector_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_vector_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Vector)

@given(instance=genmymodelreverse_C2_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c2_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C2)

@given(instance=genmymodelreverse_C1_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_c1_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_C1)

@given(instance=genmymodelreverse_java_util_HashMap_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_hashmap_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_HashMap)

@given(instance=genmymodelreverse_java_io_IOException_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_io_ioexception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_IOException)

@given(instance=genmymodelreverse_java_util_Scanner_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_scanner_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Scanner)

@given(instance=interpreter_VirtualMachine_strategy)
@settings(max_examples=50)
def test_interpreter_virtualmachine_instantiation(instance):
    assert isinstance(instance, interpreter_VirtualMachine)



@given(instance=interpreter_VirtualMachine_strategy)
def test_interpreter_virtualmachine_pc_setter(instance):
    original = instance.pc
    instance.pc = original
    assert instance.pc == original



@given(instance=interpreter_VirtualMachine_strategy)
def test_interpreter_virtualmachine_isRunning_setter(instance):
    original = instance.isRunning
    instance.isRunning = original
    assert instance.isRunning == original



@given(instance=interpreter_VirtualMachine_strategy)
def test_interpreter_virtualmachine_dumpState_setter(instance):
    original = instance.dumpState
    instance.dumpState = original
    assert instance.dumpState == original



@given(instance=interpreter_VirtualMachine_strategy)
def test_interpreter_virtualmachine_returnAddrs_setter(instance):
    original = instance.returnAddrs
    instance.returnAddrs = original
    assert instance.returnAddrs == original

@given(instance=interpreter_RunTimeStack_strategy)
@settings(max_examples=50)
def test_interpreter_runtimestack_instantiation(instance):
    assert isinstance(instance, interpreter_RunTimeStack)



@given(instance=interpreter_RunTimeStack_strategy)
def test_interpreter_runtimestack_framePointers_setter(instance):
    original = instance.framePointers
    instance.framePointers = original
    assert instance.framePointers == original



@given(instance=interpreter_RunTimeStack_strategy)
def test_interpreter_runtimestack_runStack_setter(instance):
    original = instance.runStack
    instance.runStack = original
    assert instance.runStack == original

@given(instance=interpreter_Program_strategy)
@settings(max_examples=50)
def test_interpreter_program_instantiation(instance):
    assert isinstance(instance, interpreter_Program)



@given(instance=interpreter_Program_strategy)
def test_interpreter_program_programMap_setter(instance):
    original = instance.programMap
    instance.programMap = original
    assert instance.programMap == original



@given(instance=interpreter_Program_strategy)
def test_interpreter_program_byteCodeVector_setter(instance):
    original = instance.byteCodeVector
    instance.byteCodeVector = original
    assert instance.byteCodeVector == original

@given(instance=interpreter_Interpreter_strategy)
@settings(max_examples=50)
def test_interpreter_interpreter_instantiation(instance):
    assert isinstance(instance, interpreter_Interpreter)

@given(instance=interpreter_CodeTable_strategy)
@settings(max_examples=50)
def test_interpreter_codetable_instantiation(instance):
    assert isinstance(instance, interpreter_CodeTable)



@given(instance=interpreter_CodeTable_strategy)
def test_interpreter_codetable_byteCodesTXT_setter(instance):
    original = instance.byteCodesTXT
    instance.byteCodesTXT = original
    assert instance.byteCodesTXT == original



@given(instance=interpreter_CodeTable_strategy)
def test_interpreter_codetable_codeMap_setter(instance):
    original = instance.codeMap
    instance.codeMap = original
    assert instance.codeMap == original

@given(instance=interpreter_ByteCodeLoader_strategy)
@settings(max_examples=50)
def test_interpreter_bytecodeloader_instantiation(instance):
    assert isinstance(instance, interpreter_ByteCodeLoader)



@given(instance=interpreter_ByteCodeLoader_strategy)
def test_interpreter_bytecodeloader_lineCount_setter(instance):
    original = instance.lineCount
    instance.lineCount = original
    assert instance.lineCount == original



@given(instance=interpreter_ByteCodeLoader_strategy)
def test_interpreter_bytecodeloader_programMap_setter(instance):
    original = instance.programMap
    instance.programMap = original
    assert instance.programMap == original



@given(instance=interpreter_ByteCodeLoader_strategy)
def test_interpreter_bytecodeloader_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=bytecode_WriteByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_writebytecode_instantiation(instance):
    assert isinstance(instance, bytecode_WriteByteCode)



@given(instance=bytecode_WriteByteCode_strategy)
def test_bytecode_writebytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_StoreByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_storebytecode_instantiation(instance):
    assert isinstance(instance, bytecode_StoreByteCode)



@given(instance=bytecode_StoreByteCode_strategy)
def test_bytecode_storebytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_StoreByteCode_strategy)
def test_bytecode_storebytecode_storeValue_setter(instance):
    original = instance.storeValue
    instance.storeValue = original
    assert instance.storeValue == original



@given(instance=bytecode_StoreByteCode_strategy)
def test_bytecode_storebytecode_storeID_setter(instance):
    original = instance.storeID
    instance.storeID = original
    assert instance.storeID == original



@given(instance=bytecode_StoreByteCode_strategy)
def test_bytecode_storebytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original

@given(instance=bytecode_ReturnByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_returnbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_ReturnByteCode)



@given(instance=bytecode_ReturnByteCode_strategy)
def test_bytecode_returnbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_ReadByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_readbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_ReadByteCode)



@given(instance=bytecode_ReadByteCode_strategy)
def test_bytecode_readbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_PopByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_popbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_PopByteCode)



@given(instance=bytecode_PopByteCode_strategy)
def test_bytecode_popbytecode_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original



@given(instance=bytecode_PopByteCode_strategy)
def test_bytecode_popbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_PopByteCode_strategy)
def test_bytecode_popbytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original

@given(instance=bytecode_LoadByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_loadbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_LoadByteCode)



@given(instance=bytecode_LoadByteCode_strategy)
def test_bytecode_loadbytecode_loadOffset_setter(instance):
    original = instance.loadOffset
    instance.loadOffset = original
    assert instance.loadOffset == original



@given(instance=bytecode_LoadByteCode_strategy)
def test_bytecode_loadbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_LoadByteCode_strategy)
def test_bytecode_loadbytecode_loadID_setter(instance):
    original = instance.loadID
    instance.loadID = original
    assert instance.loadID == original

@given(instance=bytecode_LitByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_litbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_LitByteCode)



@given(instance=bytecode_LitByteCode_strategy)
def test_bytecode_litbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_LitByteCode_strategy)
def test_bytecode_litbytecode_litID_setter(instance):
    original = instance.litID
    instance.litID = original
    assert instance.litID == original



@given(instance=bytecode_LitByteCode_strategy)
def test_bytecode_litbytecode_litValue_setter(instance):
    original = instance.litValue
    instance.litValue = original
    assert instance.litValue == original

@given(instance=bytecode_LabelByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_labelbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_LabelByteCode)



@given(instance=bytecode_LabelByteCode_strategy)
def test_bytecode_labelbytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original



@given(instance=bytecode_LabelByteCode_strategy)
def test_bytecode_labelbytecode_lineNO_setter(instance):
    original = instance.lineNO
    instance.lineNO = original
    assert instance.lineNO == original



@given(instance=bytecode_LabelByteCode_strategy)
def test_bytecode_labelbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_HaltByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_haltbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_HaltByteCode)



@given(instance=bytecode_HaltByteCode_strategy)
def test_bytecode_haltbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_GoToByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_gotobytecode_instantiation(instance):
    assert isinstance(instance, bytecode_GoToByteCode)



@given(instance=bytecode_GoToByteCode_strategy)
def test_bytecode_gotobytecode_lineNO_setter(instance):
    original = instance.lineNO
    instance.lineNO = original
    assert instance.lineNO == original



@given(instance=bytecode_GoToByteCode_strategy)
def test_bytecode_gotobytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original



@given(instance=bytecode_GoToByteCode_strategy)
def test_bytecode_gotobytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_FalseBranchByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_falsebranchbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_FalseBranchByteCode)



@given(instance=bytecode_FalseBranchByteCode_strategy)
def test_bytecode_falsebranchbytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original



@given(instance=bytecode_FalseBranchByteCode_strategy)
def test_bytecode_falsebranchbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_FalseBranchByteCode_strategy)
def test_bytecode_falsebranchbytecode_lineNO_setter(instance):
    original = instance.lineNO
    instance.lineNO = original
    assert instance.lineNO == original

@given(instance=bytecode_DumpByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_dumpbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_DumpByteCode)



@given(instance=bytecode_DumpByteCode_strategy)
def test_bytecode_dumpbytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original



@given(instance=bytecode_DumpByteCode_strategy)
def test_bytecode_dumpbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original

@given(instance=bytecode_CallByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_callbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_CallByteCode)



@given(instance=bytecode_CallByteCode_strategy)
def test_bytecode_callbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_CallByteCode_strategy)
def test_bytecode_callbytecode_lineNO_setter(instance):
    original = instance.lineNO
    instance.lineNO = original
    assert instance.lineNO == original



@given(instance=bytecode_CallByteCode_strategy)
def test_bytecode_callbytecode_theArg_setter(instance):
    original = instance.theArg
    instance.theArg = original
    assert instance.theArg == original

@given(instance=bytecode_ByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_bytecode_instantiation(instance):
    assert isinstance(instance, bytecode_ByteCode)

@given(instance=bytecode_BopByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_bopbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_BopByteCode)



@given(instance=bytecode_BopByteCode_strategy)
def test_bytecode_bopbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_BopByteCode_strategy)
def test_bytecode_bopbytecode_theOperator_setter(instance):
    original = instance.theOperator
    instance.theOperator = original
    assert instance.theOperator == original

@given(instance=bytecode_ArgsByteCode_strategy)
@settings(max_examples=50)
def test_bytecode_argsbytecode_instantiation(instance):
    assert isinstance(instance, bytecode_ArgsByteCode)



@given(instance=bytecode_ArgsByteCode_strategy)
def test_bytecode_argsbytecode_byteCode_setter(instance):
    original = instance.byteCode
    instance.byteCode = original
    assert instance.byteCode == original



@given(instance=bytecode_ArgsByteCode_strategy)
def test_bytecode_argsbytecode_argCount_setter(instance):
    original = instance.argCount
    instance.argCount = original
    assert instance.argCount == original
