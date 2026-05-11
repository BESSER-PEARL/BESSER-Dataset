import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PreContent,
    xhtml::PreContent,
    xhtml::Inline,
    xhtml::FormContent,
    xhtml::Flow,
    xhtml::TbodyType,
    xhtml::TrType,
    xhtml::TheadType,
    xhtml::TfootType,
    xhtml::ParamType,
    xhtml::HtmlType,
    xhtml::EStringToStringMapEntry,
    xhtml::DocumentRoot,
    Flow,
    xhtml::LiType,
    xhtml::ThType,
    xhtml::TdType,
    xhtml::DdType,
    xhtml::ColType,
    xhtml::ColgroupType,
    Block,
    xhtml::BodyType,
    xhtml::BlockquoteType,
    xhtml::HrType,
    xhtml::PreType,
    xhtml::TableType,
    xhtml::UlType,
    xhtml::DivType,
    xhtml::DlType,
    xhtml::OlType,
    xhtml::Block,
    AContent,
    xhtml::AType,
    xhtml::InsType,
    xhtml::DelType,
    xhtml::ImgType,
    xhtml::ObjectType,
    xhtml::AContent,
    Inline,
    xhtml::PType,
    xhtml::CodeType,
    xhtml::H4Type,
    xhtml::H5Type,
    xhtml::DfnType,
    xhtml::SupType,
    xhtml::StrikeType,
    xhtml::StrongType,
    xhtml::H2Type,
    xhtml::EmType,
    xhtml::CiteType,
    xhtml::UType,
    xhtml::CaptionType,
    xhtml::SubType,
    xhtml::TtType,
    xhtml::H6Type,
    xhtml::BigType,
    xhtml::QType,
    xhtml::SmallType,
    xhtml::KbdType,
    xhtml::H3Type,
    xhtml::BType,
    xhtml::AddressType,
    xhtml::AcronymType,
    xhtml::DtType,
    xhtml::SampType,
    xhtml::H1Type,
    xhtml::IType,
    xhtml::VarType,
    xhtml::AbbrType,
    xhtml::SpanType,
    xhtml::BrType,
    ValuetypeType,
    DeclareType,
    Shape,
    IsmapType,
    AlignType,
    ValignType,
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



def test_xhtml::precontent_is_not_abstract():
    assert not inspect.isabstract(xhtml::PreContent)


def test_xhtml::precontent_constructor_exists():
    assert callable(xhtml::PreContent.__init__)


def test_xhtml::precontent_constructor_args():
    sig = inspect.signature(xhtml::PreContent.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::precontent_has_mixed():
    assert hasattr(xhtml::PreContent, "mixed")
    descriptor = None
    for klass in xhtml::PreContent.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::precontent_has_group():
    assert hasattr(xhtml::PreContent, "group")
    descriptor = None
    for klass in xhtml::PreContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::inline_is_not_abstract():
    assert not inspect.isabstract(xhtml::Inline)


def test_xhtml::inline_constructor_exists():
    assert callable(xhtml::Inline.__init__)


def test_xhtml::inline_constructor_args():
    sig = inspect.signature(xhtml::Inline.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xhtml::inline_has_group():
    assert hasattr(xhtml::Inline, "group")
    descriptor = None
    for klass in xhtml::Inline.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::inline_has_mixed():
    assert hasattr(xhtml::Inline, "mixed")
    descriptor = None
    for klass in xhtml::Inline.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::formcontent_is_not_abstract():
    assert not inspect.isabstract(xhtml::FormContent)


def test_xhtml::formcontent_constructor_exists():
    assert callable(xhtml::FormContent.__init__)


def test_xhtml::formcontent_constructor_args():
    sig = inspect.signature(xhtml::FormContent.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::formcontent_has_group():
    assert hasattr(xhtml::FormContent, "group")
    descriptor = None
    for klass in xhtml::FormContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::flow_is_not_abstract():
    assert not inspect.isabstract(xhtml::Flow)


def test_xhtml::flow_constructor_exists():
    assert callable(xhtml::Flow.__init__)


def test_xhtml::flow_constructor_args():
    sig = inspect.signature(xhtml::Flow.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::flow_has_mixed():
    assert hasattr(xhtml::Flow, "mixed")
    descriptor = None
    for klass in xhtml::Flow.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::flow_has_group():
    assert hasattr(xhtml::Flow, "group")
    descriptor = None
    for klass in xhtml::Flow.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::tbodytype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TbodyType)


def test_xhtml::tbodytype_constructor_exists():
    assert callable(xhtml::TbodyType.__init__)


def test_xhtml::tbodytype_constructor_args():
    sig = inspect.signature(xhtml::TbodyType.__init__)
    params = list(sig.parameters.keys())
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "style" in params, "Missing parameter 'style'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::tbodytype_has_charoff():
    assert hasattr(xhtml::TbodyType, "charoff")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_style():
    assert hasattr(xhtml::TbodyType, "style")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_char():
    assert hasattr(xhtml::TbodyType, "char")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_class_():
    assert hasattr(xhtml::TbodyType, "class_")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_align():
    assert hasattr(xhtml::TbodyType, "align")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_valign():
    assert hasattr(xhtml::TbodyType, "valign")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_title():
    assert hasattr(xhtml::TbodyType, "title")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tbodytype_has_id():
    assert hasattr(xhtml::TbodyType, "id")
    descriptor = None
    for klass in xhtml::TbodyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::trtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TrType)


def test_xhtml::trtype_constructor_exists():
    assert callable(xhtml::TrType.__init__)


def test_xhtml::trtype_constructor_args():
    sig = inspect.signature(xhtml::TrType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "align" in params, "Missing parameter 'align'"
    assert "group" in params, "Missing parameter 'group'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "style" in params, "Missing parameter 'style'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "char" in params, "Missing parameter 'char'"

def test_xhtml::trtype_has_title():
    assert hasattr(xhtml::TrType, "title")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_class_():
    assert hasattr(xhtml::TrType, "class_")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_id():
    assert hasattr(xhtml::TrType, "id")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_align():
    assert hasattr(xhtml::TrType, "align")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_group():
    assert hasattr(xhtml::TrType, "group")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_valign():
    assert hasattr(xhtml::TrType, "valign")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_style():
    assert hasattr(xhtml::TrType, "style")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_charoff():
    assert hasattr(xhtml::TrType, "charoff")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::trtype_has_char():
    assert hasattr(xhtml::TrType, "char")
    descriptor = None
    for klass in xhtml::TrType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::theadtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TheadType)


def test_xhtml::theadtype_constructor_exists():
    assert callable(xhtml::TheadType.__init__)


def test_xhtml::theadtype_constructor_args():
    sig = inspect.signature(xhtml::TheadType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "align" in params, "Missing parameter 'align'"
    assert "char" in params, "Missing parameter 'char'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::theadtype_has_style():
    assert hasattr(xhtml::TheadType, "style")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_id():
    assert hasattr(xhtml::TheadType, "id")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_title():
    assert hasattr(xhtml::TheadType, "title")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_charoff():
    assert hasattr(xhtml::TheadType, "charoff")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_align():
    assert hasattr(xhtml::TheadType, "align")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_char():
    assert hasattr(xhtml::TheadType, "char")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_valign():
    assert hasattr(xhtml::TheadType, "valign")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::theadtype_has_class_():
    assert hasattr(xhtml::TheadType, "class_")
    descriptor = None
    for klass in xhtml::TheadType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::tfoottype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TfootType)


def test_xhtml::tfoottype_constructor_exists():
    assert callable(xhtml::TfootType.__init__)


def test_xhtml::tfoottype_constructor_args():
    sig = inspect.signature(xhtml::TfootType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "style" in params, "Missing parameter 'style'"
    assert "align" in params, "Missing parameter 'align'"

def test_xhtml::tfoottype_has_id():
    assert hasattr(xhtml::TfootType, "id")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_title():
    assert hasattr(xhtml::TfootType, "title")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_char():
    assert hasattr(xhtml::TfootType, "char")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_class_():
    assert hasattr(xhtml::TfootType, "class_")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_valign():
    assert hasattr(xhtml::TfootType, "valign")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_charoff():
    assert hasattr(xhtml::TfootType, "charoff")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_style():
    assert hasattr(xhtml::TfootType, "style")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tfoottype_has_align():
    assert hasattr(xhtml::TfootType, "align")
    descriptor = None
    for klass in xhtml::TfootType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::paramtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ParamType)


def test_xhtml::paramtype_constructor_exists():
    assert callable(xhtml::ParamType.__init__)


def test_xhtml::paramtype_constructor_args():
    sig = inspect.signature(xhtml::ParamType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "valuetype" in params, "Missing parameter 'valuetype'"
    assert "name" in params, "Missing parameter 'name'"

def test_xhtml::paramtype_has_value():
    assert hasattr(xhtml::ParamType, "value")
    descriptor = None
    for klass in xhtml::ParamType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::paramtype_has_type():
    assert hasattr(xhtml::ParamType, "type")
    descriptor = None
    for klass in xhtml::ParamType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::paramtype_has_id():
    assert hasattr(xhtml::ParamType, "id")
    descriptor = None
    for klass in xhtml::ParamType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::paramtype_has_valuetype():
    assert hasattr(xhtml::ParamType, "valuetype")
    descriptor = None
    for klass in xhtml::ParamType.__mro__:
        if "valuetype" in klass.__dict__:
            descriptor = klass.__dict__["valuetype"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::paramtype_has_name():
    assert hasattr(xhtml::ParamType, "name")
    descriptor = None
    for klass in xhtml::ParamType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::htmltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::HtmlType)


def test_xhtml::htmltype_constructor_exists():
    assert callable(xhtml::HtmlType.__init__)


def test_xhtml::htmltype_constructor_args():
    sig = inspect.signature(xhtml::HtmlType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::htmltype_has_id():
    assert hasattr(xhtml::HtmlType, "id")
    descriptor = None
    for klass in xhtml::HtmlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(xhtml::EStringToStringMapEntry)


def test_xhtml::estringtostringmapentry_constructor_exists():
    assert callable(xhtml::EStringToStringMapEntry.__init__)


def test_xhtml::estringtostringmapentry_constructor_args():
    sig = inspect.signature(xhtml::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::documentroot_is_not_abstract():
    assert not inspect.isabstract(xhtml::DocumentRoot)


def test_xhtml::documentroot_constructor_exists():
    assert callable(xhtml::DocumentRoot.__init__)


def test_xhtml::documentroot_constructor_args():
    sig = inspect.signature(xhtml::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_xhtml::documentroot_has_mixed():
    assert hasattr(xhtml::DocumentRoot, "mixed")
    descriptor = None
    for klass in xhtml::DocumentRoot.__mro__:
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



def test_xhtml::litype_is_not_abstract():
    assert not inspect.isabstract(xhtml::LiType)


def test_xhtml::litype_constructor_exists():
    assert callable(xhtml::LiType.__init__)


def test_xhtml::litype_constructor_args():
    sig = inspect.signature(xhtml::LiType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::litype_has_class_():
    assert hasattr(xhtml::LiType, "class_")
    descriptor = None
    for klass in xhtml::LiType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::litype_has_title():
    assert hasattr(xhtml::LiType, "title")
    descriptor = None
    for klass in xhtml::LiType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::litype_has_id():
    assert hasattr(xhtml::LiType, "id")
    descriptor = None
    for klass in xhtml::LiType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::litype_has_style():
    assert hasattr(xhtml::LiType, "style")
    descriptor = None
    for klass in xhtml::LiType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::thtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ThType)


def test_xhtml::thtype_constructor_exists():
    assert callable(xhtml::ThType.__init__)


def test_xhtml::thtype_constructor_args():
    sig = inspect.signature(xhtml::ThType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "headers" in params, "Missing parameter 'headers'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "align" in params, "Missing parameter 'align'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "abbr1" in params, "Missing parameter 'abbr1'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "char" in params, "Missing parameter 'char'"
    assert "style" in params, "Missing parameter 'style'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "axis" in params, "Missing parameter 'axis'"

def test_xhtml::thtype_has_id():
    assert hasattr(xhtml::ThType, "id")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_title():
    assert hasattr(xhtml::ThType, "title")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_headers():
    assert hasattr(xhtml::ThType, "headers")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "headers" in klass.__dict__:
            descriptor = klass.__dict__["headers"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_valign():
    assert hasattr(xhtml::ThType, "valign")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_align():
    assert hasattr(xhtml::ThType, "align")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_colspan():
    assert hasattr(xhtml::ThType, "colspan")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_class_():
    assert hasattr(xhtml::ThType, "class_")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_rowspan():
    assert hasattr(xhtml::ThType, "rowspan")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_abbr1():
    assert hasattr(xhtml::ThType, "abbr1")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "abbr1" in klass.__dict__:
            descriptor = klass.__dict__["abbr1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_charoff():
    assert hasattr(xhtml::ThType, "charoff")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_char():
    assert hasattr(xhtml::ThType, "char")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_style():
    assert hasattr(xhtml::ThType, "style")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_scope():
    assert hasattr(xhtml::ThType, "scope")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::thtype_has_axis():
    assert hasattr(xhtml::ThType, "axis")
    descriptor = None
    for klass in xhtml::ThType.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::tdtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TdType)


def test_xhtml::tdtype_constructor_exists():
    assert callable(xhtml::TdType.__init__)


def test_xhtml::tdtype_constructor_args():
    sig = inspect.signature(xhtml::TdType.__init__)
    params = list(sig.parameters.keys())
    assert "char" in params, "Missing parameter 'char'"
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "scope" in params, "Missing parameter 'scope'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "abbr1" in params, "Missing parameter 'abbr1'"
    assert "style" in params, "Missing parameter 'style'"
    assert "headers" in params, "Missing parameter 'headers'"
    assert "axis" in params, "Missing parameter 'axis'"
    assert "charoff" in params, "Missing parameter 'charoff'"

def test_xhtml::tdtype_has_char():
    assert hasattr(xhtml::TdType, "char")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_align():
    assert hasattr(xhtml::TdType, "align")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_valign():
    assert hasattr(xhtml::TdType, "valign")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_scope():
    assert hasattr(xhtml::TdType, "scope")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_class_():
    assert hasattr(xhtml::TdType, "class_")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_colspan():
    assert hasattr(xhtml::TdType, "colspan")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_title():
    assert hasattr(xhtml::TdType, "title")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_id():
    assert hasattr(xhtml::TdType, "id")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_rowspan():
    assert hasattr(xhtml::TdType, "rowspan")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_abbr1():
    assert hasattr(xhtml::TdType, "abbr1")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "abbr1" in klass.__dict__:
            descriptor = klass.__dict__["abbr1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_style():
    assert hasattr(xhtml::TdType, "style")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_headers():
    assert hasattr(xhtml::TdType, "headers")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "headers" in klass.__dict__:
            descriptor = klass.__dict__["headers"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_axis():
    assert hasattr(xhtml::TdType, "axis")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "axis" in klass.__dict__:
            descriptor = klass.__dict__["axis"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tdtype_has_charoff():
    assert hasattr(xhtml::TdType, "charoff")
    descriptor = None
    for klass in xhtml::TdType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::ddtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DdType)


def test_xhtml::ddtype_constructor_exists():
    assert callable(xhtml::DdType.__init__)


def test_xhtml::ddtype_constructor_args():
    sig = inspect.signature(xhtml::DdType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::ddtype_has_class_():
    assert hasattr(xhtml::DdType, "class_")
    descriptor = None
    for klass in xhtml::DdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ddtype_has_title():
    assert hasattr(xhtml::DdType, "title")
    descriptor = None
    for klass in xhtml::DdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ddtype_has_id():
    assert hasattr(xhtml::DdType, "id")
    descriptor = None
    for klass in xhtml::DdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ddtype_has_style():
    assert hasattr(xhtml::DdType, "style")
    descriptor = None
    for klass in xhtml::DdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::coltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ColType)


def test_xhtml::coltype_constructor_exists():
    assert callable(xhtml::ColType.__init__)


def test_xhtml::coltype_constructor_args():
    sig = inspect.signature(xhtml::ColType.__init__)
    params = list(sig.parameters.keys())
    assert "span" in params, "Missing parameter 'span'"
    assert "style" in params, "Missing parameter 'style'"
    assert "width" in params, "Missing parameter 'width'"
    assert "align" in params, "Missing parameter 'align'"
    assert "id" in params, "Missing parameter 'id'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "char" in params, "Missing parameter 'char'"

def test_xhtml::coltype_has_span():
    assert hasattr(xhtml::ColType, "span")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_style():
    assert hasattr(xhtml::ColType, "style")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_width():
    assert hasattr(xhtml::ColType, "width")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_align():
    assert hasattr(xhtml::ColType, "align")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_id():
    assert hasattr(xhtml::ColType, "id")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_valign():
    assert hasattr(xhtml::ColType, "valign")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_title():
    assert hasattr(xhtml::ColType, "title")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_class_():
    assert hasattr(xhtml::ColType, "class_")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_charoff():
    assert hasattr(xhtml::ColType, "charoff")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::coltype_has_char():
    assert hasattr(xhtml::ColType, "char")
    descriptor = None
    for klass in xhtml::ColType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::colgrouptype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ColgroupType)


def test_xhtml::colgrouptype_constructor_exists():
    assert callable(xhtml::ColgroupType.__init__)


def test_xhtml::colgrouptype_constructor_args():
    sig = inspect.signature(xhtml::ColgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "char" in params, "Missing parameter 'char'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "charoff" in params, "Missing parameter 'charoff'"
    assert "span" in params, "Missing parameter 'span'"
    assert "width" in params, "Missing parameter 'width'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::colgrouptype_has_align():
    assert hasattr(xhtml::ColgroupType, "align")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_char():
    assert hasattr(xhtml::ColgroupType, "char")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "char" in klass.__dict__:
            descriptor = klass.__dict__["char"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_class_():
    assert hasattr(xhtml::ColgroupType, "class_")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_style():
    assert hasattr(xhtml::ColgroupType, "style")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_title():
    assert hasattr(xhtml::ColgroupType, "title")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_charoff():
    assert hasattr(xhtml::ColgroupType, "charoff")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "charoff" in klass.__dict__:
            descriptor = klass.__dict__["charoff"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_span():
    assert hasattr(xhtml::ColgroupType, "span")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "span" in klass.__dict__:
            descriptor = klass.__dict__["span"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_width():
    assert hasattr(xhtml::ColgroupType, "width")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_valign():
    assert hasattr(xhtml::ColgroupType, "valign")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::colgrouptype_has_id():
    assert hasattr(xhtml::ColgroupType, "id")
    descriptor = None
    for klass in xhtml::ColgroupType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::bodytype_is_not_abstract():
    assert not inspect.isabstract(xhtml::BodyType)


def test_xhtml::bodytype_constructor_exists():
    assert callable(xhtml::BodyType.__init__)


def test_xhtml::bodytype_constructor_args():
    sig = inspect.signature(xhtml::BodyType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::bodytype_has_title():
    assert hasattr(xhtml::BodyType, "title")
    descriptor = None
    for klass in xhtml::BodyType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bodytype_has_class_():
    assert hasattr(xhtml::BodyType, "class_")
    descriptor = None
    for klass in xhtml::BodyType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bodytype_has_id():
    assert hasattr(xhtml::BodyType, "id")
    descriptor = None
    for klass in xhtml::BodyType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bodytype_has_style():
    assert hasattr(xhtml::BodyType, "style")
    descriptor = None
    for klass in xhtml::BodyType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::blockquotetype_is_not_abstract():
    assert not inspect.isabstract(xhtml::BlockquoteType)


def test_xhtml::blockquotetype_constructor_exists():
    assert callable(xhtml::BlockquoteType.__init__)


def test_xhtml::blockquotetype_constructor_args():
    sig = inspect.signature(xhtml::BlockquoteType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "cite" in params, "Missing parameter 'cite'"

def test_xhtml::blockquotetype_has_style():
    assert hasattr(xhtml::BlockquoteType, "style")
    descriptor = None
    for klass in xhtml::BlockquoteType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::blockquotetype_has_id():
    assert hasattr(xhtml::BlockquoteType, "id")
    descriptor = None
    for klass in xhtml::BlockquoteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::blockquotetype_has_class_():
    assert hasattr(xhtml::BlockquoteType, "class_")
    descriptor = None
    for klass in xhtml::BlockquoteType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::blockquotetype_has_title():
    assert hasattr(xhtml::BlockquoteType, "title")
    descriptor = None
    for klass in xhtml::BlockquoteType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::blockquotetype_has_cite():
    assert hasattr(xhtml::BlockquoteType, "cite")
    descriptor = None
    for klass in xhtml::BlockquoteType.__mro__:
        if "cite" in klass.__dict__:
            descriptor = klass.__dict__["cite"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::hrtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::HrType)


def test_xhtml::hrtype_constructor_exists():
    assert callable(xhtml::HrType.__init__)


def test_xhtml::hrtype_constructor_args():
    sig = inspect.signature(xhtml::HrType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::hrtype_has_class_():
    assert hasattr(xhtml::HrType, "class_")
    descriptor = None
    for klass in xhtml::HrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::hrtype_has_style():
    assert hasattr(xhtml::HrType, "style")
    descriptor = None
    for klass in xhtml::HrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::hrtype_has_id():
    assert hasattr(xhtml::HrType, "id")
    descriptor = None
    for klass in xhtml::HrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::hrtype_has_title():
    assert hasattr(xhtml::HrType, "title")
    descriptor = None
    for klass in xhtml::HrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::pretype_is_not_abstract():
    assert not inspect.isabstract(xhtml::PreType)


def test_xhtml::pretype_constructor_exists():
    assert callable(xhtml::PreType.__init__)


def test_xhtml::pretype_constructor_args():
    sig = inspect.signature(xhtml::PreType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::pretype_has_style():
    assert hasattr(xhtml::PreType, "style")
    descriptor = None
    for klass in xhtml::PreType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::pretype_has_class_():
    assert hasattr(xhtml::PreType, "class_")
    descriptor = None
    for klass in xhtml::PreType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::pretype_has_title():
    assert hasattr(xhtml::PreType, "title")
    descriptor = None
    for klass in xhtml::PreType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::pretype_has_id():
    assert hasattr(xhtml::PreType, "id")
    descriptor = None
    for klass in xhtml::PreType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::tabletype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TableType)


def test_xhtml::tabletype_constructor_exists():
    assert callable(xhtml::TableType.__init__)


def test_xhtml::tabletype_constructor_args():
    sig = inspect.signature(xhtml::TableType.__init__)
    params = list(sig.parameters.keys())
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "summary" in params, "Missing parameter 'summary'"
    assert "title" in params, "Missing parameter 'title'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"
    assert "width" in params, "Missing parameter 'width'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "border" in params, "Missing parameter 'border'"

def test_xhtml::tabletype_has_cellspacing():
    assert hasattr(xhtml::TableType, "cellspacing")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "cellspacing" in klass.__dict__:
            descriptor = klass.__dict__["cellspacing"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_summary():
    assert hasattr(xhtml::TableType, "summary")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "summary" in klass.__dict__:
            descriptor = klass.__dict__["summary"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_title():
    assert hasattr(xhtml::TableType, "title")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_cellpadding():
    assert hasattr(xhtml::TableType, "cellpadding")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "cellpadding" in klass.__dict__:
            descriptor = klass.__dict__["cellpadding"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_width():
    assert hasattr(xhtml::TableType, "width")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_style():
    assert hasattr(xhtml::TableType, "style")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_id():
    assert hasattr(xhtml::TableType, "id")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_class_():
    assert hasattr(xhtml::TableType, "class_")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tabletype_has_border():
    assert hasattr(xhtml::TableType, "border")
    descriptor = None
    for klass in xhtml::TableType.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::ultype_is_not_abstract():
    assert not inspect.isabstract(xhtml::UlType)


def test_xhtml::ultype_constructor_exists():
    assert callable(xhtml::UlType.__init__)


def test_xhtml::ultype_constructor_args():
    sig = inspect.signature(xhtml::UlType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::ultype_has_class_():
    assert hasattr(xhtml::UlType, "class_")
    descriptor = None
    for klass in xhtml::UlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ultype_has_style():
    assert hasattr(xhtml::UlType, "style")
    descriptor = None
    for klass in xhtml::UlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ultype_has_title():
    assert hasattr(xhtml::UlType, "title")
    descriptor = None
    for klass in xhtml::UlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ultype_has_id():
    assert hasattr(xhtml::UlType, "id")
    descriptor = None
    for klass in xhtml::UlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::divtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DivType)


def test_xhtml::divtype_constructor_exists():
    assert callable(xhtml::DivType.__init__)


def test_xhtml::divtype_constructor_args():
    sig = inspect.signature(xhtml::DivType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::divtype_has_id():
    assert hasattr(xhtml::DivType, "id")
    descriptor = None
    for klass in xhtml::DivType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::divtype_has_style():
    assert hasattr(xhtml::DivType, "style")
    descriptor = None
    for klass in xhtml::DivType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::divtype_has_title():
    assert hasattr(xhtml::DivType, "title")
    descriptor = None
    for klass in xhtml::DivType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::divtype_has_class_():
    assert hasattr(xhtml::DivType, "class_")
    descriptor = None
    for klass in xhtml::DivType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::dltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DlType)


def test_xhtml::dltype_constructor_exists():
    assert callable(xhtml::DlType.__init__)


def test_xhtml::dltype_constructor_args():
    sig = inspect.signature(xhtml::DlType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::dltype_has_style():
    assert hasattr(xhtml::DlType, "style")
    descriptor = None
    for klass in xhtml::DlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dltype_has_id():
    assert hasattr(xhtml::DlType, "id")
    descriptor = None
    for klass in xhtml::DlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dltype_has_group():
    assert hasattr(xhtml::DlType, "group")
    descriptor = None
    for klass in xhtml::DlType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dltype_has_title():
    assert hasattr(xhtml::DlType, "title")
    descriptor = None
    for klass in xhtml::DlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dltype_has_class_():
    assert hasattr(xhtml::DlType, "class_")
    descriptor = None
    for klass in xhtml::DlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::oltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::OlType)


def test_xhtml::oltype_constructor_exists():
    assert callable(xhtml::OlType.__init__)


def test_xhtml::oltype_constructor_args():
    sig = inspect.signature(xhtml::OlType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::oltype_has_class_():
    assert hasattr(xhtml::OlType, "class_")
    descriptor = None
    for klass in xhtml::OlType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::oltype_has_title():
    assert hasattr(xhtml::OlType, "title")
    descriptor = None
    for klass in xhtml::OlType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::oltype_has_id():
    assert hasattr(xhtml::OlType, "id")
    descriptor = None
    for klass in xhtml::OlType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::oltype_has_style():
    assert hasattr(xhtml::OlType, "style")
    descriptor = None
    for klass in xhtml::OlType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::block_is_not_abstract():
    assert not inspect.isabstract(xhtml::Block)


def test_xhtml::block_constructor_exists():
    assert callable(xhtml::Block.__init__)


def test_xhtml::block_constructor_args():
    sig = inspect.signature(xhtml::Block.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::block_has_group():
    assert hasattr(xhtml::Block, "group")
    descriptor = None
    for klass in xhtml::Block.__mro__:
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



def test_xhtml::atype_is_not_abstract():
    assert not inspect.isabstract(xhtml::AType)


def test_xhtml::atype_constructor_exists():
    assert callable(xhtml::AType.__init__)


def test_xhtml::atype_constructor_args():
    sig = inspect.signature(xhtml::AType.__init__)
    params = list(sig.parameters.keys())
    assert "rev" in params, "Missing parameter 'rev'"
    assert "charset" in params, "Missing parameter 'charset'"
    assert "shape" in params, "Missing parameter 'shape'"
    assert "hreflang" in params, "Missing parameter 'hreflang'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "style" in params, "Missing parameter 'style'"
    assert "href" in params, "Missing parameter 'href'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "coords" in params, "Missing parameter 'coords'"
    assert "rel" in params, "Missing parameter 'rel'"
    assert "type" in params, "Missing parameter 'type'"

def test_xhtml::atype_has_rev():
    assert hasattr(xhtml::AType, "rev")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "rev" in klass.__dict__:
            descriptor = klass.__dict__["rev"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_charset():
    assert hasattr(xhtml::AType, "charset")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "charset" in klass.__dict__:
            descriptor = klass.__dict__["charset"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_shape():
    assert hasattr(xhtml::AType, "shape")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_hreflang():
    assert hasattr(xhtml::AType, "hreflang")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "hreflang" in klass.__dict__:
            descriptor = klass.__dict__["hreflang"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_id():
    assert hasattr(xhtml::AType, "id")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_name():
    assert hasattr(xhtml::AType, "name")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_style():
    assert hasattr(xhtml::AType, "style")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_href():
    assert hasattr(xhtml::AType, "href")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_class_():
    assert hasattr(xhtml::AType, "class_")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_title():
    assert hasattr(xhtml::AType, "title")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_coords():
    assert hasattr(xhtml::AType, "coords")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "coords" in klass.__dict__:
            descriptor = klass.__dict__["coords"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_rel():
    assert hasattr(xhtml::AType, "rel")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "rel" in klass.__dict__:
            descriptor = klass.__dict__["rel"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::atype_has_type():
    assert hasattr(xhtml::AType, "type")
    descriptor = None
    for klass in xhtml::AType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::instype_is_not_abstract():
    assert not inspect.isabstract(xhtml::InsType)


def test_xhtml::instype_constructor_exists():
    assert callable(xhtml::InsType.__init__)


def test_xhtml::instype_constructor_args():
    sig = inspect.signature(xhtml::InsType.__init__)
    params = list(sig.parameters.keys())
    assert "cite1" in params, "Missing parameter 'cite1'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "datetime" in params, "Missing parameter 'datetime'"

def test_xhtml::instype_has_cite1():
    assert hasattr(xhtml::InsType, "cite1")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::instype_has_title():
    assert hasattr(xhtml::InsType, "title")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::instype_has_id():
    assert hasattr(xhtml::InsType, "id")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::instype_has_class_():
    assert hasattr(xhtml::InsType, "class_")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::instype_has_style():
    assert hasattr(xhtml::InsType, "style")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::instype_has_datetime():
    assert hasattr(xhtml::InsType, "datetime")
    descriptor = None
    for klass in xhtml::InsType.__mro__:
        if "datetime" in klass.__dict__:
            descriptor = klass.__dict__["datetime"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::deltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DelType)


def test_xhtml::deltype_constructor_exists():
    assert callable(xhtml::DelType.__init__)


def test_xhtml::deltype_constructor_args():
    sig = inspect.signature(xhtml::DelType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "datetime" in params, "Missing parameter 'datetime'"
    assert "cite1" in params, "Missing parameter 'cite1'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::deltype_has_id():
    assert hasattr(xhtml::DelType, "id")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::deltype_has_datetime():
    assert hasattr(xhtml::DelType, "datetime")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "datetime" in klass.__dict__:
            descriptor = klass.__dict__["datetime"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::deltype_has_cite1():
    assert hasattr(xhtml::DelType, "cite1")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::deltype_has_style():
    assert hasattr(xhtml::DelType, "style")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::deltype_has_class_():
    assert hasattr(xhtml::DelType, "class_")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::deltype_has_title():
    assert hasattr(xhtml::DelType, "title")
    descriptor = None
    for klass in xhtml::DelType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::imgtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ImgType)


def test_xhtml::imgtype_constructor_exists():
    assert callable(xhtml::ImgType.__init__)


def test_xhtml::imgtype_constructor_args():
    sig = inspect.signature(xhtml::ImgType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "ismap" in params, "Missing parameter 'ismap'"
    assert "longdesc" in params, "Missing parameter 'longdesc'"
    assert "title" in params, "Missing parameter 'title'"
    assert "src" in params, "Missing parameter 'src'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "style" in params, "Missing parameter 'style'"
    assert "height" in params, "Missing parameter 'height'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"
    assert "alt" in params, "Missing parameter 'alt'"

def test_xhtml::imgtype_has_id():
    assert hasattr(xhtml::ImgType, "id")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_ismap():
    assert hasattr(xhtml::ImgType, "ismap")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_longdesc():
    assert hasattr(xhtml::ImgType, "longdesc")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "longdesc" in klass.__dict__:
            descriptor = klass.__dict__["longdesc"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_title():
    assert hasattr(xhtml::ImgType, "title")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_src():
    assert hasattr(xhtml::ImgType, "src")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_usemap():
    assert hasattr(xhtml::ImgType, "usemap")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_style():
    assert hasattr(xhtml::ImgType, "style")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_height():
    assert hasattr(xhtml::ImgType, "height")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_class_():
    assert hasattr(xhtml::ImgType, "class_")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_width():
    assert hasattr(xhtml::ImgType, "width")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::imgtype_has_alt():
    assert hasattr(xhtml::ImgType, "alt")
    descriptor = None
    for klass in xhtml::ImgType.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::objecttype_is_not_abstract():
    assert not inspect.isabstract(xhtml::ObjectType)


def test_xhtml::objecttype_constructor_exists():
    assert callable(xhtml::ObjectType.__init__)


def test_xhtml::objecttype_constructor_args():
    sig = inspect.signature(xhtml::ObjectType.__init__)
    params = list(sig.parameters.keys())
    assert "data" in params, "Missing parameter 'data'"
    assert "standby" in params, "Missing parameter 'standby'"
    assert "height" in params, "Missing parameter 'height'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "tabindex" in params, "Missing parameter 'tabindex'"
    assert "codebase" in params, "Missing parameter 'codebase'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "width" in params, "Missing parameter 'width'"
    assert "title" in params, "Missing parameter 'title'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "classid" in params, "Missing parameter 'classid'"
    assert "archive" in params, "Missing parameter 'archive'"
    assert "declare" in params, "Missing parameter 'declare'"
    assert "codetype" in params, "Missing parameter 'codetype'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::objecttype_has_data():
    assert hasattr(xhtml::ObjectType, "data")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_standby():
    assert hasattr(xhtml::ObjectType, "standby")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "standby" in klass.__dict__:
            descriptor = klass.__dict__["standby"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_height():
    assert hasattr(xhtml::ObjectType, "height")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_style():
    assert hasattr(xhtml::ObjectType, "style")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_id():
    assert hasattr(xhtml::ObjectType, "id")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_tabindex():
    assert hasattr(xhtml::ObjectType, "tabindex")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "tabindex" in klass.__dict__:
            descriptor = klass.__dict__["tabindex"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_codebase():
    assert hasattr(xhtml::ObjectType, "codebase")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "codebase" in klass.__dict__:
            descriptor = klass.__dict__["codebase"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_class_():
    assert hasattr(xhtml::ObjectType, "class_")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_usemap():
    assert hasattr(xhtml::ObjectType, "usemap")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_width():
    assert hasattr(xhtml::ObjectType, "width")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_title():
    assert hasattr(xhtml::ObjectType, "title")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_mixed():
    assert hasattr(xhtml::ObjectType, "mixed")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_classid():
    assert hasattr(xhtml::ObjectType, "classid")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "classid" in klass.__dict__:
            descriptor = klass.__dict__["classid"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_archive():
    assert hasattr(xhtml::ObjectType, "archive")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "archive" in klass.__dict__:
            descriptor = klass.__dict__["archive"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_declare():
    assert hasattr(xhtml::ObjectType, "declare")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "declare" in klass.__dict__:
            descriptor = klass.__dict__["declare"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_codetype():
    assert hasattr(xhtml::ObjectType, "codetype")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "codetype" in klass.__dict__:
            descriptor = klass.__dict__["codetype"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_type():
    assert hasattr(xhtml::ObjectType, "type")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_name():
    assert hasattr(xhtml::ObjectType, "name")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::objecttype_has_group():
    assert hasattr(xhtml::ObjectType, "group")
    descriptor = None
    for klass in xhtml::ObjectType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::acontent_is_not_abstract():
    assert not inspect.isabstract(xhtml::AContent)


def test_xhtml::acontent_constructor_exists():
    assert callable(xhtml::AContent.__init__)


def test_xhtml::acontent_constructor_args():
    sig = inspect.signature(xhtml::AContent.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_xhtml::acontent_has_mixed():
    assert hasattr(xhtml::AContent, "mixed")
    descriptor = None
    for klass in xhtml::AContent.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::acontent_has_group():
    assert hasattr(xhtml::AContent, "group")
    descriptor = None
    for klass in xhtml::AContent.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_inline_is_not_abstract():
    assert not inspect.isabstract(Inline)


def test_inline_constructor_exists():
    assert callable(Inline.__init__)


def test_inline_constructor_args():
    sig = inspect.signature(Inline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::ptype_is_not_abstract():
    assert not inspect.isabstract(xhtml::PType)


def test_xhtml::ptype_constructor_exists():
    assert callable(xhtml::PType.__init__)


def test_xhtml::ptype_constructor_args():
    sig = inspect.signature(xhtml::PType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::ptype_has_title():
    assert hasattr(xhtml::PType, "title")
    descriptor = None
    for klass in xhtml::PType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ptype_has_id():
    assert hasattr(xhtml::PType, "id")
    descriptor = None
    for klass in xhtml::PType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ptype_has_style():
    assert hasattr(xhtml::PType, "style")
    descriptor = None
    for klass in xhtml::PType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::ptype_has_class_():
    assert hasattr(xhtml::PType, "class_")
    descriptor = None
    for klass in xhtml::PType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::codetype_is_not_abstract():
    assert not inspect.isabstract(xhtml::CodeType)


def test_xhtml::codetype_constructor_exists():
    assert callable(xhtml::CodeType.__init__)


def test_xhtml::codetype_constructor_args():
    sig = inspect.signature(xhtml::CodeType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::codetype_has_title():
    assert hasattr(xhtml::CodeType, "title")
    descriptor = None
    for klass in xhtml::CodeType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::codetype_has_class_():
    assert hasattr(xhtml::CodeType, "class_")
    descriptor = None
    for klass in xhtml::CodeType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::codetype_has_style():
    assert hasattr(xhtml::CodeType, "style")
    descriptor = None
    for klass in xhtml::CodeType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::codetype_has_id():
    assert hasattr(xhtml::CodeType, "id")
    descriptor = None
    for klass in xhtml::CodeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h4type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H4Type)


def test_xhtml::h4type_constructor_exists():
    assert callable(xhtml::H4Type.__init__)


def test_xhtml::h4type_constructor_args():
    sig = inspect.signature(xhtml::H4Type.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::h4type_has_title():
    assert hasattr(xhtml::H4Type, "title")
    descriptor = None
    for klass in xhtml::H4Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h4type_has_class_():
    assert hasattr(xhtml::H4Type, "class_")
    descriptor = None
    for klass in xhtml::H4Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h4type_has_id():
    assert hasattr(xhtml::H4Type, "id")
    descriptor = None
    for klass in xhtml::H4Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h4type_has_style():
    assert hasattr(xhtml::H4Type, "style")
    descriptor = None
    for klass in xhtml::H4Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h5type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H5Type)


def test_xhtml::h5type_constructor_exists():
    assert callable(xhtml::H5Type.__init__)


def test_xhtml::h5type_constructor_args():
    sig = inspect.signature(xhtml::H5Type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::h5type_has_id():
    assert hasattr(xhtml::H5Type, "id")
    descriptor = None
    for klass in xhtml::H5Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h5type_has_style():
    assert hasattr(xhtml::H5Type, "style")
    descriptor = None
    for klass in xhtml::H5Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h5type_has_title():
    assert hasattr(xhtml::H5Type, "title")
    descriptor = None
    for klass in xhtml::H5Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h5type_has_class_():
    assert hasattr(xhtml::H5Type, "class_")
    descriptor = None
    for klass in xhtml::H5Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::dfntype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DfnType)


def test_xhtml::dfntype_constructor_exists():
    assert callable(xhtml::DfnType.__init__)


def test_xhtml::dfntype_constructor_args():
    sig = inspect.signature(xhtml::DfnType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::dfntype_has_title():
    assert hasattr(xhtml::DfnType, "title")
    descriptor = None
    for klass in xhtml::DfnType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dfntype_has_id():
    assert hasattr(xhtml::DfnType, "id")
    descriptor = None
    for klass in xhtml::DfnType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dfntype_has_style():
    assert hasattr(xhtml::DfnType, "style")
    descriptor = None
    for klass in xhtml::DfnType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dfntype_has_class_():
    assert hasattr(xhtml::DfnType, "class_")
    descriptor = None
    for klass in xhtml::DfnType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::suptype_is_not_abstract():
    assert not inspect.isabstract(xhtml::SupType)


def test_xhtml::suptype_constructor_exists():
    assert callable(xhtml::SupType.__init__)


def test_xhtml::suptype_constructor_args():
    sig = inspect.signature(xhtml::SupType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::suptype_has_class_():
    assert hasattr(xhtml::SupType, "class_")
    descriptor = None
    for klass in xhtml::SupType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::suptype_has_id():
    assert hasattr(xhtml::SupType, "id")
    descriptor = None
    for klass in xhtml::SupType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::suptype_has_style():
    assert hasattr(xhtml::SupType, "style")
    descriptor = None
    for klass in xhtml::SupType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::suptype_has_title():
    assert hasattr(xhtml::SupType, "title")
    descriptor = None
    for klass in xhtml::SupType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::striketype_is_not_abstract():
    assert not inspect.isabstract(xhtml::StrikeType)


def test_xhtml::striketype_constructor_exists():
    assert callable(xhtml::StrikeType.__init__)


def test_xhtml::striketype_constructor_args():
    sig = inspect.signature(xhtml::StrikeType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::striketype_has_class_():
    assert hasattr(xhtml::StrikeType, "class_")
    descriptor = None
    for klass in xhtml::StrikeType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::striketype_has_id():
    assert hasattr(xhtml::StrikeType, "id")
    descriptor = None
    for klass in xhtml::StrikeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::striketype_has_title():
    assert hasattr(xhtml::StrikeType, "title")
    descriptor = None
    for klass in xhtml::StrikeType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::striketype_has_style():
    assert hasattr(xhtml::StrikeType, "style")
    descriptor = None
    for klass in xhtml::StrikeType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::strongtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::StrongType)


def test_xhtml::strongtype_constructor_exists():
    assert callable(xhtml::StrongType.__init__)


def test_xhtml::strongtype_constructor_args():
    sig = inspect.signature(xhtml::StrongType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::strongtype_has_style():
    assert hasattr(xhtml::StrongType, "style")
    descriptor = None
    for klass in xhtml::StrongType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::strongtype_has_title():
    assert hasattr(xhtml::StrongType, "title")
    descriptor = None
    for klass in xhtml::StrongType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::strongtype_has_class_():
    assert hasattr(xhtml::StrongType, "class_")
    descriptor = None
    for klass in xhtml::StrongType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::strongtype_has_id():
    assert hasattr(xhtml::StrongType, "id")
    descriptor = None
    for klass in xhtml::StrongType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h2type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H2Type)


def test_xhtml::h2type_constructor_exists():
    assert callable(xhtml::H2Type.__init__)


def test_xhtml::h2type_constructor_args():
    sig = inspect.signature(xhtml::H2Type.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::h2type_has_class_():
    assert hasattr(xhtml::H2Type, "class_")
    descriptor = None
    for klass in xhtml::H2Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h2type_has_style():
    assert hasattr(xhtml::H2Type, "style")
    descriptor = None
    for klass in xhtml::H2Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h2type_has_title():
    assert hasattr(xhtml::H2Type, "title")
    descriptor = None
    for klass in xhtml::H2Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h2type_has_id():
    assert hasattr(xhtml::H2Type, "id")
    descriptor = None
    for klass in xhtml::H2Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::emtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::EmType)


def test_xhtml::emtype_constructor_exists():
    assert callable(xhtml::EmType.__init__)


def test_xhtml::emtype_constructor_args():
    sig = inspect.signature(xhtml::EmType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::emtype_has_id():
    assert hasattr(xhtml::EmType, "id")
    descriptor = None
    for klass in xhtml::EmType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::emtype_has_style():
    assert hasattr(xhtml::EmType, "style")
    descriptor = None
    for klass in xhtml::EmType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::emtype_has_class_():
    assert hasattr(xhtml::EmType, "class_")
    descriptor = None
    for klass in xhtml::EmType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::emtype_has_title():
    assert hasattr(xhtml::EmType, "title")
    descriptor = None
    for klass in xhtml::EmType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::citetype_is_not_abstract():
    assert not inspect.isabstract(xhtml::CiteType)


def test_xhtml::citetype_constructor_exists():
    assert callable(xhtml::CiteType.__init__)


def test_xhtml::citetype_constructor_args():
    sig = inspect.signature(xhtml::CiteType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::citetype_has_style():
    assert hasattr(xhtml::CiteType, "style")
    descriptor = None
    for klass in xhtml::CiteType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::citetype_has_id():
    assert hasattr(xhtml::CiteType, "id")
    descriptor = None
    for klass in xhtml::CiteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::citetype_has_class_():
    assert hasattr(xhtml::CiteType, "class_")
    descriptor = None
    for klass in xhtml::CiteType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::citetype_has_title():
    assert hasattr(xhtml::CiteType, "title")
    descriptor = None
    for klass in xhtml::CiteType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::utype_is_not_abstract():
    assert not inspect.isabstract(xhtml::UType)


def test_xhtml::utype_constructor_exists():
    assert callable(xhtml::UType.__init__)


def test_xhtml::utype_constructor_args():
    sig = inspect.signature(xhtml::UType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::utype_has_title():
    assert hasattr(xhtml::UType, "title")
    descriptor = None
    for klass in xhtml::UType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::utype_has_id():
    assert hasattr(xhtml::UType, "id")
    descriptor = None
    for klass in xhtml::UType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::utype_has_class_():
    assert hasattr(xhtml::UType, "class_")
    descriptor = None
    for klass in xhtml::UType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::utype_has_style():
    assert hasattr(xhtml::UType, "style")
    descriptor = None
    for klass in xhtml::UType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::captiontype_is_not_abstract():
    assert not inspect.isabstract(xhtml::CaptionType)


def test_xhtml::captiontype_constructor_exists():
    assert callable(xhtml::CaptionType.__init__)


def test_xhtml::captiontype_constructor_args():
    sig = inspect.signature(xhtml::CaptionType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::captiontype_has_style():
    assert hasattr(xhtml::CaptionType, "style")
    descriptor = None
    for klass in xhtml::CaptionType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::captiontype_has_title():
    assert hasattr(xhtml::CaptionType, "title")
    descriptor = None
    for klass in xhtml::CaptionType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::captiontype_has_class_():
    assert hasattr(xhtml::CaptionType, "class_")
    descriptor = None
    for klass in xhtml::CaptionType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::captiontype_has_id():
    assert hasattr(xhtml::CaptionType, "id")
    descriptor = None
    for klass in xhtml::CaptionType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::subtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::SubType)


def test_xhtml::subtype_constructor_exists():
    assert callable(xhtml::SubType.__init__)


def test_xhtml::subtype_constructor_args():
    sig = inspect.signature(xhtml::SubType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::subtype_has_class_():
    assert hasattr(xhtml::SubType, "class_")
    descriptor = None
    for klass in xhtml::SubType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::subtype_has_style():
    assert hasattr(xhtml::SubType, "style")
    descriptor = None
    for klass in xhtml::SubType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::subtype_has_id():
    assert hasattr(xhtml::SubType, "id")
    descriptor = None
    for klass in xhtml::SubType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::subtype_has_title():
    assert hasattr(xhtml::SubType, "title")
    descriptor = None
    for klass in xhtml::SubType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::tttype_is_not_abstract():
    assert not inspect.isabstract(xhtml::TtType)


def test_xhtml::tttype_constructor_exists():
    assert callable(xhtml::TtType.__init__)


def test_xhtml::tttype_constructor_args():
    sig = inspect.signature(xhtml::TtType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::tttype_has_title():
    assert hasattr(xhtml::TtType, "title")
    descriptor = None
    for klass in xhtml::TtType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tttype_has_id():
    assert hasattr(xhtml::TtType, "id")
    descriptor = None
    for klass in xhtml::TtType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tttype_has_class_():
    assert hasattr(xhtml::TtType, "class_")
    descriptor = None
    for klass in xhtml::TtType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::tttype_has_style():
    assert hasattr(xhtml::TtType, "style")
    descriptor = None
    for klass in xhtml::TtType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h6type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H6Type)


def test_xhtml::h6type_constructor_exists():
    assert callable(xhtml::H6Type.__init__)


def test_xhtml::h6type_constructor_args():
    sig = inspect.signature(xhtml::H6Type.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::h6type_has_class_():
    assert hasattr(xhtml::H6Type, "class_")
    descriptor = None
    for klass in xhtml::H6Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h6type_has_style():
    assert hasattr(xhtml::H6Type, "style")
    descriptor = None
    for klass in xhtml::H6Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h6type_has_title():
    assert hasattr(xhtml::H6Type, "title")
    descriptor = None
    for klass in xhtml::H6Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h6type_has_id():
    assert hasattr(xhtml::H6Type, "id")
    descriptor = None
    for klass in xhtml::H6Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::bigtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::BigType)


def test_xhtml::bigtype_constructor_exists():
    assert callable(xhtml::BigType.__init__)


def test_xhtml::bigtype_constructor_args():
    sig = inspect.signature(xhtml::BigType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::bigtype_has_id():
    assert hasattr(xhtml::BigType, "id")
    descriptor = None
    for klass in xhtml::BigType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bigtype_has_class_():
    assert hasattr(xhtml::BigType, "class_")
    descriptor = None
    for klass in xhtml::BigType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bigtype_has_title():
    assert hasattr(xhtml::BigType, "title")
    descriptor = None
    for klass in xhtml::BigType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::bigtype_has_style():
    assert hasattr(xhtml::BigType, "style")
    descriptor = None
    for klass in xhtml::BigType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::qtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::QType)


def test_xhtml::qtype_constructor_exists():
    assert callable(xhtml::QType.__init__)


def test_xhtml::qtype_constructor_args():
    sig = inspect.signature(xhtml::QType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "cite1" in params, "Missing parameter 'cite1'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::qtype_has_style():
    assert hasattr(xhtml::QType, "style")
    descriptor = None
    for klass in xhtml::QType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::qtype_has_id():
    assert hasattr(xhtml::QType, "id")
    descriptor = None
    for klass in xhtml::QType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::qtype_has_class_():
    assert hasattr(xhtml::QType, "class_")
    descriptor = None
    for klass in xhtml::QType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::qtype_has_cite1():
    assert hasattr(xhtml::QType, "cite1")
    descriptor = None
    for klass in xhtml::QType.__mro__:
        if "cite1" in klass.__dict__:
            descriptor = klass.__dict__["cite1"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::qtype_has_title():
    assert hasattr(xhtml::QType, "title")
    descriptor = None
    for klass in xhtml::QType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::smalltype_is_not_abstract():
    assert not inspect.isabstract(xhtml::SmallType)


def test_xhtml::smalltype_constructor_exists():
    assert callable(xhtml::SmallType.__init__)


def test_xhtml::smalltype_constructor_args():
    sig = inspect.signature(xhtml::SmallType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::smalltype_has_style():
    assert hasattr(xhtml::SmallType, "style")
    descriptor = None
    for klass in xhtml::SmallType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::smalltype_has_title():
    assert hasattr(xhtml::SmallType, "title")
    descriptor = None
    for klass in xhtml::SmallType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::smalltype_has_id():
    assert hasattr(xhtml::SmallType, "id")
    descriptor = None
    for klass in xhtml::SmallType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::smalltype_has_class_():
    assert hasattr(xhtml::SmallType, "class_")
    descriptor = None
    for klass in xhtml::SmallType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::kbdtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::KbdType)


def test_xhtml::kbdtype_constructor_exists():
    assert callable(xhtml::KbdType.__init__)


def test_xhtml::kbdtype_constructor_args():
    sig = inspect.signature(xhtml::KbdType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::kbdtype_has_style():
    assert hasattr(xhtml::KbdType, "style")
    descriptor = None
    for klass in xhtml::KbdType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::kbdtype_has_title():
    assert hasattr(xhtml::KbdType, "title")
    descriptor = None
    for klass in xhtml::KbdType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::kbdtype_has_class_():
    assert hasattr(xhtml::KbdType, "class_")
    descriptor = None
    for klass in xhtml::KbdType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::kbdtype_has_id():
    assert hasattr(xhtml::KbdType, "id")
    descriptor = None
    for klass in xhtml::KbdType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h3type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H3Type)


def test_xhtml::h3type_constructor_exists():
    assert callable(xhtml::H3Type.__init__)


def test_xhtml::h3type_constructor_args():
    sig = inspect.signature(xhtml::H3Type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::h3type_has_id():
    assert hasattr(xhtml::H3Type, "id")
    descriptor = None
    for klass in xhtml::H3Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h3type_has_class_():
    assert hasattr(xhtml::H3Type, "class_")
    descriptor = None
    for klass in xhtml::H3Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h3type_has_style():
    assert hasattr(xhtml::H3Type, "style")
    descriptor = None
    for klass in xhtml::H3Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h3type_has_title():
    assert hasattr(xhtml::H3Type, "title")
    descriptor = None
    for klass in xhtml::H3Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::btype_is_not_abstract():
    assert not inspect.isabstract(xhtml::BType)


def test_xhtml::btype_constructor_exists():
    assert callable(xhtml::BType.__init__)


def test_xhtml::btype_constructor_args():
    sig = inspect.signature(xhtml::BType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::btype_has_style():
    assert hasattr(xhtml::BType, "style")
    descriptor = None
    for klass in xhtml::BType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::btype_has_id():
    assert hasattr(xhtml::BType, "id")
    descriptor = None
    for klass in xhtml::BType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::btype_has_class_():
    assert hasattr(xhtml::BType, "class_")
    descriptor = None
    for klass in xhtml::BType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::btype_has_title():
    assert hasattr(xhtml::BType, "title")
    descriptor = None
    for klass in xhtml::BType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::addresstype_is_not_abstract():
    assert not inspect.isabstract(xhtml::AddressType)


def test_xhtml::addresstype_constructor_exists():
    assert callable(xhtml::AddressType.__init__)


def test_xhtml::addresstype_constructor_args():
    sig = inspect.signature(xhtml::AddressType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::addresstype_has_class_():
    assert hasattr(xhtml::AddressType, "class_")
    descriptor = None
    for klass in xhtml::AddressType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::addresstype_has_style():
    assert hasattr(xhtml::AddressType, "style")
    descriptor = None
    for klass in xhtml::AddressType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::addresstype_has_title():
    assert hasattr(xhtml::AddressType, "title")
    descriptor = None
    for klass in xhtml::AddressType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::addresstype_has_id():
    assert hasattr(xhtml::AddressType, "id")
    descriptor = None
    for klass in xhtml::AddressType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::acronymtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::AcronymType)


def test_xhtml::acronymtype_constructor_exists():
    assert callable(xhtml::AcronymType.__init__)


def test_xhtml::acronymtype_constructor_args():
    sig = inspect.signature(xhtml::AcronymType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::acronymtype_has_id():
    assert hasattr(xhtml::AcronymType, "id")
    descriptor = None
    for klass in xhtml::AcronymType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::acronymtype_has_title():
    assert hasattr(xhtml::AcronymType, "title")
    descriptor = None
    for klass in xhtml::AcronymType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::acronymtype_has_style():
    assert hasattr(xhtml::AcronymType, "style")
    descriptor = None
    for klass in xhtml::AcronymType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::acronymtype_has_class_():
    assert hasattr(xhtml::AcronymType, "class_")
    descriptor = None
    for klass in xhtml::AcronymType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::dttype_is_not_abstract():
    assert not inspect.isabstract(xhtml::DtType)


def test_xhtml::dttype_constructor_exists():
    assert callable(xhtml::DtType.__init__)


def test_xhtml::dttype_constructor_args():
    sig = inspect.signature(xhtml::DtType.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::dttype_has_title():
    assert hasattr(xhtml::DtType, "title")
    descriptor = None
    for klass in xhtml::DtType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dttype_has_style():
    assert hasattr(xhtml::DtType, "style")
    descriptor = None
    for klass in xhtml::DtType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dttype_has_class_():
    assert hasattr(xhtml::DtType, "class_")
    descriptor = None
    for klass in xhtml::DtType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::dttype_has_id():
    assert hasattr(xhtml::DtType, "id")
    descriptor = None
    for klass in xhtml::DtType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::samptype_is_not_abstract():
    assert not inspect.isabstract(xhtml::SampType)


def test_xhtml::samptype_constructor_exists():
    assert callable(xhtml::SampType.__init__)


def test_xhtml::samptype_constructor_args():
    sig = inspect.signature(xhtml::SampType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::samptype_has_style():
    assert hasattr(xhtml::SampType, "style")
    descriptor = None
    for klass in xhtml::SampType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::samptype_has_title():
    assert hasattr(xhtml::SampType, "title")
    descriptor = None
    for klass in xhtml::SampType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::samptype_has_id():
    assert hasattr(xhtml::SampType, "id")
    descriptor = None
    for klass in xhtml::SampType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::samptype_has_class_():
    assert hasattr(xhtml::SampType, "class_")
    descriptor = None
    for klass in xhtml::SampType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::h1type_is_not_abstract():
    assert not inspect.isabstract(xhtml::H1Type)


def test_xhtml::h1type_constructor_exists():
    assert callable(xhtml::H1Type.__init__)


def test_xhtml::h1type_constructor_args():
    sig = inspect.signature(xhtml::H1Type.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::h1type_has_style():
    assert hasattr(xhtml::H1Type, "style")
    descriptor = None
    for klass in xhtml::H1Type.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h1type_has_title():
    assert hasattr(xhtml::H1Type, "title")
    descriptor = None
    for klass in xhtml::H1Type.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h1type_has_class_():
    assert hasattr(xhtml::H1Type, "class_")
    descriptor = None
    for klass in xhtml::H1Type.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::h1type_has_id():
    assert hasattr(xhtml::H1Type, "id")
    descriptor = None
    for klass in xhtml::H1Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::itype_is_not_abstract():
    assert not inspect.isabstract(xhtml::IType)


def test_xhtml::itype_constructor_exists():
    assert callable(xhtml::IType.__init__)


def test_xhtml::itype_constructor_args():
    sig = inspect.signature(xhtml::IType.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_xhtml::itype_has_style():
    assert hasattr(xhtml::IType, "style")
    descriptor = None
    for klass in xhtml::IType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::itype_has_id():
    assert hasattr(xhtml::IType, "id")
    descriptor = None
    for klass in xhtml::IType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::itype_has_title():
    assert hasattr(xhtml::IType, "title")
    descriptor = None
    for klass in xhtml::IType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::itype_has_class_():
    assert hasattr(xhtml::IType, "class_")
    descriptor = None
    for klass in xhtml::IType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::vartype_is_not_abstract():
    assert not inspect.isabstract(xhtml::VarType)


def test_xhtml::vartype_constructor_exists():
    assert callable(xhtml::VarType.__init__)


def test_xhtml::vartype_constructor_args():
    sig = inspect.signature(xhtml::VarType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::vartype_has_class_():
    assert hasattr(xhtml::VarType, "class_")
    descriptor = None
    for klass in xhtml::VarType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::vartype_has_title():
    assert hasattr(xhtml::VarType, "title")
    descriptor = None
    for klass in xhtml::VarType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::vartype_has_style():
    assert hasattr(xhtml::VarType, "style")
    descriptor = None
    for klass in xhtml::VarType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::vartype_has_id():
    assert hasattr(xhtml::VarType, "id")
    descriptor = None
    for klass in xhtml::VarType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::abbrtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::AbbrType)


def test_xhtml::abbrtype_constructor_exists():
    assert callable(xhtml::AbbrType.__init__)


def test_xhtml::abbrtype_constructor_args():
    sig = inspect.signature(xhtml::AbbrType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"

def test_xhtml::abbrtype_has_class_():
    assert hasattr(xhtml::AbbrType, "class_")
    descriptor = None
    for klass in xhtml::AbbrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::abbrtype_has_style():
    assert hasattr(xhtml::AbbrType, "style")
    descriptor = None
    for klass in xhtml::AbbrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::abbrtype_has_id():
    assert hasattr(xhtml::AbbrType, "id")
    descriptor = None
    for klass in xhtml::AbbrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::abbrtype_has_title():
    assert hasattr(xhtml::AbbrType, "title")
    descriptor = None
    for klass in xhtml::AbbrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::spantype_is_not_abstract():
    assert not inspect.isabstract(xhtml::SpanType)


def test_xhtml::spantype_constructor_exists():
    assert callable(xhtml::SpanType.__init__)


def test_xhtml::spantype_constructor_args():
    sig = inspect.signature(xhtml::SpanType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "title" in params, "Missing parameter 'title'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "style" in params, "Missing parameter 'style'"

def test_xhtml::spantype_has_id():
    assert hasattr(xhtml::SpanType, "id")
    descriptor = None
    for klass in xhtml::SpanType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::spantype_has_title():
    assert hasattr(xhtml::SpanType, "title")
    descriptor = None
    for klass in xhtml::SpanType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::spantype_has_class_():
    assert hasattr(xhtml::SpanType, "class_")
    descriptor = None
    for klass in xhtml::SpanType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::spantype_has_style():
    assert hasattr(xhtml::SpanType, "style")
    descriptor = None
    for klass in xhtml::SpanType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::brtype_is_not_abstract():
    assert not inspect.isabstract(xhtml::BrType)


def test_xhtml::brtype_constructor_exists():
    assert callable(xhtml::BrType.__init__)


def test_xhtml::brtype_constructor_args():
    sig = inspect.signature(xhtml::BrType.__init__)
    params = list(sig.parameters.keys())
    assert "class_" in params, "Missing parameter 'class_'"
    assert "title" in params, "Missing parameter 'title'"
    assert "style" in params, "Missing parameter 'style'"
    assert "id" in params, "Missing parameter 'id'"

def test_xhtml::brtype_has_class_():
    assert hasattr(xhtml::BrType, "class_")
    descriptor = None
    for klass in xhtml::BrType.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::brtype_has_title():
    assert hasattr(xhtml::BrType, "title")
    descriptor = None
    for klass in xhtml::BrType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::brtype_has_style():
    assert hasattr(xhtml::BrType, "style")
    descriptor = None
    for klass in xhtml::BrType.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::brtype_has_id():
    assert hasattr(xhtml::BrType, "id")
    descriptor = None
    for klass in xhtml::BrType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_valuetypetype_exists():
    # Check that the Enumeration exists
    assert ValuetypeType is not None

def test_valuetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValuetypeType]
    expected_literals = [
        "object",
        "data",
        "ref",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValuetypeType"

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
        "poly",
        "circle",
        "default",
        "rect",
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

def test_aligntype_exists():
    # Check that the Enumeration exists
    assert AlignType is not None

def test_aligntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AlignType]
    expected_literals = [
        "center",
        "char",
        "justify",
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AlignType"

def test_valigntype_exists():
    # Check that the Enumeration exists
    assert ValignType is not None

def test_valigntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValignType]
    expected_literals = [
        "baseline",
        "bottom",
        "middle",
        "top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValignType"

def test_scope_exists():
    # Check that the Enumeration exists
    assert Scope is not None

def test_scope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Scope]
    expected_literals = [
        "col",
        "row",
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
xhtml::PreContent_strategy = st.builds(
    xhtml::PreContent,
    mixed=
        safe_text,
    group=
        safe_text
)
xhtml::Inline_strategy = st.builds(
    xhtml::Inline,
    group=
        safe_text,
    mixed=
        safe_text
)
xhtml::FormContent_strategy = st.builds(
    xhtml::FormContent,
    group=
        safe_text
)
xhtml::Flow_strategy = st.builds(
    xhtml::Flow,
    mixed=
        safe_text,
    group=
        safe_text
)
xhtml::TbodyType_strategy = st.builds(
    xhtml::TbodyType,
    charoff=
        safe_text,
    style=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::TrType_strategy = st.builds(
    xhtml::TrType,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    align=
        safe_text,
    group=
        safe_text,
    valign=
        safe_text,
    style=
        safe_text,
    charoff=
        safe_text,
    char=
        safe_text
)
xhtml::TheadType_strategy = st.builds(
    xhtml::TheadType,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    charoff=
        safe_text,
    align=
        safe_text,
    char=
        safe_text,
    valign=
        safe_text,
    class_=
        safe_text
)
xhtml::TfootType_strategy = st.builds(
    xhtml::TfootType,
    id=
        safe_text,
    title=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    valign=
        safe_text,
    charoff=
        safe_text,
    style=
        safe_text,
    align=
        safe_text
)
xhtml::ParamType_strategy = st.builds(
    xhtml::ParamType,
    value=
        safe_text,
    type=
        safe_text,
    id=
        safe_text,
    valuetype=
        safe_text,
    name=
        safe_text
)
xhtml::HtmlType_strategy = st.builds(
    xhtml::HtmlType,
    id=
        safe_text
)
xhtml::EStringToStringMapEntry_strategy = st.builds(
    xhtml::EStringToStringMapEntry,
)
xhtml::DocumentRoot_strategy = st.builds(
    xhtml::DocumentRoot,
    mixed=
        safe_text
)
Flow_strategy = st.builds(
    Flow,
)
xhtml::LiType_strategy = st.builds(
    xhtml::LiType,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml::ThType_strategy = st.builds(
    xhtml::ThType,
    id=
        safe_text,
    title=
        safe_text,
    headers=
        safe_text,
    valign=
        safe_text,
    align=
        safe_text,
    colspan=
        safe_text,
    class_=
        safe_text,
    rowspan=
        safe_text,
    abbr1=
        safe_text,
    charoff=
        safe_text,
    char=
        safe_text,
    style=
        safe_text,
    scope=
        safe_text,
    axis=
        safe_text
)
xhtml::TdType_strategy = st.builds(
    xhtml::TdType,
    char=
        safe_text,
    align=
        safe_text,
    valign=
        safe_text,
    scope=
        safe_text,
    class_=
        safe_text,
    colspan=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    rowspan=
        safe_text,
    abbr1=
        safe_text,
    style=
        safe_text,
    headers=
        safe_text,
    axis=
        safe_text,
    charoff=
        safe_text
)
xhtml::DdType_strategy = st.builds(
    xhtml::DdType,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml::ColType_strategy = st.builds(
    xhtml::ColType,
    span=
        safe_text,
    style=
        safe_text,
    width=
        safe_text,
    align=
        safe_text,
    id=
        safe_text,
    valign=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    charoff=
        safe_text,
    char=
        safe_text
)
xhtml::ColgroupType_strategy = st.builds(
    xhtml::ColgroupType,
    align=
        safe_text,
    char=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    charoff=
        safe_text,
    span=
        safe_text,
    width=
        safe_text,
    valign=
        safe_text,
    id=
        safe_text
)
Block_strategy = st.builds(
    Block,
)
xhtml::BodyType_strategy = st.builds(
    xhtml::BodyType,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml::BlockquoteType_strategy = st.builds(
    xhtml::BlockquoteType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    cite=
        safe_text
)
xhtml::HrType_strategy = st.builds(
    xhtml::HrType,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text
)
xhtml::PreType_strategy = st.builds(
    xhtml::PreType,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::TableType_strategy = st.builds(
    xhtml::TableType,
    cellspacing=
        safe_text,
    summary=
        safe_text,
    title=
        safe_text,
    cellpadding=
        safe_text,
    width=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    border=
        safe_text
)
xhtml::UlType_strategy = st.builds(
    xhtml::UlType,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::DivType_strategy = st.builds(
    xhtml::DivType,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml::DlType_strategy = st.builds(
    xhtml::DlType,
    style=
        safe_text,
    id=
        safe_text,
    group=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml::OlType_strategy = st.builds(
    xhtml::OlType,
    class_=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml::Block_strategy = st.builds(
    xhtml::Block,
    group=
        safe_text
)
AContent_strategy = st.builds(
    AContent,
)
xhtml::AType_strategy = st.builds(
    xhtml::AType,
    rev=
        safe_text,
    charset=
        safe_text,
    shape=
        safe_text,
    hreflang=
        safe_text,
    id=
        safe_text,
    name=
        safe_text,
    style=
        safe_text,
    href=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    coords=
        safe_text,
    rel=
        safe_text,
    type=
        safe_text
)
xhtml::InsType_strategy = st.builds(
    xhtml::InsType,
    cite1=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    datetime=
        safe_text
)
xhtml::DelType_strategy = st.builds(
    xhtml::DelType,
    id=
        safe_text,
    datetime=
        safe_text,
    cite1=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml::ImgType_strategy = st.builds(
    xhtml::ImgType,
    id=
        safe_text,
    ismap=
        safe_text,
    longdesc=
        safe_text,
    title=
        safe_text,
    src=
        safe_text,
    usemap=
        safe_text,
    style=
        safe_text,
    height=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text,
    alt=
        safe_text
)
xhtml::ObjectType_strategy = st.builds(
    xhtml::ObjectType,
    data=
        safe_text,
    standby=
        safe_text,
    height=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    tabindex=
        safe_text,
    codebase=
        safe_text,
    class_=
        safe_text,
    usemap=
        safe_text,
    width=
        safe_text,
    title=
        safe_text,
    mixed=
        safe_text,
    classid=
        safe_text,
    archive=
        safe_text,
    declare=
        safe_text,
    codetype=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    group=
        safe_text
)
xhtml::AContent_strategy = st.builds(
    xhtml::AContent,
    mixed=
        safe_text,
    group=
        safe_text
)
Inline_strategy = st.builds(
    Inline,
)
xhtml::PType_strategy = st.builds(
    xhtml::PType,
    title=
        safe_text,
    id=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml::CodeType_strategy = st.builds(
    xhtml::CodeType,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml::H4Type_strategy = st.builds(
    xhtml::H4Type,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text
)
xhtml::H5Type_strategy = st.builds(
    xhtml::H5Type,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml::DfnType_strategy = st.builds(
    xhtml::DfnType,
    title=
        safe_text,
    id=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml::SupType_strategy = st.builds(
    xhtml::SupType,
    class_=
        safe_text,
    id=
        safe_text,
    style=
        safe_text,
    title=
        safe_text
)
xhtml::StrikeType_strategy = st.builds(
    xhtml::StrikeType,
    class_=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    style=
        safe_text
)
xhtml::StrongType_strategy = st.builds(
    xhtml::StrongType,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml::H2Type_strategy = st.builds(
    xhtml::H2Type,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::EmType_strategy = st.builds(
    xhtml::EmType,
    id=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml::CiteType_strategy = st.builds(
    xhtml::CiteType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml::UType_strategy = st.builds(
    xhtml::UType,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml::CaptionType_strategy = st.builds(
    xhtml::CaptionType,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml::SubType_strategy = st.builds(
    xhtml::SubType,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text
)
xhtml::TtType_strategy = st.builds(
    xhtml::TtType,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml::H6Type_strategy = st.builds(
    xhtml::H6Type,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::BigType_strategy = st.builds(
    xhtml::BigType,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text
)
xhtml::QType_strategy = st.builds(
    xhtml::QType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    cite1=
        safe_text,
    title=
        safe_text
)
xhtml::SmallType_strategy = st.builds(
    xhtml::SmallType,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml::KbdType_strategy = st.builds(
    xhtml::KbdType,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml::H3Type_strategy = st.builds(
    xhtml::H3Type,
    id=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text
)
xhtml::BType_strategy = st.builds(
    xhtml::BType,
    style=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text,
    title=
        safe_text
)
xhtml::AddressType_strategy = st.builds(
    xhtml::AddressType,
    class_=
        safe_text,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text
)
xhtml::AcronymType_strategy = st.builds(
    xhtml::AcronymType,
    id=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text
)
xhtml::DtType_strategy = st.builds(
    xhtml::DtType,
    title=
        safe_text,
    style=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml::SampType_strategy = st.builds(
    xhtml::SampType,
    style=
        safe_text,
    title=
        safe_text,
    id=
        safe_text,
    class_=
        safe_text
)
xhtml::H1Type_strategy = st.builds(
    xhtml::H1Type,
    style=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    id=
        safe_text
)
xhtml::IType_strategy = st.builds(
    xhtml::IType,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text
)
xhtml::VarType_strategy = st.builds(
    xhtml::VarType,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)
xhtml::AbbrType_strategy = st.builds(
    xhtml::AbbrType,
    class_=
        safe_text,
    style=
        safe_text,
    id=
        safe_text,
    title=
        safe_text
)
xhtml::SpanType_strategy = st.builds(
    xhtml::SpanType,
    id=
        safe_text,
    title=
        safe_text,
    class_=
        safe_text,
    style=
        safe_text
)
xhtml::BrType_strategy = st.builds(
    xhtml::BrType,
    class_=
        safe_text,
    title=
        safe_text,
    style=
        safe_text,
    id=
        safe_text
)

@given(instance=PreContent_strategy)
@settings(max_examples=50)
def test_precontent_instantiation(instance):
    assert isinstance(instance, PreContent)

@given(instance=xhtml::PreContent_strategy)
@settings(max_examples=50)
def test_xhtml::precontent_instantiation(instance):
    assert isinstance(instance, xhtml::PreContent)

@given(instance=xhtml::PreContent_strategy)
def test_xhtml::precontent_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::PreContent_strategy)
def test_xhtml::precontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml::PreContent_strategy)
def test_xhtml::precontent_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::PreContent_strategy)
def test_xhtml::precontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::Inline_strategy)
@settings(max_examples=50)
def test_xhtml::inline_instantiation(instance):
    assert isinstance(instance, xhtml::Inline)

@given(instance=xhtml::Inline_strategy)
def test_xhtml::inline_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::Inline_strategy)
def test_xhtml::inline_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::Inline_strategy)
def test_xhtml::inline_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::Inline_strategy)
def test_xhtml::inline_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml::FormContent_strategy)
@settings(max_examples=50)
def test_xhtml::formcontent_instantiation(instance):
    assert isinstance(instance, xhtml::FormContent)

@given(instance=xhtml::FormContent_strategy)
def test_xhtml::formcontent_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::FormContent_strategy)
def test_xhtml::formcontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::Flow_strategy)
@settings(max_examples=50)
def test_xhtml::flow_instantiation(instance):
    assert isinstance(instance, xhtml::Flow)

@given(instance=xhtml::Flow_strategy)
def test_xhtml::flow_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::Flow_strategy)
def test_xhtml::flow_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml::Flow_strategy)
def test_xhtml::flow_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::Flow_strategy)
def test_xhtml::flow_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::TbodyType_strategy)
@settings(max_examples=50)
def test_xhtml::tbodytype_instantiation(instance):
    assert isinstance(instance, xhtml::TbodyType)

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TbodyType_strategy)
def test_xhtml::tbodytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TrType_strategy)
@settings(max_examples=50)
def test_xhtml::trtype_instantiation(instance):
    assert isinstance(instance, xhtml::TrType)

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::TrType_strategy)
def test_xhtml::trtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::TheadType_strategy)
@settings(max_examples=50)
def test_xhtml::theadtype_instantiation(instance):
    assert isinstance(instance, xhtml::TheadType)

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TheadType_strategy)
def test_xhtml::theadtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TfootType_strategy)
@settings(max_examples=50)
def test_xhtml::tfoottype_instantiation(instance):
    assert isinstance(instance, xhtml::TfootType)

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::TfootType_strategy)
def test_xhtml::tfoottype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::ParamType_strategy)
@settings(max_examples=50)
def test_xhtml::paramtype_instantiation(instance):
    assert isinstance(instance, xhtml::ParamType)

@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_valuetype_type(instance):
    assert isinstance(instance.valuetype, str)


@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_valuetype_setter(instance):
    original = instance.valuetype
    instance.valuetype = original
    assert instance.valuetype == original

@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xhtml::ParamType_strategy)
def test_xhtml::paramtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xhtml::HtmlType_strategy)
@settings(max_examples=50)
def test_xhtml::htmltype_instantiation(instance):
    assert isinstance(instance, xhtml::HtmlType)

@given(instance=xhtml::HtmlType_strategy)
def test_xhtml::htmltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::HtmlType_strategy)
def test_xhtml::htmltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_xhtml::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, xhtml::EStringToStringMapEntry)

@given(instance=xhtml::DocumentRoot_strategy)
@settings(max_examples=50)
def test_xhtml::documentroot_instantiation(instance):
    assert isinstance(instance, xhtml::DocumentRoot)

@given(instance=xhtml::DocumentRoot_strategy)
def test_xhtml::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::DocumentRoot_strategy)
def test_xhtml::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=xhtml::LiType_strategy)
@settings(max_examples=50)
def test_xhtml::litype_instantiation(instance):
    assert isinstance(instance, xhtml::LiType)

@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::LiType_strategy)
def test_xhtml::litype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ThType_strategy)
@settings(max_examples=50)
def test_xhtml::thtype_instantiation(instance):
    assert isinstance(instance, xhtml::ThType)

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_headers_type(instance):
    assert isinstance(instance.headers, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_headers_setter(instance):
    original = instance.headers
    instance.headers = original
    assert instance.headers == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_colspan_type(instance):
    assert isinstance(instance.colspan, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_rowspan_type(instance):
    assert isinstance(instance.rowspan, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_abbr1_type(instance):
    assert isinstance(instance.abbr1, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_abbr1_setter(instance):
    original = instance.abbr1
    instance.abbr1 = original
    assert instance.abbr1 == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_axis_type(instance):
    assert isinstance(instance.axis, str)


@given(instance=xhtml::ThType_strategy)
def test_xhtml::thtype_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original

@given(instance=xhtml::TdType_strategy)
@settings(max_examples=50)
def test_xhtml::tdtype_instantiation(instance):
    assert isinstance(instance, xhtml::TdType)

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_colspan_type(instance):
    assert isinstance(instance.colspan, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_rowspan_type(instance):
    assert isinstance(instance.rowspan, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_abbr1_type(instance):
    assert isinstance(instance.abbr1, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_abbr1_setter(instance):
    original = instance.abbr1
    instance.abbr1 = original
    assert instance.abbr1 == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_headers_type(instance):
    assert isinstance(instance.headers, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_headers_setter(instance):
    original = instance.headers
    instance.headers = original
    assert instance.headers == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_axis_type(instance):
    assert isinstance(instance.axis, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_axis_setter(instance):
    original = instance.axis
    instance.axis = original
    assert instance.axis == original

@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::TdType_strategy)
def test_xhtml::tdtype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::DdType_strategy)
@settings(max_examples=50)
def test_xhtml::ddtype_instantiation(instance):
    assert isinstance(instance, xhtml::DdType)

@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DdType_strategy)
def test_xhtml::ddtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ColType_strategy)
@settings(max_examples=50)
def test_xhtml::coltype_instantiation(instance):
    assert isinstance(instance, xhtml::ColType)

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::ColType_strategy)
def test_xhtml::coltype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::ColgroupType_strategy)
@settings(max_examples=50)
def test_xhtml::colgrouptype_instantiation(instance):
    assert isinstance(instance, xhtml::ColgroupType)

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_char_type(instance):
    assert isinstance(instance.char, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_char_setter(instance):
    original = instance.char
    instance.char = original
    assert instance.char == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_charoff_type(instance):
    assert isinstance(instance.charoff, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_charoff_setter(instance):
    original = instance.charoff
    instance.charoff = original
    assert instance.charoff == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_span_type(instance):
    assert isinstance(instance.span, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_span_setter(instance):
    original = instance.span
    instance.span = original
    assert instance.span == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ColgroupType_strategy)
def test_xhtml::colgrouptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=xhtml::BodyType_strategy)
@settings(max_examples=50)
def test_xhtml::bodytype_instantiation(instance):
    assert isinstance(instance, xhtml::BodyType)

@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::BodyType_strategy)
def test_xhtml::bodytype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::BlockquoteType_strategy)
@settings(max_examples=50)
def test_xhtml::blockquotetype_instantiation(instance):
    assert isinstance(instance, xhtml::BlockquoteType)

@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_cite_type(instance):
    assert isinstance(instance.cite, str)


@given(instance=xhtml::BlockquoteType_strategy)
def test_xhtml::blockquotetype_cite_setter(instance):
    original = instance.cite
    instance.cite = original
    assert instance.cite == original

@given(instance=xhtml::HrType_strategy)
@settings(max_examples=50)
def test_xhtml::hrtype_instantiation(instance):
    assert isinstance(instance, xhtml::HrType)

@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::HrType_strategy)
def test_xhtml::hrtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::PreType_strategy)
@settings(max_examples=50)
def test_xhtml::pretype_instantiation(instance):
    assert isinstance(instance, xhtml::PreType)

@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::PreType_strategy)
def test_xhtml::pretype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TableType_strategy)
@settings(max_examples=50)
def test_xhtml::tabletype_instantiation(instance):
    assert isinstance(instance, xhtml::TableType)

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_cellspacing_type(instance):
    assert isinstance(instance.cellspacing, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_summary_type(instance):
    assert isinstance(instance.summary, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_summary_setter(instance):
    original = instance.summary
    instance.summary = original
    assert instance.summary == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_cellpadding_type(instance):
    assert isinstance(instance.cellpadding, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=xhtml::TableType_strategy)
def test_xhtml::tabletype_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=xhtml::UlType_strategy)
@settings(max_examples=50)
def test_xhtml::ultype_instantiation(instance):
    assert isinstance(instance, xhtml::UlType)

@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::UlType_strategy)
def test_xhtml::ultype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DivType_strategy)
@settings(max_examples=50)
def test_xhtml::divtype_instantiation(instance):
    assert isinstance(instance, xhtml::DivType)

@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DivType_strategy)
def test_xhtml::divtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DlType_strategy)
@settings(max_examples=50)
def test_xhtml::dltype_instantiation(instance):
    assert isinstance(instance, xhtml::DlType)

@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DlType_strategy)
def test_xhtml::dltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::OlType_strategy)
@settings(max_examples=50)
def test_xhtml::oltype_instantiation(instance):
    assert isinstance(instance, xhtml::OlType)

@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::OlType_strategy)
def test_xhtml::oltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::Block_strategy)
@settings(max_examples=50)
def test_xhtml::block_instantiation(instance):
    assert isinstance(instance, xhtml::Block)

@given(instance=xhtml::Block_strategy)
def test_xhtml::block_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::Block_strategy)
def test_xhtml::block_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=AContent_strategy)
@settings(max_examples=50)
def test_acontent_instantiation(instance):
    assert isinstance(instance, AContent)

@given(instance=xhtml::AType_strategy)
@settings(max_examples=50)
def test_xhtml::atype_instantiation(instance):
    assert isinstance(instance, xhtml::AType)

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_rev_type(instance):
    assert isinstance(instance.rev, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_rev_setter(instance):
    original = instance.rev
    instance.rev = original
    assert instance.rev == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_charset_type(instance):
    assert isinstance(instance.charset, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_charset_setter(instance):
    original = instance.charset
    instance.charset = original
    assert instance.charset == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_hreflang_type(instance):
    assert isinstance(instance.hreflang, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_hreflang_setter(instance):
    original = instance.hreflang
    instance.hreflang = original
    assert instance.hreflang == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_coords_type(instance):
    assert isinstance(instance.coords, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_rel_type(instance):
    assert isinstance(instance.rel, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original

@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xhtml::AType_strategy)
def test_xhtml::atype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xhtml::InsType_strategy)
@settings(max_examples=50)
def test_xhtml::instype_instantiation(instance):
    assert isinstance(instance, xhtml::InsType)

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_cite1_type(instance):
    assert isinstance(instance.cite1, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_datetime_type(instance):
    assert isinstance(instance.datetime, str)


@given(instance=xhtml::InsType_strategy)
def test_xhtml::instype_datetime_setter(instance):
    original = instance.datetime
    instance.datetime = original
    assert instance.datetime == original

@given(instance=xhtml::DelType_strategy)
@settings(max_examples=50)
def test_xhtml::deltype_instantiation(instance):
    assert isinstance(instance, xhtml::DelType)

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_datetime_type(instance):
    assert isinstance(instance.datetime, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_datetime_setter(instance):
    original = instance.datetime
    instance.datetime = original
    assert instance.datetime == original

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_cite1_type(instance):
    assert isinstance(instance.cite1, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DelType_strategy)
def test_xhtml::deltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ImgType_strategy)
@settings(max_examples=50)
def test_xhtml::imgtype_instantiation(instance):
    assert isinstance(instance, xhtml::ImgType)

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_ismap_type(instance):
    assert isinstance(instance.ismap, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_longdesc_type(instance):
    assert isinstance(instance.longdesc, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_longdesc_setter(instance):
    original = instance.longdesc
    instance.longdesc = original
    assert instance.longdesc == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_usemap_type(instance):
    assert isinstance(instance.usemap, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_alt_type(instance):
    assert isinstance(instance.alt, str)


@given(instance=xhtml::ImgType_strategy)
def test_xhtml::imgtype_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original

@given(instance=xhtml::ObjectType_strategy)
@settings(max_examples=50)
def test_xhtml::objecttype_instantiation(instance):
    assert isinstance(instance, xhtml::ObjectType)

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_standby_type(instance):
    assert isinstance(instance.standby, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_standby_setter(instance):
    original = instance.standby
    instance.standby = original
    assert instance.standby == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_tabindex_type(instance):
    assert isinstance(instance.tabindex, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_tabindex_setter(instance):
    original = instance.tabindex
    instance.tabindex = original
    assert instance.tabindex == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_codebase_type(instance):
    assert isinstance(instance.codebase, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_codebase_setter(instance):
    original = instance.codebase
    instance.codebase = original
    assert instance.codebase == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_usemap_type(instance):
    assert isinstance(instance.usemap, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_classid_type(instance):
    assert isinstance(instance.classid, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_classid_setter(instance):
    original = instance.classid
    instance.classid = original
    assert instance.classid == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_archive_type(instance):
    assert isinstance(instance.archive, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_archive_setter(instance):
    original = instance.archive
    instance.archive = original
    assert instance.archive == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_declare_type(instance):
    assert isinstance(instance.declare, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_codetype_type(instance):
    assert isinstance(instance.codetype, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_codetype_setter(instance):
    original = instance.codetype
    instance.codetype = original
    assert instance.codetype == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::ObjectType_strategy)
def test_xhtml::objecttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xhtml::AContent_strategy)
@settings(max_examples=50)
def test_xhtml::acontent_instantiation(instance):
    assert isinstance(instance, xhtml::AContent)

@given(instance=xhtml::AContent_strategy)
def test_xhtml::acontent_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xhtml::AContent_strategy)
def test_xhtml::acontent_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xhtml::AContent_strategy)
def test_xhtml::acontent_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xhtml::AContent_strategy)
def test_xhtml::acontent_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Inline_strategy)
@settings(max_examples=50)
def test_inline_instantiation(instance):
    assert isinstance(instance, Inline)

@given(instance=xhtml::PType_strategy)
@settings(max_examples=50)
def test_xhtml::ptype_instantiation(instance):
    assert isinstance(instance, xhtml::PType)

@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::PType_strategy)
def test_xhtml::ptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::CodeType_strategy)
@settings(max_examples=50)
def test_xhtml::codetype_instantiation(instance):
    assert isinstance(instance, xhtml::CodeType)

@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::CodeType_strategy)
def test_xhtml::codetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H4Type_strategy)
@settings(max_examples=50)
def test_xhtml::h4type_instantiation(instance):
    assert isinstance(instance, xhtml::H4Type)

@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H4Type_strategy)
def test_xhtml::h4type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H5Type_strategy)
@settings(max_examples=50)
def test_xhtml::h5type_instantiation(instance):
    assert isinstance(instance, xhtml::H5Type)

@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H5Type_strategy)
def test_xhtml::h5type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DfnType_strategy)
@settings(max_examples=50)
def test_xhtml::dfntype_instantiation(instance):
    assert isinstance(instance, xhtml::DfnType)

@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DfnType_strategy)
def test_xhtml::dfntype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::SupType_strategy)
@settings(max_examples=50)
def test_xhtml::suptype_instantiation(instance):
    assert isinstance(instance, xhtml::SupType)

@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::SupType_strategy)
def test_xhtml::suptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::StrikeType_strategy)
@settings(max_examples=50)
def test_xhtml::striketype_instantiation(instance):
    assert isinstance(instance, xhtml::StrikeType)

@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::StrikeType_strategy)
def test_xhtml::striketype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::StrongType_strategy)
@settings(max_examples=50)
def test_xhtml::strongtype_instantiation(instance):
    assert isinstance(instance, xhtml::StrongType)

@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::StrongType_strategy)
def test_xhtml::strongtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H2Type_strategy)
@settings(max_examples=50)
def test_xhtml::h2type_instantiation(instance):
    assert isinstance(instance, xhtml::H2Type)

@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H2Type_strategy)
def test_xhtml::h2type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::EmType_strategy)
@settings(max_examples=50)
def test_xhtml::emtype_instantiation(instance):
    assert isinstance(instance, xhtml::EmType)

@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::EmType_strategy)
def test_xhtml::emtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::CiteType_strategy)
@settings(max_examples=50)
def test_xhtml::citetype_instantiation(instance):
    assert isinstance(instance, xhtml::CiteType)

@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::CiteType_strategy)
def test_xhtml::citetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::UType_strategy)
@settings(max_examples=50)
def test_xhtml::utype_instantiation(instance):
    assert isinstance(instance, xhtml::UType)

@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::UType_strategy)
def test_xhtml::utype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::CaptionType_strategy)
@settings(max_examples=50)
def test_xhtml::captiontype_instantiation(instance):
    assert isinstance(instance, xhtml::CaptionType)

@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::CaptionType_strategy)
def test_xhtml::captiontype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SubType_strategy)
@settings(max_examples=50)
def test_xhtml::subtype_instantiation(instance):
    assert isinstance(instance, xhtml::SubType)

@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::SubType_strategy)
def test_xhtml::subtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TtType_strategy)
@settings(max_examples=50)
def test_xhtml::tttype_instantiation(instance):
    assert isinstance(instance, xhtml::TtType)

@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::TtType_strategy)
def test_xhtml::tttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H6Type_strategy)
@settings(max_examples=50)
def test_xhtml::h6type_instantiation(instance):
    assert isinstance(instance, xhtml::H6Type)

@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H6Type_strategy)
def test_xhtml::h6type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::BigType_strategy)
@settings(max_examples=50)
def test_xhtml::bigtype_instantiation(instance):
    assert isinstance(instance, xhtml::BigType)

@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::BigType_strategy)
def test_xhtml::bigtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::QType_strategy)
@settings(max_examples=50)
def test_xhtml::qtype_instantiation(instance):
    assert isinstance(instance, xhtml::QType)

@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_cite1_type(instance):
    assert isinstance(instance.cite1, str)


@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_cite1_setter(instance):
    original = instance.cite1
    instance.cite1 = original
    assert instance.cite1 == original

@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::QType_strategy)
def test_xhtml::qtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::SmallType_strategy)
@settings(max_examples=50)
def test_xhtml::smalltype_instantiation(instance):
    assert isinstance(instance, xhtml::SmallType)

@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::SmallType_strategy)
def test_xhtml::smalltype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::KbdType_strategy)
@settings(max_examples=50)
def test_xhtml::kbdtype_instantiation(instance):
    assert isinstance(instance, xhtml::KbdType)

@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::KbdType_strategy)
def test_xhtml::kbdtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H3Type_strategy)
@settings(max_examples=50)
def test_xhtml::h3type_instantiation(instance):
    assert isinstance(instance, xhtml::H3Type)

@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H3Type_strategy)
def test_xhtml::h3type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::BType_strategy)
@settings(max_examples=50)
def test_xhtml::btype_instantiation(instance):
    assert isinstance(instance, xhtml::BType)

@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::BType_strategy)
def test_xhtml::btype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::AddressType_strategy)
@settings(max_examples=50)
def test_xhtml::addresstype_instantiation(instance):
    assert isinstance(instance, xhtml::AddressType)

@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::AddressType_strategy)
def test_xhtml::addresstype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::AcronymType_strategy)
@settings(max_examples=50)
def test_xhtml::acronymtype_instantiation(instance):
    assert isinstance(instance, xhtml::AcronymType)

@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::AcronymType_strategy)
def test_xhtml::acronymtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DtType_strategy)
@settings(max_examples=50)
def test_xhtml::dttype_instantiation(instance):
    assert isinstance(instance, xhtml::DtType)

@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::DtType_strategy)
def test_xhtml::dttype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SampType_strategy)
@settings(max_examples=50)
def test_xhtml::samptype_instantiation(instance):
    assert isinstance(instance, xhtml::SampType)

@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::SampType_strategy)
def test_xhtml::samptype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H1Type_strategy)
@settings(max_examples=50)
def test_xhtml::h1type_instantiation(instance):
    assert isinstance(instance, xhtml::H1Type)

@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::H1Type_strategy)
def test_xhtml::h1type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::IType_strategy)
@settings(max_examples=50)
def test_xhtml::itype_instantiation(instance):
    assert isinstance(instance, xhtml::IType)

@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::IType_strategy)
def test_xhtml::itype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::VarType_strategy)
@settings(max_examples=50)
def test_xhtml::vartype_instantiation(instance):
    assert isinstance(instance, xhtml::VarType)

@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::VarType_strategy)
def test_xhtml::vartype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::AbbrType_strategy)
@settings(max_examples=50)
def test_xhtml::abbrtype_instantiation(instance):
    assert isinstance(instance, xhtml::AbbrType)

@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::AbbrType_strategy)
def test_xhtml::abbrtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::SpanType_strategy)
@settings(max_examples=50)
def test_xhtml::spantype_instantiation(instance):
    assert isinstance(instance, xhtml::SpanType)

@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::SpanType_strategy)
def test_xhtml::spantype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::BrType_strategy)
@settings(max_examples=50)
def test_xhtml::brtype_instantiation(instance):
    assert isinstance(instance, xhtml::BrType)

@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xhtml::BrType_strategy)
def test_xhtml::brtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
