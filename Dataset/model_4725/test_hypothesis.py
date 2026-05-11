import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    domains::TypeDomain,
    asmeta::domains::EnumElement,
    domains::EnumElement,
    RealDomain,
    asmeta::domains::IntegerDomain,
    ComplexDomain,
    asmeta::domains::RealDomain,
    AbstractTd,
    asmeta::domains::AgentDomain,
    asmeta::domains::ReserveDomain,
    StructuredTd,
    asmeta::domains::ProductDomain,
    asmeta::domains::RuleDomain,
    asmeta::domains::MapDomain,
    asmeta::domains::BagDomain,
    asmeta::domains::PowersetDomain,
    asmeta::domains::SequenceDomain,
    TypeDomain,
    asmeta::domains::BasicTd,
    asmeta::domains::AnyDomain,
    asmeta::domains::EnumTd,
    asmeta::domains::AbstractTd,
    asmeta::domains::StructuredTd,
    Domain,
    asmeta::domains::ConcreteDomain,
    asmeta::domains::TypeDomain,
    BasicTd,
    asmeta::domains::StringDomain,
    asmeta::domains::CharDomain,
    asmeta::domains::ComplexDomain,
    asmeta::domains::BooleanDomain,
    asmeta::domains::UndefDomain,
    IntegerDomain,
    asmeta::domains::NaturalDomain,
    BasicFunction,
    asmeta::definitions::StaticFunction,
    asmeta::definitions::DynamicFunction,
    Invariant,
    Classifier,
    asmeta::definitions::Function,
    asmeta::domains::Domain,
    asmeta::definitions::Property,
    asmeta::definitions::RuleDeclaration,
    BasicRule,
    asmeta::basictransitionrules::LetRule,
    asmeta::basictransitionrules::ForallRule,
    asmeta::basictransitionrules::UpdateRule,
    asmeta::basictransitionrules::BlockRule,
    asmeta::basictransitionrules::ConditionalRule,
    asmeta::basictransitionrules::MacroCallRule,
    asmeta::basictransitionrules::ExtendRule,
    asmeta::basictransitionrules::SkipRule,
    asmeta::basictransitionrules::ChooseRule,
    asmeta::basictransitionrules::Rule,
    DerivedRule,
    asmeta::derivedtransitionrules::TurboDerivedRule,
    asmeta::derivedtransitionrules::BasicDerivedRule,
    BasicDerivedRule,
    asmeta::derivedtransitionrules::CaseRule,
    TurboDerivedRule,
    asmeta::derivedtransitionrules::IterativeWhileRule,
    asmeta::derivedtransitionrules::RecursiveWhileRule,
    turbotransitionrules::TurboCallRule,
    turbotransitionrules::TurboDeclaration,
    LocalFunction,
    basictransitionrules::Rule,
    TurboRule,
    asmeta::turbotransitionrules::TurboCallRule,
    asmeta::turbotransitionrules::IterateRule,
    asmeta::turbotransitionrules::TurboReturnRule,
    asmeta::turbotransitionrules::TryCatchRule,
    asmeta::turbotransitionrules::TurboLocalStateRule,
    asmeta::turbotransitionrules::SeqRule,
    Rule,
    asmeta::derivedtransitionrules::DerivedRule,
    asmeta::basictransitionrules::BasicRule,
    asmeta::basictransitionrules::TermAsRule,
    asmeta::turbotransitionrules::TurboRule,
    basictransitionrules::MacroDeclaration,
    Body,
    ExportClause,
    Signature,
    ImportClause,
    asmeta::structure::Header,
    AgentInitialization,
    FunctionInitialization,
    DomainInitialization,
    NamedElement,
    asmeta::structure::Asm,
    asmeta::definitions::Classifier,
    asmeta::structure::Initialization,
    asmeta::structure::DomainDefinition,
    asmeta::structure::FunctionDefinition,
    asmeta::structure::ImportClause,
    asmeta::structure::ExportClause,
    domains::StructuredTd,
    Header,
    asmeta::structure::Signature,
    domains::ConcreteDomain,
    asmeta::structure::DomainInitialization,
    DynamicFunction,
    asmeta::definitions::LocalFunction,
    asmeta::definitions::OutFunction,
    asmeta::definitions::SharedFunction,
    asmeta::definitions::ControlledFunction,
    asmeta::definitions::MonitoredFunction,
    asmeta::structure::FunctionInitialization,
    Asm,
    DomainDefinition,
    Property,
    asmeta::definitions::Invariant,
    FunctionDefinition,
    asmeta::structure::Body,
    Initialization,
    basictransitionrules::MacroCallRule,
    asmeta::structure::AgentInitialization,
    asmeta::structure::NamedElement,
    basictransitionrules::TermAsRule,
    domains::Domain,
    asmeta::basicterms::Term,
    Term,
    asmeta::basicterms::BasicTerm,
    asmeta::basicterms::ExtendedTerm,
    Function,
    asmeta::definitions::DerivedFunction,
    asmeta::definitions::BasicFunction,
    FunctionTerm,
    asmeta::basicterms::LocationTerm,
    RuleDeclaration,
    asmeta::turbotransitionrules::TurboDeclaration,
    asmeta::basictransitionrules::MacroDeclaration,
    furtherterms::FiniteQuantificationTerm,
    BasicTerm,
    asmeta::basicterms::FunctionTerm,
    asmeta::basicterms::ConstantTerm,
    asmeta::basicterms::VariableTerm,
    FiniteQuantificationTerm,
    asmeta::furtherterms::ExistTerm,
    asmeta::furtherterms::ExistUniqueTerm,
    asmeta::furtherterms::ForallTerm,
    basicterms::Term,
    basicterms::VariableTerm,
    VariableBindingTerm,
    asmeta::furtherterms::FiniteQuantificationTerm,
    asmeta::furtherterms::ComprehensionTerm,
    asmeta::furtherterms::LetTerm,
    basicterms::TupleTerm,
    CollectionTerm,
    asmeta::furtherterms::MapTerm,
    asmeta::basicterms::SetTerm,
    asmeta::furtherterms::BagTerm,
    asmeta::furtherterms::SequenceTerm,
    ComprehensionTerm,
    asmeta::furtherterms::SequenceCt,
    asmeta::furtherterms::BagCt,
    asmeta::furtherterms::MapCt,
    asmeta::furtherterms::SetCt,
    ExtendedTerm,
    asmeta::furtherterms::ConditionalTerm,
    asmeta::basicterms::RuleAsTerm,
    asmeta::basicterms::CollectionTerm,
    asmeta::basicterms::TupleTerm,
    asmeta::furtherterms::CaseTerm,
    asmeta::basicterms::DomainTerm,
    asmeta::furtherterms::VariableBindingTerm,
    ConstantTerm,
    asmeta::furtherterms::RealTerm,
    asmeta::furtherterms::EnumTerm,
    asmeta::basicterms::UndefTerm,
    asmeta::furtherterms::StringTerm,
    asmeta::furtherterms::NaturalTerm,
    asmeta::furtherterms::CharTerm,
    asmeta::furtherterms::ComplexTerm,
    asmeta::basicterms::BooleanTerm,
    asmeta::furtherterms::IntegerTerm,
    VariableKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domains::typedomain_is_not_abstract():
    assert not inspect.isabstract(domains::TypeDomain)


def test_domains::typedomain_constructor_exists():
    assert callable(domains::TypeDomain.__init__)


def test_domains::typedomain_constructor_args():
    sig = inspect.signature(domains::TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::enumelement_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::EnumElement)


def test_asmeta::domains::enumelement_constructor_exists():
    assert callable(asmeta::domains::EnumElement.__init__)


def test_asmeta::domains::enumelement_constructor_args():
    sig = inspect.signature(asmeta::domains::EnumElement.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_asmeta::domains::enumelement_has_symbol():
    assert hasattr(asmeta::domains::EnumElement, "symbol")
    descriptor = None
    for klass in asmeta::domains::EnumElement.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_domains::enumelement_is_not_abstract():
    assert not inspect.isabstract(domains::EnumElement)


def test_domains::enumelement_constructor_exists():
    assert callable(domains::EnumElement.__init__)


def test_domains::enumelement_constructor_args():
    sig = inspect.signature(domains::EnumElement.__init__)
    params = list(sig.parameters.keys())



def test_realdomain_is_not_abstract():
    assert not inspect.isabstract(RealDomain)


def test_realdomain_constructor_exists():
    assert callable(RealDomain.__init__)


def test_realdomain_constructor_args():
    sig = inspect.signature(RealDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::integerdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::IntegerDomain)


def test_asmeta::domains::integerdomain_constructor_exists():
    assert callable(asmeta::domains::IntegerDomain.__init__)


def test_asmeta::domains::integerdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::IntegerDomain.__init__)
    params = list(sig.parameters.keys())



def test_complexdomain_is_not_abstract():
    assert not inspect.isabstract(ComplexDomain)


def test_complexdomain_constructor_exists():
    assert callable(ComplexDomain.__init__)


def test_complexdomain_constructor_args():
    sig = inspect.signature(ComplexDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::realdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::RealDomain)


def test_asmeta::domains::realdomain_constructor_exists():
    assert callable(asmeta::domains::RealDomain.__init__)


def test_asmeta::domains::realdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::RealDomain.__init__)
    params = list(sig.parameters.keys())



def test_abstracttd_is_not_abstract():
    assert not inspect.isabstract(AbstractTd)


def test_abstracttd_constructor_exists():
    assert callable(AbstractTd.__init__)


def test_abstracttd_constructor_args():
    sig = inspect.signature(AbstractTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::agentdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::AgentDomain)


def test_asmeta::domains::agentdomain_constructor_exists():
    assert callable(asmeta::domains::AgentDomain.__init__)


def test_asmeta::domains::agentdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::AgentDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::reservedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::ReserveDomain)


def test_asmeta::domains::reservedomain_constructor_exists():
    assert callable(asmeta::domains::ReserveDomain.__init__)


def test_asmeta::domains::reservedomain_constructor_args():
    sig = inspect.signature(asmeta::domains::ReserveDomain.__init__)
    params = list(sig.parameters.keys())



def test_structuredtd_is_not_abstract():
    assert not inspect.isabstract(StructuredTd)


def test_structuredtd_constructor_exists():
    assert callable(StructuredTd.__init__)


def test_structuredtd_constructor_args():
    sig = inspect.signature(StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::productdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::ProductDomain)


def test_asmeta::domains::productdomain_constructor_exists():
    assert callable(asmeta::domains::ProductDomain.__init__)


def test_asmeta::domains::productdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::ProductDomain.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"

def test_asmeta::domains::productdomain_has_domains():
    assert hasattr(asmeta::domains::ProductDomain, "domains")
    descriptor = None
    for klass in asmeta::domains::ProductDomain.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::domains::ruledomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::RuleDomain)


def test_asmeta::domains::ruledomain_constructor_exists():
    assert callable(asmeta::domains::RuleDomain.__init__)


def test_asmeta::domains::ruledomain_constructor_args():
    sig = inspect.signature(asmeta::domains::RuleDomain.__init__)
    params = list(sig.parameters.keys())
    assert "domains" in params, "Missing parameter 'domains'"

def test_asmeta::domains::ruledomain_has_domains():
    assert hasattr(asmeta::domains::RuleDomain, "domains")
    descriptor = None
    for klass in asmeta::domains::RuleDomain.__mro__:
        if "domains" in klass.__dict__:
            descriptor = klass.__dict__["domains"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::domains::mapdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::MapDomain)


def test_asmeta::domains::mapdomain_constructor_exists():
    assert callable(asmeta::domains::MapDomain.__init__)


def test_asmeta::domains::mapdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::MapDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::bagdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::BagDomain)


def test_asmeta::domains::bagdomain_constructor_exists():
    assert callable(asmeta::domains::BagDomain.__init__)


def test_asmeta::domains::bagdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::BagDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::powersetdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::PowersetDomain)


def test_asmeta::domains::powersetdomain_constructor_exists():
    assert callable(asmeta::domains::PowersetDomain.__init__)


def test_asmeta::domains::powersetdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::PowersetDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::sequencedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::SequenceDomain)


def test_asmeta::domains::sequencedomain_constructor_exists():
    assert callable(asmeta::domains::SequenceDomain.__init__)


def test_asmeta::domains::sequencedomain_constructor_args():
    sig = inspect.signature(asmeta::domains::SequenceDomain.__init__)
    params = list(sig.parameters.keys())



def test_typedomain_is_not_abstract():
    assert not inspect.isabstract(TypeDomain)


def test_typedomain_constructor_exists():
    assert callable(TypeDomain.__init__)


def test_typedomain_constructor_args():
    sig = inspect.signature(TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::basictd_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::BasicTd)


def test_asmeta::domains::basictd_constructor_exists():
    assert callable(asmeta::domains::BasicTd.__init__)


def test_asmeta::domains::basictd_constructor_args():
    sig = inspect.signature(asmeta::domains::BasicTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::anydomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::AnyDomain)


def test_asmeta::domains::anydomain_constructor_exists():
    assert callable(asmeta::domains::AnyDomain.__init__)


def test_asmeta::domains::anydomain_constructor_args():
    sig = inspect.signature(asmeta::domains::AnyDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::enumtd_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::EnumTd)


def test_asmeta::domains::enumtd_constructor_exists():
    assert callable(asmeta::domains::EnumTd.__init__)


def test_asmeta::domains::enumtd_constructor_args():
    sig = inspect.signature(asmeta::domains::EnumTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::abstracttd_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::AbstractTd)


def test_asmeta::domains::abstracttd_constructor_exists():
    assert callable(asmeta::domains::AbstractTd.__init__)


def test_asmeta::domains::abstracttd_constructor_args():
    sig = inspect.signature(asmeta::domains::AbstractTd.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_asmeta::domains::abstracttd_has_isDynamic():
    assert hasattr(asmeta::domains::AbstractTd, "isDynamic")
    descriptor = None
    for klass in asmeta::domains::AbstractTd.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::domains::structuredtd_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::StructuredTd)


def test_asmeta::domains::structuredtd_constructor_exists():
    assert callable(asmeta::domains::StructuredTd.__init__)


def test_asmeta::domains::structuredtd_constructor_args():
    sig = inspect.signature(asmeta::domains::StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::concretedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::ConcreteDomain)


def test_asmeta::domains::concretedomain_constructor_exists():
    assert callable(asmeta::domains::ConcreteDomain.__init__)


def test_asmeta::domains::concretedomain_constructor_args():
    sig = inspect.signature(asmeta::domains::ConcreteDomain.__init__)
    params = list(sig.parameters.keys())
    assert "isDynamic" in params, "Missing parameter 'isDynamic'"

def test_asmeta::domains::concretedomain_has_isDynamic():
    assert hasattr(asmeta::domains::ConcreteDomain, "isDynamic")
    descriptor = None
    for klass in asmeta::domains::ConcreteDomain.__mro__:
        if "isDynamic" in klass.__dict__:
            descriptor = klass.__dict__["isDynamic"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::domains::typedomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::TypeDomain)


def test_asmeta::domains::typedomain_constructor_exists():
    assert callable(asmeta::domains::TypeDomain.__init__)


def test_asmeta::domains::typedomain_constructor_args():
    sig = inspect.signature(asmeta::domains::TypeDomain.__init__)
    params = list(sig.parameters.keys())



def test_basictd_is_not_abstract():
    assert not inspect.isabstract(BasicTd)


def test_basictd_constructor_exists():
    assert callable(BasicTd.__init__)


def test_basictd_constructor_args():
    sig = inspect.signature(BasicTd.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::stringdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::StringDomain)


def test_asmeta::domains::stringdomain_constructor_exists():
    assert callable(asmeta::domains::StringDomain.__init__)


def test_asmeta::domains::stringdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::StringDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::chardomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::CharDomain)


def test_asmeta::domains::chardomain_constructor_exists():
    assert callable(asmeta::domains::CharDomain.__init__)


def test_asmeta::domains::chardomain_constructor_args():
    sig = inspect.signature(asmeta::domains::CharDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::complexdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::ComplexDomain)


def test_asmeta::domains::complexdomain_constructor_exists():
    assert callable(asmeta::domains::ComplexDomain.__init__)


def test_asmeta::domains::complexdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::ComplexDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::booleandomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::BooleanDomain)


def test_asmeta::domains::booleandomain_constructor_exists():
    assert callable(asmeta::domains::BooleanDomain.__init__)


def test_asmeta::domains::booleandomain_constructor_args():
    sig = inspect.signature(asmeta::domains::BooleanDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::undefdomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::UndefDomain)


def test_asmeta::domains::undefdomain_constructor_exists():
    assert callable(asmeta::domains::UndefDomain.__init__)


def test_asmeta::domains::undefdomain_constructor_args():
    sig = inspect.signature(asmeta::domains::UndefDomain.__init__)
    params = list(sig.parameters.keys())



def test_integerdomain_is_not_abstract():
    assert not inspect.isabstract(IntegerDomain)


def test_integerdomain_constructor_exists():
    assert callable(IntegerDomain.__init__)


def test_integerdomain_constructor_args():
    sig = inspect.signature(IntegerDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::domains::naturaldomain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::NaturalDomain)


def test_asmeta::domains::naturaldomain_constructor_exists():
    assert callable(asmeta::domains::NaturalDomain.__init__)


def test_asmeta::domains::naturaldomain_constructor_args():
    sig = inspect.signature(asmeta::domains::NaturalDomain.__init__)
    params = list(sig.parameters.keys())



def test_basicfunction_is_not_abstract():
    assert not inspect.isabstract(BasicFunction)


def test_basicfunction_constructor_exists():
    assert callable(BasicFunction.__init__)


def test_basicfunction_constructor_args():
    sig = inspect.signature(BasicFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::staticfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::StaticFunction)


def test_asmeta::definitions::staticfunction_constructor_exists():
    assert callable(asmeta::definitions::StaticFunction.__init__)


def test_asmeta::definitions::staticfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::StaticFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::dynamicfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::DynamicFunction)


def test_asmeta::definitions::dynamicfunction_constructor_exists():
    assert callable(asmeta::definitions::DynamicFunction.__init__)


def test_asmeta::definitions::dynamicfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::DynamicFunction.__init__)
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



def test_asmeta::definitions::function_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::Function)


def test_asmeta::definitions::function_constructor_exists():
    assert callable(asmeta::definitions::Function.__init__)


def test_asmeta::definitions::function_constructor_args():
    sig = inspect.signature(asmeta::definitions::Function.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"

def test_asmeta::definitions::function_has_arity():
    assert hasattr(asmeta::definitions::Function, "arity")
    descriptor = None
    for klass in asmeta::definitions::Function.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::domains::domain_is_not_abstract():
    assert not inspect.isabstract(asmeta::domains::Domain)


def test_asmeta::domains::domain_constructor_exists():
    assert callable(asmeta::domains::Domain.__init__)


def test_asmeta::domains::domain_constructor_args():
    sig = inspect.signature(asmeta::domains::Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::property_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::Property)


def test_asmeta::definitions::property_constructor_exists():
    assert callable(asmeta::definitions::Property.__init__)


def test_asmeta::definitions::property_constructor_args():
    sig = inspect.signature(asmeta::definitions::Property.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::RuleDeclaration)


def test_asmeta::definitions::ruledeclaration_constructor_exists():
    assert callable(asmeta::definitions::RuleDeclaration.__init__)


def test_asmeta::definitions::ruledeclaration_constructor_args():
    sig = inspect.signature(asmeta::definitions::RuleDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"

def test_asmeta::definitions::ruledeclaration_has_arity():
    assert hasattr(asmeta::definitions::RuleDeclaration, "arity")
    descriptor = None
    for klass in asmeta::definitions::RuleDeclaration.__mro__:
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



def test_asmeta::basictransitionrules::letrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::LetRule)


def test_asmeta::basictransitionrules::letrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::LetRule.__init__)


def test_asmeta::basictransitionrules::letrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::LetRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::forallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::ForallRule)


def test_asmeta::basictransitionrules::forallrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::ForallRule.__init__)


def test_asmeta::basictransitionrules::forallrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::ForallRule.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta::basictransitionrules::forallrule_has_ranges():
    assert hasattr(asmeta::basictransitionrules::ForallRule, "ranges")
    descriptor = None
    for klass in asmeta::basictransitionrules::ForallRule.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basictransitionrules::updaterule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::UpdateRule)


def test_asmeta::basictransitionrules::updaterule_constructor_exists():
    assert callable(asmeta::basictransitionrules::UpdateRule.__init__)


def test_asmeta::basictransitionrules::updaterule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::UpdateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::blockrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::BlockRule)


def test_asmeta::basictransitionrules::blockrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::BlockRule.__init__)


def test_asmeta::basictransitionrules::blockrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::BlockRule.__init__)
    params = list(sig.parameters.keys())
    assert "rules" in params, "Missing parameter 'rules'"

def test_asmeta::basictransitionrules::blockrule_has_rules():
    assert hasattr(asmeta::basictransitionrules::BlockRule, "rules")
    descriptor = None
    for klass in asmeta::basictransitionrules::BlockRule.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basictransitionrules::conditionalrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::ConditionalRule)


def test_asmeta::basictransitionrules::conditionalrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::ConditionalRule.__init__)


def test_asmeta::basictransitionrules::conditionalrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::ConditionalRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::macrocallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::MacroCallRule)


def test_asmeta::basictransitionrules::macrocallrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::MacroCallRule.__init__)


def test_asmeta::basictransitionrules::macrocallrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::MacroCallRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta::basictransitionrules::macrocallrule_has_parameters():
    assert hasattr(asmeta::basictransitionrules::MacroCallRule, "parameters")
    descriptor = None
    for klass in asmeta::basictransitionrules::MacroCallRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basictransitionrules::extendrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::ExtendRule)


def test_asmeta::basictransitionrules::extendrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::ExtendRule.__init__)


def test_asmeta::basictransitionrules::extendrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::ExtendRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::skiprule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::SkipRule)


def test_asmeta::basictransitionrules::skiprule_constructor_exists():
    assert callable(asmeta::basictransitionrules::SkipRule.__init__)


def test_asmeta::basictransitionrules::skiprule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::SkipRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::chooserule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::ChooseRule)


def test_asmeta::basictransitionrules::chooserule_constructor_exists():
    assert callable(asmeta::basictransitionrules::ChooseRule.__init__)


def test_asmeta::basictransitionrules::chooserule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::ChooseRule.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta::basictransitionrules::chooserule_has_ranges():
    assert hasattr(asmeta::basictransitionrules::ChooseRule, "ranges")
    descriptor = None
    for klass in asmeta::basictransitionrules::ChooseRule.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basictransitionrules::rule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::Rule)


def test_asmeta::basictransitionrules::rule_constructor_exists():
    assert callable(asmeta::basictransitionrules::Rule.__init__)


def test_asmeta::basictransitionrules::rule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::Rule.__init__)
    params = list(sig.parameters.keys())



def test_derivedrule_is_not_abstract():
    assert not inspect.isabstract(DerivedRule)


def test_derivedrule_constructor_exists():
    assert callable(DerivedRule.__init__)


def test_derivedrule_constructor_args():
    sig = inspect.signature(DerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::turboderivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::TurboDerivedRule)


def test_asmeta::derivedtransitionrules::turboderivedrule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::TurboDerivedRule.__init__)


def test_asmeta::derivedtransitionrules::turboderivedrule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::TurboDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::basicderivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::BasicDerivedRule)


def test_asmeta::derivedtransitionrules::basicderivedrule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::BasicDerivedRule.__init__)


def test_asmeta::derivedtransitionrules::basicderivedrule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::BasicDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_basicderivedrule_is_not_abstract():
    assert not inspect.isabstract(BasicDerivedRule)


def test_basicderivedrule_constructor_exists():
    assert callable(BasicDerivedRule.__init__)


def test_basicderivedrule_constructor_args():
    sig = inspect.signature(BasicDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::caserule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::CaseRule)


def test_asmeta::derivedtransitionrules::caserule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::CaseRule.__init__)


def test_asmeta::derivedtransitionrules::caserule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::CaseRule.__init__)
    params = list(sig.parameters.keys())
    assert "caseBranches" in params, "Missing parameter 'caseBranches'"

def test_asmeta::derivedtransitionrules::caserule_has_caseBranches():
    assert hasattr(asmeta::derivedtransitionrules::CaseRule, "caseBranches")
    descriptor = None
    for klass in asmeta::derivedtransitionrules::CaseRule.__mro__:
        if "caseBranches" in klass.__dict__:
            descriptor = klass.__dict__["caseBranches"]
            break
    assert isinstance(descriptor, property)



def test_turboderivedrule_is_not_abstract():
    assert not inspect.isabstract(TurboDerivedRule)


def test_turboderivedrule_constructor_exists():
    assert callable(TurboDerivedRule.__init__)


def test_turboderivedrule_constructor_args():
    sig = inspect.signature(TurboDerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::iterativewhilerule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::IterativeWhileRule)


def test_asmeta::derivedtransitionrules::iterativewhilerule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::IterativeWhileRule.__init__)


def test_asmeta::derivedtransitionrules::iterativewhilerule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::IterativeWhileRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::recursivewhilerule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::RecursiveWhileRule)


def test_asmeta::derivedtransitionrules::recursivewhilerule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::RecursiveWhileRule.__init__)


def test_asmeta::derivedtransitionrules::recursivewhilerule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::RecursiveWhileRule.__init__)
    params = list(sig.parameters.keys())



def test_turbotransitionrules::turbocallrule_is_not_abstract():
    assert not inspect.isabstract(turbotransitionrules::TurboCallRule)


def test_turbotransitionrules::turbocallrule_constructor_exists():
    assert callable(turbotransitionrules::TurboCallRule.__init__)


def test_turbotransitionrules::turbocallrule_constructor_args():
    sig = inspect.signature(turbotransitionrules::TurboCallRule.__init__)
    params = list(sig.parameters.keys())



def test_turbotransitionrules::turbodeclaration_is_not_abstract():
    assert not inspect.isabstract(turbotransitionrules::TurboDeclaration)


def test_turbotransitionrules::turbodeclaration_constructor_exists():
    assert callable(turbotransitionrules::TurboDeclaration.__init__)


def test_turbotransitionrules::turbodeclaration_constructor_args():
    sig = inspect.signature(turbotransitionrules::TurboDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_localfunction_is_not_abstract():
    assert not inspect.isabstract(LocalFunction)


def test_localfunction_constructor_exists():
    assert callable(LocalFunction.__init__)


def test_localfunction_constructor_args():
    sig = inspect.signature(LocalFunction.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules::rule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules::Rule)


def test_basictransitionrules::rule_constructor_exists():
    assert callable(basictransitionrules::Rule.__init__)


def test_basictransitionrules::rule_constructor_args():
    sig = inspect.signature(basictransitionrules::Rule.__init__)
    params = list(sig.parameters.keys())



def test_turborule_is_not_abstract():
    assert not inspect.isabstract(TurboRule)


def test_turborule_constructor_exists():
    assert callable(TurboRule.__init__)


def test_turborule_constructor_args():
    sig = inspect.signature(TurboRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::turbocallrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TurboCallRule)


def test_asmeta::turbotransitionrules::turbocallrule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TurboCallRule.__init__)


def test_asmeta::turbotransitionrules::turbocallrule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TurboCallRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta::turbotransitionrules::turbocallrule_has_parameters():
    assert hasattr(asmeta::turbotransitionrules::TurboCallRule, "parameters")
    descriptor = None
    for klass in asmeta::turbotransitionrules::TurboCallRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::turbotransitionrules::iteraterule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::IterateRule)


def test_asmeta::turbotransitionrules::iteraterule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::IterateRule.__init__)


def test_asmeta::turbotransitionrules::iteraterule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::IterateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::turboreturnrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TurboReturnRule)


def test_asmeta::turbotransitionrules::turboreturnrule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TurboReturnRule.__init__)


def test_asmeta::turbotransitionrules::turboreturnrule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TurboReturnRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::trycatchrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TryCatchRule)


def test_asmeta::turbotransitionrules::trycatchrule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TryCatchRule.__init__)


def test_asmeta::turbotransitionrules::trycatchrule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TryCatchRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::turbolocalstaterule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TurboLocalStateRule)


def test_asmeta::turbotransitionrules::turbolocalstaterule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TurboLocalStateRule.__init__)


def test_asmeta::turbotransitionrules::turbolocalstaterule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TurboLocalStateRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::seqrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::SeqRule)


def test_asmeta::turbotransitionrules::seqrule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::SeqRule.__init__)


def test_asmeta::turbotransitionrules::seqrule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::SeqRule.__init__)
    params = list(sig.parameters.keys())
    assert "rules" in params, "Missing parameter 'rules'"

def test_asmeta::turbotransitionrules::seqrule_has_rules():
    assert hasattr(asmeta::turbotransitionrules::SeqRule, "rules")
    descriptor = None
    for klass in asmeta::turbotransitionrules::SeqRule.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::derivedtransitionrules::derivedrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::derivedtransitionrules::DerivedRule)


def test_asmeta::derivedtransitionrules::derivedrule_constructor_exists():
    assert callable(asmeta::derivedtransitionrules::DerivedRule.__init__)


def test_asmeta::derivedtransitionrules::derivedrule_constructor_args():
    sig = inspect.signature(asmeta::derivedtransitionrules::DerivedRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::basicrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::BasicRule)


def test_asmeta::basictransitionrules::basicrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::BasicRule.__init__)


def test_asmeta::basictransitionrules::basicrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::BasicRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::termasrule_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::TermAsRule)


def test_asmeta::basictransitionrules::termasrule_constructor_exists():
    assert callable(asmeta::basictransitionrules::TermAsRule.__init__)


def test_asmeta::basictransitionrules::termasrule_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::TermAsRule.__init__)
    params = list(sig.parameters.keys())
    assert "parameters" in params, "Missing parameter 'parameters'"

def test_asmeta::basictransitionrules::termasrule_has_parameters():
    assert hasattr(asmeta::basictransitionrules::TermAsRule, "parameters")
    descriptor = None
    for klass in asmeta::basictransitionrules::TermAsRule.__mro__:
        if "parameters" in klass.__dict__:
            descriptor = klass.__dict__["parameters"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::turbotransitionrules::turborule_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TurboRule)


def test_asmeta::turbotransitionrules::turborule_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TurboRule.__init__)


def test_asmeta::turbotransitionrules::turborule_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TurboRule.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules::macrodeclaration_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules::MacroDeclaration)


def test_basictransitionrules::macrodeclaration_constructor_exists():
    assert callable(basictransitionrules::MacroDeclaration.__init__)


def test_basictransitionrules::macrodeclaration_constructor_args():
    sig = inspect.signature(basictransitionrules::MacroDeclaration.__init__)
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



def test_asmeta::structure::header_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::Header)


def test_asmeta::structure::header_constructor_exists():
    assert callable(asmeta::structure::Header.__init__)


def test_asmeta::structure::header_constructor_args():
    sig = inspect.signature(asmeta::structure::Header.__init__)
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



def test_asmeta::structure::asm_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::Asm)


def test_asmeta::structure::asm_constructor_exists():
    assert callable(asmeta::structure::Asm.__init__)


def test_asmeta::structure::asm_constructor_args():
    sig = inspect.signature(asmeta::structure::Asm.__init__)
    params = list(sig.parameters.keys())
    assert "isAsynchr" in params, "Missing parameter 'isAsynchr'"

def test_asmeta::structure::asm_has_isAsynchr():
    assert hasattr(asmeta::structure::Asm, "isAsynchr")
    descriptor = None
    for klass in asmeta::structure::Asm.__mro__:
        if "isAsynchr" in klass.__dict__:
            descriptor = klass.__dict__["isAsynchr"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::definitions::classifier_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::Classifier)


def test_asmeta::definitions::classifier_constructor_exists():
    assert callable(asmeta::definitions::Classifier.__init__)


def test_asmeta::definitions::classifier_constructor_args():
    sig = inspect.signature(asmeta::definitions::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::initialization_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::Initialization)


def test_asmeta::structure::initialization_constructor_exists():
    assert callable(asmeta::structure::Initialization.__init__)


def test_asmeta::structure::initialization_constructor_args():
    sig = inspect.signature(asmeta::structure::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::domaindefinition_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::DomainDefinition)


def test_asmeta::structure::domaindefinition_constructor_exists():
    assert callable(asmeta::structure::DomainDefinition.__init__)


def test_asmeta::structure::domaindefinition_constructor_args():
    sig = inspect.signature(asmeta::structure::DomainDefinition.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::FunctionDefinition)


def test_asmeta::structure::functiondefinition_constructor_exists():
    assert callable(asmeta::structure::FunctionDefinition.__init__)


def test_asmeta::structure::functiondefinition_constructor_args():
    sig = inspect.signature(asmeta::structure::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::importclause_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::ImportClause)


def test_asmeta::structure::importclause_constructor_exists():
    assert callable(asmeta::structure::ImportClause.__init__)


def test_asmeta::structure::importclause_constructor_args():
    sig = inspect.signature(asmeta::structure::ImportClause.__init__)
    params = list(sig.parameters.keys())
    assert "moduleName" in params, "Missing parameter 'moduleName'"

def test_asmeta::structure::importclause_has_moduleName():
    assert hasattr(asmeta::structure::ImportClause, "moduleName")
    descriptor = None
    for klass in asmeta::structure::ImportClause.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::structure::exportclause_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::ExportClause)


def test_asmeta::structure::exportclause_constructor_exists():
    assert callable(asmeta::structure::ExportClause.__init__)


def test_asmeta::structure::exportclause_constructor_args():
    sig = inspect.signature(asmeta::structure::ExportClause.__init__)
    params = list(sig.parameters.keys())



def test_domains::structuredtd_is_not_abstract():
    assert not inspect.isabstract(domains::StructuredTd)


def test_domains::structuredtd_constructor_exists():
    assert callable(domains::StructuredTd.__init__)


def test_domains::structuredtd_constructor_args():
    sig = inspect.signature(domains::StructuredTd.__init__)
    params = list(sig.parameters.keys())



def test_header_is_not_abstract():
    assert not inspect.isabstract(Header)


def test_header_constructor_exists():
    assert callable(Header.__init__)


def test_header_constructor_args():
    sig = inspect.signature(Header.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::signature_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::Signature)


def test_asmeta::structure::signature_constructor_exists():
    assert callable(asmeta::structure::Signature.__init__)


def test_asmeta::structure::signature_constructor_args():
    sig = inspect.signature(asmeta::structure::Signature.__init__)
    params = list(sig.parameters.keys())



def test_domains::concretedomain_is_not_abstract():
    assert not inspect.isabstract(domains::ConcreteDomain)


def test_domains::concretedomain_constructor_exists():
    assert callable(domains::ConcreteDomain.__init__)


def test_domains::concretedomain_constructor_args():
    sig = inspect.signature(domains::ConcreteDomain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::domaininitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::DomainInitialization)


def test_asmeta::structure::domaininitialization_constructor_exists():
    assert callable(asmeta::structure::DomainInitialization.__init__)


def test_asmeta::structure::domaininitialization_constructor_args():
    sig = inspect.signature(asmeta::structure::DomainInitialization.__init__)
    params = list(sig.parameters.keys())



def test_dynamicfunction_is_not_abstract():
    assert not inspect.isabstract(DynamicFunction)


def test_dynamicfunction_constructor_exists():
    assert callable(DynamicFunction.__init__)


def test_dynamicfunction_constructor_args():
    sig = inspect.signature(DynamicFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::localfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::LocalFunction)


def test_asmeta::definitions::localfunction_constructor_exists():
    assert callable(asmeta::definitions::LocalFunction.__init__)


def test_asmeta::definitions::localfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::LocalFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::outfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::OutFunction)


def test_asmeta::definitions::outfunction_constructor_exists():
    assert callable(asmeta::definitions::OutFunction.__init__)


def test_asmeta::definitions::outfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::OutFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::sharedfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::SharedFunction)


def test_asmeta::definitions::sharedfunction_constructor_exists():
    assert callable(asmeta::definitions::SharedFunction.__init__)


def test_asmeta::definitions::sharedfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::SharedFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::controlledfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::ControlledFunction)


def test_asmeta::definitions::controlledfunction_constructor_exists():
    assert callable(asmeta::definitions::ControlledFunction.__init__)


def test_asmeta::definitions::controlledfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::ControlledFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::monitoredfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::MonitoredFunction)


def test_asmeta::definitions::monitoredfunction_constructor_exists():
    assert callable(asmeta::definitions::MonitoredFunction.__init__)


def test_asmeta::definitions::monitoredfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::MonitoredFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::functioninitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::FunctionInitialization)


def test_asmeta::structure::functioninitialization_constructor_exists():
    assert callable(asmeta::structure::FunctionInitialization.__init__)


def test_asmeta::structure::functioninitialization_constructor_args():
    sig = inspect.signature(asmeta::structure::FunctionInitialization.__init__)
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



def test_asmeta::definitions::invariant_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::Invariant)


def test_asmeta::definitions::invariant_constructor_exists():
    assert callable(asmeta::definitions::Invariant.__init__)


def test_asmeta::definitions::invariant_constructor_args():
    sig = inspect.signature(asmeta::definitions::Invariant.__init__)
    params = list(sig.parameters.keys())



def test_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(FunctionDefinition)


def test_functiondefinition_constructor_exists():
    assert callable(FunctionDefinition.__init__)


def test_functiondefinition_constructor_args():
    sig = inspect.signature(FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::body_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::Body)


def test_asmeta::structure::body_constructor_exists():
    assert callable(asmeta::structure::Body.__init__)


def test_asmeta::structure::body_constructor_args():
    sig = inspect.signature(asmeta::structure::Body.__init__)
    params = list(sig.parameters.keys())



def test_initialization_is_not_abstract():
    assert not inspect.isabstract(Initialization)


def test_initialization_constructor_exists():
    assert callable(Initialization.__init__)


def test_initialization_constructor_args():
    sig = inspect.signature(Initialization.__init__)
    params = list(sig.parameters.keys())



def test_basictransitionrules::macrocallrule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules::MacroCallRule)


def test_basictransitionrules::macrocallrule_constructor_exists():
    assert callable(basictransitionrules::MacroCallRule.__init__)


def test_basictransitionrules::macrocallrule_constructor_args():
    sig = inspect.signature(basictransitionrules::MacroCallRule.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::agentinitialization_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::AgentInitialization)


def test_asmeta::structure::agentinitialization_constructor_exists():
    assert callable(asmeta::structure::AgentInitialization.__init__)


def test_asmeta::structure::agentinitialization_constructor_args():
    sig = inspect.signature(asmeta::structure::AgentInitialization.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::structure::namedelement_is_not_abstract():
    assert not inspect.isabstract(asmeta::structure::NamedElement)


def test_asmeta::structure::namedelement_constructor_exists():
    assert callable(asmeta::structure::NamedElement.__init__)


def test_asmeta::structure::namedelement_constructor_args():
    sig = inspect.signature(asmeta::structure::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_asmeta::structure::namedelement_has_name():
    assert hasattr(asmeta::structure::NamedElement, "name")
    descriptor = None
    for klass in asmeta::structure::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_basictransitionrules::termasrule_is_not_abstract():
    assert not inspect.isabstract(basictransitionrules::TermAsRule)


def test_basictransitionrules::termasrule_constructor_exists():
    assert callable(basictransitionrules::TermAsRule.__init__)


def test_basictransitionrules::termasrule_constructor_args():
    sig = inspect.signature(basictransitionrules::TermAsRule.__init__)
    params = list(sig.parameters.keys())



def test_domains::domain_is_not_abstract():
    assert not inspect.isabstract(domains::Domain)


def test_domains::domain_constructor_exists():
    assert callable(domains::Domain.__init__)


def test_domains::domain_constructor_args():
    sig = inspect.signature(domains::Domain.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::term_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::Term)


def test_asmeta::basicterms::term_constructor_exists():
    assert callable(asmeta::basicterms::Term.__init__)


def test_asmeta::basicterms::term_constructor_args():
    sig = inspect.signature(asmeta::basicterms::Term.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::basicterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::BasicTerm)


def test_asmeta::basicterms::basicterm_constructor_exists():
    assert callable(asmeta::basicterms::BasicTerm.__init__)


def test_asmeta::basicterms::basicterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::BasicTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::extendedterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::ExtendedTerm)


def test_asmeta::basicterms::extendedterm_constructor_exists():
    assert callable(asmeta::basicterms::ExtendedTerm.__init__)


def test_asmeta::basicterms::extendedterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::ExtendedTerm.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::derivedfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::DerivedFunction)


def test_asmeta::definitions::derivedfunction_constructor_exists():
    assert callable(asmeta::definitions::DerivedFunction.__init__)


def test_asmeta::definitions::derivedfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::DerivedFunction.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::definitions::basicfunction_is_not_abstract():
    assert not inspect.isabstract(asmeta::definitions::BasicFunction)


def test_asmeta::definitions::basicfunction_constructor_exists():
    assert callable(asmeta::definitions::BasicFunction.__init__)


def test_asmeta::definitions::basicfunction_constructor_args():
    sig = inspect.signature(asmeta::definitions::BasicFunction.__init__)
    params = list(sig.parameters.keys())



def test_functionterm_is_not_abstract():
    assert not inspect.isabstract(FunctionTerm)


def test_functionterm_constructor_exists():
    assert callable(FunctionTerm.__init__)


def test_functionterm_constructor_args():
    sig = inspect.signature(FunctionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::locationterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::LocationTerm)


def test_asmeta::basicterms::locationterm_constructor_exists():
    assert callable(asmeta::basicterms::LocationTerm.__init__)


def test_asmeta::basicterms::locationterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::LocationTerm.__init__)
    params = list(sig.parameters.keys())



def test_ruledeclaration_is_not_abstract():
    assert not inspect.isabstract(RuleDeclaration)


def test_ruledeclaration_constructor_exists():
    assert callable(RuleDeclaration.__init__)


def test_ruledeclaration_constructor_args():
    sig = inspect.signature(RuleDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::turbotransitionrules::turbodeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta::turbotransitionrules::TurboDeclaration)


def test_asmeta::turbotransitionrules::turbodeclaration_constructor_exists():
    assert callable(asmeta::turbotransitionrules::TurboDeclaration.__init__)


def test_asmeta::turbotransitionrules::turbodeclaration_constructor_args():
    sig = inspect.signature(asmeta::turbotransitionrules::TurboDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basictransitionrules::macrodeclaration_is_not_abstract():
    assert not inspect.isabstract(asmeta::basictransitionrules::MacroDeclaration)


def test_asmeta::basictransitionrules::macrodeclaration_constructor_exists():
    assert callable(asmeta::basictransitionrules::MacroDeclaration.__init__)


def test_asmeta::basictransitionrules::macrodeclaration_constructor_args():
    sig = inspect.signature(asmeta::basictransitionrules::MacroDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_furtherterms::finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(furtherterms::FiniteQuantificationTerm)


def test_furtherterms::finitequantificationterm_constructor_exists():
    assert callable(furtherterms::FiniteQuantificationTerm.__init__)


def test_furtherterms::finitequantificationterm_constructor_args():
    sig = inspect.signature(furtherterms::FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())



def test_basicterm_is_not_abstract():
    assert not inspect.isabstract(BasicTerm)


def test_basicterm_constructor_exists():
    assert callable(BasicTerm.__init__)


def test_basicterm_constructor_args():
    sig = inspect.signature(BasicTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::functionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::FunctionTerm)


def test_asmeta::basicterms::functionterm_constructor_exists():
    assert callable(asmeta::basicterms::FunctionTerm.__init__)


def test_asmeta::basicterms::functionterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::FunctionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::constantterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::ConstantTerm)


def test_asmeta::basicterms::constantterm_constructor_exists():
    assert callable(asmeta::basicterms::ConstantTerm.__init__)


def test_asmeta::basicterms::constantterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::ConstantTerm.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_asmeta::basicterms::constantterm_has_symbol():
    assert hasattr(asmeta::basicterms::ConstantTerm, "symbol")
    descriptor = None
    for klass in asmeta::basicterms::ConstantTerm.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basicterms::variableterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::VariableTerm)


def test_asmeta::basicterms::variableterm_constructor_exists():
    assert callable(asmeta::basicterms::VariableTerm.__init__)


def test_asmeta::basicterms::variableterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::VariableTerm.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "name" in params, "Missing parameter 'name'"

def test_asmeta::basicterms::variableterm_has_kind():
    assert hasattr(asmeta::basicterms::VariableTerm, "kind")
    descriptor = None
    for klass in asmeta::basicterms::VariableTerm.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_asmeta::basicterms::variableterm_has_name():
    assert hasattr(asmeta::basicterms::VariableTerm, "name")
    descriptor = None
    for klass in asmeta::basicterms::VariableTerm.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(FiniteQuantificationTerm)


def test_finitequantificationterm_constructor_exists():
    assert callable(FiniteQuantificationTerm.__init__)


def test_finitequantificationterm_constructor_args():
    sig = inspect.signature(FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::existterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ExistTerm)


def test_asmeta::furtherterms::existterm_constructor_exists():
    assert callable(asmeta::furtherterms::ExistTerm.__init__)


def test_asmeta::furtherterms::existterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ExistTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::existuniqueterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ExistUniqueTerm)


def test_asmeta::furtherterms::existuniqueterm_constructor_exists():
    assert callable(asmeta::furtherterms::ExistUniqueTerm.__init__)


def test_asmeta::furtherterms::existuniqueterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ExistUniqueTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::forallterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ForallTerm)


def test_asmeta::furtherterms::forallterm_constructor_exists():
    assert callable(asmeta::furtherterms::ForallTerm.__init__)


def test_asmeta::furtherterms::forallterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ForallTerm.__init__)
    params = list(sig.parameters.keys())



def test_basicterms::term_is_not_abstract():
    assert not inspect.isabstract(basicterms::Term)


def test_basicterms::term_constructor_exists():
    assert callable(basicterms::Term.__init__)


def test_basicterms::term_constructor_args():
    sig = inspect.signature(basicterms::Term.__init__)
    params = list(sig.parameters.keys())



def test_basicterms::variableterm_is_not_abstract():
    assert not inspect.isabstract(basicterms::VariableTerm)


def test_basicterms::variableterm_constructor_exists():
    assert callable(basicterms::VariableTerm.__init__)


def test_basicterms::variableterm_constructor_args():
    sig = inspect.signature(basicterms::VariableTerm.__init__)
    params = list(sig.parameters.keys())



def test_variablebindingterm_is_not_abstract():
    assert not inspect.isabstract(VariableBindingTerm)


def test_variablebindingterm_constructor_exists():
    assert callable(VariableBindingTerm.__init__)


def test_variablebindingterm_constructor_args():
    sig = inspect.signature(VariableBindingTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::finitequantificationterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::FiniteQuantificationTerm)


def test_asmeta::furtherterms::finitequantificationterm_constructor_exists():
    assert callable(asmeta::furtherterms::FiniteQuantificationTerm.__init__)


def test_asmeta::furtherterms::finitequantificationterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::FiniteQuantificationTerm.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta::furtherterms::finitequantificationterm_has_ranges():
    assert hasattr(asmeta::furtherterms::FiniteQuantificationTerm, "ranges")
    descriptor = None
    for klass in asmeta::furtherterms::FiniteQuantificationTerm.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::furtherterms::comprehensionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ComprehensionTerm)


def test_asmeta::furtherterms::comprehensionterm_constructor_exists():
    assert callable(asmeta::furtherterms::ComprehensionTerm.__init__)


def test_asmeta::furtherterms::comprehensionterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ComprehensionTerm.__init__)
    params = list(sig.parameters.keys())
    assert "ranges" in params, "Missing parameter 'ranges'"

def test_asmeta::furtherterms::comprehensionterm_has_ranges():
    assert hasattr(asmeta::furtherterms::ComprehensionTerm, "ranges")
    descriptor = None
    for klass in asmeta::furtherterms::ComprehensionTerm.__mro__:
        if "ranges" in klass.__dict__:
            descriptor = klass.__dict__["ranges"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::furtherterms::letterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::LetTerm)


def test_asmeta::furtherterms::letterm_constructor_exists():
    assert callable(asmeta::furtherterms::LetTerm.__init__)


def test_asmeta::furtherterms::letterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::LetTerm.__init__)
    params = list(sig.parameters.keys())



def test_basicterms::tupleterm_is_not_abstract():
    assert not inspect.isabstract(basicterms::TupleTerm)


def test_basicterms::tupleterm_constructor_exists():
    assert callable(basicterms::TupleTerm.__init__)


def test_basicterms::tupleterm_constructor_args():
    sig = inspect.signature(basicterms::TupleTerm.__init__)
    params = list(sig.parameters.keys())



def test_collectionterm_is_not_abstract():
    assert not inspect.isabstract(CollectionTerm)


def test_collectionterm_constructor_exists():
    assert callable(CollectionTerm.__init__)


def test_collectionterm_constructor_args():
    sig = inspect.signature(CollectionTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::mapterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::MapTerm)


def test_asmeta::furtherterms::mapterm_constructor_exists():
    assert callable(asmeta::furtherterms::MapTerm.__init__)


def test_asmeta::furtherterms::mapterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::MapTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::setterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::SetTerm)


def test_asmeta::basicterms::setterm_constructor_exists():
    assert callable(asmeta::basicterms::SetTerm.__init__)


def test_asmeta::basicterms::setterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::bagterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::BagTerm)


def test_asmeta::furtherterms::bagterm_constructor_exists():
    assert callable(asmeta::furtherterms::BagTerm.__init__)


def test_asmeta::furtherterms::bagterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::BagTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::sequenceterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::SequenceTerm)


def test_asmeta::furtherterms::sequenceterm_constructor_exists():
    assert callable(asmeta::furtherterms::SequenceTerm.__init__)


def test_asmeta::furtherterms::sequenceterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::SequenceTerm.__init__)
    params = list(sig.parameters.keys())
    assert "terms" in params, "Missing parameter 'terms'"

def test_asmeta::furtherterms::sequenceterm_has_terms():
    assert hasattr(asmeta::furtherterms::SequenceTerm, "terms")
    descriptor = None
    for klass in asmeta::furtherterms::SequenceTerm.__mro__:
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



def test_asmeta::furtherterms::sequencect_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::SequenceCt)


def test_asmeta::furtherterms::sequencect_constructor_exists():
    assert callable(asmeta::furtherterms::SequenceCt.__init__)


def test_asmeta::furtherterms::sequencect_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::SequenceCt.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::bagct_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::BagCt)


def test_asmeta::furtherterms::bagct_constructor_exists():
    assert callable(asmeta::furtherterms::BagCt.__init__)


def test_asmeta::furtherterms::bagct_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::BagCt.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::mapct_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::MapCt)


def test_asmeta::furtherterms::mapct_constructor_exists():
    assert callable(asmeta::furtherterms::MapCt.__init__)


def test_asmeta::furtherterms::mapct_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::MapCt.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::setct_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::SetCt)


def test_asmeta::furtherterms::setct_constructor_exists():
    assert callable(asmeta::furtherterms::SetCt.__init__)


def test_asmeta::furtherterms::setct_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::SetCt.__init__)
    params = list(sig.parameters.keys())



def test_extendedterm_is_not_abstract():
    assert not inspect.isabstract(ExtendedTerm)


def test_extendedterm_constructor_exists():
    assert callable(ExtendedTerm.__init__)


def test_extendedterm_constructor_args():
    sig = inspect.signature(ExtendedTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::conditionalterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ConditionalTerm)


def test_asmeta::furtherterms::conditionalterm_constructor_exists():
    assert callable(asmeta::furtherterms::ConditionalTerm.__init__)


def test_asmeta::furtherterms::conditionalterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ConditionalTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::ruleasterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::RuleAsTerm)


def test_asmeta::basicterms::ruleasterm_constructor_exists():
    assert callable(asmeta::basicterms::RuleAsTerm.__init__)


def test_asmeta::basicterms::ruleasterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::RuleAsTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::collectionterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::CollectionTerm)


def test_asmeta::basicterms::collectionterm_constructor_exists():
    assert callable(asmeta::basicterms::CollectionTerm.__init__)


def test_asmeta::basicterms::collectionterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::CollectionTerm.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_asmeta::basicterms::collectionterm_has_size():
    assert hasattr(asmeta::basicterms::CollectionTerm, "size")
    descriptor = None
    for klass in asmeta::basicterms::CollectionTerm.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basicterms::tupleterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::TupleTerm)


def test_asmeta::basicterms::tupleterm_constructor_exists():
    assert callable(asmeta::basicterms::TupleTerm.__init__)


def test_asmeta::basicterms::tupleterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::TupleTerm.__init__)
    params = list(sig.parameters.keys())
    assert "arity" in params, "Missing parameter 'arity'"
    assert "terms" in params, "Missing parameter 'terms'"

def test_asmeta::basicterms::tupleterm_has_arity():
    assert hasattr(asmeta::basicterms::TupleTerm, "arity")
    descriptor = None
    for klass in asmeta::basicterms::TupleTerm.__mro__:
        if "arity" in klass.__dict__:
            descriptor = klass.__dict__["arity"]
            break
    assert isinstance(descriptor, property)

def test_asmeta::basicterms::tupleterm_has_terms():
    assert hasattr(asmeta::basicterms::TupleTerm, "terms")
    descriptor = None
    for klass in asmeta::basicterms::TupleTerm.__mro__:
        if "terms" in klass.__dict__:
            descriptor = klass.__dict__["terms"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::furtherterms::caseterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::CaseTerm)


def test_asmeta::furtherterms::caseterm_constructor_exists():
    assert callable(asmeta::furtherterms::CaseTerm.__init__)


def test_asmeta::furtherterms::caseterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::CaseTerm.__init__)
    params = list(sig.parameters.keys())
    assert "resultTerms" in params, "Missing parameter 'resultTerms'"

def test_asmeta::furtherterms::caseterm_has_resultTerms():
    assert hasattr(asmeta::furtherterms::CaseTerm, "resultTerms")
    descriptor = None
    for klass in asmeta::furtherterms::CaseTerm.__mro__:
        if "resultTerms" in klass.__dict__:
            descriptor = klass.__dict__["resultTerms"]
            break
    assert isinstance(descriptor, property)



def test_asmeta::basicterms::domainterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::DomainTerm)


def test_asmeta::basicterms::domainterm_constructor_exists():
    assert callable(asmeta::basicterms::DomainTerm.__init__)


def test_asmeta::basicterms::domainterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::DomainTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::variablebindingterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::VariableBindingTerm)


def test_asmeta::furtherterms::variablebindingterm_constructor_exists():
    assert callable(asmeta::furtherterms::VariableBindingTerm.__init__)


def test_asmeta::furtherterms::variablebindingterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::VariableBindingTerm.__init__)
    params = list(sig.parameters.keys())



def test_constantterm_is_not_abstract():
    assert not inspect.isabstract(ConstantTerm)


def test_constantterm_constructor_exists():
    assert callable(ConstantTerm.__init__)


def test_constantterm_constructor_args():
    sig = inspect.signature(ConstantTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::realterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::RealTerm)


def test_asmeta::furtherterms::realterm_constructor_exists():
    assert callable(asmeta::furtherterms::RealTerm.__init__)


def test_asmeta::furtherterms::realterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::RealTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::enumterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::EnumTerm)


def test_asmeta::furtherterms::enumterm_constructor_exists():
    assert callable(asmeta::furtherterms::EnumTerm.__init__)


def test_asmeta::furtherterms::enumterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::EnumTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::undefterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::UndefTerm)


def test_asmeta::basicterms::undefterm_constructor_exists():
    assert callable(asmeta::basicterms::UndefTerm.__init__)


def test_asmeta::basicterms::undefterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::UndefTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::stringterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::StringTerm)


def test_asmeta::furtherterms::stringterm_constructor_exists():
    assert callable(asmeta::furtherterms::StringTerm.__init__)


def test_asmeta::furtherterms::stringterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::StringTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::naturalterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::NaturalTerm)


def test_asmeta::furtherterms::naturalterm_constructor_exists():
    assert callable(asmeta::furtherterms::NaturalTerm.__init__)


def test_asmeta::furtherterms::naturalterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::NaturalTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::charterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::CharTerm)


def test_asmeta::furtherterms::charterm_constructor_exists():
    assert callable(asmeta::furtherterms::CharTerm.__init__)


def test_asmeta::furtherterms::charterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::CharTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::complexterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::ComplexTerm)


def test_asmeta::furtherterms::complexterm_constructor_exists():
    assert callable(asmeta::furtherterms::ComplexTerm.__init__)


def test_asmeta::furtherterms::complexterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::ComplexTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::basicterms::booleanterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::basicterms::BooleanTerm)


def test_asmeta::basicterms::booleanterm_constructor_exists():
    assert callable(asmeta::basicterms::BooleanTerm.__init__)


def test_asmeta::basicterms::booleanterm_constructor_args():
    sig = inspect.signature(asmeta::basicterms::BooleanTerm.__init__)
    params = list(sig.parameters.keys())



def test_asmeta::furtherterms::integerterm_is_not_abstract():
    assert not inspect.isabstract(asmeta::furtherterms::IntegerTerm)


def test_asmeta::furtherterms::integerterm_constructor_exists():
    assert callable(asmeta::furtherterms::IntegerTerm.__init__)


def test_asmeta::furtherterms::integerterm_constructor_args():
    sig = inspect.signature(asmeta::furtherterms::IntegerTerm.__init__)
    params = list(sig.parameters.keys())

def test_variablekind_exists():
    # Check that the Enumeration exists
    assert VariableKind is not None

def test_variablekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableKind]
    expected_literals = [
        "logicalVar",
        "ruleVar",
        "locationVar",
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
domains::TypeDomain_strategy = st.builds(
    domains::TypeDomain,
)
asmeta::domains::EnumElement_strategy = st.builds(
    asmeta::domains::EnumElement,
    symbol=
        safe_text
)
domains::EnumElement_strategy = st.builds(
    domains::EnumElement,
)
RealDomain_strategy = st.builds(
    RealDomain,
)
asmeta::domains::IntegerDomain_strategy = st.builds(
    asmeta::domains::IntegerDomain,
)
ComplexDomain_strategy = st.builds(
    ComplexDomain,
)
asmeta::domains::RealDomain_strategy = st.builds(
    asmeta::domains::RealDomain,
)
AbstractTd_strategy = st.builds(
    AbstractTd,
)
asmeta::domains::AgentDomain_strategy = st.builds(
    asmeta::domains::AgentDomain,
)
asmeta::domains::ReserveDomain_strategy = st.builds(
    asmeta::domains::ReserveDomain,
)
StructuredTd_strategy = st.builds(
    StructuredTd,
)
asmeta::domains::ProductDomain_strategy = st.builds(
    asmeta::domains::ProductDomain,
    domains=
        safe_text
)
asmeta::domains::RuleDomain_strategy = st.builds(
    asmeta::domains::RuleDomain,
    domains=
        safe_text
)
asmeta::domains::MapDomain_strategy = st.builds(
    asmeta::domains::MapDomain,
)
asmeta::domains::BagDomain_strategy = st.builds(
    asmeta::domains::BagDomain,
)
asmeta::domains::PowersetDomain_strategy = st.builds(
    asmeta::domains::PowersetDomain,
)
asmeta::domains::SequenceDomain_strategy = st.builds(
    asmeta::domains::SequenceDomain,
)
TypeDomain_strategy = st.builds(
    TypeDomain,
)
asmeta::domains::BasicTd_strategy = st.builds(
    asmeta::domains::BasicTd,
)
asmeta::domains::AnyDomain_strategy = st.builds(
    asmeta::domains::AnyDomain,
)
asmeta::domains::EnumTd_strategy = st.builds(
    asmeta::domains::EnumTd,
)
asmeta::domains::AbstractTd_strategy = st.builds(
    asmeta::domains::AbstractTd,
    isDynamic=
        safe_text
)
asmeta::domains::StructuredTd_strategy = st.builds(
    asmeta::domains::StructuredTd,
)
Domain_strategy = st.builds(
    Domain,
)
asmeta::domains::ConcreteDomain_strategy = st.builds(
    asmeta::domains::ConcreteDomain,
    isDynamic=
        safe_text
)
asmeta::domains::TypeDomain_strategy = st.builds(
    asmeta::domains::TypeDomain,
)
BasicTd_strategy = st.builds(
    BasicTd,
)
asmeta::domains::StringDomain_strategy = st.builds(
    asmeta::domains::StringDomain,
)
asmeta::domains::CharDomain_strategy = st.builds(
    asmeta::domains::CharDomain,
)
asmeta::domains::ComplexDomain_strategy = st.builds(
    asmeta::domains::ComplexDomain,
)
asmeta::domains::BooleanDomain_strategy = st.builds(
    asmeta::domains::BooleanDomain,
)
asmeta::domains::UndefDomain_strategy = st.builds(
    asmeta::domains::UndefDomain,
)
IntegerDomain_strategy = st.builds(
    IntegerDomain,
)
asmeta::domains::NaturalDomain_strategy = st.builds(
    asmeta::domains::NaturalDomain,
)
BasicFunction_strategy = st.builds(
    BasicFunction,
)
asmeta::definitions::StaticFunction_strategy = st.builds(
    asmeta::definitions::StaticFunction,
)
asmeta::definitions::DynamicFunction_strategy = st.builds(
    asmeta::definitions::DynamicFunction,
)
Invariant_strategy = st.builds(
    Invariant,
)
Classifier_strategy = st.builds(
    Classifier,
)
asmeta::definitions::Function_strategy = st.builds(
    asmeta::definitions::Function,
    arity=
        safe_text
)
asmeta::domains::Domain_strategy = st.builds(
    asmeta::domains::Domain,
)
asmeta::definitions::Property_strategy = st.builds(
    asmeta::definitions::Property,
)
asmeta::definitions::RuleDeclaration_strategy = st.builds(
    asmeta::definitions::RuleDeclaration,
    arity=
        safe_text
)
BasicRule_strategy = st.builds(
    BasicRule,
)
asmeta::basictransitionrules::LetRule_strategy = st.builds(
    asmeta::basictransitionrules::LetRule,
)
asmeta::basictransitionrules::ForallRule_strategy = st.builds(
    asmeta::basictransitionrules::ForallRule,
    ranges=
        safe_text
)
asmeta::basictransitionrules::UpdateRule_strategy = st.builds(
    asmeta::basictransitionrules::UpdateRule,
)
asmeta::basictransitionrules::BlockRule_strategy = st.builds(
    asmeta::basictransitionrules::BlockRule,
    rules=
        safe_text
)
asmeta::basictransitionrules::ConditionalRule_strategy = st.builds(
    asmeta::basictransitionrules::ConditionalRule,
)
asmeta::basictransitionrules::MacroCallRule_strategy = st.builds(
    asmeta::basictransitionrules::MacroCallRule,
    parameters=
        safe_text
)
asmeta::basictransitionrules::ExtendRule_strategy = st.builds(
    asmeta::basictransitionrules::ExtendRule,
)
asmeta::basictransitionrules::SkipRule_strategy = st.builds(
    asmeta::basictransitionrules::SkipRule,
)
asmeta::basictransitionrules::ChooseRule_strategy = st.builds(
    asmeta::basictransitionrules::ChooseRule,
    ranges=
        safe_text
)
asmeta::basictransitionrules::Rule_strategy = st.builds(
    asmeta::basictransitionrules::Rule,
)
DerivedRule_strategy = st.builds(
    DerivedRule,
)
asmeta::derivedtransitionrules::TurboDerivedRule_strategy = st.builds(
    asmeta::derivedtransitionrules::TurboDerivedRule,
)
asmeta::derivedtransitionrules::BasicDerivedRule_strategy = st.builds(
    asmeta::derivedtransitionrules::BasicDerivedRule,
)
BasicDerivedRule_strategy = st.builds(
    BasicDerivedRule,
)
asmeta::derivedtransitionrules::CaseRule_strategy = st.builds(
    asmeta::derivedtransitionrules::CaseRule,
    caseBranches=
        safe_text
)
TurboDerivedRule_strategy = st.builds(
    TurboDerivedRule,
)
asmeta::derivedtransitionrules::IterativeWhileRule_strategy = st.builds(
    asmeta::derivedtransitionrules::IterativeWhileRule,
)
asmeta::derivedtransitionrules::RecursiveWhileRule_strategy = st.builds(
    asmeta::derivedtransitionrules::RecursiveWhileRule,
)
turbotransitionrules::TurboCallRule_strategy = st.builds(
    turbotransitionrules::TurboCallRule,
)
turbotransitionrules::TurboDeclaration_strategy = st.builds(
    turbotransitionrules::TurboDeclaration,
)
LocalFunction_strategy = st.builds(
    LocalFunction,
)
basictransitionrules::Rule_strategy = st.builds(
    basictransitionrules::Rule,
)
TurboRule_strategy = st.builds(
    TurboRule,
)
asmeta::turbotransitionrules::TurboCallRule_strategy = st.builds(
    asmeta::turbotransitionrules::TurboCallRule,
    parameters=
        safe_text
)
asmeta::turbotransitionrules::IterateRule_strategy = st.builds(
    asmeta::turbotransitionrules::IterateRule,
)
asmeta::turbotransitionrules::TurboReturnRule_strategy = st.builds(
    asmeta::turbotransitionrules::TurboReturnRule,
)
asmeta::turbotransitionrules::TryCatchRule_strategy = st.builds(
    asmeta::turbotransitionrules::TryCatchRule,
)
asmeta::turbotransitionrules::TurboLocalStateRule_strategy = st.builds(
    asmeta::turbotransitionrules::TurboLocalStateRule,
)
asmeta::turbotransitionrules::SeqRule_strategy = st.builds(
    asmeta::turbotransitionrules::SeqRule,
    rules=
        safe_text
)
Rule_strategy = st.builds(
    Rule,
)
asmeta::derivedtransitionrules::DerivedRule_strategy = st.builds(
    asmeta::derivedtransitionrules::DerivedRule,
)
asmeta::basictransitionrules::BasicRule_strategy = st.builds(
    asmeta::basictransitionrules::BasicRule,
)
asmeta::basictransitionrules::TermAsRule_strategy = st.builds(
    asmeta::basictransitionrules::TermAsRule,
    parameters=
        safe_text
)
asmeta::turbotransitionrules::TurboRule_strategy = st.builds(
    asmeta::turbotransitionrules::TurboRule,
)
basictransitionrules::MacroDeclaration_strategy = st.builds(
    basictransitionrules::MacroDeclaration,
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
asmeta::structure::Header_strategy = st.builds(
    asmeta::structure::Header,
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
asmeta::structure::Asm_strategy = st.builds(
    asmeta::structure::Asm,
    isAsynchr=
        safe_text
)
asmeta::definitions::Classifier_strategy = st.builds(
    asmeta::definitions::Classifier,
)
asmeta::structure::Initialization_strategy = st.builds(
    asmeta::structure::Initialization,
)
asmeta::structure::DomainDefinition_strategy = st.builds(
    asmeta::structure::DomainDefinition,
)
asmeta::structure::FunctionDefinition_strategy = st.builds(
    asmeta::structure::FunctionDefinition,
)
asmeta::structure::ImportClause_strategy = st.builds(
    asmeta::structure::ImportClause,
    moduleName=
        safe_text
)
asmeta::structure::ExportClause_strategy = st.builds(
    asmeta::structure::ExportClause,
)
domains::StructuredTd_strategy = st.builds(
    domains::StructuredTd,
)
Header_strategy = st.builds(
    Header,
)
asmeta::structure::Signature_strategy = st.builds(
    asmeta::structure::Signature,
)
domains::ConcreteDomain_strategy = st.builds(
    domains::ConcreteDomain,
)
asmeta::structure::DomainInitialization_strategy = st.builds(
    asmeta::structure::DomainInitialization,
)
DynamicFunction_strategy = st.builds(
    DynamicFunction,
)
asmeta::definitions::LocalFunction_strategy = st.builds(
    asmeta::definitions::LocalFunction,
)
asmeta::definitions::OutFunction_strategy = st.builds(
    asmeta::definitions::OutFunction,
)
asmeta::definitions::SharedFunction_strategy = st.builds(
    asmeta::definitions::SharedFunction,
)
asmeta::definitions::ControlledFunction_strategy = st.builds(
    asmeta::definitions::ControlledFunction,
)
asmeta::definitions::MonitoredFunction_strategy = st.builds(
    asmeta::definitions::MonitoredFunction,
)
asmeta::structure::FunctionInitialization_strategy = st.builds(
    asmeta::structure::FunctionInitialization,
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
asmeta::definitions::Invariant_strategy = st.builds(
    asmeta::definitions::Invariant,
)
FunctionDefinition_strategy = st.builds(
    FunctionDefinition,
)
asmeta::structure::Body_strategy = st.builds(
    asmeta::structure::Body,
)
Initialization_strategy = st.builds(
    Initialization,
)
basictransitionrules::MacroCallRule_strategy = st.builds(
    basictransitionrules::MacroCallRule,
)
asmeta::structure::AgentInitialization_strategy = st.builds(
    asmeta::structure::AgentInitialization,
)
asmeta::structure::NamedElement_strategy = st.builds(
    asmeta::structure::NamedElement,
    name=
        safe_text
)
basictransitionrules::TermAsRule_strategy = st.builds(
    basictransitionrules::TermAsRule,
)
domains::Domain_strategy = st.builds(
    domains::Domain,
)
asmeta::basicterms::Term_strategy = st.builds(
    asmeta::basicterms::Term,
)
Term_strategy = st.builds(
    Term,
)
asmeta::basicterms::BasicTerm_strategy = st.builds(
    asmeta::basicterms::BasicTerm,
)
asmeta::basicterms::ExtendedTerm_strategy = st.builds(
    asmeta::basicterms::ExtendedTerm,
)
Function_strategy = st.builds(
    Function,
)
asmeta::definitions::DerivedFunction_strategy = st.builds(
    asmeta::definitions::DerivedFunction,
)
asmeta::definitions::BasicFunction_strategy = st.builds(
    asmeta::definitions::BasicFunction,
)
FunctionTerm_strategy = st.builds(
    FunctionTerm,
)
asmeta::basicterms::LocationTerm_strategy = st.builds(
    asmeta::basicterms::LocationTerm,
)
RuleDeclaration_strategy = st.builds(
    RuleDeclaration,
)
asmeta::turbotransitionrules::TurboDeclaration_strategy = st.builds(
    asmeta::turbotransitionrules::TurboDeclaration,
)
asmeta::basictransitionrules::MacroDeclaration_strategy = st.builds(
    asmeta::basictransitionrules::MacroDeclaration,
)
furtherterms::FiniteQuantificationTerm_strategy = st.builds(
    furtherterms::FiniteQuantificationTerm,
)
BasicTerm_strategy = st.builds(
    BasicTerm,
)
asmeta::basicterms::FunctionTerm_strategy = st.builds(
    asmeta::basicterms::FunctionTerm,
)
asmeta::basicterms::ConstantTerm_strategy = st.builds(
    asmeta::basicterms::ConstantTerm,
    symbol=
        safe_text
)
asmeta::basicterms::VariableTerm_strategy = st.builds(
    asmeta::basicterms::VariableTerm,
    kind=
        safe_text,
    name=
        safe_text
)
FiniteQuantificationTerm_strategy = st.builds(
    FiniteQuantificationTerm,
)
asmeta::furtherterms::ExistTerm_strategy = st.builds(
    asmeta::furtherterms::ExistTerm,
)
asmeta::furtherterms::ExistUniqueTerm_strategy = st.builds(
    asmeta::furtherterms::ExistUniqueTerm,
)
asmeta::furtherterms::ForallTerm_strategy = st.builds(
    asmeta::furtherterms::ForallTerm,
)
basicterms::Term_strategy = st.builds(
    basicterms::Term,
)
basicterms::VariableTerm_strategy = st.builds(
    basicterms::VariableTerm,
)
VariableBindingTerm_strategy = st.builds(
    VariableBindingTerm,
)
asmeta::furtherterms::FiniteQuantificationTerm_strategy = st.builds(
    asmeta::furtherterms::FiniteQuantificationTerm,
    ranges=
        safe_text
)
asmeta::furtherterms::ComprehensionTerm_strategy = st.builds(
    asmeta::furtherterms::ComprehensionTerm,
    ranges=
        safe_text
)
asmeta::furtherterms::LetTerm_strategy = st.builds(
    asmeta::furtherterms::LetTerm,
)
basicterms::TupleTerm_strategy = st.builds(
    basicterms::TupleTerm,
)
CollectionTerm_strategy = st.builds(
    CollectionTerm,
)
asmeta::furtherterms::MapTerm_strategy = st.builds(
    asmeta::furtherterms::MapTerm,
)
asmeta::basicterms::SetTerm_strategy = st.builds(
    asmeta::basicterms::SetTerm,
)
asmeta::furtherterms::BagTerm_strategy = st.builds(
    asmeta::furtherterms::BagTerm,
)
asmeta::furtherterms::SequenceTerm_strategy = st.builds(
    asmeta::furtherterms::SequenceTerm,
    terms=
        safe_text
)
ComprehensionTerm_strategy = st.builds(
    ComprehensionTerm,
)
asmeta::furtherterms::SequenceCt_strategy = st.builds(
    asmeta::furtherterms::SequenceCt,
)
asmeta::furtherterms::BagCt_strategy = st.builds(
    asmeta::furtherterms::BagCt,
)
asmeta::furtherterms::MapCt_strategy = st.builds(
    asmeta::furtherterms::MapCt,
)
asmeta::furtherterms::SetCt_strategy = st.builds(
    asmeta::furtherterms::SetCt,
)
ExtendedTerm_strategy = st.builds(
    ExtendedTerm,
)
asmeta::furtherterms::ConditionalTerm_strategy = st.builds(
    asmeta::furtherterms::ConditionalTerm,
)
asmeta::basicterms::RuleAsTerm_strategy = st.builds(
    asmeta::basicterms::RuleAsTerm,
)
asmeta::basicterms::CollectionTerm_strategy = st.builds(
    asmeta::basicterms::CollectionTerm,
    size=
        safe_text
)
asmeta::basicterms::TupleTerm_strategy = st.builds(
    asmeta::basicterms::TupleTerm,
    arity=
        safe_text,
    terms=
        safe_text
)
asmeta::furtherterms::CaseTerm_strategy = st.builds(
    asmeta::furtherterms::CaseTerm,
    resultTerms=
        safe_text
)
asmeta::basicterms::DomainTerm_strategy = st.builds(
    asmeta::basicterms::DomainTerm,
)
asmeta::furtherterms::VariableBindingTerm_strategy = st.builds(
    asmeta::furtherterms::VariableBindingTerm,
)
ConstantTerm_strategy = st.builds(
    ConstantTerm,
)
asmeta::furtherterms::RealTerm_strategy = st.builds(
    asmeta::furtherterms::RealTerm,
)
asmeta::furtherterms::EnumTerm_strategy = st.builds(
    asmeta::furtherterms::EnumTerm,
)
asmeta::basicterms::UndefTerm_strategy = st.builds(
    asmeta::basicterms::UndefTerm,
)
asmeta::furtherterms::StringTerm_strategy = st.builds(
    asmeta::furtherterms::StringTerm,
)
asmeta::furtherterms::NaturalTerm_strategy = st.builds(
    asmeta::furtherterms::NaturalTerm,
)
asmeta::furtherterms::CharTerm_strategy = st.builds(
    asmeta::furtherterms::CharTerm,
)
asmeta::furtherterms::ComplexTerm_strategy = st.builds(
    asmeta::furtherterms::ComplexTerm,
)
asmeta::basicterms::BooleanTerm_strategy = st.builds(
    asmeta::basicterms::BooleanTerm,
)
asmeta::furtherterms::IntegerTerm_strategy = st.builds(
    asmeta::furtherterms::IntegerTerm,
)

@given(instance=domains::TypeDomain_strategy)
@settings(max_examples=50)
def test_domains::typedomain_instantiation(instance):
    assert isinstance(instance, domains::TypeDomain)

@given(instance=asmeta::domains::EnumElement_strategy)
@settings(max_examples=50)
def test_asmeta::domains::enumelement_instantiation(instance):
    assert isinstance(instance, asmeta::domains::EnumElement)

@given(instance=asmeta::domains::EnumElement_strategy)
def test_asmeta::domains::enumelement_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=asmeta::domains::EnumElement_strategy)
def test_asmeta::domains::enumelement_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=domains::EnumElement_strategy)
@settings(max_examples=50)
def test_domains::enumelement_instantiation(instance):
    assert isinstance(instance, domains::EnumElement)

@given(instance=RealDomain_strategy)
@settings(max_examples=50)
def test_realdomain_instantiation(instance):
    assert isinstance(instance, RealDomain)

@given(instance=asmeta::domains::IntegerDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::integerdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::IntegerDomain)

@given(instance=ComplexDomain_strategy)
@settings(max_examples=50)
def test_complexdomain_instantiation(instance):
    assert isinstance(instance, ComplexDomain)

@given(instance=asmeta::domains::RealDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::realdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::RealDomain)

@given(instance=AbstractTd_strategy)
@settings(max_examples=50)
def test_abstracttd_instantiation(instance):
    assert isinstance(instance, AbstractTd)

@given(instance=asmeta::domains::AgentDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::agentdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::AgentDomain)

@given(instance=asmeta::domains::ReserveDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::reservedomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::ReserveDomain)

@given(instance=StructuredTd_strategy)
@settings(max_examples=50)
def test_structuredtd_instantiation(instance):
    assert isinstance(instance, StructuredTd)

@given(instance=asmeta::domains::ProductDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::productdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::ProductDomain)

@given(instance=asmeta::domains::ProductDomain_strategy)
def test_asmeta::domains::productdomain_domains_type(instance):
    assert isinstance(instance.domains, str)


@given(instance=asmeta::domains::ProductDomain_strategy)
def test_asmeta::domains::productdomain_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=asmeta::domains::RuleDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::ruledomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::RuleDomain)

@given(instance=asmeta::domains::RuleDomain_strategy)
def test_asmeta::domains::ruledomain_domains_type(instance):
    assert isinstance(instance.domains, str)


@given(instance=asmeta::domains::RuleDomain_strategy)
def test_asmeta::domains::ruledomain_domains_setter(instance):
    original = instance.domains
    instance.domains = original
    assert instance.domains == original

@given(instance=asmeta::domains::MapDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::mapdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::MapDomain)

@given(instance=asmeta::domains::BagDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::bagdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::BagDomain)

@given(instance=asmeta::domains::PowersetDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::powersetdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::PowersetDomain)

@given(instance=asmeta::domains::SequenceDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::sequencedomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::SequenceDomain)

@given(instance=TypeDomain_strategy)
@settings(max_examples=50)
def test_typedomain_instantiation(instance):
    assert isinstance(instance, TypeDomain)

@given(instance=asmeta::domains::BasicTd_strategy)
@settings(max_examples=50)
def test_asmeta::domains::basictd_instantiation(instance):
    assert isinstance(instance, asmeta::domains::BasicTd)

@given(instance=asmeta::domains::AnyDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::anydomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::AnyDomain)

@given(instance=asmeta::domains::EnumTd_strategy)
@settings(max_examples=50)
def test_asmeta::domains::enumtd_instantiation(instance):
    assert isinstance(instance, asmeta::domains::EnumTd)

@given(instance=asmeta::domains::AbstractTd_strategy)
@settings(max_examples=50)
def test_asmeta::domains::abstracttd_instantiation(instance):
    assert isinstance(instance, asmeta::domains::AbstractTd)

@given(instance=asmeta::domains::AbstractTd_strategy)
def test_asmeta::domains::abstracttd_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=asmeta::domains::AbstractTd_strategy)
def test_asmeta::domains::abstracttd_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=asmeta::domains::StructuredTd_strategy)
@settings(max_examples=50)
def test_asmeta::domains::structuredtd_instantiation(instance):
    assert isinstance(instance, asmeta::domains::StructuredTd)

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=asmeta::domains::ConcreteDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::concretedomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::ConcreteDomain)

@given(instance=asmeta::domains::ConcreteDomain_strategy)
def test_asmeta::domains::concretedomain_isDynamic_type(instance):
    assert isinstance(instance.isDynamic, str)


@given(instance=asmeta::domains::ConcreteDomain_strategy)
def test_asmeta::domains::concretedomain_isDynamic_setter(instance):
    original = instance.isDynamic
    instance.isDynamic = original
    assert instance.isDynamic == original

@given(instance=asmeta::domains::TypeDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::typedomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::TypeDomain)

@given(instance=BasicTd_strategy)
@settings(max_examples=50)
def test_basictd_instantiation(instance):
    assert isinstance(instance, BasicTd)

@given(instance=asmeta::domains::StringDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::stringdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::StringDomain)

@given(instance=asmeta::domains::CharDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::chardomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::CharDomain)

@given(instance=asmeta::domains::ComplexDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::complexdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::ComplexDomain)

@given(instance=asmeta::domains::BooleanDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::booleandomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::BooleanDomain)

@given(instance=asmeta::domains::UndefDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::undefdomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::UndefDomain)

@given(instance=IntegerDomain_strategy)
@settings(max_examples=50)
def test_integerdomain_instantiation(instance):
    assert isinstance(instance, IntegerDomain)

@given(instance=asmeta::domains::NaturalDomain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::naturaldomain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::NaturalDomain)

@given(instance=BasicFunction_strategy)
@settings(max_examples=50)
def test_basicfunction_instantiation(instance):
    assert isinstance(instance, BasicFunction)

@given(instance=asmeta::definitions::StaticFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::staticfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::StaticFunction)

@given(instance=asmeta::definitions::DynamicFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::dynamicfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::DynamicFunction)

@given(instance=Invariant_strategy)
@settings(max_examples=50)
def test_invariant_instantiation(instance):
    assert isinstance(instance, Invariant)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=asmeta::definitions::Function_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::function_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::Function)

@given(instance=asmeta::definitions::Function_strategy)
def test_asmeta::definitions::function_arity_type(instance):
    assert isinstance(instance.arity, str)


@given(instance=asmeta::definitions::Function_strategy)
def test_asmeta::definitions::function_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=asmeta::domains::Domain_strategy)
@settings(max_examples=50)
def test_asmeta::domains::domain_instantiation(instance):
    assert isinstance(instance, asmeta::domains::Domain)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=asmeta::domains::Domain_strategy)
@settings(max_examples=30)
def test_asmeta::domains::domain_compatible_changes_state(instance):
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
        assert has_statements, f"Function 'compatible' in asmeta::domains::Domain is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compatible' in asmeta::domains::Domain did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compatible' in asmeta::domains::Domain is not implemented or raised an error")

@given(instance=asmeta::definitions::Property_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::property_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::Property)

@given(instance=asmeta::definitions::RuleDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::ruledeclaration_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::RuleDeclaration)

@given(instance=asmeta::definitions::RuleDeclaration_strategy)
def test_asmeta::definitions::ruledeclaration_arity_type(instance):
    assert isinstance(instance.arity, str)


@given(instance=asmeta::definitions::RuleDeclaration_strategy)
def test_asmeta::definitions::ruledeclaration_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=BasicRule_strategy)
@settings(max_examples=50)
def test_basicrule_instantiation(instance):
    assert isinstance(instance, BasicRule)

@given(instance=asmeta::basictransitionrules::LetRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::letrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::LetRule)

@given(instance=asmeta::basictransitionrules::ForallRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::forallrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::ForallRule)

@given(instance=asmeta::basictransitionrules::ForallRule_strategy)
def test_asmeta::basictransitionrules::forallrule_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=asmeta::basictransitionrules::ForallRule_strategy)
def test_asmeta::basictransitionrules::forallrule_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta::basictransitionrules::UpdateRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::updaterule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::UpdateRule)

@given(instance=asmeta::basictransitionrules::BlockRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::blockrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::BlockRule)

@given(instance=asmeta::basictransitionrules::BlockRule_strategy)
def test_asmeta::basictransitionrules::blockrule_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=asmeta::basictransitionrules::BlockRule_strategy)
def test_asmeta::basictransitionrules::blockrule_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=asmeta::basictransitionrules::ConditionalRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::conditionalrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::ConditionalRule)

@given(instance=asmeta::basictransitionrules::MacroCallRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::macrocallrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::MacroCallRule)

@given(instance=asmeta::basictransitionrules::MacroCallRule_strategy)
def test_asmeta::basictransitionrules::macrocallrule_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=asmeta::basictransitionrules::MacroCallRule_strategy)
def test_asmeta::basictransitionrules::macrocallrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta::basictransitionrules::ExtendRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::extendrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::ExtendRule)

@given(instance=asmeta::basictransitionrules::SkipRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::skiprule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::SkipRule)

@given(instance=asmeta::basictransitionrules::ChooseRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::chooserule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::ChooseRule)

@given(instance=asmeta::basictransitionrules::ChooseRule_strategy)
def test_asmeta::basictransitionrules::chooserule_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=asmeta::basictransitionrules::ChooseRule_strategy)
def test_asmeta::basictransitionrules::chooserule_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta::basictransitionrules::Rule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::rule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::Rule)

@given(instance=DerivedRule_strategy)
@settings(max_examples=50)
def test_derivedrule_instantiation(instance):
    assert isinstance(instance, DerivedRule)

@given(instance=asmeta::derivedtransitionrules::TurboDerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::turboderivedrule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::TurboDerivedRule)

@given(instance=asmeta::derivedtransitionrules::BasicDerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::basicderivedrule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::BasicDerivedRule)

@given(instance=BasicDerivedRule_strategy)
@settings(max_examples=50)
def test_basicderivedrule_instantiation(instance):
    assert isinstance(instance, BasicDerivedRule)

@given(instance=asmeta::derivedtransitionrules::CaseRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::caserule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::CaseRule)

@given(instance=asmeta::derivedtransitionrules::CaseRule_strategy)
def test_asmeta::derivedtransitionrules::caserule_caseBranches_type(instance):
    assert isinstance(instance.caseBranches, str)


@given(instance=asmeta::derivedtransitionrules::CaseRule_strategy)
def test_asmeta::derivedtransitionrules::caserule_caseBranches_setter(instance):
    original = instance.caseBranches
    instance.caseBranches = original
    assert instance.caseBranches == original

@given(instance=TurboDerivedRule_strategy)
@settings(max_examples=50)
def test_turboderivedrule_instantiation(instance):
    assert isinstance(instance, TurboDerivedRule)

@given(instance=asmeta::derivedtransitionrules::IterativeWhileRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::iterativewhilerule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::IterativeWhileRule)

@given(instance=asmeta::derivedtransitionrules::RecursiveWhileRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::recursivewhilerule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::RecursiveWhileRule)

@given(instance=turbotransitionrules::TurboCallRule_strategy)
@settings(max_examples=50)
def test_turbotransitionrules::turbocallrule_instantiation(instance):
    assert isinstance(instance, turbotransitionrules::TurboCallRule)

@given(instance=turbotransitionrules::TurboDeclaration_strategy)
@settings(max_examples=50)
def test_turbotransitionrules::turbodeclaration_instantiation(instance):
    assert isinstance(instance, turbotransitionrules::TurboDeclaration)

@given(instance=LocalFunction_strategy)
@settings(max_examples=50)
def test_localfunction_instantiation(instance):
    assert isinstance(instance, LocalFunction)

@given(instance=basictransitionrules::Rule_strategy)
@settings(max_examples=50)
def test_basictransitionrules::rule_instantiation(instance):
    assert isinstance(instance, basictransitionrules::Rule)

@given(instance=TurboRule_strategy)
@settings(max_examples=50)
def test_turborule_instantiation(instance):
    assert isinstance(instance, TurboRule)

@given(instance=asmeta::turbotransitionrules::TurboCallRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::turbocallrule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TurboCallRule)

@given(instance=asmeta::turbotransitionrules::TurboCallRule_strategy)
def test_asmeta::turbotransitionrules::turbocallrule_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=asmeta::turbotransitionrules::TurboCallRule_strategy)
def test_asmeta::turbotransitionrules::turbocallrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta::turbotransitionrules::IterateRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::iteraterule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::IterateRule)

@given(instance=asmeta::turbotransitionrules::TurboReturnRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::turboreturnrule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TurboReturnRule)

@given(instance=asmeta::turbotransitionrules::TryCatchRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::trycatchrule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TryCatchRule)

@given(instance=asmeta::turbotransitionrules::TurboLocalStateRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::turbolocalstaterule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TurboLocalStateRule)

@given(instance=asmeta::turbotransitionrules::SeqRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::seqrule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::SeqRule)

@given(instance=asmeta::turbotransitionrules::SeqRule_strategy)
def test_asmeta::turbotransitionrules::seqrule_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=asmeta::turbotransitionrules::SeqRule_strategy)
def test_asmeta::turbotransitionrules::seqrule_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=asmeta::derivedtransitionrules::DerivedRule_strategy)
@settings(max_examples=50)
def test_asmeta::derivedtransitionrules::derivedrule_instantiation(instance):
    assert isinstance(instance, asmeta::derivedtransitionrules::DerivedRule)

@given(instance=asmeta::basictransitionrules::BasicRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::basicrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::BasicRule)

@given(instance=asmeta::basictransitionrules::TermAsRule_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::termasrule_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::TermAsRule)

@given(instance=asmeta::basictransitionrules::TermAsRule_strategy)
def test_asmeta::basictransitionrules::termasrule_parameters_type(instance):
    assert isinstance(instance.parameters, str)


@given(instance=asmeta::basictransitionrules::TermAsRule_strategy)
def test_asmeta::basictransitionrules::termasrule_parameters_setter(instance):
    original = instance.parameters
    instance.parameters = original
    assert instance.parameters == original

@given(instance=asmeta::turbotransitionrules::TurboRule_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::turborule_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TurboRule)

@given(instance=basictransitionrules::MacroDeclaration_strategy)
@settings(max_examples=50)
def test_basictransitionrules::macrodeclaration_instantiation(instance):
    assert isinstance(instance, basictransitionrules::MacroDeclaration)

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

@given(instance=asmeta::structure::Header_strategy)
@settings(max_examples=50)
def test_asmeta::structure::header_instantiation(instance):
    assert isinstance(instance, asmeta::structure::Header)

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

@given(instance=asmeta::structure::Asm_strategy)
@settings(max_examples=50)
def test_asmeta::structure::asm_instantiation(instance):
    assert isinstance(instance, asmeta::structure::Asm)

@given(instance=asmeta::structure::Asm_strategy)
def test_asmeta::structure::asm_isAsynchr_type(instance):
    assert isinstance(instance.isAsynchr, str)


@given(instance=asmeta::structure::Asm_strategy)
def test_asmeta::structure::asm_isAsynchr_setter(instance):
    original = instance.isAsynchr
    instance.isAsynchr = original
    assert instance.isAsynchr == original

@given(instance=asmeta::definitions::Classifier_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::classifier_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::Classifier)

@given(instance=asmeta::structure::Initialization_strategy)
@settings(max_examples=50)
def test_asmeta::structure::initialization_instantiation(instance):
    assert isinstance(instance, asmeta::structure::Initialization)

@given(instance=asmeta::structure::DomainDefinition_strategy)
@settings(max_examples=50)
def test_asmeta::structure::domaindefinition_instantiation(instance):
    assert isinstance(instance, asmeta::structure::DomainDefinition)

@given(instance=asmeta::structure::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_asmeta::structure::functiondefinition_instantiation(instance):
    assert isinstance(instance, asmeta::structure::FunctionDefinition)

@given(instance=asmeta::structure::ImportClause_strategy)
@settings(max_examples=50)
def test_asmeta::structure::importclause_instantiation(instance):
    assert isinstance(instance, asmeta::structure::ImportClause)

@given(instance=asmeta::structure::ImportClause_strategy)
def test_asmeta::structure::importclause_moduleName_type(instance):
    assert isinstance(instance.moduleName, str)


@given(instance=asmeta::structure::ImportClause_strategy)
def test_asmeta::structure::importclause_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original

@given(instance=asmeta::structure::ExportClause_strategy)
@settings(max_examples=50)
def test_asmeta::structure::exportclause_instantiation(instance):
    assert isinstance(instance, asmeta::structure::ExportClause)

@given(instance=domains::StructuredTd_strategy)
@settings(max_examples=50)
def test_domains::structuredtd_instantiation(instance):
    assert isinstance(instance, domains::StructuredTd)

@given(instance=Header_strategy)
@settings(max_examples=50)
def test_header_instantiation(instance):
    assert isinstance(instance, Header)

@given(instance=asmeta::structure::Signature_strategy)
@settings(max_examples=50)
def test_asmeta::structure::signature_instantiation(instance):
    assert isinstance(instance, asmeta::structure::Signature)

@given(instance=domains::ConcreteDomain_strategy)
@settings(max_examples=50)
def test_domains::concretedomain_instantiation(instance):
    assert isinstance(instance, domains::ConcreteDomain)

@given(instance=asmeta::structure::DomainInitialization_strategy)
@settings(max_examples=50)
def test_asmeta::structure::domaininitialization_instantiation(instance):
    assert isinstance(instance, asmeta::structure::DomainInitialization)

@given(instance=DynamicFunction_strategy)
@settings(max_examples=50)
def test_dynamicfunction_instantiation(instance):
    assert isinstance(instance, DynamicFunction)

@given(instance=asmeta::definitions::LocalFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::localfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::LocalFunction)

@given(instance=asmeta::definitions::OutFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::outfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::OutFunction)

@given(instance=asmeta::definitions::SharedFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::sharedfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::SharedFunction)

@given(instance=asmeta::definitions::ControlledFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::controlledfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::ControlledFunction)

@given(instance=asmeta::definitions::MonitoredFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::monitoredfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::MonitoredFunction)

@given(instance=asmeta::structure::FunctionInitialization_strategy)
@settings(max_examples=50)
def test_asmeta::structure::functioninitialization_instantiation(instance):
    assert isinstance(instance, asmeta::structure::FunctionInitialization)

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

@given(instance=asmeta::definitions::Invariant_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::invariant_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::Invariant)

@given(instance=FunctionDefinition_strategy)
@settings(max_examples=50)
def test_functiondefinition_instantiation(instance):
    assert isinstance(instance, FunctionDefinition)

@given(instance=asmeta::structure::Body_strategy)
@settings(max_examples=50)
def test_asmeta::structure::body_instantiation(instance):
    assert isinstance(instance, asmeta::structure::Body)

@given(instance=Initialization_strategy)
@settings(max_examples=50)
def test_initialization_instantiation(instance):
    assert isinstance(instance, Initialization)

@given(instance=basictransitionrules::MacroCallRule_strategy)
@settings(max_examples=50)
def test_basictransitionrules::macrocallrule_instantiation(instance):
    assert isinstance(instance, basictransitionrules::MacroCallRule)

@given(instance=asmeta::structure::AgentInitialization_strategy)
@settings(max_examples=50)
def test_asmeta::structure::agentinitialization_instantiation(instance):
    assert isinstance(instance, asmeta::structure::AgentInitialization)

@given(instance=asmeta::structure::NamedElement_strategy)
@settings(max_examples=50)
def test_asmeta::structure::namedelement_instantiation(instance):
    assert isinstance(instance, asmeta::structure::NamedElement)

@given(instance=asmeta::structure::NamedElement_strategy)
def test_asmeta::structure::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=asmeta::structure::NamedElement_strategy)
def test_asmeta::structure::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=basictransitionrules::TermAsRule_strategy)
@settings(max_examples=50)
def test_basictransitionrules::termasrule_instantiation(instance):
    assert isinstance(instance, basictransitionrules::TermAsRule)

@given(instance=domains::Domain_strategy)
@settings(max_examples=50)
def test_domains::domain_instantiation(instance):
    assert isinstance(instance, domains::Domain)

@given(instance=asmeta::basicterms::Term_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::term_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::Term)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=asmeta::basicterms::Term_strategy)
@settings(max_examples=30)
def test_asmeta::basicterms::term_compatible_changes_state(instance):
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
        assert has_statements, f"Function 'compatible' in asmeta::basicterms::Term is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'compatible' in asmeta::basicterms::Term did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'compatible' in asmeta::basicterms::Term is not implemented or raised an error")

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=asmeta::basicterms::BasicTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::basicterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::BasicTerm)

@given(instance=asmeta::basicterms::ExtendedTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::extendedterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::ExtendedTerm)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=asmeta::definitions::DerivedFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::derivedfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::DerivedFunction)

@given(instance=asmeta::definitions::BasicFunction_strategy)
@settings(max_examples=50)
def test_asmeta::definitions::basicfunction_instantiation(instance):
    assert isinstance(instance, asmeta::definitions::BasicFunction)

@given(instance=FunctionTerm_strategy)
@settings(max_examples=50)
def test_functionterm_instantiation(instance):
    assert isinstance(instance, FunctionTerm)

@given(instance=asmeta::basicterms::LocationTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::locationterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::LocationTerm)

@given(instance=RuleDeclaration_strategy)
@settings(max_examples=50)
def test_ruledeclaration_instantiation(instance):
    assert isinstance(instance, RuleDeclaration)

@given(instance=asmeta::turbotransitionrules::TurboDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta::turbotransitionrules::turbodeclaration_instantiation(instance):
    assert isinstance(instance, asmeta::turbotransitionrules::TurboDeclaration)

@given(instance=asmeta::basictransitionrules::MacroDeclaration_strategy)
@settings(max_examples=50)
def test_asmeta::basictransitionrules::macrodeclaration_instantiation(instance):
    assert isinstance(instance, asmeta::basictransitionrules::MacroDeclaration)

@given(instance=furtherterms::FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_furtherterms::finitequantificationterm_instantiation(instance):
    assert isinstance(instance, furtherterms::FiniteQuantificationTerm)

@given(instance=BasicTerm_strategy)
@settings(max_examples=50)
def test_basicterm_instantiation(instance):
    assert isinstance(instance, BasicTerm)

@given(instance=asmeta::basicterms::FunctionTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::functionterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::FunctionTerm)

@given(instance=asmeta::basicterms::ConstantTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::constantterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::ConstantTerm)

@given(instance=asmeta::basicterms::ConstantTerm_strategy)
def test_asmeta::basicterms::constantterm_symbol_type(instance):
    assert isinstance(instance.symbol, str)


@given(instance=asmeta::basicterms::ConstantTerm_strategy)
def test_asmeta::basicterms::constantterm_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=asmeta::basicterms::VariableTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::variableterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::VariableTerm)

@given(instance=asmeta::basicterms::VariableTerm_strategy)
def test_asmeta::basicterms::variableterm_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=asmeta::basicterms::VariableTerm_strategy)
def test_asmeta::basicterms::variableterm_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=asmeta::basicterms::VariableTerm_strategy)
def test_asmeta::basicterms::variableterm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=asmeta::basicterms::VariableTerm_strategy)
def test_asmeta::basicterms::variableterm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_finitequantificationterm_instantiation(instance):
    assert isinstance(instance, FiniteQuantificationTerm)

@given(instance=asmeta::furtherterms::ExistTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::existterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ExistTerm)

@given(instance=asmeta::furtherterms::ExistUniqueTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::existuniqueterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ExistUniqueTerm)

@given(instance=asmeta::furtherterms::ForallTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::forallterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ForallTerm)

@given(instance=basicterms::Term_strategy)
@settings(max_examples=50)
def test_basicterms::term_instantiation(instance):
    assert isinstance(instance, basicterms::Term)

@given(instance=basicterms::VariableTerm_strategy)
@settings(max_examples=50)
def test_basicterms::variableterm_instantiation(instance):
    assert isinstance(instance, basicterms::VariableTerm)

@given(instance=VariableBindingTerm_strategy)
@settings(max_examples=50)
def test_variablebindingterm_instantiation(instance):
    assert isinstance(instance, VariableBindingTerm)

@given(instance=asmeta::furtherterms::FiniteQuantificationTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::finitequantificationterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::FiniteQuantificationTerm)

@given(instance=asmeta::furtherterms::FiniteQuantificationTerm_strategy)
def test_asmeta::furtherterms::finitequantificationterm_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=asmeta::furtherterms::FiniteQuantificationTerm_strategy)
def test_asmeta::furtherterms::finitequantificationterm_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta::furtherterms::ComprehensionTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::comprehensionterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ComprehensionTerm)

@given(instance=asmeta::furtherterms::ComprehensionTerm_strategy)
def test_asmeta::furtherterms::comprehensionterm_ranges_type(instance):
    assert isinstance(instance.ranges, str)


@given(instance=asmeta::furtherterms::ComprehensionTerm_strategy)
def test_asmeta::furtherterms::comprehensionterm_ranges_setter(instance):
    original = instance.ranges
    instance.ranges = original
    assert instance.ranges == original

@given(instance=asmeta::furtherterms::LetTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::letterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::LetTerm)

@given(instance=basicterms::TupleTerm_strategy)
@settings(max_examples=50)
def test_basicterms::tupleterm_instantiation(instance):
    assert isinstance(instance, basicterms::TupleTerm)

@given(instance=CollectionTerm_strategy)
@settings(max_examples=50)
def test_collectionterm_instantiation(instance):
    assert isinstance(instance, CollectionTerm)

@given(instance=asmeta::furtherterms::MapTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::mapterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::MapTerm)

@given(instance=asmeta::basicterms::SetTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::setterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::SetTerm)

@given(instance=asmeta::furtherterms::BagTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::bagterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::BagTerm)

@given(instance=asmeta::furtherterms::SequenceTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::sequenceterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::SequenceTerm)

@given(instance=asmeta::furtherterms::SequenceTerm_strategy)
def test_asmeta::furtherterms::sequenceterm_terms_type(instance):
    assert isinstance(instance.terms, str)


@given(instance=asmeta::furtherterms::SequenceTerm_strategy)
def test_asmeta::furtherterms::sequenceterm_terms_setter(instance):
    original = instance.terms
    instance.terms = original
    assert instance.terms == original

@given(instance=ComprehensionTerm_strategy)
@settings(max_examples=50)
def test_comprehensionterm_instantiation(instance):
    assert isinstance(instance, ComprehensionTerm)

@given(instance=asmeta::furtherterms::SequenceCt_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::sequencect_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::SequenceCt)

@given(instance=asmeta::furtherterms::BagCt_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::bagct_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::BagCt)

@given(instance=asmeta::furtherterms::MapCt_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::mapct_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::MapCt)

@given(instance=asmeta::furtherterms::SetCt_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::setct_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::SetCt)

@given(instance=ExtendedTerm_strategy)
@settings(max_examples=50)
def test_extendedterm_instantiation(instance):
    assert isinstance(instance, ExtendedTerm)

@given(instance=asmeta::furtherterms::ConditionalTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::conditionalterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ConditionalTerm)

@given(instance=asmeta::basicterms::RuleAsTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::ruleasterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::RuleAsTerm)

@given(instance=asmeta::basicterms::CollectionTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::collectionterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::CollectionTerm)

@given(instance=asmeta::basicterms::CollectionTerm_strategy)
def test_asmeta::basicterms::collectionterm_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=asmeta::basicterms::CollectionTerm_strategy)
def test_asmeta::basicterms::collectionterm_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=asmeta::basicterms::TupleTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::tupleterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::TupleTerm)

@given(instance=asmeta::basicterms::TupleTerm_strategy)
def test_asmeta::basicterms::tupleterm_arity_type(instance):
    assert isinstance(instance.arity, str)


@given(instance=asmeta::basicterms::TupleTerm_strategy)
def test_asmeta::basicterms::tupleterm_arity_setter(instance):
    original = instance.arity
    instance.arity = original
    assert instance.arity == original

@given(instance=asmeta::basicterms::TupleTerm_strategy)
def test_asmeta::basicterms::tupleterm_terms_type(instance):
    assert isinstance(instance.terms, str)


@given(instance=asmeta::basicterms::TupleTerm_strategy)
def test_asmeta::basicterms::tupleterm_terms_setter(instance):
    original = instance.terms
    instance.terms = original
    assert instance.terms == original

@given(instance=asmeta::furtherterms::CaseTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::caseterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::CaseTerm)

@given(instance=asmeta::furtherterms::CaseTerm_strategy)
def test_asmeta::furtherterms::caseterm_resultTerms_type(instance):
    assert isinstance(instance.resultTerms, str)


@given(instance=asmeta::furtherterms::CaseTerm_strategy)
def test_asmeta::furtherterms::caseterm_resultTerms_setter(instance):
    original = instance.resultTerms
    instance.resultTerms = original
    assert instance.resultTerms == original

@given(instance=asmeta::basicterms::DomainTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::domainterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::DomainTerm)

@given(instance=asmeta::furtherterms::VariableBindingTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::variablebindingterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::VariableBindingTerm)

@given(instance=ConstantTerm_strategy)
@settings(max_examples=50)
def test_constantterm_instantiation(instance):
    assert isinstance(instance, ConstantTerm)

@given(instance=asmeta::furtherterms::RealTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::realterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::RealTerm)

@given(instance=asmeta::furtherterms::EnumTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::enumterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::EnumTerm)

@given(instance=asmeta::basicterms::UndefTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::undefterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::UndefTerm)

@given(instance=asmeta::furtherterms::StringTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::stringterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::StringTerm)

@given(instance=asmeta::furtherterms::NaturalTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::naturalterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::NaturalTerm)

@given(instance=asmeta::furtherterms::CharTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::charterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::CharTerm)

@given(instance=asmeta::furtherterms::ComplexTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::complexterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::ComplexTerm)

@given(instance=asmeta::basicterms::BooleanTerm_strategy)
@settings(max_examples=50)
def test_asmeta::basicterms::booleanterm_instantiation(instance):
    assert isinstance(instance, asmeta::basicterms::BooleanTerm)

@given(instance=asmeta::furtherterms::IntegerTerm_strategy)
@settings(max_examples=50)
def test_asmeta::furtherterms::integerterm_instantiation(instance):
    assert isinstance(instance, asmeta::furtherterms::IntegerTerm)
