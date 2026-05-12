import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    uml2CD_Class,
    uml2CD_Association,
    uml2CD_DataType,
    uml2CD_Package,
    uml2CD_Constraint,
    uml2CD_NamedElement,
    uml2CD_Property,
    uml2CD_Comment,
    uml2CD_UMLModel,
    uml2CD_EnumerationLiteral,
    DataType,
    uml2CD_Enumeration,
    uml2CD_PrimitiveType,
    uml2CD_Operation,
    uml2CD_Parameter,
    uml2CD_GeneralizationSet,
    uml2CD_Generalization,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_class_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Class)


def test_uml2cd_class_constructor_exists():
    assert callable(uml2CD_Class.__init__)


def test_uml2cd_class_constructor_args():
    sig = inspect.signature(uml2CD_Class.__init__)
    params = list(sig.parameters.keys())
    assert "active" in params, "Missing parameter 'active'"

def test_uml2cd_class_has_active():
    assert hasattr(uml2CD_Class, "active")
    descriptor = None
    for klass in uml2CD_Class.__mro__:
        if "active" in klass.__dict__:
            descriptor = klass.__dict__["active"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_association_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Association)


def test_uml2cd_association_constructor_exists():
    assert callable(uml2CD_Association.__init__)


def test_uml2cd_association_constructor_args():
    sig = inspect.signature(uml2CD_Association.__init__)
    params = list(sig.parameters.keys())
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml2cd_association_has_isDerived():
    assert hasattr(uml2CD_Association, "isDerived")
    descriptor = None
    for klass in uml2CD_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_datatype_is_not_abstract():
    assert not inspect.isabstract(uml2CD_DataType)


def test_uml2cd_datatype_constructor_exists():
    assert callable(uml2CD_DataType.__init__)


def test_uml2cd_datatype_constructor_args():
    sig = inspect.signature(uml2CD_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_package_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Package)


def test_uml2cd_package_constructor_exists():
    assert callable(uml2CD_Package.__init__)


def test_uml2cd_package_constructor_args():
    sig = inspect.signature(uml2CD_Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_constraint_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Constraint)


def test_uml2cd_constraint_constructor_exists():
    assert callable(uml2CD_Constraint.__init__)


def test_uml2cd_constraint_constructor_args():
    sig = inspect.signature(uml2CD_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "specification" in params, "Missing parameter 'specification'"

def test_uml2cd_constraint_has_specification():
    assert hasattr(uml2CD_Constraint, "specification")
    descriptor = None
    for klass in uml2CD_Constraint.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_namedelement_is_not_abstract():
    assert not inspect.isabstract(uml2CD_NamedElement)


def test_uml2cd_namedelement_constructor_exists():
    assert callable(uml2CD_NamedElement.__init__)


def test_uml2cd_namedelement_constructor_args():
    sig = inspect.signature(uml2CD_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_uml2cd_namedelement_has_name():
    assert hasattr(uml2CD_NamedElement, "name")
    descriptor = None
    for klass in uml2CD_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_property_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Property)


def test_uml2cd_property_constructor_exists():
    assert callable(uml2CD_Property.__init__)


def test_uml2cd_property_constructor_args():
    sig = inspect.signature(uml2CD_Property.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_uml2cd_property_has_lower():
    assert hasattr(uml2CD_Property, "lower")
    descriptor = None
    for klass in uml2CD_Property.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_property_has_isDerived():
    assert hasattr(uml2CD_Property, "isDerived")
    descriptor = None
    for klass in uml2CD_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_property_has_aggregation():
    assert hasattr(uml2CD_Property, "aggregation")
    descriptor = None
    for klass in uml2CD_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_property_has_upper():
    assert hasattr(uml2CD_Property, "upper")
    descriptor = None
    for klass in uml2CD_Property.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_comment_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Comment)


def test_uml2cd_comment_constructor_exists():
    assert callable(uml2CD_Comment.__init__)


def test_uml2cd_comment_constructor_args():
    sig = inspect.signature(uml2CD_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_uml2cd_comment_has_value():
    assert hasattr(uml2CD_Comment, "value")
    descriptor = None
    for klass in uml2CD_Comment.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_umlmodel_is_not_abstract():
    assert not inspect.isabstract(uml2CD_UMLModel)


def test_uml2cd_umlmodel_constructor_exists():
    assert callable(uml2CD_UMLModel.__init__)


def test_uml2cd_umlmodel_constructor_args():
    sig = inspect.signature(uml2CD_UMLModel.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(uml2CD_EnumerationLiteral)


def test_uml2cd_enumerationliteral_constructor_exists():
    assert callable(uml2CD_EnumerationLiteral.__init__)


def test_uml2cd_enumerationliteral_constructor_args():
    sig = inspect.signature(uml2CD_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_enumeration_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Enumeration)


def test_uml2cd_enumeration_constructor_exists():
    assert callable(uml2CD_Enumeration.__init__)


def test_uml2cd_enumeration_constructor_args():
    sig = inspect.signature(uml2CD_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_primitivetype_is_not_abstract():
    assert not inspect.isabstract(uml2CD_PrimitiveType)


def test_uml2cd_primitivetype_constructor_exists():
    assert callable(uml2CD_PrimitiveType.__init__)


def test_uml2cd_primitivetype_constructor_args():
    sig = inspect.signature(uml2CD_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2cd_operation_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Operation)


def test_uml2cd_operation_constructor_exists():
    assert callable(uml2CD_Operation.__init__)


def test_uml2cd_operation_constructor_args():
    sig = inspect.signature(uml2CD_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "body" in params, "Missing parameter 'body'"

def test_uml2cd_operation_has_visibility():
    assert hasattr(uml2CD_Operation, "visibility")
    descriptor = None
    for klass in uml2CD_Operation.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_operation_has_isQuery():
    assert hasattr(uml2CD_Operation, "isQuery")
    descriptor = None
    for klass in uml2CD_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_operation_has_body():
    assert hasattr(uml2CD_Operation, "body")
    descriptor = None
    for klass in uml2CD_Operation.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_parameter_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Parameter)


def test_uml2cd_parameter_constructor_exists():
    assert callable(uml2CD_Parameter.__init__)


def test_uml2cd_parameter_constructor_args():
    sig = inspect.signature(uml2CD_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_uml2cd_parameter_has_defaultValue():
    assert hasattr(uml2CD_Parameter, "defaultValue")
    descriptor = None
    for klass in uml2CD_Parameter.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_parameter_has_kind():
    assert hasattr(uml2CD_Parameter, "kind")
    descriptor = None
    for klass in uml2CD_Parameter.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_generalizationset_is_not_abstract():
    assert not inspect.isabstract(uml2CD_GeneralizationSet)


def test_uml2cd_generalizationset_constructor_exists():
    assert callable(uml2CD_GeneralizationSet.__init__)


def test_uml2cd_generalizationset_constructor_args():
    sig = inspect.signature(uml2CD_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_uml2cd_generalizationset_has_isCovering():
    assert hasattr(uml2CD_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in uml2CD_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_uml2cd_generalizationset_has_isDisjoint():
    assert hasattr(uml2CD_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in uml2CD_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_uml2cd_generalization_is_not_abstract():
    assert not inspect.isabstract(uml2CD_Generalization)


def test_uml2cd_generalization_constructor_exists():
    assert callable(uml2CD_Generalization.__init__)


def test_uml2cd_generalization_constructor_args():
    sig = inspect.signature(uml2CD_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_uml2cd_generalization_has_isSubstitutable():
    assert hasattr(uml2CD_Generalization, "isSubstitutable")
    descriptor = None
    for klass in uml2CD_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
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
NamedElement_strategy = st.builds(
    NamedElement,
)
uml2CD_Class_strategy = st.builds(
    uml2CD_Class,
    active=
        safe_text
)
uml2CD_Association_strategy = st.builds(
    uml2CD_Association,
    isDerived=
        safe_text
)
uml2CD_DataType_strategy = st.builds(
    uml2CD_DataType,
)
uml2CD_Package_strategy = st.builds(
    uml2CD_Package,
)
uml2CD_Constraint_strategy = st.builds(
    uml2CD_Constraint,
    specification=
        safe_text
)
uml2CD_NamedElement_strategy = st.builds(
    uml2CD_NamedElement,
    name=
        safe_text
)
uml2CD_Property_strategy = st.builds(
    uml2CD_Property,
    lower=
        safe_text,
    isDerived=
        safe_text,
    aggregation=
        safe_text,
    upper=
        safe_text
)
uml2CD_Comment_strategy = st.builds(
    uml2CD_Comment,
    value=
        safe_text
)
uml2CD_UMLModel_strategy = st.builds(
    uml2CD_UMLModel,
)
uml2CD_EnumerationLiteral_strategy = st.builds(
    uml2CD_EnumerationLiteral,
)
DataType_strategy = st.builds(
    DataType,
)
uml2CD_Enumeration_strategy = st.builds(
    uml2CD_Enumeration,
)
uml2CD_PrimitiveType_strategy = st.builds(
    uml2CD_PrimitiveType,
)
uml2CD_Operation_strategy = st.builds(
    uml2CD_Operation,
    visibility=
        safe_text,
    isQuery=
        safe_text,
    body=
        safe_text
)
uml2CD_Parameter_strategy = st.builds(
    uml2CD_Parameter,
    defaultValue=
        safe_text,
    kind=
        safe_text
)
uml2CD_GeneralizationSet_strategy = st.builds(
    uml2CD_GeneralizationSet,
    isCovering=
        safe_text,
    isDisjoint=
        safe_text
)
uml2CD_Generalization_strategy = st.builds(
    uml2CD_Generalization,
    isSubstitutable=
        st.booleans()
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=uml2CD_Class_strategy)
@settings(max_examples=50)
def test_uml2cd_class_instantiation(instance):
    assert isinstance(instance, uml2CD_Class)



@given(instance=uml2CD_Class_strategy)
def test_uml2cd_class_active_setter(instance):
    original = instance.active
    instance.active = original
    assert instance.active == original

@given(instance=uml2CD_Association_strategy)
@settings(max_examples=50)
def test_uml2cd_association_instantiation(instance):
    assert isinstance(instance, uml2CD_Association)



@given(instance=uml2CD_Association_strategy)
def test_uml2cd_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=uml2CD_DataType_strategy)
@settings(max_examples=50)
def test_uml2cd_datatype_instantiation(instance):
    assert isinstance(instance, uml2CD_DataType)

@given(instance=uml2CD_Package_strategy)
@settings(max_examples=50)
def test_uml2cd_package_instantiation(instance):
    assert isinstance(instance, uml2CD_Package)

@given(instance=uml2CD_Constraint_strategy)
@settings(max_examples=50)
def test_uml2cd_constraint_instantiation(instance):
    assert isinstance(instance, uml2CD_Constraint)



@given(instance=uml2CD_Constraint_strategy)
def test_uml2cd_constraint_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original

@given(instance=uml2CD_NamedElement_strategy)
@settings(max_examples=50)
def test_uml2cd_namedelement_instantiation(instance):
    assert isinstance(instance, uml2CD_NamedElement)



@given(instance=uml2CD_NamedElement_strategy)
def test_uml2cd_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=uml2CD_Property_strategy)
@settings(max_examples=50)
def test_uml2cd_property_instantiation(instance):
    assert isinstance(instance, uml2CD_Property)



@given(instance=uml2CD_Property_strategy)
def test_uml2cd_property_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=uml2CD_Property_strategy)
def test_uml2cd_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=uml2CD_Property_strategy)
def test_uml2cd_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=uml2CD_Property_strategy)
def test_uml2cd_property_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=uml2CD_Comment_strategy)
@settings(max_examples=50)
def test_uml2cd_comment_instantiation(instance):
    assert isinstance(instance, uml2CD_Comment)



@given(instance=uml2CD_Comment_strategy)
def test_uml2cd_comment_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=uml2CD_UMLModel_strategy)
@settings(max_examples=50)
def test_uml2cd_umlmodel_instantiation(instance):
    assert isinstance(instance, uml2CD_UMLModel)

@given(instance=uml2CD_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2cd_enumerationliteral_instantiation(instance):
    assert isinstance(instance, uml2CD_EnumerationLiteral)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=uml2CD_Enumeration_strategy)
@settings(max_examples=50)
def test_uml2cd_enumeration_instantiation(instance):
    assert isinstance(instance, uml2CD_Enumeration)

@given(instance=uml2CD_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2cd_primitivetype_instantiation(instance):
    assert isinstance(instance, uml2CD_PrimitiveType)

@given(instance=uml2CD_Operation_strategy)
@settings(max_examples=50)
def test_uml2cd_operation_instantiation(instance):
    assert isinstance(instance, uml2CD_Operation)



@given(instance=uml2CD_Operation_strategy)
def test_uml2cd_operation_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=uml2CD_Operation_strategy)
def test_uml2cd_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original



@given(instance=uml2CD_Operation_strategy)
def test_uml2cd_operation_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=uml2CD_Parameter_strategy)
@settings(max_examples=50)
def test_uml2cd_parameter_instantiation(instance):
    assert isinstance(instance, uml2CD_Parameter)



@given(instance=uml2CD_Parameter_strategy)
def test_uml2cd_parameter_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=uml2CD_Parameter_strategy)
def test_uml2cd_parameter_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=uml2CD_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2cd_generalizationset_instantiation(instance):
    assert isinstance(instance, uml2CD_GeneralizationSet)



@given(instance=uml2CD_GeneralizationSet_strategy)
def test_uml2cd_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original



@given(instance=uml2CD_GeneralizationSet_strategy)
def test_uml2cd_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=uml2CD_Generalization_strategy)
@settings(max_examples=50)
def test_uml2cd_generalization_instantiation(instance):
    assert isinstance(instance, uml2CD_Generalization)



@given(instance=uml2CD_Generalization_strategy)
def test_uml2cd_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original
