import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BSExpression,
    blorqueScript::BSMulDivOrModExpression,
    blorqueScript::BSUnaryModifierExpression,
    blorqueScript::BSTernaryExpression,
    blorqueScript::BSArrayAccessExpression,
    blorqueScript::BSPlusMinusOrStringConcatExpression,
    blorqueScript::BSBitwiseShiftExpression,
    blorqueScript::BSThisLiteral,
    blorqueScript::BSOrderedRelationExpression,
    blorqueScript::BSMemberSelectionExpression,
    blorqueScript::BSBitwiseAndExpression,
    blorqueScript::BSRealConstant,
    blorqueScript::BSNewExpression,
    blorqueScript::BSBitwiseOrExpression,
    blorqueScript::BSNullLiteral,
    blorqueScript::BSBooleanOrExpression,
    blorqueScript::BSClientLiteral,
    blorqueScript::BSCastExpression,
    blorqueScript::BSBooleanConstant,
    blorqueScript::BSSymbolRef,
    blorqueScript::BSMethodInvokationExpression,
    blorqueScript::BSEqualityExpression,
    blorqueScript::BSBooleanAndExpression,
    blorqueScript::BSHexadecimalConstant,
    blorqueScript::BSPostfixArithmeticExpression,
    blorqueScript::BSNumberConstant,
    blorqueScript::BSStringConstant,
    blorqueScript::BSBitwiseXorExpression,
    blorqueScript::BSParentheticalExpression,
    blorqueScript::BSParentLiteral,
    blorqueScript::BSAssignmentExpression,
    blorqueScript::BSSymbol,
    blorqueScript::BSBlock,
    blorqueScript::BSCase,
    BSMember,
    blorqueScript::BSMethod,
    blorqueScript::BSField,
    BSStatement,
    blorqueScript::BSSwitchStatement,
    blorqueScript::BSWhileLoop,
    blorqueScript::BSContinue,
    blorqueScript::BSBreak,
    blorqueScript::BSIfStatement,
    blorqueScript::BSForLoop,
    blorqueScript::BSExpression,
    blorqueScript::BSReturn,
    blorqueScript::BSStatement,
    BSBlock,
    blorqueScript::BSCaseBlock,
    blorqueScript::BSSwitchBlock,
    blorqueScript::BSLoopBlock,
    blorqueScript::BSIfBlock,
    blorqueScript::BSMethodBody,
    BSSymbol,
    blorqueScript::BSParameter,
    blorqueScript::BSVariableDeclaration,
    blorqueScript::BSMember,
    blorqueScript::BSClass,
    blorqueScript::BSImport,
    blorqueScript::BSFile,
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



def test_blorquescript::bsmuldivormodexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMulDivOrModExpression)


def test_blorquescript::bsmuldivormodexpression_constructor_exists():
    assert callable(blorqueScript::BSMulDivOrModExpression.__init__)


def test_blorquescript::bsmuldivormodexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSMulDivOrModExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsmuldivormodexpression_has_operator():
    assert hasattr(blorqueScript::BSMulDivOrModExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSMulDivOrModExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsunarymodifierexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSUnaryModifierExpression)


def test_blorquescript::bsunarymodifierexpression_constructor_exists():
    assert callable(blorqueScript::BSUnaryModifierExpression.__init__)


def test_blorquescript::bsunarymodifierexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSUnaryModifierExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsunarymodifierexpression_has_operator():
    assert hasattr(blorqueScript::BSUnaryModifierExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSUnaryModifierExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsternaryexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSTernaryExpression)


def test_blorquescript::bsternaryexpression_constructor_exists():
    assert callable(blorqueScript::BSTernaryExpression.__init__)


def test_blorquescript::bsternaryexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSTernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsarrayaccessexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSArrayAccessExpression)


def test_blorquescript::bsarrayaccessexpression_constructor_exists():
    assert callable(blorqueScript::BSArrayAccessExpression.__init__)


def test_blorquescript::bsarrayaccessexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSArrayAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsplusminusorstringconcatexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSPlusMinusOrStringConcatExpression)


def test_blorquescript::bsplusminusorstringconcatexpression_constructor_exists():
    assert callable(blorqueScript::BSPlusMinusOrStringConcatExpression.__init__)


def test_blorquescript::bsplusminusorstringconcatexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSPlusMinusOrStringConcatExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsplusminusorstringconcatexpression_has_operator():
    assert hasattr(blorqueScript::BSPlusMinusOrStringConcatExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSPlusMinusOrStringConcatExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsbitwiseshiftexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBitwiseShiftExpression)


def test_blorquescript::bsbitwiseshiftexpression_constructor_exists():
    assert callable(blorqueScript::BSBitwiseShiftExpression.__init__)


def test_blorquescript::bsbitwiseshiftexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBitwiseShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsbitwiseshiftexpression_has_operator():
    assert hasattr(blorqueScript::BSBitwiseShiftExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSBitwiseShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsthisliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSThisLiteral)


def test_blorquescript::bsthisliteral_constructor_exists():
    assert callable(blorqueScript::BSThisLiteral.__init__)


def test_blorquescript::bsthisliteral_constructor_args():
    sig = inspect.signature(blorqueScript::BSThisLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsorderedrelationexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSOrderedRelationExpression)


def test_blorquescript::bsorderedrelationexpression_constructor_exists():
    assert callable(blorqueScript::BSOrderedRelationExpression.__init__)


def test_blorquescript::bsorderedrelationexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSOrderedRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsorderedrelationexpression_has_operator():
    assert hasattr(blorqueScript::BSOrderedRelationExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSOrderedRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsmemberselectionexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMemberSelectionExpression)


def test_blorquescript::bsmemberselectionexpression_constructor_exists():
    assert callable(blorqueScript::BSMemberSelectionExpression.__init__)


def test_blorquescript::bsmemberselectionexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSMemberSelectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsbitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBitwiseAndExpression)


def test_blorquescript::bsbitwiseandexpression_constructor_exists():
    assert callable(blorqueScript::BSBitwiseAndExpression.__init__)


def test_blorquescript::bsbitwiseandexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsrealconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSRealConstant)


def test_blorquescript::bsrealconstant_constructor_exists():
    assert callable(blorqueScript::BSRealConstant.__init__)


def test_blorquescript::bsrealconstant_constructor_args():
    sig = inspect.signature(blorqueScript::BSRealConstant.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_blorquescript::bsrealconstant_has_right():
    assert hasattr(blorqueScript::BSRealConstant, "right")
    descriptor = None
    for klass in blorqueScript::BSRealConstant.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsnewexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSNewExpression)


def test_blorquescript::bsnewexpression_constructor_exists():
    assert callable(blorqueScript::BSNewExpression.__init__)


def test_blorquescript::bsnewexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSNewExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript::bsnewexpression_has_isArray():
    assert hasattr(blorqueScript::BSNewExpression, "isArray")
    descriptor = None
    for klass in blorqueScript::BSNewExpression.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsbitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBitwiseOrExpression)


def test_blorquescript::bsbitwiseorexpression_constructor_exists():
    assert callable(blorqueScript::BSBitwiseOrExpression.__init__)


def test_blorquescript::bsbitwiseorexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsnullliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSNullLiteral)


def test_blorquescript::bsnullliteral_constructor_exists():
    assert callable(blorqueScript::BSNullLiteral.__init__)


def test_blorquescript::bsnullliteral_constructor_args():
    sig = inspect.signature(blorqueScript::BSNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsbooleanorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBooleanOrExpression)


def test_blorquescript::bsbooleanorexpression_constructor_exists():
    assert callable(blorqueScript::BSBooleanOrExpression.__init__)


def test_blorquescript::bsbooleanorexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBooleanOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsclientliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSClientLiteral)


def test_blorquescript::bsclientliteral_constructor_exists():
    assert callable(blorqueScript::BSClientLiteral.__init__)


def test_blorquescript::bsclientliteral_constructor_args():
    sig = inspect.signature(blorqueScript::BSClientLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bscastexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSCastExpression)


def test_blorquescript::bscastexpression_constructor_exists():
    assert callable(blorqueScript::BSCastExpression.__init__)


def test_blorquescript::bscastexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSCastExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"
    assert "pType" in params, "Missing parameter 'pType'"

def test_blorquescript::bscastexpression_has_isArray():
    assert hasattr(blorqueScript::BSCastExpression, "isArray")
    descriptor = None
    for klass in blorqueScript::BSCastExpression.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)

def test_blorquescript::bscastexpression_has_pType():
    assert hasattr(blorqueScript::BSCastExpression, "pType")
    descriptor = None
    for klass in blorqueScript::BSCastExpression.__mro__:
        if "pType" in klass.__dict__:
            descriptor = klass.__dict__["pType"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsbooleanconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBooleanConstant)


def test_blorquescript::bsbooleanconstant_constructor_exists():
    assert callable(blorqueScript::BSBooleanConstant.__init__)


def test_blorquescript::bsbooleanconstant_constructor_args():
    sig = inspect.signature(blorqueScript::BSBooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript::bsbooleanconstant_has_value():
    assert hasattr(blorqueScript::BSBooleanConstant, "value")
    descriptor = None
    for klass in blorqueScript::BSBooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bssymbolref_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSSymbolRef)


def test_blorquescript::bssymbolref_constructor_exists():
    assert callable(blorqueScript::BSSymbolRef.__init__)


def test_blorquescript::bssymbolref_constructor_args():
    sig = inspect.signature(blorqueScript::BSSymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsmethodinvokationexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMethodInvokationExpression)


def test_blorquescript::bsmethodinvokationexpression_constructor_exists():
    assert callable(blorqueScript::BSMethodInvokationExpression.__init__)


def test_blorquescript::bsmethodinvokationexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSMethodInvokationExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsequalityexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSEqualityExpression)


def test_blorquescript::bsequalityexpression_constructor_exists():
    assert callable(blorqueScript::BSEqualityExpression.__init__)


def test_blorquescript::bsequalityexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSEqualityExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bsequalityexpression_has_operator():
    assert hasattr(blorqueScript::BSEqualityExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSEqualityExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsbooleanandexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBooleanAndExpression)


def test_blorquescript::bsbooleanandexpression_constructor_exists():
    assert callable(blorqueScript::BSBooleanAndExpression.__init__)


def test_blorquescript::bsbooleanandexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBooleanAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bshexadecimalconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSHexadecimalConstant)


def test_blorquescript::bshexadecimalconstant_constructor_exists():
    assert callable(blorqueScript::BSHexadecimalConstant.__init__)


def test_blorquescript::bshexadecimalconstant_constructor_args():
    sig = inspect.signature(blorqueScript::BSHexadecimalConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript::bshexadecimalconstant_has_value():
    assert hasattr(blorqueScript::BSHexadecimalConstant, "value")
    descriptor = None
    for klass in blorqueScript::BSHexadecimalConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bspostfixarithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSPostfixArithmeticExpression)


def test_blorquescript::bspostfixarithmeticexpression_constructor_exists():
    assert callable(blorqueScript::BSPostfixArithmeticExpression.__init__)


def test_blorquescript::bspostfixarithmeticexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSPostfixArithmeticExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_blorquescript::bspostfixarithmeticexpression_has_operator():
    assert hasattr(blorqueScript::BSPostfixArithmeticExpression, "operator")
    descriptor = None
    for klass in blorqueScript::BSPostfixArithmeticExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsnumberconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSNumberConstant)


def test_blorquescript::bsnumberconstant_constructor_exists():
    assert callable(blorqueScript::BSNumberConstant.__init__)


def test_blorquescript::bsnumberconstant_constructor_args():
    sig = inspect.signature(blorqueScript::BSNumberConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript::bsnumberconstant_has_value():
    assert hasattr(blorqueScript::BSNumberConstant, "value")
    descriptor = None
    for klass in blorqueScript::BSNumberConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsstringconstant_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSStringConstant)


def test_blorquescript::bsstringconstant_constructor_exists():
    assert callable(blorqueScript::BSStringConstant.__init__)


def test_blorquescript::bsstringconstant_constructor_args():
    sig = inspect.signature(blorqueScript::BSStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_blorquescript::bsstringconstant_has_value():
    assert hasattr(blorqueScript::BSStringConstant, "value")
    descriptor = None
    for klass in blorqueScript::BSStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsbitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBitwiseXorExpression)


def test_blorquescript::bsbitwisexorexpression_constructor_exists():
    assert callable(blorqueScript::BSBitwiseXorExpression.__init__)


def test_blorquescript::bsbitwisexorexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSBitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsparentheticalexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSParentheticalExpression)


def test_blorquescript::bsparentheticalexpression_constructor_exists():
    assert callable(blorqueScript::BSParentheticalExpression.__init__)


def test_blorquescript::bsparentheticalexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSParentheticalExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsparentliteral_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSParentLiteral)


def test_blorquescript::bsparentliteral_constructor_exists():
    assert callable(blorqueScript::BSParentLiteral.__init__)


def test_blorquescript::bsparentliteral_constructor_args():
    sig = inspect.signature(blorqueScript::BSParentLiteral.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSAssignmentExpression)


def test_blorquescript::bsassignmentexpression_constructor_exists():
    assert callable(blorqueScript::BSAssignmentExpression.__init__)


def test_blorquescript::bsassignmentexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSAssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "assignmentOperator" in params, "Missing parameter 'assignmentOperator'"

def test_blorquescript::bsassignmentexpression_has_assignmentOperator():
    assert hasattr(blorqueScript::BSAssignmentExpression, "assignmentOperator")
    descriptor = None
    for klass in blorqueScript::BSAssignmentExpression.__mro__:
        if "assignmentOperator" in klass.__dict__:
            descriptor = klass.__dict__["assignmentOperator"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bssymbol_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSSymbol)


def test_blorquescript::bssymbol_constructor_exists():
    assert callable(blorqueScript::BSSymbol.__init__)


def test_blorquescript::bssymbol_constructor_args():
    sig = inspect.signature(blorqueScript::BSSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "pType" in params, "Missing parameter 'pType'"

def test_blorquescript::bssymbol_has_name():
    assert hasattr(blorqueScript::BSSymbol, "name")
    descriptor = None
    for klass in blorqueScript::BSSymbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_blorquescript::bssymbol_has_pType():
    assert hasattr(blorqueScript::BSSymbol, "pType")
    descriptor = None
    for klass in blorqueScript::BSSymbol.__mro__:
        if "pType" in klass.__dict__:
            descriptor = klass.__dict__["pType"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBlock)


def test_blorquescript::bsblock_constructor_exists():
    assert callable(blorqueScript::BSBlock.__init__)


def test_blorquescript::bsblock_constructor_args():
    sig = inspect.signature(blorqueScript::BSBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bscase_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSCase)


def test_blorquescript::bscase_constructor_exists():
    assert callable(blorqueScript::BSCase.__init__)


def test_blorquescript::bscase_constructor_args():
    sig = inspect.signature(blorqueScript::BSCase.__init__)
    params = list(sig.parameters.keys())



def test_bsmember_is_not_abstract():
    assert not inspect.isabstract(BSMember)


def test_bsmember_constructor_exists():
    assert callable(BSMember.__init__)


def test_bsmember_constructor_args():
    sig = inspect.signature(BSMember.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsmethod_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMethod)


def test_blorquescript::bsmethod_constructor_exists():
    assert callable(blorqueScript::BSMethod.__init__)


def test_blorquescript::bsmethod_constructor_args():
    sig = inspect.signature(blorqueScript::BSMethod.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsfield_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSField)


def test_blorquescript::bsfield_constructor_exists():
    assert callable(blorqueScript::BSField.__init__)


def test_blorquescript::bsfield_constructor_args():
    sig = inspect.signature(blorqueScript::BSField.__init__)
    params = list(sig.parameters.keys())



def test_bsstatement_is_not_abstract():
    assert not inspect.isabstract(BSStatement)


def test_bsstatement_constructor_exists():
    assert callable(BSStatement.__init__)


def test_bsstatement_constructor_args():
    sig = inspect.signature(BSStatement.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsswitchstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSSwitchStatement)


def test_blorquescript::bsswitchstatement_constructor_exists():
    assert callable(blorqueScript::BSSwitchStatement.__init__)


def test_blorquescript::bsswitchstatement_constructor_args():
    sig = inspect.signature(blorqueScript::BSSwitchStatement.__init__)
    params = list(sig.parameters.keys())
    assert "stringSwitch" in params, "Missing parameter 'stringSwitch'"

def test_blorquescript::bsswitchstatement_has_stringSwitch():
    assert hasattr(blorqueScript::BSSwitchStatement, "stringSwitch")
    descriptor = None
    for klass in blorqueScript::BSSwitchStatement.__mro__:
        if "stringSwitch" in klass.__dict__:
            descriptor = klass.__dict__["stringSwitch"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bswhileloop_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSWhileLoop)


def test_blorquescript::bswhileloop_constructor_exists():
    assert callable(blorqueScript::BSWhileLoop.__init__)


def test_blorquescript::bswhileloop_constructor_args():
    sig = inspect.signature(blorqueScript::BSWhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bscontinue_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSContinue)


def test_blorquescript::bscontinue_constructor_exists():
    assert callable(blorqueScript::BSContinue.__init__)


def test_blorquescript::bscontinue_constructor_args():
    sig = inspect.signature(blorqueScript::BSContinue.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsbreak_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSBreak)


def test_blorquescript::bsbreak_constructor_exists():
    assert callable(blorqueScript::BSBreak.__init__)


def test_blorquescript::bsbreak_constructor_args():
    sig = inspect.signature(blorqueScript::BSBreak.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsifstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSIfStatement)


def test_blorquescript::bsifstatement_constructor_exists():
    assert callable(blorqueScript::BSIfStatement.__init__)


def test_blorquescript::bsifstatement_constructor_args():
    sig = inspect.signature(blorqueScript::BSIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsforloop_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSForLoop)


def test_blorquescript::bsforloop_constructor_exists():
    assert callable(blorqueScript::BSForLoop.__init__)


def test_blorquescript::bsforloop_constructor_args():
    sig = inspect.signature(blorqueScript::BSForLoop.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsexpression_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSExpression)


def test_blorquescript::bsexpression_constructor_exists():
    assert callable(blorqueScript::BSExpression.__init__)


def test_blorquescript::bsexpression_constructor_args():
    sig = inspect.signature(blorqueScript::BSExpression.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsreturn_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSReturn)


def test_blorquescript::bsreturn_constructor_exists():
    assert callable(blorqueScript::BSReturn.__init__)


def test_blorquescript::bsreturn_constructor_args():
    sig = inspect.signature(blorqueScript::BSReturn.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsstatement_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSStatement)


def test_blorquescript::bsstatement_constructor_exists():
    assert callable(blorqueScript::BSStatement.__init__)


def test_blorquescript::bsstatement_constructor_args():
    sig = inspect.signature(blorqueScript::BSStatement.__init__)
    params = list(sig.parameters.keys())



def test_bsblock_is_not_abstract():
    assert not inspect.isabstract(BSBlock)


def test_bsblock_constructor_exists():
    assert callable(BSBlock.__init__)


def test_bsblock_constructor_args():
    sig = inspect.signature(BSBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bscaseblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSCaseBlock)


def test_blorquescript::bscaseblock_constructor_exists():
    assert callable(blorqueScript::BSCaseBlock.__init__)


def test_blorquescript::bscaseblock_constructor_args():
    sig = inspect.signature(blorqueScript::BSCaseBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsswitchblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSSwitchBlock)


def test_blorquescript::bsswitchblock_constructor_exists():
    assert callable(blorqueScript::BSSwitchBlock.__init__)


def test_blorquescript::bsswitchblock_constructor_args():
    sig = inspect.signature(blorqueScript::BSSwitchBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsloopblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSLoopBlock)


def test_blorquescript::bsloopblock_constructor_exists():
    assert callable(blorqueScript::BSLoopBlock.__init__)


def test_blorquescript::bsloopblock_constructor_args():
    sig = inspect.signature(blorqueScript::BSLoopBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsifblock_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSIfBlock)


def test_blorquescript::bsifblock_constructor_exists():
    assert callable(blorqueScript::BSIfBlock.__init__)


def test_blorquescript::bsifblock_constructor_args():
    sig = inspect.signature(blorqueScript::BSIfBlock.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsmethodbody_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMethodBody)


def test_blorquescript::bsmethodbody_constructor_exists():
    assert callable(blorqueScript::BSMethodBody.__init__)


def test_blorquescript::bsmethodbody_constructor_args():
    sig = inspect.signature(blorqueScript::BSMethodBody.__init__)
    params = list(sig.parameters.keys())



def test_bssymbol_is_not_abstract():
    assert not inspect.isabstract(BSSymbol)


def test_bssymbol_constructor_exists():
    assert callable(BSSymbol.__init__)


def test_bssymbol_constructor_args():
    sig = inspect.signature(BSSymbol.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsparameter_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSParameter)


def test_blorquescript::bsparameter_constructor_exists():
    assert callable(blorqueScript::BSParameter.__init__)


def test_blorquescript::bsparameter_constructor_args():
    sig = inspect.signature(blorqueScript::BSParameter.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript::bsparameter_has_isArray():
    assert hasattr(blorqueScript::BSParameter, "isArray")
    descriptor = None
    for klass in blorqueScript::BSParameter.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSVariableDeclaration)


def test_blorquescript::bsvariabledeclaration_constructor_exists():
    assert callable(blorqueScript::BSVariableDeclaration.__init__)


def test_blorquescript::bsvariabledeclaration_constructor_args():
    sig = inspect.signature(blorqueScript::BSVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_blorquescript::bsmember_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSMember)


def test_blorquescript::bsmember_constructor_exists():
    assert callable(blorqueScript::BSMember.__init__)


def test_blorquescript::bsmember_constructor_args():
    sig = inspect.signature(blorqueScript::BSMember.__init__)
    params = list(sig.parameters.keys())
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_blorquescript::bsmember_has_isArray():
    assert hasattr(blorqueScript::BSMember, "isArray")
    descriptor = None
    for klass in blorqueScript::BSMember.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsclass_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSClass)


def test_blorquescript::bsclass_constructor_exists():
    assert callable(blorqueScript::BSClass.__init__)


def test_blorquescript::bsclass_constructor_args():
    sig = inspect.signature(blorqueScript::BSClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_blorquescript::bsclass_has_name():
    assert hasattr(blorqueScript::BSClass, "name")
    descriptor = None
    for klass in blorqueScript::BSClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsimport_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSImport)


def test_blorquescript::bsimport_constructor_exists():
    assert callable(blorqueScript::BSImport.__init__)


def test_blorquescript::bsimport_constructor_args():
    sig = inspect.signature(blorqueScript::BSImport.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_blorquescript::bsimport_has_importedNamespace():
    assert hasattr(blorqueScript::BSImport, "importedNamespace")
    descriptor = None
    for klass in blorqueScript::BSImport.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_blorquescript::bsfile_is_not_abstract():
    assert not inspect.isabstract(blorqueScript::BSFile)


def test_blorquescript::bsfile_constructor_exists():
    assert callable(blorqueScript::BSFile.__init__)


def test_blorquescript::bsfile_constructor_args():
    sig = inspect.signature(blorqueScript::BSFile.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_blorquescript::bsfile_has_name():
    assert hasattr(blorqueScript::BSFile, "name")
    descriptor = None
    for klass in blorqueScript::BSFile.__mro__:
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
        "VOID",
        "OBJECT",
        "STRING",
        "TAGGED_STRING",
        "NONE",
        "NUMBER",
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
blorqueScript::BSMulDivOrModExpression_strategy = st.builds(
    blorqueScript::BSMulDivOrModExpression,
    operator=
        safe_text
)
blorqueScript::BSUnaryModifierExpression_strategy = st.builds(
    blorqueScript::BSUnaryModifierExpression,
    operator=
        safe_text
)
blorqueScript::BSTernaryExpression_strategy = st.builds(
    blorqueScript::BSTernaryExpression,
)
blorqueScript::BSArrayAccessExpression_strategy = st.builds(
    blorqueScript::BSArrayAccessExpression,
)
blorqueScript::BSPlusMinusOrStringConcatExpression_strategy = st.builds(
    blorqueScript::BSPlusMinusOrStringConcatExpression,
    operator=
        safe_text
)
blorqueScript::BSBitwiseShiftExpression_strategy = st.builds(
    blorqueScript::BSBitwiseShiftExpression,
    operator=
        safe_text
)
blorqueScript::BSThisLiteral_strategy = st.builds(
    blorqueScript::BSThisLiteral,
)
blorqueScript::BSOrderedRelationExpression_strategy = st.builds(
    blorqueScript::BSOrderedRelationExpression,
    operator=
        safe_text
)
blorqueScript::BSMemberSelectionExpression_strategy = st.builds(
    blorqueScript::BSMemberSelectionExpression,
)
blorqueScript::BSBitwiseAndExpression_strategy = st.builds(
    blorqueScript::BSBitwiseAndExpression,
)
blorqueScript::BSRealConstant_strategy = st.builds(
    blorqueScript::BSRealConstant,
    right=
        st.integers()
)
blorqueScript::BSNewExpression_strategy = st.builds(
    blorqueScript::BSNewExpression,
    isArray=
        st.booleans()
)
blorqueScript::BSBitwiseOrExpression_strategy = st.builds(
    blorqueScript::BSBitwiseOrExpression,
)
blorqueScript::BSNullLiteral_strategy = st.builds(
    blorqueScript::BSNullLiteral,
)
blorqueScript::BSBooleanOrExpression_strategy = st.builds(
    blorqueScript::BSBooleanOrExpression,
)
blorqueScript::BSClientLiteral_strategy = st.builds(
    blorqueScript::BSClientLiteral,
)
blorqueScript::BSCastExpression_strategy = st.builds(
    blorqueScript::BSCastExpression,
    isArray=
        st.booleans(),
    pType=
        safe_text
)
blorqueScript::BSBooleanConstant_strategy = st.builds(
    blorqueScript::BSBooleanConstant,
    value=
        safe_text
)
blorqueScript::BSSymbolRef_strategy = st.builds(
    blorqueScript::BSSymbolRef,
)
blorqueScript::BSMethodInvokationExpression_strategy = st.builds(
    blorqueScript::BSMethodInvokationExpression,
)
blorqueScript::BSEqualityExpression_strategy = st.builds(
    blorqueScript::BSEqualityExpression,
    operator=
        safe_text
)
blorqueScript::BSBooleanAndExpression_strategy = st.builds(
    blorqueScript::BSBooleanAndExpression,
)
blorqueScript::BSHexadecimalConstant_strategy = st.builds(
    blorqueScript::BSHexadecimalConstant,
    value=
        safe_text
)
blorqueScript::BSPostfixArithmeticExpression_strategy = st.builds(
    blorqueScript::BSPostfixArithmeticExpression,
    operator=
        safe_text
)
blorqueScript::BSNumberConstant_strategy = st.builds(
    blorqueScript::BSNumberConstant,
    value=
        st.integers()
)
blorqueScript::BSStringConstant_strategy = st.builds(
    blorqueScript::BSStringConstant,
    value=
        safe_text
)
blorqueScript::BSBitwiseXorExpression_strategy = st.builds(
    blorqueScript::BSBitwiseXorExpression,
)
blorqueScript::BSParentheticalExpression_strategy = st.builds(
    blorqueScript::BSParentheticalExpression,
)
blorqueScript::BSParentLiteral_strategy = st.builds(
    blorqueScript::BSParentLiteral,
)
blorqueScript::BSAssignmentExpression_strategy = st.builds(
    blorqueScript::BSAssignmentExpression,
    assignmentOperator=
        safe_text
)
blorqueScript::BSSymbol_strategy = st.builds(
    blorqueScript::BSSymbol,
    name=
        safe_text,
    pType=
        safe_text
)
blorqueScript::BSBlock_strategy = st.builds(
    blorqueScript::BSBlock,
)
blorqueScript::BSCase_strategy = st.builds(
    blorqueScript::BSCase,
)
BSMember_strategy = st.builds(
    BSMember,
)
blorqueScript::BSMethod_strategy = st.builds(
    blorqueScript::BSMethod,
)
blorqueScript::BSField_strategy = st.builds(
    blorqueScript::BSField,
)
BSStatement_strategy = st.builds(
    BSStatement,
)
blorqueScript::BSSwitchStatement_strategy = st.builds(
    blorqueScript::BSSwitchStatement,
    stringSwitch=
        st.booleans()
)
blorqueScript::BSWhileLoop_strategy = st.builds(
    blorqueScript::BSWhileLoop,
)
blorqueScript::BSContinue_strategy = st.builds(
    blorqueScript::BSContinue,
)
blorqueScript::BSBreak_strategy = st.builds(
    blorqueScript::BSBreak,
)
blorqueScript::BSIfStatement_strategy = st.builds(
    blorqueScript::BSIfStatement,
)
blorqueScript::BSForLoop_strategy = st.builds(
    blorqueScript::BSForLoop,
)
blorqueScript::BSExpression_strategy = st.builds(
    blorqueScript::BSExpression,
)
blorqueScript::BSReturn_strategy = st.builds(
    blorqueScript::BSReturn,
)
blorqueScript::BSStatement_strategy = st.builds(
    blorqueScript::BSStatement,
)
BSBlock_strategy = st.builds(
    BSBlock,
)
blorqueScript::BSCaseBlock_strategy = st.builds(
    blorqueScript::BSCaseBlock,
)
blorqueScript::BSSwitchBlock_strategy = st.builds(
    blorqueScript::BSSwitchBlock,
)
blorqueScript::BSLoopBlock_strategy = st.builds(
    blorqueScript::BSLoopBlock,
)
blorqueScript::BSIfBlock_strategy = st.builds(
    blorqueScript::BSIfBlock,
)
blorqueScript::BSMethodBody_strategy = st.builds(
    blorqueScript::BSMethodBody,
)
BSSymbol_strategy = st.builds(
    BSSymbol,
)
blorqueScript::BSParameter_strategy = st.builds(
    blorqueScript::BSParameter,
    isArray=
        st.booleans()
)
blorqueScript::BSVariableDeclaration_strategy = st.builds(
    blorqueScript::BSVariableDeclaration,
)
blorqueScript::BSMember_strategy = st.builds(
    blorqueScript::BSMember,
    isArray=
        st.booleans()
)
blorqueScript::BSClass_strategy = st.builds(
    blorqueScript::BSClass,
    name=
        safe_text
)
blorqueScript::BSImport_strategy = st.builds(
    blorqueScript::BSImport,
    importedNamespace=
        safe_text
)
blorqueScript::BSFile_strategy = st.builds(
    blorqueScript::BSFile,
    name=
        safe_text
)

@given(instance=BSExpression_strategy)
@settings(max_examples=50)
def test_bsexpression_instantiation(instance):
    assert isinstance(instance, BSExpression)

@given(instance=blorqueScript::BSMulDivOrModExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmuldivormodexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMulDivOrModExpression)

@given(instance=blorqueScript::BSMulDivOrModExpression_strategy)
def test_blorquescript::bsmuldivormodexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSMulDivOrModExpression_strategy)
def test_blorquescript::bsmuldivormodexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSUnaryModifierExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsunarymodifierexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSUnaryModifierExpression)

@given(instance=blorqueScript::BSUnaryModifierExpression_strategy)
def test_blorquescript::bsunarymodifierexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSUnaryModifierExpression_strategy)
def test_blorquescript::bsunarymodifierexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSTernaryExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsternaryexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSTernaryExpression)

@given(instance=blorqueScript::BSArrayAccessExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsarrayaccessexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSArrayAccessExpression)

@given(instance=blorqueScript::BSPlusMinusOrStringConcatExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsplusminusorstringconcatexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSPlusMinusOrStringConcatExpression)

@given(instance=blorqueScript::BSPlusMinusOrStringConcatExpression_strategy)
def test_blorquescript::bsplusminusorstringconcatexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSPlusMinusOrStringConcatExpression_strategy)
def test_blorquescript::bsplusminusorstringconcatexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSBitwiseShiftExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbitwiseshiftexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBitwiseShiftExpression)

@given(instance=blorqueScript::BSBitwiseShiftExpression_strategy)
def test_blorquescript::bsbitwiseshiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSBitwiseShiftExpression_strategy)
def test_blorquescript::bsbitwiseshiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSThisLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript::bsthisliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSThisLiteral)

@given(instance=blorqueScript::BSOrderedRelationExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsorderedrelationexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSOrderedRelationExpression)

@given(instance=blorqueScript::BSOrderedRelationExpression_strategy)
def test_blorquescript::bsorderedrelationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSOrderedRelationExpression_strategy)
def test_blorquescript::bsorderedrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSMemberSelectionExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmemberselectionexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMemberSelectionExpression)

@given(instance=blorqueScript::BSBitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbitwiseandexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBitwiseAndExpression)

@given(instance=blorqueScript::BSRealConstant_strategy)
@settings(max_examples=50)
def test_blorquescript::bsrealconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSRealConstant)

@given(instance=blorqueScript::BSRealConstant_strategy)
def test_blorquescript::bsrealconstant_right_type(instance):
    assert isinstance(instance.right, int)


@given(instance=blorqueScript::BSRealConstant_strategy)
def test_blorquescript::bsrealconstant_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=blorqueScript::BSNewExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsnewexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSNewExpression)

@given(instance=blorqueScript::BSNewExpression_strategy)
def test_blorquescript::bsnewexpression_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=blorqueScript::BSNewExpression_strategy)
def test_blorquescript::bsnewexpression_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript::BSBitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbitwiseorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBitwiseOrExpression)

@given(instance=blorqueScript::BSNullLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript::bsnullliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSNullLiteral)

@given(instance=blorqueScript::BSBooleanOrExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbooleanorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBooleanOrExpression)

@given(instance=blorqueScript::BSClientLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript::bsclientliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSClientLiteral)

@given(instance=blorqueScript::BSCastExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bscastexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSCastExpression)

@given(instance=blorqueScript::BSCastExpression_strategy)
def test_blorquescript::bscastexpression_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=blorqueScript::BSCastExpression_strategy)
def test_blorquescript::bscastexpression_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript::BSCastExpression_strategy)
def test_blorquescript::bscastexpression_pType_type(instance):
    assert isinstance(instance.pType, str)


@given(instance=blorqueScript::BSCastExpression_strategy)
def test_blorquescript::bscastexpression_pType_setter(instance):
    original = instance.pType
    instance.pType = original
    assert instance.pType == original

@given(instance=blorqueScript::BSBooleanConstant_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbooleanconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBooleanConstant)

@given(instance=blorqueScript::BSBooleanConstant_strategy)
def test_blorquescript::bsbooleanconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=blorqueScript::BSBooleanConstant_strategy)
def test_blorquescript::bsbooleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript::BSSymbolRef_strategy)
@settings(max_examples=50)
def test_blorquescript::bssymbolref_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSSymbolRef)

@given(instance=blorqueScript::BSMethodInvokationExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmethodinvokationexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMethodInvokationExpression)

@given(instance=blorqueScript::BSEqualityExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsequalityexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSEqualityExpression)

@given(instance=blorqueScript::BSEqualityExpression_strategy)
def test_blorquescript::bsequalityexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSEqualityExpression_strategy)
def test_blorquescript::bsequalityexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSBooleanAndExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbooleanandexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBooleanAndExpression)

@given(instance=blorqueScript::BSHexadecimalConstant_strategy)
@settings(max_examples=50)
def test_blorquescript::bshexadecimalconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSHexadecimalConstant)

@given(instance=blorqueScript::BSHexadecimalConstant_strategy)
def test_blorquescript::bshexadecimalconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=blorqueScript::BSHexadecimalConstant_strategy)
def test_blorquescript::bshexadecimalconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript::BSPostfixArithmeticExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bspostfixarithmeticexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSPostfixArithmeticExpression)

@given(instance=blorqueScript::BSPostfixArithmeticExpression_strategy)
def test_blorquescript::bspostfixarithmeticexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=blorqueScript::BSPostfixArithmeticExpression_strategy)
def test_blorquescript::bspostfixarithmeticexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=blorqueScript::BSNumberConstant_strategy)
@settings(max_examples=50)
def test_blorquescript::bsnumberconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSNumberConstant)

@given(instance=blorqueScript::BSNumberConstant_strategy)
def test_blorquescript::bsnumberconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=blorqueScript::BSNumberConstant_strategy)
def test_blorquescript::bsnumberconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript::BSStringConstant_strategy)
@settings(max_examples=50)
def test_blorquescript::bsstringconstant_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSStringConstant)

@given(instance=blorqueScript::BSStringConstant_strategy)
def test_blorquescript::bsstringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=blorqueScript::BSStringConstant_strategy)
def test_blorquescript::bsstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=blorqueScript::BSBitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbitwisexorexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBitwiseXorExpression)

@given(instance=blorqueScript::BSParentheticalExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsparentheticalexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSParentheticalExpression)

@given(instance=blorqueScript::BSParentLiteral_strategy)
@settings(max_examples=50)
def test_blorquescript::bsparentliteral_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSParentLiteral)

@given(instance=blorqueScript::BSAssignmentExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsassignmentexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSAssignmentExpression)

@given(instance=blorqueScript::BSAssignmentExpression_strategy)
def test_blorquescript::bsassignmentexpression_assignmentOperator_type(instance):
    assert isinstance(instance.assignmentOperator, str)


@given(instance=blorqueScript::BSAssignmentExpression_strategy)
def test_blorquescript::bsassignmentexpression_assignmentOperator_setter(instance):
    original = instance.assignmentOperator
    instance.assignmentOperator = original
    assert instance.assignmentOperator == original

@given(instance=blorqueScript::BSSymbol_strategy)
@settings(max_examples=50)
def test_blorquescript::bssymbol_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSSymbol)

@given(instance=blorqueScript::BSSymbol_strategy)
def test_blorquescript::bssymbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=blorqueScript::BSSymbol_strategy)
def test_blorquescript::bssymbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=blorqueScript::BSSymbol_strategy)
def test_blorquescript::bssymbol_pType_type(instance):
    assert isinstance(instance.pType, str)


@given(instance=blorqueScript::BSSymbol_strategy)
def test_blorquescript::bssymbol_pType_setter(instance):
    original = instance.pType
    instance.pType = original
    assert instance.pType == original

@given(instance=blorqueScript::BSBlock_strategy)
@settings(max_examples=50)
def test_blorquescript::bsblock_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBlock)

@given(instance=blorqueScript::BSCase_strategy)
@settings(max_examples=50)
def test_blorquescript::bscase_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSCase)

@given(instance=BSMember_strategy)
@settings(max_examples=50)
def test_bsmember_instantiation(instance):
    assert isinstance(instance, BSMember)

@given(instance=blorqueScript::BSMethod_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmethod_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMethod)

@given(instance=blorqueScript::BSField_strategy)
@settings(max_examples=50)
def test_blorquescript::bsfield_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSField)

@given(instance=BSStatement_strategy)
@settings(max_examples=50)
def test_bsstatement_instantiation(instance):
    assert isinstance(instance, BSStatement)

@given(instance=blorqueScript::BSSwitchStatement_strategy)
@settings(max_examples=50)
def test_blorquescript::bsswitchstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSSwitchStatement)

@given(instance=blorqueScript::BSSwitchStatement_strategy)
def test_blorquescript::bsswitchstatement_stringSwitch_type(instance):
    assert isinstance(instance.stringSwitch, bool)


@given(instance=blorqueScript::BSSwitchStatement_strategy)
def test_blorquescript::bsswitchstatement_stringSwitch_setter(instance):
    original = instance.stringSwitch
    instance.stringSwitch = original
    assert instance.stringSwitch == original

@given(instance=blorqueScript::BSWhileLoop_strategy)
@settings(max_examples=50)
def test_blorquescript::bswhileloop_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSWhileLoop)

@given(instance=blorqueScript::BSContinue_strategy)
@settings(max_examples=50)
def test_blorquescript::bscontinue_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSContinue)

@given(instance=blorqueScript::BSBreak_strategy)
@settings(max_examples=50)
def test_blorquescript::bsbreak_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSBreak)

@given(instance=blorqueScript::BSIfStatement_strategy)
@settings(max_examples=50)
def test_blorquescript::bsifstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSIfStatement)

@given(instance=blorqueScript::BSForLoop_strategy)
@settings(max_examples=50)
def test_blorquescript::bsforloop_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSForLoop)

@given(instance=blorqueScript::BSExpression_strategy)
@settings(max_examples=50)
def test_blorquescript::bsexpression_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSExpression)

@given(instance=blorqueScript::BSReturn_strategy)
@settings(max_examples=50)
def test_blorquescript::bsreturn_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSReturn)

@given(instance=blorqueScript::BSStatement_strategy)
@settings(max_examples=50)
def test_blorquescript::bsstatement_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSStatement)

@given(instance=BSBlock_strategy)
@settings(max_examples=50)
def test_bsblock_instantiation(instance):
    assert isinstance(instance, BSBlock)

@given(instance=blorqueScript::BSCaseBlock_strategy)
@settings(max_examples=50)
def test_blorquescript::bscaseblock_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSCaseBlock)

@given(instance=blorqueScript::BSSwitchBlock_strategy)
@settings(max_examples=50)
def test_blorquescript::bsswitchblock_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSSwitchBlock)

@given(instance=blorqueScript::BSLoopBlock_strategy)
@settings(max_examples=50)
def test_blorquescript::bsloopblock_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSLoopBlock)

@given(instance=blorqueScript::BSIfBlock_strategy)
@settings(max_examples=50)
def test_blorquescript::bsifblock_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSIfBlock)

@given(instance=blorqueScript::BSMethodBody_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmethodbody_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMethodBody)

@given(instance=BSSymbol_strategy)
@settings(max_examples=50)
def test_bssymbol_instantiation(instance):
    assert isinstance(instance, BSSymbol)

@given(instance=blorqueScript::BSParameter_strategy)
@settings(max_examples=50)
def test_blorquescript::bsparameter_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSParameter)

@given(instance=blorqueScript::BSParameter_strategy)
def test_blorquescript::bsparameter_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=blorqueScript::BSParameter_strategy)
def test_blorquescript::bsparameter_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript::BSVariableDeclaration_strategy)
@settings(max_examples=50)
def test_blorquescript::bsvariabledeclaration_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSVariableDeclaration)

@given(instance=blorqueScript::BSMember_strategy)
@settings(max_examples=50)
def test_blorquescript::bsmember_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSMember)

@given(instance=blorqueScript::BSMember_strategy)
def test_blorquescript::bsmember_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=blorqueScript::BSMember_strategy)
def test_blorquescript::bsmember_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=blorqueScript::BSClass_strategy)
@settings(max_examples=50)
def test_blorquescript::bsclass_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSClass)

@given(instance=blorqueScript::BSClass_strategy)
def test_blorquescript::bsclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=blorqueScript::BSClass_strategy)
def test_blorquescript::bsclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=blorqueScript::BSImport_strategy)
@settings(max_examples=50)
def test_blorquescript::bsimport_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSImport)

@given(instance=blorqueScript::BSImport_strategy)
def test_blorquescript::bsimport_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=blorqueScript::BSImport_strategy)
def test_blorquescript::bsimport_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=blorqueScript::BSFile_strategy)
@settings(max_examples=50)
def test_blorquescript::bsfile_instantiation(instance):
    assert isinstance(instance, blorqueScript::BSFile)

@given(instance=blorqueScript::BSFile_strategy)
def test_blorquescript::bsfile_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=blorqueScript::BSFile_strategy)
def test_blorquescript::bsfile_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
