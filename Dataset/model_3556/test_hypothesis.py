import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModuleType,
    RTCTLExpression,
    nuSMV_UnaryRTCTLExpression,
    nuSMV_SingleRTCTLExpression,
    nuSMV_SyncrProcessType,
    nuSMV_AsyncrProcessType,
    SimpleType,
    nuSMV_EnumType,
    nuSMV_WordType,
    nuSMV_ArrayType,
    nuSMV_SignedWordType,
    nuSMV_UnsignedWordType,
    nuSMV_IntervalType,
    nuSMV_BooleanType,
    nuSMV_RTCTLExpression,
    nuSMV_RangeExpression,
    nuSMV_CaseSimpleAssignementExpression,
    SimpleExpression,
    nuSMV_SetElementExpression,
    nuSMV_ValueExpression,
    nuSMV_UnaryExpression,
    nuSMV_UntilCTLexpression,
    nuSMV_SetValueParameter,
    nuSMV_Not,
    nuSMV_UnaryFunctionExpression,
    nuSMV_IntervalExpression,
    nuSMV_WordExpression,
    nuSMV_SetExpression,
    nuSMV_ParsExpression,
    nuSMV_Var,
    nuSMV_BinaryExpression,
    nuSMV_CaseSimpleExpression,
    nuSMV_Val,
    Type,
    nuSMV_SimpleType,
    nuSMV_ModuleType,
    nuSMV_LTLExpression,
    nuSMV_CTLExpression,
    FairnessConstraint,
    nuSMV_CompassionExpression,
    nuSMV_JusticeExpression,
    nuSMV_FairnessExpression,
    nuSMV_NextExpression,
    AssignBody,
    nuSMV_InitBody,
    nuSMV_NextBody,
    nuSMV_VarBodyAssign,
    nuSMV_EObject,
    nuSMV_AssignBody,
    nuSMV_SimpleExpression,
    nuSMV_DefineBody,
    nuSMV_Type,
    nuSMV_VarBody,
    ModuleElement,
    nuSMV_TransConstraint,
    nuSMV_ConstantsDeclaration,
    nuSMV_FairnessConstraint,
    nuSMV_IVariableDeclaration,
    nuSMV_LtlSpecification,
    nuSMV_FrozenVariableDeclaration,
    nuSMV_InvarConstraint,
    nuSMV_InitConstraint,
    nuSMV_ComputeSpecification,
    nuSMV_AssignConstraintElement,
    nuSMV_DefineDeclaration,
    nuSMV_InvarSpecification,
    nuSMV_CtlSpecification,
    nuSMV_IsaDeclaration,
    nuSMV_VariableDeclaration,
    nuSMV_ModuleElement,
    nuSMV_FormalParameter,
    nuSMV_Module,
    nuSMV_NuSmvModel,
    operators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_moduletype_is_not_abstract():
    assert not inspect.isabstract(ModuleType)


def test_moduletype_constructor_exists():
    assert callable(ModuleType.__init__)


def test_moduletype_constructor_args():
    sig = inspect.signature(ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_rtctlexpression_is_not_abstract():
    assert not inspect.isabstract(RTCTLExpression)


def test_rtctlexpression_constructor_exists():
    assert callable(RTCTLExpression.__init__)


def test_rtctlexpression_constructor_args():
    sig = inspect.signature(RTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_unaryrtctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_UnaryRTCTLExpression)


def test_nusmv_unaryrtctlexpression_constructor_exists():
    assert callable(nuSMV_UnaryRTCTLExpression.__init__)


def test_nusmv_unaryrtctlexpression_constructor_args():
    sig = inspect.signature(nuSMV_UnaryRTCTLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unary" in params, "Missing parameter 'unary'"

def test_nusmv_unaryrtctlexpression_has_unary():
    assert hasattr(nuSMV_UnaryRTCTLExpression, "unary")
    descriptor = None
    for klass in nuSMV_UnaryRTCTLExpression.__mro__:
        if "unary" in klass.__dict__:
            descriptor = klass.__dict__["unary"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_singlertctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SingleRTCTLExpression)


def test_nusmv_singlertctlexpression_constructor_exists():
    assert callable(nuSMV_SingleRTCTLExpression.__init__)


def test_nusmv_singlertctlexpression_constructor_args():
    sig = inspect.signature(nuSMV_SingleRTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_syncrprocesstype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SyncrProcessType)


def test_nusmv_syncrprocesstype_constructor_exists():
    assert callable(nuSMV_SyncrProcessType.__init__)


def test_nusmv_syncrprocesstype_constructor_args():
    sig = inspect.signature(nuSMV_SyncrProcessType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_asyncrprocesstype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_AsyncrProcessType)


def test_nusmv_asyncrprocesstype_constructor_exists():
    assert callable(nuSMV_AsyncrProcessType.__init__)


def test_nusmv_asyncrprocesstype_constructor_args():
    sig = inspect.signature(nuSMV_AsyncrProcessType.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_enumtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_EnumType)


def test_nusmv_enumtype_constructor_exists():
    assert callable(nuSMV_EnumType.__init__)


def test_nusmv_enumtype_constructor_args():
    sig = inspect.signature(nuSMV_EnumType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_wordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_WordType)


def test_nusmv_wordtype_constructor_exists():
    assert callable(nuSMV_WordType.__init__)


def test_nusmv_wordtype_constructor_args():
    sig = inspect.signature(nuSMV_WordType.__init__)
    params = list(sig.parameters.keys())
    assert "wordNumber" in params, "Missing parameter 'wordNumber'"

def test_nusmv_wordtype_has_wordNumber():
    assert hasattr(nuSMV_WordType, "wordNumber")
    descriptor = None
    for klass in nuSMV_WordType.__mro__:
        if "wordNumber" in klass.__dict__:
            descriptor = klass.__dict__["wordNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_arraytype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ArrayType)


def test_nusmv_arraytype_constructor_exists():
    assert callable(nuSMV_ArrayType.__init__)


def test_nusmv_arraytype_constructor_args():
    sig = inspect.signature(nuSMV_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_nusmv_arraytype_has_lowerBound():
    assert hasattr(nuSMV_ArrayType, "lowerBound")
    descriptor = None
    for klass in nuSMV_ArrayType.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_arraytype_has_upperBound():
    assert hasattr(nuSMV_ArrayType, "upperBound")
    descriptor = None
    for klass in nuSMV_ArrayType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_signedwordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SignedWordType)


def test_nusmv_signedwordtype_constructor_exists():
    assert callable(nuSMV_SignedWordType.__init__)


def test_nusmv_signedwordtype_constructor_args():
    sig = inspect.signature(nuSMV_SignedWordType.__init__)
    params = list(sig.parameters.keys())
    assert "signedNumber" in params, "Missing parameter 'signedNumber'"

def test_nusmv_signedwordtype_has_signedNumber():
    assert hasattr(nuSMV_SignedWordType, "signedNumber")
    descriptor = None
    for klass in nuSMV_SignedWordType.__mro__:
        if "signedNumber" in klass.__dict__:
            descriptor = klass.__dict__["signedNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_unsignedwordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_UnsignedWordType)


def test_nusmv_unsignedwordtype_constructor_exists():
    assert callable(nuSMV_UnsignedWordType.__init__)


def test_nusmv_unsignedwordtype_constructor_args():
    sig = inspect.signature(nuSMV_UnsignedWordType.__init__)
    params = list(sig.parameters.keys())
    assert "uWordNumber" in params, "Missing parameter 'uWordNumber'"

def test_nusmv_unsignedwordtype_has_uWordNumber():
    assert hasattr(nuSMV_UnsignedWordType, "uWordNumber")
    descriptor = None
    for klass in nuSMV_UnsignedWordType.__mro__:
        if "uWordNumber" in klass.__dict__:
            descriptor = klass.__dict__["uWordNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_intervaltype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_IntervalType)


def test_nusmv_intervaltype_constructor_exists():
    assert callable(nuSMV_IntervalType.__init__)


def test_nusmv_intervaltype_constructor_args():
    sig = inspect.signature(nuSMV_IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "low" in params, "Missing parameter 'low'"
    assert "high" in params, "Missing parameter 'high'"

def test_nusmv_intervaltype_has_low():
    assert hasattr(nuSMV_IntervalType, "low")
    descriptor = None
    for klass in nuSMV_IntervalType.__mro__:
        if "low" in klass.__dict__:
            descriptor = klass.__dict__["low"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_intervaltype_has_high():
    assert hasattr(nuSMV_IntervalType, "high")
    descriptor = None
    for klass in nuSMV_IntervalType.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_booleantype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_BooleanType)


def test_nusmv_booleantype_constructor_exists():
    assert callable(nuSMV_BooleanType.__init__)


def test_nusmv_booleantype_constructor_args():
    sig = inspect.signature(nuSMV_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_rtctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_RTCTLExpression)


def test_nusmv_rtctlexpression_constructor_exists():
    assert callable(nuSMV_RTCTLExpression.__init__)


def test_nusmv_rtctlexpression_constructor_args():
    sig = inspect.signature(nuSMV_RTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_rangeexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_RangeExpression)


def test_nusmv_rangeexpression_constructor_exists():
    assert callable(nuSMV_RangeExpression.__init__)


def test_nusmv_rangeexpression_constructor_args():
    sig = inspect.signature(nuSMV_RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_nusmv_rangeexpression_has_upper():
    assert hasattr(nuSMV_RangeExpression, "upper")
    descriptor = None
    for klass in nuSMV_RangeExpression.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_rangeexpression_has_lower():
    assert hasattr(nuSMV_RangeExpression, "lower")
    descriptor = None
    for klass in nuSMV_RangeExpression.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_casesimpleassignementexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_CaseSimpleAssignementExpression)


def test_nusmv_casesimpleassignementexpression_constructor_exists():
    assert callable(nuSMV_CaseSimpleAssignementExpression.__init__)


def test_nusmv_casesimpleassignementexpression_constructor_args():
    sig = inspect.signature(nuSMV_CaseSimpleAssignementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(SimpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(SimpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_setelementexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SetElementExpression)


def test_nusmv_setelementexpression_constructor_exists():
    assert callable(nuSMV_SetElementExpression.__init__)


def test_nusmv_setelementexpression_constructor_args():
    sig = inspect.signature(nuSMV_SetElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_valueexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ValueExpression)


def test_nusmv_valueexpression_constructor_exists():
    assert callable(nuSMV_ValueExpression.__init__)


def test_nusmv_valueexpression_constructor_args():
    sig = inspect.signature(nuSMV_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nusmv_valueexpression_has_value():
    assert hasattr(nuSMV_ValueExpression, "value")
    descriptor = None
    for klass in nuSMV_ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_UnaryExpression)


def test_nusmv_unaryexpression_constructor_exists():
    assert callable(nuSMV_UnaryExpression.__init__)


def test_nusmv_unaryexpression_constructor_args():
    sig = inspect.signature(nuSMV_UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_nusmv_unaryexpression_has_operator():
    assert hasattr(nuSMV_UnaryExpression, "operator")
    descriptor = None
    for klass in nuSMV_UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_untilctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_UntilCTLexpression)


def test_nusmv_untilctlexpression_constructor_exists():
    assert callable(nuSMV_UntilCTLexpression.__init__)


def test_nusmv_untilctlexpression_constructor_args():
    sig = inspect.signature(nuSMV_UntilCTLexpression.__init__)
    params = list(sig.parameters.keys())
    assert "ea" in params, "Missing parameter 'ea'"

def test_nusmv_untilctlexpression_has_ea():
    assert hasattr(nuSMV_UntilCTLexpression, "ea")
    descriptor = None
    for klass in nuSMV_UntilCTLexpression.__mro__:
        if "ea" in klass.__dict__:
            descriptor = klass.__dict__["ea"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_setvalueparameter_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SetValueParameter)


def test_nusmv_setvalueparameter_constructor_exists():
    assert callable(nuSMV_SetValueParameter.__init__)


def test_nusmv_setvalueparameter_constructor_args():
    sig = inspect.signature(nuSMV_SetValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_not_is_not_abstract():
    assert not inspect.isabstract(nuSMV_Not)


def test_nusmv_not_constructor_exists():
    assert callable(nuSMV_Not.__init__)


def test_nusmv_not_constructor_args():
    sig = inspect.signature(nuSMV_Not.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_unaryfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_UnaryFunctionExpression)


def test_nusmv_unaryfunctionexpression_constructor_exists():
    assert callable(nuSMV_UnaryFunctionExpression.__init__)


def test_nusmv_unaryfunctionexpression_constructor_args():
    sig = inspect.signature(nuSMV_UnaryFunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_nusmv_unaryfunctionexpression_has_function():
    assert hasattr(nuSMV_UnaryFunctionExpression, "function")
    descriptor = None
    for klass in nuSMV_UnaryFunctionExpression.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_intervalexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_IntervalExpression)


def test_nusmv_intervalexpression_constructor_exists():
    assert callable(nuSMV_IntervalExpression.__init__)


def test_nusmv_intervalexpression_constructor_args():
    sig = inspect.signature(nuSMV_IntervalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_nusmv_intervalexpression_has_lowerBound():
    assert hasattr(nuSMV_IntervalExpression, "lowerBound")
    descriptor = None
    for klass in nuSMV_IntervalExpression.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_intervalexpression_has_upperBound():
    assert hasattr(nuSMV_IntervalExpression, "upperBound")
    descriptor = None
    for klass in nuSMV_IntervalExpression.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_wordexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_WordExpression)


def test_nusmv_wordexpression_constructor_exists():
    assert callable(nuSMV_WordExpression.__init__)


def test_nusmv_wordexpression_constructor_args():
    sig = inspect.signature(nuSMV_WordExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nusmv_wordexpression_has_value():
    assert hasattr(nuSMV_WordExpression, "value")
    descriptor = None
    for klass in nuSMV_WordExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_setexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SetExpression)


def test_nusmv_setexpression_constructor_exists():
    assert callable(nuSMV_SetExpression.__init__)


def test_nusmv_setexpression_constructor_args():
    sig = inspect.signature(nuSMV_SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_parsexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ParsExpression)


def test_nusmv_parsexpression_constructor_exists():
    assert callable(nuSMV_ParsExpression.__init__)


def test_nusmv_parsexpression_constructor_args():
    sig = inspect.signature(nuSMV_ParsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNext" in params, "Missing parameter 'isNext'"

def test_nusmv_parsexpression_has_isNext():
    assert hasattr(nuSMV_ParsExpression, "isNext")
    descriptor = None
    for klass in nuSMV_ParsExpression.__mro__:
        if "isNext" in klass.__dict__:
            descriptor = klass.__dict__["isNext"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_var_is_not_abstract():
    assert not inspect.isabstract(nuSMV_Var)


def test_nusmv_var_constructor_exists():
    assert callable(nuSMV_Var.__init__)


def test_nusmv_var_constructor_args():
    sig = inspect.signature(nuSMV_Var.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_BinaryExpression)


def test_nusmv_binaryexpression_constructor_exists():
    assert callable(nuSMV_BinaryExpression.__init__)


def test_nusmv_binaryexpression_constructor_args():
    sig = inspect.signature(nuSMV_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "op" in params, "Missing parameter 'op'"

def test_nusmv_binaryexpression_has_operator():
    assert hasattr(nuSMV_BinaryExpression, "operator")
    descriptor = None
    for klass in nuSMV_BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_binaryexpression_has_op():
    assert hasattr(nuSMV_BinaryExpression, "op")
    descriptor = None
    for klass in nuSMV_BinaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_casesimpleexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_CaseSimpleExpression)


def test_nusmv_casesimpleexpression_constructor_exists():
    assert callable(nuSMV_CaseSimpleExpression.__init__)


def test_nusmv_casesimpleexpression_constructor_args():
    sig = inspect.signature(nuSMV_CaseSimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_val_is_not_abstract():
    assert not inspect.isabstract(nuSMV_Val)


def test_nusmv_val_constructor_exists():
    assert callable(nuSMV_Val.__init__)


def test_nusmv_val_constructor_args():
    sig = inspect.signature(nuSMV_Val.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv_val_has_num():
    assert hasattr(nuSMV_Val, "num")
    descriptor = None
    for klass in nuSMV_Val.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_val_has_name():
    assert hasattr(nuSMV_Val, "name")
    descriptor = None
    for klass in nuSMV_Val.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_simpletype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SimpleType)


def test_nusmv_simpletype_constructor_exists():
    assert callable(nuSMV_SimpleType.__init__)


def test_nusmv_simpletype_constructor_args():
    sig = inspect.signature(nuSMV_SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_moduletype_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ModuleType)


def test_nusmv_moduletype_constructor_exists():
    assert callable(nuSMV_ModuleType.__init__)


def test_nusmv_moduletype_constructor_args():
    sig = inspect.signature(nuSMV_ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_ltlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_LTLExpression)


def test_nusmv_ltlexpression_constructor_exists():
    assert callable(nuSMV_LTLExpression.__init__)


def test_nusmv_ltlexpression_constructor_args():
    sig = inspect.signature(nuSMV_LTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_ctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_CTLExpression)


def test_nusmv_ctlexpression_constructor_exists():
    assert callable(nuSMV_CTLExpression.__init__)


def test_nusmv_ctlexpression_constructor_args():
    sig = inspect.signature(nuSMV_CTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(FairnessConstraint)


def test_fairnessconstraint_constructor_exists():
    assert callable(FairnessConstraint.__init__)


def test_fairnessconstraint_constructor_args():
    sig = inspect.signature(FairnessConstraint.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_compassionexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_CompassionExpression)


def test_nusmv_compassionexpression_constructor_exists():
    assert callable(nuSMV_CompassionExpression.__init__)


def test_nusmv_compassionexpression_constructor_args():
    sig = inspect.signature(nuSMV_CompassionExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_justiceexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_JusticeExpression)


def test_nusmv_justiceexpression_constructor_exists():
    assert callable(nuSMV_JusticeExpression.__init__)


def test_nusmv_justiceexpression_constructor_args():
    sig = inspect.signature(nuSMV_JusticeExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_fairnessexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_FairnessExpression)


def test_nusmv_fairnessexpression_constructor_exists():
    assert callable(nuSMV_FairnessExpression.__init__)


def test_nusmv_fairnessexpression_constructor_args():
    sig = inspect.signature(nuSMV_FairnessExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_nextexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_NextExpression)


def test_nusmv_nextexpression_constructor_exists():
    assert callable(nuSMV_NextExpression.__init__)


def test_nusmv_nextexpression_constructor_args():
    sig = inspect.signature(nuSMV_NextExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignbody_is_not_abstract():
    assert not inspect.isabstract(AssignBody)


def test_assignbody_constructor_exists():
    assert callable(AssignBody.__init__)


def test_assignbody_constructor_args():
    sig = inspect.signature(AssignBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_initbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV_InitBody)


def test_nusmv_initbody_constructor_exists():
    assert callable(nuSMV_InitBody.__init__)


def test_nusmv_initbody_constructor_args():
    sig = inspect.signature(nuSMV_InitBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_nextbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV_NextBody)


def test_nusmv_nextbody_constructor_exists():
    assert callable(nuSMV_NextBody.__init__)


def test_nusmv_nextbody_constructor_args():
    sig = inspect.signature(nuSMV_NextBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_varbodyassign_is_not_abstract():
    assert not inspect.isabstract(nuSMV_VarBodyAssign)


def test_nusmv_varbodyassign_constructor_exists():
    assert callable(nuSMV_VarBodyAssign.__init__)


def test_nusmv_varbodyassign_constructor_args():
    sig = inspect.signature(nuSMV_VarBodyAssign.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_eobject_is_not_abstract():
    assert not inspect.isabstract(nuSMV_EObject)


def test_nusmv_eobject_constructor_exists():
    assert callable(nuSMV_EObject.__init__)


def test_nusmv_eobject_constructor_args():
    sig = inspect.signature(nuSMV_EObject.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_assignbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV_AssignBody)


def test_nusmv_assignbody_constructor_exists():
    assert callable(nuSMV_AssignBody.__init__)


def test_nusmv_assignbody_constructor_args():
    sig = inspect.signature(nuSMV_AssignBody.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_assignbody_has_array():
    assert hasattr(nuSMV_AssignBody, "array")
    descriptor = None
    for klass in nuSMV_AssignBody.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_assignbody_has_semicolon():
    assert hasattr(nuSMV_AssignBody, "semicolon")
    descriptor = None
    for klass in nuSMV_AssignBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV_SimpleExpression)


def test_nusmv_simpleexpression_constructor_exists():
    assert callable(nuSMV_SimpleExpression.__init__)


def test_nusmv_simpleexpression_constructor_args():
    sig = inspect.signature(nuSMV_SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_definebody_is_not_abstract():
    assert not inspect.isabstract(nuSMV_DefineBody)


def test_nusmv_definebody_constructor_exists():
    assert callable(nuSMV_DefineBody.__init__)


def test_nusmv_definebody_constructor_args():
    sig = inspect.signature(nuSMV_DefineBody.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"
    assert "var" in params, "Missing parameter 'var'"

def test_nusmv_definebody_has_semicolon():
    assert hasattr(nuSMV_DefineBody, "semicolon")
    descriptor = None
    for klass in nuSMV_DefineBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_definebody_has_var():
    assert hasattr(nuSMV_DefineBody, "var")
    descriptor = None
    for klass in nuSMV_DefineBody.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_type_is_not_abstract():
    assert not inspect.isabstract(nuSMV_Type)


def test_nusmv_type_constructor_exists():
    assert callable(nuSMV_Type.__init__)


def test_nusmv_type_constructor_args():
    sig = inspect.signature(nuSMV_Type.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_varbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV_VarBody)


def test_nusmv_varbody_constructor_exists():
    assert callable(nuSMV_VarBody.__init__)


def test_nusmv_varbody_constructor_args():
    sig = inspect.signature(nuSMV_VarBody.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv_varbody_has_semicolon():
    assert hasattr(nuSMV_VarBody, "semicolon")
    descriptor = None
    for klass in nuSMV_VarBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_varbody_has_name():
    assert hasattr(nuSMV_VarBody, "name")
    descriptor = None
    for klass in nuSMV_VarBody.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_transconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV_TransConstraint)


def test_nusmv_transconstraint_constructor_exists():
    assert callable(nuSMV_TransConstraint.__init__)


def test_nusmv_transconstraint_constructor_args():
    sig = inspect.signature(nuSMV_TransConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_transconstraint_has_semicolon():
    assert hasattr(nuSMV_TransConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV_TransConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_constantsdeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ConstantsDeclaration)


def test_nusmv_constantsdeclaration_constructor_exists():
    assert callable(nuSMV_ConstantsDeclaration.__init__)


def test_nusmv_constantsdeclaration_constructor_args():
    sig = inspect.signature(nuSMV_ConstantsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constants" in params, "Missing parameter 'constants'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_constantsdeclaration_has_constants():
    assert hasattr(nuSMV_ConstantsDeclaration, "constants")
    descriptor = None
    for klass in nuSMV_ConstantsDeclaration.__mro__:
        if "constants" in klass.__dict__:
            descriptor = klass.__dict__["constants"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_constantsdeclaration_has_semicolon():
    assert hasattr(nuSMV_ConstantsDeclaration, "semicolon")
    descriptor = None
    for klass in nuSMV_ConstantsDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV_FairnessConstraint)


def test_nusmv_fairnessconstraint_constructor_exists():
    assert callable(nuSMV_FairnessConstraint.__init__)


def test_nusmv_fairnessconstraint_constructor_args():
    sig = inspect.signature(nuSMV_FairnessConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_fairnessconstraint_has_semicolon():
    assert hasattr(nuSMV_FairnessConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV_FairnessConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_ivariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_IVariableDeclaration)


def test_nusmv_ivariabledeclaration_constructor_exists():
    assert callable(nuSMV_IVariableDeclaration.__init__)


def test_nusmv_ivariabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV_IVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_ltlspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV_LtlSpecification)


def test_nusmv_ltlspecification_constructor_exists():
    assert callable(nuSMV_LtlSpecification.__init__)


def test_nusmv_ltlspecification_constructor_args():
    sig = inspect.signature(nuSMV_LtlSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameId" in params, "Missing parameter 'nameId'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_ltlspecification_has_name():
    assert hasattr(nuSMV_LtlSpecification, "name")
    descriptor = None
    for klass in nuSMV_LtlSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_ltlspecification_has_nameId():
    assert hasattr(nuSMV_LtlSpecification, "nameId")
    descriptor = None
    for klass in nuSMV_LtlSpecification.__mro__:
        if "nameId" in klass.__dict__:
            descriptor = klass.__dict__["nameId"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_ltlspecification_has_semicolon():
    assert hasattr(nuSMV_LtlSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV_LtlSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_frozenvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_FrozenVariableDeclaration)


def test_nusmv_frozenvariabledeclaration_constructor_exists():
    assert callable(nuSMV_FrozenVariableDeclaration.__init__)


def test_nusmv_frozenvariabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV_FrozenVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_invarconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV_InvarConstraint)


def test_nusmv_invarconstraint_constructor_exists():
    assert callable(nuSMV_InvarConstraint.__init__)


def test_nusmv_invarconstraint_constructor_args():
    sig = inspect.signature(nuSMV_InvarConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_invarconstraint_has_semicolon():
    assert hasattr(nuSMV_InvarConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV_InvarConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_initconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV_InitConstraint)


def test_nusmv_initconstraint_constructor_exists():
    assert callable(nuSMV_InitConstraint.__init__)


def test_nusmv_initconstraint_constructor_args():
    sig = inspect.signature(nuSMV_InitConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_initconstraint_has_semicolon():
    assert hasattr(nuSMV_InitConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV_InitConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_computespecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ComputeSpecification)


def test_nusmv_computespecification_constructor_exists():
    assert callable(nuSMV_ComputeSpecification.__init__)


def test_nusmv_computespecification_constructor_args():
    sig = inspect.signature(nuSMV_ComputeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "minMax" in params, "Missing parameter 'minMax'"

def test_nusmv_computespecification_has_minMax():
    assert hasattr(nuSMV_ComputeSpecification, "minMax")
    descriptor = None
    for klass in nuSMV_ComputeSpecification.__mro__:
        if "minMax" in klass.__dict__:
            descriptor = klass.__dict__["minMax"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_assignconstraintelement_is_not_abstract():
    assert not inspect.isabstract(nuSMV_AssignConstraintElement)


def test_nusmv_assignconstraintelement_constructor_exists():
    assert callable(nuSMV_AssignConstraintElement.__init__)


def test_nusmv_assignconstraintelement_constructor_args():
    sig = inspect.signature(nuSMV_AssignConstraintElement.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_nusmv_assignconstraintelement_has_assign():
    assert hasattr(nuSMV_AssignConstraintElement, "assign")
    descriptor = None
    for klass in nuSMV_AssignConstraintElement.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_definedeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_DefineDeclaration)


def test_nusmv_definedeclaration_constructor_exists():
    assert callable(nuSMV_DefineDeclaration.__init__)


def test_nusmv_definedeclaration_constructor_args():
    sig = inspect.signature(nuSMV_DefineDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "define" in params, "Missing parameter 'define'"

def test_nusmv_definedeclaration_has_define():
    assert hasattr(nuSMV_DefineDeclaration, "define")
    descriptor = None
    for klass in nuSMV_DefineDeclaration.__mro__:
        if "define" in klass.__dict__:
            descriptor = klass.__dict__["define"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_invarspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV_InvarSpecification)


def test_nusmv_invarspecification_constructor_exists():
    assert callable(nuSMV_InvarSpecification.__init__)


def test_nusmv_invarspecification_constructor_args():
    sig = inspect.signature(nuSMV_InvarSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv_invarspecification_has_name():
    assert hasattr(nuSMV_InvarSpecification, "name")
    descriptor = None
    for klass in nuSMV_InvarSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_invarspecification_has_semicolon():
    assert hasattr(nuSMV_InvarSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV_InvarSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_ctlspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV_CtlSpecification)


def test_nusmv_ctlspecification_constructor_exists():
    assert callable(nuSMV_CtlSpecification.__init__)


def test_nusmv_ctlspecification_constructor_args():
    sig = inspect.signature(nuSMV_CtlSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"
    assert "specKeyWord" in params, "Missing parameter 'specKeyWord'"
    assert "nameKeyWord" in params, "Missing parameter 'nameKeyWord'"

def test_nusmv_ctlspecification_has_name():
    assert hasattr(nuSMV_CtlSpecification, "name")
    descriptor = None
    for klass in nuSMV_CtlSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_ctlspecification_has_semicolon():
    assert hasattr(nuSMV_CtlSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV_CtlSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_ctlspecification_has_specKeyWord():
    assert hasattr(nuSMV_CtlSpecification, "specKeyWord")
    descriptor = None
    for klass in nuSMV_CtlSpecification.__mro__:
        if "specKeyWord" in klass.__dict__:
            descriptor = klass.__dict__["specKeyWord"]
            break
    assert isinstance(descriptor, property)

def test_nusmv_ctlspecification_has_nameKeyWord():
    assert hasattr(nuSMV_CtlSpecification, "nameKeyWord")
    descriptor = None
    for klass in nuSMV_CtlSpecification.__mro__:
        if "nameKeyWord" in klass.__dict__:
            descriptor = klass.__dict__["nameKeyWord"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_isadeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_IsaDeclaration)


def test_nusmv_isadeclaration_constructor_exists():
    assert callable(nuSMV_IsaDeclaration.__init__)


def test_nusmv_isadeclaration_constructor_args():
    sig = inspect.signature(nuSMV_IsaDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_nusmv_isadeclaration_has_id():
    assert hasattr(nuSMV_IsaDeclaration, "id")
    descriptor = None
    for klass in nuSMV_IsaDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV_VariableDeclaration)


def test_nusmv_variabledeclaration_constructor_exists():
    assert callable(nuSMV_VariableDeclaration.__init__)


def test_nusmv_variabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_moduleelement_is_not_abstract():
    assert not inspect.isabstract(nuSMV_ModuleElement)


def test_nusmv_moduleelement_constructor_exists():
    assert callable(nuSMV_ModuleElement.__init__)


def test_nusmv_moduleelement_constructor_args():
    sig = inspect.signature(nuSMV_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_nusmv_formalparameter_is_not_abstract():
    assert not inspect.isabstract(nuSMV_FormalParameter)


def test_nusmv_formalparameter_constructor_exists():
    assert callable(nuSMV_FormalParameter.__init__)


def test_nusmv_formalparameter_constructor_args():
    sig = inspect.signature(nuSMV_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv_formalparameter_has_name():
    assert hasattr(nuSMV_FormalParameter, "name")
    descriptor = None
    for klass in nuSMV_FormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_module_is_not_abstract():
    assert not inspect.isabstract(nuSMV_Module)


def test_nusmv_module_constructor_exists():
    assert callable(nuSMV_Module.__init__)


def test_nusmv_module_constructor_args():
    sig = inspect.signature(nuSMV_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv_module_has_name():
    assert hasattr(nuSMV_Module, "name")
    descriptor = None
    for klass in nuSMV_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nusmv_nusmvmodel_is_not_abstract():
    assert not inspect.isabstract(nuSMV_NuSmvModel)


def test_nusmv_nusmvmodel_constructor_exists():
    assert callable(nuSMV_NuSmvModel.__init__)


def test_nusmv_nusmvmodel_constructor_args():
    sig = inspect.signature(nuSMV_NuSmvModel.__init__)
    params = list(sig.parameters.keys())

def test_operators_exists():
    # Check that the Enumeration exists
    assert operators is not None

def test_operators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in operators]
    expected_literals = [
        "and_",
        "or_",
        "v",
        "ge",
        "xor",
        "equal",
        "g",
        "u",
        "t",
        "le",
        "dis",
        "s",
        "l",
        "xnor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in operators"


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
ModuleType_strategy = st.builds(
    ModuleType,
)
RTCTLExpression_strategy = st.builds(
    RTCTLExpression,
)
nuSMV_UnaryRTCTLExpression_strategy = st.builds(
    nuSMV_UnaryRTCTLExpression,
    unary=
        safe_text
)
nuSMV_SingleRTCTLExpression_strategy = st.builds(
    nuSMV_SingleRTCTLExpression,
)
nuSMV_SyncrProcessType_strategy = st.builds(
    nuSMV_SyncrProcessType,
)
nuSMV_AsyncrProcessType_strategy = st.builds(
    nuSMV_AsyncrProcessType,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
nuSMV_EnumType_strategy = st.builds(
    nuSMV_EnumType,
)
nuSMV_WordType_strategy = st.builds(
    nuSMV_WordType,
    wordNumber=
        safe_text
)
nuSMV_ArrayType_strategy = st.builds(
    nuSMV_ArrayType,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
nuSMV_SignedWordType_strategy = st.builds(
    nuSMV_SignedWordType,
    signedNumber=
        safe_text
)
nuSMV_UnsignedWordType_strategy = st.builds(
    nuSMV_UnsignedWordType,
    uWordNumber=
        safe_text
)
nuSMV_IntervalType_strategy = st.builds(
    nuSMV_IntervalType,
    low=
        safe_text,
    high=
        safe_text
)
nuSMV_BooleanType_strategy = st.builds(
    nuSMV_BooleanType,
)
nuSMV_RTCTLExpression_strategy = st.builds(
    nuSMV_RTCTLExpression,
)
nuSMV_RangeExpression_strategy = st.builds(
    nuSMV_RangeExpression,
    upper=
        safe_text,
    lower=
        safe_text
)
nuSMV_CaseSimpleAssignementExpression_strategy = st.builds(
    nuSMV_CaseSimpleAssignementExpression,
)
SimpleExpression_strategy = st.builds(
    SimpleExpression,
)
nuSMV_SetElementExpression_strategy = st.builds(
    nuSMV_SetElementExpression,
)
nuSMV_ValueExpression_strategy = st.builds(
    nuSMV_ValueExpression,
    value=
        safe_text
)
nuSMV_UnaryExpression_strategy = st.builds(
    nuSMV_UnaryExpression,
    operator=
        safe_text
)
nuSMV_UntilCTLexpression_strategy = st.builds(
    nuSMV_UntilCTLexpression,
    ea=
        safe_text
)
nuSMV_SetValueParameter_strategy = st.builds(
    nuSMV_SetValueParameter,
)
nuSMV_Not_strategy = st.builds(
    nuSMV_Not,
)
nuSMV_UnaryFunctionExpression_strategy = st.builds(
    nuSMV_UnaryFunctionExpression,
    function=
        safe_text
)
nuSMV_IntervalExpression_strategy = st.builds(
    nuSMV_IntervalExpression,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
nuSMV_WordExpression_strategy = st.builds(
    nuSMV_WordExpression,
    value=
        safe_text
)
nuSMV_SetExpression_strategy = st.builds(
    nuSMV_SetExpression,
)
nuSMV_ParsExpression_strategy = st.builds(
    nuSMV_ParsExpression,
    isNext=
        st.booleans()
)
nuSMV_Var_strategy = st.builds(
    nuSMV_Var,
)
nuSMV_BinaryExpression_strategy = st.builds(
    nuSMV_BinaryExpression,
    operator=
        safe_text,
    op=
        safe_text
)
nuSMV_CaseSimpleExpression_strategy = st.builds(
    nuSMV_CaseSimpleExpression,
)
nuSMV_Val_strategy = st.builds(
    nuSMV_Val,
    num=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
nuSMV_SimpleType_strategy = st.builds(
    nuSMV_SimpleType,
)
nuSMV_ModuleType_strategy = st.builds(
    nuSMV_ModuleType,
)
nuSMV_LTLExpression_strategy = st.builds(
    nuSMV_LTLExpression,
)
nuSMV_CTLExpression_strategy = st.builds(
    nuSMV_CTLExpression,
)
FairnessConstraint_strategy = st.builds(
    FairnessConstraint,
)
nuSMV_CompassionExpression_strategy = st.builds(
    nuSMV_CompassionExpression,
)
nuSMV_JusticeExpression_strategy = st.builds(
    nuSMV_JusticeExpression,
)
nuSMV_FairnessExpression_strategy = st.builds(
    nuSMV_FairnessExpression,
)
nuSMV_NextExpression_strategy = st.builds(
    nuSMV_NextExpression,
)
AssignBody_strategy = st.builds(
    AssignBody,
)
nuSMV_InitBody_strategy = st.builds(
    nuSMV_InitBody,
)
nuSMV_NextBody_strategy = st.builds(
    nuSMV_NextBody,
)
nuSMV_VarBodyAssign_strategy = st.builds(
    nuSMV_VarBodyAssign,
)
nuSMV_EObject_strategy = st.builds(
    nuSMV_EObject,
)
nuSMV_AssignBody_strategy = st.builds(
    nuSMV_AssignBody,
    array=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV_SimpleExpression_strategy = st.builds(
    nuSMV_SimpleExpression,
)
nuSMV_DefineBody_strategy = st.builds(
    nuSMV_DefineBody,
    semicolon=
        st.booleans(),
    var=
        safe_text
)
nuSMV_Type_strategy = st.builds(
    nuSMV_Type,
)
nuSMV_VarBody_strategy = st.builds(
    nuSMV_VarBody,
    semicolon=
        st.booleans(),
    name=
        safe_text
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
nuSMV_TransConstraint_strategy = st.builds(
    nuSMV_TransConstraint,
    semicolon=
        st.booleans()
)
nuSMV_ConstantsDeclaration_strategy = st.builds(
    nuSMV_ConstantsDeclaration,
    constants=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV_FairnessConstraint_strategy = st.builds(
    nuSMV_FairnessConstraint,
    semicolon=
        st.booleans()
)
nuSMV_IVariableDeclaration_strategy = st.builds(
    nuSMV_IVariableDeclaration,
)
nuSMV_LtlSpecification_strategy = st.builds(
    nuSMV_LtlSpecification,
    name=
        safe_text,
    nameId=
        st.booleans(),
    semicolon=
        st.booleans()
)
nuSMV_FrozenVariableDeclaration_strategy = st.builds(
    nuSMV_FrozenVariableDeclaration,
)
nuSMV_InvarConstraint_strategy = st.builds(
    nuSMV_InvarConstraint,
    semicolon=
        st.booleans()
)
nuSMV_InitConstraint_strategy = st.builds(
    nuSMV_InitConstraint,
    semicolon=
        st.booleans()
)
nuSMV_ComputeSpecification_strategy = st.builds(
    nuSMV_ComputeSpecification,
    minMax=
        safe_text
)
nuSMV_AssignConstraintElement_strategy = st.builds(
    nuSMV_AssignConstraintElement,
    assign=
        safe_text
)
nuSMV_DefineDeclaration_strategy = st.builds(
    nuSMV_DefineDeclaration,
    define=
        safe_text
)
nuSMV_InvarSpecification_strategy = st.builds(
    nuSMV_InvarSpecification,
    name=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV_CtlSpecification_strategy = st.builds(
    nuSMV_CtlSpecification,
    name=
        safe_text,
    semicolon=
        st.booleans(),
    specKeyWord=
        safe_text,
    nameKeyWord=
        st.booleans()
)
nuSMV_IsaDeclaration_strategy = st.builds(
    nuSMV_IsaDeclaration,
    id=
        safe_text
)
nuSMV_VariableDeclaration_strategy = st.builds(
    nuSMV_VariableDeclaration,
)
nuSMV_ModuleElement_strategy = st.builds(
    nuSMV_ModuleElement,
)
nuSMV_FormalParameter_strategy = st.builds(
    nuSMV_FormalParameter,
    name=
        safe_text
)
nuSMV_Module_strategy = st.builds(
    nuSMV_Module,
    name=
        safe_text
)
nuSMV_NuSmvModel_strategy = st.builds(
    nuSMV_NuSmvModel,
)

@given(instance=ModuleType_strategy)
@settings(max_examples=50)
def test_moduletype_instantiation(instance):
    assert isinstance(instance, ModuleType)

@given(instance=RTCTLExpression_strategy)
@settings(max_examples=50)
def test_rtctlexpression_instantiation(instance):
    assert isinstance(instance, RTCTLExpression)

@given(instance=nuSMV_UnaryRTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv_unaryrtctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_UnaryRTCTLExpression)



@given(instance=nuSMV_UnaryRTCTLExpression_strategy)
def test_nusmv_unaryrtctlexpression_unary_setter(instance):
    original = instance.unary
    instance.unary = original
    assert instance.unary == original

@given(instance=nuSMV_SingleRTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv_singlertctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_SingleRTCTLExpression)

@given(instance=nuSMV_SyncrProcessType_strategy)
@settings(max_examples=50)
def test_nusmv_syncrprocesstype_instantiation(instance):
    assert isinstance(instance, nuSMV_SyncrProcessType)

@given(instance=nuSMV_AsyncrProcessType_strategy)
@settings(max_examples=50)
def test_nusmv_asyncrprocesstype_instantiation(instance):
    assert isinstance(instance, nuSMV_AsyncrProcessType)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=nuSMV_EnumType_strategy)
@settings(max_examples=50)
def test_nusmv_enumtype_instantiation(instance):
    assert isinstance(instance, nuSMV_EnumType)

@given(instance=nuSMV_WordType_strategy)
@settings(max_examples=50)
def test_nusmv_wordtype_instantiation(instance):
    assert isinstance(instance, nuSMV_WordType)



@given(instance=nuSMV_WordType_strategy)
def test_nusmv_wordtype_wordNumber_setter(instance):
    original = instance.wordNumber
    instance.wordNumber = original
    assert instance.wordNumber == original

@given(instance=nuSMV_ArrayType_strategy)
@settings(max_examples=50)
def test_nusmv_arraytype_instantiation(instance):
    assert isinstance(instance, nuSMV_ArrayType)



@given(instance=nuSMV_ArrayType_strategy)
def test_nusmv_arraytype_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=nuSMV_ArrayType_strategy)
def test_nusmv_arraytype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=nuSMV_SignedWordType_strategy)
@settings(max_examples=50)
def test_nusmv_signedwordtype_instantiation(instance):
    assert isinstance(instance, nuSMV_SignedWordType)



@given(instance=nuSMV_SignedWordType_strategy)
def test_nusmv_signedwordtype_signedNumber_setter(instance):
    original = instance.signedNumber
    instance.signedNumber = original
    assert instance.signedNumber == original

@given(instance=nuSMV_UnsignedWordType_strategy)
@settings(max_examples=50)
def test_nusmv_unsignedwordtype_instantiation(instance):
    assert isinstance(instance, nuSMV_UnsignedWordType)



@given(instance=nuSMV_UnsignedWordType_strategy)
def test_nusmv_unsignedwordtype_uWordNumber_setter(instance):
    original = instance.uWordNumber
    instance.uWordNumber = original
    assert instance.uWordNumber == original

@given(instance=nuSMV_IntervalType_strategy)
@settings(max_examples=50)
def test_nusmv_intervaltype_instantiation(instance):
    assert isinstance(instance, nuSMV_IntervalType)



@given(instance=nuSMV_IntervalType_strategy)
def test_nusmv_intervaltype_low_setter(instance):
    original = instance.low
    instance.low = original
    assert instance.low == original



@given(instance=nuSMV_IntervalType_strategy)
def test_nusmv_intervaltype_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original

@given(instance=nuSMV_BooleanType_strategy)
@settings(max_examples=50)
def test_nusmv_booleantype_instantiation(instance):
    assert isinstance(instance, nuSMV_BooleanType)

@given(instance=nuSMV_RTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv_rtctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_RTCTLExpression)

@given(instance=nuSMV_RangeExpression_strategy)
@settings(max_examples=50)
def test_nusmv_rangeexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_RangeExpression)



@given(instance=nuSMV_RangeExpression_strategy)
def test_nusmv_rangeexpression_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=nuSMV_RangeExpression_strategy)
def test_nusmv_rangeexpression_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=nuSMV_CaseSimpleAssignementExpression_strategy)
@settings(max_examples=50)
def test_nusmv_casesimpleassignementexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_CaseSimpleAssignementExpression)

@given(instance=SimpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, SimpleExpression)

@given(instance=nuSMV_SetElementExpression_strategy)
@settings(max_examples=50)
def test_nusmv_setelementexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_SetElementExpression)

@given(instance=nuSMV_ValueExpression_strategy)
@settings(max_examples=50)
def test_nusmv_valueexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_ValueExpression)



@given(instance=nuSMV_ValueExpression_strategy)
def test_nusmv_valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nuSMV_UnaryExpression_strategy)
@settings(max_examples=50)
def test_nusmv_unaryexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_UnaryExpression)



@given(instance=nuSMV_UnaryExpression_strategy)
def test_nusmv_unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=nuSMV_UntilCTLexpression_strategy)
@settings(max_examples=50)
def test_nusmv_untilctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_UntilCTLexpression)



@given(instance=nuSMV_UntilCTLexpression_strategy)
def test_nusmv_untilctlexpression_ea_setter(instance):
    original = instance.ea
    instance.ea = original
    assert instance.ea == original

@given(instance=nuSMV_SetValueParameter_strategy)
@settings(max_examples=50)
def test_nusmv_setvalueparameter_instantiation(instance):
    assert isinstance(instance, nuSMV_SetValueParameter)

@given(instance=nuSMV_Not_strategy)
@settings(max_examples=50)
def test_nusmv_not_instantiation(instance):
    assert isinstance(instance, nuSMV_Not)

@given(instance=nuSMV_UnaryFunctionExpression_strategy)
@settings(max_examples=50)
def test_nusmv_unaryfunctionexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_UnaryFunctionExpression)



@given(instance=nuSMV_UnaryFunctionExpression_strategy)
def test_nusmv_unaryfunctionexpression_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=nuSMV_IntervalExpression_strategy)
@settings(max_examples=50)
def test_nusmv_intervalexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_IntervalExpression)



@given(instance=nuSMV_IntervalExpression_strategy)
def test_nusmv_intervalexpression_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=nuSMV_IntervalExpression_strategy)
def test_nusmv_intervalexpression_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=nuSMV_WordExpression_strategy)
@settings(max_examples=50)
def test_nusmv_wordexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_WordExpression)



@given(instance=nuSMV_WordExpression_strategy)
def test_nusmv_wordexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nuSMV_SetExpression_strategy)
@settings(max_examples=50)
def test_nusmv_setexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_SetExpression)

@given(instance=nuSMV_ParsExpression_strategy)
@settings(max_examples=50)
def test_nusmv_parsexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_ParsExpression)



@given(instance=nuSMV_ParsExpression_strategy)
def test_nusmv_parsexpression_isNext_setter(instance):
    original = instance.isNext
    instance.isNext = original
    assert instance.isNext == original

@given(instance=nuSMV_Var_strategy)
@settings(max_examples=50)
def test_nusmv_var_instantiation(instance):
    assert isinstance(instance, nuSMV_Var)

@given(instance=nuSMV_BinaryExpression_strategy)
@settings(max_examples=50)
def test_nusmv_binaryexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_BinaryExpression)



@given(instance=nuSMV_BinaryExpression_strategy)
def test_nusmv_binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=nuSMV_BinaryExpression_strategy)
def test_nusmv_binaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nuSMV_CaseSimpleExpression_strategy)
@settings(max_examples=50)
def test_nusmv_casesimpleexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_CaseSimpleExpression)

@given(instance=nuSMV_Val_strategy)
@settings(max_examples=50)
def test_nusmv_val_instantiation(instance):
    assert isinstance(instance, nuSMV_Val)



@given(instance=nuSMV_Val_strategy)
def test_nusmv_val_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=nuSMV_Val_strategy)
def test_nusmv_val_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=nuSMV_SimpleType_strategy)
@settings(max_examples=50)
def test_nusmv_simpletype_instantiation(instance):
    assert isinstance(instance, nuSMV_SimpleType)

@given(instance=nuSMV_ModuleType_strategy)
@settings(max_examples=50)
def test_nusmv_moduletype_instantiation(instance):
    assert isinstance(instance, nuSMV_ModuleType)

@given(instance=nuSMV_LTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv_ltlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_LTLExpression)

@given(instance=nuSMV_CTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv_ctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_CTLExpression)

@given(instance=FairnessConstraint_strategy)
@settings(max_examples=50)
def test_fairnessconstraint_instantiation(instance):
    assert isinstance(instance, FairnessConstraint)

@given(instance=nuSMV_CompassionExpression_strategy)
@settings(max_examples=50)
def test_nusmv_compassionexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_CompassionExpression)

@given(instance=nuSMV_JusticeExpression_strategy)
@settings(max_examples=50)
def test_nusmv_justiceexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_JusticeExpression)

@given(instance=nuSMV_FairnessExpression_strategy)
@settings(max_examples=50)
def test_nusmv_fairnessexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_FairnessExpression)

@given(instance=nuSMV_NextExpression_strategy)
@settings(max_examples=50)
def test_nusmv_nextexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_NextExpression)

@given(instance=AssignBody_strategy)
@settings(max_examples=50)
def test_assignbody_instantiation(instance):
    assert isinstance(instance, AssignBody)

@given(instance=nuSMV_InitBody_strategy)
@settings(max_examples=50)
def test_nusmv_initbody_instantiation(instance):
    assert isinstance(instance, nuSMV_InitBody)

@given(instance=nuSMV_NextBody_strategy)
@settings(max_examples=50)
def test_nusmv_nextbody_instantiation(instance):
    assert isinstance(instance, nuSMV_NextBody)

@given(instance=nuSMV_VarBodyAssign_strategy)
@settings(max_examples=50)
def test_nusmv_varbodyassign_instantiation(instance):
    assert isinstance(instance, nuSMV_VarBodyAssign)

@given(instance=nuSMV_EObject_strategy)
@settings(max_examples=50)
def test_nusmv_eobject_instantiation(instance):
    assert isinstance(instance, nuSMV_EObject)

@given(instance=nuSMV_AssignBody_strategy)
@settings(max_examples=50)
def test_nusmv_assignbody_instantiation(instance):
    assert isinstance(instance, nuSMV_AssignBody)



@given(instance=nuSMV_AssignBody_strategy)
def test_nusmv_assignbody_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original



@given(instance=nuSMV_AssignBody_strategy)
def test_nusmv_assignbody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_SimpleExpression_strategy)
@settings(max_examples=50)
def test_nusmv_simpleexpression_instantiation(instance):
    assert isinstance(instance, nuSMV_SimpleExpression)

@given(instance=nuSMV_DefineBody_strategy)
@settings(max_examples=50)
def test_nusmv_definebody_instantiation(instance):
    assert isinstance(instance, nuSMV_DefineBody)



@given(instance=nuSMV_DefineBody_strategy)
def test_nusmv_definebody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original



@given(instance=nuSMV_DefineBody_strategy)
def test_nusmv_definebody_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=nuSMV_Type_strategy)
@settings(max_examples=50)
def test_nusmv_type_instantiation(instance):
    assert isinstance(instance, nuSMV_Type)

@given(instance=nuSMV_VarBody_strategy)
@settings(max_examples=50)
def test_nusmv_varbody_instantiation(instance):
    assert isinstance(instance, nuSMV_VarBody)



@given(instance=nuSMV_VarBody_strategy)
def test_nusmv_varbody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original



@given(instance=nuSMV_VarBody_strategy)
def test_nusmv_varbody_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=nuSMV_TransConstraint_strategy)
@settings(max_examples=50)
def test_nusmv_transconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV_TransConstraint)



@given(instance=nuSMV_TransConstraint_strategy)
def test_nusmv_transconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_ConstantsDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_constantsdeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_ConstantsDeclaration)



@given(instance=nuSMV_ConstantsDeclaration_strategy)
def test_nusmv_constantsdeclaration_constants_setter(instance):
    original = instance.constants
    instance.constants = original
    assert instance.constants == original



@given(instance=nuSMV_ConstantsDeclaration_strategy)
def test_nusmv_constantsdeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_FairnessConstraint_strategy)
@settings(max_examples=50)
def test_nusmv_fairnessconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV_FairnessConstraint)



@given(instance=nuSMV_FairnessConstraint_strategy)
def test_nusmv_fairnessconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_IVariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_ivariabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_IVariableDeclaration)

@given(instance=nuSMV_LtlSpecification_strategy)
@settings(max_examples=50)
def test_nusmv_ltlspecification_instantiation(instance):
    assert isinstance(instance, nuSMV_LtlSpecification)



@given(instance=nuSMV_LtlSpecification_strategy)
def test_nusmv_ltlspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nuSMV_LtlSpecification_strategy)
def test_nusmv_ltlspecification_nameId_setter(instance):
    original = instance.nameId
    instance.nameId = original
    assert instance.nameId == original



@given(instance=nuSMV_LtlSpecification_strategy)
def test_nusmv_ltlspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_FrozenVariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_frozenvariabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_FrozenVariableDeclaration)

@given(instance=nuSMV_InvarConstraint_strategy)
@settings(max_examples=50)
def test_nusmv_invarconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV_InvarConstraint)



@given(instance=nuSMV_InvarConstraint_strategy)
def test_nusmv_invarconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_InitConstraint_strategy)
@settings(max_examples=50)
def test_nusmv_initconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV_InitConstraint)



@given(instance=nuSMV_InitConstraint_strategy)
def test_nusmv_initconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_ComputeSpecification_strategy)
@settings(max_examples=50)
def test_nusmv_computespecification_instantiation(instance):
    assert isinstance(instance, nuSMV_ComputeSpecification)



@given(instance=nuSMV_ComputeSpecification_strategy)
def test_nusmv_computespecification_minMax_setter(instance):
    original = instance.minMax
    instance.minMax = original
    assert instance.minMax == original

@given(instance=nuSMV_AssignConstraintElement_strategy)
@settings(max_examples=50)
def test_nusmv_assignconstraintelement_instantiation(instance):
    assert isinstance(instance, nuSMV_AssignConstraintElement)



@given(instance=nuSMV_AssignConstraintElement_strategy)
def test_nusmv_assignconstraintelement_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=nuSMV_DefineDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_definedeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_DefineDeclaration)



@given(instance=nuSMV_DefineDeclaration_strategy)
def test_nusmv_definedeclaration_define_setter(instance):
    original = instance.define
    instance.define = original
    assert instance.define == original

@given(instance=nuSMV_InvarSpecification_strategy)
@settings(max_examples=50)
def test_nusmv_invarspecification_instantiation(instance):
    assert isinstance(instance, nuSMV_InvarSpecification)



@given(instance=nuSMV_InvarSpecification_strategy)
def test_nusmv_invarspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nuSMV_InvarSpecification_strategy)
def test_nusmv_invarspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV_CtlSpecification_strategy)
@settings(max_examples=50)
def test_nusmv_ctlspecification_instantiation(instance):
    assert isinstance(instance, nuSMV_CtlSpecification)



@given(instance=nuSMV_CtlSpecification_strategy)
def test_nusmv_ctlspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=nuSMV_CtlSpecification_strategy)
def test_nusmv_ctlspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original



@given(instance=nuSMV_CtlSpecification_strategy)
def test_nusmv_ctlspecification_specKeyWord_setter(instance):
    original = instance.specKeyWord
    instance.specKeyWord = original
    assert instance.specKeyWord == original



@given(instance=nuSMV_CtlSpecification_strategy)
def test_nusmv_ctlspecification_nameKeyWord_setter(instance):
    original = instance.nameKeyWord
    instance.nameKeyWord = original
    assert instance.nameKeyWord == original

@given(instance=nuSMV_IsaDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_isadeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_IsaDeclaration)



@given(instance=nuSMV_IsaDeclaration_strategy)
def test_nusmv_isadeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=nuSMV_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv_variabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV_VariableDeclaration)

@given(instance=nuSMV_ModuleElement_strategy)
@settings(max_examples=50)
def test_nusmv_moduleelement_instantiation(instance):
    assert isinstance(instance, nuSMV_ModuleElement)

@given(instance=nuSMV_FormalParameter_strategy)
@settings(max_examples=50)
def test_nusmv_formalparameter_instantiation(instance):
    assert isinstance(instance, nuSMV_FormalParameter)



@given(instance=nuSMV_FormalParameter_strategy)
def test_nusmv_formalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV_Module_strategy)
@settings(max_examples=50)
def test_nusmv_module_instantiation(instance):
    assert isinstance(instance, nuSMV_Module)



@given(instance=nuSMV_Module_strategy)
def test_nusmv_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV_NuSmvModel_strategy)
@settings(max_examples=50)
def test_nusmv_nusmvmodel_instantiation(instance):
    assert isinstance(instance, nuSMV_NuSmvModel)
