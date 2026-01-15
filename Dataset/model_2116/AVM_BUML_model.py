####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
CalculationTypeEnum: Enumeration = Enumeration(
    name="CalculationTypeEnum",
    literals={
            EnumerationLiteral(name="Declarative"),
			EnumerationLiteral(name="Python")
    }
)

DataTypeEnum: Enumeration = Enumeration(
    name="DataTypeEnum",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real")
    }
)

DimensionTypeEnum: Enumeration = Enumeration(
    name="DimensionTypeEnum",
    literals={
            EnumerationLiteral(name="Matrix"),
			EnumerationLiteral(name="Vector"),
			EnumerationLiteral(name="Scalar")
    }
)

SimpleFormulaOperation: Enumeration = Enumeration(
    name="SimpleFormulaOperation",
    literals={
            EnumerationLiteral(name="Addition"),
			EnumerationLiteral(name="Multiplication"),
			EnumerationLiteral(name="ArithmeticMean"),
			EnumerationLiteral(name="GeometricMean"),
			EnumerationLiteral(name="Maximum"),
			EnumerationLiteral(name="Minimum")
    }
)

DoDDistributionStatementEnum: Enumeration = Enumeration(
    name="DoDDistributionStatementEnum",
    literals={
            EnumerationLiteral(name="StatementA"),
			EnumerationLiteral(name="StatementB"),
			EnumerationLiteral(name="StatementC"),
			EnumerationLiteral(name="StatementD"),
			EnumerationLiteral(name="StatementE")
    }
)

RedeclareTypeEnum: Enumeration = Enumeration(
    name="RedeclareTypeEnum",
    literals={
            EnumerationLiteral(name="Package"),
			EnumerationLiteral(name="Class"),
			EnumerationLiteral(name="Model"),
			EnumerationLiteral(name="Record"),
			EnumerationLiteral(name="Block"),
			EnumerationLiteral(name="Connector"),
			EnumerationLiteral(name="Function")
    }
)

IntervalMethod: Enumeration = Enumeration(
    name="IntervalMethod",
    literals={
            EnumerationLiteral(name="NumberOfIntervals"),
			EnumerationLiteral(name="IntervalLength")
    }
)

JobManagerToolSelection: Enumeration = Enumeration(
    name="JobManagerToolSelection",
    literals={
            EnumerationLiteral(name="Dymola_latest"),
			EnumerationLiteral(name="Dymola_2014"),
			EnumerationLiteral(name="Dymola_2013"),
			EnumerationLiteral(name="OpenModelica_latest"),
			EnumerationLiteral(name="JModelica_1_12")
    }
)

BoundTypeEnum: Enumeration = Enumeration(
    name="BoundTypeEnum",
    literals={
            EnumerationLiteral(name="MustNotExceed"),
			EnumerationLiteral(name="MustNotMeetOrExceed"),
			EnumerationLiteral(name="MustExceed"),
			EnumerationLiteral(name="MustExceedOrEqual")
    }
)

CustomGeometryInputOperationEnum: Enumeration = Enumeration(
    name="CustomGeometryInputOperationEnum",
    literals={
            EnumerationLiteral(name="Union"),
			EnumerationLiteral(name="Intersection"),
			EnumerationLiteral(name="Subtraction")
    }
)

PartIntersectionEnum: Enumeration = Enumeration(
    name="PartIntersectionEnum",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="IntersectionWithAnyParts"),
			EnumerationLiteral(name="IntersectionWithReferencedParts")
    }
)

GeometryQualifierEnum: Enumeration = Enumeration(
    name="GeometryQualifierEnum",
    literals={
            EnumerationLiteral(name="InteriorAndBoundary"),
			EnumerationLiteral(name="InteriorOnly"),
			EnumerationLiteral(name="BoundaryOnly")
    }
)

ModelType: Enumeration = Enumeration(
    name="ModelType",
    literals={
            EnumerationLiteral(name="SignalFlow"),
			EnumerationLiteral(name="Simulink"),
			EnumerationLiteral(name="ESMoL")
    }
)

# Classes
avm_Component = Class(name="avm::Component")
avm_DomainModel = Class(name="avm::DomainModel", is_abstract=True)
avm_Property = Class(name="avm::Property", is_abstract=True)
avm_Resource = Class(name="avm::Resource")
avm_Connector = Class(name="avm::Connector")
avm_DistributionRestriction = Class(name="avm::DistributionRestriction", is_abstract=True)
avm_Port = Class(name="avm::Port", is_abstract=True)
avm_Formula = Class(name="avm::Formula", is_abstract=True)
avm_Value = Class(name="avm::Value")
ValueNode = Class(name="ValueNode")
avm_ValueExpressionType = Class(name="avm::ValueExpressionType", is_abstract=True)
avm_DataSource = Class(name="avm::DataSource")
avm_FixedValue = Class(name="avm::FixedValue")
ValueExpressionType = Class(name="ValueExpressionType")
avm_CalculatedValue = Class(name="avm::CalculatedValue")
avm_AnalysisConstruct = Class(name="avm::AnalysisConstruct", is_abstract=True)
ConnectorCompositionTarget = Class(name="ConnectorCompositionTarget")
avm_assemblyDetail = Class(name="avm::assemblyDetail")
avm_ConnectorFeature = Class(name="avm::ConnectorFeature", is_abstract=True)
PortMapTarget = Class(name="PortMapTarget")
avm_DomainModelPort = Class(name="avm::DomainModelPort", is_abstract=True)
Port = Class(name="Port")
avm_DomainModelParameter = Class(name="avm::DomainModelParameter", is_abstract=True)
avm_DerivedValue = Class(name="avm::DerivedValue")
avm_ValueNode = Class(name="avm::ValueNode", is_abstract=True)
avm_ParametricValue = Class(name="avm::ParametricValue")
avm_SecurityClassification = Class(name="avm::SecurityClassification")
DistributionRestriction = Class(name="DistributionRestriction")
avm_Proprietary = Class(name="avm::Proprietary")
avm_ITAR = Class(name="avm::ITAR")
avm_DomainModelMetric = Class(name="avm::DomainModelMetric", is_abstract=True)
avm_UniformDistribution = Class(name="avm::UniformDistribution")
avm_PrimitiveProperty = Class(name="avm::PrimitiveProperty")
Property_ = Class(name="Property")
avm_ProbabilisticValue = Class(name="avm::ProbabilisticValue", is_abstract=True)
avm_NormalDistribution = Class(name="avm::NormalDistribution")
ProbabilisticValue = Class(name="ProbabilisticValue")
avm_AbstractPort = Class(name="avm::AbstractPort")
avm_Design = Class(name="avm::Design")
avm_Container = Class(name="avm::Container", is_abstract=True)
avm_DesignDomainFeature = Class(name="avm::DesignDomainFeature", is_abstract=True)
avm_ComponentInstance = Class(name="avm::ComponentInstance")
avm_CompoundProperty = Class(name="avm::CompoundProperty")
avm_ParametricEnumeratedValue = Class(name="avm::ParametricEnumeratedValue")
avm_Alternative = Class(name="avm::Alternative")
avm_ValueFlowMux = Class(name="avm::ValueFlowMux")
avm_ComponentPortInstance = Class(name="avm::ComponentPortInstance")
avm_ComponentPrimitivePropertyInstance = Class(name="avm::ComponentPrimitivePropertyInstance")
avm_ComponentConnectorInstance = Class(name="avm::ComponentConnectorInstance")
avm_DesignSpaceContainer = Class(name="avm::DesignSpaceContainer", is_abstract=True)
avm_PortMapTarget = Class(name="avm::PortMapTarget")
avm_Compound = Class(name="avm::Compound")
Container = Class(name="Container")
avm_Optional = Class(name="avm::Optional")
DesignSpaceContainer = Class(name="DesignSpaceContainer")
avm_SimpleFormula = Class(name="avm::SimpleFormula")
Formula = Class(name="Formula")
avm_ComplexFormula = Class(name="avm::ComplexFormula")
avm_Operand = Class(name="avm::Operand")
avm_DoDDistributionStatement = Class(name="avm::DoDDistributionStatement")
avm_TestBench = Class(name="avm::TestBench")
avm_TopLevelSystemUnderTest = Class(name="avm::TopLevelSystemUnderTest")
avm_ConnectorCompositionTarget = Class(name="avm::ConnectorCompositionTarget")
avm_Settings = Class(name="avm::Settings", is_abstract=True)
ContainerInstanceBase = Class(name="ContainerInstanceBase")
TestBenchValueBase = Class(name="TestBenchValueBase")
avm_ContainerInstanceBase = Class(name="avm::ContainerInstanceBase", is_abstract=True)
avm_TestBenchValueBase = Class(name="avm::TestBenchValueBase", is_abstract=True)
avm_WorkflowTaskBase = Class(name="avm::WorkflowTaskBase", is_abstract=True)
avm_Parameter = Class(name="avm::Parameter")
avm_Metric = Class(name="avm::Metric")
avm_TestInjectionPoint = Class(name="avm::TestInjectionPoint")
avm_Workflow = Class(name="avm::Workflow")
avm_modelica_ModelicaModel = Class(name="avm::modelica::ModelicaModel")
DomainModel = Class(name="DomainModel")
Parameter_ = Class(name="Parameter")
Connector = Class(name="Connector")
Metric = Class(name="Metric")
avm_InterpreterTask = Class(name="avm::InterpreterTask")
WorkflowTaskBase = Class(name="WorkflowTaskBase")
avm_ExecutionTask = Class(name="avm::ExecutionTask")
Limit = Class(name="Limit")
Redeclare = Class(name="Redeclare")
avm_modelica_Connector = Class(name="avm::modelica::Connector")
DomainModelPort = Class(name="DomainModelPort")
avm_modelica_Parameter = Class(name="avm::modelica::Parameter")
DomainModelParameter = Class(name="DomainModelParameter")
modelica_avm_Value = Class(name="modelica::avm::Value")
avm_modelica_Metric = Class(name="avm::modelica::Metric")
DomainModelMetric = Class(name="DomainModelMetric")
avm_modelica_Limit = Class(name="avm::modelica::Limit")
avm_modelica_SolverSettings = Class(name="avm::modelica::SolverSettings")
Settings = Class(name="Settings")
avm_cad_CADModel = Class(name="avm::cad::CADModel")
Datum = Class(name="Datum")
avm_modelica_Redeclare = Class(name="avm::modelica::Redeclare")
cad_avm_Value = Class(name="cad::avm::Value")
avm_cad_Point = Class(name="avm::cad::Point")
avm_cad_Axis = Class(name="avm::cad::Axis")
avm_cad_Plane = Class(name="avm::cad::Plane")
Plane = Class(name="Plane")
avm_cad_CoordinateSystem = Class(name="avm::cad::CoordinateSystem")
avm_cad_Metric = Class(name="avm::cad::Metric")
avm_cad_Geometry = Class(name="avm::cad::Geometry", is_abstract=True)
AnalysisConstruct = Class(name="AnalysisConstruct")
avm_cad_Geometry2D = Class(name="avm::cad::Geometry2D", is_abstract=True)
Geometry = Class(name="Geometry")
avm_cad_Geometry3D = Class(name="avm::cad::Geometry3D", is_abstract=True)
avm_cad_Circle = Class(name="avm::cad::Circle")
Geometry2D = Class(name="Geometry2D")
PointReference = Class(name="PointReference")
avm_cad_Polygon = Class(name="avm::cad::Polygon")
avm_cad_Datum = Class(name="avm::cad::Datum", is_abstract=True)
avm_cad_Parameter = Class(name="avm::cad::Parameter")
avm_cad_Sphere = Class(name="avm::cad::Sphere")
avm_cad_CustomGeometry = Class(name="avm::cad::CustomGeometry")
CustomGeometryInput = Class(name="CustomGeometryInput")
avm_cad_CustomGeometryInput = Class(name="avm::cad::CustomGeometryInput")
avm_cad_RevoluteJointSpec = Class(name="avm::cad::RevoluteJointSpec")
KinematicJointSpec = Class(name="KinematicJointSpec")
Axis = Class(name="Axis")
avm_cad_ExtrudedGeometry = Class(name="avm::cad::ExtrudedGeometry")
Geometry3D = Class(name="Geometry3D")
avm_cad_TranslationalJointSpec = Class(name="avm::cad::TranslationalJointSpec")
avm_cad_PointReference = Class(name="avm::cad::PointReference")
Point = Class(name="Point")
avm_cad_Surface = Class(name="avm::cad::Surface")
PlaneReference = Class(name="PlaneReference")
avm_cad_PlaneReference = Class(name="avm::cad::PlaneReference")
avm_cad_GuideDatum = Class(name="avm::cad::GuideDatum")
ConnectorFeature = Class(name="ConnectorFeature")
avm_cad_AssemblyRoot = Class(name="avm::cad::AssemblyRoot")
DesignDomainFeature = Class(name="DesignDomainFeature")
cad_avm_ComponentInstance = Class(name="cad::avm::ComponentInstance")
avm_cad_KinematicJointSpec = Class(name="avm::cad::KinematicJointSpec", is_abstract=True)
avm_manufacturing_Metric = Class(name="avm::manufacturing::Metric")
avm_cyber_CyberModel = Class(name="avm::cyber::CyberModel")
avm_manufacturing_ManufacturingModel = Class(name="avm::manufacturing::ManufacturingModel")
avm_manufacturing_Parameter = Class(name="avm::manufacturing::Parameter")
manufacturing_avm_Value = Class(name="manufacturing::avm::Value")
avm_adamsCar_AdamsCarModel = Class(name="avm::adamsCar::AdamsCarModel")
FileReference = Class(name="FileReference")
avm_adamsCar_Parameter = Class(name="avm::adamsCar::Parameter")
adamsCar_avm_Value = Class(name="adamsCar::avm::Value")
avm_adamsCar_FileReference = Class(name="avm::adamsCar::FileReference")

# avm_Component class attributes and methods
avm_Component_Name: Property = Property(name="Name", type=StringType)
avm_Component_Version: Property = Property(name="Version", type=StringType)
avm_Component_SchemaVersion: Property = Property(name="SchemaVersion", type=StringType)
avm_Component_Classifications: Property = Property(name="Classifications", type=StringType)
avm_Component_ID: Property = Property(name="ID", type=StringType)
avm_Component_Supercedes: Property = Property(name="Supercedes", type=StringType)
avm_Component.attributes={avm_Component_SchemaVersion, avm_Component_Supercedes, avm_Component_Name, avm_Component_Classifications, avm_Component_Version, avm_Component_ID}

# avm_DomainModel class attributes and methods
avm_DomainModel_Author: Property = Property(name="Author", type=StringType)
avm_DomainModel_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModel_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModel_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModel_Name: Property = Property(name="Name", type=StringType)
avm_DomainModel.attributes={avm_DomainModel_Notes, avm_DomainModel_YPosition, avm_DomainModel_Name, avm_DomainModel_Author, avm_DomainModel_XPosition}

# avm_Property class attributes and methods
avm_Property_Name: Property = Property(name="Name", type=StringType)
avm_Property_OnDataSheet: Property = Property(name="OnDataSheet", type=StringType)
avm_Property_Notes: Property = Property(name="Notes", type=StringType)
avm_Property_Definition: Property = Property(name="Definition", type=StringType)
avm_Property_ID: Property = Property(name="ID", type=StringType)
avm_Property_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Property_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Property.attributes={avm_Property_XPosition, avm_Property_Name, avm_Property_OnDataSheet, avm_Property_YPosition, avm_Property_ID, avm_Property_Notes, avm_Property_Definition}

# avm_Resource class attributes and methods
avm_Resource_Name: Property = Property(name="Name", type=StringType)
avm_Resource_Path: Property = Property(name="Path", type=StringType)
avm_Resource_Hash: Property = Property(name="Hash", type=StringType)
avm_Resource_ID: Property = Property(name="ID", type=StringType)
avm_Resource_Notes: Property = Property(name="Notes", type=StringType)
avm_Resource_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Resource_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Resource.attributes={avm_Resource_Path, avm_Resource_Notes, avm_Resource_Hash, avm_Resource_ID, avm_Resource_XPosition, avm_Resource_YPosition, avm_Resource_Name}

# avm_Connector class attributes and methods
avm_Connector_Definition: Property = Property(name="Definition", type=StringType)
avm_Connector_Name: Property = Property(name="Name", type=StringType)
avm_Connector_Notes: Property = Property(name="Notes", type=StringType)
avm_Connector_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Connector_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Connector.attributes={avm_Connector_Definition, avm_Connector_XPosition, avm_Connector_Notes, avm_Connector_YPosition, avm_Connector_Name}

# avm_DistributionRestriction class attributes and methods
avm_DistributionRestriction_Notes: Property = Property(name="Notes", type=StringType)
avm_DistributionRestriction.attributes={avm_DistributionRestriction_Notes}

# avm_Port class attributes and methods
avm_Port_Notes: Property = Property(name="Notes", type=StringType)
avm_Port_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Port_Definition: Property = Property(name="Definition", type=StringType)
avm_Port_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Port_Name: Property = Property(name="Name", type=StringType)
avm_Port.attributes={avm_Port_XPosition, avm_Port_Definition, avm_Port_YPosition, avm_Port_Name, avm_Port_Notes}

# avm_Formula class attributes and methods
avm_Formula_Name: Property = Property(name="Name", type=StringType)
avm_Formula_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Formula_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Formula.attributes={avm_Formula_XPosition, avm_Formula_YPosition, avm_Formula_Name}

# avm_Value class attributes and methods
avm_Value_DimensionType: Property = Property(name="DimensionType", type=StringType)
avm_Value_DataType: Property = Property(name="DataType", type=StringType)
avm_Value_Dimensions: Property = Property(name="Dimensions", type=StringType)
avm_Value_Unit: Property = Property(name="Unit", type=StringType)
avm_Value.attributes={avm_Value_DimensionType, avm_Value_Dimensions, avm_Value_DataType, avm_Value_Unit}

# ValueNode class attributes and methods

# avm_ValueExpressionType class attributes and methods

# avm_DataSource class attributes and methods
avm_DataSource_Notes: Property = Property(name="Notes", type=StringType)
avm_DataSource.attributes={avm_DataSource_Notes}

# avm_FixedValue class attributes and methods
avm_FixedValue_Value: Property = Property(name="Value", type=StringType)
avm_FixedValue_Uncertainty: Property = Property(name="Uncertainty", type=StringType)
avm_FixedValue.attributes={avm_FixedValue_Value, avm_FixedValue_Uncertainty}

# ValueExpressionType class attributes and methods

# avm_CalculatedValue class attributes and methods
avm_CalculatedValue_Expression: Property = Property(name="Expression", type=StringType)
avm_CalculatedValue_Type: Property = Property(name="Type", type=StringType)
avm_CalculatedValue.attributes={avm_CalculatedValue_Type, avm_CalculatedValue_Expression}

# avm_AnalysisConstruct class attributes and methods

# ConnectorCompositionTarget class attributes and methods

# avm_assemblyDetail class attributes and methods

# avm_ConnectorFeature class attributes and methods

# PortMapTarget class attributes and methods

# avm_DomainModelPort class attributes and methods

# Port class attributes and methods

# avm_DomainModelParameter class attributes and methods
avm_DomainModelParameter_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModelParameter_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModelParameter_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModelParameter.attributes={avm_DomainModelParameter_Notes, avm_DomainModelParameter_YPosition, avm_DomainModelParameter_XPosition}

# avm_DerivedValue class attributes and methods

# avm_ValueNode class attributes and methods
avm_ValueNode_ID: Property = Property(name="ID", type=StringType)
avm_ValueNode.attributes={avm_ValueNode_ID}

# avm_ParametricValue class attributes and methods

# avm_SecurityClassification class attributes and methods
avm_SecurityClassification_Level: Property = Property(name="Level", type=StringType)
avm_SecurityClassification.attributes={avm_SecurityClassification_Level}

# DistributionRestriction class attributes and methods

# avm_Proprietary class attributes and methods
avm_Proprietary_Organization: Property = Property(name="Organization", type=StringType)
avm_Proprietary.attributes={avm_Proprietary_Organization}

# avm_ITAR class attributes and methods

# avm_DomainModelMetric class attributes and methods
avm_DomainModelMetric_ID: Property = Property(name="ID", type=StringType)
avm_DomainModelMetric_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModelMetric_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModelMetric_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModelMetric.attributes={avm_DomainModelMetric_YPosition, avm_DomainModelMetric_ID, avm_DomainModelMetric_Notes, avm_DomainModelMetric_XPosition}

# avm_UniformDistribution class attributes and methods

# avm_PrimitiveProperty class attributes and methods

# Property class attributes and methods

# avm_ProbabilisticValue class attributes and methods

# avm_NormalDistribution class attributes and methods

# ProbabilisticValue class attributes and methods

# avm_AbstractPort class attributes and methods

# avm_Design class attributes and methods
avm_Design_SchemaVersion: Property = Property(name="SchemaVersion", type=StringType)
avm_Design_DesignID: Property = Property(name="DesignID", type=StringType)
avm_Design_Name: Property = Property(name="Name", type=StringType)
avm_Design_DesignSpaceSrcID: Property = Property(name="DesignSpaceSrcID", type=StringType)
avm_Design.attributes={avm_Design_SchemaVersion, avm_Design_Name, avm_Design_DesignSpaceSrcID, avm_Design_DesignID}

# avm_Container class attributes and methods
avm_Container_Name: Property = Property(name="Name", type=StringType)
avm_Container_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Container_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Container.attributes={avm_Container_YPosition, avm_Container_XPosition, avm_Container_Name}

# avm_DesignDomainFeature class attributes and methods

# avm_ComponentInstance class attributes and methods
avm_ComponentInstance_ComponentID: Property = Property(name="ComponentID", type=StringType)
avm_ComponentInstance_ID: Property = Property(name="ID", type=StringType)
avm_ComponentInstance_Name: Property = Property(name="Name", type=StringType)
avm_ComponentInstance_DesignSpaceSrcComponentID: Property = Property(name="DesignSpaceSrcComponentID", type=StringType)
avm_ComponentInstance_XPosition: Property = Property(name="XPosition", type=StringType)
avm_ComponentInstance_YPosition: Property = Property(name="YPosition", type=StringType)
avm_ComponentInstance.attributes={avm_ComponentInstance_ID, avm_ComponentInstance_Name, avm_ComponentInstance_XPosition, avm_ComponentInstance_DesignSpaceSrcComponentID, avm_ComponentInstance_YPosition, avm_ComponentInstance_ComponentID}

# avm_CompoundProperty class attributes and methods

# avm_ParametricEnumeratedValue class attributes and methods

# avm_Alternative class attributes and methods

# avm_ValueFlowMux class attributes and methods

# avm_ComponentPortInstance class attributes and methods
avm_ComponentPortInstance_IDinComponentModel: Property = Property(name="IDinComponentModel", type=StringType)
avm_ComponentPortInstance.attributes={avm_ComponentPortInstance_IDinComponentModel}

# avm_ComponentPrimitivePropertyInstance class attributes and methods
avm_ComponentPrimitivePropertyInstance_IDinComponentModel: Property = Property(name="IDinComponentModel", type=StringType)
avm_ComponentPrimitivePropertyInstance.attributes={avm_ComponentPrimitivePropertyInstance_IDinComponentModel}

# avm_ComponentConnectorInstance class attributes and methods
avm_ComponentConnectorInstance_IDinComponentModel: Property = Property(name="IDinComponentModel", type=StringType)
avm_ComponentConnectorInstance.attributes={avm_ComponentConnectorInstance_IDinComponentModel}

# avm_DesignSpaceContainer class attributes and methods

# avm_PortMapTarget class attributes and methods
avm_PortMapTarget_ID: Property = Property(name="ID", type=StringType)
avm_PortMapTarget.attributes={avm_PortMapTarget_ID}

# avm_Compound class attributes and methods

# Container class attributes and methods

# avm_Optional class attributes and methods

# DesignSpaceContainer class attributes and methods

# avm_SimpleFormula class attributes and methods
avm_SimpleFormula_Operation: Property = Property(name="Operation", type=StringType)
avm_SimpleFormula.attributes={avm_SimpleFormula_Operation}

# Formula class attributes and methods

# avm_ComplexFormula class attributes and methods
avm_ComplexFormula_Expression: Property = Property(name="Expression", type=StringType)
avm_ComplexFormula.attributes={avm_ComplexFormula_Expression}

# avm_Operand class attributes and methods
avm_Operand_Symbol: Property = Property(name="Symbol", type=StringType)
avm_Operand.attributes={avm_Operand_Symbol}

# avm_DoDDistributionStatement class attributes and methods
avm_DoDDistributionStatement_Type: Property = Property(name="Type", type=StringType)
avm_DoDDistributionStatement.attributes={avm_DoDDistributionStatement_Type}

# avm_TestBench class attributes and methods
avm_TestBench_Name: Property = Property(name="Name", type=StringType)
avm_TestBench.attributes={avm_TestBench_Name}

# avm_TopLevelSystemUnderTest class attributes and methods
avm_TopLevelSystemUnderTest_DesignID: Property = Property(name="DesignID", type=StringType)
avm_TopLevelSystemUnderTest.attributes={avm_TopLevelSystemUnderTest_DesignID}

# avm_ConnectorCompositionTarget class attributes and methods
avm_ConnectorCompositionTarget_ID: Property = Property(name="ID", type=StringType)
avm_ConnectorCompositionTarget.attributes={avm_ConnectorCompositionTarget_ID}

# avm_Settings class attributes and methods

# ContainerInstanceBase class attributes and methods

# TestBenchValueBase class attributes and methods

# avm_ContainerInstanceBase class attributes and methods
avm_ContainerInstanceBase_IDinSourceModel: Property = Property(name="IDinSourceModel", type=StringType)
avm_ContainerInstanceBase_XPosition: Property = Property(name="XPosition", type=StringType)
avm_ContainerInstanceBase_YPosition: Property = Property(name="YPosition", type=StringType)
avm_ContainerInstanceBase.attributes={avm_ContainerInstanceBase_IDinSourceModel, avm_ContainerInstanceBase_YPosition, avm_ContainerInstanceBase_XPosition}

# avm_TestBenchValueBase class attributes and methods
avm_TestBenchValueBase_ID: Property = Property(name="ID", type=StringType)
avm_TestBenchValueBase_Name: Property = Property(name="Name", type=StringType)
avm_TestBenchValueBase_Notes: Property = Property(name="Notes", type=StringType)
avm_TestBenchValueBase_XPosition: Property = Property(name="XPosition", type=StringType)
avm_TestBenchValueBase_YPosition: Property = Property(name="YPosition", type=StringType)
avm_TestBenchValueBase.attributes={avm_TestBenchValueBase_YPosition, avm_TestBenchValueBase_Name, avm_TestBenchValueBase_XPosition, avm_TestBenchValueBase_Notes, avm_TestBenchValueBase_ID}

# avm_WorkflowTaskBase class attributes and methods
avm_WorkflowTaskBase_Name: Property = Property(name="Name", type=StringType)
avm_WorkflowTaskBase.attributes={avm_WorkflowTaskBase_Name}

# avm_Parameter class attributes and methods

# avm_Metric class attributes and methods

# avm_TestInjectionPoint class attributes and methods

# avm_Workflow class attributes and methods
avm_Workflow_Name: Property = Property(name="Name", type=StringType)
avm_Workflow.attributes={avm_Workflow_Name}

# avm_modelica_ModelicaModel class attributes and methods
avm_modelica_ModelicaModel_Class: Property = Property(name="Class", type=StringType)
avm_modelica_ModelicaModel.attributes={avm_modelica_ModelicaModel_Class}

# DomainModel class attributes and methods

# Parameter class attributes and methods

# Connector class attributes and methods

# Metric class attributes and methods

# avm_InterpreterTask class attributes and methods
avm_InterpreterTask_COMName: Property = Property(name="COMName", type=StringType)
avm_InterpreterTask_Parameters: Property = Property(name="Parameters", type=StringType)
avm_InterpreterTask.attributes={avm_InterpreterTask_COMName, avm_InterpreterTask_Parameters}

# WorkflowTaskBase class attributes and methods

# avm_ExecutionTask class attributes and methods
avm_ExecutionTask_Description: Property = Property(name="Description", type=StringType)
avm_ExecutionTask_Invocation: Property = Property(name="Invocation", type=StringType)
avm_ExecutionTask.attributes={avm_ExecutionTask_Description, avm_ExecutionTask_Invocation}

# Limit class attributes and methods

# Redeclare class attributes and methods

# avm_modelica_Connector class attributes and methods
avm_modelica_Connector_Class: Property = Property(name="Class", type=StringType)
avm_modelica_Connector_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Connector.attributes={avm_modelica_Connector_Class, avm_modelica_Connector_Locator}

# DomainModelPort class attributes and methods

# avm_modelica_Parameter class attributes and methods
avm_modelica_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Parameter.attributes={avm_modelica_Parameter_Locator}

# DomainModelParameter class attributes and methods

# modelica_avm_Value class attributes and methods

# avm_modelica_Metric class attributes and methods
avm_modelica_Metric_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Metric.attributes={avm_modelica_Metric_Locator}

# DomainModelMetric class attributes and methods

# avm_modelica_Limit class attributes and methods
avm_modelica_Limit_VariableLocator: Property = Property(name="VariableLocator", type=StringType)
avm_modelica_Limit_BoundType: Property = Property(name="BoundType", type=StringType)
avm_modelica_Limit_Name: Property = Property(name="Name", type=StringType)
avm_modelica_Limit_ToleranceTimeWindow: Property = Property(name="ToleranceTimeWindow", type=StringType)
avm_modelica_Limit_Notes: Property = Property(name="Notes", type=StringType)
avm_modelica_Limit.attributes={avm_modelica_Limit_VariableLocator, avm_modelica_Limit_Notes, avm_modelica_Limit_Name, avm_modelica_Limit_BoundType, avm_modelica_Limit_ToleranceTimeWindow}

# avm_modelica_SolverSettings class attributes and methods
avm_modelica_SolverSettings_Solver: Property = Property(name="Solver", type=StringType)
avm_modelica_SolverSettings_JobManagerToolSelection: Property = Property(name="JobManagerToolSelection", type=StringType)
avm_modelica_SolverSettings_StartTime: Property = Property(name="StartTime", type=StringType)
avm_modelica_SolverSettings_StopTime: Property = Property(name="StopTime", type=StringType)
avm_modelica_SolverSettings_IntervalMethod: Property = Property(name="IntervalMethod", type=StringType)
avm_modelica_SolverSettings_NumberOfIntervals: Property = Property(name="NumberOfIntervals", type=StringType)
avm_modelica_SolverSettings_IntervalLength: Property = Property(name="IntervalLength", type=StringType)
avm_modelica_SolverSettings_ToolSpecificAnnotations: Property = Property(name="ToolSpecificAnnotations", type=StringType)
avm_modelica_SolverSettings_Tolerance: Property = Property(name="Tolerance", type=StringType)
avm_modelica_SolverSettings.attributes={avm_modelica_SolverSettings_Solver, avm_modelica_SolverSettings_IntervalMethod, avm_modelica_SolverSettings_ToolSpecificAnnotations, avm_modelica_SolverSettings_StartTime, avm_modelica_SolverSettings_IntervalLength, avm_modelica_SolverSettings_StopTime, avm_modelica_SolverSettings_NumberOfIntervals, avm_modelica_SolverSettings_JobManagerToolSelection, avm_modelica_SolverSettings_Tolerance}

# Settings class attributes and methods

# avm_cad_CADModel class attributes and methods

# Datum class attributes and methods

# avm_modelica_Redeclare class attributes and methods
avm_modelica_Redeclare_Type: Property = Property(name="Type", type=StringType)
avm_modelica_Redeclare_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Redeclare.attributes={avm_modelica_Redeclare_Type, avm_modelica_Redeclare_Locator}

# cad_avm_Value class attributes and methods

# avm_cad_Point class attributes and methods

# avm_cad_Axis class attributes and methods

# avm_cad_Plane class attributes and methods

# Plane class attributes and methods

# avm_cad_CoordinateSystem class attributes and methods

# avm_cad_Metric class attributes and methods
avm_cad_Metric_Name: Property = Property(name="Name", type=StringType)
avm_cad_Metric.attributes={avm_cad_Metric_Name}

# avm_cad_Geometry class attributes and methods
avm_cad_Geometry_GeometryQualifier: Property = Property(name="GeometryQualifier", type=StringType)
avm_cad_Geometry_PartIntersectionModifier: Property = Property(name="PartIntersectionModifier", type=StringType)
avm_cad_Geometry.attributes={avm_cad_Geometry_PartIntersectionModifier, avm_cad_Geometry_GeometryQualifier}

# AnalysisConstruct class attributes and methods

# avm_cad_Geometry2D class attributes and methods

# Geometry class attributes and methods

# avm_cad_Geometry3D class attributes and methods

# avm_cad_Circle class attributes and methods

# Geometry2D class attributes and methods

# PointReference class attributes and methods

# avm_cad_Polygon class attributes and methods

# avm_cad_Datum class attributes and methods
avm_cad_Datum_DatumName: Property = Property(name="DatumName", type=StringType)
avm_cad_Datum.attributes={avm_cad_Datum_DatumName}

# avm_cad_Parameter class attributes and methods
avm_cad_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_cad_Parameter.attributes={avm_cad_Parameter_Name}

# avm_cad_Sphere class attributes and methods

# avm_cad_CustomGeometry class attributes and methods

# CustomGeometryInput class attributes and methods

# avm_cad_CustomGeometryInput class attributes and methods
avm_cad_CustomGeometryInput_Operation: Property = Property(name="Operation", type=StringType)
avm_cad_CustomGeometryInput.attributes={avm_cad_CustomGeometryInput_Operation}

# avm_cad_RevoluteJointSpec class attributes and methods

# KinematicJointSpec class attributes and methods

# Axis class attributes and methods

# avm_cad_ExtrudedGeometry class attributes and methods

# Geometry3D class attributes and methods

# avm_cad_TranslationalJointSpec class attributes and methods

# avm_cad_PointReference class attributes and methods

# Point class attributes and methods

# avm_cad_Surface class attributes and methods

# PlaneReference class attributes and methods

# avm_cad_PlaneReference class attributes and methods

# avm_cad_GuideDatum class attributes and methods

# ConnectorFeature class attributes and methods

# avm_cad_AssemblyRoot class attributes and methods

# DesignDomainFeature class attributes and methods

# cad_avm_ComponentInstance class attributes and methods

# avm_cad_KinematicJointSpec class attributes and methods

# avm_manufacturing_Metric class attributes and methods
avm_manufacturing_Metric_Name: Property = Property(name="Name", type=StringType)
avm_manufacturing_Metric.attributes={avm_manufacturing_Metric_Name}

# avm_cyber_CyberModel class attributes and methods
avm_cyber_CyberModel_Type: Property = Property(name="Type", type=StringType)
avm_cyber_CyberModel_Class: Property = Property(name="Class", type=StringType)
avm_cyber_CyberModel_Locator: Property = Property(name="Locator", type=StringType)
avm_cyber_CyberModel.attributes={avm_cyber_CyberModel_Type, avm_cyber_CyberModel_Locator, avm_cyber_CyberModel_Class}

# avm_manufacturing_ManufacturingModel class attributes and methods

# avm_manufacturing_Parameter class attributes and methods
avm_manufacturing_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_manufacturing_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_manufacturing_Parameter.attributes={avm_manufacturing_Parameter_Locator, avm_manufacturing_Parameter_Name}

# manufacturing_avm_Value class attributes and methods

# avm_adamsCar_AdamsCarModel class attributes and methods

# FileReference class attributes and methods

# avm_adamsCar_Parameter class attributes and methods
avm_adamsCar_Parameter_ID: Property = Property(name="ID", type=StringType)
avm_adamsCar_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_adamsCar_Parameter.attributes={avm_adamsCar_Parameter_Name, avm_adamsCar_Parameter_ID}

# adamsCar_avm_Value class attributes and methods

# avm_adamsCar_FileReference class attributes and methods
avm_adamsCar_FileReference_FilePath: Property = Property(name="FilePath", type=StringType)
avm_adamsCar_FileReference_ID: Property = Property(name="ID", type=StringType)
avm_adamsCar_FileReference_Name: Property = Property(name="Name", type=StringType)
avm_adamsCar_FileReference.attributes={avm_adamsCar_FileReference_Name, avm_adamsCar_FileReference_FilePath, avm_adamsCar_FileReference_ID}

# Relationships
DomainModel0: BinaryAssociation = BinaryAssociation(
    name="DomainModel0",
    ends={
        Property(name="avm_DomainModel", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component", type=avm_DomainModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Property1: BinaryAssociation = BinaryAssociation(
    name="Property1",
    ends={
        Property(name="avm_Property", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component2", type=avm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ResourceDependency3: BinaryAssociation = BinaryAssociation(
    name="ResourceDependency3",
    ends={
        Property(name="avm_Resource", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component4", type=avm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector5: BinaryAssociation = BinaryAssociation(
    name="Connector5",
    ends={
        Property(name="avm_Connector", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component6", type=avm_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DistributionRestriction7: BinaryAssociation = BinaryAssociation(
    name="DistributionRestriction7",
    ends={
        Property(name="avm_DistributionRestriction", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component8", type=avm_DistributionRestriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Port9: BinaryAssociation = BinaryAssociation(
    name="Port9",
    ends={
        Property(name="avm_Port", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component10", type=avm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Formula13: BinaryAssociation = BinaryAssociation(
    name="Formula13",
    ends={
        Property(name="avm_Formula", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component14", type=avm_Formula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
UsesResource15: BinaryAssociation = BinaryAssociation(
    name="UsesResource15",
    ends={
        Property(name="avm_Resource17", type=avm_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DomainModel16", type=avm_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
ValueExpression18: BinaryAssociation = BinaryAssociation(
    name="ValueExpression18",
    ends={
        Property(name="avm_ValueExpressionType", type=avm_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Value", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DataSource19: BinaryAssociation = BinaryAssociation(
    name="DataSource19",
    ends={
        Property(name="avm_DataSource", type=avm_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Value20", type=avm_DataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AnalysisConstruct11: BinaryAssociation = BinaryAssociation(
    name="AnalysisConstruct11",
    ends={
        Property(name="avm_AnalysisConstruct", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component12", type=avm_AnalysisConstruct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Role22: BinaryAssociation = BinaryAssociation(
    name="Role22",
    ends={
        Property(name="avm_Port24", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector23", type=avm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Property25: BinaryAssociation = BinaryAssociation(
    name="Property25",
    ends={
        Property(name="avm_Property27", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector26", type=avm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DefaultJoin28: BinaryAssociation = BinaryAssociation(
    name="DefaultJoin28",
    ends={
        Property(name="avm_assemblyDetail", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector29", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector31: BinaryAssociation = BinaryAssociation(
    name="Connector31",
    ends={
        Property(name="avm_Connector32", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector30", type=avm_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectorFeature33: BinaryAssociation = BinaryAssociation(
    name="ConnectorFeature33",
    ends={
        Property(name="avm_ConnectorFeature", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector34", type=avm_ConnectorFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ValueSource21: BinaryAssociation = BinaryAssociation(
    name="ValueSource21",
    ends={
        Property(name="avm_ValueNode", type=avm_DerivedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DerivedValue", type=avm_ValueNode, multiplicity=Multiplicity(1, 1))
    }
)
Default35: BinaryAssociation = BinaryAssociation(
    name="Default35",
    ends={
        Property(name="avm_ValueExpressionType36", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Maximum37: BinaryAssociation = BinaryAssociation(
    name="Maximum37",
    ends={
        Property(name="avm_ValueExpressionType39", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue38", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Minimum40: BinaryAssociation = BinaryAssociation(
    name="Minimum40",
    ends={
        Property(name="avm_ValueExpressionType42", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue41", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AssignedValue43: BinaryAssociation = BinaryAssociation(
    name="AssignedValue43",
    ends={
        Property(name="avm_ValueExpressionType45", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue44", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
StandardDeviation48: BinaryAssociation = BinaryAssociation(
    name="StandardDeviation48",
    ends={
        Property(name="avm_ValueExpressionType50", type=avm_NormalDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_NormalDistribution49", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Value51: BinaryAssociation = BinaryAssociation(
    name="Value51",
    ends={
        Property(name="avm_Value52", type=avm_DomainModelMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DomainModelMetric", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Mean46: BinaryAssociation = BinaryAssociation(
    name="Mean46",
    ends={
        Property(name="avm_ValueExpressionType47", type=avm_NormalDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_NormalDistribution", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
AssignedValue60: BinaryAssociation = BinaryAssociation(
    name="AssignedValue60",
    ends={
        Property(name="avm_FixedValue", type=avm_ParametricEnumeratedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricEnumeratedValue", type=avm_FixedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Enum61: BinaryAssociation = BinaryAssociation(
    name="Enum61",
    ends={
        Property(name="avm_ValueExpressionType63", type=avm_ParametricEnumeratedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricEnumeratedValue62", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
FromResource64: BinaryAssociation = BinaryAssociation(
    name="FromResource64",
    ends={
        Property(name="avm_Resource66", type=avm_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DataSource65", type=avm_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
RootContainer67: BinaryAssociation = BinaryAssociation(
    name="RootContainer67",
    ends={
        Property(name="avm_Container", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design", type=avm_Container, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DomainFeature68: BinaryAssociation = BinaryAssociation(
    name="DomainFeature68",
    ends={
        Property(name="avm_DesignDomainFeature", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design69", type=avm_DesignDomainFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Container71: BinaryAssociation = BinaryAssociation(
    name="Container71",
    ends={
        Property(name="avm_Container72", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container70", type=avm_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Property73: BinaryAssociation = BinaryAssociation(
    name="Property73",
    ends={
        Property(name="avm_Property75", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container74", type=avm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ComponentInstance76: BinaryAssociation = BinaryAssociation(
    name="ComponentInstance76",
    ends={
        Property(name="avm_ComponentInstance", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container77", type=avm_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Port78: BinaryAssociation = BinaryAssociation(
    name="Port78",
    ends={
        Property(name="avm_Port80", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container79", type=avm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector81: BinaryAssociation = BinaryAssociation(
    name="Connector81",
    ends={
        Property(name="avm_Connector83", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container82", type=avm_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value53: BinaryAssociation = BinaryAssociation(
    name="Value53",
    ends={
        Property(name="avm_Value54", type=avm_PrimitiveProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_PrimitiveProperty", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CompoundProperty56: BinaryAssociation = BinaryAssociation(
    name="CompoundProperty56",
    ends={
        Property(name="avm_CompoundProperty", type=avm_CompoundProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_CompoundProperty55", type=avm_CompoundProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimitiveProperty57: BinaryAssociation = BinaryAssociation(
    name="PrimitiveProperty57",
    ends={
        Property(name="avm_PrimitiveProperty59", type=avm_CompoundProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_CompoundProperty58", type=avm_PrimitiveProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ValueFlowMux90: BinaryAssociation = BinaryAssociation(
    name="ValueFlowMux90",
    ends={
        Property(name="avm_ValueFlowMux", type=avm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Alternative", type=avm_ValueFlowMux, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PortInstance91: BinaryAssociation = BinaryAssociation(
    name="PortInstance91",
    ends={
        Property(name="avm_ComponentPortInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance92", type=avm_ComponentPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimitivePropertyInstance93: BinaryAssociation = BinaryAssociation(
    name="PrimitivePropertyInstance93",
    ends={
        Property(name="avm_ComponentPrimitivePropertyInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance94", type=avm_ComponentPrimitivePropertyInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectorInstance95: BinaryAssociation = BinaryAssociation(
    name="ConnectorInstance95",
    ends={
        Property(name="avm_ComponentConnectorInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance96", type=avm_ComponentConnectorInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value97: BinaryAssociation = BinaryAssociation(
    name="Value97",
    ends={
        Property(name="avm_Value99", type=avm_ComponentPrimitivePropertyInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentPrimitivePropertyInstance98", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PortMap101: BinaryAssociation = BinaryAssociation(
    name="PortMap101",
    ends={
        Property(name="avm_PortMapTarget", type=avm_PortMapTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_PortMapTarget100", type=avm_PortMapTarget, multiplicity=Multiplicity(0, 9999))
    }
)
JoinData84: BinaryAssociation = BinaryAssociation(
    name="JoinData84",
    ends={
        Property(name="avm_assemblyDetail86", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container85", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Formula87: BinaryAssociation = BinaryAssociation(
    name="Formula87",
    ends={
        Property(name="avm_Formula89", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container88", type=avm_Formula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Operand107: BinaryAssociation = BinaryAssociation(
    name="Operand107",
    ends={
        Property(name="avm_ValueNode108", type=avm_SimpleFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_SimpleFormula", type=avm_ValueNode, multiplicity=Multiplicity(1, 9999))
    }
)
Operand109: BinaryAssociation = BinaryAssociation(
    name="Operand109",
    ends={
        Property(name="avm_Operand", type=avm_ComplexFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComplexFormula", type=avm_Operand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ValueSource110: BinaryAssociation = BinaryAssociation(
    name="ValueSource110",
    ends={
        Property(name="avm_ValueNode112", type=avm_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Operand111", type=avm_ValueNode, multiplicity=Multiplicity(1, 1))
    }
)
TopLevelSystemUnderTest113: BinaryAssociation = BinaryAssociation(
    name="TopLevelSystemUnderTest113",
    ends={
        Property(name="avm_TopLevelSystemUnderTest", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench", type=avm_TopLevelSystemUnderTest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ConnectorComposition103: BinaryAssociation = BinaryAssociation(
    name="ConnectorComposition103",
    ends={
        Property(name="avm_ConnectorCompositionTarget", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ConnectorCompositionTarget102", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(0, 9999))
    }
)
ApplyJoinData104: BinaryAssociation = BinaryAssociation(
    name="ApplyJoinData104",
    ends={
        Property(name="avm_assemblyDetail106", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ConnectorCompositionTarget105", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999))
    }
)
Workflow123: BinaryAssociation = BinaryAssociation(
    name="Workflow123",
    ends={
        Property(name="avm_TestBench124", type=avm_Workflow, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="avm_Workflow", type=avm_TestBench, multiplicity=Multiplicity(1, 1))
    }
)
Settings125: BinaryAssociation = BinaryAssociation(
    name="Settings125",
    ends={
        Property(name="avm_Settings", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench126", type=avm_Settings, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestStructure127: BinaryAssociation = BinaryAssociation(
    name="TestStructure127",
    ends={
        Property(name="avm_DomainModel129", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench128", type=avm_DomainModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value130: BinaryAssociation = BinaryAssociation(
    name="Value130",
    ends={
        Property(name="avm_Value131", type=avm_TestBenchValueBase, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBenchValueBase", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Task132: BinaryAssociation = BinaryAssociation(
    name="Task132",
    ends={
        Property(name="avm_WorkflowTaskBase", type=avm_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Workflow133", type=avm_WorkflowTaskBase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Parameter114: BinaryAssociation = BinaryAssociation(
    name="Parameter114",
    ends={
        Property(name="avm_Parameter", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench115", type=avm_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric116: BinaryAssociation = BinaryAssociation(
    name="Metric116",
    ends={
        Property(name="avm_Metric", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench117", type=avm_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestInjectionPoint118: BinaryAssociation = BinaryAssociation(
    name="TestInjectionPoint118",
    ends={
        Property(name="avm_TestInjectionPoint", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench119", type=avm_TestInjectionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestComponent120: BinaryAssociation = BinaryAssociation(
    name="TestComponent120",
    ends={
        Property(name="avm_ComponentInstance122", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench121", type=avm_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Source134: BinaryAssociation = BinaryAssociation(
    name="Source134",
    ends={
        Property(name="avm_ValueNode136", type=avm_ValueFlowMux, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ValueFlowMux135", type=avm_ValueNode, multiplicity=Multiplicity(0, 9999))
    }
)
Parameter137: BinaryAssociation = BinaryAssociation(
    name="Parameter137",
    ends={
        Property(name="Parameter", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector138: BinaryAssociation = BinaryAssociation(
    name="Connector138",
    ends={
        Property(name="Connector", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel139", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric140: BinaryAssociation = BinaryAssociation(
    name="Metric140",
    ends={
        Property(name="Metric", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel141", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Limit142: BinaryAssociation = BinaryAssociation(
    name="Limit142",
    ends={
        Property(name="Limit", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel143", type=Limit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Redeclare144: BinaryAssociation = BinaryAssociation(
    name="Redeclare144",
    ends={
        Property(name="Redeclare", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel145", type=Redeclare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter146: BinaryAssociation = BinaryAssociation(
    name="Parameter146",
    ends={
        Property(name="Parameter147", type=avm_modelica_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Connector", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Redeclare148: BinaryAssociation = BinaryAssociation(
    name="Redeclare148",
    ends={
        Property(name="Redeclare150", type=avm_modelica_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Connector149", type=Redeclare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value151: BinaryAssociation = BinaryAssociation(
    name="Value151",
    ends={
        Property(name="modelica_avm_Value", type=avm_modelica_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Parameter", type=modelica_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TargetValue152: BinaryAssociation = BinaryAssociation(
    name="TargetValue152",
    ends={
        Property(name="modelica_avm_Value153", type=avm_modelica_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Limit", type=modelica_avm_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Value154: BinaryAssociation = BinaryAssociation(
    name="Value154",
    ends={
        Property(name="modelica_avm_Value155", type=avm_modelica_Redeclare, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Redeclare", type=modelica_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Datum156: BinaryAssociation = BinaryAssociation(
    name="Datum156",
    ends={
        Property(name="Datum", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel", type=Datum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter157: BinaryAssociation = BinaryAssociation(
    name="Parameter157",
    ends={
        Property(name="Parameter159", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel158", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value165: BinaryAssociation = BinaryAssociation(
    name="Value165",
    ends={
        Property(name="cad_avm_Value", type=avm_cad_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Parameter", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SurfaceReverseMap166: BinaryAssociation = BinaryAssociation(
    name="SurfaceReverseMap166",
    ends={
        Property(name="Plane", type=avm_cad_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Plane", type=Plane, multiplicity=Multiplicity(0, 9999))
    }
)
Metric167: BinaryAssociation = BinaryAssociation(
    name="Metric167",
    ends={
        Property(name="Metric168", type=avm_cad_CoordinateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CoordinateSystem", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CircleCenter169: BinaryAssociation = BinaryAssociation(
    name="CircleCenter169",
    ends={
        Property(name="PointReference", type=avm_cad_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Circle", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CircleEdge170: BinaryAssociation = BinaryAssociation(
    name="CircleEdge170",
    ends={
        Property(name="PointReference172", type=avm_cad_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Circle171", type=PointReference, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
PolygonPoint173: BinaryAssociation = BinaryAssociation(
    name="PolygonPoint173",
    ends={
        Property(name="PointReference174", type=avm_cad_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Polygon", type=PointReference, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
ModelMetric160: BinaryAssociation = BinaryAssociation(
    name="ModelMetric160",
    ends={
        Property(name="Metric162", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel161", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DatumMetric163: BinaryAssociation = BinaryAssociation(
    name="DatumMetric163",
    ends={
        Property(name="Metric164", type=avm_cad_Datum, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Datum", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
SphereCenter182: BinaryAssociation = BinaryAssociation(
    name="SphereCenter182",
    ends={
        Property(name="PointReference183", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SphereEdge184: BinaryAssociation = BinaryAssociation(
    name="SphereEdge184",
    ends={
        Property(name="PointReference186", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere185", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CustomGeometryInput187: BinaryAssociation = BinaryAssociation(
    name="CustomGeometryInput187",
    ends={
        Property(name="CustomGeometryInput", type=avm_cad_CustomGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometry", type=CustomGeometryInput, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
AlignmentPlane196: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane196",
    ends={
        Property(name="Plane197", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis198: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis198",
    ends={
        Property(name="Axis", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec199", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
RotationLimitReference200: BinaryAssociation = BinaryAssociation(
    name="RotationLimitReference200",
    ends={
        Property(name="Plane202", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec201", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
MinimumRotation203: BinaryAssociation = BinaryAssociation(
    name="MinimumRotation203",
    ends={
        Property(name="cad_avm_Value205", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec204", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultRotation206: BinaryAssociation = BinaryAssociation(
    name="DefaultRotation206",
    ends={
        Property(name="cad_avm_Value208", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec207", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MaximumRotation209: BinaryAssociation = BinaryAssociation(
    name="MaximumRotation209",
    ends={
        Property(name="cad_avm_Value211", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec210", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ExtrusionHeight175: BinaryAssociation = BinaryAssociation(
    name="ExtrusionHeight175",
    ends={
        Property(name="PointReference176", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
InputGeometry188: BinaryAssociation = BinaryAssociation(
    name="InputGeometry188",
    ends={
        Property(name="Geometry", type=avm_cad_CustomGeometryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometryInput", type=Geometry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExtrusionSurface177: BinaryAssociation = BinaryAssociation(
    name="ExtrusionSurface177",
    ends={
        Property(name="Geometry2D", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry178", type=Geometry2D, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
DirectionReferencePoint179: BinaryAssociation = BinaryAssociation(
    name="DirectionReferencePoint179",
    ends={
        Property(name="PointReference181", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry180", type=PointReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ReferredPoint189: BinaryAssociation = BinaryAssociation(
    name="ReferredPoint189",
    ends={
        Property(name="Point", type=avm_cad_PointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PointReference", type=Point, multiplicity=Multiplicity(0, 9999))
    }
)
ReferencePlane190: BinaryAssociation = BinaryAssociation(
    name="ReferencePlane190",
    ends={
        Property(name="PlaneReference", type=avm_cad_Surface, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Surface", type=PlaneReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReferredPlane191: BinaryAssociation = BinaryAssociation(
    name="ReferredPlane191",
    ends={
        Property(name="Plane192", type=avm_cad_PlaneReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PlaneReference", type=Plane, multiplicity=Multiplicity(0, 9999))
    }
)
Datum193: BinaryAssociation = BinaryAssociation(
    name="Datum193",
    ends={
        Property(name="Datum194", type=avm_cad_GuideDatum, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_GuideDatum", type=Datum, multiplicity=Multiplicity(1, 1))
    }
)
AssemblyRootComponentInstance195: BinaryAssociation = BinaryAssociation(
    name="AssemblyRootComponentInstance195",
    ends={
        Property(name="cad_avm_ComponentInstance", type=avm_cad_AssemblyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_AssemblyRoot", type=cad_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
Connector235: BinaryAssociation = BinaryAssociation(
    name="Connector235",
    ends={
        Property(name="Connector236", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter237: BinaryAssociation = BinaryAssociation(
    name="Parameter237",
    ends={
        Property(name="Parameter239", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel238", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AlignmentPlane212: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane212",
    ends={
        Property(name="Plane213", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis214: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis214",
    ends={
        Property(name="Axis216", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec215", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
MinimumTranslation217: BinaryAssociation = BinaryAssociation(
    name="MinimumTranslation217",
    ends={
        Property(name="cad_avm_Value219", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec218", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultTranslation220: BinaryAssociation = BinaryAssociation(
    name="DefaultTranslation220",
    ends={
        Property(name="cad_avm_Value222", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec221", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MaximumTranslation223: BinaryAssociation = BinaryAssociation(
    name="MaximumTranslation223",
    ends={
        Property(name="cad_avm_Value225", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec224", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TranslationLimitReference226: BinaryAssociation = BinaryAssociation(
    name="TranslationLimitReference226",
    ends={
        Property(name="Plane228", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec227", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
Parameter229: BinaryAssociation = BinaryAssociation(
    name="Parameter229",
    ends={
        Property(name="Parameter230", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric231: BinaryAssociation = BinaryAssociation(
    name="Metric231",
    ends={
        Property(name="Metric233", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel232", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value234: BinaryAssociation = BinaryAssociation(
    name="Value234",
    ends={
        Property(name="manufacturing_avm_Value", type=avm_manufacturing_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_Parameter", type=manufacturing_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter240: BinaryAssociation = BinaryAssociation(
    name="Parameter240",
    ends={
        Property(name="Parameter241", type=avm_adamsCar_AdamsCarModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_AdamsCarModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FileReference242: BinaryAssociation = BinaryAssociation(
    name="FileReference242",
    ends={
        Property(name="FileReference", type=avm_adamsCar_AdamsCarModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_AdamsCarModel243", type=FileReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Value244: BinaryAssociation = BinaryAssociation(
    name="Value244",
    ends={
        Property(name="adamsCar_avm_Value", type=avm_adamsCar_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_Parameter", type=adamsCar_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ParameterSwap245: BinaryAssociation = BinaryAssociation(
    name="ParameterSwap245",
    ends={
        Property(name="Parameter246", type=avm_adamsCar_FileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_FileReference", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
FileReferenceSwap247: BinaryAssociation = BinaryAssociation(
    name="FileReferenceSwap247",
    ends={
        Property(name="FileReference249", type=avm_adamsCar_FileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_FileReference248", type=FileReference, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_avm_Value_ValueNode = Generalization(general=ValueNode, specific=avm_Value)
gen_avm_FixedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_FixedValue)
gen_avm_CalculatedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_CalculatedValue)
gen_avm_Connector_ConnectorCompositionTarget = Generalization(general=ConnectorCompositionTarget, specific=avm_Connector)
gen_avm_Port_PortMapTarget = Generalization(general=PortMapTarget, specific=avm_Port)
gen_avm_DomainModelPort_Port = Generalization(general=Port, specific=avm_DomainModelPort)
gen_avm_DerivedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_DerivedValue)
gen_avm_ParametricValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ParametricValue)
gen_avm_SecurityClassification_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_SecurityClassification)
gen_avm_Proprietary_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_Proprietary)
gen_avm_ITAR_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_ITAR)
gen_avm_UniformDistribution_ProbabilisticValue = Generalization(general=ProbabilisticValue, specific=avm_UniformDistribution)
gen_avm_ProbabilisticValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ProbabilisticValue)
gen_avm_NormalDistribution_ProbabilisticValue = Generalization(general=ProbabilisticValue, specific=avm_NormalDistribution)
gen_avm_AbstractPort_Port = Generalization(general=Port, specific=avm_AbstractPort)
gen_avm_PrimitiveProperty_Property = Generalization(general=Property_, specific=avm_PrimitiveProperty)
gen_avm_CompoundProperty_Property = Generalization(general=Property_, specific=avm_CompoundProperty)
gen_avm_ParametricEnumeratedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ParametricEnumeratedValue)
gen_avm_Alternative_DesignSpaceContainer = Generalization(general=DesignSpaceContainer, specific=avm_Alternative)
gen_avm_ComponentPortInstance_PortMapTarget = Generalization(general=PortMapTarget, specific=avm_ComponentPortInstance)
gen_avm_DesignSpaceContainer_Container = Generalization(general=Container, specific=avm_DesignSpaceContainer)
gen_avm_ComponentConnectorInstance_ConnectorCompositionTarget = Generalization(general=ConnectorCompositionTarget, specific=avm_ComponentConnectorInstance)
gen_avm_Compound_Container = Generalization(general=Container, specific=avm_Compound)
gen_avm_Optional_DesignSpaceContainer = Generalization(general=DesignSpaceContainer, specific=avm_Optional)
gen_avm_SimpleFormula_Formula = Generalization(general=Formula, specific=avm_SimpleFormula)
gen_avm_ComplexFormula_Formula = Generalization(general=Formula, specific=avm_ComplexFormula)
gen_avm_DoDDistributionStatement_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_DoDDistributionStatement)
gen_avm_Formula_ValueNode = Generalization(general=ValueNode, specific=avm_Formula)
gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TopLevelSystemUnderTest)
gen_avm_Parameter_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Parameter)
gen_avm_Metric_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Metric)
gen_avm_TestInjectionPoint_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TestInjectionPoint)
gen_avm_modelica_ModelicaModel_DomainModel = Generalization(general=DomainModel, specific=avm_modelica_ModelicaModel)
gen_avm_InterpreterTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_InterpreterTask)
gen_avm_ExecutionTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_ExecutionTask)
gen_avm_ValueFlowMux_ValueNode = Generalization(general=ValueNode, specific=avm_ValueFlowMux)
gen_avm_modelica_Connector_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_modelica_Connector)
gen_avm_modelica_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Parameter)
gen_avm_modelica_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_modelica_Metric)
gen_avm_modelica_SolverSettings_Settings = Generalization(general=Settings, specific=avm_modelica_SolverSettings)
gen_avm_cad_CADModel_DomainModel = Generalization(general=DomainModel, specific=avm_cad_CADModel)
gen_avm_modelica_Redeclare_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Redeclare)
gen_avm_cad_Point_Datum = Generalization(general=Datum, specific=avm_cad_Point)
gen_avm_cad_Axis_Datum = Generalization(general=Datum, specific=avm_cad_Axis)
gen_avm_cad_Plane_Datum = Generalization(general=Datum, specific=avm_cad_Plane)
gen_avm_cad_CoordinateSystem_Datum = Generalization(general=Datum, specific=avm_cad_CoordinateSystem)
gen_avm_cad_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_cad_Metric)
gen_avm_cad_Geometry_AnalysisConstruct = Generalization(general=AnalysisConstruct, specific=avm_cad_Geometry)
gen_avm_cad_Geometry2D_Geometry = Generalization(general=Geometry, specific=avm_cad_Geometry2D)
gen_avm_cad_Geometry3D_Geometry = Generalization(general=Geometry, specific=avm_cad_Geometry3D)
gen_avm_cad_Circle_Geometry2D = Generalization(general=Geometry2D, specific=avm_cad_Circle)
gen_avm_cad_Polygon_Geometry2D = Generalization(general=Geometry2D, specific=avm_cad_Polygon)
gen_avm_cad_Datum_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_cad_Datum)
gen_avm_cad_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_cad_Parameter)
gen_avm_cad_Sphere_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_Sphere)
gen_avm_cad_CustomGeometry_Geometry = Generalization(general=Geometry, specific=avm_cad_CustomGeometry)
gen_avm_cad_RevoluteJointSpec_KinematicJointSpec = Generalization(general=KinematicJointSpec, specific=avm_cad_RevoluteJointSpec)
gen_avm_cad_ExtrudedGeometry_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_ExtrudedGeometry)
gen_avm_cad_Surface_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_Surface)
gen_avm_cad_GuideDatum_ConnectorFeature = Generalization(general=ConnectorFeature, specific=avm_cad_GuideDatum)
gen_avm_cad_AssemblyRoot_DesignDomainFeature = Generalization(general=DesignDomainFeature, specific=avm_cad_AssemblyRoot)
gen_avm_cad_KinematicJointSpec_ConnectorFeature = Generalization(general=ConnectorFeature, specific=avm_cad_KinematicJointSpec)
gen_avm_manufacturing_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_manufacturing_Metric)
gen_avm_cyber_CyberModel_DomainModel = Generalization(general=DomainModel, specific=avm_cyber_CyberModel)
gen_avm_cad_TranslationalJointSpec_KinematicJointSpec = Generalization(general=KinematicJointSpec, specific=avm_cad_TranslationalJointSpec)
gen_avm_manufacturing_ManufacturingModel_DomainModel = Generalization(general=DomainModel, specific=avm_manufacturing_ManufacturingModel)
gen_avm_manufacturing_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_manufacturing_Parameter)
gen_avm_adamsCar_AdamsCarModel_DomainModel = Generalization(general=DomainModel, specific=avm_adamsCar_AdamsCarModel)
gen_avm_adamsCar_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_adamsCar_Parameter)

# Domain Model
domain_model = DomainModel(
    name="avm",
    types={avm_Component, avm_DomainModel, avm_Property, avm_Resource, avm_Connector, avm_DistributionRestriction, avm_Port, avm_Formula, avm_Value, ValueNode, avm_ValueExpressionType, avm_DataSource, avm_FixedValue, ValueExpressionType, avm_CalculatedValue, avm_AnalysisConstruct, ConnectorCompositionTarget, avm_assemblyDetail, avm_ConnectorFeature, PortMapTarget, avm_DomainModelPort, Port, avm_DomainModelParameter, avm_DerivedValue, avm_ValueNode, avm_ParametricValue, avm_SecurityClassification, DistributionRestriction, avm_Proprietary, avm_ITAR, avm_DomainModelMetric, avm_UniformDistribution, avm_PrimitiveProperty, Property_, avm_ProbabilisticValue, avm_NormalDistribution, ProbabilisticValue, avm_AbstractPort, avm_Design, avm_Container, avm_DesignDomainFeature, avm_ComponentInstance, avm_CompoundProperty, avm_ParametricEnumeratedValue, avm_Alternative, avm_ValueFlowMux, avm_ComponentPortInstance, avm_ComponentPrimitivePropertyInstance, avm_ComponentConnectorInstance, avm_DesignSpaceContainer, avm_PortMapTarget, avm_Compound, Container, avm_Optional, DesignSpaceContainer, avm_SimpleFormula, Formula, avm_ComplexFormula, avm_Operand, avm_DoDDistributionStatement, avm_TestBench, avm_TopLevelSystemUnderTest, avm_ConnectorCompositionTarget, avm_Settings, ContainerInstanceBase, TestBenchValueBase, avm_ContainerInstanceBase, avm_TestBenchValueBase, avm_WorkflowTaskBase, avm_Parameter, avm_Metric, avm_TestInjectionPoint, avm_Workflow, avm_modelica_ModelicaModel, DomainModel, Parameter_, Connector, Metric, avm_InterpreterTask, WorkflowTaskBase, avm_ExecutionTask, Limit, Redeclare, avm_modelica_Connector, DomainModelPort, avm_modelica_Parameter, DomainModelParameter, modelica_avm_Value, avm_modelica_Metric, DomainModelMetric, avm_modelica_Limit, avm_modelica_SolverSettings, Settings, avm_cad_CADModel, Datum, avm_modelica_Redeclare, cad_avm_Value, avm_cad_Point, avm_cad_Axis, avm_cad_Plane, Plane, avm_cad_CoordinateSystem, avm_cad_Metric, avm_cad_Geometry, AnalysisConstruct, avm_cad_Geometry2D, Geometry, avm_cad_Geometry3D, avm_cad_Circle, Geometry2D, PointReference, avm_cad_Polygon, avm_cad_Datum, avm_cad_Parameter, avm_cad_Sphere, avm_cad_CustomGeometry, CustomGeometryInput, avm_cad_CustomGeometryInput, avm_cad_RevoluteJointSpec, KinematicJointSpec, Axis, avm_cad_ExtrudedGeometry, Geometry3D, avm_cad_TranslationalJointSpec, avm_cad_PointReference, Point, avm_cad_Surface, PlaneReference, avm_cad_PlaneReference, avm_cad_GuideDatum, ConnectorFeature, avm_cad_AssemblyRoot, DesignDomainFeature, cad_avm_ComponentInstance, avm_cad_KinematicJointSpec, avm_manufacturing_Metric, avm_cyber_CyberModel, avm_manufacturing_ManufacturingModel, avm_manufacturing_Parameter, manufacturing_avm_Value, avm_adamsCar_AdamsCarModel, FileReference, avm_adamsCar_Parameter, adamsCar_avm_Value, avm_adamsCar_FileReference, CalculationTypeEnum, DataTypeEnum, DimensionTypeEnum, SimpleFormulaOperation, DoDDistributionStatementEnum, RedeclareTypeEnum, IntervalMethod, JobManagerToolSelection, BoundTypeEnum, CustomGeometryInputOperationEnum, PartIntersectionEnum, GeometryQualifierEnum, ModelType},
    associations={DomainModel0, Property1, ResourceDependency3, Connector5, DistributionRestriction7, Port9, Formula13, UsesResource15, ValueExpression18, DataSource19, AnalysisConstruct11, Role22, Property25, DefaultJoin28, Connector31, ConnectorFeature33, ValueSource21, Default35, Maximum37, Minimum40, AssignedValue43, StandardDeviation48, Value51, Mean46, AssignedValue60, Enum61, FromResource64, RootContainer67, DomainFeature68, Container71, Property73, ComponentInstance76, Port78, Connector81, Value53, CompoundProperty56, PrimitiveProperty57, ValueFlowMux90, PortInstance91, PrimitivePropertyInstance93, ConnectorInstance95, Value97, PortMap101, JoinData84, Formula87, Operand107, Operand109, ValueSource110, TopLevelSystemUnderTest113, ConnectorComposition103, ApplyJoinData104, Workflow123, Settings125, TestStructure127, Value130, Task132, Parameter114, Metric116, TestInjectionPoint118, TestComponent120, Source134, Parameter137, Connector138, Metric140, Limit142, Redeclare144, Parameter146, Redeclare148, Value151, TargetValue152, Value154, Datum156, Parameter157, Value165, SurfaceReverseMap166, Metric167, CircleCenter169, CircleEdge170, PolygonPoint173, ModelMetric160, DatumMetric163, SphereCenter182, SphereEdge184, CustomGeometryInput187, AlignmentPlane196, AlignmentAxis198, RotationLimitReference200, MinimumRotation203, DefaultRotation206, MaximumRotation209, ExtrusionHeight175, InputGeometry188, ExtrusionSurface177, DirectionReferencePoint179, ReferredPoint189, ReferencePlane190, ReferredPlane191, Datum193, AssemblyRootComponentInstance195, Connector235, Parameter237, AlignmentPlane212, AlignmentAxis214, MinimumTranslation217, DefaultTranslation220, MaximumTranslation223, TranslationLimitReference226, Parameter229, Metric231, Value234, Parameter240, FileReference242, Value244, ParameterSwap245, FileReferenceSwap247},
    generalizations={gen_avm_Value_ValueNode, gen_avm_FixedValue_ValueExpressionType, gen_avm_CalculatedValue_ValueExpressionType, gen_avm_Connector_ConnectorCompositionTarget, gen_avm_Port_PortMapTarget, gen_avm_DomainModelPort_Port, gen_avm_DerivedValue_ValueExpressionType, gen_avm_ParametricValue_ValueExpressionType, gen_avm_SecurityClassification_DistributionRestriction, gen_avm_Proprietary_DistributionRestriction, gen_avm_ITAR_DistributionRestriction, gen_avm_UniformDistribution_ProbabilisticValue, gen_avm_ProbabilisticValue_ValueExpressionType, gen_avm_NormalDistribution_ProbabilisticValue, gen_avm_AbstractPort_Port, gen_avm_PrimitiveProperty_Property, gen_avm_CompoundProperty_Property, gen_avm_ParametricEnumeratedValue_ValueExpressionType, gen_avm_Alternative_DesignSpaceContainer, gen_avm_ComponentPortInstance_PortMapTarget, gen_avm_DesignSpaceContainer_Container, gen_avm_ComponentConnectorInstance_ConnectorCompositionTarget, gen_avm_Compound_Container, gen_avm_Optional_DesignSpaceContainer, gen_avm_SimpleFormula_Formula, gen_avm_ComplexFormula_Formula, gen_avm_DoDDistributionStatement_DistributionRestriction, gen_avm_Formula_ValueNode, gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase, gen_avm_Parameter_TestBenchValueBase, gen_avm_Metric_TestBenchValueBase, gen_avm_TestInjectionPoint_ContainerInstanceBase, gen_avm_modelica_ModelicaModel_DomainModel, gen_avm_InterpreterTask_WorkflowTaskBase, gen_avm_ExecutionTask_WorkflowTaskBase, gen_avm_ValueFlowMux_ValueNode, gen_avm_modelica_Connector_DomainModelPort, gen_avm_modelica_Parameter_DomainModelParameter, gen_avm_modelica_Metric_DomainModelMetric, gen_avm_modelica_SolverSettings_Settings, gen_avm_cad_CADModel_DomainModel, gen_avm_modelica_Redeclare_DomainModelParameter, gen_avm_cad_Point_Datum, gen_avm_cad_Axis_Datum, gen_avm_cad_Plane_Datum, gen_avm_cad_CoordinateSystem_Datum, gen_avm_cad_Metric_DomainModelMetric, gen_avm_cad_Geometry_AnalysisConstruct, gen_avm_cad_Geometry2D_Geometry, gen_avm_cad_Geometry3D_Geometry, gen_avm_cad_Circle_Geometry2D, gen_avm_cad_Polygon_Geometry2D, gen_avm_cad_Datum_DomainModelPort, gen_avm_cad_Parameter_DomainModelParameter, gen_avm_cad_Sphere_Geometry3D, gen_avm_cad_CustomGeometry_Geometry, gen_avm_cad_RevoluteJointSpec_KinematicJointSpec, gen_avm_cad_ExtrudedGeometry_Geometry3D, gen_avm_cad_Surface_Geometry3D, gen_avm_cad_GuideDatum_ConnectorFeature, gen_avm_cad_AssemblyRoot_DesignDomainFeature, gen_avm_cad_KinematicJointSpec_ConnectorFeature, gen_avm_manufacturing_Metric_DomainModelMetric, gen_avm_cyber_CyberModel_DomainModel, gen_avm_cad_TranslationalJointSpec_KinematicJointSpec, gen_avm_manufacturing_ManufacturingModel_DomainModel, gen_avm_manufacturing_Parameter_DomainModelParameter, gen_avm_adamsCar_AdamsCarModel_DomainModel, gen_avm_adamsCar_Parameter_DomainModelParameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)