import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    InfixOperator,
    cellsheet::Multiplication,
    cellsheet::GTE,
    cellsheet::Subtraction,
    cellsheet::Intersection,
    cellsheet::GT,
    cellsheet::Addition,
    cellsheet::NEQ,
    cellsheet::LT,
    cellsheet::LTE,
    cellsheet::Concatenation,
    cellsheet::Union,
    cellsheet::Division,
    cellsheet::EQ,
    cellsheet::Exponentiation,
    PostfixOperator,
    cellsheet::Percent,
    PrefixOperator,
    cellsheet::Negation,
    cellsheet::Plus,
    Operation,
    cellsheet::Function,
    Ref,
    cellsheet::RelativeRange,
    cellsheet::RelativeRef,
    Operand,
    cellsheet::Error,
    cellsheet::Logical,
    cellsheet::Number,
    cellsheet::Ref,
    cellsheet::Range,
    cellsheet::Text,
    Ast,
    cellsheet::Noop,
    cellsheet::PrefixOperator,
    cellsheet::PostfixOperator,
    cellsheet::Operation,
    cellsheet::InfixOperator,
    cellsheet::Unknown,
    cellsheet::Operand,
    cellsheet::AstEval,
    Cell,
    cellsheet::BooleanCell,
    cellsheet::TextCell,
    cellsheet::NumericCell,
    cellsheet::FormulaCell,
    cellsheet::DateCell,
    cellsheet::BlankCell,
    cellsheet::Ast,
    HasA1,
    HasId,
    cellsheet::Row,
    cellsheet::Cell,
    cellsheet::Sheet,
    cellsheet::CellFormat,
    cellsheet::Book,
    cellsheet::Workspace,
    cellsheet::HasId,
    cellsheet::HasA1,
    cellsheet::Token,
    cellsheet::EStringToTokenEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_infixoperator_is_not_abstract():
    assert not inspect.isabstract(InfixOperator)


def test_infixoperator_constructor_exists():
    assert callable(InfixOperator.__init__)


def test_infixoperator_constructor_args():
    sig = inspect.signature(InfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::multiplication_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Multiplication)


def test_cellsheet::multiplication_constructor_exists():
    assert callable(cellsheet::Multiplication.__init__)


def test_cellsheet::multiplication_constructor_args():
    sig = inspect.signature(cellsheet::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::gte_is_not_abstract():
    assert not inspect.isabstract(cellsheet::GTE)


def test_cellsheet::gte_constructor_exists():
    assert callable(cellsheet::GTE.__init__)


def test_cellsheet::gte_constructor_args():
    sig = inspect.signature(cellsheet::GTE.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::subtraction_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Subtraction)


def test_cellsheet::subtraction_constructor_exists():
    assert callable(cellsheet::Subtraction.__init__)


def test_cellsheet::subtraction_constructor_args():
    sig = inspect.signature(cellsheet::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::intersection_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Intersection)


def test_cellsheet::intersection_constructor_exists():
    assert callable(cellsheet::Intersection.__init__)


def test_cellsheet::intersection_constructor_args():
    sig = inspect.signature(cellsheet::Intersection.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::gt_is_not_abstract():
    assert not inspect.isabstract(cellsheet::GT)


def test_cellsheet::gt_constructor_exists():
    assert callable(cellsheet::GT.__init__)


def test_cellsheet::gt_constructor_args():
    sig = inspect.signature(cellsheet::GT.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::addition_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Addition)


def test_cellsheet::addition_constructor_exists():
    assert callable(cellsheet::Addition.__init__)


def test_cellsheet::addition_constructor_args():
    sig = inspect.signature(cellsheet::Addition.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::neq_is_not_abstract():
    assert not inspect.isabstract(cellsheet::NEQ)


def test_cellsheet::neq_constructor_exists():
    assert callable(cellsheet::NEQ.__init__)


def test_cellsheet::neq_constructor_args():
    sig = inspect.signature(cellsheet::NEQ.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::lt_is_not_abstract():
    assert not inspect.isabstract(cellsheet::LT)


def test_cellsheet::lt_constructor_exists():
    assert callable(cellsheet::LT.__init__)


def test_cellsheet::lt_constructor_args():
    sig = inspect.signature(cellsheet::LT.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::lte_is_not_abstract():
    assert not inspect.isabstract(cellsheet::LTE)


def test_cellsheet::lte_constructor_exists():
    assert callable(cellsheet::LTE.__init__)


def test_cellsheet::lte_constructor_args():
    sig = inspect.signature(cellsheet::LTE.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::concatenation_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Concatenation)


def test_cellsheet::concatenation_constructor_exists():
    assert callable(cellsheet::Concatenation.__init__)


def test_cellsheet::concatenation_constructor_args():
    sig = inspect.signature(cellsheet::Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::union_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Union)


def test_cellsheet::union_constructor_exists():
    assert callable(cellsheet::Union.__init__)


def test_cellsheet::union_constructor_args():
    sig = inspect.signature(cellsheet::Union.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::division_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Division)


def test_cellsheet::division_constructor_exists():
    assert callable(cellsheet::Division.__init__)


def test_cellsheet::division_constructor_args():
    sig = inspect.signature(cellsheet::Division.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::eq_is_not_abstract():
    assert not inspect.isabstract(cellsheet::EQ)


def test_cellsheet::eq_constructor_exists():
    assert callable(cellsheet::EQ.__init__)


def test_cellsheet::eq_constructor_args():
    sig = inspect.signature(cellsheet::EQ.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::exponentiation_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Exponentiation)


def test_cellsheet::exponentiation_constructor_exists():
    assert callable(cellsheet::Exponentiation.__init__)


def test_cellsheet::exponentiation_constructor_args():
    sig = inspect.signature(cellsheet::Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_postfixoperator_is_not_abstract():
    assert not inspect.isabstract(PostfixOperator)


def test_postfixoperator_constructor_exists():
    assert callable(PostfixOperator.__init__)


def test_postfixoperator_constructor_args():
    sig = inspect.signature(PostfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::percent_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Percent)


def test_cellsheet::percent_constructor_exists():
    assert callable(cellsheet::Percent.__init__)


def test_cellsheet::percent_constructor_args():
    sig = inspect.signature(cellsheet::Percent.__init__)
    params = list(sig.parameters.keys())



def test_prefixoperator_is_not_abstract():
    assert not inspect.isabstract(PrefixOperator)


def test_prefixoperator_constructor_exists():
    assert callable(PrefixOperator.__init__)


def test_prefixoperator_constructor_args():
    sig = inspect.signature(PrefixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::negation_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Negation)


def test_cellsheet::negation_constructor_exists():
    assert callable(cellsheet::Negation.__init__)


def test_cellsheet::negation_constructor_args():
    sig = inspect.signature(cellsheet::Negation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::plus_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Plus)


def test_cellsheet::plus_constructor_exists():
    assert callable(cellsheet::Plus.__init__)


def test_cellsheet::plus_constructor_args():
    sig = inspect.signature(cellsheet::Plus.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::function_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Function)


def test_cellsheet::function_constructor_exists():
    assert callable(cellsheet::Function.__init__)


def test_cellsheet::function_constructor_args():
    sig = inspect.signature(cellsheet::Function.__init__)
    params = list(sig.parameters.keys())



def test_ref_is_not_abstract():
    assert not inspect.isabstract(Ref)


def test_ref_constructor_exists():
    assert callable(Ref.__init__)


def test_ref_constructor_args():
    sig = inspect.signature(Ref.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::relativerange_is_not_abstract():
    assert not inspect.isabstract(cellsheet::RelativeRange)


def test_cellsheet::relativerange_constructor_exists():
    assert callable(cellsheet::RelativeRange.__init__)


def test_cellsheet::relativerange_constructor_args():
    sig = inspect.signature(cellsheet::RelativeRange.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::relativeref_is_not_abstract():
    assert not inspect.isabstract(cellsheet::RelativeRef)


def test_cellsheet::relativeref_constructor_exists():
    assert callable(cellsheet::RelativeRef.__init__)


def test_cellsheet::relativeref_constructor_args():
    sig = inspect.signature(cellsheet::RelativeRef.__init__)
    params = list(sig.parameters.keys())



def test_operand_is_not_abstract():
    assert not inspect.isabstract(Operand)


def test_operand_constructor_exists():
    assert callable(Operand.__init__)


def test_operand_constructor_args():
    sig = inspect.signature(Operand.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::error_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Error)


def test_cellsheet::error_constructor_exists():
    assert callable(cellsheet::Error.__init__)


def test_cellsheet::error_constructor_args():
    sig = inspect.signature(cellsheet::Error.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::logical_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Logical)


def test_cellsheet::logical_constructor_exists():
    assert callable(cellsheet::Logical.__init__)


def test_cellsheet::logical_constructor_args():
    sig = inspect.signature(cellsheet::Logical.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::number_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Number)


def test_cellsheet::number_constructor_exists():
    assert callable(cellsheet::Number.__init__)


def test_cellsheet::number_constructor_args():
    sig = inspect.signature(cellsheet::Number.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::ref_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Ref)


def test_cellsheet::ref_constructor_exists():
    assert callable(cellsheet::Ref.__init__)


def test_cellsheet::ref_constructor_args():
    sig = inspect.signature(cellsheet::Ref.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::range_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Range)


def test_cellsheet::range_constructor_exists():
    assert callable(cellsheet::Range.__init__)


def test_cellsheet::range_constructor_args():
    sig = inspect.signature(cellsheet::Range.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::text_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Text)


def test_cellsheet::text_constructor_exists():
    assert callable(cellsheet::Text.__init__)


def test_cellsheet::text_constructor_args():
    sig = inspect.signature(cellsheet::Text.__init__)
    params = list(sig.parameters.keys())



def test_ast_is_not_abstract():
    assert not inspect.isabstract(Ast)


def test_ast_constructor_exists():
    assert callable(Ast.__init__)


def test_ast_constructor_args():
    sig = inspect.signature(Ast.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::noop_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Noop)


def test_cellsheet::noop_constructor_exists():
    assert callable(cellsheet::Noop.__init__)


def test_cellsheet::noop_constructor_args():
    sig = inspect.signature(cellsheet::Noop.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::prefixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet::PrefixOperator)


def test_cellsheet::prefixoperator_constructor_exists():
    assert callable(cellsheet::PrefixOperator.__init__)


def test_cellsheet::prefixoperator_constructor_args():
    sig = inspect.signature(cellsheet::PrefixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::postfixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet::PostfixOperator)


def test_cellsheet::postfixoperator_constructor_exists():
    assert callable(cellsheet::PostfixOperator.__init__)


def test_cellsheet::postfixoperator_constructor_args():
    sig = inspect.signature(cellsheet::PostfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::operation_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Operation)


def test_cellsheet::operation_constructor_exists():
    assert callable(cellsheet::Operation.__init__)


def test_cellsheet::operation_constructor_args():
    sig = inspect.signature(cellsheet::Operation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::infixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet::InfixOperator)


def test_cellsheet::infixoperator_constructor_exists():
    assert callable(cellsheet::InfixOperator.__init__)


def test_cellsheet::infixoperator_constructor_args():
    sig = inspect.signature(cellsheet::InfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::unknown_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Unknown)


def test_cellsheet::unknown_constructor_exists():
    assert callable(cellsheet::Unknown.__init__)


def test_cellsheet::unknown_constructor_args():
    sig = inspect.signature(cellsheet::Unknown.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::operand_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Operand)


def test_cellsheet::operand_constructor_exists():
    assert callable(cellsheet::Operand.__init__)


def test_cellsheet::operand_constructor_args():
    sig = inspect.signature(cellsheet::Operand.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::asteval_is_not_abstract():
    assert not inspect.isabstract(cellsheet::AstEval)


def test_cellsheet::asteval_constructor_exists():
    assert callable(cellsheet::AstEval.__init__)


def test_cellsheet::asteval_constructor_args():
    sig = inspect.signature(cellsheet::AstEval.__init__)
    params = list(sig.parameters.keys())
    assert "numberValue" in params, "Missing parameter 'numberValue'"
    assert "text" in params, "Missing parameter 'text'"
    assert "isError" in params, "Missing parameter 'isError'"

def test_cellsheet::asteval_has_numberValue():
    assert hasattr(cellsheet::AstEval, "numberValue")
    descriptor = None
    for klass in cellsheet::AstEval.__mro__:
        if "numberValue" in klass.__dict__:
            descriptor = klass.__dict__["numberValue"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet::asteval_has_text():
    assert hasattr(cellsheet::AstEval, "text")
    descriptor = None
    for klass in cellsheet::AstEval.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet::asteval_has_isError():
    assert hasattr(cellsheet::AstEval, "isError")
    descriptor = None
    for klass in cellsheet::AstEval.__mro__:
        if "isError" in klass.__dict__:
            descriptor = klass.__dict__["isError"]
            break
    assert isinstance(descriptor, property)



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::booleancell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::BooleanCell)


def test_cellsheet::booleancell_constructor_exists():
    assert callable(cellsheet::BooleanCell.__init__)


def test_cellsheet::booleancell_constructor_args():
    sig = inspect.signature(cellsheet::BooleanCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::booleancell_has_value():
    assert hasattr(cellsheet::BooleanCell, "value")
    descriptor = None
    for klass in cellsheet::BooleanCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::textcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::TextCell)


def test_cellsheet::textcell_constructor_exists():
    assert callable(cellsheet::TextCell.__init__)


def test_cellsheet::textcell_constructor_args():
    sig = inspect.signature(cellsheet::TextCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::textcell_has_value():
    assert hasattr(cellsheet::TextCell, "value")
    descriptor = None
    for klass in cellsheet::TextCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::numericcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::NumericCell)


def test_cellsheet::numericcell_constructor_exists():
    assert callable(cellsheet::NumericCell.__init__)


def test_cellsheet::numericcell_constructor_args():
    sig = inspect.signature(cellsheet::NumericCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::numericcell_has_value():
    assert hasattr(cellsheet::NumericCell, "value")
    descriptor = None
    for klass in cellsheet::NumericCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::formulacell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::FormulaCell)


def test_cellsheet::formulacell_constructor_exists():
    assert callable(cellsheet::FormulaCell.__init__)


def test_cellsheet::formulacell_constructor_args():
    sig = inspect.signature(cellsheet::FormulaCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::formulacell_has_value():
    assert hasattr(cellsheet::FormulaCell, "value")
    descriptor = None
    for klass in cellsheet::FormulaCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::datecell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::DateCell)


def test_cellsheet::datecell_constructor_exists():
    assert callable(cellsheet::DateCell.__init__)


def test_cellsheet::datecell_constructor_args():
    sig = inspect.signature(cellsheet::DateCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::datecell_has_value():
    assert hasattr(cellsheet::DateCell, "value")
    descriptor = None
    for klass in cellsheet::DateCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::blankcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::BlankCell)


def test_cellsheet::blankcell_constructor_exists():
    assert callable(cellsheet::BlankCell.__init__)


def test_cellsheet::blankcell_constructor_args():
    sig = inspect.signature(cellsheet::BlankCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::blankcell_has_value():
    assert hasattr(cellsheet::BlankCell, "value")
    descriptor = None
    for klass in cellsheet::BlankCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::ast_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Ast)


def test_cellsheet::ast_constructor_exists():
    assert callable(cellsheet::Ast.__init__)


def test_cellsheet::ast_constructor_args():
    sig = inspect.signature(cellsheet::Ast.__init__)
    params = list(sig.parameters.keys())



def test_hasa1_is_not_abstract():
    assert not inspect.isabstract(HasA1)


def test_hasa1_constructor_exists():
    assert callable(HasA1.__init__)


def test_hasa1_constructor_args():
    sig = inspect.signature(HasA1.__init__)
    params = list(sig.parameters.keys())



def test_hasid_is_not_abstract():
    assert not inspect.isabstract(HasId)


def test_hasid_constructor_exists():
    assert callable(HasId.__init__)


def test_hasid_constructor_args():
    sig = inspect.signature(HasId.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::row_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Row)


def test_cellsheet::row_constructor_exists():
    assert callable(cellsheet::Row.__init__)


def test_cellsheet::row_constructor_args():
    sig = inspect.signature(cellsheet::Row.__init__)
    params = list(sig.parameters.keys())
    assert "rowIndex" in params, "Missing parameter 'rowIndex'"

def test_cellsheet::row_has_rowIndex():
    assert hasattr(cellsheet::Row, "rowIndex")
    descriptor = None
    for klass in cellsheet::Row.__mro__:
        if "rowIndex" in klass.__dict__:
            descriptor = klass.__dict__["rowIndex"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::cell_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Cell)


def test_cellsheet::cell_constructor_exists():
    assert callable(cellsheet::Cell.__init__)


def test_cellsheet::cell_constructor_args():
    sig = inspect.signature(cellsheet::Cell.__init__)
    params = list(sig.parameters.keys())
    assert "colIndex" in params, "Missing parameter 'colIndex'"

def test_cellsheet::cell_has_colIndex():
    assert hasattr(cellsheet::Cell, "colIndex")
    descriptor = None
    for klass in cellsheet::Cell.__mro__:
        if "colIndex" in klass.__dict__:
            descriptor = klass.__dict__["colIndex"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::sheet_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Sheet)


def test_cellsheet::sheet_constructor_exists():
    assert callable(cellsheet::Sheet.__init__)


def test_cellsheet::sheet_constructor_args():
    sig = inspect.signature(cellsheet::Sheet.__init__)
    params = list(sig.parameters.keys())
    assert "sheetIndex" in params, "Missing parameter 'sheetIndex'"
    assert "sheetName" in params, "Missing parameter 'sheetName'"

def test_cellsheet::sheet_has_sheetIndex():
    assert hasattr(cellsheet::Sheet, "sheetIndex")
    descriptor = None
    for klass in cellsheet::Sheet.__mro__:
        if "sheetIndex" in klass.__dict__:
            descriptor = klass.__dict__["sheetIndex"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet::sheet_has_sheetName():
    assert hasattr(cellsheet::Sheet, "sheetName")
    descriptor = None
    for klass in cellsheet::Sheet.__mro__:
        if "sheetName" in klass.__dict__:
            descriptor = klass.__dict__["sheetName"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::cellformat_is_not_abstract():
    assert not inspect.isabstract(cellsheet::CellFormat)


def test_cellsheet::cellformat_constructor_exists():
    assert callable(cellsheet::CellFormat.__init__)


def test_cellsheet::cellformat_constructor_args():
    sig = inspect.signature(cellsheet::CellFormat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::cellformat_has_value():
    assert hasattr(cellsheet::CellFormat, "value")
    descriptor = None
    for klass in cellsheet::CellFormat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::book_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Book)


def test_cellsheet::book_constructor_exists():
    assert callable(cellsheet::Book.__init__)


def test_cellsheet::book_constructor_args():
    sig = inspect.signature(cellsheet::Book.__init__)
    params = list(sig.parameters.keys())
    assert "bookname" in params, "Missing parameter 'bookname'"

def test_cellsheet::book_has_bookname():
    assert hasattr(cellsheet::Book, "bookname")
    descriptor = None
    for klass in cellsheet::Book.__mro__:
        if "bookname" in klass.__dict__:
            descriptor = klass.__dict__["bookname"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::workspace_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Workspace)


def test_cellsheet::workspace_constructor_exists():
    assert callable(cellsheet::Workspace.__init__)


def test_cellsheet::workspace_constructor_args():
    sig = inspect.signature(cellsheet::Workspace.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet::hasid_is_not_abstract():
    assert not inspect.isabstract(cellsheet::HasId)


def test_cellsheet::hasid_constructor_exists():
    assert callable(cellsheet::HasId.__init__)


def test_cellsheet::hasid_constructor_args():
    sig = inspect.signature(cellsheet::HasId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_cellsheet::hasid_has_id():
    assert hasattr(cellsheet::HasId, "id")
    descriptor = None
    for klass in cellsheet::HasId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::hasa1_is_not_abstract():
    assert not inspect.isabstract(cellsheet::HasA1)


def test_cellsheet::hasa1_constructor_exists():
    assert callable(cellsheet::HasA1.__init__)


def test_cellsheet::hasa1_constructor_args():
    sig = inspect.signature(cellsheet::HasA1.__init__)
    params = list(sig.parameters.keys())
    assert "a1" in params, "Missing parameter 'a1'"

def test_cellsheet::hasa1_has_a1():
    assert hasattr(cellsheet::HasA1, "a1")
    descriptor = None
    for klass in cellsheet::HasA1.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::token_is_not_abstract():
    assert not inspect.isabstract(cellsheet::Token)


def test_cellsheet::token_constructor_exists():
    assert callable(cellsheet::Token.__init__)


def test_cellsheet::token_constructor_args():
    sig = inspect.signature(cellsheet::Token.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet::token_has_value():
    assert hasattr(cellsheet::Token, "value")
    descriptor = None
    for klass in cellsheet::Token.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet::estringtotokenentry_is_not_abstract():
    assert not inspect.isabstract(cellsheet::EStringToTokenEntry)


def test_cellsheet::estringtotokenentry_constructor_exists():
    assert callable(cellsheet::EStringToTokenEntry.__init__)


def test_cellsheet::estringtotokenentry_constructor_args():
    sig = inspect.signature(cellsheet::EStringToTokenEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_cellsheet::estringtotokenentry_has_key():
    assert hasattr(cellsheet::EStringToTokenEntry, "key")
    descriptor = None
    for klass in cellsheet::EStringToTokenEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
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
InfixOperator_strategy = st.builds(
    InfixOperator,
)
cellsheet::Multiplication_strategy = st.builds(
    cellsheet::Multiplication,
)
cellsheet::GTE_strategy = st.builds(
    cellsheet::GTE,
)
cellsheet::Subtraction_strategy = st.builds(
    cellsheet::Subtraction,
)
cellsheet::Intersection_strategy = st.builds(
    cellsheet::Intersection,
)
cellsheet::GT_strategy = st.builds(
    cellsheet::GT,
)
cellsheet::Addition_strategy = st.builds(
    cellsheet::Addition,
)
cellsheet::NEQ_strategy = st.builds(
    cellsheet::NEQ,
)
cellsheet::LT_strategy = st.builds(
    cellsheet::LT,
)
cellsheet::LTE_strategy = st.builds(
    cellsheet::LTE,
)
cellsheet::Concatenation_strategy = st.builds(
    cellsheet::Concatenation,
)
cellsheet::Union_strategy = st.builds(
    cellsheet::Union,
)
cellsheet::Division_strategy = st.builds(
    cellsheet::Division,
)
cellsheet::EQ_strategy = st.builds(
    cellsheet::EQ,
)
cellsheet::Exponentiation_strategy = st.builds(
    cellsheet::Exponentiation,
)
PostfixOperator_strategy = st.builds(
    PostfixOperator,
)
cellsheet::Percent_strategy = st.builds(
    cellsheet::Percent,
)
PrefixOperator_strategy = st.builds(
    PrefixOperator,
)
cellsheet::Negation_strategy = st.builds(
    cellsheet::Negation,
)
cellsheet::Plus_strategy = st.builds(
    cellsheet::Plus,
)
Operation_strategy = st.builds(
    Operation,
)
cellsheet::Function_strategy = st.builds(
    cellsheet::Function,
)
Ref_strategy = st.builds(
    Ref,
)
cellsheet::RelativeRange_strategy = st.builds(
    cellsheet::RelativeRange,
)
cellsheet::RelativeRef_strategy = st.builds(
    cellsheet::RelativeRef,
)
Operand_strategy = st.builds(
    Operand,
)
cellsheet::Error_strategy = st.builds(
    cellsheet::Error,
)
cellsheet::Logical_strategy = st.builds(
    cellsheet::Logical,
)
cellsheet::Number_strategy = st.builds(
    cellsheet::Number,
)
cellsheet::Ref_strategy = st.builds(
    cellsheet::Ref,
)
cellsheet::Range_strategy = st.builds(
    cellsheet::Range,
)
cellsheet::Text_strategy = st.builds(
    cellsheet::Text,
)
Ast_strategy = st.builds(
    Ast,
)
cellsheet::Noop_strategy = st.builds(
    cellsheet::Noop,
)
cellsheet::PrefixOperator_strategy = st.builds(
    cellsheet::PrefixOperator,
)
cellsheet::PostfixOperator_strategy = st.builds(
    cellsheet::PostfixOperator,
)
cellsheet::Operation_strategy = st.builds(
    cellsheet::Operation,
)
cellsheet::InfixOperator_strategy = st.builds(
    cellsheet::InfixOperator,
)
cellsheet::Unknown_strategy = st.builds(
    cellsheet::Unknown,
)
cellsheet::Operand_strategy = st.builds(
    cellsheet::Operand,
)
cellsheet::AstEval_strategy = st.builds(
    cellsheet::AstEval,
    numberValue=
        safe_text,
    text=
        safe_text,
    isError=
        st.booleans()
)
Cell_strategy = st.builds(
    Cell,
)
cellsheet::BooleanCell_strategy = st.builds(
    cellsheet::BooleanCell,
    value=
        safe_text
)
cellsheet::TextCell_strategy = st.builds(
    cellsheet::TextCell,
    value=
        safe_text
)
cellsheet::NumericCell_strategy = st.builds(
    cellsheet::NumericCell,
    value=
        safe_text
)
cellsheet::FormulaCell_strategy = st.builds(
    cellsheet::FormulaCell,
    value=
        safe_text
)
cellsheet::DateCell_strategy = st.builds(
    cellsheet::DateCell,
    value=
        st.dates()
)
cellsheet::BlankCell_strategy = st.builds(
    cellsheet::BlankCell,
    value=
        safe_text
)
cellsheet::Ast_strategy = st.builds(
    cellsheet::Ast,
)
HasA1_strategy = st.builds(
    HasA1,
)
HasId_strategy = st.builds(
    HasId,
)
cellsheet::Row_strategy = st.builds(
    cellsheet::Row,
    rowIndex=
        st.integers()
)
cellsheet::Cell_strategy = st.builds(
    cellsheet::Cell,
    colIndex=
        st.integers()
)
cellsheet::Sheet_strategy = st.builds(
    cellsheet::Sheet,
    sheetIndex=
        st.integers(),
    sheetName=
        safe_text
)
cellsheet::CellFormat_strategy = st.builds(
    cellsheet::CellFormat,
    value=
        safe_text
)
cellsheet::Book_strategy = st.builds(
    cellsheet::Book,
    bookname=
        safe_text
)
cellsheet::Workspace_strategy = st.builds(
    cellsheet::Workspace,
)
cellsheet::HasId_strategy = st.builds(
    cellsheet::HasId,
    id=
        safe_text
)
cellsheet::HasA1_strategy = st.builds(
    cellsheet::HasA1,
    a1=
        safe_text
)
cellsheet::Token_strategy = st.builds(
    cellsheet::Token,
    value=
        safe_text
)
cellsheet::EStringToTokenEntry_strategy = st.builds(
    cellsheet::EStringToTokenEntry,
    key=
        safe_text
)

@given(instance=InfixOperator_strategy)
@settings(max_examples=50)
def test_infixoperator_instantiation(instance):
    assert isinstance(instance, InfixOperator)

@given(instance=cellsheet::Multiplication_strategy)
@settings(max_examples=50)
def test_cellsheet::multiplication_instantiation(instance):
    assert isinstance(instance, cellsheet::Multiplication)

@given(instance=cellsheet::GTE_strategy)
@settings(max_examples=50)
def test_cellsheet::gte_instantiation(instance):
    assert isinstance(instance, cellsheet::GTE)

@given(instance=cellsheet::Subtraction_strategy)
@settings(max_examples=50)
def test_cellsheet::subtraction_instantiation(instance):
    assert isinstance(instance, cellsheet::Subtraction)

@given(instance=cellsheet::Intersection_strategy)
@settings(max_examples=50)
def test_cellsheet::intersection_instantiation(instance):
    assert isinstance(instance, cellsheet::Intersection)

@given(instance=cellsheet::GT_strategy)
@settings(max_examples=50)
def test_cellsheet::gt_instantiation(instance):
    assert isinstance(instance, cellsheet::GT)

@given(instance=cellsheet::Addition_strategy)
@settings(max_examples=50)
def test_cellsheet::addition_instantiation(instance):
    assert isinstance(instance, cellsheet::Addition)

@given(instance=cellsheet::NEQ_strategy)
@settings(max_examples=50)
def test_cellsheet::neq_instantiation(instance):
    assert isinstance(instance, cellsheet::NEQ)

@given(instance=cellsheet::LT_strategy)
@settings(max_examples=50)
def test_cellsheet::lt_instantiation(instance):
    assert isinstance(instance, cellsheet::LT)

@given(instance=cellsheet::LTE_strategy)
@settings(max_examples=50)
def test_cellsheet::lte_instantiation(instance):
    assert isinstance(instance, cellsheet::LTE)

@given(instance=cellsheet::Concatenation_strategy)
@settings(max_examples=50)
def test_cellsheet::concatenation_instantiation(instance):
    assert isinstance(instance, cellsheet::Concatenation)

@given(instance=cellsheet::Union_strategy)
@settings(max_examples=50)
def test_cellsheet::union_instantiation(instance):
    assert isinstance(instance, cellsheet::Union)

@given(instance=cellsheet::Division_strategy)
@settings(max_examples=50)
def test_cellsheet::division_instantiation(instance):
    assert isinstance(instance, cellsheet::Division)

@given(instance=cellsheet::EQ_strategy)
@settings(max_examples=50)
def test_cellsheet::eq_instantiation(instance):
    assert isinstance(instance, cellsheet::EQ)

@given(instance=cellsheet::Exponentiation_strategy)
@settings(max_examples=50)
def test_cellsheet::exponentiation_instantiation(instance):
    assert isinstance(instance, cellsheet::Exponentiation)

@given(instance=PostfixOperator_strategy)
@settings(max_examples=50)
def test_postfixoperator_instantiation(instance):
    assert isinstance(instance, PostfixOperator)

@given(instance=cellsheet::Percent_strategy)
@settings(max_examples=50)
def test_cellsheet::percent_instantiation(instance):
    assert isinstance(instance, cellsheet::Percent)

@given(instance=PrefixOperator_strategy)
@settings(max_examples=50)
def test_prefixoperator_instantiation(instance):
    assert isinstance(instance, PrefixOperator)

@given(instance=cellsheet::Negation_strategy)
@settings(max_examples=50)
def test_cellsheet::negation_instantiation(instance):
    assert isinstance(instance, cellsheet::Negation)

@given(instance=cellsheet::Plus_strategy)
@settings(max_examples=50)
def test_cellsheet::plus_instantiation(instance):
    assert isinstance(instance, cellsheet::Plus)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=cellsheet::Function_strategy)
@settings(max_examples=50)
def test_cellsheet::function_instantiation(instance):
    assert isinstance(instance, cellsheet::Function)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)

@given(instance=cellsheet::RelativeRange_strategy)
@settings(max_examples=50)
def test_cellsheet::relativerange_instantiation(instance):
    assert isinstance(instance, cellsheet::RelativeRange)

@given(instance=cellsheet::RelativeRef_strategy)
@settings(max_examples=50)
def test_cellsheet::relativeref_instantiation(instance):
    assert isinstance(instance, cellsheet::RelativeRef)

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=cellsheet::Error_strategy)
@settings(max_examples=50)
def test_cellsheet::error_instantiation(instance):
    assert isinstance(instance, cellsheet::Error)

@given(instance=cellsheet::Logical_strategy)
@settings(max_examples=50)
def test_cellsheet::logical_instantiation(instance):
    assert isinstance(instance, cellsheet::Logical)

@given(instance=cellsheet::Number_strategy)
@settings(max_examples=50)
def test_cellsheet::number_instantiation(instance):
    assert isinstance(instance, cellsheet::Number)

@given(instance=cellsheet::Ref_strategy)
@settings(max_examples=50)
def test_cellsheet::ref_instantiation(instance):
    assert isinstance(instance, cellsheet::Ref)

@given(instance=cellsheet::Range_strategy)
@settings(max_examples=50)
def test_cellsheet::range_instantiation(instance):
    assert isinstance(instance, cellsheet::Range)

@given(instance=cellsheet::Text_strategy)
@settings(max_examples=50)
def test_cellsheet::text_instantiation(instance):
    assert isinstance(instance, cellsheet::Text)

@given(instance=Ast_strategy)
@settings(max_examples=50)
def test_ast_instantiation(instance):
    assert isinstance(instance, Ast)

@given(instance=cellsheet::Noop_strategy)
@settings(max_examples=50)
def test_cellsheet::noop_instantiation(instance):
    assert isinstance(instance, cellsheet::Noop)

@given(instance=cellsheet::PrefixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet::prefixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet::PrefixOperator)

@given(instance=cellsheet::PostfixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet::postfixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet::PostfixOperator)

@given(instance=cellsheet::Operation_strategy)
@settings(max_examples=50)
def test_cellsheet::operation_instantiation(instance):
    assert isinstance(instance, cellsheet::Operation)

@given(instance=cellsheet::InfixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet::infixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet::InfixOperator)

@given(instance=cellsheet::Unknown_strategy)
@settings(max_examples=50)
def test_cellsheet::unknown_instantiation(instance):
    assert isinstance(instance, cellsheet::Unknown)

@given(instance=cellsheet::Operand_strategy)
@settings(max_examples=50)
def test_cellsheet::operand_instantiation(instance):
    assert isinstance(instance, cellsheet::Operand)

@given(instance=cellsheet::AstEval_strategy)
@settings(max_examples=50)
def test_cellsheet::asteval_instantiation(instance):
    assert isinstance(instance, cellsheet::AstEval)

@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_numberValue_type(instance):
    assert isinstance(instance.numberValue, str)


@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_numberValue_setter(instance):
    original = instance.numberValue
    instance.numberValue = original
    assert instance.numberValue == original

@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_isError_type(instance):
    assert isinstance(instance.isError, bool)


@given(instance=cellsheet::AstEval_strategy)
def test_cellsheet::asteval_isError_setter(instance):
    original = instance.isError
    instance.isError = original
    assert instance.isError == original

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=cellsheet::BooleanCell_strategy)
@settings(max_examples=50)
def test_cellsheet::booleancell_instantiation(instance):
    assert isinstance(instance, cellsheet::BooleanCell)

@given(instance=cellsheet::BooleanCell_strategy)
def test_cellsheet::booleancell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::BooleanCell_strategy)
def test_cellsheet::booleancell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::TextCell_strategy)
@settings(max_examples=50)
def test_cellsheet::textcell_instantiation(instance):
    assert isinstance(instance, cellsheet::TextCell)

@given(instance=cellsheet::TextCell_strategy)
def test_cellsheet::textcell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::TextCell_strategy)
def test_cellsheet::textcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::NumericCell_strategy)
@settings(max_examples=50)
def test_cellsheet::numericcell_instantiation(instance):
    assert isinstance(instance, cellsheet::NumericCell)

@given(instance=cellsheet::NumericCell_strategy)
def test_cellsheet::numericcell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::NumericCell_strategy)
def test_cellsheet::numericcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::FormulaCell_strategy)
@settings(max_examples=50)
def test_cellsheet::formulacell_instantiation(instance):
    assert isinstance(instance, cellsheet::FormulaCell)

@given(instance=cellsheet::FormulaCell_strategy)
def test_cellsheet::formulacell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::FormulaCell_strategy)
def test_cellsheet::formulacell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::DateCell_strategy)
@settings(max_examples=50)
def test_cellsheet::datecell_instantiation(instance):
    assert isinstance(instance, cellsheet::DateCell)

@given(instance=cellsheet::DateCell_strategy)
def test_cellsheet::datecell_value_type(instance):
    assert isinstance(instance.value, date)


@given(instance=cellsheet::DateCell_strategy)
def test_cellsheet::datecell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::BlankCell_strategy)
@settings(max_examples=50)
def test_cellsheet::blankcell_instantiation(instance):
    assert isinstance(instance, cellsheet::BlankCell)

@given(instance=cellsheet::BlankCell_strategy)
def test_cellsheet::blankcell_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::BlankCell_strategy)
def test_cellsheet::blankcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::Ast_strategy)
@settings(max_examples=50)
def test_cellsheet::ast_instantiation(instance):
    assert isinstance(instance, cellsheet::Ast)

@given(instance=HasA1_strategy)
@settings(max_examples=50)
def test_hasa1_instantiation(instance):
    assert isinstance(instance, HasA1)

@given(instance=HasId_strategy)
@settings(max_examples=50)
def test_hasid_instantiation(instance):
    assert isinstance(instance, HasId)

@given(instance=cellsheet::Row_strategy)
@settings(max_examples=50)
def test_cellsheet::row_instantiation(instance):
    assert isinstance(instance, cellsheet::Row)

@given(instance=cellsheet::Row_strategy)
def test_cellsheet::row_rowIndex_type(instance):
    assert isinstance(instance.rowIndex, int)


@given(instance=cellsheet::Row_strategy)
def test_cellsheet::row_rowIndex_setter(instance):
    original = instance.rowIndex
    instance.rowIndex = original
    assert instance.rowIndex == original

@given(instance=cellsheet::Cell_strategy)
@settings(max_examples=50)
def test_cellsheet::cell_instantiation(instance):
    assert isinstance(instance, cellsheet::Cell)

@given(instance=cellsheet::Cell_strategy)
def test_cellsheet::cell_colIndex_type(instance):
    assert isinstance(instance.colIndex, int)


@given(instance=cellsheet::Cell_strategy)
def test_cellsheet::cell_colIndex_setter(instance):
    original = instance.colIndex
    instance.colIndex = original
    assert instance.colIndex == original

@given(instance=cellsheet::Sheet_strategy)
@settings(max_examples=50)
def test_cellsheet::sheet_instantiation(instance):
    assert isinstance(instance, cellsheet::Sheet)

@given(instance=cellsheet::Sheet_strategy)
def test_cellsheet::sheet_sheetIndex_type(instance):
    assert isinstance(instance.sheetIndex, int)


@given(instance=cellsheet::Sheet_strategy)
def test_cellsheet::sheet_sheetIndex_setter(instance):
    original = instance.sheetIndex
    instance.sheetIndex = original
    assert instance.sheetIndex == original

@given(instance=cellsheet::Sheet_strategy)
def test_cellsheet::sheet_sheetName_type(instance):
    assert isinstance(instance.sheetName, str)


@given(instance=cellsheet::Sheet_strategy)
def test_cellsheet::sheet_sheetName_setter(instance):
    original = instance.sheetName
    instance.sheetName = original
    assert instance.sheetName == original

@given(instance=cellsheet::CellFormat_strategy)
@settings(max_examples=50)
def test_cellsheet::cellformat_instantiation(instance):
    assert isinstance(instance, cellsheet::CellFormat)

@given(instance=cellsheet::CellFormat_strategy)
def test_cellsheet::cellformat_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::CellFormat_strategy)
def test_cellsheet::cellformat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::Book_strategy)
@settings(max_examples=50)
def test_cellsheet::book_instantiation(instance):
    assert isinstance(instance, cellsheet::Book)

@given(instance=cellsheet::Book_strategy)
def test_cellsheet::book_bookname_type(instance):
    assert isinstance(instance.bookname, str)


@given(instance=cellsheet::Book_strategy)
def test_cellsheet::book_bookname_setter(instance):
    original = instance.bookname
    instance.bookname = original
    assert instance.bookname == original

@given(instance=cellsheet::Workspace_strategy)
@settings(max_examples=50)
def test_cellsheet::workspace_instantiation(instance):
    assert isinstance(instance, cellsheet::Workspace)

@given(instance=cellsheet::HasId_strategy)
@settings(max_examples=50)
def test_cellsheet::hasid_instantiation(instance):
    assert isinstance(instance, cellsheet::HasId)

@given(instance=cellsheet::HasId_strategy)
def test_cellsheet::hasid_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=cellsheet::HasId_strategy)
def test_cellsheet::hasid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=cellsheet::HasA1_strategy)
@settings(max_examples=50)
def test_cellsheet::hasa1_instantiation(instance):
    assert isinstance(instance, cellsheet::HasA1)

@given(instance=cellsheet::HasA1_strategy)
def test_cellsheet::hasa1_a1_type(instance):
    assert isinstance(instance.a1, str)


@given(instance=cellsheet::HasA1_strategy)
def test_cellsheet::hasa1_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=cellsheet::Token_strategy)
@settings(max_examples=50)
def test_cellsheet::token_instantiation(instance):
    assert isinstance(instance, cellsheet::Token)

@given(instance=cellsheet::Token_strategy)
def test_cellsheet::token_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cellsheet::Token_strategy)
def test_cellsheet::token_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet::EStringToTokenEntry_strategy)
@settings(max_examples=50)
def test_cellsheet::estringtotokenentry_instantiation(instance):
    assert isinstance(instance, cellsheet::EStringToTokenEntry)

@given(instance=cellsheet::EStringToTokenEntry_strategy)
def test_cellsheet::estringtotokenentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=cellsheet::EStringToTokenEntry_strategy)
def test_cellsheet::estringtotokenentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original
