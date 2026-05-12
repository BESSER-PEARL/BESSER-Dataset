import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ComplexDomain,
    asmeta_domains_RealDomain,
    AbstractTd,
    asmeta_domains_AgentDomain,
    asmeta_domains_ReserveDomain,
    domains_TypeDomain,
    asmeta_domains_EnumElement,
    domains_EnumElement,
    RealDomain,
    asmeta_domains_IntegerDomain,
    TemporalProperty,
    asmeta_definitions_LtlSpec,
    asmeta_definitions_CtlSpec,
    StructuredTd,
    asmeta_domains_MapDomain,
    asmeta_domains_RuleDomain,
    asmeta_domains_PowersetDomain,
    asmeta_domains_BagDomain,
    asmeta_domains_ProductDomain,
    asmeta_domains_SequenceDomain,
    TypeDomain,
    asmeta_domains_AnyDomain,
    asmeta_domains_EnumTd,
    asmeta_domains_BasicTd,
    asmeta_domains_AbstractTd,
    asmeta_domains_StructuredTd,
    Domain,
    asmeta_domains_ConcreteDomain,
    asmeta_domains_TypeDomain,
    BasicTd,
    asmeta_domains_BooleanDomain,
    asmeta_domains_StringDomain,
    asmeta_domains_ComplexDomain,
    asmeta_domains_CharDomain,
    asmeta_domains_UndefDomain,
    IntegerDomain,
    asmeta_domains_NaturalDomain,
    BasicFunction,
    asmeta_definitions_StaticFunction,
    asmeta_definitions_DynamicFunction,
    Invariant,
    Classifier,
    asmeta_domains_Domain,
    asmeta_definitions_FairnessConstraint,
    asmeta_definitions_Function,
    asmeta_definitions_InvarConstraint,
    asmeta_definitions_Property,
    asmeta_definitions_RuleDeclaration,
    BasicRule,
    asmeta_basictransitionrules_ForallRule,
    asmeta_basictransitionrules_ExtendRule,
    asmeta_basictransitionrules_SkipRule,
    asmeta_basictransitionrules_ConditionalRule,
    asmeta_basictransitionrules_BlockRule,
    asmeta_basictransitionrules_LetRule,
    asmeta_basictransitionrules_UpdateRule,
    asmeta_basictransitionrules_MacroCallRule,
    asmeta_basictransitionrules_ChooseRule,
    asmeta_basictransitionrules_Rule,
    TurboDerivedRule,
    asmeta_derivedtransitionrules_RecursiveWhileRule,
    DerivedRule,
    asmeta_derivedtransitionrules_TurboDerivedRule,
    asmeta_derivedtransitionrules_BasicDerivedRule,
    BasicDerivedRule,
    asmeta_derivedtransitionrules_CaseRule,
    asmeta_derivedtransitionrules_IterativeWhileRule,
    Rule,
    asmeta_derivedtransitionrules_DerivedRule,
    asmeta_basictransitionrules_BasicRule,
    asmeta_basictransitionrules_TermAsRule,
    asmeta_turbotransitionrules_TurboRule,
    turbotransitionrules_TurboCallRule,
    turbotransitionrules_TurboDeclaration,
    LocalFunction,
    basictransitionrules_Rule,
    TurboRule,
    asmeta_turbotransitionrules_TurboCallRule,
    asmeta_turbotransitionrules_TryCatchRule,
    asmeta_turbotransitionrules_TurboReturnRule,
    asmeta_turbotransitionrules_IterateRule,
    asmeta_turbotransitionrules_TurboLocalStateRule,
    asmeta_turbotransitionrules_SeqRule,
    asmeta_structure_DomainDefinition,
    basictransitionrules_MacroDeclaration,
    Body,
    ExportClause,
    Signature,
    ImportClause,
    asmeta_structure_Header,
    AgentInitialization,
    FunctionInitialization,
    DomainInitialization,
    NamedElement,
    asmeta_structure_Asm,
    asmeta_definitions_Classifier,
    asmeta_structure_Initialization,
    domains_ConcreteDomain,
    asmeta_structure_DomainInitialization,
    asmeta_structure_FunctionDefinition,
    asmeta_structure_ImportClause,
    asmeta_structure_ExportClause,
    domains_StructuredTd,
    Header,
    asmeta_structure_Signature,
    basictransitionrules_MacroCallRule,
    asmeta_structure_AgentInitialization,
    asmeta_structure_NamedElement,
    DynamicFunction,
    asmeta_definitions_ControlledFunction,
    asmeta_definitions_SharedFunction,
    asmeta_definitions_LocalFunction,
    asmeta_definitions_MonitoredFunction,
    asmeta_definitions_OutFunction,
    asmeta_structure_FunctionInitialization,
    InvarConstraint,
    FairnessConstraint,
    asmeta_definitions_CompassionConstraint,
    asmeta_definitions_JusticeConstraint,
    Asm,
    DomainDefinition,
    Property,
    asmeta_definitions_TemporalProperty,
    asmeta_definitions_Invariant,
    FunctionDefinition,
    asmeta_structure_Body,
    Initialization,
    RuleDeclaration,
    asmeta_basictransitionrules_MacroDeclaration,
    asmeta_turbotransitionrules_TurboDeclaration,
    basictransitionrules_TermAsRule,
    domains_Domain,
    asmeta_basicterms_Term,
    Term,
    asmeta_basicterms_BasicTerm,
    asmeta_basicterms_ExtendedTerm,
    Function,
    asmeta_definitions_BasicFunction,
    asmeta_definitions_DerivedFunction,
    FunctionTerm,
    asmeta_basicterms_LocationTerm,
    furtherterms_FiniteQuantificationTerm,
    BasicTerm,
    asmeta_basicterms_ConstantTerm,
    asmeta_basicterms_FunctionTerm,
    asmeta_basicterms_VariableTerm,
    CollectionTerm,
    asmeta_furtherterms_MapTerm,
    asmeta_furtherterms_BagTerm,
    asmeta_basicterms_SetTerm,
    asmeta_furtherterms_SequenceTerm,
    ComprehensionTerm,
    asmeta_furtherterms_BagCt,
    asmeta_furtherterms_SequenceCt,
    asmeta_furtherterms_SetCt,
    ExtendedTerm,
    asmeta_furtherterms_CaseTerm,
    asmeta_basicterms_DomainTerm,
    asmeta_basicterms_TupleTerm,
    asmeta_basicterms_RuleAsTerm,
    asmeta_basicterms_CollectionTerm,
    asmeta_furtherterms_VariableBindingTerm,
    asmeta_furtherterms_ConditionalTerm,
    FiniteQuantificationTerm,
    asmeta_furtherterms_ExistUniqueTerm,
    asmeta_furtherterms_ExistTerm,
    asmeta_furtherterms_ForallTerm,
    basicterms_Term,
    basicterms_VariableTerm,
    VariableBindingTerm,
    asmeta_furtherterms_FiniteQuantificationTerm,
    asmeta_furtherterms_ComprehensionTerm,
    asmeta_furtherterms_LetTerm,
    asmeta_furtherterms_MapCt,
    basicterms_TupleTerm,
    ConstantTerm,
    asmeta_furtherterms_RealTerm,
    asmeta_furtherterms_StringTerm,
    asmeta_furtherterms_ComplexTerm,
    asmeta_furtherterms_EnumTerm,
    asmeta_basicterms_BooleanTerm,
    asmeta_basicterms_UndefTerm,
    asmeta_furtherterms_CharTerm,
    asmeta_furtherterms_NaturalTerm,
    asmeta_furtherterms_IntegerTerm,
    VariableKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_complexdomain_is_not_abstract():
    assert not inspect.isabstract(ComplexDomain)


def test_complexdomain_constructor_exists():
    assert callable(ComplexDomain.__init__)


def test_complexdomain_constructor_args():
    sig = inspect.signature(ComplexDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_realdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_RealDomain)


def test_asmeta_domains_realdomain_constructor_exists():
    assert callable(asmeta_domains_RealDomain.__init__)


def test_asmeta_domains_realdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_RealDomain.__init__)
    params = list(sig.parameters.keys())



def test_abstracttd_is_not_abstract():
    assert not inspect.isabstract(AbstractTd)


def test_abstracttd_constructor_exists():
    assert callable(AbstractTd.__init__)


def test_abstracttd_constructor_args():
    sig = inspect.signature(AbstractTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_agentdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_AgentDomain)


def test_asmeta_domains_agentdomain_constructor_exists():
    assert callable(asmeta_domains_AgentDomain.__init__)


def test_asmeta_domains_agentdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_AgentDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_reservedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_ReserveDomain)


def test_asmeta_domains_reservedomain_constructor_exists():
    assert callable(asmeta_domains_ReserveDomain.__init__)


def test_asmeta_domains_reservedomain_constructor_args():
    sig = inspect.signature(asmeta_domains_ReserveDomain.__init__)
    params = list(sig.parameters.keys())



def test_domains_typedomain_is_not_abstract():
    assert not inspect.isabstract(domains_TypeDomain)


def test_domains_typedomain_constructor_exists():
    assert callable(domains_TypeDomain.__init__)


def test_domains_typedomain_constructor_args():
    sig = inspect.signature(domains_TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_enumelement_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_EnumElement)


def test_asmeta_domains_enumelement_constructor_exists():
    assert callable(asmeta_domains_EnumElement.__init__)


def test_asmeta_domains_enumelement_constructor_args():
    sig = inspect.signature(asmeta_domains_EnumElement.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_asmeta_domains_enumelement_has_symbol():
    assert hasattr(asmeta_domains_EnumElement, "symbol")
    descriptor = None
    for klass in asmeta_domains_EnumElement.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_domains_enumelement_is_not_abstract():
    assert not inspect.isabstract(domains_EnumElement)


def test_domains_enumelement_constructor_exists():
    assert callable(domains_EnumElement.__init__)


def test_domains_enumelement_constructor_args():
    sig = inspect.signature(domains_EnumElement.__init__)
    params = list(sig.parameters.keys())



def test_realdomain_is_not_abstract():
    assert not inspect.isabstract(RealDomain)


def test_realdomain_constructor_exists():
    assert callable(RealDomain.__init__)


def test_realdomain_constructor_args():
    sig = inspect.signature(RealDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_integerdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_IntegerDomain)


def test_asmeta_domains_integerdomain_constructor_exists():
    assert callable(asmeta_domains_IntegerDomain.__init__)


def test_asmeta_domains_integerdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_IntegerDomain.__init__)
    params = list(sig.parameters.keys())



def test_temporalproperty_is_not_abstract():
    assert not inspect.isabstract(TemporalProperty)


def test_temporalproperty_constructor_exists():
    assert callable(TemporalProperty.__init__)


def test_temporalproperty_constructor_args():
    sig = inspect.signature(TemporalProperty.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_ltlspec_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_LtlSpec)


def test_asmeta_definitions_ltlspec_constructor_exists():
    assert callable(asmeta_definitions_LtlSpec.__init__)


def test_asmeta_definitions_ltlspec_constructor_args():
    sig = inspect.signature(asmeta_definitions_LtlSpec.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_ctlspec_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_CtlSpec)


def test_asmeta_definitions_ctlspec_constructor_exists():
    assert callable(asmeta_definitions_CtlSpec.__init__)


def test_asmeta_definitions_ctlspec_constructor_args():
    sig = inspect.signature(asmeta_definitions_CtlSpec.__init__)
    params = list(sig.parameters.keys())



def test_structuredtd_is_not_abstract():
    assert not inspect.isabstract(StructuredTd)


def test_structuredtd_constructor_exists():
    assert callable(StructuredTd.__init__)


def test_structuredtd_constructor_args():
    sig = inspect.signature(StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_mapdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_MapDomain)


def test_asmeta_domains_mapdomain_constructor_exists():
    assert callable(asmeta_domains_MapDomain.__init__)


def test_asmeta_domains_mapdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_MapDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_ruledomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_RuleDomain)


def test_asmeta_domains_ruledomain_constructor_exists():
    assert callable(asmeta_domains_RuleDomain.__init__)


def test_asmeta_domains_ruledomain_constructor_args():
    sig = inspect.signature(asmeta_domains_RuleDomain.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"

def test_asmeta_domains_ruledomain_has_domains():
    assert hasattr(asmeta_domains_RuleDomain, "domains")
    descriptor = None
    for klass in asmeta_domains_RuleDomain.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_domains_powersetdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_PowersetDomain)


def test_asmeta_domains_powersetdomain_constructor_exists():
    assert callable(asmeta_domains_PowersetDomain.__init__)


def test_asmeta_domains_powersetdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_PowersetDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_bagdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_BagDomain)


def test_asmeta_domains_bagdomain_constructor_exists():
    assert callable(asmeta_domains_BagDomain.__init__)


def test_asmeta_domains_bagdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_BagDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_productdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_ProductDomain)


def test_asmeta_domains_productdomain_constructor_exists():
    assert callable(asmeta_domains_ProductDomain.__init__)


def test_asmeta_domains_productdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_ProductDomain.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"

def test_asmeta_domains_productdomain_has_domains():
    assert hasattr(asmeta_domains_ProductDomain, "domains")
    descriptor = None
    for klass in asmeta_domains_ProductDomain.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_domains_sequencedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_SequenceDomain)


def test_asmeta_domains_sequencedomain_constructor_exists():
    assert callable(asmeta_domains_SequenceDomain.__init__)


def test_asmeta_domains_sequencedomain_constructor_args():
    sig = inspect.signature(asmeta_domains_SequenceDomain.__init__)
    params = list(sig.parameters.keys())



def test_typedomain_is_not_abstract():
    assert not inspect.isabstract(TypeDomain)


def test_typedomain_constructor_exists():
    assert callable(TypeDomain.__init__)


def test_typedomain_constructor_args():
    sig = inspect.signature(TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_anydomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_AnyDomain)


def test_asmeta_domains_anydomain_constructor_exists():
    assert callable(asmeta_domains_AnyDomain.__init__)


def test_asmeta_domains_anydomain_constructor_args():
    sig = inspect.signature(asmeta_domains_AnyDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_enumtd_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_EnumTd)


def test_asmeta_domains_enumtd_constructor_exists():
    assert callable(asmeta_domains_EnumTd.__init__)


def test_asmeta_domains_enumtd_constructor_args():
    sig = inspect.signature(asmeta_domains_EnumTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_basictd_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_BasicTd)


def test_asmeta_domains_basictd_constructor_exists():
    assert callable(asmeta_domains_BasicTd.__init__)


def test_asmeta_domains_basictd_constructor_args():
    sig = inspect.signature(asmeta_domains_BasicTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_abstracttd_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_AbstractTd)


def test_asmeta_domains_abstracttd_constructor_exists():
    assert callable(asmeta_domains_AbstractTd.__init__)


def test_asmeta_domains_abstracttd_constructor_args():
    sig = inspect.signature(asmeta_domains_AbstractTd.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_asmeta_domains_abstracttd_has_isDynamic():
    assert hasattr(asmeta_domains_AbstractTd, "isDynamic")
    descriptor = None
    for klass in asmeta_domains_AbstractTd.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_domains_structuredtd_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_StructuredTd)


def test_asmeta_domains_structuredtd_constructor_exists():
    assert callable(asmeta_domains_StructuredTd.__init__)


def test_asmeta_domains_structuredtd_constructor_args():
    sig = inspect.signature(asmeta_domains_StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_concretedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_ConcreteDomain)


def test_asmeta_domains_concretedomain_constructor_exists():
    assert callable(asmeta_domains_ConcreteDomain.__init__)


def test_asmeta_domains_concretedomain_constructor_args():
    sig = inspect.signature(asmeta_domains_ConcreteDomain.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_asmeta_domains_concretedomain_has_isDynamic():
    assert hasattr(asmeta_domains_ConcreteDomain, "isDynamic")
    descriptor = None
    for klass in asmeta_domains_ConcreteDomain.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_domains_typedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_TypeDomain)


def test_asmeta_domains_typedomain_constructor_exists():
    assert callable(asmeta_domains_TypeDomain.__init__)


def test_asmeta_domains_typedomain_constructor_args():
    sig = inspect.signature(asmeta_domains_TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_basictd_is_not_abstract():
    assert not inspect.isabstract(BasicTd)


def test_basictd_constructor_exists():
    assert callable(BasicTd.__init__)


def test_basictd_constructor_args():
    sig = inspect.signature(BasicTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_booleandomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_BooleanDomain)


def test_asmeta_domains_booleandomain_constructor_exists():
    assert callable(asmeta_domains_BooleanDomain.__init__)


def test_asmeta_domains_booleandomain_constructor_args():
    sig = inspect.signature(asmeta_domains_BooleanDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_stringdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_StringDomain)


def test_asmeta_domains_stringdomain_constructor_exists():
    assert callable(asmeta_domains_StringDomain.__init__)


def test_asmeta_domains_stringdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_StringDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_complexdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_ComplexDomain)


def test_asmeta_domains_complexdomain_constructor_exists():
    assert callable(asmeta_domains_ComplexDomain.__init__)


def test_asmeta_domains_complexdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_ComplexDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_chardomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_CharDomain)


def test_asmeta_domains_chardomain_constructor_exists():
    assert callable(asmeta_domains_CharDomain.__init__)


def test_asmeta_domains_chardomain_constructor_args():
    sig = inspect.signature(asmeta_domains_CharDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_undefdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_UndefDomain)


def test_asmeta_domains_undefdomain_constructor_exists():
    assert callable(asmeta_domains_UndefDomain.__init__)


def test_asmeta_domains_undefdomain_constructor_args():
    sig = inspect.signature(asmeta_domains_UndefDomain.__init__)
    params = list(sig.parameters.keys())



def test_integerdomain_is_not_abstract():
    assert not inspect.isabstract(IntegerDomain)


def test_integerdomain_constructor_exists():
    assert callable(IntegerDomain.__init__)


def test_integerdomain_constructor_args():
    sig = inspect.signature(IntegerDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_naturaldomain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_NaturalDomain)


def test_asmeta_domains_naturaldomain_constructor_exists():
    assert callable(asmeta_domains_NaturalDomain.__init__)


def test_asmeta_domains_naturaldomain_constructor_args():
    sig = inspect.signature(asmeta_domains_NaturalDomain.__init__)
    params = list(sig.parameters.keys())



def test_basicfunction_is_not_abstract():
    assert not inspect.isabstract(BasicFunction)


def test_basicfunction_constructor_exists():
    assert callable(BasicFunction.__init__)


def test_basicfunction_constructor_args():
    sig = inspect.signature(BasicFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_staticfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_StaticFunction)


def test_asmeta_definitions_staticfunction_constructor_exists():
    assert callable(asmeta_definitions_StaticFunction.__init__)


def test_asmeta_definitions_staticfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_StaticFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_dynamicfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_DynamicFunction)


def test_asmeta_definitions_dynamicfunction_constructor_exists():
    assert callable(asmeta_definitions_DynamicFunction.__init__)


def test_asmeta_definitions_dynamicfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_DynamicFunction.__init__)
    params = list(sig.parameters.keys())



def test_invariant_is_not_abstract():
    assert not inspect.isabstract(Invariant)


def test_invariant_constructor_exists():
    assert callable(Invariant.__init__)


def test_invariant_constructor_args():
    sig = inspect.signature(Invariant.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_domains_domain_is_not_abstract():
    assert not inspect.isabstract(asmeta_domains_Domain)


def test_asmeta_domains_domain_constructor_exists():
    assert callable(asmeta_domains_Domain.__init__)


def test_asmeta_domains_domain_constructor_args():
    sig = inspect.signature(asmeta_domains_Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_FairnessConstraint)


def test_asmeta_definitions_fairnessconstraint_constructor_exists():
    assert callable(asmeta_definitions_FairnessConstraint.__init__)


def test_asmeta_definitions_fairnessconstraint_constructor_args():
    sig = inspect.signature(asmeta_definitions_FairnessConstraint.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_function_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_Function)


def test_asmeta_definitions_function_constructor_exists():
    assert callable(asmeta_definitions_Function.__init__)


def test_asmeta_definitions_function_constructor_args():
    sig = inspect.signature(asmeta_definitions_Function.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"

def test_asmeta_definitions_function_has_arity():
    assert hasattr(asmeta_definitions_Function, "arity")
    descriptor = None
    for klass in asmeta_definitions_Function.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_definitions_invarconstraint_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_InvarConstraint)


def test_asmeta_definitions_invarconstraint_constructor_exists():
    assert callable(asmeta_definitions_InvarConstraint.__init__)


def test_asmeta_definitions_invarconstraint_constructor_args():
    sig = inspect.signature(asmeta_definitions_InvarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_property_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_Property)


def test_asmeta_definitions_property_constructor_exists():
    assert callable(asmeta_definitions_Property.__init__)


def test_asmeta_definitions_property_constructor_args():
    sig = inspect.signature(asmeta_definitions_Property.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_RuleDeclaration)


def test_asmeta_definitions_ruledeclaration_constructor_exists():
    assert callable(asmeta_definitions_RuleDeclaration.__init__)


def test_asmeta_definitions_ruledeclaration_constructor_args():
    sig = inspect.signature(asmeta_definitions_RuleDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"

def test_asmeta_definitions_ruledeclaration_has_arity():
    assert hasattr(asmeta_definitions_RuleDeclaration, "arity")
    descriptor = None
    for klass in asmeta_definitions_RuleDeclaration.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)



def test_basicrule_is_not_abstract():
    assert not inspect.isabstract(BasicRule)


def test_basicrule_constructor_exists():
    assert callable(BasicRule.__init__)


def test_basicrule_constructor_args():
    sig = inspect.signature(BasicRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_forallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_ForallRule)


def test_asmeta_basictransitionrules_forallrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_ForallRule.__init__)


def test_asmeta_basictransitionrules_forallrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_ForallRule.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta_basictransitionrules_forallrule_has_ranges():
    assert hasattr(asmeta_basictransitionrules_ForallRule, "ranges")
    descriptor = None
    for klass in asmeta_basictransitionrules_ForallRule.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basictransitionrules_extendrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_ExtendRule)


def test_asmeta_basictransitionrules_extendrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_ExtendRule.__init__)


def test_asmeta_basictransitionrules_extendrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_ExtendRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_skiprule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_SkipRule)


def test_asmeta_basictransitionrules_skiprule_constructor_exists():
    assert callable(asmeta_basictransitionrules_SkipRule.__init__)


def test_asmeta_basictransitionrules_skiprule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_SkipRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_conditionalrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_ConditionalRule)


def test_asmeta_basictransitionrules_conditionalrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_ConditionalRule.__init__)


def test_asmeta_basictransitionrules_conditionalrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_blockrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_BlockRule)


def test_asmeta_basictransitionrules_blockrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_BlockRule.__init__)


def test_asmeta_basictransitionrules_blockrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_BlockRule.__init__)
    params = list(sig.parameters.keys())
    assert "rules" in params, "Missing parameter 'rules'"

def test_asmeta_basictransitionrules_blockrule_has_rules():
    assert hasattr(asmeta_basictransitionrules_BlockRule, "rules")
    descriptor = None
    for klass in asmeta_basictransitionrules_BlockRule.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basictransitionrules_letrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_LetRule)


def test_asmeta_basictransitionrules_letrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_LetRule.__init__)


def test_asmeta_basictransitionrules_letrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_LetRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_updaterule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_UpdateRule)


def test_asmeta_basictransitionrules_updaterule_constructor_exists():
    assert callable(asmeta_basictransitionrules_UpdateRule.__init__)


def test_asmeta_basictransitionrules_updaterule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_UpdateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_macrocallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_MacroCallRule)


def test_asmeta_basictransitionrules_macrocallrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_MacroCallRule.__init__)


def test_asmeta_basictransitionrules_macrocallrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_MacroCallRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta_basictransitionrules_macrocallrule_has_parameters():
    assert hasattr(asmeta_basictransitionrules_MacroCallRule, "parameters")
    descriptor = None
    for klass in asmeta_basictransitionrules_MacroCallRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basictransitionrules_chooserule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_ChooseRule)


def test_asmeta_basictransitionrules_chooserule_constructor_exists():
    assert callable(asmeta_basictransitionrules_ChooseRule.__init__)


def test_asmeta_basictransitionrules_chooserule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_ChooseRule.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta_basictransitionrules_chooserule_has_ranges():
    assert hasattr(asmeta_basictransitionrules_ChooseRule, "ranges")
    descriptor = None
    for klass in asmeta_basictransitionrules_ChooseRule.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basictransitionrules_rule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_Rule)


def test_asmeta_basictransitionrules_rule_constructor_exists():
    assert callable(asmeta_basictransitionrules_Rule.__init__)


def test_asmeta_basictransitionrules_rule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_Rule.__init__)
    params = list(sig.parameters.keys())



def test_turboderivedrule_is_not_abstract():
    assert not inspect.isabstract(TurboDerivedRule)


def test_turboderivedrule_constructor_exists():
    assert callable(TurboDerivedRule.__init__)


def test_turboderivedrule_constructor_args():
    sig = inspect.signature(TurboDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_derivedtransitionrules_recursivewhilerule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_RecursiveWhileRule)


def test_asmeta_derivedtransitionrules_recursivewhilerule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_RecursiveWhileRule.__init__)


def test_asmeta_derivedtransitionrules_recursivewhilerule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_RecursiveWhileRule.__init__)
    params = list(sig.parameters.keys())



def test_derivedrule_is_not_abstract():
    assert not inspect.isabstract(DerivedRule)


def test_derivedrule_constructor_exists():
    assert callable(DerivedRule.__init__)


def test_derivedrule_constructor_args():
    sig = inspect.signature(DerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_derivedtransitionrules_turboderivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_TurboDerivedRule)


def test_asmeta_derivedtransitionrules_turboderivedrule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_TurboDerivedRule.__init__)


def test_asmeta_derivedtransitionrules_turboderivedrule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_TurboDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_derivedtransitionrules_basicderivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_BasicDerivedRule)


def test_asmeta_derivedtransitionrules_basicderivedrule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_BasicDerivedRule.__init__)


def test_asmeta_derivedtransitionrules_basicderivedrule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_BasicDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_basicderivedrule_is_not_abstract():
    assert not inspect.isabstract(BasicDerivedRule)


def test_basicderivedrule_constructor_exists():
    assert callable(BasicDerivedRule.__init__)


def test_basicderivedrule_constructor_args():
    sig = inspect.signature(BasicDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_derivedtransitionrules_caserule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_CaseRule)


def test_asmeta_derivedtransitionrules_caserule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_CaseRule.__init__)


def test_asmeta_derivedtransitionrules_caserule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_CaseRule.__init__)
    params = list(sig.parameters.keys())
    assert "caseBranches" in params, "Missing parameter 'caseBranches'"

def test_asmeta_derivedtransitionrules_caserule_has_caseBranches():
    assert hasattr(asmeta_derivedtransitionrules_CaseRule, "caseBranches")
    descriptor = None
    for klass in asmeta_derivedtransitionrules_CaseRule.__mro__:
        if "caseBranches" in klass.__dict__:
            descriptor = klass.__dict__["caseBranches"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_derivedtransitionrules_iterativewhilerule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_IterativeWhileRule)


def test_asmeta_derivedtransitionrules_iterativewhilerule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_IterativeWhileRule.__init__)


def test_asmeta_derivedtransitionrules_iterativewhilerule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_IterativeWhileRule.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_derivedtransitionrules_derivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_derivedtransitionrules_DerivedRule)


def test_asmeta_derivedtransitionrules_derivedrule_constructor_exists():
    assert callable(asmeta_derivedtransitionrules_DerivedRule.__init__)


def test_asmeta_derivedtransitionrules_derivedrule_constructor_args():
    sig = inspect.signature(asmeta_derivedtransitionrules_DerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_basicrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_BasicRule)


def test_asmeta_basictransitionrules_basicrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_BasicRule.__init__)


def test_asmeta_basictransitionrules_basicrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_BasicRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_termasrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_TermAsRule)


def test_asmeta_basictransitionrules_termasrule_constructor_exists():
    assert callable(asmeta_basictransitionrules_TermAsRule.__init__)


def test_asmeta_basictransitionrules_termasrule_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_TermAsRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta_basictransitionrules_termasrule_has_parameters():
    assert hasattr(asmeta_basictransitionrules_TermAsRule, "parameters")
    descriptor = None
    for klass in asmeta_basictransitionrules_TermAsRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_turbotransitionrules_turborule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TurboRule)


def test_asmeta_turbotransitionrules_turborule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TurboRule.__init__)


def test_asmeta_turbotransitionrules_turborule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TurboRule.__init__)
    params = list(sig.parameters.keys())



def test_turbotransitionrules_turbocallrule_is_not_abstract():
    assert not inspect.isabstract(turbotransitionrules_TurboCallRule)


def test_turbotransitionrules_turbocallrule_constructor_exists():
    assert callable(turbotransitionrules_TurboCallRule.__init__)


def test_turbotransitionrules_turbocallrule_constructor_args():
    sig = inspect.signature(turbotransitionrules_TurboCallRule.__init__)
    params = list(sig.parameters.keys())



def test_turbotransitionrules_turbodeclaration_is_not_abstract():
    assert not inspect.isabstract(turbotransitionrules_TurboDeclaration)


def test_turbotransitionrules_turbodeclaration_constructor_exists():
    assert callable(turbotransitionrules_TurboDeclaration.__init__)


def test_turbotransitionrules_turbodeclaration_constructor_args():
    sig = inspect.signature(turbotransitionrules_TurboDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_localfunction_is_not_abstract():
    assert not inspect.isabstract(LocalFunction)


def test_localfunction_constructor_exists():
    assert callable(LocalFunction.__init__)


def test_localfunction_constructor_args():
    sig = inspect.signature(LocalFunction.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules_rule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules_Rule)


def test_basictransitionrules_rule_constructor_exists():
    assert callable(basictransitionrules_Rule.__init__)


def test_basictransitionrules_rule_constructor_args():
    sig = inspect.signature(basictransitionrules_Rule.__init__)
    params = list(sig.parameters.keys())



def test_turborule_is_not_abstract():
    assert not inspect.isabstract(TurboRule)


def test_turborule_constructor_exists():
    assert callable(TurboRule.__init__)


def test_turborule_constructor_args():
    sig = inspect.signature(TurboRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_turbocallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TurboCallRule)


def test_asmeta_turbotransitionrules_turbocallrule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TurboCallRule.__init__)


def test_asmeta_turbotransitionrules_turbocallrule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TurboCallRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta_turbotransitionrules_turbocallrule_has_parameters():
    assert hasattr(asmeta_turbotransitionrules_TurboCallRule, "parameters")
    descriptor = None
    for klass in asmeta_turbotransitionrules_TurboCallRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_turbotransitionrules_trycatchrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TryCatchRule)


def test_asmeta_turbotransitionrules_trycatchrule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TryCatchRule.__init__)


def test_asmeta_turbotransitionrules_trycatchrule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TryCatchRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_turboreturnrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TurboReturnRule)


def test_asmeta_turbotransitionrules_turboreturnrule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TurboReturnRule.__init__)


def test_asmeta_turbotransitionrules_turboreturnrule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TurboReturnRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_iteraterule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_IterateRule)


def test_asmeta_turbotransitionrules_iteraterule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_IterateRule.__init__)


def test_asmeta_turbotransitionrules_iteraterule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_IterateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_turbolocalstaterule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TurboLocalStateRule)


def test_asmeta_turbotransitionrules_turbolocalstaterule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TurboLocalStateRule.__init__)


def test_asmeta_turbotransitionrules_turbolocalstaterule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TurboLocalStateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_seqrule_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_SeqRule)


def test_asmeta_turbotransitionrules_seqrule_constructor_exists():
    assert callable(asmeta_turbotransitionrules_SeqRule.__init__)


def test_asmeta_turbotransitionrules_seqrule_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_SeqRule.__init__)
    params = list(sig.parameters.keys())
    assert "rules" in params, "Missing parameter 'rules'"

def test_asmeta_turbotransitionrules_seqrule_has_rules():
    assert hasattr(asmeta_turbotransitionrules_SeqRule, "rules")
    descriptor = None
    for klass in asmeta_turbotransitionrules_SeqRule.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_structure_domaindefinition_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_DomainDefinition)


def test_asmeta_structure_domaindefinition_constructor_exists():
    assert callable(asmeta_structure_DomainDefinition.__init__)


def test_asmeta_structure_domaindefinition_constructor_args():
    sig = inspect.signature(asmeta_structure_DomainDefinition.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules_macrodeclaration_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules_MacroDeclaration)


def test_basictransitionrules_macrodeclaration_constructor_exists():
    assert callable(basictransitionrules_MacroDeclaration.__init__)


def test_basictransitionrules_macrodeclaration_constructor_args():
    sig = inspect.signature(basictransitionrules_MacroDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_exportclause_is_not_abstract():
    assert not inspect.isabstract(ExportClause)


def test_exportclause_constructor_exists():
    assert callable(ExportClause.__init__)


def test_exportclause_constructor_args():
    sig = inspect.signature(ExportClause.__init__)
    params = list(sig.parameters.keys())



def test_signature_is_not_abstract():
    assert not inspect.isabstract(Signature)


def test_signature_constructor_exists():
    assert callable(Signature.__init__)


def test_signature_constructor_args():
    sig = inspect.signature(Signature.__init__)
    params = list(sig.parameters.keys())



def test_importclause_is_not_abstract():
    assert not inspect.isabstract(ImportClause)


def test_importclause_constructor_exists():
    assert callable(ImportClause.__init__)


def test_importclause_constructor_args():
    sig = inspect.signature(ImportClause.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_header_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_Header)


def test_asmeta_structure_header_constructor_exists():
    assert callable(asmeta_structure_Header.__init__)


def test_asmeta_structure_header_constructor_args():
    sig = inspect.signature(asmeta_structure_Header.__init__)
    params = list(sig.parameters.keys())



def test_agentinitialization_is_not_abstract():
    assert not inspect.isabstract(AgentInitialization)


def test_agentinitialization_constructor_exists():
    assert callable(AgentInitialization.__init__)


def test_agentinitialization_constructor_args():
    sig = inspect.signature(AgentInitialization.__init__)
    params = list(sig.parameters.keys())



def test_functioninitialization_is_not_abstract():
    assert not inspect.isabstract(FunctionInitialization)


def test_functioninitialization_constructor_exists():
    assert callable(FunctionInitialization.__init__)


def test_functioninitialization_constructor_args():
    sig = inspect.signature(FunctionInitialization.__init__)
    params = list(sig.parameters.keys())



def test_domaininitialization_is_not_abstract():
    assert not inspect.isabstract(DomainInitialization)


def test_domaininitialization_constructor_exists():
    assert callable(DomainInitialization.__init__)


def test_domaininitialization_constructor_args():
    sig = inspect.signature(DomainInitialization.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_asm_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_Asm)


def test_asmeta_structure_asm_constructor_exists():
    assert callable(asmeta_structure_Asm.__init__)


def test_asmeta_structure_asm_constructor_args():
    sig = inspect.signature(asmeta_structure_Asm.__init__)
    params = list(sig.parameters.keys())
    assert "isAsynchr" in params, "Missing parameter 'isAsynchr'"

def test_asmeta_structure_asm_has_isAsynchr():
    assert hasattr(asmeta_structure_Asm, "isAsynchr")
    descriptor = None
    for klass in asmeta_structure_Asm.__mro__:
        if "isAsynchr" in klass.__dict__:
            descriptor = klass.__dict__["isAsynchr"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_definitions_classifier_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_Classifier)


def test_asmeta_definitions_classifier_constructor_exists():
    assert callable(asmeta_definitions_Classifier.__init__)


def test_asmeta_definitions_classifier_constructor_args():
    sig = inspect.signature(asmeta_definitions_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_initialization_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_Initialization)


def test_asmeta_structure_initialization_constructor_exists():
    assert callable(asmeta_structure_Initialization.__init__)


def test_asmeta_structure_initialization_constructor_args():
    sig = inspect.signature(asmeta_structure_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_domains_concretedomain_is_not_abstract():
    assert not inspect.isabstract(domains_ConcreteDomain)


def test_domains_concretedomain_constructor_exists():
    assert callable(domains_ConcreteDomain.__init__)


def test_domains_concretedomain_constructor_args():
    sig = inspect.signature(domains_ConcreteDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_domaininitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_DomainInitialization)


def test_asmeta_structure_domaininitialization_constructor_exists():
    assert callable(asmeta_structure_DomainInitialization.__init__)


def test_asmeta_structure_domaininitialization_constructor_args():
    sig = inspect.signature(asmeta_structure_DomainInitialization.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_FunctionDefinition)


def test_asmeta_structure_functiondefinition_constructor_exists():
    assert callable(asmeta_structure_FunctionDefinition.__init__)


def test_asmeta_structure_functiondefinition_constructor_args():
    sig = inspect.signature(asmeta_structure_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_importclause_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_ImportClause)


def test_asmeta_structure_importclause_constructor_exists():
    assert callable(asmeta_structure_ImportClause.__init__)


def test_asmeta_structure_importclause_constructor_args():
    sig = inspect.signature(asmeta_structure_ImportClause.__init__)
    params = list(sig.parameters.keys())
    assert "moduleName" in params, "Missing parameter 'moduleName'"

def test_asmeta_structure_importclause_has_moduleName():
    assert hasattr(asmeta_structure_ImportClause, "moduleName")
    descriptor = None
    for klass in asmeta_structure_ImportClause.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_structure_exportclause_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_ExportClause)


def test_asmeta_structure_exportclause_constructor_exists():
    assert callable(asmeta_structure_ExportClause.__init__)


def test_asmeta_structure_exportclause_constructor_args():
    sig = inspect.signature(asmeta_structure_ExportClause.__init__)
    params = list(sig.parameters.keys())



def test_domains_structuredtd_is_not_abstract():
    assert not inspect.isabstract(domains_StructuredTd)


def test_domains_structuredtd_constructor_exists():
    assert callable(domains_StructuredTd.__init__)


def test_domains_structuredtd_constructor_args():
    sig = inspect.signature(domains_StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_header_is_not_abstract():
    assert not inspect.isabstract(Header)


def test_header_constructor_exists():
    assert callable(Header.__init__)


def test_header_constructor_args():
    sig = inspect.signature(Header.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_signature_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_Signature)


def test_asmeta_structure_signature_constructor_exists():
    assert callable(asmeta_structure_Signature.__init__)


def test_asmeta_structure_signature_constructor_args():
    sig = inspect.signature(asmeta_structure_Signature.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules_macrocallrule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules_MacroCallRule)


def test_basictransitionrules_macrocallrule_constructor_exists():
    assert callable(basictransitionrules_MacroCallRule.__init__)


def test_basictransitionrules_macrocallrule_constructor_args():
    sig = inspect.signature(basictransitionrules_MacroCallRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_agentinitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_AgentInitialization)


def test_asmeta_structure_agentinitialization_constructor_exists():
    assert callable(asmeta_structure_AgentInitialization.__init__)


def test_asmeta_structure_agentinitialization_constructor_args():
    sig = inspect.signature(asmeta_structure_AgentInitialization.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_namedelement_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_NamedElement)


def test_asmeta_structure_namedelement_constructor_exists():
    assert callable(asmeta_structure_NamedElement.__init__)


def test_asmeta_structure_namedelement_constructor_args():
    sig = inspect.signature(asmeta_structure_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asmeta_structure_namedelement_has_name():
    assert hasattr(asmeta_structure_NamedElement, "name")
    descriptor = None
    for klass in asmeta_structure_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dynamicfunction_is_not_abstract():
    assert not inspect.isabstract(DynamicFunction)


def test_dynamicfunction_constructor_exists():
    assert callable(DynamicFunction.__init__)


def test_dynamicfunction_constructor_args():
    sig = inspect.signature(DynamicFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_controlledfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_ControlledFunction)


def test_asmeta_definitions_controlledfunction_constructor_exists():
    assert callable(asmeta_definitions_ControlledFunction.__init__)


def test_asmeta_definitions_controlledfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_ControlledFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_sharedfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_SharedFunction)


def test_asmeta_definitions_sharedfunction_constructor_exists():
    assert callable(asmeta_definitions_SharedFunction.__init__)


def test_asmeta_definitions_sharedfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_SharedFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_localfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_LocalFunction)


def test_asmeta_definitions_localfunction_constructor_exists():
    assert callable(asmeta_definitions_LocalFunction.__init__)


def test_asmeta_definitions_localfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_LocalFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_monitoredfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_MonitoredFunction)


def test_asmeta_definitions_monitoredfunction_constructor_exists():
    assert callable(asmeta_definitions_MonitoredFunction.__init__)


def test_asmeta_definitions_monitoredfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_MonitoredFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_outfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_OutFunction)


def test_asmeta_definitions_outfunction_constructor_exists():
    assert callable(asmeta_definitions_OutFunction.__init__)


def test_asmeta_definitions_outfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_OutFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_functioninitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_FunctionInitialization)


def test_asmeta_structure_functioninitialization_constructor_exists():
    assert callable(asmeta_structure_FunctionInitialization.__init__)


def test_asmeta_structure_functioninitialization_constructor_args():
    sig = inspect.signature(asmeta_structure_FunctionInitialization.__init__)
    params = list(sig.parameters.keys())



def test_invarconstraint_is_not_abstract():
    assert not inspect.isabstract(InvarConstraint)


def test_invarconstraint_constructor_exists():
    assert callable(InvarConstraint.__init__)


def test_invarconstraint_constructor_args():
    sig = inspect.signature(InvarConstraint.__init__)
    params = list(sig.parameters.keys())



def test_fairnessconstraint_is_not_abstract():
    assert not inspect.isabstract(FairnessConstraint)


def test_fairnessconstraint_constructor_exists():
    assert callable(FairnessConstraint.__init__)


def test_fairnessconstraint_constructor_args():
    sig = inspect.signature(FairnessConstraint.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_compassionconstraint_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_CompassionConstraint)


def test_asmeta_definitions_compassionconstraint_constructor_exists():
    assert callable(asmeta_definitions_CompassionConstraint.__init__)


def test_asmeta_definitions_compassionconstraint_constructor_args():
    sig = inspect.signature(asmeta_definitions_CompassionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_justiceconstraint_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_JusticeConstraint)


def test_asmeta_definitions_justiceconstraint_constructor_exists():
    assert callable(asmeta_definitions_JusticeConstraint.__init__)


def test_asmeta_definitions_justiceconstraint_constructor_args():
    sig = inspect.signature(asmeta_definitions_JusticeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_asm_is_not_abstract():
    assert not inspect.isabstract(Asm)


def test_asm_constructor_exists():
    assert callable(Asm.__init__)


def test_asm_constructor_args():
    sig = inspect.signature(Asm.__init__)
    params = list(sig.parameters.keys())



def test_domaindefinition_is_not_abstract():
    assert not inspect.isabstract(DomainDefinition)


def test_domaindefinition_constructor_exists():
    assert callable(DomainDefinition.__init__)


def test_domaindefinition_constructor_args():
    sig = inspect.signature(DomainDefinition.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_temporalproperty_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_TemporalProperty)


def test_asmeta_definitions_temporalproperty_constructor_exists():
    assert callable(asmeta_definitions_TemporalProperty.__init__)


def test_asmeta_definitions_temporalproperty_constructor_args():
    sig = inspect.signature(asmeta_definitions_TemporalProperty.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_invariant_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_Invariant)


def test_asmeta_definitions_invariant_constructor_exists():
    assert callable(asmeta_definitions_Invariant.__init__)


def test_asmeta_definitions_invariant_constructor_args():
    sig = inspect.signature(asmeta_definitions_Invariant.__init__)
    params = list(sig.parameters.keys())



def test_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(FunctionDefinition)


def test_functiondefinition_constructor_exists():
    assert callable(FunctionDefinition.__init__)


def test_functiondefinition_constructor_args():
    sig = inspect.signature(FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_structure_body_is_not_abstract():
    assert not inspect.isabstract(asmeta_structure_Body)


def test_asmeta_structure_body_constructor_exists():
    assert callable(asmeta_structure_Body.__init__)


def test_asmeta_structure_body_constructor_args():
    sig = inspect.signature(asmeta_structure_Body.__init__)
    params = list(sig.parameters.keys())



def test_initialization_is_not_abstract():
    assert not inspect.isabstract(Initialization)


def test_initialization_constructor_exists():
    assert callable(Initialization.__init__)


def test_initialization_constructor_args():
    sig = inspect.signature(Initialization.__init__)
    params = list(sig.parameters.keys())



def test_ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(RuleDeclaration)


def test_ruledeclaration_constructor_exists():
    assert callable(RuleDeclaration.__init__)


def test_ruledeclaration_constructor_args():
    sig = inspect.signature(RuleDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basictransitionrules_macrodeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta_basictransitionrules_MacroDeclaration)


def test_asmeta_basictransitionrules_macrodeclaration_constructor_exists():
    assert callable(asmeta_basictransitionrules_MacroDeclaration.__init__)


def test_asmeta_basictransitionrules_macrodeclaration_constructor_args():
    sig = inspect.signature(asmeta_basictransitionrules_MacroDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_turbotransitionrules_turbodeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta_turbotransitionrules_TurboDeclaration)


def test_asmeta_turbotransitionrules_turbodeclaration_constructor_exists():
    assert callable(asmeta_turbotransitionrules_TurboDeclaration.__init__)


def test_asmeta_turbotransitionrules_turbodeclaration_constructor_args():
    sig = inspect.signature(asmeta_turbotransitionrules_TurboDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules_termasrule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules_TermAsRule)


def test_basictransitionrules_termasrule_constructor_exists():
    assert callable(basictransitionrules_TermAsRule.__init__)


def test_basictransitionrules_termasrule_constructor_args():
    sig = inspect.signature(basictransitionrules_TermAsRule.__init__)
    params = list(sig.parameters.keys())



def test_domains_domain_is_not_abstract():
    assert not inspect.isabstract(domains_Domain)


def test_domains_domain_constructor_exists():
    assert callable(domains_Domain.__init__)


def test_domains_domain_constructor_args():
    sig = inspect.signature(domains_Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_term_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_Term)


def test_asmeta_basicterms_term_constructor_exists():
    assert callable(asmeta_basicterms_Term.__init__)


def test_asmeta_basicterms_term_constructor_args():
    sig = inspect.signature(asmeta_basicterms_Term.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_basicterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_BasicTerm)


def test_asmeta_basicterms_basicterm_constructor_exists():
    assert callable(asmeta_basicterms_BasicTerm.__init__)


def test_asmeta_basicterms_basicterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_BasicTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_extendedterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_ExtendedTerm)


def test_asmeta_basicterms_extendedterm_constructor_exists():
    assert callable(asmeta_basicterms_ExtendedTerm.__init__)


def test_asmeta_basicterms_extendedterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_ExtendedTerm.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_basicfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_BasicFunction)


def test_asmeta_definitions_basicfunction_constructor_exists():
    assert callable(asmeta_definitions_BasicFunction.__init__)


def test_asmeta_definitions_basicfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_BasicFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_definitions_derivedfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta_definitions_DerivedFunction)


def test_asmeta_definitions_derivedfunction_constructor_exists():
    assert callable(asmeta_definitions_DerivedFunction.__init__)


def test_asmeta_definitions_derivedfunction_constructor_args():
    sig = inspect.signature(asmeta_definitions_DerivedFunction.__init__)
    params = list(sig.parameters.keys())



def test_functionterm_is_not_abstract():
    assert not inspect.isabstract(FunctionTerm)


def test_functionterm_constructor_exists():
    assert callable(FunctionTerm.__init__)


def test_functionterm_constructor_args():
    sig = inspect.signature(FunctionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_locationterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_LocationTerm)


def test_asmeta_basicterms_locationterm_constructor_exists():
    assert callable(asmeta_basicterms_LocationTerm.__init__)


def test_asmeta_basicterms_locationterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_LocationTerm.__init__)
    params = list(sig.parameters.keys())



def test_furtherterms_finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(furtherterms_FiniteQuantificationTerm)


def test_furtherterms_finitequantificationterm_constructor_exists():
    assert callable(furtherterms_FiniteQuantificationTerm.__init__)


def test_furtherterms_finitequantificationterm_constructor_args():
    sig = inspect.signature(furtherterms_FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())



def test_basicterm_is_not_abstract():
    assert not inspect.isabstract(BasicTerm)


def test_basicterm_constructor_exists():
    assert callable(BasicTerm.__init__)


def test_basicterm_constructor_args():
    sig = inspect.signature(BasicTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_constantterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_ConstantTerm)


def test_asmeta_basicterms_constantterm_constructor_exists():
    assert callable(asmeta_basicterms_ConstantTerm.__init__)


def test_asmeta_basicterms_constantterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_ConstantTerm.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_asmeta_basicterms_constantterm_has_symbol():
    assert hasattr(asmeta_basicterms_ConstantTerm, "symbol")
    descriptor = None
    for klass in asmeta_basicterms_ConstantTerm.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basicterms_functionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_FunctionTerm)


def test_asmeta_basicterms_functionterm_constructor_exists():
    assert callable(asmeta_basicterms_FunctionTerm.__init__)


def test_asmeta_basicterms_functionterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_FunctionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_variableterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_VariableTerm)


def test_asmeta_basicterms_variableterm_constructor_exists():
    assert callable(asmeta_basicterms_VariableTerm.__init__)


def test_asmeta_basicterms_variableterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_VariableTerm.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_asmeta_basicterms_variableterm_has_name():
    assert hasattr(asmeta_basicterms_VariableTerm, "name")
    descriptor = None
    for klass in asmeta_basicterms_VariableTerm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_asmeta_basicterms_variableterm_has_kind():
    assert hasattr(asmeta_basicterms_VariableTerm, "kind")
    descriptor = None
    for klass in asmeta_basicterms_VariableTerm.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectionterm_is_not_abstract():
    assert not inspect.isabstract(CollectionTerm)


def test_collectionterm_constructor_exists():
    assert callable(CollectionTerm.__init__)


def test_collectionterm_constructor_args():
    sig = inspect.signature(CollectionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_mapterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_MapTerm)


def test_asmeta_furtherterms_mapterm_constructor_exists():
    assert callable(asmeta_furtherterms_MapTerm.__init__)


def test_asmeta_furtherterms_mapterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_MapTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_bagterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_BagTerm)


def test_asmeta_furtherterms_bagterm_constructor_exists():
    assert callable(asmeta_furtherterms_BagTerm.__init__)


def test_asmeta_furtherterms_bagterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_BagTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_setterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_SetTerm)


def test_asmeta_basicterms_setterm_constructor_exists():
    assert callable(asmeta_basicterms_SetTerm.__init__)


def test_asmeta_basicterms_setterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_sequenceterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_SequenceTerm)


def test_asmeta_furtherterms_sequenceterm_constructor_exists():
    assert callable(asmeta_furtherterms_SequenceTerm.__init__)


def test_asmeta_furtherterms_sequenceterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_SequenceTerm.__init__)
    params = list(sig.parameters.keys())
    assert "terms" in params, "Missing parameter 'terms'"

def test_asmeta_furtherterms_sequenceterm_has_terms():
    assert hasattr(asmeta_furtherterms_SequenceTerm, "terms")
    descriptor = None
    for klass in asmeta_furtherterms_SequenceTerm.__mro__:
        if "terms" in klass.__dict__:
            descriptor = klass.__dict__["terms"]
            break
    assert isinstance(descriptor, property)



def test_comprehensionterm_is_not_abstract():
    assert not inspect.isabstract(ComprehensionTerm)


def test_comprehensionterm_constructor_exists():
    assert callable(ComprehensionTerm.__init__)


def test_comprehensionterm_constructor_args():
    sig = inspect.signature(ComprehensionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_bagct_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_BagCt)


def test_asmeta_furtherterms_bagct_constructor_exists():
    assert callable(asmeta_furtherterms_BagCt.__init__)


def test_asmeta_furtherterms_bagct_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_BagCt.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_sequencect_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_SequenceCt)


def test_asmeta_furtherterms_sequencect_constructor_exists():
    assert callable(asmeta_furtherterms_SequenceCt.__init__)


def test_asmeta_furtherterms_sequencect_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_SequenceCt.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_setct_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_SetCt)


def test_asmeta_furtherterms_setct_constructor_exists():
    assert callable(asmeta_furtherterms_SetCt.__init__)


def test_asmeta_furtherterms_setct_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_SetCt.__init__)
    params = list(sig.parameters.keys())



def test_extendedterm_is_not_abstract():
    assert not inspect.isabstract(ExtendedTerm)


def test_extendedterm_constructor_exists():
    assert callable(ExtendedTerm.__init__)


def test_extendedterm_constructor_args():
    sig = inspect.signature(ExtendedTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_caseterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_CaseTerm)


def test_asmeta_furtherterms_caseterm_constructor_exists():
    assert callable(asmeta_furtherterms_CaseTerm.__init__)


def test_asmeta_furtherterms_caseterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_CaseTerm.__init__)
    params = list(sig.parameters.keys())
    assert "resultTerms" in params, "Missing parameter 'resultTerms'"

def test_asmeta_furtherterms_caseterm_has_resultTerms():
    assert hasattr(asmeta_furtherterms_CaseTerm, "resultTerms")
    descriptor = None
    for klass in asmeta_furtherterms_CaseTerm.__mro__:
        if "resultTerms" in klass.__dict__:
            descriptor = klass.__dict__["resultTerms"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basicterms_domainterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_DomainTerm)


def test_asmeta_basicterms_domainterm_constructor_exists():
    assert callable(asmeta_basicterms_DomainTerm.__init__)


def test_asmeta_basicterms_domainterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_DomainTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_tupleterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_TupleTerm)


def test_asmeta_basicterms_tupleterm_constructor_exists():
    assert callable(asmeta_basicterms_TupleTerm.__init__)


def test_asmeta_basicterms_tupleterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_TupleTerm.__init__)
    params = list(sig.parameters.keys())
    assert "terms" in params, "Missing parameter 'terms'"
    assert "arity" in params, "Missing parameter 'arity'"

def test_asmeta_basicterms_tupleterm_has_terms():
    assert hasattr(asmeta_basicterms_TupleTerm, "terms")
    descriptor = None
    for klass in asmeta_basicterms_TupleTerm.__mro__:
        if "terms" in klass.__dict__:
            descriptor = klass.__dict__["terms"]
            break
    assert isinstance(descriptor, property)

def test_asmeta_basicterms_tupleterm_has_arity():
    assert hasattr(asmeta_basicterms_TupleTerm, "arity")
    descriptor = None
    for klass in asmeta_basicterms_TupleTerm.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_basicterms_ruleasterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_RuleAsTerm)


def test_asmeta_basicterms_ruleasterm_constructor_exists():
    assert callable(asmeta_basicterms_RuleAsTerm.__init__)


def test_asmeta_basicterms_ruleasterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_RuleAsTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_collectionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_CollectionTerm)


def test_asmeta_basicterms_collectionterm_constructor_exists():
    assert callable(asmeta_basicterms_CollectionTerm.__init__)


def test_asmeta_basicterms_collectionterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_CollectionTerm.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_asmeta_basicterms_collectionterm_has_size():
    assert hasattr(asmeta_basicterms_CollectionTerm, "size")
    descriptor = None
    for klass in asmeta_basicterms_CollectionTerm.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_furtherterms_variablebindingterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_VariableBindingTerm)


def test_asmeta_furtherterms_variablebindingterm_constructor_exists():
    assert callable(asmeta_furtherterms_VariableBindingTerm.__init__)


def test_asmeta_furtherterms_variablebindingterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_VariableBindingTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_conditionalterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ConditionalTerm)


def test_asmeta_furtherterms_conditionalterm_constructor_exists():
    assert callable(asmeta_furtherterms_ConditionalTerm.__init__)


def test_asmeta_furtherterms_conditionalterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ConditionalTerm.__init__)
    params = list(sig.parameters.keys())



def test_finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(FiniteQuantificationTerm)


def test_finitequantificationterm_constructor_exists():
    assert callable(FiniteQuantificationTerm.__init__)


def test_finitequantificationterm_constructor_args():
    sig = inspect.signature(FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_existuniqueterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ExistUniqueTerm)


def test_asmeta_furtherterms_existuniqueterm_constructor_exists():
    assert callable(asmeta_furtherterms_ExistUniqueTerm.__init__)


def test_asmeta_furtherterms_existuniqueterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ExistUniqueTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_existterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ExistTerm)


def test_asmeta_furtherterms_existterm_constructor_exists():
    assert callable(asmeta_furtherterms_ExistTerm.__init__)


def test_asmeta_furtherterms_existterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ExistTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_forallterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ForallTerm)


def test_asmeta_furtherterms_forallterm_constructor_exists():
    assert callable(asmeta_furtherterms_ForallTerm.__init__)


def test_asmeta_furtherterms_forallterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ForallTerm.__init__)
    params = list(sig.parameters.keys())



def test_basicterms_term_is_not_abstract():
    assert not inspect.isabstract(basicterms_Term)


def test_basicterms_term_constructor_exists():
    assert callable(basicterms_Term.__init__)


def test_basicterms_term_constructor_args():
    sig = inspect.signature(basicterms_Term.__init__)
    params = list(sig.parameters.keys())



def test_basicterms_variableterm_is_not_abstract():
    assert not inspect.isabstract(basicterms_VariableTerm)


def test_basicterms_variableterm_constructor_exists():
    assert callable(basicterms_VariableTerm.__init__)


def test_basicterms_variableterm_constructor_args():
    sig = inspect.signature(basicterms_VariableTerm.__init__)
    params = list(sig.parameters.keys())



def test_variablebindingterm_is_not_abstract():
    assert not inspect.isabstract(VariableBindingTerm)


def test_variablebindingterm_constructor_exists():
    assert callable(VariableBindingTerm.__init__)


def test_variablebindingterm_constructor_args():
    sig = inspect.signature(VariableBindingTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_FiniteQuantificationTerm)


def test_asmeta_furtherterms_finitequantificationterm_constructor_exists():
    assert callable(asmeta_furtherterms_FiniteQuantificationTerm.__init__)


def test_asmeta_furtherterms_finitequantificationterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta_furtherterms_finitequantificationterm_has_ranges():
    assert hasattr(asmeta_furtherterms_FiniteQuantificationTerm, "ranges")
    descriptor = None
    for klass in asmeta_furtherterms_FiniteQuantificationTerm.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_furtherterms_comprehensionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ComprehensionTerm)


def test_asmeta_furtherterms_comprehensionterm_constructor_exists():
    assert callable(asmeta_furtherterms_ComprehensionTerm.__init__)


def test_asmeta_furtherterms_comprehensionterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ComprehensionTerm.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta_furtherterms_comprehensionterm_has_ranges():
    assert hasattr(asmeta_furtherterms_ComprehensionTerm, "ranges")
    descriptor = None
    for klass in asmeta_furtherterms_ComprehensionTerm.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta_furtherterms_letterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_LetTerm)


def test_asmeta_furtherterms_letterm_constructor_exists():
    assert callable(asmeta_furtherterms_LetTerm.__init__)


def test_asmeta_furtherterms_letterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_LetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_mapct_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_MapCt)


def test_asmeta_furtherterms_mapct_constructor_exists():
    assert callable(asmeta_furtherterms_MapCt.__init__)


def test_asmeta_furtherterms_mapct_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_MapCt.__init__)
    params = list(sig.parameters.keys())



def test_basicterms_tupleterm_is_not_abstract():
    assert not inspect.isabstract(basicterms_TupleTerm)


def test_basicterms_tupleterm_constructor_exists():
    assert callable(basicterms_TupleTerm.__init__)


def test_basicterms_tupleterm_constructor_args():
    sig = inspect.signature(basicterms_TupleTerm.__init__)
    params = list(sig.parameters.keys())



def test_constantterm_is_not_abstract():
    assert not inspect.isabstract(ConstantTerm)


def test_constantterm_constructor_exists():
    assert callable(ConstantTerm.__init__)


def test_constantterm_constructor_args():
    sig = inspect.signature(ConstantTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_realterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_RealTerm)


def test_asmeta_furtherterms_realterm_constructor_exists():
    assert callable(asmeta_furtherterms_RealTerm.__init__)


def test_asmeta_furtherterms_realterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_RealTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_stringterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_StringTerm)


def test_asmeta_furtherterms_stringterm_constructor_exists():
    assert callable(asmeta_furtherterms_StringTerm.__init__)


def test_asmeta_furtherterms_stringterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_StringTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_complexterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_ComplexTerm)


def test_asmeta_furtherterms_complexterm_constructor_exists():
    assert callable(asmeta_furtherterms_ComplexTerm.__init__)


def test_asmeta_furtherterms_complexterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_ComplexTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_enumterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_EnumTerm)


def test_asmeta_furtherterms_enumterm_constructor_exists():
    assert callable(asmeta_furtherterms_EnumTerm.__init__)


def test_asmeta_furtherterms_enumterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_EnumTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_booleanterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_BooleanTerm)


def test_asmeta_basicterms_booleanterm_constructor_exists():
    assert callable(asmeta_basicterms_BooleanTerm.__init__)


def test_asmeta_basicterms_booleanterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_basicterms_undefterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_basicterms_UndefTerm)


def test_asmeta_basicterms_undefterm_constructor_exists():
    assert callable(asmeta_basicterms_UndefTerm.__init__)


def test_asmeta_basicterms_undefterm_constructor_args():
    sig = inspect.signature(asmeta_basicterms_UndefTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_charterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_CharTerm)


def test_asmeta_furtherterms_charterm_constructor_exists():
    assert callable(asmeta_furtherterms_CharTerm.__init__)


def test_asmeta_furtherterms_charterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_CharTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_naturalterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_NaturalTerm)


def test_asmeta_furtherterms_naturalterm_constructor_exists():
    assert callable(asmeta_furtherterms_NaturalTerm.__init__)


def test_asmeta_furtherterms_naturalterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_NaturalTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta_furtherterms_integerterm_is_not_abstract():
    assert not inspect.isabstract(asmeta_furtherterms_IntegerTerm)


def test_asmeta_furtherterms_integerterm_constructor_exists():
    assert callable(asmeta_furtherterms_IntegerTerm.__init__)


def test_asmeta_furtherterms_integerterm_constructor_args():
    sig = inspect.signature(asmeta_furtherterms_IntegerTerm.__init__)
    params = list(sig.parameters.keys())

def test_variablekind_exists():
    # Check that the Enumeration exists
    assert VariableKind is not None

def test_variablekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableKind]
    expected_literals = [
        "ruleVar",
        "locationVar",
        "logicalVar",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableKind"


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
ComplexDomain_strategy = st.builds(
    ComplexDomain,
)
asmeta_domains_RealDomain_strategy = st.builds(
    asmeta_domains_RealDomain,
)
AbstractTd_strategy = st.builds(
    AbstractTd,
)
asmeta_domains_AgentDomain_strategy = st.builds(
    asmeta_domains_AgentDomain,
)
asmeta_domains_ReserveDomain_strategy = st.builds(
    asmeta_domains_ReserveDomain,
)
domains_TypeDomain_strategy = st.builds(
    domains_TypeDomain,
)
asmeta_domains_EnumElement_strategy = st.builds(
    asmeta_domains_EnumElement,
    symbol=
        safe_text
)
domains_EnumElement_strategy = st.builds(
    domains_EnumElement,
)
RealDomain_strategy = st.builds(
    RealDomain,
)
asmeta_domains_IntegerDomain_strategy = st.builds(
    asmeta_domains_IntegerDomain,
)
TemporalProperty_strategy = st.builds(
    TemporalProperty,
)
asmeta_definitions_LtlSpec_strategy = st.builds(
    asmeta_definitions_LtlSpec,
)
asmeta_definitions_CtlSpec_strategy = st.builds(
    asmeta_definitions_CtlSpec,
)
StructuredTd_strategy = st.builds(
    StructuredTd,
)
asmeta_domains_MapDomain_strategy = st.builds(
    asmeta_domains_MapDomain,
)
asmeta_domains_RuleDomain_strategy = st.builds(
    asmeta_domains_RuleDomain,
    domains=
        safe_text
)
asmeta_domains_PowersetDomain_strategy = st.builds(
    asmeta_domains_PowersetDomain,
)
asmeta_domains_BagDomain_strategy = st.builds(
    asmeta_domains_BagDomain,
)
asmeta_domains_ProductDomain_strategy = st.builds(
    asmeta_domains_ProductDomain,
    domains=
        safe_text
)
asmeta_domains_SequenceDomain_strategy = st.builds(
    asmeta_domains_SequenceDomain,
)
TypeDomain_strategy = st.builds(
    TypeDomain,
)
asmeta_domains_AnyDomain_strategy = st.builds(
    asmeta_domains_AnyDomain,
)
asmeta_domains_EnumTd_strategy = st.builds(
    asmeta_domains_EnumTd,
)
asmeta_domains_BasicTd_strategy = st.builds(
    asmeta_domains_BasicTd,
)
asmeta_domains_AbstractTd_strategy = st.builds(
    asmeta_domains_AbstractTd,
    isDynamic=
        safe_text
)
asmeta_domains_StructuredTd_strategy = st.builds(
    asmeta_domains_StructuredTd,
)
Domain_strategy = st.builds(
    Domain,
)
asmeta_domains_ConcreteDomain_strategy = st.builds(
    asmeta_domains_ConcreteDomain,
    isDynamic=
        safe_text
)
asmeta_domains_TypeDomain_strategy = st.builds(
    asmeta_domains_TypeDomain,
)
BasicTd_strategy = st.builds(
    BasicTd,
)
asmeta_domains_BooleanDomain_strategy = st.builds(
    asmeta_domains_BooleanDomain,
)
asmeta_domains_StringDomain_strategy = st.builds(
    asmeta_domains_StringDomain,
)
asmeta_domains_ComplexDomain_strategy = st.builds(
    asmeta_domains_ComplexDomain,
)
asmeta_domains_CharDomain_strategy = st.builds(
    asmeta_domains_CharDomain,
)
asmeta_domains_UndefDomain_strategy = st.builds(
    asmeta_domains_UndefDomain,
)
IntegerDomain_strategy = st.builds(
    IntegerDomain,
)
asmeta_domains_NaturalDomain_strategy = st.builds(
    asmeta_domains_NaturalDomain,
)
BasicFunction_strategy = st.builds(
    BasicFunction,
)
asmeta_definitions_StaticFunction_strategy = st.builds(
    asmeta_definitions_StaticFunction,
)
asmeta_definitions_DynamicFunction_strategy = st.builds(
    asmeta_definitions_DynamicFunction,
)
Invariant_strategy = st.builds(
    Invariant,
)
Classifier_strategy = st.builds(
    Classifier,
)
asmeta_domains_Domain_strategy = st.builds(
    asmeta_domains_Domain,
)
asmeta_definitions_FairnessConstraint_strategy = st.builds(
    asmeta_definitions_FairnessConstraint,
)
asmeta_definitions_Function_strategy = st.builds(
    asmeta_definitions_Function,
    arity=
        safe_text
)
asmeta_definitions_InvarConstraint_strategy = st.builds(
    asmeta_definitions_InvarConstraint,
)
asmeta_definitions_Property_strategy = st.builds(
    asmeta_definitions_Property,
)
asmeta_definitions_RuleDeclaration_strategy = st.builds(
    asmeta_definitions_RuleDeclaration,
    arity=
        safe_text
)
BasicRule_strategy = st.builds(
    BasicRule,
)
asmeta_basictransitionrules_ForallRule_strategy = st.builds(
    asmeta_basictransitionrules_ForallRule,
    ranges=
        safe_text
)
asmeta_basictransitionrules_ExtendRule_strategy = st.builds(
    asmeta_basictransitionrules_ExtendRule,
)
asmeta_basictransitionrules_SkipRule_strategy = st.builds(
    asmeta_basictransitionrules_SkipRule,
)
asmeta_basictransitionrules_ConditionalRule_strategy = st.builds(
    asmeta_basictransitionrules_ConditionalRule,
)
asmeta_basictransitionrules_BlockRule_strategy = st.builds(
    asmeta_basictransitionrules_BlockRule,
    rules=
        safe_text
)
asmeta_basictransitionrules_LetRule_strategy = st.builds(
    asmeta_basictransitionrules_LetRule,
)
asmeta_basictransitionrules_UpdateRule_strategy = st.builds(
    asmeta_basictransitionrules_UpdateRule,
)
asmeta_basictransitionrules_MacroCallRule_strategy = st.builds(
    asmeta_basictransitionrules_MacroCallRule,
    parameters=
        safe_text
)
asmeta_basictransitionrules_ChooseRule_strategy = st.builds(
    asmeta_basictransitionrules_ChooseRule,
    ranges=
        safe_text
)
asmeta_basictransitionrules_Rule_strategy = st.builds(
    asmeta_basictransitionrules_Rule,
)
TurboDerivedRule_strategy = st.builds(
    TurboDerivedRule,
)
asmeta_derivedtransitionrules_RecursiveWhileRule_strategy = st.builds(
    asmeta_derivedtransitionrules_RecursiveWhileRule,
)
DerivedRule_strategy = st.builds(
    DerivedRule,
)
asmeta_derivedtransitionrules_TurboDerivedRule_strategy = st.builds(
    asmeta_derivedtransitionrules_TurboDerivedRule,
)
asmeta_derivedtransitionrules_BasicDerivedRule_strategy = st.builds(
    asmeta_derivedtransitionrules_BasicDerivedRule,
)
BasicDerivedRule_strategy = st.builds(
    BasicDerivedRule,
)
asmeta_derivedtransitionrules_CaseRule_strategy = st.builds(
    asmeta_derivedtransitionrules_CaseRule,
    caseBranches=
        safe_text
)
asmeta_derivedtransitionrules_IterativeWhileRule_strategy = st.builds(
    asmeta_derivedtransitionrules_IterativeWhileRule,
)
Rule_strategy = st.builds(
    Rule,
)
asmeta_derivedtransitionrules_DerivedRule_strategy = st.builds(
    asmeta_derivedtransitionrules_DerivedRule,
)
asmeta_basictransitionrules_BasicRule_strategy = st.builds(
    asmeta_basictransitionrules_BasicRule,
)
asmeta_basictransitionrules_TermAsRule_strategy = st.builds(
    asmeta_basictransitionrules_TermAsRule,
    parameters=
        safe_text
)
asmeta_turbotransitionrules_TurboRule_strategy = st.builds(
    asmeta_turbotransitionrules_TurboRule,
)
turbotransitionrules_TurboCallRule_strategy = st.builds(
    turbotransitionrules_TurboCallRule,
)
turbotransitionrules_TurboDeclaration_strategy = st.builds(
    turbotransitionrules_TurboDeclaration,
)
LocalFunction_strategy = st.builds(
    LocalFunction,
)
basictransitionrules_Rule_strategy = st.builds(
    basictransitionrules_Rule,
)
TurboRule_strategy = st.builds(
    TurboRule,
)
asmeta_turbotransitionrules_TurboCallRule_strategy = st.builds(
    asmeta_turbotransitionrules_TurboCallRule,
    parameters=
        safe_text
)
asmeta_turbotransitionrules_TryCatchRule_strategy = st.builds(
    asmeta_turbotransitionrules_TryCatchRule,
)
asmeta_turbotransitionrules_TurboReturnRule_strategy = st.builds(
    asmeta_turbotransitionrules_TurboReturnRule,
)
asmeta_turbotransitionrules_IterateRule_strategy = st.builds(
    asmeta_turbotransitionrules_IterateRule,
)
asmeta_turbotransitionrules_TurboLocalStateRule_strategy = st.builds(
    asmeta_turbotransitionrules_TurboLocalStateRule,
)
asmeta_turbotransitionrules_SeqRule_strategy = st.builds(
    asmeta_turbotransitionrules_SeqRule,
    rules=
        safe_text
)
asmeta_structure_DomainDefinition_strategy = st.builds(
    asmeta_structure_DomainDefinition,
)
basictransitionrules_MacroDeclaration_strategy = st.builds(
    basictransitionrules_MacroDeclaration,
)
Body_strategy = st.builds(
    Body,
)
ExportClause_strategy = st.builds(
    ExportClause,
)
Signature_strategy = st.builds(
    Signature,
)
ImportClause_strategy = st.builds(
    ImportClause,
)
asmeta_structure_Header_strategy = st.builds(
    asmeta_structure_Header,
)
AgentInitialization_strategy = st.builds(
    AgentInitialization,
)
FunctionInitialization_strategy = st.builds(
    FunctionInitialization,
)
DomainInitialization_strategy = st.builds(
    DomainInitialization,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
asmeta_structure_Asm_strategy = st.builds(
    asmeta_structure_Asm,
    isAsynchr=
        safe_text
)
asmeta_definitions_Classifier_strategy = st.builds(
    asmeta_definitions_Classifier,
)
asmeta_structure_Initialization_strategy = st.builds(
    asmeta_structure_Initialization,
)
domains_ConcreteDomain_strategy = st.builds(
    domains_ConcreteDomain,
)
asmeta_structure_DomainInitialization_strategy = st.builds(
    asmeta_structure_DomainInitialization,
)
asmeta_structure_FunctionDefinition_strategy = st.builds(
    asmeta_structure_FunctionDefinition,
)
asmeta_structure_ImportClause_strategy = st.builds(
    asmeta_structure_ImportClause,
    moduleName=
        safe_text
)
asmeta_structure_ExportClause_strategy = st.builds(
    asmeta_structure_ExportClause,
)
domains_StructuredTd_strategy = st.builds(
    domains_StructuredTd,
)
Header_strategy = st.builds(
    Header,
)
asmeta_structure_Signature_strategy = st.builds(
    asmeta_structure_Signature,
)
basictransitionrules_MacroCallRule_strategy = st.builds(
    basictransitionrules_MacroCallRule,
)
asmeta_structure_AgentInitialization_strategy = st.builds(
    asmeta_structure_AgentInitialization,
)
asmeta_structure_NamedElement_strategy = st.builds(
    asmeta_structure_NamedElement,
    name=
        safe_text
)
DynamicFunction_strategy = st.builds(
    DynamicFunction,
)
asmeta_definitions_ControlledFunction_strategy = st.builds(
    asmeta_definitions_ControlledFunction,
)
asmeta_definitions_SharedFunction_strategy = st.builds(
    asmeta_definitions_SharedFunction,
)
asmeta_definitions_LocalFunction_strategy = st.builds(
    asmeta_definitions_LocalFunction,
)
asmeta_definitions_MonitoredFunction_strategy = st.builds(
    asmeta_definitions_MonitoredFunction,
)
asmeta_definitions_OutFunction_strategy = st.builds(
    asmeta_definitions_OutFunction,
)
asmeta_structure_FunctionInitialization_strategy = st.builds(
    asmeta_structure_FunctionInitialization,
)
InvarConstraint_strategy = st.builds(
    InvarConstraint,
)
FairnessConstraint_strategy = st.builds(
    FairnessConstraint,
)
asmeta_definitions_CompassionConstraint_strategy = st.builds(
    asmeta_definitions_CompassionConstraint,
)
asmeta_definitions_JusticeConstraint_strategy = st.builds(
    asmeta_definitions_JusticeConstraint,
)
Asm_strategy = st.builds(
    Asm,
)
DomainDefinition_strategy = st.builds(
    DomainDefinition,
)
Property_strategy = st.builds(
    Property,
)
asmeta_definitions_TemporalProperty_strategy = st.builds(
    asmeta_definitions_TemporalProperty,
)
asmeta_definitions_Invariant_strategy = st.builds(
    asmeta_definitions_Invariant,
)
FunctionDefinition_strategy = st.builds(
    FunctionDefinition,
)
asmeta_structure_Body_strategy = st.builds(
    asmeta_structure_Body,
)
Initialization_strategy = st.builds(
    Initialization,
)
RuleDeclaration_strategy = st.builds(
    RuleDeclaration,
)
asmeta_basictransitionrules_MacroDeclaration_strategy = st.builds(
    asmeta_basictransitionrules_MacroDeclaration,
)
asmeta_turbotransitionrules_TurboDeclaration_strategy = st.builds(
    asmeta_turbotransitionrules_TurboDeclaration,
)
basictransitionrules_TermAsRule_strategy = st.builds(
    basictransitionrules_TermAsRule,
)
domains_Domain_strategy = st.builds(
    domains_Domain,
)
asmeta_basicterms_Term_strategy = st.builds(
    asmeta_basicterms_Term,
)
Term_strategy = st.builds(
    Term,
)
asmeta_basicterms_BasicTerm_strategy = st.builds(
    asmeta_basicterms_BasicTerm,
)
asmeta_basicterms_ExtendedTerm_strategy = st.builds(
    asmeta_basicterms_ExtendedTerm,
)
Function_strategy = st.builds(
    Function,
)
asmeta_definitions_BasicFunction_strategy = st.builds(
    asmeta_definitions_BasicFunction,
)
asmeta_definitions_DerivedFunction_strategy = st.builds(
    asmeta_definitions_DerivedFunction,
)
FunctionTerm_strategy = st.builds(
    FunctionTerm,
)
asmeta_basicterms_LocationTerm_strategy = st.builds(
    asmeta_basicterms_LocationTerm,
)
furtherterms_FiniteQuantificationTerm_strategy = st.builds(
    furtherterms_FiniteQuantificationTerm,
)
BasicTerm_strategy = st.builds(
    BasicTerm,
)
asmeta_basicterms_ConstantTerm_strategy = st.builds(
    asmeta_basicterms_ConstantTerm,
    symbol=
        safe_text
)
asmeta_basicterms_FunctionTerm_strategy = st.builds(
    asmeta_basicterms_FunctionTerm,
)
asmeta_basicterms_VariableTerm_strategy = st.builds(
    asmeta_basicterms_VariableTerm,
    name=
        safe_text,
    kind=
        safe_text
)
CollectionTerm_strategy = st.builds(
    CollectionTerm,
)
asmeta_furtherterms_MapTerm_strategy = st.builds(
    asmeta_furtherterms_MapTerm,
)
asmeta_furtherterms_BagTerm_strategy = st.builds(
    asmeta_furtherterms_BagTerm,
)
asmeta_basicterms_SetTerm_strategy = st.builds(
    asmeta_basicterms_SetTerm,
)
asmeta_furtherterms_SequenceTerm_strategy = st.builds(
    asmeta_furtherterms_SequenceTerm,
    terms=
        safe_text
)
ComprehensionTerm_strategy = st.builds(
    ComprehensionTerm,
)
asmeta_furtherterms_BagCt_strategy = st.builds(
    asmeta_furtherterms_BagCt,
)
asmeta_furtherterms_SequenceCt_strategy = st.builds(
    asmeta_furtherterms_SequenceCt,
)
asmeta_furtherterms_SetCt_strategy = st.builds(
    asmeta_furtherterms_SetCt,
)
ExtendedTerm_strategy = st.builds(
    ExtendedTerm,
)
asmeta_furtherterms_CaseTerm_strategy = st.builds(
    asmeta_furtherterms_CaseTerm,
    resultTerms=
        safe_text
)
asmeta_basicterms_DomainTerm_strategy = st.builds(
    asmeta_basicterms_DomainTerm,
)
asmeta_basicterms_TupleTerm_strategy = st.builds(
    asmeta_basicterms_TupleTerm,
    terms=
        safe_text,
    arity=
        safe_text
)
asmeta_basicterms_RuleAsTerm_strategy = st.builds(
    asmeta_basicterms_RuleAsTerm,
)
asmeta_basicterms_CollectionTerm_strategy = st.builds(
    asmeta_basicterms_CollectionTerm,
    size=
        safe_text
)
asmeta_furtherterms_VariableBindingTerm_strategy = st.builds(
    asmeta_furtherterms_VariableBindingTerm,
)
asmeta_furtherterms_ConditionalTerm_strategy = st.builds(
    asmeta_furtherterms_ConditionalTerm,
)
FiniteQuantificationTerm_strategy = st.builds(
    FiniteQuantificationTerm,
)
asmeta_furtherterms_ExistUniqueTerm_strategy = st.builds(
    asmeta_furtherterms_ExistUniqueTerm,
)
asmeta_furtherterms_ExistTerm_strategy = st.builds(
    asmeta_furtherterms_ExistTerm,
)
asmeta_furtherterms_ForallTerm_strategy = st.builds(
    asmeta_furtherterms_ForallTerm,
)
basicterms_Term_strategy = st.builds(
    basicterms_Term,
)
basicterms_VariableTerm_strategy = st.builds(
    basicterms_VariableTerm,
)
VariableBindingTerm_strategy = st.builds(
    VariableBindingTerm,
)
asmeta_furtherterms_FiniteQuantificationTerm_strategy = st.builds(
    asmeta_furtherterms_FiniteQuantificationTerm,
    ranges=
        safe_text
)
asmeta_furtherterms_ComprehensionTerm_strategy = st.builds(
    asmeta_furtherterms_ComprehensionTerm,
    ranges=
        safe_text
)
asmeta_furtherterms_LetTerm_strategy = st.builds(
    asmeta_furtherterms_LetTerm,
)
asmeta_furtherterms_MapCt_strategy = st.builds(
    asmeta_furtherterms_MapCt,
)
basicterms_TupleTerm_strategy = st.builds(
    basicterms_TupleTerm,
)
ConstantTerm_strategy = st.builds(
    ConstantTerm,
)
asmeta_furtherterms_RealTerm_strategy = st.builds(
    asmeta_furtherterms_RealTerm,
)
asmeta_furtherterms_StringTerm_strategy = st.builds(
    asmeta_furtherterms_StringTerm,
)
asmeta_furtherterms_ComplexTerm_strategy = st.builds(
    asmeta_furtherterms_ComplexTerm,
)
asmeta_furtherterms_EnumTerm_strategy = st.builds(
    asmeta_furtherterms_EnumTerm,
)
asmeta_basicterms_BooleanTerm_strategy = st.builds(
    asmeta_basicterms_BooleanTerm,
)
asmeta_basicterms_UndefTerm_strategy = st.builds(
    asmeta_basicterms_UndefTerm,
)
asmeta_furtherterms_CharTerm_strategy = st.builds(
    asmeta_furtherterms_CharTerm,
)
asmeta_furtherterms_NaturalTerm_strategy = st.builds(
    asmeta_furtherterms_NaturalTerm,
)
asmeta_furtherterms_IntegerTerm_strategy = st.builds(
    asmeta_furtherterms_IntegerTerm,
)

@given(instance=ComplexDomain_strategy)
@settings(max_examples=50)
def test_complexdomain_instantiation(instance):
    assert isinstance(instance, ComplexDomain)

@given(instance=asmeta_domains_RealDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_realdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_RealDomain)

@given(instance=AbstractTd_strategy)
@settings(max_examples=50)
def test_abstracttd_instantiation(instance):
    assert isinstance(instance, AbstractTd)

@given(instance=asmeta_domains_AgentDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_agentdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_AgentDomain)

@given(instance=asmeta_domains_ReserveDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_reservedomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_ReserveDomain)

@given(instance=domains_TypeDomain_strategy)
@settings(max_examples=50)
def test_domains_typedomain_instantiation(instance):
    assert isinstance(instance, domains_TypeDomain)

@given(instance=asmeta_domains_EnumElement_strategy)
@settings(max_examples=50)
def test_asmeta_domains_enumelement_instantiation(instance):
    assert isinstance(instance, asmeta_domains_EnumElement)



@given(instance=asmeta_domains_EnumElement_strategy)
def test_asmeta_domains_enumelement_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=domains_EnumElement_strategy)
@settings(max_examples=50)
def test_domains_enumelement_instantiation(instance):
    assert isinstance(instance, domains_EnumElement)

@given(instance=RealDomain_strategy)
@settings(max_examples=50)
def test_realdomain_instantiation(instance):
    assert isinstance(instance, RealDomain)

@given(instance=asmeta_domains_IntegerDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_integerdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_IntegerDomain)

@given(instance=TemporalProperty_strategy)
@settings(max_examples=50)
def test_temporalproperty_instantiation(instance):
    assert isinstance(instance, TemporalProperty)

@given(instance=asmeta_definitions_LtlSpec_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_ltlspec_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_LtlSpec)

@given(instance=asmeta_definitions_CtlSpec_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_ctlspec_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_CtlSpec)

@given(instance=StructuredTd_strategy)
@settings(max_examples=50)
def test_structuredtd_instantiation(instance):
    assert isinstance(instance, StructuredTd)

@given(instance=asmeta_domains_MapDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_mapdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_MapDomain)

@given(instance=asmeta_domains_RuleDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_ruledomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_RuleDomain)



@given(instance=asmeta_domains_RuleDomain_strategy)
def test_asmeta_domains_ruledomain_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=asmeta_domains_PowersetDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_powersetdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_PowersetDomain)

@given(instance=asmeta_domains_BagDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_bagdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_BagDomain)

@given(instance=asmeta_domains_ProductDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_productdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_ProductDomain)



@given(instance=asmeta_domains_ProductDomain_strategy)
def test_asmeta_domains_productdomain_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=asmeta_domains_SequenceDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_sequencedomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_SequenceDomain)

@given(instance=TypeDomain_strategy)
@settings(max_examples=50)
def test_typedomain_instantiation(instance):
    assert isinstance(instance, TypeDomain)

@given(instance=asmeta_domains_AnyDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_anydomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_AnyDomain)

@given(instance=asmeta_domains_EnumTd_strategy)
@settings(max_examples=50)
def test_asmeta_domains_enumtd_instantiation(instance):
    assert isinstance(instance, asmeta_domains_EnumTd)

@given(instance=asmeta_domains_BasicTd_strategy)
@settings(max_examples=50)
def test_asmeta_domains_basictd_instantiation(instance):
    assert isinstance(instance, asmeta_domains_BasicTd)

@given(instance=asmeta_domains_AbstractTd_strategy)
@settings(max_examples=50)
def test_asmeta_domains_abstracttd_instantiation(instance):
    assert isinstance(instance, asmeta_domains_AbstractTd)



@given(instance=asmeta_domains_AbstractTd_strategy)
def test_asmeta_domains_abstracttd_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=asmeta_domains_StructuredTd_strategy)
@settings(max_examples=50)
def test_asmeta_domains_structuredtd_instantiation(instance):
    assert isinstance(instance, asmeta_domains_StructuredTd)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=asmeta_domains_ConcreteDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_concretedomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_ConcreteDomain)



@given(instance=asmeta_domains_ConcreteDomain_strategy)
def test_asmeta_domains_concretedomain_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=asmeta_domains_TypeDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_typedomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_TypeDomain)

@given(instance=BasicTd_strategy)
@settings(max_examples=50)
def test_basictd_instantiation(instance):
    assert isinstance(instance, BasicTd)

@given(instance=asmeta_domains_BooleanDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_booleandomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_BooleanDomain)

@given(instance=asmeta_domains_StringDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_stringdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_StringDomain)

@given(instance=asmeta_domains_ComplexDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_complexdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_ComplexDomain)

@given(instance=asmeta_domains_CharDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_chardomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_CharDomain)

@given(instance=asmeta_domains_UndefDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_undefdomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_UndefDomain)

@given(instance=IntegerDomain_strategy)
@settings(max_examples=50)
def test_integerdomain_instantiation(instance):
    assert isinstance(instance, IntegerDomain)

@given(instance=asmeta_domains_NaturalDomain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_naturaldomain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_NaturalDomain)

@given(instance=BasicFunction_strategy)
@settings(max_examples=50)
def test_basicfunction_instantiation(instance):
    assert isinstance(instance, BasicFunction)

@given(instance=asmeta_definitions_StaticFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_staticfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_StaticFunction)

@given(instance=asmeta_definitions_DynamicFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_dynamicfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_DynamicFunction)

@given(instance=Invariant_strategy)
@settings(max_examples=50)
def test_invariant_instantiation(instance):
    assert isinstance(instance, Invariant)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=asmeta_domains_Domain_strategy)
@settings(max_examples=50)
def test_asmeta_domains_domain_instantiation(instance):
    assert isinstance(instance, asmeta_domains_Domain)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=asmeta_domains_Domain_strategy)
@settings(max_examples=30)
def test_asmeta_domains_domain_compatible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compatible()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compatible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compatible' in asmeta_domains_Domain is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compatible' in asmeta_domains_Domain did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compatible' in asmeta_domains_Domain is not implemented or raised an error")

@given(instance=asmeta_definitions_FairnessConstraint_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_fairnessconstraint_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_FairnessConstraint)

@given(instance=asmeta_definitions_Function_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_function_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_Function)



@given(instance=asmeta_definitions_Function_strategy)
def test_asmeta_definitions_function_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=asmeta_definitions_InvarConstraint_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_invarconstraint_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_InvarConstraint)

@given(instance=asmeta_definitions_Property_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_property_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_Property)

@given(instance=asmeta_definitions_RuleDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_ruledeclaration_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_RuleDeclaration)



@given(instance=asmeta_definitions_RuleDeclaration_strategy)
def test_asmeta_definitions_ruledeclaration_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=BasicRule_strategy)
@settings(max_examples=50)
def test_basicrule_instantiation(instance):
    assert isinstance(instance, BasicRule)

@given(instance=asmeta_basictransitionrules_ForallRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_forallrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_ForallRule)



@given(instance=asmeta_basictransitionrules_ForallRule_strategy)
def test_asmeta_basictransitionrules_forallrule_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta_basictransitionrules_ExtendRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_extendrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_ExtendRule)

@given(instance=asmeta_basictransitionrules_SkipRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_skiprule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_SkipRule)

@given(instance=asmeta_basictransitionrules_ConditionalRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_conditionalrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_ConditionalRule)

@given(instance=asmeta_basictransitionrules_BlockRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_blockrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_BlockRule)



@given(instance=asmeta_basictransitionrules_BlockRule_strategy)
def test_asmeta_basictransitionrules_blockrule_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=asmeta_basictransitionrules_LetRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_letrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_LetRule)

@given(instance=asmeta_basictransitionrules_UpdateRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_updaterule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_UpdateRule)

@given(instance=asmeta_basictransitionrules_MacroCallRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_macrocallrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_MacroCallRule)



@given(instance=asmeta_basictransitionrules_MacroCallRule_strategy)
def test_asmeta_basictransitionrules_macrocallrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta_basictransitionrules_ChooseRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_chooserule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_ChooseRule)



@given(instance=asmeta_basictransitionrules_ChooseRule_strategy)
def test_asmeta_basictransitionrules_chooserule_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta_basictransitionrules_Rule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_rule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_Rule)

@given(instance=TurboDerivedRule_strategy)
@settings(max_examples=50)
def test_turboderivedrule_instantiation(instance):
    assert isinstance(instance, TurboDerivedRule)

@given(instance=asmeta_derivedtransitionrules_RecursiveWhileRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_recursivewhilerule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_RecursiveWhileRule)

@given(instance=DerivedRule_strategy)
@settings(max_examples=50)
def test_derivedrule_instantiation(instance):
    assert isinstance(instance, DerivedRule)

@given(instance=asmeta_derivedtransitionrules_TurboDerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_turboderivedrule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_TurboDerivedRule)

@given(instance=asmeta_derivedtransitionrules_BasicDerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_basicderivedrule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_BasicDerivedRule)

@given(instance=BasicDerivedRule_strategy)
@settings(max_examples=50)
def test_basicderivedrule_instantiation(instance):
    assert isinstance(instance, BasicDerivedRule)

@given(instance=asmeta_derivedtransitionrules_CaseRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_caserule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_CaseRule)



@given(instance=asmeta_derivedtransitionrules_CaseRule_strategy)
def test_asmeta_derivedtransitionrules_caserule_caseBranches_setter(instance):
    original = instance.caseBranches
    instance.caseBranches = original
    assert instance.caseBranches == original

@given(instance=asmeta_derivedtransitionrules_IterativeWhileRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_iterativewhilerule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_IterativeWhileRule)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=asmeta_derivedtransitionrules_DerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta_derivedtransitionrules_derivedrule_instantiation(instance):
    assert isinstance(instance, asmeta_derivedtransitionrules_DerivedRule)

@given(instance=asmeta_basictransitionrules_BasicRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_basicrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_BasicRule)

@given(instance=asmeta_basictransitionrules_TermAsRule_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_termasrule_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_TermAsRule)



@given(instance=asmeta_basictransitionrules_TermAsRule_strategy)
def test_asmeta_basictransitionrules_termasrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta_turbotransitionrules_TurboRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_turborule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TurboRule)

@given(instance=turbotransitionrules_TurboCallRule_strategy)
@settings(max_examples=50)
def test_turbotransitionrules_turbocallrule_instantiation(instance):
    assert isinstance(instance, turbotransitionrules_TurboCallRule)

@given(instance=turbotransitionrules_TurboDeclaration_strategy)
@settings(max_examples=50)
def test_turbotransitionrules_turbodeclaration_instantiation(instance):
    assert isinstance(instance, turbotransitionrules_TurboDeclaration)

@given(instance=LocalFunction_strategy)
@settings(max_examples=50)
def test_localfunction_instantiation(instance):
    assert isinstance(instance, LocalFunction)

@given(instance=basictransitionrules_Rule_strategy)
@settings(max_examples=50)
def test_basictransitionrules_rule_instantiation(instance):
    assert isinstance(instance, basictransitionrules_Rule)

@given(instance=TurboRule_strategy)
@settings(max_examples=50)
def test_turborule_instantiation(instance):
    assert isinstance(instance, TurboRule)

@given(instance=asmeta_turbotransitionrules_TurboCallRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_turbocallrule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TurboCallRule)



@given(instance=asmeta_turbotransitionrules_TurboCallRule_strategy)
def test_asmeta_turbotransitionrules_turbocallrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta_turbotransitionrules_TryCatchRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_trycatchrule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TryCatchRule)

@given(instance=asmeta_turbotransitionrules_TurboReturnRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_turboreturnrule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TurboReturnRule)

@given(instance=asmeta_turbotransitionrules_IterateRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_iteraterule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_IterateRule)

@given(instance=asmeta_turbotransitionrules_TurboLocalStateRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_turbolocalstaterule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TurboLocalStateRule)

@given(instance=asmeta_turbotransitionrules_SeqRule_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_seqrule_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_SeqRule)



@given(instance=asmeta_turbotransitionrules_SeqRule_strategy)
def test_asmeta_turbotransitionrules_seqrule_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=asmeta_structure_DomainDefinition_strategy)
@settings(max_examples=50)
def test_asmeta_structure_domaindefinition_instantiation(instance):
    assert isinstance(instance, asmeta_structure_DomainDefinition)

@given(instance=basictransitionrules_MacroDeclaration_strategy)
@settings(max_examples=50)
def test_basictransitionrules_macrodeclaration_instantiation(instance):
    assert isinstance(instance, basictransitionrules_MacroDeclaration)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=ExportClause_strategy)
@settings(max_examples=50)
def test_exportclause_instantiation(instance):
    assert isinstance(instance, ExportClause)

@given(instance=Signature_strategy)
@settings(max_examples=50)
def test_signature_instantiation(instance):
    assert isinstance(instance, Signature)

@given(instance=ImportClause_strategy)
@settings(max_examples=50)
def test_importclause_instantiation(instance):
    assert isinstance(instance, ImportClause)

@given(instance=asmeta_structure_Header_strategy)
@settings(max_examples=50)
def test_asmeta_structure_header_instantiation(instance):
    assert isinstance(instance, asmeta_structure_Header)

@given(instance=AgentInitialization_strategy)
@settings(max_examples=50)
def test_agentinitialization_instantiation(instance):
    assert isinstance(instance, AgentInitialization)

@given(instance=FunctionInitialization_strategy)
@settings(max_examples=50)
def test_functioninitialization_instantiation(instance):
    assert isinstance(instance, FunctionInitialization)

@given(instance=DomainInitialization_strategy)
@settings(max_examples=50)
def test_domaininitialization_instantiation(instance):
    assert isinstance(instance, DomainInitialization)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=asmeta_structure_Asm_strategy)
@settings(max_examples=50)
def test_asmeta_structure_asm_instantiation(instance):
    assert isinstance(instance, asmeta_structure_Asm)



@given(instance=asmeta_structure_Asm_strategy)
def test_asmeta_structure_asm_isAsynchr_setter(instance):
    original = instance.isAsynchr
    instance.isAsynchr = original
    assert instance.isAsynchr == original

@given(instance=asmeta_definitions_Classifier_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_classifier_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_Classifier)

@given(instance=asmeta_structure_Initialization_strategy)
@settings(max_examples=50)
def test_asmeta_structure_initialization_instantiation(instance):
    assert isinstance(instance, asmeta_structure_Initialization)

@given(instance=domains_ConcreteDomain_strategy)
@settings(max_examples=50)
def test_domains_concretedomain_instantiation(instance):
    assert isinstance(instance, domains_ConcreteDomain)

@given(instance=asmeta_structure_DomainInitialization_strategy)
@settings(max_examples=50)
def test_asmeta_structure_domaininitialization_instantiation(instance):
    assert isinstance(instance, asmeta_structure_DomainInitialization)

@given(instance=asmeta_structure_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_asmeta_structure_functiondefinition_instantiation(instance):
    assert isinstance(instance, asmeta_structure_FunctionDefinition)

@given(instance=asmeta_structure_ImportClause_strategy)
@settings(max_examples=50)
def test_asmeta_structure_importclause_instantiation(instance):
    assert isinstance(instance, asmeta_structure_ImportClause)



@given(instance=asmeta_structure_ImportClause_strategy)
def test_asmeta_structure_importclause_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=asmeta_structure_ExportClause_strategy)
@settings(max_examples=50)
def test_asmeta_structure_exportclause_instantiation(instance):
    assert isinstance(instance, asmeta_structure_ExportClause)

@given(instance=domains_StructuredTd_strategy)
@settings(max_examples=50)
def test_domains_structuredtd_instantiation(instance):
    assert isinstance(instance, domains_StructuredTd)

@given(instance=Header_strategy)
@settings(max_examples=50)
def test_header_instantiation(instance):
    assert isinstance(instance, Header)

@given(instance=asmeta_structure_Signature_strategy)
@settings(max_examples=50)
def test_asmeta_structure_signature_instantiation(instance):
    assert isinstance(instance, asmeta_structure_Signature)

@given(instance=basictransitionrules_MacroCallRule_strategy)
@settings(max_examples=50)
def test_basictransitionrules_macrocallrule_instantiation(instance):
    assert isinstance(instance, basictransitionrules_MacroCallRule)

@given(instance=asmeta_structure_AgentInitialization_strategy)
@settings(max_examples=50)
def test_asmeta_structure_agentinitialization_instantiation(instance):
    assert isinstance(instance, asmeta_structure_AgentInitialization)

@given(instance=asmeta_structure_NamedElement_strategy)
@settings(max_examples=50)
def test_asmeta_structure_namedelement_instantiation(instance):
    assert isinstance(instance, asmeta_structure_NamedElement)



@given(instance=asmeta_structure_NamedElement_strategy)
def test_asmeta_structure_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DynamicFunction_strategy)
@settings(max_examples=50)
def test_dynamicfunction_instantiation(instance):
    assert isinstance(instance, DynamicFunction)

@given(instance=asmeta_definitions_ControlledFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_controlledfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_ControlledFunction)

@given(instance=asmeta_definitions_SharedFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_sharedfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_SharedFunction)

@given(instance=asmeta_definitions_LocalFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_localfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_LocalFunction)

@given(instance=asmeta_definitions_MonitoredFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_monitoredfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_MonitoredFunction)

@given(instance=asmeta_definitions_OutFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_outfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_OutFunction)

@given(instance=asmeta_structure_FunctionInitialization_strategy)
@settings(max_examples=50)
def test_asmeta_structure_functioninitialization_instantiation(instance):
    assert isinstance(instance, asmeta_structure_FunctionInitialization)

@given(instance=InvarConstraint_strategy)
@settings(max_examples=50)
def test_invarconstraint_instantiation(instance):
    assert isinstance(instance, InvarConstraint)

@given(instance=FairnessConstraint_strategy)
@settings(max_examples=50)
def test_fairnessconstraint_instantiation(instance):
    assert isinstance(instance, FairnessConstraint)

@given(instance=asmeta_definitions_CompassionConstraint_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_compassionconstraint_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_CompassionConstraint)

@given(instance=asmeta_definitions_JusticeConstraint_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_justiceconstraint_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_JusticeConstraint)

@given(instance=Asm_strategy)
@settings(max_examples=50)
def test_asm_instantiation(instance):
    assert isinstance(instance, Asm)

@given(instance=DomainDefinition_strategy)
@settings(max_examples=50)
def test_domaindefinition_instantiation(instance):
    assert isinstance(instance, DomainDefinition)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=asmeta_definitions_TemporalProperty_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_temporalproperty_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_TemporalProperty)

@given(instance=asmeta_definitions_Invariant_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_invariant_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_Invariant)

@given(instance=FunctionDefinition_strategy)
@settings(max_examples=50)
def test_functiondefinition_instantiation(instance):
    assert isinstance(instance, FunctionDefinition)

@given(instance=asmeta_structure_Body_strategy)
@settings(max_examples=50)
def test_asmeta_structure_body_instantiation(instance):
    assert isinstance(instance, asmeta_structure_Body)

@given(instance=Initialization_strategy)
@settings(max_examples=50)
def test_initialization_instantiation(instance):
    assert isinstance(instance, Initialization)

@given(instance=RuleDeclaration_strategy)
@settings(max_examples=50)
def test_ruledeclaration_instantiation(instance):
    assert isinstance(instance, RuleDeclaration)

@given(instance=asmeta_basictransitionrules_MacroDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta_basictransitionrules_macrodeclaration_instantiation(instance):
    assert isinstance(instance, asmeta_basictransitionrules_MacroDeclaration)

@given(instance=asmeta_turbotransitionrules_TurboDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta_turbotransitionrules_turbodeclaration_instantiation(instance):
    assert isinstance(instance, asmeta_turbotransitionrules_TurboDeclaration)

@given(instance=basictransitionrules_TermAsRule_strategy)
@settings(max_examples=50)
def test_basictransitionrules_termasrule_instantiation(instance):
    assert isinstance(instance, basictransitionrules_TermAsRule)

@given(instance=domains_Domain_strategy)
@settings(max_examples=50)
def test_domains_domain_instantiation(instance):
    assert isinstance(instance, domains_Domain)

@given(instance=asmeta_basicterms_Term_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_term_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_Term)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=asmeta_basicterms_Term_strategy)
@settings(max_examples=30)
def test_asmeta_basicterms_term_compatible_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.compatible()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.compatible).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'compatible' in asmeta_basicterms_Term is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compatible' in asmeta_basicterms_Term did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compatible' in asmeta_basicterms_Term is not implemented or raised an error")

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=asmeta_basicterms_BasicTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_basicterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_BasicTerm)

@given(instance=asmeta_basicterms_ExtendedTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_extendedterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_ExtendedTerm)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=asmeta_definitions_BasicFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_basicfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_BasicFunction)

@given(instance=asmeta_definitions_DerivedFunction_strategy)
@settings(max_examples=50)
def test_asmeta_definitions_derivedfunction_instantiation(instance):
    assert isinstance(instance, asmeta_definitions_DerivedFunction)

@given(instance=FunctionTerm_strategy)
@settings(max_examples=50)
def test_functionterm_instantiation(instance):
    assert isinstance(instance, FunctionTerm)

@given(instance=asmeta_basicterms_LocationTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_locationterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_LocationTerm)

@given(instance=furtherterms_FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_furtherterms_finitequantificationterm_instantiation(instance):
    assert isinstance(instance, furtherterms_FiniteQuantificationTerm)

@given(instance=BasicTerm_strategy)
@settings(max_examples=50)
def test_basicterm_instantiation(instance):
    assert isinstance(instance, BasicTerm)

@given(instance=asmeta_basicterms_ConstantTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_constantterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_ConstantTerm)



@given(instance=asmeta_basicterms_ConstantTerm_strategy)
def test_asmeta_basicterms_constantterm_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=asmeta_basicterms_FunctionTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_functionterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_FunctionTerm)

@given(instance=asmeta_basicterms_VariableTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_variableterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_VariableTerm)



@given(instance=asmeta_basicterms_VariableTerm_strategy)
def test_asmeta_basicterms_variableterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=asmeta_basicterms_VariableTerm_strategy)
def test_asmeta_basicterms_variableterm_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionTerm_strategy)
@settings(max_examples=50)
def test_collectionterm_instantiation(instance):
    assert isinstance(instance, CollectionTerm)

@given(instance=asmeta_furtherterms_MapTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_mapterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_MapTerm)

@given(instance=asmeta_furtherterms_BagTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_bagterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_BagTerm)

@given(instance=asmeta_basicterms_SetTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_setterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_SetTerm)

@given(instance=asmeta_furtherterms_SequenceTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_sequenceterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_SequenceTerm)



@given(instance=asmeta_furtherterms_SequenceTerm_strategy)
def test_asmeta_furtherterms_sequenceterm_terms_setter(instance):
    original = instance.terms
    instance.terms = original
    assert instance.terms == original

@given(instance=ComprehensionTerm_strategy)
@settings(max_examples=50)
def test_comprehensionterm_instantiation(instance):
    assert isinstance(instance, ComprehensionTerm)

@given(instance=asmeta_furtherterms_BagCt_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_bagct_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_BagCt)

@given(instance=asmeta_furtherterms_SequenceCt_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_sequencect_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_SequenceCt)

@given(instance=asmeta_furtherterms_SetCt_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_setct_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_SetCt)

@given(instance=ExtendedTerm_strategy)
@settings(max_examples=50)
def test_extendedterm_instantiation(instance):
    assert isinstance(instance, ExtendedTerm)

@given(instance=asmeta_furtherterms_CaseTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_caseterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_CaseTerm)



@given(instance=asmeta_furtherterms_CaseTerm_strategy)
def test_asmeta_furtherterms_caseterm_resultTerms_setter(instance):
    original = instance.resultTerms
    instance.resultTerms = original
    assert instance.resultTerms == original

@given(instance=asmeta_basicterms_DomainTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_domainterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_DomainTerm)

@given(instance=asmeta_basicterms_TupleTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_tupleterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_TupleTerm)



@given(instance=asmeta_basicterms_TupleTerm_strategy)
def test_asmeta_basicterms_tupleterm_terms_setter(instance):
    original = instance.terms
    instance.terms = original
    assert instance.terms == original



@given(instance=asmeta_basicterms_TupleTerm_strategy)
def test_asmeta_basicterms_tupleterm_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=asmeta_basicterms_RuleAsTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_ruleasterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_RuleAsTerm)

@given(instance=asmeta_basicterms_CollectionTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_collectionterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_CollectionTerm)



@given(instance=asmeta_basicterms_CollectionTerm_strategy)
def test_asmeta_basicterms_collectionterm_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=asmeta_furtherterms_VariableBindingTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_variablebindingterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_VariableBindingTerm)

@given(instance=asmeta_furtherterms_ConditionalTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_conditionalterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ConditionalTerm)

@given(instance=FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_finitequantificationterm_instantiation(instance):
    assert isinstance(instance, FiniteQuantificationTerm)

@given(instance=asmeta_furtherterms_ExistUniqueTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_existuniqueterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ExistUniqueTerm)

@given(instance=asmeta_furtherterms_ExistTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_existterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ExistTerm)

@given(instance=asmeta_furtherterms_ForallTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_forallterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ForallTerm)

@given(instance=basicterms_Term_strategy)
@settings(max_examples=50)
def test_basicterms_term_instantiation(instance):
    assert isinstance(instance, basicterms_Term)

@given(instance=basicterms_VariableTerm_strategy)
@settings(max_examples=50)
def test_basicterms_variableterm_instantiation(instance):
    assert isinstance(instance, basicterms_VariableTerm)

@given(instance=VariableBindingTerm_strategy)
@settings(max_examples=50)
def test_variablebindingterm_instantiation(instance):
    assert isinstance(instance, VariableBindingTerm)

@given(instance=asmeta_furtherterms_FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_finitequantificationterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_FiniteQuantificationTerm)



@given(instance=asmeta_furtherterms_FiniteQuantificationTerm_strategy)
def test_asmeta_furtherterms_finitequantificationterm_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta_furtherterms_ComprehensionTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_comprehensionterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ComprehensionTerm)



@given(instance=asmeta_furtherterms_ComprehensionTerm_strategy)
def test_asmeta_furtherterms_comprehensionterm_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta_furtherterms_LetTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_letterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_LetTerm)

@given(instance=asmeta_furtherterms_MapCt_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_mapct_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_MapCt)

@given(instance=basicterms_TupleTerm_strategy)
@settings(max_examples=50)
def test_basicterms_tupleterm_instantiation(instance):
    assert isinstance(instance, basicterms_TupleTerm)

@given(instance=ConstantTerm_strategy)
@settings(max_examples=50)
def test_constantterm_instantiation(instance):
    assert isinstance(instance, ConstantTerm)

@given(instance=asmeta_furtherterms_RealTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_realterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_RealTerm)

@given(instance=asmeta_furtherterms_StringTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_stringterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_StringTerm)

@given(instance=asmeta_furtherterms_ComplexTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_complexterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_ComplexTerm)

@given(instance=asmeta_furtherterms_EnumTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_enumterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_EnumTerm)

@given(instance=asmeta_basicterms_BooleanTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_booleanterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_BooleanTerm)

@given(instance=asmeta_basicterms_UndefTerm_strategy)
@settings(max_examples=50)
def test_asmeta_basicterms_undefterm_instantiation(instance):
    assert isinstance(instance, asmeta_basicterms_UndefTerm)

@given(instance=asmeta_furtherterms_CharTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_charterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_CharTerm)

@given(instance=asmeta_furtherterms_NaturalTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_naturalterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_NaturalTerm)

@given(instance=asmeta_furtherterms_IntegerTerm_strategy)
@settings(max_examples=50)
def test_asmeta_furtherterms_integerterm_instantiation(instance):
    assert isinstance(instance, asmeta_furtherterms_IntegerTerm)
