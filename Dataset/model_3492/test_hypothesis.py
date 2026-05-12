import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Abstract_ATT_ID,
    vM_PairFeatureReal,
    vM_PairFeatureInteger,
    TableBasedValuationByAttribute,
    vM_TableBasedValuationByAttributeForReal,
    vM_TableBasedValuationByAttributeForInteger,
    vM_PairAttributeValue,
    vM_TableBasedValuationByFeatureAndClone,
    vM_TableBasedValuationByAttribute,
    vM_TableBasedValuationByFeature,
    BasicAttrValuation,
    vM_IntegerAttrValuation,
    vM_StringAttrValuation,
    vM_BooleanAttrValuation,
    vM_RealAttrValuation,
    ExtendedValuation,
    vM_AdvancedAttrValuation,
    vM_Configuration,
    vM_ObjectiveExpression,
    vM_Objective,
    vM_NumericExpression_List,
    vM_BooleanExpression_List,
    vM_ExtendedValuation,
    vM_BooleanValuation,
    vM_AttHead,
    Expression,
    vM_StringExpression,
    vM_NumericExpression,
    vM_PrimitiveExpression,
    vM_BrackedExpression,
    vM_SpecialExpression,
    ComplexExpression,
    vM_Minus,
    vM_Equality,
    vM_If,
    vM_Requires,
    vM_Inequality,
    vM_Or,
    vM_Multiplication,
    vM_Lessequal,
    vM_Less,
    vM_LeftImplication,
    vM_Greater,
    vM_RightImplication,
    vM_Greaterequal,
    vM_And,
    vM_Plus,
    vM_Excludes,
    vM_Division,
    vM_BiImplication,
    vM_Expression,
    vM_ComplexExpression,
    vM_Constraint,
    vM_Abstract_ATT_ID,
    vM_BooleanExpression,
    vM_AttributeDescription,
    vM_FeatureDescription,
    vM_Enum_Real_ATT_ID,
    vM_Enum_Integer_ATT_ID,
    vM_Enum_String_ATT_ID,
    EnumAttrDef,
    vM_EnumRealDef,
    vM_EnumIntegerDef,
    vM_EnumStringDef,
    vM_RealDeltaDef,
    vM_RealDefaultDef,
    vM_Real_ATT_ID,
    vM_IntegerDeltaDef,
    vM_IntegerAttrDefComplement,
    IntegerAttrDef,
    vM_IntegerAttrDefUnbounded,
    vM_IntegerAttrDefBounded,
    vM_IntegerDefaultDef,
    vM_Integer_ATT_ID,
    vM_BasicAttrValuation,
    vM_StringDefaultDef,
    vM_AttrDef,
    vM_String_ATT_ID,
    vM_BoolDefaultDef,
    vM_Boolean_ATT_ID,
    FeaturesGroup,
    vM_Orgroup,
    vM_CardinalityBased,
    BasicAttrDef,
    vM_StringAttrDef,
    vM_RealAttrDef,
    vM_IntegerAttrDef,
    vM_Xorgroup,
    vM_BooleanAttrDef,
    vM_EnumAttrDef,
    vM_BasicAttrDef,
    vM_RealAttrDefComplement,
    RealAttrDef,
    vM_RealAttrDefUnbounded,
    vM_RealAttrDefBounded,
    vM_Email,
    vM_Version,
    VmBlock,
    vM_Attributes,
    vM_MetaDataDeclaration,
    vM_ImportDeclaration,
    vM_Constraints,
    vM_Descriptions,
    vM_Configurations,
    vM_Objectives,
    vM_PackageDeclaration,
    vM_FeatureDefinition,
    FeatureDefinition,
    vM_Feature,
    vM_FeaturesGroup,
    vM_FeatureHierarchy,
    vM_Relationships,
    vM_VmBlock,
    vM_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abstract_att_id_is_not_abstract():
    assert not inspect.isabstract(Abstract_ATT_ID)


def test_abstract_att_id_constructor_exists():
    assert callable(Abstract_ATT_ID.__init__)


def test_abstract_att_id_constructor_args():
    sig = inspect.signature(Abstract_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_pairfeaturereal_is_not_abstract():
    assert not inspect.isabstract(vM_PairFeatureReal)


def test_vm_pairfeaturereal_constructor_exists():
    assert callable(vM_PairFeatureReal.__init__)


def test_vm_pairfeaturereal_constructor_args():
    sig = inspect.signature(vM_PairFeatureReal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_pairfeaturereal_has_value():
    assert hasattr(vM_PairFeatureReal, "value")
    descriptor = None
    for klass in vM_PairFeatureReal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_pairfeatureinteger_is_not_abstract():
    assert not inspect.isabstract(vM_PairFeatureInteger)


def test_vm_pairfeatureinteger_constructor_exists():
    assert callable(vM_PairFeatureInteger.__init__)


def test_vm_pairfeatureinteger_constructor_args():
    sig = inspect.signature(vM_PairFeatureInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_pairfeatureinteger_has_value():
    assert hasattr(vM_PairFeatureInteger, "value")
    descriptor = None
    for klass in vM_PairFeatureInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tablebasedvaluationbyattribute_is_not_abstract():
    assert not inspect.isabstract(TableBasedValuationByAttribute)


def test_tablebasedvaluationbyattribute_constructor_exists():
    assert callable(TableBasedValuationByAttribute.__init__)


def test_tablebasedvaluationbyattribute_constructor_args():
    sig = inspect.signature(TableBasedValuationByAttribute.__init__)
    params = list(sig.parameters.keys())



def test_vm_tablebasedvaluationbyattributeforreal_is_not_abstract():
    assert not inspect.isabstract(vM_TableBasedValuationByAttributeForReal)


def test_vm_tablebasedvaluationbyattributeforreal_constructor_exists():
    assert callable(vM_TableBasedValuationByAttributeForReal.__init__)


def test_vm_tablebasedvaluationbyattributeforreal_constructor_args():
    sig = inspect.signature(vM_TableBasedValuationByAttributeForReal.__init__)
    params = list(sig.parameters.keys())



def test_vm_tablebasedvaluationbyattributeforinteger_is_not_abstract():
    assert not inspect.isabstract(vM_TableBasedValuationByAttributeForInteger)


def test_vm_tablebasedvaluationbyattributeforinteger_constructor_exists():
    assert callable(vM_TableBasedValuationByAttributeForInteger.__init__)


def test_vm_tablebasedvaluationbyattributeforinteger_constructor_args():
    sig = inspect.signature(vM_TableBasedValuationByAttributeForInteger.__init__)
    params = list(sig.parameters.keys())



def test_vm_pairattributevalue_is_not_abstract():
    assert not inspect.isabstract(vM_PairAttributeValue)


def test_vm_pairattributevalue_constructor_exists():
    assert callable(vM_PairAttributeValue.__init__)


def test_vm_pairattributevalue_constructor_args():
    sig = inspect.signature(vM_PairAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_pairattributevalue_has_value():
    assert hasattr(vM_PairAttributeValue, "value")
    descriptor = None
    for klass in vM_PairAttributeValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_tablebasedvaluationbyfeatureandclone_is_not_abstract():
    assert not inspect.isabstract(vM_TableBasedValuationByFeatureAndClone)


def test_vm_tablebasedvaluationbyfeatureandclone_constructor_exists():
    assert callable(vM_TableBasedValuationByFeatureAndClone.__init__)


def test_vm_tablebasedvaluationbyfeatureandclone_constructor_args():
    sig = inspect.signature(vM_TableBasedValuationByFeatureAndClone.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm_tablebasedvaluationbyfeatureandclone_has_name():
    assert hasattr(vM_TableBasedValuationByFeatureAndClone, "name")
    descriptor = None
    for klass in vM_TableBasedValuationByFeatureAndClone.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm_tablebasedvaluationbyattribute_is_not_abstract():
    assert not inspect.isabstract(vM_TableBasedValuationByAttribute)


def test_vm_tablebasedvaluationbyattribute_constructor_exists():
    assert callable(vM_TableBasedValuationByAttribute.__init__)


def test_vm_tablebasedvaluationbyattribute_constructor_args():
    sig = inspect.signature(vM_TableBasedValuationByAttribute.__init__)
    params = list(sig.parameters.keys())



def test_vm_tablebasedvaluationbyfeature_is_not_abstract():
    assert not inspect.isabstract(vM_TableBasedValuationByFeature)


def test_vm_tablebasedvaluationbyfeature_constructor_exists():
    assert callable(vM_TableBasedValuationByFeature.__init__)


def test_vm_tablebasedvaluationbyfeature_constructor_args():
    sig = inspect.signature(vM_TableBasedValuationByFeature.__init__)
    params = list(sig.parameters.keys())



def test_basicattrvaluation_is_not_abstract():
    assert not inspect.isabstract(BasicAttrValuation)


def test_basicattrvaluation_constructor_exists():
    assert callable(BasicAttrValuation.__init__)


def test_basicattrvaluation_constructor_args():
    sig = inspect.signature(BasicAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_integerattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerAttrValuation)


def test_vm_integerattrvaluation_constructor_exists():
    assert callable(vM_IntegerAttrValuation.__init__)


def test_vm_integerattrvaluation_constructor_args():
    sig = inspect.signature(vM_IntegerAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_stringattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_StringAttrValuation)


def test_vm_stringattrvaluation_constructor_exists():
    assert callable(vM_StringAttrValuation.__init__)


def test_vm_stringattrvaluation_constructor_args():
    sig = inspect.signature(vM_StringAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_booleanattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_BooleanAttrValuation)


def test_vm_booleanattrvaluation_constructor_exists():
    assert callable(vM_BooleanAttrValuation.__init__)


def test_vm_booleanattrvaluation_constructor_args():
    sig = inspect.signature(vM_BooleanAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_realattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_RealAttrValuation)


def test_vm_realattrvaluation_constructor_exists():
    assert callable(vM_RealAttrValuation.__init__)


def test_vm_realattrvaluation_constructor_args():
    sig = inspect.signature(vM_RealAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_extendedvaluation_is_not_abstract():
    assert not inspect.isabstract(ExtendedValuation)


def test_extendedvaluation_constructor_exists():
    assert callable(ExtendedValuation.__init__)


def test_extendedvaluation_constructor_args():
    sig = inspect.signature(ExtendedValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_advancedattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_AdvancedAttrValuation)


def test_vm_advancedattrvaluation_constructor_exists():
    assert callable(vM_AdvancedAttrValuation.__init__)


def test_vm_advancedattrvaluation_constructor_args():
    sig = inspect.signature(vM_AdvancedAttrValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_configuration_is_not_abstract():
    assert not inspect.isabstract(vM_Configuration)


def test_vm_configuration_constructor_exists():
    assert callable(vM_Configuration.__init__)


def test_vm_configuration_constructor_args():
    sig = inspect.signature(vM_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm_configuration_has_name():
    assert hasattr(vM_Configuration, "name")
    descriptor = None
    for klass in vM_Configuration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm_objectiveexpression_is_not_abstract():
    assert not inspect.isabstract(vM_ObjectiveExpression)


def test_vm_objectiveexpression_constructor_exists():
    assert callable(vM_ObjectiveExpression.__init__)


def test_vm_objectiveexpression_constructor_args():
    sig = inspect.signature(vM_ObjectiveExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_vm_objectiveexpression_has_op():
    assert hasattr(vM_ObjectiveExpression, "op")
    descriptor = None
    for klass in vM_ObjectiveExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm_objective_is_not_abstract():
    assert not inspect.isabstract(vM_Objective)


def test_vm_objective_constructor_exists():
    assert callable(vM_Objective.__init__)


def test_vm_objective_constructor_args():
    sig = inspect.signature(vM_Objective.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "op" in params, "Missing parameter 'op'"

def test_vm_objective_has_name():
    assert hasattr(vM_Objective, "name")
    descriptor = None
    for klass in vM_Objective.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm_objective_has_op():
    assert hasattr(vM_Objective, "op")
    descriptor = None
    for klass in vM_Objective.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_vm_numericexpression_list_is_not_abstract():
    assert not inspect.isabstract(vM_NumericExpression_List)


def test_vm_numericexpression_list_constructor_exists():
    assert callable(vM_NumericExpression_List.__init__)


def test_vm_numericexpression_list_constructor_args():
    sig = inspect.signature(vM_NumericExpression_List.__init__)
    params = list(sig.parameters.keys())



def test_vm_booleanexpression_list_is_not_abstract():
    assert not inspect.isabstract(vM_BooleanExpression_List)


def test_vm_booleanexpression_list_constructor_exists():
    assert callable(vM_BooleanExpression_List.__init__)


def test_vm_booleanexpression_list_constructor_args():
    sig = inspect.signature(vM_BooleanExpression_List.__init__)
    params = list(sig.parameters.keys())



def test_vm_extendedvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_ExtendedValuation)


def test_vm_extendedvaluation_constructor_exists():
    assert callable(vM_ExtendedValuation.__init__)


def test_vm_extendedvaluation_constructor_args():
    sig = inspect.signature(vM_ExtendedValuation.__init__)
    params = list(sig.parameters.keys())



def test_vm_booleanvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_BooleanValuation)


def test_vm_booleanvaluation_constructor_exists():
    assert callable(vM_BooleanValuation.__init__)


def test_vm_booleanvaluation_constructor_args():
    sig = inspect.signature(vM_BooleanValuation.__init__)
    params = list(sig.parameters.keys())
    assert "notSelected" in params, "Missing parameter 'notSelected'"

def test_vm_booleanvaluation_has_notSelected():
    assert hasattr(vM_BooleanValuation, "notSelected")
    descriptor = None
    for klass in vM_BooleanValuation.__mro__:
        if "notSelected" in klass.__dict__:
            descriptor = klass.__dict__["notSelected"]
            break
    assert isinstance(descriptor, property)



def test_vm_atthead_is_not_abstract():
    assert not inspect.isabstract(vM_AttHead)


def test_vm_atthead_constructor_exists():
    assert callable(vM_AttHead.__init__)


def test_vm_atthead_constructor_args():
    sig = inspect.signature(vM_AttHead.__init__)
    params = list(sig.parameters.keys())
    assert "forAllFeatures" in params, "Missing parameter 'forAllFeatures'"

def test_vm_atthead_has_forAllFeatures():
    assert hasattr(vM_AttHead, "forAllFeatures")
    descriptor = None
    for klass in vM_AttHead.__mro__:
        if "forAllFeatures" in klass.__dict__:
            descriptor = klass.__dict__["forAllFeatures"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_vm_stringexpression_is_not_abstract():
    assert not inspect.isabstract(vM_StringExpression)


def test_vm_stringexpression_constructor_exists():
    assert callable(vM_StringExpression.__init__)


def test_vm_stringexpression_constructor_args():
    sig = inspect.signature(vM_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_stringexpression_has_value():
    assert hasattr(vM_StringExpression, "value")
    descriptor = None
    for klass in vM_StringExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_numericexpression_is_not_abstract():
    assert not inspect.isabstract(vM_NumericExpression)


def test_vm_numericexpression_constructor_exists():
    assert callable(vM_NumericExpression.__init__)


def test_vm_numericexpression_constructor_args():
    sig = inspect.signature(vM_NumericExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "value" in params, "Missing parameter 'value'"

def test_vm_numericexpression_has_op():
    assert hasattr(vM_NumericExpression, "op")
    descriptor = None
    for klass in vM_NumericExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_vm_numericexpression_has_value():
    assert hasattr(vM_NumericExpression, "value")
    descriptor = None
    for klass in vM_NumericExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(vM_PrimitiveExpression)


def test_vm_primitiveexpression_constructor_exists():
    assert callable(vM_PrimitiveExpression.__init__)


def test_vm_primitiveexpression_constructor_args():
    sig = inspect.signature(vM_PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm_brackedexpression_is_not_abstract():
    assert not inspect.isabstract(vM_BrackedExpression)


def test_vm_brackedexpression_constructor_exists():
    assert callable(vM_BrackedExpression.__init__)


def test_vm_brackedexpression_constructor_args():
    sig = inspect.signature(vM_BrackedExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm_specialexpression_is_not_abstract():
    assert not inspect.isabstract(vM_SpecialExpression)


def test_vm_specialexpression_constructor_exists():
    assert callable(vM_SpecialExpression.__init__)


def test_vm_specialexpression_constructor_args():
    sig = inspect.signature(vM_SpecialExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_vm_specialexpression_has_op():
    assert hasattr(vM_SpecialExpression, "op")
    descriptor = None
    for klass in vM_SpecialExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_complexexpression_is_not_abstract():
    assert not inspect.isabstract(ComplexExpression)


def test_complexexpression_constructor_exists():
    assert callable(ComplexExpression.__init__)


def test_complexexpression_constructor_args():
    sig = inspect.signature(ComplexExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm_minus_is_not_abstract():
    assert not inspect.isabstract(vM_Minus)


def test_vm_minus_constructor_exists():
    assert callable(vM_Minus.__init__)


def test_vm_minus_constructor_args():
    sig = inspect.signature(vM_Minus.__init__)
    params = list(sig.parameters.keys())



def test_vm_equality_is_not_abstract():
    assert not inspect.isabstract(vM_Equality)


def test_vm_equality_constructor_exists():
    assert callable(vM_Equality.__init__)


def test_vm_equality_constructor_args():
    sig = inspect.signature(vM_Equality.__init__)
    params = list(sig.parameters.keys())



def test_vm_if_is_not_abstract():
    assert not inspect.isabstract(vM_If)


def test_vm_if_constructor_exists():
    assert callable(vM_If.__init__)


def test_vm_if_constructor_args():
    sig = inspect.signature(vM_If.__init__)
    params = list(sig.parameters.keys())



def test_vm_requires_is_not_abstract():
    assert not inspect.isabstract(vM_Requires)


def test_vm_requires_constructor_exists():
    assert callable(vM_Requires.__init__)


def test_vm_requires_constructor_args():
    sig = inspect.signature(vM_Requires.__init__)
    params = list(sig.parameters.keys())



def test_vm_inequality_is_not_abstract():
    assert not inspect.isabstract(vM_Inequality)


def test_vm_inequality_constructor_exists():
    assert callable(vM_Inequality.__init__)


def test_vm_inequality_constructor_args():
    sig = inspect.signature(vM_Inequality.__init__)
    params = list(sig.parameters.keys())



def test_vm_or_is_not_abstract():
    assert not inspect.isabstract(vM_Or)


def test_vm_or_constructor_exists():
    assert callable(vM_Or.__init__)


def test_vm_or_constructor_args():
    sig = inspect.signature(vM_Or.__init__)
    params = list(sig.parameters.keys())



def test_vm_multiplication_is_not_abstract():
    assert not inspect.isabstract(vM_Multiplication)


def test_vm_multiplication_constructor_exists():
    assert callable(vM_Multiplication.__init__)


def test_vm_multiplication_constructor_args():
    sig = inspect.signature(vM_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_vm_lessequal_is_not_abstract():
    assert not inspect.isabstract(vM_Lessequal)


def test_vm_lessequal_constructor_exists():
    assert callable(vM_Lessequal.__init__)


def test_vm_lessequal_constructor_args():
    sig = inspect.signature(vM_Lessequal.__init__)
    params = list(sig.parameters.keys())



def test_vm_less_is_not_abstract():
    assert not inspect.isabstract(vM_Less)


def test_vm_less_constructor_exists():
    assert callable(vM_Less.__init__)


def test_vm_less_constructor_args():
    sig = inspect.signature(vM_Less.__init__)
    params = list(sig.parameters.keys())



def test_vm_leftimplication_is_not_abstract():
    assert not inspect.isabstract(vM_LeftImplication)


def test_vm_leftimplication_constructor_exists():
    assert callable(vM_LeftImplication.__init__)


def test_vm_leftimplication_constructor_args():
    sig = inspect.signature(vM_LeftImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm_greater_is_not_abstract():
    assert not inspect.isabstract(vM_Greater)


def test_vm_greater_constructor_exists():
    assert callable(vM_Greater.__init__)


def test_vm_greater_constructor_args():
    sig = inspect.signature(vM_Greater.__init__)
    params = list(sig.parameters.keys())



def test_vm_rightimplication_is_not_abstract():
    assert not inspect.isabstract(vM_RightImplication)


def test_vm_rightimplication_constructor_exists():
    assert callable(vM_RightImplication.__init__)


def test_vm_rightimplication_constructor_args():
    sig = inspect.signature(vM_RightImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm_greaterequal_is_not_abstract():
    assert not inspect.isabstract(vM_Greaterequal)


def test_vm_greaterequal_constructor_exists():
    assert callable(vM_Greaterequal.__init__)


def test_vm_greaterequal_constructor_args():
    sig = inspect.signature(vM_Greaterequal.__init__)
    params = list(sig.parameters.keys())



def test_vm_and_is_not_abstract():
    assert not inspect.isabstract(vM_And)


def test_vm_and_constructor_exists():
    assert callable(vM_And.__init__)


def test_vm_and_constructor_args():
    sig = inspect.signature(vM_And.__init__)
    params = list(sig.parameters.keys())



def test_vm_plus_is_not_abstract():
    assert not inspect.isabstract(vM_Plus)


def test_vm_plus_constructor_exists():
    assert callable(vM_Plus.__init__)


def test_vm_plus_constructor_args():
    sig = inspect.signature(vM_Plus.__init__)
    params = list(sig.parameters.keys())



def test_vm_excludes_is_not_abstract():
    assert not inspect.isabstract(vM_Excludes)


def test_vm_excludes_constructor_exists():
    assert callable(vM_Excludes.__init__)


def test_vm_excludes_constructor_args():
    sig = inspect.signature(vM_Excludes.__init__)
    params = list(sig.parameters.keys())



def test_vm_division_is_not_abstract():
    assert not inspect.isabstract(vM_Division)


def test_vm_division_constructor_exists():
    assert callable(vM_Division.__init__)


def test_vm_division_constructor_args():
    sig = inspect.signature(vM_Division.__init__)
    params = list(sig.parameters.keys())



def test_vm_biimplication_is_not_abstract():
    assert not inspect.isabstract(vM_BiImplication)


def test_vm_biimplication_constructor_exists():
    assert callable(vM_BiImplication.__init__)


def test_vm_biimplication_constructor_args():
    sig = inspect.signature(vM_BiImplication.__init__)
    params = list(sig.parameters.keys())



def test_vm_expression_is_not_abstract():
    assert not inspect.isabstract(vM_Expression)


def test_vm_expression_constructor_exists():
    assert callable(vM_Expression.__init__)


def test_vm_expression_constructor_args():
    sig = inspect.signature(vM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_vm_complexexpression_is_not_abstract():
    assert not inspect.isabstract(vM_ComplexExpression)


def test_vm_complexexpression_constructor_exists():
    assert callable(vM_ComplexExpression.__init__)


def test_vm_complexexpression_constructor_args():
    sig = inspect.signature(vM_ComplexExpression.__init__)
    params = list(sig.parameters.keys())



def test_vm_constraint_is_not_abstract():
    assert not inspect.isabstract(vM_Constraint)


def test_vm_constraint_constructor_exists():
    assert callable(vM_Constraint.__init__)


def test_vm_constraint_constructor_args():
    sig = inspect.signature(vM_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_vm_constraint_has_name():
    assert hasattr(vM_Constraint, "name")
    descriptor = None
    for klass in vM_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm_constraint_has_not_():
    assert hasattr(vM_Constraint, "not_")
    descriptor = None
    for klass in vM_Constraint.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_vm_abstract_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Abstract_ATT_ID)


def test_vm_abstract_att_id_constructor_exists():
    assert callable(vM_Abstract_ATT_ID.__init__)


def test_vm_abstract_att_id_constructor_args():
    sig = inspect.signature(vM_Abstract_ATT_ID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm_abstract_att_id_has_name():
    assert hasattr(vM_Abstract_ATT_ID, "name")
    descriptor = None
    for klass in vM_Abstract_ATT_ID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm_booleanexpression_is_not_abstract():
    assert not inspect.isabstract(vM_BooleanExpression)


def test_vm_booleanexpression_constructor_exists():
    assert callable(vM_BooleanExpression.__init__)


def test_vm_booleanexpression_constructor_args():
    sig = inspect.signature(vM_BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "value" in params, "Missing parameter 'value'"

def test_vm_booleanexpression_has_op():
    assert hasattr(vM_BooleanExpression, "op")
    descriptor = None
    for klass in vM_BooleanExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_vm_booleanexpression_has_value():
    assert hasattr(vM_BooleanExpression, "value")
    descriptor = None
    for klass in vM_BooleanExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_attributedescription_is_not_abstract():
    assert not inspect.isabstract(vM_AttributeDescription)


def test_vm_attributedescription_constructor_exists():
    assert callable(vM_AttributeDescription.__init__)


def test_vm_attributedescription_constructor_args():
    sig = inspect.signature(vM_AttributeDescription.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_vm_attributedescription_has_description():
    assert hasattr(vM_AttributeDescription, "description")
    descriptor = None
    for klass in vM_AttributeDescription.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_vm_featuredescription_is_not_abstract():
    assert not inspect.isabstract(vM_FeatureDescription)


def test_vm_featuredescription_constructor_exists():
    assert callable(vM_FeatureDescription.__init__)


def test_vm_featuredescription_constructor_args():
    sig = inspect.signature(vM_FeatureDescription.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_vm_featuredescription_has_description():
    assert hasattr(vM_FeatureDescription, "description")
    descriptor = None
    for klass in vM_FeatureDescription.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_vm_enum_real_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Enum_Real_ATT_ID)


def test_vm_enum_real_att_id_constructor_exists():
    assert callable(vM_Enum_Real_ATT_ID.__init__)


def test_vm_enum_real_att_id_constructor_args():
    sig = inspect.signature(vM_Enum_Real_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_enum_integer_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Enum_Integer_ATT_ID)


def test_vm_enum_integer_att_id_constructor_exists():
    assert callable(vM_Enum_Integer_ATT_ID.__init__)


def test_vm_enum_integer_att_id_constructor_args():
    sig = inspect.signature(vM_Enum_Integer_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_enum_string_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Enum_String_ATT_ID)


def test_vm_enum_string_att_id_constructor_exists():
    assert callable(vM_Enum_String_ATT_ID.__init__)


def test_vm_enum_string_att_id_constructor_args():
    sig = inspect.signature(vM_Enum_String_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_enumattrdef_is_not_abstract():
    assert not inspect.isabstract(EnumAttrDef)


def test_enumattrdef_constructor_exists():
    assert callable(EnumAttrDef.__init__)


def test_enumattrdef_constructor_args():
    sig = inspect.signature(EnumAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_enumrealdef_is_not_abstract():
    assert not inspect.isabstract(vM_EnumRealDef)


def test_vm_enumrealdef_constructor_exists():
    assert callable(vM_EnumRealDef.__init__)


def test_vm_enumrealdef_constructor_args():
    sig = inspect.signature(vM_EnumRealDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_enumintegerdef_is_not_abstract():
    assert not inspect.isabstract(vM_EnumIntegerDef)


def test_vm_enumintegerdef_constructor_exists():
    assert callable(vM_EnumIntegerDef.__init__)


def test_vm_enumintegerdef_constructor_args():
    sig = inspect.signature(vM_EnumIntegerDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_enumstringdef_is_not_abstract():
    assert not inspect.isabstract(vM_EnumStringDef)


def test_vm_enumstringdef_constructor_exists():
    assert callable(vM_EnumStringDef.__init__)


def test_vm_enumstringdef_constructor_args():
    sig = inspect.signature(vM_EnumStringDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_realdeltadef_is_not_abstract():
    assert not inspect.isabstract(vM_RealDeltaDef)


def test_vm_realdeltadef_constructor_exists():
    assert callable(vM_RealDeltaDef.__init__)


def test_vm_realdeltadef_constructor_args():
    sig = inspect.signature(vM_RealDeltaDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_realdeltadef_has_value():
    assert hasattr(vM_RealDeltaDef, "value")
    descriptor = None
    for klass in vM_RealDeltaDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_realdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM_RealDefaultDef)


def test_vm_realdefaultdef_constructor_exists():
    assert callable(vM_RealDefaultDef.__init__)


def test_vm_realdefaultdef_constructor_args():
    sig = inspect.signature(vM_RealDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_realdefaultdef_has_value():
    assert hasattr(vM_RealDefaultDef, "value")
    descriptor = None
    for klass in vM_RealDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_real_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Real_ATT_ID)


def test_vm_real_att_id_constructor_exists():
    assert callable(vM_Real_ATT_ID.__init__)


def test_vm_real_att_id_constructor_args():
    sig = inspect.signature(vM_Real_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_integerdeltadef_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerDeltaDef)


def test_vm_integerdeltadef_constructor_exists():
    assert callable(vM_IntegerDeltaDef.__init__)


def test_vm_integerdeltadef_constructor_args():
    sig = inspect.signature(vM_IntegerDeltaDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_integerdeltadef_has_value():
    assert hasattr(vM_IntegerDeltaDef, "value")
    descriptor = None
    for klass in vM_IntegerDeltaDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_integerattrdefcomplement_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerAttrDefComplement)


def test_vm_integerattrdefcomplement_constructor_exists():
    assert callable(vM_IntegerAttrDefComplement.__init__)


def test_vm_integerattrdefcomplement_constructor_args():
    sig = inspect.signature(vM_IntegerAttrDefComplement.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_vm_integerattrdefcomplement_has_max():
    assert hasattr(vM_IntegerAttrDefComplement, "max")
    descriptor = None
    for klass in vM_IntegerAttrDefComplement.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_vm_integerattrdefcomplement_has_min():
    assert hasattr(vM_IntegerAttrDefComplement, "min")
    descriptor = None
    for klass in vM_IntegerAttrDefComplement.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_integerattrdef_is_not_abstract():
    assert not inspect.isabstract(IntegerAttrDef)


def test_integerattrdef_constructor_exists():
    assert callable(IntegerAttrDef.__init__)


def test_integerattrdef_constructor_args():
    sig = inspect.signature(IntegerAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_integerattrdefunbounded_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerAttrDefUnbounded)


def test_vm_integerattrdefunbounded_constructor_exists():
    assert callable(vM_IntegerAttrDefUnbounded.__init__)


def test_vm_integerattrdefunbounded_constructor_args():
    sig = inspect.signature(vM_IntegerAttrDefUnbounded.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_integerattrdefunbounded_has_value():
    assert hasattr(vM_IntegerAttrDefUnbounded, "value")
    descriptor = None
    for klass in vM_IntegerAttrDefUnbounded.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_integerattrdefbounded_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerAttrDefBounded)


def test_vm_integerattrdefbounded_constructor_exists():
    assert callable(vM_IntegerAttrDefBounded.__init__)


def test_vm_integerattrdefbounded_constructor_args():
    sig = inspect.signature(vM_IntegerAttrDefBounded.__init__)
    params = list(sig.parameters.keys())



def test_vm_integerdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerDefaultDef)


def test_vm_integerdefaultdef_constructor_exists():
    assert callable(vM_IntegerDefaultDef.__init__)


def test_vm_integerdefaultdef_constructor_args():
    sig = inspect.signature(vM_IntegerDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_integerdefaultdef_has_value():
    assert hasattr(vM_IntegerDefaultDef, "value")
    descriptor = None
    for klass in vM_IntegerDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_integer_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Integer_ATT_ID)


def test_vm_integer_att_id_constructor_exists():
    assert callable(vM_Integer_ATT_ID.__init__)


def test_vm_integer_att_id_constructor_args():
    sig = inspect.signature(vM_Integer_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_basicattrvaluation_is_not_abstract():
    assert not inspect.isabstract(vM_BasicAttrValuation)


def test_vm_basicattrvaluation_constructor_exists():
    assert callable(vM_BasicAttrValuation.__init__)


def test_vm_basicattrvaluation_constructor_args():
    sig = inspect.signature(vM_BasicAttrValuation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_basicattrvaluation_has_value():
    assert hasattr(vM_BasicAttrValuation, "value")
    descriptor = None
    for klass in vM_BasicAttrValuation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_stringdefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM_StringDefaultDef)


def test_vm_stringdefaultdef_constructor_exists():
    assert callable(vM_StringDefaultDef.__init__)


def test_vm_stringdefaultdef_constructor_args():
    sig = inspect.signature(vM_StringDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_stringdefaultdef_has_value():
    assert hasattr(vM_StringDefaultDef, "value")
    descriptor = None
    for klass in vM_StringDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_attrdef_is_not_abstract():
    assert not inspect.isabstract(vM_AttrDef)


def test_vm_attrdef_constructor_exists():
    assert callable(vM_AttrDef.__init__)


def test_vm_attrdef_constructor_args():
    sig = inspect.signature(vM_AttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "notDecidable" in params, "Missing parameter 'notDecidable'"
    assert "notTranslatable" in params, "Missing parameter 'notTranslatable'"
    assert "runTime" in params, "Missing parameter 'runTime'"

def test_vm_attrdef_has_notDecidable():
    assert hasattr(vM_AttrDef, "notDecidable")
    descriptor = None
    for klass in vM_AttrDef.__mro__:
        if "notDecidable" in klass.__dict__:
            descriptor = klass.__dict__["notDecidable"]
            break
    assert isinstance(descriptor, property)

def test_vm_attrdef_has_notTranslatable():
    assert hasattr(vM_AttrDef, "notTranslatable")
    descriptor = None
    for klass in vM_AttrDef.__mro__:
        if "notTranslatable" in klass.__dict__:
            descriptor = klass.__dict__["notTranslatable"]
            break
    assert isinstance(descriptor, property)

def test_vm_attrdef_has_runTime():
    assert hasattr(vM_AttrDef, "runTime")
    descriptor = None
    for klass in vM_AttrDef.__mro__:
        if "runTime" in klass.__dict__:
            descriptor = klass.__dict__["runTime"]
            break
    assert isinstance(descriptor, property)



def test_vm_string_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_String_ATT_ID)


def test_vm_string_att_id_constructor_exists():
    assert callable(vM_String_ATT_ID.__init__)


def test_vm_string_att_id_constructor_args():
    sig = inspect.signature(vM_String_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_vm_booldefaultdef_is_not_abstract():
    assert not inspect.isabstract(vM_BoolDefaultDef)


def test_vm_booldefaultdef_constructor_exists():
    assert callable(vM_BoolDefaultDef.__init__)


def test_vm_booldefaultdef_constructor_args():
    sig = inspect.signature(vM_BoolDefaultDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_booldefaultdef_has_value():
    assert hasattr(vM_BoolDefaultDef, "value")
    descriptor = None
    for klass in vM_BoolDefaultDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_boolean_att_id_is_not_abstract():
    assert not inspect.isabstract(vM_Boolean_ATT_ID)


def test_vm_boolean_att_id_constructor_exists():
    assert callable(vM_Boolean_ATT_ID.__init__)


def test_vm_boolean_att_id_constructor_args():
    sig = inspect.signature(vM_Boolean_ATT_ID.__init__)
    params = list(sig.parameters.keys())



def test_featuresgroup_is_not_abstract():
    assert not inspect.isabstract(FeaturesGroup)


def test_featuresgroup_constructor_exists():
    assert callable(FeaturesGroup.__init__)


def test_featuresgroup_constructor_args():
    sig = inspect.signature(FeaturesGroup.__init__)
    params = list(sig.parameters.keys())



def test_vm_orgroup_is_not_abstract():
    assert not inspect.isabstract(vM_Orgroup)


def test_vm_orgroup_constructor_exists():
    assert callable(vM_Orgroup.__init__)


def test_vm_orgroup_constructor_args():
    sig = inspect.signature(vM_Orgroup.__init__)
    params = list(sig.parameters.keys())



def test_vm_cardinalitybased_is_not_abstract():
    assert not inspect.isabstract(vM_CardinalityBased)


def test_vm_cardinalitybased_constructor_exists():
    assert callable(vM_CardinalityBased.__init__)


def test_vm_cardinalitybased_constructor_args():
    sig = inspect.signature(vM_CardinalityBased.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"
    assert "all" in params, "Missing parameter 'all'"

def test_vm_cardinalitybased_has_max():
    assert hasattr(vM_CardinalityBased, "max")
    descriptor = None
    for klass in vM_CardinalityBased.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_vm_cardinalitybased_has_min():
    assert hasattr(vM_CardinalityBased, "min")
    descriptor = None
    for klass in vM_CardinalityBased.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_vm_cardinalitybased_has_all():
    assert hasattr(vM_CardinalityBased, "all")
    descriptor = None
    for klass in vM_CardinalityBased.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_basicattrdef_is_not_abstract():
    assert not inspect.isabstract(BasicAttrDef)


def test_basicattrdef_constructor_exists():
    assert callable(BasicAttrDef.__init__)


def test_basicattrdef_constructor_args():
    sig = inspect.signature(BasicAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_stringattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_StringAttrDef)


def test_vm_stringattrdef_constructor_exists():
    assert callable(vM_StringAttrDef.__init__)


def test_vm_stringattrdef_constructor_args():
    sig = inspect.signature(vM_StringAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_stringattrdef_has_value():
    assert hasattr(vM_StringAttrDef, "value")
    descriptor = None
    for klass in vM_StringAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_realattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_RealAttrDef)


def test_vm_realattrdef_constructor_exists():
    assert callable(vM_RealAttrDef.__init__)


def test_vm_realattrdef_constructor_args():
    sig = inspect.signature(vM_RealAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_integerattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_IntegerAttrDef)


def test_vm_integerattrdef_constructor_exists():
    assert callable(vM_IntegerAttrDef.__init__)


def test_vm_integerattrdef_constructor_args():
    sig = inspect.signature(vM_IntegerAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_xorgroup_is_not_abstract():
    assert not inspect.isabstract(vM_Xorgroup)


def test_vm_xorgroup_constructor_exists():
    assert callable(vM_Xorgroup.__init__)


def test_vm_xorgroup_constructor_args():
    sig = inspect.signature(vM_Xorgroup.__init__)
    params = list(sig.parameters.keys())



def test_vm_booleanattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_BooleanAttrDef)


def test_vm_booleanattrdef_constructor_exists():
    assert callable(vM_BooleanAttrDef.__init__)


def test_vm_booleanattrdef_constructor_args():
    sig = inspect.signature(vM_BooleanAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_booleanattrdef_has_value():
    assert hasattr(vM_BooleanAttrDef, "value")
    descriptor = None
    for klass in vM_BooleanAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_enumattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_EnumAttrDef)


def test_vm_enumattrdef_constructor_exists():
    assert callable(vM_EnumAttrDef.__init__)


def test_vm_enumattrdef_constructor_args():
    sig = inspect.signature(vM_EnumAttrDef.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_enumattrdef_has_value():
    assert hasattr(vM_EnumAttrDef, "value")
    descriptor = None
    for klass in vM_EnumAttrDef.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_basicattrdef_is_not_abstract():
    assert not inspect.isabstract(vM_BasicAttrDef)


def test_vm_basicattrdef_constructor_exists():
    assert callable(vM_BasicAttrDef.__init__)


def test_vm_basicattrdef_constructor_args():
    sig = inspect.signature(vM_BasicAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_realattrdefcomplement_is_not_abstract():
    assert not inspect.isabstract(vM_RealAttrDefComplement)


def test_vm_realattrdefcomplement_constructor_exists():
    assert callable(vM_RealAttrDefComplement.__init__)


def test_vm_realattrdefcomplement_constructor_args():
    sig = inspect.signature(vM_RealAttrDefComplement.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "max" in params, "Missing parameter 'max'"

def test_vm_realattrdefcomplement_has_min():
    assert hasattr(vM_RealAttrDefComplement, "min")
    descriptor = None
    for klass in vM_RealAttrDefComplement.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_vm_realattrdefcomplement_has_max():
    assert hasattr(vM_RealAttrDefComplement, "max")
    descriptor = None
    for klass in vM_RealAttrDefComplement.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)



def test_realattrdef_is_not_abstract():
    assert not inspect.isabstract(RealAttrDef)


def test_realattrdef_constructor_exists():
    assert callable(RealAttrDef.__init__)


def test_realattrdef_constructor_args():
    sig = inspect.signature(RealAttrDef.__init__)
    params = list(sig.parameters.keys())



def test_vm_realattrdefunbounded_is_not_abstract():
    assert not inspect.isabstract(vM_RealAttrDefUnbounded)


def test_vm_realattrdefunbounded_constructor_exists():
    assert callable(vM_RealAttrDefUnbounded.__init__)


def test_vm_realattrdefunbounded_constructor_args():
    sig = inspect.signature(vM_RealAttrDefUnbounded.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_vm_realattrdefunbounded_has_value():
    assert hasattr(vM_RealAttrDefUnbounded, "value")
    descriptor = None
    for klass in vM_RealAttrDefUnbounded.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_vm_realattrdefbounded_is_not_abstract():
    assert not inspect.isabstract(vM_RealAttrDefBounded)


def test_vm_realattrdefbounded_constructor_exists():
    assert callable(vM_RealAttrDefBounded.__init__)


def test_vm_realattrdefbounded_constructor_args():
    sig = inspect.signature(vM_RealAttrDefBounded.__init__)
    params = list(sig.parameters.keys())



def test_vm_email_is_not_abstract():
    assert not inspect.isabstract(vM_Email)


def test_vm_email_constructor_exists():
    assert callable(vM_Email.__init__)


def test_vm_email_constructor_args():
    sig = inspect.signature(vM_Email.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"
    assert "username" in params, "Missing parameter 'username'"

def test_vm_email_has_domain():
    assert hasattr(vM_Email, "domain")
    descriptor = None
    for klass in vM_Email.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

def test_vm_email_has_username():
    assert hasattr(vM_Email, "username")
    descriptor = None
    for klass in vM_Email.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_vm_version_is_not_abstract():
    assert not inspect.isabstract(vM_Version)


def test_vm_version_constructor_exists():
    assert callable(vM_Version.__init__)


def test_vm_version_constructor_args():
    sig = inspect.signature(vM_Version.__init__)
    params = list(sig.parameters.keys())
    assert "tail" in params, "Missing parameter 'tail'"
    assert "main" in params, "Missing parameter 'main'"

def test_vm_version_has_tail():
    assert hasattr(vM_Version, "tail")
    descriptor = None
    for klass in vM_Version.__mro__:
        if "tail" in klass.__dict__:
            descriptor = klass.__dict__["tail"]
            break
    assert isinstance(descriptor, property)

def test_vm_version_has_main():
    assert hasattr(vM_Version, "main")
    descriptor = None
    for klass in vM_Version.__mro__:
        if "main" in klass.__dict__:
            descriptor = klass.__dict__["main"]
            break
    assert isinstance(descriptor, property)



def test_vmblock_is_not_abstract():
    assert not inspect.isabstract(VmBlock)


def test_vmblock_constructor_exists():
    assert callable(VmBlock.__init__)


def test_vmblock_constructor_args():
    sig = inspect.signature(VmBlock.__init__)
    params = list(sig.parameters.keys())



def test_vm_attributes_is_not_abstract():
    assert not inspect.isabstract(vM_Attributes)


def test_vm_attributes_constructor_exists():
    assert callable(vM_Attributes.__init__)


def test_vm_attributes_constructor_args():
    sig = inspect.signature(vM_Attributes.__init__)
    params = list(sig.parameters.keys())



def test_vm_metadatadeclaration_is_not_abstract():
    assert not inspect.isabstract(vM_MetaDataDeclaration)


def test_vm_metadatadeclaration_constructor_exists():
    assert callable(vM_MetaDataDeclaration.__init__)


def test_vm_metadatadeclaration_constructor_args():
    sig = inspect.signature(vM_MetaDataDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "description" in params, "Missing parameter 'description'"
    assert "publication" in params, "Missing parameter 'publication'"

def test_vm_metadatadeclaration_has_author():
    assert hasattr(vM_MetaDataDeclaration, "author")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_vm_metadatadeclaration_has_date():
    assert hasattr(vM_MetaDataDeclaration, "date")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_vm_metadatadeclaration_has_name():
    assert hasattr(vM_MetaDataDeclaration, "name")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm_metadatadeclaration_has_organization():
    assert hasattr(vM_MetaDataDeclaration, "organization")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_vm_metadatadeclaration_has_description():
    assert hasattr(vM_MetaDataDeclaration, "description")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_vm_metadatadeclaration_has_publication():
    assert hasattr(vM_MetaDataDeclaration, "publication")
    descriptor = None
    for klass in vM_MetaDataDeclaration.__mro__:
        if "publication" in klass.__dict__:
            descriptor = klass.__dict__["publication"]
            break
    assert isinstance(descriptor, property)



def test_vm_importdeclaration_is_not_abstract():
    assert not inspect.isabstract(vM_ImportDeclaration)


def test_vm_importdeclaration_constructor_exists():
    assert callable(vM_ImportDeclaration.__init__)


def test_vm_importdeclaration_constructor_args():
    sig = inspect.signature(vM_ImportDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_vm_importdeclaration_has_importedNamespace():
    assert hasattr(vM_ImportDeclaration, "importedNamespace")
    descriptor = None
    for klass in vM_ImportDeclaration.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_vm_constraints_is_not_abstract():
    assert not inspect.isabstract(vM_Constraints)


def test_vm_constraints_constructor_exists():
    assert callable(vM_Constraints.__init__)


def test_vm_constraints_constructor_args():
    sig = inspect.signature(vM_Constraints.__init__)
    params = list(sig.parameters.keys())



def test_vm_descriptions_is_not_abstract():
    assert not inspect.isabstract(vM_Descriptions)


def test_vm_descriptions_constructor_exists():
    assert callable(vM_Descriptions.__init__)


def test_vm_descriptions_constructor_args():
    sig = inspect.signature(vM_Descriptions.__init__)
    params = list(sig.parameters.keys())



def test_vm_configurations_is_not_abstract():
    assert not inspect.isabstract(vM_Configurations)


def test_vm_configurations_constructor_exists():
    assert callable(vM_Configurations.__init__)


def test_vm_configurations_constructor_args():
    sig = inspect.signature(vM_Configurations.__init__)
    params = list(sig.parameters.keys())



def test_vm_objectives_is_not_abstract():
    assert not inspect.isabstract(vM_Objectives)


def test_vm_objectives_constructor_exists():
    assert callable(vM_Objectives.__init__)


def test_vm_objectives_constructor_args():
    sig = inspect.signature(vM_Objectives.__init__)
    params = list(sig.parameters.keys())



def test_vm_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(vM_PackageDeclaration)


def test_vm_packagedeclaration_constructor_exists():
    assert callable(vM_PackageDeclaration.__init__)


def test_vm_packagedeclaration_constructor_args():
    sig = inspect.signature(vM_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_vm_packagedeclaration_has_name():
    assert hasattr(vM_PackageDeclaration, "name")
    descriptor = None
    for klass in vM_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_vm_featuredefinition_is_not_abstract():
    assert not inspect.isabstract(vM_FeatureDefinition)


def test_vm_featuredefinition_constructor_exists():
    assert callable(vM_FeatureDefinition.__init__)


def test_vm_featuredefinition_constructor_args():
    sig = inspect.signature(vM_FeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_featuredefinition_is_not_abstract():
    assert not inspect.isabstract(FeatureDefinition)


def test_featuredefinition_constructor_exists():
    assert callable(FeatureDefinition.__init__)


def test_featuredefinition_constructor_args():
    sig = inspect.signature(FeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_vm_feature_is_not_abstract():
    assert not inspect.isabstract(vM_Feature)


def test_vm_feature_constructor_exists():
    assert callable(vM_Feature.__init__)


def test_vm_feature_constructor_args():
    sig = inspect.signature(vM_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "notTranslatable" in params, "Missing parameter 'notTranslatable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "min" in params, "Missing parameter 'min'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "max" in params, "Missing parameter 'max'"
    assert "runTime" in params, "Missing parameter 'runTime'"
    assert "notDecidable" in params, "Missing parameter 'notDecidable'"

def test_vm_feature_has_notTranslatable():
    assert hasattr(vM_Feature, "notTranslatable")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "notTranslatable" in klass.__dict__:
            descriptor = klass.__dict__["notTranslatable"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_name():
    assert hasattr(vM_Feature, "name")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_min():
    assert hasattr(vM_Feature, "min")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_optional():
    assert hasattr(vM_Feature, "optional")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_max():
    assert hasattr(vM_Feature, "max")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_runTime():
    assert hasattr(vM_Feature, "runTime")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "runTime" in klass.__dict__:
            descriptor = klass.__dict__["runTime"]
            break
    assert isinstance(descriptor, property)

def test_vm_feature_has_notDecidable():
    assert hasattr(vM_Feature, "notDecidable")
    descriptor = None
    for klass in vM_Feature.__mro__:
        if "notDecidable" in klass.__dict__:
            descriptor = klass.__dict__["notDecidable"]
            break
    assert isinstance(descriptor, property)



def test_vm_featuresgroup_is_not_abstract():
    assert not inspect.isabstract(vM_FeaturesGroup)


def test_vm_featuresgroup_constructor_exists():
    assert callable(vM_FeaturesGroup.__init__)


def test_vm_featuresgroup_constructor_args():
    sig = inspect.signature(vM_FeaturesGroup.__init__)
    params = list(sig.parameters.keys())



def test_vm_featurehierarchy_is_not_abstract():
    assert not inspect.isabstract(vM_FeatureHierarchy)


def test_vm_featurehierarchy_constructor_exists():
    assert callable(vM_FeatureHierarchy.__init__)


def test_vm_featurehierarchy_constructor_args():
    sig = inspect.signature(vM_FeatureHierarchy.__init__)
    params = list(sig.parameters.keys())



def test_vm_relationships_is_not_abstract():
    assert not inspect.isabstract(vM_Relationships)


def test_vm_relationships_constructor_exists():
    assert callable(vM_Relationships.__init__)


def test_vm_relationships_constructor_args():
    sig = inspect.signature(vM_Relationships.__init__)
    params = list(sig.parameters.keys())



def test_vm_vmblock_is_not_abstract():
    assert not inspect.isabstract(vM_VmBlock)


def test_vm_vmblock_constructor_exists():
    assert callable(vM_VmBlock.__init__)


def test_vm_vmblock_constructor_args():
    sig = inspect.signature(vM_VmBlock.__init__)
    params = list(sig.parameters.keys())



def test_vm_model_is_not_abstract():
    assert not inspect.isabstract(vM_Model)


def test_vm_model_constructor_exists():
    assert callable(vM_Model.__init__)


def test_vm_model_constructor_args():
    sig = inspect.signature(vM_Model.__init__)
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
Abstract_ATT_ID_strategy = st.builds(
    Abstract_ATT_ID,
)
vM_PairFeatureReal_strategy = st.builds(
    vM_PairFeatureReal,
    value=
        safe_text
)
vM_PairFeatureInteger_strategy = st.builds(
    vM_PairFeatureInteger,
    value=
        safe_text
)
TableBasedValuationByAttribute_strategy = st.builds(
    TableBasedValuationByAttribute,
)
vM_TableBasedValuationByAttributeForReal_strategy = st.builds(
    vM_TableBasedValuationByAttributeForReal,
)
vM_TableBasedValuationByAttributeForInteger_strategy = st.builds(
    vM_TableBasedValuationByAttributeForInteger,
)
vM_PairAttributeValue_strategy = st.builds(
    vM_PairAttributeValue,
    value=
        safe_text
)
vM_TableBasedValuationByFeatureAndClone_strategy = st.builds(
    vM_TableBasedValuationByFeatureAndClone,
    name=
        safe_text
)
vM_TableBasedValuationByAttribute_strategy = st.builds(
    vM_TableBasedValuationByAttribute,
)
vM_TableBasedValuationByFeature_strategy = st.builds(
    vM_TableBasedValuationByFeature,
)
BasicAttrValuation_strategy = st.builds(
    BasicAttrValuation,
)
vM_IntegerAttrValuation_strategy = st.builds(
    vM_IntegerAttrValuation,
)
vM_StringAttrValuation_strategy = st.builds(
    vM_StringAttrValuation,
)
vM_BooleanAttrValuation_strategy = st.builds(
    vM_BooleanAttrValuation,
)
vM_RealAttrValuation_strategy = st.builds(
    vM_RealAttrValuation,
)
ExtendedValuation_strategy = st.builds(
    ExtendedValuation,
)
vM_AdvancedAttrValuation_strategy = st.builds(
    vM_AdvancedAttrValuation,
)
vM_Configuration_strategy = st.builds(
    vM_Configuration,
    name=
        safe_text
)
vM_ObjectiveExpression_strategy = st.builds(
    vM_ObjectiveExpression,
    op=
        safe_text
)
vM_Objective_strategy = st.builds(
    vM_Objective,
    name=
        safe_text,
    op=
        safe_text
)
vM_NumericExpression_List_strategy = st.builds(
    vM_NumericExpression_List,
)
vM_BooleanExpression_List_strategy = st.builds(
    vM_BooleanExpression_List,
)
vM_ExtendedValuation_strategy = st.builds(
    vM_ExtendedValuation,
)
vM_BooleanValuation_strategy = st.builds(
    vM_BooleanValuation,
    notSelected=
        st.booleans()
)
vM_AttHead_strategy = st.builds(
    vM_AttHead,
    forAllFeatures=
        st.booleans()
)
Expression_strategy = st.builds(
    Expression,
)
vM_StringExpression_strategy = st.builds(
    vM_StringExpression,
    value=
        safe_text
)
vM_NumericExpression_strategy = st.builds(
    vM_NumericExpression,
    op=
        safe_text,
    value=
        safe_text
)
vM_PrimitiveExpression_strategy = st.builds(
    vM_PrimitiveExpression,
)
vM_BrackedExpression_strategy = st.builds(
    vM_BrackedExpression,
)
vM_SpecialExpression_strategy = st.builds(
    vM_SpecialExpression,
    op=
        safe_text
)
ComplexExpression_strategy = st.builds(
    ComplexExpression,
)
vM_Minus_strategy = st.builds(
    vM_Minus,
)
vM_Equality_strategy = st.builds(
    vM_Equality,
)
vM_If_strategy = st.builds(
    vM_If,
)
vM_Requires_strategy = st.builds(
    vM_Requires,
)
vM_Inequality_strategy = st.builds(
    vM_Inequality,
)
vM_Or_strategy = st.builds(
    vM_Or,
)
vM_Multiplication_strategy = st.builds(
    vM_Multiplication,
)
vM_Lessequal_strategy = st.builds(
    vM_Lessequal,
)
vM_Less_strategy = st.builds(
    vM_Less,
)
vM_LeftImplication_strategy = st.builds(
    vM_LeftImplication,
)
vM_Greater_strategy = st.builds(
    vM_Greater,
)
vM_RightImplication_strategy = st.builds(
    vM_RightImplication,
)
vM_Greaterequal_strategy = st.builds(
    vM_Greaterequal,
)
vM_And_strategy = st.builds(
    vM_And,
)
vM_Plus_strategy = st.builds(
    vM_Plus,
)
vM_Excludes_strategy = st.builds(
    vM_Excludes,
)
vM_Division_strategy = st.builds(
    vM_Division,
)
vM_BiImplication_strategy = st.builds(
    vM_BiImplication,
)
vM_Expression_strategy = st.builds(
    vM_Expression,
)
vM_ComplexExpression_strategy = st.builds(
    vM_ComplexExpression,
)
vM_Constraint_strategy = st.builds(
    vM_Constraint,
    name=
        safe_text,
    not_=
        st.booleans()
)
vM_Abstract_ATT_ID_strategy = st.builds(
    vM_Abstract_ATT_ID,
    name=
        safe_text
)
vM_BooleanExpression_strategy = st.builds(
    vM_BooleanExpression,
    op=
        safe_text,
    value=
        safe_text
)
vM_AttributeDescription_strategy = st.builds(
    vM_AttributeDescription,
    description=
        safe_text
)
vM_FeatureDescription_strategy = st.builds(
    vM_FeatureDescription,
    description=
        safe_text
)
vM_Enum_Real_ATT_ID_strategy = st.builds(
    vM_Enum_Real_ATT_ID,
)
vM_Enum_Integer_ATT_ID_strategy = st.builds(
    vM_Enum_Integer_ATT_ID,
)
vM_Enum_String_ATT_ID_strategy = st.builds(
    vM_Enum_String_ATT_ID,
)
EnumAttrDef_strategy = st.builds(
    EnumAttrDef,
)
vM_EnumRealDef_strategy = st.builds(
    vM_EnumRealDef,
)
vM_EnumIntegerDef_strategy = st.builds(
    vM_EnumIntegerDef,
)
vM_EnumStringDef_strategy = st.builds(
    vM_EnumStringDef,
)
vM_RealDeltaDef_strategy = st.builds(
    vM_RealDeltaDef,
    value=
        safe_text
)
vM_RealDefaultDef_strategy = st.builds(
    vM_RealDefaultDef,
    value=
        safe_text
)
vM_Real_ATT_ID_strategy = st.builds(
    vM_Real_ATT_ID,
)
vM_IntegerDeltaDef_strategy = st.builds(
    vM_IntegerDeltaDef,
    value=
        st.integers()
)
vM_IntegerAttrDefComplement_strategy = st.builds(
    vM_IntegerAttrDefComplement,
    max=
        safe_text,
    min=
        safe_text
)
IntegerAttrDef_strategy = st.builds(
    IntegerAttrDef,
)
vM_IntegerAttrDefUnbounded_strategy = st.builds(
    vM_IntegerAttrDefUnbounded,
    value=
        safe_text
)
vM_IntegerAttrDefBounded_strategy = st.builds(
    vM_IntegerAttrDefBounded,
)
vM_IntegerDefaultDef_strategy = st.builds(
    vM_IntegerDefaultDef,
    value=
        st.integers()
)
vM_Integer_ATT_ID_strategy = st.builds(
    vM_Integer_ATT_ID,
)
vM_BasicAttrValuation_strategy = st.builds(
    vM_BasicAttrValuation,
    value=
        safe_text
)
vM_StringDefaultDef_strategy = st.builds(
    vM_StringDefaultDef,
    value=
        safe_text
)
vM_AttrDef_strategy = st.builds(
    vM_AttrDef,
    notDecidable=
        st.booleans(),
    notTranslatable=
        st.booleans(),
    runTime=
        st.booleans()
)
vM_String_ATT_ID_strategy = st.builds(
    vM_String_ATT_ID,
)
vM_BoolDefaultDef_strategy = st.builds(
    vM_BoolDefaultDef,
    value=
        safe_text
)
vM_Boolean_ATT_ID_strategy = st.builds(
    vM_Boolean_ATT_ID,
)
FeaturesGroup_strategy = st.builds(
    FeaturesGroup,
)
vM_Orgroup_strategy = st.builds(
    vM_Orgroup,
)
vM_CardinalityBased_strategy = st.builds(
    vM_CardinalityBased,
    max=
        safe_text,
    min=
        safe_text,
    all=
        st.booleans()
)
BasicAttrDef_strategy = st.builds(
    BasicAttrDef,
)
vM_StringAttrDef_strategy = st.builds(
    vM_StringAttrDef,
    value=
        safe_text
)
vM_RealAttrDef_strategy = st.builds(
    vM_RealAttrDef,
)
vM_IntegerAttrDef_strategy = st.builds(
    vM_IntegerAttrDef,
)
vM_Xorgroup_strategy = st.builds(
    vM_Xorgroup,
)
vM_BooleanAttrDef_strategy = st.builds(
    vM_BooleanAttrDef,
    value=
        safe_text
)
vM_EnumAttrDef_strategy = st.builds(
    vM_EnumAttrDef,
    value=
        safe_text
)
vM_BasicAttrDef_strategy = st.builds(
    vM_BasicAttrDef,
)
vM_RealAttrDefComplement_strategy = st.builds(
    vM_RealAttrDefComplement,
    min=
        safe_text,
    max=
        safe_text
)
RealAttrDef_strategy = st.builds(
    RealAttrDef,
)
vM_RealAttrDefUnbounded_strategy = st.builds(
    vM_RealAttrDefUnbounded,
    value=
        safe_text
)
vM_RealAttrDefBounded_strategy = st.builds(
    vM_RealAttrDefBounded,
)
vM_Email_strategy = st.builds(
    vM_Email,
    domain=
        safe_text,
    username=
        safe_text
)
vM_Version_strategy = st.builds(
    vM_Version,
    tail=
        st.integers(),
    main=
        st.integers()
)
VmBlock_strategy = st.builds(
    VmBlock,
)
vM_Attributes_strategy = st.builds(
    vM_Attributes,
)
vM_MetaDataDeclaration_strategy = st.builds(
    vM_MetaDataDeclaration,
    author=
        safe_text,
    date=
        safe_text,
    name=
        safe_text,
    organization=
        safe_text,
    description=
        safe_text,
    publication=
        safe_text
)
vM_ImportDeclaration_strategy = st.builds(
    vM_ImportDeclaration,
    importedNamespace=
        safe_text
)
vM_Constraints_strategy = st.builds(
    vM_Constraints,
)
vM_Descriptions_strategy = st.builds(
    vM_Descriptions,
)
vM_Configurations_strategy = st.builds(
    vM_Configurations,
)
vM_Objectives_strategy = st.builds(
    vM_Objectives,
)
vM_PackageDeclaration_strategy = st.builds(
    vM_PackageDeclaration,
    name=
        safe_text
)
vM_FeatureDefinition_strategy = st.builds(
    vM_FeatureDefinition,
)
FeatureDefinition_strategy = st.builds(
    FeatureDefinition,
)
vM_Feature_strategy = st.builds(
    vM_Feature,
    notTranslatable=
        st.booleans(),
    name=
        safe_text,
    min=
        safe_text,
    optional=
        st.booleans(),
    max=
        safe_text,
    runTime=
        st.booleans(),
    notDecidable=
        st.booleans()
)
vM_FeaturesGroup_strategy = st.builds(
    vM_FeaturesGroup,
)
vM_FeatureHierarchy_strategy = st.builds(
    vM_FeatureHierarchy,
)
vM_Relationships_strategy = st.builds(
    vM_Relationships,
)
vM_VmBlock_strategy = st.builds(
    vM_VmBlock,
)
vM_Model_strategy = st.builds(
    vM_Model,
)

@given(instance=Abstract_ATT_ID_strategy)
@settings(max_examples=50)
def test_abstract_att_id_instantiation(instance):
    assert isinstance(instance, Abstract_ATT_ID)

@given(instance=vM_PairFeatureReal_strategy)
@settings(max_examples=50)
def test_vm_pairfeaturereal_instantiation(instance):
    assert isinstance(instance, vM_PairFeatureReal)



@given(instance=vM_PairFeatureReal_strategy)
def test_vm_pairfeaturereal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_PairFeatureInteger_strategy)
@settings(max_examples=50)
def test_vm_pairfeatureinteger_instantiation(instance):
    assert isinstance(instance, vM_PairFeatureInteger)



@given(instance=vM_PairFeatureInteger_strategy)
def test_vm_pairfeatureinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=TableBasedValuationByAttribute_strategy)
@settings(max_examples=50)
def test_tablebasedvaluationbyattribute_instantiation(instance):
    assert isinstance(instance, TableBasedValuationByAttribute)

@given(instance=vM_TableBasedValuationByAttributeForReal_strategy)
@settings(max_examples=50)
def test_vm_tablebasedvaluationbyattributeforreal_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttributeForReal)

@given(instance=vM_TableBasedValuationByAttributeForInteger_strategy)
@settings(max_examples=50)
def test_vm_tablebasedvaluationbyattributeforinteger_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttributeForInteger)

@given(instance=vM_PairAttributeValue_strategy)
@settings(max_examples=50)
def test_vm_pairattributevalue_instantiation(instance):
    assert isinstance(instance, vM_PairAttributeValue)



@given(instance=vM_PairAttributeValue_strategy)
def test_vm_pairattributevalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_TableBasedValuationByFeatureAndClone_strategy)
@settings(max_examples=50)
def test_vm_tablebasedvaluationbyfeatureandclone_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByFeatureAndClone)



@given(instance=vM_TableBasedValuationByFeatureAndClone_strategy)
def test_vm_tablebasedvaluationbyfeatureandclone_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM_TableBasedValuationByAttribute_strategy)
@settings(max_examples=50)
def test_vm_tablebasedvaluationbyattribute_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByAttribute)

@given(instance=vM_TableBasedValuationByFeature_strategy)
@settings(max_examples=50)
def test_vm_tablebasedvaluationbyfeature_instantiation(instance):
    assert isinstance(instance, vM_TableBasedValuationByFeature)

@given(instance=BasicAttrValuation_strategy)
@settings(max_examples=50)
def test_basicattrvaluation_instantiation(instance):
    assert isinstance(instance, BasicAttrValuation)

@given(instance=vM_IntegerAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_integerattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrValuation)

@given(instance=vM_StringAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_stringattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_StringAttrValuation)

@given(instance=vM_BooleanAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_booleanattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_BooleanAttrValuation)

@given(instance=vM_RealAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_realattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_RealAttrValuation)

@given(instance=ExtendedValuation_strategy)
@settings(max_examples=50)
def test_extendedvaluation_instantiation(instance):
    assert isinstance(instance, ExtendedValuation)

@given(instance=vM_AdvancedAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_advancedattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_AdvancedAttrValuation)

@given(instance=vM_Configuration_strategy)
@settings(max_examples=50)
def test_vm_configuration_instantiation(instance):
    assert isinstance(instance, vM_Configuration)



@given(instance=vM_Configuration_strategy)
def test_vm_configuration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM_ObjectiveExpression_strategy)
@settings(max_examples=50)
def test_vm_objectiveexpression_instantiation(instance):
    assert isinstance(instance, vM_ObjectiveExpression)



@given(instance=vM_ObjectiveExpression_strategy)
def test_vm_objectiveexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM_Objective_strategy)
@settings(max_examples=50)
def test_vm_objective_instantiation(instance):
    assert isinstance(instance, vM_Objective)



@given(instance=vM_Objective_strategy)
def test_vm_objective_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vM_Objective_strategy)
def test_vm_objective_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=vM_NumericExpression_List_strategy)
@settings(max_examples=50)
def test_vm_numericexpression_list_instantiation(instance):
    assert isinstance(instance, vM_NumericExpression_List)

@given(instance=vM_BooleanExpression_List_strategy)
@settings(max_examples=50)
def test_vm_booleanexpression_list_instantiation(instance):
    assert isinstance(instance, vM_BooleanExpression_List)

@given(instance=vM_ExtendedValuation_strategy)
@settings(max_examples=50)
def test_vm_extendedvaluation_instantiation(instance):
    assert isinstance(instance, vM_ExtendedValuation)

@given(instance=vM_BooleanValuation_strategy)
@settings(max_examples=50)
def test_vm_booleanvaluation_instantiation(instance):
    assert isinstance(instance, vM_BooleanValuation)



@given(instance=vM_BooleanValuation_strategy)
def test_vm_booleanvaluation_notSelected_setter(instance):
    original = instance.notSelected
    instance.notSelected = original
    assert instance.notSelected == original

@given(instance=vM_AttHead_strategy)
@settings(max_examples=50)
def test_vm_atthead_instantiation(instance):
    assert isinstance(instance, vM_AttHead)



@given(instance=vM_AttHead_strategy)
def test_vm_atthead_forAllFeatures_setter(instance):
    original = instance.forAllFeatures
    instance.forAllFeatures = original
    assert instance.forAllFeatures == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=vM_StringExpression_strategy)
@settings(max_examples=50)
def test_vm_stringexpression_instantiation(instance):
    assert isinstance(instance, vM_StringExpression)



@given(instance=vM_StringExpression_strategy)
def test_vm_stringexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_NumericExpression_strategy)
@settings(max_examples=50)
def test_vm_numericexpression_instantiation(instance):
    assert isinstance(instance, vM_NumericExpression)



@given(instance=vM_NumericExpression_strategy)
def test_vm_numericexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=vM_NumericExpression_strategy)
def test_vm_numericexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_vm_primitiveexpression_instantiation(instance):
    assert isinstance(instance, vM_PrimitiveExpression)

@given(instance=vM_BrackedExpression_strategy)
@settings(max_examples=50)
def test_vm_brackedexpression_instantiation(instance):
    assert isinstance(instance, vM_BrackedExpression)

@given(instance=vM_SpecialExpression_strategy)
@settings(max_examples=50)
def test_vm_specialexpression_instantiation(instance):
    assert isinstance(instance, vM_SpecialExpression)



@given(instance=vM_SpecialExpression_strategy)
def test_vm_specialexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ComplexExpression_strategy)
@settings(max_examples=50)
def test_complexexpression_instantiation(instance):
    assert isinstance(instance, ComplexExpression)

@given(instance=vM_Minus_strategy)
@settings(max_examples=50)
def test_vm_minus_instantiation(instance):
    assert isinstance(instance, vM_Minus)

@given(instance=vM_Equality_strategy)
@settings(max_examples=50)
def test_vm_equality_instantiation(instance):
    assert isinstance(instance, vM_Equality)

@given(instance=vM_If_strategy)
@settings(max_examples=50)
def test_vm_if_instantiation(instance):
    assert isinstance(instance, vM_If)

@given(instance=vM_Requires_strategy)
@settings(max_examples=50)
def test_vm_requires_instantiation(instance):
    assert isinstance(instance, vM_Requires)

@given(instance=vM_Inequality_strategy)
@settings(max_examples=50)
def test_vm_inequality_instantiation(instance):
    assert isinstance(instance, vM_Inequality)

@given(instance=vM_Or_strategy)
@settings(max_examples=50)
def test_vm_or_instantiation(instance):
    assert isinstance(instance, vM_Or)

@given(instance=vM_Multiplication_strategy)
@settings(max_examples=50)
def test_vm_multiplication_instantiation(instance):
    assert isinstance(instance, vM_Multiplication)

@given(instance=vM_Lessequal_strategy)
@settings(max_examples=50)
def test_vm_lessequal_instantiation(instance):
    assert isinstance(instance, vM_Lessequal)

@given(instance=vM_Less_strategy)
@settings(max_examples=50)
def test_vm_less_instantiation(instance):
    assert isinstance(instance, vM_Less)

@given(instance=vM_LeftImplication_strategy)
@settings(max_examples=50)
def test_vm_leftimplication_instantiation(instance):
    assert isinstance(instance, vM_LeftImplication)

@given(instance=vM_Greater_strategy)
@settings(max_examples=50)
def test_vm_greater_instantiation(instance):
    assert isinstance(instance, vM_Greater)

@given(instance=vM_RightImplication_strategy)
@settings(max_examples=50)
def test_vm_rightimplication_instantiation(instance):
    assert isinstance(instance, vM_RightImplication)

@given(instance=vM_Greaterequal_strategy)
@settings(max_examples=50)
def test_vm_greaterequal_instantiation(instance):
    assert isinstance(instance, vM_Greaterequal)

@given(instance=vM_And_strategy)
@settings(max_examples=50)
def test_vm_and_instantiation(instance):
    assert isinstance(instance, vM_And)

@given(instance=vM_Plus_strategy)
@settings(max_examples=50)
def test_vm_plus_instantiation(instance):
    assert isinstance(instance, vM_Plus)

@given(instance=vM_Excludes_strategy)
@settings(max_examples=50)
def test_vm_excludes_instantiation(instance):
    assert isinstance(instance, vM_Excludes)

@given(instance=vM_Division_strategy)
@settings(max_examples=50)
def test_vm_division_instantiation(instance):
    assert isinstance(instance, vM_Division)

@given(instance=vM_BiImplication_strategy)
@settings(max_examples=50)
def test_vm_biimplication_instantiation(instance):
    assert isinstance(instance, vM_BiImplication)

@given(instance=vM_Expression_strategy)
@settings(max_examples=50)
def test_vm_expression_instantiation(instance):
    assert isinstance(instance, vM_Expression)

@given(instance=vM_ComplexExpression_strategy)
@settings(max_examples=50)
def test_vm_complexexpression_instantiation(instance):
    assert isinstance(instance, vM_ComplexExpression)

@given(instance=vM_Constraint_strategy)
@settings(max_examples=50)
def test_vm_constraint_instantiation(instance):
    assert isinstance(instance, vM_Constraint)



@given(instance=vM_Constraint_strategy)
def test_vm_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vM_Constraint_strategy)
def test_vm_constraint_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=vM_Abstract_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_abstract_att_id_instantiation(instance):
    assert isinstance(instance, vM_Abstract_ATT_ID)



@given(instance=vM_Abstract_ATT_ID_strategy)
def test_vm_abstract_att_id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM_BooleanExpression_strategy)
@settings(max_examples=50)
def test_vm_booleanexpression_instantiation(instance):
    assert isinstance(instance, vM_BooleanExpression)



@given(instance=vM_BooleanExpression_strategy)
def test_vm_booleanexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=vM_BooleanExpression_strategy)
def test_vm_booleanexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_AttributeDescription_strategy)
@settings(max_examples=50)
def test_vm_attributedescription_instantiation(instance):
    assert isinstance(instance, vM_AttributeDescription)



@given(instance=vM_AttributeDescription_strategy)
def test_vm_attributedescription_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=vM_FeatureDescription_strategy)
@settings(max_examples=50)
def test_vm_featuredescription_instantiation(instance):
    assert isinstance(instance, vM_FeatureDescription)



@given(instance=vM_FeatureDescription_strategy)
def test_vm_featuredescription_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=vM_Enum_Real_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_enum_real_att_id_instantiation(instance):
    assert isinstance(instance, vM_Enum_Real_ATT_ID)

@given(instance=vM_Enum_Integer_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_enum_integer_att_id_instantiation(instance):
    assert isinstance(instance, vM_Enum_Integer_ATT_ID)

@given(instance=vM_Enum_String_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_enum_string_att_id_instantiation(instance):
    assert isinstance(instance, vM_Enum_String_ATT_ID)

@given(instance=EnumAttrDef_strategy)
@settings(max_examples=50)
def test_enumattrdef_instantiation(instance):
    assert isinstance(instance, EnumAttrDef)

@given(instance=vM_EnumRealDef_strategy)
@settings(max_examples=50)
def test_vm_enumrealdef_instantiation(instance):
    assert isinstance(instance, vM_EnumRealDef)

@given(instance=vM_EnumIntegerDef_strategy)
@settings(max_examples=50)
def test_vm_enumintegerdef_instantiation(instance):
    assert isinstance(instance, vM_EnumIntegerDef)

@given(instance=vM_EnumStringDef_strategy)
@settings(max_examples=50)
def test_vm_enumstringdef_instantiation(instance):
    assert isinstance(instance, vM_EnumStringDef)

@given(instance=vM_RealDeltaDef_strategy)
@settings(max_examples=50)
def test_vm_realdeltadef_instantiation(instance):
    assert isinstance(instance, vM_RealDeltaDef)



@given(instance=vM_RealDeltaDef_strategy)
def test_vm_realdeltadef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_RealDefaultDef_strategy)
@settings(max_examples=50)
def test_vm_realdefaultdef_instantiation(instance):
    assert isinstance(instance, vM_RealDefaultDef)



@given(instance=vM_RealDefaultDef_strategy)
def test_vm_realdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_Real_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_real_att_id_instantiation(instance):
    assert isinstance(instance, vM_Real_ATT_ID)

@given(instance=vM_IntegerDeltaDef_strategy)
@settings(max_examples=50)
def test_vm_integerdeltadef_instantiation(instance):
    assert isinstance(instance, vM_IntegerDeltaDef)



@given(instance=vM_IntegerDeltaDef_strategy)
def test_vm_integerdeltadef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_IntegerAttrDefComplement_strategy)
@settings(max_examples=50)
def test_vm_integerattrdefcomplement_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefComplement)



@given(instance=vM_IntegerAttrDefComplement_strategy)
def test_vm_integerattrdefcomplement_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=vM_IntegerAttrDefComplement_strategy)
def test_vm_integerattrdefcomplement_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=IntegerAttrDef_strategy)
@settings(max_examples=50)
def test_integerattrdef_instantiation(instance):
    assert isinstance(instance, IntegerAttrDef)

@given(instance=vM_IntegerAttrDefUnbounded_strategy)
@settings(max_examples=50)
def test_vm_integerattrdefunbounded_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefUnbounded)



@given(instance=vM_IntegerAttrDefUnbounded_strategy)
def test_vm_integerattrdefunbounded_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_IntegerAttrDefBounded_strategy)
@settings(max_examples=50)
def test_vm_integerattrdefbounded_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDefBounded)

@given(instance=vM_IntegerDefaultDef_strategy)
@settings(max_examples=50)
def test_vm_integerdefaultdef_instantiation(instance):
    assert isinstance(instance, vM_IntegerDefaultDef)



@given(instance=vM_IntegerDefaultDef_strategy)
def test_vm_integerdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_Integer_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_integer_att_id_instantiation(instance):
    assert isinstance(instance, vM_Integer_ATT_ID)

@given(instance=vM_BasicAttrValuation_strategy)
@settings(max_examples=50)
def test_vm_basicattrvaluation_instantiation(instance):
    assert isinstance(instance, vM_BasicAttrValuation)



@given(instance=vM_BasicAttrValuation_strategy)
def test_vm_basicattrvaluation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_StringDefaultDef_strategy)
@settings(max_examples=50)
def test_vm_stringdefaultdef_instantiation(instance):
    assert isinstance(instance, vM_StringDefaultDef)



@given(instance=vM_StringDefaultDef_strategy)
def test_vm_stringdefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_AttrDef_strategy)
@settings(max_examples=50)
def test_vm_attrdef_instantiation(instance):
    assert isinstance(instance, vM_AttrDef)



@given(instance=vM_AttrDef_strategy)
def test_vm_attrdef_notDecidable_setter(instance):
    original = instance.notDecidable
    instance.notDecidable = original
    assert instance.notDecidable == original



@given(instance=vM_AttrDef_strategy)
def test_vm_attrdef_notTranslatable_setter(instance):
    original = instance.notTranslatable
    instance.notTranslatable = original
    assert instance.notTranslatable == original



@given(instance=vM_AttrDef_strategy)
def test_vm_attrdef_runTime_setter(instance):
    original = instance.runTime
    instance.runTime = original
    assert instance.runTime == original

@given(instance=vM_String_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_string_att_id_instantiation(instance):
    assert isinstance(instance, vM_String_ATT_ID)

@given(instance=vM_BoolDefaultDef_strategy)
@settings(max_examples=50)
def test_vm_booldefaultdef_instantiation(instance):
    assert isinstance(instance, vM_BoolDefaultDef)



@given(instance=vM_BoolDefaultDef_strategy)
def test_vm_booldefaultdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_Boolean_ATT_ID_strategy)
@settings(max_examples=50)
def test_vm_boolean_att_id_instantiation(instance):
    assert isinstance(instance, vM_Boolean_ATT_ID)

@given(instance=FeaturesGroup_strategy)
@settings(max_examples=50)
def test_featuresgroup_instantiation(instance):
    assert isinstance(instance, FeaturesGroup)

@given(instance=vM_Orgroup_strategy)
@settings(max_examples=50)
def test_vm_orgroup_instantiation(instance):
    assert isinstance(instance, vM_Orgroup)

@given(instance=vM_CardinalityBased_strategy)
@settings(max_examples=50)
def test_vm_cardinalitybased_instantiation(instance):
    assert isinstance(instance, vM_CardinalityBased)



@given(instance=vM_CardinalityBased_strategy)
def test_vm_cardinalitybased_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=vM_CardinalityBased_strategy)
def test_vm_cardinalitybased_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=vM_CardinalityBased_strategy)
def test_vm_cardinalitybased_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=BasicAttrDef_strategy)
@settings(max_examples=50)
def test_basicattrdef_instantiation(instance):
    assert isinstance(instance, BasicAttrDef)

@given(instance=vM_StringAttrDef_strategy)
@settings(max_examples=50)
def test_vm_stringattrdef_instantiation(instance):
    assert isinstance(instance, vM_StringAttrDef)



@given(instance=vM_StringAttrDef_strategy)
def test_vm_stringattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_RealAttrDef_strategy)
@settings(max_examples=50)
def test_vm_realattrdef_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDef)

@given(instance=vM_IntegerAttrDef_strategy)
@settings(max_examples=50)
def test_vm_integerattrdef_instantiation(instance):
    assert isinstance(instance, vM_IntegerAttrDef)

@given(instance=vM_Xorgroup_strategy)
@settings(max_examples=50)
def test_vm_xorgroup_instantiation(instance):
    assert isinstance(instance, vM_Xorgroup)

@given(instance=vM_BooleanAttrDef_strategy)
@settings(max_examples=50)
def test_vm_booleanattrdef_instantiation(instance):
    assert isinstance(instance, vM_BooleanAttrDef)



@given(instance=vM_BooleanAttrDef_strategy)
def test_vm_booleanattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_EnumAttrDef_strategy)
@settings(max_examples=50)
def test_vm_enumattrdef_instantiation(instance):
    assert isinstance(instance, vM_EnumAttrDef)



@given(instance=vM_EnumAttrDef_strategy)
def test_vm_enumattrdef_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_BasicAttrDef_strategy)
@settings(max_examples=50)
def test_vm_basicattrdef_instantiation(instance):
    assert isinstance(instance, vM_BasicAttrDef)

@given(instance=vM_RealAttrDefComplement_strategy)
@settings(max_examples=50)
def test_vm_realattrdefcomplement_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefComplement)



@given(instance=vM_RealAttrDefComplement_strategy)
def test_vm_realattrdefcomplement_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=vM_RealAttrDefComplement_strategy)
def test_vm_realattrdefcomplement_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original

@given(instance=RealAttrDef_strategy)
@settings(max_examples=50)
def test_realattrdef_instantiation(instance):
    assert isinstance(instance, RealAttrDef)

@given(instance=vM_RealAttrDefUnbounded_strategy)
@settings(max_examples=50)
def test_vm_realattrdefunbounded_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefUnbounded)



@given(instance=vM_RealAttrDefUnbounded_strategy)
def test_vm_realattrdefunbounded_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=vM_RealAttrDefBounded_strategy)
@settings(max_examples=50)
def test_vm_realattrdefbounded_instantiation(instance):
    assert isinstance(instance, vM_RealAttrDefBounded)

@given(instance=vM_Email_strategy)
@settings(max_examples=50)
def test_vm_email_instantiation(instance):
    assert isinstance(instance, vM_Email)



@given(instance=vM_Email_strategy)
def test_vm_email_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original



@given(instance=vM_Email_strategy)
def test_vm_email_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=vM_Version_strategy)
@settings(max_examples=50)
def test_vm_version_instantiation(instance):
    assert isinstance(instance, vM_Version)



@given(instance=vM_Version_strategy)
def test_vm_version_tail_setter(instance):
    original = instance.tail
    instance.tail = original
    assert instance.tail == original



@given(instance=vM_Version_strategy)
def test_vm_version_main_setter(instance):
    original = instance.main
    instance.main = original
    assert instance.main == original

@given(instance=VmBlock_strategy)
@settings(max_examples=50)
def test_vmblock_instantiation(instance):
    assert isinstance(instance, VmBlock)

@given(instance=vM_Attributes_strategy)
@settings(max_examples=50)
def test_vm_attributes_instantiation(instance):
    assert isinstance(instance, vM_Attributes)

@given(instance=vM_MetaDataDeclaration_strategy)
@settings(max_examples=50)
def test_vm_metadatadeclaration_instantiation(instance):
    assert isinstance(instance, vM_MetaDataDeclaration)



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=vM_MetaDataDeclaration_strategy)
def test_vm_metadatadeclaration_publication_setter(instance):
    original = instance.publication
    instance.publication = original
    assert instance.publication == original

@given(instance=vM_ImportDeclaration_strategy)
@settings(max_examples=50)
def test_vm_importdeclaration_instantiation(instance):
    assert isinstance(instance, vM_ImportDeclaration)



@given(instance=vM_ImportDeclaration_strategy)
def test_vm_importdeclaration_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=vM_Constraints_strategy)
@settings(max_examples=50)
def test_vm_constraints_instantiation(instance):
    assert isinstance(instance, vM_Constraints)

@given(instance=vM_Descriptions_strategy)
@settings(max_examples=50)
def test_vm_descriptions_instantiation(instance):
    assert isinstance(instance, vM_Descriptions)

@given(instance=vM_Configurations_strategy)
@settings(max_examples=50)
def test_vm_configurations_instantiation(instance):
    assert isinstance(instance, vM_Configurations)

@given(instance=vM_Objectives_strategy)
@settings(max_examples=50)
def test_vm_objectives_instantiation(instance):
    assert isinstance(instance, vM_Objectives)

@given(instance=vM_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_vm_packagedeclaration_instantiation(instance):
    assert isinstance(instance, vM_PackageDeclaration)



@given(instance=vM_PackageDeclaration_strategy)
def test_vm_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=vM_FeatureDefinition_strategy)
@settings(max_examples=50)
def test_vm_featuredefinition_instantiation(instance):
    assert isinstance(instance, vM_FeatureDefinition)

@given(instance=FeatureDefinition_strategy)
@settings(max_examples=50)
def test_featuredefinition_instantiation(instance):
    assert isinstance(instance, FeatureDefinition)

@given(instance=vM_Feature_strategy)
@settings(max_examples=50)
def test_vm_feature_instantiation(instance):
    assert isinstance(instance, vM_Feature)



@given(instance=vM_Feature_strategy)
def test_vm_feature_notTranslatable_setter(instance):
    original = instance.notTranslatable
    instance.notTranslatable = original
    assert instance.notTranslatable == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_runTime_setter(instance):
    original = instance.runTime
    instance.runTime = original
    assert instance.runTime == original



@given(instance=vM_Feature_strategy)
def test_vm_feature_notDecidable_setter(instance):
    original = instance.notDecidable
    instance.notDecidable = original
    assert instance.notDecidable == original

@given(instance=vM_FeaturesGroup_strategy)
@settings(max_examples=50)
def test_vm_featuresgroup_instantiation(instance):
    assert isinstance(instance, vM_FeaturesGroup)

@given(instance=vM_FeatureHierarchy_strategy)
@settings(max_examples=50)
def test_vm_featurehierarchy_instantiation(instance):
    assert isinstance(instance, vM_FeatureHierarchy)

@given(instance=vM_Relationships_strategy)
@settings(max_examples=50)
def test_vm_relationships_instantiation(instance):
    assert isinstance(instance, vM_Relationships)

@given(instance=vM_VmBlock_strategy)
@settings(max_examples=50)
def test_vm_vmblock_instantiation(instance):
    assert isinstance(instance, vM_VmBlock)

@given(instance=vM_Model_strategy)
@settings(max_examples=50)
def test_vm_model_instantiation(instance):
    assert isinstance(instance, vM_Model)
