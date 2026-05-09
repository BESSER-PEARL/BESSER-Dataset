import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ptnet::Variable,
    BooleanExpression,
    ptnet::OpOr,
    ptnet::OpAnd,
    ComparisonOperator,
    ptnet::OpLessEqual,
    ptnet::OpLess,
    ptnet::OpGreaterEqual,
    ptnet::OpGreater,
    ptnet::OpEqual,
    EvaluationType,
    ptnet::InstantOfTime,
    ptnet::IntervalOfTime,
    ptnet::IntervalOfTimeAveraged,
    ptnet::SteadyState,
    ArithmeticBinaryOperator,
    ptnet::OpMultiply,
    ptnet::OpMinus,
    ptnet::OpDivide,
    ptnet::OpSum,
    LogicalExpression,
    ptnet::BooleanExpression,
    ptnet::OpFalse,
    ptnet::OpNot,
    ptnet::ComparisonOperator,
    ptnet::OpTrue,
    ptnet::EvaluationType,
    ptnet::VariableValues,
    ptnet::Measure,
    ptnet::Study,
    ptnet::EvaluationList,
    Expression,
    ArithmeticExpression,
    ptnet::ArithmeticBinaryOperator,
    ptnet::VariableExpression,
    ptnet::IfThenElse,
    ptnet::MarkingExpression,
    ptnet::ValueExpression,
    ptnet::Expression,
    Distribution,
    ptnet::Gaussian,
    ptnet::Exponential,
    ptnet::Deterministic,
    ptnet::Distribution,
    GSPNTransition,
    ptnet::GSPNTimedTransition,
    ptnet::GSPNImmediateTransition,
    ptnet::ArithmeticExpression,
    ptnet::Weibull,
    ptnet::Gamma,
    ptnet::Uniform,
    Label,
    ptnet::Attribute,
    Arc,
    ptnet::GSPNArc,
    ptnet::LogicalExpression,
    Transition,
    ptnet::GSPNTransition,
    Node,
    ptnet::TransitionNode,
    ptnet::PlaceNode,
    TransitionNode,
    ptnet::RefTransition,
    ptnet::Transition,
    PlaceNode,
    ptnet::RefPlace,
    ptnet::Annotation,
    ptnet::Font,
    ptnet::Graphics,
    ptnet::Line,
    Coordinate,
    ptnet::Offset,
    ptnet::Coordinate,
    ptnet::AnyObject,
    ptnet::Label,
    ptnet::Fill,
    ptnet::Dimension,
    ptnet::Position,
    Graphics,
    ptnet::ArcGraphics,
    ptnet::AnnotationGraphics,
    ptnet::NodeGraphics,
    ptnet::PnObject,
    ptnet::PetriNet,
    ptnet::PetriNetDoc,
    ptnet::Place,
    PnObject,
    ptnet::Page,
    ptnet::Node,
    ptnet::Arc,
    ptnet::ToolInfo,
    Annotation,
    ptnet::Name,
    ptnet::PTArcAnnotation,
    ptnet::PTMarking,
    GSPNArcType,
    LineShape,
    CSS2Color,
    GSPNTransitionType,
    LineStyle,
    CSS2FontStyle,
    FontAlign,
    CSS2FontFamily,
    Gradient,
    CSS2FontWeight,
    FontDecoration,
    PNType,
    CSS2FontSize,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ptnet::variable_is_not_abstract():
    assert not inspect.isabstract(ptnet::Variable)


def test_ptnet::variable_constructor_exists():
    assert callable(ptnet::Variable.__init__)


def test_ptnet::variable_constructor_args():
    sig = inspect.signature(ptnet::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet::variable_has_name():
    assert hasattr(ptnet::Variable, "name")
    descriptor = None
    for klass in ptnet::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(BooleanExpression)


def test_booleanexpression_constructor_exists():
    assert callable(BooleanExpression.__init__)


def test_booleanexpression_constructor_args():
    sig = inspect.signature(BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opor_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpOr)


def test_ptnet::opor_constructor_exists():
    assert callable(ptnet::OpOr.__init__)


def test_ptnet::opor_constructor_args():
    sig = inspect.signature(ptnet::OpOr.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opand_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpAnd)


def test_ptnet::opand_constructor_exists():
    assert callable(ptnet::OpAnd.__init__)


def test_ptnet::opand_constructor_args():
    sig = inspect.signature(ptnet::OpAnd.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperator)


def test_comparisonoperator_constructor_exists():
    assert callable(ComparisonOperator.__init__)


def test_comparisonoperator_constructor_args():
    sig = inspect.signature(ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::oplessequal_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpLessEqual)


def test_ptnet::oplessequal_constructor_exists():
    assert callable(ptnet::OpLessEqual.__init__)


def test_ptnet::oplessequal_constructor_args():
    sig = inspect.signature(ptnet::OpLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opless_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpLess)


def test_ptnet::opless_constructor_exists():
    assert callable(ptnet::OpLess.__init__)


def test_ptnet::opless_constructor_args():
    sig = inspect.signature(ptnet::OpLess.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opgreaterequal_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpGreaterEqual)


def test_ptnet::opgreaterequal_constructor_exists():
    assert callable(ptnet::OpGreaterEqual.__init__)


def test_ptnet::opgreaterequal_constructor_args():
    sig = inspect.signature(ptnet::OpGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opgreater_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpGreater)


def test_ptnet::opgreater_constructor_exists():
    assert callable(ptnet::OpGreater.__init__)


def test_ptnet::opgreater_constructor_args():
    sig = inspect.signature(ptnet::OpGreater.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opequal_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpEqual)


def test_ptnet::opequal_constructor_exists():
    assert callable(ptnet::OpEqual.__init__)


def test_ptnet::opequal_constructor_args():
    sig = inspect.signature(ptnet::OpEqual.__init__)
    params = list(sig.parameters.keys())



def test_evaluationtype_is_not_abstract():
    assert not inspect.isabstract(EvaluationType)


def test_evaluationtype_constructor_exists():
    assert callable(EvaluationType.__init__)


def test_evaluationtype_constructor_args():
    sig = inspect.signature(EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::instantoftime_is_not_abstract():
    assert not inspect.isabstract(ptnet::InstantOfTime)


def test_ptnet::instantoftime_constructor_exists():
    assert callable(ptnet::InstantOfTime.__init__)


def test_ptnet::instantoftime_constructor_args():
    sig = inspect.signature(ptnet::InstantOfTime.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::intervaloftime_is_not_abstract():
    assert not inspect.isabstract(ptnet::IntervalOfTime)


def test_ptnet::intervaloftime_constructor_exists():
    assert callable(ptnet::IntervalOfTime.__init__)


def test_ptnet::intervaloftime_constructor_args():
    sig = inspect.signature(ptnet::IntervalOfTime.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::intervaloftimeaveraged_is_not_abstract():
    assert not inspect.isabstract(ptnet::IntervalOfTimeAveraged)


def test_ptnet::intervaloftimeaveraged_constructor_exists():
    assert callable(ptnet::IntervalOfTimeAveraged.__init__)


def test_ptnet::intervaloftimeaveraged_constructor_args():
    sig = inspect.signature(ptnet::IntervalOfTimeAveraged.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::steadystate_is_not_abstract():
    assert not inspect.isabstract(ptnet::SteadyState)


def test_ptnet::steadystate_constructor_exists():
    assert callable(ptnet::SteadyState.__init__)


def test_ptnet::steadystate_constructor_args():
    sig = inspect.signature(ptnet::SteadyState.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticBinaryOperator)


def test_arithmeticbinaryoperator_constructor_exists():
    assert callable(ArithmeticBinaryOperator.__init__)


def test_arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opmultiply_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpMultiply)


def test_ptnet::opmultiply_constructor_exists():
    assert callable(ptnet::OpMultiply.__init__)


def test_ptnet::opmultiply_constructor_args():
    sig = inspect.signature(ptnet::OpMultiply.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opminus_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpMinus)


def test_ptnet::opminus_constructor_exists():
    assert callable(ptnet::OpMinus.__init__)


def test_ptnet::opminus_constructor_args():
    sig = inspect.signature(ptnet::OpMinus.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opdivide_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpDivide)


def test_ptnet::opdivide_constructor_exists():
    assert callable(ptnet::OpDivide.__init__)


def test_ptnet::opdivide_constructor_args():
    sig = inspect.signature(ptnet::OpDivide.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opsum_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpSum)


def test_ptnet::opsum_constructor_exists():
    assert callable(ptnet::OpSum.__init__)


def test_ptnet::opsum_constructor_args():
    sig = inspect.signature(ptnet::OpSum.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::BooleanExpression)


def test_ptnet::booleanexpression_constructor_exists():
    assert callable(ptnet::BooleanExpression.__init__)


def test_ptnet::booleanexpression_constructor_args():
    sig = inspect.signature(ptnet::BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opfalse_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpFalse)


def test_ptnet::opfalse_constructor_exists():
    assert callable(ptnet::OpFalse.__init__)


def test_ptnet::opfalse_constructor_args():
    sig = inspect.signature(ptnet::OpFalse.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::opnot_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpNot)


def test_ptnet::opnot_constructor_exists():
    assert callable(ptnet::OpNot.__init__)


def test_ptnet::opnot_constructor_args():
    sig = inspect.signature(ptnet::OpNot.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet::ComparisonOperator)


def test_ptnet::comparisonoperator_constructor_exists():
    assert callable(ptnet::ComparisonOperator.__init__)


def test_ptnet::comparisonoperator_constructor_args():
    sig = inspect.signature(ptnet::ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::optrue_is_not_abstract():
    assert not inspect.isabstract(ptnet::OpTrue)


def test_ptnet::optrue_constructor_exists():
    assert callable(ptnet::OpTrue.__init__)


def test_ptnet::optrue_constructor_args():
    sig = inspect.signature(ptnet::OpTrue.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::evaluationtype_is_not_abstract():
    assert not inspect.isabstract(ptnet::EvaluationType)


def test_ptnet::evaluationtype_constructor_exists():
    assert callable(ptnet::EvaluationType.__init__)


def test_ptnet::evaluationtype_constructor_args():
    sig = inspect.signature(ptnet::EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::variablevalues_is_not_abstract():
    assert not inspect.isabstract(ptnet::VariableValues)


def test_ptnet::variablevalues_constructor_exists():
    assert callable(ptnet::VariableValues.__init__)


def test_ptnet::variablevalues_constructor_args():
    sig = inspect.signature(ptnet::VariableValues.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_ptnet::variablevalues_has_values():
    assert hasattr(ptnet::VariableValues, "values")
    descriptor = None
    for klass in ptnet::VariableValues.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::measure_is_not_abstract():
    assert not inspect.isabstract(ptnet::Measure)


def test_ptnet::measure_constructor_exists():
    assert callable(ptnet::Measure.__init__)


def test_ptnet::measure_constructor_args():
    sig = inspect.signature(ptnet::Measure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet::measure_has_name():
    assert hasattr(ptnet::Measure, "name")
    descriptor = None
    for klass in ptnet::Measure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::study_is_not_abstract():
    assert not inspect.isabstract(ptnet::Study)


def test_ptnet::study_constructor_exists():
    assert callable(ptnet::Study.__init__)


def test_ptnet::study_constructor_args():
    sig = inspect.signature(ptnet::Study.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet::study_has_name():
    assert hasattr(ptnet::Study, "name")
    descriptor = None
    for klass in ptnet::Study.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::evaluationlist_is_not_abstract():
    assert not inspect.isabstract(ptnet::EvaluationList)


def test_ptnet::evaluationlist_constructor_exists():
    assert callable(ptnet::EvaluationList.__init__)


def test_ptnet::evaluationlist_constructor_args():
    sig = inspect.signature(ptnet::EvaluationList.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet::ArithmeticBinaryOperator)


def test_ptnet::arithmeticbinaryoperator_constructor_exists():
    assert callable(ptnet::ArithmeticBinaryOperator.__init__)


def test_ptnet::arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ptnet::ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::variableexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::VariableExpression)


def test_ptnet::variableexpression_constructor_exists():
    assert callable(ptnet::VariableExpression.__init__)


def test_ptnet::variableexpression_constructor_args():
    sig = inspect.signature(ptnet::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(ptnet::IfThenElse)


def test_ptnet::ifthenelse_constructor_exists():
    assert callable(ptnet::IfThenElse.__init__)


def test_ptnet::ifthenelse_constructor_args():
    sig = inspect.signature(ptnet::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::markingexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::MarkingExpression)


def test_ptnet::markingexpression_constructor_exists():
    assert callable(ptnet::MarkingExpression.__init__)


def test_ptnet::markingexpression_constructor_args():
    sig = inspect.signature(ptnet::MarkingExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::valueexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::ValueExpression)


def test_ptnet::valueexpression_constructor_exists():
    assert callable(ptnet::ValueExpression.__init__)


def test_ptnet::valueexpression_constructor_args():
    sig = inspect.signature(ptnet::ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ptnet::valueexpression_has_value():
    assert hasattr(ptnet::ValueExpression, "value")
    descriptor = None
    for klass in ptnet::ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::expression_is_not_abstract():
    assert not inspect.isabstract(ptnet::Expression)


def test_ptnet::expression_constructor_exists():
    assert callable(ptnet::Expression.__init__)


def test_ptnet::expression_constructor_args():
    sig = inspect.signature(ptnet::Expression.__init__)
    params = list(sig.parameters.keys())



def test_distribution_is_not_abstract():
    assert not inspect.isabstract(Distribution)


def test_distribution_constructor_exists():
    assert callable(Distribution.__init__)


def test_distribution_constructor_args():
    sig = inspect.signature(Distribution.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::gaussian_is_not_abstract():
    assert not inspect.isabstract(ptnet::Gaussian)


def test_ptnet::gaussian_constructor_exists():
    assert callable(ptnet::Gaussian.__init__)


def test_ptnet::gaussian_constructor_args():
    sig = inspect.signature(ptnet::Gaussian.__init__)
    params = list(sig.parameters.keys())
    assert "Variance" in params, "Missing parameter 'Variance'"
    assert "Mean" in params, "Missing parameter 'Mean'"

def test_ptnet::gaussian_has_Variance():
    assert hasattr(ptnet::Gaussian, "Variance")
    descriptor = None
    for klass in ptnet::Gaussian.__mro__:
        if "Variance" in klass.__dict__:
            descriptor = klass.__dict__["Variance"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::gaussian_has_Mean():
    assert hasattr(ptnet::Gaussian, "Mean")
    descriptor = None
    for klass in ptnet::Gaussian.__mro__:
        if "Mean" in klass.__dict__:
            descriptor = klass.__dict__["Mean"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::exponential_is_not_abstract():
    assert not inspect.isabstract(ptnet::Exponential)


def test_ptnet::exponential_constructor_exists():
    assert callable(ptnet::Exponential.__init__)


def test_ptnet::exponential_constructor_args():
    sig = inspect.signature(ptnet::Exponential.__init__)
    params = list(sig.parameters.keys())
    assert "Rate" in params, "Missing parameter 'Rate'"

def test_ptnet::exponential_has_Rate():
    assert hasattr(ptnet::Exponential, "Rate")
    descriptor = None
    for klass in ptnet::Exponential.__mro__:
        if "Rate" in klass.__dict__:
            descriptor = klass.__dict__["Rate"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::deterministic_is_not_abstract():
    assert not inspect.isabstract(ptnet::Deterministic)


def test_ptnet::deterministic_constructor_exists():
    assert callable(ptnet::Deterministic.__init__)


def test_ptnet::deterministic_constructor_args():
    sig = inspect.signature(ptnet::Deterministic.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_ptnet::deterministic_has_Value():
    assert hasattr(ptnet::Deterministic, "Value")
    descriptor = None
    for klass in ptnet::Deterministic.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::distribution_is_not_abstract():
    assert not inspect.isabstract(ptnet::Distribution)


def test_ptnet::distribution_constructor_exists():
    assert callable(ptnet::Distribution.__init__)


def test_ptnet::distribution_constructor_args():
    sig = inspect.signature(ptnet::Distribution.__init__)
    params = list(sig.parameters.keys())



def test_gspntransition_is_not_abstract():
    assert not inspect.isabstract(GSPNTransition)


def test_gspntransition_constructor_exists():
    assert callable(GSPNTransition.__init__)


def test_gspntransition_constructor_args():
    sig = inspect.signature(GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::gspntimedtransition_is_not_abstract():
    assert not inspect.isabstract(ptnet::GSPNTimedTransition)


def test_ptnet::gspntimedtransition_constructor_exists():
    assert callable(ptnet::GSPNTimedTransition.__init__)


def test_ptnet::gspntimedtransition_constructor_args():
    sig = inspect.signature(ptnet::GSPNTimedTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::gspnimmediatetransition_is_not_abstract():
    assert not inspect.isabstract(ptnet::GSPNImmediateTransition)


def test_ptnet::gspnimmediatetransition_constructor_exists():
    assert callable(ptnet::GSPNImmediateTransition.__init__)


def test_ptnet::gspnimmediatetransition_constructor_args():
    sig = inspect.signature(ptnet::GSPNImmediateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "Weight" in params, "Missing parameter 'Weight'"
    assert "Priority" in params, "Missing parameter 'Priority'"

def test_ptnet::gspnimmediatetransition_has_Weight():
    assert hasattr(ptnet::GSPNImmediateTransition, "Weight")
    descriptor = None
    for klass in ptnet::GSPNImmediateTransition.__mro__:
        if "Weight" in klass.__dict__:
            descriptor = klass.__dict__["Weight"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::gspnimmediatetransition_has_Priority():
    assert hasattr(ptnet::GSPNImmediateTransition, "Priority")
    descriptor = None
    for klass in ptnet::GSPNImmediateTransition.__mro__:
        if "Priority" in klass.__dict__:
            descriptor = klass.__dict__["Priority"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::ArithmeticExpression)


def test_ptnet::arithmeticexpression_constructor_exists():
    assert callable(ptnet::ArithmeticExpression.__init__)


def test_ptnet::arithmeticexpression_constructor_args():
    sig = inspect.signature(ptnet::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::weibull_is_not_abstract():
    assert not inspect.isabstract(ptnet::Weibull)


def test_ptnet::weibull_constructor_exists():
    assert callable(ptnet::Weibull.__init__)


def test_ptnet::weibull_constructor_args():
    sig = inspect.signature(ptnet::Weibull.__init__)
    params = list(sig.parameters.keys())
    assert "Beta" in params, "Missing parameter 'Beta'"
    assert "Alpha" in params, "Missing parameter 'Alpha'"

def test_ptnet::weibull_has_Beta():
    assert hasattr(ptnet::Weibull, "Beta")
    descriptor = None
    for klass in ptnet::Weibull.__mro__:
        if "Beta" in klass.__dict__:
            descriptor = klass.__dict__["Beta"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::weibull_has_Alpha():
    assert hasattr(ptnet::Weibull, "Alpha")
    descriptor = None
    for klass in ptnet::Weibull.__mro__:
        if "Alpha" in klass.__dict__:
            descriptor = klass.__dict__["Alpha"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::gamma_is_not_abstract():
    assert not inspect.isabstract(ptnet::Gamma)


def test_ptnet::gamma_constructor_exists():
    assert callable(ptnet::Gamma.__init__)


def test_ptnet::gamma_constructor_args():
    sig = inspect.signature(ptnet::Gamma.__init__)
    params = list(sig.parameters.keys())
    assert "Alpha" in params, "Missing parameter 'Alpha'"
    assert "Beta" in params, "Missing parameter 'Beta'"

def test_ptnet::gamma_has_Alpha():
    assert hasattr(ptnet::Gamma, "Alpha")
    descriptor = None
    for klass in ptnet::Gamma.__mro__:
        if "Alpha" in klass.__dict__:
            descriptor = klass.__dict__["Alpha"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::gamma_has_Beta():
    assert hasattr(ptnet::Gamma, "Beta")
    descriptor = None
    for klass in ptnet::Gamma.__mro__:
        if "Beta" in klass.__dict__:
            descriptor = klass.__dict__["Beta"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::uniform_is_not_abstract():
    assert not inspect.isabstract(ptnet::Uniform)


def test_ptnet::uniform_constructor_exists():
    assert callable(ptnet::Uniform.__init__)


def test_ptnet::uniform_constructor_args():
    sig = inspect.signature(ptnet::Uniform.__init__)
    params = list(sig.parameters.keys())
    assert "Lower" in params, "Missing parameter 'Lower'"
    assert "Upper" in params, "Missing parameter 'Upper'"

def test_ptnet::uniform_has_Lower():
    assert hasattr(ptnet::Uniform, "Lower")
    descriptor = None
    for klass in ptnet::Uniform.__mro__:
        if "Lower" in klass.__dict__:
            descriptor = klass.__dict__["Lower"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::uniform_has_Upper():
    assert hasattr(ptnet::Uniform, "Upper")
    descriptor = None
    for klass in ptnet::Uniform.__mro__:
        if "Upper" in klass.__dict__:
            descriptor = klass.__dict__["Upper"]
            break
    assert isinstance(descriptor, property)



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::attribute_is_not_abstract():
    assert not inspect.isabstract(ptnet::Attribute)


def test_ptnet::attribute_constructor_exists():
    assert callable(ptnet::Attribute.__init__)


def test_ptnet::attribute_constructor_args():
    sig = inspect.signature(ptnet::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::gspnarc_is_not_abstract():
    assert not inspect.isabstract(ptnet::GSPNArc)


def test_ptnet::gspnarc_constructor_exists():
    assert callable(ptnet::GSPNArc.__init__)


def test_ptnet::gspnarc_constructor_args():
    sig = inspect.signature(ptnet::GSPNArc.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ptnet::gspnarc_has_type():
    assert hasattr(ptnet::GSPNArc, "type")
    descriptor = None
    for klass in ptnet::GSPNArc.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::logicalexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet::LogicalExpression)


def test_ptnet::logicalexpression_constructor_exists():
    assert callable(ptnet::LogicalExpression.__init__)


def test_ptnet::logicalexpression_constructor_args():
    sig = inspect.signature(ptnet::LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::gspntransition_is_not_abstract():
    assert not inspect.isabstract(ptnet::GSPNTransition)


def test_ptnet::gspntransition_constructor_exists():
    assert callable(ptnet::GSPNTransition.__init__)


def test_ptnet::gspntransition_constructor_args():
    sig = inspect.signature(ptnet::GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::transitionnode_is_not_abstract():
    assert not inspect.isabstract(ptnet::TransitionNode)


def test_ptnet::transitionnode_constructor_exists():
    assert callable(ptnet::TransitionNode.__init__)


def test_ptnet::transitionnode_constructor_args():
    sig = inspect.signature(ptnet::TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::placenode_is_not_abstract():
    assert not inspect.isabstract(ptnet::PlaceNode)


def test_ptnet::placenode_constructor_exists():
    assert callable(ptnet::PlaceNode.__init__)


def test_ptnet::placenode_constructor_args():
    sig = inspect.signature(ptnet::PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::reftransition_is_not_abstract():
    assert not inspect.isabstract(ptnet::RefTransition)


def test_ptnet::reftransition_constructor_exists():
    assert callable(ptnet::RefTransition.__init__)


def test_ptnet::reftransition_constructor_args():
    sig = inspect.signature(ptnet::RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::transition_is_not_abstract():
    assert not inspect.isabstract(ptnet::Transition)


def test_ptnet::transition_constructor_exists():
    assert callable(ptnet::Transition.__init__)


def test_ptnet::transition_constructor_args():
    sig = inspect.signature(ptnet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::refplace_is_not_abstract():
    assert not inspect.isabstract(ptnet::RefPlace)


def test_ptnet::refplace_constructor_exists():
    assert callable(ptnet::RefPlace.__init__)


def test_ptnet::refplace_constructor_args():
    sig = inspect.signature(ptnet::RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::annotation_is_not_abstract():
    assert not inspect.isabstract(ptnet::Annotation)


def test_ptnet::annotation_constructor_exists():
    assert callable(ptnet::Annotation.__init__)


def test_ptnet::annotation_constructor_args():
    sig = inspect.signature(ptnet::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::font_is_not_abstract():
    assert not inspect.isabstract(ptnet::Font)


def test_ptnet::font_constructor_exists():
    assert callable(ptnet::Font.__init__)


def test_ptnet::font_constructor_args():
    sig = inspect.signature(ptnet::Font.__init__)
    params = list(sig.parameters.keys())
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "family" in params, "Missing parameter 'family'"
    assert "size" in params, "Missing parameter 'size'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "align" in params, "Missing parameter 'align'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "style" in params, "Missing parameter 'style'"

def test_ptnet::font_has_rotation():
    assert hasattr(ptnet::Font, "rotation")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_family():
    assert hasattr(ptnet::Font, "family")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_size():
    assert hasattr(ptnet::Font, "size")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_decoration():
    assert hasattr(ptnet::Font, "decoration")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_align():
    assert hasattr(ptnet::Font, "align")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_weight():
    assert hasattr(ptnet::Font, "weight")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::font_has_style():
    assert hasattr(ptnet::Font, "style")
    descriptor = None
    for klass in ptnet::Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::graphics_is_not_abstract():
    assert not inspect.isabstract(ptnet::Graphics)


def test_ptnet::graphics_constructor_exists():
    assert callable(ptnet::Graphics.__init__)


def test_ptnet::graphics_constructor_args():
    sig = inspect.signature(ptnet::Graphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::line_is_not_abstract():
    assert not inspect.isabstract(ptnet::Line)


def test_ptnet::line_constructor_exists():
    assert callable(ptnet::Line.__init__)


def test_ptnet::line_constructor_args():
    sig = inspect.signature(ptnet::Line.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "width" in params, "Missing parameter 'width'"
    assert "color" in params, "Missing parameter 'color'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_ptnet::line_has_style():
    assert hasattr(ptnet::Line, "style")
    descriptor = None
    for klass in ptnet::Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::line_has_width():
    assert hasattr(ptnet::Line, "width")
    descriptor = None
    for klass in ptnet::Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::line_has_color():
    assert hasattr(ptnet::Line, "color")
    descriptor = None
    for klass in ptnet::Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::line_has_shape():
    assert hasattr(ptnet::Line, "shape")
    descriptor = None
    for klass in ptnet::Line.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_coordinate_is_not_abstract():
    assert not inspect.isabstract(Coordinate)


def test_coordinate_constructor_exists():
    assert callable(Coordinate.__init__)


def test_coordinate_constructor_args():
    sig = inspect.signature(Coordinate.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::offset_is_not_abstract():
    assert not inspect.isabstract(ptnet::Offset)


def test_ptnet::offset_constructor_exists():
    assert callable(ptnet::Offset.__init__)


def test_ptnet::offset_constructor_args():
    sig = inspect.signature(ptnet::Offset.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::coordinate_is_not_abstract():
    assert not inspect.isabstract(ptnet::Coordinate)


def test_ptnet::coordinate_constructor_exists():
    assert callable(ptnet::Coordinate.__init__)


def test_ptnet::coordinate_constructor_args():
    sig = inspect.signature(ptnet::Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"
    assert "y" in params, "Missing parameter 'y'"

def test_ptnet::coordinate_has_x():
    assert hasattr(ptnet::Coordinate, "x")
    descriptor = None
    for klass in ptnet::Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::coordinate_has_y():
    assert hasattr(ptnet::Coordinate, "y")
    descriptor = None
    for klass in ptnet::Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::anyobject_is_not_abstract():
    assert not inspect.isabstract(ptnet::AnyObject)


def test_ptnet::anyobject_constructor_exists():
    assert callable(ptnet::AnyObject.__init__)


def test_ptnet::anyobject_constructor_args():
    sig = inspect.signature(ptnet::AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::label_is_not_abstract():
    assert not inspect.isabstract(ptnet::Label)


def test_ptnet::label_constructor_exists():
    assert callable(ptnet::Label.__init__)


def test_ptnet::label_constructor_args():
    sig = inspect.signature(ptnet::Label.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::fill_is_not_abstract():
    assert not inspect.isabstract(ptnet::Fill)


def test_ptnet::fill_constructor_exists():
    assert callable(ptnet::Fill.__init__)


def test_ptnet::fill_constructor_args():
    sig = inspect.signature(ptnet::Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"

def test_ptnet::fill_has_color():
    assert hasattr(ptnet::Fill, "color")
    descriptor = None
    for klass in ptnet::Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::fill_has_gradientcolor():
    assert hasattr(ptnet::Fill, "gradientcolor")
    descriptor = None
    for klass in ptnet::Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::fill_has_gradientrotation():
    assert hasattr(ptnet::Fill, "gradientrotation")
    descriptor = None
    for klass in ptnet::Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::fill_has_image():
    assert hasattr(ptnet::Fill, "image")
    descriptor = None
    for klass in ptnet::Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::dimension_is_not_abstract():
    assert not inspect.isabstract(ptnet::Dimension)


def test_ptnet::dimension_constructor_exists():
    assert callable(ptnet::Dimension.__init__)


def test_ptnet::dimension_constructor_args():
    sig = inspect.signature(ptnet::Dimension.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::position_is_not_abstract():
    assert not inspect.isabstract(ptnet::Position)


def test_ptnet::position_constructor_exists():
    assert callable(ptnet::Position.__init__)


def test_ptnet::position_constructor_args():
    sig = inspect.signature(ptnet::Position.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::arcgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet::ArcGraphics)


def test_ptnet::arcgraphics_constructor_exists():
    assert callable(ptnet::ArcGraphics.__init__)


def test_ptnet::arcgraphics_constructor_args():
    sig = inspect.signature(ptnet::ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet::AnnotationGraphics)


def test_ptnet::annotationgraphics_constructor_exists():
    assert callable(ptnet::AnnotationGraphics.__init__)


def test_ptnet::annotationgraphics_constructor_args():
    sig = inspect.signature(ptnet::AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::nodegraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet::NodeGraphics)


def test_ptnet::nodegraphics_constructor_exists():
    assert callable(ptnet::NodeGraphics.__init__)


def test_ptnet::nodegraphics_constructor_args():
    sig = inspect.signature(ptnet::NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::pnobject_is_not_abstract():
    assert not inspect.isabstract(ptnet::PnObject)


def test_ptnet::pnobject_constructor_exists():
    assert callable(ptnet::PnObject.__init__)


def test_ptnet::pnobject_constructor_args():
    sig = inspect.signature(ptnet::PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ptnet::pnobject_has_id():
    assert hasattr(ptnet::PnObject, "id")
    descriptor = None
    for klass in ptnet::PnObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::petrinet_is_not_abstract():
    assert not inspect.isabstract(ptnet::PetriNet)


def test_ptnet::petrinet_constructor_exists():
    assert callable(ptnet::PetriNet.__init__)


def test_ptnet::petrinet_constructor_args():
    sig = inspect.signature(ptnet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_ptnet::petrinet_has_type():
    assert hasattr(ptnet::PetriNet, "type")
    descriptor = None
    for klass in ptnet::PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::petrinet_has_id():
    assert hasattr(ptnet::PetriNet, "id")
    descriptor = None
    for klass in ptnet::PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(ptnet::PetriNetDoc)


def test_ptnet::petrinetdoc_constructor_exists():
    assert callable(ptnet::PetriNetDoc.__init__)


def test_ptnet::petrinetdoc_constructor_args():
    sig = inspect.signature(ptnet::PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_ptnet::petrinetdoc_has_xmlns():
    assert hasattr(ptnet::PetriNetDoc, "xmlns")
    descriptor = None
    for klass in ptnet::PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::place_is_not_abstract():
    assert not inspect.isabstract(ptnet::Place)


def test_ptnet::place_constructor_exists():
    assert callable(ptnet::Place.__init__)


def test_ptnet::place_constructor_args():
    sig = inspect.signature(ptnet::Place.__init__)
    params = list(sig.parameters.keys())



def test_pnobject_is_not_abstract():
    assert not inspect.isabstract(PnObject)


def test_pnobject_constructor_exists():
    assert callable(PnObject.__init__)


def test_pnobject_constructor_args():
    sig = inspect.signature(PnObject.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::page_is_not_abstract():
    assert not inspect.isabstract(ptnet::Page)


def test_ptnet::page_constructor_exists():
    assert callable(ptnet::Page.__init__)


def test_ptnet::page_constructor_args():
    sig = inspect.signature(ptnet::Page.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::node_is_not_abstract():
    assert not inspect.isabstract(ptnet::Node)


def test_ptnet::node_constructor_exists():
    assert callable(ptnet::Node.__init__)


def test_ptnet::node_constructor_args():
    sig = inspect.signature(ptnet::Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::arc_is_not_abstract():
    assert not inspect.isabstract(ptnet::Arc)


def test_ptnet::arc_constructor_exists():
    assert callable(ptnet::Arc.__init__)


def test_ptnet::arc_constructor_args():
    sig = inspect.signature(ptnet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::toolinfo_is_not_abstract():
    assert not inspect.isabstract(ptnet::ToolInfo)


def test_ptnet::toolinfo_constructor_exists():
    assert callable(ptnet::ToolInfo.__init__)


def test_ptnet::toolinfo_constructor_args():
    sig = inspect.signature(ptnet::ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "tool" in params, "Missing parameter 'tool'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "version" in params, "Missing parameter 'version'"

def test_ptnet::toolinfo_has_tool():
    assert hasattr(ptnet::ToolInfo, "tool")
    descriptor = None
    for klass in ptnet::ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::toolinfo_has_toolInfoGrammarURI():
    assert hasattr(ptnet::ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in ptnet::ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::toolinfo_has_formattedXMLBuffer():
    assert hasattr(ptnet::ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in ptnet::ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_ptnet::toolinfo_has_version():
    assert hasattr(ptnet::ToolInfo, "version")
    descriptor = None
    for klass in ptnet::ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ptnet::name_is_not_abstract():
    assert not inspect.isabstract(ptnet::Name)


def test_ptnet::name_constructor_exists():
    assert callable(ptnet::Name.__init__)


def test_ptnet::name_constructor_args():
    sig = inspect.signature(ptnet::Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet::name_has_text():
    assert hasattr(ptnet::Name, "text")
    descriptor = None
    for klass in ptnet::Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::ptarcannotation_is_not_abstract():
    assert not inspect.isabstract(ptnet::PTArcAnnotation)


def test_ptnet::ptarcannotation_constructor_exists():
    assert callable(ptnet::PTArcAnnotation.__init__)


def test_ptnet::ptarcannotation_constructor_args():
    sig = inspect.signature(ptnet::PTArcAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet::ptarcannotation_has_text():
    assert hasattr(ptnet::PTArcAnnotation, "text")
    descriptor = None
    for klass in ptnet::PTArcAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ptnet::ptmarking_is_not_abstract():
    assert not inspect.isabstract(ptnet::PTMarking)


def test_ptnet::ptmarking_constructor_exists():
    assert callable(ptnet::PTMarking.__init__)


def test_ptnet::ptmarking_constructor_args():
    sig = inspect.signature(ptnet::PTMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet::ptmarking_has_text():
    assert hasattr(ptnet::PTMarking, "text")
    descriptor = None
    for klass in ptnet::PTMarking.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_gspnarctype_exists():
    # Check that the Enumeration exists
    assert GSPNArcType is not None

def test_gspnarctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSPNArcType]
    expected_literals = [
        "normal",
        "inhibitor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSPNArcType"

def test_lineshape_exists():
    # Check that the Enumeration exists
    assert LineShape is not None

def test_lineshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineShape]
    expected_literals = [
        "CURVE",
        "LINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "AQUA",
        "TEAL",
        "FUCHSIA",
        "NAVY",
        "RED",
        "SILVER",
        "OLIVE",
        "PURPLE",
        "YELLOW",
        "ORANGE",
        "BLACK",
        "WHITE",
        "BLUE",
        "GREEN",
        "GRAY",
        "LIME",
        "MAROON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_gspntransitiontype_exists():
    # Check that the Enumeration exists
    assert GSPNTransitionType is not None

def test_gspntransitiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSPNTransitionType]
    expected_literals = [
        "immediate",
        "timed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSPNTransitionType"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DOT",
        "DASH",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

def test_css2fontstyle_exists():
    # Check that the Enumeration exists
    assert CSS2FontStyle is not None

def test_css2fontstyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontStyle]
    expected_literals = [
        "OBLIQUE",
        "ITALIC",
        "NORMAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontStyle"

def test_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "RIGHT",
        "LEFT",
        "CENTER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "GEORGIA",
        "ARIAL",
        "VERDANA",
        "TREBUCHET",
        "TIMES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontFamily"

def test_gradient_exists():
    # Check that the Enumeration exists
    assert Gradient is not None

def test_gradient_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Gradient]
    expected_literals = [
        "HORIZONTAL",
        "DIAGONAL",
        "VERTICAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

def test_css2fontweight_exists():
    # Check that the Enumeration exists
    assert CSS2FontWeight is not None

def test_css2fontweight_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontWeight]
    expected_literals = [
        "NORMAL",
        "BOLDER",
        "LIGHTER",
        "BOLD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontWeight"

def test_fontdecoration_exists():
    # Check that the Enumeration exists
    assert FontDecoration is not None

def test_fontdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontDecoration]
    expected_literals = [
        "UNDERLINE",
        "LINETHROUGH",
        "OVERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontDecoration"

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "COREMODEL",
        "GSPN",
        "HLPN",
        "SYMNET",
        "PTNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "SMALL",
        "XXLARGE",
        "LARGE",
        "MEDIUM",
        "XXSMALL",
        "XSMALL",
        "XLARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"


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
ptnet::Variable_strategy = st.builds(
    ptnet::Variable,
    name=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
ptnet::OpOr_strategy = st.builds(
    ptnet::OpOr,
)
ptnet::OpAnd_strategy = st.builds(
    ptnet::OpAnd,
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
ptnet::OpLessEqual_strategy = st.builds(
    ptnet::OpLessEqual,
)
ptnet::OpLess_strategy = st.builds(
    ptnet::OpLess,
)
ptnet::OpGreaterEqual_strategy = st.builds(
    ptnet::OpGreaterEqual,
)
ptnet::OpGreater_strategy = st.builds(
    ptnet::OpGreater,
)
ptnet::OpEqual_strategy = st.builds(
    ptnet::OpEqual,
)
EvaluationType_strategy = st.builds(
    EvaluationType,
)
ptnet::InstantOfTime_strategy = st.builds(
    ptnet::InstantOfTime,
)
ptnet::IntervalOfTime_strategy = st.builds(
    ptnet::IntervalOfTime,
)
ptnet::IntervalOfTimeAveraged_strategy = st.builds(
    ptnet::IntervalOfTimeAveraged,
)
ptnet::SteadyState_strategy = st.builds(
    ptnet::SteadyState,
)
ArithmeticBinaryOperator_strategy = st.builds(
    ArithmeticBinaryOperator,
)
ptnet::OpMultiply_strategy = st.builds(
    ptnet::OpMultiply,
)
ptnet::OpMinus_strategy = st.builds(
    ptnet::OpMinus,
)
ptnet::OpDivide_strategy = st.builds(
    ptnet::OpDivide,
)
ptnet::OpSum_strategy = st.builds(
    ptnet::OpSum,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
ptnet::BooleanExpression_strategy = st.builds(
    ptnet::BooleanExpression,
)
ptnet::OpFalse_strategy = st.builds(
    ptnet::OpFalse,
)
ptnet::OpNot_strategy = st.builds(
    ptnet::OpNot,
)
ptnet::ComparisonOperator_strategy = st.builds(
    ptnet::ComparisonOperator,
)
ptnet::OpTrue_strategy = st.builds(
    ptnet::OpTrue,
)
ptnet::EvaluationType_strategy = st.builds(
    ptnet::EvaluationType,
)
ptnet::VariableValues_strategy = st.builds(
    ptnet::VariableValues,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Measure_strategy = st.builds(
    ptnet::Measure,
    name=
        safe_text
)
ptnet::Study_strategy = st.builds(
    ptnet::Study,
    name=
        safe_text
)
ptnet::EvaluationList_strategy = st.builds(
    ptnet::EvaluationList,
)
Expression_strategy = st.builds(
    Expression,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
ptnet::ArithmeticBinaryOperator_strategy = st.builds(
    ptnet::ArithmeticBinaryOperator,
)
ptnet::VariableExpression_strategy = st.builds(
    ptnet::VariableExpression,
)
ptnet::IfThenElse_strategy = st.builds(
    ptnet::IfThenElse,
)
ptnet::MarkingExpression_strategy = st.builds(
    ptnet::MarkingExpression,
)
ptnet::ValueExpression_strategy = st.builds(
    ptnet::ValueExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Expression_strategy = st.builds(
    ptnet::Expression,
)
Distribution_strategy = st.builds(
    Distribution,
)
ptnet::Gaussian_strategy = st.builds(
    ptnet::Gaussian,
    Variance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Mean=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Exponential_strategy = st.builds(
    ptnet::Exponential,
    Rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Deterministic_strategy = st.builds(
    ptnet::Deterministic,
    Value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Distribution_strategy = st.builds(
    ptnet::Distribution,
)
GSPNTransition_strategy = st.builds(
    GSPNTransition,
)
ptnet::GSPNTimedTransition_strategy = st.builds(
    ptnet::GSPNTimedTransition,
)
ptnet::GSPNImmediateTransition_strategy = st.builds(
    ptnet::GSPNImmediateTransition,
    Weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Priority=
        st.integers()
)
ptnet::ArithmeticExpression_strategy = st.builds(
    ptnet::ArithmeticExpression,
)
ptnet::Weibull_strategy = st.builds(
    ptnet::Weibull,
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Gamma_strategy = st.builds(
    ptnet::Gamma,
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet::Uniform_strategy = st.builds(
    ptnet::Uniform,
    Lower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Upper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Label_strategy = st.builds(
    Label,
)
ptnet::Attribute_strategy = st.builds(
    ptnet::Attribute,
)
Arc_strategy = st.builds(
    Arc,
)
ptnet::GSPNArc_strategy = st.builds(
    ptnet::GSPNArc,
    type=
        safe_text
)
ptnet::LogicalExpression_strategy = st.builds(
    ptnet::LogicalExpression,
)
Transition_strategy = st.builds(
    Transition,
)
ptnet::GSPNTransition_strategy = st.builds(
    ptnet::GSPNTransition,
)
Node_strategy = st.builds(
    Node,
)
ptnet::TransitionNode_strategy = st.builds(
    ptnet::TransitionNode,
)
ptnet::PlaceNode_strategy = st.builds(
    ptnet::PlaceNode,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
ptnet::RefTransition_strategy = st.builds(
    ptnet::RefTransition,
)
ptnet::Transition_strategy = st.builds(
    ptnet::Transition,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
ptnet::RefPlace_strategy = st.builds(
    ptnet::RefPlace,
)
ptnet::Annotation_strategy = st.builds(
    ptnet::Annotation,
)
ptnet::Font_strategy = st.builds(
    ptnet::Font,
    rotation=
        safe_text,
    family=
        safe_text,
    size=
        safe_text,
    decoration=
        safe_text,
    align=
        safe_text,
    weight=
        safe_text,
    style=
        safe_text
)
ptnet::Graphics_strategy = st.builds(
    ptnet::Graphics,
)
ptnet::Line_strategy = st.builds(
    ptnet::Line,
    style=
        safe_text,
    width=
        safe_text,
    color=
        safe_text,
    shape=
        safe_text
)
Coordinate_strategy = st.builds(
    Coordinate,
)
ptnet::Offset_strategy = st.builds(
    ptnet::Offset,
)
ptnet::Coordinate_strategy = st.builds(
    ptnet::Coordinate,
    x=
        safe_text,
    y=
        safe_text
)
ptnet::AnyObject_strategy = st.builds(
    ptnet::AnyObject,
)
ptnet::Label_strategy = st.builds(
    ptnet::Label,
)
ptnet::Fill_strategy = st.builds(
    ptnet::Fill,
    color=
        safe_text,
    gradientcolor=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text
)
ptnet::Dimension_strategy = st.builds(
    ptnet::Dimension,
)
ptnet::Position_strategy = st.builds(
    ptnet::Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
ptnet::ArcGraphics_strategy = st.builds(
    ptnet::ArcGraphics,
)
ptnet::AnnotationGraphics_strategy = st.builds(
    ptnet::AnnotationGraphics,
)
ptnet::NodeGraphics_strategy = st.builds(
    ptnet::NodeGraphics,
)
ptnet::PnObject_strategy = st.builds(
    ptnet::PnObject,
    id=
        safe_text
)
ptnet::PetriNet_strategy = st.builds(
    ptnet::PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
ptnet::PetriNetDoc_strategy = st.builds(
    ptnet::PetriNetDoc,
    xmlns=
        safe_text
)
ptnet::Place_strategy = st.builds(
    ptnet::Place,
)
PnObject_strategy = st.builds(
    PnObject,
)
ptnet::Page_strategy = st.builds(
    ptnet::Page,
)
ptnet::Node_strategy = st.builds(
    ptnet::Node,
)
ptnet::Arc_strategy = st.builds(
    ptnet::Arc,
)
ptnet::ToolInfo_strategy = st.builds(
    ptnet::ToolInfo,
    tool=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    formattedXMLBuffer=
        safe_text,
    version=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
ptnet::Name_strategy = st.builds(
    ptnet::Name,
    text=
        safe_text
)
ptnet::PTArcAnnotation_strategy = st.builds(
    ptnet::PTArcAnnotation,
    text=
        safe_text
)
ptnet::PTMarking_strategy = st.builds(
    ptnet::PTMarking,
    text=
        safe_text
)

@given(instance=ptnet::Variable_strategy)
@settings(max_examples=50)
def test_ptnet::variable_instantiation(instance):
    assert isinstance(instance, ptnet::Variable)

@given(instance=ptnet::Variable_strategy)
def test_ptnet::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptnet::Variable_strategy)
def test_ptnet::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=ptnet::OpOr_strategy)
@settings(max_examples=50)
def test_ptnet::opor_instantiation(instance):
    assert isinstance(instance, ptnet::OpOr)

@given(instance=ptnet::OpAnd_strategy)
@settings(max_examples=50)
def test_ptnet::opand_instantiation(instance):
    assert isinstance(instance, ptnet::OpAnd)

@given(instance=ComparisonOperator_strategy)
@settings(max_examples=50)
def test_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)

@given(instance=ptnet::OpLessEqual_strategy)
@settings(max_examples=50)
def test_ptnet::oplessequal_instantiation(instance):
    assert isinstance(instance, ptnet::OpLessEqual)

@given(instance=ptnet::OpLess_strategy)
@settings(max_examples=50)
def test_ptnet::opless_instantiation(instance):
    assert isinstance(instance, ptnet::OpLess)

@given(instance=ptnet::OpGreaterEqual_strategy)
@settings(max_examples=50)
def test_ptnet::opgreaterequal_instantiation(instance):
    assert isinstance(instance, ptnet::OpGreaterEqual)

@given(instance=ptnet::OpGreater_strategy)
@settings(max_examples=50)
def test_ptnet::opgreater_instantiation(instance):
    assert isinstance(instance, ptnet::OpGreater)

@given(instance=ptnet::OpEqual_strategy)
@settings(max_examples=50)
def test_ptnet::opequal_instantiation(instance):
    assert isinstance(instance, ptnet::OpEqual)

@given(instance=EvaluationType_strategy)
@settings(max_examples=50)
def test_evaluationtype_instantiation(instance):
    assert isinstance(instance, EvaluationType)

@given(instance=ptnet::InstantOfTime_strategy)
@settings(max_examples=50)
def test_ptnet::instantoftime_instantiation(instance):
    assert isinstance(instance, ptnet::InstantOfTime)

@given(instance=ptnet::IntervalOfTime_strategy)
@settings(max_examples=50)
def test_ptnet::intervaloftime_instantiation(instance):
    assert isinstance(instance, ptnet::IntervalOfTime)

@given(instance=ptnet::IntervalOfTimeAveraged_strategy)
@settings(max_examples=50)
def test_ptnet::intervaloftimeaveraged_instantiation(instance):
    assert isinstance(instance, ptnet::IntervalOfTimeAveraged)

@given(instance=ptnet::SteadyState_strategy)
@settings(max_examples=50)
def test_ptnet::steadystate_instantiation(instance):
    assert isinstance(instance, ptnet::SteadyState)

@given(instance=ArithmeticBinaryOperator_strategy)
@settings(max_examples=50)
def test_arithmeticbinaryoperator_instantiation(instance):
    assert isinstance(instance, ArithmeticBinaryOperator)

@given(instance=ptnet::OpMultiply_strategy)
@settings(max_examples=50)
def test_ptnet::opmultiply_instantiation(instance):
    assert isinstance(instance, ptnet::OpMultiply)

@given(instance=ptnet::OpMinus_strategy)
@settings(max_examples=50)
def test_ptnet::opminus_instantiation(instance):
    assert isinstance(instance, ptnet::OpMinus)

@given(instance=ptnet::OpDivide_strategy)
@settings(max_examples=50)
def test_ptnet::opdivide_instantiation(instance):
    assert isinstance(instance, ptnet::OpDivide)

@given(instance=ptnet::OpSum_strategy)
@settings(max_examples=50)
def test_ptnet::opsum_instantiation(instance):
    assert isinstance(instance, ptnet::OpSum)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=ptnet::BooleanExpression_strategy)
@settings(max_examples=50)
def test_ptnet::booleanexpression_instantiation(instance):
    assert isinstance(instance, ptnet::BooleanExpression)

@given(instance=ptnet::OpFalse_strategy)
@settings(max_examples=50)
def test_ptnet::opfalse_instantiation(instance):
    assert isinstance(instance, ptnet::OpFalse)

@given(instance=ptnet::OpNot_strategy)
@settings(max_examples=50)
def test_ptnet::opnot_instantiation(instance):
    assert isinstance(instance, ptnet::OpNot)

@given(instance=ptnet::ComparisonOperator_strategy)
@settings(max_examples=50)
def test_ptnet::comparisonoperator_instantiation(instance):
    assert isinstance(instance, ptnet::ComparisonOperator)

@given(instance=ptnet::OpTrue_strategy)
@settings(max_examples=50)
def test_ptnet::optrue_instantiation(instance):
    assert isinstance(instance, ptnet::OpTrue)

@given(instance=ptnet::EvaluationType_strategy)
@settings(max_examples=50)
def test_ptnet::evaluationtype_instantiation(instance):
    assert isinstance(instance, ptnet::EvaluationType)

@given(instance=ptnet::VariableValues_strategy)
@settings(max_examples=50)
def test_ptnet::variablevalues_instantiation(instance):
    assert isinstance(instance, ptnet::VariableValues)

@given(instance=ptnet::VariableValues_strategy)
def test_ptnet::variablevalues_values_type(instance):
    assert isinstance(instance.values, float)


@given(instance=ptnet::VariableValues_strategy)
def test_ptnet::variablevalues_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ptnet::Measure_strategy)
@settings(max_examples=50)
def test_ptnet::measure_instantiation(instance):
    assert isinstance(instance, ptnet::Measure)

@given(instance=ptnet::Measure_strategy)
def test_ptnet::measure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptnet::Measure_strategy)
def test_ptnet::measure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnet::Study_strategy)
@settings(max_examples=50)
def test_ptnet::study_instantiation(instance):
    assert isinstance(instance, ptnet::Study)

@given(instance=ptnet::Study_strategy)
def test_ptnet::study_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ptnet::Study_strategy)
def test_ptnet::study_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnet::EvaluationList_strategy)
@settings(max_examples=50)
def test_ptnet::evaluationlist_instantiation(instance):
    assert isinstance(instance, ptnet::EvaluationList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=ptnet::ArithmeticBinaryOperator_strategy)
@settings(max_examples=50)
def test_ptnet::arithmeticbinaryoperator_instantiation(instance):
    assert isinstance(instance, ptnet::ArithmeticBinaryOperator)

@given(instance=ptnet::VariableExpression_strategy)
@settings(max_examples=50)
def test_ptnet::variableexpression_instantiation(instance):
    assert isinstance(instance, ptnet::VariableExpression)

@given(instance=ptnet::IfThenElse_strategy)
@settings(max_examples=50)
def test_ptnet::ifthenelse_instantiation(instance):
    assert isinstance(instance, ptnet::IfThenElse)

@given(instance=ptnet::MarkingExpression_strategy)
@settings(max_examples=50)
def test_ptnet::markingexpression_instantiation(instance):
    assert isinstance(instance, ptnet::MarkingExpression)

@given(instance=ptnet::ValueExpression_strategy)
@settings(max_examples=50)
def test_ptnet::valueexpression_instantiation(instance):
    assert isinstance(instance, ptnet::ValueExpression)

@given(instance=ptnet::ValueExpression_strategy)
def test_ptnet::valueexpression_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=ptnet::ValueExpression_strategy)
def test_ptnet::valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ptnet::Expression_strategy)
@settings(max_examples=50)
def test_ptnet::expression_instantiation(instance):
    assert isinstance(instance, ptnet::Expression)

@given(instance=Distribution_strategy)
@settings(max_examples=50)
def test_distribution_instantiation(instance):
    assert isinstance(instance, Distribution)

@given(instance=ptnet::Gaussian_strategy)
@settings(max_examples=50)
def test_ptnet::gaussian_instantiation(instance):
    assert isinstance(instance, ptnet::Gaussian)

@given(instance=ptnet::Gaussian_strategy)
def test_ptnet::gaussian_Variance_type(instance):
    assert isinstance(instance.Variance, float)


@given(instance=ptnet::Gaussian_strategy)
def test_ptnet::gaussian_Variance_setter(instance):
    original = instance.Variance
    instance.Variance = original
    assert instance.Variance == original

@given(instance=ptnet::Gaussian_strategy)
def test_ptnet::gaussian_Mean_type(instance):
    assert isinstance(instance.Mean, float)


@given(instance=ptnet::Gaussian_strategy)
def test_ptnet::gaussian_Mean_setter(instance):
    original = instance.Mean
    instance.Mean = original
    assert instance.Mean == original

@given(instance=ptnet::Exponential_strategy)
@settings(max_examples=50)
def test_ptnet::exponential_instantiation(instance):
    assert isinstance(instance, ptnet::Exponential)

@given(instance=ptnet::Exponential_strategy)
def test_ptnet::exponential_Rate_type(instance):
    assert isinstance(instance.Rate, float)


@given(instance=ptnet::Exponential_strategy)
def test_ptnet::exponential_Rate_setter(instance):
    original = instance.Rate
    instance.Rate = original
    assert instance.Rate == original

@given(instance=ptnet::Deterministic_strategy)
@settings(max_examples=50)
def test_ptnet::deterministic_instantiation(instance):
    assert isinstance(instance, ptnet::Deterministic)

@given(instance=ptnet::Deterministic_strategy)
def test_ptnet::deterministic_Value_type(instance):
    assert isinstance(instance.Value, float)


@given(instance=ptnet::Deterministic_strategy)
def test_ptnet::deterministic_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=ptnet::Distribution_strategy)
@settings(max_examples=50)
def test_ptnet::distribution_instantiation(instance):
    assert isinstance(instance, ptnet::Distribution)

@given(instance=GSPNTransition_strategy)
@settings(max_examples=50)
def test_gspntransition_instantiation(instance):
    assert isinstance(instance, GSPNTransition)

@given(instance=ptnet::GSPNTimedTransition_strategy)
@settings(max_examples=50)
def test_ptnet::gspntimedtransition_instantiation(instance):
    assert isinstance(instance, ptnet::GSPNTimedTransition)

@given(instance=ptnet::GSPNImmediateTransition_strategy)
@settings(max_examples=50)
def test_ptnet::gspnimmediatetransition_instantiation(instance):
    assert isinstance(instance, ptnet::GSPNImmediateTransition)

@given(instance=ptnet::GSPNImmediateTransition_strategy)
def test_ptnet::gspnimmediatetransition_Weight_type(instance):
    assert isinstance(instance.Weight, float)


@given(instance=ptnet::GSPNImmediateTransition_strategy)
def test_ptnet::gspnimmediatetransition_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original

@given(instance=ptnet::GSPNImmediateTransition_strategy)
def test_ptnet::gspnimmediatetransition_Priority_type(instance):
    assert isinstance(instance.Priority, int)


@given(instance=ptnet::GSPNImmediateTransition_strategy)
def test_ptnet::gspnimmediatetransition_Priority_setter(instance):
    original = instance.Priority
    instance.Priority = original
    assert instance.Priority == original

@given(instance=ptnet::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ptnet::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ptnet::ArithmeticExpression)

@given(instance=ptnet::Weibull_strategy)
@settings(max_examples=50)
def test_ptnet::weibull_instantiation(instance):
    assert isinstance(instance, ptnet::Weibull)

@given(instance=ptnet::Weibull_strategy)
def test_ptnet::weibull_Beta_type(instance):
    assert isinstance(instance.Beta, float)


@given(instance=ptnet::Weibull_strategy)
def test_ptnet::weibull_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original

@given(instance=ptnet::Weibull_strategy)
def test_ptnet::weibull_Alpha_type(instance):
    assert isinstance(instance.Alpha, float)


@given(instance=ptnet::Weibull_strategy)
def test_ptnet::weibull_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original

@given(instance=ptnet::Gamma_strategy)
@settings(max_examples=50)
def test_ptnet::gamma_instantiation(instance):
    assert isinstance(instance, ptnet::Gamma)

@given(instance=ptnet::Gamma_strategy)
def test_ptnet::gamma_Alpha_type(instance):
    assert isinstance(instance.Alpha, float)


@given(instance=ptnet::Gamma_strategy)
def test_ptnet::gamma_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original

@given(instance=ptnet::Gamma_strategy)
def test_ptnet::gamma_Beta_type(instance):
    assert isinstance(instance.Beta, float)


@given(instance=ptnet::Gamma_strategy)
def test_ptnet::gamma_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original

@given(instance=ptnet::Uniform_strategy)
@settings(max_examples=50)
def test_ptnet::uniform_instantiation(instance):
    assert isinstance(instance, ptnet::Uniform)

@given(instance=ptnet::Uniform_strategy)
def test_ptnet::uniform_Lower_type(instance):
    assert isinstance(instance.Lower, float)


@given(instance=ptnet::Uniform_strategy)
def test_ptnet::uniform_Lower_setter(instance):
    original = instance.Lower
    instance.Lower = original
    assert instance.Lower == original

@given(instance=ptnet::Uniform_strategy)
def test_ptnet::uniform_Upper_type(instance):
    assert isinstance(instance.Upper, float)


@given(instance=ptnet::Uniform_strategy)
def test_ptnet::uniform_Upper_setter(instance):
    original = instance.Upper
    instance.Upper = original
    assert instance.Upper == original

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=ptnet::Attribute_strategy)
@settings(max_examples=50)
def test_ptnet::attribute_instantiation(instance):
    assert isinstance(instance, ptnet::Attribute)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=ptnet::GSPNArc_strategy)
@settings(max_examples=50)
def test_ptnet::gspnarc_instantiation(instance):
    assert isinstance(instance, ptnet::GSPNArc)

@given(instance=ptnet::GSPNArc_strategy)
def test_ptnet::gspnarc_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ptnet::GSPNArc_strategy)
def test_ptnet::gspnarc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ptnet::LogicalExpression_strategy)
@settings(max_examples=50)
def test_ptnet::logicalexpression_instantiation(instance):
    assert isinstance(instance, ptnet::LogicalExpression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=ptnet::GSPNTransition_strategy)
@settings(max_examples=50)
def test_ptnet::gspntransition_instantiation(instance):
    assert isinstance(instance, ptnet::GSPNTransition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ptnet::TransitionNode_strategy)
@settings(max_examples=50)
def test_ptnet::transitionnode_instantiation(instance):
    assert isinstance(instance, ptnet::TransitionNode)

@given(instance=ptnet::PlaceNode_strategy)
@settings(max_examples=50)
def test_ptnet::placenode_instantiation(instance):
    assert isinstance(instance, ptnet::PlaceNode)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=ptnet::RefTransition_strategy)
@settings(max_examples=50)
def test_ptnet::reftransition_instantiation(instance):
    assert isinstance(instance, ptnet::RefTransition)

@given(instance=ptnet::Transition_strategy)
@settings(max_examples=50)
def test_ptnet::transition_instantiation(instance):
    assert isinstance(instance, ptnet::Transition)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=ptnet::RefPlace_strategy)
@settings(max_examples=50)
def test_ptnet::refplace_instantiation(instance):
    assert isinstance(instance, ptnet::RefPlace)

@given(instance=ptnet::Annotation_strategy)
@settings(max_examples=50)
def test_ptnet::annotation_instantiation(instance):
    assert isinstance(instance, ptnet::Annotation)

@given(instance=ptnet::Font_strategy)
@settings(max_examples=50)
def test_ptnet::font_instantiation(instance):
    assert isinstance(instance, ptnet::Font)

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_rotation_type(instance):
    assert isinstance(instance.rotation, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_family_type(instance):
    assert isinstance(instance.family, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_decoration_type(instance):
    assert isinstance(instance.decoration, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=ptnet::Font_strategy)
def test_ptnet::font_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=ptnet::Font_strategy)
def test_ptnet::font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=ptnet::Graphics_strategy)
@settings(max_examples=50)
def test_ptnet::graphics_instantiation(instance):
    assert isinstance(instance, ptnet::Graphics)

@given(instance=ptnet::Line_strategy)
@settings(max_examples=50)
def test_ptnet::line_instantiation(instance):
    assert isinstance(instance, ptnet::Line)

@given(instance=ptnet::Line_strategy)
def test_ptnet::line_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=ptnet::Line_strategy)
def test_ptnet::line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=ptnet::Line_strategy)
def test_ptnet::line_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=ptnet::Line_strategy)
def test_ptnet::line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=ptnet::Line_strategy)
def test_ptnet::line_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=ptnet::Line_strategy)
def test_ptnet::line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=ptnet::Line_strategy)
def test_ptnet::line_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=ptnet::Line_strategy)
def test_ptnet::line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=ptnet::Offset_strategy)
@settings(max_examples=50)
def test_ptnet::offset_instantiation(instance):
    assert isinstance(instance, ptnet::Offset)

@given(instance=ptnet::Coordinate_strategy)
@settings(max_examples=50)
def test_ptnet::coordinate_instantiation(instance):
    assert isinstance(instance, ptnet::Coordinate)

@given(instance=ptnet::Coordinate_strategy)
def test_ptnet::coordinate_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=ptnet::Coordinate_strategy)
def test_ptnet::coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=ptnet::Coordinate_strategy)
def test_ptnet::coordinate_y_type(instance):
    assert isinstance(instance.y, str)


@given(instance=ptnet::Coordinate_strategy)
def test_ptnet::coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=ptnet::AnyObject_strategy)
@settings(max_examples=50)
def test_ptnet::anyobject_instantiation(instance):
    assert isinstance(instance, ptnet::AnyObject)

@given(instance=ptnet::Label_strategy)
@settings(max_examples=50)
def test_ptnet::label_instantiation(instance):
    assert isinstance(instance, ptnet::Label)

@given(instance=ptnet::Fill_strategy)
@settings(max_examples=50)
def test_ptnet::fill_instantiation(instance):
    assert isinstance(instance, ptnet::Fill)

@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_gradientcolor_type(instance):
    assert isinstance(instance.gradientcolor, str)


@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original

@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_gradientrotation_type(instance):
    assert isinstance(instance.gradientrotation, str)


@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original

@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=ptnet::Fill_strategy)
def test_ptnet::fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=ptnet::Dimension_strategy)
@settings(max_examples=50)
def test_ptnet::dimension_instantiation(instance):
    assert isinstance(instance, ptnet::Dimension)

@given(instance=ptnet::Position_strategy)
@settings(max_examples=50)
def test_ptnet::position_instantiation(instance):
    assert isinstance(instance, ptnet::Position)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=ptnet::ArcGraphics_strategy)
@settings(max_examples=50)
def test_ptnet::arcgraphics_instantiation(instance):
    assert isinstance(instance, ptnet::ArcGraphics)

@given(instance=ptnet::AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_ptnet::annotationgraphics_instantiation(instance):
    assert isinstance(instance, ptnet::AnnotationGraphics)

@given(instance=ptnet::NodeGraphics_strategy)
@settings(max_examples=50)
def test_ptnet::nodegraphics_instantiation(instance):
    assert isinstance(instance, ptnet::NodeGraphics)

@given(instance=ptnet::PnObject_strategy)
@settings(max_examples=50)
def test_ptnet::pnobject_instantiation(instance):
    assert isinstance(instance, ptnet::PnObject)

@given(instance=ptnet::PnObject_strategy)
def test_ptnet::pnobject_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ptnet::PnObject_strategy)
def test_ptnet::pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ptnet::PetriNet_strategy)
@settings(max_examples=50)
def test_ptnet::petrinet_instantiation(instance):
    assert isinstance(instance, ptnet::PetriNet)

@given(instance=ptnet::PetriNet_strategy)
def test_ptnet::petrinet_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ptnet::PetriNet_strategy)
def test_ptnet::petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ptnet::PetriNet_strategy)
def test_ptnet::petrinet_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=ptnet::PetriNet_strategy)
def test_ptnet::petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ptnet::PetriNetDoc_strategy)
@settings(max_examples=50)
def test_ptnet::petrinetdoc_instantiation(instance):
    assert isinstance(instance, ptnet::PetriNetDoc)

@given(instance=ptnet::PetriNetDoc_strategy)
def test_ptnet::petrinetdoc_xmlns_type(instance):
    assert isinstance(instance.xmlns, str)


@given(instance=ptnet::PetriNetDoc_strategy)
def test_ptnet::petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original

@given(instance=ptnet::Place_strategy)
@settings(max_examples=50)
def test_ptnet::place_instantiation(instance):
    assert isinstance(instance, ptnet::Place)

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=ptnet::Page_strategy)
@settings(max_examples=50)
def test_ptnet::page_instantiation(instance):
    assert isinstance(instance, ptnet::Page)

@given(instance=ptnet::Node_strategy)
@settings(max_examples=50)
def test_ptnet::node_instantiation(instance):
    assert isinstance(instance, ptnet::Node)

@given(instance=ptnet::Arc_strategy)
@settings(max_examples=50)
def test_ptnet::arc_instantiation(instance):
    assert isinstance(instance, ptnet::Arc)

@given(instance=ptnet::ToolInfo_strategy)
@settings(max_examples=50)
def test_ptnet::toolinfo_instantiation(instance):
    assert isinstance(instance, ptnet::ToolInfo)

@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_tool_type(instance):
    assert isinstance(instance.tool, str)


@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_toolInfoGrammarURI_type(instance):
    assert isinstance(instance.toolInfoGrammarURI, str)


@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original

@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_formattedXMLBuffer_type(instance):
    assert isinstance(instance.formattedXMLBuffer, str)


@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original

@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=ptnet::ToolInfo_strategy)
def test_ptnet::toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=ptnet::Name_strategy)
@settings(max_examples=50)
def test_ptnet::name_instantiation(instance):
    assert isinstance(instance, ptnet::Name)

@given(instance=ptnet::Name_strategy)
def test_ptnet::name_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ptnet::Name_strategy)
def test_ptnet::name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ptnet::PTArcAnnotation_strategy)
@settings(max_examples=50)
def test_ptnet::ptarcannotation_instantiation(instance):
    assert isinstance(instance, ptnet::PTArcAnnotation)

@given(instance=ptnet::PTArcAnnotation_strategy)
def test_ptnet::ptarcannotation_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ptnet::PTArcAnnotation_strategy)
def test_ptnet::ptarcannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ptnet::PTMarking_strategy)
@settings(max_examples=50)
def test_ptnet::ptmarking_instantiation(instance):
    assert isinstance(instance, ptnet::PTMarking)

@given(instance=ptnet::PTMarking_strategy)
def test_ptnet::ptmarking_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=ptnet::PTMarking_strategy)
def test_ptnet::ptmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
