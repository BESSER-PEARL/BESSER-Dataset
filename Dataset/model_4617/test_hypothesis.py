import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::OnoObject,
    Diagram,
    model::DomainDiagram,
    ReifiableTopicType,
    AbstractUniqueValueTopicType,
    AbstractRegExpTopicType,
    ScopedReifiableTopicType,
    ScopedTopicType,
    model::ScopedReifiableTopicType,
    model::OccurrenceType,
    model::NameType,
    model::AssociationType,
    TopicType,
    model::AbstractUniqueValueTopicType,
    model::ReifiableTopicType,
    model::AbstractRegExpTopicType,
    model::ScopedTopicType,
    model::RoleType,
    Node,
    model::Comment,
    model::TypeNode,
    OnoObject,
    model::File,
    model::TMCLConstruct,
    model::Node,
    model::Annotation,
    model::Bendpoint,
    model::Edge,
    model::LabelPos,
    model::Diagram,
    AbstractTypedConstraint,
    model::AssociationNode,
    model::MappingElement,
    model::AssociationTypeConstraint,
    AbstractCardinalityConstraint,
    model::AbstractTypedCardinalityConstraint,
    model::RolePlayerConstraint,
    AbstractTypedCardinalityConstraint,
    model::NameTypeConstraint,
    model::ScopeConstraint,
    model::OccurrenceTypeConstraint,
    model::RoleConstraint,
    model::ReifierConstraint,
    AbstractConstraint,
    model::RoleCombinationConstraint,
    model::AbstractTypedConstraint,
    model::AbstractCardinalityConstraint,
    model::AbstractRegExpConstraint,
    model::TopicReifiesConstraint,
    AbstractRegExpConstraint,
    model::ItemIdentifierConstraint,
    model::SubjectLocatorConstraint,
    model::SubjectIdentifierConstraint,
    TMCLConstruct,
    model::AbstractConstraint,
    model::TopicMapSchema,
    model::TopicType,
    TopicId,
    EdgeType,
    KindOfTopicType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::onoobject_is_not_abstract():
    assert not inspect.isabstract(model::OnoObject)


def test_model::onoobject_constructor_exists():
    assert callable(model::OnoObject.__init__)


def test_model::onoobject_constructor_args():
    sig = inspect.signature(model::OnoObject.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_model::onoobject_has_id():
    assert hasattr(model::OnoObject, "id")
    descriptor = None
    for klass in model::OnoObject.__mro__:
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



def test_model::domaindiagram_is_not_abstract():
    assert not inspect.isabstract(model::DomainDiagram)


def test_model::domaindiagram_constructor_exists():
    assert callable(model::DomainDiagram.__init__)


def test_model::domaindiagram_constructor_args():
    sig = inspect.signature(model::DomainDiagram.__init__)
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



def test_model::scopedreifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(model::ScopedReifiableTopicType)


def test_model::scopedreifiabletopictype_constructor_exists():
    assert callable(model::ScopedReifiableTopicType.__init__)


def test_model::scopedreifiabletopictype_constructor_args():
    sig = inspect.signature(model::ScopedReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model::occurrencetype_is_not_abstract():
    assert not inspect.isabstract(model::OccurrenceType)


def test_model::occurrencetype_constructor_exists():
    assert callable(model::OccurrenceType.__init__)


def test_model::occurrencetype_constructor_args():
    sig = inspect.signature(model::OccurrenceType.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_model::occurrencetype_has_dataType():
    assert hasattr(model::OccurrenceType, "dataType")
    descriptor = None
    for klass in model::OccurrenceType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_model::nametype_is_not_abstract():
    assert not inspect.isabstract(model::NameType)


def test_model::nametype_constructor_exists():
    assert callable(model::NameType.__init__)


def test_model::nametype_constructor_args():
    sig = inspect.signature(model::NameType.__init__)
    params = list(sig.parameters.keys())



def test_model::associationtype_is_not_abstract():
    assert not inspect.isabstract(model::AssociationType)


def test_model::associationtype_constructor_exists():
    assert callable(model::AssociationType.__init__)


def test_model::associationtype_constructor_args():
    sig = inspect.signature(model::AssociationType.__init__)
    params = list(sig.parameters.keys())



def test_topictype_is_not_abstract():
    assert not inspect.isabstract(TopicType)


def test_topictype_constructor_exists():
    assert callable(TopicType.__init__)


def test_topictype_constructor_args():
    sig = inspect.signature(TopicType.__init__)
    params = list(sig.parameters.keys())



def test_model::abstractuniquevaluetopictype_is_not_abstract():
    assert not inspect.isabstract(model::AbstractUniqueValueTopicType)


def test_model::abstractuniquevaluetopictype_constructor_exists():
    assert callable(model::AbstractUniqueValueTopicType.__init__)


def test_model::abstractuniquevaluetopictype_constructor_args():
    sig = inspect.signature(model::AbstractUniqueValueTopicType.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_model::abstractuniquevaluetopictype_has_unique():
    assert hasattr(model::AbstractUniqueValueTopicType, "unique")
    descriptor = None
    for klass in model::AbstractUniqueValueTopicType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_model::reifiabletopictype_is_not_abstract():
    assert not inspect.isabstract(model::ReifiableTopicType)


def test_model::reifiabletopictype_constructor_exists():
    assert callable(model::ReifiableTopicType.__init__)


def test_model::reifiabletopictype_constructor_args():
    sig = inspect.signature(model::ReifiableTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model::abstractregexptopictype_is_not_abstract():
    assert not inspect.isabstract(model::AbstractRegExpTopicType)


def test_model::abstractregexptopictype_constructor_exists():
    assert callable(model::AbstractRegExpTopicType.__init__)


def test_model::abstractregexptopictype_constructor_args():
    sig = inspect.signature(model::AbstractRegExpTopicType.__init__)
    params = list(sig.parameters.keys())
    assert "regExp" in params, "Missing parameter 'regExp'"

def test_model::abstractregexptopictype_has_regExp():
    assert hasattr(model::AbstractRegExpTopicType, "regExp")
    descriptor = None
    for klass in model::AbstractRegExpTopicType.__mro__:
        if "regExp" in klass.__dict__:
            descriptor = klass.__dict__["regExp"]
            break
    assert isinstance(descriptor, property)



def test_model::scopedtopictype_is_not_abstract():
    assert not inspect.isabstract(model::ScopedTopicType)


def test_model::scopedtopictype_constructor_exists():
    assert callable(model::ScopedTopicType.__init__)


def test_model::scopedtopictype_constructor_args():
    sig = inspect.signature(model::ScopedTopicType.__init__)
    params = list(sig.parameters.keys())



def test_model::roletype_is_not_abstract():
    assert not inspect.isabstract(model::RoleType)


def test_model::roletype_constructor_exists():
    assert callable(model::RoleType.__init__)


def test_model::roletype_constructor_args():
    sig = inspect.signature(model::RoleType.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_model::comment_is_not_abstract():
    assert not inspect.isabstract(model::Comment)


def test_model::comment_constructor_exists():
    assert callable(model::Comment.__init__)


def test_model::comment_constructor_args():
    sig = inspect.signature(model::Comment.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"
    assert "content" in params, "Missing parameter 'content'"

def test_model::comment_has_width():
    assert hasattr(model::Comment, "width")
    descriptor = None
    for klass in model::Comment.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_model::comment_has_height():
    assert hasattr(model::Comment, "height")
    descriptor = None
    for klass in model::Comment.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_model::comment_has_content():
    assert hasattr(model::Comment, "content")
    descriptor = None
    for klass in model::Comment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_model::typenode_is_not_abstract():
    assert not inspect.isabstract(model::TypeNode)


def test_model::typenode_constructor_exists():
    assert callable(model::TypeNode.__init__)


def test_model::typenode_constructor_args():
    sig = inspect.signature(model::TypeNode.__init__)
    params = list(sig.parameters.keys())
    assert "image" in params, "Missing parameter 'image'"

def test_model::typenode_has_image():
    assert hasattr(model::TypeNode, "image")
    descriptor = None
    for klass in model::TypeNode.__mro__:
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



def test_model::file_is_not_abstract():
    assert not inspect.isabstract(model::File)


def test_model::file_constructor_exists():
    assert callable(model::File.__init__)


def test_model::file_constructor_args():
    sig = inspect.signature(model::File.__init__)
    params = list(sig.parameters.keys())
    assert "dirty" in params, "Missing parameter 'dirty'"
    assert "filename" in params, "Missing parameter 'filename'"
    assert "notes" in params, "Missing parameter 'notes'"

def test_model::file_has_dirty():
    assert hasattr(model::File, "dirty")
    descriptor = None
    for klass in model::File.__mro__:
        if "dirty" in klass.__dict__:
            descriptor = klass.__dict__["dirty"]
            break
    assert isinstance(descriptor, property)

def test_model::file_has_filename():
    assert hasattr(model::File, "filename")
    descriptor = None
    for klass in model::File.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)

def test_model::file_has_notes():
    assert hasattr(model::File, "notes")
    descriptor = None
    for klass in model::File.__mro__:
        if "notes" in klass.__dict__:
            descriptor = klass.__dict__["notes"]
            break
    assert isinstance(descriptor, property)



def test_model::tmclconstruct_is_not_abstract():
    assert not inspect.isabstract(model::TMCLConstruct)


def test_model::tmclconstruct_constructor_exists():
    assert callable(model::TMCLConstruct.__init__)


def test_model::tmclconstruct_constructor_args():
    sig = inspect.signature(model::TMCLConstruct.__init__)
    params = list(sig.parameters.keys())
    assert "see_also" in params, "Missing parameter 'see_also'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "description" in params, "Missing parameter 'description'"

def test_model::tmclconstruct_has_see_also():
    assert hasattr(model::TMCLConstruct, "see_also")
    descriptor = None
    for klass in model::TMCLConstruct.__mro__:
        if "see_also" in klass.__dict__:
            descriptor = klass.__dict__["see_also"]
            break
    assert isinstance(descriptor, property)

def test_model::tmclconstruct_has_comment():
    assert hasattr(model::TMCLConstruct, "comment")
    descriptor = None
    for klass in model::TMCLConstruct.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_model::tmclconstruct_has_description():
    assert hasattr(model::TMCLConstruct, "description")
    descriptor = None
    for klass in model::TMCLConstruct.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_model::node_is_not_abstract():
    assert not inspect.isabstract(model::Node)


def test_model::node_constructor_exists():
    assert callable(model::Node.__init__)


def test_model::node_constructor_args():
    sig = inspect.signature(model::Node.__init__)
    params = list(sig.parameters.keys())
    assert "posX" in params, "Missing parameter 'posX'"
    assert "posY" in params, "Missing parameter 'posY'"

def test_model::node_has_posX():
    assert hasattr(model::Node, "posX")
    descriptor = None
    for klass in model::Node.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)

def test_model::node_has_posY():
    assert hasattr(model::Node, "posY")
    descriptor = None
    for klass in model::Node.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)



def test_model::annotation_is_not_abstract():
    assert not inspect.isabstract(model::Annotation)


def test_model::annotation_constructor_exists():
    assert callable(model::Annotation.__init__)


def test_model::annotation_constructor_args():
    sig = inspect.signature(model::Annotation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_model::annotation_has_value():
    assert hasattr(model::Annotation, "value")
    descriptor = None
    for klass in model::Annotation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::annotation_has_key():
    assert hasattr(model::Annotation, "key")
    descriptor = None
    for klass in model::Annotation.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_model::bendpoint_is_not_abstract():
    assert not inspect.isabstract(model::Bendpoint)


def test_model::bendpoint_constructor_exists():
    assert callable(model::Bendpoint.__init__)


def test_model::bendpoint_constructor_args():
    sig = inspect.signature(model::Bendpoint.__init__)
    params = list(sig.parameters.keys())
    assert "posY" in params, "Missing parameter 'posY'"
    assert "posX" in params, "Missing parameter 'posX'"

def test_model::bendpoint_has_posY():
    assert hasattr(model::Bendpoint, "posY")
    descriptor = None
    for klass in model::Bendpoint.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)

def test_model::bendpoint_has_posX():
    assert hasattr(model::Bendpoint, "posX")
    descriptor = None
    for klass in model::Bendpoint.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)



def test_model::edge_is_not_abstract():
    assert not inspect.isabstract(model::Edge)


def test_model::edge_constructor_exists():
    assert callable(model::Edge.__init__)


def test_model::edge_constructor_args():
    sig = inspect.signature(model::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_model::edge_has_type():
    assert hasattr(model::Edge, "type")
    descriptor = None
    for klass in model::Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_model::labelpos_is_not_abstract():
    assert not inspect.isabstract(model::LabelPos)


def test_model::labelpos_constructor_exists():
    assert callable(model::LabelPos.__init__)


def test_model::labelpos_constructor_args():
    sig = inspect.signature(model::LabelPos.__init__)
    params = list(sig.parameters.keys())
    assert "posX" in params, "Missing parameter 'posX'"
    assert "posY" in params, "Missing parameter 'posY'"

def test_model::labelpos_has_posX():
    assert hasattr(model::LabelPos, "posX")
    descriptor = None
    for klass in model::LabelPos.__mro__:
        if "posX" in klass.__dict__:
            descriptor = klass.__dict__["posX"]
            break
    assert isinstance(descriptor, property)

def test_model::labelpos_has_posY():
    assert hasattr(model::LabelPos, "posY")
    descriptor = None
    for klass in model::LabelPos.__mro__:
        if "posY" in klass.__dict__:
            descriptor = klass.__dict__["posY"]
            break
    assert isinstance(descriptor, property)



def test_model::diagram_is_not_abstract():
    assert not inspect.isabstract(model::Diagram)


def test_model::diagram_constructor_exists():
    assert callable(model::Diagram.__init__)


def test_model::diagram_constructor_args():
    sig = inspect.signature(model::Diagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::diagram_has_name():
    assert hasattr(model::Diagram, "name")
    descriptor = None
    for klass in model::Diagram.__mro__:
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



def test_model::associationnode_is_not_abstract():
    assert not inspect.isabstract(model::AssociationNode)


def test_model::associationnode_constructor_exists():
    assert callable(model::AssociationNode.__init__)


def test_model::associationnode_constructor_args():
    sig = inspect.signature(model::AssociationNode.__init__)
    params = list(sig.parameters.keys())



def test_model::mappingelement_is_not_abstract():
    assert not inspect.isabstract(model::MappingElement)


def test_model::mappingelement_constructor_exists():
    assert callable(model::MappingElement.__init__)


def test_model::mappingelement_constructor_args():
    sig = inspect.signature(model::MappingElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_model::mappingelement_has_value():
    assert hasattr(model::MappingElement, "value")
    descriptor = None
    for klass in model::MappingElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_model::mappingelement_has_key():
    assert hasattr(model::MappingElement, "key")
    descriptor = None
    for klass in model::MappingElement.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_model::associationtypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AssociationTypeConstraint)


def test_model::associationtypeconstraint_constructor_exists():
    assert callable(model::AssociationTypeConstraint.__init__)


def test_model::associationtypeconstraint_constructor_args():
    sig = inspect.signature(model::AssociationTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractCardinalityConstraint)


def test_abstractcardinalityconstraint_constructor_exists():
    assert callable(AbstractCardinalityConstraint.__init__)


def test_abstractcardinalityconstraint_constructor_args():
    sig = inspect.signature(AbstractCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::abstracttypedcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AbstractTypedCardinalityConstraint)


def test_model::abstracttypedcardinalityconstraint_constructor_exists():
    assert callable(model::AbstractTypedCardinalityConstraint.__init__)


def test_model::abstracttypedcardinalityconstraint_constructor_args():
    sig = inspect.signature(model::AbstractTypedCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::roleplayerconstraint_is_not_abstract():
    assert not inspect.isabstract(model::RolePlayerConstraint)


def test_model::roleplayerconstraint_constructor_exists():
    assert callable(model::RolePlayerConstraint.__init__)


def test_model::roleplayerconstraint_constructor_args():
    sig = inspect.signature(model::RolePlayerConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstracttypedcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractTypedCardinalityConstraint)


def test_abstracttypedcardinalityconstraint_constructor_exists():
    assert callable(AbstractTypedCardinalityConstraint.__init__)


def test_abstracttypedcardinalityconstraint_constructor_args():
    sig = inspect.signature(AbstractTypedCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::nametypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model::NameTypeConstraint)


def test_model::nametypeconstraint_constructor_exists():
    assert callable(model::NameTypeConstraint.__init__)


def test_model::nametypeconstraint_constructor_args():
    sig = inspect.signature(model::NameTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::scopeconstraint_is_not_abstract():
    assert not inspect.isabstract(model::ScopeConstraint)


def test_model::scopeconstraint_constructor_exists():
    assert callable(model::ScopeConstraint.__init__)


def test_model::scopeconstraint_constructor_args():
    sig = inspect.signature(model::ScopeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::occurrencetypeconstraint_is_not_abstract():
    assert not inspect.isabstract(model::OccurrenceTypeConstraint)


def test_model::occurrencetypeconstraint_constructor_exists():
    assert callable(model::OccurrenceTypeConstraint.__init__)


def test_model::occurrencetypeconstraint_constructor_args():
    sig = inspect.signature(model::OccurrenceTypeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::roleconstraint_is_not_abstract():
    assert not inspect.isabstract(model::RoleConstraint)


def test_model::roleconstraint_constructor_exists():
    assert callable(model::RoleConstraint.__init__)


def test_model::roleconstraint_constructor_args():
    sig = inspect.signature(model::RoleConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::reifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model::ReifierConstraint)


def test_model::reifierconstraint_constructor_exists():
    assert callable(model::ReifierConstraint.__init__)


def test_model::reifierconstraint_constructor_args():
    sig = inspect.signature(model::ReifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractConstraint)


def test_abstractconstraint_constructor_exists():
    assert callable(AbstractConstraint.__init__)


def test_abstractconstraint_constructor_args():
    sig = inspect.signature(AbstractConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::rolecombinationconstraint_is_not_abstract():
    assert not inspect.isabstract(model::RoleCombinationConstraint)


def test_model::rolecombinationconstraint_constructor_exists():
    assert callable(model::RoleCombinationConstraint.__init__)


def test_model::rolecombinationconstraint_constructor_args():
    sig = inspect.signature(model::RoleCombinationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::abstracttypedconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AbstractTypedConstraint)


def test_model::abstracttypedconstraint_constructor_exists():
    assert callable(model::AbstractTypedConstraint.__init__)


def test_model::abstracttypedconstraint_constructor_args():
    sig = inspect.signature(model::AbstractTypedConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::abstractcardinalityconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AbstractCardinalityConstraint)


def test_model::abstractcardinalityconstraint_constructor_exists():
    assert callable(model::AbstractCardinalityConstraint.__init__)


def test_model::abstractcardinalityconstraint_constructor_args():
    sig = inspect.signature(model::AbstractCardinalityConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "cardMax" in params, "Missing parameter 'cardMax'"
    assert "cardMin" in params, "Missing parameter 'cardMin'"

def test_model::abstractcardinalityconstraint_has_cardMax():
    assert hasattr(model::AbstractCardinalityConstraint, "cardMax")
    descriptor = None
    for klass in model::AbstractCardinalityConstraint.__mro__:
        if "cardMax" in klass.__dict__:
            descriptor = klass.__dict__["cardMax"]
            break
    assert isinstance(descriptor, property)

def test_model::abstractcardinalityconstraint_has_cardMin():
    assert hasattr(model::AbstractCardinalityConstraint, "cardMin")
    descriptor = None
    for klass in model::AbstractCardinalityConstraint.__mro__:
        if "cardMin" in klass.__dict__:
            descriptor = klass.__dict__["cardMin"]
            break
    assert isinstance(descriptor, property)



def test_model::abstractregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AbstractRegExpConstraint)


def test_model::abstractregexpconstraint_constructor_exists():
    assert callable(model::AbstractRegExpConstraint.__init__)


def test_model::abstractregexpconstraint_constructor_args():
    sig = inspect.signature(model::AbstractRegExpConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "regexp" in params, "Missing parameter 'regexp'"

def test_model::abstractregexpconstraint_has_regexp():
    assert hasattr(model::AbstractRegExpConstraint, "regexp")
    descriptor = None
    for klass in model::AbstractRegExpConstraint.__mro__:
        if "regexp" in klass.__dict__:
            descriptor = klass.__dict__["regexp"]
            break
    assert isinstance(descriptor, property)



def test_model::topicreifiesconstraint_is_not_abstract():
    assert not inspect.isabstract(model::TopicReifiesConstraint)


def test_model::topicreifiesconstraint_constructor_exists():
    assert callable(model::TopicReifiesConstraint.__init__)


def test_model::topicreifiesconstraint_constructor_args():
    sig = inspect.signature(model::TopicReifiesConstraint.__init__)
    params = list(sig.parameters.keys())



def test_abstractregexpconstraint_is_not_abstract():
    assert not inspect.isabstract(AbstractRegExpConstraint)


def test_abstractregexpconstraint_constructor_exists():
    assert callable(AbstractRegExpConstraint.__init__)


def test_abstractregexpconstraint_constructor_args():
    sig = inspect.signature(AbstractRegExpConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::itemidentifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model::ItemIdentifierConstraint)


def test_model::itemidentifierconstraint_constructor_exists():
    assert callable(model::ItemIdentifierConstraint.__init__)


def test_model::itemidentifierconstraint_constructor_args():
    sig = inspect.signature(model::ItemIdentifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::subjectlocatorconstraint_is_not_abstract():
    assert not inspect.isabstract(model::SubjectLocatorConstraint)


def test_model::subjectlocatorconstraint_constructor_exists():
    assert callable(model::SubjectLocatorConstraint.__init__)


def test_model::subjectlocatorconstraint_constructor_args():
    sig = inspect.signature(model::SubjectLocatorConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::subjectidentifierconstraint_is_not_abstract():
    assert not inspect.isabstract(model::SubjectIdentifierConstraint)


def test_model::subjectidentifierconstraint_constructor_exists():
    assert callable(model::SubjectIdentifierConstraint.__init__)


def test_model::subjectidentifierconstraint_constructor_args():
    sig = inspect.signature(model::SubjectIdentifierConstraint.__init__)
    params = list(sig.parameters.keys())



def test_tmclconstruct_is_not_abstract():
    assert not inspect.isabstract(TMCLConstruct)


def test_tmclconstruct_constructor_exists():
    assert callable(TMCLConstruct.__init__)


def test_tmclconstruct_constructor_args():
    sig = inspect.signature(TMCLConstruct.__init__)
    params = list(sig.parameters.keys())



def test_model::abstractconstraint_is_not_abstract():
    assert not inspect.isabstract(model::AbstractConstraint)


def test_model::abstractconstraint_constructor_exists():
    assert callable(model::AbstractConstraint.__init__)


def test_model::abstractconstraint_constructor_args():
    sig = inspect.signature(model::AbstractConstraint.__init__)
    params = list(sig.parameters.keys())



def test_model::topicmapschema_is_not_abstract():
    assert not inspect.isabstract(model::TopicMapSchema)


def test_model::topicmapschema_constructor_exists():
    assert callable(model::TopicMapSchema.__init__)


def test_model::topicmapschema_constructor_args():
    sig = inspect.signature(model::TopicMapSchema.__init__)
    params = list(sig.parameters.keys())
    assert "baseLocator" in params, "Missing parameter 'baseLocator'"
    assert "name" in params, "Missing parameter 'name'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "version" in params, "Missing parameter 'version'"
    assert "schemaResource" in params, "Missing parameter 'schemaResource'"

def test_model::topicmapschema_has_baseLocator():
    assert hasattr(model::TopicMapSchema, "baseLocator")
    descriptor = None
    for klass in model::TopicMapSchema.__mro__:
        if "baseLocator" in klass.__dict__:
            descriptor = klass.__dict__["baseLocator"]
            break
    assert isinstance(descriptor, property)

def test_model::topicmapschema_has_name():
    assert hasattr(model::TopicMapSchema, "name")
    descriptor = None
    for klass in model::TopicMapSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::topicmapschema_has_includes():
    assert hasattr(model::TopicMapSchema, "includes")
    descriptor = None
    for klass in model::TopicMapSchema.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_model::topicmapschema_has_version():
    assert hasattr(model::TopicMapSchema, "version")
    descriptor = None
    for klass in model::TopicMapSchema.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_model::topicmapschema_has_schemaResource():
    assert hasattr(model::TopicMapSchema, "schemaResource")
    descriptor = None
    for klass in model::TopicMapSchema.__mro__:
        if "schemaResource" in klass.__dict__:
            descriptor = klass.__dict__["schemaResource"]
            break
    assert isinstance(descriptor, property)



def test_model::topictype_is_not_abstract():
    assert not inspect.isabstract(model::TopicType)


def test_model::topictype_constructor_exists():
    assert callable(model::TopicType.__init__)


def test_model::topictype_constructor_args():
    sig = inspect.signature(model::TopicType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "idType" in params, "Missing parameter 'idType'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "locators" in params, "Missing parameter 'locators'"
    assert "identifiers" in params, "Missing parameter 'identifiers'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_model::topictype_has_name():
    assert hasattr(model::TopicType, "name")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::topictype_has_idType():
    assert hasattr(model::TopicType, "idType")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "idType" in klass.__dict__:
            descriptor = klass.__dict__["idType"]
            break
    assert isinstance(descriptor, property)

def test_model::topictype_has_kind():
    assert hasattr(model::TopicType, "kind")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_model::topictype_has_locators():
    assert hasattr(model::TopicType, "locators")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "locators" in klass.__dict__:
            descriptor = klass.__dict__["locators"]
            break
    assert isinstance(descriptor, property)

def test_model::topictype_has_identifiers():
    assert hasattr(model::TopicType, "identifiers")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)

def test_model::topictype_has_abstract():
    assert hasattr(model::TopicType, "abstract")
    descriptor = None
    for klass in model::TopicType.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
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

def test_edgetype_exists():
    # Check that the Enumeration exists
    assert EdgeType is not None

def test_edgetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeType]
    expected_literals = [
        "IS_ATYPE",
        "AKO_TYPE",
        "ROLE_CONSTRAINT_TYPE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeType"

def test_kindoftopictype_exists():
    # Check that the Enumeration exists
    assert KindOfTopicType is not None

def test_kindoftopictype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindOfTopicType]
    expected_literals = [
        "RoleType",
        "TopicType",
        "AssociationType",
        "ScopeType",
        "OccurrenceType",
        "NoType",
        "NameType",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindOfTopicType"


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
model::OnoObject_strategy = st.builds(
    model::OnoObject,
    id=
        st.integers()
)
Diagram_strategy = st.builds(
    Diagram,
)
model::DomainDiagram_strategy = st.builds(
    model::DomainDiagram,
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
model::ScopedReifiableTopicType_strategy = st.builds(
    model::ScopedReifiableTopicType,
)
model::OccurrenceType_strategy = st.builds(
    model::OccurrenceType,
    dataType=
        safe_text
)
model::NameType_strategy = st.builds(
    model::NameType,
)
model::AssociationType_strategy = st.builds(
    model::AssociationType,
)
TopicType_strategy = st.builds(
    TopicType,
)
model::AbstractUniqueValueTopicType_strategy = st.builds(
    model::AbstractUniqueValueTopicType,
    unique=
        st.booleans()
)
model::ReifiableTopicType_strategy = st.builds(
    model::ReifiableTopicType,
)
model::AbstractRegExpTopicType_strategy = st.builds(
    model::AbstractRegExpTopicType,
    regExp=
        safe_text
)
model::ScopedTopicType_strategy = st.builds(
    model::ScopedTopicType,
)
model::RoleType_strategy = st.builds(
    model::RoleType,
)
Node_strategy = st.builds(
    Node,
)
model::Comment_strategy = st.builds(
    model::Comment,
    width=
        st.integers(),
    height=
        st.integers(),
    content=
        safe_text
)
model::TypeNode_strategy = st.builds(
    model::TypeNode,
    image=
        safe_text
)
OnoObject_strategy = st.builds(
    OnoObject,
)
model::File_strategy = st.builds(
    model::File,
    dirty=
        st.booleans(),
    filename=
        safe_text,
    notes=
        safe_text
)
model::TMCLConstruct_strategy = st.builds(
    model::TMCLConstruct,
    see_also=
        safe_text,
    comment=
        safe_text,
    description=
        safe_text
)
model::Node_strategy = st.builds(
    model::Node,
    posX=
        st.integers(),
    posY=
        st.integers()
)
model::Annotation_strategy = st.builds(
    model::Annotation,
    value=
        safe_text,
    key=
        safe_text
)
model::Bendpoint_strategy = st.builds(
    model::Bendpoint,
    posY=
        st.integers(),
    posX=
        st.integers()
)
model::Edge_strategy = st.builds(
    model::Edge,
    type=
        safe_text
)
model::LabelPos_strategy = st.builds(
    model::LabelPos,
    posX=
        st.integers(),
    posY=
        st.integers()
)
model::Diagram_strategy = st.builds(
    model::Diagram,
    name=
        safe_text
)
AbstractTypedConstraint_strategy = st.builds(
    AbstractTypedConstraint,
)
model::AssociationNode_strategy = st.builds(
    model::AssociationNode,
)
model::MappingElement_strategy = st.builds(
    model::MappingElement,
    value=
        safe_text,
    key=
        safe_text
)
model::AssociationTypeConstraint_strategy = st.builds(
    model::AssociationTypeConstraint,
)
AbstractCardinalityConstraint_strategy = st.builds(
    AbstractCardinalityConstraint,
)
model::AbstractTypedCardinalityConstraint_strategy = st.builds(
    model::AbstractTypedCardinalityConstraint,
)
model::RolePlayerConstraint_strategy = st.builds(
    model::RolePlayerConstraint,
)
AbstractTypedCardinalityConstraint_strategy = st.builds(
    AbstractTypedCardinalityConstraint,
)
model::NameTypeConstraint_strategy = st.builds(
    model::NameTypeConstraint,
)
model::ScopeConstraint_strategy = st.builds(
    model::ScopeConstraint,
)
model::OccurrenceTypeConstraint_strategy = st.builds(
    model::OccurrenceTypeConstraint,
)
model::RoleConstraint_strategy = st.builds(
    model::RoleConstraint,
)
model::ReifierConstraint_strategy = st.builds(
    model::ReifierConstraint,
)
AbstractConstraint_strategy = st.builds(
    AbstractConstraint,
)
model::RoleCombinationConstraint_strategy = st.builds(
    model::RoleCombinationConstraint,
)
model::AbstractTypedConstraint_strategy = st.builds(
    model::AbstractTypedConstraint,
)
model::AbstractCardinalityConstraint_strategy = st.builds(
    model::AbstractCardinalityConstraint,
    cardMax=
        safe_text,
    cardMin=
        safe_text
)
model::AbstractRegExpConstraint_strategy = st.builds(
    model::AbstractRegExpConstraint,
    regexp=
        safe_text
)
model::TopicReifiesConstraint_strategy = st.builds(
    model::TopicReifiesConstraint,
)
AbstractRegExpConstraint_strategy = st.builds(
    AbstractRegExpConstraint,
)
model::ItemIdentifierConstraint_strategy = st.builds(
    model::ItemIdentifierConstraint,
)
model::SubjectLocatorConstraint_strategy = st.builds(
    model::SubjectLocatorConstraint,
)
model::SubjectIdentifierConstraint_strategy = st.builds(
    model::SubjectIdentifierConstraint,
)
TMCLConstruct_strategy = st.builds(
    TMCLConstruct,
)
model::AbstractConstraint_strategy = st.builds(
    model::AbstractConstraint,
)
model::TopicMapSchema_strategy = st.builds(
    model::TopicMapSchema,
    baseLocator=
        safe_text,
    name=
        safe_text,
    includes=
        safe_text,
    version=
        safe_text,
    schemaResource=
        safe_text
)
model::TopicType_strategy = st.builds(
    model::TopicType,
    name=
        safe_text,
    idType=
        safe_text,
    kind=
        safe_text,
    locators=
        safe_text,
    identifiers=
        safe_text,
    abstract=
        st.booleans()
)

@given(instance=model::OnoObject_strategy)
@settings(max_examples=50)
def test_model::onoobject_instantiation(instance):
    assert isinstance(instance, model::OnoObject)

@given(instance=model::OnoObject_strategy)
def test_model::onoobject_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=model::OnoObject_strategy)
def test_model::onoobject_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Diagram_strategy)
@settings(max_examples=50)
def test_diagram_instantiation(instance):
    assert isinstance(instance, Diagram)

@given(instance=model::DomainDiagram_strategy)
@settings(max_examples=50)
def test_model::domaindiagram_instantiation(instance):
    assert isinstance(instance, model::DomainDiagram)

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

@given(instance=model::ScopedReifiableTopicType_strategy)
@settings(max_examples=50)
def test_model::scopedreifiabletopictype_instantiation(instance):
    assert isinstance(instance, model::ScopedReifiableTopicType)

@given(instance=model::OccurrenceType_strategy)
@settings(max_examples=50)
def test_model::occurrencetype_instantiation(instance):
    assert isinstance(instance, model::OccurrenceType)

@given(instance=model::OccurrenceType_strategy)
def test_model::occurrencetype_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=model::OccurrenceType_strategy)
def test_model::occurrencetype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=model::NameType_strategy)
@settings(max_examples=50)
def test_model::nametype_instantiation(instance):
    assert isinstance(instance, model::NameType)

@given(instance=model::AssociationType_strategy)
@settings(max_examples=50)
def test_model::associationtype_instantiation(instance):
    assert isinstance(instance, model::AssociationType)

@given(instance=TopicType_strategy)
@settings(max_examples=50)
def test_topictype_instantiation(instance):
    assert isinstance(instance, TopicType)

@given(instance=model::AbstractUniqueValueTopicType_strategy)
@settings(max_examples=50)
def test_model::abstractuniquevaluetopictype_instantiation(instance):
    assert isinstance(instance, model::AbstractUniqueValueTopicType)

@given(instance=model::AbstractUniqueValueTopicType_strategy)
def test_model::abstractuniquevaluetopictype_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=model::AbstractUniqueValueTopicType_strategy)
def test_model::abstractuniquevaluetopictype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=model::ReifiableTopicType_strategy)
@settings(max_examples=50)
def test_model::reifiabletopictype_instantiation(instance):
    assert isinstance(instance, model::ReifiableTopicType)

@given(instance=model::AbstractRegExpTopicType_strategy)
@settings(max_examples=50)
def test_model::abstractregexptopictype_instantiation(instance):
    assert isinstance(instance, model::AbstractRegExpTopicType)

@given(instance=model::AbstractRegExpTopicType_strategy)
def test_model::abstractregexptopictype_regExp_type(instance):
    assert isinstance(instance.regExp, str)


@given(instance=model::AbstractRegExpTopicType_strategy)
def test_model::abstractregexptopictype_regExp_setter(instance):
    original = instance.regExp
    instance.regExp = original
    assert instance.regExp == original

@given(instance=model::ScopedTopicType_strategy)
@settings(max_examples=50)
def test_model::scopedtopictype_instantiation(instance):
    assert isinstance(instance, model::ScopedTopicType)

@given(instance=model::RoleType_strategy)
@settings(max_examples=50)
def test_model::roletype_instantiation(instance):
    assert isinstance(instance, model::RoleType)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=model::Comment_strategy)
@settings(max_examples=50)
def test_model::comment_instantiation(instance):
    assert isinstance(instance, model::Comment)

@given(instance=model::Comment_strategy)
def test_model::comment_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=model::Comment_strategy)
def test_model::comment_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=model::Comment_strategy)
def test_model::comment_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=model::Comment_strategy)
def test_model::comment_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=model::Comment_strategy)
def test_model::comment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=model::Comment_strategy)
def test_model::comment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=model::TypeNode_strategy)
@settings(max_examples=50)
def test_model::typenode_instantiation(instance):
    assert isinstance(instance, model::TypeNode)

@given(instance=model::TypeNode_strategy)
def test_model::typenode_image_type(instance):
    assert isinstance(instance.image, str)


@given(instance=model::TypeNode_strategy)
def test_model::typenode_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original

@given(instance=OnoObject_strategy)
@settings(max_examples=50)
def test_onoobject_instantiation(instance):
    assert isinstance(instance, OnoObject)

@given(instance=model::File_strategy)
@settings(max_examples=50)
def test_model::file_instantiation(instance):
    assert isinstance(instance, model::File)

@given(instance=model::File_strategy)
def test_model::file_dirty_type(instance):
    assert isinstance(instance.dirty, bool)


@given(instance=model::File_strategy)
def test_model::file_dirty_setter(instance):
    original = instance.dirty
    instance.dirty = original
    assert instance.dirty == original

@given(instance=model::File_strategy)
def test_model::file_filename_type(instance):
    assert isinstance(instance.filename, str)


@given(instance=model::File_strategy)
def test_model::file_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=model::File_strategy)
def test_model::file_notes_type(instance):
    assert isinstance(instance.notes, str)


@given(instance=model::File_strategy)
def test_model::file_notes_setter(instance):
    original = instance.notes
    instance.notes = original
    assert instance.notes == original

@given(instance=model::TMCLConstruct_strategy)
@settings(max_examples=50)
def test_model::tmclconstruct_instantiation(instance):
    assert isinstance(instance, model::TMCLConstruct)

@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_see_also_type(instance):
    assert isinstance(instance.see_also, str)


@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_see_also_setter(instance):
    original = instance.see_also
    instance.see_also = original
    assert instance.see_also == original

@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=model::TMCLConstruct_strategy)
def test_model::tmclconstruct_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=model::Node_strategy)
@settings(max_examples=50)
def test_model::node_instantiation(instance):
    assert isinstance(instance, model::Node)

@given(instance=model::Node_strategy)
def test_model::node_posX_type(instance):
    assert isinstance(instance.posX, int)


@given(instance=model::Node_strategy)
def test_model::node_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model::Node_strategy)
def test_model::node_posY_type(instance):
    assert isinstance(instance.posY, int)


@given(instance=model::Node_strategy)
def test_model::node_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model::Annotation_strategy)
@settings(max_examples=50)
def test_model::annotation_instantiation(instance):
    assert isinstance(instance, model::Annotation)

@given(instance=model::Annotation_strategy)
def test_model::annotation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::Annotation_strategy)
def test_model::annotation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::Annotation_strategy)
def test_model::annotation_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::Annotation_strategy)
def test_model::annotation_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model::Bendpoint_strategy)
@settings(max_examples=50)
def test_model::bendpoint_instantiation(instance):
    assert isinstance(instance, model::Bendpoint)

@given(instance=model::Bendpoint_strategy)
def test_model::bendpoint_posY_type(instance):
    assert isinstance(instance.posY, int)


@given(instance=model::Bendpoint_strategy)
def test_model::bendpoint_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model::Bendpoint_strategy)
def test_model::bendpoint_posX_type(instance):
    assert isinstance(instance.posX, int)


@given(instance=model::Bendpoint_strategy)
def test_model::bendpoint_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model::Edge_strategy)
@settings(max_examples=50)
def test_model::edge_instantiation(instance):
    assert isinstance(instance, model::Edge)

@given(instance=model::Edge_strategy)
def test_model::edge_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=model::Edge_strategy)
def test_model::edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=model::LabelPos_strategy)
@settings(max_examples=50)
def test_model::labelpos_instantiation(instance):
    assert isinstance(instance, model::LabelPos)

@given(instance=model::LabelPos_strategy)
def test_model::labelpos_posX_type(instance):
    assert isinstance(instance.posX, int)


@given(instance=model::LabelPos_strategy)
def test_model::labelpos_posX_setter(instance):
    original = instance.posX
    instance.posX = original
    assert instance.posX == original

@given(instance=model::LabelPos_strategy)
def test_model::labelpos_posY_type(instance):
    assert isinstance(instance.posY, int)


@given(instance=model::LabelPos_strategy)
def test_model::labelpos_posY_setter(instance):
    original = instance.posY
    instance.posY = original
    assert instance.posY == original

@given(instance=model::Diagram_strategy)
@settings(max_examples=50)
def test_model::diagram_instantiation(instance):
    assert isinstance(instance, model::Diagram)

@given(instance=model::Diagram_strategy)
def test_model::diagram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Diagram_strategy)
def test_model::diagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AbstractTypedConstraint_strategy)
@settings(max_examples=50)
def test_abstracttypedconstraint_instantiation(instance):
    assert isinstance(instance, AbstractTypedConstraint)

@given(instance=model::AssociationNode_strategy)
@settings(max_examples=50)
def test_model::associationnode_instantiation(instance):
    assert isinstance(instance, model::AssociationNode)

@given(instance=model::MappingElement_strategy)
@settings(max_examples=50)
def test_model::mappingelement_instantiation(instance):
    assert isinstance(instance, model::MappingElement)

@given(instance=model::MappingElement_strategy)
def test_model::mappingelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=model::MappingElement_strategy)
def test_model::mappingelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=model::MappingElement_strategy)
def test_model::mappingelement_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=model::MappingElement_strategy)
def test_model::mappingelement_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=model::AssociationTypeConstraint_strategy)
@settings(max_examples=50)
def test_model::associationtypeconstraint_instantiation(instance):
    assert isinstance(instance, model::AssociationTypeConstraint)

@given(instance=AbstractCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_abstractcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, AbstractCardinalityConstraint)

@given(instance=model::AbstractTypedCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_model::abstracttypedcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, model::AbstractTypedCardinalityConstraint)

@given(instance=model::RolePlayerConstraint_strategy)
@settings(max_examples=50)
def test_model::roleplayerconstraint_instantiation(instance):
    assert isinstance(instance, model::RolePlayerConstraint)

@given(instance=AbstractTypedCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_abstracttypedcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, AbstractTypedCardinalityConstraint)

@given(instance=model::NameTypeConstraint_strategy)
@settings(max_examples=50)
def test_model::nametypeconstraint_instantiation(instance):
    assert isinstance(instance, model::NameTypeConstraint)

@given(instance=model::ScopeConstraint_strategy)
@settings(max_examples=50)
def test_model::scopeconstraint_instantiation(instance):
    assert isinstance(instance, model::ScopeConstraint)

@given(instance=model::OccurrenceTypeConstraint_strategy)
@settings(max_examples=50)
def test_model::occurrencetypeconstraint_instantiation(instance):
    assert isinstance(instance, model::OccurrenceTypeConstraint)

@given(instance=model::RoleConstraint_strategy)
@settings(max_examples=50)
def test_model::roleconstraint_instantiation(instance):
    assert isinstance(instance, model::RoleConstraint)

@given(instance=model::ReifierConstraint_strategy)
@settings(max_examples=50)
def test_model::reifierconstraint_instantiation(instance):
    assert isinstance(instance, model::ReifierConstraint)

@given(instance=AbstractConstraint_strategy)
@settings(max_examples=50)
def test_abstractconstraint_instantiation(instance):
    assert isinstance(instance, AbstractConstraint)

@given(instance=model::RoleCombinationConstraint_strategy)
@settings(max_examples=50)
def test_model::rolecombinationconstraint_instantiation(instance):
    assert isinstance(instance, model::RoleCombinationConstraint)

@given(instance=model::AbstractTypedConstraint_strategy)
@settings(max_examples=50)
def test_model::abstracttypedconstraint_instantiation(instance):
    assert isinstance(instance, model::AbstractTypedConstraint)

@given(instance=model::AbstractCardinalityConstraint_strategy)
@settings(max_examples=50)
def test_model::abstractcardinalityconstraint_instantiation(instance):
    assert isinstance(instance, model::AbstractCardinalityConstraint)

@given(instance=model::AbstractCardinalityConstraint_strategy)
def test_model::abstractcardinalityconstraint_cardMax_type(instance):
    assert isinstance(instance.cardMax, str)


@given(instance=model::AbstractCardinalityConstraint_strategy)
def test_model::abstractcardinalityconstraint_cardMax_setter(instance):
    original = instance.cardMax
    instance.cardMax = original
    assert instance.cardMax == original

@given(instance=model::AbstractCardinalityConstraint_strategy)
def test_model::abstractcardinalityconstraint_cardMin_type(instance):
    assert isinstance(instance.cardMin, str)


@given(instance=model::AbstractCardinalityConstraint_strategy)
def test_model::abstractcardinalityconstraint_cardMin_setter(instance):
    original = instance.cardMin
    instance.cardMin = original
    assert instance.cardMin == original

@given(instance=model::AbstractRegExpConstraint_strategy)
@settings(max_examples=50)
def test_model::abstractregexpconstraint_instantiation(instance):
    assert isinstance(instance, model::AbstractRegExpConstraint)

@given(instance=model::AbstractRegExpConstraint_strategy)
def test_model::abstractregexpconstraint_regexp_type(instance):
    assert isinstance(instance.regexp, str)


@given(instance=model::AbstractRegExpConstraint_strategy)
def test_model::abstractregexpconstraint_regexp_setter(instance):
    original = instance.regexp
    instance.regexp = original
    assert instance.regexp == original

@given(instance=model::TopicReifiesConstraint_strategy)
@settings(max_examples=50)
def test_model::topicreifiesconstraint_instantiation(instance):
    assert isinstance(instance, model::TopicReifiesConstraint)

@given(instance=AbstractRegExpConstraint_strategy)
@settings(max_examples=50)
def test_abstractregexpconstraint_instantiation(instance):
    assert isinstance(instance, AbstractRegExpConstraint)

@given(instance=model::ItemIdentifierConstraint_strategy)
@settings(max_examples=50)
def test_model::itemidentifierconstraint_instantiation(instance):
    assert isinstance(instance, model::ItemIdentifierConstraint)

@given(instance=model::SubjectLocatorConstraint_strategy)
@settings(max_examples=50)
def test_model::subjectlocatorconstraint_instantiation(instance):
    assert isinstance(instance, model::SubjectLocatorConstraint)

@given(instance=model::SubjectIdentifierConstraint_strategy)
@settings(max_examples=50)
def test_model::subjectidentifierconstraint_instantiation(instance):
    assert isinstance(instance, model::SubjectIdentifierConstraint)

@given(instance=TMCLConstruct_strategy)
@settings(max_examples=50)
def test_tmclconstruct_instantiation(instance):
    assert isinstance(instance, TMCLConstruct)

@given(instance=model::AbstractConstraint_strategy)
@settings(max_examples=50)
def test_model::abstractconstraint_instantiation(instance):
    assert isinstance(instance, model::AbstractConstraint)

@given(instance=model::TopicMapSchema_strategy)
@settings(max_examples=50)
def test_model::topicmapschema_instantiation(instance):
    assert isinstance(instance, model::TopicMapSchema)

@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_baseLocator_type(instance):
    assert isinstance(instance.baseLocator, str)


@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_baseLocator_setter(instance):
    original = instance.baseLocator
    instance.baseLocator = original
    assert instance.baseLocator == original

@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_includes_type(instance):
    assert isinstance(instance.includes, str)


@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original

@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_schemaResource_type(instance):
    assert isinstance(instance.schemaResource, str)


@given(instance=model::TopicMapSchema_strategy)
def test_model::topicmapschema_schemaResource_setter(instance):
    original = instance.schemaResource
    instance.schemaResource = original
    assert instance.schemaResource == original

@given(instance=model::TopicType_strategy)
@settings(max_examples=50)
def test_model::topictype_instantiation(instance):
    assert isinstance(instance, model::TopicType)

@given(instance=model::TopicType_strategy)
def test_model::topictype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::TopicType_strategy)
def test_model::topictype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::TopicType_strategy)
def test_model::topictype_idType_type(instance):
    assert isinstance(instance.idType, str)


@given(instance=model::TopicType_strategy)
def test_model::topictype_idType_setter(instance):
    original = instance.idType
    instance.idType = original
    assert instance.idType == original

@given(instance=model::TopicType_strategy)
def test_model::topictype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=model::TopicType_strategy)
def test_model::topictype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=model::TopicType_strategy)
def test_model::topictype_locators_type(instance):
    assert isinstance(instance.locators, str)


@given(instance=model::TopicType_strategy)
def test_model::topictype_locators_setter(instance):
    original = instance.locators
    instance.locators = original
    assert instance.locators == original

@given(instance=model::TopicType_strategy)
def test_model::topictype_identifiers_type(instance):
    assert isinstance(instance.identifiers, str)


@given(instance=model::TopicType_strategy)
def test_model::topictype_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=model::TopicType_strategy)
def test_model::topictype_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=model::TopicType_strategy)
def test_model::topictype_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original
