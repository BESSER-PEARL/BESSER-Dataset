import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GlobalAspect,
    workflow::DocumentTypeContainer,
    workflow::Organisation,
    RuntimeGlobalAspect,
    workflow::DocumentContainer,
    workflow::AgentContainer,
    workflow::EnumLiteral,
    DocumentCondition,
    workflow::DefaultDocumentCondition,
    Operator,
    workflow::GreaterThanOperator,
    workflow::EqualToOperator,
    workflow::UnequalToOperator,
    workflow::LessThanOperator,
    workflow::DotOperator,
    Atom,
    workflow::FieldAtom,
    workflow::ConstantAtom,
    workflow::EnumFieldAtom,
    workflow::EnumLiteralAtom,
    workflow::DocumentDescrAtom,
    Expression,
    workflow::Operator,
    workflow::Atom,
    DocumentDescriptor,
    workflow::DefaultDocumentDescriptor,
    RuntimeModelAspect,
    workflow::InformationRuntimeAspect,
    workflow::EnumFieldValue,
    workflow::FieldValue,
    Document,
    workflow::DefaultDocument,
    workflow::EnumField,
    workflow::Field,
    DocumentType,
    workflow::DefaultDocumentType,
    workflow::Expression,
    workflow::RuntimeGlobalAspect,
    ModelAspect,
    workflow::ControlAspect,
    workflow::InformationAspect,
    workflow::OrganisationAspect,
    workflow::ModelAspect,
    workflow::RuntimeModelAspect,
    workflow::TaskAspect,
    workflow::ProcessAspect,
    State,
    workflow::Marking,
    workflow::String2DocumentMap,
    workflow::Document,
    workflow::DocumentType,
    workflow::DocumentCondition,
    workflow::DocumentDescriptor,
    workflow::ProcessDocument,
    workflow::GlobalAspect,
    workflow::CoreModel,
    workflow::WorkflowEngine,
    workflow::ModelRegistry,
    workflow::Token,
    TaskC,
    workflow::Transition,
    workflow::Place,
    workflow::Arc,
    Control,
    workflow::PetriNet,
    workflow::State,
    CaseAspect,
    workflow::CaseO,
    workflow::CaseI,
    ProcessAspect,
    workflow::Information,
    workflow::ProcessO,
    workflow::Control,
    workflow::CaseC,
    workflow::RuntimeInformation,
    workflow::Task,
    workflow::ActivityAspect,
    workflow::RuntimeCoreModel,
    workflow::Process,
    workflow::Activity,
    workflow::CaseAspect,
    workflow::Case,
    workflow::Agent,
    ActivityAspect,
    workflow::ActivityC,
    workflow::ActivityI,
    workflow::ActivityO,
    workflow::Role,
    TaskAspect,
    workflow::TaskC,
    workflow::TaskI,
    workflow::TaskO,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_globalaspect_is_not_abstract():
    assert not inspect.isabstract(GlobalAspect)


def test_globalaspect_constructor_exists():
    assert callable(GlobalAspect.__init__)


def test_globalaspect_constructor_args():
    sig = inspect.signature(GlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::documenttypecontainer_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentTypeContainer)


def test_workflow::documenttypecontainer_constructor_exists():
    assert callable(workflow::DocumentTypeContainer.__init__)


def test_workflow::documenttypecontainer_constructor_args():
    sig = inspect.signature(workflow::DocumentTypeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::documenttypecontainer_has_name():
    assert hasattr(workflow::DocumentTypeContainer, "name")
    descriptor = None
    for klass in workflow::DocumentTypeContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::organisation_is_not_abstract():
    assert not inspect.isabstract(workflow::Organisation)


def test_workflow::organisation_constructor_exists():
    assert callable(workflow::Organisation.__init__)


def test_workflow::organisation_constructor_args():
    sig = inspect.signature(workflow::Organisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::organisation_has_name():
    assert hasattr(workflow::Organisation, "name")
    descriptor = None
    for klass in workflow::Organisation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_runtimeglobalaspect_is_not_abstract():
    assert not inspect.isabstract(RuntimeGlobalAspect)


def test_runtimeglobalaspect_constructor_exists():
    assert callable(RuntimeGlobalAspect.__init__)


def test_runtimeglobalaspect_constructor_args():
    sig = inspect.signature(RuntimeGlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::documentcontainer_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentContainer)


def test_workflow::documentcontainer_constructor_exists():
    assert callable(workflow::DocumentContainer.__init__)


def test_workflow::documentcontainer_constructor_args():
    sig = inspect.signature(workflow::DocumentContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::documentcontainer_has_name():
    assert hasattr(workflow::DocumentContainer, "name")
    descriptor = None
    for klass in workflow::DocumentContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::agentcontainer_is_not_abstract():
    assert not inspect.isabstract(workflow::AgentContainer)


def test_workflow::agentcontainer_constructor_exists():
    assert callable(workflow::AgentContainer.__init__)


def test_workflow::agentcontainer_constructor_args():
    sig = inspect.signature(workflow::AgentContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::agentcontainer_has_name():
    assert hasattr(workflow::AgentContainer, "name")
    descriptor = None
    for klass in workflow::AgentContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::enumliteral_is_not_abstract():
    assert not inspect.isabstract(workflow::EnumLiteral)


def test_workflow::enumliteral_constructor_exists():
    assert callable(workflow::EnumLiteral.__init__)


def test_workflow::enumliteral_constructor_args():
    sig = inspect.signature(workflow::EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::enumliteral_has_name():
    assert hasattr(workflow::EnumLiteral, "name")
    descriptor = None
    for klass in workflow::EnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_documentcondition_is_not_abstract():
    assert not inspect.isabstract(DocumentCondition)


def test_documentcondition_constructor_exists():
    assert callable(DocumentCondition.__init__)


def test_documentcondition_constructor_args():
    sig = inspect.signature(DocumentCondition.__init__)
    params = list(sig.parameters.keys())



def test_workflow::defaultdocumentcondition_is_not_abstract():
    assert not inspect.isabstract(workflow::DefaultDocumentCondition)


def test_workflow::defaultdocumentcondition_constructor_exists():
    assert callable(workflow::DefaultDocumentCondition.__init__)


def test_workflow::defaultdocumentcondition_constructor_args():
    sig = inspect.signature(workflow::DefaultDocumentCondition.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::greaterthanoperator_is_not_abstract():
    assert not inspect.isabstract(workflow::GreaterThanOperator)


def test_workflow::greaterthanoperator_constructor_exists():
    assert callable(workflow::GreaterThanOperator.__init__)


def test_workflow::greaterthanoperator_constructor_args():
    sig = inspect.signature(workflow::GreaterThanOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::equaltooperator_is_not_abstract():
    assert not inspect.isabstract(workflow::EqualToOperator)


def test_workflow::equaltooperator_constructor_exists():
    assert callable(workflow::EqualToOperator.__init__)


def test_workflow::equaltooperator_constructor_args():
    sig = inspect.signature(workflow::EqualToOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::unequaltooperator_is_not_abstract():
    assert not inspect.isabstract(workflow::UnequalToOperator)


def test_workflow::unequaltooperator_constructor_exists():
    assert callable(workflow::UnequalToOperator.__init__)


def test_workflow::unequaltooperator_constructor_args():
    sig = inspect.signature(workflow::UnequalToOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::lessthanoperator_is_not_abstract():
    assert not inspect.isabstract(workflow::LessThanOperator)


def test_workflow::lessthanoperator_constructor_exists():
    assert callable(workflow::LessThanOperator.__init__)


def test_workflow::lessthanoperator_constructor_args():
    sig = inspect.signature(workflow::LessThanOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::dotoperator_is_not_abstract():
    assert not inspect.isabstract(workflow::DotOperator)


def test_workflow::dotoperator_constructor_exists():
    assert callable(workflow::DotOperator.__init__)


def test_workflow::dotoperator_constructor_args():
    sig = inspect.signature(workflow::DotOperator.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_workflow::fieldatom_is_not_abstract():
    assert not inspect.isabstract(workflow::FieldAtom)


def test_workflow::fieldatom_constructor_exists():
    assert callable(workflow::FieldAtom.__init__)


def test_workflow::fieldatom_constructor_args():
    sig = inspect.signature(workflow::FieldAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow::constantatom_is_not_abstract():
    assert not inspect.isabstract(workflow::ConstantAtom)


def test_workflow::constantatom_constructor_exists():
    assert callable(workflow::ConstantAtom.__init__)


def test_workflow::constantatom_constructor_args():
    sig = inspect.signature(workflow::ConstantAtom.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_workflow::constantatom_has_value():
    assert hasattr(workflow::ConstantAtom, "value")
    descriptor = None
    for klass in workflow::ConstantAtom.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_workflow::enumfieldatom_is_not_abstract():
    assert not inspect.isabstract(workflow::EnumFieldAtom)


def test_workflow::enumfieldatom_constructor_exists():
    assert callable(workflow::EnumFieldAtom.__init__)


def test_workflow::enumfieldatom_constructor_args():
    sig = inspect.signature(workflow::EnumFieldAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow::enumliteralatom_is_not_abstract():
    assert not inspect.isabstract(workflow::EnumLiteralAtom)


def test_workflow::enumliteralatom_constructor_exists():
    assert callable(workflow::EnumLiteralAtom.__init__)


def test_workflow::enumliteralatom_constructor_args():
    sig = inspect.signature(workflow::EnumLiteralAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow::documentdescratom_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentDescrAtom)


def test_workflow::documentdescratom_constructor_exists():
    assert callable(workflow::DocumentDescrAtom.__init__)


def test_workflow::documentdescratom_constructor_args():
    sig = inspect.signature(workflow::DocumentDescrAtom.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::operator_is_not_abstract():
    assert not inspect.isabstract(workflow::Operator)


def test_workflow::operator_constructor_exists():
    assert callable(workflow::Operator.__init__)


def test_workflow::operator_constructor_args():
    sig = inspect.signature(workflow::Operator.__init__)
    params = list(sig.parameters.keys())



def test_workflow::atom_is_not_abstract():
    assert not inspect.isabstract(workflow::Atom)


def test_workflow::atom_constructor_exists():
    assert callable(workflow::Atom.__init__)


def test_workflow::atom_constructor_args():
    sig = inspect.signature(workflow::Atom.__init__)
    params = list(sig.parameters.keys())



def test_documentdescriptor_is_not_abstract():
    assert not inspect.isabstract(DocumentDescriptor)


def test_documentdescriptor_constructor_exists():
    assert callable(DocumentDescriptor.__init__)


def test_documentdescriptor_constructor_args():
    sig = inspect.signature(DocumentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_workflow::defaultdocumentdescriptor_is_not_abstract():
    assert not inspect.isabstract(workflow::DefaultDocumentDescriptor)


def test_workflow::defaultdocumentdescriptor_constructor_exists():
    assert callable(workflow::DefaultDocumentDescriptor.__init__)


def test_workflow::defaultdocumentdescriptor_constructor_args():
    sig = inspect.signature(workflow::DefaultDocumentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_runtimemodelaspect_is_not_abstract():
    assert not inspect.isabstract(RuntimeModelAspect)


def test_runtimemodelaspect_constructor_exists():
    assert callable(RuntimeModelAspect.__init__)


def test_runtimemodelaspect_constructor_args():
    sig = inspect.signature(RuntimeModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::informationruntimeaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::InformationRuntimeAspect)


def test_workflow::informationruntimeaspect_constructor_exists():
    assert callable(workflow::InformationRuntimeAspect.__init__)


def test_workflow::informationruntimeaspect_constructor_args():
    sig = inspect.signature(workflow::InformationRuntimeAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::enumfieldvalue_is_not_abstract():
    assert not inspect.isabstract(workflow::EnumFieldValue)


def test_workflow::enumfieldvalue_constructor_exists():
    assert callable(workflow::EnumFieldValue.__init__)


def test_workflow::enumfieldvalue_constructor_args():
    sig = inspect.signature(workflow::EnumFieldValue.__init__)
    params = list(sig.parameters.keys())



def test_workflow::fieldvalue_is_not_abstract():
    assert not inspect.isabstract(workflow::FieldValue)


def test_workflow::fieldvalue_constructor_exists():
    assert callable(workflow::FieldValue.__init__)


def test_workflow::fieldvalue_constructor_args():
    sig = inspect.signature(workflow::FieldValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_workflow::fieldvalue_has_value():
    assert hasattr(workflow::FieldValue, "value")
    descriptor = None
    for klass in workflow::FieldValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_document_is_not_abstract():
    assert not inspect.isabstract(Document)


def test_document_constructor_exists():
    assert callable(Document.__init__)


def test_document_constructor_args():
    sig = inspect.signature(Document.__init__)
    params = list(sig.parameters.keys())



def test_workflow::defaultdocument_is_not_abstract():
    assert not inspect.isabstract(workflow::DefaultDocument)


def test_workflow::defaultdocument_constructor_exists():
    assert callable(workflow::DefaultDocument.__init__)


def test_workflow::defaultdocument_constructor_args():
    sig = inspect.signature(workflow::DefaultDocument.__init__)
    params = list(sig.parameters.keys())
    assert "placeholder" in params, "Missing parameter 'placeholder'"

def test_workflow::defaultdocument_has_placeholder():
    assert hasattr(workflow::DefaultDocument, "placeholder")
    descriptor = None
    for klass in workflow::DefaultDocument.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)



def test_workflow::enumfield_is_not_abstract():
    assert not inspect.isabstract(workflow::EnumField)


def test_workflow::enumfield_constructor_exists():
    assert callable(workflow::EnumField.__init__)


def test_workflow::enumfield_constructor_args():
    sig = inspect.signature(workflow::EnumField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::enumfield_has_name():
    assert hasattr(workflow::EnumField, "name")
    descriptor = None
    for klass in workflow::EnumField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::field_is_not_abstract():
    assert not inspect.isabstract(workflow::Field)


def test_workflow::field_constructor_exists():
    assert callable(workflow::Field.__init__)


def test_workflow::field_constructor_args():
    sig = inspect.signature(workflow::Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::field_has_name():
    assert hasattr(workflow::Field, "name")
    descriptor = None
    for klass in workflow::Field.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_documenttype_is_not_abstract():
    assert not inspect.isabstract(DocumentType)


def test_documenttype_constructor_exists():
    assert callable(DocumentType.__init__)


def test_documenttype_constructor_args():
    sig = inspect.signature(DocumentType.__init__)
    params = list(sig.parameters.keys())



def test_workflow::defaultdocumenttype_is_not_abstract():
    assert not inspect.isabstract(workflow::DefaultDocumentType)


def test_workflow::defaultdocumenttype_constructor_exists():
    assert callable(workflow::DefaultDocumentType.__init__)


def test_workflow::defaultdocumenttype_constructor_args():
    sig = inspect.signature(workflow::DefaultDocumentType.__init__)
    params = list(sig.parameters.keys())



def test_workflow::expression_is_not_abstract():
    assert not inspect.isabstract(workflow::Expression)


def test_workflow::expression_constructor_exists():
    assert callable(workflow::Expression.__init__)


def test_workflow::expression_constructor_args():
    sig = inspect.signature(workflow::Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::runtimeglobalaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::RuntimeGlobalAspect)


def test_workflow::runtimeglobalaspect_constructor_exists():
    assert callable(workflow::RuntimeGlobalAspect.__init__)


def test_workflow::runtimeglobalaspect_constructor_args():
    sig = inspect.signature(workflow::RuntimeGlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_modelaspect_is_not_abstract():
    assert not inspect.isabstract(ModelAspect)


def test_modelaspect_constructor_exists():
    assert callable(ModelAspect.__init__)


def test_modelaspect_constructor_args():
    sig = inspect.signature(ModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::controlaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::ControlAspect)


def test_workflow::controlaspect_constructor_exists():
    assert callable(workflow::ControlAspect.__init__)


def test_workflow::controlaspect_constructor_args():
    sig = inspect.signature(workflow::ControlAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::informationaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::InformationAspect)


def test_workflow::informationaspect_constructor_exists():
    assert callable(workflow::InformationAspect.__init__)


def test_workflow::informationaspect_constructor_args():
    sig = inspect.signature(workflow::InformationAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::organisationaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::OrganisationAspect)


def test_workflow::organisationaspect_constructor_exists():
    assert callable(workflow::OrganisationAspect.__init__)


def test_workflow::organisationaspect_constructor_args():
    sig = inspect.signature(workflow::OrganisationAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::modelaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::ModelAspect)


def test_workflow::modelaspect_constructor_exists():
    assert callable(workflow::ModelAspect.__init__)


def test_workflow::modelaspect_constructor_args():
    sig = inspect.signature(workflow::ModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::runtimemodelaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::RuntimeModelAspect)


def test_workflow::runtimemodelaspect_constructor_exists():
    assert callable(workflow::RuntimeModelAspect.__init__)


def test_workflow::runtimemodelaspect_constructor_args():
    sig = inspect.signature(workflow::RuntimeModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::taskaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::TaskAspect)


def test_workflow::taskaspect_constructor_exists():
    assert callable(workflow::TaskAspect.__init__)


def test_workflow::taskaspect_constructor_args():
    sig = inspect.signature(workflow::TaskAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::processaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcessAspect)


def test_workflow::processaspect_constructor_exists():
    assert callable(workflow::ProcessAspect.__init__)


def test_workflow::processaspect_constructor_args():
    sig = inspect.signature(workflow::ProcessAspect.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_workflow::marking_is_not_abstract():
    assert not inspect.isabstract(workflow::Marking)


def test_workflow::marking_constructor_exists():
    assert callable(workflow::Marking.__init__)


def test_workflow::marking_constructor_args():
    sig = inspect.signature(workflow::Marking.__init__)
    params = list(sig.parameters.keys())



def test_workflow::string2documentmap_is_not_abstract():
    assert not inspect.isabstract(workflow::String2DocumentMap)


def test_workflow::string2documentmap_constructor_exists():
    assert callable(workflow::String2DocumentMap.__init__)


def test_workflow::string2documentmap_constructor_args():
    sig = inspect.signature(workflow::String2DocumentMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_workflow::string2documentmap_has_key():
    assert hasattr(workflow::String2DocumentMap, "key")
    descriptor = None
    for klass in workflow::String2DocumentMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_workflow::document_is_not_abstract():
    assert not inspect.isabstract(workflow::Document)


def test_workflow::document_constructor_exists():
    assert callable(workflow::Document.__init__)


def test_workflow::document_constructor_args():
    sig = inspect.signature(workflow::Document.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::document_has_id():
    assert hasattr(workflow::Document, "id")
    descriptor = None
    for klass in workflow::Document.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_workflow::document_has_name():
    assert hasattr(workflow::Document, "name")
    descriptor = None
    for klass in workflow::Document.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::documenttype_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentType)


def test_workflow::documenttype_constructor_exists():
    assert callable(workflow::DocumentType.__init__)


def test_workflow::documenttype_constructor_args():
    sig = inspect.signature(workflow::DocumentType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::documenttype_has_name():
    assert hasattr(workflow::DocumentType, "name")
    descriptor = None
    for klass in workflow::DocumentType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::documentcondition_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentCondition)


def test_workflow::documentcondition_constructor_exists():
    assert callable(workflow::DocumentCondition.__init__)


def test_workflow::documentcondition_constructor_args():
    sig = inspect.signature(workflow::DocumentCondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::documentcondition_has_name():
    assert hasattr(workflow::DocumentCondition, "name")
    descriptor = None
    for klass in workflow::DocumentCondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::documentdescriptor_is_not_abstract():
    assert not inspect.isabstract(workflow::DocumentDescriptor)


def test_workflow::documentdescriptor_constructor_exists():
    assert callable(workflow::DocumentDescriptor.__init__)


def test_workflow::documentdescriptor_constructor_args():
    sig = inspect.signature(workflow::DocumentDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::documentdescriptor_has_name():
    assert hasattr(workflow::DocumentDescriptor, "name")
    descriptor = None
    for klass in workflow::DocumentDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::processdocument_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcessDocument)


def test_workflow::processdocument_constructor_exists():
    assert callable(workflow::ProcessDocument.__init__)


def test_workflow::processdocument_constructor_args():
    sig = inspect.signature(workflow::ProcessDocument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::processdocument_has_name():
    assert hasattr(workflow::ProcessDocument, "name")
    descriptor = None
    for klass in workflow::ProcessDocument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::globalaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::GlobalAspect)


def test_workflow::globalaspect_constructor_exists():
    assert callable(workflow::GlobalAspect.__init__)


def test_workflow::globalaspect_constructor_args():
    sig = inspect.signature(workflow::GlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::coremodel_is_not_abstract():
    assert not inspect.isabstract(workflow::CoreModel)


def test_workflow::coremodel_constructor_exists():
    assert callable(workflow::CoreModel.__init__)


def test_workflow::coremodel_constructor_args():
    sig = inspect.signature(workflow::CoreModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::coremodel_has_name():
    assert hasattr(workflow::CoreModel, "name")
    descriptor = None
    for klass in workflow::CoreModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::workflowengine_is_not_abstract():
    assert not inspect.isabstract(workflow::WorkflowEngine)


def test_workflow::workflowengine_constructor_exists():
    assert callable(workflow::WorkflowEngine.__init__)


def test_workflow::workflowengine_constructor_args():
    sig = inspect.signature(workflow::WorkflowEngine.__init__)
    params = list(sig.parameters.keys())



def test_workflow::modelregistry_is_not_abstract():
    assert not inspect.isabstract(workflow::ModelRegistry)


def test_workflow::modelregistry_constructor_exists():
    assert callable(workflow::ModelRegistry.__init__)


def test_workflow::modelregistry_constructor_args():
    sig = inspect.signature(workflow::ModelRegistry.__init__)
    params = list(sig.parameters.keys())



def test_workflow::token_is_not_abstract():
    assert not inspect.isabstract(workflow::Token)


def test_workflow::token_constructor_exists():
    assert callable(workflow::Token.__init__)


def test_workflow::token_constructor_args():
    sig = inspect.signature(workflow::Token.__init__)
    params = list(sig.parameters.keys())



def test_taskc_is_not_abstract():
    assert not inspect.isabstract(TaskC)


def test_taskc_constructor_exists():
    assert callable(TaskC.__init__)


def test_taskc_constructor_args():
    sig = inspect.signature(TaskC.__init__)
    params = list(sig.parameters.keys())



def test_workflow::transition_is_not_abstract():
    assert not inspect.isabstract(workflow::Transition)


def test_workflow::transition_constructor_exists():
    assert callable(workflow::Transition.__init__)


def test_workflow::transition_constructor_args():
    sig = inspect.signature(workflow::Transition.__init__)
    params = list(sig.parameters.keys())



def test_workflow::place_is_not_abstract():
    assert not inspect.isabstract(workflow::Place)


def test_workflow::place_constructor_exists():
    assert callable(workflow::Place.__init__)


def test_workflow::place_constructor_args():
    sig = inspect.signature(workflow::Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::place_has_name():
    assert hasattr(workflow::Place, "name")
    descriptor = None
    for klass in workflow::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::arc_is_not_abstract():
    assert not inspect.isabstract(workflow::Arc)


def test_workflow::arc_constructor_exists():
    assert callable(workflow::Arc.__init__)


def test_workflow::arc_constructor_args():
    sig = inspect.signature(workflow::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::arc_has_name():
    assert hasattr(workflow::Arc, "name")
    descriptor = None
    for klass in workflow::Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_control_is_not_abstract():
    assert not inspect.isabstract(Control)


def test_control_constructor_exists():
    assert callable(Control.__init__)


def test_control_constructor_args():
    sig = inspect.signature(Control.__init__)
    params = list(sig.parameters.keys())



def test_workflow::petrinet_is_not_abstract():
    assert not inspect.isabstract(workflow::PetriNet)


def test_workflow::petrinet_constructor_exists():
    assert callable(workflow::PetriNet.__init__)


def test_workflow::petrinet_constructor_args():
    sig = inspect.signature(workflow::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_workflow::state_is_not_abstract():
    assert not inspect.isabstract(workflow::State)


def test_workflow::state_constructor_exists():
    assert callable(workflow::State.__init__)


def test_workflow::state_constructor_args():
    sig = inspect.signature(workflow::State.__init__)
    params = list(sig.parameters.keys())



def test_caseaspect_is_not_abstract():
    assert not inspect.isabstract(CaseAspect)


def test_caseaspect_constructor_exists():
    assert callable(CaseAspect.__init__)


def test_caseaspect_constructor_args():
    sig = inspect.signature(CaseAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::caseo_is_not_abstract():
    assert not inspect.isabstract(workflow::CaseO)


def test_workflow::caseo_constructor_exists():
    assert callable(workflow::CaseO.__init__)


def test_workflow::caseo_constructor_args():
    sig = inspect.signature(workflow::CaseO.__init__)
    params = list(sig.parameters.keys())



def test_workflow::casei_is_not_abstract():
    assert not inspect.isabstract(workflow::CaseI)


def test_workflow::casei_constructor_exists():
    assert callable(workflow::CaseI.__init__)


def test_workflow::casei_constructor_args():
    sig = inspect.signature(workflow::CaseI.__init__)
    params = list(sig.parameters.keys())



def test_processaspect_is_not_abstract():
    assert not inspect.isabstract(ProcessAspect)


def test_processaspect_constructor_exists():
    assert callable(ProcessAspect.__init__)


def test_processaspect_constructor_args():
    sig = inspect.signature(ProcessAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::information_is_not_abstract():
    assert not inspect.isabstract(workflow::Information)


def test_workflow::information_constructor_exists():
    assert callable(workflow::Information.__init__)


def test_workflow::information_constructor_args():
    sig = inspect.signature(workflow::Information.__init__)
    params = list(sig.parameters.keys())



def test_workflow::processo_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcessO)


def test_workflow::processo_constructor_exists():
    assert callable(workflow::ProcessO.__init__)


def test_workflow::processo_constructor_args():
    sig = inspect.signature(workflow::ProcessO.__init__)
    params = list(sig.parameters.keys())



def test_workflow::control_is_not_abstract():
    assert not inspect.isabstract(workflow::Control)


def test_workflow::control_constructor_exists():
    assert callable(workflow::Control.__init__)


def test_workflow::control_constructor_args():
    sig = inspect.signature(workflow::Control.__init__)
    params = list(sig.parameters.keys())



def test_workflow::casec_is_not_abstract():
    assert not inspect.isabstract(workflow::CaseC)


def test_workflow::casec_constructor_exists():
    assert callable(workflow::CaseC.__init__)


def test_workflow::casec_constructor_args():
    sig = inspect.signature(workflow::CaseC.__init__)
    params = list(sig.parameters.keys())



def test_workflow::runtimeinformation_is_not_abstract():
    assert not inspect.isabstract(workflow::RuntimeInformation)


def test_workflow::runtimeinformation_constructor_exists():
    assert callable(workflow::RuntimeInformation.__init__)


def test_workflow::runtimeinformation_constructor_args():
    sig = inspect.signature(workflow::RuntimeInformation.__init__)
    params = list(sig.parameters.keys())
    assert "caseIdCount" in params, "Missing parameter 'caseIdCount'"

def test_workflow::runtimeinformation_has_caseIdCount():
    assert hasattr(workflow::RuntimeInformation, "caseIdCount")
    descriptor = None
    for klass in workflow::RuntimeInformation.__mro__:
        if "caseIdCount" in klass.__dict__:
            descriptor = klass.__dict__["caseIdCount"]
            break
    assert isinstance(descriptor, property)



def test_workflow::task_is_not_abstract():
    assert not inspect.isabstract(workflow::Task)


def test_workflow::task_constructor_exists():
    assert callable(workflow::Task.__init__)


def test_workflow::task_constructor_args():
    sig = inspect.signature(workflow::Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::task_has_name():
    assert hasattr(workflow::Task, "name")
    descriptor = None
    for klass in workflow::Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::activityaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::ActivityAspect)


def test_workflow::activityaspect_constructor_exists():
    assert callable(workflow::ActivityAspect.__init__)


def test_workflow::activityaspect_constructor_args():
    sig = inspect.signature(workflow::ActivityAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::runtimecoremodel_is_not_abstract():
    assert not inspect.isabstract(workflow::RuntimeCoreModel)


def test_workflow::runtimecoremodel_constructor_exists():
    assert callable(workflow::RuntimeCoreModel.__init__)


def test_workflow::runtimecoremodel_constructor_args():
    sig = inspect.signature(workflow::RuntimeCoreModel.__init__)
    params = list(sig.parameters.keys())



def test_workflow::process_is_not_abstract():
    assert not inspect.isabstract(workflow::Process)


def test_workflow::process_constructor_exists():
    assert callable(workflow::Process.__init__)


def test_workflow::process_constructor_args():
    sig = inspect.signature(workflow::Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::process_has_name():
    assert hasattr(workflow::Process, "name")
    descriptor = None
    for klass in workflow::Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::activity_is_not_abstract():
    assert not inspect.isabstract(workflow::Activity)


def test_workflow::activity_constructor_exists():
    assert callable(workflow::Activity.__init__)


def test_workflow::activity_constructor_args():
    sig = inspect.signature(workflow::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "started" in params, "Missing parameter 'started'"
    assert "finished" in params, "Missing parameter 'finished'"

def test_workflow::activity_has_started():
    assert hasattr(workflow::Activity, "started")
    descriptor = None
    for klass in workflow::Activity.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)

def test_workflow::activity_has_finished():
    assert hasattr(workflow::Activity, "finished")
    descriptor = None
    for klass in workflow::Activity.__mro__:
        if "finished" in klass.__dict__:
            descriptor = klass.__dict__["finished"]
            break
    assert isinstance(descriptor, property)



def test_workflow::caseaspect_is_not_abstract():
    assert not inspect.isabstract(workflow::CaseAspect)


def test_workflow::caseaspect_constructor_exists():
    assert callable(workflow::CaseAspect.__init__)


def test_workflow::caseaspect_constructor_args():
    sig = inspect.signature(workflow::CaseAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::case_is_not_abstract():
    assert not inspect.isabstract(workflow::Case)


def test_workflow::case_constructor_exists():
    assert callable(workflow::Case.__init__)


def test_workflow::case_constructor_args():
    sig = inspect.signature(workflow::Case.__init__)
    params = list(sig.parameters.keys())
    assert "started" in params, "Missing parameter 'started'"
    assert "client" in params, "Missing parameter 'client'"
    assert "finished" in params, "Missing parameter 'finished'"
    assert "id" in params, "Missing parameter 'id'"

def test_workflow::case_has_started():
    assert hasattr(workflow::Case, "started")
    descriptor = None
    for klass in workflow::Case.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)

def test_workflow::case_has_client():
    assert hasattr(workflow::Case, "client")
    descriptor = None
    for klass in workflow::Case.__mro__:
        if "client" in klass.__dict__:
            descriptor = klass.__dict__["client"]
            break
    assert isinstance(descriptor, property)

def test_workflow::case_has_finished():
    assert hasattr(workflow::Case, "finished")
    descriptor = None
    for klass in workflow::Case.__mro__:
        if "finished" in klass.__dict__:
            descriptor = klass.__dict__["finished"]
            break
    assert isinstance(descriptor, property)

def test_workflow::case_has_id():
    assert hasattr(workflow::Case, "id")
    descriptor = None
    for klass in workflow::Case.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_workflow::agent_is_not_abstract():
    assert not inspect.isabstract(workflow::Agent)


def test_workflow::agent_constructor_exists():
    assert callable(workflow::Agent.__init__)


def test_workflow::agent_constructor_args():
    sig = inspect.signature(workflow::Agent.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::agent_has_username():
    assert hasattr(workflow::Agent, "username")
    descriptor = None
    for klass in workflow::Agent.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_workflow::agent_has_password():
    assert hasattr(workflow::Agent, "password")
    descriptor = None
    for klass in workflow::Agent.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_workflow::agent_has_name():
    assert hasattr(workflow::Agent, "name")
    descriptor = None
    for klass in workflow::Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activityaspect_is_not_abstract():
    assert not inspect.isabstract(ActivityAspect)


def test_activityaspect_constructor_exists():
    assert callable(ActivityAspect.__init__)


def test_activityaspect_constructor_args():
    sig = inspect.signature(ActivityAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::activityc_is_not_abstract():
    assert not inspect.isabstract(workflow::ActivityC)


def test_workflow::activityc_constructor_exists():
    assert callable(workflow::ActivityC.__init__)


def test_workflow::activityc_constructor_args():
    sig = inspect.signature(workflow::ActivityC.__init__)
    params = list(sig.parameters.keys())



def test_workflow::activityi_is_not_abstract():
    assert not inspect.isabstract(workflow::ActivityI)


def test_workflow::activityi_constructor_exists():
    assert callable(workflow::ActivityI.__init__)


def test_workflow::activityi_constructor_args():
    sig = inspect.signature(workflow::ActivityI.__init__)
    params = list(sig.parameters.keys())



def test_workflow::activityo_is_not_abstract():
    assert not inspect.isabstract(workflow::ActivityO)


def test_workflow::activityo_constructor_exists():
    assert callable(workflow::ActivityO.__init__)


def test_workflow::activityo_constructor_args():
    sig = inspect.signature(workflow::ActivityO.__init__)
    params = list(sig.parameters.keys())



def test_workflow::role_is_not_abstract():
    assert not inspect.isabstract(workflow::Role)


def test_workflow::role_constructor_exists():
    assert callable(workflow::Role.__init__)


def test_workflow::role_constructor_args():
    sig = inspect.signature(workflow::Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::role_has_name():
    assert hasattr(workflow::Role, "name")
    descriptor = None
    for klass in workflow::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_taskaspect_is_not_abstract():
    assert not inspect.isabstract(TaskAspect)


def test_taskaspect_constructor_exists():
    assert callable(TaskAspect.__init__)


def test_taskaspect_constructor_args():
    sig = inspect.signature(TaskAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow::taskc_is_not_abstract():
    assert not inspect.isabstract(workflow::TaskC)


def test_workflow::taskc_constructor_exists():
    assert callable(workflow::TaskC.__init__)


def test_workflow::taskc_constructor_args():
    sig = inspect.signature(workflow::TaskC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::taskc_has_name():
    assert hasattr(workflow::TaskC, "name")
    descriptor = None
    for klass in workflow::TaskC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::taski_is_not_abstract():
    assert not inspect.isabstract(workflow::TaskI)


def test_workflow::taski_constructor_exists():
    assert callable(workflow::TaskI.__init__)


def test_workflow::taski_constructor_args():
    sig = inspect.signature(workflow::TaskI.__init__)
    params = list(sig.parameters.keys())



def test_workflow::tasko_is_not_abstract():
    assert not inspect.isabstract(workflow::TaskO)


def test_workflow::tasko_constructor_exists():
    assert callable(workflow::TaskO.__init__)


def test_workflow::tasko_constructor_args():
    sig = inspect.signature(workflow::TaskO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::tasko_has_name():
    assert hasattr(workflow::TaskO, "name")
    descriptor = None
    for klass in workflow::TaskO.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
GlobalAspect_strategy = st.builds(
    GlobalAspect,
)
workflow::DocumentTypeContainer_strategy = st.builds(
    workflow::DocumentTypeContainer,
    name=
        safe_text
)
workflow::Organisation_strategy = st.builds(
    workflow::Organisation,
    name=
        safe_text
)
RuntimeGlobalAspect_strategy = st.builds(
    RuntimeGlobalAspect,
)
workflow::DocumentContainer_strategy = st.builds(
    workflow::DocumentContainer,
    name=
        safe_text
)
workflow::AgentContainer_strategy = st.builds(
    workflow::AgentContainer,
    name=
        safe_text
)
workflow::EnumLiteral_strategy = st.builds(
    workflow::EnumLiteral,
    name=
        safe_text
)
DocumentCondition_strategy = st.builds(
    DocumentCondition,
)
workflow::DefaultDocumentCondition_strategy = st.builds(
    workflow::DefaultDocumentCondition,
)
Operator_strategy = st.builds(
    Operator,
)
workflow::GreaterThanOperator_strategy = st.builds(
    workflow::GreaterThanOperator,
)
workflow::EqualToOperator_strategy = st.builds(
    workflow::EqualToOperator,
)
workflow::UnequalToOperator_strategy = st.builds(
    workflow::UnequalToOperator,
)
workflow::LessThanOperator_strategy = st.builds(
    workflow::LessThanOperator,
)
workflow::DotOperator_strategy = st.builds(
    workflow::DotOperator,
)
Atom_strategy = st.builds(
    Atom,
)
workflow::FieldAtom_strategy = st.builds(
    workflow::FieldAtom,
)
workflow::ConstantAtom_strategy = st.builds(
    workflow::ConstantAtom,
    value=
        safe_text
)
workflow::EnumFieldAtom_strategy = st.builds(
    workflow::EnumFieldAtom,
)
workflow::EnumLiteralAtom_strategy = st.builds(
    workflow::EnumLiteralAtom,
)
workflow::DocumentDescrAtom_strategy = st.builds(
    workflow::DocumentDescrAtom,
)
Expression_strategy = st.builds(
    Expression,
)
workflow::Operator_strategy = st.builds(
    workflow::Operator,
)
workflow::Atom_strategy = st.builds(
    workflow::Atom,
)
DocumentDescriptor_strategy = st.builds(
    DocumentDescriptor,
)
workflow::DefaultDocumentDescriptor_strategy = st.builds(
    workflow::DefaultDocumentDescriptor,
)
RuntimeModelAspect_strategy = st.builds(
    RuntimeModelAspect,
)
workflow::InformationRuntimeAspect_strategy = st.builds(
    workflow::InformationRuntimeAspect,
)
workflow::EnumFieldValue_strategy = st.builds(
    workflow::EnumFieldValue,
)
workflow::FieldValue_strategy = st.builds(
    workflow::FieldValue,
    value=
        safe_text
)
Document_strategy = st.builds(
    Document,
)
workflow::DefaultDocument_strategy = st.builds(
    workflow::DefaultDocument,
    placeholder=
        st.booleans()
)
workflow::EnumField_strategy = st.builds(
    workflow::EnumField,
    name=
        safe_text
)
workflow::Field_strategy = st.builds(
    workflow::Field,
    name=
        safe_text
)
DocumentType_strategy = st.builds(
    DocumentType,
)
workflow::DefaultDocumentType_strategy = st.builds(
    workflow::DefaultDocumentType,
)
workflow::Expression_strategy = st.builds(
    workflow::Expression,
)
workflow::RuntimeGlobalAspect_strategy = st.builds(
    workflow::RuntimeGlobalAspect,
)
ModelAspect_strategy = st.builds(
    ModelAspect,
)
workflow::ControlAspect_strategy = st.builds(
    workflow::ControlAspect,
)
workflow::InformationAspect_strategy = st.builds(
    workflow::InformationAspect,
)
workflow::OrganisationAspect_strategy = st.builds(
    workflow::OrganisationAspect,
)
workflow::ModelAspect_strategy = st.builds(
    workflow::ModelAspect,
)
workflow::RuntimeModelAspect_strategy = st.builds(
    workflow::RuntimeModelAspect,
)
workflow::TaskAspect_strategy = st.builds(
    workflow::TaskAspect,
)
workflow::ProcessAspect_strategy = st.builds(
    workflow::ProcessAspect,
)
State_strategy = st.builds(
    State,
)
workflow::Marking_strategy = st.builds(
    workflow::Marking,
)
workflow::String2DocumentMap_strategy = st.builds(
    workflow::String2DocumentMap,
    key=
        safe_text
)
workflow::Document_strategy = st.builds(
    workflow::Document,
    id=
        safe_text,
    name=
        safe_text
)
workflow::DocumentType_strategy = st.builds(
    workflow::DocumentType,
    name=
        safe_text
)
workflow::DocumentCondition_strategy = st.builds(
    workflow::DocumentCondition,
    name=
        safe_text
)
workflow::DocumentDescriptor_strategy = st.builds(
    workflow::DocumentDescriptor,
    name=
        safe_text
)
workflow::ProcessDocument_strategy = st.builds(
    workflow::ProcessDocument,
    name=
        safe_text
)
workflow::GlobalAspect_strategy = st.builds(
    workflow::GlobalAspect,
)
workflow::CoreModel_strategy = st.builds(
    workflow::CoreModel,
    name=
        safe_text
)
workflow::WorkflowEngine_strategy = st.builds(
    workflow::WorkflowEngine,
)
workflow::ModelRegistry_strategy = st.builds(
    workflow::ModelRegistry,
)
workflow::Token_strategy = st.builds(
    workflow::Token,
)
TaskC_strategy = st.builds(
    TaskC,
)
workflow::Transition_strategy = st.builds(
    workflow::Transition,
)
workflow::Place_strategy = st.builds(
    workflow::Place,
    name=
        safe_text
)
workflow::Arc_strategy = st.builds(
    workflow::Arc,
    name=
        safe_text
)
Control_strategy = st.builds(
    Control,
)
workflow::PetriNet_strategy = st.builds(
    workflow::PetriNet,
)
workflow::State_strategy = st.builds(
    workflow::State,
)
CaseAspect_strategy = st.builds(
    CaseAspect,
)
workflow::CaseO_strategy = st.builds(
    workflow::CaseO,
)
workflow::CaseI_strategy = st.builds(
    workflow::CaseI,
)
ProcessAspect_strategy = st.builds(
    ProcessAspect,
)
workflow::Information_strategy = st.builds(
    workflow::Information,
)
workflow::ProcessO_strategy = st.builds(
    workflow::ProcessO,
)
workflow::Control_strategy = st.builds(
    workflow::Control,
)
workflow::CaseC_strategy = st.builds(
    workflow::CaseC,
)
workflow::RuntimeInformation_strategy = st.builds(
    workflow::RuntimeInformation,
    caseIdCount=
        safe_text
)
workflow::Task_strategy = st.builds(
    workflow::Task,
    name=
        safe_text
)
workflow::ActivityAspect_strategy = st.builds(
    workflow::ActivityAspect,
)
workflow::RuntimeCoreModel_strategy = st.builds(
    workflow::RuntimeCoreModel,
)
workflow::Process_strategy = st.builds(
    workflow::Process,
    name=
        safe_text
)
workflow::Activity_strategy = st.builds(
    workflow::Activity,
    started=
        st.booleans(),
    finished=
        st.booleans()
)
workflow::CaseAspect_strategy = st.builds(
    workflow::CaseAspect,
)
workflow::Case_strategy = st.builds(
    workflow::Case,
    started=
        st.booleans(),
    client=
        safe_text,
    finished=
        st.booleans(),
    id=
        safe_text
)
workflow::Agent_strategy = st.builds(
    workflow::Agent,
    username=
        safe_text,
    password=
        safe_text,
    name=
        safe_text
)
ActivityAspect_strategy = st.builds(
    ActivityAspect,
)
workflow::ActivityC_strategy = st.builds(
    workflow::ActivityC,
)
workflow::ActivityI_strategy = st.builds(
    workflow::ActivityI,
)
workflow::ActivityO_strategy = st.builds(
    workflow::ActivityO,
)
workflow::Role_strategy = st.builds(
    workflow::Role,
    name=
        safe_text
)
TaskAspect_strategy = st.builds(
    TaskAspect,
)
workflow::TaskC_strategy = st.builds(
    workflow::TaskC,
    name=
        safe_text
)
workflow::TaskI_strategy = st.builds(
    workflow::TaskI,
)
workflow::TaskO_strategy = st.builds(
    workflow::TaskO,
    name=
        safe_text
)

@given(instance=GlobalAspect_strategy)
@settings(max_examples=50)
def test_globalaspect_instantiation(instance):
    assert isinstance(instance, GlobalAspect)

@given(instance=workflow::DocumentTypeContainer_strategy)
@settings(max_examples=50)
def test_workflow::documenttypecontainer_instantiation(instance):
    assert isinstance(instance, workflow::DocumentTypeContainer)

@given(instance=workflow::DocumentTypeContainer_strategy)
def test_workflow::documenttypecontainer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::DocumentTypeContainer_strategy)
def test_workflow::documenttypecontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Organisation_strategy)
@settings(max_examples=50)
def test_workflow::organisation_instantiation(instance):
    assert isinstance(instance, workflow::Organisation)

@given(instance=workflow::Organisation_strategy)
def test_workflow::organisation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Organisation_strategy)
def test_workflow::organisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RuntimeGlobalAspect_strategy)
@settings(max_examples=50)
def test_runtimeglobalaspect_instantiation(instance):
    assert isinstance(instance, RuntimeGlobalAspect)

@given(instance=workflow::DocumentContainer_strategy)
@settings(max_examples=50)
def test_workflow::documentcontainer_instantiation(instance):
    assert isinstance(instance, workflow::DocumentContainer)

@given(instance=workflow::DocumentContainer_strategy)
def test_workflow::documentcontainer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::DocumentContainer_strategy)
def test_workflow::documentcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::AgentContainer_strategy)
@settings(max_examples=50)
def test_workflow::agentcontainer_instantiation(instance):
    assert isinstance(instance, workflow::AgentContainer)

@given(instance=workflow::AgentContainer_strategy)
def test_workflow::agentcontainer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::AgentContainer_strategy)
def test_workflow::agentcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::EnumLiteral_strategy)
@settings(max_examples=50)
def test_workflow::enumliteral_instantiation(instance):
    assert isinstance(instance, workflow::EnumLiteral)

@given(instance=workflow::EnumLiteral_strategy)
def test_workflow::enumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::EnumLiteral_strategy)
def test_workflow::enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DocumentCondition_strategy)
@settings(max_examples=50)
def test_documentcondition_instantiation(instance):
    assert isinstance(instance, DocumentCondition)

@given(instance=workflow::DefaultDocumentCondition_strategy)
@settings(max_examples=50)
def test_workflow::defaultdocumentcondition_instantiation(instance):
    assert isinstance(instance, workflow::DefaultDocumentCondition)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=workflow::GreaterThanOperator_strategy)
@settings(max_examples=50)
def test_workflow::greaterthanoperator_instantiation(instance):
    assert isinstance(instance, workflow::GreaterThanOperator)

@given(instance=workflow::EqualToOperator_strategy)
@settings(max_examples=50)
def test_workflow::equaltooperator_instantiation(instance):
    assert isinstance(instance, workflow::EqualToOperator)

@given(instance=workflow::UnequalToOperator_strategy)
@settings(max_examples=50)
def test_workflow::unequaltooperator_instantiation(instance):
    assert isinstance(instance, workflow::UnequalToOperator)

@given(instance=workflow::LessThanOperator_strategy)
@settings(max_examples=50)
def test_workflow::lessthanoperator_instantiation(instance):
    assert isinstance(instance, workflow::LessThanOperator)

@given(instance=workflow::DotOperator_strategy)
@settings(max_examples=50)
def test_workflow::dotoperator_instantiation(instance):
    assert isinstance(instance, workflow::DotOperator)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=workflow::FieldAtom_strategy)
@settings(max_examples=50)
def test_workflow::fieldatom_instantiation(instance):
    assert isinstance(instance, workflow::FieldAtom)

@given(instance=workflow::ConstantAtom_strategy)
@settings(max_examples=50)
def test_workflow::constantatom_instantiation(instance):
    assert isinstance(instance, workflow::ConstantAtom)

@given(instance=workflow::ConstantAtom_strategy)
def test_workflow::constantatom_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=workflow::ConstantAtom_strategy)
def test_workflow::constantatom_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=workflow::EnumFieldAtom_strategy)
@settings(max_examples=50)
def test_workflow::enumfieldatom_instantiation(instance):
    assert isinstance(instance, workflow::EnumFieldAtom)

@given(instance=workflow::EnumLiteralAtom_strategy)
@settings(max_examples=50)
def test_workflow::enumliteralatom_instantiation(instance):
    assert isinstance(instance, workflow::EnumLiteralAtom)

@given(instance=workflow::DocumentDescrAtom_strategy)
@settings(max_examples=50)
def test_workflow::documentdescratom_instantiation(instance):
    assert isinstance(instance, workflow::DocumentDescrAtom)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=workflow::Operator_strategy)
@settings(max_examples=50)
def test_workflow::operator_instantiation(instance):
    assert isinstance(instance, workflow::Operator)

@given(instance=workflow::Atom_strategy)
@settings(max_examples=50)
def test_workflow::atom_instantiation(instance):
    assert isinstance(instance, workflow::Atom)

@given(instance=DocumentDescriptor_strategy)
@settings(max_examples=50)
def test_documentdescriptor_instantiation(instance):
    assert isinstance(instance, DocumentDescriptor)

@given(instance=workflow::DefaultDocumentDescriptor_strategy)
@settings(max_examples=50)
def test_workflow::defaultdocumentdescriptor_instantiation(instance):
    assert isinstance(instance, workflow::DefaultDocumentDescriptor)

@given(instance=RuntimeModelAspect_strategy)
@settings(max_examples=50)
def test_runtimemodelaspect_instantiation(instance):
    assert isinstance(instance, RuntimeModelAspect)

@given(instance=workflow::InformationRuntimeAspect_strategy)
@settings(max_examples=50)
def test_workflow::informationruntimeaspect_instantiation(instance):
    assert isinstance(instance, workflow::InformationRuntimeAspect)

@given(instance=workflow::EnumFieldValue_strategy)
@settings(max_examples=50)
def test_workflow::enumfieldvalue_instantiation(instance):
    assert isinstance(instance, workflow::EnumFieldValue)

@given(instance=workflow::FieldValue_strategy)
@settings(max_examples=50)
def test_workflow::fieldvalue_instantiation(instance):
    assert isinstance(instance, workflow::FieldValue)

@given(instance=workflow::FieldValue_strategy)
def test_workflow::fieldvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=workflow::FieldValue_strategy)
def test_workflow::fieldvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=workflow::DefaultDocument_strategy)
@settings(max_examples=50)
def test_workflow::defaultdocument_instantiation(instance):
    assert isinstance(instance, workflow::DefaultDocument)

@given(instance=workflow::DefaultDocument_strategy)
def test_workflow::defaultdocument_placeholder_type(instance):
    assert isinstance(instance.placeholder, bool)


@given(instance=workflow::DefaultDocument_strategy)
def test_workflow::defaultdocument_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=workflow::EnumField_strategy)
@settings(max_examples=50)
def test_workflow::enumfield_instantiation(instance):
    assert isinstance(instance, workflow::EnumField)

@given(instance=workflow::EnumField_strategy)
def test_workflow::enumfield_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::EnumField_strategy)
def test_workflow::enumfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Field_strategy)
@settings(max_examples=50)
def test_workflow::field_instantiation(instance):
    assert isinstance(instance, workflow::Field)

@given(instance=workflow::Field_strategy)
def test_workflow::field_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Field_strategy)
def test_workflow::field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DocumentType_strategy)
@settings(max_examples=50)
def test_documenttype_instantiation(instance):
    assert isinstance(instance, DocumentType)

@given(instance=workflow::DefaultDocumentType_strategy)
@settings(max_examples=50)
def test_workflow::defaultdocumenttype_instantiation(instance):
    assert isinstance(instance, workflow::DefaultDocumentType)

@given(instance=workflow::Expression_strategy)
@settings(max_examples=50)
def test_workflow::expression_instantiation(instance):
    assert isinstance(instance, workflow::Expression)

@given(instance=workflow::RuntimeGlobalAspect_strategy)
@settings(max_examples=50)
def test_workflow::runtimeglobalaspect_instantiation(instance):
    assert isinstance(instance, workflow::RuntimeGlobalAspect)

@given(instance=ModelAspect_strategy)
@settings(max_examples=50)
def test_modelaspect_instantiation(instance):
    assert isinstance(instance, ModelAspect)

@given(instance=workflow::ControlAspect_strategy)
@settings(max_examples=50)
def test_workflow::controlaspect_instantiation(instance):
    assert isinstance(instance, workflow::ControlAspect)

@given(instance=workflow::InformationAspect_strategy)
@settings(max_examples=50)
def test_workflow::informationaspect_instantiation(instance):
    assert isinstance(instance, workflow::InformationAspect)

@given(instance=workflow::OrganisationAspect_strategy)
@settings(max_examples=50)
def test_workflow::organisationaspect_instantiation(instance):
    assert isinstance(instance, workflow::OrganisationAspect)

@given(instance=workflow::ModelAspect_strategy)
@settings(max_examples=50)
def test_workflow::modelaspect_instantiation(instance):
    assert isinstance(instance, workflow::ModelAspect)

@given(instance=workflow::RuntimeModelAspect_strategy)
@settings(max_examples=50)
def test_workflow::runtimemodelaspect_instantiation(instance):
    assert isinstance(instance, workflow::RuntimeModelAspect)

@given(instance=workflow::TaskAspect_strategy)
@settings(max_examples=50)
def test_workflow::taskaspect_instantiation(instance):
    assert isinstance(instance, workflow::TaskAspect)

@given(instance=workflow::ProcessAspect_strategy)
@settings(max_examples=50)
def test_workflow::processaspect_instantiation(instance):
    assert isinstance(instance, workflow::ProcessAspect)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=workflow::Marking_strategy)
@settings(max_examples=50)
def test_workflow::marking_instantiation(instance):
    assert isinstance(instance, workflow::Marking)

@given(instance=workflow::String2DocumentMap_strategy)
@settings(max_examples=50)
def test_workflow::string2documentmap_instantiation(instance):
    assert isinstance(instance, workflow::String2DocumentMap)

@given(instance=workflow::String2DocumentMap_strategy)
def test_workflow::string2documentmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=workflow::String2DocumentMap_strategy)
def test_workflow::string2documentmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=workflow::Document_strategy)
@settings(max_examples=50)
def test_workflow::document_instantiation(instance):
    assert isinstance(instance, workflow::Document)

@given(instance=workflow::Document_strategy)
def test_workflow::document_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=workflow::Document_strategy)
def test_workflow::document_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=workflow::Document_strategy)
def test_workflow::document_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Document_strategy)
def test_workflow::document_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::DocumentType_strategy)
@settings(max_examples=50)
def test_workflow::documenttype_instantiation(instance):
    assert isinstance(instance, workflow::DocumentType)

@given(instance=workflow::DocumentType_strategy)
def test_workflow::documenttype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::DocumentType_strategy)
def test_workflow::documenttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::DocumentCondition_strategy)
@settings(max_examples=50)
def test_workflow::documentcondition_instantiation(instance):
    assert isinstance(instance, workflow::DocumentCondition)

@given(instance=workflow::DocumentCondition_strategy)
def test_workflow::documentcondition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::DocumentCondition_strategy)
def test_workflow::documentcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::DocumentDescriptor_strategy)
@settings(max_examples=50)
def test_workflow::documentdescriptor_instantiation(instance):
    assert isinstance(instance, workflow::DocumentDescriptor)

@given(instance=workflow::DocumentDescriptor_strategy)
def test_workflow::documentdescriptor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::DocumentDescriptor_strategy)
def test_workflow::documentdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::ProcessDocument_strategy)
@settings(max_examples=50)
def test_workflow::processdocument_instantiation(instance):
    assert isinstance(instance, workflow::ProcessDocument)

@given(instance=workflow::ProcessDocument_strategy)
def test_workflow::processdocument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::ProcessDocument_strategy)
def test_workflow::processdocument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::GlobalAspect_strategy)
@settings(max_examples=50)
def test_workflow::globalaspect_instantiation(instance):
    assert isinstance(instance, workflow::GlobalAspect)

@given(instance=workflow::CoreModel_strategy)
@settings(max_examples=50)
def test_workflow::coremodel_instantiation(instance):
    assert isinstance(instance, workflow::CoreModel)

@given(instance=workflow::CoreModel_strategy)
def test_workflow::coremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::CoreModel_strategy)
def test_workflow::coremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::WorkflowEngine_strategy)
@settings(max_examples=50)
def test_workflow::workflowengine_instantiation(instance):
    assert isinstance(instance, workflow::WorkflowEngine)

@given(instance=workflow::ModelRegistry_strategy)
@settings(max_examples=50)
def test_workflow::modelregistry_instantiation(instance):
    assert isinstance(instance, workflow::ModelRegistry)

@given(instance=workflow::Token_strategy)
@settings(max_examples=50)
def test_workflow::token_instantiation(instance):
    assert isinstance(instance, workflow::Token)

@given(instance=TaskC_strategy)
@settings(max_examples=50)
def test_taskc_instantiation(instance):
    assert isinstance(instance, TaskC)

@given(instance=workflow::Transition_strategy)
@settings(max_examples=50)
def test_workflow::transition_instantiation(instance):
    assert isinstance(instance, workflow::Transition)

@given(instance=workflow::Place_strategy)
@settings(max_examples=50)
def test_workflow::place_instantiation(instance):
    assert isinstance(instance, workflow::Place)

@given(instance=workflow::Place_strategy)
def test_workflow::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Place_strategy)
def test_workflow::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Arc_strategy)
@settings(max_examples=50)
def test_workflow::arc_instantiation(instance):
    assert isinstance(instance, workflow::Arc)

@given(instance=workflow::Arc_strategy)
def test_workflow::arc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Arc_strategy)
def test_workflow::arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=workflow::PetriNet_strategy)
@settings(max_examples=50)
def test_workflow::petrinet_instantiation(instance):
    assert isinstance(instance, workflow::PetriNet)

@given(instance=workflow::State_strategy)
@settings(max_examples=50)
def test_workflow::state_instantiation(instance):
    assert isinstance(instance, workflow::State)

@given(instance=CaseAspect_strategy)
@settings(max_examples=50)
def test_caseaspect_instantiation(instance):
    assert isinstance(instance, CaseAspect)

@given(instance=workflow::CaseO_strategy)
@settings(max_examples=50)
def test_workflow::caseo_instantiation(instance):
    assert isinstance(instance, workflow::CaseO)

@given(instance=workflow::CaseI_strategy)
@settings(max_examples=50)
def test_workflow::casei_instantiation(instance):
    assert isinstance(instance, workflow::CaseI)

@given(instance=ProcessAspect_strategy)
@settings(max_examples=50)
def test_processaspect_instantiation(instance):
    assert isinstance(instance, ProcessAspect)

@given(instance=workflow::Information_strategy)
@settings(max_examples=50)
def test_workflow::information_instantiation(instance):
    assert isinstance(instance, workflow::Information)

@given(instance=workflow::ProcessO_strategy)
@settings(max_examples=50)
def test_workflow::processo_instantiation(instance):
    assert isinstance(instance, workflow::ProcessO)

@given(instance=workflow::Control_strategy)
@settings(max_examples=50)
def test_workflow::control_instantiation(instance):
    assert isinstance(instance, workflow::Control)

@given(instance=workflow::CaseC_strategy)
@settings(max_examples=50)
def test_workflow::casec_instantiation(instance):
    assert isinstance(instance, workflow::CaseC)

@given(instance=workflow::RuntimeInformation_strategy)
@settings(max_examples=50)
def test_workflow::runtimeinformation_instantiation(instance):
    assert isinstance(instance, workflow::RuntimeInformation)

@given(instance=workflow::RuntimeInformation_strategy)
def test_workflow::runtimeinformation_caseIdCount_type(instance):
    assert isinstance(instance.caseIdCount, str)


@given(instance=workflow::RuntimeInformation_strategy)
def test_workflow::runtimeinformation_caseIdCount_setter(instance):
    original = instance.caseIdCount
    instance.caseIdCount = original
    assert instance.caseIdCount == original

@given(instance=workflow::Task_strategy)
@settings(max_examples=50)
def test_workflow::task_instantiation(instance):
    assert isinstance(instance, workflow::Task)

@given(instance=workflow::Task_strategy)
def test_workflow::task_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Task_strategy)
def test_workflow::task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::ActivityAspect_strategy)
@settings(max_examples=50)
def test_workflow::activityaspect_instantiation(instance):
    assert isinstance(instance, workflow::ActivityAspect)

@given(instance=workflow::RuntimeCoreModel_strategy)
@settings(max_examples=50)
def test_workflow::runtimecoremodel_instantiation(instance):
    assert isinstance(instance, workflow::RuntimeCoreModel)

@given(instance=workflow::Process_strategy)
@settings(max_examples=50)
def test_workflow::process_instantiation(instance):
    assert isinstance(instance, workflow::Process)

@given(instance=workflow::Process_strategy)
def test_workflow::process_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Process_strategy)
def test_workflow::process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Activity_strategy)
@settings(max_examples=50)
def test_workflow::activity_instantiation(instance):
    assert isinstance(instance, workflow::Activity)

@given(instance=workflow::Activity_strategy)
def test_workflow::activity_started_type(instance):
    assert isinstance(instance.started, bool)


@given(instance=workflow::Activity_strategy)
def test_workflow::activity_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original

@given(instance=workflow::Activity_strategy)
def test_workflow::activity_finished_type(instance):
    assert isinstance(instance.finished, bool)


@given(instance=workflow::Activity_strategy)
def test_workflow::activity_finished_setter(instance):
    original = instance.finished
    instance.finished = original
    assert instance.finished == original

@given(instance=workflow::CaseAspect_strategy)
@settings(max_examples=50)
def test_workflow::caseaspect_instantiation(instance):
    assert isinstance(instance, workflow::CaseAspect)

@given(instance=workflow::Case_strategy)
@settings(max_examples=50)
def test_workflow::case_instantiation(instance):
    assert isinstance(instance, workflow::Case)

@given(instance=workflow::Case_strategy)
def test_workflow::case_started_type(instance):
    assert isinstance(instance.started, bool)


@given(instance=workflow::Case_strategy)
def test_workflow::case_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original

@given(instance=workflow::Case_strategy)
def test_workflow::case_client_type(instance):
    assert isinstance(instance.client, str)


@given(instance=workflow::Case_strategy)
def test_workflow::case_client_setter(instance):
    original = instance.client
    instance.client = original
    assert instance.client == original

@given(instance=workflow::Case_strategy)
def test_workflow::case_finished_type(instance):
    assert isinstance(instance.finished, bool)


@given(instance=workflow::Case_strategy)
def test_workflow::case_finished_setter(instance):
    original = instance.finished
    instance.finished = original
    assert instance.finished == original

@given(instance=workflow::Case_strategy)
def test_workflow::case_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=workflow::Case_strategy)
def test_workflow::case_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=workflow::Agent_strategy)
@settings(max_examples=50)
def test_workflow::agent_instantiation(instance):
    assert isinstance(instance, workflow::Agent)

@given(instance=workflow::Agent_strategy)
def test_workflow::agent_username_type(instance):
    assert isinstance(instance.username, str)


@given(instance=workflow::Agent_strategy)
def test_workflow::agent_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=workflow::Agent_strategy)
def test_workflow::agent_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=workflow::Agent_strategy)
def test_workflow::agent_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=workflow::Agent_strategy)
def test_workflow::agent_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Agent_strategy)
def test_workflow::agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActivityAspect_strategy)
@settings(max_examples=50)
def test_activityaspect_instantiation(instance):
    assert isinstance(instance, ActivityAspect)

@given(instance=workflow::ActivityC_strategy)
@settings(max_examples=50)
def test_workflow::activityc_instantiation(instance):
    assert isinstance(instance, workflow::ActivityC)

@given(instance=workflow::ActivityI_strategy)
@settings(max_examples=50)
def test_workflow::activityi_instantiation(instance):
    assert isinstance(instance, workflow::ActivityI)

@given(instance=workflow::ActivityO_strategy)
@settings(max_examples=50)
def test_workflow::activityo_instantiation(instance):
    assert isinstance(instance, workflow::ActivityO)

@given(instance=workflow::Role_strategy)
@settings(max_examples=50)
def test_workflow::role_instantiation(instance):
    assert isinstance(instance, workflow::Role)

@given(instance=workflow::Role_strategy)
def test_workflow::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Role_strategy)
def test_workflow::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TaskAspect_strategy)
@settings(max_examples=50)
def test_taskaspect_instantiation(instance):
    assert isinstance(instance, TaskAspect)

@given(instance=workflow::TaskC_strategy)
@settings(max_examples=50)
def test_workflow::taskc_instantiation(instance):
    assert isinstance(instance, workflow::TaskC)

@given(instance=workflow::TaskC_strategy)
def test_workflow::taskc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::TaskC_strategy)
def test_workflow::taskc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::TaskI_strategy)
@settings(max_examples=50)
def test_workflow::taski_instantiation(instance):
    assert isinstance(instance, workflow::TaskI)

@given(instance=workflow::TaskO_strategy)
@settings(max_examples=50)
def test_workflow::tasko_instantiation(instance):
    assert isinstance(instance, workflow::TaskO)

@given(instance=workflow::TaskO_strategy)
def test_workflow::tasko_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::TaskO_strategy)
def test_workflow::tasko_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
