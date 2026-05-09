import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relation,
    umlclassdiagram::Aggregation,
    umlclassdiagram::Association,
    umlclassdiagram::Composition,
    umlclassdiagram::Dependency,
    Modifier,
    umlclassdiagram::Operator,
    Feature,
    umlclassdiagram::Operation,
    umlclassdiagram::Attribute,
    Classifier,
    umlclassdiagram::Class,
    umlclassdiagram::AssociationClass,
    NavigationPathCS,
    umlclassdiagram::NavigationPathElementCS,
    umlclassdiagram::NavigationPathVariableCS,
    umlclassdiagram::NavigationPathCS,
    NamedElement,
    umlclassdiagram::Parameter,
    umlclassdiagram::Modifier,
    umlclassdiagram::NamedElement,
    umlclassdiagram::Constraint,
    umlclassdiagram::PrimitiveElement,
    umlclassdiagram::Relation,
    umlclassdiagram::Classifier,
    umlclassdiagram::ClassDiagram,
    umlclassdiagram::AccVarCS,
    LoopExpCS,
    umlclassdiagram::ForAllExpCS,
    umlclassdiagram::IterateExpCS,
    umlclassdiagram::CollectExpCS,
    umlclassdiagram::IteratorVarCS,
    umlclassdiagram::NavigationPathNameCS,
    umlclassdiagram::ExistsExpCS,
    BooleanLiteralExpCS,
    umlclassdiagram::BooleanExpCS,
    umlclassdiagram::Feature,
    PathCS,
    umlclassdiagram::PathElementCS,
    umlclassdiagram::PathVariableCS,
    umlclassdiagram::PathCS,
    LiteralExpCS,
    umlclassdiagram::StringLiteralExpCS,
    umlclassdiagram::BooleanLiteralExpCS,
    umlclassdiagram::IntLiteralExpCS,
    umlclassdiagram::InvariantCS,
    umlclassdiagram::ExpCS,
    umlclassdiagram::RoundedBracketClauseCS,
    NavigationExpCS,
    umlclassdiagram::LoopExpCS,
    umlclassdiagram::NavigationNameExpCS,
    umlclassdiagram::NameExpCS,
    PrimaryExpCS,
    umlclassdiagram::LiteralExpCS,
    CallExpCS,
    umlclassdiagram::PrimaryExpCS,
    umlclassdiagram::NavigationExpCS,
    LogicExpCS,
    umlclassdiagram::CallExpCS,
    ExpCS,
    umlclassdiagram::LogicExpCS,
    umlclassdiagram::ParameterCS,
    umlclassdiagram::OperationCS,
    umlclassdiagram::PropertyCS,
    umlclassdiagram::PathNameCS,
    umlclassdiagram::ClassCS,
    umlclassdiagram::ConstraintCS,
    umlclassdiagram::PackageCS,
    umlclassdiagram::RootCS,
    PrimitiveDataType,
    ScopeType,
    OperatorType,
    VisbilityType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::aggregation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Aggregation)


def test_umlclassdiagram::aggregation_constructor_exists():
    assert callable(umlclassdiagram::Aggregation.__init__)


def test_umlclassdiagram::aggregation_constructor_args():
    sig = inspect.signature(umlclassdiagram::Aggregation.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::association_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Association)


def test_umlclassdiagram::association_constructor_exists():
    assert callable(umlclassdiagram::Association.__init__)


def test_umlclassdiagram::association_constructor_args():
    sig = inspect.signature(umlclassdiagram::Association.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::composition_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Composition)


def test_umlclassdiagram::composition_constructor_exists():
    assert callable(umlclassdiagram::Composition.__init__)


def test_umlclassdiagram::composition_constructor_args():
    sig = inspect.signature(umlclassdiagram::Composition.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::dependency_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Dependency)


def test_umlclassdiagram::dependency_constructor_exists():
    assert callable(umlclassdiagram::Dependency.__init__)


def test_umlclassdiagram::dependency_constructor_args():
    sig = inspect.signature(umlclassdiagram::Dependency.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::operator_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Operator)


def test_umlclassdiagram::operator_constructor_exists():
    assert callable(umlclassdiagram::Operator.__init__)


def test_umlclassdiagram::operator_constructor_args():
    sig = inspect.signature(umlclassdiagram::Operator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_umlclassdiagram::operator_has_operator():
    assert hasattr(umlclassdiagram::Operator, "operator")
    descriptor = None
    for klass in umlclassdiagram::Operator.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::operation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Operation)


def test_umlclassdiagram::operation_constructor_exists():
    assert callable(umlclassdiagram::Operation.__init__)


def test_umlclassdiagram::operation_constructor_args():
    sig = inspect.signature(umlclassdiagram::Operation.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Attribute)


def test_umlclassdiagram::attribute_constructor_exists():
    assert callable(umlclassdiagram::Attribute.__init__)


def test_umlclassdiagram::attribute_constructor_args():
    sig = inspect.signature(umlclassdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_umlclassdiagram::attribute_has_derived():
    assert hasattr(umlclassdiagram::Attribute, "derived")
    descriptor = None
    for klass in umlclassdiagram::Attribute.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::class_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Class)


def test_umlclassdiagram::class_constructor_exists():
    assert callable(umlclassdiagram::Class.__init__)


def test_umlclassdiagram::class_constructor_args():
    sig = inspect.signature(umlclassdiagram::Class.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::associationclass_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::AssociationClass)


def test_umlclassdiagram::associationclass_constructor_exists():
    assert callable(umlclassdiagram::AssociationClass.__init__)


def test_umlclassdiagram::associationclass_constructor_args():
    sig = inspect.signature(umlclassdiagram::AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationPathElementCS)


def test_umlclassdiagram::navigationpathelementcs_constructor_exists():
    assert callable(umlclassdiagram::NavigationPathElementCS.__init__)


def test_umlclassdiagram::navigationpathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationPathVariableCS)


def test_umlclassdiagram::navigationpathvariablecs_constructor_exists():
    assert callable(umlclassdiagram::NavigationPathVariableCS.__init__)


def test_umlclassdiagram::navigationpathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_umlclassdiagram::navigationpathvariablecs_has_varName():
    assert hasattr(umlclassdiagram::NavigationPathVariableCS, "varName")
    descriptor = None
    for klass in umlclassdiagram::NavigationPathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationPathCS)


def test_umlclassdiagram::navigationpathcs_constructor_exists():
    assert callable(umlclassdiagram::NavigationPathCS.__init__)


def test_umlclassdiagram::navigationpathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::parameter_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Parameter)


def test_umlclassdiagram::parameter_constructor_exists():
    assert callable(umlclassdiagram::Parameter.__init__)


def test_umlclassdiagram::parameter_constructor_args():
    sig = inspect.signature(umlclassdiagram::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::modifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Modifier)


def test_umlclassdiagram::modifier_constructor_exists():
    assert callable(umlclassdiagram::Modifier.__init__)


def test_umlclassdiagram::modifier_constructor_args():
    sig = inspect.signature(umlclassdiagram::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_umlclassdiagram::modifier_has_visibility():
    assert hasattr(umlclassdiagram::Modifier, "visibility")
    descriptor = None
    for klass in umlclassdiagram::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::modifier_has_scope():
    assert hasattr(umlclassdiagram::Modifier, "scope")
    descriptor = None
    for klass in umlclassdiagram::Modifier.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NamedElement)


def test_umlclassdiagram::namedelement_constructor_exists():
    assert callable(umlclassdiagram::NamedElement.__init__)


def test_umlclassdiagram::namedelement_constructor_args():
    sig = inspect.signature(umlclassdiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::namedelement_has_name():
    assert hasattr(umlclassdiagram::NamedElement, "name")
    descriptor = None
    for klass in umlclassdiagram::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::constraint_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Constraint)


def test_umlclassdiagram::constraint_constructor_exists():
    assert callable(umlclassdiagram::Constraint.__init__)


def test_umlclassdiagram::constraint_constructor_args():
    sig = inspect.signature(umlclassdiagram::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_umlclassdiagram::constraint_has_id():
    assert hasattr(umlclassdiagram::Constraint, "id")
    descriptor = None
    for klass in umlclassdiagram::Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::primitiveelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PrimitiveElement)


def test_umlclassdiagram::primitiveelement_constructor_exists():
    assert callable(umlclassdiagram::PrimitiveElement.__init__)


def test_umlclassdiagram::primitiveelement_constructor_args():
    sig = inspect.signature(umlclassdiagram::PrimitiveElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlclassdiagram::primitiveelement_has_type():
    assert hasattr(umlclassdiagram::PrimitiveElement, "type")
    descriptor = None
    for klass in umlclassdiagram::PrimitiveElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::relation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Relation)


def test_umlclassdiagram::relation_constructor_exists():
    assert callable(umlclassdiagram::Relation.__init__)


def test_umlclassdiagram::relation_constructor_args():
    sig = inspect.signature(umlclassdiagram::Relation.__init__)
    params = list(sig.parameters.keys())
    assert "nsrc" in params, "Missing parameter 'nsrc'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "ntar" in params, "Missing parameter 'ntar'"

def test_umlclassdiagram::relation_has_nsrc():
    assert hasattr(umlclassdiagram::Relation, "nsrc")
    descriptor = None
    for klass in umlclassdiagram::Relation.__mro__:
        if "nsrc" in klass.__dict__:
            descriptor = klass.__dict__["nsrc"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::relation_has_derived():
    assert hasattr(umlclassdiagram::Relation, "derived")
    descriptor = None
    for klass in umlclassdiagram::Relation.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::relation_has_ntar():
    assert hasattr(umlclassdiagram::Relation, "ntar")
    descriptor = None
    for klass in umlclassdiagram::Relation.__mro__:
        if "ntar" in klass.__dict__:
            descriptor = klass.__dict__["ntar"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::classifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Classifier)


def test_umlclassdiagram::classifier_constructor_exists():
    assert callable(umlclassdiagram::Classifier.__init__)


def test_umlclassdiagram::classifier_constructor_args():
    sig = inspect.signature(umlclassdiagram::Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_umlclassdiagram::classifier_has_derived():
    assert hasattr(umlclassdiagram::Classifier, "derived")
    descriptor = None
    for klass in umlclassdiagram::Classifier.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::classifier_has_abstract():
    assert hasattr(umlclassdiagram::Classifier, "abstract")
    descriptor = None
    for klass in umlclassdiagram::Classifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::classdiagram_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ClassDiagram)


def test_umlclassdiagram::classdiagram_constructor_exists():
    assert callable(umlclassdiagram::ClassDiagram.__init__)


def test_umlclassdiagram::classdiagram_constructor_args():
    sig = inspect.signature(umlclassdiagram::ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::accvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::AccVarCS)


def test_umlclassdiagram::accvarcs_constructor_exists():
    assert callable(umlclassdiagram::AccVarCS.__init__)


def test_umlclassdiagram::accvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"

def test_umlclassdiagram::accvarcs_has_accVarName():
    assert hasattr(umlclassdiagram::AccVarCS, "accVarName")
    descriptor = None
    for klass in umlclassdiagram::AccVarCS.__mro__:
        if "accVarName" in klass.__dict__:
            descriptor = klass.__dict__["accVarName"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::forallexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ForAllExpCS)


def test_umlclassdiagram::forallexpcs_constructor_exists():
    assert callable(umlclassdiagram::ForAllExpCS.__init__)


def test_umlclassdiagram::forallexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::IterateExpCS)


def test_umlclassdiagram::iterateexpcs_constructor_exists():
    assert callable(umlclassdiagram::IterateExpCS.__init__)


def test_umlclassdiagram::iterateexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::collectexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::CollectExpCS)


def test_umlclassdiagram::collectexpcs_constructor_exists():
    assert callable(umlclassdiagram::CollectExpCS.__init__)


def test_umlclassdiagram::collectexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::IteratorVarCS)


def test_umlclassdiagram::iteratorvarcs_constructor_exists():
    assert callable(umlclassdiagram::IteratorVarCS.__init__)


def test_umlclassdiagram::iteratorvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_umlclassdiagram::iteratorvarcs_has_itName():
    assert hasattr(umlclassdiagram::IteratorVarCS, "itName")
    descriptor = None
    for klass in umlclassdiagram::IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationPathNameCS)


def test_umlclassdiagram::navigationpathnamecs_constructor_exists():
    assert callable(umlclassdiagram::NavigationPathNameCS.__init__)


def test_umlclassdiagram::navigationpathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::existsexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ExistsExpCS)


def test_umlclassdiagram::existsexpcs_constructor_exists():
    assert callable(umlclassdiagram::ExistsExpCS.__init__)


def test_umlclassdiagram::existsexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::BooleanExpCS)


def test_umlclassdiagram::booleanexpcs_constructor_exists():
    assert callable(umlclassdiagram::BooleanExpCS.__init__)


def test_umlclassdiagram::booleanexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_umlclassdiagram::booleanexpcs_has_boolSymbol():
    assert hasattr(umlclassdiagram::BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in umlclassdiagram::BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::feature_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::Feature)


def test_umlclassdiagram::feature_constructor_exists():
    assert callable(umlclassdiagram::Feature.__init__)


def test_umlclassdiagram::feature_constructor_args():
    sig = inspect.signature(umlclassdiagram::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "scope" in params, "Missing parameter 'scope'"

def test_umlclassdiagram::feature_has_name():
    assert hasattr(umlclassdiagram::Feature, "name")
    descriptor = None
    for klass in umlclassdiagram::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::feature_has_visibility():
    assert hasattr(umlclassdiagram::Feature, "visibility")
    descriptor = None
    for klass in umlclassdiagram::Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram::feature_has_scope():
    assert hasattr(umlclassdiagram::Feature, "scope")
    descriptor = None
    for klass in umlclassdiagram::Feature.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PathElementCS)


def test_umlclassdiagram::pathelementcs_constructor_exists():
    assert callable(umlclassdiagram::PathElementCS.__init__)


def test_umlclassdiagram::pathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PathVariableCS)


def test_umlclassdiagram::pathvariablecs_constructor_exists():
    assert callable(umlclassdiagram::PathVariableCS.__init__)


def test_umlclassdiagram::pathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_umlclassdiagram::pathvariablecs_has_varName():
    assert hasattr(umlclassdiagram::PathVariableCS, "varName")
    descriptor = None
    for klass in umlclassdiagram::PathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::pathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PathCS)


def test_umlclassdiagram::pathcs_constructor_exists():
    assert callable(umlclassdiagram::PathCS.__init__)


def test_umlclassdiagram::pathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PathCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::StringLiteralExpCS)


def test_umlclassdiagram::stringliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram::StringLiteralExpCS.__init__)


def test_umlclassdiagram::stringliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_umlclassdiagram::stringliteralexpcs_has_stringSymbol():
    assert hasattr(umlclassdiagram::StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in umlclassdiagram::StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::BooleanLiteralExpCS)


def test_umlclassdiagram::booleanliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram::BooleanLiteralExpCS.__init__)


def test_umlclassdiagram::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::IntLiteralExpCS)


def test_umlclassdiagram::intliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram::IntLiteralExpCS.__init__)


def test_umlclassdiagram::intliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_umlclassdiagram::intliteralexpcs_has_intSymbol():
    assert hasattr(umlclassdiagram::IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in umlclassdiagram::IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::invariantcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::InvariantCS)


def test_umlclassdiagram::invariantcs_constructor_exists():
    assert callable(umlclassdiagram::InvariantCS.__init__)


def test_umlclassdiagram::invariantcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::expcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ExpCS)


def test_umlclassdiagram::expcs_constructor_exists():
    assert callable(umlclassdiagram::ExpCS.__init__)


def test_umlclassdiagram::expcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::RoundedBracketClauseCS)


def test_umlclassdiagram::roundedbracketclausecs_constructor_exists():
    assert callable(umlclassdiagram::RoundedBracketClauseCS.__init__)


def test_umlclassdiagram::roundedbracketclausecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::loopexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::LoopExpCS)


def test_umlclassdiagram::loopexpcs_constructor_exists():
    assert callable(umlclassdiagram::LoopExpCS.__init__)


def test_umlclassdiagram::loopexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"

def test_umlclassdiagram::loopexpcs_has_logicOp():
    assert hasattr(umlclassdiagram::LoopExpCS, "logicOp")
    descriptor = None
    for klass in umlclassdiagram::LoopExpCS.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationNameExpCS)


def test_umlclassdiagram::navigationnameexpcs_constructor_exists():
    assert callable(umlclassdiagram::NavigationNameExpCS.__init__)


def test_umlclassdiagram::navigationnameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NameExpCS)


def test_umlclassdiagram::nameexpcs_constructor_exists():
    assert callable(umlclassdiagram::NameExpCS.__init__)


def test_umlclassdiagram::nameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::LiteralExpCS)


def test_umlclassdiagram::literalexpcs_constructor_exists():
    assert callable(umlclassdiagram::LiteralExpCS.__init__)


def test_umlclassdiagram::literalexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PrimaryExpCS)


def test_umlclassdiagram::primaryexpcs_constructor_exists():
    assert callable(umlclassdiagram::PrimaryExpCS.__init__)


def test_umlclassdiagram::primaryexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::NavigationExpCS)


def test_umlclassdiagram::navigationexpcs_constructor_exists():
    assert callable(umlclassdiagram::NavigationExpCS.__init__)


def test_umlclassdiagram::navigationexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::callexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::CallExpCS)


def test_umlclassdiagram::callexpcs_constructor_exists():
    assert callable(umlclassdiagram::CallExpCS.__init__)


def test_umlclassdiagram::callexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::logicexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::LogicExpCS)


def test_umlclassdiagram::logicexpcs_constructor_exists():
    assert callable(umlclassdiagram::LogicExpCS.__init__)


def test_umlclassdiagram::logicexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_umlclassdiagram::logicexpcs_has_op():
    assert hasattr(umlclassdiagram::LogicExpCS, "op")
    descriptor = None
    for klass in umlclassdiagram::LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::parametercs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ParameterCS)


def test_umlclassdiagram::parametercs_constructor_exists():
    assert callable(umlclassdiagram::ParameterCS.__init__)


def test_umlclassdiagram::parametercs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::parametercs_has_name():
    assert hasattr(umlclassdiagram::ParameterCS, "name")
    descriptor = None
    for klass in umlclassdiagram::ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::operationcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::OperationCS)


def test_umlclassdiagram::operationcs_constructor_exists():
    assert callable(umlclassdiagram::OperationCS.__init__)


def test_umlclassdiagram::operationcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::operationcs_has_name():
    assert hasattr(umlclassdiagram::OperationCS, "name")
    descriptor = None
    for klass in umlclassdiagram::OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::propertycs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PropertyCS)


def test_umlclassdiagram::propertycs_constructor_exists():
    assert callable(umlclassdiagram::PropertyCS.__init__)


def test_umlclassdiagram::propertycs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::propertycs_has_name():
    assert hasattr(umlclassdiagram::PropertyCS, "name")
    descriptor = None
    for klass in umlclassdiagram::PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PathNameCS)


def test_umlclassdiagram::pathnamecs_constructor_exists():
    assert callable(umlclassdiagram::PathNameCS.__init__)


def test_umlclassdiagram::pathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::classcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ClassCS)


def test_umlclassdiagram::classcs_constructor_exists():
    assert callable(umlclassdiagram::ClassCS.__init__)


def test_umlclassdiagram::classcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::classcs_has_name():
    assert hasattr(umlclassdiagram::ClassCS, "name")
    descriptor = None
    for klass in umlclassdiagram::ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::constraintcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::ConstraintCS)


def test_umlclassdiagram::constraintcs_constructor_exists():
    assert callable(umlclassdiagram::ConstraintCS.__init__)


def test_umlclassdiagram::constraintcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram::packagecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::PackageCS)


def test_umlclassdiagram::packagecs_constructor_exists():
    assert callable(umlclassdiagram::PackageCS.__init__)


def test_umlclassdiagram::packagecs_constructor_args():
    sig = inspect.signature(umlclassdiagram::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram::packagecs_has_name():
    assert hasattr(umlclassdiagram::PackageCS, "name")
    descriptor = None
    for klass in umlclassdiagram::PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram::rootcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram::RootCS)


def test_umlclassdiagram::rootcs_constructor_exists():
    assert callable(umlclassdiagram::RootCS.__init__)


def test_umlclassdiagram::rootcs_constructor_args():
    sig = inspect.signature(umlclassdiagram::RootCS.__init__)
    params = list(sig.parameters.keys())

def test_primitivedatatype_exists():
    # Check that the Enumeration exists
    assert PrimitiveDataType is not None

def test_primitivedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveDataType]
    expected_literals = [
        "Integer",
        "Double",
        "String",
        "Boolean",
        "Date",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveDataType"

def test_scopetype_exists():
    # Check that the Enumeration exists
    assert ScopeType is not None

def test_scopetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScopeType]
    expected_literals = [
        "instance",
        "classifier",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"

def test_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "module",
        "gte",
        "lte",
        "negative",
        "gt",
        "equals",
        "multiply",
        "lt",
        "or_",
        "add",
        "divide",
        "not_",
        "subtract",
        "and_",
        "distinct",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorType"

def test_visbilitytype_exists():
    # Check that the Enumeration exists
    assert VisbilityType is not None

def test_visbilitytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisbilityType]
    expected_literals = [
        "public",
        "package",
        "protected",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisbilityType"


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
Relation_strategy = st.builds(
    Relation,
)
umlclassdiagram::Aggregation_strategy = st.builds(
    umlclassdiagram::Aggregation,
)
umlclassdiagram::Association_strategy = st.builds(
    umlclassdiagram::Association,
)
umlclassdiagram::Composition_strategy = st.builds(
    umlclassdiagram::Composition,
)
umlclassdiagram::Dependency_strategy = st.builds(
    umlclassdiagram::Dependency,
)
Modifier_strategy = st.builds(
    Modifier,
)
umlclassdiagram::Operator_strategy = st.builds(
    umlclassdiagram::Operator,
    operator=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
umlclassdiagram::Operation_strategy = st.builds(
    umlclassdiagram::Operation,
)
umlclassdiagram::Attribute_strategy = st.builds(
    umlclassdiagram::Attribute,
    derived=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
umlclassdiagram::Class_strategy = st.builds(
    umlclassdiagram::Class,
)
umlclassdiagram::AssociationClass_strategy = st.builds(
    umlclassdiagram::AssociationClass,
)
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
umlclassdiagram::NavigationPathElementCS_strategy = st.builds(
    umlclassdiagram::NavigationPathElementCS,
)
umlclassdiagram::NavigationPathVariableCS_strategy = st.builds(
    umlclassdiagram::NavigationPathVariableCS,
    varName=
        safe_text
)
umlclassdiagram::NavigationPathCS_strategy = st.builds(
    umlclassdiagram::NavigationPathCS,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umlclassdiagram::Parameter_strategy = st.builds(
    umlclassdiagram::Parameter,
)
umlclassdiagram::Modifier_strategy = st.builds(
    umlclassdiagram::Modifier,
    visibility=
        safe_text,
    scope=
        safe_text
)
umlclassdiagram::NamedElement_strategy = st.builds(
    umlclassdiagram::NamedElement,
    name=
        safe_text
)
umlclassdiagram::Constraint_strategy = st.builds(
    umlclassdiagram::Constraint,
    id=
        safe_text
)
umlclassdiagram::PrimitiveElement_strategy = st.builds(
    umlclassdiagram::PrimitiveElement,
    type=
        safe_text
)
umlclassdiagram::Relation_strategy = st.builds(
    umlclassdiagram::Relation,
    nsrc=
        safe_text,
    derived=
        st.booleans(),
    ntar=
        safe_text
)
umlclassdiagram::Classifier_strategy = st.builds(
    umlclassdiagram::Classifier,
    derived=
        st.booleans(),
    abstract=
        st.booleans()
)
umlclassdiagram::ClassDiagram_strategy = st.builds(
    umlclassdiagram::ClassDiagram,
)
umlclassdiagram::AccVarCS_strategy = st.builds(
    umlclassdiagram::AccVarCS,
    accVarName=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
umlclassdiagram::ForAllExpCS_strategy = st.builds(
    umlclassdiagram::ForAllExpCS,
)
umlclassdiagram::IterateExpCS_strategy = st.builds(
    umlclassdiagram::IterateExpCS,
)
umlclassdiagram::CollectExpCS_strategy = st.builds(
    umlclassdiagram::CollectExpCS,
)
umlclassdiagram::IteratorVarCS_strategy = st.builds(
    umlclassdiagram::IteratorVarCS,
    itName=
        safe_text
)
umlclassdiagram::NavigationPathNameCS_strategy = st.builds(
    umlclassdiagram::NavigationPathNameCS,
)
umlclassdiagram::ExistsExpCS_strategy = st.builds(
    umlclassdiagram::ExistsExpCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
umlclassdiagram::BooleanExpCS_strategy = st.builds(
    umlclassdiagram::BooleanExpCS,
    boolSymbol=
        st.booleans()
)
umlclassdiagram::Feature_strategy = st.builds(
    umlclassdiagram::Feature,
    name=
        safe_text,
    visibility=
        safe_text,
    scope=
        safe_text
)
PathCS_strategy = st.builds(
    PathCS,
)
umlclassdiagram::PathElementCS_strategy = st.builds(
    umlclassdiagram::PathElementCS,
)
umlclassdiagram::PathVariableCS_strategy = st.builds(
    umlclassdiagram::PathVariableCS,
    varName=
        safe_text
)
umlclassdiagram::PathCS_strategy = st.builds(
    umlclassdiagram::PathCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
umlclassdiagram::StringLiteralExpCS_strategy = st.builds(
    umlclassdiagram::StringLiteralExpCS,
    stringSymbol=
        safe_text
)
umlclassdiagram::BooleanLiteralExpCS_strategy = st.builds(
    umlclassdiagram::BooleanLiteralExpCS,
)
umlclassdiagram::IntLiteralExpCS_strategy = st.builds(
    umlclassdiagram::IntLiteralExpCS,
    intSymbol=
        st.integers()
)
umlclassdiagram::InvariantCS_strategy = st.builds(
    umlclassdiagram::InvariantCS,
)
umlclassdiagram::ExpCS_strategy = st.builds(
    umlclassdiagram::ExpCS,
)
umlclassdiagram::RoundedBracketClauseCS_strategy = st.builds(
    umlclassdiagram::RoundedBracketClauseCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
umlclassdiagram::LoopExpCS_strategy = st.builds(
    umlclassdiagram::LoopExpCS,
    logicOp=
        safe_text
)
umlclassdiagram::NavigationNameExpCS_strategy = st.builds(
    umlclassdiagram::NavigationNameExpCS,
)
umlclassdiagram::NameExpCS_strategy = st.builds(
    umlclassdiagram::NameExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
umlclassdiagram::LiteralExpCS_strategy = st.builds(
    umlclassdiagram::LiteralExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
umlclassdiagram::PrimaryExpCS_strategy = st.builds(
    umlclassdiagram::PrimaryExpCS,
)
umlclassdiagram::NavigationExpCS_strategy = st.builds(
    umlclassdiagram::NavigationExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
umlclassdiagram::CallExpCS_strategy = st.builds(
    umlclassdiagram::CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
umlclassdiagram::LogicExpCS_strategy = st.builds(
    umlclassdiagram::LogicExpCS,
    op=
        safe_text
)
umlclassdiagram::ParameterCS_strategy = st.builds(
    umlclassdiagram::ParameterCS,
    name=
        safe_text
)
umlclassdiagram::OperationCS_strategy = st.builds(
    umlclassdiagram::OperationCS,
    name=
        safe_text
)
umlclassdiagram::PropertyCS_strategy = st.builds(
    umlclassdiagram::PropertyCS,
    name=
        safe_text
)
umlclassdiagram::PathNameCS_strategy = st.builds(
    umlclassdiagram::PathNameCS,
)
umlclassdiagram::ClassCS_strategy = st.builds(
    umlclassdiagram::ClassCS,
    name=
        safe_text
)
umlclassdiagram::ConstraintCS_strategy = st.builds(
    umlclassdiagram::ConstraintCS,
)
umlclassdiagram::PackageCS_strategy = st.builds(
    umlclassdiagram::PackageCS,
    name=
        safe_text
)
umlclassdiagram::RootCS_strategy = st.builds(
    umlclassdiagram::RootCS,
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=umlclassdiagram::Aggregation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::aggregation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Aggregation)

@given(instance=umlclassdiagram::Association_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::association_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Association)

@given(instance=umlclassdiagram::Composition_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::composition_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Composition)

@given(instance=umlclassdiagram::Dependency_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::dependency_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Dependency)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=umlclassdiagram::Operator_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::operator_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Operator)

@given(instance=umlclassdiagram::Operator_strategy)
def test_umlclassdiagram::operator_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=umlclassdiagram::Operator_strategy)
def test_umlclassdiagram::operator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=umlclassdiagram::Operation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::operation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Operation)

@given(instance=umlclassdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::attribute_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Attribute)

@given(instance=umlclassdiagram::Attribute_strategy)
def test_umlclassdiagram::attribute_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=umlclassdiagram::Attribute_strategy)
def test_umlclassdiagram::attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlclassdiagram::Class_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::class_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Class)

@given(instance=umlclassdiagram::AssociationClass_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::associationclass_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::AssociationClass)

@given(instance=NavigationPathCS_strategy)
@settings(max_examples=50)
def test_navigationpathcs_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)

@given(instance=umlclassdiagram::NavigationPathElementCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationpathelementcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationPathElementCS)

@given(instance=umlclassdiagram::NavigationPathVariableCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationpathvariablecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationPathVariableCS)

@given(instance=umlclassdiagram::NavigationPathVariableCS_strategy)
def test_umlclassdiagram::navigationpathvariablecs_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=umlclassdiagram::NavigationPathVariableCS_strategy)
def test_umlclassdiagram::navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=umlclassdiagram::NavigationPathCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationpathcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationPathCS)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=umlclassdiagram::Parameter_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::parameter_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Parameter)

@given(instance=umlclassdiagram::Modifier_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::modifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Modifier)

@given(instance=umlclassdiagram::Modifier_strategy)
def test_umlclassdiagram::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=umlclassdiagram::Modifier_strategy)
def test_umlclassdiagram::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=umlclassdiagram::Modifier_strategy)
def test_umlclassdiagram::modifier_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=umlclassdiagram::Modifier_strategy)
def test_umlclassdiagram::modifier_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=umlclassdiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NamedElement)

@given(instance=umlclassdiagram::NamedElement_strategy)
def test_umlclassdiagram::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::NamedElement_strategy)
def test_umlclassdiagram::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::Constraint_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::constraint_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Constraint)

@given(instance=umlclassdiagram::Constraint_strategy)
def test_umlclassdiagram::constraint_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=umlclassdiagram::Constraint_strategy)
def test_umlclassdiagram::constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=umlclassdiagram::PrimitiveElement_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::primitiveelement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PrimitiveElement)

@given(instance=umlclassdiagram::PrimitiveElement_strategy)
def test_umlclassdiagram::primitiveelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=umlclassdiagram::PrimitiveElement_strategy)
def test_umlclassdiagram::primitiveelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=umlclassdiagram::Relation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::relation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Relation)

@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_nsrc_type(instance):
    assert isinstance(instance.nsrc, str)


@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_nsrc_setter(instance):
    original = instance.nsrc
    instance.nsrc = original
    assert instance.nsrc == original

@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_ntar_type(instance):
    assert isinstance(instance.ntar, str)


@given(instance=umlclassdiagram::Relation_strategy)
def test_umlclassdiagram::relation_ntar_setter(instance):
    original = instance.ntar
    instance.ntar = original
    assert instance.ntar == original

@given(instance=umlclassdiagram::Classifier_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::classifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Classifier)

@given(instance=umlclassdiagram::Classifier_strategy)
def test_umlclassdiagram::classifier_derived_type(instance):
    assert isinstance(instance.derived, bool)


@given(instance=umlclassdiagram::Classifier_strategy)
def test_umlclassdiagram::classifier_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=umlclassdiagram::Classifier_strategy)
def test_umlclassdiagram::classifier_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=umlclassdiagram::Classifier_strategy)
def test_umlclassdiagram::classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=umlclassdiagram::ClassDiagram_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::classdiagram_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ClassDiagram)

@given(instance=umlclassdiagram::AccVarCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::accvarcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::AccVarCS)

@given(instance=umlclassdiagram::AccVarCS_strategy)
def test_umlclassdiagram::accvarcs_accVarName_type(instance):
    assert isinstance(instance.accVarName, str)


@given(instance=umlclassdiagram::AccVarCS_strategy)
def test_umlclassdiagram::accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=umlclassdiagram::ForAllExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::forallexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ForAllExpCS)

@given(instance=umlclassdiagram::IterateExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::iterateexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::IterateExpCS)

@given(instance=umlclassdiagram::CollectExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::collectexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::CollectExpCS)

@given(instance=umlclassdiagram::IteratorVarCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::iteratorvarcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::IteratorVarCS)

@given(instance=umlclassdiagram::IteratorVarCS_strategy)
def test_umlclassdiagram::iteratorvarcs_itName_type(instance):
    assert isinstance(instance.itName, str)


@given(instance=umlclassdiagram::IteratorVarCS_strategy)
def test_umlclassdiagram::iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=umlclassdiagram::NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationPathNameCS)

@given(instance=umlclassdiagram::ExistsExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::existsexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ExistsExpCS)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=umlclassdiagram::BooleanExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::booleanexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::BooleanExpCS)

@given(instance=umlclassdiagram::BooleanExpCS_strategy)
def test_umlclassdiagram::booleanexpcs_boolSymbol_type(instance):
    assert isinstance(instance.boolSymbol, bool)


@given(instance=umlclassdiagram::BooleanExpCS_strategy)
def test_umlclassdiagram::booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=umlclassdiagram::Feature_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::feature_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::Feature)

@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=umlclassdiagram::Feature_strategy)
def test_umlclassdiagram::feature_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=PathCS_strategy)
@settings(max_examples=50)
def test_pathcs_instantiation(instance):
    assert isinstance(instance, PathCS)

@given(instance=umlclassdiagram::PathElementCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::pathelementcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PathElementCS)

@given(instance=umlclassdiagram::PathVariableCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::pathvariablecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PathVariableCS)

@given(instance=umlclassdiagram::PathVariableCS_strategy)
def test_umlclassdiagram::pathvariablecs_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=umlclassdiagram::PathVariableCS_strategy)
def test_umlclassdiagram::pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=umlclassdiagram::PathCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::pathcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PathCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=umlclassdiagram::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::StringLiteralExpCS)

@given(instance=umlclassdiagram::StringLiteralExpCS_strategy)
def test_umlclassdiagram::stringliteralexpcs_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=umlclassdiagram::StringLiteralExpCS_strategy)
def test_umlclassdiagram::stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=umlclassdiagram::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::BooleanLiteralExpCS)

@given(instance=umlclassdiagram::IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::intliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::IntLiteralExpCS)

@given(instance=umlclassdiagram::IntLiteralExpCS_strategy)
def test_umlclassdiagram::intliteralexpcs_intSymbol_type(instance):
    assert isinstance(instance.intSymbol, int)


@given(instance=umlclassdiagram::IntLiteralExpCS_strategy)
def test_umlclassdiagram::intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=umlclassdiagram::InvariantCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::invariantcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::InvariantCS)

@given(instance=umlclassdiagram::ExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::expcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ExpCS)

@given(instance=umlclassdiagram::RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::RoundedBracketClauseCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=umlclassdiagram::LoopExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::loopexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::LoopExpCS)

@given(instance=umlclassdiagram::LoopExpCS_strategy)
def test_umlclassdiagram::loopexpcs_logicOp_type(instance):
    assert isinstance(instance.logicOp, str)


@given(instance=umlclassdiagram::LoopExpCS_strategy)
def test_umlclassdiagram::loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=umlclassdiagram::NavigationNameExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationnameexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationNameExpCS)

@given(instance=umlclassdiagram::NameExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::nameexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NameExpCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=umlclassdiagram::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::literalexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::LiteralExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=umlclassdiagram::PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::primaryexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PrimaryExpCS)

@given(instance=umlclassdiagram::NavigationExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::navigationexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::NavigationExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=umlclassdiagram::CallExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::callexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=umlclassdiagram::LogicExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::logicexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::LogicExpCS)

@given(instance=umlclassdiagram::LogicExpCS_strategy)
def test_umlclassdiagram::logicexpcs_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=umlclassdiagram::LogicExpCS_strategy)
def test_umlclassdiagram::logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=umlclassdiagram::ParameterCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::parametercs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ParameterCS)

@given(instance=umlclassdiagram::ParameterCS_strategy)
def test_umlclassdiagram::parametercs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::ParameterCS_strategy)
def test_umlclassdiagram::parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::OperationCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::operationcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::OperationCS)

@given(instance=umlclassdiagram::OperationCS_strategy)
def test_umlclassdiagram::operationcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::OperationCS_strategy)
def test_umlclassdiagram::operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::PropertyCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::propertycs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PropertyCS)

@given(instance=umlclassdiagram::PropertyCS_strategy)
def test_umlclassdiagram::propertycs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::PropertyCS_strategy)
def test_umlclassdiagram::propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::PathNameCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::pathnamecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PathNameCS)

@given(instance=umlclassdiagram::ClassCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::classcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ClassCS)

@given(instance=umlclassdiagram::ClassCS_strategy)
def test_umlclassdiagram::classcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::ClassCS_strategy)
def test_umlclassdiagram::classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::ConstraintCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::constraintcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::ConstraintCS)

@given(instance=umlclassdiagram::PackageCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::packagecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::PackageCS)

@given(instance=umlclassdiagram::PackageCS_strategy)
def test_umlclassdiagram::packagecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=umlclassdiagram::PackageCS_strategy)
def test_umlclassdiagram::packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram::RootCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram::rootcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram::RootCS)
