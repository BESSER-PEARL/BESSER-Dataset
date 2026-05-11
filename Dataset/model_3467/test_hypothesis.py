import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    coCoMM::FiniteDomainSCValue,
    coCoMM::Config,
    SolutionConstraint,
    coCoMM::OptimizationSC,
    coCoMM::FiniteDomainSC,
    coCoMM::SelectionStateSC,
    coCoMM::CMConstraintExpression,
    coCoMM::Stakeholder,
    coCoMM::Project,
    coCoMM::SolutionConstraint,
    coCoMM::CrossModelConstraint,
    coCoMM::CoCo,
    coCoMM::HardLimitDRExpression,
    coCoMM::HardLimitSC,
    coCoMM::AttributeType,
    coCoMM::FeatureAttribute,
    coCoMM::TreeConstraint,
    coCoMM::CrossTreeConstraint,
    coCoMM::Feature,
    coCoMM::CTConstraintExpression,
    coCoMM::FeatureAttributeElement,
    coCoMM::AttributeTypeElement,
    coCoMM::FeatureModel,
    SelectionStateSCType,
    DataType,
    CMConstraintType,
    ConfigScenarioType,
    TreeConstraintType,
    SCType,
    ConfigType,
    CTConstraintType,
    HardLimitSCOp,
    OptimizationSCFunct,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cocomm::finitedomainscvalue_is_not_abstract():
    assert not inspect.isabstract(coCoMM::FiniteDomainSCValue)


def test_cocomm::finitedomainscvalue_constructor_exists():
    assert callable(coCoMM::FiniteDomainSCValue.__init__)


def test_cocomm::finitedomainscvalue_constructor_args():
    sig = inspect.signature(coCoMM::FiniteDomainSCValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cocomm::finitedomainscvalue_has_value():
    assert hasattr(coCoMM::FiniteDomainSCValue, "value")
    descriptor = None
    for klass in coCoMM::FiniteDomainSCValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::config_is_not_abstract():
    assert not inspect.isabstract(coCoMM::Config)


def test_cocomm::config_constructor_exists():
    assert callable(coCoMM::Config.__init__)


def test_cocomm::config_constructor_args():
    sig = inspect.signature(coCoMM::Config.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm::config_has_selected():
    assert hasattr(coCoMM::Config, "selected")
    descriptor = None
    for klass in coCoMM::Config.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::config_has_type():
    assert hasattr(coCoMM::Config, "type")
    descriptor = None
    for klass in coCoMM::Config.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_solutionconstraint_is_not_abstract():
    assert not inspect.isabstract(SolutionConstraint)


def test_solutionconstraint_constructor_exists():
    assert callable(SolutionConstraint.__init__)


def test_solutionconstraint_constructor_args():
    sig = inspect.signature(SolutionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm::optimizationsc_is_not_abstract():
    assert not inspect.isabstract(coCoMM::OptimizationSC)


def test_cocomm::optimizationsc_constructor_exists():
    assert callable(coCoMM::OptimizationSC.__init__)


def test_cocomm::optimizationsc_constructor_args():
    sig = inspect.signature(coCoMM::OptimizationSC.__init__)
    params = list(sig.parameters.keys())
    assert "funct" in params, "Missing parameter 'funct'"

def test_cocomm::optimizationsc_has_funct():
    assert hasattr(coCoMM::OptimizationSC, "funct")
    descriptor = None
    for klass in coCoMM::OptimizationSC.__mro__:
        if "funct" in klass.__dict__:
            descriptor = klass.__dict__["funct"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::finitedomainsc_is_not_abstract():
    assert not inspect.isabstract(coCoMM::FiniteDomainSC)


def test_cocomm::finitedomainsc_constructor_exists():
    assert callable(coCoMM::FiniteDomainSC.__init__)


def test_cocomm::finitedomainsc_constructor_args():
    sig = inspect.signature(coCoMM::FiniteDomainSC.__init__)
    params = list(sig.parameters.keys())



def test_cocomm::selectionstatesc_is_not_abstract():
    assert not inspect.isabstract(coCoMM::SelectionStateSC)


def test_cocomm::selectionstatesc_constructor_exists():
    assert callable(coCoMM::SelectionStateSC.__init__)


def test_cocomm::selectionstatesc_constructor_args():
    sig = inspect.signature(coCoMM::SelectionStateSC.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"

def test_cocomm::selectionstatesc_has_state():
    assert hasattr(coCoMM::SelectionStateSC, "state")
    descriptor = None
    for klass in coCoMM::SelectionStateSC.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::cmconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM::CMConstraintExpression)


def test_cocomm::cmconstraintexpression_constructor_exists():
    assert callable(coCoMM::CMConstraintExpression.__init__)


def test_cocomm::cmconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM::CMConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm::cmconstraintexpression_has_op():
    assert hasattr(coCoMM::CMConstraintExpression, "op")
    descriptor = None
    for klass in coCoMM::CMConstraintExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::stakeholder_is_not_abstract():
    assert not inspect.isabstract(coCoMM::Stakeholder)


def test_cocomm::stakeholder_constructor_exists():
    assert callable(coCoMM::Stakeholder.__init__)


def test_cocomm::stakeholder_constructor_args():
    sig = inspect.signature(coCoMM::Stakeholder.__init__)
    params = list(sig.parameters.keys())
    assert "job" in params, "Missing parameter 'job'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::stakeholder_has_job():
    assert hasattr(coCoMM::Stakeholder, "job")
    descriptor = None
    for klass in coCoMM::Stakeholder.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::stakeholder_has_name():
    assert hasattr(coCoMM::Stakeholder, "name")
    descriptor = None
    for klass in coCoMM::Stakeholder.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::project_is_not_abstract():
    assert not inspect.isabstract(coCoMM::Project)


def test_cocomm::project_constructor_exists():
    assert callable(coCoMM::Project.__init__)


def test_cocomm::project_constructor_args():
    sig = inspect.signature(coCoMM::Project.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "target" in params, "Missing parameter 'target'"
    assert "date" in params, "Missing parameter 'date'"

def test_cocomm::project_has_name():
    assert hasattr(coCoMM::Project, "name")
    descriptor = None
    for klass in coCoMM::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::project_has_target():
    assert hasattr(coCoMM::Project, "target")
    descriptor = None
    for klass in coCoMM::Project.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::project_has_date():
    assert hasattr(coCoMM::Project, "date")
    descriptor = None
    for klass in coCoMM::Project.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::solutionconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM::SolutionConstraint)


def test_cocomm::solutionconstraint_constructor_exists():
    assert callable(coCoMM::SolutionConstraint.__init__)


def test_cocomm::solutionconstraint_constructor_args():
    sig = inspect.signature(coCoMM::SolutionConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm::solutionconstraint_has_type():
    assert hasattr(coCoMM::SolutionConstraint, "type")
    descriptor = None
    for klass in coCoMM::SolutionConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::crossmodelconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM::CrossModelConstraint)


def test_cocomm::crossmodelconstraint_constructor_exists():
    assert callable(coCoMM::CrossModelConstraint.__init__)


def test_cocomm::crossmodelconstraint_constructor_args():
    sig = inspect.signature(coCoMM::CrossModelConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm::coco_is_not_abstract():
    assert not inspect.isabstract(coCoMM::CoCo)


def test_cocomm::coco_constructor_exists():
    assert callable(coCoMM::CoCo.__init__)


def test_cocomm::coco_constructor_args():
    sig = inspect.signature(coCoMM::CoCo.__init__)
    params = list(sig.parameters.keys())
    assert "configScenario" in params, "Missing parameter 'configScenario'"

def test_cocomm::coco_has_configScenario():
    assert hasattr(coCoMM::CoCo, "configScenario")
    descriptor = None
    for klass in coCoMM::CoCo.__mro__:
        if "configScenario" in klass.__dict__:
            descriptor = klass.__dict__["configScenario"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::hardlimitdrexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM::HardLimitDRExpression)


def test_cocomm::hardlimitdrexpression_constructor_exists():
    assert callable(coCoMM::HardLimitDRExpression.__init__)


def test_cocomm::hardlimitdrexpression_constructor_args():
    sig = inspect.signature(coCoMM::HardLimitDRExpression.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm::hardlimitdrexpression_has_value():
    assert hasattr(coCoMM::HardLimitDRExpression, "value")
    descriptor = None
    for klass in coCoMM::HardLimitDRExpression.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::hardlimitdrexpression_has_op():
    assert hasattr(coCoMM::HardLimitDRExpression, "op")
    descriptor = None
    for klass in coCoMM::HardLimitDRExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::hardlimitsc_is_not_abstract():
    assert not inspect.isabstract(coCoMM::HardLimitSC)


def test_cocomm::hardlimitsc_constructor_exists():
    assert callable(coCoMM::HardLimitSC.__init__)


def test_cocomm::hardlimitsc_constructor_args():
    sig = inspect.signature(coCoMM::HardLimitSC.__init__)
    params = list(sig.parameters.keys())



def test_cocomm::attributetype_is_not_abstract():
    assert not inspect.isabstract(coCoMM::AttributeType)


def test_cocomm::attributetype_constructor_exists():
    assert callable(coCoMM::AttributeType.__init__)


def test_cocomm::attributetype_constructor_args():
    sig = inspect.signature(coCoMM::AttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::attributetype_has_id():
    assert hasattr(coCoMM::AttributeType, "id")
    descriptor = None
    for klass in coCoMM::AttributeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::attributetype_has_name():
    assert hasattr(coCoMM::AttributeType, "name")
    descriptor = None
    for klass in coCoMM::AttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::featureattribute_is_not_abstract():
    assert not inspect.isabstract(coCoMM::FeatureAttribute)


def test_cocomm::featureattribute_constructor_exists():
    assert callable(coCoMM::FeatureAttribute.__init__)


def test_cocomm::featureattribute_constructor_args():
    sig = inspect.signature(coCoMM::FeatureAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::featureattribute_has_name():
    assert hasattr(coCoMM::FeatureAttribute, "name")
    descriptor = None
    for klass in coCoMM::FeatureAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::treeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM::TreeConstraint)


def test_cocomm::treeconstraint_constructor_exists():
    assert callable(coCoMM::TreeConstraint.__init__)


def test_cocomm::treeconstraint_constructor_args():
    sig = inspect.signature(coCoMM::TreeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cocomm::treeconstraint_has_type():
    assert hasattr(coCoMM::TreeConstraint, "type")
    descriptor = None
    for klass in coCoMM::TreeConstraint.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::crosstreeconstraint_is_not_abstract():
    assert not inspect.isabstract(coCoMM::CrossTreeConstraint)


def test_cocomm::crosstreeconstraint_constructor_exists():
    assert callable(coCoMM::CrossTreeConstraint.__init__)


def test_cocomm::crosstreeconstraint_constructor_args():
    sig = inspect.signature(coCoMM::CrossTreeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_cocomm::feature_is_not_abstract():
    assert not inspect.isabstract(coCoMM::Feature)


def test_cocomm::feature_constructor_exists():
    assert callable(coCoMM::Feature.__init__)


def test_cocomm::feature_constructor_args():
    sig = inspect.signature(coCoMM::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "abstract" in params, "Missing parameter 'abstract'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::feature_has_id():
    assert hasattr(coCoMM::Feature, "id")
    descriptor = None
    for klass in coCoMM::Feature.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::feature_has_abstract():
    assert hasattr(coCoMM::Feature, "abstract")
    descriptor = None
    for klass in coCoMM::Feature.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::feature_has_mandatory():
    assert hasattr(coCoMM::Feature, "mandatory")
    descriptor = None
    for klass in coCoMM::Feature.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::feature_has_name():
    assert hasattr(coCoMM::Feature, "name")
    descriptor = None
    for klass in coCoMM::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::ctconstraintexpression_is_not_abstract():
    assert not inspect.isabstract(coCoMM::CTConstraintExpression)


def test_cocomm::ctconstraintexpression_constructor_exists():
    assert callable(coCoMM::CTConstraintExpression.__init__)


def test_cocomm::ctconstraintexpression_constructor_args():
    sig = inspect.signature(coCoMM::CTConstraintExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cocomm::ctconstraintexpression_has_op():
    assert hasattr(coCoMM::CTConstraintExpression, "op")
    descriptor = None
    for klass in coCoMM::CTConstraintExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::featureattributeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM::FeatureAttributeElement)


def test_cocomm::featureattributeelement_constructor_exists():
    assert callable(coCoMM::FeatureAttributeElement.__init__)


def test_cocomm::featureattributeelement_constructor_args():
    sig = inspect.signature(coCoMM::FeatureAttributeElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cocomm::featureattributeelement_has_value():
    assert hasattr(coCoMM::FeatureAttributeElement, "value")
    descriptor = None
    for klass in coCoMM::FeatureAttributeElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::attributetypeelement_is_not_abstract():
    assert not inspect.isabstract(coCoMM::AttributeTypeElement)


def test_cocomm::attributetypeelement_constructor_exists():
    assert callable(coCoMM::AttributeTypeElement.__init__)


def test_cocomm::attributetypeelement_constructor_args():
    sig = inspect.signature(coCoMM::AttributeTypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::attributetypeelement_has_dataType():
    assert hasattr(coCoMM::AttributeTypeElement, "dataType")
    descriptor = None
    for klass in coCoMM::AttributeTypeElement.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::attributetypeelement_has_name():
    assert hasattr(coCoMM::AttributeTypeElement, "name")
    descriptor = None
    for klass in coCoMM::AttributeTypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cocomm::featuremodel_is_not_abstract():
    assert not inspect.isabstract(coCoMM::FeatureModel)


def test_cocomm::featuremodel_constructor_exists():
    assert callable(coCoMM::FeatureModel.__init__)


def test_cocomm::featuremodel_constructor_args():
    sig = inspect.signature(coCoMM::FeatureModel.__init__)
    params = list(sig.parameters.keys())
    assert "isDomain" in params, "Missing parameter 'isDomain'"
    assert "name" in params, "Missing parameter 'name'"

def test_cocomm::featuremodel_has_isDomain():
    assert hasattr(coCoMM::FeatureModel, "isDomain")
    descriptor = None
    for klass in coCoMM::FeatureModel.__mro__:
        if "isDomain" in klass.__dict__:
            descriptor = klass.__dict__["isDomain"]
            break
    assert isinstance(descriptor, property)

def test_cocomm::featuremodel_has_name():
    assert hasattr(coCoMM::FeatureModel, "name")
    descriptor = None
    for klass in coCoMM::FeatureModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_selectionstatesctype_exists():
    # Check that the Enumeration exists
    assert SelectionStateSCType is not None

def test_selectionstatesctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SelectionStateSCType]
    expected_literals = [
        "preferred",
        "forbidden",
        "mandatory",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SelectionStateSCType"

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "boolean",
        "string",
        "int",
        "double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"

def test_cmconstrainttype_exists():
    # Check that the Enumeration exists
    assert CMConstraintType is not None

def test_cmconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CMConstraintType]
    expected_literals = [
        "implies",
        "or_",
        "and_",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CMConstraintType"

def test_configscenariotype_exists():
    # Check that the Enumeration exists
    assert ConfigScenarioType is not None

def test_configscenariotype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigScenarioType]
    expected_literals = [
        "fsgPreferences",
        "fmPreferences",
        "fsgConflicts",
        "fmSearch",
        "fsgSearch",
        "fmConflicts",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConfigScenarioType"

def test_treeconstrainttype_exists():
    # Check that the Enumeration exists
    assert TreeConstraintType is not None

def test_treeconstrainttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TreeConstraintType]
    expected_literals = [
        "Or",
        "And",
        "Alternative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TreeConstraintType"

def test_sctype_exists():
    # Check that the Enumeration exists
    assert SCType is not None

def test_sctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SCType]
    expected_literals = [
        "selectionState",
        "optimization",
        "finiteDomain",
        "hardLimit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SCType"

def test_configtype_exists():
    # Check that the Enumeration exists
    assert ConfigType is not None

def test_configtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConfigType]
    expected_literals = [
        "input",
        "output",
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
        "and_",
        "implies",
        "or_",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CTConstraintType"

def test_hardlimitscop_exists():
    # Check that the Enumeration exists
    assert HardLimitSCOp is not None

def test_hardlimitscop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HardLimitSCOp]
    expected_literals = [
        "eq",
        "geq",
        "gt",
        "leq",
        "lt",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HardLimitSCOp"

def test_optimizationscfunct_exists():
    # Check that the Enumeration exists
    assert OptimizationSCFunct is not None

def test_optimizationscfunct_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OptimizationSCFunct]
    expected_literals = [
        "maximize",
        "minimize",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OptimizationSCFunct"


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
coCoMM::FiniteDomainSCValue_strategy = st.builds(
    coCoMM::FiniteDomainSCValue,
    value=
        safe_text
)
coCoMM::Config_strategy = st.builds(
    coCoMM::Config,
    selected=
        st.booleans(),
    type=
        safe_text
)
SolutionConstraint_strategy = st.builds(
    SolutionConstraint,
)
coCoMM::OptimizationSC_strategy = st.builds(
    coCoMM::OptimizationSC,
    funct=
        safe_text
)
coCoMM::FiniteDomainSC_strategy = st.builds(
    coCoMM::FiniteDomainSC,
)
coCoMM::SelectionStateSC_strategy = st.builds(
    coCoMM::SelectionStateSC,
    state=
        safe_text
)
coCoMM::CMConstraintExpression_strategy = st.builds(
    coCoMM::CMConstraintExpression,
    op=
        safe_text
)
coCoMM::Stakeholder_strategy = st.builds(
    coCoMM::Stakeholder,
    job=
        safe_text,
    name=
        safe_text
)
coCoMM::Project_strategy = st.builds(
    coCoMM::Project,
    name=
        safe_text,
    target=
        st.booleans(),
    date=
        st.dates()
)
coCoMM::SolutionConstraint_strategy = st.builds(
    coCoMM::SolutionConstraint,
    type=
        safe_text
)
coCoMM::CrossModelConstraint_strategy = st.builds(
    coCoMM::CrossModelConstraint,
)
coCoMM::CoCo_strategy = st.builds(
    coCoMM::CoCo,
    configScenario=
        safe_text
)
coCoMM::HardLimitDRExpression_strategy = st.builds(
    coCoMM::HardLimitDRExpression,
    value=
        safe_text,
    op=
        safe_text
)
coCoMM::HardLimitSC_strategy = st.builds(
    coCoMM::HardLimitSC,
)
coCoMM::AttributeType_strategy = st.builds(
    coCoMM::AttributeType,
    id=
        safe_text,
    name=
        safe_text
)
coCoMM::FeatureAttribute_strategy = st.builds(
    coCoMM::FeatureAttribute,
    name=
        safe_text
)
coCoMM::TreeConstraint_strategy = st.builds(
    coCoMM::TreeConstraint,
    type=
        safe_text
)
coCoMM::CrossTreeConstraint_strategy = st.builds(
    coCoMM::CrossTreeConstraint,
)
coCoMM::Feature_strategy = st.builds(
    coCoMM::Feature,
    id=
        safe_text,
    abstract=
        st.booleans(),
    mandatory=
        st.booleans(),
    name=
        safe_text
)
coCoMM::CTConstraintExpression_strategy = st.builds(
    coCoMM::CTConstraintExpression,
    op=
        safe_text
)
coCoMM::FeatureAttributeElement_strategy = st.builds(
    coCoMM::FeatureAttributeElement,
    value=
        safe_text
)
coCoMM::AttributeTypeElement_strategy = st.builds(
    coCoMM::AttributeTypeElement,
    dataType=
        safe_text,
    name=
        safe_text
)
coCoMM::FeatureModel_strategy = st.builds(
    coCoMM::FeatureModel,
    isDomain=
        st.booleans(),
    name=
        safe_text
)

@given(instance=coCoMM::FiniteDomainSCValue_strategy)
@settings(max_examples=50)
def test_cocomm::finitedomainscvalue_instantiation(instance):
    assert isinstance(instance, coCoMM::FiniteDomainSCValue)

@given(instance=coCoMM::FiniteDomainSCValue_strategy)
def test_cocomm::finitedomainscvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=coCoMM::FiniteDomainSCValue_strategy)
def test_cocomm::finitedomainscvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=coCoMM::Config_strategy)
@settings(max_examples=50)
def test_cocomm::config_instantiation(instance):
    assert isinstance(instance, coCoMM::Config)

@given(instance=coCoMM::Config_strategy)
def test_cocomm::config_selected_type(instance):
    assert isinstance(instance.selected, bool)


@given(instance=coCoMM::Config_strategy)
def test_cocomm::config_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=coCoMM::Config_strategy)
def test_cocomm::config_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=coCoMM::Config_strategy)
def test_cocomm::config_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SolutionConstraint_strategy)
@settings(max_examples=50)
def test_solutionconstraint_instantiation(instance):
    assert isinstance(instance, SolutionConstraint)

@given(instance=coCoMM::OptimizationSC_strategy)
@settings(max_examples=50)
def test_cocomm::optimizationsc_instantiation(instance):
    assert isinstance(instance, coCoMM::OptimizationSC)

@given(instance=coCoMM::OptimizationSC_strategy)
def test_cocomm::optimizationsc_funct_type(instance):
    assert isinstance(instance.funct, str)


@given(instance=coCoMM::OptimizationSC_strategy)
def test_cocomm::optimizationsc_funct_setter(instance):
    original = instance.funct
    instance.funct = original
    assert instance.funct == original

@given(instance=coCoMM::FiniteDomainSC_strategy)
@settings(max_examples=50)
def test_cocomm::finitedomainsc_instantiation(instance):
    assert isinstance(instance, coCoMM::FiniteDomainSC)

@given(instance=coCoMM::SelectionStateSC_strategy)
@settings(max_examples=50)
def test_cocomm::selectionstatesc_instantiation(instance):
    assert isinstance(instance, coCoMM::SelectionStateSC)

@given(instance=coCoMM::SelectionStateSC_strategy)
def test_cocomm::selectionstatesc_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=coCoMM::SelectionStateSC_strategy)
def test_cocomm::selectionstatesc_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=coCoMM::CMConstraintExpression_strategy)
@settings(max_examples=50)
def test_cocomm::cmconstraintexpression_instantiation(instance):
    assert isinstance(instance, coCoMM::CMConstraintExpression)

@given(instance=coCoMM::CMConstraintExpression_strategy)
def test_cocomm::cmconstraintexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=coCoMM::CMConstraintExpression_strategy)
def test_cocomm::cmconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=coCoMM::Stakeholder_strategy)
@settings(max_examples=50)
def test_cocomm::stakeholder_instantiation(instance):
    assert isinstance(instance, coCoMM::Stakeholder)

@given(instance=coCoMM::Stakeholder_strategy)
def test_cocomm::stakeholder_job_type(instance):
    assert isinstance(instance.job, str)


@given(instance=coCoMM::Stakeholder_strategy)
def test_cocomm::stakeholder_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original

@given(instance=coCoMM::Stakeholder_strategy)
def test_cocomm::stakeholder_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::Stakeholder_strategy)
def test_cocomm::stakeholder_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::Project_strategy)
@settings(max_examples=50)
def test_cocomm::project_instantiation(instance):
    assert isinstance(instance, coCoMM::Project)

@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_target_type(instance):
    assert isinstance(instance.target, bool)


@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=coCoMM::Project_strategy)
def test_cocomm::project_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=coCoMM::SolutionConstraint_strategy)
@settings(max_examples=50)
def test_cocomm::solutionconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM::SolutionConstraint)

@given(instance=coCoMM::SolutionConstraint_strategy)
def test_cocomm::solutionconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=coCoMM::SolutionConstraint_strategy)
def test_cocomm::solutionconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM::CrossModelConstraint_strategy)
@settings(max_examples=50)
def test_cocomm::crossmodelconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM::CrossModelConstraint)

@given(instance=coCoMM::CoCo_strategy)
@settings(max_examples=50)
def test_cocomm::coco_instantiation(instance):
    assert isinstance(instance, coCoMM::CoCo)

@given(instance=coCoMM::CoCo_strategy)
def test_cocomm::coco_configScenario_type(instance):
    assert isinstance(instance.configScenario, str)


@given(instance=coCoMM::CoCo_strategy)
def test_cocomm::coco_configScenario_setter(instance):
    original = instance.configScenario
    instance.configScenario = original
    assert instance.configScenario == original

@given(instance=coCoMM::HardLimitDRExpression_strategy)
@settings(max_examples=50)
def test_cocomm::hardlimitdrexpression_instantiation(instance):
    assert isinstance(instance, coCoMM::HardLimitDRExpression)

@given(instance=coCoMM::HardLimitDRExpression_strategy)
def test_cocomm::hardlimitdrexpression_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=coCoMM::HardLimitDRExpression_strategy)
def test_cocomm::hardlimitdrexpression_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=coCoMM::HardLimitDRExpression_strategy)
def test_cocomm::hardlimitdrexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=coCoMM::HardLimitDRExpression_strategy)
def test_cocomm::hardlimitdrexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=coCoMM::HardLimitSC_strategy)
@settings(max_examples=50)
def test_cocomm::hardlimitsc_instantiation(instance):
    assert isinstance(instance, coCoMM::HardLimitSC)

@given(instance=coCoMM::AttributeType_strategy)
@settings(max_examples=50)
def test_cocomm::attributetype_instantiation(instance):
    assert isinstance(instance, coCoMM::AttributeType)

@given(instance=coCoMM::AttributeType_strategy)
def test_cocomm::attributetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=coCoMM::AttributeType_strategy)
def test_cocomm::attributetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=coCoMM::AttributeType_strategy)
def test_cocomm::attributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::AttributeType_strategy)
def test_cocomm::attributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::FeatureAttribute_strategy)
@settings(max_examples=50)
def test_cocomm::featureattribute_instantiation(instance):
    assert isinstance(instance, coCoMM::FeatureAttribute)

@given(instance=coCoMM::FeatureAttribute_strategy)
def test_cocomm::featureattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::FeatureAttribute_strategy)
def test_cocomm::featureattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::TreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm::treeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM::TreeConstraint)

@given(instance=coCoMM::TreeConstraint_strategy)
def test_cocomm::treeconstraint_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=coCoMM::TreeConstraint_strategy)
def test_cocomm::treeconstraint_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=coCoMM::CrossTreeConstraint_strategy)
@settings(max_examples=50)
def test_cocomm::crosstreeconstraint_instantiation(instance):
    assert isinstance(instance, coCoMM::CrossTreeConstraint)

@given(instance=coCoMM::Feature_strategy)
@settings(max_examples=50)
def test_cocomm::feature_instantiation(instance):
    assert isinstance(instance, coCoMM::Feature)

@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_mandatory_type(instance):
    assert isinstance(instance.mandatory, bool)


@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::Feature_strategy)
def test_cocomm::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::CTConstraintExpression_strategy)
@settings(max_examples=50)
def test_cocomm::ctconstraintexpression_instantiation(instance):
    assert isinstance(instance, coCoMM::CTConstraintExpression)

@given(instance=coCoMM::CTConstraintExpression_strategy)
def test_cocomm::ctconstraintexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=coCoMM::CTConstraintExpression_strategy)
def test_cocomm::ctconstraintexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=coCoMM::FeatureAttributeElement_strategy)
@settings(max_examples=50)
def test_cocomm::featureattributeelement_instantiation(instance):
    assert isinstance(instance, coCoMM::FeatureAttributeElement)

@given(instance=coCoMM::FeatureAttributeElement_strategy)
def test_cocomm::featureattributeelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=coCoMM::FeatureAttributeElement_strategy)
def test_cocomm::featureattributeelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=coCoMM::AttributeTypeElement_strategy)
@settings(max_examples=50)
def test_cocomm::attributetypeelement_instantiation(instance):
    assert isinstance(instance, coCoMM::AttributeTypeElement)

@given(instance=coCoMM::AttributeTypeElement_strategy)
def test_cocomm::attributetypeelement_dataType_type(instance):
    assert isinstance(instance.dataType, str)


@given(instance=coCoMM::AttributeTypeElement_strategy)
def test_cocomm::attributetypeelement_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=coCoMM::AttributeTypeElement_strategy)
def test_cocomm::attributetypeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::AttributeTypeElement_strategy)
def test_cocomm::attributetypeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=coCoMM::FeatureModel_strategy)
@settings(max_examples=50)
def test_cocomm::featuremodel_instantiation(instance):
    assert isinstance(instance, coCoMM::FeatureModel)

@given(instance=coCoMM::FeatureModel_strategy)
def test_cocomm::featuremodel_isDomain_type(instance):
    assert isinstance(instance.isDomain, bool)


@given(instance=coCoMM::FeatureModel_strategy)
def test_cocomm::featuremodel_isDomain_setter(instance):
    original = instance.isDomain
    instance.isDomain = original
    assert instance.isDomain == original

@given(instance=coCoMM::FeatureModel_strategy)
def test_cocomm::featuremodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=coCoMM::FeatureModel_strategy)
def test_cocomm::featuremodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
