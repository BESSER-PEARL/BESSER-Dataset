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
            EnumerationLiteral(name="Vector"),
			EnumerationLiteral(name="Scalar"),
			EnumerationLiteral(name="Matrix")
    }
)

SimpleFormulaOperation: Enumeration = Enumeration(
    name="SimpleFormulaOperation",
    literals={
            EnumerationLiteral(name="ArithmeticMean"),
			EnumerationLiteral(name="GeometricMean"),
			EnumerationLiteral(name="Addition"),
			EnumerationLiteral(name="Multiplication"),
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

IntervalMethod: Enumeration = Enumeration(
    name="IntervalMethod",
    literals={
            EnumerationLiteral(name="NumberOfIntervals"),
			EnumerationLiteral(name="IntervalLength")
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

GeometryQualifierEnum: Enumeration = Enumeration(
    name="GeometryQualifierEnum",
    literals={
            EnumerationLiteral(name="InteriorAndBoundary"),
			EnumerationLiteral(name="InteriorOnly"),
			EnumerationLiteral(name="BoundaryOnly")
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
            EnumerationLiteral(name="None_"),
			EnumerationLiteral(name="IntersectionWithAnyParts"),
			EnumerationLiteral(name="IntersectionWithReferencedParts")
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

GlobalConstraintTypeEnum: Enumeration = Enumeration(
    name="GlobalConstraintTypeEnum",
    literals={
            EnumerationLiteral(name="BoardEdgeSpacing")
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

DirectionalityEnum: Enumeration = Enumeration(
    name="DirectionalityEnum",
    literals={
            EnumerationLiteral(name="in_"),
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
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="out")
    }
)

# Classes
avm_Property = Class(name="avm_Property", is_abstract=True)
avm_Component = Class(name="avm_Component")
avm_DomainModel = Class(name="avm_DomainModel_", is_abstract=True)
avm_Value = Class(name="avm_Value")
ValueNode = Class(name="ValueNode")
avm_ValueExpressionType = Class(name="avm_ValueExpressionType", is_abstract=True)
avm_Resource = Class(name="avm_Resource")
avm_Connector = Class(name="avm_Connector")
avm_DistributionRestriction = Class(name="avm_DistributionRestriction", is_abstract=True)
avm_Port = Class(name="avm_Port", is_abstract=True)
avm_AnalysisConstruct = Class(name="avm_AnalysisConstruct", is_abstract=True)
avm_Formula = Class(name="avm_Formula", is_abstract=True)
avm_DomainMapping = Class(name="avm_DomainMapping", is_abstract=True)
avm_assemblyDetail = Class(name="avm_assemblyDetail")
avm_DataSource = Class(name="avm_DataSource")
avm_FixedValue = Class(name="avm_FixedValue")
ValueExpressionType = Class(name="ValueExpressionType")
avm_CalculatedValue = Class(name="avm_CalculatedValue")
avm_DerivedValue = Class(name="avm_DerivedValue")
avm_ValueNode = Class(name="avm_ValueNode", is_abstract=True)
ConnectorCompositionTarget = Class(name="ConnectorCompositionTarget")
avm_ConnectorFeature = Class(name="avm_ConnectorFeature", is_abstract=True)
PortMapTarget = Class(name="PortMapTarget")
avm_DomainModelPort = Class(name="avm_DomainModelPort", is_abstract=True)
Port = Class(name="Port")
avm_DomainModelParameter = Class(name="avm_DomainModelParameter", is_abstract=True)
avm_ParametricValue = Class(name="avm_ParametricValue")
avm_ProbabilisticValue = Class(name="avm_ProbabilisticValue", is_abstract=True)
avm_NormalDistribution = Class(name="avm_NormalDistribution")
ProbabilisticValue = Class(name="ProbabilisticValue")
avm_SecurityClassification = Class(name="avm_SecurityClassification")
DistributionRestriction = Class(name="DistributionRestriction")
avm_Proprietary = Class(name="avm_Proprietary")
avm_ITAR = Class(name="avm_ITAR")
avm_DomainModelMetric = Class(name="avm_DomainModelMetric", is_abstract=True)
avm_UniformDistribution = Class(name="avm_UniformDistribution")
avm_PrimitiveProperty = Class(name="avm_PrimitiveProperty")
Property_ = Class(name="Property")
avm_CompoundProperty = Class(name="avm_CompoundProperty")
avm_ParametricEnumeratedValue = Class(name="avm_ParametricEnumeratedValue")
avm_AbstractPort = Class(name="avm_AbstractPort")
avm_Design = Class(name="avm_Design")
avm_Container = Class(name="avm_Container", is_abstract=True)
avm_ContainerFeature = Class(name="avm_ContainerFeature", is_abstract=True)
avm_DesignDomainFeature = Class(name="avm_DesignDomainFeature", is_abstract=True)
avm_ComponentInstance = Class(name="avm_ComponentInstance")
avm_ComponentPortInstance = Class(name="avm_ComponentPortInstance")
avm_Compound = Class(name="avm_Compound")
Container = Class(name="Container")
avm_Optional = Class(name="avm_Optional")
DesignSpaceContainer = Class(name="DesignSpaceContainer")
avm_Alternative = Class(name="avm_Alternative")
avm_ValueFlowMux = Class(name="avm_ValueFlowMux")
avm_ComponentPrimitivePropertyInstance = Class(name="avm_ComponentPrimitivePropertyInstance")
avm_ComponentConnectorInstance = Class(name="avm_ComponentConnectorInstance")
avm_DesignSpaceContainer = Class(name="avm_DesignSpaceContainer", is_abstract=True)
avm_PortMapTarget = Class(name="avm_PortMapTarget")
avm_ConnectorCompositionTarget = Class(name="avm_ConnectorCompositionTarget")
avm_SimpleFormula = Class(name="avm_SimpleFormula")
Formula = Class(name="Formula")
avm_TestBench = Class(name="avm_TestBench")
avm_ComplexFormula = Class(name="avm_ComplexFormula")
avm_Operand = Class(name="avm_Operand")
avm_DoDDistributionStatement = Class(name="avm_DoDDistributionStatement")
avm_TopLevelSystemUnderTest = Class(name="avm_TopLevelSystemUnderTest")
avm_Parameter = Class(name="avm_Parameter")
avm_Metric = Class(name="avm_Metric")
avm_TestInjectionPoint = Class(name="avm_TestInjectionPoint")
avm_Workflow = Class(name="avm_Workflow")
avm_Settings = Class(name="avm_Settings", is_abstract=True)
ContainerInstanceBase = Class(name="ContainerInstanceBase")
TestBenchValueBase = Class(name="TestBenchValueBase")
avm_ContainerInstanceBase = Class(name="avm_ContainerInstanceBase", is_abstract=True)
avm_TestBenchValueBase = Class(name="avm_TestBenchValueBase", is_abstract=True)
avm_WorkflowTaskBase = Class(name="avm_WorkflowTaskBase", is_abstract=True)
avm_InterpreterTask = Class(name="avm_InterpreterTask")
WorkflowTaskBase = Class(name="WorkflowTaskBase")
modelica_avm_Value = Class(name="modelica_avm_Value")
avm_ExecutionTask = Class(name="avm_ExecutionTask")
avm_modelica_ModelicaModel = Class(name="avm_modelica_ModelicaModel")
DomainModel_ = Class(name="DomainModel_")
Parameter_ = Class(name="Parameter")
Connector = Class(name="Connector")
Metric = Class(name="Metric")
Limit = Class(name="Limit")
Redeclare = Class(name="Redeclare")
avm_modelica_Connector = Class(name="avm_modelica_Connector")
DomainModelPort = Class(name="DomainModelPort")
avm_modelica_Parameter = Class(name="avm_modelica_Parameter")
DomainModelParameter = Class(name="DomainModelParameter")
avm_modelica_Metric = Class(name="avm_modelica_Metric")
DomainModelMetric = Class(name="DomainModelMetric")
avm_modelica_Limit = Class(name="avm_modelica_Limit")
avm_modelica_Redeclare = Class(name="avm_modelica_Redeclare")
avm_modelica_SolverSettings = Class(name="avm_modelica_SolverSettings")
Settings = Class(name="Settings")
AnalysisConstruct = Class(name="AnalysisConstruct")
avm_cad_CADModel = Class(name="avm_cad_CADModel")
Datum = Class(name="Datum")
avm_cad_Datum = Class(name="avm_cad_Datum", is_abstract=True)
avm_cad_Parameter = Class(name="avm_cad_Parameter")
cad_avm_Value = Class(name="cad_avm_Value")
avm_cad_Point = Class(name="avm_cad_Point")
avm_cad_Axis = Class(name="avm_cad_Axis")
avm_cad_Plane = Class(name="avm_cad_Plane")
Plane = Class(name="Plane")
avm_cad_CoordinateSystem = Class(name="avm_cad_CoordinateSystem")
avm_cad_Metric = Class(name="avm_cad_Metric")
avm_cad_Geometry = Class(name="avm_cad_Geometry", is_abstract=True)
avm_cad_Geometry2D = Class(name="avm_cad_Geometry2D", is_abstract=True)
Geometry = Class(name="Geometry")
avm_cad_Geometry3D = Class(name="avm_cad_Geometry3D", is_abstract=True)
avm_cad_Circle = Class(name="avm_cad_Circle")
Geometry2D = Class(name="Geometry2D")
PointReference = Class(name="PointReference")
avm_cad_Polygon = Class(name="avm_cad_Polygon")
avm_cad_ExtrudedGeometry = Class(name="avm_cad_ExtrudedGeometry")
Geometry3D = Class(name="Geometry3D")
avm_cad_Sphere = Class(name="avm_cad_Sphere")
avm_cad_CustomGeometry = Class(name="avm_cad_CustomGeometry")
CustomGeometryInput = Class(name="CustomGeometryInput")
avm_cad_CustomGeometryInput = Class(name="avm_cad_CustomGeometryInput")
avm_cad_PointReference = Class(name="avm_cad_PointReference")
Point = Class(name="Point")
avm_cad_Surface = Class(name="avm_cad_Surface")
PlaneReference = Class(name="PlaneReference")
avm_cad_PlaneReference = Class(name="avm_cad_PlaneReference")
avm_cad_GuideDatum = Class(name="avm_cad_GuideDatum")
ConnectorFeature = Class(name="ConnectorFeature")
avm_cad_AssemblyRoot = Class(name="avm_cad_AssemblyRoot")
DesignDomainFeature = Class(name="DesignDomainFeature")
cad_avm_ComponentInstance = Class(name="cad_avm_ComponentInstance")
avm_cad_KinematicJointSpec = Class(name="avm_cad_KinematicJointSpec", is_abstract=True)
avm_cad_RevoluteJointSpec = Class(name="avm_cad_RevoluteJointSpec")
KinematicJointSpec = Class(name="KinematicJointSpec")
Axis = Class(name="Axis")
avm_cad_TranslationalJointSpec = Class(name="avm_cad_TranslationalJointSpec")
avm_manufacturing_ManufacturingModel = Class(name="avm_manufacturing_ManufacturingModel")
avm_manufacturing_Parameter = Class(name="avm_manufacturing_Parameter")
manufacturing_avm_Value = Class(name="manufacturing_avm_Value")
avm_manufacturing_Metric = Class(name="avm_manufacturing_Metric")
avm_cyber_CyberModel = Class(name="avm_cyber_CyberModel")
avm_schematic_SchematicModel = Class(name="avm_schematic_SchematicModel", is_abstract=True)
Pin = Class(name="Pin")
avm_schematic_Pin = Class(name="avm_schematic_Pin")
eda_avm_Value = Class(name="eda_avm_Value")
avm_eda_PcbLayoutConstraint = Class(name="avm_eda_PcbLayoutConstraint", is_abstract=True)
ContainerFeature = Class(name="ContainerFeature")
avm_eda_EDAModel = Class(name="avm_eda_EDAModel")
SchematicModel = Class(name="SchematicModel")
eda_Parameter = Class(name="eda_Parameter")
avm_eda_Parameter = Class(name="avm_eda_Parameter")
avm_eda_ExactLayoutConstraint = Class(name="avm_eda_ExactLayoutConstraint")
PcbLayoutConstraint = Class(name="PcbLayoutConstraint")
eda_avm_ComponentInstance = Class(name="eda_avm_ComponentInstance")
eda_avm_Container = Class(name="eda_avm_Container")
avm_eda_RangeLayoutConstraint = Class(name="avm_eda_RangeLayoutConstraint")
avm_eda_RelativeLayoutConstraint = Class(name="avm_eda_RelativeLayoutConstraint")
spice_Parameter = Class(name="spice_Parameter")
avm_spice_Parameter = Class(name="avm_spice_Parameter")
avm_eda_RelativeRangeLayoutConstraint = Class(name="avm_eda_RelativeRangeLayoutConstraint")
avm_eda_GlobalLayoutConstraintException = Class(name="avm_eda_GlobalLayoutConstraintException")
avm_eda_CircuitLayout = Class(name="avm_eda_CircuitLayout")
avm_spice_SPICEModel = Class(name="avm_spice_SPICEModel")
spice_avm_Value = Class(name="spice_avm_Value")
avm_systemc_SystemCModel = Class(name="avm_systemc_SystemCModel")
SystemCPort = Class(name="SystemCPort")
avm_systemc_Parameter = Class(name="avm_systemc_Parameter")
systemc_avm_Value = Class(name="systemc_avm_Value")
avm_systemc_SystemCPort = Class(name="avm_systemc_SystemCPort")
avm_rf_RFModel = Class(name="avm_rf_RFModel")
RFPort = Class(name="RFPort")
FileReference = Class(name="FileReference")
avm_rf_RFPort = Class(name="avm_rf_RFPort")
avm_domainmapping_CAD2EDATransform = Class(name="avm_domainmapping_CAD2EDATransform")
DomainMapping = Class(name="DomainMapping")
eda_EDAModel = Class(name="eda_EDAModel")
CADModel = Class(name="CADModel")
avm_adamsCar_AdamsCarModel = Class(name="avm_adamsCar_AdamsCarModel")
avm_adamsCar_Parameter = Class(name="avm_adamsCar_Parameter")
adamsCar_avm_Value = Class(name="adamsCar_avm_Value")
avm_adamsCar_FileReference = Class(name="avm_adamsCar_FileReference")

# avm_Property class attributes and methods
avm_Property_Name: Property = Property(name="Name", type=StringType)
avm_Property_OnDataSheet: Property = Property(name="OnDataSheet", type=StringType)
avm_Property_Notes: Property = Property(name="Notes", type=StringType)
avm_Property_Definition: Property = Property(name="Definition", type=StringType)
avm_Property_ID: Property = Property(name="ID", type=StringType)
avm_Property_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Property_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Property.attributes={avm_Property_Notes, avm_Property_OnDataSheet, avm_Property_XPosition, avm_Property_YPosition, avm_Property_ID, avm_Property_Definition, avm_Property_Name}

# avm_Component class attributes and methods
avm_Component_Name: Property = Property(name="Name", type=StringType)
avm_Component_Version: Property = Property(name="Version", type=StringType)
avm_Component_SchemaVersion: Property = Property(name="SchemaVersion", type=StringType)
avm_Component_Classifications: Property = Property(name="Classifications", type=StringType)
avm_Component_ID: Property = Property(name="ID", type=StringType)
avm_Component_Supercedes: Property = Property(name="Supercedes", type=StringType)
avm_Component.attributes={avm_Component_Classifications, avm_Component_Version, avm_Component_Supercedes, avm_Component_Name, avm_Component_ID, avm_Component_SchemaVersion}

# avm_DomainModel class attributes and methods
avm_DomainModel_Author: Property = Property(name="Author", type=StringType)
avm_DomainModel_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModel_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModel_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModel_Name: Property = Property(name="Name", type=StringType)
avm_DomainModel_ID: Property = Property(name="ID", type=StringType)
avm_DomainModel.attributes={avm_DomainModel_ID, avm_DomainModel_Notes, avm_DomainModel_XPosition, avm_DomainModel_YPosition, avm_DomainModel_Author, avm_DomainModel_Name}

# avm_Value class attributes and methods
avm_Value_DimensionType: Property = Property(name="DimensionType", type=StringType)
avm_Value_DataType: Property = Property(name="DataType", type=StringType)
avm_Value_Dimensions: Property = Property(name="Dimensions", type=StringType)
avm_Value_Unit: Property = Property(name="Unit", type=StringType)
avm_Value.attributes={avm_Value_Dimensions, avm_Value_DimensionType, avm_Value_Unit, avm_Value_DataType}

# ValueNode class attributes and methods

# avm_ValueExpressionType class attributes and methods

# avm_Resource class attributes and methods
avm_Resource_Name: Property = Property(name="Name", type=StringType)
avm_Resource_Path: Property = Property(name="Path", type=StringType)
avm_Resource_Hash: Property = Property(name="Hash", type=StringType)
avm_Resource_ID: Property = Property(name="ID", type=StringType)
avm_Resource_Notes: Property = Property(name="Notes", type=StringType)
avm_Resource_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Resource_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Resource.attributes={avm_Resource_ID, avm_Resource_YPosition, avm_Resource_Name, avm_Resource_Hash, avm_Resource_Path, avm_Resource_Notes, avm_Resource_XPosition}

# avm_Connector class attributes and methods
avm_Connector_Definition: Property = Property(name="Definition", type=StringType)
avm_Connector_Name: Property = Property(name="Name", type=StringType)
avm_Connector_Notes: Property = Property(name="Notes", type=StringType)
avm_Connector_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Connector_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Connector.attributes={avm_Connector_Notes, avm_Connector_Definition, avm_Connector_Name, avm_Connector_YPosition, avm_Connector_XPosition}

# avm_DistributionRestriction class attributes and methods
avm_DistributionRestriction_Notes: Property = Property(name="Notes", type=StringType)
avm_DistributionRestriction.attributes={avm_DistributionRestriction_Notes}

# avm_Port class attributes and methods
avm_Port_Notes: Property = Property(name="Notes", type=StringType)
avm_Port_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Port_Definition: Property = Property(name="Definition", type=StringType)
avm_Port_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Port_Name: Property = Property(name="Name", type=StringType)
avm_Port.attributes={avm_Port_YPosition, avm_Port_Notes, avm_Port_Definition, avm_Port_Name, avm_Port_XPosition}

# avm_AnalysisConstruct class attributes and methods

# avm_Formula class attributes and methods
avm_Formula_Name: Property = Property(name="Name", type=StringType)
avm_Formula_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Formula_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Formula.attributes={avm_Formula_YPosition, avm_Formula_Name, avm_Formula_XPosition}

# avm_DomainMapping class attributes and methods

# avm_assemblyDetail class attributes and methods

# avm_DataSource class attributes and methods
avm_DataSource_Notes: Property = Property(name="Notes", type=StringType)
avm_DataSource.attributes={avm_DataSource_Notes}

# avm_FixedValue class attributes and methods
avm_FixedValue_Value: Property = Property(name="Value", type=StringType)
avm_FixedValue_Uncertainty: Property = Property(name="Uncertainty", type=StringType)
avm_FixedValue.attributes={avm_FixedValue_Uncertainty, avm_FixedValue_Value}

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

# avm_ConnectorFeature class attributes and methods

# PortMapTarget class attributes and methods

# avm_DomainModelPort class attributes and methods

# Port class attributes and methods

# avm_DomainModelParameter class attributes and methods
avm_DomainModelParameter_Notes: Property = Property(name="Notes", type=StringType)
avm_DomainModelParameter_XPosition: Property = Property(name="XPosition", type=StringType)
avm_DomainModelParameter_YPosition: Property = Property(name="YPosition", type=StringType)
avm_DomainModelParameter.attributes={avm_DomainModelParameter_XPosition, avm_DomainModelParameter_Notes, avm_DomainModelParameter_YPosition}

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
avm_DomainModelMetric.attributes={avm_DomainModelMetric_Notes, avm_DomainModelMetric_XPosition, avm_DomainModelMetric_ID, avm_DomainModelMetric_YPosition}

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
avm_Design.attributes={avm_Design_DesignSpaceSrcID, avm_Design_SchemaVersion, avm_Design_Name, avm_Design_DesignID}

# avm_Container class attributes and methods
avm_Container_XPosition: Property = Property(name="XPosition", type=StringType)
avm_Container_Name: Property = Property(name="Name", type=StringType)
avm_Container_YPosition: Property = Property(name="YPosition", type=StringType)
avm_Container_ID: Property = Property(name="ID", type=StringType)
avm_Container_Description: Property = Property(name="Description", type=StringType)
avm_Container_Classifications: Property = Property(name="Classifications", type=StringType)
avm_Container.attributes={avm_Container_XPosition, avm_Container_YPosition, avm_Container_Description, avm_Container_Classifications, avm_Container_ID, avm_Container_Name}

# avm_ContainerFeature class attributes and methods

# avm_DesignDomainFeature class attributes and methods

# avm_ComponentInstance class attributes and methods
avm_ComponentInstance_ComponentID: Property = Property(name="ComponentID", type=StringType)
avm_ComponentInstance_ID: Property = Property(name="ID", type=StringType)
avm_ComponentInstance_Name: Property = Property(name="Name", type=StringType)
avm_ComponentInstance_DesignSpaceSrcComponentID: Property = Property(name="DesignSpaceSrcComponentID", type=StringType)
avm_ComponentInstance_XPosition: Property = Property(name="XPosition", type=StringType)
avm_ComponentInstance_YPosition: Property = Property(name="YPosition", type=StringType)
avm_ComponentInstance.attributes={avm_ComponentInstance_ComponentID, avm_ComponentInstance_YPosition, avm_ComponentInstance_ID, avm_ComponentInstance_DesignSpaceSrcComponentID, avm_ComponentInstance_XPosition, avm_ComponentInstance_Name}

# avm_ComponentPortInstance class attributes and methods
avm_ComponentPortInstance_IDinComponentModel: Property = Property(name="IDinComponentModel", type=StringType)
avm_ComponentPortInstance.attributes={avm_ComponentPortInstance_IDinComponentModel}

# avm_Compound class attributes and methods

# Container class attributes and methods

# avm_Optional class attributes and methods

# DesignSpaceContainer class attributes and methods

# avm_Alternative class attributes and methods

# avm_ValueFlowMux class attributes and methods

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

# avm_TestBench class attributes and methods
avm_TestBench_Name: Property = Property(name="Name", type=StringType)
avm_TestBench.attributes={avm_TestBench_Name}

# avm_ComplexFormula class attributes and methods
avm_ComplexFormula_Expression: Property = Property(name="Expression", type=StringType)
avm_ComplexFormula.attributes={avm_ComplexFormula_Expression}

# avm_Operand class attributes and methods
avm_Operand_Symbol: Property = Property(name="Symbol", type=StringType)
avm_Operand.attributes={avm_Operand_Symbol}

# avm_DoDDistributionStatement class attributes and methods
avm_DoDDistributionStatement_Type: Property = Property(name="Type", type=StringType)
avm_DoDDistributionStatement.attributes={avm_DoDDistributionStatement_Type}

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
avm_ContainerInstanceBase.attributes={avm_ContainerInstanceBase_IDinSourceModel, avm_ContainerInstanceBase_XPosition, avm_ContainerInstanceBase_YPosition}

# avm_TestBenchValueBase class attributes and methods
avm_TestBenchValueBase_ID: Property = Property(name="ID", type=StringType)
avm_TestBenchValueBase_Name: Property = Property(name="Name", type=StringType)
avm_TestBenchValueBase_Notes: Property = Property(name="Notes", type=StringType)
avm_TestBenchValueBase_XPosition: Property = Property(name="XPosition", type=StringType)
avm_TestBenchValueBase_YPosition: Property = Property(name="YPosition", type=StringType)
avm_TestBenchValueBase.attributes={avm_TestBenchValueBase_Notes, avm_TestBenchValueBase_Name, avm_TestBenchValueBase_YPosition, avm_TestBenchValueBase_ID, avm_TestBenchValueBase_XPosition}

# avm_WorkflowTaskBase class attributes and methods
avm_WorkflowTaskBase_Name: Property = Property(name="Name", type=StringType)
avm_WorkflowTaskBase.attributes={avm_WorkflowTaskBase_Name}

# avm_InterpreterTask class attributes and methods
avm_InterpreterTask_Parameters: Property = Property(name="Parameters", type=StringType)
avm_InterpreterTask_COMName: Property = Property(name="COMName", type=StringType)
avm_InterpreterTask.attributes={avm_InterpreterTask_Parameters, avm_InterpreterTask_COMName}

# WorkflowTaskBase class attributes and methods

# modelica_avm_Value class attributes and methods

# avm_ExecutionTask class attributes and methods
avm_ExecutionTask_Description: Property = Property(name="Description", type=StringType)
avm_ExecutionTask_Invocation: Property = Property(name="Invocation", type=StringType)
avm_ExecutionTask.attributes={avm_ExecutionTask_Description, avm_ExecutionTask_Invocation}

# avm_modelica_ModelicaModel class attributes and methods
avm_modelica_ModelicaModel_Class: Property = Property(name="Class", type=StringType)
avm_modelica_ModelicaModel.attributes={avm_modelica_ModelicaModel_Class}

# DomainModel_ class attributes and methods

# Parameter class attributes and methods

# Connector class attributes and methods

# Metric class attributes and methods

# Limit class attributes and methods

# Redeclare class attributes and methods

# avm_modelica_Connector class attributes and methods
avm_modelica_Connector_Class: Property = Property(name="Class", type=StringType)
avm_modelica_Connector_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Connector.attributes={avm_modelica_Connector_Locator, avm_modelica_Connector_Class}

# DomainModelPort class attributes and methods

# avm_modelica_Parameter class attributes and methods
avm_modelica_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Parameter.attributes={avm_modelica_Parameter_Locator}

# DomainModelParameter class attributes and methods

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
avm_modelica_Limit.attributes={avm_modelica_Limit_Name, avm_modelica_Limit_BoundType, avm_modelica_Limit_Notes, avm_modelica_Limit_ToleranceTimeWindow, avm_modelica_Limit_VariableLocator}

# avm_modelica_Redeclare class attributes and methods
avm_modelica_Redeclare_Locator: Property = Property(name="Locator", type=StringType)
avm_modelica_Redeclare_Type: Property = Property(name="Type", type=StringType)
avm_modelica_Redeclare.attributes={avm_modelica_Redeclare_Locator, avm_modelica_Redeclare_Type}

# avm_modelica_SolverSettings class attributes and methods
avm_modelica_SolverSettings_Tolerance: Property = Property(name="Tolerance", type=StringType)
avm_modelica_SolverSettings_Solver: Property = Property(name="Solver", type=StringType)
avm_modelica_SolverSettings_JobManagerToolSelection: Property = Property(name="JobManagerToolSelection", type=StringType)
avm_modelica_SolverSettings_StartTime: Property = Property(name="StartTime", type=StringType)
avm_modelica_SolverSettings_StopTime: Property = Property(name="StopTime", type=StringType)
avm_modelica_SolverSettings_IntervalMethod: Property = Property(name="IntervalMethod", type=StringType)
avm_modelica_SolverSettings_NumberOfIntervals: Property = Property(name="NumberOfIntervals", type=StringType)
avm_modelica_SolverSettings_IntervalLength: Property = Property(name="IntervalLength", type=StringType)
avm_modelica_SolverSettings_ToolSpecificAnnotations: Property = Property(name="ToolSpecificAnnotations", type=StringType)
avm_modelica_SolverSettings.attributes={avm_modelica_SolverSettings_Tolerance, avm_modelica_SolverSettings_IntervalLength, avm_modelica_SolverSettings_StartTime, avm_modelica_SolverSettings_JobManagerToolSelection, avm_modelica_SolverSettings_StopTime, avm_modelica_SolverSettings_ToolSpecificAnnotations, avm_modelica_SolverSettings_IntervalMethod, avm_modelica_SolverSettings_NumberOfIntervals, avm_modelica_SolverSettings_Solver}

# Settings class attributes and methods

# AnalysisConstruct class attributes and methods

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
avm_cyber_CyberModel.attributes={avm_cyber_CyberModel_Class, avm_cyber_CyberModel_Type, avm_cyber_CyberModel_Locator}

# avm_schematic_SchematicModel class attributes and methods

# Pin class attributes and methods

# avm_schematic_Pin class attributes and methods
avm_schematic_Pin_EDASymbolLocationY: Property = Property(name="EDASymbolLocationY", type=StringType)
avm_schematic_Pin_EDASymbolRotation: Property = Property(name="EDASymbolRotation", type=StringType)
avm_schematic_Pin_SPICEPortNumber: Property = Property(name="SPICEPortNumber", type=StringType)
avm_schematic_Pin_EDAGate: Property = Property(name="EDAGate", type=StringType)
avm_schematic_Pin_EDASymbolLocationX: Property = Property(name="EDASymbolLocationX", type=StringType)
avm_schematic_Pin.attributes={avm_schematic_Pin_SPICEPortNumber, avm_schematic_Pin_EDASymbolLocationY, avm_schematic_Pin_EDASymbolLocationX, avm_schematic_Pin_EDAGate, avm_schematic_Pin_EDASymbolRotation}

# eda_avm_Value class attributes and methods

# avm_eda_PcbLayoutConstraint class attributes and methods
avm_eda_PcbLayoutConstraint_XPosition: Property = Property(name="XPosition", type=StringType)
avm_eda_PcbLayoutConstraint_YPosition: Property = Property(name="YPosition", type=StringType)
avm_eda_PcbLayoutConstraint_Notes: Property = Property(name="Notes", type=StringType)
avm_eda_PcbLayoutConstraint.attributes={avm_eda_PcbLayoutConstraint_Notes, avm_eda_PcbLayoutConstraint_XPosition, avm_eda_PcbLayoutConstraint_YPosition}

# ContainerFeature class attributes and methods

# avm_eda_EDAModel class attributes and methods
avm_eda_EDAModel_Library: Property = Property(name="Library", type=StringType)
avm_eda_EDAModel_DeviceSet: Property = Property(name="DeviceSet", type=StringType)
avm_eda_EDAModel_Device: Property = Property(name="Device", type=StringType)
avm_eda_EDAModel_Package: Property = Property(name="Package", type=StringType)
avm_eda_EDAModel_HasMultiLayerFootprint: Property = Property(name="HasMultiLayerFootprint", type=StringType)
avm_eda_EDAModel.attributes={avm_eda_EDAModel_HasMultiLayerFootprint, avm_eda_EDAModel_Library, avm_eda_EDAModel_Device, avm_eda_EDAModel_DeviceSet, avm_eda_EDAModel_Package}

# SchematicModel class attributes and methods

# eda_Parameter class attributes and methods

# avm_eda_Parameter class attributes and methods
avm_eda_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_eda_Parameter.attributes={avm_eda_Parameter_Locator}

# avm_eda_ExactLayoutConstraint class attributes and methods
avm_eda_ExactLayoutConstraint_X: Property = Property(name="X", type=StringType)
avm_eda_ExactLayoutConstraint_Y: Property = Property(name="Y", type=StringType)
avm_eda_ExactLayoutConstraint_Layer: Property = Property(name="Layer", type=StringType)
avm_eda_ExactLayoutConstraint_Rotation: Property = Property(name="Rotation", type=StringType)
avm_eda_ExactLayoutConstraint.attributes={avm_eda_ExactLayoutConstraint_Rotation, avm_eda_ExactLayoutConstraint_X, avm_eda_ExactLayoutConstraint_Y, avm_eda_ExactLayoutConstraint_Layer}

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
avm_eda_RangeLayoutConstraint.attributes={avm_eda_RangeLayoutConstraint_XRangeMax, avm_eda_RangeLayoutConstraint_XRangeMin, avm_eda_RangeLayoutConstraint_Type, avm_eda_RangeLayoutConstraint_LayerRange, avm_eda_RangeLayoutConstraint_YRangeMax, avm_eda_RangeLayoutConstraint_YRangeMin}

# avm_eda_RelativeLayoutConstraint class attributes and methods
avm_eda_RelativeLayoutConstraint_XOffset: Property = Property(name="XOffset", type=StringType)
avm_eda_RelativeLayoutConstraint_YOffset: Property = Property(name="YOffset", type=StringType)
avm_eda_RelativeLayoutConstraint_RelativeLayer: Property = Property(name="RelativeLayer", type=StringType)
avm_eda_RelativeLayoutConstraint_RelativeRotation: Property = Property(name="RelativeRotation", type=StringType)
avm_eda_RelativeLayoutConstraint.attributes={avm_eda_RelativeLayoutConstraint_RelativeLayer, avm_eda_RelativeLayoutConstraint_XOffset, avm_eda_RelativeLayoutConstraint_YOffset, avm_eda_RelativeLayoutConstraint_RelativeRotation}

# spice_Parameter class attributes and methods

# avm_spice_Parameter class attributes and methods
avm_spice_Parameter_Locator: Property = Property(name="Locator", type=StringType)
avm_spice_Parameter.attributes={avm_spice_Parameter_Locator}

# avm_eda_RelativeRangeLayoutConstraint class attributes and methods
avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMin: Property = Property(name="XRelativeRangeMin", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMax: Property = Property(name="XRelativeRangeMax", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMin: Property = Property(name="YRelativeRangeMin", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMax: Property = Property(name="YRelativeRangeMax", type=StringType)
avm_eda_RelativeRangeLayoutConstraint_RelativeLayer: Property = Property(name="RelativeLayer", type=StringType)
avm_eda_RelativeRangeLayoutConstraint.attributes={avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMax, avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMax, avm_eda_RelativeRangeLayoutConstraint_XRelativeRangeMin, avm_eda_RelativeRangeLayoutConstraint_YRelativeRangeMin, avm_eda_RelativeRangeLayoutConstraint_RelativeLayer}

# avm_eda_GlobalLayoutConstraintException class attributes and methods
avm_eda_GlobalLayoutConstraintException_Constraint: Property = Property(name="Constraint", type=StringType)
avm_eda_GlobalLayoutConstraintException.attributes={avm_eda_GlobalLayoutConstraintException_Constraint}

# avm_eda_CircuitLayout class attributes and methods
avm_eda_CircuitLayout_BoundingBoxes: Property = Property(name="BoundingBoxes", type=StringType)
avm_eda_CircuitLayout.attributes={avm_eda_CircuitLayout_BoundingBoxes}

# avm_spice_SPICEModel class attributes and methods
avm_spice_SPICEModel_Class: Property = Property(name="Class", type=StringType)
avm_spice_SPICEModel.attributes={avm_spice_SPICEModel_Class}

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
avm_systemc_SystemCPort.attributes={avm_systemc_SystemCPort_Directionality, avm_systemc_SystemCPort_DataTypeDimension, avm_systemc_SystemCPort_Function, avm_systemc_SystemCPort_DataType}

# avm_rf_RFModel class attributes and methods
avm_rf_RFModel_Rotation: Property = Property(name="Rotation", type=StringType)
avm_rf_RFModel_X: Property = Property(name="X", type=StringType)
avm_rf_RFModel_Y: Property = Property(name="Y", type=StringType)
avm_rf_RFModel.attributes={avm_rf_RFModel_Rotation, avm_rf_RFModel_Y, avm_rf_RFModel_X}

# RFPort class attributes and methods

# FileReference class attributes and methods

# avm_rf_RFPort class attributes and methods
avm_rf_RFPort_Directionality: Property = Property(name="Directionality", type=StringType)
avm_rf_RFPort_NominalImpedance: Property = Property(name="NominalImpedance", type=StringType)
avm_rf_RFPort.attributes={avm_rf_RFPort_NominalImpedance, avm_rf_RFPort_Directionality}

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
avm_domainmapping_CAD2EDATransform.attributes={avm_domainmapping_CAD2EDATransform_TranslationY, avm_domainmapping_CAD2EDATransform_RotationY, avm_domainmapping_CAD2EDATransform_ScaleX, avm_domainmapping_CAD2EDATransform_RotationZ, avm_domainmapping_CAD2EDATransform_TranslationZ, avm_domainmapping_CAD2EDATransform_ScaleY, avm_domainmapping_CAD2EDATransform_RotationX, avm_domainmapping_CAD2EDATransform_TranslationX, avm_domainmapping_CAD2EDATransform_ScaleZ}

# DomainMapping class attributes and methods

# eda_EDAModel class attributes and methods

# CADModel class attributes and methods

# avm_adamsCar_AdamsCarModel class attributes and methods

# avm_adamsCar_Parameter class attributes and methods
avm_adamsCar_Parameter_ID: Property = Property(name="ID", type=StringType)
avm_adamsCar_Parameter_Name: Property = Property(name="Name", type=StringType)
avm_adamsCar_Parameter.attributes={avm_adamsCar_Parameter_Name, avm_adamsCar_Parameter_ID}

# adamsCar_avm_Value class attributes and methods

# avm_adamsCar_FileReference class attributes and methods
avm_adamsCar_FileReference_FilePath: Property = Property(name="FilePath", type=StringType)
avm_adamsCar_FileReference_ID: Property = Property(name="ID", type=StringType)
avm_adamsCar_FileReference_Name: Property = Property(name="Name", type=StringType)
avm_adamsCar_FileReference.attributes={avm_adamsCar_FileReference_ID, avm_adamsCar_FileReference_FilePath, avm_adamsCar_FileReference_Name}

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
StandardDeviation50: BinaryAssociation = BinaryAssociation(
    name="StandardDeviation50",
    ends={
        Property(name="avm_ValueExpressionType52", type=avm_NormalDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_NormalDistribution51", type=avm_ValueExpressionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
RootContainer69: BinaryAssociation = BinaryAssociation(
    name="RootContainer69",
    ends={
        Property(name="avm_Container", type=avm_Design, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Design", type=avm_Container, multiplicity=Multiplicity(0, 1), is_composite=True)
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
FromResource66: BinaryAssociation = BinaryAssociation(
    name="FromResource66",
    ends={
        Property(name="avm_Resource68", type=avm_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_DataSource67", type=avm_Resource, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerFeature95: BinaryAssociation = BinaryAssociation(
    name="ContainerFeature95",
    ends={
        Property(name="avm_ContainerFeature", type=avm_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_Container96", type=avm_ContainerFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
PortInstance107: BinaryAssociation = BinaryAssociation(
    name="PortInstance107",
    ends={
        Property(name="avm_ComponentPortInstance", type=avm_ComponentInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ComponentInstance108", type=avm_ComponentPortInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
TopLevelSystemUnderTest129: BinaryAssociation = BinaryAssociation(
    name="TopLevelSystemUnderTest129",
    ends={
        Property(name="avm_TopLevelSystemUnderTest", type=avm_TestBench, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_TestBench", type=avm_TopLevelSystemUnderTest, multiplicity=Multiplicity(0, 1), is_composite=True)
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
Value167: BinaryAssociation = BinaryAssociation(
    name="Value167",
    ends={
        Property(name="modelica_avm_Value", type=avm_modelica_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_Parameter", type=modelica_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Source150: BinaryAssociation = BinaryAssociation(
    name="Source150",
    ends={
        Property(name="avm_ValueNode152", type=avm_ValueFlowMux, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_ValueFlowMux151", type=avm_ValueNode, multiplicity=Multiplicity(0, 9999))
    }
)
Parameter153: BinaryAssociation = BinaryAssociation(
    name="Parameter153",
    ends={
        Property(name="Parameter", type=avm_modelica_ModelicaModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_modelica_ModelicaModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
Datum172: BinaryAssociation = BinaryAssociation(
    name="Datum172",
    ends={
        Property(name="Datum", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel", type=Datum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter173: BinaryAssociation = BinaryAssociation(
    name="Parameter173",
    ends={
        Property(name="Parameter175", type=avm_cad_CADModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CADModel174", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
DirectionReferencePoint195: BinaryAssociation = BinaryAssociation(
    name="DirectionReferencePoint195",
    ends={
        Property(name="PointReference197", type=avm_cad_ExtrudedGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_ExtrudedGeometry196", type=PointReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SphereCenter198: BinaryAssociation = BinaryAssociation(
    name="SphereCenter198",
    ends={
        Property(name="PointReference199", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SphereEdge200: BinaryAssociation = BinaryAssociation(
    name="SphereEdge200",
    ends={
        Property(name="PointReference202", type=avm_cad_Sphere, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Sphere201", type=PointReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
CustomGeometryInput203: BinaryAssociation = BinaryAssociation(
    name="CustomGeometryInput203",
    ends={
        Property(name="CustomGeometryInput", type=avm_cad_CustomGeometry, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometry", type=CustomGeometryInput, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
InputGeometry204: BinaryAssociation = BinaryAssociation(
    name="InputGeometry204",
    ends={
        Property(name="Geometry", type=avm_cad_CustomGeometryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_CustomGeometryInput", type=Geometry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReferredPoint205: BinaryAssociation = BinaryAssociation(
    name="ReferredPoint205",
    ends={
        Property(name="Point", type=avm_cad_PointReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PointReference", type=Point, multiplicity=Multiplicity(0, 9999))
    }
)
MinimumTranslation233: BinaryAssociation = BinaryAssociation(
    name="MinimumTranslation233",
    ends={
        Property(name="cad_avm_Value235", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec234", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultTranslation236: BinaryAssociation = BinaryAssociation(
    name="DefaultTranslation236",
    ends={
        Property(name="cad_avm_Value238", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec237", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ReferencePlane206: BinaryAssociation = BinaryAssociation(
    name="ReferencePlane206",
    ends={
        Property(name="PlaneReference", type=avm_cad_Surface, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_Surface", type=PlaneReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ReferredPlane207: BinaryAssociation = BinaryAssociation(
    name="ReferredPlane207",
    ends={
        Property(name="Plane208", type=avm_cad_PlaneReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_PlaneReference", type=Plane, multiplicity=Multiplicity(0, 9999))
    }
)
Datum209: BinaryAssociation = BinaryAssociation(
    name="Datum209",
    ends={
        Property(name="Datum210", type=avm_cad_GuideDatum, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_GuideDatum", type=Datum, multiplicity=Multiplicity(1, 1))
    }
)
AssemblyRootComponentInstance211: BinaryAssociation = BinaryAssociation(
    name="AssemblyRootComponentInstance211",
    ends={
        Property(name="cad_avm_ComponentInstance", type=avm_cad_AssemblyRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_AssemblyRoot", type=cad_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentPlane212: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane212",
    ends={
        Property(name="Plane213", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis214: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis214",
    ends={
        Property(name="Axis", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec215", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
RotationLimitReference216: BinaryAssociation = BinaryAssociation(
    name="RotationLimitReference216",
    ends={
        Property(name="Plane218", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec217", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
MinimumRotation219: BinaryAssociation = BinaryAssociation(
    name="MinimumRotation219",
    ends={
        Property(name="cad_avm_Value221", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec220", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
DefaultRotation222: BinaryAssociation = BinaryAssociation(
    name="DefaultRotation222",
    ends={
        Property(name="cad_avm_Value224", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec223", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MaximumRotation225: BinaryAssociation = BinaryAssociation(
    name="MaximumRotation225",
    ends={
        Property(name="cad_avm_Value227", type=avm_cad_RevoluteJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_RevoluteJointSpec226", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
AlignmentPlane228: BinaryAssociation = BinaryAssociation(
    name="AlignmentPlane228",
    ends={
        Property(name="Plane229", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec", type=Plane, multiplicity=Multiplicity(1, 1))
    }
)
AlignmentAxis230: BinaryAssociation = BinaryAssociation(
    name="AlignmentAxis230",
    ends={
        Property(name="Axis232", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec231", type=Axis, multiplicity=Multiplicity(1, 1))
    }
)
MaximumTranslation239: BinaryAssociation = BinaryAssociation(
    name="MaximumTranslation239",
    ends={
        Property(name="cad_avm_Value241", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec240", type=cad_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TranslationLimitReference242: BinaryAssociation = BinaryAssociation(
    name="TranslationLimitReference242",
    ends={
        Property(name="Plane244", type=avm_cad_TranslationalJointSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cad_TranslationalJointSpec243", type=Plane, multiplicity=Multiplicity(0, 1))
    }
)
Parameter245: BinaryAssociation = BinaryAssociation(
    name="Parameter245",
    ends={
        Property(name="Parameter246", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Metric247: BinaryAssociation = BinaryAssociation(
    name="Metric247",
    ends={
        Property(name="Metric249", type=avm_manufacturing_ManufacturingModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_ManufacturingModel248", type=Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value250: BinaryAssociation = BinaryAssociation(
    name="Value250",
    ends={
        Property(name="manufacturing_avm_Value", type=avm_manufacturing_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_manufacturing_Parameter", type=manufacturing_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Connector251: BinaryAssociation = BinaryAssociation(
    name="Connector251",
    ends={
        Property(name="Connector252", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel", type=Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter253: BinaryAssociation = BinaryAssociation(
    name="Parameter253",
    ends={
        Property(name="Parameter255", type=avm_cyber_CyberModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_cyber_CyberModel254", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Pin256: BinaryAssociation = BinaryAssociation(
    name="Pin256",
    ends={
        Property(name="Pin", type=avm_schematic_SchematicModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_schematic_SchematicModel", type=Pin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value258: BinaryAssociation = BinaryAssociation(
    name="Value258",
    ends={
        Property(name="eda_avm_Value", type=avm_eda_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_Parameter", type=eda_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Parameter257: BinaryAssociation = BinaryAssociation(
    name="Parameter257",
    ends={
        Property(name="eda_Parameter", type=avm_eda_EDAModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_EDAModel", type=eda_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ConstraintTarget259: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget259",
    ends={
        Property(name="eda_avm_ComponentInstance", type=avm_eda_ExactLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_ExactLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget260: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget260",
    ends={
        Property(name="eda_avm_Container", type=avm_eda_ExactLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_ExactLayoutConstraint261", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget262: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget262",
    ends={
        Property(name="eda_avm_ComponentInstance263", type=avm_eda_RangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RangeLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget264: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget264",
    ends={
        Property(name="eda_avm_Container266", type=avm_eda_RangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RangeLayoutConstraint265", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget267: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget267",
    ends={
        Property(name="eda_avm_ComponentInstance268", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
Origin269: BinaryAssociation = BinaryAssociation(
    name="Origin269",
    ends={
        Property(name="eda_avm_ComponentInstance271", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint270", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
ContainerConstraintTarget272: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget272",
    ends={
        Property(name="eda_avm_Container274", type=avm_eda_RelativeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeLayoutConstraint273", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
Parameter288: BinaryAssociation = BinaryAssociation(
    name="Parameter288",
    ends={
        Property(name="spice_Parameter", type=avm_spice_SPICEModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_spice_SPICEModel", type=spice_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ContainerConstraintTarget275: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget275",
    ends={
        Property(name="eda_avm_Container276", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
Origin277: BinaryAssociation = BinaryAssociation(
    name="Origin277",
    ends={
        Property(name="eda_avm_ComponentInstance279", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint278", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(1, 1))
    }
)
ConstraintTarget280: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget280",
    ends={
        Property(name="eda_avm_ComponentInstance282", type=avm_eda_RelativeRangeLayoutConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_RelativeRangeLayoutConstraint281", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ConstraintTarget283: BinaryAssociation = BinaryAssociation(
    name="ConstraintTarget283",
    ends={
        Property(name="eda_avm_ComponentInstance284", type=avm_eda_GlobalLayoutConstraintException, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_GlobalLayoutConstraintException", type=eda_avm_ComponentInstance, multiplicity=Multiplicity(0, 9999))
    }
)
ContainerConstraintTarget285: BinaryAssociation = BinaryAssociation(
    name="ContainerConstraintTarget285",
    ends={
        Property(name="eda_avm_Container287", type=avm_eda_GlobalLayoutConstraintException, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_eda_GlobalLayoutConstraintException286", type=eda_avm_Container, multiplicity=Multiplicity(0, 9999))
    }
)
Value289: BinaryAssociation = BinaryAssociation(
    name="Value289",
    ends={
        Property(name="spice_avm_Value", type=avm_spice_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_spice_Parameter", type=spice_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
SystemCPort290: BinaryAssociation = BinaryAssociation(
    name="SystemCPort290",
    ends={
        Property(name="SystemCPort", type=avm_systemc_SystemCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_SystemCModel", type=SystemCPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Parameter291: BinaryAssociation = BinaryAssociation(
    name="Parameter291",
    ends={
        Property(name="Parameter293", type=avm_systemc_SystemCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_SystemCModel292", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value294: BinaryAssociation = BinaryAssociation(
    name="Value294",
    ends={
        Property(name="systemc_avm_Value", type=avm_systemc_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_systemc_Parameter", type=systemc_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RFPort295: BinaryAssociation = BinaryAssociation(
    name="RFPort295",
    ends={
        Property(name="RFPort", type=avm_rf_RFModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_rf_RFModel", type=RFPort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FileReference301: BinaryAssociation = BinaryAssociation(
    name="FileReference301",
    ends={
        Property(name="FileReference", type=avm_adamsCar_AdamsCarModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_AdamsCarModel302", type=FileReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
EDAModel296: BinaryAssociation = BinaryAssociation(
    name="EDAModel296",
    ends={
        Property(name="eda_EDAModel", type=avm_domainmapping_CAD2EDATransform, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_domainmapping_CAD2EDATransform", type=eda_EDAModel, multiplicity=Multiplicity(1, 1))
    }
)
CADModel297: BinaryAssociation = BinaryAssociation(
    name="CADModel297",
    ends={
        Property(name="CADModel", type=avm_domainmapping_CAD2EDATransform, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_domainmapping_CAD2EDATransform298", type=CADModel, multiplicity=Multiplicity(1, 1))
    }
)
Parameter299: BinaryAssociation = BinaryAssociation(
    name="Parameter299",
    ends={
        Property(name="Parameter300", type=avm_adamsCar_AdamsCarModel, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_AdamsCarModel", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Value303: BinaryAssociation = BinaryAssociation(
    name="Value303",
    ends={
        Property(name="adamsCar_avm_Value", type=avm_adamsCar_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_Parameter", type=adamsCar_avm_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ParameterSwap304: BinaryAssociation = BinaryAssociation(
    name="ParameterSwap304",
    ends={
        Property(name="Parameter305", type=avm_adamsCar_FileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_FileReference", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
FileReferenceSwap306: BinaryAssociation = BinaryAssociation(
    name="FileReferenceSwap306",
    ends={
        Property(name="FileReference308", type=avm_adamsCar_FileReference, multiplicity=Multiplicity(1, 1)),
        Property(name="avm_adamsCar_FileReference307", type=FileReference, multiplicity=Multiplicity(0, 9999))
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
gen_avm_Metric_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Metric)
gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TopLevelSystemUnderTest)
gen_avm_Parameter_TestBenchValueBase = Generalization(general=TestBenchValueBase, specific=avm_Parameter)
gen_avm_TestInjectionPoint_ContainerInstanceBase = Generalization(general=ContainerInstanceBase, specific=avm_TestInjectionPoint)
gen_avm_InterpreterTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_InterpreterTask)
gen_avm_ExecutionTask_WorkflowTaskBase = Generalization(general=WorkflowTaskBase, specific=avm_ExecutionTask)
gen_avm_ValueFlowMux_ValueNode = Generalization(general=ValueNode, specific=avm_ValueFlowMux)
gen_avm_modelica_ModelicaModel_DomainModel = Generalization(general=DomainModel_, specific=avm_modelica_ModelicaModel)
gen_avm_modelica_Connector_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_modelica_Connector)
gen_avm_modelica_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Parameter)
gen_avm_modelica_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_modelica_Metric)
gen_avm_modelica_Redeclare_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_modelica_Redeclare)
gen_avm_modelica_SolverSettings_Settings = Generalization(general=Settings, specific=avm_modelica_SolverSettings)
gen_avm_cad_Geometry_AnalysisConstruct = Generalization(general=AnalysisConstruct, specific=avm_cad_Geometry)
gen_avm_cad_CADModel_DomainModel = Generalization(general=DomainModel_, specific=avm_cad_CADModel)
gen_avm_cad_Datum_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_cad_Datum)
gen_avm_cad_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_cad_Parameter)
gen_avm_cad_Point_Datum = Generalization(general=Datum, specific=avm_cad_Point)
gen_avm_cad_Axis_Datum = Generalization(general=Datum, specific=avm_cad_Axis)
gen_avm_cad_Plane_Datum = Generalization(general=Datum, specific=avm_cad_Plane)
gen_avm_cad_CoordinateSystem_Datum = Generalization(general=Datum, specific=avm_cad_CoordinateSystem)
gen_avm_cad_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_cad_Metric)
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
gen_avm_manufacturing_ManufacturingModel_DomainModel = Generalization(general=DomainModel_, specific=avm_manufacturing_ManufacturingModel)
gen_avm_manufacturing_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_manufacturing_Parameter)
gen_avm_manufacturing_Metric_DomainModelMetric = Generalization(general=DomainModelMetric, specific=avm_manufacturing_Metric)
gen_avm_cyber_CyberModel_DomainModel = Generalization(general=DomainModel_, specific=avm_cyber_CyberModel)
gen_avm_schematic_SchematicModel_DomainModel = Generalization(general=DomainModel_, specific=avm_schematic_SchematicModel)
gen_avm_schematic_Pin_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_schematic_Pin)
gen_avm_eda_PcbLayoutConstraint_ContainerFeature = Generalization(general=ContainerFeature, specific=avm_eda_PcbLayoutConstraint)
gen_avm_eda_EDAModel_SchematicModel = Generalization(general=SchematicModel, specific=avm_eda_EDAModel)
gen_avm_eda_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_eda_Parameter)
gen_avm_eda_ExactLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_ExactLayoutConstraint)
gen_avm_eda_RangeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RangeLayoutConstraint)
gen_avm_eda_RelativeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RelativeLayoutConstraint)
gen_avm_spice_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_spice_Parameter)
gen_avm_eda_RelativeRangeLayoutConstraint_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_RelativeRangeLayoutConstraint)
gen_avm_eda_GlobalLayoutConstraintException_PcbLayoutConstraint = Generalization(general=PcbLayoutConstraint, specific=avm_eda_GlobalLayoutConstraintException)
gen_avm_eda_CircuitLayout_DomainModel = Generalization(general=DomainModel_, specific=avm_eda_CircuitLayout)
gen_avm_spice_SPICEModel_SchematicModel = Generalization(general=SchematicModel, specific=avm_spice_SPICEModel)
gen_avm_systemc_SystemCModel_DomainModel = Generalization(general=DomainModel_, specific=avm_systemc_SystemCModel)
gen_avm_systemc_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_systemc_Parameter)
gen_avm_systemc_SystemCPort_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_systemc_SystemCPort)
gen_avm_rf_RFModel_DomainModel = Generalization(general=DomainModel_, specific=avm_rf_RFModel)
gen_avm_rf_RFPort_DomainModelPort = Generalization(general=DomainModelPort, specific=avm_rf_RFPort)
gen_avm_domainmapping_CAD2EDATransform_DomainMapping = Generalization(general=DomainMapping, specific=avm_domainmapping_CAD2EDATransform)
gen_avm_adamsCar_AdamsCarModel_DomainModel = Generalization(general=DomainModel_, specific=avm_adamsCar_AdamsCarModel)
gen_avm_adamsCar_Parameter_DomainModelParameter = Generalization(general=DomainModelParameter, specific=avm_adamsCar_Parameter)

# Domain Model
domain_model = DomainModel(
    name="avm",
    types={avm_Property, avm_Component, avm_DomainModel, avm_Value, ValueNode, avm_ValueExpressionType, avm_Resource, avm_Connector, avm_DistributionRestriction, avm_Port, avm_AnalysisConstruct, avm_Formula, avm_DomainMapping, avm_assemblyDetail, avm_DataSource, avm_FixedValue, ValueExpressionType, avm_CalculatedValue, avm_DerivedValue, avm_ValueNode, ConnectorCompositionTarget, avm_ConnectorFeature, PortMapTarget, avm_DomainModelPort, Port, avm_DomainModelParameter, avm_ParametricValue, avm_ProbabilisticValue, avm_NormalDistribution, ProbabilisticValue, avm_SecurityClassification, DistributionRestriction, avm_Proprietary, avm_ITAR, avm_DomainModelMetric, avm_UniformDistribution, avm_PrimitiveProperty, Property_, avm_CompoundProperty, avm_ParametricEnumeratedValue, avm_AbstractPort, avm_Design, avm_Container, avm_ContainerFeature, avm_DesignDomainFeature, avm_ComponentInstance, avm_ComponentPortInstance, avm_Compound, Container, avm_Optional, DesignSpaceContainer, avm_Alternative, avm_ValueFlowMux, avm_ComponentPrimitivePropertyInstance, avm_ComponentConnectorInstance, avm_DesignSpaceContainer, avm_PortMapTarget, avm_ConnectorCompositionTarget, avm_SimpleFormula, Formula, avm_TestBench, avm_ComplexFormula, avm_Operand, avm_DoDDistributionStatement, avm_TopLevelSystemUnderTest, avm_Parameter, avm_Metric, avm_TestInjectionPoint, avm_Workflow, avm_Settings, ContainerInstanceBase, TestBenchValueBase, avm_ContainerInstanceBase, avm_TestBenchValueBase, avm_WorkflowTaskBase, avm_InterpreterTask, WorkflowTaskBase, modelica_avm_Value, avm_ExecutionTask, avm_modelica_ModelicaModel, DomainModel_, Parameter_, Connector, Metric, Limit, Redeclare, avm_modelica_Connector, DomainModelPort, avm_modelica_Parameter, DomainModelParameter, avm_modelica_Metric, DomainModelMetric, avm_modelica_Limit, avm_modelica_Redeclare, avm_modelica_SolverSettings, Settings, AnalysisConstruct, avm_cad_CADModel, Datum, avm_cad_Datum, avm_cad_Parameter, cad_avm_Value, avm_cad_Point, avm_cad_Axis, avm_cad_Plane, Plane, avm_cad_CoordinateSystem, avm_cad_Metric, avm_cad_Geometry, avm_cad_Geometry2D, Geometry, avm_cad_Geometry3D, avm_cad_Circle, Geometry2D, PointReference, avm_cad_Polygon, avm_cad_ExtrudedGeometry, Geometry3D, avm_cad_Sphere, avm_cad_CustomGeometry, CustomGeometryInput, avm_cad_CustomGeometryInput, avm_cad_PointReference, Point, avm_cad_Surface, PlaneReference, avm_cad_PlaneReference, avm_cad_GuideDatum, ConnectorFeature, avm_cad_AssemblyRoot, DesignDomainFeature, cad_avm_ComponentInstance, avm_cad_KinematicJointSpec, avm_cad_RevoluteJointSpec, KinematicJointSpec, Axis, avm_cad_TranslationalJointSpec, avm_manufacturing_ManufacturingModel, avm_manufacturing_Parameter, manufacturing_avm_Value, avm_manufacturing_Metric, avm_cyber_CyberModel, avm_schematic_SchematicModel, Pin, avm_schematic_Pin, eda_avm_Value, avm_eda_PcbLayoutConstraint, ContainerFeature, avm_eda_EDAModel, SchematicModel, eda_Parameter, avm_eda_Parameter, avm_eda_ExactLayoutConstraint, PcbLayoutConstraint, eda_avm_ComponentInstance, eda_avm_Container, avm_eda_RangeLayoutConstraint, avm_eda_RelativeLayoutConstraint, spice_Parameter, avm_spice_Parameter, avm_eda_RelativeRangeLayoutConstraint, avm_eda_GlobalLayoutConstraintException, avm_eda_CircuitLayout, avm_spice_SPICEModel, spice_avm_Value, avm_systemc_SystemCModel, SystemCPort, avm_systemc_Parameter, systemc_avm_Value, avm_systemc_SystemCPort, avm_rf_RFModel, RFPort, FileReference, avm_rf_RFPort, avm_domainmapping_CAD2EDATransform, DomainMapping, eda_EDAModel, CADModel, avm_adamsCar_AdamsCarModel, avm_adamsCar_Parameter, adamsCar_avm_Value, avm_adamsCar_FileReference, CalculationTypeEnum, DataTypeEnum, DimensionTypeEnum, SimpleFormulaOperation, DoDDistributionStatementEnum, IntervalMethod, BoundTypeEnum, RedeclareTypeEnum, JobManagerToolSelection, GeometryQualifierEnum, CustomGeometryInputOperationEnum, PartIntersectionEnum, FileFormat, ModelType, LayerEnum, LayerRangeEnum, RelativeLayerEnum, RangeConstraintTypeEnum, GlobalConstraintTypeEnum, RelativeRotationEnum, SystemCDataTypeEnum, DirectionalityEnum, FunctionEnum, RotationEnum, PortDirectionality},
    associations={DomainModel0, Property1, ResourceDependency3, Connector5, DistributionRestriction7, Port9, AnalysisConstruct11, Formula13, DomainMapping15, UsesResource17, DefaultJoin30, Connector33, ValueExpression20, DataSource21, ValueSource23, Role24, Property27, ConnectorFeature35, Default37, Maximum39, Minimum42, AssignedValue45, Mean48, StandardDeviation50, RootContainer69, Value53, Value55, CompoundProperty58, PrimitiveProperty59, AssignedValue62, Enum63, FromResource66, ContainerFeature95, DomainFeature70, ResourceDependency72, Container76, Property78, ComponentInstance81, Port83, Connector86, JoinData89, Formula92, PortInstance107, ResourceDependency97, DomainModel100, Resource103, ValueFlowMux106, PrimitivePropertyInstance109, ConnectorInstance111, Value113, PortMap117, ConnectorComposition119, ApplyJoinData120, Operand123, Operand125, ValueSource126, TopLevelSystemUnderTest129, Parameter130, Metric132, TestInjectionPoint134, TestComponent136, Workflow139, Settings141, TestStructure143, Value146, Task148, Value167, Source150, Parameter153, Connector154, Metric156, Limit158, Redeclare160, Parameter162, Redeclare164, TargetValue168, Value170, Datum172, Parameter173, ModelMetric176, DatumMetric179, Value181, SurfaceReverseMap182, Metric183, CircleCenter185, CircleEdge186, PolygonPoint189, ExtrusionHeight191, ExtrusionSurface193, DirectionReferencePoint195, SphereCenter198, SphereEdge200, CustomGeometryInput203, InputGeometry204, ReferredPoint205, MinimumTranslation233, DefaultTranslation236, ReferencePlane206, ReferredPlane207, Datum209, AssemblyRootComponentInstance211, AlignmentPlane212, AlignmentAxis214, RotationLimitReference216, MinimumRotation219, DefaultRotation222, MaximumRotation225, AlignmentPlane228, AlignmentAxis230, MaximumTranslation239, TranslationLimitReference242, Parameter245, Metric247, Value250, Connector251, Parameter253, Pin256, Value258, Parameter257, ConstraintTarget259, ContainerConstraintTarget260, ConstraintTarget262, ContainerConstraintTarget264, ConstraintTarget267, Origin269, ContainerConstraintTarget272, Parameter288, ContainerConstraintTarget275, Origin277, ConstraintTarget280, ConstraintTarget283, ContainerConstraintTarget285, Value289, SystemCPort290, Parameter291, Value294, RFPort295, FileReference301, EDAModel296, CADModel297, Parameter299, Value303, ParameterSwap304, FileReferenceSwap306},
    generalizations={gen_avm_Value_ValueNode, gen_avm_FixedValue_ValueExpressionType, gen_avm_CalculatedValue_ValueExpressionType, gen_avm_DerivedValue_ValueExpressionType, gen_avm_Connector_ConnectorCompositionTarget, gen_avm_Port_PortMapTarget, gen_avm_DomainModelPort_Port, gen_avm_ParametricValue_ValueExpressionType, gen_avm_ProbabilisticValue_ValueExpressionType, gen_avm_NormalDistribution_ProbabilisticValue, gen_avm_SecurityClassification_DistributionRestriction, gen_avm_Proprietary_DistributionRestriction, gen_avm_ITAR_DistributionRestriction, gen_avm_UniformDistribution_ProbabilisticValue, gen_avm_PrimitiveProperty_Property, gen_avm_CompoundProperty_Property, gen_avm_ParametricEnumeratedValue_ValueExpressionType, gen_avm_AbstractPort_Port, gen_avm_Compound_Container, gen_avm_Optional_DesignSpaceContainer, gen_avm_Alternative_DesignSpaceContainer, gen_avm_ComponentPortInstance_PortMapTarget, gen_avm_DesignSpaceContainer_Container, gen_avm_ComponentConnectorInstance_ConnectorCompositionTarget, gen_avm_Formula_ValueNode, gen_avm_SimpleFormula_Formula, gen_avm_ComplexFormula_Formula, gen_avm_DoDDistributionStatement_DistributionRestriction, gen_avm_Metric_TestBenchValueBase, gen_avm_TopLevelSystemUnderTest_ContainerInstanceBase, gen_avm_Parameter_TestBenchValueBase, gen_avm_TestInjectionPoint_ContainerInstanceBase, gen_avm_InterpreterTask_WorkflowTaskBase, gen_avm_ExecutionTask_WorkflowTaskBase, gen_avm_ValueFlowMux_ValueNode, gen_avm_modelica_ModelicaModel_DomainModel, gen_avm_modelica_Connector_DomainModelPort, gen_avm_modelica_Parameter_DomainModelParameter, gen_avm_modelica_Metric_DomainModelMetric, gen_avm_modelica_Redeclare_DomainModelParameter, gen_avm_modelica_SolverSettings_Settings, gen_avm_cad_Geometry_AnalysisConstruct, gen_avm_cad_CADModel_DomainModel, gen_avm_cad_Datum_DomainModelPort, gen_avm_cad_Parameter_DomainModelParameter, gen_avm_cad_Point_Datum, gen_avm_cad_Axis_Datum, gen_avm_cad_Plane_Datum, gen_avm_cad_CoordinateSystem_Datum, gen_avm_cad_Metric_DomainModelMetric, gen_avm_cad_Geometry2D_Geometry, gen_avm_cad_Geometry3D_Geometry, gen_avm_cad_Circle_Geometry2D, gen_avm_cad_Polygon_Geometry2D, gen_avm_cad_ExtrudedGeometry_Geometry3D, gen_avm_cad_Sphere_Geometry3D, gen_avm_cad_CustomGeometry_Geometry, gen_avm_cad_Surface_Geometry3D, gen_avm_cad_GuideDatum_ConnectorFeature, gen_avm_cad_AssemblyRoot_DesignDomainFeature, gen_avm_cad_KinematicJointSpec_ConnectorFeature, gen_avm_cad_RevoluteJointSpec_KinematicJointSpec, gen_avm_cad_TranslationalJointSpec_KinematicJointSpec, gen_avm_manufacturing_ManufacturingModel_DomainModel, gen_avm_manufacturing_Parameter_DomainModelParameter, gen_avm_manufacturing_Metric_DomainModelMetric, gen_avm_cyber_CyberModel_DomainModel, gen_avm_schematic_SchematicModel_DomainModel, gen_avm_schematic_Pin_DomainModelPort, gen_avm_eda_PcbLayoutConstraint_ContainerFeature, gen_avm_eda_EDAModel_SchematicModel, gen_avm_eda_Parameter_DomainModelParameter, gen_avm_eda_ExactLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_RangeLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_RelativeLayoutConstraint_PcbLayoutConstraint, gen_avm_spice_Parameter_DomainModelParameter, gen_avm_eda_RelativeRangeLayoutConstraint_PcbLayoutConstraint, gen_avm_eda_GlobalLayoutConstraintException_PcbLayoutConstraint, gen_avm_eda_CircuitLayout_DomainModel, gen_avm_spice_SPICEModel_SchematicModel, gen_avm_systemc_SystemCModel_DomainModel, gen_avm_systemc_Parameter_DomainModelParameter, gen_avm_systemc_SystemCPort_DomainModelPort, gen_avm_rf_RFModel_DomainModel, gen_avm_rf_RFPort_DomainModelPort, gen_avm_domainmapping_CAD2EDATransform_DomainMapping, gen_avm_adamsCar_AdamsCarModel_DomainModel, gen_avm_adamsCar_Parameter_DomainModelParameter},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)