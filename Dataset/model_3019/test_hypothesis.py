import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ItemIdValue,
    ir_ItemIdValueCall,
    ir_ItemIdValueIterator,
    Container,
    ir_SetRef,
    IrType,
    IterationBlock,
    ir_Interval,
    ir_Iterator,
    ir_ConnectivityCall,
    Expression,
    ir_RealConstant,
    ir_Parenthesis,
    ir_BoolConstant,
    ir_FunctionCall,
    ir_BinaryExpression,
    ir_UnaryExpression,
    ir_VectorConstant,
    ir_IntConstant,
    ir_BaseTypeConstant,
    ir_MaxConstant,
    ir_MinConstant,
    ir_Cardinality,
    ir_ContractedIf,
    IterableInstruction,
    ir_ReductionInstruction,
    Instruction,
    ir_Return,
    ir_Exit,
    ir_IterableInstruction,
    ir_ItemIndexDefinition,
    ir_Affectation,
    ir_VariableDefinition,
    ir_ItemIdDefinition,
    ir_SetDefinition,
    ir_If,
    ir_InstructionBlock,
    TimeLoopCopyJob,
    ir_BeforeTimeLoopJob,
    ir_AfterTimeLoopJob,
    Job,
    ir_TimeLoopCopyJob,
    ir_InstructionJob,
    ir_Loop,
    ir_ArgOrVarRef,
    ir_ConnectivityType,
    Variable,
    ir_BaseType,
    ArgOrVar,
    ir_Arg,
    JobContainer,
    ir_TimeLoopJob,
    ir_IrModule,
    ir_ConnectivityVariable,
    ir_Variable,
    ir_SimpleVariable,
    IrAnnotable,
    ir_Import,
    ir_TimeLoopCopy,
    ir_ItemType,
    ir_Connectivity,
    ir_IterationBlock,
    ir_ItemIndexValue,
    ir_Container,
    ir_Function,
    ir_Job,
    ir_ItemIdValue,
    ir_Instruction,
    ir_ItemId,
    ir_ItemIndex,
    ir_PostProcessingInfo,
    ir_TimeLoopVariable,
    ir_ArgOrVar,
    ir_TimeLoop,
    ir_IrType,
    ir_Expression,
    ir_JobContainer,
    ir_EStringToStringMapEntry,
    ir_IrAnnotation,
    ir_IrAnnotable,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_itemidvalue_is_not_abstract():
    assert not inspect.isabstract(ItemIdValue)


def test_itemidvalue_constructor_exists():
    assert callable(ItemIdValue.__init__)


def test_itemidvalue_constructor_args():
    sig = inspect.signature(ItemIdValue.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemidvaluecall_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIdValueCall)


def test_ir_itemidvaluecall_constructor_exists():
    assert callable(ir_ItemIdValueCall.__init__)


def test_ir_itemidvaluecall_constructor_args():
    sig = inspect.signature(ir_ItemIdValueCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemidvalueiterator_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIdValueIterator)


def test_ir_itemidvalueiterator_constructor_exists():
    assert callable(ir_ItemIdValueIterator.__init__)


def test_ir_itemidvalueiterator_constructor_args():
    sig = inspect.signature(ir_ItemIdValueIterator.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"

def test_ir_itemidvalueiterator_has_shift():
    assert hasattr(ir_ItemIdValueIterator, "shift")
    descriptor = None
    for klass in ir_ItemIdValueIterator.__mro__:
        if "shift" in klass.__dict__:
            descriptor = klass.__dict__["shift"]
            break
    assert isinstance(descriptor, property)



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_ir_setref_is_not_abstract():
    assert not inspect.isabstract(ir_SetRef)


def test_ir_setref_constructor_exists():
    assert callable(ir_SetRef.__init__)


def test_ir_setref_constructor_args():
    sig = inspect.signature(ir_SetRef.__init__)
    params = list(sig.parameters.keys())



def test_irtype_is_not_abstract():
    assert not inspect.isabstract(IrType)


def test_irtype_constructor_exists():
    assert callable(IrType.__init__)


def test_irtype_constructor_args():
    sig = inspect.signature(IrType.__init__)
    params = list(sig.parameters.keys())



def test_iterationblock_is_not_abstract():
    assert not inspect.isabstract(IterationBlock)


def test_iterationblock_constructor_exists():
    assert callable(IterationBlock.__init__)


def test_iterationblock_constructor_args():
    sig = inspect.signature(IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_ir_interval_is_not_abstract():
    assert not inspect.isabstract(ir_Interval)


def test_ir_interval_constructor_exists():
    assert callable(ir_Interval.__init__)


def test_ir_interval_constructor_args():
    sig = inspect.signature(ir_Interval.__init__)
    params = list(sig.parameters.keys())



def test_ir_iterator_is_not_abstract():
    assert not inspect.isabstract(ir_Iterator)


def test_ir_iterator_constructor_exists():
    assert callable(ir_Iterator.__init__)


def test_ir_iterator_constructor_args():
    sig = inspect.signature(ir_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ir_connectivitycall_is_not_abstract():
    assert not inspect.isabstract(ir_ConnectivityCall)


def test_ir_connectivitycall_constructor_exists():
    assert callable(ir_ConnectivityCall.__init__)


def test_ir_connectivitycall_constructor_args():
    sig = inspect.signature(ir_ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir_realconstant_is_not_abstract():
    assert not inspect.isabstract(ir_RealConstant)


def test_ir_realconstant_constructor_exists():
    assert callable(ir_RealConstant.__init__)


def test_ir_realconstant_constructor_args():
    sig = inspect.signature(ir_RealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_realconstant_has_value():
    assert hasattr(ir_RealConstant, "value")
    descriptor = None
    for klass in ir_RealConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_parenthesis_is_not_abstract():
    assert not inspect.isabstract(ir_Parenthesis)


def test_ir_parenthesis_constructor_exists():
    assert callable(ir_Parenthesis.__init__)


def test_ir_parenthesis_constructor_args():
    sig = inspect.signature(ir_Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_ir_boolconstant_is_not_abstract():
    assert not inspect.isabstract(ir_BoolConstant)


def test_ir_boolconstant_constructor_exists():
    assert callable(ir_BoolConstant.__init__)


def test_ir_boolconstant_constructor_args():
    sig = inspect.signature(ir_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_boolconstant_has_value():
    assert hasattr(ir_BoolConstant, "value")
    descriptor = None
    for klass in ir_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_functioncall_is_not_abstract():
    assert not inspect.isabstract(ir_FunctionCall)


def test_ir_functioncall_constructor_exists():
    assert callable(ir_FunctionCall.__init__)


def test_ir_functioncall_constructor_args():
    sig = inspect.signature(ir_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir_BinaryExpression)


def test_ir_binaryexpression_constructor_exists():
    assert callable(ir_BinaryExpression.__init__)


def test_ir_binaryexpression_constructor_args():
    sig = inspect.signature(ir_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir_binaryexpression_has_operator():
    assert hasattr(ir_BinaryExpression, "operator")
    descriptor = None
    for klass in ir_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir_UnaryExpression)


def test_ir_unaryexpression_constructor_exists():
    assert callable(ir_UnaryExpression.__init__)


def test_ir_unaryexpression_constructor_args():
    sig = inspect.signature(ir_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir_unaryexpression_has_operator():
    assert hasattr(ir_UnaryExpression, "operator")
    descriptor = None
    for klass in ir_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir_vectorconstant_is_not_abstract():
    assert not inspect.isabstract(ir_VectorConstant)


def test_ir_vectorconstant_constructor_exists():
    assert callable(ir_VectorConstant.__init__)


def test_ir_vectorconstant_constructor_args():
    sig = inspect.signature(ir_VectorConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir_intconstant_is_not_abstract():
    assert not inspect.isabstract(ir_IntConstant)


def test_ir_intconstant_constructor_exists():
    assert callable(ir_IntConstant.__init__)


def test_ir_intconstant_constructor_args():
    sig = inspect.signature(ir_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_intconstant_has_value():
    assert hasattr(ir_IntConstant, "value")
    descriptor = None
    for klass in ir_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_basetypeconstant_is_not_abstract():
    assert not inspect.isabstract(ir_BaseTypeConstant)


def test_ir_basetypeconstant_constructor_exists():
    assert callable(ir_BaseTypeConstant.__init__)


def test_ir_basetypeconstant_constructor_args():
    sig = inspect.signature(ir_BaseTypeConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir_maxconstant_is_not_abstract():
    assert not inspect.isabstract(ir_MaxConstant)


def test_ir_maxconstant_constructor_exists():
    assert callable(ir_MaxConstant.__init__)


def test_ir_maxconstant_constructor_args():
    sig = inspect.signature(ir_MaxConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir_minconstant_is_not_abstract():
    assert not inspect.isabstract(ir_MinConstant)


def test_ir_minconstant_constructor_exists():
    assert callable(ir_MinConstant.__init__)


def test_ir_minconstant_constructor_args():
    sig = inspect.signature(ir_MinConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir_cardinality_is_not_abstract():
    assert not inspect.isabstract(ir_Cardinality)


def test_ir_cardinality_constructor_exists():
    assert callable(ir_Cardinality.__init__)


def test_ir_cardinality_constructor_args():
    sig = inspect.signature(ir_Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_ir_contractedif_is_not_abstract():
    assert not inspect.isabstract(ir_ContractedIf)


def test_ir_contractedif_constructor_exists():
    assert callable(ir_ContractedIf.__init__)


def test_ir_contractedif_constructor_args():
    sig = inspect.signature(ir_ContractedIf.__init__)
    params = list(sig.parameters.keys())



def test_iterableinstruction_is_not_abstract():
    assert not inspect.isabstract(IterableInstruction)


def test_iterableinstruction_constructor_exists():
    assert callable(IterableInstruction.__init__)


def test_iterableinstruction_constructor_args():
    sig = inspect.signature(IterableInstruction.__init__)
    params = list(sig.parameters.keys())



def test_ir_reductioninstruction_is_not_abstract():
    assert not inspect.isabstract(ir_ReductionInstruction)


def test_ir_reductioninstruction_constructor_exists():
    assert callable(ir_ReductionInstruction.__init__)


def test_ir_reductioninstruction_constructor_args():
    sig = inspect.signature(ir_ReductionInstruction.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_ir_return_is_not_abstract():
    assert not inspect.isabstract(ir_Return)


def test_ir_return_constructor_exists():
    assert callable(ir_Return.__init__)


def test_ir_return_constructor_args():
    sig = inspect.signature(ir_Return.__init__)
    params = list(sig.parameters.keys())



def test_ir_exit_is_not_abstract():
    assert not inspect.isabstract(ir_Exit)


def test_ir_exit_constructor_exists():
    assert callable(ir_Exit.__init__)


def test_ir_exit_constructor_args():
    sig = inspect.signature(ir_Exit.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_ir_exit_has_message():
    assert hasattr(ir_Exit, "message")
    descriptor = None
    for klass in ir_Exit.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_ir_iterableinstruction_is_not_abstract():
    assert not inspect.isabstract(ir_IterableInstruction)


def test_ir_iterableinstruction_constructor_exists():
    assert callable(ir_IterableInstruction.__init__)


def test_ir_iterableinstruction_constructor_args():
    sig = inspect.signature(ir_IterableInstruction.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemindexdefinition_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIndexDefinition)


def test_ir_itemindexdefinition_constructor_exists():
    assert callable(ir_ItemIndexDefinition.__init__)


def test_ir_itemindexdefinition_constructor_args():
    sig = inspect.signature(ir_ItemIndexDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir_affectation_is_not_abstract():
    assert not inspect.isabstract(ir_Affectation)


def test_ir_affectation_constructor_exists():
    assert callable(ir_Affectation.__init__)


def test_ir_affectation_constructor_args():
    sig = inspect.signature(ir_Affectation.__init__)
    params = list(sig.parameters.keys())



def test_ir_variabledefinition_is_not_abstract():
    assert not inspect.isabstract(ir_VariableDefinition)


def test_ir_variabledefinition_constructor_exists():
    assert callable(ir_VariableDefinition.__init__)


def test_ir_variabledefinition_constructor_args():
    sig = inspect.signature(ir_VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemiddefinition_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIdDefinition)


def test_ir_itemiddefinition_constructor_exists():
    assert callable(ir_ItemIdDefinition.__init__)


def test_ir_itemiddefinition_constructor_args():
    sig = inspect.signature(ir_ItemIdDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir_setdefinition_is_not_abstract():
    assert not inspect.isabstract(ir_SetDefinition)


def test_ir_setdefinition_constructor_exists():
    assert callable(ir_SetDefinition.__init__)


def test_ir_setdefinition_constructor_args():
    sig = inspect.signature(ir_SetDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_setdefinition_has_name():
    assert hasattr(ir_SetDefinition, "name")
    descriptor = None
    for klass in ir_SetDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_if_is_not_abstract():
    assert not inspect.isabstract(ir_If)


def test_ir_if_constructor_exists():
    assert callable(ir_If.__init__)


def test_ir_if_constructor_args():
    sig = inspect.signature(ir_If.__init__)
    params = list(sig.parameters.keys())



def test_ir_instructionblock_is_not_abstract():
    assert not inspect.isabstract(ir_InstructionBlock)


def test_ir_instructionblock_constructor_exists():
    assert callable(ir_InstructionBlock.__init__)


def test_ir_instructionblock_constructor_args():
    sig = inspect.signature(ir_InstructionBlock.__init__)
    params = list(sig.parameters.keys())



def test_timeloopcopyjob_is_not_abstract():
    assert not inspect.isabstract(TimeLoopCopyJob)


def test_timeloopcopyjob_constructor_exists():
    assert callable(TimeLoopCopyJob.__init__)


def test_timeloopcopyjob_constructor_args():
    sig = inspect.signature(TimeLoopCopyJob.__init__)
    params = list(sig.parameters.keys())



def test_ir_beforetimeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir_BeforeTimeLoopJob)


def test_ir_beforetimeloopjob_constructor_exists():
    assert callable(ir_BeforeTimeLoopJob.__init__)


def test_ir_beforetimeloopjob_constructor_args():
    sig = inspect.signature(ir_BeforeTimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_ir_aftertimeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir_AfterTimeLoopJob)


def test_ir_aftertimeloopjob_constructor_exists():
    assert callable(ir_AfterTimeLoopJob.__init__)


def test_ir_aftertimeloopjob_constructor_args():
    sig = inspect.signature(ir_AfterTimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_job_is_not_abstract():
    assert not inspect.isabstract(Job)


def test_job_constructor_exists():
    assert callable(Job.__init__)


def test_job_constructor_args():
    sig = inspect.signature(Job.__init__)
    params = list(sig.parameters.keys())



def test_ir_timeloopcopyjob_is_not_abstract():
    assert not inspect.isabstract(ir_TimeLoopCopyJob)


def test_ir_timeloopcopyjob_constructor_exists():
    assert callable(ir_TimeLoopCopyJob.__init__)


def test_ir_timeloopcopyjob_constructor_args():
    sig = inspect.signature(ir_TimeLoopCopyJob.__init__)
    params = list(sig.parameters.keys())



def test_ir_instructionjob_is_not_abstract():
    assert not inspect.isabstract(ir_InstructionJob)


def test_ir_instructionjob_constructor_exists():
    assert callable(ir_InstructionJob.__init__)


def test_ir_instructionjob_constructor_args():
    sig = inspect.signature(ir_InstructionJob.__init__)
    params = list(sig.parameters.keys())



def test_ir_loop_is_not_abstract():
    assert not inspect.isabstract(ir_Loop)


def test_ir_loop_constructor_exists():
    assert callable(ir_Loop.__init__)


def test_ir_loop_constructor_args():
    sig = inspect.signature(ir_Loop.__init__)
    params = list(sig.parameters.keys())
    assert "multithreadable" in params, "Missing parameter 'multithreadable'"

def test_ir_loop_has_multithreadable():
    assert hasattr(ir_Loop, "multithreadable")
    descriptor = None
    for klass in ir_Loop.__mro__:
        if "multithreadable" in klass.__dict__:
            descriptor = klass.__dict__["multithreadable"]
            break
    assert isinstance(descriptor, property)



def test_ir_argorvarref_is_not_abstract():
    assert not inspect.isabstract(ir_ArgOrVarRef)


def test_ir_argorvarref_constructor_exists():
    assert callable(ir_ArgOrVarRef.__init__)


def test_ir_argorvarref_constructor_args():
    sig = inspect.signature(ir_ArgOrVarRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_connectivitytype_is_not_abstract():
    assert not inspect.isabstract(ir_ConnectivityType)


def test_ir_connectivitytype_constructor_exists():
    assert callable(ir_ConnectivityType.__init__)


def test_ir_connectivitytype_constructor_args():
    sig = inspect.signature(ir_ConnectivityType.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ir_basetype_is_not_abstract():
    assert not inspect.isabstract(ir_BaseType)


def test_ir_basetype_constructor_exists():
    assert callable(ir_BaseType.__init__)


def test_ir_basetype_constructor_args():
    sig = inspect.signature(ir_BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_ir_basetype_has_primitive():
    assert hasattr(ir_BaseType, "primitive")
    descriptor = None
    for klass in ir_BaseType.__mro__:
        if "primitive" in klass.__dict__:
            descriptor = klass.__dict__["primitive"]
            break
    assert isinstance(descriptor, property)



def test_argorvar_is_not_abstract():
    assert not inspect.isabstract(ArgOrVar)


def test_argorvar_constructor_exists():
    assert callable(ArgOrVar.__init__)


def test_argorvar_constructor_args():
    sig = inspect.signature(ArgOrVar.__init__)
    params = list(sig.parameters.keys())



def test_ir_arg_is_not_abstract():
    assert not inspect.isabstract(ir_Arg)


def test_ir_arg_constructor_exists():
    assert callable(ir_Arg.__init__)


def test_ir_arg_constructor_args():
    sig = inspect.signature(ir_Arg.__init__)
    params = list(sig.parameters.keys())



def test_jobcontainer_is_not_abstract():
    assert not inspect.isabstract(JobContainer)


def test_jobcontainer_constructor_exists():
    assert callable(JobContainer.__init__)


def test_jobcontainer_constructor_args():
    sig = inspect.signature(JobContainer.__init__)
    params = list(sig.parameters.keys())



def test_ir_timeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir_TimeLoopJob)


def test_ir_timeloopjob_constructor_exists():
    assert callable(ir_TimeLoopJob.__init__)


def test_ir_timeloopjob_constructor_args():
    sig = inspect.signature(ir_TimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_ir_irmodule_is_not_abstract():
    assert not inspect.isabstract(ir_IrModule)


def test_ir_irmodule_constructor_exists():
    assert callable(ir_IrModule.__init__)


def test_ir_irmodule_constructor_args():
    sig = inspect.signature(ir_IrModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_irmodule_has_name():
    assert hasattr(ir_IrModule, "name")
    descriptor = None
    for klass in ir_IrModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_connectivityvariable_is_not_abstract():
    assert not inspect.isabstract(ir_ConnectivityVariable)


def test_ir_connectivityvariable_constructor_exists():
    assert callable(ir_ConnectivityVariable.__init__)


def test_ir_connectivityvariable_constructor_args():
    sig = inspect.signature(ir_ConnectivityVariable.__init__)
    params = list(sig.parameters.keys())



def test_ir_variable_is_not_abstract():
    assert not inspect.isabstract(ir_Variable)


def test_ir_variable_constructor_exists():
    assert callable(ir_Variable.__init__)


def test_ir_variable_constructor_args():
    sig = inspect.signature(ir_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"
    assert "persistenceName" in params, "Missing parameter 'persistenceName'"

def test_ir_variable_has_const():
    assert hasattr(ir_Variable, "const")
    descriptor = None
    for klass in ir_Variable.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)

def test_ir_variable_has_persistenceName():
    assert hasattr(ir_Variable, "persistenceName")
    descriptor = None
    for klass in ir_Variable.__mro__:
        if "persistenceName" in klass.__dict__:
            descriptor = klass.__dict__["persistenceName"]
            break
    assert isinstance(descriptor, property)



def test_ir_simplevariable_is_not_abstract():
    assert not inspect.isabstract(ir_SimpleVariable)


def test_ir_simplevariable_constructor_exists():
    assert callable(ir_SimpleVariable.__init__)


def test_ir_simplevariable_constructor_args():
    sig = inspect.signature(ir_SimpleVariable.__init__)
    params = list(sig.parameters.keys())



def test_irannotable_is_not_abstract():
    assert not inspect.isabstract(IrAnnotable)


def test_irannotable_constructor_exists():
    assert callable(IrAnnotable.__init__)


def test_irannotable_constructor_args():
    sig = inspect.signature(IrAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_ir_import_is_not_abstract():
    assert not inspect.isabstract(ir_Import)


def test_ir_import_constructor_exists():
    assert callable(ir_Import.__init__)


def test_ir_import_constructor_args():
    sig = inspect.signature(ir_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ir_import_has_importedNamespace():
    assert hasattr(ir_Import, "importedNamespace")
    descriptor = None
    for klass in ir_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ir_timeloopcopy_is_not_abstract():
    assert not inspect.isabstract(ir_TimeLoopCopy)


def test_ir_timeloopcopy_constructor_exists():
    assert callable(ir_TimeLoopCopy.__init__)


def test_ir_timeloopcopy_constructor_args():
    sig = inspect.signature(ir_TimeLoopCopy.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemtype_is_not_abstract():
    assert not inspect.isabstract(ir_ItemType)


def test_ir_itemtype_constructor_exists():
    assert callable(ir_ItemType.__init__)


def test_ir_itemtype_constructor_args():
    sig = inspect.signature(ir_ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_itemtype_has_name():
    assert hasattr(ir_ItemType, "name")
    descriptor = None
    for klass in ir_ItemType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_connectivity_is_not_abstract():
    assert not inspect.isabstract(ir_Connectivity)


def test_ir_connectivity_constructor_exists():
    assert callable(ir_Connectivity.__init__)


def test_ir_connectivity_constructor_args():
    sig = inspect.signature(ir_Connectivity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "indexEqualId" in params, "Missing parameter 'indexEqualId'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_ir_connectivity_has_name():
    assert hasattr(ir_Connectivity, "name")
    descriptor = None
    for klass in ir_Connectivity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir_connectivity_has_indexEqualId():
    assert hasattr(ir_Connectivity, "indexEqualId")
    descriptor = None
    for klass in ir_Connectivity.__mro__:
        if "indexEqualId" in klass.__dict__:
            descriptor = klass.__dict__["indexEqualId"]
            break
    assert isinstance(descriptor, property)

def test_ir_connectivity_has_multiple():
    assert hasattr(ir_Connectivity, "multiple")
    descriptor = None
    for klass in ir_Connectivity.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_ir_iterationblock_is_not_abstract():
    assert not inspect.isabstract(ir_IterationBlock)


def test_ir_iterationblock_constructor_exists():
    assert callable(ir_IterationBlock.__init__)


def test_ir_iterationblock_constructor_args():
    sig = inspect.signature(ir_IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemindexvalue_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIndexValue)


def test_ir_itemindexvalue_constructor_exists():
    assert callable(ir_ItemIndexValue.__init__)


def test_ir_itemindexvalue_constructor_args():
    sig = inspect.signature(ir_ItemIndexValue.__init__)
    params = list(sig.parameters.keys())



def test_ir_container_is_not_abstract():
    assert not inspect.isabstract(ir_Container)


def test_ir_container_constructor_exists():
    assert callable(ir_Container.__init__)


def test_ir_container_constructor_args():
    sig = inspect.signature(ir_Container.__init__)
    params = list(sig.parameters.keys())



def test_ir_function_is_not_abstract():
    assert not inspect.isabstract(ir_Function)


def test_ir_function_constructor_exists():
    assert callable(ir_Function.__init__)


def test_ir_function_constructor_args():
    sig = inspect.signature(ir_Function.__init__)
    params = list(sig.parameters.keys())
    assert "provider" in params, "Missing parameter 'provider'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir_function_has_provider():
    assert hasattr(ir_Function, "provider")
    descriptor = None
    for klass in ir_Function.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)

def test_ir_function_has_name():
    assert hasattr(ir_Function, "name")
    descriptor = None
    for klass in ir_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_job_is_not_abstract():
    assert not inspect.isabstract(ir_Job)


def test_ir_job_constructor_exists():
    assert callable(ir_Job.__init__)


def test_ir_job_constructor_args():
    sig = inspect.signature(ir_Job.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "at" in params, "Missing parameter 'at'"
    assert "onCycle" in params, "Missing parameter 'onCycle'"

def test_ir_job_has_name():
    assert hasattr(ir_Job, "name")
    descriptor = None
    for klass in ir_Job.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir_job_has_at():
    assert hasattr(ir_Job, "at")
    descriptor = None
    for klass in ir_Job.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)

def test_ir_job_has_onCycle():
    assert hasattr(ir_Job, "onCycle")
    descriptor = None
    for klass in ir_Job.__mro__:
        if "onCycle" in klass.__dict__:
            descriptor = klass.__dict__["onCycle"]
            break
    assert isinstance(descriptor, property)



def test_ir_itemidvalue_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIdValue)


def test_ir_itemidvalue_constructor_exists():
    assert callable(ir_ItemIdValue.__init__)


def test_ir_itemidvalue_constructor_args():
    sig = inspect.signature(ir_ItemIdValue.__init__)
    params = list(sig.parameters.keys())



def test_ir_instruction_is_not_abstract():
    assert not inspect.isabstract(ir_Instruction)


def test_ir_instruction_constructor_exists():
    assert callable(ir_Instruction.__init__)


def test_ir_instruction_constructor_args():
    sig = inspect.signature(ir_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_ir_itemid_is_not_abstract():
    assert not inspect.isabstract(ir_ItemId)


def test_ir_itemid_constructor_exists():
    assert callable(ir_ItemId.__init__)


def test_ir_itemid_constructor_args():
    sig = inspect.signature(ir_ItemId.__init__)
    params = list(sig.parameters.keys())
    assert "itemName" in params, "Missing parameter 'itemName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir_itemid_has_itemName():
    assert hasattr(ir_ItemId, "itemName")
    descriptor = None
    for klass in ir_ItemId.__mro__:
        if "itemName" in klass.__dict__:
            descriptor = klass.__dict__["itemName"]
            break
    assert isinstance(descriptor, property)

def test_ir_itemid_has_name():
    assert hasattr(ir_ItemId, "name")
    descriptor = None
    for klass in ir_ItemId.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_itemindex_is_not_abstract():
    assert not inspect.isabstract(ir_ItemIndex)


def test_ir_itemindex_constructor_exists():
    assert callable(ir_ItemIndex.__init__)


def test_ir_itemindex_constructor_args():
    sig = inspect.signature(ir_ItemIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "itemName" in params, "Missing parameter 'itemName'"

def test_ir_itemindex_has_name():
    assert hasattr(ir_ItemIndex, "name")
    descriptor = None
    for klass in ir_ItemIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir_itemindex_has_itemName():
    assert hasattr(ir_ItemIndex, "itemName")
    descriptor = None
    for klass in ir_ItemIndex.__mro__:
        if "itemName" in klass.__dict__:
            descriptor = klass.__dict__["itemName"]
            break
    assert isinstance(descriptor, property)



def test_ir_postprocessinginfo_is_not_abstract():
    assert not inspect.isabstract(ir_PostProcessingInfo)


def test_ir_postprocessinginfo_constructor_exists():
    assert callable(ir_PostProcessingInfo.__init__)


def test_ir_postprocessinginfo_constructor_args():
    sig = inspect.signature(ir_PostProcessingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "periodValue" in params, "Missing parameter 'periodValue'"

def test_ir_postprocessinginfo_has_periodValue():
    assert hasattr(ir_PostProcessingInfo, "periodValue")
    descriptor = None
    for klass in ir_PostProcessingInfo.__mro__:
        if "periodValue" in klass.__dict__:
            descriptor = klass.__dict__["periodValue"]
            break
    assert isinstance(descriptor, property)



def test_ir_timeloopvariable_is_not_abstract():
    assert not inspect.isabstract(ir_TimeLoopVariable)


def test_ir_timeloopvariable_constructor_exists():
    assert callable(ir_TimeLoopVariable.__init__)


def test_ir_timeloopvariable_constructor_args():
    sig = inspect.signature(ir_TimeLoopVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_timeloopvariable_has_name():
    assert hasattr(ir_TimeLoopVariable, "name")
    descriptor = None
    for klass in ir_TimeLoopVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_argorvar_is_not_abstract():
    assert not inspect.isabstract(ir_ArgOrVar)


def test_ir_argorvar_constructor_exists():
    assert callable(ir_ArgOrVar.__init__)


def test_ir_argorvar_constructor_args():
    sig = inspect.signature(ir_ArgOrVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_argorvar_has_name():
    assert hasattr(ir_ArgOrVar, "name")
    descriptor = None
    for klass in ir_ArgOrVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_timeloop_is_not_abstract():
    assert not inspect.isabstract(ir_TimeLoop)


def test_ir_timeloop_constructor_exists():
    assert callable(ir_TimeLoop.__init__)


def test_ir_timeloop_constructor_args():
    sig = inspect.signature(ir_TimeLoop.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_timeloop_has_name():
    assert hasattr(ir_TimeLoop, "name")
    descriptor = None
    for klass in ir_TimeLoop.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_irtype_is_not_abstract():
    assert not inspect.isabstract(ir_IrType)


def test_ir_irtype_constructor_exists():
    assert callable(ir_IrType.__init__)


def test_ir_irtype_constructor_args():
    sig = inspect.signature(ir_IrType.__init__)
    params = list(sig.parameters.keys())



def test_ir_expression_is_not_abstract():
    assert not inspect.isabstract(ir_Expression)


def test_ir_expression_constructor_exists():
    assert callable(ir_Expression.__init__)


def test_ir_expression_constructor_args():
    sig = inspect.signature(ir_Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir_jobcontainer_is_not_abstract():
    assert not inspect.isabstract(ir_JobContainer)


def test_ir_jobcontainer_constructor_exists():
    assert callable(ir_JobContainer.__init__)


def test_ir_jobcontainer_constructor_args():
    sig = inspect.signature(ir_JobContainer.__init__)
    params = list(sig.parameters.keys())



def test_ir_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ir_EStringToStringMapEntry)


def test_ir_estringtostringmapentry_constructor_exists():
    assert callable(ir_EStringToStringMapEntry.__init__)


def test_ir_estringtostringmapentry_constructor_args():
    sig = inspect.signature(ir_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ir_irannotation_is_not_abstract():
    assert not inspect.isabstract(ir_IrAnnotation)


def test_ir_irannotation_constructor_exists():
    assert callable(ir_IrAnnotation.__init__)


def test_ir_irannotation_constructor_args():
    sig = inspect.signature(ir_IrAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_ir_irannotation_has_source():
    assert hasattr(ir_IrAnnotation, "source")
    descriptor = None
    for klass in ir_IrAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_ir_irannotable_is_not_abstract():
    assert not inspect.isabstract(ir_IrAnnotable)


def test_ir_irannotable_constructor_exists():
    assert callable(ir_IrAnnotable.__init__)


def test_ir_irannotable_constructor_args():
    sig = inspect.signature(ir_IrAnnotable.__init__)
    params = list(sig.parameters.keys())

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "Real",
        "Bool",
        "Int",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"


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
ItemIdValue_strategy = st.builds(
    ItemIdValue,
)
ir_ItemIdValueCall_strategy = st.builds(
    ir_ItemIdValueCall,
)
ir_ItemIdValueIterator_strategy = st.builds(
    ir_ItemIdValueIterator,
    shift=
        st.integers()
)
Container_strategy = st.builds(
    Container,
)
ir_SetRef_strategy = st.builds(
    ir_SetRef,
)
IrType_strategy = st.builds(
    IrType,
)
IterationBlock_strategy = st.builds(
    IterationBlock,
)
ir_Interval_strategy = st.builds(
    ir_Interval,
)
ir_Iterator_strategy = st.builds(
    ir_Iterator,
)
ir_ConnectivityCall_strategy = st.builds(
    ir_ConnectivityCall,
)
Expression_strategy = st.builds(
    Expression,
)
ir_RealConstant_strategy = st.builds(
    ir_RealConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir_Parenthesis_strategy = st.builds(
    ir_Parenthesis,
)
ir_BoolConstant_strategy = st.builds(
    ir_BoolConstant,
    value=
        st.booleans()
)
ir_FunctionCall_strategy = st.builds(
    ir_FunctionCall,
)
ir_BinaryExpression_strategy = st.builds(
    ir_BinaryExpression,
    operator=
        safe_text
)
ir_UnaryExpression_strategy = st.builds(
    ir_UnaryExpression,
    operator=
        safe_text
)
ir_VectorConstant_strategy = st.builds(
    ir_VectorConstant,
)
ir_IntConstant_strategy = st.builds(
    ir_IntConstant,
    value=
        st.integers()
)
ir_BaseTypeConstant_strategy = st.builds(
    ir_BaseTypeConstant,
)
ir_MaxConstant_strategy = st.builds(
    ir_MaxConstant,
)
ir_MinConstant_strategy = st.builds(
    ir_MinConstant,
)
ir_Cardinality_strategy = st.builds(
    ir_Cardinality,
)
ir_ContractedIf_strategy = st.builds(
    ir_ContractedIf,
)
IterableInstruction_strategy = st.builds(
    IterableInstruction,
)
ir_ReductionInstruction_strategy = st.builds(
    ir_ReductionInstruction,
)
Instruction_strategy = st.builds(
    Instruction,
)
ir_Return_strategy = st.builds(
    ir_Return,
)
ir_Exit_strategy = st.builds(
    ir_Exit,
    message=
        safe_text
)
ir_IterableInstruction_strategy = st.builds(
    ir_IterableInstruction,
)
ir_ItemIndexDefinition_strategy = st.builds(
    ir_ItemIndexDefinition,
)
ir_Affectation_strategy = st.builds(
    ir_Affectation,
)
ir_VariableDefinition_strategy = st.builds(
    ir_VariableDefinition,
)
ir_ItemIdDefinition_strategy = st.builds(
    ir_ItemIdDefinition,
)
ir_SetDefinition_strategy = st.builds(
    ir_SetDefinition,
    name=
        safe_text
)
ir_If_strategy = st.builds(
    ir_If,
)
ir_InstructionBlock_strategy = st.builds(
    ir_InstructionBlock,
)
TimeLoopCopyJob_strategy = st.builds(
    TimeLoopCopyJob,
)
ir_BeforeTimeLoopJob_strategy = st.builds(
    ir_BeforeTimeLoopJob,
)
ir_AfterTimeLoopJob_strategy = st.builds(
    ir_AfterTimeLoopJob,
)
Job_strategy = st.builds(
    Job,
)
ir_TimeLoopCopyJob_strategy = st.builds(
    ir_TimeLoopCopyJob,
)
ir_InstructionJob_strategy = st.builds(
    ir_InstructionJob,
)
ir_Loop_strategy = st.builds(
    ir_Loop,
    multithreadable=
        st.booleans()
)
ir_ArgOrVarRef_strategy = st.builds(
    ir_ArgOrVarRef,
)
ir_ConnectivityType_strategy = st.builds(
    ir_ConnectivityType,
)
Variable_strategy = st.builds(
    Variable,
)
ir_BaseType_strategy = st.builds(
    ir_BaseType,
    primitive=
        safe_text
)
ArgOrVar_strategy = st.builds(
    ArgOrVar,
)
ir_Arg_strategy = st.builds(
    ir_Arg,
)
JobContainer_strategy = st.builds(
    JobContainer,
)
ir_TimeLoopJob_strategy = st.builds(
    ir_TimeLoopJob,
)
ir_IrModule_strategy = st.builds(
    ir_IrModule,
    name=
        safe_text
)
ir_ConnectivityVariable_strategy = st.builds(
    ir_ConnectivityVariable,
)
ir_Variable_strategy = st.builds(
    ir_Variable,
    const=
        st.booleans(),
    persistenceName=
        safe_text
)
ir_SimpleVariable_strategy = st.builds(
    ir_SimpleVariable,
)
IrAnnotable_strategy = st.builds(
    IrAnnotable,
)
ir_Import_strategy = st.builds(
    ir_Import,
    importedNamespace=
        safe_text
)
ir_TimeLoopCopy_strategy = st.builds(
    ir_TimeLoopCopy,
)
ir_ItemType_strategy = st.builds(
    ir_ItemType,
    name=
        safe_text
)
ir_Connectivity_strategy = st.builds(
    ir_Connectivity,
    name=
        safe_text,
    indexEqualId=
        st.booleans(),
    multiple=
        st.booleans()
)
ir_IterationBlock_strategy = st.builds(
    ir_IterationBlock,
)
ir_ItemIndexValue_strategy = st.builds(
    ir_ItemIndexValue,
)
ir_Container_strategy = st.builds(
    ir_Container,
)
ir_Function_strategy = st.builds(
    ir_Function,
    provider=
        safe_text,
    name=
        safe_text
)
ir_Job_strategy = st.builds(
    ir_Job,
    name=
        safe_text,
    at=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    onCycle=
        st.booleans()
)
ir_ItemIdValue_strategy = st.builds(
    ir_ItemIdValue,
)
ir_Instruction_strategy = st.builds(
    ir_Instruction,
)
ir_ItemId_strategy = st.builds(
    ir_ItemId,
    itemName=
        safe_text,
    name=
        safe_text
)
ir_ItemIndex_strategy = st.builds(
    ir_ItemIndex,
    name=
        safe_text,
    itemName=
        safe_text
)
ir_PostProcessingInfo_strategy = st.builds(
    ir_PostProcessingInfo,
    periodValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir_TimeLoopVariable_strategy = st.builds(
    ir_TimeLoopVariable,
    name=
        safe_text
)
ir_ArgOrVar_strategy = st.builds(
    ir_ArgOrVar,
    name=
        safe_text
)
ir_TimeLoop_strategy = st.builds(
    ir_TimeLoop,
    name=
        safe_text
)
ir_IrType_strategy = st.builds(
    ir_IrType,
)
ir_Expression_strategy = st.builds(
    ir_Expression,
)
ir_JobContainer_strategy = st.builds(
    ir_JobContainer,
)
ir_EStringToStringMapEntry_strategy = st.builds(
    ir_EStringToStringMapEntry,
)
ir_IrAnnotation_strategy = st.builds(
    ir_IrAnnotation,
    source=
        safe_text
)
ir_IrAnnotable_strategy = st.builds(
    ir_IrAnnotable,
)

@given(instance=ItemIdValue_strategy)
@settings(max_examples=50)
def test_itemidvalue_instantiation(instance):
    assert isinstance(instance, ItemIdValue)

@given(instance=ir_ItemIdValueCall_strategy)
@settings(max_examples=50)
def test_ir_itemidvaluecall_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValueCall)

@given(instance=ir_ItemIdValueIterator_strategy)
@settings(max_examples=50)
def test_ir_itemidvalueiterator_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValueIterator)



@given(instance=ir_ItemIdValueIterator_strategy)
def test_ir_itemidvalueiterator_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=ir_SetRef_strategy)
@settings(max_examples=50)
def test_ir_setref_instantiation(instance):
    assert isinstance(instance, ir_SetRef)

@given(instance=IrType_strategy)
@settings(max_examples=50)
def test_irtype_instantiation(instance):
    assert isinstance(instance, IrType)

@given(instance=IterationBlock_strategy)
@settings(max_examples=50)
def test_iterationblock_instantiation(instance):
    assert isinstance(instance, IterationBlock)

@given(instance=ir_Interval_strategy)
@settings(max_examples=50)
def test_ir_interval_instantiation(instance):
    assert isinstance(instance, ir_Interval)

@given(instance=ir_Iterator_strategy)
@settings(max_examples=50)
def test_ir_iterator_instantiation(instance):
    assert isinstance(instance, ir_Iterator)

@given(instance=ir_ConnectivityCall_strategy)
@settings(max_examples=50)
def test_ir_connectivitycall_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityCall)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ir_RealConstant_strategy)
@settings(max_examples=50)
def test_ir_realconstant_instantiation(instance):
    assert isinstance(instance, ir_RealConstant)



@given(instance=ir_RealConstant_strategy)
def test_ir_realconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_Parenthesis_strategy)
@settings(max_examples=50)
def test_ir_parenthesis_instantiation(instance):
    assert isinstance(instance, ir_Parenthesis)

@given(instance=ir_BoolConstant_strategy)
@settings(max_examples=50)
def test_ir_boolconstant_instantiation(instance):
    assert isinstance(instance, ir_BoolConstant)



@given(instance=ir_BoolConstant_strategy)
def test_ir_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_FunctionCall_strategy)
@settings(max_examples=50)
def test_ir_functioncall_instantiation(instance):
    assert isinstance(instance, ir_FunctionCall)

@given(instance=ir_BinaryExpression_strategy)
@settings(max_examples=50)
def test_ir_binaryexpression_instantiation(instance):
    assert isinstance(instance, ir_BinaryExpression)



@given(instance=ir_BinaryExpression_strategy)
def test_ir_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir_UnaryExpression_strategy)
@settings(max_examples=50)
def test_ir_unaryexpression_instantiation(instance):
    assert isinstance(instance, ir_UnaryExpression)



@given(instance=ir_UnaryExpression_strategy)
def test_ir_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir_VectorConstant_strategy)
@settings(max_examples=50)
def test_ir_vectorconstant_instantiation(instance):
    assert isinstance(instance, ir_VectorConstant)

@given(instance=ir_IntConstant_strategy)
@settings(max_examples=50)
def test_ir_intconstant_instantiation(instance):
    assert isinstance(instance, ir_IntConstant)



@given(instance=ir_IntConstant_strategy)
def test_ir_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_BaseTypeConstant_strategy)
@settings(max_examples=50)
def test_ir_basetypeconstant_instantiation(instance):
    assert isinstance(instance, ir_BaseTypeConstant)

@given(instance=ir_MaxConstant_strategy)
@settings(max_examples=50)
def test_ir_maxconstant_instantiation(instance):
    assert isinstance(instance, ir_MaxConstant)

@given(instance=ir_MinConstant_strategy)
@settings(max_examples=50)
def test_ir_minconstant_instantiation(instance):
    assert isinstance(instance, ir_MinConstant)

@given(instance=ir_Cardinality_strategy)
@settings(max_examples=50)
def test_ir_cardinality_instantiation(instance):
    assert isinstance(instance, ir_Cardinality)

@given(instance=ir_ContractedIf_strategy)
@settings(max_examples=50)
def test_ir_contractedif_instantiation(instance):
    assert isinstance(instance, ir_ContractedIf)

@given(instance=IterableInstruction_strategy)
@settings(max_examples=50)
def test_iterableinstruction_instantiation(instance):
    assert isinstance(instance, IterableInstruction)

@given(instance=ir_ReductionInstruction_strategy)
@settings(max_examples=50)
def test_ir_reductioninstruction_instantiation(instance):
    assert isinstance(instance, ir_ReductionInstruction)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=ir_Return_strategy)
@settings(max_examples=50)
def test_ir_return_instantiation(instance):
    assert isinstance(instance, ir_Return)

@given(instance=ir_Exit_strategy)
@settings(max_examples=50)
def test_ir_exit_instantiation(instance):
    assert isinstance(instance, ir_Exit)



@given(instance=ir_Exit_strategy)
def test_ir_exit_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=ir_IterableInstruction_strategy)
@settings(max_examples=50)
def test_ir_iterableinstruction_instantiation(instance):
    assert isinstance(instance, ir_IterableInstruction)

@given(instance=ir_ItemIndexDefinition_strategy)
@settings(max_examples=50)
def test_ir_itemindexdefinition_instantiation(instance):
    assert isinstance(instance, ir_ItemIndexDefinition)

@given(instance=ir_Affectation_strategy)
@settings(max_examples=50)
def test_ir_affectation_instantiation(instance):
    assert isinstance(instance, ir_Affectation)

@given(instance=ir_VariableDefinition_strategy)
@settings(max_examples=50)
def test_ir_variabledefinition_instantiation(instance):
    assert isinstance(instance, ir_VariableDefinition)

@given(instance=ir_ItemIdDefinition_strategy)
@settings(max_examples=50)
def test_ir_itemiddefinition_instantiation(instance):
    assert isinstance(instance, ir_ItemIdDefinition)

@given(instance=ir_SetDefinition_strategy)
@settings(max_examples=50)
def test_ir_setdefinition_instantiation(instance):
    assert isinstance(instance, ir_SetDefinition)



@given(instance=ir_SetDefinition_strategy)
def test_ir_setdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_If_strategy)
@settings(max_examples=50)
def test_ir_if_instantiation(instance):
    assert isinstance(instance, ir_If)

@given(instance=ir_InstructionBlock_strategy)
@settings(max_examples=50)
def test_ir_instructionblock_instantiation(instance):
    assert isinstance(instance, ir_InstructionBlock)

@given(instance=TimeLoopCopyJob_strategy)
@settings(max_examples=50)
def test_timeloopcopyjob_instantiation(instance):
    assert isinstance(instance, TimeLoopCopyJob)

@given(instance=ir_BeforeTimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir_beforetimeloopjob_instantiation(instance):
    assert isinstance(instance, ir_BeforeTimeLoopJob)

@given(instance=ir_AfterTimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir_aftertimeloopjob_instantiation(instance):
    assert isinstance(instance, ir_AfterTimeLoopJob)

@given(instance=Job_strategy)
@settings(max_examples=50)
def test_job_instantiation(instance):
    assert isinstance(instance, Job)

@given(instance=ir_TimeLoopCopyJob_strategy)
@settings(max_examples=50)
def test_ir_timeloopcopyjob_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopCopyJob)

@given(instance=ir_InstructionJob_strategy)
@settings(max_examples=50)
def test_ir_instructionjob_instantiation(instance):
    assert isinstance(instance, ir_InstructionJob)

@given(instance=ir_Loop_strategy)
@settings(max_examples=50)
def test_ir_loop_instantiation(instance):
    assert isinstance(instance, ir_Loop)



@given(instance=ir_Loop_strategy)
def test_ir_loop_multithreadable_setter(instance):
    original = instance.multithreadable
    instance.multithreadable = original
    assert instance.multithreadable == original

@given(instance=ir_ArgOrVarRef_strategy)
@settings(max_examples=50)
def test_ir_argorvarref_instantiation(instance):
    assert isinstance(instance, ir_ArgOrVarRef)

@given(instance=ir_ConnectivityType_strategy)
@settings(max_examples=50)
def test_ir_connectivitytype_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityType)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ir_BaseType_strategy)
@settings(max_examples=50)
def test_ir_basetype_instantiation(instance):
    assert isinstance(instance, ir_BaseType)



@given(instance=ir_BaseType_strategy)
def test_ir_basetype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=ArgOrVar_strategy)
@settings(max_examples=50)
def test_argorvar_instantiation(instance):
    assert isinstance(instance, ArgOrVar)

@given(instance=ir_Arg_strategy)
@settings(max_examples=50)
def test_ir_arg_instantiation(instance):
    assert isinstance(instance, ir_Arg)

@given(instance=JobContainer_strategy)
@settings(max_examples=50)
def test_jobcontainer_instantiation(instance):
    assert isinstance(instance, JobContainer)

@given(instance=ir_TimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir_timeloopjob_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopJob)

@given(instance=ir_IrModule_strategy)
@settings(max_examples=50)
def test_ir_irmodule_instantiation(instance):
    assert isinstance(instance, ir_IrModule)



@given(instance=ir_IrModule_strategy)
def test_ir_irmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_ConnectivityVariable_strategy)
@settings(max_examples=50)
def test_ir_connectivityvariable_instantiation(instance):
    assert isinstance(instance, ir_ConnectivityVariable)

@given(instance=ir_Variable_strategy)
@settings(max_examples=50)
def test_ir_variable_instantiation(instance):
    assert isinstance(instance, ir_Variable)



@given(instance=ir_Variable_strategy)
def test_ir_variable_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original



@given(instance=ir_Variable_strategy)
def test_ir_variable_persistenceName_setter(instance):
    original = instance.persistenceName
    instance.persistenceName = original
    assert instance.persistenceName == original

@given(instance=ir_SimpleVariable_strategy)
@settings(max_examples=50)
def test_ir_simplevariable_instantiation(instance):
    assert isinstance(instance, ir_SimpleVariable)

@given(instance=IrAnnotable_strategy)
@settings(max_examples=50)
def test_irannotable_instantiation(instance):
    assert isinstance(instance, IrAnnotable)

@given(instance=ir_Import_strategy)
@settings(max_examples=50)
def test_ir_import_instantiation(instance):
    assert isinstance(instance, ir_Import)



@given(instance=ir_Import_strategy)
def test_ir_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ir_TimeLoopCopy_strategy)
@settings(max_examples=50)
def test_ir_timeloopcopy_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopCopy)

@given(instance=ir_ItemType_strategy)
@settings(max_examples=50)
def test_ir_itemtype_instantiation(instance):
    assert isinstance(instance, ir_ItemType)



@given(instance=ir_ItemType_strategy)
def test_ir_itemtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_Connectivity_strategy)
@settings(max_examples=50)
def test_ir_connectivity_instantiation(instance):
    assert isinstance(instance, ir_Connectivity)



@given(instance=ir_Connectivity_strategy)
def test_ir_connectivity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ir_Connectivity_strategy)
def test_ir_connectivity_indexEqualId_setter(instance):
    original = instance.indexEqualId
    instance.indexEqualId = original
    assert instance.indexEqualId == original



@given(instance=ir_Connectivity_strategy)
def test_ir_connectivity_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ir_IterationBlock_strategy)
@settings(max_examples=50)
def test_ir_iterationblock_instantiation(instance):
    assert isinstance(instance, ir_IterationBlock)

@given(instance=ir_ItemIndexValue_strategy)
@settings(max_examples=50)
def test_ir_itemindexvalue_instantiation(instance):
    assert isinstance(instance, ir_ItemIndexValue)

@given(instance=ir_Container_strategy)
@settings(max_examples=50)
def test_ir_container_instantiation(instance):
    assert isinstance(instance, ir_Container)

@given(instance=ir_Function_strategy)
@settings(max_examples=50)
def test_ir_function_instantiation(instance):
    assert isinstance(instance, ir_Function)



@given(instance=ir_Function_strategy)
def test_ir_function_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original



@given(instance=ir_Function_strategy)
def test_ir_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_Job_strategy)
@settings(max_examples=50)
def test_ir_job_instantiation(instance):
    assert isinstance(instance, ir_Job)



@given(instance=ir_Job_strategy)
def test_ir_job_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ir_Job_strategy)
def test_ir_job_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original



@given(instance=ir_Job_strategy)
def test_ir_job_onCycle_setter(instance):
    original = instance.onCycle
    instance.onCycle = original
    assert instance.onCycle == original

@given(instance=ir_ItemIdValue_strategy)
@settings(max_examples=50)
def test_ir_itemidvalue_instantiation(instance):
    assert isinstance(instance, ir_ItemIdValue)

@given(instance=ir_Instruction_strategy)
@settings(max_examples=50)
def test_ir_instruction_instantiation(instance):
    assert isinstance(instance, ir_Instruction)

@given(instance=ir_ItemId_strategy)
@settings(max_examples=50)
def test_ir_itemid_instantiation(instance):
    assert isinstance(instance, ir_ItemId)



@given(instance=ir_ItemId_strategy)
def test_ir_itemid_itemName_setter(instance):
    original = instance.itemName
    instance.itemName = original
    assert instance.itemName == original



@given(instance=ir_ItemId_strategy)
def test_ir_itemid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_ItemIndex_strategy)
@settings(max_examples=50)
def test_ir_itemindex_instantiation(instance):
    assert isinstance(instance, ir_ItemIndex)



@given(instance=ir_ItemIndex_strategy)
def test_ir_itemindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ir_ItemIndex_strategy)
def test_ir_itemindex_itemName_setter(instance):
    original = instance.itemName
    instance.itemName = original
    assert instance.itemName == original

@given(instance=ir_PostProcessingInfo_strategy)
@settings(max_examples=50)
def test_ir_postprocessinginfo_instantiation(instance):
    assert isinstance(instance, ir_PostProcessingInfo)



@given(instance=ir_PostProcessingInfo_strategy)
def test_ir_postprocessinginfo_periodValue_setter(instance):
    original = instance.periodValue
    instance.periodValue = original
    assert instance.periodValue == original

@given(instance=ir_TimeLoopVariable_strategy)
@settings(max_examples=50)
def test_ir_timeloopvariable_instantiation(instance):
    assert isinstance(instance, ir_TimeLoopVariable)



@given(instance=ir_TimeLoopVariable_strategy)
def test_ir_timeloopvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_ArgOrVar_strategy)
@settings(max_examples=50)
def test_ir_argorvar_instantiation(instance):
    assert isinstance(instance, ir_ArgOrVar)



@given(instance=ir_ArgOrVar_strategy)
def test_ir_argorvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_TimeLoop_strategy)
@settings(max_examples=50)
def test_ir_timeloop_instantiation(instance):
    assert isinstance(instance, ir_TimeLoop)



@given(instance=ir_TimeLoop_strategy)
def test_ir_timeloop_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_IrType_strategy)
@settings(max_examples=50)
def test_ir_irtype_instantiation(instance):
    assert isinstance(instance, ir_IrType)

@given(instance=ir_Expression_strategy)
@settings(max_examples=50)
def test_ir_expression_instantiation(instance):
    assert isinstance(instance, ir_Expression)

@given(instance=ir_JobContainer_strategy)
@settings(max_examples=50)
def test_ir_jobcontainer_instantiation(instance):
    assert isinstance(instance, ir_JobContainer)

@given(instance=ir_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ir_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ir_EStringToStringMapEntry)

@given(instance=ir_IrAnnotation_strategy)
@settings(max_examples=50)
def test_ir_irannotation_instantiation(instance):
    assert isinstance(instance, ir_IrAnnotation)



@given(instance=ir_IrAnnotation_strategy)
def test_ir_irannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=ir_IrAnnotable_strategy)
@settings(max_examples=50)
def test_ir_irannotable_instantiation(instance):
    assert isinstance(instance, ir_IrAnnotable)
