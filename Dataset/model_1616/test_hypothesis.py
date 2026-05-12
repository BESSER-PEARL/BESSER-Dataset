import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ptnet_Variable,
    BooleanExpression,
    ptnet_OpOr,
    ptnet_OpAnd,
    ComparisonOperator,
    ptnet_OpGreater,
    ptnet_OpLessEqual,
    ptnet_OpGreaterEqual,
    ptnet_OpLess,
    ptnet_OpEqual,
    EvaluationType,
    ptnet_InstantOfTime,
    ptnet_IntervalOfTime,
    ptnet_IntervalOfTimeAveraged,
    ptnet_SteadyState,
    ArithmeticBinaryOperator,
    ptnet_OpDivide,
    ptnet_OpMultiply,
    ptnet_OpMinus,
    ptnet_OpSum,
    LogicalExpression,
    ptnet_BooleanExpression,
    ptnet_OpFalse,
    ptnet_ComparisonOperator,
    ptnet_OpNot,
    ptnet_OpTrue,
    ptnet_EvaluationType,
    ptnet_VariableValues,
    ptnet_Measure,
    ptnet_Study,
    ptnet_EvaluationList,
    Expression,
    ArithmeticExpression,
    ptnet_IfThenElse,
    ptnet_ArithmeticBinaryOperator,
    ptnet_MarkingExpression,
    ptnet_VariableExpression,
    ptnet_ValueExpression,
    ptnet_Expression,
    Distribution,
    ptnet_Gaussian,
    ptnet_Exponential,
    ptnet_Deterministic,
    ptnet_Distribution,
    GSPNTransition,
    ptnet_GSPNTimedTransition,
    ptnet_GSPNImmediateTransition,
    ptnet_ArithmeticExpression,
    ptnet_Weibull,
    ptnet_Gamma,
    ptnet_Uniform,
    Label,
    ptnet_Attribute,
    Arc,
    ptnet_GSPNArc,
    ptnet_LogicalExpression,
    Transition,
    ptnet_GSPNTransition,
    Node,
    ptnet_TransitionNode,
    ptnet_PlaceNode,
    TransitionNode,
    ptnet_RefTransition,
    ptnet_Transition,
    PlaceNode,
    ptnet_RefPlace,
    ptnet_Annotation,
    ptnet_Font,
    ptnet_Graphics,
    ptnet_Line,
    Coordinate,
    ptnet_Offset,
    ptnet_Coordinate,
    ptnet_AnyObject,
    ptnet_Label,
    ptnet_Fill,
    ptnet_Dimension,
    ptnet_Position,
    Graphics,
    ptnet_AnnotationGraphics,
    ptnet_ArcGraphics,
    ptnet_NodeGraphics,
    ptnet_PnObject,
    ptnet_PetriNet,
    ptnet_PetriNetDoc,
    ptnet_Place,
    PnObject,
    ptnet_Arc,
    ptnet_Page,
    ptnet_Node,
    ptnet_ToolInfo,
    Annotation,
    ptnet_PTArcAnnotation,
    ptnet_Name,
    ptnet_PTMarking,
    FontDecoration,
    CSS2FontSize,
    PNType,
    CSS2Color,
    GSPNArcType,
    LineStyle,
    CSS2FontWeight,
    LineShape,
    FontAlign,
    GSPNTransitionType,
    CSS2FontFamily,
    Gradient,
    CSS2FontStyle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ptnet_variable_is_not_abstract():
    assert not inspect.isabstract(ptnet_Variable)


def test_ptnet_variable_constructor_exists():
    assert callable(ptnet_Variable.__init__)


def test_ptnet_variable_constructor_args():
    sig = inspect.signature(ptnet_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet_variable_has_name():
    assert hasattr(ptnet_Variable, "name")
    descriptor = None
    for klass in ptnet_Variable.__mro__:
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



def test_ptnet_opor_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpOr)


def test_ptnet_opor_constructor_exists():
    assert callable(ptnet_OpOr.__init__)


def test_ptnet_opor_constructor_args():
    sig = inspect.signature(ptnet_OpOr.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opand_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpAnd)


def test_ptnet_opand_constructor_exists():
    assert callable(ptnet_OpAnd.__init__)


def test_ptnet_opand_constructor_args():
    sig = inspect.signature(ptnet_OpAnd.__init__)
    params = list(sig.parameters.keys())



def test_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperator)


def test_comparisonoperator_constructor_exists():
    assert callable(ComparisonOperator.__init__)


def test_comparisonoperator_constructor_args():
    sig = inspect.signature(ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opgreater_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpGreater)


def test_ptnet_opgreater_constructor_exists():
    assert callable(ptnet_OpGreater.__init__)


def test_ptnet_opgreater_constructor_args():
    sig = inspect.signature(ptnet_OpGreater.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_oplessequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpLessEqual)


def test_ptnet_oplessequal_constructor_exists():
    assert callable(ptnet_OpLessEqual.__init__)


def test_ptnet_oplessequal_constructor_args():
    sig = inspect.signature(ptnet_OpLessEqual.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opgreaterequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpGreaterEqual)


def test_ptnet_opgreaterequal_constructor_exists():
    assert callable(ptnet_OpGreaterEqual.__init__)


def test_ptnet_opgreaterequal_constructor_args():
    sig = inspect.signature(ptnet_OpGreaterEqual.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opless_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpLess)


def test_ptnet_opless_constructor_exists():
    assert callable(ptnet_OpLess.__init__)


def test_ptnet_opless_constructor_args():
    sig = inspect.signature(ptnet_OpLess.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opequal_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpEqual)


def test_ptnet_opequal_constructor_exists():
    assert callable(ptnet_OpEqual.__init__)


def test_ptnet_opequal_constructor_args():
    sig = inspect.signature(ptnet_OpEqual.__init__)
    params = list(sig.parameters.keys())



def test_evaluationtype_is_not_abstract():
    assert not inspect.isabstract(EvaluationType)


def test_evaluationtype_constructor_exists():
    assert callable(EvaluationType.__init__)


def test_evaluationtype_constructor_args():
    sig = inspect.signature(EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_instantoftime_is_not_abstract():
    assert not inspect.isabstract(ptnet_InstantOfTime)


def test_ptnet_instantoftime_constructor_exists():
    assert callable(ptnet_InstantOfTime.__init__)


def test_ptnet_instantoftime_constructor_args():
    sig = inspect.signature(ptnet_InstantOfTime.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_intervaloftime_is_not_abstract():
    assert not inspect.isabstract(ptnet_IntervalOfTime)


def test_ptnet_intervaloftime_constructor_exists():
    assert callable(ptnet_IntervalOfTime.__init__)


def test_ptnet_intervaloftime_constructor_args():
    sig = inspect.signature(ptnet_IntervalOfTime.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_intervaloftimeaveraged_is_not_abstract():
    assert not inspect.isabstract(ptnet_IntervalOfTimeAveraged)


def test_ptnet_intervaloftimeaveraged_constructor_exists():
    assert callable(ptnet_IntervalOfTimeAveraged.__init__)


def test_ptnet_intervaloftimeaveraged_constructor_args():
    sig = inspect.signature(ptnet_IntervalOfTimeAveraged.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_steadystate_is_not_abstract():
    assert not inspect.isabstract(ptnet_SteadyState)


def test_ptnet_steadystate_constructor_exists():
    assert callable(ptnet_SteadyState.__init__)


def test_ptnet_steadystate_constructor_args():
    sig = inspect.signature(ptnet_SteadyState.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticBinaryOperator)


def test_arithmeticbinaryoperator_constructor_exists():
    assert callable(ArithmeticBinaryOperator.__init__)


def test_arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opdivide_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpDivide)


def test_ptnet_opdivide_constructor_exists():
    assert callable(ptnet_OpDivide.__init__)


def test_ptnet_opdivide_constructor_args():
    sig = inspect.signature(ptnet_OpDivide.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opmultiply_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpMultiply)


def test_ptnet_opmultiply_constructor_exists():
    assert callable(ptnet_OpMultiply.__init__)


def test_ptnet_opmultiply_constructor_args():
    sig = inspect.signature(ptnet_OpMultiply.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opminus_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpMinus)


def test_ptnet_opminus_constructor_exists():
    assert callable(ptnet_OpMinus.__init__)


def test_ptnet_opminus_constructor_args():
    sig = inspect.signature(ptnet_OpMinus.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opsum_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpSum)


def test_ptnet_opsum_constructor_exists():
    assert callable(ptnet_OpSum.__init__)


def test_ptnet_opsum_constructor_args():
    sig = inspect.signature(ptnet_OpSum.__init__)
    params = list(sig.parameters.keys())



def test_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(LogicalExpression)


def test_logicalexpression_constructor_exists():
    assert callable(LogicalExpression.__init__)


def test_logicalexpression_constructor_args():
    sig = inspect.signature(LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_BooleanExpression)


def test_ptnet_booleanexpression_constructor_exists():
    assert callable(ptnet_BooleanExpression.__init__)


def test_ptnet_booleanexpression_constructor_args():
    sig = inspect.signature(ptnet_BooleanExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opfalse_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpFalse)


def test_ptnet_opfalse_constructor_exists():
    assert callable(ptnet_OpFalse.__init__)


def test_ptnet_opfalse_constructor_args():
    sig = inspect.signature(ptnet_OpFalse.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet_ComparisonOperator)


def test_ptnet_comparisonoperator_constructor_exists():
    assert callable(ptnet_ComparisonOperator.__init__)


def test_ptnet_comparisonoperator_constructor_args():
    sig = inspect.signature(ptnet_ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_opnot_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpNot)


def test_ptnet_opnot_constructor_exists():
    assert callable(ptnet_OpNot.__init__)


def test_ptnet_opnot_constructor_args():
    sig = inspect.signature(ptnet_OpNot.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_optrue_is_not_abstract():
    assert not inspect.isabstract(ptnet_OpTrue)


def test_ptnet_optrue_constructor_exists():
    assert callable(ptnet_OpTrue.__init__)


def test_ptnet_optrue_constructor_args():
    sig = inspect.signature(ptnet_OpTrue.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_evaluationtype_is_not_abstract():
    assert not inspect.isabstract(ptnet_EvaluationType)


def test_ptnet_evaluationtype_constructor_exists():
    assert callable(ptnet_EvaluationType.__init__)


def test_ptnet_evaluationtype_constructor_args():
    sig = inspect.signature(ptnet_EvaluationType.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_variablevalues_is_not_abstract():
    assert not inspect.isabstract(ptnet_VariableValues)


def test_ptnet_variablevalues_constructor_exists():
    assert callable(ptnet_VariableValues.__init__)


def test_ptnet_variablevalues_constructor_args():
    sig = inspect.signature(ptnet_VariableValues.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_ptnet_variablevalues_has_values():
    assert hasattr(ptnet_VariableValues, "values")
    descriptor = None
    for klass in ptnet_VariableValues.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_measure_is_not_abstract():
    assert not inspect.isabstract(ptnet_Measure)


def test_ptnet_measure_constructor_exists():
    assert callable(ptnet_Measure.__init__)


def test_ptnet_measure_constructor_args():
    sig = inspect.signature(ptnet_Measure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet_measure_has_name():
    assert hasattr(ptnet_Measure, "name")
    descriptor = None
    for klass in ptnet_Measure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_study_is_not_abstract():
    assert not inspect.isabstract(ptnet_Study)


def test_ptnet_study_constructor_exists():
    assert callable(ptnet_Study.__init__)


def test_ptnet_study_constructor_args():
    sig = inspect.signature(ptnet_Study.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ptnet_study_has_name():
    assert hasattr(ptnet_Study, "name")
    descriptor = None
    for klass in ptnet_Study.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_evaluationlist_is_not_abstract():
    assert not inspect.isabstract(ptnet_EvaluationList)


def test_ptnet_evaluationlist_constructor_exists():
    assert callable(ptnet_EvaluationList.__init__)


def test_ptnet_evaluationlist_constructor_args():
    sig = inspect.signature(ptnet_EvaluationList.__init__)
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



def test_ptnet_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(ptnet_IfThenElse)


def test_ptnet_ifthenelse_constructor_exists():
    assert callable(ptnet_IfThenElse.__init__)


def test_ptnet_ifthenelse_constructor_args():
    sig = inspect.signature(ptnet_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_arithmeticbinaryoperator_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArithmeticBinaryOperator)


def test_ptnet_arithmeticbinaryoperator_constructor_exists():
    assert callable(ptnet_ArithmeticBinaryOperator.__init__)


def test_ptnet_arithmeticbinaryoperator_constructor_args():
    sig = inspect.signature(ptnet_ArithmeticBinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_markingexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_MarkingExpression)


def test_ptnet_markingexpression_constructor_exists():
    assert callable(ptnet_MarkingExpression.__init__)


def test_ptnet_markingexpression_constructor_args():
    sig = inspect.signature(ptnet_MarkingExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_variableexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_VariableExpression)


def test_ptnet_variableexpression_constructor_exists():
    assert callable(ptnet_VariableExpression.__init__)


def test_ptnet_variableexpression_constructor_args():
    sig = inspect.signature(ptnet_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_ValueExpression)


def test_ptnet_valueexpression_constructor_exists():
    assert callable(ptnet_ValueExpression.__init__)


def test_ptnet_valueexpression_constructor_args():
    sig = inspect.signature(ptnet_ValueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ptnet_valueexpression_has_value():
    assert hasattr(ptnet_ValueExpression, "value")
    descriptor = None
    for klass in ptnet_ValueExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_expression_is_not_abstract():
    assert not inspect.isabstract(ptnet_Expression)


def test_ptnet_expression_constructor_exists():
    assert callable(ptnet_Expression.__init__)


def test_ptnet_expression_constructor_args():
    sig = inspect.signature(ptnet_Expression.__init__)
    params = list(sig.parameters.keys())



def test_distribution_is_not_abstract():
    assert not inspect.isabstract(Distribution)


def test_distribution_constructor_exists():
    assert callable(Distribution.__init__)


def test_distribution_constructor_args():
    sig = inspect.signature(Distribution.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_gaussian_is_not_abstract():
    assert not inspect.isabstract(ptnet_Gaussian)


def test_ptnet_gaussian_constructor_exists():
    assert callable(ptnet_Gaussian.__init__)


def test_ptnet_gaussian_constructor_args():
    sig = inspect.signature(ptnet_Gaussian.__init__)
    params = list(sig.parameters.keys())
    assert "Variance" in params, "Missing parameter 'Variance'"
    assert "Mean" in params, "Missing parameter 'Mean'"

def test_ptnet_gaussian_has_Variance():
    assert hasattr(ptnet_Gaussian, "Variance")
    descriptor = None
    for klass in ptnet_Gaussian.__mro__:
        if "Variance" in klass.__dict__:
            descriptor = klass.__dict__["Variance"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_gaussian_has_Mean():
    assert hasattr(ptnet_Gaussian, "Mean")
    descriptor = None
    for klass in ptnet_Gaussian.__mro__:
        if "Mean" in klass.__dict__:
            descriptor = klass.__dict__["Mean"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_exponential_is_not_abstract():
    assert not inspect.isabstract(ptnet_Exponential)


def test_ptnet_exponential_constructor_exists():
    assert callable(ptnet_Exponential.__init__)


def test_ptnet_exponential_constructor_args():
    sig = inspect.signature(ptnet_Exponential.__init__)
    params = list(sig.parameters.keys())
    assert "Rate" in params, "Missing parameter 'Rate'"

def test_ptnet_exponential_has_Rate():
    assert hasattr(ptnet_Exponential, "Rate")
    descriptor = None
    for klass in ptnet_Exponential.__mro__:
        if "Rate" in klass.__dict__:
            descriptor = klass.__dict__["Rate"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_deterministic_is_not_abstract():
    assert not inspect.isabstract(ptnet_Deterministic)


def test_ptnet_deterministic_constructor_exists():
    assert callable(ptnet_Deterministic.__init__)


def test_ptnet_deterministic_constructor_args():
    sig = inspect.signature(ptnet_Deterministic.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_ptnet_deterministic_has_Value():
    assert hasattr(ptnet_Deterministic, "Value")
    descriptor = None
    for klass in ptnet_Deterministic.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_distribution_is_not_abstract():
    assert not inspect.isabstract(ptnet_Distribution)


def test_ptnet_distribution_constructor_exists():
    assert callable(ptnet_Distribution.__init__)


def test_ptnet_distribution_constructor_args():
    sig = inspect.signature(ptnet_Distribution.__init__)
    params = list(sig.parameters.keys())



def test_gspntransition_is_not_abstract():
    assert not inspect.isabstract(GSPNTransition)


def test_gspntransition_constructor_exists():
    assert callable(GSPNTransition.__init__)


def test_gspntransition_constructor_args():
    sig = inspect.signature(GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_gspntimedtransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNTimedTransition)


def test_ptnet_gspntimedtransition_constructor_exists():
    assert callable(ptnet_GSPNTimedTransition.__init__)


def test_ptnet_gspntimedtransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNTimedTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_gspnimmediatetransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNImmediateTransition)


def test_ptnet_gspnimmediatetransition_constructor_exists():
    assert callable(ptnet_GSPNImmediateTransition.__init__)


def test_ptnet_gspnimmediatetransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNImmediateTransition.__init__)
    params = list(sig.parameters.keys())
    assert "Weight" in params, "Missing parameter 'Weight'"
    assert "Priority" in params, "Missing parameter 'Priority'"

def test_ptnet_gspnimmediatetransition_has_Weight():
    assert hasattr(ptnet_GSPNImmediateTransition, "Weight")
    descriptor = None
    for klass in ptnet_GSPNImmediateTransition.__mro__:
        if "Weight" in klass.__dict__:
            descriptor = klass.__dict__["Weight"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_gspnimmediatetransition_has_Priority():
    assert hasattr(ptnet_GSPNImmediateTransition, "Priority")
    descriptor = None
    for klass in ptnet_GSPNImmediateTransition.__mro__:
        if "Priority" in klass.__dict__:
            descriptor = klass.__dict__["Priority"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArithmeticExpression)


def test_ptnet_arithmeticexpression_constructor_exists():
    assert callable(ptnet_ArithmeticExpression.__init__)


def test_ptnet_arithmeticexpression_constructor_args():
    sig = inspect.signature(ptnet_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_weibull_is_not_abstract():
    assert not inspect.isabstract(ptnet_Weibull)


def test_ptnet_weibull_constructor_exists():
    assert callable(ptnet_Weibull.__init__)


def test_ptnet_weibull_constructor_args():
    sig = inspect.signature(ptnet_Weibull.__init__)
    params = list(sig.parameters.keys())
    assert "Alpha" in params, "Missing parameter 'Alpha'"
    assert "Beta" in params, "Missing parameter 'Beta'"

def test_ptnet_weibull_has_Alpha():
    assert hasattr(ptnet_Weibull, "Alpha")
    descriptor = None
    for klass in ptnet_Weibull.__mro__:
        if "Alpha" in klass.__dict__:
            descriptor = klass.__dict__["Alpha"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_weibull_has_Beta():
    assert hasattr(ptnet_Weibull, "Beta")
    descriptor = None
    for klass in ptnet_Weibull.__mro__:
        if "Beta" in klass.__dict__:
            descriptor = klass.__dict__["Beta"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_gamma_is_not_abstract():
    assert not inspect.isabstract(ptnet_Gamma)


def test_ptnet_gamma_constructor_exists():
    assert callable(ptnet_Gamma.__init__)


def test_ptnet_gamma_constructor_args():
    sig = inspect.signature(ptnet_Gamma.__init__)
    params = list(sig.parameters.keys())
    assert "Beta" in params, "Missing parameter 'Beta'"
    assert "Alpha" in params, "Missing parameter 'Alpha'"

def test_ptnet_gamma_has_Beta():
    assert hasattr(ptnet_Gamma, "Beta")
    descriptor = None
    for klass in ptnet_Gamma.__mro__:
        if "Beta" in klass.__dict__:
            descriptor = klass.__dict__["Beta"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_gamma_has_Alpha():
    assert hasattr(ptnet_Gamma, "Alpha")
    descriptor = None
    for klass in ptnet_Gamma.__mro__:
        if "Alpha" in klass.__dict__:
            descriptor = klass.__dict__["Alpha"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_uniform_is_not_abstract():
    assert not inspect.isabstract(ptnet_Uniform)


def test_ptnet_uniform_constructor_exists():
    assert callable(ptnet_Uniform.__init__)


def test_ptnet_uniform_constructor_args():
    sig = inspect.signature(ptnet_Uniform.__init__)
    params = list(sig.parameters.keys())
    assert "Upper" in params, "Missing parameter 'Upper'"
    assert "Lower" in params, "Missing parameter 'Lower'"

def test_ptnet_uniform_has_Upper():
    assert hasattr(ptnet_Uniform, "Upper")
    descriptor = None
    for klass in ptnet_Uniform.__mro__:
        if "Upper" in klass.__dict__:
            descriptor = klass.__dict__["Upper"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_uniform_has_Lower():
    assert hasattr(ptnet_Uniform, "Lower")
    descriptor = None
    for klass in ptnet_Uniform.__mro__:
        if "Lower" in klass.__dict__:
            descriptor = klass.__dict__["Lower"]
            break
    assert isinstance(descriptor, property)



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_attribute_is_not_abstract():
    assert not inspect.isabstract(ptnet_Attribute)


def test_ptnet_attribute_constructor_exists():
    assert callable(ptnet_Attribute.__init__)


def test_ptnet_attribute_constructor_args():
    sig = inspect.signature(ptnet_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_gspnarc_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNArc)


def test_ptnet_gspnarc_constructor_exists():
    assert callable(ptnet_GSPNArc.__init__)


def test_ptnet_gspnarc_constructor_args():
    sig = inspect.signature(ptnet_GSPNArc.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ptnet_gspnarc_has_type():
    assert hasattr(ptnet_GSPNArc, "type")
    descriptor = None
    for klass in ptnet_GSPNArc.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_logicalexpression_is_not_abstract():
    assert not inspect.isabstract(ptnet_LogicalExpression)


def test_ptnet_logicalexpression_constructor_exists():
    assert callable(ptnet_LogicalExpression.__init__)


def test_ptnet_logicalexpression_constructor_args():
    sig = inspect.signature(ptnet_LogicalExpression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_gspntransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_GSPNTransition)


def test_ptnet_gspntransition_constructor_exists():
    assert callable(ptnet_GSPNTransition.__init__)


def test_ptnet_gspntransition_constructor_args():
    sig = inspect.signature(ptnet_GSPNTransition.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_transitionnode_is_not_abstract():
    assert not inspect.isabstract(ptnet_TransitionNode)


def test_ptnet_transitionnode_constructor_exists():
    assert callable(ptnet_TransitionNode.__init__)


def test_ptnet_transitionnode_constructor_args():
    sig = inspect.signature(ptnet_TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_placenode_is_not_abstract():
    assert not inspect.isabstract(ptnet_PlaceNode)


def test_ptnet_placenode_constructor_exists():
    assert callable(ptnet_PlaceNode.__init__)


def test_ptnet_placenode_constructor_args():
    sig = inspect.signature(ptnet_PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_transitionnode_is_not_abstract():
    assert not inspect.isabstract(TransitionNode)


def test_transitionnode_constructor_exists():
    assert callable(TransitionNode.__init__)


def test_transitionnode_constructor_args():
    sig = inspect.signature(TransitionNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_reftransition_is_not_abstract():
    assert not inspect.isabstract(ptnet_RefTransition)


def test_ptnet_reftransition_constructor_exists():
    assert callable(ptnet_RefTransition.__init__)


def test_ptnet_reftransition_constructor_args():
    sig = inspect.signature(ptnet_RefTransition.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_transition_is_not_abstract():
    assert not inspect.isabstract(ptnet_Transition)


def test_ptnet_transition_constructor_exists():
    assert callable(ptnet_Transition.__init__)


def test_ptnet_transition_constructor_args():
    sig = inspect.signature(ptnet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_placenode_is_not_abstract():
    assert not inspect.isabstract(PlaceNode)


def test_placenode_constructor_exists():
    assert callable(PlaceNode.__init__)


def test_placenode_constructor_args():
    sig = inspect.signature(PlaceNode.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_refplace_is_not_abstract():
    assert not inspect.isabstract(ptnet_RefPlace)


def test_ptnet_refplace_constructor_exists():
    assert callable(ptnet_RefPlace.__init__)


def test_ptnet_refplace_constructor_args():
    sig = inspect.signature(ptnet_RefPlace.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_annotation_is_not_abstract():
    assert not inspect.isabstract(ptnet_Annotation)


def test_ptnet_annotation_constructor_exists():
    assert callable(ptnet_Annotation.__init__)


def test_ptnet_annotation_constructor_args():
    sig = inspect.signature(ptnet_Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_font_is_not_abstract():
    assert not inspect.isabstract(ptnet_Font)


def test_ptnet_font_constructor_exists():
    assert callable(ptnet_Font.__init__)


def test_ptnet_font_constructor_args():
    sig = inspect.signature(ptnet_Font.__init__)
    params = list(sig.parameters.keys())
    assert "family" in params, "Missing parameter 'family'"
    assert "rotation" in params, "Missing parameter 'rotation'"
    assert "style" in params, "Missing parameter 'style'"
    assert "decoration" in params, "Missing parameter 'decoration'"
    assert "weight" in params, "Missing parameter 'weight'"
    assert "size" in params, "Missing parameter 'size'"
    assert "align" in params, "Missing parameter 'align'"

def test_ptnet_font_has_family():
    assert hasattr(ptnet_Font, "family")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "family" in klass.__dict__:
            descriptor = klass.__dict__["family"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_rotation():
    assert hasattr(ptnet_Font, "rotation")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "rotation" in klass.__dict__:
            descriptor = klass.__dict__["rotation"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_style():
    assert hasattr(ptnet_Font, "style")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_decoration():
    assert hasattr(ptnet_Font, "decoration")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "decoration" in klass.__dict__:
            descriptor = klass.__dict__["decoration"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_weight():
    assert hasattr(ptnet_Font, "weight")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_size():
    assert hasattr(ptnet_Font, "size")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_font_has_align():
    assert hasattr(ptnet_Font, "align")
    descriptor = None
    for klass in ptnet_Font.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_graphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_Graphics)


def test_ptnet_graphics_constructor_exists():
    assert callable(ptnet_Graphics.__init__)


def test_ptnet_graphics_constructor_args():
    sig = inspect.signature(ptnet_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_line_is_not_abstract():
    assert not inspect.isabstract(ptnet_Line)


def test_ptnet_line_constructor_exists():
    assert callable(ptnet_Line.__init__)


def test_ptnet_line_constructor_args():
    sig = inspect.signature(ptnet_Line.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_ptnet_line_has_color():
    assert hasattr(ptnet_Line, "color")
    descriptor = None
    for klass in ptnet_Line.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_line_has_width():
    assert hasattr(ptnet_Line, "width")
    descriptor = None
    for klass in ptnet_Line.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_line_has_style():
    assert hasattr(ptnet_Line, "style")
    descriptor = None
    for klass in ptnet_Line.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_line_has_shape():
    assert hasattr(ptnet_Line, "shape")
    descriptor = None
    for klass in ptnet_Line.__mro__:
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



def test_ptnet_offset_is_not_abstract():
    assert not inspect.isabstract(ptnet_Offset)


def test_ptnet_offset_constructor_exists():
    assert callable(ptnet_Offset.__init__)


def test_ptnet_offset_constructor_args():
    sig = inspect.signature(ptnet_Offset.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_coordinate_is_not_abstract():
    assert not inspect.isabstract(ptnet_Coordinate)


def test_ptnet_coordinate_constructor_exists():
    assert callable(ptnet_Coordinate.__init__)


def test_ptnet_coordinate_constructor_args():
    sig = inspect.signature(ptnet_Coordinate.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_ptnet_coordinate_has_y():
    assert hasattr(ptnet_Coordinate, "y")
    descriptor = None
    for klass in ptnet_Coordinate.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_coordinate_has_x():
    assert hasattr(ptnet_Coordinate, "x")
    descriptor = None
    for klass in ptnet_Coordinate.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_anyobject_is_not_abstract():
    assert not inspect.isabstract(ptnet_AnyObject)


def test_ptnet_anyobject_constructor_exists():
    assert callable(ptnet_AnyObject.__init__)


def test_ptnet_anyobject_constructor_args():
    sig = inspect.signature(ptnet_AnyObject.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_label_is_not_abstract():
    assert not inspect.isabstract(ptnet_Label)


def test_ptnet_label_constructor_exists():
    assert callable(ptnet_Label.__init__)


def test_ptnet_label_constructor_args():
    sig = inspect.signature(ptnet_Label.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_fill_is_not_abstract():
    assert not inspect.isabstract(ptnet_Fill)


def test_ptnet_fill_constructor_exists():
    assert callable(ptnet_Fill.__init__)


def test_ptnet_fill_constructor_args():
    sig = inspect.signature(ptnet_Fill.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "gradientrotation" in params, "Missing parameter 'gradientrotation'"
    assert "image" in params, "Missing parameter 'image'"
    assert "gradientcolor" in params, "Missing parameter 'gradientcolor'"

def test_ptnet_fill_has_color():
    assert hasattr(ptnet_Fill, "color")
    descriptor = None
    for klass in ptnet_Fill.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_fill_has_gradientrotation():
    assert hasattr(ptnet_Fill, "gradientrotation")
    descriptor = None
    for klass in ptnet_Fill.__mro__:
        if "gradientrotation" in klass.__dict__:
            descriptor = klass.__dict__["gradientrotation"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_fill_has_image():
    assert hasattr(ptnet_Fill, "image")
    descriptor = None
    for klass in ptnet_Fill.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_fill_has_gradientcolor():
    assert hasattr(ptnet_Fill, "gradientcolor")
    descriptor = None
    for klass in ptnet_Fill.__mro__:
        if "gradientcolor" in klass.__dict__:
            descriptor = klass.__dict__["gradientcolor"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_dimension_is_not_abstract():
    assert not inspect.isabstract(ptnet_Dimension)


def test_ptnet_dimension_constructor_exists():
    assert callable(ptnet_Dimension.__init__)


def test_ptnet_dimension_constructor_args():
    sig = inspect.signature(ptnet_Dimension.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_position_is_not_abstract():
    assert not inspect.isabstract(ptnet_Position)


def test_ptnet_position_constructor_exists():
    assert callable(ptnet_Position.__init__)


def test_ptnet_position_constructor_args():
    sig = inspect.signature(ptnet_Position.__init__)
    params = list(sig.parameters.keys())



def test_graphics_is_not_abstract():
    assert not inspect.isabstract(Graphics)


def test_graphics_constructor_exists():
    assert callable(Graphics.__init__)


def test_graphics_constructor_args():
    sig = inspect.signature(Graphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_annotationgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_AnnotationGraphics)


def test_ptnet_annotationgraphics_constructor_exists():
    assert callable(ptnet_AnnotationGraphics.__init__)


def test_ptnet_annotationgraphics_constructor_args():
    sig = inspect.signature(ptnet_AnnotationGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_arcgraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_ArcGraphics)


def test_ptnet_arcgraphics_constructor_exists():
    assert callable(ptnet_ArcGraphics.__init__)


def test_ptnet_arcgraphics_constructor_args():
    sig = inspect.signature(ptnet_ArcGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_nodegraphics_is_not_abstract():
    assert not inspect.isabstract(ptnet_NodeGraphics)


def test_ptnet_nodegraphics_constructor_exists():
    assert callable(ptnet_NodeGraphics.__init__)


def test_ptnet_nodegraphics_constructor_args():
    sig = inspect.signature(ptnet_NodeGraphics.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_pnobject_is_not_abstract():
    assert not inspect.isabstract(ptnet_PnObject)


def test_ptnet_pnobject_constructor_exists():
    assert callable(ptnet_PnObject.__init__)


def test_ptnet_pnobject_constructor_args():
    sig = inspect.signature(ptnet_PnObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ptnet_pnobject_has_id():
    assert hasattr(ptnet_PnObject, "id")
    descriptor = None
    for klass in ptnet_PnObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_petrinet_is_not_abstract():
    assert not inspect.isabstract(ptnet_PetriNet)


def test_ptnet_petrinet_constructor_exists():
    assert callable(ptnet_PetriNet.__init__)


def test_ptnet_petrinet_constructor_args():
    sig = inspect.signature(ptnet_PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"

def test_ptnet_petrinet_has_type():
    assert hasattr(ptnet_PetriNet, "type")
    descriptor = None
    for klass in ptnet_PetriNet.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_petrinet_has_id():
    assert hasattr(ptnet_PetriNet, "id")
    descriptor = None
    for klass in ptnet_PetriNet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_petrinetdoc_is_not_abstract():
    assert not inspect.isabstract(ptnet_PetriNetDoc)


def test_ptnet_petrinetdoc_constructor_exists():
    assert callable(ptnet_PetriNetDoc.__init__)


def test_ptnet_petrinetdoc_constructor_args():
    sig = inspect.signature(ptnet_PetriNetDoc.__init__)
    params = list(sig.parameters.keys())
    assert "xmlns" in params, "Missing parameter 'xmlns'"

def test_ptnet_petrinetdoc_has_xmlns():
    assert hasattr(ptnet_PetriNetDoc, "xmlns")
    descriptor = None
    for klass in ptnet_PetriNetDoc.__mro__:
        if "xmlns" in klass.__dict__:
            descriptor = klass.__dict__["xmlns"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_place_is_not_abstract():
    assert not inspect.isabstract(ptnet_Place)


def test_ptnet_place_constructor_exists():
    assert callable(ptnet_Place.__init__)


def test_ptnet_place_constructor_args():
    sig = inspect.signature(ptnet_Place.__init__)
    params = list(sig.parameters.keys())



def test_pnobject_is_not_abstract():
    assert not inspect.isabstract(PnObject)


def test_pnobject_constructor_exists():
    assert callable(PnObject.__init__)


def test_pnobject_constructor_args():
    sig = inspect.signature(PnObject.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_arc_is_not_abstract():
    assert not inspect.isabstract(ptnet_Arc)


def test_ptnet_arc_constructor_exists():
    assert callable(ptnet_Arc.__init__)


def test_ptnet_arc_constructor_args():
    sig = inspect.signature(ptnet_Arc.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_page_is_not_abstract():
    assert not inspect.isabstract(ptnet_Page)


def test_ptnet_page_constructor_exists():
    assert callable(ptnet_Page.__init__)


def test_ptnet_page_constructor_args():
    sig = inspect.signature(ptnet_Page.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_node_is_not_abstract():
    assert not inspect.isabstract(ptnet_Node)


def test_ptnet_node_constructor_exists():
    assert callable(ptnet_Node.__init__)


def test_ptnet_node_constructor_args():
    sig = inspect.signature(ptnet_Node.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_toolinfo_is_not_abstract():
    assert not inspect.isabstract(ptnet_ToolInfo)


def test_ptnet_toolinfo_constructor_exists():
    assert callable(ptnet_ToolInfo.__init__)


def test_ptnet_toolinfo_constructor_args():
    sig = inspect.signature(ptnet_ToolInfo.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "toolInfoGrammarURI" in params, "Missing parameter 'toolInfoGrammarURI'"
    assert "formattedXMLBuffer" in params, "Missing parameter 'formattedXMLBuffer'"
    assert "tool" in params, "Missing parameter 'tool'"

def test_ptnet_toolinfo_has_version():
    assert hasattr(ptnet_ToolInfo, "version")
    descriptor = None
    for klass in ptnet_ToolInfo.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_toolinfo_has_toolInfoGrammarURI():
    assert hasattr(ptnet_ToolInfo, "toolInfoGrammarURI")
    descriptor = None
    for klass in ptnet_ToolInfo.__mro__:
        if "toolInfoGrammarURI" in klass.__dict__:
            descriptor = klass.__dict__["toolInfoGrammarURI"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_toolinfo_has_formattedXMLBuffer():
    assert hasattr(ptnet_ToolInfo, "formattedXMLBuffer")
    descriptor = None
    for klass in ptnet_ToolInfo.__mro__:
        if "formattedXMLBuffer" in klass.__dict__:
            descriptor = klass.__dict__["formattedXMLBuffer"]
            break
    assert isinstance(descriptor, property)

def test_ptnet_toolinfo_has_tool():
    assert hasattr(ptnet_ToolInfo, "tool")
    descriptor = None
    for klass in ptnet_ToolInfo.__mro__:
        if "tool" in klass.__dict__:
            descriptor = klass.__dict__["tool"]
            break
    assert isinstance(descriptor, property)



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_ptnet_ptarcannotation_is_not_abstract():
    assert not inspect.isabstract(ptnet_PTArcAnnotation)


def test_ptnet_ptarcannotation_constructor_exists():
    assert callable(ptnet_PTArcAnnotation.__init__)


def test_ptnet_ptarcannotation_constructor_args():
    sig = inspect.signature(ptnet_PTArcAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet_ptarcannotation_has_text():
    assert hasattr(ptnet_PTArcAnnotation, "text")
    descriptor = None
    for klass in ptnet_PTArcAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_name_is_not_abstract():
    assert not inspect.isabstract(ptnet_Name)


def test_ptnet_name_constructor_exists():
    assert callable(ptnet_Name.__init__)


def test_ptnet_name_constructor_args():
    sig = inspect.signature(ptnet_Name.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet_name_has_text():
    assert hasattr(ptnet_Name, "text")
    descriptor = None
    for klass in ptnet_Name.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_ptnet_ptmarking_is_not_abstract():
    assert not inspect.isabstract(ptnet_PTMarking)


def test_ptnet_ptmarking_constructor_exists():
    assert callable(ptnet_PTMarking.__init__)


def test_ptnet_ptmarking_constructor_args():
    sig = inspect.signature(ptnet_PTMarking.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_ptnet_ptmarking_has_text():
    assert hasattr(ptnet_PTMarking, "text")
    descriptor = None
    for klass in ptnet_PTMarking.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_fontdecoration_exists():
    # Check that the Enumeration exists
    assert FontDecoration is not None

def test_fontdecoration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontDecoration]
    expected_literals = [
        "LINETHROUGH",
        "OVERLINE",
        "UNDERLINE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontDecoration"

def test_css2fontsize_exists():
    # Check that the Enumeration exists
    assert CSS2FontSize is not None

def test_css2fontsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontSize]
    expected_literals = [
        "XXSMALL",
        "LARGE",
        "XXLARGE",
        "MEDIUM",
        "XSMALL",
        "SMALL",
        "XLARGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2FontSize"

def test_pntype_exists():
    # Check that the Enumeration exists
    assert PNType is not None

def test_pntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PNType]
    expected_literals = [
        "COREMODEL",
        "HLPN",
        "PTNET",
        "GSPN",
        "SYMNET",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PNType"

def test_css2color_exists():
    # Check that the Enumeration exists
    assert CSS2Color is not None

def test_css2color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2Color]
    expected_literals = [
        "NAVY",
        "ORANGE",
        "TEAL",
        "LIME",
        "RED",
        "FUCHSIA",
        "YELLOW",
        "OLIVE",
        "BLACK",
        "AQUA",
        "GREEN",
        "SILVER",
        "PURPLE",
        "WHITE",
        "BLUE",
        "GRAY",
        "MAROON",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CSS2Color"

def test_gspnarctype_exists():
    # Check that the Enumeration exists
    assert GSPNArcType is not None

def test_gspnarctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GSPNArcType]
    expected_literals = [
        "inhibitor",
        "normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GSPNArcType"

def test_linestyle_exists():
    # Check that the Enumeration exists
    assert LineStyle is not None

def test_linestyle_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineStyle]
    expected_literals = [
        "DASH",
        "DOT",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineStyle"

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

def test_lineshape_exists():
    # Check that the Enumeration exists
    assert LineShape is not None

def test_lineshape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineShape]
    expected_literals = [
        "LINE",
        "CURVE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineShape"

def test_fontalign_exists():
    # Check that the Enumeration exists
    assert FontAlign is not None

def test_fontalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FontAlign]
    expected_literals = [
        "LEFT",
        "CENTER",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FontAlign"

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

def test_css2fontfamily_exists():
    # Check that the Enumeration exists
    assert CSS2FontFamily is not None

def test_css2fontfamily_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CSS2FontFamily]
    expected_literals = [
        "TREBUCHET",
        "GEORGIA",
        "TIMES",
        "VERDANA",
        "ARIAL",
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
        "DIAGONAL",
        "VERTICAL",
        "HORIZONTAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Gradient"

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
ptnet_Variable_strategy = st.builds(
    ptnet_Variable,
    name=
        safe_text
)
BooleanExpression_strategy = st.builds(
    BooleanExpression,
)
ptnet_OpOr_strategy = st.builds(
    ptnet_OpOr,
)
ptnet_OpAnd_strategy = st.builds(
    ptnet_OpAnd,
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
ptnet_OpGreater_strategy = st.builds(
    ptnet_OpGreater,
)
ptnet_OpLessEqual_strategy = st.builds(
    ptnet_OpLessEqual,
)
ptnet_OpGreaterEqual_strategy = st.builds(
    ptnet_OpGreaterEqual,
)
ptnet_OpLess_strategy = st.builds(
    ptnet_OpLess,
)
ptnet_OpEqual_strategy = st.builds(
    ptnet_OpEqual,
)
EvaluationType_strategy = st.builds(
    EvaluationType,
)
ptnet_InstantOfTime_strategy = st.builds(
    ptnet_InstantOfTime,
)
ptnet_IntervalOfTime_strategy = st.builds(
    ptnet_IntervalOfTime,
)
ptnet_IntervalOfTimeAveraged_strategy = st.builds(
    ptnet_IntervalOfTimeAveraged,
)
ptnet_SteadyState_strategy = st.builds(
    ptnet_SteadyState,
)
ArithmeticBinaryOperator_strategy = st.builds(
    ArithmeticBinaryOperator,
)
ptnet_OpDivide_strategy = st.builds(
    ptnet_OpDivide,
)
ptnet_OpMultiply_strategy = st.builds(
    ptnet_OpMultiply,
)
ptnet_OpMinus_strategy = st.builds(
    ptnet_OpMinus,
)
ptnet_OpSum_strategy = st.builds(
    ptnet_OpSum,
)
LogicalExpression_strategy = st.builds(
    LogicalExpression,
)
ptnet_BooleanExpression_strategy = st.builds(
    ptnet_BooleanExpression,
)
ptnet_OpFalse_strategy = st.builds(
    ptnet_OpFalse,
)
ptnet_ComparisonOperator_strategy = st.builds(
    ptnet_ComparisonOperator,
)
ptnet_OpNot_strategy = st.builds(
    ptnet_OpNot,
)
ptnet_OpTrue_strategy = st.builds(
    ptnet_OpTrue,
)
ptnet_EvaluationType_strategy = st.builds(
    ptnet_EvaluationType,
)
ptnet_VariableValues_strategy = st.builds(
    ptnet_VariableValues,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Measure_strategy = st.builds(
    ptnet_Measure,
    name=
        safe_text
)
ptnet_Study_strategy = st.builds(
    ptnet_Study,
    name=
        safe_text
)
ptnet_EvaluationList_strategy = st.builds(
    ptnet_EvaluationList,
)
Expression_strategy = st.builds(
    Expression,
)
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
ptnet_IfThenElse_strategy = st.builds(
    ptnet_IfThenElse,
)
ptnet_ArithmeticBinaryOperator_strategy = st.builds(
    ptnet_ArithmeticBinaryOperator,
)
ptnet_MarkingExpression_strategy = st.builds(
    ptnet_MarkingExpression,
)
ptnet_VariableExpression_strategy = st.builds(
    ptnet_VariableExpression,
)
ptnet_ValueExpression_strategy = st.builds(
    ptnet_ValueExpression,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Expression_strategy = st.builds(
    ptnet_Expression,
)
Distribution_strategy = st.builds(
    Distribution,
)
ptnet_Gaussian_strategy = st.builds(
    ptnet_Gaussian,
    Variance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Mean=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Exponential_strategy = st.builds(
    ptnet_Exponential,
    Rate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Deterministic_strategy = st.builds(
    ptnet_Deterministic,
    Value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Distribution_strategy = st.builds(
    ptnet_Distribution,
)
GSPNTransition_strategy = st.builds(
    GSPNTransition,
)
ptnet_GSPNTimedTransition_strategy = st.builds(
    ptnet_GSPNTimedTransition,
)
ptnet_GSPNImmediateTransition_strategy = st.builds(
    ptnet_GSPNImmediateTransition,
    Weight=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Priority=
        st.integers()
)
ptnet_ArithmeticExpression_strategy = st.builds(
    ptnet_ArithmeticExpression,
)
ptnet_Weibull_strategy = st.builds(
    ptnet_Weibull,
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Gamma_strategy = st.builds(
    ptnet_Gamma,
    Beta=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Alpha=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
ptnet_Uniform_strategy = st.builds(
    ptnet_Uniform,
    Upper=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    Lower=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Label_strategy = st.builds(
    Label,
)
ptnet_Attribute_strategy = st.builds(
    ptnet_Attribute,
)
Arc_strategy = st.builds(
    Arc,
)
ptnet_GSPNArc_strategy = st.builds(
    ptnet_GSPNArc,
    type=
        safe_text
)
ptnet_LogicalExpression_strategy = st.builds(
    ptnet_LogicalExpression,
)
Transition_strategy = st.builds(
    Transition,
)
ptnet_GSPNTransition_strategy = st.builds(
    ptnet_GSPNTransition,
)
Node_strategy = st.builds(
    Node,
)
ptnet_TransitionNode_strategy = st.builds(
    ptnet_TransitionNode,
)
ptnet_PlaceNode_strategy = st.builds(
    ptnet_PlaceNode,
)
TransitionNode_strategy = st.builds(
    TransitionNode,
)
ptnet_RefTransition_strategy = st.builds(
    ptnet_RefTransition,
)
ptnet_Transition_strategy = st.builds(
    ptnet_Transition,
)
PlaceNode_strategy = st.builds(
    PlaceNode,
)
ptnet_RefPlace_strategy = st.builds(
    ptnet_RefPlace,
)
ptnet_Annotation_strategy = st.builds(
    ptnet_Annotation,
)
ptnet_Font_strategy = st.builds(
    ptnet_Font,
    family=
        safe_text,
    rotation=
        safe_text,
    style=
        safe_text,
    decoration=
        safe_text,
    weight=
        safe_text,
    size=
        safe_text,
    align=
        safe_text
)
ptnet_Graphics_strategy = st.builds(
    ptnet_Graphics,
)
ptnet_Line_strategy = st.builds(
    ptnet_Line,
    color=
        safe_text,
    width=
        safe_text,
    style=
        safe_text,
    shape=
        safe_text
)
Coordinate_strategy = st.builds(
    Coordinate,
)
ptnet_Offset_strategy = st.builds(
    ptnet_Offset,
)
ptnet_Coordinate_strategy = st.builds(
    ptnet_Coordinate,
    y=
        safe_text,
    x=
        safe_text
)
ptnet_AnyObject_strategy = st.builds(
    ptnet_AnyObject,
)
ptnet_Label_strategy = st.builds(
    ptnet_Label,
)
ptnet_Fill_strategy = st.builds(
    ptnet_Fill,
    color=
        safe_text,
    gradientrotation=
        safe_text,
    image=
        safe_text,
    gradientcolor=
        safe_text
)
ptnet_Dimension_strategy = st.builds(
    ptnet_Dimension,
)
ptnet_Position_strategy = st.builds(
    ptnet_Position,
)
Graphics_strategy = st.builds(
    Graphics,
)
ptnet_AnnotationGraphics_strategy = st.builds(
    ptnet_AnnotationGraphics,
)
ptnet_ArcGraphics_strategy = st.builds(
    ptnet_ArcGraphics,
)
ptnet_NodeGraphics_strategy = st.builds(
    ptnet_NodeGraphics,
)
ptnet_PnObject_strategy = st.builds(
    ptnet_PnObject,
    id=
        safe_text
)
ptnet_PetriNet_strategy = st.builds(
    ptnet_PetriNet,
    type=
        safe_text,
    id=
        safe_text
)
ptnet_PetriNetDoc_strategy = st.builds(
    ptnet_PetriNetDoc,
    xmlns=
        safe_text
)
ptnet_Place_strategy = st.builds(
    ptnet_Place,
)
PnObject_strategy = st.builds(
    PnObject,
)
ptnet_Arc_strategy = st.builds(
    ptnet_Arc,
)
ptnet_Page_strategy = st.builds(
    ptnet_Page,
)
ptnet_Node_strategy = st.builds(
    ptnet_Node,
)
ptnet_ToolInfo_strategy = st.builds(
    ptnet_ToolInfo,
    version=
        safe_text,
    toolInfoGrammarURI=
        safe_text,
    formattedXMLBuffer=
        safe_text,
    tool=
        safe_text
)
Annotation_strategy = st.builds(
    Annotation,
)
ptnet_PTArcAnnotation_strategy = st.builds(
    ptnet_PTArcAnnotation,
    text=
        safe_text
)
ptnet_Name_strategy = st.builds(
    ptnet_Name,
    text=
        safe_text
)
ptnet_PTMarking_strategy = st.builds(
    ptnet_PTMarking,
    text=
        safe_text
)

@given(instance=ptnet_Variable_strategy)
@settings(max_examples=50)
def test_ptnet_variable_instantiation(instance):
    assert isinstance(instance, ptnet_Variable)



@given(instance=ptnet_Variable_strategy)
def test_ptnet_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BooleanExpression_strategy)
@settings(max_examples=50)
def test_booleanexpression_instantiation(instance):
    assert isinstance(instance, BooleanExpression)

@given(instance=ptnet_OpOr_strategy)
@settings(max_examples=50)
def test_ptnet_opor_instantiation(instance):
    assert isinstance(instance, ptnet_OpOr)

@given(instance=ptnet_OpAnd_strategy)
@settings(max_examples=50)
def test_ptnet_opand_instantiation(instance):
    assert isinstance(instance, ptnet_OpAnd)

@given(instance=ComparisonOperator_strategy)
@settings(max_examples=50)
def test_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)

@given(instance=ptnet_OpGreater_strategy)
@settings(max_examples=50)
def test_ptnet_opgreater_instantiation(instance):
    assert isinstance(instance, ptnet_OpGreater)

@given(instance=ptnet_OpLessEqual_strategy)
@settings(max_examples=50)
def test_ptnet_oplessequal_instantiation(instance):
    assert isinstance(instance, ptnet_OpLessEqual)

@given(instance=ptnet_OpGreaterEqual_strategy)
@settings(max_examples=50)
def test_ptnet_opgreaterequal_instantiation(instance):
    assert isinstance(instance, ptnet_OpGreaterEqual)

@given(instance=ptnet_OpLess_strategy)
@settings(max_examples=50)
def test_ptnet_opless_instantiation(instance):
    assert isinstance(instance, ptnet_OpLess)

@given(instance=ptnet_OpEqual_strategy)
@settings(max_examples=50)
def test_ptnet_opequal_instantiation(instance):
    assert isinstance(instance, ptnet_OpEqual)

@given(instance=EvaluationType_strategy)
@settings(max_examples=50)
def test_evaluationtype_instantiation(instance):
    assert isinstance(instance, EvaluationType)

@given(instance=ptnet_InstantOfTime_strategy)
@settings(max_examples=50)
def test_ptnet_instantoftime_instantiation(instance):
    assert isinstance(instance, ptnet_InstantOfTime)

@given(instance=ptnet_IntervalOfTime_strategy)
@settings(max_examples=50)
def test_ptnet_intervaloftime_instantiation(instance):
    assert isinstance(instance, ptnet_IntervalOfTime)

@given(instance=ptnet_IntervalOfTimeAveraged_strategy)
@settings(max_examples=50)
def test_ptnet_intervaloftimeaveraged_instantiation(instance):
    assert isinstance(instance, ptnet_IntervalOfTimeAveraged)

@given(instance=ptnet_SteadyState_strategy)
@settings(max_examples=50)
def test_ptnet_steadystate_instantiation(instance):
    assert isinstance(instance, ptnet_SteadyState)

@given(instance=ArithmeticBinaryOperator_strategy)
@settings(max_examples=50)
def test_arithmeticbinaryoperator_instantiation(instance):
    assert isinstance(instance, ArithmeticBinaryOperator)

@given(instance=ptnet_OpDivide_strategy)
@settings(max_examples=50)
def test_ptnet_opdivide_instantiation(instance):
    assert isinstance(instance, ptnet_OpDivide)

@given(instance=ptnet_OpMultiply_strategy)
@settings(max_examples=50)
def test_ptnet_opmultiply_instantiation(instance):
    assert isinstance(instance, ptnet_OpMultiply)

@given(instance=ptnet_OpMinus_strategy)
@settings(max_examples=50)
def test_ptnet_opminus_instantiation(instance):
    assert isinstance(instance, ptnet_OpMinus)

@given(instance=ptnet_OpSum_strategy)
@settings(max_examples=50)
def test_ptnet_opsum_instantiation(instance):
    assert isinstance(instance, ptnet_OpSum)

@given(instance=LogicalExpression_strategy)
@settings(max_examples=50)
def test_logicalexpression_instantiation(instance):
    assert isinstance(instance, LogicalExpression)

@given(instance=ptnet_BooleanExpression_strategy)
@settings(max_examples=50)
def test_ptnet_booleanexpression_instantiation(instance):
    assert isinstance(instance, ptnet_BooleanExpression)

@given(instance=ptnet_OpFalse_strategy)
@settings(max_examples=50)
def test_ptnet_opfalse_instantiation(instance):
    assert isinstance(instance, ptnet_OpFalse)

@given(instance=ptnet_ComparisonOperator_strategy)
@settings(max_examples=50)
def test_ptnet_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ptnet_ComparisonOperator)

@given(instance=ptnet_OpNot_strategy)
@settings(max_examples=50)
def test_ptnet_opnot_instantiation(instance):
    assert isinstance(instance, ptnet_OpNot)

@given(instance=ptnet_OpTrue_strategy)
@settings(max_examples=50)
def test_ptnet_optrue_instantiation(instance):
    assert isinstance(instance, ptnet_OpTrue)

@given(instance=ptnet_EvaluationType_strategy)
@settings(max_examples=50)
def test_ptnet_evaluationtype_instantiation(instance):
    assert isinstance(instance, ptnet_EvaluationType)

@given(instance=ptnet_VariableValues_strategy)
@settings(max_examples=50)
def test_ptnet_variablevalues_instantiation(instance):
    assert isinstance(instance, ptnet_VariableValues)



@given(instance=ptnet_VariableValues_strategy)
def test_ptnet_variablevalues_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=ptnet_Measure_strategy)
@settings(max_examples=50)
def test_ptnet_measure_instantiation(instance):
    assert isinstance(instance, ptnet_Measure)



@given(instance=ptnet_Measure_strategy)
def test_ptnet_measure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnet_Study_strategy)
@settings(max_examples=50)
def test_ptnet_study_instantiation(instance):
    assert isinstance(instance, ptnet_Study)



@given(instance=ptnet_Study_strategy)
def test_ptnet_study_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ptnet_EvaluationList_strategy)
@settings(max_examples=50)
def test_ptnet_evaluationlist_instantiation(instance):
    assert isinstance(instance, ptnet_EvaluationList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=ptnet_IfThenElse_strategy)
@settings(max_examples=50)
def test_ptnet_ifthenelse_instantiation(instance):
    assert isinstance(instance, ptnet_IfThenElse)

@given(instance=ptnet_ArithmeticBinaryOperator_strategy)
@settings(max_examples=50)
def test_ptnet_arithmeticbinaryoperator_instantiation(instance):
    assert isinstance(instance, ptnet_ArithmeticBinaryOperator)

@given(instance=ptnet_MarkingExpression_strategy)
@settings(max_examples=50)
def test_ptnet_markingexpression_instantiation(instance):
    assert isinstance(instance, ptnet_MarkingExpression)

@given(instance=ptnet_VariableExpression_strategy)
@settings(max_examples=50)
def test_ptnet_variableexpression_instantiation(instance):
    assert isinstance(instance, ptnet_VariableExpression)

@given(instance=ptnet_ValueExpression_strategy)
@settings(max_examples=50)
def test_ptnet_valueexpression_instantiation(instance):
    assert isinstance(instance, ptnet_ValueExpression)



@given(instance=ptnet_ValueExpression_strategy)
def test_ptnet_valueexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ptnet_Expression_strategy)
@settings(max_examples=50)
def test_ptnet_expression_instantiation(instance):
    assert isinstance(instance, ptnet_Expression)

@given(instance=Distribution_strategy)
@settings(max_examples=50)
def test_distribution_instantiation(instance):
    assert isinstance(instance, Distribution)

@given(instance=ptnet_Gaussian_strategy)
@settings(max_examples=50)
def test_ptnet_gaussian_instantiation(instance):
    assert isinstance(instance, ptnet_Gaussian)



@given(instance=ptnet_Gaussian_strategy)
def test_ptnet_gaussian_Variance_setter(instance):
    original = instance.Variance
    instance.Variance = original
    assert instance.Variance == original



@given(instance=ptnet_Gaussian_strategy)
def test_ptnet_gaussian_Mean_setter(instance):
    original = instance.Mean
    instance.Mean = original
    assert instance.Mean == original

@given(instance=ptnet_Exponential_strategy)
@settings(max_examples=50)
def test_ptnet_exponential_instantiation(instance):
    assert isinstance(instance, ptnet_Exponential)



@given(instance=ptnet_Exponential_strategy)
def test_ptnet_exponential_Rate_setter(instance):
    original = instance.Rate
    instance.Rate = original
    assert instance.Rate == original

@given(instance=ptnet_Deterministic_strategy)
@settings(max_examples=50)
def test_ptnet_deterministic_instantiation(instance):
    assert isinstance(instance, ptnet_Deterministic)



@given(instance=ptnet_Deterministic_strategy)
def test_ptnet_deterministic_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=ptnet_Distribution_strategy)
@settings(max_examples=50)
def test_ptnet_distribution_instantiation(instance):
    assert isinstance(instance, ptnet_Distribution)

@given(instance=GSPNTransition_strategy)
@settings(max_examples=50)
def test_gspntransition_instantiation(instance):
    assert isinstance(instance, GSPNTransition)

@given(instance=ptnet_GSPNTimedTransition_strategy)
@settings(max_examples=50)
def test_ptnet_gspntimedtransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNTimedTransition)

@given(instance=ptnet_GSPNImmediateTransition_strategy)
@settings(max_examples=50)
def test_ptnet_gspnimmediatetransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNImmediateTransition)



@given(instance=ptnet_GSPNImmediateTransition_strategy)
def test_ptnet_gspnimmediatetransition_Weight_setter(instance):
    original = instance.Weight
    instance.Weight = original
    assert instance.Weight == original



@given(instance=ptnet_GSPNImmediateTransition_strategy)
def test_ptnet_gspnimmediatetransition_Priority_setter(instance):
    original = instance.Priority
    instance.Priority = original
    assert instance.Priority == original

@given(instance=ptnet_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_ptnet_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ptnet_ArithmeticExpression)

@given(instance=ptnet_Weibull_strategy)
@settings(max_examples=50)
def test_ptnet_weibull_instantiation(instance):
    assert isinstance(instance, ptnet_Weibull)



@given(instance=ptnet_Weibull_strategy)
def test_ptnet_weibull_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original



@given(instance=ptnet_Weibull_strategy)
def test_ptnet_weibull_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original

@given(instance=ptnet_Gamma_strategy)
@settings(max_examples=50)
def test_ptnet_gamma_instantiation(instance):
    assert isinstance(instance, ptnet_Gamma)



@given(instance=ptnet_Gamma_strategy)
def test_ptnet_gamma_Beta_setter(instance):
    original = instance.Beta
    instance.Beta = original
    assert instance.Beta == original



@given(instance=ptnet_Gamma_strategy)
def test_ptnet_gamma_Alpha_setter(instance):
    original = instance.Alpha
    instance.Alpha = original
    assert instance.Alpha == original

@given(instance=ptnet_Uniform_strategy)
@settings(max_examples=50)
def test_ptnet_uniform_instantiation(instance):
    assert isinstance(instance, ptnet_Uniform)



@given(instance=ptnet_Uniform_strategy)
def test_ptnet_uniform_Upper_setter(instance):
    original = instance.Upper
    instance.Upper = original
    assert instance.Upper == original



@given(instance=ptnet_Uniform_strategy)
def test_ptnet_uniform_Lower_setter(instance):
    original = instance.Lower
    instance.Lower = original
    assert instance.Lower == original

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=ptnet_Attribute_strategy)
@settings(max_examples=50)
def test_ptnet_attribute_instantiation(instance):
    assert isinstance(instance, ptnet_Attribute)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=ptnet_GSPNArc_strategy)
@settings(max_examples=50)
def test_ptnet_gspnarc_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNArc)



@given(instance=ptnet_GSPNArc_strategy)
def test_ptnet_gspnarc_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ptnet_LogicalExpression_strategy)
@settings(max_examples=50)
def test_ptnet_logicalexpression_instantiation(instance):
    assert isinstance(instance, ptnet_LogicalExpression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=ptnet_GSPNTransition_strategy)
@settings(max_examples=50)
def test_ptnet_gspntransition_instantiation(instance):
    assert isinstance(instance, ptnet_GSPNTransition)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ptnet_TransitionNode_strategy)
@settings(max_examples=50)
def test_ptnet_transitionnode_instantiation(instance):
    assert isinstance(instance, ptnet_TransitionNode)

@given(instance=ptnet_PlaceNode_strategy)
@settings(max_examples=50)
def test_ptnet_placenode_instantiation(instance):
    assert isinstance(instance, ptnet_PlaceNode)

@given(instance=TransitionNode_strategy)
@settings(max_examples=50)
def test_transitionnode_instantiation(instance):
    assert isinstance(instance, TransitionNode)

@given(instance=ptnet_RefTransition_strategy)
@settings(max_examples=50)
def test_ptnet_reftransition_instantiation(instance):
    assert isinstance(instance, ptnet_RefTransition)

@given(instance=ptnet_Transition_strategy)
@settings(max_examples=50)
def test_ptnet_transition_instantiation(instance):
    assert isinstance(instance, ptnet_Transition)

@given(instance=PlaceNode_strategy)
@settings(max_examples=50)
def test_placenode_instantiation(instance):
    assert isinstance(instance, PlaceNode)

@given(instance=ptnet_RefPlace_strategy)
@settings(max_examples=50)
def test_ptnet_refplace_instantiation(instance):
    assert isinstance(instance, ptnet_RefPlace)

@given(instance=ptnet_Annotation_strategy)
@settings(max_examples=50)
def test_ptnet_annotation_instantiation(instance):
    assert isinstance(instance, ptnet_Annotation)

@given(instance=ptnet_Font_strategy)
@settings(max_examples=50)
def test_ptnet_font_instantiation(instance):
    assert isinstance(instance, ptnet_Font)



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_family_setter(instance):
    original = instance.family
    instance.family = original
    assert instance.family == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_rotation_setter(instance):
    original = instance.rotation
    instance.rotation = original
    assert instance.rotation == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_decoration_setter(instance):
    original = instance.decoration
    instance.decoration = original
    assert instance.decoration == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ptnet_Font_strategy)
def test_ptnet_font_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=ptnet_Graphics_strategy)
@settings(max_examples=50)
def test_ptnet_graphics_instantiation(instance):
    assert isinstance(instance, ptnet_Graphics)

@given(instance=ptnet_Line_strategy)
@settings(max_examples=50)
def test_ptnet_line_instantiation(instance):
    assert isinstance(instance, ptnet_Line)



@given(instance=ptnet_Line_strategy)
def test_ptnet_line_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=ptnet_Line_strategy)
def test_ptnet_line_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=ptnet_Line_strategy)
def test_ptnet_line_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=ptnet_Line_strategy)
def test_ptnet_line_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=Coordinate_strategy)
@settings(max_examples=50)
def test_coordinate_instantiation(instance):
    assert isinstance(instance, Coordinate)

@given(instance=ptnet_Offset_strategy)
@settings(max_examples=50)
def test_ptnet_offset_instantiation(instance):
    assert isinstance(instance, ptnet_Offset)

@given(instance=ptnet_Coordinate_strategy)
@settings(max_examples=50)
def test_ptnet_coordinate_instantiation(instance):
    assert isinstance(instance, ptnet_Coordinate)



@given(instance=ptnet_Coordinate_strategy)
def test_ptnet_coordinate_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=ptnet_Coordinate_strategy)
def test_ptnet_coordinate_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=ptnet_AnyObject_strategy)
@settings(max_examples=50)
def test_ptnet_anyobject_instantiation(instance):
    assert isinstance(instance, ptnet_AnyObject)

@given(instance=ptnet_Label_strategy)
@settings(max_examples=50)
def test_ptnet_label_instantiation(instance):
    assert isinstance(instance, ptnet_Label)

@given(instance=ptnet_Fill_strategy)
@settings(max_examples=50)
def test_ptnet_fill_instantiation(instance):
    assert isinstance(instance, ptnet_Fill)



@given(instance=ptnet_Fill_strategy)
def test_ptnet_fill_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=ptnet_Fill_strategy)
def test_ptnet_fill_gradientrotation_setter(instance):
    original = instance.gradientrotation
    instance.gradientrotation = original
    assert instance.gradientrotation == original



@given(instance=ptnet_Fill_strategy)
def test_ptnet_fill_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=ptnet_Fill_strategy)
def test_ptnet_fill_gradientcolor_setter(instance):
    original = instance.gradientcolor
    instance.gradientcolor = original
    assert instance.gradientcolor == original

@given(instance=ptnet_Dimension_strategy)
@settings(max_examples=50)
def test_ptnet_dimension_instantiation(instance):
    assert isinstance(instance, ptnet_Dimension)

@given(instance=ptnet_Position_strategy)
@settings(max_examples=50)
def test_ptnet_position_instantiation(instance):
    assert isinstance(instance, ptnet_Position)

@given(instance=Graphics_strategy)
@settings(max_examples=50)
def test_graphics_instantiation(instance):
    assert isinstance(instance, Graphics)

@given(instance=ptnet_AnnotationGraphics_strategy)
@settings(max_examples=50)
def test_ptnet_annotationgraphics_instantiation(instance):
    assert isinstance(instance, ptnet_AnnotationGraphics)

@given(instance=ptnet_ArcGraphics_strategy)
@settings(max_examples=50)
def test_ptnet_arcgraphics_instantiation(instance):
    assert isinstance(instance, ptnet_ArcGraphics)

@given(instance=ptnet_NodeGraphics_strategy)
@settings(max_examples=50)
def test_ptnet_nodegraphics_instantiation(instance):
    assert isinstance(instance, ptnet_NodeGraphics)

@given(instance=ptnet_PnObject_strategy)
@settings(max_examples=50)
def test_ptnet_pnobject_instantiation(instance):
    assert isinstance(instance, ptnet_PnObject)



@given(instance=ptnet_PnObject_strategy)
def test_ptnet_pnobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ptnet_PetriNet_strategy)
@settings(max_examples=50)
def test_ptnet_petrinet_instantiation(instance):
    assert isinstance(instance, ptnet_PetriNet)



@given(instance=ptnet_PetriNet_strategy)
def test_ptnet_petrinet_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ptnet_PetriNet_strategy)
def test_ptnet_petrinet_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ptnet_PetriNetDoc_strategy)
@settings(max_examples=50)
def test_ptnet_petrinetdoc_instantiation(instance):
    assert isinstance(instance, ptnet_PetriNetDoc)



@given(instance=ptnet_PetriNetDoc_strategy)
def test_ptnet_petrinetdoc_xmlns_setter(instance):
    original = instance.xmlns
    instance.xmlns = original
    assert instance.xmlns == original

@given(instance=ptnet_Place_strategy)
@settings(max_examples=50)
def test_ptnet_place_instantiation(instance):
    assert isinstance(instance, ptnet_Place)

@given(instance=PnObject_strategy)
@settings(max_examples=50)
def test_pnobject_instantiation(instance):
    assert isinstance(instance, PnObject)

@given(instance=ptnet_Arc_strategy)
@settings(max_examples=50)
def test_ptnet_arc_instantiation(instance):
    assert isinstance(instance, ptnet_Arc)

@given(instance=ptnet_Page_strategy)
@settings(max_examples=50)
def test_ptnet_page_instantiation(instance):
    assert isinstance(instance, ptnet_Page)

@given(instance=ptnet_Node_strategy)
@settings(max_examples=50)
def test_ptnet_node_instantiation(instance):
    assert isinstance(instance, ptnet_Node)

@given(instance=ptnet_ToolInfo_strategy)
@settings(max_examples=50)
def test_ptnet_toolinfo_instantiation(instance):
    assert isinstance(instance, ptnet_ToolInfo)



@given(instance=ptnet_ToolInfo_strategy)
def test_ptnet_toolinfo_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=ptnet_ToolInfo_strategy)
def test_ptnet_toolinfo_toolInfoGrammarURI_setter(instance):
    original = instance.toolInfoGrammarURI
    instance.toolInfoGrammarURI = original
    assert instance.toolInfoGrammarURI == original



@given(instance=ptnet_ToolInfo_strategy)
def test_ptnet_toolinfo_formattedXMLBuffer_setter(instance):
    original = instance.formattedXMLBuffer
    instance.formattedXMLBuffer = original
    assert instance.formattedXMLBuffer == original



@given(instance=ptnet_ToolInfo_strategy)
def test_ptnet_toolinfo_tool_setter(instance):
    original = instance.tool
    instance.tool = original
    assert instance.tool == original

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=ptnet_PTArcAnnotation_strategy)
@settings(max_examples=50)
def test_ptnet_ptarcannotation_instantiation(instance):
    assert isinstance(instance, ptnet_PTArcAnnotation)



@given(instance=ptnet_PTArcAnnotation_strategy)
def test_ptnet_ptarcannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ptnet_Name_strategy)
@settings(max_examples=50)
def test_ptnet_name_instantiation(instance):
    assert isinstance(instance, ptnet_Name)



@given(instance=ptnet_Name_strategy)
def test_ptnet_name_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=ptnet_PTMarking_strategy)
@settings(max_examples=50)
def test_ptnet_ptmarking_instantiation(instance):
    assert isinstance(instance, ptnet_PTMarking)



@given(instance=ptnet_PTMarking_strategy)
def test_ptnet_ptmarking_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
