import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RTCTLExpression,
    nuSMV::UnaryRTCTLExpression,
    nuSMV::SingleRTCTLExpression,
    ModuleType,
    nuSMV::SyncrProcessType,
    nuSMV::AsyncrProcessType,
    SimpleType,
    nuSMV::IntervalType,
    nuSMV::SignedWordType,
    nuSMV::EnumType,
    nuSMV::UnsignedWordType,
    nuSMV::ArrayType,
    nuSMV::WordType,
    nuSMV::BooleanType,
    nuSMV::RTCTLExpression,
    nuSMV::RangeExpression,
    nuSMV::CaseSimpleAssignementExpression,
    SimpleExpression,
    nuSMV::UnaryExpression,
    nuSMV::BinaryExpression,
    nuSMV::UntilCTLexpression,
    nuSMV::Not,
    nuSMV::Var,
    nuSMV::WordExpression,
    nuSMV::SetExpression,
    nuSMV::ValueExpression,
    nuSMV::ParsExpression,
    nuSMV::SetValueParameter,
    nuSMV::UnaryFunctionExpression,
    nuSMV::SetElementExpression,
    nuSMV::IntervalExpression,
    nuSMV::CaseSimpleExpression,
    nuSMV::Val,
    Type,
    nuSMV::ModuleType,
    nuSMV::SimpleType,
    nuSMV::LTLExpression,
    nuSMV::CTLExpression,
    FairnessConstraint,
    nuSMV::JusticeExpression,
    nuSMV::CompassionExpression,
    nuSMV::FairnessExpression,
    nuSMV::NextExpression,
    AssignBody,
    nuSMV::InitBody,
    nuSMV::NextBody,
    nuSMV::VarBodyAssign,
    nuSMV::EObject,
    nuSMV::AssignBody,
    nuSMV::SimpleExpression,
    nuSMV::DefineBody,
    nuSMV::Type,
    nuSMV::VarBody,
    ModuleElement,
    nuSMV::IsaDeclaration,
    nuSMV::LtlSpecification,
    nuSMV::InvarConstraint,
    nuSMV::AssignConstraintElement,
    nuSMV::IVariableDeclaration,
    nuSMV::DefineDeclaration,
    nuSMV::InvarSpecification,
    nuSMV::ComputeSpecification,
    nuSMV::CtlSpecification,
    nuSMV::FairnessConstraint,
    nuSMV::FrozenVariableDeclaration,
    nuSMV::ConstantsDeclaration,
    nuSMV::InitConstraint,
    nuSMV::TransConstraint,
    nuSMV::VariableDeclaration,
    nuSMV::ModuleElement,
    nuSMV::FormalParameter,
    nuSMV::Module,
    nuSMV::NuSmvModel,
    operators,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rtctlexpression_is_not_abstract():
    assert not inspect.isabstract(RTCTLExpression)


def test_rtctlexpression_constructor_exists():
    assert callable(RTCTLExpression.__init__)


def test_rtctlexpression_constructor_args():
    sig = inspect.signature(RTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::unaryrtctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::UnaryRTCTLExpression)


def test_nusmv::unaryrtctlexpression_constructor_exists():
    assert callable(nuSMV::UnaryRTCTLExpression.__init__)


def test_nusmv::unaryrtctlexpression_constructor_args():
    sig = inspect.signature(nuSMV::UnaryRTCTLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "unary" in params, "Missing parameter 'unary'"

def test_nusmv::unaryrtctlexpression_has_unary():
    assert hasattr(nuSMV::UnaryRTCTLExpression, "unary")
    descriptor = None
    for klass in nuSMV::UnaryRTCTLExpression.__mro__:
        if "unary" in klass.__dict__:
            descriptor = klass.__dict__["unary"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::singlertctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SingleRTCTLExpression)


def test_nusmv::singlertctlexpression_constructor_exists():
    assert callable(nuSMV::SingleRTCTLExpression.__init__)


def test_nusmv::singlertctlexpression_constructor_args():
    sig = inspect.signature(nuSMV::SingleRTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_moduletype_is_not_abstract():
    assert not inspect.isabstract(ModuleType)


def test_moduletype_constructor_exists():
    assert callable(ModuleType.__init__)


def test_moduletype_constructor_args():
    sig = inspect.signature(ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::syncrprocesstype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SyncrProcessType)


def test_nusmv::syncrprocesstype_constructor_exists():
    assert callable(nuSMV::SyncrProcessType.__init__)


def test_nusmv::syncrprocesstype_constructor_args():
    sig = inspect.signature(nuSMV::SyncrProcessType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::asyncrprocesstype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::AsyncrProcessType)


def test_nusmv::asyncrprocesstype_constructor_exists():
    assert callable(nuSMV::AsyncrProcessType.__init__)


def test_nusmv::asyncrprocesstype_constructor_args():
    sig = inspect.signature(nuSMV::AsyncrProcessType.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::intervaltype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::IntervalType)


def test_nusmv::intervaltype_constructor_exists():
    assert callable(nuSMV::IntervalType.__init__)


def test_nusmv::intervaltype_constructor_args():
    sig = inspect.signature(nuSMV::IntervalType.__init__)
    params = list(sig.parameters.keys())
    assert "low" in params, "Missing parameter 'low'"
    assert "high" in params, "Missing parameter 'high'"

def test_nusmv::intervaltype_has_low():
    assert hasattr(nuSMV::IntervalType, "low")
    descriptor = None
    for klass in nuSMV::IntervalType.__mro__:
        if "low" in klass.__dict__:
            descriptor = klass.__dict__["low"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::intervaltype_has_high():
    assert hasattr(nuSMV::IntervalType, "high")
    descriptor = None
    for klass in nuSMV::IntervalType.__mro__:
        if "high" in klass.__dict__:
            descriptor = klass.__dict__["high"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::signedwordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SignedWordType)


def test_nusmv::signedwordtype_constructor_exists():
    assert callable(nuSMV::SignedWordType.__init__)


def test_nusmv::signedwordtype_constructor_args():
    sig = inspect.signature(nuSMV::SignedWordType.__init__)
    params = list(sig.parameters.keys())
    assert "signedNumber" in params, "Missing parameter 'signedNumber'"

def test_nusmv::signedwordtype_has_signedNumber():
    assert hasattr(nuSMV::SignedWordType, "signedNumber")
    descriptor = None
    for klass in nuSMV::SignedWordType.__mro__:
        if "signedNumber" in klass.__dict__:
            descriptor = klass.__dict__["signedNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::enumtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::EnumType)


def test_nusmv::enumtype_constructor_exists():
    assert callable(nuSMV::EnumType.__init__)


def test_nusmv::enumtype_constructor_args():
    sig = inspect.signature(nuSMV::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::unsignedwordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::UnsignedWordType)


def test_nusmv::unsignedwordtype_constructor_exists():
    assert callable(nuSMV::UnsignedWordType.__init__)


def test_nusmv::unsignedwordtype_constructor_args():
    sig = inspect.signature(nuSMV::UnsignedWordType.__init__)
    params = list(sig.parameters.keys())
    assert "uWordNumber" in params, "Missing parameter 'uWordNumber'"

def test_nusmv::unsignedwordtype_has_uWordNumber():
    assert hasattr(nuSMV::UnsignedWordType, "uWordNumber")
    descriptor = None
    for klass in nuSMV::UnsignedWordType.__mro__:
        if "uWordNumber" in klass.__dict__:
            descriptor = klass.__dict__["uWordNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::arraytype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ArrayType)


def test_nusmv::arraytype_constructor_exists():
    assert callable(nuSMV::ArrayType.__init__)


def test_nusmv::arraytype_constructor_args():
    sig = inspect.signature(nuSMV::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_nusmv::arraytype_has_lowerBound():
    assert hasattr(nuSMV::ArrayType, "lowerBound")
    descriptor = None
    for klass in nuSMV::ArrayType.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::arraytype_has_upperBound():
    assert hasattr(nuSMV::ArrayType, "upperBound")
    descriptor = None
    for klass in nuSMV::ArrayType.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::wordtype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::WordType)


def test_nusmv::wordtype_constructor_exists():
    assert callable(nuSMV::WordType.__init__)


def test_nusmv::wordtype_constructor_args():
    sig = inspect.signature(nuSMV::WordType.__init__)
    params = list(sig.parameters.keys())
    assert "wordNumber" in params, "Missing parameter 'wordNumber'"

def test_nusmv::wordtype_has_wordNumber():
    assert hasattr(nuSMV::WordType, "wordNumber")
    descriptor = None
    for klass in nuSMV::WordType.__mro__:
        if "wordNumber" in klass.__dict__:
            descriptor = klass.__dict__["wordNumber"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::booleantype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::BooleanType)


def test_nusmv::booleantype_constructor_exists():
    assert callable(nuSMV::BooleanType.__init__)


def test_nusmv::booleantype_constructor_args():
    sig = inspect.signature(nuSMV::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::rtctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::RTCTLExpression)


def test_nusmv::rtctlexpression_constructor_exists():
    assert callable(nuSMV::RTCTLExpression.__init__)


def test_nusmv::rtctlexpression_constructor_args():
    sig = inspect.signature(nuSMV::RTCTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::rangeexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::RangeExpression)


def test_nusmv::rangeexpression_constructor_exists():
    assert callable(nuSMV::RangeExpression.__init__)


def test_nusmv::rangeexpression_constructor_args():
    sig = inspect.signature(nuSMV::RangeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_nusmv::rangeexpression_has_lower():
    assert hasattr(nuSMV::RangeExpression, "lower")
    descriptor = None
    for klass in nuSMV::RangeExpression.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::rangeexpression_has_upper():
    assert hasattr(nuSMV::RangeExpression, "upper")
    descriptor = None
    for klass in nuSMV::RangeExpression.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::casesimpleassignementexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::CaseSimpleAssignementExpression)


def test_nusmv::casesimpleassignementexpression_constructor_exists():
    assert callable(nuSMV::CaseSimpleAssignementExpression.__init__)


def test_nusmv::casesimpleassignementexpression_constructor_args():
    sig = inspect.signature(nuSMV::CaseSimpleAssignementExpression.__init__)
    params = list(sig.parameters.keys())



def test_simpleexpression_is_not_abstract():
    assert not inspect.isabstract(SimpleExpression)


def test_simpleexpression_constructor_exists():
    assert callable(SimpleExpression.__init__)


def test_simpleexpression_constructor_args():
    sig = inspect.signature(SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::UnaryExpression)


def test_nusmv::unaryexpression_constructor_exists():
    assert callable(nuSMV::UnaryExpression.__init__)


def test_nusmv::unaryexpression_constructor_args():
    sig = inspect.signature(nuSMV::UnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_nusmv::unaryexpression_has_operator():
    assert hasattr(nuSMV::UnaryExpression, "operator")
    descriptor = None
    for klass in nuSMV::UnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::BinaryExpression)


def test_nusmv::binaryexpression_constructor_exists():
    assert callable(nuSMV::BinaryExpression.__init__)


def test_nusmv::binaryexpression_constructor_args():
    sig = inspect.signature(nuSMV::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_nusmv::binaryexpression_has_op():
    assert hasattr(nuSMV::BinaryExpression, "op")
    descriptor = None
    for klass in nuSMV::BinaryExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::binaryexpression_has_operator():
    assert hasattr(nuSMV::BinaryExpression, "operator")
    descriptor = None
    for klass in nuSMV::BinaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::untilctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::UntilCTLexpression)


def test_nusmv::untilctlexpression_constructor_exists():
    assert callable(nuSMV::UntilCTLexpression.__init__)


def test_nusmv::untilctlexpression_constructor_args():
    sig = inspect.signature(nuSMV::UntilCTLexpression.__init__)
    params = list(sig.parameters.keys())
    assert "ea" in params, "Missing parameter 'ea'"

def test_nusmv::untilctlexpression_has_ea():
    assert hasattr(nuSMV::UntilCTLexpression, "ea")
    descriptor = None
    for klass in nuSMV::UntilCTLexpression.__mro__:
        if "ea" in klass.__dict__:
            descriptor = klass.__dict__["ea"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::not_is_not_abstract():
    assert not inspect.isabstract(nuSMV::Not)


def test_nusmv::not_constructor_exists():
    assert callable(nuSMV::Not.__init__)


def test_nusmv::not_constructor_args():
    sig = inspect.signature(nuSMV::Not.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::var_is_not_abstract():
    assert not inspect.isabstract(nuSMV::Var)


def test_nusmv::var_constructor_exists():
    assert callable(nuSMV::Var.__init__)


def test_nusmv::var_constructor_args():
    sig = inspect.signature(nuSMV::Var.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::wordexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::WordExpression)


def test_nusmv::wordexpression_constructor_exists():
    assert callable(nuSMV::WordExpression.__init__)


def test_nusmv::wordexpression_constructor_args():
    sig = inspect.signature(nuSMV::WordExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nusmv::wordexpression_has_value():
    assert hasattr(nuSMV::WordExpression, "value")
    descriptor = None
    for klass in nuSMV::WordExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::setexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SetExpression)


def test_nusmv::setexpression_constructor_exists():
    assert callable(nuSMV::SetExpression.__init__)


def test_nusmv::setexpression_constructor_args():
    sig = inspect.signature(nuSMV::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::valueexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ValueExpression)


def test_nusmv::valueexpression_constructor_exists():
    assert callable(nuSMV::ValueExpression.__init__)


def test_nusmv::valueexpression_constructor_args():
    sig = inspect.signature(nuSMV::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_nusmv::valueexpression_has_value():
    assert hasattr(nuSMV::ValueExpression, "value")
    descriptor = None
    for klass in nuSMV::ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::parsexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ParsExpression)


def test_nusmv::parsexpression_constructor_exists():
    assert callable(nuSMV::ParsExpression.__init__)


def test_nusmv::parsexpression_constructor_args():
    sig = inspect.signature(nuSMV::ParsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isNext" in params, "Missing parameter 'isNext'"

def test_nusmv::parsexpression_has_isNext():
    assert hasattr(nuSMV::ParsExpression, "isNext")
    descriptor = None
    for klass in nuSMV::ParsExpression.__mro__:
        if "isNext" in klass.__dict__:
            descriptor = klass.__dict__["isNext"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::setvalueparameter_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SetValueParameter)


def test_nusmv::setvalueparameter_constructor_exists():
    assert callable(nuSMV::SetValueParameter.__init__)


def test_nusmv::setvalueparameter_constructor_args():
    sig = inspect.signature(nuSMV::SetValueParameter.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::unaryfunctionexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::UnaryFunctionExpression)


def test_nusmv::unaryfunctionexpression_constructor_exists():
    assert callable(nuSMV::UnaryFunctionExpression.__init__)


def test_nusmv::unaryfunctionexpression_constructor_args():
    sig = inspect.signature(nuSMV::UnaryFunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_nusmv::unaryfunctionexpression_has_function():
    assert hasattr(nuSMV::UnaryFunctionExpression, "function")
    descriptor = None
    for klass in nuSMV::UnaryFunctionExpression.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::setelementexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SetElementExpression)


def test_nusmv::setelementexpression_constructor_exists():
    assert callable(nuSMV::SetElementExpression.__init__)


def test_nusmv::setelementexpression_constructor_args():
    sig = inspect.signature(nuSMV::SetElementExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::intervalexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::IntervalExpression)


def test_nusmv::intervalexpression_constructor_exists():
    assert callable(nuSMV::IntervalExpression.__init__)


def test_nusmv::intervalexpression_constructor_args():
    sig = inspect.signature(nuSMV::IntervalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_nusmv::intervalexpression_has_lowerBound():
    assert hasattr(nuSMV::IntervalExpression, "lowerBound")
    descriptor = None
    for klass in nuSMV::IntervalExpression.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::intervalexpression_has_upperBound():
    assert hasattr(nuSMV::IntervalExpression, "upperBound")
    descriptor = None
    for klass in nuSMV::IntervalExpression.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::casesimpleexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::CaseSimpleExpression)


def test_nusmv::casesimpleexpression_constructor_exists():
    assert callable(nuSMV::CaseSimpleExpression.__init__)


def test_nusmv::casesimpleexpression_constructor_args():
    sig = inspect.signature(nuSMV::CaseSimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::val_is_not_abstract():
    assert not inspect.isabstract(nuSMV::Val)


def test_nusmv::val_constructor_exists():
    assert callable(nuSMV::Val.__init__)


def test_nusmv::val_constructor_args():
    sig = inspect.signature(nuSMV::Val.__init__)
    params = list(sig.parameters.keys())
    assert "num" in params, "Missing parameter 'num'"
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv::val_has_num():
    assert hasattr(nuSMV::Val, "num")
    descriptor = None
    for klass in nuSMV::Val.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::val_has_name():
    assert hasattr(nuSMV::Val, "name")
    descriptor = None
    for klass in nuSMV::Val.__mro__:
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



def test_nusmv::moduletype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ModuleType)


def test_nusmv::moduletype_constructor_exists():
    assert callable(nuSMV::ModuleType.__init__)


def test_nusmv::moduletype_constructor_args():
    sig = inspect.signature(nuSMV::ModuleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::simpletype_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SimpleType)


def test_nusmv::simpletype_constructor_exists():
    assert callable(nuSMV::SimpleType.__init__)


def test_nusmv::simpletype_constructor_args():
    sig = inspect.signature(nuSMV::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::ltlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::LTLExpression)


def test_nusmv::ltlexpression_constructor_exists():
    assert callable(nuSMV::LTLExpression.__init__)


def test_nusmv::ltlexpression_constructor_args():
    sig = inspect.signature(nuSMV::LTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::ctlexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::CTLExpression)


def test_nusmv::ctlexpression_constructor_exists():
    assert callable(nuSMV::CTLExpression.__init__)


def test_nusmv::ctlexpression_constructor_args():
    sig = inspect.signature(nuSMV::CTLExpression.__init__)
    params = list(sig.parameters.keys())



def test_fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(FairnessConstraint)


def test_fairnessconstraint_constructor_exists():
    assert callable(FairnessConstraint.__init__)


def test_fairnessconstraint_constructor_args():
    sig = inspect.signature(FairnessConstraint.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::justiceexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::JusticeExpression)


def test_nusmv::justiceexpression_constructor_exists():
    assert callable(nuSMV::JusticeExpression.__init__)


def test_nusmv::justiceexpression_constructor_args():
    sig = inspect.signature(nuSMV::JusticeExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::compassionexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::CompassionExpression)


def test_nusmv::compassionexpression_constructor_exists():
    assert callable(nuSMV::CompassionExpression.__init__)


def test_nusmv::compassionexpression_constructor_args():
    sig = inspect.signature(nuSMV::CompassionExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::fairnessexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::FairnessExpression)


def test_nusmv::fairnessexpression_constructor_exists():
    assert callable(nuSMV::FairnessExpression.__init__)


def test_nusmv::fairnessexpression_constructor_args():
    sig = inspect.signature(nuSMV::FairnessExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::nextexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::NextExpression)


def test_nusmv::nextexpression_constructor_exists():
    assert callable(nuSMV::NextExpression.__init__)


def test_nusmv::nextexpression_constructor_args():
    sig = inspect.signature(nuSMV::NextExpression.__init__)
    params = list(sig.parameters.keys())



def test_assignbody_is_not_abstract():
    assert not inspect.isabstract(AssignBody)


def test_assignbody_constructor_exists():
    assert callable(AssignBody.__init__)


def test_assignbody_constructor_args():
    sig = inspect.signature(AssignBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::initbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV::InitBody)


def test_nusmv::initbody_constructor_exists():
    assert callable(nuSMV::InitBody.__init__)


def test_nusmv::initbody_constructor_args():
    sig = inspect.signature(nuSMV::InitBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::nextbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV::NextBody)


def test_nusmv::nextbody_constructor_exists():
    assert callable(nuSMV::NextBody.__init__)


def test_nusmv::nextbody_constructor_args():
    sig = inspect.signature(nuSMV::NextBody.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::varbodyassign_is_not_abstract():
    assert not inspect.isabstract(nuSMV::VarBodyAssign)


def test_nusmv::varbodyassign_constructor_exists():
    assert callable(nuSMV::VarBodyAssign.__init__)


def test_nusmv::varbodyassign_constructor_args():
    sig = inspect.signature(nuSMV::VarBodyAssign.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::eobject_is_not_abstract():
    assert not inspect.isabstract(nuSMV::EObject)


def test_nusmv::eobject_constructor_exists():
    assert callable(nuSMV::EObject.__init__)


def test_nusmv::eobject_constructor_args():
    sig = inspect.signature(nuSMV::EObject.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::assignbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV::AssignBody)


def test_nusmv::assignbody_constructor_exists():
    assert callable(nuSMV::AssignBody.__init__)


def test_nusmv::assignbody_constructor_args():
    sig = inspect.signature(nuSMV::AssignBody.__init__)
    params = list(sig.parameters.keys())
    assert "array" in params, "Missing parameter 'array'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::assignbody_has_array():
    assert hasattr(nuSMV::AssignBody, "array")
    descriptor = None
    for klass in nuSMV::AssignBody.__mro__:
        if "array" in klass.__dict__:
            descriptor = klass.__dict__["array"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::assignbody_has_semicolon():
    assert hasattr(nuSMV::AssignBody, "semicolon")
    descriptor = None
    for klass in nuSMV::AssignBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::simpleexpression_is_not_abstract():
    assert not inspect.isabstract(nuSMV::SimpleExpression)


def test_nusmv::simpleexpression_constructor_exists():
    assert callable(nuSMV::SimpleExpression.__init__)


def test_nusmv::simpleexpression_constructor_args():
    sig = inspect.signature(nuSMV::SimpleExpression.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::definebody_is_not_abstract():
    assert not inspect.isabstract(nuSMV::DefineBody)


def test_nusmv::definebody_constructor_exists():
    assert callable(nuSMV::DefineBody.__init__)


def test_nusmv::definebody_constructor_args():
    sig = inspect.signature(nuSMV::DefineBody.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::definebody_has_var():
    assert hasattr(nuSMV::DefineBody, "var")
    descriptor = None
    for klass in nuSMV::DefineBody.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::definebody_has_semicolon():
    assert hasattr(nuSMV::DefineBody, "semicolon")
    descriptor = None
    for klass in nuSMV::DefineBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::type_is_not_abstract():
    assert not inspect.isabstract(nuSMV::Type)


def test_nusmv::type_constructor_exists():
    assert callable(nuSMV::Type.__init__)


def test_nusmv::type_constructor_args():
    sig = inspect.signature(nuSMV::Type.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::varbody_is_not_abstract():
    assert not inspect.isabstract(nuSMV::VarBody)


def test_nusmv::varbody_constructor_exists():
    assert callable(nuSMV::VarBody.__init__)


def test_nusmv::varbody_constructor_args():
    sig = inspect.signature(nuSMV::VarBody.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::varbody_has_name():
    assert hasattr(nuSMV::VarBody, "name")
    descriptor = None
    for klass in nuSMV::VarBody.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::varbody_has_semicolon():
    assert hasattr(nuSMV::VarBody, "semicolon")
    descriptor = None
    for klass in nuSMV::VarBody.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::isadeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::IsaDeclaration)


def test_nusmv::isadeclaration_constructor_exists():
    assert callable(nuSMV::IsaDeclaration.__init__)


def test_nusmv::isadeclaration_constructor_args():
    sig = inspect.signature(nuSMV::IsaDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_nusmv::isadeclaration_has_id():
    assert hasattr(nuSMV::IsaDeclaration, "id")
    descriptor = None
    for klass in nuSMV::IsaDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::ltlspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV::LtlSpecification)


def test_nusmv::ltlspecification_constructor_exists():
    assert callable(nuSMV::LtlSpecification.__init__)


def test_nusmv::ltlspecification_constructor_args():
    sig = inspect.signature(nuSMV::LtlSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nameId" in params, "Missing parameter 'nameId'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::ltlspecification_has_name():
    assert hasattr(nuSMV::LtlSpecification, "name")
    descriptor = None
    for klass in nuSMV::LtlSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::ltlspecification_has_nameId():
    assert hasattr(nuSMV::LtlSpecification, "nameId")
    descriptor = None
    for klass in nuSMV::LtlSpecification.__mro__:
        if "nameId" in klass.__dict__:
            descriptor = klass.__dict__["nameId"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::ltlspecification_has_semicolon():
    assert hasattr(nuSMV::LtlSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV::LtlSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::invarconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV::InvarConstraint)


def test_nusmv::invarconstraint_constructor_exists():
    assert callable(nuSMV::InvarConstraint.__init__)


def test_nusmv::invarconstraint_constructor_args():
    sig = inspect.signature(nuSMV::InvarConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::invarconstraint_has_semicolon():
    assert hasattr(nuSMV::InvarConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV::InvarConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::assignconstraintelement_is_not_abstract():
    assert not inspect.isabstract(nuSMV::AssignConstraintElement)


def test_nusmv::assignconstraintelement_constructor_exists():
    assert callable(nuSMV::AssignConstraintElement.__init__)


def test_nusmv::assignconstraintelement_constructor_args():
    sig = inspect.signature(nuSMV::AssignConstraintElement.__init__)
    params = list(sig.parameters.keys())
    assert "assign" in params, "Missing parameter 'assign'"

def test_nusmv::assignconstraintelement_has_assign():
    assert hasattr(nuSMV::AssignConstraintElement, "assign")
    descriptor = None
    for klass in nuSMV::AssignConstraintElement.__mro__:
        if "assign" in klass.__dict__:
            descriptor = klass.__dict__["assign"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::ivariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::IVariableDeclaration)


def test_nusmv::ivariabledeclaration_constructor_exists():
    assert callable(nuSMV::IVariableDeclaration.__init__)


def test_nusmv::ivariabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV::IVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::definedeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::DefineDeclaration)


def test_nusmv::definedeclaration_constructor_exists():
    assert callable(nuSMV::DefineDeclaration.__init__)


def test_nusmv::definedeclaration_constructor_args():
    sig = inspect.signature(nuSMV::DefineDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "define" in params, "Missing parameter 'define'"

def test_nusmv::definedeclaration_has_define():
    assert hasattr(nuSMV::DefineDeclaration, "define")
    descriptor = None
    for klass in nuSMV::DefineDeclaration.__mro__:
        if "define" in klass.__dict__:
            descriptor = klass.__dict__["define"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::invarspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV::InvarSpecification)


def test_nusmv::invarspecification_constructor_exists():
    assert callable(nuSMV::InvarSpecification.__init__)


def test_nusmv::invarspecification_constructor_args():
    sig = inspect.signature(nuSMV::InvarSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv::invarspecification_has_semicolon():
    assert hasattr(nuSMV::InvarSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV::InvarSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::invarspecification_has_name():
    assert hasattr(nuSMV::InvarSpecification, "name")
    descriptor = None
    for klass in nuSMV::InvarSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::computespecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ComputeSpecification)


def test_nusmv::computespecification_constructor_exists():
    assert callable(nuSMV::ComputeSpecification.__init__)


def test_nusmv::computespecification_constructor_args():
    sig = inspect.signature(nuSMV::ComputeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "minMax" in params, "Missing parameter 'minMax'"

def test_nusmv::computespecification_has_minMax():
    assert hasattr(nuSMV::ComputeSpecification, "minMax")
    descriptor = None
    for klass in nuSMV::ComputeSpecification.__mro__:
        if "minMax" in klass.__dict__:
            descriptor = klass.__dict__["minMax"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::ctlspecification_is_not_abstract():
    assert not inspect.isabstract(nuSMV::CtlSpecification)


def test_nusmv::ctlspecification_constructor_exists():
    assert callable(nuSMV::CtlSpecification.__init__)


def test_nusmv::ctlspecification_constructor_args():
    sig = inspect.signature(nuSMV::CtlSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"
    assert "name" in params, "Missing parameter 'name'"
    assert "nameKeyWord" in params, "Missing parameter 'nameKeyWord'"
    assert "specKeyWord" in params, "Missing parameter 'specKeyWord'"

def test_nusmv::ctlspecification_has_semicolon():
    assert hasattr(nuSMV::CtlSpecification, "semicolon")
    descriptor = None
    for klass in nuSMV::CtlSpecification.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::ctlspecification_has_name():
    assert hasattr(nuSMV::CtlSpecification, "name")
    descriptor = None
    for klass in nuSMV::CtlSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::ctlspecification_has_nameKeyWord():
    assert hasattr(nuSMV::CtlSpecification, "nameKeyWord")
    descriptor = None
    for klass in nuSMV::CtlSpecification.__mro__:
        if "nameKeyWord" in klass.__dict__:
            descriptor = klass.__dict__["nameKeyWord"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::ctlspecification_has_specKeyWord():
    assert hasattr(nuSMV::CtlSpecification, "specKeyWord")
    descriptor = None
    for klass in nuSMV::CtlSpecification.__mro__:
        if "specKeyWord" in klass.__dict__:
            descriptor = klass.__dict__["specKeyWord"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV::FairnessConstraint)


def test_nusmv::fairnessconstraint_constructor_exists():
    assert callable(nuSMV::FairnessConstraint.__init__)


def test_nusmv::fairnessconstraint_constructor_args():
    sig = inspect.signature(nuSMV::FairnessConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::fairnessconstraint_has_semicolon():
    assert hasattr(nuSMV::FairnessConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV::FairnessConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::frozenvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::FrozenVariableDeclaration)


def test_nusmv::frozenvariabledeclaration_constructor_exists():
    assert callable(nuSMV::FrozenVariableDeclaration.__init__)


def test_nusmv::frozenvariabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV::FrozenVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::constantsdeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ConstantsDeclaration)


def test_nusmv::constantsdeclaration_constructor_exists():
    assert callable(nuSMV::ConstantsDeclaration.__init__)


def test_nusmv::constantsdeclaration_constructor_args():
    sig = inspect.signature(nuSMV::ConstantsDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "constants" in params, "Missing parameter 'constants'"
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::constantsdeclaration_has_constants():
    assert hasattr(nuSMV::ConstantsDeclaration, "constants")
    descriptor = None
    for klass in nuSMV::ConstantsDeclaration.__mro__:
        if "constants" in klass.__dict__:
            descriptor = klass.__dict__["constants"]
            break
    assert isinstance(descriptor, property)

def test_nusmv::constantsdeclaration_has_semicolon():
    assert hasattr(nuSMV::ConstantsDeclaration, "semicolon")
    descriptor = None
    for klass in nuSMV::ConstantsDeclaration.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::initconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV::InitConstraint)


def test_nusmv::initconstraint_constructor_exists():
    assert callable(nuSMV::InitConstraint.__init__)


def test_nusmv::initconstraint_constructor_args():
    sig = inspect.signature(nuSMV::InitConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::initconstraint_has_semicolon():
    assert hasattr(nuSMV::InitConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV::InitConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::transconstraint_is_not_abstract():
    assert not inspect.isabstract(nuSMV::TransConstraint)


def test_nusmv::transconstraint_constructor_exists():
    assert callable(nuSMV::TransConstraint.__init__)


def test_nusmv::transconstraint_constructor_args():
    sig = inspect.signature(nuSMV::TransConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "semicolon" in params, "Missing parameter 'semicolon'"

def test_nusmv::transconstraint_has_semicolon():
    assert hasattr(nuSMV::TransConstraint, "semicolon")
    descriptor = None
    for klass in nuSMV::TransConstraint.__mro__:
        if "semicolon" in klass.__dict__:
            descriptor = klass.__dict__["semicolon"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(nuSMV::VariableDeclaration)


def test_nusmv::variabledeclaration_constructor_exists():
    assert callable(nuSMV::VariableDeclaration.__init__)


def test_nusmv::variabledeclaration_constructor_args():
    sig = inspect.signature(nuSMV::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::moduleelement_is_not_abstract():
    assert not inspect.isabstract(nuSMV::ModuleElement)


def test_nusmv::moduleelement_constructor_exists():
    assert callable(nuSMV::ModuleElement.__init__)


def test_nusmv::moduleelement_constructor_args():
    sig = inspect.signature(nuSMV::ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_nusmv::formalparameter_is_not_abstract():
    assert not inspect.isabstract(nuSMV::FormalParameter)


def test_nusmv::formalparameter_constructor_exists():
    assert callable(nuSMV::FormalParameter.__init__)


def test_nusmv::formalparameter_constructor_args():
    sig = inspect.signature(nuSMV::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv::formalparameter_has_name():
    assert hasattr(nuSMV::FormalParameter, "name")
    descriptor = None
    for klass in nuSMV::FormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::module_is_not_abstract():
    assert not inspect.isabstract(nuSMV::Module)


def test_nusmv::module_constructor_exists():
    assert callable(nuSMV::Module.__init__)


def test_nusmv::module_constructor_args():
    sig = inspect.signature(nuSMV::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nusmv::module_has_name():
    assert hasattr(nuSMV::Module, "name")
    descriptor = None
    for klass in nuSMV::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nusmv::nusmvmodel_is_not_abstract():
    assert not inspect.isabstract(nuSMV::NuSmvModel)


def test_nusmv::nusmvmodel_constructor_exists():
    assert callable(nuSMV::NuSmvModel.__init__)


def test_nusmv::nusmvmodel_constructor_args():
    sig = inspect.signature(nuSMV::NuSmvModel.__init__)
    params = list(sig.parameters.keys())

def test_operators_exists():
    # Check that the Enumeration exists
    assert operators is not None

def test_operators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in operators]
    expected_literals = [
        "le",
        "v",
        "s",
        "ge",
        "and_",
        "or_",
        "u",
        "xor",
        "l",
        "t",
        "g",
        "dis",
        "xnor",
        "equal",
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
RTCTLExpression_strategy = st.builds(
    RTCTLExpression,
)
nuSMV::UnaryRTCTLExpression_strategy = st.builds(
    nuSMV::UnaryRTCTLExpression,
    unary=
        safe_text
)
nuSMV::SingleRTCTLExpression_strategy = st.builds(
    nuSMV::SingleRTCTLExpression,
)
ModuleType_strategy = st.builds(
    ModuleType,
)
nuSMV::SyncrProcessType_strategy = st.builds(
    nuSMV::SyncrProcessType,
)
nuSMV::AsyncrProcessType_strategy = st.builds(
    nuSMV::AsyncrProcessType,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
nuSMV::IntervalType_strategy = st.builds(
    nuSMV::IntervalType,
    low=
        safe_text,
    high=
        safe_text
)
nuSMV::SignedWordType_strategy = st.builds(
    nuSMV::SignedWordType,
    signedNumber=
        safe_text
)
nuSMV::EnumType_strategy = st.builds(
    nuSMV::EnumType,
)
nuSMV::UnsignedWordType_strategy = st.builds(
    nuSMV::UnsignedWordType,
    uWordNumber=
        safe_text
)
nuSMV::ArrayType_strategy = st.builds(
    nuSMV::ArrayType,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
nuSMV::WordType_strategy = st.builds(
    nuSMV::WordType,
    wordNumber=
        safe_text
)
nuSMV::BooleanType_strategy = st.builds(
    nuSMV::BooleanType,
)
nuSMV::RTCTLExpression_strategy = st.builds(
    nuSMV::RTCTLExpression,
)
nuSMV::RangeExpression_strategy = st.builds(
    nuSMV::RangeExpression,
    lower=
        safe_text,
    upper=
        safe_text
)
nuSMV::CaseSimpleAssignementExpression_strategy = st.builds(
    nuSMV::CaseSimpleAssignementExpression,
)
SimpleExpression_strategy = st.builds(
    SimpleExpression,
)
nuSMV::UnaryExpression_strategy = st.builds(
    nuSMV::UnaryExpression,
    operator=
        safe_text
)
nuSMV::BinaryExpression_strategy = st.builds(
    nuSMV::BinaryExpression,
    op=
        safe_text,
    operator=
        safe_text
)
nuSMV::UntilCTLexpression_strategy = st.builds(
    nuSMV::UntilCTLexpression,
    ea=
        safe_text
)
nuSMV::Not_strategy = st.builds(
    nuSMV::Not,
)
nuSMV::Var_strategy = st.builds(
    nuSMV::Var,
)
nuSMV::WordExpression_strategy = st.builds(
    nuSMV::WordExpression,
    value=
        safe_text
)
nuSMV::SetExpression_strategy = st.builds(
    nuSMV::SetExpression,
)
nuSMV::ValueExpression_strategy = st.builds(
    nuSMV::ValueExpression,
    value=
        safe_text
)
nuSMV::ParsExpression_strategy = st.builds(
    nuSMV::ParsExpression,
    isNext=
        st.booleans()
)
nuSMV::SetValueParameter_strategy = st.builds(
    nuSMV::SetValueParameter,
)
nuSMV::UnaryFunctionExpression_strategy = st.builds(
    nuSMV::UnaryFunctionExpression,
    function=
        safe_text
)
nuSMV::SetElementExpression_strategy = st.builds(
    nuSMV::SetElementExpression,
)
nuSMV::IntervalExpression_strategy = st.builds(
    nuSMV::IntervalExpression,
    lowerBound=
        safe_text,
    upperBound=
        safe_text
)
nuSMV::CaseSimpleExpression_strategy = st.builds(
    nuSMV::CaseSimpleExpression,
)
nuSMV::Val_strategy = st.builds(
    nuSMV::Val,
    num=
        safe_text,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
nuSMV::ModuleType_strategy = st.builds(
    nuSMV::ModuleType,
)
nuSMV::SimpleType_strategy = st.builds(
    nuSMV::SimpleType,
)
nuSMV::LTLExpression_strategy = st.builds(
    nuSMV::LTLExpression,
)
nuSMV::CTLExpression_strategy = st.builds(
    nuSMV::CTLExpression,
)
FairnessConstraint_strategy = st.builds(
    FairnessConstraint,
)
nuSMV::JusticeExpression_strategy = st.builds(
    nuSMV::JusticeExpression,
)
nuSMV::CompassionExpression_strategy = st.builds(
    nuSMV::CompassionExpression,
)
nuSMV::FairnessExpression_strategy = st.builds(
    nuSMV::FairnessExpression,
)
nuSMV::NextExpression_strategy = st.builds(
    nuSMV::NextExpression,
)
AssignBody_strategy = st.builds(
    AssignBody,
)
nuSMV::InitBody_strategy = st.builds(
    nuSMV::InitBody,
)
nuSMV::NextBody_strategy = st.builds(
    nuSMV::NextBody,
)
nuSMV::VarBodyAssign_strategy = st.builds(
    nuSMV::VarBodyAssign,
)
nuSMV::EObject_strategy = st.builds(
    nuSMV::EObject,
)
nuSMV::AssignBody_strategy = st.builds(
    nuSMV::AssignBody,
    array=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV::SimpleExpression_strategy = st.builds(
    nuSMV::SimpleExpression,
)
nuSMV::DefineBody_strategy = st.builds(
    nuSMV::DefineBody,
    var=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV::Type_strategy = st.builds(
    nuSMV::Type,
)
nuSMV::VarBody_strategy = st.builds(
    nuSMV::VarBody,
    name=
        safe_text,
    semicolon=
        st.booleans()
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
nuSMV::IsaDeclaration_strategy = st.builds(
    nuSMV::IsaDeclaration,
    id=
        safe_text
)
nuSMV::LtlSpecification_strategy = st.builds(
    nuSMV::LtlSpecification,
    name=
        safe_text,
    nameId=
        st.booleans(),
    semicolon=
        st.booleans()
)
nuSMV::InvarConstraint_strategy = st.builds(
    nuSMV::InvarConstraint,
    semicolon=
        st.booleans()
)
nuSMV::AssignConstraintElement_strategy = st.builds(
    nuSMV::AssignConstraintElement,
    assign=
        safe_text
)
nuSMV::IVariableDeclaration_strategy = st.builds(
    nuSMV::IVariableDeclaration,
)
nuSMV::DefineDeclaration_strategy = st.builds(
    nuSMV::DefineDeclaration,
    define=
        safe_text
)
nuSMV::InvarSpecification_strategy = st.builds(
    nuSMV::InvarSpecification,
    semicolon=
        st.booleans(),
    name=
        safe_text
)
nuSMV::ComputeSpecification_strategy = st.builds(
    nuSMV::ComputeSpecification,
    minMax=
        safe_text
)
nuSMV::CtlSpecification_strategy = st.builds(
    nuSMV::CtlSpecification,
    semicolon=
        st.booleans(),
    name=
        safe_text,
    nameKeyWord=
        st.booleans(),
    specKeyWord=
        safe_text
)
nuSMV::FairnessConstraint_strategy = st.builds(
    nuSMV::FairnessConstraint,
    semicolon=
        st.booleans()
)
nuSMV::FrozenVariableDeclaration_strategy = st.builds(
    nuSMV::FrozenVariableDeclaration,
)
nuSMV::ConstantsDeclaration_strategy = st.builds(
    nuSMV::ConstantsDeclaration,
    constants=
        safe_text,
    semicolon=
        st.booleans()
)
nuSMV::InitConstraint_strategy = st.builds(
    nuSMV::InitConstraint,
    semicolon=
        st.booleans()
)
nuSMV::TransConstraint_strategy = st.builds(
    nuSMV::TransConstraint,
    semicolon=
        st.booleans()
)
nuSMV::VariableDeclaration_strategy = st.builds(
    nuSMV::VariableDeclaration,
)
nuSMV::ModuleElement_strategy = st.builds(
    nuSMV::ModuleElement,
)
nuSMV::FormalParameter_strategy = st.builds(
    nuSMV::FormalParameter,
    name=
        safe_text
)
nuSMV::Module_strategy = st.builds(
    nuSMV::Module,
    name=
        safe_text
)
nuSMV::NuSmvModel_strategy = st.builds(
    nuSMV::NuSmvModel,
)

@given(instance=RTCTLExpression_strategy)
@settings(max_examples=50)
def test_rtctlexpression_instantiation(instance):
    assert isinstance(instance, RTCTLExpression)

@given(instance=nuSMV::UnaryRTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv::unaryrtctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::UnaryRTCTLExpression)

@given(instance=nuSMV::UnaryRTCTLExpression_strategy)
def test_nusmv::unaryrtctlexpression_unary_type(instance):
    assert isinstance(instance.unary, str)


@given(instance=nuSMV::UnaryRTCTLExpression_strategy)
def test_nusmv::unaryrtctlexpression_unary_setter(instance):
    original = instance.unary
    instance.unary = original
    assert instance.unary == original

@given(instance=nuSMV::SingleRTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv::singlertctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::SingleRTCTLExpression)

@given(instance=ModuleType_strategy)
@settings(max_examples=50)
def test_moduletype_instantiation(instance):
    assert isinstance(instance, ModuleType)

@given(instance=nuSMV::SyncrProcessType_strategy)
@settings(max_examples=50)
def test_nusmv::syncrprocesstype_instantiation(instance):
    assert isinstance(instance, nuSMV::SyncrProcessType)

@given(instance=nuSMV::AsyncrProcessType_strategy)
@settings(max_examples=50)
def test_nusmv::asyncrprocesstype_instantiation(instance):
    assert isinstance(instance, nuSMV::AsyncrProcessType)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=nuSMV::IntervalType_strategy)
@settings(max_examples=50)
def test_nusmv::intervaltype_instantiation(instance):
    assert isinstance(instance, nuSMV::IntervalType)

@given(instance=nuSMV::IntervalType_strategy)
def test_nusmv::intervaltype_low_type(instance):
    assert isinstance(instance.low, str)


@given(instance=nuSMV::IntervalType_strategy)
def test_nusmv::intervaltype_low_setter(instance):
    original = instance.low
    instance.low = original
    assert instance.low == original

@given(instance=nuSMV::IntervalType_strategy)
def test_nusmv::intervaltype_high_type(instance):
    assert isinstance(instance.high, str)


@given(instance=nuSMV::IntervalType_strategy)
def test_nusmv::intervaltype_high_setter(instance):
    original = instance.high
    instance.high = original
    assert instance.high == original

@given(instance=nuSMV::SignedWordType_strategy)
@settings(max_examples=50)
def test_nusmv::signedwordtype_instantiation(instance):
    assert isinstance(instance, nuSMV::SignedWordType)

@given(instance=nuSMV::SignedWordType_strategy)
def test_nusmv::signedwordtype_signedNumber_type(instance):
    assert isinstance(instance.signedNumber, str)


@given(instance=nuSMV::SignedWordType_strategy)
def test_nusmv::signedwordtype_signedNumber_setter(instance):
    original = instance.signedNumber
    instance.signedNumber = original
    assert instance.signedNumber == original

@given(instance=nuSMV::EnumType_strategy)
@settings(max_examples=50)
def test_nusmv::enumtype_instantiation(instance):
    assert isinstance(instance, nuSMV::EnumType)

@given(instance=nuSMV::UnsignedWordType_strategy)
@settings(max_examples=50)
def test_nusmv::unsignedwordtype_instantiation(instance):
    assert isinstance(instance, nuSMV::UnsignedWordType)

@given(instance=nuSMV::UnsignedWordType_strategy)
def test_nusmv::unsignedwordtype_uWordNumber_type(instance):
    assert isinstance(instance.uWordNumber, str)


@given(instance=nuSMV::UnsignedWordType_strategy)
def test_nusmv::unsignedwordtype_uWordNumber_setter(instance):
    original = instance.uWordNumber
    instance.uWordNumber = original
    assert instance.uWordNumber == original

@given(instance=nuSMV::ArrayType_strategy)
@settings(max_examples=50)
def test_nusmv::arraytype_instantiation(instance):
    assert isinstance(instance, nuSMV::ArrayType)

@given(instance=nuSMV::ArrayType_strategy)
def test_nusmv::arraytype_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=nuSMV::ArrayType_strategy)
def test_nusmv::arraytype_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=nuSMV::ArrayType_strategy)
def test_nusmv::arraytype_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=nuSMV::ArrayType_strategy)
def test_nusmv::arraytype_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=nuSMV::WordType_strategy)
@settings(max_examples=50)
def test_nusmv::wordtype_instantiation(instance):
    assert isinstance(instance, nuSMV::WordType)

@given(instance=nuSMV::WordType_strategy)
def test_nusmv::wordtype_wordNumber_type(instance):
    assert isinstance(instance.wordNumber, str)


@given(instance=nuSMV::WordType_strategy)
def test_nusmv::wordtype_wordNumber_setter(instance):
    original = instance.wordNumber
    instance.wordNumber = original
    assert instance.wordNumber == original

@given(instance=nuSMV::BooleanType_strategy)
@settings(max_examples=50)
def test_nusmv::booleantype_instantiation(instance):
    assert isinstance(instance, nuSMV::BooleanType)

@given(instance=nuSMV::RTCTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv::rtctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::RTCTLExpression)

@given(instance=nuSMV::RangeExpression_strategy)
@settings(max_examples=50)
def test_nusmv::rangeexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::RangeExpression)

@given(instance=nuSMV::RangeExpression_strategy)
def test_nusmv::rangeexpression_lower_type(instance):
    assert isinstance(instance.lower, str)


@given(instance=nuSMV::RangeExpression_strategy)
def test_nusmv::rangeexpression_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=nuSMV::RangeExpression_strategy)
def test_nusmv::rangeexpression_upper_type(instance):
    assert isinstance(instance.upper, str)


@given(instance=nuSMV::RangeExpression_strategy)
def test_nusmv::rangeexpression_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=nuSMV::CaseSimpleAssignementExpression_strategy)
@settings(max_examples=50)
def test_nusmv::casesimpleassignementexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::CaseSimpleAssignementExpression)

@given(instance=SimpleExpression_strategy)
@settings(max_examples=50)
def test_simpleexpression_instantiation(instance):
    assert isinstance(instance, SimpleExpression)

@given(instance=nuSMV::UnaryExpression_strategy)
@settings(max_examples=50)
def test_nusmv::unaryexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::UnaryExpression)

@given(instance=nuSMV::UnaryExpression_strategy)
def test_nusmv::unaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=nuSMV::UnaryExpression_strategy)
def test_nusmv::unaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=nuSMV::BinaryExpression_strategy)
@settings(max_examples=50)
def test_nusmv::binaryexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::BinaryExpression)

@given(instance=nuSMV::BinaryExpression_strategy)
def test_nusmv::binaryexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=nuSMV::BinaryExpression_strategy)
def test_nusmv::binaryexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=nuSMV::BinaryExpression_strategy)
def test_nusmv::binaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=nuSMV::BinaryExpression_strategy)
def test_nusmv::binaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=nuSMV::UntilCTLexpression_strategy)
@settings(max_examples=50)
def test_nusmv::untilctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::UntilCTLexpression)

@given(instance=nuSMV::UntilCTLexpression_strategy)
def test_nusmv::untilctlexpression_ea_type(instance):
    assert isinstance(instance.ea, str)


@given(instance=nuSMV::UntilCTLexpression_strategy)
def test_nusmv::untilctlexpression_ea_setter(instance):
    original = instance.ea
    instance.ea = original
    assert instance.ea == original

@given(instance=nuSMV::Not_strategy)
@settings(max_examples=50)
def test_nusmv::not_instantiation(instance):
    assert isinstance(instance, nuSMV::Not)

@given(instance=nuSMV::Var_strategy)
@settings(max_examples=50)
def test_nusmv::var_instantiation(instance):
    assert isinstance(instance, nuSMV::Var)

@given(instance=nuSMV::WordExpression_strategy)
@settings(max_examples=50)
def test_nusmv::wordexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::WordExpression)

@given(instance=nuSMV::WordExpression_strategy)
def test_nusmv::wordexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=nuSMV::WordExpression_strategy)
def test_nusmv::wordexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nuSMV::SetExpression_strategy)
@settings(max_examples=50)
def test_nusmv::setexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::SetExpression)

@given(instance=nuSMV::ValueExpression_strategy)
@settings(max_examples=50)
def test_nusmv::valueexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::ValueExpression)

@given(instance=nuSMV::ValueExpression_strategy)
def test_nusmv::valueexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=nuSMV::ValueExpression_strategy)
def test_nusmv::valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=nuSMV::ParsExpression_strategy)
@settings(max_examples=50)
def test_nusmv::parsexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::ParsExpression)

@given(instance=nuSMV::ParsExpression_strategy)
def test_nusmv::parsexpression_isNext_type(instance):
    assert isinstance(instance.isNext, bool)


@given(instance=nuSMV::ParsExpression_strategy)
def test_nusmv::parsexpression_isNext_setter(instance):
    original = instance.isNext
    instance.isNext = original
    assert instance.isNext == original

@given(instance=nuSMV::SetValueParameter_strategy)
@settings(max_examples=50)
def test_nusmv::setvalueparameter_instantiation(instance):
    assert isinstance(instance, nuSMV::SetValueParameter)

@given(instance=nuSMV::UnaryFunctionExpression_strategy)
@settings(max_examples=50)
def test_nusmv::unaryfunctionexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::UnaryFunctionExpression)

@given(instance=nuSMV::UnaryFunctionExpression_strategy)
def test_nusmv::unaryfunctionexpression_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=nuSMV::UnaryFunctionExpression_strategy)
def test_nusmv::unaryfunctionexpression_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=nuSMV::SetElementExpression_strategy)
@settings(max_examples=50)
def test_nusmv::setelementexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::SetElementExpression)

@given(instance=nuSMV::IntervalExpression_strategy)
@settings(max_examples=50)
def test_nusmv::intervalexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::IntervalExpression)

@given(instance=nuSMV::IntervalExpression_strategy)
def test_nusmv::intervalexpression_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, str)


@given(instance=nuSMV::IntervalExpression_strategy)
def test_nusmv::intervalexpression_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=nuSMV::IntervalExpression_strategy)
def test_nusmv::intervalexpression_upperBound_type(instance):
    assert isinstance(instance.upperBound, str)


@given(instance=nuSMV::IntervalExpression_strategy)
def test_nusmv::intervalexpression_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=nuSMV::CaseSimpleExpression_strategy)
@settings(max_examples=50)
def test_nusmv::casesimpleexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::CaseSimpleExpression)

@given(instance=nuSMV::Val_strategy)
@settings(max_examples=50)
def test_nusmv::val_instantiation(instance):
    assert isinstance(instance, nuSMV::Val)

@given(instance=nuSMV::Val_strategy)
def test_nusmv::val_num_type(instance):
    assert isinstance(instance.num, str)


@given(instance=nuSMV::Val_strategy)
def test_nusmv::val_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=nuSMV::Val_strategy)
def test_nusmv::val_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::Val_strategy)
def test_nusmv::val_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=nuSMV::ModuleType_strategy)
@settings(max_examples=50)
def test_nusmv::moduletype_instantiation(instance):
    assert isinstance(instance, nuSMV::ModuleType)

@given(instance=nuSMV::SimpleType_strategy)
@settings(max_examples=50)
def test_nusmv::simpletype_instantiation(instance):
    assert isinstance(instance, nuSMV::SimpleType)

@given(instance=nuSMV::LTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv::ltlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::LTLExpression)

@given(instance=nuSMV::CTLExpression_strategy)
@settings(max_examples=50)
def test_nusmv::ctlexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::CTLExpression)

@given(instance=FairnessConstraint_strategy)
@settings(max_examples=50)
def test_fairnessconstraint_instantiation(instance):
    assert isinstance(instance, FairnessConstraint)

@given(instance=nuSMV::JusticeExpression_strategy)
@settings(max_examples=50)
def test_nusmv::justiceexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::JusticeExpression)

@given(instance=nuSMV::CompassionExpression_strategy)
@settings(max_examples=50)
def test_nusmv::compassionexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::CompassionExpression)

@given(instance=nuSMV::FairnessExpression_strategy)
@settings(max_examples=50)
def test_nusmv::fairnessexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::FairnessExpression)

@given(instance=nuSMV::NextExpression_strategy)
@settings(max_examples=50)
def test_nusmv::nextexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::NextExpression)

@given(instance=AssignBody_strategy)
@settings(max_examples=50)
def test_assignbody_instantiation(instance):
    assert isinstance(instance, AssignBody)

@given(instance=nuSMV::InitBody_strategy)
@settings(max_examples=50)
def test_nusmv::initbody_instantiation(instance):
    assert isinstance(instance, nuSMV::InitBody)

@given(instance=nuSMV::NextBody_strategy)
@settings(max_examples=50)
def test_nusmv::nextbody_instantiation(instance):
    assert isinstance(instance, nuSMV::NextBody)

@given(instance=nuSMV::VarBodyAssign_strategy)
@settings(max_examples=50)
def test_nusmv::varbodyassign_instantiation(instance):
    assert isinstance(instance, nuSMV::VarBodyAssign)

@given(instance=nuSMV::EObject_strategy)
@settings(max_examples=50)
def test_nusmv::eobject_instantiation(instance):
    assert isinstance(instance, nuSMV::EObject)

@given(instance=nuSMV::AssignBody_strategy)
@settings(max_examples=50)
def test_nusmv::assignbody_instantiation(instance):
    assert isinstance(instance, nuSMV::AssignBody)

@given(instance=nuSMV::AssignBody_strategy)
def test_nusmv::assignbody_array_type(instance):
    assert isinstance(instance.array, str)


@given(instance=nuSMV::AssignBody_strategy)
def test_nusmv::assignbody_array_setter(instance):
    original = instance.array
    instance.array = original
    assert instance.array == original

@given(instance=nuSMV::AssignBody_strategy)
def test_nusmv::assignbody_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::AssignBody_strategy)
def test_nusmv::assignbody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::SimpleExpression_strategy)
@settings(max_examples=50)
def test_nusmv::simpleexpression_instantiation(instance):
    assert isinstance(instance, nuSMV::SimpleExpression)

@given(instance=nuSMV::DefineBody_strategy)
@settings(max_examples=50)
def test_nusmv::definebody_instantiation(instance):
    assert isinstance(instance, nuSMV::DefineBody)

@given(instance=nuSMV::DefineBody_strategy)
def test_nusmv::definebody_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=nuSMV::DefineBody_strategy)
def test_nusmv::definebody_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=nuSMV::DefineBody_strategy)
def test_nusmv::definebody_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::DefineBody_strategy)
def test_nusmv::definebody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::Type_strategy)
@settings(max_examples=50)
def test_nusmv::type_instantiation(instance):
    assert isinstance(instance, nuSMV::Type)

@given(instance=nuSMV::VarBody_strategy)
@settings(max_examples=50)
def test_nusmv::varbody_instantiation(instance):
    assert isinstance(instance, nuSMV::VarBody)

@given(instance=nuSMV::VarBody_strategy)
def test_nusmv::varbody_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::VarBody_strategy)
def test_nusmv::varbody_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::VarBody_strategy)
def test_nusmv::varbody_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::VarBody_strategy)
def test_nusmv::varbody_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=nuSMV::IsaDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::isadeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::IsaDeclaration)

@given(instance=nuSMV::IsaDeclaration_strategy)
def test_nusmv::isadeclaration_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=nuSMV::IsaDeclaration_strategy)
def test_nusmv::isadeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=nuSMV::LtlSpecification_strategy)
@settings(max_examples=50)
def test_nusmv::ltlspecification_instantiation(instance):
    assert isinstance(instance, nuSMV::LtlSpecification)

@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_nameId_type(instance):
    assert isinstance(instance.nameId, bool)


@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_nameId_setter(instance):
    original = instance.nameId
    instance.nameId = original
    assert instance.nameId == original

@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::LtlSpecification_strategy)
def test_nusmv::ltlspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::InvarConstraint_strategy)
@settings(max_examples=50)
def test_nusmv::invarconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV::InvarConstraint)

@given(instance=nuSMV::InvarConstraint_strategy)
def test_nusmv::invarconstraint_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::InvarConstraint_strategy)
def test_nusmv::invarconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::AssignConstraintElement_strategy)
@settings(max_examples=50)
def test_nusmv::assignconstraintelement_instantiation(instance):
    assert isinstance(instance, nuSMV::AssignConstraintElement)

@given(instance=nuSMV::AssignConstraintElement_strategy)
def test_nusmv::assignconstraintelement_assign_type(instance):
    assert isinstance(instance.assign, str)


@given(instance=nuSMV::AssignConstraintElement_strategy)
def test_nusmv::assignconstraintelement_assign_setter(instance):
    original = instance.assign
    instance.assign = original
    assert instance.assign == original

@given(instance=nuSMV::IVariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::ivariabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::IVariableDeclaration)

@given(instance=nuSMV::DefineDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::definedeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::DefineDeclaration)

@given(instance=nuSMV::DefineDeclaration_strategy)
def test_nusmv::definedeclaration_define_type(instance):
    assert isinstance(instance.define, str)


@given(instance=nuSMV::DefineDeclaration_strategy)
def test_nusmv::definedeclaration_define_setter(instance):
    original = instance.define
    instance.define = original
    assert instance.define == original

@given(instance=nuSMV::InvarSpecification_strategy)
@settings(max_examples=50)
def test_nusmv::invarspecification_instantiation(instance):
    assert isinstance(instance, nuSMV::InvarSpecification)

@given(instance=nuSMV::InvarSpecification_strategy)
def test_nusmv::invarspecification_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::InvarSpecification_strategy)
def test_nusmv::invarspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::InvarSpecification_strategy)
def test_nusmv::invarspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::InvarSpecification_strategy)
def test_nusmv::invarspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::ComputeSpecification_strategy)
@settings(max_examples=50)
def test_nusmv::computespecification_instantiation(instance):
    assert isinstance(instance, nuSMV::ComputeSpecification)

@given(instance=nuSMV::ComputeSpecification_strategy)
def test_nusmv::computespecification_minMax_type(instance):
    assert isinstance(instance.minMax, str)


@given(instance=nuSMV::ComputeSpecification_strategy)
def test_nusmv::computespecification_minMax_setter(instance):
    original = instance.minMax
    instance.minMax = original
    assert instance.minMax == original

@given(instance=nuSMV::CtlSpecification_strategy)
@settings(max_examples=50)
def test_nusmv::ctlspecification_instantiation(instance):
    assert isinstance(instance, nuSMV::CtlSpecification)

@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_nameKeyWord_type(instance):
    assert isinstance(instance.nameKeyWord, bool)


@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_nameKeyWord_setter(instance):
    original = instance.nameKeyWord
    instance.nameKeyWord = original
    assert instance.nameKeyWord == original

@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_specKeyWord_type(instance):
    assert isinstance(instance.specKeyWord, str)


@given(instance=nuSMV::CtlSpecification_strategy)
def test_nusmv::ctlspecification_specKeyWord_setter(instance):
    original = instance.specKeyWord
    instance.specKeyWord = original
    assert instance.specKeyWord == original

@given(instance=nuSMV::FairnessConstraint_strategy)
@settings(max_examples=50)
def test_nusmv::fairnessconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV::FairnessConstraint)

@given(instance=nuSMV::FairnessConstraint_strategy)
def test_nusmv::fairnessconstraint_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::FairnessConstraint_strategy)
def test_nusmv::fairnessconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::FrozenVariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::frozenvariabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::FrozenVariableDeclaration)

@given(instance=nuSMV::ConstantsDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::constantsdeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::ConstantsDeclaration)

@given(instance=nuSMV::ConstantsDeclaration_strategy)
def test_nusmv::constantsdeclaration_constants_type(instance):
    assert isinstance(instance.constants, str)


@given(instance=nuSMV::ConstantsDeclaration_strategy)
def test_nusmv::constantsdeclaration_constants_setter(instance):
    original = instance.constants
    instance.constants = original
    assert instance.constants == original

@given(instance=nuSMV::ConstantsDeclaration_strategy)
def test_nusmv::constantsdeclaration_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::ConstantsDeclaration_strategy)
def test_nusmv::constantsdeclaration_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::InitConstraint_strategy)
@settings(max_examples=50)
def test_nusmv::initconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV::InitConstraint)

@given(instance=nuSMV::InitConstraint_strategy)
def test_nusmv::initconstraint_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::InitConstraint_strategy)
def test_nusmv::initconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::TransConstraint_strategy)
@settings(max_examples=50)
def test_nusmv::transconstraint_instantiation(instance):
    assert isinstance(instance, nuSMV::TransConstraint)

@given(instance=nuSMV::TransConstraint_strategy)
def test_nusmv::transconstraint_semicolon_type(instance):
    assert isinstance(instance.semicolon, bool)


@given(instance=nuSMV::TransConstraint_strategy)
def test_nusmv::transconstraint_semicolon_setter(instance):
    original = instance.semicolon
    instance.semicolon = original
    assert instance.semicolon == original

@given(instance=nuSMV::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_nusmv::variabledeclaration_instantiation(instance):
    assert isinstance(instance, nuSMV::VariableDeclaration)

@given(instance=nuSMV::ModuleElement_strategy)
@settings(max_examples=50)
def test_nusmv::moduleelement_instantiation(instance):
    assert isinstance(instance, nuSMV::ModuleElement)

@given(instance=nuSMV::FormalParameter_strategy)
@settings(max_examples=50)
def test_nusmv::formalparameter_instantiation(instance):
    assert isinstance(instance, nuSMV::FormalParameter)

@given(instance=nuSMV::FormalParameter_strategy)
def test_nusmv::formalparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::FormalParameter_strategy)
def test_nusmv::formalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::Module_strategy)
@settings(max_examples=50)
def test_nusmv::module_instantiation(instance):
    assert isinstance(instance, nuSMV::Module)

@given(instance=nuSMV::Module_strategy)
def test_nusmv::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nuSMV::Module_strategy)
def test_nusmv::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nuSMV::NuSmvModel_strategy)
@settings(max_examples=50)
def test_nusmv::nusmvmodel_instantiation(instance):
    assert isinstance(instance, nuSMV::NuSmvModel)
