import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SolutionConstraint,
    coCoMM_OptimizationSC,
    coCoMM_Config,
    coCoMM_AggregationFunction,
    coCoMM_HardLimitCCExpression,
    ConfigurationConstraint,
    coCoMM_HardLimitCC,
    coCoMM_OptimizationCC,
    coCoMM_SelectionStateCC,
    coCoMM_CMConstraintExpression,
    coCoMM_Stakeholder,
    coCoMM_Project,
    coCoMM_ConfigurationConstraint,
    coCoMM_SolutionConstraint,
    coCoMM_CrossModelConstraint,
    coCoMM_CoCo,
    coCoMM_CTConstraintExpression,
    coCoMM_AttributeType,
    coCoMM_FeatureAttribute,
    coCoMM_TreeConstraint,
    coCoMM_CrossTreeConstraint,
    coCoMM_Feature,
    coCoMM_FeatureModel,
    CMConstraintType,
    ConfigType,
    CTConstraintType,
    SCType,
    CCOptimizationOp,
    TreeConstraintType,
    CCSelectionStateType,
    AggregationOp,
    DataType,
    CCType,
    OptimizationSCFunct,
    CCHardLimitOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_solutionconstraint_is_not_abstract():
    assert not inspect.isabstract(SolutionConstraint)


def test_solutionconstraint_constructor_exists():
    assert callable(SolutionConstraint.__init__)


def test_solutionconstraint_constructor_args():
    sig = inspect.signature(SolutionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_optimizationsc_is_not_abstract():
    assert not inspect.isabstract(coCoMM_OptimizationSC)


def test_cocomm_optimizationsc_constructor_exists():
    assert callable(coCoMM_OptimizationSC.__init__)


def test_cocomm_optimizationsc_constructor_args():
    sig = inspect.signature(coCoMM_OptimizationSC.__init__)
    params = list(sig.parameters.keys())
    assert "funct" in params, "Missing parameter 'funct'"

def test_cocomm_optimizationsc_has_funct():
    assert hasattr(coCoMM_OptimizationSC, "funct")
    descriptor = None
    for klass in coCoMM_OptimizationSC.__mro__:
        if "funct" in klass.__dict__:
            descriptor = klass.__dict__["funct"]
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



def test_cocomm_aggregationfunction_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AggregationFunction)


def test_cocomm_aggregationfunction_constructor_exists():
    assert callable(coCoMM_AggregationFunction.__init__)


def test_cocomm_aggregationfunction_constructor_args():
    sig = inspect.signature(coCoMM_AggregationFunction.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_cocomm_aggregationfunction_has_operation():
    assert hasattr(coCoMM_AggregationFunction, "operation")
    descriptor = None
    for klass in coCoMM_AggregationFunction.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_hardlimitccexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitCCExpression)


def test_cocomm_hardlimitccexpression_constructor_exists():
    assert callable(coCoMM_HardLimitCCExpression.__init__)


def test_cocomm_hardlimitccexpression_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitCCExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm_hardlimitccexpression_has_value():
    assert hasattr(coCoMM_HardLimitCCExpression, "value")
    descriptor = None
    for klass in coCoMM_HardLimitCCExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_hardlimitccexpression_has_op():
    assert hasattr(coCoMM_HardLimitCCExpression, "op")
    descriptor = None
    for klass in coCoMM_HardLimitCCExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_configurationconstraint_is_not_abstract():
    assert not inspect.isabstract(ConfigurationConstraint)


def test_configurationconstraint_constructor_exists():
    assert callable(ConfigurationConstraint.__init__)


def test_configurationconstraint_constructor_args():
    sig = inspect.signature(ConfigurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_hardlimitcc_is_not_abstract():
    assert not inspect.isabstract(coCoMM_HardLimitCC)


def test_cocomm_hardlimitcc_constructor_exists():
    assert callable(coCoMM_HardLimitCC.__init__)


def test_cocomm_hardlimitcc_constructor_args():
    sig = inspect.signature(coCoMM_HardLimitCC.__init__)
    params = list(sig.parameters.keys())



def test_cocomm_optimizationcc_is_not_abstract():
    assert not inspect.isabstract(coCoMM_OptimizationCC)


def test_cocomm_optimizationcc_constructor_exists():
    assert callable(coCoMM_OptimizationCC.__init__)


def test_cocomm_optimizationcc_constructor_args():
    sig = inspect.signature(coCoMM_OptimizationCC.__init__)
    params = list(sig.parameters.keys())
    assert "funct" in params, "Missing parameter 'funct'"

def test_cocomm_optimizationcc_has_funct():
    assert hasattr(coCoMM_OptimizationCC, "funct")
    descriptor = None
    for klass in coCoMM_OptimizationCC.__mro__:
        if "funct" in klass.__dict__:
            descriptor = klass.__dict__["funct"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_selectionstatecc_is_not_abstract():
    assert not inspect.isabstract(coCoMM_SelectionStateCC)


def test_cocomm_selectionstatecc_constructor_exists():
    assert callable(coCoMM_SelectionStateCC.__init__)


def test_cocomm_selectionstatecc_constructor_args():
    sig = inspect.signature(coCoMM_SelectionStateCC.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_cocomm_selectionstatecc_has_state():
    assert hasattr(coCoMM_SelectionStateCC, "state")
    descriptor = None
    for klass in coCoMM_SelectionStateCC.__mro__:
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
    assert "name" in params, "Missing parameter 'name'"
    assert "job" in params, "Missing parameter 'job'"

def test_cocomm_stakeholder_has_name():
    assert hasattr(coCoMM_Stakeholder, "name")
    descriptor = None
    for klass in coCoMM_Stakeholder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_stakeholder_has_job():
    assert hasattr(coCoMM_Stakeholder, "job")
    descriptor = None
    for klass in coCoMM_Stakeholder.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_project_is_not_abstract():
    assert not inspect.isabstract(coCoMM_Project)


def test_cocomm_project_constructor_exists():
    assert callable(coCoMM_Project.__init__)


def test_cocomm_project_constructor_args():
    sig = inspect.signature(coCoMM_Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"
    assert "date" in params, "Missing parameter 'date'"

def test_cocomm_project_has_name():
    assert hasattr(coCoMM_Project, "name")
    descriptor = None
    for klass in coCoMM_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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

def test_cocomm_project_has_date():
    assert hasattr(coCoMM_Project, "date")
    descriptor = None
    for klass in coCoMM_Project.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_configurationconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_ConfigurationConstraint)


def test_cocomm_configurationconstraint_constructor_exists():
    assert callable(coCoMM_ConfigurationConstraint.__init__)


def test_cocomm_configurationconstraint_constructor_args():
    sig = inspect.signature(coCoMM_ConfigurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_cocomm_configurationconstraint_has_type():
    assert hasattr(coCoMM_ConfigurationConstraint, "type")
    descriptor = None
    for klass in coCoMM_ConfigurationConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_configurationconstraint_has_name():
    assert hasattr(coCoMM_ConfigurationConstraint, "name")
    descriptor = None
    for klass in coCoMM_ConfigurationConstraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_configurationconstraint_has_id():
    assert hasattr(coCoMM_ConfigurationConstraint, "id")
    descriptor = None
    for klass in coCoMM_ConfigurationConstraint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_solutionconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM_SolutionConstraint)


def test_cocomm_solutionconstraint_constructor_exists():
    assert callable(coCoMM_SolutionConstraint.__init__)


def test_cocomm_solutionconstraint_constructor_args():
    sig = inspect.signature(coCoMM_SolutionConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm_solutionconstraint_has_type():
    assert hasattr(coCoMM_SolutionConstraint, "type")
    descriptor = None
    for klass in coCoMM_SolutionConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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
    assert "configScenario" in params, "Missing parameter 'configScenario'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_coco_has_configScenario():
    assert hasattr(coCoMM_CoCo, "configScenario")
    descriptor = None
    for klass in coCoMM_CoCo.__mro__:
        if "configScenario" in klass.__dict__:
            descriptor = klass.__dict__["configScenario"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_coco_has_id():
    assert hasattr(coCoMM_CoCo, "id")
    descriptor = None
    for klass in coCoMM_CoCo.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_coco_has_name():
    assert hasattr(coCoMM_CoCo, "name")
    descriptor = None
    for klass in coCoMM_CoCo.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_cocomm_attributetype_is_not_abstract():
    assert not inspect.isabstract(coCoMM_AttributeType)


def test_cocomm_attributetype_constructor_exists():
    assert callable(coCoMM_AttributeType.__init__)


def test_cocomm_attributetype_constructor_args():
    sig = inspect.signature(coCoMM_AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_cocomm_attributetype_has_name():
    assert hasattr(coCoMM_AttributeType, "name")
    descriptor = None
    for klass in coCoMM_AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_attributetype_has_id():
    assert hasattr(coCoMM_AttributeType, "id")
    descriptor = None
    for klass in coCoMM_AttributeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_attributetype_has_dataType():
    assert hasattr(coCoMM_AttributeType, "dataType")
    descriptor = None
    for klass in coCoMM_AttributeType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_cocomm_featureattribute_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureAttribute)


def test_cocomm_featureattribute_constructor_exists():
    assert callable(coCoMM_FeatureAttribute.__init__)


def test_cocomm_featureattribute_constructor_args():
    sig = inspect.signature(coCoMM_FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"

def test_cocomm_featureattribute_has_maxValue():
    assert hasattr(coCoMM_FeatureAttribute, "maxValue")
    descriptor = None
    for klass in coCoMM_FeatureAttribute.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_featureattribute_has_defaultValue():
    assert hasattr(coCoMM_FeatureAttribute, "defaultValue")
    descriptor = None
    for klass in coCoMM_FeatureAttribute.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_featureattribute_has_minValue():
    assert hasattr(coCoMM_FeatureAttribute, "minValue")
    descriptor = None
    for klass in coCoMM_FeatureAttribute.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
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
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm_feature_has_abstract():
    assert hasattr(coCoMM_Feature, "abstract")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_feature_has_id():
    assert hasattr(coCoMM_Feature, "id")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm_feature_has_mandatory():
    assert hasattr(coCoMM_Feature, "mandatory")
    descriptor = None
    for klass in coCoMM_Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
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



def test_cocomm_featuremodel_is_not_abstract():
    assert not inspect.isabstract(coCoMM_FeatureModel)


def test_cocomm_featuremodel_constructor_exists():
    assert callable(coCoMM_FeatureModel.__init__)


def test_cocomm_featuremodel_constructor_args():
    sig = inspect.signature(coCoMM_FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "isDomain" in params, "Missing parameter 'isDomain'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

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

def test_cocomm_featuremodel_has_id():
    assert hasattr(coCoMM_FeatureModel, "id")
    descriptor = None
    for klass in coCoMM_FeatureModel.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cmconstrainttype_exists():
    # Check that the Enumeration exists
    assert CMConstraintType is not None

def test_cmconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CMConstraintType]
    expected_literals = [
        "implies",
        "and_",
        "or_",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CMConstraintType"

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
        "implies",
        "or_",
        "not_",
        "and_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CTConstraintType"

def test_sctype_exists():
    # Check that the Enumeration exists
    assert SCType is not None

def test_sctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SCType]
    expected_literals = [
        "hardLimit",
        "finiteDomain",
        "optimization",
        "selectionState",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SCType"

def test_ccoptimizationop_exists():
    # Check that the Enumeration exists
    assert CCOptimizationOp is not None

def test_ccoptimizationop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CCOptimizationOp]
    expected_literals = [
        "maximize",
        "minimize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CCOptimizationOp"

def test_treeconstrainttype_exists():
    # Check that the Enumeration exists
    assert TreeConstraintType is not None

def test_treeconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeConstraintType]
    expected_literals = [
        "Alternative",
        "Or",
        "And",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeConstraintType"

def test_ccselectionstatetype_exists():
    # Check that the Enumeration exists
    assert CCSelectionStateType is not None

def test_ccselectionstatetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CCSelectionStateType]
    expected_literals = [
        "mandatory",
        "forbidden",
        "preferred",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CCSelectionStateType"

def test_aggregationop_exists():
    # Check that the Enumeration exists
    assert AggregationOp is not None

def test_aggregationop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationOp]
    expected_literals = [
        "min",
        "multiply",
        "add",
        "max",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationOp"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "double",
        "String",
        "int",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_cctype_exists():
    # Check that the Enumeration exists
    assert CCType is not None

def test_cctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CCType]
    expected_literals = [
        "optimization",
        "selectionState",
        "hardLimit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CCType"

def test_optimizationscfunct_exists():
    # Check that the Enumeration exists
    assert OptimizationSCFunct is not None

def test_optimizationscfunct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimizationSCFunct]
    expected_literals = [
        "minimize",
        "maximize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimizationSCFunct"

def test_cchardlimitop_exists():
    # Check that the Enumeration exists
    assert CCHardLimitOp is not None

def test_cchardlimitop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CCHardLimitOp]
    expected_literals = [
        "gt",
        "leq",
        "lt",
        "eq",
        "geq",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CCHardLimitOp"


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
SolutionConstraint_strategy = st.builds(
    SolutionConstraint,
)
coCoMM_OptimizationSC_strategy = st.builds(
    coCoMM_OptimizationSC,
    funct=
        safe_text
)
coCoMM_Config_strategy = st.builds(
    coCoMM_Config,
    type=
        safe_text,
    selected=
        st.booleans()
)
coCoMM_AggregationFunction_strategy = st.builds(
    coCoMM_AggregationFunction,
    operation=
        safe_text
)
coCoMM_HardLimitCCExpression_strategy = st.builds(
    coCoMM_HardLimitCCExpression,
    value=
        safe_text,
    op=
        safe_text
)
ConfigurationConstraint_strategy = st.builds(
    ConfigurationConstraint,
)
coCoMM_HardLimitCC_strategy = st.builds(
    coCoMM_HardLimitCC,
)
coCoMM_OptimizationCC_strategy = st.builds(
    coCoMM_OptimizationCC,
    funct=
        safe_text
)
coCoMM_SelectionStateCC_strategy = st.builds(
    coCoMM_SelectionStateCC,
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
    name=
        safe_text,
    job=
        safe_text
)
coCoMM_Project_strategy = st.builds(
    coCoMM_Project,
    name=
        safe_text,
    target=
        st.booleans(),
    date=
        st.dates()
)
coCoMM_ConfigurationConstraint_strategy = st.builds(
    coCoMM_ConfigurationConstraint,
    type=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
coCoMM_SolutionConstraint_strategy = st.builds(
    coCoMM_SolutionConstraint,
    type=
        safe_text
)
coCoMM_CrossModelConstraint_strategy = st.builds(
    coCoMM_CrossModelConstraint,
)
coCoMM_CoCo_strategy = st.builds(
    coCoMM_CoCo,
    configScenario=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
coCoMM_CTConstraintExpression_strategy = st.builds(
    coCoMM_CTConstraintExpression,
    op=
        safe_text
)
coCoMM_AttributeType_strategy = st.builds(
    coCoMM_AttributeType,
    name=
        safe_text,
    id=
        safe_text,
    dataType=
        safe_text
)
coCoMM_FeatureAttribute_strategy = st.builds(
    coCoMM_FeatureAttribute,
    maxValue=
        safe_text,
    defaultValue=
        safe_text,
    minValue=
        safe_text
)
coCoMM_TreeConstraint_strategy = st.builds(
    coCoMM_TreeConstraint,
    type=
        safe_text
)
coCoMM_CrossTreeConstraint_strategy = st.builds(
    coCoMM_CrossTreeConstraint,
)
coCoMM_Feature_strategy = st.builds(
    coCoMM_Feature,
    abstract=
        st.booleans(),
    id=
        safe_text,
    mandatory=
        st.booleans(),
    name=
        safe_text
)
coCoMM_FeatureModel_strategy = st.builds(
    coCoMM_FeatureModel,
    isDomain=
        st.booleans(),
    name=
        safe_text,
    id=
        safe_text
)

@given(instance=SolutionConstraint_strategy)
@settings(max_examples=50)
def test_solutionconstraint_instantiation(instance):
    assert isinstance(instance, SolutionConstraint)

@given(instance=coCoMM_OptimizationSC_strategy)
@settings(max_examples=50)
def test_cocomm_optimizationsc_instantiation(instance):
    assert isinstance(instance, coCoMM_OptimizationSC)



@given(instance=coCoMM_OptimizationSC_strategy)
def test_cocomm_optimizationsc_funct_setter(instance):
    original = instance.funct
    instance.funct = original
    assert instance.funct == original

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

@given(instance=coCoMM_AggregationFunction_strategy)
@settings(max_examples=50)
def test_cocomm_aggregationfunction_instantiation(instance):
    assert isinstance(instance, coCoMM_AggregationFunction)



@given(instance=coCoMM_AggregationFunction_strategy)
def test_cocomm_aggregationfunction_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=coCoMM_HardLimitCCExpression_strategy)
@settings(max_examples=50)
def test_cocomm_hardlimitccexpression_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitCCExpression)



@given(instance=coCoMM_HardLimitCCExpression_strategy)
def test_cocomm_hardlimitccexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=coCoMM_HardLimitCCExpression_strategy)
def test_cocomm_hardlimitccexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ConfigurationConstraint_strategy)
@settings(max_examples=50)
def test_configurationconstraint_instantiation(instance):
    assert isinstance(instance, ConfigurationConstraint)

@given(instance=coCoMM_HardLimitCC_strategy)
@settings(max_examples=50)
def test_cocomm_hardlimitcc_instantiation(instance):
    assert isinstance(instance, coCoMM_HardLimitCC)

@given(instance=coCoMM_OptimizationCC_strategy)
@settings(max_examples=50)
def test_cocomm_optimizationcc_instantiation(instance):
    assert isinstance(instance, coCoMM_OptimizationCC)



@given(instance=coCoMM_OptimizationCC_strategy)
def test_cocomm_optimizationcc_funct_setter(instance):
    original = instance.funct
    instance.funct = original
    assert instance.funct == original

@given(instance=coCoMM_SelectionStateCC_strategy)
@settings(max_examples=50)
def test_cocomm_selectionstatecc_instantiation(instance):
    assert isinstance(instance, coCoMM_SelectionStateCC)



@given(instance=coCoMM_SelectionStateCC_strategy)
def test_cocomm_selectionstatecc_state_setter(instance):
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
def test_cocomm_stakeholder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_Stakeholder_strategy)
def test_cocomm_stakeholder_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original

@given(instance=coCoMM_Project_strategy)
@settings(max_examples=50)
def test_cocomm_project_instantiation(instance):
    assert isinstance(instance, coCoMM_Project)



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=coCoMM_Project_strategy)
def test_cocomm_project_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=coCoMM_ConfigurationConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_configurationconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_ConfigurationConstraint)



@given(instance=coCoMM_ConfigurationConstraint_strategy)
def test_cocomm_configurationconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=coCoMM_ConfigurationConstraint_strategy)
def test_cocomm_configurationconstraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_ConfigurationConstraint_strategy)
def test_cocomm_configurationconstraint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=coCoMM_SolutionConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_solutionconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_SolutionConstraint)



@given(instance=coCoMM_SolutionConstraint_strategy)
def test_cocomm_solutionconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM_CrossModelConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_crossmodelconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossModelConstraint)

@given(instance=coCoMM_CoCo_strategy)
@settings(max_examples=50)
def test_cocomm_coco_instantiation(instance):
    assert isinstance(instance, coCoMM_CoCo)



@given(instance=coCoMM_CoCo_strategy)
def test_cocomm_coco_configScenario_setter(instance):
    original = instance.configScenario
    instance.configScenario = original
    assert instance.configScenario == original



@given(instance=coCoMM_CoCo_strategy)
def test_cocomm_coco_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_CoCo_strategy)
def test_cocomm_coco_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM_CTConstraintExpression_strategy)
@settings(max_examples=50)
def test_cocomm_ctconstraintexpression_instantiation(instance):
    assert isinstance(instance, coCoMM_CTConstraintExpression)



@given(instance=coCoMM_CTConstraintExpression_strategy)
def test_cocomm_ctconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=coCoMM_AttributeType_strategy)
@settings(max_examples=50)
def test_cocomm_attributetype_instantiation(instance):
    assert isinstance(instance, coCoMM_AttributeType)



@given(instance=coCoMM_AttributeType_strategy)
def test_cocomm_attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coCoMM_AttributeType_strategy)
def test_cocomm_attributetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_AttributeType_strategy)
def test_cocomm_attributetype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=coCoMM_FeatureAttribute_strategy)
@settings(max_examples=50)
def test_cocomm_featureattribute_instantiation(instance):
    assert isinstance(instance, coCoMM_FeatureAttribute)



@given(instance=coCoMM_FeatureAttribute_strategy)
def test_cocomm_featureattribute_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=coCoMM_FeatureAttribute_strategy)
def test_cocomm_featureattribute_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original



@given(instance=coCoMM_FeatureAttribute_strategy)
def test_cocomm_featureattribute_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=coCoMM_TreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_treeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_TreeConstraint)



@given(instance=coCoMM_TreeConstraint_strategy)
def test_cocomm_treeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM_CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm_crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM_CrossTreeConstraint)

@given(instance=coCoMM_Feature_strategy)
@settings(max_examples=50)
def test_cocomm_feature_instantiation(instance):
    assert isinstance(instance, coCoMM_Feature)



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=coCoMM_Feature_strategy)
def test_cocomm_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

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



@given(instance=coCoMM_FeatureModel_strategy)
def test_cocomm_featuremodel_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
