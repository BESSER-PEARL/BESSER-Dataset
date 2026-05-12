import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relation,
    umlclassdiagram_Association,
    umlclassdiagram_Aggregation,
    umlclassdiagram_Composition,
    umlclassdiagram_Dependency,
    Modifier,
    umlclassdiagram_Operator,
    Feature,
    umlclassdiagram_Operation,
    umlclassdiagram_Attribute,
    Classifier,
    umlclassdiagram_Class,
    umlclassdiagram_AssociationClass,
    NavigationPathCS,
    umlclassdiagram_NavigationPathElementCS,
    umlclassdiagram_NavigationPathVariableCS,
    umlclassdiagram_NavigationPathCS,
    NamedElement,
    umlclassdiagram_Modifier,
    umlclassdiagram_Parameter,
    umlclassdiagram_NamedElement,
    umlclassdiagram_Constraint,
    umlclassdiagram_PrimitiveElement,
    umlclassdiagram_Relation,
    umlclassdiagram_Classifier,
    umlclassdiagram_ClassDiagram,
    umlclassdiagram_AccVarCS,
    LoopExpCS,
    umlclassdiagram_IterateExpCS,
    umlclassdiagram_ForAllExpCS,
    umlclassdiagram_CollectExpCS,
    umlclassdiagram_IteratorVarCS,
    umlclassdiagram_NavigationPathNameCS,
    umlclassdiagram_ExistsExpCS,
    BooleanLiteralExpCS,
    umlclassdiagram_BooleanExpCS,
    umlclassdiagram_Feature,
    PathCS,
    umlclassdiagram_PathElementCS,
    umlclassdiagram_PathVariableCS,
    umlclassdiagram_PathCS,
    LiteralExpCS,
    umlclassdiagram_BooleanLiteralExpCS,
    umlclassdiagram_StringLiteralExpCS,
    umlclassdiagram_IntLiteralExpCS,
    umlclassdiagram_InvariantCS,
    umlclassdiagram_ExpCS,
    umlclassdiagram_RoundedBracketClauseCS,
    NavigationExpCS,
    umlclassdiagram_NavigationNameExpCS,
    umlclassdiagram_LoopExpCS,
    umlclassdiagram_NameExpCS,
    PrimaryExpCS,
    umlclassdiagram_LiteralExpCS,
    CallExpCS,
    umlclassdiagram_PrimaryExpCS,
    umlclassdiagram_NavigationExpCS,
    LogicExpCS,
    umlclassdiagram_CallExpCS,
    ExpCS,
    umlclassdiagram_LogicExpCS,
    umlclassdiagram_ParameterCS,
    umlclassdiagram_OperationCS,
    umlclassdiagram_PropertyCS,
    umlclassdiagram_PathNameCS,
    umlclassdiagram_ClassCS,
    umlclassdiagram_ConstraintCS,
    umlclassdiagram_PackageCS,
    umlclassdiagram_RootCS,
    OperatorType,
    VisbilityType,
    PrimitiveDataType,
    ScopeType,
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



def test_umlclassdiagram_association_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Association)


def test_umlclassdiagram_association_constructor_exists():
    assert callable(umlclassdiagram_Association.__init__)


def test_umlclassdiagram_association_constructor_args():
    sig = inspect.signature(umlclassdiagram_Association.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_aggregation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Aggregation)


def test_umlclassdiagram_aggregation_constructor_exists():
    assert callable(umlclassdiagram_Aggregation.__init__)


def test_umlclassdiagram_aggregation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Aggregation.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_composition_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Composition)


def test_umlclassdiagram_composition_constructor_exists():
    assert callable(umlclassdiagram_Composition.__init__)


def test_umlclassdiagram_composition_constructor_args():
    sig = inspect.signature(umlclassdiagram_Composition.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_dependency_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Dependency)


def test_umlclassdiagram_dependency_constructor_exists():
    assert callable(umlclassdiagram_Dependency.__init__)


def test_umlclassdiagram_dependency_constructor_args():
    sig = inspect.signature(umlclassdiagram_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_modifier_is_not_abstract():
    assert not inspect.isabstract(Modifier)


def test_modifier_constructor_exists():
    assert callable(Modifier.__init__)


def test_modifier_constructor_args():
    sig = inspect.signature(Modifier.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_operator_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Operator)


def test_umlclassdiagram_operator_constructor_exists():
    assert callable(umlclassdiagram_Operator.__init__)


def test_umlclassdiagram_operator_constructor_args():
    sig = inspect.signature(umlclassdiagram_Operator.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_umlclassdiagram_operator_has_operator():
    assert hasattr(umlclassdiagram_Operator, "operator")
    descriptor = None
    for klass in umlclassdiagram_Operator.__mro__:
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



def test_umlclassdiagram_operation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Operation)


def test_umlclassdiagram_operation_constructor_exists():
    assert callable(umlclassdiagram_Operation.__init__)


def test_umlclassdiagram_operation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Operation.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_attribute_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Attribute)


def test_umlclassdiagram_attribute_constructor_exists():
    assert callable(umlclassdiagram_Attribute.__init__)


def test_umlclassdiagram_attribute_constructor_args():
    sig = inspect.signature(umlclassdiagram_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"

def test_umlclassdiagram_attribute_has_derived():
    assert hasattr(umlclassdiagram_Attribute, "derived")
    descriptor = None
    for klass in umlclassdiagram_Attribute.__mro__:
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



def test_umlclassdiagram_class_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Class)


def test_umlclassdiagram_class_constructor_exists():
    assert callable(umlclassdiagram_Class.__init__)


def test_umlclassdiagram_class_constructor_args():
    sig = inspect.signature(umlclassdiagram_Class.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_associationclass_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_AssociationClass)


def test_umlclassdiagram_associationclass_constructor_exists():
    assert callable(umlclassdiagram_AssociationClass.__init__)


def test_umlclassdiagram_associationclass_constructor_args():
    sig = inspect.signature(umlclassdiagram_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathElementCS)


def test_umlclassdiagram_navigationpathelementcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathElementCS.__init__)


def test_umlclassdiagram_navigationpathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathVariableCS)


def test_umlclassdiagram_navigationpathvariablecs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathVariableCS.__init__)


def test_umlclassdiagram_navigationpathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_umlclassdiagram_navigationpathvariablecs_has_varName():
    assert hasattr(umlclassdiagram_NavigationPathVariableCS, "varName")
    descriptor = None
    for klass in umlclassdiagram_NavigationPathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathCS)


def test_umlclassdiagram_navigationpathcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathCS.__init__)


def test_umlclassdiagram_navigationpathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_modifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Modifier)


def test_umlclassdiagram_modifier_constructor_exists():
    assert callable(umlclassdiagram_Modifier.__init__)


def test_umlclassdiagram_modifier_constructor_args():
    sig = inspect.signature(umlclassdiagram_Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_umlclassdiagram_modifier_has_scope():
    assert hasattr(umlclassdiagram_Modifier, "scope")
    descriptor = None
    for klass in umlclassdiagram_Modifier.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_modifier_has_visibility():
    assert hasattr(umlclassdiagram_Modifier, "visibility")
    descriptor = None
    for klass in umlclassdiagram_Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_parameter_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Parameter)


def test_umlclassdiagram_parameter_constructor_exists():
    assert callable(umlclassdiagram_Parameter.__init__)


def test_umlclassdiagram_parameter_constructor_args():
    sig = inspect.signature(umlclassdiagram_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_namedelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NamedElement)


def test_umlclassdiagram_namedelement_constructor_exists():
    assert callable(umlclassdiagram_NamedElement.__init__)


def test_umlclassdiagram_namedelement_constructor_args():
    sig = inspect.signature(umlclassdiagram_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_namedelement_has_name():
    assert hasattr(umlclassdiagram_NamedElement, "name")
    descriptor = None
    for klass in umlclassdiagram_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_constraint_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Constraint)


def test_umlclassdiagram_constraint_constructor_exists():
    assert callable(umlclassdiagram_Constraint.__init__)


def test_umlclassdiagram_constraint_constructor_args():
    sig = inspect.signature(umlclassdiagram_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_umlclassdiagram_constraint_has_id():
    assert hasattr(umlclassdiagram_Constraint, "id")
    descriptor = None
    for klass in umlclassdiagram_Constraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_primitiveelement_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PrimitiveElement)


def test_umlclassdiagram_primitiveelement_constructor_exists():
    assert callable(umlclassdiagram_PrimitiveElement.__init__)


def test_umlclassdiagram_primitiveelement_constructor_args():
    sig = inspect.signature(umlclassdiagram_PrimitiveElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlclassdiagram_primitiveelement_has_type():
    assert hasattr(umlclassdiagram_PrimitiveElement, "type")
    descriptor = None
    for klass in umlclassdiagram_PrimitiveElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_relation_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Relation)


def test_umlclassdiagram_relation_constructor_exists():
    assert callable(umlclassdiagram_Relation.__init__)


def test_umlclassdiagram_relation_constructor_args():
    sig = inspect.signature(umlclassdiagram_Relation.__init__)
    params = list(sig.parameters.keys())
    assert "ntar" in params, "Missing parameter 'ntar'"
    assert "derived" in params, "Missing parameter 'derived'"
    assert "nsrc" in params, "Missing parameter 'nsrc'"

def test_umlclassdiagram_relation_has_ntar():
    assert hasattr(umlclassdiagram_Relation, "ntar")
    descriptor = None
    for klass in umlclassdiagram_Relation.__mro__:
        if "ntar" in klass.__dict__:
            descriptor = klass.__dict__["ntar"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_relation_has_derived():
    assert hasattr(umlclassdiagram_Relation, "derived")
    descriptor = None
    for klass in umlclassdiagram_Relation.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_relation_has_nsrc():
    assert hasattr(umlclassdiagram_Relation, "nsrc")
    descriptor = None
    for klass in umlclassdiagram_Relation.__mro__:
        if "nsrc" in klass.__dict__:
            descriptor = klass.__dict__["nsrc"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_classifier_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Classifier)


def test_umlclassdiagram_classifier_constructor_exists():
    assert callable(umlclassdiagram_Classifier.__init__)


def test_umlclassdiagram_classifier_constructor_args():
    sig = inspect.signature(umlclassdiagram_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "derived" in params, "Missing parameter 'derived'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_umlclassdiagram_classifier_has_derived():
    assert hasattr(umlclassdiagram_Classifier, "derived")
    descriptor = None
    for klass in umlclassdiagram_Classifier.__mro__:
        if "derived" in klass.__dict__:
            descriptor = klass.__dict__["derived"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_classifier_has_abstract():
    assert hasattr(umlclassdiagram_Classifier, "abstract")
    descriptor = None
    for klass in umlclassdiagram_Classifier.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_classdiagram_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ClassDiagram)


def test_umlclassdiagram_classdiagram_constructor_exists():
    assert callable(umlclassdiagram_ClassDiagram.__init__)


def test_umlclassdiagram_classdiagram_constructor_args():
    sig = inspect.signature(umlclassdiagram_ClassDiagram.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_accvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_AccVarCS)


def test_umlclassdiagram_accvarcs_constructor_exists():
    assert callable(umlclassdiagram_AccVarCS.__init__)


def test_umlclassdiagram_accvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"

def test_umlclassdiagram_accvarcs_has_accVarName():
    assert hasattr(umlclassdiagram_AccVarCS, "accVarName")
    descriptor = None
    for klass in umlclassdiagram_AccVarCS.__mro__:
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



def test_umlclassdiagram_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IterateExpCS)


def test_umlclassdiagram_iterateexpcs_constructor_exists():
    assert callable(umlclassdiagram_IterateExpCS.__init__)


def test_umlclassdiagram_iterateexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_forallexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ForAllExpCS)


def test_umlclassdiagram_forallexpcs_constructor_exists():
    assert callable(umlclassdiagram_ForAllExpCS.__init__)


def test_umlclassdiagram_forallexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_collectexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_CollectExpCS)


def test_umlclassdiagram_collectexpcs_constructor_exists():
    assert callable(umlclassdiagram_CollectExpCS.__init__)


def test_umlclassdiagram_collectexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IteratorVarCS)


def test_umlclassdiagram_iteratorvarcs_constructor_exists():
    assert callable(umlclassdiagram_IteratorVarCS.__init__)


def test_umlclassdiagram_iteratorvarcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_umlclassdiagram_iteratorvarcs_has_itName():
    assert hasattr(umlclassdiagram_IteratorVarCS, "itName")
    descriptor = None
    for klass in umlclassdiagram_IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationPathNameCS)


def test_umlclassdiagram_navigationpathnamecs_constructor_exists():
    assert callable(umlclassdiagram_NavigationPathNameCS.__init__)


def test_umlclassdiagram_navigationpathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_existsexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ExistsExpCS)


def test_umlclassdiagram_existsexpcs_constructor_exists():
    assert callable(umlclassdiagram_ExistsExpCS.__init__)


def test_umlclassdiagram_existsexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_BooleanExpCS)


def test_umlclassdiagram_booleanexpcs_constructor_exists():
    assert callable(umlclassdiagram_BooleanExpCS.__init__)


def test_umlclassdiagram_booleanexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_umlclassdiagram_booleanexpcs_has_boolSymbol():
    assert hasattr(umlclassdiagram_BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in umlclassdiagram_BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_feature_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_Feature)


def test_umlclassdiagram_feature_constructor_exists():
    assert callable(umlclassdiagram_Feature.__init__)


def test_umlclassdiagram_feature_constructor_args():
    sig = inspect.signature(umlclassdiagram_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_feature_has_scope():
    assert hasattr(umlclassdiagram_Feature, "scope")
    descriptor = None
    for klass in umlclassdiagram_Feature.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_feature_has_visibility():
    assert hasattr(umlclassdiagram_Feature, "visibility")
    descriptor = None
    for klass in umlclassdiagram_Feature.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlclassdiagram_feature_has_name():
    assert hasattr(umlclassdiagram_Feature, "name")
    descriptor = None
    for klass in umlclassdiagram_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathElementCS)


def test_umlclassdiagram_pathelementcs_constructor_exists():
    assert callable(umlclassdiagram_PathElementCS.__init__)


def test_umlclassdiagram_pathelementcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathVariableCS)


def test_umlclassdiagram_pathvariablecs_constructor_exists():
    assert callable(umlclassdiagram_PathVariableCS.__init__)


def test_umlclassdiagram_pathvariablecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_umlclassdiagram_pathvariablecs_has_varName():
    assert hasattr(umlclassdiagram_PathVariableCS, "varName")
    descriptor = None
    for klass in umlclassdiagram_PathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_pathcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathCS)


def test_umlclassdiagram_pathcs_constructor_exists():
    assert callable(umlclassdiagram_PathCS.__init__)


def test_umlclassdiagram_pathcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_BooleanLiteralExpCS)


def test_umlclassdiagram_booleanliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_BooleanLiteralExpCS.__init__)


def test_umlclassdiagram_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_StringLiteralExpCS)


def test_umlclassdiagram_stringliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_StringLiteralExpCS.__init__)


def test_umlclassdiagram_stringliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_umlclassdiagram_stringliteralexpcs_has_stringSymbol():
    assert hasattr(umlclassdiagram_StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in umlclassdiagram_StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_IntLiteralExpCS)


def test_umlclassdiagram_intliteralexpcs_constructor_exists():
    assert callable(umlclassdiagram_IntLiteralExpCS.__init__)


def test_umlclassdiagram_intliteralexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_umlclassdiagram_intliteralexpcs_has_intSymbol():
    assert hasattr(umlclassdiagram_IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in umlclassdiagram_IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_invariantcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_InvariantCS)


def test_umlclassdiagram_invariantcs_constructor_exists():
    assert callable(umlclassdiagram_InvariantCS.__init__)


def test_umlclassdiagram_invariantcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_expcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ExpCS)


def test_umlclassdiagram_expcs_constructor_exists():
    assert callable(umlclassdiagram_ExpCS.__init__)


def test_umlclassdiagram_expcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_RoundedBracketClauseCS)


def test_umlclassdiagram_roundedbracketclausecs_constructor_exists():
    assert callable(umlclassdiagram_RoundedBracketClauseCS.__init__)


def test_umlclassdiagram_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationNameExpCS)


def test_umlclassdiagram_navigationnameexpcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationNameExpCS.__init__)


def test_umlclassdiagram_navigationnameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LoopExpCS)


def test_umlclassdiagram_loopexpcs_constructor_exists():
    assert callable(umlclassdiagram_LoopExpCS.__init__)


def test_umlclassdiagram_loopexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"

def test_umlclassdiagram_loopexpcs_has_logicOp():
    assert hasattr(umlclassdiagram_LoopExpCS, "logicOp")
    descriptor = None
    for klass in umlclassdiagram_LoopExpCS.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NameExpCS)


def test_umlclassdiagram_nameexpcs_constructor_exists():
    assert callable(umlclassdiagram_NameExpCS.__init__)


def test_umlclassdiagram_nameexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LiteralExpCS)


def test_umlclassdiagram_literalexpcs_constructor_exists():
    assert callable(umlclassdiagram_LiteralExpCS.__init__)


def test_umlclassdiagram_literalexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PrimaryExpCS)


def test_umlclassdiagram_primaryexpcs_constructor_exists():
    assert callable(umlclassdiagram_PrimaryExpCS.__init__)


def test_umlclassdiagram_primaryexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_NavigationExpCS)


def test_umlclassdiagram_navigationexpcs_constructor_exists():
    assert callable(umlclassdiagram_NavigationExpCS.__init__)


def test_umlclassdiagram_navigationexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_callexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_CallExpCS)


def test_umlclassdiagram_callexpcs_constructor_exists():
    assert callable(umlclassdiagram_CallExpCS.__init__)


def test_umlclassdiagram_callexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_LogicExpCS)


def test_umlclassdiagram_logicexpcs_constructor_exists():
    assert callable(umlclassdiagram_LogicExpCS.__init__)


def test_umlclassdiagram_logicexpcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_umlclassdiagram_logicexpcs_has_op():
    assert hasattr(umlclassdiagram_LogicExpCS, "op")
    descriptor = None
    for klass in umlclassdiagram_LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_parametercs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ParameterCS)


def test_umlclassdiagram_parametercs_constructor_exists():
    assert callable(umlclassdiagram_ParameterCS.__init__)


def test_umlclassdiagram_parametercs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_parametercs_has_name():
    assert hasattr(umlclassdiagram_ParameterCS, "name")
    descriptor = None
    for klass in umlclassdiagram_ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_operationcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_OperationCS)


def test_umlclassdiagram_operationcs_constructor_exists():
    assert callable(umlclassdiagram_OperationCS.__init__)


def test_umlclassdiagram_operationcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_operationcs_has_name():
    assert hasattr(umlclassdiagram_OperationCS, "name")
    descriptor = None
    for klass in umlclassdiagram_OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_propertycs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PropertyCS)


def test_umlclassdiagram_propertycs_constructor_exists():
    assert callable(umlclassdiagram_PropertyCS.__init__)


def test_umlclassdiagram_propertycs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_propertycs_has_name():
    assert hasattr(umlclassdiagram_PropertyCS, "name")
    descriptor = None
    for klass in umlclassdiagram_PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PathNameCS)


def test_umlclassdiagram_pathnamecs_constructor_exists():
    assert callable(umlclassdiagram_PathNameCS.__init__)


def test_umlclassdiagram_pathnamecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_classcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ClassCS)


def test_umlclassdiagram_classcs_constructor_exists():
    assert callable(umlclassdiagram_ClassCS.__init__)


def test_umlclassdiagram_classcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_classcs_has_name():
    assert hasattr(umlclassdiagram_ClassCS, "name")
    descriptor = None
    for klass in umlclassdiagram_ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_constraintcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_ConstraintCS)


def test_umlclassdiagram_constraintcs_constructor_exists():
    assert callable(umlclassdiagram_ConstraintCS.__init__)


def test_umlclassdiagram_constraintcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_umlclassdiagram_packagecs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_PackageCS)


def test_umlclassdiagram_packagecs_constructor_exists():
    assert callable(umlclassdiagram_PackageCS.__init__)


def test_umlclassdiagram_packagecs_constructor_args():
    sig = inspect.signature(umlclassdiagram_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_umlclassdiagram_packagecs_has_name():
    assert hasattr(umlclassdiagram_PackageCS, "name")
    descriptor = None
    for klass in umlclassdiagram_PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclassdiagram_rootcs_is_not_abstract():
    assert not inspect.isabstract(umlclassdiagram_RootCS)


def test_umlclassdiagram_rootcs_constructor_exists():
    assert callable(umlclassdiagram_RootCS.__init__)


def test_umlclassdiagram_rootcs_constructor_args():
    sig = inspect.signature(umlclassdiagram_RootCS.__init__)
    params = list(sig.parameters.keys())

def test_operatortype_exists():
    # Check that the Enumeration exists
    assert OperatorType is not None

def test_operatortype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorType]
    expected_literals = [
        "subtract",
        "or_",
        "gte",
        "module",
        "and_",
        "add",
        "multiply",
        "distinct",
        "lt",
        "gt",
        "negative",
        "equals",
        "lte",
        "not_",
        "divide",
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
        "protected",
        "package",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisbilityType"

def test_primitivedatatype_exists():
    # Check that the Enumeration exists
    assert PrimitiveDataType is not None

def test_primitivedatatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveDataType]
    expected_literals = [
        "Integer",
        "Date",
        "Boolean",
        "String",
        "Double",
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
        "classifier",
        "instance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScopeType"


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
umlclassdiagram_Association_strategy = st.builds(
    umlclassdiagram_Association,
)
umlclassdiagram_Aggregation_strategy = st.builds(
    umlclassdiagram_Aggregation,
)
umlclassdiagram_Composition_strategy = st.builds(
    umlclassdiagram_Composition,
)
umlclassdiagram_Dependency_strategy = st.builds(
    umlclassdiagram_Dependency,
)
Modifier_strategy = st.builds(
    Modifier,
)
umlclassdiagram_Operator_strategy = st.builds(
    umlclassdiagram_Operator,
    operator=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
umlclassdiagram_Operation_strategy = st.builds(
    umlclassdiagram_Operation,
)
umlclassdiagram_Attribute_strategy = st.builds(
    umlclassdiagram_Attribute,
    derived=
        st.booleans()
)
Classifier_strategy = st.builds(
    Classifier,
)
umlclassdiagram_Class_strategy = st.builds(
    umlclassdiagram_Class,
)
umlclassdiagram_AssociationClass_strategy = st.builds(
    umlclassdiagram_AssociationClass,
)
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
umlclassdiagram_NavigationPathElementCS_strategy = st.builds(
    umlclassdiagram_NavigationPathElementCS,
)
umlclassdiagram_NavigationPathVariableCS_strategy = st.builds(
    umlclassdiagram_NavigationPathVariableCS,
    varName=
        safe_text
)
umlclassdiagram_NavigationPathCS_strategy = st.builds(
    umlclassdiagram_NavigationPathCS,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
umlclassdiagram_Modifier_strategy = st.builds(
    umlclassdiagram_Modifier,
    scope=
        safe_text,
    visibility=
        safe_text
)
umlclassdiagram_Parameter_strategy = st.builds(
    umlclassdiagram_Parameter,
)
umlclassdiagram_NamedElement_strategy = st.builds(
    umlclassdiagram_NamedElement,
    name=
        safe_text
)
umlclassdiagram_Constraint_strategy = st.builds(
    umlclassdiagram_Constraint,
    id=
        safe_text
)
umlclassdiagram_PrimitiveElement_strategy = st.builds(
    umlclassdiagram_PrimitiveElement,
    type=
        safe_text
)
umlclassdiagram_Relation_strategy = st.builds(
    umlclassdiagram_Relation,
    ntar=
        safe_text,
    derived=
        st.booleans(),
    nsrc=
        safe_text
)
umlclassdiagram_Classifier_strategy = st.builds(
    umlclassdiagram_Classifier,
    derived=
        st.booleans(),
    abstract=
        st.booleans()
)
umlclassdiagram_ClassDiagram_strategy = st.builds(
    umlclassdiagram_ClassDiagram,
)
umlclassdiagram_AccVarCS_strategy = st.builds(
    umlclassdiagram_AccVarCS,
    accVarName=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
umlclassdiagram_IterateExpCS_strategy = st.builds(
    umlclassdiagram_IterateExpCS,
)
umlclassdiagram_ForAllExpCS_strategy = st.builds(
    umlclassdiagram_ForAllExpCS,
)
umlclassdiagram_CollectExpCS_strategy = st.builds(
    umlclassdiagram_CollectExpCS,
)
umlclassdiagram_IteratorVarCS_strategy = st.builds(
    umlclassdiagram_IteratorVarCS,
    itName=
        safe_text
)
umlclassdiagram_NavigationPathNameCS_strategy = st.builds(
    umlclassdiagram_NavigationPathNameCS,
)
umlclassdiagram_ExistsExpCS_strategy = st.builds(
    umlclassdiagram_ExistsExpCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
umlclassdiagram_BooleanExpCS_strategy = st.builds(
    umlclassdiagram_BooleanExpCS,
    boolSymbol=
        st.booleans()
)
umlclassdiagram_Feature_strategy = st.builds(
    umlclassdiagram_Feature,
    scope=
        safe_text,
    visibility=
        safe_text,
    name=
        safe_text
)
PathCS_strategy = st.builds(
    PathCS,
)
umlclassdiagram_PathElementCS_strategy = st.builds(
    umlclassdiagram_PathElementCS,
)
umlclassdiagram_PathVariableCS_strategy = st.builds(
    umlclassdiagram_PathVariableCS,
    varName=
        safe_text
)
umlclassdiagram_PathCS_strategy = st.builds(
    umlclassdiagram_PathCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
umlclassdiagram_BooleanLiteralExpCS_strategy = st.builds(
    umlclassdiagram_BooleanLiteralExpCS,
)
umlclassdiagram_StringLiteralExpCS_strategy = st.builds(
    umlclassdiagram_StringLiteralExpCS,
    stringSymbol=
        safe_text
)
umlclassdiagram_IntLiteralExpCS_strategy = st.builds(
    umlclassdiagram_IntLiteralExpCS,
    intSymbol=
        st.integers()
)
umlclassdiagram_InvariantCS_strategy = st.builds(
    umlclassdiagram_InvariantCS,
)
umlclassdiagram_ExpCS_strategy = st.builds(
    umlclassdiagram_ExpCS,
)
umlclassdiagram_RoundedBracketClauseCS_strategy = st.builds(
    umlclassdiagram_RoundedBracketClauseCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
umlclassdiagram_NavigationNameExpCS_strategy = st.builds(
    umlclassdiagram_NavigationNameExpCS,
)
umlclassdiagram_LoopExpCS_strategy = st.builds(
    umlclassdiagram_LoopExpCS,
    logicOp=
        safe_text
)
umlclassdiagram_NameExpCS_strategy = st.builds(
    umlclassdiagram_NameExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
umlclassdiagram_LiteralExpCS_strategy = st.builds(
    umlclassdiagram_LiteralExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
umlclassdiagram_PrimaryExpCS_strategy = st.builds(
    umlclassdiagram_PrimaryExpCS,
)
umlclassdiagram_NavigationExpCS_strategy = st.builds(
    umlclassdiagram_NavigationExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
umlclassdiagram_CallExpCS_strategy = st.builds(
    umlclassdiagram_CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
umlclassdiagram_LogicExpCS_strategy = st.builds(
    umlclassdiagram_LogicExpCS,
    op=
        safe_text
)
umlclassdiagram_ParameterCS_strategy = st.builds(
    umlclassdiagram_ParameterCS,
    name=
        safe_text
)
umlclassdiagram_OperationCS_strategy = st.builds(
    umlclassdiagram_OperationCS,
    name=
        safe_text
)
umlclassdiagram_PropertyCS_strategy = st.builds(
    umlclassdiagram_PropertyCS,
    name=
        safe_text
)
umlclassdiagram_PathNameCS_strategy = st.builds(
    umlclassdiagram_PathNameCS,
)
umlclassdiagram_ClassCS_strategy = st.builds(
    umlclassdiagram_ClassCS,
    name=
        safe_text
)
umlclassdiagram_ConstraintCS_strategy = st.builds(
    umlclassdiagram_ConstraintCS,
)
umlclassdiagram_PackageCS_strategy = st.builds(
    umlclassdiagram_PackageCS,
    name=
        safe_text
)
umlclassdiagram_RootCS_strategy = st.builds(
    umlclassdiagram_RootCS,
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=umlclassdiagram_Association_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_association_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Association)

@given(instance=umlclassdiagram_Aggregation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_aggregation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Aggregation)

@given(instance=umlclassdiagram_Composition_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_composition_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Composition)

@given(instance=umlclassdiagram_Dependency_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_dependency_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Dependency)

@given(instance=Modifier_strategy)
@settings(max_examples=50)
def test_modifier_instantiation(instance):
    assert isinstance(instance, Modifier)

@given(instance=umlclassdiagram_Operator_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_operator_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Operator)



@given(instance=umlclassdiagram_Operator_strategy)
def test_umlclassdiagram_operator_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=umlclassdiagram_Operation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_operation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Operation)

@given(instance=umlclassdiagram_Attribute_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_attribute_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Attribute)



@given(instance=umlclassdiagram_Attribute_strategy)
def test_umlclassdiagram_attribute_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=umlclassdiagram_Class_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_class_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Class)

@given(instance=umlclassdiagram_AssociationClass_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_associationclass_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_AssociationClass)

@given(instance=NavigationPathCS_strategy)
@settings(max_examples=50)
def test_navigationpathcs_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)

@given(instance=umlclassdiagram_NavigationPathElementCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationpathelementcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathElementCS)

@given(instance=umlclassdiagram_NavigationPathVariableCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationpathvariablecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathVariableCS)



@given(instance=umlclassdiagram_NavigationPathVariableCS_strategy)
def test_umlclassdiagram_navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=umlclassdiagram_NavigationPathCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationpathcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathCS)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=umlclassdiagram_Modifier_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_modifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Modifier)



@given(instance=umlclassdiagram_Modifier_strategy)
def test_umlclassdiagram_modifier_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=umlclassdiagram_Modifier_strategy)
def test_umlclassdiagram_modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=umlclassdiagram_Parameter_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_parameter_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Parameter)

@given(instance=umlclassdiagram_NamedElement_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_namedelement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NamedElement)



@given(instance=umlclassdiagram_NamedElement_strategy)
def test_umlclassdiagram_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_Constraint_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_constraint_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Constraint)



@given(instance=umlclassdiagram_Constraint_strategy)
def test_umlclassdiagram_constraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=umlclassdiagram_PrimitiveElement_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_primitiveelement_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PrimitiveElement)



@given(instance=umlclassdiagram_PrimitiveElement_strategy)
def test_umlclassdiagram_primitiveelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=umlclassdiagram_Relation_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_relation_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Relation)



@given(instance=umlclassdiagram_Relation_strategy)
def test_umlclassdiagram_relation_ntar_setter(instance):
    original = instance.ntar
    instance.ntar = original
    assert instance.ntar == original



@given(instance=umlclassdiagram_Relation_strategy)
def test_umlclassdiagram_relation_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=umlclassdiagram_Relation_strategy)
def test_umlclassdiagram_relation_nsrc_setter(instance):
    original = instance.nsrc
    instance.nsrc = original
    assert instance.nsrc == original

@given(instance=umlclassdiagram_Classifier_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_classifier_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Classifier)



@given(instance=umlclassdiagram_Classifier_strategy)
def test_umlclassdiagram_classifier_derived_setter(instance):
    original = instance.derived
    instance.derived = original
    assert instance.derived == original



@given(instance=umlclassdiagram_Classifier_strategy)
def test_umlclassdiagram_classifier_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=umlclassdiagram_ClassDiagram_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_classdiagram_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ClassDiagram)

@given(instance=umlclassdiagram_AccVarCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_accvarcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_AccVarCS)



@given(instance=umlclassdiagram_AccVarCS_strategy)
def test_umlclassdiagram_accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=umlclassdiagram_IterateExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_iterateexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IterateExpCS)

@given(instance=umlclassdiagram_ForAllExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_forallexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ForAllExpCS)

@given(instance=umlclassdiagram_CollectExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_collectexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_CollectExpCS)

@given(instance=umlclassdiagram_IteratorVarCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IteratorVarCS)



@given(instance=umlclassdiagram_IteratorVarCS_strategy)
def test_umlclassdiagram_iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=umlclassdiagram_NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationPathNameCS)

@given(instance=umlclassdiagram_ExistsExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_existsexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ExistsExpCS)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=umlclassdiagram_BooleanExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_booleanexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_BooleanExpCS)



@given(instance=umlclassdiagram_BooleanExpCS_strategy)
def test_umlclassdiagram_booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=umlclassdiagram_Feature_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_feature_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_Feature)



@given(instance=umlclassdiagram_Feature_strategy)
def test_umlclassdiagram_feature_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=umlclassdiagram_Feature_strategy)
def test_umlclassdiagram_feature_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=umlclassdiagram_Feature_strategy)
def test_umlclassdiagram_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PathCS_strategy)
@settings(max_examples=50)
def test_pathcs_instantiation(instance):
    assert isinstance(instance, PathCS)

@given(instance=umlclassdiagram_PathElementCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_pathelementcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathElementCS)

@given(instance=umlclassdiagram_PathVariableCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_pathvariablecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathVariableCS)



@given(instance=umlclassdiagram_PathVariableCS_strategy)
def test_umlclassdiagram_pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=umlclassdiagram_PathCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_pathcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=umlclassdiagram_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_BooleanLiteralExpCS)

@given(instance=umlclassdiagram_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_StringLiteralExpCS)



@given(instance=umlclassdiagram_StringLiteralExpCS_strategy)
def test_umlclassdiagram_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=umlclassdiagram_IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_intliteralexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_IntLiteralExpCS)



@given(instance=umlclassdiagram_IntLiteralExpCS_strategy)
def test_umlclassdiagram_intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=umlclassdiagram_InvariantCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_invariantcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_InvariantCS)

@given(instance=umlclassdiagram_ExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_expcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ExpCS)

@given(instance=umlclassdiagram_RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_RoundedBracketClauseCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=umlclassdiagram_NavigationNameExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationnameexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationNameExpCS)

@given(instance=umlclassdiagram_LoopExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_loopexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LoopExpCS)



@given(instance=umlclassdiagram_LoopExpCS_strategy)
def test_umlclassdiagram_loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=umlclassdiagram_NameExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_nameexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NameExpCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=umlclassdiagram_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_literalexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LiteralExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=umlclassdiagram_PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_primaryexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PrimaryExpCS)

@given(instance=umlclassdiagram_NavigationExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_navigationexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_NavigationExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=umlclassdiagram_CallExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_callexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=umlclassdiagram_LogicExpCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_logicexpcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_LogicExpCS)



@given(instance=umlclassdiagram_LogicExpCS_strategy)
def test_umlclassdiagram_logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=umlclassdiagram_ParameterCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_parametercs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ParameterCS)



@given(instance=umlclassdiagram_ParameterCS_strategy)
def test_umlclassdiagram_parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_OperationCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_operationcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_OperationCS)



@given(instance=umlclassdiagram_OperationCS_strategy)
def test_umlclassdiagram_operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_PropertyCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_propertycs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PropertyCS)



@given(instance=umlclassdiagram_PropertyCS_strategy)
def test_umlclassdiagram_propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_PathNameCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_pathnamecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PathNameCS)

@given(instance=umlclassdiagram_ClassCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_classcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ClassCS)



@given(instance=umlclassdiagram_ClassCS_strategy)
def test_umlclassdiagram_classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_ConstraintCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_constraintcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_ConstraintCS)

@given(instance=umlclassdiagram_PackageCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_packagecs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_PackageCS)



@given(instance=umlclassdiagram_PackageCS_strategy)
def test_umlclassdiagram_packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=umlclassdiagram_RootCS_strategy)
@settings(max_examples=50)
def test_umlclassdiagram_rootcs_instantiation(instance):
    assert isinstance(instance, umlclassdiagram_RootCS)
