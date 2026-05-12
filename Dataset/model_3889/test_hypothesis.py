import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    S_Definition,
    gaml_S_Var,
    gaml_S_Action,
    TerminalExpression,
    gaml_StringLiteral,
    gaml_TypeInfo,
    Expression,
    gaml_Access,
    gaml_BinaryOperator,
    gaml_Array,
    gaml_VariableRef,
    gaml_ExpressionList,
    gaml_If,
    gaml_TerminalExpression,
    gaml_ArgumentPair,
    GamlDefinition,
    gaml_SkillFakeDefinition,
    gaml_VarDefinition,
    gaml_ActionDefinition,
    gaml_UnitFakeDefinition,
    gaml_EquationDefinition,
    gaml_GamlDefinition,
    gaml_ActionArguments,
    ActionDefinition,
    gaml_TypeDefinition,
    gaml_ActionFakeDefinition,
    gaml_EObject,
    TypeDefinition,
    gaml_TypeFakeDefinition,
    S_Declaration,
    gaml_S_Reflex,
    gaml_S_Definition,
    gaml_S_Loop,
    Statement,
    gaml_S_Species,
    gaml_S_Try,
    gaml_speciesOrGridDisplayStatement,
    gaml_S_Display,
    gaml_S_Return,
    gaml_S_Other,
    gaml_S_Do,
    gaml_S_If,
    gaml_S_Solve,
    gaml_S_Global,
    EquationDefinition,
    gaml_EquationFakeDefinition,
    gaml_S_Equations,
    S_Assignment,
    gaml_S_Set,
    gaml_S_DirectAssignment,
    gaml_S_Assignment,
    gaml_HeadlessExperiment,
    gaml_Statement,
    gaml_Pragma,
    VarDefinition,
    gaml_S_Declaration,
    gaml_S_Experiment,
    gaml_ArgumentDefinition,
    gaml_VarFakeDefinition,
    gaml_Import,
    gaml_Expression,
    gaml_Block,
    Entry,
    gaml_StringEvaluator,
    gaml_ExperimentFileStructure,
    gaml_Model,
    gaml_StandaloneBlock,
    gaml_Entry,
    gaml_Facet,
    gaml_ReservedLiteral,
    gaml_BooleanLiteral,
    gaml_DoubleLiteral,
    gaml_IntLiteral,
    gaml_TypeRef,
    gaml_UnitName,
    gaml_Parameter,
    gaml_Function,
    gaml_Point,
    gaml_EquationRef,
    gaml_ActionRef,
    gaml_SkillRef,
    gaml_Unary,
    gaml_Unit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_s_definition_is_not_abstract():
    assert not inspect.isabstract(S_Definition)


def test_s_definition_constructor_exists():
    assert callable(S_Definition.__init__)


def test_s_definition_constructor_args():
    sig = inspect.signature(S_Definition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_var_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Var)


def test_gaml_s_var_constructor_exists():
    assert callable(gaml_S_Var.__init__)


def test_gaml_s_var_constructor_args():
    sig = inspect.signature(gaml_S_Var.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_action_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Action)


def test_gaml_s_action_constructor_exists():
    assert callable(gaml_S_Action.__init__)


def test_gaml_s_action_constructor_args():
    sig = inspect.signature(gaml_S_Action.__init__)
    params = list(sig.parameters.keys())



def test_terminalexpression_is_not_abstract():
    assert not inspect.isabstract(TerminalExpression)


def test_terminalexpression_constructor_exists():
    assert callable(TerminalExpression.__init__)


def test_terminalexpression_constructor_args():
    sig = inspect.signature(TerminalExpression.__init__)
    params = list(sig.parameters.keys())



def test_gaml_stringliteral_is_not_abstract():
    assert not inspect.isabstract(gaml_StringLiteral)


def test_gaml_stringliteral_constructor_exists():
    assert callable(gaml_StringLiteral.__init__)


def test_gaml_stringliteral_constructor_args():
    sig = inspect.signature(gaml_StringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml_typeinfo_is_not_abstract():
    assert not inspect.isabstract(gaml_TypeInfo)


def test_gaml_typeinfo_constructor_exists():
    assert callable(gaml_TypeInfo.__init__)


def test_gaml_typeinfo_constructor_args():
    sig = inspect.signature(gaml_TypeInfo.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_gaml_access_is_not_abstract():
    assert not inspect.isabstract(gaml_Access)


def test_gaml_access_constructor_exists():
    assert callable(gaml_Access.__init__)


def test_gaml_access_constructor_args():
    sig = inspect.signature(gaml_Access.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_access_has_op():
    assert hasattr(gaml_Access, "op")
    descriptor = None
    for klass in gaml_Access.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(gaml_BinaryOperator)


def test_gaml_binaryoperator_constructor_exists():
    assert callable(gaml_BinaryOperator.__init__)


def test_gaml_binaryoperator_constructor_args():
    sig = inspect.signature(gaml_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_binaryoperator_has_op():
    assert hasattr(gaml_BinaryOperator, "op")
    descriptor = None
    for klass in gaml_BinaryOperator.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_array_is_not_abstract():
    assert not inspect.isabstract(gaml_Array)


def test_gaml_array_constructor_exists():
    assert callable(gaml_Array.__init__)


def test_gaml_array_constructor_args():
    sig = inspect.signature(gaml_Array.__init__)
    params = list(sig.parameters.keys())



def test_gaml_variableref_is_not_abstract():
    assert not inspect.isabstract(gaml_VariableRef)


def test_gaml_variableref_constructor_exists():
    assert callable(gaml_VariableRef.__init__)


def test_gaml_variableref_constructor_args():
    sig = inspect.signature(gaml_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml_expressionlist_is_not_abstract():
    assert not inspect.isabstract(gaml_ExpressionList)


def test_gaml_expressionlist_constructor_exists():
    assert callable(gaml_ExpressionList.__init__)


def test_gaml_expressionlist_constructor_args():
    sig = inspect.signature(gaml_ExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_gaml_if_is_not_abstract():
    assert not inspect.isabstract(gaml_If)


def test_gaml_if_constructor_exists():
    assert callable(gaml_If.__init__)


def test_gaml_if_constructor_args():
    sig = inspect.signature(gaml_If.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_if_has_op():
    assert hasattr(gaml_If, "op")
    descriptor = None
    for klass in gaml_If.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_terminalexpression_is_not_abstract():
    assert not inspect.isabstract(gaml_TerminalExpression)


def test_gaml_terminalexpression_constructor_exists():
    assert callable(gaml_TerminalExpression.__init__)


def test_gaml_terminalexpression_constructor_args():
    sig = inspect.signature(gaml_TerminalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_terminalexpression_has_op():
    assert hasattr(gaml_TerminalExpression, "op")
    descriptor = None
    for klass in gaml_TerminalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_argumentpair_is_not_abstract():
    assert not inspect.isabstract(gaml_ArgumentPair)


def test_gaml_argumentpair_constructor_exists():
    assert callable(gaml_ArgumentPair.__init__)


def test_gaml_argumentpair_constructor_args():
    sig = inspect.signature(gaml_ArgumentPair.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_argumentpair_has_op():
    assert hasattr(gaml_ArgumentPair, "op")
    descriptor = None
    for klass in gaml_ArgumentPair.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gamldefinition_is_not_abstract():
    assert not inspect.isabstract(GamlDefinition)


def test_gamldefinition_constructor_exists():
    assert callable(GamlDefinition.__init__)


def test_gamldefinition_constructor_args():
    sig = inspect.signature(GamlDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_skillfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_SkillFakeDefinition)


def test_gaml_skillfakedefinition_constructor_exists():
    assert callable(gaml_SkillFakeDefinition.__init__)


def test_gaml_skillfakedefinition_constructor_args():
    sig = inspect.signature(gaml_SkillFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_vardefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_VarDefinition)


def test_gaml_vardefinition_constructor_exists():
    assert callable(gaml_VarDefinition.__init__)


def test_gaml_vardefinition_constructor_args():
    sig = inspect.signature(gaml_VarDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_actiondefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_ActionDefinition)


def test_gaml_actiondefinition_constructor_exists():
    assert callable(gaml_ActionDefinition.__init__)


def test_gaml_actiondefinition_constructor_args():
    sig = inspect.signature(gaml_ActionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_unitfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_UnitFakeDefinition)


def test_gaml_unitfakedefinition_constructor_exists():
    assert callable(gaml_UnitFakeDefinition.__init__)


def test_gaml_unitfakedefinition_constructor_args():
    sig = inspect.signature(gaml_UnitFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_equationdefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_EquationDefinition)


def test_gaml_equationdefinition_constructor_exists():
    assert callable(gaml_EquationDefinition.__init__)


def test_gaml_equationdefinition_constructor_args():
    sig = inspect.signature(gaml_EquationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_gamldefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_GamlDefinition)


def test_gaml_gamldefinition_constructor_exists():
    assert callable(gaml_GamlDefinition.__init__)


def test_gaml_gamldefinition_constructor_args():
    sig = inspect.signature(gaml_GamlDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml_gamldefinition_has_name():
    assert hasattr(gaml_GamlDefinition, "name")
    descriptor = None
    for klass in gaml_GamlDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gaml_actionarguments_is_not_abstract():
    assert not inspect.isabstract(gaml_ActionArguments)


def test_gaml_actionarguments_constructor_exists():
    assert callable(gaml_ActionArguments.__init__)


def test_gaml_actionarguments_constructor_args():
    sig = inspect.signature(gaml_ActionArguments.__init__)
    params = list(sig.parameters.keys())



def test_actiondefinition_is_not_abstract():
    assert not inspect.isabstract(ActionDefinition)


def test_actiondefinition_constructor_exists():
    assert callable(ActionDefinition.__init__)


def test_actiondefinition_constructor_args():
    sig = inspect.signature(ActionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_typedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_TypeDefinition)


def test_gaml_typedefinition_constructor_exists():
    assert callable(gaml_TypeDefinition.__init__)


def test_gaml_typedefinition_constructor_args():
    sig = inspect.signature(gaml_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_actionfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_ActionFakeDefinition)


def test_gaml_actionfakedefinition_constructor_exists():
    assert callable(gaml_ActionFakeDefinition.__init__)


def test_gaml_actionfakedefinition_constructor_args():
    sig = inspect.signature(gaml_ActionFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_eobject_is_not_abstract():
    assert not inspect.isabstract(gaml_EObject)


def test_gaml_eobject_constructor_exists():
    assert callable(gaml_EObject.__init__)


def test_gaml_eobject_constructor_args():
    sig = inspect.signature(gaml_EObject.__init__)
    params = list(sig.parameters.keys())



def test_typedefinition_is_not_abstract():
    assert not inspect.isabstract(TypeDefinition)


def test_typedefinition_constructor_exists():
    assert callable(TypeDefinition.__init__)


def test_typedefinition_constructor_args():
    sig = inspect.signature(TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_typefakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_TypeFakeDefinition)


def test_gaml_typefakedefinition_constructor_exists():
    assert callable(gaml_TypeFakeDefinition.__init__)


def test_gaml_typefakedefinition_constructor_args():
    sig = inspect.signature(gaml_TypeFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_s_declaration_is_not_abstract():
    assert not inspect.isabstract(S_Declaration)


def test_s_declaration_constructor_exists():
    assert callable(S_Declaration.__init__)


def test_s_declaration_constructor_args():
    sig = inspect.signature(S_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_reflex_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Reflex)


def test_gaml_s_reflex_constructor_exists():
    assert callable(gaml_S_Reflex.__init__)


def test_gaml_s_reflex_constructor_args():
    sig = inspect.signature(gaml_S_Reflex.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_definition_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Definition)


def test_gaml_s_definition_constructor_exists():
    assert callable(gaml_S_Definition.__init__)


def test_gaml_s_definition_constructor_args():
    sig = inspect.signature(gaml_S_Definition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_loop_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Loop)


def test_gaml_s_loop_constructor_exists():
    assert callable(gaml_S_Loop.__init__)


def test_gaml_s_loop_constructor_args():
    sig = inspect.signature(gaml_S_Loop.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_species_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Species)


def test_gaml_s_species_constructor_exists():
    assert callable(gaml_S_Species.__init__)


def test_gaml_s_species_constructor_args():
    sig = inspect.signature(gaml_S_Species.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_try_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Try)


def test_gaml_s_try_constructor_exists():
    assert callable(gaml_S_Try.__init__)


def test_gaml_s_try_constructor_args():
    sig = inspect.signature(gaml_S_Try.__init__)
    params = list(sig.parameters.keys())



def test_gaml_speciesorgriddisplaystatement_is_not_abstract():
    assert not inspect.isabstract(gaml_speciesOrGridDisplayStatement)


def test_gaml_speciesorgriddisplaystatement_constructor_exists():
    assert callable(gaml_speciesOrGridDisplayStatement.__init__)


def test_gaml_speciesorgriddisplaystatement_constructor_args():
    sig = inspect.signature(gaml_speciesOrGridDisplayStatement.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_display_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Display)


def test_gaml_s_display_constructor_exists():
    assert callable(gaml_S_Display.__init__)


def test_gaml_s_display_constructor_args():
    sig = inspect.signature(gaml_S_Display.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml_s_display_has_name():
    assert hasattr(gaml_S_Display, "name")
    descriptor = None
    for klass in gaml_S_Display.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gaml_s_return_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Return)


def test_gaml_s_return_constructor_exists():
    assert callable(gaml_S_Return.__init__)


def test_gaml_s_return_constructor_args():
    sig = inspect.signature(gaml_S_Return.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_other_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Other)


def test_gaml_s_other_constructor_exists():
    assert callable(gaml_S_Other.__init__)


def test_gaml_s_other_constructor_args():
    sig = inspect.signature(gaml_S_Other.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_do_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Do)


def test_gaml_s_do_constructor_exists():
    assert callable(gaml_S_Do.__init__)


def test_gaml_s_do_constructor_args():
    sig = inspect.signature(gaml_S_Do.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_if_is_not_abstract():
    assert not inspect.isabstract(gaml_S_If)


def test_gaml_s_if_constructor_exists():
    assert callable(gaml_S_If.__init__)


def test_gaml_s_if_constructor_args():
    sig = inspect.signature(gaml_S_If.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_solve_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Solve)


def test_gaml_s_solve_constructor_exists():
    assert callable(gaml_S_Solve.__init__)


def test_gaml_s_solve_constructor_args():
    sig = inspect.signature(gaml_S_Solve.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_global_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Global)


def test_gaml_s_global_constructor_exists():
    assert callable(gaml_S_Global.__init__)


def test_gaml_s_global_constructor_args():
    sig = inspect.signature(gaml_S_Global.__init__)
    params = list(sig.parameters.keys())



def test_equationdefinition_is_not_abstract():
    assert not inspect.isabstract(EquationDefinition)


def test_equationdefinition_constructor_exists():
    assert callable(EquationDefinition.__init__)


def test_equationdefinition_constructor_args():
    sig = inspect.signature(EquationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_equationfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_EquationFakeDefinition)


def test_gaml_equationfakedefinition_constructor_exists():
    assert callable(gaml_EquationFakeDefinition.__init__)


def test_gaml_equationfakedefinition_constructor_args():
    sig = inspect.signature(gaml_EquationFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_equations_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Equations)


def test_gaml_s_equations_constructor_exists():
    assert callable(gaml_S_Equations.__init__)


def test_gaml_s_equations_constructor_args():
    sig = inspect.signature(gaml_S_Equations.__init__)
    params = list(sig.parameters.keys())



def test_s_assignment_is_not_abstract():
    assert not inspect.isabstract(S_Assignment)


def test_s_assignment_constructor_exists():
    assert callable(S_Assignment.__init__)


def test_s_assignment_constructor_args():
    sig = inspect.signature(S_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_set_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Set)


def test_gaml_s_set_constructor_exists():
    assert callable(gaml_S_Set.__init__)


def test_gaml_s_set_constructor_args():
    sig = inspect.signature(gaml_S_Set.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_directassignment_is_not_abstract():
    assert not inspect.isabstract(gaml_S_DirectAssignment)


def test_gaml_s_directassignment_constructor_exists():
    assert callable(gaml_S_DirectAssignment.__init__)


def test_gaml_s_directassignment_constructor_args():
    sig = inspect.signature(gaml_S_DirectAssignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_assignment_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Assignment)


def test_gaml_s_assignment_constructor_exists():
    assert callable(gaml_S_Assignment.__init__)


def test_gaml_s_assignment_constructor_args():
    sig = inspect.signature(gaml_S_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_gaml_headlessexperiment_is_not_abstract():
    assert not inspect.isabstract(gaml_HeadlessExperiment)


def test_gaml_headlessexperiment_constructor_exists():
    assert callable(gaml_HeadlessExperiment.__init__)


def test_gaml_headlessexperiment_constructor_args():
    sig = inspect.signature(gaml_HeadlessExperiment.__init__)
    params = list(sig.parameters.keys())
    assert "firstFacet" in params, "Missing parameter 'firstFacet'"
    assert "name" in params, "Missing parameter 'name'"
    assert "key" in params, "Missing parameter 'key'"
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_gaml_headlessexperiment_has_firstFacet():
    assert hasattr(gaml_HeadlessExperiment, "firstFacet")
    descriptor = None
    for klass in gaml_HeadlessExperiment.__mro__:
        if "firstFacet" in klass.__dict__:
            descriptor = klass.__dict__["firstFacet"]
            break
    assert isinstance(descriptor, property)

def test_gaml_headlessexperiment_has_name():
    assert hasattr(gaml_HeadlessExperiment, "name")
    descriptor = None
    for klass in gaml_HeadlessExperiment.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gaml_headlessexperiment_has_key():
    assert hasattr(gaml_HeadlessExperiment, "key")
    descriptor = None
    for klass in gaml_HeadlessExperiment.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_gaml_headlessexperiment_has_importURI():
    assert hasattr(gaml_HeadlessExperiment, "importURI")
    descriptor = None
    for klass in gaml_HeadlessExperiment.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_gaml_statement_is_not_abstract():
    assert not inspect.isabstract(gaml_Statement)


def test_gaml_statement_constructor_exists():
    assert callable(gaml_Statement.__init__)


def test_gaml_statement_constructor_args():
    sig = inspect.signature(gaml_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "firstFacet" in params, "Missing parameter 'firstFacet'"
    assert "key" in params, "Missing parameter 'key'"

def test_gaml_statement_has_firstFacet():
    assert hasattr(gaml_Statement, "firstFacet")
    descriptor = None
    for klass in gaml_Statement.__mro__:
        if "firstFacet" in klass.__dict__:
            descriptor = klass.__dict__["firstFacet"]
            break
    assert isinstance(descriptor, property)

def test_gaml_statement_has_key():
    assert hasattr(gaml_Statement, "key")
    descriptor = None
    for klass in gaml_Statement.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_gaml_pragma_is_not_abstract():
    assert not inspect.isabstract(gaml_Pragma)


def test_gaml_pragma_constructor_exists():
    assert callable(gaml_Pragma.__init__)


def test_gaml_pragma_constructor_args():
    sig = inspect.signature(gaml_Pragma.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gaml_pragma_has_name():
    assert hasattr(gaml_Pragma, "name")
    descriptor = None
    for klass in gaml_Pragma.__mro__:
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



def test_gaml_s_declaration_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Declaration)


def test_gaml_s_declaration_constructor_exists():
    assert callable(gaml_S_Declaration.__init__)


def test_gaml_s_declaration_constructor_args():
    sig = inspect.signature(gaml_S_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_gaml_s_experiment_is_not_abstract():
    assert not inspect.isabstract(gaml_S_Experiment)


def test_gaml_s_experiment_constructor_exists():
    assert callable(gaml_S_Experiment.__init__)


def test_gaml_s_experiment_constructor_args():
    sig = inspect.signature(gaml_S_Experiment.__init__)
    params = list(sig.parameters.keys())



def test_gaml_argumentdefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_ArgumentDefinition)


def test_gaml_argumentdefinition_constructor_exists():
    assert callable(gaml_ArgumentDefinition.__init__)


def test_gaml_argumentdefinition_constructor_args():
    sig = inspect.signature(gaml_ArgumentDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_varfakedefinition_is_not_abstract():
    assert not inspect.isabstract(gaml_VarFakeDefinition)


def test_gaml_varfakedefinition_constructor_exists():
    assert callable(gaml_VarFakeDefinition.__init__)


def test_gaml_varfakedefinition_constructor_args():
    sig = inspect.signature(gaml_VarFakeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_gaml_import_is_not_abstract():
    assert not inspect.isabstract(gaml_Import)


def test_gaml_import_constructor_exists():
    assert callable(gaml_Import.__init__)


def test_gaml_import_constructor_args():
    sig = inspect.signature(gaml_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"

def test_gaml_import_has_importURI():
    assert hasattr(gaml_Import, "importURI")
    descriptor = None
    for klass in gaml_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)



def test_gaml_expression_is_not_abstract():
    assert not inspect.isabstract(gaml_Expression)


def test_gaml_expression_constructor_exists():
    assert callable(gaml_Expression.__init__)


def test_gaml_expression_constructor_args():
    sig = inspect.signature(gaml_Expression.__init__)
    params = list(sig.parameters.keys())



def test_gaml_block_is_not_abstract():
    assert not inspect.isabstract(gaml_Block)


def test_gaml_block_constructor_exists():
    assert callable(gaml_Block.__init__)


def test_gaml_block_constructor_args():
    sig = inspect.signature(gaml_Block.__init__)
    params = list(sig.parameters.keys())



def test_entry_is_not_abstract():
    assert not inspect.isabstract(Entry)


def test_entry_constructor_exists():
    assert callable(Entry.__init__)


def test_entry_constructor_args():
    sig = inspect.signature(Entry.__init__)
    params = list(sig.parameters.keys())



def test_gaml_stringevaluator_is_not_abstract():
    assert not inspect.isabstract(gaml_StringEvaluator)


def test_gaml_stringevaluator_constructor_exists():
    assert callable(gaml_StringEvaluator.__init__)


def test_gaml_stringevaluator_constructor_args():
    sig = inspect.signature(gaml_StringEvaluator.__init__)
    params = list(sig.parameters.keys())
    assert "toto" in params, "Missing parameter 'toto'"

def test_gaml_stringevaluator_has_toto():
    assert hasattr(gaml_StringEvaluator, "toto")
    descriptor = None
    for klass in gaml_StringEvaluator.__mro__:
        if "toto" in klass.__dict__:
            descriptor = klass.__dict__["toto"]
            break
    assert isinstance(descriptor, property)



def test_gaml_experimentfilestructure_is_not_abstract():
    assert not inspect.isabstract(gaml_ExperimentFileStructure)


def test_gaml_experimentfilestructure_constructor_exists():
    assert callable(gaml_ExperimentFileStructure.__init__)


def test_gaml_experimentfilestructure_constructor_args():
    sig = inspect.signature(gaml_ExperimentFileStructure.__init__)
    params = list(sig.parameters.keys())



def test_gaml_model_is_not_abstract():
    assert not inspect.isabstract(gaml_Model)


def test_gaml_model_constructor_exists():
    assert callable(gaml_Model.__init__)


def test_gaml_model_constructor_args():
    sig = inspect.signature(gaml_Model.__init__)
    params = list(sig.parameters.keys())



def test_gaml_standaloneblock_is_not_abstract():
    assert not inspect.isabstract(gaml_StandaloneBlock)


def test_gaml_standaloneblock_constructor_exists():
    assert callable(gaml_StandaloneBlock.__init__)


def test_gaml_standaloneblock_constructor_args():
    sig = inspect.signature(gaml_StandaloneBlock.__init__)
    params = list(sig.parameters.keys())



def test_gaml_entry_is_not_abstract():
    assert not inspect.isabstract(gaml_Entry)


def test_gaml_entry_constructor_exists():
    assert callable(gaml_Entry.__init__)


def test_gaml_entry_constructor_args():
    sig = inspect.signature(gaml_Entry.__init__)
    params = list(sig.parameters.keys())



def test_gaml_facet_is_not_abstract():
    assert not inspect.isabstract(gaml_Facet)


def test_gaml_facet_constructor_exists():
    assert callable(gaml_Facet.__init__)


def test_gaml_facet_constructor_args():
    sig = inspect.signature(gaml_Facet.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_gaml_facet_has_key():
    assert hasattr(gaml_Facet, "key")
    descriptor = None
    for klass in gaml_Facet.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_gaml_reservedliteral_is_not_abstract():
    assert not inspect.isabstract(gaml_ReservedLiteral)


def test_gaml_reservedliteral_constructor_exists():
    assert callable(gaml_ReservedLiteral.__init__)


def test_gaml_reservedliteral_constructor_args():
    sig = inspect.signature(gaml_ReservedLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(gaml_BooleanLiteral)


def test_gaml_booleanliteral_constructor_exists():
    assert callable(gaml_BooleanLiteral.__init__)


def test_gaml_booleanliteral_constructor_args():
    sig = inspect.signature(gaml_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(gaml_DoubleLiteral)


def test_gaml_doubleliteral_constructor_exists():
    assert callable(gaml_DoubleLiteral.__init__)


def test_gaml_doubleliteral_constructor_args():
    sig = inspect.signature(gaml_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml_intliteral_is_not_abstract():
    assert not inspect.isabstract(gaml_IntLiteral)


def test_gaml_intliteral_constructor_exists():
    assert callable(gaml_IntLiteral.__init__)


def test_gaml_intliteral_constructor_args():
    sig = inspect.signature(gaml_IntLiteral.__init__)
    params = list(sig.parameters.keys())



def test_gaml_typeref_is_not_abstract():
    assert not inspect.isabstract(gaml_TypeRef)


def test_gaml_typeref_constructor_exists():
    assert callable(gaml_TypeRef.__init__)


def test_gaml_typeref_constructor_args():
    sig = inspect.signature(gaml_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml_unitname_is_not_abstract():
    assert not inspect.isabstract(gaml_UnitName)


def test_gaml_unitname_constructor_exists():
    assert callable(gaml_UnitName.__init__)


def test_gaml_unitname_constructor_args():
    sig = inspect.signature(gaml_UnitName.__init__)
    params = list(sig.parameters.keys())



def test_gaml_parameter_is_not_abstract():
    assert not inspect.isabstract(gaml_Parameter)


def test_gaml_parameter_constructor_exists():
    assert callable(gaml_Parameter.__init__)


def test_gaml_parameter_constructor_args():
    sig = inspect.signature(gaml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "builtInFacetKey" in params, "Missing parameter 'builtInFacetKey'"

def test_gaml_parameter_has_builtInFacetKey():
    assert hasattr(gaml_Parameter, "builtInFacetKey")
    descriptor = None
    for klass in gaml_Parameter.__mro__:
        if "builtInFacetKey" in klass.__dict__:
            descriptor = klass.__dict__["builtInFacetKey"]
            break
    assert isinstance(descriptor, property)



def test_gaml_function_is_not_abstract():
    assert not inspect.isabstract(gaml_Function)


def test_gaml_function_constructor_exists():
    assert callable(gaml_Function.__init__)


def test_gaml_function_constructor_args():
    sig = inspect.signature(gaml_Function.__init__)
    params = list(sig.parameters.keys())



def test_gaml_point_is_not_abstract():
    assert not inspect.isabstract(gaml_Point)


def test_gaml_point_constructor_exists():
    assert callable(gaml_Point.__init__)


def test_gaml_point_constructor_args():
    sig = inspect.signature(gaml_Point.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_point_has_op():
    assert hasattr(gaml_Point, "op")
    descriptor = None
    for klass in gaml_Point.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_equationref_is_not_abstract():
    assert not inspect.isabstract(gaml_EquationRef)


def test_gaml_equationref_constructor_exists():
    assert callable(gaml_EquationRef.__init__)


def test_gaml_equationref_constructor_args():
    sig = inspect.signature(gaml_EquationRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml_actionref_is_not_abstract():
    assert not inspect.isabstract(gaml_ActionRef)


def test_gaml_actionref_constructor_exists():
    assert callable(gaml_ActionRef.__init__)


def test_gaml_actionref_constructor_args():
    sig = inspect.signature(gaml_ActionRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml_skillref_is_not_abstract():
    assert not inspect.isabstract(gaml_SkillRef)


def test_gaml_skillref_constructor_exists():
    assert callable(gaml_SkillRef.__init__)


def test_gaml_skillref_constructor_args():
    sig = inspect.signature(gaml_SkillRef.__init__)
    params = list(sig.parameters.keys())



def test_gaml_unary_is_not_abstract():
    assert not inspect.isabstract(gaml_Unary)


def test_gaml_unary_constructor_exists():
    assert callable(gaml_Unary.__init__)


def test_gaml_unary_constructor_args():
    sig = inspect.signature(gaml_Unary.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_unary_has_op():
    assert hasattr(gaml_Unary, "op")
    descriptor = None
    for klass in gaml_Unary.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_gaml_unit_is_not_abstract():
    assert not inspect.isabstract(gaml_Unit)


def test_gaml_unit_constructor_exists():
    assert callable(gaml_Unit.__init__)


def test_gaml_unit_constructor_args():
    sig = inspect.signature(gaml_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_gaml_unit_has_op():
    assert hasattr(gaml_Unit, "op")
    descriptor = None
    for klass in gaml_Unit.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
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
S_Definition_strategy = st.builds(
    S_Definition,
)
gaml_S_Var_strategy = st.builds(
    gaml_S_Var,
)
gaml_S_Action_strategy = st.builds(
    gaml_S_Action,
)
TerminalExpression_strategy = st.builds(
    TerminalExpression,
)
gaml_StringLiteral_strategy = st.builds(
    gaml_StringLiteral,
)
gaml_TypeInfo_strategy = st.builds(
    gaml_TypeInfo,
)
Expression_strategy = st.builds(
    Expression,
)
gaml_Access_strategy = st.builds(
    gaml_Access,
    op=
        safe_text
)
gaml_BinaryOperator_strategy = st.builds(
    gaml_BinaryOperator,
    op=
        safe_text
)
gaml_Array_strategy = st.builds(
    gaml_Array,
)
gaml_VariableRef_strategy = st.builds(
    gaml_VariableRef,
)
gaml_ExpressionList_strategy = st.builds(
    gaml_ExpressionList,
)
gaml_If_strategy = st.builds(
    gaml_If,
    op=
        safe_text
)
gaml_TerminalExpression_strategy = st.builds(
    gaml_TerminalExpression,
    op=
        safe_text
)
gaml_ArgumentPair_strategy = st.builds(
    gaml_ArgumentPair,
    op=
        safe_text
)
GamlDefinition_strategy = st.builds(
    GamlDefinition,
)
gaml_SkillFakeDefinition_strategy = st.builds(
    gaml_SkillFakeDefinition,
)
gaml_VarDefinition_strategy = st.builds(
    gaml_VarDefinition,
)
gaml_ActionDefinition_strategy = st.builds(
    gaml_ActionDefinition,
)
gaml_UnitFakeDefinition_strategy = st.builds(
    gaml_UnitFakeDefinition,
)
gaml_EquationDefinition_strategy = st.builds(
    gaml_EquationDefinition,
)
gaml_GamlDefinition_strategy = st.builds(
    gaml_GamlDefinition,
    name=
        safe_text
)
gaml_ActionArguments_strategy = st.builds(
    gaml_ActionArguments,
)
ActionDefinition_strategy = st.builds(
    ActionDefinition,
)
gaml_TypeDefinition_strategy = st.builds(
    gaml_TypeDefinition,
)
gaml_ActionFakeDefinition_strategy = st.builds(
    gaml_ActionFakeDefinition,
)
gaml_EObject_strategy = st.builds(
    gaml_EObject,
)
TypeDefinition_strategy = st.builds(
    TypeDefinition,
)
gaml_TypeFakeDefinition_strategy = st.builds(
    gaml_TypeFakeDefinition,
)
S_Declaration_strategy = st.builds(
    S_Declaration,
)
gaml_S_Reflex_strategy = st.builds(
    gaml_S_Reflex,
)
gaml_S_Definition_strategy = st.builds(
    gaml_S_Definition,
)
gaml_S_Loop_strategy = st.builds(
    gaml_S_Loop,
)
Statement_strategy = st.builds(
    Statement,
)
gaml_S_Species_strategy = st.builds(
    gaml_S_Species,
)
gaml_S_Try_strategy = st.builds(
    gaml_S_Try,
)
gaml_speciesOrGridDisplayStatement_strategy = st.builds(
    gaml_speciesOrGridDisplayStatement,
)
gaml_S_Display_strategy = st.builds(
    gaml_S_Display,
    name=
        safe_text
)
gaml_S_Return_strategy = st.builds(
    gaml_S_Return,
)
gaml_S_Other_strategy = st.builds(
    gaml_S_Other,
)
gaml_S_Do_strategy = st.builds(
    gaml_S_Do,
)
gaml_S_If_strategy = st.builds(
    gaml_S_If,
)
gaml_S_Solve_strategy = st.builds(
    gaml_S_Solve,
)
gaml_S_Global_strategy = st.builds(
    gaml_S_Global,
)
EquationDefinition_strategy = st.builds(
    EquationDefinition,
)
gaml_EquationFakeDefinition_strategy = st.builds(
    gaml_EquationFakeDefinition,
)
gaml_S_Equations_strategy = st.builds(
    gaml_S_Equations,
)
S_Assignment_strategy = st.builds(
    S_Assignment,
)
gaml_S_Set_strategy = st.builds(
    gaml_S_Set,
)
gaml_S_DirectAssignment_strategy = st.builds(
    gaml_S_DirectAssignment,
)
gaml_S_Assignment_strategy = st.builds(
    gaml_S_Assignment,
)
gaml_HeadlessExperiment_strategy = st.builds(
    gaml_HeadlessExperiment,
    firstFacet=
        safe_text,
    name=
        safe_text,
    key=
        safe_text,
    importURI=
        safe_text
)
gaml_Statement_strategy = st.builds(
    gaml_Statement,
    firstFacet=
        safe_text,
    key=
        safe_text
)
gaml_Pragma_strategy = st.builds(
    gaml_Pragma,
    name=
        safe_text
)
VarDefinition_strategy = st.builds(
    VarDefinition,
)
gaml_S_Declaration_strategy = st.builds(
    gaml_S_Declaration,
)
gaml_S_Experiment_strategy = st.builds(
    gaml_S_Experiment,
)
gaml_ArgumentDefinition_strategy = st.builds(
    gaml_ArgumentDefinition,
)
gaml_VarFakeDefinition_strategy = st.builds(
    gaml_VarFakeDefinition,
)
gaml_Import_strategy = st.builds(
    gaml_Import,
    importURI=
        safe_text
)
gaml_Expression_strategy = st.builds(
    gaml_Expression,
)
gaml_Block_strategy = st.builds(
    gaml_Block,
)
Entry_strategy = st.builds(
    Entry,
)
gaml_StringEvaluator_strategy = st.builds(
    gaml_StringEvaluator,
    toto=
        safe_text
)
gaml_ExperimentFileStructure_strategy = st.builds(
    gaml_ExperimentFileStructure,
)
gaml_Model_strategy = st.builds(
    gaml_Model,
)
gaml_StandaloneBlock_strategy = st.builds(
    gaml_StandaloneBlock,
)
gaml_Entry_strategy = st.builds(
    gaml_Entry,
)
gaml_Facet_strategy = st.builds(
    gaml_Facet,
    key=
        safe_text
)
gaml_ReservedLiteral_strategy = st.builds(
    gaml_ReservedLiteral,
)
gaml_BooleanLiteral_strategy = st.builds(
    gaml_BooleanLiteral,
)
gaml_DoubleLiteral_strategy = st.builds(
    gaml_DoubleLiteral,
)
gaml_IntLiteral_strategy = st.builds(
    gaml_IntLiteral,
)
gaml_TypeRef_strategy = st.builds(
    gaml_TypeRef,
)
gaml_UnitName_strategy = st.builds(
    gaml_UnitName,
)
gaml_Parameter_strategy = st.builds(
    gaml_Parameter,
    builtInFacetKey=
        safe_text
)
gaml_Function_strategy = st.builds(
    gaml_Function,
)
gaml_Point_strategy = st.builds(
    gaml_Point,
    op=
        safe_text
)
gaml_EquationRef_strategy = st.builds(
    gaml_EquationRef,
)
gaml_ActionRef_strategy = st.builds(
    gaml_ActionRef,
)
gaml_SkillRef_strategy = st.builds(
    gaml_SkillRef,
)
gaml_Unary_strategy = st.builds(
    gaml_Unary,
    op=
        safe_text
)
gaml_Unit_strategy = st.builds(
    gaml_Unit,
    op=
        safe_text
)

@given(instance=S_Definition_strategy)
@settings(max_examples=50)
def test_s_definition_instantiation(instance):
    assert isinstance(instance, S_Definition)

@given(instance=gaml_S_Var_strategy)
@settings(max_examples=50)
def test_gaml_s_var_instantiation(instance):
    assert isinstance(instance, gaml_S_Var)

@given(instance=gaml_S_Action_strategy)
@settings(max_examples=50)
def test_gaml_s_action_instantiation(instance):
    assert isinstance(instance, gaml_S_Action)

@given(instance=TerminalExpression_strategy)
@settings(max_examples=50)
def test_terminalexpression_instantiation(instance):
    assert isinstance(instance, TerminalExpression)

@given(instance=gaml_StringLiteral_strategy)
@settings(max_examples=50)
def test_gaml_stringliteral_instantiation(instance):
    assert isinstance(instance, gaml_StringLiteral)

@given(instance=gaml_TypeInfo_strategy)
@settings(max_examples=50)
def test_gaml_typeinfo_instantiation(instance):
    assert isinstance(instance, gaml_TypeInfo)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=gaml_Access_strategy)
@settings(max_examples=50)
def test_gaml_access_instantiation(instance):
    assert isinstance(instance, gaml_Access)



@given(instance=gaml_Access_strategy)
def test_gaml_access_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_BinaryOperator_strategy)
@settings(max_examples=50)
def test_gaml_binaryoperator_instantiation(instance):
    assert isinstance(instance, gaml_BinaryOperator)



@given(instance=gaml_BinaryOperator_strategy)
def test_gaml_binaryoperator_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_Array_strategy)
@settings(max_examples=50)
def test_gaml_array_instantiation(instance):
    assert isinstance(instance, gaml_Array)

@given(instance=gaml_VariableRef_strategy)
@settings(max_examples=50)
def test_gaml_variableref_instantiation(instance):
    assert isinstance(instance, gaml_VariableRef)

@given(instance=gaml_ExpressionList_strategy)
@settings(max_examples=50)
def test_gaml_expressionlist_instantiation(instance):
    assert isinstance(instance, gaml_ExpressionList)

@given(instance=gaml_If_strategy)
@settings(max_examples=50)
def test_gaml_if_instantiation(instance):
    assert isinstance(instance, gaml_If)



@given(instance=gaml_If_strategy)
def test_gaml_if_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_TerminalExpression_strategy)
@settings(max_examples=50)
def test_gaml_terminalexpression_instantiation(instance):
    assert isinstance(instance, gaml_TerminalExpression)



@given(instance=gaml_TerminalExpression_strategy)
def test_gaml_terminalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_ArgumentPair_strategy)
@settings(max_examples=50)
def test_gaml_argumentpair_instantiation(instance):
    assert isinstance(instance, gaml_ArgumentPair)



@given(instance=gaml_ArgumentPair_strategy)
def test_gaml_argumentpair_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=GamlDefinition_strategy)
@settings(max_examples=50)
def test_gamldefinition_instantiation(instance):
    assert isinstance(instance, GamlDefinition)

@given(instance=gaml_SkillFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_skillfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_SkillFakeDefinition)

@given(instance=gaml_VarDefinition_strategy)
@settings(max_examples=50)
def test_gaml_vardefinition_instantiation(instance):
    assert isinstance(instance, gaml_VarDefinition)

@given(instance=gaml_ActionDefinition_strategy)
@settings(max_examples=50)
def test_gaml_actiondefinition_instantiation(instance):
    assert isinstance(instance, gaml_ActionDefinition)

@given(instance=gaml_UnitFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_unitfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_UnitFakeDefinition)

@given(instance=gaml_EquationDefinition_strategy)
@settings(max_examples=50)
def test_gaml_equationdefinition_instantiation(instance):
    assert isinstance(instance, gaml_EquationDefinition)

@given(instance=gaml_GamlDefinition_strategy)
@settings(max_examples=50)
def test_gaml_gamldefinition_instantiation(instance):
    assert isinstance(instance, gaml_GamlDefinition)



@given(instance=gaml_GamlDefinition_strategy)
def test_gaml_gamldefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gaml_ActionArguments_strategy)
@settings(max_examples=50)
def test_gaml_actionarguments_instantiation(instance):
    assert isinstance(instance, gaml_ActionArguments)

@given(instance=ActionDefinition_strategy)
@settings(max_examples=50)
def test_actiondefinition_instantiation(instance):
    assert isinstance(instance, ActionDefinition)

@given(instance=gaml_TypeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_typedefinition_instantiation(instance):
    assert isinstance(instance, gaml_TypeDefinition)

@given(instance=gaml_ActionFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_actionfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_ActionFakeDefinition)

@given(instance=gaml_EObject_strategy)
@settings(max_examples=50)
def test_gaml_eobject_instantiation(instance):
    assert isinstance(instance, gaml_EObject)

@given(instance=TypeDefinition_strategy)
@settings(max_examples=50)
def test_typedefinition_instantiation(instance):
    assert isinstance(instance, TypeDefinition)

@given(instance=gaml_TypeFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_typefakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_TypeFakeDefinition)

@given(instance=S_Declaration_strategy)
@settings(max_examples=50)
def test_s_declaration_instantiation(instance):
    assert isinstance(instance, S_Declaration)

@given(instance=gaml_S_Reflex_strategy)
@settings(max_examples=50)
def test_gaml_s_reflex_instantiation(instance):
    assert isinstance(instance, gaml_S_Reflex)

@given(instance=gaml_S_Definition_strategy)
@settings(max_examples=50)
def test_gaml_s_definition_instantiation(instance):
    assert isinstance(instance, gaml_S_Definition)

@given(instance=gaml_S_Loop_strategy)
@settings(max_examples=50)
def test_gaml_s_loop_instantiation(instance):
    assert isinstance(instance, gaml_S_Loop)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=gaml_S_Species_strategy)
@settings(max_examples=50)
def test_gaml_s_species_instantiation(instance):
    assert isinstance(instance, gaml_S_Species)

@given(instance=gaml_S_Try_strategy)
@settings(max_examples=50)
def test_gaml_s_try_instantiation(instance):
    assert isinstance(instance, gaml_S_Try)

@given(instance=gaml_speciesOrGridDisplayStatement_strategy)
@settings(max_examples=50)
def test_gaml_speciesorgriddisplaystatement_instantiation(instance):
    assert isinstance(instance, gaml_speciesOrGridDisplayStatement)

@given(instance=gaml_S_Display_strategy)
@settings(max_examples=50)
def test_gaml_s_display_instantiation(instance):
    assert isinstance(instance, gaml_S_Display)



@given(instance=gaml_S_Display_strategy)
def test_gaml_s_display_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gaml_S_Return_strategy)
@settings(max_examples=50)
def test_gaml_s_return_instantiation(instance):
    assert isinstance(instance, gaml_S_Return)

@given(instance=gaml_S_Other_strategy)
@settings(max_examples=50)
def test_gaml_s_other_instantiation(instance):
    assert isinstance(instance, gaml_S_Other)

@given(instance=gaml_S_Do_strategy)
@settings(max_examples=50)
def test_gaml_s_do_instantiation(instance):
    assert isinstance(instance, gaml_S_Do)

@given(instance=gaml_S_If_strategy)
@settings(max_examples=50)
def test_gaml_s_if_instantiation(instance):
    assert isinstance(instance, gaml_S_If)

@given(instance=gaml_S_Solve_strategy)
@settings(max_examples=50)
def test_gaml_s_solve_instantiation(instance):
    assert isinstance(instance, gaml_S_Solve)

@given(instance=gaml_S_Global_strategy)
@settings(max_examples=50)
def test_gaml_s_global_instantiation(instance):
    assert isinstance(instance, gaml_S_Global)

@given(instance=EquationDefinition_strategy)
@settings(max_examples=50)
def test_equationdefinition_instantiation(instance):
    assert isinstance(instance, EquationDefinition)

@given(instance=gaml_EquationFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_equationfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_EquationFakeDefinition)

@given(instance=gaml_S_Equations_strategy)
@settings(max_examples=50)
def test_gaml_s_equations_instantiation(instance):
    assert isinstance(instance, gaml_S_Equations)

@given(instance=S_Assignment_strategy)
@settings(max_examples=50)
def test_s_assignment_instantiation(instance):
    assert isinstance(instance, S_Assignment)

@given(instance=gaml_S_Set_strategy)
@settings(max_examples=50)
def test_gaml_s_set_instantiation(instance):
    assert isinstance(instance, gaml_S_Set)

@given(instance=gaml_S_DirectAssignment_strategy)
@settings(max_examples=50)
def test_gaml_s_directassignment_instantiation(instance):
    assert isinstance(instance, gaml_S_DirectAssignment)

@given(instance=gaml_S_Assignment_strategy)
@settings(max_examples=50)
def test_gaml_s_assignment_instantiation(instance):
    assert isinstance(instance, gaml_S_Assignment)

@given(instance=gaml_HeadlessExperiment_strategy)
@settings(max_examples=50)
def test_gaml_headlessexperiment_instantiation(instance):
    assert isinstance(instance, gaml_HeadlessExperiment)



@given(instance=gaml_HeadlessExperiment_strategy)
def test_gaml_headlessexperiment_firstFacet_setter(instance):
    original = instance.firstFacet
    instance.firstFacet = original
    assert instance.firstFacet == original



@given(instance=gaml_HeadlessExperiment_strategy)
def test_gaml_headlessexperiment_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=gaml_HeadlessExperiment_strategy)
def test_gaml_headlessexperiment_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=gaml_HeadlessExperiment_strategy)
def test_gaml_headlessexperiment_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=gaml_Statement_strategy)
@settings(max_examples=50)
def test_gaml_statement_instantiation(instance):
    assert isinstance(instance, gaml_Statement)



@given(instance=gaml_Statement_strategy)
def test_gaml_statement_firstFacet_setter(instance):
    original = instance.firstFacet
    instance.firstFacet = original
    assert instance.firstFacet == original



@given(instance=gaml_Statement_strategy)
def test_gaml_statement_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gaml_Pragma_strategy)
@settings(max_examples=50)
def test_gaml_pragma_instantiation(instance):
    assert isinstance(instance, gaml_Pragma)



@given(instance=gaml_Pragma_strategy)
def test_gaml_pragma_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=VarDefinition_strategy)
@settings(max_examples=50)
def test_vardefinition_instantiation(instance):
    assert isinstance(instance, VarDefinition)

@given(instance=gaml_S_Declaration_strategy)
@settings(max_examples=50)
def test_gaml_s_declaration_instantiation(instance):
    assert isinstance(instance, gaml_S_Declaration)

@given(instance=gaml_S_Experiment_strategy)
@settings(max_examples=50)
def test_gaml_s_experiment_instantiation(instance):
    assert isinstance(instance, gaml_S_Experiment)

@given(instance=gaml_ArgumentDefinition_strategy)
@settings(max_examples=50)
def test_gaml_argumentdefinition_instantiation(instance):
    assert isinstance(instance, gaml_ArgumentDefinition)

@given(instance=gaml_VarFakeDefinition_strategy)
@settings(max_examples=50)
def test_gaml_varfakedefinition_instantiation(instance):
    assert isinstance(instance, gaml_VarFakeDefinition)

@given(instance=gaml_Import_strategy)
@settings(max_examples=50)
def test_gaml_import_instantiation(instance):
    assert isinstance(instance, gaml_Import)



@given(instance=gaml_Import_strategy)
def test_gaml_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original

@given(instance=gaml_Expression_strategy)
@settings(max_examples=50)
def test_gaml_expression_instantiation(instance):
    assert isinstance(instance, gaml_Expression)

@given(instance=gaml_Block_strategy)
@settings(max_examples=50)
def test_gaml_block_instantiation(instance):
    assert isinstance(instance, gaml_Block)

@given(instance=Entry_strategy)
@settings(max_examples=50)
def test_entry_instantiation(instance):
    assert isinstance(instance, Entry)

@given(instance=gaml_StringEvaluator_strategy)
@settings(max_examples=50)
def test_gaml_stringevaluator_instantiation(instance):
    assert isinstance(instance, gaml_StringEvaluator)



@given(instance=gaml_StringEvaluator_strategy)
def test_gaml_stringevaluator_toto_setter(instance):
    original = instance.toto
    instance.toto = original
    assert instance.toto == original

@given(instance=gaml_ExperimentFileStructure_strategy)
@settings(max_examples=50)
def test_gaml_experimentfilestructure_instantiation(instance):
    assert isinstance(instance, gaml_ExperimentFileStructure)

@given(instance=gaml_Model_strategy)
@settings(max_examples=50)
def test_gaml_model_instantiation(instance):
    assert isinstance(instance, gaml_Model)

@given(instance=gaml_StandaloneBlock_strategy)
@settings(max_examples=50)
def test_gaml_standaloneblock_instantiation(instance):
    assert isinstance(instance, gaml_StandaloneBlock)

@given(instance=gaml_Entry_strategy)
@settings(max_examples=50)
def test_gaml_entry_instantiation(instance):
    assert isinstance(instance, gaml_Entry)

@given(instance=gaml_Facet_strategy)
@settings(max_examples=50)
def test_gaml_facet_instantiation(instance):
    assert isinstance(instance, gaml_Facet)



@given(instance=gaml_Facet_strategy)
def test_gaml_facet_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=gaml_ReservedLiteral_strategy)
@settings(max_examples=50)
def test_gaml_reservedliteral_instantiation(instance):
    assert isinstance(instance, gaml_ReservedLiteral)

@given(instance=gaml_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_gaml_booleanliteral_instantiation(instance):
    assert isinstance(instance, gaml_BooleanLiteral)

@given(instance=gaml_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_gaml_doubleliteral_instantiation(instance):
    assert isinstance(instance, gaml_DoubleLiteral)

@given(instance=gaml_IntLiteral_strategy)
@settings(max_examples=50)
def test_gaml_intliteral_instantiation(instance):
    assert isinstance(instance, gaml_IntLiteral)

@given(instance=gaml_TypeRef_strategy)
@settings(max_examples=50)
def test_gaml_typeref_instantiation(instance):
    assert isinstance(instance, gaml_TypeRef)

@given(instance=gaml_UnitName_strategy)
@settings(max_examples=50)
def test_gaml_unitname_instantiation(instance):
    assert isinstance(instance, gaml_UnitName)

@given(instance=gaml_Parameter_strategy)
@settings(max_examples=50)
def test_gaml_parameter_instantiation(instance):
    assert isinstance(instance, gaml_Parameter)



@given(instance=gaml_Parameter_strategy)
def test_gaml_parameter_builtInFacetKey_setter(instance):
    original = instance.builtInFacetKey
    instance.builtInFacetKey = original
    assert instance.builtInFacetKey == original

@given(instance=gaml_Function_strategy)
@settings(max_examples=50)
def test_gaml_function_instantiation(instance):
    assert isinstance(instance, gaml_Function)

@given(instance=gaml_Point_strategy)
@settings(max_examples=50)
def test_gaml_point_instantiation(instance):
    assert isinstance(instance, gaml_Point)



@given(instance=gaml_Point_strategy)
def test_gaml_point_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_EquationRef_strategy)
@settings(max_examples=50)
def test_gaml_equationref_instantiation(instance):
    assert isinstance(instance, gaml_EquationRef)

@given(instance=gaml_ActionRef_strategy)
@settings(max_examples=50)
def test_gaml_actionref_instantiation(instance):
    assert isinstance(instance, gaml_ActionRef)

@given(instance=gaml_SkillRef_strategy)
@settings(max_examples=50)
def test_gaml_skillref_instantiation(instance):
    assert isinstance(instance, gaml_SkillRef)

@given(instance=gaml_Unary_strategy)
@settings(max_examples=50)
def test_gaml_unary_instantiation(instance):
    assert isinstance(instance, gaml_Unary)



@given(instance=gaml_Unary_strategy)
def test_gaml_unary_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=gaml_Unit_strategy)
@settings(max_examples=50)
def test_gaml_unit_instantiation(instance):
    assert isinstance(instance, gaml_Unit)



@given(instance=gaml_Unit_strategy)
def test_gaml_unit_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original
