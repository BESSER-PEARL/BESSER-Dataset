import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    InfixOperator,
    cellsheet_Union,
    cellsheet_Addition,
    cellsheet_NEQ,
    cellsheet_LTE,
    cellsheet_Division,
    cellsheet_EQ,
    cellsheet_LT,
    cellsheet_Subtraction,
    cellsheet_Multiplication,
    cellsheet_GTE,
    cellsheet_Intersection,
    cellsheet_Concatenation,
    cellsheet_GT,
    cellsheet_Exponentiation,
    PostfixOperator,
    cellsheet_Percent,
    PrefixOperator,
    cellsheet_Negation,
    cellsheet_Plus,
    Operation,
    cellsheet_Function,
    Ref,
    cellsheet_RelativeRange,
    cellsheet_RelativeRef,
    Operand,
    cellsheet_Error,
    cellsheet_Number,
    cellsheet_Ref,
    cellsheet_Logical,
    cellsheet_Range,
    cellsheet_Text,
    Ast,
    cellsheet_Unknown,
    cellsheet_InfixOperator,
    cellsheet_PrefixOperator,
    cellsheet_Noop,
    cellsheet_Operation,
    cellsheet_PostfixOperator,
    cellsheet_Operand,
    cellsheet_AstEval,
    Cell,
    cellsheet_DateCell,
    cellsheet_TextCell,
    cellsheet_FormulaCell,
    cellsheet_BooleanCell,
    cellsheet_NumericCell,
    cellsheet_BlankCell,
    cellsheet_Ast,
    HasA1,
    HasId,
    cellsheet_CellFormat,
    cellsheet_Row,
    cellsheet_Cell,
    cellsheet_Sheet,
    cellsheet_Book,
    cellsheet_Workspace,
    cellsheet_HasId,
    cellsheet_HasA1,
    cellsheet_Token,
    cellsheet_EStringToTokenEntry,
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



def test_cellsheet_union_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Union)


def test_cellsheet_union_constructor_exists():
    assert callable(cellsheet_Union.__init__)


def test_cellsheet_union_constructor_args():
    sig = inspect.signature(cellsheet_Union.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_addition_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Addition)


def test_cellsheet_addition_constructor_exists():
    assert callable(cellsheet_Addition.__init__)


def test_cellsheet_addition_constructor_args():
    sig = inspect.signature(cellsheet_Addition.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_neq_is_not_abstract():
    assert not inspect.isabstract(cellsheet_NEQ)


def test_cellsheet_neq_constructor_exists():
    assert callable(cellsheet_NEQ.__init__)


def test_cellsheet_neq_constructor_args():
    sig = inspect.signature(cellsheet_NEQ.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_lte_is_not_abstract():
    assert not inspect.isabstract(cellsheet_LTE)


def test_cellsheet_lte_constructor_exists():
    assert callable(cellsheet_LTE.__init__)


def test_cellsheet_lte_constructor_args():
    sig = inspect.signature(cellsheet_LTE.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_division_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Division)


def test_cellsheet_division_constructor_exists():
    assert callable(cellsheet_Division.__init__)


def test_cellsheet_division_constructor_args():
    sig = inspect.signature(cellsheet_Division.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_eq_is_not_abstract():
    assert not inspect.isabstract(cellsheet_EQ)


def test_cellsheet_eq_constructor_exists():
    assert callable(cellsheet_EQ.__init__)


def test_cellsheet_eq_constructor_args():
    sig = inspect.signature(cellsheet_EQ.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_lt_is_not_abstract():
    assert not inspect.isabstract(cellsheet_LT)


def test_cellsheet_lt_constructor_exists():
    assert callable(cellsheet_LT.__init__)


def test_cellsheet_lt_constructor_args():
    sig = inspect.signature(cellsheet_LT.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_subtraction_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Subtraction)


def test_cellsheet_subtraction_constructor_exists():
    assert callable(cellsheet_Subtraction.__init__)


def test_cellsheet_subtraction_constructor_args():
    sig = inspect.signature(cellsheet_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_multiplication_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Multiplication)


def test_cellsheet_multiplication_constructor_exists():
    assert callable(cellsheet_Multiplication.__init__)


def test_cellsheet_multiplication_constructor_args():
    sig = inspect.signature(cellsheet_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_gte_is_not_abstract():
    assert not inspect.isabstract(cellsheet_GTE)


def test_cellsheet_gte_constructor_exists():
    assert callable(cellsheet_GTE.__init__)


def test_cellsheet_gte_constructor_args():
    sig = inspect.signature(cellsheet_GTE.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_intersection_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Intersection)


def test_cellsheet_intersection_constructor_exists():
    assert callable(cellsheet_Intersection.__init__)


def test_cellsheet_intersection_constructor_args():
    sig = inspect.signature(cellsheet_Intersection.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_concatenation_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Concatenation)


def test_cellsheet_concatenation_constructor_exists():
    assert callable(cellsheet_Concatenation.__init__)


def test_cellsheet_concatenation_constructor_args():
    sig = inspect.signature(cellsheet_Concatenation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_gt_is_not_abstract():
    assert not inspect.isabstract(cellsheet_GT)


def test_cellsheet_gt_constructor_exists():
    assert callable(cellsheet_GT.__init__)


def test_cellsheet_gt_constructor_args():
    sig = inspect.signature(cellsheet_GT.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_exponentiation_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Exponentiation)


def test_cellsheet_exponentiation_constructor_exists():
    assert callable(cellsheet_Exponentiation.__init__)


def test_cellsheet_exponentiation_constructor_args():
    sig = inspect.signature(cellsheet_Exponentiation.__init__)
    params = list(sig.parameters.keys())



def test_postfixoperator_is_not_abstract():
    assert not inspect.isabstract(PostfixOperator)


def test_postfixoperator_constructor_exists():
    assert callable(PostfixOperator.__init__)


def test_postfixoperator_constructor_args():
    sig = inspect.signature(PostfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_percent_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Percent)


def test_cellsheet_percent_constructor_exists():
    assert callable(cellsheet_Percent.__init__)


def test_cellsheet_percent_constructor_args():
    sig = inspect.signature(cellsheet_Percent.__init__)
    params = list(sig.parameters.keys())



def test_prefixoperator_is_not_abstract():
    assert not inspect.isabstract(PrefixOperator)


def test_prefixoperator_constructor_exists():
    assert callable(PrefixOperator.__init__)


def test_prefixoperator_constructor_args():
    sig = inspect.signature(PrefixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_negation_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Negation)


def test_cellsheet_negation_constructor_exists():
    assert callable(cellsheet_Negation.__init__)


def test_cellsheet_negation_constructor_args():
    sig = inspect.signature(cellsheet_Negation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_plus_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Plus)


def test_cellsheet_plus_constructor_exists():
    assert callable(cellsheet_Plus.__init__)


def test_cellsheet_plus_constructor_args():
    sig = inspect.signature(cellsheet_Plus.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_function_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Function)


def test_cellsheet_function_constructor_exists():
    assert callable(cellsheet_Function.__init__)


def test_cellsheet_function_constructor_args():
    sig = inspect.signature(cellsheet_Function.__init__)
    params = list(sig.parameters.keys())



def test_ref_is_not_abstract():
    assert not inspect.isabstract(Ref)


def test_ref_constructor_exists():
    assert callable(Ref.__init__)


def test_ref_constructor_args():
    sig = inspect.signature(Ref.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_relativerange_is_not_abstract():
    assert not inspect.isabstract(cellsheet_RelativeRange)


def test_cellsheet_relativerange_constructor_exists():
    assert callable(cellsheet_RelativeRange.__init__)


def test_cellsheet_relativerange_constructor_args():
    sig = inspect.signature(cellsheet_RelativeRange.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_relativeref_is_not_abstract():
    assert not inspect.isabstract(cellsheet_RelativeRef)


def test_cellsheet_relativeref_constructor_exists():
    assert callable(cellsheet_RelativeRef.__init__)


def test_cellsheet_relativeref_constructor_args():
    sig = inspect.signature(cellsheet_RelativeRef.__init__)
    params = list(sig.parameters.keys())



def test_operand_is_not_abstract():
    assert not inspect.isabstract(Operand)


def test_operand_constructor_exists():
    assert callable(Operand.__init__)


def test_operand_constructor_args():
    sig = inspect.signature(Operand.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_error_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Error)


def test_cellsheet_error_constructor_exists():
    assert callable(cellsheet_Error.__init__)


def test_cellsheet_error_constructor_args():
    sig = inspect.signature(cellsheet_Error.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_number_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Number)


def test_cellsheet_number_constructor_exists():
    assert callable(cellsheet_Number.__init__)


def test_cellsheet_number_constructor_args():
    sig = inspect.signature(cellsheet_Number.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_ref_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Ref)


def test_cellsheet_ref_constructor_exists():
    assert callable(cellsheet_Ref.__init__)


def test_cellsheet_ref_constructor_args():
    sig = inspect.signature(cellsheet_Ref.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_logical_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Logical)


def test_cellsheet_logical_constructor_exists():
    assert callable(cellsheet_Logical.__init__)


def test_cellsheet_logical_constructor_args():
    sig = inspect.signature(cellsheet_Logical.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_range_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Range)


def test_cellsheet_range_constructor_exists():
    assert callable(cellsheet_Range.__init__)


def test_cellsheet_range_constructor_args():
    sig = inspect.signature(cellsheet_Range.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_text_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Text)


def test_cellsheet_text_constructor_exists():
    assert callable(cellsheet_Text.__init__)


def test_cellsheet_text_constructor_args():
    sig = inspect.signature(cellsheet_Text.__init__)
    params = list(sig.parameters.keys())



def test_ast_is_not_abstract():
    assert not inspect.isabstract(Ast)


def test_ast_constructor_exists():
    assert callable(Ast.__init__)


def test_ast_constructor_args():
    sig = inspect.signature(Ast.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_unknown_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Unknown)


def test_cellsheet_unknown_constructor_exists():
    assert callable(cellsheet_Unknown.__init__)


def test_cellsheet_unknown_constructor_args():
    sig = inspect.signature(cellsheet_Unknown.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_infixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet_InfixOperator)


def test_cellsheet_infixoperator_constructor_exists():
    assert callable(cellsheet_InfixOperator.__init__)


def test_cellsheet_infixoperator_constructor_args():
    sig = inspect.signature(cellsheet_InfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_prefixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet_PrefixOperator)


def test_cellsheet_prefixoperator_constructor_exists():
    assert callable(cellsheet_PrefixOperator.__init__)


def test_cellsheet_prefixoperator_constructor_args():
    sig = inspect.signature(cellsheet_PrefixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_noop_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Noop)


def test_cellsheet_noop_constructor_exists():
    assert callable(cellsheet_Noop.__init__)


def test_cellsheet_noop_constructor_args():
    sig = inspect.signature(cellsheet_Noop.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_operation_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Operation)


def test_cellsheet_operation_constructor_exists():
    assert callable(cellsheet_Operation.__init__)


def test_cellsheet_operation_constructor_args():
    sig = inspect.signature(cellsheet_Operation.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_postfixoperator_is_not_abstract():
    assert not inspect.isabstract(cellsheet_PostfixOperator)


def test_cellsheet_postfixoperator_constructor_exists():
    assert callable(cellsheet_PostfixOperator.__init__)


def test_cellsheet_postfixoperator_constructor_args():
    sig = inspect.signature(cellsheet_PostfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_operand_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Operand)


def test_cellsheet_operand_constructor_exists():
    assert callable(cellsheet_Operand.__init__)


def test_cellsheet_operand_constructor_args():
    sig = inspect.signature(cellsheet_Operand.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_asteval_is_not_abstract():
    assert not inspect.isabstract(cellsheet_AstEval)


def test_cellsheet_asteval_constructor_exists():
    assert callable(cellsheet_AstEval.__init__)


def test_cellsheet_asteval_constructor_args():
    sig = inspect.signature(cellsheet_AstEval.__init__)
    params = list(sig.parameters.keys())
    assert "numberValue" in params, "Missing parameter 'numberValue'"
    assert "isError" in params, "Missing parameter 'isError'"
    assert "text" in params, "Missing parameter 'text'"

def test_cellsheet_asteval_has_numberValue():
    assert hasattr(cellsheet_AstEval, "numberValue")
    descriptor = None
    for klass in cellsheet_AstEval.__mro__:
        if "numberValue" in klass.__dict__:
            descriptor = klass.__dict__["numberValue"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet_asteval_has_isError():
    assert hasattr(cellsheet_AstEval, "isError")
    descriptor = None
    for klass in cellsheet_AstEval.__mro__:
        if "isError" in klass.__dict__:
            descriptor = klass.__dict__["isError"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet_asteval_has_text():
    assert hasattr(cellsheet_AstEval, "text")
    descriptor = None
    for klass in cellsheet_AstEval.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_cell_is_not_abstract():
    assert not inspect.isabstract(Cell)


def test_cell_constructor_exists():
    assert callable(Cell.__init__)


def test_cell_constructor_args():
    sig = inspect.signature(Cell.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_datecell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_DateCell)


def test_cellsheet_datecell_constructor_exists():
    assert callable(cellsheet_DateCell.__init__)


def test_cellsheet_datecell_constructor_args():
    sig = inspect.signature(cellsheet_DateCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_datecell_has_value():
    assert hasattr(cellsheet_DateCell, "value")
    descriptor = None
    for klass in cellsheet_DateCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_textcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_TextCell)


def test_cellsheet_textcell_constructor_exists():
    assert callable(cellsheet_TextCell.__init__)


def test_cellsheet_textcell_constructor_args():
    sig = inspect.signature(cellsheet_TextCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_textcell_has_value():
    assert hasattr(cellsheet_TextCell, "value")
    descriptor = None
    for klass in cellsheet_TextCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_formulacell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_FormulaCell)


def test_cellsheet_formulacell_constructor_exists():
    assert callable(cellsheet_FormulaCell.__init__)


def test_cellsheet_formulacell_constructor_args():
    sig = inspect.signature(cellsheet_FormulaCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_formulacell_has_value():
    assert hasattr(cellsheet_FormulaCell, "value")
    descriptor = None
    for klass in cellsheet_FormulaCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_booleancell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_BooleanCell)


def test_cellsheet_booleancell_constructor_exists():
    assert callable(cellsheet_BooleanCell.__init__)


def test_cellsheet_booleancell_constructor_args():
    sig = inspect.signature(cellsheet_BooleanCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_booleancell_has_value():
    assert hasattr(cellsheet_BooleanCell, "value")
    descriptor = None
    for klass in cellsheet_BooleanCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_numericcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_NumericCell)


def test_cellsheet_numericcell_constructor_exists():
    assert callable(cellsheet_NumericCell.__init__)


def test_cellsheet_numericcell_constructor_args():
    sig = inspect.signature(cellsheet_NumericCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_numericcell_has_value():
    assert hasattr(cellsheet_NumericCell, "value")
    descriptor = None
    for klass in cellsheet_NumericCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_blankcell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_BlankCell)


def test_cellsheet_blankcell_constructor_exists():
    assert callable(cellsheet_BlankCell.__init__)


def test_cellsheet_blankcell_constructor_args():
    sig = inspect.signature(cellsheet_BlankCell.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_blankcell_has_value():
    assert hasattr(cellsheet_BlankCell, "value")
    descriptor = None
    for klass in cellsheet_BlankCell.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_ast_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Ast)


def test_cellsheet_ast_constructor_exists():
    assert callable(cellsheet_Ast.__init__)


def test_cellsheet_ast_constructor_args():
    sig = inspect.signature(cellsheet_Ast.__init__)
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



def test_cellsheet_cellformat_is_not_abstract():
    assert not inspect.isabstract(cellsheet_CellFormat)


def test_cellsheet_cellformat_constructor_exists():
    assert callable(cellsheet_CellFormat.__init__)


def test_cellsheet_cellformat_constructor_args():
    sig = inspect.signature(cellsheet_CellFormat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_cellformat_has_value():
    assert hasattr(cellsheet_CellFormat, "value")
    descriptor = None
    for klass in cellsheet_CellFormat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_row_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Row)


def test_cellsheet_row_constructor_exists():
    assert callable(cellsheet_Row.__init__)


def test_cellsheet_row_constructor_args():
    sig = inspect.signature(cellsheet_Row.__init__)
    params = list(sig.parameters.keys())
    assert "rowIndex" in params, "Missing parameter 'rowIndex'"

def test_cellsheet_row_has_rowIndex():
    assert hasattr(cellsheet_Row, "rowIndex")
    descriptor = None
    for klass in cellsheet_Row.__mro__:
        if "rowIndex" in klass.__dict__:
            descriptor = klass.__dict__["rowIndex"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_cell_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Cell)


def test_cellsheet_cell_constructor_exists():
    assert callable(cellsheet_Cell.__init__)


def test_cellsheet_cell_constructor_args():
    sig = inspect.signature(cellsheet_Cell.__init__)
    params = list(sig.parameters.keys())
    assert "colIndex" in params, "Missing parameter 'colIndex'"

def test_cellsheet_cell_has_colIndex():
    assert hasattr(cellsheet_Cell, "colIndex")
    descriptor = None
    for klass in cellsheet_Cell.__mro__:
        if "colIndex" in klass.__dict__:
            descriptor = klass.__dict__["colIndex"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_sheet_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Sheet)


def test_cellsheet_sheet_constructor_exists():
    assert callable(cellsheet_Sheet.__init__)


def test_cellsheet_sheet_constructor_args():
    sig = inspect.signature(cellsheet_Sheet.__init__)
    params = list(sig.parameters.keys())
    assert "sheetIndex" in params, "Missing parameter 'sheetIndex'"
    assert "sheetName" in params, "Missing parameter 'sheetName'"

def test_cellsheet_sheet_has_sheetIndex():
    assert hasattr(cellsheet_Sheet, "sheetIndex")
    descriptor = None
    for klass in cellsheet_Sheet.__mro__:
        if "sheetIndex" in klass.__dict__:
            descriptor = klass.__dict__["sheetIndex"]
            break
    assert isinstance(descriptor, property)

def test_cellsheet_sheet_has_sheetName():
    assert hasattr(cellsheet_Sheet, "sheetName")
    descriptor = None
    for klass in cellsheet_Sheet.__mro__:
        if "sheetName" in klass.__dict__:
            descriptor = klass.__dict__["sheetName"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_book_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Book)


def test_cellsheet_book_constructor_exists():
    assert callable(cellsheet_Book.__init__)


def test_cellsheet_book_constructor_args():
    sig = inspect.signature(cellsheet_Book.__init__)
    params = list(sig.parameters.keys())
    assert "bookname" in params, "Missing parameter 'bookname'"

def test_cellsheet_book_has_bookname():
    assert hasattr(cellsheet_Book, "bookname")
    descriptor = None
    for klass in cellsheet_Book.__mro__:
        if "bookname" in klass.__dict__:
            descriptor = klass.__dict__["bookname"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_workspace_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Workspace)


def test_cellsheet_workspace_constructor_exists():
    assert callable(cellsheet_Workspace.__init__)


def test_cellsheet_workspace_constructor_args():
    sig = inspect.signature(cellsheet_Workspace.__init__)
    params = list(sig.parameters.keys())



def test_cellsheet_hasid_is_not_abstract():
    assert not inspect.isabstract(cellsheet_HasId)


def test_cellsheet_hasid_constructor_exists():
    assert callable(cellsheet_HasId.__init__)


def test_cellsheet_hasid_constructor_args():
    sig = inspect.signature(cellsheet_HasId.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_cellsheet_hasid_has_id():
    assert hasattr(cellsheet_HasId, "id")
    descriptor = None
    for klass in cellsheet_HasId.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_hasa1_is_not_abstract():
    assert not inspect.isabstract(cellsheet_HasA1)


def test_cellsheet_hasa1_constructor_exists():
    assert callable(cellsheet_HasA1.__init__)


def test_cellsheet_hasa1_constructor_args():
    sig = inspect.signature(cellsheet_HasA1.__init__)
    params = list(sig.parameters.keys())
    assert "a1" in params, "Missing parameter 'a1'"

def test_cellsheet_hasa1_has_a1():
    assert hasattr(cellsheet_HasA1, "a1")
    descriptor = None
    for klass in cellsheet_HasA1.__mro__:
        if "a1" in klass.__dict__:
            descriptor = klass.__dict__["a1"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_token_is_not_abstract():
    assert not inspect.isabstract(cellsheet_Token)


def test_cellsheet_token_constructor_exists():
    assert callable(cellsheet_Token.__init__)


def test_cellsheet_token_constructor_args():
    sig = inspect.signature(cellsheet_Token.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cellsheet_token_has_value():
    assert hasattr(cellsheet_Token, "value")
    descriptor = None
    for klass in cellsheet_Token.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cellsheet_estringtotokenentry_is_not_abstract():
    assert not inspect.isabstract(cellsheet_EStringToTokenEntry)


def test_cellsheet_estringtotokenentry_constructor_exists():
    assert callable(cellsheet_EStringToTokenEntry.__init__)


def test_cellsheet_estringtotokenentry_constructor_args():
    sig = inspect.signature(cellsheet_EStringToTokenEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_cellsheet_estringtotokenentry_has_key():
    assert hasattr(cellsheet_EStringToTokenEntry, "key")
    descriptor = None
    for klass in cellsheet_EStringToTokenEntry.__mro__:
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
cellsheet_Union_strategy = st.builds(
    cellsheet_Union,
)
cellsheet_Addition_strategy = st.builds(
    cellsheet_Addition,
)
cellsheet_NEQ_strategy = st.builds(
    cellsheet_NEQ,
)
cellsheet_LTE_strategy = st.builds(
    cellsheet_LTE,
)
cellsheet_Division_strategy = st.builds(
    cellsheet_Division,
)
cellsheet_EQ_strategy = st.builds(
    cellsheet_EQ,
)
cellsheet_LT_strategy = st.builds(
    cellsheet_LT,
)
cellsheet_Subtraction_strategy = st.builds(
    cellsheet_Subtraction,
)
cellsheet_Multiplication_strategy = st.builds(
    cellsheet_Multiplication,
)
cellsheet_GTE_strategy = st.builds(
    cellsheet_GTE,
)
cellsheet_Intersection_strategy = st.builds(
    cellsheet_Intersection,
)
cellsheet_Concatenation_strategy = st.builds(
    cellsheet_Concatenation,
)
cellsheet_GT_strategy = st.builds(
    cellsheet_GT,
)
cellsheet_Exponentiation_strategy = st.builds(
    cellsheet_Exponentiation,
)
PostfixOperator_strategy = st.builds(
    PostfixOperator,
)
cellsheet_Percent_strategy = st.builds(
    cellsheet_Percent,
)
PrefixOperator_strategy = st.builds(
    PrefixOperator,
)
cellsheet_Negation_strategy = st.builds(
    cellsheet_Negation,
)
cellsheet_Plus_strategy = st.builds(
    cellsheet_Plus,
)
Operation_strategy = st.builds(
    Operation,
)
cellsheet_Function_strategy = st.builds(
    cellsheet_Function,
)
Ref_strategy = st.builds(
    Ref,
)
cellsheet_RelativeRange_strategy = st.builds(
    cellsheet_RelativeRange,
)
cellsheet_RelativeRef_strategy = st.builds(
    cellsheet_RelativeRef,
)
Operand_strategy = st.builds(
    Operand,
)
cellsheet_Error_strategy = st.builds(
    cellsheet_Error,
)
cellsheet_Number_strategy = st.builds(
    cellsheet_Number,
)
cellsheet_Ref_strategy = st.builds(
    cellsheet_Ref,
)
cellsheet_Logical_strategy = st.builds(
    cellsheet_Logical,
)
cellsheet_Range_strategy = st.builds(
    cellsheet_Range,
)
cellsheet_Text_strategy = st.builds(
    cellsheet_Text,
)
Ast_strategy = st.builds(
    Ast,
)
cellsheet_Unknown_strategy = st.builds(
    cellsheet_Unknown,
)
cellsheet_InfixOperator_strategy = st.builds(
    cellsheet_InfixOperator,
)
cellsheet_PrefixOperator_strategy = st.builds(
    cellsheet_PrefixOperator,
)
cellsheet_Noop_strategy = st.builds(
    cellsheet_Noop,
)
cellsheet_Operation_strategy = st.builds(
    cellsheet_Operation,
)
cellsheet_PostfixOperator_strategy = st.builds(
    cellsheet_PostfixOperator,
)
cellsheet_Operand_strategy = st.builds(
    cellsheet_Operand,
)
cellsheet_AstEval_strategy = st.builds(
    cellsheet_AstEval,
    numberValue=
        safe_text,
    isError=
        st.booleans(),
    text=
        safe_text
)
Cell_strategy = st.builds(
    Cell,
)
cellsheet_DateCell_strategy = st.builds(
    cellsheet_DateCell,
    value=
        st.dates()
)
cellsheet_TextCell_strategy = st.builds(
    cellsheet_TextCell,
    value=
        safe_text
)
cellsheet_FormulaCell_strategy = st.builds(
    cellsheet_FormulaCell,
    value=
        safe_text
)
cellsheet_BooleanCell_strategy = st.builds(
    cellsheet_BooleanCell,
    value=
        safe_text
)
cellsheet_NumericCell_strategy = st.builds(
    cellsheet_NumericCell,
    value=
        safe_text
)
cellsheet_BlankCell_strategy = st.builds(
    cellsheet_BlankCell,
    value=
        safe_text
)
cellsheet_Ast_strategy = st.builds(
    cellsheet_Ast,
)
HasA1_strategy = st.builds(
    HasA1,
)
HasId_strategy = st.builds(
    HasId,
)
cellsheet_CellFormat_strategy = st.builds(
    cellsheet_CellFormat,
    value=
        safe_text
)
cellsheet_Row_strategy = st.builds(
    cellsheet_Row,
    rowIndex=
        st.integers()
)
cellsheet_Cell_strategy = st.builds(
    cellsheet_Cell,
    colIndex=
        st.integers()
)
cellsheet_Sheet_strategy = st.builds(
    cellsheet_Sheet,
    sheetIndex=
        st.integers(),
    sheetName=
        safe_text
)
cellsheet_Book_strategy = st.builds(
    cellsheet_Book,
    bookname=
        safe_text
)
cellsheet_Workspace_strategy = st.builds(
    cellsheet_Workspace,
)
cellsheet_HasId_strategy = st.builds(
    cellsheet_HasId,
    id=
        safe_text
)
cellsheet_HasA1_strategy = st.builds(
    cellsheet_HasA1,
    a1=
        safe_text
)
cellsheet_Token_strategy = st.builds(
    cellsheet_Token,
    value=
        safe_text
)
cellsheet_EStringToTokenEntry_strategy = st.builds(
    cellsheet_EStringToTokenEntry,
    key=
        safe_text
)

@given(instance=InfixOperator_strategy)
@settings(max_examples=50)
def test_infixoperator_instantiation(instance):
    assert isinstance(instance, InfixOperator)

@given(instance=cellsheet_Union_strategy)
@settings(max_examples=50)
def test_cellsheet_union_instantiation(instance):
    assert isinstance(instance, cellsheet_Union)

@given(instance=cellsheet_Addition_strategy)
@settings(max_examples=50)
def test_cellsheet_addition_instantiation(instance):
    assert isinstance(instance, cellsheet_Addition)

@given(instance=cellsheet_NEQ_strategy)
@settings(max_examples=50)
def test_cellsheet_neq_instantiation(instance):
    assert isinstance(instance, cellsheet_NEQ)

@given(instance=cellsheet_LTE_strategy)
@settings(max_examples=50)
def test_cellsheet_lte_instantiation(instance):
    assert isinstance(instance, cellsheet_LTE)

@given(instance=cellsheet_Division_strategy)
@settings(max_examples=50)
def test_cellsheet_division_instantiation(instance):
    assert isinstance(instance, cellsheet_Division)

@given(instance=cellsheet_EQ_strategy)
@settings(max_examples=50)
def test_cellsheet_eq_instantiation(instance):
    assert isinstance(instance, cellsheet_EQ)

@given(instance=cellsheet_LT_strategy)
@settings(max_examples=50)
def test_cellsheet_lt_instantiation(instance):
    assert isinstance(instance, cellsheet_LT)

@given(instance=cellsheet_Subtraction_strategy)
@settings(max_examples=50)
def test_cellsheet_subtraction_instantiation(instance):
    assert isinstance(instance, cellsheet_Subtraction)

@given(instance=cellsheet_Multiplication_strategy)
@settings(max_examples=50)
def test_cellsheet_multiplication_instantiation(instance):
    assert isinstance(instance, cellsheet_Multiplication)

@given(instance=cellsheet_GTE_strategy)
@settings(max_examples=50)
def test_cellsheet_gte_instantiation(instance):
    assert isinstance(instance, cellsheet_GTE)

@given(instance=cellsheet_Intersection_strategy)
@settings(max_examples=50)
def test_cellsheet_intersection_instantiation(instance):
    assert isinstance(instance, cellsheet_Intersection)

@given(instance=cellsheet_Concatenation_strategy)
@settings(max_examples=50)
def test_cellsheet_concatenation_instantiation(instance):
    assert isinstance(instance, cellsheet_Concatenation)

@given(instance=cellsheet_GT_strategy)
@settings(max_examples=50)
def test_cellsheet_gt_instantiation(instance):
    assert isinstance(instance, cellsheet_GT)

@given(instance=cellsheet_Exponentiation_strategy)
@settings(max_examples=50)
def test_cellsheet_exponentiation_instantiation(instance):
    assert isinstance(instance, cellsheet_Exponentiation)

@given(instance=PostfixOperator_strategy)
@settings(max_examples=50)
def test_postfixoperator_instantiation(instance):
    assert isinstance(instance, PostfixOperator)

@given(instance=cellsheet_Percent_strategy)
@settings(max_examples=50)
def test_cellsheet_percent_instantiation(instance):
    assert isinstance(instance, cellsheet_Percent)

@given(instance=PrefixOperator_strategy)
@settings(max_examples=50)
def test_prefixoperator_instantiation(instance):
    assert isinstance(instance, PrefixOperator)

@given(instance=cellsheet_Negation_strategy)
@settings(max_examples=50)
def test_cellsheet_negation_instantiation(instance):
    assert isinstance(instance, cellsheet_Negation)

@given(instance=cellsheet_Plus_strategy)
@settings(max_examples=50)
def test_cellsheet_plus_instantiation(instance):
    assert isinstance(instance, cellsheet_Plus)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=cellsheet_Function_strategy)
@settings(max_examples=50)
def test_cellsheet_function_instantiation(instance):
    assert isinstance(instance, cellsheet_Function)

@given(instance=Ref_strategy)
@settings(max_examples=50)
def test_ref_instantiation(instance):
    assert isinstance(instance, Ref)

@given(instance=cellsheet_RelativeRange_strategy)
@settings(max_examples=50)
def test_cellsheet_relativerange_instantiation(instance):
    assert isinstance(instance, cellsheet_RelativeRange)

@given(instance=cellsheet_RelativeRef_strategy)
@settings(max_examples=50)
def test_cellsheet_relativeref_instantiation(instance):
    assert isinstance(instance, cellsheet_RelativeRef)

@given(instance=Operand_strategy)
@settings(max_examples=50)
def test_operand_instantiation(instance):
    assert isinstance(instance, Operand)

@given(instance=cellsheet_Error_strategy)
@settings(max_examples=50)
def test_cellsheet_error_instantiation(instance):
    assert isinstance(instance, cellsheet_Error)

@given(instance=cellsheet_Number_strategy)
@settings(max_examples=50)
def test_cellsheet_number_instantiation(instance):
    assert isinstance(instance, cellsheet_Number)

@given(instance=cellsheet_Ref_strategy)
@settings(max_examples=50)
def test_cellsheet_ref_instantiation(instance):
    assert isinstance(instance, cellsheet_Ref)

@given(instance=cellsheet_Logical_strategy)
@settings(max_examples=50)
def test_cellsheet_logical_instantiation(instance):
    assert isinstance(instance, cellsheet_Logical)

@given(instance=cellsheet_Range_strategy)
@settings(max_examples=50)
def test_cellsheet_range_instantiation(instance):
    assert isinstance(instance, cellsheet_Range)

@given(instance=cellsheet_Text_strategy)
@settings(max_examples=50)
def test_cellsheet_text_instantiation(instance):
    assert isinstance(instance, cellsheet_Text)

@given(instance=Ast_strategy)
@settings(max_examples=50)
def test_ast_instantiation(instance):
    assert isinstance(instance, Ast)

@given(instance=cellsheet_Unknown_strategy)
@settings(max_examples=50)
def test_cellsheet_unknown_instantiation(instance):
    assert isinstance(instance, cellsheet_Unknown)

@given(instance=cellsheet_InfixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet_infixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet_InfixOperator)

@given(instance=cellsheet_PrefixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet_prefixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet_PrefixOperator)

@given(instance=cellsheet_Noop_strategy)
@settings(max_examples=50)
def test_cellsheet_noop_instantiation(instance):
    assert isinstance(instance, cellsheet_Noop)

@given(instance=cellsheet_Operation_strategy)
@settings(max_examples=50)
def test_cellsheet_operation_instantiation(instance):
    assert isinstance(instance, cellsheet_Operation)

@given(instance=cellsheet_PostfixOperator_strategy)
@settings(max_examples=50)
def test_cellsheet_postfixoperator_instantiation(instance):
    assert isinstance(instance, cellsheet_PostfixOperator)

@given(instance=cellsheet_Operand_strategy)
@settings(max_examples=50)
def test_cellsheet_operand_instantiation(instance):
    assert isinstance(instance, cellsheet_Operand)

@given(instance=cellsheet_AstEval_strategy)
@settings(max_examples=50)
def test_cellsheet_asteval_instantiation(instance):
    assert isinstance(instance, cellsheet_AstEval)



@given(instance=cellsheet_AstEval_strategy)
def test_cellsheet_asteval_numberValue_setter(instance):
    original = instance.numberValue
    instance.numberValue = original
    assert instance.numberValue == original



@given(instance=cellsheet_AstEval_strategy)
def test_cellsheet_asteval_isError_setter(instance):
    original = instance.isError
    instance.isError = original
    assert instance.isError == original



@given(instance=cellsheet_AstEval_strategy)
def test_cellsheet_asteval_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=Cell_strategy)
@settings(max_examples=50)
def test_cell_instantiation(instance):
    assert isinstance(instance, Cell)

@given(instance=cellsheet_DateCell_strategy)
@settings(max_examples=50)
def test_cellsheet_datecell_instantiation(instance):
    assert isinstance(instance, cellsheet_DateCell)



@given(instance=cellsheet_DateCell_strategy)
def test_cellsheet_datecell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_TextCell_strategy)
@settings(max_examples=50)
def test_cellsheet_textcell_instantiation(instance):
    assert isinstance(instance, cellsheet_TextCell)



@given(instance=cellsheet_TextCell_strategy)
def test_cellsheet_textcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_FormulaCell_strategy)
@settings(max_examples=50)
def test_cellsheet_formulacell_instantiation(instance):
    assert isinstance(instance, cellsheet_FormulaCell)



@given(instance=cellsheet_FormulaCell_strategy)
def test_cellsheet_formulacell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_BooleanCell_strategy)
@settings(max_examples=50)
def test_cellsheet_booleancell_instantiation(instance):
    assert isinstance(instance, cellsheet_BooleanCell)



@given(instance=cellsheet_BooleanCell_strategy)
def test_cellsheet_booleancell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_NumericCell_strategy)
@settings(max_examples=50)
def test_cellsheet_numericcell_instantiation(instance):
    assert isinstance(instance, cellsheet_NumericCell)



@given(instance=cellsheet_NumericCell_strategy)
def test_cellsheet_numericcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_BlankCell_strategy)
@settings(max_examples=50)
def test_cellsheet_blankcell_instantiation(instance):
    assert isinstance(instance, cellsheet_BlankCell)



@given(instance=cellsheet_BlankCell_strategy)
def test_cellsheet_blankcell_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_Ast_strategy)
@settings(max_examples=50)
def test_cellsheet_ast_instantiation(instance):
    assert isinstance(instance, cellsheet_Ast)

@given(instance=HasA1_strategy)
@settings(max_examples=50)
def test_hasa1_instantiation(instance):
    assert isinstance(instance, HasA1)

@given(instance=HasId_strategy)
@settings(max_examples=50)
def test_hasid_instantiation(instance):
    assert isinstance(instance, HasId)

@given(instance=cellsheet_CellFormat_strategy)
@settings(max_examples=50)
def test_cellsheet_cellformat_instantiation(instance):
    assert isinstance(instance, cellsheet_CellFormat)



@given(instance=cellsheet_CellFormat_strategy)
def test_cellsheet_cellformat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_Row_strategy)
@settings(max_examples=50)
def test_cellsheet_row_instantiation(instance):
    assert isinstance(instance, cellsheet_Row)



@given(instance=cellsheet_Row_strategy)
def test_cellsheet_row_rowIndex_setter(instance):
    original = instance.rowIndex
    instance.rowIndex = original
    assert instance.rowIndex == original

@given(instance=cellsheet_Cell_strategy)
@settings(max_examples=50)
def test_cellsheet_cell_instantiation(instance):
    assert isinstance(instance, cellsheet_Cell)



@given(instance=cellsheet_Cell_strategy)
def test_cellsheet_cell_colIndex_setter(instance):
    original = instance.colIndex
    instance.colIndex = original
    assert instance.colIndex == original

@given(instance=cellsheet_Sheet_strategy)
@settings(max_examples=50)
def test_cellsheet_sheet_instantiation(instance):
    assert isinstance(instance, cellsheet_Sheet)



@given(instance=cellsheet_Sheet_strategy)
def test_cellsheet_sheet_sheetIndex_setter(instance):
    original = instance.sheetIndex
    instance.sheetIndex = original
    assert instance.sheetIndex == original



@given(instance=cellsheet_Sheet_strategy)
def test_cellsheet_sheet_sheetName_setter(instance):
    original = instance.sheetName
    instance.sheetName = original
    assert instance.sheetName == original

@given(instance=cellsheet_Book_strategy)
@settings(max_examples=50)
def test_cellsheet_book_instantiation(instance):
    assert isinstance(instance, cellsheet_Book)



@given(instance=cellsheet_Book_strategy)
def test_cellsheet_book_bookname_setter(instance):
    original = instance.bookname
    instance.bookname = original
    assert instance.bookname == original

@given(instance=cellsheet_Workspace_strategy)
@settings(max_examples=50)
def test_cellsheet_workspace_instantiation(instance):
    assert isinstance(instance, cellsheet_Workspace)

@given(instance=cellsheet_HasId_strategy)
@settings(max_examples=50)
def test_cellsheet_hasid_instantiation(instance):
    assert isinstance(instance, cellsheet_HasId)



@given(instance=cellsheet_HasId_strategy)
def test_cellsheet_hasid_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=cellsheet_HasA1_strategy)
@settings(max_examples=50)
def test_cellsheet_hasa1_instantiation(instance):
    assert isinstance(instance, cellsheet_HasA1)



@given(instance=cellsheet_HasA1_strategy)
def test_cellsheet_hasa1_a1_setter(instance):
    original = instance.a1
    instance.a1 = original
    assert instance.a1 == original

@given(instance=cellsheet_Token_strategy)
@settings(max_examples=50)
def test_cellsheet_token_instantiation(instance):
    assert isinstance(instance, cellsheet_Token)



@given(instance=cellsheet_Token_strategy)
def test_cellsheet_token_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cellsheet_EStringToTokenEntry_strategy)
@settings(max_examples=50)
def test_cellsheet_estringtotokenentry_instantiation(instance):
    assert isinstance(instance, cellsheet_EStringToTokenEntry)



@given(instance=cellsheet_EStringToTokenEntry_strategy)
def test_cellsheet_estringtotokenentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original
