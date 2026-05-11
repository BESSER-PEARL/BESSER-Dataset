import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Definition,
    kernel::expressions::Affects,
    kernel::expressions::Defines,
    ElementReference,
    kernel::expressions::SubExpression,
    SubExpression,
    End,
    Start,
    ProcedureCall,
    Parameter,
    Member,
    references::ReferenceableElement,
    procedures::Procedure,
    ReturnSite,
    Argument,
    references::ElementReference,
    procedures::ProcedureCall,
    Expression,
    kernel::statements::Conditional,
    ExceptionHandlerStatement,
    kernel::references::ElementReference,
    kernel::references::Argument,
    kernel::references::Reference,
    NamedElement,
    kernel::references::ReferenceableElement,
    ReferenceableElement,
    DataItem,
    kernel::parameters::Parameter,
    commons::Variable,
    kernel::members::Member,
    MainProcedure,
    KernelRoot,
    kernel::containers::CompilationUnit,
    kernel::expressions::Usage,
    kernel::expressions::Definition,
    Usage,
    kernel::expressions::Uses,
    Jump,
    kernel::statements::Goto,
    LabellableElement,
    kernel::procedures::MainProcedure,
    kernel::containers::KernelRoot,
    kernel::expressions::Expression,
    statements::StatementListContainer,
    statements::Conditional,
    statements::StatementContainer,
    statements::Statement,
    kernel::statements::NonDeterministicBlock,
    kernel::statements::ProcedureCall,
    kernel::statements::Block,
    kernel::statements::ParallelBlock,
    kernel::statements::WhileLoop,
    kernel::statements::StatementWithException,
    kernel::statements::Condition,
    kernel::statements::StatementContainer,
    Statement,
    kernel::statements::Abort,
    kernel::statements::Skip,
    kernel::statements::Return,
    kernel::statements::Jump,
    kernel::statements::ExpressionStatement,
    kernel::statements::StatementListContainer,
    members::Member,
    kernel::dataitems::DataItem,
    commons::LabellableElement,
    kernel::statements::ExceptionHandlerStatement,
    kernel::procedures::Procedure,
    kernel::statements::Statement,
    kernel::commons::NamedElement,
    ExecutionOrder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::affects_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Affects)


def test_kernel::expressions::affects_constructor_exists():
    assert callable(kernel::expressions::Affects.__init__)


def test_kernel::expressions::affects_constructor_args():
    sig = inspect.signature(kernel::expressions::Affects.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::defines_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Defines)


def test_kernel::expressions::defines_constructor_exists():
    assert callable(kernel::expressions::Defines.__init__)


def test_kernel::expressions::defines_constructor_args():
    sig = inspect.signature(kernel::expressions::Defines.__init__)
    params = list(sig.parameters.keys())



def test_elementreference_is_not_abstract():
    assert not inspect.isabstract(ElementReference)


def test_elementreference_constructor_exists():
    assert callable(ElementReference.__init__)


def test_elementreference_constructor_args():
    sig = inspect.signature(ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::subexpression_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::SubExpression)


def test_kernel::expressions::subexpression_constructor_exists():
    assert callable(kernel::expressions::SubExpression.__init__)


def test_kernel::expressions::subexpression_constructor_args():
    sig = inspect.signature(kernel::expressions::SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_subexpression_is_not_abstract():
    assert not inspect.isabstract(SubExpression)


def test_subexpression_constructor_exists():
    assert callable(SubExpression.__init__)


def test_subexpression_constructor_args():
    sig = inspect.signature(SubExpression.__init__)
    params = list(sig.parameters.keys())



def test_end_is_not_abstract():
    assert not inspect.isabstract(End)


def test_end_constructor_exists():
    assert callable(End.__init__)


def test_end_constructor_args():
    sig = inspect.signature(End.__init__)
    params = list(sig.parameters.keys())



def test_start_is_not_abstract():
    assert not inspect.isabstract(Start)


def test_start_constructor_exists():
    assert callable(Start.__init__)


def test_start_constructor_args():
    sig = inspect.signature(Start.__init__)
    params = list(sig.parameters.keys())



def test_procedurecall_is_not_abstract():
    assert not inspect.isabstract(ProcedureCall)


def test_procedurecall_constructor_exists():
    assert callable(ProcedureCall.__init__)


def test_procedurecall_constructor_args():
    sig = inspect.signature(ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(references::ReferenceableElement)


def test_references::referenceableelement_constructor_exists():
    assert callable(references::ReferenceableElement.__init__)


def test_references::referenceableelement_constructor_args():
    sig = inspect.signature(references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_procedures::procedure_is_not_abstract():
    assert not inspect.isabstract(procedures::Procedure)


def test_procedures::procedure_constructor_exists():
    assert callable(procedures::Procedure.__init__)


def test_procedures::procedure_constructor_args():
    sig = inspect.signature(procedures::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_returnsite_is_not_abstract():
    assert not inspect.isabstract(ReturnSite)


def test_returnsite_constructor_exists():
    assert callable(ReturnSite.__init__)


def test_returnsite_constructor_args():
    sig = inspect.signature(ReturnSite.__init__)
    params = list(sig.parameters.keys())



def test_argument_is_not_abstract():
    assert not inspect.isabstract(Argument)


def test_argument_constructor_exists():
    assert callable(Argument.__init__)


def test_argument_constructor_args():
    sig = inspect.signature(Argument.__init__)
    params = list(sig.parameters.keys())



def test_references::elementreference_is_not_abstract():
    assert not inspect.isabstract(references::ElementReference)


def test_references::elementreference_constructor_exists():
    assert callable(references::ElementReference.__init__)


def test_references::elementreference_constructor_args():
    sig = inspect.signature(references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_procedures::procedurecall_is_not_abstract():
    assert not inspect.isabstract(procedures::ProcedureCall)


def test_procedures::procedurecall_constructor_exists():
    assert callable(procedures::ProcedureCall.__init__)


def test_procedures::procedurecall_constructor_args():
    sig = inspect.signature(procedures::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::conditional_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Conditional)


def test_kernel::statements::conditional_constructor_exists():
    assert callable(kernel::statements::Conditional.__init__)


def test_kernel::statements::conditional_constructor_args():
    sig = inspect.signature(kernel::statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_exceptionhandlerstatement_is_not_abstract():
    assert not inspect.isabstract(ExceptionHandlerStatement)


def test_exceptionhandlerstatement_constructor_exists():
    assert callable(ExceptionHandlerStatement.__init__)


def test_exceptionhandlerstatement_constructor_args():
    sig = inspect.signature(ExceptionHandlerStatement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::references::elementreference_is_not_abstract():
    assert not inspect.isabstract(kernel::references::ElementReference)


def test_kernel::references::elementreference_constructor_exists():
    assert callable(kernel::references::ElementReference.__init__)


def test_kernel::references::elementreference_constructor_args():
    sig = inspect.signature(kernel::references::ElementReference.__init__)
    params = list(sig.parameters.keys())



def test_kernel::references::argument_is_not_abstract():
    assert not inspect.isabstract(kernel::references::Argument)


def test_kernel::references::argument_constructor_exists():
    assert callable(kernel::references::Argument.__init__)


def test_kernel::references::argument_constructor_args():
    sig = inspect.signature(kernel::references::Argument.__init__)
    params = list(sig.parameters.keys())



def test_kernel::references::reference_is_not_abstract():
    assert not inspect.isabstract(kernel::references::Reference)


def test_kernel::references::reference_constructor_exists():
    assert callable(kernel::references::Reference.__init__)


def test_kernel::references::reference_constructor_args():
    sig = inspect.signature(kernel::references::Reference.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::references::referenceableelement_is_not_abstract():
    assert not inspect.isabstract(kernel::references::ReferenceableElement)


def test_kernel::references::referenceableelement_constructor_exists():
    assert callable(kernel::references::ReferenceableElement.__init__)


def test_kernel::references::referenceableelement_constructor_args():
    sig = inspect.signature(kernel::references::ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_referenceableelement_is_not_abstract():
    assert not inspect.isabstract(ReferenceableElement)


def test_referenceableelement_constructor_exists():
    assert callable(ReferenceableElement.__init__)


def test_referenceableelement_constructor_args():
    sig = inspect.signature(ReferenceableElement.__init__)
    params = list(sig.parameters.keys())



def test_dataitem_is_not_abstract():
    assert not inspect.isabstract(DataItem)


def test_dataitem_constructor_exists():
    assert callable(DataItem.__init__)


def test_dataitem_constructor_args():
    sig = inspect.signature(DataItem.__init__)
    params = list(sig.parameters.keys())



def test_kernel::parameters::parameter_is_not_abstract():
    assert not inspect.isabstract(kernel::parameters::Parameter)


def test_kernel::parameters::parameter_constructor_exists():
    assert callable(kernel::parameters::Parameter.__init__)


def test_kernel::parameters::parameter_constructor_args():
    sig = inspect.signature(kernel::parameters::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "byReference" in params, "Missing parameter 'byReference'"
    assert "correspondingArgument" in params, "Missing parameter 'correspondingArgument'"

def test_kernel::parameters::parameter_has_byReference():
    assert hasattr(kernel::parameters::Parameter, "byReference")
    descriptor = None
    for klass in kernel::parameters::Parameter.__mro__:
        if "byReference" in klass.__dict__:
            descriptor = klass.__dict__["byReference"]
            break
    assert isinstance(descriptor, property)

def test_kernel::parameters::parameter_has_correspondingArgument():
    assert hasattr(kernel::parameters::Parameter, "correspondingArgument")
    descriptor = None
    for klass in kernel::parameters::Parameter.__mro__:
        if "correspondingArgument" in klass.__dict__:
            descriptor = klass.__dict__["correspondingArgument"]
            break
    assert isinstance(descriptor, property)



def test_commons::variable_is_not_abstract():
    assert not inspect.isabstract(commons::Variable)


def test_commons::variable_constructor_exists():
    assert callable(commons::Variable.__init__)


def test_commons::variable_constructor_args():
    sig = inspect.signature(commons::Variable.__init__)
    params = list(sig.parameters.keys())



def test_kernel::members::member_is_not_abstract():
    assert not inspect.isabstract(kernel::members::Member)


def test_kernel::members::member_constructor_exists():
    assert callable(kernel::members::Member.__init__)


def test_kernel::members::member_constructor_args():
    sig = inspect.signature(kernel::members::Member.__init__)
    params = list(sig.parameters.keys())



def test_mainprocedure_is_not_abstract():
    assert not inspect.isabstract(MainProcedure)


def test_mainprocedure_constructor_exists():
    assert callable(MainProcedure.__init__)


def test_mainprocedure_constructor_args():
    sig = inspect.signature(MainProcedure.__init__)
    params = list(sig.parameters.keys())



def test_kernelroot_is_not_abstract():
    assert not inspect.isabstract(KernelRoot)


def test_kernelroot_constructor_exists():
    assert callable(KernelRoot.__init__)


def test_kernelroot_constructor_args():
    sig = inspect.signature(KernelRoot.__init__)
    params = list(sig.parameters.keys())



def test_kernel::containers::compilationunit_is_not_abstract():
    assert not inspect.isabstract(kernel::containers::CompilationUnit)


def test_kernel::containers::compilationunit_constructor_exists():
    assert callable(kernel::containers::CompilationUnit.__init__)


def test_kernel::containers::compilationunit_constructor_args():
    sig = inspect.signature(kernel::containers::CompilationUnit.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::usage_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Usage)


def test_kernel::expressions::usage_constructor_exists():
    assert callable(kernel::expressions::Usage.__init__)


def test_kernel::expressions::usage_constructor_args():
    sig = inspect.signature(kernel::expressions::Usage.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::definition_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Definition)


def test_kernel::expressions::definition_constructor_exists():
    assert callable(kernel::expressions::Definition.__init__)


def test_kernel::expressions::definition_constructor_args():
    sig = inspect.signature(kernel::expressions::Definition.__init__)
    params = list(sig.parameters.keys())



def test_usage_is_not_abstract():
    assert not inspect.isabstract(Usage)


def test_usage_constructor_exists():
    assert callable(Usage.__init__)


def test_usage_constructor_args():
    sig = inspect.signature(Usage.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::uses_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Uses)


def test_kernel::expressions::uses_constructor_exists():
    assert callable(kernel::expressions::Uses.__init__)


def test_kernel::expressions::uses_constructor_args():
    sig = inspect.signature(kernel::expressions::Uses.__init__)
    params = list(sig.parameters.keys())



def test_jump_is_not_abstract():
    assert not inspect.isabstract(Jump)


def test_jump_constructor_exists():
    assert callable(Jump.__init__)


def test_jump_constructor_args():
    sig = inspect.signature(Jump.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::goto_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Goto)


def test_kernel::statements::goto_constructor_exists():
    assert callable(kernel::statements::Goto.__init__)


def test_kernel::statements::goto_constructor_args():
    sig = inspect.signature(kernel::statements::Goto.__init__)
    params = list(sig.parameters.keys())



def test_labellableelement_is_not_abstract():
    assert not inspect.isabstract(LabellableElement)


def test_labellableelement_constructor_exists():
    assert callable(LabellableElement.__init__)


def test_labellableelement_constructor_args():
    sig = inspect.signature(LabellableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::procedures::mainprocedure_is_not_abstract():
    assert not inspect.isabstract(kernel::procedures::MainProcedure)


def test_kernel::procedures::mainprocedure_constructor_exists():
    assert callable(kernel::procedures::MainProcedure.__init__)


def test_kernel::procedures::mainprocedure_constructor_args():
    sig = inspect.signature(kernel::procedures::MainProcedure.__init__)
    params = list(sig.parameters.keys())



def test_kernel::containers::kernelroot_is_not_abstract():
    assert not inspect.isabstract(kernel::containers::KernelRoot)


def test_kernel::containers::kernelroot_constructor_exists():
    assert callable(kernel::containers::KernelRoot.__init__)


def test_kernel::containers::kernelroot_constructor_args():
    sig = inspect.signature(kernel::containers::KernelRoot.__init__)
    params = list(sig.parameters.keys())



def test_kernel::expressions::expression_is_not_abstract():
    assert not inspect.isabstract(kernel::expressions::Expression)


def test_kernel::expressions::expression_constructor_exists():
    assert callable(kernel::expressions::Expression.__init__)


def test_kernel::expressions::expression_constructor_args():
    sig = inspect.signature(kernel::expressions::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statements::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(statements::StatementListContainer)


def test_statements::statementlistcontainer_constructor_exists():
    assert callable(statements::StatementListContainer.__init__)


def test_statements::statementlistcontainer_constructor_args():
    sig = inspect.signature(statements::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_statements::conditional_is_not_abstract():
    assert not inspect.isabstract(statements::Conditional)


def test_statements::conditional_constructor_exists():
    assert callable(statements::Conditional.__init__)


def test_statements::conditional_constructor_args():
    sig = inspect.signature(statements::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_statements::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(statements::StatementContainer)


def test_statements::statementcontainer_constructor_exists():
    assert callable(statements::StatementContainer.__init__)


def test_statements::statementcontainer_constructor_args():
    sig = inspect.signature(statements::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_statements::statement_is_not_abstract():
    assert not inspect.isabstract(statements::Statement)


def test_statements::statement_constructor_exists():
    assert callable(statements::Statement.__init__)


def test_statements::statement_constructor_args():
    sig = inspect.signature(statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::nondeterministicblock_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::NonDeterministicBlock)


def test_kernel::statements::nondeterministicblock_constructor_exists():
    assert callable(kernel::statements::NonDeterministicBlock.__init__)


def test_kernel::statements::nondeterministicblock_constructor_args():
    sig = inspect.signature(kernel::statements::NonDeterministicBlock.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::procedurecall_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::ProcedureCall)


def test_kernel::statements::procedurecall_constructor_exists():
    assert callable(kernel::statements::ProcedureCall.__init__)


def test_kernel::statements::procedurecall_constructor_args():
    sig = inspect.signature(kernel::statements::ProcedureCall.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::block_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Block)


def test_kernel::statements::block_constructor_exists():
    assert callable(kernel::statements::Block.__init__)


def test_kernel::statements::block_constructor_args():
    sig = inspect.signature(kernel::statements::Block.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::parallelblock_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::ParallelBlock)


def test_kernel::statements::parallelblock_constructor_exists():
    assert callable(kernel::statements::ParallelBlock.__init__)


def test_kernel::statements::parallelblock_constructor_args():
    sig = inspect.signature(kernel::statements::ParallelBlock.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_kernel::statements::parallelblock_has_order():
    assert hasattr(kernel::statements::ParallelBlock, "order")
    descriptor = None
    for klass in kernel::statements::ParallelBlock.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_kernel::statements::whileloop_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::WhileLoop)


def test_kernel::statements::whileloop_constructor_exists():
    assert callable(kernel::statements::WhileLoop.__init__)


def test_kernel::statements::whileloop_constructor_args():
    sig = inspect.signature(kernel::statements::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::statementwithexception_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::StatementWithException)


def test_kernel::statements::statementwithexception_constructor_exists():
    assert callable(kernel::statements::StatementWithException.__init__)


def test_kernel::statements::statementwithexception_constructor_args():
    sig = inspect.signature(kernel::statements::StatementWithException.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::condition_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Condition)


def test_kernel::statements::condition_constructor_exists():
    assert callable(kernel::statements::Condition.__init__)


def test_kernel::statements::condition_constructor_args():
    sig = inspect.signature(kernel::statements::Condition.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::statementcontainer_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::StatementContainer)


def test_kernel::statements::statementcontainer_constructor_exists():
    assert callable(kernel::statements::StatementContainer.__init__)


def test_kernel::statements::statementcontainer_constructor_args():
    sig = inspect.signature(kernel::statements::StatementContainer.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::abort_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Abort)


def test_kernel::statements::abort_constructor_exists():
    assert callable(kernel::statements::Abort.__init__)


def test_kernel::statements::abort_constructor_args():
    sig = inspect.signature(kernel::statements::Abort.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::skip_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Skip)


def test_kernel::statements::skip_constructor_exists():
    assert callable(kernel::statements::Skip.__init__)


def test_kernel::statements::skip_constructor_args():
    sig = inspect.signature(kernel::statements::Skip.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::return_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Return)


def test_kernel::statements::return_constructor_exists():
    assert callable(kernel::statements::Return.__init__)


def test_kernel::statements::return_constructor_args():
    sig = inspect.signature(kernel::statements::Return.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::jump_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Jump)


def test_kernel::statements::jump_constructor_exists():
    assert callable(kernel::statements::Jump.__init__)


def test_kernel::statements::jump_constructor_args():
    sig = inspect.signature(kernel::statements::Jump.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::ExpressionStatement)


def test_kernel::statements::expressionstatement_constructor_exists():
    assert callable(kernel::statements::ExpressionStatement.__init__)


def test_kernel::statements::expressionstatement_constructor_args():
    sig = inspect.signature(kernel::statements::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::statementlistcontainer_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::StatementListContainer)


def test_kernel::statements::statementlistcontainer_constructor_exists():
    assert callable(kernel::statements::StatementListContainer.__init__)


def test_kernel::statements::statementlistcontainer_constructor_args():
    sig = inspect.signature(kernel::statements::StatementListContainer.__init__)
    params = list(sig.parameters.keys())



def test_members::member_is_not_abstract():
    assert not inspect.isabstract(members::Member)


def test_members::member_constructor_exists():
    assert callable(members::Member.__init__)


def test_members::member_constructor_args():
    sig = inspect.signature(members::Member.__init__)
    params = list(sig.parameters.keys())



def test_kernel::dataitems::dataitem_is_not_abstract():
    assert not inspect.isabstract(kernel::dataitems::DataItem)


def test_kernel::dataitems::dataitem_constructor_exists():
    assert callable(kernel::dataitems::DataItem.__init__)


def test_kernel::dataitems::dataitem_constructor_args():
    sig = inspect.signature(kernel::dataitems::DataItem.__init__)
    params = list(sig.parameters.keys())



def test_commons::labellableelement_is_not_abstract():
    assert not inspect.isabstract(commons::LabellableElement)


def test_commons::labellableelement_constructor_exists():
    assert callable(commons::LabellableElement.__init__)


def test_commons::labellableelement_constructor_args():
    sig = inspect.signature(commons::LabellableElement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::exceptionhandlerstatement_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::ExceptionHandlerStatement)


def test_kernel::statements::exceptionhandlerstatement_constructor_exists():
    assert callable(kernel::statements::ExceptionHandlerStatement.__init__)


def test_kernel::statements::exceptionhandlerstatement_constructor_args():
    sig = inspect.signature(kernel::statements::ExceptionHandlerStatement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::procedures::procedure_is_not_abstract():
    assert not inspect.isabstract(kernel::procedures::Procedure)


def test_kernel::procedures::procedure_constructor_exists():
    assert callable(kernel::procedures::Procedure.__init__)


def test_kernel::procedures::procedure_constructor_args():
    sig = inspect.signature(kernel::procedures::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_kernel::statements::statement_is_not_abstract():
    assert not inspect.isabstract(kernel::statements::Statement)


def test_kernel::statements::statement_constructor_exists():
    assert callable(kernel::statements::Statement.__init__)


def test_kernel::statements::statement_constructor_args():
    sig = inspect.signature(kernel::statements::Statement.__init__)
    params = list(sig.parameters.keys())



def test_kernel::commons::namedelement_is_not_abstract():
    assert not inspect.isabstract(kernel::commons::NamedElement)


def test_kernel::commons::namedelement_constructor_exists():
    assert callable(kernel::commons::NamedElement.__init__)


def test_kernel::commons::namedelement_constructor_args():
    sig = inspect.signature(kernel::commons::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kernel::commons::namedelement_has_name():
    assert hasattr(kernel::commons::NamedElement, "name")
    descriptor = None
    for klass in kernel::commons::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_executionorder_exists():
    # Check that the Enumeration exists
    assert ExecutionOrder is not None

def test_executionorder_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExecutionOrder]
    expected_literals = [
        "r2l",
        "interleaved",
        "l2r",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExecutionOrder"


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
Definition_strategy = st.builds(
    Definition,
)
kernel::expressions::Affects_strategy = st.builds(
    kernel::expressions::Affects,
)
kernel::expressions::Defines_strategy = st.builds(
    kernel::expressions::Defines,
)
ElementReference_strategy = st.builds(
    ElementReference,
)
kernel::expressions::SubExpression_strategy = st.builds(
    kernel::expressions::SubExpression,
)
SubExpression_strategy = st.builds(
    SubExpression,
)
End_strategy = st.builds(
    End,
)
Start_strategy = st.builds(
    Start,
)
ProcedureCall_strategy = st.builds(
    ProcedureCall,
)
Parameter_strategy = st.builds(
    Parameter,
)
Member_strategy = st.builds(
    Member,
)
references::ReferenceableElement_strategy = st.builds(
    references::ReferenceableElement,
)
procedures::Procedure_strategy = st.builds(
    procedures::Procedure,
)
ReturnSite_strategy = st.builds(
    ReturnSite,
)
Argument_strategy = st.builds(
    Argument,
)
references::ElementReference_strategy = st.builds(
    references::ElementReference,
)
procedures::ProcedureCall_strategy = st.builds(
    procedures::ProcedureCall,
)
Expression_strategy = st.builds(
    Expression,
)
kernel::statements::Conditional_strategy = st.builds(
    kernel::statements::Conditional,
)
ExceptionHandlerStatement_strategy = st.builds(
    ExceptionHandlerStatement,
)
kernel::references::ElementReference_strategy = st.builds(
    kernel::references::ElementReference,
)
kernel::references::Argument_strategy = st.builds(
    kernel::references::Argument,
)
kernel::references::Reference_strategy = st.builds(
    kernel::references::Reference,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
kernel::references::ReferenceableElement_strategy = st.builds(
    kernel::references::ReferenceableElement,
)
ReferenceableElement_strategy = st.builds(
    ReferenceableElement,
)
DataItem_strategy = st.builds(
    DataItem,
)
kernel::parameters::Parameter_strategy = st.builds(
    kernel::parameters::Parameter,
    byReference=
        st.booleans(),
    correspondingArgument=
        safe_text
)
commons::Variable_strategy = st.builds(
    commons::Variable,
)
kernel::members::Member_strategy = st.builds(
    kernel::members::Member,
)
MainProcedure_strategy = st.builds(
    MainProcedure,
)
KernelRoot_strategy = st.builds(
    KernelRoot,
)
kernel::containers::CompilationUnit_strategy = st.builds(
    kernel::containers::CompilationUnit,
)
kernel::expressions::Usage_strategy = st.builds(
    kernel::expressions::Usage,
)
kernel::expressions::Definition_strategy = st.builds(
    kernel::expressions::Definition,
)
Usage_strategy = st.builds(
    Usage,
)
kernel::expressions::Uses_strategy = st.builds(
    kernel::expressions::Uses,
)
Jump_strategy = st.builds(
    Jump,
)
kernel::statements::Goto_strategy = st.builds(
    kernel::statements::Goto,
)
LabellableElement_strategy = st.builds(
    LabellableElement,
)
kernel::procedures::MainProcedure_strategy = st.builds(
    kernel::procedures::MainProcedure,
)
kernel::containers::KernelRoot_strategy = st.builds(
    kernel::containers::KernelRoot,
)
kernel::expressions::Expression_strategy = st.builds(
    kernel::expressions::Expression,
)
statements::StatementListContainer_strategy = st.builds(
    statements::StatementListContainer,
)
statements::Conditional_strategy = st.builds(
    statements::Conditional,
)
statements::StatementContainer_strategy = st.builds(
    statements::StatementContainer,
)
statements::Statement_strategy = st.builds(
    statements::Statement,
)
kernel::statements::NonDeterministicBlock_strategy = st.builds(
    kernel::statements::NonDeterministicBlock,
)
kernel::statements::ProcedureCall_strategy = st.builds(
    kernel::statements::ProcedureCall,
)
kernel::statements::Block_strategy = st.builds(
    kernel::statements::Block,
)
kernel::statements::ParallelBlock_strategy = st.builds(
    kernel::statements::ParallelBlock,
    order=
        safe_text
)
kernel::statements::WhileLoop_strategy = st.builds(
    kernel::statements::WhileLoop,
)
kernel::statements::StatementWithException_strategy = st.builds(
    kernel::statements::StatementWithException,
)
kernel::statements::Condition_strategy = st.builds(
    kernel::statements::Condition,
)
kernel::statements::StatementContainer_strategy = st.builds(
    kernel::statements::StatementContainer,
)
Statement_strategy = st.builds(
    Statement,
)
kernel::statements::Abort_strategy = st.builds(
    kernel::statements::Abort,
)
kernel::statements::Skip_strategy = st.builds(
    kernel::statements::Skip,
)
kernel::statements::Return_strategy = st.builds(
    kernel::statements::Return,
)
kernel::statements::Jump_strategy = st.builds(
    kernel::statements::Jump,
)
kernel::statements::ExpressionStatement_strategy = st.builds(
    kernel::statements::ExpressionStatement,
)
kernel::statements::StatementListContainer_strategy = st.builds(
    kernel::statements::StatementListContainer,
)
members::Member_strategy = st.builds(
    members::Member,
)
kernel::dataitems::DataItem_strategy = st.builds(
    kernel::dataitems::DataItem,
)
commons::LabellableElement_strategy = st.builds(
    commons::LabellableElement,
)
kernel::statements::ExceptionHandlerStatement_strategy = st.builds(
    kernel::statements::ExceptionHandlerStatement,
)
kernel::procedures::Procedure_strategy = st.builds(
    kernel::procedures::Procedure,
)
kernel::statements::Statement_strategy = st.builds(
    kernel::statements::Statement,
)
kernel::commons::NamedElement_strategy = st.builds(
    kernel::commons::NamedElement,
    name=
        safe_text
)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=kernel::expressions::Affects_strategy)
@settings(max_examples=50)
def test_kernel::expressions::affects_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Affects)

@given(instance=kernel::expressions::Defines_strategy)
@settings(max_examples=50)
def test_kernel::expressions::defines_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Defines)

@given(instance=ElementReference_strategy)
@settings(max_examples=50)
def test_elementreference_instantiation(instance):
    assert isinstance(instance, ElementReference)

@given(instance=kernel::expressions::SubExpression_strategy)
@settings(max_examples=50)
def test_kernel::expressions::subexpression_instantiation(instance):
    assert isinstance(instance, kernel::expressions::SubExpression)

@given(instance=SubExpression_strategy)
@settings(max_examples=50)
def test_subexpression_instantiation(instance):
    assert isinstance(instance, SubExpression)

@given(instance=End_strategy)
@settings(max_examples=50)
def test_end_instantiation(instance):
    assert isinstance(instance, End)

@given(instance=Start_strategy)
@settings(max_examples=50)
def test_start_instantiation(instance):
    assert isinstance(instance, Start)

@given(instance=ProcedureCall_strategy)
@settings(max_examples=50)
def test_procedurecall_instantiation(instance):
    assert isinstance(instance, ProcedureCall)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_references::referenceableelement_instantiation(instance):
    assert isinstance(instance, references::ReferenceableElement)

@given(instance=procedures::Procedure_strategy)
@settings(max_examples=50)
def test_procedures::procedure_instantiation(instance):
    assert isinstance(instance, procedures::Procedure)

@given(instance=ReturnSite_strategy)
@settings(max_examples=50)
def test_returnsite_instantiation(instance):
    assert isinstance(instance, ReturnSite)

@given(instance=Argument_strategy)
@settings(max_examples=50)
def test_argument_instantiation(instance):
    assert isinstance(instance, Argument)

@given(instance=references::ElementReference_strategy)
@settings(max_examples=50)
def test_references::elementreference_instantiation(instance):
    assert isinstance(instance, references::ElementReference)

@given(instance=procedures::ProcedureCall_strategy)
@settings(max_examples=50)
def test_procedures::procedurecall_instantiation(instance):
    assert isinstance(instance, procedures::ProcedureCall)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=kernel::statements::Conditional_strategy)
@settings(max_examples=50)
def test_kernel::statements::conditional_instantiation(instance):
    assert isinstance(instance, kernel::statements::Conditional)

@given(instance=ExceptionHandlerStatement_strategy)
@settings(max_examples=50)
def test_exceptionhandlerstatement_instantiation(instance):
    assert isinstance(instance, ExceptionHandlerStatement)

@given(instance=kernel::references::ElementReference_strategy)
@settings(max_examples=50)
def test_kernel::references::elementreference_instantiation(instance):
    assert isinstance(instance, kernel::references::ElementReference)

@given(instance=kernel::references::Argument_strategy)
@settings(max_examples=50)
def test_kernel::references::argument_instantiation(instance):
    assert isinstance(instance, kernel::references::Argument)

@given(instance=kernel::references::Reference_strategy)
@settings(max_examples=50)
def test_kernel::references::reference_instantiation(instance):
    assert isinstance(instance, kernel::references::Reference)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=kernel::references::ReferenceableElement_strategy)
@settings(max_examples=50)
def test_kernel::references::referenceableelement_instantiation(instance):
    assert isinstance(instance, kernel::references::ReferenceableElement)

@given(instance=ReferenceableElement_strategy)
@settings(max_examples=50)
def test_referenceableelement_instantiation(instance):
    assert isinstance(instance, ReferenceableElement)

@given(instance=DataItem_strategy)
@settings(max_examples=50)
def test_dataitem_instantiation(instance):
    assert isinstance(instance, DataItem)

@given(instance=kernel::parameters::Parameter_strategy)
@settings(max_examples=50)
def test_kernel::parameters::parameter_instantiation(instance):
    assert isinstance(instance, kernel::parameters::Parameter)

@given(instance=kernel::parameters::Parameter_strategy)
def test_kernel::parameters::parameter_byReference_type(instance):
    assert isinstance(instance.byReference, bool)


@given(instance=kernel::parameters::Parameter_strategy)
def test_kernel::parameters::parameter_byReference_setter(instance):
    original = instance.byReference
    instance.byReference = original
    assert instance.byReference == original

@given(instance=kernel::parameters::Parameter_strategy)
def test_kernel::parameters::parameter_correspondingArgument_type(instance):
    assert isinstance(instance.correspondingArgument, str)


@given(instance=kernel::parameters::Parameter_strategy)
def test_kernel::parameters::parameter_correspondingArgument_setter(instance):
    original = instance.correspondingArgument
    instance.correspondingArgument = original
    assert instance.correspondingArgument == original

@given(instance=commons::Variable_strategy)
@settings(max_examples=50)
def test_commons::variable_instantiation(instance):
    assert isinstance(instance, commons::Variable)

@given(instance=kernel::members::Member_strategy)
@settings(max_examples=50)
def test_kernel::members::member_instantiation(instance):
    assert isinstance(instance, kernel::members::Member)

@given(instance=MainProcedure_strategy)
@settings(max_examples=50)
def test_mainprocedure_instantiation(instance):
    assert isinstance(instance, MainProcedure)

@given(instance=KernelRoot_strategy)
@settings(max_examples=50)
def test_kernelroot_instantiation(instance):
    assert isinstance(instance, KernelRoot)

@given(instance=kernel::containers::CompilationUnit_strategy)
@settings(max_examples=50)
def test_kernel::containers::compilationunit_instantiation(instance):
    assert isinstance(instance, kernel::containers::CompilationUnit)

@given(instance=kernel::expressions::Usage_strategy)
@settings(max_examples=50)
def test_kernel::expressions::usage_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Usage)

@given(instance=kernel::expressions::Definition_strategy)
@settings(max_examples=50)
def test_kernel::expressions::definition_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Definition)

@given(instance=Usage_strategy)
@settings(max_examples=50)
def test_usage_instantiation(instance):
    assert isinstance(instance, Usage)

@given(instance=kernel::expressions::Uses_strategy)
@settings(max_examples=50)
def test_kernel::expressions::uses_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Uses)

@given(instance=Jump_strategy)
@settings(max_examples=50)
def test_jump_instantiation(instance):
    assert isinstance(instance, Jump)

@given(instance=kernel::statements::Goto_strategy)
@settings(max_examples=50)
def test_kernel::statements::goto_instantiation(instance):
    assert isinstance(instance, kernel::statements::Goto)

@given(instance=LabellableElement_strategy)
@settings(max_examples=50)
def test_labellableelement_instantiation(instance):
    assert isinstance(instance, LabellableElement)

@given(instance=kernel::procedures::MainProcedure_strategy)
@settings(max_examples=50)
def test_kernel::procedures::mainprocedure_instantiation(instance):
    assert isinstance(instance, kernel::procedures::MainProcedure)

@given(instance=kernel::containers::KernelRoot_strategy)
@settings(max_examples=50)
def test_kernel::containers::kernelroot_instantiation(instance):
    assert isinstance(instance, kernel::containers::KernelRoot)

@given(instance=kernel::expressions::Expression_strategy)
@settings(max_examples=50)
def test_kernel::expressions::expression_instantiation(instance):
    assert isinstance(instance, kernel::expressions::Expression)

@given(instance=statements::StatementListContainer_strategy)
@settings(max_examples=50)
def test_statements::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, statements::StatementListContainer)

@given(instance=statements::Conditional_strategy)
@settings(max_examples=50)
def test_statements::conditional_instantiation(instance):
    assert isinstance(instance, statements::Conditional)

@given(instance=statements::StatementContainer_strategy)
@settings(max_examples=50)
def test_statements::statementcontainer_instantiation(instance):
    assert isinstance(instance, statements::StatementContainer)

@given(instance=statements::Statement_strategy)
@settings(max_examples=50)
def test_statements::statement_instantiation(instance):
    assert isinstance(instance, statements::Statement)

@given(instance=kernel::statements::NonDeterministicBlock_strategy)
@settings(max_examples=50)
def test_kernel::statements::nondeterministicblock_instantiation(instance):
    assert isinstance(instance, kernel::statements::NonDeterministicBlock)

@given(instance=kernel::statements::ProcedureCall_strategy)
@settings(max_examples=50)
def test_kernel::statements::procedurecall_instantiation(instance):
    assert isinstance(instance, kernel::statements::ProcedureCall)

@given(instance=kernel::statements::Block_strategy)
@settings(max_examples=50)
def test_kernel::statements::block_instantiation(instance):
    assert isinstance(instance, kernel::statements::Block)

@given(instance=kernel::statements::ParallelBlock_strategy)
@settings(max_examples=50)
def test_kernel::statements::parallelblock_instantiation(instance):
    assert isinstance(instance, kernel::statements::ParallelBlock)

@given(instance=kernel::statements::ParallelBlock_strategy)
def test_kernel::statements::parallelblock_order_type(instance):
    assert isinstance(instance.order, str)


@given(instance=kernel::statements::ParallelBlock_strategy)
def test_kernel::statements::parallelblock_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=kernel::statements::WhileLoop_strategy)
@settings(max_examples=50)
def test_kernel::statements::whileloop_instantiation(instance):
    assert isinstance(instance, kernel::statements::WhileLoop)

@given(instance=kernel::statements::StatementWithException_strategy)
@settings(max_examples=50)
def test_kernel::statements::statementwithexception_instantiation(instance):
    assert isinstance(instance, kernel::statements::StatementWithException)

@given(instance=kernel::statements::Condition_strategy)
@settings(max_examples=50)
def test_kernel::statements::condition_instantiation(instance):
    assert isinstance(instance, kernel::statements::Condition)

@given(instance=kernel::statements::StatementContainer_strategy)
@settings(max_examples=50)
def test_kernel::statements::statementcontainer_instantiation(instance):
    assert isinstance(instance, kernel::statements::StatementContainer)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=kernel::statements::Abort_strategy)
@settings(max_examples=50)
def test_kernel::statements::abort_instantiation(instance):
    assert isinstance(instance, kernel::statements::Abort)

@given(instance=kernel::statements::Skip_strategy)
@settings(max_examples=50)
def test_kernel::statements::skip_instantiation(instance):
    assert isinstance(instance, kernel::statements::Skip)

@given(instance=kernel::statements::Return_strategy)
@settings(max_examples=50)
def test_kernel::statements::return_instantiation(instance):
    assert isinstance(instance, kernel::statements::Return)

@given(instance=kernel::statements::Jump_strategy)
@settings(max_examples=50)
def test_kernel::statements::jump_instantiation(instance):
    assert isinstance(instance, kernel::statements::Jump)

@given(instance=kernel::statements::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_kernel::statements::expressionstatement_instantiation(instance):
    assert isinstance(instance, kernel::statements::ExpressionStatement)

@given(instance=kernel::statements::StatementListContainer_strategy)
@settings(max_examples=50)
def test_kernel::statements::statementlistcontainer_instantiation(instance):
    assert isinstance(instance, kernel::statements::StatementListContainer)

@given(instance=members::Member_strategy)
@settings(max_examples=50)
def test_members::member_instantiation(instance):
    assert isinstance(instance, members::Member)

@given(instance=kernel::dataitems::DataItem_strategy)
@settings(max_examples=50)
def test_kernel::dataitems::dataitem_instantiation(instance):
    assert isinstance(instance, kernel::dataitems::DataItem)

@given(instance=commons::LabellableElement_strategy)
@settings(max_examples=50)
def test_commons::labellableelement_instantiation(instance):
    assert isinstance(instance, commons::LabellableElement)

@given(instance=kernel::statements::ExceptionHandlerStatement_strategy)
@settings(max_examples=50)
def test_kernel::statements::exceptionhandlerstatement_instantiation(instance):
    assert isinstance(instance, kernel::statements::ExceptionHandlerStatement)

@given(instance=kernel::procedures::Procedure_strategy)
@settings(max_examples=50)
def test_kernel::procedures::procedure_instantiation(instance):
    assert isinstance(instance, kernel::procedures::Procedure)

@given(instance=kernel::statements::Statement_strategy)
@settings(max_examples=50)
def test_kernel::statements::statement_instantiation(instance):
    assert isinstance(instance, kernel::statements::Statement)

@given(instance=kernel::commons::NamedElement_strategy)
@settings(max_examples=50)
def test_kernel::commons::namedelement_instantiation(instance):
    assert isinstance(instance, kernel::commons::NamedElement)

@given(instance=kernel::commons::NamedElement_strategy)
def test_kernel::commons::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=kernel::commons::NamedElement_strategy)
def test_kernel::commons::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
