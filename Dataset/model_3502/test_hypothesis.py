import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    go::ElseCondition,
    go::ElseIfCondition,
    go::BasicType,
    go::PARAMETER,
    go::BOOL::OP,
    ElseIfCondition,
    go::IfCondition,
    go::PARAMETERS::LIST,
    go::Parameters,
    go::BLOCK,
    go::Signature,
    go::ReturnStmt,
    go::IfStmt,
    go::Chamada,
    go::ArrayValue,
    go::EObject,
    go::LiteraisList,
    go::Const,
    go::LITERAIS::BASICOS,
    go::BINARY::EXP,
    go::ArrayType,
    go::Var,
    go::SignatureDel,
    go::Assignment,
    go::Types,
    go::TIPO,
    go::ARIT::EXPR,
    go::PostStmt,
    go::Condition,
    go::InitStmt,
    go::COMPARISON,
    go::EXPRESSAO,
    go::RangeDecl,
    go::ForClause,
    go::ForDecl,
    go::EXPRESSAOLINHA,
    go::FunctionType,
    go::FunctionCall,
    go::VarCall,
    go::PONTOSIGUAL,
    go::IGUAL,
    go::IDList,
    go::VarDecl,
    go::BOOLEAN::VALUE,
    go::GoDecl,
    go::Init,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_go::elsecondition_is_not_abstract():
    assert not inspect.isabstract(go::ElseCondition)


def test_go::elsecondition_constructor_exists():
    assert callable(go::ElseCondition.__init__)


def test_go::elsecondition_constructor_args():
    sig = inspect.signature(go::ElseCondition.__init__)
    params = list(sig.parameters.keys())



def test_go::elseifcondition_is_not_abstract():
    assert not inspect.isabstract(go::ElseIfCondition)


def test_go::elseifcondition_constructor_exists():
    assert callable(go::ElseIfCondition.__init__)


def test_go::elseifcondition_constructor_args():
    sig = inspect.signature(go::ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go::basictype_is_not_abstract():
    assert not inspect.isabstract(go::BasicType)


def test_go::basictype_constructor_exists():
    assert callable(go::BasicType.__init__)


def test_go::basictype_constructor_args():
    sig = inspect.signature(go::BasicType.__init__)
    params = list(sig.parameters.keys())
    assert "float" in params, "Missing parameter 'float'"
    assert "boolean" in params, "Missing parameter 'boolean'"
    assert "string" in params, "Missing parameter 'string'"
    assert "int" in params, "Missing parameter 'int'"

def test_go::basictype_has_float():
    assert hasattr(go::BasicType, "float")
    descriptor = None
    for klass in go::BasicType.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_go::basictype_has_boolean():
    assert hasattr(go::BasicType, "boolean")
    descriptor = None
    for klass in go::BasicType.__mro__:
        if "boolean" in klass.__dict__:
            descriptor = klass.__dict__["boolean"]
            break
    assert isinstance(descriptor, property)

def test_go::basictype_has_string():
    assert hasattr(go::BasicType, "string")
    descriptor = None
    for klass in go::BasicType.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_go::basictype_has_int():
    assert hasattr(go::BasicType, "int")
    descriptor = None
    for klass in go::BasicType.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_go::parameter_is_not_abstract():
    assert not inspect.isabstract(go::PARAMETER)


def test_go::parameter_constructor_exists():
    assert callable(go::PARAMETER.__init__)


def test_go::parameter_constructor_args():
    sig = inspect.signature(go::PARAMETER.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go::parameter_has_id():
    assert hasattr(go::PARAMETER, "id")
    descriptor = None
    for klass in go::PARAMETER.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go::bool::op_is_not_abstract():
    assert not inspect.isabstract(go::BOOL::OP)


def test_go::bool::op_constructor_exists():
    assert callable(go::BOOL::OP.__init__)


def test_go::bool::op_constructor_args():
    sig = inspect.signature(go::BOOL::OP.__init__)
    params = list(sig.parameters.keys())



def test_elseifcondition_is_not_abstract():
    assert not inspect.isabstract(ElseIfCondition)


def test_elseifcondition_constructor_exists():
    assert callable(ElseIfCondition.__init__)


def test_elseifcondition_constructor_args():
    sig = inspect.signature(ElseIfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go::ifcondition_is_not_abstract():
    assert not inspect.isabstract(go::IfCondition)


def test_go::ifcondition_constructor_exists():
    assert callable(go::IfCondition.__init__)


def test_go::ifcondition_constructor_args():
    sig = inspect.signature(go::IfCondition.__init__)
    params = list(sig.parameters.keys())



def test_go::parameters::list_is_not_abstract():
    assert not inspect.isabstract(go::PARAMETERS::LIST)


def test_go::parameters::list_constructor_exists():
    assert callable(go::PARAMETERS::LIST.__init__)


def test_go::parameters::list_constructor_args():
    sig = inspect.signature(go::PARAMETERS::LIST.__init__)
    params = list(sig.parameters.keys())
    assert "vir" in params, "Missing parameter 'vir'"

def test_go::parameters::list_has_vir():
    assert hasattr(go::PARAMETERS::LIST, "vir")
    descriptor = None
    for klass in go::PARAMETERS::LIST.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)



def test_go::parameters_is_not_abstract():
    assert not inspect.isabstract(go::Parameters)


def test_go::parameters_constructor_exists():
    assert callable(go::Parameters.__init__)


def test_go::parameters_constructor_args():
    sig = inspect.signature(go::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_go::block_is_not_abstract():
    assert not inspect.isabstract(go::BLOCK)


def test_go::block_constructor_exists():
    assert callable(go::BLOCK.__init__)


def test_go::block_constructor_args():
    sig = inspect.signature(go::BLOCK.__init__)
    params = list(sig.parameters.keys())



def test_go::signature_is_not_abstract():
    assert not inspect.isabstract(go::Signature)


def test_go::signature_constructor_exists():
    assert callable(go::Signature.__init__)


def test_go::signature_constructor_args():
    sig = inspect.signature(go::Signature.__init__)
    params = list(sig.parameters.keys())



def test_go::returnstmt_is_not_abstract():
    assert not inspect.isabstract(go::ReturnStmt)


def test_go::returnstmt_constructor_exists():
    assert callable(go::ReturnStmt.__init__)


def test_go::returnstmt_constructor_args():
    sig = inspect.signature(go::ReturnStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::ifstmt_is_not_abstract():
    assert not inspect.isabstract(go::IfStmt)


def test_go::ifstmt_constructor_exists():
    assert callable(go::IfStmt.__init__)


def test_go::ifstmt_constructor_args():
    sig = inspect.signature(go::IfStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::chamada_is_not_abstract():
    assert not inspect.isabstract(go::Chamada)


def test_go::chamada_constructor_exists():
    assert callable(go::Chamada.__init__)


def test_go::chamada_constructor_args():
    sig = inspect.signature(go::Chamada.__init__)
    params = list(sig.parameters.keys())



def test_go::arrayvalue_is_not_abstract():
    assert not inspect.isabstract(go::ArrayValue)


def test_go::arrayvalue_constructor_exists():
    assert callable(go::ArrayValue.__init__)


def test_go::arrayvalue_constructor_args():
    sig = inspect.signature(go::ArrayValue.__init__)
    params = list(sig.parameters.keys())



def test_go::eobject_is_not_abstract():
    assert not inspect.isabstract(go::EObject)


def test_go::eobject_constructor_exists():
    assert callable(go::EObject.__init__)


def test_go::eobject_constructor_args():
    sig = inspect.signature(go::EObject.__init__)
    params = list(sig.parameters.keys())



def test_go::literaislist_is_not_abstract():
    assert not inspect.isabstract(go::LiteraisList)


def test_go::literaislist_constructor_exists():
    assert callable(go::LiteraisList.__init__)


def test_go::literaislist_constructor_args():
    sig = inspect.signature(go::LiteraisList.__init__)
    params = list(sig.parameters.keys())
    assert "vir" in params, "Missing parameter 'vir'"

def test_go::literaislist_has_vir():
    assert hasattr(go::LiteraisList, "vir")
    descriptor = None
    for klass in go::LiteraisList.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)



def test_go::const_is_not_abstract():
    assert not inspect.isabstract(go::Const)


def test_go::const_constructor_exists():
    assert callable(go::Const.__init__)


def test_go::const_constructor_args():
    sig = inspect.signature(go::Const.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"

def test_go::const_has_const():
    assert hasattr(go::Const, "const")
    descriptor = None
    for klass in go::Const.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_go::literais::basicos_is_not_abstract():
    assert not inspect.isabstract(go::LITERAIS::BASICOS)


def test_go::literais::basicos_constructor_exists():
    assert callable(go::LITERAIS::BASICOS.__init__)


def test_go::literais::basicos_constructor_args():
    sig = inspect.signature(go::LITERAIS::BASICOS.__init__)
    params = list(sig.parameters.keys())
    assert "numero" in params, "Missing parameter 'numero'"
    assert "string" in params, "Missing parameter 'string'"

def test_go::literais::basicos_has_numero():
    assert hasattr(go::LITERAIS::BASICOS, "numero")
    descriptor = None
    for klass in go::LITERAIS::BASICOS.__mro__:
        if "numero" in klass.__dict__:
            descriptor = klass.__dict__["numero"]
            break
    assert isinstance(descriptor, property)

def test_go::literais::basicos_has_string():
    assert hasattr(go::LITERAIS::BASICOS, "string")
    descriptor = None
    for klass in go::LITERAIS::BASICOS.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_go::binary::exp_is_not_abstract():
    assert not inspect.isabstract(go::BINARY::EXP)


def test_go::binary::exp_constructor_exists():
    assert callable(go::BINARY::EXP.__init__)


def test_go::binary::exp_constructor_args():
    sig = inspect.signature(go::BINARY::EXP.__init__)
    params = list(sig.parameters.keys())
    assert "arit" in params, "Missing parameter 'arit'"

def test_go::binary::exp_has_arit():
    assert hasattr(go::BINARY::EXP, "arit")
    descriptor = None
    for klass in go::BINARY::EXP.__mro__:
        if "arit" in klass.__dict__:
            descriptor = klass.__dict__["arit"]
            break
    assert isinstance(descriptor, property)



def test_go::arraytype_is_not_abstract():
    assert not inspect.isabstract(go::ArrayType)


def test_go::arraytype_constructor_exists():
    assert callable(go::ArrayType.__init__)


def test_go::arraytype_constructor_args():
    sig = inspect.signature(go::ArrayType.__init__)
    params = list(sig.parameters.keys())
    assert "qtd" in params, "Missing parameter 'qtd'"

def test_go::arraytype_has_qtd():
    assert hasattr(go::ArrayType, "qtd")
    descriptor = None
    for klass in go::ArrayType.__mro__:
        if "qtd" in klass.__dict__:
            descriptor = klass.__dict__["qtd"]
            break
    assert isinstance(descriptor, property)



def test_go::var_is_not_abstract():
    assert not inspect.isabstract(go::Var)


def test_go::var_constructor_exists():
    assert callable(go::Var.__init__)


def test_go::var_constructor_args():
    sig = inspect.signature(go::Var.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_go::var_has_var():
    assert hasattr(go::Var, "var")
    descriptor = None
    for klass in go::Var.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_go::signaturedel_is_not_abstract():
    assert not inspect.isabstract(go::SignatureDel)


def test_go::signaturedel_constructor_exists():
    assert callable(go::SignatureDel.__init__)


def test_go::signaturedel_constructor_args():
    sig = inspect.signature(go::SignatureDel.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go::signaturedel_has_id():
    assert hasattr(go::SignatureDel, "id")
    descriptor = None
    for klass in go::SignatureDel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go::assignment_is_not_abstract():
    assert not inspect.isabstract(go::Assignment)


def test_go::assignment_constructor_exists():
    assert callable(go::Assignment.__init__)


def test_go::assignment_constructor_args():
    sig = inspect.signature(go::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "qtd" in params, "Missing parameter 'qtd'"

def test_go::assignment_has_id():
    assert hasattr(go::Assignment, "id")
    descriptor = None
    for klass in go::Assignment.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_go::assignment_has_qtd():
    assert hasattr(go::Assignment, "qtd")
    descriptor = None
    for klass in go::Assignment.__mro__:
        if "qtd" in klass.__dict__:
            descriptor = klass.__dict__["qtd"]
            break
    assert isinstance(descriptor, property)



def test_go::types_is_not_abstract():
    assert not inspect.isabstract(go::Types)


def test_go::types_constructor_exists():
    assert callable(go::Types.__init__)


def test_go::types_constructor_args():
    sig = inspect.signature(go::Types.__init__)
    params = list(sig.parameters.keys())



def test_go::tipo_is_not_abstract():
    assert not inspect.isabstract(go::TIPO)


def test_go::tipo_constructor_exists():
    assert callable(go::TIPO.__init__)


def test_go::tipo_constructor_args():
    sig = inspect.signature(go::TIPO.__init__)
    params = list(sig.parameters.keys())



def test_go::arit::expr_is_not_abstract():
    assert not inspect.isabstract(go::ARIT::EXPR)


def test_go::arit::expr_constructor_exists():
    assert callable(go::ARIT::EXPR.__init__)


def test_go::arit::expr_constructor_args():
    sig = inspect.signature(go::ARIT::EXPR.__init__)
    params = list(sig.parameters.keys())
    assert "atr" in params, "Missing parameter 'atr'"
    assert "num1" in params, "Missing parameter 'num1'"
    assert "num" in params, "Missing parameter 'num'"
    assert "op" in params, "Missing parameter 'op'"
    assert "num2" in params, "Missing parameter 'num2'"

def test_go::arit::expr_has_atr():
    assert hasattr(go::ARIT::EXPR, "atr")
    descriptor = None
    for klass in go::ARIT::EXPR.__mro__:
        if "atr" in klass.__dict__:
            descriptor = klass.__dict__["atr"]
            break
    assert isinstance(descriptor, property)

def test_go::arit::expr_has_num1():
    assert hasattr(go::ARIT::EXPR, "num1")
    descriptor = None
    for klass in go::ARIT::EXPR.__mro__:
        if "num1" in klass.__dict__:
            descriptor = klass.__dict__["num1"]
            break
    assert isinstance(descriptor, property)

def test_go::arit::expr_has_num():
    assert hasattr(go::ARIT::EXPR, "num")
    descriptor = None
    for klass in go::ARIT::EXPR.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_go::arit::expr_has_op():
    assert hasattr(go::ARIT::EXPR, "op")
    descriptor = None
    for klass in go::ARIT::EXPR.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_go::arit::expr_has_num2():
    assert hasattr(go::ARIT::EXPR, "num2")
    descriptor = None
    for klass in go::ARIT::EXPR.__mro__:
        if "num2" in klass.__dict__:
            descriptor = klass.__dict__["num2"]
            break
    assert isinstance(descriptor, property)



def test_go::poststmt_is_not_abstract():
    assert not inspect.isabstract(go::PostStmt)


def test_go::poststmt_constructor_exists():
    assert callable(go::PostStmt.__init__)


def test_go::poststmt_constructor_args():
    sig = inspect.signature(go::PostStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::condition_is_not_abstract():
    assert not inspect.isabstract(go::Condition)


def test_go::condition_constructor_exists():
    assert callable(go::Condition.__init__)


def test_go::condition_constructor_args():
    sig = inspect.signature(go::Condition.__init__)
    params = list(sig.parameters.keys())



def test_go::initstmt_is_not_abstract():
    assert not inspect.isabstract(go::InitStmt)


def test_go::initstmt_constructor_exists():
    assert callable(go::InitStmt.__init__)


def test_go::initstmt_constructor_args():
    sig = inspect.signature(go::InitStmt.__init__)
    params = list(sig.parameters.keys())



def test_go::comparison_is_not_abstract():
    assert not inspect.isabstract(go::COMPARISON)


def test_go::comparison_constructor_exists():
    assert callable(go::COMPARISON.__init__)


def test_go::comparison_constructor_args():
    sig = inspect.signature(go::COMPARISON.__init__)
    params = list(sig.parameters.keys())
    assert "maiorigualque" in params, "Missing parameter 'maiorigualque'"
    assert "igual" in params, "Missing parameter 'igual'"
    assert "maiorque" in params, "Missing parameter 'maiorque'"
    assert "menorque" in params, "Missing parameter 'menorque'"
    assert "menorigualque" in params, "Missing parameter 'menorigualque'"

def test_go::comparison_has_maiorigualque():
    assert hasattr(go::COMPARISON, "maiorigualque")
    descriptor = None
    for klass in go::COMPARISON.__mro__:
        if "maiorigualque" in klass.__dict__:
            descriptor = klass.__dict__["maiorigualque"]
            break
    assert isinstance(descriptor, property)

def test_go::comparison_has_igual():
    assert hasattr(go::COMPARISON, "igual")
    descriptor = None
    for klass in go::COMPARISON.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)

def test_go::comparison_has_maiorque():
    assert hasattr(go::COMPARISON, "maiorque")
    descriptor = None
    for klass in go::COMPARISON.__mro__:
        if "maiorque" in klass.__dict__:
            descriptor = klass.__dict__["maiorque"]
            break
    assert isinstance(descriptor, property)

def test_go::comparison_has_menorque():
    assert hasattr(go::COMPARISON, "menorque")
    descriptor = None
    for klass in go::COMPARISON.__mro__:
        if "menorque" in klass.__dict__:
            descriptor = klass.__dict__["menorque"]
            break
    assert isinstance(descriptor, property)

def test_go::comparison_has_menorigualque():
    assert hasattr(go::COMPARISON, "menorigualque")
    descriptor = None
    for klass in go::COMPARISON.__mro__:
        if "menorigualque" in klass.__dict__:
            descriptor = klass.__dict__["menorigualque"]
            break
    assert isinstance(descriptor, property)



def test_go::expressao_is_not_abstract():
    assert not inspect.isabstract(go::EXPRESSAO)


def test_go::expressao_constructor_exists():
    assert callable(go::EXPRESSAO.__init__)


def test_go::expressao_constructor_args():
    sig = inspect.signature(go::EXPRESSAO.__init__)
    params = list(sig.parameters.keys())



def test_go::rangedecl_is_not_abstract():
    assert not inspect.isabstract(go::RangeDecl)


def test_go::rangedecl_constructor_exists():
    assert callable(go::RangeDecl.__init__)


def test_go::rangedecl_constructor_args():
    sig = inspect.signature(go::RangeDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::forclause_is_not_abstract():
    assert not inspect.isabstract(go::ForClause)


def test_go::forclause_constructor_exists():
    assert callable(go::ForClause.__init__)


def test_go::forclause_constructor_args():
    sig = inspect.signature(go::ForClause.__init__)
    params = list(sig.parameters.keys())



def test_go::fordecl_is_not_abstract():
    assert not inspect.isabstract(go::ForDecl)


def test_go::fordecl_constructor_exists():
    assert callable(go::ForDecl.__init__)


def test_go::fordecl_constructor_args():
    sig = inspect.signature(go::ForDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::expressaolinha_is_not_abstract():
    assert not inspect.isabstract(go::EXPRESSAOLINHA)


def test_go::expressaolinha_constructor_exists():
    assert callable(go::EXPRESSAOLINHA.__init__)


def test_go::expressaolinha_constructor_args():
    sig = inspect.signature(go::EXPRESSAOLINHA.__init__)
    params = list(sig.parameters.keys())



def test_go::functiontype_is_not_abstract():
    assert not inspect.isabstract(go::FunctionType)


def test_go::functiontype_constructor_exists():
    assert callable(go::FunctionType.__init__)


def test_go::functiontype_constructor_args():
    sig = inspect.signature(go::FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "nome" in params, "Missing parameter 'nome'"

def test_go::functiontype_has_nome():
    assert hasattr(go::FunctionType, "nome")
    descriptor = None
    for klass in go::FunctionType.__mro__:
        if "nome" in klass.__dict__:
            descriptor = klass.__dict__["nome"]
            break
    assert isinstance(descriptor, property)



def test_go::functioncall_is_not_abstract():
    assert not inspect.isabstract(go::FunctionCall)


def test_go::functioncall_constructor_exists():
    assert callable(go::FunctionCall.__init__)


def test_go::functioncall_constructor_args():
    sig = inspect.signature(go::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go::functioncall_has_id():
    assert hasattr(go::FunctionCall, "id")
    descriptor = None
    for klass in go::FunctionCall.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go::varcall_is_not_abstract():
    assert not inspect.isabstract(go::VarCall)


def test_go::varcall_constructor_exists():
    assert callable(go::VarCall.__init__)


def test_go::varcall_constructor_args():
    sig = inspect.signature(go::VarCall.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_go::varcall_has_id():
    assert hasattr(go::VarCall, "id")
    descriptor = None
    for klass in go::VarCall.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_go::pontosigual_is_not_abstract():
    assert not inspect.isabstract(go::PONTOSIGUAL)


def test_go::pontosigual_constructor_exists():
    assert callable(go::PONTOSIGUAL.__init__)


def test_go::pontosigual_constructor_args():
    sig = inspect.signature(go::PONTOSIGUAL.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_go::pontosigual_has_op():
    assert hasattr(go::PONTOSIGUAL, "op")
    descriptor = None
    for klass in go::PONTOSIGUAL.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_go::igual_is_not_abstract():
    assert not inspect.isabstract(go::IGUAL)


def test_go::igual_constructor_exists():
    assert callable(go::IGUAL.__init__)


def test_go::igual_constructor_args():
    sig = inspect.signature(go::IGUAL.__init__)
    params = list(sig.parameters.keys())
    assert "igual" in params, "Missing parameter 'igual'"

def test_go::igual_has_igual():
    assert hasattr(go::IGUAL, "igual")
    descriptor = None
    for klass in go::IGUAL.__mro__:
        if "igual" in klass.__dict__:
            descriptor = klass.__dict__["igual"]
            break
    assert isinstance(descriptor, property)



def test_go::idlist_is_not_abstract():
    assert not inspect.isabstract(go::IDList)


def test_go::idlist_constructor_exists():
    assert callable(go::IDList.__init__)


def test_go::idlist_constructor_args():
    sig = inspect.signature(go::IDList.__init__)
    params = list(sig.parameters.keys())
    assert "idList" in params, "Missing parameter 'idList'"
    assert "vir" in params, "Missing parameter 'vir'"

def test_go::idlist_has_idList():
    assert hasattr(go::IDList, "idList")
    descriptor = None
    for klass in go::IDList.__mro__:
        if "idList" in klass.__dict__:
            descriptor = klass.__dict__["idList"]
            break
    assert isinstance(descriptor, property)

def test_go::idlist_has_vir():
    assert hasattr(go::IDList, "vir")
    descriptor = None
    for klass in go::IDList.__mro__:
        if "vir" in klass.__dict__:
            descriptor = klass.__dict__["vir"]
            break
    assert isinstance(descriptor, property)



def test_go::vardecl_is_not_abstract():
    assert not inspect.isabstract(go::VarDecl)


def test_go::vardecl_constructor_exists():
    assert callable(go::VarDecl.__init__)


def test_go::vardecl_constructor_args():
    sig = inspect.signature(go::VarDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::boolean::value_is_not_abstract():
    assert not inspect.isabstract(go::BOOLEAN::VALUE)


def test_go::boolean::value_constructor_exists():
    assert callable(go::BOOLEAN::VALUE.__init__)


def test_go::boolean::value_constructor_args():
    sig = inspect.signature(go::BOOLEAN::VALUE.__init__)
    params = list(sig.parameters.keys())
    assert "falso" in params, "Missing parameter 'falso'"
    assert "verdadeiro" in params, "Missing parameter 'verdadeiro'"

def test_go::boolean::value_has_falso():
    assert hasattr(go::BOOLEAN::VALUE, "falso")
    descriptor = None
    for klass in go::BOOLEAN::VALUE.__mro__:
        if "falso" in klass.__dict__:
            descriptor = klass.__dict__["falso"]
            break
    assert isinstance(descriptor, property)

def test_go::boolean::value_has_verdadeiro():
    assert hasattr(go::BOOLEAN::VALUE, "verdadeiro")
    descriptor = None
    for klass in go::BOOLEAN::VALUE.__mro__:
        if "verdadeiro" in klass.__dict__:
            descriptor = klass.__dict__["verdadeiro"]
            break
    assert isinstance(descriptor, property)



def test_go::godecl_is_not_abstract():
    assert not inspect.isabstract(go::GoDecl)


def test_go::godecl_constructor_exists():
    assert callable(go::GoDecl.__init__)


def test_go::godecl_constructor_args():
    sig = inspect.signature(go::GoDecl.__init__)
    params = list(sig.parameters.keys())



def test_go::init_is_not_abstract():
    assert not inspect.isabstract(go::Init)


def test_go::init_constructor_exists():
    assert callable(go::Init.__init__)


def test_go::init_constructor_args():
    sig = inspect.signature(go::Init.__init__)
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
go::ElseCondition_strategy = st.builds(
    go::ElseCondition,
)
go::ElseIfCondition_strategy = st.builds(
    go::ElseIfCondition,
)
go::BasicType_strategy = st.builds(
    go::BasicType,
    float=
        safe_text,
    boolean=
        safe_text,
    string=
        safe_text,
    int=
        safe_text
)
go::PARAMETER_strategy = st.builds(
    go::PARAMETER,
    id=
        safe_text
)
go::BOOL::OP_strategy = st.builds(
    go::BOOL::OP,
)
ElseIfCondition_strategy = st.builds(
    ElseIfCondition,
)
go::IfCondition_strategy = st.builds(
    go::IfCondition,
)
go::PARAMETERS::LIST_strategy = st.builds(
    go::PARAMETERS::LIST,
    vir=
        safe_text
)
go::Parameters_strategy = st.builds(
    go::Parameters,
)
go::BLOCK_strategy = st.builds(
    go::BLOCK,
)
go::Signature_strategy = st.builds(
    go::Signature,
)
go::ReturnStmt_strategy = st.builds(
    go::ReturnStmt,
)
go::IfStmt_strategy = st.builds(
    go::IfStmt,
)
go::Chamada_strategy = st.builds(
    go::Chamada,
)
go::ArrayValue_strategy = st.builds(
    go::ArrayValue,
)
go::EObject_strategy = st.builds(
    go::EObject,
)
go::LiteraisList_strategy = st.builds(
    go::LiteraisList,
    vir=
        safe_text
)
go::Const_strategy = st.builds(
    go::Const,
    const=
        safe_text
)
go::LITERAIS::BASICOS_strategy = st.builds(
    go::LITERAIS::BASICOS,
    numero=
        safe_text,
    string=
        safe_text
)
go::BINARY::EXP_strategy = st.builds(
    go::BINARY::EXP,
    arit=
        safe_text
)
go::ArrayType_strategy = st.builds(
    go::ArrayType,
    qtd=
        safe_text
)
go::Var_strategy = st.builds(
    go::Var,
    var=
        safe_text
)
go::SignatureDel_strategy = st.builds(
    go::SignatureDel,
    id=
        safe_text
)
go::Assignment_strategy = st.builds(
    go::Assignment,
    id=
        safe_text,
    qtd=
        safe_text
)
go::Types_strategy = st.builds(
    go::Types,
)
go::TIPO_strategy = st.builds(
    go::TIPO,
)
go::ARIT::EXPR_strategy = st.builds(
    go::ARIT::EXPR,
    atr=
        safe_text,
    num1=
        safe_text,
    num=
        safe_text,
    op=
        safe_text,
    num2=
        safe_text
)
go::PostStmt_strategy = st.builds(
    go::PostStmt,
)
go::Condition_strategy = st.builds(
    go::Condition,
)
go::InitStmt_strategy = st.builds(
    go::InitStmt,
)
go::COMPARISON_strategy = st.builds(
    go::COMPARISON,
    maiorigualque=
        safe_text,
    igual=
        safe_text,
    maiorque=
        safe_text,
    menorque=
        safe_text,
    menorigualque=
        safe_text
)
go::EXPRESSAO_strategy = st.builds(
    go::EXPRESSAO,
)
go::RangeDecl_strategy = st.builds(
    go::RangeDecl,
)
go::ForClause_strategy = st.builds(
    go::ForClause,
)
go::ForDecl_strategy = st.builds(
    go::ForDecl,
)
go::EXPRESSAOLINHA_strategy = st.builds(
    go::EXPRESSAOLINHA,
)
go::FunctionType_strategy = st.builds(
    go::FunctionType,
    nome=
        safe_text
)
go::FunctionCall_strategy = st.builds(
    go::FunctionCall,
    id=
        safe_text
)
go::VarCall_strategy = st.builds(
    go::VarCall,
    id=
        safe_text
)
go::PONTOSIGUAL_strategy = st.builds(
    go::PONTOSIGUAL,
    op=
        safe_text
)
go::IGUAL_strategy = st.builds(
    go::IGUAL,
    igual=
        safe_text
)
go::IDList_strategy = st.builds(
    go::IDList,
    idList=
        safe_text,
    vir=
        safe_text
)
go::VarDecl_strategy = st.builds(
    go::VarDecl,
)
go::BOOLEAN::VALUE_strategy = st.builds(
    go::BOOLEAN::VALUE,
    falso=
        safe_text,
    verdadeiro=
        safe_text
)
go::GoDecl_strategy = st.builds(
    go::GoDecl,
)
go::Init_strategy = st.builds(
    go::Init,
)

@given(instance=go::ElseCondition_strategy)
@settings(max_examples=50)
def test_go::elsecondition_instantiation(instance):
    assert isinstance(instance, go::ElseCondition)

@given(instance=go::ElseIfCondition_strategy)
@settings(max_examples=50)
def test_go::elseifcondition_instantiation(instance):
    assert isinstance(instance, go::ElseIfCondition)

@given(instance=go::BasicType_strategy)
@settings(max_examples=50)
def test_go::basictype_instantiation(instance):
    assert isinstance(instance, go::BasicType)

@given(instance=go::BasicType_strategy)
def test_go::basictype_float_type(instance):
    assert isinstance(instance.float, str)


@given(instance=go::BasicType_strategy)
def test_go::basictype_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=go::BasicType_strategy)
def test_go::basictype_boolean_type(instance):
    assert isinstance(instance.boolean, str)


@given(instance=go::BasicType_strategy)
def test_go::basictype_boolean_setter(instance):
    original = instance.boolean
    instance.boolean = original
    assert instance.boolean == original

@given(instance=go::BasicType_strategy)
def test_go::basictype_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=go::BasicType_strategy)
def test_go::basictype_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=go::BasicType_strategy)
def test_go::basictype_int_type(instance):
    assert isinstance(instance.int, str)


@given(instance=go::BasicType_strategy)
def test_go::basictype_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=go::PARAMETER_strategy)
@settings(max_examples=50)
def test_go::parameter_instantiation(instance):
    assert isinstance(instance, go::PARAMETER)

@given(instance=go::PARAMETER_strategy)
def test_go::parameter_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=go::PARAMETER_strategy)
def test_go::parameter_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go::BOOL::OP_strategy)
@settings(max_examples=50)
def test_go::bool::op_instantiation(instance):
    assert isinstance(instance, go::BOOL::OP)

@given(instance=ElseIfCondition_strategy)
@settings(max_examples=50)
def test_elseifcondition_instantiation(instance):
    assert isinstance(instance, ElseIfCondition)

@given(instance=go::IfCondition_strategy)
@settings(max_examples=50)
def test_go::ifcondition_instantiation(instance):
    assert isinstance(instance, go::IfCondition)

@given(instance=go::PARAMETERS::LIST_strategy)
@settings(max_examples=50)
def test_go::parameters::list_instantiation(instance):
    assert isinstance(instance, go::PARAMETERS::LIST)

@given(instance=go::PARAMETERS::LIST_strategy)
def test_go::parameters::list_vir_type(instance):
    assert isinstance(instance.vir, str)


@given(instance=go::PARAMETERS::LIST_strategy)
def test_go::parameters::list_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original

@given(instance=go::Parameters_strategy)
@settings(max_examples=50)
def test_go::parameters_instantiation(instance):
    assert isinstance(instance, go::Parameters)

@given(instance=go::BLOCK_strategy)
@settings(max_examples=50)
def test_go::block_instantiation(instance):
    assert isinstance(instance, go::BLOCK)

@given(instance=go::Signature_strategy)
@settings(max_examples=50)
def test_go::signature_instantiation(instance):
    assert isinstance(instance, go::Signature)

@given(instance=go::ReturnStmt_strategy)
@settings(max_examples=50)
def test_go::returnstmt_instantiation(instance):
    assert isinstance(instance, go::ReturnStmt)

@given(instance=go::IfStmt_strategy)
@settings(max_examples=50)
def test_go::ifstmt_instantiation(instance):
    assert isinstance(instance, go::IfStmt)

@given(instance=go::Chamada_strategy)
@settings(max_examples=50)
def test_go::chamada_instantiation(instance):
    assert isinstance(instance, go::Chamada)

@given(instance=go::ArrayValue_strategy)
@settings(max_examples=50)
def test_go::arrayvalue_instantiation(instance):
    assert isinstance(instance, go::ArrayValue)

@given(instance=go::EObject_strategy)
@settings(max_examples=50)
def test_go::eobject_instantiation(instance):
    assert isinstance(instance, go::EObject)

@given(instance=go::LiteraisList_strategy)
@settings(max_examples=50)
def test_go::literaislist_instantiation(instance):
    assert isinstance(instance, go::LiteraisList)

@given(instance=go::LiteraisList_strategy)
def test_go::literaislist_vir_type(instance):
    assert isinstance(instance.vir, str)


@given(instance=go::LiteraisList_strategy)
def test_go::literaislist_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original

@given(instance=go::Const_strategy)
@settings(max_examples=50)
def test_go::const_instantiation(instance):
    assert isinstance(instance, go::Const)

@given(instance=go::Const_strategy)
def test_go::const_const_type(instance):
    assert isinstance(instance.const, str)


@given(instance=go::Const_strategy)
def test_go::const_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=go::LITERAIS::BASICOS_strategy)
@settings(max_examples=50)
def test_go::literais::basicos_instantiation(instance):
    assert isinstance(instance, go::LITERAIS::BASICOS)

@given(instance=go::LITERAIS::BASICOS_strategy)
def test_go::literais::basicos_numero_type(instance):
    assert isinstance(instance.numero, str)


@given(instance=go::LITERAIS::BASICOS_strategy)
def test_go::literais::basicos_numero_setter(instance):
    original = instance.numero
    instance.numero = original
    assert instance.numero == original

@given(instance=go::LITERAIS::BASICOS_strategy)
def test_go::literais::basicos_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=go::LITERAIS::BASICOS_strategy)
def test_go::literais::basicos_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=go::BINARY::EXP_strategy)
@settings(max_examples=50)
def test_go::binary::exp_instantiation(instance):
    assert isinstance(instance, go::BINARY::EXP)

@given(instance=go::BINARY::EXP_strategy)
def test_go::binary::exp_arit_type(instance):
    assert isinstance(instance.arit, str)


@given(instance=go::BINARY::EXP_strategy)
def test_go::binary::exp_arit_setter(instance):
    original = instance.arit
    instance.arit = original
    assert instance.arit == original

@given(instance=go::ArrayType_strategy)
@settings(max_examples=50)
def test_go::arraytype_instantiation(instance):
    assert isinstance(instance, go::ArrayType)

@given(instance=go::ArrayType_strategy)
def test_go::arraytype_qtd_type(instance):
    assert isinstance(instance.qtd, str)


@given(instance=go::ArrayType_strategy)
def test_go::arraytype_qtd_setter(instance):
    original = instance.qtd
    instance.qtd = original
    assert instance.qtd == original

@given(instance=go::Var_strategy)
@settings(max_examples=50)
def test_go::var_instantiation(instance):
    assert isinstance(instance, go::Var)

@given(instance=go::Var_strategy)
def test_go::var_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=go::Var_strategy)
def test_go::var_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=go::SignatureDel_strategy)
@settings(max_examples=50)
def test_go::signaturedel_instantiation(instance):
    assert isinstance(instance, go::SignatureDel)

@given(instance=go::SignatureDel_strategy)
def test_go::signaturedel_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=go::SignatureDel_strategy)
def test_go::signaturedel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go::Assignment_strategy)
@settings(max_examples=50)
def test_go::assignment_instantiation(instance):
    assert isinstance(instance, go::Assignment)

@given(instance=go::Assignment_strategy)
def test_go::assignment_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=go::Assignment_strategy)
def test_go::assignment_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go::Assignment_strategy)
def test_go::assignment_qtd_type(instance):
    assert isinstance(instance.qtd, str)


@given(instance=go::Assignment_strategy)
def test_go::assignment_qtd_setter(instance):
    original = instance.qtd
    instance.qtd = original
    assert instance.qtd == original

@given(instance=go::Types_strategy)
@settings(max_examples=50)
def test_go::types_instantiation(instance):
    assert isinstance(instance, go::Types)

@given(instance=go::TIPO_strategy)
@settings(max_examples=50)
def test_go::tipo_instantiation(instance):
    assert isinstance(instance, go::TIPO)

@given(instance=go::ARIT::EXPR_strategy)
@settings(max_examples=50)
def test_go::arit::expr_instantiation(instance):
    assert isinstance(instance, go::ARIT::EXPR)

@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_atr_type(instance):
    assert isinstance(instance.atr, str)


@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_atr_setter(instance):
    original = instance.atr
    instance.atr = original
    assert instance.atr == original

@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num1_type(instance):
    assert isinstance(instance.num1, str)


@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num1_setter(instance):
    original = instance.num1
    instance.num1 = original
    assert instance.num1 == original

@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num_type(instance):
    assert isinstance(instance.num, str)


@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original

@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num2_type(instance):
    assert isinstance(instance.num2, str)


@given(instance=go::ARIT::EXPR_strategy)
def test_go::arit::expr_num2_setter(instance):
    original = instance.num2
    instance.num2 = original
    assert instance.num2 == original

@given(instance=go::PostStmt_strategy)
@settings(max_examples=50)
def test_go::poststmt_instantiation(instance):
    assert isinstance(instance, go::PostStmt)

@given(instance=go::Condition_strategy)
@settings(max_examples=50)
def test_go::condition_instantiation(instance):
    assert isinstance(instance, go::Condition)

@given(instance=go::InitStmt_strategy)
@settings(max_examples=50)
def test_go::initstmt_instantiation(instance):
    assert isinstance(instance, go::InitStmt)

@given(instance=go::COMPARISON_strategy)
@settings(max_examples=50)
def test_go::comparison_instantiation(instance):
    assert isinstance(instance, go::COMPARISON)

@given(instance=go::COMPARISON_strategy)
def test_go::comparison_maiorigualque_type(instance):
    assert isinstance(instance.maiorigualque, str)


@given(instance=go::COMPARISON_strategy)
def test_go::comparison_maiorigualque_setter(instance):
    original = instance.maiorigualque
    instance.maiorigualque = original
    assert instance.maiorigualque == original

@given(instance=go::COMPARISON_strategy)
def test_go::comparison_igual_type(instance):
    assert isinstance(instance.igual, str)


@given(instance=go::COMPARISON_strategy)
def test_go::comparison_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original

@given(instance=go::COMPARISON_strategy)
def test_go::comparison_maiorque_type(instance):
    assert isinstance(instance.maiorque, str)


@given(instance=go::COMPARISON_strategy)
def test_go::comparison_maiorque_setter(instance):
    original = instance.maiorque
    instance.maiorque = original
    assert instance.maiorque == original

@given(instance=go::COMPARISON_strategy)
def test_go::comparison_menorque_type(instance):
    assert isinstance(instance.menorque, str)


@given(instance=go::COMPARISON_strategy)
def test_go::comparison_menorque_setter(instance):
    original = instance.menorque
    instance.menorque = original
    assert instance.menorque == original

@given(instance=go::COMPARISON_strategy)
def test_go::comparison_menorigualque_type(instance):
    assert isinstance(instance.menorigualque, str)


@given(instance=go::COMPARISON_strategy)
def test_go::comparison_menorigualque_setter(instance):
    original = instance.menorigualque
    instance.menorigualque = original
    assert instance.menorigualque == original

@given(instance=go::EXPRESSAO_strategy)
@settings(max_examples=50)
def test_go::expressao_instantiation(instance):
    assert isinstance(instance, go::EXPRESSAO)

@given(instance=go::RangeDecl_strategy)
@settings(max_examples=50)
def test_go::rangedecl_instantiation(instance):
    assert isinstance(instance, go::RangeDecl)

@given(instance=go::ForClause_strategy)
@settings(max_examples=50)
def test_go::forclause_instantiation(instance):
    assert isinstance(instance, go::ForClause)

@given(instance=go::ForDecl_strategy)
@settings(max_examples=50)
def test_go::fordecl_instantiation(instance):
    assert isinstance(instance, go::ForDecl)

@given(instance=go::EXPRESSAOLINHA_strategy)
@settings(max_examples=50)
def test_go::expressaolinha_instantiation(instance):
    assert isinstance(instance, go::EXPRESSAOLINHA)

@given(instance=go::FunctionType_strategy)
@settings(max_examples=50)
def test_go::functiontype_instantiation(instance):
    assert isinstance(instance, go::FunctionType)

@given(instance=go::FunctionType_strategy)
def test_go::functiontype_nome_type(instance):
    assert isinstance(instance.nome, str)


@given(instance=go::FunctionType_strategy)
def test_go::functiontype_nome_setter(instance):
    original = instance.nome
    instance.nome = original
    assert instance.nome == original

@given(instance=go::FunctionCall_strategy)
@settings(max_examples=50)
def test_go::functioncall_instantiation(instance):
    assert isinstance(instance, go::FunctionCall)

@given(instance=go::FunctionCall_strategy)
def test_go::functioncall_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=go::FunctionCall_strategy)
def test_go::functioncall_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go::VarCall_strategy)
@settings(max_examples=50)
def test_go::varcall_instantiation(instance):
    assert isinstance(instance, go::VarCall)

@given(instance=go::VarCall_strategy)
def test_go::varcall_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=go::VarCall_strategy)
def test_go::varcall_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=go::PONTOSIGUAL_strategy)
@settings(max_examples=50)
def test_go::pontosigual_instantiation(instance):
    assert isinstance(instance, go::PONTOSIGUAL)

@given(instance=go::PONTOSIGUAL_strategy)
def test_go::pontosigual_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=go::PONTOSIGUAL_strategy)
def test_go::pontosigual_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=go::IGUAL_strategy)
@settings(max_examples=50)
def test_go::igual_instantiation(instance):
    assert isinstance(instance, go::IGUAL)

@given(instance=go::IGUAL_strategy)
def test_go::igual_igual_type(instance):
    assert isinstance(instance.igual, str)


@given(instance=go::IGUAL_strategy)
def test_go::igual_igual_setter(instance):
    original = instance.igual
    instance.igual = original
    assert instance.igual == original

@given(instance=go::IDList_strategy)
@settings(max_examples=50)
def test_go::idlist_instantiation(instance):
    assert isinstance(instance, go::IDList)

@given(instance=go::IDList_strategy)
def test_go::idlist_idList_type(instance):
    assert isinstance(instance.idList, str)


@given(instance=go::IDList_strategy)
def test_go::idlist_idList_setter(instance):
    original = instance.idList
    instance.idList = original
    assert instance.idList == original

@given(instance=go::IDList_strategy)
def test_go::idlist_vir_type(instance):
    assert isinstance(instance.vir, str)


@given(instance=go::IDList_strategy)
def test_go::idlist_vir_setter(instance):
    original = instance.vir
    instance.vir = original
    assert instance.vir == original

@given(instance=go::VarDecl_strategy)
@settings(max_examples=50)
def test_go::vardecl_instantiation(instance):
    assert isinstance(instance, go::VarDecl)

@given(instance=go::BOOLEAN::VALUE_strategy)
@settings(max_examples=50)
def test_go::boolean::value_instantiation(instance):
    assert isinstance(instance, go::BOOLEAN::VALUE)

@given(instance=go::BOOLEAN::VALUE_strategy)
def test_go::boolean::value_falso_type(instance):
    assert isinstance(instance.falso, str)


@given(instance=go::BOOLEAN::VALUE_strategy)
def test_go::boolean::value_falso_setter(instance):
    original = instance.falso
    instance.falso = original
    assert instance.falso == original

@given(instance=go::BOOLEAN::VALUE_strategy)
def test_go::boolean::value_verdadeiro_type(instance):
    assert isinstance(instance.verdadeiro, str)


@given(instance=go::BOOLEAN::VALUE_strategy)
def test_go::boolean::value_verdadeiro_setter(instance):
    original = instance.verdadeiro
    instance.verdadeiro = original
    assert instance.verdadeiro == original

@given(instance=go::GoDecl_strategy)
@settings(max_examples=50)
def test_go::godecl_instantiation(instance):
    assert isinstance(instance, go::GoDecl)

@given(instance=go::Init_strategy)
@settings(max_examples=50)
def test_go::init_instantiation(instance):
    assert isinstance(instance, go::Init)
