import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    ir::ContractedIf,
    IterableInstruction,
    ir::ReductionInstruction,
    Instruction,
    ir::SetDefinition,
    ir::VariableDefinition,
    ir::ItemIdDefinition,
    ir::ItemIndexDefinition,
    ir::Affectation,
    ir::IterableInstruction,
    ir::InstructionBlock,
    TimeLoopCopyJob,
    ir::BeforeTimeLoopJob,
    ir::AfterTimeLoopJob,
    ItemIdValue,
    ir::ItemIdValueCall,
    ir::ItemIdValueIterator,
    Container,
    ir::SetRef,
    ir::ConnectivityCall,
    IrType,
    ir::VectorConstant,
    ir::BaseTypeConstant,
    ir::FunctionCall,
    ir::MaxConstant,
    ir::MinConstant,
    ir::BoolConstant,
    ir::RealConstant,
    ir::IntConstant,
    ir::Parenthesis,
    ir::UnaryExpression,
    ir::BinaryExpression,
    ir::Cardinality,
    IterationBlock,
    ir::Interval,
    ir::Iterator,
    ir::Exit,
    ir::Return,
    ir::If,
    Job,
    ir::TimeLoopCopyJob,
    ir::InstructionJob,
    ir::Loop,
    ir::ArgOrVarRef,
    ir::ConnectivityType,
    Variable,
    ir::BaseType,
    ArgOrVar,
    ir::Arg,
    JobContainer,
    ir::TimeLoopJob,
    ir::IrModule,
    ir::ConnectivityVariable,
    ir::Variable,
    ir::SimpleVariable,
    IrAnnotable,
    ir::IterationBlock,
    ir::TimeLoopVariable,
    ir::ItemId,
    ir::IrType,
    ir::Container,
    ir::Instruction,
    ir::ArgOrVar,
    ir::Import,
    ir::ItemType,
    ir::TimeLoopCopy,
    ir::PostProcessingInfo,
    ir::Connectivity,
    ir::Expression,
    ir::Job,
    ir::Function,
    ir::ItemIndexValue,
    ir::ItemIdValue,
    ir::TimeLoop,
    ir::ItemIndex,
    ir::JobContainer,
    ir::EStringToStringMapEntry,
    ir::IrAnnotation,
    ir::IrAnnotable,
    PrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir::contractedif_is_not_abstract():
    assert not inspect.isabstract(ir::ContractedIf)


def test_ir::contractedif_constructor_exists():
    assert callable(ir::ContractedIf.__init__)


def test_ir::contractedif_constructor_args():
    sig = inspect.signature(ir::ContractedIf.__init__)
    params = list(sig.parameters.keys())



def test_iterableinstruction_is_not_abstract():
    assert not inspect.isabstract(IterableInstruction)


def test_iterableinstruction_constructor_exists():
    assert callable(IterableInstruction.__init__)


def test_iterableinstruction_constructor_args():
    sig = inspect.signature(IterableInstruction.__init__)
    params = list(sig.parameters.keys())



def test_ir::reductioninstruction_is_not_abstract():
    assert not inspect.isabstract(ir::ReductionInstruction)


def test_ir::reductioninstruction_constructor_exists():
    assert callable(ir::ReductionInstruction.__init__)


def test_ir::reductioninstruction_constructor_args():
    sig = inspect.signature(ir::ReductionInstruction.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_ir::setdefinition_is_not_abstract():
    assert not inspect.isabstract(ir::SetDefinition)


def test_ir::setdefinition_constructor_exists():
    assert callable(ir::SetDefinition.__init__)


def test_ir::setdefinition_constructor_args():
    sig = inspect.signature(ir::SetDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::setdefinition_has_name():
    assert hasattr(ir::SetDefinition, "name")
    descriptor = None
    for klass in ir::SetDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::variabledefinition_is_not_abstract():
    assert not inspect.isabstract(ir::VariableDefinition)


def test_ir::variabledefinition_constructor_exists():
    assert callable(ir::VariableDefinition.__init__)


def test_ir::variabledefinition_constructor_args():
    sig = inspect.signature(ir::VariableDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir::itemiddefinition_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIdDefinition)


def test_ir::itemiddefinition_constructor_exists():
    assert callable(ir::ItemIdDefinition.__init__)


def test_ir::itemiddefinition_constructor_args():
    sig = inspect.signature(ir::ItemIdDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir::itemindexdefinition_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIndexDefinition)


def test_ir::itemindexdefinition_constructor_exists():
    assert callable(ir::ItemIndexDefinition.__init__)


def test_ir::itemindexdefinition_constructor_args():
    sig = inspect.signature(ir::ItemIndexDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ir::affectation_is_not_abstract():
    assert not inspect.isabstract(ir::Affectation)


def test_ir::affectation_constructor_exists():
    assert callable(ir::Affectation.__init__)


def test_ir::affectation_constructor_args():
    sig = inspect.signature(ir::Affectation.__init__)
    params = list(sig.parameters.keys())



def test_ir::iterableinstruction_is_not_abstract():
    assert not inspect.isabstract(ir::IterableInstruction)


def test_ir::iterableinstruction_constructor_exists():
    assert callable(ir::IterableInstruction.__init__)


def test_ir::iterableinstruction_constructor_args():
    sig = inspect.signature(ir::IterableInstruction.__init__)
    params = list(sig.parameters.keys())



def test_ir::instructionblock_is_not_abstract():
    assert not inspect.isabstract(ir::InstructionBlock)


def test_ir::instructionblock_constructor_exists():
    assert callable(ir::InstructionBlock.__init__)


def test_ir::instructionblock_constructor_args():
    sig = inspect.signature(ir::InstructionBlock.__init__)
    params = list(sig.parameters.keys())



def test_timeloopcopyjob_is_not_abstract():
    assert not inspect.isabstract(TimeLoopCopyJob)


def test_timeloopcopyjob_constructor_exists():
    assert callable(TimeLoopCopyJob.__init__)


def test_timeloopcopyjob_constructor_args():
    sig = inspect.signature(TimeLoopCopyJob.__init__)
    params = list(sig.parameters.keys())



def test_ir::beforetimeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir::BeforeTimeLoopJob)


def test_ir::beforetimeloopjob_constructor_exists():
    assert callable(ir::BeforeTimeLoopJob.__init__)


def test_ir::beforetimeloopjob_constructor_args():
    sig = inspect.signature(ir::BeforeTimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_ir::aftertimeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir::AfterTimeLoopJob)


def test_ir::aftertimeloopjob_constructor_exists():
    assert callable(ir::AfterTimeLoopJob.__init__)


def test_ir::aftertimeloopjob_constructor_args():
    sig = inspect.signature(ir::AfterTimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_itemidvalue_is_not_abstract():
    assert not inspect.isabstract(ItemIdValue)


def test_itemidvalue_constructor_exists():
    assert callable(ItemIdValue.__init__)


def test_itemidvalue_constructor_args():
    sig = inspect.signature(ItemIdValue.__init__)
    params = list(sig.parameters.keys())



def test_ir::itemidvaluecall_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIdValueCall)


def test_ir::itemidvaluecall_constructor_exists():
    assert callable(ir::ItemIdValueCall.__init__)


def test_ir::itemidvaluecall_constructor_args():
    sig = inspect.signature(ir::ItemIdValueCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::itemidvalueiterator_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIdValueIterator)


def test_ir::itemidvalueiterator_constructor_exists():
    assert callable(ir::ItemIdValueIterator.__init__)


def test_ir::itemidvalueiterator_constructor_args():
    sig = inspect.signature(ir::ItemIdValueIterator.__init__)
    params = list(sig.parameters.keys())
    assert "shift" in params, "Missing parameter 'shift'"

def test_ir::itemidvalueiterator_has_shift():
    assert hasattr(ir::ItemIdValueIterator, "shift")
    descriptor = None
    for klass in ir::ItemIdValueIterator.__mro__:
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



def test_ir::setref_is_not_abstract():
    assert not inspect.isabstract(ir::SetRef)


def test_ir::setref_constructor_exists():
    assert callable(ir::SetRef.__init__)


def test_ir::setref_constructor_args():
    sig = inspect.signature(ir::SetRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::connectivitycall_is_not_abstract():
    assert not inspect.isabstract(ir::ConnectivityCall)


def test_ir::connectivitycall_constructor_exists():
    assert callable(ir::ConnectivityCall.__init__)


def test_ir::connectivitycall_constructor_args():
    sig = inspect.signature(ir::ConnectivityCall.__init__)
    params = list(sig.parameters.keys())



def test_irtype_is_not_abstract():
    assert not inspect.isabstract(IrType)


def test_irtype_constructor_exists():
    assert callable(IrType.__init__)


def test_irtype_constructor_args():
    sig = inspect.signature(IrType.__init__)
    params = list(sig.parameters.keys())



def test_ir::vectorconstant_is_not_abstract():
    assert not inspect.isabstract(ir::VectorConstant)


def test_ir::vectorconstant_constructor_exists():
    assert callable(ir::VectorConstant.__init__)


def test_ir::vectorconstant_constructor_args():
    sig = inspect.signature(ir::VectorConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir::basetypeconstant_is_not_abstract():
    assert not inspect.isabstract(ir::BaseTypeConstant)


def test_ir::basetypeconstant_constructor_exists():
    assert callable(ir::BaseTypeConstant.__init__)


def test_ir::basetypeconstant_constructor_args():
    sig = inspect.signature(ir::BaseTypeConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir::functioncall_is_not_abstract():
    assert not inspect.isabstract(ir::FunctionCall)


def test_ir::functioncall_constructor_exists():
    assert callable(ir::FunctionCall.__init__)


def test_ir::functioncall_constructor_args():
    sig = inspect.signature(ir::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_ir::maxconstant_is_not_abstract():
    assert not inspect.isabstract(ir::MaxConstant)


def test_ir::maxconstant_constructor_exists():
    assert callable(ir::MaxConstant.__init__)


def test_ir::maxconstant_constructor_args():
    sig = inspect.signature(ir::MaxConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir::minconstant_is_not_abstract():
    assert not inspect.isabstract(ir::MinConstant)


def test_ir::minconstant_constructor_exists():
    assert callable(ir::MinConstant.__init__)


def test_ir::minconstant_constructor_args():
    sig = inspect.signature(ir::MinConstant.__init__)
    params = list(sig.parameters.keys())



def test_ir::boolconstant_is_not_abstract():
    assert not inspect.isabstract(ir::BoolConstant)


def test_ir::boolconstant_constructor_exists():
    assert callable(ir::BoolConstant.__init__)


def test_ir::boolconstant_constructor_args():
    sig = inspect.signature(ir::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::boolconstant_has_value():
    assert hasattr(ir::BoolConstant, "value")
    descriptor = None
    for klass in ir::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::realconstant_is_not_abstract():
    assert not inspect.isabstract(ir::RealConstant)


def test_ir::realconstant_constructor_exists():
    assert callable(ir::RealConstant.__init__)


def test_ir::realconstant_constructor_args():
    sig = inspect.signature(ir::RealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::realconstant_has_value():
    assert hasattr(ir::RealConstant, "value")
    descriptor = None
    for klass in ir::RealConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::intconstant_is_not_abstract():
    assert not inspect.isabstract(ir::IntConstant)


def test_ir::intconstant_constructor_exists():
    assert callable(ir::IntConstant.__init__)


def test_ir::intconstant_constructor_args():
    sig = inspect.signature(ir::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir::intconstant_has_value():
    assert hasattr(ir::IntConstant, "value")
    descriptor = None
    for klass in ir::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir::parenthesis_is_not_abstract():
    assert not inspect.isabstract(ir::Parenthesis)


def test_ir::parenthesis_constructor_exists():
    assert callable(ir::Parenthesis.__init__)


def test_ir::parenthesis_constructor_args():
    sig = inspect.signature(ir::Parenthesis.__init__)
    params = list(sig.parameters.keys())



def test_ir::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir::UnaryExpression)


def test_ir::unaryexpression_constructor_exists():
    assert callable(ir::UnaryExpression.__init__)


def test_ir::unaryexpression_constructor_args():
    sig = inspect.signature(ir::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir::unaryexpression_has_operator():
    assert hasattr(ir::UnaryExpression, "operator")
    descriptor = None
    for klass in ir::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(ir::BinaryExpression)


def test_ir::binaryexpression_constructor_exists():
    assert callable(ir::BinaryExpression.__init__)


def test_ir::binaryexpression_constructor_args():
    sig = inspect.signature(ir::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir::binaryexpression_has_operator():
    assert hasattr(ir::BinaryExpression, "operator")
    descriptor = None
    for klass in ir::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir::cardinality_is_not_abstract():
    assert not inspect.isabstract(ir::Cardinality)


def test_ir::cardinality_constructor_exists():
    assert callable(ir::Cardinality.__init__)


def test_ir::cardinality_constructor_args():
    sig = inspect.signature(ir::Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_iterationblock_is_not_abstract():
    assert not inspect.isabstract(IterationBlock)


def test_iterationblock_constructor_exists():
    assert callable(IterationBlock.__init__)


def test_iterationblock_constructor_args():
    sig = inspect.signature(IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_ir::interval_is_not_abstract():
    assert not inspect.isabstract(ir::Interval)


def test_ir::interval_constructor_exists():
    assert callable(ir::Interval.__init__)


def test_ir::interval_constructor_args():
    sig = inspect.signature(ir::Interval.__init__)
    params = list(sig.parameters.keys())



def test_ir::iterator_is_not_abstract():
    assert not inspect.isabstract(ir::Iterator)


def test_ir::iterator_constructor_exists():
    assert callable(ir::Iterator.__init__)


def test_ir::iterator_constructor_args():
    sig = inspect.signature(ir::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ir::exit_is_not_abstract():
    assert not inspect.isabstract(ir::Exit)


def test_ir::exit_constructor_exists():
    assert callable(ir::Exit.__init__)


def test_ir::exit_constructor_args():
    sig = inspect.signature(ir::Exit.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_ir::exit_has_message():
    assert hasattr(ir::Exit, "message")
    descriptor = None
    for klass in ir::Exit.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_ir::return_is_not_abstract():
    assert not inspect.isabstract(ir::Return)


def test_ir::return_constructor_exists():
    assert callable(ir::Return.__init__)


def test_ir::return_constructor_args():
    sig = inspect.signature(ir::Return.__init__)
    params = list(sig.parameters.keys())



def test_ir::if_is_not_abstract():
    assert not inspect.isabstract(ir::If)


def test_ir::if_constructor_exists():
    assert callable(ir::If.__init__)


def test_ir::if_constructor_args():
    sig = inspect.signature(ir::If.__init__)
    params = list(sig.parameters.keys())



def test_job_is_not_abstract():
    assert not inspect.isabstract(Job)


def test_job_constructor_exists():
    assert callable(Job.__init__)


def test_job_constructor_args():
    sig = inspect.signature(Job.__init__)
    params = list(sig.parameters.keys())



def test_ir::timeloopcopyjob_is_not_abstract():
    assert not inspect.isabstract(ir::TimeLoopCopyJob)


def test_ir::timeloopcopyjob_constructor_exists():
    assert callable(ir::TimeLoopCopyJob.__init__)


def test_ir::timeloopcopyjob_constructor_args():
    sig = inspect.signature(ir::TimeLoopCopyJob.__init__)
    params = list(sig.parameters.keys())



def test_ir::instructionjob_is_not_abstract():
    assert not inspect.isabstract(ir::InstructionJob)


def test_ir::instructionjob_constructor_exists():
    assert callable(ir::InstructionJob.__init__)


def test_ir::instructionjob_constructor_args():
    sig = inspect.signature(ir::InstructionJob.__init__)
    params = list(sig.parameters.keys())



def test_ir::loop_is_not_abstract():
    assert not inspect.isabstract(ir::Loop)


def test_ir::loop_constructor_exists():
    assert callable(ir::Loop.__init__)


def test_ir::loop_constructor_args():
    sig = inspect.signature(ir::Loop.__init__)
    params = list(sig.parameters.keys())
    assert "multithreadable" in params, "Missing parameter 'multithreadable'"

def test_ir::loop_has_multithreadable():
    assert hasattr(ir::Loop, "multithreadable")
    descriptor = None
    for klass in ir::Loop.__mro__:
        if "multithreadable" in klass.__dict__:
            descriptor = klass.__dict__["multithreadable"]
            break
    assert isinstance(descriptor, property)



def test_ir::argorvarref_is_not_abstract():
    assert not inspect.isabstract(ir::ArgOrVarRef)


def test_ir::argorvarref_constructor_exists():
    assert callable(ir::ArgOrVarRef.__init__)


def test_ir::argorvarref_constructor_args():
    sig = inspect.signature(ir::ArgOrVarRef.__init__)
    params = list(sig.parameters.keys())



def test_ir::connectivitytype_is_not_abstract():
    assert not inspect.isabstract(ir::ConnectivityType)


def test_ir::connectivitytype_constructor_exists():
    assert callable(ir::ConnectivityType.__init__)


def test_ir::connectivitytype_constructor_args():
    sig = inspect.signature(ir::ConnectivityType.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ir::basetype_is_not_abstract():
    assert not inspect.isabstract(ir::BaseType)


def test_ir::basetype_constructor_exists():
    assert callable(ir::BaseType.__init__)


def test_ir::basetype_constructor_args():
    sig = inspect.signature(ir::BaseType.__init__)
    params = list(sig.parameters.keys())
    assert "primitive" in params, "Missing parameter 'primitive'"

def test_ir::basetype_has_primitive():
    assert hasattr(ir::BaseType, "primitive")
    descriptor = None
    for klass in ir::BaseType.__mro__:
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



def test_ir::arg_is_not_abstract():
    assert not inspect.isabstract(ir::Arg)


def test_ir::arg_constructor_exists():
    assert callable(ir::Arg.__init__)


def test_ir::arg_constructor_args():
    sig = inspect.signature(ir::Arg.__init__)
    params = list(sig.parameters.keys())



def test_jobcontainer_is_not_abstract():
    assert not inspect.isabstract(JobContainer)


def test_jobcontainer_constructor_exists():
    assert callable(JobContainer.__init__)


def test_jobcontainer_constructor_args():
    sig = inspect.signature(JobContainer.__init__)
    params = list(sig.parameters.keys())



def test_ir::timeloopjob_is_not_abstract():
    assert not inspect.isabstract(ir::TimeLoopJob)


def test_ir::timeloopjob_constructor_exists():
    assert callable(ir::TimeLoopJob.__init__)


def test_ir::timeloopjob_constructor_args():
    sig = inspect.signature(ir::TimeLoopJob.__init__)
    params = list(sig.parameters.keys())



def test_ir::irmodule_is_not_abstract():
    assert not inspect.isabstract(ir::IrModule)


def test_ir::irmodule_constructor_exists():
    assert callable(ir::IrModule.__init__)


def test_ir::irmodule_constructor_args():
    sig = inspect.signature(ir::IrModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::irmodule_has_name():
    assert hasattr(ir::IrModule, "name")
    descriptor = None
    for klass in ir::IrModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::connectivityvariable_is_not_abstract():
    assert not inspect.isabstract(ir::ConnectivityVariable)


def test_ir::connectivityvariable_constructor_exists():
    assert callable(ir::ConnectivityVariable.__init__)


def test_ir::connectivityvariable_constructor_args():
    sig = inspect.signature(ir::ConnectivityVariable.__init__)
    params = list(sig.parameters.keys())



def test_ir::variable_is_not_abstract():
    assert not inspect.isabstract(ir::Variable)


def test_ir::variable_constructor_exists():
    assert callable(ir::Variable.__init__)


def test_ir::variable_constructor_args():
    sig = inspect.signature(ir::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "persistenceName" in params, "Missing parameter 'persistenceName'"
    assert "const" in params, "Missing parameter 'const'"

def test_ir::variable_has_persistenceName():
    assert hasattr(ir::Variable, "persistenceName")
    descriptor = None
    for klass in ir::Variable.__mro__:
        if "persistenceName" in klass.__dict__:
            descriptor = klass.__dict__["persistenceName"]
            break
    assert isinstance(descriptor, property)

def test_ir::variable_has_const():
    assert hasattr(ir::Variable, "const")
    descriptor = None
    for klass in ir::Variable.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_ir::simplevariable_is_not_abstract():
    assert not inspect.isabstract(ir::SimpleVariable)


def test_ir::simplevariable_constructor_exists():
    assert callable(ir::SimpleVariable.__init__)


def test_ir::simplevariable_constructor_args():
    sig = inspect.signature(ir::SimpleVariable.__init__)
    params = list(sig.parameters.keys())



def test_irannotable_is_not_abstract():
    assert not inspect.isabstract(IrAnnotable)


def test_irannotable_constructor_exists():
    assert callable(IrAnnotable.__init__)


def test_irannotable_constructor_args():
    sig = inspect.signature(IrAnnotable.__init__)
    params = list(sig.parameters.keys())



def test_ir::iterationblock_is_not_abstract():
    assert not inspect.isabstract(ir::IterationBlock)


def test_ir::iterationblock_constructor_exists():
    assert callable(ir::IterationBlock.__init__)


def test_ir::iterationblock_constructor_args():
    sig = inspect.signature(ir::IterationBlock.__init__)
    params = list(sig.parameters.keys())



def test_ir::timeloopvariable_is_not_abstract():
    assert not inspect.isabstract(ir::TimeLoopVariable)


def test_ir::timeloopvariable_constructor_exists():
    assert callable(ir::TimeLoopVariable.__init__)


def test_ir::timeloopvariable_constructor_args():
    sig = inspect.signature(ir::TimeLoopVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::timeloopvariable_has_name():
    assert hasattr(ir::TimeLoopVariable, "name")
    descriptor = None
    for klass in ir::TimeLoopVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::itemid_is_not_abstract():
    assert not inspect.isabstract(ir::ItemId)


def test_ir::itemid_constructor_exists():
    assert callable(ir::ItemId.__init__)


def test_ir::itemid_constructor_args():
    sig = inspect.signature(ir::ItemId.__init__)
    params = list(sig.parameters.keys())
    assert "itemName" in params, "Missing parameter 'itemName'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir::itemid_has_itemName():
    assert hasattr(ir::ItemId, "itemName")
    descriptor = None
    for klass in ir::ItemId.__mro__:
        if "itemName" in klass.__dict__:
            descriptor = klass.__dict__["itemName"]
            break
    assert isinstance(descriptor, property)

def test_ir::itemid_has_name():
    assert hasattr(ir::ItemId, "name")
    descriptor = None
    for klass in ir::ItemId.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::irtype_is_not_abstract():
    assert not inspect.isabstract(ir::IrType)


def test_ir::irtype_constructor_exists():
    assert callable(ir::IrType.__init__)


def test_ir::irtype_constructor_args():
    sig = inspect.signature(ir::IrType.__init__)
    params = list(sig.parameters.keys())



def test_ir::container_is_not_abstract():
    assert not inspect.isabstract(ir::Container)


def test_ir::container_constructor_exists():
    assert callable(ir::Container.__init__)


def test_ir::container_constructor_args():
    sig = inspect.signature(ir::Container.__init__)
    params = list(sig.parameters.keys())



def test_ir::instruction_is_not_abstract():
    assert not inspect.isabstract(ir::Instruction)


def test_ir::instruction_constructor_exists():
    assert callable(ir::Instruction.__init__)


def test_ir::instruction_constructor_args():
    sig = inspect.signature(ir::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_ir::argorvar_is_not_abstract():
    assert not inspect.isabstract(ir::ArgOrVar)


def test_ir::argorvar_constructor_exists():
    assert callable(ir::ArgOrVar.__init__)


def test_ir::argorvar_constructor_args():
    sig = inspect.signature(ir::ArgOrVar.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::argorvar_has_name():
    assert hasattr(ir::ArgOrVar, "name")
    descriptor = None
    for klass in ir::ArgOrVar.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::import_is_not_abstract():
    assert not inspect.isabstract(ir::Import)


def test_ir::import_constructor_exists():
    assert callable(ir::Import.__init__)


def test_ir::import_constructor_args():
    sig = inspect.signature(ir::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ir::import_has_importedNamespace():
    assert hasattr(ir::Import, "importedNamespace")
    descriptor = None
    for klass in ir::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ir::itemtype_is_not_abstract():
    assert not inspect.isabstract(ir::ItemType)


def test_ir::itemtype_constructor_exists():
    assert callable(ir::ItemType.__init__)


def test_ir::itemtype_constructor_args():
    sig = inspect.signature(ir::ItemType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::itemtype_has_name():
    assert hasattr(ir::ItemType, "name")
    descriptor = None
    for klass in ir::ItemType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::timeloopcopy_is_not_abstract():
    assert not inspect.isabstract(ir::TimeLoopCopy)


def test_ir::timeloopcopy_constructor_exists():
    assert callable(ir::TimeLoopCopy.__init__)


def test_ir::timeloopcopy_constructor_args():
    sig = inspect.signature(ir::TimeLoopCopy.__init__)
    params = list(sig.parameters.keys())



def test_ir::postprocessinginfo_is_not_abstract():
    assert not inspect.isabstract(ir::PostProcessingInfo)


def test_ir::postprocessinginfo_constructor_exists():
    assert callable(ir::PostProcessingInfo.__init__)


def test_ir::postprocessinginfo_constructor_args():
    sig = inspect.signature(ir::PostProcessingInfo.__init__)
    params = list(sig.parameters.keys())
    assert "periodValue" in params, "Missing parameter 'periodValue'"

def test_ir::postprocessinginfo_has_periodValue():
    assert hasattr(ir::PostProcessingInfo, "periodValue")
    descriptor = None
    for klass in ir::PostProcessingInfo.__mro__:
        if "periodValue" in klass.__dict__:
            descriptor = klass.__dict__["periodValue"]
            break
    assert isinstance(descriptor, property)



def test_ir::connectivity_is_not_abstract():
    assert not inspect.isabstract(ir::Connectivity)


def test_ir::connectivity_constructor_exists():
    assert callable(ir::Connectivity.__init__)


def test_ir::connectivity_constructor_args():
    sig = inspect.signature(ir::Connectivity.__init__)
    params = list(sig.parameters.keys())
    assert "indexEqualId" in params, "Missing parameter 'indexEqualId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_ir::connectivity_has_indexEqualId():
    assert hasattr(ir::Connectivity, "indexEqualId")
    descriptor = None
    for klass in ir::Connectivity.__mro__:
        if "indexEqualId" in klass.__dict__:
            descriptor = klass.__dict__["indexEqualId"]
            break
    assert isinstance(descriptor, property)

def test_ir::connectivity_has_name():
    assert hasattr(ir::Connectivity, "name")
    descriptor = None
    for klass in ir::Connectivity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir::connectivity_has_multiple():
    assert hasattr(ir::Connectivity, "multiple")
    descriptor = None
    for klass in ir::Connectivity.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_ir::expression_is_not_abstract():
    assert not inspect.isabstract(ir::Expression)


def test_ir::expression_constructor_exists():
    assert callable(ir::Expression.__init__)


def test_ir::expression_constructor_args():
    sig = inspect.signature(ir::Expression.__init__)
    params = list(sig.parameters.keys())



def test_ir::job_is_not_abstract():
    assert not inspect.isabstract(ir::Job)


def test_ir::job_constructor_exists():
    assert callable(ir::Job.__init__)


def test_ir::job_constructor_args():
    sig = inspect.signature(ir::Job.__init__)
    params = list(sig.parameters.keys())
    assert "onCycle" in params, "Missing parameter 'onCycle'"
    assert "name" in params, "Missing parameter 'name'"
    assert "at" in params, "Missing parameter 'at'"

def test_ir::job_has_onCycle():
    assert hasattr(ir::Job, "onCycle")
    descriptor = None
    for klass in ir::Job.__mro__:
        if "onCycle" in klass.__dict__:
            descriptor = klass.__dict__["onCycle"]
            break
    assert isinstance(descriptor, property)

def test_ir::job_has_name():
    assert hasattr(ir::Job, "name")
    descriptor = None
    for klass in ir::Job.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir::job_has_at():
    assert hasattr(ir::Job, "at")
    descriptor = None
    for klass in ir::Job.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)



def test_ir::function_is_not_abstract():
    assert not inspect.isabstract(ir::Function)


def test_ir::function_constructor_exists():
    assert callable(ir::Function.__init__)


def test_ir::function_constructor_args():
    sig = inspect.signature(ir::Function.__init__)
    params = list(sig.parameters.keys())
    assert "provider" in params, "Missing parameter 'provider'"
    assert "name" in params, "Missing parameter 'name'"

def test_ir::function_has_provider():
    assert hasattr(ir::Function, "provider")
    descriptor = None
    for klass in ir::Function.__mro__:
        if "provider" in klass.__dict__:
            descriptor = klass.__dict__["provider"]
            break
    assert isinstance(descriptor, property)

def test_ir::function_has_name():
    assert hasattr(ir::Function, "name")
    descriptor = None
    for klass in ir::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::itemindexvalue_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIndexValue)


def test_ir::itemindexvalue_constructor_exists():
    assert callable(ir::ItemIndexValue.__init__)


def test_ir::itemindexvalue_constructor_args():
    sig = inspect.signature(ir::ItemIndexValue.__init__)
    params = list(sig.parameters.keys())



def test_ir::itemidvalue_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIdValue)


def test_ir::itemidvalue_constructor_exists():
    assert callable(ir::ItemIdValue.__init__)


def test_ir::itemidvalue_constructor_args():
    sig = inspect.signature(ir::ItemIdValue.__init__)
    params = list(sig.parameters.keys())



def test_ir::timeloop_is_not_abstract():
    assert not inspect.isabstract(ir::TimeLoop)


def test_ir::timeloop_constructor_exists():
    assert callable(ir::TimeLoop.__init__)


def test_ir::timeloop_constructor_args():
    sig = inspect.signature(ir::TimeLoop.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir::timeloop_has_name():
    assert hasattr(ir::TimeLoop, "name")
    descriptor = None
    for klass in ir::TimeLoop.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir::itemindex_is_not_abstract():
    assert not inspect.isabstract(ir::ItemIndex)


def test_ir::itemindex_constructor_exists():
    assert callable(ir::ItemIndex.__init__)


def test_ir::itemindex_constructor_args():
    sig = inspect.signature(ir::ItemIndex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "itemName" in params, "Missing parameter 'itemName'"

def test_ir::itemindex_has_name():
    assert hasattr(ir::ItemIndex, "name")
    descriptor = None
    for klass in ir::ItemIndex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ir::itemindex_has_itemName():
    assert hasattr(ir::ItemIndex, "itemName")
    descriptor = None
    for klass in ir::ItemIndex.__mro__:
        if "itemName" in klass.__dict__:
            descriptor = klass.__dict__["itemName"]
            break
    assert isinstance(descriptor, property)



def test_ir::jobcontainer_is_not_abstract():
    assert not inspect.isabstract(ir::JobContainer)


def test_ir::jobcontainer_constructor_exists():
    assert callable(ir::JobContainer.__init__)


def test_ir::jobcontainer_constructor_args():
    sig = inspect.signature(ir::JobContainer.__init__)
    params = list(sig.parameters.keys())



def test_ir::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(ir::EStringToStringMapEntry)


def test_ir::estringtostringmapentry_constructor_exists():
    assert callable(ir::EStringToStringMapEntry.__init__)


def test_ir::estringtostringmapentry_constructor_args():
    sig = inspect.signature(ir::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_ir::irannotation_is_not_abstract():
    assert not inspect.isabstract(ir::IrAnnotation)


def test_ir::irannotation_constructor_exists():
    assert callable(ir::IrAnnotation.__init__)


def test_ir::irannotation_constructor_args():
    sig = inspect.signature(ir::IrAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "source" in params, "Missing parameter 'source'"

def test_ir::irannotation_has_source():
    assert hasattr(ir::IrAnnotation, "source")
    descriptor = None
    for klass in ir::IrAnnotation.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_ir::irannotable_is_not_abstract():
    assert not inspect.isabstract(ir::IrAnnotable)


def test_ir::irannotable_constructor_exists():
    assert callable(ir::IrAnnotable.__init__)


def test_ir::irannotable_constructor_args():
    sig = inspect.signature(ir::IrAnnotable.__init__)
    params = list(sig.parameters.keys())

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "Real",
        "Int",
        "Bool",
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
Expression_strategy = st.builds(
    Expression,
)
ir::ContractedIf_strategy = st.builds(
    ir::ContractedIf,
)
IterableInstruction_strategy = st.builds(
    IterableInstruction,
)
ir::ReductionInstruction_strategy = st.builds(
    ir::ReductionInstruction,
)
Instruction_strategy = st.builds(
    Instruction,
)
ir::SetDefinition_strategy = st.builds(
    ir::SetDefinition,
    name=
        safe_text
)
ir::VariableDefinition_strategy = st.builds(
    ir::VariableDefinition,
)
ir::ItemIdDefinition_strategy = st.builds(
    ir::ItemIdDefinition,
)
ir::ItemIndexDefinition_strategy = st.builds(
    ir::ItemIndexDefinition,
)
ir::Affectation_strategy = st.builds(
    ir::Affectation,
)
ir::IterableInstruction_strategy = st.builds(
    ir::IterableInstruction,
)
ir::InstructionBlock_strategy = st.builds(
    ir::InstructionBlock,
)
TimeLoopCopyJob_strategy = st.builds(
    TimeLoopCopyJob,
)
ir::BeforeTimeLoopJob_strategy = st.builds(
    ir::BeforeTimeLoopJob,
)
ir::AfterTimeLoopJob_strategy = st.builds(
    ir::AfterTimeLoopJob,
)
ItemIdValue_strategy = st.builds(
    ItemIdValue,
)
ir::ItemIdValueCall_strategy = st.builds(
    ir::ItemIdValueCall,
)
ir::ItemIdValueIterator_strategy = st.builds(
    ir::ItemIdValueIterator,
    shift=
        st.integers()
)
Container_strategy = st.builds(
    Container,
)
ir::SetRef_strategy = st.builds(
    ir::SetRef,
)
ir::ConnectivityCall_strategy = st.builds(
    ir::ConnectivityCall,
)
IrType_strategy = st.builds(
    IrType,
)
ir::VectorConstant_strategy = st.builds(
    ir::VectorConstant,
)
ir::BaseTypeConstant_strategy = st.builds(
    ir::BaseTypeConstant,
)
ir::FunctionCall_strategy = st.builds(
    ir::FunctionCall,
)
ir::MaxConstant_strategy = st.builds(
    ir::MaxConstant,
)
ir::MinConstant_strategy = st.builds(
    ir::MinConstant,
)
ir::BoolConstant_strategy = st.builds(
    ir::BoolConstant,
    value=
        st.booleans()
)
ir::RealConstant_strategy = st.builds(
    ir::RealConstant,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir::IntConstant_strategy = st.builds(
    ir::IntConstant,
    value=
        st.integers()
)
ir::Parenthesis_strategy = st.builds(
    ir::Parenthesis,
)
ir::UnaryExpression_strategy = st.builds(
    ir::UnaryExpression,
    operator=
        safe_text
)
ir::BinaryExpression_strategy = st.builds(
    ir::BinaryExpression,
    operator=
        safe_text
)
ir::Cardinality_strategy = st.builds(
    ir::Cardinality,
)
IterationBlock_strategy = st.builds(
    IterationBlock,
)
ir::Interval_strategy = st.builds(
    ir::Interval,
)
ir::Iterator_strategy = st.builds(
    ir::Iterator,
)
ir::Exit_strategy = st.builds(
    ir::Exit,
    message=
        safe_text
)
ir::Return_strategy = st.builds(
    ir::Return,
)
ir::If_strategy = st.builds(
    ir::If,
)
Job_strategy = st.builds(
    Job,
)
ir::TimeLoopCopyJob_strategy = st.builds(
    ir::TimeLoopCopyJob,
)
ir::InstructionJob_strategy = st.builds(
    ir::InstructionJob,
)
ir::Loop_strategy = st.builds(
    ir::Loop,
    multithreadable=
        st.booleans()
)
ir::ArgOrVarRef_strategy = st.builds(
    ir::ArgOrVarRef,
)
ir::ConnectivityType_strategy = st.builds(
    ir::ConnectivityType,
)
Variable_strategy = st.builds(
    Variable,
)
ir::BaseType_strategy = st.builds(
    ir::BaseType,
    primitive=
        safe_text
)
ArgOrVar_strategy = st.builds(
    ArgOrVar,
)
ir::Arg_strategy = st.builds(
    ir::Arg,
)
JobContainer_strategy = st.builds(
    JobContainer,
)
ir::TimeLoopJob_strategy = st.builds(
    ir::TimeLoopJob,
)
ir::IrModule_strategy = st.builds(
    ir::IrModule,
    name=
        safe_text
)
ir::ConnectivityVariable_strategy = st.builds(
    ir::ConnectivityVariable,
)
ir::Variable_strategy = st.builds(
    ir::Variable,
    persistenceName=
        safe_text,
    const=
        st.booleans()
)
ir::SimpleVariable_strategy = st.builds(
    ir::SimpleVariable,
)
IrAnnotable_strategy = st.builds(
    IrAnnotable,
)
ir::IterationBlock_strategy = st.builds(
    ir::IterationBlock,
)
ir::TimeLoopVariable_strategy = st.builds(
    ir::TimeLoopVariable,
    name=
        safe_text
)
ir::ItemId_strategy = st.builds(
    ir::ItemId,
    itemName=
        safe_text,
    name=
        safe_text
)
ir::IrType_strategy = st.builds(
    ir::IrType,
)
ir::Container_strategy = st.builds(
    ir::Container,
)
ir::Instruction_strategy = st.builds(
    ir::Instruction,
)
ir::ArgOrVar_strategy = st.builds(
    ir::ArgOrVar,
    name=
        safe_text
)
ir::Import_strategy = st.builds(
    ir::Import,
    importedNamespace=
        safe_text
)
ir::ItemType_strategy = st.builds(
    ir::ItemType,
    name=
        safe_text
)
ir::TimeLoopCopy_strategy = st.builds(
    ir::TimeLoopCopy,
)
ir::PostProcessingInfo_strategy = st.builds(
    ir::PostProcessingInfo,
    periodValue=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir::Connectivity_strategy = st.builds(
    ir::Connectivity,
    indexEqualId=
        st.booleans(),
    name=
        safe_text,
    multiple=
        st.booleans()
)
ir::Expression_strategy = st.builds(
    ir::Expression,
)
ir::Job_strategy = st.builds(
    ir::Job,
    onCycle=
        st.booleans(),
    name=
        safe_text,
    at=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ir::Function_strategy = st.builds(
    ir::Function,
    provider=
        safe_text,
    name=
        safe_text
)
ir::ItemIndexValue_strategy = st.builds(
    ir::ItemIndexValue,
)
ir::ItemIdValue_strategy = st.builds(
    ir::ItemIdValue,
)
ir::TimeLoop_strategy = st.builds(
    ir::TimeLoop,
    name=
        safe_text
)
ir::ItemIndex_strategy = st.builds(
    ir::ItemIndex,
    name=
        safe_text,
    itemName=
        safe_text
)
ir::JobContainer_strategy = st.builds(
    ir::JobContainer,
)
ir::EStringToStringMapEntry_strategy = st.builds(
    ir::EStringToStringMapEntry,
)
ir::IrAnnotation_strategy = st.builds(
    ir::IrAnnotation,
    source=
        safe_text
)
ir::IrAnnotable_strategy = st.builds(
    ir::IrAnnotable,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ir::ContractedIf_strategy)
@settings(max_examples=50)
def test_ir::contractedif_instantiation(instance):
    assert isinstance(instance, ir::ContractedIf)

@given(instance=IterableInstruction_strategy)
@settings(max_examples=50)
def test_iterableinstruction_instantiation(instance):
    assert isinstance(instance, IterableInstruction)

@given(instance=ir::ReductionInstruction_strategy)
@settings(max_examples=50)
def test_ir::reductioninstruction_instantiation(instance):
    assert isinstance(instance, ir::ReductionInstruction)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=ir::SetDefinition_strategy)
@settings(max_examples=50)
def test_ir::setdefinition_instantiation(instance):
    assert isinstance(instance, ir::SetDefinition)

@given(instance=ir::SetDefinition_strategy)
def test_ir::setdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::SetDefinition_strategy)
def test_ir::setdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::VariableDefinition_strategy)
@settings(max_examples=50)
def test_ir::variabledefinition_instantiation(instance):
    assert isinstance(instance, ir::VariableDefinition)

@given(instance=ir::ItemIdDefinition_strategy)
@settings(max_examples=50)
def test_ir::itemiddefinition_instantiation(instance):
    assert isinstance(instance, ir::ItemIdDefinition)

@given(instance=ir::ItemIndexDefinition_strategy)
@settings(max_examples=50)
def test_ir::itemindexdefinition_instantiation(instance):
    assert isinstance(instance, ir::ItemIndexDefinition)

@given(instance=ir::Affectation_strategy)
@settings(max_examples=50)
def test_ir::affectation_instantiation(instance):
    assert isinstance(instance, ir::Affectation)

@given(instance=ir::IterableInstruction_strategy)
@settings(max_examples=50)
def test_ir::iterableinstruction_instantiation(instance):
    assert isinstance(instance, ir::IterableInstruction)

@given(instance=ir::InstructionBlock_strategy)
@settings(max_examples=50)
def test_ir::instructionblock_instantiation(instance):
    assert isinstance(instance, ir::InstructionBlock)

@given(instance=TimeLoopCopyJob_strategy)
@settings(max_examples=50)
def test_timeloopcopyjob_instantiation(instance):
    assert isinstance(instance, TimeLoopCopyJob)

@given(instance=ir::BeforeTimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir::beforetimeloopjob_instantiation(instance):
    assert isinstance(instance, ir::BeforeTimeLoopJob)

@given(instance=ir::AfterTimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir::aftertimeloopjob_instantiation(instance):
    assert isinstance(instance, ir::AfterTimeLoopJob)

@given(instance=ItemIdValue_strategy)
@settings(max_examples=50)
def test_itemidvalue_instantiation(instance):
    assert isinstance(instance, ItemIdValue)

@given(instance=ir::ItemIdValueCall_strategy)
@settings(max_examples=50)
def test_ir::itemidvaluecall_instantiation(instance):
    assert isinstance(instance, ir::ItemIdValueCall)

@given(instance=ir::ItemIdValueIterator_strategy)
@settings(max_examples=50)
def test_ir::itemidvalueiterator_instantiation(instance):
    assert isinstance(instance, ir::ItemIdValueIterator)

@given(instance=ir::ItemIdValueIterator_strategy)
def test_ir::itemidvalueiterator_shift_type(instance):
    assert isinstance(instance.shift, int)


@given(instance=ir::ItemIdValueIterator_strategy)
def test_ir::itemidvalueiterator_shift_setter(instance):
    original = instance.shift
    instance.shift = original
    assert instance.shift == original

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=ir::SetRef_strategy)
@settings(max_examples=50)
def test_ir::setref_instantiation(instance):
    assert isinstance(instance, ir::SetRef)

@given(instance=ir::ConnectivityCall_strategy)
@settings(max_examples=50)
def test_ir::connectivitycall_instantiation(instance):
    assert isinstance(instance, ir::ConnectivityCall)

@given(instance=IrType_strategy)
@settings(max_examples=50)
def test_irtype_instantiation(instance):
    assert isinstance(instance, IrType)

@given(instance=ir::VectorConstant_strategy)
@settings(max_examples=50)
def test_ir::vectorconstant_instantiation(instance):
    assert isinstance(instance, ir::VectorConstant)

@given(instance=ir::BaseTypeConstant_strategy)
@settings(max_examples=50)
def test_ir::basetypeconstant_instantiation(instance):
    assert isinstance(instance, ir::BaseTypeConstant)

@given(instance=ir::FunctionCall_strategy)
@settings(max_examples=50)
def test_ir::functioncall_instantiation(instance):
    assert isinstance(instance, ir::FunctionCall)

@given(instance=ir::MaxConstant_strategy)
@settings(max_examples=50)
def test_ir::maxconstant_instantiation(instance):
    assert isinstance(instance, ir::MaxConstant)

@given(instance=ir::MinConstant_strategy)
@settings(max_examples=50)
def test_ir::minconstant_instantiation(instance):
    assert isinstance(instance, ir::MinConstant)

@given(instance=ir::BoolConstant_strategy)
@settings(max_examples=50)
def test_ir::boolconstant_instantiation(instance):
    assert isinstance(instance, ir::BoolConstant)

@given(instance=ir::BoolConstant_strategy)
def test_ir::boolconstant_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=ir::BoolConstant_strategy)
def test_ir::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::RealConstant_strategy)
@settings(max_examples=50)
def test_ir::realconstant_instantiation(instance):
    assert isinstance(instance, ir::RealConstant)

@given(instance=ir::RealConstant_strategy)
def test_ir::realconstant_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=ir::RealConstant_strategy)
def test_ir::realconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::IntConstant_strategy)
@settings(max_examples=50)
def test_ir::intconstant_instantiation(instance):
    assert isinstance(instance, ir::IntConstant)

@given(instance=ir::IntConstant_strategy)
def test_ir::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ir::IntConstant_strategy)
def test_ir::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir::Parenthesis_strategy)
@settings(max_examples=50)
def test_ir::parenthesis_instantiation(instance):
    assert isinstance(instance, ir::Parenthesis)

@given(instance=ir::UnaryExpression_strategy)
@settings(max_examples=50)
def test_ir::unaryexpression_instantiation(instance):
    assert isinstance(instance, ir::UnaryExpression)

@given(instance=ir::UnaryExpression_strategy)
def test_ir::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ir::UnaryExpression_strategy)
def test_ir::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir::BinaryExpression_strategy)
@settings(max_examples=50)
def test_ir::binaryexpression_instantiation(instance):
    assert isinstance(instance, ir::BinaryExpression)

@given(instance=ir::BinaryExpression_strategy)
def test_ir::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=ir::BinaryExpression_strategy)
def test_ir::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir::Cardinality_strategy)
@settings(max_examples=50)
def test_ir::cardinality_instantiation(instance):
    assert isinstance(instance, ir::Cardinality)

@given(instance=IterationBlock_strategy)
@settings(max_examples=50)
def test_iterationblock_instantiation(instance):
    assert isinstance(instance, IterationBlock)

@given(instance=ir::Interval_strategy)
@settings(max_examples=50)
def test_ir::interval_instantiation(instance):
    assert isinstance(instance, ir::Interval)

@given(instance=ir::Iterator_strategy)
@settings(max_examples=50)
def test_ir::iterator_instantiation(instance):
    assert isinstance(instance, ir::Iterator)

@given(instance=ir::Exit_strategy)
@settings(max_examples=50)
def test_ir::exit_instantiation(instance):
    assert isinstance(instance, ir::Exit)

@given(instance=ir::Exit_strategy)
def test_ir::exit_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=ir::Exit_strategy)
def test_ir::exit_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=ir::Return_strategy)
@settings(max_examples=50)
def test_ir::return_instantiation(instance):
    assert isinstance(instance, ir::Return)

@given(instance=ir::If_strategy)
@settings(max_examples=50)
def test_ir::if_instantiation(instance):
    assert isinstance(instance, ir::If)

@given(instance=Job_strategy)
@settings(max_examples=50)
def test_job_instantiation(instance):
    assert isinstance(instance, Job)

@given(instance=ir::TimeLoopCopyJob_strategy)
@settings(max_examples=50)
def test_ir::timeloopcopyjob_instantiation(instance):
    assert isinstance(instance, ir::TimeLoopCopyJob)

@given(instance=ir::InstructionJob_strategy)
@settings(max_examples=50)
def test_ir::instructionjob_instantiation(instance):
    assert isinstance(instance, ir::InstructionJob)

@given(instance=ir::Loop_strategy)
@settings(max_examples=50)
def test_ir::loop_instantiation(instance):
    assert isinstance(instance, ir::Loop)

@given(instance=ir::Loop_strategy)
def test_ir::loop_multithreadable_type(instance):
    assert isinstance(instance.multithreadable, bool)


@given(instance=ir::Loop_strategy)
def test_ir::loop_multithreadable_setter(instance):
    original = instance.multithreadable
    instance.multithreadable = original
    assert instance.multithreadable == original

@given(instance=ir::ArgOrVarRef_strategy)
@settings(max_examples=50)
def test_ir::argorvarref_instantiation(instance):
    assert isinstance(instance, ir::ArgOrVarRef)

@given(instance=ir::ConnectivityType_strategy)
@settings(max_examples=50)
def test_ir::connectivitytype_instantiation(instance):
    assert isinstance(instance, ir::ConnectivityType)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=ir::BaseType_strategy)
@settings(max_examples=50)
def test_ir::basetype_instantiation(instance):
    assert isinstance(instance, ir::BaseType)

@given(instance=ir::BaseType_strategy)
def test_ir::basetype_primitive_type(instance):
    assert isinstance(instance.primitive, str)


@given(instance=ir::BaseType_strategy)
def test_ir::basetype_primitive_setter(instance):
    original = instance.primitive
    instance.primitive = original
    assert instance.primitive == original

@given(instance=ArgOrVar_strategy)
@settings(max_examples=50)
def test_argorvar_instantiation(instance):
    assert isinstance(instance, ArgOrVar)

@given(instance=ir::Arg_strategy)
@settings(max_examples=50)
def test_ir::arg_instantiation(instance):
    assert isinstance(instance, ir::Arg)

@given(instance=JobContainer_strategy)
@settings(max_examples=50)
def test_jobcontainer_instantiation(instance):
    assert isinstance(instance, JobContainer)

@given(instance=ir::TimeLoopJob_strategy)
@settings(max_examples=50)
def test_ir::timeloopjob_instantiation(instance):
    assert isinstance(instance, ir::TimeLoopJob)

@given(instance=ir::IrModule_strategy)
@settings(max_examples=50)
def test_ir::irmodule_instantiation(instance):
    assert isinstance(instance, ir::IrModule)

@given(instance=ir::IrModule_strategy)
def test_ir::irmodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::IrModule_strategy)
def test_ir::irmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ConnectivityVariable_strategy)
@settings(max_examples=50)
def test_ir::connectivityvariable_instantiation(instance):
    assert isinstance(instance, ir::ConnectivityVariable)

@given(instance=ir::Variable_strategy)
@settings(max_examples=50)
def test_ir::variable_instantiation(instance):
    assert isinstance(instance, ir::Variable)

@given(instance=ir::Variable_strategy)
def test_ir::variable_persistenceName_type(instance):
    assert isinstance(instance.persistenceName, str)


@given(instance=ir::Variable_strategy)
def test_ir::variable_persistenceName_setter(instance):
    original = instance.persistenceName
    instance.persistenceName = original
    assert instance.persistenceName == original

@given(instance=ir::Variable_strategy)
def test_ir::variable_const_type(instance):
    assert isinstance(instance.const, bool)


@given(instance=ir::Variable_strategy)
def test_ir::variable_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=ir::SimpleVariable_strategy)
@settings(max_examples=50)
def test_ir::simplevariable_instantiation(instance):
    assert isinstance(instance, ir::SimpleVariable)

@given(instance=IrAnnotable_strategy)
@settings(max_examples=50)
def test_irannotable_instantiation(instance):
    assert isinstance(instance, IrAnnotable)

@given(instance=ir::IterationBlock_strategy)
@settings(max_examples=50)
def test_ir::iterationblock_instantiation(instance):
    assert isinstance(instance, ir::IterationBlock)

@given(instance=ir::TimeLoopVariable_strategy)
@settings(max_examples=50)
def test_ir::timeloopvariable_instantiation(instance):
    assert isinstance(instance, ir::TimeLoopVariable)

@given(instance=ir::TimeLoopVariable_strategy)
def test_ir::timeloopvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TimeLoopVariable_strategy)
def test_ir::timeloopvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ItemId_strategy)
@settings(max_examples=50)
def test_ir::itemid_instantiation(instance):
    assert isinstance(instance, ir::ItemId)

@given(instance=ir::ItemId_strategy)
def test_ir::itemid_itemName_type(instance):
    assert isinstance(instance.itemName, str)


@given(instance=ir::ItemId_strategy)
def test_ir::itemid_itemName_setter(instance):
    original = instance.itemName
    instance.itemName = original
    assert instance.itemName == original

@given(instance=ir::ItemId_strategy)
def test_ir::itemid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ItemId_strategy)
def test_ir::itemid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::IrType_strategy)
@settings(max_examples=50)
def test_ir::irtype_instantiation(instance):
    assert isinstance(instance, ir::IrType)

@given(instance=ir::Container_strategy)
@settings(max_examples=50)
def test_ir::container_instantiation(instance):
    assert isinstance(instance, ir::Container)

@given(instance=ir::Instruction_strategy)
@settings(max_examples=50)
def test_ir::instruction_instantiation(instance):
    assert isinstance(instance, ir::Instruction)

@given(instance=ir::ArgOrVar_strategy)
@settings(max_examples=50)
def test_ir::argorvar_instantiation(instance):
    assert isinstance(instance, ir::ArgOrVar)

@given(instance=ir::ArgOrVar_strategy)
def test_ir::argorvar_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ArgOrVar_strategy)
def test_ir::argorvar_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Import_strategy)
@settings(max_examples=50)
def test_ir::import_instantiation(instance):
    assert isinstance(instance, ir::Import)

@given(instance=ir::Import_strategy)
def test_ir::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=ir::Import_strategy)
def test_ir::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ir::ItemType_strategy)
@settings(max_examples=50)
def test_ir::itemtype_instantiation(instance):
    assert isinstance(instance, ir::ItemType)

@given(instance=ir::ItemType_strategy)
def test_ir::itemtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ItemType_strategy)
def test_ir::itemtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::TimeLoopCopy_strategy)
@settings(max_examples=50)
def test_ir::timeloopcopy_instantiation(instance):
    assert isinstance(instance, ir::TimeLoopCopy)

@given(instance=ir::PostProcessingInfo_strategy)
@settings(max_examples=50)
def test_ir::postprocessinginfo_instantiation(instance):
    assert isinstance(instance, ir::PostProcessingInfo)

@given(instance=ir::PostProcessingInfo_strategy)
def test_ir::postprocessinginfo_periodValue_type(instance):
    assert isinstance(instance.periodValue, float)


@given(instance=ir::PostProcessingInfo_strategy)
def test_ir::postprocessinginfo_periodValue_setter(instance):
    original = instance.periodValue
    instance.periodValue = original
    assert instance.periodValue == original

@given(instance=ir::Connectivity_strategy)
@settings(max_examples=50)
def test_ir::connectivity_instantiation(instance):
    assert isinstance(instance, ir::Connectivity)

@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_indexEqualId_type(instance):
    assert isinstance(instance.indexEqualId, bool)


@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_indexEqualId_setter(instance):
    original = instance.indexEqualId
    instance.indexEqualId = original
    assert instance.indexEqualId == original

@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_multiple_type(instance):
    assert isinstance(instance.multiple, bool)


@given(instance=ir::Connectivity_strategy)
def test_ir::connectivity_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=ir::Expression_strategy)
@settings(max_examples=50)
def test_ir::expression_instantiation(instance):
    assert isinstance(instance, ir::Expression)

@given(instance=ir::Job_strategy)
@settings(max_examples=50)
def test_ir::job_instantiation(instance):
    assert isinstance(instance, ir::Job)

@given(instance=ir::Job_strategy)
def test_ir::job_onCycle_type(instance):
    assert isinstance(instance.onCycle, bool)


@given(instance=ir::Job_strategy)
def test_ir::job_onCycle_setter(instance):
    original = instance.onCycle
    instance.onCycle = original
    assert instance.onCycle == original

@given(instance=ir::Job_strategy)
def test_ir::job_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Job_strategy)
def test_ir::job_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::Job_strategy)
def test_ir::job_at_type(instance):
    assert isinstance(instance.at, float)


@given(instance=ir::Job_strategy)
def test_ir::job_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=ir::Function_strategy)
@settings(max_examples=50)
def test_ir::function_instantiation(instance):
    assert isinstance(instance, ir::Function)

@given(instance=ir::Function_strategy)
def test_ir::function_provider_type(instance):
    assert isinstance(instance.provider, str)


@given(instance=ir::Function_strategy)
def test_ir::function_provider_setter(instance):
    original = instance.provider
    instance.provider = original
    assert instance.provider == original

@given(instance=ir::Function_strategy)
def test_ir::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::Function_strategy)
def test_ir::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ItemIndexValue_strategy)
@settings(max_examples=50)
def test_ir::itemindexvalue_instantiation(instance):
    assert isinstance(instance, ir::ItemIndexValue)

@given(instance=ir::ItemIdValue_strategy)
@settings(max_examples=50)
def test_ir::itemidvalue_instantiation(instance):
    assert isinstance(instance, ir::ItemIdValue)

@given(instance=ir::TimeLoop_strategy)
@settings(max_examples=50)
def test_ir::timeloop_instantiation(instance):
    assert isinstance(instance, ir::TimeLoop)

@given(instance=ir::TimeLoop_strategy)
def test_ir::timeloop_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::TimeLoop_strategy)
def test_ir::timeloop_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ItemIndex_strategy)
@settings(max_examples=50)
def test_ir::itemindex_instantiation(instance):
    assert isinstance(instance, ir::ItemIndex)

@given(instance=ir::ItemIndex_strategy)
def test_ir::itemindex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ir::ItemIndex_strategy)
def test_ir::itemindex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir::ItemIndex_strategy)
def test_ir::itemindex_itemName_type(instance):
    assert isinstance(instance.itemName, str)


@given(instance=ir::ItemIndex_strategy)
def test_ir::itemindex_itemName_setter(instance):
    original = instance.itemName
    instance.itemName = original
    assert instance.itemName == original

@given(instance=ir::JobContainer_strategy)
@settings(max_examples=50)
def test_ir::jobcontainer_instantiation(instance):
    assert isinstance(instance, ir::JobContainer)

@given(instance=ir::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_ir::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, ir::EStringToStringMapEntry)

@given(instance=ir::IrAnnotation_strategy)
@settings(max_examples=50)
def test_ir::irannotation_instantiation(instance):
    assert isinstance(instance, ir::IrAnnotation)

@given(instance=ir::IrAnnotation_strategy)
def test_ir::irannotation_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=ir::IrAnnotation_strategy)
def test_ir::irannotation_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=ir::IrAnnotable_strategy)
@settings(max_examples=50)
def test_ir::irannotable_instantiation(instance):
    assert isinstance(instance, ir::IrAnnotable)
