from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Effect(Enum):
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
class Type(Enum):
    NONE = "NONE"
    FINDINGS = "FINDINGS"
    NUMBER = "NUMBER"


############################################
# Definition of Classes
############################################

class qm_Result(ABC):

    def __init__(self, message: str):
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

class EvaluationResult:

    pass
class qm_MultiMeasureEvaluationResult(EvaluationResult):

    pass
class qm_SingleMeasureEvaluationResult(EvaluationResult):

    def __init__(self, ratioAffected: float):
        self.ratioAffected = ratioAffected
        
    @property
    def ratioAffected(self) -> float:
        return self.__ratioAffected

    @ratioAffected.setter
    def ratioAffected(self, ratioAffected: float):
        self.__ratioAffected = ratioAffected

class qm_FindingMessage:

    def __init__(self, message: str, location: str, qm_FindingMessage: "qm_FindingsMeasurementResult" = None):
        self.message = message
        self.location = location
        self.qm_FindingMessage = qm_FindingMessage
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def qm_FindingMessage(self):
        return self.__qm_FindingMessage

    @qm_FindingMessage.setter
    def qm_FindingMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_FindingMessage__qm_FindingMessage", None)
        self.__qm_FindingMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_FindingsMeasurementResult"):
                opp_val = getattr(old_value, "qm_FindingsMeasurementResult", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_FindingsMeasurementResult"):
                opp_val = getattr(value, "qm_FindingsMeasurementResult", None)
                if opp_val is None:
                    setattr(value, "qm_FindingsMeasurementResult", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class qm_MeasureRankingEvaluationResult:

    def __init__(self, ratioAffected: float, qm_MeasureRankingEvaluationResult: "qm_MultiMeasureEvaluationResult" = None, qm_MeasureRankingEvaluationResult122: "qm_DoubleInterval" = None, qm_MeasureRankingEvaluationResult125: "qm_MeasureRanking" = None):
        self.ratioAffected = ratioAffected
        self.qm_MeasureRankingEvaluationResult = qm_MeasureRankingEvaluationResult
        self.qm_MeasureRankingEvaluationResult122 = qm_MeasureRankingEvaluationResult122
        self.qm_MeasureRankingEvaluationResult125 = qm_MeasureRankingEvaluationResult125
        
    @property
    def ratioAffected(self) -> float:
        return self.__ratioAffected

    @ratioAffected.setter
    def ratioAffected(self, ratioAffected: float):
        self.__ratioAffected = ratioAffected

    @property
    def qm_MeasureRankingEvaluationResult(self):
        return self.__qm_MeasureRankingEvaluationResult

    @qm_MeasureRankingEvaluationResult.setter
    def qm_MeasureRankingEvaluationResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureRankingEvaluationResult__qm_MeasureRankingEvaluationResult", None)
        self.__qm_MeasureRankingEvaluationResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MultiMeasureEvaluationResult"):
                opp_val = getattr(old_value, "qm_MultiMeasureEvaluationResult", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MultiMeasureEvaluationResult"):
                opp_val = getattr(value, "qm_MultiMeasureEvaluationResult", None)
                if opp_val is None:
                    setattr(value, "qm_MultiMeasureEvaluationResult", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qm_MeasureRankingEvaluationResult122(self):
        return self.__qm_MeasureRankingEvaluationResult122

    @qm_MeasureRankingEvaluationResult122.setter
    def qm_MeasureRankingEvaluationResult122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureRankingEvaluationResult__qm_MeasureRankingEvaluationResult122", None)
        self.__qm_MeasureRankingEvaluationResult122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_DoubleInterval123"):
                opp_val = getattr(old_value, "qm_DoubleInterval123", None)
                if opp_val == self:
                    setattr(old_value, "qm_DoubleInterval123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_DoubleInterval123"):
                opp_val = getattr(value, "qm_DoubleInterval123", None)
                setattr(value, "qm_DoubleInterval123", self)

    @property
    def qm_MeasureRankingEvaluationResult125(self):
        return self.__qm_MeasureRankingEvaluationResult125

    @qm_MeasureRankingEvaluationResult125.setter
    def qm_MeasureRankingEvaluationResult125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureRankingEvaluationResult__qm_MeasureRankingEvaluationResult125", None)
        self.__qm_MeasureRankingEvaluationResult125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MeasureRanking126"):
                opp_val = getattr(old_value, "qm_MeasureRanking126", None)
                if opp_val == self:
                    setattr(old_value, "qm_MeasureRanking126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MeasureRanking126"):
                opp_val = getattr(value, "qm_MeasureRanking126", None)
                setattr(value, "qm_MeasureRanking126", self)

class qm_MeasureEvaluation(ABC):

    def __init__(self, range: str, qm_MeasureEvaluation102: "qm_NormalizationMeasure" = None, qm_MeasureEvaluation104: "qm_Function" = None, qm_MeasureEvaluation: "qm_Measure" = None):
        self.range = range
        self.qm_MeasureEvaluation102 = qm_MeasureEvaluation102
        self.qm_MeasureEvaluation104 = qm_MeasureEvaluation104
        self.qm_MeasureEvaluation = qm_MeasureEvaluation
        
    @property
    def range(self) -> str:
        return self.__range

    @range.setter
    def range(self, range: str):
        self.__range = range

    @property
    def qm_MeasureEvaluation(self):
        return self.__qm_MeasureEvaluation

    @qm_MeasureEvaluation.setter
    def qm_MeasureEvaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureEvaluation__qm_MeasureEvaluation", None)
        self.__qm_MeasureEvaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Measure100"):
                opp_val = getattr(old_value, "qm_Measure100", None)
                if opp_val == self:
                    setattr(old_value, "qm_Measure100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Measure100"):
                opp_val = getattr(value, "qm_Measure100", None)
                setattr(value, "qm_Measure100", self)

    @property
    def qm_MeasureEvaluation102(self):
        return self.__qm_MeasureEvaluation102

    @qm_MeasureEvaluation102.setter
    def qm_MeasureEvaluation102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureEvaluation__qm_MeasureEvaluation102", None)
        self.__qm_MeasureEvaluation102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_NormalizationMeasure"):
                opp_val = getattr(old_value, "qm_NormalizationMeasure", None)
                if opp_val == self:
                    setattr(old_value, "qm_NormalizationMeasure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_NormalizationMeasure"):
                opp_val = getattr(value, "qm_NormalizationMeasure", None)
                setattr(value, "qm_NormalizationMeasure", self)

    @property
    def qm_MeasureEvaluation104(self):
        return self.__qm_MeasureEvaluation104

    @qm_MeasureEvaluation104.setter
    def qm_MeasureEvaluation104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_MeasureEvaluation__qm_MeasureEvaluation104", None)
        self.__qm_MeasureEvaluation104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Function"):
                opp_val = getattr(old_value, "qm_Function", None)
                if opp_val == self:
                    setattr(old_value, "qm_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Function"):
                opp_val = getattr(value, "qm_Function", None)
                setattr(value, "qm_Function", self)

class FormBasedMeasureAggregation:

    pass
class qm_NumberMeanMeasureAggregation(FormBasedMeasureAggregation):

    pass
class qm_FindingsUnionMeasureAggregation(FormBasedMeasureAggregation):

    pass
class FactorAggregation:

    pass
class qm_WeightedSumFactorAggregation(FactorAggregation):

    pass
class LinearFunction:

    pass
class qm_LinearDecreasingFunction(LinearFunction):

    pass
class qm_LinearIncreasingFunction(LinearFunction):

    pass
class qm_DoubleInterval:

    def __init__(self, lower: float, upper: float, qm_DoubleInterval: "qm_NumberMeasurementResult" = None, qm_DoubleInterval123: "qm_MeasureRankingEvaluationResult" = None, qm_DoubleInterval116: "qm_EvaluationResult" = None):
        self.lower = lower
        self.upper = upper
        self.qm_DoubleInterval = qm_DoubleInterval
        self.qm_DoubleInterval123 = qm_DoubleInterval123
        self.qm_DoubleInterval116 = qm_DoubleInterval116
        
    @property
    def lower(self) -> float:
        return self.__lower

    @lower.setter
    def lower(self, lower: float):
        self.__lower = lower

    @property
    def upper(self) -> float:
        return self.__upper

    @upper.setter
    def upper(self, upper: float):
        self.__upper = upper

    @property
    def qm_DoubleInterval116(self):
        return self.__qm_DoubleInterval116

    @qm_DoubleInterval116.setter
    def qm_DoubleInterval116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_DoubleInterval__qm_DoubleInterval116", None)
        self.__qm_DoubleInterval116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_EvaluationResult115"):
                opp_val = getattr(old_value, "qm_EvaluationResult115", None)
                if opp_val == self:
                    setattr(old_value, "qm_EvaluationResult115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_EvaluationResult115"):
                opp_val = getattr(value, "qm_EvaluationResult115", None)
                setattr(value, "qm_EvaluationResult115", self)

    @property
    def qm_DoubleInterval123(self):
        return self.__qm_DoubleInterval123

    @qm_DoubleInterval123.setter
    def qm_DoubleInterval123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_DoubleInterval__qm_DoubleInterval123", None)
        self.__qm_DoubleInterval123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MeasureRankingEvaluationResult122"):
                opp_val = getattr(old_value, "qm_MeasureRankingEvaluationResult122", None)
                if opp_val == self:
                    setattr(old_value, "qm_MeasureRankingEvaluationResult122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MeasureRankingEvaluationResult122"):
                opp_val = getattr(value, "qm_MeasureRankingEvaluationResult122", None)
                setattr(value, "qm_MeasureRankingEvaluationResult122", self)

    @property
    def qm_DoubleInterval(self):
        return self.__qm_DoubleInterval

    @qm_DoubleInterval.setter
    def qm_DoubleInterval(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_DoubleInterval__qm_DoubleInterval", None)
        self.__qm_DoubleInterval = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_NumberMeasurementResult"):
                opp_val = getattr(old_value, "qm_NumberMeasurementResult", None)
                if opp_val == self:
                    setattr(old_value, "qm_NumberMeasurementResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_NumberMeasurementResult"):
                opp_val = getattr(value, "qm_NumberMeasurementResult", None)
                setattr(value, "qm_NumberMeasurementResult", self)

class MeasurementResult:

    pass
class qm_FindingsMeasurementResult(MeasurementResult):

    def __init__(self, count: int, findings: str, qm_FindingsMeasurementResult: set["qm_FindingMessage"] = None):
        self.count = count
        self.findings = findings
        self.qm_FindingsMeasurementResult = qm_FindingsMeasurementResult if qm_FindingsMeasurementResult is not None else set()
        
    @property
    def findings(self) -> str:
        return self.__findings

    @findings.setter
    def findings(self, findings: str):
        self.__findings = findings

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def qm_FindingsMeasurementResult(self):
        return self.__qm_FindingsMeasurementResult

    @qm_FindingsMeasurementResult.setter
    def qm_FindingsMeasurementResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_FindingsMeasurementResult__qm_FindingsMeasurementResult", None)
        self.__qm_FindingsMeasurementResult = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_FindingMessage"):
                    opp_val = getattr(item, "qm_FindingMessage", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_FindingMessage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_FindingMessage"):
                    opp_val = getattr(item, "qm_FindingMessage", None)
                    
                    setattr(item, "qm_FindingMessage", self)
                    

class qm_NumberMeasurementResult(MeasurementResult):

    pass
class Result:

    pass
class qm_EvaluationResult(Result):

    pass
class qm_MeasurementResult(Result):

    pass
class qm_QualityModelResult:

    def __init__(self, system: str, date: date, qm_QualityModelResult: set["qm_MeasurementResult"] = None, qm_QualityModelResult108: set["qm_EvaluationResult"] = None):
        self.system = system
        self.date = date
        self.qm_QualityModelResult = qm_QualityModelResult if qm_QualityModelResult is not None else set()
        self.qm_QualityModelResult108 = qm_QualityModelResult108 if qm_QualityModelResult108 is not None else set()
        
    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def system(self) -> str:
        return self.__system

    @system.setter
    def system(self, system: str):
        self.__system = system

    @property
    def qm_QualityModelResult(self):
        return self.__qm_QualityModelResult

    @qm_QualityModelResult.setter
    def qm_QualityModelResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModelResult__qm_QualityModelResult", None)
        self.__qm_QualityModelResult = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_MeasurementResult"):
                    opp_val = getattr(item, "qm_MeasurementResult", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_MeasurementResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_MeasurementResult"):
                    opp_val = getattr(item, "qm_MeasurementResult", None)
                    
                    setattr(item, "qm_MeasurementResult", self)
                    

    @property
    def qm_QualityModelResult108(self):
        return self.__qm_QualityModelResult108

    @qm_QualityModelResult108.setter
    def qm_QualityModelResult108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModelResult__qm_QualityModelResult108", None)
        self.__qm_QualityModelResult108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_EvaluationResult"):
                    opp_val = getattr(item, "qm_EvaluationResult", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_EvaluationResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_EvaluationResult"):
                    opp_val = getattr(item, "qm_EvaluationResult", None)
                    
                    setattr(item, "qm_EvaluationResult", self)
                    

class MultiMeasureEvaluation:

    pass
class qm_WeightedSumMultiMeasureEvaluation(MultiMeasureEvaluation):

    pass
class qm_Ranking(ABC):

    def __init__(self, rank: int, weight: float):
        self.rank = rank
        self.weight = weight
        
    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def rank(self) -> int:
        return self.__rank

    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

class Instrument:

    pass
class qm_ToolBasedInstrument(Instrument):

    def __init__(self, metric: str, qm_ToolBasedInstrument: "qm_Tool" = None):
        self.metric = metric
        self.qm_ToolBasedInstrument = qm_ToolBasedInstrument
        
    @property
    def metric(self) -> str:
        return self.__metric

    @metric.setter
    def metric(self, metric: str):
        self.__metric = metric

    @property
    def qm_ToolBasedInstrument(self):
        return self.__qm_ToolBasedInstrument

    @qm_ToolBasedInstrument.setter
    def qm_ToolBasedInstrument(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_ToolBasedInstrument__qm_ToolBasedInstrument", None)
        self.__qm_ToolBasedInstrument = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Tool"):
                opp_val = getattr(old_value, "qm_Tool", None)
                if opp_val == self:
                    setattr(old_value, "qm_Tool", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Tool"):
                opp_val = getattr(value, "qm_Tool", None)
                setattr(value, "qm_Tool", self)

class MeasurementMethod:

    pass
class qm_Instrument(MeasurementMethod):

    pass
class qm_Function(ABC):

    pass
class Function:

    pass
class qm_LinearFunction(Function):

    def __init__(self, lowerBound: float, upperBound: float):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        
    @property
    def upperBound(self) -> float:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: float):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> float:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: float):
        self.__lowerBound = lowerBound

class Ranking:

    pass
class qm_FactorRanking(Ranking):

    pass
class MeasureAggregation:

    pass
class qm_FormBasedMeasureAggregation(MeasureAggregation):

    pass
class qm_TextAggregation(MeasureAggregation):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class TextAggregation:

    pass
class qm_QIESLAggregation(TextAggregation):

    pass
class Measure:

    pass
class qm_NormalizationMeasure(Measure):

    pass
class MeasureEvaluation:

    pass
class qm_MeasureRanking(MeasureEvaluation, Ranking):

    pass
class FormBasedEvaluation:

    pass
class qm_FactorAggregation(FormBasedEvaluation):

    pass
class qm_MultiMeasureEvaluation(FormBasedEvaluation):

    pass
class qm_SingleMeasureEvaluation(MeasureEvaluation, FormBasedEvaluation):

    pass
class Evaluation:

    pass
class qm_FormBasedEvaluation(Evaluation):

    pass
class qm_ManualEvaluation(Evaluation):

    pass
class qm_TextEvaluation(Evaluation):

    def __init__(self, specification: str):
        self.specification = specification
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

class TextEvaluation:

    pass
class qm_QIESLEvaluation(TextEvaluation):

    pass
class CharacterizingElement:

    pass
class QualityModelElement:

    pass
class qm_TaggedElement(QualityModelElement):

    pass
class qm_AnnotationBase(ABC):

    pass
class qm_Annotation:

    def __init__(self, key: str, value: str, qm_Annotation: "qm_AnnotatedElement" = None):
        self.key = key
        self.value = value
        self.qm_Annotation = qm_Annotation
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def qm_Annotation(self):
        return self.__qm_Annotation

    @qm_Annotation.setter
    def qm_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Annotation__qm_Annotation", None)
        self.__qm_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_AnnotatedElement"):
                opp_val = getattr(old_value, "qm_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_AnnotatedElement"):
                opp_val = getattr(value, "qm_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "qm_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TaggedElement:

    pass
class qm_AnnotatedElement(TaggedElement):

    pass
class DescribedElement:

    pass
class qm_NamedElement(DescribedElement):

    def __init__(self, name: str, title: str):
        self.name = name
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AnnotatedElement:

    pass
class qm_Decomposition(AnnotatedElement):

    pass
class qm_Impact(AnnotatedElement):

    def __init__(self, justification: str, effect: str, influences: "qm_Factor" = None, qm_Impact: "qm_Factor" = None, Impact: "qm_Factor" = None):
        self.justification = justification
        self.effect = effect
        self.influences = influences
        self.qm_Impact = qm_Impact
        self.Impact = Impact
        
    @property
    def justification(self) -> str:
        return self.__justification

    @justification.setter
    def justification(self, justification: str):
        self.__justification = justification

    @property
    def effect(self) -> str:
        return self.__effect

    @effect.setter
    def effect(self, effect: str):
        self.__effect = effect

    @property
    def influences(self):
        return self.__influences

    @influences.setter
    def influences(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Impact__influences", None)
        self.__influences = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Factor56"):
                opp_val = getattr(old_value, "Factor56", None)
                if opp_val == self:
                    setattr(old_value, "Factor56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Factor56"):
                opp_val = getattr(value, "Factor56", None)
                setattr(value, "Factor56", self)

    @property
    def Impact(self):
        return self.__Impact

    @Impact.setter
    def Impact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Impact__Impact", None)
        self.__Impact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qm_Impact(self):
        return self.__qm_Impact

    @qm_Impact.setter
    def qm_Impact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Impact__qm_Impact", None)
        self.__qm_Impact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Factor58"):
                opp_val = getattr(old_value, "qm_Factor58", None)
                if opp_val == self:
                    setattr(old_value, "qm_Factor58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Factor58"):
                opp_val = getattr(value, "qm_Factor58", None)
                setattr(value, "qm_Factor58", self)

class qm_Measurement(AnnotatedElement):

    pass
class qm_MeasureRefinement(AnnotatedElement):

    pass
class qm_Specialization(AnnotatedElement):

    pass
class qm_FactorRefinement(AnnotatedElement):

    pass
class qm_MeasurementMethod(AnnotatedElement):

    pass
class qm_DescribedElement(AnnotatedElement):

    def __init__(self, description: str):
        self.description = description
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class qm_QualityModelElement(ABC):

    def __init__(self, qualifiedName: str, qm_QualityModelElement: set["qm_Source"] = None):
        self.qualifiedName = qualifiedName
        self.qm_QualityModelElement = qm_QualityModelElement if qm_QualityModelElement is not None else set()
        
    @property
    def qualifiedName(self) -> str:
        return self.__qualifiedName

    @qualifiedName.setter
    def qualifiedName(self, qualifiedName: str):
        self.__qualifiedName = qualifiedName

    @property
    def qm_QualityModelElement(self):
        return self.__qm_QualityModelElement

    @qm_QualityModelElement.setter
    def qm_QualityModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModelElement__qm_QualityModelElement", None)
        self.__qm_QualityModelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_Source"):
                    opp_val = getattr(item, "qm_Source", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_Source"):
                    opp_val = getattr(item, "qm_Source", None)
                    
                    setattr(item, "qm_Source", self)
                    

class qm_Measure(CharacterizingElement):

    def __init__(self, type: str, Measure: "qm_QualityModel" = None, Measure70: "qm_Measurement" = None, qm_Measure: "qm_MeasureRefinement" = None, Measure74: "qm_MeasureRefinement" = None, child76: set["qm_Measurement"] = None, qm_Measure78: set["qm_Factor"] = None, measures81: "qm_QualityModel" = None, child84: set["qm_MeasureRefinement"] = None, qm_Measure87: "qm_Measure" = None, qm_Measure85: set["qm_Measure"] = None, qm_Measure89: "qm_MeasurementMethod" = None, qm_Measure100: "qm_MeasureEvaluation" = None):
        self.type = type
        self.Measure = Measure
        self.Measure70 = Measure70
        self.qm_Measure = qm_Measure
        self.Measure74 = Measure74
        self.child76 = child76 if child76 is not None else set()
        self.qm_Measure78 = qm_Measure78 if qm_Measure78 is not None else set()
        self.measures81 = measures81
        self.child84 = child84 if child84 is not None else set()
        self.qm_Measure87 = qm_Measure87
        self.qm_Measure85 = qm_Measure85 if qm_Measure85 is not None else set()
        self.qm_Measure89 = qm_Measure89
        self.qm_Measure100 = qm_Measure100
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def qm_Measure85(self):
        return self.__qm_Measure85

    @qm_Measure85.setter
    def qm_Measure85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure85", None)
        self.__qm_Measure85 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_Measure87"):
                    opp_val = getattr(item, "qm_Measure87", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_Measure87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_Measure87"):
                    opp_val = getattr(item, "qm_Measure87", None)
                    
                    setattr(item, "qm_Measure87", self)
                    

    @property
    def Measure70(self):
        return self.__Measure70

    @Measure70.setter
    def Measure70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__Measure70", None)
        self.__Measure70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures"):
                opp_val = getattr(old_value, "measures", None)
                if opp_val == self:
                    setattr(old_value, "measures", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures"):
                opp_val = getattr(value, "measures", None)
                setattr(value, "measures", self)

    @property
    def qm_Measure89(self):
        return self.__qm_Measure89

    @qm_Measure89.setter
    def qm_Measure89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure89", None)
        self.__qm_Measure89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MeasurementMethod"):
                opp_val = getattr(old_value, "qm_MeasurementMethod", None)
                if opp_val == self:
                    setattr(old_value, "qm_MeasurementMethod", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MeasurementMethod"):
                opp_val = getattr(value, "qm_MeasurementMethod", None)
                setattr(value, "qm_MeasurementMethod", self)

    @property
    def Measure74(self):
        return self.__Measure74

    @Measure74.setter
    def Measure74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__Measure74", None)
        self.__Measure74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "refines73"):
                opp_val = getattr(old_value, "refines73", None)
                if opp_val == self:
                    setattr(old_value, "refines73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "refines73"):
                opp_val = getattr(value, "refines73", None)
                setattr(value, "refines73", self)

    @property
    def child76(self):
        return self.__child76

    @child76.setter
    def child76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__child76", None)
        self.__child76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measurement"):
                    opp_val = getattr(item, "Measurement", None)
                    
                    if opp_val == self:
                        setattr(item, "Measurement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measurement"):
                    opp_val = getattr(item, "Measurement", None)
                    
                    setattr(item, "Measurement", self)
                    

    @property
    def qm_Measure87(self):
        return self.__qm_Measure87

    @qm_Measure87.setter
    def qm_Measure87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure87", None)
        self.__qm_Measure87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Measure85"):
                opp_val = getattr(old_value, "qm_Measure85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Measure85"):
                opp_val = getattr(value, "qm_Measure85", None)
                if opp_val is None:
                    setattr(value, "qm_Measure85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qm_Measure78(self):
        return self.__qm_Measure78

    @qm_Measure78.setter
    def qm_Measure78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure78", None)
        self.__qm_Measure78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_Factor79"):
                    opp_val = getattr(item, "qm_Factor79", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_Factor79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_Factor79"):
                    opp_val = getattr(item, "qm_Factor79", None)
                    
                    setattr(item, "qm_Factor79", self)
                    

    @property
    def Measure(self):
        return self.__Measure

    @Measure.setter
    def Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__Measure", None)
        self.__Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualityModel6"):
                opp_val = getattr(old_value, "qualityModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualityModel6"):
                opp_val = getattr(value, "qualityModel6", None)
                if opp_val is None:
                    setattr(value, "qualityModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def child84(self):
        return self.__child84

    @child84.setter
    def child84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__child84", None)
        self.__child84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasureRefinement"):
                    opp_val = getattr(item, "MeasureRefinement", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasureRefinement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasureRefinement"):
                    opp_val = getattr(item, "MeasureRefinement", None)
                    
                    setattr(item, "MeasureRefinement", self)
                    

    @property
    def measures81(self):
        return self.__measures81

    @measures81.setter
    def measures81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__measures81", None)
        self.__measures81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityModel82"):
                opp_val = getattr(old_value, "QualityModel82", None)
                if opp_val == self:
                    setattr(old_value, "QualityModel82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityModel82"):
                opp_val = getattr(value, "QualityModel82", None)
                setattr(value, "QualityModel82", self)

    @property
    def qm_Measure100(self):
        return self.__qm_Measure100

    @qm_Measure100.setter
    def qm_Measure100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure100", None)
        self.__qm_Measure100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MeasureEvaluation"):
                opp_val = getattr(old_value, "qm_MeasureEvaluation", None)
                if opp_val == self:
                    setattr(old_value, "qm_MeasureEvaluation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MeasureEvaluation"):
                opp_val = getattr(value, "qm_MeasureEvaluation", None)
                setattr(value, "qm_MeasureEvaluation", self)

    @property
    def qm_Measure(self):
        return self.__qm_Measure

    @qm_Measure.setter
    def qm_Measure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Measure__qm_Measure", None)
        self.__qm_Measure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_MeasureRefinement"):
                opp_val = getattr(old_value, "qm_MeasureRefinement", None)
                if opp_val == self:
                    setattr(old_value, "qm_MeasureRefinement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_MeasureRefinement"):
                opp_val = getattr(value, "qm_MeasureRefinement", None)
                setattr(value, "qm_MeasureRefinement", self)

class qm_Factor(CharacterizingElement):

    pass
class NamedElement:

    pass
class qm_Entity(NamedElement):

    def __init__(self, stakeholder: bool, useCase: bool, Entity: "qm_QualityModel" = None, child: set["qm_Specialization"] = None, qm_Entity: "qm_Entity" = None, qm_Entity26: set["qm_Entity"] = None, child29: "qm_Decomposition" = None, qm_Entity32: "qm_Entity" = None, qm_Entity30: "qm_Entity" = None, entities: "qm_QualityModel" = None, qm_Entity36: "qm_Specialization" = None, Entity38: "qm_Specialization" = None, qm_Entity40: "qm_Decomposition" = None, Entity42: "qm_Decomposition" = None, qm_Entity44: "qm_CharacterizingElement" = None):
        self.stakeholder = stakeholder
        self.useCase = useCase
        self.Entity = Entity
        self.child = child if child is not None else set()
        self.qm_Entity = qm_Entity
        self.qm_Entity26 = qm_Entity26 if qm_Entity26 is not None else set()
        self.child29 = child29
        self.qm_Entity32 = qm_Entity32
        self.qm_Entity30 = qm_Entity30
        self.entities = entities
        self.qm_Entity36 = qm_Entity36
        self.Entity38 = Entity38
        self.qm_Entity40 = qm_Entity40
        self.Entity42 = Entity42
        self.qm_Entity44 = qm_Entity44
        
    @property
    def useCase(self) -> bool:
        return self.__useCase

    @useCase.setter
    def useCase(self, useCase: bool):
        self.__useCase = useCase

    @property
    def stakeholder(self) -> bool:
        return self.__stakeholder

    @stakeholder.setter
    def stakeholder(self, stakeholder: bool):
        self.__stakeholder = stakeholder

    @property
    def qm_Entity32(self):
        return self.__qm_Entity32

    @qm_Entity32.setter
    def qm_Entity32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity32", None)
        self.__qm_Entity32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Entity30"):
                opp_val = getattr(old_value, "qm_Entity30", None)
                if opp_val == self:
                    setattr(old_value, "qm_Entity30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Entity30"):
                opp_val = getattr(value, "qm_Entity30", None)
                setattr(value, "qm_Entity30", self)

    @property
    def qm_Entity30(self):
        return self.__qm_Entity30

    @qm_Entity30.setter
    def qm_Entity30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity30", None)
        self.__qm_Entity30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Entity32"):
                opp_val = getattr(old_value, "qm_Entity32", None)
                if opp_val == self:
                    setattr(old_value, "qm_Entity32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Entity32"):
                opp_val = getattr(value, "qm_Entity32", None)
                setattr(value, "qm_Entity32", self)

    @property
    def Entity42(self):
        return self.__Entity42

    @Entity42.setter
    def Entity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__Entity42", None)
        self.__Entity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partOf"):
                opp_val = getattr(old_value, "partOf", None)
                if opp_val == self:
                    setattr(old_value, "partOf", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partOf"):
                opp_val = getattr(value, "partOf", None)
                setattr(value, "partOf", self)

    @property
    def qm_Entity(self):
        return self.__qm_Entity

    @qm_Entity.setter
    def qm_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity", None)
        self.__qm_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Entity26"):
                opp_val = getattr(old_value, "qm_Entity26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Entity26"):
                opp_val = getattr(value, "qm_Entity26", None)
                if opp_val is None:
                    setattr(value, "qm_Entity26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Entity38(self):
        return self.__Entity38

    @Entity38.setter
    def Entity38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__Entity38", None)
        self.__Entity38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isA"):
                opp_val = getattr(old_value, "isA", None)
                if opp_val == self:
                    setattr(old_value, "isA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isA"):
                opp_val = getattr(value, "isA", None)
                setattr(value, "isA", self)

    @property
    def qm_Entity26(self):
        return self.__qm_Entity26

    @qm_Entity26.setter
    def qm_Entity26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity26", None)
        self.__qm_Entity26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_Entity"):
                    opp_val = getattr(item, "qm_Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_Entity"):
                    opp_val = getattr(item, "qm_Entity", None)
                    
                    setattr(item, "qm_Entity", self)
                    

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualityModel"):
                opp_val = getattr(old_value, "qualityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualityModel"):
                opp_val = getattr(value, "qualityModel", None)
                if opp_val is None:
                    setattr(value, "qualityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qm_Entity36(self):
        return self.__qm_Entity36

    @qm_Entity36.setter
    def qm_Entity36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity36", None)
        self.__qm_Entity36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Specialization"):
                opp_val = getattr(old_value, "qm_Specialization", None)
                if opp_val == self:
                    setattr(old_value, "qm_Specialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Specialization"):
                opp_val = getattr(value, "qm_Specialization", None)
                setattr(value, "qm_Specialization", self)

    @property
    def entities(self):
        return self.__entities

    @entities.setter
    def entities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__entities", None)
        self.__entities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityModel34"):
                opp_val = getattr(old_value, "QualityModel34", None)
                if opp_val == self:
                    setattr(old_value, "QualityModel34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityModel34"):
                opp_val = getattr(value, "QualityModel34", None)
                setattr(value, "QualityModel34", self)

    @property
    def child29(self):
        return self.__child29

    @child29.setter
    def child29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__child29", None)
        self.__child29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Decomposition"):
                opp_val = getattr(old_value, "Decomposition", None)
                if opp_val == self:
                    setattr(old_value, "Decomposition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Decomposition"):
                opp_val = getattr(value, "Decomposition", None)
                setattr(value, "Decomposition", self)

    @property
    def qm_Entity40(self):
        return self.__qm_Entity40

    @qm_Entity40.setter
    def qm_Entity40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity40", None)
        self.__qm_Entity40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Decomposition"):
                opp_val = getattr(old_value, "qm_Decomposition", None)
                if opp_val == self:
                    setattr(old_value, "qm_Decomposition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Decomposition"):
                opp_val = getattr(value, "qm_Decomposition", None)
                setattr(value, "qm_Decomposition", self)

    @property
    def qm_Entity44(self):
        return self.__qm_Entity44

    @qm_Entity44.setter
    def qm_Entity44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__qm_Entity44", None)
        self.__qm_Entity44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_CharacterizingElement"):
                opp_val = getattr(old_value, "qm_CharacterizingElement", None)
                if opp_val == self:
                    setattr(old_value, "qm_CharacterizingElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_CharacterizingElement"):
                opp_val = getattr(value, "qm_CharacterizingElement", None)
                setattr(value, "qm_CharacterizingElement", self)

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Entity__child", None)
        self.__child = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    setattr(item, "Specialization", self)
                    

class qm_Source(NamedElement):

    pass
class qm_ManualInstrument(NamedElement, Instrument):

    pass
class qm_Tag(NamedElement):

    pass
class qm_Evaluation(NamedElement):

    def __init__(self, maximumPoints: int, completeness: int, Evaluation: "qm_QualityModel" = None, qm_Evaluation: "qm_Factor" = None, evaluations: "qm_QualityModel" = None, qm_Evaluation119: "qm_EvaluationResult" = None):
        self.maximumPoints = maximumPoints
        self.completeness = completeness
        self.Evaluation = Evaluation
        self.qm_Evaluation = qm_Evaluation
        self.evaluations = evaluations
        self.qm_Evaluation119 = qm_Evaluation119
        
    @property
    def completeness(self) -> int:
        return self.__completeness

    @completeness.setter
    def completeness(self, completeness: int):
        self.__completeness = completeness

    @property
    def maximumPoints(self) -> int:
        return self.__maximumPoints

    @maximumPoints.setter
    def maximumPoints(self, maximumPoints: int):
        self.__maximumPoints = maximumPoints

    @property
    def evaluations(self):
        return self.__evaluations

    @evaluations.setter
    def evaluations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Evaluation__evaluations", None)
        self.__evaluations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "QualityModel62"):
                opp_val = getattr(old_value, "QualityModel62", None)
                if opp_val == self:
                    setattr(old_value, "QualityModel62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "QualityModel62"):
                opp_val = getattr(value, "QualityModel62", None)
                setattr(value, "QualityModel62", self)

    @property
    def Evaluation(self):
        return self.__Evaluation

    @Evaluation.setter
    def Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Evaluation__Evaluation", None)
        self.__Evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualityModel4"):
                opp_val = getattr(old_value, "qualityModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualityModel4"):
                opp_val = getattr(value, "qualityModel4", None)
                if opp_val is None:
                    setattr(value, "qualityModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qm_Evaluation(self):
        return self.__qm_Evaluation

    @qm_Evaluation.setter
    def qm_Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Evaluation__qm_Evaluation", None)
        self.__qm_Evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_Factor60"):
                opp_val = getattr(old_value, "qm_Factor60", None)
                if opp_val == self:
                    setattr(old_value, "qm_Factor60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_Factor60"):
                opp_val = getattr(value, "qm_Factor60", None)
                setattr(value, "qm_Factor60", self)

    @property
    def qm_Evaluation119(self):
        return self.__qm_Evaluation119

    @qm_Evaluation119.setter
    def qm_Evaluation119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_Evaluation__qm_Evaluation119", None)
        self.__qm_Evaluation119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_EvaluationResult118"):
                opp_val = getattr(old_value, "qm_EvaluationResult118", None)
                if opp_val == self:
                    setattr(old_value, "qm_EvaluationResult118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_EvaluationResult118"):
                opp_val = getattr(value, "qm_EvaluationResult118", None)
                setattr(value, "qm_EvaluationResult118", self)

class qm_CharacterizingElement(NamedElement):

    pass
class qm_Tool(NamedElement):

    pass
class qm_MeasureAggregation(NamedElement, MeasurementMethod):

    pass
class qm_QualityModel(NamedElement):

    def __init__(self, schoolGradeBoundary3: str, schoolGradeBoundary4: str, schoolGradeBoundary5: str, schoolGradeBoundary6: str, schoolGradeBoundary2: str, qualityModel: set["qm_Entity"] = None, qualityModel2: set["qm_Factor"] = None, qualityModel4: set["qm_Evaluation"] = None, qualityModel6: set["qm_Measure"] = None, QualityModel: "qm_Source" = None, qualityModel8: set["qm_MeasurementMethod"] = None, qualityModel10: set["qm_Tool"] = None, qualityModel12: set["qm_Tag"] = None, qualityModel14: set["qm_Source"] = None, qm_QualityModel: "qm_QualityModel" = None, qm_QualityModel15: set["qm_QualityModel"] = None, QualityModel34: "qm_Entity" = None, QualityModel23: "qm_Tag" = None, QualityModel54: "qm_Factor" = None, QualityModel82: "qm_Measure" = None, QualityModel62: "qm_Evaluation" = None, QualityModel94: "qm_Tool" = None, QualityModel91: "qm_MeasurementMethod" = None):
        self.schoolGradeBoundary3 = schoolGradeBoundary3
        self.schoolGradeBoundary4 = schoolGradeBoundary4
        self.schoolGradeBoundary5 = schoolGradeBoundary5
        self.schoolGradeBoundary6 = schoolGradeBoundary6
        self.schoolGradeBoundary2 = schoolGradeBoundary2
        self.qualityModel = qualityModel if qualityModel is not None else set()
        self.qualityModel2 = qualityModel2 if qualityModel2 is not None else set()
        self.qualityModel4 = qualityModel4 if qualityModel4 is not None else set()
        self.qualityModel6 = qualityModel6 if qualityModel6 is not None else set()
        self.QualityModel = QualityModel
        self.qualityModel8 = qualityModel8 if qualityModel8 is not None else set()
        self.qualityModel10 = qualityModel10 if qualityModel10 is not None else set()
        self.qualityModel12 = qualityModel12 if qualityModel12 is not None else set()
        self.qualityModel14 = qualityModel14 if qualityModel14 is not None else set()
        self.qm_QualityModel = qm_QualityModel
        self.qm_QualityModel15 = qm_QualityModel15 if qm_QualityModel15 is not None else set()
        self.QualityModel34 = QualityModel34
        self.QualityModel23 = QualityModel23
        self.QualityModel54 = QualityModel54
        self.QualityModel82 = QualityModel82
        self.QualityModel62 = QualityModel62
        self.QualityModel94 = QualityModel94
        self.QualityModel91 = QualityModel91
        
    @property
    def schoolGradeBoundary6(self) -> str:
        return self.__schoolGradeBoundary6

    @schoolGradeBoundary6.setter
    def schoolGradeBoundary6(self, schoolGradeBoundary6: str):
        self.__schoolGradeBoundary6 = schoolGradeBoundary6

    @property
    def schoolGradeBoundary3(self) -> str:
        return self.__schoolGradeBoundary3

    @schoolGradeBoundary3.setter
    def schoolGradeBoundary3(self, schoolGradeBoundary3: str):
        self.__schoolGradeBoundary3 = schoolGradeBoundary3

    @property
    def schoolGradeBoundary4(self) -> str:
        return self.__schoolGradeBoundary4

    @schoolGradeBoundary4.setter
    def schoolGradeBoundary4(self, schoolGradeBoundary4: str):
        self.__schoolGradeBoundary4 = schoolGradeBoundary4

    @property
    def schoolGradeBoundary5(self) -> str:
        return self.__schoolGradeBoundary5

    @schoolGradeBoundary5.setter
    def schoolGradeBoundary5(self, schoolGradeBoundary5: str):
        self.__schoolGradeBoundary5 = schoolGradeBoundary5

    @property
    def schoolGradeBoundary2(self) -> str:
        return self.__schoolGradeBoundary2

    @schoolGradeBoundary2.setter
    def schoolGradeBoundary2(self, schoolGradeBoundary2: str):
        self.__schoolGradeBoundary2 = schoolGradeBoundary2

    @property
    def QualityModel62(self):
        return self.__QualityModel62

    @QualityModel62.setter
    def QualityModel62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel62", None)
        self.__QualityModel62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "evaluations"):
                opp_val = getattr(old_value, "evaluations", None)
                if opp_val == self:
                    setattr(old_value, "evaluations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "evaluations"):
                opp_val = getattr(value, "evaluations", None)
                setattr(value, "evaluations", self)

    @property
    def QualityModel91(self):
        return self.__QualityModel91

    @QualityModel91.setter
    def QualityModel91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel91", None)
        self.__QualityModel91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measurementMethods"):
                opp_val = getattr(old_value, "measurementMethods", None)
                if opp_val == self:
                    setattr(old_value, "measurementMethods", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measurementMethods"):
                opp_val = getattr(value, "measurementMethods", None)
                setattr(value, "measurementMethods", self)

    @property
    def qualityModel12(self):
        return self.__qualityModel12

    @qualityModel12.setter
    def qualityModel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel12", None)
        self.__qualityModel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tag"):
                    opp_val = getattr(item, "Tag", None)
                    
                    setattr(item, "Tag", self)
                    

    @property
    def qualityModel2(self):
        return self.__qualityModel2

    @qualityModel2.setter
    def qualityModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel2", None)
        self.__qualityModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Factor"):
                    opp_val = getattr(item, "Factor", None)
                    
                    if opp_val == self:
                        setattr(item, "Factor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Factor"):
                    opp_val = getattr(item, "Factor", None)
                    
                    setattr(item, "Factor", self)
                    

    @property
    def QualityModel54(self):
        return self.__QualityModel54

    @QualityModel54.setter
    def QualityModel54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel54", None)
        self.__QualityModel54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "factors"):
                opp_val = getattr(old_value, "factors", None)
                if opp_val == self:
                    setattr(old_value, "factors", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "factors"):
                opp_val = getattr(value, "factors", None)
                setattr(value, "factors", self)

    @property
    def qualityModel(self):
        return self.__qualityModel

    @qualityModel.setter
    def qualityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel", None)
        self.__qualityModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    if opp_val == self:
                        setattr(item, "Entity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Entity"):
                    opp_val = getattr(item, "Entity", None)
                    
                    setattr(item, "Entity", self)
                    

    @property
    def qualityModel14(self):
        return self.__qualityModel14

    @qualityModel14.setter
    def qualityModel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel14", None)
        self.__qualityModel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    if opp_val == self:
                        setattr(item, "Source", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Source"):
                    opp_val = getattr(item, "Source", None)
                    
                    setattr(item, "Source", self)
                    

    @property
    def QualityModel(self):
        return self.__QualityModel

    @QualityModel.setter
    def QualityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel", None)
        self.__QualityModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if opp_val == self:
                    setattr(old_value, "sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                setattr(value, "sources", self)

    @property
    def qualityModel8(self):
        return self.__qualityModel8

    @qualityModel8.setter
    def qualityModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel8", None)
        self.__qualityModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MeasurementMethod"):
                    opp_val = getattr(item, "MeasurementMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "MeasurementMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MeasurementMethod"):
                    opp_val = getattr(item, "MeasurementMethod", None)
                    
                    setattr(item, "MeasurementMethod", self)
                    

    @property
    def qualityModel10(self):
        return self.__qualityModel10

    @qualityModel10.setter
    def qualityModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel10", None)
        self.__qualityModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tool"):
                    opp_val = getattr(item, "Tool", None)
                    
                    if opp_val == self:
                        setattr(item, "Tool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tool"):
                    opp_val = getattr(item, "Tool", None)
                    
                    setattr(item, "Tool", self)
                    

    @property
    def QualityModel94(self):
        return self.__QualityModel94

    @QualityModel94.setter
    def QualityModel94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel94", None)
        self.__QualityModel94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tools"):
                opp_val = getattr(old_value, "tools", None)
                if opp_val == self:
                    setattr(old_value, "tools", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tools"):
                opp_val = getattr(value, "tools", None)
                setattr(value, "tools", self)

    @property
    def qm_QualityModel(self):
        return self.__qm_QualityModel

    @qm_QualityModel.setter
    def qm_QualityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qm_QualityModel", None)
        self.__qm_QualityModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qm_QualityModel15"):
                opp_val = getattr(old_value, "qm_QualityModel15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qm_QualityModel15"):
                opp_val = getattr(value, "qm_QualityModel15", None)
                if opp_val is None:
                    setattr(value, "qm_QualityModel15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualityModel6(self):
        return self.__qualityModel6

    @qualityModel6.setter
    def qualityModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel6", None)
        self.__qualityModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    if opp_val == self:
                        setattr(item, "Measure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Measure"):
                    opp_val = getattr(item, "Measure", None)
                    
                    setattr(item, "Measure", self)
                    

    @property
    def QualityModel23(self):
        return self.__QualityModel23

    @QualityModel23.setter
    def QualityModel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel23", None)
        self.__QualityModel23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tags"):
                opp_val = getattr(old_value, "tags", None)
                if opp_val == self:
                    setattr(old_value, "tags", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tags"):
                opp_val = getattr(value, "tags", None)
                setattr(value, "tags", self)

    @property
    def QualityModel82(self):
        return self.__QualityModel82

    @QualityModel82.setter
    def QualityModel82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel82", None)
        self.__QualityModel82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "measures81"):
                opp_val = getattr(old_value, "measures81", None)
                if opp_val == self:
                    setattr(old_value, "measures81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "measures81"):
                opp_val = getattr(value, "measures81", None)
                setattr(value, "measures81", self)

    @property
    def QualityModel34(self):
        return self.__QualityModel34

    @QualityModel34.setter
    def QualityModel34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__QualityModel34", None)
        self.__QualityModel34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entities"):
                opp_val = getattr(old_value, "entities", None)
                if opp_val == self:
                    setattr(old_value, "entities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entities"):
                opp_val = getattr(value, "entities", None)
                setattr(value, "entities", self)

    @property
    def qm_QualityModel15(self):
        return self.__qm_QualityModel15

    @qm_QualityModel15.setter
    def qm_QualityModel15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qm_QualityModel15", None)
        self.__qm_QualityModel15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "qm_QualityModel"):
                    opp_val = getattr(item, "qm_QualityModel", None)
                    
                    if opp_val == self:
                        setattr(item, "qm_QualityModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "qm_QualityModel"):
                    opp_val = getattr(item, "qm_QualityModel", None)
                    
                    setattr(item, "qm_QualityModel", self)
                    

    @property
    def qualityModel4(self):
        return self.__qualityModel4

    @qualityModel4.setter
    def qualityModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_qm_QualityModel__qualityModel4", None)
        self.__qualityModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    if opp_val == self:
                        setattr(item, "Evaluation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Evaluation"):
                    opp_val = getattr(item, "Evaluation", None)
                    
                    setattr(item, "Evaluation", self)
                    
