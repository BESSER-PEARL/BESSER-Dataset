import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Connector,
    Parameter,
    DomainModel_,
    avm::modelica::ModelicaModel,
    avm::WorkflowTaskBase,
    avm::TestBenchValueBase,
    avm::ContainerInstanceBase,
    TestBenchValueBase,
    ContainerInstanceBase,
    avm::Settings,
    avm::Workflow,
    WorkflowTaskBase,
    avm::ExecutionTask,
    avm::InterpreterTask,
    avm::TopLevelSystemUnderTest,
    avm::TestBench,
    avm::Operand,
    Formula,
    avm::ComplexFormula,
    avm::SimpleFormula,
    avm::TestInjectionPoint,
    avm::Metric,
    avm::Parameter,
    avm::PortMapTarget,
    avm::ComponentPrimitivePropertyInstance,
    DesignSpaceContainer,
    avm::Alternative,
    avm::Optional,
    Container,
    avm::DesignSpaceContainer,
    avm::Compound,
    avm::ConnectorCompositionTarget,
    avm::DesignDomainFeature,
    avm::Container,
    avm::Design,
    avm::ComponentInstance,
    avm::DomainModelMetric,
    DistributionRestriction,
    avm::Proprietary,
    avm::DoDDistributionStatement,
    avm::ITAR,
    avm::SecurityClassification,
    ProbabilisticValue,
    avm::NormalDistribution,
    Property,
    avm::CompoundProperty,
    avm::PrimitiveProperty,
    avm::UniformDistribution,
    avm::DomainModelParameter,
    Port,
    avm::AbstractPort,
    avm::DomainModelPort,
    PortMapTarget,
    avm::ComponentPortInstance,
    avm::ConnectorFeature,
    avm::assemblyDetail,
    ConnectorCompositionTarget,
    avm::ComponentConnectorInstance,
    avm::ValueNode,
    ValueExpressionType,
    avm::ParametricEnumeratedValue,
    avm::DerivedValue,
    avm::ProbabilisticValue,
    avm::CalculatedValue,
    avm::ParametricValue,
    avm::FixedValue,
    avm::DataSource,
    avm::ValueExpressionType,
    avm::cyber::CyberModel,
    manufacturing::avm::Value,
    avm::manufacturing::ManufacturingModel,
    avm::adamsCar::FileReference,
    adamsCar::avm::Value,
    FileReference,
    avm::adamsCar::AdamsCarModel,
    Axis,
    KinematicJointSpec,
    avm::cad::RevoluteJointSpec,
    cad::avm::ComponentInstance,
    DesignDomainFeature,
    avm::cad::AssemblyRoot,
    ConnectorFeature,
    avm::cad::KinematicJointSpec,
    avm::cad::GuideDatum,
    avm::cad::PlaneReference,
    PlaneReference,
    avm::cad::TranslationalJointSpec,
    avm::cad::CustomGeometryInput,
    CustomGeometryInput,
    Geometry3D,
    avm::cad::Sphere,
    avm::cad::ExtrudedGeometry,
    avm::cad::Surface,
    Point,
    avm::cad::PointReference,
    AnalysisConstruct,
    avm::cad::Geometry,
    Plane,
    cad::avm::Value,
    PointReference,
    Geometry2D,
    avm::cad::Polygon,
    avm::cad::Circle,
    Geometry,
    avm::cad::CustomGeometry,
    avm::cad::Geometry3D,
    avm::cad::Geometry2D,
    Datum,
    avm::cad::Plane,
    avm::cad::Axis,
    avm::cad::Point,
    avm::cad::CoordinateSystem,
    avm::cad::CADModel,
    Settings,
    avm::modelica::SolverSettings,
    avm::modelica::Limit,
    DomainModelMetric,
    avm::manufacturing::Metric,
    avm::cad::Metric,
    avm::modelica::Metric,
    modelica::avm::Value,
    DomainModelParameter,
    avm::modelica::Redeclare,
    avm::adamsCar::Parameter,
    avm::manufacturing::Parameter,
    avm::cad::Parameter,
    avm::modelica::Parameter,
    DomainModelPort,
    avm::cad::Datum,
    avm::modelica::Connector,
    Redeclare,
    Limit,
    Metric,
    ValueNode,
    avm::ValueFlowMux,
    avm::Value,
    avm::AnalysisConstruct,
    avm::Port,
    avm::DistributionRestriction,
    avm::Connector,
    avm::Resource,
    avm::Property,
    avm::Formula,
    avm::DomainModel_,
    avm::Component,
    ModelType,
    DoDDistributionStatementEnum,
    RedeclareTypeEnum,
    DataTypeEnum,
    GeometryQualifierEnum,
    BoundTypeEnum,
    PartIntersectionEnum,
    DimensionTypeEnum,
    CustomGeometryInputOperationEnum,
    IntervalMethod,
    CalculationTypeEnum,
    SimpleFormulaOperation,
    JobManagerToolSelection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connector_is_not_abstract():
    assert not inspect.isabstract(Connector)


def test_connector_constructor_exists():
    assert callable(Connector.__init__)


def test_connector_constructor_args():
    sig = inspect.signature(Connector.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel__is_not_abstract():
    assert not inspect.isabstract(DomainModel_)


def test_domainmodel__constructor_exists():
    assert callable(DomainModel_.__init__)


def test_domainmodel__constructor_args():
    sig = inspect.signature(DomainModel_.__init__)
    params = list(sig.parameters.keys())



def test_avm::modelica::modelicamodel_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::ModelicaModel)


def test_avm::modelica::modelicamodel_constructor_exists():
    assert callable(avm::modelica::ModelicaModel.__init__)


def test_avm::modelica::modelicamodel_constructor_args():
    sig = inspect.signature(avm::modelica::ModelicaModel.__init__)
    params = list(sig.parameters.keys())
    assert "Class" in params, "Missing parameter 'Class'"

def test_avm::modelica::modelicamodel_has_Class():
    assert hasattr(avm::modelica::ModelicaModel, "Class")
    descriptor = None
    for klass in avm::modelica::ModelicaModel.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)



def test_avm::workflowtaskbase_is_not_abstract():
    assert not inspect.isabstract(avm::WorkflowTaskBase)


def test_avm::workflowtaskbase_constructor_exists():
    assert callable(avm::WorkflowTaskBase.__init__)


def test_avm::workflowtaskbase_constructor_args():
    sig = inspect.signature(avm::WorkflowTaskBase.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::workflowtaskbase_has_Name():
    assert hasattr(avm::WorkflowTaskBase, "Name")
    descriptor = None
    for klass in avm::WorkflowTaskBase.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::testbenchvaluebase_is_not_abstract():
    assert not inspect.isabstract(avm::TestBenchValueBase)


def test_avm::testbenchvaluebase_constructor_exists():
    assert callable(avm::TestBenchValueBase.__init__)


def test_avm::testbenchvaluebase_constructor_args():
    sig = inspect.signature(avm::TestBenchValueBase.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::testbenchvaluebase_has_Name():
    assert hasattr(avm::TestBenchValueBase, "Name")
    descriptor = None
    for klass in avm::TestBenchValueBase.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::testbenchvaluebase_has_YPosition():
    assert hasattr(avm::TestBenchValueBase, "YPosition")
    descriptor = None
    for klass in avm::TestBenchValueBase.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::testbenchvaluebase_has_Notes():
    assert hasattr(avm::TestBenchValueBase, "Notes")
    descriptor = None
    for klass in avm::TestBenchValueBase.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::testbenchvaluebase_has_ID():
    assert hasattr(avm::TestBenchValueBase, "ID")
    descriptor = None
    for klass in avm::TestBenchValueBase.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::testbenchvaluebase_has_XPosition():
    assert hasattr(avm::TestBenchValueBase, "XPosition")
    descriptor = None
    for klass in avm::TestBenchValueBase.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm::containerinstancebase_is_not_abstract():
    assert not inspect.isabstract(avm::ContainerInstanceBase)


def test_avm::containerinstancebase_constructor_exists():
    assert callable(avm::ContainerInstanceBase.__init__)


def test_avm::containerinstancebase_constructor_args():
    sig = inspect.signature(avm::ContainerInstanceBase.__init__)
    params = list(sig.parameters.keys())
    assert "IDinSourceModel" in params, "Missing parameter 'IDinSourceModel'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::containerinstancebase_has_IDinSourceModel():
    assert hasattr(avm::ContainerInstanceBase, "IDinSourceModel")
    descriptor = None
    for klass in avm::ContainerInstanceBase.__mro__:
        if "IDinSourceModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinSourceModel"]
            break
    assert isinstance(descriptor, property)

def test_avm::containerinstancebase_has_YPosition():
    assert hasattr(avm::ContainerInstanceBase, "YPosition")
    descriptor = None
    for klass in avm::ContainerInstanceBase.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::containerinstancebase_has_XPosition():
    assert hasattr(avm::ContainerInstanceBase, "XPosition")
    descriptor = None
    for klass in avm::ContainerInstanceBase.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_testbenchvaluebase_is_not_abstract():
    assert not inspect.isabstract(TestBenchValueBase)


def test_testbenchvaluebase_constructor_exists():
    assert callable(TestBenchValueBase.__init__)


def test_testbenchvaluebase_constructor_args():
    sig = inspect.signature(TestBenchValueBase.__init__)
    params = list(sig.parameters.keys())



def test_containerinstancebase_is_not_abstract():
    assert not inspect.isabstract(ContainerInstanceBase)


def test_containerinstancebase_constructor_exists():
    assert callable(ContainerInstanceBase.__init__)


def test_containerinstancebase_constructor_args():
    sig = inspect.signature(ContainerInstanceBase.__init__)
    params = list(sig.parameters.keys())



def test_avm::settings_is_not_abstract():
    assert not inspect.isabstract(avm::Settings)


def test_avm::settings_constructor_exists():
    assert callable(avm::Settings.__init__)


def test_avm::settings_constructor_args():
    sig = inspect.signature(avm::Settings.__init__)
    params = list(sig.parameters.keys())



def test_avm::workflow_is_not_abstract():
    assert not inspect.isabstract(avm::Workflow)


def test_avm::workflow_constructor_exists():
    assert callable(avm::Workflow.__init__)


def test_avm::workflow_constructor_args():
    sig = inspect.signature(avm::Workflow.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::workflow_has_Name():
    assert hasattr(avm::Workflow, "Name")
    descriptor = None
    for klass in avm::Workflow.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_workflowtaskbase_is_not_abstract():
    assert not inspect.isabstract(WorkflowTaskBase)


def test_workflowtaskbase_constructor_exists():
    assert callable(WorkflowTaskBase.__init__)


def test_workflowtaskbase_constructor_args():
    sig = inspect.signature(WorkflowTaskBase.__init__)
    params = list(sig.parameters.keys())



def test_avm::executiontask_is_not_abstract():
    assert not inspect.isabstract(avm::ExecutionTask)


def test_avm::executiontask_constructor_exists():
    assert callable(avm::ExecutionTask.__init__)


def test_avm::executiontask_constructor_args():
    sig = inspect.signature(avm::ExecutionTask.__init__)
    params = list(sig.parameters.keys())
    assert "Invocation" in params, "Missing parameter 'Invocation'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_avm::executiontask_has_Invocation():
    assert hasattr(avm::ExecutionTask, "Invocation")
    descriptor = None
    for klass in avm::ExecutionTask.__mro__:
        if "Invocation" in klass.__dict__:
            descriptor = klass.__dict__["Invocation"]
            break
    assert isinstance(descriptor, property)

def test_avm::executiontask_has_Description():
    assert hasattr(avm::ExecutionTask, "Description")
    descriptor = None
    for klass in avm::ExecutionTask.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_avm::interpretertask_is_not_abstract():
    assert not inspect.isabstract(avm::InterpreterTask)


def test_avm::interpretertask_constructor_exists():
    assert callable(avm::InterpreterTask.__init__)


def test_avm::interpretertask_constructor_args():
    sig = inspect.signature(avm::InterpreterTask.__init__)
    params = list(sig.parameters.keys())
    assert "Parameters" in params, "Missing parameter 'Parameters'"
    assert "COMName" in params, "Missing parameter 'COMName'"

def test_avm::interpretertask_has_Parameters():
    assert hasattr(avm::InterpreterTask, "Parameters")
    descriptor = None
    for klass in avm::InterpreterTask.__mro__:
        if "Parameters" in klass.__dict__:
            descriptor = klass.__dict__["Parameters"]
            break
    assert isinstance(descriptor, property)

def test_avm::interpretertask_has_COMName():
    assert hasattr(avm::InterpreterTask, "COMName")
    descriptor = None
    for klass in avm::InterpreterTask.__mro__:
        if "COMName" in klass.__dict__:
            descriptor = klass.__dict__["COMName"]
            break
    assert isinstance(descriptor, property)



def test_avm::toplevelsystemundertest_is_not_abstract():
    assert not inspect.isabstract(avm::TopLevelSystemUnderTest)


def test_avm::toplevelsystemundertest_constructor_exists():
    assert callable(avm::TopLevelSystemUnderTest.__init__)


def test_avm::toplevelsystemundertest_constructor_args():
    sig = inspect.signature(avm::TopLevelSystemUnderTest.__init__)
    params = list(sig.parameters.keys())
    assert "DesignID" in params, "Missing parameter 'DesignID'"

def test_avm::toplevelsystemundertest_has_DesignID():
    assert hasattr(avm::TopLevelSystemUnderTest, "DesignID")
    descriptor = None
    for klass in avm::TopLevelSystemUnderTest.__mro__:
        if "DesignID" in klass.__dict__:
            descriptor = klass.__dict__["DesignID"]
            break
    assert isinstance(descriptor, property)



def test_avm::testbench_is_not_abstract():
    assert not inspect.isabstract(avm::TestBench)


def test_avm::testbench_constructor_exists():
    assert callable(avm::TestBench.__init__)


def test_avm::testbench_constructor_args():
    sig = inspect.signature(avm::TestBench.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::testbench_has_Name():
    assert hasattr(avm::TestBench, "Name")
    descriptor = None
    for klass in avm::TestBench.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::operand_is_not_abstract():
    assert not inspect.isabstract(avm::Operand)


def test_avm::operand_constructor_exists():
    assert callable(avm::Operand.__init__)


def test_avm::operand_constructor_args():
    sig = inspect.signature(avm::Operand.__init__)
    params = list(sig.parameters.keys())
    assert "Symbol" in params, "Missing parameter 'Symbol'"

def test_avm::operand_has_Symbol():
    assert hasattr(avm::Operand, "Symbol")
    descriptor = None
    for klass in avm::Operand.__mro__:
        if "Symbol" in klass.__dict__:
            descriptor = klass.__dict__["Symbol"]
            break
    assert isinstance(descriptor, property)



def test_formula_is_not_abstract():
    assert not inspect.isabstract(Formula)


def test_formula_constructor_exists():
    assert callable(Formula.__init__)


def test_formula_constructor_args():
    sig = inspect.signature(Formula.__init__)
    params = list(sig.parameters.keys())



def test_avm::complexformula_is_not_abstract():
    assert not inspect.isabstract(avm::ComplexFormula)


def test_avm::complexformula_constructor_exists():
    assert callable(avm::ComplexFormula.__init__)


def test_avm::complexformula_constructor_args():
    sig = inspect.signature(avm::ComplexFormula.__init__)
    params = list(sig.parameters.keys())
    assert "Expression" in params, "Missing parameter 'Expression'"

def test_avm::complexformula_has_Expression():
    assert hasattr(avm::ComplexFormula, "Expression")
    descriptor = None
    for klass in avm::ComplexFormula.__mro__:
        if "Expression" in klass.__dict__:
            descriptor = klass.__dict__["Expression"]
            break
    assert isinstance(descriptor, property)



def test_avm::simpleformula_is_not_abstract():
    assert not inspect.isabstract(avm::SimpleFormula)


def test_avm::simpleformula_constructor_exists():
    assert callable(avm::SimpleFormula.__init__)


def test_avm::simpleformula_constructor_args():
    sig = inspect.signature(avm::SimpleFormula.__init__)
    params = list(sig.parameters.keys())
    assert "Operation" in params, "Missing parameter 'Operation'"

def test_avm::simpleformula_has_Operation():
    assert hasattr(avm::SimpleFormula, "Operation")
    descriptor = None
    for klass in avm::SimpleFormula.__mro__:
        if "Operation" in klass.__dict__:
            descriptor = klass.__dict__["Operation"]
            break
    assert isinstance(descriptor, property)



def test_avm::testinjectionpoint_is_not_abstract():
    assert not inspect.isabstract(avm::TestInjectionPoint)


def test_avm::testinjectionpoint_constructor_exists():
    assert callable(avm::TestInjectionPoint.__init__)


def test_avm::testinjectionpoint_constructor_args():
    sig = inspect.signature(avm::TestInjectionPoint.__init__)
    params = list(sig.parameters.keys())



def test_avm::metric_is_not_abstract():
    assert not inspect.isabstract(avm::Metric)


def test_avm::metric_constructor_exists():
    assert callable(avm::Metric.__init__)


def test_avm::metric_constructor_args():
    sig = inspect.signature(avm::Metric.__init__)
    params = list(sig.parameters.keys())



def test_avm::parameter_is_not_abstract():
    assert not inspect.isabstract(avm::Parameter)


def test_avm::parameter_constructor_exists():
    assert callable(avm::Parameter.__init__)


def test_avm::parameter_constructor_args():
    sig = inspect.signature(avm::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_avm::portmaptarget_is_not_abstract():
    assert not inspect.isabstract(avm::PortMapTarget)


def test_avm::portmaptarget_constructor_exists():
    assert callable(avm::PortMapTarget.__init__)


def test_avm::portmaptarget_constructor_args():
    sig = inspect.signature(avm::PortMapTarget.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm::portmaptarget_has_ID():
    assert hasattr(avm::PortMapTarget, "ID")
    descriptor = None
    for klass in avm::PortMapTarget.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm::componentprimitivepropertyinstance_is_not_abstract():
    assert not inspect.isabstract(avm::ComponentPrimitivePropertyInstance)


def test_avm::componentprimitivepropertyinstance_constructor_exists():
    assert callable(avm::ComponentPrimitivePropertyInstance.__init__)


def test_avm::componentprimitivepropertyinstance_constructor_args():
    sig = inspect.signature(avm::ComponentPrimitivePropertyInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm::componentprimitivepropertyinstance_has_IDinComponentModel():
    assert hasattr(avm::ComponentPrimitivePropertyInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm::ComponentPrimitivePropertyInstance.__mro__:
        if "IDinComponentModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinComponentModel"]
            break
    assert isinstance(descriptor, property)



def test_designspacecontainer_is_not_abstract():
    assert not inspect.isabstract(DesignSpaceContainer)


def test_designspacecontainer_constructor_exists():
    assert callable(DesignSpaceContainer.__init__)


def test_designspacecontainer_constructor_args():
    sig = inspect.signature(DesignSpaceContainer.__init__)
    params = list(sig.parameters.keys())



def test_avm::alternative_is_not_abstract():
    assert not inspect.isabstract(avm::Alternative)


def test_avm::alternative_constructor_exists():
    assert callable(avm::Alternative.__init__)


def test_avm::alternative_constructor_args():
    sig = inspect.signature(avm::Alternative.__init__)
    params = list(sig.parameters.keys())



def test_avm::optional_is_not_abstract():
    assert not inspect.isabstract(avm::Optional)


def test_avm::optional_constructor_exists():
    assert callable(avm::Optional.__init__)


def test_avm::optional_constructor_args():
    sig = inspect.signature(avm::Optional.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_avm::designspacecontainer_is_not_abstract():
    assert not inspect.isabstract(avm::DesignSpaceContainer)


def test_avm::designspacecontainer_constructor_exists():
    assert callable(avm::DesignSpaceContainer.__init__)


def test_avm::designspacecontainer_constructor_args():
    sig = inspect.signature(avm::DesignSpaceContainer.__init__)
    params = list(sig.parameters.keys())



def test_avm::compound_is_not_abstract():
    assert not inspect.isabstract(avm::Compound)


def test_avm::compound_constructor_exists():
    assert callable(avm::Compound.__init__)


def test_avm::compound_constructor_args():
    sig = inspect.signature(avm::Compound.__init__)
    params = list(sig.parameters.keys())



def test_avm::connectorcompositiontarget_is_not_abstract():
    assert not inspect.isabstract(avm::ConnectorCompositionTarget)


def test_avm::connectorcompositiontarget_constructor_exists():
    assert callable(avm::ConnectorCompositionTarget.__init__)


def test_avm::connectorcompositiontarget_constructor_args():
    sig = inspect.signature(avm::ConnectorCompositionTarget.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm::connectorcompositiontarget_has_ID():
    assert hasattr(avm::ConnectorCompositionTarget, "ID")
    descriptor = None
    for klass in avm::ConnectorCompositionTarget.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm::designdomainfeature_is_not_abstract():
    assert not inspect.isabstract(avm::DesignDomainFeature)


def test_avm::designdomainfeature_constructor_exists():
    assert callable(avm::DesignDomainFeature.__init__)


def test_avm::designdomainfeature_constructor_args():
    sig = inspect.signature(avm::DesignDomainFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm::container_is_not_abstract():
    assert not inspect.isabstract(avm::Container)


def test_avm::container_constructor_exists():
    assert callable(avm::Container.__init__)


def test_avm::container_constructor_args():
    sig = inspect.signature(avm::Container.__init__)
    params = list(sig.parameters.keys())
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::container_has_YPosition():
    assert hasattr(avm::Container, "YPosition")
    descriptor = None
    for klass in avm::Container.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::container_has_XPosition():
    assert hasattr(avm::Container, "XPosition")
    descriptor = None
    for klass in avm::Container.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::container_has_Name():
    assert hasattr(avm::Container, "Name")
    descriptor = None
    for klass in avm::Container.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::design_is_not_abstract():
    assert not inspect.isabstract(avm::Design)


def test_avm::design_constructor_exists():
    assert callable(avm::Design.__init__)


def test_avm::design_constructor_args():
    sig = inspect.signature(avm::Design.__init__)
    params = list(sig.parameters.keys())
    assert "DesignSpaceSrcID" in params, "Missing parameter 'DesignSpaceSrcID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "DesignID" in params, "Missing parameter 'DesignID'"
    assert "SchemaVersion" in params, "Missing parameter 'SchemaVersion'"

def test_avm::design_has_DesignSpaceSrcID():
    assert hasattr(avm::Design, "DesignSpaceSrcID")
    descriptor = None
    for klass in avm::Design.__mro__:
        if "DesignSpaceSrcID" in klass.__dict__:
            descriptor = klass.__dict__["DesignSpaceSrcID"]
            break
    assert isinstance(descriptor, property)

def test_avm::design_has_Name():
    assert hasattr(avm::Design, "Name")
    descriptor = None
    for klass in avm::Design.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::design_has_DesignID():
    assert hasattr(avm::Design, "DesignID")
    descriptor = None
    for klass in avm::Design.__mro__:
        if "DesignID" in klass.__dict__:
            descriptor = klass.__dict__["DesignID"]
            break
    assert isinstance(descriptor, property)

def test_avm::design_has_SchemaVersion():
    assert hasattr(avm::Design, "SchemaVersion")
    descriptor = None
    for klass in avm::Design.__mro__:
        if "SchemaVersion" in klass.__dict__:
            descriptor = klass.__dict__["SchemaVersion"]
            break
    assert isinstance(descriptor, property)



def test_avm::componentinstance_is_not_abstract():
    assert not inspect.isabstract(avm::ComponentInstance)


def test_avm::componentinstance_constructor_exists():
    assert callable(avm::ComponentInstance.__init__)


def test_avm::componentinstance_constructor_args():
    sig = inspect.signature(avm::ComponentInstance.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "ComponentID" in params, "Missing parameter 'ComponentID'"
    assert "DesignSpaceSrcComponentID" in params, "Missing parameter 'DesignSpaceSrcComponentID'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::componentinstance_has_Name():
    assert hasattr(avm::ComponentInstance, "Name")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::componentinstance_has_YPosition():
    assert hasattr(avm::ComponentInstance, "YPosition")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::componentinstance_has_ComponentID():
    assert hasattr(avm::ComponentInstance, "ComponentID")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "ComponentID" in klass.__dict__:
            descriptor = klass.__dict__["ComponentID"]
            break
    assert isinstance(descriptor, property)

def test_avm::componentinstance_has_DesignSpaceSrcComponentID():
    assert hasattr(avm::ComponentInstance, "DesignSpaceSrcComponentID")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "DesignSpaceSrcComponentID" in klass.__dict__:
            descriptor = klass.__dict__["DesignSpaceSrcComponentID"]
            break
    assert isinstance(descriptor, property)

def test_avm::componentinstance_has_ID():
    assert hasattr(avm::ComponentInstance, "ID")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::componentinstance_has_XPosition():
    assert hasattr(avm::ComponentInstance, "XPosition")
    descriptor = None
    for klass in avm::ComponentInstance.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm::domainmodelmetric_is_not_abstract():
    assert not inspect.isabstract(avm::DomainModelMetric)


def test_avm::domainmodelmetric_constructor_exists():
    assert callable(avm::DomainModelMetric.__init__)


def test_avm::domainmodelmetric_constructor_args():
    sig = inspect.signature(avm::DomainModelMetric.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::domainmodelmetric_has_ID():
    assert hasattr(avm::DomainModelMetric, "ID")
    descriptor = None
    for klass in avm::DomainModelMetric.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodelmetric_has_YPosition():
    assert hasattr(avm::DomainModelMetric, "YPosition")
    descriptor = None
    for klass in avm::DomainModelMetric.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodelmetric_has_Notes():
    assert hasattr(avm::DomainModelMetric, "Notes")
    descriptor = None
    for klass in avm::DomainModelMetric.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodelmetric_has_XPosition():
    assert hasattr(avm::DomainModelMetric, "XPosition")
    descriptor = None
    for klass in avm::DomainModelMetric.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_distributionrestriction_is_not_abstract():
    assert not inspect.isabstract(DistributionRestriction)


def test_distributionrestriction_constructor_exists():
    assert callable(DistributionRestriction.__init__)


def test_distributionrestriction_constructor_args():
    sig = inspect.signature(DistributionRestriction.__init__)
    params = list(sig.parameters.keys())



def test_avm::proprietary_is_not_abstract():
    assert not inspect.isabstract(avm::Proprietary)


def test_avm::proprietary_constructor_exists():
    assert callable(avm::Proprietary.__init__)


def test_avm::proprietary_constructor_args():
    sig = inspect.signature(avm::Proprietary.__init__)
    params = list(sig.parameters.keys())
    assert "Organization" in params, "Missing parameter 'Organization'"

def test_avm::proprietary_has_Organization():
    assert hasattr(avm::Proprietary, "Organization")
    descriptor = None
    for klass in avm::Proprietary.__mro__:
        if "Organization" in klass.__dict__:
            descriptor = klass.__dict__["Organization"]
            break
    assert isinstance(descriptor, property)



def test_avm::doddistributionstatement_is_not_abstract():
    assert not inspect.isabstract(avm::DoDDistributionStatement)


def test_avm::doddistributionstatement_constructor_exists():
    assert callable(avm::DoDDistributionStatement.__init__)


def test_avm::doddistributionstatement_constructor_args():
    sig = inspect.signature(avm::DoDDistributionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_avm::doddistributionstatement_has_Type():
    assert hasattr(avm::DoDDistributionStatement, "Type")
    descriptor = None
    for klass in avm::DoDDistributionStatement.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_avm::itar_is_not_abstract():
    assert not inspect.isabstract(avm::ITAR)


def test_avm::itar_constructor_exists():
    assert callable(avm::ITAR.__init__)


def test_avm::itar_constructor_args():
    sig = inspect.signature(avm::ITAR.__init__)
    params = list(sig.parameters.keys())



def test_avm::securityclassification_is_not_abstract():
    assert not inspect.isabstract(avm::SecurityClassification)


def test_avm::securityclassification_constructor_exists():
    assert callable(avm::SecurityClassification.__init__)


def test_avm::securityclassification_constructor_args():
    sig = inspect.signature(avm::SecurityClassification.__init__)
    params = list(sig.parameters.keys())
    assert "Level" in params, "Missing parameter 'Level'"

def test_avm::securityclassification_has_Level():
    assert hasattr(avm::SecurityClassification, "Level")
    descriptor = None
    for klass in avm::SecurityClassification.__mro__:
        if "Level" in klass.__dict__:
            descriptor = klass.__dict__["Level"]
            break
    assert isinstance(descriptor, property)



def test_probabilisticvalue_is_not_abstract():
    assert not inspect.isabstract(ProbabilisticValue)


def test_probabilisticvalue_constructor_exists():
    assert callable(ProbabilisticValue.__init__)


def test_probabilisticvalue_constructor_args():
    sig = inspect.signature(ProbabilisticValue.__init__)
    params = list(sig.parameters.keys())



def test_avm::normaldistribution_is_not_abstract():
    assert not inspect.isabstract(avm::NormalDistribution)


def test_avm::normaldistribution_constructor_exists():
    assert callable(avm::NormalDistribution.__init__)


def test_avm::normaldistribution_constructor_args():
    sig = inspect.signature(avm::NormalDistribution.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_avm::compoundproperty_is_not_abstract():
    assert not inspect.isabstract(avm::CompoundProperty)


def test_avm::compoundproperty_constructor_exists():
    assert callable(avm::CompoundProperty.__init__)


def test_avm::compoundproperty_constructor_args():
    sig = inspect.signature(avm::CompoundProperty.__init__)
    params = list(sig.parameters.keys())



def test_avm::primitiveproperty_is_not_abstract():
    assert not inspect.isabstract(avm::PrimitiveProperty)


def test_avm::primitiveproperty_constructor_exists():
    assert callable(avm::PrimitiveProperty.__init__)


def test_avm::primitiveproperty_constructor_args():
    sig = inspect.signature(avm::PrimitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_avm::uniformdistribution_is_not_abstract():
    assert not inspect.isabstract(avm::UniformDistribution)


def test_avm::uniformdistribution_constructor_exists():
    assert callable(avm::UniformDistribution.__init__)


def test_avm::uniformdistribution_constructor_args():
    sig = inspect.signature(avm::UniformDistribution.__init__)
    params = list(sig.parameters.keys())



def test_avm::domainmodelparameter_is_not_abstract():
    assert not inspect.isabstract(avm::DomainModelParameter)


def test_avm::domainmodelparameter_constructor_exists():
    assert callable(avm::DomainModelParameter.__init__)


def test_avm::domainmodelparameter_constructor_args():
    sig = inspect.signature(avm::DomainModelParameter.__init__)
    params = list(sig.parameters.keys())
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm::domainmodelparameter_has_YPosition():
    assert hasattr(avm::DomainModelParameter, "YPosition")
    descriptor = None
    for klass in avm::DomainModelParameter.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodelparameter_has_XPosition():
    assert hasattr(avm::DomainModelParameter, "XPosition")
    descriptor = None
    for klass in avm::DomainModelParameter.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodelparameter_has_Notes():
    assert hasattr(avm::DomainModelParameter, "Notes")
    descriptor = None
    for klass in avm::DomainModelParameter.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_avm::abstractport_is_not_abstract():
    assert not inspect.isabstract(avm::AbstractPort)


def test_avm::abstractport_constructor_exists():
    assert callable(avm::AbstractPort.__init__)


def test_avm::abstractport_constructor_args():
    sig = inspect.signature(avm::AbstractPort.__init__)
    params = list(sig.parameters.keys())



def test_avm::domainmodelport_is_not_abstract():
    assert not inspect.isabstract(avm::DomainModelPort)


def test_avm::domainmodelport_constructor_exists():
    assert callable(avm::DomainModelPort.__init__)


def test_avm::domainmodelport_constructor_args():
    sig = inspect.signature(avm::DomainModelPort.__init__)
    params = list(sig.parameters.keys())



def test_portmaptarget_is_not_abstract():
    assert not inspect.isabstract(PortMapTarget)


def test_portmaptarget_constructor_exists():
    assert callable(PortMapTarget.__init__)


def test_portmaptarget_constructor_args():
    sig = inspect.signature(PortMapTarget.__init__)
    params = list(sig.parameters.keys())



def test_avm::componentportinstance_is_not_abstract():
    assert not inspect.isabstract(avm::ComponentPortInstance)


def test_avm::componentportinstance_constructor_exists():
    assert callable(avm::ComponentPortInstance.__init__)


def test_avm::componentportinstance_constructor_args():
    sig = inspect.signature(avm::ComponentPortInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm::componentportinstance_has_IDinComponentModel():
    assert hasattr(avm::ComponentPortInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm::ComponentPortInstance.__mro__:
        if "IDinComponentModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinComponentModel"]
            break
    assert isinstance(descriptor, property)



def test_avm::connectorfeature_is_not_abstract():
    assert not inspect.isabstract(avm::ConnectorFeature)


def test_avm::connectorfeature_constructor_exists():
    assert callable(avm::ConnectorFeature.__init__)


def test_avm::connectorfeature_constructor_args():
    sig = inspect.signature(avm::ConnectorFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm::assemblydetail_is_not_abstract():
    assert not inspect.isabstract(avm::assemblyDetail)


def test_avm::assemblydetail_constructor_exists():
    assert callable(avm::assemblyDetail.__init__)


def test_avm::assemblydetail_constructor_args():
    sig = inspect.signature(avm::assemblyDetail.__init__)
    params = list(sig.parameters.keys())



def test_connectorcompositiontarget_is_not_abstract():
    assert not inspect.isabstract(ConnectorCompositionTarget)


def test_connectorcompositiontarget_constructor_exists():
    assert callable(ConnectorCompositionTarget.__init__)


def test_connectorcompositiontarget_constructor_args():
    sig = inspect.signature(ConnectorCompositionTarget.__init__)
    params = list(sig.parameters.keys())



def test_avm::componentconnectorinstance_is_not_abstract():
    assert not inspect.isabstract(avm::ComponentConnectorInstance)


def test_avm::componentconnectorinstance_constructor_exists():
    assert callable(avm::ComponentConnectorInstance.__init__)


def test_avm::componentconnectorinstance_constructor_args():
    sig = inspect.signature(avm::ComponentConnectorInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm::componentconnectorinstance_has_IDinComponentModel():
    assert hasattr(avm::ComponentConnectorInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm::ComponentConnectorInstance.__mro__:
        if "IDinComponentModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinComponentModel"]
            break
    assert isinstance(descriptor, property)



def test_avm::valuenode_is_not_abstract():
    assert not inspect.isabstract(avm::ValueNode)


def test_avm::valuenode_constructor_exists():
    assert callable(avm::ValueNode.__init__)


def test_avm::valuenode_constructor_args():
    sig = inspect.signature(avm::ValueNode.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm::valuenode_has_ID():
    assert hasattr(avm::ValueNode, "ID")
    descriptor = None
    for klass in avm::ValueNode.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_valueexpressiontype_is_not_abstract():
    assert not inspect.isabstract(ValueExpressionType)


def test_valueexpressiontype_constructor_exists():
    assert callable(ValueExpressionType.__init__)


def test_valueexpressiontype_constructor_args():
    sig = inspect.signature(ValueExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_avm::parametricenumeratedvalue_is_not_abstract():
    assert not inspect.isabstract(avm::ParametricEnumeratedValue)


def test_avm::parametricenumeratedvalue_constructor_exists():
    assert callable(avm::ParametricEnumeratedValue.__init__)


def test_avm::parametricenumeratedvalue_constructor_args():
    sig = inspect.signature(avm::ParametricEnumeratedValue.__init__)
    params = list(sig.parameters.keys())



def test_avm::derivedvalue_is_not_abstract():
    assert not inspect.isabstract(avm::DerivedValue)


def test_avm::derivedvalue_constructor_exists():
    assert callable(avm::DerivedValue.__init__)


def test_avm::derivedvalue_constructor_args():
    sig = inspect.signature(avm::DerivedValue.__init__)
    params = list(sig.parameters.keys())



def test_avm::probabilisticvalue_is_not_abstract():
    assert not inspect.isabstract(avm::ProbabilisticValue)


def test_avm::probabilisticvalue_constructor_exists():
    assert callable(avm::ProbabilisticValue.__init__)


def test_avm::probabilisticvalue_constructor_args():
    sig = inspect.signature(avm::ProbabilisticValue.__init__)
    params = list(sig.parameters.keys())



def test_avm::calculatedvalue_is_not_abstract():
    assert not inspect.isabstract(avm::CalculatedValue)


def test_avm::calculatedvalue_constructor_exists():
    assert callable(avm::CalculatedValue.__init__)


def test_avm::calculatedvalue_constructor_args():
    sig = inspect.signature(avm::CalculatedValue.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Expression" in params, "Missing parameter 'Expression'"

def test_avm::calculatedvalue_has_Type():
    assert hasattr(avm::CalculatedValue, "Type")
    descriptor = None
    for klass in avm::CalculatedValue.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_avm::calculatedvalue_has_Expression():
    assert hasattr(avm::CalculatedValue, "Expression")
    descriptor = None
    for klass in avm::CalculatedValue.__mro__:
        if "Expression" in klass.__dict__:
            descriptor = klass.__dict__["Expression"]
            break
    assert isinstance(descriptor, property)



def test_avm::parametricvalue_is_not_abstract():
    assert not inspect.isabstract(avm::ParametricValue)


def test_avm::parametricvalue_constructor_exists():
    assert callable(avm::ParametricValue.__init__)


def test_avm::parametricvalue_constructor_args():
    sig = inspect.signature(avm::ParametricValue.__init__)
    params = list(sig.parameters.keys())



def test_avm::fixedvalue_is_not_abstract():
    assert not inspect.isabstract(avm::FixedValue)


def test_avm::fixedvalue_constructor_exists():
    assert callable(avm::FixedValue.__init__)


def test_avm::fixedvalue_constructor_args():
    sig = inspect.signature(avm::FixedValue.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"
    assert "Uncertainty" in params, "Missing parameter 'Uncertainty'"

def test_avm::fixedvalue_has_Value():
    assert hasattr(avm::FixedValue, "Value")
    descriptor = None
    for klass in avm::FixedValue.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_avm::fixedvalue_has_Uncertainty():
    assert hasattr(avm::FixedValue, "Uncertainty")
    descriptor = None
    for klass in avm::FixedValue.__mro__:
        if "Uncertainty" in klass.__dict__:
            descriptor = klass.__dict__["Uncertainty"]
            break
    assert isinstance(descriptor, property)



def test_avm::datasource_is_not_abstract():
    assert not inspect.isabstract(avm::DataSource)


def test_avm::datasource_constructor_exists():
    assert callable(avm::DataSource.__init__)


def test_avm::datasource_constructor_args():
    sig = inspect.signature(avm::DataSource.__init__)
    params = list(sig.parameters.keys())
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm::datasource_has_Notes():
    assert hasattr(avm::DataSource, "Notes")
    descriptor = None
    for klass in avm::DataSource.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_avm::valueexpressiontype_is_not_abstract():
    assert not inspect.isabstract(avm::ValueExpressionType)


def test_avm::valueexpressiontype_constructor_exists():
    assert callable(avm::ValueExpressionType.__init__)


def test_avm::valueexpressiontype_constructor_args():
    sig = inspect.signature(avm::ValueExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_avm::cyber::cybermodel_is_not_abstract():
    assert not inspect.isabstract(avm::cyber::CyberModel)


def test_avm::cyber::cybermodel_constructor_exists():
    assert callable(avm::cyber::CyberModel.__init__)


def test_avm::cyber::cybermodel_constructor_args():
    sig = inspect.signature(avm::cyber::CyberModel.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Locator" in params, "Missing parameter 'Locator'"
    assert "Class" in params, "Missing parameter 'Class'"

def test_avm::cyber::cybermodel_has_Type():
    assert hasattr(avm::cyber::CyberModel, "Type")
    descriptor = None
    for klass in avm::cyber::CyberModel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_avm::cyber::cybermodel_has_Locator():
    assert hasattr(avm::cyber::CyberModel, "Locator")
    descriptor = None
    for klass in avm::cyber::CyberModel.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)

def test_avm::cyber::cybermodel_has_Class():
    assert hasattr(avm::cyber::CyberModel, "Class")
    descriptor = None
    for klass in avm::cyber::CyberModel.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)



def test_manufacturing::avm::value_is_not_abstract():
    assert not inspect.isabstract(manufacturing::avm::Value)


def test_manufacturing::avm::value_constructor_exists():
    assert callable(manufacturing::avm::Value.__init__)


def test_manufacturing::avm::value_constructor_args():
    sig = inspect.signature(manufacturing::avm::Value.__init__)
    params = list(sig.parameters.keys())



def test_avm::manufacturing::manufacturingmodel_is_not_abstract():
    assert not inspect.isabstract(avm::manufacturing::ManufacturingModel)


def test_avm::manufacturing::manufacturingmodel_constructor_exists():
    assert callable(avm::manufacturing::ManufacturingModel.__init__)


def test_avm::manufacturing::manufacturingmodel_constructor_args():
    sig = inspect.signature(avm::manufacturing::ManufacturingModel.__init__)
    params = list(sig.parameters.keys())



def test_avm::adamscar::filereference_is_not_abstract():
    assert not inspect.isabstract(avm::adamsCar::FileReference)


def test_avm::adamscar::filereference_constructor_exists():
    assert callable(avm::adamsCar::FileReference.__init__)


def test_avm::adamscar::filereference_constructor_args():
    sig = inspect.signature(avm::adamsCar::FileReference.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "FilePath" in params, "Missing parameter 'FilePath'"

def test_avm::adamscar::filereference_has_ID():
    assert hasattr(avm::adamsCar::FileReference, "ID")
    descriptor = None
    for klass in avm::adamsCar::FileReference.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::adamscar::filereference_has_Name():
    assert hasattr(avm::adamsCar::FileReference, "Name")
    descriptor = None
    for klass in avm::adamsCar::FileReference.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::adamscar::filereference_has_FilePath():
    assert hasattr(avm::adamsCar::FileReference, "FilePath")
    descriptor = None
    for klass in avm::adamsCar::FileReference.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)



def test_adamscar::avm::value_is_not_abstract():
    assert not inspect.isabstract(adamsCar::avm::Value)


def test_adamscar::avm::value_constructor_exists():
    assert callable(adamsCar::avm::Value.__init__)


def test_adamscar::avm::value_constructor_args():
    sig = inspect.signature(adamsCar::avm::Value.__init__)
    params = list(sig.parameters.keys())



def test_filereference_is_not_abstract():
    assert not inspect.isabstract(FileReference)


def test_filereference_constructor_exists():
    assert callable(FileReference.__init__)


def test_filereference_constructor_args():
    sig = inspect.signature(FileReference.__init__)
    params = list(sig.parameters.keys())



def test_avm::adamscar::adamscarmodel_is_not_abstract():
    assert not inspect.isabstract(avm::adamsCar::AdamsCarModel)


def test_avm::adamscar::adamscarmodel_constructor_exists():
    assert callable(avm::adamsCar::AdamsCarModel.__init__)


def test_avm::adamscar::adamscarmodel_constructor_args():
    sig = inspect.signature(avm::adamsCar::AdamsCarModel.__init__)
    params = list(sig.parameters.keys())



def test_axis_is_not_abstract():
    assert not inspect.isabstract(Axis)


def test_axis_constructor_exists():
    assert callable(Axis.__init__)


def test_axis_constructor_args():
    sig = inspect.signature(Axis.__init__)
    params = list(sig.parameters.keys())



def test_kinematicjointspec_is_not_abstract():
    assert not inspect.isabstract(KinematicJointSpec)


def test_kinematicjointspec_constructor_exists():
    assert callable(KinematicJointSpec.__init__)


def test_kinematicjointspec_constructor_args():
    sig = inspect.signature(KinematicJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::revolutejointspec_is_not_abstract():
    assert not inspect.isabstract(avm::cad::RevoluteJointSpec)


def test_avm::cad::revolutejointspec_constructor_exists():
    assert callable(avm::cad::RevoluteJointSpec.__init__)


def test_avm::cad::revolutejointspec_constructor_args():
    sig = inspect.signature(avm::cad::RevoluteJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_cad::avm::componentinstance_is_not_abstract():
    assert not inspect.isabstract(cad::avm::ComponentInstance)


def test_cad::avm::componentinstance_constructor_exists():
    assert callable(cad::avm::ComponentInstance.__init__)


def test_cad::avm::componentinstance_constructor_args():
    sig = inspect.signature(cad::avm::ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_designdomainfeature_is_not_abstract():
    assert not inspect.isabstract(DesignDomainFeature)


def test_designdomainfeature_constructor_exists():
    assert callable(DesignDomainFeature.__init__)


def test_designdomainfeature_constructor_args():
    sig = inspect.signature(DesignDomainFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::assemblyroot_is_not_abstract():
    assert not inspect.isabstract(avm::cad::AssemblyRoot)


def test_avm::cad::assemblyroot_constructor_exists():
    assert callable(avm::cad::AssemblyRoot.__init__)


def test_avm::cad::assemblyroot_constructor_args():
    sig = inspect.signature(avm::cad::AssemblyRoot.__init__)
    params = list(sig.parameters.keys())



def test_connectorfeature_is_not_abstract():
    assert not inspect.isabstract(ConnectorFeature)


def test_connectorfeature_constructor_exists():
    assert callable(ConnectorFeature.__init__)


def test_connectorfeature_constructor_args():
    sig = inspect.signature(ConnectorFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::kinematicjointspec_is_not_abstract():
    assert not inspect.isabstract(avm::cad::KinematicJointSpec)


def test_avm::cad::kinematicjointspec_constructor_exists():
    assert callable(avm::cad::KinematicJointSpec.__init__)


def test_avm::cad::kinematicjointspec_constructor_args():
    sig = inspect.signature(avm::cad::KinematicJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::guidedatum_is_not_abstract():
    assert not inspect.isabstract(avm::cad::GuideDatum)


def test_avm::cad::guidedatum_constructor_exists():
    assert callable(avm::cad::GuideDatum.__init__)


def test_avm::cad::guidedatum_constructor_args():
    sig = inspect.signature(avm::cad::GuideDatum.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::planereference_is_not_abstract():
    assert not inspect.isabstract(avm::cad::PlaneReference)


def test_avm::cad::planereference_constructor_exists():
    assert callable(avm::cad::PlaneReference.__init__)


def test_avm::cad::planereference_constructor_args():
    sig = inspect.signature(avm::cad::PlaneReference.__init__)
    params = list(sig.parameters.keys())



def test_planereference_is_not_abstract():
    assert not inspect.isabstract(PlaneReference)


def test_planereference_constructor_exists():
    assert callable(PlaneReference.__init__)


def test_planereference_constructor_args():
    sig = inspect.signature(PlaneReference.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::translationaljointspec_is_not_abstract():
    assert not inspect.isabstract(avm::cad::TranslationalJointSpec)


def test_avm::cad::translationaljointspec_constructor_exists():
    assert callable(avm::cad::TranslationalJointSpec.__init__)


def test_avm::cad::translationaljointspec_constructor_args():
    sig = inspect.signature(avm::cad::TranslationalJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::customgeometryinput_is_not_abstract():
    assert not inspect.isabstract(avm::cad::CustomGeometryInput)


def test_avm::cad::customgeometryinput_constructor_exists():
    assert callable(avm::cad::CustomGeometryInput.__init__)


def test_avm::cad::customgeometryinput_constructor_args():
    sig = inspect.signature(avm::cad::CustomGeometryInput.__init__)
    params = list(sig.parameters.keys())
    assert "Operation" in params, "Missing parameter 'Operation'"

def test_avm::cad::customgeometryinput_has_Operation():
    assert hasattr(avm::cad::CustomGeometryInput, "Operation")
    descriptor = None
    for klass in avm::cad::CustomGeometryInput.__mro__:
        if "Operation" in klass.__dict__:
            descriptor = klass.__dict__["Operation"]
            break
    assert isinstance(descriptor, property)



def test_customgeometryinput_is_not_abstract():
    assert not inspect.isabstract(CustomGeometryInput)


def test_customgeometryinput_constructor_exists():
    assert callable(CustomGeometryInput.__init__)


def test_customgeometryinput_constructor_args():
    sig = inspect.signature(CustomGeometryInput.__init__)
    params = list(sig.parameters.keys())



def test_geometry3d_is_not_abstract():
    assert not inspect.isabstract(Geometry3D)


def test_geometry3d_constructor_exists():
    assert callable(Geometry3D.__init__)


def test_geometry3d_constructor_args():
    sig = inspect.signature(Geometry3D.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::sphere_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Sphere)


def test_avm::cad::sphere_constructor_exists():
    assert callable(avm::cad::Sphere.__init__)


def test_avm::cad::sphere_constructor_args():
    sig = inspect.signature(avm::cad::Sphere.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::extrudedgeometry_is_not_abstract():
    assert not inspect.isabstract(avm::cad::ExtrudedGeometry)


def test_avm::cad::extrudedgeometry_constructor_exists():
    assert callable(avm::cad::ExtrudedGeometry.__init__)


def test_avm::cad::extrudedgeometry_constructor_args():
    sig = inspect.signature(avm::cad::ExtrudedGeometry.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::surface_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Surface)


def test_avm::cad::surface_constructor_exists():
    assert callable(avm::cad::Surface.__init__)


def test_avm::cad::surface_constructor_args():
    sig = inspect.signature(avm::cad::Surface.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::pointreference_is_not_abstract():
    assert not inspect.isabstract(avm::cad::PointReference)


def test_avm::cad::pointreference_constructor_exists():
    assert callable(avm::cad::PointReference.__init__)


def test_avm::cad::pointreference_constructor_args():
    sig = inspect.signature(avm::cad::PointReference.__init__)
    params = list(sig.parameters.keys())



def test_analysisconstruct_is_not_abstract():
    assert not inspect.isabstract(AnalysisConstruct)


def test_analysisconstruct_constructor_exists():
    assert callable(AnalysisConstruct.__init__)


def test_analysisconstruct_constructor_args():
    sig = inspect.signature(AnalysisConstruct.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::geometry_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Geometry)


def test_avm::cad::geometry_constructor_exists():
    assert callable(avm::cad::Geometry.__init__)


def test_avm::cad::geometry_constructor_args():
    sig = inspect.signature(avm::cad::Geometry.__init__)
    params = list(sig.parameters.keys())
    assert "PartIntersectionModifier" in params, "Missing parameter 'PartIntersectionModifier'"
    assert "GeometryQualifier" in params, "Missing parameter 'GeometryQualifier'"

def test_avm::cad::geometry_has_PartIntersectionModifier():
    assert hasattr(avm::cad::Geometry, "PartIntersectionModifier")
    descriptor = None
    for klass in avm::cad::Geometry.__mro__:
        if "PartIntersectionModifier" in klass.__dict__:
            descriptor = klass.__dict__["PartIntersectionModifier"]
            break
    assert isinstance(descriptor, property)

def test_avm::cad::geometry_has_GeometryQualifier():
    assert hasattr(avm::cad::Geometry, "GeometryQualifier")
    descriptor = None
    for klass in avm::cad::Geometry.__mro__:
        if "GeometryQualifier" in klass.__dict__:
            descriptor = klass.__dict__["GeometryQualifier"]
            break
    assert isinstance(descriptor, property)



def test_plane_is_not_abstract():
    assert not inspect.isabstract(Plane)


def test_plane_constructor_exists():
    assert callable(Plane.__init__)


def test_plane_constructor_args():
    sig = inspect.signature(Plane.__init__)
    params = list(sig.parameters.keys())



def test_cad::avm::value_is_not_abstract():
    assert not inspect.isabstract(cad::avm::Value)


def test_cad::avm::value_constructor_exists():
    assert callable(cad::avm::Value.__init__)


def test_cad::avm::value_constructor_args():
    sig = inspect.signature(cad::avm::Value.__init__)
    params = list(sig.parameters.keys())



def test_pointreference_is_not_abstract():
    assert not inspect.isabstract(PointReference)


def test_pointreference_constructor_exists():
    assert callable(PointReference.__init__)


def test_pointreference_constructor_args():
    sig = inspect.signature(PointReference.__init__)
    params = list(sig.parameters.keys())



def test_geometry2d_is_not_abstract():
    assert not inspect.isabstract(Geometry2D)


def test_geometry2d_constructor_exists():
    assert callable(Geometry2D.__init__)


def test_geometry2d_constructor_args():
    sig = inspect.signature(Geometry2D.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::polygon_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Polygon)


def test_avm::cad::polygon_constructor_exists():
    assert callable(avm::cad::Polygon.__init__)


def test_avm::cad::polygon_constructor_args():
    sig = inspect.signature(avm::cad::Polygon.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::circle_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Circle)


def test_avm::cad::circle_constructor_exists():
    assert callable(avm::cad::Circle.__init__)


def test_avm::cad::circle_constructor_args():
    sig = inspect.signature(avm::cad::Circle.__init__)
    params = list(sig.parameters.keys())



def test_geometry_is_not_abstract():
    assert not inspect.isabstract(Geometry)


def test_geometry_constructor_exists():
    assert callable(Geometry.__init__)


def test_geometry_constructor_args():
    sig = inspect.signature(Geometry.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::customgeometry_is_not_abstract():
    assert not inspect.isabstract(avm::cad::CustomGeometry)


def test_avm::cad::customgeometry_constructor_exists():
    assert callable(avm::cad::CustomGeometry.__init__)


def test_avm::cad::customgeometry_constructor_args():
    sig = inspect.signature(avm::cad::CustomGeometry.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::geometry3d_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Geometry3D)


def test_avm::cad::geometry3d_constructor_exists():
    assert callable(avm::cad::Geometry3D.__init__)


def test_avm::cad::geometry3d_constructor_args():
    sig = inspect.signature(avm::cad::Geometry3D.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::geometry2d_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Geometry2D)


def test_avm::cad::geometry2d_constructor_exists():
    assert callable(avm::cad::Geometry2D.__init__)


def test_avm::cad::geometry2d_constructor_args():
    sig = inspect.signature(avm::cad::Geometry2D.__init__)
    params = list(sig.parameters.keys())



def test_datum_is_not_abstract():
    assert not inspect.isabstract(Datum)


def test_datum_constructor_exists():
    assert callable(Datum.__init__)


def test_datum_constructor_args():
    sig = inspect.signature(Datum.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::plane_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Plane)


def test_avm::cad::plane_constructor_exists():
    assert callable(avm::cad::Plane.__init__)


def test_avm::cad::plane_constructor_args():
    sig = inspect.signature(avm::cad::Plane.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::axis_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Axis)


def test_avm::cad::axis_constructor_exists():
    assert callable(avm::cad::Axis.__init__)


def test_avm::cad::axis_constructor_args():
    sig = inspect.signature(avm::cad::Axis.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::point_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Point)


def test_avm::cad::point_constructor_exists():
    assert callable(avm::cad::Point.__init__)


def test_avm::cad::point_constructor_args():
    sig = inspect.signature(avm::cad::Point.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::coordinatesystem_is_not_abstract():
    assert not inspect.isabstract(avm::cad::CoordinateSystem)


def test_avm::cad::coordinatesystem_constructor_exists():
    assert callable(avm::cad::CoordinateSystem.__init__)


def test_avm::cad::coordinatesystem_constructor_args():
    sig = inspect.signature(avm::cad::CoordinateSystem.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::cadmodel_is_not_abstract():
    assert not inspect.isabstract(avm::cad::CADModel)


def test_avm::cad::cadmodel_constructor_exists():
    assert callable(avm::cad::CADModel.__init__)


def test_avm::cad::cadmodel_constructor_args():
    sig = inspect.signature(avm::cad::CADModel.__init__)
    params = list(sig.parameters.keys())



def test_settings_is_not_abstract():
    assert not inspect.isabstract(Settings)


def test_settings_constructor_exists():
    assert callable(Settings.__init__)


def test_settings_constructor_args():
    sig = inspect.signature(Settings.__init__)
    params = list(sig.parameters.keys())



def test_avm::modelica::solversettings_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::SolverSettings)


def test_avm::modelica::solversettings_constructor_exists():
    assert callable(avm::modelica::SolverSettings.__init__)


def test_avm::modelica::solversettings_constructor_args():
    sig = inspect.signature(avm::modelica::SolverSettings.__init__)
    params = list(sig.parameters.keys())
    assert "Solver" in params, "Missing parameter 'Solver'"
    assert "NumberOfIntervals" in params, "Missing parameter 'NumberOfIntervals'"
    assert "JobManagerToolSelection" in params, "Missing parameter 'JobManagerToolSelection'"
    assert "IntervalLength" in params, "Missing parameter 'IntervalLength'"
    assert "ToolSpecificAnnotations" in params, "Missing parameter 'ToolSpecificAnnotations'"
    assert "StartTime" in params, "Missing parameter 'StartTime'"
    assert "Tolerance" in params, "Missing parameter 'Tolerance'"
    assert "StopTime" in params, "Missing parameter 'StopTime'"
    assert "IntervalMethod" in params, "Missing parameter 'IntervalMethod'"

def test_avm::modelica::solversettings_has_Solver():
    assert hasattr(avm::modelica::SolverSettings, "Solver")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "Solver" in klass.__dict__:
            descriptor = klass.__dict__["Solver"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_NumberOfIntervals():
    assert hasattr(avm::modelica::SolverSettings, "NumberOfIntervals")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "NumberOfIntervals" in klass.__dict__:
            descriptor = klass.__dict__["NumberOfIntervals"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_JobManagerToolSelection():
    assert hasattr(avm::modelica::SolverSettings, "JobManagerToolSelection")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "JobManagerToolSelection" in klass.__dict__:
            descriptor = klass.__dict__["JobManagerToolSelection"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_IntervalLength():
    assert hasattr(avm::modelica::SolverSettings, "IntervalLength")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "IntervalLength" in klass.__dict__:
            descriptor = klass.__dict__["IntervalLength"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_ToolSpecificAnnotations():
    assert hasattr(avm::modelica::SolverSettings, "ToolSpecificAnnotations")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "ToolSpecificAnnotations" in klass.__dict__:
            descriptor = klass.__dict__["ToolSpecificAnnotations"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_StartTime():
    assert hasattr(avm::modelica::SolverSettings, "StartTime")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "StartTime" in klass.__dict__:
            descriptor = klass.__dict__["StartTime"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_Tolerance():
    assert hasattr(avm::modelica::SolverSettings, "Tolerance")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "Tolerance" in klass.__dict__:
            descriptor = klass.__dict__["Tolerance"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_StopTime():
    assert hasattr(avm::modelica::SolverSettings, "StopTime")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "StopTime" in klass.__dict__:
            descriptor = klass.__dict__["StopTime"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::solversettings_has_IntervalMethod():
    assert hasattr(avm::modelica::SolverSettings, "IntervalMethod")
    descriptor = None
    for klass in avm::modelica::SolverSettings.__mro__:
        if "IntervalMethod" in klass.__dict__:
            descriptor = klass.__dict__["IntervalMethod"]
            break
    assert isinstance(descriptor, property)



def test_avm::modelica::limit_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::Limit)


def test_avm::modelica::limit_constructor_exists():
    assert callable(avm::modelica::Limit.__init__)


def test_avm::modelica::limit_constructor_args():
    sig = inspect.signature(avm::modelica::Limit.__init__)
    params = list(sig.parameters.keys())
    assert "BoundType" in params, "Missing parameter 'BoundType'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ToleranceTimeWindow" in params, "Missing parameter 'ToleranceTimeWindow'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "VariableLocator" in params, "Missing parameter 'VariableLocator'"

def test_avm::modelica::limit_has_BoundType():
    assert hasattr(avm::modelica::Limit, "BoundType")
    descriptor = None
    for klass in avm::modelica::Limit.__mro__:
        if "BoundType" in klass.__dict__:
            descriptor = klass.__dict__["BoundType"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::limit_has_Name():
    assert hasattr(avm::modelica::Limit, "Name")
    descriptor = None
    for klass in avm::modelica::Limit.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::limit_has_ToleranceTimeWindow():
    assert hasattr(avm::modelica::Limit, "ToleranceTimeWindow")
    descriptor = None
    for klass in avm::modelica::Limit.__mro__:
        if "ToleranceTimeWindow" in klass.__dict__:
            descriptor = klass.__dict__["ToleranceTimeWindow"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::limit_has_Notes():
    assert hasattr(avm::modelica::Limit, "Notes")
    descriptor = None
    for klass in avm::modelica::Limit.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::limit_has_VariableLocator():
    assert hasattr(avm::modelica::Limit, "VariableLocator")
    descriptor = None
    for klass in avm::modelica::Limit.__mro__:
        if "VariableLocator" in klass.__dict__:
            descriptor = klass.__dict__["VariableLocator"]
            break
    assert isinstance(descriptor, property)



def test_domainmodelmetric_is_not_abstract():
    assert not inspect.isabstract(DomainModelMetric)


def test_domainmodelmetric_constructor_exists():
    assert callable(DomainModelMetric.__init__)


def test_domainmodelmetric_constructor_args():
    sig = inspect.signature(DomainModelMetric.__init__)
    params = list(sig.parameters.keys())



def test_avm::manufacturing::metric_is_not_abstract():
    assert not inspect.isabstract(avm::manufacturing::Metric)


def test_avm::manufacturing::metric_constructor_exists():
    assert callable(avm::manufacturing::Metric.__init__)


def test_avm::manufacturing::metric_constructor_args():
    sig = inspect.signature(avm::manufacturing::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::manufacturing::metric_has_Name():
    assert hasattr(avm::manufacturing::Metric, "Name")
    descriptor = None
    for klass in avm::manufacturing::Metric.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::cad::metric_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Metric)


def test_avm::cad::metric_constructor_exists():
    assert callable(avm::cad::Metric.__init__)


def test_avm::cad::metric_constructor_args():
    sig = inspect.signature(avm::cad::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::cad::metric_has_Name():
    assert hasattr(avm::cad::Metric, "Name")
    descriptor = None
    for klass in avm::cad::Metric.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::modelica::metric_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::Metric)


def test_avm::modelica::metric_constructor_exists():
    assert callable(avm::modelica::Metric.__init__)


def test_avm::modelica::metric_constructor_args():
    sig = inspect.signature(avm::modelica::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm::modelica::metric_has_Locator():
    assert hasattr(avm::modelica::Metric, "Locator")
    descriptor = None
    for klass in avm::modelica::Metric.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)



def test_modelica::avm::value_is_not_abstract():
    assert not inspect.isabstract(modelica::avm::Value)


def test_modelica::avm::value_constructor_exists():
    assert callable(modelica::avm::Value.__init__)


def test_modelica::avm::value_constructor_args():
    sig = inspect.signature(modelica::avm::Value.__init__)
    params = list(sig.parameters.keys())



def test_domainmodelparameter_is_not_abstract():
    assert not inspect.isabstract(DomainModelParameter)


def test_domainmodelparameter_constructor_exists():
    assert callable(DomainModelParameter.__init__)


def test_domainmodelparameter_constructor_args():
    sig = inspect.signature(DomainModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_avm::modelica::redeclare_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::Redeclare)


def test_avm::modelica::redeclare_constructor_exists():
    assert callable(avm::modelica::Redeclare.__init__)


def test_avm::modelica::redeclare_constructor_args():
    sig = inspect.signature(avm::modelica::Redeclare.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm::modelica::redeclare_has_Type():
    assert hasattr(avm::modelica::Redeclare, "Type")
    descriptor = None
    for klass in avm::modelica::Redeclare.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::redeclare_has_Locator():
    assert hasattr(avm::modelica::Redeclare, "Locator")
    descriptor = None
    for klass in avm::modelica::Redeclare.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)



def test_avm::adamscar::parameter_is_not_abstract():
    assert not inspect.isabstract(avm::adamsCar::Parameter)


def test_avm::adamscar::parameter_constructor_exists():
    assert callable(avm::adamsCar::Parameter.__init__)


def test_avm::adamscar::parameter_constructor_args():
    sig = inspect.signature(avm::adamsCar::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::adamscar::parameter_has_ID():
    assert hasattr(avm::adamsCar::Parameter, "ID")
    descriptor = None
    for klass in avm::adamsCar::Parameter.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::adamscar::parameter_has_Name():
    assert hasattr(avm::adamsCar::Parameter, "Name")
    descriptor = None
    for klass in avm::adamsCar::Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::manufacturing::parameter_is_not_abstract():
    assert not inspect.isabstract(avm::manufacturing::Parameter)


def test_avm::manufacturing::parameter_constructor_exists():
    assert callable(avm::manufacturing::Parameter.__init__)


def test_avm::manufacturing::parameter_constructor_args():
    sig = inspect.signature(avm::manufacturing::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::manufacturing::parameter_has_Locator():
    assert hasattr(avm::manufacturing::Parameter, "Locator")
    descriptor = None
    for klass in avm::manufacturing::Parameter.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)

def test_avm::manufacturing::parameter_has_Name():
    assert hasattr(avm::manufacturing::Parameter, "Name")
    descriptor = None
    for klass in avm::manufacturing::Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::cad::parameter_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Parameter)


def test_avm::cad::parameter_constructor_exists():
    assert callable(avm::cad::Parameter.__init__)


def test_avm::cad::parameter_constructor_args():
    sig = inspect.signature(avm::cad::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::cad::parameter_has_Name():
    assert hasattr(avm::cad::Parameter, "Name")
    descriptor = None
    for klass in avm::cad::Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::modelica::parameter_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::Parameter)


def test_avm::modelica::parameter_constructor_exists():
    assert callable(avm::modelica::Parameter.__init__)


def test_avm::modelica::parameter_constructor_args():
    sig = inspect.signature(avm::modelica::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm::modelica::parameter_has_Locator():
    assert hasattr(avm::modelica::Parameter, "Locator")
    descriptor = None
    for klass in avm::modelica::Parameter.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)



def test_domainmodelport_is_not_abstract():
    assert not inspect.isabstract(DomainModelPort)


def test_domainmodelport_constructor_exists():
    assert callable(DomainModelPort.__init__)


def test_domainmodelport_constructor_args():
    sig = inspect.signature(DomainModelPort.__init__)
    params = list(sig.parameters.keys())



def test_avm::cad::datum_is_not_abstract():
    assert not inspect.isabstract(avm::cad::Datum)


def test_avm::cad::datum_constructor_exists():
    assert callable(avm::cad::Datum.__init__)


def test_avm::cad::datum_constructor_args():
    sig = inspect.signature(avm::cad::Datum.__init__)
    params = list(sig.parameters.keys())
    assert "DatumName" in params, "Missing parameter 'DatumName'"

def test_avm::cad::datum_has_DatumName():
    assert hasattr(avm::cad::Datum, "DatumName")
    descriptor = None
    for klass in avm::cad::Datum.__mro__:
        if "DatumName" in klass.__dict__:
            descriptor = klass.__dict__["DatumName"]
            break
    assert isinstance(descriptor, property)



def test_avm::modelica::connector_is_not_abstract():
    assert not inspect.isabstract(avm::modelica::Connector)


def test_avm::modelica::connector_constructor_exists():
    assert callable(avm::modelica::Connector.__init__)


def test_avm::modelica::connector_constructor_args():
    sig = inspect.signature(avm::modelica::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"
    assert "Class" in params, "Missing parameter 'Class'"

def test_avm::modelica::connector_has_Locator():
    assert hasattr(avm::modelica::Connector, "Locator")
    descriptor = None
    for klass in avm::modelica::Connector.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)

def test_avm::modelica::connector_has_Class():
    assert hasattr(avm::modelica::Connector, "Class")
    descriptor = None
    for klass in avm::modelica::Connector.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)



def test_redeclare_is_not_abstract():
    assert not inspect.isabstract(Redeclare)


def test_redeclare_constructor_exists():
    assert callable(Redeclare.__init__)


def test_redeclare_constructor_args():
    sig = inspect.signature(Redeclare.__init__)
    params = list(sig.parameters.keys())



def test_limit_is_not_abstract():
    assert not inspect.isabstract(Limit)


def test_limit_constructor_exists():
    assert callable(Limit.__init__)


def test_limit_constructor_args():
    sig = inspect.signature(Limit.__init__)
    params = list(sig.parameters.keys())



def test_metric_is_not_abstract():
    assert not inspect.isabstract(Metric)


def test_metric_constructor_exists():
    assert callable(Metric.__init__)


def test_metric_constructor_args():
    sig = inspect.signature(Metric.__init__)
    params = list(sig.parameters.keys())



def test_valuenode_is_not_abstract():
    assert not inspect.isabstract(ValueNode)


def test_valuenode_constructor_exists():
    assert callable(ValueNode.__init__)


def test_valuenode_constructor_args():
    sig = inspect.signature(ValueNode.__init__)
    params = list(sig.parameters.keys())



def test_avm::valueflowmux_is_not_abstract():
    assert not inspect.isabstract(avm::ValueFlowMux)


def test_avm::valueflowmux_constructor_exists():
    assert callable(avm::ValueFlowMux.__init__)


def test_avm::valueflowmux_constructor_args():
    sig = inspect.signature(avm::ValueFlowMux.__init__)
    params = list(sig.parameters.keys())



def test_avm::value_is_not_abstract():
    assert not inspect.isabstract(avm::Value)


def test_avm::value_constructor_exists():
    assert callable(avm::Value.__init__)


def test_avm::value_constructor_args():
    sig = inspect.signature(avm::Value.__init__)
    params = list(sig.parameters.keys())
    assert "DataType" in params, "Missing parameter 'DataType'"
    assert "DimensionType" in params, "Missing parameter 'DimensionType'"
    assert "Unit" in params, "Missing parameter 'Unit'"
    assert "Dimensions" in params, "Missing parameter 'Dimensions'"

def test_avm::value_has_DataType():
    assert hasattr(avm::Value, "DataType")
    descriptor = None
    for klass in avm::Value.__mro__:
        if "DataType" in klass.__dict__:
            descriptor = klass.__dict__["DataType"]
            break
    assert isinstance(descriptor, property)

def test_avm::value_has_DimensionType():
    assert hasattr(avm::Value, "DimensionType")
    descriptor = None
    for klass in avm::Value.__mro__:
        if "DimensionType" in klass.__dict__:
            descriptor = klass.__dict__["DimensionType"]
            break
    assert isinstance(descriptor, property)

def test_avm::value_has_Unit():
    assert hasattr(avm::Value, "Unit")
    descriptor = None
    for klass in avm::Value.__mro__:
        if "Unit" in klass.__dict__:
            descriptor = klass.__dict__["Unit"]
            break
    assert isinstance(descriptor, property)

def test_avm::value_has_Dimensions():
    assert hasattr(avm::Value, "Dimensions")
    descriptor = None
    for klass in avm::Value.__mro__:
        if "Dimensions" in klass.__dict__:
            descriptor = klass.__dict__["Dimensions"]
            break
    assert isinstance(descriptor, property)



def test_avm::analysisconstruct_is_not_abstract():
    assert not inspect.isabstract(avm::AnalysisConstruct)


def test_avm::analysisconstruct_constructor_exists():
    assert callable(avm::AnalysisConstruct.__init__)


def test_avm::analysisconstruct_constructor_args():
    sig = inspect.signature(avm::AnalysisConstruct.__init__)
    params = list(sig.parameters.keys())



def test_avm::port_is_not_abstract():
    assert not inspect.isabstract(avm::Port)


def test_avm::port_constructor_exists():
    assert callable(avm::Port.__init__)


def test_avm::port_constructor_args():
    sig = inspect.signature(avm::Port.__init__)
    params = list(sig.parameters.keys())
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::port_has_Definition():
    assert hasattr(avm::Port, "Definition")
    descriptor = None
    for klass in avm::Port.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm::port_has_Notes():
    assert hasattr(avm::Port, "Notes")
    descriptor = None
    for klass in avm::Port.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::port_has_YPosition():
    assert hasattr(avm::Port, "YPosition")
    descriptor = None
    for klass in avm::Port.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::port_has_XPosition():
    assert hasattr(avm::Port, "XPosition")
    descriptor = None
    for klass in avm::Port.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::port_has_Name():
    assert hasattr(avm::Port, "Name")
    descriptor = None
    for klass in avm::Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm::distributionrestriction_is_not_abstract():
    assert not inspect.isabstract(avm::DistributionRestriction)


def test_avm::distributionrestriction_constructor_exists():
    assert callable(avm::DistributionRestriction.__init__)


def test_avm::distributionrestriction_constructor_args():
    sig = inspect.signature(avm::DistributionRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm::distributionrestriction_has_Notes():
    assert hasattr(avm::DistributionRestriction, "Notes")
    descriptor = None
    for klass in avm::DistributionRestriction.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_avm::connector_is_not_abstract():
    assert not inspect.isabstract(avm::Connector)


def test_avm::connector_constructor_exists():
    assert callable(avm::Connector.__init__)


def test_avm::connector_constructor_args():
    sig = inspect.signature(avm::Connector.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::connector_has_Name():
    assert hasattr(avm::Connector, "Name")
    descriptor = None
    for klass in avm::Connector.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::connector_has_YPosition():
    assert hasattr(avm::Connector, "YPosition")
    descriptor = None
    for klass in avm::Connector.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::connector_has_Notes():
    assert hasattr(avm::Connector, "Notes")
    descriptor = None
    for klass in avm::Connector.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::connector_has_Definition():
    assert hasattr(avm::Connector, "Definition")
    descriptor = None
    for klass in avm::Connector.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm::connector_has_XPosition():
    assert hasattr(avm::Connector, "XPosition")
    descriptor = None
    for klass in avm::Connector.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm::resource_is_not_abstract():
    assert not inspect.isabstract(avm::Resource)


def test_avm::resource_constructor_exists():
    assert callable(avm::Resource.__init__)


def test_avm::resource_constructor_args():
    sig = inspect.signature(avm::Resource.__init__)
    params = list(sig.parameters.keys())
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Path" in params, "Missing parameter 'Path'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Hash" in params, "Missing parameter 'Hash'"

def test_avm::resource_has_XPosition():
    assert hasattr(avm::Resource, "XPosition")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_Name():
    assert hasattr(avm::Resource, "Name")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_ID():
    assert hasattr(avm::Resource, "ID")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_YPosition():
    assert hasattr(avm::Resource, "YPosition")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_Path():
    assert hasattr(avm::Resource, "Path")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "Path" in klass.__dict__:
            descriptor = klass.__dict__["Path"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_Notes():
    assert hasattr(avm::Resource, "Notes")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::resource_has_Hash():
    assert hasattr(avm::Resource, "Hash")
    descriptor = None
    for klass in avm::Resource.__mro__:
        if "Hash" in klass.__dict__:
            descriptor = klass.__dict__["Hash"]
            break
    assert isinstance(descriptor, property)



def test_avm::property_is_not_abstract():
    assert not inspect.isabstract(avm::Property)


def test_avm::property_constructor_exists():
    assert callable(avm::Property.__init__)


def test_avm::property_constructor_args():
    sig = inspect.signature(avm::Property.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "OnDataSheet" in params, "Missing parameter 'OnDataSheet'"

def test_avm::property_has_ID():
    assert hasattr(avm::Property, "ID")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_Notes():
    assert hasattr(avm::Property, "Notes")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_XPosition():
    assert hasattr(avm::Property, "XPosition")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_Name():
    assert hasattr(avm::Property, "Name")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_Definition():
    assert hasattr(avm::Property, "Definition")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_YPosition():
    assert hasattr(avm::Property, "YPosition")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::property_has_OnDataSheet():
    assert hasattr(avm::Property, "OnDataSheet")
    descriptor = None
    for klass in avm::Property.__mro__:
        if "OnDataSheet" in klass.__dict__:
            descriptor = klass.__dict__["OnDataSheet"]
            break
    assert isinstance(descriptor, property)



def test_avm::formula_is_not_abstract():
    assert not inspect.isabstract(avm::Formula)


def test_avm::formula_constructor_exists():
    assert callable(avm::Formula.__init__)


def test_avm::formula_constructor_args():
    sig = inspect.signature(avm::Formula.__init__)
    params = list(sig.parameters.keys())
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::formula_has_YPosition():
    assert hasattr(avm::Formula, "YPosition")
    descriptor = None
    for klass in avm::Formula.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::formula_has_Name():
    assert hasattr(avm::Formula, "Name")
    descriptor = None
    for klass in avm::Formula.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::formula_has_XPosition():
    assert hasattr(avm::Formula, "XPosition")
    descriptor = None
    for klass in avm::Formula.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm::domainmodel__is_not_abstract():
    assert not inspect.isabstract(avm::DomainModel_)


def test_avm::domainmodel__constructor_exists():
    assert callable(avm::DomainModel_.__init__)


def test_avm::domainmodel__constructor_args():
    sig = inspect.signature(avm::DomainModel_.__init__)
    params = list(sig.parameters.keys())
    assert "Author" in params, "Missing parameter 'Author'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm::domainmodel__has_Author():
    assert hasattr(avm::DomainModel_, "Author")
    descriptor = None
    for klass in avm::DomainModel_.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodel__has_YPosition():
    assert hasattr(avm::DomainModel_, "YPosition")
    descriptor = None
    for klass in avm::DomainModel_.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodel__has_Notes():
    assert hasattr(avm::DomainModel_, "Notes")
    descriptor = None
    for klass in avm::DomainModel_.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodel__has_Name():
    assert hasattr(avm::DomainModel_, "Name")
    descriptor = None
    for klass in avm::DomainModel_.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm::domainmodel__has_XPosition():
    assert hasattr(avm::DomainModel_, "XPosition")
    descriptor = None
    for klass in avm::DomainModel_.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm::component_is_not_abstract():
    assert not inspect.isabstract(avm::Component)


def test_avm::component_constructor_exists():
    assert callable(avm::Component.__init__)


def test_avm::component_constructor_args():
    sig = inspect.signature(avm::Component.__init__)
    params = list(sig.parameters.keys())
    assert "SchemaVersion" in params, "Missing parameter 'SchemaVersion'"
    assert "Supercedes" in params, "Missing parameter 'Supercedes'"
    assert "Classifications" in params, "Missing parameter 'Classifications'"
    assert "Version" in params, "Missing parameter 'Version'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm::component_has_SchemaVersion():
    assert hasattr(avm::Component, "SchemaVersion")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "SchemaVersion" in klass.__dict__:
            descriptor = klass.__dict__["SchemaVersion"]
            break
    assert isinstance(descriptor, property)

def test_avm::component_has_Supercedes():
    assert hasattr(avm::Component, "Supercedes")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "Supercedes" in klass.__dict__:
            descriptor = klass.__dict__["Supercedes"]
            break
    assert isinstance(descriptor, property)

def test_avm::component_has_Classifications():
    assert hasattr(avm::Component, "Classifications")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "Classifications" in klass.__dict__:
            descriptor = klass.__dict__["Classifications"]
            break
    assert isinstance(descriptor, property)

def test_avm::component_has_Version():
    assert hasattr(avm::Component, "Version")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "Version" in klass.__dict__:
            descriptor = klass.__dict__["Version"]
            break
    assert isinstance(descriptor, property)

def test_avm::component_has_ID():
    assert hasattr(avm::Component, "ID")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm::component_has_Name():
    assert hasattr(avm::Component, "Name")
    descriptor = None
    for klass in avm::Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_modeltype_exists():
    # Check that the Enumeration exists
    assert ModelType is not None

def test_modeltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModelType]
    expected_literals = [
        "SignalFlow",
        "ESMoL",
        "Simulink",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModelType"

def test_doddistributionstatementenum_exists():
    # Check that the Enumeration exists
    assert DoDDistributionStatementEnum is not None

def test_doddistributionstatementenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DoDDistributionStatementEnum]
    expected_literals = [
        "StatementA",
        "StatementB",
        "StatementC",
        "StatementD",
        "StatementE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DoDDistributionStatementEnum"

def test_redeclaretypeenum_exists():
    # Check that the Enumeration exists
    assert RedeclareTypeEnum is not None

def test_redeclaretypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedeclareTypeEnum]
    expected_literals = [
        "Model",
        "Record",
        "Block",
        "Package",
        "Connector",
        "Function",
        "Class",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedeclareTypeEnum"

def test_datatypeenum_exists():
    # Check that the Enumeration exists
    assert DataTypeEnum is not None

def test_datatypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypeEnum]
    expected_literals = [
        "Boolean",
        "Integer",
        "String",
        "Real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypeEnum"

def test_geometryqualifierenum_exists():
    # Check that the Enumeration exists
    assert GeometryQualifierEnum is not None

def test_geometryqualifierenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GeometryQualifierEnum]
    expected_literals = [
        "InteriorOnly",
        "InteriorAndBoundary",
        "BoundaryOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GeometryQualifierEnum"

def test_boundtypeenum_exists():
    # Check that the Enumeration exists
    assert BoundTypeEnum is not None

def test_boundtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoundTypeEnum]
    expected_literals = [
        "MustExceedOrEqual",
        "MustExceed",
        "MustNotExceed",
        "MustNotMeetOrExceed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoundTypeEnum"

def test_partintersectionenum_exists():
    # Check that the Enumeration exists
    assert PartIntersectionEnum is not None

def test_partintersectionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PartIntersectionEnum]
    expected_literals = [
        "IntersectionWithAnyParts",
        "None_",
        "IntersectionWithReferencedParts",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PartIntersectionEnum"

def test_dimensiontypeenum_exists():
    # Check that the Enumeration exists
    assert DimensionTypeEnum is not None

def test_dimensiontypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DimensionTypeEnum]
    expected_literals = [
        "Matrix",
        "Scalar",
        "Vector",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DimensionTypeEnum"

def test_customgeometryinputoperationenum_exists():
    # Check that the Enumeration exists
    assert CustomGeometryInputOperationEnum is not None

def test_customgeometryinputoperationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomGeometryInputOperationEnum]
    expected_literals = [
        "Intersection",
        "Union",
        "Subtraction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomGeometryInputOperationEnum"

def test_intervalmethod_exists():
    # Check that the Enumeration exists
    assert IntervalMethod is not None

def test_intervalmethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntervalMethod]
    expected_literals = [
        "IntervalLength",
        "NumberOfIntervals",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntervalMethod"

def test_calculationtypeenum_exists():
    # Check that the Enumeration exists
    assert CalculationTypeEnum is not None

def test_calculationtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationTypeEnum]
    expected_literals = [
        "Declarative",
        "Python",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CalculationTypeEnum"

def test_simpleformulaoperation_exists():
    # Check that the Enumeration exists
    assert SimpleFormulaOperation is not None

def test_simpleformulaoperation_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleFormulaOperation]
    expected_literals = [
        "ArithmeticMean",
        "GeometricMean",
        "Maximum",
        "Minimum",
        "Addition",
        "Multiplication",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleFormulaOperation"

def test_jobmanagertoolselection_exists():
    # Check that the Enumeration exists
    assert JobManagerToolSelection is not None

def test_jobmanagertoolselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JobManagerToolSelection]
    expected_literals = [
        "Dymola_2014",
        "Dymola_2013",
        "OpenModelica_latest",
        "JModelica_1_12",
        "Dymola_latest",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JobManagerToolSelection"


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
Connector_strategy = st.builds(
    Connector,
)
Parameter_strategy = st.builds(
    Parameter,
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
avm::modelica::ModelicaModel_strategy = st.builds(
    avm::modelica::ModelicaModel,
    Class=
        safe_text
)
avm::WorkflowTaskBase_strategy = st.builds(
    avm::WorkflowTaskBase,
    Name=
        safe_text
)
avm::TestBenchValueBase_strategy = st.builds(
    avm::TestBenchValueBase,
    Name=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text,
    ID=
        safe_text,
    XPosition=
        safe_text
)
avm::ContainerInstanceBase_strategy = st.builds(
    avm::ContainerInstanceBase,
    IDinSourceModel=
        safe_text,
    YPosition=
        safe_text,
    XPosition=
        safe_text
)
TestBenchValueBase_strategy = st.builds(
    TestBenchValueBase,
)
ContainerInstanceBase_strategy = st.builds(
    ContainerInstanceBase,
)
avm::Settings_strategy = st.builds(
    avm::Settings,
)
avm::Workflow_strategy = st.builds(
    avm::Workflow,
    Name=
        safe_text
)
WorkflowTaskBase_strategy = st.builds(
    WorkflowTaskBase,
)
avm::ExecutionTask_strategy = st.builds(
    avm::ExecutionTask,
    Invocation=
        safe_text,
    Description=
        safe_text
)
avm::InterpreterTask_strategy = st.builds(
    avm::InterpreterTask,
    Parameters=
        safe_text,
    COMName=
        safe_text
)
avm::TopLevelSystemUnderTest_strategy = st.builds(
    avm::TopLevelSystemUnderTest,
    DesignID=
        safe_text
)
avm::TestBench_strategy = st.builds(
    avm::TestBench,
    Name=
        safe_text
)
avm::Operand_strategy = st.builds(
    avm::Operand,
    Symbol=
        safe_text
)
Formula_strategy = st.builds(
    Formula,
)
avm::ComplexFormula_strategy = st.builds(
    avm::ComplexFormula,
    Expression=
        safe_text
)
avm::SimpleFormula_strategy = st.builds(
    avm::SimpleFormula,
    Operation=
        safe_text
)
avm::TestInjectionPoint_strategy = st.builds(
    avm::TestInjectionPoint,
)
avm::Metric_strategy = st.builds(
    avm::Metric,
)
avm::Parameter_strategy = st.builds(
    avm::Parameter,
)
avm::PortMapTarget_strategy = st.builds(
    avm::PortMapTarget,
    ID=
        safe_text
)
avm::ComponentPrimitivePropertyInstance_strategy = st.builds(
    avm::ComponentPrimitivePropertyInstance,
    IDinComponentModel=
        safe_text
)
DesignSpaceContainer_strategy = st.builds(
    DesignSpaceContainer,
)
avm::Alternative_strategy = st.builds(
    avm::Alternative,
)
avm::Optional_strategy = st.builds(
    avm::Optional,
)
Container_strategy = st.builds(
    Container,
)
avm::DesignSpaceContainer_strategy = st.builds(
    avm::DesignSpaceContainer,
)
avm::Compound_strategy = st.builds(
    avm::Compound,
)
avm::ConnectorCompositionTarget_strategy = st.builds(
    avm::ConnectorCompositionTarget,
    ID=
        safe_text
)
avm::DesignDomainFeature_strategy = st.builds(
    avm::DesignDomainFeature,
)
avm::Container_strategy = st.builds(
    avm::Container,
    YPosition=
        safe_text,
    XPosition=
        safe_text,
    Name=
        safe_text
)
avm::Design_strategy = st.builds(
    avm::Design,
    DesignSpaceSrcID=
        safe_text,
    Name=
        safe_text,
    DesignID=
        safe_text,
    SchemaVersion=
        safe_text
)
avm::ComponentInstance_strategy = st.builds(
    avm::ComponentInstance,
    Name=
        safe_text,
    YPosition=
        safe_text,
    ComponentID=
        safe_text,
    DesignSpaceSrcComponentID=
        safe_text,
    ID=
        safe_text,
    XPosition=
        safe_text
)
avm::DomainModelMetric_strategy = st.builds(
    avm::DomainModelMetric,
    ID=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text,
    XPosition=
        safe_text
)
DistributionRestriction_strategy = st.builds(
    DistributionRestriction,
)
avm::Proprietary_strategy = st.builds(
    avm::Proprietary,
    Organization=
        safe_text
)
avm::DoDDistributionStatement_strategy = st.builds(
    avm::DoDDistributionStatement,
    Type=
        safe_text
)
avm::ITAR_strategy = st.builds(
    avm::ITAR,
)
avm::SecurityClassification_strategy = st.builds(
    avm::SecurityClassification,
    Level=
        safe_text
)
ProbabilisticValue_strategy = st.builds(
    ProbabilisticValue,
)
avm::NormalDistribution_strategy = st.builds(
    avm::NormalDistribution,
)
Property_strategy = st.builds(
    Property,
)
avm::CompoundProperty_strategy = st.builds(
    avm::CompoundProperty,
)
avm::PrimitiveProperty_strategy = st.builds(
    avm::PrimitiveProperty,
)
avm::UniformDistribution_strategy = st.builds(
    avm::UniformDistribution,
)
avm::DomainModelParameter_strategy = st.builds(
    avm::DomainModelParameter,
    YPosition=
        safe_text,
    XPosition=
        safe_text,
    Notes=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
avm::AbstractPort_strategy = st.builds(
    avm::AbstractPort,
)
avm::DomainModelPort_strategy = st.builds(
    avm::DomainModelPort,
)
PortMapTarget_strategy = st.builds(
    PortMapTarget,
)
avm::ComponentPortInstance_strategy = st.builds(
    avm::ComponentPortInstance,
    IDinComponentModel=
        safe_text
)
avm::ConnectorFeature_strategy = st.builds(
    avm::ConnectorFeature,
)
avm::assemblyDetail_strategy = st.builds(
    avm::assemblyDetail,
)
ConnectorCompositionTarget_strategy = st.builds(
    ConnectorCompositionTarget,
)
avm::ComponentConnectorInstance_strategy = st.builds(
    avm::ComponentConnectorInstance,
    IDinComponentModel=
        safe_text
)
avm::ValueNode_strategy = st.builds(
    avm::ValueNode,
    ID=
        safe_text
)
ValueExpressionType_strategy = st.builds(
    ValueExpressionType,
)
avm::ParametricEnumeratedValue_strategy = st.builds(
    avm::ParametricEnumeratedValue,
)
avm::DerivedValue_strategy = st.builds(
    avm::DerivedValue,
)
avm::ProbabilisticValue_strategy = st.builds(
    avm::ProbabilisticValue,
)
avm::CalculatedValue_strategy = st.builds(
    avm::CalculatedValue,
    Type=
        safe_text,
    Expression=
        safe_text
)
avm::ParametricValue_strategy = st.builds(
    avm::ParametricValue,
)
avm::FixedValue_strategy = st.builds(
    avm::FixedValue,
    Value=
        safe_text,
    Uncertainty=
        safe_text
)
avm::DataSource_strategy = st.builds(
    avm::DataSource,
    Notes=
        safe_text
)
avm::ValueExpressionType_strategy = st.builds(
    avm::ValueExpressionType,
)
avm::cyber::CyberModel_strategy = st.builds(
    avm::cyber::CyberModel,
    Type=
        safe_text,
    Locator=
        safe_text,
    Class=
        safe_text
)
manufacturing::avm::Value_strategy = st.builds(
    manufacturing::avm::Value,
)
avm::manufacturing::ManufacturingModel_strategy = st.builds(
    avm::manufacturing::ManufacturingModel,
)
avm::adamsCar::FileReference_strategy = st.builds(
    avm::adamsCar::FileReference,
    ID=
        safe_text,
    Name=
        safe_text,
    FilePath=
        safe_text
)
adamsCar::avm::Value_strategy = st.builds(
    adamsCar::avm::Value,
)
FileReference_strategy = st.builds(
    FileReference,
)
avm::adamsCar::AdamsCarModel_strategy = st.builds(
    avm::adamsCar::AdamsCarModel,
)
Axis_strategy = st.builds(
    Axis,
)
KinematicJointSpec_strategy = st.builds(
    KinematicJointSpec,
)
avm::cad::RevoluteJointSpec_strategy = st.builds(
    avm::cad::RevoluteJointSpec,
)
cad::avm::ComponentInstance_strategy = st.builds(
    cad::avm::ComponentInstance,
)
DesignDomainFeature_strategy = st.builds(
    DesignDomainFeature,
)
avm::cad::AssemblyRoot_strategy = st.builds(
    avm::cad::AssemblyRoot,
)
ConnectorFeature_strategy = st.builds(
    ConnectorFeature,
)
avm::cad::KinematicJointSpec_strategy = st.builds(
    avm::cad::KinematicJointSpec,
)
avm::cad::GuideDatum_strategy = st.builds(
    avm::cad::GuideDatum,
)
avm::cad::PlaneReference_strategy = st.builds(
    avm::cad::PlaneReference,
)
PlaneReference_strategy = st.builds(
    PlaneReference,
)
avm::cad::TranslationalJointSpec_strategy = st.builds(
    avm::cad::TranslationalJointSpec,
)
avm::cad::CustomGeometryInput_strategy = st.builds(
    avm::cad::CustomGeometryInput,
    Operation=
        safe_text
)
CustomGeometryInput_strategy = st.builds(
    CustomGeometryInput,
)
Geometry3D_strategy = st.builds(
    Geometry3D,
)
avm::cad::Sphere_strategy = st.builds(
    avm::cad::Sphere,
)
avm::cad::ExtrudedGeometry_strategy = st.builds(
    avm::cad::ExtrudedGeometry,
)
avm::cad::Surface_strategy = st.builds(
    avm::cad::Surface,
)
Point_strategy = st.builds(
    Point,
)
avm::cad::PointReference_strategy = st.builds(
    avm::cad::PointReference,
)
AnalysisConstruct_strategy = st.builds(
    AnalysisConstruct,
)
avm::cad::Geometry_strategy = st.builds(
    avm::cad::Geometry,
    PartIntersectionModifier=
        safe_text,
    GeometryQualifier=
        safe_text
)
Plane_strategy = st.builds(
    Plane,
)
cad::avm::Value_strategy = st.builds(
    cad::avm::Value,
)
PointReference_strategy = st.builds(
    PointReference,
)
Geometry2D_strategy = st.builds(
    Geometry2D,
)
avm::cad::Polygon_strategy = st.builds(
    avm::cad::Polygon,
)
avm::cad::Circle_strategy = st.builds(
    avm::cad::Circle,
)
Geometry_strategy = st.builds(
    Geometry,
)
avm::cad::CustomGeometry_strategy = st.builds(
    avm::cad::CustomGeometry,
)
avm::cad::Geometry3D_strategy = st.builds(
    avm::cad::Geometry3D,
)
avm::cad::Geometry2D_strategy = st.builds(
    avm::cad::Geometry2D,
)
Datum_strategy = st.builds(
    Datum,
)
avm::cad::Plane_strategy = st.builds(
    avm::cad::Plane,
)
avm::cad::Axis_strategy = st.builds(
    avm::cad::Axis,
)
avm::cad::Point_strategy = st.builds(
    avm::cad::Point,
)
avm::cad::CoordinateSystem_strategy = st.builds(
    avm::cad::CoordinateSystem,
)
avm::cad::CADModel_strategy = st.builds(
    avm::cad::CADModel,
)
Settings_strategy = st.builds(
    Settings,
)
avm::modelica::SolverSettings_strategy = st.builds(
    avm::modelica::SolverSettings,
    Solver=
        safe_text,
    NumberOfIntervals=
        safe_text,
    JobManagerToolSelection=
        safe_text,
    IntervalLength=
        safe_text,
    ToolSpecificAnnotations=
        safe_text,
    StartTime=
        safe_text,
    Tolerance=
        safe_text,
    StopTime=
        safe_text,
    IntervalMethod=
        safe_text
)
avm::modelica::Limit_strategy = st.builds(
    avm::modelica::Limit,
    BoundType=
        safe_text,
    Name=
        safe_text,
    ToleranceTimeWindow=
        safe_text,
    Notes=
        safe_text,
    VariableLocator=
        safe_text
)
DomainModelMetric_strategy = st.builds(
    DomainModelMetric,
)
avm::manufacturing::Metric_strategy = st.builds(
    avm::manufacturing::Metric,
    Name=
        safe_text
)
avm::cad::Metric_strategy = st.builds(
    avm::cad::Metric,
    Name=
        safe_text
)
avm::modelica::Metric_strategy = st.builds(
    avm::modelica::Metric,
    Locator=
        safe_text
)
modelica::avm::Value_strategy = st.builds(
    modelica::avm::Value,
)
DomainModelParameter_strategy = st.builds(
    DomainModelParameter,
)
avm::modelica::Redeclare_strategy = st.builds(
    avm::modelica::Redeclare,
    Type=
        safe_text,
    Locator=
        safe_text
)
avm::adamsCar::Parameter_strategy = st.builds(
    avm::adamsCar::Parameter,
    ID=
        safe_text,
    Name=
        safe_text
)
avm::manufacturing::Parameter_strategy = st.builds(
    avm::manufacturing::Parameter,
    Locator=
        safe_text,
    Name=
        safe_text
)
avm::cad::Parameter_strategy = st.builds(
    avm::cad::Parameter,
    Name=
        safe_text
)
avm::modelica::Parameter_strategy = st.builds(
    avm::modelica::Parameter,
    Locator=
        safe_text
)
DomainModelPort_strategy = st.builds(
    DomainModelPort,
)
avm::cad::Datum_strategy = st.builds(
    avm::cad::Datum,
    DatumName=
        safe_text
)
avm::modelica::Connector_strategy = st.builds(
    avm::modelica::Connector,
    Locator=
        safe_text,
    Class=
        safe_text
)
Redeclare_strategy = st.builds(
    Redeclare,
)
Limit_strategy = st.builds(
    Limit,
)
Metric_strategy = st.builds(
    Metric,
)
ValueNode_strategy = st.builds(
    ValueNode,
)
avm::ValueFlowMux_strategy = st.builds(
    avm::ValueFlowMux,
)
avm::Value_strategy = st.builds(
    avm::Value,
    DataType=
        safe_text,
    DimensionType=
        safe_text,
    Unit=
        safe_text,
    Dimensions=
        safe_text
)
avm::AnalysisConstruct_strategy = st.builds(
    avm::AnalysisConstruct,
)
avm::Port_strategy = st.builds(
    avm::Port,
    Definition=
        safe_text,
    Notes=
        safe_text,
    YPosition=
        safe_text,
    XPosition=
        safe_text,
    Name=
        safe_text
)
avm::DistributionRestriction_strategy = st.builds(
    avm::DistributionRestriction,
    Notes=
        safe_text
)
avm::Connector_strategy = st.builds(
    avm::Connector,
    Name=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text,
    Definition=
        safe_text,
    XPosition=
        safe_text
)
avm::Resource_strategy = st.builds(
    avm::Resource,
    XPosition=
        safe_text,
    Name=
        safe_text,
    ID=
        safe_text,
    YPosition=
        safe_text,
    Path=
        safe_text,
    Notes=
        safe_text,
    Hash=
        safe_text
)
avm::Property_strategy = st.builds(
    avm::Property,
    ID=
        safe_text,
    Notes=
        safe_text,
    XPosition=
        safe_text,
    Name=
        safe_text,
    Definition=
        safe_text,
    YPosition=
        safe_text,
    OnDataSheet=
        safe_text
)
avm::Formula_strategy = st.builds(
    avm::Formula,
    YPosition=
        safe_text,
    Name=
        safe_text,
    XPosition=
        safe_text
)
avm::DomainModel__strategy = st.builds(
    avm::DomainModel_,
    Author=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text,
    Name=
        safe_text,
    XPosition=
        safe_text
)
avm::Component_strategy = st.builds(
    avm::Component,
    SchemaVersion=
        safe_text,
    Supercedes=
        safe_text,
    Classifications=
        safe_text,
    Version=
        safe_text,
    ID=
        safe_text,
    Name=
        safe_text
)

@given(instance=Connector_strategy)
@settings(max_examples=50)
def test_connector_instantiation(instance):
    assert isinstance(instance, Connector)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=DomainModel__strategy)
@settings(max_examples=50)
def test_domainmodel__instantiation(instance):
    assert isinstance(instance, DomainModel_)

@given(instance=avm::modelica::ModelicaModel_strategy)
@settings(max_examples=50)
def test_avm::modelica::modelicamodel_instantiation(instance):
    assert isinstance(instance, avm::modelica::ModelicaModel)

@given(instance=avm::modelica::ModelicaModel_strategy)
def test_avm::modelica::modelicamodel_Class_type(instance):
    assert isinstance(instance.Class, str)


@given(instance=avm::modelica::ModelicaModel_strategy)
def test_avm::modelica::modelicamodel_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original

@given(instance=avm::WorkflowTaskBase_strategy)
@settings(max_examples=50)
def test_avm::workflowtaskbase_instantiation(instance):
    assert isinstance(instance, avm::WorkflowTaskBase)

@given(instance=avm::WorkflowTaskBase_strategy)
def test_avm::workflowtaskbase_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::WorkflowTaskBase_strategy)
def test_avm::workflowtaskbase_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::TestBenchValueBase_strategy)
@settings(max_examples=50)
def test_avm::testbenchvaluebase_instantiation(instance):
    assert isinstance(instance, avm::TestBenchValueBase)

@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::TestBenchValueBase_strategy)
def test_avm::testbenchvaluebase_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::ContainerInstanceBase_strategy)
@settings(max_examples=50)
def test_avm::containerinstancebase_instantiation(instance):
    assert isinstance(instance, avm::ContainerInstanceBase)

@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_IDinSourceModel_type(instance):
    assert isinstance(instance.IDinSourceModel, str)


@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_IDinSourceModel_setter(instance):
    original = instance.IDinSourceModel
    instance.IDinSourceModel = original
    assert instance.IDinSourceModel == original

@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::ContainerInstanceBase_strategy)
def test_avm::containerinstancebase_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=TestBenchValueBase_strategy)
@settings(max_examples=50)
def test_testbenchvaluebase_instantiation(instance):
    assert isinstance(instance, TestBenchValueBase)

@given(instance=ContainerInstanceBase_strategy)
@settings(max_examples=50)
def test_containerinstancebase_instantiation(instance):
    assert isinstance(instance, ContainerInstanceBase)

@given(instance=avm::Settings_strategy)
@settings(max_examples=50)
def test_avm::settings_instantiation(instance):
    assert isinstance(instance, avm::Settings)

@given(instance=avm::Workflow_strategy)
@settings(max_examples=50)
def test_avm::workflow_instantiation(instance):
    assert isinstance(instance, avm::Workflow)

@given(instance=avm::Workflow_strategy)
def test_avm::workflow_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Workflow_strategy)
def test_avm::workflow_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=WorkflowTaskBase_strategy)
@settings(max_examples=50)
def test_workflowtaskbase_instantiation(instance):
    assert isinstance(instance, WorkflowTaskBase)

@given(instance=avm::ExecutionTask_strategy)
@settings(max_examples=50)
def test_avm::executiontask_instantiation(instance):
    assert isinstance(instance, avm::ExecutionTask)

@given(instance=avm::ExecutionTask_strategy)
def test_avm::executiontask_Invocation_type(instance):
    assert isinstance(instance.Invocation, str)


@given(instance=avm::ExecutionTask_strategy)
def test_avm::executiontask_Invocation_setter(instance):
    original = instance.Invocation
    instance.Invocation = original
    assert instance.Invocation == original

@given(instance=avm::ExecutionTask_strategy)
def test_avm::executiontask_Description_type(instance):
    assert isinstance(instance.Description, str)


@given(instance=avm::ExecutionTask_strategy)
def test_avm::executiontask_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=avm::InterpreterTask_strategy)
@settings(max_examples=50)
def test_avm::interpretertask_instantiation(instance):
    assert isinstance(instance, avm::InterpreterTask)

@given(instance=avm::InterpreterTask_strategy)
def test_avm::interpretertask_Parameters_type(instance):
    assert isinstance(instance.Parameters, str)


@given(instance=avm::InterpreterTask_strategy)
def test_avm::interpretertask_Parameters_setter(instance):
    original = instance.Parameters
    instance.Parameters = original
    assert instance.Parameters == original

@given(instance=avm::InterpreterTask_strategy)
def test_avm::interpretertask_COMName_type(instance):
    assert isinstance(instance.COMName, str)


@given(instance=avm::InterpreterTask_strategy)
def test_avm::interpretertask_COMName_setter(instance):
    original = instance.COMName
    instance.COMName = original
    assert instance.COMName == original

@given(instance=avm::TopLevelSystemUnderTest_strategy)
@settings(max_examples=50)
def test_avm::toplevelsystemundertest_instantiation(instance):
    assert isinstance(instance, avm::TopLevelSystemUnderTest)

@given(instance=avm::TopLevelSystemUnderTest_strategy)
def test_avm::toplevelsystemundertest_DesignID_type(instance):
    assert isinstance(instance.DesignID, str)


@given(instance=avm::TopLevelSystemUnderTest_strategy)
def test_avm::toplevelsystemundertest_DesignID_setter(instance):
    original = instance.DesignID
    instance.DesignID = original
    assert instance.DesignID == original

@given(instance=avm::TestBench_strategy)
@settings(max_examples=50)
def test_avm::testbench_instantiation(instance):
    assert isinstance(instance, avm::TestBench)

@given(instance=avm::TestBench_strategy)
def test_avm::testbench_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::TestBench_strategy)
def test_avm::testbench_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Operand_strategy)
@settings(max_examples=50)
def test_avm::operand_instantiation(instance):
    assert isinstance(instance, avm::Operand)

@given(instance=avm::Operand_strategy)
def test_avm::operand_Symbol_type(instance):
    assert isinstance(instance.Symbol, str)


@given(instance=avm::Operand_strategy)
def test_avm::operand_Symbol_setter(instance):
    original = instance.Symbol
    instance.Symbol = original
    assert instance.Symbol == original

@given(instance=Formula_strategy)
@settings(max_examples=50)
def test_formula_instantiation(instance):
    assert isinstance(instance, Formula)

@given(instance=avm::ComplexFormula_strategy)
@settings(max_examples=50)
def test_avm::complexformula_instantiation(instance):
    assert isinstance(instance, avm::ComplexFormula)

@given(instance=avm::ComplexFormula_strategy)
def test_avm::complexformula_Expression_type(instance):
    assert isinstance(instance.Expression, str)


@given(instance=avm::ComplexFormula_strategy)
def test_avm::complexformula_Expression_setter(instance):
    original = instance.Expression
    instance.Expression = original
    assert instance.Expression == original

@given(instance=avm::SimpleFormula_strategy)
@settings(max_examples=50)
def test_avm::simpleformula_instantiation(instance):
    assert isinstance(instance, avm::SimpleFormula)

@given(instance=avm::SimpleFormula_strategy)
def test_avm::simpleformula_Operation_type(instance):
    assert isinstance(instance.Operation, str)


@given(instance=avm::SimpleFormula_strategy)
def test_avm::simpleformula_Operation_setter(instance):
    original = instance.Operation
    instance.Operation = original
    assert instance.Operation == original

@given(instance=avm::TestInjectionPoint_strategy)
@settings(max_examples=50)
def test_avm::testinjectionpoint_instantiation(instance):
    assert isinstance(instance, avm::TestInjectionPoint)

@given(instance=avm::Metric_strategy)
@settings(max_examples=50)
def test_avm::metric_instantiation(instance):
    assert isinstance(instance, avm::Metric)

@given(instance=avm::Parameter_strategy)
@settings(max_examples=50)
def test_avm::parameter_instantiation(instance):
    assert isinstance(instance, avm::Parameter)

@given(instance=avm::PortMapTarget_strategy)
@settings(max_examples=50)
def test_avm::portmaptarget_instantiation(instance):
    assert isinstance(instance, avm::PortMapTarget)

@given(instance=avm::PortMapTarget_strategy)
def test_avm::portmaptarget_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::PortMapTarget_strategy)
def test_avm::portmaptarget_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::ComponentPrimitivePropertyInstance_strategy)
@settings(max_examples=50)
def test_avm::componentprimitivepropertyinstance_instantiation(instance):
    assert isinstance(instance, avm::ComponentPrimitivePropertyInstance)

@given(instance=avm::ComponentPrimitivePropertyInstance_strategy)
def test_avm::componentprimitivepropertyinstance_IDinComponentModel_type(instance):
    assert isinstance(instance.IDinComponentModel, str)


@given(instance=avm::ComponentPrimitivePropertyInstance_strategy)
def test_avm::componentprimitivepropertyinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=DesignSpaceContainer_strategy)
@settings(max_examples=50)
def test_designspacecontainer_instantiation(instance):
    assert isinstance(instance, DesignSpaceContainer)

@given(instance=avm::Alternative_strategy)
@settings(max_examples=50)
def test_avm::alternative_instantiation(instance):
    assert isinstance(instance, avm::Alternative)

@given(instance=avm::Optional_strategy)
@settings(max_examples=50)
def test_avm::optional_instantiation(instance):
    assert isinstance(instance, avm::Optional)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=avm::DesignSpaceContainer_strategy)
@settings(max_examples=50)
def test_avm::designspacecontainer_instantiation(instance):
    assert isinstance(instance, avm::DesignSpaceContainer)

@given(instance=avm::Compound_strategy)
@settings(max_examples=50)
def test_avm::compound_instantiation(instance):
    assert isinstance(instance, avm::Compound)

@given(instance=avm::ConnectorCompositionTarget_strategy)
@settings(max_examples=50)
def test_avm::connectorcompositiontarget_instantiation(instance):
    assert isinstance(instance, avm::ConnectorCompositionTarget)

@given(instance=avm::ConnectorCompositionTarget_strategy)
def test_avm::connectorcompositiontarget_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::ConnectorCompositionTarget_strategy)
def test_avm::connectorcompositiontarget_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::DesignDomainFeature_strategy)
@settings(max_examples=50)
def test_avm::designdomainfeature_instantiation(instance):
    assert isinstance(instance, avm::DesignDomainFeature)

@given(instance=avm::Container_strategy)
@settings(max_examples=50)
def test_avm::container_instantiation(instance):
    assert isinstance(instance, avm::Container)

@given(instance=avm::Container_strategy)
def test_avm::container_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Container_strategy)
def test_avm::container_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Container_strategy)
def test_avm::container_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Container_strategy)
def test_avm::container_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Container_strategy)
def test_avm::container_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Container_strategy)
def test_avm::container_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Design_strategy)
@settings(max_examples=50)
def test_avm::design_instantiation(instance):
    assert isinstance(instance, avm::Design)

@given(instance=avm::Design_strategy)
def test_avm::design_DesignSpaceSrcID_type(instance):
    assert isinstance(instance.DesignSpaceSrcID, str)


@given(instance=avm::Design_strategy)
def test_avm::design_DesignSpaceSrcID_setter(instance):
    original = instance.DesignSpaceSrcID
    instance.DesignSpaceSrcID = original
    assert instance.DesignSpaceSrcID == original

@given(instance=avm::Design_strategy)
def test_avm::design_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Design_strategy)
def test_avm::design_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Design_strategy)
def test_avm::design_DesignID_type(instance):
    assert isinstance(instance.DesignID, str)


@given(instance=avm::Design_strategy)
def test_avm::design_DesignID_setter(instance):
    original = instance.DesignID
    instance.DesignID = original
    assert instance.DesignID == original

@given(instance=avm::Design_strategy)
def test_avm::design_SchemaVersion_type(instance):
    assert isinstance(instance.SchemaVersion, str)


@given(instance=avm::Design_strategy)
def test_avm::design_SchemaVersion_setter(instance):
    original = instance.SchemaVersion
    instance.SchemaVersion = original
    assert instance.SchemaVersion == original

@given(instance=avm::ComponentInstance_strategy)
@settings(max_examples=50)
def test_avm::componentinstance_instantiation(instance):
    assert isinstance(instance, avm::ComponentInstance)

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_ComponentID_type(instance):
    assert isinstance(instance.ComponentID, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_ComponentID_setter(instance):
    original = instance.ComponentID
    instance.ComponentID = original
    assert instance.ComponentID == original

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_DesignSpaceSrcComponentID_type(instance):
    assert isinstance(instance.DesignSpaceSrcComponentID, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_DesignSpaceSrcComponentID_setter(instance):
    original = instance.DesignSpaceSrcComponentID
    instance.DesignSpaceSrcComponentID = original
    assert instance.DesignSpaceSrcComponentID == original

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::ComponentInstance_strategy)
def test_avm::componentinstance_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::DomainModelMetric_strategy)
@settings(max_examples=50)
def test_avm::domainmodelmetric_instantiation(instance):
    assert isinstance(instance, avm::DomainModelMetric)

@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::DomainModelMetric_strategy)
def test_avm::domainmodelmetric_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=DistributionRestriction_strategy)
@settings(max_examples=50)
def test_distributionrestriction_instantiation(instance):
    assert isinstance(instance, DistributionRestriction)

@given(instance=avm::Proprietary_strategy)
@settings(max_examples=50)
def test_avm::proprietary_instantiation(instance):
    assert isinstance(instance, avm::Proprietary)

@given(instance=avm::Proprietary_strategy)
def test_avm::proprietary_Organization_type(instance):
    assert isinstance(instance.Organization, str)


@given(instance=avm::Proprietary_strategy)
def test_avm::proprietary_Organization_setter(instance):
    original = instance.Organization
    instance.Organization = original
    assert instance.Organization == original

@given(instance=avm::DoDDistributionStatement_strategy)
@settings(max_examples=50)
def test_avm::doddistributionstatement_instantiation(instance):
    assert isinstance(instance, avm::DoDDistributionStatement)

@given(instance=avm::DoDDistributionStatement_strategy)
def test_avm::doddistributionstatement_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=avm::DoDDistributionStatement_strategy)
def test_avm::doddistributionstatement_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm::ITAR_strategy)
@settings(max_examples=50)
def test_avm::itar_instantiation(instance):
    assert isinstance(instance, avm::ITAR)

@given(instance=avm::SecurityClassification_strategy)
@settings(max_examples=50)
def test_avm::securityclassification_instantiation(instance):
    assert isinstance(instance, avm::SecurityClassification)

@given(instance=avm::SecurityClassification_strategy)
def test_avm::securityclassification_Level_type(instance):
    assert isinstance(instance.Level, str)


@given(instance=avm::SecurityClassification_strategy)
def test_avm::securityclassification_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=ProbabilisticValue_strategy)
@settings(max_examples=50)
def test_probabilisticvalue_instantiation(instance):
    assert isinstance(instance, ProbabilisticValue)

@given(instance=avm::NormalDistribution_strategy)
@settings(max_examples=50)
def test_avm::normaldistribution_instantiation(instance):
    assert isinstance(instance, avm::NormalDistribution)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=avm::CompoundProperty_strategy)
@settings(max_examples=50)
def test_avm::compoundproperty_instantiation(instance):
    assert isinstance(instance, avm::CompoundProperty)

@given(instance=avm::PrimitiveProperty_strategy)
@settings(max_examples=50)
def test_avm::primitiveproperty_instantiation(instance):
    assert isinstance(instance, avm::PrimitiveProperty)

@given(instance=avm::UniformDistribution_strategy)
@settings(max_examples=50)
def test_avm::uniformdistribution_instantiation(instance):
    assert isinstance(instance, avm::UniformDistribution)

@given(instance=avm::DomainModelParameter_strategy)
@settings(max_examples=50)
def test_avm::domainmodelparameter_instantiation(instance):
    assert isinstance(instance, avm::DomainModelParameter)

@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::DomainModelParameter_strategy)
def test_avm::domainmodelparameter_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=avm::AbstractPort_strategy)
@settings(max_examples=50)
def test_avm::abstractport_instantiation(instance):
    assert isinstance(instance, avm::AbstractPort)

@given(instance=avm::DomainModelPort_strategy)
@settings(max_examples=50)
def test_avm::domainmodelport_instantiation(instance):
    assert isinstance(instance, avm::DomainModelPort)

@given(instance=PortMapTarget_strategy)
@settings(max_examples=50)
def test_portmaptarget_instantiation(instance):
    assert isinstance(instance, PortMapTarget)

@given(instance=avm::ComponentPortInstance_strategy)
@settings(max_examples=50)
def test_avm::componentportinstance_instantiation(instance):
    assert isinstance(instance, avm::ComponentPortInstance)

@given(instance=avm::ComponentPortInstance_strategy)
def test_avm::componentportinstance_IDinComponentModel_type(instance):
    assert isinstance(instance.IDinComponentModel, str)


@given(instance=avm::ComponentPortInstance_strategy)
def test_avm::componentportinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=avm::ConnectorFeature_strategy)
@settings(max_examples=50)
def test_avm::connectorfeature_instantiation(instance):
    assert isinstance(instance, avm::ConnectorFeature)

@given(instance=avm::assemblyDetail_strategy)
@settings(max_examples=50)
def test_avm::assemblydetail_instantiation(instance):
    assert isinstance(instance, avm::assemblyDetail)

@given(instance=ConnectorCompositionTarget_strategy)
@settings(max_examples=50)
def test_connectorcompositiontarget_instantiation(instance):
    assert isinstance(instance, ConnectorCompositionTarget)

@given(instance=avm::ComponentConnectorInstance_strategy)
@settings(max_examples=50)
def test_avm::componentconnectorinstance_instantiation(instance):
    assert isinstance(instance, avm::ComponentConnectorInstance)

@given(instance=avm::ComponentConnectorInstance_strategy)
def test_avm::componentconnectorinstance_IDinComponentModel_type(instance):
    assert isinstance(instance.IDinComponentModel, str)


@given(instance=avm::ComponentConnectorInstance_strategy)
def test_avm::componentconnectorinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=avm::ValueNode_strategy)
@settings(max_examples=50)
def test_avm::valuenode_instantiation(instance):
    assert isinstance(instance, avm::ValueNode)

@given(instance=avm::ValueNode_strategy)
def test_avm::valuenode_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::ValueNode_strategy)
def test_avm::valuenode_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ValueExpressionType_strategy)
@settings(max_examples=50)
def test_valueexpressiontype_instantiation(instance):
    assert isinstance(instance, ValueExpressionType)

@given(instance=avm::ParametricEnumeratedValue_strategy)
@settings(max_examples=50)
def test_avm::parametricenumeratedvalue_instantiation(instance):
    assert isinstance(instance, avm::ParametricEnumeratedValue)

@given(instance=avm::DerivedValue_strategy)
@settings(max_examples=50)
def test_avm::derivedvalue_instantiation(instance):
    assert isinstance(instance, avm::DerivedValue)

@given(instance=avm::ProbabilisticValue_strategy)
@settings(max_examples=50)
def test_avm::probabilisticvalue_instantiation(instance):
    assert isinstance(instance, avm::ProbabilisticValue)

@given(instance=avm::CalculatedValue_strategy)
@settings(max_examples=50)
def test_avm::calculatedvalue_instantiation(instance):
    assert isinstance(instance, avm::CalculatedValue)

@given(instance=avm::CalculatedValue_strategy)
def test_avm::calculatedvalue_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=avm::CalculatedValue_strategy)
def test_avm::calculatedvalue_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm::CalculatedValue_strategy)
def test_avm::calculatedvalue_Expression_type(instance):
    assert isinstance(instance.Expression, str)


@given(instance=avm::CalculatedValue_strategy)
def test_avm::calculatedvalue_Expression_setter(instance):
    original = instance.Expression
    instance.Expression = original
    assert instance.Expression == original

@given(instance=avm::ParametricValue_strategy)
@settings(max_examples=50)
def test_avm::parametricvalue_instantiation(instance):
    assert isinstance(instance, avm::ParametricValue)

@given(instance=avm::FixedValue_strategy)
@settings(max_examples=50)
def test_avm::fixedvalue_instantiation(instance):
    assert isinstance(instance, avm::FixedValue)

@given(instance=avm::FixedValue_strategy)
def test_avm::fixedvalue_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=avm::FixedValue_strategy)
def test_avm::fixedvalue_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=avm::FixedValue_strategy)
def test_avm::fixedvalue_Uncertainty_type(instance):
    assert isinstance(instance.Uncertainty, str)


@given(instance=avm::FixedValue_strategy)
def test_avm::fixedvalue_Uncertainty_setter(instance):
    original = instance.Uncertainty
    instance.Uncertainty = original
    assert instance.Uncertainty == original

@given(instance=avm::DataSource_strategy)
@settings(max_examples=50)
def test_avm::datasource_instantiation(instance):
    assert isinstance(instance, avm::DataSource)

@given(instance=avm::DataSource_strategy)
def test_avm::datasource_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::DataSource_strategy)
def test_avm::datasource_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::ValueExpressionType_strategy)
@settings(max_examples=50)
def test_avm::valueexpressiontype_instantiation(instance):
    assert isinstance(instance, avm::ValueExpressionType)

@given(instance=avm::cyber::CyberModel_strategy)
@settings(max_examples=50)
def test_avm::cyber::cybermodel_instantiation(instance):
    assert isinstance(instance, avm::cyber::CyberModel)

@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Class_type(instance):
    assert isinstance(instance.Class, str)


@given(instance=avm::cyber::CyberModel_strategy)
def test_avm::cyber::cybermodel_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original

@given(instance=manufacturing::avm::Value_strategy)
@settings(max_examples=50)
def test_manufacturing::avm::value_instantiation(instance):
    assert isinstance(instance, manufacturing::avm::Value)

@given(instance=avm::manufacturing::ManufacturingModel_strategy)
@settings(max_examples=50)
def test_avm::manufacturing::manufacturingmodel_instantiation(instance):
    assert isinstance(instance, avm::manufacturing::ManufacturingModel)

@given(instance=avm::adamsCar::FileReference_strategy)
@settings(max_examples=50)
def test_avm::adamscar::filereference_instantiation(instance):
    assert isinstance(instance, avm::adamsCar::FileReference)

@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_FilePath_type(instance):
    assert isinstance(instance.FilePath, str)


@given(instance=avm::adamsCar::FileReference_strategy)
def test_avm::adamscar::filereference_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original

@given(instance=adamsCar::avm::Value_strategy)
@settings(max_examples=50)
def test_adamscar::avm::value_instantiation(instance):
    assert isinstance(instance, adamsCar::avm::Value)

@given(instance=FileReference_strategy)
@settings(max_examples=50)
def test_filereference_instantiation(instance):
    assert isinstance(instance, FileReference)

@given(instance=avm::adamsCar::AdamsCarModel_strategy)
@settings(max_examples=50)
def test_avm::adamscar::adamscarmodel_instantiation(instance):
    assert isinstance(instance, avm::adamsCar::AdamsCarModel)

@given(instance=Axis_strategy)
@settings(max_examples=50)
def test_axis_instantiation(instance):
    assert isinstance(instance, Axis)

@given(instance=KinematicJointSpec_strategy)
@settings(max_examples=50)
def test_kinematicjointspec_instantiation(instance):
    assert isinstance(instance, KinematicJointSpec)

@given(instance=avm::cad::RevoluteJointSpec_strategy)
@settings(max_examples=50)
def test_avm::cad::revolutejointspec_instantiation(instance):
    assert isinstance(instance, avm::cad::RevoluteJointSpec)

@given(instance=cad::avm::ComponentInstance_strategy)
@settings(max_examples=50)
def test_cad::avm::componentinstance_instantiation(instance):
    assert isinstance(instance, cad::avm::ComponentInstance)

@given(instance=DesignDomainFeature_strategy)
@settings(max_examples=50)
def test_designdomainfeature_instantiation(instance):
    assert isinstance(instance, DesignDomainFeature)

@given(instance=avm::cad::AssemblyRoot_strategy)
@settings(max_examples=50)
def test_avm::cad::assemblyroot_instantiation(instance):
    assert isinstance(instance, avm::cad::AssemblyRoot)

@given(instance=ConnectorFeature_strategy)
@settings(max_examples=50)
def test_connectorfeature_instantiation(instance):
    assert isinstance(instance, ConnectorFeature)

@given(instance=avm::cad::KinematicJointSpec_strategy)
@settings(max_examples=50)
def test_avm::cad::kinematicjointspec_instantiation(instance):
    assert isinstance(instance, avm::cad::KinematicJointSpec)

@given(instance=avm::cad::GuideDatum_strategy)
@settings(max_examples=50)
def test_avm::cad::guidedatum_instantiation(instance):
    assert isinstance(instance, avm::cad::GuideDatum)

@given(instance=avm::cad::PlaneReference_strategy)
@settings(max_examples=50)
def test_avm::cad::planereference_instantiation(instance):
    assert isinstance(instance, avm::cad::PlaneReference)

@given(instance=PlaneReference_strategy)
@settings(max_examples=50)
def test_planereference_instantiation(instance):
    assert isinstance(instance, PlaneReference)

@given(instance=avm::cad::TranslationalJointSpec_strategy)
@settings(max_examples=50)
def test_avm::cad::translationaljointspec_instantiation(instance):
    assert isinstance(instance, avm::cad::TranslationalJointSpec)

@given(instance=avm::cad::CustomGeometryInput_strategy)
@settings(max_examples=50)
def test_avm::cad::customgeometryinput_instantiation(instance):
    assert isinstance(instance, avm::cad::CustomGeometryInput)

@given(instance=avm::cad::CustomGeometryInput_strategy)
def test_avm::cad::customgeometryinput_Operation_type(instance):
    assert isinstance(instance.Operation, str)


@given(instance=avm::cad::CustomGeometryInput_strategy)
def test_avm::cad::customgeometryinput_Operation_setter(instance):
    original = instance.Operation
    instance.Operation = original
    assert instance.Operation == original

@given(instance=CustomGeometryInput_strategy)
@settings(max_examples=50)
def test_customgeometryinput_instantiation(instance):
    assert isinstance(instance, CustomGeometryInput)

@given(instance=Geometry3D_strategy)
@settings(max_examples=50)
def test_geometry3d_instantiation(instance):
    assert isinstance(instance, Geometry3D)

@given(instance=avm::cad::Sphere_strategy)
@settings(max_examples=50)
def test_avm::cad::sphere_instantiation(instance):
    assert isinstance(instance, avm::cad::Sphere)

@given(instance=avm::cad::ExtrudedGeometry_strategy)
@settings(max_examples=50)
def test_avm::cad::extrudedgeometry_instantiation(instance):
    assert isinstance(instance, avm::cad::ExtrudedGeometry)

@given(instance=avm::cad::Surface_strategy)
@settings(max_examples=50)
def test_avm::cad::surface_instantiation(instance):
    assert isinstance(instance, avm::cad::Surface)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=avm::cad::PointReference_strategy)
@settings(max_examples=50)
def test_avm::cad::pointreference_instantiation(instance):
    assert isinstance(instance, avm::cad::PointReference)

@given(instance=AnalysisConstruct_strategy)
@settings(max_examples=50)
def test_analysisconstruct_instantiation(instance):
    assert isinstance(instance, AnalysisConstruct)

@given(instance=avm::cad::Geometry_strategy)
@settings(max_examples=50)
def test_avm::cad::geometry_instantiation(instance):
    assert isinstance(instance, avm::cad::Geometry)

@given(instance=avm::cad::Geometry_strategy)
def test_avm::cad::geometry_PartIntersectionModifier_type(instance):
    assert isinstance(instance.PartIntersectionModifier, str)


@given(instance=avm::cad::Geometry_strategy)
def test_avm::cad::geometry_PartIntersectionModifier_setter(instance):
    original = instance.PartIntersectionModifier
    instance.PartIntersectionModifier = original
    assert instance.PartIntersectionModifier == original

@given(instance=avm::cad::Geometry_strategy)
def test_avm::cad::geometry_GeometryQualifier_type(instance):
    assert isinstance(instance.GeometryQualifier, str)


@given(instance=avm::cad::Geometry_strategy)
def test_avm::cad::geometry_GeometryQualifier_setter(instance):
    original = instance.GeometryQualifier
    instance.GeometryQualifier = original
    assert instance.GeometryQualifier == original

@given(instance=Plane_strategy)
@settings(max_examples=50)
def test_plane_instantiation(instance):
    assert isinstance(instance, Plane)

@given(instance=cad::avm::Value_strategy)
@settings(max_examples=50)
def test_cad::avm::value_instantiation(instance):
    assert isinstance(instance, cad::avm::Value)

@given(instance=PointReference_strategy)
@settings(max_examples=50)
def test_pointreference_instantiation(instance):
    assert isinstance(instance, PointReference)

@given(instance=Geometry2D_strategy)
@settings(max_examples=50)
def test_geometry2d_instantiation(instance):
    assert isinstance(instance, Geometry2D)

@given(instance=avm::cad::Polygon_strategy)
@settings(max_examples=50)
def test_avm::cad::polygon_instantiation(instance):
    assert isinstance(instance, avm::cad::Polygon)

@given(instance=avm::cad::Circle_strategy)
@settings(max_examples=50)
def test_avm::cad::circle_instantiation(instance):
    assert isinstance(instance, avm::cad::Circle)

@given(instance=Geometry_strategy)
@settings(max_examples=50)
def test_geometry_instantiation(instance):
    assert isinstance(instance, Geometry)

@given(instance=avm::cad::CustomGeometry_strategy)
@settings(max_examples=50)
def test_avm::cad::customgeometry_instantiation(instance):
    assert isinstance(instance, avm::cad::CustomGeometry)

@given(instance=avm::cad::Geometry3D_strategy)
@settings(max_examples=50)
def test_avm::cad::geometry3d_instantiation(instance):
    assert isinstance(instance, avm::cad::Geometry3D)

@given(instance=avm::cad::Geometry2D_strategy)
@settings(max_examples=50)
def test_avm::cad::geometry2d_instantiation(instance):
    assert isinstance(instance, avm::cad::Geometry2D)

@given(instance=Datum_strategy)
@settings(max_examples=50)
def test_datum_instantiation(instance):
    assert isinstance(instance, Datum)

@given(instance=avm::cad::Plane_strategy)
@settings(max_examples=50)
def test_avm::cad::plane_instantiation(instance):
    assert isinstance(instance, avm::cad::Plane)

@given(instance=avm::cad::Axis_strategy)
@settings(max_examples=50)
def test_avm::cad::axis_instantiation(instance):
    assert isinstance(instance, avm::cad::Axis)

@given(instance=avm::cad::Point_strategy)
@settings(max_examples=50)
def test_avm::cad::point_instantiation(instance):
    assert isinstance(instance, avm::cad::Point)

@given(instance=avm::cad::CoordinateSystem_strategy)
@settings(max_examples=50)
def test_avm::cad::coordinatesystem_instantiation(instance):
    assert isinstance(instance, avm::cad::CoordinateSystem)

@given(instance=avm::cad::CADModel_strategy)
@settings(max_examples=50)
def test_avm::cad::cadmodel_instantiation(instance):
    assert isinstance(instance, avm::cad::CADModel)

@given(instance=Settings_strategy)
@settings(max_examples=50)
def test_settings_instantiation(instance):
    assert isinstance(instance, Settings)

@given(instance=avm::modelica::SolverSettings_strategy)
@settings(max_examples=50)
def test_avm::modelica::solversettings_instantiation(instance):
    assert isinstance(instance, avm::modelica::SolverSettings)

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_Solver_type(instance):
    assert isinstance(instance.Solver, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_Solver_setter(instance):
    original = instance.Solver
    instance.Solver = original
    assert instance.Solver == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_NumberOfIntervals_type(instance):
    assert isinstance(instance.NumberOfIntervals, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_NumberOfIntervals_setter(instance):
    original = instance.NumberOfIntervals
    instance.NumberOfIntervals = original
    assert instance.NumberOfIntervals == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_JobManagerToolSelection_type(instance):
    assert isinstance(instance.JobManagerToolSelection, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_JobManagerToolSelection_setter(instance):
    original = instance.JobManagerToolSelection
    instance.JobManagerToolSelection = original
    assert instance.JobManagerToolSelection == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_IntervalLength_type(instance):
    assert isinstance(instance.IntervalLength, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_IntervalLength_setter(instance):
    original = instance.IntervalLength
    instance.IntervalLength = original
    assert instance.IntervalLength == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_ToolSpecificAnnotations_type(instance):
    assert isinstance(instance.ToolSpecificAnnotations, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_ToolSpecificAnnotations_setter(instance):
    original = instance.ToolSpecificAnnotations
    instance.ToolSpecificAnnotations = original
    assert instance.ToolSpecificAnnotations == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_StartTime_type(instance):
    assert isinstance(instance.StartTime, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_StartTime_setter(instance):
    original = instance.StartTime
    instance.StartTime = original
    assert instance.StartTime == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_Tolerance_type(instance):
    assert isinstance(instance.Tolerance, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_Tolerance_setter(instance):
    original = instance.Tolerance
    instance.Tolerance = original
    assert instance.Tolerance == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_StopTime_type(instance):
    assert isinstance(instance.StopTime, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_StopTime_setter(instance):
    original = instance.StopTime
    instance.StopTime = original
    assert instance.StopTime == original

@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_IntervalMethod_type(instance):
    assert isinstance(instance.IntervalMethod, str)


@given(instance=avm::modelica::SolverSettings_strategy)
def test_avm::modelica::solversettings_IntervalMethod_setter(instance):
    original = instance.IntervalMethod
    instance.IntervalMethod = original
    assert instance.IntervalMethod == original

@given(instance=avm::modelica::Limit_strategy)
@settings(max_examples=50)
def test_avm::modelica::limit_instantiation(instance):
    assert isinstance(instance, avm::modelica::Limit)

@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_BoundType_type(instance):
    assert isinstance(instance.BoundType, str)


@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_BoundType_setter(instance):
    original = instance.BoundType
    instance.BoundType = original
    assert instance.BoundType == original

@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_ToleranceTimeWindow_type(instance):
    assert isinstance(instance.ToleranceTimeWindow, str)


@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_ToleranceTimeWindow_setter(instance):
    original = instance.ToleranceTimeWindow
    instance.ToleranceTimeWindow = original
    assert instance.ToleranceTimeWindow == original

@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_VariableLocator_type(instance):
    assert isinstance(instance.VariableLocator, str)


@given(instance=avm::modelica::Limit_strategy)
def test_avm::modelica::limit_VariableLocator_setter(instance):
    original = instance.VariableLocator
    instance.VariableLocator = original
    assert instance.VariableLocator == original

@given(instance=DomainModelMetric_strategy)
@settings(max_examples=50)
def test_domainmodelmetric_instantiation(instance):
    assert isinstance(instance, DomainModelMetric)

@given(instance=avm::manufacturing::Metric_strategy)
@settings(max_examples=50)
def test_avm::manufacturing::metric_instantiation(instance):
    assert isinstance(instance, avm::manufacturing::Metric)

@given(instance=avm::manufacturing::Metric_strategy)
def test_avm::manufacturing::metric_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::manufacturing::Metric_strategy)
def test_avm::manufacturing::metric_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::cad::Metric_strategy)
@settings(max_examples=50)
def test_avm::cad::metric_instantiation(instance):
    assert isinstance(instance, avm::cad::Metric)

@given(instance=avm::cad::Metric_strategy)
def test_avm::cad::metric_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::cad::Metric_strategy)
def test_avm::cad::metric_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::modelica::Metric_strategy)
@settings(max_examples=50)
def test_avm::modelica::metric_instantiation(instance):
    assert isinstance(instance, avm::modelica::Metric)

@given(instance=avm::modelica::Metric_strategy)
def test_avm::modelica::metric_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::modelica::Metric_strategy)
def test_avm::modelica::metric_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=modelica::avm::Value_strategy)
@settings(max_examples=50)
def test_modelica::avm::value_instantiation(instance):
    assert isinstance(instance, modelica::avm::Value)

@given(instance=DomainModelParameter_strategy)
@settings(max_examples=50)
def test_domainmodelparameter_instantiation(instance):
    assert isinstance(instance, DomainModelParameter)

@given(instance=avm::modelica::Redeclare_strategy)
@settings(max_examples=50)
def test_avm::modelica::redeclare_instantiation(instance):
    assert isinstance(instance, avm::modelica::Redeclare)

@given(instance=avm::modelica::Redeclare_strategy)
def test_avm::modelica::redeclare_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=avm::modelica::Redeclare_strategy)
def test_avm::modelica::redeclare_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm::modelica::Redeclare_strategy)
def test_avm::modelica::redeclare_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::modelica::Redeclare_strategy)
def test_avm::modelica::redeclare_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=avm::adamsCar::Parameter_strategy)
@settings(max_examples=50)
def test_avm::adamscar::parameter_instantiation(instance):
    assert isinstance(instance, avm::adamsCar::Parameter)

@given(instance=avm::adamsCar::Parameter_strategy)
def test_avm::adamscar::parameter_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::adamsCar::Parameter_strategy)
def test_avm::adamscar::parameter_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::adamsCar::Parameter_strategy)
def test_avm::adamscar::parameter_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::adamsCar::Parameter_strategy)
def test_avm::adamscar::parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::manufacturing::Parameter_strategy)
@settings(max_examples=50)
def test_avm::manufacturing::parameter_instantiation(instance):
    assert isinstance(instance, avm::manufacturing::Parameter)

@given(instance=avm::manufacturing::Parameter_strategy)
def test_avm::manufacturing::parameter_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::manufacturing::Parameter_strategy)
def test_avm::manufacturing::parameter_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=avm::manufacturing::Parameter_strategy)
def test_avm::manufacturing::parameter_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::manufacturing::Parameter_strategy)
def test_avm::manufacturing::parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::cad::Parameter_strategy)
@settings(max_examples=50)
def test_avm::cad::parameter_instantiation(instance):
    assert isinstance(instance, avm::cad::Parameter)

@given(instance=avm::cad::Parameter_strategy)
def test_avm::cad::parameter_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::cad::Parameter_strategy)
def test_avm::cad::parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::modelica::Parameter_strategy)
@settings(max_examples=50)
def test_avm::modelica::parameter_instantiation(instance):
    assert isinstance(instance, avm::modelica::Parameter)

@given(instance=avm::modelica::Parameter_strategy)
def test_avm::modelica::parameter_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::modelica::Parameter_strategy)
def test_avm::modelica::parameter_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=DomainModelPort_strategy)
@settings(max_examples=50)
def test_domainmodelport_instantiation(instance):
    assert isinstance(instance, DomainModelPort)

@given(instance=avm::cad::Datum_strategy)
@settings(max_examples=50)
def test_avm::cad::datum_instantiation(instance):
    assert isinstance(instance, avm::cad::Datum)

@given(instance=avm::cad::Datum_strategy)
def test_avm::cad::datum_DatumName_type(instance):
    assert isinstance(instance.DatumName, str)


@given(instance=avm::cad::Datum_strategy)
def test_avm::cad::datum_DatumName_setter(instance):
    original = instance.DatumName
    instance.DatumName = original
    assert instance.DatumName == original

@given(instance=avm::modelica::Connector_strategy)
@settings(max_examples=50)
def test_avm::modelica::connector_instantiation(instance):
    assert isinstance(instance, avm::modelica::Connector)

@given(instance=avm::modelica::Connector_strategy)
def test_avm::modelica::connector_Locator_type(instance):
    assert isinstance(instance.Locator, str)


@given(instance=avm::modelica::Connector_strategy)
def test_avm::modelica::connector_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=avm::modelica::Connector_strategy)
def test_avm::modelica::connector_Class_type(instance):
    assert isinstance(instance.Class, str)


@given(instance=avm::modelica::Connector_strategy)
def test_avm::modelica::connector_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original

@given(instance=Redeclare_strategy)
@settings(max_examples=50)
def test_redeclare_instantiation(instance):
    assert isinstance(instance, Redeclare)

@given(instance=Limit_strategy)
@settings(max_examples=50)
def test_limit_instantiation(instance):
    assert isinstance(instance, Limit)

@given(instance=Metric_strategy)
@settings(max_examples=50)
def test_metric_instantiation(instance):
    assert isinstance(instance, Metric)

@given(instance=ValueNode_strategy)
@settings(max_examples=50)
def test_valuenode_instantiation(instance):
    assert isinstance(instance, ValueNode)

@given(instance=avm::ValueFlowMux_strategy)
@settings(max_examples=50)
def test_avm::valueflowmux_instantiation(instance):
    assert isinstance(instance, avm::ValueFlowMux)

@given(instance=avm::Value_strategy)
@settings(max_examples=50)
def test_avm::value_instantiation(instance):
    assert isinstance(instance, avm::Value)

@given(instance=avm::Value_strategy)
def test_avm::value_DataType_type(instance):
    assert isinstance(instance.DataType, str)


@given(instance=avm::Value_strategy)
def test_avm::value_DataType_setter(instance):
    original = instance.DataType
    instance.DataType = original
    assert instance.DataType == original

@given(instance=avm::Value_strategy)
def test_avm::value_DimensionType_type(instance):
    assert isinstance(instance.DimensionType, str)


@given(instance=avm::Value_strategy)
def test_avm::value_DimensionType_setter(instance):
    original = instance.DimensionType
    instance.DimensionType = original
    assert instance.DimensionType == original

@given(instance=avm::Value_strategy)
def test_avm::value_Unit_type(instance):
    assert isinstance(instance.Unit, str)


@given(instance=avm::Value_strategy)
def test_avm::value_Unit_setter(instance):
    original = instance.Unit
    instance.Unit = original
    assert instance.Unit == original

@given(instance=avm::Value_strategy)
def test_avm::value_Dimensions_type(instance):
    assert isinstance(instance.Dimensions, str)


@given(instance=avm::Value_strategy)
def test_avm::value_Dimensions_setter(instance):
    original = instance.Dimensions
    instance.Dimensions = original
    assert instance.Dimensions == original

@given(instance=avm::AnalysisConstruct_strategy)
@settings(max_examples=50)
def test_avm::analysisconstruct_instantiation(instance):
    assert isinstance(instance, avm::AnalysisConstruct)

@given(instance=avm::Port_strategy)
@settings(max_examples=50)
def test_avm::port_instantiation(instance):
    assert isinstance(instance, avm::Port)

@given(instance=avm::Port_strategy)
def test_avm::port_Definition_type(instance):
    assert isinstance(instance.Definition, str)


@given(instance=avm::Port_strategy)
def test_avm::port_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original

@given(instance=avm::Port_strategy)
def test_avm::port_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::Port_strategy)
def test_avm::port_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::Port_strategy)
def test_avm::port_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Port_strategy)
def test_avm::port_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Port_strategy)
def test_avm::port_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Port_strategy)
def test_avm::port_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Port_strategy)
def test_avm::port_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Port_strategy)
def test_avm::port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::DistributionRestriction_strategy)
@settings(max_examples=50)
def test_avm::distributionrestriction_instantiation(instance):
    assert isinstance(instance, avm::DistributionRestriction)

@given(instance=avm::DistributionRestriction_strategy)
def test_avm::distributionrestriction_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::DistributionRestriction_strategy)
def test_avm::distributionrestriction_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::Connector_strategy)
@settings(max_examples=50)
def test_avm::connector_instantiation(instance):
    assert isinstance(instance, avm::Connector)

@given(instance=avm::Connector_strategy)
def test_avm::connector_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Connector_strategy)
def test_avm::connector_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Connector_strategy)
def test_avm::connector_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Connector_strategy)
def test_avm::connector_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Connector_strategy)
def test_avm::connector_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::Connector_strategy)
def test_avm::connector_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::Connector_strategy)
def test_avm::connector_Definition_type(instance):
    assert isinstance(instance.Definition, str)


@given(instance=avm::Connector_strategy)
def test_avm::connector_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original

@given(instance=avm::Connector_strategy)
def test_avm::connector_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Connector_strategy)
def test_avm::connector_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Resource_strategy)
@settings(max_examples=50)
def test_avm::resource_instantiation(instance):
    assert isinstance(instance, avm::Resource)

@given(instance=avm::Resource_strategy)
def test_avm::resource_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_Path_type(instance):
    assert isinstance(instance.Path, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_Path_setter(instance):
    original = instance.Path
    instance.Path = original
    assert instance.Path == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::Resource_strategy)
def test_avm::resource_Hash_type(instance):
    assert isinstance(instance.Hash, str)


@given(instance=avm::Resource_strategy)
def test_avm::resource_Hash_setter(instance):
    original = instance.Hash
    instance.Hash = original
    assert instance.Hash == original

@given(instance=avm::Property_strategy)
@settings(max_examples=50)
def test_avm::property_instantiation(instance):
    assert isinstance(instance, avm::Property)

@given(instance=avm::Property_strategy)
def test_avm::property_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::Property_strategy)
def test_avm::property_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::Property_strategy)
def test_avm::property_Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::Property_strategy)
def test_avm::property_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::Property_strategy)
def test_avm::property_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Property_strategy)
def test_avm::property_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Property_strategy)
def test_avm::property_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Property_strategy)
def test_avm::property_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Property_strategy)
def test_avm::property_Definition_type(instance):
    assert isinstance(instance.Definition, str)


@given(instance=avm::Property_strategy)
def test_avm::property_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original

@given(instance=avm::Property_strategy)
def test_avm::property_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Property_strategy)
def test_avm::property_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Property_strategy)
def test_avm::property_OnDataSheet_type(instance):
    assert isinstance(instance.OnDataSheet, str)


@given(instance=avm::Property_strategy)
def test_avm::property_OnDataSheet_setter(instance):
    original = instance.OnDataSheet
    instance.OnDataSheet = original
    assert instance.OnDataSheet == original

@given(instance=avm::Formula_strategy)
@settings(max_examples=50)
def test_avm::formula_instantiation(instance):
    assert isinstance(instance, avm::Formula)

@given(instance=avm::Formula_strategy)
def test_avm::formula_YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::Formula_strategy)
def test_avm::formula_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::Formula_strategy)
def test_avm::formula_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Formula_strategy)
def test_avm::formula_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::Formula_strategy)
def test_avm::formula_XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::Formula_strategy)
def test_avm::formula_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::DomainModel__strategy)
@settings(max_examples=50)
def test_avm::domainmodel__instantiation(instance):
    assert isinstance(instance, avm::DomainModel_)

@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Author_type(instance):
    assert isinstance(instance.Author, str)


@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original

@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__YPosition_type(instance):
    assert isinstance(instance.YPosition, str)


@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Notes_type(instance):
    assert isinstance(instance.Notes, str)


@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__XPosition_type(instance):
    assert isinstance(instance.XPosition, str)


@given(instance=avm::DomainModel__strategy)
def test_avm::domainmodel__XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm::Component_strategy)
@settings(max_examples=50)
def test_avm::component_instantiation(instance):
    assert isinstance(instance, avm::Component)

@given(instance=avm::Component_strategy)
def test_avm::component_SchemaVersion_type(instance):
    assert isinstance(instance.SchemaVersion, str)


@given(instance=avm::Component_strategy)
def test_avm::component_SchemaVersion_setter(instance):
    original = instance.SchemaVersion
    instance.SchemaVersion = original
    assert instance.SchemaVersion == original

@given(instance=avm::Component_strategy)
def test_avm::component_Supercedes_type(instance):
    assert isinstance(instance.Supercedes, str)


@given(instance=avm::Component_strategy)
def test_avm::component_Supercedes_setter(instance):
    original = instance.Supercedes
    instance.Supercedes = original
    assert instance.Supercedes == original

@given(instance=avm::Component_strategy)
def test_avm::component_Classifications_type(instance):
    assert isinstance(instance.Classifications, str)


@given(instance=avm::Component_strategy)
def test_avm::component_Classifications_setter(instance):
    original = instance.Classifications
    instance.Classifications = original
    assert instance.Classifications == original

@given(instance=avm::Component_strategy)
def test_avm::component_Version_type(instance):
    assert isinstance(instance.Version, str)


@given(instance=avm::Component_strategy)
def test_avm::component_Version_setter(instance):
    original = instance.Version
    instance.Version = original
    assert instance.Version == original

@given(instance=avm::Component_strategy)
def test_avm::component_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=avm::Component_strategy)
def test_avm::component_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm::Component_strategy)
def test_avm::component_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=avm::Component_strategy)
def test_avm::component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
