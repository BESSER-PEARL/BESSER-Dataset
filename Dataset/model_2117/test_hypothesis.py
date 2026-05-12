import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    manufacturing_avm_Value,
    avm_adamsCar_FileReference,
    adamsCar_avm_Value,
    FileReference,
    Axis,
    KinematicJointSpec,
    avm_cad_RevoluteJointSpec,
    cad_avm_ComponentInstance,
    DesignDomainFeature,
    avm_cad_AssemblyRoot,
    ConnectorFeature,
    avm_cad_KinematicJointSpec,
    avm_cad_GuideDatum,
    avm_cad_PlaneReference,
    PlaneReference,
    avm_cad_TranslationalJointSpec,
    avm_cad_CustomGeometryInput,
    CustomGeometryInput,
    Geometry3D,
    avm_cad_Sphere,
    avm_cad_ExtrudedGeometry,
    avm_cad_Surface,
    Point,
    avm_cad_PointReference,
    AnalysisConstruct,
    avm_cad_Geometry,
    Plane,
    cad_avm_Value,
    PointReference,
    Geometry2D,
    avm_cad_Polygon,
    avm_cad_Circle,
    Geometry,
    avm_cad_Geometry3D,
    avm_cad_CustomGeometry,
    avm_cad_Geometry2D,
    Datum,
    avm_cad_CoordinateSystem,
    avm_cad_Point,
    avm_cad_Axis,
    avm_cad_Plane,
    Settings,
    avm_modelica_SolverSettings,
    avm_modelica_Limit,
    DomainModelMetric,
    avm_manufacturing_Metric,
    avm_cad_Metric,
    avm_modelica_Metric,
    modelica_avm_Value,
    DomainModelParameter,
    avm_modelica_Redeclare,
    avm_adamsCar_Parameter,
    avm_manufacturing_Parameter,
    avm_cad_Parameter,
    avm_modelica_Parameter,
    DomainModelPort,
    avm_cad_Datum,
    avm_modelica_Connector,
    Redeclare,
    Limit,
    Metric,
    Connector,
    Parameter,
    DomainModel_,
    avm_cyber_CyberModel,
    avm_manufacturing_ManufacturingModel,
    avm_adamsCar_AdamsCarModel,
    avm_cad_CADModel,
    avm_modelica_ModelicaModel,
    avm_WorkflowTaskBase,
    avm_TestBenchValueBase,
    avm_ContainerInstanceBase,
    TestBenchValueBase,
    ContainerInstanceBase,
    avm_Settings,
    avm_Workflow,
    WorkflowTaskBase,
    avm_ExecutionTask,
    avm_InterpreterTask,
    avm_TopLevelSystemUnderTest,
    avm_TestBench,
    avm_Operand,
    Formula,
    avm_ComplexFormula,
    avm_SimpleFormula,
    avm_TestInjectionPoint,
    avm_Metric,
    avm_Parameter,
    avm_PortMapTarget,
    avm_ComponentPrimitivePropertyInstance,
    DesignSpaceContainer,
    avm_Alternative,
    avm_Optional,
    Container,
    avm_DesignSpaceContainer,
    avm_Compound,
    avm_ConnectorCompositionTarget,
    avm_DesignDomainFeature,
    avm_Container,
    avm_Design,
    avm_ComponentInstance,
    avm_DomainModelMetric,
    DistributionRestriction,
    avm_ITAR,
    avm_DoDDistributionStatement,
    avm_Proprietary,
    avm_SecurityClassification,
    ProbabilisticValue,
    avm_NormalDistribution,
    Property,
    avm_CompoundProperty,
    avm_PrimitiveProperty,
    avm_UniformDistribution,
    avm_DomainModelParameter,
    Port,
    avm_AbstractPort,
    avm_DomainModelPort,
    PortMapTarget,
    avm_ComponentPortInstance,
    avm_ConnectorFeature,
    avm_assemblyDetail,
    ConnectorCompositionTarget,
    avm_ComponentConnectorInstance,
    avm_ValueNode,
    ValueExpressionType,
    avm_DerivedValue,
    avm_ParametricValue,
    avm_CalculatedValue,
    avm_ParametricEnumeratedValue,
    avm_ProbabilisticValue,
    avm_FixedValue,
    avm_DataSource,
    avm_ValueExpressionType,
    ValueNode,
    avm_ValueFlowMux,
    avm_Value,
    avm_AnalysisConstruct,
    avm_Port,
    avm_DistributionRestriction,
    avm_Connector,
    avm_Resource,
    avm_Property,
    avm_Formula,
    avm_DomainModel_,
    avm_Component,
    BoundTypeEnum,
    CalculationTypeEnum,
    SimpleFormulaOperation,
    DimensionTypeEnum,
    DoDDistributionStatementEnum,
    GeometryQualifierEnum,
    PartIntersectionEnum,
    IntervalMethod,
    RedeclareTypeEnum,
    ModelType,
    DataTypeEnum,
    JobManagerToolSelection,
    CustomGeometryInputOperationEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_manufacturing_avm_value_is_not_abstract():
    assert not inspect.isabstract(manufacturing_avm_Value)


def test_manufacturing_avm_value_constructor_exists():
    assert callable(manufacturing_avm_Value.__init__)


def test_manufacturing_avm_value_constructor_args():
    sig = inspect.signature(manufacturing_avm_Value.__init__)
    params = list(sig.parameters.keys())



def test_avm_adamscar_filereference_is_not_abstract():
    assert not inspect.isabstract(avm_adamsCar_FileReference)


def test_avm_adamscar_filereference_constructor_exists():
    assert callable(avm_adamsCar_FileReference.__init__)


def test_avm_adamscar_filereference_constructor_args():
    sig = inspect.signature(avm_adamsCar_FileReference.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "FilePath" in params, "Missing parameter 'FilePath'"

def test_avm_adamscar_filereference_has_Name():
    assert hasattr(avm_adamsCar_FileReference, "Name")
    descriptor = None
    for klass in avm_adamsCar_FileReference.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_adamscar_filereference_has_ID():
    assert hasattr(avm_adamsCar_FileReference, "ID")
    descriptor = None
    for klass in avm_adamsCar_FileReference.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_adamscar_filereference_has_FilePath():
    assert hasattr(avm_adamsCar_FileReference, "FilePath")
    descriptor = None
    for klass in avm_adamsCar_FileReference.__mro__:
        if "FilePath" in klass.__dict__:
            descriptor = klass.__dict__["FilePath"]
            break
    assert isinstance(descriptor, property)



def test_adamscar_avm_value_is_not_abstract():
    assert not inspect.isabstract(adamsCar_avm_Value)


def test_adamscar_avm_value_constructor_exists():
    assert callable(adamsCar_avm_Value.__init__)


def test_adamscar_avm_value_constructor_args():
    sig = inspect.signature(adamsCar_avm_Value.__init__)
    params = list(sig.parameters.keys())



def test_filereference_is_not_abstract():
    assert not inspect.isabstract(FileReference)


def test_filereference_constructor_exists():
    assert callable(FileReference.__init__)


def test_filereference_constructor_args():
    sig = inspect.signature(FileReference.__init__)
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



def test_avm_cad_revolutejointspec_is_not_abstract():
    assert not inspect.isabstract(avm_cad_RevoluteJointSpec)


def test_avm_cad_revolutejointspec_constructor_exists():
    assert callable(avm_cad_RevoluteJointSpec.__init__)


def test_avm_cad_revolutejointspec_constructor_args():
    sig = inspect.signature(avm_cad_RevoluteJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_cad_avm_componentinstance_is_not_abstract():
    assert not inspect.isabstract(cad_avm_ComponentInstance)


def test_cad_avm_componentinstance_constructor_exists():
    assert callable(cad_avm_ComponentInstance.__init__)


def test_cad_avm_componentinstance_constructor_args():
    sig = inspect.signature(cad_avm_ComponentInstance.__init__)
    params = list(sig.parameters.keys())



def test_designdomainfeature_is_not_abstract():
    assert not inspect.isabstract(DesignDomainFeature)


def test_designdomainfeature_constructor_exists():
    assert callable(DesignDomainFeature.__init__)


def test_designdomainfeature_constructor_args():
    sig = inspect.signature(DesignDomainFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_assemblyroot_is_not_abstract():
    assert not inspect.isabstract(avm_cad_AssemblyRoot)


def test_avm_cad_assemblyroot_constructor_exists():
    assert callable(avm_cad_AssemblyRoot.__init__)


def test_avm_cad_assemblyroot_constructor_args():
    sig = inspect.signature(avm_cad_AssemblyRoot.__init__)
    params = list(sig.parameters.keys())



def test_connectorfeature_is_not_abstract():
    assert not inspect.isabstract(ConnectorFeature)


def test_connectorfeature_constructor_exists():
    assert callable(ConnectorFeature.__init__)


def test_connectorfeature_constructor_args():
    sig = inspect.signature(ConnectorFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_kinematicjointspec_is_not_abstract():
    assert not inspect.isabstract(avm_cad_KinematicJointSpec)


def test_avm_cad_kinematicjointspec_constructor_exists():
    assert callable(avm_cad_KinematicJointSpec.__init__)


def test_avm_cad_kinematicjointspec_constructor_args():
    sig = inspect.signature(avm_cad_KinematicJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_guidedatum_is_not_abstract():
    assert not inspect.isabstract(avm_cad_GuideDatum)


def test_avm_cad_guidedatum_constructor_exists():
    assert callable(avm_cad_GuideDatum.__init__)


def test_avm_cad_guidedatum_constructor_args():
    sig = inspect.signature(avm_cad_GuideDatum.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_planereference_is_not_abstract():
    assert not inspect.isabstract(avm_cad_PlaneReference)


def test_avm_cad_planereference_constructor_exists():
    assert callable(avm_cad_PlaneReference.__init__)


def test_avm_cad_planereference_constructor_args():
    sig = inspect.signature(avm_cad_PlaneReference.__init__)
    params = list(sig.parameters.keys())



def test_planereference_is_not_abstract():
    assert not inspect.isabstract(PlaneReference)


def test_planereference_constructor_exists():
    assert callable(PlaneReference.__init__)


def test_planereference_constructor_args():
    sig = inspect.signature(PlaneReference.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_translationaljointspec_is_not_abstract():
    assert not inspect.isabstract(avm_cad_TranslationalJointSpec)


def test_avm_cad_translationaljointspec_constructor_exists():
    assert callable(avm_cad_TranslationalJointSpec.__init__)


def test_avm_cad_translationaljointspec_constructor_args():
    sig = inspect.signature(avm_cad_TranslationalJointSpec.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_customgeometryinput_is_not_abstract():
    assert not inspect.isabstract(avm_cad_CustomGeometryInput)


def test_avm_cad_customgeometryinput_constructor_exists():
    assert callable(avm_cad_CustomGeometryInput.__init__)


def test_avm_cad_customgeometryinput_constructor_args():
    sig = inspect.signature(avm_cad_CustomGeometryInput.__init__)
    params = list(sig.parameters.keys())
    assert "Operation" in params, "Missing parameter 'Operation'"

def test_avm_cad_customgeometryinput_has_Operation():
    assert hasattr(avm_cad_CustomGeometryInput, "Operation")
    descriptor = None
    for klass in avm_cad_CustomGeometryInput.__mro__:
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



def test_avm_cad_sphere_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Sphere)


def test_avm_cad_sphere_constructor_exists():
    assert callable(avm_cad_Sphere.__init__)


def test_avm_cad_sphere_constructor_args():
    sig = inspect.signature(avm_cad_Sphere.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_extrudedgeometry_is_not_abstract():
    assert not inspect.isabstract(avm_cad_ExtrudedGeometry)


def test_avm_cad_extrudedgeometry_constructor_exists():
    assert callable(avm_cad_ExtrudedGeometry.__init__)


def test_avm_cad_extrudedgeometry_constructor_args():
    sig = inspect.signature(avm_cad_ExtrudedGeometry.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_surface_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Surface)


def test_avm_cad_surface_constructor_exists():
    assert callable(avm_cad_Surface.__init__)


def test_avm_cad_surface_constructor_args():
    sig = inspect.signature(avm_cad_Surface.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_pointreference_is_not_abstract():
    assert not inspect.isabstract(avm_cad_PointReference)


def test_avm_cad_pointreference_constructor_exists():
    assert callable(avm_cad_PointReference.__init__)


def test_avm_cad_pointreference_constructor_args():
    sig = inspect.signature(avm_cad_PointReference.__init__)
    params = list(sig.parameters.keys())



def test_analysisconstruct_is_not_abstract():
    assert not inspect.isabstract(AnalysisConstruct)


def test_analysisconstruct_constructor_exists():
    assert callable(AnalysisConstruct.__init__)


def test_analysisconstruct_constructor_args():
    sig = inspect.signature(AnalysisConstruct.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_geometry_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Geometry)


def test_avm_cad_geometry_constructor_exists():
    assert callable(avm_cad_Geometry.__init__)


def test_avm_cad_geometry_constructor_args():
    sig = inspect.signature(avm_cad_Geometry.__init__)
    params = list(sig.parameters.keys())
    assert "GeometryQualifier" in params, "Missing parameter 'GeometryQualifier'"
    assert "PartIntersectionModifier" in params, "Missing parameter 'PartIntersectionModifier'"

def test_avm_cad_geometry_has_GeometryQualifier():
    assert hasattr(avm_cad_Geometry, "GeometryQualifier")
    descriptor = None
    for klass in avm_cad_Geometry.__mro__:
        if "GeometryQualifier" in klass.__dict__:
            descriptor = klass.__dict__["GeometryQualifier"]
            break
    assert isinstance(descriptor, property)

def test_avm_cad_geometry_has_PartIntersectionModifier():
    assert hasattr(avm_cad_Geometry, "PartIntersectionModifier")
    descriptor = None
    for klass in avm_cad_Geometry.__mro__:
        if "PartIntersectionModifier" in klass.__dict__:
            descriptor = klass.__dict__["PartIntersectionModifier"]
            break
    assert isinstance(descriptor, property)



def test_plane_is_not_abstract():
    assert not inspect.isabstract(Plane)


def test_plane_constructor_exists():
    assert callable(Plane.__init__)


def test_plane_constructor_args():
    sig = inspect.signature(Plane.__init__)
    params = list(sig.parameters.keys())



def test_cad_avm_value_is_not_abstract():
    assert not inspect.isabstract(cad_avm_Value)


def test_cad_avm_value_constructor_exists():
    assert callable(cad_avm_Value.__init__)


def test_cad_avm_value_constructor_args():
    sig = inspect.signature(cad_avm_Value.__init__)
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



def test_avm_cad_polygon_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Polygon)


def test_avm_cad_polygon_constructor_exists():
    assert callable(avm_cad_Polygon.__init__)


def test_avm_cad_polygon_constructor_args():
    sig = inspect.signature(avm_cad_Polygon.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_circle_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Circle)


def test_avm_cad_circle_constructor_exists():
    assert callable(avm_cad_Circle.__init__)


def test_avm_cad_circle_constructor_args():
    sig = inspect.signature(avm_cad_Circle.__init__)
    params = list(sig.parameters.keys())



def test_geometry_is_not_abstract():
    assert not inspect.isabstract(Geometry)


def test_geometry_constructor_exists():
    assert callable(Geometry.__init__)


def test_geometry_constructor_args():
    sig = inspect.signature(Geometry.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_geometry3d_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Geometry3D)


def test_avm_cad_geometry3d_constructor_exists():
    assert callable(avm_cad_Geometry3D.__init__)


def test_avm_cad_geometry3d_constructor_args():
    sig = inspect.signature(avm_cad_Geometry3D.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_customgeometry_is_not_abstract():
    assert not inspect.isabstract(avm_cad_CustomGeometry)


def test_avm_cad_customgeometry_constructor_exists():
    assert callable(avm_cad_CustomGeometry.__init__)


def test_avm_cad_customgeometry_constructor_args():
    sig = inspect.signature(avm_cad_CustomGeometry.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_geometry2d_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Geometry2D)


def test_avm_cad_geometry2d_constructor_exists():
    assert callable(avm_cad_Geometry2D.__init__)


def test_avm_cad_geometry2d_constructor_args():
    sig = inspect.signature(avm_cad_Geometry2D.__init__)
    params = list(sig.parameters.keys())



def test_datum_is_not_abstract():
    assert not inspect.isabstract(Datum)


def test_datum_constructor_exists():
    assert callable(Datum.__init__)


def test_datum_constructor_args():
    sig = inspect.signature(Datum.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_coordinatesystem_is_not_abstract():
    assert not inspect.isabstract(avm_cad_CoordinateSystem)


def test_avm_cad_coordinatesystem_constructor_exists():
    assert callable(avm_cad_CoordinateSystem.__init__)


def test_avm_cad_coordinatesystem_constructor_args():
    sig = inspect.signature(avm_cad_CoordinateSystem.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_point_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Point)


def test_avm_cad_point_constructor_exists():
    assert callable(avm_cad_Point.__init__)


def test_avm_cad_point_constructor_args():
    sig = inspect.signature(avm_cad_Point.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_axis_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Axis)


def test_avm_cad_axis_constructor_exists():
    assert callable(avm_cad_Axis.__init__)


def test_avm_cad_axis_constructor_args():
    sig = inspect.signature(avm_cad_Axis.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_plane_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Plane)


def test_avm_cad_plane_constructor_exists():
    assert callable(avm_cad_Plane.__init__)


def test_avm_cad_plane_constructor_args():
    sig = inspect.signature(avm_cad_Plane.__init__)
    params = list(sig.parameters.keys())



def test_settings_is_not_abstract():
    assert not inspect.isabstract(Settings)


def test_settings_constructor_exists():
    assert callable(Settings.__init__)


def test_settings_constructor_args():
    sig = inspect.signature(Settings.__init__)
    params = list(sig.parameters.keys())



def test_avm_modelica_solversettings_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_SolverSettings)


def test_avm_modelica_solversettings_constructor_exists():
    assert callable(avm_modelica_SolverSettings.__init__)


def test_avm_modelica_solversettings_constructor_args():
    sig = inspect.signature(avm_modelica_SolverSettings.__init__)
    params = list(sig.parameters.keys())
    assert "JobManagerToolSelection" in params, "Missing parameter 'JobManagerToolSelection'"
    assert "NumberOfIntervals" in params, "Missing parameter 'NumberOfIntervals'"
    assert "ToolSpecificAnnotations" in params, "Missing parameter 'ToolSpecificAnnotations'"
    assert "StartTime" in params, "Missing parameter 'StartTime'"
    assert "IntervalLength" in params, "Missing parameter 'IntervalLength'"
    assert "Solver" in params, "Missing parameter 'Solver'"
    assert "IntervalMethod" in params, "Missing parameter 'IntervalMethod'"
    assert "Tolerance" in params, "Missing parameter 'Tolerance'"
    assert "StopTime" in params, "Missing parameter 'StopTime'"

def test_avm_modelica_solversettings_has_JobManagerToolSelection():
    assert hasattr(avm_modelica_SolverSettings, "JobManagerToolSelection")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "JobManagerToolSelection" in klass.__dict__:
            descriptor = klass.__dict__["JobManagerToolSelection"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_NumberOfIntervals():
    assert hasattr(avm_modelica_SolverSettings, "NumberOfIntervals")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "NumberOfIntervals" in klass.__dict__:
            descriptor = klass.__dict__["NumberOfIntervals"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_ToolSpecificAnnotations():
    assert hasattr(avm_modelica_SolverSettings, "ToolSpecificAnnotations")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "ToolSpecificAnnotations" in klass.__dict__:
            descriptor = klass.__dict__["ToolSpecificAnnotations"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_StartTime():
    assert hasattr(avm_modelica_SolverSettings, "StartTime")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "StartTime" in klass.__dict__:
            descriptor = klass.__dict__["StartTime"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_IntervalLength():
    assert hasattr(avm_modelica_SolverSettings, "IntervalLength")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "IntervalLength" in klass.__dict__:
            descriptor = klass.__dict__["IntervalLength"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_Solver():
    assert hasattr(avm_modelica_SolverSettings, "Solver")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "Solver" in klass.__dict__:
            descriptor = klass.__dict__["Solver"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_IntervalMethod():
    assert hasattr(avm_modelica_SolverSettings, "IntervalMethod")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "IntervalMethod" in klass.__dict__:
            descriptor = klass.__dict__["IntervalMethod"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_Tolerance():
    assert hasattr(avm_modelica_SolverSettings, "Tolerance")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "Tolerance" in klass.__dict__:
            descriptor = klass.__dict__["Tolerance"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_solversettings_has_StopTime():
    assert hasattr(avm_modelica_SolverSettings, "StopTime")
    descriptor = None
    for klass in avm_modelica_SolverSettings.__mro__:
        if "StopTime" in klass.__dict__:
            descriptor = klass.__dict__["StopTime"]
            break
    assert isinstance(descriptor, property)



def test_avm_modelica_limit_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_Limit)


def test_avm_modelica_limit_constructor_exists():
    assert callable(avm_modelica_Limit.__init__)


def test_avm_modelica_limit_constructor_args():
    sig = inspect.signature(avm_modelica_Limit.__init__)
    params = list(sig.parameters.keys())
    assert "BoundType" in params, "Missing parameter 'BoundType'"
    assert "VariableLocator" in params, "Missing parameter 'VariableLocator'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ToleranceTimeWindow" in params, "Missing parameter 'ToleranceTimeWindow'"
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm_modelica_limit_has_BoundType():
    assert hasattr(avm_modelica_Limit, "BoundType")
    descriptor = None
    for klass in avm_modelica_Limit.__mro__:
        if "BoundType" in klass.__dict__:
            descriptor = klass.__dict__["BoundType"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_limit_has_VariableLocator():
    assert hasattr(avm_modelica_Limit, "VariableLocator")
    descriptor = None
    for klass in avm_modelica_Limit.__mro__:
        if "VariableLocator" in klass.__dict__:
            descriptor = klass.__dict__["VariableLocator"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_limit_has_Name():
    assert hasattr(avm_modelica_Limit, "Name")
    descriptor = None
    for klass in avm_modelica_Limit.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_limit_has_ToleranceTimeWindow():
    assert hasattr(avm_modelica_Limit, "ToleranceTimeWindow")
    descriptor = None
    for klass in avm_modelica_Limit.__mro__:
        if "ToleranceTimeWindow" in klass.__dict__:
            descriptor = klass.__dict__["ToleranceTimeWindow"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_limit_has_Notes():
    assert hasattr(avm_modelica_Limit, "Notes")
    descriptor = None
    for klass in avm_modelica_Limit.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_domainmodelmetric_is_not_abstract():
    assert not inspect.isabstract(DomainModelMetric)


def test_domainmodelmetric_constructor_exists():
    assert callable(DomainModelMetric.__init__)


def test_domainmodelmetric_constructor_args():
    sig = inspect.signature(DomainModelMetric.__init__)
    params = list(sig.parameters.keys())



def test_avm_manufacturing_metric_is_not_abstract():
    assert not inspect.isabstract(avm_manufacturing_Metric)


def test_avm_manufacturing_metric_constructor_exists():
    assert callable(avm_manufacturing_Metric.__init__)


def test_avm_manufacturing_metric_constructor_args():
    sig = inspect.signature(avm_manufacturing_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_manufacturing_metric_has_Name():
    assert hasattr(avm_manufacturing_Metric, "Name")
    descriptor = None
    for klass in avm_manufacturing_Metric.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_cad_metric_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Metric)


def test_avm_cad_metric_constructor_exists():
    assert callable(avm_cad_Metric.__init__)


def test_avm_cad_metric_constructor_args():
    sig = inspect.signature(avm_cad_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_cad_metric_has_Name():
    assert hasattr(avm_cad_Metric, "Name")
    descriptor = None
    for klass in avm_cad_Metric.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_modelica_metric_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_Metric)


def test_avm_modelica_metric_constructor_exists():
    assert callable(avm_modelica_Metric.__init__)


def test_avm_modelica_metric_constructor_args():
    sig = inspect.signature(avm_modelica_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm_modelica_metric_has_Locator():
    assert hasattr(avm_modelica_Metric, "Locator")
    descriptor = None
    for klass in avm_modelica_Metric.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)



def test_modelica_avm_value_is_not_abstract():
    assert not inspect.isabstract(modelica_avm_Value)


def test_modelica_avm_value_constructor_exists():
    assert callable(modelica_avm_Value.__init__)


def test_modelica_avm_value_constructor_args():
    sig = inspect.signature(modelica_avm_Value.__init__)
    params = list(sig.parameters.keys())



def test_domainmodelparameter_is_not_abstract():
    assert not inspect.isabstract(DomainModelParameter)


def test_domainmodelparameter_constructor_exists():
    assert callable(DomainModelParameter.__init__)


def test_domainmodelparameter_constructor_args():
    sig = inspect.signature(DomainModelParameter.__init__)
    params = list(sig.parameters.keys())



def test_avm_modelica_redeclare_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_Redeclare)


def test_avm_modelica_redeclare_constructor_exists():
    assert callable(avm_modelica_Redeclare.__init__)


def test_avm_modelica_redeclare_constructor_args():
    sig = inspect.signature(avm_modelica_Redeclare.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm_modelica_redeclare_has_Type():
    assert hasattr(avm_modelica_Redeclare, "Type")
    descriptor = None
    for klass in avm_modelica_Redeclare.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_redeclare_has_Locator():
    assert hasattr(avm_modelica_Redeclare, "Locator")
    descriptor = None
    for klass in avm_modelica_Redeclare.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)



def test_avm_adamscar_parameter_is_not_abstract():
    assert not inspect.isabstract(avm_adamsCar_Parameter)


def test_avm_adamscar_parameter_constructor_exists():
    assert callable(avm_adamsCar_Parameter.__init__)


def test_avm_adamscar_parameter_constructor_args():
    sig = inspect.signature(avm_adamsCar_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm_adamscar_parameter_has_Name():
    assert hasattr(avm_adamsCar_Parameter, "Name")
    descriptor = None
    for klass in avm_adamsCar_Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_adamscar_parameter_has_ID():
    assert hasattr(avm_adamsCar_Parameter, "ID")
    descriptor = None
    for klass in avm_adamsCar_Parameter.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm_manufacturing_parameter_is_not_abstract():
    assert not inspect.isabstract(avm_manufacturing_Parameter)


def test_avm_manufacturing_parameter_constructor_exists():
    assert callable(avm_manufacturing_Parameter.__init__)


def test_avm_manufacturing_parameter_constructor_args():
    sig = inspect.signature(avm_manufacturing_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_manufacturing_parameter_has_Locator():
    assert hasattr(avm_manufacturing_Parameter, "Locator")
    descriptor = None
    for klass in avm_manufacturing_Parameter.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)

def test_avm_manufacturing_parameter_has_Name():
    assert hasattr(avm_manufacturing_Parameter, "Name")
    descriptor = None
    for klass in avm_manufacturing_Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_cad_parameter_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Parameter)


def test_avm_cad_parameter_constructor_exists():
    assert callable(avm_cad_Parameter.__init__)


def test_avm_cad_parameter_constructor_args():
    sig = inspect.signature(avm_cad_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_cad_parameter_has_Name():
    assert hasattr(avm_cad_Parameter, "Name")
    descriptor = None
    for klass in avm_cad_Parameter.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_modelica_parameter_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_Parameter)


def test_avm_modelica_parameter_constructor_exists():
    assert callable(avm_modelica_Parameter.__init__)


def test_avm_modelica_parameter_constructor_args():
    sig = inspect.signature(avm_modelica_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm_modelica_parameter_has_Locator():
    assert hasattr(avm_modelica_Parameter, "Locator")
    descriptor = None
    for klass in avm_modelica_Parameter.__mro__:
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



def test_avm_cad_datum_is_not_abstract():
    assert not inspect.isabstract(avm_cad_Datum)


def test_avm_cad_datum_constructor_exists():
    assert callable(avm_cad_Datum.__init__)


def test_avm_cad_datum_constructor_args():
    sig = inspect.signature(avm_cad_Datum.__init__)
    params = list(sig.parameters.keys())
    assert "DatumName" in params, "Missing parameter 'DatumName'"

def test_avm_cad_datum_has_DatumName():
    assert hasattr(avm_cad_Datum, "DatumName")
    descriptor = None
    for klass in avm_cad_Datum.__mro__:
        if "DatumName" in klass.__dict__:
            descriptor = klass.__dict__["DatumName"]
            break
    assert isinstance(descriptor, property)



def test_avm_modelica_connector_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_Connector)


def test_avm_modelica_connector_constructor_exists():
    assert callable(avm_modelica_Connector.__init__)


def test_avm_modelica_connector_constructor_args():
    sig = inspect.signature(avm_modelica_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "Class" in params, "Missing parameter 'Class'"
    assert "Locator" in params, "Missing parameter 'Locator'"

def test_avm_modelica_connector_has_Class():
    assert hasattr(avm_modelica_Connector, "Class")
    descriptor = None
    for klass in avm_modelica_Connector.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)

def test_avm_modelica_connector_has_Locator():
    assert hasattr(avm_modelica_Connector, "Locator")
    descriptor = None
    for klass in avm_modelica_Connector.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
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



def test_avm_cyber_cybermodel_is_not_abstract():
    assert not inspect.isabstract(avm_cyber_CyberModel)


def test_avm_cyber_cybermodel_constructor_exists():
    assert callable(avm_cyber_CyberModel.__init__)


def test_avm_cyber_cybermodel_constructor_args():
    sig = inspect.signature(avm_cyber_CyberModel.__init__)
    params = list(sig.parameters.keys())
    assert "Class" in params, "Missing parameter 'Class'"
    assert "Locator" in params, "Missing parameter 'Locator'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_avm_cyber_cybermodel_has_Class():
    assert hasattr(avm_cyber_CyberModel, "Class")
    descriptor = None
    for klass in avm_cyber_CyberModel.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)

def test_avm_cyber_cybermodel_has_Locator():
    assert hasattr(avm_cyber_CyberModel, "Locator")
    descriptor = None
    for klass in avm_cyber_CyberModel.__mro__:
        if "Locator" in klass.__dict__:
            descriptor = klass.__dict__["Locator"]
            break
    assert isinstance(descriptor, property)

def test_avm_cyber_cybermodel_has_Type():
    assert hasattr(avm_cyber_CyberModel, "Type")
    descriptor = None
    for klass in avm_cyber_CyberModel.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_avm_manufacturing_manufacturingmodel_is_not_abstract():
    assert not inspect.isabstract(avm_manufacturing_ManufacturingModel)


def test_avm_manufacturing_manufacturingmodel_constructor_exists():
    assert callable(avm_manufacturing_ManufacturingModel.__init__)


def test_avm_manufacturing_manufacturingmodel_constructor_args():
    sig = inspect.signature(avm_manufacturing_ManufacturingModel.__init__)
    params = list(sig.parameters.keys())



def test_avm_adamscar_adamscarmodel_is_not_abstract():
    assert not inspect.isabstract(avm_adamsCar_AdamsCarModel)


def test_avm_adamscar_adamscarmodel_constructor_exists():
    assert callable(avm_adamsCar_AdamsCarModel.__init__)


def test_avm_adamscar_adamscarmodel_constructor_args():
    sig = inspect.signature(avm_adamsCar_AdamsCarModel.__init__)
    params = list(sig.parameters.keys())



def test_avm_cad_cadmodel_is_not_abstract():
    assert not inspect.isabstract(avm_cad_CADModel)


def test_avm_cad_cadmodel_constructor_exists():
    assert callable(avm_cad_CADModel.__init__)


def test_avm_cad_cadmodel_constructor_args():
    sig = inspect.signature(avm_cad_CADModel.__init__)
    params = list(sig.parameters.keys())



def test_avm_modelica_modelicamodel_is_not_abstract():
    assert not inspect.isabstract(avm_modelica_ModelicaModel)


def test_avm_modelica_modelicamodel_constructor_exists():
    assert callable(avm_modelica_ModelicaModel.__init__)


def test_avm_modelica_modelicamodel_constructor_args():
    sig = inspect.signature(avm_modelica_ModelicaModel.__init__)
    params = list(sig.parameters.keys())
    assert "Class" in params, "Missing parameter 'Class'"

def test_avm_modelica_modelicamodel_has_Class():
    assert hasattr(avm_modelica_ModelicaModel, "Class")
    descriptor = None
    for klass in avm_modelica_ModelicaModel.__mro__:
        if "Class" in klass.__dict__:
            descriptor = klass.__dict__["Class"]
            break
    assert isinstance(descriptor, property)



def test_avm_workflowtaskbase_is_not_abstract():
    assert not inspect.isabstract(avm_WorkflowTaskBase)


def test_avm_workflowtaskbase_constructor_exists():
    assert callable(avm_WorkflowTaskBase.__init__)


def test_avm_workflowtaskbase_constructor_args():
    sig = inspect.signature(avm_WorkflowTaskBase.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_workflowtaskbase_has_Name():
    assert hasattr(avm_WorkflowTaskBase, "Name")
    descriptor = None
    for klass in avm_WorkflowTaskBase.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_testbenchvaluebase_is_not_abstract():
    assert not inspect.isabstract(avm_TestBenchValueBase)


def test_avm_testbenchvaluebase_constructor_exists():
    assert callable(avm_TestBenchValueBase.__init__)


def test_avm_testbenchvaluebase_constructor_args():
    sig = inspect.signature(avm_TestBenchValueBase.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm_testbenchvaluebase_has_Name():
    assert hasattr(avm_TestBenchValueBase, "Name")
    descriptor = None
    for klass in avm_TestBenchValueBase.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_testbenchvaluebase_has_Notes():
    assert hasattr(avm_TestBenchValueBase, "Notes")
    descriptor = None
    for klass in avm_TestBenchValueBase.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_testbenchvaluebase_has_YPosition():
    assert hasattr(avm_TestBenchValueBase, "YPosition")
    descriptor = None
    for klass in avm_TestBenchValueBase.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_testbenchvaluebase_has_ID():
    assert hasattr(avm_TestBenchValueBase, "ID")
    descriptor = None
    for klass in avm_TestBenchValueBase.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_testbenchvaluebase_has_XPosition():
    assert hasattr(avm_TestBenchValueBase, "XPosition")
    descriptor = None
    for klass in avm_TestBenchValueBase.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm_containerinstancebase_is_not_abstract():
    assert not inspect.isabstract(avm_ContainerInstanceBase)


def test_avm_containerinstancebase_constructor_exists():
    assert callable(avm_ContainerInstanceBase.__init__)


def test_avm_containerinstancebase_constructor_args():
    sig = inspect.signature(avm_ContainerInstanceBase.__init__)
    params = list(sig.parameters.keys())
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "IDinSourceModel" in params, "Missing parameter 'IDinSourceModel'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"

def test_avm_containerinstancebase_has_XPosition():
    assert hasattr(avm_ContainerInstanceBase, "XPosition")
    descriptor = None
    for klass in avm_ContainerInstanceBase.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_containerinstancebase_has_IDinSourceModel():
    assert hasattr(avm_ContainerInstanceBase, "IDinSourceModel")
    descriptor = None
    for klass in avm_ContainerInstanceBase.__mro__:
        if "IDinSourceModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinSourceModel"]
            break
    assert isinstance(descriptor, property)

def test_avm_containerinstancebase_has_YPosition():
    assert hasattr(avm_ContainerInstanceBase, "YPosition")
    descriptor = None
    for klass in avm_ContainerInstanceBase.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
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



def test_avm_settings_is_not_abstract():
    assert not inspect.isabstract(avm_Settings)


def test_avm_settings_constructor_exists():
    assert callable(avm_Settings.__init__)


def test_avm_settings_constructor_args():
    sig = inspect.signature(avm_Settings.__init__)
    params = list(sig.parameters.keys())



def test_avm_workflow_is_not_abstract():
    assert not inspect.isabstract(avm_Workflow)


def test_avm_workflow_constructor_exists():
    assert callable(avm_Workflow.__init__)


def test_avm_workflow_constructor_args():
    sig = inspect.signature(avm_Workflow.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_workflow_has_Name():
    assert hasattr(avm_Workflow, "Name")
    descriptor = None
    for klass in avm_Workflow.__mro__:
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



def test_avm_executiontask_is_not_abstract():
    assert not inspect.isabstract(avm_ExecutionTask)


def test_avm_executiontask_constructor_exists():
    assert callable(avm_ExecutionTask.__init__)


def test_avm_executiontask_constructor_args():
    sig = inspect.signature(avm_ExecutionTask.__init__)
    params = list(sig.parameters.keys())
    assert "Description" in params, "Missing parameter 'Description'"
    assert "Invocation" in params, "Missing parameter 'Invocation'"

def test_avm_executiontask_has_Description():
    assert hasattr(avm_ExecutionTask, "Description")
    descriptor = None
    for klass in avm_ExecutionTask.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)

def test_avm_executiontask_has_Invocation():
    assert hasattr(avm_ExecutionTask, "Invocation")
    descriptor = None
    for klass in avm_ExecutionTask.__mro__:
        if "Invocation" in klass.__dict__:
            descriptor = klass.__dict__["Invocation"]
            break
    assert isinstance(descriptor, property)



def test_avm_interpretertask_is_not_abstract():
    assert not inspect.isabstract(avm_InterpreterTask)


def test_avm_interpretertask_constructor_exists():
    assert callable(avm_InterpreterTask.__init__)


def test_avm_interpretertask_constructor_args():
    sig = inspect.signature(avm_InterpreterTask.__init__)
    params = list(sig.parameters.keys())
    assert "Parameters" in params, "Missing parameter 'Parameters'"
    assert "COMName" in params, "Missing parameter 'COMName'"

def test_avm_interpretertask_has_Parameters():
    assert hasattr(avm_InterpreterTask, "Parameters")
    descriptor = None
    for klass in avm_InterpreterTask.__mro__:
        if "Parameters" in klass.__dict__:
            descriptor = klass.__dict__["Parameters"]
            break
    assert isinstance(descriptor, property)

def test_avm_interpretertask_has_COMName():
    assert hasattr(avm_InterpreterTask, "COMName")
    descriptor = None
    for klass in avm_InterpreterTask.__mro__:
        if "COMName" in klass.__dict__:
            descriptor = klass.__dict__["COMName"]
            break
    assert isinstance(descriptor, property)



def test_avm_toplevelsystemundertest_is_not_abstract():
    assert not inspect.isabstract(avm_TopLevelSystemUnderTest)


def test_avm_toplevelsystemundertest_constructor_exists():
    assert callable(avm_TopLevelSystemUnderTest.__init__)


def test_avm_toplevelsystemundertest_constructor_args():
    sig = inspect.signature(avm_TopLevelSystemUnderTest.__init__)
    params = list(sig.parameters.keys())
    assert "DesignID" in params, "Missing parameter 'DesignID'"

def test_avm_toplevelsystemundertest_has_DesignID():
    assert hasattr(avm_TopLevelSystemUnderTest, "DesignID")
    descriptor = None
    for klass in avm_TopLevelSystemUnderTest.__mro__:
        if "DesignID" in klass.__dict__:
            descriptor = klass.__dict__["DesignID"]
            break
    assert isinstance(descriptor, property)



def test_avm_testbench_is_not_abstract():
    assert not inspect.isabstract(avm_TestBench)


def test_avm_testbench_constructor_exists():
    assert callable(avm_TestBench.__init__)


def test_avm_testbench_constructor_args():
    sig = inspect.signature(avm_TestBench.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_testbench_has_Name():
    assert hasattr(avm_TestBench, "Name")
    descriptor = None
    for klass in avm_TestBench.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_operand_is_not_abstract():
    assert not inspect.isabstract(avm_Operand)


def test_avm_operand_constructor_exists():
    assert callable(avm_Operand.__init__)


def test_avm_operand_constructor_args():
    sig = inspect.signature(avm_Operand.__init__)
    params = list(sig.parameters.keys())
    assert "Symbol" in params, "Missing parameter 'Symbol'"

def test_avm_operand_has_Symbol():
    assert hasattr(avm_Operand, "Symbol")
    descriptor = None
    for klass in avm_Operand.__mro__:
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



def test_avm_complexformula_is_not_abstract():
    assert not inspect.isabstract(avm_ComplexFormula)


def test_avm_complexformula_constructor_exists():
    assert callable(avm_ComplexFormula.__init__)


def test_avm_complexformula_constructor_args():
    sig = inspect.signature(avm_ComplexFormula.__init__)
    params = list(sig.parameters.keys())
    assert "Expression" in params, "Missing parameter 'Expression'"

def test_avm_complexformula_has_Expression():
    assert hasattr(avm_ComplexFormula, "Expression")
    descriptor = None
    for klass in avm_ComplexFormula.__mro__:
        if "Expression" in klass.__dict__:
            descriptor = klass.__dict__["Expression"]
            break
    assert isinstance(descriptor, property)



def test_avm_simpleformula_is_not_abstract():
    assert not inspect.isabstract(avm_SimpleFormula)


def test_avm_simpleformula_constructor_exists():
    assert callable(avm_SimpleFormula.__init__)


def test_avm_simpleformula_constructor_args():
    sig = inspect.signature(avm_SimpleFormula.__init__)
    params = list(sig.parameters.keys())
    assert "Operation" in params, "Missing parameter 'Operation'"

def test_avm_simpleformula_has_Operation():
    assert hasattr(avm_SimpleFormula, "Operation")
    descriptor = None
    for klass in avm_SimpleFormula.__mro__:
        if "Operation" in klass.__dict__:
            descriptor = klass.__dict__["Operation"]
            break
    assert isinstance(descriptor, property)



def test_avm_testinjectionpoint_is_not_abstract():
    assert not inspect.isabstract(avm_TestInjectionPoint)


def test_avm_testinjectionpoint_constructor_exists():
    assert callable(avm_TestInjectionPoint.__init__)


def test_avm_testinjectionpoint_constructor_args():
    sig = inspect.signature(avm_TestInjectionPoint.__init__)
    params = list(sig.parameters.keys())



def test_avm_metric_is_not_abstract():
    assert not inspect.isabstract(avm_Metric)


def test_avm_metric_constructor_exists():
    assert callable(avm_Metric.__init__)


def test_avm_metric_constructor_args():
    sig = inspect.signature(avm_Metric.__init__)
    params = list(sig.parameters.keys())



def test_avm_parameter_is_not_abstract():
    assert not inspect.isabstract(avm_Parameter)


def test_avm_parameter_constructor_exists():
    assert callable(avm_Parameter.__init__)


def test_avm_parameter_constructor_args():
    sig = inspect.signature(avm_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_avm_portmaptarget_is_not_abstract():
    assert not inspect.isabstract(avm_PortMapTarget)


def test_avm_portmaptarget_constructor_exists():
    assert callable(avm_PortMapTarget.__init__)


def test_avm_portmaptarget_constructor_args():
    sig = inspect.signature(avm_PortMapTarget.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm_portmaptarget_has_ID():
    assert hasattr(avm_PortMapTarget, "ID")
    descriptor = None
    for klass in avm_PortMapTarget.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm_componentprimitivepropertyinstance_is_not_abstract():
    assert not inspect.isabstract(avm_ComponentPrimitivePropertyInstance)


def test_avm_componentprimitivepropertyinstance_constructor_exists():
    assert callable(avm_ComponentPrimitivePropertyInstance.__init__)


def test_avm_componentprimitivepropertyinstance_constructor_args():
    sig = inspect.signature(avm_ComponentPrimitivePropertyInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm_componentprimitivepropertyinstance_has_IDinComponentModel():
    assert hasattr(avm_ComponentPrimitivePropertyInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm_ComponentPrimitivePropertyInstance.__mro__:
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



def test_avm_alternative_is_not_abstract():
    assert not inspect.isabstract(avm_Alternative)


def test_avm_alternative_constructor_exists():
    assert callable(avm_Alternative.__init__)


def test_avm_alternative_constructor_args():
    sig = inspect.signature(avm_Alternative.__init__)
    params = list(sig.parameters.keys())



def test_avm_optional_is_not_abstract():
    assert not inspect.isabstract(avm_Optional)


def test_avm_optional_constructor_exists():
    assert callable(avm_Optional.__init__)


def test_avm_optional_constructor_args():
    sig = inspect.signature(avm_Optional.__init__)
    params = list(sig.parameters.keys())



def test_container_is_not_abstract():
    assert not inspect.isabstract(Container)


def test_container_constructor_exists():
    assert callable(Container.__init__)


def test_container_constructor_args():
    sig = inspect.signature(Container.__init__)
    params = list(sig.parameters.keys())



def test_avm_designspacecontainer_is_not_abstract():
    assert not inspect.isabstract(avm_DesignSpaceContainer)


def test_avm_designspacecontainer_constructor_exists():
    assert callable(avm_DesignSpaceContainer.__init__)


def test_avm_designspacecontainer_constructor_args():
    sig = inspect.signature(avm_DesignSpaceContainer.__init__)
    params = list(sig.parameters.keys())



def test_avm_compound_is_not_abstract():
    assert not inspect.isabstract(avm_Compound)


def test_avm_compound_constructor_exists():
    assert callable(avm_Compound.__init__)


def test_avm_compound_constructor_args():
    sig = inspect.signature(avm_Compound.__init__)
    params = list(sig.parameters.keys())



def test_avm_connectorcompositiontarget_is_not_abstract():
    assert not inspect.isabstract(avm_ConnectorCompositionTarget)


def test_avm_connectorcompositiontarget_constructor_exists():
    assert callable(avm_ConnectorCompositionTarget.__init__)


def test_avm_connectorcompositiontarget_constructor_args():
    sig = inspect.signature(avm_ConnectorCompositionTarget.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm_connectorcompositiontarget_has_ID():
    assert hasattr(avm_ConnectorCompositionTarget, "ID")
    descriptor = None
    for klass in avm_ConnectorCompositionTarget.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm_designdomainfeature_is_not_abstract():
    assert not inspect.isabstract(avm_DesignDomainFeature)


def test_avm_designdomainfeature_constructor_exists():
    assert callable(avm_DesignDomainFeature.__init__)


def test_avm_designdomainfeature_constructor_args():
    sig = inspect.signature(avm_DesignDomainFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm_container_is_not_abstract():
    assert not inspect.isabstract(avm_Container)


def test_avm_container_constructor_exists():
    assert callable(avm_Container.__init__)


def test_avm_container_constructor_args():
    sig = inspect.signature(avm_Container.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm_container_has_Name():
    assert hasattr(avm_Container, "Name")
    descriptor = None
    for klass in avm_Container.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_container_has_YPosition():
    assert hasattr(avm_Container, "YPosition")
    descriptor = None
    for klass in avm_Container.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_container_has_XPosition():
    assert hasattr(avm_Container, "XPosition")
    descriptor = None
    for klass in avm_Container.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm_design_is_not_abstract():
    assert not inspect.isabstract(avm_Design)


def test_avm_design_constructor_exists():
    assert callable(avm_Design.__init__)


def test_avm_design_constructor_args():
    sig = inspect.signature(avm_Design.__init__)
    params = list(sig.parameters.keys())
    assert "DesignSpaceSrcID" in params, "Missing parameter 'DesignSpaceSrcID'"
    assert "SchemaVersion" in params, "Missing parameter 'SchemaVersion'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "DesignID" in params, "Missing parameter 'DesignID'"

def test_avm_design_has_DesignSpaceSrcID():
    assert hasattr(avm_Design, "DesignSpaceSrcID")
    descriptor = None
    for klass in avm_Design.__mro__:
        if "DesignSpaceSrcID" in klass.__dict__:
            descriptor = klass.__dict__["DesignSpaceSrcID"]
            break
    assert isinstance(descriptor, property)

def test_avm_design_has_SchemaVersion():
    assert hasattr(avm_Design, "SchemaVersion")
    descriptor = None
    for klass in avm_Design.__mro__:
        if "SchemaVersion" in klass.__dict__:
            descriptor = klass.__dict__["SchemaVersion"]
            break
    assert isinstance(descriptor, property)

def test_avm_design_has_Name():
    assert hasattr(avm_Design, "Name")
    descriptor = None
    for klass in avm_Design.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_design_has_DesignID():
    assert hasattr(avm_Design, "DesignID")
    descriptor = None
    for klass in avm_Design.__mro__:
        if "DesignID" in klass.__dict__:
            descriptor = klass.__dict__["DesignID"]
            break
    assert isinstance(descriptor, property)



def test_avm_componentinstance_is_not_abstract():
    assert not inspect.isabstract(avm_ComponentInstance)


def test_avm_componentinstance_constructor_exists():
    assert callable(avm_ComponentInstance.__init__)


def test_avm_componentinstance_constructor_args():
    sig = inspect.signature(avm_ComponentInstance.__init__)
    params = list(sig.parameters.keys())
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "ComponentID" in params, "Missing parameter 'ComponentID'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "DesignSpaceSrcComponentID" in params, "Missing parameter 'DesignSpaceSrcComponentID'"

def test_avm_componentinstance_has_YPosition():
    assert hasattr(avm_ComponentInstance, "YPosition")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_componentinstance_has_XPosition():
    assert hasattr(avm_ComponentInstance, "XPosition")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_componentinstance_has_ComponentID():
    assert hasattr(avm_ComponentInstance, "ComponentID")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "ComponentID" in klass.__dict__:
            descriptor = klass.__dict__["ComponentID"]
            break
    assert isinstance(descriptor, property)

def test_avm_componentinstance_has_Name():
    assert hasattr(avm_ComponentInstance, "Name")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_componentinstance_has_ID():
    assert hasattr(avm_ComponentInstance, "ID")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_componentinstance_has_DesignSpaceSrcComponentID():
    assert hasattr(avm_ComponentInstance, "DesignSpaceSrcComponentID")
    descriptor = None
    for klass in avm_ComponentInstance.__mro__:
        if "DesignSpaceSrcComponentID" in klass.__dict__:
            descriptor = klass.__dict__["DesignSpaceSrcComponentID"]
            break
    assert isinstance(descriptor, property)



def test_avm_domainmodelmetric_is_not_abstract():
    assert not inspect.isabstract(avm_DomainModelMetric)


def test_avm_domainmodelmetric_constructor_exists():
    assert callable(avm_DomainModelMetric.__init__)


def test_avm_domainmodelmetric_constructor_args():
    sig = inspect.signature(avm_DomainModelMetric.__init__)
    params = list(sig.parameters.keys())
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm_domainmodelmetric_has_XPosition():
    assert hasattr(avm_DomainModelMetric, "XPosition")
    descriptor = None
    for klass in avm_DomainModelMetric.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodelmetric_has_ID():
    assert hasattr(avm_DomainModelMetric, "ID")
    descriptor = None
    for klass in avm_DomainModelMetric.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodelmetric_has_YPosition():
    assert hasattr(avm_DomainModelMetric, "YPosition")
    descriptor = None
    for klass in avm_DomainModelMetric.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodelmetric_has_Notes():
    assert hasattr(avm_DomainModelMetric, "Notes")
    descriptor = None
    for klass in avm_DomainModelMetric.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_distributionrestriction_is_not_abstract():
    assert not inspect.isabstract(DistributionRestriction)


def test_distributionrestriction_constructor_exists():
    assert callable(DistributionRestriction.__init__)


def test_distributionrestriction_constructor_args():
    sig = inspect.signature(DistributionRestriction.__init__)
    params = list(sig.parameters.keys())



def test_avm_itar_is_not_abstract():
    assert not inspect.isabstract(avm_ITAR)


def test_avm_itar_constructor_exists():
    assert callable(avm_ITAR.__init__)


def test_avm_itar_constructor_args():
    sig = inspect.signature(avm_ITAR.__init__)
    params = list(sig.parameters.keys())



def test_avm_doddistributionstatement_is_not_abstract():
    assert not inspect.isabstract(avm_DoDDistributionStatement)


def test_avm_doddistributionstatement_constructor_exists():
    assert callable(avm_DoDDistributionStatement.__init__)


def test_avm_doddistributionstatement_constructor_args():
    sig = inspect.signature(avm_DoDDistributionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_avm_doddistributionstatement_has_Type():
    assert hasattr(avm_DoDDistributionStatement, "Type")
    descriptor = None
    for klass in avm_DoDDistributionStatement.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_avm_proprietary_is_not_abstract():
    assert not inspect.isabstract(avm_Proprietary)


def test_avm_proprietary_constructor_exists():
    assert callable(avm_Proprietary.__init__)


def test_avm_proprietary_constructor_args():
    sig = inspect.signature(avm_Proprietary.__init__)
    params = list(sig.parameters.keys())
    assert "Organization" in params, "Missing parameter 'Organization'"

def test_avm_proprietary_has_Organization():
    assert hasattr(avm_Proprietary, "Organization")
    descriptor = None
    for klass in avm_Proprietary.__mro__:
        if "Organization" in klass.__dict__:
            descriptor = klass.__dict__["Organization"]
            break
    assert isinstance(descriptor, property)



def test_avm_securityclassification_is_not_abstract():
    assert not inspect.isabstract(avm_SecurityClassification)


def test_avm_securityclassification_constructor_exists():
    assert callable(avm_SecurityClassification.__init__)


def test_avm_securityclassification_constructor_args():
    sig = inspect.signature(avm_SecurityClassification.__init__)
    params = list(sig.parameters.keys())
    assert "Level" in params, "Missing parameter 'Level'"

def test_avm_securityclassification_has_Level():
    assert hasattr(avm_SecurityClassification, "Level")
    descriptor = None
    for klass in avm_SecurityClassification.__mro__:
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



def test_avm_normaldistribution_is_not_abstract():
    assert not inspect.isabstract(avm_NormalDistribution)


def test_avm_normaldistribution_constructor_exists():
    assert callable(avm_NormalDistribution.__init__)


def test_avm_normaldistribution_constructor_args():
    sig = inspect.signature(avm_NormalDistribution.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_avm_compoundproperty_is_not_abstract():
    assert not inspect.isabstract(avm_CompoundProperty)


def test_avm_compoundproperty_constructor_exists():
    assert callable(avm_CompoundProperty.__init__)


def test_avm_compoundproperty_constructor_args():
    sig = inspect.signature(avm_CompoundProperty.__init__)
    params = list(sig.parameters.keys())



def test_avm_primitiveproperty_is_not_abstract():
    assert not inspect.isabstract(avm_PrimitiveProperty)


def test_avm_primitiveproperty_constructor_exists():
    assert callable(avm_PrimitiveProperty.__init__)


def test_avm_primitiveproperty_constructor_args():
    sig = inspect.signature(avm_PrimitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_avm_uniformdistribution_is_not_abstract():
    assert not inspect.isabstract(avm_UniformDistribution)


def test_avm_uniformdistribution_constructor_exists():
    assert callable(avm_UniformDistribution.__init__)


def test_avm_uniformdistribution_constructor_args():
    sig = inspect.signature(avm_UniformDistribution.__init__)
    params = list(sig.parameters.keys())



def test_avm_domainmodelparameter_is_not_abstract():
    assert not inspect.isabstract(avm_DomainModelParameter)


def test_avm_domainmodelparameter_constructor_exists():
    assert callable(avm_DomainModelParameter.__init__)


def test_avm_domainmodelparameter_constructor_args():
    sig = inspect.signature(avm_DomainModelParameter.__init__)
    params = list(sig.parameters.keys())
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm_domainmodelparameter_has_Notes():
    assert hasattr(avm_DomainModelParameter, "Notes")
    descriptor = None
    for klass in avm_DomainModelParameter.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodelparameter_has_YPosition():
    assert hasattr(avm_DomainModelParameter, "YPosition")
    descriptor = None
    for klass in avm_DomainModelParameter.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodelparameter_has_XPosition():
    assert hasattr(avm_DomainModelParameter, "XPosition")
    descriptor = None
    for klass in avm_DomainModelParameter.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_avm_abstractport_is_not_abstract():
    assert not inspect.isabstract(avm_AbstractPort)


def test_avm_abstractport_constructor_exists():
    assert callable(avm_AbstractPort.__init__)


def test_avm_abstractport_constructor_args():
    sig = inspect.signature(avm_AbstractPort.__init__)
    params = list(sig.parameters.keys())



def test_avm_domainmodelport_is_not_abstract():
    assert not inspect.isabstract(avm_DomainModelPort)


def test_avm_domainmodelport_constructor_exists():
    assert callable(avm_DomainModelPort.__init__)


def test_avm_domainmodelport_constructor_args():
    sig = inspect.signature(avm_DomainModelPort.__init__)
    params = list(sig.parameters.keys())



def test_portmaptarget_is_not_abstract():
    assert not inspect.isabstract(PortMapTarget)


def test_portmaptarget_constructor_exists():
    assert callable(PortMapTarget.__init__)


def test_portmaptarget_constructor_args():
    sig = inspect.signature(PortMapTarget.__init__)
    params = list(sig.parameters.keys())



def test_avm_componentportinstance_is_not_abstract():
    assert not inspect.isabstract(avm_ComponentPortInstance)


def test_avm_componentportinstance_constructor_exists():
    assert callable(avm_ComponentPortInstance.__init__)


def test_avm_componentportinstance_constructor_args():
    sig = inspect.signature(avm_ComponentPortInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm_componentportinstance_has_IDinComponentModel():
    assert hasattr(avm_ComponentPortInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm_ComponentPortInstance.__mro__:
        if "IDinComponentModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinComponentModel"]
            break
    assert isinstance(descriptor, property)



def test_avm_connectorfeature_is_not_abstract():
    assert not inspect.isabstract(avm_ConnectorFeature)


def test_avm_connectorfeature_constructor_exists():
    assert callable(avm_ConnectorFeature.__init__)


def test_avm_connectorfeature_constructor_args():
    sig = inspect.signature(avm_ConnectorFeature.__init__)
    params = list(sig.parameters.keys())



def test_avm_assemblydetail_is_not_abstract():
    assert not inspect.isabstract(avm_assemblyDetail)


def test_avm_assemblydetail_constructor_exists():
    assert callable(avm_assemblyDetail.__init__)


def test_avm_assemblydetail_constructor_args():
    sig = inspect.signature(avm_assemblyDetail.__init__)
    params = list(sig.parameters.keys())



def test_connectorcompositiontarget_is_not_abstract():
    assert not inspect.isabstract(ConnectorCompositionTarget)


def test_connectorcompositiontarget_constructor_exists():
    assert callable(ConnectorCompositionTarget.__init__)


def test_connectorcompositiontarget_constructor_args():
    sig = inspect.signature(ConnectorCompositionTarget.__init__)
    params = list(sig.parameters.keys())



def test_avm_componentconnectorinstance_is_not_abstract():
    assert not inspect.isabstract(avm_ComponentConnectorInstance)


def test_avm_componentconnectorinstance_constructor_exists():
    assert callable(avm_ComponentConnectorInstance.__init__)


def test_avm_componentconnectorinstance_constructor_args():
    sig = inspect.signature(avm_ComponentConnectorInstance.__init__)
    params = list(sig.parameters.keys())
    assert "IDinComponentModel" in params, "Missing parameter 'IDinComponentModel'"

def test_avm_componentconnectorinstance_has_IDinComponentModel():
    assert hasattr(avm_ComponentConnectorInstance, "IDinComponentModel")
    descriptor = None
    for klass in avm_ComponentConnectorInstance.__mro__:
        if "IDinComponentModel" in klass.__dict__:
            descriptor = klass.__dict__["IDinComponentModel"]
            break
    assert isinstance(descriptor, property)



def test_avm_valuenode_is_not_abstract():
    assert not inspect.isabstract(avm_ValueNode)


def test_avm_valuenode_constructor_exists():
    assert callable(avm_ValueNode.__init__)


def test_avm_valuenode_constructor_args():
    sig = inspect.signature(avm_ValueNode.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm_valuenode_has_ID():
    assert hasattr(avm_ValueNode, "ID")
    descriptor = None
    for klass in avm_ValueNode.__mro__:
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



def test_avm_derivedvalue_is_not_abstract():
    assert not inspect.isabstract(avm_DerivedValue)


def test_avm_derivedvalue_constructor_exists():
    assert callable(avm_DerivedValue.__init__)


def test_avm_derivedvalue_constructor_args():
    sig = inspect.signature(avm_DerivedValue.__init__)
    params = list(sig.parameters.keys())



def test_avm_parametricvalue_is_not_abstract():
    assert not inspect.isabstract(avm_ParametricValue)


def test_avm_parametricvalue_constructor_exists():
    assert callable(avm_ParametricValue.__init__)


def test_avm_parametricvalue_constructor_args():
    sig = inspect.signature(avm_ParametricValue.__init__)
    params = list(sig.parameters.keys())



def test_avm_calculatedvalue_is_not_abstract():
    assert not inspect.isabstract(avm_CalculatedValue)


def test_avm_calculatedvalue_constructor_exists():
    assert callable(avm_CalculatedValue.__init__)


def test_avm_calculatedvalue_constructor_args():
    sig = inspect.signature(avm_CalculatedValue.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Expression" in params, "Missing parameter 'Expression'"

def test_avm_calculatedvalue_has_Type():
    assert hasattr(avm_CalculatedValue, "Type")
    descriptor = None
    for klass in avm_CalculatedValue.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_avm_calculatedvalue_has_Expression():
    assert hasattr(avm_CalculatedValue, "Expression")
    descriptor = None
    for klass in avm_CalculatedValue.__mro__:
        if "Expression" in klass.__dict__:
            descriptor = klass.__dict__["Expression"]
            break
    assert isinstance(descriptor, property)



def test_avm_parametricenumeratedvalue_is_not_abstract():
    assert not inspect.isabstract(avm_ParametricEnumeratedValue)


def test_avm_parametricenumeratedvalue_constructor_exists():
    assert callable(avm_ParametricEnumeratedValue.__init__)


def test_avm_parametricenumeratedvalue_constructor_args():
    sig = inspect.signature(avm_ParametricEnumeratedValue.__init__)
    params = list(sig.parameters.keys())



def test_avm_probabilisticvalue_is_not_abstract():
    assert not inspect.isabstract(avm_ProbabilisticValue)


def test_avm_probabilisticvalue_constructor_exists():
    assert callable(avm_ProbabilisticValue.__init__)


def test_avm_probabilisticvalue_constructor_args():
    sig = inspect.signature(avm_ProbabilisticValue.__init__)
    params = list(sig.parameters.keys())



def test_avm_fixedvalue_is_not_abstract():
    assert not inspect.isabstract(avm_FixedValue)


def test_avm_fixedvalue_constructor_exists():
    assert callable(avm_FixedValue.__init__)


def test_avm_fixedvalue_constructor_args():
    sig = inspect.signature(avm_FixedValue.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"
    assert "Uncertainty" in params, "Missing parameter 'Uncertainty'"

def test_avm_fixedvalue_has_Value():
    assert hasattr(avm_FixedValue, "Value")
    descriptor = None
    for klass in avm_FixedValue.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)

def test_avm_fixedvalue_has_Uncertainty():
    assert hasattr(avm_FixedValue, "Uncertainty")
    descriptor = None
    for klass in avm_FixedValue.__mro__:
        if "Uncertainty" in klass.__dict__:
            descriptor = klass.__dict__["Uncertainty"]
            break
    assert isinstance(descriptor, property)



def test_avm_datasource_is_not_abstract():
    assert not inspect.isabstract(avm_DataSource)


def test_avm_datasource_constructor_exists():
    assert callable(avm_DataSource.__init__)


def test_avm_datasource_constructor_args():
    sig = inspect.signature(avm_DataSource.__init__)
    params = list(sig.parameters.keys())
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm_datasource_has_Notes():
    assert hasattr(avm_DataSource, "Notes")
    descriptor = None
    for klass in avm_DataSource.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_avm_valueexpressiontype_is_not_abstract():
    assert not inspect.isabstract(avm_ValueExpressionType)


def test_avm_valueexpressiontype_constructor_exists():
    assert callable(avm_ValueExpressionType.__init__)


def test_avm_valueexpressiontype_constructor_args():
    sig = inspect.signature(avm_ValueExpressionType.__init__)
    params = list(sig.parameters.keys())



def test_valuenode_is_not_abstract():
    assert not inspect.isabstract(ValueNode)


def test_valuenode_constructor_exists():
    assert callable(ValueNode.__init__)


def test_valuenode_constructor_args():
    sig = inspect.signature(ValueNode.__init__)
    params = list(sig.parameters.keys())



def test_avm_valueflowmux_is_not_abstract():
    assert not inspect.isabstract(avm_ValueFlowMux)


def test_avm_valueflowmux_constructor_exists():
    assert callable(avm_ValueFlowMux.__init__)


def test_avm_valueflowmux_constructor_args():
    sig = inspect.signature(avm_ValueFlowMux.__init__)
    params = list(sig.parameters.keys())



def test_avm_value_is_not_abstract():
    assert not inspect.isabstract(avm_Value)


def test_avm_value_constructor_exists():
    assert callable(avm_Value.__init__)


def test_avm_value_constructor_args():
    sig = inspect.signature(avm_Value.__init__)
    params = list(sig.parameters.keys())
    assert "DataType" in params, "Missing parameter 'DataType'"
    assert "Dimensions" in params, "Missing parameter 'Dimensions'"
    assert "DimensionType" in params, "Missing parameter 'DimensionType'"
    assert "Unit" in params, "Missing parameter 'Unit'"

def test_avm_value_has_DataType():
    assert hasattr(avm_Value, "DataType")
    descriptor = None
    for klass in avm_Value.__mro__:
        if "DataType" in klass.__dict__:
            descriptor = klass.__dict__["DataType"]
            break
    assert isinstance(descriptor, property)

def test_avm_value_has_Dimensions():
    assert hasattr(avm_Value, "Dimensions")
    descriptor = None
    for klass in avm_Value.__mro__:
        if "Dimensions" in klass.__dict__:
            descriptor = klass.__dict__["Dimensions"]
            break
    assert isinstance(descriptor, property)

def test_avm_value_has_DimensionType():
    assert hasattr(avm_Value, "DimensionType")
    descriptor = None
    for klass in avm_Value.__mro__:
        if "DimensionType" in klass.__dict__:
            descriptor = klass.__dict__["DimensionType"]
            break
    assert isinstance(descriptor, property)

def test_avm_value_has_Unit():
    assert hasattr(avm_Value, "Unit")
    descriptor = None
    for klass in avm_Value.__mro__:
        if "Unit" in klass.__dict__:
            descriptor = klass.__dict__["Unit"]
            break
    assert isinstance(descriptor, property)



def test_avm_analysisconstruct_is_not_abstract():
    assert not inspect.isabstract(avm_AnalysisConstruct)


def test_avm_analysisconstruct_constructor_exists():
    assert callable(avm_AnalysisConstruct.__init__)


def test_avm_analysisconstruct_constructor_args():
    sig = inspect.signature(avm_AnalysisConstruct.__init__)
    params = list(sig.parameters.keys())



def test_avm_port_is_not_abstract():
    assert not inspect.isabstract(avm_Port)


def test_avm_port_constructor_exists():
    assert callable(avm_Port.__init__)


def test_avm_port_constructor_args():
    sig = inspect.signature(avm_Port.__init__)
    params = list(sig.parameters.keys())
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"

def test_avm_port_has_Definition():
    assert hasattr(avm_Port, "Definition")
    descriptor = None
    for klass in avm_Port.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm_port_has_Notes():
    assert hasattr(avm_Port, "Notes")
    descriptor = None
    for klass in avm_Port.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_port_has_YPosition():
    assert hasattr(avm_Port, "YPosition")
    descriptor = None
    for klass in avm_Port.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_port_has_Name():
    assert hasattr(avm_Port, "Name")
    descriptor = None
    for klass in avm_Port.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_port_has_XPosition():
    assert hasattr(avm_Port, "XPosition")
    descriptor = None
    for klass in avm_Port.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm_distributionrestriction_is_not_abstract():
    assert not inspect.isabstract(avm_DistributionRestriction)


def test_avm_distributionrestriction_constructor_exists():
    assert callable(avm_DistributionRestriction.__init__)


def test_avm_distributionrestriction_constructor_args():
    sig = inspect.signature(avm_DistributionRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "Notes" in params, "Missing parameter 'Notes'"

def test_avm_distributionrestriction_has_Notes():
    assert hasattr(avm_DistributionRestriction, "Notes")
    descriptor = None
    for klass in avm_DistributionRestriction.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)



def test_avm_connector_is_not_abstract():
    assert not inspect.isabstract(avm_Connector)


def test_avm_connector_constructor_exists():
    assert callable(avm_Connector.__init__)


def test_avm_connector_constructor_args():
    sig = inspect.signature(avm_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_connector_has_Definition():
    assert hasattr(avm_Connector, "Definition")
    descriptor = None
    for klass in avm_Connector.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm_connector_has_XPosition():
    assert hasattr(avm_Connector, "XPosition")
    descriptor = None
    for klass in avm_Connector.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_connector_has_YPosition():
    assert hasattr(avm_Connector, "YPosition")
    descriptor = None
    for klass in avm_Connector.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_connector_has_Notes():
    assert hasattr(avm_Connector, "Notes")
    descriptor = None
    for klass in avm_Connector.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_connector_has_Name():
    assert hasattr(avm_Connector, "Name")
    descriptor = None
    for klass in avm_Connector.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_resource_is_not_abstract():
    assert not inspect.isabstract(avm_Resource)


def test_avm_resource_constructor_exists():
    assert callable(avm_Resource.__init__)


def test_avm_resource_constructor_args():
    sig = inspect.signature(avm_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Path" in params, "Missing parameter 'Path'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Hash" in params, "Missing parameter 'Hash'"

def test_avm_resource_has_ID():
    assert hasattr(avm_Resource, "ID")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_XPosition():
    assert hasattr(avm_Resource, "XPosition")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_YPosition():
    assert hasattr(avm_Resource, "YPosition")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_Name():
    assert hasattr(avm_Resource, "Name")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_Path():
    assert hasattr(avm_Resource, "Path")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "Path" in klass.__dict__:
            descriptor = klass.__dict__["Path"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_Notes():
    assert hasattr(avm_Resource, "Notes")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_resource_has_Hash():
    assert hasattr(avm_Resource, "Hash")
    descriptor = None
    for klass in avm_Resource.__mro__:
        if "Hash" in klass.__dict__:
            descriptor = klass.__dict__["Hash"]
            break
    assert isinstance(descriptor, property)



def test_avm_property_is_not_abstract():
    assert not inspect.isabstract(avm_Property)


def test_avm_property_constructor_exists():
    assert callable(avm_Property.__init__)


def test_avm_property_constructor_args():
    sig = inspect.signature(avm_Property.__init__)
    params = list(sig.parameters.keys())
    assert "Definition" in params, "Missing parameter 'Definition'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "OnDataSheet" in params, "Missing parameter 'OnDataSheet'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_avm_property_has_Definition():
    assert hasattr(avm_Property, "Definition")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "Definition" in klass.__dict__:
            descriptor = klass.__dict__["Definition"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_YPosition():
    assert hasattr(avm_Property, "YPosition")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_Name():
    assert hasattr(avm_Property, "Name")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_Notes():
    assert hasattr(avm_Property, "Notes")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_XPosition():
    assert hasattr(avm_Property, "XPosition")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_OnDataSheet():
    assert hasattr(avm_Property, "OnDataSheet")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "OnDataSheet" in klass.__dict__:
            descriptor = klass.__dict__["OnDataSheet"]
            break
    assert isinstance(descriptor, property)

def test_avm_property_has_ID():
    assert hasattr(avm_Property, "ID")
    descriptor = None
    for klass in avm_Property.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_avm_formula_is_not_abstract():
    assert not inspect.isabstract(avm_Formula)


def test_avm_formula_constructor_exists():
    assert callable(avm_Formula.__init__)


def test_avm_formula_constructor_args():
    sig = inspect.signature(avm_Formula.__init__)
    params = list(sig.parameters.keys())
    assert "YPosition" in params, "Missing parameter 'YPosition'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_avm_formula_has_YPosition():
    assert hasattr(avm_Formula, "YPosition")
    descriptor = None
    for klass in avm_Formula.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_formula_has_XPosition():
    assert hasattr(avm_Formula, "XPosition")
    descriptor = None
    for klass in avm_Formula.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_formula_has_Name():
    assert hasattr(avm_Formula, "Name")
    descriptor = None
    for klass in avm_Formula.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_avm_domainmodel__is_not_abstract():
    assert not inspect.isabstract(avm_DomainModel_)


def test_avm_domainmodel__constructor_exists():
    assert callable(avm_DomainModel_.__init__)


def test_avm_domainmodel__constructor_args():
    sig = inspect.signature(avm_DomainModel_.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Notes" in params, "Missing parameter 'Notes'"
    assert "Author" in params, "Missing parameter 'Author'"
    assert "XPosition" in params, "Missing parameter 'XPosition'"
    assert "YPosition" in params, "Missing parameter 'YPosition'"

def test_avm_domainmodel__has_Name():
    assert hasattr(avm_DomainModel_, "Name")
    descriptor = None
    for klass in avm_DomainModel_.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodel__has_Notes():
    assert hasattr(avm_DomainModel_, "Notes")
    descriptor = None
    for klass in avm_DomainModel_.__mro__:
        if "Notes" in klass.__dict__:
            descriptor = klass.__dict__["Notes"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodel__has_Author():
    assert hasattr(avm_DomainModel_, "Author")
    descriptor = None
    for klass in avm_DomainModel_.__mro__:
        if "Author" in klass.__dict__:
            descriptor = klass.__dict__["Author"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodel__has_XPosition():
    assert hasattr(avm_DomainModel_, "XPosition")
    descriptor = None
    for klass in avm_DomainModel_.__mro__:
        if "XPosition" in klass.__dict__:
            descriptor = klass.__dict__["XPosition"]
            break
    assert isinstance(descriptor, property)

def test_avm_domainmodel__has_YPosition():
    assert hasattr(avm_DomainModel_, "YPosition")
    descriptor = None
    for klass in avm_DomainModel_.__mro__:
        if "YPosition" in klass.__dict__:
            descriptor = klass.__dict__["YPosition"]
            break
    assert isinstance(descriptor, property)



def test_avm_component_is_not_abstract():
    assert not inspect.isabstract(avm_Component)


def test_avm_component_constructor_exists():
    assert callable(avm_Component.__init__)


def test_avm_component_constructor_args():
    sig = inspect.signature(avm_Component.__init__)
    params = list(sig.parameters.keys())
    assert "Classifications" in params, "Missing parameter 'Classifications'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Version" in params, "Missing parameter 'Version'"
    assert "Supercedes" in params, "Missing parameter 'Supercedes'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "SchemaVersion" in params, "Missing parameter 'SchemaVersion'"

def test_avm_component_has_Classifications():
    assert hasattr(avm_Component, "Classifications")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "Classifications" in klass.__dict__:
            descriptor = klass.__dict__["Classifications"]
            break
    assert isinstance(descriptor, property)

def test_avm_component_has_Name():
    assert hasattr(avm_Component, "Name")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_avm_component_has_Version():
    assert hasattr(avm_Component, "Version")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "Version" in klass.__dict__:
            descriptor = klass.__dict__["Version"]
            break
    assert isinstance(descriptor, property)

def test_avm_component_has_Supercedes():
    assert hasattr(avm_Component, "Supercedes")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "Supercedes" in klass.__dict__:
            descriptor = klass.__dict__["Supercedes"]
            break
    assert isinstance(descriptor, property)

def test_avm_component_has_ID():
    assert hasattr(avm_Component, "ID")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_avm_component_has_SchemaVersion():
    assert hasattr(avm_Component, "SchemaVersion")
    descriptor = None
    for klass in avm_Component.__mro__:
        if "SchemaVersion" in klass.__dict__:
            descriptor = klass.__dict__["SchemaVersion"]
            break
    assert isinstance(descriptor, property)

def test_boundtypeenum_exists():
    # Check that the Enumeration exists
    assert BoundTypeEnum is not None

def test_boundtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BoundTypeEnum]
    expected_literals = [
        "MustExceed",
        "MustNotMeetOrExceed",
        "MustExceedOrEqual",
        "MustNotExceed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BoundTypeEnum"

def test_calculationtypeenum_exists():
    # Check that the Enumeration exists
    assert CalculationTypeEnum is not None

def test_calculationtypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CalculationTypeEnum]
    expected_literals = [
        "Python",
        "Declarative",
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
        "Maximum",
        "Minimum",
        "Multiplication",
        "GeometricMean",
        "Addition",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleFormulaOperation"

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

def test_doddistributionstatementenum_exists():
    # Check that the Enumeration exists
    assert DoDDistributionStatementEnum is not None

def test_doddistributionstatementenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DoDDistributionStatementEnum]
    expected_literals = [
        "StatementE",
        "StatementA",
        "StatementB",
        "StatementD",
        "StatementC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DoDDistributionStatementEnum"

def test_geometryqualifierenum_exists():
    # Check that the Enumeration exists
    assert GeometryQualifierEnum is not None

def test_geometryqualifierenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GeometryQualifierEnum]
    expected_literals = [
        "BoundaryOnly",
        "InteriorAndBoundary",
        "InteriorOnly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GeometryQualifierEnum"

def test_partintersectionenum_exists():
    # Check that the Enumeration exists
    assert PartIntersectionEnum is not None

def test_partintersectionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PartIntersectionEnum]
    expected_literals = [
        "IntersectionWithAnyParts",
        "IntersectionWithReferencedParts",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PartIntersectionEnum"

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

def test_redeclaretypeenum_exists():
    # Check that the Enumeration exists
    assert RedeclareTypeEnum is not None

def test_redeclaretypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RedeclareTypeEnum]
    expected_literals = [
        "Package",
        "Block",
        "Record",
        "Class",
        "Connector",
        "Function",
        "Model",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RedeclareTypeEnum"

def test_modeltype_exists():
    # Check that the Enumeration exists
    assert ModelType is not None

def test_modeltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModelType]
    expected_literals = [
        "Simulink",
        "ESMoL",
        "SignalFlow",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModelType"

def test_datatypeenum_exists():
    # Check that the Enumeration exists
    assert DataTypeEnum is not None

def test_datatypeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypeEnum]
    expected_literals = [
        "Real",
        "Integer",
        "Boolean",
        "String",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypeEnum"

def test_jobmanagertoolselection_exists():
    # Check that the Enumeration exists
    assert JobManagerToolSelection is not None

def test_jobmanagertoolselection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in JobManagerToolSelection]
    expected_literals = [
        "Dymola_2014",
        "Dymola_2013",
        "Dymola_latest",
        "OpenModelica_latest",
        "JModelica_1_12",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in JobManagerToolSelection"

def test_customgeometryinputoperationenum_exists():
    # Check that the Enumeration exists
    assert CustomGeometryInputOperationEnum is not None

def test_customgeometryinputoperationenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CustomGeometryInputOperationEnum]
    expected_literals = [
        "Subtraction",
        "Union",
        "Intersection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CustomGeometryInputOperationEnum"


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
manufacturing_avm_Value_strategy = st.builds(
    manufacturing_avm_Value,
)
avm_adamsCar_FileReference_strategy = st.builds(
    avm_adamsCar_FileReference,
    Name=
        safe_text,
    ID=
        safe_text,
    FilePath=
        safe_text
)
adamsCar_avm_Value_strategy = st.builds(
    adamsCar_avm_Value,
)
FileReference_strategy = st.builds(
    FileReference,
)
Axis_strategy = st.builds(
    Axis,
)
KinematicJointSpec_strategy = st.builds(
    KinematicJointSpec,
)
avm_cad_RevoluteJointSpec_strategy = st.builds(
    avm_cad_RevoluteJointSpec,
)
cad_avm_ComponentInstance_strategy = st.builds(
    cad_avm_ComponentInstance,
)
DesignDomainFeature_strategy = st.builds(
    DesignDomainFeature,
)
avm_cad_AssemblyRoot_strategy = st.builds(
    avm_cad_AssemblyRoot,
)
ConnectorFeature_strategy = st.builds(
    ConnectorFeature,
)
avm_cad_KinematicJointSpec_strategy = st.builds(
    avm_cad_KinematicJointSpec,
)
avm_cad_GuideDatum_strategy = st.builds(
    avm_cad_GuideDatum,
)
avm_cad_PlaneReference_strategy = st.builds(
    avm_cad_PlaneReference,
)
PlaneReference_strategy = st.builds(
    PlaneReference,
)
avm_cad_TranslationalJointSpec_strategy = st.builds(
    avm_cad_TranslationalJointSpec,
)
avm_cad_CustomGeometryInput_strategy = st.builds(
    avm_cad_CustomGeometryInput,
    Operation=
        safe_text
)
CustomGeometryInput_strategy = st.builds(
    CustomGeometryInput,
)
Geometry3D_strategy = st.builds(
    Geometry3D,
)
avm_cad_Sphere_strategy = st.builds(
    avm_cad_Sphere,
)
avm_cad_ExtrudedGeometry_strategy = st.builds(
    avm_cad_ExtrudedGeometry,
)
avm_cad_Surface_strategy = st.builds(
    avm_cad_Surface,
)
Point_strategy = st.builds(
    Point,
)
avm_cad_PointReference_strategy = st.builds(
    avm_cad_PointReference,
)
AnalysisConstruct_strategy = st.builds(
    AnalysisConstruct,
)
avm_cad_Geometry_strategy = st.builds(
    avm_cad_Geometry,
    GeometryQualifier=
        safe_text,
    PartIntersectionModifier=
        safe_text
)
Plane_strategy = st.builds(
    Plane,
)
cad_avm_Value_strategy = st.builds(
    cad_avm_Value,
)
PointReference_strategy = st.builds(
    PointReference,
)
Geometry2D_strategy = st.builds(
    Geometry2D,
)
avm_cad_Polygon_strategy = st.builds(
    avm_cad_Polygon,
)
avm_cad_Circle_strategy = st.builds(
    avm_cad_Circle,
)
Geometry_strategy = st.builds(
    Geometry,
)
avm_cad_Geometry3D_strategy = st.builds(
    avm_cad_Geometry3D,
)
avm_cad_CustomGeometry_strategy = st.builds(
    avm_cad_CustomGeometry,
)
avm_cad_Geometry2D_strategy = st.builds(
    avm_cad_Geometry2D,
)
Datum_strategy = st.builds(
    Datum,
)
avm_cad_CoordinateSystem_strategy = st.builds(
    avm_cad_CoordinateSystem,
)
avm_cad_Point_strategy = st.builds(
    avm_cad_Point,
)
avm_cad_Axis_strategy = st.builds(
    avm_cad_Axis,
)
avm_cad_Plane_strategy = st.builds(
    avm_cad_Plane,
)
Settings_strategy = st.builds(
    Settings,
)
avm_modelica_SolverSettings_strategy = st.builds(
    avm_modelica_SolverSettings,
    JobManagerToolSelection=
        safe_text,
    NumberOfIntervals=
        safe_text,
    ToolSpecificAnnotations=
        safe_text,
    StartTime=
        safe_text,
    IntervalLength=
        safe_text,
    Solver=
        safe_text,
    IntervalMethod=
        safe_text,
    Tolerance=
        safe_text,
    StopTime=
        safe_text
)
avm_modelica_Limit_strategy = st.builds(
    avm_modelica_Limit,
    BoundType=
        safe_text,
    VariableLocator=
        safe_text,
    Name=
        safe_text,
    ToleranceTimeWindow=
        safe_text,
    Notes=
        safe_text
)
DomainModelMetric_strategy = st.builds(
    DomainModelMetric,
)
avm_manufacturing_Metric_strategy = st.builds(
    avm_manufacturing_Metric,
    Name=
        safe_text
)
avm_cad_Metric_strategy = st.builds(
    avm_cad_Metric,
    Name=
        safe_text
)
avm_modelica_Metric_strategy = st.builds(
    avm_modelica_Metric,
    Locator=
        safe_text
)
modelica_avm_Value_strategy = st.builds(
    modelica_avm_Value,
)
DomainModelParameter_strategy = st.builds(
    DomainModelParameter,
)
avm_modelica_Redeclare_strategy = st.builds(
    avm_modelica_Redeclare,
    Type=
        safe_text,
    Locator=
        safe_text
)
avm_adamsCar_Parameter_strategy = st.builds(
    avm_adamsCar_Parameter,
    Name=
        safe_text,
    ID=
        safe_text
)
avm_manufacturing_Parameter_strategy = st.builds(
    avm_manufacturing_Parameter,
    Locator=
        safe_text,
    Name=
        safe_text
)
avm_cad_Parameter_strategy = st.builds(
    avm_cad_Parameter,
    Name=
        safe_text
)
avm_modelica_Parameter_strategy = st.builds(
    avm_modelica_Parameter,
    Locator=
        safe_text
)
DomainModelPort_strategy = st.builds(
    DomainModelPort,
)
avm_cad_Datum_strategy = st.builds(
    avm_cad_Datum,
    DatumName=
        safe_text
)
avm_modelica_Connector_strategy = st.builds(
    avm_modelica_Connector,
    Class=
        safe_text,
    Locator=
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
Connector_strategy = st.builds(
    Connector,
)
Parameter_strategy = st.builds(
    Parameter,
)
DomainModel__strategy = st.builds(
    DomainModel_,
)
avm_cyber_CyberModel_strategy = st.builds(
    avm_cyber_CyberModel,
    Class=
        safe_text,
    Locator=
        safe_text,
    Type=
        safe_text
)
avm_manufacturing_ManufacturingModel_strategy = st.builds(
    avm_manufacturing_ManufacturingModel,
)
avm_adamsCar_AdamsCarModel_strategy = st.builds(
    avm_adamsCar_AdamsCarModel,
)
avm_cad_CADModel_strategy = st.builds(
    avm_cad_CADModel,
)
avm_modelica_ModelicaModel_strategy = st.builds(
    avm_modelica_ModelicaModel,
    Class=
        safe_text
)
avm_WorkflowTaskBase_strategy = st.builds(
    avm_WorkflowTaskBase,
    Name=
        safe_text
)
avm_TestBenchValueBase_strategy = st.builds(
    avm_TestBenchValueBase,
    Name=
        safe_text,
    Notes=
        safe_text,
    YPosition=
        safe_text,
    ID=
        safe_text,
    XPosition=
        safe_text
)
avm_ContainerInstanceBase_strategy = st.builds(
    avm_ContainerInstanceBase,
    XPosition=
        safe_text,
    IDinSourceModel=
        safe_text,
    YPosition=
        safe_text
)
TestBenchValueBase_strategy = st.builds(
    TestBenchValueBase,
)
ContainerInstanceBase_strategy = st.builds(
    ContainerInstanceBase,
)
avm_Settings_strategy = st.builds(
    avm_Settings,
)
avm_Workflow_strategy = st.builds(
    avm_Workflow,
    Name=
        safe_text
)
WorkflowTaskBase_strategy = st.builds(
    WorkflowTaskBase,
)
avm_ExecutionTask_strategy = st.builds(
    avm_ExecutionTask,
    Description=
        safe_text,
    Invocation=
        safe_text
)
avm_InterpreterTask_strategy = st.builds(
    avm_InterpreterTask,
    Parameters=
        safe_text,
    COMName=
        safe_text
)
avm_TopLevelSystemUnderTest_strategy = st.builds(
    avm_TopLevelSystemUnderTest,
    DesignID=
        safe_text
)
avm_TestBench_strategy = st.builds(
    avm_TestBench,
    Name=
        safe_text
)
avm_Operand_strategy = st.builds(
    avm_Operand,
    Symbol=
        safe_text
)
Formula_strategy = st.builds(
    Formula,
)
avm_ComplexFormula_strategy = st.builds(
    avm_ComplexFormula,
    Expression=
        safe_text
)
avm_SimpleFormula_strategy = st.builds(
    avm_SimpleFormula,
    Operation=
        safe_text
)
avm_TestInjectionPoint_strategy = st.builds(
    avm_TestInjectionPoint,
)
avm_Metric_strategy = st.builds(
    avm_Metric,
)
avm_Parameter_strategy = st.builds(
    avm_Parameter,
)
avm_PortMapTarget_strategy = st.builds(
    avm_PortMapTarget,
    ID=
        safe_text
)
avm_ComponentPrimitivePropertyInstance_strategy = st.builds(
    avm_ComponentPrimitivePropertyInstance,
    IDinComponentModel=
        safe_text
)
DesignSpaceContainer_strategy = st.builds(
    DesignSpaceContainer,
)
avm_Alternative_strategy = st.builds(
    avm_Alternative,
)
avm_Optional_strategy = st.builds(
    avm_Optional,
)
Container_strategy = st.builds(
    Container,
)
avm_DesignSpaceContainer_strategy = st.builds(
    avm_DesignSpaceContainer,
)
avm_Compound_strategy = st.builds(
    avm_Compound,
)
avm_ConnectorCompositionTarget_strategy = st.builds(
    avm_ConnectorCompositionTarget,
    ID=
        safe_text
)
avm_DesignDomainFeature_strategy = st.builds(
    avm_DesignDomainFeature,
)
avm_Container_strategy = st.builds(
    avm_Container,
    Name=
        safe_text,
    YPosition=
        safe_text,
    XPosition=
        safe_text
)
avm_Design_strategy = st.builds(
    avm_Design,
    DesignSpaceSrcID=
        safe_text,
    SchemaVersion=
        safe_text,
    Name=
        safe_text,
    DesignID=
        safe_text
)
avm_ComponentInstance_strategy = st.builds(
    avm_ComponentInstance,
    YPosition=
        safe_text,
    XPosition=
        safe_text,
    ComponentID=
        safe_text,
    Name=
        safe_text,
    ID=
        safe_text,
    DesignSpaceSrcComponentID=
        safe_text
)
avm_DomainModelMetric_strategy = st.builds(
    avm_DomainModelMetric,
    XPosition=
        safe_text,
    ID=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text
)
DistributionRestriction_strategy = st.builds(
    DistributionRestriction,
)
avm_ITAR_strategy = st.builds(
    avm_ITAR,
)
avm_DoDDistributionStatement_strategy = st.builds(
    avm_DoDDistributionStatement,
    Type=
        safe_text
)
avm_Proprietary_strategy = st.builds(
    avm_Proprietary,
    Organization=
        safe_text
)
avm_SecurityClassification_strategy = st.builds(
    avm_SecurityClassification,
    Level=
        safe_text
)
ProbabilisticValue_strategy = st.builds(
    ProbabilisticValue,
)
avm_NormalDistribution_strategy = st.builds(
    avm_NormalDistribution,
)
Property_strategy = st.builds(
    Property,
)
avm_CompoundProperty_strategy = st.builds(
    avm_CompoundProperty,
)
avm_PrimitiveProperty_strategy = st.builds(
    avm_PrimitiveProperty,
)
avm_UniformDistribution_strategy = st.builds(
    avm_UniformDistribution,
)
avm_DomainModelParameter_strategy = st.builds(
    avm_DomainModelParameter,
    Notes=
        safe_text,
    YPosition=
        safe_text,
    XPosition=
        safe_text
)
Port_strategy = st.builds(
    Port,
)
avm_AbstractPort_strategy = st.builds(
    avm_AbstractPort,
)
avm_DomainModelPort_strategy = st.builds(
    avm_DomainModelPort,
)
PortMapTarget_strategy = st.builds(
    PortMapTarget,
)
avm_ComponentPortInstance_strategy = st.builds(
    avm_ComponentPortInstance,
    IDinComponentModel=
        safe_text
)
avm_ConnectorFeature_strategy = st.builds(
    avm_ConnectorFeature,
)
avm_assemblyDetail_strategy = st.builds(
    avm_assemblyDetail,
)
ConnectorCompositionTarget_strategy = st.builds(
    ConnectorCompositionTarget,
)
avm_ComponentConnectorInstance_strategy = st.builds(
    avm_ComponentConnectorInstance,
    IDinComponentModel=
        safe_text
)
avm_ValueNode_strategy = st.builds(
    avm_ValueNode,
    ID=
        safe_text
)
ValueExpressionType_strategy = st.builds(
    ValueExpressionType,
)
avm_DerivedValue_strategy = st.builds(
    avm_DerivedValue,
)
avm_ParametricValue_strategy = st.builds(
    avm_ParametricValue,
)
avm_CalculatedValue_strategy = st.builds(
    avm_CalculatedValue,
    Type=
        safe_text,
    Expression=
        safe_text
)
avm_ParametricEnumeratedValue_strategy = st.builds(
    avm_ParametricEnumeratedValue,
)
avm_ProbabilisticValue_strategy = st.builds(
    avm_ProbabilisticValue,
)
avm_FixedValue_strategy = st.builds(
    avm_FixedValue,
    Value=
        safe_text,
    Uncertainty=
        safe_text
)
avm_DataSource_strategy = st.builds(
    avm_DataSource,
    Notes=
        safe_text
)
avm_ValueExpressionType_strategy = st.builds(
    avm_ValueExpressionType,
)
ValueNode_strategy = st.builds(
    ValueNode,
)
avm_ValueFlowMux_strategy = st.builds(
    avm_ValueFlowMux,
)
avm_Value_strategy = st.builds(
    avm_Value,
    DataType=
        safe_text,
    Dimensions=
        safe_text,
    DimensionType=
        safe_text,
    Unit=
        safe_text
)
avm_AnalysisConstruct_strategy = st.builds(
    avm_AnalysisConstruct,
)
avm_Port_strategy = st.builds(
    avm_Port,
    Definition=
        safe_text,
    Notes=
        safe_text,
    YPosition=
        safe_text,
    Name=
        safe_text,
    XPosition=
        safe_text
)
avm_DistributionRestriction_strategy = st.builds(
    avm_DistributionRestriction,
    Notes=
        safe_text
)
avm_Connector_strategy = st.builds(
    avm_Connector,
    Definition=
        safe_text,
    XPosition=
        safe_text,
    YPosition=
        safe_text,
    Notes=
        safe_text,
    Name=
        safe_text
)
avm_Resource_strategy = st.builds(
    avm_Resource,
    ID=
        safe_text,
    XPosition=
        safe_text,
    YPosition=
        safe_text,
    Name=
        safe_text,
    Path=
        safe_text,
    Notes=
        safe_text,
    Hash=
        safe_text
)
avm_Property_strategy = st.builds(
    avm_Property,
    Definition=
        safe_text,
    YPosition=
        safe_text,
    Name=
        safe_text,
    Notes=
        safe_text,
    XPosition=
        safe_text,
    OnDataSheet=
        safe_text,
    ID=
        safe_text
)
avm_Formula_strategy = st.builds(
    avm_Formula,
    YPosition=
        safe_text,
    XPosition=
        safe_text,
    Name=
        safe_text
)
avm_DomainModel__strategy = st.builds(
    avm_DomainModel_,
    Name=
        safe_text,
    Notes=
        safe_text,
    Author=
        safe_text,
    XPosition=
        safe_text,
    YPosition=
        safe_text
)
avm_Component_strategy = st.builds(
    avm_Component,
    Classifications=
        safe_text,
    Name=
        safe_text,
    Version=
        safe_text,
    Supercedes=
        safe_text,
    ID=
        safe_text,
    SchemaVersion=
        safe_text
)

@given(instance=manufacturing_avm_Value_strategy)
@settings(max_examples=50)
def test_manufacturing_avm_value_instantiation(instance):
    assert isinstance(instance, manufacturing_avm_Value)

@given(instance=avm_adamsCar_FileReference_strategy)
@settings(max_examples=50)
def test_avm_adamscar_filereference_instantiation(instance):
    assert isinstance(instance, avm_adamsCar_FileReference)



@given(instance=avm_adamsCar_FileReference_strategy)
def test_avm_adamscar_filereference_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_adamsCar_FileReference_strategy)
def test_avm_adamscar_filereference_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_adamsCar_FileReference_strategy)
def test_avm_adamscar_filereference_FilePath_setter(instance):
    original = instance.FilePath
    instance.FilePath = original
    assert instance.FilePath == original

@given(instance=adamsCar_avm_Value_strategy)
@settings(max_examples=50)
def test_adamscar_avm_value_instantiation(instance):
    assert isinstance(instance, adamsCar_avm_Value)

@given(instance=FileReference_strategy)
@settings(max_examples=50)
def test_filereference_instantiation(instance):
    assert isinstance(instance, FileReference)

@given(instance=Axis_strategy)
@settings(max_examples=50)
def test_axis_instantiation(instance):
    assert isinstance(instance, Axis)

@given(instance=KinematicJointSpec_strategy)
@settings(max_examples=50)
def test_kinematicjointspec_instantiation(instance):
    assert isinstance(instance, KinematicJointSpec)

@given(instance=avm_cad_RevoluteJointSpec_strategy)
@settings(max_examples=50)
def test_avm_cad_revolutejointspec_instantiation(instance):
    assert isinstance(instance, avm_cad_RevoluteJointSpec)

@given(instance=cad_avm_ComponentInstance_strategy)
@settings(max_examples=50)
def test_cad_avm_componentinstance_instantiation(instance):
    assert isinstance(instance, cad_avm_ComponentInstance)

@given(instance=DesignDomainFeature_strategy)
@settings(max_examples=50)
def test_designdomainfeature_instantiation(instance):
    assert isinstance(instance, DesignDomainFeature)

@given(instance=avm_cad_AssemblyRoot_strategy)
@settings(max_examples=50)
def test_avm_cad_assemblyroot_instantiation(instance):
    assert isinstance(instance, avm_cad_AssemblyRoot)

@given(instance=ConnectorFeature_strategy)
@settings(max_examples=50)
def test_connectorfeature_instantiation(instance):
    assert isinstance(instance, ConnectorFeature)

@given(instance=avm_cad_KinematicJointSpec_strategy)
@settings(max_examples=50)
def test_avm_cad_kinematicjointspec_instantiation(instance):
    assert isinstance(instance, avm_cad_KinematicJointSpec)

@given(instance=avm_cad_GuideDatum_strategy)
@settings(max_examples=50)
def test_avm_cad_guidedatum_instantiation(instance):
    assert isinstance(instance, avm_cad_GuideDatum)

@given(instance=avm_cad_PlaneReference_strategy)
@settings(max_examples=50)
def test_avm_cad_planereference_instantiation(instance):
    assert isinstance(instance, avm_cad_PlaneReference)

@given(instance=PlaneReference_strategy)
@settings(max_examples=50)
def test_planereference_instantiation(instance):
    assert isinstance(instance, PlaneReference)

@given(instance=avm_cad_TranslationalJointSpec_strategy)
@settings(max_examples=50)
def test_avm_cad_translationaljointspec_instantiation(instance):
    assert isinstance(instance, avm_cad_TranslationalJointSpec)

@given(instance=avm_cad_CustomGeometryInput_strategy)
@settings(max_examples=50)
def test_avm_cad_customgeometryinput_instantiation(instance):
    assert isinstance(instance, avm_cad_CustomGeometryInput)



@given(instance=avm_cad_CustomGeometryInput_strategy)
def test_avm_cad_customgeometryinput_Operation_setter(instance):
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

@given(instance=avm_cad_Sphere_strategy)
@settings(max_examples=50)
def test_avm_cad_sphere_instantiation(instance):
    assert isinstance(instance, avm_cad_Sphere)

@given(instance=avm_cad_ExtrudedGeometry_strategy)
@settings(max_examples=50)
def test_avm_cad_extrudedgeometry_instantiation(instance):
    assert isinstance(instance, avm_cad_ExtrudedGeometry)

@given(instance=avm_cad_Surface_strategy)
@settings(max_examples=50)
def test_avm_cad_surface_instantiation(instance):
    assert isinstance(instance, avm_cad_Surface)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=avm_cad_PointReference_strategy)
@settings(max_examples=50)
def test_avm_cad_pointreference_instantiation(instance):
    assert isinstance(instance, avm_cad_PointReference)

@given(instance=AnalysisConstruct_strategy)
@settings(max_examples=50)
def test_analysisconstruct_instantiation(instance):
    assert isinstance(instance, AnalysisConstruct)

@given(instance=avm_cad_Geometry_strategy)
@settings(max_examples=50)
def test_avm_cad_geometry_instantiation(instance):
    assert isinstance(instance, avm_cad_Geometry)



@given(instance=avm_cad_Geometry_strategy)
def test_avm_cad_geometry_GeometryQualifier_setter(instance):
    original = instance.GeometryQualifier
    instance.GeometryQualifier = original
    assert instance.GeometryQualifier == original



@given(instance=avm_cad_Geometry_strategy)
def test_avm_cad_geometry_PartIntersectionModifier_setter(instance):
    original = instance.PartIntersectionModifier
    instance.PartIntersectionModifier = original
    assert instance.PartIntersectionModifier == original

@given(instance=Plane_strategy)
@settings(max_examples=50)
def test_plane_instantiation(instance):
    assert isinstance(instance, Plane)

@given(instance=cad_avm_Value_strategy)
@settings(max_examples=50)
def test_cad_avm_value_instantiation(instance):
    assert isinstance(instance, cad_avm_Value)

@given(instance=PointReference_strategy)
@settings(max_examples=50)
def test_pointreference_instantiation(instance):
    assert isinstance(instance, PointReference)

@given(instance=Geometry2D_strategy)
@settings(max_examples=50)
def test_geometry2d_instantiation(instance):
    assert isinstance(instance, Geometry2D)

@given(instance=avm_cad_Polygon_strategy)
@settings(max_examples=50)
def test_avm_cad_polygon_instantiation(instance):
    assert isinstance(instance, avm_cad_Polygon)

@given(instance=avm_cad_Circle_strategy)
@settings(max_examples=50)
def test_avm_cad_circle_instantiation(instance):
    assert isinstance(instance, avm_cad_Circle)

@given(instance=Geometry_strategy)
@settings(max_examples=50)
def test_geometry_instantiation(instance):
    assert isinstance(instance, Geometry)

@given(instance=avm_cad_Geometry3D_strategy)
@settings(max_examples=50)
def test_avm_cad_geometry3d_instantiation(instance):
    assert isinstance(instance, avm_cad_Geometry3D)

@given(instance=avm_cad_CustomGeometry_strategy)
@settings(max_examples=50)
def test_avm_cad_customgeometry_instantiation(instance):
    assert isinstance(instance, avm_cad_CustomGeometry)

@given(instance=avm_cad_Geometry2D_strategy)
@settings(max_examples=50)
def test_avm_cad_geometry2d_instantiation(instance):
    assert isinstance(instance, avm_cad_Geometry2D)

@given(instance=Datum_strategy)
@settings(max_examples=50)
def test_datum_instantiation(instance):
    assert isinstance(instance, Datum)

@given(instance=avm_cad_CoordinateSystem_strategy)
@settings(max_examples=50)
def test_avm_cad_coordinatesystem_instantiation(instance):
    assert isinstance(instance, avm_cad_CoordinateSystem)

@given(instance=avm_cad_Point_strategy)
@settings(max_examples=50)
def test_avm_cad_point_instantiation(instance):
    assert isinstance(instance, avm_cad_Point)

@given(instance=avm_cad_Axis_strategy)
@settings(max_examples=50)
def test_avm_cad_axis_instantiation(instance):
    assert isinstance(instance, avm_cad_Axis)

@given(instance=avm_cad_Plane_strategy)
@settings(max_examples=50)
def test_avm_cad_plane_instantiation(instance):
    assert isinstance(instance, avm_cad_Plane)

@given(instance=Settings_strategy)
@settings(max_examples=50)
def test_settings_instantiation(instance):
    assert isinstance(instance, Settings)

@given(instance=avm_modelica_SolverSettings_strategy)
@settings(max_examples=50)
def test_avm_modelica_solversettings_instantiation(instance):
    assert isinstance(instance, avm_modelica_SolverSettings)



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_JobManagerToolSelection_setter(instance):
    original = instance.JobManagerToolSelection
    instance.JobManagerToolSelection = original
    assert instance.JobManagerToolSelection == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_NumberOfIntervals_setter(instance):
    original = instance.NumberOfIntervals
    instance.NumberOfIntervals = original
    assert instance.NumberOfIntervals == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_ToolSpecificAnnotations_setter(instance):
    original = instance.ToolSpecificAnnotations
    instance.ToolSpecificAnnotations = original
    assert instance.ToolSpecificAnnotations == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_StartTime_setter(instance):
    original = instance.StartTime
    instance.StartTime = original
    assert instance.StartTime == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_IntervalLength_setter(instance):
    original = instance.IntervalLength
    instance.IntervalLength = original
    assert instance.IntervalLength == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_Solver_setter(instance):
    original = instance.Solver
    instance.Solver = original
    assert instance.Solver == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_IntervalMethod_setter(instance):
    original = instance.IntervalMethod
    instance.IntervalMethod = original
    assert instance.IntervalMethod == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_Tolerance_setter(instance):
    original = instance.Tolerance
    instance.Tolerance = original
    assert instance.Tolerance == original



@given(instance=avm_modelica_SolverSettings_strategy)
def test_avm_modelica_solversettings_StopTime_setter(instance):
    original = instance.StopTime
    instance.StopTime = original
    assert instance.StopTime == original

@given(instance=avm_modelica_Limit_strategy)
@settings(max_examples=50)
def test_avm_modelica_limit_instantiation(instance):
    assert isinstance(instance, avm_modelica_Limit)



@given(instance=avm_modelica_Limit_strategy)
def test_avm_modelica_limit_BoundType_setter(instance):
    original = instance.BoundType
    instance.BoundType = original
    assert instance.BoundType == original



@given(instance=avm_modelica_Limit_strategy)
def test_avm_modelica_limit_VariableLocator_setter(instance):
    original = instance.VariableLocator
    instance.VariableLocator = original
    assert instance.VariableLocator == original



@given(instance=avm_modelica_Limit_strategy)
def test_avm_modelica_limit_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_modelica_Limit_strategy)
def test_avm_modelica_limit_ToleranceTimeWindow_setter(instance):
    original = instance.ToleranceTimeWindow
    instance.ToleranceTimeWindow = original
    assert instance.ToleranceTimeWindow == original



@given(instance=avm_modelica_Limit_strategy)
def test_avm_modelica_limit_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=DomainModelMetric_strategy)
@settings(max_examples=50)
def test_domainmodelmetric_instantiation(instance):
    assert isinstance(instance, DomainModelMetric)

@given(instance=avm_manufacturing_Metric_strategy)
@settings(max_examples=50)
def test_avm_manufacturing_metric_instantiation(instance):
    assert isinstance(instance, avm_manufacturing_Metric)



@given(instance=avm_manufacturing_Metric_strategy)
def test_avm_manufacturing_metric_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_cad_Metric_strategy)
@settings(max_examples=50)
def test_avm_cad_metric_instantiation(instance):
    assert isinstance(instance, avm_cad_Metric)



@given(instance=avm_cad_Metric_strategy)
def test_avm_cad_metric_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_modelica_Metric_strategy)
@settings(max_examples=50)
def test_avm_modelica_metric_instantiation(instance):
    assert isinstance(instance, avm_modelica_Metric)



@given(instance=avm_modelica_Metric_strategy)
def test_avm_modelica_metric_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=modelica_avm_Value_strategy)
@settings(max_examples=50)
def test_modelica_avm_value_instantiation(instance):
    assert isinstance(instance, modelica_avm_Value)

@given(instance=DomainModelParameter_strategy)
@settings(max_examples=50)
def test_domainmodelparameter_instantiation(instance):
    assert isinstance(instance, DomainModelParameter)

@given(instance=avm_modelica_Redeclare_strategy)
@settings(max_examples=50)
def test_avm_modelica_redeclare_instantiation(instance):
    assert isinstance(instance, avm_modelica_Redeclare)



@given(instance=avm_modelica_Redeclare_strategy)
def test_avm_modelica_redeclare_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=avm_modelica_Redeclare_strategy)
def test_avm_modelica_redeclare_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=avm_adamsCar_Parameter_strategy)
@settings(max_examples=50)
def test_avm_adamscar_parameter_instantiation(instance):
    assert isinstance(instance, avm_adamsCar_Parameter)



@given(instance=avm_adamsCar_Parameter_strategy)
def test_avm_adamscar_parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_adamsCar_Parameter_strategy)
def test_avm_adamscar_parameter_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm_manufacturing_Parameter_strategy)
@settings(max_examples=50)
def test_avm_manufacturing_parameter_instantiation(instance):
    assert isinstance(instance, avm_manufacturing_Parameter)



@given(instance=avm_manufacturing_Parameter_strategy)
def test_avm_manufacturing_parameter_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original



@given(instance=avm_manufacturing_Parameter_strategy)
def test_avm_manufacturing_parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_cad_Parameter_strategy)
@settings(max_examples=50)
def test_avm_cad_parameter_instantiation(instance):
    assert isinstance(instance, avm_cad_Parameter)



@given(instance=avm_cad_Parameter_strategy)
def test_avm_cad_parameter_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_modelica_Parameter_strategy)
@settings(max_examples=50)
def test_avm_modelica_parameter_instantiation(instance):
    assert isinstance(instance, avm_modelica_Parameter)



@given(instance=avm_modelica_Parameter_strategy)
def test_avm_modelica_parameter_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

@given(instance=DomainModelPort_strategy)
@settings(max_examples=50)
def test_domainmodelport_instantiation(instance):
    assert isinstance(instance, DomainModelPort)

@given(instance=avm_cad_Datum_strategy)
@settings(max_examples=50)
def test_avm_cad_datum_instantiation(instance):
    assert isinstance(instance, avm_cad_Datum)



@given(instance=avm_cad_Datum_strategy)
def test_avm_cad_datum_DatumName_setter(instance):
    original = instance.DatumName
    instance.DatumName = original
    assert instance.DatumName == original

@given(instance=avm_modelica_Connector_strategy)
@settings(max_examples=50)
def test_avm_modelica_connector_instantiation(instance):
    assert isinstance(instance, avm_modelica_Connector)



@given(instance=avm_modelica_Connector_strategy)
def test_avm_modelica_connector_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original



@given(instance=avm_modelica_Connector_strategy)
def test_avm_modelica_connector_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original

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

@given(instance=avm_cyber_CyberModel_strategy)
@settings(max_examples=50)
def test_avm_cyber_cybermodel_instantiation(instance):
    assert isinstance(instance, avm_cyber_CyberModel)



@given(instance=avm_cyber_CyberModel_strategy)
def test_avm_cyber_cybermodel_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original



@given(instance=avm_cyber_CyberModel_strategy)
def test_avm_cyber_cybermodel_Locator_setter(instance):
    original = instance.Locator
    instance.Locator = original
    assert instance.Locator == original



@given(instance=avm_cyber_CyberModel_strategy)
def test_avm_cyber_cybermodel_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm_manufacturing_ManufacturingModel_strategy)
@settings(max_examples=50)
def test_avm_manufacturing_manufacturingmodel_instantiation(instance):
    assert isinstance(instance, avm_manufacturing_ManufacturingModel)

@given(instance=avm_adamsCar_AdamsCarModel_strategy)
@settings(max_examples=50)
def test_avm_adamscar_adamscarmodel_instantiation(instance):
    assert isinstance(instance, avm_adamsCar_AdamsCarModel)

@given(instance=avm_cad_CADModel_strategy)
@settings(max_examples=50)
def test_avm_cad_cadmodel_instantiation(instance):
    assert isinstance(instance, avm_cad_CADModel)

@given(instance=avm_modelica_ModelicaModel_strategy)
@settings(max_examples=50)
def test_avm_modelica_modelicamodel_instantiation(instance):
    assert isinstance(instance, avm_modelica_ModelicaModel)



@given(instance=avm_modelica_ModelicaModel_strategy)
def test_avm_modelica_modelicamodel_Class_setter(instance):
    original = instance.Class
    instance.Class = original
    assert instance.Class == original

@given(instance=avm_WorkflowTaskBase_strategy)
@settings(max_examples=50)
def test_avm_workflowtaskbase_instantiation(instance):
    assert isinstance(instance, avm_WorkflowTaskBase)



@given(instance=avm_WorkflowTaskBase_strategy)
def test_avm_workflowtaskbase_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_TestBenchValueBase_strategy)
@settings(max_examples=50)
def test_avm_testbenchvaluebase_instantiation(instance):
    assert isinstance(instance, avm_TestBenchValueBase)



@given(instance=avm_TestBenchValueBase_strategy)
def test_avm_testbenchvaluebase_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_TestBenchValueBase_strategy)
def test_avm_testbenchvaluebase_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_TestBenchValueBase_strategy)
def test_avm_testbenchvaluebase_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_TestBenchValueBase_strategy)
def test_avm_testbenchvaluebase_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_TestBenchValueBase_strategy)
def test_avm_testbenchvaluebase_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm_ContainerInstanceBase_strategy)
@settings(max_examples=50)
def test_avm_containerinstancebase_instantiation(instance):
    assert isinstance(instance, avm_ContainerInstanceBase)



@given(instance=avm_ContainerInstanceBase_strategy)
def test_avm_containerinstancebase_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_ContainerInstanceBase_strategy)
def test_avm_containerinstancebase_IDinSourceModel_setter(instance):
    original = instance.IDinSourceModel
    instance.IDinSourceModel = original
    assert instance.IDinSourceModel == original



@given(instance=avm_ContainerInstanceBase_strategy)
def test_avm_containerinstancebase_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=TestBenchValueBase_strategy)
@settings(max_examples=50)
def test_testbenchvaluebase_instantiation(instance):
    assert isinstance(instance, TestBenchValueBase)

@given(instance=ContainerInstanceBase_strategy)
@settings(max_examples=50)
def test_containerinstancebase_instantiation(instance):
    assert isinstance(instance, ContainerInstanceBase)

@given(instance=avm_Settings_strategy)
@settings(max_examples=50)
def test_avm_settings_instantiation(instance):
    assert isinstance(instance, avm_Settings)

@given(instance=avm_Workflow_strategy)
@settings(max_examples=50)
def test_avm_workflow_instantiation(instance):
    assert isinstance(instance, avm_Workflow)



@given(instance=avm_Workflow_strategy)
def test_avm_workflow_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=WorkflowTaskBase_strategy)
@settings(max_examples=50)
def test_workflowtaskbase_instantiation(instance):
    assert isinstance(instance, WorkflowTaskBase)

@given(instance=avm_ExecutionTask_strategy)
@settings(max_examples=50)
def test_avm_executiontask_instantiation(instance):
    assert isinstance(instance, avm_ExecutionTask)



@given(instance=avm_ExecutionTask_strategy)
def test_avm_executiontask_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original



@given(instance=avm_ExecutionTask_strategy)
def test_avm_executiontask_Invocation_setter(instance):
    original = instance.Invocation
    instance.Invocation = original
    assert instance.Invocation == original

@given(instance=avm_InterpreterTask_strategy)
@settings(max_examples=50)
def test_avm_interpretertask_instantiation(instance):
    assert isinstance(instance, avm_InterpreterTask)



@given(instance=avm_InterpreterTask_strategy)
def test_avm_interpretertask_Parameters_setter(instance):
    original = instance.Parameters
    instance.Parameters = original
    assert instance.Parameters == original



@given(instance=avm_InterpreterTask_strategy)
def test_avm_interpretertask_COMName_setter(instance):
    original = instance.COMName
    instance.COMName = original
    assert instance.COMName == original

@given(instance=avm_TopLevelSystemUnderTest_strategy)
@settings(max_examples=50)
def test_avm_toplevelsystemundertest_instantiation(instance):
    assert isinstance(instance, avm_TopLevelSystemUnderTest)



@given(instance=avm_TopLevelSystemUnderTest_strategy)
def test_avm_toplevelsystemundertest_DesignID_setter(instance):
    original = instance.DesignID
    instance.DesignID = original
    assert instance.DesignID == original

@given(instance=avm_TestBench_strategy)
@settings(max_examples=50)
def test_avm_testbench_instantiation(instance):
    assert isinstance(instance, avm_TestBench)



@given(instance=avm_TestBench_strategy)
def test_avm_testbench_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_Operand_strategy)
@settings(max_examples=50)
def test_avm_operand_instantiation(instance):
    assert isinstance(instance, avm_Operand)



@given(instance=avm_Operand_strategy)
def test_avm_operand_Symbol_setter(instance):
    original = instance.Symbol
    instance.Symbol = original
    assert instance.Symbol == original

@given(instance=Formula_strategy)
@settings(max_examples=50)
def test_formula_instantiation(instance):
    assert isinstance(instance, Formula)

@given(instance=avm_ComplexFormula_strategy)
@settings(max_examples=50)
def test_avm_complexformula_instantiation(instance):
    assert isinstance(instance, avm_ComplexFormula)



@given(instance=avm_ComplexFormula_strategy)
def test_avm_complexformula_Expression_setter(instance):
    original = instance.Expression
    instance.Expression = original
    assert instance.Expression == original

@given(instance=avm_SimpleFormula_strategy)
@settings(max_examples=50)
def test_avm_simpleformula_instantiation(instance):
    assert isinstance(instance, avm_SimpleFormula)



@given(instance=avm_SimpleFormula_strategy)
def test_avm_simpleformula_Operation_setter(instance):
    original = instance.Operation
    instance.Operation = original
    assert instance.Operation == original

@given(instance=avm_TestInjectionPoint_strategy)
@settings(max_examples=50)
def test_avm_testinjectionpoint_instantiation(instance):
    assert isinstance(instance, avm_TestInjectionPoint)

@given(instance=avm_Metric_strategy)
@settings(max_examples=50)
def test_avm_metric_instantiation(instance):
    assert isinstance(instance, avm_Metric)

@given(instance=avm_Parameter_strategy)
@settings(max_examples=50)
def test_avm_parameter_instantiation(instance):
    assert isinstance(instance, avm_Parameter)

@given(instance=avm_PortMapTarget_strategy)
@settings(max_examples=50)
def test_avm_portmaptarget_instantiation(instance):
    assert isinstance(instance, avm_PortMapTarget)



@given(instance=avm_PortMapTarget_strategy)
def test_avm_portmaptarget_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm_ComponentPrimitivePropertyInstance_strategy)
@settings(max_examples=50)
def test_avm_componentprimitivepropertyinstance_instantiation(instance):
    assert isinstance(instance, avm_ComponentPrimitivePropertyInstance)



@given(instance=avm_ComponentPrimitivePropertyInstance_strategy)
def test_avm_componentprimitivepropertyinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=DesignSpaceContainer_strategy)
@settings(max_examples=50)
def test_designspacecontainer_instantiation(instance):
    assert isinstance(instance, DesignSpaceContainer)

@given(instance=avm_Alternative_strategy)
@settings(max_examples=50)
def test_avm_alternative_instantiation(instance):
    assert isinstance(instance, avm_Alternative)

@given(instance=avm_Optional_strategy)
@settings(max_examples=50)
def test_avm_optional_instantiation(instance):
    assert isinstance(instance, avm_Optional)

@given(instance=Container_strategy)
@settings(max_examples=50)
def test_container_instantiation(instance):
    assert isinstance(instance, Container)

@given(instance=avm_DesignSpaceContainer_strategy)
@settings(max_examples=50)
def test_avm_designspacecontainer_instantiation(instance):
    assert isinstance(instance, avm_DesignSpaceContainer)

@given(instance=avm_Compound_strategy)
@settings(max_examples=50)
def test_avm_compound_instantiation(instance):
    assert isinstance(instance, avm_Compound)

@given(instance=avm_ConnectorCompositionTarget_strategy)
@settings(max_examples=50)
def test_avm_connectorcompositiontarget_instantiation(instance):
    assert isinstance(instance, avm_ConnectorCompositionTarget)



@given(instance=avm_ConnectorCompositionTarget_strategy)
def test_avm_connectorcompositiontarget_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm_DesignDomainFeature_strategy)
@settings(max_examples=50)
def test_avm_designdomainfeature_instantiation(instance):
    assert isinstance(instance, avm_DesignDomainFeature)

@given(instance=avm_Container_strategy)
@settings(max_examples=50)
def test_avm_container_instantiation(instance):
    assert isinstance(instance, avm_Container)



@given(instance=avm_Container_strategy)
def test_avm_container_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Container_strategy)
def test_avm_container_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Container_strategy)
def test_avm_container_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm_Design_strategy)
@settings(max_examples=50)
def test_avm_design_instantiation(instance):
    assert isinstance(instance, avm_Design)



@given(instance=avm_Design_strategy)
def test_avm_design_DesignSpaceSrcID_setter(instance):
    original = instance.DesignSpaceSrcID
    instance.DesignSpaceSrcID = original
    assert instance.DesignSpaceSrcID == original



@given(instance=avm_Design_strategy)
def test_avm_design_SchemaVersion_setter(instance):
    original = instance.SchemaVersion
    instance.SchemaVersion = original
    assert instance.SchemaVersion == original



@given(instance=avm_Design_strategy)
def test_avm_design_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Design_strategy)
def test_avm_design_DesignID_setter(instance):
    original = instance.DesignID
    instance.DesignID = original
    assert instance.DesignID == original

@given(instance=avm_ComponentInstance_strategy)
@settings(max_examples=50)
def test_avm_componentinstance_instantiation(instance):
    assert isinstance(instance, avm_ComponentInstance)



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_ComponentID_setter(instance):
    original = instance.ComponentID
    instance.ComponentID = original
    assert instance.ComponentID == original



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_ComponentInstance_strategy)
def test_avm_componentinstance_DesignSpaceSrcComponentID_setter(instance):
    original = instance.DesignSpaceSrcComponentID
    instance.DesignSpaceSrcComponentID = original
    assert instance.DesignSpaceSrcComponentID == original

@given(instance=avm_DomainModelMetric_strategy)
@settings(max_examples=50)
def test_avm_domainmodelmetric_instantiation(instance):
    assert isinstance(instance, avm_DomainModelMetric)



@given(instance=avm_DomainModelMetric_strategy)
def test_avm_domainmodelmetric_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_DomainModelMetric_strategy)
def test_avm_domainmodelmetric_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_DomainModelMetric_strategy)
def test_avm_domainmodelmetric_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_DomainModelMetric_strategy)
def test_avm_domainmodelmetric_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=DistributionRestriction_strategy)
@settings(max_examples=50)
def test_distributionrestriction_instantiation(instance):
    assert isinstance(instance, DistributionRestriction)

@given(instance=avm_ITAR_strategy)
@settings(max_examples=50)
def test_avm_itar_instantiation(instance):
    assert isinstance(instance, avm_ITAR)

@given(instance=avm_DoDDistributionStatement_strategy)
@settings(max_examples=50)
def test_avm_doddistributionstatement_instantiation(instance):
    assert isinstance(instance, avm_DoDDistributionStatement)



@given(instance=avm_DoDDistributionStatement_strategy)
def test_avm_doddistributionstatement_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=avm_Proprietary_strategy)
@settings(max_examples=50)
def test_avm_proprietary_instantiation(instance):
    assert isinstance(instance, avm_Proprietary)



@given(instance=avm_Proprietary_strategy)
def test_avm_proprietary_Organization_setter(instance):
    original = instance.Organization
    instance.Organization = original
    assert instance.Organization == original

@given(instance=avm_SecurityClassification_strategy)
@settings(max_examples=50)
def test_avm_securityclassification_instantiation(instance):
    assert isinstance(instance, avm_SecurityClassification)



@given(instance=avm_SecurityClassification_strategy)
def test_avm_securityclassification_Level_setter(instance):
    original = instance.Level
    instance.Level = original
    assert instance.Level == original

@given(instance=ProbabilisticValue_strategy)
@settings(max_examples=50)
def test_probabilisticvalue_instantiation(instance):
    assert isinstance(instance, ProbabilisticValue)

@given(instance=avm_NormalDistribution_strategy)
@settings(max_examples=50)
def test_avm_normaldistribution_instantiation(instance):
    assert isinstance(instance, avm_NormalDistribution)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=avm_CompoundProperty_strategy)
@settings(max_examples=50)
def test_avm_compoundproperty_instantiation(instance):
    assert isinstance(instance, avm_CompoundProperty)

@given(instance=avm_PrimitiveProperty_strategy)
@settings(max_examples=50)
def test_avm_primitiveproperty_instantiation(instance):
    assert isinstance(instance, avm_PrimitiveProperty)

@given(instance=avm_UniformDistribution_strategy)
@settings(max_examples=50)
def test_avm_uniformdistribution_instantiation(instance):
    assert isinstance(instance, avm_UniformDistribution)

@given(instance=avm_DomainModelParameter_strategy)
@settings(max_examples=50)
def test_avm_domainmodelparameter_instantiation(instance):
    assert isinstance(instance, avm_DomainModelParameter)



@given(instance=avm_DomainModelParameter_strategy)
def test_avm_domainmodelparameter_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_DomainModelParameter_strategy)
def test_avm_domainmodelparameter_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_DomainModelParameter_strategy)
def test_avm_domainmodelparameter_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=avm_AbstractPort_strategy)
@settings(max_examples=50)
def test_avm_abstractport_instantiation(instance):
    assert isinstance(instance, avm_AbstractPort)

@given(instance=avm_DomainModelPort_strategy)
@settings(max_examples=50)
def test_avm_domainmodelport_instantiation(instance):
    assert isinstance(instance, avm_DomainModelPort)

@given(instance=PortMapTarget_strategy)
@settings(max_examples=50)
def test_portmaptarget_instantiation(instance):
    assert isinstance(instance, PortMapTarget)

@given(instance=avm_ComponentPortInstance_strategy)
@settings(max_examples=50)
def test_avm_componentportinstance_instantiation(instance):
    assert isinstance(instance, avm_ComponentPortInstance)



@given(instance=avm_ComponentPortInstance_strategy)
def test_avm_componentportinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=avm_ConnectorFeature_strategy)
@settings(max_examples=50)
def test_avm_connectorfeature_instantiation(instance):
    assert isinstance(instance, avm_ConnectorFeature)

@given(instance=avm_assemblyDetail_strategy)
@settings(max_examples=50)
def test_avm_assemblydetail_instantiation(instance):
    assert isinstance(instance, avm_assemblyDetail)

@given(instance=ConnectorCompositionTarget_strategy)
@settings(max_examples=50)
def test_connectorcompositiontarget_instantiation(instance):
    assert isinstance(instance, ConnectorCompositionTarget)

@given(instance=avm_ComponentConnectorInstance_strategy)
@settings(max_examples=50)
def test_avm_componentconnectorinstance_instantiation(instance):
    assert isinstance(instance, avm_ComponentConnectorInstance)



@given(instance=avm_ComponentConnectorInstance_strategy)
def test_avm_componentconnectorinstance_IDinComponentModel_setter(instance):
    original = instance.IDinComponentModel
    instance.IDinComponentModel = original
    assert instance.IDinComponentModel == original

@given(instance=avm_ValueNode_strategy)
@settings(max_examples=50)
def test_avm_valuenode_instantiation(instance):
    assert isinstance(instance, avm_ValueNode)



@given(instance=avm_ValueNode_strategy)
def test_avm_valuenode_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=ValueExpressionType_strategy)
@settings(max_examples=50)
def test_valueexpressiontype_instantiation(instance):
    assert isinstance(instance, ValueExpressionType)

@given(instance=avm_DerivedValue_strategy)
@settings(max_examples=50)
def test_avm_derivedvalue_instantiation(instance):
    assert isinstance(instance, avm_DerivedValue)

@given(instance=avm_ParametricValue_strategy)
@settings(max_examples=50)
def test_avm_parametricvalue_instantiation(instance):
    assert isinstance(instance, avm_ParametricValue)

@given(instance=avm_CalculatedValue_strategy)
@settings(max_examples=50)
def test_avm_calculatedvalue_instantiation(instance):
    assert isinstance(instance, avm_CalculatedValue)



@given(instance=avm_CalculatedValue_strategy)
def test_avm_calculatedvalue_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=avm_CalculatedValue_strategy)
def test_avm_calculatedvalue_Expression_setter(instance):
    original = instance.Expression
    instance.Expression = original
    assert instance.Expression == original

@given(instance=avm_ParametricEnumeratedValue_strategy)
@settings(max_examples=50)
def test_avm_parametricenumeratedvalue_instantiation(instance):
    assert isinstance(instance, avm_ParametricEnumeratedValue)

@given(instance=avm_ProbabilisticValue_strategy)
@settings(max_examples=50)
def test_avm_probabilisticvalue_instantiation(instance):
    assert isinstance(instance, avm_ProbabilisticValue)

@given(instance=avm_FixedValue_strategy)
@settings(max_examples=50)
def test_avm_fixedvalue_instantiation(instance):
    assert isinstance(instance, avm_FixedValue)



@given(instance=avm_FixedValue_strategy)
def test_avm_fixedvalue_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original



@given(instance=avm_FixedValue_strategy)
def test_avm_fixedvalue_Uncertainty_setter(instance):
    original = instance.Uncertainty
    instance.Uncertainty = original
    assert instance.Uncertainty == original

@given(instance=avm_DataSource_strategy)
@settings(max_examples=50)
def test_avm_datasource_instantiation(instance):
    assert isinstance(instance, avm_DataSource)



@given(instance=avm_DataSource_strategy)
def test_avm_datasource_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm_ValueExpressionType_strategy)
@settings(max_examples=50)
def test_avm_valueexpressiontype_instantiation(instance):
    assert isinstance(instance, avm_ValueExpressionType)

@given(instance=ValueNode_strategy)
@settings(max_examples=50)
def test_valuenode_instantiation(instance):
    assert isinstance(instance, ValueNode)

@given(instance=avm_ValueFlowMux_strategy)
@settings(max_examples=50)
def test_avm_valueflowmux_instantiation(instance):
    assert isinstance(instance, avm_ValueFlowMux)

@given(instance=avm_Value_strategy)
@settings(max_examples=50)
def test_avm_value_instantiation(instance):
    assert isinstance(instance, avm_Value)



@given(instance=avm_Value_strategy)
def test_avm_value_DataType_setter(instance):
    original = instance.DataType
    instance.DataType = original
    assert instance.DataType == original



@given(instance=avm_Value_strategy)
def test_avm_value_Dimensions_setter(instance):
    original = instance.Dimensions
    instance.Dimensions = original
    assert instance.Dimensions == original



@given(instance=avm_Value_strategy)
def test_avm_value_DimensionType_setter(instance):
    original = instance.DimensionType
    instance.DimensionType = original
    assert instance.DimensionType == original



@given(instance=avm_Value_strategy)
def test_avm_value_Unit_setter(instance):
    original = instance.Unit
    instance.Unit = original
    assert instance.Unit == original

@given(instance=avm_AnalysisConstruct_strategy)
@settings(max_examples=50)
def test_avm_analysisconstruct_instantiation(instance):
    assert isinstance(instance, avm_AnalysisConstruct)

@given(instance=avm_Port_strategy)
@settings(max_examples=50)
def test_avm_port_instantiation(instance):
    assert isinstance(instance, avm_Port)



@given(instance=avm_Port_strategy)
def test_avm_port_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original



@given(instance=avm_Port_strategy)
def test_avm_port_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_Port_strategy)
def test_avm_port_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Port_strategy)
def test_avm_port_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Port_strategy)
def test_avm_port_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original

@given(instance=avm_DistributionRestriction_strategy)
@settings(max_examples=50)
def test_avm_distributionrestriction_instantiation(instance):
    assert isinstance(instance, avm_DistributionRestriction)



@given(instance=avm_DistributionRestriction_strategy)
def test_avm_distributionrestriction_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original

@given(instance=avm_Connector_strategy)
@settings(max_examples=50)
def test_avm_connector_instantiation(instance):
    assert isinstance(instance, avm_Connector)



@given(instance=avm_Connector_strategy)
def test_avm_connector_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original



@given(instance=avm_Connector_strategy)
def test_avm_connector_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_Connector_strategy)
def test_avm_connector_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Connector_strategy)
def test_avm_connector_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_Connector_strategy)
def test_avm_connector_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_Resource_strategy)
@settings(max_examples=50)
def test_avm_resource_instantiation(instance):
    assert isinstance(instance, avm_Resource)



@given(instance=avm_Resource_strategy)
def test_avm_resource_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_Path_setter(instance):
    original = instance.Path
    instance.Path = original
    assert instance.Path == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_Resource_strategy)
def test_avm_resource_Hash_setter(instance):
    original = instance.Hash
    instance.Hash = original
    assert instance.Hash == original

@given(instance=avm_Property_strategy)
@settings(max_examples=50)
def test_avm_property_instantiation(instance):
    assert isinstance(instance, avm_Property)



@given(instance=avm_Property_strategy)
def test_avm_property_Definition_setter(instance):
    original = instance.Definition
    instance.Definition = original
    assert instance.Definition == original



@given(instance=avm_Property_strategy)
def test_avm_property_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Property_strategy)
def test_avm_property_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Property_strategy)
def test_avm_property_Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_Property_strategy)
def test_avm_property_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_Property_strategy)
def test_avm_property_OnDataSheet_setter(instance):
    original = instance.OnDataSheet
    instance.OnDataSheet = original
    assert instance.OnDataSheet == original



@given(instance=avm_Property_strategy)
def test_avm_property_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=avm_Formula_strategy)
@settings(max_examples=50)
def test_avm_formula_instantiation(instance):
    assert isinstance(instance, avm_Formula)



@given(instance=avm_Formula_strategy)
def test_avm_formula_YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original



@given(instance=avm_Formula_strategy)
def test_avm_formula_XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_Formula_strategy)
def test_avm_formula_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=avm_DomainModel__strategy)
@settings(max_examples=50)
def test_avm_domainmodel__instantiation(instance):
    assert isinstance(instance, avm_DomainModel_)



@given(instance=avm_DomainModel__strategy)
def test_avm_domainmodel__Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_DomainModel__strategy)
def test_avm_domainmodel__Notes_setter(instance):
    original = instance.Notes
    instance.Notes = original
    assert instance.Notes == original



@given(instance=avm_DomainModel__strategy)
def test_avm_domainmodel__Author_setter(instance):
    original = instance.Author
    instance.Author = original
    assert instance.Author == original



@given(instance=avm_DomainModel__strategy)
def test_avm_domainmodel__XPosition_setter(instance):
    original = instance.XPosition
    instance.XPosition = original
    assert instance.XPosition == original



@given(instance=avm_DomainModel__strategy)
def test_avm_domainmodel__YPosition_setter(instance):
    original = instance.YPosition
    instance.YPosition = original
    assert instance.YPosition == original

@given(instance=avm_Component_strategy)
@settings(max_examples=50)
def test_avm_component_instantiation(instance):
    assert isinstance(instance, avm_Component)



@given(instance=avm_Component_strategy)
def test_avm_component_Classifications_setter(instance):
    original = instance.Classifications
    instance.Classifications = original
    assert instance.Classifications == original



@given(instance=avm_Component_strategy)
def test_avm_component_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=avm_Component_strategy)
def test_avm_component_Version_setter(instance):
    original = instance.Version
    instance.Version = original
    assert instance.Version == original



@given(instance=avm_Component_strategy)
def test_avm_component_Supercedes_setter(instance):
    original = instance.Supercedes
    instance.Supercedes = original
    assert instance.Supercedes == original



@given(instance=avm_Component_strategy)
def test_avm_component_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=avm_Component_strategy)
def test_avm_component_SchemaVersion_setter(instance):
    original = instance.SchemaVersion
    instance.SchemaVersion = original
    assert instance.SchemaVersion == original
