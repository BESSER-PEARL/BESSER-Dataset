import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GlobalAspect,
    workflow_DocumentTypeContainer,
    workflow_Organisation,
    RuntimeGlobalAspect,
    workflow_DocumentContainer,
    workflow_AgentContainer,
    workflow_EnumLiteral,
    DocumentCondition,
    workflow_DefaultDocumentCondition,
    Operator,
    workflow_EqualToOperator,
    workflow_UnequalToOperator,
    workflow_GreaterThanOperator,
    workflow_LessThanOperator,
    workflow_DotOperator,
    Atom,
    workflow_ConstantAtom,
    workflow_EnumLiteralAtom,
    workflow_FieldAtom,
    workflow_EnumFieldAtom,
    workflow_DocumentDescrAtom,
    Expression,
    workflow_Operator,
    workflow_Atom,
    DocumentDescriptor,
    workflow_DefaultDocumentDescriptor,
    RuntimeModelAspect,
    workflow_InformationRuntimeAspect,
    workflow_EnumFieldValue,
    workflow_FieldValue,
    Document,
    workflow_DefaultDocument,
    workflow_EnumField,
    workflow_Field,
    DocumentType,
    workflow_DefaultDocumentType,
    workflow_Expression,
    workflow_RuntimeGlobalAspect,
    ModelAspect,
    workflow_InformationAspect,
    workflow_ControlAspect,
    workflow_OrganisationAspect,
    workflow_ModelAspect,
    workflow_RuntimeModelAspect,
    workflow_TaskAspect,
    workflow_ProcessAspect,
    State,
    workflow_Marking,
    workflow_String2DocumentMap,
    workflow_Document,
    workflow_DocumentType,
    workflow_DocumentCondition,
    workflow_DocumentDescriptor,
    workflow_ProcessDocument,
    workflow_GlobalAspect,
    workflow_CoreModel,
    workflow_WorkflowEngine,
    workflow_ModelRegistry,
    workflow_Token,
    TaskC,
    workflow_Transition,
    workflow_Place,
    workflow_Arc,
    Control,
    workflow_PetriNet,
    workflow_State,
    CaseAspect,
    workflow_CaseI,
    workflow_CaseO,
    ProcessAspect,
    workflow_Information,
    workflow_ProcessO,
    workflow_Control,
    workflow_CaseC,
    workflow_RuntimeInformation,
    workflow_Task,
    workflow_ActivityAspect,
    workflow_RuntimeCoreModel,
    workflow_Process,
    workflow_Activity,
    workflow_CaseAspect,
    workflow_Case,
    workflow_Agent,
    ActivityAspect,
    workflow_ActivityI,
    workflow_ActivityC,
    workflow_ActivityO,
    workflow_Role,
    TaskAspect,
    workflow_TaskC,
    workflow_TaskI,
    workflow_TaskO,
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



def test_workflow_documenttypecontainer_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentTypeContainer)


def test_workflow_documenttypecontainer_constructor_exists():
    assert callable(workflow_DocumentTypeContainer.__init__)


def test_workflow_documenttypecontainer_constructor_args():
    sig = inspect.signature(workflow_DocumentTypeContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_documenttypecontainer_has_name():
    assert hasattr(workflow_DocumentTypeContainer, "name")
    descriptor = None
    for klass in workflow_DocumentTypeContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_organisation_is_not_abstract():
    assert not inspect.isabstract(workflow_Organisation)


def test_workflow_organisation_constructor_exists():
    assert callable(workflow_Organisation.__init__)


def test_workflow_organisation_constructor_args():
    sig = inspect.signature(workflow_Organisation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_organisation_has_name():
    assert hasattr(workflow_Organisation, "name")
    descriptor = None
    for klass in workflow_Organisation.__mro__:
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



def test_workflow_documentcontainer_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentContainer)


def test_workflow_documentcontainer_constructor_exists():
    assert callable(workflow_DocumentContainer.__init__)


def test_workflow_documentcontainer_constructor_args():
    sig = inspect.signature(workflow_DocumentContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_documentcontainer_has_name():
    assert hasattr(workflow_DocumentContainer, "name")
    descriptor = None
    for klass in workflow_DocumentContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_agentcontainer_is_not_abstract():
    assert not inspect.isabstract(workflow_AgentContainer)


def test_workflow_agentcontainer_constructor_exists():
    assert callable(workflow_AgentContainer.__init__)


def test_workflow_agentcontainer_constructor_args():
    sig = inspect.signature(workflow_AgentContainer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_agentcontainer_has_name():
    assert hasattr(workflow_AgentContainer, "name")
    descriptor = None
    for klass in workflow_AgentContainer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_enumliteral_is_not_abstract():
    assert not inspect.isabstract(workflow_EnumLiteral)


def test_workflow_enumliteral_constructor_exists():
    assert callable(workflow_EnumLiteral.__init__)


def test_workflow_enumliteral_constructor_args():
    sig = inspect.signature(workflow_EnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_enumliteral_has_name():
    assert hasattr(workflow_EnumLiteral, "name")
    descriptor = None
    for klass in workflow_EnumLiteral.__mro__:
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



def test_workflow_defaultdocumentcondition_is_not_abstract():
    assert not inspect.isabstract(workflow_DefaultDocumentCondition)


def test_workflow_defaultdocumentcondition_constructor_exists():
    assert callable(workflow_DefaultDocumentCondition.__init__)


def test_workflow_defaultdocumentcondition_constructor_args():
    sig = inspect.signature(workflow_DefaultDocumentCondition.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_equaltooperator_is_not_abstract():
    assert not inspect.isabstract(workflow_EqualToOperator)


def test_workflow_equaltooperator_constructor_exists():
    assert callable(workflow_EqualToOperator.__init__)


def test_workflow_equaltooperator_constructor_args():
    sig = inspect.signature(workflow_EqualToOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_unequaltooperator_is_not_abstract():
    assert not inspect.isabstract(workflow_UnequalToOperator)


def test_workflow_unequaltooperator_constructor_exists():
    assert callable(workflow_UnequalToOperator.__init__)


def test_workflow_unequaltooperator_constructor_args():
    sig = inspect.signature(workflow_UnequalToOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_greaterthanoperator_is_not_abstract():
    assert not inspect.isabstract(workflow_GreaterThanOperator)


def test_workflow_greaterthanoperator_constructor_exists():
    assert callable(workflow_GreaterThanOperator.__init__)


def test_workflow_greaterthanoperator_constructor_args():
    sig = inspect.signature(workflow_GreaterThanOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_lessthanoperator_is_not_abstract():
    assert not inspect.isabstract(workflow_LessThanOperator)


def test_workflow_lessthanoperator_constructor_exists():
    assert callable(workflow_LessThanOperator.__init__)


def test_workflow_lessthanoperator_constructor_args():
    sig = inspect.signature(workflow_LessThanOperator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_dotoperator_is_not_abstract():
    assert not inspect.isabstract(workflow_DotOperator)


def test_workflow_dotoperator_constructor_exists():
    assert callable(workflow_DotOperator.__init__)


def test_workflow_dotoperator_constructor_args():
    sig = inspect.signature(workflow_DotOperator.__init__)
    params = list(sig.parameters.keys())



def test_atom_is_not_abstract():
    assert not inspect.isabstract(Atom)


def test_atom_constructor_exists():
    assert callable(Atom.__init__)


def test_atom_constructor_args():
    sig = inspect.signature(Atom.__init__)
    params = list(sig.parameters.keys())



def test_workflow_constantatom_is_not_abstract():
    assert not inspect.isabstract(workflow_ConstantAtom)


def test_workflow_constantatom_constructor_exists():
    assert callable(workflow_ConstantAtom.__init__)


def test_workflow_constantatom_constructor_args():
    sig = inspect.signature(workflow_ConstantAtom.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_workflow_constantatom_has_value():
    assert hasattr(workflow_ConstantAtom, "value")
    descriptor = None
    for klass in workflow_ConstantAtom.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_workflow_enumliteralatom_is_not_abstract():
    assert not inspect.isabstract(workflow_EnumLiteralAtom)


def test_workflow_enumliteralatom_constructor_exists():
    assert callable(workflow_EnumLiteralAtom.__init__)


def test_workflow_enumliteralatom_constructor_args():
    sig = inspect.signature(workflow_EnumLiteralAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow_fieldatom_is_not_abstract():
    assert not inspect.isabstract(workflow_FieldAtom)


def test_workflow_fieldatom_constructor_exists():
    assert callable(workflow_FieldAtom.__init__)


def test_workflow_fieldatom_constructor_args():
    sig = inspect.signature(workflow_FieldAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow_enumfieldatom_is_not_abstract():
    assert not inspect.isabstract(workflow_EnumFieldAtom)


def test_workflow_enumfieldatom_constructor_exists():
    assert callable(workflow_EnumFieldAtom.__init__)


def test_workflow_enumfieldatom_constructor_args():
    sig = inspect.signature(workflow_EnumFieldAtom.__init__)
    params = list(sig.parameters.keys())



def test_workflow_documentdescratom_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentDescrAtom)


def test_workflow_documentdescratom_constructor_exists():
    assert callable(workflow_DocumentDescrAtom.__init__)


def test_workflow_documentdescratom_constructor_args():
    sig = inspect.signature(workflow_DocumentDescrAtom.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_operator_is_not_abstract():
    assert not inspect.isabstract(workflow_Operator)


def test_workflow_operator_constructor_exists():
    assert callable(workflow_Operator.__init__)


def test_workflow_operator_constructor_args():
    sig = inspect.signature(workflow_Operator.__init__)
    params = list(sig.parameters.keys())



def test_workflow_atom_is_not_abstract():
    assert not inspect.isabstract(workflow_Atom)


def test_workflow_atom_constructor_exists():
    assert callable(workflow_Atom.__init__)


def test_workflow_atom_constructor_args():
    sig = inspect.signature(workflow_Atom.__init__)
    params = list(sig.parameters.keys())



def test_documentdescriptor_is_not_abstract():
    assert not inspect.isabstract(DocumentDescriptor)


def test_documentdescriptor_constructor_exists():
    assert callable(DocumentDescriptor.__init__)


def test_documentdescriptor_constructor_args():
    sig = inspect.signature(DocumentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_workflow_defaultdocumentdescriptor_is_not_abstract():
    assert not inspect.isabstract(workflow_DefaultDocumentDescriptor)


def test_workflow_defaultdocumentdescriptor_constructor_exists():
    assert callable(workflow_DefaultDocumentDescriptor.__init__)


def test_workflow_defaultdocumentdescriptor_constructor_args():
    sig = inspect.signature(workflow_DefaultDocumentDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_runtimemodelaspect_is_not_abstract():
    assert not inspect.isabstract(RuntimeModelAspect)


def test_runtimemodelaspect_constructor_exists():
    assert callable(RuntimeModelAspect.__init__)


def test_runtimemodelaspect_constructor_args():
    sig = inspect.signature(RuntimeModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_informationruntimeaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_InformationRuntimeAspect)


def test_workflow_informationruntimeaspect_constructor_exists():
    assert callable(workflow_InformationRuntimeAspect.__init__)


def test_workflow_informationruntimeaspect_constructor_args():
    sig = inspect.signature(workflow_InformationRuntimeAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_enumfieldvalue_is_not_abstract():
    assert not inspect.isabstract(workflow_EnumFieldValue)


def test_workflow_enumfieldvalue_constructor_exists():
    assert callable(workflow_EnumFieldValue.__init__)


def test_workflow_enumfieldvalue_constructor_args():
    sig = inspect.signature(workflow_EnumFieldValue.__init__)
    params = list(sig.parameters.keys())



def test_workflow_fieldvalue_is_not_abstract():
    assert not inspect.isabstract(workflow_FieldValue)


def test_workflow_fieldvalue_constructor_exists():
    assert callable(workflow_FieldValue.__init__)


def test_workflow_fieldvalue_constructor_args():
    sig = inspect.signature(workflow_FieldValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_workflow_fieldvalue_has_value():
    assert hasattr(workflow_FieldValue, "value")
    descriptor = None
    for klass in workflow_FieldValue.__mro__:
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



def test_workflow_defaultdocument_is_not_abstract():
    assert not inspect.isabstract(workflow_DefaultDocument)


def test_workflow_defaultdocument_constructor_exists():
    assert callable(workflow_DefaultDocument.__init__)


def test_workflow_defaultdocument_constructor_args():
    sig = inspect.signature(workflow_DefaultDocument.__init__)
    params = list(sig.parameters.keys())
    assert "placeholder" in params, "Missing parameter 'placeholder'"

def test_workflow_defaultdocument_has_placeholder():
    assert hasattr(workflow_DefaultDocument, "placeholder")
    descriptor = None
    for klass in workflow_DefaultDocument.__mro__:
        if "placeholder" in klass.__dict__:
            descriptor = klass.__dict__["placeholder"]
            break
    assert isinstance(descriptor, property)



def test_workflow_enumfield_is_not_abstract():
    assert not inspect.isabstract(workflow_EnumField)


def test_workflow_enumfield_constructor_exists():
    assert callable(workflow_EnumField.__init__)


def test_workflow_enumfield_constructor_args():
    sig = inspect.signature(workflow_EnumField.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_enumfield_has_name():
    assert hasattr(workflow_EnumField, "name")
    descriptor = None
    for klass in workflow_EnumField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_field_is_not_abstract():
    assert not inspect.isabstract(workflow_Field)


def test_workflow_field_constructor_exists():
    assert callable(workflow_Field.__init__)


def test_workflow_field_constructor_args():
    sig = inspect.signature(workflow_Field.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_field_has_name():
    assert hasattr(workflow_Field, "name")
    descriptor = None
    for klass in workflow_Field.__mro__:
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



def test_workflow_defaultdocumenttype_is_not_abstract():
    assert not inspect.isabstract(workflow_DefaultDocumentType)


def test_workflow_defaultdocumenttype_constructor_exists():
    assert callable(workflow_DefaultDocumentType.__init__)


def test_workflow_defaultdocumenttype_constructor_args():
    sig = inspect.signature(workflow_DefaultDocumentType.__init__)
    params = list(sig.parameters.keys())



def test_workflow_expression_is_not_abstract():
    assert not inspect.isabstract(workflow_Expression)


def test_workflow_expression_constructor_exists():
    assert callable(workflow_Expression.__init__)


def test_workflow_expression_constructor_args():
    sig = inspect.signature(workflow_Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_runtimeglobalaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_RuntimeGlobalAspect)


def test_workflow_runtimeglobalaspect_constructor_exists():
    assert callable(workflow_RuntimeGlobalAspect.__init__)


def test_workflow_runtimeglobalaspect_constructor_args():
    sig = inspect.signature(workflow_RuntimeGlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_modelaspect_is_not_abstract():
    assert not inspect.isabstract(ModelAspect)


def test_modelaspect_constructor_exists():
    assert callable(ModelAspect.__init__)


def test_modelaspect_constructor_args():
    sig = inspect.signature(ModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_informationaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_InformationAspect)


def test_workflow_informationaspect_constructor_exists():
    assert callable(workflow_InformationAspect.__init__)


def test_workflow_informationaspect_constructor_args():
    sig = inspect.signature(workflow_InformationAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_controlaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_ControlAspect)


def test_workflow_controlaspect_constructor_exists():
    assert callable(workflow_ControlAspect.__init__)


def test_workflow_controlaspect_constructor_args():
    sig = inspect.signature(workflow_ControlAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_organisationaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_OrganisationAspect)


def test_workflow_organisationaspect_constructor_exists():
    assert callable(workflow_OrganisationAspect.__init__)


def test_workflow_organisationaspect_constructor_args():
    sig = inspect.signature(workflow_OrganisationAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_modelaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_ModelAspect)


def test_workflow_modelaspect_constructor_exists():
    assert callable(workflow_ModelAspect.__init__)


def test_workflow_modelaspect_constructor_args():
    sig = inspect.signature(workflow_ModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_runtimemodelaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_RuntimeModelAspect)


def test_workflow_runtimemodelaspect_constructor_exists():
    assert callable(workflow_RuntimeModelAspect.__init__)


def test_workflow_runtimemodelaspect_constructor_args():
    sig = inspect.signature(workflow_RuntimeModelAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_taskaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_TaskAspect)


def test_workflow_taskaspect_constructor_exists():
    assert callable(workflow_TaskAspect.__init__)


def test_workflow_taskaspect_constructor_args():
    sig = inspect.signature(workflow_TaskAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_processaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcessAspect)


def test_workflow_processaspect_constructor_exists():
    assert callable(workflow_ProcessAspect.__init__)


def test_workflow_processaspect_constructor_args():
    sig = inspect.signature(workflow_ProcessAspect.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_workflow_marking_is_not_abstract():
    assert not inspect.isabstract(workflow_Marking)


def test_workflow_marking_constructor_exists():
    assert callable(workflow_Marking.__init__)


def test_workflow_marking_constructor_args():
    sig = inspect.signature(workflow_Marking.__init__)
    params = list(sig.parameters.keys())



def test_workflow_string2documentmap_is_not_abstract():
    assert not inspect.isabstract(workflow_String2DocumentMap)


def test_workflow_string2documentmap_constructor_exists():
    assert callable(workflow_String2DocumentMap.__init__)


def test_workflow_string2documentmap_constructor_args():
    sig = inspect.signature(workflow_String2DocumentMap.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"

def test_workflow_string2documentmap_has_key():
    assert hasattr(workflow_String2DocumentMap, "key")
    descriptor = None
    for klass in workflow_String2DocumentMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_workflow_document_is_not_abstract():
    assert not inspect.isabstract(workflow_Document)


def test_workflow_document_constructor_exists():
    assert callable(workflow_Document.__init__)


def test_workflow_document_constructor_args():
    sig = inspect.signature(workflow_Document.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_workflow_document_has_name():
    assert hasattr(workflow_Document, "name")
    descriptor = None
    for klass in workflow_Document.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_workflow_document_has_id():
    assert hasattr(workflow_Document, "id")
    descriptor = None
    for klass in workflow_Document.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_workflow_documenttype_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentType)


def test_workflow_documenttype_constructor_exists():
    assert callable(workflow_DocumentType.__init__)


def test_workflow_documenttype_constructor_args():
    sig = inspect.signature(workflow_DocumentType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_documenttype_has_name():
    assert hasattr(workflow_DocumentType, "name")
    descriptor = None
    for klass in workflow_DocumentType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_documentcondition_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentCondition)


def test_workflow_documentcondition_constructor_exists():
    assert callable(workflow_DocumentCondition.__init__)


def test_workflow_documentcondition_constructor_args():
    sig = inspect.signature(workflow_DocumentCondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_documentcondition_has_name():
    assert hasattr(workflow_DocumentCondition, "name")
    descriptor = None
    for klass in workflow_DocumentCondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_documentdescriptor_is_not_abstract():
    assert not inspect.isabstract(workflow_DocumentDescriptor)


def test_workflow_documentdescriptor_constructor_exists():
    assert callable(workflow_DocumentDescriptor.__init__)


def test_workflow_documentdescriptor_constructor_args():
    sig = inspect.signature(workflow_DocumentDescriptor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_documentdescriptor_has_name():
    assert hasattr(workflow_DocumentDescriptor, "name")
    descriptor = None
    for klass in workflow_DocumentDescriptor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_processdocument_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcessDocument)


def test_workflow_processdocument_constructor_exists():
    assert callable(workflow_ProcessDocument.__init__)


def test_workflow_processdocument_constructor_args():
    sig = inspect.signature(workflow_ProcessDocument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_processdocument_has_name():
    assert hasattr(workflow_ProcessDocument, "name")
    descriptor = None
    for klass in workflow_ProcessDocument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_globalaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_GlobalAspect)


def test_workflow_globalaspect_constructor_exists():
    assert callable(workflow_GlobalAspect.__init__)


def test_workflow_globalaspect_constructor_args():
    sig = inspect.signature(workflow_GlobalAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_coremodel_is_not_abstract():
    assert not inspect.isabstract(workflow_CoreModel)


def test_workflow_coremodel_constructor_exists():
    assert callable(workflow_CoreModel.__init__)


def test_workflow_coremodel_constructor_args():
    sig = inspect.signature(workflow_CoreModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_coremodel_has_name():
    assert hasattr(workflow_CoreModel, "name")
    descriptor = None
    for klass in workflow_CoreModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_workflowengine_is_not_abstract():
    assert not inspect.isabstract(workflow_WorkflowEngine)


def test_workflow_workflowengine_constructor_exists():
    assert callable(workflow_WorkflowEngine.__init__)


def test_workflow_workflowengine_constructor_args():
    sig = inspect.signature(workflow_WorkflowEngine.__init__)
    params = list(sig.parameters.keys())



def test_workflow_modelregistry_is_not_abstract():
    assert not inspect.isabstract(workflow_ModelRegistry)


def test_workflow_modelregistry_constructor_exists():
    assert callable(workflow_ModelRegistry.__init__)


def test_workflow_modelregistry_constructor_args():
    sig = inspect.signature(workflow_ModelRegistry.__init__)
    params = list(sig.parameters.keys())



def test_workflow_token_is_not_abstract():
    assert not inspect.isabstract(workflow_Token)


def test_workflow_token_constructor_exists():
    assert callable(workflow_Token.__init__)


def test_workflow_token_constructor_args():
    sig = inspect.signature(workflow_Token.__init__)
    params = list(sig.parameters.keys())



def test_taskc_is_not_abstract():
    assert not inspect.isabstract(TaskC)


def test_taskc_constructor_exists():
    assert callable(TaskC.__init__)


def test_taskc_constructor_args():
    sig = inspect.signature(TaskC.__init__)
    params = list(sig.parameters.keys())



def test_workflow_transition_is_not_abstract():
    assert not inspect.isabstract(workflow_Transition)


def test_workflow_transition_constructor_exists():
    assert callable(workflow_Transition.__init__)


def test_workflow_transition_constructor_args():
    sig = inspect.signature(workflow_Transition.__init__)
    params = list(sig.parameters.keys())



def test_workflow_place_is_not_abstract():
    assert not inspect.isabstract(workflow_Place)


def test_workflow_place_constructor_exists():
    assert callable(workflow_Place.__init__)


def test_workflow_place_constructor_args():
    sig = inspect.signature(workflow_Place.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_place_has_name():
    assert hasattr(workflow_Place, "name")
    descriptor = None
    for klass in workflow_Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_arc_is_not_abstract():
    assert not inspect.isabstract(workflow_Arc)


def test_workflow_arc_constructor_exists():
    assert callable(workflow_Arc.__init__)


def test_workflow_arc_constructor_args():
    sig = inspect.signature(workflow_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_arc_has_name():
    assert hasattr(workflow_Arc, "name")
    descriptor = None
    for klass in workflow_Arc.__mro__:
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



def test_workflow_petrinet_is_not_abstract():
    assert not inspect.isabstract(workflow_PetriNet)


def test_workflow_petrinet_constructor_exists():
    assert callable(workflow_PetriNet.__init__)


def test_workflow_petrinet_constructor_args():
    sig = inspect.signature(workflow_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_workflow_state_is_not_abstract():
    assert not inspect.isabstract(workflow_State)


def test_workflow_state_constructor_exists():
    assert callable(workflow_State.__init__)


def test_workflow_state_constructor_args():
    sig = inspect.signature(workflow_State.__init__)
    params = list(sig.parameters.keys())



def test_caseaspect_is_not_abstract():
    assert not inspect.isabstract(CaseAspect)


def test_caseaspect_constructor_exists():
    assert callable(CaseAspect.__init__)


def test_caseaspect_constructor_args():
    sig = inspect.signature(CaseAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_casei_is_not_abstract():
    assert not inspect.isabstract(workflow_CaseI)


def test_workflow_casei_constructor_exists():
    assert callable(workflow_CaseI.__init__)


def test_workflow_casei_constructor_args():
    sig = inspect.signature(workflow_CaseI.__init__)
    params = list(sig.parameters.keys())



def test_workflow_caseo_is_not_abstract():
    assert not inspect.isabstract(workflow_CaseO)


def test_workflow_caseo_constructor_exists():
    assert callable(workflow_CaseO.__init__)


def test_workflow_caseo_constructor_args():
    sig = inspect.signature(workflow_CaseO.__init__)
    params = list(sig.parameters.keys())



def test_processaspect_is_not_abstract():
    assert not inspect.isabstract(ProcessAspect)


def test_processaspect_constructor_exists():
    assert callable(ProcessAspect.__init__)


def test_processaspect_constructor_args():
    sig = inspect.signature(ProcessAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_information_is_not_abstract():
    assert not inspect.isabstract(workflow_Information)


def test_workflow_information_constructor_exists():
    assert callable(workflow_Information.__init__)


def test_workflow_information_constructor_args():
    sig = inspect.signature(workflow_Information.__init__)
    params = list(sig.parameters.keys())



def test_workflow_processo_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcessO)


def test_workflow_processo_constructor_exists():
    assert callable(workflow_ProcessO.__init__)


def test_workflow_processo_constructor_args():
    sig = inspect.signature(workflow_ProcessO.__init__)
    params = list(sig.parameters.keys())



def test_workflow_control_is_not_abstract():
    assert not inspect.isabstract(workflow_Control)


def test_workflow_control_constructor_exists():
    assert callable(workflow_Control.__init__)


def test_workflow_control_constructor_args():
    sig = inspect.signature(workflow_Control.__init__)
    params = list(sig.parameters.keys())



def test_workflow_casec_is_not_abstract():
    assert not inspect.isabstract(workflow_CaseC)


def test_workflow_casec_constructor_exists():
    assert callable(workflow_CaseC.__init__)


def test_workflow_casec_constructor_args():
    sig = inspect.signature(workflow_CaseC.__init__)
    params = list(sig.parameters.keys())



def test_workflow_runtimeinformation_is_not_abstract():
    assert not inspect.isabstract(workflow_RuntimeInformation)


def test_workflow_runtimeinformation_constructor_exists():
    assert callable(workflow_RuntimeInformation.__init__)


def test_workflow_runtimeinformation_constructor_args():
    sig = inspect.signature(workflow_RuntimeInformation.__init__)
    params = list(sig.parameters.keys())
    assert "caseIdCount" in params, "Missing parameter 'caseIdCount'"

def test_workflow_runtimeinformation_has_caseIdCount():
    assert hasattr(workflow_RuntimeInformation, "caseIdCount")
    descriptor = None
    for klass in workflow_RuntimeInformation.__mro__:
        if "caseIdCount" in klass.__dict__:
            descriptor = klass.__dict__["caseIdCount"]
            break
    assert isinstance(descriptor, property)



def test_workflow_task_is_not_abstract():
    assert not inspect.isabstract(workflow_Task)


def test_workflow_task_constructor_exists():
    assert callable(workflow_Task.__init__)


def test_workflow_task_constructor_args():
    sig = inspect.signature(workflow_Task.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_task_has_name():
    assert hasattr(workflow_Task, "name")
    descriptor = None
    for klass in workflow_Task.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_activityaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_ActivityAspect)


def test_workflow_activityaspect_constructor_exists():
    assert callable(workflow_ActivityAspect.__init__)


def test_workflow_activityaspect_constructor_args():
    sig = inspect.signature(workflow_ActivityAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_runtimecoremodel_is_not_abstract():
    assert not inspect.isabstract(workflow_RuntimeCoreModel)


def test_workflow_runtimecoremodel_constructor_exists():
    assert callable(workflow_RuntimeCoreModel.__init__)


def test_workflow_runtimecoremodel_constructor_args():
    sig = inspect.signature(workflow_RuntimeCoreModel.__init__)
    params = list(sig.parameters.keys())



def test_workflow_process_is_not_abstract():
    assert not inspect.isabstract(workflow_Process)


def test_workflow_process_constructor_exists():
    assert callable(workflow_Process.__init__)


def test_workflow_process_constructor_args():
    sig = inspect.signature(workflow_Process.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_process_has_name():
    assert hasattr(workflow_Process, "name")
    descriptor = None
    for klass in workflow_Process.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_activity_is_not_abstract():
    assert not inspect.isabstract(workflow_Activity)


def test_workflow_activity_constructor_exists():
    assert callable(workflow_Activity.__init__)


def test_workflow_activity_constructor_args():
    sig = inspect.signature(workflow_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "finished" in params, "Missing parameter 'finished'"
    assert "started" in params, "Missing parameter 'started'"

def test_workflow_activity_has_finished():
    assert hasattr(workflow_Activity, "finished")
    descriptor = None
    for klass in workflow_Activity.__mro__:
        if "finished" in klass.__dict__:
            descriptor = klass.__dict__["finished"]
            break
    assert isinstance(descriptor, property)

def test_workflow_activity_has_started():
    assert hasattr(workflow_Activity, "started")
    descriptor = None
    for klass in workflow_Activity.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)



def test_workflow_caseaspect_is_not_abstract():
    assert not inspect.isabstract(workflow_CaseAspect)


def test_workflow_caseaspect_constructor_exists():
    assert callable(workflow_CaseAspect.__init__)


def test_workflow_caseaspect_constructor_args():
    sig = inspect.signature(workflow_CaseAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_case_is_not_abstract():
    assert not inspect.isabstract(workflow_Case)


def test_workflow_case_constructor_exists():
    assert callable(workflow_Case.__init__)


def test_workflow_case_constructor_args():
    sig = inspect.signature(workflow_Case.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "client" in params, "Missing parameter 'client'"
    assert "finished" in params, "Missing parameter 'finished'"
    assert "started" in params, "Missing parameter 'started'"

def test_workflow_case_has_id():
    assert hasattr(workflow_Case, "id")
    descriptor = None
    for klass in workflow_Case.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_workflow_case_has_client():
    assert hasattr(workflow_Case, "client")
    descriptor = None
    for klass in workflow_Case.__mro__:
        if "client" in klass.__dict__:
            descriptor = klass.__dict__["client"]
            break
    assert isinstance(descriptor, property)

def test_workflow_case_has_finished():
    assert hasattr(workflow_Case, "finished")
    descriptor = None
    for klass in workflow_Case.__mro__:
        if "finished" in klass.__dict__:
            descriptor = klass.__dict__["finished"]
            break
    assert isinstance(descriptor, property)

def test_workflow_case_has_started():
    assert hasattr(workflow_Case, "started")
    descriptor = None
    for klass in workflow_Case.__mro__:
        if "started" in klass.__dict__:
            descriptor = klass.__dict__["started"]
            break
    assert isinstance(descriptor, property)



def test_workflow_agent_is_not_abstract():
    assert not inspect.isabstract(workflow_Agent)


def test_workflow_agent_constructor_exists():
    assert callable(workflow_Agent.__init__)


def test_workflow_agent_constructor_args():
    sig = inspect.signature(workflow_Agent.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"

def test_workflow_agent_has_username():
    assert hasattr(workflow_Agent, "username")
    descriptor = None
    for klass in workflow_Agent.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_workflow_agent_has_name():
    assert hasattr(workflow_Agent, "name")
    descriptor = None
    for klass in workflow_Agent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_workflow_agent_has_password():
    assert hasattr(workflow_Agent, "password")
    descriptor = None
    for klass in workflow_Agent.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_activityaspect_is_not_abstract():
    assert not inspect.isabstract(ActivityAspect)


def test_activityaspect_constructor_exists():
    assert callable(ActivityAspect.__init__)


def test_activityaspect_constructor_args():
    sig = inspect.signature(ActivityAspect.__init__)
    params = list(sig.parameters.keys())



def test_workflow_activityi_is_not_abstract():
    assert not inspect.isabstract(workflow_ActivityI)


def test_workflow_activityi_constructor_exists():
    assert callable(workflow_ActivityI.__init__)


def test_workflow_activityi_constructor_args():
    sig = inspect.signature(workflow_ActivityI.__init__)
    params = list(sig.parameters.keys())



def test_workflow_activityc_is_not_abstract():
    assert not inspect.isabstract(workflow_ActivityC)


def test_workflow_activityc_constructor_exists():
    assert callable(workflow_ActivityC.__init__)


def test_workflow_activityc_constructor_args():
    sig = inspect.signature(workflow_ActivityC.__init__)
    params = list(sig.parameters.keys())



def test_workflow_activityo_is_not_abstract():
    assert not inspect.isabstract(workflow_ActivityO)


def test_workflow_activityo_constructor_exists():
    assert callable(workflow_ActivityO.__init__)


def test_workflow_activityo_constructor_args():
    sig = inspect.signature(workflow_ActivityO.__init__)
    params = list(sig.parameters.keys())



def test_workflow_role_is_not_abstract():
    assert not inspect.isabstract(workflow_Role)


def test_workflow_role_constructor_exists():
    assert callable(workflow_Role.__init__)


def test_workflow_role_constructor_args():
    sig = inspect.signature(workflow_Role.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_role_has_name():
    assert hasattr(workflow_Role, "name")
    descriptor = None
    for klass in workflow_Role.__mro__:
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



def test_workflow_taskc_is_not_abstract():
    assert not inspect.isabstract(workflow_TaskC)


def test_workflow_taskc_constructor_exists():
    assert callable(workflow_TaskC.__init__)


def test_workflow_taskc_constructor_args():
    sig = inspect.signature(workflow_TaskC.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_taskc_has_name():
    assert hasattr(workflow_TaskC, "name")
    descriptor = None
    for klass in workflow_TaskC.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_taski_is_not_abstract():
    assert not inspect.isabstract(workflow_TaskI)


def test_workflow_taski_constructor_exists():
    assert callable(workflow_TaskI.__init__)


def test_workflow_taski_constructor_args():
    sig = inspect.signature(workflow_TaskI.__init__)
    params = list(sig.parameters.keys())



def test_workflow_tasko_is_not_abstract():
    assert not inspect.isabstract(workflow_TaskO)


def test_workflow_tasko_constructor_exists():
    assert callable(workflow_TaskO.__init__)


def test_workflow_tasko_constructor_args():
    sig = inspect.signature(workflow_TaskO.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_tasko_has_name():
    assert hasattr(workflow_TaskO, "name")
    descriptor = None
    for klass in workflow_TaskO.__mro__:
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
workflow_DocumentTypeContainer_strategy = st.builds(
    workflow_DocumentTypeContainer,
    name=
        safe_text
)
workflow_Organisation_strategy = st.builds(
    workflow_Organisation,
    name=
        safe_text
)
RuntimeGlobalAspect_strategy = st.builds(
    RuntimeGlobalAspect,
)
workflow_DocumentContainer_strategy = st.builds(
    workflow_DocumentContainer,
    name=
        safe_text
)
workflow_AgentContainer_strategy = st.builds(
    workflow_AgentContainer,
    name=
        safe_text
)
workflow_EnumLiteral_strategy = st.builds(
    workflow_EnumLiteral,
    name=
        safe_text
)
DocumentCondition_strategy = st.builds(
    DocumentCondition,
)
workflow_DefaultDocumentCondition_strategy = st.builds(
    workflow_DefaultDocumentCondition,
)
Operator_strategy = st.builds(
    Operator,
)
workflow_EqualToOperator_strategy = st.builds(
    workflow_EqualToOperator,
)
workflow_UnequalToOperator_strategy = st.builds(
    workflow_UnequalToOperator,
)
workflow_GreaterThanOperator_strategy = st.builds(
    workflow_GreaterThanOperator,
)
workflow_LessThanOperator_strategy = st.builds(
    workflow_LessThanOperator,
)
workflow_DotOperator_strategy = st.builds(
    workflow_DotOperator,
)
Atom_strategy = st.builds(
    Atom,
)
workflow_ConstantAtom_strategy = st.builds(
    workflow_ConstantAtom,
    value=
        safe_text
)
workflow_EnumLiteralAtom_strategy = st.builds(
    workflow_EnumLiteralAtom,
)
workflow_FieldAtom_strategy = st.builds(
    workflow_FieldAtom,
)
workflow_EnumFieldAtom_strategy = st.builds(
    workflow_EnumFieldAtom,
)
workflow_DocumentDescrAtom_strategy = st.builds(
    workflow_DocumentDescrAtom,
)
Expression_strategy = st.builds(
    Expression,
)
workflow_Operator_strategy = st.builds(
    workflow_Operator,
)
workflow_Atom_strategy = st.builds(
    workflow_Atom,
)
DocumentDescriptor_strategy = st.builds(
    DocumentDescriptor,
)
workflow_DefaultDocumentDescriptor_strategy = st.builds(
    workflow_DefaultDocumentDescriptor,
)
RuntimeModelAspect_strategy = st.builds(
    RuntimeModelAspect,
)
workflow_InformationRuntimeAspect_strategy = st.builds(
    workflow_InformationRuntimeAspect,
)
workflow_EnumFieldValue_strategy = st.builds(
    workflow_EnumFieldValue,
)
workflow_FieldValue_strategy = st.builds(
    workflow_FieldValue,
    value=
        safe_text
)
Document_strategy = st.builds(
    Document,
)
workflow_DefaultDocument_strategy = st.builds(
    workflow_DefaultDocument,
    placeholder=
        st.booleans()
)
workflow_EnumField_strategy = st.builds(
    workflow_EnumField,
    name=
        safe_text
)
workflow_Field_strategy = st.builds(
    workflow_Field,
    name=
        safe_text
)
DocumentType_strategy = st.builds(
    DocumentType,
)
workflow_DefaultDocumentType_strategy = st.builds(
    workflow_DefaultDocumentType,
)
workflow_Expression_strategy = st.builds(
    workflow_Expression,
)
workflow_RuntimeGlobalAspect_strategy = st.builds(
    workflow_RuntimeGlobalAspect,
)
ModelAspect_strategy = st.builds(
    ModelAspect,
)
workflow_InformationAspect_strategy = st.builds(
    workflow_InformationAspect,
)
workflow_ControlAspect_strategy = st.builds(
    workflow_ControlAspect,
)
workflow_OrganisationAspect_strategy = st.builds(
    workflow_OrganisationAspect,
)
workflow_ModelAspect_strategy = st.builds(
    workflow_ModelAspect,
)
workflow_RuntimeModelAspect_strategy = st.builds(
    workflow_RuntimeModelAspect,
)
workflow_TaskAspect_strategy = st.builds(
    workflow_TaskAspect,
)
workflow_ProcessAspect_strategy = st.builds(
    workflow_ProcessAspect,
)
State_strategy = st.builds(
    State,
)
workflow_Marking_strategy = st.builds(
    workflow_Marking,
)
workflow_String2DocumentMap_strategy = st.builds(
    workflow_String2DocumentMap,
    key=
        safe_text
)
workflow_Document_strategy = st.builds(
    workflow_Document,
    name=
        safe_text,
    id=
        safe_text
)
workflow_DocumentType_strategy = st.builds(
    workflow_DocumentType,
    name=
        safe_text
)
workflow_DocumentCondition_strategy = st.builds(
    workflow_DocumentCondition,
    name=
        safe_text
)
workflow_DocumentDescriptor_strategy = st.builds(
    workflow_DocumentDescriptor,
    name=
        safe_text
)
workflow_ProcessDocument_strategy = st.builds(
    workflow_ProcessDocument,
    name=
        safe_text
)
workflow_GlobalAspect_strategy = st.builds(
    workflow_GlobalAspect,
)
workflow_CoreModel_strategy = st.builds(
    workflow_CoreModel,
    name=
        safe_text
)
workflow_WorkflowEngine_strategy = st.builds(
    workflow_WorkflowEngine,
)
workflow_ModelRegistry_strategy = st.builds(
    workflow_ModelRegistry,
)
workflow_Token_strategy = st.builds(
    workflow_Token,
)
TaskC_strategy = st.builds(
    TaskC,
)
workflow_Transition_strategy = st.builds(
    workflow_Transition,
)
workflow_Place_strategy = st.builds(
    workflow_Place,
    name=
        safe_text
)
workflow_Arc_strategy = st.builds(
    workflow_Arc,
    name=
        safe_text
)
Control_strategy = st.builds(
    Control,
)
workflow_PetriNet_strategy = st.builds(
    workflow_PetriNet,
)
workflow_State_strategy = st.builds(
    workflow_State,
)
CaseAspect_strategy = st.builds(
    CaseAspect,
)
workflow_CaseI_strategy = st.builds(
    workflow_CaseI,
)
workflow_CaseO_strategy = st.builds(
    workflow_CaseO,
)
ProcessAspect_strategy = st.builds(
    ProcessAspect,
)
workflow_Information_strategy = st.builds(
    workflow_Information,
)
workflow_ProcessO_strategy = st.builds(
    workflow_ProcessO,
)
workflow_Control_strategy = st.builds(
    workflow_Control,
)
workflow_CaseC_strategy = st.builds(
    workflow_CaseC,
)
workflow_RuntimeInformation_strategy = st.builds(
    workflow_RuntimeInformation,
    caseIdCount=
        safe_text
)
workflow_Task_strategy = st.builds(
    workflow_Task,
    name=
        safe_text
)
workflow_ActivityAspect_strategy = st.builds(
    workflow_ActivityAspect,
)
workflow_RuntimeCoreModel_strategy = st.builds(
    workflow_RuntimeCoreModel,
)
workflow_Process_strategy = st.builds(
    workflow_Process,
    name=
        safe_text
)
workflow_Activity_strategy = st.builds(
    workflow_Activity,
    finished=
        st.booleans(),
    started=
        st.booleans()
)
workflow_CaseAspect_strategy = st.builds(
    workflow_CaseAspect,
)
workflow_Case_strategy = st.builds(
    workflow_Case,
    id=
        safe_text,
    client=
        safe_text,
    finished=
        st.booleans(),
    started=
        st.booleans()
)
workflow_Agent_strategy = st.builds(
    workflow_Agent,
    username=
        safe_text,
    name=
        safe_text,
    password=
        safe_text
)
ActivityAspect_strategy = st.builds(
    ActivityAspect,
)
workflow_ActivityI_strategy = st.builds(
    workflow_ActivityI,
)
workflow_ActivityC_strategy = st.builds(
    workflow_ActivityC,
)
workflow_ActivityO_strategy = st.builds(
    workflow_ActivityO,
)
workflow_Role_strategy = st.builds(
    workflow_Role,
    name=
        safe_text
)
TaskAspect_strategy = st.builds(
    TaskAspect,
)
workflow_TaskC_strategy = st.builds(
    workflow_TaskC,
    name=
        safe_text
)
workflow_TaskI_strategy = st.builds(
    workflow_TaskI,
)
workflow_TaskO_strategy = st.builds(
    workflow_TaskO,
    name=
        safe_text
)

@given(instance=GlobalAspect_strategy)
@settings(max_examples=50)
def test_globalaspect_instantiation(instance):
    assert isinstance(instance, GlobalAspect)

@given(instance=workflow_DocumentTypeContainer_strategy)
@settings(max_examples=50)
def test_workflow_documenttypecontainer_instantiation(instance):
    assert isinstance(instance, workflow_DocumentTypeContainer)



@given(instance=workflow_DocumentTypeContainer_strategy)
def test_workflow_documenttypecontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Organisation_strategy)
@settings(max_examples=50)
def test_workflow_organisation_instantiation(instance):
    assert isinstance(instance, workflow_Organisation)



@given(instance=workflow_Organisation_strategy)
def test_workflow_organisation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RuntimeGlobalAspect_strategy)
@settings(max_examples=50)
def test_runtimeglobalaspect_instantiation(instance):
    assert isinstance(instance, RuntimeGlobalAspect)

@given(instance=workflow_DocumentContainer_strategy)
@settings(max_examples=50)
def test_workflow_documentcontainer_instantiation(instance):
    assert isinstance(instance, workflow_DocumentContainer)



@given(instance=workflow_DocumentContainer_strategy)
def test_workflow_documentcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_AgentContainer_strategy)
@settings(max_examples=50)
def test_workflow_agentcontainer_instantiation(instance):
    assert isinstance(instance, workflow_AgentContainer)



@given(instance=workflow_AgentContainer_strategy)
def test_workflow_agentcontainer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_EnumLiteral_strategy)
@settings(max_examples=50)
def test_workflow_enumliteral_instantiation(instance):
    assert isinstance(instance, workflow_EnumLiteral)



@given(instance=workflow_EnumLiteral_strategy)
def test_workflow_enumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DocumentCondition_strategy)
@settings(max_examples=50)
def test_documentcondition_instantiation(instance):
    assert isinstance(instance, DocumentCondition)

@given(instance=workflow_DefaultDocumentCondition_strategy)
@settings(max_examples=50)
def test_workflow_defaultdocumentcondition_instantiation(instance):
    assert isinstance(instance, workflow_DefaultDocumentCondition)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=workflow_EqualToOperator_strategy)
@settings(max_examples=50)
def test_workflow_equaltooperator_instantiation(instance):
    assert isinstance(instance, workflow_EqualToOperator)

@given(instance=workflow_UnequalToOperator_strategy)
@settings(max_examples=50)
def test_workflow_unequaltooperator_instantiation(instance):
    assert isinstance(instance, workflow_UnequalToOperator)

@given(instance=workflow_GreaterThanOperator_strategy)
@settings(max_examples=50)
def test_workflow_greaterthanoperator_instantiation(instance):
    assert isinstance(instance, workflow_GreaterThanOperator)

@given(instance=workflow_LessThanOperator_strategy)
@settings(max_examples=50)
def test_workflow_lessthanoperator_instantiation(instance):
    assert isinstance(instance, workflow_LessThanOperator)

@given(instance=workflow_DotOperator_strategy)
@settings(max_examples=50)
def test_workflow_dotoperator_instantiation(instance):
    assert isinstance(instance, workflow_DotOperator)

@given(instance=Atom_strategy)
@settings(max_examples=50)
def test_atom_instantiation(instance):
    assert isinstance(instance, Atom)

@given(instance=workflow_ConstantAtom_strategy)
@settings(max_examples=50)
def test_workflow_constantatom_instantiation(instance):
    assert isinstance(instance, workflow_ConstantAtom)



@given(instance=workflow_ConstantAtom_strategy)
def test_workflow_constantatom_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=workflow_EnumLiteralAtom_strategy)
@settings(max_examples=50)
def test_workflow_enumliteralatom_instantiation(instance):
    assert isinstance(instance, workflow_EnumLiteralAtom)

@given(instance=workflow_FieldAtom_strategy)
@settings(max_examples=50)
def test_workflow_fieldatom_instantiation(instance):
    assert isinstance(instance, workflow_FieldAtom)

@given(instance=workflow_EnumFieldAtom_strategy)
@settings(max_examples=50)
def test_workflow_enumfieldatom_instantiation(instance):
    assert isinstance(instance, workflow_EnumFieldAtom)

@given(instance=workflow_DocumentDescrAtom_strategy)
@settings(max_examples=50)
def test_workflow_documentdescratom_instantiation(instance):
    assert isinstance(instance, workflow_DocumentDescrAtom)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=workflow_Operator_strategy)
@settings(max_examples=50)
def test_workflow_operator_instantiation(instance):
    assert isinstance(instance, workflow_Operator)

@given(instance=workflow_Atom_strategy)
@settings(max_examples=50)
def test_workflow_atom_instantiation(instance):
    assert isinstance(instance, workflow_Atom)

@given(instance=DocumentDescriptor_strategy)
@settings(max_examples=50)
def test_documentdescriptor_instantiation(instance):
    assert isinstance(instance, DocumentDescriptor)

@given(instance=workflow_DefaultDocumentDescriptor_strategy)
@settings(max_examples=50)
def test_workflow_defaultdocumentdescriptor_instantiation(instance):
    assert isinstance(instance, workflow_DefaultDocumentDescriptor)

@given(instance=RuntimeModelAspect_strategy)
@settings(max_examples=50)
def test_runtimemodelaspect_instantiation(instance):
    assert isinstance(instance, RuntimeModelAspect)

@given(instance=workflow_InformationRuntimeAspect_strategy)
@settings(max_examples=50)
def test_workflow_informationruntimeaspect_instantiation(instance):
    assert isinstance(instance, workflow_InformationRuntimeAspect)

@given(instance=workflow_EnumFieldValue_strategy)
@settings(max_examples=50)
def test_workflow_enumfieldvalue_instantiation(instance):
    assert isinstance(instance, workflow_EnumFieldValue)

@given(instance=workflow_FieldValue_strategy)
@settings(max_examples=50)
def test_workflow_fieldvalue_instantiation(instance):
    assert isinstance(instance, workflow_FieldValue)



@given(instance=workflow_FieldValue_strategy)
def test_workflow_fieldvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Document_strategy)
@settings(max_examples=50)
def test_document_instantiation(instance):
    assert isinstance(instance, Document)

@given(instance=workflow_DefaultDocument_strategy)
@settings(max_examples=50)
def test_workflow_defaultdocument_instantiation(instance):
    assert isinstance(instance, workflow_DefaultDocument)



@given(instance=workflow_DefaultDocument_strategy)
def test_workflow_defaultdocument_placeholder_setter(instance):
    original = instance.placeholder
    instance.placeholder = original
    assert instance.placeholder == original

@given(instance=workflow_EnumField_strategy)
@settings(max_examples=50)
def test_workflow_enumfield_instantiation(instance):
    assert isinstance(instance, workflow_EnumField)



@given(instance=workflow_EnumField_strategy)
def test_workflow_enumfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Field_strategy)
@settings(max_examples=50)
def test_workflow_field_instantiation(instance):
    assert isinstance(instance, workflow_Field)



@given(instance=workflow_Field_strategy)
def test_workflow_field_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DocumentType_strategy)
@settings(max_examples=50)
def test_documenttype_instantiation(instance):
    assert isinstance(instance, DocumentType)

@given(instance=workflow_DefaultDocumentType_strategy)
@settings(max_examples=50)
def test_workflow_defaultdocumenttype_instantiation(instance):
    assert isinstance(instance, workflow_DefaultDocumentType)

@given(instance=workflow_Expression_strategy)
@settings(max_examples=50)
def test_workflow_expression_instantiation(instance):
    assert isinstance(instance, workflow_Expression)

@given(instance=workflow_RuntimeGlobalAspect_strategy)
@settings(max_examples=50)
def test_workflow_runtimeglobalaspect_instantiation(instance):
    assert isinstance(instance, workflow_RuntimeGlobalAspect)

@given(instance=ModelAspect_strategy)
@settings(max_examples=50)
def test_modelaspect_instantiation(instance):
    assert isinstance(instance, ModelAspect)

@given(instance=workflow_InformationAspect_strategy)
@settings(max_examples=50)
def test_workflow_informationaspect_instantiation(instance):
    assert isinstance(instance, workflow_InformationAspect)

@given(instance=workflow_ControlAspect_strategy)
@settings(max_examples=50)
def test_workflow_controlaspect_instantiation(instance):
    assert isinstance(instance, workflow_ControlAspect)

@given(instance=workflow_OrganisationAspect_strategy)
@settings(max_examples=50)
def test_workflow_organisationaspect_instantiation(instance):
    assert isinstance(instance, workflow_OrganisationAspect)

@given(instance=workflow_ModelAspect_strategy)
@settings(max_examples=50)
def test_workflow_modelaspect_instantiation(instance):
    assert isinstance(instance, workflow_ModelAspect)

@given(instance=workflow_RuntimeModelAspect_strategy)
@settings(max_examples=50)
def test_workflow_runtimemodelaspect_instantiation(instance):
    assert isinstance(instance, workflow_RuntimeModelAspect)

@given(instance=workflow_TaskAspect_strategy)
@settings(max_examples=50)
def test_workflow_taskaspect_instantiation(instance):
    assert isinstance(instance, workflow_TaskAspect)

@given(instance=workflow_ProcessAspect_strategy)
@settings(max_examples=50)
def test_workflow_processaspect_instantiation(instance):
    assert isinstance(instance, workflow_ProcessAspect)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=workflow_Marking_strategy)
@settings(max_examples=50)
def test_workflow_marking_instantiation(instance):
    assert isinstance(instance, workflow_Marking)

@given(instance=workflow_String2DocumentMap_strategy)
@settings(max_examples=50)
def test_workflow_string2documentmap_instantiation(instance):
    assert isinstance(instance, workflow_String2DocumentMap)



@given(instance=workflow_String2DocumentMap_strategy)
def test_workflow_string2documentmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=workflow_Document_strategy)
@settings(max_examples=50)
def test_workflow_document_instantiation(instance):
    assert isinstance(instance, workflow_Document)



@given(instance=workflow_Document_strategy)
def test_workflow_document_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=workflow_Document_strategy)
def test_workflow_document_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=workflow_DocumentType_strategy)
@settings(max_examples=50)
def test_workflow_documenttype_instantiation(instance):
    assert isinstance(instance, workflow_DocumentType)



@given(instance=workflow_DocumentType_strategy)
def test_workflow_documenttype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_DocumentCondition_strategy)
@settings(max_examples=50)
def test_workflow_documentcondition_instantiation(instance):
    assert isinstance(instance, workflow_DocumentCondition)



@given(instance=workflow_DocumentCondition_strategy)
def test_workflow_documentcondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_DocumentDescriptor_strategy)
@settings(max_examples=50)
def test_workflow_documentdescriptor_instantiation(instance):
    assert isinstance(instance, workflow_DocumentDescriptor)



@given(instance=workflow_DocumentDescriptor_strategy)
def test_workflow_documentdescriptor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_ProcessDocument_strategy)
@settings(max_examples=50)
def test_workflow_processdocument_instantiation(instance):
    assert isinstance(instance, workflow_ProcessDocument)



@given(instance=workflow_ProcessDocument_strategy)
def test_workflow_processdocument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_GlobalAspect_strategy)
@settings(max_examples=50)
def test_workflow_globalaspect_instantiation(instance):
    assert isinstance(instance, workflow_GlobalAspect)

@given(instance=workflow_CoreModel_strategy)
@settings(max_examples=50)
def test_workflow_coremodel_instantiation(instance):
    assert isinstance(instance, workflow_CoreModel)



@given(instance=workflow_CoreModel_strategy)
def test_workflow_coremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_WorkflowEngine_strategy)
@settings(max_examples=50)
def test_workflow_workflowengine_instantiation(instance):
    assert isinstance(instance, workflow_WorkflowEngine)

@given(instance=workflow_ModelRegistry_strategy)
@settings(max_examples=50)
def test_workflow_modelregistry_instantiation(instance):
    assert isinstance(instance, workflow_ModelRegistry)

@given(instance=workflow_Token_strategy)
@settings(max_examples=50)
def test_workflow_token_instantiation(instance):
    assert isinstance(instance, workflow_Token)

@given(instance=TaskC_strategy)
@settings(max_examples=50)
def test_taskc_instantiation(instance):
    assert isinstance(instance, TaskC)

@given(instance=workflow_Transition_strategy)
@settings(max_examples=50)
def test_workflow_transition_instantiation(instance):
    assert isinstance(instance, workflow_Transition)

@given(instance=workflow_Place_strategy)
@settings(max_examples=50)
def test_workflow_place_instantiation(instance):
    assert isinstance(instance, workflow_Place)



@given(instance=workflow_Place_strategy)
def test_workflow_place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Arc_strategy)
@settings(max_examples=50)
def test_workflow_arc_instantiation(instance):
    assert isinstance(instance, workflow_Arc)



@given(instance=workflow_Arc_strategy)
def test_workflow_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Control_strategy)
@settings(max_examples=50)
def test_control_instantiation(instance):
    assert isinstance(instance, Control)

@given(instance=workflow_PetriNet_strategy)
@settings(max_examples=50)
def test_workflow_petrinet_instantiation(instance):
    assert isinstance(instance, workflow_PetriNet)

@given(instance=workflow_State_strategy)
@settings(max_examples=50)
def test_workflow_state_instantiation(instance):
    assert isinstance(instance, workflow_State)

@given(instance=CaseAspect_strategy)
@settings(max_examples=50)
def test_caseaspect_instantiation(instance):
    assert isinstance(instance, CaseAspect)

@given(instance=workflow_CaseI_strategy)
@settings(max_examples=50)
def test_workflow_casei_instantiation(instance):
    assert isinstance(instance, workflow_CaseI)

@given(instance=workflow_CaseO_strategy)
@settings(max_examples=50)
def test_workflow_caseo_instantiation(instance):
    assert isinstance(instance, workflow_CaseO)

@given(instance=ProcessAspect_strategy)
@settings(max_examples=50)
def test_processaspect_instantiation(instance):
    assert isinstance(instance, ProcessAspect)

@given(instance=workflow_Information_strategy)
@settings(max_examples=50)
def test_workflow_information_instantiation(instance):
    assert isinstance(instance, workflow_Information)

@given(instance=workflow_ProcessO_strategy)
@settings(max_examples=50)
def test_workflow_processo_instantiation(instance):
    assert isinstance(instance, workflow_ProcessO)

@given(instance=workflow_Control_strategy)
@settings(max_examples=50)
def test_workflow_control_instantiation(instance):
    assert isinstance(instance, workflow_Control)

@given(instance=workflow_CaseC_strategy)
@settings(max_examples=50)
def test_workflow_casec_instantiation(instance):
    assert isinstance(instance, workflow_CaseC)

@given(instance=workflow_RuntimeInformation_strategy)
@settings(max_examples=50)
def test_workflow_runtimeinformation_instantiation(instance):
    assert isinstance(instance, workflow_RuntimeInformation)



@given(instance=workflow_RuntimeInformation_strategy)
def test_workflow_runtimeinformation_caseIdCount_setter(instance):
    original = instance.caseIdCount
    instance.caseIdCount = original
    assert instance.caseIdCount == original

@given(instance=workflow_Task_strategy)
@settings(max_examples=50)
def test_workflow_task_instantiation(instance):
    assert isinstance(instance, workflow_Task)



@given(instance=workflow_Task_strategy)
def test_workflow_task_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_ActivityAspect_strategy)
@settings(max_examples=50)
def test_workflow_activityaspect_instantiation(instance):
    assert isinstance(instance, workflow_ActivityAspect)

@given(instance=workflow_RuntimeCoreModel_strategy)
@settings(max_examples=50)
def test_workflow_runtimecoremodel_instantiation(instance):
    assert isinstance(instance, workflow_RuntimeCoreModel)

@given(instance=workflow_Process_strategy)
@settings(max_examples=50)
def test_workflow_process_instantiation(instance):
    assert isinstance(instance, workflow_Process)



@given(instance=workflow_Process_strategy)
def test_workflow_process_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Activity_strategy)
@settings(max_examples=50)
def test_workflow_activity_instantiation(instance):
    assert isinstance(instance, workflow_Activity)



@given(instance=workflow_Activity_strategy)
def test_workflow_activity_finished_setter(instance):
    original = instance.finished
    instance.finished = original
    assert instance.finished == original



@given(instance=workflow_Activity_strategy)
def test_workflow_activity_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original

@given(instance=workflow_CaseAspect_strategy)
@settings(max_examples=50)
def test_workflow_caseaspect_instantiation(instance):
    assert isinstance(instance, workflow_CaseAspect)

@given(instance=workflow_Case_strategy)
@settings(max_examples=50)
def test_workflow_case_instantiation(instance):
    assert isinstance(instance, workflow_Case)



@given(instance=workflow_Case_strategy)
def test_workflow_case_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=workflow_Case_strategy)
def test_workflow_case_client_setter(instance):
    original = instance.client
    instance.client = original
    assert instance.client == original



@given(instance=workflow_Case_strategy)
def test_workflow_case_finished_setter(instance):
    original = instance.finished
    instance.finished = original
    assert instance.finished == original



@given(instance=workflow_Case_strategy)
def test_workflow_case_started_setter(instance):
    original = instance.started
    instance.started = original
    assert instance.started == original

@given(instance=workflow_Agent_strategy)
@settings(max_examples=50)
def test_workflow_agent_instantiation(instance):
    assert isinstance(instance, workflow_Agent)



@given(instance=workflow_Agent_strategy)
def test_workflow_agent_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=workflow_Agent_strategy)
def test_workflow_agent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=workflow_Agent_strategy)
def test_workflow_agent_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=ActivityAspect_strategy)
@settings(max_examples=50)
def test_activityaspect_instantiation(instance):
    assert isinstance(instance, ActivityAspect)

@given(instance=workflow_ActivityI_strategy)
@settings(max_examples=50)
def test_workflow_activityi_instantiation(instance):
    assert isinstance(instance, workflow_ActivityI)

@given(instance=workflow_ActivityC_strategy)
@settings(max_examples=50)
def test_workflow_activityc_instantiation(instance):
    assert isinstance(instance, workflow_ActivityC)

@given(instance=workflow_ActivityO_strategy)
@settings(max_examples=50)
def test_workflow_activityo_instantiation(instance):
    assert isinstance(instance, workflow_ActivityO)

@given(instance=workflow_Role_strategy)
@settings(max_examples=50)
def test_workflow_role_instantiation(instance):
    assert isinstance(instance, workflow_Role)



@given(instance=workflow_Role_strategy)
def test_workflow_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TaskAspect_strategy)
@settings(max_examples=50)
def test_taskaspect_instantiation(instance):
    assert isinstance(instance, TaskAspect)

@given(instance=workflow_TaskC_strategy)
@settings(max_examples=50)
def test_workflow_taskc_instantiation(instance):
    assert isinstance(instance, workflow_TaskC)



@given(instance=workflow_TaskC_strategy)
def test_workflow_taskc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_TaskI_strategy)
@settings(max_examples=50)
def test_workflow_taski_instantiation(instance):
    assert isinstance(instance, workflow_TaskI)

@given(instance=workflow_TaskO_strategy)
@settings(max_examples=50)
def test_workflow_tasko_instantiation(instance):
    assert isinstance(instance, workflow_TaskO)



@given(instance=workflow_TaskO_strategy)
def test_workflow_tasko_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
