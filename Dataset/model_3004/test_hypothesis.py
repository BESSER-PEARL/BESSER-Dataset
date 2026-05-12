import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BSExpression,
    blorqueScript_BSPostfixArithmeticExpression,
    blorqueScript_BSCastExpression,
    blorqueScript_BSMemberSelectionExpression,
    blorqueScript_BSPlusMinusOrStringConcatExpression,
    blorqueScript_BSBooleanAndExpression,
    blorqueScript_BSClientLiteral,
    blorqueScript_BSBooleanConstant,
    blorqueScript_BSEqualityExpression,
    blorqueScript_BSNullLiteral,
    blorqueScript_BSBitwiseXorExpression,
    blorqueScript_BSParentLiteral,
    blorqueScript_BSBitwiseShiftExpression,
    blorqueScript_BSRealConstant,
    blorqueScript_BSOrderedRelationExpression,
    blorqueScript_BSMulDivOrModExpression,
    blorqueScript_BSParentheticalExpression,
    blorqueScript_BSSymbolRef,
    blorqueScript_BSNumberConstant,
    blorqueScript_BSUnaryModifierExpression,
    blorqueScript_BSBitwiseAndExpression,
    blorqueScript_BSHexadecimalConstant,
    blorqueScript_BSBitwiseOrExpression,
    blorqueScript_BSStringConstant,
    blorqueScript_BSMethodInvokationExpression,
    blorqueScript_BSTernaryExpression,
    blorqueScript_BSNewExpression,
    blorqueScript_BSArrayAccessExpression,
    blorqueScript_BSThisLiteral,
    blorqueScript_BSBooleanOrExpression,
    blorqueScript_BSAssignmentExpression,
    blorqueScript_BSSymbol,
    blorqueScript_BSBlock,
    blorqueScript_BSCase,
    BSMember,
    blorqueScript_BSMethod,
    blorqueScript_BSField,
    BSStatement,
    blorqueScript_BSIfStatement,
    blorqueScript_BSBreak,
    blorqueScript_BSContinue,
    blorqueScript_BSWhileLoop,
    blorqueScript_BSForLoop,
    blorqueScript_BSExpression,
    blorqueScript_BSSwitchStatement,
    blorqueScript_BSReturn,
    blorqueScript_BSStatement,
    BSBlock,
    blorqueScript_BSIfBlock,
    blorqueScript_BSCaseBlock,
    blorqueScript_BSLoopBlock,
    blorqueScript_BSSwitchBlock,
    blorqueScript_BSMethodBody,
    BSSymbol,
    blorqueScript_BSParameter,
    blorqueScript_BSVariableDeclaration,
    blorqueScript_BSMember,
    blorqueScript_BSClass,
    blorqueScript_BSImport,
    blorqueScript_BSFile,
    BSPrimitiveType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bsexpression_is_not_abstract():
    assert not inspect.isabstract(BSExpression)


def test_bsexpression_constructor_exists():
    assert callable(BSExpression.__init__)


def test_bsexpression_constructor_args():
    sig = inspect.signature(BSExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bspostfixarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSPostfixArithmeticExpression)


def test_blorquescript_bspostfixarithmeticexpression_constructor_exists():
    assert callable(blorqueScript_BSPostfixArithmeticExpression.__init__)


def test_blorquescript_bspostfixarithmeticexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSPostfixArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bspostfixarithmeticexpression_has_operator():
    assert hasattr(blorqueScript_BSPostfixArithmeticExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSPostfixArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bscastexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSCastExpression)


def test_blorquescript_bscastexpression_constructor_exists():
    assert callable(blorqueScript_BSCastExpression.__init__)


def test_blorquescript_bscastexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSCastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "pType" in params, "Missing parameter 'pType'"

def test_blorquescript_bscastexpression_has_isArray():
    assert hasattr(blorqueScript_BSCastExpression, "isArray")
    descriptor = None
    for klass in blorqueScript_BSCastExpression.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_blorquescript_bscastexpression_has_pType():
    assert hasattr(blorqueScript_BSCastExpression, "pType")
    descriptor = None
    for klass in blorqueScript_BSCastExpression.__mro__:
        if "pType" in klass.__dict__:
            descriptor = klass.__dict__["pType"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsmemberselectionexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMemberSelectionExpression)


def test_blorquescript_bsmemberselectionexpression_constructor_exists():
    assert callable(blorqueScript_BSMemberSelectionExpression.__init__)


def test_blorquescript_bsmemberselectionexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSMemberSelectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsplusminusorstringconcatexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSPlusMinusOrStringConcatExpression)


def test_blorquescript_bsplusminusorstringconcatexpression_constructor_exists():
    assert callable(blorqueScript_BSPlusMinusOrStringConcatExpression.__init__)


def test_blorquescript_bsplusminusorstringconcatexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSPlusMinusOrStringConcatExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsplusminusorstringconcatexpression_has_operator():
    assert hasattr(blorqueScript_BSPlusMinusOrStringConcatExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSPlusMinusOrStringConcatExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsbooleanandexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBooleanAndExpression)


def test_blorquescript_bsbooleanandexpression_constructor_exists():
    assert callable(blorqueScript_BSBooleanAndExpression.__init__)


def test_blorquescript_bsbooleanandexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBooleanAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsclientliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSClientLiteral)


def test_blorquescript_bsclientliteral_constructor_exists():
    assert callable(blorqueScript_BSClientLiteral.__init__)


def test_blorquescript_bsclientliteral_constructor_args():
    sig = inspect.signature(blorqueScript_BSClientLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsbooleanconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBooleanConstant)


def test_blorquescript_bsbooleanconstant_constructor_exists():
    assert callable(blorqueScript_BSBooleanConstant.__init__)


def test_blorquescript_bsbooleanconstant_constructor_args():
    sig = inspect.signature(blorqueScript_BSBooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript_bsbooleanconstant_has_value():
    assert hasattr(blorqueScript_BSBooleanConstant, "value")
    descriptor = None
    for klass in blorqueScript_BSBooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsequalityexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSEqualityExpression)


def test_blorquescript_bsequalityexpression_constructor_exists():
    assert callable(blorqueScript_BSEqualityExpression.__init__)


def test_blorquescript_bsequalityexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSEqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsequalityexpression_has_operator():
    assert hasattr(blorqueScript_BSEqualityExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSEqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsnullliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSNullLiteral)


def test_blorquescript_bsnullliteral_constructor_exists():
    assert callable(blorqueScript_BSNullLiteral.__init__)


def test_blorquescript_bsnullliteral_constructor_args():
    sig = inspect.signature(blorqueScript_BSNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsbitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBitwiseXorExpression)


def test_blorquescript_bsbitwisexorexpression_constructor_exists():
    assert callable(blorqueScript_BSBitwiseXorExpression.__init__)


def test_blorquescript_bsbitwisexorexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsparentliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSParentLiteral)


def test_blorquescript_bsparentliteral_constructor_exists():
    assert callable(blorqueScript_BSParentLiteral.__init__)


def test_blorquescript_bsparentliteral_constructor_args():
    sig = inspect.signature(blorqueScript_BSParentLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsbitwiseshiftexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBitwiseShiftExpression)


def test_blorquescript_bsbitwiseshiftexpression_constructor_exists():
    assert callable(blorqueScript_BSBitwiseShiftExpression.__init__)


def test_blorquescript_bsbitwiseshiftexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBitwiseShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsbitwiseshiftexpression_has_operator():
    assert hasattr(blorqueScript_BSBitwiseShiftExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSBitwiseShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsrealconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSRealConstant)


def test_blorquescript_bsrealconstant_constructor_exists():
    assert callable(blorqueScript_BSRealConstant.__init__)


def test_blorquescript_bsrealconstant_constructor_args():
    sig = inspect.signature(blorqueScript_BSRealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_blorquescript_bsrealconstant_has_right():
    assert hasattr(blorqueScript_BSRealConstant, "right")
    descriptor = None
    for klass in blorqueScript_BSRealConstant.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsorderedrelationexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSOrderedRelationExpression)


def test_blorquescript_bsorderedrelationexpression_constructor_exists():
    assert callable(blorqueScript_BSOrderedRelationExpression.__init__)


def test_blorquescript_bsorderedrelationexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSOrderedRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsorderedrelationexpression_has_operator():
    assert hasattr(blorqueScript_BSOrderedRelationExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSOrderedRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsmuldivormodexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMulDivOrModExpression)


def test_blorquescript_bsmuldivormodexpression_constructor_exists():
    assert callable(blorqueScript_BSMulDivOrModExpression.__init__)


def test_blorquescript_bsmuldivormodexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSMulDivOrModExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsmuldivormodexpression_has_operator():
    assert hasattr(blorqueScript_BSMulDivOrModExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSMulDivOrModExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsparentheticalexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSParentheticalExpression)


def test_blorquescript_bsparentheticalexpression_constructor_exists():
    assert callable(blorqueScript_BSParentheticalExpression.__init__)


def test_blorquescript_bsparentheticalexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSParentheticalExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bssymbolref_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSSymbolRef)


def test_blorquescript_bssymbolref_constructor_exists():
    assert callable(blorqueScript_BSSymbolRef.__init__)


def test_blorquescript_bssymbolref_constructor_args():
    sig = inspect.signature(blorqueScript_BSSymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsnumberconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSNumberConstant)


def test_blorquescript_bsnumberconstant_constructor_exists():
    assert callable(blorqueScript_BSNumberConstant.__init__)


def test_blorquescript_bsnumberconstant_constructor_args():
    sig = inspect.signature(blorqueScript_BSNumberConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript_bsnumberconstant_has_value():
    assert hasattr(blorqueScript_BSNumberConstant, "value")
    descriptor = None
    for klass in blorqueScript_BSNumberConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsunarymodifierexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSUnaryModifierExpression)


def test_blorquescript_bsunarymodifierexpression_constructor_exists():
    assert callable(blorqueScript_BSUnaryModifierExpression.__init__)


def test_blorquescript_bsunarymodifierexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSUnaryModifierExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript_bsunarymodifierexpression_has_operator():
    assert hasattr(blorqueScript_BSUnaryModifierExpression, "operator")
    descriptor = None
    for klass in blorqueScript_BSUnaryModifierExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsbitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBitwiseAndExpression)


def test_blorquescript_bsbitwiseandexpression_constructor_exists():
    assert callable(blorqueScript_BSBitwiseAndExpression.__init__)


def test_blorquescript_bsbitwiseandexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bshexadecimalconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSHexadecimalConstant)


def test_blorquescript_bshexadecimalconstant_constructor_exists():
    assert callable(blorqueScript_BSHexadecimalConstant.__init__)


def test_blorquescript_bshexadecimalconstant_constructor_args():
    sig = inspect.signature(blorqueScript_BSHexadecimalConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript_bshexadecimalconstant_has_value():
    assert hasattr(blorqueScript_BSHexadecimalConstant, "value")
    descriptor = None
    for klass in blorqueScript_BSHexadecimalConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsbitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBitwiseOrExpression)


def test_blorquescript_bsbitwiseorexpression_constructor_exists():
    assert callable(blorqueScript_BSBitwiseOrExpression.__init__)


def test_blorquescript_bsbitwiseorexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsstringconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSStringConstant)


def test_blorquescript_bsstringconstant_constructor_exists():
    assert callable(blorqueScript_BSStringConstant.__init__)


def test_blorquescript_bsstringconstant_constructor_args():
    sig = inspect.signature(blorqueScript_BSStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript_bsstringconstant_has_value():
    assert hasattr(blorqueScript_BSStringConstant, "value")
    descriptor = None
    for klass in blorqueScript_BSStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsmethodinvokationexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMethodInvokationExpression)


def test_blorquescript_bsmethodinvokationexpression_constructor_exists():
    assert callable(blorqueScript_BSMethodInvokationExpression.__init__)


def test_blorquescript_bsmethodinvokationexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSMethodInvokationExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsternaryexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSTernaryExpression)


def test_blorquescript_bsternaryexpression_constructor_exists():
    assert callable(blorqueScript_BSTernaryExpression.__init__)


def test_blorquescript_bsternaryexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSTernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsnewexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSNewExpression)


def test_blorquescript_bsnewexpression_constructor_exists():
    assert callable(blorqueScript_BSNewExpression.__init__)


def test_blorquescript_bsnewexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSNewExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript_bsnewexpression_has_isArray():
    assert hasattr(blorqueScript_BSNewExpression, "isArray")
    descriptor = None
    for klass in blorqueScript_BSNewExpression.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsarrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSArrayAccessExpression)


def test_blorquescript_bsarrayaccessexpression_constructor_exists():
    assert callable(blorqueScript_BSArrayAccessExpression.__init__)


def test_blorquescript_bsarrayaccessexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsthisliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSThisLiteral)


def test_blorquescript_bsthisliteral_constructor_exists():
    assert callable(blorqueScript_BSThisLiteral.__init__)


def test_blorquescript_bsthisliteral_constructor_args():
    sig = inspect.signature(blorqueScript_BSThisLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsbooleanorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBooleanOrExpression)


def test_blorquescript_bsbooleanorexpression_constructor_exists():
    assert callable(blorqueScript_BSBooleanOrExpression.__init__)


def test_blorquescript_bsbooleanorexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSBooleanOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSAssignmentExpression)


def test_blorquescript_bsassignmentexpression_constructor_exists():
    assert callable(blorqueScript_BSAssignmentExpression.__init__)


def test_blorquescript_bsassignmentexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSAssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assignmentOperator" in params, "Missing parameter 'assignmentOperator'"

def test_blorquescript_bsassignmentexpression_has_assignmentOperator():
    assert hasattr(blorqueScript_BSAssignmentExpression, "assignmentOperator")
    descriptor = None
    for klass in blorqueScript_BSAssignmentExpression.__mro__:
        if "assignmentOperator" in klass.__dict__:
            descriptor = klass.__dict__["assignmentOperator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bssymbol_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSSymbol)


def test_blorquescript_bssymbol_constructor_exists():
    assert callable(blorqueScript_BSSymbol.__init__)


def test_blorquescript_bssymbol_constructor_args():
    sig = inspect.signature(blorqueScript_BSSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "pType" in params, "Missing parameter 'pType'"
    assert "name" in params, "Missing parameter 'name'"

def test_blorquescript_bssymbol_has_pType():
    assert hasattr(blorqueScript_BSSymbol, "pType")
    descriptor = None
    for klass in blorqueScript_BSSymbol.__mro__:
        if "pType" in klass.__dict__:
            descriptor = klass.__dict__["pType"]
            break
    assert isinstance(descriptor, property)

def test_blorquescript_bssymbol_has_name():
    assert hasattr(blorqueScript_BSSymbol, "name")
    descriptor = None
    for klass in blorqueScript_BSSymbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBlock)


def test_blorquescript_bsblock_constructor_exists():
    assert callable(blorqueScript_BSBlock.__init__)


def test_blorquescript_bsblock_constructor_args():
    sig = inspect.signature(blorqueScript_BSBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bscase_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSCase)


def test_blorquescript_bscase_constructor_exists():
    assert callable(blorqueScript_BSCase.__init__)


def test_blorquescript_bscase_constructor_args():
    sig = inspect.signature(blorqueScript_BSCase.__init__)
    params = list(sig.parameters.keys())



def test_bsmember_is_not_abstract():
    assert not inspect.isabstract(BSMember)


def test_bsmember_constructor_exists():
    assert callable(BSMember.__init__)


def test_bsmember_constructor_args():
    sig = inspect.signature(BSMember.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsmethod_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMethod)


def test_blorquescript_bsmethod_constructor_exists():
    assert callable(blorqueScript_BSMethod.__init__)


def test_blorquescript_bsmethod_constructor_args():
    sig = inspect.signature(blorqueScript_BSMethod.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsfield_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSField)


def test_blorquescript_bsfield_constructor_exists():
    assert callable(blorqueScript_BSField.__init__)


def test_blorquescript_bsfield_constructor_args():
    sig = inspect.signature(blorqueScript_BSField.__init__)
    params = list(sig.parameters.keys())



def test_bsstatement_is_not_abstract():
    assert not inspect.isabstract(BSStatement)


def test_bsstatement_constructor_exists():
    assert callable(BSStatement.__init__)


def test_bsstatement_constructor_args():
    sig = inspect.signature(BSStatement.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsifstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSIfStatement)


def test_blorquescript_bsifstatement_constructor_exists():
    assert callable(blorqueScript_BSIfStatement.__init__)


def test_blorquescript_bsifstatement_constructor_args():
    sig = inspect.signature(blorqueScript_BSIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsbreak_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSBreak)


def test_blorquescript_bsbreak_constructor_exists():
    assert callable(blorqueScript_BSBreak.__init__)


def test_blorquescript_bsbreak_constructor_args():
    sig = inspect.signature(blorqueScript_BSBreak.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bscontinue_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSContinue)


def test_blorquescript_bscontinue_constructor_exists():
    assert callable(blorqueScript_BSContinue.__init__)


def test_blorquescript_bscontinue_constructor_args():
    sig = inspect.signature(blorqueScript_BSContinue.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bswhileloop_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSWhileLoop)


def test_blorquescript_bswhileloop_constructor_exists():
    assert callable(blorqueScript_BSWhileLoop.__init__)


def test_blorquescript_bswhileloop_constructor_args():
    sig = inspect.signature(blorqueScript_BSWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsforloop_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSForLoop)


def test_blorquescript_bsforloop_constructor_exists():
    assert callable(blorqueScript_BSForLoop.__init__)


def test_blorquescript_bsforloop_constructor_args():
    sig = inspect.signature(blorqueScript_BSForLoop.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSExpression)


def test_blorquescript_bsexpression_constructor_exists():
    assert callable(blorqueScript_BSExpression.__init__)


def test_blorquescript_bsexpression_constructor_args():
    sig = inspect.signature(blorqueScript_BSExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsswitchstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSSwitchStatement)


def test_blorquescript_bsswitchstatement_constructor_exists():
    assert callable(blorqueScript_BSSwitchStatement.__init__)


def test_blorquescript_bsswitchstatement_constructor_args():
    sig = inspect.signature(blorqueScript_BSSwitchStatement.__init__)
    params = list(sig.parameters.keys())
    assert "stringSwitch" in params, "Missing parameter 'stringSwitch'"

def test_blorquescript_bsswitchstatement_has_stringSwitch():
    assert hasattr(blorqueScript_BSSwitchStatement, "stringSwitch")
    descriptor = None
    for klass in blorqueScript_BSSwitchStatement.__mro__:
        if "stringSwitch" in klass.__dict__:
            descriptor = klass.__dict__["stringSwitch"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsreturn_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSReturn)


def test_blorquescript_bsreturn_constructor_exists():
    assert callable(blorqueScript_BSReturn.__init__)


def test_blorquescript_bsreturn_constructor_args():
    sig = inspect.signature(blorqueScript_BSReturn.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSStatement)


def test_blorquescript_bsstatement_constructor_exists():
    assert callable(blorqueScript_BSStatement.__init__)


def test_blorquescript_bsstatement_constructor_args():
    sig = inspect.signature(blorqueScript_BSStatement.__init__)
    params = list(sig.parameters.keys())



def test_bsblock_is_not_abstract():
    assert not inspect.isabstract(BSBlock)


def test_bsblock_constructor_exists():
    assert callable(BSBlock.__init__)


def test_bsblock_constructor_args():
    sig = inspect.signature(BSBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsifblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSIfBlock)


def test_blorquescript_bsifblock_constructor_exists():
    assert callable(blorqueScript_BSIfBlock.__init__)


def test_blorquescript_bsifblock_constructor_args():
    sig = inspect.signature(blorqueScript_BSIfBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bscaseblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSCaseBlock)


def test_blorquescript_bscaseblock_constructor_exists():
    assert callable(blorqueScript_BSCaseBlock.__init__)


def test_blorquescript_bscaseblock_constructor_args():
    sig = inspect.signature(blorqueScript_BSCaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsloopblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSLoopBlock)


def test_blorquescript_bsloopblock_constructor_exists():
    assert callable(blorqueScript_BSLoopBlock.__init__)


def test_blorquescript_bsloopblock_constructor_args():
    sig = inspect.signature(blorqueScript_BSLoopBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsswitchblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSSwitchBlock)


def test_blorquescript_bsswitchblock_constructor_exists():
    assert callable(blorqueScript_BSSwitchBlock.__init__)


def test_blorquescript_bsswitchblock_constructor_args():
    sig = inspect.signature(blorqueScript_BSSwitchBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsmethodbody_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMethodBody)


def test_blorquescript_bsmethodbody_constructor_exists():
    assert callable(blorqueScript_BSMethodBody.__init__)


def test_blorquescript_bsmethodbody_constructor_args():
    sig = inspect.signature(blorqueScript_BSMethodBody.__init__)
    params = list(sig.parameters.keys())



def test_bssymbol_is_not_abstract():
    assert not inspect.isabstract(BSSymbol)


def test_bssymbol_constructor_exists():
    assert callable(BSSymbol.__init__)


def test_bssymbol_constructor_args():
    sig = inspect.signature(BSSymbol.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsparameter_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSParameter)


def test_blorquescript_bsparameter_constructor_exists():
    assert callable(blorqueScript_BSParameter.__init__)


def test_blorquescript_bsparameter_constructor_args():
    sig = inspect.signature(blorqueScript_BSParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript_bsparameter_has_isArray():
    assert hasattr(blorqueScript_BSParameter, "isArray")
    descriptor = None
    for klass in blorqueScript_BSParameter.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSVariableDeclaration)


def test_blorquescript_bsvariabledeclaration_constructor_exists():
    assert callable(blorqueScript_BSVariableDeclaration.__init__)


def test_blorquescript_bsvariabledeclaration_constructor_args():
    sig = inspect.signature(blorqueScript_BSVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript_bsmember_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSMember)


def test_blorquescript_bsmember_constructor_exists():
    assert callable(blorqueScript_BSMember.__init__)


def test_blorquescript_bsmember_constructor_args():
    sig = inspect.signature(blorqueScript_BSMember.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript_bsmember_has_isArray():
    assert hasattr(blorqueScript_BSMember, "isArray")
    descriptor = None
    for klass in blorqueScript_BSMember.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsclass_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSClass)


def test_blorquescript_bsclass_constructor_exists():
    assert callable(blorqueScript_BSClass.__init__)


def test_blorquescript_bsclass_constructor_args():
    sig = inspect.signature(blorqueScript_BSClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_blorquescript_bsclass_has_name():
    assert hasattr(blorqueScript_BSClass, "name")
    descriptor = None
    for klass in blorqueScript_BSClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsimport_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSImport)


def test_blorquescript_bsimport_constructor_exists():
    assert callable(blorqueScript_BSImport.__init__)


def test_blorquescript_bsimport_constructor_args():
    sig = inspect.signature(blorqueScript_BSImport.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_blorquescript_bsimport_has_importedNamespace():
    assert hasattr(blorqueScript_BSImport, "importedNamespace")
    descriptor = None
    for klass in blorqueScript_BSImport.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript_bsfile_is_not_abstract():
    assert not inspect.isabstract(blorqueScript_BSFile)


def test_blorquescript_bsfile_constructor_exists():
    assert callable(blorqueScript_BSFile.__init__)


def test_blorquescript_bsfile_constructor_args():
    sig = inspect.signature(blorqueScript_BSFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_blorquescript_bsfile_has_name():
    assert hasattr(blorqueScript_BSFile, "name")
    descriptor = None
    for klass in blorqueScript_BSFile.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bsprimitivetype_exists():
    # Check that the Enumeration exists
    assert BSPrimitiveType is not None

def test_bsprimitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BSPrimitiveType]
    expected_literals = [
        "TAGGED_STRING",
        "VOID",
        "STRING",
        "NONE",
        "NUMBER",
        "OBJECT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BSPrimitiveType"


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
BSExpression_strategy = st.builds(
    BSExpression,
)
blorqueScript_BSPostfixArithmeticExpression_strategy = st.builds(
    blorqueScript_BSPostfixArithmeticExpression,
    operator=
        safe_text
)
blorqueScript_BSCastExpression_strategy = st.builds(
    blorqueScript_BSCastExpression,
    isArray=
        st.booleans(),
    pType=
        safe_text
)
blorqueScript_BSMemberSelectionExpression_strategy = st.builds(
    blorqueScript_BSMemberSelectionExpression,
)
blorqueScript_BSPlusMinusOrStringConcatExpression_strategy = st.builds(
    blorqueScript_BSPlusMinusOrStringConcatExpression,
    operator=
        safe_text
)
blorqueScript_BSBooleanAndExpression_strategy = st.builds(
    blorqueScript_BSBooleanAndExpression,
)
blorqueScript_BSClientLiteral_strategy = st.builds(
    blorqueScript_BSClientLiteral,
)
blorqueScript_BSBooleanConstant_strategy = st.builds(
    blorqueScript_BSBooleanConstant,
    value=
        safe_text
)
blorqueScript_BSEqualityExpression_strategy = st.builds(
    blorqueScript_BSEqualityExpression,
    operator=
        safe_text
)
blorqueScript_BSNullLiteral_strategy = st.builds(
    blorqueScript_BSNullLiteral,
)
blorqueScript_BSBitwiseXorExpression_strategy = st.builds(
    blorqueScript_BSBitwiseXorExpression,
)
blorqueScript_BSParentLiteral_strategy = st.builds(
    blorqueScript_BSParentLiteral,
)
blorqueScript_BSBitwiseShiftExpression_strategy = st.builds(
    blorqueScript_BSBitwiseShiftExpression,
    operator=
        safe_text
)
blorqueScript_BSRealConstant_strategy = st.builds(
    blorqueScript_BSRealConstant,
    right=
        st.integers()
)
blorqueScript_BSOrderedRelationExpression_strategy = st.builds(
    blorqueScript_BSOrderedRelationExpression,
    operator=
        safe_text
)
blorqueScript_BSMulDivOrModExpression_strategy = st.builds(
    blorqueScript_BSMulDivOrModExpression,
    operator=
        safe_text
)
blorqueScript_BSParentheticalExpression_strategy = st.builds(
    blorqueScript_BSParentheticalExpression,
)
blorqueScript_BSSymbolRef_strategy = st.builds(
    blorqueScript_BSSymbolRef,
)
blorqueScript_BSNumberConstant_strategy = st.builds(
    blorqueScript_BSNumberConstant,
    value=
        st.integers()
)
blorqueScript_BSUnaryModifierExpression_strategy = st.builds(
    blorqueScript_BSUnaryModifierExpression,
    operator=
        safe_text
)
blorqueScript_BSBitwiseAndExpression_strategy = st.builds(
    blorqueScript_BSBitwiseAndExpression,
)
blorqueScript_BSHexadecimalConstant_strategy = st.builds(
    blorqueScript_BSHexadecimalConstant,
    value=
        safe_text
)
blorqueScript_BSBitwiseOrExpression_strategy = st.builds(
    blorqueScript_BSBitwiseOrExpression,
)
blorqueScript_BSStringConstant_strategy = st.builds(
    blorqueScript_BSStringConstant,
    value=
        safe_text
)
blorqueScript_BSMethodInvokationExpression_strategy = st.builds(
    blorqueScript_BSMethodInvokationExpression,
)
blorqueScript_BSTernaryExpression_strategy = st.builds(
    blorqueScript_BSTernaryExpression,
)
blorqueScript_BSNewExpression_strategy = st.builds(
    blorqueScript_BSNewExpression,
    isArray=
        st.booleans()
)
blorqueScript_BSArrayAccessExpression_strategy = st.builds(
    blorqueScript_BSArrayAccessExpression,
)
blorqueScript_BSThisLiteral_strategy = st.builds(
    blorqueScript_BSThisLiteral,
)
blorqueScript_BSBooleanOrExpression_strategy = st.builds(
    blorqueScript_BSBooleanOrExpression,
)
blorqueScript_BSAssignmentExpression_strategy = st.builds(
    blorqueScript_BSAssignmentExpression,
    assignmentOperator=
        safe_text
)
blorqueScript_BSSymbol_strategy = st.builds(
    blorqueScript_BSSymbol,
    pType=
        safe_text,
    name=
        safe_text
)
blorqueScript_BSBlock_strategy = st.builds(
    blorqueScript_BSBlock,
)
blorqueScript_BSCase_strategy = st.builds(
    blorqueScript_BSCase,
)
BSMember_strategy = st.builds(
    BSMember,
)
blorqueScript_BSMethod_strategy = st.builds(
    blorqueScript_BSMethod,
)
blorqueScript_BSField_strategy = st.builds(
    blorqueScript_BSField,
)
BSStatement_strategy = st.builds(
    BSStatement,
)
blorqueScript_BSIfStatement_strategy = st.builds(
    blorqueScript_BSIfStatement,
)
blorqueScript_BSBreak_strategy = st.builds(
    blorqueScript_BSBreak,
)
blorqueScript_BSContinue_strategy = st.builds(
    blorqueScript_BSContinue,
)
blorqueScript_BSWhileLoop_strategy = st.builds(
    blorqueScript_BSWhileLoop,
)
blorqueScript_BSForLoop_strategy = st.builds(
    blorqueScript_BSForLoop,
)
blorqueScript_BSExpression_strategy = st.builds(
    blorqueScript_BSExpression,
)
blorqueScript_BSSwitchStatement_strategy = st.builds(
    blorqueScript_BSSwitchStatement,
    stringSwitch=
        st.booleans()
)
blorqueScript_BSReturn_strategy = st.builds(
    blorqueScript_BSReturn,
)
blorqueScript_BSStatement_strategy = st.builds(
    blorqueScript_BSStatement,
)
BSBlock_strategy = st.builds(
    BSBlock,
)
blorqueScript_BSIfBlock_strategy = st.builds(
    blorqueScript_BSIfBlock,
)
blorqueScript_BSCaseBlock_strategy = st.builds(
    blorqueScript_BSCaseBlock,
)
blorqueScript_BSLoopBlock_strategy = st.builds(
    blorqueScript_BSLoopBlock,
)
blorqueScript_BSSwitchBlock_strategy = st.builds(
    blorqueScript_BSSwitchBlock,
)
blorqueScript_BSMethodBody_strategy = st.builds(
    blorqueScript_BSMethodBody,
)
BSSymbol_strategy = st.builds(
    BSSymbol,
)
blorqueScript_BSParameter_strategy = st.builds(
    blorqueScript_BSParameter,
    isArray=
        st.booleans()
)
blorqueScript_BSVariableDeclaration_strategy = st.builds(
    blorqueScript_BSVariableDeclaration,
)
blorqueScript_BSMember_strategy = st.builds(
    blorqueScript_BSMember,
    isArray=
        st.booleans()
)
blorqueScript_BSClass_strategy = st.builds(
    blorqueScript_BSClass,
    name=
        safe_text
)
blorqueScript_BSImport_strategy = st.builds(
    blorqueScript_BSImport,
    importedNamespace=
        safe_text
)
blorqueScript_BSFile_strategy = st.builds(
    blorqueScript_BSFile,
    name=
        safe_text
)

@given(instance=BSExpression_strategy)
@settings(max_examples=50)
def test_bsexpression_instantiation(instance):
    assert isinstance(instance, BSExpression)

@given(instance=blorqueScript_BSPostfixArithmeticExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bspostfixarithmeticexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSPostfixArithmeticExpression)



@given(instance=blorqueScript_BSPostfixArithmeticExpression_strategy)
def test_blorquescript_bspostfixarithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSCastExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bscastexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCastExpression)



@given(instance=blorqueScript_BSCastExpression_strategy)
def test_blorquescript_bscastexpression_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original



@given(instance=blorqueScript_BSCastExpression_strategy)
def test_blorquescript_bscastexpression_pType_setter(instance):
    original = instance.pType
    instance.pType = original
    assert instance.pType == original

@given(instance=blorqueScript_BSMemberSelectionExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmemberselectionexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMemberSelectionExpression)

@given(instance=blorqueScript_BSPlusMinusOrStringConcatExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsplusminusorstringconcatexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSPlusMinusOrStringConcatExpression)



@given(instance=blorqueScript_BSPlusMinusOrStringConcatExpression_strategy)
def test_blorquescript_bsplusminusorstringconcatexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSBooleanAndExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbooleanandexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanAndExpression)

@given(instance=blorqueScript_BSClientLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript_bsclientliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSClientLiteral)

@given(instance=blorqueScript_BSBooleanConstant_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbooleanconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanConstant)



@given(instance=blorqueScript_BSBooleanConstant_strategy)
def test_blorquescript_bsbooleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript_BSEqualityExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsequalityexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSEqualityExpression)



@given(instance=blorqueScript_BSEqualityExpression_strategy)
def test_blorquescript_bsequalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSNullLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript_bsnullliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNullLiteral)

@given(instance=blorqueScript_BSBitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbitwisexorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseXorExpression)

@given(instance=blorqueScript_BSParentLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript_bsparentliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParentLiteral)

@given(instance=blorqueScript_BSBitwiseShiftExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbitwiseshiftexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseShiftExpression)



@given(instance=blorqueScript_BSBitwiseShiftExpression_strategy)
def test_blorquescript_bsbitwiseshiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSRealConstant_strategy)
@settings(max_examples=50)
def test_blorquescript_bsrealconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSRealConstant)



@given(instance=blorqueScript_BSRealConstant_strategy)
def test_blorquescript_bsrealconstant_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=blorqueScript_BSOrderedRelationExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsorderedrelationexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSOrderedRelationExpression)



@given(instance=blorqueScript_BSOrderedRelationExpression_strategy)
def test_blorquescript_bsorderedrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSMulDivOrModExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmuldivormodexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMulDivOrModExpression)



@given(instance=blorqueScript_BSMulDivOrModExpression_strategy)
def test_blorquescript_bsmuldivormodexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSParentheticalExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsparentheticalexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParentheticalExpression)

@given(instance=blorqueScript_BSSymbolRef_strategy)
@settings(max_examples=50)
def test_blorquescript_bssymbolref_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSymbolRef)

@given(instance=blorqueScript_BSNumberConstant_strategy)
@settings(max_examples=50)
def test_blorquescript_bsnumberconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNumberConstant)



@given(instance=blorqueScript_BSNumberConstant_strategy)
def test_blorquescript_bsnumberconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript_BSUnaryModifierExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsunarymodifierexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSUnaryModifierExpression)



@given(instance=blorqueScript_BSUnaryModifierExpression_strategy)
def test_blorquescript_bsunarymodifierexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript_BSBitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbitwiseandexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseAndExpression)

@given(instance=blorqueScript_BSHexadecimalConstant_strategy)
@settings(max_examples=50)
def test_blorquescript_bshexadecimalconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSHexadecimalConstant)



@given(instance=blorqueScript_BSHexadecimalConstant_strategy)
def test_blorquescript_bshexadecimalconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript_BSBitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbitwiseorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBitwiseOrExpression)

@given(instance=blorqueScript_BSStringConstant_strategy)
@settings(max_examples=50)
def test_blorquescript_bsstringconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSStringConstant)



@given(instance=blorqueScript_BSStringConstant_strategy)
def test_blorquescript_bsstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript_BSMethodInvokationExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmethodinvokationexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethodInvokationExpression)

@given(instance=blorqueScript_BSTernaryExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsternaryexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSTernaryExpression)

@given(instance=blorqueScript_BSNewExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsnewexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSNewExpression)



@given(instance=blorqueScript_BSNewExpression_strategy)
def test_blorquescript_bsnewexpression_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript_BSArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsarrayaccessexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSArrayAccessExpression)

@given(instance=blorqueScript_BSThisLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript_bsthisliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSThisLiteral)

@given(instance=blorqueScript_BSBooleanOrExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbooleanorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBooleanOrExpression)

@given(instance=blorqueScript_BSAssignmentExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsassignmentexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSAssignmentExpression)



@given(instance=blorqueScript_BSAssignmentExpression_strategy)
def test_blorquescript_bsassignmentexpression_assignmentOperator_setter(instance):
    original = instance.assignmentOperator
    instance.assignmentOperator = original
    assert instance.assignmentOperator == original

@given(instance=blorqueScript_BSSymbol_strategy)
@settings(max_examples=50)
def test_blorquescript_bssymbol_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSymbol)



@given(instance=blorqueScript_BSSymbol_strategy)
def test_blorquescript_bssymbol_pType_setter(instance):
    original = instance.pType
    instance.pType = original
    assert instance.pType == original



@given(instance=blorqueScript_BSSymbol_strategy)
def test_blorquescript_bssymbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=blorqueScript_BSBlock_strategy)
@settings(max_examples=50)
def test_blorquescript_bsblock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBlock)

@given(instance=blorqueScript_BSCase_strategy)
@settings(max_examples=50)
def test_blorquescript_bscase_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCase)

@given(instance=BSMember_strategy)
@settings(max_examples=50)
def test_bsmember_instantiation(instance):
    assert isinstance(instance, BSMember)

@given(instance=blorqueScript_BSMethod_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmethod_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethod)

@given(instance=blorqueScript_BSField_strategy)
@settings(max_examples=50)
def test_blorquescript_bsfield_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSField)

@given(instance=BSStatement_strategy)
@settings(max_examples=50)
def test_bsstatement_instantiation(instance):
    assert isinstance(instance, BSStatement)

@given(instance=blorqueScript_BSIfStatement_strategy)
@settings(max_examples=50)
def test_blorquescript_bsifstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSIfStatement)

@given(instance=blorqueScript_BSBreak_strategy)
@settings(max_examples=50)
def test_blorquescript_bsbreak_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSBreak)

@given(instance=blorqueScript_BSContinue_strategy)
@settings(max_examples=50)
def test_blorquescript_bscontinue_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSContinue)

@given(instance=blorqueScript_BSWhileLoop_strategy)
@settings(max_examples=50)
def test_blorquescript_bswhileloop_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSWhileLoop)

@given(instance=blorqueScript_BSForLoop_strategy)
@settings(max_examples=50)
def test_blorquescript_bsforloop_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSForLoop)

@given(instance=blorqueScript_BSExpression_strategy)
@settings(max_examples=50)
def test_blorquescript_bsexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSExpression)

@given(instance=blorqueScript_BSSwitchStatement_strategy)
@settings(max_examples=50)
def test_blorquescript_bsswitchstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSwitchStatement)



@given(instance=blorqueScript_BSSwitchStatement_strategy)
def test_blorquescript_bsswitchstatement_stringSwitch_setter(instance):
    original = instance.stringSwitch
    instance.stringSwitch = original
    assert instance.stringSwitch == original

@given(instance=blorqueScript_BSReturn_strategy)
@settings(max_examples=50)
def test_blorquescript_bsreturn_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSReturn)

@given(instance=blorqueScript_BSStatement_strategy)
@settings(max_examples=50)
def test_blorquescript_bsstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSStatement)

@given(instance=BSBlock_strategy)
@settings(max_examples=50)
def test_bsblock_instantiation(instance):
    assert isinstance(instance, BSBlock)

@given(instance=blorqueScript_BSIfBlock_strategy)
@settings(max_examples=50)
def test_blorquescript_bsifblock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSIfBlock)

@given(instance=blorqueScript_BSCaseBlock_strategy)
@settings(max_examples=50)
def test_blorquescript_bscaseblock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSCaseBlock)

@given(instance=blorqueScript_BSLoopBlock_strategy)
@settings(max_examples=50)
def test_blorquescript_bsloopblock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSLoopBlock)

@given(instance=blorqueScript_BSSwitchBlock_strategy)
@settings(max_examples=50)
def test_blorquescript_bsswitchblock_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSSwitchBlock)

@given(instance=blorqueScript_BSMethodBody_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmethodbody_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMethodBody)

@given(instance=BSSymbol_strategy)
@settings(max_examples=50)
def test_bssymbol_instantiation(instance):
    assert isinstance(instance, BSSymbol)

@given(instance=blorqueScript_BSParameter_strategy)
@settings(max_examples=50)
def test_blorquescript_bsparameter_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSParameter)



@given(instance=blorqueScript_BSParameter_strategy)
def test_blorquescript_bsparameter_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript_BSVariableDeclaration_strategy)
@settings(max_examples=50)
def test_blorquescript_bsvariabledeclaration_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSVariableDeclaration)

@given(instance=blorqueScript_BSMember_strategy)
@settings(max_examples=50)
def test_blorquescript_bsmember_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSMember)



@given(instance=blorqueScript_BSMember_strategy)
def test_blorquescript_bsmember_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript_BSClass_strategy)
@settings(max_examples=50)
def test_blorquescript_bsclass_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSClass)



@given(instance=blorqueScript_BSClass_strategy)
def test_blorquescript_bsclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=blorqueScript_BSImport_strategy)
@settings(max_examples=50)
def test_blorquescript_bsimport_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSImport)



@given(instance=blorqueScript_BSImport_strategy)
def test_blorquescript_bsimport_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=blorqueScript_BSFile_strategy)
@settings(max_examples=50)
def test_blorquescript_bsfile_instantiation(instance):
    assert isinstance(instance, blorqueScript_BSFile)



@given(instance=blorqueScript_BSFile_strategy)
def test_blorquescript_bsfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
