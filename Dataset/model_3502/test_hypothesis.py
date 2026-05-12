import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    go_ElseCondition,
    go_ElseIfCondition,
    go_BasicType,
    go_PARAMETER,
    go_BOOL_OP,
    ElseIfCondition,
    go_IfCondition,
    go_PARAMETERS_LIST,
    go_Parameters,
    go_BLOCK,
    go_Signature,
    go_ReturnStmt,
    go_IfStmt,
    go_Chamada,
    go_ArrayValue,
    go_EObject,
    go_LiteraisList,
    go_Const,
    go_LITERAIS_BASICOS,
    go_BINARY_EXP,
    go_ArrayType,
    go_Var,
    go_SignatureDel,
    go_Assignment,
    go_Types,
    go_TIPO,
    go_ARIT_EXPR,
    go_PostStmt,
    go_Condition,
    go_InitStmt,
    go_COMPARISON,
    go_EXPRESSAO,
    go_RangeDecl,
    go_ForClause,
    go_ForDecl,
    go_EXPRESSAOLINHA,
    go_FunctionType,
    go_FunctionCall,
    go_VarCall,
    go_PONTOSIGUAL,
    go_IGUAL,
    go_IDList,
    go_VarDecl,
    go_BOOLEAN_VALUE,
    go_GoDecl,
    go_Init,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_go_elsecondition_is_not_abstract():
    assert not inspect.isabstract(go_ElseCondition)


def test_go_elsecondition_constructor_exists():
    assert callable(go_ElseCondition.__init__)


def test_go_elsecondition_constructor_args():
    sig = inspect.signature(go_ElseCondition.__init__)
    params = list(sig.parameters.keys())



def test_go_elseifcondition_is_not_abstract():
    assert not inspect.isabstract(go_ElseIfCondition)


def test_go_elseifcondition_constructor_exists():
    assert callable(go_ElseIfCondition.__init__)


def test_go_elseifcondition_constructor_args():
    sig = inspect.signature(go_ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go_basictype_is_not_abstract():
    assert not inspect.isabstract(go_BasicType)


def test_go_basictype_constructor_exists():
    assert callable(go_BasicType.__init__)


def test_go_basictype_constructor_args():
    sig = inspect.signature(go_BasicType.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "string" in params, "Missing parameter 'string'"
    assert "float" in params, "Missing parameter 'float'"

def test_go_basictype_has_int():
    assert hasattr(go_BasicType, "int")
    descriptor = None
    for klass in go_BasicType.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)

def test_go_basictype_has_boolean():
    assert hasattr(go_BasicType, "boolean")
    descriptor = None
    for klass in go_BasicType.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_go_basictype_has_string():
    assert hasattr(go_BasicType, "string")
    descriptor = None
    for klass in go_BasicType.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_go_basictype_has_float():
    assert hasattr(go_BasicType, "float")
    descriptor = None
    for klass in go_BasicType.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)



def test_go_parameter_is_not_abstract():
    assert not inspect.isabstract(go_PARAMETER)


def test_go_parameter_constructor_exists():
    assert callable(go_PARAMETER.__init__)


def test_go_parameter_constructor_args():
    sig = inspect.signature(go_PARAMETER.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go_parameter_has_id():
    assert hasattr(go_PARAMETER, "id")
    descriptor = None
    for klass in go_PARAMETER.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go_bool_op_is_not_abstract():
    assert not inspect.isabstract(go_BOOL_OP)


def test_go_bool_op_constructor_exists():
    assert callable(go_BOOL_OP.__init__)


def test_go_bool_op_constructor_args():
    sig = inspect.signature(go_BOOL_OP.__init__)
    params = list(sig.parameters.keys())



def test_elseifcondition_is_not_abstract():
    assert not inspect.isabstract(ElseIfCondition)


def test_elseifcondition_constructor_exists():
    assert callable(ElseIfCondition.__init__)


def test_elseifcondition_constructor_args():
    sig = inspect.signature(ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go_ifcondition_is_not_abstract():
    assert not inspect.isabstract(go_IfCondition)


def test_go_ifcondition_constructor_exists():
    assert callable(go_IfCondition.__init__)


def test_go_ifcondition_constructor_args():
    sig = inspect.signature(go_IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go_parameters_list_is_not_abstract():
    assert not inspect.isabstract(go_PARAMETERS_LIST)


def test_go_parameters_list_constructor_exists():
    assert callable(go_PARAMETERS_LIST.__init__)


def test_go_parameters_list_constructor_args():
    sig = inspect.signature(go_PARAMETERS_LIST.__init__)
    params = list(sig.parameters.keys())
    assert "vir" in params, "Missing parameter 'vir'"

def test_go_parameters_list_has_vir():
    assert hasattr(go_PARAMETERS_LIST, "vir")
    descriptor = None
    for klass in go_PARAMETERS_LIST.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)



def test_go_parameters_is_not_abstract():
    assert not inspect.isabstract(go_Parameters)


def test_go_parameters_constructor_exists():
    assert callable(go_Parameters.__init__)


def test_go_parameters_constructor_args():
    sig = inspect.signature(go_Parameters.__init__)
    params = list(sig.parameters.keys())



def test_go_block_is_not_abstract():
    assert not inspect.isabstract(go_BLOCK)


def test_go_block_constructor_exists():
    assert callable(go_BLOCK.__init__)


def test_go_block_constructor_args():
    sig = inspect.signature(go_BLOCK.__init__)
    params = list(sig.parameters.keys())



def test_go_signature_is_not_abstract():
    assert not inspect.isabstract(go_Signature)


def test_go_signature_constructor_exists():
    assert callable(go_Signature.__init__)


def test_go_signature_constructor_args():
    sig = inspect.signature(go_Signature.__init__)
    params = list(sig.parameters.keys())



def test_go_returnstmt_is_not_abstract():
    assert not inspect.isabstract(go_ReturnStmt)


def test_go_returnstmt_constructor_exists():
    assert callable(go_ReturnStmt.__init__)


def test_go_returnstmt_constructor_args():
    sig = inspect.signature(go_ReturnStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_ifstmt_is_not_abstract():
    assert not inspect.isabstract(go_IfStmt)


def test_go_ifstmt_constructor_exists():
    assert callable(go_IfStmt.__init__)


def test_go_ifstmt_constructor_args():
    sig = inspect.signature(go_IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_chamada_is_not_abstract():
    assert not inspect.isabstract(go_Chamada)


def test_go_chamada_constructor_exists():
    assert callable(go_Chamada.__init__)


def test_go_chamada_constructor_args():
    sig = inspect.signature(go_Chamada.__init__)
    params = list(sig.parameters.keys())



def test_go_arrayvalue_is_not_abstract():
    assert not inspect.isabstract(go_ArrayValue)


def test_go_arrayvalue_constructor_exists():
    assert callable(go_ArrayValue.__init__)


def test_go_arrayvalue_constructor_args():
    sig = inspect.signature(go_ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_go_eobject_is_not_abstract():
    assert not inspect.isabstract(go_EObject)


def test_go_eobject_constructor_exists():
    assert callable(go_EObject.__init__)


def test_go_eobject_constructor_args():
    sig = inspect.signature(go_EObject.__init__)
    params = list(sig.parameters.keys())



def test_go_literaislist_is_not_abstract():
    assert not inspect.isabstract(go_LiteraisList)


def test_go_literaislist_constructor_exists():
    assert callable(go_LiteraisList.__init__)


def test_go_literaislist_constructor_args():
    sig = inspect.signature(go_LiteraisList.__init__)
    params = list(sig.parameters.keys())
    assert "vir" in params, "Missing parameter 'vir'"

def test_go_literaislist_has_vir():
    assert hasattr(go_LiteraisList, "vir")
    descriptor = None
    for klass in go_LiteraisList.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)



def test_go_const_is_not_abstract():
    assert not inspect.isabstract(go_Const)


def test_go_const_constructor_exists():
    assert callable(go_Const.__init__)


def test_go_const_constructor_args():
    sig = inspect.signature(go_Const.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"

def test_go_const_has_const():
    assert hasattr(go_Const, "const")
    descriptor = None
    for klass in go_Const.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_go_literais_basicos_is_not_abstract():
    assert not inspect.isabstract(go_LITERAIS_BASICOS)


def test_go_literais_basicos_constructor_exists():
    assert callable(go_LITERAIS_BASICOS.__init__)


def test_go_literais_basicos_constructor_args():
    sig = inspect.signature(go_LITERAIS_BASICOS.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "string" in params, "Missing parameter 'string'"

def test_go_literais_basicos_has_numero():
    assert hasattr(go_LITERAIS_BASICOS, "numero")
    descriptor = None
    for klass in go_LITERAIS_BASICOS.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_go_literais_basicos_has_string():
    assert hasattr(go_LITERAIS_BASICOS, "string")
    descriptor = None
    for klass in go_LITERAIS_BASICOS.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_go_binary_exp_is_not_abstract():
    assert not inspect.isabstract(go_BINARY_EXP)


def test_go_binary_exp_constructor_exists():
    assert callable(go_BINARY_EXP.__init__)


def test_go_binary_exp_constructor_args():
    sig = inspect.signature(go_BINARY_EXP.__init__)
    params = list(sig.parameters.keys())
    assert "arit" in params, "Missing parameter 'arit'"

def test_go_binary_exp_has_arit():
    assert hasattr(go_BINARY_EXP, "arit")
    descriptor = None
    for klass in go_BINARY_EXP.__mro__:
        if "arit" in klass.__dict__:
            descriptor = klass.__dict__["arit"]
            break
    assert isinstance(descriptor, property)



def test_go_arraytype_is_not_abstract():
    assert not inspect.isabstract(go_ArrayType)


def test_go_arraytype_constructor_exists():
    assert callable(go_ArrayType.__init__)


def test_go_arraytype_constructor_args():
    sig = inspect.signature(go_ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "qtd" in params, "Missing parameter 'qtd'"

def test_go_arraytype_has_qtd():
    assert hasattr(go_ArrayType, "qtd")
    descriptor = None
    for klass in go_ArrayType.__mro__:
        if "qtd" in klass.__dict__:
            descriptor = klass.__dict__["qtd"]
            break
    assert isinstance(descriptor, property)



def test_go_var_is_not_abstract():
    assert not inspect.isabstract(go_Var)


def test_go_var_constructor_exists():
    assert callable(go_Var.__init__)


def test_go_var_constructor_args():
    sig = inspect.signature(go_Var.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_go_var_has_var():
    assert hasattr(go_Var, "var")
    descriptor = None
    for klass in go_Var.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_go_signaturedel_is_not_abstract():
    assert not inspect.isabstract(go_SignatureDel)


def test_go_signaturedel_constructor_exists():
    assert callable(go_SignatureDel.__init__)


def test_go_signaturedel_constructor_args():
    sig = inspect.signature(go_SignatureDel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go_signaturedel_has_id():
    assert hasattr(go_SignatureDel, "id")
    descriptor = None
    for klass in go_SignatureDel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go_assignment_is_not_abstract():
    assert not inspect.isabstract(go_Assignment)


def test_go_assignment_constructor_exists():
    assert callable(go_Assignment.__init__)


def test_go_assignment_constructor_args():
    sig = inspect.signature(go_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "qtd" in params, "Missing parameter 'qtd'"

def test_go_assignment_has_id():
    assert hasattr(go_Assignment, "id")
    descriptor = None
    for klass in go_Assignment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_go_assignment_has_qtd():
    assert hasattr(go_Assignment, "qtd")
    descriptor = None
    for klass in go_Assignment.__mro__:
        if "qtd" in klass.__dict__:
            descriptor = klass.__dict__["qtd"]
            break
    assert isinstance(descriptor, property)



def test_go_types_is_not_abstract():
    assert not inspect.isabstract(go_Types)


def test_go_types_constructor_exists():
    assert callable(go_Types.__init__)


def test_go_types_constructor_args():
    sig = inspect.signature(go_Types.__init__)
    params = list(sig.parameters.keys())



def test_go_tipo_is_not_abstract():
    assert not inspect.isabstract(go_TIPO)


def test_go_tipo_constructor_exists():
    assert callable(go_TIPO.__init__)


def test_go_tipo_constructor_args():
    sig = inspect.signature(go_TIPO.__init__)
    params = list(sig.parameters.keys())



def test_go_arit_expr_is_not_abstract():
    assert not inspect.isabstract(go_ARIT_EXPR)


def test_go_arit_expr_constructor_exists():
    assert callable(go_ARIT_EXPR.__init__)


def test_go_arit_expr_constructor_args():
    sig = inspect.signature(go_ARIT_EXPR.__init__)
    params = list(sig.parameters.keys())
    assert "num2" in params, "Missing parameter 'num2'"
    assert "atr" in params, "Missing parameter 'atr'"
    assert "num" in params, "Missing parameter 'num'"
    assert "num1" in params, "Missing parameter 'num1'"
    assert "op" in params, "Missing parameter 'op'"

def test_go_arit_expr_has_num2():
    assert hasattr(go_ARIT_EXPR, "num2")
    descriptor = None
    for klass in go_ARIT_EXPR.__mro__:
        if "num2" in klass.__dict__:
            descriptor = klass.__dict__["num2"]
            break
    assert isinstance(descriptor, property)

def test_go_arit_expr_has_atr():
    assert hasattr(go_ARIT_EXPR, "atr")
    descriptor = None
    for klass in go_ARIT_EXPR.__mro__:
        if "atr" in klass.__dict__:
            descriptor = klass.__dict__["atr"]
            break
    assert isinstance(descriptor, property)

def test_go_arit_expr_has_num():
    assert hasattr(go_ARIT_EXPR, "num")
    descriptor = None
    for klass in go_ARIT_EXPR.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_go_arit_expr_has_num1():
    assert hasattr(go_ARIT_EXPR, "num1")
    descriptor = None
    for klass in go_ARIT_EXPR.__mro__:
        if "num1" in klass.__dict__:
            descriptor = klass.__dict__["num1"]
            break
    assert isinstance(descriptor, property)

def test_go_arit_expr_has_op():
    assert hasattr(go_ARIT_EXPR, "op")
    descriptor = None
    for klass in go_ARIT_EXPR.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_go_poststmt_is_not_abstract():
    assert not inspect.isabstract(go_PostStmt)


def test_go_poststmt_constructor_exists():
    assert callable(go_PostStmt.__init__)


def test_go_poststmt_constructor_args():
    sig = inspect.signature(go_PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_condition_is_not_abstract():
    assert not inspect.isabstract(go_Condition)


def test_go_condition_constructor_exists():
    assert callable(go_Condition.__init__)


def test_go_condition_constructor_args():
    sig = inspect.signature(go_Condition.__init__)
    params = list(sig.parameters.keys())



def test_go_initstmt_is_not_abstract():
    assert not inspect.isabstract(go_InitStmt)


def test_go_initstmt_constructor_exists():
    assert callable(go_InitStmt.__init__)


def test_go_initstmt_constructor_args():
    sig = inspect.signature(go_InitStmt.__init__)
    params = list(sig.parameters.keys())



def test_go_comparison_is_not_abstract():
    assert not inspect.isabstract(go_COMPARISON)


def test_go_comparison_constructor_exists():
    assert callable(go_COMPARISON.__init__)


def test_go_comparison_constructor_args():
    sig = inspect.signature(go_COMPARISON.__init__)
    params = list(sig.parameters.keys())
    assert "maiorque" in params, "Missing parameter 'maiorque'"
    assert "menorigualque" in params, "Missing parameter 'menorigualque'"
    assert "maiorigualque" in params, "Missing parameter 'maiorigualque'"
    assert "igual" in params, "Missing parameter 'igual'"
    assert "menorque" in params, "Missing parameter 'menorque'"

def test_go_comparison_has_maiorque():
    assert hasattr(go_COMPARISON, "maiorque")
    descriptor = None
    for klass in go_COMPARISON.__mro__:
        if "maiorque" in klass.__dict__:
            descriptor = klass.__dict__["maiorque"]
            break
    assert isinstance(descriptor, property)

def test_go_comparison_has_menorigualque():
    assert hasattr(go_COMPARISON, "menorigualque")
    descriptor = None
    for klass in go_COMPARISON.__mro__:
        if "menorigualque" in klass.__dict__:
            descriptor = klass.__dict__["menorigualque"]
            break
    assert isinstance(descriptor, property)

def test_go_comparison_has_maiorigualque():
    assert hasattr(go_COMPARISON, "maiorigualque")
    descriptor = None
    for klass in go_COMPARISON.__mro__:
        if "maiorigualque" in klass.__dict__:
            descriptor = klass.__dict__["maiorigualque"]
            break
    assert isinstance(descriptor, property)

def test_go_comparison_has_igual():
    assert hasattr(go_COMPARISON, "igual")
    descriptor = None
    for klass in go_COMPARISON.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)

def test_go_comparison_has_menorque():
    assert hasattr(go_COMPARISON, "menorque")
    descriptor = None
    for klass in go_COMPARISON.__mro__:
        if "menorque" in klass.__dict__:
            descriptor = klass.__dict__["menorque"]
            break
    assert isinstance(descriptor, property)



def test_go_expressao_is_not_abstract():
    assert not inspect.isabstract(go_EXPRESSAO)


def test_go_expressao_constructor_exists():
    assert callable(go_EXPRESSAO.__init__)


def test_go_expressao_constructor_args():
    sig = inspect.signature(go_EXPRESSAO.__init__)
    params = list(sig.parameters.keys())



def test_go_rangedecl_is_not_abstract():
    assert not inspect.isabstract(go_RangeDecl)


def test_go_rangedecl_constructor_exists():
    assert callable(go_RangeDecl.__init__)


def test_go_rangedecl_constructor_args():
    sig = inspect.signature(go_RangeDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_forclause_is_not_abstract():
    assert not inspect.isabstract(go_ForClause)


def test_go_forclause_constructor_exists():
    assert callable(go_ForClause.__init__)


def test_go_forclause_constructor_args():
    sig = inspect.signature(go_ForClause.__init__)
    params = list(sig.parameters.keys())



def test_go_fordecl_is_not_abstract():
    assert not inspect.isabstract(go_ForDecl)


def test_go_fordecl_constructor_exists():
    assert callable(go_ForDecl.__init__)


def test_go_fordecl_constructor_args():
    sig = inspect.signature(go_ForDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_expressaolinha_is_not_abstract():
    assert not inspect.isabstract(go_EXPRESSAOLINHA)


def test_go_expressaolinha_constructor_exists():
    assert callable(go_EXPRESSAOLINHA.__init__)


def test_go_expressaolinha_constructor_args():
    sig = inspect.signature(go_EXPRESSAOLINHA.__init__)
    params = list(sig.parameters.keys())



def test_go_functiontype_is_not_abstract():
    assert not inspect.isabstract(go_FunctionType)


def test_go_functiontype_constructor_exists():
    assert callable(go_FunctionType.__init__)


def test_go_functiontype_constructor_args():
    sig = inspect.signature(go_FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_go_functiontype_has_nome():
    assert hasattr(go_FunctionType, "nome")
    descriptor = None
    for klass in go_FunctionType.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_go_functioncall_is_not_abstract():
    assert not inspect.isabstract(go_FunctionCall)


def test_go_functioncall_constructor_exists():
    assert callable(go_FunctionCall.__init__)


def test_go_functioncall_constructor_args():
    sig = inspect.signature(go_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go_functioncall_has_id():
    assert hasattr(go_FunctionCall, "id")
    descriptor = None
    for klass in go_FunctionCall.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go_varcall_is_not_abstract():
    assert not inspect.isabstract(go_VarCall)


def test_go_varcall_constructor_exists():
    assert callable(go_VarCall.__init__)


def test_go_varcall_constructor_args():
    sig = inspect.signature(go_VarCall.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go_varcall_has_id():
    assert hasattr(go_VarCall, "id")
    descriptor = None
    for klass in go_VarCall.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go_pontosigual_is_not_abstract():
    assert not inspect.isabstract(go_PONTOSIGUAL)


def test_go_pontosigual_constructor_exists():
    assert callable(go_PONTOSIGUAL.__init__)


def test_go_pontosigual_constructor_args():
    sig = inspect.signature(go_PONTOSIGUAL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_go_pontosigual_has_op():
    assert hasattr(go_PONTOSIGUAL, "op")
    descriptor = None
    for klass in go_PONTOSIGUAL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_go_igual_is_not_abstract():
    assert not inspect.isabstract(go_IGUAL)


def test_go_igual_constructor_exists():
    assert callable(go_IGUAL.__init__)


def test_go_igual_constructor_args():
    sig = inspect.signature(go_IGUAL.__init__)
    params = list(sig.parameters.keys())
    assert "igual" in params, "Missing parameter 'igual'"

def test_go_igual_has_igual():
    assert hasattr(go_IGUAL, "igual")
    descriptor = None
    for klass in go_IGUAL.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)



def test_go_idlist_is_not_abstract():
    assert not inspect.isabstract(go_IDList)


def test_go_idlist_constructor_exists():
    assert callable(go_IDList.__init__)


def test_go_idlist_constructor_args():
    sig = inspect.signature(go_IDList.__init__)
    params = list(sig.parameters.keys())
    assert "vir" in params, "Missing parameter 'vir'"
    assert "idList" in params, "Missing parameter 'idList'"

def test_go_idlist_has_vir():
    assert hasattr(go_IDList, "vir")
    descriptor = None
    for klass in go_IDList.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)

def test_go_idlist_has_idList():
    assert hasattr(go_IDList, "idList")
    descriptor = None
    for klass in go_IDList.__mro__:
        if "idList" in klass.__dict__:
            descriptor = klass.__dict__["idList"]
            break
    assert isinstance(descriptor, property)



def test_go_vardecl_is_not_abstract():
    assert not inspect.isabstract(go_VarDecl)


def test_go_vardecl_constructor_exists():
    assert callable(go_VarDecl.__init__)


def test_go_vardecl_constructor_args():
    sig = inspect.signature(go_VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_boolean_value_is_not_abstract():
    assert not inspect.isabstract(go_BOOLEAN_VALUE)


def test_go_boolean_value_constructor_exists():
    assert callable(go_BOOLEAN_VALUE.__init__)


def test_go_boolean_value_constructor_args():
    sig = inspect.signature(go_BOOLEAN_VALUE.__init__)
    params = list(sig.parameters.keys())
    assert "falso" in params, "Missing parameter 'falso'"
    assert "verdadeiro" in params, "Missing parameter 'verdadeiro'"

def test_go_boolean_value_has_falso():
    assert hasattr(go_BOOLEAN_VALUE, "falso")
    descriptor = None
    for klass in go_BOOLEAN_VALUE.__mro__:
        if "falso" in klass.__dict__:
            descriptor = klass.__dict__["falso"]
            break
    assert isinstance(descriptor, property)

def test_go_boolean_value_has_verdadeiro():
    assert hasattr(go_BOOLEAN_VALUE, "verdadeiro")
    descriptor = None
    for klass in go_BOOLEAN_VALUE.__mro__:
        if "verdadeiro" in klass.__dict__:
            descriptor = klass.__dict__["verdadeiro"]
            break
    assert isinstance(descriptor, property)



def test_go_godecl_is_not_abstract():
    assert not inspect.isabstract(go_GoDecl)


def test_go_godecl_constructor_exists():
    assert callable(go_GoDecl.__init__)


def test_go_godecl_constructor_args():
    sig = inspect.signature(go_GoDecl.__init__)
    params = list(sig.parameters.keys())



def test_go_init_is_not_abstract():
    assert not inspect.isabstract(go_Init)


def test_go_init_constructor_exists():
    assert callable(go_Init.__init__)


def test_go_init_constructor_args():
    sig = inspect.signature(go_Init.__init__)
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
go_ElseCondition_strategy = st.builds(
    go_ElseCondition,
)
go_ElseIfCondition_strategy = st.builds(
    go_ElseIfCondition,
)
go_BasicType_strategy = st.builds(
    go_BasicType,
    int=
        safe_text,
    boolean=
        safe_text,
    string=
        safe_text,
    float=
        safe_text
)
go_PARAMETER_strategy = st.builds(
    go_PARAMETER,
    id=
        safe_text
)
go_BOOL_OP_strategy = st.builds(
    go_BOOL_OP,
)
ElseIfCondition_strategy = st.builds(
    ElseIfCondition,
)
go_IfCondition_strategy = st.builds(
    go_IfCondition,
)
go_PARAMETERS_LIST_strategy = st.builds(
    go_PARAMETERS_LIST,
    vir=
        safe_text
)
go_Parameters_strategy = st.builds(
    go_Parameters,
)
go_BLOCK_strategy = st.builds(
    go_BLOCK,
)
go_Signature_strategy = st.builds(
    go_Signature,
)
go_ReturnStmt_strategy = st.builds(
    go_ReturnStmt,
)
go_IfStmt_strategy = st.builds(
    go_IfStmt,
)
go_Chamada_strategy = st.builds(
    go_Chamada,
)
go_ArrayValue_strategy = st.builds(
    go_ArrayValue,
)
go_EObject_strategy = st.builds(
    go_EObject,
)
go_LiteraisList_strategy = st.builds(
    go_LiteraisList,
    vir=
        safe_text
)
go_Const_strategy = st.builds(
    go_Const,
    const=
        safe_text
)
go_LITERAIS_BASICOS_strategy = st.builds(
    go_LITERAIS_BASICOS,
    numero=
        safe_text,
    string=
        safe_text
)
go_BINARY_EXP_strategy = st.builds(
    go_BINARY_EXP,
    arit=
        safe_text
)
go_ArrayType_strategy = st.builds(
    go_ArrayType,
    qtd=
        safe_text
)
go_Var_strategy = st.builds(
    go_Var,
    var=
        safe_text
)
go_SignatureDel_strategy = st.builds(
    go_SignatureDel,
    id=
        safe_text
)
go_Assignment_strategy = st.builds(
    go_Assignment,
    id=
        safe_text,
    qtd=
        safe_text
)
go_Types_strategy = st.builds(
    go_Types,
)
go_TIPO_strategy = st.builds(
    go_TIPO,
)
go_ARIT_EXPR_strategy = st.builds(
    go_ARIT_EXPR,
    num2=
        safe_text,
    atr=
        safe_text,
    num=
        safe_text,
    num1=
        safe_text,
    op=
        safe_text
)
go_PostStmt_strategy = st.builds(
    go_PostStmt,
)
go_Condition_strategy = st.builds(
    go_Condition,
)
go_InitStmt_strategy = st.builds(
    go_InitStmt,
)
go_COMPARISON_strategy = st.builds(
    go_COMPARISON,
    maiorque=
        safe_text,
    menorigualque=
        safe_text,
    maiorigualque=
        safe_text,
    igual=
        safe_text,
    menorque=
        safe_text
)
go_EXPRESSAO_strategy = st.builds(
    go_EXPRESSAO,
)
go_RangeDecl_strategy = st.builds(
    go_RangeDecl,
)
go_ForClause_strategy = st.builds(
    go_ForClause,
)
go_ForDecl_strategy = st.builds(
    go_ForDecl,
)
go_EXPRESSAOLINHA_strategy = st.builds(
    go_EXPRESSAOLINHA,
)
go_FunctionType_strategy = st.builds(
    go_FunctionType,
    nome=
        safe_text
)
go_FunctionCall_strategy = st.builds(
    go_FunctionCall,
    id=
        safe_text
)
go_VarCall_strategy = st.builds(
    go_VarCall,
    id=
        safe_text
)
go_PONTOSIGUAL_strategy = st.builds(
    go_PONTOSIGUAL,
    op=
        safe_text
)
go_IGUAL_strategy = st.builds(
    go_IGUAL,
    igual=
        safe_text
)
go_IDList_strategy = st.builds(
    go_IDList,
    vir=
        safe_text,
    idList=
        safe_text
)
go_VarDecl_strategy = st.builds(
    go_VarDecl,
)
go_BOOLEAN_VALUE_strategy = st.builds(
    go_BOOLEAN_VALUE,
    falso=
        safe_text,
    verdadeiro=
        safe_text
)
go_GoDecl_strategy = st.builds(
    go_GoDecl,
)
go_Init_strategy = st.builds(
    go_Init,
)

@given(instance=go_ElseCondition_strategy)
@settings(max_examples=50)
def test_go_elsecondition_instantiation(instance):
    assert isinstance(instance, go_ElseCondition)

@given(instance=go_ElseIfCondition_strategy)
@settings(max_examples=50)
def test_go_elseifcondition_instantiation(instance):
    assert isinstance(instance, go_ElseIfCondition)

@given(instance=go_BasicType_strategy)
@settings(max_examples=50)
def test_go_basictype_instantiation(instance):
    assert isinstance(instance, go_BasicType)



@given(instance=go_BasicType_strategy)
def test_go_basictype_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original



@given(instance=go_BasicType_strategy)
def test_go_basictype_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original



@given(instance=go_BasicType_strategy)
def test_go_basictype_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=go_BasicType_strategy)
def test_go_basictype_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=go_PARAMETER_strategy)
@settings(max_examples=50)
def test_go_parameter_instantiation(instance):
    assert isinstance(instance, go_PARAMETER)



@given(instance=go_PARAMETER_strategy)
def test_go_parameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go_BOOL_OP_strategy)
@settings(max_examples=50)
def test_go_bool_op_instantiation(instance):
    assert isinstance(instance, go_BOOL_OP)

@given(instance=ElseIfCondition_strategy)
@settings(max_examples=50)
def test_elseifcondition_instantiation(instance):
    assert isinstance(instance, ElseIfCondition)

@given(instance=go_IfCondition_strategy)
@settings(max_examples=50)
def test_go_ifcondition_instantiation(instance):
    assert isinstance(instance, go_IfCondition)

@given(instance=go_PARAMETERS_LIST_strategy)
@settings(max_examples=50)
def test_go_parameters_list_instantiation(instance):
    assert isinstance(instance, go_PARAMETERS_LIST)



@given(instance=go_PARAMETERS_LIST_strategy)
def test_go_parameters_list_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original

@given(instance=go_Parameters_strategy)
@settings(max_examples=50)
def test_go_parameters_instantiation(instance):
    assert isinstance(instance, go_Parameters)

@given(instance=go_BLOCK_strategy)
@settings(max_examples=50)
def test_go_block_instantiation(instance):
    assert isinstance(instance, go_BLOCK)

@given(instance=go_Signature_strategy)
@settings(max_examples=50)
def test_go_signature_instantiation(instance):
    assert isinstance(instance, go_Signature)

@given(instance=go_ReturnStmt_strategy)
@settings(max_examples=50)
def test_go_returnstmt_instantiation(instance):
    assert isinstance(instance, go_ReturnStmt)

@given(instance=go_IfStmt_strategy)
@settings(max_examples=50)
def test_go_ifstmt_instantiation(instance):
    assert isinstance(instance, go_IfStmt)

@given(instance=go_Chamada_strategy)
@settings(max_examples=50)
def test_go_chamada_instantiation(instance):
    assert isinstance(instance, go_Chamada)

@given(instance=go_ArrayValue_strategy)
@settings(max_examples=50)
def test_go_arrayvalue_instantiation(instance):
    assert isinstance(instance, go_ArrayValue)

@given(instance=go_EObject_strategy)
@settings(max_examples=50)
def test_go_eobject_instantiation(instance):
    assert isinstance(instance, go_EObject)

@given(instance=go_LiteraisList_strategy)
@settings(max_examples=50)
def test_go_literaislist_instantiation(instance):
    assert isinstance(instance, go_LiteraisList)



@given(instance=go_LiteraisList_strategy)
def test_go_literaislist_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original

@given(instance=go_Const_strategy)
@settings(max_examples=50)
def test_go_const_instantiation(instance):
    assert isinstance(instance, go_Const)



@given(instance=go_Const_strategy)
def test_go_const_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=go_LITERAIS_BASICOS_strategy)
@settings(max_examples=50)
def test_go_literais_basicos_instantiation(instance):
    assert isinstance(instance, go_LITERAIS_BASICOS)



@given(instance=go_LITERAIS_BASICOS_strategy)
def test_go_literais_basicos_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original



@given(instance=go_LITERAIS_BASICOS_strategy)
def test_go_literais_basicos_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=go_BINARY_EXP_strategy)
@settings(max_examples=50)
def test_go_binary_exp_instantiation(instance):
    assert isinstance(instance, go_BINARY_EXP)



@given(instance=go_BINARY_EXP_strategy)
def test_go_binary_exp_arit_setter(instance):
    original = instance.arit
    instance.arit = original
    assert instance.arit == original

@given(instance=go_ArrayType_strategy)
@settings(max_examples=50)
def test_go_arraytype_instantiation(instance):
    assert isinstance(instance, go_ArrayType)



@given(instance=go_ArrayType_strategy)
def test_go_arraytype_qtd_setter(instance):
    original = instance.qtd
    instance.qtd = original
    assert instance.qtd == original

@given(instance=go_Var_strategy)
@settings(max_examples=50)
def test_go_var_instantiation(instance):
    assert isinstance(instance, go_Var)



@given(instance=go_Var_strategy)
def test_go_var_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=go_SignatureDel_strategy)
@settings(max_examples=50)
def test_go_signaturedel_instantiation(instance):
    assert isinstance(instance, go_SignatureDel)



@given(instance=go_SignatureDel_strategy)
def test_go_signaturedel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go_Assignment_strategy)
@settings(max_examples=50)
def test_go_assignment_instantiation(instance):
    assert isinstance(instance, go_Assignment)



@given(instance=go_Assignment_strategy)
def test_go_assignment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=go_Assignment_strategy)
def test_go_assignment_qtd_setter(instance):
    original = instance.qtd
    instance.qtd = original
    assert instance.qtd == original

@given(instance=go_Types_strategy)
@settings(max_examples=50)
def test_go_types_instantiation(instance):
    assert isinstance(instance, go_Types)

@given(instance=go_TIPO_strategy)
@settings(max_examples=50)
def test_go_tipo_instantiation(instance):
    assert isinstance(instance, go_TIPO)

@given(instance=go_ARIT_EXPR_strategy)
@settings(max_examples=50)
def test_go_arit_expr_instantiation(instance):
    assert isinstance(instance, go_ARIT_EXPR)



@given(instance=go_ARIT_EXPR_strategy)
def test_go_arit_expr_num2_setter(instance):
    original = instance.num2
    instance.num2 = original
    assert instance.num2 == original



@given(instance=go_ARIT_EXPR_strategy)
def test_go_arit_expr_atr_setter(instance):
    original = instance.atr
    instance.atr = original
    assert instance.atr == original



@given(instance=go_ARIT_EXPR_strategy)
def test_go_arit_expr_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=go_ARIT_EXPR_strategy)
def test_go_arit_expr_num1_setter(instance):
    original = instance.num1
    instance.num1 = original
    assert instance.num1 == original



@given(instance=go_ARIT_EXPR_strategy)
def test_go_arit_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=go_PostStmt_strategy)
@settings(max_examples=50)
def test_go_poststmt_instantiation(instance):
    assert isinstance(instance, go_PostStmt)

@given(instance=go_Condition_strategy)
@settings(max_examples=50)
def test_go_condition_instantiation(instance):
    assert isinstance(instance, go_Condition)

@given(instance=go_InitStmt_strategy)
@settings(max_examples=50)
def test_go_initstmt_instantiation(instance):
    assert isinstance(instance, go_InitStmt)

@given(instance=go_COMPARISON_strategy)
@settings(max_examples=50)
def test_go_comparison_instantiation(instance):
    assert isinstance(instance, go_COMPARISON)



@given(instance=go_COMPARISON_strategy)
def test_go_comparison_maiorque_setter(instance):
    original = instance.maiorque
    instance.maiorque = original
    assert instance.maiorque == original



@given(instance=go_COMPARISON_strategy)
def test_go_comparison_menorigualque_setter(instance):
    original = instance.menorigualque
    instance.menorigualque = original
    assert instance.menorigualque == original



@given(instance=go_COMPARISON_strategy)
def test_go_comparison_maiorigualque_setter(instance):
    original = instance.maiorigualque
    instance.maiorigualque = original
    assert instance.maiorigualque == original



@given(instance=go_COMPARISON_strategy)
def test_go_comparison_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original



@given(instance=go_COMPARISON_strategy)
def test_go_comparison_menorque_setter(instance):
    original = instance.menorque
    instance.menorque = original
    assert instance.menorque == original

@given(instance=go_EXPRESSAO_strategy)
@settings(max_examples=50)
def test_go_expressao_instantiation(instance):
    assert isinstance(instance, go_EXPRESSAO)

@given(instance=go_RangeDecl_strategy)
@settings(max_examples=50)
def test_go_rangedecl_instantiation(instance):
    assert isinstance(instance, go_RangeDecl)

@given(instance=go_ForClause_strategy)
@settings(max_examples=50)
def test_go_forclause_instantiation(instance):
    assert isinstance(instance, go_ForClause)

@given(instance=go_ForDecl_strategy)
@settings(max_examples=50)
def test_go_fordecl_instantiation(instance):
    assert isinstance(instance, go_ForDecl)

@given(instance=go_EXPRESSAOLINHA_strategy)
@settings(max_examples=50)
def test_go_expressaolinha_instantiation(instance):
    assert isinstance(instance, go_EXPRESSAOLINHA)

@given(instance=go_FunctionType_strategy)
@settings(max_examples=50)
def test_go_functiontype_instantiation(instance):
    assert isinstance(instance, go_FunctionType)



@given(instance=go_FunctionType_strategy)
def test_go_functiontype_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=go_FunctionCall_strategy)
@settings(max_examples=50)
def test_go_functioncall_instantiation(instance):
    assert isinstance(instance, go_FunctionCall)



@given(instance=go_FunctionCall_strategy)
def test_go_functioncall_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go_VarCall_strategy)
@settings(max_examples=50)
def test_go_varcall_instantiation(instance):
    assert isinstance(instance, go_VarCall)



@given(instance=go_VarCall_strategy)
def test_go_varcall_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go_PONTOSIGUAL_strategy)
@settings(max_examples=50)
def test_go_pontosigual_instantiation(instance):
    assert isinstance(instance, go_PONTOSIGUAL)



@given(instance=go_PONTOSIGUAL_strategy)
def test_go_pontosigual_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=go_IGUAL_strategy)
@settings(max_examples=50)
def test_go_igual_instantiation(instance):
    assert isinstance(instance, go_IGUAL)



@given(instance=go_IGUAL_strategy)
def test_go_igual_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original

@given(instance=go_IDList_strategy)
@settings(max_examples=50)
def test_go_idlist_instantiation(instance):
    assert isinstance(instance, go_IDList)



@given(instance=go_IDList_strategy)
def test_go_idlist_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original



@given(instance=go_IDList_strategy)
def test_go_idlist_idList_setter(instance):
    original = instance.idList
    instance.idList = original
    assert instance.idList == original

@given(instance=go_VarDecl_strategy)
@settings(max_examples=50)
def test_go_vardecl_instantiation(instance):
    assert isinstance(instance, go_VarDecl)

@given(instance=go_BOOLEAN_VALUE_strategy)
@settings(max_examples=50)
def test_go_boolean_value_instantiation(instance):
    assert isinstance(instance, go_BOOLEAN_VALUE)



@given(instance=go_BOOLEAN_VALUE_strategy)
def test_go_boolean_value_falso_setter(instance):
    original = instance.falso
    instance.falso = original
    assert instance.falso == original



@given(instance=go_BOOLEAN_VALUE_strategy)
def test_go_boolean_value_verdadeiro_setter(instance):
    original = instance.verdadeiro
    instance.verdadeiro = original
    assert instance.verdadeiro == original

@given(instance=go_GoDecl_strategy)
@settings(max_examples=50)
def test_go_godecl_instantiation(instance):
    assert isinstance(instance, go_GoDecl)

@given(instance=go_Init_strategy)
@settings(max_examples=50)
def test_go_init_instantiation(instance):
    assert isinstance(instance, go_Init)
