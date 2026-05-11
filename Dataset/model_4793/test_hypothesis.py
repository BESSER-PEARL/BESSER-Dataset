import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Declarator,
    types::ForwardDcl,
    MemberContainer,
    PrimitiveType,
    types::Any,
    types::LongLong,
    types::ValueBaseType,
    types::IdlObject,
    types::IdlChar,
    types::WChar,
    types::Double,
    types::Float,
    types::LongDouble,
    types::Octet,
    types::IdlWChar,
    types::UShort,
    types::ULongLong,
    types::ULong,
    types::Boolean,
    types::Long,
    types::Short,
    Typed,
    TemplateType,
    types::WString,
    types::FixedPtType,
    types::IdlString,
    types::SequenceType,
    types::Declarator,
    types::Expression,
    CaseLabel,
    types::ExprCaseLabel,
    types::DefaultCaseLabel,
    types::IdlType,
    FileRegion,
    types::Case,
    types::CaseLabel,
    types::ElementSpec,
    types::Switch,
    IdlType,
    types::PrimitiveType,
    types::TemplateType,
    types::VoidType,
    IdlTypeDcl,
    types::UnionForwardDcl,
    types::StructType,
    types::EnumType,
    types::UnionType,
    types::StructForwardDcl,
    types::Enumeration,
    TypedElement,
    types::TypeDef,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_declarator_is_not_abstract():
    assert not inspect.isabstract(Declarator)


def test_declarator_constructor_exists():
    assert callable(Declarator.__init__)


def test_declarator_constructor_args():
    sig = inspect.signature(Declarator.__init__)
    params = list(sig.parameters.keys())



def test_types::forwarddcl_is_not_abstract():
    assert not inspect.isabstract(types::ForwardDcl)


def test_types::forwarddcl_constructor_exists():
    assert callable(types::ForwardDcl.__init__)


def test_types::forwarddcl_constructor_args():
    sig = inspect.signature(types::ForwardDcl.__init__)
    params = list(sig.parameters.keys())



def test_membercontainer_is_not_abstract():
    assert not inspect.isabstract(MemberContainer)


def test_membercontainer_constructor_exists():
    assert callable(MemberContainer.__init__)


def test_membercontainer_constructor_args():
    sig = inspect.signature(MemberContainer.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::any_is_not_abstract():
    assert not inspect.isabstract(types::Any)


def test_types::any_constructor_exists():
    assert callable(types::Any.__init__)


def test_types::any_constructor_args():
    sig = inspect.signature(types::Any.__init__)
    params = list(sig.parameters.keys())



def test_types::longlong_is_not_abstract():
    assert not inspect.isabstract(types::LongLong)


def test_types::longlong_constructor_exists():
    assert callable(types::LongLong.__init__)


def test_types::longlong_constructor_args():
    sig = inspect.signature(types::LongLong.__init__)
    params = list(sig.parameters.keys())



def test_types::valuebasetype_is_not_abstract():
    assert not inspect.isabstract(types::ValueBaseType)


def test_types::valuebasetype_constructor_exists():
    assert callable(types::ValueBaseType.__init__)


def test_types::valuebasetype_constructor_args():
    sig = inspect.signature(types::ValueBaseType.__init__)
    params = list(sig.parameters.keys())



def test_types::idlobject_is_not_abstract():
    assert not inspect.isabstract(types::IdlObject)


def test_types::idlobject_constructor_exists():
    assert callable(types::IdlObject.__init__)


def test_types::idlobject_constructor_args():
    sig = inspect.signature(types::IdlObject.__init__)
    params = list(sig.parameters.keys())



def test_types::idlchar_is_not_abstract():
    assert not inspect.isabstract(types::IdlChar)


def test_types::idlchar_constructor_exists():
    assert callable(types::IdlChar.__init__)


def test_types::idlchar_constructor_args():
    sig = inspect.signature(types::IdlChar.__init__)
    params = list(sig.parameters.keys())



def test_types::wchar_is_not_abstract():
    assert not inspect.isabstract(types::WChar)


def test_types::wchar_constructor_exists():
    assert callable(types::WChar.__init__)


def test_types::wchar_constructor_args():
    sig = inspect.signature(types::WChar.__init__)
    params = list(sig.parameters.keys())



def test_types::double_is_not_abstract():
    assert not inspect.isabstract(types::Double)


def test_types::double_constructor_exists():
    assert callable(types::Double.__init__)


def test_types::double_constructor_args():
    sig = inspect.signature(types::Double.__init__)
    params = list(sig.parameters.keys())



def test_types::float_is_not_abstract():
    assert not inspect.isabstract(types::Float)


def test_types::float_constructor_exists():
    assert callable(types::Float.__init__)


def test_types::float_constructor_args():
    sig = inspect.signature(types::Float.__init__)
    params = list(sig.parameters.keys())



def test_types::longdouble_is_not_abstract():
    assert not inspect.isabstract(types::LongDouble)


def test_types::longdouble_constructor_exists():
    assert callable(types::LongDouble.__init__)


def test_types::longdouble_constructor_args():
    sig = inspect.signature(types::LongDouble.__init__)
    params = list(sig.parameters.keys())



def test_types::octet_is_not_abstract():
    assert not inspect.isabstract(types::Octet)


def test_types::octet_constructor_exists():
    assert callable(types::Octet.__init__)


def test_types::octet_constructor_args():
    sig = inspect.signature(types::Octet.__init__)
    params = list(sig.parameters.keys())



def test_types::idlwchar_is_not_abstract():
    assert not inspect.isabstract(types::IdlWChar)


def test_types::idlwchar_constructor_exists():
    assert callable(types::IdlWChar.__init__)


def test_types::idlwchar_constructor_args():
    sig = inspect.signature(types::IdlWChar.__init__)
    params = list(sig.parameters.keys())



def test_types::ushort_is_not_abstract():
    assert not inspect.isabstract(types::UShort)


def test_types::ushort_constructor_exists():
    assert callable(types::UShort.__init__)


def test_types::ushort_constructor_args():
    sig = inspect.signature(types::UShort.__init__)
    params = list(sig.parameters.keys())



def test_types::ulonglong_is_not_abstract():
    assert not inspect.isabstract(types::ULongLong)


def test_types::ulonglong_constructor_exists():
    assert callable(types::ULongLong.__init__)


def test_types::ulonglong_constructor_args():
    sig = inspect.signature(types::ULongLong.__init__)
    params = list(sig.parameters.keys())



def test_types::ulong_is_not_abstract():
    assert not inspect.isabstract(types::ULong)


def test_types::ulong_constructor_exists():
    assert callable(types::ULong.__init__)


def test_types::ulong_constructor_args():
    sig = inspect.signature(types::ULong.__init__)
    params = list(sig.parameters.keys())



def test_types::boolean_is_not_abstract():
    assert not inspect.isabstract(types::Boolean)


def test_types::boolean_constructor_exists():
    assert callable(types::Boolean.__init__)


def test_types::boolean_constructor_args():
    sig = inspect.signature(types::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_types::long_is_not_abstract():
    assert not inspect.isabstract(types::Long)


def test_types::long_constructor_exists():
    assert callable(types::Long.__init__)


def test_types::long_constructor_args():
    sig = inspect.signature(types::Long.__init__)
    params = list(sig.parameters.keys())



def test_types::short_is_not_abstract():
    assert not inspect.isabstract(types::Short)


def test_types::short_constructor_exists():
    assert callable(types::Short.__init__)


def test_types::short_constructor_args():
    sig = inspect.signature(types::Short.__init__)
    params = list(sig.parameters.keys())



def test_typed_is_not_abstract():
    assert not inspect.isabstract(Typed)


def test_typed_constructor_exists():
    assert callable(Typed.__init__)


def test_typed_constructor_args():
    sig = inspect.signature(Typed.__init__)
    params = list(sig.parameters.keys())



def test_templatetype_is_not_abstract():
    assert not inspect.isabstract(TemplateType)


def test_templatetype_constructor_exists():
    assert callable(TemplateType.__init__)


def test_templatetype_constructor_args():
    sig = inspect.signature(TemplateType.__init__)
    params = list(sig.parameters.keys())



def test_types::wstring_is_not_abstract():
    assert not inspect.isabstract(types::WString)


def test_types::wstring_constructor_exists():
    assert callable(types::WString.__init__)


def test_types::wstring_constructor_args():
    sig = inspect.signature(types::WString.__init__)
    params = list(sig.parameters.keys())



def test_types::fixedpttype_is_not_abstract():
    assert not inspect.isabstract(types::FixedPtType)


def test_types::fixedpttype_constructor_exists():
    assert callable(types::FixedPtType.__init__)


def test_types::fixedpttype_constructor_args():
    sig = inspect.signature(types::FixedPtType.__init__)
    params = list(sig.parameters.keys())



def test_types::idlstring_is_not_abstract():
    assert not inspect.isabstract(types::IdlString)


def test_types::idlstring_constructor_exists():
    assert callable(types::IdlString.__init__)


def test_types::idlstring_constructor_args():
    sig = inspect.signature(types::IdlString.__init__)
    params = list(sig.parameters.keys())



def test_types::sequencetype_is_not_abstract():
    assert not inspect.isabstract(types::SequenceType)


def test_types::sequencetype_constructor_exists():
    assert callable(types::SequenceType.__init__)


def test_types::sequencetype_constructor_args():
    sig = inspect.signature(types::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_types::declarator_is_not_abstract():
    assert not inspect.isabstract(types::Declarator)


def test_types::declarator_constructor_exists():
    assert callable(types::Declarator.__init__)


def test_types::declarator_constructor_args():
    sig = inspect.signature(types::Declarator.__init__)
    params = list(sig.parameters.keys())



def test_types::expression_is_not_abstract():
    assert not inspect.isabstract(types::Expression)


def test_types::expression_constructor_exists():
    assert callable(types::Expression.__init__)


def test_types::expression_constructor_args():
    sig = inspect.signature(types::Expression.__init__)
    params = list(sig.parameters.keys())



def test_caselabel_is_not_abstract():
    assert not inspect.isabstract(CaseLabel)


def test_caselabel_constructor_exists():
    assert callable(CaseLabel.__init__)


def test_caselabel_constructor_args():
    sig = inspect.signature(CaseLabel.__init__)
    params = list(sig.parameters.keys())



def test_types::exprcaselabel_is_not_abstract():
    assert not inspect.isabstract(types::ExprCaseLabel)


def test_types::exprcaselabel_constructor_exists():
    assert callable(types::ExprCaseLabel.__init__)


def test_types::exprcaselabel_constructor_args():
    sig = inspect.signature(types::ExprCaseLabel.__init__)
    params = list(sig.parameters.keys())



def test_types::defaultcaselabel_is_not_abstract():
    assert not inspect.isabstract(types::DefaultCaseLabel)


def test_types::defaultcaselabel_constructor_exists():
    assert callable(types::DefaultCaseLabel.__init__)


def test_types::defaultcaselabel_constructor_args():
    sig = inspect.signature(types::DefaultCaseLabel.__init__)
    params = list(sig.parameters.keys())



def test_types::idltype_is_not_abstract():
    assert not inspect.isabstract(types::IdlType)


def test_types::idltype_constructor_exists():
    assert callable(types::IdlType.__init__)


def test_types::idltype_constructor_args():
    sig = inspect.signature(types::IdlType.__init__)
    params = list(sig.parameters.keys())



def test_fileregion_is_not_abstract():
    assert not inspect.isabstract(FileRegion)


def test_fileregion_constructor_exists():
    assert callable(FileRegion.__init__)


def test_fileregion_constructor_args():
    sig = inspect.signature(FileRegion.__init__)
    params = list(sig.parameters.keys())



def test_types::case_is_not_abstract():
    assert not inspect.isabstract(types::Case)


def test_types::case_constructor_exists():
    assert callable(types::Case.__init__)


def test_types::case_constructor_args():
    sig = inspect.signature(types::Case.__init__)
    params = list(sig.parameters.keys())



def test_types::caselabel_is_not_abstract():
    assert not inspect.isabstract(types::CaseLabel)


def test_types::caselabel_constructor_exists():
    assert callable(types::CaseLabel.__init__)


def test_types::caselabel_constructor_args():
    sig = inspect.signature(types::CaseLabel.__init__)
    params = list(sig.parameters.keys())



def test_types::elementspec_is_not_abstract():
    assert not inspect.isabstract(types::ElementSpec)


def test_types::elementspec_constructor_exists():
    assert callable(types::ElementSpec.__init__)


def test_types::elementspec_constructor_args():
    sig = inspect.signature(types::ElementSpec.__init__)
    params = list(sig.parameters.keys())



def test_types::switch_is_not_abstract():
    assert not inspect.isabstract(types::Switch)


def test_types::switch_constructor_exists():
    assert callable(types::Switch.__init__)


def test_types::switch_constructor_args():
    sig = inspect.signature(types::Switch.__init__)
    params = list(sig.parameters.keys())



def test_idltype_is_not_abstract():
    assert not inspect.isabstract(IdlType)


def test_idltype_constructor_exists():
    assert callable(IdlType.__init__)


def test_idltype_constructor_args():
    sig = inspect.signature(IdlType.__init__)
    params = list(sig.parameters.keys())



def test_types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(types::PrimitiveType)


def test_types::primitivetype_constructor_exists():
    assert callable(types::PrimitiveType.__init__)


def test_types::primitivetype_constructor_args():
    sig = inspect.signature(types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_types::templatetype_is_not_abstract():
    assert not inspect.isabstract(types::TemplateType)


def test_types::templatetype_constructor_exists():
    assert callable(types::TemplateType.__init__)


def test_types::templatetype_constructor_args():
    sig = inspect.signature(types::TemplateType.__init__)
    params = list(sig.parameters.keys())



def test_types::voidtype_is_not_abstract():
    assert not inspect.isabstract(types::VoidType)


def test_types::voidtype_constructor_exists():
    assert callable(types::VoidType.__init__)


def test_types::voidtype_constructor_args():
    sig = inspect.signature(types::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_idltypedcl_is_not_abstract():
    assert not inspect.isabstract(IdlTypeDcl)


def test_idltypedcl_constructor_exists():
    assert callable(IdlTypeDcl.__init__)


def test_idltypedcl_constructor_args():
    sig = inspect.signature(IdlTypeDcl.__init__)
    params = list(sig.parameters.keys())



def test_types::unionforwarddcl_is_not_abstract():
    assert not inspect.isabstract(types::UnionForwardDcl)


def test_types::unionforwarddcl_constructor_exists():
    assert callable(types::UnionForwardDcl.__init__)


def test_types::unionforwarddcl_constructor_args():
    sig = inspect.signature(types::UnionForwardDcl.__init__)
    params = list(sig.parameters.keys())



def test_types::structtype_is_not_abstract():
    assert not inspect.isabstract(types::StructType)


def test_types::structtype_constructor_exists():
    assert callable(types::StructType.__init__)


def test_types::structtype_constructor_args():
    sig = inspect.signature(types::StructType.__init__)
    params = list(sig.parameters.keys())



def test_types::enumtype_is_not_abstract():
    assert not inspect.isabstract(types::EnumType)


def test_types::enumtype_constructor_exists():
    assert callable(types::EnumType.__init__)


def test_types::enumtype_constructor_args():
    sig = inspect.signature(types::EnumType.__init__)
    params = list(sig.parameters.keys())



def test_types::uniontype_is_not_abstract():
    assert not inspect.isabstract(types::UnionType)


def test_types::uniontype_constructor_exists():
    assert callable(types::UnionType.__init__)


def test_types::uniontype_constructor_args():
    sig = inspect.signature(types::UnionType.__init__)
    params = list(sig.parameters.keys())



def test_types::structforwarddcl_is_not_abstract():
    assert not inspect.isabstract(types::StructForwardDcl)


def test_types::structforwarddcl_constructor_exists():
    assert callable(types::StructForwardDcl.__init__)


def test_types::structforwarddcl_constructor_args():
    sig = inspect.signature(types::StructForwardDcl.__init__)
    params = list(sig.parameters.keys())



def test_types::enumeration_is_not_abstract():
    assert not inspect.isabstract(types::Enumeration)


def test_types::enumeration_constructor_exists():
    assert callable(types::Enumeration.__init__)


def test_types::enumeration_constructor_args():
    sig = inspect.signature(types::Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_types::typedef_is_not_abstract():
    assert not inspect.isabstract(types::TypeDef)


def test_types::typedef_constructor_exists():
    assert callable(types::TypeDef.__init__)


def test_types::typedef_constructor_args():
    sig = inspect.signature(types::TypeDef.__init__)
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
Declarator_strategy = st.builds(
    Declarator,
)
types::ForwardDcl_strategy = st.builds(
    types::ForwardDcl,
)
MemberContainer_strategy = st.builds(
    MemberContainer,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
types::Any_strategy = st.builds(
    types::Any,
)
types::LongLong_strategy = st.builds(
    types::LongLong,
)
types::ValueBaseType_strategy = st.builds(
    types::ValueBaseType,
)
types::IdlObject_strategy = st.builds(
    types::IdlObject,
)
types::IdlChar_strategy = st.builds(
    types::IdlChar,
)
types::WChar_strategy = st.builds(
    types::WChar,
)
types::Double_strategy = st.builds(
    types::Double,
)
types::Float_strategy = st.builds(
    types::Float,
)
types::LongDouble_strategy = st.builds(
    types::LongDouble,
)
types::Octet_strategy = st.builds(
    types::Octet,
)
types::IdlWChar_strategy = st.builds(
    types::IdlWChar,
)
types::UShort_strategy = st.builds(
    types::UShort,
)
types::ULongLong_strategy = st.builds(
    types::ULongLong,
)
types::ULong_strategy = st.builds(
    types::ULong,
)
types::Boolean_strategy = st.builds(
    types::Boolean,
)
types::Long_strategy = st.builds(
    types::Long,
)
types::Short_strategy = st.builds(
    types::Short,
)
Typed_strategy = st.builds(
    Typed,
)
TemplateType_strategy = st.builds(
    TemplateType,
)
types::WString_strategy = st.builds(
    types::WString,
)
types::FixedPtType_strategy = st.builds(
    types::FixedPtType,
)
types::IdlString_strategy = st.builds(
    types::IdlString,
)
types::SequenceType_strategy = st.builds(
    types::SequenceType,
)
types::Declarator_strategy = st.builds(
    types::Declarator,
)
types::Expression_strategy = st.builds(
    types::Expression,
)
CaseLabel_strategy = st.builds(
    CaseLabel,
)
types::ExprCaseLabel_strategy = st.builds(
    types::ExprCaseLabel,
)
types::DefaultCaseLabel_strategy = st.builds(
    types::DefaultCaseLabel,
)
types::IdlType_strategy = st.builds(
    types::IdlType,
)
FileRegion_strategy = st.builds(
    FileRegion,
)
types::Case_strategy = st.builds(
    types::Case,
)
types::CaseLabel_strategy = st.builds(
    types::CaseLabel,
)
types::ElementSpec_strategy = st.builds(
    types::ElementSpec,
)
types::Switch_strategy = st.builds(
    types::Switch,
)
IdlType_strategy = st.builds(
    IdlType,
)
types::PrimitiveType_strategy = st.builds(
    types::PrimitiveType,
)
types::TemplateType_strategy = st.builds(
    types::TemplateType,
)
types::VoidType_strategy = st.builds(
    types::VoidType,
)
IdlTypeDcl_strategy = st.builds(
    IdlTypeDcl,
)
types::UnionForwardDcl_strategy = st.builds(
    types::UnionForwardDcl,
)
types::StructType_strategy = st.builds(
    types::StructType,
)
types::EnumType_strategy = st.builds(
    types::EnumType,
)
types::UnionType_strategy = st.builds(
    types::UnionType,
)
types::StructForwardDcl_strategy = st.builds(
    types::StructForwardDcl,
)
types::Enumeration_strategy = st.builds(
    types::Enumeration,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
types::TypeDef_strategy = st.builds(
    types::TypeDef,
)

@given(instance=Declarator_strategy)
@settings(max_examples=50)
def test_declarator_instantiation(instance):
    assert isinstance(instance, Declarator)

@given(instance=types::ForwardDcl_strategy)
@settings(max_examples=50)
def test_types::forwarddcl_instantiation(instance):
    assert isinstance(instance, types::ForwardDcl)

@given(instance=MemberContainer_strategy)
@settings(max_examples=50)
def test_membercontainer_instantiation(instance):
    assert isinstance(instance, MemberContainer)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=types::Any_strategy)
@settings(max_examples=50)
def test_types::any_instantiation(instance):
    assert isinstance(instance, types::Any)

@given(instance=types::LongLong_strategy)
@settings(max_examples=50)
def test_types::longlong_instantiation(instance):
    assert isinstance(instance, types::LongLong)

@given(instance=types::ValueBaseType_strategy)
@settings(max_examples=50)
def test_types::valuebasetype_instantiation(instance):
    assert isinstance(instance, types::ValueBaseType)

@given(instance=types::IdlObject_strategy)
@settings(max_examples=50)
def test_types::idlobject_instantiation(instance):
    assert isinstance(instance, types::IdlObject)

@given(instance=types::IdlChar_strategy)
@settings(max_examples=50)
def test_types::idlchar_instantiation(instance):
    assert isinstance(instance, types::IdlChar)

@given(instance=types::WChar_strategy)
@settings(max_examples=50)
def test_types::wchar_instantiation(instance):
    assert isinstance(instance, types::WChar)

@given(instance=types::Double_strategy)
@settings(max_examples=50)
def test_types::double_instantiation(instance):
    assert isinstance(instance, types::Double)

@given(instance=types::Float_strategy)
@settings(max_examples=50)
def test_types::float_instantiation(instance):
    assert isinstance(instance, types::Float)

@given(instance=types::LongDouble_strategy)
@settings(max_examples=50)
def test_types::longdouble_instantiation(instance):
    assert isinstance(instance, types::LongDouble)

@given(instance=types::Octet_strategy)
@settings(max_examples=50)
def test_types::octet_instantiation(instance):
    assert isinstance(instance, types::Octet)

@given(instance=types::IdlWChar_strategy)
@settings(max_examples=50)
def test_types::idlwchar_instantiation(instance):
    assert isinstance(instance, types::IdlWChar)

@given(instance=types::UShort_strategy)
@settings(max_examples=50)
def test_types::ushort_instantiation(instance):
    assert isinstance(instance, types::UShort)

@given(instance=types::ULongLong_strategy)
@settings(max_examples=50)
def test_types::ulonglong_instantiation(instance):
    assert isinstance(instance, types::ULongLong)

@given(instance=types::ULong_strategy)
@settings(max_examples=50)
def test_types::ulong_instantiation(instance):
    assert isinstance(instance, types::ULong)

@given(instance=types::Boolean_strategy)
@settings(max_examples=50)
def test_types::boolean_instantiation(instance):
    assert isinstance(instance, types::Boolean)

@given(instance=types::Long_strategy)
@settings(max_examples=50)
def test_types::long_instantiation(instance):
    assert isinstance(instance, types::Long)

@given(instance=types::Short_strategy)
@settings(max_examples=50)
def test_types::short_instantiation(instance):
    assert isinstance(instance, types::Short)

@given(instance=Typed_strategy)
@settings(max_examples=50)
def test_typed_instantiation(instance):
    assert isinstance(instance, Typed)

@given(instance=TemplateType_strategy)
@settings(max_examples=50)
def test_templatetype_instantiation(instance):
    assert isinstance(instance, TemplateType)

@given(instance=types::WString_strategy)
@settings(max_examples=50)
def test_types::wstring_instantiation(instance):
    assert isinstance(instance, types::WString)

@given(instance=types::FixedPtType_strategy)
@settings(max_examples=50)
def test_types::fixedpttype_instantiation(instance):
    assert isinstance(instance, types::FixedPtType)

@given(instance=types::IdlString_strategy)
@settings(max_examples=50)
def test_types::idlstring_instantiation(instance):
    assert isinstance(instance, types::IdlString)

@given(instance=types::SequenceType_strategy)
@settings(max_examples=50)
def test_types::sequencetype_instantiation(instance):
    assert isinstance(instance, types::SequenceType)

@given(instance=types::Declarator_strategy)
@settings(max_examples=50)
def test_types::declarator_instantiation(instance):
    assert isinstance(instance, types::Declarator)

@given(instance=types::Expression_strategy)
@settings(max_examples=50)
def test_types::expression_instantiation(instance):
    assert isinstance(instance, types::Expression)

@given(instance=CaseLabel_strategy)
@settings(max_examples=50)
def test_caselabel_instantiation(instance):
    assert isinstance(instance, CaseLabel)

@given(instance=types::ExprCaseLabel_strategy)
@settings(max_examples=50)
def test_types::exprcaselabel_instantiation(instance):
    assert isinstance(instance, types::ExprCaseLabel)

@given(instance=types::DefaultCaseLabel_strategy)
@settings(max_examples=50)
def test_types::defaultcaselabel_instantiation(instance):
    assert isinstance(instance, types::DefaultCaseLabel)

@given(instance=types::IdlType_strategy)
@settings(max_examples=50)
def test_types::idltype_instantiation(instance):
    assert isinstance(instance, types::IdlType)

@given(instance=FileRegion_strategy)
@settings(max_examples=50)
def test_fileregion_instantiation(instance):
    assert isinstance(instance, FileRegion)

@given(instance=types::Case_strategy)
@settings(max_examples=50)
def test_types::case_instantiation(instance):
    assert isinstance(instance, types::Case)

@given(instance=types::CaseLabel_strategy)
@settings(max_examples=50)
def test_types::caselabel_instantiation(instance):
    assert isinstance(instance, types::CaseLabel)

@given(instance=types::ElementSpec_strategy)
@settings(max_examples=50)
def test_types::elementspec_instantiation(instance):
    assert isinstance(instance, types::ElementSpec)

@given(instance=types::Switch_strategy)
@settings(max_examples=50)
def test_types::switch_instantiation(instance):
    assert isinstance(instance, types::Switch)

@given(instance=IdlType_strategy)
@settings(max_examples=50)
def test_idltype_instantiation(instance):
    assert isinstance(instance, IdlType)

@given(instance=types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_types::primitivetype_instantiation(instance):
    assert isinstance(instance, types::PrimitiveType)

@given(instance=types::TemplateType_strategy)
@settings(max_examples=50)
def test_types::templatetype_instantiation(instance):
    assert isinstance(instance, types::TemplateType)

@given(instance=types::VoidType_strategy)
@settings(max_examples=50)
def test_types::voidtype_instantiation(instance):
    assert isinstance(instance, types::VoidType)

@given(instance=IdlTypeDcl_strategy)
@settings(max_examples=50)
def test_idltypedcl_instantiation(instance):
    assert isinstance(instance, IdlTypeDcl)

@given(instance=types::UnionForwardDcl_strategy)
@settings(max_examples=50)
def test_types::unionforwarddcl_instantiation(instance):
    assert isinstance(instance, types::UnionForwardDcl)

@given(instance=types::StructType_strategy)
@settings(max_examples=50)
def test_types::structtype_instantiation(instance):
    assert isinstance(instance, types::StructType)

@given(instance=types::EnumType_strategy)
@settings(max_examples=50)
def test_types::enumtype_instantiation(instance):
    assert isinstance(instance, types::EnumType)

@given(instance=types::UnionType_strategy)
@settings(max_examples=50)
def test_types::uniontype_instantiation(instance):
    assert isinstance(instance, types::UnionType)

@given(instance=types::StructForwardDcl_strategy)
@settings(max_examples=50)
def test_types::structforwarddcl_instantiation(instance):
    assert isinstance(instance, types::StructForwardDcl)

@given(instance=types::Enumeration_strategy)
@settings(max_examples=50)
def test_types::enumeration_instantiation(instance):
    assert isinstance(instance, types::Enumeration)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=types::TypeDef_strategy)
@settings(max_examples=50)
def test_types::typedef_instantiation(instance):
    assert isinstance(instance, types::TypeDef)
