import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PreContent,
    xhtml_PreContent,
    xhtml_Inline,
    xhtml_FormContent,
    xhtml_Flow,
    xhtml_TbodyType,
    xhtml_TrType,
    xhtml_TheadType,
    xhtml_TfootType,
    xhtml_ParamType,
    xhtml_HtmlType,
    xhtml_EStringToStringMapEntry,
    xhtml_DocumentRoot,
    Flow,
    xhtml_TdType,
    xhtml_LiType,
    xhtml_ThType,
    xhtml_DdType,
    xhtml_ColType,
    xhtml_ColgroupType,
    Block,
    xhtml_BodyType,
    xhtml_BlockquoteType,
    xhtml_HrType,
    xhtml_PreType,
    xhtml_TableType,
    xhtml_UlType,
    xhtml_DivType,
    xhtml_DlType,
    xhtml_OlType,
    xhtml_Block,
    AContent,
    xhtml_AType,
    xhtml_InsType,
    xhtml_DelType,
    xhtml_ImgType,
    xhtml_ObjectType,
    xhtml_AContent,
    Inline,
    xhtml_DfnType,
    xhtml_PType,
    xhtml_QType,
    xhtml_KbdType,
    xhtml_EmType,
    xhtml_DtType,
    xhtml_AcronymType,
    xhtml_BigType,
    xhtml_TtType,
    xhtml_H6Type,
    xhtml_H2Type,
    xhtml_StrongType,
    xhtml_SampType,
    xhtml_IType,
    xhtml_AddressType,
    xhtml_CiteType,
    xhtml_BType,
    xhtml_H5Type,
    xhtml_H1Type,
    xhtml_H3Type,
    xhtml_VarType,
    xhtml_SmallType,
    xhtml_UType,
    xhtml_StrikeType,
    xhtml_SubType,
    xhtml_CaptionType,
    xhtml_H4Type,
    xhtml_CodeType,
    xhtml_SupType,
    xhtml_AbbrType,
    xhtml_SpanType,
    xhtml_BrType,
    ValuetypeType,
    ValignType,
    AlignType,
    DeclareType,
    Shape,
    IsmapType,
    Scope,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_precontent_is_not_abstract():
    assert not inspect.isabstract(PreContent)


def test_precontent_constructor_exists():
    assert callable(PreContent.__init__)


def test_precontent_constructor_args():
    sig = inspect.signature(PreContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_precontent_is_not_abstract():
    assert not inspect.isabstract(xhtml_PreContent)


def test_xhtml_precontent_constructor_exists():
    assert callable(xhtml_PreContent.__init__)


def test_xhtml_precontent_constructor_args():
    sig = inspect.signature(xhtml_PreContent.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml_precontent_has_mixed():
    assert hasattr(xhtml_PreContent, "mixed")
    descriptor = None
    for klass in xhtml_PreContent.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_precontent_has_group():
    assert hasattr(xhtml_PreContent, "group")
    descriptor = None
    for klass in xhtml_PreContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_inline_is_not_abstract():
    assert not inspect.isabstract(xhtml_Inline)


def test_xhtml_inline_constructor_exists():
    assert callable(xhtml_Inline.__init__)


def test_xhtml_inline_constructor_args():
    sig = inspect.signature(xhtml_Inline.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml_inline_has_mixed():
    assert hasattr(xhtml_Inline, "mixed")
    descriptor = None
    for klass in xhtml_Inline.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_inline_has_group():
    assert hasattr(xhtml_Inline, "group")
    descriptor = None
    for klass in xhtml_Inline.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_formcontent_is_not_abstract():
    assert not inspect.isabstract(xhtml_FormContent)


def test_xhtml_formcontent_constructor_exists():
    assert callable(xhtml_FormContent.__init__)


def test_xhtml_formcontent_constructor_args():
    sig = inspect.signature(xhtml_FormContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml_formcontent_has_group():
    assert hasattr(xhtml_FormContent, "group")
    descriptor = None
    for klass in xhtml_FormContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_flow_is_not_abstract():
    assert not inspect.isabstract(xhtml_Flow)


def test_xhtml_flow_constructor_exists():
    assert callable(xhtml_Flow.__init__)


def test_xhtml_flow_constructor_args():
    sig = inspect.signature(xhtml_Flow.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xhtml_flow_has_group():
    assert hasattr(xhtml_Flow, "group")
    descriptor = None
    for klass in xhtml_Flow.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_flow_has_mixed():
    assert hasattr(xhtml_Flow, "mixed")
    descriptor = None
    for klass in xhtml_Flow.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_tbodytype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TbodyType)


def test_xhtml_tbodytype_constructor_exists():
    assert callable(xhtml_TbodyType.__init__)


def test_xhtml_tbodytype_constructor_args():
    sig = inspect.signature(xhtml_TbodyType.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "style" in params, "Missing parameter 'style'"
    assert "align" in params, "Missing parameter 'align'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_tbodytype_has_char():
    assert hasattr(xhtml_TbodyType, "char")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_style():
    assert hasattr(xhtml_TbodyType, "style")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_align():
    assert hasattr(xhtml_TbodyType, "align")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_class_():
    assert hasattr(xhtml_TbodyType, "class_")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_id():
    assert hasattr(xhtml_TbodyType, "id")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_valign():
    assert hasattr(xhtml_TbodyType, "valign")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_charoff():
    assert hasattr(xhtml_TbodyType, "charoff")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tbodytype_has_title():
    assert hasattr(xhtml_TbodyType, "title")
    descriptor = None
    for klass in xhtml_TbodyType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_trtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TrType)


def test_xhtml_trtype_constructor_exists():
    assert callable(xhtml_TrType.__init__)


def test_xhtml_trtype_constructor_args():
    sig = inspect.signature(xhtml_TrType.__init__)
    params = list(sig.parameters.keys())
    assert "valign" in params, "Missing parameter 'valign'"
    assert "title" in params, "Missing parameter 'title'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "style" in params, "Missing parameter 'style'"
    assert "align" in params, "Missing parameter 'align'"

def test_xhtml_trtype_has_valign():
    assert hasattr(xhtml_TrType, "valign")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_title():
    assert hasattr(xhtml_TrType, "title")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_char():
    assert hasattr(xhtml_TrType, "char")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_class_():
    assert hasattr(xhtml_TrType, "class_")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_id():
    assert hasattr(xhtml_TrType, "id")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_group():
    assert hasattr(xhtml_TrType, "group")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_charoff():
    assert hasattr(xhtml_TrType, "charoff")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_style():
    assert hasattr(xhtml_TrType, "style")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_trtype_has_align():
    assert hasattr(xhtml_TrType, "align")
    descriptor = None
    for klass in xhtml_TrType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_theadtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TheadType)


def test_xhtml_theadtype_constructor_exists():
    assert callable(xhtml_TheadType.__init__)


def test_xhtml_theadtype_constructor_args():
    sig = inspect.signature(xhtml_TheadType.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "char" in params, "Missing parameter 'char'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_theadtype_has_align():
    assert hasattr(xhtml_TheadType, "align")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_id():
    assert hasattr(xhtml_TheadType, "id")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_title():
    assert hasattr(xhtml_TheadType, "title")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_char():
    assert hasattr(xhtml_TheadType, "char")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_valign():
    assert hasattr(xhtml_TheadType, "valign")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_charoff():
    assert hasattr(xhtml_TheadType, "charoff")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_class_():
    assert hasattr(xhtml_TheadType, "class_")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_theadtype_has_style():
    assert hasattr(xhtml_TheadType, "style")
    descriptor = None
    for klass in xhtml_TheadType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_tfoottype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TfootType)


def test_xhtml_tfoottype_constructor_exists():
    assert callable(xhtml_TfootType.__init__)


def test_xhtml_tfoottype_constructor_args():
    sig = inspect.signature(xhtml_TfootType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "align" in params, "Missing parameter 'align'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "id" in params, "Missing parameter 'id'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "char" in params, "Missing parameter 'char'"

def test_xhtml_tfoottype_has_title():
    assert hasattr(xhtml_TfootType, "title")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_style():
    assert hasattr(xhtml_TfootType, "style")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_class_():
    assert hasattr(xhtml_TfootType, "class_")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_align():
    assert hasattr(xhtml_TfootType, "align")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_charoff():
    assert hasattr(xhtml_TfootType, "charoff")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_id():
    assert hasattr(xhtml_TfootType, "id")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_valign():
    assert hasattr(xhtml_TfootType, "valign")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tfoottype_has_char():
    assert hasattr(xhtml_TfootType, "char")
    descriptor = None
    for klass in xhtml_TfootType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_paramtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ParamType)


def test_xhtml_paramtype_constructor_exists():
    assert callable(xhtml_ParamType.__init__)


def test_xhtml_paramtype_constructor_args():
    sig = inspect.signature(xhtml_ParamType.__init__)
    params = list(sig.parameters.keys())
    assert "valuetype" in params, "Missing parameter 'valuetype'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_paramtype_has_valuetype():
    assert hasattr(xhtml_ParamType, "valuetype")
    descriptor = None
    for klass in xhtml_ParamType.__mro__:
        if "valuetype" in klass.__dict__:
            descriptor = klass.__dict__["valuetype"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_paramtype_has_type():
    assert hasattr(xhtml_ParamType, "type")
    descriptor = None
    for klass in xhtml_ParamType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_paramtype_has_name():
    assert hasattr(xhtml_ParamType, "name")
    descriptor = None
    for klass in xhtml_ParamType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_paramtype_has_value():
    assert hasattr(xhtml_ParamType, "value")
    descriptor = None
    for klass in xhtml_ParamType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_paramtype_has_id():
    assert hasattr(xhtml_ParamType, "id")
    descriptor = None
    for klass in xhtml_ParamType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_htmltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_HtmlType)


def test_xhtml_htmltype_constructor_exists():
    assert callable(xhtml_HtmlType.__init__)


def test_xhtml_htmltype_constructor_args():
    sig = inspect.signature(xhtml_HtmlType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_htmltype_has_id():
    assert hasattr(xhtml_HtmlType, "id")
    descriptor = None
    for klass in xhtml_HtmlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xhtml_EStringToStringMapEntry)


def test_xhtml_estringtostringmapentry_constructor_exists():
    assert callable(xhtml_EStringToStringMapEntry.__init__)


def test_xhtml_estringtostringmapentry_constructor_args():
    sig = inspect.signature(xhtml_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_documentroot_is_not_abstract():
    assert not inspect.isabstract(xhtml_DocumentRoot)


def test_xhtml_documentroot_constructor_exists():
    assert callable(xhtml_DocumentRoot.__init__)


def test_xhtml_documentroot_constructor_args():
    sig = inspect.signature(xhtml_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xhtml_documentroot_has_mixed():
    assert hasattr(xhtml_DocumentRoot, "mixed")
    descriptor = None
    for klass in xhtml_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_tdtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TdType)


def test_xhtml_tdtype_constructor_exists():
    assert callable(xhtml_TdType.__init__)


def test_xhtml_tdtype_constructor_args():
    sig = inspect.signature(xhtml_TdType.__init__)
    params = list(sig.parameters.keys())
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "id" in params, "Missing parameter 'id'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "align" in params, "Missing parameter 'align'"
    assert "style" in params, "Missing parameter 'style'"
    assert "char" in params, "Missing parameter 'char'"
    assert "headers" in params, "Missing parameter 'headers'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "title" in params, "Missing parameter 'title'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "axis" in params, "Missing parameter 'axis'"
    assert "abbr1" in params, "Missing parameter 'abbr1'"

def test_xhtml_tdtype_has_charoff():
    assert hasattr(xhtml_TdType, "charoff")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_id():
    assert hasattr(xhtml_TdType, "id")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_colspan():
    assert hasattr(xhtml_TdType, "colspan")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_class_():
    assert hasattr(xhtml_TdType, "class_")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_align():
    assert hasattr(xhtml_TdType, "align")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_style():
    assert hasattr(xhtml_TdType, "style")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_char():
    assert hasattr(xhtml_TdType, "char")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_headers():
    assert hasattr(xhtml_TdType, "headers")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "headers" in klass.__dict__:
            descriptor = klass.__dict__["headers"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_rowspan():
    assert hasattr(xhtml_TdType, "rowspan")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_title():
    assert hasattr(xhtml_TdType, "title")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_scope():
    assert hasattr(xhtml_TdType, "scope")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_valign():
    assert hasattr(xhtml_TdType, "valign")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_axis():
    assert hasattr(xhtml_TdType, "axis")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tdtype_has_abbr1():
    assert hasattr(xhtml_TdType, "abbr1")
    descriptor = None
    for klass in xhtml_TdType.__mro__:
        if "abbr1" in klass.__dict__:
            descriptor = klass.__dict__["abbr1"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_litype_is_not_abstract():
    assert not inspect.isabstract(xhtml_LiType)


def test_xhtml_litype_constructor_exists():
    assert callable(xhtml_LiType.__init__)


def test_xhtml_litype_constructor_args():
    sig = inspect.signature(xhtml_LiType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_litype_has_id():
    assert hasattr(xhtml_LiType, "id")
    descriptor = None
    for klass in xhtml_LiType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_litype_has_style():
    assert hasattr(xhtml_LiType, "style")
    descriptor = None
    for klass in xhtml_LiType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_litype_has_title():
    assert hasattr(xhtml_LiType, "title")
    descriptor = None
    for klass in xhtml_LiType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_litype_has_class_():
    assert hasattr(xhtml_LiType, "class_")
    descriptor = None
    for klass in xhtml_LiType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_thtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ThType)


def test_xhtml_thtype_constructor_exists():
    assert callable(xhtml_ThType.__init__)


def test_xhtml_thtype_constructor_args():
    sig = inspect.signature(xhtml_ThType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "char" in params, "Missing parameter 'char'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "headers" in params, "Missing parameter 'headers'"
    assert "style" in params, "Missing parameter 'style'"
    assert "axis" in params, "Missing parameter 'axis'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "align" in params, "Missing parameter 'align'"
    assert "abbr1" in params, "Missing parameter 'abbr1'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_thtype_has_class_():
    assert hasattr(xhtml_ThType, "class_")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_char():
    assert hasattr(xhtml_ThType, "char")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_colspan():
    assert hasattr(xhtml_ThType, "colspan")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_charoff():
    assert hasattr(xhtml_ThType, "charoff")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_headers():
    assert hasattr(xhtml_ThType, "headers")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "headers" in klass.__dict__:
            descriptor = klass.__dict__["headers"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_style():
    assert hasattr(xhtml_ThType, "style")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_axis():
    assert hasattr(xhtml_ThType, "axis")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_scope():
    assert hasattr(xhtml_ThType, "scope")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_rowspan():
    assert hasattr(xhtml_ThType, "rowspan")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_align():
    assert hasattr(xhtml_ThType, "align")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_abbr1():
    assert hasattr(xhtml_ThType, "abbr1")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "abbr1" in klass.__dict__:
            descriptor = klass.__dict__["abbr1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_valign():
    assert hasattr(xhtml_ThType, "valign")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_title():
    assert hasattr(xhtml_ThType, "title")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_thtype_has_id():
    assert hasattr(xhtml_ThType, "id")
    descriptor = None
    for klass in xhtml_ThType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_ddtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DdType)


def test_xhtml_ddtype_constructor_exists():
    assert callable(xhtml_DdType.__init__)


def test_xhtml_ddtype_constructor_args():
    sig = inspect.signature(xhtml_DdType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_ddtype_has_style():
    assert hasattr(xhtml_DdType, "style")
    descriptor = None
    for klass in xhtml_DdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ddtype_has_id():
    assert hasattr(xhtml_DdType, "id")
    descriptor = None
    for klass in xhtml_DdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ddtype_has_class_():
    assert hasattr(xhtml_DdType, "class_")
    descriptor = None
    for klass in xhtml_DdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ddtype_has_title():
    assert hasattr(xhtml_DdType, "title")
    descriptor = None
    for klass in xhtml_DdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_coltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ColType)


def test_xhtml_coltype_constructor_exists():
    assert callable(xhtml_ColType.__init__)


def test_xhtml_coltype_constructor_args():
    sig = inspect.signature(xhtml_ColType.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "id" in params, "Missing parameter 'id'"
    assert "span" in params, "Missing parameter 'span'"

def test_xhtml_coltype_has_char():
    assert hasattr(xhtml_ColType, "char")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_class_():
    assert hasattr(xhtml_ColType, "class_")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_charoff():
    assert hasattr(xhtml_ColType, "charoff")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_width():
    assert hasattr(xhtml_ColType, "width")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_style():
    assert hasattr(xhtml_ColType, "style")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_title():
    assert hasattr(xhtml_ColType, "title")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_align():
    assert hasattr(xhtml_ColType, "align")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_valign():
    assert hasattr(xhtml_ColType, "valign")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_id():
    assert hasattr(xhtml_ColType, "id")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_coltype_has_span():
    assert hasattr(xhtml_ColType, "span")
    descriptor = None
    for klass in xhtml_ColType.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_colgrouptype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ColgroupType)


def test_xhtml_colgrouptype_constructor_exists():
    assert callable(xhtml_ColgroupType.__init__)


def test_xhtml_colgrouptype_constructor_args():
    sig = inspect.signature(xhtml_ColgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "align" in params, "Missing parameter 'align'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "char" in params, "Missing parameter 'char'"
    assert "width" in params, "Missing parameter 'width'"
    assert "span" in params, "Missing parameter 'span'"
    assert "charoff" in params, "Missing parameter 'charoff'"

def test_xhtml_colgrouptype_has_id():
    assert hasattr(xhtml_ColgroupType, "id")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_align():
    assert hasattr(xhtml_ColgroupType, "align")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_class_():
    assert hasattr(xhtml_ColgroupType, "class_")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_valign():
    assert hasattr(xhtml_ColgroupType, "valign")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_title():
    assert hasattr(xhtml_ColgroupType, "title")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_style():
    assert hasattr(xhtml_ColgroupType, "style")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_char():
    assert hasattr(xhtml_ColgroupType, "char")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_width():
    assert hasattr(xhtml_ColgroupType, "width")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_span():
    assert hasattr(xhtml_ColgroupType, "span")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_colgrouptype_has_charoff():
    assert hasattr(xhtml_ColgroupType, "charoff")
    descriptor = None
    for klass in xhtml_ColgroupType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_bodytype_is_not_abstract():
    assert not inspect.isabstract(xhtml_BodyType)


def test_xhtml_bodytype_constructor_exists():
    assert callable(xhtml_BodyType.__init__)


def test_xhtml_bodytype_constructor_args():
    sig = inspect.signature(xhtml_BodyType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_bodytype_has_id():
    assert hasattr(xhtml_BodyType, "id")
    descriptor = None
    for klass in xhtml_BodyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bodytype_has_title():
    assert hasattr(xhtml_BodyType, "title")
    descriptor = None
    for klass in xhtml_BodyType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bodytype_has_class_():
    assert hasattr(xhtml_BodyType, "class_")
    descriptor = None
    for klass in xhtml_BodyType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bodytype_has_style():
    assert hasattr(xhtml_BodyType, "style")
    descriptor = None
    for klass in xhtml_BodyType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_blockquotetype_is_not_abstract():
    assert not inspect.isabstract(xhtml_BlockquoteType)


def test_xhtml_blockquotetype_constructor_exists():
    assert callable(xhtml_BlockquoteType.__init__)


def test_xhtml_blockquotetype_constructor_args():
    sig = inspect.signature(xhtml_BlockquoteType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "cite" in params, "Missing parameter 'cite'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_blockquotetype_has_title():
    assert hasattr(xhtml_BlockquoteType, "title")
    descriptor = None
    for klass in xhtml_BlockquoteType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_blockquotetype_has_cite():
    assert hasattr(xhtml_BlockquoteType, "cite")
    descriptor = None
    for klass in xhtml_BlockquoteType.__mro__:
        if "cite" in klass.__dict__:
            descriptor = klass.__dict__["cite"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_blockquotetype_has_id():
    assert hasattr(xhtml_BlockquoteType, "id")
    descriptor = None
    for klass in xhtml_BlockquoteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_blockquotetype_has_class_():
    assert hasattr(xhtml_BlockquoteType, "class_")
    descriptor = None
    for klass in xhtml_BlockquoteType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_blockquotetype_has_style():
    assert hasattr(xhtml_BlockquoteType, "style")
    descriptor = None
    for klass in xhtml_BlockquoteType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_hrtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_HrType)


def test_xhtml_hrtype_constructor_exists():
    assert callable(xhtml_HrType.__init__)


def test_xhtml_hrtype_constructor_args():
    sig = inspect.signature(xhtml_HrType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_hrtype_has_class_():
    assert hasattr(xhtml_HrType, "class_")
    descriptor = None
    for klass in xhtml_HrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_hrtype_has_title():
    assert hasattr(xhtml_HrType, "title")
    descriptor = None
    for klass in xhtml_HrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_hrtype_has_style():
    assert hasattr(xhtml_HrType, "style")
    descriptor = None
    for klass in xhtml_HrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_hrtype_has_id():
    assert hasattr(xhtml_HrType, "id")
    descriptor = None
    for klass in xhtml_HrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_pretype_is_not_abstract():
    assert not inspect.isabstract(xhtml_PreType)


def test_xhtml_pretype_constructor_exists():
    assert callable(xhtml_PreType.__init__)


def test_xhtml_pretype_constructor_args():
    sig = inspect.signature(xhtml_PreType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_pretype_has_id():
    assert hasattr(xhtml_PreType, "id")
    descriptor = None
    for klass in xhtml_PreType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_pretype_has_style():
    assert hasattr(xhtml_PreType, "style")
    descriptor = None
    for klass in xhtml_PreType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_pretype_has_title():
    assert hasattr(xhtml_PreType, "title")
    descriptor = None
    for klass in xhtml_PreType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_pretype_has_class_():
    assert hasattr(xhtml_PreType, "class_")
    descriptor = None
    for klass in xhtml_PreType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_tabletype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TableType)


def test_xhtml_tabletype_constructor_exists():
    assert callable(xhtml_TableType.__init__)


def test_xhtml_tabletype_constructor_args():
    sig = inspect.signature(xhtml_TableType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "style" in params, "Missing parameter 'style'"
    assert "border" in params, "Missing parameter 'border'"

def test_xhtml_tabletype_has_title():
    assert hasattr(xhtml_TableType, "title")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_cellpadding():
    assert hasattr(xhtml_TableType, "cellpadding")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "cellpadding" in klass.__dict__:
            descriptor = klass.__dict__["cellpadding"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_id():
    assert hasattr(xhtml_TableType, "id")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_class_():
    assert hasattr(xhtml_TableType, "class_")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_width():
    assert hasattr(xhtml_TableType, "width")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_summary():
    assert hasattr(xhtml_TableType, "summary")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_cellspacing():
    assert hasattr(xhtml_TableType, "cellspacing")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "cellspacing" in klass.__dict__:
            descriptor = klass.__dict__["cellspacing"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_style():
    assert hasattr(xhtml_TableType, "style")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tabletype_has_border():
    assert hasattr(xhtml_TableType, "border")
    descriptor = None
    for klass in xhtml_TableType.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_ultype_is_not_abstract():
    assert not inspect.isabstract(xhtml_UlType)


def test_xhtml_ultype_constructor_exists():
    assert callable(xhtml_UlType.__init__)


def test_xhtml_ultype_constructor_args():
    sig = inspect.signature(xhtml_UlType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_ultype_has_title():
    assert hasattr(xhtml_UlType, "title")
    descriptor = None
    for klass in xhtml_UlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ultype_has_style():
    assert hasattr(xhtml_UlType, "style")
    descriptor = None
    for klass in xhtml_UlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ultype_has_id():
    assert hasattr(xhtml_UlType, "id")
    descriptor = None
    for klass in xhtml_UlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ultype_has_class_():
    assert hasattr(xhtml_UlType, "class_")
    descriptor = None
    for klass in xhtml_UlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_divtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DivType)


def test_xhtml_divtype_constructor_exists():
    assert callable(xhtml_DivType.__init__)


def test_xhtml_divtype_constructor_args():
    sig = inspect.signature(xhtml_DivType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_divtype_has_id():
    assert hasattr(xhtml_DivType, "id")
    descriptor = None
    for klass in xhtml_DivType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_divtype_has_title():
    assert hasattr(xhtml_DivType, "title")
    descriptor = None
    for klass in xhtml_DivType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_divtype_has_class_():
    assert hasattr(xhtml_DivType, "class_")
    descriptor = None
    for klass in xhtml_DivType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_divtype_has_style():
    assert hasattr(xhtml_DivType, "style")
    descriptor = None
    for klass in xhtml_DivType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_dltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DlType)


def test_xhtml_dltype_constructor_exists():
    assert callable(xhtml_DlType.__init__)


def test_xhtml_dltype_constructor_args():
    sig = inspect.signature(xhtml_DlType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml_dltype_has_title():
    assert hasattr(xhtml_DlType, "title")
    descriptor = None
    for klass in xhtml_DlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dltype_has_style():
    assert hasattr(xhtml_DlType, "style")
    descriptor = None
    for klass in xhtml_DlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dltype_has_id():
    assert hasattr(xhtml_DlType, "id")
    descriptor = None
    for klass in xhtml_DlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dltype_has_class_():
    assert hasattr(xhtml_DlType, "class_")
    descriptor = None
    for klass in xhtml_DlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dltype_has_group():
    assert hasattr(xhtml_DlType, "group")
    descriptor = None
    for klass in xhtml_DlType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_oltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_OlType)


def test_xhtml_oltype_constructor_exists():
    assert callable(xhtml_OlType.__init__)


def test_xhtml_oltype_constructor_args():
    sig = inspect.signature(xhtml_OlType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_oltype_has_id():
    assert hasattr(xhtml_OlType, "id")
    descriptor = None
    for klass in xhtml_OlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_oltype_has_class_():
    assert hasattr(xhtml_OlType, "class_")
    descriptor = None
    for klass in xhtml_OlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_oltype_has_title():
    assert hasattr(xhtml_OlType, "title")
    descriptor = None
    for klass in xhtml_OlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_oltype_has_style():
    assert hasattr(xhtml_OlType, "style")
    descriptor = None
    for klass in xhtml_OlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_block_is_not_abstract():
    assert not inspect.isabstract(xhtml_Block)


def test_xhtml_block_constructor_exists():
    assert callable(xhtml_Block.__init__)


def test_xhtml_block_constructor_args():
    sig = inspect.signature(xhtml_Block.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml_block_has_group():
    assert hasattr(xhtml_Block, "group")
    descriptor = None
    for klass in xhtml_Block.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_acontent_is_not_abstract():
    assert not inspect.isabstract(AContent)


def test_acontent_constructor_exists():
    assert callable(AContent.__init__)


def test_acontent_constructor_args():
    sig = inspect.signature(AContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_atype_is_not_abstract():
    assert not inspect.isabstract(xhtml_AType)


def test_xhtml_atype_constructor_exists():
    assert callable(xhtml_AType.__init__)


def test_xhtml_atype_constructor_args():
    sig = inspect.signature(xhtml_AType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "rel" in params, "Missing parameter 'rel'"
    assert "id" in params, "Missing parameter 'id'"
    assert "href" in params, "Missing parameter 'href'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "coords" in params, "Missing parameter 'coords'"
    assert "rev" in params, "Missing parameter 'rev'"
    assert "name" in params, "Missing parameter 'name'"
    assert "charset" in params, "Missing parameter 'charset'"
    assert "title" in params, "Missing parameter 'title'"
    assert "hreflang" in params, "Missing parameter 'hreflang'"
    assert "style" in params, "Missing parameter 'style'"
    assert "type" in params, "Missing parameter 'type'"

def test_xhtml_atype_has_class_():
    assert hasattr(xhtml_AType, "class_")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_rel():
    assert hasattr(xhtml_AType, "rel")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "rel" in klass.__dict__:
            descriptor = klass.__dict__["rel"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_id():
    assert hasattr(xhtml_AType, "id")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_href():
    assert hasattr(xhtml_AType, "href")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_shape():
    assert hasattr(xhtml_AType, "shape")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_coords():
    assert hasattr(xhtml_AType, "coords")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "coords" in klass.__dict__:
            descriptor = klass.__dict__["coords"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_rev():
    assert hasattr(xhtml_AType, "rev")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "rev" in klass.__dict__:
            descriptor = klass.__dict__["rev"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_name():
    assert hasattr(xhtml_AType, "name")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_charset():
    assert hasattr(xhtml_AType, "charset")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "charset" in klass.__dict__:
            descriptor = klass.__dict__["charset"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_title():
    assert hasattr(xhtml_AType, "title")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_hreflang():
    assert hasattr(xhtml_AType, "hreflang")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "hreflang" in klass.__dict__:
            descriptor = klass.__dict__["hreflang"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_style():
    assert hasattr(xhtml_AType, "style")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_atype_has_type():
    assert hasattr(xhtml_AType, "type")
    descriptor = None
    for klass in xhtml_AType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_instype_is_not_abstract():
    assert not inspect.isabstract(xhtml_InsType)


def test_xhtml_instype_constructor_exists():
    assert callable(xhtml_InsType.__init__)


def test_xhtml_instype_constructor_args():
    sig = inspect.signature(xhtml_InsType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "datetime" in params, "Missing parameter 'datetime'"
    assert "cite1" in params, "Missing parameter 'cite1'"

def test_xhtml_instype_has_title():
    assert hasattr(xhtml_InsType, "title")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_instype_has_style():
    assert hasattr(xhtml_InsType, "style")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_instype_has_class_():
    assert hasattr(xhtml_InsType, "class_")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_instype_has_id():
    assert hasattr(xhtml_InsType, "id")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_instype_has_datetime():
    assert hasattr(xhtml_InsType, "datetime")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "datetime" in klass.__dict__:
            descriptor = klass.__dict__["datetime"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_instype_has_cite1():
    assert hasattr(xhtml_InsType, "cite1")
    descriptor = None
    for klass in xhtml_InsType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_deltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DelType)


def test_xhtml_deltype_constructor_exists():
    assert callable(xhtml_DelType.__init__)


def test_xhtml_deltype_constructor_args():
    sig = inspect.signature(xhtml_DelType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "datetime" in params, "Missing parameter 'datetime'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "cite1" in params, "Missing parameter 'cite1'"

def test_xhtml_deltype_has_title():
    assert hasattr(xhtml_DelType, "title")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_deltype_has_datetime():
    assert hasattr(xhtml_DelType, "datetime")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "datetime" in klass.__dict__:
            descriptor = klass.__dict__["datetime"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_deltype_has_style():
    assert hasattr(xhtml_DelType, "style")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_deltype_has_id():
    assert hasattr(xhtml_DelType, "id")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_deltype_has_class_():
    assert hasattr(xhtml_DelType, "class_")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_deltype_has_cite1():
    assert hasattr(xhtml_DelType, "cite1")
    descriptor = None
    for klass in xhtml_DelType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_imgtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ImgType)


def test_xhtml_imgtype_constructor_exists():
    assert callable(xhtml_ImgType.__init__)


def test_xhtml_imgtype_constructor_args():
    sig = inspect.signature(xhtml_ImgType.__init__)
    params = list(sig.parameters.keys())
    assert "ismap" in params, "Missing parameter 'ismap'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "alt" in params, "Missing parameter 'alt'"
    assert "height" in params, "Missing parameter 'height'"
    assert "longdesc" in params, "Missing parameter 'longdesc'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "src" in params, "Missing parameter 'src'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"

def test_xhtml_imgtype_has_ismap():
    assert hasattr(xhtml_ImgType, "ismap")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_usemap():
    assert hasattr(xhtml_ImgType, "usemap")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_alt():
    assert hasattr(xhtml_ImgType, "alt")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_height():
    assert hasattr(xhtml_ImgType, "height")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_longdesc():
    assert hasattr(xhtml_ImgType, "longdesc")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "longdesc" in klass.__dict__:
            descriptor = klass.__dict__["longdesc"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_style():
    assert hasattr(xhtml_ImgType, "style")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_title():
    assert hasattr(xhtml_ImgType, "title")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_src():
    assert hasattr(xhtml_ImgType, "src")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_id():
    assert hasattr(xhtml_ImgType, "id")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_class_():
    assert hasattr(xhtml_ImgType, "class_")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_imgtype_has_width():
    assert hasattr(xhtml_ImgType, "width")
    descriptor = None
    for klass in xhtml_ImgType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_objecttype_is_not_abstract():
    assert not inspect.isabstract(xhtml_ObjectType)


def test_xhtml_objecttype_constructor_exists():
    assert callable(xhtml_ObjectType.__init__)


def test_xhtml_objecttype_constructor_args():
    sig = inspect.signature(xhtml_ObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "tabindex" in params, "Missing parameter 'tabindex'"
    assert "group" in params, "Missing parameter 'group'"
    assert "type" in params, "Missing parameter 'type'"
    assert "title" in params, "Missing parameter 'title'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "data" in params, "Missing parameter 'data'"
    assert "id" in params, "Missing parameter 'id'"
    assert "classid" in params, "Missing parameter 'classid'"
    assert "standby" in params, "Missing parameter 'standby'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "codebase" in params, "Missing parameter 'codebase'"
    assert "style" in params, "Missing parameter 'style'"
    assert "height" in params, "Missing parameter 'height'"
    assert "declare" in params, "Missing parameter 'declare'"
    assert "codetype" in params, "Missing parameter 'codetype'"
    assert "archive" in params, "Missing parameter 'archive'"
    assert "width" in params, "Missing parameter 'width'"
    assert "name" in params, "Missing parameter 'name'"

def test_xhtml_objecttype_has_tabindex():
    assert hasattr(xhtml_ObjectType, "tabindex")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "tabindex" in klass.__dict__:
            descriptor = klass.__dict__["tabindex"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_group():
    assert hasattr(xhtml_ObjectType, "group")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_type():
    assert hasattr(xhtml_ObjectType, "type")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_title():
    assert hasattr(xhtml_ObjectType, "title")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_mixed():
    assert hasattr(xhtml_ObjectType, "mixed")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_data():
    assert hasattr(xhtml_ObjectType, "data")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_id():
    assert hasattr(xhtml_ObjectType, "id")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_classid():
    assert hasattr(xhtml_ObjectType, "classid")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "classid" in klass.__dict__:
            descriptor = klass.__dict__["classid"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_standby():
    assert hasattr(xhtml_ObjectType, "standby")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "standby" in klass.__dict__:
            descriptor = klass.__dict__["standby"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_usemap():
    assert hasattr(xhtml_ObjectType, "usemap")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_class_():
    assert hasattr(xhtml_ObjectType, "class_")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_codebase():
    assert hasattr(xhtml_ObjectType, "codebase")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "codebase" in klass.__dict__:
            descriptor = klass.__dict__["codebase"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_style():
    assert hasattr(xhtml_ObjectType, "style")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_height():
    assert hasattr(xhtml_ObjectType, "height")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_declare():
    assert hasattr(xhtml_ObjectType, "declare")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "declare" in klass.__dict__:
            descriptor = klass.__dict__["declare"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_codetype():
    assert hasattr(xhtml_ObjectType, "codetype")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "codetype" in klass.__dict__:
            descriptor = klass.__dict__["codetype"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_archive():
    assert hasattr(xhtml_ObjectType, "archive")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "archive" in klass.__dict__:
            descriptor = klass.__dict__["archive"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_width():
    assert hasattr(xhtml_ObjectType, "width")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_objecttype_has_name():
    assert hasattr(xhtml_ObjectType, "name")
    descriptor = None
    for klass in xhtml_ObjectType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_acontent_is_not_abstract():
    assert not inspect.isabstract(xhtml_AContent)


def test_xhtml_acontent_constructor_exists():
    assert callable(xhtml_AContent.__init__)


def test_xhtml_acontent_constructor_args():
    sig = inspect.signature(xhtml_AContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xhtml_acontent_has_group():
    assert hasattr(xhtml_AContent, "group")
    descriptor = None
    for klass in xhtml_AContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_acontent_has_mixed():
    assert hasattr(xhtml_AContent, "mixed")
    descriptor = None
    for klass in xhtml_AContent.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_inline_is_not_abstract():
    assert not inspect.isabstract(Inline)


def test_inline_constructor_exists():
    assert callable(Inline.__init__)


def test_inline_constructor_args():
    sig = inspect.signature(Inline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_dfntype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DfnType)


def test_xhtml_dfntype_constructor_exists():
    assert callable(xhtml_DfnType.__init__)


def test_xhtml_dfntype_constructor_args():
    sig = inspect.signature(xhtml_DfnType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_dfntype_has_id():
    assert hasattr(xhtml_DfnType, "id")
    descriptor = None
    for klass in xhtml_DfnType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dfntype_has_style():
    assert hasattr(xhtml_DfnType, "style")
    descriptor = None
    for klass in xhtml_DfnType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dfntype_has_title():
    assert hasattr(xhtml_DfnType, "title")
    descriptor = None
    for klass in xhtml_DfnType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dfntype_has_class_():
    assert hasattr(xhtml_DfnType, "class_")
    descriptor = None
    for klass in xhtml_DfnType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_ptype_is_not_abstract():
    assert not inspect.isabstract(xhtml_PType)


def test_xhtml_ptype_constructor_exists():
    assert callable(xhtml_PType.__init__)


def test_xhtml_ptype_constructor_args():
    sig = inspect.signature(xhtml_PType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_ptype_has_style():
    assert hasattr(xhtml_PType, "style")
    descriptor = None
    for klass in xhtml_PType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ptype_has_class_():
    assert hasattr(xhtml_PType, "class_")
    descriptor = None
    for klass in xhtml_PType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ptype_has_id():
    assert hasattr(xhtml_PType, "id")
    descriptor = None
    for klass in xhtml_PType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_ptype_has_title():
    assert hasattr(xhtml_PType, "title")
    descriptor = None
    for klass in xhtml_PType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_qtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_QType)


def test_xhtml_qtype_constructor_exists():
    assert callable(xhtml_QType.__init__)


def test_xhtml_qtype_constructor_args():
    sig = inspect.signature(xhtml_QType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "cite1" in params, "Missing parameter 'cite1'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_qtype_has_title():
    assert hasattr(xhtml_QType, "title")
    descriptor = None
    for klass in xhtml_QType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_qtype_has_style():
    assert hasattr(xhtml_QType, "style")
    descriptor = None
    for klass in xhtml_QType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_qtype_has_id():
    assert hasattr(xhtml_QType, "id")
    descriptor = None
    for klass in xhtml_QType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_qtype_has_cite1():
    assert hasattr(xhtml_QType, "cite1")
    descriptor = None
    for klass in xhtml_QType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_qtype_has_class_():
    assert hasattr(xhtml_QType, "class_")
    descriptor = None
    for klass in xhtml_QType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_kbdtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_KbdType)


def test_xhtml_kbdtype_constructor_exists():
    assert callable(xhtml_KbdType.__init__)


def test_xhtml_kbdtype_constructor_args():
    sig = inspect.signature(xhtml_KbdType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_kbdtype_has_title():
    assert hasattr(xhtml_KbdType, "title")
    descriptor = None
    for klass in xhtml_KbdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_kbdtype_has_style():
    assert hasattr(xhtml_KbdType, "style")
    descriptor = None
    for klass in xhtml_KbdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_kbdtype_has_id():
    assert hasattr(xhtml_KbdType, "id")
    descriptor = None
    for klass in xhtml_KbdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_kbdtype_has_class_():
    assert hasattr(xhtml_KbdType, "class_")
    descriptor = None
    for klass in xhtml_KbdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_emtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_EmType)


def test_xhtml_emtype_constructor_exists():
    assert callable(xhtml_EmType.__init__)


def test_xhtml_emtype_constructor_args():
    sig = inspect.signature(xhtml_EmType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_emtype_has_title():
    assert hasattr(xhtml_EmType, "title")
    descriptor = None
    for klass in xhtml_EmType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_emtype_has_class_():
    assert hasattr(xhtml_EmType, "class_")
    descriptor = None
    for klass in xhtml_EmType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_emtype_has_style():
    assert hasattr(xhtml_EmType, "style")
    descriptor = None
    for klass in xhtml_EmType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_emtype_has_id():
    assert hasattr(xhtml_EmType, "id")
    descriptor = None
    for klass in xhtml_EmType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_dttype_is_not_abstract():
    assert not inspect.isabstract(xhtml_DtType)


def test_xhtml_dttype_constructor_exists():
    assert callable(xhtml_DtType.__init__)


def test_xhtml_dttype_constructor_args():
    sig = inspect.signature(xhtml_DtType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_dttype_has_title():
    assert hasattr(xhtml_DtType, "title")
    descriptor = None
    for klass in xhtml_DtType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dttype_has_class_():
    assert hasattr(xhtml_DtType, "class_")
    descriptor = None
    for klass in xhtml_DtType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dttype_has_style():
    assert hasattr(xhtml_DtType, "style")
    descriptor = None
    for klass in xhtml_DtType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_dttype_has_id():
    assert hasattr(xhtml_DtType, "id")
    descriptor = None
    for klass in xhtml_DtType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_acronymtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_AcronymType)


def test_xhtml_acronymtype_constructor_exists():
    assert callable(xhtml_AcronymType.__init__)


def test_xhtml_acronymtype_constructor_args():
    sig = inspect.signature(xhtml_AcronymType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_acronymtype_has_style():
    assert hasattr(xhtml_AcronymType, "style")
    descriptor = None
    for klass in xhtml_AcronymType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_acronymtype_has_id():
    assert hasattr(xhtml_AcronymType, "id")
    descriptor = None
    for klass in xhtml_AcronymType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_acronymtype_has_title():
    assert hasattr(xhtml_AcronymType, "title")
    descriptor = None
    for klass in xhtml_AcronymType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_acronymtype_has_class_():
    assert hasattr(xhtml_AcronymType, "class_")
    descriptor = None
    for klass in xhtml_AcronymType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_bigtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_BigType)


def test_xhtml_bigtype_constructor_exists():
    assert callable(xhtml_BigType.__init__)


def test_xhtml_bigtype_constructor_args():
    sig = inspect.signature(xhtml_BigType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_bigtype_has_class_():
    assert hasattr(xhtml_BigType, "class_")
    descriptor = None
    for klass in xhtml_BigType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bigtype_has_id():
    assert hasattr(xhtml_BigType, "id")
    descriptor = None
    for klass in xhtml_BigType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bigtype_has_title():
    assert hasattr(xhtml_BigType, "title")
    descriptor = None
    for klass in xhtml_BigType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_bigtype_has_style():
    assert hasattr(xhtml_BigType, "style")
    descriptor = None
    for klass in xhtml_BigType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_tttype_is_not_abstract():
    assert not inspect.isabstract(xhtml_TtType)


def test_xhtml_tttype_constructor_exists():
    assert callable(xhtml_TtType.__init__)


def test_xhtml_tttype_constructor_args():
    sig = inspect.signature(xhtml_TtType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_tttype_has_id():
    assert hasattr(xhtml_TtType, "id")
    descriptor = None
    for klass in xhtml_TtType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tttype_has_style():
    assert hasattr(xhtml_TtType, "style")
    descriptor = None
    for klass in xhtml_TtType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tttype_has_title():
    assert hasattr(xhtml_TtType, "title")
    descriptor = None
    for klass in xhtml_TtType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_tttype_has_class_():
    assert hasattr(xhtml_TtType, "class_")
    descriptor = None
    for klass in xhtml_TtType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h6type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H6Type)


def test_xhtml_h6type_constructor_exists():
    assert callable(xhtml_H6Type.__init__)


def test_xhtml_h6type_constructor_args():
    sig = inspect.signature(xhtml_H6Type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_h6type_has_id():
    assert hasattr(xhtml_H6Type, "id")
    descriptor = None
    for klass in xhtml_H6Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h6type_has_class_():
    assert hasattr(xhtml_H6Type, "class_")
    descriptor = None
    for klass in xhtml_H6Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h6type_has_style():
    assert hasattr(xhtml_H6Type, "style")
    descriptor = None
    for klass in xhtml_H6Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h6type_has_title():
    assert hasattr(xhtml_H6Type, "title")
    descriptor = None
    for klass in xhtml_H6Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h2type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H2Type)


def test_xhtml_h2type_constructor_exists():
    assert callable(xhtml_H2Type.__init__)


def test_xhtml_h2type_constructor_args():
    sig = inspect.signature(xhtml_H2Type.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_h2type_has_style():
    assert hasattr(xhtml_H2Type, "style")
    descriptor = None
    for klass in xhtml_H2Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h2type_has_class_():
    assert hasattr(xhtml_H2Type, "class_")
    descriptor = None
    for klass in xhtml_H2Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h2type_has_title():
    assert hasattr(xhtml_H2Type, "title")
    descriptor = None
    for klass in xhtml_H2Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h2type_has_id():
    assert hasattr(xhtml_H2Type, "id")
    descriptor = None
    for klass in xhtml_H2Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_strongtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_StrongType)


def test_xhtml_strongtype_constructor_exists():
    assert callable(xhtml_StrongType.__init__)


def test_xhtml_strongtype_constructor_args():
    sig = inspect.signature(xhtml_StrongType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_strongtype_has_style():
    assert hasattr(xhtml_StrongType, "style")
    descriptor = None
    for klass in xhtml_StrongType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_strongtype_has_title():
    assert hasattr(xhtml_StrongType, "title")
    descriptor = None
    for klass in xhtml_StrongType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_strongtype_has_id():
    assert hasattr(xhtml_StrongType, "id")
    descriptor = None
    for klass in xhtml_StrongType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_strongtype_has_class_():
    assert hasattr(xhtml_StrongType, "class_")
    descriptor = None
    for klass in xhtml_StrongType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_samptype_is_not_abstract():
    assert not inspect.isabstract(xhtml_SampType)


def test_xhtml_samptype_constructor_exists():
    assert callable(xhtml_SampType.__init__)


def test_xhtml_samptype_constructor_args():
    sig = inspect.signature(xhtml_SampType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_samptype_has_class_():
    assert hasattr(xhtml_SampType, "class_")
    descriptor = None
    for klass in xhtml_SampType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_samptype_has_style():
    assert hasattr(xhtml_SampType, "style")
    descriptor = None
    for klass in xhtml_SampType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_samptype_has_title():
    assert hasattr(xhtml_SampType, "title")
    descriptor = None
    for klass in xhtml_SampType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_samptype_has_id():
    assert hasattr(xhtml_SampType, "id")
    descriptor = None
    for klass in xhtml_SampType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_itype_is_not_abstract():
    assert not inspect.isabstract(xhtml_IType)


def test_xhtml_itype_constructor_exists():
    assert callable(xhtml_IType.__init__)


def test_xhtml_itype_constructor_args():
    sig = inspect.signature(xhtml_IType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_itype_has_style():
    assert hasattr(xhtml_IType, "style")
    descriptor = None
    for klass in xhtml_IType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_itype_has_id():
    assert hasattr(xhtml_IType, "id")
    descriptor = None
    for klass in xhtml_IType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_itype_has_class_():
    assert hasattr(xhtml_IType, "class_")
    descriptor = None
    for klass in xhtml_IType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_itype_has_title():
    assert hasattr(xhtml_IType, "title")
    descriptor = None
    for klass in xhtml_IType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_addresstype_is_not_abstract():
    assert not inspect.isabstract(xhtml_AddressType)


def test_xhtml_addresstype_constructor_exists():
    assert callable(xhtml_AddressType.__init__)


def test_xhtml_addresstype_constructor_args():
    sig = inspect.signature(xhtml_AddressType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_addresstype_has_class_():
    assert hasattr(xhtml_AddressType, "class_")
    descriptor = None
    for klass in xhtml_AddressType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_addresstype_has_style():
    assert hasattr(xhtml_AddressType, "style")
    descriptor = None
    for klass in xhtml_AddressType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_addresstype_has_title():
    assert hasattr(xhtml_AddressType, "title")
    descriptor = None
    for klass in xhtml_AddressType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_addresstype_has_id():
    assert hasattr(xhtml_AddressType, "id")
    descriptor = None
    for klass in xhtml_AddressType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_citetype_is_not_abstract():
    assert not inspect.isabstract(xhtml_CiteType)


def test_xhtml_citetype_constructor_exists():
    assert callable(xhtml_CiteType.__init__)


def test_xhtml_citetype_constructor_args():
    sig = inspect.signature(xhtml_CiteType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_citetype_has_style():
    assert hasattr(xhtml_CiteType, "style")
    descriptor = None
    for klass in xhtml_CiteType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_citetype_has_class_():
    assert hasattr(xhtml_CiteType, "class_")
    descriptor = None
    for klass in xhtml_CiteType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_citetype_has_title():
    assert hasattr(xhtml_CiteType, "title")
    descriptor = None
    for klass in xhtml_CiteType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_citetype_has_id():
    assert hasattr(xhtml_CiteType, "id")
    descriptor = None
    for klass in xhtml_CiteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_btype_is_not_abstract():
    assert not inspect.isabstract(xhtml_BType)


def test_xhtml_btype_constructor_exists():
    assert callable(xhtml_BType.__init__)


def test_xhtml_btype_constructor_args():
    sig = inspect.signature(xhtml_BType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_btype_has_id():
    assert hasattr(xhtml_BType, "id")
    descriptor = None
    for klass in xhtml_BType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_btype_has_title():
    assert hasattr(xhtml_BType, "title")
    descriptor = None
    for klass in xhtml_BType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_btype_has_style():
    assert hasattr(xhtml_BType, "style")
    descriptor = None
    for klass in xhtml_BType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_btype_has_class_():
    assert hasattr(xhtml_BType, "class_")
    descriptor = None
    for klass in xhtml_BType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h5type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H5Type)


def test_xhtml_h5type_constructor_exists():
    assert callable(xhtml_H5Type.__init__)


def test_xhtml_h5type_constructor_args():
    sig = inspect.signature(xhtml_H5Type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_h5type_has_id():
    assert hasattr(xhtml_H5Type, "id")
    descriptor = None
    for klass in xhtml_H5Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h5type_has_style():
    assert hasattr(xhtml_H5Type, "style")
    descriptor = None
    for klass in xhtml_H5Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h5type_has_class_():
    assert hasattr(xhtml_H5Type, "class_")
    descriptor = None
    for klass in xhtml_H5Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h5type_has_title():
    assert hasattr(xhtml_H5Type, "title")
    descriptor = None
    for klass in xhtml_H5Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h1type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H1Type)


def test_xhtml_h1type_constructor_exists():
    assert callable(xhtml_H1Type.__init__)


def test_xhtml_h1type_constructor_args():
    sig = inspect.signature(xhtml_H1Type.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_h1type_has_title():
    assert hasattr(xhtml_H1Type, "title")
    descriptor = None
    for klass in xhtml_H1Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h1type_has_class_():
    assert hasattr(xhtml_H1Type, "class_")
    descriptor = None
    for klass in xhtml_H1Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h1type_has_id():
    assert hasattr(xhtml_H1Type, "id")
    descriptor = None
    for klass in xhtml_H1Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h1type_has_style():
    assert hasattr(xhtml_H1Type, "style")
    descriptor = None
    for klass in xhtml_H1Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h3type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H3Type)


def test_xhtml_h3type_constructor_exists():
    assert callable(xhtml_H3Type.__init__)


def test_xhtml_h3type_constructor_args():
    sig = inspect.signature(xhtml_H3Type.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_h3type_has_title():
    assert hasattr(xhtml_H3Type, "title")
    descriptor = None
    for klass in xhtml_H3Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h3type_has_class_():
    assert hasattr(xhtml_H3Type, "class_")
    descriptor = None
    for klass in xhtml_H3Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h3type_has_id():
    assert hasattr(xhtml_H3Type, "id")
    descriptor = None
    for klass in xhtml_H3Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h3type_has_style():
    assert hasattr(xhtml_H3Type, "style")
    descriptor = None
    for klass in xhtml_H3Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_vartype_is_not_abstract():
    assert not inspect.isabstract(xhtml_VarType)


def test_xhtml_vartype_constructor_exists():
    assert callable(xhtml_VarType.__init__)


def test_xhtml_vartype_constructor_args():
    sig = inspect.signature(xhtml_VarType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_vartype_has_id():
    assert hasattr(xhtml_VarType, "id")
    descriptor = None
    for klass in xhtml_VarType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_vartype_has_style():
    assert hasattr(xhtml_VarType, "style")
    descriptor = None
    for klass in xhtml_VarType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_vartype_has_class_():
    assert hasattr(xhtml_VarType, "class_")
    descriptor = None
    for klass in xhtml_VarType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_vartype_has_title():
    assert hasattr(xhtml_VarType, "title")
    descriptor = None
    for klass in xhtml_VarType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_smalltype_is_not_abstract():
    assert not inspect.isabstract(xhtml_SmallType)


def test_xhtml_smalltype_constructor_exists():
    assert callable(xhtml_SmallType.__init__)


def test_xhtml_smalltype_constructor_args():
    sig = inspect.signature(xhtml_SmallType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_smalltype_has_title():
    assert hasattr(xhtml_SmallType, "title")
    descriptor = None
    for klass in xhtml_SmallType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_smalltype_has_style():
    assert hasattr(xhtml_SmallType, "style")
    descriptor = None
    for klass in xhtml_SmallType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_smalltype_has_class_():
    assert hasattr(xhtml_SmallType, "class_")
    descriptor = None
    for klass in xhtml_SmallType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_smalltype_has_id():
    assert hasattr(xhtml_SmallType, "id")
    descriptor = None
    for klass in xhtml_SmallType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_utype_is_not_abstract():
    assert not inspect.isabstract(xhtml_UType)


def test_xhtml_utype_constructor_exists():
    assert callable(xhtml_UType.__init__)


def test_xhtml_utype_constructor_args():
    sig = inspect.signature(xhtml_UType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_utype_has_class_():
    assert hasattr(xhtml_UType, "class_")
    descriptor = None
    for klass in xhtml_UType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_utype_has_id():
    assert hasattr(xhtml_UType, "id")
    descriptor = None
    for klass in xhtml_UType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_utype_has_style():
    assert hasattr(xhtml_UType, "style")
    descriptor = None
    for klass in xhtml_UType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_utype_has_title():
    assert hasattr(xhtml_UType, "title")
    descriptor = None
    for klass in xhtml_UType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_striketype_is_not_abstract():
    assert not inspect.isabstract(xhtml_StrikeType)


def test_xhtml_striketype_constructor_exists():
    assert callable(xhtml_StrikeType.__init__)


def test_xhtml_striketype_constructor_args():
    sig = inspect.signature(xhtml_StrikeType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_striketype_has_title():
    assert hasattr(xhtml_StrikeType, "title")
    descriptor = None
    for klass in xhtml_StrikeType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_striketype_has_style():
    assert hasattr(xhtml_StrikeType, "style")
    descriptor = None
    for klass in xhtml_StrikeType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_striketype_has_id():
    assert hasattr(xhtml_StrikeType, "id")
    descriptor = None
    for klass in xhtml_StrikeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_striketype_has_class_():
    assert hasattr(xhtml_StrikeType, "class_")
    descriptor = None
    for klass in xhtml_StrikeType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_subtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_SubType)


def test_xhtml_subtype_constructor_exists():
    assert callable(xhtml_SubType.__init__)


def test_xhtml_subtype_constructor_args():
    sig = inspect.signature(xhtml_SubType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml_subtype_has_class_():
    assert hasattr(xhtml_SubType, "class_")
    descriptor = None
    for klass in xhtml_SubType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_subtype_has_style():
    assert hasattr(xhtml_SubType, "style")
    descriptor = None
    for klass in xhtml_SubType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_subtype_has_id():
    assert hasattr(xhtml_SubType, "id")
    descriptor = None
    for klass in xhtml_SubType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_subtype_has_title():
    assert hasattr(xhtml_SubType, "title")
    descriptor = None
    for klass in xhtml_SubType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_captiontype_is_not_abstract():
    assert not inspect.isabstract(xhtml_CaptionType)


def test_xhtml_captiontype_constructor_exists():
    assert callable(xhtml_CaptionType.__init__)


def test_xhtml_captiontype_constructor_args():
    sig = inspect.signature(xhtml_CaptionType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_captiontype_has_class_():
    assert hasattr(xhtml_CaptionType, "class_")
    descriptor = None
    for klass in xhtml_CaptionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_captiontype_has_title():
    assert hasattr(xhtml_CaptionType, "title")
    descriptor = None
    for klass in xhtml_CaptionType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_captiontype_has_style():
    assert hasattr(xhtml_CaptionType, "style")
    descriptor = None
    for klass in xhtml_CaptionType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_captiontype_has_id():
    assert hasattr(xhtml_CaptionType, "id")
    descriptor = None
    for klass in xhtml_CaptionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h4type_is_not_abstract():
    assert not inspect.isabstract(xhtml_H4Type)


def test_xhtml_h4type_constructor_exists():
    assert callable(xhtml_H4Type.__init__)


def test_xhtml_h4type_constructor_args():
    sig = inspect.signature(xhtml_H4Type.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_h4type_has_style():
    assert hasattr(xhtml_H4Type, "style")
    descriptor = None
    for klass in xhtml_H4Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h4type_has_title():
    assert hasattr(xhtml_H4Type, "title")
    descriptor = None
    for klass in xhtml_H4Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h4type_has_class_():
    assert hasattr(xhtml_H4Type, "class_")
    descriptor = None
    for klass in xhtml_H4Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_h4type_has_id():
    assert hasattr(xhtml_H4Type, "id")
    descriptor = None
    for klass in xhtml_H4Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_codetype_is_not_abstract():
    assert not inspect.isabstract(xhtml_CodeType)


def test_xhtml_codetype_constructor_exists():
    assert callable(xhtml_CodeType.__init__)


def test_xhtml_codetype_constructor_args():
    sig = inspect.signature(xhtml_CodeType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml_codetype_has_style():
    assert hasattr(xhtml_CodeType, "style")
    descriptor = None
    for klass in xhtml_CodeType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_codetype_has_title():
    assert hasattr(xhtml_CodeType, "title")
    descriptor = None
    for klass in xhtml_CodeType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_codetype_has_class_():
    assert hasattr(xhtml_CodeType, "class_")
    descriptor = None
    for klass in xhtml_CodeType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_codetype_has_id():
    assert hasattr(xhtml_CodeType, "id")
    descriptor = None
    for klass in xhtml_CodeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_suptype_is_not_abstract():
    assert not inspect.isabstract(xhtml_SupType)


def test_xhtml_suptype_constructor_exists():
    assert callable(xhtml_SupType.__init__)


def test_xhtml_suptype_constructor_args():
    sig = inspect.signature(xhtml_SupType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml_suptype_has_class_():
    assert hasattr(xhtml_SupType, "class_")
    descriptor = None
    for klass in xhtml_SupType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_suptype_has_id():
    assert hasattr(xhtml_SupType, "id")
    descriptor = None
    for klass in xhtml_SupType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_suptype_has_title():
    assert hasattr(xhtml_SupType, "title")
    descriptor = None
    for klass in xhtml_SupType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_suptype_has_style():
    assert hasattr(xhtml_SupType, "style")
    descriptor = None
    for klass in xhtml_SupType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_abbrtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_AbbrType)


def test_xhtml_abbrtype_constructor_exists():
    assert callable(xhtml_AbbrType.__init__)


def test_xhtml_abbrtype_constructor_args():
    sig = inspect.signature(xhtml_AbbrType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_abbrtype_has_id():
    assert hasattr(xhtml_AbbrType, "id")
    descriptor = None
    for klass in xhtml_AbbrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_abbrtype_has_style():
    assert hasattr(xhtml_AbbrType, "style")
    descriptor = None
    for klass in xhtml_AbbrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_abbrtype_has_title():
    assert hasattr(xhtml_AbbrType, "title")
    descriptor = None
    for klass in xhtml_AbbrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_abbrtype_has_class_():
    assert hasattr(xhtml_AbbrType, "class_")
    descriptor = None
    for klass in xhtml_AbbrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_spantype_is_not_abstract():
    assert not inspect.isabstract(xhtml_SpanType)


def test_xhtml_spantype_constructor_exists():
    assert callable(xhtml_SpanType.__init__)


def test_xhtml_spantype_constructor_args():
    sig = inspect.signature(xhtml_SpanType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_spantype_has_style():
    assert hasattr(xhtml_SpanType, "style")
    descriptor = None
    for klass in xhtml_SpanType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_spantype_has_title():
    assert hasattr(xhtml_SpanType, "title")
    descriptor = None
    for klass in xhtml_SpanType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_spantype_has_id():
    assert hasattr(xhtml_SpanType, "id")
    descriptor = None
    for klass in xhtml_SpanType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_spantype_has_class_():
    assert hasattr(xhtml_SpanType, "class_")
    descriptor = None
    for klass in xhtml_SpanType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_brtype_is_not_abstract():
    assert not inspect.isabstract(xhtml_BrType)


def test_xhtml_brtype_constructor_exists():
    assert callable(xhtml_BrType.__init__)


def test_xhtml_brtype_constructor_args():
    sig = inspect.signature(xhtml_BrType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml_brtype_has_title():
    assert hasattr(xhtml_BrType, "title")
    descriptor = None
    for klass in xhtml_BrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_brtype_has_style():
    assert hasattr(xhtml_BrType, "style")
    descriptor = None
    for klass in xhtml_BrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_brtype_has_id():
    assert hasattr(xhtml_BrType, "id")
    descriptor = None
    for klass in xhtml_BrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_brtype_has_class_():
    assert hasattr(xhtml_BrType, "class_")
    descriptor = None
    for klass in xhtml_BrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_valuetypetype_exists():
    # Check that the Enumeration exists
    assert ValuetypeType is not None

def test_valuetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValuetypeType]
    expected_literals = [
        "data",
        "ref",
        "object",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValuetypeType"

def test_valigntype_exists():
    # Check that the Enumeration exists
    assert ValignType is not None

def test_valigntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValignType]
    expected_literals = [
        "middle",
        "top",
        "baseline",
        "bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValignType"

def test_aligntype_exists():
    # Check that the Enumeration exists
    assert AlignType is not None

def test_aligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignType]
    expected_literals = [
        "left",
        "right",
        "char",
        "center",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignType"

def test_declaretype_exists():
    # Check that the Enumeration exists
    assert DeclareType is not None

def test_declaretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeclareType]
    expected_literals = [
        "declare",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeclareType"

def test_shape_exists():
    # Check that the Enumeration exists
    assert Shape is not None

def test_shape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Shape]
    expected_literals = [
        "circle",
        "rect",
        "default",
        "poly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Shape"

def test_ismaptype_exists():
    # Check that the Enumeration exists
    assert IsmapType is not None

def test_ismaptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IsmapType]
    expected_literals = [
        "ismap",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IsmapType"

def test_scope_exists():
    # Check that the Enumeration exists
    assert Scope is not None

def test_scope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Scope]
    expected_literals = [
        "row",
        "col",
        "colgroup",
        "rowgroup",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Scope"


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
PreContent_strategy = st.builds(
    PreContent,
)
xhtml_PreContent_strategy = st.builds(
    xhtml_PreContent,
    mixed=
        safe_text,
    group=
        safe_text
)
xhtml_Inline_strategy = st.builds(
    xhtml_Inline,
    mixed=
        safe_text,
    group=
        safe_text
)
xhtml_FormContent_strategy = st.builds(
    xhtml_FormContent,
    group=
        safe_text
)
xhtml_Flow_strategy = st.builds(
    xhtml_Flow,
    group=
        safe_text,
    mixed=
        safe_text
)
xhtml_TbodyType_strategy = st.builds(
    xhtml_TbodyType,
    char=
        safe_text,
    style=
        safe_text,
    align=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    valign=
        safe_text,
    charoff=
        safe_text,
    title=
        safe_text
)
xhtml_TrType_strategy = st.builds(
    xhtml_TrType,
    valign=
        safe_text,
    title=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    group=
        safe_text,
    charoff=
        safe_text,
    style=
        safe_text,
    align=
        safe_text
)
xhtml_TheadType_strategy = st.builds(
    xhtml_TheadType,
    align=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    char=
        safe_text,
    valign=
        safe_text,
    charoff=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_TfootType_strategy = st.builds(
    xhtml_TfootType,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    align=
        safe_text,
    charoff=
        safe_text,
    id=
        safe_text,
    valign=
        safe_text,
    char=
        safe_text
)
xhtml_ParamType_strategy = st.builds(
    xhtml_ParamType,
    valuetype=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    value=
        safe_text,
    id=
        safe_text
)
xhtml_HtmlType_strategy = st.builds(
    xhtml_HtmlType,
    id=
        safe_text
)
xhtml_EStringToStringMapEntry_strategy = st.builds(
    xhtml_EStringToStringMapEntry,
)
xhtml_DocumentRoot_strategy = st.builds(
    xhtml_DocumentRoot,
    mixed=
        safe_text
)
Flow_strategy = st.builds(
    Flow,
)
xhtml_TdType_strategy = st.builds(
    xhtml_TdType,
    charoff=
        safe_text,
    id=
        safe_text,
    colspan=
        safe_text,
    class_=
        safe_text,
    align=
        safe_text,
    style=
        safe_text,
    char=
        safe_text,
    headers=
        safe_text,
    rowspan=
        safe_text,
    title=
        safe_text,
    scope=
        safe_text,
    valign=
        safe_text,
    axis=
        safe_text,
    abbr1=
        safe_text
)
xhtml_LiType_strategy = st.builds(
    xhtml_LiType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_ThType_strategy = st.builds(
    xhtml_ThType,
    class_=
        safe_text,
    char=
        safe_text,
    colspan=
        safe_text,
    charoff=
        safe_text,
    headers=
        safe_text,
    style=
        safe_text,
    axis=
        safe_text,
    scope=
        safe_text,
    rowspan=
        safe_text,
    align=
        safe_text,
    abbr1=
        safe_text,
    valign=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml_DdType_strategy = st.builds(
    xhtml_DdType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml_ColType_strategy = st.builds(
    xhtml_ColType,
    char=
        safe_text,
    class_=
        safe_text,
    charoff=
        safe_text,
    width=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    id=
        safe_text,
    span=
        safe_text
)
xhtml_ColgroupType_strategy = st.builds(
    xhtml_ColgroupType,
    id=
        safe_text,
    align=
        safe_text,
    class_=
        safe_text,
    valign=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    char=
        safe_text,
    width=
        safe_text,
    span=
        safe_text,
    charoff=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
xhtml_BodyType_strategy = st.builds(
    xhtml_BodyType,
    id=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_BlockquoteType_strategy = st.builds(
    xhtml_BlockquoteType,
    title=
        safe_text,
    cite=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_HrType_strategy = st.builds(
    xhtml_HrType,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml_PreType_strategy = st.builds(
    xhtml_PreType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_TableType_strategy = st.builds(
    xhtml_TableType,
    title=
        safe_text,
    cellpadding=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text,
    summary=
        safe_text,
    cellspacing=
        safe_text,
    style=
        safe_text,
    border=
        safe_text
)
xhtml_UlType_strategy = st.builds(
    xhtml_UlType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml_DivType_strategy = st.builds(
    xhtml_DivType,
    id=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml_DlType_strategy = st.builds(
    xhtml_DlType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    group=
        safe_text
)
xhtml_OlType_strategy = st.builds(
    xhtml_OlType,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text
)
xhtml_Block_strategy = st.builds(
    xhtml_Block,
    group=
        safe_text
)
AContent_strategy = st.builds(
    AContent,
)
xhtml_AType_strategy = st.builds(
    xhtml_AType,
    class_=
        safe_text,
    rel=
        safe_text,
    id=
        safe_text,
    href=
        safe_text,
    shape=
        safe_text,
    coords=
        safe_text,
    rev=
        safe_text,
    name=
        safe_text,
    charset=
        safe_text,
    title=
        safe_text,
    hreflang=
        safe_text,
    style=
        safe_text,
    type=
        safe_text
)
xhtml_InsType_strategy = st.builds(
    xhtml_InsType,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    datetime=
        safe_text,
    cite1=
        safe_text
)
xhtml_DelType_strategy = st.builds(
    xhtml_DelType,
    title=
        safe_text,
    datetime=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    cite1=
        safe_text
)
xhtml_ImgType_strategy = st.builds(
    xhtml_ImgType,
    ismap=
        safe_text,
    usemap=
        safe_text,
    alt=
        safe_text,
    height=
        safe_text,
    longdesc=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    src=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text
)
xhtml_ObjectType_strategy = st.builds(
    xhtml_ObjectType,
    tabindex=
        safe_text,
    group=
        safe_text,
    type=
        safe_text,
    title=
        safe_text,
    mixed=
        safe_text,
    data=
        safe_text,
    id=
        safe_text,
    classid=
        safe_text,
    standby=
        safe_text,
    usemap=
        safe_text,
    class_=
        safe_text,
    codebase=
        safe_text,
    style=
        safe_text,
    height=
        safe_text,
    declare=
        safe_text,
    codetype=
        safe_text,
    archive=
        safe_text,
    width=
        safe_text,
    name=
        safe_text
)
xhtml_AContent_strategy = st.builds(
    xhtml_AContent,
    group=
        safe_text,
    mixed=
        safe_text
)
Inline_strategy = st.builds(
    Inline,
)
xhtml_DfnType_strategy = st.builds(
    xhtml_DfnType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_PType_strategy = st.builds(
    xhtml_PType,
    style=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    title=
        safe_text
)
xhtml_QType_strategy = st.builds(
    xhtml_QType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    cite1=
        safe_text,
    class_=
        safe_text
)
xhtml_KbdType_strategy = st.builds(
    xhtml_KbdType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml_EmType_strategy = st.builds(
    xhtml_EmType,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml_DtType_strategy = st.builds(
    xhtml_DtType,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml_AcronymType_strategy = st.builds(
    xhtml_AcronymType,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_BigType_strategy = st.builds(
    xhtml_BigType,
    class_=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    style=
        safe_text
)
xhtml_TtType_strategy = st.builds(
    xhtml_TtType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_H6Type_strategy = st.builds(
    xhtml_H6Type,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text
)
xhtml_H2Type_strategy = st.builds(
    xhtml_H2Type,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml_StrongType_strategy = st.builds(
    xhtml_StrongType,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml_SampType_strategy = st.builds(
    xhtml_SampType,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml_IType_strategy = st.builds(
    xhtml_IType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml_AddressType_strategy = st.builds(
    xhtml_AddressType,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml_CiteType_strategy = st.builds(
    xhtml_CiteType,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml_BType_strategy = st.builds(
    xhtml_BType,
    id=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml_H5Type_strategy = st.builds(
    xhtml_H5Type,
    id=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml_H1Type_strategy = st.builds(
    xhtml_H1Type,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml_H3Type_strategy = st.builds(
    xhtml_H3Type,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml_VarType_strategy = st.builds(
    xhtml_VarType,
    id=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml_SmallType_strategy = st.builds(
    xhtml_SmallType,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml_UType_strategy = st.builds(
    xhtml_UType,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text
)
xhtml_StrikeType_strategy = st.builds(
    xhtml_StrikeType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml_SubType_strategy = st.builds(
    xhtml_SubType,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text
)
xhtml_CaptionType_strategy = st.builds(
    xhtml_CaptionType,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml_H4Type_strategy = st.builds(
    xhtml_H4Type,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml_CodeType_strategy = st.builds(
    xhtml_CodeType,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml_SupType_strategy = st.builds(
    xhtml_SupType,
    class_=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    style=
        safe_text
)
xhtml_AbbrType_strategy = st.builds(
    xhtml_AbbrType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml_SpanType_strategy = st.builds(
    xhtml_SpanType,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml_BrType_strategy = st.builds(
    xhtml_BrType,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)

@given(instance=PreContent_strategy)
@settings(max_examples=50)
def test_precontent_instantiation(instance):
    assert isinstance(instance, PreContent)

@given(instance=xhtml_PreContent_strategy)
@settings(max_examples=50)
def test_xhtml_precontent_instantiation(instance):
    assert isinstance(instance, xhtml_PreContent)



@given(instance=xhtml_PreContent_strategy)
def test_xhtml_precontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_PreContent_strategy)
def test_xhtml_precontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml_Inline_strategy)
@settings(max_examples=50)
def test_xhtml_inline_instantiation(instance):
    assert isinstance(instance, xhtml_Inline)



@given(instance=xhtml_Inline_strategy)
def test_xhtml_inline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_Inline_strategy)
def test_xhtml_inline_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml_FormContent_strategy)
@settings(max_examples=50)
def test_xhtml_formcontent_instantiation(instance):
    assert isinstance(instance, xhtml_FormContent)



@given(instance=xhtml_FormContent_strategy)
def test_xhtml_formcontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml_Flow_strategy)
@settings(max_examples=50)
def test_xhtml_flow_instantiation(instance):
    assert isinstance(instance, xhtml_Flow)



@given(instance=xhtml_Flow_strategy)
def test_xhtml_flow_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_Flow_strategy)
def test_xhtml_flow_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml_TbodyType_strategy)
@settings(max_examples=50)
def test_xhtml_tbodytype_instantiation(instance):
    assert isinstance(instance, xhtml_TbodyType)



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_TbodyType_strategy)
def test_xhtml_tbodytype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_TrType_strategy)
@settings(max_examples=50)
def test_xhtml_trtype_instantiation(instance):
    assert isinstance(instance, xhtml_TrType)



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TrType_strategy)
def test_xhtml_trtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml_TheadType_strategy)
@settings(max_examples=50)
def test_xhtml_theadtype_instantiation(instance):
    assert isinstance(instance, xhtml_TheadType)



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TheadType_strategy)
def test_xhtml_theadtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_TfootType_strategy)
@settings(max_examples=50)
def test_xhtml_tfoottype_instantiation(instance):
    assert isinstance(instance, xhtml_TfootType)



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_TfootType_strategy)
def test_xhtml_tfoottype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml_ParamType_strategy)
@settings(max_examples=50)
def test_xhtml_paramtype_instantiation(instance):
    assert isinstance(instance, xhtml_ParamType)



@given(instance=xhtml_ParamType_strategy)
def test_xhtml_paramtype_valuetype_setter(instance):
    original = instance.valuetype
    instance.valuetype = original
    assert instance.valuetype == original



@given(instance=xhtml_ParamType_strategy)
def test_xhtml_paramtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xhtml_ParamType_strategy)
def test_xhtml_paramtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xhtml_ParamType_strategy)
def test_xhtml_paramtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xhtml_ParamType_strategy)
def test_xhtml_paramtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_HtmlType_strategy)
@settings(max_examples=50)
def test_xhtml_htmltype_instantiation(instance):
    assert isinstance(instance, xhtml_HtmlType)



@given(instance=xhtml_HtmlType_strategy)
def test_xhtml_htmltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xhtml_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xhtml_EStringToStringMapEntry)

@given(instance=xhtml_DocumentRoot_strategy)
@settings(max_examples=50)
def test_xhtml_documentroot_instantiation(instance):
    assert isinstance(instance, xhtml_DocumentRoot)



@given(instance=xhtml_DocumentRoot_strategy)
def test_xhtml_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=xhtml_TdType_strategy)
@settings(max_examples=50)
def test_xhtml_tdtype_instantiation(instance):
    assert isinstance(instance, xhtml_TdType)



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_headers_setter(instance):
    original = instance.headers
    instance.headers = original
    assert instance.headers == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original



@given(instance=xhtml_TdType_strategy)
def test_xhtml_tdtype_abbr1_setter(instance):
    original = instance.abbr1
    instance.abbr1 = original
    assert instance.abbr1 == original

@given(instance=xhtml_LiType_strategy)
@settings(max_examples=50)
def test_xhtml_litype_instantiation(instance):
    assert isinstance(instance, xhtml_LiType)



@given(instance=xhtml_LiType_strategy)
def test_xhtml_litype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_LiType_strategy)
def test_xhtml_litype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_LiType_strategy)
def test_xhtml_litype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_LiType_strategy)
def test_xhtml_litype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_ThType_strategy)
@settings(max_examples=50)
def test_xhtml_thtype_instantiation(instance):
    assert isinstance(instance, xhtml_ThType)



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_headers_setter(instance):
    original = instance.headers
    instance.headers = original
    assert instance.headers == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_abbr1_setter(instance):
    original = instance.abbr1
    instance.abbr1 = original
    assert instance.abbr1 == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_ThType_strategy)
def test_xhtml_thtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_DdType_strategy)
@settings(max_examples=50)
def test_xhtml_ddtype_instantiation(instance):
    assert isinstance(instance, xhtml_DdType)



@given(instance=xhtml_DdType_strategy)
def test_xhtml_ddtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_DdType_strategy)
def test_xhtml_ddtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_DdType_strategy)
def test_xhtml_ddtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_DdType_strategy)
def test_xhtml_ddtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_ColType_strategy)
@settings(max_examples=50)
def test_xhtml_coltype_instantiation(instance):
    assert isinstance(instance, xhtml_ColType)



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_ColType_strategy)
def test_xhtml_coltype_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=xhtml_ColgroupType_strategy)
@settings(max_examples=50)
def test_xhtml_colgrouptype_instantiation(instance):
    assert isinstance(instance, xhtml_ColgroupType)



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original



@given(instance=xhtml_ColgroupType_strategy)
def test_xhtml_colgrouptype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=xhtml_BodyType_strategy)
@settings(max_examples=50)
def test_xhtml_bodytype_instantiation(instance):
    assert isinstance(instance, xhtml_BodyType)



@given(instance=xhtml_BodyType_strategy)
def test_xhtml_bodytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_BodyType_strategy)
def test_xhtml_bodytype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_BodyType_strategy)
def test_xhtml_bodytype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_BodyType_strategy)
def test_xhtml_bodytype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_BlockquoteType_strategy)
@settings(max_examples=50)
def test_xhtml_blockquotetype_instantiation(instance):
    assert isinstance(instance, xhtml_BlockquoteType)



@given(instance=xhtml_BlockquoteType_strategy)
def test_xhtml_blockquotetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_BlockquoteType_strategy)
def test_xhtml_blockquotetype_cite_setter(instance):
    original = instance.cite
    instance.cite = original
    assert instance.cite == original



@given(instance=xhtml_BlockquoteType_strategy)
def test_xhtml_blockquotetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_BlockquoteType_strategy)
def test_xhtml_blockquotetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_BlockquoteType_strategy)
def test_xhtml_blockquotetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_HrType_strategy)
@settings(max_examples=50)
def test_xhtml_hrtype_instantiation(instance):
    assert isinstance(instance, xhtml_HrType)



@given(instance=xhtml_HrType_strategy)
def test_xhtml_hrtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_HrType_strategy)
def test_xhtml_hrtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_HrType_strategy)
def test_xhtml_hrtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_HrType_strategy)
def test_xhtml_hrtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_PreType_strategy)
@settings(max_examples=50)
def test_xhtml_pretype_instantiation(instance):
    assert isinstance(instance, xhtml_PreType)



@given(instance=xhtml_PreType_strategy)
def test_xhtml_pretype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_PreType_strategy)
def test_xhtml_pretype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_PreType_strategy)
def test_xhtml_pretype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_PreType_strategy)
def test_xhtml_pretype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_TableType_strategy)
@settings(max_examples=50)
def test_xhtml_tabletype_instantiation(instance):
    assert isinstance(instance, xhtml_TableType)



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TableType_strategy)
def test_xhtml_tabletype_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=xhtml_UlType_strategy)
@settings(max_examples=50)
def test_xhtml_ultype_instantiation(instance):
    assert isinstance(instance, xhtml_UlType)



@given(instance=xhtml_UlType_strategy)
def test_xhtml_ultype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_UlType_strategy)
def test_xhtml_ultype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_UlType_strategy)
def test_xhtml_ultype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_UlType_strategy)
def test_xhtml_ultype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_DivType_strategy)
@settings(max_examples=50)
def test_xhtml_divtype_instantiation(instance):
    assert isinstance(instance, xhtml_DivType)



@given(instance=xhtml_DivType_strategy)
def test_xhtml_divtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_DivType_strategy)
def test_xhtml_divtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_DivType_strategy)
def test_xhtml_divtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_DivType_strategy)
def test_xhtml_divtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_DlType_strategy)
@settings(max_examples=50)
def test_xhtml_dltype_instantiation(instance):
    assert isinstance(instance, xhtml_DlType)



@given(instance=xhtml_DlType_strategy)
def test_xhtml_dltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_DlType_strategy)
def test_xhtml_dltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_DlType_strategy)
def test_xhtml_dltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_DlType_strategy)
def test_xhtml_dltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_DlType_strategy)
def test_xhtml_dltype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml_OlType_strategy)
@settings(max_examples=50)
def test_xhtml_oltype_instantiation(instance):
    assert isinstance(instance, xhtml_OlType)



@given(instance=xhtml_OlType_strategy)
def test_xhtml_oltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_OlType_strategy)
def test_xhtml_oltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_OlType_strategy)
def test_xhtml_oltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_OlType_strategy)
def test_xhtml_oltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_Block_strategy)
@settings(max_examples=50)
def test_xhtml_block_instantiation(instance):
    assert isinstance(instance, xhtml_Block)



@given(instance=xhtml_Block_strategy)
def test_xhtml_block_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=AContent_strategy)
@settings(max_examples=50)
def test_acontent_instantiation(instance):
    assert isinstance(instance, AContent)

@given(instance=xhtml_AType_strategy)
@settings(max_examples=50)
def test_xhtml_atype_instantiation(instance):
    assert isinstance(instance, xhtml_AType)



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_rev_setter(instance):
    original = instance.rev
    instance.rev = original
    assert instance.rev == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_charset_setter(instance):
    original = instance.charset
    instance.charset = original
    assert instance.charset == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_hreflang_setter(instance):
    original = instance.hreflang
    instance.hreflang = original
    assert instance.hreflang == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_AType_strategy)
def test_xhtml_atype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xhtml_InsType_strategy)
@settings(max_examples=50)
def test_xhtml_instype_instantiation(instance):
    assert isinstance(instance, xhtml_InsType)



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_datetime_setter(instance):
    original = instance.datetime
    instance.datetime = original
    assert instance.datetime == original



@given(instance=xhtml_InsType_strategy)
def test_xhtml_instype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original

@given(instance=xhtml_DelType_strategy)
@settings(max_examples=50)
def test_xhtml_deltype_instantiation(instance):
    assert isinstance(instance, xhtml_DelType)



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_datetime_setter(instance):
    original = instance.datetime
    instance.datetime = original
    assert instance.datetime == original



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_DelType_strategy)
def test_xhtml_deltype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original

@given(instance=xhtml_ImgType_strategy)
@settings(max_examples=50)
def test_xhtml_imgtype_instantiation(instance):
    assert isinstance(instance, xhtml_ImgType)



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_longdesc_setter(instance):
    original = instance.longdesc
    instance.longdesc = original
    assert instance.longdesc == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_ImgType_strategy)
def test_xhtml_imgtype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml_ObjectType_strategy)
@settings(max_examples=50)
def test_xhtml_objecttype_instantiation(instance):
    assert isinstance(instance, xhtml_ObjectType)



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_tabindex_setter(instance):
    original = instance.tabindex
    instance.tabindex = original
    assert instance.tabindex == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_classid_setter(instance):
    original = instance.classid
    instance.classid = original
    assert instance.classid == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_standby_setter(instance):
    original = instance.standby
    instance.standby = original
    assert instance.standby == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_codebase_setter(instance):
    original = instance.codebase
    instance.codebase = original
    assert instance.codebase == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_codetype_setter(instance):
    original = instance.codetype
    instance.codetype = original
    assert instance.codetype == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_archive_setter(instance):
    original = instance.archive
    instance.archive = original
    assert instance.archive == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=xhtml_ObjectType_strategy)
def test_xhtml_objecttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xhtml_AContent_strategy)
@settings(max_examples=50)
def test_xhtml_acontent_instantiation(instance):
    assert isinstance(instance, xhtml_AContent)



@given(instance=xhtml_AContent_strategy)
def test_xhtml_acontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xhtml_AContent_strategy)
def test_xhtml_acontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Inline_strategy)
@settings(max_examples=50)
def test_inline_instantiation(instance):
    assert isinstance(instance, Inline)

@given(instance=xhtml_DfnType_strategy)
@settings(max_examples=50)
def test_xhtml_dfntype_instantiation(instance):
    assert isinstance(instance, xhtml_DfnType)



@given(instance=xhtml_DfnType_strategy)
def test_xhtml_dfntype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_DfnType_strategy)
def test_xhtml_dfntype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_DfnType_strategy)
def test_xhtml_dfntype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_DfnType_strategy)
def test_xhtml_dfntype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_PType_strategy)
@settings(max_examples=50)
def test_xhtml_ptype_instantiation(instance):
    assert isinstance(instance, xhtml_PType)



@given(instance=xhtml_PType_strategy)
def test_xhtml_ptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_PType_strategy)
def test_xhtml_ptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_PType_strategy)
def test_xhtml_ptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_PType_strategy)
def test_xhtml_ptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_QType_strategy)
@settings(max_examples=50)
def test_xhtml_qtype_instantiation(instance):
    assert isinstance(instance, xhtml_QType)



@given(instance=xhtml_QType_strategy)
def test_xhtml_qtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_QType_strategy)
def test_xhtml_qtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_QType_strategy)
def test_xhtml_qtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_QType_strategy)
def test_xhtml_qtype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original



@given(instance=xhtml_QType_strategy)
def test_xhtml_qtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_KbdType_strategy)
@settings(max_examples=50)
def test_xhtml_kbdtype_instantiation(instance):
    assert isinstance(instance, xhtml_KbdType)



@given(instance=xhtml_KbdType_strategy)
def test_xhtml_kbdtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_KbdType_strategy)
def test_xhtml_kbdtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_KbdType_strategy)
def test_xhtml_kbdtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_KbdType_strategy)
def test_xhtml_kbdtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_EmType_strategy)
@settings(max_examples=50)
def test_xhtml_emtype_instantiation(instance):
    assert isinstance(instance, xhtml_EmType)



@given(instance=xhtml_EmType_strategy)
def test_xhtml_emtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_EmType_strategy)
def test_xhtml_emtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_EmType_strategy)
def test_xhtml_emtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_EmType_strategy)
def test_xhtml_emtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_DtType_strategy)
@settings(max_examples=50)
def test_xhtml_dttype_instantiation(instance):
    assert isinstance(instance, xhtml_DtType)



@given(instance=xhtml_DtType_strategy)
def test_xhtml_dttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_DtType_strategy)
def test_xhtml_dttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_DtType_strategy)
def test_xhtml_dttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_DtType_strategy)
def test_xhtml_dttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_AcronymType_strategy)
@settings(max_examples=50)
def test_xhtml_acronymtype_instantiation(instance):
    assert isinstance(instance, xhtml_AcronymType)



@given(instance=xhtml_AcronymType_strategy)
def test_xhtml_acronymtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_AcronymType_strategy)
def test_xhtml_acronymtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_AcronymType_strategy)
def test_xhtml_acronymtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_AcronymType_strategy)
def test_xhtml_acronymtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_BigType_strategy)
@settings(max_examples=50)
def test_xhtml_bigtype_instantiation(instance):
    assert isinstance(instance, xhtml_BigType)



@given(instance=xhtml_BigType_strategy)
def test_xhtml_bigtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_BigType_strategy)
def test_xhtml_bigtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_BigType_strategy)
def test_xhtml_bigtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_BigType_strategy)
def test_xhtml_bigtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_TtType_strategy)
@settings(max_examples=50)
def test_xhtml_tttype_instantiation(instance):
    assert isinstance(instance, xhtml_TtType)



@given(instance=xhtml_TtType_strategy)
def test_xhtml_tttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_TtType_strategy)
def test_xhtml_tttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_TtType_strategy)
def test_xhtml_tttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_TtType_strategy)
def test_xhtml_tttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_H6Type_strategy)
@settings(max_examples=50)
def test_xhtml_h6type_instantiation(instance):
    assert isinstance(instance, xhtml_H6Type)



@given(instance=xhtml_H6Type_strategy)
def test_xhtml_h6type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_H6Type_strategy)
def test_xhtml_h6type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H6Type_strategy)
def test_xhtml_h6type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_H6Type_strategy)
def test_xhtml_h6type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_H2Type_strategy)
@settings(max_examples=50)
def test_xhtml_h2type_instantiation(instance):
    assert isinstance(instance, xhtml_H2Type)



@given(instance=xhtml_H2Type_strategy)
def test_xhtml_h2type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_H2Type_strategy)
def test_xhtml_h2type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H2Type_strategy)
def test_xhtml_h2type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_H2Type_strategy)
def test_xhtml_h2type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_StrongType_strategy)
@settings(max_examples=50)
def test_xhtml_strongtype_instantiation(instance):
    assert isinstance(instance, xhtml_StrongType)



@given(instance=xhtml_StrongType_strategy)
def test_xhtml_strongtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_StrongType_strategy)
def test_xhtml_strongtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_StrongType_strategy)
def test_xhtml_strongtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_StrongType_strategy)
def test_xhtml_strongtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_SampType_strategy)
@settings(max_examples=50)
def test_xhtml_samptype_instantiation(instance):
    assert isinstance(instance, xhtml_SampType)



@given(instance=xhtml_SampType_strategy)
def test_xhtml_samptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_SampType_strategy)
def test_xhtml_samptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_SampType_strategy)
def test_xhtml_samptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_SampType_strategy)
def test_xhtml_samptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_IType_strategy)
@settings(max_examples=50)
def test_xhtml_itype_instantiation(instance):
    assert isinstance(instance, xhtml_IType)



@given(instance=xhtml_IType_strategy)
def test_xhtml_itype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_IType_strategy)
def test_xhtml_itype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_IType_strategy)
def test_xhtml_itype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_IType_strategy)
def test_xhtml_itype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_AddressType_strategy)
@settings(max_examples=50)
def test_xhtml_addresstype_instantiation(instance):
    assert isinstance(instance, xhtml_AddressType)



@given(instance=xhtml_AddressType_strategy)
def test_xhtml_addresstype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_AddressType_strategy)
def test_xhtml_addresstype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_AddressType_strategy)
def test_xhtml_addresstype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_AddressType_strategy)
def test_xhtml_addresstype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_CiteType_strategy)
@settings(max_examples=50)
def test_xhtml_citetype_instantiation(instance):
    assert isinstance(instance, xhtml_CiteType)



@given(instance=xhtml_CiteType_strategy)
def test_xhtml_citetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_CiteType_strategy)
def test_xhtml_citetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_CiteType_strategy)
def test_xhtml_citetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_CiteType_strategy)
def test_xhtml_citetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_BType_strategy)
@settings(max_examples=50)
def test_xhtml_btype_instantiation(instance):
    assert isinstance(instance, xhtml_BType)



@given(instance=xhtml_BType_strategy)
def test_xhtml_btype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_BType_strategy)
def test_xhtml_btype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_BType_strategy)
def test_xhtml_btype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_BType_strategy)
def test_xhtml_btype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_H5Type_strategy)
@settings(max_examples=50)
def test_xhtml_h5type_instantiation(instance):
    assert isinstance(instance, xhtml_H5Type)



@given(instance=xhtml_H5Type_strategy)
def test_xhtml_h5type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_H5Type_strategy)
def test_xhtml_h5type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_H5Type_strategy)
def test_xhtml_h5type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H5Type_strategy)
def test_xhtml_h5type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_H1Type_strategy)
@settings(max_examples=50)
def test_xhtml_h1type_instantiation(instance):
    assert isinstance(instance, xhtml_H1Type)



@given(instance=xhtml_H1Type_strategy)
def test_xhtml_h1type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_H1Type_strategy)
def test_xhtml_h1type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H1Type_strategy)
def test_xhtml_h1type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_H1Type_strategy)
def test_xhtml_h1type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_H3Type_strategy)
@settings(max_examples=50)
def test_xhtml_h3type_instantiation(instance):
    assert isinstance(instance, xhtml_H3Type)



@given(instance=xhtml_H3Type_strategy)
def test_xhtml_h3type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_H3Type_strategy)
def test_xhtml_h3type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H3Type_strategy)
def test_xhtml_h3type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_H3Type_strategy)
def test_xhtml_h3type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_VarType_strategy)
@settings(max_examples=50)
def test_xhtml_vartype_instantiation(instance):
    assert isinstance(instance, xhtml_VarType)



@given(instance=xhtml_VarType_strategy)
def test_xhtml_vartype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_VarType_strategy)
def test_xhtml_vartype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_VarType_strategy)
def test_xhtml_vartype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_VarType_strategy)
def test_xhtml_vartype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_SmallType_strategy)
@settings(max_examples=50)
def test_xhtml_smalltype_instantiation(instance):
    assert isinstance(instance, xhtml_SmallType)



@given(instance=xhtml_SmallType_strategy)
def test_xhtml_smalltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_SmallType_strategy)
def test_xhtml_smalltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_SmallType_strategy)
def test_xhtml_smalltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_SmallType_strategy)
def test_xhtml_smalltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_UType_strategy)
@settings(max_examples=50)
def test_xhtml_utype_instantiation(instance):
    assert isinstance(instance, xhtml_UType)



@given(instance=xhtml_UType_strategy)
def test_xhtml_utype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_UType_strategy)
def test_xhtml_utype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_UType_strategy)
def test_xhtml_utype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_UType_strategy)
def test_xhtml_utype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_StrikeType_strategy)
@settings(max_examples=50)
def test_xhtml_striketype_instantiation(instance):
    assert isinstance(instance, xhtml_StrikeType)



@given(instance=xhtml_StrikeType_strategy)
def test_xhtml_striketype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_StrikeType_strategy)
def test_xhtml_striketype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_StrikeType_strategy)
def test_xhtml_striketype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_StrikeType_strategy)
def test_xhtml_striketype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_SubType_strategy)
@settings(max_examples=50)
def test_xhtml_subtype_instantiation(instance):
    assert isinstance(instance, xhtml_SubType)



@given(instance=xhtml_SubType_strategy)
def test_xhtml_subtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_SubType_strategy)
def test_xhtml_subtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_SubType_strategy)
def test_xhtml_subtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_SubType_strategy)
def test_xhtml_subtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml_CaptionType_strategy)
@settings(max_examples=50)
def test_xhtml_captiontype_instantiation(instance):
    assert isinstance(instance, xhtml_CaptionType)



@given(instance=xhtml_CaptionType_strategy)
def test_xhtml_captiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_CaptionType_strategy)
def test_xhtml_captiontype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_CaptionType_strategy)
def test_xhtml_captiontype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_CaptionType_strategy)
def test_xhtml_captiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_H4Type_strategy)
@settings(max_examples=50)
def test_xhtml_h4type_instantiation(instance):
    assert isinstance(instance, xhtml_H4Type)



@given(instance=xhtml_H4Type_strategy)
def test_xhtml_h4type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_H4Type_strategy)
def test_xhtml_h4type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_H4Type_strategy)
def test_xhtml_h4type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_H4Type_strategy)
def test_xhtml_h4type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_CodeType_strategy)
@settings(max_examples=50)
def test_xhtml_codetype_instantiation(instance):
    assert isinstance(instance, xhtml_CodeType)



@given(instance=xhtml_CodeType_strategy)
def test_xhtml_codetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_CodeType_strategy)
def test_xhtml_codetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_CodeType_strategy)
def test_xhtml_codetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_CodeType_strategy)
def test_xhtml_codetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml_SupType_strategy)
@settings(max_examples=50)
def test_xhtml_suptype_instantiation(instance):
    assert isinstance(instance, xhtml_SupType)



@given(instance=xhtml_SupType_strategy)
def test_xhtml_suptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=xhtml_SupType_strategy)
def test_xhtml_suptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_SupType_strategy)
def test_xhtml_suptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_SupType_strategy)
def test_xhtml_suptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml_AbbrType_strategy)
@settings(max_examples=50)
def test_xhtml_abbrtype_instantiation(instance):
    assert isinstance(instance, xhtml_AbbrType)



@given(instance=xhtml_AbbrType_strategy)
def test_xhtml_abbrtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_AbbrType_strategy)
def test_xhtml_abbrtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_AbbrType_strategy)
def test_xhtml_abbrtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_AbbrType_strategy)
def test_xhtml_abbrtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_SpanType_strategy)
@settings(max_examples=50)
def test_xhtml_spantype_instantiation(instance):
    assert isinstance(instance, xhtml_SpanType)



@given(instance=xhtml_SpanType_strategy)
def test_xhtml_spantype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_SpanType_strategy)
def test_xhtml_spantype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_SpanType_strategy)
def test_xhtml_spantype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_SpanType_strategy)
def test_xhtml_spantype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml_BrType_strategy)
@settings(max_examples=50)
def test_xhtml_brtype_instantiation(instance):
    assert isinstance(instance, xhtml_BrType)



@given(instance=xhtml_BrType_strategy)
def test_xhtml_brtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=xhtml_BrType_strategy)
def test_xhtml_brtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xhtml_BrType_strategy)
def test_xhtml_brtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xhtml_BrType_strategy)
def test_xhtml_brtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original
