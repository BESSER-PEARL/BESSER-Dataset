import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    coCoMM_HardLimitDRExpression,
    coCoMM_Config,
    coCoMM_CrossModelConstraint,
    coCoMM_CoCo,
    coCoMM_CTConstraintExpression,
    DecisionRule,
    coCoMM_HardLimitDR,
    coCoMM_OptimizationDR,
    coCoMM_SelectionStateDR,
    coCoMM_CMConstraintExpression,
    coCoMM_Stakeholder,
    coCoMM_Project,
    coCoMM_DecisionRule,
    coCoMM_FeatureAttribute,
    coCoMM_TreeConstraint,
    coCoMM_FeatureAttributeElement,
    coCoMM_AttributeTypeElement,
    coCoMM_AttributeType,
    coCoMM_CrossTreeConstraint,
    coCoMM_Feature,
    coCoMM_FeatureModel,
    ConfigType,
    CTConstraintType,
    DataType,
    DRSelectionStateType,
    CMConstraintType,
    DROptimizationOp,
    DRType,
    DRHardLimitOp,
    TreeConstraintType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cocomm_hardlimitdrexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitDRExpression)


def test_cocomm_hardlimitdrexpression_constructor_exists():
    assert callable(coCoMM_HardLimitDRExpression.__init__)


def test_cocomm_hardlimitdrexpression_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitDRExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "value" in params, "Missing parameter 'value'"

def test_cocomm_hardlimitdrexpression_has_op():
    assert hasattr(coCoMM_HardLimitDRExpression, "op")
    descriptor = None
    for klass in coCoMM_HardLimitDRExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_hardlimitdrexpression_has_value():
    assert hasattr(coCoMM_HardLimitDRExpression, "value")
    descriptor = None
    for klass in coCoMM_HardLimitDRExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_config_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Config)


def test_cocomm_config_constructor_exists():
    assert callable(coCoMM_Config.__init__)


def test_cocomm_config_constructor_args():
    sig = inspect.signature(coCoMM_Config.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_cocomm_config_has_type():
    assert hasattr(coCoMM_Config, "type")
    descriptor = None
    for klass in coCoMM_Config.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_config_has_selected():
    assert hasattr(coCoMM_Config, "selected")
    descriptor = None
    for klass in coCoMM_Config.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_crossmodelconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CrossModelConstraint)


def test_cocomm_crossmodelconstraint_constructor_exists():
    assert callable(coCoMM_CrossModelConstraint.__init__)


def test_cocomm_crossmodelconstraint_constructor_args():
    sig = inspect.signature(coCoMM_CrossModelConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_coco_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CoCo)


def test_cocomm_coco_constructor_exists():
    assert callable(coCoMM_CoCo.__init__)


def test_cocomm_coco_constructor_args():
    sig = inspect.signature(coCoMM_CoCo.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_ctconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CTConstraintExpression)


def test_cocomm_ctconstraintexpression_constructor_exists():
    assert callable(coCoMM_CTConstraintExpression.__init__)


def test_cocomm_ctconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM_CTConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm_ctconstraintexpression_has_op():
    assert hasattr(coCoMM_CTConstraintExpression, "op")
    descriptor = None
    for klass in coCoMM_CTConstraintExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_decisionrule_is_not_abstract():
    assert not inspect.isabstract(DecisionRule)


def test_decisionrule_constructor_exists():
    assert callable(DecisionRule.__init__)


def test_decisionrule_constructor_args():
    sig = inspect.signature(DecisionRule.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_hardlimitdr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitDR)


def test_cocomm_hardlimitdr_constructor_exists():
    assert callable(coCoMM_HardLimitDR.__init__)


def test_cocomm_hardlimitdr_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitDR.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_optimizationdr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_OptimizationDR)


def test_cocomm_optimizationdr_constructor_exists():
    assert callable(coCoMM_OptimizationDR.__init__)


def test_cocomm_optimizationdr_constructor_args():
    sig = inspect.signature(coCoMM_OptimizationDR.__init__)
    params = list(sig.parameters.keys())
    assert "funct" in params, "Missing parameter 'funct'"

def test_cocomm_optimizationdr_has_funct():
    assert hasattr(coCoMM_OptimizationDR, "funct")
    descriptor = None
    for klass in coCoMM_OptimizationDR.__mro__:
        if "funct" in klass.__dict__:
            descriptor = klass.__dict__["funct"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_selectionstatedr_is_not_abstract():
    assert not inspect.isabstract(coCoMM_SelectionStateDR)


def test_cocomm_selectionstatedr_constructor_exists():
    assert callable(coCoMM_SelectionStateDR.__init__)


def test_cocomm_selectionstatedr_constructor_args():
    sig = inspect.signature(coCoMM_SelectionStateDR.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_cocomm_selectionstatedr_has_state():
    assert hasattr(coCoMM_SelectionStateDR, "state")
    descriptor = None
    for klass in coCoMM_SelectionStateDR.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_cmconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CMConstraintExpression)


def test_cocomm_cmconstraintexpression_constructor_exists():
    assert callable(coCoMM_CMConstraintExpression.__init__)


def test_cocomm_cmconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM_CMConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm_cmconstraintexpression_has_op():
    assert hasattr(coCoMM_CMConstraintExpression, "op")
    descriptor = None
    for klass in coCoMM_CMConstraintExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_stakeholder_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Stakeholder)


def test_cocomm_stakeholder_constructor_exists():
    assert callable(coCoMM_Stakeholder.__init__)


def test_cocomm_stakeholder_constructor_args():
    sig = inspect.signature(coCoMM_Stakeholder.__init__)
    params = list(sig.parameters.keys())
    assert "job" in params, "Missing parameter 'job'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_stakeholder_has_job():
    assert hasattr(coCoMM_Stakeholder, "job")
    descriptor = None
    for klass in coCoMM_Stakeholder.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_stakeholder_has_name():
    assert hasattr(coCoMM_Stakeholder, "name")
    descriptor = None
    for klass in coCoMM_Stakeholder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_project_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Project)


def test_cocomm_project_constructor_exists():
    assert callable(coCoMM_Project.__init__)


def test_cocomm_project_constructor_args():
    sig = inspect.signature(coCoMM_Project.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "target" in params, "Missing parameter 'target'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_project_has_date():
    assert hasattr(coCoMM_Project, "date")
    descriptor = None
    for klass in coCoMM_Project.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_project_has_target():
    assert hasattr(coCoMM_Project, "target")
    descriptor = None
    for klass in coCoMM_Project.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_project_has_name():
    assert hasattr(coCoMM_Project, "name")
    descriptor = None
    for klass in coCoMM_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_decisionrule_is_not_abstract():
    assert not inspect.isabstract(coCoMM_DecisionRule)


def test_cocomm_decisionrule_constructor_exists():
    assert callable(coCoMM_DecisionRule.__init__)


def test_cocomm_decisionrule_constructor_args():
    sig = inspect.signature(coCoMM_DecisionRule.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm_decisionrule_has_type():
    assert hasattr(coCoMM_DecisionRule, "type")
    descriptor = None
    for klass in coCoMM_DecisionRule.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_featureattribute_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureAttribute)


def test_cocomm_featureattribute_constructor_exists():
    assert callable(coCoMM_FeatureAttribute.__init__)


def test_cocomm_featureattribute_constructor_args():
    sig = inspect.signature(coCoMM_FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_featureattribute_has_name():
    assert hasattr(coCoMM_FeatureAttribute, "name")
    descriptor = None
    for klass in coCoMM_FeatureAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_treeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_TreeConstraint)


def test_cocomm_treeconstraint_constructor_exists():
    assert callable(coCoMM_TreeConstraint.__init__)


def test_cocomm_treeconstraint_constructor_args():
    sig = inspect.signature(coCoMM_TreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm_treeconstraint_has_type():
    assert hasattr(coCoMM_TreeConstraint, "type")
    descriptor = None
    for klass in coCoMM_TreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_featureattributeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureAttributeElement)


def test_cocomm_featureattributeelement_constructor_exists():
    assert callable(coCoMM_FeatureAttributeElement.__init__)


def test_cocomm_featureattributeelement_constructor_args():
    sig = inspect.signature(coCoMM_FeatureAttributeElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cocomm_featureattributeelement_has_value():
    assert hasattr(coCoMM_FeatureAttributeElement, "value")
    descriptor = None
    for klass in coCoMM_FeatureAttributeElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_attributetypeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AttributeTypeElement)


def test_cocomm_attributetypeelement_constructor_exists():
    assert callable(coCoMM_AttributeTypeElement.__init__)


def test_cocomm_attributetypeelement_constructor_args():
    sig = inspect.signature(coCoMM_AttributeTypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_cocomm_attributetypeelement_has_name():
    assert hasattr(coCoMM_AttributeTypeElement, "name")
    descriptor = None
    for klass in coCoMM_AttributeTypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_attributetypeelement_has_dataType():
    assert hasattr(coCoMM_AttributeTypeElement, "dataType")
    descriptor = None
    for klass in coCoMM_AttributeTypeElement.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_attributetype_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AttributeType)


def test_cocomm_attributetype_constructor_exists():
    assert callable(coCoMM_AttributeType.__init__)


def test_cocomm_attributetype_constructor_args():
    sig = inspect.signature(coCoMM_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_attributetype_has_id():
    assert hasattr(coCoMM_AttributeType, "id")
    descriptor = None
    for klass in coCoMM_AttributeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_attributetype_has_name():
    assert hasattr(coCoMM_AttributeType, "name")
    descriptor = None
    for klass in coCoMM_AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_CrossTreeConstraint)


def test_cocomm_crosstreeconstraint_constructor_exists():
    assert callable(coCoMM_CrossTreeConstraint.__init__)


def test_cocomm_crosstreeconstraint_constructor_args():
    sig = inspect.signature(coCoMM_CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_feature_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Feature)


def test_cocomm_feature_constructor_exists():
    assert callable(coCoMM_Feature.__init__)


def test_cocomm_feature_constructor_args():
    sig = inspect.signature(coCoMM_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_cocomm_feature_has_id():
    assert hasattr(coCoMM_Feature, "id")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_feature_has_name():
    assert hasattr(coCoMM_Feature, "name")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_feature_has_abstract():
    assert hasattr(coCoMM_Feature, "abstract")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureModel)


def test_cocomm_featuremodel_constructor_exists():
    assert callable(coCoMM_FeatureModel.__init__)


def test_cocomm_featuremodel_constructor_args():
    sig = inspect.signature(coCoMM_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "isDomain" in params, "Missing parameter 'isDomain'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_featuremodel_has_isDomain():
    assert hasattr(coCoMM_FeatureModel, "isDomain")
    descriptor = None
    for klass in coCoMM_FeatureModel.__mro__:
        if "isDomain" in klass.__dict__:
            descriptor = klass.__dict__["isDomain"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_featuremodel_has_name():
    assert hasattr(coCoMM_FeatureModel, "name")
    descriptor = None
    for klass in coCoMM_FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_configtype_exists():
    # Check that the Enumeration exists
    assert ConfigType is not None

def test_configtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigType]
    expected_literals = [
        "output",
        "input",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigType"

def test_ctconstrainttype_exists():
    # Check that the Enumeration exists
    assert CTConstraintType is not None

def test_ctconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CTConstraintType]
    expected_literals = [
        "or_",
        "not_",
        "implies",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CTConstraintType"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "int",
        "String",
        "double",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_drselectionstatetype_exists():
    # Check that the Enumeration exists
    assert DRSelectionStateType is not None

def test_drselectionstatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRSelectionStateType]
    expected_literals = [
        "mandatory",
        "forbidden",
        "preferred",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRSelectionStateType"

def test_cmconstrainttype_exists():
    # Check that the Enumeration exists
    assert CMConstraintType is not None

def test_cmconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CMConstraintType]
    expected_literals = [
        "and_",
        "or_",
        "not_",
        "implies",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CMConstraintType"

def test_droptimizationop_exists():
    # Check that the Enumeration exists
    assert DROptimizationOp is not None

def test_droptimizationop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DROptimizationOp]
    expected_literals = [
        "maximize",
        "minimize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DROptimizationOp"

def test_drtype_exists():
    # Check that the Enumeration exists
    assert DRType is not None

def test_drtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRType]
    expected_literals = [
        "hardLimit",
        "selectionState",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRType"

def test_drhardlimitop_exists():
    # Check that the Enumeration exists
    assert DRHardLimitOp is not None

def test_drhardlimitop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DRHardLimitOp]
    expected_literals = [
        "eq",
        "lt",
        "leq",
        "gt",
        "geq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DRHardLimitOp"

def test_treeconstrainttype_exists():
    # Check that the Enumeration exists
    assert TreeConstraintType is not None

def test_treeconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeConstraintType]
    expected_literals = [
        "Optional",
        "Mandatory",
        "Alternative",
        "Or",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeConstraintType"


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
coCoMM_HardLimitDRExpression_strategy = st.builds(
    coCoMM_HardLimitDRExpression,
    op=
        safe_text,
    value=
        safe_text
)
coCoMM_Config_strategy = st.builds(
    coCoMM_Config,
    type=
        safe_text,
    selected=
        st.booleans()
)
coCoMM_CrossModelConstraint_strategy = st.builds(
    coCoMM_CrossModelConstraint,
)
coCoMM_CoCo_strategy = st.builds(
    coCoMM_CoCo,
)
coCoMM_CTConstraintExpression_strategy = st.builds(
    coCoMM_CTConstraintExpression,
    op=
        safe_text
)
DecisionRule_strategy = st.builds(
    DecisionRule,
)
coCoMM_HardLimitDR_strategy = st.builds(
    coCoMM_HardLimitDR,
)
coCoMM_OptimizationDR_strategy = st.builds(
    coCoMM_OptimizationDR,
    funct=
        safe_text
)
coCoMM_SelectionStateDR_strategy = st.builds(
    coCoMM_SelectionStateDR,
    state=
        safe_text
)
coCoMM_CMConstraintExpression_strategy = st.builds(
    coCoMM_CMConstraintExpression,
    op=
        safe_text
)
coCoMM_Stakeholder_strategy = st.builds(
    coCoMM_Stakeholder,
    job=
        safe_text,
    name=
        safe_text
)
coCoMM_Project_strategy = st.builds(
    coCoMM_Project,
    date=
        st.dates(),
    target=
        st.booleans(),
    name=
        safe_text
)
coCoMM_DecisionRule_strategy = st.builds(
    coCoMM_DecisionRule,
    type=
        safe_text
)
coCoMM_FeatureAttribute_strategy = st.builds(
    coCoMM_FeatureAttribute,
    name=
        safe_text
)
coCoMM_TreeConstraint_strategy = st.builds(
    coCoMM_TreeConstraint,
    type=
        safe_text
)
coCoMM_FeatureAttributeElement_strategy = st.builds(
    coCoMM_FeatureAttributeElement,
    value=
        safe_text
)
coCoMM_AttributeTypeElement_strategy = st.builds(
    coCoMM_AttributeTypeElement,
    name=
        safe_text,
    dataType=
        safe_text
)
coCoMM_AttributeType_strategy = st.builds(
    coCoMM_AttributeType,
    id=
        safe_text,
    name=
        safe_text
)
coCoMM_CrossTreeConstraint_strategy = st.builds(
    coCoMM_CrossTreeConstraint,
)
coCoMM_Feature_strategy = st.builds(
    coCoMM_Feature,
    id=
        safe_text,
    name=
        safe_text,
    abstract=
        st.booleans()
)
coCoMM_FeatureModel_strategy = st.builds(
    coCoMM_FeatureModel,
    isDomain=
        st.booleans(),
    name=
        safe_text
)

@given(instance=coCoMM_HardLimitDRExpression_strategy)
@settings(max_examples=50)
def test_cocomm_hardlimitdrexpression_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDRExpression)



@given(instance=coCoMM_HardLimitDRExpression_strategy)
def test_cocomm_hardlimitdrexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=coCoMM_HardLimitDRExpression_strategy)
def test_cocomm_hardlimitdrexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=coCoMM_Config_strategy)
@settings(max_examples=50)
def test_cocomm_config_instantiation(instance):
    assert isinstance(instance, coCoMM_Config)



@given(instance=coCoMM_Config_strategy)
def test_cocomm_config_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=coCoMM_Config_strategy)
def test_cocomm_config_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=coCoMM_CrossModelConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_crossmodelconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossModelConstraint)

@given(instance=coCoMM_CoCo_strategy)
@settings(max_examples=50)
def test_cocomm_coco_instantiation(instance):
    assert isinstance(instance, coCoMM_CoCo)

@given(instance=coCoMM_CTConstraintExpression_strategy)
@settings(max_examples=50)
def test_cocomm_ctconstraintexpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CTConstraintExpression)



@given(instance=coCoMM_CTConstraintExpression_strategy)
def test_cocomm_ctconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=DecisionRule_strategy)
@settings(max_examples=50)
def test_decisionrule_instantiation(instance):
    assert isinstance(instance, DecisionRule)

@given(instance=coCoMM_HardLimitDR_strategy)
@settings(max_examples=50)
def test_cocomm_hardlimitdr_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitDR)

@given(instance=coCoMM_OptimizationDR_strategy)
@settings(max_examples=50)
def test_cocomm_optimizationdr_instantiation(instance):
    assert isinstance(instance, coCoMM_OptimizationDR)



@given(instance=coCoMM_OptimizationDR_strategy)
def test_cocomm_optimizationdr_funct_setter(instance):
    original = instance.funct
    instance.funct = original
    assert instance.funct == original

@given(instance=coCoMM_SelectionStateDR_strategy)
@settings(max_examples=50)
def test_cocomm_selectionstatedr_instantiation(instance):
    assert isinstance(instance, coCoMM_SelectionStateDR)



@given(instance=coCoMM_SelectionStateDR_strategy)
def test_cocomm_selectionstatedr_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=coCoMM_CMConstraintExpression_strategy)
@settings(max_examples=50)
def test_cocomm_cmconstraintexpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CMConstraintExpression)



@given(instance=coCoMM_CMConstraintExpression_strategy)
def test_cocomm_cmconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=coCoMM_Stakeholder_strategy)
@settings(max_examples=50)
def test_cocomm_stakeholder_instantiation(instance):
    assert isinstance(instance, coCoMM_Stakeholder)



@given(instance=coCoMM_Stakeholder_strategy)
def test_cocomm_stakeholder_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original



@given(instance=coCoMM_Stakeholder_strategy)
def test_cocomm_stakeholder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM_Project_strategy)
@settings(max_examples=50)
def test_cocomm_project_instantiation(instance):
    assert isinstance(instance, coCoMM_Project)



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM_DecisionRule_strategy)
@settings(max_examples=50)
def test_cocomm_decisionrule_instantiation(instance):
    assert isinstance(instance, coCoMM_DecisionRule)



@given(instance=coCoMM_DecisionRule_strategy)
def test_cocomm_decisionrule_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM_FeatureAttribute_strategy)
@settings(max_examples=50)
def test_cocomm_featureattribute_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttribute)



@given(instance=coCoMM_FeatureAttribute_strategy)
def test_cocomm_featureattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM_TreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_treeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_TreeConstraint)



@given(instance=coCoMM_TreeConstraint_strategy)
def test_cocomm_treeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM_FeatureAttributeElement_strategy)
@settings(max_examples=50)
def test_cocomm_featureattributeelement_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttributeElement)



@given(instance=coCoMM_FeatureAttributeElement_strategy)
def test_cocomm_featureattributeelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=coCoMM_AttributeTypeElement_strategy)
@settings(max_examples=50)
def test_cocomm_attributetypeelement_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeTypeElement)



@given(instance=coCoMM_AttributeTypeElement_strategy)
def test_cocomm_attributetypeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_AttributeTypeElement_strategy)
def test_cocomm_attributetypeelement_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=coCoMM_AttributeType_strategy)
@settings(max_examples=50)
def test_cocomm_attributetype_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeType)



@given(instance=coCoMM_AttributeType_strategy)
def test_cocomm_attributetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_AttributeType_strategy)
def test_cocomm_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM_CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossTreeConstraint)

@given(instance=coCoMM_Feature_strategy)
@settings(max_examples=50)
def test_cocomm_feature_instantiation(instance):
    assert isinstance(instance, coCoMM_Feature)



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=coCoMM_FeatureModel_strategy)
@settings(max_examples=50)
def test_cocomm_featuremodel_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureModel)



@given(instance=coCoMM_FeatureModel_strategy)
def test_cocomm_featuremodel_isDomain_setter(instance):
    original = instance.isDomain
    instance.isDomain = original
    assert instance.isDomain == original



@given(instance=coCoMM_FeatureModel_strategy)
def test_cocomm_featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
