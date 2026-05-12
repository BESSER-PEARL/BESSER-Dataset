import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    idl_FormalParameterType,
    idl_TemplateDefinition,
    idl_FormalParameter,
    idl_ActualParameter,
    idl_FixedDefinition,
    idl_StateMember,
    Event,
    idl_EventDcl,
    idl_ConnectorExport,
    idl_ConnectorHeader,
    idl_PortExport,
    idl_EventForwardDcl,
    idl_HomeExport,
    idl_PrimaryKeySpec,
    idl_ComponentExport,
    idl_PrimaryExpr,
    ConstParamType,
    idl_ConstType,
    idl_UnaryExpr,
    idl_MultExpr,
    idl_AddExpr,
    idl_ShiftExpr,
    idl_AndExpr,
    idl_XOrExpr,
    ConstExp,
    idl_OrExpr,
    idl_ElementSpec,
    idl_CaseLabel,
    idl_Case,
    idl_SwitchBody,
    idl_SwitchTypeSpec,
    ConstrForwardDecl,
    idl_UnionForwardDecl,
    idl_StructForwardDecl,
    FormalParameterType,
    idl_TypenameParamType,
    idl_ConstParamType,
    idl_SequenceParamType,
    idl_EventParamType,
    idl_UnionParamType,
    idl_StructParamType,
    idl_InterfaceParamType,
    idl_EnumParamType,
    idl_ExceptionParamType,
    idl_ValuetypeParamType,
    idl_Declarator,
    idl_Member,
    TypeSpec,
    idl_ConstrTypeSpec,
    idl_SimpleTypeSpec,
    ActualParameter,
    idl_TypeSpec,
    ConstrTypeSpec,
    TypeDecl,
    idl_TypeDeclarator,
    idl_UnionType,
    idl_ConstrForwardDecl,
    ComplexDeclarator,
    idl_ComplexDeclarator,
    Declarator,
    idl_ArrayDeclarator,
    idl_SimpleDeclarator,
    PrimaryExpr,
    idl_Literal,
    ConstType,
    idl_FixedPtConstType,
    SwitchTypeSpec,
    idl_EnumType,
    SimpleTypeSpec,
    idl_TemplateTypeSpec,
    ParamTypeSpec,
    idl_BaseTypeSpec,
    OpTypeDecl,
    idl_ParamDcl,
    idl_PositiveIntConst,
    TemplateTypeSpec,
    idl_FixedPtType,
    idl_WideStringType,
    idl_SequenceType,
    idl_StringType,
    Preproc,
    idl_Preproc_Include,
    ComponentExport,
    idl_PublishesDcl,
    idl_EmitDcl,
    idl_ConsumesDcl,
    Export,
    Definition,
    idl_StructType,
    idl_TemplateModuleInst,
    idl_TemplateModule,
    idl_ComponentForwardDecl,
    idl_Preproc,
    idl_Definition,
    idl_Import_decl,
    idl_Specification,
    Preproc_Pragma,
    idl_Preproc_Pragma_Conn_Type,
    idl_Preproc_Pragma_Prefix,
    idl_Preproc_Pragma,
    idl_Preproc_Endif,
    idl_Preproc_Define,
    idl_Preproc_Error,
    idl_Preproc_Else,
    idl_ConstExp,
    idl_Preproc_If_Val,
    idl_Preproc_If_Compare,
    idl_Preproc_If,
    idl_Preproc_Undef,
    UnsignedInt,
    idl_UnsignedLongLongInt,
    idl_UnsignedLongInt,
    idl_UnsignedShortInt,
    SignedInt,
    idl_SignedLongLongInt,
    idl_SignedLongInt,
    idl_SignedShortInt,
    IntegerType,
    idl_UnsignedInt,
    idl_SignedInt,
    FloatingPtType,
    idl_LongDoubleType,
    idl_DoubleType,
    idl_FloatType,
    BaseTypeSpec,
    idl_OctetType,
    idl_IntegerType,
    idl_AnyType,
    idl_BooleanType,
    idl_WideCharType,
    idl_CharType,
    idl_ObjectType,
    idl_ValueBaseType,
    idl_FloatingPtType,
    idl_ParamTypeSpec,
    ConnectorExport,
    idl_PortDecl,
    PortExport,
    idl_ProvidesDcl,
    idl_UsesDcl,
    idl_AttrDecl,
    HomeExport,
    idl_FinderDcl,
    idl_FactoryDcl,
    idl_Export,
    idl_ScopedName,
    idl_ContextExpr,
    idl_ParameterDecls,
    idl_OpTypeDecl,
    idl_OpDecl,
    idl_ExceptionList,
    idl_AttrRaisesExpr,
    AttrDecl,
    idl_ReadOnlyAttrSpec,
    idl_AttrSpec,
    idl_Preproc_Pragma_Component,
    idl_Preproc_Pragma_Ndds,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Idl,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle,
    idl_Preproc_Pragma_Ciao_Ami4ccm_Interface,
    idl_Preproc_Pragma_Ciao_Lem,
    idl_InterfaceBody,
    idl_Interface_header,
    FixedDefinition,
    TemplateDefinition,
    idl_ConstDecl,
    idl_NativeType,
    idl_ComponentDecl,
    idl_Connector,
    idl_FixedModule,
    idl_TypeDecl,
    idl_TemplateModuleRef,
    idl_PortTypeDecl,
    idl_HomeDecl,
    idl_ExceptDecl,
    idl_Event,
    Interface_or_Forward_Decl,
    idl_Forward_decl,
    idl_Interface_decl,
    idl_Interface_or_Forward_Decl,
    idl_IDLComment,
    idl_Module,
    idl_Excluded_File_Marker,
    idl_File_Marker,
    idl_Preproc_Pragma_Misc,
    idl_Preproc_Pragma_DDS4CCM_Impl,
    idl_Preproc_Pragma_Home,
    idl_Preproc_Ifndef,
    idl_Preproc_Ifdef,
    idl_FileName,
    ParamDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idl_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(idl_FormalParameterType)


def test_idl_formalparametertype_constructor_exists():
    assert callable(idl_FormalParameterType.__init__)


def test_idl_formalparametertype_constructor_args():
    sig = inspect.signature(idl_FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_idl_templatedefinition_is_not_abstract():
    assert not inspect.isabstract(idl_TemplateDefinition)


def test_idl_templatedefinition_constructor_exists():
    assert callable(idl_TemplateDefinition.__init__)


def test_idl_templatedefinition_constructor_args():
    sig = inspect.signature(idl_TemplateDefinition.__init__)
    params = list(sig.parameters.keys())



def test_idl_formalparameter_is_not_abstract():
    assert not inspect.isabstract(idl_FormalParameter)


def test_idl_formalparameter_constructor_exists():
    assert callable(idl_FormalParameter.__init__)


def test_idl_formalparameter_constructor_args():
    sig = inspect.signature(idl_FormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_formalparameter_has_name():
    assert hasattr(idl_FormalParameter, "name")
    descriptor = None
    for klass in idl_FormalParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_actualparameter_is_not_abstract():
    assert not inspect.isabstract(idl_ActualParameter)


def test_idl_actualparameter_constructor_exists():
    assert callable(idl_ActualParameter.__init__)


def test_idl_actualparameter_constructor_args():
    sig = inspect.signature(idl_ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_idl_fixeddefinition_is_not_abstract():
    assert not inspect.isabstract(idl_FixedDefinition)


def test_idl_fixeddefinition_constructor_exists():
    assert callable(idl_FixedDefinition.__init__)


def test_idl_fixeddefinition_constructor_args():
    sig = inspect.signature(idl_FixedDefinition.__init__)
    params = list(sig.parameters.keys())



def test_idl_statemember_is_not_abstract():
    assert not inspect.isabstract(idl_StateMember)


def test_idl_statemember_constructor_exists():
    assert callable(idl_StateMember.__init__)


def test_idl_statemember_constructor_args():
    sig = inspect.signature(idl_StateMember.__init__)
    params = list(sig.parameters.keys())
    assert "isPublic" in params, "Missing parameter 'isPublic'"
    assert "names" in params, "Missing parameter 'names'"

def test_idl_statemember_has_isPublic():
    assert hasattr(idl_StateMember, "isPublic")
    descriptor = None
    for klass in idl_StateMember.__mro__:
        if "isPublic" in klass.__dict__:
            descriptor = klass.__dict__["isPublic"]
            break
    assert isinstance(descriptor, property)

def test_idl_statemember_has_names():
    assert hasattr(idl_StateMember, "names")
    descriptor = None
    for klass in idl_StateMember.__mro__:
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



def test_idl_eventdcl_is_not_abstract():
    assert not inspect.isabstract(idl_EventDcl)


def test_idl_eventdcl_constructor_exists():
    assert callable(idl_EventDcl.__init__)


def test_idl_eventdcl_constructor_args():
    sig = inspect.signature(idl_EventDcl.__init__)
    params = list(sig.parameters.keys())
    assert "isCustom" in params, "Missing parameter 'isCustom'"
    assert "isTruncatable" in params, "Missing parameter 'isTruncatable'"

def test_idl_eventdcl_has_isCustom():
    assert hasattr(idl_EventDcl, "isCustom")
    descriptor = None
    for klass in idl_EventDcl.__mro__:
        if "isCustom" in klass.__dict__:
            descriptor = klass.__dict__["isCustom"]
            break
    assert isinstance(descriptor, property)

def test_idl_eventdcl_has_isTruncatable():
    assert hasattr(idl_EventDcl, "isTruncatable")
    descriptor = None
    for klass in idl_EventDcl.__mro__:
        if "isTruncatable" in klass.__dict__:
            descriptor = klass.__dict__["isTruncatable"]
            break
    assert isinstance(descriptor, property)



def test_idl_connectorexport_is_not_abstract():
    assert not inspect.isabstract(idl_ConnectorExport)


def test_idl_connectorexport_constructor_exists():
    assert callable(idl_ConnectorExport.__init__)


def test_idl_connectorexport_constructor_args():
    sig = inspect.signature(idl_ConnectorExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_connectorheader_is_not_abstract():
    assert not inspect.isabstract(idl_ConnectorHeader)


def test_idl_connectorheader_constructor_exists():
    assert callable(idl_ConnectorHeader.__init__)


def test_idl_connectorheader_constructor_args():
    sig = inspect.signature(idl_ConnectorHeader.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_connectorheader_has_name():
    assert hasattr(idl_ConnectorHeader, "name")
    descriptor = None
    for klass in idl_ConnectorHeader.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_portexport_is_not_abstract():
    assert not inspect.isabstract(idl_PortExport)


def test_idl_portexport_constructor_exists():
    assert callable(idl_PortExport.__init__)


def test_idl_portexport_constructor_args():
    sig = inspect.signature(idl_PortExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_eventforwarddcl_is_not_abstract():
    assert not inspect.isabstract(idl_EventForwardDcl)


def test_idl_eventforwarddcl_constructor_exists():
    assert callable(idl_EventForwardDcl.__init__)


def test_idl_eventforwarddcl_constructor_args():
    sig = inspect.signature(idl_EventForwardDcl.__init__)
    params = list(sig.parameters.keys())



def test_idl_homeexport_is_not_abstract():
    assert not inspect.isabstract(idl_HomeExport)


def test_idl_homeexport_constructor_exists():
    assert callable(idl_HomeExport.__init__)


def test_idl_homeexport_constructor_args():
    sig = inspect.signature(idl_HomeExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_primarykeyspec_is_not_abstract():
    assert not inspect.isabstract(idl_PrimaryKeySpec)


def test_idl_primarykeyspec_constructor_exists():
    assert callable(idl_PrimaryKeySpec.__init__)


def test_idl_primarykeyspec_constructor_args():
    sig = inspect.signature(idl_PrimaryKeySpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_componentexport_is_not_abstract():
    assert not inspect.isabstract(idl_ComponentExport)


def test_idl_componentexport_constructor_exists():
    assert callable(idl_ComponentExport.__init__)


def test_idl_componentexport_constructor_args():
    sig = inspect.signature(idl_ComponentExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_primaryexpr_is_not_abstract():
    assert not inspect.isabstract(idl_PrimaryExpr)


def test_idl_primaryexpr_constructor_exists():
    assert callable(idl_PrimaryExpr.__init__)


def test_idl_primaryexpr_constructor_args():
    sig = inspect.signature(idl_PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_constparamtype_is_not_abstract():
    assert not inspect.isabstract(ConstParamType)


def test_constparamtype_constructor_exists():
    assert callable(ConstParamType.__init__)


def test_constparamtype_constructor_args():
    sig = inspect.signature(ConstParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_consttype_is_not_abstract():
    assert not inspect.isabstract(idl_ConstType)


def test_idl_consttype_constructor_exists():
    assert callable(idl_ConstType.__init__)


def test_idl_consttype_constructor_args():
    sig = inspect.signature(idl_ConstType.__init__)
    params = list(sig.parameters.keys())



def test_idl_unaryexpr_is_not_abstract():
    assert not inspect.isabstract(idl_UnaryExpr)


def test_idl_unaryexpr_constructor_exists():
    assert callable(idl_UnaryExpr.__init__)


def test_idl_unaryexpr_constructor_args():
    sig = inspect.signature(idl_UnaryExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_unaryexpr_has_op():
    assert hasattr(idl_UnaryExpr, "op")
    descriptor = None
    for klass in idl_UnaryExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_multexpr_is_not_abstract():
    assert not inspect.isabstract(idl_MultExpr)


def test_idl_multexpr_constructor_exists():
    assert callable(idl_MultExpr.__init__)


def test_idl_multexpr_constructor_args():
    sig = inspect.signature(idl_MultExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_multexpr_has_op():
    assert hasattr(idl_MultExpr, "op")
    descriptor = None
    for klass in idl_MultExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_addexpr_is_not_abstract():
    assert not inspect.isabstract(idl_AddExpr)


def test_idl_addexpr_constructor_exists():
    assert callable(idl_AddExpr.__init__)


def test_idl_addexpr_constructor_args():
    sig = inspect.signature(idl_AddExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_addexpr_has_op():
    assert hasattr(idl_AddExpr, "op")
    descriptor = None
    for klass in idl_AddExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_shiftexpr_is_not_abstract():
    assert not inspect.isabstract(idl_ShiftExpr)


def test_idl_shiftexpr_constructor_exists():
    assert callable(idl_ShiftExpr.__init__)


def test_idl_shiftexpr_constructor_args():
    sig = inspect.signature(idl_ShiftExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_shiftexpr_has_op():
    assert hasattr(idl_ShiftExpr, "op")
    descriptor = None
    for klass in idl_ShiftExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_andexpr_is_not_abstract():
    assert not inspect.isabstract(idl_AndExpr)


def test_idl_andexpr_constructor_exists():
    assert callable(idl_AndExpr.__init__)


def test_idl_andexpr_constructor_args():
    sig = inspect.signature(idl_AndExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_andexpr_has_op():
    assert hasattr(idl_AndExpr, "op")
    descriptor = None
    for klass in idl_AndExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_xorexpr_is_not_abstract():
    assert not inspect.isabstract(idl_XOrExpr)


def test_idl_xorexpr_constructor_exists():
    assert callable(idl_XOrExpr.__init__)


def test_idl_xorexpr_constructor_args():
    sig = inspect.signature(idl_XOrExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_xorexpr_has_op():
    assert hasattr(idl_XOrExpr, "op")
    descriptor = None
    for klass in idl_XOrExpr.__mro__:
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



def test_idl_orexpr_is_not_abstract():
    assert not inspect.isabstract(idl_OrExpr)


def test_idl_orexpr_constructor_exists():
    assert callable(idl_OrExpr.__init__)


def test_idl_orexpr_constructor_args():
    sig = inspect.signature(idl_OrExpr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_orexpr_has_op():
    assert hasattr(idl_OrExpr, "op")
    descriptor = None
    for klass in idl_OrExpr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_elementspec_is_not_abstract():
    assert not inspect.isabstract(idl_ElementSpec)


def test_idl_elementspec_constructor_exists():
    assert callable(idl_ElementSpec.__init__)


def test_idl_elementspec_constructor_args():
    sig = inspect.signature(idl_ElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_caselabel_is_not_abstract():
    assert not inspect.isabstract(idl_CaseLabel)


def test_idl_caselabel_constructor_exists():
    assert callable(idl_CaseLabel.__init__)


def test_idl_caselabel_constructor_args():
    sig = inspect.signature(idl_CaseLabel.__init__)
    params = list(sig.parameters.keys())
    assert "isDefault" in params, "Missing parameter 'isDefault'"
    assert "isCase" in params, "Missing parameter 'isCase'"

def test_idl_caselabel_has_isDefault():
    assert hasattr(idl_CaseLabel, "isDefault")
    descriptor = None
    for klass in idl_CaseLabel.__mro__:
        if "isDefault" in klass.__dict__:
            descriptor = klass.__dict__["isDefault"]
            break
    assert isinstance(descriptor, property)

def test_idl_caselabel_has_isCase():
    assert hasattr(idl_CaseLabel, "isCase")
    descriptor = None
    for klass in idl_CaseLabel.__mro__:
        if "isCase" in klass.__dict__:
            descriptor = klass.__dict__["isCase"]
            break
    assert isinstance(descriptor, property)



def test_idl_case_is_not_abstract():
    assert not inspect.isabstract(idl_Case)


def test_idl_case_constructor_exists():
    assert callable(idl_Case.__init__)


def test_idl_case_constructor_args():
    sig = inspect.signature(idl_Case.__init__)
    params = list(sig.parameters.keys())



def test_idl_switchbody_is_not_abstract():
    assert not inspect.isabstract(idl_SwitchBody)


def test_idl_switchbody_constructor_exists():
    assert callable(idl_SwitchBody.__init__)


def test_idl_switchbody_constructor_args():
    sig = inspect.signature(idl_SwitchBody.__init__)
    params = list(sig.parameters.keys())



def test_idl_switchtypespec_is_not_abstract():
    assert not inspect.isabstract(idl_SwitchTypeSpec)


def test_idl_switchtypespec_constructor_exists():
    assert callable(idl_SwitchTypeSpec.__init__)


def test_idl_switchtypespec_constructor_args():
    sig = inspect.signature(idl_SwitchTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_constrforwarddecl_is_not_abstract():
    assert not inspect.isabstract(ConstrForwardDecl)


def test_constrforwarddecl_constructor_exists():
    assert callable(ConstrForwardDecl.__init__)


def test_constrforwarddecl_constructor_args():
    sig = inspect.signature(ConstrForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_unionforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl_UnionForwardDecl)


def test_idl_unionforwarddecl_constructor_exists():
    assert callable(idl_UnionForwardDecl.__init__)


def test_idl_unionforwarddecl_constructor_args():
    sig = inspect.signature(idl_UnionForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_structforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl_StructForwardDecl)


def test_idl_structforwarddecl_constructor_exists():
    assert callable(idl_StructForwardDecl.__init__)


def test_idl_structforwarddecl_constructor_args():
    sig = inspect.signature(idl_StructForwardDecl.__init__)
    params = list(sig.parameters.keys())



def test_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(FormalParameterType)


def test_formalparametertype_constructor_exists():
    assert callable(FormalParameterType.__init__)


def test_formalparametertype_constructor_args():
    sig = inspect.signature(FormalParameterType.__init__)
    params = list(sig.parameters.keys())



def test_idl_typenameparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_TypenameParamType)


def test_idl_typenameparamtype_constructor_exists():
    assert callable(idl_TypenameParamType.__init__)


def test_idl_typenameparamtype_constructor_args():
    sig = inspect.signature(idl_TypenameParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_constparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_ConstParamType)


def test_idl_constparamtype_constructor_exists():
    assert callable(idl_ConstParamType.__init__)


def test_idl_constparamtype_constructor_args():
    sig = inspect.signature(idl_ConstParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_sequenceparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_SequenceParamType)


def test_idl_sequenceparamtype_constructor_exists():
    assert callable(idl_SequenceParamType.__init__)


def test_idl_sequenceparamtype_constructor_args():
    sig = inspect.signature(idl_SequenceParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_eventparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_EventParamType)


def test_idl_eventparamtype_constructor_exists():
    assert callable(idl_EventParamType.__init__)


def test_idl_eventparamtype_constructor_args():
    sig = inspect.signature(idl_EventParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_unionparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_UnionParamType)


def test_idl_unionparamtype_constructor_exists():
    assert callable(idl_UnionParamType.__init__)


def test_idl_unionparamtype_constructor_args():
    sig = inspect.signature(idl_UnionParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_structparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_StructParamType)


def test_idl_structparamtype_constructor_exists():
    assert callable(idl_StructParamType.__init__)


def test_idl_structparamtype_constructor_args():
    sig = inspect.signature(idl_StructParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_interfaceparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_InterfaceParamType)


def test_idl_interfaceparamtype_constructor_exists():
    assert callable(idl_InterfaceParamType.__init__)


def test_idl_interfaceparamtype_constructor_args():
    sig = inspect.signature(idl_InterfaceParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_enumparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_EnumParamType)


def test_idl_enumparamtype_constructor_exists():
    assert callable(idl_EnumParamType.__init__)


def test_idl_enumparamtype_constructor_args():
    sig = inspect.signature(idl_EnumParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_exceptionparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_ExceptionParamType)


def test_idl_exceptionparamtype_constructor_exists():
    assert callable(idl_ExceptionParamType.__init__)


def test_idl_exceptionparamtype_constructor_args():
    sig = inspect.signature(idl_ExceptionParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_valuetypeparamtype_is_not_abstract():
    assert not inspect.isabstract(idl_ValuetypeParamType)


def test_idl_valuetypeparamtype_constructor_exists():
    assert callable(idl_ValuetypeParamType.__init__)


def test_idl_valuetypeparamtype_constructor_args():
    sig = inspect.signature(idl_ValuetypeParamType.__init__)
    params = list(sig.parameters.keys())



def test_idl_declarator_is_not_abstract():
    assert not inspect.isabstract(idl_Declarator)


def test_idl_declarator_constructor_exists():
    assert callable(idl_Declarator.__init__)


def test_idl_declarator_constructor_args():
    sig = inspect.signature(idl_Declarator.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_idl_declarator_has_id():
    assert hasattr(idl_Declarator, "id")
    descriptor = None
    for klass in idl_Declarator.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_idl_member_is_not_abstract():
    assert not inspect.isabstract(idl_Member)


def test_idl_member_constructor_exists():
    assert callable(idl_Member.__init__)


def test_idl_member_constructor_args():
    sig = inspect.signature(idl_Member.__init__)
    params = list(sig.parameters.keys())



def test_typespec_is_not_abstract():
    assert not inspect.isabstract(TypeSpec)


def test_typespec_constructor_exists():
    assert callable(TypeSpec.__init__)


def test_typespec_constructor_args():
    sig = inspect.signature(TypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_constrtypespec_is_not_abstract():
    assert not inspect.isabstract(idl_ConstrTypeSpec)


def test_idl_constrtypespec_constructor_exists():
    assert callable(idl_ConstrTypeSpec.__init__)


def test_idl_constrtypespec_constructor_args():
    sig = inspect.signature(idl_ConstrTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_simpletypespec_is_not_abstract():
    assert not inspect.isabstract(idl_SimpleTypeSpec)


def test_idl_simpletypespec_constructor_exists():
    assert callable(idl_SimpleTypeSpec.__init__)


def test_idl_simpletypespec_constructor_args():
    sig = inspect.signature(idl_SimpleTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_actualparameter_is_not_abstract():
    assert not inspect.isabstract(ActualParameter)


def test_actualparameter_constructor_exists():
    assert callable(ActualParameter.__init__)


def test_actualparameter_constructor_args():
    sig = inspect.signature(ActualParameter.__init__)
    params = list(sig.parameters.keys())



def test_idl_typespec_is_not_abstract():
    assert not inspect.isabstract(idl_TypeSpec)


def test_idl_typespec_constructor_exists():
    assert callable(idl_TypeSpec.__init__)


def test_idl_typespec_constructor_args():
    sig = inspect.signature(idl_TypeSpec.__init__)
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



def test_idl_typedeclarator_is_not_abstract():
    assert not inspect.isabstract(idl_TypeDeclarator)


def test_idl_typedeclarator_constructor_exists():
    assert callable(idl_TypeDeclarator.__init__)


def test_idl_typedeclarator_constructor_args():
    sig = inspect.signature(idl_TypeDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_idl_uniontype_is_not_abstract():
    assert not inspect.isabstract(idl_UnionType)


def test_idl_uniontype_constructor_exists():
    assert callable(idl_UnionType.__init__)


def test_idl_uniontype_constructor_args():
    sig = inspect.signature(idl_UnionType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_uniontype_has_name():
    assert hasattr(idl_UnionType, "name")
    descriptor = None
    for klass in idl_UnionType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_constrforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl_ConstrForwardDecl)


def test_idl_constrforwarddecl_constructor_exists():
    assert callable(idl_ConstrForwardDecl.__init__)


def test_idl_constrforwarddecl_constructor_args():
    sig = inspect.signature(idl_ConstrForwardDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_constrforwarddecl_has_name():
    assert hasattr(idl_ConstrForwardDecl, "name")
    descriptor = None
    for klass in idl_ConstrForwardDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_complexdeclarator_is_not_abstract():
    assert not inspect.isabstract(ComplexDeclarator)


def test_complexdeclarator_constructor_exists():
    assert callable(ComplexDeclarator.__init__)


def test_complexdeclarator_constructor_args():
    sig = inspect.signature(ComplexDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_idl_complexdeclarator_is_not_abstract():
    assert not inspect.isabstract(idl_ComplexDeclarator)


def test_idl_complexdeclarator_constructor_exists():
    assert callable(idl_ComplexDeclarator.__init__)


def test_idl_complexdeclarator_constructor_args():
    sig = inspect.signature(idl_ComplexDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_declarator_is_not_abstract():
    assert not inspect.isabstract(Declarator)


def test_declarator_constructor_exists():
    assert callable(Declarator.__init__)


def test_declarator_constructor_args():
    sig = inspect.signature(Declarator.__init__)
    params = list(sig.parameters.keys())



def test_idl_arraydeclarator_is_not_abstract():
    assert not inspect.isabstract(idl_ArrayDeclarator)


def test_idl_arraydeclarator_constructor_exists():
    assert callable(idl_ArrayDeclarator.__init__)


def test_idl_arraydeclarator_constructor_args():
    sig = inspect.signature(idl_ArrayDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_idl_simpledeclarator_is_not_abstract():
    assert not inspect.isabstract(idl_SimpleDeclarator)


def test_idl_simpledeclarator_constructor_exists():
    assert callable(idl_SimpleDeclarator.__init__)


def test_idl_simpledeclarator_constructor_args():
    sig = inspect.signature(idl_SimpleDeclarator.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpr_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpr)


def test_primaryexpr_constructor_exists():
    assert callable(PrimaryExpr.__init__)


def test_primaryexpr_constructor_args():
    sig = inspect.signature(PrimaryExpr.__init__)
    params = list(sig.parameters.keys())



def test_idl_literal_is_not_abstract():
    assert not inspect.isabstract(idl_Literal)


def test_idl_literal_constructor_exists():
    assert callable(idl_Literal.__init__)


def test_idl_literal_constructor_args():
    sig = inspect.signature(idl_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_literal_has_value():
    assert hasattr(idl_Literal, "value")
    descriptor = None
    for klass in idl_Literal.__mro__:
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



def test_idl_fixedptconsttype_is_not_abstract():
    assert not inspect.isabstract(idl_FixedPtConstType)


def test_idl_fixedptconsttype_constructor_exists():
    assert callable(idl_FixedPtConstType.__init__)


def test_idl_fixedptconsttype_constructor_args():
    sig = inspect.signature(idl_FixedPtConstType.__init__)
    params = list(sig.parameters.keys())



def test_switchtypespec_is_not_abstract():
    assert not inspect.isabstract(SwitchTypeSpec)


def test_switchtypespec_constructor_exists():
    assert callable(SwitchTypeSpec.__init__)


def test_switchtypespec_constructor_args():
    sig = inspect.signature(SwitchTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_enumtype_is_not_abstract():
    assert not inspect.isabstract(idl_EnumType)


def test_idl_enumtype_constructor_exists():
    assert callable(idl_EnumType.__init__)


def test_idl_enumtype_constructor_args():
    sig = inspect.signature(idl_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl_enumtype_has_literal():
    assert hasattr(idl_EnumType, "literal")
    descriptor = None
    for klass in idl_EnumType.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)

def test_idl_enumtype_has_name():
    assert hasattr(idl_EnumType, "name")
    descriptor = None
    for klass in idl_EnumType.__mro__:
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



def test_idl_templatetypespec_is_not_abstract():
    assert not inspect.isabstract(idl_TemplateTypeSpec)


def test_idl_templatetypespec_constructor_exists():
    assert callable(idl_TemplateTypeSpec.__init__)


def test_idl_templatetypespec_constructor_args():
    sig = inspect.signature(idl_TemplateTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_paramtypespec_is_not_abstract():
    assert not inspect.isabstract(ParamTypeSpec)


def test_paramtypespec_constructor_exists():
    assert callable(ParamTypeSpec.__init__)


def test_paramtypespec_constructor_args():
    sig = inspect.signature(ParamTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_basetypespec_is_not_abstract():
    assert not inspect.isabstract(idl_BaseTypeSpec)


def test_idl_basetypespec_constructor_exists():
    assert callable(idl_BaseTypeSpec.__init__)


def test_idl_basetypespec_constructor_args():
    sig = inspect.signature(idl_BaseTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_optypedecl_is_not_abstract():
    assert not inspect.isabstract(OpTypeDecl)


def test_optypedecl_constructor_exists():
    assert callable(OpTypeDecl.__init__)


def test_optypedecl_constructor_args():
    sig = inspect.signature(OpTypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_paramdcl_is_not_abstract():
    assert not inspect.isabstract(idl_ParamDcl)


def test_idl_paramdcl_constructor_exists():
    assert callable(idl_ParamDcl.__init__)


def test_idl_paramdcl_constructor_args():
    sig = inspect.signature(idl_ParamDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_idl_paramdcl_has_name():
    assert hasattr(idl_ParamDcl, "name")
    descriptor = None
    for klass in idl_ParamDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl_paramdcl_has_direction():
    assert hasattr(idl_ParamDcl, "direction")
    descriptor = None
    for klass in idl_ParamDcl.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_idl_positiveintconst_is_not_abstract():
    assert not inspect.isabstract(idl_PositiveIntConst)


def test_idl_positiveintconst_constructor_exists():
    assert callable(idl_PositiveIntConst.__init__)


def test_idl_positiveintconst_constructor_args():
    sig = inspect.signature(idl_PositiveIntConst.__init__)
    params = list(sig.parameters.keys())



def test_templatetypespec_is_not_abstract():
    assert not inspect.isabstract(TemplateTypeSpec)


def test_templatetypespec_constructor_exists():
    assert callable(TemplateTypeSpec.__init__)


def test_templatetypespec_constructor_args():
    sig = inspect.signature(TemplateTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_fixedpttype_is_not_abstract():
    assert not inspect.isabstract(idl_FixedPtType)


def test_idl_fixedpttype_constructor_exists():
    assert callable(idl_FixedPtType.__init__)


def test_idl_fixedpttype_constructor_args():
    sig = inspect.signature(idl_FixedPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl_widestringtype_is_not_abstract():
    assert not inspect.isabstract(idl_WideStringType)


def test_idl_widestringtype_constructor_exists():
    assert callable(idl_WideStringType.__init__)


def test_idl_widestringtype_constructor_args():
    sig = inspect.signature(idl_WideStringType.__init__)
    params = list(sig.parameters.keys())



def test_idl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(idl_SequenceType)


def test_idl_sequencetype_constructor_exists():
    assert callable(idl_SequenceType.__init__)


def test_idl_sequencetype_constructor_args():
    sig = inspect.signature(idl_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_idl_stringtype_is_not_abstract():
    assert not inspect.isabstract(idl_StringType)


def test_idl_stringtype_constructor_exists():
    assert callable(idl_StringType.__init__)


def test_idl_stringtype_constructor_args():
    sig = inspect.signature(idl_StringType.__init__)
    params = list(sig.parameters.keys())



def test_preproc_is_not_abstract():
    assert not inspect.isabstract(Preproc)


def test_preproc_constructor_exists():
    assert callable(Preproc.__init__)


def test_preproc_constructor_args():
    sig = inspect.signature(Preproc.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_include_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Include)


def test_idl_preproc_include_constructor_exists():
    assert callable(idl_Preproc_Include.__init__)


def test_idl_preproc_include_constructor_args():
    sig = inspect.signature(idl_Preproc_Include.__init__)
    params = list(sig.parameters.keys())
    assert "strValue" in params, "Missing parameter 'strValue'"

def test_idl_preproc_include_has_strValue():
    assert hasattr(idl_Preproc_Include, "strValue")
    descriptor = None
    for klass in idl_Preproc_Include.__mro__:
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



def test_idl_publishesdcl_is_not_abstract():
    assert not inspect.isabstract(idl_PublishesDcl)


def test_idl_publishesdcl_constructor_exists():
    assert callable(idl_PublishesDcl.__init__)


def test_idl_publishesdcl_constructor_args():
    sig = inspect.signature(idl_PublishesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_publishesdcl_has_name():
    assert hasattr(idl_PublishesDcl, "name")
    descriptor = None
    for klass in idl_PublishesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_emitdcl_is_not_abstract():
    assert not inspect.isabstract(idl_EmitDcl)


def test_idl_emitdcl_constructor_exists():
    assert callable(idl_EmitDcl.__init__)


def test_idl_emitdcl_constructor_args():
    sig = inspect.signature(idl_EmitDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_emitdcl_has_name():
    assert hasattr(idl_EmitDcl, "name")
    descriptor = None
    for klass in idl_EmitDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_consumesdcl_is_not_abstract():
    assert not inspect.isabstract(idl_ConsumesDcl)


def test_idl_consumesdcl_constructor_exists():
    assert callable(idl_ConsumesDcl.__init__)


def test_idl_consumesdcl_constructor_args():
    sig = inspect.signature(idl_ConsumesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_consumesdcl_has_name():
    assert hasattr(idl_ConsumesDcl, "name")
    descriptor = None
    for klass in idl_ConsumesDcl.__mro__:
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



def test_idl_structtype_is_not_abstract():
    assert not inspect.isabstract(idl_StructType)


def test_idl_structtype_constructor_exists():
    assert callable(idl_StructType.__init__)


def test_idl_structtype_constructor_args():
    sig = inspect.signature(idl_StructType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_structtype_has_name():
    assert hasattr(idl_StructType, "name")
    descriptor = None
    for klass in idl_StructType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_templatemoduleinst_is_not_abstract():
    assert not inspect.isabstract(idl_TemplateModuleInst)


def test_idl_templatemoduleinst_constructor_exists():
    assert callable(idl_TemplateModuleInst.__init__)


def test_idl_templatemoduleinst_constructor_args():
    sig = inspect.signature(idl_TemplateModuleInst.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_templatemoduleinst_has_name():
    assert hasattr(idl_TemplateModuleInst, "name")
    descriptor = None
    for klass in idl_TemplateModuleInst.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_templatemodule_is_not_abstract():
    assert not inspect.isabstract(idl_TemplateModule)


def test_idl_templatemodule_constructor_exists():
    assert callable(idl_TemplateModule.__init__)


def test_idl_templatemodule_constructor_args():
    sig = inspect.signature(idl_TemplateModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_templatemodule_has_name():
    assert hasattr(idl_TemplateModule, "name")
    descriptor = None
    for klass in idl_TemplateModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_componentforwarddecl_is_not_abstract():
    assert not inspect.isabstract(idl_ComponentForwardDecl)


def test_idl_componentforwarddecl_constructor_exists():
    assert callable(idl_ComponentForwardDecl.__init__)


def test_idl_componentforwarddecl_constructor_args():
    sig = inspect.signature(idl_ComponentForwardDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_componentforwarddecl_has_name():
    assert hasattr(idl_ComponentForwardDecl, "name")
    descriptor = None
    for klass in idl_ComponentForwardDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc)


def test_idl_preproc_constructor_exists():
    assert callable(idl_Preproc.__init__)


def test_idl_preproc_constructor_args():
    sig = inspect.signature(idl_Preproc.__init__)
    params = list(sig.parameters.keys())



def test_idl_definition_is_not_abstract():
    assert not inspect.isabstract(idl_Definition)


def test_idl_definition_constructor_exists():
    assert callable(idl_Definition.__init__)


def test_idl_definition_constructor_args():
    sig = inspect.signature(idl_Definition.__init__)
    params = list(sig.parameters.keys())



def test_idl_import_decl_is_not_abstract():
    assert not inspect.isabstract(idl_Import_decl)


def test_idl_import_decl_constructor_exists():
    assert callable(idl_Import_decl.__init__)


def test_idl_import_decl_constructor_args():
    sig = inspect.signature(idl_Import_decl.__init__)
    params = list(sig.parameters.keys())
    assert "imported_scope" in params, "Missing parameter 'imported_scope'"

def test_idl_import_decl_has_imported_scope():
    assert hasattr(idl_Import_decl, "imported_scope")
    descriptor = None
    for klass in idl_Import_decl.__mro__:
        if "imported_scope" in klass.__dict__:
            descriptor = klass.__dict__["imported_scope"]
            break
    assert isinstance(descriptor, property)



def test_idl_specification_is_not_abstract():
    assert not inspect.isabstract(idl_Specification)


def test_idl_specification_constructor_exists():
    assert callable(idl_Specification.__init__)


def test_idl_specification_constructor_args():
    sig = inspect.signature(idl_Specification.__init__)
    params = list(sig.parameters.keys())



def test_preproc_pragma_is_not_abstract():
    assert not inspect.isabstract(Preproc_Pragma)


def test_preproc_pragma_constructor_exists():
    assert callable(Preproc_Pragma.__init__)


def test_preproc_pragma_constructor_args():
    sig = inspect.signature(Preproc_Pragma.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_pragma_conn_type_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Conn_Type)


def test_idl_preproc_pragma_conn_type_constructor_exists():
    assert callable(idl_Preproc_Pragma_Conn_Type.__init__)


def test_idl_preproc_pragma_conn_type_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Conn_Type.__init__)
    params = list(sig.parameters.keys())
    assert "valuePort" in params, "Missing parameter 'valuePort'"
    assert "valueConnType" in params, "Missing parameter 'valueConnType'"

def test_idl_preproc_pragma_conn_type_has_valuePort():
    assert hasattr(idl_Preproc_Pragma_Conn_Type, "valuePort")
    descriptor = None
    for klass in idl_Preproc_Pragma_Conn_Type.__mro__:
        if "valuePort" in klass.__dict__:
            descriptor = klass.__dict__["valuePort"]
            break
    assert isinstance(descriptor, property)

def test_idl_preproc_pragma_conn_type_has_valueConnType():
    assert hasattr(idl_Preproc_Pragma_Conn_Type, "valueConnType")
    descriptor = None
    for klass in idl_Preproc_Pragma_Conn_Type.__mro__:
        if "valueConnType" in klass.__dict__:
            descriptor = klass.__dict__["valueConnType"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_prefix_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Prefix)


def test_idl_preproc_pragma_prefix_constructor_exists():
    assert callable(idl_Preproc_Pragma_Prefix.__init__)


def test_idl_preproc_pragma_prefix_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Prefix.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_prefix_has_value():
    assert hasattr(idl_Preproc_Pragma_Prefix, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Prefix.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma)


def test_idl_preproc_pragma_constructor_exists():
    assert callable(idl_Preproc_Pragma.__init__)


def test_idl_preproc_pragma_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_endif_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Endif)


def test_idl_preproc_endif_constructor_exists():
    assert callable(idl_Preproc_Endif.__init__)


def test_idl_preproc_endif_constructor_args():
    sig = inspect.signature(idl_Preproc_Endif.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_define_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Define)


def test_idl_preproc_define_constructor_exists():
    assert callable(idl_Preproc_Define.__init__)


def test_idl_preproc_define_constructor_args():
    sig = inspect.signature(idl_Preproc_Define.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_define_has_value():
    assert hasattr(idl_Preproc_Define, "value")
    descriptor = None
    for klass in idl_Preproc_Define.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_error_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Error)


def test_idl_preproc_error_constructor_exists():
    assert callable(idl_Preproc_Error.__init__)


def test_idl_preproc_error_constructor_args():
    sig = inspect.signature(idl_Preproc_Error.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_error_has_value():
    assert hasattr(idl_Preproc_Error, "value")
    descriptor = None
    for klass in idl_Preproc_Error.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_else_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Else)


def test_idl_preproc_else_constructor_exists():
    assert callable(idl_Preproc_Else.__init__)


def test_idl_preproc_else_constructor_args():
    sig = inspect.signature(idl_Preproc_Else.__init__)
    params = list(sig.parameters.keys())



def test_idl_constexp_is_not_abstract():
    assert not inspect.isabstract(idl_ConstExp)


def test_idl_constexp_constructor_exists():
    assert callable(idl_ConstExp.__init__)


def test_idl_constexp_constructor_args():
    sig = inspect.signature(idl_ConstExp.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_if_val_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_If_Val)


def test_idl_preproc_if_val_constructor_exists():
    assert callable(idl_Preproc_If_Val.__init__)


def test_idl_preproc_if_val_constructor_args():
    sig = inspect.signature(idl_Preproc_If_Val.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_if_compare_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_If_Compare)


def test_idl_preproc_if_compare_constructor_exists():
    assert callable(idl_Preproc_If_Compare.__init__)


def test_idl_preproc_if_compare_constructor_args():
    sig = inspect.signature(idl_Preproc_If_Compare.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_idl_preproc_if_compare_has_op():
    assert hasattr(idl_Preproc_If_Compare, "op")
    descriptor = None
    for klass in idl_Preproc_If_Compare.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_if_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_If)


def test_idl_preproc_if_constructor_exists():
    assert callable(idl_Preproc_If.__init__)


def test_idl_preproc_if_constructor_args():
    sig = inspect.signature(idl_Preproc_If.__init__)
    params = list(sig.parameters.keys())
    assert "negation" in params, "Missing parameter 'negation'"

def test_idl_preproc_if_has_negation():
    assert hasattr(idl_Preproc_If, "negation")
    descriptor = None
    for klass in idl_Preproc_If.__mro__:
        if "negation" in klass.__dict__:
            descriptor = klass.__dict__["negation"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_undef_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Undef)


def test_idl_preproc_undef_constructor_exists():
    assert callable(idl_Preproc_Undef.__init__)


def test_idl_preproc_undef_constructor_args():
    sig = inspect.signature(idl_Preproc_Undef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_undef_has_value():
    assert hasattr(idl_Preproc_Undef, "value")
    descriptor = None
    for klass in idl_Preproc_Undef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_unsignedint_is_not_abstract():
    assert not inspect.isabstract(UnsignedInt)


def test_unsignedint_constructor_exists():
    assert callable(UnsignedInt.__init__)


def test_unsignedint_constructor_args():
    sig = inspect.signature(UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_unsignedlonglongint_is_not_abstract():
    assert not inspect.isabstract(idl_UnsignedLongLongInt)


def test_idl_unsignedlonglongint_constructor_exists():
    assert callable(idl_UnsignedLongLongInt.__init__)


def test_idl_unsignedlonglongint_constructor_args():
    sig = inspect.signature(idl_UnsignedLongLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_unsignedlongint_is_not_abstract():
    assert not inspect.isabstract(idl_UnsignedLongInt)


def test_idl_unsignedlongint_constructor_exists():
    assert callable(idl_UnsignedLongInt.__init__)


def test_idl_unsignedlongint_constructor_args():
    sig = inspect.signature(idl_UnsignedLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_unsignedshortint_is_not_abstract():
    assert not inspect.isabstract(idl_UnsignedShortInt)


def test_idl_unsignedshortint_constructor_exists():
    assert callable(idl_UnsignedShortInt.__init__)


def test_idl_unsignedshortint_constructor_args():
    sig = inspect.signature(idl_UnsignedShortInt.__init__)
    params = list(sig.parameters.keys())



def test_signedint_is_not_abstract():
    assert not inspect.isabstract(SignedInt)


def test_signedint_constructor_exists():
    assert callable(SignedInt.__init__)


def test_signedint_constructor_args():
    sig = inspect.signature(SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_signedlonglongint_is_not_abstract():
    assert not inspect.isabstract(idl_SignedLongLongInt)


def test_idl_signedlonglongint_constructor_exists():
    assert callable(idl_SignedLongLongInt.__init__)


def test_idl_signedlonglongint_constructor_args():
    sig = inspect.signature(idl_SignedLongLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_signedlongint_is_not_abstract():
    assert not inspect.isabstract(idl_SignedLongInt)


def test_idl_signedlongint_constructor_exists():
    assert callable(idl_SignedLongInt.__init__)


def test_idl_signedlongint_constructor_args():
    sig = inspect.signature(idl_SignedLongInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_signedshortint_is_not_abstract():
    assert not inspect.isabstract(idl_SignedShortInt)


def test_idl_signedshortint_constructor_exists():
    assert callable(idl_SignedShortInt.__init__)


def test_idl_signedshortint_constructor_args():
    sig = inspect.signature(idl_SignedShortInt.__init__)
    params = list(sig.parameters.keys())



def test_integertype_is_not_abstract():
    assert not inspect.isabstract(IntegerType)


def test_integertype_constructor_exists():
    assert callable(IntegerType.__init__)


def test_integertype_constructor_args():
    sig = inspect.signature(IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_idl_unsignedint_is_not_abstract():
    assert not inspect.isabstract(idl_UnsignedInt)


def test_idl_unsignedint_constructor_exists():
    assert callable(idl_UnsignedInt.__init__)


def test_idl_unsignedint_constructor_args():
    sig = inspect.signature(idl_UnsignedInt.__init__)
    params = list(sig.parameters.keys())



def test_idl_signedint_is_not_abstract():
    assert not inspect.isabstract(idl_SignedInt)


def test_idl_signedint_constructor_exists():
    assert callable(idl_SignedInt.__init__)


def test_idl_signedint_constructor_args():
    sig = inspect.signature(idl_SignedInt.__init__)
    params = list(sig.parameters.keys())



def test_floatingpttype_is_not_abstract():
    assert not inspect.isabstract(FloatingPtType)


def test_floatingpttype_constructor_exists():
    assert callable(FloatingPtType.__init__)


def test_floatingpttype_constructor_args():
    sig = inspect.signature(FloatingPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl_longdoubletype_is_not_abstract():
    assert not inspect.isabstract(idl_LongDoubleType)


def test_idl_longdoubletype_constructor_exists():
    assert callable(idl_LongDoubleType.__init__)


def test_idl_longdoubletype_constructor_args():
    sig = inspect.signature(idl_LongDoubleType.__init__)
    params = list(sig.parameters.keys())



def test_idl_doubletype_is_not_abstract():
    assert not inspect.isabstract(idl_DoubleType)


def test_idl_doubletype_constructor_exists():
    assert callable(idl_DoubleType.__init__)


def test_idl_doubletype_constructor_args():
    sig = inspect.signature(idl_DoubleType.__init__)
    params = list(sig.parameters.keys())



def test_idl_floattype_is_not_abstract():
    assert not inspect.isabstract(idl_FloatType)


def test_idl_floattype_constructor_exists():
    assert callable(idl_FloatType.__init__)


def test_idl_floattype_constructor_args():
    sig = inspect.signature(idl_FloatType.__init__)
    params = list(sig.parameters.keys())



def test_basetypespec_is_not_abstract():
    assert not inspect.isabstract(BaseTypeSpec)


def test_basetypespec_constructor_exists():
    assert callable(BaseTypeSpec.__init__)


def test_basetypespec_constructor_args():
    sig = inspect.signature(BaseTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_octettype_is_not_abstract():
    assert not inspect.isabstract(idl_OctetType)


def test_idl_octettype_constructor_exists():
    assert callable(idl_OctetType.__init__)


def test_idl_octettype_constructor_args():
    sig = inspect.signature(idl_OctetType.__init__)
    params = list(sig.parameters.keys())



def test_idl_integertype_is_not_abstract():
    assert not inspect.isabstract(idl_IntegerType)


def test_idl_integertype_constructor_exists():
    assert callable(idl_IntegerType.__init__)


def test_idl_integertype_constructor_args():
    sig = inspect.signature(idl_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_idl_anytype_is_not_abstract():
    assert not inspect.isabstract(idl_AnyType)


def test_idl_anytype_constructor_exists():
    assert callable(idl_AnyType.__init__)


def test_idl_anytype_constructor_args():
    sig = inspect.signature(idl_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_idl_booleantype_is_not_abstract():
    assert not inspect.isabstract(idl_BooleanType)


def test_idl_booleantype_constructor_exists():
    assert callable(idl_BooleanType.__init__)


def test_idl_booleantype_constructor_args():
    sig = inspect.signature(idl_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_idl_widechartype_is_not_abstract():
    assert not inspect.isabstract(idl_WideCharType)


def test_idl_widechartype_constructor_exists():
    assert callable(idl_WideCharType.__init__)


def test_idl_widechartype_constructor_args():
    sig = inspect.signature(idl_WideCharType.__init__)
    params = list(sig.parameters.keys())



def test_idl_chartype_is_not_abstract():
    assert not inspect.isabstract(idl_CharType)


def test_idl_chartype_constructor_exists():
    assert callable(idl_CharType.__init__)


def test_idl_chartype_constructor_args():
    sig = inspect.signature(idl_CharType.__init__)
    params = list(sig.parameters.keys())



def test_idl_objecttype_is_not_abstract():
    assert not inspect.isabstract(idl_ObjectType)


def test_idl_objecttype_constructor_exists():
    assert callable(idl_ObjectType.__init__)


def test_idl_objecttype_constructor_args():
    sig = inspect.signature(idl_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_idl_valuebasetype_is_not_abstract():
    assert not inspect.isabstract(idl_ValueBaseType)


def test_idl_valuebasetype_constructor_exists():
    assert callable(idl_ValueBaseType.__init__)


def test_idl_valuebasetype_constructor_args():
    sig = inspect.signature(idl_ValueBaseType.__init__)
    params = list(sig.parameters.keys())



def test_idl_floatingpttype_is_not_abstract():
    assert not inspect.isabstract(idl_FloatingPtType)


def test_idl_floatingpttype_constructor_exists():
    assert callable(idl_FloatingPtType.__init__)


def test_idl_floatingpttype_constructor_args():
    sig = inspect.signature(idl_FloatingPtType.__init__)
    params = list(sig.parameters.keys())



def test_idl_paramtypespec_is_not_abstract():
    assert not inspect.isabstract(idl_ParamTypeSpec)


def test_idl_paramtypespec_constructor_exists():
    assert callable(idl_ParamTypeSpec.__init__)


def test_idl_paramtypespec_constructor_args():
    sig = inspect.signature(idl_ParamTypeSpec.__init__)
    params = list(sig.parameters.keys())



def test_connectorexport_is_not_abstract():
    assert not inspect.isabstract(ConnectorExport)


def test_connectorexport_constructor_exists():
    assert callable(ConnectorExport.__init__)


def test_connectorexport_constructor_args():
    sig = inspect.signature(ConnectorExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_portdecl_is_not_abstract():
    assert not inspect.isabstract(idl_PortDecl)


def test_idl_portdecl_constructor_exists():
    assert callable(idl_PortDecl.__init__)


def test_idl_portdecl_constructor_args():
    sig = inspect.signature(idl_PortDecl.__init__)
    params = list(sig.parameters.keys())
    assert "isMirror" in params, "Missing parameter 'isMirror'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl_portdecl_has_isMirror():
    assert hasattr(idl_PortDecl, "isMirror")
    descriptor = None
    for klass in idl_PortDecl.__mro__:
        if "isMirror" in klass.__dict__:
            descriptor = klass.__dict__["isMirror"]
            break
    assert isinstance(descriptor, property)

def test_idl_portdecl_has_name():
    assert hasattr(idl_PortDecl, "name")
    descriptor = None
    for klass in idl_PortDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_portexport_is_not_abstract():
    assert not inspect.isabstract(PortExport)


def test_portexport_constructor_exists():
    assert callable(PortExport.__init__)


def test_portexport_constructor_args():
    sig = inspect.signature(PortExport.__init__)
    params = list(sig.parameters.keys())



def test_idl_providesdcl_is_not_abstract():
    assert not inspect.isabstract(idl_ProvidesDcl)


def test_idl_providesdcl_constructor_exists():
    assert callable(idl_ProvidesDcl.__init__)


def test_idl_providesdcl_constructor_args():
    sig = inspect.signature(idl_ProvidesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_providesdcl_has_name():
    assert hasattr(idl_ProvidesDcl, "name")
    descriptor = None
    for klass in idl_ProvidesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_usesdcl_is_not_abstract():
    assert not inspect.isabstract(idl_UsesDcl)


def test_idl_usesdcl_constructor_exists():
    assert callable(idl_UsesDcl.__init__)


def test_idl_usesdcl_constructor_args():
    sig = inspect.signature(idl_UsesDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isMultiple" in params, "Missing parameter 'isMultiple'"

def test_idl_usesdcl_has_name():
    assert hasattr(idl_UsesDcl, "name")
    descriptor = None
    for klass in idl_UsesDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl_usesdcl_has_isMultiple():
    assert hasattr(idl_UsesDcl, "isMultiple")
    descriptor = None
    for klass in idl_UsesDcl.__mro__:
        if "isMultiple" in klass.__dict__:
            descriptor = klass.__dict__["isMultiple"]
            break
    assert isinstance(descriptor, property)



def test_idl_attrdecl_is_not_abstract():
    assert not inspect.isabstract(idl_AttrDecl)


def test_idl_attrdecl_constructor_exists():
    assert callable(idl_AttrDecl.__init__)


def test_idl_attrdecl_constructor_args():
    sig = inspect.signature(idl_AttrDecl.__init__)
    params = list(sig.parameters.keys())
    assert "names" in params, "Missing parameter 'names'"

def test_idl_attrdecl_has_names():
    assert hasattr(idl_AttrDecl, "names")
    descriptor = None
    for klass in idl_AttrDecl.__mro__:
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



def test_idl_finderdcl_is_not_abstract():
    assert not inspect.isabstract(idl_FinderDcl)


def test_idl_finderdcl_constructor_exists():
    assert callable(idl_FinderDcl.__init__)


def test_idl_finderdcl_constructor_args():
    sig = inspect.signature(idl_FinderDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_finderdcl_has_name():
    assert hasattr(idl_FinderDcl, "name")
    descriptor = None
    for klass in idl_FinderDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_factorydcl_is_not_abstract():
    assert not inspect.isabstract(idl_FactoryDcl)


def test_idl_factorydcl_constructor_exists():
    assert callable(idl_FactoryDcl.__init__)


def test_idl_factorydcl_constructor_args():
    sig = inspect.signature(idl_FactoryDcl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_factorydcl_has_name():
    assert hasattr(idl_FactoryDcl, "name")
    descriptor = None
    for klass in idl_FactoryDcl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_export_is_not_abstract():
    assert not inspect.isabstract(idl_Export)


def test_idl_export_constructor_exists():
    assert callable(idl_Export.__init__)


def test_idl_export_constructor_args():
    sig = inspect.signature(idl_Export.__init__)
    params = list(sig.parameters.keys())



def test_idl_scopedname_is_not_abstract():
    assert not inspect.isabstract(idl_ScopedName)


def test_idl_scopedname_constructor_exists():
    assert callable(idl_ScopedName.__init__)


def test_idl_scopedname_constructor_args():
    sig = inspect.signature(idl_ScopedName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_scopedname_has_name():
    assert hasattr(idl_ScopedName, "name")
    descriptor = None
    for klass in idl_ScopedName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_contextexpr_is_not_abstract():
    assert not inspect.isabstract(idl_ContextExpr)


def test_idl_contextexpr_constructor_exists():
    assert callable(idl_ContextExpr.__init__)


def test_idl_contextexpr_constructor_args():
    sig = inspect.signature(idl_ContextExpr.__init__)
    params = list(sig.parameters.keys())
    assert "literal" in params, "Missing parameter 'literal'"

def test_idl_contextexpr_has_literal():
    assert hasattr(idl_ContextExpr, "literal")
    descriptor = None
    for klass in idl_ContextExpr.__mro__:
        if "literal" in klass.__dict__:
            descriptor = klass.__dict__["literal"]
            break
    assert isinstance(descriptor, property)



def test_idl_parameterdecls_is_not_abstract():
    assert not inspect.isabstract(idl_ParameterDecls)


def test_idl_parameterdecls_constructor_exists():
    assert callable(idl_ParameterDecls.__init__)


def test_idl_parameterdecls_constructor_args():
    sig = inspect.signature(idl_ParameterDecls.__init__)
    params = list(sig.parameters.keys())



def test_idl_optypedecl_is_not_abstract():
    assert not inspect.isabstract(idl_OpTypeDecl)


def test_idl_optypedecl_constructor_exists():
    assert callable(idl_OpTypeDecl.__init__)


def test_idl_optypedecl_constructor_args():
    sig = inspect.signature(idl_OpTypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_opdecl_is_not_abstract():
    assert not inspect.isabstract(idl_OpDecl)


def test_idl_opdecl_constructor_exists():
    assert callable(idl_OpDecl.__init__)


def test_idl_opdecl_constructor_args():
    sig = inspect.signature(idl_OpDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isOneway" in params, "Missing parameter 'isOneway'"

def test_idl_opdecl_has_name():
    assert hasattr(idl_OpDecl, "name")
    descriptor = None
    for klass in idl_OpDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl_opdecl_has_isOneway():
    assert hasattr(idl_OpDecl, "isOneway")
    descriptor = None
    for klass in idl_OpDecl.__mro__:
        if "isOneway" in klass.__dict__:
            descriptor = klass.__dict__["isOneway"]
            break
    assert isinstance(descriptor, property)



def test_idl_exceptionlist_is_not_abstract():
    assert not inspect.isabstract(idl_ExceptionList)


def test_idl_exceptionlist_constructor_exists():
    assert callable(idl_ExceptionList.__init__)


def test_idl_exceptionlist_constructor_args():
    sig = inspect.signature(idl_ExceptionList.__init__)
    params = list(sig.parameters.keys())



def test_idl_attrraisesexpr_is_not_abstract():
    assert not inspect.isabstract(idl_AttrRaisesExpr)


def test_idl_attrraisesexpr_constructor_exists():
    assert callable(idl_AttrRaisesExpr.__init__)


def test_idl_attrraisesexpr_constructor_args():
    sig = inspect.signature(idl_AttrRaisesExpr.__init__)
    params = list(sig.parameters.keys())



def test_attrdecl_is_not_abstract():
    assert not inspect.isabstract(AttrDecl)


def test_attrdecl_constructor_exists():
    assert callable(AttrDecl.__init__)


def test_attrdecl_constructor_args():
    sig = inspect.signature(AttrDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_readonlyattrspec_is_not_abstract():
    assert not inspect.isabstract(idl_ReadOnlyAttrSpec)


def test_idl_readonlyattrspec_constructor_exists():
    assert callable(idl_ReadOnlyAttrSpec.__init__)


def test_idl_readonlyattrspec_constructor_args():
    sig = inspect.signature(idl_ReadOnlyAttrSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_attrspec_is_not_abstract():
    assert not inspect.isabstract(idl_AttrSpec)


def test_idl_attrspec_constructor_exists():
    assert callable(idl_AttrSpec.__init__)


def test_idl_attrspec_constructor_args():
    sig = inspect.signature(idl_AttrSpec.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_pragma_component_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Component)


def test_idl_preproc_pragma_component_constructor_exists():
    assert callable(idl_Preproc_Pragma_Component.__init__)


def test_idl_preproc_pragma_component_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Component.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_component_has_value():
    assert hasattr(idl_Preproc_Pragma_Component, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Component.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_ndds_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Ndds)


def test_idl_preproc_pragma_ndds_constructor_exists():
    assert callable(idl_Preproc_Pragma_Ndds.__init__)


def test_idl_preproc_pragma_ndds_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Ndds.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_ndds_has_value():
    assert hasattr(idl_Preproc_Pragma_Ndds, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Ndds.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_ciao_ami4ccm_idl_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Ciao_Ami4ccm_Idl)


def test_idl_preproc_pragma_ciao_ami4ccm_idl_constructor_exists():
    assert callable(idl_Preproc_Pragma_Ciao_Ami4ccm_Idl.__init__)


def test_idl_preproc_pragma_ciao_ami4ccm_idl_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Ciao_Ami4ccm_Idl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_ciao_ami4ccm_idl_has_value():
    assert hasattr(idl_Preproc_Pragma_Ciao_Ami4ccm_Idl, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Ciao_Ami4ccm_Idl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle)


def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_constructor_exists():
    assert callable(idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle.__init__)


def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_has_value():
    assert hasattr(idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_ciao_ami4ccm_interface_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Ciao_Ami4ccm_Interface)


def test_idl_preproc_pragma_ciao_ami4ccm_interface_constructor_exists():
    assert callable(idl_Preproc_Pragma_Ciao_Ami4ccm_Interface.__init__)


def test_idl_preproc_pragma_ciao_ami4ccm_interface_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Ciao_Ami4ccm_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_ciao_ami4ccm_interface_has_value():
    assert hasattr(idl_Preproc_Pragma_Ciao_Ami4ccm_Interface, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Ciao_Ami4ccm_Interface.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_ciao_lem_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Ciao_Lem)


def test_idl_preproc_pragma_ciao_lem_constructor_exists():
    assert callable(idl_Preproc_Pragma_Ciao_Lem.__init__)


def test_idl_preproc_pragma_ciao_lem_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Ciao_Lem.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_ciao_lem_has_value():
    assert hasattr(idl_Preproc_Pragma_Ciao_Lem, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Ciao_Lem.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_interfacebody_is_not_abstract():
    assert not inspect.isabstract(idl_InterfaceBody)


def test_idl_interfacebody_constructor_exists():
    assert callable(idl_InterfaceBody.__init__)


def test_idl_interfacebody_constructor_args():
    sig = inspect.signature(idl_InterfaceBody.__init__)
    params = list(sig.parameters.keys())



def test_idl_interface_header_is_not_abstract():
    assert not inspect.isabstract(idl_Interface_header)


def test_idl_interface_header_constructor_exists():
    assert callable(idl_Interface_header.__init__)


def test_idl_interface_header_constructor_args():
    sig = inspect.signature(idl_Interface_header.__init__)
    params = list(sig.parameters.keys())
    assert "isLocal" in params, "Missing parameter 'isLocal'"
    assert "name" in params, "Missing parameter 'name'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_idl_interface_header_has_isLocal():
    assert hasattr(idl_Interface_header, "isLocal")
    descriptor = None
    for klass in idl_Interface_header.__mro__:
        if "isLocal" in klass.__dict__:
            descriptor = klass.__dict__["isLocal"]
            break
    assert isinstance(descriptor, property)

def test_idl_interface_header_has_name():
    assert hasattr(idl_Interface_header, "name")
    descriptor = None
    for klass in idl_Interface_header.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_idl_interface_header_has_isAbstract():
    assert hasattr(idl_Interface_header, "isAbstract")
    descriptor = None
    for klass in idl_Interface_header.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
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



def test_idl_constdecl_is_not_abstract():
    assert not inspect.isabstract(idl_ConstDecl)


def test_idl_constdecl_constructor_exists():
    assert callable(idl_ConstDecl.__init__)


def test_idl_constdecl_constructor_args():
    sig = inspect.signature(idl_ConstDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_constdecl_has_name():
    assert hasattr(idl_ConstDecl, "name")
    descriptor = None
    for klass in idl_ConstDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_nativetype_is_not_abstract():
    assert not inspect.isabstract(idl_NativeType)


def test_idl_nativetype_constructor_exists():
    assert callable(idl_NativeType.__init__)


def test_idl_nativetype_constructor_args():
    sig = inspect.signature(idl_NativeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_nativetype_has_name():
    assert hasattr(idl_NativeType, "name")
    descriptor = None
    for klass in idl_NativeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_componentdecl_is_not_abstract():
    assert not inspect.isabstract(idl_ComponentDecl)


def test_idl_componentdecl_constructor_exists():
    assert callable(idl_ComponentDecl.__init__)


def test_idl_componentdecl_constructor_args():
    sig = inspect.signature(idl_ComponentDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_componentdecl_has_name():
    assert hasattr(idl_ComponentDecl, "name")
    descriptor = None
    for klass in idl_ComponentDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_connector_is_not_abstract():
    assert not inspect.isabstract(idl_Connector)


def test_idl_connector_constructor_exists():
    assert callable(idl_Connector.__init__)


def test_idl_connector_constructor_args():
    sig = inspect.signature(idl_Connector.__init__)
    params = list(sig.parameters.keys())



def test_idl_fixedmodule_is_not_abstract():
    assert not inspect.isabstract(idl_FixedModule)


def test_idl_fixedmodule_constructor_exists():
    assert callable(idl_FixedModule.__init__)


def test_idl_fixedmodule_constructor_args():
    sig = inspect.signature(idl_FixedModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_fixedmodule_has_name():
    assert hasattr(idl_FixedModule, "name")
    descriptor = None
    for klass in idl_FixedModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_typedecl_is_not_abstract():
    assert not inspect.isabstract(idl_TypeDecl)


def test_idl_typedecl_constructor_exists():
    assert callable(idl_TypeDecl.__init__)


def test_idl_typedecl_constructor_args():
    sig = inspect.signature(idl_TypeDecl.__init__)
    params = list(sig.parameters.keys())



def test_idl_templatemoduleref_is_not_abstract():
    assert not inspect.isabstract(idl_TemplateModuleRef)


def test_idl_templatemoduleref_constructor_exists():
    assert callable(idl_TemplateModuleRef.__init__)


def test_idl_templatemoduleref_constructor_args():
    sig = inspect.signature(idl_TemplateModuleRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl_templatemoduleref_has_id():
    assert hasattr(idl_TemplateModuleRef, "id")
    descriptor = None
    for klass in idl_TemplateModuleRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_idl_templatemoduleref_has_name():
    assert hasattr(idl_TemplateModuleRef, "name")
    descriptor = None
    for klass in idl_TemplateModuleRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_porttypedecl_is_not_abstract():
    assert not inspect.isabstract(idl_PortTypeDecl)


def test_idl_porttypedecl_constructor_exists():
    assert callable(idl_PortTypeDecl.__init__)


def test_idl_porttypedecl_constructor_args():
    sig = inspect.signature(idl_PortTypeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_porttypedecl_has_name():
    assert hasattr(idl_PortTypeDecl, "name")
    descriptor = None
    for klass in idl_PortTypeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_homedecl_is_not_abstract():
    assert not inspect.isabstract(idl_HomeDecl)


def test_idl_homedecl_constructor_exists():
    assert callable(idl_HomeDecl.__init__)


def test_idl_homedecl_constructor_args():
    sig = inspect.signature(idl_HomeDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_homedecl_has_name():
    assert hasattr(idl_HomeDecl, "name")
    descriptor = None
    for klass in idl_HomeDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_exceptdecl_is_not_abstract():
    assert not inspect.isabstract(idl_ExceptDecl)


def test_idl_exceptdecl_constructor_exists():
    assert callable(idl_ExceptDecl.__init__)


def test_idl_exceptdecl_constructor_args():
    sig = inspect.signature(idl_ExceptDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_exceptdecl_has_name():
    assert hasattr(idl_ExceptDecl, "name")
    descriptor = None
    for klass in idl_ExceptDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_event_is_not_abstract():
    assert not inspect.isabstract(idl_Event)


def test_idl_event_constructor_exists():
    assert callable(idl_Event.__init__)


def test_idl_event_constructor_args():
    sig = inspect.signature(idl_Event.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_idl_event_has_isAbstract():
    assert hasattr(idl_Event, "isAbstract")
    descriptor = None
    for klass in idl_Event.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_idl_event_has_name():
    assert hasattr(idl_Event, "name")
    descriptor = None
    for klass in idl_Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_interface_or_forward_decl_is_not_abstract():
    assert not inspect.isabstract(Interface_or_Forward_Decl)


def test_interface_or_forward_decl_constructor_exists():
    assert callable(Interface_or_Forward_Decl.__init__)


def test_interface_or_forward_decl_constructor_args():
    sig = inspect.signature(Interface_or_Forward_Decl.__init__)
    params = list(sig.parameters.keys())



def test_idl_forward_decl_is_not_abstract():
    assert not inspect.isabstract(idl_Forward_decl)


def test_idl_forward_decl_constructor_exists():
    assert callable(idl_Forward_decl.__init__)


def test_idl_forward_decl_constructor_args():
    sig = inspect.signature(idl_Forward_decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_forward_decl_has_name():
    assert hasattr(idl_Forward_decl, "name")
    descriptor = None
    for klass in idl_Forward_decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_interface_decl_is_not_abstract():
    assert not inspect.isabstract(idl_Interface_decl)


def test_idl_interface_decl_constructor_exists():
    assert callable(idl_Interface_decl.__init__)


def test_idl_interface_decl_constructor_args():
    sig = inspect.signature(idl_Interface_decl.__init__)
    params = list(sig.parameters.keys())



def test_idl_interface_or_forward_decl_is_not_abstract():
    assert not inspect.isabstract(idl_Interface_or_Forward_Decl)


def test_idl_interface_or_forward_decl_constructor_exists():
    assert callable(idl_Interface_or_Forward_Decl.__init__)


def test_idl_interface_or_forward_decl_constructor_args():
    sig = inspect.signature(idl_Interface_or_Forward_Decl.__init__)
    params = list(sig.parameters.keys())



def test_idl_idlcomment_is_not_abstract():
    assert not inspect.isabstract(idl_IDLComment)


def test_idl_idlcomment_constructor_exists():
    assert callable(idl_IDLComment.__init__)


def test_idl_idlcomment_constructor_args():
    sig = inspect.signature(idl_IDLComment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"

def test_idl_idlcomment_has_body():
    assert hasattr(idl_IDLComment, "body")
    descriptor = None
    for klass in idl_IDLComment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_idl_module_is_not_abstract():
    assert not inspect.isabstract(idl_Module)


def test_idl_module_constructor_exists():
    assert callable(idl_Module.__init__)


def test_idl_module_constructor_args():
    sig = inspect.signature(idl_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_module_has_name():
    assert hasattr(idl_Module, "name")
    descriptor = None
    for klass in idl_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_idl_excluded_file_marker_is_not_abstract():
    assert not inspect.isabstract(idl_Excluded_File_Marker)


def test_idl_excluded_file_marker_constructor_exists():
    assert callable(idl_Excluded_File_Marker.__init__)


def test_idl_excluded_file_marker_constructor_args():
    sig = inspect.signature(idl_Excluded_File_Marker.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_idl_excluded_file_marker_has_file():
    assert hasattr(idl_Excluded_File_Marker, "file")
    descriptor = None
    for klass in idl_Excluded_File_Marker.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_idl_file_marker_is_not_abstract():
    assert not inspect.isabstract(idl_File_Marker)


def test_idl_file_marker_constructor_exists():
    assert callable(idl_File_Marker.__init__)


def test_idl_file_marker_constructor_args():
    sig = inspect.signature(idl_File_Marker.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_idl_file_marker_has_file():
    assert hasattr(idl_File_Marker, "file")
    descriptor = None
    for klass in idl_File_Marker.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_misc_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Misc)


def test_idl_preproc_pragma_misc_constructor_exists():
    assert callable(idl_Preproc_Pragma_Misc.__init__)


def test_idl_preproc_pragma_misc_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Misc.__init__)
    params = list(sig.parameters.keys())



def test_idl_preproc_pragma_dds4ccm_impl_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_DDS4CCM_Impl)


def test_idl_preproc_pragma_dds4ccm_impl_constructor_exists():
    assert callable(idl_Preproc_Pragma_DDS4CCM_Impl.__init__)


def test_idl_preproc_pragma_dds4ccm_impl_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_DDS4CCM_Impl.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_dds4ccm_impl_has_value():
    assert hasattr(idl_Preproc_Pragma_DDS4CCM_Impl, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_DDS4CCM_Impl.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_pragma_home_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Pragma_Home)


def test_idl_preproc_pragma_home_constructor_exists():
    assert callable(idl_Preproc_Pragma_Home.__init__)


def test_idl_preproc_pragma_home_constructor_args():
    sig = inspect.signature(idl_Preproc_Pragma_Home.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_pragma_home_has_value():
    assert hasattr(idl_Preproc_Pragma_Home, "value")
    descriptor = None
    for klass in idl_Preproc_Pragma_Home.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_ifndef_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Ifndef)


def test_idl_preproc_ifndef_constructor_exists():
    assert callable(idl_Preproc_Ifndef.__init__)


def test_idl_preproc_ifndef_constructor_args():
    sig = inspect.signature(idl_Preproc_Ifndef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_ifndef_has_value():
    assert hasattr(idl_Preproc_Ifndef, "value")
    descriptor = None
    for klass in idl_Preproc_Ifndef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_preproc_ifdef_is_not_abstract():
    assert not inspect.isabstract(idl_Preproc_Ifdef)


def test_idl_preproc_ifdef_constructor_exists():
    assert callable(idl_Preproc_Ifdef.__init__)


def test_idl_preproc_ifdef_constructor_args():
    sig = inspect.signature(idl_Preproc_Ifdef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_idl_preproc_ifdef_has_value():
    assert hasattr(idl_Preproc_Ifdef, "value")
    descriptor = None
    for klass in idl_Preproc_Ifdef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_idl_filename_is_not_abstract():
    assert not inspect.isabstract(idl_FileName)


def test_idl_filename_constructor_exists():
    assert callable(idl_FileName.__init__)


def test_idl_filename_constructor_args():
    sig = inspect.signature(idl_FileName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_idl_filename_has_name():
    assert hasattr(idl_FileName, "name")
    descriptor = None
    for klass in idl_FileName.__mro__:
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
        "InOut",
        "Out",
        "In",
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
idl_FormalParameterType_strategy = st.builds(
    idl_FormalParameterType,
)
idl_TemplateDefinition_strategy = st.builds(
    idl_TemplateDefinition,
)
idl_FormalParameter_strategy = st.builds(
    idl_FormalParameter,
    name=
        safe_text
)
idl_ActualParameter_strategy = st.builds(
    idl_ActualParameter,
)
idl_FixedDefinition_strategy = st.builds(
    idl_FixedDefinition,
)
idl_StateMember_strategy = st.builds(
    idl_StateMember,
    isPublic=
        st.booleans(),
    names=
        safe_text
)
Event_strategy = st.builds(
    Event,
)
idl_EventDcl_strategy = st.builds(
    idl_EventDcl,
    isCustom=
        st.booleans(),
    isTruncatable=
        st.booleans()
)
idl_ConnectorExport_strategy = st.builds(
    idl_ConnectorExport,
)
idl_ConnectorHeader_strategy = st.builds(
    idl_ConnectorHeader,
    name=
        safe_text
)
idl_PortExport_strategy = st.builds(
    idl_PortExport,
)
idl_EventForwardDcl_strategy = st.builds(
    idl_EventForwardDcl,
)
idl_HomeExport_strategy = st.builds(
    idl_HomeExport,
)
idl_PrimaryKeySpec_strategy = st.builds(
    idl_PrimaryKeySpec,
)
idl_ComponentExport_strategy = st.builds(
    idl_ComponentExport,
)
idl_PrimaryExpr_strategy = st.builds(
    idl_PrimaryExpr,
)
ConstParamType_strategy = st.builds(
    ConstParamType,
)
idl_ConstType_strategy = st.builds(
    idl_ConstType,
)
idl_UnaryExpr_strategy = st.builds(
    idl_UnaryExpr,
    op=
        safe_text
)
idl_MultExpr_strategy = st.builds(
    idl_MultExpr,
    op=
        safe_text
)
idl_AddExpr_strategy = st.builds(
    idl_AddExpr,
    op=
        safe_text
)
idl_ShiftExpr_strategy = st.builds(
    idl_ShiftExpr,
    op=
        safe_text
)
idl_AndExpr_strategy = st.builds(
    idl_AndExpr,
    op=
        safe_text
)
idl_XOrExpr_strategy = st.builds(
    idl_XOrExpr,
    op=
        safe_text
)
ConstExp_strategy = st.builds(
    ConstExp,
)
idl_OrExpr_strategy = st.builds(
    idl_OrExpr,
    op=
        safe_text
)
idl_ElementSpec_strategy = st.builds(
    idl_ElementSpec,
)
idl_CaseLabel_strategy = st.builds(
    idl_CaseLabel,
    isDefault=
        st.booleans(),
    isCase=
        st.booleans()
)
idl_Case_strategy = st.builds(
    idl_Case,
)
idl_SwitchBody_strategy = st.builds(
    idl_SwitchBody,
)
idl_SwitchTypeSpec_strategy = st.builds(
    idl_SwitchTypeSpec,
)
ConstrForwardDecl_strategy = st.builds(
    ConstrForwardDecl,
)
idl_UnionForwardDecl_strategy = st.builds(
    idl_UnionForwardDecl,
)
idl_StructForwardDecl_strategy = st.builds(
    idl_StructForwardDecl,
)
FormalParameterType_strategy = st.builds(
    FormalParameterType,
)
idl_TypenameParamType_strategy = st.builds(
    idl_TypenameParamType,
)
idl_ConstParamType_strategy = st.builds(
    idl_ConstParamType,
)
idl_SequenceParamType_strategy = st.builds(
    idl_SequenceParamType,
)
idl_EventParamType_strategy = st.builds(
    idl_EventParamType,
)
idl_UnionParamType_strategy = st.builds(
    idl_UnionParamType,
)
idl_StructParamType_strategy = st.builds(
    idl_StructParamType,
)
idl_InterfaceParamType_strategy = st.builds(
    idl_InterfaceParamType,
)
idl_EnumParamType_strategy = st.builds(
    idl_EnumParamType,
)
idl_ExceptionParamType_strategy = st.builds(
    idl_ExceptionParamType,
)
idl_ValuetypeParamType_strategy = st.builds(
    idl_ValuetypeParamType,
)
idl_Declarator_strategy = st.builds(
    idl_Declarator,
    id=
        safe_text
)
idl_Member_strategy = st.builds(
    idl_Member,
)
TypeSpec_strategy = st.builds(
    TypeSpec,
)
idl_ConstrTypeSpec_strategy = st.builds(
    idl_ConstrTypeSpec,
)
idl_SimpleTypeSpec_strategy = st.builds(
    idl_SimpleTypeSpec,
)
ActualParameter_strategy = st.builds(
    ActualParameter,
)
idl_TypeSpec_strategy = st.builds(
    idl_TypeSpec,
)
ConstrTypeSpec_strategy = st.builds(
    ConstrTypeSpec,
)
TypeDecl_strategy = st.builds(
    TypeDecl,
)
idl_TypeDeclarator_strategy = st.builds(
    idl_TypeDeclarator,
)
idl_UnionType_strategy = st.builds(
    idl_UnionType,
    name=
        safe_text
)
idl_ConstrForwardDecl_strategy = st.builds(
    idl_ConstrForwardDecl,
    name=
        safe_text
)
ComplexDeclarator_strategy = st.builds(
    ComplexDeclarator,
)
idl_ComplexDeclarator_strategy = st.builds(
    idl_ComplexDeclarator,
)
Declarator_strategy = st.builds(
    Declarator,
)
idl_ArrayDeclarator_strategy = st.builds(
    idl_ArrayDeclarator,
)
idl_SimpleDeclarator_strategy = st.builds(
    idl_SimpleDeclarator,
)
PrimaryExpr_strategy = st.builds(
    PrimaryExpr,
)
idl_Literal_strategy = st.builds(
    idl_Literal,
    value=
        safe_text
)
ConstType_strategy = st.builds(
    ConstType,
)
idl_FixedPtConstType_strategy = st.builds(
    idl_FixedPtConstType,
)
SwitchTypeSpec_strategy = st.builds(
    SwitchTypeSpec,
)
idl_EnumType_strategy = st.builds(
    idl_EnumType,
    literal=
        safe_text,
    name=
        safe_text
)
SimpleTypeSpec_strategy = st.builds(
    SimpleTypeSpec,
)
idl_TemplateTypeSpec_strategy = st.builds(
    idl_TemplateTypeSpec,
)
ParamTypeSpec_strategy = st.builds(
    ParamTypeSpec,
)
idl_BaseTypeSpec_strategy = st.builds(
    idl_BaseTypeSpec,
)
OpTypeDecl_strategy = st.builds(
    OpTypeDecl,
)
idl_ParamDcl_strategy = st.builds(
    idl_ParamDcl,
    name=
        safe_text,
    direction=
        safe_text
)
idl_PositiveIntConst_strategy = st.builds(
    idl_PositiveIntConst,
)
TemplateTypeSpec_strategy = st.builds(
    TemplateTypeSpec,
)
idl_FixedPtType_strategy = st.builds(
    idl_FixedPtType,
)
idl_WideStringType_strategy = st.builds(
    idl_WideStringType,
)
idl_SequenceType_strategy = st.builds(
    idl_SequenceType,
)
idl_StringType_strategy = st.builds(
    idl_StringType,
)
Preproc_strategy = st.builds(
    Preproc,
)
idl_Preproc_Include_strategy = st.builds(
    idl_Preproc_Include,
    strValue=
        safe_text
)
ComponentExport_strategy = st.builds(
    ComponentExport,
)
idl_PublishesDcl_strategy = st.builds(
    idl_PublishesDcl,
    name=
        safe_text
)
idl_EmitDcl_strategy = st.builds(
    idl_EmitDcl,
    name=
        safe_text
)
idl_ConsumesDcl_strategy = st.builds(
    idl_ConsumesDcl,
    name=
        safe_text
)
Export_strategy = st.builds(
    Export,
)
Definition_strategy = st.builds(
    Definition,
)
idl_StructType_strategy = st.builds(
    idl_StructType,
    name=
        safe_text
)
idl_TemplateModuleInst_strategy = st.builds(
    idl_TemplateModuleInst,
    name=
        safe_text
)
idl_TemplateModule_strategy = st.builds(
    idl_TemplateModule,
    name=
        safe_text
)
idl_ComponentForwardDecl_strategy = st.builds(
    idl_ComponentForwardDecl,
    name=
        safe_text
)
idl_Preproc_strategy = st.builds(
    idl_Preproc,
)
idl_Definition_strategy = st.builds(
    idl_Definition,
)
idl_Import_decl_strategy = st.builds(
    idl_Import_decl,
    imported_scope=
        safe_text
)
idl_Specification_strategy = st.builds(
    idl_Specification,
)
Preproc_Pragma_strategy = st.builds(
    Preproc_Pragma,
)
idl_Preproc_Pragma_Conn_Type_strategy = st.builds(
    idl_Preproc_Pragma_Conn_Type,
    valuePort=
        safe_text,
    valueConnType=
        safe_text
)
idl_Preproc_Pragma_Prefix_strategy = st.builds(
    idl_Preproc_Pragma_Prefix,
    value=
        safe_text
)
idl_Preproc_Pragma_strategy = st.builds(
    idl_Preproc_Pragma,
)
idl_Preproc_Endif_strategy = st.builds(
    idl_Preproc_Endif,
)
idl_Preproc_Define_strategy = st.builds(
    idl_Preproc_Define,
    value=
        safe_text
)
idl_Preproc_Error_strategy = st.builds(
    idl_Preproc_Error,
    value=
        safe_text
)
idl_Preproc_Else_strategy = st.builds(
    idl_Preproc_Else,
)
idl_ConstExp_strategy = st.builds(
    idl_ConstExp,
)
idl_Preproc_If_Val_strategy = st.builds(
    idl_Preproc_If_Val,
)
idl_Preproc_If_Compare_strategy = st.builds(
    idl_Preproc_If_Compare,
    op=
        safe_text
)
idl_Preproc_If_strategy = st.builds(
    idl_Preproc_If,
    negation=
        st.booleans()
)
idl_Preproc_Undef_strategy = st.builds(
    idl_Preproc_Undef,
    value=
        safe_text
)
UnsignedInt_strategy = st.builds(
    UnsignedInt,
)
idl_UnsignedLongLongInt_strategy = st.builds(
    idl_UnsignedLongLongInt,
)
idl_UnsignedLongInt_strategy = st.builds(
    idl_UnsignedLongInt,
)
idl_UnsignedShortInt_strategy = st.builds(
    idl_UnsignedShortInt,
)
SignedInt_strategy = st.builds(
    SignedInt,
)
idl_SignedLongLongInt_strategy = st.builds(
    idl_SignedLongLongInt,
)
idl_SignedLongInt_strategy = st.builds(
    idl_SignedLongInt,
)
idl_SignedShortInt_strategy = st.builds(
    idl_SignedShortInt,
)
IntegerType_strategy = st.builds(
    IntegerType,
)
idl_UnsignedInt_strategy = st.builds(
    idl_UnsignedInt,
)
idl_SignedInt_strategy = st.builds(
    idl_SignedInt,
)
FloatingPtType_strategy = st.builds(
    FloatingPtType,
)
idl_LongDoubleType_strategy = st.builds(
    idl_LongDoubleType,
)
idl_DoubleType_strategy = st.builds(
    idl_DoubleType,
)
idl_FloatType_strategy = st.builds(
    idl_FloatType,
)
BaseTypeSpec_strategy = st.builds(
    BaseTypeSpec,
)
idl_OctetType_strategy = st.builds(
    idl_OctetType,
)
idl_IntegerType_strategy = st.builds(
    idl_IntegerType,
)
idl_AnyType_strategy = st.builds(
    idl_AnyType,
)
idl_BooleanType_strategy = st.builds(
    idl_BooleanType,
)
idl_WideCharType_strategy = st.builds(
    idl_WideCharType,
)
idl_CharType_strategy = st.builds(
    idl_CharType,
)
idl_ObjectType_strategy = st.builds(
    idl_ObjectType,
)
idl_ValueBaseType_strategy = st.builds(
    idl_ValueBaseType,
)
idl_FloatingPtType_strategy = st.builds(
    idl_FloatingPtType,
)
idl_ParamTypeSpec_strategy = st.builds(
    idl_ParamTypeSpec,
)
ConnectorExport_strategy = st.builds(
    ConnectorExport,
)
idl_PortDecl_strategy = st.builds(
    idl_PortDecl,
    isMirror=
        st.booleans(),
    name=
        safe_text
)
PortExport_strategy = st.builds(
    PortExport,
)
idl_ProvidesDcl_strategy = st.builds(
    idl_ProvidesDcl,
    name=
        safe_text
)
idl_UsesDcl_strategy = st.builds(
    idl_UsesDcl,
    name=
        safe_text,
    isMultiple=
        st.booleans()
)
idl_AttrDecl_strategy = st.builds(
    idl_AttrDecl,
    names=
        safe_text
)
HomeExport_strategy = st.builds(
    HomeExport,
)
idl_FinderDcl_strategy = st.builds(
    idl_FinderDcl,
    name=
        safe_text
)
idl_FactoryDcl_strategy = st.builds(
    idl_FactoryDcl,
    name=
        safe_text
)
idl_Export_strategy = st.builds(
    idl_Export,
)
idl_ScopedName_strategy = st.builds(
    idl_ScopedName,
    name=
        safe_text
)
idl_ContextExpr_strategy = st.builds(
    idl_ContextExpr,
    literal=
        safe_text
)
idl_ParameterDecls_strategy = st.builds(
    idl_ParameterDecls,
)
idl_OpTypeDecl_strategy = st.builds(
    idl_OpTypeDecl,
)
idl_OpDecl_strategy = st.builds(
    idl_OpDecl,
    name=
        safe_text,
    isOneway=
        st.booleans()
)
idl_ExceptionList_strategy = st.builds(
    idl_ExceptionList,
)
idl_AttrRaisesExpr_strategy = st.builds(
    idl_AttrRaisesExpr,
)
AttrDecl_strategy = st.builds(
    AttrDecl,
)
idl_ReadOnlyAttrSpec_strategy = st.builds(
    idl_ReadOnlyAttrSpec,
)
idl_AttrSpec_strategy = st.builds(
    idl_AttrSpec,
)
idl_Preproc_Pragma_Component_strategy = st.builds(
    idl_Preproc_Pragma_Component,
    value=
        safe_text
)
idl_Preproc_Pragma_Ndds_strategy = st.builds(
    idl_Preproc_Pragma_Ndds,
    value=
        safe_text
)
idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_strategy = st.builds(
    idl_Preproc_Pragma_Ciao_Ami4ccm_Idl,
    value=
        safe_text
)
idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_strategy = st.builds(
    idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle,
    value=
        safe_text
)
idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_strategy = st.builds(
    idl_Preproc_Pragma_Ciao_Ami4ccm_Interface,
    value=
        safe_text
)
idl_Preproc_Pragma_Ciao_Lem_strategy = st.builds(
    idl_Preproc_Pragma_Ciao_Lem,
    value=
        safe_text
)
idl_InterfaceBody_strategy = st.builds(
    idl_InterfaceBody,
)
idl_Interface_header_strategy = st.builds(
    idl_Interface_header,
    isLocal=
        st.booleans(),
    name=
        safe_text,
    isAbstract=
        st.booleans()
)
FixedDefinition_strategy = st.builds(
    FixedDefinition,
)
TemplateDefinition_strategy = st.builds(
    TemplateDefinition,
)
idl_ConstDecl_strategy = st.builds(
    idl_ConstDecl,
    name=
        safe_text
)
idl_NativeType_strategy = st.builds(
    idl_NativeType,
    name=
        safe_text
)
idl_ComponentDecl_strategy = st.builds(
    idl_ComponentDecl,
    name=
        safe_text
)
idl_Connector_strategy = st.builds(
    idl_Connector,
)
idl_FixedModule_strategy = st.builds(
    idl_FixedModule,
    name=
        safe_text
)
idl_TypeDecl_strategy = st.builds(
    idl_TypeDecl,
)
idl_TemplateModuleRef_strategy = st.builds(
    idl_TemplateModuleRef,
    id=
        safe_text,
    name=
        safe_text
)
idl_PortTypeDecl_strategy = st.builds(
    idl_PortTypeDecl,
    name=
        safe_text
)
idl_HomeDecl_strategy = st.builds(
    idl_HomeDecl,
    name=
        safe_text
)
idl_ExceptDecl_strategy = st.builds(
    idl_ExceptDecl,
    name=
        safe_text
)
idl_Event_strategy = st.builds(
    idl_Event,
    isAbstract=
        st.booleans(),
    name=
        safe_text
)
Interface_or_Forward_Decl_strategy = st.builds(
    Interface_or_Forward_Decl,
)
idl_Forward_decl_strategy = st.builds(
    idl_Forward_decl,
    name=
        safe_text
)
idl_Interface_decl_strategy = st.builds(
    idl_Interface_decl,
)
idl_Interface_or_Forward_Decl_strategy = st.builds(
    idl_Interface_or_Forward_Decl,
)
idl_IDLComment_strategy = st.builds(
    idl_IDLComment,
    body=
        safe_text
)
idl_Module_strategy = st.builds(
    idl_Module,
    name=
        safe_text
)
idl_Excluded_File_Marker_strategy = st.builds(
    idl_Excluded_File_Marker,
    file=
        safe_text
)
idl_File_Marker_strategy = st.builds(
    idl_File_Marker,
    file=
        safe_text
)
idl_Preproc_Pragma_Misc_strategy = st.builds(
    idl_Preproc_Pragma_Misc,
)
idl_Preproc_Pragma_DDS4CCM_Impl_strategy = st.builds(
    idl_Preproc_Pragma_DDS4CCM_Impl,
    value=
        safe_text
)
idl_Preproc_Pragma_Home_strategy = st.builds(
    idl_Preproc_Pragma_Home,
    value=
        safe_text
)
idl_Preproc_Ifndef_strategy = st.builds(
    idl_Preproc_Ifndef,
    value=
        safe_text
)
idl_Preproc_Ifdef_strategy = st.builds(
    idl_Preproc_Ifdef,
    value=
        safe_text
)
idl_FileName_strategy = st.builds(
    idl_FileName,
    name=
        safe_text
)

@given(instance=idl_FormalParameterType_strategy)
@settings(max_examples=50)
def test_idl_formalparametertype_instantiation(instance):
    assert isinstance(instance, idl_FormalParameterType)

@given(instance=idl_TemplateDefinition_strategy)
@settings(max_examples=50)
def test_idl_templatedefinition_instantiation(instance):
    assert isinstance(instance, idl_TemplateDefinition)

@given(instance=idl_FormalParameter_strategy)
@settings(max_examples=50)
def test_idl_formalparameter_instantiation(instance):
    assert isinstance(instance, idl_FormalParameter)



@given(instance=idl_FormalParameter_strategy)
def test_idl_formalparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ActualParameter_strategy)
@settings(max_examples=50)
def test_idl_actualparameter_instantiation(instance):
    assert isinstance(instance, idl_ActualParameter)

@given(instance=idl_FixedDefinition_strategy)
@settings(max_examples=50)
def test_idl_fixeddefinition_instantiation(instance):
    assert isinstance(instance, idl_FixedDefinition)

@given(instance=idl_StateMember_strategy)
@settings(max_examples=50)
def test_idl_statemember_instantiation(instance):
    assert isinstance(instance, idl_StateMember)



@given(instance=idl_StateMember_strategy)
def test_idl_statemember_isPublic_setter(instance):
    original = instance.isPublic
    instance.isPublic = original
    assert instance.isPublic == original



@given(instance=idl_StateMember_strategy)
def test_idl_statemember_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=idl_EventDcl_strategy)
@settings(max_examples=50)
def test_idl_eventdcl_instantiation(instance):
    assert isinstance(instance, idl_EventDcl)



@given(instance=idl_EventDcl_strategy)
def test_idl_eventdcl_isCustom_setter(instance):
    original = instance.isCustom
    instance.isCustom = original
    assert instance.isCustom == original



@given(instance=idl_EventDcl_strategy)
def test_idl_eventdcl_isTruncatable_setter(instance):
    original = instance.isTruncatable
    instance.isTruncatable = original
    assert instance.isTruncatable == original

@given(instance=idl_ConnectorExport_strategy)
@settings(max_examples=50)
def test_idl_connectorexport_instantiation(instance):
    assert isinstance(instance, idl_ConnectorExport)

@given(instance=idl_ConnectorHeader_strategy)
@settings(max_examples=50)
def test_idl_connectorheader_instantiation(instance):
    assert isinstance(instance, idl_ConnectorHeader)



@given(instance=idl_ConnectorHeader_strategy)
def test_idl_connectorheader_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_PortExport_strategy)
@settings(max_examples=50)
def test_idl_portexport_instantiation(instance):
    assert isinstance(instance, idl_PortExport)

@given(instance=idl_EventForwardDcl_strategy)
@settings(max_examples=50)
def test_idl_eventforwarddcl_instantiation(instance):
    assert isinstance(instance, idl_EventForwardDcl)

@given(instance=idl_HomeExport_strategy)
@settings(max_examples=50)
def test_idl_homeexport_instantiation(instance):
    assert isinstance(instance, idl_HomeExport)

@given(instance=idl_PrimaryKeySpec_strategy)
@settings(max_examples=50)
def test_idl_primarykeyspec_instantiation(instance):
    assert isinstance(instance, idl_PrimaryKeySpec)

@given(instance=idl_ComponentExport_strategy)
@settings(max_examples=50)
def test_idl_componentexport_instantiation(instance):
    assert isinstance(instance, idl_ComponentExport)

@given(instance=idl_PrimaryExpr_strategy)
@settings(max_examples=50)
def test_idl_primaryexpr_instantiation(instance):
    assert isinstance(instance, idl_PrimaryExpr)

@given(instance=ConstParamType_strategy)
@settings(max_examples=50)
def test_constparamtype_instantiation(instance):
    assert isinstance(instance, ConstParamType)

@given(instance=idl_ConstType_strategy)
@settings(max_examples=50)
def test_idl_consttype_instantiation(instance):
    assert isinstance(instance, idl_ConstType)

@given(instance=idl_UnaryExpr_strategy)
@settings(max_examples=50)
def test_idl_unaryexpr_instantiation(instance):
    assert isinstance(instance, idl_UnaryExpr)



@given(instance=idl_UnaryExpr_strategy)
def test_idl_unaryexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_MultExpr_strategy)
@settings(max_examples=50)
def test_idl_multexpr_instantiation(instance):
    assert isinstance(instance, idl_MultExpr)



@given(instance=idl_MultExpr_strategy)
def test_idl_multexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_AddExpr_strategy)
@settings(max_examples=50)
def test_idl_addexpr_instantiation(instance):
    assert isinstance(instance, idl_AddExpr)



@given(instance=idl_AddExpr_strategy)
def test_idl_addexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_ShiftExpr_strategy)
@settings(max_examples=50)
def test_idl_shiftexpr_instantiation(instance):
    assert isinstance(instance, idl_ShiftExpr)



@given(instance=idl_ShiftExpr_strategy)
def test_idl_shiftexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_AndExpr_strategy)
@settings(max_examples=50)
def test_idl_andexpr_instantiation(instance):
    assert isinstance(instance, idl_AndExpr)



@given(instance=idl_AndExpr_strategy)
def test_idl_andexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_XOrExpr_strategy)
@settings(max_examples=50)
def test_idl_xorexpr_instantiation(instance):
    assert isinstance(instance, idl_XOrExpr)



@given(instance=idl_XOrExpr_strategy)
def test_idl_xorexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ConstExp_strategy)
@settings(max_examples=50)
def test_constexp_instantiation(instance):
    assert isinstance(instance, ConstExp)

@given(instance=idl_OrExpr_strategy)
@settings(max_examples=50)
def test_idl_orexpr_instantiation(instance):
    assert isinstance(instance, idl_OrExpr)



@given(instance=idl_OrExpr_strategy)
def test_idl_orexpr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_ElementSpec_strategy)
@settings(max_examples=50)
def test_idl_elementspec_instantiation(instance):
    assert isinstance(instance, idl_ElementSpec)

@given(instance=idl_CaseLabel_strategy)
@settings(max_examples=50)
def test_idl_caselabel_instantiation(instance):
    assert isinstance(instance, idl_CaseLabel)



@given(instance=idl_CaseLabel_strategy)
def test_idl_caselabel_isDefault_setter(instance):
    original = instance.isDefault
    instance.isDefault = original
    assert instance.isDefault == original



@given(instance=idl_CaseLabel_strategy)
def test_idl_caselabel_isCase_setter(instance):
    original = instance.isCase
    instance.isCase = original
    assert instance.isCase == original

@given(instance=idl_Case_strategy)
@settings(max_examples=50)
def test_idl_case_instantiation(instance):
    assert isinstance(instance, idl_Case)

@given(instance=idl_SwitchBody_strategy)
@settings(max_examples=50)
def test_idl_switchbody_instantiation(instance):
    assert isinstance(instance, idl_SwitchBody)

@given(instance=idl_SwitchTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_switchtypespec_instantiation(instance):
    assert isinstance(instance, idl_SwitchTypeSpec)

@given(instance=ConstrForwardDecl_strategy)
@settings(max_examples=50)
def test_constrforwarddecl_instantiation(instance):
    assert isinstance(instance, ConstrForwardDecl)

@given(instance=idl_UnionForwardDecl_strategy)
@settings(max_examples=50)
def test_idl_unionforwarddecl_instantiation(instance):
    assert isinstance(instance, idl_UnionForwardDecl)

@given(instance=idl_StructForwardDecl_strategy)
@settings(max_examples=50)
def test_idl_structforwarddecl_instantiation(instance):
    assert isinstance(instance, idl_StructForwardDecl)

@given(instance=FormalParameterType_strategy)
@settings(max_examples=50)
def test_formalparametertype_instantiation(instance):
    assert isinstance(instance, FormalParameterType)

@given(instance=idl_TypenameParamType_strategy)
@settings(max_examples=50)
def test_idl_typenameparamtype_instantiation(instance):
    assert isinstance(instance, idl_TypenameParamType)

@given(instance=idl_ConstParamType_strategy)
@settings(max_examples=50)
def test_idl_constparamtype_instantiation(instance):
    assert isinstance(instance, idl_ConstParamType)

@given(instance=idl_SequenceParamType_strategy)
@settings(max_examples=50)
def test_idl_sequenceparamtype_instantiation(instance):
    assert isinstance(instance, idl_SequenceParamType)

@given(instance=idl_EventParamType_strategy)
@settings(max_examples=50)
def test_idl_eventparamtype_instantiation(instance):
    assert isinstance(instance, idl_EventParamType)

@given(instance=idl_UnionParamType_strategy)
@settings(max_examples=50)
def test_idl_unionparamtype_instantiation(instance):
    assert isinstance(instance, idl_UnionParamType)

@given(instance=idl_StructParamType_strategy)
@settings(max_examples=50)
def test_idl_structparamtype_instantiation(instance):
    assert isinstance(instance, idl_StructParamType)

@given(instance=idl_InterfaceParamType_strategy)
@settings(max_examples=50)
def test_idl_interfaceparamtype_instantiation(instance):
    assert isinstance(instance, idl_InterfaceParamType)

@given(instance=idl_EnumParamType_strategy)
@settings(max_examples=50)
def test_idl_enumparamtype_instantiation(instance):
    assert isinstance(instance, idl_EnumParamType)

@given(instance=idl_ExceptionParamType_strategy)
@settings(max_examples=50)
def test_idl_exceptionparamtype_instantiation(instance):
    assert isinstance(instance, idl_ExceptionParamType)

@given(instance=idl_ValuetypeParamType_strategy)
@settings(max_examples=50)
def test_idl_valuetypeparamtype_instantiation(instance):
    assert isinstance(instance, idl_ValuetypeParamType)

@given(instance=idl_Declarator_strategy)
@settings(max_examples=50)
def test_idl_declarator_instantiation(instance):
    assert isinstance(instance, idl_Declarator)



@given(instance=idl_Declarator_strategy)
def test_idl_declarator_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=idl_Member_strategy)
@settings(max_examples=50)
def test_idl_member_instantiation(instance):
    assert isinstance(instance, idl_Member)

@given(instance=TypeSpec_strategy)
@settings(max_examples=50)
def test_typespec_instantiation(instance):
    assert isinstance(instance, TypeSpec)

@given(instance=idl_ConstrTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_constrtypespec_instantiation(instance):
    assert isinstance(instance, idl_ConstrTypeSpec)

@given(instance=idl_SimpleTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_simpletypespec_instantiation(instance):
    assert isinstance(instance, idl_SimpleTypeSpec)

@given(instance=ActualParameter_strategy)
@settings(max_examples=50)
def test_actualparameter_instantiation(instance):
    assert isinstance(instance, ActualParameter)

@given(instance=idl_TypeSpec_strategy)
@settings(max_examples=50)
def test_idl_typespec_instantiation(instance):
    assert isinstance(instance, idl_TypeSpec)

@given(instance=ConstrTypeSpec_strategy)
@settings(max_examples=50)
def test_constrtypespec_instantiation(instance):
    assert isinstance(instance, ConstrTypeSpec)

@given(instance=TypeDecl_strategy)
@settings(max_examples=50)
def test_typedecl_instantiation(instance):
    assert isinstance(instance, TypeDecl)

@given(instance=idl_TypeDeclarator_strategy)
@settings(max_examples=50)
def test_idl_typedeclarator_instantiation(instance):
    assert isinstance(instance, idl_TypeDeclarator)

@given(instance=idl_UnionType_strategy)
@settings(max_examples=50)
def test_idl_uniontype_instantiation(instance):
    assert isinstance(instance, idl_UnionType)



@given(instance=idl_UnionType_strategy)
def test_idl_uniontype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ConstrForwardDecl_strategy)
@settings(max_examples=50)
def test_idl_constrforwarddecl_instantiation(instance):
    assert isinstance(instance, idl_ConstrForwardDecl)



@given(instance=idl_ConstrForwardDecl_strategy)
def test_idl_constrforwarddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ComplexDeclarator_strategy)
@settings(max_examples=50)
def test_complexdeclarator_instantiation(instance):
    assert isinstance(instance, ComplexDeclarator)

@given(instance=idl_ComplexDeclarator_strategy)
@settings(max_examples=50)
def test_idl_complexdeclarator_instantiation(instance):
    assert isinstance(instance, idl_ComplexDeclarator)

@given(instance=Declarator_strategy)
@settings(max_examples=50)
def test_declarator_instantiation(instance):
    assert isinstance(instance, Declarator)

@given(instance=idl_ArrayDeclarator_strategy)
@settings(max_examples=50)
def test_idl_arraydeclarator_instantiation(instance):
    assert isinstance(instance, idl_ArrayDeclarator)

@given(instance=idl_SimpleDeclarator_strategy)
@settings(max_examples=50)
def test_idl_simpledeclarator_instantiation(instance):
    assert isinstance(instance, idl_SimpleDeclarator)

@given(instance=PrimaryExpr_strategy)
@settings(max_examples=50)
def test_primaryexpr_instantiation(instance):
    assert isinstance(instance, PrimaryExpr)

@given(instance=idl_Literal_strategy)
@settings(max_examples=50)
def test_idl_literal_instantiation(instance):
    assert isinstance(instance, idl_Literal)



@given(instance=idl_Literal_strategy)
def test_idl_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ConstType_strategy)
@settings(max_examples=50)
def test_consttype_instantiation(instance):
    assert isinstance(instance, ConstType)

@given(instance=idl_FixedPtConstType_strategy)
@settings(max_examples=50)
def test_idl_fixedptconsttype_instantiation(instance):
    assert isinstance(instance, idl_FixedPtConstType)

@given(instance=SwitchTypeSpec_strategy)
@settings(max_examples=50)
def test_switchtypespec_instantiation(instance):
    assert isinstance(instance, SwitchTypeSpec)

@given(instance=idl_EnumType_strategy)
@settings(max_examples=50)
def test_idl_enumtype_instantiation(instance):
    assert isinstance(instance, idl_EnumType)



@given(instance=idl_EnumType_strategy)
def test_idl_enumtype_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original



@given(instance=idl_EnumType_strategy)
def test_idl_enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SimpleTypeSpec_strategy)
@settings(max_examples=50)
def test_simpletypespec_instantiation(instance):
    assert isinstance(instance, SimpleTypeSpec)

@given(instance=idl_TemplateTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_templatetypespec_instantiation(instance):
    assert isinstance(instance, idl_TemplateTypeSpec)

@given(instance=ParamTypeSpec_strategy)
@settings(max_examples=50)
def test_paramtypespec_instantiation(instance):
    assert isinstance(instance, ParamTypeSpec)

@given(instance=idl_BaseTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_basetypespec_instantiation(instance):
    assert isinstance(instance, idl_BaseTypeSpec)

@given(instance=OpTypeDecl_strategy)
@settings(max_examples=50)
def test_optypedecl_instantiation(instance):
    assert isinstance(instance, OpTypeDecl)

@given(instance=idl_ParamDcl_strategy)
@settings(max_examples=50)
def test_idl_paramdcl_instantiation(instance):
    assert isinstance(instance, idl_ParamDcl)



@given(instance=idl_ParamDcl_strategy)
def test_idl_paramdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=idl_ParamDcl_strategy)
def test_idl_paramdcl_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=idl_PositiveIntConst_strategy)
@settings(max_examples=50)
def test_idl_positiveintconst_instantiation(instance):
    assert isinstance(instance, idl_PositiveIntConst)

@given(instance=TemplateTypeSpec_strategy)
@settings(max_examples=50)
def test_templatetypespec_instantiation(instance):
    assert isinstance(instance, TemplateTypeSpec)

@given(instance=idl_FixedPtType_strategy)
@settings(max_examples=50)
def test_idl_fixedpttype_instantiation(instance):
    assert isinstance(instance, idl_FixedPtType)

@given(instance=idl_WideStringType_strategy)
@settings(max_examples=50)
def test_idl_widestringtype_instantiation(instance):
    assert isinstance(instance, idl_WideStringType)

@given(instance=idl_SequenceType_strategy)
@settings(max_examples=50)
def test_idl_sequencetype_instantiation(instance):
    assert isinstance(instance, idl_SequenceType)

@given(instance=idl_StringType_strategy)
@settings(max_examples=50)
def test_idl_stringtype_instantiation(instance):
    assert isinstance(instance, idl_StringType)

@given(instance=Preproc_strategy)
@settings(max_examples=50)
def test_preproc_instantiation(instance):
    assert isinstance(instance, Preproc)

@given(instance=idl_Preproc_Include_strategy)
@settings(max_examples=50)
def test_idl_preproc_include_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Include)



@given(instance=idl_Preproc_Include_strategy)
def test_idl_preproc_include_strValue_setter(instance):
    original = instance.strValue
    instance.strValue = original
    assert instance.strValue == original

@given(instance=ComponentExport_strategy)
@settings(max_examples=50)
def test_componentexport_instantiation(instance):
    assert isinstance(instance, ComponentExport)

@given(instance=idl_PublishesDcl_strategy)
@settings(max_examples=50)
def test_idl_publishesdcl_instantiation(instance):
    assert isinstance(instance, idl_PublishesDcl)



@given(instance=idl_PublishesDcl_strategy)
def test_idl_publishesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_EmitDcl_strategy)
@settings(max_examples=50)
def test_idl_emitdcl_instantiation(instance):
    assert isinstance(instance, idl_EmitDcl)



@given(instance=idl_EmitDcl_strategy)
def test_idl_emitdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ConsumesDcl_strategy)
@settings(max_examples=50)
def test_idl_consumesdcl_instantiation(instance):
    assert isinstance(instance, idl_ConsumesDcl)



@given(instance=idl_ConsumesDcl_strategy)
def test_idl_consumesdcl_name_setter(instance):
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

@given(instance=idl_StructType_strategy)
@settings(max_examples=50)
def test_idl_structtype_instantiation(instance):
    assert isinstance(instance, idl_StructType)



@given(instance=idl_StructType_strategy)
def test_idl_structtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_TemplateModuleInst_strategy)
@settings(max_examples=50)
def test_idl_templatemoduleinst_instantiation(instance):
    assert isinstance(instance, idl_TemplateModuleInst)



@given(instance=idl_TemplateModuleInst_strategy)
def test_idl_templatemoduleinst_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_TemplateModule_strategy)
@settings(max_examples=50)
def test_idl_templatemodule_instantiation(instance):
    assert isinstance(instance, idl_TemplateModule)



@given(instance=idl_TemplateModule_strategy)
def test_idl_templatemodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ComponentForwardDecl_strategy)
@settings(max_examples=50)
def test_idl_componentforwarddecl_instantiation(instance):
    assert isinstance(instance, idl_ComponentForwardDecl)



@given(instance=idl_ComponentForwardDecl_strategy)
def test_idl_componentforwarddecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Preproc_strategy)
@settings(max_examples=50)
def test_idl_preproc_instantiation(instance):
    assert isinstance(instance, idl_Preproc)

@given(instance=idl_Definition_strategy)
@settings(max_examples=50)
def test_idl_definition_instantiation(instance):
    assert isinstance(instance, idl_Definition)

@given(instance=idl_Import_decl_strategy)
@settings(max_examples=50)
def test_idl_import_decl_instantiation(instance):
    assert isinstance(instance, idl_Import_decl)



@given(instance=idl_Import_decl_strategy)
def test_idl_import_decl_imported_scope_setter(instance):
    original = instance.imported_scope
    instance.imported_scope = original
    assert instance.imported_scope == original

@given(instance=idl_Specification_strategy)
@settings(max_examples=50)
def test_idl_specification_instantiation(instance):
    assert isinstance(instance, idl_Specification)

@given(instance=Preproc_Pragma_strategy)
@settings(max_examples=50)
def test_preproc_pragma_instantiation(instance):
    assert isinstance(instance, Preproc_Pragma)

@given(instance=idl_Preproc_Pragma_Conn_Type_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_conn_type_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Conn_Type)



@given(instance=idl_Preproc_Pragma_Conn_Type_strategy)
def test_idl_preproc_pragma_conn_type_valuePort_setter(instance):
    original = instance.valuePort
    instance.valuePort = original
    assert instance.valuePort == original



@given(instance=idl_Preproc_Pragma_Conn_Type_strategy)
def test_idl_preproc_pragma_conn_type_valueConnType_setter(instance):
    original = instance.valueConnType
    instance.valueConnType = original
    assert instance.valueConnType == original

@given(instance=idl_Preproc_Pragma_Prefix_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_prefix_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Prefix)



@given(instance=idl_Preproc_Pragma_Prefix_strategy)
def test_idl_preproc_pragma_prefix_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma)

@given(instance=idl_Preproc_Endif_strategy)
@settings(max_examples=50)
def test_idl_preproc_endif_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Endif)

@given(instance=idl_Preproc_Define_strategy)
@settings(max_examples=50)
def test_idl_preproc_define_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Define)



@given(instance=idl_Preproc_Define_strategy)
def test_idl_preproc_define_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Error_strategy)
@settings(max_examples=50)
def test_idl_preproc_error_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Error)



@given(instance=idl_Preproc_Error_strategy)
def test_idl_preproc_error_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Else_strategy)
@settings(max_examples=50)
def test_idl_preproc_else_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Else)

@given(instance=idl_ConstExp_strategy)
@settings(max_examples=50)
def test_idl_constexp_instantiation(instance):
    assert isinstance(instance, idl_ConstExp)

@given(instance=idl_Preproc_If_Val_strategy)
@settings(max_examples=50)
def test_idl_preproc_if_val_instantiation(instance):
    assert isinstance(instance, idl_Preproc_If_Val)

@given(instance=idl_Preproc_If_Compare_strategy)
@settings(max_examples=50)
def test_idl_preproc_if_compare_instantiation(instance):
    assert isinstance(instance, idl_Preproc_If_Compare)



@given(instance=idl_Preproc_If_Compare_strategy)
def test_idl_preproc_if_compare_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=idl_Preproc_If_strategy)
@settings(max_examples=50)
def test_idl_preproc_if_instantiation(instance):
    assert isinstance(instance, idl_Preproc_If)



@given(instance=idl_Preproc_If_strategy)
def test_idl_preproc_if_negation_setter(instance):
    original = instance.negation
    instance.negation = original
    assert instance.negation == original

@given(instance=idl_Preproc_Undef_strategy)
@settings(max_examples=50)
def test_idl_preproc_undef_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Undef)



@given(instance=idl_Preproc_Undef_strategy)
def test_idl_preproc_undef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UnsignedInt_strategy)
@settings(max_examples=50)
def test_unsignedint_instantiation(instance):
    assert isinstance(instance, UnsignedInt)

@given(instance=idl_UnsignedLongLongInt_strategy)
@settings(max_examples=50)
def test_idl_unsignedlonglongint_instantiation(instance):
    assert isinstance(instance, idl_UnsignedLongLongInt)

@given(instance=idl_UnsignedLongInt_strategy)
@settings(max_examples=50)
def test_idl_unsignedlongint_instantiation(instance):
    assert isinstance(instance, idl_UnsignedLongInt)

@given(instance=idl_UnsignedShortInt_strategy)
@settings(max_examples=50)
def test_idl_unsignedshortint_instantiation(instance):
    assert isinstance(instance, idl_UnsignedShortInt)

@given(instance=SignedInt_strategy)
@settings(max_examples=50)
def test_signedint_instantiation(instance):
    assert isinstance(instance, SignedInt)

@given(instance=idl_SignedLongLongInt_strategy)
@settings(max_examples=50)
def test_idl_signedlonglongint_instantiation(instance):
    assert isinstance(instance, idl_SignedLongLongInt)

@given(instance=idl_SignedLongInt_strategy)
@settings(max_examples=50)
def test_idl_signedlongint_instantiation(instance):
    assert isinstance(instance, idl_SignedLongInt)

@given(instance=idl_SignedShortInt_strategy)
@settings(max_examples=50)
def test_idl_signedshortint_instantiation(instance):
    assert isinstance(instance, idl_SignedShortInt)

@given(instance=IntegerType_strategy)
@settings(max_examples=50)
def test_integertype_instantiation(instance):
    assert isinstance(instance, IntegerType)

@given(instance=idl_UnsignedInt_strategy)
@settings(max_examples=50)
def test_idl_unsignedint_instantiation(instance):
    assert isinstance(instance, idl_UnsignedInt)

@given(instance=idl_SignedInt_strategy)
@settings(max_examples=50)
def test_idl_signedint_instantiation(instance):
    assert isinstance(instance, idl_SignedInt)

@given(instance=FloatingPtType_strategy)
@settings(max_examples=50)
def test_floatingpttype_instantiation(instance):
    assert isinstance(instance, FloatingPtType)

@given(instance=idl_LongDoubleType_strategy)
@settings(max_examples=50)
def test_idl_longdoubletype_instantiation(instance):
    assert isinstance(instance, idl_LongDoubleType)

@given(instance=idl_DoubleType_strategy)
@settings(max_examples=50)
def test_idl_doubletype_instantiation(instance):
    assert isinstance(instance, idl_DoubleType)

@given(instance=idl_FloatType_strategy)
@settings(max_examples=50)
def test_idl_floattype_instantiation(instance):
    assert isinstance(instance, idl_FloatType)

@given(instance=BaseTypeSpec_strategy)
@settings(max_examples=50)
def test_basetypespec_instantiation(instance):
    assert isinstance(instance, BaseTypeSpec)

@given(instance=idl_OctetType_strategy)
@settings(max_examples=50)
def test_idl_octettype_instantiation(instance):
    assert isinstance(instance, idl_OctetType)

@given(instance=idl_IntegerType_strategy)
@settings(max_examples=50)
def test_idl_integertype_instantiation(instance):
    assert isinstance(instance, idl_IntegerType)

@given(instance=idl_AnyType_strategy)
@settings(max_examples=50)
def test_idl_anytype_instantiation(instance):
    assert isinstance(instance, idl_AnyType)

@given(instance=idl_BooleanType_strategy)
@settings(max_examples=50)
def test_idl_booleantype_instantiation(instance):
    assert isinstance(instance, idl_BooleanType)

@given(instance=idl_WideCharType_strategy)
@settings(max_examples=50)
def test_idl_widechartype_instantiation(instance):
    assert isinstance(instance, idl_WideCharType)

@given(instance=idl_CharType_strategy)
@settings(max_examples=50)
def test_idl_chartype_instantiation(instance):
    assert isinstance(instance, idl_CharType)

@given(instance=idl_ObjectType_strategy)
@settings(max_examples=50)
def test_idl_objecttype_instantiation(instance):
    assert isinstance(instance, idl_ObjectType)

@given(instance=idl_ValueBaseType_strategy)
@settings(max_examples=50)
def test_idl_valuebasetype_instantiation(instance):
    assert isinstance(instance, idl_ValueBaseType)

@given(instance=idl_FloatingPtType_strategy)
@settings(max_examples=50)
def test_idl_floatingpttype_instantiation(instance):
    assert isinstance(instance, idl_FloatingPtType)

@given(instance=idl_ParamTypeSpec_strategy)
@settings(max_examples=50)
def test_idl_paramtypespec_instantiation(instance):
    assert isinstance(instance, idl_ParamTypeSpec)

@given(instance=ConnectorExport_strategy)
@settings(max_examples=50)
def test_connectorexport_instantiation(instance):
    assert isinstance(instance, ConnectorExport)

@given(instance=idl_PortDecl_strategy)
@settings(max_examples=50)
def test_idl_portdecl_instantiation(instance):
    assert isinstance(instance, idl_PortDecl)



@given(instance=idl_PortDecl_strategy)
def test_idl_portdecl_isMirror_setter(instance):
    original = instance.isMirror
    instance.isMirror = original
    assert instance.isMirror == original



@given(instance=idl_PortDecl_strategy)
def test_idl_portdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PortExport_strategy)
@settings(max_examples=50)
def test_portexport_instantiation(instance):
    assert isinstance(instance, PortExport)

@given(instance=idl_ProvidesDcl_strategy)
@settings(max_examples=50)
def test_idl_providesdcl_instantiation(instance):
    assert isinstance(instance, idl_ProvidesDcl)



@given(instance=idl_ProvidesDcl_strategy)
def test_idl_providesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_UsesDcl_strategy)
@settings(max_examples=50)
def test_idl_usesdcl_instantiation(instance):
    assert isinstance(instance, idl_UsesDcl)



@given(instance=idl_UsesDcl_strategy)
def test_idl_usesdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=idl_UsesDcl_strategy)
def test_idl_usesdcl_isMultiple_setter(instance):
    original = instance.isMultiple
    instance.isMultiple = original
    assert instance.isMultiple == original

@given(instance=idl_AttrDecl_strategy)
@settings(max_examples=50)
def test_idl_attrdecl_instantiation(instance):
    assert isinstance(instance, idl_AttrDecl)



@given(instance=idl_AttrDecl_strategy)
def test_idl_attrdecl_names_setter(instance):
    original = instance.names
    instance.names = original
    assert instance.names == original

@given(instance=HomeExport_strategy)
@settings(max_examples=50)
def test_homeexport_instantiation(instance):
    assert isinstance(instance, HomeExport)

@given(instance=idl_FinderDcl_strategy)
@settings(max_examples=50)
def test_idl_finderdcl_instantiation(instance):
    assert isinstance(instance, idl_FinderDcl)



@given(instance=idl_FinderDcl_strategy)
def test_idl_finderdcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_FactoryDcl_strategy)
@settings(max_examples=50)
def test_idl_factorydcl_instantiation(instance):
    assert isinstance(instance, idl_FactoryDcl)



@given(instance=idl_FactoryDcl_strategy)
def test_idl_factorydcl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Export_strategy)
@settings(max_examples=50)
def test_idl_export_instantiation(instance):
    assert isinstance(instance, idl_Export)

@given(instance=idl_ScopedName_strategy)
@settings(max_examples=50)
def test_idl_scopedname_instantiation(instance):
    assert isinstance(instance, idl_ScopedName)



@given(instance=idl_ScopedName_strategy)
def test_idl_scopedname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ContextExpr_strategy)
@settings(max_examples=50)
def test_idl_contextexpr_instantiation(instance):
    assert isinstance(instance, idl_ContextExpr)



@given(instance=idl_ContextExpr_strategy)
def test_idl_contextexpr_literal_setter(instance):
    original = instance.literal
    instance.literal = original
    assert instance.literal == original

@given(instance=idl_ParameterDecls_strategy)
@settings(max_examples=50)
def test_idl_parameterdecls_instantiation(instance):
    assert isinstance(instance, idl_ParameterDecls)

@given(instance=idl_OpTypeDecl_strategy)
@settings(max_examples=50)
def test_idl_optypedecl_instantiation(instance):
    assert isinstance(instance, idl_OpTypeDecl)

@given(instance=idl_OpDecl_strategy)
@settings(max_examples=50)
def test_idl_opdecl_instantiation(instance):
    assert isinstance(instance, idl_OpDecl)



@given(instance=idl_OpDecl_strategy)
def test_idl_opdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=idl_OpDecl_strategy)
def test_idl_opdecl_isOneway_setter(instance):
    original = instance.isOneway
    instance.isOneway = original
    assert instance.isOneway == original

@given(instance=idl_ExceptionList_strategy)
@settings(max_examples=50)
def test_idl_exceptionlist_instantiation(instance):
    assert isinstance(instance, idl_ExceptionList)

@given(instance=idl_AttrRaisesExpr_strategy)
@settings(max_examples=50)
def test_idl_attrraisesexpr_instantiation(instance):
    assert isinstance(instance, idl_AttrRaisesExpr)

@given(instance=AttrDecl_strategy)
@settings(max_examples=50)
def test_attrdecl_instantiation(instance):
    assert isinstance(instance, AttrDecl)

@given(instance=idl_ReadOnlyAttrSpec_strategy)
@settings(max_examples=50)
def test_idl_readonlyattrspec_instantiation(instance):
    assert isinstance(instance, idl_ReadOnlyAttrSpec)

@given(instance=idl_AttrSpec_strategy)
@settings(max_examples=50)
def test_idl_attrspec_instantiation(instance):
    assert isinstance(instance, idl_AttrSpec)

@given(instance=idl_Preproc_Pragma_Component_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_component_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Component)



@given(instance=idl_Preproc_Pragma_Component_strategy)
def test_idl_preproc_pragma_component_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Ndds_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_ndds_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Ndds)



@given(instance=idl_Preproc_Pragma_Ndds_strategy)
def test_idl_preproc_pragma_ndds_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_ciao_ami4ccm_idl_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Ciao_Ami4ccm_Idl)



@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Idl_strategy)
def test_idl_preproc_pragma_ciao_ami4ccm_idl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle)



@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Receptacle_strategy)
def test_idl_preproc_pragma_ciao_ami4ccm_receptacle_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_ciao_ami4ccm_interface_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Ciao_Ami4ccm_Interface)



@given(instance=idl_Preproc_Pragma_Ciao_Ami4ccm_Interface_strategy)
def test_idl_preproc_pragma_ciao_ami4ccm_interface_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Ciao_Lem_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_ciao_lem_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Ciao_Lem)



@given(instance=idl_Preproc_Pragma_Ciao_Lem_strategy)
def test_idl_preproc_pragma_ciao_lem_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_InterfaceBody_strategy)
@settings(max_examples=50)
def test_idl_interfacebody_instantiation(instance):
    assert isinstance(instance, idl_InterfaceBody)

@given(instance=idl_Interface_header_strategy)
@settings(max_examples=50)
def test_idl_interface_header_instantiation(instance):
    assert isinstance(instance, idl_Interface_header)



@given(instance=idl_Interface_header_strategy)
def test_idl_interface_header_isLocal_setter(instance):
    original = instance.isLocal
    instance.isLocal = original
    assert instance.isLocal == original



@given(instance=idl_Interface_header_strategy)
def test_idl_interface_header_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=idl_Interface_header_strategy)
def test_idl_interface_header_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=FixedDefinition_strategy)
@settings(max_examples=50)
def test_fixeddefinition_instantiation(instance):
    assert isinstance(instance, FixedDefinition)

@given(instance=TemplateDefinition_strategy)
@settings(max_examples=50)
def test_templatedefinition_instantiation(instance):
    assert isinstance(instance, TemplateDefinition)

@given(instance=idl_ConstDecl_strategy)
@settings(max_examples=50)
def test_idl_constdecl_instantiation(instance):
    assert isinstance(instance, idl_ConstDecl)



@given(instance=idl_ConstDecl_strategy)
def test_idl_constdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_NativeType_strategy)
@settings(max_examples=50)
def test_idl_nativetype_instantiation(instance):
    assert isinstance(instance, idl_NativeType)



@given(instance=idl_NativeType_strategy)
def test_idl_nativetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ComponentDecl_strategy)
@settings(max_examples=50)
def test_idl_componentdecl_instantiation(instance):
    assert isinstance(instance, idl_ComponentDecl)



@given(instance=idl_ComponentDecl_strategy)
def test_idl_componentdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Connector_strategy)
@settings(max_examples=50)
def test_idl_connector_instantiation(instance):
    assert isinstance(instance, idl_Connector)

@given(instance=idl_FixedModule_strategy)
@settings(max_examples=50)
def test_idl_fixedmodule_instantiation(instance):
    assert isinstance(instance, idl_FixedModule)



@given(instance=idl_FixedModule_strategy)
def test_idl_fixedmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_TypeDecl_strategy)
@settings(max_examples=50)
def test_idl_typedecl_instantiation(instance):
    assert isinstance(instance, idl_TypeDecl)

@given(instance=idl_TemplateModuleRef_strategy)
@settings(max_examples=50)
def test_idl_templatemoduleref_instantiation(instance):
    assert isinstance(instance, idl_TemplateModuleRef)



@given(instance=idl_TemplateModuleRef_strategy)
def test_idl_templatemoduleref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=idl_TemplateModuleRef_strategy)
def test_idl_templatemoduleref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_PortTypeDecl_strategy)
@settings(max_examples=50)
def test_idl_porttypedecl_instantiation(instance):
    assert isinstance(instance, idl_PortTypeDecl)



@given(instance=idl_PortTypeDecl_strategy)
def test_idl_porttypedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_HomeDecl_strategy)
@settings(max_examples=50)
def test_idl_homedecl_instantiation(instance):
    assert isinstance(instance, idl_HomeDecl)



@given(instance=idl_HomeDecl_strategy)
def test_idl_homedecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_ExceptDecl_strategy)
@settings(max_examples=50)
def test_idl_exceptdecl_instantiation(instance):
    assert isinstance(instance, idl_ExceptDecl)



@given(instance=idl_ExceptDecl_strategy)
def test_idl_exceptdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Event_strategy)
@settings(max_examples=50)
def test_idl_event_instantiation(instance):
    assert isinstance(instance, idl_Event)



@given(instance=idl_Event_strategy)
def test_idl_event_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=idl_Event_strategy)
def test_idl_event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Interface_or_Forward_Decl_strategy)
@settings(max_examples=50)
def test_interface_or_forward_decl_instantiation(instance):
    assert isinstance(instance, Interface_or_Forward_Decl)

@given(instance=idl_Forward_decl_strategy)
@settings(max_examples=50)
def test_idl_forward_decl_instantiation(instance):
    assert isinstance(instance, idl_Forward_decl)



@given(instance=idl_Forward_decl_strategy)
def test_idl_forward_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Interface_decl_strategy)
@settings(max_examples=50)
def test_idl_interface_decl_instantiation(instance):
    assert isinstance(instance, idl_Interface_decl)

@given(instance=idl_Interface_or_Forward_Decl_strategy)
@settings(max_examples=50)
def test_idl_interface_or_forward_decl_instantiation(instance):
    assert isinstance(instance, idl_Interface_or_Forward_Decl)

@given(instance=idl_IDLComment_strategy)
@settings(max_examples=50)
def test_idl_idlcomment_instantiation(instance):
    assert isinstance(instance, idl_IDLComment)



@given(instance=idl_IDLComment_strategy)
def test_idl_idlcomment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=idl_Module_strategy)
@settings(max_examples=50)
def test_idl_module_instantiation(instance):
    assert isinstance(instance, idl_Module)



@given(instance=idl_Module_strategy)
def test_idl_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=idl_Excluded_File_Marker_strategy)
@settings(max_examples=50)
def test_idl_excluded_file_marker_instantiation(instance):
    assert isinstance(instance, idl_Excluded_File_Marker)



@given(instance=idl_Excluded_File_Marker_strategy)
def test_idl_excluded_file_marker_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=idl_File_Marker_strategy)
@settings(max_examples=50)
def test_idl_file_marker_instantiation(instance):
    assert isinstance(instance, idl_File_Marker)



@given(instance=idl_File_Marker_strategy)
def test_idl_file_marker_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=idl_Preproc_Pragma_Misc_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_misc_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Misc)

@given(instance=idl_Preproc_Pragma_DDS4CCM_Impl_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_dds4ccm_impl_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_DDS4CCM_Impl)



@given(instance=idl_Preproc_Pragma_DDS4CCM_Impl_strategy)
def test_idl_preproc_pragma_dds4ccm_impl_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Pragma_Home_strategy)
@settings(max_examples=50)
def test_idl_preproc_pragma_home_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Pragma_Home)



@given(instance=idl_Preproc_Pragma_Home_strategy)
def test_idl_preproc_pragma_home_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Ifndef_strategy)
@settings(max_examples=50)
def test_idl_preproc_ifndef_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Ifndef)



@given(instance=idl_Preproc_Ifndef_strategy)
def test_idl_preproc_ifndef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_Preproc_Ifdef_strategy)
@settings(max_examples=50)
def test_idl_preproc_ifdef_instantiation(instance):
    assert isinstance(instance, idl_Preproc_Ifdef)



@given(instance=idl_Preproc_Ifdef_strategy)
def test_idl_preproc_ifdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=idl_FileName_strategy)
@settings(max_examples=50)
def test_idl_filename_instantiation(instance):
    assert isinstance(instance, idl_FileName)



@given(instance=idl_FileName_strategy)
def test_idl_filename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
