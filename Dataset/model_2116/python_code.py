from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SimpleFormulaOperation(Enum):
    Addition = "Addition"
    Multiplication = "Multiplication"
    ArithmeticMean = "ArithmeticMean"
    GeometricMean = "GeometricMean"
    Maximum = "Maximum"
    Minimum = "Minimum"
class PartIntersectionEnum(Enum):
    None = "None"
    IntersectionWithAnyParts = "IntersectionWithAnyParts"
    IntersectionWithReferencedParts = "IntersectionWithReferencedParts"
class BoundTypeEnum(Enum):
    MustNotExceed = "MustNotExceed"
    MustNotMeetOrExceed = "MustNotMeetOrExceed"
    MustExceed = "MustExceed"
    MustExceedOrEqual = "MustExceedOrEqual"
class DoDDistributionStatementEnum(Enum):
    StatementA = "StatementA"
    StatementB = "StatementB"
    StatementC = "StatementC"
    StatementD = "StatementD"
    StatementE = "StatementE"
class JobManagerToolSelection(Enum):
    Dymola_latest = "Dymola_latest"
    Dymola_2014 = "Dymola_2014"
    Dymola_2013 = "Dymola_2013"
    OpenModelica_latest = "OpenModelica_latest"
    JModelica_1_12 = "JModelica_1_12"
class DataTypeEnum(Enum):
    String = "String"
    Boolean = "Boolean"
    Integer = "Integer"
    Real = "Real"
class CustomGeometryInputOperationEnum(Enum):
    Union = "Union"
    Intersection = "Intersection"
    Subtraction = "Subtraction"
class IntervalMethod(Enum):
    NumberOfIntervals = "NumberOfIntervals"
    IntervalLength = "IntervalLength"
class RedeclareTypeEnum(Enum):
    Package = "Package"
    Class = "Class"
    Model = "Model"
    Record = "Record"
    Block = "Block"
    Connector = "Connector"
    Function = "Function"
class CalculationTypeEnum(Enum):
    Declarative = "Declarative"
    Python = "Python"
class GeometryQualifierEnum(Enum):
    InteriorAndBoundary = "InteriorAndBoundary"
    InteriorOnly = "InteriorOnly"
    BoundaryOnly = "BoundaryOnly"
class DimensionTypeEnum(Enum):
    Matrix = "Matrix"
    Vector = "Vector"
    Scalar = "Scalar"
class ModelType(Enum):
    SignalFlow = "SignalFlow"
    Simulink = "Simulink"
    ESMoL = "ESMoL"


############################################
# Definition of Classes
############################################

class avm_adamsCar_FileReference:

    def __init__(self, FilePath: str, ID: str, Name: str, avm_adamsCar_FileReference: set["Parameter"] = None, avm_adamsCar_FileReference248: set["FileReference"] = None):
        self.FilePath = FilePath
        self.ID = ID
        self.Name = Name
        self.avm_adamsCar_FileReference = avm_adamsCar_FileReference if avm_adamsCar_FileReference is not None else set()
        self.avm_adamsCar_FileReference248 = avm_adamsCar_FileReference248 if avm_adamsCar_FileReference248 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def FilePath(self) -> str:
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_adamsCar_FileReference(self):
        return self.__avm_adamsCar_FileReference

    @avm_adamsCar_FileReference.setter
    def avm_adamsCar_FileReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_adamsCar_FileReference__avm_adamsCar_FileReference", None)
        self.__avm_adamsCar_FileReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter246"):
                    opp_val = getattr(item, "Parameter246", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter246"):
                    opp_val = getattr(item, "Parameter246", None)
                    
                    setattr(item, "Parameter246", self)
                    

    @property
    def avm_adamsCar_FileReference248(self):
        return self.__avm_adamsCar_FileReference248

    @avm_adamsCar_FileReference248.setter
    def avm_adamsCar_FileReference248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_adamsCar_FileReference__avm_adamsCar_FileReference248", None)
        self.__avm_adamsCar_FileReference248 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileReference249"):
                    opp_val = getattr(item, "FileReference249", None)
                    
                    if opp_val == self:
                        setattr(item, "FileReference249", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileReference249"):
                    opp_val = getattr(item, "FileReference249", None)
                    
                    setattr(item, "FileReference249", self)
                    

class adamsCar_avm_Value:

    pass
class FileReference:

    pass
class manufacturing_avm_Value:

    pass
class cad_avm_ComponentInstance:

    pass
class DesignDomainFeature:

    pass
class avm_cad_AssemblyRoot(DesignDomainFeature):

    pass
class ConnectorFeature:

    pass
class avm_cad_KinematicJointSpec(ConnectorFeature):

    pass
class avm_cad_GuideDatum(ConnectorFeature):

    pass
class avm_cad_PlaneReference:

    pass
class PlaneReference:

    pass
class Point:

    pass
class avm_cad_PointReference:

    pass
class Geometry3D:

    pass
class avm_cad_Surface(Geometry3D):

    pass
class avm_cad_ExtrudedGeometry(Geometry3D):

    pass
class Axis:

    pass
class KinematicJointSpec:

    pass
class avm_cad_TranslationalJointSpec(KinematicJointSpec):

    pass
class avm_cad_RevoluteJointSpec(KinematicJointSpec):

    pass
class avm_cad_CustomGeometryInput:

    def __init__(self, Operation: str, avm_cad_CustomGeometryInput: "Geometry" = None):
        self.Operation = Operation
        self.avm_cad_CustomGeometryInput = avm_cad_CustomGeometryInput
        
    @property
    def Operation(self) -> str:
        return self.__Operation

    @Operation.setter
    def Operation(self, Operation: str):
        self.__Operation = Operation

    @property
    def avm_cad_CustomGeometryInput(self):
        return self.__avm_cad_CustomGeometryInput

    @avm_cad_CustomGeometryInput.setter
    def avm_cad_CustomGeometryInput(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_CustomGeometryInput__avm_cad_CustomGeometryInput", None)
        self.__avm_cad_CustomGeometryInput = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Geometry"):
                opp_val = getattr(old_value, "Geometry", None)
                if opp_val == self:
                    setattr(old_value, "Geometry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Geometry"):
                opp_val = getattr(value, "Geometry", None)
                setattr(value, "Geometry", self)

class CustomGeometryInput:

    pass
class avm_cad_Sphere(Geometry3D):

    pass
class PointReference:

    pass
class Geometry2D:

    pass
class avm_cad_Polygon(Geometry2D):

    pass
class avm_cad_Circle(Geometry2D):

    pass
class Geometry:

    pass
class avm_cad_CustomGeometry(Geometry):

    pass
class avm_cad_Geometry3D(Geometry):

    pass
class avm_cad_Geometry2D(Geometry):

    pass
class AnalysisConstruct:

    pass
class avm_cad_Geometry(AnalysisConstruct):

    def __init__(self, GeometryQualifier: str, PartIntersectionModifier: str):
        self.GeometryQualifier = GeometryQualifier
        self.PartIntersectionModifier = PartIntersectionModifier
        
    @property
    def PartIntersectionModifier(self) -> str:
        return self.__PartIntersectionModifier

    @PartIntersectionModifier.setter
    def PartIntersectionModifier(self, PartIntersectionModifier: str):
        self.__PartIntersectionModifier = PartIntersectionModifier

    @property
    def GeometryQualifier(self) -> str:
        return self.__GeometryQualifier

    @GeometryQualifier.setter
    def GeometryQualifier(self, GeometryQualifier: str):
        self.__GeometryQualifier = GeometryQualifier

class Plane:

    pass
class cad_avm_Value:

    pass
class Datum:

    pass
class avm_cad_Axis(Datum):

    pass
class avm_cad_CoordinateSystem(Datum):

    pass
class avm_cad_Point(Datum):

    pass
class avm_cad_Plane(Datum):

    pass
class Settings:

    pass
class avm_modelica_SolverSettings(Settings):

    def __init__(self, Solver: str, JobManagerToolSelection: str, StartTime: str, StopTime: str, IntervalMethod: str, NumberOfIntervals: str, IntervalLength: str, ToolSpecificAnnotations: str, Tolerance: str):
        self.Solver = Solver
        self.JobManagerToolSelection = JobManagerToolSelection
        self.StartTime = StartTime
        self.StopTime = StopTime
        self.IntervalMethod = IntervalMethod
        self.NumberOfIntervals = NumberOfIntervals
        self.IntervalLength = IntervalLength
        self.ToolSpecificAnnotations = ToolSpecificAnnotations
        self.Tolerance = Tolerance
        
    @property
    def Solver(self) -> str:
        return self.__Solver

    @Solver.setter
    def Solver(self, Solver: str):
        self.__Solver = Solver

    @property
    def IntervalMethod(self) -> str:
        return self.__IntervalMethod

    @IntervalMethod.setter
    def IntervalMethod(self, IntervalMethod: str):
        self.__IntervalMethod = IntervalMethod

    @property
    def ToolSpecificAnnotations(self) -> str:
        return self.__ToolSpecificAnnotations

    @ToolSpecificAnnotations.setter
    def ToolSpecificAnnotations(self, ToolSpecificAnnotations: str):
        self.__ToolSpecificAnnotations = ToolSpecificAnnotations

    @property
    def StartTime(self) -> str:
        return self.__StartTime

    @StartTime.setter
    def StartTime(self, StartTime: str):
        self.__StartTime = StartTime

    @property
    def IntervalLength(self) -> str:
        return self.__IntervalLength

    @IntervalLength.setter
    def IntervalLength(self, IntervalLength: str):
        self.__IntervalLength = IntervalLength

    @property
    def StopTime(self) -> str:
        return self.__StopTime

    @StopTime.setter
    def StopTime(self, StopTime: str):
        self.__StopTime = StopTime

    @property
    def NumberOfIntervals(self) -> str:
        return self.__NumberOfIntervals

    @NumberOfIntervals.setter
    def NumberOfIntervals(self, NumberOfIntervals: str):
        self.__NumberOfIntervals = NumberOfIntervals

    @property
    def JobManagerToolSelection(self) -> str:
        return self.__JobManagerToolSelection

    @JobManagerToolSelection.setter
    def JobManagerToolSelection(self, JobManagerToolSelection: str):
        self.__JobManagerToolSelection = JobManagerToolSelection

    @property
    def Tolerance(self) -> str:
        return self.__Tolerance

    @Tolerance.setter
    def Tolerance(self, Tolerance: str):
        self.__Tolerance = Tolerance

class avm_modelica_Limit:

    def __init__(self, VariableLocator: str, BoundType: str, Name: str, ToleranceTimeWindow: str, Notes: str, avm_modelica_Limit: "modelica_avm_Value" = None):
        self.VariableLocator = VariableLocator
        self.BoundType = BoundType
        self.Name = Name
        self.ToleranceTimeWindow = ToleranceTimeWindow
        self.Notes = Notes
        self.avm_modelica_Limit = avm_modelica_Limit
        
    @property
    def VariableLocator(self) -> str:
        return self.__VariableLocator

    @VariableLocator.setter
    def VariableLocator(self, VariableLocator: str):
        self.__VariableLocator = VariableLocator

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def BoundType(self) -> str:
        return self.__BoundType

    @BoundType.setter
    def BoundType(self, BoundType: str):
        self.__BoundType = BoundType

    @property
    def ToleranceTimeWindow(self) -> str:
        return self.__ToleranceTimeWindow

    @ToleranceTimeWindow.setter
    def ToleranceTimeWindow(self, ToleranceTimeWindow: str):
        self.__ToleranceTimeWindow = ToleranceTimeWindow

    @property
    def avm_modelica_Limit(self):
        return self.__avm_modelica_Limit

    @avm_modelica_Limit.setter
    def avm_modelica_Limit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Limit__avm_modelica_Limit", None)
        self.__avm_modelica_Limit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelica_avm_Value153"):
                opp_val = getattr(old_value, "modelica_avm_Value153", None)
                if opp_val == self:
                    setattr(old_value, "modelica_avm_Value153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelica_avm_Value153"):
                opp_val = getattr(value, "modelica_avm_Value153", None)
                setattr(value, "modelica_avm_Value153", self)

class DomainModelMetric:

    pass
class avm_manufacturing_Metric(DomainModelMetric):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class avm_cad_Metric(DomainModelMetric):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class avm_modelica_Metric(DomainModelMetric):

    def __init__(self, Locator: str):
        self.Locator = Locator
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

class modelica_avm_Value:

    pass
class DomainModelParameter:

    pass
class avm_modelica_Redeclare(DomainModelParameter):

    def __init__(self, Type: str, Locator: str, avm_modelica_Redeclare: "modelica_avm_Value" = None):
        self.Type = Type
        self.Locator = Locator
        self.avm_modelica_Redeclare = avm_modelica_Redeclare
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def avm_modelica_Redeclare(self):
        return self.__avm_modelica_Redeclare

    @avm_modelica_Redeclare.setter
    def avm_modelica_Redeclare(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Redeclare__avm_modelica_Redeclare", None)
        self.__avm_modelica_Redeclare = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelica_avm_Value155"):
                opp_val = getattr(old_value, "modelica_avm_Value155", None)
                if opp_val == self:
                    setattr(old_value, "modelica_avm_Value155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelica_avm_Value155"):
                opp_val = getattr(value, "modelica_avm_Value155", None)
                setattr(value, "modelica_avm_Value155", self)

class avm_cad_Parameter(DomainModelParameter):

    def __init__(self, Name: str, avm_cad_Parameter: "cad_avm_Value" = None):
        self.Name = Name
        self.avm_cad_Parameter = avm_cad_Parameter
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_cad_Parameter(self):
        return self.__avm_cad_Parameter

    @avm_cad_Parameter.setter
    def avm_cad_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_Parameter__avm_cad_Parameter", None)
        self.__avm_cad_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cad_avm_Value"):
                opp_val = getattr(old_value, "cad_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "cad_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cad_avm_Value"):
                opp_val = getattr(value, "cad_avm_Value", None)
                setattr(value, "cad_avm_Value", self)

class avm_adamsCar_Parameter(DomainModelParameter):

    def __init__(self, ID: str, Name: str, avm_adamsCar_Parameter: "adamsCar_avm_Value" = None):
        self.ID = ID
        self.Name = Name
        self.avm_adamsCar_Parameter = avm_adamsCar_Parameter
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_adamsCar_Parameter(self):
        return self.__avm_adamsCar_Parameter

    @avm_adamsCar_Parameter.setter
    def avm_adamsCar_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_adamsCar_Parameter__avm_adamsCar_Parameter", None)
        self.__avm_adamsCar_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "adamsCar_avm_Value"):
                opp_val = getattr(old_value, "adamsCar_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "adamsCar_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "adamsCar_avm_Value"):
                opp_val = getattr(value, "adamsCar_avm_Value", None)
                setattr(value, "adamsCar_avm_Value", self)

class avm_manufacturing_Parameter(DomainModelParameter):

    def __init__(self, Name: str, Locator: str, avm_manufacturing_Parameter: "manufacturing_avm_Value" = None):
        self.Name = Name
        self.Locator = Locator
        self.avm_manufacturing_Parameter = avm_manufacturing_Parameter
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_manufacturing_Parameter(self):
        return self.__avm_manufacturing_Parameter

    @avm_manufacturing_Parameter.setter
    def avm_manufacturing_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_manufacturing_Parameter__avm_manufacturing_Parameter", None)
        self.__avm_manufacturing_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manufacturing_avm_Value"):
                opp_val = getattr(old_value, "manufacturing_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "manufacturing_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manufacturing_avm_Value"):
                opp_val = getattr(value, "manufacturing_avm_Value", None)
                setattr(value, "manufacturing_avm_Value", self)

class avm_modelica_Parameter(DomainModelParameter):

    def __init__(self, Locator: str, avm_modelica_Parameter: "modelica_avm_Value" = None):
        self.Locator = Locator
        self.avm_modelica_Parameter = avm_modelica_Parameter
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def avm_modelica_Parameter(self):
        return self.__avm_modelica_Parameter

    @avm_modelica_Parameter.setter
    def avm_modelica_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Parameter__avm_modelica_Parameter", None)
        self.__avm_modelica_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelica_avm_Value"):
                opp_val = getattr(old_value, "modelica_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "modelica_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelica_avm_Value"):
                opp_val = getattr(value, "modelica_avm_Value", None)
                setattr(value, "modelica_avm_Value", self)

class DomainModelPort:

    pass
class avm_cad_Datum(DomainModelPort):

    def __init__(self, DatumName: str, avm_cad_Datum: set["Metric"] = None):
        self.DatumName = DatumName
        self.avm_cad_Datum = avm_cad_Datum if avm_cad_Datum is not None else set()
        
    @property
    def DatumName(self) -> str:
        return self.__DatumName

    @DatumName.setter
    def DatumName(self, DatumName: str):
        self.__DatumName = DatumName

    @property
    def avm_cad_Datum(self):
        return self.__avm_cad_Datum

    @avm_cad_Datum.setter
    def avm_cad_Datum(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_Datum__avm_cad_Datum", None)
        self.__avm_cad_Datum = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metric164"):
                    opp_val = getattr(item, "Metric164", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric164"):
                    opp_val = getattr(item, "Metric164", None)
                    
                    setattr(item, "Metric164", self)
                    

class avm_modelica_Connector(DomainModelPort):

    def __init__(self, Class: str, Locator: str, avm_modelica_Connector: set["Parameter"] = None, avm_modelica_Connector149: set["Redeclare"] = None):
        self.Class = Class
        self.Locator = Locator
        self.avm_modelica_Connector = avm_modelica_Connector if avm_modelica_Connector is not None else set()
        self.avm_modelica_Connector149 = avm_modelica_Connector149 if avm_modelica_Connector149 is not None else set()
        
    @property
    def Class(self) -> str:
        return self.__Class

    @Class.setter
    def Class(self, Class: str):
        self.__Class = Class

    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def avm_modelica_Connector(self):
        return self.__avm_modelica_Connector

    @avm_modelica_Connector.setter
    def avm_modelica_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Connector__avm_modelica_Connector", None)
        self.__avm_modelica_Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter147"):
                    opp_val = getattr(item, "Parameter147", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter147"):
                    opp_val = getattr(item, "Parameter147", None)
                    
                    setattr(item, "Parameter147", self)
                    

    @property
    def avm_modelica_Connector149(self):
        return self.__avm_modelica_Connector149

    @avm_modelica_Connector149.setter
    def avm_modelica_Connector149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Connector__avm_modelica_Connector149", None)
        self.__avm_modelica_Connector149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Redeclare150"):
                    opp_val = getattr(item, "Redeclare150", None)
                    
                    if opp_val == self:
                        setattr(item, "Redeclare150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Redeclare150"):
                    opp_val = getattr(item, "Redeclare150", None)
                    
                    setattr(item, "Redeclare150", self)
                    

class Redeclare:

    pass
class Limit:

    pass
class WorkflowTaskBase:

    pass
class avm_ExecutionTask(WorkflowTaskBase):

    def __init__(self, Description: str, Invocation: str):
        self.Description = Description
        self.Invocation = Invocation
        
    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Invocation(self) -> str:
        return self.__Invocation

    @Invocation.setter
    def Invocation(self, Invocation: str):
        self.__Invocation = Invocation

class avm_InterpreterTask(WorkflowTaskBase):

    def __init__(self, COMName: str, Parameters: str):
        self.COMName = COMName
        self.Parameters = Parameters
        
    @property
    def COMName(self) -> str:
        return self.__COMName

    @COMName.setter
    def COMName(self, COMName: str):
        self.__COMName = COMName

    @property
    def Parameters(self) -> str:
        return self.__Parameters

    @Parameters.setter
    def Parameters(self, Parameters: str):
        self.__Parameters = Parameters

class Metric:

    pass
class Connector:

    pass
class Parameter:

    pass
class DomainModel:

    pass
class avm_manufacturing_ManufacturingModel(DomainModel):

    pass
class avm_cad_CADModel(DomainModel):

    pass
class avm_adamsCar_AdamsCarModel(DomainModel):

    pass
class avm_cyber_CyberModel(DomainModel):

    def __init__(self, Type: str, Class: str, Locator: str, avm_cyber_CyberModel: set["Connector"] = None, avm_cyber_CyberModel238: set["Parameter"] = None):
        self.Type = Type
        self.Class = Class
        self.Locator = Locator
        self.avm_cyber_CyberModel = avm_cyber_CyberModel if avm_cyber_CyberModel is not None else set()
        self.avm_cyber_CyberModel238 = avm_cyber_CyberModel238 if avm_cyber_CyberModel238 is not None else set()
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def Class(self) -> str:
        return self.__Class

    @Class.setter
    def Class(self, Class: str):
        self.__Class = Class

    @property
    def avm_cyber_CyberModel238(self):
        return self.__avm_cyber_CyberModel238

    @avm_cyber_CyberModel238.setter
    def avm_cyber_CyberModel238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cyber_CyberModel__avm_cyber_CyberModel238", None)
        self.__avm_cyber_CyberModel238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter239"):
                    opp_val = getattr(item, "Parameter239", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter239"):
                    opp_val = getattr(item, "Parameter239", None)
                    
                    setattr(item, "Parameter239", self)
                    

    @property
    def avm_cyber_CyberModel(self):
        return self.__avm_cyber_CyberModel

    @avm_cyber_CyberModel.setter
    def avm_cyber_CyberModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cyber_CyberModel__avm_cyber_CyberModel", None)
        self.__avm_cyber_CyberModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector236"):
                    opp_val = getattr(item, "Connector236", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector236", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector236"):
                    opp_val = getattr(item, "Connector236", None)
                    
                    setattr(item, "Connector236", self)
                    

class avm_modelica_ModelicaModel(DomainModel):

    def __init__(self, Class: str, avm_modelica_ModelicaModel: set["Parameter"] = None, avm_modelica_ModelicaModel139: set["Connector"] = None, avm_modelica_ModelicaModel141: set["Metric"] = None, avm_modelica_ModelicaModel143: set["Limit"] = None, avm_modelica_ModelicaModel145: set["Redeclare"] = None):
        self.Class = Class
        self.avm_modelica_ModelicaModel = avm_modelica_ModelicaModel if avm_modelica_ModelicaModel is not None else set()
        self.avm_modelica_ModelicaModel139 = avm_modelica_ModelicaModel139 if avm_modelica_ModelicaModel139 is not None else set()
        self.avm_modelica_ModelicaModel141 = avm_modelica_ModelicaModel141 if avm_modelica_ModelicaModel141 is not None else set()
        self.avm_modelica_ModelicaModel143 = avm_modelica_ModelicaModel143 if avm_modelica_ModelicaModel143 is not None else set()
        self.avm_modelica_ModelicaModel145 = avm_modelica_ModelicaModel145 if avm_modelica_ModelicaModel145 is not None else set()
        
    @property
    def Class(self) -> str:
        return self.__Class

    @Class.setter
    def Class(self, Class: str):
        self.__Class = Class

    @property
    def avm_modelica_ModelicaModel(self):
        return self.__avm_modelica_ModelicaModel

    @avm_modelica_ModelicaModel.setter
    def avm_modelica_ModelicaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel", None)
        self.__avm_modelica_ModelicaModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    @property
    def avm_modelica_ModelicaModel141(self):
        return self.__avm_modelica_ModelicaModel141

    @avm_modelica_ModelicaModel141.setter
    def avm_modelica_ModelicaModel141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel141", None)
        self.__avm_modelica_ModelicaModel141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric"):
                    opp_val = getattr(item, "Metric", None)
                    
                    setattr(item, "Metric", self)
                    

    @property
    def avm_modelica_ModelicaModel139(self):
        return self.__avm_modelica_ModelicaModel139

    @avm_modelica_ModelicaModel139.setter
    def avm_modelica_ModelicaModel139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel139", None)
        self.__avm_modelica_ModelicaModel139 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    setattr(item, "Connector", self)
                    

    @property
    def avm_modelica_ModelicaModel145(self):
        return self.__avm_modelica_ModelicaModel145

    @avm_modelica_ModelicaModel145.setter
    def avm_modelica_ModelicaModel145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel145", None)
        self.__avm_modelica_ModelicaModel145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Redeclare"):
                    opp_val = getattr(item, "Redeclare", None)
                    
                    if opp_val == self:
                        setattr(item, "Redeclare", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Redeclare"):
                    opp_val = getattr(item, "Redeclare", None)
                    
                    setattr(item, "Redeclare", self)
                    

    @property
    def avm_modelica_ModelicaModel143(self):
        return self.__avm_modelica_ModelicaModel143

    @avm_modelica_ModelicaModel143.setter
    def avm_modelica_ModelicaModel143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel143", None)
        self.__avm_modelica_ModelicaModel143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Limit"):
                    opp_val = getattr(item, "Limit", None)
                    
                    if opp_val == self:
                        setattr(item, "Limit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Limit"):
                    opp_val = getattr(item, "Limit", None)
                    
                    setattr(item, "Limit", self)
                    

class avm_Workflow:

    def __init__(self, Name: str, avm_Workflow133: set["avm_WorkflowTaskBase"] = None, avm_Workflow: "avm_TestBench" = None):
        self.Name = Name
        self.avm_Workflow133 = avm_Workflow133 if avm_Workflow133 is not None else set()
        self.avm_Workflow = avm_Workflow
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Workflow(self):
        return self.__avm_Workflow

    @avm_Workflow.setter
    def avm_Workflow(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Workflow__avm_Workflow", None)
        self.__avm_Workflow = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench124"):
                opp_val = getattr(old_value, "avm_TestBench124", None)
                if opp_val == self:
                    setattr(old_value, "avm_TestBench124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench124"):
                opp_val = getattr(value, "avm_TestBench124", None)
                setattr(value, "avm_TestBench124", self)

    @property
    def avm_Workflow133(self):
        return self.__avm_Workflow133

    @avm_Workflow133.setter
    def avm_Workflow133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Workflow__avm_Workflow133", None)
        self.__avm_Workflow133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_WorkflowTaskBase"):
                    opp_val = getattr(item, "avm_WorkflowTaskBase", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_WorkflowTaskBase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_WorkflowTaskBase"):
                    opp_val = getattr(item, "avm_WorkflowTaskBase", None)
                    
                    setattr(item, "avm_WorkflowTaskBase", self)
                    

class avm_WorkflowTaskBase(ABC):

    def __init__(self, Name: str, avm_WorkflowTaskBase: "avm_Workflow" = None):
        self.Name = Name
        self.avm_WorkflowTaskBase = avm_WorkflowTaskBase
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_WorkflowTaskBase(self):
        return self.__avm_WorkflowTaskBase

    @avm_WorkflowTaskBase.setter
    def avm_WorkflowTaskBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_WorkflowTaskBase__avm_WorkflowTaskBase", None)
        self.__avm_WorkflowTaskBase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Workflow133"):
                opp_val = getattr(old_value, "avm_Workflow133", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Workflow133"):
                opp_val = getattr(value, "avm_Workflow133", None)
                if opp_val is None:
                    setattr(value, "avm_Workflow133", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_TestBenchValueBase(ABC):

    def __init__(self, ID: str, Name: str, Notes: str, XPosition: str, YPosition: str, avm_TestBenchValueBase: "avm_Value" = None):
        self.ID = ID
        self.Name = Name
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_TestBenchValueBase = avm_TestBenchValueBase
        
    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_TestBenchValueBase(self):
        return self.__avm_TestBenchValueBase

    @avm_TestBenchValueBase.setter
    def avm_TestBenchValueBase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBenchValueBase__avm_TestBenchValueBase", None)
        self.__avm_TestBenchValueBase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Value131"):
                opp_val = getattr(old_value, "avm_Value131", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value131"):
                opp_val = getattr(value, "avm_Value131", None)
                setattr(value, "avm_Value131", self)

class avm_ContainerInstanceBase(ABC):

    def __init__(self, IDinSourceModel: str, XPosition: str, YPosition: str):
        self.IDinSourceModel = IDinSourceModel
        self.XPosition = XPosition
        self.YPosition = YPosition
        
    @property
    def IDinSourceModel(self) -> str:
        return self.__IDinSourceModel

    @IDinSourceModel.setter
    def IDinSourceModel(self, IDinSourceModel: str):
        self.__IDinSourceModel = IDinSourceModel

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

class TestBenchValueBase:

    pass
class avm_Metric(TestBenchValueBase):

    pass
class avm_Parameter(TestBenchValueBase):

    pass
class ContainerInstanceBase:

    pass
class avm_TestInjectionPoint(ContainerInstanceBase):

    pass
class avm_Settings(ABC):

    pass
class avm_ConnectorCompositionTarget:

    def __init__(self, ID: str, avm_ConnectorCompositionTarget: "avm_ConnectorCompositionTarget" = None, avm_ConnectorCompositionTarget102: set["avm_ConnectorCompositionTarget"] = None, avm_ConnectorCompositionTarget105: set["avm_assemblyDetail"] = None):
        self.ID = ID
        self.avm_ConnectorCompositionTarget = avm_ConnectorCompositionTarget
        self.avm_ConnectorCompositionTarget102 = avm_ConnectorCompositionTarget102 if avm_ConnectorCompositionTarget102 is not None else set()
        self.avm_ConnectorCompositionTarget105 = avm_ConnectorCompositionTarget105 if avm_ConnectorCompositionTarget105 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_ConnectorCompositionTarget105(self):
        return self.__avm_ConnectorCompositionTarget105

    @avm_ConnectorCompositionTarget105.setter
    def avm_ConnectorCompositionTarget105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget105", None)
        self.__avm_ConnectorCompositionTarget105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_assemblyDetail106"):
                    opp_val = getattr(item, "avm_assemblyDetail106", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_assemblyDetail106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_assemblyDetail106"):
                    opp_val = getattr(item, "avm_assemblyDetail106", None)
                    
                    setattr(item, "avm_assemblyDetail106", self)
                    

    @property
    def avm_ConnectorCompositionTarget(self):
        return self.__avm_ConnectorCompositionTarget

    @avm_ConnectorCompositionTarget.setter
    def avm_ConnectorCompositionTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget", None)
        self.__avm_ConnectorCompositionTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ConnectorCompositionTarget102"):
                opp_val = getattr(old_value, "avm_ConnectorCompositionTarget102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ConnectorCompositionTarget102"):
                opp_val = getattr(value, "avm_ConnectorCompositionTarget102", None)
                if opp_val is None:
                    setattr(value, "avm_ConnectorCompositionTarget102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ConnectorCompositionTarget102(self):
        return self.__avm_ConnectorCompositionTarget102

    @avm_ConnectorCompositionTarget102.setter
    def avm_ConnectorCompositionTarget102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget102", None)
        self.__avm_ConnectorCompositionTarget102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ConnectorCompositionTarget"):
                    opp_val = getattr(item, "avm_ConnectorCompositionTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ConnectorCompositionTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ConnectorCompositionTarget"):
                    opp_val = getattr(item, "avm_ConnectorCompositionTarget", None)
                    
                    setattr(item, "avm_ConnectorCompositionTarget", self)
                    

class avm_TopLevelSystemUnderTest(ContainerInstanceBase):

    def __init__(self, DesignID: str, avm_TopLevelSystemUnderTest: "avm_TestBench" = None):
        self.DesignID = DesignID
        self.avm_TopLevelSystemUnderTest = avm_TopLevelSystemUnderTest
        
    @property
    def DesignID(self) -> str:
        return self.__DesignID

    @DesignID.setter
    def DesignID(self, DesignID: str):
        self.__DesignID = DesignID

    @property
    def avm_TopLevelSystemUnderTest(self):
        return self.__avm_TopLevelSystemUnderTest

    @avm_TopLevelSystemUnderTest.setter
    def avm_TopLevelSystemUnderTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TopLevelSystemUnderTest__avm_TopLevelSystemUnderTest", None)
        self.__avm_TopLevelSystemUnderTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench"):
                opp_val = getattr(old_value, "avm_TestBench", None)
                if opp_val == self:
                    setattr(old_value, "avm_TestBench", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench"):
                opp_val = getattr(value, "avm_TestBench", None)
                setattr(value, "avm_TestBench", self)

class avm_TestBench:

    def __init__(self, Name: str, avm_TestBench: "avm_TopLevelSystemUnderTest" = None, avm_TestBench124: "avm_Workflow" = None, avm_TestBench126: set["avm_Settings"] = None, avm_TestBench128: set["avm_DomainModel"] = None, avm_TestBench115: set["avm_Parameter"] = None, avm_TestBench117: set["avm_Metric"] = None, avm_TestBench119: set["avm_TestInjectionPoint"] = None, avm_TestBench121: set["avm_ComponentInstance"] = None):
        self.Name = Name
        self.avm_TestBench = avm_TestBench
        self.avm_TestBench124 = avm_TestBench124
        self.avm_TestBench126 = avm_TestBench126 if avm_TestBench126 is not None else set()
        self.avm_TestBench128 = avm_TestBench128 if avm_TestBench128 is not None else set()
        self.avm_TestBench115 = avm_TestBench115 if avm_TestBench115 is not None else set()
        self.avm_TestBench117 = avm_TestBench117 if avm_TestBench117 is not None else set()
        self.avm_TestBench119 = avm_TestBench119 if avm_TestBench119 is not None else set()
        self.avm_TestBench121 = avm_TestBench121 if avm_TestBench121 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_TestBench119(self):
        return self.__avm_TestBench119

    @avm_TestBench119.setter
    def avm_TestBench119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench119", None)
        self.__avm_TestBench119 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_TestInjectionPoint"):
                    opp_val = getattr(item, "avm_TestInjectionPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_TestInjectionPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_TestInjectionPoint"):
                    opp_val = getattr(item, "avm_TestInjectionPoint", None)
                    
                    setattr(item, "avm_TestInjectionPoint", self)
                    

    @property
    def avm_TestBench128(self):
        return self.__avm_TestBench128

    @avm_TestBench128.setter
    def avm_TestBench128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench128", None)
        self.__avm_TestBench128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DomainModel129"):
                    opp_val = getattr(item, "avm_DomainModel129", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DomainModel129", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DomainModel129"):
                    opp_val = getattr(item, "avm_DomainModel129", None)
                    
                    setattr(item, "avm_DomainModel129", self)
                    

    @property
    def avm_TestBench126(self):
        return self.__avm_TestBench126

    @avm_TestBench126.setter
    def avm_TestBench126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench126", None)
        self.__avm_TestBench126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Settings"):
                    opp_val = getattr(item, "avm_Settings", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Settings", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Settings"):
                    opp_val = getattr(item, "avm_Settings", None)
                    
                    setattr(item, "avm_Settings", self)
                    

    @property
    def avm_TestBench115(self):
        return self.__avm_TestBench115

    @avm_TestBench115.setter
    def avm_TestBench115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench115", None)
        self.__avm_TestBench115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Parameter"):
                    opp_val = getattr(item, "avm_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Parameter"):
                    opp_val = getattr(item, "avm_Parameter", None)
                    
                    setattr(item, "avm_Parameter", self)
                    

    @property
    def avm_TestBench121(self):
        return self.__avm_TestBench121

    @avm_TestBench121.setter
    def avm_TestBench121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench121", None)
        self.__avm_TestBench121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentInstance122"):
                    opp_val = getattr(item, "avm_ComponentInstance122", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentInstance122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentInstance122"):
                    opp_val = getattr(item, "avm_ComponentInstance122", None)
                    
                    setattr(item, "avm_ComponentInstance122", self)
                    

    @property
    def avm_TestBench124(self):
        return self.__avm_TestBench124

    @avm_TestBench124.setter
    def avm_TestBench124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench124", None)
        self.__avm_TestBench124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Workflow"):
                opp_val = getattr(old_value, "avm_Workflow", None)
                if opp_val == self:
                    setattr(old_value, "avm_Workflow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Workflow"):
                opp_val = getattr(value, "avm_Workflow", None)
                setattr(value, "avm_Workflow", self)

    @property
    def avm_TestBench(self):
        return self.__avm_TestBench

    @avm_TestBench.setter
    def avm_TestBench(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench", None)
        self.__avm_TestBench = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TopLevelSystemUnderTest"):
                opp_val = getattr(old_value, "avm_TopLevelSystemUnderTest", None)
                if opp_val == self:
                    setattr(old_value, "avm_TopLevelSystemUnderTest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TopLevelSystemUnderTest"):
                opp_val = getattr(value, "avm_TopLevelSystemUnderTest", None)
                setattr(value, "avm_TopLevelSystemUnderTest", self)

    @property
    def avm_TestBench117(self):
        return self.__avm_TestBench117

    @avm_TestBench117.setter
    def avm_TestBench117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench117", None)
        self.__avm_TestBench117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Metric"):
                    opp_val = getattr(item, "avm_Metric", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Metric", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Metric"):
                    opp_val = getattr(item, "avm_Metric", None)
                    
                    setattr(item, "avm_Metric", self)
                    

class avm_Operand:

    def __init__(self, Symbol: str, avm_Operand: "avm_ComplexFormula" = None, avm_Operand111: "avm_ValueNode" = None):
        self.Symbol = Symbol
        self.avm_Operand = avm_Operand
        self.avm_Operand111 = avm_Operand111
        
    @property
    def Symbol(self) -> str:
        return self.__Symbol

    @Symbol.setter
    def Symbol(self, Symbol: str):
        self.__Symbol = Symbol

    @property
    def avm_Operand(self):
        return self.__avm_Operand

    @avm_Operand.setter
    def avm_Operand(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Operand__avm_Operand", None)
        self.__avm_Operand = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComplexFormula"):
                opp_val = getattr(old_value, "avm_ComplexFormula", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComplexFormula"):
                opp_val = getattr(value, "avm_ComplexFormula", None)
                if opp_val is None:
                    setattr(value, "avm_ComplexFormula", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Operand111(self):
        return self.__avm_Operand111

    @avm_Operand111.setter
    def avm_Operand111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Operand__avm_Operand111", None)
        self.__avm_Operand111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ValueNode112"):
                opp_val = getattr(old_value, "avm_ValueNode112", None)
                if opp_val == self:
                    setattr(old_value, "avm_ValueNode112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ValueNode112"):
                opp_val = getattr(value, "avm_ValueNode112", None)
                setattr(value, "avm_ValueNode112", self)

class Formula:

    pass
class avm_ComplexFormula(Formula):

    def __init__(self, Expression: str, avm_ComplexFormula: set["avm_Operand"] = None):
        self.Expression = Expression
        self.avm_ComplexFormula = avm_ComplexFormula if avm_ComplexFormula is not None else set()
        
    @property
    def Expression(self) -> str:
        return self.__Expression

    @Expression.setter
    def Expression(self, Expression: str):
        self.__Expression = Expression

    @property
    def avm_ComplexFormula(self):
        return self.__avm_ComplexFormula

    @avm_ComplexFormula.setter
    def avm_ComplexFormula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComplexFormula__avm_ComplexFormula", None)
        self.__avm_ComplexFormula = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Operand"):
                    opp_val = getattr(item, "avm_Operand", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Operand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Operand"):
                    opp_val = getattr(item, "avm_Operand", None)
                    
                    setattr(item, "avm_Operand", self)
                    

class avm_SimpleFormula(Formula):

    def __init__(self, Operation: str, avm_SimpleFormula: set["avm_ValueNode"] = None):
        self.Operation = Operation
        self.avm_SimpleFormula = avm_SimpleFormula if avm_SimpleFormula is not None else set()
        
    @property
    def Operation(self) -> str:
        return self.__Operation

    @Operation.setter
    def Operation(self, Operation: str):
        self.__Operation = Operation

    @property
    def avm_SimpleFormula(self):
        return self.__avm_SimpleFormula

    @avm_SimpleFormula.setter
    def avm_SimpleFormula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_SimpleFormula__avm_SimpleFormula", None)
        self.__avm_SimpleFormula = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ValueNode108"):
                    opp_val = getattr(item, "avm_ValueNode108", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ValueNode108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ValueNode108"):
                    opp_val = getattr(item, "avm_ValueNode108", None)
                    
                    setattr(item, "avm_ValueNode108", self)
                    

class DesignSpaceContainer:

    pass
class avm_Optional(DesignSpaceContainer):

    pass
class Container:

    pass
class avm_Compound(Container):

    pass
class avm_PortMapTarget:

    def __init__(self, ID: str, avm_PortMapTarget: "avm_PortMapTarget" = None, avm_PortMapTarget100: set["avm_PortMapTarget"] = None):
        self.ID = ID
        self.avm_PortMapTarget = avm_PortMapTarget
        self.avm_PortMapTarget100 = avm_PortMapTarget100 if avm_PortMapTarget100 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_PortMapTarget(self):
        return self.__avm_PortMapTarget

    @avm_PortMapTarget.setter
    def avm_PortMapTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_PortMapTarget__avm_PortMapTarget", None)
        self.__avm_PortMapTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_PortMapTarget100"):
                opp_val = getattr(old_value, "avm_PortMapTarget100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_PortMapTarget100"):
                opp_val = getattr(value, "avm_PortMapTarget100", None)
                if opp_val is None:
                    setattr(value, "avm_PortMapTarget100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_PortMapTarget100(self):
        return self.__avm_PortMapTarget100

    @avm_PortMapTarget100.setter
    def avm_PortMapTarget100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_PortMapTarget__avm_PortMapTarget100", None)
        self.__avm_PortMapTarget100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_PortMapTarget"):
                    opp_val = getattr(item, "avm_PortMapTarget", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_PortMapTarget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_PortMapTarget"):
                    opp_val = getattr(item, "avm_PortMapTarget", None)
                    
                    setattr(item, "avm_PortMapTarget", self)
                    

class avm_DesignSpaceContainer(Container):

    pass
class avm_ComponentPrimitivePropertyInstance:

    def __init__(self, IDinComponentModel: str, avm_ComponentPrimitivePropertyInstance: "avm_ComponentInstance" = None, avm_ComponentPrimitivePropertyInstance98: "avm_Value" = None):
        self.IDinComponentModel = IDinComponentModel
        self.avm_ComponentPrimitivePropertyInstance = avm_ComponentPrimitivePropertyInstance
        self.avm_ComponentPrimitivePropertyInstance98 = avm_ComponentPrimitivePropertyInstance98
        
    @property
    def IDinComponentModel(self) -> str:
        return self.__IDinComponentModel

    @IDinComponentModel.setter
    def IDinComponentModel(self, IDinComponentModel: str):
        self.__IDinComponentModel = IDinComponentModel

    @property
    def avm_ComponentPrimitivePropertyInstance(self):
        return self.__avm_ComponentPrimitivePropertyInstance

    @avm_ComponentPrimitivePropertyInstance.setter
    def avm_ComponentPrimitivePropertyInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentPrimitivePropertyInstance__avm_ComponentPrimitivePropertyInstance", None)
        self.__avm_ComponentPrimitivePropertyInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComponentInstance94"):
                opp_val = getattr(old_value, "avm_ComponentInstance94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance94"):
                opp_val = getattr(value, "avm_ComponentInstance94", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ComponentPrimitivePropertyInstance98(self):
        return self.__avm_ComponentPrimitivePropertyInstance98

    @avm_ComponentPrimitivePropertyInstance98.setter
    def avm_ComponentPrimitivePropertyInstance98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentPrimitivePropertyInstance__avm_ComponentPrimitivePropertyInstance98", None)
        self.__avm_ComponentPrimitivePropertyInstance98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Value99"):
                opp_val = getattr(old_value, "avm_Value99", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value99"):
                opp_val = getattr(value, "avm_Value99", None)
                setattr(value, "avm_Value99", self)

class avm_Alternative(DesignSpaceContainer):

    pass
class avm_ComponentInstance:

    def __init__(self, ComponentID: str, ID: str, Name: str, DesignSpaceSrcComponentID: str, XPosition: str, YPosition: str, avm_ComponentInstance: "avm_Container" = None, avm_ComponentInstance92: set["avm_ComponentPortInstance"] = None, avm_ComponentInstance94: set["avm_ComponentPrimitivePropertyInstance"] = None, avm_ComponentInstance96: set["avm_ComponentConnectorInstance"] = None, avm_ComponentInstance122: "avm_TestBench" = None):
        self.ComponentID = ComponentID
        self.ID = ID
        self.Name = Name
        self.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_ComponentInstance = avm_ComponentInstance
        self.avm_ComponentInstance92 = avm_ComponentInstance92 if avm_ComponentInstance92 is not None else set()
        self.avm_ComponentInstance94 = avm_ComponentInstance94 if avm_ComponentInstance94 is not None else set()
        self.avm_ComponentInstance96 = avm_ComponentInstance96 if avm_ComponentInstance96 is not None else set()
        self.avm_ComponentInstance122 = avm_ComponentInstance122
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def DesignSpaceSrcComponentID(self) -> str:
        return self.__DesignSpaceSrcComponentID

    @DesignSpaceSrcComponentID.setter
    def DesignSpaceSrcComponentID(self, DesignSpaceSrcComponentID: str):
        self.__DesignSpaceSrcComponentID = DesignSpaceSrcComponentID

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def ComponentID(self) -> str:
        return self.__ComponentID

    @ComponentID.setter
    def ComponentID(self, ComponentID: str):
        self.__ComponentID = ComponentID

    @property
    def avm_ComponentInstance96(self):
        return self.__avm_ComponentInstance96

    @avm_ComponentInstance96.setter
    def avm_ComponentInstance96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance96", None)
        self.__avm_ComponentInstance96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentConnectorInstance"):
                    opp_val = getattr(item, "avm_ComponentConnectorInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentConnectorInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentConnectorInstance"):
                    opp_val = getattr(item, "avm_ComponentConnectorInstance", None)
                    
                    setattr(item, "avm_ComponentConnectorInstance", self)
                    

    @property
    def avm_ComponentInstance92(self):
        return self.__avm_ComponentInstance92

    @avm_ComponentInstance92.setter
    def avm_ComponentInstance92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance92", None)
        self.__avm_ComponentInstance92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentPortInstance"):
                    opp_val = getattr(item, "avm_ComponentPortInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentPortInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentPortInstance"):
                    opp_val = getattr(item, "avm_ComponentPortInstance", None)
                    
                    setattr(item, "avm_ComponentPortInstance", self)
                    

    @property
    def avm_ComponentInstance(self):
        return self.__avm_ComponentInstance

    @avm_ComponentInstance.setter
    def avm_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance", None)
        self.__avm_ComponentInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container77"):
                opp_val = getattr(old_value, "avm_Container77", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container77"):
                opp_val = getattr(value, "avm_Container77", None)
                if opp_val is None:
                    setattr(value, "avm_Container77", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ComponentInstance122(self):
        return self.__avm_ComponentInstance122

    @avm_ComponentInstance122.setter
    def avm_ComponentInstance122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance122", None)
        self.__avm_ComponentInstance122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench121"):
                opp_val = getattr(old_value, "avm_TestBench121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench121"):
                opp_val = getattr(value, "avm_TestBench121", None)
                if opp_val is None:
                    setattr(value, "avm_TestBench121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ComponentInstance94(self):
        return self.__avm_ComponentInstance94

    @avm_ComponentInstance94.setter
    def avm_ComponentInstance94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance94", None)
        self.__avm_ComponentInstance94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentPrimitivePropertyInstance"):
                    opp_val = getattr(item, "avm_ComponentPrimitivePropertyInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentPrimitivePropertyInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentPrimitivePropertyInstance"):
                    opp_val = getattr(item, "avm_ComponentPrimitivePropertyInstance", None)
                    
                    setattr(item, "avm_ComponentPrimitivePropertyInstance", self)
                    

class avm_DesignDomainFeature(ABC):

    pass
class avm_Container(ABC):

    def __init__(self, Name: str, XPosition: str, YPosition: str, avm_Container: "avm_Design" = None, avm_Container72: "avm_Container" = None, avm_Container70: set["avm_Container"] = None, avm_Container74: set["avm_Property"] = None, avm_Container77: set["avm_ComponentInstance"] = None, avm_Container79: set["avm_Port"] = None, avm_Container82: set["avm_Connector"] = None, avm_Container85: set["avm_assemblyDetail"] = None, avm_Container88: set["avm_Formula"] = None):
        self.Name = Name
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Container = avm_Container
        self.avm_Container72 = avm_Container72
        self.avm_Container70 = avm_Container70 if avm_Container70 is not None else set()
        self.avm_Container74 = avm_Container74 if avm_Container74 is not None else set()
        self.avm_Container77 = avm_Container77 if avm_Container77 is not None else set()
        self.avm_Container79 = avm_Container79 if avm_Container79 is not None else set()
        self.avm_Container82 = avm_Container82 if avm_Container82 is not None else set()
        self.avm_Container85 = avm_Container85 if avm_Container85 is not None else set()
        self.avm_Container88 = avm_Container88 if avm_Container88 is not None else set()
        
    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Container85(self):
        return self.__avm_Container85

    @avm_Container85.setter
    def avm_Container85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container85", None)
        self.__avm_Container85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_assemblyDetail86"):
                    opp_val = getattr(item, "avm_assemblyDetail86", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_assemblyDetail86", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_assemblyDetail86"):
                    opp_val = getattr(item, "avm_assemblyDetail86", None)
                    
                    setattr(item, "avm_assemblyDetail86", self)
                    

    @property
    def avm_Container74(self):
        return self.__avm_Container74

    @avm_Container74.setter
    def avm_Container74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container74", None)
        self.__avm_Container74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Property75"):
                    opp_val = getattr(item, "avm_Property75", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Property75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Property75"):
                    opp_val = getattr(item, "avm_Property75", None)
                    
                    setattr(item, "avm_Property75", self)
                    

    @property
    def avm_Container79(self):
        return self.__avm_Container79

    @avm_Container79.setter
    def avm_Container79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container79", None)
        self.__avm_Container79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Port80"):
                    opp_val = getattr(item, "avm_Port80", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Port80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Port80"):
                    opp_val = getattr(item, "avm_Port80", None)
                    
                    setattr(item, "avm_Port80", self)
                    

    @property
    def avm_Container72(self):
        return self.__avm_Container72

    @avm_Container72.setter
    def avm_Container72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container72", None)
        self.__avm_Container72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container70"):
                opp_val = getattr(old_value, "avm_Container70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container70"):
                opp_val = getattr(value, "avm_Container70", None)
                if opp_val is None:
                    setattr(value, "avm_Container70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Container(self):
        return self.__avm_Container

    @avm_Container.setter
    def avm_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container", None)
        self.__avm_Container = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Design"):
                opp_val = getattr(old_value, "avm_Design", None)
                if opp_val == self:
                    setattr(old_value, "avm_Design", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Design"):
                opp_val = getattr(value, "avm_Design", None)
                setattr(value, "avm_Design", self)

    @property
    def avm_Container70(self):
        return self.__avm_Container70

    @avm_Container70.setter
    def avm_Container70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container70", None)
        self.__avm_Container70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Container72"):
                    opp_val = getattr(item, "avm_Container72", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Container72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Container72"):
                    opp_val = getattr(item, "avm_Container72", None)
                    
                    setattr(item, "avm_Container72", self)
                    

    @property
    def avm_Container82(self):
        return self.__avm_Container82

    @avm_Container82.setter
    def avm_Container82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container82", None)
        self.__avm_Container82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Connector83"):
                    opp_val = getattr(item, "avm_Connector83", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Connector83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Connector83"):
                    opp_val = getattr(item, "avm_Connector83", None)
                    
                    setattr(item, "avm_Connector83", self)
                    

    @property
    def avm_Container88(self):
        return self.__avm_Container88

    @avm_Container88.setter
    def avm_Container88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container88", None)
        self.__avm_Container88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Formula89"):
                    opp_val = getattr(item, "avm_Formula89", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Formula89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Formula89"):
                    opp_val = getattr(item, "avm_Formula89", None)
                    
                    setattr(item, "avm_Formula89", self)
                    

    @property
    def avm_Container77(self):
        return self.__avm_Container77

    @avm_Container77.setter
    def avm_Container77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container77", None)
        self.__avm_Container77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentInstance"):
                    opp_val = getattr(item, "avm_ComponentInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentInstance"):
                    opp_val = getattr(item, "avm_ComponentInstance", None)
                    
                    setattr(item, "avm_ComponentInstance", self)
                    

class avm_Design:

    def __init__(self, SchemaVersion: str, DesignID: str, Name: str, DesignSpaceSrcID: str, avm_Design: "avm_Container" = None, avm_Design69: set["avm_DesignDomainFeature"] = None):
        self.SchemaVersion = SchemaVersion
        self.DesignID = DesignID
        self.Name = Name
        self.DesignSpaceSrcID = DesignSpaceSrcID
        self.avm_Design = avm_Design
        self.avm_Design69 = avm_Design69 if avm_Design69 is not None else set()
        
    @property
    def SchemaVersion(self) -> str:
        return self.__SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion: str):
        self.__SchemaVersion = SchemaVersion

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DesignSpaceSrcID(self) -> str:
        return self.__DesignSpaceSrcID

    @DesignSpaceSrcID.setter
    def DesignSpaceSrcID(self, DesignSpaceSrcID: str):
        self.__DesignSpaceSrcID = DesignSpaceSrcID

    @property
    def DesignID(self) -> str:
        return self.__DesignID

    @DesignID.setter
    def DesignID(self, DesignID: str):
        self.__DesignID = DesignID

    @property
    def avm_Design69(self):
        return self.__avm_Design69

    @avm_Design69.setter
    def avm_Design69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Design__avm_Design69", None)
        self.__avm_Design69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DesignDomainFeature"):
                    opp_val = getattr(item, "avm_DesignDomainFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DesignDomainFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DesignDomainFeature"):
                    opp_val = getattr(item, "avm_DesignDomainFeature", None)
                    
                    setattr(item, "avm_DesignDomainFeature", self)
                    

    @property
    def avm_Design(self):
        return self.__avm_Design

    @avm_Design.setter
    def avm_Design(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Design__avm_Design", None)
        self.__avm_Design = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container"):
                opp_val = getattr(old_value, "avm_Container", None)
                if opp_val == self:
                    setattr(old_value, "avm_Container", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container"):
                opp_val = getattr(value, "avm_Container", None)
                setattr(value, "avm_Container", self)

class ProbabilisticValue:

    pass
class avm_NormalDistribution(ProbabilisticValue):

    pass
class Property:

    pass
class avm_CompoundProperty(Property):

    pass
class avm_PrimitiveProperty(Property):

    pass
class avm_UniformDistribution(ProbabilisticValue):

    pass
class avm_DomainModelMetric(ABC):

    def __init__(self, ID: str, Notes: str, XPosition: str, YPosition: str, avm_DomainModelMetric: "avm_Value" = None):
        self.ID = ID
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_DomainModelMetric = avm_DomainModelMetric
        
    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def avm_DomainModelMetric(self):
        return self.__avm_DomainModelMetric

    @avm_DomainModelMetric.setter
    def avm_DomainModelMetric(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModelMetric__avm_DomainModelMetric", None)
        self.__avm_DomainModelMetric = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Value52"):
                opp_val = getattr(old_value, "avm_Value52", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value52"):
                opp_val = getattr(value, "avm_Value52", None)
                setattr(value, "avm_Value52", self)

class DistributionRestriction:

    pass
class avm_ITAR(DistributionRestriction):

    pass
class avm_DoDDistributionStatement(DistributionRestriction):

    def __init__(self, Type: str):
        self.Type = Type
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

class avm_Proprietary(DistributionRestriction):

    def __init__(self, Organization: str):
        self.Organization = Organization
        
    @property
    def Organization(self) -> str:
        return self.__Organization

    @Organization.setter
    def Organization(self, Organization: str):
        self.__Organization = Organization

class avm_SecurityClassification(DistributionRestriction):

    def __init__(self, Level: str):
        self.Level = Level
        
    @property
    def Level(self) -> str:
        return self.__Level

    @Level.setter
    def Level(self, Level: str):
        self.__Level = Level

class avm_ValueNode(ABC):

    def __init__(self, ID: str, avm_ValueNode: "avm_DerivedValue" = None, avm_ValueNode108: "avm_SimpleFormula" = None, avm_ValueNode112: "avm_Operand" = None, avm_ValueNode136: "avm_ValueFlowMux" = None):
        self.ID = ID
        self.avm_ValueNode = avm_ValueNode
        self.avm_ValueNode108 = avm_ValueNode108
        self.avm_ValueNode112 = avm_ValueNode112
        self.avm_ValueNode136 = avm_ValueNode136
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_ValueNode112(self):
        return self.__avm_ValueNode112

    @avm_ValueNode112.setter
    def avm_ValueNode112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode112", None)
        self.__avm_ValueNode112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Operand111"):
                opp_val = getattr(old_value, "avm_Operand111", None)
                if opp_val == self:
                    setattr(old_value, "avm_Operand111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Operand111"):
                opp_val = getattr(value, "avm_Operand111", None)
                setattr(value, "avm_Operand111", self)

    @property
    def avm_ValueNode(self):
        return self.__avm_ValueNode

    @avm_ValueNode.setter
    def avm_ValueNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode", None)
        self.__avm_ValueNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DerivedValue"):
                opp_val = getattr(old_value, "avm_DerivedValue", None)
                if opp_val == self:
                    setattr(old_value, "avm_DerivedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DerivedValue"):
                opp_val = getattr(value, "avm_DerivedValue", None)
                setattr(value, "avm_DerivedValue", self)

    @property
    def avm_ValueNode108(self):
        return self.__avm_ValueNode108

    @avm_ValueNode108.setter
    def avm_ValueNode108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode108", None)
        self.__avm_ValueNode108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_SimpleFormula"):
                opp_val = getattr(old_value, "avm_SimpleFormula", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_SimpleFormula"):
                opp_val = getattr(value, "avm_SimpleFormula", None)
                if opp_val is None:
                    setattr(value, "avm_SimpleFormula", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ValueNode136(self):
        return self.__avm_ValueNode136

    @avm_ValueNode136.setter
    def avm_ValueNode136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode136", None)
        self.__avm_ValueNode136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ValueFlowMux135"):
                opp_val = getattr(old_value, "avm_ValueFlowMux135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ValueFlowMux135"):
                opp_val = getattr(value, "avm_ValueFlowMux135", None)
                if opp_val is None:
                    setattr(value, "avm_ValueFlowMux135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_DomainModelParameter(ABC):

    def __init__(self, Notes: str, XPosition: str, YPosition: str):
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        
    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

class Port:

    pass
class avm_AbstractPort(Port):

    pass
class avm_DomainModelPort(Port):

    pass
class PortMapTarget:

    pass
class avm_ComponentPortInstance(PortMapTarget):

    def __init__(self, IDinComponentModel: str, avm_ComponentPortInstance: "avm_ComponentInstance" = None):
        self.IDinComponentModel = IDinComponentModel
        self.avm_ComponentPortInstance = avm_ComponentPortInstance
        
    @property
    def IDinComponentModel(self) -> str:
        return self.__IDinComponentModel

    @IDinComponentModel.setter
    def IDinComponentModel(self, IDinComponentModel: str):
        self.__IDinComponentModel = IDinComponentModel

    @property
    def avm_ComponentPortInstance(self):
        return self.__avm_ComponentPortInstance

    @avm_ComponentPortInstance.setter
    def avm_ComponentPortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentPortInstance__avm_ComponentPortInstance", None)
        self.__avm_ComponentPortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComponentInstance92"):
                opp_val = getattr(old_value, "avm_ComponentInstance92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance92"):
                opp_val = getattr(value, "avm_ComponentInstance92", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_ConnectorFeature(ABC):

    pass
class avm_assemblyDetail:

    pass
class ConnectorCompositionTarget:

    pass
class avm_ComponentConnectorInstance(ConnectorCompositionTarget):

    def __init__(self, IDinComponentModel: str, avm_ComponentConnectorInstance: "avm_ComponentInstance" = None):
        self.IDinComponentModel = IDinComponentModel
        self.avm_ComponentConnectorInstance = avm_ComponentConnectorInstance
        
    @property
    def IDinComponentModel(self) -> str:
        return self.__IDinComponentModel

    @IDinComponentModel.setter
    def IDinComponentModel(self, IDinComponentModel: str):
        self.__IDinComponentModel = IDinComponentModel

    @property
    def avm_ComponentConnectorInstance(self):
        return self.__avm_ComponentConnectorInstance

    @avm_ComponentConnectorInstance.setter
    def avm_ComponentConnectorInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentConnectorInstance__avm_ComponentConnectorInstance", None)
        self.__avm_ComponentConnectorInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComponentInstance96"):
                opp_val = getattr(old_value, "avm_ComponentInstance96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance96"):
                opp_val = getattr(value, "avm_ComponentInstance96", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_AnalysisConstruct(ABC):

    pass
class ValueExpressionType:

    pass
class avm_CalculatedValue(ValueExpressionType):

    def __init__(self, Expression: str, Type: str):
        self.Expression = Expression
        self.Type = Type
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Expression(self) -> str:
        return self.__Expression

    @Expression.setter
    def Expression(self, Expression: str):
        self.__Expression = Expression

class avm_ProbabilisticValue(ValueExpressionType):

    pass
class avm_ParametricValue(ValueExpressionType):

    pass
class avm_ParametricEnumeratedValue(ValueExpressionType):

    pass
class avm_DerivedValue(ValueExpressionType):

    pass
class avm_FixedValue(ValueExpressionType):

    def __init__(self, Value: str, Uncertainty: str, avm_FixedValue: "avm_ParametricEnumeratedValue" = None):
        self.Value = Value
        self.Uncertainty = Uncertainty
        self.avm_FixedValue = avm_FixedValue
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def Uncertainty(self) -> str:
        return self.__Uncertainty

    @Uncertainty.setter
    def Uncertainty(self, Uncertainty: str):
        self.__Uncertainty = Uncertainty

    @property
    def avm_FixedValue(self):
        return self.__avm_FixedValue

    @avm_FixedValue.setter
    def avm_FixedValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_FixedValue__avm_FixedValue", None)
        self.__avm_FixedValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ParametricEnumeratedValue"):
                opp_val = getattr(old_value, "avm_ParametricEnumeratedValue", None)
                if opp_val == self:
                    setattr(old_value, "avm_ParametricEnumeratedValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ParametricEnumeratedValue"):
                opp_val = getattr(value, "avm_ParametricEnumeratedValue", None)
                setattr(value, "avm_ParametricEnumeratedValue", self)

class avm_DataSource:

    def __init__(self, Notes: str, avm_DataSource: "avm_Value" = None, avm_DataSource65: set["avm_Resource"] = None):
        self.Notes = Notes
        self.avm_DataSource = avm_DataSource
        self.avm_DataSource65 = avm_DataSource65 if avm_DataSource65 is not None else set()
        
    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def avm_DataSource(self):
        return self.__avm_DataSource

    @avm_DataSource.setter
    def avm_DataSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DataSource__avm_DataSource", None)
        self.__avm_DataSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Value20"):
                opp_val = getattr(old_value, "avm_Value20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value20"):
                opp_val = getattr(value, "avm_Value20", None)
                if opp_val is None:
                    setattr(value, "avm_Value20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_DataSource65(self):
        return self.__avm_DataSource65

    @avm_DataSource65.setter
    def avm_DataSource65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DataSource__avm_DataSource65", None)
        self.__avm_DataSource65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource66"):
                    opp_val = getattr(item, "avm_Resource66", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource66"):
                    opp_val = getattr(item, "avm_Resource66", None)
                    
                    setattr(item, "avm_Resource66", self)
                    

class avm_ValueExpressionType(ABC):

    pass
class ValueNode:

    pass
class avm_ValueFlowMux(ValueNode):

    pass
class avm_Value(ValueNode):

    def __init__(self, DimensionType: str, DataType: str, Dimensions: str, Unit: str, avm_Value: "avm_ValueExpressionType" = None, avm_Value20: set["avm_DataSource"] = None, avm_Value52: "avm_DomainModelMetric" = None, avm_Value54: "avm_PrimitiveProperty" = None, avm_Value99: "avm_ComponentPrimitivePropertyInstance" = None, avm_Value131: "avm_TestBenchValueBase" = None):
        self.DimensionType = DimensionType
        self.DataType = DataType
        self.Dimensions = Dimensions
        self.Unit = Unit
        self.avm_Value = avm_Value
        self.avm_Value20 = avm_Value20 if avm_Value20 is not None else set()
        self.avm_Value52 = avm_Value52
        self.avm_Value54 = avm_Value54
        self.avm_Value99 = avm_Value99
        self.avm_Value131 = avm_Value131
        
    @property
    def DimensionType(self) -> str:
        return self.__DimensionType

    @DimensionType.setter
    def DimensionType(self, DimensionType: str):
        self.__DimensionType = DimensionType

    @property
    def Dimensions(self) -> str:
        return self.__Dimensions

    @Dimensions.setter
    def Dimensions(self, Dimensions: str):
        self.__Dimensions = Dimensions

    @property
    def DataType(self) -> str:
        return self.__DataType

    @DataType.setter
    def DataType(self, DataType: str):
        self.__DataType = DataType

    @property
    def Unit(self) -> str:
        return self.__Unit

    @Unit.setter
    def Unit(self, Unit: str):
        self.__Unit = Unit

    @property
    def avm_Value20(self):
        return self.__avm_Value20

    @avm_Value20.setter
    def avm_Value20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value20", None)
        self.__avm_Value20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DataSource"):
                    opp_val = getattr(item, "avm_DataSource", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DataSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DataSource"):
                    opp_val = getattr(item, "avm_DataSource", None)
                    
                    setattr(item, "avm_DataSource", self)
                    

    @property
    def avm_Value99(self):
        return self.__avm_Value99

    @avm_Value99.setter
    def avm_Value99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value99", None)
        self.__avm_Value99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComponentPrimitivePropertyInstance98"):
                opp_val = getattr(old_value, "avm_ComponentPrimitivePropertyInstance98", None)
                if opp_val == self:
                    setattr(old_value, "avm_ComponentPrimitivePropertyInstance98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentPrimitivePropertyInstance98"):
                opp_val = getattr(value, "avm_ComponentPrimitivePropertyInstance98", None)
                setattr(value, "avm_ComponentPrimitivePropertyInstance98", self)

    @property
    def avm_Value52(self):
        return self.__avm_Value52

    @avm_Value52.setter
    def avm_Value52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value52", None)
        self.__avm_Value52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DomainModelMetric"):
                opp_val = getattr(old_value, "avm_DomainModelMetric", None)
                if opp_val == self:
                    setattr(old_value, "avm_DomainModelMetric", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DomainModelMetric"):
                opp_val = getattr(value, "avm_DomainModelMetric", None)
                setattr(value, "avm_DomainModelMetric", self)

    @property
    def avm_Value131(self):
        return self.__avm_Value131

    @avm_Value131.setter
    def avm_Value131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value131", None)
        self.__avm_Value131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBenchValueBase"):
                opp_val = getattr(old_value, "avm_TestBenchValueBase", None)
                if opp_val == self:
                    setattr(old_value, "avm_TestBenchValueBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBenchValueBase"):
                opp_val = getattr(value, "avm_TestBenchValueBase", None)
                setattr(value, "avm_TestBenchValueBase", self)

    @property
    def avm_Value54(self):
        return self.__avm_Value54

    @avm_Value54.setter
    def avm_Value54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value54", None)
        self.__avm_Value54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_PrimitiveProperty"):
                opp_val = getattr(old_value, "avm_PrimitiveProperty", None)
                if opp_val == self:
                    setattr(old_value, "avm_PrimitiveProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_PrimitiveProperty"):
                opp_val = getattr(value, "avm_PrimitiveProperty", None)
                setattr(value, "avm_PrimitiveProperty", self)

    @property
    def avm_Value(self):
        return self.__avm_Value

    @avm_Value.setter
    def avm_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value", None)
        self.__avm_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ValueExpressionType"):
                opp_val = getattr(old_value, "avm_ValueExpressionType", None)
                if opp_val == self:
                    setattr(old_value, "avm_ValueExpressionType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ValueExpressionType"):
                opp_val = getattr(value, "avm_ValueExpressionType", None)
                setattr(value, "avm_ValueExpressionType", self)

class avm_Formula(ValueNode):

    def __init__(self, Name: str, XPosition: str, YPosition: str, avm_Formula: "avm_Component" = None, avm_Formula89: "avm_Container" = None):
        self.Name = Name
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Formula = avm_Formula
        self.avm_Formula89 = avm_Formula89
        
    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Formula89(self):
        return self.__avm_Formula89

    @avm_Formula89.setter
    def avm_Formula89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Formula__avm_Formula89", None)
        self.__avm_Formula89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container88"):
                opp_val = getattr(old_value, "avm_Container88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container88"):
                opp_val = getattr(value, "avm_Container88", None)
                if opp_val is None:
                    setattr(value, "avm_Container88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Formula(self):
        return self.__avm_Formula

    @avm_Formula.setter
    def avm_Formula(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Formula__avm_Formula", None)
        self.__avm_Formula = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component14"):
                opp_val = getattr(old_value, "avm_Component14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component14"):
                opp_val = getattr(value, "avm_Component14", None)
                if opp_val is None:
                    setattr(value, "avm_Component14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Port(PortMapTarget):

    def __init__(self, Notes: str, XPosition: str, Definition: str, YPosition: str, Name: str, avm_Port: "avm_Component" = None, avm_Port24: "avm_Connector" = None, avm_Port80: "avm_Container" = None):
        self.Notes = Notes
        self.XPosition = XPosition
        self.Definition = Definition
        self.YPosition = YPosition
        self.Name = Name
        self.avm_Port = avm_Port
        self.avm_Port24 = avm_Port24
        self.avm_Port80 = avm_Port80
        
    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def Definition(self) -> str:
        return self.__Definition

    @Definition.setter
    def Definition(self, Definition: str):
        self.__Definition = Definition

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def avm_Port24(self):
        return self.__avm_Port24

    @avm_Port24.setter
    def avm_Port24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Port__avm_Port24", None)
        self.__avm_Port24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector23"):
                opp_val = getattr(old_value, "avm_Connector23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector23"):
                opp_val = getattr(value, "avm_Connector23", None)
                if opp_val is None:
                    setattr(value, "avm_Connector23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Port(self):
        return self.__avm_Port

    @avm_Port.setter
    def avm_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Port__avm_Port", None)
        self.__avm_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component10"):
                opp_val = getattr(old_value, "avm_Component10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component10"):
                opp_val = getattr(value, "avm_Component10", None)
                if opp_val is None:
                    setattr(value, "avm_Component10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Port80(self):
        return self.__avm_Port80

    @avm_Port80.setter
    def avm_Port80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Port__avm_Port80", None)
        self.__avm_Port80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container79"):
                opp_val = getattr(old_value, "avm_Container79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container79"):
                opp_val = getattr(value, "avm_Container79", None)
                if opp_val is None:
                    setattr(value, "avm_Container79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_DistributionRestriction(ABC):

    def __init__(self, Notes: str, avm_DistributionRestriction: "avm_Component" = None):
        self.Notes = Notes
        self.avm_DistributionRestriction = avm_DistributionRestriction
        
    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def avm_DistributionRestriction(self):
        return self.__avm_DistributionRestriction

    @avm_DistributionRestriction.setter
    def avm_DistributionRestriction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DistributionRestriction__avm_DistributionRestriction", None)
        self.__avm_DistributionRestriction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component8"):
                opp_val = getattr(old_value, "avm_Component8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component8"):
                opp_val = getattr(value, "avm_Component8", None)
                if opp_val is None:
                    setattr(value, "avm_Component8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Connector(ConnectorCompositionTarget):

    def __init__(self, Definition: str, Name: str, Notes: str, XPosition: str, YPosition: str, avm_Connector: "avm_Component" = None, avm_Connector23: set["avm_Port"] = None, avm_Connector26: set["avm_Property"] = None, avm_Connector29: set["avm_assemblyDetail"] = None, avm_Connector32: "avm_Connector" = None, avm_Connector30: set["avm_Connector"] = None, avm_Connector34: set["avm_ConnectorFeature"] = None, avm_Connector83: "avm_Container" = None):
        self.Definition = Definition
        self.Name = Name
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Connector = avm_Connector
        self.avm_Connector23 = avm_Connector23 if avm_Connector23 is not None else set()
        self.avm_Connector26 = avm_Connector26 if avm_Connector26 is not None else set()
        self.avm_Connector29 = avm_Connector29 if avm_Connector29 is not None else set()
        self.avm_Connector32 = avm_Connector32
        self.avm_Connector30 = avm_Connector30 if avm_Connector30 is not None else set()
        self.avm_Connector34 = avm_Connector34 if avm_Connector34 is not None else set()
        self.avm_Connector83 = avm_Connector83
        
    @property
    def Definition(self) -> str:
        return self.__Definition

    @Definition.setter
    def Definition(self, Definition: str):
        self.__Definition = Definition

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Connector23(self):
        return self.__avm_Connector23

    @avm_Connector23.setter
    def avm_Connector23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector23", None)
        self.__avm_Connector23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Port24"):
                    opp_val = getattr(item, "avm_Port24", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Port24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Port24"):
                    opp_val = getattr(item, "avm_Port24", None)
                    
                    setattr(item, "avm_Port24", self)
                    

    @property
    def avm_Connector29(self):
        return self.__avm_Connector29

    @avm_Connector29.setter
    def avm_Connector29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector29", None)
        self.__avm_Connector29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_assemblyDetail"):
                    opp_val = getattr(item, "avm_assemblyDetail", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_assemblyDetail", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_assemblyDetail"):
                    opp_val = getattr(item, "avm_assemblyDetail", None)
                    
                    setattr(item, "avm_assemblyDetail", self)
                    

    @property
    def avm_Connector30(self):
        return self.__avm_Connector30

    @avm_Connector30.setter
    def avm_Connector30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector30", None)
        self.__avm_Connector30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Connector32"):
                    opp_val = getattr(item, "avm_Connector32", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Connector32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Connector32"):
                    opp_val = getattr(item, "avm_Connector32", None)
                    
                    setattr(item, "avm_Connector32", self)
                    

    @property
    def avm_Connector34(self):
        return self.__avm_Connector34

    @avm_Connector34.setter
    def avm_Connector34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector34", None)
        self.__avm_Connector34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ConnectorFeature"):
                    opp_val = getattr(item, "avm_ConnectorFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ConnectorFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ConnectorFeature"):
                    opp_val = getattr(item, "avm_ConnectorFeature", None)
                    
                    setattr(item, "avm_ConnectorFeature", self)
                    

    @property
    def avm_Connector32(self):
        return self.__avm_Connector32

    @avm_Connector32.setter
    def avm_Connector32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector32", None)
        self.__avm_Connector32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector30"):
                opp_val = getattr(old_value, "avm_Connector30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector30"):
                opp_val = getattr(value, "avm_Connector30", None)
                if opp_val is None:
                    setattr(value, "avm_Connector30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Connector83(self):
        return self.__avm_Connector83

    @avm_Connector83.setter
    def avm_Connector83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector83", None)
        self.__avm_Connector83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container82"):
                opp_val = getattr(old_value, "avm_Container82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container82"):
                opp_val = getattr(value, "avm_Container82", None)
                if opp_val is None:
                    setattr(value, "avm_Container82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Connector26(self):
        return self.__avm_Connector26

    @avm_Connector26.setter
    def avm_Connector26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector26", None)
        self.__avm_Connector26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Property27"):
                    opp_val = getattr(item, "avm_Property27", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Property27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Property27"):
                    opp_val = getattr(item, "avm_Property27", None)
                    
                    setattr(item, "avm_Property27", self)
                    

    @property
    def avm_Connector(self):
        return self.__avm_Connector

    @avm_Connector.setter
    def avm_Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector", None)
        self.__avm_Connector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component6"):
                opp_val = getattr(old_value, "avm_Component6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component6"):
                opp_val = getattr(value, "avm_Component6", None)
                if opp_val is None:
                    setattr(value, "avm_Component6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Resource:

    def __init__(self, Name: str, Path: str, Hash: str, ID: str, Notes: str, XPosition: str, YPosition: str, avm_Resource: "avm_Component" = None, avm_Resource17: "avm_DomainModel" = None, avm_Resource66: "avm_DataSource" = None):
        self.Name = Name
        self.Path = Path
        self.Hash = Hash
        self.ID = ID
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Resource = avm_Resource
        self.avm_Resource17 = avm_Resource17
        self.avm_Resource66 = avm_Resource66
        
    @property
    def Path(self) -> str:
        return self.__Path

    @Path.setter
    def Path(self, Path: str):
        self.__Path = Path

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def Hash(self) -> str:
        return self.__Hash

    @Hash.setter
    def Hash(self, Hash: str):
        self.__Hash = Hash

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Resource66(self):
        return self.__avm_Resource66

    @avm_Resource66.setter
    def avm_Resource66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource66", None)
        self.__avm_Resource66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DataSource65"):
                opp_val = getattr(old_value, "avm_DataSource65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DataSource65"):
                opp_val = getattr(value, "avm_DataSource65", None)
                if opp_val is None:
                    setattr(value, "avm_DataSource65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Resource17(self):
        return self.__avm_Resource17

    @avm_Resource17.setter
    def avm_Resource17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource17", None)
        self.__avm_Resource17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DomainModel16"):
                opp_val = getattr(old_value, "avm_DomainModel16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DomainModel16"):
                opp_val = getattr(value, "avm_DomainModel16", None)
                if opp_val is None:
                    setattr(value, "avm_DomainModel16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Resource(self):
        return self.__avm_Resource

    @avm_Resource.setter
    def avm_Resource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource", None)
        self.__avm_Resource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component4"):
                opp_val = getattr(old_value, "avm_Component4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component4"):
                opp_val = getattr(value, "avm_Component4", None)
                if opp_val is None:
                    setattr(value, "avm_Component4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Property(ABC):

    def __init__(self, Name: str, OnDataSheet: str, Notes: str, Definition: str, ID: str, XPosition: str, YPosition: str, avm_Property: "avm_Component" = None, avm_Property27: "avm_Connector" = None, avm_Property75: "avm_Container" = None):
        self.Name = Name
        self.OnDataSheet = OnDataSheet
        self.Notes = Notes
        self.Definition = Definition
        self.ID = ID
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Property = avm_Property
        self.avm_Property27 = avm_Property27
        self.avm_Property75 = avm_Property75
        
    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def OnDataSheet(self) -> str:
        return self.__OnDataSheet

    @OnDataSheet.setter
    def OnDataSheet(self, OnDataSheet: str):
        self.__OnDataSheet = OnDataSheet

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def Definition(self) -> str:
        return self.__Definition

    @Definition.setter
    def Definition(self, Definition: str):
        self.__Definition = Definition

    @property
    def avm_Property27(self):
        return self.__avm_Property27

    @avm_Property27.setter
    def avm_Property27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Property__avm_Property27", None)
        self.__avm_Property27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector26"):
                opp_val = getattr(old_value, "avm_Connector26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector26"):
                opp_val = getattr(value, "avm_Connector26", None)
                if opp_val is None:
                    setattr(value, "avm_Connector26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Property75(self):
        return self.__avm_Property75

    @avm_Property75.setter
    def avm_Property75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Property__avm_Property75", None)
        self.__avm_Property75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container74"):
                opp_val = getattr(old_value, "avm_Container74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container74"):
                opp_val = getattr(value, "avm_Container74", None)
                if opp_val is None:
                    setattr(value, "avm_Container74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Property(self):
        return self.__avm_Property

    @avm_Property.setter
    def avm_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Property__avm_Property", None)
        self.__avm_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component2"):
                opp_val = getattr(old_value, "avm_Component2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component2"):
                opp_val = getattr(value, "avm_Component2", None)
                if opp_val is None:
                    setattr(value, "avm_Component2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_DomainModel(ABC):

    def __init__(self, Author: str, Notes: str, XPosition: str, YPosition: str, Name: str, avm_DomainModel: "avm_Component" = None, avm_DomainModel16: set["avm_Resource"] = None, avm_DomainModel129: "avm_TestBench" = None):
        self.Author = Author
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.Name = Name
        self.avm_DomainModel = avm_DomainModel
        self.avm_DomainModel16 = avm_DomainModel16 if avm_DomainModel16 is not None else set()
        self.avm_DomainModel129 = avm_DomainModel129
        
    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Author(self) -> str:
        return self.__Author

    @Author.setter
    def Author(self, Author: str):
        self.__Author = Author

    @property
    def XPosition(self) -> str:
        return self.__XPosition

    @XPosition.setter
    def XPosition(self, XPosition: str):
        self.__XPosition = XPosition

    @property
    def avm_DomainModel129(self):
        return self.__avm_DomainModel129

    @avm_DomainModel129.setter
    def avm_DomainModel129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel129", None)
        self.__avm_DomainModel129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench128"):
                opp_val = getattr(old_value, "avm_TestBench128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench128"):
                opp_val = getattr(value, "avm_TestBench128", None)
                if opp_val is None:
                    setattr(value, "avm_TestBench128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_DomainModel(self):
        return self.__avm_DomainModel

    @avm_DomainModel.setter
    def avm_DomainModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel", None)
        self.__avm_DomainModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Component"):
                opp_val = getattr(old_value, "avm_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Component"):
                opp_val = getattr(value, "avm_Component", None)
                if opp_val is None:
                    setattr(value, "avm_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_DomainModel16(self):
        return self.__avm_DomainModel16

    @avm_DomainModel16.setter
    def avm_DomainModel16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel16", None)
        self.__avm_DomainModel16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource17"):
                    opp_val = getattr(item, "avm_Resource17", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource17"):
                    opp_val = getattr(item, "avm_Resource17", None)
                    
                    setattr(item, "avm_Resource17", self)
                    

class avm_Component:

    def __init__(self, Name: str, Version: str, SchemaVersion: str, Classifications: str, ID: str, Supercedes: str, avm_Component: set["avm_DomainModel"] = None, avm_Component2: set["avm_Property"] = None, avm_Component4: set["avm_Resource"] = None, avm_Component6: set["avm_Connector"] = None, avm_Component8: set["avm_DistributionRestriction"] = None, avm_Component10: set["avm_Port"] = None, avm_Component14: set["avm_Formula"] = None, avm_Component12: set["avm_AnalysisConstruct"] = None):
        self.Name = Name
        self.Version = Version
        self.SchemaVersion = SchemaVersion
        self.Classifications = Classifications
        self.ID = ID
        self.Supercedes = Supercedes
        self.avm_Component = avm_Component if avm_Component is not None else set()
        self.avm_Component2 = avm_Component2 if avm_Component2 is not None else set()
        self.avm_Component4 = avm_Component4 if avm_Component4 is not None else set()
        self.avm_Component6 = avm_Component6 if avm_Component6 is not None else set()
        self.avm_Component8 = avm_Component8 if avm_Component8 is not None else set()
        self.avm_Component10 = avm_Component10 if avm_Component10 is not None else set()
        self.avm_Component14 = avm_Component14 if avm_Component14 is not None else set()
        self.avm_Component12 = avm_Component12 if avm_Component12 is not None else set()
        
    @property
    def SchemaVersion(self) -> str:
        return self.__SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion: str):
        self.__SchemaVersion = SchemaVersion

    @property
    def Supercedes(self) -> str:
        return self.__Supercedes

    @Supercedes.setter
    def Supercedes(self, Supercedes: str):
        self.__Supercedes = Supercedes

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Classifications(self) -> str:
        return self.__Classifications

    @Classifications.setter
    def Classifications(self, Classifications: str):
        self.__Classifications = Classifications

    @property
    def Version(self) -> str:
        return self.__Version

    @Version.setter
    def Version(self, Version: str):
        self.__Version = Version

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_Component8(self):
        return self.__avm_Component8

    @avm_Component8.setter
    def avm_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component8", None)
        self.__avm_Component8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DistributionRestriction"):
                    opp_val = getattr(item, "avm_DistributionRestriction", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DistributionRestriction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DistributionRestriction"):
                    opp_val = getattr(item, "avm_DistributionRestriction", None)
                    
                    setattr(item, "avm_DistributionRestriction", self)
                    

    @property
    def avm_Component10(self):
        return self.__avm_Component10

    @avm_Component10.setter
    def avm_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component10", None)
        self.__avm_Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Port"):
                    opp_val = getattr(item, "avm_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Port"):
                    opp_val = getattr(item, "avm_Port", None)
                    
                    setattr(item, "avm_Port", self)
                    

    @property
    def avm_Component4(self):
        return self.__avm_Component4

    @avm_Component4.setter
    def avm_Component4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component4", None)
        self.__avm_Component4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource"):
                    opp_val = getattr(item, "avm_Resource", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource"):
                    opp_val = getattr(item, "avm_Resource", None)
                    
                    setattr(item, "avm_Resource", self)
                    

    @property
    def avm_Component12(self):
        return self.__avm_Component12

    @avm_Component12.setter
    def avm_Component12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component12", None)
        self.__avm_Component12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_AnalysisConstruct"):
                    opp_val = getattr(item, "avm_AnalysisConstruct", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_AnalysisConstruct", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_AnalysisConstruct"):
                    opp_val = getattr(item, "avm_AnalysisConstruct", None)
                    
                    setattr(item, "avm_AnalysisConstruct", self)
                    

    @property
    def avm_Component6(self):
        return self.__avm_Component6

    @avm_Component6.setter
    def avm_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component6", None)
        self.__avm_Component6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Connector"):
                    opp_val = getattr(item, "avm_Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Connector"):
                    opp_val = getattr(item, "avm_Connector", None)
                    
                    setattr(item, "avm_Connector", self)
                    

    @property
    def avm_Component14(self):
        return self.__avm_Component14

    @avm_Component14.setter
    def avm_Component14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component14", None)
        self.__avm_Component14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Formula"):
                    opp_val = getattr(item, "avm_Formula", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Formula", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Formula"):
                    opp_val = getattr(item, "avm_Formula", None)
                    
                    setattr(item, "avm_Formula", self)
                    

    @property
    def avm_Component(self):
        return self.__avm_Component

    @avm_Component.setter
    def avm_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component", None)
        self.__avm_Component = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DomainModel"):
                    opp_val = getattr(item, "avm_DomainModel", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DomainModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DomainModel"):
                    opp_val = getattr(item, "avm_DomainModel", None)
                    
                    setattr(item, "avm_DomainModel", self)
                    

    @property
    def avm_Component2(self):
        return self.__avm_Component2

    @avm_Component2.setter
    def avm_Component2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component2", None)
        self.__avm_Component2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Property"):
                    opp_val = getattr(item, "avm_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Property"):
                    opp_val = getattr(item, "avm_Property", None)
                    
                    setattr(item, "avm_Property", self)
                    
