from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Accumulator(Enum):
    sum = "sum"
    maximum = "maximum"
    minimum = "minimum"
    average = "average"
    standardDeviation = "standardDeviation"


############################################
# Definition of Classes
############################################

class BinaryMeasurement:

    pass
class smm_RatioMeasurement(BinaryMeasurement):

    pass
class BinaryMeasure:

    pass
class smm_RatioMeasure(BinaryMeasure):

    pass
class smm_EObject:

    pass
class smm_SmmElement(ABC):

    def __init__(self, name: str, shortDescription: str, description: str, SmmElement: "smm_Observation" = None, smm_SmmElement: set["smm_Attribute"] = None, smm_SmmElement212: set["smm_Annotation"] = None, requestedMeasures: set["smm_Observation"] = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.SmmElement = SmmElement
        self.smm_SmmElement = smm_SmmElement if smm_SmmElement is not None else set()
        self.smm_SmmElement212 = smm_SmmElement212 if smm_SmmElement212 is not None else set()
        self.requestedMeasures = requestedMeasures if requestedMeasures is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smm_SmmElement(self):
        return self.__smm_SmmElement

    @smm_SmmElement.setter
    def smm_SmmElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement", None)
        self.__smm_SmmElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Attribute"):
                    opp_val = getattr(item, "smm_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Attribute"):
                    opp_val = getattr(item, "smm_Attribute", None)
                    
                    setattr(item, "smm_Attribute", self)
                    

    @property
    def requestedMeasures(self):
        return self.__requestedMeasures

    @requestedMeasures.setter
    def requestedMeasures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__requestedMeasures", None)
        self.__requestedMeasures = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Observation"):
                    opp_val = getattr(item, "Observation", None)
                    
                    if opp_val == self:
                        setattr(item, "Observation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Observation"):
                    opp_val = getattr(item, "Observation", None)
                    
                    setattr(item, "Observation", self)
                    

    @property
    def SmmElement(self):
        return self.__SmmElement

    @SmmElement.setter
    def SmmElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__SmmElement", None)
        self.__SmmElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requestedObservations"):
                opp_val = getattr(old_value, "requestedObservations", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requestedObservations"):
                opp_val = getattr(value, "requestedObservations", None)
                if opp_val is None:
                    setattr(value, "requestedObservations", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_SmmElement212(self):
        return self.__smm_SmmElement212

    @smm_SmmElement212.setter
    def smm_SmmElement212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement212", None)
        self.__smm_SmmElement212 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Annotation"):
                    opp_val = getattr(item, "smm_Annotation", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Annotation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Annotation"):
                    opp_val = getattr(item, "smm_Annotation", None)
                    
                    setattr(item, "smm_Annotation", self)
                    

    def getInbound(self) -> SmmRelationship:
        # TODO: Implement getInbound method
        pass

    def getOutbound(self) -> SmmRelationship:
        # TODO: Implement getOutbound method
        pass

class Measure:

    pass
class smm_Ranking(Measure):

    pass
class DirectMeasure:

    pass
class smm_Counting(DirectMeasure):

    pass
class DirectMeasurement:

    pass
class smm_Count(DirectMeasurement):

    pass
class Measurement:

    pass
class smm_Grade(Measurement):

    def __init__(self, isBaseSupplied: bool, value: str, from77: "smm_RankingMeasurementRelationship" = None, smm_Grade: "smm_DimensionalMeasurement" = None, Grade: "smm_RankingMeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.value = value
        self.from77 = from77
        self.smm_Grade = smm_Grade
        self.Grade = Grade
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def smm_Grade(self):
        return self.__smm_Grade

    @smm_Grade.setter
    def smm_Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Grade__smm_Grade", None)
        self.__smm_Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DimensionalMeasurement75"):
                opp_val = getattr(old_value, "smm_DimensionalMeasurement75", None)
                if opp_val == self:
                    setattr(old_value, "smm_DimensionalMeasurement75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DimensionalMeasurement75"):
                opp_val = getattr(value, "smm_DimensionalMeasurement75", None)
                setattr(value, "smm_DimensionalMeasurement75", self)

    @property
    def Grade(self):
        return self.__Grade

    @Grade.setter
    def Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Grade__Grade", None)
        self.__Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankingTo163"):
                opp_val = getattr(old_value, "rankingTo163", None)
                if opp_val == self:
                    setattr(old_value, "rankingTo163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankingTo163"):
                opp_val = getattr(value, "rankingTo163", None)
                setattr(value, "rankingTo163", self)

    @property
    def from77(self):
        return self.__from77

    @from77.setter
    def from77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Grade__from77", None)
        self.__from77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RankingMeasurementRelationship78"):
                opp_val = getattr(old_value, "RankingMeasurementRelationship78", None)
                if opp_val == self:
                    setattr(old_value, "RankingMeasurementRelationship78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RankingMeasurementRelationship78"):
                opp_val = getattr(value, "RankingMeasurementRelationship78", None)
                setattr(value, "RankingMeasurementRelationship78", self)

class AbstractMeasureElement:

    pass
class smm_OCLOperation(AbstractMeasureElement):

    def __init__(self, context: str, body: str):
        self.context = context
        self.body = body
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

class smm_Scope(AbstractMeasureElement):

    def __init__(self, class: str, smm_Scope: "smm_Measure" = None, smm_Scope205: "smm_Operation" = None, smm_Scope208: "smm_Operation" = None, smm_Scope202: set["smm_EObject"] = None):
        self.class = class
        self.smm_Scope = smm_Scope
        self.smm_Scope205 = smm_Scope205
        self.smm_Scope208 = smm_Scope208
        self.smm_Scope202 = smm_Scope202 if smm_Scope202 is not None else set()
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def smm_Scope(self):
        return self.__smm_Scope

    @smm_Scope.setter
    def smm_Scope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope", None)
        self.__smm_Scope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure83"):
                opp_val = getattr(old_value, "smm_Measure83", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure83"):
                opp_val = getattr(value, "smm_Measure83", None)
                setattr(value, "smm_Measure83", self)

    @property
    def smm_Scope202(self):
        return self.__smm_Scope202

    @smm_Scope202.setter
    def smm_Scope202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope202", None)
        self.__smm_Scope202 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_EObject203"):
                    opp_val = getattr(item, "smm_EObject203", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_EObject203", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_EObject203"):
                    opp_val = getattr(item, "smm_EObject203", None)
                    
                    setattr(item, "smm_EObject203", self)
                    

    @property
    def smm_Scope208(self):
        return self.__smm_Scope208

    @smm_Scope208.setter
    def smm_Scope208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope208", None)
        self.__smm_Scope208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation209"):
                opp_val = getattr(old_value, "smm_Operation209", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation209"):
                opp_val = getattr(value, "smm_Operation209", None)
                setattr(value, "smm_Operation209", self)

    @property
    def smm_Scope205(self):
        return self.__smm_Scope205

    @smm_Scope205.setter
    def smm_Scope205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope205", None)
        self.__smm_Scope205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation206"):
                opp_val = getattr(old_value, "smm_Operation206", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation206"):
                opp_val = getattr(value, "smm_Operation206", None)
                setattr(value, "smm_Operation206", self)

class smm_Measure(AbstractMeasureElement):

    def __init__(self, measureLabelFormat: str, measurementLabelFormat: str, visible: bool, Measure: "smm_EquivalentMeasureRelationship" = None, Measure68: "smm_EquivalentMeasureRelationship" = None, categoryMeasure: set["smm_MeasureCategory"] = None, smm_Measure: "smm_Characteristic" = None, smm_Measure83: "smm_Scope" = None, from85: set["smm_RefinementMeasureRelationship"] = None, to87: set["smm_RefinementMeasureRelationship"] = None, to97: "smm_RecursiveMeasureRelationship" = None, smm_Measure100: set["smm_MeasureRelationship"] = None, smm_Measure102: "smm_Operation" = None, Measure112: "smm_MeasureCategory" = None, from90: set["smm_EquivalentMeasureRelationship"] = None, to92: set["smm_EquivalentMeasureRelationship"] = None, from95: "smm_RecursiveMeasureRelationship" = None, smm_Measure149: "smm_ObservedMeasure" = None, Measure170: "smm_RecursiveMeasureRelationship" = None, Measure178: "smm_RefinementMeasureRelationship" = None, Measure180: "smm_RefinementMeasureRelationship" = None, Measure168: "smm_RecursiveMeasureRelationship" = None):
        self.measureLabelFormat = measureLabelFormat
        self.measurementLabelFormat = measurementLabelFormat
        self.visible = visible
        self.Measure = Measure
        self.Measure68 = Measure68
        self.categoryMeasure = categoryMeasure if categoryMeasure is not None else set()
        self.smm_Measure = smm_Measure
        self.smm_Measure83 = smm_Measure83
        self.from85 = from85 if from85 is not None else set()
        self.to87 = to87 if to87 is not None else set()
        self.to97 = to97
        self.smm_Measure100 = smm_Measure100 if smm_Measure100 is not None else set()
        self.smm_Measure102 = smm_Measure102
        self.Measure112 = Measure112
        self.from90 = from90 if from90 is not None else set()
        self.to92 = to92 if to92 is not None else set()
        self.from95 = from95
        self.smm_Measure149 = smm_Measure149
        self.Measure170 = Measure170
        self.Measure178 = Measure178
        self.Measure180 = Measure180
        self.Measure168 = Measure168
        
    @property
    def measurementLabelFormat(self) -> str:
        return self.__measurementLabelFormat

    @measurementLabelFormat.setter
    def measurementLabelFormat(self, measurementLabelFormat: str):
        self.__measurementLabelFormat = measurementLabelFormat

    @property
    def measureLabelFormat(self) -> str:
        return self.__measureLabelFormat

    @measureLabelFormat.setter
    def measureLabelFormat(self, measureLabelFormat: str):
        self.__measureLabelFormat = measureLabelFormat

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def to97(self):
        return self.__to97

    @to97.setter
    def to97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to97", None)
        self.__to97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecursiveMeasureRelationship98"):
                opp_val = getattr(old_value, "RecursiveMeasureRelationship98", None)
                if opp_val == self:
                    setattr(old_value, "RecursiveMeasureRelationship98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecursiveMeasureRelationship98"):
                opp_val = getattr(value, "RecursiveMeasureRelationship98", None)
                setattr(value, "RecursiveMeasureRelationship98", self)

    @property
    def Measure68(self):
        return self.__Measure68

    @Measure68.setter
    def Measure68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure68", None)
        self.__Measure68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentFrom"):
                opp_val = getattr(old_value, "equivalentFrom", None)
                if opp_val == self:
                    setattr(old_value, "equivalentFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentFrom"):
                opp_val = getattr(value, "equivalentFrom", None)
                setattr(value, "equivalentFrom", self)

    @property
    def Measure178(self):
        return self.__Measure178

    @Measure178.setter
    def Measure178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure178", None)
        self.__Measure178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementTo"):
                opp_val = getattr(old_value, "refinementTo", None)
                if opp_val == self:
                    setattr(old_value, "refinementTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementTo"):
                opp_val = getattr(value, "refinementTo", None)
                setattr(value, "refinementTo", self)

    @property
    def smm_Measure102(self):
        return self.__smm_Measure102

    @smm_Measure102.setter
    def smm_Measure102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure102", None)
        self.__smm_Measure102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation103"):
                opp_val = getattr(old_value, "smm_Operation103", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation103"):
                opp_val = getattr(value, "smm_Operation103", None)
                setattr(value, "smm_Operation103", self)

    @property
    def Measure168(self):
        return self.__Measure168

    @Measure168.setter
    def Measure168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure168", None)
        self.__Measure168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveTo"):
                opp_val = getattr(old_value, "recursiveTo", None)
                if opp_val == self:
                    setattr(old_value, "recursiveTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveTo"):
                opp_val = getattr(value, "recursiveTo", None)
                setattr(value, "recursiveTo", self)

    @property
    def to87(self):
        return self.__to87

    @to87.setter
    def to87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to87", None)
        self.__to87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementMeasureRelationship88"):
                    opp_val = getattr(item, "RefinementMeasureRelationship88", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementMeasureRelationship88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementMeasureRelationship88"):
                    opp_val = getattr(item, "RefinementMeasureRelationship88", None)
                    
                    setattr(item, "RefinementMeasureRelationship88", self)
                    

    @property
    def smm_Measure100(self):
        return self.__smm_Measure100

    @smm_Measure100.setter
    def smm_Measure100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure100", None)
        self.__smm_Measure100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship"):
                    opp_val = getattr(item, "smm_MeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship"):
                    opp_val = getattr(item, "smm_MeasureRelationship", None)
                    
                    setattr(item, "smm_MeasureRelationship", self)
                    

    @property
    def categoryMeasure(self):
        return self.__categoryMeasure

    @categoryMeasure.setter
    def categoryMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__categoryMeasure", None)
        self.__categoryMeasure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureCategory"):
                    opp_val = getattr(item, "MeasureCategory", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureCategory", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureCategory"):
                    opp_val = getattr(item, "MeasureCategory", None)
                    
                    setattr(item, "MeasureCategory", self)
                    

    @property
    def smm_Measure(self):
        return self.__smm_Measure

    @smm_Measure.setter
    def smm_Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure", None)
        self.__smm_Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Characteristic81"):
                opp_val = getattr(old_value, "smm_Characteristic81", None)
                if opp_val == self:
                    setattr(old_value, "smm_Characteristic81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Characteristic81"):
                opp_val = getattr(value, "smm_Characteristic81", None)
                setattr(value, "smm_Characteristic81", self)

    @property
    def to92(self):
        return self.__to92

    @to92.setter
    def to92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to92", None)
        self.__to92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquivalentMeasureRelationship93"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship93", None)
                    
                    if opp_val == self:
                        setattr(item, "EquivalentMeasureRelationship93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquivalentMeasureRelationship93"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship93", None)
                    
                    setattr(item, "EquivalentMeasureRelationship93", self)
                    

    @property
    def smm_Measure83(self):
        return self.__smm_Measure83

    @smm_Measure83.setter
    def smm_Measure83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure83", None)
        self.__smm_Measure83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope"):
                opp_val = getattr(old_value, "smm_Scope", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope"):
                opp_val = getattr(value, "smm_Scope", None)
                setattr(value, "smm_Scope", self)

    @property
    def smm_Measure149(self):
        return self.__smm_Measure149

    @smm_Measure149.setter
    def smm_Measure149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure149", None)
        self.__smm_Measure149 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_ObservedMeasure148"):
                opp_val = getattr(old_value, "smm_ObservedMeasure148", None)
                if opp_val == self:
                    setattr(old_value, "smm_ObservedMeasure148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_ObservedMeasure148"):
                opp_val = getattr(value, "smm_ObservedMeasure148", None)
                setattr(value, "smm_ObservedMeasure148", self)

    @property
    def Measure180(self):
        return self.__Measure180

    @Measure180.setter
    def Measure180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure180", None)
        self.__Measure180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementFrom"):
                opp_val = getattr(old_value, "refinementFrom", None)
                if opp_val == self:
                    setattr(old_value, "refinementFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementFrom"):
                opp_val = getattr(value, "refinementFrom", None)
                setattr(value, "refinementFrom", self)

    @property
    def Measure170(self):
        return self.__Measure170

    @Measure170.setter
    def Measure170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure170", None)
        self.__Measure170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveFrom"):
                opp_val = getattr(old_value, "recursiveFrom", None)
                if opp_val == self:
                    setattr(old_value, "recursiveFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveFrom"):
                opp_val = getattr(value, "recursiveFrom", None)
                setattr(value, "recursiveFrom", self)

    @property
    def from90(self):
        return self.__from90

    @from90.setter
    def from90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from90", None)
        self.__from90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquivalentMeasureRelationship"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "EquivalentMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquivalentMeasureRelationship"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship", None)
                    
                    setattr(item, "EquivalentMeasureRelationship", self)
                    

    @property
    def from95(self):
        return self.__from95

    @from95.setter
    def from95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from95", None)
        self.__from95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecursiveMeasureRelationship"):
                opp_val = getattr(old_value, "RecursiveMeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "RecursiveMeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecursiveMeasureRelationship"):
                opp_val = getattr(value, "RecursiveMeasureRelationship", None)
                setattr(value, "RecursiveMeasureRelationship", self)

    @property
    def Measure112(self):
        return self.__Measure112

    @Measure112.setter
    def Measure112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure112", None)
        self.__Measure112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category111"):
                opp_val = getattr(old_value, "category111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category111"):
                opp_val = getattr(value, "category111", None)
                if opp_val is None:
                    setattr(value, "category111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def from85(self):
        return self.__from85

    @from85.setter
    def from85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from85", None)
        self.__from85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementMeasureRelationship"):
                    opp_val = getattr(item, "RefinementMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementMeasureRelationship"):
                    opp_val = getattr(item, "RefinementMeasureRelationship", None)
                    
                    setattr(item, "RefinementMeasureRelationship", self)
                    

    @property
    def Measure(self):
        return self.__Measure

    @Measure.setter
    def Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure", None)
        self.__Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentTo"):
                opp_val = getattr(old_value, "equivalentTo", None)
                if opp_val == self:
                    setattr(old_value, "equivalentTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentTo"):
                opp_val = getattr(value, "equivalentTo", None)
                setattr(value, "equivalentTo", self)

    def getAllArguments(self) -> str:
        # TODO: Implement getAllArguments method
        pass

    def getArguments(self) -> str:
        # TODO: Implement getArguments method
        pass

class smm_Operation(AbstractMeasureElement):

    def __init__(self, language: str, body: str, smm_Operation: "smm_DirectMeasure" = None, smm_Operation65: "smm_EquivalentMeasureRelationship" = None, smm_Operation103: "smm_Measure" = None, smm_Operation120: "smm_MeasureRelationship" = None, smm_Operation206: "smm_Scope" = None, smm_Operation209: "smm_Scope" = None):
        self.language = language
        self.body = body
        self.smm_Operation = smm_Operation
        self.smm_Operation65 = smm_Operation65
        self.smm_Operation103 = smm_Operation103
        self.smm_Operation120 = smm_Operation120
        self.smm_Operation206 = smm_Operation206
        self.smm_Operation209 = smm_Operation209
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def smm_Operation(self):
        return self.__smm_Operation

    @smm_Operation.setter
    def smm_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation", None)
        self.__smm_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_DirectMeasure"):
                opp_val = getattr(old_value, "smm_DirectMeasure", None)
                if opp_val == self:
                    setattr(old_value, "smm_DirectMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_DirectMeasure"):
                opp_val = getattr(value, "smm_DirectMeasure", None)
                setattr(value, "smm_DirectMeasure", self)

    @property
    def smm_Operation103(self):
        return self.__smm_Operation103

    @smm_Operation103.setter
    def smm_Operation103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation103", None)
        self.__smm_Operation103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure102"):
                opp_val = getattr(old_value, "smm_Measure102", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure102"):
                opp_val = getattr(value, "smm_Measure102", None)
                setattr(value, "smm_Measure102", self)

    @property
    def smm_Operation120(self):
        return self.__smm_Operation120

    @smm_Operation120.setter
    def smm_Operation120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation120", None)
        self.__smm_Operation120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_MeasureRelationship119"):
                opp_val = getattr(old_value, "smm_MeasureRelationship119", None)
                if opp_val == self:
                    setattr(old_value, "smm_MeasureRelationship119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_MeasureRelationship119"):
                opp_val = getattr(value, "smm_MeasureRelationship119", None)
                setattr(value, "smm_MeasureRelationship119", self)

    @property
    def smm_Operation206(self):
        return self.__smm_Operation206

    @smm_Operation206.setter
    def smm_Operation206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation206", None)
        self.__smm_Operation206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope205"):
                opp_val = getattr(old_value, "smm_Scope205", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope205"):
                opp_val = getattr(value, "smm_Scope205", None)
                setattr(value, "smm_Scope205", self)

    @property
    def smm_Operation209(self):
        return self.__smm_Operation209

    @smm_Operation209.setter
    def smm_Operation209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation209", None)
        self.__smm_Operation209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope208"):
                opp_val = getattr(old_value, "smm_Scope208", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope208"):
                opp_val = getattr(value, "smm_Scope208", None)
                setattr(value, "smm_Scope208", self)

    @property
    def smm_Operation65(self):
        return self.__smm_Operation65

    @smm_Operation65.setter
    def smm_Operation65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation65", None)
        self.__smm_Operation65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_EquivalentMeasureRelationship"):
                opp_val = getattr(old_value, "smm_EquivalentMeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "smm_EquivalentMeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_EquivalentMeasureRelationship"):
                opp_val = getattr(value, "smm_EquivalentMeasureRelationship", None)
                setattr(value, "smm_EquivalentMeasureRelationship", self)

    def getParamStrings(self) -> str:
        # TODO: Implement getParamStrings method
        pass

class smm_Characteristic(AbstractMeasureElement):

    pass
class smm_MeasureCategory(AbstractMeasureElement):

    pass
class SmmRelationship:

    pass
class smm_ObservedMeasure(SmmRelationship):

    def __init__(self, smm_ObservedMeasure: "smm_Observation" = None, smm_ObservedMeasure151: set["smm_Measurement"] = None, smm_ObservedMeasure148: "smm_Measure" = None):
        self.smm_ObservedMeasure = smm_ObservedMeasure
        self.smm_ObservedMeasure151 = smm_ObservedMeasure151 if smm_ObservedMeasure151 is not None else set()
        self.smm_ObservedMeasure148 = smm_ObservedMeasure148
        
    @property
    def smm_ObservedMeasure151(self):
        return self.__smm_ObservedMeasure151

    @smm_ObservedMeasure151.setter
    def smm_ObservedMeasure151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_ObservedMeasure__smm_ObservedMeasure151", None)
        self.__smm_ObservedMeasure151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Measurement152"):
                    opp_val = getattr(item, "smm_Measurement152", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Measurement152", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Measurement152"):
                    opp_val = getattr(item, "smm_Measurement152", None)
                    
                    setattr(item, "smm_Measurement152", self)
                    

    @property
    def smm_ObservedMeasure(self):
        return self.__smm_ObservedMeasure

    @smm_ObservedMeasure.setter
    def smm_ObservedMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_ObservedMeasure__smm_ObservedMeasure", None)
        self.__smm_ObservedMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation141"):
                opp_val = getattr(old_value, "smm_Observation141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation141"):
                opp_val = getattr(value, "smm_Observation141", None)
                if opp_val is None:
                    setattr(value, "smm_Observation141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_ObservedMeasure148(self):
        return self.__smm_ObservedMeasure148

    @smm_ObservedMeasure148.setter
    def smm_ObservedMeasure148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_ObservedMeasure__smm_ObservedMeasure148", None)
        self.__smm_ObservedMeasure148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure149"):
                opp_val = getattr(old_value, "smm_Measure149", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure149"):
                opp_val = getattr(value, "smm_Measure149", None)
                setattr(value, "smm_Measure149", self)

    def getMeasureRefimentsObservedMeasures(self) -> str:
        # TODO: Implement getMeasureRefimentsObservedMeasures method
        pass

class smm_MeasurementRelationship(SmmRelationship):

    def __init__(self, smm_MeasurementRelationship: "smm_Measurement" = None):
        self.smm_MeasurementRelationship = smm_MeasurementRelationship
        
    @property
    def smm_MeasurementRelationship(self):
        return self.__smm_MeasurementRelationship

    @smm_MeasurementRelationship.setter
    def smm_MeasurementRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__smm_MeasurementRelationship", None)
        self.__smm_MeasurementRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measurement138"):
                opp_val = getattr(old_value, "smm_Measurement138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measurement138"):
                opp_val = getattr(value, "smm_Measurement138", None)
                if opp_val is None:
                    setattr(value, "smm_Measurement138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getFrom(self) -> Measurement:
        # TODO: Implement getFrom method
        pass

    def getTo(self) -> Measurement:
        # TODO: Implement getTo method
        pass

class smm_MeasureRelationship(SmmRelationship):

    def __init__(self, smm_MeasureRelationship: "smm_Measure" = None, smm_MeasureRelationship119: "smm_Operation" = None):
        self.smm_MeasureRelationship = smm_MeasureRelationship
        self.smm_MeasureRelationship119 = smm_MeasureRelationship119
        
    @property
    def smm_MeasureRelationship(self):
        return self.__smm_MeasureRelationship

    @smm_MeasureRelationship.setter
    def smm_MeasureRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship", None)
        self.__smm_MeasureRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure100"):
                opp_val = getattr(old_value, "smm_Measure100", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure100"):
                opp_val = getattr(value, "smm_Measure100", None)
                if opp_val is None:
                    setattr(value, "smm_Measure100", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_MeasureRelationship119(self):
        return self.__smm_MeasureRelationship119

    @smm_MeasureRelationship119.setter
    def smm_MeasureRelationship119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureRelationship__smm_MeasureRelationship119", None)
        self.__smm_MeasureRelationship119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation120"):
                opp_val = getattr(old_value, "smm_Operation120", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation120"):
                opp_val = getattr(value, "smm_Operation120", None)
                setattr(value, "smm_Operation120", self)

    def getTo(self) -> Measure:
        # TODO: Implement getTo method
        pass

    def getFrom(self) -> Measure:
        # TODO: Implement getFrom method
        pass

class DimensionalMeasure:

    pass
class smm_DirectMeasure(DimensionalMeasure):

    pass
class smm_RescaledMeasure(DimensionalMeasure):

    def __init__(self, formula: str, to188: set["smm_RescaleMeasureRelationship"] = None, RescaledMeasure: "smm_RescaleMeasureRelationship" = None):
        self.formula = formula
        self.to188 = to188 if to188 is not None else set()
        self.RescaledMeasure = RescaledMeasure
        
    @property
    def formula(self) -> str:
        return self.__formula

    @formula.setter
    def formula(self, formula: str):
        self.__formula = formula

    @property
    def RescaledMeasure(self):
        return self.__RescaledMeasure

    @RescaledMeasure.setter
    def RescaledMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__RescaledMeasure", None)
        self.__RescaledMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescaleFrom"):
                opp_val = getattr(old_value, "rescaleFrom", None)
                if opp_val == self:
                    setattr(old_value, "rescaleFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleFrom"):
                opp_val = getattr(value, "rescaleFrom", None)
                setattr(value, "rescaleFrom", self)

    @property
    def to188(self):
        return self.__to188

    @to188.setter
    def to188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__to188", None)
        self.__to188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasureRelationship189"):
                    opp_val = getattr(item, "RescaleMeasureRelationship189", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasureRelationship189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasureRelationship189"):
                    opp_val = getattr(item, "RescaleMeasureRelationship189", None)
                    
                    setattr(item, "RescaleMeasureRelationship189", self)
                    

class smm_NamedMeasure(DimensionalMeasure):

    pass
class smm_CollectiveMeasure(DimensionalMeasure):

    def __init__(self, accumulator: str, CollectiveMeasure: "smm_BaseMeasureRelationship" = None, from35: set["smm_BaseMeasureRelationship"] = None):
        self.accumulator = accumulator
        self.CollectiveMeasure = CollectiveMeasure
        self.from35 = from35 if from35 is not None else set()
        
    @property
    def accumulator(self) -> str:
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, accumulator: str):
        self.__accumulator = accumulator

    @property
    def CollectiveMeasure(self):
        return self.__CollectiveMeasure

    @CollectiveMeasure.setter
    def CollectiveMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasure__CollectiveMeasure", None)
        self.__CollectiveMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasureTo"):
                opp_val = getattr(old_value, "baseMeasureTo", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasureTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasureTo"):
                opp_val = getattr(value, "baseMeasureTo", None)
                setattr(value, "baseMeasureTo", self)

    @property
    def from35(self):
        return self.__from35

    @from35.setter
    def from35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasure__from35", None)
        self.__from35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseMeasureRelationship"):
                    opp_val = getattr(item, "BaseMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasureRelationship"):
                    opp_val = getattr(item, "BaseMeasureRelationship", None)
                    
                    setattr(item, "BaseMeasureRelationship", self)
                    

class smm_CategoryRelationship(SmmRelationship):

    pass
class SmmElement:

    pass
class smm_Measurement(SmmElement):

    def __init__(self, error: str, breakValue: str, Measurement: "smm_EquivalentMeasurementRelationship" = None, Measurement73: "smm_EquivalentMeasurementRelationship" = None, from123: set["smm_RefinementMeasurementRelationship"] = None, to125: set["smm_RefinementMeasurementRelationship"] = None, from128: set["smm_EquivalentMeasurementRelationship"] = None, to130: set["smm_EquivalentMeasurementRelationship"] = None, from133: "smm_RecursiveMeasurementRelationship" = None, to135: set["smm_RecursiveMeasurementRelationship"] = None, smm_Measurement138: set["smm_MeasurementRelationship"] = None, smm_Measurement: "smm_EObject" = None, smm_Measurement152: "smm_ObservedMeasure" = None, Measurement173: "smm_RecursiveMeasurementRelationship" = None, Measurement176: "smm_RecursiveMeasurementRelationship" = None, Measurement183: "smm_RefinementMeasurementRelationship" = None, Measurement186: "smm_RefinementMeasurementRelationship" = None):
        self.error = error
        self.breakValue = breakValue
        self.Measurement = Measurement
        self.Measurement73 = Measurement73
        self.from123 = from123 if from123 is not None else set()
        self.to125 = to125 if to125 is not None else set()
        self.from128 = from128 if from128 is not None else set()
        self.to130 = to130 if to130 is not None else set()
        self.from133 = from133
        self.to135 = to135 if to135 is not None else set()
        self.smm_Measurement138 = smm_Measurement138 if smm_Measurement138 is not None else set()
        self.smm_Measurement = smm_Measurement
        self.smm_Measurement152 = smm_Measurement152
        self.Measurement173 = Measurement173
        self.Measurement176 = Measurement176
        self.Measurement183 = Measurement183
        self.Measurement186 = Measurement186
        
    @property
    def breakValue(self) -> str:
        return self.__breakValue

    @breakValue.setter
    def breakValue(self, breakValue: str):
        self.__breakValue = breakValue

    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def Measurement186(self):
        return self.__Measurement186

    @Measurement186.setter
    def Measurement186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement186", None)
        self.__Measurement186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementFrom185"):
                opp_val = getattr(old_value, "refinementFrom185", None)
                if opp_val == self:
                    setattr(old_value, "refinementFrom185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementFrom185"):
                opp_val = getattr(value, "refinementFrom185", None)
                setattr(value, "refinementFrom185", self)

    @property
    def smm_Measurement138(self):
        return self.__smm_Measurement138

    @smm_Measurement138.setter
    def smm_Measurement138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement138", None)
        self.__smm_Measurement138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship"):
                    opp_val = getattr(item, "smm_MeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship"):
                    opp_val = getattr(item, "smm_MeasurementRelationship", None)
                    
                    setattr(item, "smm_MeasurementRelationship", self)
                    

    @property
    def Measurement183(self):
        return self.__Measurement183

    @Measurement183.setter
    def Measurement183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement183", None)
        self.__Measurement183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementTo182"):
                opp_val = getattr(old_value, "refinementTo182", None)
                if opp_val == self:
                    setattr(old_value, "refinementTo182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementTo182"):
                opp_val = getattr(value, "refinementTo182", None)
                setattr(value, "refinementTo182", self)

    @property
    def smm_Measurement(self):
        return self.__smm_Measurement

    @smm_Measurement.setter
    def smm_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement", None)
        self.__smm_Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_EObject"):
                opp_val = getattr(old_value, "smm_EObject", None)
                if opp_val == self:
                    setattr(old_value, "smm_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_EObject"):
                opp_val = getattr(value, "smm_EObject", None)
                setattr(value, "smm_EObject", self)

    @property
    def to125(self):
        return self.__to125

    @to125.setter
    def to125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__to125", None)
        self.__to125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementMeasurementRelationship126"):
                    opp_val = getattr(item, "RefinementMeasurementRelationship126", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementMeasurementRelationship126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementMeasurementRelationship126"):
                    opp_val = getattr(item, "RefinementMeasurementRelationship126", None)
                    
                    setattr(item, "RefinementMeasurementRelationship126", self)
                    

    @property
    def from128(self):
        return self.__from128

    @from128.setter
    def from128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__from128", None)
        self.__from128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquivalentMeasurementRelationship"):
                    opp_val = getattr(item, "EquivalentMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "EquivalentMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquivalentMeasurementRelationship"):
                    opp_val = getattr(item, "EquivalentMeasurementRelationship", None)
                    
                    setattr(item, "EquivalentMeasurementRelationship", self)
                    

    @property
    def Measurement(self):
        return self.__Measurement

    @Measurement.setter
    def Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement", None)
        self.__Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentTo70"):
                opp_val = getattr(old_value, "equivalentTo70", None)
                if opp_val == self:
                    setattr(old_value, "equivalentTo70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentTo70"):
                opp_val = getattr(value, "equivalentTo70", None)
                setattr(value, "equivalentTo70", self)

    @property
    def from123(self):
        return self.__from123

    @from123.setter
    def from123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__from123", None)
        self.__from123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementMeasurementRelationship"):
                    opp_val = getattr(item, "RefinementMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementMeasurementRelationship"):
                    opp_val = getattr(item, "RefinementMeasurementRelationship", None)
                    
                    setattr(item, "RefinementMeasurementRelationship", self)
                    

    @property
    def from133(self):
        return self.__from133

    @from133.setter
    def from133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__from133", None)
        self.__from133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecursiveMeasurementRelationship"):
                opp_val = getattr(old_value, "RecursiveMeasurementRelationship", None)
                if opp_val == self:
                    setattr(old_value, "RecursiveMeasurementRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecursiveMeasurementRelationship"):
                opp_val = getattr(value, "RecursiveMeasurementRelationship", None)
                setattr(value, "RecursiveMeasurementRelationship", self)

    @property
    def smm_Measurement152(self):
        return self.__smm_Measurement152

    @smm_Measurement152.setter
    def smm_Measurement152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement152", None)
        self.__smm_Measurement152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_ObservedMeasure151"):
                opp_val = getattr(old_value, "smm_ObservedMeasure151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_ObservedMeasure151"):
                opp_val = getattr(value, "smm_ObservedMeasure151", None)
                if opp_val is None:
                    setattr(value, "smm_ObservedMeasure151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Measurement173(self):
        return self.__Measurement173

    @Measurement173.setter
    def Measurement173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement173", None)
        self.__Measurement173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveTo172"):
                opp_val = getattr(old_value, "recursiveTo172", None)
                if opp_val == self:
                    setattr(old_value, "recursiveTo172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveTo172"):
                opp_val = getattr(value, "recursiveTo172", None)
                setattr(value, "recursiveTo172", self)

    @property
    def to135(self):
        return self.__to135

    @to135.setter
    def to135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__to135", None)
        self.__to135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RecursiveMeasurementRelationship136"):
                    opp_val = getattr(item, "RecursiveMeasurementRelationship136", None)
                    
                    if opp_val == self:
                        setattr(item, "RecursiveMeasurementRelationship136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RecursiveMeasurementRelationship136"):
                    opp_val = getattr(item, "RecursiveMeasurementRelationship136", None)
                    
                    setattr(item, "RecursiveMeasurementRelationship136", self)
                    

    @property
    def Measurement73(self):
        return self.__Measurement73

    @Measurement73.setter
    def Measurement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement73", None)
        self.__Measurement73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentFrom72"):
                opp_val = getattr(old_value, "equivalentFrom72", None)
                if opp_val == self:
                    setattr(old_value, "equivalentFrom72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentFrom72"):
                opp_val = getattr(value, "equivalentFrom72", None)
                setattr(value, "equivalentFrom72", self)

    @property
    def to130(self):
        return self.__to130

    @to130.setter
    def to130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__to130", None)
        self.__to130 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquivalentMeasurementRelationship131"):
                    opp_val = getattr(item, "EquivalentMeasurementRelationship131", None)
                    
                    if opp_val == self:
                        setattr(item, "EquivalentMeasurementRelationship131", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquivalentMeasurementRelationship131"):
                    opp_val = getattr(item, "EquivalentMeasurementRelationship131", None)
                    
                    setattr(item, "EquivalentMeasurementRelationship131", self)
                    

    @property
    def Measurement176(self):
        return self.__Measurement176

    @Measurement176.setter
    def Measurement176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement176", None)
        self.__Measurement176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveFrom175"):
                opp_val = getattr(old_value, "recursiveFrom175", None)
                if opp_val == self:
                    setattr(old_value, "recursiveFrom175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveFrom175"):
                opp_val = getattr(value, "recursiveFrom175", None)
                setattr(value, "recursiveFrom175", self)

    def getMeasurementLabel(self) -> str:
        # TODO: Implement getMeasurementLabel method
        pass

    def getMeasureLabel(self) -> str:
        # TODO: Implement getMeasureLabel method
        pass

class smm_SmmRelationship(SmmElement):

    def __init__(self, smm_SmmRelationship: "smm_Observation" = None):
        self.smm_SmmRelationship = smm_SmmRelationship
        
    @property
    def smm_SmmRelationship(self):
        return self.__smm_SmmRelationship

    @smm_SmmRelationship.setter
    def smm_SmmRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmRelationship__smm_SmmRelationship", None)
        self.__smm_SmmRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation144"):
                opp_val = getattr(old_value, "smm_Observation144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation144"):
                opp_val = getattr(value, "smm_Observation144", None)
                if opp_val is None:
                    setattr(value, "smm_Observation144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getTo(self) -> SmmElement:
        # TODO: Implement getTo method
        pass

    def getFrom(self) -> SmmElement:
        # TODO: Implement getFrom method
        pass

class smm_MeasureLibrary(SmmElement):

    def __init__(self, smm_MeasureLibrary: set["smm_AbstractMeasureElement"] = None, smm_MeasureLibrary116: set["smm_CategoryRelationship"] = None, smm_MeasureLibrary218: "smm_SmmModel" = None):
        self.smm_MeasureLibrary = smm_MeasureLibrary if smm_MeasureLibrary is not None else set()
        self.smm_MeasureLibrary116 = smm_MeasureLibrary116 if smm_MeasureLibrary116 is not None else set()
        self.smm_MeasureLibrary218 = smm_MeasureLibrary218
        
    @property
    def smm_MeasureLibrary218(self):
        return self.__smm_MeasureLibrary218

    @smm_MeasureLibrary218.setter
    def smm_MeasureLibrary218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureLibrary__smm_MeasureLibrary218", None)
        self.__smm_MeasureLibrary218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmModel217"):
                opp_val = getattr(old_value, "smm_SmmModel217", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmModel217"):
                opp_val = getattr(value, "smm_SmmModel217", None)
                if opp_val is None:
                    setattr(value, "smm_SmmModel217", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_MeasureLibrary116(self):
        return self.__smm_MeasureLibrary116

    @smm_MeasureLibrary116.setter
    def smm_MeasureLibrary116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureLibrary__smm_MeasureLibrary116", None)
        self.__smm_MeasureLibrary116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_CategoryRelationship117"):
                    opp_val = getattr(item, "smm_CategoryRelationship117", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_CategoryRelationship117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_CategoryRelationship117"):
                    opp_val = getattr(item, "smm_CategoryRelationship117", None)
                    
                    setattr(item, "smm_CategoryRelationship117", self)
                    

    @property
    def smm_MeasureLibrary(self):
        return self.__smm_MeasureLibrary

    @smm_MeasureLibrary.setter
    def smm_MeasureLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureLibrary__smm_MeasureLibrary", None)
        self.__smm_MeasureLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_AbstractMeasureElement114"):
                    opp_val = getattr(item, "smm_AbstractMeasureElement114", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_AbstractMeasureElement114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_AbstractMeasureElement114"):
                    opp_val = getattr(item, "smm_AbstractMeasureElement114", None)
                    
                    setattr(item, "smm_AbstractMeasureElement114", self)
                    

    def getOperations(self) -> AbstractMeasureElement:
        # TODO: Implement getOperations method
        pass

    def getOclOperations(self) -> AbstractMeasureElement:
        # TODO: Implement getOclOperations method
        pass

class smm_SmmModel(SmmElement):

    pass
class smm_ObservationScope(SmmElement):

    def __init__(self, scopeUri: str, smm_ObservationScope: "smm_Observation" = None):
        self.scopeUri = scopeUri
        self.smm_ObservationScope = smm_ObservationScope
        
    @property
    def scopeUri(self) -> str:
        return self.__scopeUri

    @scopeUri.setter
    def scopeUri(self, scopeUri: str):
        self.__scopeUri = scopeUri

    @property
    def smm_ObservationScope(self):
        return self.__smm_ObservationScope

    @smm_ObservationScope.setter
    def smm_ObservationScope(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_ObservationScope__smm_ObservationScope", None)
        self.__smm_ObservationScope = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation"):
                opp_val = getattr(old_value, "smm_Observation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation"):
                opp_val = getattr(value, "smm_Observation", None)
                if opp_val is None:
                    setattr(value, "smm_Observation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_Observation(SmmElement):

    def __init__(self, observer: str, tool: str, whenObserved: str, smm_Observation: set["smm_ObservationScope"] = None, smm_Observation141: set["smm_ObservedMeasure"] = None, requestedObservations: set["smm_SmmElement"] = None, smm_Observation144: set["smm_SmmRelationship"] = None, smm_Observation146: set["smm_Argument"] = None, Observation: "smm_SmmElement" = None, smm_Observation215: "smm_SmmModel" = None):
        self.observer = observer
        self.tool = tool
        self.whenObserved = whenObserved
        self.smm_Observation = smm_Observation if smm_Observation is not None else set()
        self.smm_Observation141 = smm_Observation141 if smm_Observation141 is not None else set()
        self.requestedObservations = requestedObservations if requestedObservations is not None else set()
        self.smm_Observation144 = smm_Observation144 if smm_Observation144 is not None else set()
        self.smm_Observation146 = smm_Observation146 if smm_Observation146 is not None else set()
        self.Observation = Observation
        self.smm_Observation215 = smm_Observation215
        
    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def whenObserved(self) -> str:
        return self.__whenObserved

    @whenObserved.setter
    def whenObserved(self, whenObserved: str):
        self.__whenObserved = whenObserved

    @property
    def observer(self) -> str:
        return self.__observer

    @observer.setter
    def observer(self, observer: str):
        self.__observer = observer

    @property
    def smm_Observation144(self):
        return self.__smm_Observation144

    @smm_Observation144.setter
    def smm_Observation144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation144", None)
        self.__smm_Observation144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_SmmRelationship"):
                    opp_val = getattr(item, "smm_SmmRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_SmmRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_SmmRelationship"):
                    opp_val = getattr(item, "smm_SmmRelationship", None)
                    
                    setattr(item, "smm_SmmRelationship", self)
                    

    @property
    def smm_Observation(self):
        return self.__smm_Observation

    @smm_Observation.setter
    def smm_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation", None)
        self.__smm_Observation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_ObservationScope"):
                    opp_val = getattr(item, "smm_ObservationScope", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_ObservationScope", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_ObservationScope"):
                    opp_val = getattr(item, "smm_ObservationScope", None)
                    
                    setattr(item, "smm_ObservationScope", self)
                    

    @property
    def requestedObservations(self):
        return self.__requestedObservations

    @requestedObservations.setter
    def requestedObservations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__requestedObservations", None)
        self.__requestedObservations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SmmElement"):
                    opp_val = getattr(item, "SmmElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SmmElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SmmElement"):
                    opp_val = getattr(item, "SmmElement", None)
                    
                    setattr(item, "SmmElement", self)
                    

    @property
    def Observation(self):
        return self.__Observation

    @Observation.setter
    def Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__Observation", None)
        self.__Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requestedMeasures"):
                opp_val = getattr(old_value, "requestedMeasures", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requestedMeasures"):
                opp_val = getattr(value, "requestedMeasures", None)
                if opp_val is None:
                    setattr(value, "requestedMeasures", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_Observation141(self):
        return self.__smm_Observation141

    @smm_Observation141.setter
    def smm_Observation141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation141", None)
        self.__smm_Observation141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_ObservedMeasure"):
                    opp_val = getattr(item, "smm_ObservedMeasure", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_ObservedMeasure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_ObservedMeasure"):
                    opp_val = getattr(item, "smm_ObservedMeasure", None)
                    
                    setattr(item, "smm_ObservedMeasure", self)
                    

    @property
    def smm_Observation146(self):
        return self.__smm_Observation146

    @smm_Observation146.setter
    def smm_Observation146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation146", None)
        self.__smm_Observation146 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_Argument"):
                    opp_val = getattr(item, "smm_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_Argument"):
                    opp_val = getattr(item, "smm_Argument", None)
                    
                    setattr(item, "smm_Argument", self)
                    

    @property
    def smm_Observation215(self):
        return self.__smm_Observation215

    @smm_Observation215.setter
    def smm_Observation215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation215", None)
        self.__smm_Observation215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmModel"):
                opp_val = getattr(old_value, "smm_SmmModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmModel"):
                opp_val = getattr(value, "smm_SmmModel", None)
                if opp_val is None:
                    setattr(value, "smm_SmmModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_RankingInterval(SmmElement):

    def __init__(self, maximumEndpoint: float, maximumOpen: bool, minimumEndpoint: float, minimumOpen: bool, symbol: str, RankingInterval: "smm_Ranking" = None, interval: "smm_Ranking" = None):
        self.maximumEndpoint = maximumEndpoint
        self.maximumOpen = maximumOpen
        self.minimumEndpoint = minimumEndpoint
        self.minimumOpen = minimumOpen
        self.symbol = symbol
        self.RankingInterval = RankingInterval
        self.interval = interval
        
    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def maximumOpen(self) -> bool:
        return self.__maximumOpen

    @maximumOpen.setter
    def maximumOpen(self, maximumOpen: bool):
        self.__maximumOpen = maximumOpen

    @property
    def maximumEndpoint(self) -> float:
        return self.__maximumEndpoint

    @maximumEndpoint.setter
    def maximumEndpoint(self, maximumEndpoint: float):
        self.__maximumEndpoint = maximumEndpoint

    @property
    def minimumOpen(self) -> bool:
        return self.__minimumOpen

    @minimumOpen.setter
    def minimumOpen(self, minimumOpen: bool):
        self.__minimumOpen = minimumOpen

    @property
    def minimumEndpoint(self) -> float:
        return self.__minimumEndpoint

    @minimumEndpoint.setter
    def minimumEndpoint(self, minimumEndpoint: float):
        self.__minimumEndpoint = minimumEndpoint

    @property
    def RankingInterval(self):
        return self.__RankingInterval

    @RankingInterval.setter
    def RankingInterval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingInterval__RankingInterval", None)
        self.__RankingInterval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rank"):
                opp_val = getattr(old_value, "rank", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rank"):
                opp_val = getattr(value, "rank", None)
                if opp_val is None:
                    setattr(value, "rank", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def interval(self):
        return self.__interval

    @interval.setter
    def interval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingInterval__interval", None)
        self.__interval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ranking"):
                opp_val = getattr(old_value, "Ranking", None)
                if opp_val == self:
                    setattr(old_value, "Ranking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ranking"):
                opp_val = getattr(value, "Ranking", None)
                setattr(value, "Ranking", self)

class smm_AbstractMeasureElement(SmmElement):

    pass
class smm_DimensionalMeasure(Measure):

    def __init__(self, unit: str, DimensionalMeasure: "smm_Base1MeasureRelationship" = None, DimensionalMeasure19: "smm_BaseMeasureRelationship" = None, DimensionalMeasure13: "smm_Base2MeasureRelationship" = None, to: set["smm_BaseMeasureRelationship"] = None, to41: set["smm_Base1MeasureRelationship"] = None, to44: set["smm_Base2MeasureRelationship"] = None, from47: "smm_RescaleMeasureRelationship" = None, to49: set["smm_RankingMeasureRelationship"] = None, DimensionalMeasure161: "smm_RankingMeasureRelationship" = None, DimensionalMeasure192: "smm_RescaleMeasureRelationship" = None):
        self.unit = unit
        self.DimensionalMeasure = DimensionalMeasure
        self.DimensionalMeasure19 = DimensionalMeasure19
        self.DimensionalMeasure13 = DimensionalMeasure13
        self.to = to if to is not None else set()
        self.to41 = to41 if to41 is not None else set()
        self.to44 = to44 if to44 is not None else set()
        self.from47 = from47
        self.to49 = to49 if to49 is not None else set()
        self.DimensionalMeasure161 = DimensionalMeasure161
        self.DimensionalMeasure192 = DimensionalMeasure192
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def to44(self):
        return self.__to44

    @to44.setter
    def to44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to44", None)
        self.__to44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base2MeasureRelationship45"):
                    opp_val = getattr(item, "Base2MeasureRelationship45", None)
                    
                    if opp_val == self:
                        setattr(item, "Base2MeasureRelationship45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base2MeasureRelationship45"):
                    opp_val = getattr(item, "Base2MeasureRelationship45", None)
                    
                    setattr(item, "Base2MeasureRelationship45", self)
                    

    @property
    def DimensionalMeasure192(self):
        return self.__DimensionalMeasure192

    @DimensionalMeasure192.setter
    def DimensionalMeasure192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure192", None)
        self.__DimensionalMeasure192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescaleTo"):
                opp_val = getattr(old_value, "rescaleTo", None)
                if opp_val == self:
                    setattr(old_value, "rescaleTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleTo"):
                opp_val = getattr(value, "rescaleTo", None)
                setattr(value, "rescaleTo", self)

    @property
    def to41(self):
        return self.__to41

    @to41.setter
    def to41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to41", None)
        self.__to41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base1MeasureRelationship42"):
                    opp_val = getattr(item, "Base1MeasureRelationship42", None)
                    
                    if opp_val == self:
                        setattr(item, "Base1MeasureRelationship42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base1MeasureRelationship42"):
                    opp_val = getattr(item, "Base1MeasureRelationship42", None)
                    
                    setattr(item, "Base1MeasureRelationship42", self)
                    

    @property
    def DimensionalMeasure(self):
        return self.__DimensionalMeasure

    @DimensionalMeasure.setter
    def DimensionalMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure", None)
        self.__DimensionalMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasure1From"):
                opp_val = getattr(old_value, "baseMeasure1From", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasure1From", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasure1From"):
                opp_val = getattr(value, "baseMeasure1From", None)
                setattr(value, "baseMeasure1From", self)

    @property
    def DimensionalMeasure161(self):
        return self.__DimensionalMeasure161

    @DimensionalMeasure161.setter
    def DimensionalMeasure161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure161", None)
        self.__DimensionalMeasure161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankingFrom"):
                opp_val = getattr(old_value, "rankingFrom", None)
                if opp_val == self:
                    setattr(old_value, "rankingFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankingFrom"):
                opp_val = getattr(value, "rankingFrom", None)
                setattr(value, "rankingFrom", self)

    @property
    def DimensionalMeasure13(self):
        return self.__DimensionalMeasure13

    @DimensionalMeasure13.setter
    def DimensionalMeasure13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure13", None)
        self.__DimensionalMeasure13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasure2From"):
                opp_val = getattr(old_value, "baseMeasure2From", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasure2From", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasure2From"):
                opp_val = getattr(value, "baseMeasure2From", None)
                setattr(value, "baseMeasure2From", self)

    @property
    def from47(self):
        return self.__from47

    @from47.setter
    def from47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__from47", None)
        self.__from47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RescaleMeasureRelationship"):
                opp_val = getattr(old_value, "RescaleMeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "RescaleMeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RescaleMeasureRelationship"):
                opp_val = getattr(value, "RescaleMeasureRelationship", None)
                setattr(value, "RescaleMeasureRelationship", self)

    @property
    def DimensionalMeasure19(self):
        return self.__DimensionalMeasure19

    @DimensionalMeasure19.setter
    def DimensionalMeasure19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure19", None)
        self.__DimensionalMeasure19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasureFrom"):
                opp_val = getattr(old_value, "baseMeasureFrom", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasureFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasureFrom"):
                opp_val = getattr(value, "baseMeasureFrom", None)
                setattr(value, "baseMeasureFrom", self)

    @property
    def to49(self):
        return self.__to49

    @to49.setter
    def to49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to49", None)
        self.__to49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RankingMeasureRelationship"):
                    opp_val = getattr(item, "RankingMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RankingMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RankingMeasureRelationship"):
                    opp_val = getattr(item, "RankingMeasureRelationship", None)
                    
                    setattr(item, "RankingMeasureRelationship", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseMeasureRelationship39"):
                    opp_val = getattr(item, "BaseMeasureRelationship39", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasureRelationship39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasureRelationship39"):
                    opp_val = getattr(item, "BaseMeasureRelationship39", None)
                    
                    setattr(item, "BaseMeasureRelationship39", self)
                    

class smm_BinaryMeasure(DimensionalMeasure):

    def __init__(self, functor: str, BinaryMeasure: "smm_Base1MeasureRelationship" = None, BinaryMeasure11: "smm_Base2MeasureRelationship" = None, from: "smm_Base1MeasureRelationship" = None, from22: "smm_Base2MeasureRelationship" = None):
        self.functor = functor
        self.BinaryMeasure = BinaryMeasure
        self.BinaryMeasure11 = BinaryMeasure11
        self.from = from
        self.from22 = from22
        
    @property
    def functor(self) -> str:
        return self.__functor

    @functor.setter
    def functor(self, functor: str):
        self.__functor = functor

    @property
    def from(self):
        return self.__from

    @from.setter
    def from(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__from", None)
        self.__from = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Base1MeasureRelationship"):
                opp_val = getattr(old_value, "Base1MeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "Base1MeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Base1MeasureRelationship"):
                opp_val = getattr(value, "Base1MeasureRelationship", None)
                setattr(value, "Base1MeasureRelationship", self)

    @property
    def BinaryMeasure(self):
        return self.__BinaryMeasure

    @BinaryMeasure.setter
    def BinaryMeasure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__BinaryMeasure", None)
        self.__BinaryMeasure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasure1To"):
                opp_val = getattr(old_value, "baseMeasure1To", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasure1To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasure1To"):
                opp_val = getattr(value, "baseMeasure1To", None)
                setattr(value, "baseMeasure1To", self)

    @property
    def BinaryMeasure11(self):
        return self.__BinaryMeasure11

    @BinaryMeasure11.setter
    def BinaryMeasure11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__BinaryMeasure11", None)
        self.__BinaryMeasure11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasure2To"):
                opp_val = getattr(old_value, "baseMeasure2To", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasure2To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasure2To"):
                opp_val = getattr(value, "baseMeasure2To", None)
                setattr(value, "baseMeasure2To", self)

    @property
    def from22(self):
        return self.__from22

    @from22.setter
    def from22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__from22", None)
        self.__from22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Base2MeasureRelationship"):
                opp_val = getattr(old_value, "Base2MeasureRelationship", None)
                if opp_val == self:
                    setattr(old_value, "Base2MeasureRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Base2MeasureRelationship"):
                opp_val = getattr(value, "Base2MeasureRelationship", None)
                setattr(value, "Base2MeasureRelationship", self)

class MeasureRelationship:

    pass
class smm_BaseMeasureRelationship(MeasureRelationship):

    pass
class smm_RecursiveMeasureRelationship(MeasureRelationship):

    pass
class smm_RefinementMeasureRelationship(MeasureRelationship):

    pass
class smm_EquivalentMeasureRelationship(MeasureRelationship):

    pass
class smm_RankingMeasureRelationship(MeasureRelationship):

    pass
class smm_Base2MeasureRelationship(MeasureRelationship):

    pass
class smm_RescaleMeasureRelationship(MeasureRelationship):

    pass
class smm_Base1MeasureRelationship(MeasureRelationship):

    pass
class MeasurementRelationship:

    pass
class smm_BaseMeasurementRelationship(MeasurementRelationship):

    pass
class smm_EquivalentMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RecursiveMeasurementRelationship(MeasurementRelationship):

    pass
class smm_Base2MeasurementRelationship(MeasurementRelationship):

    pass
class smm_RescaleMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RefinementMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RankingMeasurementRelationship(MeasurementRelationship):

    pass
class smm_Base1MeasurementRelationship(MeasurementRelationship):

    pass
class smm_DimensionalMeasurement(Measurement):

    def __init__(self, value: float, smm_DimensionalMeasurement: "smm_AggregatedMeasurement" = None, DimensionalMeasurement: "smm_Base1MeasurementRelationship" = None, DimensionalMeasurement9: "smm_Base2MeasurementRelationship" = None, DimensionalMeasurement16: "smm_BaseMeasurementRelationship" = None, to51: set["smm_BaseMeasurementRelationship"] = None, to54: set["smm_Base1MeasurementRelationship"] = None, to57: set["smm_Base2MeasurementRelationship"] = None, from60: set["smm_RescaleMeasurementRelationship"] = None, to62: set["smm_RankingMeasurementRelationship"] = None, smm_DimensionalMeasurement75: "smm_Grade" = None, DimensionalMeasurement166: "smm_RankingMeasurementRelationship" = None, DimensionalMeasurement200: "smm_RescaleMeasurementRelationship" = None):
        self.value = value
        self.smm_DimensionalMeasurement = smm_DimensionalMeasurement
        self.DimensionalMeasurement = DimensionalMeasurement
        self.DimensionalMeasurement9 = DimensionalMeasurement9
        self.DimensionalMeasurement16 = DimensionalMeasurement16
        self.to51 = to51 if to51 is not None else set()
        self.to54 = to54 if to54 is not None else set()
        self.to57 = to57 if to57 is not None else set()
        self.from60 = from60 if from60 is not None else set()
        self.to62 = to62 if to62 is not None else set()
        self.smm_DimensionalMeasurement75 = smm_DimensionalMeasurement75
        self.DimensionalMeasurement166 = DimensionalMeasurement166
        self.DimensionalMeasurement200 = DimensionalMeasurement200
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def DimensionalMeasurement16(self):
        return self.__DimensionalMeasurement16

    @DimensionalMeasurement16.setter
    def DimensionalMeasurement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement16", None)
        self.__DimensionalMeasurement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurementFrom"):
                opp_val = getattr(old_value, "baseMeasurementFrom", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurementFrom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurementFrom"):
                opp_val = getattr(value, "baseMeasurementFrom", None)
                setattr(value, "baseMeasurementFrom", self)

    @property
    def to51(self):
        return self.__to51

    @to51.setter
    def to51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to51", None)
        self.__to51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseMeasurementRelationship52"):
                    opp_val = getattr(item, "BaseMeasurementRelationship52", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasurementRelationship52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasurementRelationship52"):
                    opp_val = getattr(item, "BaseMeasurementRelationship52", None)
                    
                    setattr(item, "BaseMeasurementRelationship52", self)
                    

    @property
    def to57(self):
        return self.__to57

    @to57.setter
    def to57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to57", None)
        self.__to57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base2MeasurementRelationship58"):
                    opp_val = getattr(item, "Base2MeasurementRelationship58", None)
                    
                    if opp_val == self:
                        setattr(item, "Base2MeasurementRelationship58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base2MeasurementRelationship58"):
                    opp_val = getattr(item, "Base2MeasurementRelationship58", None)
                    
                    setattr(item, "Base2MeasurementRelationship58", self)
                    

    @property
    def DimensionalMeasurement200(self):
        return self.__DimensionalMeasurement200

    @DimensionalMeasurement200.setter
    def DimensionalMeasurement200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement200", None)
        self.__DimensionalMeasurement200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescaleTo199"):
                opp_val = getattr(old_value, "rescaleTo199", None)
                if opp_val == self:
                    setattr(old_value, "rescaleTo199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleTo199"):
                opp_val = getattr(value, "rescaleTo199", None)
                setattr(value, "rescaleTo199", self)

    @property
    def from60(self):
        return self.__from60

    @from60.setter
    def from60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__from60", None)
        self.__from60 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasurementRelationship"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasurementRelationship"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship", None)
                    
                    setattr(item, "RescaleMeasurementRelationship", self)
                    

    @property
    def to62(self):
        return self.__to62

    @to62.setter
    def to62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to62", None)
        self.__to62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RankingMeasurementRelationship"):
                    opp_val = getattr(item, "RankingMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RankingMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RankingMeasurementRelationship"):
                    opp_val = getattr(item, "RankingMeasurementRelationship", None)
                    
                    setattr(item, "RankingMeasurementRelationship", self)
                    

    @property
    def smm_DimensionalMeasurement75(self):
        return self.__smm_DimensionalMeasurement75

    @smm_DimensionalMeasurement75.setter
    def smm_DimensionalMeasurement75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement75", None)
        self.__smm_DimensionalMeasurement75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Grade"):
                opp_val = getattr(old_value, "smm_Grade", None)
                if opp_val == self:
                    setattr(old_value, "smm_Grade", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Grade"):
                opp_val = getattr(value, "smm_Grade", None)
                setattr(value, "smm_Grade", self)

    @property
    def DimensionalMeasurement(self):
        return self.__DimensionalMeasurement

    @DimensionalMeasurement.setter
    def DimensionalMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement", None)
        self.__DimensionalMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurement1From"):
                opp_val = getattr(old_value, "baseMeasurement1From", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurement1From", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurement1From"):
                opp_val = getattr(value, "baseMeasurement1From", None)
                setattr(value, "baseMeasurement1From", self)

    @property
    def to54(self):
        return self.__to54

    @to54.setter
    def to54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to54", None)
        self.__to54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base1MeasurementRelationship55"):
                    opp_val = getattr(item, "Base1MeasurementRelationship55", None)
                    
                    if opp_val == self:
                        setattr(item, "Base1MeasurementRelationship55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base1MeasurementRelationship55"):
                    opp_val = getattr(item, "Base1MeasurementRelationship55", None)
                    
                    setattr(item, "Base1MeasurementRelationship55", self)
                    

    @property
    def smm_DimensionalMeasurement(self):
        return self.__smm_DimensionalMeasurement

    @smm_DimensionalMeasurement.setter
    def smm_DimensionalMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__smm_DimensionalMeasurement", None)
        self.__smm_DimensionalMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_AggregatedMeasurement"):
                opp_val = getattr(old_value, "smm_AggregatedMeasurement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_AggregatedMeasurement"):
                opp_val = getattr(value, "smm_AggregatedMeasurement", None)
                if opp_val is None:
                    setattr(value, "smm_AggregatedMeasurement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def DimensionalMeasurement9(self):
        return self.__DimensionalMeasurement9

    @DimensionalMeasurement9.setter
    def DimensionalMeasurement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement9", None)
        self.__DimensionalMeasurement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurement2From"):
                opp_val = getattr(old_value, "baseMeasurement2From", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurement2From", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurement2From"):
                opp_val = getattr(value, "baseMeasurement2From", None)
                setattr(value, "baseMeasurement2From", self)

    @property
    def DimensionalMeasurement166(self):
        return self.__DimensionalMeasurement166

    @DimensionalMeasurement166.setter
    def DimensionalMeasurement166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement166", None)
        self.__DimensionalMeasurement166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankingFrom165"):
                opp_val = getattr(old_value, "rankingFrom165", None)
                if opp_val == self:
                    setattr(old_value, "rankingFrom165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankingFrom165"):
                opp_val = getattr(value, "rankingFrom165", None)
                setattr(value, "rankingFrom165", self)

class DimensionalMeasurement:

    pass
class smm_NamedMeasurement(DimensionalMeasurement):

    pass
class smm_CollectiveMeasurement(DimensionalMeasurement):

    def __init__(self, accumulator: str, isBaseSupplied: bool, CollectiveMeasurement: "smm_BaseMeasurementRelationship" = None, from37: set["smm_BaseMeasurementRelationship"] = None):
        self.accumulator = accumulator
        self.isBaseSupplied = isBaseSupplied
        self.CollectiveMeasurement = CollectiveMeasurement
        self.from37 = from37 if from37 is not None else set()
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def accumulator(self) -> str:
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, accumulator: str):
        self.__accumulator = accumulator

    @property
    def from37(self):
        return self.__from37

    @from37.setter
    def from37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasurement__from37", None)
        self.__from37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseMeasurementRelationship"):
                    opp_val = getattr(item, "BaseMeasurementRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasurementRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasurementRelationship"):
                    opp_val = getattr(item, "BaseMeasurementRelationship", None)
                    
                    setattr(item, "BaseMeasurementRelationship", self)
                    

    @property
    def CollectiveMeasurement(self):
        return self.__CollectiveMeasurement

    @CollectiveMeasurement.setter
    def CollectiveMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasurement__CollectiveMeasurement", None)
        self.__CollectiveMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurementTo"):
                opp_val = getattr(old_value, "baseMeasurementTo", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurementTo", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurementTo"):
                opp_val = getattr(value, "baseMeasurementTo", None)
                setattr(value, "baseMeasurementTo", self)

class smm_BinaryMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: bool, BinaryMeasurement: "smm_Base1MeasurementRelationship" = None, BinaryMeasurement7: "smm_Base2MeasurementRelationship" = None, from24: "smm_Base1MeasurementRelationship" = None, from26: "smm_Base2MeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.BinaryMeasurement = BinaryMeasurement
        self.BinaryMeasurement7 = BinaryMeasurement7
        self.from24 = from24
        self.from26 = from26
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def from26(self):
        return self.__from26

    @from26.setter
    def from26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__from26", None)
        self.__from26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Base2MeasurementRelationship"):
                opp_val = getattr(old_value, "Base2MeasurementRelationship", None)
                if opp_val == self:
                    setattr(old_value, "Base2MeasurementRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Base2MeasurementRelationship"):
                opp_val = getattr(value, "Base2MeasurementRelationship", None)
                setattr(value, "Base2MeasurementRelationship", self)

    @property
    def BinaryMeasurement(self):
        return self.__BinaryMeasurement

    @BinaryMeasurement.setter
    def BinaryMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__BinaryMeasurement", None)
        self.__BinaryMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurement1To"):
                opp_val = getattr(old_value, "baseMeasurement1To", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurement1To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurement1To"):
                opp_val = getattr(value, "baseMeasurement1To", None)
                setattr(value, "baseMeasurement1To", self)

    @property
    def BinaryMeasurement7(self):
        return self.__BinaryMeasurement7

    @BinaryMeasurement7.setter
    def BinaryMeasurement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__BinaryMeasurement7", None)
        self.__BinaryMeasurement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseMeasurement2To"):
                opp_val = getattr(old_value, "baseMeasurement2To", None)
                if opp_val == self:
                    setattr(old_value, "baseMeasurement2To", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseMeasurement2To"):
                opp_val = getattr(value, "baseMeasurement2To", None)
                setattr(value, "baseMeasurement2To", self)

    @property
    def from24(self):
        return self.__from24

    @from24.setter
    def from24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__from24", None)
        self.__from24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Base1MeasurementRelationship"):
                opp_val = getattr(old_value, "Base1MeasurementRelationship", None)
                if opp_val == self:
                    setattr(old_value, "Base1MeasurementRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Base1MeasurementRelationship"):
                opp_val = getattr(value, "Base1MeasurementRelationship", None)
                setattr(value, "Base1MeasurementRelationship", self)

class smm_DirectMeasurement(DimensionalMeasurement):

    pass
class smm_RescaledMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: bool, to194: set["smm_RescaleMeasurementRelationship"] = None, RescaledMeasurement: "smm_RescaleMeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.to194 = to194 if to194 is not None else set()
        self.RescaledMeasurement = RescaledMeasurement
        
    @property
    def isBaseSupplied(self) -> bool:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: bool):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def to194(self):
        return self.__to194

    @to194.setter
    def to194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasurement__to194", None)
        self.__to194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasurementRelationship195"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship195", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasurementRelationship195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasurementRelationship195"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship195", None)
                    
                    setattr(item, "RescaleMeasurementRelationship195", self)
                    

    @property
    def RescaledMeasurement(self):
        return self.__RescaledMeasurement

    @RescaledMeasurement.setter
    def RescaledMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasurement__RescaledMeasurement", None)
        self.__RescaledMeasurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescaleFrom197"):
                opp_val = getattr(old_value, "rescaleFrom197", None)
                if opp_val == self:
                    setattr(old_value, "rescaleFrom197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleFrom197"):
                opp_val = getattr(value, "rescaleFrom197", None)
                setattr(value, "rescaleFrom197", self)

class smm_AggregatedMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSuppled: bool, smm_AggregatedMeasurement: set["smm_DimensionalMeasurement"] = None):
        self.isBaseSuppled = isBaseSuppled
        self.smm_AggregatedMeasurement = smm_AggregatedMeasurement if smm_AggregatedMeasurement is not None else set()
        
    @property
    def isBaseSuppled(self) -> bool:
        return self.__isBaseSuppled

    @isBaseSuppled.setter
    def isBaseSuppled(self, isBaseSuppled: bool):
        self.__isBaseSuppled = isBaseSuppled

    @property
    def smm_AggregatedMeasurement(self):
        return self.__smm_AggregatedMeasurement

    @smm_AggregatedMeasurement.setter
    def smm_AggregatedMeasurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_AggregatedMeasurement__smm_AggregatedMeasurement", None)
        self.__smm_AggregatedMeasurement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_DimensionalMeasurement"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_DimensionalMeasurement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_DimensionalMeasurement"):
                    opp_val = getattr(item, "smm_DimensionalMeasurement", None)
                    
                    setattr(item, "smm_DimensionalMeasurement", self)
                    

class smm_Attribute(SmmElement):

    def __init__(self, tag: str, value: str, smm_Attribute: "smm_SmmElement" = None):
        self.tag = tag
        self.value = value
        self.smm_Attribute = smm_Attribute
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

    @property
    def smm_Attribute(self):
        return self.__smm_Attribute

    @smm_Attribute.setter
    def smm_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Attribute__smm_Attribute", None)
        self.__smm_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmElement"):
                opp_val = getattr(old_value, "smm_SmmElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement"):
                opp_val = getattr(value, "smm_SmmElement", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_Argument(SmmElement):

    def __init__(self, type: str, value: str, smm_Argument: "smm_Observation" = None):
        self.type = type
        self.value = value
        self.smm_Argument = smm_Argument
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def smm_Argument(self):
        return self.__smm_Argument

    @smm_Argument.setter
    def smm_Argument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Argument__smm_Argument", None)
        self.__smm_Argument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation146"):
                opp_val = getattr(old_value, "smm_Observation146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation146"):
                opp_val = getattr(value, "smm_Observation146", None)
                if opp_val is None:
                    setattr(value, "smm_Observation146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_Annotation(SmmElement):

    def __init__(self, text: str, smm_Annotation: "smm_SmmElement" = None):
        self.text = text
        self.smm_Annotation = smm_Annotation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def smm_Annotation(self):
        return self.__smm_Annotation

    @smm_Annotation.setter
    def smm_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Annotation__smm_Annotation", None)
        self.__smm_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmElement212"):
                opp_val = getattr(old_value, "smm_SmmElement212", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement212"):
                opp_val = getattr(value, "smm_SmmElement212", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement212", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
