import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocltestmodel::MyClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocltestmodel::myclass_is_not_abstract():
    assert not inspect.isabstract(ocltestmodel::MyClass)


def test_ocltestmodel::myclass_constructor_exists():
    assert callable(ocltestmodel::MyClass.__init__)


def test_ocltestmodel::myclass_constructor_args():
    sig = inspect.signature(ocltestmodel::MyClass.__init__)
    params = list(sig.parameters.keys())
    assert "_IfExp2" in params, "Missing parameter '_IfExp2'"
    assert "string_replaceAll" in params, "Missing parameter 'string_replaceAll'"
    assert "boolean_not" in params, "Missing parameter 'boolean_not'"
    assert "integer_modulo" in params, "Missing parameter 'integer_modulo'"
    assert "_IntegerLiteralExp" in params, "Missing parameter '_IntegerLiteralExp'"
    assert "boolean_or" in params, "Missing parameter 'boolean_or'"
    assert "real_absolute" in params, "Missing parameter 'real_absolute'"
    assert "string_greaterthan" in params, "Missing parameter 'string_greaterthan'"
    assert "boolean_implies" in params, "Missing parameter 'boolean_implies'"
    assert "integer_absolute" in params, "Missing parameter 'integer_absolute'"
    assert "integer_multiplication" in params, "Missing parameter 'integer_multiplication'"
    assert "string_unequal" in params, "Missing parameter 'string_unequal'"
    assert "real_minimum" in params, "Missing parameter 'real_minimum'"
    assert "_IfExp" in params, "Missing parameter '_IfExp'"
    assert "tuple_literal" in params, "Missing parameter 'tuple_literal'"
    assert "let" in params, "Missing parameter 'let'"
    assert "unEmployed" in params, "Missing parameter 'unEmployed'"
    assert "string_at" in params, "Missing parameter 'string_at'"
    assert "integer_minimum" in params, "Missing parameter 'integer_minimum'"
    assert "string_greaterequals" in params, "Missing parameter 'string_greaterequals'"
    assert "integer_toString" in params, "Missing parameter 'integer_toString'"
    assert "real_subtraction" in params, "Missing parameter 'real_subtraction'"
    assert "real_greaterequals" in params, "Missing parameter 'real_greaterequals'"
    assert "string_compareTo" in params, "Missing parameter 'string_compareTo'"
    assert "real_multiplication" in params, "Missing parameter 'real_multiplication'"
    assert "string_lessthan" in params, "Missing parameter 'string_lessthan'"
    assert "boolean_and" in params, "Missing parameter 'boolean_and'"
    assert "real_floor" in params, "Missing parameter 'real_floor'"
    assert "integer_division" in params, "Missing parameter 'integer_division'"
    assert "integer_addition" in params, "Missing parameter 'integer_addition'"
    assert "real_toString" in params, "Missing parameter 'real_toString'"
    assert "let3" in params, "Missing parameter 'let3'"
    assert "string_size" in params, "Missing parameter 'string_size'"
    assert "real_addition" in params, "Missing parameter 'real_addition'"
    assert "integer_greaterthan" in params, "Missing parameter 'integer_greaterthan'"
    assert "string_concat" in params, "Missing parameter 'string_concat'"
    assert "boolean_equal" in params, "Missing parameter 'boolean_equal'"
    assert "string_addition" in params, "Missing parameter 'string_addition'"
    assert "boolean_xor" in params, "Missing parameter 'boolean_xor'"
    assert "orderedset_size" in params, "Missing parameter 'orderedset_size'"
    assert "_BooleanLiteralExp" in params, "Missing parameter '_BooleanLiteralExp'"
    assert "real_division" in params, "Missing parameter 'real_division'"
    assert "integer_lessequals" in params, "Missing parameter 'integer_lessequals'"
    assert "_StringLiteralExp" in params, "Missing parameter '_StringLiteralExp'"
    assert "let2" in params, "Missing parameter 'let2'"
    assert "integer_subtraction" in params, "Missing parameter 'integer_subtraction'"
    assert "boolean_unequal" in params, "Missing parameter 'boolean_unequal'"
    assert "integer_maximum" in params, "Missing parameter 'integer_maximum'"
    assert "integer_sequence" in params, "Missing parameter 'integer_sequence'"
    assert "string_indexOf" in params, "Missing parameter 'string_indexOf'"
    assert "_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER" in params, "Missing parameter '_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER'"
    assert "_RealLiteralExp" in params, "Missing parameter '_RealLiteralExp'"
    assert "sequence_selectByKind" in params, "Missing parameter 'sequence_selectByKind'"
    assert "static_sequence" in params, "Missing parameter 'static_sequence'"
    assert "string_equal" in params, "Missing parameter 'string_equal'"
    assert "string_equalsIgnoreCase" in params, "Missing parameter 'string_equalsIgnoreCase'"
    assert "real_lessequals" in params, "Missing parameter 'real_lessequals'"
    assert "real_greaterthan" in params, "Missing parameter 'real_greaterthan'"
    assert "real_lessthan" in params, "Missing parameter 'real_lessthan'"
    assert "boolean_toString" in params, "Missing parameter 'boolean_toString'"
    assert "_NumberLiteralExp" in params, "Missing parameter '_NumberLiteralExp'"
    assert "string_lastIndexOf" in params, "Missing parameter 'string_lastIndexOf'"
    assert "integer_greaterequals" in params, "Missing parameter 'integer_greaterequals'"
    assert "integer_lessthan" in params, "Missing parameter 'integer_lessthan'"
    assert "sequence_selectByType" in params, "Missing parameter 'sequence_selectByType'"
    assert "collection_literals" in params, "Missing parameter 'collection_literals'"
    assert "real_maximum" in params, "Missing parameter 'real_maximum'"
    assert "string_lessequals" in params, "Missing parameter 'string_lessequals'"
    assert "sequence_count" in params, "Missing parameter 'sequence_count'"

def test_ocltestmodel::myclass_has__IfExp2():
    assert hasattr(ocltestmodel::MyClass, "_IfExp2")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_IfExp2" in klass.__dict__:
            descriptor = klass.__dict__["_IfExp2"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_replaceAll():
    assert hasattr(ocltestmodel::MyClass, "string_replaceAll")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_replaceAll" in klass.__dict__:
            descriptor = klass.__dict__["string_replaceAll"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_not():
    assert hasattr(ocltestmodel::MyClass, "boolean_not")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_not" in klass.__dict__:
            descriptor = klass.__dict__["boolean_not"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_modulo():
    assert hasattr(ocltestmodel::MyClass, "integer_modulo")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_modulo" in klass.__dict__:
            descriptor = klass.__dict__["integer_modulo"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__IntegerLiteralExp():
    assert hasattr(ocltestmodel::MyClass, "_IntegerLiteralExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_IntegerLiteralExp" in klass.__dict__:
            descriptor = klass.__dict__["_IntegerLiteralExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_or():
    assert hasattr(ocltestmodel::MyClass, "boolean_or")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_or" in klass.__dict__:
            descriptor = klass.__dict__["boolean_or"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_absolute():
    assert hasattr(ocltestmodel::MyClass, "real_absolute")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_absolute" in klass.__dict__:
            descriptor = klass.__dict__["real_absolute"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_greaterthan():
    assert hasattr(ocltestmodel::MyClass, "string_greaterthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_greaterthan" in klass.__dict__:
            descriptor = klass.__dict__["string_greaterthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_implies():
    assert hasattr(ocltestmodel::MyClass, "boolean_implies")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_implies" in klass.__dict__:
            descriptor = klass.__dict__["boolean_implies"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_absolute():
    assert hasattr(ocltestmodel::MyClass, "integer_absolute")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_absolute" in klass.__dict__:
            descriptor = klass.__dict__["integer_absolute"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_multiplication():
    assert hasattr(ocltestmodel::MyClass, "integer_multiplication")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_multiplication" in klass.__dict__:
            descriptor = klass.__dict__["integer_multiplication"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_unequal():
    assert hasattr(ocltestmodel::MyClass, "string_unequal")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_unequal" in klass.__dict__:
            descriptor = klass.__dict__["string_unequal"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_minimum():
    assert hasattr(ocltestmodel::MyClass, "real_minimum")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_minimum" in klass.__dict__:
            descriptor = klass.__dict__["real_minimum"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__IfExp():
    assert hasattr(ocltestmodel::MyClass, "_IfExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_IfExp" in klass.__dict__:
            descriptor = klass.__dict__["_IfExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_tuple_literal():
    assert hasattr(ocltestmodel::MyClass, "tuple_literal")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "tuple_literal" in klass.__dict__:
            descriptor = klass.__dict__["tuple_literal"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_let():
    assert hasattr(ocltestmodel::MyClass, "let")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "let" in klass.__dict__:
            descriptor = klass.__dict__["let"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_unEmployed():
    assert hasattr(ocltestmodel::MyClass, "unEmployed")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "unEmployed" in klass.__dict__:
            descriptor = klass.__dict__["unEmployed"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_at():
    assert hasattr(ocltestmodel::MyClass, "string_at")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_at" in klass.__dict__:
            descriptor = klass.__dict__["string_at"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_minimum():
    assert hasattr(ocltestmodel::MyClass, "integer_minimum")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_minimum" in klass.__dict__:
            descriptor = klass.__dict__["integer_minimum"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_greaterequals():
    assert hasattr(ocltestmodel::MyClass, "string_greaterequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_greaterequals" in klass.__dict__:
            descriptor = klass.__dict__["string_greaterequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_toString():
    assert hasattr(ocltestmodel::MyClass, "integer_toString")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_toString" in klass.__dict__:
            descriptor = klass.__dict__["integer_toString"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_subtraction():
    assert hasattr(ocltestmodel::MyClass, "real_subtraction")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_subtraction" in klass.__dict__:
            descriptor = klass.__dict__["real_subtraction"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_greaterequals():
    assert hasattr(ocltestmodel::MyClass, "real_greaterequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_greaterequals" in klass.__dict__:
            descriptor = klass.__dict__["real_greaterequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_compareTo():
    assert hasattr(ocltestmodel::MyClass, "string_compareTo")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_compareTo" in klass.__dict__:
            descriptor = klass.__dict__["string_compareTo"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_multiplication():
    assert hasattr(ocltestmodel::MyClass, "real_multiplication")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_multiplication" in klass.__dict__:
            descriptor = klass.__dict__["real_multiplication"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_lessthan():
    assert hasattr(ocltestmodel::MyClass, "string_lessthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_lessthan" in klass.__dict__:
            descriptor = klass.__dict__["string_lessthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_and():
    assert hasattr(ocltestmodel::MyClass, "boolean_and")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_and" in klass.__dict__:
            descriptor = klass.__dict__["boolean_and"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_floor():
    assert hasattr(ocltestmodel::MyClass, "real_floor")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_floor" in klass.__dict__:
            descriptor = klass.__dict__["real_floor"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_division():
    assert hasattr(ocltestmodel::MyClass, "integer_division")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_division" in klass.__dict__:
            descriptor = klass.__dict__["integer_division"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_addition():
    assert hasattr(ocltestmodel::MyClass, "integer_addition")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_addition" in klass.__dict__:
            descriptor = klass.__dict__["integer_addition"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_toString():
    assert hasattr(ocltestmodel::MyClass, "real_toString")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_toString" in klass.__dict__:
            descriptor = klass.__dict__["real_toString"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_let3():
    assert hasattr(ocltestmodel::MyClass, "let3")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "let3" in klass.__dict__:
            descriptor = klass.__dict__["let3"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_size():
    assert hasattr(ocltestmodel::MyClass, "string_size")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_size" in klass.__dict__:
            descriptor = klass.__dict__["string_size"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_addition():
    assert hasattr(ocltestmodel::MyClass, "real_addition")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_addition" in klass.__dict__:
            descriptor = klass.__dict__["real_addition"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_greaterthan():
    assert hasattr(ocltestmodel::MyClass, "integer_greaterthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_greaterthan" in klass.__dict__:
            descriptor = klass.__dict__["integer_greaterthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_concat():
    assert hasattr(ocltestmodel::MyClass, "string_concat")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_concat" in klass.__dict__:
            descriptor = klass.__dict__["string_concat"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_equal():
    assert hasattr(ocltestmodel::MyClass, "boolean_equal")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_equal" in klass.__dict__:
            descriptor = klass.__dict__["boolean_equal"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_addition():
    assert hasattr(ocltestmodel::MyClass, "string_addition")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_addition" in klass.__dict__:
            descriptor = klass.__dict__["string_addition"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_xor():
    assert hasattr(ocltestmodel::MyClass, "boolean_xor")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_xor" in klass.__dict__:
            descriptor = klass.__dict__["boolean_xor"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_orderedset_size():
    assert hasattr(ocltestmodel::MyClass, "orderedset_size")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "orderedset_size" in klass.__dict__:
            descriptor = klass.__dict__["orderedset_size"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__BooleanLiteralExp():
    assert hasattr(ocltestmodel::MyClass, "_BooleanLiteralExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_BooleanLiteralExp" in klass.__dict__:
            descriptor = klass.__dict__["_BooleanLiteralExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_division():
    assert hasattr(ocltestmodel::MyClass, "real_division")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_division" in klass.__dict__:
            descriptor = klass.__dict__["real_division"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_lessequals():
    assert hasattr(ocltestmodel::MyClass, "integer_lessequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_lessequals" in klass.__dict__:
            descriptor = klass.__dict__["integer_lessequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__StringLiteralExp():
    assert hasattr(ocltestmodel::MyClass, "_StringLiteralExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_StringLiteralExp" in klass.__dict__:
            descriptor = klass.__dict__["_StringLiteralExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_let2():
    assert hasattr(ocltestmodel::MyClass, "let2")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "let2" in klass.__dict__:
            descriptor = klass.__dict__["let2"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_subtraction():
    assert hasattr(ocltestmodel::MyClass, "integer_subtraction")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_subtraction" in klass.__dict__:
            descriptor = klass.__dict__["integer_subtraction"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_unequal():
    assert hasattr(ocltestmodel::MyClass, "boolean_unequal")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_unequal" in klass.__dict__:
            descriptor = klass.__dict__["boolean_unequal"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_maximum():
    assert hasattr(ocltestmodel::MyClass, "integer_maximum")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_maximum" in klass.__dict__:
            descriptor = klass.__dict__["integer_maximum"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_sequence():
    assert hasattr(ocltestmodel::MyClass, "integer_sequence")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_sequence" in klass.__dict__:
            descriptor = klass.__dict__["integer_sequence"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_indexOf():
    assert hasattr(ocltestmodel::MyClass, "string_indexOf")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_indexOf" in klass.__dict__:
            descriptor = klass.__dict__["string_indexOf"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER():
    assert hasattr(ocltestmodel::MyClass, "_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER" in klass.__dict__:
            descriptor = klass.__dict__["_InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__RealLiteralExp():
    assert hasattr(ocltestmodel::MyClass, "_RealLiteralExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_RealLiteralExp" in klass.__dict__:
            descriptor = klass.__dict__["_RealLiteralExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_sequence_selectByKind():
    assert hasattr(ocltestmodel::MyClass, "sequence_selectByKind")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "sequence_selectByKind" in klass.__dict__:
            descriptor = klass.__dict__["sequence_selectByKind"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_static_sequence():
    assert hasattr(ocltestmodel::MyClass, "static_sequence")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "static_sequence" in klass.__dict__:
            descriptor = klass.__dict__["static_sequence"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_equal():
    assert hasattr(ocltestmodel::MyClass, "string_equal")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_equal" in klass.__dict__:
            descriptor = klass.__dict__["string_equal"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_equalsIgnoreCase():
    assert hasattr(ocltestmodel::MyClass, "string_equalsIgnoreCase")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_equalsIgnoreCase" in klass.__dict__:
            descriptor = klass.__dict__["string_equalsIgnoreCase"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_lessequals():
    assert hasattr(ocltestmodel::MyClass, "real_lessequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_lessequals" in klass.__dict__:
            descriptor = klass.__dict__["real_lessequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_greaterthan():
    assert hasattr(ocltestmodel::MyClass, "real_greaterthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_greaterthan" in klass.__dict__:
            descriptor = klass.__dict__["real_greaterthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_lessthan():
    assert hasattr(ocltestmodel::MyClass, "real_lessthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_lessthan" in klass.__dict__:
            descriptor = klass.__dict__["real_lessthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_boolean_toString():
    assert hasattr(ocltestmodel::MyClass, "boolean_toString")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "boolean_toString" in klass.__dict__:
            descriptor = klass.__dict__["boolean_toString"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has__NumberLiteralExp():
    assert hasattr(ocltestmodel::MyClass, "_NumberLiteralExp")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "_NumberLiteralExp" in klass.__dict__:
            descriptor = klass.__dict__["_NumberLiteralExp"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_lastIndexOf():
    assert hasattr(ocltestmodel::MyClass, "string_lastIndexOf")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_lastIndexOf" in klass.__dict__:
            descriptor = klass.__dict__["string_lastIndexOf"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_greaterequals():
    assert hasattr(ocltestmodel::MyClass, "integer_greaterequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_greaterequals" in klass.__dict__:
            descriptor = klass.__dict__["integer_greaterequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_integer_lessthan():
    assert hasattr(ocltestmodel::MyClass, "integer_lessthan")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "integer_lessthan" in klass.__dict__:
            descriptor = klass.__dict__["integer_lessthan"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_sequence_selectByType():
    assert hasattr(ocltestmodel::MyClass, "sequence_selectByType")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "sequence_selectByType" in klass.__dict__:
            descriptor = klass.__dict__["sequence_selectByType"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_collection_literals():
    assert hasattr(ocltestmodel::MyClass, "collection_literals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "collection_literals" in klass.__dict__:
            descriptor = klass.__dict__["collection_literals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_real_maximum():
    assert hasattr(ocltestmodel::MyClass, "real_maximum")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "real_maximum" in klass.__dict__:
            descriptor = klass.__dict__["real_maximum"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_string_lessequals():
    assert hasattr(ocltestmodel::MyClass, "string_lessequals")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "string_lessequals" in klass.__dict__:
            descriptor = klass.__dict__["string_lessequals"]
            break
    assert isinstance(descriptor, property)

def test_ocltestmodel::myclass_has_sequence_count():
    assert hasattr(ocltestmodel::MyClass, "sequence_count")
    descriptor = None
    for klass in ocltestmodel::MyClass.__mro__:
        if "sequence_count" in klass.__dict__:
            descriptor = klass.__dict__["sequence_count"]
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
ocltestmodel::MyClass_strategy = st.builds(
    ocltestmodel::MyClass,
    _IfExp2=
        safe_text,
    string_replaceAll=
        safe_text,
    boolean_not=
        st.booleans(),
    integer_modulo=
        st.integers(),
    _IntegerLiteralExp=
        safe_text,
    boolean_or=
        st.booleans(),
    real_absolute=
        safe_text,
    string_greaterthan=
        st.booleans(),
    boolean_implies=
        st.booleans(),
    integer_absolute=
        st.integers(),
    integer_multiplication=
        st.integers(),
    string_unequal=
        st.booleans(),
    real_minimum=
        safe_text,
    _IfExp=
        safe_text,
    tuple_literal=
        st.booleans(),
    let=
        st.booleans(),
    unEmployed=
        st.booleans(),
    string_at=
        safe_text,
    integer_minimum=
        st.integers(),
    string_greaterequals=
        st.booleans(),
    integer_toString=
        safe_text,
    real_subtraction=
        safe_text,
    real_greaterequals=
        st.booleans(),
    string_compareTo=
        safe_text,
    real_multiplication=
        safe_text,
    string_lessthan=
        st.booleans(),
    boolean_and=
        st.booleans(),
    real_floor=
        safe_text,
    integer_division=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    integer_addition=
        st.integers(),
    real_toString=
        safe_text,
    let3=
        st.integers(),
    string_size=
        safe_text,
    real_addition=
        safe_text,
    integer_greaterthan=
        st.booleans(),
    string_concat=
        safe_text,
    boolean_equal=
        st.booleans(),
    string_addition=
        safe_text,
    boolean_xor=
        st.booleans(),
    orderedset_size=
        safe_text,
    _BooleanLiteralExp=
        st.booleans(),
    real_division=
        safe_text,
    integer_lessequals=
        st.booleans(),
    _StringLiteralExp=
        safe_text,
    let2=
        st.booleans(),
    integer_subtraction=
        st.integers(),
    boolean_unequal=
        st.booleans(),
    integer_maximum=
        st.integers(),
    integer_sequence=
        st.integers(),
    string_indexOf=
        safe_text,
    _InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER=
        safe_text,
    _RealLiteralExp=
        safe_text,
    sequence_selectByKind=
        safe_text,
    static_sequence=
        safe_text,
    string_equal=
        st.booleans(),
    string_equalsIgnoreCase=
        st.booleans(),
    real_lessequals=
        st.booleans(),
    real_greaterthan=
        st.booleans(),
    real_lessthan=
        st.booleans(),
    boolean_toString=
        safe_text,
    _NumberLiteralExp=
        safe_text,
    string_lastIndexOf=
        safe_text,
    integer_greaterequals=
        st.booleans(),
    integer_lessthan=
        st.booleans(),
    sequence_selectByType=
        safe_text,
    collection_literals=
        safe_text,
    real_maximum=
        safe_text,
    string_lessequals=
        st.booleans(),
    sequence_count=
        safe_text
)

@given(instance=ocltestmodel::MyClass_strategy)
@settings(max_examples=50)
def test_ocltestmodel::myclass_instantiation(instance):
    assert isinstance(instance, ocltestmodel::MyClass)

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IfExp2_type(instance):
    assert isinstance(instance._IfExp2, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IfExp2_setter(instance):
    original = instance._IfExp2
    instance._IfExp2 = original
    assert instance._IfExp2 == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_replaceAll_type(instance):
    assert isinstance(instance.string_replaceAll, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_replaceAll_setter(instance):
    original = instance.string_replaceAll
    instance.string_replaceAll = original
    assert instance.string_replaceAll == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_not_type(instance):
    assert isinstance(instance.boolean_not, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_not_setter(instance):
    original = instance.boolean_not
    instance.boolean_not = original
    assert instance.boolean_not == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_modulo_type(instance):
    assert isinstance(instance.integer_modulo, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_modulo_setter(instance):
    original = instance.integer_modulo
    instance.integer_modulo = original
    assert instance.integer_modulo == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IntegerLiteralExp_type(instance):
    assert isinstance(instance._IntegerLiteralExp, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IntegerLiteralExp_setter(instance):
    original = instance._IntegerLiteralExp
    instance._IntegerLiteralExp = original
    assert instance._IntegerLiteralExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_or_type(instance):
    assert isinstance(instance.boolean_or, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_or_setter(instance):
    original = instance.boolean_or
    instance.boolean_or = original
    assert instance.boolean_or == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_absolute_type(instance):
    assert isinstance(instance.real_absolute, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_absolute_setter(instance):
    original = instance.real_absolute
    instance.real_absolute = original
    assert instance.real_absolute == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_greaterthan_type(instance):
    assert isinstance(instance.string_greaterthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_greaterthan_setter(instance):
    original = instance.string_greaterthan
    instance.string_greaterthan = original
    assert instance.string_greaterthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_implies_type(instance):
    assert isinstance(instance.boolean_implies, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_implies_setter(instance):
    original = instance.boolean_implies
    instance.boolean_implies = original
    assert instance.boolean_implies == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_absolute_type(instance):
    assert isinstance(instance.integer_absolute, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_absolute_setter(instance):
    original = instance.integer_absolute
    instance.integer_absolute = original
    assert instance.integer_absolute == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_multiplication_type(instance):
    assert isinstance(instance.integer_multiplication, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_multiplication_setter(instance):
    original = instance.integer_multiplication
    instance.integer_multiplication = original
    assert instance.integer_multiplication == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_unequal_type(instance):
    assert isinstance(instance.string_unequal, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_unequal_setter(instance):
    original = instance.string_unequal
    instance.string_unequal = original
    assert instance.string_unequal == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_minimum_type(instance):
    assert isinstance(instance.real_minimum, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_minimum_setter(instance):
    original = instance.real_minimum
    instance.real_minimum = original
    assert instance.real_minimum == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IfExp_type(instance):
    assert isinstance(instance._IfExp, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__IfExp_setter(instance):
    original = instance._IfExp
    instance._IfExp = original
    assert instance._IfExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_tuple_literal_type(instance):
    assert isinstance(instance.tuple_literal, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_tuple_literal_setter(instance):
    original = instance.tuple_literal
    instance.tuple_literal = original
    assert instance.tuple_literal == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let_type(instance):
    assert isinstance(instance.let, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let_setter(instance):
    original = instance.let
    instance.let = original
    assert instance.let == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_unEmployed_type(instance):
    assert isinstance(instance.unEmployed, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_unEmployed_setter(instance):
    original = instance.unEmployed
    instance.unEmployed = original
    assert instance.unEmployed == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_at_type(instance):
    assert isinstance(instance.string_at, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_at_setter(instance):
    original = instance.string_at
    instance.string_at = original
    assert instance.string_at == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_minimum_type(instance):
    assert isinstance(instance.integer_minimum, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_minimum_setter(instance):
    original = instance.integer_minimum
    instance.integer_minimum = original
    assert instance.integer_minimum == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_greaterequals_type(instance):
    assert isinstance(instance.string_greaterequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_greaterequals_setter(instance):
    original = instance.string_greaterequals
    instance.string_greaterequals = original
    assert instance.string_greaterequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_toString_type(instance):
    assert isinstance(instance.integer_toString, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_toString_setter(instance):
    original = instance.integer_toString
    instance.integer_toString = original
    assert instance.integer_toString == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_subtraction_type(instance):
    assert isinstance(instance.real_subtraction, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_subtraction_setter(instance):
    original = instance.real_subtraction
    instance.real_subtraction = original
    assert instance.real_subtraction == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_greaterequals_type(instance):
    assert isinstance(instance.real_greaterequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_greaterequals_setter(instance):
    original = instance.real_greaterequals
    instance.real_greaterequals = original
    assert instance.real_greaterequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_compareTo_type(instance):
    assert isinstance(instance.string_compareTo, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_compareTo_setter(instance):
    original = instance.string_compareTo
    instance.string_compareTo = original
    assert instance.string_compareTo == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_multiplication_type(instance):
    assert isinstance(instance.real_multiplication, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_multiplication_setter(instance):
    original = instance.real_multiplication
    instance.real_multiplication = original
    assert instance.real_multiplication == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lessthan_type(instance):
    assert isinstance(instance.string_lessthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lessthan_setter(instance):
    original = instance.string_lessthan
    instance.string_lessthan = original
    assert instance.string_lessthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_and_type(instance):
    assert isinstance(instance.boolean_and, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_and_setter(instance):
    original = instance.boolean_and
    instance.boolean_and = original
    assert instance.boolean_and == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_floor_type(instance):
    assert isinstance(instance.real_floor, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_floor_setter(instance):
    original = instance.real_floor
    instance.real_floor = original
    assert instance.real_floor == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_division_type(instance):
    assert isinstance(instance.integer_division, float)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_division_setter(instance):
    original = instance.integer_division
    instance.integer_division = original
    assert instance.integer_division == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_addition_type(instance):
    assert isinstance(instance.integer_addition, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_addition_setter(instance):
    original = instance.integer_addition
    instance.integer_addition = original
    assert instance.integer_addition == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_toString_type(instance):
    assert isinstance(instance.real_toString, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_toString_setter(instance):
    original = instance.real_toString
    instance.real_toString = original
    assert instance.real_toString == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let3_type(instance):
    assert isinstance(instance.let3, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let3_setter(instance):
    original = instance.let3
    instance.let3 = original
    assert instance.let3 == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_size_type(instance):
    assert isinstance(instance.string_size, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_size_setter(instance):
    original = instance.string_size
    instance.string_size = original
    assert instance.string_size == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_addition_type(instance):
    assert isinstance(instance.real_addition, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_addition_setter(instance):
    original = instance.real_addition
    instance.real_addition = original
    assert instance.real_addition == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_greaterthan_type(instance):
    assert isinstance(instance.integer_greaterthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_greaterthan_setter(instance):
    original = instance.integer_greaterthan
    instance.integer_greaterthan = original
    assert instance.integer_greaterthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_concat_type(instance):
    assert isinstance(instance.string_concat, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_concat_setter(instance):
    original = instance.string_concat
    instance.string_concat = original
    assert instance.string_concat == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_equal_type(instance):
    assert isinstance(instance.boolean_equal, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_equal_setter(instance):
    original = instance.boolean_equal
    instance.boolean_equal = original
    assert instance.boolean_equal == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_addition_type(instance):
    assert isinstance(instance.string_addition, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_addition_setter(instance):
    original = instance.string_addition
    instance.string_addition = original
    assert instance.string_addition == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_xor_type(instance):
    assert isinstance(instance.boolean_xor, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_xor_setter(instance):
    original = instance.boolean_xor
    instance.boolean_xor = original
    assert instance.boolean_xor == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_orderedset_size_type(instance):
    assert isinstance(instance.orderedset_size, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_orderedset_size_setter(instance):
    original = instance.orderedset_size
    instance.orderedset_size = original
    assert instance.orderedset_size == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__BooleanLiteralExp_type(instance):
    assert isinstance(instance._BooleanLiteralExp, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__BooleanLiteralExp_setter(instance):
    original = instance._BooleanLiteralExp
    instance._BooleanLiteralExp = original
    assert instance._BooleanLiteralExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_division_type(instance):
    assert isinstance(instance.real_division, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_division_setter(instance):
    original = instance.real_division
    instance.real_division = original
    assert instance.real_division == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_lessequals_type(instance):
    assert isinstance(instance.integer_lessequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_lessequals_setter(instance):
    original = instance.integer_lessequals
    instance.integer_lessequals = original
    assert instance.integer_lessequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__StringLiteralExp_type(instance):
    assert isinstance(instance._StringLiteralExp, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__StringLiteralExp_setter(instance):
    original = instance._StringLiteralExp
    instance._StringLiteralExp = original
    assert instance._StringLiteralExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let2_type(instance):
    assert isinstance(instance.let2, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_let2_setter(instance):
    original = instance.let2
    instance.let2 = original
    assert instance.let2 == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_subtraction_type(instance):
    assert isinstance(instance.integer_subtraction, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_subtraction_setter(instance):
    original = instance.integer_subtraction
    instance.integer_subtraction = original
    assert instance.integer_subtraction == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_unequal_type(instance):
    assert isinstance(instance.boolean_unequal, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_unequal_setter(instance):
    original = instance.boolean_unequal
    instance.boolean_unequal = original
    assert instance.boolean_unequal == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_maximum_type(instance):
    assert isinstance(instance.integer_maximum, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_maximum_setter(instance):
    original = instance.integer_maximum
    instance.integer_maximum = original
    assert instance.integer_maximum == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_sequence_type(instance):
    assert isinstance(instance.integer_sequence, int)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_sequence_setter(instance):
    original = instance.integer_sequence
    instance.integer_sequence = original
    assert instance.integer_sequence == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_indexOf_type(instance):
    assert isinstance(instance.string_indexOf, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_indexOf_setter(instance):
    original = instance.string_indexOf
    instance.string_indexOf = original
    assert instance.string_indexOf == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER_type(instance):
    assert isinstance(instance._InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER_setter(instance):
    original = instance._InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER
    instance._InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER = original
    assert instance._InfixExp_NOT_PASSING_DUE_TO_BUG_IN_OCLHELPER == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__RealLiteralExp_type(instance):
    assert isinstance(instance._RealLiteralExp, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__RealLiteralExp_setter(instance):
    original = instance._RealLiteralExp
    instance._RealLiteralExp = original
    assert instance._RealLiteralExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_selectByKind_type(instance):
    assert isinstance(instance.sequence_selectByKind, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_selectByKind_setter(instance):
    original = instance.sequence_selectByKind
    instance.sequence_selectByKind = original
    assert instance.sequence_selectByKind == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_static_sequence_type(instance):
    assert isinstance(instance.static_sequence, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_static_sequence_setter(instance):
    original = instance.static_sequence
    instance.static_sequence = original
    assert instance.static_sequence == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_equal_type(instance):
    assert isinstance(instance.string_equal, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_equal_setter(instance):
    original = instance.string_equal
    instance.string_equal = original
    assert instance.string_equal == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_equalsIgnoreCase_type(instance):
    assert isinstance(instance.string_equalsIgnoreCase, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_equalsIgnoreCase_setter(instance):
    original = instance.string_equalsIgnoreCase
    instance.string_equalsIgnoreCase = original
    assert instance.string_equalsIgnoreCase == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_lessequals_type(instance):
    assert isinstance(instance.real_lessequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_lessequals_setter(instance):
    original = instance.real_lessequals
    instance.real_lessequals = original
    assert instance.real_lessequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_greaterthan_type(instance):
    assert isinstance(instance.real_greaterthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_greaterthan_setter(instance):
    original = instance.real_greaterthan
    instance.real_greaterthan = original
    assert instance.real_greaterthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_lessthan_type(instance):
    assert isinstance(instance.real_lessthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_lessthan_setter(instance):
    original = instance.real_lessthan
    instance.real_lessthan = original
    assert instance.real_lessthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_toString_type(instance):
    assert isinstance(instance.boolean_toString, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_boolean_toString_setter(instance):
    original = instance.boolean_toString
    instance.boolean_toString = original
    assert instance.boolean_toString == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__NumberLiteralExp_type(instance):
    assert isinstance(instance._NumberLiteralExp, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass__NumberLiteralExp_setter(instance):
    original = instance._NumberLiteralExp
    instance._NumberLiteralExp = original
    assert instance._NumberLiteralExp == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lastIndexOf_type(instance):
    assert isinstance(instance.string_lastIndexOf, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lastIndexOf_setter(instance):
    original = instance.string_lastIndexOf
    instance.string_lastIndexOf = original
    assert instance.string_lastIndexOf == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_greaterequals_type(instance):
    assert isinstance(instance.integer_greaterequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_greaterequals_setter(instance):
    original = instance.integer_greaterequals
    instance.integer_greaterequals = original
    assert instance.integer_greaterequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_lessthan_type(instance):
    assert isinstance(instance.integer_lessthan, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_integer_lessthan_setter(instance):
    original = instance.integer_lessthan
    instance.integer_lessthan = original
    assert instance.integer_lessthan == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_selectByType_type(instance):
    assert isinstance(instance.sequence_selectByType, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_selectByType_setter(instance):
    original = instance.sequence_selectByType
    instance.sequence_selectByType = original
    assert instance.sequence_selectByType == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_collection_literals_type(instance):
    assert isinstance(instance.collection_literals, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_collection_literals_setter(instance):
    original = instance.collection_literals
    instance.collection_literals = original
    assert instance.collection_literals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_maximum_type(instance):
    assert isinstance(instance.real_maximum, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_real_maximum_setter(instance):
    original = instance.real_maximum
    instance.real_maximum = original
    assert instance.real_maximum == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lessequals_type(instance):
    assert isinstance(instance.string_lessequals, bool)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_string_lessequals_setter(instance):
    original = instance.string_lessequals
    instance.string_lessequals = original
    assert instance.string_lessequals == original

@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_count_type(instance):
    assert isinstance(instance.sequence_count, str)


@given(instance=ocltestmodel::MyClass_strategy)
def test_ocltestmodel::myclass_sequence_count_setter(instance):
    original = instance.sequence_count
    instance.sequence_count = original
    assert instance.sequence_count == original
