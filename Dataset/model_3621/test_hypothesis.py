import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tgg::Operator,
    tgg::EReference,
    tgg::NamedElements,
    tgg::OperatorPattern,
    tgg::ContextObjectVariablePattern,
    tgg::AttributeConstraint,
    tgg::AttributeAssignment,
    OperatorPattern,
    tgg::LinkVariablePattern,
    tgg::EObject,
    tgg::EEnumLiteral,
    tgg::EEnum,
    Expression,
    tgg::AttributeExpression,
    tgg::LiteralExpression,
    tgg::EnumExpression,
    tgg::EAttribute,
    tgg::ContextLinkVariablePattern,
    NamePattern,
    tgg::ObjectVariablePattern,
    tgg::CorrVariablePattern,
    ParamValue,
    tgg::Expression,
    tgg::LocalVariable,
    tgg::ParamValue,
    NamedElements,
    tgg::NamePattern,
    tgg::AttrCondDefLibrary,
    tgg::AttrCond,
    tgg::Nac,
    tgg::ComplementRule,
    tgg::EDataType,
    tgg::Adornment,
    tgg::Param,
    tgg::EClass,
    tgg::AttrCondDef,
    tgg::CorrType,
    tgg::EPackage,
    tgg::Rule,
    tgg::Schema,
    tgg::Using,
    tgg::Import,
    tgg::TripleGraphGrammarFile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tgg::operator_is_not_abstract():
    assert not inspect.isabstract(tgg::Operator)


def test_tgg::operator_constructor_exists():
    assert callable(tgg::Operator.__init__)


def test_tgg::operator_constructor_args():
    sig = inspect.signature(tgg::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tgg::operator_has_value():
    assert hasattr(tgg::Operator, "value")
    descriptor = None
    for klass in tgg::Operator.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tgg::ereference_is_not_abstract():
    assert not inspect.isabstract(tgg::EReference)


def test_tgg::ereference_constructor_exists():
    assert callable(tgg::EReference.__init__)


def test_tgg::ereference_constructor_args():
    sig = inspect.signature(tgg::EReference.__init__)
    params = list(sig.parameters.keys())



def test_tgg::namedelements_is_not_abstract():
    assert not inspect.isabstract(tgg::NamedElements)


def test_tgg::namedelements_constructor_exists():
    assert callable(tgg::NamedElements.__init__)


def test_tgg::namedelements_constructor_args():
    sig = inspect.signature(tgg::NamedElements.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tgg::namedelements_has_name():
    assert hasattr(tgg::NamedElements, "name")
    descriptor = None
    for klass in tgg::NamedElements.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tgg::operatorpattern_is_not_abstract():
    assert not inspect.isabstract(tgg::OperatorPattern)


def test_tgg::operatorpattern_constructor_exists():
    assert callable(tgg::OperatorPattern.__init__)


def test_tgg::operatorpattern_constructor_args():
    sig = inspect.signature(tgg::OperatorPattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::contextobjectvariablepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::ContextObjectVariablePattern)


def test_tgg::contextobjectvariablepattern_constructor_exists():
    assert callable(tgg::ContextObjectVariablePattern.__init__)


def test_tgg::contextobjectvariablepattern_constructor_args():
    sig = inspect.signature(tgg::ContextObjectVariablePattern.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tgg::contextobjectvariablepattern_has_name():
    assert hasattr(tgg::ContextObjectVariablePattern, "name")
    descriptor = None
    for klass in tgg::ContextObjectVariablePattern.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tgg::attributeconstraint_is_not_abstract():
    assert not inspect.isabstract(tgg::AttributeConstraint)


def test_tgg::attributeconstraint_constructor_exists():
    assert callable(tgg::AttributeConstraint.__init__)


def test_tgg::attributeconstraint_constructor_args():
    sig = inspect.signature(tgg::AttributeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tgg::attributeconstraint_has_op():
    assert hasattr(tgg::AttributeConstraint, "op")
    descriptor = None
    for klass in tgg::AttributeConstraint.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tgg::attributeassignment_is_not_abstract():
    assert not inspect.isabstract(tgg::AttributeAssignment)


def test_tgg::attributeassignment_constructor_exists():
    assert callable(tgg::AttributeAssignment.__init__)


def test_tgg::attributeassignment_constructor_args():
    sig = inspect.signature(tgg::AttributeAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tgg::attributeassignment_has_op():
    assert hasattr(tgg::AttributeAssignment, "op")
    descriptor = None
    for klass in tgg::AttributeAssignment.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_operatorpattern_is_not_abstract():
    assert not inspect.isabstract(OperatorPattern)


def test_operatorpattern_constructor_exists():
    assert callable(OperatorPattern.__init__)


def test_operatorpattern_constructor_args():
    sig = inspect.signature(OperatorPattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::linkvariablepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::LinkVariablePattern)


def test_tgg::linkvariablepattern_constructor_exists():
    assert callable(tgg::LinkVariablePattern.__init__)


def test_tgg::linkvariablepattern_constructor_args():
    sig = inspect.signature(tgg::LinkVariablePattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::eobject_is_not_abstract():
    assert not inspect.isabstract(tgg::EObject)


def test_tgg::eobject_constructor_exists():
    assert callable(tgg::EObject.__init__)


def test_tgg::eobject_constructor_args():
    sig = inspect.signature(tgg::EObject.__init__)
    params = list(sig.parameters.keys())



def test_tgg::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(tgg::EEnumLiteral)


def test_tgg::eenumliteral_constructor_exists():
    assert callable(tgg::EEnumLiteral.__init__)


def test_tgg::eenumliteral_constructor_args():
    sig = inspect.signature(tgg::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_tgg::eenum_is_not_abstract():
    assert not inspect.isabstract(tgg::EEnum)


def test_tgg::eenum_constructor_exists():
    assert callable(tgg::EEnum.__init__)


def test_tgg::eenum_constructor_args():
    sig = inspect.signature(tgg::EEnum.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_tgg::attributeexpression_is_not_abstract():
    assert not inspect.isabstract(tgg::AttributeExpression)


def test_tgg::attributeexpression_constructor_exists():
    assert callable(tgg::AttributeExpression.__init__)


def test_tgg::attributeexpression_constructor_args():
    sig = inspect.signature(tgg::AttributeExpression.__init__)
    params = list(sig.parameters.keys())



def test_tgg::literalexpression_is_not_abstract():
    assert not inspect.isabstract(tgg::LiteralExpression)


def test_tgg::literalexpression_constructor_exists():
    assert callable(tgg::LiteralExpression.__init__)


def test_tgg::literalexpression_constructor_args():
    sig = inspect.signature(tgg::LiteralExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tgg::literalexpression_has_value():
    assert hasattr(tgg::LiteralExpression, "value")
    descriptor = None
    for klass in tgg::LiteralExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tgg::enumexpression_is_not_abstract():
    assert not inspect.isabstract(tgg::EnumExpression)


def test_tgg::enumexpression_constructor_exists():
    assert callable(tgg::EnumExpression.__init__)


def test_tgg::enumexpression_constructor_args():
    sig = inspect.signature(tgg::EnumExpression.__init__)
    params = list(sig.parameters.keys())



def test_tgg::eattribute_is_not_abstract():
    assert not inspect.isabstract(tgg::EAttribute)


def test_tgg::eattribute_constructor_exists():
    assert callable(tgg::EAttribute.__init__)


def test_tgg::eattribute_constructor_args():
    sig = inspect.signature(tgg::EAttribute.__init__)
    params = list(sig.parameters.keys())



def test_tgg::contextlinkvariablepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::ContextLinkVariablePattern)


def test_tgg::contextlinkvariablepattern_constructor_exists():
    assert callable(tgg::ContextLinkVariablePattern.__init__)


def test_tgg::contextlinkvariablepattern_constructor_args():
    sig = inspect.signature(tgg::ContextLinkVariablePattern.__init__)
    params = list(sig.parameters.keys())



def test_namepattern_is_not_abstract():
    assert not inspect.isabstract(NamePattern)


def test_namepattern_constructor_exists():
    assert callable(NamePattern.__init__)


def test_namepattern_constructor_args():
    sig = inspect.signature(NamePattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::objectvariablepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::ObjectVariablePattern)


def test_tgg::objectvariablepattern_constructor_exists():
    assert callable(tgg::ObjectVariablePattern.__init__)


def test_tgg::objectvariablepattern_constructor_args():
    sig = inspect.signature(tgg::ObjectVariablePattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::corrvariablepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::CorrVariablePattern)


def test_tgg::corrvariablepattern_constructor_exists():
    assert callable(tgg::CorrVariablePattern.__init__)


def test_tgg::corrvariablepattern_constructor_args():
    sig = inspect.signature(tgg::CorrVariablePattern.__init__)
    params = list(sig.parameters.keys())



def test_paramvalue_is_not_abstract():
    assert not inspect.isabstract(ParamValue)


def test_paramvalue_constructor_exists():
    assert callable(ParamValue.__init__)


def test_paramvalue_constructor_args():
    sig = inspect.signature(ParamValue.__init__)
    params = list(sig.parameters.keys())



def test_tgg::expression_is_not_abstract():
    assert not inspect.isabstract(tgg::Expression)


def test_tgg::expression_constructor_exists():
    assert callable(tgg::Expression.__init__)


def test_tgg::expression_constructor_args():
    sig = inspect.signature(tgg::Expression.__init__)
    params = list(sig.parameters.keys())



def test_tgg::localvariable_is_not_abstract():
    assert not inspect.isabstract(tgg::LocalVariable)


def test_tgg::localvariable_constructor_exists():
    assert callable(tgg::LocalVariable.__init__)


def test_tgg::localvariable_constructor_args():
    sig = inspect.signature(tgg::LocalVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tgg::localvariable_has_name():
    assert hasattr(tgg::LocalVariable, "name")
    descriptor = None
    for klass in tgg::LocalVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tgg::paramvalue_is_not_abstract():
    assert not inspect.isabstract(tgg::ParamValue)


def test_tgg::paramvalue_constructor_exists():
    assert callable(tgg::ParamValue.__init__)


def test_tgg::paramvalue_constructor_args():
    sig = inspect.signature(tgg::ParamValue.__init__)
    params = list(sig.parameters.keys())



def test_namedelements_is_not_abstract():
    assert not inspect.isabstract(NamedElements)


def test_namedelements_constructor_exists():
    assert callable(NamedElements.__init__)


def test_namedelements_constructor_args():
    sig = inspect.signature(NamedElements.__init__)
    params = list(sig.parameters.keys())



def test_tgg::namepattern_is_not_abstract():
    assert not inspect.isabstract(tgg::NamePattern)


def test_tgg::namepattern_constructor_exists():
    assert callable(tgg::NamePattern.__init__)


def test_tgg::namepattern_constructor_args():
    sig = inspect.signature(tgg::NamePattern.__init__)
    params = list(sig.parameters.keys())



def test_tgg::attrconddeflibrary_is_not_abstract():
    assert not inspect.isabstract(tgg::AttrCondDefLibrary)


def test_tgg::attrconddeflibrary_constructor_exists():
    assert callable(tgg::AttrCondDefLibrary.__init__)


def test_tgg::attrconddeflibrary_constructor_args():
    sig = inspect.signature(tgg::AttrCondDefLibrary.__init__)
    params = list(sig.parameters.keys())



def test_tgg::attrcond_is_not_abstract():
    assert not inspect.isabstract(tgg::AttrCond)


def test_tgg::attrcond_constructor_exists():
    assert callable(tgg::AttrCond.__init__)


def test_tgg::attrcond_constructor_args():
    sig = inspect.signature(tgg::AttrCond.__init__)
    params = list(sig.parameters.keys())



def test_tgg::nac_is_not_abstract():
    assert not inspect.isabstract(tgg::Nac)


def test_tgg::nac_constructor_exists():
    assert callable(tgg::Nac.__init__)


def test_tgg::nac_constructor_args():
    sig = inspect.signature(tgg::Nac.__init__)
    params = list(sig.parameters.keys())



def test_tgg::complementrule_is_not_abstract():
    assert not inspect.isabstract(tgg::ComplementRule)


def test_tgg::complementrule_constructor_exists():
    assert callable(tgg::ComplementRule.__init__)


def test_tgg::complementrule_constructor_args():
    sig = inspect.signature(tgg::ComplementRule.__init__)
    params = list(sig.parameters.keys())



def test_tgg::edatatype_is_not_abstract():
    assert not inspect.isabstract(tgg::EDataType)


def test_tgg::edatatype_constructor_exists():
    assert callable(tgg::EDataType.__init__)


def test_tgg::edatatype_constructor_args():
    sig = inspect.signature(tgg::EDataType.__init__)
    params = list(sig.parameters.keys())



def test_tgg::adornment_is_not_abstract():
    assert not inspect.isabstract(tgg::Adornment)


def test_tgg::adornment_constructor_exists():
    assert callable(tgg::Adornment.__init__)


def test_tgg::adornment_constructor_args():
    sig = inspect.signature(tgg::Adornment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tgg::adornment_has_value():
    assert hasattr(tgg::Adornment, "value")
    descriptor = None
    for klass in tgg::Adornment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tgg::param_is_not_abstract():
    assert not inspect.isabstract(tgg::Param)


def test_tgg::param_constructor_exists():
    assert callable(tgg::Param.__init__)


def test_tgg::param_constructor_args():
    sig = inspect.signature(tgg::Param.__init__)
    params = list(sig.parameters.keys())
    assert "paramName" in params, "Missing parameter 'paramName'"

def test_tgg::param_has_paramName():
    assert hasattr(tgg::Param, "paramName")
    descriptor = None
    for klass in tgg::Param.__mro__:
        if "paramName" in klass.__dict__:
            descriptor = klass.__dict__["paramName"]
            break
    assert isinstance(descriptor, property)



def test_tgg::eclass_is_not_abstract():
    assert not inspect.isabstract(tgg::EClass)


def test_tgg::eclass_constructor_exists():
    assert callable(tgg::EClass.__init__)


def test_tgg::eclass_constructor_args():
    sig = inspect.signature(tgg::EClass.__init__)
    params = list(sig.parameters.keys())



def test_tgg::attrconddef_is_not_abstract():
    assert not inspect.isabstract(tgg::AttrCondDef)


def test_tgg::attrconddef_constructor_exists():
    assert callable(tgg::AttrCondDef.__init__)


def test_tgg::attrconddef_constructor_args():
    sig = inspect.signature(tgg::AttrCondDef.__init__)
    params = list(sig.parameters.keys())
    assert "userDefined" in params, "Missing parameter 'userDefined'"

def test_tgg::attrconddef_has_userDefined():
    assert hasattr(tgg::AttrCondDef, "userDefined")
    descriptor = None
    for klass in tgg::AttrCondDef.__mro__:
        if "userDefined" in klass.__dict__:
            descriptor = klass.__dict__["userDefined"]
            break
    assert isinstance(descriptor, property)



def test_tgg::corrtype_is_not_abstract():
    assert not inspect.isabstract(tgg::CorrType)


def test_tgg::corrtype_constructor_exists():
    assert callable(tgg::CorrType.__init__)


def test_tgg::corrtype_constructor_args():
    sig = inspect.signature(tgg::CorrType.__init__)
    params = list(sig.parameters.keys())



def test_tgg::epackage_is_not_abstract():
    assert not inspect.isabstract(tgg::EPackage)


def test_tgg::epackage_constructor_exists():
    assert callable(tgg::EPackage.__init__)


def test_tgg::epackage_constructor_args():
    sig = inspect.signature(tgg::EPackage.__init__)
    params = list(sig.parameters.keys())



def test_tgg::rule_is_not_abstract():
    assert not inspect.isabstract(tgg::Rule)


def test_tgg::rule_constructor_exists():
    assert callable(tgg::Rule.__init__)


def test_tgg::rule_constructor_args():
    sig = inspect.signature(tgg::Rule.__init__)
    params = list(sig.parameters.keys())
    assert "abstractRule" in params, "Missing parameter 'abstractRule'"

def test_tgg::rule_has_abstractRule():
    assert hasattr(tgg::Rule, "abstractRule")
    descriptor = None
    for klass in tgg::Rule.__mro__:
        if "abstractRule" in klass.__dict__:
            descriptor = klass.__dict__["abstractRule"]
            break
    assert isinstance(descriptor, property)



def test_tgg::schema_is_not_abstract():
    assert not inspect.isabstract(tgg::Schema)


def test_tgg::schema_constructor_exists():
    assert callable(tgg::Schema.__init__)


def test_tgg::schema_constructor_args():
    sig = inspect.signature(tgg::Schema.__init__)
    params = list(sig.parameters.keys())



def test_tgg::using_is_not_abstract():
    assert not inspect.isabstract(tgg::Using)


def test_tgg::using_constructor_exists():
    assert callable(tgg::Using.__init__)


def test_tgg::using_constructor_args():
    sig = inspect.signature(tgg::Using.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_tgg::using_has_importedNamespace():
    assert hasattr(tgg::Using, "importedNamespace")
    descriptor = None
    for klass in tgg::Using.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_tgg::import_is_not_abstract():
    assert not inspect.isabstract(tgg::Import)


def test_tgg::import_constructor_exists():
    assert callable(tgg::Import.__init__)


def test_tgg::import_constructor_args():
    sig = inspect.signature(tgg::Import.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tgg::import_has_name():
    assert hasattr(tgg::Import, "name")
    descriptor = None
    for klass in tgg::Import.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tgg::triplegraphgrammarfile_is_not_abstract():
    assert not inspect.isabstract(tgg::TripleGraphGrammarFile)


def test_tgg::triplegraphgrammarfile_constructor_exists():
    assert callable(tgg::TripleGraphGrammarFile.__init__)


def test_tgg::triplegraphgrammarfile_constructor_args():
    sig = inspect.signature(tgg::TripleGraphGrammarFile.__init__)
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
tgg::Operator_strategy = st.builds(
    tgg::Operator,
    value=
        safe_text
)
tgg::EReference_strategy = st.builds(
    tgg::EReference,
)
tgg::NamedElements_strategy = st.builds(
    tgg::NamedElements,
    name=
        safe_text
)
tgg::OperatorPattern_strategy = st.builds(
    tgg::OperatorPattern,
)
tgg::ContextObjectVariablePattern_strategy = st.builds(
    tgg::ContextObjectVariablePattern,
    name=
        safe_text
)
tgg::AttributeConstraint_strategy = st.builds(
    tgg::AttributeConstraint,
    op=
        safe_text
)
tgg::AttributeAssignment_strategy = st.builds(
    tgg::AttributeAssignment,
    op=
        safe_text
)
OperatorPattern_strategy = st.builds(
    OperatorPattern,
)
tgg::LinkVariablePattern_strategy = st.builds(
    tgg::LinkVariablePattern,
)
tgg::EObject_strategy = st.builds(
    tgg::EObject,
)
tgg::EEnumLiteral_strategy = st.builds(
    tgg::EEnumLiteral,
)
tgg::EEnum_strategy = st.builds(
    tgg::EEnum,
)
Expression_strategy = st.builds(
    Expression,
)
tgg::AttributeExpression_strategy = st.builds(
    tgg::AttributeExpression,
)
tgg::LiteralExpression_strategy = st.builds(
    tgg::LiteralExpression,
    value=
        safe_text
)
tgg::EnumExpression_strategy = st.builds(
    tgg::EnumExpression,
)
tgg::EAttribute_strategy = st.builds(
    tgg::EAttribute,
)
tgg::ContextLinkVariablePattern_strategy = st.builds(
    tgg::ContextLinkVariablePattern,
)
NamePattern_strategy = st.builds(
    NamePattern,
)
tgg::ObjectVariablePattern_strategy = st.builds(
    tgg::ObjectVariablePattern,
)
tgg::CorrVariablePattern_strategy = st.builds(
    tgg::CorrVariablePattern,
)
ParamValue_strategy = st.builds(
    ParamValue,
)
tgg::Expression_strategy = st.builds(
    tgg::Expression,
)
tgg::LocalVariable_strategy = st.builds(
    tgg::LocalVariable,
    name=
        safe_text
)
tgg::ParamValue_strategy = st.builds(
    tgg::ParamValue,
)
NamedElements_strategy = st.builds(
    NamedElements,
)
tgg::NamePattern_strategy = st.builds(
    tgg::NamePattern,
)
tgg::AttrCondDefLibrary_strategy = st.builds(
    tgg::AttrCondDefLibrary,
)
tgg::AttrCond_strategy = st.builds(
    tgg::AttrCond,
)
tgg::Nac_strategy = st.builds(
    tgg::Nac,
)
tgg::ComplementRule_strategy = st.builds(
    tgg::ComplementRule,
)
tgg::EDataType_strategy = st.builds(
    tgg::EDataType,
)
tgg::Adornment_strategy = st.builds(
    tgg::Adornment,
    value=
        safe_text
)
tgg::Param_strategy = st.builds(
    tgg::Param,
    paramName=
        safe_text
)
tgg::EClass_strategy = st.builds(
    tgg::EClass,
)
tgg::AttrCondDef_strategy = st.builds(
    tgg::AttrCondDef,
    userDefined=
        st.booleans()
)
tgg::CorrType_strategy = st.builds(
    tgg::CorrType,
)
tgg::EPackage_strategy = st.builds(
    tgg::EPackage,
)
tgg::Rule_strategy = st.builds(
    tgg::Rule,
    abstractRule=
        st.booleans()
)
tgg::Schema_strategy = st.builds(
    tgg::Schema,
)
tgg::Using_strategy = st.builds(
    tgg::Using,
    importedNamespace=
        safe_text
)
tgg::Import_strategy = st.builds(
    tgg::Import,
    name=
        safe_text
)
tgg::TripleGraphGrammarFile_strategy = st.builds(
    tgg::TripleGraphGrammarFile,
)

@given(instance=tgg::Operator_strategy)
@settings(max_examples=50)
def test_tgg::operator_instantiation(instance):
    assert isinstance(instance, tgg::Operator)

@given(instance=tgg::Operator_strategy)
def test_tgg::operator_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tgg::Operator_strategy)
def test_tgg::operator_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tgg::EReference_strategy)
@settings(max_examples=50)
def test_tgg::ereference_instantiation(instance):
    assert isinstance(instance, tgg::EReference)

@given(instance=tgg::NamedElements_strategy)
@settings(max_examples=50)
def test_tgg::namedelements_instantiation(instance):
    assert isinstance(instance, tgg::NamedElements)

@given(instance=tgg::NamedElements_strategy)
def test_tgg::namedelements_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tgg::NamedElements_strategy)
def test_tgg::namedelements_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tgg::OperatorPattern_strategy)
@settings(max_examples=50)
def test_tgg::operatorpattern_instantiation(instance):
    assert isinstance(instance, tgg::OperatorPattern)

@given(instance=tgg::ContextObjectVariablePattern_strategy)
@settings(max_examples=50)
def test_tgg::contextobjectvariablepattern_instantiation(instance):
    assert isinstance(instance, tgg::ContextObjectVariablePattern)

@given(instance=tgg::ContextObjectVariablePattern_strategy)
def test_tgg::contextobjectvariablepattern_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tgg::ContextObjectVariablePattern_strategy)
def test_tgg::contextobjectvariablepattern_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tgg::AttributeConstraint_strategy)
@settings(max_examples=50)
def test_tgg::attributeconstraint_instantiation(instance):
    assert isinstance(instance, tgg::AttributeConstraint)

@given(instance=tgg::AttributeConstraint_strategy)
def test_tgg::attributeconstraint_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tgg::AttributeConstraint_strategy)
def test_tgg::attributeconstraint_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tgg::AttributeAssignment_strategy)
@settings(max_examples=50)
def test_tgg::attributeassignment_instantiation(instance):
    assert isinstance(instance, tgg::AttributeAssignment)

@given(instance=tgg::AttributeAssignment_strategy)
def test_tgg::attributeassignment_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tgg::AttributeAssignment_strategy)
def test_tgg::attributeassignment_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=OperatorPattern_strategy)
@settings(max_examples=50)
def test_operatorpattern_instantiation(instance):
    assert isinstance(instance, OperatorPattern)

@given(instance=tgg::LinkVariablePattern_strategy)
@settings(max_examples=50)
def test_tgg::linkvariablepattern_instantiation(instance):
    assert isinstance(instance, tgg::LinkVariablePattern)

@given(instance=tgg::EObject_strategy)
@settings(max_examples=50)
def test_tgg::eobject_instantiation(instance):
    assert isinstance(instance, tgg::EObject)

@given(instance=tgg::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_tgg::eenumliteral_instantiation(instance):
    assert isinstance(instance, tgg::EEnumLiteral)

@given(instance=tgg::EEnum_strategy)
@settings(max_examples=50)
def test_tgg::eenum_instantiation(instance):
    assert isinstance(instance, tgg::EEnum)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=tgg::AttributeExpression_strategy)
@settings(max_examples=50)
def test_tgg::attributeexpression_instantiation(instance):
    assert isinstance(instance, tgg::AttributeExpression)

@given(instance=tgg::LiteralExpression_strategy)
@settings(max_examples=50)
def test_tgg::literalexpression_instantiation(instance):
    assert isinstance(instance, tgg::LiteralExpression)

@given(instance=tgg::LiteralExpression_strategy)
def test_tgg::literalexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tgg::LiteralExpression_strategy)
def test_tgg::literalexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tgg::EnumExpression_strategy)
@settings(max_examples=50)
def test_tgg::enumexpression_instantiation(instance):
    assert isinstance(instance, tgg::EnumExpression)

@given(instance=tgg::EAttribute_strategy)
@settings(max_examples=50)
def test_tgg::eattribute_instantiation(instance):
    assert isinstance(instance, tgg::EAttribute)

@given(instance=tgg::ContextLinkVariablePattern_strategy)
@settings(max_examples=50)
def test_tgg::contextlinkvariablepattern_instantiation(instance):
    assert isinstance(instance, tgg::ContextLinkVariablePattern)

@given(instance=NamePattern_strategy)
@settings(max_examples=50)
def test_namepattern_instantiation(instance):
    assert isinstance(instance, NamePattern)

@given(instance=tgg::ObjectVariablePattern_strategy)
@settings(max_examples=50)
def test_tgg::objectvariablepattern_instantiation(instance):
    assert isinstance(instance, tgg::ObjectVariablePattern)

@given(instance=tgg::CorrVariablePattern_strategy)
@settings(max_examples=50)
def test_tgg::corrvariablepattern_instantiation(instance):
    assert isinstance(instance, tgg::CorrVariablePattern)

@given(instance=ParamValue_strategy)
@settings(max_examples=50)
def test_paramvalue_instantiation(instance):
    assert isinstance(instance, ParamValue)

@given(instance=tgg::Expression_strategy)
@settings(max_examples=50)
def test_tgg::expression_instantiation(instance):
    assert isinstance(instance, tgg::Expression)

@given(instance=tgg::LocalVariable_strategy)
@settings(max_examples=50)
def test_tgg::localvariable_instantiation(instance):
    assert isinstance(instance, tgg::LocalVariable)

@given(instance=tgg::LocalVariable_strategy)
def test_tgg::localvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tgg::LocalVariable_strategy)
def test_tgg::localvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tgg::ParamValue_strategy)
@settings(max_examples=50)
def test_tgg::paramvalue_instantiation(instance):
    assert isinstance(instance, tgg::ParamValue)

@given(instance=NamedElements_strategy)
@settings(max_examples=50)
def test_namedelements_instantiation(instance):
    assert isinstance(instance, NamedElements)

@given(instance=tgg::NamePattern_strategy)
@settings(max_examples=50)
def test_tgg::namepattern_instantiation(instance):
    assert isinstance(instance, tgg::NamePattern)

@given(instance=tgg::AttrCondDefLibrary_strategy)
@settings(max_examples=50)
def test_tgg::attrconddeflibrary_instantiation(instance):
    assert isinstance(instance, tgg::AttrCondDefLibrary)

@given(instance=tgg::AttrCond_strategy)
@settings(max_examples=50)
def test_tgg::attrcond_instantiation(instance):
    assert isinstance(instance, tgg::AttrCond)

@given(instance=tgg::Nac_strategy)
@settings(max_examples=50)
def test_tgg::nac_instantiation(instance):
    assert isinstance(instance, tgg::Nac)

@given(instance=tgg::ComplementRule_strategy)
@settings(max_examples=50)
def test_tgg::complementrule_instantiation(instance):
    assert isinstance(instance, tgg::ComplementRule)

@given(instance=tgg::EDataType_strategy)
@settings(max_examples=50)
def test_tgg::edatatype_instantiation(instance):
    assert isinstance(instance, tgg::EDataType)

@given(instance=tgg::Adornment_strategy)
@settings(max_examples=50)
def test_tgg::adornment_instantiation(instance):
    assert isinstance(instance, tgg::Adornment)

@given(instance=tgg::Adornment_strategy)
def test_tgg::adornment_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tgg::Adornment_strategy)
def test_tgg::adornment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tgg::Param_strategy)
@settings(max_examples=50)
def test_tgg::param_instantiation(instance):
    assert isinstance(instance, tgg::Param)

@given(instance=tgg::Param_strategy)
def test_tgg::param_paramName_type(instance):
    assert isinstance(instance.paramName, str)


@given(instance=tgg::Param_strategy)
def test_tgg::param_paramName_setter(instance):
    original = instance.paramName
    instance.paramName = original
    assert instance.paramName == original

@given(instance=tgg::EClass_strategy)
@settings(max_examples=50)
def test_tgg::eclass_instantiation(instance):
    assert isinstance(instance, tgg::EClass)

@given(instance=tgg::AttrCondDef_strategy)
@settings(max_examples=50)
def test_tgg::attrconddef_instantiation(instance):
    assert isinstance(instance, tgg::AttrCondDef)

@given(instance=tgg::AttrCondDef_strategy)
def test_tgg::attrconddef_userDefined_type(instance):
    assert isinstance(instance.userDefined, bool)


@given(instance=tgg::AttrCondDef_strategy)
def test_tgg::attrconddef_userDefined_setter(instance):
    original = instance.userDefined
    instance.userDefined = original
    assert instance.userDefined == original

@given(instance=tgg::CorrType_strategy)
@settings(max_examples=50)
def test_tgg::corrtype_instantiation(instance):
    assert isinstance(instance, tgg::CorrType)

@given(instance=tgg::EPackage_strategy)
@settings(max_examples=50)
def test_tgg::epackage_instantiation(instance):
    assert isinstance(instance, tgg::EPackage)

@given(instance=tgg::Rule_strategy)
@settings(max_examples=50)
def test_tgg::rule_instantiation(instance):
    assert isinstance(instance, tgg::Rule)

@given(instance=tgg::Rule_strategy)
def test_tgg::rule_abstractRule_type(instance):
    assert isinstance(instance.abstractRule, bool)


@given(instance=tgg::Rule_strategy)
def test_tgg::rule_abstractRule_setter(instance):
    original = instance.abstractRule
    instance.abstractRule = original
    assert instance.abstractRule == original

@given(instance=tgg::Schema_strategy)
@settings(max_examples=50)
def test_tgg::schema_instantiation(instance):
    assert isinstance(instance, tgg::Schema)

@given(instance=tgg::Using_strategy)
@settings(max_examples=50)
def test_tgg::using_instantiation(instance):
    assert isinstance(instance, tgg::Using)

@given(instance=tgg::Using_strategy)
def test_tgg::using_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=tgg::Using_strategy)
def test_tgg::using_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=tgg::Import_strategy)
@settings(max_examples=50)
def test_tgg::import_instantiation(instance):
    assert isinstance(instance, tgg::Import)

@given(instance=tgg::Import_strategy)
def test_tgg::import_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tgg::Import_strategy)
def test_tgg::import_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tgg::TripleGraphGrammarFile_strategy)
@settings(max_examples=50)
def test_tgg::triplegraphgrammarfile_instantiation(instance):
    assert isinstance(instance, tgg::TripleGraphGrammarFile)
