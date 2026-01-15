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

CalculationTypeEnum: Enumeration = Enumeration(
    name="CalculationTypeEnum",
    literals={
            EnumerationLiteral(name="Python"),
			EnumerationLiteral(name="Declarative")
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

BoundTypeEnum: Enumeration = Enumeration(
    name="BoundTypeEnum",
    literals={
            EnumerationLiteral(name="MustNotExceed"),
			EnumerationLiteral(name="MustNotMeetOrExceed"),
			EnumerationLiteral(name="MustExceed"),
			EnumerationLiteral(name="MustExceedOrEqual")
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

FileFormat: Enumeration = Enumeration(
    name="FileFormat",
    literals={
            EnumerationLiteral(name="Creo"),
			EnumerationLiteral(name="AP_203"),
			EnumerationLiteral(name="AP_214"),
			EnumerationLiteral(name="STL")
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

LayerEnum: Enumeration = Enumeration(
    name="LayerEnum",
    literals={
            EnumerationLiteral(name="Top"),
			EnumerationLiteral(name="Bottom")
    }
)

LayerRangeEnum: Enumeration = Enumeration(
    name="LayerRangeEnum",
    literals={
            EnumerationLiteral(name="Either"),
			EnumerationLiteral(name="Top"),
			EnumerationLiteral(name="Bottom")
    }
)

RelativeLayerEnum: Enumeration = Enumeration(
    name="RelativeLayerEnum",
    literals={
            EnumerationLiteral(name="Same"),
			EnumerationLiteral(name="Opposite")
    }
)

RangeConstraintTypeEnum: Enumeration = Enumeration(
    name="RangeConstraintTypeEnum",
    literals={
            EnumerationLiteral(name="Inclusion"),
			EnumerationLiteral(name="Exclusion")
    }
)

RelativeRotationEnum: Enumeration = Enumeration(
    name="RelativeRotationEnum",
    literals={
            EnumerationLiteral(name="r0"),
			EnumerationLiteral(name="r90"),
			EnumerationLiteral(name="r180"),
			EnumerationLiteral(name="r270"),
			EnumerationLiteral(name="NoRestriction")
    }
)

SystemCDataTypeEnum: Enumeration = Enumeration(
    name="SystemCDataTypeEnum",
    literals={
            EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="sc_int"),
			EnumerationLiteral(name="sc_uint"),
			EnumerationLiteral(name="sc_logic"),
			EnumerationLiteral(name="sc_bit")
    }
)

GlobalConstraintTypeEnum: Enumeration = Enumeration(
    name="GlobalConstraintTypeEnum",
    literals={
            EnumerationLiteral(name="BoardEdgeSpacing")
    }
)

DirectionalityEnum: Enumeration = Enumeration(
    name="DirectionalityEnum",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="not_applicable")
    }
)

FunctionEnum: Enumeration = Enumeration(
    name="FunctionEnum",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="clock"),
			EnumerationLiteral(name="reset_async"),
			EnumerationLiteral(name="reset_sync")
    }
)

RotationEnum: Enumeration = Enumeration(
    name="RotationEnum",
    literals={
            EnumerationLiteral(name="r0"),
			EnumerationLiteral(name="r90"),
			EnumerationLiteral(name="r180"),
			EnumerationLiteral(name="r270")
    }
)

PortDirectionality: Enumeration = Enumeration(
    name="PortDirectionality",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="out")
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
avm_AnalysisConstruct = Class(name="avm::AnalysisConstruct", is_abstract=True)
avm_Formula = Class(name="avm::Formula", is_abstract=True)
avm_DomainMapping = Class(name="avm::DomainMapping", is_abstract=True)
avm_Value = Class(name="avm::Value")
ValueNode = Class(name="ValueNode")
avm_ValueExpressionType = Class(name="avm::ValueExpressionType", is_abstract=True)
avm_DataSource = Class(name="avm::DataSource")
avm_FixedValue = Class(name="avm::FixedValue")
ValueExpressionType = Class(name="ValueExpressionType")
avm_CalculatedValue = Class(name="avm::CalculatedValue")
avm_DerivedValue = Class(name="avm::DerivedValue")
avm_ValueNode = Class(name="avm::ValueNode", is_abstract=True)
ConnectorCompositionTarget = Class(name="ConnectorCompositionTarget")
avm_assemblyDetail = Class(name="avm::assemblyDetail")
avm_ConnectorFeature = Class(name="avm::ConnectorFeature", is_abstract=True)
PortMapTarget = Class(name="PortMapTarget")
avm_DomainModelPort = Class(name="avm::DomainModelPort", is_abstract=True)
Port = Class(name="Port")
avm_DomainModelParameter = Class(name="avm::DomainModelParameter", is_abstract=True)
avm_ParametricValue = Class(name="avm::ParametricValue")
avm_ProbabilisticValue = Class(name="avm::ProbabilisticValue", is_abstract=True)
avm_NormalDistribution = Class(name="avm::NormalDistribution")
ProbabilisticValue = Class(name="ProbabilisticValue")
avm_SecurityClassification = Class(name="avm::SecurityClassification")
DistributionRestriction = Class(name="DistributionRestriction")
avm_Proprietary = Class(name="avm::Proprietary")
avm_ITAR = Class(name="avm::ITAR")
avm_DomainModelMetric = Class(name="avm::DomainModelMetric", is_abstract=True)
avm_UniformDistribution = Class(name="avm::UniformDistribution")
avm_PrimitiveProperty = Class(name="avm::PrimitiveProperty")
Property_ = Class(name="Property")
avm_CompoundProperty = Class(name="avm::CompoundProperty")
avm_ParametricEnumeratedValue = Class(name="avm::ParametricEnumeratedValue")
avm_AbstractPort = Class(name="avm::AbstractPort")
avm_Design = Class(name="avm::Design")
avm_Container = Class(name="avm::Container", is_abstract=True)
avm_DesignDomainFeature = Class(name="avm::DesignDomainFeature", is_abstract=True)
avm_ComponentInstance = Class(name="avm::ComponentInstance")
avm_ContainerFeature = Class(name="avm::ContainerFeature", is_abstract=True)
avm_Compound = Class(name="avm::Compound")
Container = Class(name="Container")
avm_Optional = Class(name="avm::Optional")
DesignSpaceContainer = Class(name="DesignSpaceContainer")
avm_Alternative = Class(name="avm::Alternative")
avm_ValueFlowMux = Class(name="avm::ValueFlowMux")
avm_ComponentPortInstance = Class(name="avm::ComponentPortInstance")
avm_ComponentPrimitivePropertyInstance = Class(name="avm::ComponentPrimitivePropertyInstance")
avm_ComponentConnectorInstance = Class(name="avm::ComponentConnectorInstance")
avm_DesignSpaceContainer = Class(name="avm::DesignSpaceContainer", is_abstract=True)
avm_PortMapTarget = Class(name="avm::PortMapTarget")
avm_ConnectorCompositionTarget = Class(name="avm::ConnectorCompositionTarget")
avm_SimpleFormula = Class(name="avm::SimpleFormula")
Formula = Class(name="Formula")
avm_ComplexFormula = Class(name="avm::ComplexFormula")
avm_Operand = Class(name="avm::Operand")
avm_DoDDistributionStatement = Class(name="avm::DoDDistributionStatement")
avm_TestBench = Class(name="avm::TestBench")
avm_TopLevelSystemUnderTest = Class(name="avm::TopLevelSystemUnderTest")
avm_Parameter = Class(name="avm::Parameter")
avm_Metric = Class(name="avm::Metric")
avm_TestInjectionPoint = Class(name="avm::TestInjectionPoint")
avm_Workflow = Class(name="avm::Workflow")
avm_Settings = Class(name="avm::Settings", is_abstract=True)
ContainerInstanceBase = Class(name="ContainerInstanceBase")
TestBenchValueBase = Class(name="TestBenchValueBase")
avm_ContainerInstanceBase = Class(name="avm::ContainerInstanceBase", is_abstract=True)
avm_TestBenchValueBase = Class(name="avm::TestBenchValueBase", is_abstract=True)
avm_WorkflowTaskBase = Class(name="avm::WorkflowTaskBase", is_abstract=True)
avm_ExecutionTask = Class(name="avm::ExecutionTask")
avm_modelica_ModelicaModel = Class(name="avm::modelica::ModelicaModel")
DomainModel = Class(name="DomainModel")
avm_InterpreterTask = Class(name="avm::InterpreterTask")
WorkflowTaskBase = Class(name="WorkflowTaskBase")
Connector = Class(name="Connector")
Metric = Class(name="Metric")
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
avm_modelica_Redeclare = Class(name="avm::modelica::Redeclare")
Parameter_ = Class(name="Parameter")
avm_modelica_SolverSettings = Class(name="avm::modelica::SolverSettings")
Settings = Class(name="Settings")
avm_cad_CADModel = Class(name="avm::cad::CADModel")
Datum = Class(name="Datum")
avm_cad_Datum = Class(name="avm::cad::Datum", is_abstract=True)
avm_cad_Parameter = Class(name="avm::cad::Parameter")
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
avm_cad_ExtrudedGeometry = Class(name="avm::cad::ExtrudedGeometry")
Geometry3D = Class(name="Geometry3D")
avm_cad_Sphere = Class(name="avm::cad::Sphere")
avm_cad_CustomGeometry = Class(name="avm::cad::CustomGeometry")
CustomGeometryInput = Class(name="CustomGeometryInput")
avm_cad_CustomGeometryInput = Class(name="avm::cad::CustomGeometryInput")
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
avm_cad_RevoluteJointSpec = Class(name="avm::cad::RevoluteJointSpec")
KinematicJointSpec = Class(name="KinematicJointSpec")
Axis = Class(name="Axis")
avm_cad_TranslationalJointSpec = Class(name="avm::cad::TranslationalJointSpec")
avm_manufacturing_ManufacturingModel = Class(name="avm::manufacturing::ManufacturingModel")
avm_manufacturing_Parameter = Class(name="avm::manufacturing::Parameter")
manufacturing_avm_Value = Class(name="manufacturing::avm::Value")
avm_manufacturing_Metric = Class(name="avm::manufacturing::Metric")
avm_cyber_CyberModel = Class(name="avm::cyber::CyberModel")
avm_schematic_SchematicModel = Class(name="avm::schematic::SchematicModel", is_abstract=True)
Pin = Class(name="Pin")
avm_schematic_Pin = Class(name="avm::schematic::Pin")
avm_eda_EDAModel = Class(name="avm::eda::EDAModel")
SchematicModel = Class(name="SchematicModel")
avm_eda_Parameter = Class(name="avm::eda::Parameter")
eda_avm_Value = Class(name="eda::avm::Value")
avm_eda_PcbLayoutConstraint = Class(name="avm::eda::PcbLayoutConstraint", is_abstract=True)
ContainerFeature = Class(name="ContainerFeature")
avm_eda_ExactLayoutConstraint = Class(name="avm::eda::ExactLayoutConstraint")
PcbLayoutConstraint = Class(name="PcbLayoutConstraint")
eda_avm_ComponentInstance = Class(name="eda::avm::ComponentInstance")
eda_avm_Container = Class(name="eda::avm::Container")
avm_eda_RangeLayoutConstraint = Class(name="avm::eda::RangeLayoutConstraint")
avm_eda_RelativeLayoutConstraint = Class(name="avm::eda::RelativeLayoutConstraint")
eda_Parameter = Class(name="eda::Parameter")
avm_eda_RelativeRangeLayoutConstraint = Class(name="avm::eda::RelativeRangeLayoutConstraint")
avm_eda_GlobalLayoutConstraintException = Class(name="avm::eda::GlobalLayoutConstraintException")
avm_eda_CircuitLayout = Class(name="avm::eda::CircuitLayout")
avm_spice_SPICEModel = Class(name="avm::spice::SPICEModel")
spice_Parameter = Class(name="spice::Parameter")
avm_spice_Parameter = Class(name="avm::spice::Parameter")
spice_avm_Value = Class(name="spice::avm::Value")
avm_systemc_SystemCModel = Class(name="avm::systemc::SystemCModel")
SystemCPort = Class(name="SystemCPort")
avm_systemc_Parameter = Class(name="avm::systemc::Parameter")
systemc_avm_Value = Class(name="systemc::avm::Value")
avm_systemc_SystemCPort = Class(name="avm::systemc::SystemCPort")
avm_rf_RFModel = Class(name="avm::rf::RFModel")
RFPort = Class(name="RFPort")
avm_rf_RFPort = Class(name="avm::rf::RFPort")
avm_domainmapping_CAD2EDATransform = Class(name="avm::domainmapping::CAD2EDATransform")
DomainMapping = Class(name="DomainMapping")
eda_EDAModel = Class(name="eda::EDAModel")
CADModel = Class(name="CADModel")

# avm_Component class attributes and methods
avm_Component_Name: Property = Property(name="Name", type=StringType)
avm_Component_Version: Property = Property(name="Version", type=StringType)
avm_Component_SchemaVersion: Property = Property(name="SchemaVersion", type=StringType)
avm_Component_Classifications: Property = Property(name="Classifications", type=StringType)
avm_Component_ID: Property = Property(name="ID", type=StringType)
avm_Component_Supercedes: Property = Property(name="Supercedes", type=StringType)
avm_Component.attributes={avm_Component_Supercedes, avm_Component_SchemaVersion, avm_Component_Version, avm_Component_Name, avm_Component_ID, avm_Component_Classifications}

# avm_DomainModel class attributes and methods
avm_DomainModel_Author: Property = Property(name="Author", type=StringType)
avm_DomainModel_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModel_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModel_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModel_Name: Property = Property(name="Name", type=StringType)
avm_DomainModel_ID: Property = Property(name="ID", type=StringType)
avm_DomainModel.attributes={avm_DomainModel_XPosition, avm_DomainModel_Name, avm_DomainModel_ID, avm_DomainModel_Notes, avm_DomainModel_Author, avm_DomainModel_YPosition}

# avm_Property class attributes and methods
avm_Property_Name: Property = Property(name="Name", type=StringType)
avm_Property_OnDataSheet: Property = Property(name="OnDataSheet", type=StringType)
avm_Property_Notes: Property = Property(name="Notes", type=StringType)
avm_Property_Definition: Property = Property(name="Definition", type=StringType)
avm_Property_ID: Property = Property(name="ID", type=StringType)
avm_Property_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Property_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Property.attributes={avm_Property_XPosition, avm_Property_Notes, avm_Property_ID, avm_Property_YPosition, avm_Property_OnDataSheet, avm_Property_Definition, avm_Property_Name}

# avm_Resource class attributes and methods
avm_Resource_Name: Property = Property(name="Name", type=StringType)
avm_Resource_Path: Property = Property(name="Path", type=StringType)
avm_Resource_Hash: Property = Property(name="Hash", type=StringType)
avm_Resource_ID: Property = Property(name="ID", type=StringType)
avm_Resource_Notes: Property = Property(name="Notes", type=StringType)
avm_Resource_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Resource_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Resource.attributes={avm_Resource_Path, avm_Resource_XPosition, avm_Resource_Hash, avm_Resource_Notes, avm_Resource_YPosition, avm_Resource_Name, avm_Resource_ID}

# avm_Connector class attributes and methods
avm_Connector_Definition: Property = Property(name="Definition", type=StringType)
avm_Connector_Name: Property = Property(name="Name", type=StringType)
avm_Connector_Notes: Property = Property(name="Notes", type=StringType)
avm_Connector_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Connector_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Connector.attributes={avm_Connector_YPosition, avm_Connector_XPosition, avm_Connector_Definition, avm_Connector_Name, avm_Connector_Notes}

# avm_DistributionRestriction class attributes and methods
avm_DistributionRestriction_Notes: Property = Property(name="Notes", type=StringType)
avm_DistributionRestriction.attributes={avm_DistributionRestriction_Notes}

# avm_Port class attributes and methods
avm_Port_Notes: Property = Property(name="Notes", type=StringType)
avm_Port_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Port_Definition: Property = Property(name="Definition", type=StringType)
avm_Port_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Port_Name: Property = Property(name="Name", type=StringType)
avm_Port.attributes={avm_Port_Notes, avm_Port_Name, avm_Port_XPosition, avm_Port_Definition, avm_Port_YPosition}

# avm_AnalysisConstruct class attributes and methods

# avm_Formula class attributes and methods
avm_Formula_Name: Property = Property(name="Name", type=StringType)
avm_Formula_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Formula_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Formula.attributes={avm_Formula_Name, avm_Formula_XPosition, avm_Formula_YPosition}

# avm_DomainMapping class attributes and methods

# avm_Value class attributes and methods
avm_Value_DimensionType: Property = Property(name="DimensionType", type=StringType)
avm_Value_DataType: Property = Property(name="DataType", type=StringType)
avm_Value_Dimensions: Property = Property(name="Dimensions", type=StringType)
avm_Value_Unit: Property = Property(name="Unit", type=StringType)
avm_Value.attributes={avm_Value_Dimensions, avm_Value_Unit, avm_Value_DimensionType, avm_Value_DataType}

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

# avm_DerivedValue class attributes and methods

# avm_ValueNode class attributes and methods
avm_ValueNode_ID: Property = Property(name="ID", type=StringType)
avm_ValueNode.attributes={avm_ValueNode_ID}

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
avm_DomainModelParameter.attributes={avm_DomainModelParameter_YPosition, avm_DomainModelParameter_XPosition, avm_DomainModelParameter_Notes}

# avm_ParametricValue class attributes and methods

# avm_ProbabilisticValue class attributes and methods

# avm_NormalDistribution class attributes and methods

# ProbabilisticValue class attributes and methods

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
avm_DomainModelMetric.attributes={avm_DomainModelMetric_XPosition, avm_DomainModelMetric_ID, avm_DomainModelMetric_Notes, avm_DomainModelMetric_YPosition}

# avm_UniformDistribution class attributes and methods

# avm_PrimitiveProperty class attributes and methods

# Property class attributes and methods

# avm_CompoundProperty class attributes and methods

# avm_ParametricEnumeratedValue class attributes and methods

# avm_AbstractPort class attributes and methods

# avm_Design class attributes and methods
avm_Design_SchemaVersion: Property = Property(name="SchemaVersion", type=StringType)
avm_Design_DesignID: Property = Property(name="DesignID", type=StringType)
avm_Design_Name: Property = Property(name="Name", type=StringType)
avm_Design_DesignSpaceSrcID: Property = Property(name="DesignSpaceSrcID", type=StringType)
avm_Design.attributes={avm_Design_SchemaVersion, avm_Design_DesignID, avm_Design_Name, avm_Design_DesignSpaceSrcID}

# avm_Container class attributes and methods
avm_Container_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Container_Name: Property = Property(name="Name", type=StringType)
avm_Container_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Container_ID: Property = Property(name="ID", type=StringType)
avm_Container_Description: Property = Property(name="Description", type=StringType)
avm_Container.attributes={avm_Container_Description, avm_Container_XPosition, avm_Container_YPosition, avm_Container_ID, avm_Container_Name}

# avm_DesignDomainFeature class attributes and methods

# avm_ComponentInstance class attributes and methods
avm_ComponentInstance_ComponentID: Property = Property(name="ComponentID", type=StringType)
avm_ComponentInstance_ID: Property = Property(name="ID", type=StringType)
avm_ComponentInstance_Name: Property = Property(name="Name", type=StringType)
avm_ComponentInstance_DesignSpaceSrcComponentID: Property = Property(name="DesignSpaceSrcComponentID", type=StringType)
avm_ComponentInstance_XPosition: Property = Property(name="XPosition", type=StringType)
avm_ComponentInstance_YPosition: Property = Property(name="YPosition", type=StringType)
avm_ComponentInstance.attributes={avm_ComponentInstance_ComponentID, avm_ComponentInstance_DesignSpaceSrcComponentID, avm_ComponentInstance_YPosition, avm_ComponentInstance_ID, avm_ComponentInstance_Name, avm_ComponentInstance_XPosition}

# avm_ContainerFeature class attributes and methods

# avm_Compound class attributes and methods

# Container class attributes and methods

# avm_Optional class attributes and methods

# DesignSpaceContainer class attributes and methods

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

# avm_ConnectorCompositionTarget class attributes and methods
avm_ConnectorCompositionTarget_ID: Property = Property(name="ID", type=StringType)
avm_ConnectorCompositionTarget.attributes={avm_ConnectorCompositionTarget_ID}

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

# avm_Parameter class attributes and methods

# avm_Metric class attributes and methods

# avm_TestInjectionPoint class attributes and methods

# avm_Workflow class attributes and methods
avm_Workflow_Name: Property = Property(name="Name", type=StringType)
avm_Workflow.attributes={avm_Workflow_Name}

# avm_Settings class attributes and methods

# ContainerInstanceBase class attributes and methods

# TestBenchValueBase class attributes and methods

# avm_ContainerInstanceBase class attributes and methods
avm_ContainerInstanceBase_IDinSourceModel: Property = Property(name="IDinSourceModel", type=StringType)
avm_ContainerInstanceBase_XPosition: Property = Property(name="XPosition", type=StringType)
avm_ContainerInstanceBase_YPosition: Property = Property(name="YPosition", type=StringType)
avm_ContainerInstanceBase.attributes={avm_ContainerInstanceBase_YPosition, avm_ContainerInstanceBase_IDinSourceModel, avm_ContainerInstanceBase_XPosition}

# avm_TestBenchValueBase class attributes and methods
avm_TestBenchValueBase_ID: Property = Property(name="ID", type=StringType)
avm_TestBenchValueBase_Name: Property = Property(name="Name", type=StringType)
avm_TestBenchValueBase_Notes: Property = Property(name="Notes", type=StringType)
avm_TestBenchValueBase_XPosition: Property = Property(name="XPosition", type=StringType)
avm_TestBenchValueBase_YPosition: Property = Property(name="YPosition", type=StringType)
avm_TestBenchValueBase.attributes={avm_TestBenchValueBase_YPosition, avm_TestBenchValueBase_XPosition, avm_TestBenchValueBase_Name, avm_TestBenchValueBase_Notes, avm_TestBenchValueBase_ID}

# avm_WorkflowTaskBase class attributes and methods
avm_WorkflowTaskBase_Name: Property = Property(name="Name", type=StringType)
avm_WorkflowTaskBase.attributes={avm_WorkflowTaskBase_Name}

# avm_ExecutionTask class attributes and methods
avm_ExecutionTask_Description: Property = Property(name="Description", type=StringType)
avm_ExecutionTask_Invocation: Property = Property(name="Invocation", type=StringType)
avm_ExecutionTask.attributes={avm_ExecutionTask_Invocation, avm_ExecutionTask_Description}

# avm_modelica_ModelicaModel class attributes and methods
avm_modelica_ModelicaModel_Class: Property = Property(name="Class", type=StringType)
avm_modelica_ModelicaModel.attributes={avm_modelica_ModelicaModel_Class}

# DomainModel class attributes and methods

# avm_InterpreterTask class attributes and methods
avm_InterpreterTask_COMName: Property = Property(name="COMName", type=StringType)
avm_InterpreterTask_Parameters: Property = Property(name="Parameters", type=StringType)
avm_InterpreterTask.attributes={avm_InterpreterTask_COMName, avm_InterpreterTask_Parameters}

# WorkflowTaskBase class attributes and methods

# Connector class attributes and methods

# Metric class attributes and methods

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
avm_modelica_Limit.attributes={avm_modelica_Limit_Name, avm_modelica_Limit_VariableLocator, avm_modelica_Limit_BoundType, avm_modelica_Limit_ToleranceTimeWindow, avm_modelica_Limit_Notes}

# avm_modelica_Redeclare class attributes and methods
avm_modelica_Redeclare_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Redeclare_Type: Property = Property(name="Type", type=StringType)
avm_modelica_Redeclare.attributes={avm_modelica_Redeclare_Locator, avm_modelica_Redeclare_Type}

# Parameter class attributes and methods

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
avm_modelica_SolverSettings.attributes={avm_modelica_SolverSettings_IntervalMethod, avm_modelica_SolverSettings_NumberOfIntervals, avm_modelica_SolverSettings_JobManagerToolSelection, avm_modelica_SolverSettings_IntervalLength, avm_modelica_SolverSettings_Solver, avm_modelica_SolverSettings_StartTime, avm_modelica_SolverSettings_StopTime, avm_modelica_SolverSettings_ToolSpecificAnnotations, avm_modelica_SolverSettings_Tolerance}

# Settings class attributes and methods

# avm_cad_CADModel class attributes and methods
avm_cad_CADModel_Format: Property = Property(name="Format", type=StringType)
avm_cad_CADModel.attributes={avm_cad_CADModel_Format}

# Datum class attributes and methods

# avm_cad_Datum class attributes and methods
avm_cad_Datum_DatumName: Property = Property(name="DatumName", type=StringType)
avm_cad_Datum.attributes={avm_cad_Datum_DatumName}

# avm_cad_Parameter class attributes and methods
avm_cad_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_cad_Parameter.attributes={avm_cad_Parameter_Name}

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
avm_cad_Geometry.attributes={avm_cad_Geometry_GeometryQualifier, avm_cad_Geometry_PartIntersectionModifier}

# AnalysisConstruct class attributes and methods

# avm_cad_Geometry2D class attributes and methods

# Geometry class attributes and methods

# avm_cad_Geometry3D class attributes and methods

# avm_cad_Circle class attributes and methods

# Geometry2D class attributes and methods

# PointReference class attributes and methods

# avm_cad_Polygon class attributes and methods

# avm_cad_ExtrudedGeometry class attributes and methods

# Geometry3D class attributes and methods

# avm_cad_Sphere class attributes and methods

# avm_cad_CustomGeometry class attributes and methods

# CustomGeometryInput class attributes and methods

# avm_cad_CustomGeometryInput class attributes and methods
avm_cad_CustomGeometryInput_Operation: Property = Property(name="Operation", type=StringType)
avm_cad_CustomGeometryInput.attributes={avm_cad_CustomGeometryInput_Operation}

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

# avm_cad_RevoluteJointSpec class attributes and methods

# KinematicJointSpec class attributes and methods

# Axis class attributes and methods

# avm_cad_TranslationalJointSpec class attributes and methods

# avm_manufacturing_ManufacturingModel class attributes and methods

# avm_manufacturing_Parameter class attributes and methods
avm_manufacturing_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_manufacturing_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_manufacturing_Parameter.attributes={avm_manufacturing_Parameter_Locator, avm_manufacturing_Parameter_Name}

# manufacturing_avm_Value class attributes and methods

# avm_manufacturing_Metric class attributes and methods
avm_manufacturing_Metric_Name: Property = Property(name="Name", type=StringType)
avm_manufacturing_Metric.attributes={avm_manufacturing_Metric_Name}

# avm_cyber_CyberModel class attributes and methods
avm_cyber_CyberModel_Type: Property = Property(name="Type", type=StringType)
avm_cyber_CyberModel_Class: Property = Property(name="Class", type=StringType)
avm_cyber_CyberModel_Locator: Property = Property(name="Locator", type=StringType)
avm_cyber_CyberModel.attributes={avm_cyber_CyberModel_Locator, avm_cyber_CyberModel_Type, avm_cyber_CyberModel_Class}

# avm_schematic_SchematicModel class attributes and methods

# Pin class attributes and methods

# avm_schematic_Pin class attributes and methods
avm_schematic_Pin_EDAGate: Property = Property(name="EDAGate", type=StringType)
avm_schematic_Pin_EDASymbolLocationX: Property = Property(name="EDASymbolLocationX", type=StringType)
avm_schematic_Pin_EDASymbolLocationY: Property = Property(name="EDASymbolLocationY", type=StringType)
avm_schematic_Pin_EDASymbolRotation: Property = Property(name="EDASymbolRotation", type=StringType)
avm_schematic_Pin_SPICEPortNumber: Property = Property(name="SPICEPortNumber", type=StringType)
avm_schematic_Pin.attributes={avm_schematic_Pin_EDASymbolRotation, avm_schematic_Pin_EDASymbolLocationX, avm_schematic_Pin_SPICEPortNumber, avm_schematic_Pin_EDASymbolLocationY, avm_schematic_Pin_EDAGate}

# avm_eda_EDAModel class attributes and methods
avm_eda_EDAModel_Library: Property = Property(name="Library", type=StringType)
avm_eda_EDAModel_DeviceSet: Property = Property(name="DeviceSet", type=StringType)
avm_eda_EDAModel_Device: Property = Property(name="Device", type=StringType)
avm_eda_EDAModel_Package: Property = Property(name="Package", type=StringType)
avm_eda_EDAModel_HasMultiLayerFootprint: Property = Property(name="HasMultiLayerFootprint", type=StringType)
avm_eda_EDAModel.attributes={avm_eda_EDAModel_Library, avm_eda_EDAModel_Device, avm_eda_EDAModel_DeviceSet, avm_eda_EDAModel_Package, avm_eda_EDAModel_HasMultiLayerFootprint}

# SchematicModel class attributes and methods

# avm_eda_Parameter class attributes and methods
avm_eda_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_eda_Parameter.attributes={avm_eda_Parameter_Locator}

# eda_avm_Value class attributes and methods

# avm_eda_PcbLayoutConstraint class attributes and methods
avm_eda_PcbLayoutConstraint_XPosition: Property = Property(name="XPosition", type=StringType)
avm_eda_PcbLayoutConstraint_YPosition: Property = Property(name="YPosition", type=StringType)
avm_eda_PcbLayoutConstraint_Notes: Property = Property(name="Notes", type=StringType)
avm_eda_PcbLayoutConstraint.attributes={avm_eda_PcbLayoutConstraint_XPosition, avm_eda_PcbLayoutConstraint_YPosition, avm_eda_PcbLayoutConstraint_Notes}

# ContainerFeature class attributes and methods

# avm_eda_ExactLayoutConstraint class attributes and methods
avm_eda_ExactLayoutConstraint_X: Property = Property(name="X", type=StringType)
avm_eda_ExactLayoutConstraint_Y: Property = Property(name="Y", type=StringType)
avm_eda_ExactLayoutConstraint_Layer: Property = Property(name="Layer", type=StringType)
avm_eda_ExactLayoutConstraint_Rotation: Property = Property(name="Rotation", type=StringType)
avm_eda_ExactLayoutConstraint.attributes={avm_eda_ExactLayoutConstraint_Layer, avm_eda_ExactLayoutConstraint_Y, avm_eda_ExactLayoutConstraint_Rotation, avm_eda_ExactLayoutConstraint_X}

# PcbLayoutConstraint class attributes and methods

# eda_avm_ComponentInstance class attributes and methods

# eda_avm_Container class attributes and methods

# avm_eda_RangeLayoutConstraint class attributes and methods
avm_eda_RangeLayoutConstraint_XRangeMin: Property = Property(name="XRangeMin", type=StringType)
avm_eda_RangeLayoutConstraint_XRangeMax: Property = Property(name="XRangeMax", type=StringType)
avm_eda_RangeLayoutConstraint_YRangeMin: Property = Property(name="YRangeMin", type=StringType)
avm_eda_RangeLayoutConstraint_YRangeMax: Property = Property(name="YRangeMax", type=StringType)
avm_eda_RangeLayoutConstraint_LayerRange: Property = Property(name="LayerRange", type=StringType)
avm_eda_RangeLayoutConstraint_Type: Property = Property(name="Type", type=StringType)
avm_eda_RangeLayoutConstraint.attributes={avm_eda_RangeLayoutConstraint_XRangeMin, avm_eda_RangeLayoutConstraint_XRangeMax, avm_eda_RangeLayoutConstraint_YRangeMax, avm_eda_RangeLayoutConstraint_YRangeMin, avm_eda_RangeLayoutConstraint_Type, avm_eda_RangeLayoutConstraint_LayerRange}

# avm_eda_RelativeLayoutConstraint class attributes and methods
avm_eda_RelativeLayoutConstraint_XOffset: Property = Property(name="XOffset", type=StringType)
avm_eda_RelativeLayoutConstraint_YOffset: Property = Property(name="YOffset", type=StringType)
avm_eda_RelativeLayoutConstraint_RelativeLayer: Property = Property(name="RelativeLayer", type=StringType)
avm_eda_RelativeLayoutConstraint_RelativeRotation: Property = Property(name="RelativeRotation", type=StringType)
avm_eda_RelativeLayoutConstraint.attributes={avm_eda_RelativeLayoutConstraint_RelativeLayer, avm_eda_RelativeLayoutConstraint_YOffset, avm_eda_RelativeLayoutConstraint_XOffset, avm_eda_RelativeLayoutConstraint_RelativeRotation}

# eda_Parameter class attributes and methods

# avm_eda_RelativeRangeLayoutConstraint class attributes and methods
avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMin: Property = Property(name="XRelativeRangeMin", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMax: Property = Property(name="XRelativeRangeMax", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMin: Property = Property(name="YRelativeRangeMin", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMax: Property = Property(name="YRelativeRangeMax", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_RelativeLayer: Property = Property(name="RelativeLayer", type=StringType)
avm_eda_RelativeRangeLayoutConstraint.attributes={avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMin, avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMax, avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMax, avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMin, avm_eda_RelativeRangeLayoutConstraint_RelativeLayer}

# avm_eda_GlobalLayoutConstraintException class attributes and methods
avm_eda_GlobalLayoutConstraintException_Constraint: Property = Property(name="Constraint", type=StringType)
avm_eda_GlobalLayoutConstraintException.attributes={avm_eda_GlobalLayoutConstraintException_Constraint}

# avm_eda_CircuitLayout class attributes and methods
avm_eda_CircuitLayout_BoundingBoxes: Property = Property(name="BoundingBoxes", type=StringType)
avm_eda_CircuitLayout.attributes={avm_eda_CircuitLayout_BoundingBoxes}

# avm_spice_SPICEModel class attributes and methods
avm_spice_SPICEModel_Class: Property = Property(name="Class", type=StringType)
avm_spice_SPICEModel.attributes={avm_spice_SPICEModel_Class}

# spice_Parameter class attributes and methods

# avm_spice_Parameter class attributes and methods
avm_spice_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_spice_Parameter.attributes={avm_spice_Parameter_Locator}

# spice_avm_Value class attributes and methods

# avm_systemc_SystemCModel class attributes and methods
avm_systemc_SystemCModel_ModuleName: Property = Property(name="ModuleName", type=StringType)
avm_systemc_SystemCModel.attributes={avm_systemc_SystemCModel_ModuleName}

# SystemCPort class attributes and methods

# avm_systemc_Parameter class attributes and methods
avm_systemc_Parameter_ParamName: Property = Property(name="ParamName", type=StringType)
avm_systemc_Parameter_ParamPosition: Property = Property(name="ParamPosition", type=StringType)
avm_systemc_Parameter.attributes={avm_systemc_Parameter_ParamPosition, avm_systemc_Parameter_ParamName}

# systemc_avm_Value class attributes and methods

# avm_systemc_SystemCPort class attributes and methods
avm_systemc_SystemCPort_DataType: Property = Property(name="DataType", type=StringType)
avm_systemc_SystemCPort_DataTypeDimension: Property = Property(name="DataTypeDimension", type=StringType)
avm_systemc_SystemCPort_Directionality: Property = Property(name="Directionality", type=StringType)
avm_systemc_SystemCPort_Function: Property = Property(name="Function", type=StringType)
avm_systemc_SystemCPort.attributes={avm_systemc_SystemCPort_Function, avm_systemc_SystemCPort_Directionality, avm_systemc_SystemCPort_DataTypeDimension, avm_systemc_SystemCPort_DataType}

# avm_rf_RFModel class attributes and methods
avm_rf_RFModel_Rotation: Property = Property(name="Rotation", type=StringType)
avm_rf_RFModel_X: Property = Property(name="X", type=StringType)
avm_rf_RFModel_Y: Property = Property(name="Y", type=StringType)
avm_rf_RFModel.attributes={avm_rf_RFModel_X, avm_rf_RFModel_Rotation, avm_rf_RFModel_Y}

# RFPort class attributes and methods

# avm_rf_RFPort class attributes and methods
avm_rf_RFPort_Directionality: Property = Property(name="Directionality", type=StringType)
avm_rf_RFPort_NominalImpedance: Property = Property(name="NominalImpedance", type=StringType)
avm_rf_RFPort.attributes={avm_rf_RFPort_Directionality, avm_rf_RFPort_NominalImpedance}

# avm_domainmapping_CAD2EDATransform class attributes and methods
avm_domainmapping_CAD2EDATransform_RotationX: Property = Property(name="RotationX", type=StringType)
avm_domainmapping_CAD2EDATransform_RotationY: Property = Property(name="RotationY", type=StringType)
avm_domainmapping_CAD2EDATransform_RotationZ: Property = Property(name="RotationZ", type=StringType)
avm_domainmapping_CAD2EDATransform_TranslationX: Property = Property(name="TranslationX", type=StringType)
avm_domainmapping_CAD2EDATransform_TranslationY: Property = Property(name="TranslationY", type=StringType)
avm_domainmapping_CAD2EDATransform_TranslationZ: Property = Property(name="TranslationZ", type=StringType)
avm_domainmapping_CAD2EDATransform_ScaleX: Property = Property(name="ScaleX", type=StringType)
avm_domainmapping_CAD2EDATransform_ScaleY: Property = Property(name="ScaleY", type=StringType)
avm_domainmapping_CAD2EDATransform_ScaleZ: Property = Property(name="ScaleZ", type=StringType)
avm_domainmapping_CAD2EDATransform.attributes={avm_domainmapping_CAD2EDATransform_ScaleX, avm_domainmapping_CAD2EDATransform_RotationZ, avm_domainmapping_CAD2EDATransform_TranslationZ, avm_domainmapping_CAD2EDATransform_TranslationY, avm_domainmapping_CAD2EDATransform_ScaleZ, avm_domainmapping_CAD2EDATransform_RotationX, avm_domainmapping_CAD2EDATransform_TranslationX, avm_domainmapping_CAD2EDATransform_ScaleY, avm_domainmapping_CAD2EDATransform_RotationY}

# DomainMapping class attributes and methods

# eda_EDAModel class attributes and methods

# CADModel class attributes and methods

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
AnalysisConstruct11: BinaryAssociation = BinaryAssociation(
    name="AnalysisConstruct11",
    ends={
        Property(name="avm_AnalysisConstruct", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component12", type=avm_AnalysisConstruct, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Formula13: BinaryAssociation = BinaryAssociation(
    name="Formula13",
    ends={
        Property(name="avm_Formula", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component14", type=avm_Formula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DomainMapping15: BinaryAssociation = BinaryAssociation(
    name="DomainMapping15",
    ends={
        Property(name="avm_DomainMapping", type=avm_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Component16", type=avm_DomainMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
UsesResource17: BinaryAssociation = BinaryAssociation(
    name="UsesResource17",
    ends={
        Property(name="avm_Resource19", type=avm_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DomainModel18", type=avm_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
ValueExpression20: BinaryAssociation = BinaryAssociation(
    name="ValueExpression20",
    ends={
        Property(name="avm_ValueExpressionType", type=avm_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Value", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DataSource21: BinaryAssociation = BinaryAssociation(
    name="DataSource21",
    ends={
        Property(name="avm_DataSource", type=avm_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Value22", type=avm_DataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ValueSource23: BinaryAssociation = BinaryAssociation(
    name="ValueSource23",
    ends={
        Property(name="avm_ValueNode", type=avm_DerivedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DerivedValue", type=avm_ValueNode, multiplicity=Multiplicity(1, 1))
    }
)
Role24: BinaryAssociation = BinaryAssociation(
    name="Role24",
    ends={
        Property(name="avm_Port26", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector25", type=avm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Property27: BinaryAssociation = BinaryAssociation(
    name="Property27",
    ends={
        Property(name="avm_Property29", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector28", type=avm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DefaultJoin30: BinaryAssociation = BinaryAssociation(
    name="DefaultJoin30",
    ends={
        Property(name="avm_assemblyDetail", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector31", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector33: BinaryAssociation = BinaryAssociation(
    name="Connector33",
    ends={
        Property(name="avm_Connector34", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector32", type=avm_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectorFeature35: BinaryAssociation = BinaryAssociation(
    name="ConnectorFeature35",
    ends={
        Property(name="avm_ConnectorFeature", type=avm_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Connector36", type=avm_ConnectorFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Default37: BinaryAssociation = BinaryAssociation(
    name="Default37",
    ends={
        Property(name="avm_ValueExpressionType38", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Maximum39: BinaryAssociation = BinaryAssociation(
    name="Maximum39",
    ends={
        Property(name="avm_ValueExpressionType41", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue40", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Minimum42: BinaryAssociation = BinaryAssociation(
    name="Minimum42",
    ends={
        Property(name="avm_ValueExpressionType44", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue43", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AssignedValue45: BinaryAssociation = BinaryAssociation(
    name="AssignedValue45",
    ends={
        Property(name="avm_ValueExpressionType47", type=avm_ParametricValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricValue46", type=avm_ValueExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Mean48: BinaryAssociation = BinaryAssociation(
    name="Mean48",
    ends={
        Property(name="avm_ValueExpressionType49", type=avm_NormalDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_NormalDistribution", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Value53: BinaryAssociation = BinaryAssociation(
    name="Value53",
    ends={
        Property(name="avm_Value54", type=avm_DomainModelMetric, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DomainModelMetric", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Value55: BinaryAssociation = BinaryAssociation(
    name="Value55",
    ends={
        Property(name="avm_Value56", type=avm_PrimitiveProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_PrimitiveProperty", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CompoundProperty58: BinaryAssociation = BinaryAssociation(
    name="CompoundProperty58",
    ends={
        Property(name="avm_CompoundProperty", type=avm_CompoundProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_CompoundProperty57", type=avm_CompoundProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimitiveProperty59: BinaryAssociation = BinaryAssociation(
    name="PrimitiveProperty59",
    ends={
        Property(name="avm_PrimitiveProperty61", type=avm_CompoundProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_CompoundProperty60", type=avm_PrimitiveProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AssignedValue62: BinaryAssociation = BinaryAssociation(
    name="AssignedValue62",
    ends={
        Property(name="avm_FixedValue", type=avm_ParametricEnumeratedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricEnumeratedValue", type=avm_FixedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Enum63: BinaryAssociation = BinaryAssociation(
    name="Enum63",
    ends={
        Property(name="avm_ValueExpressionType65", type=avm_ParametricEnumeratedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ParametricEnumeratedValue64", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
StandardDeviation50: BinaryAssociation = BinaryAssociation(
    name="StandardDeviation50",
    ends={
        Property(name="avm_ValueExpressionType52", type=avm_NormalDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_NormalDistribution51", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
FromResource66: BinaryAssociation = BinaryAssociation(
    name="FromResource66",
    ends={
        Property(name="avm_Resource68", type=avm_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DataSource67", type=avm_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
RootContainer69: BinaryAssociation = BinaryAssociation(
    name="RootContainer69",
    ends={
        Property(name="avm_Container", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design", type=avm_Container, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DomainFeature70: BinaryAssociation = BinaryAssociation(
    name="DomainFeature70",
    ends={
        Property(name="avm_DesignDomainFeature", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design71", type=avm_DesignDomainFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ResourceDependency72: BinaryAssociation = BinaryAssociation(
    name="ResourceDependency72",
    ends={
        Property(name="avm_Resource74", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design73", type=avm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Container76: BinaryAssociation = BinaryAssociation(
    name="Container76",
    ends={
        Property(name="avm_Container77", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container75", type=avm_Container, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Property78: BinaryAssociation = BinaryAssociation(
    name="Property78",
    ends={
        Property(name="avm_Property80", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container79", type=avm_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ComponentInstance81: BinaryAssociation = BinaryAssociation(
    name="ComponentInstance81",
    ends={
        Property(name="avm_ComponentInstance", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container82", type=avm_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Port83: BinaryAssociation = BinaryAssociation(
    name="Port83",
    ends={
        Property(name="avm_Port85", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container84", type=avm_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Connector86: BinaryAssociation = BinaryAssociation(
    name="Connector86",
    ends={
        Property(name="avm_Connector88", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container87", type=avm_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
JoinData89: BinaryAssociation = BinaryAssociation(
    name="JoinData89",
    ends={
        Property(name="avm_assemblyDetail91", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container90", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Formula92: BinaryAssociation = BinaryAssociation(
    name="Formula92",
    ends={
        Property(name="avm_Formula94", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container93", type=avm_Formula, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ContainerFeature95: BinaryAssociation = BinaryAssociation(
    name="ContainerFeature95",
    ends={
        Property(name="avm_ContainerFeature", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container96", type=avm_ContainerFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ResourceDependency97: BinaryAssociation = BinaryAssociation(
    name="ResourceDependency97",
    ends={
        Property(name="avm_Resource99", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container98", type=avm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DomainModel100: BinaryAssociation = BinaryAssociation(
    name="DomainModel100",
    ends={
        Property(name="avm_DomainModel102", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container101", type=avm_DomainModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Resource103: BinaryAssociation = BinaryAssociation(
    name="Resource103",
    ends={
        Property(name="avm_Resource105", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container104", type=avm_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ValueFlowMux106: BinaryAssociation = BinaryAssociation(
    name="ValueFlowMux106",
    ends={
        Property(name="avm_ValueFlowMux", type=avm_Alternative, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Alternative", type=avm_ValueFlowMux, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PortInstance107: BinaryAssociation = BinaryAssociation(
    name="PortInstance107",
    ends={
        Property(name="avm_ComponentPortInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance108", type=avm_ComponentPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PrimitivePropertyInstance109: BinaryAssociation = BinaryAssociation(
    name="PrimitivePropertyInstance109",
    ends={
        Property(name="avm_ComponentPrimitivePropertyInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance110", type=avm_ComponentPrimitivePropertyInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConnectorInstance111: BinaryAssociation = BinaryAssociation(
    name="ConnectorInstance111",
    ends={
        Property(name="avm_ComponentConnectorInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance112", type=avm_ComponentConnectorInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value113: BinaryAssociation = BinaryAssociation(
    name="Value113",
    ends={
        Property(name="avm_Value115", type=avm_ComponentPrimitivePropertyInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentPrimitivePropertyInstance114", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
PortMap117: BinaryAssociation = BinaryAssociation(
    name="PortMap117",
    ends={
        Property(name="avm_PortMapTarget", type=avm_PortMapTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_PortMapTarget116", type=avm_PortMapTarget, multiplicity=Multiplicity(0, 9999))
    }
)
ConnectorComposition119: BinaryAssociation = BinaryAssociation(
    name="ConnectorComposition119",
    ends={
        Property(name="avm_ConnectorCompositionTarget", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ConnectorCompositionTarget118", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(0, 9999))
    }
)
ApplyJoinData120: BinaryAssociation = BinaryAssociation(
    name="ApplyJoinData120",
    ends={
        Property(name="avm_assemblyDetail122", type=avm_ConnectorCompositionTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ConnectorCompositionTarget121", type=avm_assemblyDetail, multiplicity=Multiplicity(0, 9999))
    }
)
Operand123: BinaryAssociation = BinaryAssociation(
    name="Operand123",
    ends={
        Property(name="avm_ValueNode124", type=avm_SimpleFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_SimpleFormula", type=avm_ValueNode, multiplicity=Multiplicity(1, 9999))
    }
)
Operand125: BinaryAssociation = BinaryAssociation(
    name="Operand125",
    ends={
        Property(name="avm_Operand", type=avm_ComplexFormula, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComplexFormula", type=avm_Operand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ValueSource126: BinaryAssociation = BinaryAssociation(
    name="ValueSource126",
    ends={
        Property(name="avm_ValueNode128", type=avm_Operand, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Operand127", type=avm_ValueNode, multiplicity=Multiplicity(1, 1))
    }
)
Parameter130: BinaryAssociation = BinaryAssociation(
    name="Parameter130",
    ends={
        Property(name="avm_Parameter", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench131", type=avm_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric132: BinaryAssociation = BinaryAssociation(
    name="Metric132",
    ends={
        Property(name="avm_Metric", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench133", type=avm_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestInjectionPoint134: BinaryAssociation = BinaryAssociation(
    name="TestInjectionPoint134",
    ends={
        Property(name="avm_TestInjectionPoint", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench135", type=avm_TestInjectionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestComponent136: BinaryAssociation = BinaryAssociation(
    name="TestComponent136",
    ends={
        Property(name="avm_ComponentInstance138", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench137", type=avm_ComponentInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Workflow139: BinaryAssociation = BinaryAssociation(
    name="Workflow139",
    ends={
        Property(name="avm_Workflow", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench140", type=avm_Workflow, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Settings141: BinaryAssociation = BinaryAssociation(
    name="Settings141",
    ends={
        Property(name="avm_Settings", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench142", type=avm_Settings, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestStructure143: BinaryAssociation = BinaryAssociation(
    name="TestStructure143",
    ends={
        Property(name="avm_DomainModel145", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench144", type=avm_DomainModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value146: BinaryAssociation = BinaryAssociation(
    name="Value146",
    ends={
        Property(name="avm_Value147", type=avm_TestBenchValueBase, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBenchValueBase", type=avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Task148: BinaryAssociation = BinaryAssociation(
    name="Task148",
    ends={
        Property(name="avm_WorkflowTaskBase", type=avm_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Workflow149", type=avm_WorkflowTaskBase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
TopLevelSystemUnderTest129: BinaryAssociation = BinaryAssociation(
    name="TopLevelSystemUnderTest129",
    ends={
        Property(name="avm_TopLevelSystemUnderTest", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench", type=avm_TopLevelSystemUnderTest, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Source150: BinaryAssociation = BinaryAssociation(
    name="Source150",
    ends={
        Property(name="avm_ValueNode152", type=avm_ValueFlowMux, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ValueFlowMux151", type=avm_ValueNode, multiplicity=Multiplicity(0, 9999))
    }
)
Connector154: BinaryAssociation = BinaryAssociation(
    name="Connector154",
    ends={
        Property(name="Connector", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel155", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric156: BinaryAssociation = BinaryAssociation(
    name="Metric156",
    ends={
        Property(name="Metric", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel157", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Limit158: BinaryAssociation = BinaryAssociation(
    name="Limit158",
    ends={
        Property(name="Limit", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel159", type=Limit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Redeclare160: BinaryAssociation = BinaryAssociation(
    name="Redeclare160",
    ends={
        Property(name="Redeclare", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel161", type=Redeclare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter162: BinaryAssociation = BinaryAssociation(
    name="Parameter162",
    ends={
        Property(name="Parameter163", type=avm_modelica_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Connector", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Redeclare164: BinaryAssociation = BinaryAssociation(
    name="Redeclare164",
    ends={
        Property(name="Redeclare166", type=avm_modelica_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Connector165", type=Redeclare, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value167: BinaryAssociation = BinaryAssociation(
    name="Value167",
    ends={
        Property(name="modelica_avm_Value", type=avm_modelica_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Parameter", type=modelica_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TargetValue168: BinaryAssociation = BinaryAssociation(
    name="TargetValue168",
    ends={
        Property(name="modelica_avm_Value169", type=avm_modelica_Limit, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Limit", type=modelica_avm_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
Value170: BinaryAssociation = BinaryAssociation(
    name="Value170",
    ends={
        Property(name="modelica_avm_Value171", type=avm_modelica_Redeclare, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Redeclare", type=modelica_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter153: BinaryAssociation = BinaryAssociation(
    name="Parameter153",
    ends={
        Property(name="Parameter", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Datum172: BinaryAssociation = BinaryAssociation(
    name="Datum172",
    ends={
        Property(name="Datum", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel", type=Datum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ModelMetric176: BinaryAssociation = BinaryAssociation(
    name="ModelMetric176",
    ends={
        Property(name="Metric178", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel177", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DatumMetric179: BinaryAssociation = BinaryAssociation(
    name="DatumMetric179",
    ends={
        Property(name="Metric180", type=avm_cad_Datum, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Datum", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value181: BinaryAssociation = BinaryAssociation(
    name="Value181",
    ends={
        Property(name="cad_avm_Value", type=avm_cad_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Parameter", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SurfaceReverseMap182: BinaryAssociation = BinaryAssociation(
    name="SurfaceReverseMap182",
    ends={
        Property(name="Plane", type=avm_cad_Plane, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Plane", type=Plane, multiplicity=Multiplicity(0, 9999))
    }
)
Metric183: BinaryAssociation = BinaryAssociation(
    name="Metric183",
    ends={
        Property(name="Metric184", type=avm_cad_CoordinateSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CoordinateSystem", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CircleCenter185: BinaryAssociation = BinaryAssociation(
    name="CircleCenter185",
    ends={
        Property(name="PointReference", type=avm_cad_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Circle", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CircleEdge186: BinaryAssociation = BinaryAssociation(
    name="CircleEdge186",
    ends={
        Property(name="PointReference188", type=avm_cad_Circle, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Circle187", type=PointReference, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
Parameter173: BinaryAssociation = BinaryAssociation(
    name="Parameter173",
    ends={
        Property(name="Parameter175", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel174", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PolygonPoint189: BinaryAssociation = BinaryAssociation(
    name="PolygonPoint189",
    ends={
        Property(name="PointReference190", type=avm_cad_Polygon, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Polygon", type=PointReference, multiplicity=Multiplicity(3, 9999), is_composite=True)
    }
)
ExtrusionHeight191: BinaryAssociation = BinaryAssociation(
    name="ExtrusionHeight191",
    ends={
        Property(name="PointReference192", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ExtrusionSurface193: BinaryAssociation = BinaryAssociation(
    name="ExtrusionSurface193",
    ends={
        Property(name="Geometry2D", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry194", type=Geometry2D, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SphereCenter195: BinaryAssociation = BinaryAssociation(
    name="SphereCenter195",
    ends={
        Property(name="PointReference196", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SphereEdge197: BinaryAssociation = BinaryAssociation(
    name="SphereEdge197",
    ends={
        Property(name="PointReference199", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere198", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CustomGeometryInput200: BinaryAssociation = BinaryAssociation(
    name="CustomGeometryInput200",
    ends={
        Property(name="CustomGeometryInput", type=avm_cad_CustomGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometry", type=CustomGeometryInput, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
InputGeometry201: BinaryAssociation = BinaryAssociation(
    name="InputGeometry201",
    ends={
        Property(name="Geometry", type=avm_cad_CustomGeometryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometryInput", type=Geometry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReferredPoint202: BinaryAssociation = BinaryAssociation(
    name="ReferredPoint202",
    ends={
        Property(name="Point", type=avm_cad_PointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PointReference", type=Point, multiplicity=Multiplicity(0, 9999))
    }
)
ReferencePlane203: BinaryAssociation = BinaryAssociation(
    name="ReferencePlane203",
    ends={
        Property(name="PlaneReference", type=avm_cad_Surface, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Surface", type=PlaneReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReferredPlane204: BinaryAssociation = BinaryAssociation(
    name="ReferredPlane204",
    ends={
        Property(name="Plane205", type=avm_cad_PlaneReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PlaneReference", type=Plane, multiplicity=Multiplicity(0, 9999))
    }
)
Datum206: BinaryAssociation = BinaryAssociation(
    name="Datum206",
    ends={
        Property(name="Datum207", type=avm_cad_GuideDatum, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_GuideDatum", type=Datum, multiplicity=Multiplicity(1, 1))
    }
)
AssemblyRootComponentInstance208: BinaryAssociation = BinaryAssociation(
    name="AssemblyRootComponentInstance208",
    ends={
        Property(name="cad_avm_ComponentInstance", type=avm_cad_AssemblyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_AssemblyRoot", type=cad_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentPlane209: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane209",
    ends={
        Property(name="Plane210", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis211: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis211",
    ends={
        Property(name="Axis", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec212", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
RotationLimitReference213: BinaryAssociation = BinaryAssociation(
    name="RotationLimitReference213",
    ends={
        Property(name="Plane215", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec214", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
MinimumRotation216: BinaryAssociation = BinaryAssociation(
    name="MinimumRotation216",
    ends={
        Property(name="cad_avm_Value218", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec217", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultRotation219: BinaryAssociation = BinaryAssociation(
    name="DefaultRotation219",
    ends={
        Property(name="cad_avm_Value221", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec220", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MaximumRotation222: BinaryAssociation = BinaryAssociation(
    name="MaximumRotation222",
    ends={
        Property(name="cad_avm_Value224", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec223", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AlignmentPlane225: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane225",
    ends={
        Property(name="Plane226", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis227: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis227",
    ends={
        Property(name="Axis229", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec228", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
MinimumTranslation230: BinaryAssociation = BinaryAssociation(
    name="MinimumTranslation230",
    ends={
        Property(name="cad_avm_Value232", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec231", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultTranslation233: BinaryAssociation = BinaryAssociation(
    name="DefaultTranslation233",
    ends={
        Property(name="cad_avm_Value235", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec234", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MaximumTranslation236: BinaryAssociation = BinaryAssociation(
    name="MaximumTranslation236",
    ends={
        Property(name="cad_avm_Value238", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec237", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TranslationLimitReference239: BinaryAssociation = BinaryAssociation(
    name="TranslationLimitReference239",
    ends={
        Property(name="Plane241", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec240", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
Parameter242: BinaryAssociation = BinaryAssociation(
    name="Parameter242",
    ends={
        Property(name="Parameter243", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric244: BinaryAssociation = BinaryAssociation(
    name="Metric244",
    ends={
        Property(name="Metric246", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel245", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value247: BinaryAssociation = BinaryAssociation(
    name="Value247",
    ends={
        Property(name="manufacturing_avm_Value", type=avm_manufacturing_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_Parameter", type=manufacturing_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Connector248: BinaryAssociation = BinaryAssociation(
    name="Connector248",
    ends={
        Property(name="Connector249", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter250: BinaryAssociation = BinaryAssociation(
    name="Parameter250",
    ends={
        Property(name="Parameter252", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel251", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Pin253: BinaryAssociation = BinaryAssociation(
    name="Pin253",
    ends={
        Property(name="Pin", type=avm_schematic_SchematicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_schematic_SchematicModel", type=Pin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter254: BinaryAssociation = BinaryAssociation(
    name="Parameter254",
    ends={
        Property(name="avm_eda_EDAModel", type=eda_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eda_Parameter", type=avm_eda_EDAModel, multiplicity=Multiplicity(1, 1))
    }
)
Value255: BinaryAssociation = BinaryAssociation(
    name="Value255",
    ends={
        Property(name="eda_avm_Value", type=avm_eda_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_Parameter", type=eda_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ConstraintTarget256: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget256",
    ends={
        Property(name="eda_avm_ComponentInstance", type=avm_eda_ExactLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_ExactLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget257: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget257",
    ends={
        Property(name="eda_avm_Container", type=avm_eda_ExactLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_ExactLayoutConstraint258", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget259: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget259",
    ends={
        Property(name="eda_avm_ComponentInstance260", type=avm_eda_RangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RangeLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget261: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget261",
    ends={
        Property(name="eda_avm_Container263", type=avm_eda_RangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RangeLayoutConstraint262", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget264: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget264",
    ends={
        Property(name="eda_avm_ComponentInstance265", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
Origin266: BinaryAssociation = BinaryAssociation(
    name="Origin266",
    ends={
        Property(name="eda_avm_ComponentInstance268", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint267", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
ContainerConstraintTarget269: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget269",
    ends={
        Property(name="eda_avm_Container271", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint270", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget272: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget272",
    ends={
        Property(name="eda_avm_Container273", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
Origin274: BinaryAssociation = BinaryAssociation(
    name="Origin274",
    ends={
        Property(name="eda_avm_ComponentInstance276", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint275", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
ConstraintTarget277: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget277",
    ends={
        Property(name="eda_avm_ComponentInstance279", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint278", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget280: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget280",
    ends={
        Property(name="eda_avm_ComponentInstance281", type=avm_eda_GlobalLayoutConstraintException, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_GlobalLayoutConstraintException", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget282: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget282",
    ends={
        Property(name="eda_avm_Container284", type=avm_eda_GlobalLayoutConstraintException, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_GlobalLayoutConstraintException283", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
Parameter285: BinaryAssociation = BinaryAssociation(
    name="Parameter285",
    ends={
        Property(name="spice_Parameter", type=avm_spice_SPICEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_spice_SPICEModel", type=spice_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value286: BinaryAssociation = BinaryAssociation(
    name="Value286",
    ends={
        Property(name="spice_avm_Value", type=avm_spice_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_spice_Parameter", type=spice_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SystemCPort287: BinaryAssociation = BinaryAssociation(
    name="SystemCPort287",
    ends={
        Property(name="SystemCPort", type=avm_systemc_SystemCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_SystemCModel", type=SystemCPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter288: BinaryAssociation = BinaryAssociation(
    name="Parameter288",
    ends={
        Property(name="Parameter290", type=avm_systemc_SystemCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_SystemCModel289", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value291: BinaryAssociation = BinaryAssociation(
    name="Value291",
    ends={
        Property(name="systemc_avm_Value", type=avm_systemc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_Parameter", type=systemc_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RFPort292: BinaryAssociation = BinaryAssociation(
    name="RFPort292",
    ends={
        Property(name="RFPort", type=avm_rf_RFModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_rf_RFModel", type=RFPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
EDAModel293: BinaryAssociation = BinaryAssociation(
    name="EDAModel293",
    ends={
        Property(name="eda_EDAModel", type=avm_domainmapping_CAD2EDATransform, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_domainmapping_CAD2EDATransform", type=eda_EDAModel, multiplicity=Multiplicity(1, 1))
    }
)
CADModel294: BinaryAssociation = BinaryAssociation(
    name="CADModel294",
    ends={
        Property(name="avm_domainmapping_CAD2EDATransform295", type=CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="CADModel", type=avm_domainmapping_CAD2EDATransform, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_avm_Value_ValueNode = Generalization(general=ValueNode, specific=avm_Value)
gen_avm_FixedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_FixedValue)
gen_avm_CalculatedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_CalculatedValue)
gen_avm_DerivedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_DerivedValue)
gen_avm_Connector_ConnectorCompositionTarget = Generalization(general=ConnectorCompositionTarget, specific=avm_Connector)
gen_avm_Port_PortMapTarget = Generalization(general=PortMapTarget, specific=avm_Port)
gen_avm_DomainModelPort_Port = Generalization(general=Port, specific=avm_DomainModelPort)
gen_avm_ParametricValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ParametricValue)
gen_avm_ProbabilisticValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ProbabilisticValue)
gen_avm_NormalDistribution_ProbabilisticValue = Generalization(general=ProbabilisticValue, specific=avm_NormalDistribution)
gen_avm_SecurityClassification_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_SecurityClassification)
gen_avm_Proprietary_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_Proprietary)
gen_avm_ITAR_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_ITAR)
gen_avm_UniformDistribution_ProbabilisticValue = Generalization(general=ProbabilisticValue, specific=avm_UniformDistribution)
gen_avm_PrimitiveProperty_Property = Generalization(general=Property_, specific=avm_PrimitiveProperty)
gen_avm_CompoundProperty_Property = Generalization(general=Property_, specific=avm_CompoundProperty)
gen_avm_ParametricEnumeratedValue_ValueExpressionType = Generalization(general=ValueExpressionType, specific=avm_ParametricEnumeratedValue)
gen_avm_AbstractPort_Port = Generalization(general=Port, specific=avm_AbstractPort)
gen_avm_Compound_Container = Generalization(general=Container, specific=avm_Compound)
gen_avm_Optional_DesignSpaceContainer = Generalization(general=DesignSpaceContainer, specific=avm_Optional)
gen_avm_Alternative_DesignSpaceContainer = Generalization(general=DesignSpaceContainer, specific=avm_Alternative)
gen_avm_ComponentPortInstance_PortMapTarget = Generalization(general=PortMapTarget, specific=avm_ComponentPortInstance)
gen_avm_DesignSpaceContainer_Container = Generalization(general=Container, specific=avm_DesignSpaceContainer)
gen_avm_ComponentConnectorInstance_ConnectorCompositionTarget = Generalization(general=ConnectorCompositionTarget, specific=avm_ComponentConnectorInstance)
gen_avm_Formula_ValueNode = Generalization(general=ValueNode, specific=avm_Formula)
gen_avm_SimpleFormula_Formula = Generalization(general=Formula, specific=avm_SimpleFormula)
gen_avm_ComplexFormula_Formula = Generalization(general=Formula, specific=avm_ComplexFormula)
gen_avm_DoDDistributionStatement_DistributionRestriction = Generalization(general=DistributionRestriction, specific=avm_DoDDistributionStatement)
gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TopLevelSystemUnderTest)
gen_avm_Parameter_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Parameter)
gen_avm_Metric_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Metric)
gen_avm_TestInjectionPoint_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TestInjectionPoint)
gen_avm_ExecutionTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_ExecutionTask)
gen_avm_ValueFlowMux_ValueNode = Generalization(general=ValueNode, specific=avm_ValueFlowMux)
gen_avm_modelica_ModelicaModel_DomainModel = Generalization(general=DomainModel, specific=avm_modelica_ModelicaModel)
gen_avm_InterpreterTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_InterpreterTask)
gen_avm_modelica_Connector_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_modelica_Connector)
gen_avm_modelica_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Parameter)
gen_avm_modelica_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_modelica_Metric)
gen_avm_modelica_Redeclare_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Redeclare)
gen_avm_modelica_SolverSettings_Settings = Generalization(general=Settings, specific=avm_modelica_SolverSettings)
gen_avm_cad_CADModel_DomainModel = Generalization(general=DomainModel, specific=avm_cad_CADModel)
gen_avm_cad_Datum_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_cad_Datum)
gen_avm_cad_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_cad_Parameter)
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
gen_avm_cad_ExtrudedGeometry_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_ExtrudedGeometry)
gen_avm_cad_Sphere_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_Sphere)
gen_avm_cad_CustomGeometry_Geometry = Generalization(general=Geometry, specific=avm_cad_CustomGeometry)
gen_avm_cad_Surface_Geometry3D = Generalization(general=Geometry3D, specific=avm_cad_Surface)
gen_avm_cad_GuideDatum_ConnectorFeature = Generalization(general=ConnectorFeature, specific=avm_cad_GuideDatum)
gen_avm_cad_AssemblyRoot_DesignDomainFeature = Generalization(general=DesignDomainFeature, specific=avm_cad_AssemblyRoot)
gen_avm_cad_KinematicJointSpec_ConnectorFeature = Generalization(general=ConnectorFeature, specific=avm_cad_KinematicJointSpec)
gen_avm_cad_RevoluteJointSpec_KinematicJointSpec = Generalization(general=KinematicJointSpec, specific=avm_cad_RevoluteJointSpec)
gen_avm_cad_TranslationalJointSpec_KinematicJointSpec = Generalization(general=KinematicJointSpec, specific=avm_cad_TranslationalJointSpec)
gen_avm_manufacturing_ManufacturingModel_DomainModel = Generalization(general=DomainModel, specific=avm_manufacturing_ManufacturingModel)
gen_avm_manufacturing_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_manufacturing_Parameter)
gen_avm_manufacturing_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_manufacturing_Metric)
gen_avm_cyber_CyberModel_DomainModel = Generalization(general=DomainModel, specific=avm_cyber_CyberModel)
gen_avm_schematic_SchematicModel_DomainModel = Generalization(general=DomainModel, specific=avm_schematic_SchematicModel)
gen_avm_schematic_Pin_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_schematic_Pin)
gen_avm_eda_EDAModel_SchematicModel = Generalization(general=SchematicModel, specific=avm_eda_EDAModel)
gen_avm_eda_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_eda_Parameter)
gen_avm_eda_PcbLayoutConstraint_ContainerFeature = Generalization(general=ContainerFeature, specific=avm_eda_PcbLayoutConstraint)
gen_avm_eda_ExactLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_ExactLayoutConstraint)
gen_avm_eda_RangeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RangeLayoutConstraint)
gen_avm_eda_RelativeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RelativeLayoutConstraint)
gen_avm_eda_RelativeRangeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RelativeRangeLayoutConstraint)
gen_avm_eda_GlobalLayoutConstraintException_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_GlobalLayoutConstraintException)
gen_avm_eda_CircuitLayout_DomainModel = Generalization(general=DomainModel, specific=avm_eda_CircuitLayout)
gen_avm_spice_SPICEModel_SchematicModel = Generalization(general=SchematicModel, specific=avm_spice_SPICEModel)
gen_avm_spice_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_spice_Parameter)
gen_avm_systemc_SystemCModel_DomainModel = Generalization(general=DomainModel, specific=avm_systemc_SystemCModel)
gen_avm_systemc_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_systemc_Parameter)
gen_avm_systemc_SystemCPort_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_systemc_SystemCPort)
gen_avm_rf_RFModel_DomainModel = Generalization(general=DomainModel, specific=avm_rf_RFModel)
gen_avm_rf_RFPort_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_rf_RFPort)
gen_avm_domainmapping_CAD2EDATransform_DomainMapping = Generalization(general=DomainMapping, specific=avm_domainmapping_CAD2EDATransform)

# Domain Model
domain_model = DomainModel(
    name="avm",
    types={avm_Component, avm_DomainModel, avm_Property, avm_Resource, avm_Connector, avm_DistributionRestriction, avm_Port, avm_AnalysisConstruct, avm_Formula, avm_DomainMapping, avm_Value, ValueNode, avm_ValueExpressionType, avm_DataSource, avm_FixedValue, ValueExpressionType, avm_CalculatedValue, avm_DerivedValue, avm_ValueNode, ConnectorCompositionTarget, avm_assemblyDetail, avm_ConnectorFeature, PortMapTarget, avm_DomainModelPort, Port, avm_DomainModelParameter, avm_ParametricValue, avm_ProbabilisticValue, avm_NormalDistribution, ProbabilisticValue, avm_SecurityClassification, DistributionRestriction, avm_Proprietary, avm_ITAR, avm_DomainModelMetric, avm_UniformDistribution, avm_PrimitiveProperty, Property_, avm_CompoundProperty, avm_ParametricEnumeratedValue, avm_AbstractPort, avm_Design, avm_Container, avm_DesignDomainFeature, avm_ComponentInstance, avm_ContainerFeature, avm_Compound, Container, avm_Optional, DesignSpaceContainer, avm_Alternative, avm_ValueFlowMux, avm_ComponentPortInstance, avm_ComponentPrimitivePropertyInstance, avm_ComponentConnectorInstance, avm_DesignSpaceContainer, avm_PortMapTarget, avm_ConnectorCompositionTarget, avm_SimpleFormula, Formula, avm_ComplexFormula, avm_Operand, avm_DoDDistributionStatement, avm_TestBench, avm_TopLevelSystemUnderTest, avm_Parameter, avm_Metric, avm_TestInjectionPoint, avm_Workflow, avm_Settings, ContainerInstanceBase, TestBenchValueBase, avm_ContainerInstanceBase, avm_TestBenchValueBase, avm_WorkflowTaskBase, avm_ExecutionTask, avm_modelica_ModelicaModel, DomainModel, avm_InterpreterTask, WorkflowTaskBase, Connector, Metric, Limit, Redeclare, avm_modelica_Connector, DomainModelPort, avm_modelica_Parameter, DomainModelParameter, modelica_avm_Value, avm_modelica_Metric, DomainModelMetric, avm_modelica_Limit, avm_modelica_Redeclare, Parameter_, avm_modelica_SolverSettings, Settings, avm_cad_CADModel, Datum, avm_cad_Datum, avm_cad_Parameter, cad_avm_Value, avm_cad_Point, avm_cad_Axis, avm_cad_Plane, Plane, avm_cad_CoordinateSystem, avm_cad_Metric, avm_cad_Geometry, AnalysisConstruct, avm_cad_Geometry2D, Geometry, avm_cad_Geometry3D, avm_cad_Circle, Geometry2D, PointReference, avm_cad_Polygon, avm_cad_ExtrudedGeometry, Geometry3D, avm_cad_Sphere, avm_cad_CustomGeometry, CustomGeometryInput, avm_cad_CustomGeometryInput, avm_cad_PointReference, Point, avm_cad_Surface, PlaneReference, avm_cad_PlaneReference, avm_cad_GuideDatum, ConnectorFeature, avm_cad_AssemblyRoot, DesignDomainFeature, cad_avm_ComponentInstance, avm_cad_KinematicJointSpec, avm_cad_RevoluteJointSpec, KinematicJointSpec, Axis, avm_cad_TranslationalJointSpec, avm_manufacturing_ManufacturingModel, avm_manufacturing_Parameter, manufacturing_avm_Value, avm_manufacturing_Metric, avm_cyber_CyberModel, avm_schematic_SchematicModel, Pin, avm_schematic_Pin, avm_eda_EDAModel, SchematicModel, avm_eda_Parameter, eda_avm_Value, avm_eda_PcbLayoutConstraint, ContainerFeature, avm_eda_ExactLayoutConstraint, PcbLayoutConstraint, eda_avm_ComponentInstance, eda_avm_Container, avm_eda_RangeLayoutConstraint, avm_eda_RelativeLayoutConstraint, eda_Parameter, avm_eda_RelativeRangeLayoutConstraint, avm_eda_GlobalLayoutConstraintException, avm_eda_CircuitLayout, avm_spice_SPICEModel, spice_Parameter, avm_spice_Parameter, spice_avm_Value, avm_systemc_SystemCModel, SystemCPort, avm_systemc_Parameter, systemc_avm_Value, avm_systemc_SystemCPort, avm_rf_RFModel, RFPort, avm_rf_RFPort, avm_domainmapping_CAD2EDATransform, DomainMapping, eda_EDAModel, CADModel, DataTypeEnum, DimensionTypeEnum, CalculationTypeEnum, SimpleFormulaOperation, DoDDistributionStatementEnum, BoundTypeEnum, RedeclareTypeEnum, IntervalMethod, JobManagerToolSelection, CustomGeometryInputOperationEnum, PartIntersectionEnum, GeometryQualifierEnum, FileFormat, ModelType, LayerEnum, LayerRangeEnum, RelativeLayerEnum, RangeConstraintTypeEnum, RelativeRotationEnum, SystemCDataTypeEnum, GlobalConstraintTypeEnum, DirectionalityEnum, FunctionEnum, RotationEnum, PortDirectionality},
    associations={DomainModel0, Property1, ResourceDependency3, Connector5, DistributionRestriction7, Port9, AnalysisConstruct11, Formula13, DomainMapping15, UsesResource17, ValueExpression20, DataSource21, ValueSource23, Role24, Property27, DefaultJoin30, Connector33, ConnectorFeature35, Default37, Maximum39, Minimum42, AssignedValue45, Mean48, Value53, Value55, CompoundProperty58, PrimitiveProperty59, AssignedValue62, Enum63, StandardDeviation50, FromResource66, RootContainer69, DomainFeature70, ResourceDependency72, Container76, Property78, ComponentInstance81, Port83, Connector86, JoinData89, Formula92, ContainerFeature95, ResourceDependency97, DomainModel100, Resource103, ValueFlowMux106, PortInstance107, PrimitivePropertyInstance109, ConnectorInstance111, Value113, PortMap117, ConnectorComposition119, ApplyJoinData120, Operand123, Operand125, ValueSource126, Parameter130, Metric132, TestInjectionPoint134, TestComponent136, Workflow139, Settings141, TestStructure143, Value146, Task148, TopLevelSystemUnderTest129, Source150, Connector154, Metric156, Limit158, Redeclare160, Parameter162, Redeclare164, Value167, TargetValue168, Value170, Parameter153, Datum172, ModelMetric176, DatumMetric179, Value181, SurfaceReverseMap182, Metric183, CircleCenter185, CircleEdge186, Parameter173, PolygonPoint189, ExtrusionHeight191, ExtrusionSurface193, SphereCenter195, SphereEdge197, CustomGeometryInput200, InputGeometry201, ReferredPoint202, ReferencePlane203, ReferredPlane204, Datum206, AssemblyRootComponentInstance208, AlignmentPlane209, AlignmentAxis211, RotationLimitReference213, MinimumRotation216, DefaultRotation219, MaximumRotation222, AlignmentPlane225, AlignmentAxis227, MinimumTranslation230, DefaultTranslation233, MaximumTranslation236, TranslationLimitReference239, Parameter242, Metric244, Value247, Connector248, Parameter250, Pin253, Parameter254, Value255, ConstraintTarget256, ContainerConstraintTarget257, ConstraintTarget259, ContainerConstraintTarget261, ConstraintTarget264, Origin266, ContainerConstraintTarget269, ContainerConstraintTarget272, Origin274, ConstraintTarget277, ConstraintTarget280, ContainerConstraintTarget282, Parameter285, Value286, SystemCPort287, Parameter288, Value291, RFPort292, EDAModel293, CADModel294},
    generalizations={gen_avm_Value_ValueNode, gen_avm_FixedValue_ValueExpressionType, gen_avm_CalculatedValue_ValueExpressionType, gen_avm_DerivedValue_ValueExpressionType, gen_avm_Connector_ConnectorCompositionTarget, gen_avm_Port_PortMapTarget, gen_avm_DomainModelPort_Port, gen_avm_ParametricValue_ValueExpressionType, gen_avm_ProbabilisticValue_ValueExpressionType, gen_avm_NormalDistribution_ProbabilisticValue, gen_avm_SecurityClassification_DistributionRestriction, gen_avm_Proprietary_DistributionRestriction, gen_avm_ITAR_DistributionRestriction, gen_avm_UniformDistribution_ProbabilisticValue, gen_avm_PrimitiveProperty_Property, gen_avm_CompoundProperty_Property, gen_avm_ParametricEnumeratedValue_ValueExpressionType, gen_avm_AbstractPort_Port, gen_avm_Compound_Container, gen_avm_Optional_DesignSpaceContainer, gen_avm_Alternative_DesignSpaceContainer, gen_avm_ComponentPortInstance_PortMapTarget, gen_avm_DesignSpaceContainer_Container, gen_avm_ComponentConnectorInstance_ConnectorCompositionTarget, gen_avm_Formula_ValueNode, gen_avm_SimpleFormula_Formula, gen_avm_ComplexFormula_Formula, gen_avm_DoDDistributionStatement_DistributionRestriction, gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase, gen_avm_Parameter_TestBenchValueBase, gen_avm_Metric_TestBenchValueBase, gen_avm_TestInjectionPoint_ContainerInstanceBase, gen_avm_ExecutionTask_WorkflowTaskBase, gen_avm_ValueFlowMux_ValueNode, gen_avm_modelica_ModelicaModel_DomainModel, gen_avm_InterpreterTask_WorkflowTaskBase, gen_avm_modelica_Connector_DomainModelPort, gen_avm_modelica_Parameter_DomainModelParameter, gen_avm_modelica_Metric_DomainModelMetric, gen_avm_modelica_Redeclare_DomainModelParameter, gen_avm_modelica_SolverSettings_Settings, gen_avm_cad_CADModel_DomainModel, gen_avm_cad_Datum_DomainModelPort, gen_avm_cad_Parameter_DomainModelParameter, gen_avm_cad_Point_Datum, gen_avm_cad_Axis_Datum, gen_avm_cad_Plane_Datum, gen_avm_cad_CoordinateSystem_Datum, gen_avm_cad_Metric_DomainModelMetric, gen_avm_cad_Geometry_AnalysisConstruct, gen_avm_cad_Geometry2D_Geometry, gen_avm_cad_Geometry3D_Geometry, gen_avm_cad_Circle_Geometry2D, gen_avm_cad_Polygon_Geometry2D, gen_avm_cad_ExtrudedGeometry_Geometry3D, gen_avm_cad_Sphere_Geometry3D, gen_avm_cad_CustomGeometry_Geometry, gen_avm_cad_Surface_Geometry3D, gen_avm_cad_GuideDatum_ConnectorFeature, gen_avm_cad_AssemblyRoot_DesignDomainFeature, gen_avm_cad_KinematicJointSpec_ConnectorFeature, gen_avm_cad_RevoluteJointSpec_KinematicJointSpec, gen_avm_cad_TranslationalJointSpec_KinematicJointSpec, gen_avm_manufacturing_ManufacturingModel_DomainModel, gen_avm_manufacturing_Parameter_DomainModelParameter, gen_avm_manufacturing_Metric_DomainModelMetric, gen_avm_cyber_CyberModel_DomainModel, gen_avm_schematic_SchematicModel_DomainModel, gen_avm_schematic_Pin_DomainModelPort, gen_avm_eda_EDAModel_SchematicModel, gen_avm_eda_Parameter_DomainModelParameter, gen_avm_eda_PcbLayoutConstraint_ContainerFeature, gen_avm_eda_ExactLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_RangeLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_RelativeLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_RelativeRangeLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_GlobalLayoutConstraintException_PcbLayoutConstraint, gen_avm_eda_CircuitLayout_DomainModel, gen_avm_spice_SPICEModel_SchematicModel, gen_avm_spice_Parameter_DomainModelParameter, gen_avm_systemc_SystemCModel_DomainModel, gen_avm_systemc_Parameter_DomainModelParameter, gen_avm_systemc_SystemCPort_DomainModelPort, gen_avm_rf_RFModel_DomainModel, gen_avm_rf_RFPort_DomainModelPort, gen_avm_domainmapping_CAD2EDATransform_DomainMapping},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)