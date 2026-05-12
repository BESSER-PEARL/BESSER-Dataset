import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    RequirementSet,
    reqSpec::GlobalRequirementSet,
    reqSpec::SystemRequirementSet,
    ReqPredicate,
    reqSpec::Predicate,
    reqSpec::InformalPredicate,
    reqSpec::AVariableReference,
    reqSpec::DesiredValue,
    reqSpec::ValuePredicate,
    reqSpec::PropertyExpression,
    reqSpec::ErrorBehaviorState,
    reqSpec::Mode,
    reqSpec::IncludeGlobalRequirement,
    reqSpec::ReqPredicate,
    reqSpec::Stakeholder,
    ContractualElement,
    reqSpec::DocumentSection,
    reqSpec::Requirement,
    reqSpec::Uncertainty,
    ReqRoot,
    reqSpec::RequirementSet,
    reqSpec::ReqDocument,
    reqSpec::StakeholderGoals,
    reqSpec::ReqRoot,
    reqSpec::Goal,
    reqSpec::ExternalDocument,
    reqSpec::ContractualElement,
    reqSpec::AVariableDeclaration,
    reqSpec::Rationale,
    reqSpec::WhenCondition,
    reqSpec::Description,
    reqSpec::Category,
    reqSpec::NamedElement,
    reqSpec::ComponentClassifier,
    reqSpec::GlobalConstants,
    reqSpec::EObject,
    reqSpec::ReqSpec,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_requirementset_is_not_abstract():
    assert not inspect.isabstract(RequirementSet)


def test_requirementset_constructor_exists():
    assert callable(RequirementSet.__init__)


def test_requirementset_constructor_args():
    sig = inspect.signature(RequirementSet.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::globalrequirementset_is_not_abstract():
    assert not inspect.isabstract(reqSpec::GlobalRequirementSet)


def test_reqspec::globalrequirementset_constructor_exists():
    assert callable(reqSpec::GlobalRequirementSet.__init__)


def test_reqspec::globalrequirementset_constructor_args():
    sig = inspect.signature(reqSpec::GlobalRequirementSet.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::systemrequirementset_is_not_abstract():
    assert not inspect.isabstract(reqSpec::SystemRequirementSet)


def test_reqspec::systemrequirementset_constructor_exists():
    assert callable(reqSpec::SystemRequirementSet.__init__)


def test_reqspec::systemrequirementset_constructor_args():
    sig = inspect.signature(reqSpec::SystemRequirementSet.__init__)
    params = list(sig.parameters.keys())



def test_reqpredicate_is_not_abstract():
    assert not inspect.isabstract(ReqPredicate)


def test_reqpredicate_constructor_exists():
    assert callable(ReqPredicate.__init__)


def test_reqpredicate_constructor_args():
    sig = inspect.signature(ReqPredicate.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::predicate_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Predicate)


def test_reqspec::predicate_constructor_exists():
    assert callable(reqSpec::Predicate.__init__)


def test_reqspec::predicate_constructor_args():
    sig = inspect.signature(reqSpec::Predicate.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::informalpredicate_is_not_abstract():
    assert not inspect.isabstract(reqSpec::InformalPredicate)


def test_reqspec::informalpredicate_constructor_exists():
    assert callable(reqSpec::InformalPredicate.__init__)


def test_reqspec::informalpredicate_constructor_args():
    sig = inspect.signature(reqSpec::InformalPredicate.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_reqspec::informalpredicate_has_description():
    assert hasattr(reqSpec::InformalPredicate, "description")
    descriptor = None
    for klass in reqSpec::InformalPredicate.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::avariablereference_is_not_abstract():
    assert not inspect.isabstract(reqSpec::AVariableReference)


def test_reqspec::avariablereference_constructor_exists():
    assert callable(reqSpec::AVariableReference.__init__)


def test_reqspec::avariablereference_constructor_args():
    sig = inspect.signature(reqSpec::AVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::desiredvalue_is_not_abstract():
    assert not inspect.isabstract(reqSpec::DesiredValue)


def test_reqspec::desiredvalue_constructor_exists():
    assert callable(reqSpec::DesiredValue.__init__)


def test_reqspec::desiredvalue_constructor_args():
    sig = inspect.signature(reqSpec::DesiredValue.__init__)
    params = list(sig.parameters.keys())
    assert "upto" in params, "Missing parameter 'upto'"

def test_reqspec::desiredvalue_has_upto():
    assert hasattr(reqSpec::DesiredValue, "upto")
    descriptor = None
    for klass in reqSpec::DesiredValue.__mro__:
        if "upto" in klass.__dict__:
            descriptor = klass.__dict__["upto"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::valuepredicate_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ValuePredicate)


def test_reqspec::valuepredicate_constructor_exists():
    assert callable(reqSpec::ValuePredicate.__init__)


def test_reqspec::valuepredicate_constructor_args():
    sig = inspect.signature(reqSpec::ValuePredicate.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::propertyexpression_is_not_abstract():
    assert not inspect.isabstract(reqSpec::PropertyExpression)


def test_reqspec::propertyexpression_constructor_exists():
    assert callable(reqSpec::PropertyExpression.__init__)


def test_reqspec::propertyexpression_constructor_args():
    sig = inspect.signature(reqSpec::PropertyExpression.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::errorbehaviorstate_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ErrorBehaviorState)


def test_reqspec::errorbehaviorstate_constructor_exists():
    assert callable(reqSpec::ErrorBehaviorState.__init__)


def test_reqspec::errorbehaviorstate_constructor_args():
    sig = inspect.signature(reqSpec::ErrorBehaviorState.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::mode_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Mode)


def test_reqspec::mode_constructor_exists():
    assert callable(reqSpec::Mode.__init__)


def test_reqspec::mode_constructor_args():
    sig = inspect.signature(reqSpec::Mode.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::includeglobalrequirement_is_not_abstract():
    assert not inspect.isabstract(reqSpec::IncludeGlobalRequirement)


def test_reqspec::includeglobalrequirement_constructor_exists():
    assert callable(reqSpec::IncludeGlobalRequirement.__init__)


def test_reqspec::includeglobalrequirement_constructor_args():
    sig = inspect.signature(reqSpec::IncludeGlobalRequirement.__init__)
    params = list(sig.parameters.keys())
    assert "componentCategory" in params, "Missing parameter 'componentCategory'"
    assert "self" in params, "Missing parameter 'self'"

def test_reqspec::includeglobalrequirement_has_componentCategory():
    assert hasattr(reqSpec::IncludeGlobalRequirement, "componentCategory")
    descriptor = None
    for klass in reqSpec::IncludeGlobalRequirement.__mro__:
        if "componentCategory" in klass.__dict__:
            descriptor = klass.__dict__["componentCategory"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::includeglobalrequirement_has_self():
    assert hasattr(reqSpec::IncludeGlobalRequirement, "self")
    descriptor = None
    for klass in reqSpec::IncludeGlobalRequirement.__mro__:
        if "self" in klass.__dict__:
            descriptor = klass.__dict__["self"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::reqpredicate_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ReqPredicate)


def test_reqspec::reqpredicate_constructor_exists():
    assert callable(reqSpec::ReqPredicate.__init__)


def test_reqspec::reqpredicate_constructor_args():
    sig = inspect.signature(reqSpec::ReqPredicate.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::stakeholder_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Stakeholder)


def test_reqspec::stakeholder_constructor_exists():
    assert callable(reqSpec::Stakeholder.__init__)


def test_reqspec::stakeholder_constructor_args():
    sig = inspect.signature(reqSpec::Stakeholder.__init__)
    params = list(sig.parameters.keys())



def test_contractualelement_is_not_abstract():
    assert not inspect.isabstract(ContractualElement)


def test_contractualelement_constructor_exists():
    assert callable(ContractualElement.__init__)


def test_contractualelement_constructor_args():
    sig = inspect.signature(ContractualElement.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::documentsection_is_not_abstract():
    assert not inspect.isabstract(reqSpec::DocumentSection)


def test_reqspec::documentsection_constructor_exists():
    assert callable(reqSpec::DocumentSection.__init__)


def test_reqspec::documentsection_constructor_args():
    sig = inspect.signature(reqSpec::DocumentSection.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "title" in params, "Missing parameter 'title'"

def test_reqspec::documentsection_has_label():
    assert hasattr(reqSpec::DocumentSection, "label")
    descriptor = None
    for klass in reqSpec::DocumentSection.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::documentsection_has_title():
    assert hasattr(reqSpec::DocumentSection, "title")
    descriptor = None
    for klass in reqSpec::DocumentSection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::requirement_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Requirement)


def test_reqspec::requirement_constructor_exists():
    assert callable(reqSpec::Requirement.__init__)


def test_reqspec::requirement_constructor_args():
    sig = inspect.signature(reqSpec::Requirement.__init__)
    params = list(sig.parameters.keys())
    assert "connections" in params, "Missing parameter 'connections'"
    assert "exceptionText" in params, "Missing parameter 'exceptionText'"
    assert "componentCategory" in params, "Missing parameter 'componentCategory'"

def test_reqspec::requirement_has_connections():
    assert hasattr(reqSpec::Requirement, "connections")
    descriptor = None
    for klass in reqSpec::Requirement.__mro__:
        if "connections" in klass.__dict__:
            descriptor = klass.__dict__["connections"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::requirement_has_exceptionText():
    assert hasattr(reqSpec::Requirement, "exceptionText")
    descriptor = None
    for klass in reqSpec::Requirement.__mro__:
        if "exceptionText" in klass.__dict__:
            descriptor = klass.__dict__["exceptionText"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::requirement_has_componentCategory():
    assert hasattr(reqSpec::Requirement, "componentCategory")
    descriptor = None
    for klass in reqSpec::Requirement.__mro__:
        if "componentCategory" in klass.__dict__:
            descriptor = klass.__dict__["componentCategory"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::uncertainty_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Uncertainty)


def test_reqspec::uncertainty_constructor_exists():
    assert callable(reqSpec::Uncertainty.__init__)


def test_reqspec::uncertainty_constructor_args():
    sig = inspect.signature(reqSpec::Uncertainty.__init__)
    params = list(sig.parameters.keys())



def test_reqroot_is_not_abstract():
    assert not inspect.isabstract(ReqRoot)


def test_reqroot_constructor_exists():
    assert callable(ReqRoot.__init__)


def test_reqroot_constructor_args():
    sig = inspect.signature(ReqRoot.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::requirementset_is_not_abstract():
    assert not inspect.isabstract(reqSpec::RequirementSet)


def test_reqspec::requirementset_constructor_exists():
    assert callable(reqSpec::RequirementSet.__init__)


def test_reqspec::requirementset_constructor_args():
    sig = inspect.signature(reqSpec::RequirementSet.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::reqdocument_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ReqDocument)


def test_reqspec::reqdocument_constructor_exists():
    assert callable(reqSpec::ReqDocument.__init__)


def test_reqspec::reqdocument_constructor_args():
    sig = inspect.signature(reqSpec::ReqDocument.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::stakeholdergoals_is_not_abstract():
    assert not inspect.isabstract(reqSpec::StakeholderGoals)


def test_reqspec::stakeholdergoals_constructor_exists():
    assert callable(reqSpec::StakeholderGoals.__init__)


def test_reqspec::stakeholdergoals_constructor_args():
    sig = inspect.signature(reqSpec::StakeholderGoals.__init__)
    params = list(sig.parameters.keys())
    assert "componentCategory" in params, "Missing parameter 'componentCategory'"

def test_reqspec::stakeholdergoals_has_componentCategory():
    assert hasattr(reqSpec::StakeholderGoals, "componentCategory")
    descriptor = None
    for klass in reqSpec::StakeholderGoals.__mro__:
        if "componentCategory" in klass.__dict__:
            descriptor = klass.__dict__["componentCategory"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::reqroot_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ReqRoot)


def test_reqspec::reqroot_constructor_exists():
    assert callable(reqSpec::ReqRoot.__init__)


def test_reqspec::reqroot_constructor_args():
    sig = inspect.signature(reqSpec::ReqRoot.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "issues" in params, "Missing parameter 'issues'"
    assert "title" in params, "Missing parameter 'title'"

def test_reqspec::reqroot_has_name():
    assert hasattr(reqSpec::ReqRoot, "name")
    descriptor = None
    for klass in reqSpec::ReqRoot.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::reqroot_has_issues():
    assert hasattr(reqSpec::ReqRoot, "issues")
    descriptor = None
    for klass in reqSpec::ReqRoot.__mro__:
        if "issues" in klass.__dict__:
            descriptor = klass.__dict__["issues"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::reqroot_has_title():
    assert hasattr(reqSpec::ReqRoot, "title")
    descriptor = None
    for klass in reqSpec::ReqRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::goal_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Goal)


def test_reqspec::goal_constructor_exists():
    assert callable(reqSpec::Goal.__init__)


def test_reqspec::goal_constructor_args():
    sig = inspect.signature(reqSpec::Goal.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::externaldocument_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ExternalDocument)


def test_reqspec::externaldocument_constructor_exists():
    assert callable(reqSpec::ExternalDocument.__init__)


def test_reqspec::externaldocument_constructor_args():
    sig = inspect.signature(reqSpec::ExternalDocument.__init__)
    params = list(sig.parameters.keys())
    assert "docReference" in params, "Missing parameter 'docReference'"
    assert "docFragment" in params, "Missing parameter 'docFragment'"

def test_reqspec::externaldocument_has_docReference():
    assert hasattr(reqSpec::ExternalDocument, "docReference")
    descriptor = None
    for klass in reqSpec::ExternalDocument.__mro__:
        if "docReference" in klass.__dict__:
            descriptor = klass.__dict__["docReference"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::externaldocument_has_docFragment():
    assert hasattr(reqSpec::ExternalDocument, "docFragment")
    descriptor = None
    for klass in reqSpec::ExternalDocument.__mro__:
        if "docFragment" in klass.__dict__:
            descriptor = klass.__dict__["docFragment"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::contractualelement_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ContractualElement)


def test_reqspec::contractualelement_constructor_exists():
    assert callable(reqSpec::ContractualElement.__init__)


def test_reqspec::contractualelement_constructor_args():
    sig = inspect.signature(reqSpec::ContractualElement.__init__)
    params = list(sig.parameters.keys())
    assert "targetDescription" in params, "Missing parameter 'targetDescription'"
    assert "name" in params, "Missing parameter 'name'"
    assert "issues" in params, "Missing parameter 'issues'"
    assert "dropRationale" in params, "Missing parameter 'dropRationale'"
    assert "title" in params, "Missing parameter 'title'"
    assert "dropped" in params, "Missing parameter 'dropped'"

def test_reqspec::contractualelement_has_targetDescription():
    assert hasattr(reqSpec::ContractualElement, "targetDescription")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "targetDescription" in klass.__dict__:
            descriptor = klass.__dict__["targetDescription"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::contractualelement_has_name():
    assert hasattr(reqSpec::ContractualElement, "name")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::contractualelement_has_issues():
    assert hasattr(reqSpec::ContractualElement, "issues")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "issues" in klass.__dict__:
            descriptor = klass.__dict__["issues"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::contractualelement_has_dropRationale():
    assert hasattr(reqSpec::ContractualElement, "dropRationale")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "dropRationale" in klass.__dict__:
            descriptor = klass.__dict__["dropRationale"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::contractualelement_has_title():
    assert hasattr(reqSpec::ContractualElement, "title")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_reqspec::contractualelement_has_dropped():
    assert hasattr(reqSpec::ContractualElement, "dropped")
    descriptor = None
    for klass in reqSpec::ContractualElement.__mro__:
        if "dropped" in klass.__dict__:
            descriptor = klass.__dict__["dropped"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::avariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(reqSpec::AVariableDeclaration)


def test_reqspec::avariabledeclaration_constructor_exists():
    assert callable(reqSpec::AVariableDeclaration.__init__)


def test_reqspec::avariabledeclaration_constructor_args():
    sig = inspect.signature(reqSpec::AVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::rationale_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Rationale)


def test_reqspec::rationale_constructor_exists():
    assert callable(reqSpec::Rationale.__init__)


def test_reqspec::rationale_constructor_args():
    sig = inspect.signature(reqSpec::Rationale.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::whencondition_is_not_abstract():
    assert not inspect.isabstract(reqSpec::WhenCondition)


def test_reqspec::whencondition_constructor_exists():
    assert callable(reqSpec::WhenCondition.__init__)


def test_reqspec::whencondition_constructor_args():
    sig = inspect.signature(reqSpec::WhenCondition.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::description_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Description)


def test_reqspec::description_constructor_exists():
    assert callable(reqSpec::Description.__init__)


def test_reqspec::description_constructor_args():
    sig = inspect.signature(reqSpec::Description.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::category_is_not_abstract():
    assert not inspect.isabstract(reqSpec::Category)


def test_reqspec::category_constructor_exists():
    assert callable(reqSpec::Category.__init__)


def test_reqspec::category_constructor_args():
    sig = inspect.signature(reqSpec::Category.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::namedelement_is_not_abstract():
    assert not inspect.isabstract(reqSpec::NamedElement)


def test_reqspec::namedelement_constructor_exists():
    assert callable(reqSpec::NamedElement.__init__)


def test_reqspec::namedelement_constructor_args():
    sig = inspect.signature(reqSpec::NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::componentclassifier_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ComponentClassifier)


def test_reqspec::componentclassifier_constructor_exists():
    assert callable(reqSpec::ComponentClassifier.__init__)


def test_reqspec::componentclassifier_constructor_args():
    sig = inspect.signature(reqSpec::ComponentClassifier.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::globalconstants_is_not_abstract():
    assert not inspect.isabstract(reqSpec::GlobalConstants)


def test_reqspec::globalconstants_constructor_exists():
    assert callable(reqSpec::GlobalConstants.__init__)


def test_reqspec::globalconstants_constructor_args():
    sig = inspect.signature(reqSpec::GlobalConstants.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_reqspec::globalconstants_has_name():
    assert hasattr(reqSpec::GlobalConstants, "name")
    descriptor = None
    for klass in reqSpec::GlobalConstants.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_reqspec::eobject_is_not_abstract():
    assert not inspect.isabstract(reqSpec::EObject)


def test_reqspec::eobject_constructor_exists():
    assert callable(reqSpec::EObject.__init__)


def test_reqspec::eobject_constructor_args():
    sig = inspect.signature(reqSpec::EObject.__init__)
    params = list(sig.parameters.keys())



def test_reqspec::reqspec_is_not_abstract():
    assert not inspect.isabstract(reqSpec::ReqSpec)


def test_reqspec::reqspec_constructor_exists():
    assert callable(reqSpec::ReqSpec.__init__)


def test_reqspec::reqspec_constructor_args():
    sig = inspect.signature(reqSpec::ReqSpec.__init__)
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
RequirementSet_strategy = st.builds(
    RequirementSet,
)
reqSpec::GlobalRequirementSet_strategy = st.builds(
    reqSpec::GlobalRequirementSet,
)
reqSpec::SystemRequirementSet_strategy = st.builds(
    reqSpec::SystemRequirementSet,
)
ReqPredicate_strategy = st.builds(
    ReqPredicate,
)
reqSpec::Predicate_strategy = st.builds(
    reqSpec::Predicate,
)
reqSpec::InformalPredicate_strategy = st.builds(
    reqSpec::InformalPredicate,
    description=
        safe_text
)
reqSpec::AVariableReference_strategy = st.builds(
    reqSpec::AVariableReference,
)
reqSpec::DesiredValue_strategy = st.builds(
    reqSpec::DesiredValue,
    upto=
        st.booleans()
)
reqSpec::ValuePredicate_strategy = st.builds(
    reqSpec::ValuePredicate,
)
reqSpec::PropertyExpression_strategy = st.builds(
    reqSpec::PropertyExpression,
)
reqSpec::ErrorBehaviorState_strategy = st.builds(
    reqSpec::ErrorBehaviorState,
)
reqSpec::Mode_strategy = st.builds(
    reqSpec::Mode,
)
reqSpec::IncludeGlobalRequirement_strategy = st.builds(
    reqSpec::IncludeGlobalRequirement,
    componentCategory=
        safe_text,
    self=
        st.booleans()
)
reqSpec::ReqPredicate_strategy = st.builds(
    reqSpec::ReqPredicate,
)
reqSpec::Stakeholder_strategy = st.builds(
    reqSpec::Stakeholder,
)
ContractualElement_strategy = st.builds(
    ContractualElement,
)
reqSpec::DocumentSection_strategy = st.builds(
    reqSpec::DocumentSection,
    label=
        safe_text,
    title=
        safe_text
)
reqSpec::Requirement_strategy = st.builds(
    reqSpec::Requirement,
    connections=
        st.booleans(),
    exceptionText=
        safe_text,
    componentCategory=
        safe_text
)
reqSpec::Uncertainty_strategy = st.builds(
    reqSpec::Uncertainty,
)
ReqRoot_strategy = st.builds(
    ReqRoot,
)
reqSpec::RequirementSet_strategy = st.builds(
    reqSpec::RequirementSet,
)
reqSpec::ReqDocument_strategy = st.builds(
    reqSpec::ReqDocument,
)
reqSpec::StakeholderGoals_strategy = st.builds(
    reqSpec::StakeholderGoals,
    componentCategory=
        safe_text
)
reqSpec::ReqRoot_strategy = st.builds(
    reqSpec::ReqRoot,
    name=
        safe_text,
    issues=
        safe_text,
    title=
        safe_text
)
reqSpec::Goal_strategy = st.builds(
    reqSpec::Goal,
)
reqSpec::ExternalDocument_strategy = st.builds(
    reqSpec::ExternalDocument,
    docReference=
        safe_text,
    docFragment=
        safe_text
)
reqSpec::ContractualElement_strategy = st.builds(
    reqSpec::ContractualElement,
    targetDescription=
        safe_text,
    name=
        safe_text,
    issues=
        safe_text,
    dropRationale=
        safe_text,
    title=
        safe_text,
    dropped=
        st.booleans()
)
reqSpec::AVariableDeclaration_strategy = st.builds(
    reqSpec::AVariableDeclaration,
)
reqSpec::Rationale_strategy = st.builds(
    reqSpec::Rationale,
)
reqSpec::WhenCondition_strategy = st.builds(
    reqSpec::WhenCondition,
)
reqSpec::Description_strategy = st.builds(
    reqSpec::Description,
)
reqSpec::Category_strategy = st.builds(
    reqSpec::Category,
)
reqSpec::NamedElement_strategy = st.builds(
    reqSpec::NamedElement,
)
reqSpec::ComponentClassifier_strategy = st.builds(
    reqSpec::ComponentClassifier,
)
reqSpec::GlobalConstants_strategy = st.builds(
    reqSpec::GlobalConstants,
    name=
        safe_text
)
reqSpec::EObject_strategy = st.builds(
    reqSpec::EObject,
)
reqSpec::ReqSpec_strategy = st.builds(
    reqSpec::ReqSpec,
)

@given(instance=RequirementSet_strategy)
@settings(max_examples=50)
def test_requirementset_instantiation(instance):
    assert isinstance(instance, RequirementSet)

@given(instance=reqSpec::GlobalRequirementSet_strategy)
@settings(max_examples=50)
def test_reqspec::globalrequirementset_instantiation(instance):
    assert isinstance(instance, reqSpec::GlobalRequirementSet)

@given(instance=reqSpec::SystemRequirementSet_strategy)
@settings(max_examples=50)
def test_reqspec::systemrequirementset_instantiation(instance):
    assert isinstance(instance, reqSpec::SystemRequirementSet)

@given(instance=ReqPredicate_strategy)
@settings(max_examples=50)
def test_reqpredicate_instantiation(instance):
    assert isinstance(instance, ReqPredicate)

@given(instance=reqSpec::Predicate_strategy)
@settings(max_examples=50)
def test_reqspec::predicate_instantiation(instance):
    assert isinstance(instance, reqSpec::Predicate)

@given(instance=reqSpec::InformalPredicate_strategy)
@settings(max_examples=50)
def test_reqspec::informalpredicate_instantiation(instance):
    assert isinstance(instance, reqSpec::InformalPredicate)

@given(instance=reqSpec::InformalPredicate_strategy)
def test_reqspec::informalpredicate_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=reqSpec::InformalPredicate_strategy)
def test_reqspec::informalpredicate_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=reqSpec::AVariableReference_strategy)
@settings(max_examples=50)
def test_reqspec::avariablereference_instantiation(instance):
    assert isinstance(instance, reqSpec::AVariableReference)

@given(instance=reqSpec::DesiredValue_strategy)
@settings(max_examples=50)
def test_reqspec::desiredvalue_instantiation(instance):
    assert isinstance(instance, reqSpec::DesiredValue)

@given(instance=reqSpec::DesiredValue_strategy)
def test_reqspec::desiredvalue_upto_type(instance):
    assert isinstance(instance.upto, bool)


@given(instance=reqSpec::DesiredValue_strategy)
def test_reqspec::desiredvalue_upto_setter(instance):
    original = instance.upto
    instance.upto = original
    assert instance.upto == original

@given(instance=reqSpec::ValuePredicate_strategy)
@settings(max_examples=50)
def test_reqspec::valuepredicate_instantiation(instance):
    assert isinstance(instance, reqSpec::ValuePredicate)

@given(instance=reqSpec::PropertyExpression_strategy)
@settings(max_examples=50)
def test_reqspec::propertyexpression_instantiation(instance):
    assert isinstance(instance, reqSpec::PropertyExpression)

@given(instance=reqSpec::ErrorBehaviorState_strategy)
@settings(max_examples=50)
def test_reqspec::errorbehaviorstate_instantiation(instance):
    assert isinstance(instance, reqSpec::ErrorBehaviorState)

@given(instance=reqSpec::Mode_strategy)
@settings(max_examples=50)
def test_reqspec::mode_instantiation(instance):
    assert isinstance(instance, reqSpec::Mode)

@given(instance=reqSpec::IncludeGlobalRequirement_strategy)
@settings(max_examples=50)
def test_reqspec::includeglobalrequirement_instantiation(instance):
    assert isinstance(instance, reqSpec::IncludeGlobalRequirement)

@given(instance=reqSpec::IncludeGlobalRequirement_strategy)
def test_reqspec::includeglobalrequirement_componentCategory_type(instance):
    assert isinstance(instance.componentCategory, str)


@given(instance=reqSpec::IncludeGlobalRequirement_strategy)
def test_reqspec::includeglobalrequirement_componentCategory_setter(instance):
    original = instance.componentCategory
    instance.componentCategory = original
    assert instance.componentCategory == original

@given(instance=reqSpec::IncludeGlobalRequirement_strategy)
def test_reqspec::includeglobalrequirement_self_type(instance):
    assert isinstance(instance.self, bool)


@given(instance=reqSpec::IncludeGlobalRequirement_strategy)
def test_reqspec::includeglobalrequirement_self_setter(instance):
    original = instance.self
    instance.self = original
    assert instance.self == original

@given(instance=reqSpec::ReqPredicate_strategy)
@settings(max_examples=50)
def test_reqspec::reqpredicate_instantiation(instance):
    assert isinstance(instance, reqSpec::ReqPredicate)

@given(instance=reqSpec::Stakeholder_strategy)
@settings(max_examples=50)
def test_reqspec::stakeholder_instantiation(instance):
    assert isinstance(instance, reqSpec::Stakeholder)

@given(instance=ContractualElement_strategy)
@settings(max_examples=50)
def test_contractualelement_instantiation(instance):
    assert isinstance(instance, ContractualElement)

@given(instance=reqSpec::DocumentSection_strategy)
@settings(max_examples=50)
def test_reqspec::documentsection_instantiation(instance):
    assert isinstance(instance, reqSpec::DocumentSection)

@given(instance=reqSpec::DocumentSection_strategy)
def test_reqspec::documentsection_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=reqSpec::DocumentSection_strategy)
def test_reqspec::documentsection_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=reqSpec::DocumentSection_strategy)
def test_reqspec::documentsection_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=reqSpec::DocumentSection_strategy)
def test_reqspec::documentsection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=reqSpec::Requirement_strategy)
@settings(max_examples=50)
def test_reqspec::requirement_instantiation(instance):
    assert isinstance(instance, reqSpec::Requirement)

@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_connections_type(instance):
    assert isinstance(instance.connections, bool)


@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_connections_setter(instance):
    original = instance.connections
    instance.connections = original
    assert instance.connections == original

@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_exceptionText_type(instance):
    assert isinstance(instance.exceptionText, str)


@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_exceptionText_setter(instance):
    original = instance.exceptionText
    instance.exceptionText = original
    assert instance.exceptionText == original

@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_componentCategory_type(instance):
    assert isinstance(instance.componentCategory, str)


@given(instance=reqSpec::Requirement_strategy)
def test_reqspec::requirement_componentCategory_setter(instance):
    original = instance.componentCategory
    instance.componentCategory = original
    assert instance.componentCategory == original

@given(instance=reqSpec::Uncertainty_strategy)
@settings(max_examples=50)
def test_reqspec::uncertainty_instantiation(instance):
    assert isinstance(instance, reqSpec::Uncertainty)

@given(instance=ReqRoot_strategy)
@settings(max_examples=50)
def test_reqroot_instantiation(instance):
    assert isinstance(instance, ReqRoot)

@given(instance=reqSpec::RequirementSet_strategy)
@settings(max_examples=50)
def test_reqspec::requirementset_instantiation(instance):
    assert isinstance(instance, reqSpec::RequirementSet)

@given(instance=reqSpec::ReqDocument_strategy)
@settings(max_examples=50)
def test_reqspec::reqdocument_instantiation(instance):
    assert isinstance(instance, reqSpec::ReqDocument)

@given(instance=reqSpec::StakeholderGoals_strategy)
@settings(max_examples=50)
def test_reqspec::stakeholdergoals_instantiation(instance):
    assert isinstance(instance, reqSpec::StakeholderGoals)

@given(instance=reqSpec::StakeholderGoals_strategy)
def test_reqspec::stakeholdergoals_componentCategory_type(instance):
    assert isinstance(instance.componentCategory, str)


@given(instance=reqSpec::StakeholderGoals_strategy)
def test_reqspec::stakeholdergoals_componentCategory_setter(instance):
    original = instance.componentCategory
    instance.componentCategory = original
    assert instance.componentCategory == original

@given(instance=reqSpec::ReqRoot_strategy)
@settings(max_examples=50)
def test_reqspec::reqroot_instantiation(instance):
    assert isinstance(instance, reqSpec::ReqRoot)

@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_issues_type(instance):
    assert isinstance(instance.issues, str)


@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_issues_setter(instance):
    original = instance.issues
    instance.issues = original
    assert instance.issues == original

@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=reqSpec::ReqRoot_strategy)
def test_reqspec::reqroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=reqSpec::Goal_strategy)
@settings(max_examples=50)
def test_reqspec::goal_instantiation(instance):
    assert isinstance(instance, reqSpec::Goal)

@given(instance=reqSpec::ExternalDocument_strategy)
@settings(max_examples=50)
def test_reqspec::externaldocument_instantiation(instance):
    assert isinstance(instance, reqSpec::ExternalDocument)

@given(instance=reqSpec::ExternalDocument_strategy)
def test_reqspec::externaldocument_docReference_type(instance):
    assert isinstance(instance.docReference, str)


@given(instance=reqSpec::ExternalDocument_strategy)
def test_reqspec::externaldocument_docReference_setter(instance):
    original = instance.docReference
    instance.docReference = original
    assert instance.docReference == original

@given(instance=reqSpec::ExternalDocument_strategy)
def test_reqspec::externaldocument_docFragment_type(instance):
    assert isinstance(instance.docFragment, str)


@given(instance=reqSpec::ExternalDocument_strategy)
def test_reqspec::externaldocument_docFragment_setter(instance):
    original = instance.docFragment
    instance.docFragment = original
    assert instance.docFragment == original

@given(instance=reqSpec::ContractualElement_strategy)
@settings(max_examples=50)
def test_reqspec::contractualelement_instantiation(instance):
    assert isinstance(instance, reqSpec::ContractualElement)

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_targetDescription_type(instance):
    assert isinstance(instance.targetDescription, str)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_targetDescription_setter(instance):
    original = instance.targetDescription
    instance.targetDescription = original
    assert instance.targetDescription == original

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_issues_type(instance):
    assert isinstance(instance.issues, str)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_issues_setter(instance):
    original = instance.issues
    instance.issues = original
    assert instance.issues == original

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_dropRationale_type(instance):
    assert isinstance(instance.dropRationale, str)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_dropRationale_setter(instance):
    original = instance.dropRationale
    instance.dropRationale = original
    assert instance.dropRationale == original

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_dropped_type(instance):
    assert isinstance(instance.dropped, bool)


@given(instance=reqSpec::ContractualElement_strategy)
def test_reqspec::contractualelement_dropped_setter(instance):
    original = instance.dropped
    instance.dropped = original
    assert instance.dropped == original

@given(instance=reqSpec::AVariableDeclaration_strategy)
@settings(max_examples=50)
def test_reqspec::avariabledeclaration_instantiation(instance):
    assert isinstance(instance, reqSpec::AVariableDeclaration)

@given(instance=reqSpec::Rationale_strategy)
@settings(max_examples=50)
def test_reqspec::rationale_instantiation(instance):
    assert isinstance(instance, reqSpec::Rationale)

@given(instance=reqSpec::WhenCondition_strategy)
@settings(max_examples=50)
def test_reqspec::whencondition_instantiation(instance):
    assert isinstance(instance, reqSpec::WhenCondition)

@given(instance=reqSpec::Description_strategy)
@settings(max_examples=50)
def test_reqspec::description_instantiation(instance):
    assert isinstance(instance, reqSpec::Description)

@given(instance=reqSpec::Category_strategy)
@settings(max_examples=50)
def test_reqspec::category_instantiation(instance):
    assert isinstance(instance, reqSpec::Category)

@given(instance=reqSpec::NamedElement_strategy)
@settings(max_examples=50)
def test_reqspec::namedelement_instantiation(instance):
    assert isinstance(instance, reqSpec::NamedElement)

@given(instance=reqSpec::ComponentClassifier_strategy)
@settings(max_examples=50)
def test_reqspec::componentclassifier_instantiation(instance):
    assert isinstance(instance, reqSpec::ComponentClassifier)

@given(instance=reqSpec::GlobalConstants_strategy)
@settings(max_examples=50)
def test_reqspec::globalconstants_instantiation(instance):
    assert isinstance(instance, reqSpec::GlobalConstants)

@given(instance=reqSpec::GlobalConstants_strategy)
def test_reqspec::globalconstants_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=reqSpec::GlobalConstants_strategy)
def test_reqspec::globalconstants_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reqSpec::EObject_strategy)
@settings(max_examples=50)
def test_reqspec::eobject_instantiation(instance):
    assert isinstance(instance, reqSpec::EObject)

@given(instance=reqSpec::ReqSpec_strategy)
@settings(max_examples=50)
def test_reqspec::reqspec_instantiation(instance):
    assert isinstance(instance, reqSpec::ReqSpec)
