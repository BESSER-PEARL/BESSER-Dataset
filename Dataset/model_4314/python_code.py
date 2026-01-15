from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Accumulator(Enum):
    maximum = "maximum"
    minimum = "minimum"
    average = "average"
    standardDeviation = "standardDeviation"
    sum = "sum"


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
class smm_SmmElement(ABC):

    def __init__(self, name: str, shortDescription: str, description: str, smm_SmmElement: "smm_Observation" = None, smm_SmmElement213: set["smm_Attribute"] = None, smm_SmmElement215: set["smm_Annotation"] = None):
        self.name = name
        self.shortDescription = shortDescription
        self.description = description
        self.smm_SmmElement = smm_SmmElement
        self.smm_SmmElement213 = smm_SmmElement213 if smm_SmmElement213 is not None else set()
        self.smm_SmmElement215 = smm_SmmElement215 if smm_SmmElement215 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortDescription(self) -> str:
        return self.__shortDescription

    @shortDescription.setter
    def shortDescription(self, shortDescription: str):
        self.__shortDescription = shortDescription

    @property
    def smm_SmmElement(self):
        return self.__smm_SmmElement

    @smm_SmmElement.setter
    def smm_SmmElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement", None)
        self.__smm_SmmElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Observation149"):
                opp_val = getattr(old_value, "smm_Observation149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation149"):
                opp_val = getattr(value, "smm_Observation149", None)
                if opp_val is None:
                    setattr(value, "smm_Observation149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_SmmElement215(self):
        return self.__smm_SmmElement215

    @smm_SmmElement215.setter
    def smm_SmmElement215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement215", None)
        self.__smm_SmmElement215 = value if value is not None else set()
        
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
                    

    @property
    def smm_SmmElement213(self):
        return self.__smm_SmmElement213

    @smm_SmmElement213.setter
    def smm_SmmElement213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_SmmElement__smm_SmmElement213", None)
        self.__smm_SmmElement213 = value if value is not None else set()
        
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
                    

    def getOutbound(self) -> SmmRelationship:
        # TODO: Implement getOutbound method
        pass

    def getInbound(self) -> SmmRelationship:
        # TODO: Implement getInbound method
        pass

class smm_MofElement:

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

    def __init__(self, isBaseSupplied: str, value: str, from71: "smm_RankingMeasurementRelationship" = None, Grade: "smm_RankingMeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.value = value
        self.from71 = from71
        self.Grade = Grade
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

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
            if hasattr(old_value, "rankingTo168"):
                opp_val = getattr(old_value, "rankingTo168", None)
                if opp_val == self:
                    setattr(old_value, "rankingTo168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankingTo168"):
                opp_val = getattr(value, "rankingTo168", None)
                setattr(value, "rankingTo168", self)

    @property
    def from71(self):
        return self.__from71

    @from71.setter
    def from71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Grade__from71", None)
        self.__from71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RankingMeasurementRelationship72"):
                opp_val = getattr(old_value, "RankingMeasurementRelationship72", None)
                if opp_val == self:
                    setattr(old_value, "RankingMeasurementRelationship72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RankingMeasurementRelationship72"):
                opp_val = getattr(value, "RankingMeasurementRelationship72", None)
                setattr(value, "RankingMeasurementRelationship72", self)

class Measure:

    pass
class smm_Ranking(Measure):

    pass
class AbstractMeasureElement:

    pass
class smm_Measure(AbstractMeasureElement):

    def __init__(self, measureLabelFormat: str, measurementLabelFormat: str, visible: str, categoryMeasure: set["smm_MeasureCategory"] = None, smm_Measure: "smm_Characteristic" = None, smm_Measure77: "smm_Scope" = None, from79: set["smm_RefinementMeasureRelationship"] = None, to81: set["smm_RefinementMeasureRelationship"] = None, from84: set["smm_EquivalentMeasureRelationship"] = None, to86: set["smm_EquivalentMeasureRelationship"] = None, from89: "smm_RecursiveMeasureRelationship" = None, to91: "smm_RecursiveMeasureRelationship" = None, smm_Measure94: set["smm_MeasureRelationship"] = None, Measure: "smm_EquivalentMeasureRelationship" = None, Measure64: "smm_EquivalentMeasureRelationship" = None, smm_Measure99: set["smm_MeasureRelationship"] = None, smm_Measure102: set["smm_MeasureRelationship"] = None, Measure112: "smm_MeasureCategory" = None, smm_Measure96: "smm_Operation" = None, Measure173: "smm_RecursiveMeasureRelationship" = None, Measure175: "smm_RecursiveMeasureRelationship" = None, smm_Measure156: "smm_ObservedMeasure" = None, Measure185: "smm_RefinementMeasureRelationship" = None, Measure183: "smm_RefinementMeasureRelationship" = None):
        self.measureLabelFormat = measureLabelFormat
        self.measurementLabelFormat = measurementLabelFormat
        self.visible = visible
        self.categoryMeasure = categoryMeasure if categoryMeasure is not None else set()
        self.smm_Measure = smm_Measure
        self.smm_Measure77 = smm_Measure77
        self.from79 = from79 if from79 is not None else set()
        self.to81 = to81 if to81 is not None else set()
        self.from84 = from84 if from84 is not None else set()
        self.to86 = to86 if to86 is not None else set()
        self.from89 = from89
        self.to91 = to91
        self.smm_Measure94 = smm_Measure94 if smm_Measure94 is not None else set()
        self.Measure = Measure
        self.Measure64 = Measure64
        self.smm_Measure99 = smm_Measure99 if smm_Measure99 is not None else set()
        self.smm_Measure102 = smm_Measure102 if smm_Measure102 is not None else set()
        self.Measure112 = Measure112
        self.smm_Measure96 = smm_Measure96
        self.Measure173 = Measure173
        self.Measure175 = Measure175
        self.smm_Measure156 = smm_Measure156
        self.Measure185 = Measure185
        self.Measure183 = Measure183
        
    @property
    def measureLabelFormat(self) -> str:
        return self.__measureLabelFormat

    @measureLabelFormat.setter
    def measureLabelFormat(self, measureLabelFormat: str):
        self.__measureLabelFormat = measureLabelFormat

    @property
    def measurementLabelFormat(self) -> str:
        return self.__measurementLabelFormat

    @measurementLabelFormat.setter
    def measurementLabelFormat(self, measurementLabelFormat: str):
        self.__measurementLabelFormat = measurementLabelFormat

    @property
    def visible(self) -> str:
        return self.__visible

    @visible.setter
    def visible(self, visible: str):
        self.__visible = visible

    @property
    def smm_Measure96(self):
        return self.__smm_Measure96

    @smm_Measure96.setter
    def smm_Measure96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure96", None)
        self.__smm_Measure96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation97"):
                opp_val = getattr(old_value, "smm_Operation97", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation97"):
                opp_val = getattr(value, "smm_Operation97", None)
                setattr(value, "smm_Operation97", self)

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
    def smm_Measure94(self):
        return self.__smm_Measure94

    @smm_Measure94.setter
    def smm_Measure94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure94", None)
        self.__smm_Measure94 = value if value is not None else set()
        
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

    @property
    def from84(self):
        return self.__from84

    @from84.setter
    def from84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from84", None)
        self.__from84 = value if value is not None else set()
        
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
    def smm_Measure156(self):
        return self.__smm_Measure156

    @smm_Measure156.setter
    def smm_Measure156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure156", None)
        self.__smm_Measure156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_ObservedMeasure155"):
                opp_val = getattr(old_value, "smm_ObservedMeasure155", None)
                if opp_val == self:
                    setattr(old_value, "smm_ObservedMeasure155", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_ObservedMeasure155"):
                opp_val = getattr(value, "smm_ObservedMeasure155", None)
                setattr(value, "smm_ObservedMeasure155", self)

    @property
    def smm_Measure77(self):
        return self.__smm_Measure77

    @smm_Measure77.setter
    def smm_Measure77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure77", None)
        self.__smm_Measure77 = value
        
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
    def to86(self):
        return self.__to86

    @to86.setter
    def to86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to86", None)
        self.__to86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EquivalentMeasureRelationship87"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship87", None)
                    
                    if opp_val == self:
                        setattr(item, "EquivalentMeasureRelationship87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EquivalentMeasureRelationship87"):
                    opp_val = getattr(item, "EquivalentMeasureRelationship87", None)
                    
                    setattr(item, "EquivalentMeasureRelationship87", self)
                    

    @property
    def from89(self):
        return self.__from89

    @from89.setter
    def from89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from89", None)
        self.__from89 = value
        
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
    def Measure64(self):
        return self.__Measure64

    @Measure64.setter
    def Measure64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure64", None)
        self.__Measure64 = value
        
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
    def to91(self):
        return self.__to91

    @to91.setter
    def to91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to91", None)
        self.__to91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecursiveMeasureRelationship92"):
                opp_val = getattr(old_value, "RecursiveMeasureRelationship92", None)
                if opp_val == self:
                    setattr(old_value, "RecursiveMeasureRelationship92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecursiveMeasureRelationship92"):
                opp_val = getattr(value, "RecursiveMeasureRelationship92", None)
                setattr(value, "RecursiveMeasureRelationship92", self)

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
    def Measure173(self):
        return self.__Measure173

    @Measure173.setter
    def Measure173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure173", None)
        self.__Measure173 = value
        
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
    def Measure175(self):
        return self.__Measure175

    @Measure175.setter
    def Measure175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure175", None)
        self.__Measure175 = value
        
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
    def Measure183(self):
        return self.__Measure183

    @Measure183.setter
    def Measure183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure183", None)
        self.__Measure183 = value
        
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
    def from79(self):
        return self.__from79

    @from79.setter
    def from79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__from79", None)
        self.__from79 = value if value is not None else set()
        
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
    def to81(self):
        return self.__to81

    @to81.setter
    def to81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__to81", None)
        self.__to81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RefinementMeasureRelationship82"):
                    opp_val = getattr(item, "RefinementMeasureRelationship82", None)
                    
                    if opp_val == self:
                        setattr(item, "RefinementMeasureRelationship82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RefinementMeasureRelationship82"):
                    opp_val = getattr(item, "RefinementMeasureRelationship82", None)
                    
                    setattr(item, "RefinementMeasureRelationship82", self)
                    

    @property
    def Measure185(self):
        return self.__Measure185

    @Measure185.setter
    def Measure185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__Measure185", None)
        self.__Measure185 = value
        
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
    def smm_Measure99(self):
        return self.__smm_Measure99

    @smm_Measure99.setter
    def smm_Measure99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure99", None)
        self.__smm_Measure99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship100"):
                    opp_val = getattr(item, "smm_MeasureRelationship100", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship100"):
                    opp_val = getattr(item, "smm_MeasureRelationship100", None)
                    
                    setattr(item, "smm_MeasureRelationship100", self)
                    

    @property
    def smm_Measure102(self):
        return self.__smm_Measure102

    @smm_Measure102.setter
    def smm_Measure102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measure__smm_Measure102", None)
        self.__smm_Measure102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasureRelationship103"):
                    opp_val = getattr(item, "smm_MeasureRelationship103", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasureRelationship103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasureRelationship103"):
                    opp_val = getattr(item, "smm_MeasureRelationship103", None)
                    
                    setattr(item, "smm_MeasureRelationship103", self)
                    

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
            if hasattr(old_value, "smm_Characteristic75"):
                opp_val = getattr(old_value, "smm_Characteristic75", None)
                if opp_val == self:
                    setattr(old_value, "smm_Characteristic75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Characteristic75"):
                opp_val = getattr(value, "smm_Characteristic75", None)
                setattr(value, "smm_Characteristic75", self)

    def getAllArguments(self) -> str:
        # TODO: Implement getAllArguments method
        pass

    def getArguments(self) -> str:
        # TODO: Implement getArguments method
        pass

class smm_Scope(AbstractMeasureElement):

    def __init__(self, class: str, smm_Scope: "smm_Measure" = None, smm_Scope207: "smm_Operation" = None, smm_Scope210: "smm_Operation" = None):
        self.class = class
        self.smm_Scope = smm_Scope
        self.smm_Scope207 = smm_Scope207
        self.smm_Scope210 = smm_Scope210
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

    @property
    def smm_Scope207(self):
        return self.__smm_Scope207

    @smm_Scope207.setter
    def smm_Scope207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope207", None)
        self.__smm_Scope207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation208"):
                opp_val = getattr(old_value, "smm_Operation208", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation208"):
                opp_val = getattr(value, "smm_Operation208", None)
                setattr(value, "smm_Operation208", self)

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
            if hasattr(old_value, "smm_Measure77"):
                opp_val = getattr(old_value, "smm_Measure77", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure77"):
                opp_val = getattr(value, "smm_Measure77", None)
                setattr(value, "smm_Measure77", self)

    @property
    def smm_Scope210(self):
        return self.__smm_Scope210

    @smm_Scope210.setter
    def smm_Scope210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Scope__smm_Scope210", None)
        self.__smm_Scope210 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Operation211"):
                opp_val = getattr(old_value, "smm_Operation211", None)
                if opp_val == self:
                    setattr(old_value, "smm_Operation211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Operation211"):
                opp_val = getattr(value, "smm_Operation211", None)
                setattr(value, "smm_Operation211", self)

class smm_Operation(AbstractMeasureElement):

    def __init__(self, language: str, body: str, smm_Operation: "smm_DirectMeasure" = None, smm_Operation61: "smm_EquivalentMeasureRelationship" = None, smm_Operation120: "smm_MeasureRelationship" = None, smm_Operation97: "smm_Measure" = None, smm_Operation208: "smm_Scope" = None, smm_Operation211: "smm_Scope" = None):
        self.language = language
        self.body = body
        self.smm_Operation = smm_Operation
        self.smm_Operation61 = smm_Operation61
        self.smm_Operation120 = smm_Operation120
        self.smm_Operation97 = smm_Operation97
        self.smm_Operation208 = smm_Operation208
        self.smm_Operation211 = smm_Operation211
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def smm_Operation61(self):
        return self.__smm_Operation61

    @smm_Operation61.setter
    def smm_Operation61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation61", None)
        self.__smm_Operation61 = value
        
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
    def smm_Operation208(self):
        return self.__smm_Operation208

    @smm_Operation208.setter
    def smm_Operation208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation208", None)
        self.__smm_Operation208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope207"):
                opp_val = getattr(old_value, "smm_Scope207", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope207"):
                opp_val = getattr(value, "smm_Scope207", None)
                setattr(value, "smm_Scope207", self)

    @property
    def smm_Operation211(self):
        return self.__smm_Operation211

    @smm_Operation211.setter
    def smm_Operation211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation211", None)
        self.__smm_Operation211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Scope210"):
                opp_val = getattr(old_value, "smm_Scope210", None)
                if opp_val == self:
                    setattr(old_value, "smm_Scope210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Scope210"):
                opp_val = getattr(value, "smm_Scope210", None)
                setattr(value, "smm_Scope210", self)

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
    def smm_Operation97(self):
        return self.__smm_Operation97

    @smm_Operation97.setter
    def smm_Operation97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Operation__smm_Operation97", None)
        self.__smm_Operation97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measure96"):
                opp_val = getattr(old_value, "smm_Measure96", None)
                if opp_val == self:
                    setattr(old_value, "smm_Measure96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measure96"):
                opp_val = getattr(value, "smm_Measure96", None)
                setattr(value, "smm_Measure96", self)

    def getParamStrings(self) -> str:
        # TODO: Implement getParamStrings method
        pass

class smm_OCLOperation(AbstractMeasureElement):

    def __init__(self, context: str, body: str):
        self.context = context
        self.body = body
        
    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

class smm_Characteristic(AbstractMeasureElement):

    pass
class smm_MeasureCategory(AbstractMeasureElement):

    pass
class SmmRelationship:

    pass
class smm_MeasureRelationship(SmmRelationship):

    pass
class smm_ObservedMeasure(SmmRelationship):

    pass
class smm_MeasurementRelationship(SmmRelationship):

    def __init__(self, smm_MeasurementRelationship: "smm_Measurement" = None, smm_MeasurementRelationship141: "smm_Measurement" = None, smm_MeasurementRelationship144: "smm_Measurement" = None):
        self.smm_MeasurementRelationship = smm_MeasurementRelationship
        self.smm_MeasurementRelationship141 = smm_MeasurementRelationship141
        self.smm_MeasurementRelationship144 = smm_MeasurementRelationship144
        
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

    @property
    def smm_MeasurementRelationship141(self):
        return self.__smm_MeasurementRelationship141

    @smm_MeasurementRelationship141.setter
    def smm_MeasurementRelationship141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__smm_MeasurementRelationship141", None)
        self.__smm_MeasurementRelationship141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measurement140"):
                opp_val = getattr(old_value, "smm_Measurement140", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measurement140"):
                opp_val = getattr(value, "smm_Measurement140", None)
                if opp_val is None:
                    setattr(value, "smm_Measurement140", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smm_MeasurementRelationship144(self):
        return self.__smm_MeasurementRelationship144

    @smm_MeasurementRelationship144.setter
    def smm_MeasurementRelationship144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasurementRelationship__smm_MeasurementRelationship144", None)
        self.__smm_MeasurementRelationship144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Measurement143"):
                opp_val = getattr(old_value, "smm_Measurement143", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Measurement143"):
                opp_val = getattr(value, "smm_Measurement143", None)
                if opp_val is None:
                    setattr(value, "smm_Measurement143", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getTo(self) -> Measurement:
        # TODO: Implement getTo method
        pass

    def getFrom(self) -> Measurement:
        # TODO: Implement getFrom method
        pass

class smm_CategoryRelationship(SmmRelationship):

    pass
class DimensionalMeasurement:

    pass
class smm_RescaledMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, to199: set["smm_RescaleMeasurementRelationship"] = None, RescaledMeasurement: "smm_RescaleMeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.to199 = to199 if to199 is not None else set()
        self.RescaledMeasurement = RescaledMeasurement
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

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
            if hasattr(old_value, "rescaleFrom202"):
                opp_val = getattr(old_value, "rescaleFrom202", None)
                if opp_val == self:
                    setattr(old_value, "rescaleFrom202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleFrom202"):
                opp_val = getattr(value, "rescaleFrom202", None)
                setattr(value, "rescaleFrom202", self)

    @property
    def to199(self):
        return self.__to199

    @to199.setter
    def to199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasurement__to199", None)
        self.__to199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasurementRelationship200"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship200", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasurementRelationship200", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasurementRelationship200"):
                    opp_val = getattr(item, "RescaleMeasurementRelationship200", None)
                    
                    setattr(item, "RescaleMeasurementRelationship200", self)
                    

class smm_DirectMeasurement(DimensionalMeasurement):

    pass
class smm_NamedMeasurement(DimensionalMeasurement):

    pass
class DimensionalMeasure:

    pass
class smm_RescaledMeasure(DimensionalMeasure):

    def __init__(self, formula: str, to193: set["smm_RescaleMeasureRelationship"] = None, RescaledMeasure: "smm_RescaleMeasureRelationship" = None):
        self.formula = formula
        self.to193 = to193 if to193 is not None else set()
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
    def to193(self):
        return self.__to193

    @to193.setter
    def to193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RescaledMeasure__to193", None)
        self.__to193 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasureRelationship194"):
                    opp_val = getattr(item, "RescaleMeasureRelationship194", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasureRelationship194", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasureRelationship194"):
                    opp_val = getattr(item, "RescaleMeasureRelationship194", None)
                    
                    setattr(item, "RescaleMeasureRelationship194", self)
                    

class smm_DirectMeasure(DimensionalMeasure):

    pass
class smm_CollectiveMeasure(DimensionalMeasure):

    def __init__(self, accumulator: str, from31: set["smm_BaseMeasureRelationship"] = None, CollectiveMeasure: "smm_BaseMeasureRelationship" = None):
        self.accumulator = accumulator
        self.from31 = from31 if from31 is not None else set()
        self.CollectiveMeasure = CollectiveMeasure
        
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
    def from31(self):
        return self.__from31

    @from31.setter
    def from31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasure__from31", None)
        self.__from31 = value if value is not None else set()
        
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
                    

class smm_NamedMeasure(DimensionalMeasure):

    pass
class smm_CollectiveMeasurement(DimensionalMeasurement):

    def __init__(self, accumulator: str, isBaseSupplied: str, CollectiveMeasurement: "smm_BaseMeasurementRelationship" = None, from33: set["smm_BaseMeasurementRelationship"] = None):
        self.accumulator = accumulator
        self.isBaseSupplied = isBaseSupplied
        self.CollectiveMeasurement = CollectiveMeasurement
        self.from33 = from33 if from33 is not None else set()
        
    @property
    def accumulator(self) -> str:
        return self.__accumulator

    @accumulator.setter
    def accumulator(self, accumulator: str):
        self.__accumulator = accumulator

    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

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

    @property
    def from33(self):
        return self.__from33

    @from33.setter
    def from33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_CollectiveMeasurement__from33", None)
        self.__from33 = value if value is not None else set()
        
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
                    

class SmmElement:

    pass
class smm_MeasureLibrary(SmmElement):

    def __init__(self, smm_MeasureLibrary: set["smm_AbstractMeasureElement"] = None, smm_MeasureLibrary116: set["smm_CategoryRelationship"] = None, smm_MeasureLibrary220: "smm_SmmModel" = None):
        self.smm_MeasureLibrary = smm_MeasureLibrary if smm_MeasureLibrary is not None else set()
        self.smm_MeasureLibrary116 = smm_MeasureLibrary116 if smm_MeasureLibrary116 is not None else set()
        self.smm_MeasureLibrary220 = smm_MeasureLibrary220
        
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
    def smm_MeasureLibrary220(self):
        return self.__smm_MeasureLibrary220

    @smm_MeasureLibrary220.setter
    def smm_MeasureLibrary220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_MeasureLibrary__smm_MeasureLibrary220", None)
        self.__smm_MeasureLibrary220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_SmmModel219"):
                opp_val = getattr(old_value, "smm_SmmModel219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmModel219"):
                opp_val = getattr(value, "smm_SmmModel219", None)
                if opp_val is None:
                    setattr(value, "smm_SmmModel219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getOclOperations(self) -> AbstractMeasureElement:
        # TODO: Implement getOclOperations method
        pass

    def getOperations(self) -> AbstractMeasureElement:
        # TODO: Implement getOperations method
        pass

class smm_Observation(SmmElement):

    def __init__(self, observer: str, tool: str, whenObserved: str, smm_Observation: set["smm_ObservationScope"] = None, smm_Observation147: set["smm_ObservedMeasure"] = None, smm_Observation149: set["smm_SmmElement"] = None, smm_Observation151: set["smm_SmmRelationship"] = None, smm_Observation153: set["smm_Argument"] = None, smm_Observation217: "smm_SmmModel" = None):
        self.observer = observer
        self.tool = tool
        self.whenObserved = whenObserved
        self.smm_Observation = smm_Observation if smm_Observation is not None else set()
        self.smm_Observation147 = smm_Observation147 if smm_Observation147 is not None else set()
        self.smm_Observation149 = smm_Observation149 if smm_Observation149 is not None else set()
        self.smm_Observation151 = smm_Observation151 if smm_Observation151 is not None else set()
        self.smm_Observation153 = smm_Observation153 if smm_Observation153 is not None else set()
        self.smm_Observation217 = smm_Observation217
        
    @property
    def observer(self) -> str:
        return self.__observer

    @observer.setter
    def observer(self, observer: str):
        self.__observer = observer

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
    def smm_Observation153(self):
        return self.__smm_Observation153

    @smm_Observation153.setter
    def smm_Observation153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation153", None)
        self.__smm_Observation153 = value if value is not None else set()
        
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
    def smm_Observation149(self):
        return self.__smm_Observation149

    @smm_Observation149.setter
    def smm_Observation149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation149", None)
        self.__smm_Observation149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_SmmElement"):
                    opp_val = getattr(item, "smm_SmmElement", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_SmmElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_SmmElement"):
                    opp_val = getattr(item, "smm_SmmElement", None)
                    
                    setattr(item, "smm_SmmElement", self)
                    

    @property
    def smm_Observation151(self):
        return self.__smm_Observation151

    @smm_Observation151.setter
    def smm_Observation151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation151", None)
        self.__smm_Observation151 = value if value is not None else set()
        
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
    def smm_Observation147(self):
        return self.__smm_Observation147

    @smm_Observation147.setter
    def smm_Observation147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation147", None)
        self.__smm_Observation147 = value if value is not None else set()
        
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
    def smm_Observation217(self):
        return self.__smm_Observation217

    @smm_Observation217.setter
    def smm_Observation217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Observation__smm_Observation217", None)
        self.__smm_Observation217 = value
        
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

    def __init__(self, maximumEndpoint: str, maximumOpen: str, minimumEndpoint: str, minimumOpen: str, symbol: str, smm_RankingInterval: "smm_Ranking" = None):
        self.maximumEndpoint = maximumEndpoint
        self.maximumOpen = maximumOpen
        self.minimumEndpoint = minimumEndpoint
        self.minimumOpen = minimumOpen
        self.symbol = symbol
        self.smm_RankingInterval = smm_RankingInterval
        
    @property
    def minimumOpen(self) -> str:
        return self.__minimumOpen

    @minimumOpen.setter
    def minimumOpen(self, minimumOpen: str):
        self.__minimumOpen = minimumOpen

    @property
    def minimumEndpoint(self) -> str:
        return self.__minimumEndpoint

    @minimumEndpoint.setter
    def minimumEndpoint(self, minimumEndpoint: str):
        self.__minimumEndpoint = minimumEndpoint

    @property
    def maximumOpen(self) -> str:
        return self.__maximumOpen

    @maximumOpen.setter
    def maximumOpen(self, maximumOpen: str):
        self.__maximumOpen = maximumOpen

    @property
    def symbol(self) -> str:
        return self.__symbol

    @symbol.setter
    def symbol(self, symbol: str):
        self.__symbol = symbol

    @property
    def maximumEndpoint(self) -> str:
        return self.__maximumEndpoint

    @maximumEndpoint.setter
    def maximumEndpoint(self, maximumEndpoint: str):
        self.__maximumEndpoint = maximumEndpoint

    @property
    def smm_RankingInterval(self):
        return self.__smm_RankingInterval

    @smm_RankingInterval.setter
    def smm_RankingInterval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_RankingInterval__smm_RankingInterval", None)
        self.__smm_RankingInterval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_Ranking"):
                opp_val = getattr(old_value, "smm_Ranking", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Ranking"):
                opp_val = getattr(value, "smm_Ranking", None)
                if opp_val is None:
                    setattr(value, "smm_Ranking", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "smm_Observation151"):
                opp_val = getattr(old_value, "smm_Observation151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation151"):
                opp_val = getattr(value, "smm_Observation151", None)
                if opp_val is None:
                    setattr(value, "smm_Observation151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getTo(self) -> SmmElement:
        # TODO: Implement getTo method
        pass

    def getFrom(self) -> SmmElement:
        # TODO: Implement getFrom method
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

class smm_Measurement(SmmElement):

    def __init__(self, error: str, breakValue: str, Measurement69: "smm_EquivalentMeasurementRelationship" = None, Measurement: "smm_EquivalentMeasurementRelationship" = None, from128: set["smm_EquivalentMeasurementRelationship"] = None, to130: set["smm_EquivalentMeasurementRelationship"] = None, from133: "smm_RecursiveMeasurementRelationship" = None, to135: "smm_RecursiveMeasurementRelationship" = None, smm_Measurement138: set["smm_MeasurementRelationship"] = None, smm_Measurement140: set["smm_MeasurementRelationship"] = None, smm_Measurement143: set["smm_MeasurementRelationship"] = None, smm_Measurement: "smm_MofElement" = None, from123: set["smm_RefinementMeasurementRelationship"] = None, to125: set["smm_RefinementMeasurementRelationship"] = None, smm_Measurement159: "smm_ObservedMeasure" = None, Measurement188: "smm_RefinementMeasurementRelationship" = None, Measurement191: "smm_RefinementMeasurementRelationship" = None, Measurement178: "smm_RecursiveMeasurementRelationship" = None, Measurement181: "smm_RecursiveMeasurementRelationship" = None):
        self.error = error
        self.breakValue = breakValue
        self.Measurement69 = Measurement69
        self.Measurement = Measurement
        self.from128 = from128 if from128 is not None else set()
        self.to130 = to130 if to130 is not None else set()
        self.from133 = from133
        self.to135 = to135
        self.smm_Measurement138 = smm_Measurement138 if smm_Measurement138 is not None else set()
        self.smm_Measurement140 = smm_Measurement140 if smm_Measurement140 is not None else set()
        self.smm_Measurement143 = smm_Measurement143 if smm_Measurement143 is not None else set()
        self.smm_Measurement = smm_Measurement
        self.from123 = from123 if from123 is not None else set()
        self.to125 = to125 if to125 is not None else set()
        self.smm_Measurement159 = smm_Measurement159
        self.Measurement188 = Measurement188
        self.Measurement191 = Measurement191
        self.Measurement178 = Measurement178
        self.Measurement181 = Measurement181
        
    @property
    def error(self) -> str:
        return self.__error

    @error.setter
    def error(self, error: str):
        self.__error = error

    @property
    def breakValue(self) -> str:
        return self.__breakValue

    @breakValue.setter
    def breakValue(self, breakValue: str):
        self.__breakValue = breakValue

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
    def Measurement178(self):
        return self.__Measurement178

    @Measurement178.setter
    def Measurement178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement178", None)
        self.__Measurement178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveTo177"):
                opp_val = getattr(old_value, "recursiveTo177", None)
                if opp_val == self:
                    setattr(old_value, "recursiveTo177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveTo177"):
                opp_val = getattr(value, "recursiveTo177", None)
                setattr(value, "recursiveTo177", self)

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
    def Measurement69(self):
        return self.__Measurement69

    @Measurement69.setter
    def Measurement69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement69", None)
        self.__Measurement69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "equivalentFrom68"):
                opp_val = getattr(old_value, "equivalentFrom68", None)
                if opp_val == self:
                    setattr(old_value, "equivalentFrom68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentFrom68"):
                opp_val = getattr(value, "equivalentFrom68", None)
                setattr(value, "equivalentFrom68", self)

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
            if hasattr(old_value, "equivalentTo66"):
                opp_val = getattr(old_value, "equivalentTo66", None)
                if opp_val == self:
                    setattr(old_value, "equivalentTo66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "equivalentTo66"):
                opp_val = getattr(value, "equivalentTo66", None)
                setattr(value, "equivalentTo66", self)

    @property
    def smm_Measurement159(self):
        return self.__smm_Measurement159

    @smm_Measurement159.setter
    def smm_Measurement159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement159", None)
        self.__smm_Measurement159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_ObservedMeasure158"):
                opp_val = getattr(old_value, "smm_ObservedMeasure158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_ObservedMeasure158"):
                opp_val = getattr(value, "smm_ObservedMeasure158", None)
                if opp_val is None:
                    setattr(value, "smm_ObservedMeasure158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def to135(self):
        return self.__to135

    @to135.setter
    def to135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__to135", None)
        self.__to135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RecursiveMeasurementRelationship136"):
                opp_val = getattr(old_value, "RecursiveMeasurementRelationship136", None)
                if opp_val == self:
                    setattr(old_value, "RecursiveMeasurementRelationship136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RecursiveMeasurementRelationship136"):
                opp_val = getattr(value, "RecursiveMeasurementRelationship136", None)
                setattr(value, "RecursiveMeasurementRelationship136", self)

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
    def smm_Measurement143(self):
        return self.__smm_Measurement143

    @smm_Measurement143.setter
    def smm_Measurement143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement143", None)
        self.__smm_Measurement143 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship144"):
                    opp_val = getattr(item, "smm_MeasurementRelationship144", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship144", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship144"):
                    opp_val = getattr(item, "smm_MeasurementRelationship144", None)
                    
                    setattr(item, "smm_MeasurementRelationship144", self)
                    

    @property
    def smm_Measurement140(self):
        return self.__smm_Measurement140

    @smm_Measurement140.setter
    def smm_Measurement140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement140", None)
        self.__smm_Measurement140 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smm_MeasurementRelationship141"):
                    opp_val = getattr(item, "smm_MeasurementRelationship141", None)
                    
                    if opp_val == self:
                        setattr(item, "smm_MeasurementRelationship141", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smm_MeasurementRelationship141"):
                    opp_val = getattr(item, "smm_MeasurementRelationship141", None)
                    
                    setattr(item, "smm_MeasurementRelationship141", self)
                    

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
    def smm_Measurement(self):
        return self.__smm_Measurement

    @smm_Measurement.setter
    def smm_Measurement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__smm_Measurement", None)
        self.__smm_Measurement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smm_MofElement"):
                opp_val = getattr(old_value, "smm_MofElement", None)
                if opp_val == self:
                    setattr(old_value, "smm_MofElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_MofElement"):
                opp_val = getattr(value, "smm_MofElement", None)
                setattr(value, "smm_MofElement", self)

    @property
    def Measurement191(self):
        return self.__Measurement191

    @Measurement191.setter
    def Measurement191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement191", None)
        self.__Measurement191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementFrom190"):
                opp_val = getattr(old_value, "refinementFrom190", None)
                if opp_val == self:
                    setattr(old_value, "refinementFrom190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementFrom190"):
                opp_val = getattr(value, "refinementFrom190", None)
                setattr(value, "refinementFrom190", self)

    @property
    def Measurement181(self):
        return self.__Measurement181

    @Measurement181.setter
    def Measurement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement181", None)
        self.__Measurement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "recursiveFrom180"):
                opp_val = getattr(old_value, "recursiveFrom180", None)
                if opp_val == self:
                    setattr(old_value, "recursiveFrom180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "recursiveFrom180"):
                opp_val = getattr(value, "recursiveFrom180", None)
                setattr(value, "recursiveFrom180", self)

    @property
    def Measurement188(self):
        return self.__Measurement188

    @Measurement188.setter
    def Measurement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_Measurement__Measurement188", None)
        self.__Measurement188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refinementTo187"):
                opp_val = getattr(old_value, "refinementTo187", None)
                if opp_val == self:
                    setattr(old_value, "refinementTo187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refinementTo187"):
                opp_val = getattr(value, "refinementTo187", None)
                setattr(value, "refinementTo187", self)

    def getMeasurementLabel(self) -> str:
        # TODO: Implement getMeasurementLabel method
        pass

    def getMeasureLabel(self) -> str:
        # TODO: Implement getMeasureLabel method
        pass

class smm_SmmModel(SmmElement):

    pass
class smm_AbstractMeasureElement(SmmElement):

    pass
class smm_DimensionalMeasurement(Measurement):

    def __init__(self, value: str, DimensionalMeasurement: "smm_Base1MeasurementRelationship" = None, DimensionalMeasurement17: "smm_BaseMeasurementRelationship" = None, DimensionalMeasurement11: "smm_Base2MeasurementRelationship" = None, to47: set["smm_BaseMeasurementRelationship"] = None, to50: set["smm_Base1MeasurementRelationship"] = None, to53: set["smm_Base2MeasurementRelationship"] = None, from56: set["smm_RescaleMeasurementRelationship"] = None, to58: set["smm_RankingMeasurementRelationship"] = None, DimensionalMeasurement171: "smm_RankingMeasurementRelationship" = None, DimensionalMeasurement205: "smm_RescaleMeasurementRelationship" = None):
        self.value = value
        self.DimensionalMeasurement = DimensionalMeasurement
        self.DimensionalMeasurement17 = DimensionalMeasurement17
        self.DimensionalMeasurement11 = DimensionalMeasurement11
        self.to47 = to47 if to47 is not None else set()
        self.to50 = to50 if to50 is not None else set()
        self.to53 = to53 if to53 is not None else set()
        self.from56 = from56 if from56 is not None else set()
        self.to58 = to58 if to58 is not None else set()
        self.DimensionalMeasurement171 = DimensionalMeasurement171
        self.DimensionalMeasurement205 = DimensionalMeasurement205
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def DimensionalMeasurement17(self):
        return self.__DimensionalMeasurement17

    @DimensionalMeasurement17.setter
    def DimensionalMeasurement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement17", None)
        self.__DimensionalMeasurement17 = value
        
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
    def from56(self):
        return self.__from56

    @from56.setter
    def from56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__from56", None)
        self.__from56 = value if value is not None else set()
        
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
    def DimensionalMeasurement205(self):
        return self.__DimensionalMeasurement205

    @DimensionalMeasurement205.setter
    def DimensionalMeasurement205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement205", None)
        self.__DimensionalMeasurement205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rescaleTo204"):
                opp_val = getattr(old_value, "rescaleTo204", None)
                if opp_val == self:
                    setattr(old_value, "rescaleTo204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rescaleTo204"):
                opp_val = getattr(value, "rescaleTo204", None)
                setattr(value, "rescaleTo204", self)

    @property
    def to53(self):
        return self.__to53

    @to53.setter
    def to53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to53", None)
        self.__to53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base2MeasurementRelationship54"):
                    opp_val = getattr(item, "Base2MeasurementRelationship54", None)
                    
                    if opp_val == self:
                        setattr(item, "Base2MeasurementRelationship54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base2MeasurementRelationship54"):
                    opp_val = getattr(item, "Base2MeasurementRelationship54", None)
                    
                    setattr(item, "Base2MeasurementRelationship54", self)
                    

    @property
    def to58(self):
        return self.__to58

    @to58.setter
    def to58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to58", None)
        self.__to58 = value if value is not None else set()
        
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
    def DimensionalMeasurement11(self):
        return self.__DimensionalMeasurement11

    @DimensionalMeasurement11.setter
    def DimensionalMeasurement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement11", None)
        self.__DimensionalMeasurement11 = value
        
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
    def to47(self):
        return self.__to47

    @to47.setter
    def to47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to47", None)
        self.__to47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BaseMeasurementRelationship48"):
                    opp_val = getattr(item, "BaseMeasurementRelationship48", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasurementRelationship48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasurementRelationship48"):
                    opp_val = getattr(item, "BaseMeasurementRelationship48", None)
                    
                    setattr(item, "BaseMeasurementRelationship48", self)
                    

    @property
    def DimensionalMeasurement171(self):
        return self.__DimensionalMeasurement171

    @DimensionalMeasurement171.setter
    def DimensionalMeasurement171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__DimensionalMeasurement171", None)
        self.__DimensionalMeasurement171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rankingFrom170"):
                opp_val = getattr(old_value, "rankingFrom170", None)
                if opp_val == self:
                    setattr(old_value, "rankingFrom170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rankingFrom170"):
                opp_val = getattr(value, "rankingFrom170", None)
                setattr(value, "rankingFrom170", self)

    @property
    def to50(self):
        return self.__to50

    @to50.setter
    def to50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasurement__to50", None)
        self.__to50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base1MeasurementRelationship51"):
                    opp_val = getattr(item, "Base1MeasurementRelationship51", None)
                    
                    if opp_val == self:
                        setattr(item, "Base1MeasurementRelationship51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base1MeasurementRelationship51"):
                    opp_val = getattr(item, "Base1MeasurementRelationship51", None)
                    
                    setattr(item, "Base1MeasurementRelationship51", self)
                    

class smm_BinaryMeasurement(DimensionalMeasurement):

    def __init__(self, isBaseSupplied: str, BinaryMeasurement: "smm_Base1MeasurementRelationship" = None, from22: "smm_Base1MeasurementRelationship" = None, from24: "smm_Base2MeasurementRelationship" = None, BinaryMeasurement9: "smm_Base2MeasurementRelationship" = None):
        self.isBaseSupplied = isBaseSupplied
        self.BinaryMeasurement = BinaryMeasurement
        self.from22 = from22
        self.from24 = from24
        self.BinaryMeasurement9 = BinaryMeasurement9
        
    @property
    def isBaseSupplied(self) -> str:
        return self.__isBaseSupplied

    @isBaseSupplied.setter
    def isBaseSupplied(self, isBaseSupplied: str):
        self.__isBaseSupplied = isBaseSupplied

    @property
    def BinaryMeasurement9(self):
        return self.__BinaryMeasurement9

    @BinaryMeasurement9.setter
    def BinaryMeasurement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__BinaryMeasurement9", None)
        self.__BinaryMeasurement9 = value
        
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
    def from22(self):
        return self.__from22

    @from22.setter
    def from22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__from22", None)
        self.__from22 = value
        
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
    def from24(self):
        return self.__from24

    @from24.setter
    def from24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasurement__from24", None)
        self.__from24 = value
        
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

class MeasurementRelationship:

    pass
class smm_Base2MeasurementRelationship(MeasurementRelationship):

    pass
class smm_RescaleMeasurementRelationship(MeasurementRelationship):

    pass
class smm_BaseMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RefinementMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RankingMeasurementRelationship(MeasurementRelationship):

    pass
class smm_RecursiveMeasurementRelationship(MeasurementRelationship):

    pass
class smm_EquivalentMeasurementRelationship(MeasurementRelationship):

    pass
class smm_Base1MeasurementRelationship(MeasurementRelationship):

    pass
class smm_DimensionalMeasure(Measure):

    def __init__(self, unit: str, DimensionalMeasure: "smm_Base1MeasureRelationship" = None, DimensionalMeasure7: "smm_Base2MeasureRelationship" = None, DimensionalMeasure14: "smm_BaseMeasureRelationship" = None, to: set["smm_BaseMeasureRelationship"] = None, to37: set["smm_Base1MeasureRelationship"] = None, to40: set["smm_Base2MeasureRelationship"] = None, from43: set["smm_RescaleMeasureRelationship"] = None, to45: set["smm_RankingMeasureRelationship"] = None, DimensionalMeasure166: "smm_RankingMeasureRelationship" = None, DimensionalMeasure197: "smm_RescaleMeasureRelationship" = None):
        self.unit = unit
        self.DimensionalMeasure = DimensionalMeasure
        self.DimensionalMeasure7 = DimensionalMeasure7
        self.DimensionalMeasure14 = DimensionalMeasure14
        self.to = to if to is not None else set()
        self.to37 = to37 if to37 is not None else set()
        self.to40 = to40 if to40 is not None else set()
        self.from43 = from43 if from43 is not None else set()
        self.to45 = to45 if to45 is not None else set()
        self.DimensionalMeasure166 = DimensionalMeasure166
        self.DimensionalMeasure197 = DimensionalMeasure197
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def to45(self):
        return self.__to45

    @to45.setter
    def to45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to45", None)
        self.__to45 = value if value is not None else set()
        
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
    def to37(self):
        return self.__to37

    @to37.setter
    def to37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to37", None)
        self.__to37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base1MeasureRelationship38"):
                    opp_val = getattr(item, "Base1MeasureRelationship38", None)
                    
                    if opp_val == self:
                        setattr(item, "Base1MeasureRelationship38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base1MeasureRelationship38"):
                    opp_val = getattr(item, "Base1MeasureRelationship38", None)
                    
                    setattr(item, "Base1MeasureRelationship38", self)
                    

    @property
    def DimensionalMeasure166(self):
        return self.__DimensionalMeasure166

    @DimensionalMeasure166.setter
    def DimensionalMeasure166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure166", None)
        self.__DimensionalMeasure166 = value
        
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
    def DimensionalMeasure7(self):
        return self.__DimensionalMeasure7

    @DimensionalMeasure7.setter
    def DimensionalMeasure7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure7", None)
        self.__DimensionalMeasure7 = value
        
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
    def from43(self):
        return self.__from43

    @from43.setter
    def from43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__from43", None)
        self.__from43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RescaleMeasureRelationship"):
                    opp_val = getattr(item, "RescaleMeasureRelationship", None)
                    
                    if opp_val == self:
                        setattr(item, "RescaleMeasureRelationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RescaleMeasureRelationship"):
                    opp_val = getattr(item, "RescaleMeasureRelationship", None)
                    
                    setattr(item, "RescaleMeasureRelationship", self)
                    

    @property
    def DimensionalMeasure197(self):
        return self.__DimensionalMeasure197

    @DimensionalMeasure197.setter
    def DimensionalMeasure197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure197", None)
        self.__DimensionalMeasure197 = value
        
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
    def DimensionalMeasure14(self):
        return self.__DimensionalMeasure14

    @DimensionalMeasure14.setter
    def DimensionalMeasure14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__DimensionalMeasure14", None)
        self.__DimensionalMeasure14 = value
        
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
                if hasattr(item, "BaseMeasureRelationship35"):
                    opp_val = getattr(item, "BaseMeasureRelationship35", None)
                    
                    if opp_val == self:
                        setattr(item, "BaseMeasureRelationship35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BaseMeasureRelationship35"):
                    opp_val = getattr(item, "BaseMeasureRelationship35", None)
                    
                    setattr(item, "BaseMeasureRelationship35", self)
                    

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
    def to40(self):
        return self.__to40

    @to40.setter
    def to40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_DimensionalMeasure__to40", None)
        self.__to40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Base2MeasureRelationship41"):
                    opp_val = getattr(item, "Base2MeasureRelationship41", None)
                    
                    if opp_val == self:
                        setattr(item, "Base2MeasureRelationship41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Base2MeasureRelationship41"):
                    opp_val = getattr(item, "Base2MeasureRelationship41", None)
                    
                    setattr(item, "Base2MeasureRelationship41", self)
                    

class smm_BinaryMeasure(DimensionalMeasure):

    def __init__(self, functor: str, BinaryMeasure: "smm_Base1MeasureRelationship" = None, BinaryMeasure5: "smm_Base2MeasureRelationship" = None, from: "smm_Base1MeasureRelationship" = None, from20: "smm_Base2MeasureRelationship" = None):
        self.functor = functor
        self.BinaryMeasure = BinaryMeasure
        self.BinaryMeasure5 = BinaryMeasure5
        self.from = from
        self.from20 = from20
        
    @property
    def functor(self) -> str:
        return self.__functor

    @functor.setter
    def functor(self, functor: str):
        self.__functor = functor

    @property
    def from20(self):
        return self.__from20

    @from20.setter
    def from20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__from20", None)
        self.__from20 = value
        
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
    def BinaryMeasure5(self):
        return self.__BinaryMeasure5

    @BinaryMeasure5.setter
    def BinaryMeasure5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smm_BinaryMeasure__BinaryMeasure5", None)
        self.__BinaryMeasure5 = value
        
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

class MeasureRelationship:

    pass
class smm_RecursiveMeasureRelationship(MeasureRelationship):

    pass
class smm_Base2MeasureRelationship(MeasureRelationship):

    pass
class smm_RefinementMeasureRelationship(MeasureRelationship):

    pass
class smm_EquivalentMeasureRelationship(MeasureRelationship):

    pass
class smm_RescaleMeasureRelationship(MeasureRelationship):

    pass
class smm_RankingMeasureRelationship(MeasureRelationship):

    pass
class smm_BaseMeasureRelationship(MeasureRelationship):

    pass
class smm_Base1MeasureRelationship(MeasureRelationship):

    pass
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
            if hasattr(old_value, "smm_SmmElement213"):
                opp_val = getattr(old_value, "smm_SmmElement213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement213"):
                opp_val = getattr(value, "smm_SmmElement213", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smm_Argument(SmmElement):

    def __init__(self, type: str, value: str, smm_Argument: "smm_Observation" = None):
        self.type = type
        self.value = value
        self.smm_Argument = smm_Argument
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "smm_Observation153"):
                opp_val = getattr(old_value, "smm_Observation153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_Observation153"):
                opp_val = getattr(value, "smm_Observation153", None)
                if opp_val is None:
                    setattr(value, "smm_Observation153", set([self]))
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
            if hasattr(old_value, "smm_SmmElement215"):
                opp_val = getattr(old_value, "smm_SmmElement215", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smm_SmmElement215"):
                opp_val = getattr(value, "smm_SmmElement215", None)
                if opp_val is None:
                    setattr(value, "smm_SmmElement215", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
