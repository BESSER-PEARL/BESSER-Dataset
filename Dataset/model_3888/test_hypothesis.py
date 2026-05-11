import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TerminalExpression,
    gaml::DoubleLiteral,
    gaml::BooleanLiteral,
    gaml::ColorLiteral,
    gaml::ReservedLiteral,
    gaml::StringLiteral,
    gaml::IntLiteral,
    S::Definition,
    gaml::S::Var,
    gaml::S::Action,
    gaml::TypeInfo,
    GamlDefinition,
    gaml::VarDefinition,
    gaml::UnitFakeDefinition,
    gaml::ActionDefinition,
    gaml::SkillFakeDefinition,
    gaml::EquationDefinition,
    gaml::GamlDefinition,
    Expression,
    gaml::Pair,
    gaml::TypeRef,
    gaml::Point,
    gaml::ExpressionList,
    gaml::ArgumentPair,
    gaml::Array,
    gaml::Cast,
    gaml::Unary,
    gaml::UnitName,
    gaml::SkillRef,
    gaml::If,
    gaml::VariableRef,
    gaml::Parameter,
    gaml::ActionRef,
    gaml::Unit,
    gaml::Access,
    gaml::Function,
    gaml::TerminalExpression,
    gaml::EquationRef,
    gaml::Binary,
    gaml::Parameters,
    gaml::EObject,
    TypeDefinition,
    gaml::TypeFakeDefinition,
    S::Declaration,
    gaml::S::Loop,
    Statement,
    gaml::S::Return,
    gaml::S::Other,
    gaml::S::Species,
    gaml::S::Do,
    gaml::S::If,
    gaml::speciesOrGridDisplayStatement,
    gaml::S::Global,
    gaml::S::Display,
    gaml::S::Solve,
    EquationDefinition,
    gaml::EquationFakeDefinition,
    gaml::S::Equations,
    S::Assignment,
    gaml::S::Set,
    gaml::S::DirectAssignment,
    gaml::S::Assignment,
    gaml::ActionArguments,
    ActionDefinition,
    gaml::TypeDefinition,
    gaml::ActionFakeDefinition,
    gaml::S::Definition,
    gaml::S::Reflex,
    gaml::Statement,
    gaml::Pragma,
    VarDefinition,
    gaml::ArgumentDefinition,
    gaml::S::Declaration,
    gaml::VarFakeDefinition,
    gaml::S::Experiment,
    gaml::Import,
    gaml::Expression,
    gaml::Block,
    gaml::Facet,
    gaml::HeadlessExperiment,
    Entry,
    gaml::StringEvaluator,
    gaml::Model,
    gaml::ExperimentFileStructure,
    gaml::StandaloneBlock,
    gaml::Entry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_terminalexpression_is_not_abstract():
    assert not inspect.isabstract(TerminalExpression)


def test_terminalexpression_constructor_exists():
    assert callable(TerminalExpression.__init__)


def test_terminalexpression_constructor_args():
    sig = inspect.signature(TerminalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gaml::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::DoubleLiteral)


def test_gaml::doubleliteral_constructor_exists():
    assert callable(gaml::DoubleLiteral.__init__)


def test_gaml::doubleliteral_constructor_args():
    sig = inspect.signature(gaml::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::BooleanLiteral)


def test_gaml::booleanliteral_constructor_exists():
    assert callable(gaml::BooleanLiteral.__init__)


def test_gaml::booleanliteral_constructor_args():
    sig = inspect.signature(gaml::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml::colorliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::ColorLiteral)


def test_gaml::colorliteral_constructor_exists():
    assert callable(gaml::ColorLiteral.__init__)


def test_gaml::colorliteral_constructor_args():
    sig = inspect.signature(gaml::ColorLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml::reservedliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::ReservedLiteral)


def test_gaml::reservedliteral_constructor_exists():
    assert callable(gaml::ReservedLiteral.__init__)


def test_gaml::reservedliteral_constructor_args():
    sig = inspect.signature(gaml::ReservedLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml::stringliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::StringLiteral)


def test_gaml::stringliteral_constructor_exists():
    assert callable(gaml::StringLiteral.__init__)


def test_gaml::stringliteral_constructor_args():
    sig = inspect.signature(gaml::StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml::intliteral_is_not_abstract():
    assert not inspect.isabstract(gaml::IntLiteral)


def test_gaml::intliteral_constructor_exists():
    assert callable(gaml::IntLiteral.__init__)


def test_gaml::intliteral_constructor_args():
    sig = inspect.signature(gaml::IntLiteral.__init__)
    params = list(sig.parameters.keys())



def test_s::definition_is_not_abstract():
    assert not inspect.isabstract(S::Definition)


def test_s::definition_constructor_exists():
    assert callable(S::Definition.__init__)


def test_s::definition_constructor_args():
    sig = inspect.signature(S::Definition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::var_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Var)


def test_gaml::s::var_constructor_exists():
    assert callable(gaml::S::Var.__init__)


def test_gaml::s::var_constructor_args():
    sig = inspect.signature(gaml::S::Var.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::action_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Action)


def test_gaml::s::action_constructor_exists():
    assert callable(gaml::S::Action.__init__)


def test_gaml::s::action_constructor_args():
    sig = inspect.signature(gaml::S::Action.__init__)
    params = list(sig.parameters.keys())



def test_gaml::typeinfo_is_not_abstract():
    assert not inspect.isabstract(gaml::TypeInfo)


def test_gaml::typeinfo_constructor_exists():
    assert callable(gaml::TypeInfo.__init__)


def test_gaml::typeinfo_constructor_args():
    sig = inspect.signature(gaml::TypeInfo.__init__)
    params = list(sig.parameters.keys())



def test_gamldefinition_is_not_abstract():
    assert not inspect.isabstract(GamlDefinition)


def test_gamldefinition_constructor_exists():
    assert callable(GamlDefinition.__init__)


def test_gamldefinition_constructor_args():
    sig = inspect.signature(GamlDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::vardefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::VarDefinition)


def test_gaml::vardefinition_constructor_exists():
    assert callable(gaml::VarDefinition.__init__)


def test_gaml::vardefinition_constructor_args():
    sig = inspect.signature(gaml::VarDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::unitfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::UnitFakeDefinition)


def test_gaml::unitfakedefinition_constructor_exists():
    assert callable(gaml::UnitFakeDefinition.__init__)


def test_gaml::unitfakedefinition_constructor_args():
    sig = inspect.signature(gaml::UnitFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::actiondefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::ActionDefinition)


def test_gaml::actiondefinition_constructor_exists():
    assert callable(gaml::ActionDefinition.__init__)


def test_gaml::actiondefinition_constructor_args():
    sig = inspect.signature(gaml::ActionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::skillfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::SkillFakeDefinition)


def test_gaml::skillfakedefinition_constructor_exists():
    assert callable(gaml::SkillFakeDefinition.__init__)


def test_gaml::skillfakedefinition_constructor_args():
    sig = inspect.signature(gaml::SkillFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::equationdefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::EquationDefinition)


def test_gaml::equationdefinition_constructor_exists():
    assert callable(gaml::EquationDefinition.__init__)


def test_gaml::equationdefinition_constructor_args():
    sig = inspect.signature(gaml::EquationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::gamldefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::GamlDefinition)


def test_gaml::gamldefinition_constructor_exists():
    assert callable(gaml::GamlDefinition.__init__)


def test_gaml::gamldefinition_constructor_args():
    sig = inspect.signature(gaml::GamlDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml::gamldefinition_has_name():
    assert hasattr(gaml::GamlDefinition, "name")
    descriptor = None
    for klass in gaml::GamlDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_gaml::pair_is_not_abstract():
    assert not inspect.isabstract(gaml::Pair)


def test_gaml::pair_constructor_exists():
    assert callable(gaml::Pair.__init__)


def test_gaml::pair_constructor_args():
    sig = inspect.signature(gaml::Pair.__init__)
    params = list(sig.parameters.keys())



def test_gaml::typeref_is_not_abstract():
    assert not inspect.isabstract(gaml::TypeRef)


def test_gaml::typeref_constructor_exists():
    assert callable(gaml::TypeRef.__init__)


def test_gaml::typeref_constructor_args():
    sig = inspect.signature(gaml::TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml::point_is_not_abstract():
    assert not inspect.isabstract(gaml::Point)


def test_gaml::point_constructor_exists():
    assert callable(gaml::Point.__init__)


def test_gaml::point_constructor_args():
    sig = inspect.signature(gaml::Point.__init__)
    params = list(sig.parameters.keys())



def test_gaml::expressionlist_is_not_abstract():
    assert not inspect.isabstract(gaml::ExpressionList)


def test_gaml::expressionlist_constructor_exists():
    assert callable(gaml::ExpressionList.__init__)


def test_gaml::expressionlist_constructor_args():
    sig = inspect.signature(gaml::ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_gaml::argumentpair_is_not_abstract():
    assert not inspect.isabstract(gaml::ArgumentPair)


def test_gaml::argumentpair_constructor_exists():
    assert callable(gaml::ArgumentPair.__init__)


def test_gaml::argumentpair_constructor_args():
    sig = inspect.signature(gaml::ArgumentPair.__init__)
    params = list(sig.parameters.keys())



def test_gaml::array_is_not_abstract():
    assert not inspect.isabstract(gaml::Array)


def test_gaml::array_constructor_exists():
    assert callable(gaml::Array.__init__)


def test_gaml::array_constructor_args():
    sig = inspect.signature(gaml::Array.__init__)
    params = list(sig.parameters.keys())



def test_gaml::cast_is_not_abstract():
    assert not inspect.isabstract(gaml::Cast)


def test_gaml::cast_constructor_exists():
    assert callable(gaml::Cast.__init__)


def test_gaml::cast_constructor_args():
    sig = inspect.signature(gaml::Cast.__init__)
    params = list(sig.parameters.keys())



def test_gaml::unary_is_not_abstract():
    assert not inspect.isabstract(gaml::Unary)


def test_gaml::unary_constructor_exists():
    assert callable(gaml::Unary.__init__)


def test_gaml::unary_constructor_args():
    sig = inspect.signature(gaml::Unary.__init__)
    params = list(sig.parameters.keys())



def test_gaml::unitname_is_not_abstract():
    assert not inspect.isabstract(gaml::UnitName)


def test_gaml::unitname_constructor_exists():
    assert callable(gaml::UnitName.__init__)


def test_gaml::unitname_constructor_args():
    sig = inspect.signature(gaml::UnitName.__init__)
    params = list(sig.parameters.keys())



def test_gaml::skillref_is_not_abstract():
    assert not inspect.isabstract(gaml::SkillRef)


def test_gaml::skillref_constructor_exists():
    assert callable(gaml::SkillRef.__init__)


def test_gaml::skillref_constructor_args():
    sig = inspect.signature(gaml::SkillRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml::if_is_not_abstract():
    assert not inspect.isabstract(gaml::If)


def test_gaml::if_constructor_exists():
    assert callable(gaml::If.__init__)


def test_gaml::if_constructor_args():
    sig = inspect.signature(gaml::If.__init__)
    params = list(sig.parameters.keys())



def test_gaml::variableref_is_not_abstract():
    assert not inspect.isabstract(gaml::VariableRef)


def test_gaml::variableref_constructor_exists():
    assert callable(gaml::VariableRef.__init__)


def test_gaml::variableref_constructor_args():
    sig = inspect.signature(gaml::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml::parameter_is_not_abstract():
    assert not inspect.isabstract(gaml::Parameter)


def test_gaml::parameter_constructor_exists():
    assert callable(gaml::Parameter.__init__)


def test_gaml::parameter_constructor_args():
    sig = inspect.signature(gaml::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "builtInFacetKey" in params, "Missing parameter 'builtInFacetKey'"

def test_gaml::parameter_has_builtInFacetKey():
    assert hasattr(gaml::Parameter, "builtInFacetKey")
    descriptor = None
    for klass in gaml::Parameter.__mro__:
        if "builtInFacetKey" in klass.__dict__:
            descriptor = klass.__dict__["builtInFacetKey"]
            break
    assert isinstance(descriptor, property)



def test_gaml::actionref_is_not_abstract():
    assert not inspect.isabstract(gaml::ActionRef)


def test_gaml::actionref_constructor_exists():
    assert callable(gaml::ActionRef.__init__)


def test_gaml::actionref_constructor_args():
    sig = inspect.signature(gaml::ActionRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml::unit_is_not_abstract():
    assert not inspect.isabstract(gaml::Unit)


def test_gaml::unit_constructor_exists():
    assert callable(gaml::Unit.__init__)


def test_gaml::unit_constructor_args():
    sig = inspect.signature(gaml::Unit.__init__)
    params = list(sig.parameters.keys())



def test_gaml::access_is_not_abstract():
    assert not inspect.isabstract(gaml::Access)


def test_gaml::access_constructor_exists():
    assert callable(gaml::Access.__init__)


def test_gaml::access_constructor_args():
    sig = inspect.signature(gaml::Access.__init__)
    params = list(sig.parameters.keys())
    assert "named_exp" in params, "Missing parameter 'named_exp'"

def test_gaml::access_has_named_exp():
    assert hasattr(gaml::Access, "named_exp")
    descriptor = None
    for klass in gaml::Access.__mro__:
        if "named_exp" in klass.__dict__:
            descriptor = klass.__dict__["named_exp"]
            break
    assert isinstance(descriptor, property)



def test_gaml::function_is_not_abstract():
    assert not inspect.isabstract(gaml::Function)


def test_gaml::function_constructor_exists():
    assert callable(gaml::Function.__init__)


def test_gaml::function_constructor_args():
    sig = inspect.signature(gaml::Function.__init__)
    params = list(sig.parameters.keys())



def test_gaml::terminalexpression_is_not_abstract():
    assert not inspect.isabstract(gaml::TerminalExpression)


def test_gaml::terminalexpression_constructor_exists():
    assert callable(gaml::TerminalExpression.__init__)


def test_gaml::terminalexpression_constructor_args():
    sig = inspect.signature(gaml::TerminalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gaml::equationref_is_not_abstract():
    assert not inspect.isabstract(gaml::EquationRef)


def test_gaml::equationref_constructor_exists():
    assert callable(gaml::EquationRef.__init__)


def test_gaml::equationref_constructor_args():
    sig = inspect.signature(gaml::EquationRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml::binary_is_not_abstract():
    assert not inspect.isabstract(gaml::Binary)


def test_gaml::binary_constructor_exists():
    assert callable(gaml::Binary.__init__)


def test_gaml::binary_constructor_args():
    sig = inspect.signature(gaml::Binary.__init__)
    params = list(sig.parameters.keys())



def test_gaml::parameters_is_not_abstract():
    assert not inspect.isabstract(gaml::Parameters)


def test_gaml::parameters_constructor_exists():
    assert callable(gaml::Parameters.__init__)


def test_gaml::parameters_constructor_args():
    sig = inspect.signature(gaml::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_gaml::eobject_is_not_abstract():
    assert not inspect.isabstract(gaml::EObject)


def test_gaml::eobject_constructor_exists():
    assert callable(gaml::EObject.__init__)


def test_gaml::eobject_constructor_args():
    sig = inspect.signature(gaml::EObject.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::typefakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::TypeFakeDefinition)


def test_gaml::typefakedefinition_constructor_exists():
    assert callable(gaml::TypeFakeDefinition.__init__)


def test_gaml::typefakedefinition_constructor_args():
    sig = inspect.signature(gaml::TypeFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_s::declaration_is_not_abstract():
    assert not inspect.isabstract(S::Declaration)


def test_s::declaration_constructor_exists():
    assert callable(S::Declaration.__init__)


def test_s::declaration_constructor_args():
    sig = inspect.signature(S::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::loop_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Loop)


def test_gaml::s::loop_constructor_exists():
    assert callable(gaml::S::Loop.__init__)


def test_gaml::s::loop_constructor_args():
    sig = inspect.signature(gaml::S::Loop.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::return_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Return)


def test_gaml::s::return_constructor_exists():
    assert callable(gaml::S::Return.__init__)


def test_gaml::s::return_constructor_args():
    sig = inspect.signature(gaml::S::Return.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::other_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Other)


def test_gaml::s::other_constructor_exists():
    assert callable(gaml::S::Other.__init__)


def test_gaml::s::other_constructor_args():
    sig = inspect.signature(gaml::S::Other.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::species_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Species)


def test_gaml::s::species_constructor_exists():
    assert callable(gaml::S::Species.__init__)


def test_gaml::s::species_constructor_args():
    sig = inspect.signature(gaml::S::Species.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::do_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Do)


def test_gaml::s::do_constructor_exists():
    assert callable(gaml::S::Do.__init__)


def test_gaml::s::do_constructor_args():
    sig = inspect.signature(gaml::S::Do.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::if_is_not_abstract():
    assert not inspect.isabstract(gaml::S::If)


def test_gaml::s::if_constructor_exists():
    assert callable(gaml::S::If.__init__)


def test_gaml::s::if_constructor_args():
    sig = inspect.signature(gaml::S::If.__init__)
    params = list(sig.parameters.keys())



def test_gaml::speciesorgriddisplaystatement_is_not_abstract():
    assert not inspect.isabstract(gaml::speciesOrGridDisplayStatement)


def test_gaml::speciesorgriddisplaystatement_constructor_exists():
    assert callable(gaml::speciesOrGridDisplayStatement.__init__)


def test_gaml::speciesorgriddisplaystatement_constructor_args():
    sig = inspect.signature(gaml::speciesOrGridDisplayStatement.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::global_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Global)


def test_gaml::s::global_constructor_exists():
    assert callable(gaml::S::Global.__init__)


def test_gaml::s::global_constructor_args():
    sig = inspect.signature(gaml::S::Global.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::display_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Display)


def test_gaml::s::display_constructor_exists():
    assert callable(gaml::S::Display.__init__)


def test_gaml::s::display_constructor_args():
    sig = inspect.signature(gaml::S::Display.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml::s::display_has_name():
    assert hasattr(gaml::S::Display, "name")
    descriptor = None
    for klass in gaml::S::Display.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gaml::s::solve_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Solve)


def test_gaml::s::solve_constructor_exists():
    assert callable(gaml::S::Solve.__init__)


def test_gaml::s::solve_constructor_args():
    sig = inspect.signature(gaml::S::Solve.__init__)
    params = list(sig.parameters.keys())



def test_equationdefinition_is_not_abstract():
    assert not inspect.isabstract(EquationDefinition)


def test_equationdefinition_constructor_exists():
    assert callable(EquationDefinition.__init__)


def test_equationdefinition_constructor_args():
    sig = inspect.signature(EquationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::equationfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::EquationFakeDefinition)


def test_gaml::equationfakedefinition_constructor_exists():
    assert callable(gaml::EquationFakeDefinition.__init__)


def test_gaml::equationfakedefinition_constructor_args():
    sig = inspect.signature(gaml::EquationFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::equations_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Equations)


def test_gaml::s::equations_constructor_exists():
    assert callable(gaml::S::Equations.__init__)


def test_gaml::s::equations_constructor_args():
    sig = inspect.signature(gaml::S::Equations.__init__)
    params = list(sig.parameters.keys())



def test_s::assignment_is_not_abstract():
    assert not inspect.isabstract(S::Assignment)


def test_s::assignment_constructor_exists():
    assert callable(S::Assignment.__init__)


def test_s::assignment_constructor_args():
    sig = inspect.signature(S::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::set_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Set)


def test_gaml::s::set_constructor_exists():
    assert callable(gaml::S::Set.__init__)


def test_gaml::s::set_constructor_args():
    sig = inspect.signature(gaml::S::Set.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::directassignment_is_not_abstract():
    assert not inspect.isabstract(gaml::S::DirectAssignment)


def test_gaml::s::directassignment_constructor_exists():
    assert callable(gaml::S::DirectAssignment.__init__)


def test_gaml::s::directassignment_constructor_args():
    sig = inspect.signature(gaml::S::DirectAssignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::assignment_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Assignment)


def test_gaml::s::assignment_constructor_exists():
    assert callable(gaml::S::Assignment.__init__)


def test_gaml::s::assignment_constructor_args():
    sig = inspect.signature(gaml::S::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml::actionarguments_is_not_abstract():
    assert not inspect.isabstract(gaml::ActionArguments)


def test_gaml::actionarguments_constructor_exists():
    assert callable(gaml::ActionArguments.__init__)


def test_gaml::actionarguments_constructor_args():
    sig = inspect.signature(gaml::ActionArguments.__init__)
    params = list(sig.parameters.keys())



def test_actiondefinition_is_not_abstract():
    assert not inspect.isabstract(ActionDefinition)


def test_actiondefinition_constructor_exists():
    assert callable(ActionDefinition.__init__)


def test_actiondefinition_constructor_args():
    sig = inspect.signature(ActionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::typedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::TypeDefinition)


def test_gaml::typedefinition_constructor_exists():
    assert callable(gaml::TypeDefinition.__init__)


def test_gaml::typedefinition_constructor_args():
    sig = inspect.signature(gaml::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::actionfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::ActionFakeDefinition)


def test_gaml::actionfakedefinition_constructor_exists():
    assert callable(gaml::ActionFakeDefinition.__init__)


def test_gaml::actionfakedefinition_constructor_args():
    sig = inspect.signature(gaml::ActionFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::definition_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Definition)


def test_gaml::s::definition_constructor_exists():
    assert callable(gaml::S::Definition.__init__)


def test_gaml::s::definition_constructor_args():
    sig = inspect.signature(gaml::S::Definition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::reflex_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Reflex)


def test_gaml::s::reflex_constructor_exists():
    assert callable(gaml::S::Reflex.__init__)


def test_gaml::s::reflex_constructor_args():
    sig = inspect.signature(gaml::S::Reflex.__init__)
    params = list(sig.parameters.keys())



def test_gaml::statement_is_not_abstract():
    assert not inspect.isabstract(gaml::Statement)


def test_gaml::statement_constructor_exists():
    assert callable(gaml::Statement.__init__)


def test_gaml::statement_constructor_args():
    sig = inspect.signature(gaml::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "firstFacet" in params, "Missing parameter 'firstFacet'"
    assert "key" in params, "Missing parameter 'key'"

def test_gaml::statement_has_firstFacet():
    assert hasattr(gaml::Statement, "firstFacet")
    descriptor = None
    for klass in gaml::Statement.__mro__:
        if "firstFacet" in klass.__dict__:
            descriptor = klass.__dict__["firstFacet"]
            break
    assert isinstance(descriptor, property)

def test_gaml::statement_has_key():
    assert hasattr(gaml::Statement, "key")
    descriptor = None
    for klass in gaml::Statement.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_gaml::pragma_is_not_abstract():
    assert not inspect.isabstract(gaml::Pragma)


def test_gaml::pragma_constructor_exists():
    assert callable(gaml::Pragma.__init__)


def test_gaml::pragma_constructor_args():
    sig = inspect.signature(gaml::Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml::pragma_has_name():
    assert hasattr(gaml::Pragma, "name")
    descriptor = None
    for klass in gaml::Pragma.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vardefinition_is_not_abstract():
    assert not inspect.isabstract(VarDefinition)


def test_vardefinition_constructor_exists():
    assert callable(VarDefinition.__init__)


def test_vardefinition_constructor_args():
    sig = inspect.signature(VarDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::argumentdefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::ArgumentDefinition)


def test_gaml::argumentdefinition_constructor_exists():
    assert callable(gaml::ArgumentDefinition.__init__)


def test_gaml::argumentdefinition_constructor_args():
    sig = inspect.signature(gaml::ArgumentDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::declaration_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Declaration)


def test_gaml::s::declaration_constructor_exists():
    assert callable(gaml::S::Declaration.__init__)


def test_gaml::s::declaration_constructor_args():
    sig = inspect.signature(gaml::S::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gaml::varfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml::VarFakeDefinition)


def test_gaml::varfakedefinition_constructor_exists():
    assert callable(gaml::VarFakeDefinition.__init__)


def test_gaml::varfakedefinition_constructor_args():
    sig = inspect.signature(gaml::VarFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml::s::experiment_is_not_abstract():
    assert not inspect.isabstract(gaml::S::Experiment)


def test_gaml::s::experiment_constructor_exists():
    assert callable(gaml::S::Experiment.__init__)


def test_gaml::s::experiment_constructor_args():
    sig = inspect.signature(gaml::S::Experiment.__init__)
    params = list(sig.parameters.keys())



def test_gaml::import_is_not_abstract():
    assert not inspect.isabstract(gaml::Import)


def test_gaml::import_constructor_exists():
    assert callable(gaml::Import.__init__)


def test_gaml::import_constructor_args():
    sig = inspect.signature(gaml::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_gaml::import_has_importURI():
    assert hasattr(gaml::Import, "importURI")
    descriptor = None
    for klass in gaml::Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_gaml::expression_is_not_abstract():
    assert not inspect.isabstract(gaml::Expression)


def test_gaml::expression_constructor_exists():
    assert callable(gaml::Expression.__init__)


def test_gaml::expression_constructor_args():
    sig = inspect.signature(gaml::Expression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml::expression_has_op():
    assert hasattr(gaml::Expression, "op")
    descriptor = None
    for klass in gaml::Expression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml::block_is_not_abstract():
    assert not inspect.isabstract(gaml::Block)


def test_gaml::block_constructor_exists():
    assert callable(gaml::Block.__init__)


def test_gaml::block_constructor_args():
    sig = inspect.signature(gaml::Block.__init__)
    params = list(sig.parameters.keys())



def test_gaml::facet_is_not_abstract():
    assert not inspect.isabstract(gaml::Facet)


def test_gaml::facet_constructor_exists():
    assert callable(gaml::Facet.__init__)


def test_gaml::facet_constructor_args():
    sig = inspect.signature(gaml::Facet.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_gaml::facet_has_key():
    assert hasattr(gaml::Facet, "key")
    descriptor = None
    for klass in gaml::Facet.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_gaml::headlessexperiment_is_not_abstract():
    assert not inspect.isabstract(gaml::HeadlessExperiment)


def test_gaml::headlessexperiment_constructor_exists():
    assert callable(gaml::HeadlessExperiment.__init__)


def test_gaml::headlessexperiment_constructor_args():
    sig = inspect.signature(gaml::HeadlessExperiment.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "firstFacet" in params, "Missing parameter 'firstFacet'"
    assert "name" in params, "Missing parameter 'name'"

def test_gaml::headlessexperiment_has_key():
    assert hasattr(gaml::HeadlessExperiment, "key")
    descriptor = None
    for klass in gaml::HeadlessExperiment.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_gaml::headlessexperiment_has_importURI():
    assert hasattr(gaml::HeadlessExperiment, "importURI")
    descriptor = None
    for klass in gaml::HeadlessExperiment.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)

def test_gaml::headlessexperiment_has_firstFacet():
    assert hasattr(gaml::HeadlessExperiment, "firstFacet")
    descriptor = None
    for klass in gaml::HeadlessExperiment.__mro__:
        if "firstFacet" in klass.__dict__:
            descriptor = klass.__dict__["firstFacet"]
            break
    assert isinstance(descriptor, property)

def test_gaml::headlessexperiment_has_name():
    assert hasattr(gaml::HeadlessExperiment, "name")
    descriptor = None
    for klass in gaml::HeadlessExperiment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entry_is_not_abstract():
    assert not inspect.isabstract(Entry)


def test_entry_constructor_exists():
    assert callable(Entry.__init__)


def test_entry_constructor_args():
    sig = inspect.signature(Entry.__init__)
    params = list(sig.parameters.keys())



def test_gaml::stringevaluator_is_not_abstract():
    assert not inspect.isabstract(gaml::StringEvaluator)


def test_gaml::stringevaluator_constructor_exists():
    assert callable(gaml::StringEvaluator.__init__)


def test_gaml::stringevaluator_constructor_args():
    sig = inspect.signature(gaml::StringEvaluator.__init__)
    params = list(sig.parameters.keys())
    assert "toto" in params, "Missing parameter 'toto'"

def test_gaml::stringevaluator_has_toto():
    assert hasattr(gaml::StringEvaluator, "toto")
    descriptor = None
    for klass in gaml::StringEvaluator.__mro__:
        if "toto" in klass.__dict__:
            descriptor = klass.__dict__["toto"]
            break
    assert isinstance(descriptor, property)



def test_gaml::model_is_not_abstract():
    assert not inspect.isabstract(gaml::Model)


def test_gaml::model_constructor_exists():
    assert callable(gaml::Model.__init__)


def test_gaml::model_constructor_args():
    sig = inspect.signature(gaml::Model.__init__)
    params = list(sig.parameters.keys())



def test_gaml::experimentfilestructure_is_not_abstract():
    assert not inspect.isabstract(gaml::ExperimentFileStructure)


def test_gaml::experimentfilestructure_constructor_exists():
    assert callable(gaml::ExperimentFileStructure.__init__)


def test_gaml::experimentfilestructure_constructor_args():
    sig = inspect.signature(gaml::ExperimentFileStructure.__init__)
    params = list(sig.parameters.keys())



def test_gaml::standaloneblock_is_not_abstract():
    assert not inspect.isabstract(gaml::StandaloneBlock)


def test_gaml::standaloneblock_constructor_exists():
    assert callable(gaml::StandaloneBlock.__init__)


def test_gaml::standaloneblock_constructor_args():
    sig = inspect.signature(gaml::StandaloneBlock.__init__)
    params = list(sig.parameters.keys())



def test_gaml::entry_is_not_abstract():
    assert not inspect.isabstract(gaml::Entry)


def test_gaml::entry_constructor_exists():
    assert callable(gaml::Entry.__init__)


def test_gaml::entry_constructor_args():
    sig = inspect.signature(gaml::Entry.__init__)
    params = list(sig.parameters.keys())


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
TerminalExpression_strategy = st.builds(
    TerminalExpression,
)
gaml::DoubleLiteral_strategy = st.builds(
    gaml::DoubleLiteral,
)
gaml::BooleanLiteral_strategy = st.builds(
    gaml::BooleanLiteral,
)
gaml::ColorLiteral_strategy = st.builds(
    gaml::ColorLiteral,
)
gaml::ReservedLiteral_strategy = st.builds(
    gaml::ReservedLiteral,
)
gaml::StringLiteral_strategy = st.builds(
    gaml::StringLiteral,
)
gaml::IntLiteral_strategy = st.builds(
    gaml::IntLiteral,
)
S::Definition_strategy = st.builds(
    S::Definition,
)
gaml::S::Var_strategy = st.builds(
    gaml::S::Var,
)
gaml::S::Action_strategy = st.builds(
    gaml::S::Action,
)
gaml::TypeInfo_strategy = st.builds(
    gaml::TypeInfo,
)
GamlDefinition_strategy = st.builds(
    GamlDefinition,
)
gaml::VarDefinition_strategy = st.builds(
    gaml::VarDefinition,
)
gaml::UnitFakeDefinition_strategy = st.builds(
    gaml::UnitFakeDefinition,
)
gaml::ActionDefinition_strategy = st.builds(
    gaml::ActionDefinition,
)
gaml::SkillFakeDefinition_strategy = st.builds(
    gaml::SkillFakeDefinition,
)
gaml::EquationDefinition_strategy = st.builds(
    gaml::EquationDefinition,
)
gaml::GamlDefinition_strategy = st.builds(
    gaml::GamlDefinition,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
gaml::Pair_strategy = st.builds(
    gaml::Pair,
)
gaml::TypeRef_strategy = st.builds(
    gaml::TypeRef,
)
gaml::Point_strategy = st.builds(
    gaml::Point,
)
gaml::ExpressionList_strategy = st.builds(
    gaml::ExpressionList,
)
gaml::ArgumentPair_strategy = st.builds(
    gaml::ArgumentPair,
)
gaml::Array_strategy = st.builds(
    gaml::Array,
)
gaml::Cast_strategy = st.builds(
    gaml::Cast,
)
gaml::Unary_strategy = st.builds(
    gaml::Unary,
)
gaml::UnitName_strategy = st.builds(
    gaml::UnitName,
)
gaml::SkillRef_strategy = st.builds(
    gaml::SkillRef,
)
gaml::If_strategy = st.builds(
    gaml::If,
)
gaml::VariableRef_strategy = st.builds(
    gaml::VariableRef,
)
gaml::Parameter_strategy = st.builds(
    gaml::Parameter,
    builtInFacetKey=
        safe_text
)
gaml::ActionRef_strategy = st.builds(
    gaml::ActionRef,
)
gaml::Unit_strategy = st.builds(
    gaml::Unit,
)
gaml::Access_strategy = st.builds(
    gaml::Access,
    named_exp=
        safe_text
)
gaml::Function_strategy = st.builds(
    gaml::Function,
)
gaml::TerminalExpression_strategy = st.builds(
    gaml::TerminalExpression,
)
gaml::EquationRef_strategy = st.builds(
    gaml::EquationRef,
)
gaml::Binary_strategy = st.builds(
    gaml::Binary,
)
gaml::Parameters_strategy = st.builds(
    gaml::Parameters,
)
gaml::EObject_strategy = st.builds(
    gaml::EObject,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
gaml::TypeFakeDefinition_strategy = st.builds(
    gaml::TypeFakeDefinition,
)
S::Declaration_strategy = st.builds(
    S::Declaration,
)
gaml::S::Loop_strategy = st.builds(
    gaml::S::Loop,
)
Statement_strategy = st.builds(
    Statement,
)
gaml::S::Return_strategy = st.builds(
    gaml::S::Return,
)
gaml::S::Other_strategy = st.builds(
    gaml::S::Other,
)
gaml::S::Species_strategy = st.builds(
    gaml::S::Species,
)
gaml::S::Do_strategy = st.builds(
    gaml::S::Do,
)
gaml::S::If_strategy = st.builds(
    gaml::S::If,
)
gaml::speciesOrGridDisplayStatement_strategy = st.builds(
    gaml::speciesOrGridDisplayStatement,
)
gaml::S::Global_strategy = st.builds(
    gaml::S::Global,
)
gaml::S::Display_strategy = st.builds(
    gaml::S::Display,
    name=
        safe_text
)
gaml::S::Solve_strategy = st.builds(
    gaml::S::Solve,
)
EquationDefinition_strategy = st.builds(
    EquationDefinition,
)
gaml::EquationFakeDefinition_strategy = st.builds(
    gaml::EquationFakeDefinition,
)
gaml::S::Equations_strategy = st.builds(
    gaml::S::Equations,
)
S::Assignment_strategy = st.builds(
    S::Assignment,
)
gaml::S::Set_strategy = st.builds(
    gaml::S::Set,
)
gaml::S::DirectAssignment_strategy = st.builds(
    gaml::S::DirectAssignment,
)
gaml::S::Assignment_strategy = st.builds(
    gaml::S::Assignment,
)
gaml::ActionArguments_strategy = st.builds(
    gaml::ActionArguments,
)
ActionDefinition_strategy = st.builds(
    ActionDefinition,
)
gaml::TypeDefinition_strategy = st.builds(
    gaml::TypeDefinition,
)
gaml::ActionFakeDefinition_strategy = st.builds(
    gaml::ActionFakeDefinition,
)
gaml::S::Definition_strategy = st.builds(
    gaml::S::Definition,
)
gaml::S::Reflex_strategy = st.builds(
    gaml::S::Reflex,
)
gaml::Statement_strategy = st.builds(
    gaml::Statement,
    firstFacet=
        safe_text,
    key=
        safe_text
)
gaml::Pragma_strategy = st.builds(
    gaml::Pragma,
    name=
        safe_text
)
VarDefinition_strategy = st.builds(
    VarDefinition,
)
gaml::ArgumentDefinition_strategy = st.builds(
    gaml::ArgumentDefinition,
)
gaml::S::Declaration_strategy = st.builds(
    gaml::S::Declaration,
)
gaml::VarFakeDefinition_strategy = st.builds(
    gaml::VarFakeDefinition,
)
gaml::S::Experiment_strategy = st.builds(
    gaml::S::Experiment,
)
gaml::Import_strategy = st.builds(
    gaml::Import,
    importURI=
        safe_text
)
gaml::Expression_strategy = st.builds(
    gaml::Expression,
    op=
        safe_text
)
gaml::Block_strategy = st.builds(
    gaml::Block,
)
gaml::Facet_strategy = st.builds(
    gaml::Facet,
    key=
        safe_text
)
gaml::HeadlessExperiment_strategy = st.builds(
    gaml::HeadlessExperiment,
    key=
        safe_text,
    importURI=
        safe_text,
    firstFacet=
        safe_text,
    name=
        safe_text
)
Entry_strategy = st.builds(
    Entry,
)
gaml::StringEvaluator_strategy = st.builds(
    gaml::StringEvaluator,
    toto=
        safe_text
)
gaml::Model_strategy = st.builds(
    gaml::Model,
)
gaml::ExperimentFileStructure_strategy = st.builds(
    gaml::ExperimentFileStructure,
)
gaml::StandaloneBlock_strategy = st.builds(
    gaml::StandaloneBlock,
)
gaml::Entry_strategy = st.builds(
    gaml::Entry,
)

@given(instance=TerminalExpression_strategy)
@settings(max_examples=50)
def test_terminalexpression_instantiation(instance):
    assert isinstance(instance, TerminalExpression)

@given(instance=gaml::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_gaml::doubleliteral_instantiation(instance):
    assert isinstance(instance, gaml::DoubleLiteral)

@given(instance=gaml::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_gaml::booleanliteral_instantiation(instance):
    assert isinstance(instance, gaml::BooleanLiteral)

@given(instance=gaml::ColorLiteral_strategy)
@settings(max_examples=50)
def test_gaml::colorliteral_instantiation(instance):
    assert isinstance(instance, gaml::ColorLiteral)

@given(instance=gaml::ReservedLiteral_strategy)
@settings(max_examples=50)
def test_gaml::reservedliteral_instantiation(instance):
    assert isinstance(instance, gaml::ReservedLiteral)

@given(instance=gaml::StringLiteral_strategy)
@settings(max_examples=50)
def test_gaml::stringliteral_instantiation(instance):
    assert isinstance(instance, gaml::StringLiteral)

@given(instance=gaml::IntLiteral_strategy)
@settings(max_examples=50)
def test_gaml::intliteral_instantiation(instance):
    assert isinstance(instance, gaml::IntLiteral)

@given(instance=S::Definition_strategy)
@settings(max_examples=50)
def test_s::definition_instantiation(instance):
    assert isinstance(instance, S::Definition)

@given(instance=gaml::S::Var_strategy)
@settings(max_examples=50)
def test_gaml::s::var_instantiation(instance):
    assert isinstance(instance, gaml::S::Var)

@given(instance=gaml::S::Action_strategy)
@settings(max_examples=50)
def test_gaml::s::action_instantiation(instance):
    assert isinstance(instance, gaml::S::Action)

@given(instance=gaml::TypeInfo_strategy)
@settings(max_examples=50)
def test_gaml::typeinfo_instantiation(instance):
    assert isinstance(instance, gaml::TypeInfo)

@given(instance=GamlDefinition_strategy)
@settings(max_examples=50)
def test_gamldefinition_instantiation(instance):
    assert isinstance(instance, GamlDefinition)

@given(instance=gaml::VarDefinition_strategy)
@settings(max_examples=50)
def test_gaml::vardefinition_instantiation(instance):
    assert isinstance(instance, gaml::VarDefinition)

@given(instance=gaml::UnitFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::unitfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::UnitFakeDefinition)

@given(instance=gaml::ActionDefinition_strategy)
@settings(max_examples=50)
def test_gaml::actiondefinition_instantiation(instance):
    assert isinstance(instance, gaml::ActionDefinition)

@given(instance=gaml::SkillFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::skillfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::SkillFakeDefinition)

@given(instance=gaml::EquationDefinition_strategy)
@settings(max_examples=50)
def test_gaml::equationdefinition_instantiation(instance):
    assert isinstance(instance, gaml::EquationDefinition)

@given(instance=gaml::GamlDefinition_strategy)
@settings(max_examples=50)
def test_gaml::gamldefinition_instantiation(instance):
    assert isinstance(instance, gaml::GamlDefinition)

@given(instance=gaml::GamlDefinition_strategy)
def test_gaml::gamldefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gaml::GamlDefinition_strategy)
def test_gaml::gamldefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gaml::Pair_strategy)
@settings(max_examples=50)
def test_gaml::pair_instantiation(instance):
    assert isinstance(instance, gaml::Pair)

@given(instance=gaml::TypeRef_strategy)
@settings(max_examples=50)
def test_gaml::typeref_instantiation(instance):
    assert isinstance(instance, gaml::TypeRef)

@given(instance=gaml::Point_strategy)
@settings(max_examples=50)
def test_gaml::point_instantiation(instance):
    assert isinstance(instance, gaml::Point)

@given(instance=gaml::ExpressionList_strategy)
@settings(max_examples=50)
def test_gaml::expressionlist_instantiation(instance):
    assert isinstance(instance, gaml::ExpressionList)

@given(instance=gaml::ArgumentPair_strategy)
@settings(max_examples=50)
def test_gaml::argumentpair_instantiation(instance):
    assert isinstance(instance, gaml::ArgumentPair)

@given(instance=gaml::Array_strategy)
@settings(max_examples=50)
def test_gaml::array_instantiation(instance):
    assert isinstance(instance, gaml::Array)

@given(instance=gaml::Cast_strategy)
@settings(max_examples=50)
def test_gaml::cast_instantiation(instance):
    assert isinstance(instance, gaml::Cast)

@given(instance=gaml::Unary_strategy)
@settings(max_examples=50)
def test_gaml::unary_instantiation(instance):
    assert isinstance(instance, gaml::Unary)

@given(instance=gaml::UnitName_strategy)
@settings(max_examples=50)
def test_gaml::unitname_instantiation(instance):
    assert isinstance(instance, gaml::UnitName)

@given(instance=gaml::SkillRef_strategy)
@settings(max_examples=50)
def test_gaml::skillref_instantiation(instance):
    assert isinstance(instance, gaml::SkillRef)

@given(instance=gaml::If_strategy)
@settings(max_examples=50)
def test_gaml::if_instantiation(instance):
    assert isinstance(instance, gaml::If)

@given(instance=gaml::VariableRef_strategy)
@settings(max_examples=50)
def test_gaml::variableref_instantiation(instance):
    assert isinstance(instance, gaml::VariableRef)

@given(instance=gaml::Parameter_strategy)
@settings(max_examples=50)
def test_gaml::parameter_instantiation(instance):
    assert isinstance(instance, gaml::Parameter)

@given(instance=gaml::Parameter_strategy)
def test_gaml::parameter_builtInFacetKey_type(instance):
    assert isinstance(instance.builtInFacetKey, str)


@given(instance=gaml::Parameter_strategy)
def test_gaml::parameter_builtInFacetKey_setter(instance):
    original = instance.builtInFacetKey
    instance.builtInFacetKey = original
    assert instance.builtInFacetKey == original

@given(instance=gaml::ActionRef_strategy)
@settings(max_examples=50)
def test_gaml::actionref_instantiation(instance):
    assert isinstance(instance, gaml::ActionRef)

@given(instance=gaml::Unit_strategy)
@settings(max_examples=50)
def test_gaml::unit_instantiation(instance):
    assert isinstance(instance, gaml::Unit)

@given(instance=gaml::Access_strategy)
@settings(max_examples=50)
def test_gaml::access_instantiation(instance):
    assert isinstance(instance, gaml::Access)

@given(instance=gaml::Access_strategy)
def test_gaml::access_named_exp_type(instance):
    assert isinstance(instance.named_exp, str)


@given(instance=gaml::Access_strategy)
def test_gaml::access_named_exp_setter(instance):
    original = instance.named_exp
    instance.named_exp = original
    assert instance.named_exp == original

@given(instance=gaml::Function_strategy)
@settings(max_examples=50)
def test_gaml::function_instantiation(instance):
    assert isinstance(instance, gaml::Function)

@given(instance=gaml::TerminalExpression_strategy)
@settings(max_examples=50)
def test_gaml::terminalexpression_instantiation(instance):
    assert isinstance(instance, gaml::TerminalExpression)

@given(instance=gaml::EquationRef_strategy)
@settings(max_examples=50)
def test_gaml::equationref_instantiation(instance):
    assert isinstance(instance, gaml::EquationRef)

@given(instance=gaml::Binary_strategy)
@settings(max_examples=50)
def test_gaml::binary_instantiation(instance):
    assert isinstance(instance, gaml::Binary)

@given(instance=gaml::Parameters_strategy)
@settings(max_examples=50)
def test_gaml::parameters_instantiation(instance):
    assert isinstance(instance, gaml::Parameters)

@given(instance=gaml::EObject_strategy)
@settings(max_examples=50)
def test_gaml::eobject_instantiation(instance):
    assert isinstance(instance, gaml::EObject)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=gaml::TypeFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::typefakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::TypeFakeDefinition)

@given(instance=S::Declaration_strategy)
@settings(max_examples=50)
def test_s::declaration_instantiation(instance):
    assert isinstance(instance, S::Declaration)

@given(instance=gaml::S::Loop_strategy)
@settings(max_examples=50)
def test_gaml::s::loop_instantiation(instance):
    assert isinstance(instance, gaml::S::Loop)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gaml::S::Return_strategy)
@settings(max_examples=50)
def test_gaml::s::return_instantiation(instance):
    assert isinstance(instance, gaml::S::Return)

@given(instance=gaml::S::Other_strategy)
@settings(max_examples=50)
def test_gaml::s::other_instantiation(instance):
    assert isinstance(instance, gaml::S::Other)

@given(instance=gaml::S::Species_strategy)
@settings(max_examples=50)
def test_gaml::s::species_instantiation(instance):
    assert isinstance(instance, gaml::S::Species)

@given(instance=gaml::S::Do_strategy)
@settings(max_examples=50)
def test_gaml::s::do_instantiation(instance):
    assert isinstance(instance, gaml::S::Do)

@given(instance=gaml::S::If_strategy)
@settings(max_examples=50)
def test_gaml::s::if_instantiation(instance):
    assert isinstance(instance, gaml::S::If)

@given(instance=gaml::speciesOrGridDisplayStatement_strategy)
@settings(max_examples=50)
def test_gaml::speciesorgriddisplaystatement_instantiation(instance):
    assert isinstance(instance, gaml::speciesOrGridDisplayStatement)

@given(instance=gaml::S::Global_strategy)
@settings(max_examples=50)
def test_gaml::s::global_instantiation(instance):
    assert isinstance(instance, gaml::S::Global)

@given(instance=gaml::S::Display_strategy)
@settings(max_examples=50)
def test_gaml::s::display_instantiation(instance):
    assert isinstance(instance, gaml::S::Display)

@given(instance=gaml::S::Display_strategy)
def test_gaml::s::display_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gaml::S::Display_strategy)
def test_gaml::s::display_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gaml::S::Solve_strategy)
@settings(max_examples=50)
def test_gaml::s::solve_instantiation(instance):
    assert isinstance(instance, gaml::S::Solve)

@given(instance=EquationDefinition_strategy)
@settings(max_examples=50)
def test_equationdefinition_instantiation(instance):
    assert isinstance(instance, EquationDefinition)

@given(instance=gaml::EquationFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::equationfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::EquationFakeDefinition)

@given(instance=gaml::S::Equations_strategy)
@settings(max_examples=50)
def test_gaml::s::equations_instantiation(instance):
    assert isinstance(instance, gaml::S::Equations)

@given(instance=S::Assignment_strategy)
@settings(max_examples=50)
def test_s::assignment_instantiation(instance):
    assert isinstance(instance, S::Assignment)

@given(instance=gaml::S::Set_strategy)
@settings(max_examples=50)
def test_gaml::s::set_instantiation(instance):
    assert isinstance(instance, gaml::S::Set)

@given(instance=gaml::S::DirectAssignment_strategy)
@settings(max_examples=50)
def test_gaml::s::directassignment_instantiation(instance):
    assert isinstance(instance, gaml::S::DirectAssignment)

@given(instance=gaml::S::Assignment_strategy)
@settings(max_examples=50)
def test_gaml::s::assignment_instantiation(instance):
    assert isinstance(instance, gaml::S::Assignment)

@given(instance=gaml::ActionArguments_strategy)
@settings(max_examples=50)
def test_gaml::actionarguments_instantiation(instance):
    assert isinstance(instance, gaml::ActionArguments)

@given(instance=ActionDefinition_strategy)
@settings(max_examples=50)
def test_actiondefinition_instantiation(instance):
    assert isinstance(instance, ActionDefinition)

@given(instance=gaml::TypeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::typedefinition_instantiation(instance):
    assert isinstance(instance, gaml::TypeDefinition)

@given(instance=gaml::ActionFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::actionfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::ActionFakeDefinition)

@given(instance=gaml::S::Definition_strategy)
@settings(max_examples=50)
def test_gaml::s::definition_instantiation(instance):
    assert isinstance(instance, gaml::S::Definition)

@given(instance=gaml::S::Reflex_strategy)
@settings(max_examples=50)
def test_gaml::s::reflex_instantiation(instance):
    assert isinstance(instance, gaml::S::Reflex)

@given(instance=gaml::Statement_strategy)
@settings(max_examples=50)
def test_gaml::statement_instantiation(instance):
    assert isinstance(instance, gaml::Statement)

@given(instance=gaml::Statement_strategy)
def test_gaml::statement_firstFacet_type(instance):
    assert isinstance(instance.firstFacet, str)


@given(instance=gaml::Statement_strategy)
def test_gaml::statement_firstFacet_setter(instance):
    original = instance.firstFacet
    instance.firstFacet = original
    assert instance.firstFacet == original

@given(instance=gaml::Statement_strategy)
def test_gaml::statement_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=gaml::Statement_strategy)
def test_gaml::statement_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gaml::Pragma_strategy)
@settings(max_examples=50)
def test_gaml::pragma_instantiation(instance):
    assert isinstance(instance, gaml::Pragma)

@given(instance=gaml::Pragma_strategy)
def test_gaml::pragma_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gaml::Pragma_strategy)
def test_gaml::pragma_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VarDefinition_strategy)
@settings(max_examples=50)
def test_vardefinition_instantiation(instance):
    assert isinstance(instance, VarDefinition)

@given(instance=gaml::ArgumentDefinition_strategy)
@settings(max_examples=50)
def test_gaml::argumentdefinition_instantiation(instance):
    assert isinstance(instance, gaml::ArgumentDefinition)

@given(instance=gaml::S::Declaration_strategy)
@settings(max_examples=50)
def test_gaml::s::declaration_instantiation(instance):
    assert isinstance(instance, gaml::S::Declaration)

@given(instance=gaml::VarFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml::varfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml::VarFakeDefinition)

@given(instance=gaml::S::Experiment_strategy)
@settings(max_examples=50)
def test_gaml::s::experiment_instantiation(instance):
    assert isinstance(instance, gaml::S::Experiment)

@given(instance=gaml::Import_strategy)
@settings(max_examples=50)
def test_gaml::import_instantiation(instance):
    assert isinstance(instance, gaml::Import)

@given(instance=gaml::Import_strategy)
def test_gaml::import_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=gaml::Import_strategy)
def test_gaml::import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=gaml::Expression_strategy)
@settings(max_examples=50)
def test_gaml::expression_instantiation(instance):
    assert isinstance(instance, gaml::Expression)

@given(instance=gaml::Expression_strategy)
def test_gaml::expression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=gaml::Expression_strategy)
def test_gaml::expression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml::Block_strategy)
@settings(max_examples=50)
def test_gaml::block_instantiation(instance):
    assert isinstance(instance, gaml::Block)

@given(instance=gaml::Facet_strategy)
@settings(max_examples=50)
def test_gaml::facet_instantiation(instance):
    assert isinstance(instance, gaml::Facet)

@given(instance=gaml::Facet_strategy)
def test_gaml::facet_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=gaml::Facet_strategy)
def test_gaml::facet_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gaml::HeadlessExperiment_strategy)
@settings(max_examples=50)
def test_gaml::headlessexperiment_instantiation(instance):
    assert isinstance(instance, gaml::HeadlessExperiment)

@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_importURI_type(instance):
    assert isinstance(instance.importURI, str)


@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_firstFacet_type(instance):
    assert isinstance(instance.firstFacet, str)


@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_firstFacet_setter(instance):
    original = instance.firstFacet
    instance.firstFacet = original
    assert instance.firstFacet == original

@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gaml::HeadlessExperiment_strategy)
def test_gaml::headlessexperiment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=gaml::StringEvaluator_strategy)
@settings(max_examples=50)
def test_gaml::stringevaluator_instantiation(instance):
    assert isinstance(instance, gaml::StringEvaluator)

@given(instance=gaml::StringEvaluator_strategy)
def test_gaml::stringevaluator_toto_type(instance):
    assert isinstance(instance.toto, str)


@given(instance=gaml::StringEvaluator_strategy)
def test_gaml::stringevaluator_toto_setter(instance):
    original = instance.toto
    instance.toto = original
    assert instance.toto == original

@given(instance=gaml::Model_strategy)
@settings(max_examples=50)
def test_gaml::model_instantiation(instance):
    assert isinstance(instance, gaml::Model)

@given(instance=gaml::ExperimentFileStructure_strategy)
@settings(max_examples=50)
def test_gaml::experimentfilestructure_instantiation(instance):
    assert isinstance(instance, gaml::ExperimentFileStructure)

@given(instance=gaml::StandaloneBlock_strategy)
@settings(max_examples=50)
def test_gaml::standaloneblock_instantiation(instance):
    assert isinstance(instance, gaml::StandaloneBlock)

@given(instance=gaml::Entry_strategy)
@settings(max_examples=50)
def test_gaml::entry_instantiation(instance):
    assert isinstance(instance, gaml::Entry)
