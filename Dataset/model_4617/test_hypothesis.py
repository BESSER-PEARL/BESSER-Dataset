import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_OnoObject,
    Diagram,
    model_DomainDiagram,
    ReifiableTopicType,
    AbstractUniqueValueTopicType,
    AbstractRegExpTopicType,
    ScopedReifiableTopicType,
    ScopedTopicType,
    model_ScopedReifiableTopicType,
    model_NameType,
    model_OccurrenceType,
    model_AssociationType,
    TopicType,
    model_AbstractUniqueValueTopicType,
    model_AbstractRegExpTopicType,
    model_ReifiableTopicType,
    model_ScopedTopicType,
    model_RoleType,
    Node,
    model_Comment,
    model_TypeNode,
    OnoObject,
    model_Bendpoint,
    model_LabelPos,
    model_TMCLConstruct,
    model_Node,
    model_Edge,
    model_Annotation,
    model_File,
    model_Diagram,
    AbstractTypedConstraint,
    model_AssociationNode,
    model_MappingElement,
    model_AssociationTypeConstraint,
    AbstractCardinalityConstraint,
    model_AbstractTypedCardinalityConstraint,
    model_RolePlayerConstraint,
    AbstractTypedCardinalityConstraint,
    model_ReifierConstraint,
    model_ScopeConstraint,
    model_OccurrenceTypeConstraint,
    model_NameTypeConstraint,
    model_RoleConstraint,
    AbstractConstraint,
    model_RoleCombinationConstraint,
    model_AbstractTypedConstraint,
    model_AbstractCardinalityConstraint,
    model_AbstractRegExpConstraint,
    model_TopicReifiesConstraint,
    AbstractRegExpConstraint,
    model_SubjectIdentifierConstraint,
    model_SubjectLocatorConstraint,
    model_ItemIdentifierConstraint,
    TMCLConstruct,
    model_AbstractConstraint,
    model_TopicMapSchema,
    model_TopicType,
    TopicId,
    KindOfTopicType,
    EdgeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_onoobject_is_not_abstract():
    assert not inspect.isabstract(model_OnoObject)


def test_model_onoobject_constructor_exists():
    assert callable(model_OnoObject.__init__)


def test_model_onoobject_constructor_args():
    sig = inspect.signature(model_OnoObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model_onoobject_has_id():
    assert hasattr(model_OnoObject, "id")
    descriptor = None
    for klass in model_OnoObject.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_diagram_is_not_abstract():
    assert not inspect.isabstract(Diagram)


def test_diagram_constructor_exists():
    assert callable(Diagram.__init__)


def test_diagram_constructor_args():
    sig = inspect.signature(Diagram.__init__)
    params = list(sig.parameters.keys())



def test_model_domaindiagram_is_not_abstract():
    assert not inspect.isabstract(model_DomainDiagram)


def test_model_domaindiagram_constructor_exists():
    assert callable(model_DomainDiagram.__init__)


def test_model_domaindiagram_constructor_args():
    sig = inspect.signature(model_DomainDiagram.__init__)
    params = list(sig.parameters.keys())



def test_reifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(ReifiableTopicType)


def test_reifiabletopictype_constructor_exists():
    assert callable(ReifiableTopicType.__init__)


def test_reifiabletopictype_constructor_args():
    sig = inspect.signature(ReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_abstractuniquevaluetopictype_is_not_abstract():
    assert not inspect.isabstract(AbstractUniqueValueTopicType)


def test_abstractuniquevaluetopictype_constructor_exists():
    assert callable(AbstractUniqueValueTopicType.__init__)


def test_abstractuniquevaluetopictype_constructor_args():
    sig = inspect.signature(AbstractUniqueValueTopicType.__init__)
    params = list(sig.parameters.keys())



def test_abstractregexptopictype_is_not_abstract():
    assert not inspect.isabstract(AbstractRegExpTopicType)


def test_abstractregexptopictype_constructor_exists():
    assert callable(AbstractRegExpTopicType.__init__)


def test_abstractregexptopictype_constructor_args():
    sig = inspect.signature(AbstractRegExpTopicType.__init__)
    params = list(sig.parameters.keys())



def test_scopedreifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(ScopedReifiableTopicType)


def test_scopedreifiabletopictype_constructor_exists():
    assert callable(ScopedReifiableTopicType.__init__)


def test_scopedreifiabletopictype_constructor_args():
    sig = inspect.signature(ScopedReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_scopedtopictype_is_not_abstract():
    assert not inspect.isabstract(ScopedTopicType)


def test_scopedtopictype_constructor_exists():
    assert callable(ScopedTopicType.__init__)


def test_scopedtopictype_constructor_args():
    sig = inspect.signature(ScopedTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model_scopedreifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(model_ScopedReifiableTopicType)


def test_model_scopedreifiabletopictype_constructor_exists():
    assert callable(model_ScopedReifiableTopicType.__init__)


def test_model_scopedreifiabletopictype_constructor_args():
    sig = inspect.signature(model_ScopedReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model_nametype_is_not_abstract():
    assert not inspect.isabstract(model_NameType)


def test_model_nametype_constructor_exists():
    assert callable(model_NameType.__init__)


def test_model_nametype_constructor_args():
    sig = inspect.signature(model_NameType.__init__)
    params = list(sig.parameters.keys())



def test_model_occurrencetype_is_not_abstract():
    assert not inspect.isabstract(model_OccurrenceType)


def test_model_occurrencetype_constructor_exists():
    assert callable(model_OccurrenceType.__init__)


def test_model_occurrencetype_constructor_args():
    sig = inspect.signature(model_OccurrenceType.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_model_occurrencetype_has_dataType():
    assert hasattr(model_OccurrenceType, "dataType")
    descriptor = None
    for klass in model_OccurrenceType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_model_associationtype_is_not_abstract():
    assert not inspect.isabstract(model_AssociationType)


def test_model_associationtype_constructor_exists():
    assert callable(model_AssociationType.__init__)


def test_model_associationtype_constructor_args():
    sig = inspect.signature(model_AssociationType.__init__)
    params = list(sig.parameters.keys())



def test_topictype_is_not_abstract():
    assert not inspect.isabstract(TopicType)


def test_topictype_constructor_exists():
    assert callable(TopicType.__init__)


def test_topictype_constructor_args():
    sig = inspect.signature(TopicType.__init__)
    params = list(sig.parameters.keys())



def test_model_abstractuniquevaluetopictype_is_not_abstract():
    assert not inspect.isabstract(model_AbstractUniqueValueTopicType)


def test_model_abstractuniquevaluetopictype_constructor_exists():
    assert callable(model_AbstractUniqueValueTopicType.__init__)


def test_model_abstractuniquevaluetopictype_constructor_args():
    sig = inspect.signature(model_AbstractUniqueValueTopicType.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_model_abstractuniquevaluetopictype_has_unique():
    assert hasattr(model_AbstractUniqueValueTopicType, "unique")
    descriptor = None
    for klass in model_AbstractUniqueValueTopicType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_model_abstractregexptopictype_is_not_abstract():
    assert not inspect.isabstract(model_AbstractRegExpTopicType)


def test_model_abstractregexptopictype_constructor_exists():
    assert callable(model_AbstractRegExpTopicType.__init__)


def test_model_abstractregexptopictype_constructor_args():
    sig = inspect.signature(model_AbstractRegExpTopicType.__init__)
    params = list(sig.parameters.keys())
    assert "regExp" in params, "Missing parameter 'regExp'"

def test_model_abstractregexptopictype_has_regExp():
    assert hasattr(model_AbstractRegExpTopicType, "regExp")
    descriptor = None
    for klass in model_AbstractRegExpTopicType.__mro__:
        if "regExp" in klass.__dict__:
            descriptor = klass.__dict__["regExp"]
            break
    assert isinstance(descriptor, property)



def test_model_reifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(model_ReifiableTopicType)


def test_model_reifiabletopictype_constructor_exists():
    assert callable(model_ReifiableTopicType.__init__)


def test_model_reifiabletopictype_constructor_args():
    sig = inspect.signature(model_ReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model_scopedtopictype_is_not_abstract():
    assert not inspect.isabstract(model_ScopedTopicType)


def test_model_scopedtopictype_constructor_exists():
    assert callable(model_ScopedTopicType.__init__)


def test_model_scopedtopictype_constructor_args():
    sig = inspect.signature(model_ScopedTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model_roletype_is_not_abstract():
    assert not inspect.isabstract(model_RoleType)


def test_model_roletype_constructor_exists():
    assert callable(model_RoleType.__init__)


def test_model_roletype_constructor_args():
    sig = inspect.signature(model_RoleType.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model_comment_is_not_abstract():
    assert not inspect.isabstract(model_Comment)


def test_model_comment_constructor_exists():
    assert callable(model_Comment.__init__)


def test_model_comment_constructor_args():
    sig = inspect.signature(model_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "content" in params, "Missing parameter 'content'"

def test_model_comment_has_width():
    assert hasattr(model_Comment, "width")
    descriptor = None
    for klass in model_Comment.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model_comment_has_height():
    assert hasattr(model_Comment, "height")
    descriptor = None
    for klass in model_Comment.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model_comment_has_content():
    assert hasattr(model_Comment, "content")
    descriptor = None
    for klass in model_Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_model_typenode_is_not_abstract():
    assert not inspect.isabstract(model_TypeNode)


def test_model_typenode_constructor_exists():
    assert callable(model_TypeNode.__init__)


def test_model_typenode_constructor_args():
    sig = inspect.signature(model_TypeNode.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_model_typenode_has_image():
    assert hasattr(model_TypeNode, "image")
    descriptor = None
    for klass in model_TypeNode.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)



def test_onoobject_is_not_abstract():
    assert not inspect.isabstract(OnoObject)


def test_onoobject_constructor_exists():
    assert callable(OnoObject.__init__)


def test_onoobject_constructor_args():
    sig = inspect.signature(OnoObject.__init__)
    params = list(sig.parameters.keys())



def test_model_bendpoint_is_not_abstract():
    assert not inspect.isabstract(model_Bendpoint)


def test_model_bendpoint_constructor_exists():
    assert callable(model_Bendpoint.__init__)


def test_model_bendpoint_constructor_args():
    sig = inspect.signature(model_Bendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "posY" in params, "Missing parameter 'posY'"
    assert "posX" in params, "Missing parameter 'posX'"

def test_model_bendpoint_has_posY():
    assert hasattr(model_Bendpoint, "posY")
    descriptor = None
    for klass in model_Bendpoint.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)

def test_model_bendpoint_has_posX():
    assert hasattr(model_Bendpoint, "posX")
    descriptor = None
    for klass in model_Bendpoint.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)



def test_model_labelpos_is_not_abstract():
    assert not inspect.isabstract(model_LabelPos)


def test_model_labelpos_constructor_exists():
    assert callable(model_LabelPos.__init__)


def test_model_labelpos_constructor_args():
    sig = inspect.signature(model_LabelPos.__init__)
    params = list(sig.parameters.keys())
    assert "posX" in params, "Missing parameter 'posX'"
    assert "posY" in params, "Missing parameter 'posY'"

def test_model_labelpos_has_posX():
    assert hasattr(model_LabelPos, "posX")
    descriptor = None
    for klass in model_LabelPos.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)

def test_model_labelpos_has_posY():
    assert hasattr(model_LabelPos, "posY")
    descriptor = None
    for klass in model_LabelPos.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)



def test_model_tmclconstruct_is_not_abstract():
    assert not inspect.isabstract(model_TMCLConstruct)


def test_model_tmclconstruct_constructor_exists():
    assert callable(model_TMCLConstruct.__init__)


def test_model_tmclconstruct_constructor_args():
    sig = inspect.signature(model_TMCLConstruct.__init__)
    params = list(sig.parameters.keys())
    assert "see_also" in params, "Missing parameter 'see_also'"
    assert "description" in params, "Missing parameter 'description'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_model_tmclconstruct_has_see_also():
    assert hasattr(model_TMCLConstruct, "see_also")
    descriptor = None
    for klass in model_TMCLConstruct.__mro__:
        if "see_also" in klass.__dict__:
            descriptor = klass.__dict__["see_also"]
            break
    assert isinstance(descriptor, property)

def test_model_tmclconstruct_has_description():
    assert hasattr(model_TMCLConstruct, "description")
    descriptor = None
    for klass in model_TMCLConstruct.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_model_tmclconstruct_has_comment():
    assert hasattr(model_TMCLConstruct, "comment")
    descriptor = None
    for klass in model_TMCLConstruct.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_model_node_is_not_abstract():
    assert not inspect.isabstract(model_Node)


def test_model_node_constructor_exists():
    assert callable(model_Node.__init__)


def test_model_node_constructor_args():
    sig = inspect.signature(model_Node.__init__)
    params = list(sig.parameters.keys())
    assert "posY" in params, "Missing parameter 'posY'"
    assert "posX" in params, "Missing parameter 'posX'"

def test_model_node_has_posY():
    assert hasattr(model_Node, "posY")
    descriptor = None
    for klass in model_Node.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)

def test_model_node_has_posX():
    assert hasattr(model_Node, "posX")
    descriptor = None
    for klass in model_Node.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)



def test_model_edge_is_not_abstract():
    assert not inspect.isabstract(model_Edge)


def test_model_edge_constructor_exists():
    assert callable(model_Edge.__init__)


def test_model_edge_constructor_args():
    sig = inspect.signature(model_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model_edge_has_type():
    assert hasattr(model_Edge, "type")
    descriptor = None
    for klass in model_Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model_annotation_is_not_abstract():
    assert not inspect.isabstract(model_Annotation)


def test_model_annotation_constructor_exists():
    assert callable(model_Annotation.__init__)


def test_model_annotation_constructor_args():
    sig = inspect.signature(model_Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_model_annotation_has_key():
    assert hasattr(model_Annotation, "key")
    descriptor = None
    for klass in model_Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_model_annotation_has_value():
    assert hasattr(model_Annotation, "value")
    descriptor = None
    for klass in model_Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_file_is_not_abstract():
    assert not inspect.isabstract(model_File)


def test_model_file_constructor_exists():
    assert callable(model_File.__init__)


def test_model_file_constructor_args():
    sig = inspect.signature(model_File.__init__)
    params = list(sig.parameters.keys())
    assert "filename" in params, "Missing parameter 'filename'"
    assert "notes" in params, "Missing parameter 'notes'"
    assert "dirty" in params, "Missing parameter 'dirty'"

def test_model_file_has_filename():
    assert hasattr(model_File, "filename")
    descriptor = None
    for klass in model_File.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_model_file_has_notes():
    assert hasattr(model_File, "notes")
    descriptor = None
    for klass in model_File.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)

def test_model_file_has_dirty():
    assert hasattr(model_File, "dirty")
    descriptor = None
    for klass in model_File.__mro__:
        if "dirty" in klass.__dict__:
            descriptor = klass.__dict__["dirty"]
            break
    assert isinstance(descriptor, property)



def test_model_diagram_is_not_abstract():
    assert not inspect.isabstract(model_Diagram)


def test_model_diagram_constructor_exists():
    assert callable(model_Diagram.__init__)


def test_model_diagram_constructor_args():
    sig = inspect.signature(model_Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_diagram_has_name():
    assert hasattr(model_Diagram, "name")
    descriptor = None
    for klass in model_Diagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_abstracttypedconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractTypedConstraint)


def test_abstracttypedconstraint_constructor_exists():
    assert callable(AbstractTypedConstraint.__init__)


def test_abstracttypedconstraint_constructor_args():
    sig = inspect.signature(AbstractTypedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_associationnode_is_not_abstract():
    assert not inspect.isabstract(model_AssociationNode)


def test_model_associationnode_constructor_exists():
    assert callable(model_AssociationNode.__init__)


def test_model_associationnode_constructor_args():
    sig = inspect.signature(model_AssociationNode.__init__)
    params = list(sig.parameters.keys())



def test_model_mappingelement_is_not_abstract():
    assert not inspect.isabstract(model_MappingElement)


def test_model_mappingelement_constructor_exists():
    assert callable(model_MappingElement.__init__)


def test_model_mappingelement_constructor_args():
    sig = inspect.signature(model_MappingElement.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_model_mappingelement_has_key():
    assert hasattr(model_MappingElement, "key")
    descriptor = None
    for klass in model_MappingElement.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_model_mappingelement_has_value():
    assert hasattr(model_MappingElement, "value")
    descriptor = None
    for klass in model_MappingElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_model_associationtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AssociationTypeConstraint)


def test_model_associationtypeconstraint_constructor_exists():
    assert callable(model_AssociationTypeConstraint.__init__)


def test_model_associationtypeconstraint_constructor_args():
    sig = inspect.signature(model_AssociationTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractCardinalityConstraint)


def test_abstractcardinalityconstraint_constructor_exists():
    assert callable(AbstractCardinalityConstraint.__init__)


def test_abstractcardinalityconstraint_constructor_args():
    sig = inspect.signature(AbstractCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_abstracttypedcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AbstractTypedCardinalityConstraint)


def test_model_abstracttypedcardinalityconstraint_constructor_exists():
    assert callable(model_AbstractTypedCardinalityConstraint.__init__)


def test_model_abstracttypedcardinalityconstraint_constructor_args():
    sig = inspect.signature(model_AbstractTypedCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_roleplayerconstraint_is_not_abstract():
    assert not inspect.isabstract(model_RolePlayerConstraint)


def test_model_roleplayerconstraint_constructor_exists():
    assert callable(model_RolePlayerConstraint.__init__)


def test_model_roleplayerconstraint_constructor_args():
    sig = inspect.signature(model_RolePlayerConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractTypedCardinalityConstraint)


def test_abstracttypedcardinalityconstraint_constructor_exists():
    assert callable(AbstractTypedCardinalityConstraint.__init__)


def test_abstracttypedcardinalityconstraint_constructor_args():
    sig = inspect.signature(AbstractTypedCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_reifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model_ReifierConstraint)


def test_model_reifierconstraint_constructor_exists():
    assert callable(model_ReifierConstraint.__init__)


def test_model_reifierconstraint_constructor_args():
    sig = inspect.signature(model_ReifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_scopeconstraint_is_not_abstract():
    assert not inspect.isabstract(model_ScopeConstraint)


def test_model_scopeconstraint_constructor_exists():
    assert callable(model_ScopeConstraint.__init__)


def test_model_scopeconstraint_constructor_args():
    sig = inspect.signature(model_ScopeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_occurrencetypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model_OccurrenceTypeConstraint)


def test_model_occurrencetypeconstraint_constructor_exists():
    assert callable(model_OccurrenceTypeConstraint.__init__)


def test_model_occurrencetypeconstraint_constructor_args():
    sig = inspect.signature(model_OccurrenceTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_nametypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model_NameTypeConstraint)


def test_model_nametypeconstraint_constructor_exists():
    assert callable(model_NameTypeConstraint.__init__)


def test_model_nametypeconstraint_constructor_args():
    sig = inspect.signature(model_NameTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_roleconstraint_is_not_abstract():
    assert not inspect.isabstract(model_RoleConstraint)


def test_model_roleconstraint_constructor_exists():
    assert callable(model_RoleConstraint.__init__)


def test_model_roleconstraint_constructor_args():
    sig = inspect.signature(model_RoleConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractConstraint)


def test_abstractconstraint_constructor_exists():
    assert callable(AbstractConstraint.__init__)


def test_abstractconstraint_constructor_args():
    sig = inspect.signature(AbstractConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_rolecombinationconstraint_is_not_abstract():
    assert not inspect.isabstract(model_RoleCombinationConstraint)


def test_model_rolecombinationconstraint_constructor_exists():
    assert callable(model_RoleCombinationConstraint.__init__)


def test_model_rolecombinationconstraint_constructor_args():
    sig = inspect.signature(model_RoleCombinationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_abstracttypedconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AbstractTypedConstraint)


def test_model_abstracttypedconstraint_constructor_exists():
    assert callable(model_AbstractTypedConstraint.__init__)


def test_model_abstracttypedconstraint_constructor_args():
    sig = inspect.signature(model_AbstractTypedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_abstractcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AbstractCardinalityConstraint)


def test_model_abstractcardinalityconstraint_constructor_exists():
    assert callable(model_AbstractCardinalityConstraint.__init__)


def test_model_abstractcardinalityconstraint_constructor_args():
    sig = inspect.signature(model_AbstractCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "cardMax" in params, "Missing parameter 'cardMax'"
    assert "cardMin" in params, "Missing parameter 'cardMin'"

def test_model_abstractcardinalityconstraint_has_cardMax():
    assert hasattr(model_AbstractCardinalityConstraint, "cardMax")
    descriptor = None
    for klass in model_AbstractCardinalityConstraint.__mro__:
        if "cardMax" in klass.__dict__:
            descriptor = klass.__dict__["cardMax"]
            break
    assert isinstance(descriptor, property)

def test_model_abstractcardinalityconstraint_has_cardMin():
    assert hasattr(model_AbstractCardinalityConstraint, "cardMin")
    descriptor = None
    for klass in model_AbstractCardinalityConstraint.__mro__:
        if "cardMin" in klass.__dict__:
            descriptor = klass.__dict__["cardMin"]
            break
    assert isinstance(descriptor, property)



def test_model_abstractregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AbstractRegExpConstraint)


def test_model_abstractregexpconstraint_constructor_exists():
    assert callable(model_AbstractRegExpConstraint.__init__)


def test_model_abstractregexpconstraint_constructor_args():
    sig = inspect.signature(model_AbstractRegExpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "regexp" in params, "Missing parameter 'regexp'"

def test_model_abstractregexpconstraint_has_regexp():
    assert hasattr(model_AbstractRegExpConstraint, "regexp")
    descriptor = None
    for klass in model_AbstractRegExpConstraint.__mro__:
        if "regexp" in klass.__dict__:
            descriptor = klass.__dict__["regexp"]
            break
    assert isinstance(descriptor, property)



def test_model_topicreifiesconstraint_is_not_abstract():
    assert not inspect.isabstract(model_TopicReifiesConstraint)


def test_model_topicreifiesconstraint_constructor_exists():
    assert callable(model_TopicReifiesConstraint.__init__)


def test_model_topicreifiesconstraint_constructor_args():
    sig = inspect.signature(model_TopicReifiesConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractRegExpConstraint)


def test_abstractregexpconstraint_constructor_exists():
    assert callable(AbstractRegExpConstraint.__init__)


def test_abstractregexpconstraint_constructor_args():
    sig = inspect.signature(AbstractRegExpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_subjectidentifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model_SubjectIdentifierConstraint)


def test_model_subjectidentifierconstraint_constructor_exists():
    assert callable(model_SubjectIdentifierConstraint.__init__)


def test_model_subjectidentifierconstraint_constructor_args():
    sig = inspect.signature(model_SubjectIdentifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_subjectlocatorconstraint_is_not_abstract():
    assert not inspect.isabstract(model_SubjectLocatorConstraint)


def test_model_subjectlocatorconstraint_constructor_exists():
    assert callable(model_SubjectLocatorConstraint.__init__)


def test_model_subjectlocatorconstraint_constructor_args():
    sig = inspect.signature(model_SubjectLocatorConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_itemidentifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model_ItemIdentifierConstraint)


def test_model_itemidentifierconstraint_constructor_exists():
    assert callable(model_ItemIdentifierConstraint.__init__)


def test_model_itemidentifierconstraint_constructor_args():
    sig = inspect.signature(model_ItemIdentifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tmclconstruct_is_not_abstract():
    assert not inspect.isabstract(TMCLConstruct)


def test_tmclconstruct_constructor_exists():
    assert callable(TMCLConstruct.__init__)


def test_tmclconstruct_constructor_args():
    sig = inspect.signature(TMCLConstruct.__init__)
    params = list(sig.parameters.keys())



def test_model_abstractconstraint_is_not_abstract():
    assert not inspect.isabstract(model_AbstractConstraint)


def test_model_abstractconstraint_constructor_exists():
    assert callable(model_AbstractConstraint.__init__)


def test_model_abstractconstraint_constructor_args():
    sig = inspect.signature(model_AbstractConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model_topicmapschema_is_not_abstract():
    assert not inspect.isabstract(model_TopicMapSchema)


def test_model_topicmapschema_constructor_exists():
    assert callable(model_TopicMapSchema.__init__)


def test_model_topicmapschema_constructor_args():
    sig = inspect.signature(model_TopicMapSchema.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "baseLocator" in params, "Missing parameter 'baseLocator'"
    assert "name" in params, "Missing parameter 'name'"
    assert "schemaResource" in params, "Missing parameter 'schemaResource'"

def test_model_topicmapschema_has_version():
    assert hasattr(model_TopicMapSchema, "version")
    descriptor = None
    for klass in model_TopicMapSchema.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_model_topicmapschema_has_includes():
    assert hasattr(model_TopicMapSchema, "includes")
    descriptor = None
    for klass in model_TopicMapSchema.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_model_topicmapschema_has_baseLocator():
    assert hasattr(model_TopicMapSchema, "baseLocator")
    descriptor = None
    for klass in model_TopicMapSchema.__mro__:
        if "baseLocator" in klass.__dict__:
            descriptor = klass.__dict__["baseLocator"]
            break
    assert isinstance(descriptor, property)

def test_model_topicmapschema_has_name():
    assert hasattr(model_TopicMapSchema, "name")
    descriptor = None
    for klass in model_TopicMapSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_topicmapschema_has_schemaResource():
    assert hasattr(model_TopicMapSchema, "schemaResource")
    descriptor = None
    for klass in model_TopicMapSchema.__mro__:
        if "schemaResource" in klass.__dict__:
            descriptor = klass.__dict__["schemaResource"]
            break
    assert isinstance(descriptor, property)



def test_model_topictype_is_not_abstract():
    assert not inspect.isabstract(model_TopicType)


def test_model_topictype_constructor_exists():
    assert callable(model_TopicType.__init__)


def test_model_topictype_constructor_args():
    sig = inspect.signature(model_TopicType.__init__)
    params = list(sig.parameters.keys())
    assert "locators" in params, "Missing parameter 'locators'"
    assert "idType" in params, "Missing parameter 'idType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "identifiers" in params, "Missing parameter 'identifiers'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_model_topictype_has_locators():
    assert hasattr(model_TopicType, "locators")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "locators" in klass.__dict__:
            descriptor = klass.__dict__["locators"]
            break
    assert isinstance(descriptor, property)

def test_model_topictype_has_idType():
    assert hasattr(model_TopicType, "idType")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "idType" in klass.__dict__:
            descriptor = klass.__dict__["idType"]
            break
    assert isinstance(descriptor, property)

def test_model_topictype_has_name():
    assert hasattr(model_TopicType, "name")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_topictype_has_identifiers():
    assert hasattr(model_TopicType, "identifiers")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)

def test_model_topictype_has_abstract():
    assert hasattr(model_TopicType, "abstract")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_model_topictype_has_kind():
    assert hasattr(model_TopicType, "kind")
    descriptor = None
    for klass in model_TopicType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_topicid_exists():
    # Check that the Enumeration exists
    assert TopicId is not None

def test_topicid_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TopicId]
    expected_literals = [
        "SUBJECT_IDENTIFIER",
        "SUBJECT_LOCATOR",
        "IDENTIFIER",
        "ITEM_IDENTIFIER",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TopicId"

def test_kindoftopictype_exists():
    # Check that the Enumeration exists
    assert KindOfTopicType is not None

def test_kindoftopictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindOfTopicType]
    expected_literals = [
        "OccurrenceType",
        "RoleType",
        "ScopeType",
        "TopicType",
        "AssociationType",
        "NameType",
        "NoType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindOfTopicType"

def test_edgetype_exists():
    # Check that the Enumeration exists
    assert EdgeType is not None

def test_edgetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeType]
    expected_literals = [
        "AKO_TYPE",
        "IS_ATYPE",
        "ROLE_CONSTRAINT_TYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeType"


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
model_OnoObject_strategy = st.builds(
    model_OnoObject,
    id=
        st.integers()
)
Diagram_strategy = st.builds(
    Diagram,
)
model_DomainDiagram_strategy = st.builds(
    model_DomainDiagram,
)
ReifiableTopicType_strategy = st.builds(
    ReifiableTopicType,
)
AbstractUniqueValueTopicType_strategy = st.builds(
    AbstractUniqueValueTopicType,
)
AbstractRegExpTopicType_strategy = st.builds(
    AbstractRegExpTopicType,
)
ScopedReifiableTopicType_strategy = st.builds(
    ScopedReifiableTopicType,
)
ScopedTopicType_strategy = st.builds(
    ScopedTopicType,
)
model_ScopedReifiableTopicType_strategy = st.builds(
    model_ScopedReifiableTopicType,
)
model_NameType_strategy = st.builds(
    model_NameType,
)
model_OccurrenceType_strategy = st.builds(
    model_OccurrenceType,
    dataType=
        safe_text
)
model_AssociationType_strategy = st.builds(
    model_AssociationType,
)
TopicType_strategy = st.builds(
    TopicType,
)
model_AbstractUniqueValueTopicType_strategy = st.builds(
    model_AbstractUniqueValueTopicType,
    unique=
        st.booleans()
)
model_AbstractRegExpTopicType_strategy = st.builds(
    model_AbstractRegExpTopicType,
    regExp=
        safe_text
)
model_ReifiableTopicType_strategy = st.builds(
    model_ReifiableTopicType,
)
model_ScopedTopicType_strategy = st.builds(
    model_ScopedTopicType,
)
model_RoleType_strategy = st.builds(
    model_RoleType,
)
Node_strategy = st.builds(
    Node,
)
model_Comment_strategy = st.builds(
    model_Comment,
    width=
        st.integers(),
    height=
        st.integers(),
    content=
        safe_text
)
model_TypeNode_strategy = st.builds(
    model_TypeNode,
    image=
        safe_text
)
OnoObject_strategy = st.builds(
    OnoObject,
)
model_Bendpoint_strategy = st.builds(
    model_Bendpoint,
    posY=
        st.integers(),
    posX=
        st.integers()
)
model_LabelPos_strategy = st.builds(
    model_LabelPos,
    posX=
        st.integers(),
    posY=
        st.integers()
)
model_TMCLConstruct_strategy = st.builds(
    model_TMCLConstruct,
    see_also=
        safe_text,
    description=
        safe_text,
    comment=
        safe_text
)
model_Node_strategy = st.builds(
    model_Node,
    posY=
        st.integers(),
    posX=
        st.integers()
)
model_Edge_strategy = st.builds(
    model_Edge,
    type=
        safe_text
)
model_Annotation_strategy = st.builds(
    model_Annotation,
    key=
        safe_text,
    value=
        safe_text
)
model_File_strategy = st.builds(
    model_File,
    filename=
        safe_text,
    notes=
        safe_text,
    dirty=
        st.booleans()
)
model_Diagram_strategy = st.builds(
    model_Diagram,
    name=
        safe_text
)
AbstractTypedConstraint_strategy = st.builds(
    AbstractTypedConstraint,
)
model_AssociationNode_strategy = st.builds(
    model_AssociationNode,
)
model_MappingElement_strategy = st.builds(
    model_MappingElement,
    key=
        safe_text,
    value=
        safe_text
)
model_AssociationTypeConstraint_strategy = st.builds(
    model_AssociationTypeConstraint,
)
AbstractCardinalityConstraint_strategy = st.builds(
    AbstractCardinalityConstraint,
)
model_AbstractTypedCardinalityConstraint_strategy = st.builds(
    model_AbstractTypedCardinalityConstraint,
)
model_RolePlayerConstraint_strategy = st.builds(
    model_RolePlayerConstraint,
)
AbstractTypedCardinalityConstraint_strategy = st.builds(
    AbstractTypedCardinalityConstraint,
)
model_ReifierConstraint_strategy = st.builds(
    model_ReifierConstraint,
)
model_ScopeConstraint_strategy = st.builds(
    model_ScopeConstraint,
)
model_OccurrenceTypeConstraint_strategy = st.builds(
    model_OccurrenceTypeConstraint,
)
model_NameTypeConstraint_strategy = st.builds(
    model_NameTypeConstraint,
)
model_RoleConstraint_strategy = st.builds(
    model_RoleConstraint,
)
AbstractConstraint_strategy = st.builds(
    AbstractConstraint,
)
model_RoleCombinationConstraint_strategy = st.builds(
    model_RoleCombinationConstraint,
)
model_AbstractTypedConstraint_strategy = st.builds(
    model_AbstractTypedConstraint,
)
model_AbstractCardinalityConstraint_strategy = st.builds(
    model_AbstractCardinalityConstraint,
    cardMax=
        safe_text,
    cardMin=
        safe_text
)
model_AbstractRegExpConstraint_strategy = st.builds(
    model_AbstractRegExpConstraint,
    regexp=
        safe_text
)
model_TopicReifiesConstraint_strategy = st.builds(
    model_TopicReifiesConstraint,
)
AbstractRegExpConstraint_strategy = st.builds(
    AbstractRegExpConstraint,
)
model_SubjectIdentifierConstraint_strategy = st.builds(
    model_SubjectIdentifierConstraint,
)
model_SubjectLocatorConstraint_strategy = st.builds(
    model_SubjectLocatorConstraint,
)
model_ItemIdentifierConstraint_strategy = st.builds(
    model_ItemIdentifierConstraint,
)
TMCLConstruct_strategy = st.builds(
    TMCLConstruct,
)
model_AbstractConstraint_strategy = st.builds(
    model_AbstractConstraint,
)
model_TopicMapSchema_strategy = st.builds(
    model_TopicMapSchema,
    version=
        safe_text,
    includes=
        safe_text,
    baseLocator=
        safe_text,
    name=
        safe_text,
    schemaResource=
        safe_text
)
model_TopicType_strategy = st.builds(
    model_TopicType,
    locators=
        safe_text,
    idType=
        safe_text,
    name=
        safe_text,
    identifiers=
        safe_text,
    abstract=
        st.booleans(),
    kind=
        safe_text
)

@given(instance=model_OnoObject_strategy)
@settings(max_examples=50)
def test_model_onoobject_instantiation(instance):
    assert isinstance(instance, model_OnoObject)



@given(instance=model_OnoObject_strategy)
def test_model_onoobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=model_DomainDiagram_strategy)
@settings(max_examples=50)
def test_model_domaindiagram_instantiation(instance):
    assert isinstance(instance, model_DomainDiagram)

@given(instance=ReifiableTopicType_strategy)
@settings(max_examples=50)
def test_reifiabletopictype_instantiation(instance):
    assert isinstance(instance, ReifiableTopicType)

@given(instance=AbstractUniqueValueTopicType_strategy)
@settings(max_examples=50)
def test_abstractuniquevaluetopictype_instantiation(instance):
    assert isinstance(instance, AbstractUniqueValueTopicType)

@given(instance=AbstractRegExpTopicType_strategy)
@settings(max_examples=50)
def test_abstractregexptopictype_instantiation(instance):
    assert isinstance(instance, AbstractRegExpTopicType)

@given(instance=ScopedReifiableTopicType_strategy)
@settings(max_examples=50)
def test_scopedreifiabletopictype_instantiation(instance):
    assert isinstance(instance, ScopedReifiableTopicType)

@given(instance=ScopedTopicType_strategy)
@settings(max_examples=50)
def test_scopedtopictype_instantiation(instance):
    assert isinstance(instance, ScopedTopicType)

@given(instance=model_ScopedReifiableTopicType_strategy)
@settings(max_examples=50)
def test_model_scopedreifiabletopictype_instantiation(instance):
    assert isinstance(instance, model_ScopedReifiableTopicType)

@given(instance=model_NameType_strategy)
@settings(max_examples=50)
def test_model_nametype_instantiation(instance):
    assert isinstance(instance, model_NameType)

@given(instance=model_OccurrenceType_strategy)
@settings(max_examples=50)
def test_model_occurrencetype_instantiation(instance):
    assert isinstance(instance, model_OccurrenceType)



@given(instance=model_OccurrenceType_strategy)
def test_model_occurrencetype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=model_AssociationType_strategy)
@settings(max_examples=50)
def test_model_associationtype_instantiation(instance):
    assert isinstance(instance, model_AssociationType)

@given(instance=TopicType_strategy)
@settings(max_examples=50)
def test_topictype_instantiation(instance):
    assert isinstance(instance, TopicType)

@given(instance=model_AbstractUniqueValueTopicType_strategy)
@settings(max_examples=50)
def test_model_abstractuniquevaluetopictype_instantiation(instance):
    assert isinstance(instance, model_AbstractUniqueValueTopicType)



@given(instance=model_AbstractUniqueValueTopicType_strategy)
def test_model_abstractuniquevaluetopictype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=model_AbstractRegExpTopicType_strategy)
@settings(max_examples=50)
def test_model_abstractregexptopictype_instantiation(instance):
    assert isinstance(instance, model_AbstractRegExpTopicType)



@given(instance=model_AbstractRegExpTopicType_strategy)
def test_model_abstractregexptopictype_regExp_setter(instance):
    original = instance.regExp
    instance.regExp = original
    assert instance.regExp == original

@given(instance=model_ReifiableTopicType_strategy)
@settings(max_examples=50)
def test_model_reifiabletopictype_instantiation(instance):
    assert isinstance(instance, model_ReifiableTopicType)

@given(instance=model_ScopedTopicType_strategy)
@settings(max_examples=50)
def test_model_scopedtopictype_instantiation(instance):
    assert isinstance(instance, model_ScopedTopicType)

@given(instance=model_RoleType_strategy)
@settings(max_examples=50)
def test_model_roletype_instantiation(instance):
    assert isinstance(instance, model_RoleType)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model_Comment_strategy)
@settings(max_examples=50)
def test_model_comment_instantiation(instance):
    assert isinstance(instance, model_Comment)



@given(instance=model_Comment_strategy)
def test_model_comment_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=model_Comment_strategy)
def test_model_comment_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=model_Comment_strategy)
def test_model_comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=model_TypeNode_strategy)
@settings(max_examples=50)
def test_model_typenode_instantiation(instance):
    assert isinstance(instance, model_TypeNode)



@given(instance=model_TypeNode_strategy)
def test_model_typenode_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=OnoObject_strategy)
@settings(max_examples=50)
def test_onoobject_instantiation(instance):
    assert isinstance(instance, OnoObject)

@given(instance=model_Bendpoint_strategy)
@settings(max_examples=50)
def test_model_bendpoint_instantiation(instance):
    assert isinstance(instance, model_Bendpoint)



@given(instance=model_Bendpoint_strategy)
def test_model_bendpoint_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original



@given(instance=model_Bendpoint_strategy)
def test_model_bendpoint_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model_LabelPos_strategy)
@settings(max_examples=50)
def test_model_labelpos_instantiation(instance):
    assert isinstance(instance, model_LabelPos)



@given(instance=model_LabelPos_strategy)
def test_model_labelpos_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original



@given(instance=model_LabelPos_strategy)
def test_model_labelpos_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model_TMCLConstruct_strategy)
@settings(max_examples=50)
def test_model_tmclconstruct_instantiation(instance):
    assert isinstance(instance, model_TMCLConstruct)



@given(instance=model_TMCLConstruct_strategy)
def test_model_tmclconstruct_see_also_setter(instance):
    original = instance.see_also
    instance.see_also = original
    assert instance.see_also == original



@given(instance=model_TMCLConstruct_strategy)
def test_model_tmclconstruct_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=model_TMCLConstruct_strategy)
def test_model_tmclconstruct_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model_Node_strategy)
@settings(max_examples=50)
def test_model_node_instantiation(instance):
    assert isinstance(instance, model_Node)



@given(instance=model_Node_strategy)
def test_model_node_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original



@given(instance=model_Node_strategy)
def test_model_node_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model_Edge_strategy)
@settings(max_examples=50)
def test_model_edge_instantiation(instance):
    assert isinstance(instance, model_Edge)



@given(instance=model_Edge_strategy)
def test_model_edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model_Annotation_strategy)
@settings(max_examples=50)
def test_model_annotation_instantiation(instance):
    assert isinstance(instance, model_Annotation)



@given(instance=model_Annotation_strategy)
def test_model_annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=model_Annotation_strategy)
def test_model_annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_File_strategy)
@settings(max_examples=50)
def test_model_file_instantiation(instance):
    assert isinstance(instance, model_File)



@given(instance=model_File_strategy)
def test_model_file_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original



@given(instance=model_File_strategy)
def test_model_file_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original



@given(instance=model_File_strategy)
def test_model_file_dirty_setter(instance):
    original = instance.dirty
    instance.dirty = original
    assert instance.dirty == original

@given(instance=model_Diagram_strategy)
@settings(max_examples=50)
def test_model_diagram_instantiation(instance):
    assert isinstance(instance, model_Diagram)



@given(instance=model_Diagram_strategy)
def test_model_diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTypedConstraint_strategy)
@settings(max_examples=50)
def test_abstracttypedconstraint_instantiation(instance):
    assert isinstance(instance, AbstractTypedConstraint)

@given(instance=model_AssociationNode_strategy)
@settings(max_examples=50)
def test_model_associationnode_instantiation(instance):
    assert isinstance(instance, model_AssociationNode)

@given(instance=model_MappingElement_strategy)
@settings(max_examples=50)
def test_model_mappingelement_instantiation(instance):
    assert isinstance(instance, model_MappingElement)



@given(instance=model_MappingElement_strategy)
def test_model_mappingelement_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=model_MappingElement_strategy)
def test_model_mappingelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model_AssociationTypeConstraint_strategy)
@settings(max_examples=50)
def test_model_associationtypeconstraint_instantiation(instance):
    assert isinstance(instance, model_AssociationTypeConstraint)

@given(instance=AbstractCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_abstractcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, AbstractCardinalityConstraint)

@given(instance=model_AbstractTypedCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_model_abstracttypedcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, model_AbstractTypedCardinalityConstraint)

@given(instance=model_RolePlayerConstraint_strategy)
@settings(max_examples=50)
def test_model_roleplayerconstraint_instantiation(instance):
    assert isinstance(instance, model_RolePlayerConstraint)

@given(instance=AbstractTypedCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_abstracttypedcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, AbstractTypedCardinalityConstraint)

@given(instance=model_ReifierConstraint_strategy)
@settings(max_examples=50)
def test_model_reifierconstraint_instantiation(instance):
    assert isinstance(instance, model_ReifierConstraint)

@given(instance=model_ScopeConstraint_strategy)
@settings(max_examples=50)
def test_model_scopeconstraint_instantiation(instance):
    assert isinstance(instance, model_ScopeConstraint)

@given(instance=model_OccurrenceTypeConstraint_strategy)
@settings(max_examples=50)
def test_model_occurrencetypeconstraint_instantiation(instance):
    assert isinstance(instance, model_OccurrenceTypeConstraint)

@given(instance=model_NameTypeConstraint_strategy)
@settings(max_examples=50)
def test_model_nametypeconstraint_instantiation(instance):
    assert isinstance(instance, model_NameTypeConstraint)

@given(instance=model_RoleConstraint_strategy)
@settings(max_examples=50)
def test_model_roleconstraint_instantiation(instance):
    assert isinstance(instance, model_RoleConstraint)

@given(instance=AbstractConstraint_strategy)
@settings(max_examples=50)
def test_abstractconstraint_instantiation(instance):
    assert isinstance(instance, AbstractConstraint)

@given(instance=model_RoleCombinationConstraint_strategy)
@settings(max_examples=50)
def test_model_rolecombinationconstraint_instantiation(instance):
    assert isinstance(instance, model_RoleCombinationConstraint)

@given(instance=model_AbstractTypedConstraint_strategy)
@settings(max_examples=50)
def test_model_abstracttypedconstraint_instantiation(instance):
    assert isinstance(instance, model_AbstractTypedConstraint)

@given(instance=model_AbstractCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_model_abstractcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, model_AbstractCardinalityConstraint)



@given(instance=model_AbstractCardinalityConstraint_strategy)
def test_model_abstractcardinalityconstraint_cardMax_setter(instance):
    original = instance.cardMax
    instance.cardMax = original
    assert instance.cardMax == original



@given(instance=model_AbstractCardinalityConstraint_strategy)
def test_model_abstractcardinalityconstraint_cardMin_setter(instance):
    original = instance.cardMin
    instance.cardMin = original
    assert instance.cardMin == original

@given(instance=model_AbstractRegExpConstraint_strategy)
@settings(max_examples=50)
def test_model_abstractregexpconstraint_instantiation(instance):
    assert isinstance(instance, model_AbstractRegExpConstraint)



@given(instance=model_AbstractRegExpConstraint_strategy)
def test_model_abstractregexpconstraint_regexp_setter(instance):
    original = instance.regexp
    instance.regexp = original
    assert instance.regexp == original

@given(instance=model_TopicReifiesConstraint_strategy)
@settings(max_examples=50)
def test_model_topicreifiesconstraint_instantiation(instance):
    assert isinstance(instance, model_TopicReifiesConstraint)

@given(instance=AbstractRegExpConstraint_strategy)
@settings(max_examples=50)
def test_abstractregexpconstraint_instantiation(instance):
    assert isinstance(instance, AbstractRegExpConstraint)

@given(instance=model_SubjectIdentifierConstraint_strategy)
@settings(max_examples=50)
def test_model_subjectidentifierconstraint_instantiation(instance):
    assert isinstance(instance, model_SubjectIdentifierConstraint)

@given(instance=model_SubjectLocatorConstraint_strategy)
@settings(max_examples=50)
def test_model_subjectlocatorconstraint_instantiation(instance):
    assert isinstance(instance, model_SubjectLocatorConstraint)

@given(instance=model_ItemIdentifierConstraint_strategy)
@settings(max_examples=50)
def test_model_itemidentifierconstraint_instantiation(instance):
    assert isinstance(instance, model_ItemIdentifierConstraint)

@given(instance=TMCLConstruct_strategy)
@settings(max_examples=50)
def test_tmclconstruct_instantiation(instance):
    assert isinstance(instance, TMCLConstruct)

@given(instance=model_AbstractConstraint_strategy)
@settings(max_examples=50)
def test_model_abstractconstraint_instantiation(instance):
    assert isinstance(instance, model_AbstractConstraint)

@given(instance=model_TopicMapSchema_strategy)
@settings(max_examples=50)
def test_model_topicmapschema_instantiation(instance):
    assert isinstance(instance, model_TopicMapSchema)



@given(instance=model_TopicMapSchema_strategy)
def test_model_topicmapschema_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=model_TopicMapSchema_strategy)
def test_model_topicmapschema_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original



@given(instance=model_TopicMapSchema_strategy)
def test_model_topicmapschema_baseLocator_setter(instance):
    original = instance.baseLocator
    instance.baseLocator = original
    assert instance.baseLocator == original



@given(instance=model_TopicMapSchema_strategy)
def test_model_topicmapschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_TopicMapSchema_strategy)
def test_model_topicmapschema_schemaResource_setter(instance):
    original = instance.schemaResource
    instance.schemaResource = original
    assert instance.schemaResource == original

@given(instance=model_TopicType_strategy)
@settings(max_examples=50)
def test_model_topictype_instantiation(instance):
    assert isinstance(instance, model_TopicType)



@given(instance=model_TopicType_strategy)
def test_model_topictype_locators_setter(instance):
    original = instance.locators
    instance.locators = original
    assert instance.locators == original



@given(instance=model_TopicType_strategy)
def test_model_topictype_idType_setter(instance):
    original = instance.idType
    instance.idType = original
    assert instance.idType == original



@given(instance=model_TopicType_strategy)
def test_model_topictype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_TopicType_strategy)
def test_model_topictype_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original



@given(instance=model_TopicType_strategy)
def test_model_topictype_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=model_TopicType_strategy)
def test_model_topictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original
