from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RedeclareTypeEnum(Enum):
    Package = "Package"
    Class = "Class"
    Model = "Model"
    Record = "Record"
    Block = "Block"
    Connector = "Connector"
    Function = "Function"
class ModelType(Enum):
    SignalFlow = "SignalFlow"
    Simulink = "Simulink"
    ESMoL = "ESMoL"
class RelativeRotationEnum(Enum):
    r0 = "r0"
    r90 = "r90"
    r180 = "r180"
    r270 = "r270"
    NoRestriction = "NoRestriction"
class GlobalConstraintTypeEnum(Enum):
    BoardEdgeSpacing = "BoardEdgeSpacing"
class FunctionEnum(Enum):
    normal = "normal"
    clock = "clock"
    reset_async = "reset_async"
    reset_sync = "reset_sync"
class BoundTypeEnum(Enum):
    MustNotExceed = "MustNotExceed"
    MustNotMeetOrExceed = "MustNotMeetOrExceed"
    MustExceed = "MustExceed"
    MustExceedOrEqual = "MustExceedOrEqual"
class RangeConstraintTypeEnum(Enum):
    Inclusion = "Inclusion"
    Exclusion = "Exclusion"
class JobManagerToolSelection(Enum):
    Dymola_latest = "Dymola_latest"
    Dymola_2014 = "Dymola_2014"
    Dymola_2013 = "Dymola_2013"
    OpenModelica_latest = "OpenModelica_latest"
    JModelica_1_12 = "JModelica_1_12"
class DoDDistributionStatementEnum(Enum):
    StatementA = "StatementA"
    StatementB = "StatementB"
    StatementC = "StatementC"
    StatementD = "StatementD"
    StatementE = "StatementE"
class CalculationTypeEnum(Enum):
    Declarative = "Declarative"
    Python = "Python"
class CustomGeometryInputOperationEnum(Enum):
    Union = "Union"
    Intersection = "Intersection"
    Subtraction = "Subtraction"
class RelativeLayerEnum(Enum):
    Same = "Same"
    Opposite = "Opposite"
class PortDirectionality(Enum):
    in = "in"
    out = "out"
class RotationEnum(Enum):
    r0 = "r0"
    r90 = "r90"
    r180 = "r180"
    r270 = "r270"
class FileFormat(Enum):
    Creo = "Creo"
    AP_203 = "AP_203"
    AP_214 = "AP_214"
    STL = "STL"
class IntervalMethod(Enum):
    NumberOfIntervals = "NumberOfIntervals"
    IntervalLength = "IntervalLength"
class SystemCDataTypeEnum(Enum):
    bool = "bool"
    sc_int = "sc_int"
    sc_uint = "sc_uint"
    sc_logic = "sc_logic"
    sc_bit = "sc_bit"
class LayerEnum(Enum):
    Top = "Top"
    Bottom = "Bottom"
class PartIntersectionEnum(Enum):
    None = "None"
    IntersectionWithAnyParts = "IntersectionWithAnyParts"
    IntersectionWithReferencedParts = "IntersectionWithReferencedParts"
class DirectionalityEnum(Enum):
    in = "in"
    out = "out"
    inout = "inout"
    not_applicable = "not_applicable"
class DimensionTypeEnum(Enum):
    Matrix = "Matrix"
    Vector = "Vector"
    Scalar = "Scalar"
class SimpleFormulaOperation(Enum):
    Addition = "Addition"
    Multiplication = "Multiplication"
    ArithmeticMean = "ArithmeticMean"
    GeometricMean = "GeometricMean"
    Maximum = "Maximum"
    Minimum = "Minimum"
class GeometryQualifierEnum(Enum):
    InteriorAndBoundary = "InteriorAndBoundary"
    InteriorOnly = "InteriorOnly"
    BoundaryOnly = "BoundaryOnly"
class LayerRangeEnum(Enum):
    Either = "Either"
    Top = "Top"
    Bottom = "Bottom"
class DataTypeEnum(Enum):
    String = "String"
    Boolean = "Boolean"
    Integer = "Integer"
    Real = "Real"


############################################
# Definition of Classes
############################################

class avm_adamsCar_FileReference:

    def __init__(self, FilePath: str, ID: str, Name: str, avm_adamsCar_FileReference307: set["FileReference"] = None, avm_adamsCar_FileReference: set["Parameter"] = None):
        self.FilePath = FilePath
        self.ID = ID
        self.Name = Name
        self.avm_adamsCar_FileReference307 = avm_adamsCar_FileReference307 if avm_adamsCar_FileReference307 is not None else set()
        self.avm_adamsCar_FileReference = avm_adamsCar_FileReference if avm_adamsCar_FileReference is not None else set()
        
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
    def FilePath(self) -> str:
        return self.__FilePath

    @FilePath.setter
    def FilePath(self, FilePath: str):
        self.__FilePath = FilePath

    @property
    def avm_adamsCar_FileReference307(self):
        return self.__avm_adamsCar_FileReference307

    @avm_adamsCar_FileReference307.setter
    def avm_adamsCar_FileReference307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_adamsCar_FileReference__avm_adamsCar_FileReference307", None)
        self.__avm_adamsCar_FileReference307 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileReference308"):
                    opp_val = getattr(item, "FileReference308", None)
                    
                    if opp_val == self:
                        setattr(item, "FileReference308", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileReference308"):
                    opp_val = getattr(item, "FileReference308", None)
                    
                    setattr(item, "FileReference308", self)
                    

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
                if hasattr(item, "Parameter305"):
                    opp_val = getattr(item, "Parameter305", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter305", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter305"):
                    opp_val = getattr(item, "Parameter305", None)
                    
                    setattr(item, "Parameter305", self)
                    

class adamsCar_avm_Value:

    pass
class FileReference:

    pass
class CADModel:

    pass
class eda_EDAModel:

    pass
class DomainMapping:

    pass
class avm_domainmapping_CAD2EDATransform(DomainMapping):

    def __init__(self, RotationX: str, RotationY: str, RotationZ: str, TranslationX: str, TranslationY: str, TranslationZ: str, ScaleX: str, ScaleY: str, ScaleZ: str, avm_domainmapping_CAD2EDATransform: "eda_EDAModel" = None, avm_domainmapping_CAD2EDATransform298: "CADModel" = None):
        self.RotationX = RotationX
        self.RotationY = RotationY
        self.RotationZ = RotationZ
        self.TranslationX = TranslationX
        self.TranslationY = TranslationY
        self.TranslationZ = TranslationZ
        self.ScaleX = ScaleX
        self.ScaleY = ScaleY
        self.ScaleZ = ScaleZ
        self.avm_domainmapping_CAD2EDATransform = avm_domainmapping_CAD2EDATransform
        self.avm_domainmapping_CAD2EDATransform298 = avm_domainmapping_CAD2EDATransform298
        
    @property
    def ScaleY(self) -> str:
        return self.__ScaleY

    @ScaleY.setter
    def ScaleY(self, ScaleY: str):
        self.__ScaleY = ScaleY

    @property
    def TranslationZ(self) -> str:
        return self.__TranslationZ

    @TranslationZ.setter
    def TranslationZ(self, TranslationZ: str):
        self.__TranslationZ = TranslationZ

    @property
    def TranslationX(self) -> str:
        return self.__TranslationX

    @TranslationX.setter
    def TranslationX(self, TranslationX: str):
        self.__TranslationX = TranslationX

    @property
    def TranslationY(self) -> str:
        return self.__TranslationY

    @TranslationY.setter
    def TranslationY(self, TranslationY: str):
        self.__TranslationY = TranslationY

    @property
    def ScaleZ(self) -> str:
        return self.__ScaleZ

    @ScaleZ.setter
    def ScaleZ(self, ScaleZ: str):
        self.__ScaleZ = ScaleZ

    @property
    def RotationY(self) -> str:
        return self.__RotationY

    @RotationY.setter
    def RotationY(self, RotationY: str):
        self.__RotationY = RotationY

    @property
    def ScaleX(self) -> str:
        return self.__ScaleX

    @ScaleX.setter
    def ScaleX(self, ScaleX: str):
        self.__ScaleX = ScaleX

    @property
    def RotationZ(self) -> str:
        return self.__RotationZ

    @RotationZ.setter
    def RotationZ(self, RotationZ: str):
        self.__RotationZ = RotationZ

    @property
    def RotationX(self) -> str:
        return self.__RotationX

    @RotationX.setter
    def RotationX(self, RotationX: str):
        self.__RotationX = RotationX

    @property
    def avm_domainmapping_CAD2EDATransform(self):
        return self.__avm_domainmapping_CAD2EDATransform

    @avm_domainmapping_CAD2EDATransform.setter
    def avm_domainmapping_CAD2EDATransform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_domainmapping_CAD2EDATransform__avm_domainmapping_CAD2EDATransform", None)
        self.__avm_domainmapping_CAD2EDATransform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eda_EDAModel"):
                opp_val = getattr(old_value, "eda_EDAModel", None)
                if opp_val == self:
                    setattr(old_value, "eda_EDAModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eda_EDAModel"):
                opp_val = getattr(value, "eda_EDAModel", None)
                setattr(value, "eda_EDAModel", self)

    @property
    def avm_domainmapping_CAD2EDATransform298(self):
        return self.__avm_domainmapping_CAD2EDATransform298

    @avm_domainmapping_CAD2EDATransform298.setter
    def avm_domainmapping_CAD2EDATransform298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_domainmapping_CAD2EDATransform__avm_domainmapping_CAD2EDATransform298", None)
        self.__avm_domainmapping_CAD2EDATransform298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CADModel"):
                opp_val = getattr(old_value, "CADModel", None)
                if opp_val == self:
                    setattr(old_value, "CADModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CADModel"):
                opp_val = getattr(value, "CADModel", None)
                setattr(value, "CADModel", self)

class RFPort:

    pass
class systemc_avm_Value:

    pass
class SystemCPort:

    pass
class spice_avm_Value:

    pass
class spice_Parameter:

    pass
class eda_avm_Container:

    pass
class eda_avm_ComponentInstance:

    pass
class PcbLayoutConstraint:

    pass
class avm_eda_RelativeRangeLayoutConstraint(PcbLayoutConstraint):

    def __init__(self, XRelativeRangeMin: str, XRelativeRangeMax: str, YRelativeRangeMin: str, YRelativeRangeMax: str, RelativeLayer: str, avm_eda_RelativeRangeLayoutConstraint: set["eda_avm_Container"] = None, avm_eda_RelativeRangeLayoutConstraint278: "eda_avm_ComponentInstance" = None, avm_eda_RelativeRangeLayoutConstraint281: set["eda_avm_ComponentInstance"] = None):
        self.XRelativeRangeMin = XRelativeRangeMin
        self.XRelativeRangeMax = XRelativeRangeMax
        self.YRelativeRangeMin = YRelativeRangeMin
        self.YRelativeRangeMax = YRelativeRangeMax
        self.RelativeLayer = RelativeLayer
        self.avm_eda_RelativeRangeLayoutConstraint = avm_eda_RelativeRangeLayoutConstraint if avm_eda_RelativeRangeLayoutConstraint is not None else set()
        self.avm_eda_RelativeRangeLayoutConstraint278 = avm_eda_RelativeRangeLayoutConstraint278
        self.avm_eda_RelativeRangeLayoutConstraint281 = avm_eda_RelativeRangeLayoutConstraint281 if avm_eda_RelativeRangeLayoutConstraint281 is not None else set()
        
    @property
    def XRelativeRangeMax(self) -> str:
        return self.__XRelativeRangeMax

    @XRelativeRangeMax.setter
    def XRelativeRangeMax(self, XRelativeRangeMax: str):
        self.__XRelativeRangeMax = XRelativeRangeMax

    @property
    def YRelativeRangeMax(self) -> str:
        return self.__YRelativeRangeMax

    @YRelativeRangeMax.setter
    def YRelativeRangeMax(self, YRelativeRangeMax: str):
        self.__YRelativeRangeMax = YRelativeRangeMax

    @property
    def XRelativeRangeMin(self) -> str:
        return self.__XRelativeRangeMin

    @XRelativeRangeMin.setter
    def XRelativeRangeMin(self, XRelativeRangeMin: str):
        self.__XRelativeRangeMin = XRelativeRangeMin

    @property
    def RelativeLayer(self) -> str:
        return self.__RelativeLayer

    @RelativeLayer.setter
    def RelativeLayer(self, RelativeLayer: str):
        self.__RelativeLayer = RelativeLayer

    @property
    def YRelativeRangeMin(self) -> str:
        return self.__YRelativeRangeMin

    @YRelativeRangeMin.setter
    def YRelativeRangeMin(self, YRelativeRangeMin: str):
        self.__YRelativeRangeMin = YRelativeRangeMin

    @property
    def avm_eda_RelativeRangeLayoutConstraint278(self):
        return self.__avm_eda_RelativeRangeLayoutConstraint278

    @avm_eda_RelativeRangeLayoutConstraint278.setter
    def avm_eda_RelativeRangeLayoutConstraint278(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeRangeLayoutConstraint__avm_eda_RelativeRangeLayoutConstraint278", None)
        self.__avm_eda_RelativeRangeLayoutConstraint278 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eda_avm_ComponentInstance279"):
                opp_val = getattr(old_value, "eda_avm_ComponentInstance279", None)
                if opp_val == self:
                    setattr(old_value, "eda_avm_ComponentInstance279", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eda_avm_ComponentInstance279"):
                opp_val = getattr(value, "eda_avm_ComponentInstance279", None)
                setattr(value, "eda_avm_ComponentInstance279", self)

    @property
    def avm_eda_RelativeRangeLayoutConstraint(self):
        return self.__avm_eda_RelativeRangeLayoutConstraint

    @avm_eda_RelativeRangeLayoutConstraint.setter
    def avm_eda_RelativeRangeLayoutConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeRangeLayoutConstraint__avm_eda_RelativeRangeLayoutConstraint", None)
        self.__avm_eda_RelativeRangeLayoutConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_Container276"):
                    opp_val = getattr(item, "eda_avm_Container276", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_Container276", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_Container276"):
                    opp_val = getattr(item, "eda_avm_Container276", None)
                    
                    setattr(item, "eda_avm_Container276", self)
                    

    @property
    def avm_eda_RelativeRangeLayoutConstraint281(self):
        return self.__avm_eda_RelativeRangeLayoutConstraint281

    @avm_eda_RelativeRangeLayoutConstraint281.setter
    def avm_eda_RelativeRangeLayoutConstraint281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeRangeLayoutConstraint__avm_eda_RelativeRangeLayoutConstraint281", None)
        self.__avm_eda_RelativeRangeLayoutConstraint281 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_ComponentInstance282"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance282", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_ComponentInstance282", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_ComponentInstance282"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance282", None)
                    
                    setattr(item, "eda_avm_ComponentInstance282", self)
                    

class avm_eda_RelativeLayoutConstraint(PcbLayoutConstraint):

    def __init__(self, XOffset: str, YOffset: str, RelativeLayer: str, RelativeRotation: str, avm_eda_RelativeLayoutConstraint270: "eda_avm_ComponentInstance" = None, avm_eda_RelativeLayoutConstraint273: set["eda_avm_Container"] = None, avm_eda_RelativeLayoutConstraint: set["eda_avm_ComponentInstance"] = None):
        self.XOffset = XOffset
        self.YOffset = YOffset
        self.RelativeLayer = RelativeLayer
        self.RelativeRotation = RelativeRotation
        self.avm_eda_RelativeLayoutConstraint270 = avm_eda_RelativeLayoutConstraint270
        self.avm_eda_RelativeLayoutConstraint273 = avm_eda_RelativeLayoutConstraint273 if avm_eda_RelativeLayoutConstraint273 is not None else set()
        self.avm_eda_RelativeLayoutConstraint = avm_eda_RelativeLayoutConstraint if avm_eda_RelativeLayoutConstraint is not None else set()
        
    @property
    def RelativeLayer(self) -> str:
        return self.__RelativeLayer

    @RelativeLayer.setter
    def RelativeLayer(self, RelativeLayer: str):
        self.__RelativeLayer = RelativeLayer

    @property
    def RelativeRotation(self) -> str:
        return self.__RelativeRotation

    @RelativeRotation.setter
    def RelativeRotation(self, RelativeRotation: str):
        self.__RelativeRotation = RelativeRotation

    @property
    def YOffset(self) -> str:
        return self.__YOffset

    @YOffset.setter
    def YOffset(self, YOffset: str):
        self.__YOffset = YOffset

    @property
    def XOffset(self) -> str:
        return self.__XOffset

    @XOffset.setter
    def XOffset(self, XOffset: str):
        self.__XOffset = XOffset

    @property
    def avm_eda_RelativeLayoutConstraint273(self):
        return self.__avm_eda_RelativeLayoutConstraint273

    @avm_eda_RelativeLayoutConstraint273.setter
    def avm_eda_RelativeLayoutConstraint273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeLayoutConstraint__avm_eda_RelativeLayoutConstraint273", None)
        self.__avm_eda_RelativeLayoutConstraint273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_Container274"):
                    opp_val = getattr(item, "eda_avm_Container274", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_Container274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_Container274"):
                    opp_val = getattr(item, "eda_avm_Container274", None)
                    
                    setattr(item, "eda_avm_Container274", self)
                    

    @property
    def avm_eda_RelativeLayoutConstraint(self):
        return self.__avm_eda_RelativeLayoutConstraint

    @avm_eda_RelativeLayoutConstraint.setter
    def avm_eda_RelativeLayoutConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeLayoutConstraint__avm_eda_RelativeLayoutConstraint", None)
        self.__avm_eda_RelativeLayoutConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_ComponentInstance268"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance268", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_ComponentInstance268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_ComponentInstance268"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance268", None)
                    
                    setattr(item, "eda_avm_ComponentInstance268", self)
                    

    @property
    def avm_eda_RelativeLayoutConstraint270(self):
        return self.__avm_eda_RelativeLayoutConstraint270

    @avm_eda_RelativeLayoutConstraint270.setter
    def avm_eda_RelativeLayoutConstraint270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RelativeLayoutConstraint__avm_eda_RelativeLayoutConstraint270", None)
        self.__avm_eda_RelativeLayoutConstraint270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eda_avm_ComponentInstance271"):
                opp_val = getattr(old_value, "eda_avm_ComponentInstance271", None)
                if opp_val == self:
                    setattr(old_value, "eda_avm_ComponentInstance271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eda_avm_ComponentInstance271"):
                opp_val = getattr(value, "eda_avm_ComponentInstance271", None)
                setattr(value, "eda_avm_ComponentInstance271", self)

class avm_eda_GlobalLayoutConstraintException(PcbLayoutConstraint):

    def __init__(self, Constraint: str, avm_eda_GlobalLayoutConstraintException: set["eda_avm_ComponentInstance"] = None, avm_eda_GlobalLayoutConstraintException286: set["eda_avm_Container"] = None):
        self.Constraint = Constraint
        self.avm_eda_GlobalLayoutConstraintException = avm_eda_GlobalLayoutConstraintException if avm_eda_GlobalLayoutConstraintException is not None else set()
        self.avm_eda_GlobalLayoutConstraintException286 = avm_eda_GlobalLayoutConstraintException286 if avm_eda_GlobalLayoutConstraintException286 is not None else set()
        
    @property
    def Constraint(self) -> str:
        return self.__Constraint

    @Constraint.setter
    def Constraint(self, Constraint: str):
        self.__Constraint = Constraint

    @property
    def avm_eda_GlobalLayoutConstraintException(self):
        return self.__avm_eda_GlobalLayoutConstraintException

    @avm_eda_GlobalLayoutConstraintException.setter
    def avm_eda_GlobalLayoutConstraintException(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_GlobalLayoutConstraintException__avm_eda_GlobalLayoutConstraintException", None)
        self.__avm_eda_GlobalLayoutConstraintException = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_ComponentInstance284"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance284", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_ComponentInstance284", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_ComponentInstance284"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance284", None)
                    
                    setattr(item, "eda_avm_ComponentInstance284", self)
                    

    @property
    def avm_eda_GlobalLayoutConstraintException286(self):
        return self.__avm_eda_GlobalLayoutConstraintException286

    @avm_eda_GlobalLayoutConstraintException286.setter
    def avm_eda_GlobalLayoutConstraintException286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_GlobalLayoutConstraintException__avm_eda_GlobalLayoutConstraintException286", None)
        self.__avm_eda_GlobalLayoutConstraintException286 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_Container287"):
                    opp_val = getattr(item, "eda_avm_Container287", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_Container287", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_Container287"):
                    opp_val = getattr(item, "eda_avm_Container287", None)
                    
                    setattr(item, "eda_avm_Container287", self)
                    

class avm_eda_RangeLayoutConstraint(PcbLayoutConstraint):

    def __init__(self, XRangeMin: str, XRangeMax: str, YRangeMin: str, YRangeMax: str, LayerRange: str, Type: str, avm_eda_RangeLayoutConstraint: set["eda_avm_ComponentInstance"] = None, avm_eda_RangeLayoutConstraint265: set["eda_avm_Container"] = None):
        self.XRangeMin = XRangeMin
        self.XRangeMax = XRangeMax
        self.YRangeMin = YRangeMin
        self.YRangeMax = YRangeMax
        self.LayerRange = LayerRange
        self.Type = Type
        self.avm_eda_RangeLayoutConstraint = avm_eda_RangeLayoutConstraint if avm_eda_RangeLayoutConstraint is not None else set()
        self.avm_eda_RangeLayoutConstraint265 = avm_eda_RangeLayoutConstraint265 if avm_eda_RangeLayoutConstraint265 is not None else set()
        
    @property
    def LayerRange(self) -> str:
        return self.__LayerRange

    @LayerRange.setter
    def LayerRange(self, LayerRange: str):
        self.__LayerRange = LayerRange

    @property
    def XRangeMax(self) -> str:
        return self.__XRangeMax

    @XRangeMax.setter
    def XRangeMax(self, XRangeMax: str):
        self.__XRangeMax = XRangeMax

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def YRangeMin(self) -> str:
        return self.__YRangeMin

    @YRangeMin.setter
    def YRangeMin(self, YRangeMin: str):
        self.__YRangeMin = YRangeMin

    @property
    def XRangeMin(self) -> str:
        return self.__XRangeMin

    @XRangeMin.setter
    def XRangeMin(self, XRangeMin: str):
        self.__XRangeMin = XRangeMin

    @property
    def YRangeMax(self) -> str:
        return self.__YRangeMax

    @YRangeMax.setter
    def YRangeMax(self, YRangeMax: str):
        self.__YRangeMax = YRangeMax

    @property
    def avm_eda_RangeLayoutConstraint(self):
        return self.__avm_eda_RangeLayoutConstraint

    @avm_eda_RangeLayoutConstraint.setter
    def avm_eda_RangeLayoutConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RangeLayoutConstraint__avm_eda_RangeLayoutConstraint", None)
        self.__avm_eda_RangeLayoutConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_ComponentInstance263"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance263", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_ComponentInstance263", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_ComponentInstance263"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance263", None)
                    
                    setattr(item, "eda_avm_ComponentInstance263", self)
                    

    @property
    def avm_eda_RangeLayoutConstraint265(self):
        return self.__avm_eda_RangeLayoutConstraint265

    @avm_eda_RangeLayoutConstraint265.setter
    def avm_eda_RangeLayoutConstraint265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_RangeLayoutConstraint__avm_eda_RangeLayoutConstraint265", None)
        self.__avm_eda_RangeLayoutConstraint265 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_Container266"):
                    opp_val = getattr(item, "eda_avm_Container266", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_Container266", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_Container266"):
                    opp_val = getattr(item, "eda_avm_Container266", None)
                    
                    setattr(item, "eda_avm_Container266", self)
                    

class avm_eda_ExactLayoutConstraint(PcbLayoutConstraint):

    def __init__(self, X: str, Y: str, Layer: str, Rotation: str, avm_eda_ExactLayoutConstraint: set["eda_avm_ComponentInstance"] = None, avm_eda_ExactLayoutConstraint261: set["eda_avm_Container"] = None):
        self.X = X
        self.Y = Y
        self.Layer = Layer
        self.Rotation = Rotation
        self.avm_eda_ExactLayoutConstraint = avm_eda_ExactLayoutConstraint if avm_eda_ExactLayoutConstraint is not None else set()
        self.avm_eda_ExactLayoutConstraint261 = avm_eda_ExactLayoutConstraint261 if avm_eda_ExactLayoutConstraint261 is not None else set()
        
    @property
    def Y(self) -> str:
        return self.__Y

    @Y.setter
    def Y(self, Y: str):
        self.__Y = Y

    @property
    def Rotation(self) -> str:
        return self.__Rotation

    @Rotation.setter
    def Rotation(self, Rotation: str):
        self.__Rotation = Rotation

    @property
    def Layer(self) -> str:
        return self.__Layer

    @Layer.setter
    def Layer(self, Layer: str):
        self.__Layer = Layer

    @property
    def X(self) -> str:
        return self.__X

    @X.setter
    def X(self, X: str):
        self.__X = X

    @property
    def avm_eda_ExactLayoutConstraint(self):
        return self.__avm_eda_ExactLayoutConstraint

    @avm_eda_ExactLayoutConstraint.setter
    def avm_eda_ExactLayoutConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_ExactLayoutConstraint__avm_eda_ExactLayoutConstraint", None)
        self.__avm_eda_ExactLayoutConstraint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_ComponentInstance"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_ComponentInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_ComponentInstance"):
                    opp_val = getattr(item, "eda_avm_ComponentInstance", None)
                    
                    setattr(item, "eda_avm_ComponentInstance", self)
                    

    @property
    def avm_eda_ExactLayoutConstraint261(self):
        return self.__avm_eda_ExactLayoutConstraint261

    @avm_eda_ExactLayoutConstraint261.setter
    def avm_eda_ExactLayoutConstraint261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_ExactLayoutConstraint__avm_eda_ExactLayoutConstraint261", None)
        self.__avm_eda_ExactLayoutConstraint261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_avm_Container"):
                    opp_val = getattr(item, "eda_avm_Container", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_avm_Container", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_avm_Container"):
                    opp_val = getattr(item, "eda_avm_Container", None)
                    
                    setattr(item, "eda_avm_Container", self)
                    

class ContainerFeature:

    pass
class avm_eda_PcbLayoutConstraint(ContainerFeature):

    def __init__(self, XPosition: str, YPosition: str, Notes: str):
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.Notes = Notes
        
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
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

class eda_avm_Value:

    pass
class eda_Parameter:

    pass
class SchematicModel:

    pass
class avm_spice_SPICEModel(SchematicModel):

    def __init__(self, Class: str, avm_spice_SPICEModel: set["spice_Parameter"] = None):
        self.Class = Class
        self.avm_spice_SPICEModel = avm_spice_SPICEModel if avm_spice_SPICEModel is not None else set()
        
    @property
    def Class(self) -> str:
        return self.__Class

    @Class.setter
    def Class(self, Class: str):
        self.__Class = Class

    @property
    def avm_spice_SPICEModel(self):
        return self.__avm_spice_SPICEModel

    @avm_spice_SPICEModel.setter
    def avm_spice_SPICEModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_spice_SPICEModel__avm_spice_SPICEModel", None)
        self.__avm_spice_SPICEModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "spice_Parameter"):
                    opp_val = getattr(item, "spice_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "spice_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "spice_Parameter"):
                    opp_val = getattr(item, "spice_Parameter", None)
                    
                    setattr(item, "spice_Parameter", self)
                    

class avm_eda_EDAModel(SchematicModel):

    def __init__(self, Library: str, DeviceSet: str, Device: str, Package: str, HasMultiLayerFootprint: str, avm_eda_EDAModel: set["eda_Parameter"] = None):
        self.Library = Library
        self.DeviceSet = DeviceSet
        self.Device = Device
        self.Package = Package
        self.HasMultiLayerFootprint = HasMultiLayerFootprint
        self.avm_eda_EDAModel = avm_eda_EDAModel if avm_eda_EDAModel is not None else set()
        
    @property
    def DeviceSet(self) -> str:
        return self.__DeviceSet

    @DeviceSet.setter
    def DeviceSet(self, DeviceSet: str):
        self.__DeviceSet = DeviceSet

    @property
    def Package(self) -> str:
        return self.__Package

    @Package.setter
    def Package(self, Package: str):
        self.__Package = Package

    @property
    def HasMultiLayerFootprint(self) -> str:
        return self.__HasMultiLayerFootprint

    @HasMultiLayerFootprint.setter
    def HasMultiLayerFootprint(self, HasMultiLayerFootprint: str):
        self.__HasMultiLayerFootprint = HasMultiLayerFootprint

    @property
    def Device(self) -> str:
        return self.__Device

    @Device.setter
    def Device(self, Device: str):
        self.__Device = Device

    @property
    def Library(self) -> str:
        return self.__Library

    @Library.setter
    def Library(self, Library: str):
        self.__Library = Library

    @property
    def avm_eda_EDAModel(self):
        return self.__avm_eda_EDAModel

    @avm_eda_EDAModel.setter
    def avm_eda_EDAModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_EDAModel__avm_eda_EDAModel", None)
        self.__avm_eda_EDAModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eda_Parameter"):
                    opp_val = getattr(item, "eda_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "eda_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eda_Parameter"):
                    opp_val = getattr(item, "eda_Parameter", None)
                    
                    setattr(item, "eda_Parameter", self)
                    

class Pin:

    pass
class manufacturing_avm_Value:

    pass
class Axis:

    pass
class KinematicJointSpec:

    pass
class avm_cad_TranslationalJointSpec(KinematicJointSpec):

    pass
class avm_cad_RevoluteJointSpec(KinematicJointSpec):

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
class Geometry3D:

    pass
class avm_cad_Surface(Geometry3D):

    pass
class avm_cad_Sphere(Geometry3D):

    pass
class avm_cad_ExtrudedGeometry(Geometry3D):

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
class avm_cad_Geometry3D(Geometry):

    pass
class avm_cad_CustomGeometry(Geometry):

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
class avm_cad_Point(Datum):

    pass
class avm_cad_CoordinateSystem(Datum):

    pass
class avm_cad_Plane(Datum):

    pass
class avm_cad_Axis(Datum):

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
    def Tolerance(self) -> str:
        return self.__Tolerance

    @Tolerance.setter
    def Tolerance(self, Tolerance: str):
        self.__Tolerance = Tolerance

    @property
    def IntervalLength(self) -> str:
        return self.__IntervalLength

    @IntervalLength.setter
    def IntervalLength(self, IntervalLength: str):
        self.__IntervalLength = IntervalLength

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
    def JobManagerToolSelection(self) -> str:
        return self.__JobManagerToolSelection

    @JobManagerToolSelection.setter
    def JobManagerToolSelection(self, JobManagerToolSelection: str):
        self.__JobManagerToolSelection = JobManagerToolSelection

class avm_modelica_Limit:

    def __init__(self, VariableLocator: str, BoundType: str, Name: str, ToleranceTimeWindow: str, Notes: str, avm_modelica_Limit: "modelica_avm_Value" = None):
        self.VariableLocator = VariableLocator
        self.BoundType = BoundType
        self.Name = Name
        self.ToleranceTimeWindow = ToleranceTimeWindow
        self.Notes = Notes
        self.avm_modelica_Limit = avm_modelica_Limit
        
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
    def avm_modelica_Limit(self):
        return self.__avm_modelica_Limit

    @avm_modelica_Limit.setter
    def avm_modelica_Limit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Limit__avm_modelica_Limit", None)
        self.__avm_modelica_Limit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelica_avm_Value169"):
                opp_val = getattr(old_value, "modelica_avm_Value169", None)
                if opp_val == self:
                    setattr(old_value, "modelica_avm_Value169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelica_avm_Value169"):
                opp_val = getattr(value, "modelica_avm_Value169", None)
                setattr(value, "modelica_avm_Value169", self)

class DomainModelMetric:

    pass
class avm_cad_Metric(DomainModelMetric):

    def __init__(self, Name: str):
        self.Name = Name
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

class avm_manufacturing_Metric(DomainModelMetric):

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
class avm_systemc_Parameter(DomainModelParameter):

    def __init__(self, ParamName: str, ParamPosition: str, avm_systemc_Parameter: "systemc_avm_Value" = None):
        self.ParamName = ParamName
        self.ParamPosition = ParamPosition
        self.avm_systemc_Parameter = avm_systemc_Parameter
        
    @property
    def ParamPosition(self) -> str:
        return self.__ParamPosition

    @ParamPosition.setter
    def ParamPosition(self, ParamPosition: str):
        self.__ParamPosition = ParamPosition

    @property
    def ParamName(self) -> str:
        return self.__ParamName

    @ParamName.setter
    def ParamName(self, ParamName: str):
        self.__ParamName = ParamName

    @property
    def avm_systemc_Parameter(self):
        return self.__avm_systemc_Parameter

    @avm_systemc_Parameter.setter
    def avm_systemc_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_systemc_Parameter__avm_systemc_Parameter", None)
        self.__avm_systemc_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "systemc_avm_Value"):
                opp_val = getattr(old_value, "systemc_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "systemc_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "systemc_avm_Value"):
                opp_val = getattr(value, "systemc_avm_Value", None)
                setattr(value, "systemc_avm_Value", self)

class avm_manufacturing_Parameter(DomainModelParameter):

    def __init__(self, Locator: str, Name: str, avm_manufacturing_Parameter: "manufacturing_avm_Value" = None):
        self.Locator = Locator
        self.Name = Name
        self.avm_manufacturing_Parameter = avm_manufacturing_Parameter
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

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

class avm_modelica_Redeclare(DomainModelParameter):

    def __init__(self, Locator: str, Type: str, avm_modelica_Redeclare: "modelica_avm_Value" = None):
        self.Locator = Locator
        self.Type = Type
        self.avm_modelica_Redeclare = avm_modelica_Redeclare
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

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
            if hasattr(old_value, "modelica_avm_Value171"):
                opp_val = getattr(old_value, "modelica_avm_Value171", None)
                if opp_val == self:
                    setattr(old_value, "modelica_avm_Value171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelica_avm_Value171"):
                opp_val = getattr(value, "modelica_avm_Value171", None)
                setattr(value, "modelica_avm_Value171", self)

class avm_eda_Parameter(DomainModelParameter):

    def __init__(self, Locator: str, avm_eda_Parameter: "eda_avm_Value" = None):
        self.Locator = Locator
        self.avm_eda_Parameter = avm_eda_Parameter
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def avm_eda_Parameter(self):
        return self.__avm_eda_Parameter

    @avm_eda_Parameter.setter
    def avm_eda_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_eda_Parameter__avm_eda_Parameter", None)
        self.__avm_eda_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eda_avm_Value"):
                opp_val = getattr(old_value, "eda_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "eda_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eda_avm_Value"):
                opp_val = getattr(value, "eda_avm_Value", None)
                setattr(value, "eda_avm_Value", self)

class avm_spice_Parameter(DomainModelParameter):

    def __init__(self, Locator: str, avm_spice_Parameter: "spice_avm_Value" = None):
        self.Locator = Locator
        self.avm_spice_Parameter = avm_spice_Parameter
        
    @property
    def Locator(self) -> str:
        return self.__Locator

    @Locator.setter
    def Locator(self, Locator: str):
        self.__Locator = Locator

    @property
    def avm_spice_Parameter(self):
        return self.__avm_spice_Parameter

    @avm_spice_Parameter.setter
    def avm_spice_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_spice_Parameter__avm_spice_Parameter", None)
        self.__avm_spice_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "spice_avm_Value"):
                opp_val = getattr(old_value, "spice_avm_Value", None)
                if opp_val == self:
                    setattr(old_value, "spice_avm_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "spice_avm_Value"):
                opp_val = getattr(value, "spice_avm_Value", None)
                setattr(value, "spice_avm_Value", self)

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
class avm_schematic_Pin(DomainModelPort):

    def __init__(self, EDAGate: str, EDASymbolLocationX: str, SPICEPortNumber: str, EDASymbolLocationY: str, EDASymbolRotation: str):
        self.EDAGate = EDAGate
        self.EDASymbolLocationX = EDASymbolLocationX
        self.SPICEPortNumber = SPICEPortNumber
        self.EDASymbolLocationY = EDASymbolLocationY
        self.EDASymbolRotation = EDASymbolRotation
        
    @property
    def EDAGate(self) -> str:
        return self.__EDAGate

    @EDAGate.setter
    def EDAGate(self, EDAGate: str):
        self.__EDAGate = EDAGate

    @property
    def EDASymbolLocationX(self) -> str:
        return self.__EDASymbolLocationX

    @EDASymbolLocationX.setter
    def EDASymbolLocationX(self, EDASymbolLocationX: str):
        self.__EDASymbolLocationX = EDASymbolLocationX

    @property
    def EDASymbolLocationY(self) -> str:
        return self.__EDASymbolLocationY

    @EDASymbolLocationY.setter
    def EDASymbolLocationY(self, EDASymbolLocationY: str):
        self.__EDASymbolLocationY = EDASymbolLocationY

    @property
    def SPICEPortNumber(self) -> str:
        return self.__SPICEPortNumber

    @SPICEPortNumber.setter
    def SPICEPortNumber(self, SPICEPortNumber: str):
        self.__SPICEPortNumber = SPICEPortNumber

    @property
    def EDASymbolRotation(self) -> str:
        return self.__EDASymbolRotation

    @EDASymbolRotation.setter
    def EDASymbolRotation(self, EDASymbolRotation: str):
        self.__EDASymbolRotation = EDASymbolRotation

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
                if hasattr(item, "Metric180"):
                    opp_val = getattr(item, "Metric180", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric180"):
                    opp_val = getattr(item, "Metric180", None)
                    
                    setattr(item, "Metric180", self)
                    

class avm_rf_RFPort(DomainModelPort):

    def __init__(self, Directionality: str, NominalImpedance: str):
        self.Directionality = Directionality
        self.NominalImpedance = NominalImpedance
        
    @property
    def Directionality(self) -> str:
        return self.__Directionality

    @Directionality.setter
    def Directionality(self, Directionality: str):
        self.__Directionality = Directionality

    @property
    def NominalImpedance(self) -> str:
        return self.__NominalImpedance

    @NominalImpedance.setter
    def NominalImpedance(self, NominalImpedance: str):
        self.__NominalImpedance = NominalImpedance

class avm_systemc_SystemCPort(DomainModelPort):

    def __init__(self, DataType: str, DataTypeDimension: str, Directionality: str, Function: str):
        self.DataType = DataType
        self.DataTypeDimension = DataTypeDimension
        self.Directionality = Directionality
        self.Function = Function
        
    @property
    def DataType(self) -> str:
        return self.__DataType

    @DataType.setter
    def DataType(self, DataType: str):
        self.__DataType = DataType

    @property
    def Directionality(self) -> str:
        return self.__Directionality

    @Directionality.setter
    def Directionality(self, Directionality: str):
        self.__Directionality = Directionality

    @property
    def DataTypeDimension(self) -> str:
        return self.__DataTypeDimension

    @DataTypeDimension.setter
    def DataTypeDimension(self, DataTypeDimension: str):
        self.__DataTypeDimension = DataTypeDimension

    @property
    def Function(self) -> str:
        return self.__Function

    @Function.setter
    def Function(self, Function: str):
        self.__Function = Function

class avm_modelica_Connector(DomainModelPort):

    def __init__(self, Class: str, Locator: str, avm_modelica_Connector: set["Parameter"] = None, avm_modelica_Connector165: set["Redeclare"] = None):
        self.Class = Class
        self.Locator = Locator
        self.avm_modelica_Connector = avm_modelica_Connector if avm_modelica_Connector is not None else set()
        self.avm_modelica_Connector165 = avm_modelica_Connector165 if avm_modelica_Connector165 is not None else set()
        
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
                if hasattr(item, "Parameter163"):
                    opp_val = getattr(item, "Parameter163", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter163"):
                    opp_val = getattr(item, "Parameter163", None)
                    
                    setattr(item, "Parameter163", self)
                    

    @property
    def avm_modelica_Connector165(self):
        return self.__avm_modelica_Connector165

    @avm_modelica_Connector165.setter
    def avm_modelica_Connector165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_Connector__avm_modelica_Connector165", None)
        self.__avm_modelica_Connector165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Redeclare166"):
                    opp_val = getattr(item, "Redeclare166", None)
                    
                    if opp_val == self:
                        setattr(item, "Redeclare166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Redeclare166"):
                    opp_val = getattr(item, "Redeclare166", None)
                    
                    setattr(item, "Redeclare166", self)
                    

class Redeclare:

    pass
class Limit:

    pass
class Metric:

    pass
class Connector:

    pass
class Parameter:

    pass
class DomainModel:

    pass
class avm_cad_CADModel(DomainModel):

    def __init__(self, Format: str, avm_cad_CADModel: set["Datum"] = None, avm_cad_CADModel174: set["Parameter"] = None, avm_cad_CADModel177: set["Metric"] = None):
        self.Format = Format
        self.avm_cad_CADModel = avm_cad_CADModel if avm_cad_CADModel is not None else set()
        self.avm_cad_CADModel174 = avm_cad_CADModel174 if avm_cad_CADModel174 is not None else set()
        self.avm_cad_CADModel177 = avm_cad_CADModel177 if avm_cad_CADModel177 is not None else set()
        
    @property
    def Format(self) -> str:
        return self.__Format

    @Format.setter
    def Format(self, Format: str):
        self.__Format = Format

    @property
    def avm_cad_CADModel177(self):
        return self.__avm_cad_CADModel177

    @avm_cad_CADModel177.setter
    def avm_cad_CADModel177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_CADModel__avm_cad_CADModel177", None)
        self.__avm_cad_CADModel177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Metric178"):
                    opp_val = getattr(item, "Metric178", None)
                    
                    if opp_val == self:
                        setattr(item, "Metric178", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Metric178"):
                    opp_val = getattr(item, "Metric178", None)
                    
                    setattr(item, "Metric178", self)
                    

    @property
    def avm_cad_CADModel(self):
        return self.__avm_cad_CADModel

    @avm_cad_CADModel.setter
    def avm_cad_CADModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_CADModel__avm_cad_CADModel", None)
        self.__avm_cad_CADModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Datum"):
                    opp_val = getattr(item, "Datum", None)
                    
                    if opp_val == self:
                        setattr(item, "Datum", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Datum"):
                    opp_val = getattr(item, "Datum", None)
                    
                    setattr(item, "Datum", self)
                    

    @property
    def avm_cad_CADModel174(self):
        return self.__avm_cad_CADModel174

    @avm_cad_CADModel174.setter
    def avm_cad_CADModel174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cad_CADModel__avm_cad_CADModel174", None)
        self.__avm_cad_CADModel174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter175"):
                    opp_val = getattr(item, "Parameter175", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter175"):
                    opp_val = getattr(item, "Parameter175", None)
                    
                    setattr(item, "Parameter175", self)
                    

class avm_manufacturing_ManufacturingModel(DomainModel):

    pass
class avm_rf_RFModel(DomainModel):

    def __init__(self, Rotation: str, X: str, Y: str, avm_rf_RFModel: set["RFPort"] = None):
        self.Rotation = Rotation
        self.X = X
        self.Y = Y
        self.avm_rf_RFModel = avm_rf_RFModel if avm_rf_RFModel is not None else set()
        
    @property
    def Rotation(self) -> str:
        return self.__Rotation

    @Rotation.setter
    def Rotation(self, Rotation: str):
        self.__Rotation = Rotation

    @property
    def X(self) -> str:
        return self.__X

    @X.setter
    def X(self, X: str):
        self.__X = X

    @property
    def Y(self) -> str:
        return self.__Y

    @Y.setter
    def Y(self, Y: str):
        self.__Y = Y

    @property
    def avm_rf_RFModel(self):
        return self.__avm_rf_RFModel

    @avm_rf_RFModel.setter
    def avm_rf_RFModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_rf_RFModel__avm_rf_RFModel", None)
        self.__avm_rf_RFModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RFPort"):
                    opp_val = getattr(item, "RFPort", None)
                    
                    if opp_val == self:
                        setattr(item, "RFPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RFPort"):
                    opp_val = getattr(item, "RFPort", None)
                    
                    setattr(item, "RFPort", self)
                    

class avm_systemc_SystemCModel(DomainModel):

    def __init__(self, ModuleName: str, avm_systemc_SystemCModel: set["SystemCPort"] = None, avm_systemc_SystemCModel292: set["Parameter"] = None):
        self.ModuleName = ModuleName
        self.avm_systemc_SystemCModel = avm_systemc_SystemCModel if avm_systemc_SystemCModel is not None else set()
        self.avm_systemc_SystemCModel292 = avm_systemc_SystemCModel292 if avm_systemc_SystemCModel292 is not None else set()
        
    @property
    def ModuleName(self) -> str:
        return self.__ModuleName

    @ModuleName.setter
    def ModuleName(self, ModuleName: str):
        self.__ModuleName = ModuleName

    @property
    def avm_systemc_SystemCModel292(self):
        return self.__avm_systemc_SystemCModel292

    @avm_systemc_SystemCModel292.setter
    def avm_systemc_SystemCModel292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_systemc_SystemCModel__avm_systemc_SystemCModel292", None)
        self.__avm_systemc_SystemCModel292 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter293"):
                    opp_val = getattr(item, "Parameter293", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter293", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter293"):
                    opp_val = getattr(item, "Parameter293", None)
                    
                    setattr(item, "Parameter293", self)
                    

    @property
    def avm_systemc_SystemCModel(self):
        return self.__avm_systemc_SystemCModel

    @avm_systemc_SystemCModel.setter
    def avm_systemc_SystemCModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_systemc_SystemCModel__avm_systemc_SystemCModel", None)
        self.__avm_systemc_SystemCModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SystemCPort"):
                    opp_val = getattr(item, "SystemCPort", None)
                    
                    if opp_val == self:
                        setattr(item, "SystemCPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SystemCPort"):
                    opp_val = getattr(item, "SystemCPort", None)
                    
                    setattr(item, "SystemCPort", self)
                    

class avm_eda_CircuitLayout(DomainModel):

    def __init__(self, BoundingBoxes: str):
        self.BoundingBoxes = BoundingBoxes
        
    @property
    def BoundingBoxes(self) -> str:
        return self.__BoundingBoxes

    @BoundingBoxes.setter
    def BoundingBoxes(self, BoundingBoxes: str):
        self.__BoundingBoxes = BoundingBoxes

class avm_adamsCar_AdamsCarModel(DomainModel):

    pass
class avm_cyber_CyberModel(DomainModel):

    def __init__(self, Type: str, Class: str, Locator: str, avm_cyber_CyberModel: set["Connector"] = None, avm_cyber_CyberModel254: set["Parameter"] = None):
        self.Type = Type
        self.Class = Class
        self.Locator = Locator
        self.avm_cyber_CyberModel = avm_cyber_CyberModel if avm_cyber_CyberModel is not None else set()
        self.avm_cyber_CyberModel254 = avm_cyber_CyberModel254 if avm_cyber_CyberModel254 is not None else set()
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

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
    def avm_cyber_CyberModel254(self):
        return self.__avm_cyber_CyberModel254

    @avm_cyber_CyberModel254.setter
    def avm_cyber_CyberModel254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_cyber_CyberModel__avm_cyber_CyberModel254", None)
        self.__avm_cyber_CyberModel254 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter255"):
                    opp_val = getattr(item, "Parameter255", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter255", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter255"):
                    opp_val = getattr(item, "Parameter255", None)
                    
                    setattr(item, "Parameter255", self)
                    

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
                if hasattr(item, "Connector252"):
                    opp_val = getattr(item, "Connector252", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector252", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector252"):
                    opp_val = getattr(item, "Connector252", None)
                    
                    setattr(item, "Connector252", self)
                    

class avm_schematic_SchematicModel(DomainModel):

    pass
class avm_modelica_ModelicaModel(DomainModel):

    def __init__(self, Class: str, avm_modelica_ModelicaModel: set["Parameter"] = None, avm_modelica_ModelicaModel155: set["Connector"] = None, avm_modelica_ModelicaModel157: set["Metric"] = None, avm_modelica_ModelicaModel159: set["Limit"] = None, avm_modelica_ModelicaModel161: set["Redeclare"] = None):
        self.Class = Class
        self.avm_modelica_ModelicaModel = avm_modelica_ModelicaModel if avm_modelica_ModelicaModel is not None else set()
        self.avm_modelica_ModelicaModel155 = avm_modelica_ModelicaModel155 if avm_modelica_ModelicaModel155 is not None else set()
        self.avm_modelica_ModelicaModel157 = avm_modelica_ModelicaModel157 if avm_modelica_ModelicaModel157 is not None else set()
        self.avm_modelica_ModelicaModel159 = avm_modelica_ModelicaModel159 if avm_modelica_ModelicaModel159 is not None else set()
        self.avm_modelica_ModelicaModel161 = avm_modelica_ModelicaModel161 if avm_modelica_ModelicaModel161 is not None else set()
        
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
    def avm_modelica_ModelicaModel157(self):
        return self.__avm_modelica_ModelicaModel157

    @avm_modelica_ModelicaModel157.setter
    def avm_modelica_ModelicaModel157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel157", None)
        self.__avm_modelica_ModelicaModel157 = value if value is not None else set()
        
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
    def avm_modelica_ModelicaModel161(self):
        return self.__avm_modelica_ModelicaModel161

    @avm_modelica_ModelicaModel161.setter
    def avm_modelica_ModelicaModel161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel161", None)
        self.__avm_modelica_ModelicaModel161 = value if value is not None else set()
        
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
    def avm_modelica_ModelicaModel155(self):
        return self.__avm_modelica_ModelicaModel155

    @avm_modelica_ModelicaModel155.setter
    def avm_modelica_ModelicaModel155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel155", None)
        self.__avm_modelica_ModelicaModel155 = value if value is not None else set()
        
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
    def avm_modelica_ModelicaModel159(self):
        return self.__avm_modelica_ModelicaModel159

    @avm_modelica_ModelicaModel159.setter
    def avm_modelica_ModelicaModel159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_modelica_ModelicaModel__avm_modelica_ModelicaModel159", None)
        self.__avm_modelica_ModelicaModel159 = value if value is not None else set()
        
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
                    

class WorkflowTaskBase:

    pass
class avm_ExecutionTask(WorkflowTaskBase):

    def __init__(self, Description: str, Invocation: str):
        self.Description = Description
        self.Invocation = Invocation
        
    @property
    def Invocation(self) -> str:
        return self.__Invocation

    @Invocation.setter
    def Invocation(self, Invocation: str):
        self.__Invocation = Invocation

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

class avm_InterpreterTask(WorkflowTaskBase):

    def __init__(self, COMName: str, Parameters: str):
        self.COMName = COMName
        self.Parameters = Parameters
        
    @property
    def Parameters(self) -> str:
        return self.__Parameters

    @Parameters.setter
    def Parameters(self, Parameters: str):
        self.__Parameters = Parameters

    @property
    def COMName(self) -> str:
        return self.__COMName

    @COMName.setter
    def COMName(self, COMName: str):
        self.__COMName = COMName

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
            if hasattr(old_value, "avm_Workflow149"):
                opp_val = getattr(old_value, "avm_Workflow149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Workflow149"):
                opp_val = getattr(value, "avm_Workflow149", None)
                if opp_val is None:
                    setattr(value, "avm_Workflow149", set([self]))
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
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
            if hasattr(old_value, "avm_Value147"):
                opp_val = getattr(old_value, "avm_Value147", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value147", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value147"):
                opp_val = getattr(value, "avm_Value147", None)
                setattr(value, "avm_Value147", self)

class Formula:

    pass
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
                if hasattr(item, "avm_ValueNode124"):
                    opp_val = getattr(item, "avm_ValueNode124", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ValueNode124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ValueNode124"):
                    opp_val = getattr(item, "avm_ValueNode124", None)
                    
                    setattr(item, "avm_ValueNode124", self)
                    

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

class TestBenchValueBase:

    pass
class ContainerInstanceBase:

    pass
class avm_Settings(ABC):

    pass
class avm_Workflow:

    def __init__(self, Name: str, avm_Workflow: "avm_TestBench" = None, avm_Workflow149: set["avm_WorkflowTaskBase"] = None):
        self.Name = Name
        self.avm_Workflow = avm_Workflow
        self.avm_Workflow149 = avm_Workflow149 if avm_Workflow149 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Workflow149(self):
        return self.__avm_Workflow149

    @avm_Workflow149.setter
    def avm_Workflow149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Workflow__avm_Workflow149", None)
        self.__avm_Workflow149 = value if value is not None else set()
        
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
            if hasattr(old_value, "avm_TestBench140"):
                opp_val = getattr(old_value, "avm_TestBench140", None)
                if opp_val == self:
                    setattr(old_value, "avm_TestBench140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench140"):
                opp_val = getattr(value, "avm_TestBench140", None)
                setattr(value, "avm_TestBench140", self)

class avm_TestInjectionPoint(ContainerInstanceBase):

    pass
class avm_Metric(TestBenchValueBase):

    pass
class avm_Parameter(TestBenchValueBase):

    pass
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

    def __init__(self, Name: str, avm_TestBench: "avm_TopLevelSystemUnderTest" = None, avm_TestBench131: set["avm_Parameter"] = None, avm_TestBench133: set["avm_Metric"] = None, avm_TestBench135: set["avm_TestInjectionPoint"] = None, avm_TestBench137: set["avm_ComponentInstance"] = None, avm_TestBench140: "avm_Workflow" = None, avm_TestBench142: set["avm_Settings"] = None, avm_TestBench144: set["avm_DomainModel"] = None):
        self.Name = Name
        self.avm_TestBench = avm_TestBench
        self.avm_TestBench131 = avm_TestBench131 if avm_TestBench131 is not None else set()
        self.avm_TestBench133 = avm_TestBench133 if avm_TestBench133 is not None else set()
        self.avm_TestBench135 = avm_TestBench135 if avm_TestBench135 is not None else set()
        self.avm_TestBench137 = avm_TestBench137 if avm_TestBench137 is not None else set()
        self.avm_TestBench140 = avm_TestBench140
        self.avm_TestBench142 = avm_TestBench142 if avm_TestBench142 is not None else set()
        self.avm_TestBench144 = avm_TestBench144 if avm_TestBench144 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
    def avm_TestBench133(self):
        return self.__avm_TestBench133

    @avm_TestBench133.setter
    def avm_TestBench133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench133", None)
        self.__avm_TestBench133 = value if value is not None else set()
        
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
                    

    @property
    def avm_TestBench140(self):
        return self.__avm_TestBench140

    @avm_TestBench140.setter
    def avm_TestBench140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench140", None)
        self.__avm_TestBench140 = value
        
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
    def avm_TestBench131(self):
        return self.__avm_TestBench131

    @avm_TestBench131.setter
    def avm_TestBench131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench131", None)
        self.__avm_TestBench131 = value if value is not None else set()
        
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
    def avm_TestBench137(self):
        return self.__avm_TestBench137

    @avm_TestBench137.setter
    def avm_TestBench137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench137", None)
        self.__avm_TestBench137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ComponentInstance138"):
                    opp_val = getattr(item, "avm_ComponentInstance138", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ComponentInstance138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ComponentInstance138"):
                    opp_val = getattr(item, "avm_ComponentInstance138", None)
                    
                    setattr(item, "avm_ComponentInstance138", self)
                    

    @property
    def avm_TestBench142(self):
        return self.__avm_TestBench142

    @avm_TestBench142.setter
    def avm_TestBench142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench142", None)
        self.__avm_TestBench142 = value if value is not None else set()
        
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
    def avm_TestBench135(self):
        return self.__avm_TestBench135

    @avm_TestBench135.setter
    def avm_TestBench135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench135", None)
        self.__avm_TestBench135 = value if value is not None else set()
        
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
    def avm_TestBench144(self):
        return self.__avm_TestBench144

    @avm_TestBench144.setter
    def avm_TestBench144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_TestBench__avm_TestBench144", None)
        self.__avm_TestBench144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DomainModel145"):
                    opp_val = getattr(item, "avm_DomainModel145", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DomainModel145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DomainModel145"):
                    opp_val = getattr(item, "avm_DomainModel145", None)
                    
                    setattr(item, "avm_DomainModel145", self)
                    

class avm_Operand:

    def __init__(self, Symbol: str, avm_Operand: "avm_ComplexFormula" = None, avm_Operand127: "avm_ValueNode" = None):
        self.Symbol = Symbol
        self.avm_Operand = avm_Operand
        self.avm_Operand127 = avm_Operand127
        
    @property
    def Symbol(self) -> str:
        return self.__Symbol

    @Symbol.setter
    def Symbol(self, Symbol: str):
        self.__Symbol = Symbol

    @property
    def avm_Operand127(self):
        return self.__avm_Operand127

    @avm_Operand127.setter
    def avm_Operand127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Operand__avm_Operand127", None)
        self.__avm_Operand127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ValueNode128"):
                opp_val = getattr(old_value, "avm_ValueNode128", None)
                if opp_val == self:
                    setattr(old_value, "avm_ValueNode128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ValueNode128"):
                opp_val = getattr(value, "avm_ValueNode128", None)
                setattr(value, "avm_ValueNode128", self)

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
                    

class Container:

    pass
class avm_Compound(Container):

    pass
class avm_ConnectorCompositionTarget:

    def __init__(self, ID: str, avm_ConnectorCompositionTarget: "avm_ConnectorCompositionTarget" = None, avm_ConnectorCompositionTarget118: set["avm_ConnectorCompositionTarget"] = None, avm_ConnectorCompositionTarget121: set["avm_assemblyDetail"] = None):
        self.ID = ID
        self.avm_ConnectorCompositionTarget = avm_ConnectorCompositionTarget
        self.avm_ConnectorCompositionTarget118 = avm_ConnectorCompositionTarget118 if avm_ConnectorCompositionTarget118 is not None else set()
        self.avm_ConnectorCompositionTarget121 = avm_ConnectorCompositionTarget121 if avm_ConnectorCompositionTarget121 is not None else set()
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_ConnectorCompositionTarget121(self):
        return self.__avm_ConnectorCompositionTarget121

    @avm_ConnectorCompositionTarget121.setter
    def avm_ConnectorCompositionTarget121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget121", None)
        self.__avm_ConnectorCompositionTarget121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_assemblyDetail122"):
                    opp_val = getattr(item, "avm_assemblyDetail122", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_assemblyDetail122", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_assemblyDetail122"):
                    opp_val = getattr(item, "avm_assemblyDetail122", None)
                    
                    setattr(item, "avm_assemblyDetail122", self)
                    

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
            if hasattr(old_value, "avm_ConnectorCompositionTarget118"):
                opp_val = getattr(old_value, "avm_ConnectorCompositionTarget118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ConnectorCompositionTarget118"):
                opp_val = getattr(value, "avm_ConnectorCompositionTarget118", None)
                if opp_val is None:
                    setattr(value, "avm_ConnectorCompositionTarget118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ConnectorCompositionTarget118(self):
        return self.__avm_ConnectorCompositionTarget118

    @avm_ConnectorCompositionTarget118.setter
    def avm_ConnectorCompositionTarget118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ConnectorCompositionTarget__avm_ConnectorCompositionTarget118", None)
        self.__avm_ConnectorCompositionTarget118 = value if value is not None else set()
        
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
                    

class avm_PortMapTarget:

    def __init__(self, ID: str, avm_PortMapTarget: "avm_PortMapTarget" = None, avm_PortMapTarget116: set["avm_PortMapTarget"] = None):
        self.ID = ID
        self.avm_PortMapTarget = avm_PortMapTarget
        self.avm_PortMapTarget116 = avm_PortMapTarget116 if avm_PortMapTarget116 is not None else set()
        
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
            if hasattr(old_value, "avm_PortMapTarget116"):
                opp_val = getattr(old_value, "avm_PortMapTarget116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_PortMapTarget116"):
                opp_val = getattr(value, "avm_PortMapTarget116", None)
                if opp_val is None:
                    setattr(value, "avm_PortMapTarget116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_PortMapTarget116(self):
        return self.__avm_PortMapTarget116

    @avm_PortMapTarget116.setter
    def avm_PortMapTarget116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_PortMapTarget__avm_PortMapTarget116", None)
        self.__avm_PortMapTarget116 = value if value is not None else set()
        
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

    def __init__(self, IDinComponentModel: str, avm_ComponentPrimitivePropertyInstance: "avm_ComponentInstance" = None, avm_ComponentPrimitivePropertyInstance114: "avm_Value" = None):
        self.IDinComponentModel = IDinComponentModel
        self.avm_ComponentPrimitivePropertyInstance = avm_ComponentPrimitivePropertyInstance
        self.avm_ComponentPrimitivePropertyInstance114 = avm_ComponentPrimitivePropertyInstance114
        
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
            if hasattr(old_value, "avm_ComponentInstance110"):
                opp_val = getattr(old_value, "avm_ComponentInstance110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance110"):
                opp_val = getattr(value, "avm_ComponentInstance110", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ComponentPrimitivePropertyInstance114(self):
        return self.__avm_ComponentPrimitivePropertyInstance114

    @avm_ComponentPrimitivePropertyInstance114.setter
    def avm_ComponentPrimitivePropertyInstance114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentPrimitivePropertyInstance__avm_ComponentPrimitivePropertyInstance114", None)
        self.__avm_ComponentPrimitivePropertyInstance114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Value115"):
                opp_val = getattr(old_value, "avm_Value115", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value115"):
                opp_val = getattr(value, "avm_Value115", None)
                setattr(value, "avm_Value115", self)

class DesignSpaceContainer:

    pass
class avm_Alternative(DesignSpaceContainer):

    pass
class avm_Optional(DesignSpaceContainer):

    pass
class avm_ComponentInstance:

    def __init__(self, ComponentID: str, ID: str, Name: str, DesignSpaceSrcComponentID: str, XPosition: str, YPosition: str, avm_ComponentInstance: "avm_Container" = None, avm_ComponentInstance108: set["avm_ComponentPortInstance"] = None, avm_ComponentInstance110: set["avm_ComponentPrimitivePropertyInstance"] = None, avm_ComponentInstance112: set["avm_ComponentConnectorInstance"] = None, avm_ComponentInstance138: "avm_TestBench" = None):
        self.ComponentID = ComponentID
        self.ID = ID
        self.Name = Name
        self.DesignSpaceSrcComponentID = DesignSpaceSrcComponentID
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_ComponentInstance = avm_ComponentInstance
        self.avm_ComponentInstance108 = avm_ComponentInstance108 if avm_ComponentInstance108 is not None else set()
        self.avm_ComponentInstance110 = avm_ComponentInstance110 if avm_ComponentInstance110 is not None else set()
        self.avm_ComponentInstance112 = avm_ComponentInstance112 if avm_ComponentInstance112 is not None else set()
        self.avm_ComponentInstance138 = avm_ComponentInstance138
        
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
    def ComponentID(self) -> str:
        return self.__ComponentID

    @ComponentID.setter
    def ComponentID(self, ComponentID: str):
        self.__ComponentID = ComponentID

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
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_ComponentInstance110(self):
        return self.__avm_ComponentInstance110

    @avm_ComponentInstance110.setter
    def avm_ComponentInstance110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance110", None)
        self.__avm_ComponentInstance110 = value if value is not None else set()
        
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
                    

    @property
    def avm_ComponentInstance138(self):
        return self.__avm_ComponentInstance138

    @avm_ComponentInstance138.setter
    def avm_ComponentInstance138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance138", None)
        self.__avm_ComponentInstance138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench137"):
                opp_val = getattr(old_value, "avm_TestBench137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench137"):
                opp_val = getattr(value, "avm_TestBench137", None)
                if opp_val is None:
                    setattr(value, "avm_TestBench137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ComponentInstance112(self):
        return self.__avm_ComponentInstance112

    @avm_ComponentInstance112.setter
    def avm_ComponentInstance112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance112", None)
        self.__avm_ComponentInstance112 = value if value is not None else set()
        
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
    def avm_ComponentInstance(self):
        return self.__avm_ComponentInstance

    @avm_ComponentInstance.setter
    def avm_ComponentInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance", None)
        self.__avm_ComponentInstance = value
        
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
    def avm_ComponentInstance108(self):
        return self.__avm_ComponentInstance108

    @avm_ComponentInstance108.setter
    def avm_ComponentInstance108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ComponentInstance__avm_ComponentInstance108", None)
        self.__avm_ComponentInstance108 = value if value is not None else set()
        
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
                    

class avm_DesignDomainFeature(ABC):

    pass
class avm_Container(ABC):

    def __init__(self, YPosition: str, XPosition: str, Name: str, ID: str, Description: str, Classifications: str, avm_Container87: set["avm_Connector"] = None, avm_Container90: set["avm_assemblyDetail"] = None, avm_Container93: set["avm_Formula"] = None, avm_Container96: set["avm_ContainerFeature"] = None, avm_Container: "avm_Design" = None, avm_Container77: "avm_Container" = None, avm_Container75: set["avm_Container"] = None, avm_Container79: set["avm_Property"] = None, avm_Container82: set["avm_ComponentInstance"] = None, avm_Container84: set["avm_Port"] = None, avm_Container98: set["avm_Resource"] = None, avm_Container101: set["avm_DomainModel"] = None, avm_Container104: set["avm_Resource"] = None):
        self.YPosition = YPosition
        self.XPosition = XPosition
        self.Name = Name
        self.ID = ID
        self.Description = Description
        self.Classifications = Classifications
        self.avm_Container87 = avm_Container87 if avm_Container87 is not None else set()
        self.avm_Container90 = avm_Container90 if avm_Container90 is not None else set()
        self.avm_Container93 = avm_Container93 if avm_Container93 is not None else set()
        self.avm_Container96 = avm_Container96 if avm_Container96 is not None else set()
        self.avm_Container = avm_Container
        self.avm_Container77 = avm_Container77
        self.avm_Container75 = avm_Container75 if avm_Container75 is not None else set()
        self.avm_Container79 = avm_Container79 if avm_Container79 is not None else set()
        self.avm_Container82 = avm_Container82 if avm_Container82 is not None else set()
        self.avm_Container84 = avm_Container84 if avm_Container84 is not None else set()
        self.avm_Container98 = avm_Container98 if avm_Container98 is not None else set()
        self.avm_Container101 = avm_Container101 if avm_Container101 is not None else set()
        self.avm_Container104 = avm_Container104 if avm_Container104 is not None else set()
        
    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

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
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Classifications(self) -> str:
        return self.__Classifications

    @Classifications.setter
    def Classifications(self, Classifications: str):
        self.__Classifications = Classifications

    @property
    def avm_Container75(self):
        return self.__avm_Container75

    @avm_Container75.setter
    def avm_Container75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container75", None)
        self.__avm_Container75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Container77"):
                    opp_val = getattr(item, "avm_Container77", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Container77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Container77"):
                    opp_val = getattr(item, "avm_Container77", None)
                    
                    setattr(item, "avm_Container77", self)
                    

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
                if hasattr(item, "avm_Property80"):
                    opp_val = getattr(item, "avm_Property80", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Property80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Property80"):
                    opp_val = getattr(item, "avm_Property80", None)
                    
                    setattr(item, "avm_Property80", self)
                    

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
                    

    @property
    def avm_Container84(self):
        return self.__avm_Container84

    @avm_Container84.setter
    def avm_Container84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container84", None)
        self.__avm_Container84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Port85"):
                    opp_val = getattr(item, "avm_Port85", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Port85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Port85"):
                    opp_val = getattr(item, "avm_Port85", None)
                    
                    setattr(item, "avm_Port85", self)
                    

    @property
    def avm_Container87(self):
        return self.__avm_Container87

    @avm_Container87.setter
    def avm_Container87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container87", None)
        self.__avm_Container87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Connector88"):
                    opp_val = getattr(item, "avm_Connector88", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Connector88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Connector88"):
                    opp_val = getattr(item, "avm_Connector88", None)
                    
                    setattr(item, "avm_Connector88", self)
                    

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
    def avm_Container104(self):
        return self.__avm_Container104

    @avm_Container104.setter
    def avm_Container104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container104", None)
        self.__avm_Container104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource105"):
                    opp_val = getattr(item, "avm_Resource105", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource105"):
                    opp_val = getattr(item, "avm_Resource105", None)
                    
                    setattr(item, "avm_Resource105", self)
                    

    @property
    def avm_Container77(self):
        return self.__avm_Container77

    @avm_Container77.setter
    def avm_Container77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container77", None)
        self.__avm_Container77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container75"):
                opp_val = getattr(old_value, "avm_Container75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container75"):
                opp_val = getattr(value, "avm_Container75", None)
                if opp_val is None:
                    setattr(value, "avm_Container75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Container98(self):
        return self.__avm_Container98

    @avm_Container98.setter
    def avm_Container98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container98", None)
        self.__avm_Container98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource99"):
                    opp_val = getattr(item, "avm_Resource99", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource99"):
                    opp_val = getattr(item, "avm_Resource99", None)
                    
                    setattr(item, "avm_Resource99", self)
                    

    @property
    def avm_Container96(self):
        return self.__avm_Container96

    @avm_Container96.setter
    def avm_Container96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container96", None)
        self.__avm_Container96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_ContainerFeature"):
                    opp_val = getattr(item, "avm_ContainerFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_ContainerFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_ContainerFeature"):
                    opp_val = getattr(item, "avm_ContainerFeature", None)
                    
                    setattr(item, "avm_ContainerFeature", self)
                    

    @property
    def avm_Container93(self):
        return self.__avm_Container93

    @avm_Container93.setter
    def avm_Container93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container93", None)
        self.__avm_Container93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Formula94"):
                    opp_val = getattr(item, "avm_Formula94", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Formula94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Formula94"):
                    opp_val = getattr(item, "avm_Formula94", None)
                    
                    setattr(item, "avm_Formula94", self)
                    

    @property
    def avm_Container101(self):
        return self.__avm_Container101

    @avm_Container101.setter
    def avm_Container101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container101", None)
        self.__avm_Container101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DomainModel102"):
                    opp_val = getattr(item, "avm_DomainModel102", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DomainModel102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DomainModel102"):
                    opp_val = getattr(item, "avm_DomainModel102", None)
                    
                    setattr(item, "avm_DomainModel102", self)
                    

    @property
    def avm_Container90(self):
        return self.__avm_Container90

    @avm_Container90.setter
    def avm_Container90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Container__avm_Container90", None)
        self.__avm_Container90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_assemblyDetail91"):
                    opp_val = getattr(item, "avm_assemblyDetail91", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_assemblyDetail91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_assemblyDetail91"):
                    opp_val = getattr(item, "avm_assemblyDetail91", None)
                    
                    setattr(item, "avm_assemblyDetail91", self)
                    

class avm_Design:

    def __init__(self, SchemaVersion: str, DesignID: str, Name: str, DesignSpaceSrcID: str, avm_Design: "avm_Container" = None, avm_Design71: set["avm_DesignDomainFeature"] = None, avm_Design73: set["avm_Resource"] = None):
        self.SchemaVersion = SchemaVersion
        self.DesignID = DesignID
        self.Name = Name
        self.DesignSpaceSrcID = DesignSpaceSrcID
        self.avm_Design = avm_Design
        self.avm_Design71 = avm_Design71 if avm_Design71 is not None else set()
        self.avm_Design73 = avm_Design73 if avm_Design73 is not None else set()
        
    @property
    def SchemaVersion(self) -> str:
        return self.__SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion: str):
        self.__SchemaVersion = SchemaVersion

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
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def avm_Design73(self):
        return self.__avm_Design73

    @avm_Design73.setter
    def avm_Design73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Design__avm_Design73", None)
        self.__avm_Design73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource74"):
                    opp_val = getattr(item, "avm_Resource74", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource74"):
                    opp_val = getattr(item, "avm_Resource74", None)
                    
                    setattr(item, "avm_Resource74", self)
                    

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

    @property
    def avm_Design71(self):
        return self.__avm_Design71

    @avm_Design71.setter
    def avm_Design71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Design__avm_Design71", None)
        self.__avm_Design71 = value if value is not None else set()
        
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
                    

class avm_ContainerFeature(ABC):

    pass
class avm_DomainModelMetric(ABC):

    def __init__(self, ID: str, Notes: str, XPosition: str, YPosition: str, avm_DomainModelMetric: "avm_Value" = None):
        self.ID = ID
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_DomainModelMetric = avm_DomainModelMetric
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

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
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

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
            if hasattr(old_value, "avm_Value54"):
                opp_val = getattr(old_value, "avm_Value54", None)
                if opp_val == self:
                    setattr(old_value, "avm_Value54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value54"):
                opp_val = getattr(value, "avm_Value54", None)
                setattr(value, "avm_Value54", self)

class DistributionRestriction:

    pass
class avm_Proprietary(DistributionRestriction):

    def __init__(self, Organization: str):
        self.Organization = Organization
        
    @property
    def Organization(self) -> str:
        return self.__Organization

    @Organization.setter
    def Organization(self, Organization: str):
        self.__Organization = Organization

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

class avm_SecurityClassification(DistributionRestriction):

    def __init__(self, Level: str):
        self.Level = Level
        
    @property
    def Level(self) -> str:
        return self.__Level

    @Level.setter
    def Level(self, Level: str):
        self.__Level = Level

class ProbabilisticValue:

    pass
class avm_UniformDistribution(ProbabilisticValue):

    pass
class avm_NormalDistribution(ProbabilisticValue):

    pass
class Property:

    pass
class avm_CompoundProperty(Property):

    pass
class avm_PrimitiveProperty(Property):

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
            if hasattr(old_value, "avm_ComponentInstance112"):
                opp_val = getattr(old_value, "avm_ComponentInstance112", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance112"):
                opp_val = getattr(value, "avm_ComponentInstance112", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance112", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_ValueNode(ABC):

    def __init__(self, ID: str, avm_ValueNode: "avm_DerivedValue" = None, avm_ValueNode124: "avm_SimpleFormula" = None, avm_ValueNode128: "avm_Operand" = None, avm_ValueNode152: "avm_ValueFlowMux" = None):
        self.ID = ID
        self.avm_ValueNode = avm_ValueNode
        self.avm_ValueNode124 = avm_ValueNode124
        self.avm_ValueNode128 = avm_ValueNode128
        self.avm_ValueNode152 = avm_ValueNode152
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_ValueNode124(self):
        return self.__avm_ValueNode124

    @avm_ValueNode124.setter
    def avm_ValueNode124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode124", None)
        self.__avm_ValueNode124 = value
        
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
    def avm_ValueNode152(self):
        return self.__avm_ValueNode152

    @avm_ValueNode152.setter
    def avm_ValueNode152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode152", None)
        self.__avm_ValueNode152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ValueFlowMux151"):
                opp_val = getattr(old_value, "avm_ValueFlowMux151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ValueFlowMux151"):
                opp_val = getattr(value, "avm_ValueFlowMux151", None)
                if opp_val is None:
                    setattr(value, "avm_ValueFlowMux151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_ValueNode128(self):
        return self.__avm_ValueNode128

    @avm_ValueNode128.setter
    def avm_ValueNode128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_ValueNode__avm_ValueNode128", None)
        self.__avm_ValueNode128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Operand127"):
                opp_val = getattr(old_value, "avm_Operand127", None)
                if opp_val == self:
                    setattr(old_value, "avm_Operand127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Operand127"):
                opp_val = getattr(value, "avm_Operand127", None)
                setattr(value, "avm_Operand127", self)

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
class avm_ParametricEnumeratedValue(ValueExpressionType):

    pass
class avm_ParametricValue(ValueExpressionType):

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

class avm_DomainModelParameter(ABC):

    def __init__(self, Notes: str, XPosition: str, YPosition: str):
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        
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
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

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
            if hasattr(old_value, "avm_ComponentInstance108"):
                opp_val = getattr(old_value, "avm_ComponentInstance108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentInstance108"):
                opp_val = getattr(value, "avm_ComponentInstance108", None)
                if opp_val is None:
                    setattr(value, "avm_ComponentInstance108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_ConnectorFeature(ABC):

    pass
class avm_DomainMapping(ABC):

    pass
class avm_AnalysisConstruct(ABC):

    pass
class avm_Port(PortMapTarget):

    def __init__(self, Notes: str, XPosition: str, Definition: str, YPosition: str, Name: str, avm_Port: "avm_Component" = None, avm_Port26: "avm_Connector" = None, avm_Port85: "avm_Container" = None):
        self.Notes = Notes
        self.XPosition = XPosition
        self.Definition = Definition
        self.YPosition = YPosition
        self.Name = Name
        self.avm_Port = avm_Port
        self.avm_Port26 = avm_Port26
        self.avm_Port85 = avm_Port85
        
    @property
    def Definition(self) -> str:
        return self.__Definition

    @Definition.setter
    def Definition(self, Definition: str):
        self.__Definition = Definition

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def YPosition(self) -> str:
        return self.__YPosition

    @YPosition.setter
    def YPosition(self, YPosition: str):
        self.__YPosition = YPosition

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
    def avm_Port85(self):
        return self.__avm_Port85

    @avm_Port85.setter
    def avm_Port85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Port__avm_Port85", None)
        self.__avm_Port85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container84"):
                opp_val = getattr(old_value, "avm_Container84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container84"):
                opp_val = getattr(value, "avm_Container84", None)
                if opp_val is None:
                    setattr(value, "avm_Container84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Port26(self):
        return self.__avm_Port26

    @avm_Port26.setter
    def avm_Port26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Port__avm_Port26", None)
        self.__avm_Port26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector25"):
                opp_val = getattr(old_value, "avm_Connector25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector25"):
                opp_val = getattr(value, "avm_Connector25", None)
                if opp_val is None:
                    setattr(value, "avm_Connector25", set([self]))
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

    def __init__(self, Definition: str, Name: str, Notes: str, XPosition: str, YPosition: str, avm_Connector: "avm_Component" = None, avm_Connector36: set["avm_ConnectorFeature"] = None, avm_Connector25: set["avm_Port"] = None, avm_Connector28: set["avm_Property"] = None, avm_Connector31: set["avm_assemblyDetail"] = None, avm_Connector34: "avm_Connector" = None, avm_Connector32: set["avm_Connector"] = None, avm_Connector88: "avm_Container" = None):
        self.Definition = Definition
        self.Name = Name
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Connector = avm_Connector
        self.avm_Connector36 = avm_Connector36 if avm_Connector36 is not None else set()
        self.avm_Connector25 = avm_Connector25 if avm_Connector25 is not None else set()
        self.avm_Connector28 = avm_Connector28 if avm_Connector28 is not None else set()
        self.avm_Connector31 = avm_Connector31 if avm_Connector31 is not None else set()
        self.avm_Connector34 = avm_Connector34
        self.avm_Connector32 = avm_Connector32 if avm_Connector32 is not None else set()
        self.avm_Connector88 = avm_Connector88
        
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
    def avm_Connector32(self):
        return self.__avm_Connector32

    @avm_Connector32.setter
    def avm_Connector32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector32", None)
        self.__avm_Connector32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Connector34"):
                    opp_val = getattr(item, "avm_Connector34", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Connector34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Connector34"):
                    opp_val = getattr(item, "avm_Connector34", None)
                    
                    setattr(item, "avm_Connector34", self)
                    

    @property
    def avm_Connector31(self):
        return self.__avm_Connector31

    @avm_Connector31.setter
    def avm_Connector31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector31", None)
        self.__avm_Connector31 = value if value is not None else set()
        
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
    def avm_Connector28(self):
        return self.__avm_Connector28

    @avm_Connector28.setter
    def avm_Connector28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector28", None)
        self.__avm_Connector28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Property29"):
                    opp_val = getattr(item, "avm_Property29", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Property29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Property29"):
                    opp_val = getattr(item, "avm_Property29", None)
                    
                    setattr(item, "avm_Property29", self)
                    

    @property
    def avm_Connector25(self):
        return self.__avm_Connector25

    @avm_Connector25.setter
    def avm_Connector25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector25", None)
        self.__avm_Connector25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Port26"):
                    opp_val = getattr(item, "avm_Port26", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Port26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Port26"):
                    opp_val = getattr(item, "avm_Port26", None)
                    
                    setattr(item, "avm_Port26", self)
                    

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

    @property
    def avm_Connector36(self):
        return self.__avm_Connector36

    @avm_Connector36.setter
    def avm_Connector36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector36", None)
        self.__avm_Connector36 = value if value is not None else set()
        
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
    def avm_Connector88(self):
        return self.__avm_Connector88

    @avm_Connector88.setter
    def avm_Connector88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector88", None)
        self.__avm_Connector88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container87"):
                opp_val = getattr(old_value, "avm_Container87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container87"):
                opp_val = getattr(value, "avm_Container87", None)
                if opp_val is None:
                    setattr(value, "avm_Container87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Connector34(self):
        return self.__avm_Connector34

    @avm_Connector34.setter
    def avm_Connector34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Connector__avm_Connector34", None)
        self.__avm_Connector34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector32"):
                opp_val = getattr(old_value, "avm_Connector32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector32"):
                opp_val = getattr(value, "avm_Connector32", None)
                if opp_val is None:
                    setattr(value, "avm_Connector32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Resource:

    def __init__(self, Name: str, Path: str, Hash: str, ID: str, Notes: str, XPosition: str, YPosition: str, avm_Resource: "avm_Component" = None, avm_Resource19: "avm_DomainModel" = None, avm_Resource68: "avm_DataSource" = None, avm_Resource74: "avm_Design" = None, avm_Resource99: "avm_Container" = None, avm_Resource105: "avm_Container" = None):
        self.Name = Name
        self.Path = Path
        self.Hash = Hash
        self.ID = ID
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Resource = avm_Resource
        self.avm_Resource19 = avm_Resource19
        self.avm_Resource68 = avm_Resource68
        self.avm_Resource74 = avm_Resource74
        self.avm_Resource99 = avm_Resource99
        self.avm_Resource105 = avm_Resource105
        
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
    def Hash(self) -> str:
        return self.__Hash

    @Hash.setter
    def Hash(self, Hash: str):
        self.__Hash = Hash

    @property
    def Path(self) -> str:
        return self.__Path

    @Path.setter
    def Path(self, Path: str):
        self.__Path = Path

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_Resource68(self):
        return self.__avm_Resource68

    @avm_Resource68.setter
    def avm_Resource68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource68", None)
        self.__avm_Resource68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DataSource67"):
                opp_val = getattr(old_value, "avm_DataSource67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DataSource67"):
                opp_val = getattr(value, "avm_DataSource67", None)
                if opp_val is None:
                    setattr(value, "avm_DataSource67", set([self]))
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

    @property
    def avm_Resource105(self):
        return self.__avm_Resource105

    @avm_Resource105.setter
    def avm_Resource105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource105", None)
        self.__avm_Resource105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container104"):
                opp_val = getattr(old_value, "avm_Container104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container104"):
                opp_val = getattr(value, "avm_Container104", None)
                if opp_val is None:
                    setattr(value, "avm_Container104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Resource99(self):
        return self.__avm_Resource99

    @avm_Resource99.setter
    def avm_Resource99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource99", None)
        self.__avm_Resource99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container98"):
                opp_val = getattr(old_value, "avm_Container98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container98"):
                opp_val = getattr(value, "avm_Container98", None)
                if opp_val is None:
                    setattr(value, "avm_Container98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Resource74(self):
        return self.__avm_Resource74

    @avm_Resource74.setter
    def avm_Resource74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource74", None)
        self.__avm_Resource74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Design73"):
                opp_val = getattr(old_value, "avm_Design73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Design73"):
                opp_val = getattr(value, "avm_Design73", None)
                if opp_val is None:
                    setattr(value, "avm_Design73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_Resource19(self):
        return self.__avm_Resource19

    @avm_Resource19.setter
    def avm_Resource19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Resource__avm_Resource19", None)
        self.__avm_Resource19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_DomainModel18"):
                opp_val = getattr(old_value, "avm_DomainModel18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_DomainModel18"):
                opp_val = getattr(value, "avm_DomainModel18", None)
                if opp_val is None:
                    setattr(value, "avm_DomainModel18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_Property(ABC):

    def __init__(self, Notes: str, Definition: str, ID: str, XPosition: str, YPosition: str, Name: str, OnDataSheet: str, avm_Property: "avm_Component" = None, avm_Property29: "avm_Connector" = None, avm_Property80: "avm_Container" = None):
        self.Notes = Notes
        self.Definition = Definition
        self.ID = ID
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.Name = Name
        self.OnDataSheet = OnDataSheet
        self.avm_Property = avm_Property
        self.avm_Property29 = avm_Property29
        self.avm_Property80 = avm_Property80
        
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
    def Definition(self) -> str:
        return self.__Definition

    @Definition.setter
    def Definition(self, Definition: str):
        self.__Definition = Definition

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
    def OnDataSheet(self) -> str:
        return self.__OnDataSheet

    @OnDataSheet.setter
    def OnDataSheet(self, OnDataSheet: str):
        self.__OnDataSheet = OnDataSheet

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

    @property
    def avm_Property80(self):
        return self.__avm_Property80

    @avm_Property80.setter
    def avm_Property80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Property__avm_Property80", None)
        self.__avm_Property80 = value
        
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

    @property
    def avm_Property29(self):
        return self.__avm_Property29

    @avm_Property29.setter
    def avm_Property29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Property__avm_Property29", None)
        self.__avm_Property29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Connector28"):
                opp_val = getattr(old_value, "avm_Connector28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Connector28"):
                opp_val = getattr(value, "avm_Connector28", None)
                if opp_val is None:
                    setattr(value, "avm_Connector28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_DomainModel(ABC):

    def __init__(self, Author: str, Notes: str, XPosition: str, YPosition: str, Name: str, ID: str, avm_DomainModel: "avm_Component" = None, avm_DomainModel18: set["avm_Resource"] = None, avm_DomainModel102: "avm_Container" = None, avm_DomainModel145: "avm_TestBench" = None):
        self.Author = Author
        self.Notes = Notes
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.Name = Name
        self.ID = ID
        self.avm_DomainModel = avm_DomainModel
        self.avm_DomainModel18 = avm_DomainModel18 if avm_DomainModel18 is not None else set()
        self.avm_DomainModel102 = avm_DomainModel102
        self.avm_DomainModel145 = avm_DomainModel145
        
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
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def avm_DomainModel18(self):
        return self.__avm_DomainModel18

    @avm_DomainModel18.setter
    def avm_DomainModel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel18", None)
        self.__avm_DomainModel18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource19"):
                    opp_val = getattr(item, "avm_Resource19", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource19"):
                    opp_val = getattr(item, "avm_Resource19", None)
                    
                    setattr(item, "avm_Resource19", self)
                    

    @property
    def avm_DomainModel145(self):
        return self.__avm_DomainModel145

    @avm_DomainModel145.setter
    def avm_DomainModel145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel145", None)
        self.__avm_DomainModel145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_TestBench144"):
                opp_val = getattr(old_value, "avm_TestBench144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_TestBench144"):
                opp_val = getattr(value, "avm_TestBench144", None)
                if opp_val is None:
                    setattr(value, "avm_TestBench144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def avm_DomainModel102(self):
        return self.__avm_DomainModel102

    @avm_DomainModel102.setter
    def avm_DomainModel102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DomainModel__avm_DomainModel102", None)
        self.__avm_DomainModel102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container101"):
                opp_val = getattr(old_value, "avm_Container101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container101"):
                opp_val = getattr(value, "avm_Container101", None)
                if opp_val is None:
                    setattr(value, "avm_Container101", set([self]))
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

class avm_DataSource:

    def __init__(self, Notes: str, avm_DataSource: "avm_Value" = None, avm_DataSource67: set["avm_Resource"] = None):
        self.Notes = Notes
        self.avm_DataSource = avm_DataSource
        self.avm_DataSource67 = avm_DataSource67 if avm_DataSource67 is not None else set()
        
    @property
    def Notes(self) -> str:
        return self.__Notes

    @Notes.setter
    def Notes(self, Notes: str):
        self.__Notes = Notes

    @property
    def avm_DataSource67(self):
        return self.__avm_DataSource67

    @avm_DataSource67.setter
    def avm_DataSource67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_DataSource__avm_DataSource67", None)
        self.__avm_DataSource67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_Resource68"):
                    opp_val = getattr(item, "avm_Resource68", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_Resource68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_Resource68"):
                    opp_val = getattr(item, "avm_Resource68", None)
                    
                    setattr(item, "avm_Resource68", self)
                    

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
            if hasattr(old_value, "avm_Value22"):
                opp_val = getattr(old_value, "avm_Value22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Value22"):
                opp_val = getattr(value, "avm_Value22", None)
                if opp_val is None:
                    setattr(value, "avm_Value22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_ValueExpressionType(ABC):

    pass
class ValueNode:

    pass
class avm_Formula(ValueNode):

    def __init__(self, Name: str, XPosition: str, YPosition: str, avm_Formula: "avm_Component" = None, avm_Formula94: "avm_Container" = None):
        self.Name = Name
        self.XPosition = XPosition
        self.YPosition = YPosition
        self.avm_Formula = avm_Formula
        self.avm_Formula94 = avm_Formula94
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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

    @property
    def avm_Formula94(self):
        return self.__avm_Formula94

    @avm_Formula94.setter
    def avm_Formula94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Formula__avm_Formula94", None)
        self.__avm_Formula94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_Container93"):
                opp_val = getattr(old_value, "avm_Container93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_Container93"):
                opp_val = getattr(value, "avm_Container93", None)
                if opp_val is None:
                    setattr(value, "avm_Container93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class avm_ValueFlowMux(ValueNode):

    pass
class avm_Value(ValueNode):

    def __init__(self, DimensionType: str, DataType: str, Dimensions: str, Unit: str, avm_Value: "avm_ValueExpressionType" = None, avm_Value22: set["avm_DataSource"] = None, avm_Value56: "avm_PrimitiveProperty" = None, avm_Value54: "avm_DomainModelMetric" = None, avm_Value115: "avm_ComponentPrimitivePropertyInstance" = None, avm_Value147: "avm_TestBenchValueBase" = None):
        self.DimensionType = DimensionType
        self.DataType = DataType
        self.Dimensions = Dimensions
        self.Unit = Unit
        self.avm_Value = avm_Value
        self.avm_Value22 = avm_Value22 if avm_Value22 is not None else set()
        self.avm_Value56 = avm_Value56
        self.avm_Value54 = avm_Value54
        self.avm_Value115 = avm_Value115
        self.avm_Value147 = avm_Value147
        
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
    def DimensionType(self) -> str:
        return self.__DimensionType

    @DimensionType.setter
    def DimensionType(self, DimensionType: str):
        self.__DimensionType = DimensionType

    @property
    def avm_Value115(self):
        return self.__avm_Value115

    @avm_Value115.setter
    def avm_Value115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value115", None)
        self.__avm_Value115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "avm_ComponentPrimitivePropertyInstance114"):
                opp_val = getattr(old_value, "avm_ComponentPrimitivePropertyInstance114", None)
                if opp_val == self:
                    setattr(old_value, "avm_ComponentPrimitivePropertyInstance114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "avm_ComponentPrimitivePropertyInstance114"):
                opp_val = getattr(value, "avm_ComponentPrimitivePropertyInstance114", None)
                setattr(value, "avm_ComponentPrimitivePropertyInstance114", self)

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
    def avm_Value56(self):
        return self.__avm_Value56

    @avm_Value56.setter
    def avm_Value56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value56", None)
        self.__avm_Value56 = value
        
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

    @property
    def avm_Value22(self):
        return self.__avm_Value22

    @avm_Value22.setter
    def avm_Value22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value22", None)
        self.__avm_Value22 = value if value is not None else set()
        
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
    def avm_Value147(self):
        return self.__avm_Value147

    @avm_Value147.setter
    def avm_Value147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Value__avm_Value147", None)
        self.__avm_Value147 = value
        
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

class avm_Component:

    def __init__(self, Name: str, Version: str, SchemaVersion: str, Classifications: str, ID: str, Supercedes: str, avm_Component: set["avm_DomainModel"] = None, avm_Component2: set["avm_Property"] = None, avm_Component4: set["avm_Resource"] = None, avm_Component6: set["avm_Connector"] = None, avm_Component8: set["avm_DistributionRestriction"] = None, avm_Component10: set["avm_Port"] = None, avm_Component12: set["avm_AnalysisConstruct"] = None, avm_Component14: set["avm_Formula"] = None, avm_Component16: set["avm_DomainMapping"] = None):
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
        self.avm_Component12 = avm_Component12 if avm_Component12 is not None else set()
        self.avm_Component14 = avm_Component14 if avm_Component14 is not None else set()
        self.avm_Component16 = avm_Component16 if avm_Component16 is not None else set()
        
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
    def Version(self) -> str:
        return self.__Version

    @Version.setter
    def Version(self, Version: str):
        self.__Version = Version

    @property
    def Supercedes(self) -> str:
        return self.__Supercedes

    @Supercedes.setter
    def Supercedes(self, Supercedes: str):
        self.__Supercedes = Supercedes

    @property
    def SchemaVersion(self) -> str:
        return self.__SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion: str):
        self.__SchemaVersion = SchemaVersion

    @property
    def Classifications(self) -> str:
        return self.__Classifications

    @Classifications.setter
    def Classifications(self, Classifications: str):
        self.__Classifications = Classifications

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
                    

    @property
    def avm_Component16(self):
        return self.__avm_Component16

    @avm_Component16.setter
    def avm_Component16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_avm_Component__avm_Component16", None)
        self.__avm_Component16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "avm_DomainMapping"):
                    opp_val = getattr(item, "avm_DomainMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "avm_DomainMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "avm_DomainMapping"):
                    opp_val = getattr(item, "avm_DomainMapping", None)
                    
                    setattr(item, "avm_DomainMapping", self)
                    

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
                    
