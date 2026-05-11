import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    idl::FormalParameterType,
    idl::TemplateDefinition,
    idl::FormalParameter,
    idl::ActualParameter,
    idl::FixedDefinition,
    idl::StateMember,
    Event,
    idl::EventDcl,
    idl::ConnectorExport,
    idl::ConnectorHeader,
    idl::PortExport,
    idl::EventForwardDcl,
    idl::HomeExport,
    idl::PrimaryKeySpec,
    idl::ComponentExport,
    idl::PrimaryExpr,
    ConstParamType,
    idl::ConstType,
    idl::UnaryExpr,
    idl::MultExpr,
    idl::AddExpr,
    idl::ShiftExpr,
    idl::AndExpr,
    idl::XOrExpr,
    ConstExp,
    idl::OrExpr,
    idl::ElementSpec,
    idl::CaseLabel,
    idl::Case,
    idl::SwitchBody,
    idl::SwitchTypeSpec,
    ConstrForwardDecl,
    idl::UnionForwardDecl,
    idl::StructForwardDecl,
    FormalParameterType,
    idl::ExceptionParamType,
    idl::EventParamType,
    idl::ValuetypeParamType,
    idl::InterfaceParamType,
    idl::EnumParamType,
    idl::ConstParamType,
    idl::SequenceParamType,
    idl::TypenameParamType,
    idl::UnionParamType,
    idl::StructParamType,
    idl::Declarator,
    idl::Member,
    TypeSpec,
    idl::ConstrTypeSpec,
    idl::SimpleTypeSpec,
    ActualParameter,
    idl::TypeSpec,
    ConstrTypeSpec,
    TypeDecl,
    idl::ConstrForwardDecl,
    idl::UnionType,
    idl::TypeDeclarator,
    Preproc,
    idl::Preproc::Include,
    ComponentExport,
    idl::ConsumesDcl,
    idl::EmitDcl,
    idl::PublishesDcl,
    Export,
    Definition,
    idl::ComponentForwardDecl,
    idl::TemplateModuleInst,
    idl::TemplateModule,
    idl::StructType,
    idl::Preproc,
    idl::Definition,
    idl::Import::decl,
    idl::Specification,
    Preproc::Pragma,
    idl::Preproc::Pragma::Conn::Type,
    idl::Preproc::Pragma::Prefix,
    idl::Preproc::Pragma,
    idl::Preproc::Endif,
    idl::Preproc::Define,
    idl::Preproc::Error,
    idl::Preproc::Else,
    idl::Preproc::If::Val,
    idl::Preproc::If::Compare,
    idl::Preproc::If,
    idl::Preproc::Undef,
    ComplexDeclarator,
    idl::ComplexDeclarator,
    Declarator,
    idl::ArrayDeclarator,
    idl::SimpleDeclarator,
    PrimaryExpr,
    idl::ConstExp,
    idl::Literal,
    ConstType,
    idl::FixedPtConstType,
    SwitchTypeSpec,
    idl::EnumType,
    SimpleTypeSpec,
    idl::TemplateTypeSpec,
    ParamTypeSpec,
    idl::BaseTypeSpec,
    OpTypeDecl,
    idl::ParamDcl,
    idl::PositiveIntConst,
    TemplateTypeSpec,
    idl::FixedPtType,
    idl::SequenceType,
    idl::WideStringType,
    idl::StringType,
    UnsignedInt,
    idl::UnsignedLongLongInt,
    idl::UnsignedLongInt,
    idl::UnsignedShortInt,
    SignedInt,
    idl::SignedLongLongInt,
    idl::SignedLongInt,
    idl::SignedShortInt,
    IntegerType,
    idl::UnsignedInt,
    idl::SignedInt,
    FloatingPtType,
    idl::LongDoubleType,
    idl::DoubleType,
    idl::FloatType,
    BaseTypeSpec,
    idl::OctetType,
    idl::AnyType,
    idl::IntegerType,
    idl::ValueBaseType,
    idl::WideCharType,
    idl::CharType,
    idl::ObjectType,
    idl::BooleanType,
    idl::FloatingPtType,
    idl::ParamTypeSpec,
    ConnectorExport,
    idl::PortDecl,
    PortExport,
    idl::UsesDcl,
    idl::ProvidesDcl,
    idl::AttrDecl,
    HomeExport,
    idl::FactoryDcl,
    idl::FinderDcl,
    idl::Export,
    idl::ScopedName,
    idl::ContextExpr,
    idl::ParameterDecls,
    idl::OpTypeDecl,
    idl::OpDecl,
    idl::ExceptionList,
    idl::AttrRaisesExpr,
    AttrDecl,
    idl::ReadOnlyAttrSpec,
    idl::AttrSpec,
    idl::Preproc::Pragma::Component,
    idl::Preproc::Pragma::Ndds,
    idl::Preproc::Pragma::Ciao::Ami4ccm::Idl,
    idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle,
    idl::Preproc::Pragma::Ciao::Ami4ccm::Interface,
    idl::Preproc::Pragma::Ciao::Lem,
    idl::InterfaceBody,
    idl::Interface::header,
    FixedDefinition,
    TemplateDefinition,
    idl::PortTypeDecl,
    idl::TypeDecl,
    idl::ExceptDecl,
    idl::Event,
    idl::HomeDecl,
    idl::FixedModule,
    idl::NativeType,
    idl::ComponentDecl,
    idl::ConstDecl,
    idl::Connector,
    idl::TemplateModuleRef,
    Interface::or::Forward::Decl,
    idl::Forward::decl,
    idl::Interface::decl,
    idl::Interface::or::Forward::Decl,
    idl::IDLComment,
    idl::Module,
    idl::Excluded::File::Marker,
    idl::File::Marker,
    idl::Preproc::Pragma::Misc,
    idl::Preproc::Pragma::DDS4CCM::Impl,
    idl::Preproc::Pragma::Home,
    idl::Preproc::Ifndef,
    idl::Preproc::Ifdef,
    idl::FileName,
    ParamDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idl::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(idl::FormalParameterType)


def test_idl::formalparametertype_constructor_exists():
    assert callable(idl::FormalParameterType.__init__)


def test_idl::formalparametertype_constructor_args():
    sig = inspect.signature(idl::FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_idl::templatedefinition_is_not_abstract():
    assert not inspect.isabstract(idl::TemplateDefinition)


def test_idl::templatedefinition_constructor_exists():
    assert callable(idl::TemplateDefinition.__init__)


def test_idl::templatedefinition_constructor_args():
    sig = inspect.signature(idl::TemplateDefinition.__init__)
    params = list(sig.parameters.keys())



def test_idl::formalparameter_is_not_abstract():
    assert not inspect.isabstract(idl::FormalParameter)


def test_idl::formalparameter_constructor_exists():
    assert callable(idl::FormalParameter.__init__)


def test_idl::formalparameter_constructor_args():
    sig = inspect.signature(idl::FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::formalparameter_has_name():
    assert hasattr(idl::FormalParameter, "name")
    descriptor = None
    for klass in idl::FormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::actualparameter_is_not_abstract():
    assert not inspect.isabstract(idl::ActualParameter)


def test_idl::actualparameter_constructor_exists():
    assert callable(idl::ActualParameter.__init__)


def test_idl::actualparameter_constructor_args():
    sig = inspect.signature(idl::ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_idl::fixeddefinition_is_not_abstract():
    assert not inspect.isabstract(idl::FixedDefinition)


def test_idl::fixeddefinition_constructor_exists():
    assert callable(idl::FixedDefinition.__init__)


def test_idl::fixeddefinition_constructor_args():
    sig = inspect.signature(idl::FixedDefinition.__init__)
    params = list(sig.parameters.keys())



def test_idl::statemember_is_not_abstract():
    assert not inspect.isabstract(idl::StateMember)


def test_idl::statemember_constructor_exists():
    assert callable(idl::StateMember.__init__)


def test_idl::statemember_constructor_args():
    sig = inspect.signature(idl::StateMember.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "names" in params, "Missing parameter 'names'"

def test_idl::statemember_has_isPublic():
    assert hasattr(idl::StateMember, "isPublic")
    descriptor = None
    for klass in idl::StateMember.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_idl::statemember_has_names():
    assert hasattr(idl::StateMember, "names")
    descriptor = None
    for klass in idl::StateMember.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_idl::eventdcl_is_not_abstract():
    assert not inspect.isabstract(idl::EventDcl)


def test_idl::eventdcl_constructor_exists():
    assert callable(idl::EventDcl.__init__)


def test_idl::eventdcl_constructor_args():
    sig = inspect.signature(idl::EventDcl.__init__)
    params = list(sig.parameters.keys())
    assert "isTruncatable" in params, "Missing parameter 'isTruncatable'"
    assert "isCustom" in params, "Missing parameter 'isCustom'"

def test_idl::eventdcl_has_isTruncatable():
    assert hasattr(idl::EventDcl, "isTruncatable")
    descriptor = None
    for klass in idl::EventDcl.__mro__:
        if "isTruncatable" in klass.__dict__:
            descriptor = klass.__dict__["isTruncatable"]
            break
    assert isinstance(descriptor, property)

def test_idl::eventdcl_has_isCustom():
    assert hasattr(idl::EventDcl, "isCustom")
    descriptor = None
    for klass in idl::EventDcl.__mro__:
        if "isCustom" in klass.__dict__:
            descriptor = klass.__dict__["isCustom"]
            break
    assert isinstance(descriptor, property)



def test_idl::connectorexport_is_not_abstract():
    assert not inspect.isabstract(idl::ConnectorExport)


def test_idl::connectorexport_constructor_exists():
    assert callable(idl::ConnectorExport.__init__)


def test_idl::connectorexport_constructor_args():
    sig = inspect.signature(idl::ConnectorExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::connectorheader_is_not_abstract():
    assert not inspect.isabstract(idl::ConnectorHeader)


def test_idl::connectorheader_constructor_exists():
    assert callable(idl::ConnectorHeader.__init__)


def test_idl::connectorheader_constructor_args():
    sig = inspect.signature(idl::ConnectorHeader.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::connectorheader_has_name():
    assert hasattr(idl::ConnectorHeader, "name")
    descriptor = None
    for klass in idl::ConnectorHeader.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::portexport_is_not_abstract():
    assert not inspect.isabstract(idl::PortExport)


def test_idl::portexport_constructor_exists():
    assert callable(idl::PortExport.__init__)


def test_idl::portexport_constructor_args():
    sig = inspect.signature(idl::PortExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::eventforwarddcl_is_not_abstract():
    assert not inspect.isabstract(idl::EventForwardDcl)


def test_idl::eventforwarddcl_constructor_exists():
    assert callable(idl::EventForwardDcl.__init__)


def test_idl::eventforwarddcl_constructor_args():
    sig = inspect.signature(idl::EventForwardDcl.__init__)
    params = list(sig.parameters.keys())



def test_idl::homeexport_is_not_abstract():
    assert not inspect.isabstract(idl::HomeExport)


def test_idl::homeexport_constructor_exists():
    assert callable(idl::HomeExport.__init__)


def test_idl::homeexport_constructor_args():
    sig = inspect.signature(idl::HomeExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::primarykeyspec_is_not_abstract():
    assert not inspect.isabstract(idl::PrimaryKeySpec)


def test_idl::primarykeyspec_constructor_exists():
    assert callable(idl::PrimaryKeySpec.__init__)


def test_idl::primarykeyspec_constructor_args():
    sig = inspect.signature(idl::PrimaryKeySpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::componentexport_is_not_abstract():
    assert not inspect.isabstract(idl::ComponentExport)


def test_idl::componentexport_constructor_exists():
    assert callable(idl::ComponentExport.__init__)


def test_idl::componentexport_constructor_args():
    sig = inspect.signature(idl::ComponentExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::primaryexpr_is_not_abstract():
    assert not inspect.isabstract(idl::PrimaryExpr)


def test_idl::primaryexpr_constructor_exists():
    assert callable(idl::PrimaryExpr.__init__)


def test_idl::primaryexpr_constructor_args():
    sig = inspect.signature(idl::PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_constparamtype_is_not_abstract():
    assert not inspect.isabstract(ConstParamType)


def test_constparamtype_constructor_exists():
    assert callable(ConstParamType.__init__)


def test_constparamtype_constructor_args():
    sig = inspect.signature(ConstParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::consttype_is_not_abstract():
    assert not inspect.isabstract(idl::ConstType)


def test_idl::consttype_constructor_exists():
    assert callable(idl::ConstType.__init__)


def test_idl::consttype_constructor_args():
    sig = inspect.signature(idl::ConstType.__init__)
    params = list(sig.parameters.keys())



def test_idl::unaryexpr_is_not_abstract():
    assert not inspect.isabstract(idl::UnaryExpr)


def test_idl::unaryexpr_constructor_exists():
    assert callable(idl::UnaryExpr.__init__)


def test_idl::unaryexpr_constructor_args():
    sig = inspect.signature(idl::UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::unaryexpr_has_op():
    assert hasattr(idl::UnaryExpr, "op")
    descriptor = None
    for klass in idl::UnaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::multexpr_is_not_abstract():
    assert not inspect.isabstract(idl::MultExpr)


def test_idl::multexpr_constructor_exists():
    assert callable(idl::MultExpr.__init__)


def test_idl::multexpr_constructor_args():
    sig = inspect.signature(idl::MultExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::multexpr_has_op():
    assert hasattr(idl::MultExpr, "op")
    descriptor = None
    for klass in idl::MultExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::addexpr_is_not_abstract():
    assert not inspect.isabstract(idl::AddExpr)


def test_idl::addexpr_constructor_exists():
    assert callable(idl::AddExpr.__init__)


def test_idl::addexpr_constructor_args():
    sig = inspect.signature(idl::AddExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::addexpr_has_op():
    assert hasattr(idl::AddExpr, "op")
    descriptor = None
    for klass in idl::AddExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::shiftexpr_is_not_abstract():
    assert not inspect.isabstract(idl::ShiftExpr)


def test_idl::shiftexpr_constructor_exists():
    assert callable(idl::ShiftExpr.__init__)


def test_idl::shiftexpr_constructor_args():
    sig = inspect.signature(idl::ShiftExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::shiftexpr_has_op():
    assert hasattr(idl::ShiftExpr, "op")
    descriptor = None
    for klass in idl::ShiftExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::andexpr_is_not_abstract():
    assert not inspect.isabstract(idl::AndExpr)


def test_idl::andexpr_constructor_exists():
    assert callable(idl::AndExpr.__init__)


def test_idl::andexpr_constructor_args():
    sig = inspect.signature(idl::AndExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::andexpr_has_op():
    assert hasattr(idl::AndExpr, "op")
    descriptor = None
    for klass in idl::AndExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::xorexpr_is_not_abstract():
    assert not inspect.isabstract(idl::XOrExpr)


def test_idl::xorexpr_constructor_exists():
    assert callable(idl::XOrExpr.__init__)


def test_idl::xorexpr_constructor_args():
    sig = inspect.signature(idl::XOrExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::xorexpr_has_op():
    assert hasattr(idl::XOrExpr, "op")
    descriptor = None
    for klass in idl::XOrExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_constexp_is_not_abstract():
    assert not inspect.isabstract(ConstExp)


def test_constexp_constructor_exists():
    assert callable(ConstExp.__init__)


def test_constexp_constructor_args():
    sig = inspect.signature(ConstExp.__init__)
    params = list(sig.parameters.keys())



def test_idl::orexpr_is_not_abstract():
    assert not inspect.isabstract(idl::OrExpr)


def test_idl::orexpr_constructor_exists():
    assert callable(idl::OrExpr.__init__)


def test_idl::orexpr_constructor_args():
    sig = inspect.signature(idl::OrExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::orexpr_has_op():
    assert hasattr(idl::OrExpr, "op")
    descriptor = None
    for klass in idl::OrExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::elementspec_is_not_abstract():
    assert not inspect.isabstract(idl::ElementSpec)


def test_idl::elementspec_constructor_exists():
    assert callable(idl::ElementSpec.__init__)


def test_idl::elementspec_constructor_args():
    sig = inspect.signature(idl::ElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::caselabel_is_not_abstract():
    assert not inspect.isabstract(idl::CaseLabel)


def test_idl::caselabel_constructor_exists():
    assert callable(idl::CaseLabel.__init__)


def test_idl::caselabel_constructor_args():
    sig = inspect.signature(idl::CaseLabel.__init__)
    params = list(sig.parameters.keys())
    assert "isCase" in params, "Missing parameter 'isCase'"
    assert "isDefault" in params, "Missing parameter 'isDefault'"

def test_idl::caselabel_has_isCase():
    assert hasattr(idl::CaseLabel, "isCase")
    descriptor = None
    for klass in idl::CaseLabel.__mro__:
        if "isCase" in klass.__dict__:
            descriptor = klass.__dict__["isCase"]
            break
    assert isinstance(descriptor, property)

def test_idl::caselabel_has_isDefault():
    assert hasattr(idl::CaseLabel, "isDefault")
    descriptor = None
    for klass in idl::CaseLabel.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)



def test_idl::case_is_not_abstract():
    assert not inspect.isabstract(idl::Case)


def test_idl::case_constructor_exists():
    assert callable(idl::Case.__init__)


def test_idl::case_constructor_args():
    sig = inspect.signature(idl::Case.__init__)
    params = list(sig.parameters.keys())



def test_idl::switchbody_is_not_abstract():
    assert not inspect.isabstract(idl::SwitchBody)


def test_idl::switchbody_constructor_exists():
    assert callable(idl::SwitchBody.__init__)


def test_idl::switchbody_constructor_args():
    sig = inspect.signature(idl::SwitchBody.__init__)
    params = list(sig.parameters.keys())



def test_idl::switchtypespec_is_not_abstract():
    assert not inspect.isabstract(idl::SwitchTypeSpec)


def test_idl::switchtypespec_constructor_exists():
    assert callable(idl::SwitchTypeSpec.__init__)


def test_idl::switchtypespec_constructor_args():
    sig = inspect.signature(idl::SwitchTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_constrforwarddecl_is_not_abstract():
    assert not inspect.isabstract(ConstrForwardDecl)


def test_constrforwarddecl_constructor_exists():
    assert callable(ConstrForwardDecl.__init__)


def test_constrforwarddecl_constructor_args():
    sig = inspect.signature(ConstrForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::unionforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl::UnionForwardDecl)


def test_idl::unionforwarddecl_constructor_exists():
    assert callable(idl::UnionForwardDecl.__init__)


def test_idl::unionforwarddecl_constructor_args():
    sig = inspect.signature(idl::UnionForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::structforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl::StructForwardDecl)


def test_idl::structforwarddecl_constructor_exists():
    assert callable(idl::StructForwardDecl.__init__)


def test_idl::structforwarddecl_constructor_args():
    sig = inspect.signature(idl::StructForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_idl::exceptionparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::ExceptionParamType)


def test_idl::exceptionparamtype_constructor_exists():
    assert callable(idl::ExceptionParamType.__init__)


def test_idl::exceptionparamtype_constructor_args():
    sig = inspect.signature(idl::ExceptionParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::eventparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::EventParamType)


def test_idl::eventparamtype_constructor_exists():
    assert callable(idl::EventParamType.__init__)


def test_idl::eventparamtype_constructor_args():
    sig = inspect.signature(idl::EventParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::valuetypeparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::ValuetypeParamType)


def test_idl::valuetypeparamtype_constructor_exists():
    assert callable(idl::ValuetypeParamType.__init__)


def test_idl::valuetypeparamtype_constructor_args():
    sig = inspect.signature(idl::ValuetypeParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::interfaceparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::InterfaceParamType)


def test_idl::interfaceparamtype_constructor_exists():
    assert callable(idl::InterfaceParamType.__init__)


def test_idl::interfaceparamtype_constructor_args():
    sig = inspect.signature(idl::InterfaceParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::enumparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::EnumParamType)


def test_idl::enumparamtype_constructor_exists():
    assert callable(idl::EnumParamType.__init__)


def test_idl::enumparamtype_constructor_args():
    sig = inspect.signature(idl::EnumParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::constparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::ConstParamType)


def test_idl::constparamtype_constructor_exists():
    assert callable(idl::ConstParamType.__init__)


def test_idl::constparamtype_constructor_args():
    sig = inspect.signature(idl::ConstParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::sequenceparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::SequenceParamType)


def test_idl::sequenceparamtype_constructor_exists():
    assert callable(idl::SequenceParamType.__init__)


def test_idl::sequenceparamtype_constructor_args():
    sig = inspect.signature(idl::SequenceParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::typenameparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::TypenameParamType)


def test_idl::typenameparamtype_constructor_exists():
    assert callable(idl::TypenameParamType.__init__)


def test_idl::typenameparamtype_constructor_args():
    sig = inspect.signature(idl::TypenameParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::unionparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::UnionParamType)


def test_idl::unionparamtype_constructor_exists():
    assert callable(idl::UnionParamType.__init__)


def test_idl::unionparamtype_constructor_args():
    sig = inspect.signature(idl::UnionParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::structparamtype_is_not_abstract():
    assert not inspect.isabstract(idl::StructParamType)


def test_idl::structparamtype_constructor_exists():
    assert callable(idl::StructParamType.__init__)


def test_idl::structparamtype_constructor_args():
    sig = inspect.signature(idl::StructParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl::declarator_is_not_abstract():
    assert not inspect.isabstract(idl::Declarator)


def test_idl::declarator_constructor_exists():
    assert callable(idl::Declarator.__init__)


def test_idl::declarator_constructor_args():
    sig = inspect.signature(idl::Declarator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_idl::declarator_has_id():
    assert hasattr(idl::Declarator, "id")
    descriptor = None
    for klass in idl::Declarator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_idl::member_is_not_abstract():
    assert not inspect.isabstract(idl::Member)


def test_idl::member_constructor_exists():
    assert callable(idl::Member.__init__)


def test_idl::member_constructor_args():
    sig = inspect.signature(idl::Member.__init__)
    params = list(sig.parameters.keys())



def test_typespec_is_not_abstract():
    assert not inspect.isabstract(TypeSpec)


def test_typespec_constructor_exists():
    assert callable(TypeSpec.__init__)


def test_typespec_constructor_args():
    sig = inspect.signature(TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::constrtypespec_is_not_abstract():
    assert not inspect.isabstract(idl::ConstrTypeSpec)


def test_idl::constrtypespec_constructor_exists():
    assert callable(idl::ConstrTypeSpec.__init__)


def test_idl::constrtypespec_constructor_args():
    sig = inspect.signature(idl::ConstrTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::simpletypespec_is_not_abstract():
    assert not inspect.isabstract(idl::SimpleTypeSpec)


def test_idl::simpletypespec_constructor_exists():
    assert callable(idl::SimpleTypeSpec.__init__)


def test_idl::simpletypespec_constructor_args():
    sig = inspect.signature(idl::SimpleTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_idl::typespec_is_not_abstract():
    assert not inspect.isabstract(idl::TypeSpec)


def test_idl::typespec_constructor_exists():
    assert callable(idl::TypeSpec.__init__)


def test_idl::typespec_constructor_args():
    sig = inspect.signature(idl::TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_constrtypespec_is_not_abstract():
    assert not inspect.isabstract(ConstrTypeSpec)


def test_constrtypespec_constructor_exists():
    assert callable(ConstrTypeSpec.__init__)


def test_constrtypespec_constructor_args():
    sig = inspect.signature(ConstrTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_typedecl_is_not_abstract():
    assert not inspect.isabstract(TypeDecl)


def test_typedecl_constructor_exists():
    assert callable(TypeDecl.__init__)


def test_typedecl_constructor_args():
    sig = inspect.signature(TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::constrforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl::ConstrForwardDecl)


def test_idl::constrforwarddecl_constructor_exists():
    assert callable(idl::ConstrForwardDecl.__init__)


def test_idl::constrforwarddecl_constructor_args():
    sig = inspect.signature(idl::ConstrForwardDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::constrforwarddecl_has_name():
    assert hasattr(idl::ConstrForwardDecl, "name")
    descriptor = None
    for klass in idl::ConstrForwardDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::uniontype_is_not_abstract():
    assert not inspect.isabstract(idl::UnionType)


def test_idl::uniontype_constructor_exists():
    assert callable(idl::UnionType.__init__)


def test_idl::uniontype_constructor_args():
    sig = inspect.signature(idl::UnionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::uniontype_has_name():
    assert hasattr(idl::UnionType, "name")
    descriptor = None
    for klass in idl::UnionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::typedeclarator_is_not_abstract():
    assert not inspect.isabstract(idl::TypeDeclarator)


def test_idl::typedeclarator_constructor_exists():
    assert callable(idl::TypeDeclarator.__init__)


def test_idl::typedeclarator_constructor_args():
    sig = inspect.signature(idl::TypeDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_preproc_is_not_abstract():
    assert not inspect.isabstract(Preproc)


def test_preproc_constructor_exists():
    assert callable(Preproc.__init__)


def test_preproc_constructor_args():
    sig = inspect.signature(Preproc.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::include_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Include)


def test_idl::preproc::include_constructor_exists():
    assert callable(idl::Preproc::Include.__init__)


def test_idl::preproc::include_constructor_args():
    sig = inspect.signature(idl::Preproc::Include.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_idl::preproc::include_has_strValue():
    assert hasattr(idl::Preproc::Include, "strValue")
    descriptor = None
    for klass in idl::Preproc::Include.__mro__:
        if "strValue" in klass.__dict__:
            descriptor = klass.__dict__["strValue"]
            break
    assert isinstance(descriptor, property)



def test_componentexport_is_not_abstract():
    assert not inspect.isabstract(ComponentExport)


def test_componentexport_constructor_exists():
    assert callable(ComponentExport.__init__)


def test_componentexport_constructor_args():
    sig = inspect.signature(ComponentExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::consumesdcl_is_not_abstract():
    assert not inspect.isabstract(idl::ConsumesDcl)


def test_idl::consumesdcl_constructor_exists():
    assert callable(idl::ConsumesDcl.__init__)


def test_idl::consumesdcl_constructor_args():
    sig = inspect.signature(idl::ConsumesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::consumesdcl_has_name():
    assert hasattr(idl::ConsumesDcl, "name")
    descriptor = None
    for klass in idl::ConsumesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::emitdcl_is_not_abstract():
    assert not inspect.isabstract(idl::EmitDcl)


def test_idl::emitdcl_constructor_exists():
    assert callable(idl::EmitDcl.__init__)


def test_idl::emitdcl_constructor_args():
    sig = inspect.signature(idl::EmitDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::emitdcl_has_name():
    assert hasattr(idl::EmitDcl, "name")
    descriptor = None
    for klass in idl::EmitDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::publishesdcl_is_not_abstract():
    assert not inspect.isabstract(idl::PublishesDcl)


def test_idl::publishesdcl_constructor_exists():
    assert callable(idl::PublishesDcl.__init__)


def test_idl::publishesdcl_constructor_args():
    sig = inspect.signature(idl::PublishesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::publishesdcl_has_name():
    assert hasattr(idl::PublishesDcl, "name")
    descriptor = None
    for klass in idl::PublishesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_export_is_not_abstract():
    assert not inspect.isabstract(Export)


def test_export_constructor_exists():
    assert callable(Export.__init__)


def test_export_constructor_args():
    sig = inspect.signature(Export.__init__)
    params = list(sig.parameters.keys())



def test_definition_is_not_abstract():
    assert not inspect.isabstract(Definition)


def test_definition_constructor_exists():
    assert callable(Definition.__init__)


def test_definition_constructor_args():
    sig = inspect.signature(Definition.__init__)
    params = list(sig.parameters.keys())



def test_idl::componentforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl::ComponentForwardDecl)


def test_idl::componentforwarddecl_constructor_exists():
    assert callable(idl::ComponentForwardDecl.__init__)


def test_idl::componentforwarddecl_constructor_args():
    sig = inspect.signature(idl::ComponentForwardDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::componentforwarddecl_has_name():
    assert hasattr(idl::ComponentForwardDecl, "name")
    descriptor = None
    for klass in idl::ComponentForwardDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::templatemoduleinst_is_not_abstract():
    assert not inspect.isabstract(idl::TemplateModuleInst)


def test_idl::templatemoduleinst_constructor_exists():
    assert callable(idl::TemplateModuleInst.__init__)


def test_idl::templatemoduleinst_constructor_args():
    sig = inspect.signature(idl::TemplateModuleInst.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::templatemoduleinst_has_name():
    assert hasattr(idl::TemplateModuleInst, "name")
    descriptor = None
    for klass in idl::TemplateModuleInst.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::templatemodule_is_not_abstract():
    assert not inspect.isabstract(idl::TemplateModule)


def test_idl::templatemodule_constructor_exists():
    assert callable(idl::TemplateModule.__init__)


def test_idl::templatemodule_constructor_args():
    sig = inspect.signature(idl::TemplateModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::templatemodule_has_name():
    assert hasattr(idl::TemplateModule, "name")
    descriptor = None
    for klass in idl::TemplateModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::structtype_is_not_abstract():
    assert not inspect.isabstract(idl::StructType)


def test_idl::structtype_constructor_exists():
    assert callable(idl::StructType.__init__)


def test_idl::structtype_constructor_args():
    sig = inspect.signature(idl::StructType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::structtype_has_name():
    assert hasattr(idl::StructType, "name")
    descriptor = None
    for klass in idl::StructType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc)


def test_idl::preproc_constructor_exists():
    assert callable(idl::Preproc.__init__)


def test_idl::preproc_constructor_args():
    sig = inspect.signature(idl::Preproc.__init__)
    params = list(sig.parameters.keys())



def test_idl::definition_is_not_abstract():
    assert not inspect.isabstract(idl::Definition)


def test_idl::definition_constructor_exists():
    assert callable(idl::Definition.__init__)


def test_idl::definition_constructor_args():
    sig = inspect.signature(idl::Definition.__init__)
    params = list(sig.parameters.keys())



def test_idl::import::decl_is_not_abstract():
    assert not inspect.isabstract(idl::Import::decl)


def test_idl::import::decl_constructor_exists():
    assert callable(idl::Import::decl.__init__)


def test_idl::import::decl_constructor_args():
    sig = inspect.signature(idl::Import::decl.__init__)
    params = list(sig.parameters.keys())
    assert "imported_scope" in params, "Missing parameter 'imported_scope'"

def test_idl::import::decl_has_imported_scope():
    assert hasattr(idl::Import::decl, "imported_scope")
    descriptor = None
    for klass in idl::Import::decl.__mro__:
        if "imported_scope" in klass.__dict__:
            descriptor = klass.__dict__["imported_scope"]
            break
    assert isinstance(descriptor, property)



def test_idl::specification_is_not_abstract():
    assert not inspect.isabstract(idl::Specification)


def test_idl::specification_constructor_exists():
    assert callable(idl::Specification.__init__)


def test_idl::specification_constructor_args():
    sig = inspect.signature(idl::Specification.__init__)
    params = list(sig.parameters.keys())



def test_preproc::pragma_is_not_abstract():
    assert not inspect.isabstract(Preproc::Pragma)


def test_preproc::pragma_constructor_exists():
    assert callable(Preproc::Pragma.__init__)


def test_preproc::pragma_constructor_args():
    sig = inspect.signature(Preproc::Pragma.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::pragma::conn::type_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Conn::Type)


def test_idl::preproc::pragma::conn::type_constructor_exists():
    assert callable(idl::Preproc::Pragma::Conn::Type.__init__)


def test_idl::preproc::pragma::conn::type_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Conn::Type.__init__)
    params = list(sig.parameters.keys())
    assert "valuePort" in params, "Missing parameter 'valuePort'"
    assert "valueConnType" in params, "Missing parameter 'valueConnType'"

def test_idl::preproc::pragma::conn::type_has_valuePort():
    assert hasattr(idl::Preproc::Pragma::Conn::Type, "valuePort")
    descriptor = None
    for klass in idl::Preproc::Pragma::Conn::Type.__mro__:
        if "valuePort" in klass.__dict__:
            descriptor = klass.__dict__["valuePort"]
            break
    assert isinstance(descriptor, property)

def test_idl::preproc::pragma::conn::type_has_valueConnType():
    assert hasattr(idl::Preproc::Pragma::Conn::Type, "valueConnType")
    descriptor = None
    for klass in idl::Preproc::Pragma::Conn::Type.__mro__:
        if "valueConnType" in klass.__dict__:
            descriptor = klass.__dict__["valueConnType"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::prefix_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Prefix)


def test_idl::preproc::pragma::prefix_constructor_exists():
    assert callable(idl::Preproc::Pragma::Prefix.__init__)


def test_idl::preproc::pragma::prefix_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Prefix.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::prefix_has_value():
    assert hasattr(idl::Preproc::Pragma::Prefix, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Prefix.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma)


def test_idl::preproc::pragma_constructor_exists():
    assert callable(idl::Preproc::Pragma.__init__)


def test_idl::preproc::pragma_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::endif_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Endif)


def test_idl::preproc::endif_constructor_exists():
    assert callable(idl::Preproc::Endif.__init__)


def test_idl::preproc::endif_constructor_args():
    sig = inspect.signature(idl::Preproc::Endif.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::define_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Define)


def test_idl::preproc::define_constructor_exists():
    assert callable(idl::Preproc::Define.__init__)


def test_idl::preproc::define_constructor_args():
    sig = inspect.signature(idl::Preproc::Define.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::define_has_value():
    assert hasattr(idl::Preproc::Define, "value")
    descriptor = None
    for klass in idl::Preproc::Define.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::error_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Error)


def test_idl::preproc::error_constructor_exists():
    assert callable(idl::Preproc::Error.__init__)


def test_idl::preproc::error_constructor_args():
    sig = inspect.signature(idl::Preproc::Error.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::error_has_value():
    assert hasattr(idl::Preproc::Error, "value")
    descriptor = None
    for klass in idl::Preproc::Error.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::else_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Else)


def test_idl::preproc::else_constructor_exists():
    assert callable(idl::Preproc::Else.__init__)


def test_idl::preproc::else_constructor_args():
    sig = inspect.signature(idl::Preproc::Else.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::if::val_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::If::Val)


def test_idl::preproc::if::val_constructor_exists():
    assert callable(idl::Preproc::If::Val.__init__)


def test_idl::preproc::if::val_constructor_args():
    sig = inspect.signature(idl::Preproc::If::Val.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::if::compare_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::If::Compare)


def test_idl::preproc::if::compare_constructor_exists():
    assert callable(idl::Preproc::If::Compare.__init__)


def test_idl::preproc::if::compare_constructor_args():
    sig = inspect.signature(idl::Preproc::If::Compare.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl::preproc::if::compare_has_op():
    assert hasattr(idl::Preproc::If::Compare, "op")
    descriptor = None
    for klass in idl::Preproc::If::Compare.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::if_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::If)


def test_idl::preproc::if_constructor_exists():
    assert callable(idl::Preproc::If.__init__)


def test_idl::preproc::if_constructor_args():
    sig = inspect.signature(idl::Preproc::If.__init__)
    params = list(sig.parameters.keys())
    assert "negation" in params, "Missing parameter 'negation'"

def test_idl::preproc::if_has_negation():
    assert hasattr(idl::Preproc::If, "negation")
    descriptor = None
    for klass in idl::Preproc::If.__mro__:
        if "negation" in klass.__dict__:
            descriptor = klass.__dict__["negation"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::undef_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Undef)


def test_idl::preproc::undef_constructor_exists():
    assert callable(idl::Preproc::Undef.__init__)


def test_idl::preproc::undef_constructor_args():
    sig = inspect.signature(idl::Preproc::Undef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::undef_has_value():
    assert hasattr(idl::Preproc::Undef, "value")
    descriptor = None
    for klass in idl::Preproc::Undef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_complexdeclarator_is_not_abstract():
    assert not inspect.isabstract(ComplexDeclarator)


def test_complexdeclarator_constructor_exists():
    assert callable(ComplexDeclarator.__init__)


def test_complexdeclarator_constructor_args():
    sig = inspect.signature(ComplexDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_idl::complexdeclarator_is_not_abstract():
    assert not inspect.isabstract(idl::ComplexDeclarator)


def test_idl::complexdeclarator_constructor_exists():
    assert callable(idl::ComplexDeclarator.__init__)


def test_idl::complexdeclarator_constructor_args():
    sig = inspect.signature(idl::ComplexDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_declarator_is_not_abstract():
    assert not inspect.isabstract(Declarator)


def test_declarator_constructor_exists():
    assert callable(Declarator.__init__)


def test_declarator_constructor_args():
    sig = inspect.signature(Declarator.__init__)
    params = list(sig.parameters.keys())



def test_idl::arraydeclarator_is_not_abstract():
    assert not inspect.isabstract(idl::ArrayDeclarator)


def test_idl::arraydeclarator_constructor_exists():
    assert callable(idl::ArrayDeclarator.__init__)


def test_idl::arraydeclarator_constructor_args():
    sig = inspect.signature(idl::ArrayDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_idl::simpledeclarator_is_not_abstract():
    assert not inspect.isabstract(idl::SimpleDeclarator)


def test_idl::simpledeclarator_constructor_exists():
    assert callable(idl::SimpleDeclarator.__init__)


def test_idl::simpledeclarator_constructor_args():
    sig = inspect.signature(idl::SimpleDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpr_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpr)


def test_primaryexpr_constructor_exists():
    assert callable(PrimaryExpr.__init__)


def test_primaryexpr_constructor_args():
    sig = inspect.signature(PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_idl::constexp_is_not_abstract():
    assert not inspect.isabstract(idl::ConstExp)


def test_idl::constexp_constructor_exists():
    assert callable(idl::ConstExp.__init__)


def test_idl::constexp_constructor_args():
    sig = inspect.signature(idl::ConstExp.__init__)
    params = list(sig.parameters.keys())



def test_idl::literal_is_not_abstract():
    assert not inspect.isabstract(idl::Literal)


def test_idl::literal_constructor_exists():
    assert callable(idl::Literal.__init__)


def test_idl::literal_constructor_args():
    sig = inspect.signature(idl::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::literal_has_value():
    assert hasattr(idl::Literal, "value")
    descriptor = None
    for klass in idl::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_consttype_is_not_abstract():
    assert not inspect.isabstract(ConstType)


def test_consttype_constructor_exists():
    assert callable(ConstType.__init__)


def test_consttype_constructor_args():
    sig = inspect.signature(ConstType.__init__)
    params = list(sig.parameters.keys())



def test_idl::fixedptconsttype_is_not_abstract():
    assert not inspect.isabstract(idl::FixedPtConstType)


def test_idl::fixedptconsttype_constructor_exists():
    assert callable(idl::FixedPtConstType.__init__)


def test_idl::fixedptconsttype_constructor_args():
    sig = inspect.signature(idl::FixedPtConstType.__init__)
    params = list(sig.parameters.keys())



def test_switchtypespec_is_not_abstract():
    assert not inspect.isabstract(SwitchTypeSpec)


def test_switchtypespec_constructor_exists():
    assert callable(SwitchTypeSpec.__init__)


def test_switchtypespec_constructor_args():
    sig = inspect.signature(SwitchTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::enumtype_is_not_abstract():
    assert not inspect.isabstract(idl::EnumType)


def test_idl::enumtype_constructor_exists():
    assert callable(idl::EnumType.__init__)


def test_idl::enumtype_constructor_args():
    sig = inspect.signature(idl::EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl::enumtype_has_literal():
    assert hasattr(idl::EnumType, "literal")
    descriptor = None
    for klass in idl::EnumType.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_idl::enumtype_has_name():
    assert hasattr(idl::EnumType, "name")
    descriptor = None
    for klass in idl::EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpletypespec_is_not_abstract():
    assert not inspect.isabstract(SimpleTypeSpec)


def test_simpletypespec_constructor_exists():
    assert callable(SimpleTypeSpec.__init__)


def test_simpletypespec_constructor_args():
    sig = inspect.signature(SimpleTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::templatetypespec_is_not_abstract():
    assert not inspect.isabstract(idl::TemplateTypeSpec)


def test_idl::templatetypespec_constructor_exists():
    assert callable(idl::TemplateTypeSpec.__init__)


def test_idl::templatetypespec_constructor_args():
    sig = inspect.signature(idl::TemplateTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_paramtypespec_is_not_abstract():
    assert not inspect.isabstract(ParamTypeSpec)


def test_paramtypespec_constructor_exists():
    assert callable(ParamTypeSpec.__init__)


def test_paramtypespec_constructor_args():
    sig = inspect.signature(ParamTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::basetypespec_is_not_abstract():
    assert not inspect.isabstract(idl::BaseTypeSpec)


def test_idl::basetypespec_constructor_exists():
    assert callable(idl::BaseTypeSpec.__init__)


def test_idl::basetypespec_constructor_args():
    sig = inspect.signature(idl::BaseTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_optypedecl_is_not_abstract():
    assert not inspect.isabstract(OpTypeDecl)


def test_optypedecl_constructor_exists():
    assert callable(OpTypeDecl.__init__)


def test_optypedecl_constructor_args():
    sig = inspect.signature(OpTypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::paramdcl_is_not_abstract():
    assert not inspect.isabstract(idl::ParamDcl)


def test_idl::paramdcl_constructor_exists():
    assert callable(idl::ParamDcl.__init__)


def test_idl::paramdcl_constructor_args():
    sig = inspect.signature(idl::ParamDcl.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl::paramdcl_has_direction():
    assert hasattr(idl::ParamDcl, "direction")
    descriptor = None
    for klass in idl::ParamDcl.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_idl::paramdcl_has_name():
    assert hasattr(idl::ParamDcl, "name")
    descriptor = None
    for klass in idl::ParamDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::positiveintconst_is_not_abstract():
    assert not inspect.isabstract(idl::PositiveIntConst)


def test_idl::positiveintconst_constructor_exists():
    assert callable(idl::PositiveIntConst.__init__)


def test_idl::positiveintconst_constructor_args():
    sig = inspect.signature(idl::PositiveIntConst.__init__)
    params = list(sig.parameters.keys())



def test_templatetypespec_is_not_abstract():
    assert not inspect.isabstract(TemplateTypeSpec)


def test_templatetypespec_constructor_exists():
    assert callable(TemplateTypeSpec.__init__)


def test_templatetypespec_constructor_args():
    sig = inspect.signature(TemplateTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::fixedpttype_is_not_abstract():
    assert not inspect.isabstract(idl::FixedPtType)


def test_idl::fixedpttype_constructor_exists():
    assert callable(idl::FixedPtType.__init__)


def test_idl::fixedpttype_constructor_args():
    sig = inspect.signature(idl::FixedPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl::sequencetype_is_not_abstract():
    assert not inspect.isabstract(idl::SequenceType)


def test_idl::sequencetype_constructor_exists():
    assert callable(idl::SequenceType.__init__)


def test_idl::sequencetype_constructor_args():
    sig = inspect.signature(idl::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_idl::widestringtype_is_not_abstract():
    assert not inspect.isabstract(idl::WideStringType)


def test_idl::widestringtype_constructor_exists():
    assert callable(idl::WideStringType.__init__)


def test_idl::widestringtype_constructor_args():
    sig = inspect.signature(idl::WideStringType.__init__)
    params = list(sig.parameters.keys())



def test_idl::stringtype_is_not_abstract():
    assert not inspect.isabstract(idl::StringType)


def test_idl::stringtype_constructor_exists():
    assert callable(idl::StringType.__init__)


def test_idl::stringtype_constructor_args():
    sig = inspect.signature(idl::StringType.__init__)
    params = list(sig.parameters.keys())



def test_unsignedint_is_not_abstract():
    assert not inspect.isabstract(UnsignedInt)


def test_unsignedint_constructor_exists():
    assert callable(UnsignedInt.__init__)


def test_unsignedint_constructor_args():
    sig = inspect.signature(UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::unsignedlonglongint_is_not_abstract():
    assert not inspect.isabstract(idl::UnsignedLongLongInt)


def test_idl::unsignedlonglongint_constructor_exists():
    assert callable(idl::UnsignedLongLongInt.__init__)


def test_idl::unsignedlonglongint_constructor_args():
    sig = inspect.signature(idl::UnsignedLongLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::unsignedlongint_is_not_abstract():
    assert not inspect.isabstract(idl::UnsignedLongInt)


def test_idl::unsignedlongint_constructor_exists():
    assert callable(idl::UnsignedLongInt.__init__)


def test_idl::unsignedlongint_constructor_args():
    sig = inspect.signature(idl::UnsignedLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::unsignedshortint_is_not_abstract():
    assert not inspect.isabstract(idl::UnsignedShortInt)


def test_idl::unsignedshortint_constructor_exists():
    assert callable(idl::UnsignedShortInt.__init__)


def test_idl::unsignedshortint_constructor_args():
    sig = inspect.signature(idl::UnsignedShortInt.__init__)
    params = list(sig.parameters.keys())



def test_signedint_is_not_abstract():
    assert not inspect.isabstract(SignedInt)


def test_signedint_constructor_exists():
    assert callable(SignedInt.__init__)


def test_signedint_constructor_args():
    sig = inspect.signature(SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::signedlonglongint_is_not_abstract():
    assert not inspect.isabstract(idl::SignedLongLongInt)


def test_idl::signedlonglongint_constructor_exists():
    assert callable(idl::SignedLongLongInt.__init__)


def test_idl::signedlonglongint_constructor_args():
    sig = inspect.signature(idl::SignedLongLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::signedlongint_is_not_abstract():
    assert not inspect.isabstract(idl::SignedLongInt)


def test_idl::signedlongint_constructor_exists():
    assert callable(idl::SignedLongInt.__init__)


def test_idl::signedlongint_constructor_args():
    sig = inspect.signature(idl::SignedLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::signedshortint_is_not_abstract():
    assert not inspect.isabstract(idl::SignedShortInt)


def test_idl::signedshortint_constructor_exists():
    assert callable(idl::SignedShortInt.__init__)


def test_idl::signedshortint_constructor_args():
    sig = inspect.signature(idl::SignedShortInt.__init__)
    params = list(sig.parameters.keys())



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_idl::unsignedint_is_not_abstract():
    assert not inspect.isabstract(idl::UnsignedInt)


def test_idl::unsignedint_constructor_exists():
    assert callable(idl::UnsignedInt.__init__)


def test_idl::unsignedint_constructor_args():
    sig = inspect.signature(idl::UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl::signedint_is_not_abstract():
    assert not inspect.isabstract(idl::SignedInt)


def test_idl::signedint_constructor_exists():
    assert callable(idl::SignedInt.__init__)


def test_idl::signedint_constructor_args():
    sig = inspect.signature(idl::SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_floatingpttype_is_not_abstract():
    assert not inspect.isabstract(FloatingPtType)


def test_floatingpttype_constructor_exists():
    assert callable(FloatingPtType.__init__)


def test_floatingpttype_constructor_args():
    sig = inspect.signature(FloatingPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl::longdoubletype_is_not_abstract():
    assert not inspect.isabstract(idl::LongDoubleType)


def test_idl::longdoubletype_constructor_exists():
    assert callable(idl::LongDoubleType.__init__)


def test_idl::longdoubletype_constructor_args():
    sig = inspect.signature(idl::LongDoubleType.__init__)
    params = list(sig.parameters.keys())



def test_idl::doubletype_is_not_abstract():
    assert not inspect.isabstract(idl::DoubleType)


def test_idl::doubletype_constructor_exists():
    assert callable(idl::DoubleType.__init__)


def test_idl::doubletype_constructor_args():
    sig = inspect.signature(idl::DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_idl::floattype_is_not_abstract():
    assert not inspect.isabstract(idl::FloatType)


def test_idl::floattype_constructor_exists():
    assert callable(idl::FloatType.__init__)


def test_idl::floattype_constructor_args():
    sig = inspect.signature(idl::FloatType.__init__)
    params = list(sig.parameters.keys())



def test_basetypespec_is_not_abstract():
    assert not inspect.isabstract(BaseTypeSpec)


def test_basetypespec_constructor_exists():
    assert callable(BaseTypeSpec.__init__)


def test_basetypespec_constructor_args():
    sig = inspect.signature(BaseTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::octettype_is_not_abstract():
    assert not inspect.isabstract(idl::OctetType)


def test_idl::octettype_constructor_exists():
    assert callable(idl::OctetType.__init__)


def test_idl::octettype_constructor_args():
    sig = inspect.signature(idl::OctetType.__init__)
    params = list(sig.parameters.keys())



def test_idl::anytype_is_not_abstract():
    assert not inspect.isabstract(idl::AnyType)


def test_idl::anytype_constructor_exists():
    assert callable(idl::AnyType.__init__)


def test_idl::anytype_constructor_args():
    sig = inspect.signature(idl::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_idl::integertype_is_not_abstract():
    assert not inspect.isabstract(idl::IntegerType)


def test_idl::integertype_constructor_exists():
    assert callable(idl::IntegerType.__init__)


def test_idl::integertype_constructor_args():
    sig = inspect.signature(idl::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_idl::valuebasetype_is_not_abstract():
    assert not inspect.isabstract(idl::ValueBaseType)


def test_idl::valuebasetype_constructor_exists():
    assert callable(idl::ValueBaseType.__init__)


def test_idl::valuebasetype_constructor_args():
    sig = inspect.signature(idl::ValueBaseType.__init__)
    params = list(sig.parameters.keys())



def test_idl::widechartype_is_not_abstract():
    assert not inspect.isabstract(idl::WideCharType)


def test_idl::widechartype_constructor_exists():
    assert callable(idl::WideCharType.__init__)


def test_idl::widechartype_constructor_args():
    sig = inspect.signature(idl::WideCharType.__init__)
    params = list(sig.parameters.keys())



def test_idl::chartype_is_not_abstract():
    assert not inspect.isabstract(idl::CharType)


def test_idl::chartype_constructor_exists():
    assert callable(idl::CharType.__init__)


def test_idl::chartype_constructor_args():
    sig = inspect.signature(idl::CharType.__init__)
    params = list(sig.parameters.keys())



def test_idl::objecttype_is_not_abstract():
    assert not inspect.isabstract(idl::ObjectType)


def test_idl::objecttype_constructor_exists():
    assert callable(idl::ObjectType.__init__)


def test_idl::objecttype_constructor_args():
    sig = inspect.signature(idl::ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_idl::booleantype_is_not_abstract():
    assert not inspect.isabstract(idl::BooleanType)


def test_idl::booleantype_constructor_exists():
    assert callable(idl::BooleanType.__init__)


def test_idl::booleantype_constructor_args():
    sig = inspect.signature(idl::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_idl::floatingpttype_is_not_abstract():
    assert not inspect.isabstract(idl::FloatingPtType)


def test_idl::floatingpttype_constructor_exists():
    assert callable(idl::FloatingPtType.__init__)


def test_idl::floatingpttype_constructor_args():
    sig = inspect.signature(idl::FloatingPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl::paramtypespec_is_not_abstract():
    assert not inspect.isabstract(idl::ParamTypeSpec)


def test_idl::paramtypespec_constructor_exists():
    assert callable(idl::ParamTypeSpec.__init__)


def test_idl::paramtypespec_constructor_args():
    sig = inspect.signature(idl::ParamTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_connectorexport_is_not_abstract():
    assert not inspect.isabstract(ConnectorExport)


def test_connectorexport_constructor_exists():
    assert callable(ConnectorExport.__init__)


def test_connectorexport_constructor_args():
    sig = inspect.signature(ConnectorExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::portdecl_is_not_abstract():
    assert not inspect.isabstract(idl::PortDecl)


def test_idl::portdecl_constructor_exists():
    assert callable(idl::PortDecl.__init__)


def test_idl::portdecl_constructor_args():
    sig = inspect.signature(idl::PortDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMirror" in params, "Missing parameter 'isMirror'"

def test_idl::portdecl_has_name():
    assert hasattr(idl::PortDecl, "name")
    descriptor = None
    for klass in idl::PortDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl::portdecl_has_isMirror():
    assert hasattr(idl::PortDecl, "isMirror")
    descriptor = None
    for klass in idl::PortDecl.__mro__:
        if "isMirror" in klass.__dict__:
            descriptor = klass.__dict__["isMirror"]
            break
    assert isinstance(descriptor, property)



def test_portexport_is_not_abstract():
    assert not inspect.isabstract(PortExport)


def test_portexport_constructor_exists():
    assert callable(PortExport.__init__)


def test_portexport_constructor_args():
    sig = inspect.signature(PortExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::usesdcl_is_not_abstract():
    assert not inspect.isabstract(idl::UsesDcl)


def test_idl::usesdcl_constructor_exists():
    assert callable(idl::UsesDcl.__init__)


def test_idl::usesdcl_constructor_args():
    sig = inspect.signature(idl::UsesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "isMultiple" in params, "Missing parameter 'isMultiple'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl::usesdcl_has_isMultiple():
    assert hasattr(idl::UsesDcl, "isMultiple")
    descriptor = None
    for klass in idl::UsesDcl.__mro__:
        if "isMultiple" in klass.__dict__:
            descriptor = klass.__dict__["isMultiple"]
            break
    assert isinstance(descriptor, property)

def test_idl::usesdcl_has_name():
    assert hasattr(idl::UsesDcl, "name")
    descriptor = None
    for klass in idl::UsesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::providesdcl_is_not_abstract():
    assert not inspect.isabstract(idl::ProvidesDcl)


def test_idl::providesdcl_constructor_exists():
    assert callable(idl::ProvidesDcl.__init__)


def test_idl::providesdcl_constructor_args():
    sig = inspect.signature(idl::ProvidesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::providesdcl_has_name():
    assert hasattr(idl::ProvidesDcl, "name")
    descriptor = None
    for klass in idl::ProvidesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::attrdecl_is_not_abstract():
    assert not inspect.isabstract(idl::AttrDecl)


def test_idl::attrdecl_constructor_exists():
    assert callable(idl::AttrDecl.__init__)


def test_idl::attrdecl_constructor_args():
    sig = inspect.signature(idl::AttrDecl.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_idl::attrdecl_has_names():
    assert hasattr(idl::AttrDecl, "names")
    descriptor = None
    for klass in idl::AttrDecl.__mro__:
        if "names" in klass.__dict__:
            descriptor = klass.__dict__["names"]
            break
    assert isinstance(descriptor, property)



def test_homeexport_is_not_abstract():
    assert not inspect.isabstract(HomeExport)


def test_homeexport_constructor_exists():
    assert callable(HomeExport.__init__)


def test_homeexport_constructor_args():
    sig = inspect.signature(HomeExport.__init__)
    params = list(sig.parameters.keys())



def test_idl::factorydcl_is_not_abstract():
    assert not inspect.isabstract(idl::FactoryDcl)


def test_idl::factorydcl_constructor_exists():
    assert callable(idl::FactoryDcl.__init__)


def test_idl::factorydcl_constructor_args():
    sig = inspect.signature(idl::FactoryDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::factorydcl_has_name():
    assert hasattr(idl::FactoryDcl, "name")
    descriptor = None
    for klass in idl::FactoryDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::finderdcl_is_not_abstract():
    assert not inspect.isabstract(idl::FinderDcl)


def test_idl::finderdcl_constructor_exists():
    assert callable(idl::FinderDcl.__init__)


def test_idl::finderdcl_constructor_args():
    sig = inspect.signature(idl::FinderDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::finderdcl_has_name():
    assert hasattr(idl::FinderDcl, "name")
    descriptor = None
    for klass in idl::FinderDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::export_is_not_abstract():
    assert not inspect.isabstract(idl::Export)


def test_idl::export_constructor_exists():
    assert callable(idl::Export.__init__)


def test_idl::export_constructor_args():
    sig = inspect.signature(idl::Export.__init__)
    params = list(sig.parameters.keys())



def test_idl::scopedname_is_not_abstract():
    assert not inspect.isabstract(idl::ScopedName)


def test_idl::scopedname_constructor_exists():
    assert callable(idl::ScopedName.__init__)


def test_idl::scopedname_constructor_args():
    sig = inspect.signature(idl::ScopedName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::scopedname_has_name():
    assert hasattr(idl::ScopedName, "name")
    descriptor = None
    for klass in idl::ScopedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::contextexpr_is_not_abstract():
    assert not inspect.isabstract(idl::ContextExpr)


def test_idl::contextexpr_constructor_exists():
    assert callable(idl::ContextExpr.__init__)


def test_idl::contextexpr_constructor_args():
    sig = inspect.signature(idl::ContextExpr.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_idl::contextexpr_has_literal():
    assert hasattr(idl::ContextExpr, "literal")
    descriptor = None
    for klass in idl::ContextExpr.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_idl::parameterdecls_is_not_abstract():
    assert not inspect.isabstract(idl::ParameterDecls)


def test_idl::parameterdecls_constructor_exists():
    assert callable(idl::ParameterDecls.__init__)


def test_idl::parameterdecls_constructor_args():
    sig = inspect.signature(idl::ParameterDecls.__init__)
    params = list(sig.parameters.keys())



def test_idl::optypedecl_is_not_abstract():
    assert not inspect.isabstract(idl::OpTypeDecl)


def test_idl::optypedecl_constructor_exists():
    assert callable(idl::OpTypeDecl.__init__)


def test_idl::optypedecl_constructor_args():
    sig = inspect.signature(idl::OpTypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::opdecl_is_not_abstract():
    assert not inspect.isabstract(idl::OpDecl)


def test_idl::opdecl_constructor_exists():
    assert callable(idl::OpDecl.__init__)


def test_idl::opdecl_constructor_args():
    sig = inspect.signature(idl::OpDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isOneway" in params, "Missing parameter 'isOneway'"

def test_idl::opdecl_has_name():
    assert hasattr(idl::OpDecl, "name")
    descriptor = None
    for klass in idl::OpDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl::opdecl_has_isOneway():
    assert hasattr(idl::OpDecl, "isOneway")
    descriptor = None
    for klass in idl::OpDecl.__mro__:
        if "isOneway" in klass.__dict__:
            descriptor = klass.__dict__["isOneway"]
            break
    assert isinstance(descriptor, property)



def test_idl::exceptionlist_is_not_abstract():
    assert not inspect.isabstract(idl::ExceptionList)


def test_idl::exceptionlist_constructor_exists():
    assert callable(idl::ExceptionList.__init__)


def test_idl::exceptionlist_constructor_args():
    sig = inspect.signature(idl::ExceptionList.__init__)
    params = list(sig.parameters.keys())



def test_idl::attrraisesexpr_is_not_abstract():
    assert not inspect.isabstract(idl::AttrRaisesExpr)


def test_idl::attrraisesexpr_constructor_exists():
    assert callable(idl::AttrRaisesExpr.__init__)


def test_idl::attrraisesexpr_constructor_args():
    sig = inspect.signature(idl::AttrRaisesExpr.__init__)
    params = list(sig.parameters.keys())



def test_attrdecl_is_not_abstract():
    assert not inspect.isabstract(AttrDecl)


def test_attrdecl_constructor_exists():
    assert callable(AttrDecl.__init__)


def test_attrdecl_constructor_args():
    sig = inspect.signature(AttrDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::readonlyattrspec_is_not_abstract():
    assert not inspect.isabstract(idl::ReadOnlyAttrSpec)


def test_idl::readonlyattrspec_constructor_exists():
    assert callable(idl::ReadOnlyAttrSpec.__init__)


def test_idl::readonlyattrspec_constructor_args():
    sig = inspect.signature(idl::ReadOnlyAttrSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::attrspec_is_not_abstract():
    assert not inspect.isabstract(idl::AttrSpec)


def test_idl::attrspec_constructor_exists():
    assert callable(idl::AttrSpec.__init__)


def test_idl::attrspec_constructor_args():
    sig = inspect.signature(idl::AttrSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::pragma::component_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Component)


def test_idl::preproc::pragma::component_constructor_exists():
    assert callable(idl::Preproc::Pragma::Component.__init__)


def test_idl::preproc::pragma::component_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Component.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::component_has_value():
    assert hasattr(idl::Preproc::Pragma::Component, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Component.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::ndds_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Ndds)


def test_idl::preproc::pragma::ndds_constructor_exists():
    assert callable(idl::Preproc::Pragma::Ndds.__init__)


def test_idl::preproc::pragma::ndds_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Ndds.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::ndds_has_value():
    assert hasattr(idl::Preproc::Pragma::Ndds, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Ndds.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::ciao::ami4ccm::idl_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Ciao::Ami4ccm::Idl)


def test_idl::preproc::pragma::ciao::ami4ccm::idl_constructor_exists():
    assert callable(idl::Preproc::Pragma::Ciao::Ami4ccm::Idl.__init__)


def test_idl::preproc::pragma::ciao::ami4ccm::idl_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Ciao::Ami4ccm::Idl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::ciao::ami4ccm::idl_has_value():
    assert hasattr(idl::Preproc::Pragma::Ciao::Ami4ccm::Idl, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Ciao::Ami4ccm::Idl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle)


def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_constructor_exists():
    assert callable(idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle.__init__)


def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_has_value():
    assert hasattr(idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::ciao::ami4ccm::interface_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Ciao::Ami4ccm::Interface)


def test_idl::preproc::pragma::ciao::ami4ccm::interface_constructor_exists():
    assert callable(idl::Preproc::Pragma::Ciao::Ami4ccm::Interface.__init__)


def test_idl::preproc::pragma::ciao::ami4ccm::interface_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Ciao::Ami4ccm::Interface.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::ciao::ami4ccm::interface_has_value():
    assert hasattr(idl::Preproc::Pragma::Ciao::Ami4ccm::Interface, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Ciao::Ami4ccm::Interface.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::ciao::lem_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Ciao::Lem)


def test_idl::preproc::pragma::ciao::lem_constructor_exists():
    assert callable(idl::Preproc::Pragma::Ciao::Lem.__init__)


def test_idl::preproc::pragma::ciao::lem_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Ciao::Lem.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::ciao::lem_has_value():
    assert hasattr(idl::Preproc::Pragma::Ciao::Lem, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Ciao::Lem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::interfacebody_is_not_abstract():
    assert not inspect.isabstract(idl::InterfaceBody)


def test_idl::interfacebody_constructor_exists():
    assert callable(idl::InterfaceBody.__init__)


def test_idl::interfacebody_constructor_args():
    sig = inspect.signature(idl::InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_idl::interface::header_is_not_abstract():
    assert not inspect.isabstract(idl::Interface::header)


def test_idl::interface::header_constructor_exists():
    assert callable(idl::Interface::header.__init__)


def test_idl::interface::header_constructor_args():
    sig = inspect.signature(idl::Interface::header.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isLocal" in params, "Missing parameter 'isLocal'"

def test_idl::interface::header_has_isAbstract():
    assert hasattr(idl::Interface::header, "isAbstract")
    descriptor = None
    for klass in idl::Interface::header.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_idl::interface::header_has_name():
    assert hasattr(idl::Interface::header, "name")
    descriptor = None
    for klass in idl::Interface::header.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl::interface::header_has_isLocal():
    assert hasattr(idl::Interface::header, "isLocal")
    descriptor = None
    for klass in idl::Interface::header.__mro__:
        if "isLocal" in klass.__dict__:
            descriptor = klass.__dict__["isLocal"]
            break
    assert isinstance(descriptor, property)



def test_fixeddefinition_is_not_abstract():
    assert not inspect.isabstract(FixedDefinition)


def test_fixeddefinition_constructor_exists():
    assert callable(FixedDefinition.__init__)


def test_fixeddefinition_constructor_args():
    sig = inspect.signature(FixedDefinition.__init__)
    params = list(sig.parameters.keys())



def test_templatedefinition_is_not_abstract():
    assert not inspect.isabstract(TemplateDefinition)


def test_templatedefinition_constructor_exists():
    assert callable(TemplateDefinition.__init__)


def test_templatedefinition_constructor_args():
    sig = inspect.signature(TemplateDefinition.__init__)
    params = list(sig.parameters.keys())



def test_idl::porttypedecl_is_not_abstract():
    assert not inspect.isabstract(idl::PortTypeDecl)


def test_idl::porttypedecl_constructor_exists():
    assert callable(idl::PortTypeDecl.__init__)


def test_idl::porttypedecl_constructor_args():
    sig = inspect.signature(idl::PortTypeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::porttypedecl_has_name():
    assert hasattr(idl::PortTypeDecl, "name")
    descriptor = None
    for klass in idl::PortTypeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::typedecl_is_not_abstract():
    assert not inspect.isabstract(idl::TypeDecl)


def test_idl::typedecl_constructor_exists():
    assert callable(idl::TypeDecl.__init__)


def test_idl::typedecl_constructor_args():
    sig = inspect.signature(idl::TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl::exceptdecl_is_not_abstract():
    assert not inspect.isabstract(idl::ExceptDecl)


def test_idl::exceptdecl_constructor_exists():
    assert callable(idl::ExceptDecl.__init__)


def test_idl::exceptdecl_constructor_args():
    sig = inspect.signature(idl::ExceptDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::exceptdecl_has_name():
    assert hasattr(idl::ExceptDecl, "name")
    descriptor = None
    for klass in idl::ExceptDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::event_is_not_abstract():
    assert not inspect.isabstract(idl::Event)


def test_idl::event_constructor_exists():
    assert callable(idl::Event.__init__)


def test_idl::event_constructor_args():
    sig = inspect.signature(idl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_idl::event_has_name():
    assert hasattr(idl::Event, "name")
    descriptor = None
    for klass in idl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl::event_has_isAbstract():
    assert hasattr(idl::Event, "isAbstract")
    descriptor = None
    for klass in idl::Event.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_idl::homedecl_is_not_abstract():
    assert not inspect.isabstract(idl::HomeDecl)


def test_idl::homedecl_constructor_exists():
    assert callable(idl::HomeDecl.__init__)


def test_idl::homedecl_constructor_args():
    sig = inspect.signature(idl::HomeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::homedecl_has_name():
    assert hasattr(idl::HomeDecl, "name")
    descriptor = None
    for klass in idl::HomeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::fixedmodule_is_not_abstract():
    assert not inspect.isabstract(idl::FixedModule)


def test_idl::fixedmodule_constructor_exists():
    assert callable(idl::FixedModule.__init__)


def test_idl::fixedmodule_constructor_args():
    sig = inspect.signature(idl::FixedModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::fixedmodule_has_name():
    assert hasattr(idl::FixedModule, "name")
    descriptor = None
    for klass in idl::FixedModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::nativetype_is_not_abstract():
    assert not inspect.isabstract(idl::NativeType)


def test_idl::nativetype_constructor_exists():
    assert callable(idl::NativeType.__init__)


def test_idl::nativetype_constructor_args():
    sig = inspect.signature(idl::NativeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::nativetype_has_name():
    assert hasattr(idl::NativeType, "name")
    descriptor = None
    for klass in idl::NativeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::componentdecl_is_not_abstract():
    assert not inspect.isabstract(idl::ComponentDecl)


def test_idl::componentdecl_constructor_exists():
    assert callable(idl::ComponentDecl.__init__)


def test_idl::componentdecl_constructor_args():
    sig = inspect.signature(idl::ComponentDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::componentdecl_has_name():
    assert hasattr(idl::ComponentDecl, "name")
    descriptor = None
    for klass in idl::ComponentDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::constdecl_is_not_abstract():
    assert not inspect.isabstract(idl::ConstDecl)


def test_idl::constdecl_constructor_exists():
    assert callable(idl::ConstDecl.__init__)


def test_idl::constdecl_constructor_args():
    sig = inspect.signature(idl::ConstDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::constdecl_has_name():
    assert hasattr(idl::ConstDecl, "name")
    descriptor = None
    for klass in idl::ConstDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::connector_is_not_abstract():
    assert not inspect.isabstract(idl::Connector)


def test_idl::connector_constructor_exists():
    assert callable(idl::Connector.__init__)


def test_idl::connector_constructor_args():
    sig = inspect.signature(idl::Connector.__init__)
    params = list(sig.parameters.keys())



def test_idl::templatemoduleref_is_not_abstract():
    assert not inspect.isabstract(idl::TemplateModuleRef)


def test_idl::templatemoduleref_constructor_exists():
    assert callable(idl::TemplateModuleRef.__init__)


def test_idl::templatemoduleref_constructor_args():
    sig = inspect.signature(idl::TemplateModuleRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_idl::templatemoduleref_has_name():
    assert hasattr(idl::TemplateModuleRef, "name")
    descriptor = None
    for klass in idl::TemplateModuleRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl::templatemoduleref_has_id():
    assert hasattr(idl::TemplateModuleRef, "id")
    descriptor = None
    for klass in idl::TemplateModuleRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_interface::or::forward::decl_is_not_abstract():
    assert not inspect.isabstract(Interface::or::Forward::Decl)


def test_interface::or::forward::decl_constructor_exists():
    assert callable(Interface::or::Forward::Decl.__init__)


def test_interface::or::forward::decl_constructor_args():
    sig = inspect.signature(Interface::or::Forward::Decl.__init__)
    params = list(sig.parameters.keys())



def test_idl::forward::decl_is_not_abstract():
    assert not inspect.isabstract(idl::Forward::decl)


def test_idl::forward::decl_constructor_exists():
    assert callable(idl::Forward::decl.__init__)


def test_idl::forward::decl_constructor_args():
    sig = inspect.signature(idl::Forward::decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::forward::decl_has_name():
    assert hasattr(idl::Forward::decl, "name")
    descriptor = None
    for klass in idl::Forward::decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::interface::decl_is_not_abstract():
    assert not inspect.isabstract(idl::Interface::decl)


def test_idl::interface::decl_constructor_exists():
    assert callable(idl::Interface::decl.__init__)


def test_idl::interface::decl_constructor_args():
    sig = inspect.signature(idl::Interface::decl.__init__)
    params = list(sig.parameters.keys())



def test_idl::interface::or::forward::decl_is_not_abstract():
    assert not inspect.isabstract(idl::Interface::or::Forward::Decl)


def test_idl::interface::or::forward::decl_constructor_exists():
    assert callable(idl::Interface::or::Forward::Decl.__init__)


def test_idl::interface::or::forward::decl_constructor_args():
    sig = inspect.signature(idl::Interface::or::Forward::Decl.__init__)
    params = list(sig.parameters.keys())



def test_idl::idlcomment_is_not_abstract():
    assert not inspect.isabstract(idl::IDLComment)


def test_idl::idlcomment_constructor_exists():
    assert callable(idl::IDLComment.__init__)


def test_idl::idlcomment_constructor_args():
    sig = inspect.signature(idl::IDLComment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_idl::idlcomment_has_body():
    assert hasattr(idl::IDLComment, "body")
    descriptor = None
    for klass in idl::IDLComment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_idl::module_is_not_abstract():
    assert not inspect.isabstract(idl::Module)


def test_idl::module_constructor_exists():
    assert callable(idl::Module.__init__)


def test_idl::module_constructor_args():
    sig = inspect.signature(idl::Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::module_has_name():
    assert hasattr(idl::Module, "name")
    descriptor = None
    for klass in idl::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl::excluded::file::marker_is_not_abstract():
    assert not inspect.isabstract(idl::Excluded::File::Marker)


def test_idl::excluded::file::marker_constructor_exists():
    assert callable(idl::Excluded::File::Marker.__init__)


def test_idl::excluded::file::marker_constructor_args():
    sig = inspect.signature(idl::Excluded::File::Marker.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_idl::excluded::file::marker_has_file():
    assert hasattr(idl::Excluded::File::Marker, "file")
    descriptor = None
    for klass in idl::Excluded::File::Marker.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_idl::file::marker_is_not_abstract():
    assert not inspect.isabstract(idl::File::Marker)


def test_idl::file::marker_constructor_exists():
    assert callable(idl::File::Marker.__init__)


def test_idl::file::marker_constructor_args():
    sig = inspect.signature(idl::File::Marker.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_idl::file::marker_has_file():
    assert hasattr(idl::File::Marker, "file")
    descriptor = None
    for klass in idl::File::Marker.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::misc_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Misc)


def test_idl::preproc::pragma::misc_constructor_exists():
    assert callable(idl::Preproc::Pragma::Misc.__init__)


def test_idl::preproc::pragma::misc_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Misc.__init__)
    params = list(sig.parameters.keys())



def test_idl::preproc::pragma::dds4ccm::impl_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::DDS4CCM::Impl)


def test_idl::preproc::pragma::dds4ccm::impl_constructor_exists():
    assert callable(idl::Preproc::Pragma::DDS4CCM::Impl.__init__)


def test_idl::preproc::pragma::dds4ccm::impl_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::DDS4CCM::Impl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::dds4ccm::impl_has_value():
    assert hasattr(idl::Preproc::Pragma::DDS4CCM::Impl, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::DDS4CCM::Impl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::pragma::home_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Pragma::Home)


def test_idl::preproc::pragma::home_constructor_exists():
    assert callable(idl::Preproc::Pragma::Home.__init__)


def test_idl::preproc::pragma::home_constructor_args():
    sig = inspect.signature(idl::Preproc::Pragma::Home.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::pragma::home_has_value():
    assert hasattr(idl::Preproc::Pragma::Home, "value")
    descriptor = None
    for klass in idl::Preproc::Pragma::Home.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::ifndef_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Ifndef)


def test_idl::preproc::ifndef_constructor_exists():
    assert callable(idl::Preproc::Ifndef.__init__)


def test_idl::preproc::ifndef_constructor_args():
    sig = inspect.signature(idl::Preproc::Ifndef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::ifndef_has_value():
    assert hasattr(idl::Preproc::Ifndef, "value")
    descriptor = None
    for klass in idl::Preproc::Ifndef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::preproc::ifdef_is_not_abstract():
    assert not inspect.isabstract(idl::Preproc::Ifdef)


def test_idl::preproc::ifdef_constructor_exists():
    assert callable(idl::Preproc::Ifdef.__init__)


def test_idl::preproc::ifdef_constructor_args():
    sig = inspect.signature(idl::Preproc::Ifdef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl::preproc::ifdef_has_value():
    assert hasattr(idl::Preproc::Ifdef, "value")
    descriptor = None
    for klass in idl::Preproc::Ifdef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl::filename_is_not_abstract():
    assert not inspect.isabstract(idl::FileName)


def test_idl::filename_constructor_exists():
    assert callable(idl::FileName.__init__)


def test_idl::filename_constructor_args():
    sig = inspect.signature(idl::FileName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl::filename_has_name():
    assert hasattr(idl::FileName, "name")
    descriptor = None
    for klass in idl::FileName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_paramdirection_exists():
    # Check that the Enumeration exists
    assert ParamDirection is not None

def test_paramdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParamDirection]
    expected_literals = [
        "In",
        "InOut",
        "Out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParamDirection"


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
idl::FormalParameterType_strategy = st.builds(
    idl::FormalParameterType,
)
idl::TemplateDefinition_strategy = st.builds(
    idl::TemplateDefinition,
)
idl::FormalParameter_strategy = st.builds(
    idl::FormalParameter,
    name=
        safe_text
)
idl::ActualParameter_strategy = st.builds(
    idl::ActualParameter,
)
idl::FixedDefinition_strategy = st.builds(
    idl::FixedDefinition,
)
idl::StateMember_strategy = st.builds(
    idl::StateMember,
    isPublic=
        st.booleans(),
    names=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
idl::EventDcl_strategy = st.builds(
    idl::EventDcl,
    isTruncatable=
        st.booleans(),
    isCustom=
        st.booleans()
)
idl::ConnectorExport_strategy = st.builds(
    idl::ConnectorExport,
)
idl::ConnectorHeader_strategy = st.builds(
    idl::ConnectorHeader,
    name=
        safe_text
)
idl::PortExport_strategy = st.builds(
    idl::PortExport,
)
idl::EventForwardDcl_strategy = st.builds(
    idl::EventForwardDcl,
)
idl::HomeExport_strategy = st.builds(
    idl::HomeExport,
)
idl::PrimaryKeySpec_strategy = st.builds(
    idl::PrimaryKeySpec,
)
idl::ComponentExport_strategy = st.builds(
    idl::ComponentExport,
)
idl::PrimaryExpr_strategy = st.builds(
    idl::PrimaryExpr,
)
ConstParamType_strategy = st.builds(
    ConstParamType,
)
idl::ConstType_strategy = st.builds(
    idl::ConstType,
)
idl::UnaryExpr_strategy = st.builds(
    idl::UnaryExpr,
    op=
        safe_text
)
idl::MultExpr_strategy = st.builds(
    idl::MultExpr,
    op=
        safe_text
)
idl::AddExpr_strategy = st.builds(
    idl::AddExpr,
    op=
        safe_text
)
idl::ShiftExpr_strategy = st.builds(
    idl::ShiftExpr,
    op=
        safe_text
)
idl::AndExpr_strategy = st.builds(
    idl::AndExpr,
    op=
        safe_text
)
idl::XOrExpr_strategy = st.builds(
    idl::XOrExpr,
    op=
        safe_text
)
ConstExp_strategy = st.builds(
    ConstExp,
)
idl::OrExpr_strategy = st.builds(
    idl::OrExpr,
    op=
        safe_text
)
idl::ElementSpec_strategy = st.builds(
    idl::ElementSpec,
)
idl::CaseLabel_strategy = st.builds(
    idl::CaseLabel,
    isCase=
        st.booleans(),
    isDefault=
        st.booleans()
)
idl::Case_strategy = st.builds(
    idl::Case,
)
idl::SwitchBody_strategy = st.builds(
    idl::SwitchBody,
)
idl::SwitchTypeSpec_strategy = st.builds(
    idl::SwitchTypeSpec,
)
ConstrForwardDecl_strategy = st.builds(
    ConstrForwardDecl,
)
idl::UnionForwardDecl_strategy = st.builds(
    idl::UnionForwardDecl,
)
idl::StructForwardDecl_strategy = st.builds(
    idl::StructForwardDecl,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
idl::ExceptionParamType_strategy = st.builds(
    idl::ExceptionParamType,
)
idl::EventParamType_strategy = st.builds(
    idl::EventParamType,
)
idl::ValuetypeParamType_strategy = st.builds(
    idl::ValuetypeParamType,
)
idl::InterfaceParamType_strategy = st.builds(
    idl::InterfaceParamType,
)
idl::EnumParamType_strategy = st.builds(
    idl::EnumParamType,
)
idl::ConstParamType_strategy = st.builds(
    idl::ConstParamType,
)
idl::SequenceParamType_strategy = st.builds(
    idl::SequenceParamType,
)
idl::TypenameParamType_strategy = st.builds(
    idl::TypenameParamType,
)
idl::UnionParamType_strategy = st.builds(
    idl::UnionParamType,
)
idl::StructParamType_strategy = st.builds(
    idl::StructParamType,
)
idl::Declarator_strategy = st.builds(
    idl::Declarator,
    id=
        safe_text
)
idl::Member_strategy = st.builds(
    idl::Member,
)
TypeSpec_strategy = st.builds(
    TypeSpec,
)
idl::ConstrTypeSpec_strategy = st.builds(
    idl::ConstrTypeSpec,
)
idl::SimpleTypeSpec_strategy = st.builds(
    idl::SimpleTypeSpec,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
idl::TypeSpec_strategy = st.builds(
    idl::TypeSpec,
)
ConstrTypeSpec_strategy = st.builds(
    ConstrTypeSpec,
)
TypeDecl_strategy = st.builds(
    TypeDecl,
)
idl::ConstrForwardDecl_strategy = st.builds(
    idl::ConstrForwardDecl,
    name=
        safe_text
)
idl::UnionType_strategy = st.builds(
    idl::UnionType,
    name=
        safe_text
)
idl::TypeDeclarator_strategy = st.builds(
    idl::TypeDeclarator,
)
Preproc_strategy = st.builds(
    Preproc,
)
idl::Preproc::Include_strategy = st.builds(
    idl::Preproc::Include,
    strValue=
        safe_text
)
ComponentExport_strategy = st.builds(
    ComponentExport,
)
idl::ConsumesDcl_strategy = st.builds(
    idl::ConsumesDcl,
    name=
        safe_text
)
idl::EmitDcl_strategy = st.builds(
    idl::EmitDcl,
    name=
        safe_text
)
idl::PublishesDcl_strategy = st.builds(
    idl::PublishesDcl,
    name=
        safe_text
)
Export_strategy = st.builds(
    Export,
)
Definition_strategy = st.builds(
    Definition,
)
idl::ComponentForwardDecl_strategy = st.builds(
    idl::ComponentForwardDecl,
    name=
        safe_text
)
idl::TemplateModuleInst_strategy = st.builds(
    idl::TemplateModuleInst,
    name=
        safe_text
)
idl::TemplateModule_strategy = st.builds(
    idl::TemplateModule,
    name=
        safe_text
)
idl::StructType_strategy = st.builds(
    idl::StructType,
    name=
        safe_text
)
idl::Preproc_strategy = st.builds(
    idl::Preproc,
)
idl::Definition_strategy = st.builds(
    idl::Definition,
)
idl::Import::decl_strategy = st.builds(
    idl::Import::decl,
    imported_scope=
        safe_text
)
idl::Specification_strategy = st.builds(
    idl::Specification,
)
Preproc::Pragma_strategy = st.builds(
    Preproc::Pragma,
)
idl::Preproc::Pragma::Conn::Type_strategy = st.builds(
    idl::Preproc::Pragma::Conn::Type,
    valuePort=
        safe_text,
    valueConnType=
        safe_text
)
idl::Preproc::Pragma::Prefix_strategy = st.builds(
    idl::Preproc::Pragma::Prefix,
    value=
        safe_text
)
idl::Preproc::Pragma_strategy = st.builds(
    idl::Preproc::Pragma,
)
idl::Preproc::Endif_strategy = st.builds(
    idl::Preproc::Endif,
)
idl::Preproc::Define_strategy = st.builds(
    idl::Preproc::Define,
    value=
        safe_text
)
idl::Preproc::Error_strategy = st.builds(
    idl::Preproc::Error,
    value=
        safe_text
)
idl::Preproc::Else_strategy = st.builds(
    idl::Preproc::Else,
)
idl::Preproc::If::Val_strategy = st.builds(
    idl::Preproc::If::Val,
)
idl::Preproc::If::Compare_strategy = st.builds(
    idl::Preproc::If::Compare,
    op=
        safe_text
)
idl::Preproc::If_strategy = st.builds(
    idl::Preproc::If,
    negation=
        st.booleans()
)
idl::Preproc::Undef_strategy = st.builds(
    idl::Preproc::Undef,
    value=
        safe_text
)
ComplexDeclarator_strategy = st.builds(
    ComplexDeclarator,
)
idl::ComplexDeclarator_strategy = st.builds(
    idl::ComplexDeclarator,
)
Declarator_strategy = st.builds(
    Declarator,
)
idl::ArrayDeclarator_strategy = st.builds(
    idl::ArrayDeclarator,
)
idl::SimpleDeclarator_strategy = st.builds(
    idl::SimpleDeclarator,
)
PrimaryExpr_strategy = st.builds(
    PrimaryExpr,
)
idl::ConstExp_strategy = st.builds(
    idl::ConstExp,
)
idl::Literal_strategy = st.builds(
    idl::Literal,
    value=
        safe_text
)
ConstType_strategy = st.builds(
    ConstType,
)
idl::FixedPtConstType_strategy = st.builds(
    idl::FixedPtConstType,
)
SwitchTypeSpec_strategy = st.builds(
    SwitchTypeSpec,
)
idl::EnumType_strategy = st.builds(
    idl::EnumType,
    literal=
        safe_text,
    name=
        safe_text
)
SimpleTypeSpec_strategy = st.builds(
    SimpleTypeSpec,
)
idl::TemplateTypeSpec_strategy = st.builds(
    idl::TemplateTypeSpec,
)
ParamTypeSpec_strategy = st.builds(
    ParamTypeSpec,
)
idl::BaseTypeSpec_strategy = st.builds(
    idl::BaseTypeSpec,
)
OpTypeDecl_strategy = st.builds(
    OpTypeDecl,
)
idl::ParamDcl_strategy = st.builds(
    idl::ParamDcl,
    direction=
        safe_text,
    name=
        safe_text
)
idl::PositiveIntConst_strategy = st.builds(
    idl::PositiveIntConst,
)
TemplateTypeSpec_strategy = st.builds(
    TemplateTypeSpec,
)
idl::FixedPtType_strategy = st.builds(
    idl::FixedPtType,
)
idl::SequenceType_strategy = st.builds(
    idl::SequenceType,
)
idl::WideStringType_strategy = st.builds(
    idl::WideStringType,
)
idl::StringType_strategy = st.builds(
    idl::StringType,
)
UnsignedInt_strategy = st.builds(
    UnsignedInt,
)
idl::UnsignedLongLongInt_strategy = st.builds(
    idl::UnsignedLongLongInt,
)
idl::UnsignedLongInt_strategy = st.builds(
    idl::UnsignedLongInt,
)
idl::UnsignedShortInt_strategy = st.builds(
    idl::UnsignedShortInt,
)
SignedInt_strategy = st.builds(
    SignedInt,
)
idl::SignedLongLongInt_strategy = st.builds(
    idl::SignedLongLongInt,
)
idl::SignedLongInt_strategy = st.builds(
    idl::SignedLongInt,
)
idl::SignedShortInt_strategy = st.builds(
    idl::SignedShortInt,
)
IntegerType_strategy = st.builds(
    IntegerType,
)
idl::UnsignedInt_strategy = st.builds(
    idl::UnsignedInt,
)
idl::SignedInt_strategy = st.builds(
    idl::SignedInt,
)
FloatingPtType_strategy = st.builds(
    FloatingPtType,
)
idl::LongDoubleType_strategy = st.builds(
    idl::LongDoubleType,
)
idl::DoubleType_strategy = st.builds(
    idl::DoubleType,
)
idl::FloatType_strategy = st.builds(
    idl::FloatType,
)
BaseTypeSpec_strategy = st.builds(
    BaseTypeSpec,
)
idl::OctetType_strategy = st.builds(
    idl::OctetType,
)
idl::AnyType_strategy = st.builds(
    idl::AnyType,
)
idl::IntegerType_strategy = st.builds(
    idl::IntegerType,
)
idl::ValueBaseType_strategy = st.builds(
    idl::ValueBaseType,
)
idl::WideCharType_strategy = st.builds(
    idl::WideCharType,
)
idl::CharType_strategy = st.builds(
    idl::CharType,
)
idl::ObjectType_strategy = st.builds(
    idl::ObjectType,
)
idl::BooleanType_strategy = st.builds(
    idl::BooleanType,
)
idl::FloatingPtType_strategy = st.builds(
    idl::FloatingPtType,
)
idl::ParamTypeSpec_strategy = st.builds(
    idl::ParamTypeSpec,
)
ConnectorExport_strategy = st.builds(
    ConnectorExport,
)
idl::PortDecl_strategy = st.builds(
    idl::PortDecl,
    name=
        safe_text,
    isMirror=
        st.booleans()
)
PortExport_strategy = st.builds(
    PortExport,
)
idl::UsesDcl_strategy = st.builds(
    idl::UsesDcl,
    isMultiple=
        st.booleans(),
    name=
        safe_text
)
idl::ProvidesDcl_strategy = st.builds(
    idl::ProvidesDcl,
    name=
        safe_text
)
idl::AttrDecl_strategy = st.builds(
    idl::AttrDecl,
    names=
        safe_text
)
HomeExport_strategy = st.builds(
    HomeExport,
)
idl::FactoryDcl_strategy = st.builds(
    idl::FactoryDcl,
    name=
        safe_text
)
idl::FinderDcl_strategy = st.builds(
    idl::FinderDcl,
    name=
        safe_text
)
idl::Export_strategy = st.builds(
    idl::Export,
)
idl::ScopedName_strategy = st.builds(
    idl::ScopedName,
    name=
        safe_text
)
idl::ContextExpr_strategy = st.builds(
    idl::ContextExpr,
    literal=
        safe_text
)
idl::ParameterDecls_strategy = st.builds(
    idl::ParameterDecls,
)
idl::OpTypeDecl_strategy = st.builds(
    idl::OpTypeDecl,
)
idl::OpDecl_strategy = st.builds(
    idl::OpDecl,
    name=
        safe_text,
    isOneway=
        st.booleans()
)
idl::ExceptionList_strategy = st.builds(
    idl::ExceptionList,
)
idl::AttrRaisesExpr_strategy = st.builds(
    idl::AttrRaisesExpr,
)
AttrDecl_strategy = st.builds(
    AttrDecl,
)
idl::ReadOnlyAttrSpec_strategy = st.builds(
    idl::ReadOnlyAttrSpec,
)
idl::AttrSpec_strategy = st.builds(
    idl::AttrSpec,
)
idl::Preproc::Pragma::Component_strategy = st.builds(
    idl::Preproc::Pragma::Component,
    value=
        safe_text
)
idl::Preproc::Pragma::Ndds_strategy = st.builds(
    idl::Preproc::Pragma::Ndds,
    value=
        safe_text
)
idl::Preproc::Pragma::Ciao::Ami4ccm::Idl_strategy = st.builds(
    idl::Preproc::Pragma::Ciao::Ami4ccm::Idl,
    value=
        safe_text
)
idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle_strategy = st.builds(
    idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle,
    value=
        safe_text
)
idl::Preproc::Pragma::Ciao::Ami4ccm::Interface_strategy = st.builds(
    idl::Preproc::Pragma::Ciao::Ami4ccm::Interface,
    value=
        safe_text
)
idl::Preproc::Pragma::Ciao::Lem_strategy = st.builds(
    idl::Preproc::Pragma::Ciao::Lem,
    value=
        safe_text
)
idl::InterfaceBody_strategy = st.builds(
    idl::InterfaceBody,
)
idl::Interface::header_strategy = st.builds(
    idl::Interface::header,
    isAbstract=
        st.booleans(),
    name=
        safe_text,
    isLocal=
        st.booleans()
)
FixedDefinition_strategy = st.builds(
    FixedDefinition,
)
TemplateDefinition_strategy = st.builds(
    TemplateDefinition,
)
idl::PortTypeDecl_strategy = st.builds(
    idl::PortTypeDecl,
    name=
        safe_text
)
idl::TypeDecl_strategy = st.builds(
    idl::TypeDecl,
)
idl::ExceptDecl_strategy = st.builds(
    idl::ExceptDecl,
    name=
        safe_text
)
idl::Event_strategy = st.builds(
    idl::Event,
    name=
        safe_text,
    isAbstract=
        st.booleans()
)
idl::HomeDecl_strategy = st.builds(
    idl::HomeDecl,
    name=
        safe_text
)
idl::FixedModule_strategy = st.builds(
    idl::FixedModule,
    name=
        safe_text
)
idl::NativeType_strategy = st.builds(
    idl::NativeType,
    name=
        safe_text
)
idl::ComponentDecl_strategy = st.builds(
    idl::ComponentDecl,
    name=
        safe_text
)
idl::ConstDecl_strategy = st.builds(
    idl::ConstDecl,
    name=
        safe_text
)
idl::Connector_strategy = st.builds(
    idl::Connector,
)
idl::TemplateModuleRef_strategy = st.builds(
    idl::TemplateModuleRef,
    name=
        safe_text,
    id=
        safe_text
)
Interface::or::Forward::Decl_strategy = st.builds(
    Interface::or::Forward::Decl,
)
idl::Forward::decl_strategy = st.builds(
    idl::Forward::decl,
    name=
        safe_text
)
idl::Interface::decl_strategy = st.builds(
    idl::Interface::decl,
)
idl::Interface::or::Forward::Decl_strategy = st.builds(
    idl::Interface::or::Forward::Decl,
)
idl::IDLComment_strategy = st.builds(
    idl::IDLComment,
    body=
        safe_text
)
idl::Module_strategy = st.builds(
    idl::Module,
    name=
        safe_text
)
idl::Excluded::File::Marker_strategy = st.builds(
    idl::Excluded::File::Marker,
    file=
        safe_text
)
idl::File::Marker_strategy = st.builds(
    idl::File::Marker,
    file=
        safe_text
)
idl::Preproc::Pragma::Misc_strategy = st.builds(
    idl::Preproc::Pragma::Misc,
)
idl::Preproc::Pragma::DDS4CCM::Impl_strategy = st.builds(
    idl::Preproc::Pragma::DDS4CCM::Impl,
    value=
        safe_text
)
idl::Preproc::Pragma::Home_strategy = st.builds(
    idl::Preproc::Pragma::Home,
    value=
        safe_text
)
idl::Preproc::Ifndef_strategy = st.builds(
    idl::Preproc::Ifndef,
    value=
        safe_text
)
idl::Preproc::Ifdef_strategy = st.builds(
    idl::Preproc::Ifdef,
    value=
        safe_text
)
idl::FileName_strategy = st.builds(
    idl::FileName,
    name=
        safe_text
)

@given(instance=idl::FormalParameterType_strategy)
@settings(max_examples=50)
def test_idl::formalparametertype_instantiation(instance):
    assert isinstance(instance, idl::FormalParameterType)

@given(instance=idl::TemplateDefinition_strategy)
@settings(max_examples=50)
def test_idl::templatedefinition_instantiation(instance):
    assert isinstance(instance, idl::TemplateDefinition)

@given(instance=idl::FormalParameter_strategy)
@settings(max_examples=50)
def test_idl::formalparameter_instantiation(instance):
    assert isinstance(instance, idl::FormalParameter)

@given(instance=idl::FormalParameter_strategy)
def test_idl::formalparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::FormalParameter_strategy)
def test_idl::formalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::ActualParameter_strategy)
@settings(max_examples=50)
def test_idl::actualparameter_instantiation(instance):
    assert isinstance(instance, idl::ActualParameter)

@given(instance=idl::FixedDefinition_strategy)
@settings(max_examples=50)
def test_idl::fixeddefinition_instantiation(instance):
    assert isinstance(instance, idl::FixedDefinition)

@given(instance=idl::StateMember_strategy)
@settings(max_examples=50)
def test_idl::statemember_instantiation(instance):
    assert isinstance(instance, idl::StateMember)

@given(instance=idl::StateMember_strategy)
def test_idl::statemember_isPublic_type(instance):
    assert isinstance(instance.isPublic, bool)


@given(instance=idl::StateMember_strategy)
def test_idl::statemember_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original

@given(instance=idl::StateMember_strategy)
def test_idl::statemember_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=idl::StateMember_strategy)
def test_idl::statemember_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=idl::EventDcl_strategy)
@settings(max_examples=50)
def test_idl::eventdcl_instantiation(instance):
    assert isinstance(instance, idl::EventDcl)

@given(instance=idl::EventDcl_strategy)
def test_idl::eventdcl_isTruncatable_type(instance):
    assert isinstance(instance.isTruncatable, bool)


@given(instance=idl::EventDcl_strategy)
def test_idl::eventdcl_isTruncatable_setter(instance):
    original = instance.isTruncatable
    instance.isTruncatable = original
    assert instance.isTruncatable == original

@given(instance=idl::EventDcl_strategy)
def test_idl::eventdcl_isCustom_type(instance):
    assert isinstance(instance.isCustom, bool)


@given(instance=idl::EventDcl_strategy)
def test_idl::eventdcl_isCustom_setter(instance):
    original = instance.isCustom
    instance.isCustom = original
    assert instance.isCustom == original

@given(instance=idl::ConnectorExport_strategy)
@settings(max_examples=50)
def test_idl::connectorexport_instantiation(instance):
    assert isinstance(instance, idl::ConnectorExport)

@given(instance=idl::ConnectorHeader_strategy)
@settings(max_examples=50)
def test_idl::connectorheader_instantiation(instance):
    assert isinstance(instance, idl::ConnectorHeader)

@given(instance=idl::ConnectorHeader_strategy)
def test_idl::connectorheader_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ConnectorHeader_strategy)
def test_idl::connectorheader_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::PortExport_strategy)
@settings(max_examples=50)
def test_idl::portexport_instantiation(instance):
    assert isinstance(instance, idl::PortExport)

@given(instance=idl::EventForwardDcl_strategy)
@settings(max_examples=50)
def test_idl::eventforwarddcl_instantiation(instance):
    assert isinstance(instance, idl::EventForwardDcl)

@given(instance=idl::HomeExport_strategy)
@settings(max_examples=50)
def test_idl::homeexport_instantiation(instance):
    assert isinstance(instance, idl::HomeExport)

@given(instance=idl::PrimaryKeySpec_strategy)
@settings(max_examples=50)
def test_idl::primarykeyspec_instantiation(instance):
    assert isinstance(instance, idl::PrimaryKeySpec)

@given(instance=idl::ComponentExport_strategy)
@settings(max_examples=50)
def test_idl::componentexport_instantiation(instance):
    assert isinstance(instance, idl::ComponentExport)

@given(instance=idl::PrimaryExpr_strategy)
@settings(max_examples=50)
def test_idl::primaryexpr_instantiation(instance):
    assert isinstance(instance, idl::PrimaryExpr)

@given(instance=ConstParamType_strategy)
@settings(max_examples=50)
def test_constparamtype_instantiation(instance):
    assert isinstance(instance, ConstParamType)

@given(instance=idl::ConstType_strategy)
@settings(max_examples=50)
def test_idl::consttype_instantiation(instance):
    assert isinstance(instance, idl::ConstType)

@given(instance=idl::UnaryExpr_strategy)
@settings(max_examples=50)
def test_idl::unaryexpr_instantiation(instance):
    assert isinstance(instance, idl::UnaryExpr)

@given(instance=idl::UnaryExpr_strategy)
def test_idl::unaryexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::UnaryExpr_strategy)
def test_idl::unaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::MultExpr_strategy)
@settings(max_examples=50)
def test_idl::multexpr_instantiation(instance):
    assert isinstance(instance, idl::MultExpr)

@given(instance=idl::MultExpr_strategy)
def test_idl::multexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::MultExpr_strategy)
def test_idl::multexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::AddExpr_strategy)
@settings(max_examples=50)
def test_idl::addexpr_instantiation(instance):
    assert isinstance(instance, idl::AddExpr)

@given(instance=idl::AddExpr_strategy)
def test_idl::addexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::AddExpr_strategy)
def test_idl::addexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::ShiftExpr_strategy)
@settings(max_examples=50)
def test_idl::shiftexpr_instantiation(instance):
    assert isinstance(instance, idl::ShiftExpr)

@given(instance=idl::ShiftExpr_strategy)
def test_idl::shiftexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::ShiftExpr_strategy)
def test_idl::shiftexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::AndExpr_strategy)
@settings(max_examples=50)
def test_idl::andexpr_instantiation(instance):
    assert isinstance(instance, idl::AndExpr)

@given(instance=idl::AndExpr_strategy)
def test_idl::andexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::AndExpr_strategy)
def test_idl::andexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::XOrExpr_strategy)
@settings(max_examples=50)
def test_idl::xorexpr_instantiation(instance):
    assert isinstance(instance, idl::XOrExpr)

@given(instance=idl::XOrExpr_strategy)
def test_idl::xorexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::XOrExpr_strategy)
def test_idl::xorexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ConstExp_strategy)
@settings(max_examples=50)
def test_constexp_instantiation(instance):
    assert isinstance(instance, ConstExp)

@given(instance=idl::OrExpr_strategy)
@settings(max_examples=50)
def test_idl::orexpr_instantiation(instance):
    assert isinstance(instance, idl::OrExpr)

@given(instance=idl::OrExpr_strategy)
def test_idl::orexpr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::OrExpr_strategy)
def test_idl::orexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::ElementSpec_strategy)
@settings(max_examples=50)
def test_idl::elementspec_instantiation(instance):
    assert isinstance(instance, idl::ElementSpec)

@given(instance=idl::CaseLabel_strategy)
@settings(max_examples=50)
def test_idl::caselabel_instantiation(instance):
    assert isinstance(instance, idl::CaseLabel)

@given(instance=idl::CaseLabel_strategy)
def test_idl::caselabel_isCase_type(instance):
    assert isinstance(instance.isCase, bool)


@given(instance=idl::CaseLabel_strategy)
def test_idl::caselabel_isCase_setter(instance):
    original = instance.isCase
    instance.isCase = original
    assert instance.isCase == original

@given(instance=idl::CaseLabel_strategy)
def test_idl::caselabel_isDefault_type(instance):
    assert isinstance(instance.isDefault, bool)


@given(instance=idl::CaseLabel_strategy)
def test_idl::caselabel_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original

@given(instance=idl::Case_strategy)
@settings(max_examples=50)
def test_idl::case_instantiation(instance):
    assert isinstance(instance, idl::Case)

@given(instance=idl::SwitchBody_strategy)
@settings(max_examples=50)
def test_idl::switchbody_instantiation(instance):
    assert isinstance(instance, idl::SwitchBody)

@given(instance=idl::SwitchTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::switchtypespec_instantiation(instance):
    assert isinstance(instance, idl::SwitchTypeSpec)

@given(instance=ConstrForwardDecl_strategy)
@settings(max_examples=50)
def test_constrforwarddecl_instantiation(instance):
    assert isinstance(instance, ConstrForwardDecl)

@given(instance=idl::UnionForwardDecl_strategy)
@settings(max_examples=50)
def test_idl::unionforwarddecl_instantiation(instance):
    assert isinstance(instance, idl::UnionForwardDecl)

@given(instance=idl::StructForwardDecl_strategy)
@settings(max_examples=50)
def test_idl::structforwarddecl_instantiation(instance):
    assert isinstance(instance, idl::StructForwardDecl)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=idl::ExceptionParamType_strategy)
@settings(max_examples=50)
def test_idl::exceptionparamtype_instantiation(instance):
    assert isinstance(instance, idl::ExceptionParamType)

@given(instance=idl::EventParamType_strategy)
@settings(max_examples=50)
def test_idl::eventparamtype_instantiation(instance):
    assert isinstance(instance, idl::EventParamType)

@given(instance=idl::ValuetypeParamType_strategy)
@settings(max_examples=50)
def test_idl::valuetypeparamtype_instantiation(instance):
    assert isinstance(instance, idl::ValuetypeParamType)

@given(instance=idl::InterfaceParamType_strategy)
@settings(max_examples=50)
def test_idl::interfaceparamtype_instantiation(instance):
    assert isinstance(instance, idl::InterfaceParamType)

@given(instance=idl::EnumParamType_strategy)
@settings(max_examples=50)
def test_idl::enumparamtype_instantiation(instance):
    assert isinstance(instance, idl::EnumParamType)

@given(instance=idl::ConstParamType_strategy)
@settings(max_examples=50)
def test_idl::constparamtype_instantiation(instance):
    assert isinstance(instance, idl::ConstParamType)

@given(instance=idl::SequenceParamType_strategy)
@settings(max_examples=50)
def test_idl::sequenceparamtype_instantiation(instance):
    assert isinstance(instance, idl::SequenceParamType)

@given(instance=idl::TypenameParamType_strategy)
@settings(max_examples=50)
def test_idl::typenameparamtype_instantiation(instance):
    assert isinstance(instance, idl::TypenameParamType)

@given(instance=idl::UnionParamType_strategy)
@settings(max_examples=50)
def test_idl::unionparamtype_instantiation(instance):
    assert isinstance(instance, idl::UnionParamType)

@given(instance=idl::StructParamType_strategy)
@settings(max_examples=50)
def test_idl::structparamtype_instantiation(instance):
    assert isinstance(instance, idl::StructParamType)

@given(instance=idl::Declarator_strategy)
@settings(max_examples=50)
def test_idl::declarator_instantiation(instance):
    assert isinstance(instance, idl::Declarator)

@given(instance=idl::Declarator_strategy)
def test_idl::declarator_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=idl::Declarator_strategy)
def test_idl::declarator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=idl::Member_strategy)
@settings(max_examples=50)
def test_idl::member_instantiation(instance):
    assert isinstance(instance, idl::Member)

@given(instance=TypeSpec_strategy)
@settings(max_examples=50)
def test_typespec_instantiation(instance):
    assert isinstance(instance, TypeSpec)

@given(instance=idl::ConstrTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::constrtypespec_instantiation(instance):
    assert isinstance(instance, idl::ConstrTypeSpec)

@given(instance=idl::SimpleTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::simpletypespec_instantiation(instance):
    assert isinstance(instance, idl::SimpleTypeSpec)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=idl::TypeSpec_strategy)
@settings(max_examples=50)
def test_idl::typespec_instantiation(instance):
    assert isinstance(instance, idl::TypeSpec)

@given(instance=ConstrTypeSpec_strategy)
@settings(max_examples=50)
def test_constrtypespec_instantiation(instance):
    assert isinstance(instance, ConstrTypeSpec)

@given(instance=TypeDecl_strategy)
@settings(max_examples=50)
def test_typedecl_instantiation(instance):
    assert isinstance(instance, TypeDecl)

@given(instance=idl::ConstrForwardDecl_strategy)
@settings(max_examples=50)
def test_idl::constrforwarddecl_instantiation(instance):
    assert isinstance(instance, idl::ConstrForwardDecl)

@given(instance=idl::ConstrForwardDecl_strategy)
def test_idl::constrforwarddecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ConstrForwardDecl_strategy)
def test_idl::constrforwarddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::UnionType_strategy)
@settings(max_examples=50)
def test_idl::uniontype_instantiation(instance):
    assert isinstance(instance, idl::UnionType)

@given(instance=idl::UnionType_strategy)
def test_idl::uniontype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::UnionType_strategy)
def test_idl::uniontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::TypeDeclarator_strategy)
@settings(max_examples=50)
def test_idl::typedeclarator_instantiation(instance):
    assert isinstance(instance, idl::TypeDeclarator)

@given(instance=Preproc_strategy)
@settings(max_examples=50)
def test_preproc_instantiation(instance):
    assert isinstance(instance, Preproc)

@given(instance=idl::Preproc::Include_strategy)
@settings(max_examples=50)
def test_idl::preproc::include_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Include)

@given(instance=idl::Preproc::Include_strategy)
def test_idl::preproc::include_strValue_type(instance):
    assert isinstance(instance.strValue, str)


@given(instance=idl::Preproc::Include_strategy)
def test_idl::preproc::include_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=ComponentExport_strategy)
@settings(max_examples=50)
def test_componentexport_instantiation(instance):
    assert isinstance(instance, ComponentExport)

@given(instance=idl::ConsumesDcl_strategy)
@settings(max_examples=50)
def test_idl::consumesdcl_instantiation(instance):
    assert isinstance(instance, idl::ConsumesDcl)

@given(instance=idl::ConsumesDcl_strategy)
def test_idl::consumesdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ConsumesDcl_strategy)
def test_idl::consumesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::EmitDcl_strategy)
@settings(max_examples=50)
def test_idl::emitdcl_instantiation(instance):
    assert isinstance(instance, idl::EmitDcl)

@given(instance=idl::EmitDcl_strategy)
def test_idl::emitdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::EmitDcl_strategy)
def test_idl::emitdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::PublishesDcl_strategy)
@settings(max_examples=50)
def test_idl::publishesdcl_instantiation(instance):
    assert isinstance(instance, idl::PublishesDcl)

@given(instance=idl::PublishesDcl_strategy)
def test_idl::publishesdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::PublishesDcl_strategy)
def test_idl::publishesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Export_strategy)
@settings(max_examples=50)
def test_export_instantiation(instance):
    assert isinstance(instance, Export)

@given(instance=Definition_strategy)
@settings(max_examples=50)
def test_definition_instantiation(instance):
    assert isinstance(instance, Definition)

@given(instance=idl::ComponentForwardDecl_strategy)
@settings(max_examples=50)
def test_idl::componentforwarddecl_instantiation(instance):
    assert isinstance(instance, idl::ComponentForwardDecl)

@given(instance=idl::ComponentForwardDecl_strategy)
def test_idl::componentforwarddecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ComponentForwardDecl_strategy)
def test_idl::componentforwarddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::TemplateModuleInst_strategy)
@settings(max_examples=50)
def test_idl::templatemoduleinst_instantiation(instance):
    assert isinstance(instance, idl::TemplateModuleInst)

@given(instance=idl::TemplateModuleInst_strategy)
def test_idl::templatemoduleinst_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::TemplateModuleInst_strategy)
def test_idl::templatemoduleinst_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::TemplateModule_strategy)
@settings(max_examples=50)
def test_idl::templatemodule_instantiation(instance):
    assert isinstance(instance, idl::TemplateModule)

@given(instance=idl::TemplateModule_strategy)
def test_idl::templatemodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::TemplateModule_strategy)
def test_idl::templatemodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::StructType_strategy)
@settings(max_examples=50)
def test_idl::structtype_instantiation(instance):
    assert isinstance(instance, idl::StructType)

@given(instance=idl::StructType_strategy)
def test_idl::structtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::StructType_strategy)
def test_idl::structtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Preproc_strategy)
@settings(max_examples=50)
def test_idl::preproc_instantiation(instance):
    assert isinstance(instance, idl::Preproc)

@given(instance=idl::Definition_strategy)
@settings(max_examples=50)
def test_idl::definition_instantiation(instance):
    assert isinstance(instance, idl::Definition)

@given(instance=idl::Import::decl_strategy)
@settings(max_examples=50)
def test_idl::import::decl_instantiation(instance):
    assert isinstance(instance, idl::Import::decl)

@given(instance=idl::Import::decl_strategy)
def test_idl::import::decl_imported_scope_type(instance):
    assert isinstance(instance.imported_scope, str)


@given(instance=idl::Import::decl_strategy)
def test_idl::import::decl_imported_scope_setter(instance):
    original = instance.imported_scope
    instance.imported_scope = original
    assert instance.imported_scope == original

@given(instance=idl::Specification_strategy)
@settings(max_examples=50)
def test_idl::specification_instantiation(instance):
    assert isinstance(instance, idl::Specification)

@given(instance=Preproc::Pragma_strategy)
@settings(max_examples=50)
def test_preproc::pragma_instantiation(instance):
    assert isinstance(instance, Preproc::Pragma)

@given(instance=idl::Preproc::Pragma::Conn::Type_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::conn::type_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Conn::Type)

@given(instance=idl::Preproc::Pragma::Conn::Type_strategy)
def test_idl::preproc::pragma::conn::type_valuePort_type(instance):
    assert isinstance(instance.valuePort, str)


@given(instance=idl::Preproc::Pragma::Conn::Type_strategy)
def test_idl::preproc::pragma::conn::type_valuePort_setter(instance):
    original = instance.valuePort
    instance.valuePort = original
    assert instance.valuePort == original

@given(instance=idl::Preproc::Pragma::Conn::Type_strategy)
def test_idl::preproc::pragma::conn::type_valueConnType_type(instance):
    assert isinstance(instance.valueConnType, str)


@given(instance=idl::Preproc::Pragma::Conn::Type_strategy)
def test_idl::preproc::pragma::conn::type_valueConnType_setter(instance):
    original = instance.valueConnType
    instance.valueConnType = original
    assert instance.valueConnType == original

@given(instance=idl::Preproc::Pragma::Prefix_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::prefix_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Prefix)

@given(instance=idl::Preproc::Pragma::Prefix_strategy)
def test_idl::preproc::pragma::prefix_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Prefix_strategy)
def test_idl::preproc::pragma::prefix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma)

@given(instance=idl::Preproc::Endif_strategy)
@settings(max_examples=50)
def test_idl::preproc::endif_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Endif)

@given(instance=idl::Preproc::Define_strategy)
@settings(max_examples=50)
def test_idl::preproc::define_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Define)

@given(instance=idl::Preproc::Define_strategy)
def test_idl::preproc::define_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Define_strategy)
def test_idl::preproc::define_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Error_strategy)
@settings(max_examples=50)
def test_idl::preproc::error_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Error)

@given(instance=idl::Preproc::Error_strategy)
def test_idl::preproc::error_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Error_strategy)
def test_idl::preproc::error_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Else_strategy)
@settings(max_examples=50)
def test_idl::preproc::else_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Else)

@given(instance=idl::Preproc::If::Val_strategy)
@settings(max_examples=50)
def test_idl::preproc::if::val_instantiation(instance):
    assert isinstance(instance, idl::Preproc::If::Val)

@given(instance=idl::Preproc::If::Compare_strategy)
@settings(max_examples=50)
def test_idl::preproc::if::compare_instantiation(instance):
    assert isinstance(instance, idl::Preproc::If::Compare)

@given(instance=idl::Preproc::If::Compare_strategy)
def test_idl::preproc::if::compare_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=idl::Preproc::If::Compare_strategy)
def test_idl::preproc::if::compare_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl::Preproc::If_strategy)
@settings(max_examples=50)
def test_idl::preproc::if_instantiation(instance):
    assert isinstance(instance, idl::Preproc::If)

@given(instance=idl::Preproc::If_strategy)
def test_idl::preproc::if_negation_type(instance):
    assert isinstance(instance.negation, bool)


@given(instance=idl::Preproc::If_strategy)
def test_idl::preproc::if_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original

@given(instance=idl::Preproc::Undef_strategy)
@settings(max_examples=50)
def test_idl::preproc::undef_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Undef)

@given(instance=idl::Preproc::Undef_strategy)
def test_idl::preproc::undef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Undef_strategy)
def test_idl::preproc::undef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ComplexDeclarator_strategy)
@settings(max_examples=50)
def test_complexdeclarator_instantiation(instance):
    assert isinstance(instance, ComplexDeclarator)

@given(instance=idl::ComplexDeclarator_strategy)
@settings(max_examples=50)
def test_idl::complexdeclarator_instantiation(instance):
    assert isinstance(instance, idl::ComplexDeclarator)

@given(instance=Declarator_strategy)
@settings(max_examples=50)
def test_declarator_instantiation(instance):
    assert isinstance(instance, Declarator)

@given(instance=idl::ArrayDeclarator_strategy)
@settings(max_examples=50)
def test_idl::arraydeclarator_instantiation(instance):
    assert isinstance(instance, idl::ArrayDeclarator)

@given(instance=idl::SimpleDeclarator_strategy)
@settings(max_examples=50)
def test_idl::simpledeclarator_instantiation(instance):
    assert isinstance(instance, idl::SimpleDeclarator)

@given(instance=PrimaryExpr_strategy)
@settings(max_examples=50)
def test_primaryexpr_instantiation(instance):
    assert isinstance(instance, PrimaryExpr)

@given(instance=idl::ConstExp_strategy)
@settings(max_examples=50)
def test_idl::constexp_instantiation(instance):
    assert isinstance(instance, idl::ConstExp)

@given(instance=idl::Literal_strategy)
@settings(max_examples=50)
def test_idl::literal_instantiation(instance):
    assert isinstance(instance, idl::Literal)

@given(instance=idl::Literal_strategy)
def test_idl::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Literal_strategy)
def test_idl::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ConstType_strategy)
@settings(max_examples=50)
def test_consttype_instantiation(instance):
    assert isinstance(instance, ConstType)

@given(instance=idl::FixedPtConstType_strategy)
@settings(max_examples=50)
def test_idl::fixedptconsttype_instantiation(instance):
    assert isinstance(instance, idl::FixedPtConstType)

@given(instance=SwitchTypeSpec_strategy)
@settings(max_examples=50)
def test_switchtypespec_instantiation(instance):
    assert isinstance(instance, SwitchTypeSpec)

@given(instance=idl::EnumType_strategy)
@settings(max_examples=50)
def test_idl::enumtype_instantiation(instance):
    assert isinstance(instance, idl::EnumType)

@given(instance=idl::EnumType_strategy)
def test_idl::enumtype_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=idl::EnumType_strategy)
def test_idl::enumtype_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=idl::EnumType_strategy)
def test_idl::enumtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::EnumType_strategy)
def test_idl::enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleTypeSpec_strategy)
@settings(max_examples=50)
def test_simpletypespec_instantiation(instance):
    assert isinstance(instance, SimpleTypeSpec)

@given(instance=idl::TemplateTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::templatetypespec_instantiation(instance):
    assert isinstance(instance, idl::TemplateTypeSpec)

@given(instance=ParamTypeSpec_strategy)
@settings(max_examples=50)
def test_paramtypespec_instantiation(instance):
    assert isinstance(instance, ParamTypeSpec)

@given(instance=idl::BaseTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::basetypespec_instantiation(instance):
    assert isinstance(instance, idl::BaseTypeSpec)

@given(instance=OpTypeDecl_strategy)
@settings(max_examples=50)
def test_optypedecl_instantiation(instance):
    assert isinstance(instance, OpTypeDecl)

@given(instance=idl::ParamDcl_strategy)
@settings(max_examples=50)
def test_idl::paramdcl_instantiation(instance):
    assert isinstance(instance, idl::ParamDcl)

@given(instance=idl::ParamDcl_strategy)
def test_idl::paramdcl_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=idl::ParamDcl_strategy)
def test_idl::paramdcl_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=idl::ParamDcl_strategy)
def test_idl::paramdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ParamDcl_strategy)
def test_idl::paramdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::PositiveIntConst_strategy)
@settings(max_examples=50)
def test_idl::positiveintconst_instantiation(instance):
    assert isinstance(instance, idl::PositiveIntConst)

@given(instance=TemplateTypeSpec_strategy)
@settings(max_examples=50)
def test_templatetypespec_instantiation(instance):
    assert isinstance(instance, TemplateTypeSpec)

@given(instance=idl::FixedPtType_strategy)
@settings(max_examples=50)
def test_idl::fixedpttype_instantiation(instance):
    assert isinstance(instance, idl::FixedPtType)

@given(instance=idl::SequenceType_strategy)
@settings(max_examples=50)
def test_idl::sequencetype_instantiation(instance):
    assert isinstance(instance, idl::SequenceType)

@given(instance=idl::WideStringType_strategy)
@settings(max_examples=50)
def test_idl::widestringtype_instantiation(instance):
    assert isinstance(instance, idl::WideStringType)

@given(instance=idl::StringType_strategy)
@settings(max_examples=50)
def test_idl::stringtype_instantiation(instance):
    assert isinstance(instance, idl::StringType)

@given(instance=UnsignedInt_strategy)
@settings(max_examples=50)
def test_unsignedint_instantiation(instance):
    assert isinstance(instance, UnsignedInt)

@given(instance=idl::UnsignedLongLongInt_strategy)
@settings(max_examples=50)
def test_idl::unsignedlonglongint_instantiation(instance):
    assert isinstance(instance, idl::UnsignedLongLongInt)

@given(instance=idl::UnsignedLongInt_strategy)
@settings(max_examples=50)
def test_idl::unsignedlongint_instantiation(instance):
    assert isinstance(instance, idl::UnsignedLongInt)

@given(instance=idl::UnsignedShortInt_strategy)
@settings(max_examples=50)
def test_idl::unsignedshortint_instantiation(instance):
    assert isinstance(instance, idl::UnsignedShortInt)

@given(instance=SignedInt_strategy)
@settings(max_examples=50)
def test_signedint_instantiation(instance):
    assert isinstance(instance, SignedInt)

@given(instance=idl::SignedLongLongInt_strategy)
@settings(max_examples=50)
def test_idl::signedlonglongint_instantiation(instance):
    assert isinstance(instance, idl::SignedLongLongInt)

@given(instance=idl::SignedLongInt_strategy)
@settings(max_examples=50)
def test_idl::signedlongint_instantiation(instance):
    assert isinstance(instance, idl::SignedLongInt)

@given(instance=idl::SignedShortInt_strategy)
@settings(max_examples=50)
def test_idl::signedshortint_instantiation(instance):
    assert isinstance(instance, idl::SignedShortInt)

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=idl::UnsignedInt_strategy)
@settings(max_examples=50)
def test_idl::unsignedint_instantiation(instance):
    assert isinstance(instance, idl::UnsignedInt)

@given(instance=idl::SignedInt_strategy)
@settings(max_examples=50)
def test_idl::signedint_instantiation(instance):
    assert isinstance(instance, idl::SignedInt)

@given(instance=FloatingPtType_strategy)
@settings(max_examples=50)
def test_floatingpttype_instantiation(instance):
    assert isinstance(instance, FloatingPtType)

@given(instance=idl::LongDoubleType_strategy)
@settings(max_examples=50)
def test_idl::longdoubletype_instantiation(instance):
    assert isinstance(instance, idl::LongDoubleType)

@given(instance=idl::DoubleType_strategy)
@settings(max_examples=50)
def test_idl::doubletype_instantiation(instance):
    assert isinstance(instance, idl::DoubleType)

@given(instance=idl::FloatType_strategy)
@settings(max_examples=50)
def test_idl::floattype_instantiation(instance):
    assert isinstance(instance, idl::FloatType)

@given(instance=BaseTypeSpec_strategy)
@settings(max_examples=50)
def test_basetypespec_instantiation(instance):
    assert isinstance(instance, BaseTypeSpec)

@given(instance=idl::OctetType_strategy)
@settings(max_examples=50)
def test_idl::octettype_instantiation(instance):
    assert isinstance(instance, idl::OctetType)

@given(instance=idl::AnyType_strategy)
@settings(max_examples=50)
def test_idl::anytype_instantiation(instance):
    assert isinstance(instance, idl::AnyType)

@given(instance=idl::IntegerType_strategy)
@settings(max_examples=50)
def test_idl::integertype_instantiation(instance):
    assert isinstance(instance, idl::IntegerType)

@given(instance=idl::ValueBaseType_strategy)
@settings(max_examples=50)
def test_idl::valuebasetype_instantiation(instance):
    assert isinstance(instance, idl::ValueBaseType)

@given(instance=idl::WideCharType_strategy)
@settings(max_examples=50)
def test_idl::widechartype_instantiation(instance):
    assert isinstance(instance, idl::WideCharType)

@given(instance=idl::CharType_strategy)
@settings(max_examples=50)
def test_idl::chartype_instantiation(instance):
    assert isinstance(instance, idl::CharType)

@given(instance=idl::ObjectType_strategy)
@settings(max_examples=50)
def test_idl::objecttype_instantiation(instance):
    assert isinstance(instance, idl::ObjectType)

@given(instance=idl::BooleanType_strategy)
@settings(max_examples=50)
def test_idl::booleantype_instantiation(instance):
    assert isinstance(instance, idl::BooleanType)

@given(instance=idl::FloatingPtType_strategy)
@settings(max_examples=50)
def test_idl::floatingpttype_instantiation(instance):
    assert isinstance(instance, idl::FloatingPtType)

@given(instance=idl::ParamTypeSpec_strategy)
@settings(max_examples=50)
def test_idl::paramtypespec_instantiation(instance):
    assert isinstance(instance, idl::ParamTypeSpec)

@given(instance=ConnectorExport_strategy)
@settings(max_examples=50)
def test_connectorexport_instantiation(instance):
    assert isinstance(instance, ConnectorExport)

@given(instance=idl::PortDecl_strategy)
@settings(max_examples=50)
def test_idl::portdecl_instantiation(instance):
    assert isinstance(instance, idl::PortDecl)

@given(instance=idl::PortDecl_strategy)
def test_idl::portdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::PortDecl_strategy)
def test_idl::portdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::PortDecl_strategy)
def test_idl::portdecl_isMirror_type(instance):
    assert isinstance(instance.isMirror, bool)


@given(instance=idl::PortDecl_strategy)
def test_idl::portdecl_isMirror_setter(instance):
    original = instance.isMirror
    instance.isMirror = original
    assert instance.isMirror == original

@given(instance=PortExport_strategy)
@settings(max_examples=50)
def test_portexport_instantiation(instance):
    assert isinstance(instance, PortExport)

@given(instance=idl::UsesDcl_strategy)
@settings(max_examples=50)
def test_idl::usesdcl_instantiation(instance):
    assert isinstance(instance, idl::UsesDcl)

@given(instance=idl::UsesDcl_strategy)
def test_idl::usesdcl_isMultiple_type(instance):
    assert isinstance(instance.isMultiple, bool)


@given(instance=idl::UsesDcl_strategy)
def test_idl::usesdcl_isMultiple_setter(instance):
    original = instance.isMultiple
    instance.isMultiple = original
    assert instance.isMultiple == original

@given(instance=idl::UsesDcl_strategy)
def test_idl::usesdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::UsesDcl_strategy)
def test_idl::usesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::ProvidesDcl_strategy)
@settings(max_examples=50)
def test_idl::providesdcl_instantiation(instance):
    assert isinstance(instance, idl::ProvidesDcl)

@given(instance=idl::ProvidesDcl_strategy)
def test_idl::providesdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ProvidesDcl_strategy)
def test_idl::providesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::AttrDecl_strategy)
@settings(max_examples=50)
def test_idl::attrdecl_instantiation(instance):
    assert isinstance(instance, idl::AttrDecl)

@given(instance=idl::AttrDecl_strategy)
def test_idl::attrdecl_names_type(instance):
    assert isinstance(instance.names, str)


@given(instance=idl::AttrDecl_strategy)
def test_idl::attrdecl_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=HomeExport_strategy)
@settings(max_examples=50)
def test_homeexport_instantiation(instance):
    assert isinstance(instance, HomeExport)

@given(instance=idl::FactoryDcl_strategy)
@settings(max_examples=50)
def test_idl::factorydcl_instantiation(instance):
    assert isinstance(instance, idl::FactoryDcl)

@given(instance=idl::FactoryDcl_strategy)
def test_idl::factorydcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::FactoryDcl_strategy)
def test_idl::factorydcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::FinderDcl_strategy)
@settings(max_examples=50)
def test_idl::finderdcl_instantiation(instance):
    assert isinstance(instance, idl::FinderDcl)

@given(instance=idl::FinderDcl_strategy)
def test_idl::finderdcl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::FinderDcl_strategy)
def test_idl::finderdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Export_strategy)
@settings(max_examples=50)
def test_idl::export_instantiation(instance):
    assert isinstance(instance, idl::Export)

@given(instance=idl::ScopedName_strategy)
@settings(max_examples=50)
def test_idl::scopedname_instantiation(instance):
    assert isinstance(instance, idl::ScopedName)

@given(instance=idl::ScopedName_strategy)
def test_idl::scopedname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ScopedName_strategy)
def test_idl::scopedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::ContextExpr_strategy)
@settings(max_examples=50)
def test_idl::contextexpr_instantiation(instance):
    assert isinstance(instance, idl::ContextExpr)

@given(instance=idl::ContextExpr_strategy)
def test_idl::contextexpr_literal_type(instance):
    assert isinstance(instance.literal, str)


@given(instance=idl::ContextExpr_strategy)
def test_idl::contextexpr_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=idl::ParameterDecls_strategy)
@settings(max_examples=50)
def test_idl::parameterdecls_instantiation(instance):
    assert isinstance(instance, idl::ParameterDecls)

@given(instance=idl::OpTypeDecl_strategy)
@settings(max_examples=50)
def test_idl::optypedecl_instantiation(instance):
    assert isinstance(instance, idl::OpTypeDecl)

@given(instance=idl::OpDecl_strategy)
@settings(max_examples=50)
def test_idl::opdecl_instantiation(instance):
    assert isinstance(instance, idl::OpDecl)

@given(instance=idl::OpDecl_strategy)
def test_idl::opdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::OpDecl_strategy)
def test_idl::opdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::OpDecl_strategy)
def test_idl::opdecl_isOneway_type(instance):
    assert isinstance(instance.isOneway, bool)


@given(instance=idl::OpDecl_strategy)
def test_idl::opdecl_isOneway_setter(instance):
    original = instance.isOneway
    instance.isOneway = original
    assert instance.isOneway == original

@given(instance=idl::ExceptionList_strategy)
@settings(max_examples=50)
def test_idl::exceptionlist_instantiation(instance):
    assert isinstance(instance, idl::ExceptionList)

@given(instance=idl::AttrRaisesExpr_strategy)
@settings(max_examples=50)
def test_idl::attrraisesexpr_instantiation(instance):
    assert isinstance(instance, idl::AttrRaisesExpr)

@given(instance=AttrDecl_strategy)
@settings(max_examples=50)
def test_attrdecl_instantiation(instance):
    assert isinstance(instance, AttrDecl)

@given(instance=idl::ReadOnlyAttrSpec_strategy)
@settings(max_examples=50)
def test_idl::readonlyattrspec_instantiation(instance):
    assert isinstance(instance, idl::ReadOnlyAttrSpec)

@given(instance=idl::AttrSpec_strategy)
@settings(max_examples=50)
def test_idl::attrspec_instantiation(instance):
    assert isinstance(instance, idl::AttrSpec)

@given(instance=idl::Preproc::Pragma::Component_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::component_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Component)

@given(instance=idl::Preproc::Pragma::Component_strategy)
def test_idl::preproc::pragma::component_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Component_strategy)
def test_idl::preproc::pragma::component_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Ndds_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::ndds_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Ndds)

@given(instance=idl::Preproc::Pragma::Ndds_strategy)
def test_idl::preproc::pragma::ndds_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Ndds_strategy)
def test_idl::preproc::pragma::ndds_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Idl_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::ciao::ami4ccm::idl_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Ciao::Ami4ccm::Idl)

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Idl_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::idl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Idl_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::idl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle)

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Receptacle_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::receptacle_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Interface_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::ciao::ami4ccm::interface_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Ciao::Ami4ccm::Interface)

@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Interface_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::interface_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Ciao::Ami4ccm::Interface_strategy)
def test_idl::preproc::pragma::ciao::ami4ccm::interface_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Ciao::Lem_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::ciao::lem_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Ciao::Lem)

@given(instance=idl::Preproc::Pragma::Ciao::Lem_strategy)
def test_idl::preproc::pragma::ciao::lem_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Ciao::Lem_strategy)
def test_idl::preproc::pragma::ciao::lem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::InterfaceBody_strategy)
@settings(max_examples=50)
def test_idl::interfacebody_instantiation(instance):
    assert isinstance(instance, idl::InterfaceBody)

@given(instance=idl::Interface::header_strategy)
@settings(max_examples=50)
def test_idl::interface::header_instantiation(instance):
    assert isinstance(instance, idl::Interface::header)

@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_isLocal_type(instance):
    assert isinstance(instance.isLocal, bool)


@given(instance=idl::Interface::header_strategy)
def test_idl::interface::header_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original

@given(instance=FixedDefinition_strategy)
@settings(max_examples=50)
def test_fixeddefinition_instantiation(instance):
    assert isinstance(instance, FixedDefinition)

@given(instance=TemplateDefinition_strategy)
@settings(max_examples=50)
def test_templatedefinition_instantiation(instance):
    assert isinstance(instance, TemplateDefinition)

@given(instance=idl::PortTypeDecl_strategy)
@settings(max_examples=50)
def test_idl::porttypedecl_instantiation(instance):
    assert isinstance(instance, idl::PortTypeDecl)

@given(instance=idl::PortTypeDecl_strategy)
def test_idl::porttypedecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::PortTypeDecl_strategy)
def test_idl::porttypedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::TypeDecl_strategy)
@settings(max_examples=50)
def test_idl::typedecl_instantiation(instance):
    assert isinstance(instance, idl::TypeDecl)

@given(instance=idl::ExceptDecl_strategy)
@settings(max_examples=50)
def test_idl::exceptdecl_instantiation(instance):
    assert isinstance(instance, idl::ExceptDecl)

@given(instance=idl::ExceptDecl_strategy)
def test_idl::exceptdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ExceptDecl_strategy)
def test_idl::exceptdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Event_strategy)
@settings(max_examples=50)
def test_idl::event_instantiation(instance):
    assert isinstance(instance, idl::Event)

@given(instance=idl::Event_strategy)
def test_idl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::Event_strategy)
def test_idl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Event_strategy)
def test_idl::event_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=idl::Event_strategy)
def test_idl::event_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=idl::HomeDecl_strategy)
@settings(max_examples=50)
def test_idl::homedecl_instantiation(instance):
    assert isinstance(instance, idl::HomeDecl)

@given(instance=idl::HomeDecl_strategy)
def test_idl::homedecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::HomeDecl_strategy)
def test_idl::homedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::FixedModule_strategy)
@settings(max_examples=50)
def test_idl::fixedmodule_instantiation(instance):
    assert isinstance(instance, idl::FixedModule)

@given(instance=idl::FixedModule_strategy)
def test_idl::fixedmodule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::FixedModule_strategy)
def test_idl::fixedmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::NativeType_strategy)
@settings(max_examples=50)
def test_idl::nativetype_instantiation(instance):
    assert isinstance(instance, idl::NativeType)

@given(instance=idl::NativeType_strategy)
def test_idl::nativetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::NativeType_strategy)
def test_idl::nativetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::ComponentDecl_strategy)
@settings(max_examples=50)
def test_idl::componentdecl_instantiation(instance):
    assert isinstance(instance, idl::ComponentDecl)

@given(instance=idl::ComponentDecl_strategy)
def test_idl::componentdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ComponentDecl_strategy)
def test_idl::componentdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::ConstDecl_strategy)
@settings(max_examples=50)
def test_idl::constdecl_instantiation(instance):
    assert isinstance(instance, idl::ConstDecl)

@given(instance=idl::ConstDecl_strategy)
def test_idl::constdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::ConstDecl_strategy)
def test_idl::constdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Connector_strategy)
@settings(max_examples=50)
def test_idl::connector_instantiation(instance):
    assert isinstance(instance, idl::Connector)

@given(instance=idl::TemplateModuleRef_strategy)
@settings(max_examples=50)
def test_idl::templatemoduleref_instantiation(instance):
    assert isinstance(instance, idl::TemplateModuleRef)

@given(instance=idl::TemplateModuleRef_strategy)
def test_idl::templatemoduleref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::TemplateModuleRef_strategy)
def test_idl::templatemoduleref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::TemplateModuleRef_strategy)
def test_idl::templatemoduleref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=idl::TemplateModuleRef_strategy)
def test_idl::templatemoduleref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Interface::or::Forward::Decl_strategy)
@settings(max_examples=50)
def test_interface::or::forward::decl_instantiation(instance):
    assert isinstance(instance, Interface::or::Forward::Decl)

@given(instance=idl::Forward::decl_strategy)
@settings(max_examples=50)
def test_idl::forward::decl_instantiation(instance):
    assert isinstance(instance, idl::Forward::decl)

@given(instance=idl::Forward::decl_strategy)
def test_idl::forward::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::Forward::decl_strategy)
def test_idl::forward::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Interface::decl_strategy)
@settings(max_examples=50)
def test_idl::interface::decl_instantiation(instance):
    assert isinstance(instance, idl::Interface::decl)

@given(instance=idl::Interface::or::Forward::Decl_strategy)
@settings(max_examples=50)
def test_idl::interface::or::forward::decl_instantiation(instance):
    assert isinstance(instance, idl::Interface::or::Forward::Decl)

@given(instance=idl::IDLComment_strategy)
@settings(max_examples=50)
def test_idl::idlcomment_instantiation(instance):
    assert isinstance(instance, idl::IDLComment)

@given(instance=idl::IDLComment_strategy)
def test_idl::idlcomment_body_type(instance):
    assert isinstance(instance.body, str)


@given(instance=idl::IDLComment_strategy)
def test_idl::idlcomment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=idl::Module_strategy)
@settings(max_examples=50)
def test_idl::module_instantiation(instance):
    assert isinstance(instance, idl::Module)

@given(instance=idl::Module_strategy)
def test_idl::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::Module_strategy)
def test_idl::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl::Excluded::File::Marker_strategy)
@settings(max_examples=50)
def test_idl::excluded::file::marker_instantiation(instance):
    assert isinstance(instance, idl::Excluded::File::Marker)

@given(instance=idl::Excluded::File::Marker_strategy)
def test_idl::excluded::file::marker_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=idl::Excluded::File::Marker_strategy)
def test_idl::excluded::file::marker_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=idl::File::Marker_strategy)
@settings(max_examples=50)
def test_idl::file::marker_instantiation(instance):
    assert isinstance(instance, idl::File::Marker)

@given(instance=idl::File::Marker_strategy)
def test_idl::file::marker_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=idl::File::Marker_strategy)
def test_idl::file::marker_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=idl::Preproc::Pragma::Misc_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::misc_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Misc)

@given(instance=idl::Preproc::Pragma::DDS4CCM::Impl_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::dds4ccm::impl_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::DDS4CCM::Impl)

@given(instance=idl::Preproc::Pragma::DDS4CCM::Impl_strategy)
def test_idl::preproc::pragma::dds4ccm::impl_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::DDS4CCM::Impl_strategy)
def test_idl::preproc::pragma::dds4ccm::impl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Pragma::Home_strategy)
@settings(max_examples=50)
def test_idl::preproc::pragma::home_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Pragma::Home)

@given(instance=idl::Preproc::Pragma::Home_strategy)
def test_idl::preproc::pragma::home_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Pragma::Home_strategy)
def test_idl::preproc::pragma::home_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Ifndef_strategy)
@settings(max_examples=50)
def test_idl::preproc::ifndef_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Ifndef)

@given(instance=idl::Preproc::Ifndef_strategy)
def test_idl::preproc::ifndef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Ifndef_strategy)
def test_idl::preproc::ifndef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::Preproc::Ifdef_strategy)
@settings(max_examples=50)
def test_idl::preproc::ifdef_instantiation(instance):
    assert isinstance(instance, idl::Preproc::Ifdef)

@given(instance=idl::Preproc::Ifdef_strategy)
def test_idl::preproc::ifdef_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=idl::Preproc::Ifdef_strategy)
def test_idl::preproc::ifdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl::FileName_strategy)
@settings(max_examples=50)
def test_idl::filename_instantiation(instance):
    assert isinstance(instance, idl::FileName)

@given(instance=idl::FileName_strategy)
def test_idl::filename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=idl::FileName_strategy)
def test_idl::filename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
