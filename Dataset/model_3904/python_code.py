from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class QuellenConstrainType(Enum):
    notTogether = "notTogether"
    needOneOf = "needOneOf"
class GeneratorState(Enum):
    new = "new"
    readyForCreation = "readyForCreation"
    commited = "commited"
    personaCreated = "personaCreated"
class Sex(Enum):
    female = "female"
    male = "male"
    undefinde = "undefinde"
    none = "none"
class LifeModuleType(Enum):
    nationality = "nationality"
    formativeYears = "formativeYears"
    teenYears = "teenYears"
    furtherEducation = "furtherEducation"
    realLife = "realLife"


############################################
# Definition of Classes
############################################

class shr5Management_MartialartTechnique:

    pass
class shr5Management_MartialartStyle:

    pass
class PersonaChange:

    pass
class shr5Management_PersonaMartialArtChange(PersonaChange):

    pass
class shr5Management_TrainingRange:

    def __init__(self, start: str, end: str, daysTrained: int, TrainingRange: "shr5Management_TrainingsTime" = None, training: "shr5Management_TrainingsTime" = None):
        self.start = start
        self.end = end
        self.daysTrained = daysTrained
        self.TrainingRange = TrainingRange
        self.training = training
        
    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def daysTrained(self) -> int:
        return self.__daysTrained

    @daysTrained.setter
    def daysTrained(self, daysTrained: int):
        self.__daysTrained = daysTrained

    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def training(self):
        return self.__training

    @training.setter
    def training(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_TrainingRange__training", None)
        self.__training = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrainingsTime"):
                opp_val = getattr(old_value, "TrainingsTime", None)
                if opp_val == self:
                    setattr(old_value, "TrainingsTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrainingsTime"):
                opp_val = getattr(value, "TrainingsTime", None)
                setattr(value, "TrainingsTime", self)

    @property
    def TrainingRange(self):
        return self.__TrainingRange

    @TrainingRange.setter
    def TrainingRange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_TrainingRange__TrainingRange", None)
        self.__TrainingRange = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trainingTime"):
                opp_val = getattr(old_value, "trainingTime", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trainingTime"):
                opp_val = getattr(value, "trainingTime", None)
                if opp_val is None:
                    setattr(value, "trainingTime", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CharacterChange:

    pass
class shr5Management_TrainingsTime(CharacterChange):

    def __init__(self, daysTrained: int, daysRemains: int, trainingComplete: bool, trainingTime: set["shr5Management_TrainingRange"] = None, TrainingsTime: "shr5Management_TrainingRange" = None):
        self.daysTrained = daysTrained
        self.daysRemains = daysRemains
        self.trainingComplete = trainingComplete
        self.trainingTime = trainingTime if trainingTime is not None else set()
        self.TrainingsTime = TrainingsTime
        
    @property
    def daysRemains(self) -> int:
        return self.__daysRemains

    @daysRemains.setter
    def daysRemains(self, daysRemains: int):
        self.__daysRemains = daysRemains

    @property
    def trainingComplete(self) -> bool:
        return self.__trainingComplete

    @trainingComplete.setter
    def trainingComplete(self, trainingComplete: bool):
        self.__trainingComplete = trainingComplete

    @property
    def daysTrained(self) -> int:
        return self.__daysTrained

    @daysTrained.setter
    def daysTrained(self, daysTrained: int):
        self.__daysTrained = daysTrained

    @property
    def TrainingsTime(self):
        return self.__TrainingsTime

    @TrainingsTime.setter
    def TrainingsTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_TrainingsTime__TrainingsTime", None)
        self.__TrainingsTime = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "training"):
                opp_val = getattr(old_value, "training", None)
                if opp_val == self:
                    setattr(old_value, "training", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "training"):
                opp_val = getattr(value, "training", None)
                setattr(value, "training", self)

    @property
    def trainingTime(self):
        return self.__trainingTime

    @trainingTime.setter
    def trainingTime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_TrainingsTime__trainingTime", None)
        self.__trainingTime = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrainingRange"):
                    opp_val = getattr(item, "TrainingRange", None)
                    
                    if opp_val == self:
                        setattr(item, "TrainingRange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrainingRange"):
                    opp_val = getattr(item, "TrainingRange", None)
                    
                    setattr(item, "TrainingRange", self)
                    

    def hasValidRange(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasValidRange method
        pass

class shr5Management_ModuleSkillGroupChange:

    pass
class shr5Management_EObject:

    pass
class shr5Management_EReference:

    pass
class ModuleChange:

    pass
class shr5Management_ModuleTypeChange(ModuleChange):

    def __init__(self, grade: int):
        self.grade = grade
        
    @property
    def grade(self) -> int:
        return self.__grade

    @grade.setter
    def grade(self, grade: int):
        self.__grade = grade

class shr5Management_ModuleFeatureChange(ModuleChange):

    pass
class shr5Management_ModuleAttributeChange:

    pass
class shr5Management_ModuleTeachableChange:

    pass
class shr5Management_ModuleSkillChange:

    pass
class shr5Management_RangeTable(ABC):

    pass
class shr5Management_RangeTableEntry(ABC):

    def __init__(self, from: int, to: int):
        self.from = from
        self.to = to
        
    @property
    def to(self) -> int:
        return self.__to

    @to.setter
    def to(self, to: int):
        self.__to = to

    @property
    def from(self) -> int:
        return self.__from

    @from.setter
    def from(self, from: int):
        self.__from = from

class RangeTableEntry:

    pass
class shr5Management_TrainingRate(RangeTableEntry):

    def __init__(self, factor: int, timeUnit: str):
        self.factor = factor
        self.timeUnit = timeUnit
        
    @property
    def timeUnit(self) -> str:
        return self.__timeUnit

    @timeUnit.setter
    def timeUnit(self, timeUnit: str):
        self.__timeUnit = timeUnit

    @property
    def factor(self) -> int:
        return self.__factor

    @factor.setter
    def factor(self, factor: int):
        self.__factor = factor

class shr5Management_Shr5KarmaGenerator:

    pass
class shr5Management_LifeModulesGenerator:

    def __init__(self, moduleKarmaCost: int, startingAge: int, shr5Management_LifeModulesGenerator110: "shr5Management_LifeModule" = None, shr5Management_LifeModulesGenerator113: set["shr5Management_LifeModule"] = None, shr5Management_LifeModulesGenerator: "shr5Management_LifeModule" = None, shr5Management_LifeModulesGenerator104: "shr5Management_LifeModule" = None, shr5Management_LifeModulesGenerator107: "shr5Management_LifeModule" = None):
        self.moduleKarmaCost = moduleKarmaCost
        self.startingAge = startingAge
        self.shr5Management_LifeModulesGenerator110 = shr5Management_LifeModulesGenerator110
        self.shr5Management_LifeModulesGenerator113 = shr5Management_LifeModulesGenerator113 if shr5Management_LifeModulesGenerator113 is not None else set()
        self.shr5Management_LifeModulesGenerator = shr5Management_LifeModulesGenerator
        self.shr5Management_LifeModulesGenerator104 = shr5Management_LifeModulesGenerator104
        self.shr5Management_LifeModulesGenerator107 = shr5Management_LifeModulesGenerator107
        
    @property
    def startingAge(self) -> int:
        return self.__startingAge

    @startingAge.setter
    def startingAge(self, startingAge: int):
        self.__startingAge = startingAge

    @property
    def moduleKarmaCost(self) -> int:
        return self.__moduleKarmaCost

    @moduleKarmaCost.setter
    def moduleKarmaCost(self, moduleKarmaCost: int):
        self.__moduleKarmaCost = moduleKarmaCost

    @property
    def shr5Management_LifeModulesGenerator(self):
        return self.__shr5Management_LifeModulesGenerator

    @shr5Management_LifeModulesGenerator.setter
    def shr5Management_LifeModulesGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesGenerator__shr5Management_LifeModulesGenerator", None)
        self.__shr5Management_LifeModulesGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModule"):
                opp_val = getattr(old_value, "shr5Management_LifeModule", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModule"):
                opp_val = getattr(value, "shr5Management_LifeModule", None)
                setattr(value, "shr5Management_LifeModule", self)

    @property
    def shr5Management_LifeModulesGenerator113(self):
        return self.__shr5Management_LifeModulesGenerator113

    @shr5Management_LifeModulesGenerator113.setter
    def shr5Management_LifeModulesGenerator113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesGenerator__shr5Management_LifeModulesGenerator113", None)
        self.__shr5Management_LifeModulesGenerator113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_LifeModule114"):
                    opp_val = getattr(item, "shr5Management_LifeModule114", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_LifeModule114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_LifeModule114"):
                    opp_val = getattr(item, "shr5Management_LifeModule114", None)
                    
                    setattr(item, "shr5Management_LifeModule114", self)
                    

    @property
    def shr5Management_LifeModulesGenerator104(self):
        return self.__shr5Management_LifeModulesGenerator104

    @shr5Management_LifeModulesGenerator104.setter
    def shr5Management_LifeModulesGenerator104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesGenerator__shr5Management_LifeModulesGenerator104", None)
        self.__shr5Management_LifeModulesGenerator104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModule105"):
                opp_val = getattr(old_value, "shr5Management_LifeModule105", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModule105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModule105"):
                opp_val = getattr(value, "shr5Management_LifeModule105", None)
                setattr(value, "shr5Management_LifeModule105", self)

    @property
    def shr5Management_LifeModulesGenerator107(self):
        return self.__shr5Management_LifeModulesGenerator107

    @shr5Management_LifeModulesGenerator107.setter
    def shr5Management_LifeModulesGenerator107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesGenerator__shr5Management_LifeModulesGenerator107", None)
        self.__shr5Management_LifeModulesGenerator107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModule108"):
                opp_val = getattr(old_value, "shr5Management_LifeModule108", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModule108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModule108"):
                opp_val = getattr(value, "shr5Management_LifeModule108", None)
                setattr(value, "shr5Management_LifeModule108", self)

    @property
    def shr5Management_LifeModulesGenerator110(self):
        return self.__shr5Management_LifeModulesGenerator110

    @shr5Management_LifeModulesGenerator110.setter
    def shr5Management_LifeModulesGenerator110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesGenerator__shr5Management_LifeModulesGenerator110", None)
        self.__shr5Management_LifeModulesGenerator110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModule111"):
                opp_val = getattr(old_value, "shr5Management_LifeModule111", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModule111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModule111"):
                opp_val = getattr(value, "shr5Management_LifeModule111", None)
                setattr(value, "shr5Management_LifeModule111", self)

class Shr5Generator:

    pass
class shr5Management_SumToTenGenerator(Shr5Generator):

    def __init__(self):
        
    def hasSumToTen(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSumToTen method
        pass

class DiaryEntry:

    pass
class shr5Management_CharacterChange(DiaryEntry):

    pass
class shr5Management_ContractPayment(DiaryEntry):

    def __init__(self, payed: bool, shr5Management_ContractPayment: "shr5Management_Vertrag" = None):
        self.payed = payed
        self.shr5Management_ContractPayment = shr5Management_ContractPayment
        
    @property
    def payed(self) -> bool:
        return self.__payed

    @payed.setter
    def payed(self, payed: bool):
        self.__payed = payed

    @property
    def shr5Management_ContractPayment(self):
        return self.__shr5Management_ContractPayment

    @shr5Management_ContractPayment.setter
    def shr5Management_ContractPayment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ContractPayment__shr5Management_ContractPayment", None)
        self.__shr5Management_ContractPayment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Vertrag100"):
                opp_val = getattr(old_value, "shr5Management_Vertrag100", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Vertrag100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Vertrag100"):
                opp_val = getattr(value, "shr5Management_Vertrag100", None)
                setattr(value, "shr5Management_Vertrag100", self)

class shr5Management_ModuleChange(ABC):

    pass
class Shr5System:

    pass
class shr5Management_LifeModulesSystem(Shr5System):

    def __init__(self, knowlegeSkillMax: int, shr5Management_LifeModulesSystem: set["shr5Management_LifeModule"] = None):
        self.knowlegeSkillMax = knowlegeSkillMax
        self.shr5Management_LifeModulesSystem = shr5Management_LifeModulesSystem if shr5Management_LifeModulesSystem is not None else set()
        
    @property
    def knowlegeSkillMax(self) -> int:
        return self.__knowlegeSkillMax

    @knowlegeSkillMax.setter
    def knowlegeSkillMax(self, knowlegeSkillMax: int):
        self.__knowlegeSkillMax = knowlegeSkillMax

    @property
    def shr5Management_LifeModulesSystem(self):
        return self.__shr5Management_LifeModulesSystem

    @shr5Management_LifeModulesSystem.setter
    def shr5Management_LifeModulesSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModulesSystem__shr5Management_LifeModulesSystem", None)
        self.__shr5Management_LifeModulesSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_LifeModule116"):
                    opp_val = getattr(item, "shr5Management_LifeModule116", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_LifeModule116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_LifeModule116"):
                    opp_val = getattr(item, "shr5Management_LifeModule116", None)
                    
                    setattr(item, "shr5Management_LifeModule116", self)
                    

class shr5Management_Quelle:

    pass
class shr5Management_DiaryEntry:

    def __init__(self, date: str, message: str, shr5Management_DiaryEntry: "shr5Management_CharacterDiary" = None):
        self.date = date
        self.message = message
        self.shr5Management_DiaryEntry = shr5Management_DiaryEntry
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def shr5Management_DiaryEntry(self):
        return self.__shr5Management_DiaryEntry

    @shr5Management_DiaryEntry.setter
    def shr5Management_DiaryEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_DiaryEntry__shr5Management_DiaryEntry", None)
        self.__shr5Management_DiaryEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterDiary98"):
                opp_val = getattr(old_value, "shr5Management_CharacterDiary98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterDiary98"):
                opp_val = getattr(value, "shr5Management_CharacterDiary98", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterDiary98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GeldWert:

    pass
class shr5Management_KarmaGenerator(ABC):

    def __init__(self, karmaToResource: int, karmaSpend: int, resourceSpend: int, startKarma: int, startResources: int, choiseKarmaCost: int, shr5Management_KarmaGenerator: "shr5Management_MetaType" = None, shr5Management_KarmaGenerator88: "shr5Management_SpecialType" = None):
        self.karmaToResource = karmaToResource
        self.karmaSpend = karmaSpend
        self.resourceSpend = resourceSpend
        self.startKarma = startKarma
        self.startResources = startResources
        self.choiseKarmaCost = choiseKarmaCost
        self.shr5Management_KarmaGenerator = shr5Management_KarmaGenerator
        self.shr5Management_KarmaGenerator88 = shr5Management_KarmaGenerator88
        
    @property
    def karmaSpend(self) -> int:
        return self.__karmaSpend

    @karmaSpend.setter
    def karmaSpend(self, karmaSpend: int):
        self.__karmaSpend = karmaSpend

    @property
    def karmaToResource(self) -> int:
        return self.__karmaToResource

    @karmaToResource.setter
    def karmaToResource(self, karmaToResource: int):
        self.__karmaToResource = karmaToResource

    @property
    def startResources(self) -> int:
        return self.__startResources

    @startResources.setter
    def startResources(self, startResources: int):
        self.__startResources = startResources

    @property
    def resourceSpend(self) -> int:
        return self.__resourceSpend

    @resourceSpend.setter
    def resourceSpend(self, resourceSpend: int):
        self.__resourceSpend = resourceSpend

    @property
    def choiseKarmaCost(self) -> int:
        return self.__choiseKarmaCost

    @choiseKarmaCost.setter
    def choiseKarmaCost(self, choiseKarmaCost: int):
        self.__choiseKarmaCost = choiseKarmaCost

    @property
    def startKarma(self) -> int:
        return self.__startKarma

    @startKarma.setter
    def startKarma(self, startKarma: int):
        self.__startKarma = startKarma

    @property
    def shr5Management_KarmaGenerator88(self):
        return self.__shr5Management_KarmaGenerator88

    @shr5Management_KarmaGenerator88.setter
    def shr5Management_KarmaGenerator88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_KarmaGenerator__shr5Management_KarmaGenerator88", None)
        self.__shr5Management_KarmaGenerator88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_SpecialType89"):
                opp_val = getattr(old_value, "shr5Management_SpecialType89", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_SpecialType89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_SpecialType89"):
                opp_val = getattr(value, "shr5Management_SpecialType89", None)
                setattr(value, "shr5Management_SpecialType89", self)

    @property
    def shr5Management_KarmaGenerator(self):
        return self.__shr5Management_KarmaGenerator

    @shr5Management_KarmaGenerator.setter
    def shr5Management_KarmaGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_KarmaGenerator__shr5Management_KarmaGenerator", None)
        self.__shr5Management_KarmaGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_MetaType86"):
                opp_val = getattr(old_value, "shr5Management_MetaType86", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_MetaType86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_MetaType86"):
                opp_val = getattr(value, "shr5Management_MetaType86", None)
                setattr(value, "shr5Management_MetaType86", self)

    def hasSpendAllKarmaPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllKarmaPoints method
        pass

    def hasSpendAllResources(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllResources method
        pass

class shr5Management_Shr5RuleGenerator(ABC):

    def __init__(self, shr5Management_Shr5RuleGenerator: set["shr5Management_SourceBook"] = None):
        self.shr5Management_Shr5RuleGenerator = shr5Management_Shr5RuleGenerator if shr5Management_Shr5RuleGenerator is not None else set()
        
    @property
    def shr5Management_Shr5RuleGenerator(self):
        return self.__shr5Management_Shr5RuleGenerator

    @shr5Management_Shr5RuleGenerator.setter
    def shr5Management_Shr5RuleGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5RuleGenerator__shr5Management_Shr5RuleGenerator", None)
        self.__shr5Management_Shr5RuleGenerator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_SourceBook"):
                    opp_val = getattr(item, "shr5Management_SourceBook", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_SourceBook", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_SourceBook"):
                    opp_val = getattr(item, "shr5Management_SourceBook", None)
                    
                    setattr(item, "shr5Management_SourceBook", self)
                    

    def hasOnlyAllowedSources(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasOnlyAllowedSources method
        pass

    def hasKiPowerOverLimit(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasKiPowerOverLimit method
        pass

    def hasLifestyleChoosen(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasLifestyleChoosen method
        pass

    def hasSpendAllPoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllPoints method
        pass

    def hasBasicViolations(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasBasicViolations method
        pass

    def hasNotMoreMaxAttributes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasNotMoreMaxAttributes method
        pass

    def hasNoConstrainVoilation(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasNoConstrainVoilation method
        pass

    def hasNoAttributesOverSpeciesAtt(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasNoAttributesOverSpeciesAtt method
        pass

    def hasNotMoreSpecalism(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasNotMoreSpecalism method
        pass

    def hasNoSkillsOverMax(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasNoSkillsOverMax method
        pass

class shr5Management_SourceBook:

    pass
class PlayerManagement:

    pass
class shr5Management_GamemasterManagement(PlayerManagement):

    pass
class shr5Management_GruntMembers:

    def __init__(self, count: int, shr5Management_GruntMembers: "shr5Management_GruntGroup" = None, shr5Management_GruntMembers72: "shr5Management_GruntGroup" = None, shr5Management_GruntMembers74: "shr5Management_NonPlayerCharacter" = None):
        self.count = count
        self.shr5Management_GruntMembers = shr5Management_GruntMembers
        self.shr5Management_GruntMembers72 = shr5Management_GruntMembers72
        self.shr5Management_GruntMembers74 = shr5Management_GruntMembers74
        
    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, count: int):
        self.__count = count

    @property
    def shr5Management_GruntMembers74(self):
        return self.__shr5Management_GruntMembers74

    @shr5Management_GruntMembers74.setter
    def shr5Management_GruntMembers74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntMembers__shr5Management_GruntMembers74", None)
        self.__shr5Management_GruntMembers74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_NonPlayerCharacter"):
                opp_val = getattr(old_value, "shr5Management_NonPlayerCharacter", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_NonPlayerCharacter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_NonPlayerCharacter"):
                opp_val = getattr(value, "shr5Management_NonPlayerCharacter", None)
                setattr(value, "shr5Management_NonPlayerCharacter", self)

    @property
    def shr5Management_GruntMembers72(self):
        return self.__shr5Management_GruntMembers72

    @shr5Management_GruntMembers72.setter
    def shr5Management_GruntMembers72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntMembers__shr5Management_GruntMembers72", None)
        self.__shr5Management_GruntMembers72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_GruntGroup71"):
                opp_val = getattr(old_value, "shr5Management_GruntGroup71", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_GruntGroup71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_GruntGroup71"):
                opp_val = getattr(value, "shr5Management_GruntGroup71", None)
                setattr(value, "shr5Management_GruntGroup71", self)

    @property
    def shr5Management_GruntMembers(self):
        return self.__shr5Management_GruntMembers

    @shr5Management_GruntMembers.setter
    def shr5Management_GruntMembers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntMembers__shr5Management_GruntMembers", None)
        self.__shr5Management_GruntMembers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_GruntGroup"):
                opp_val = getattr(old_value, "shr5Management_GruntGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_GruntGroup"):
                opp_val = getattr(value, "shr5Management_GruntGroup", None)
                if opp_val is None:
                    setattr(value, "shr5Management_GruntGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5Management_IncreaseCharacterPart:

    pass
class shr5Management_Advancement(ABC):

    def __init__(self, karmaFactor: int, shr5Management_Advancement: "shr5Management_CharacterAdvancementSystem" = None):
        self.karmaFactor = karmaFactor
        self.shr5Management_Advancement = shr5Management_Advancement
        
    @property
    def karmaFactor(self) -> int:
        return self.__karmaFactor

    @karmaFactor.setter
    def karmaFactor(self, karmaFactor: int):
        self.__karmaFactor = karmaFactor

    @property
    def shr5Management_Advancement(self):
        return self.__shr5Management_Advancement

    @shr5Management_Advancement.setter
    def shr5Management_Advancement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Advancement__shr5Management_Advancement", None)
        self.__shr5Management_Advancement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterAdvancementSystem83"):
                opp_val = getattr(old_value, "shr5Management_CharacterAdvancementSystem83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterAdvancementSystem83"):
                opp_val = getattr(value, "shr5Management_CharacterAdvancementSystem83", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterAdvancementSystem83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5Management_Erlernbar:

    pass
class shr5Management_CharacterDiary:

    def __init__(self, characterDate: str, shr5Management_CharacterDiary: "shr5Management_PlayerCharacter" = None, shr5Management_CharacterDiary98: set["shr5Management_DiaryEntry"] = None):
        self.characterDate = characterDate
        self.shr5Management_CharacterDiary = shr5Management_CharacterDiary
        self.shr5Management_CharacterDiary98 = shr5Management_CharacterDiary98 if shr5Management_CharacterDiary98 is not None else set()
        
    @property
    def characterDate(self) -> str:
        return self.__characterDate

    @characterDate.setter
    def characterDate(self, characterDate: str):
        self.__characterDate = characterDate

    @property
    def shr5Management_CharacterDiary(self):
        return self.__shr5Management_CharacterDiary

    @shr5Management_CharacterDiary.setter
    def shr5Management_CharacterDiary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_CharacterDiary__shr5Management_CharacterDiary", None)
        self.__shr5Management_CharacterDiary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_PlayerCharacter"):
                opp_val = getattr(old_value, "shr5Management_PlayerCharacter", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_PlayerCharacter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_PlayerCharacter"):
                opp_val = getattr(value, "shr5Management_PlayerCharacter", None)
                setattr(value, "shr5Management_PlayerCharacter", self)

    @property
    def shr5Management_CharacterDiary98(self):
        return self.__shr5Management_CharacterDiary98

    @shr5Management_CharacterDiary98.setter
    def shr5Management_CharacterDiary98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_CharacterDiary__shr5Management_CharacterDiary98", None)
        self.__shr5Management_CharacterDiary98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_DiaryEntry"):
                    opp_val = getattr(item, "shr5Management_DiaryEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_DiaryEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_DiaryEntry"):
                    opp_val = getattr(item, "shr5Management_DiaryEntry", None)
                    
                    setattr(item, "shr5Management_DiaryEntry", self)
                    

class shr5Management_EAttribute:

    pass
class PersonaValueChange:

    pass
class shr5Management_PersonaChange(PersonaValueChange):

    pass
class shr5Management_AttributeChange(PersonaValueChange):

    pass
class shr5Management_CharacterGenerator(ABC):

    def __init__(self, state: str, characterName: str, currentInstruction: str, chracterSource: "shr5Management_ManagedCharacter" = None, shr5Management_CharacterGenerator: "shr5Management_CharacterGroup" = None):
        self.state = state
        self.characterName = characterName
        self.currentInstruction = currentInstruction
        self.chracterSource = chracterSource
        self.shr5Management_CharacterGenerator = shr5Management_CharacterGenerator
        
    @property
    def characterName(self) -> str:
        return self.__characterName

    @characterName.setter
    def characterName(self, characterName: str):
        self.__characterName = characterName

    @property
    def currentInstruction(self) -> str:
        return self.__currentInstruction

    @currentInstruction.setter
    def currentInstruction(self, currentInstruction: str):
        self.__currentInstruction = currentInstruction

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def chracterSource(self):
        return self.__chracterSource

    @chracterSource.setter
    def chracterSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_CharacterGenerator__chracterSource", None)
        self.__chracterSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ManagedCharacter32"):
                opp_val = getattr(old_value, "ManagedCharacter32", None)
                if opp_val == self:
                    setattr(old_value, "ManagedCharacter32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ManagedCharacter32"):
                opp_val = getattr(value, "ManagedCharacter32", None)
                setattr(value, "ManagedCharacter32", self)

    @property
    def shr5Management_CharacterGenerator(self):
        return self.__shr5Management_CharacterGenerator

    @shr5Management_CharacterGenerator.setter
    def shr5Management_CharacterGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_CharacterGenerator__shr5Management_CharacterGenerator", None)
        self.__shr5Management_CharacterGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterGroup"):
                opp_val = getattr(old_value, "shr5Management_CharacterGroup", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_CharacterGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterGroup"):
                opp_val = getattr(value, "shr5Management_CharacterGroup", None)
                setattr(value, "shr5Management_CharacterGroup", self)

class Adept:

    pass
class shr5Management_Spellcaster(Adept):

    def __init__(self, spellPoints: int):
        self.spellPoints = spellPoints
        
    @property
    def spellPoints(self) -> int:
        return self.__spellPoints

    @spellPoints.setter
    def spellPoints(self, spellPoints: int):
        self.__spellPoints = spellPoints

    def calcSpellPointsSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcSpellPointsSpend method
        pass

class shr5Management_Shr5Generator:

    def __init__(self, karmaToResource: int, karmaSpend: int, attributeSpend: int, resourceSpend: int, connectionSpend: int, skillPointSpend: int, specialPointSpend: int, groupPointSpend: int, knownlegePointSpend: int, spellPointSpend: int, startKarma: int, startResources: int, shr5Management_Shr5Generator: "shr5Management_Resourcen" = None, shr5Management_Shr5Generator46: "shr5Management_Skill" = None, shr5Management_Shr5Generator48: "shr5Management_Attributes" = None, shr5Management_Shr5Generator50: "shr5Management_MetaType" = None, shr5Management_Shr5Generator53: "shr5Management_SpecialType" = None):
        self.karmaToResource = karmaToResource
        self.karmaSpend = karmaSpend
        self.attributeSpend = attributeSpend
        self.resourceSpend = resourceSpend
        self.connectionSpend = connectionSpend
        self.skillPointSpend = skillPointSpend
        self.specialPointSpend = specialPointSpend
        self.groupPointSpend = groupPointSpend
        self.knownlegePointSpend = knownlegePointSpend
        self.spellPointSpend = spellPointSpend
        self.startKarma = startKarma
        self.startResources = startResources
        self.shr5Management_Shr5Generator = shr5Management_Shr5Generator
        self.shr5Management_Shr5Generator46 = shr5Management_Shr5Generator46
        self.shr5Management_Shr5Generator48 = shr5Management_Shr5Generator48
        self.shr5Management_Shr5Generator50 = shr5Management_Shr5Generator50
        self.shr5Management_Shr5Generator53 = shr5Management_Shr5Generator53
        
    @property
    def attributeSpend(self) -> int:
        return self.__attributeSpend

    @attributeSpend.setter
    def attributeSpend(self, attributeSpend: int):
        self.__attributeSpend = attributeSpend

    @property
    def knownlegePointSpend(self) -> int:
        return self.__knownlegePointSpend

    @knownlegePointSpend.setter
    def knownlegePointSpend(self, knownlegePointSpend: int):
        self.__knownlegePointSpend = knownlegePointSpend

    @property
    def karmaToResource(self) -> int:
        return self.__karmaToResource

    @karmaToResource.setter
    def karmaToResource(self, karmaToResource: int):
        self.__karmaToResource = karmaToResource

    @property
    def spellPointSpend(self) -> int:
        return self.__spellPointSpend

    @spellPointSpend.setter
    def spellPointSpend(self, spellPointSpend: int):
        self.__spellPointSpend = spellPointSpend

    @property
    def startResources(self) -> int:
        return self.__startResources

    @startResources.setter
    def startResources(self, startResources: int):
        self.__startResources = startResources

    @property
    def resourceSpend(self) -> int:
        return self.__resourceSpend

    @resourceSpend.setter
    def resourceSpend(self, resourceSpend: int):
        self.__resourceSpend = resourceSpend

    @property
    def specialPointSpend(self) -> int:
        return self.__specialPointSpend

    @specialPointSpend.setter
    def specialPointSpend(self, specialPointSpend: int):
        self.__specialPointSpend = specialPointSpend

    @property
    def karmaSpend(self) -> int:
        return self.__karmaSpend

    @karmaSpend.setter
    def karmaSpend(self, karmaSpend: int):
        self.__karmaSpend = karmaSpend

    @property
    def groupPointSpend(self) -> int:
        return self.__groupPointSpend

    @groupPointSpend.setter
    def groupPointSpend(self, groupPointSpend: int):
        self.__groupPointSpend = groupPointSpend

    @property
    def startKarma(self) -> int:
        return self.__startKarma

    @startKarma.setter
    def startKarma(self, startKarma: int):
        self.__startKarma = startKarma

    @property
    def skillPointSpend(self) -> int:
        return self.__skillPointSpend

    @skillPointSpend.setter
    def skillPointSpend(self, skillPointSpend: int):
        self.__skillPointSpend = skillPointSpend

    @property
    def connectionSpend(self) -> int:
        return self.__connectionSpend

    @connectionSpend.setter
    def connectionSpend(self, connectionSpend: int):
        self.__connectionSpend = connectionSpend

    @property
    def shr5Management_Shr5Generator48(self):
        return self.__shr5Management_Shr5Generator48

    @shr5Management_Shr5Generator48.setter
    def shr5Management_Shr5Generator48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5Generator__shr5Management_Shr5Generator48", None)
        self.__shr5Management_Shr5Generator48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Attributes"):
                opp_val = getattr(old_value, "shr5Management_Attributes", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Attributes"):
                opp_val = getattr(value, "shr5Management_Attributes", None)
                setattr(value, "shr5Management_Attributes", self)

    @property
    def shr5Management_Shr5Generator50(self):
        return self.__shr5Management_Shr5Generator50

    @shr5Management_Shr5Generator50.setter
    def shr5Management_Shr5Generator50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5Generator__shr5Management_Shr5Generator50", None)
        self.__shr5Management_Shr5Generator50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_MetaType51"):
                opp_val = getattr(old_value, "shr5Management_MetaType51", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_MetaType51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_MetaType51"):
                opp_val = getattr(value, "shr5Management_MetaType51", None)
                setattr(value, "shr5Management_MetaType51", self)

    @property
    def shr5Management_Shr5Generator(self):
        return self.__shr5Management_Shr5Generator

    @shr5Management_Shr5Generator.setter
    def shr5Management_Shr5Generator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5Generator__shr5Management_Shr5Generator", None)
        self.__shr5Management_Shr5Generator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Resourcen"):
                opp_val = getattr(old_value, "shr5Management_Resourcen", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Resourcen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Resourcen"):
                opp_val = getattr(value, "shr5Management_Resourcen", None)
                setattr(value, "shr5Management_Resourcen", self)

    @property
    def shr5Management_Shr5Generator53(self):
        return self.__shr5Management_Shr5Generator53

    @shr5Management_Shr5Generator53.setter
    def shr5Management_Shr5Generator53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5Generator__shr5Management_Shr5Generator53", None)
        self.__shr5Management_Shr5Generator53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_SpecialType54"):
                opp_val = getattr(old_value, "shr5Management_SpecialType54", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_SpecialType54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_SpecialType54"):
                opp_val = getattr(value, "shr5Management_SpecialType54", None)
                setattr(value, "shr5Management_SpecialType54", self)

    @property
    def shr5Management_Shr5Generator46(self):
        return self.__shr5Management_Shr5Generator46

    @shr5Management_Shr5Generator46.setter
    def shr5Management_Shr5Generator46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5Generator__shr5Management_Shr5Generator46", None)
        self.__shr5Management_Shr5Generator46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Skill"):
                opp_val = getattr(old_value, "shr5Management_Skill", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Skill", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Skill"):
                opp_val = getattr(value, "shr5Management_Skill", None)
                setattr(value, "shr5Management_Skill", self)

    def hasSpendAllAttributesPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllAttributesPoints method
        pass

    def hasSpendAllConnectionPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllConnectionPoints method
        pass

    def hasSpendAllSkillPoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllSkillPoints method
        pass

    def hasSpendAllSpecialPoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllSpecialPoints method
        pass

    def hasSpendAllSpellPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllSpellPoints method
        pass

    def hasSpendAllResourcePoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllResourcePoints method
        pass

    def hasSpendAllSpecialTypePoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllSpecialTypePoints method
        pass

    def hasSpendAllMagicPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllMagicPoints method
        pass

    def hasCategoryOnlyOnce(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasCategoryOnlyOnce method
        pass

    def hasSpendAllGroupPoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllGroupPoints method
        pass

    def hasNotMoreMaxAttributes(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasNotMoreMaxAttributes method
        pass

    def hasSpendAllKnowlegeSkillPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllKnowlegeSkillPoints method
        pass

    def hasSpendAllKarmaPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllKarmaPoints method
        pass

    def hasSpendAllMagicSkillsPoints(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement hasSpendAllMagicSkillsPoints method
        pass

    def hasSpendAllPowerPoints(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement hasSpendAllPowerPoints method
        pass

class shr5Management_FreeStyleGenerator:

    pass
class PriorityCategorie:

    pass
class shr5Management_MetaType(PriorityCategorie):

    def __init__(self, specialPoints: int, shr5Management_MetaType: "shr5Management_Spezies" = None, shr5Management_MetaType51: "shr5Management_Shr5Generator" = None, shr5Management_MetaType86: "shr5Management_KarmaGenerator" = None):
        self.specialPoints = specialPoints
        self.shr5Management_MetaType = shr5Management_MetaType
        self.shr5Management_MetaType51 = shr5Management_MetaType51
        self.shr5Management_MetaType86 = shr5Management_MetaType86
        
    @property
    def specialPoints(self) -> int:
        return self.__specialPoints

    @specialPoints.setter
    def specialPoints(self, specialPoints: int):
        self.__specialPoints = specialPoints

    @property
    def shr5Management_MetaType51(self):
        return self.__shr5Management_MetaType51

    @shr5Management_MetaType51.setter
    def shr5Management_MetaType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_MetaType__shr5Management_MetaType51", None)
        self.__shr5Management_MetaType51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Shr5Generator50"):
                opp_val = getattr(old_value, "shr5Management_Shr5Generator50", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Shr5Generator50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Shr5Generator50"):
                opp_val = getattr(value, "shr5Management_Shr5Generator50", None)
                setattr(value, "shr5Management_Shr5Generator50", self)

    @property
    def shr5Management_MetaType86(self):
        return self.__shr5Management_MetaType86

    @shr5Management_MetaType86.setter
    def shr5Management_MetaType86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_MetaType__shr5Management_MetaType86", None)
        self.__shr5Management_MetaType86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_KarmaGenerator"):
                opp_val = getattr(old_value, "shr5Management_KarmaGenerator", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_KarmaGenerator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_KarmaGenerator"):
                opp_val = getattr(value, "shr5Management_KarmaGenerator", None)
                setattr(value, "shr5Management_KarmaGenerator", self)

    @property
    def shr5Management_MetaType(self):
        return self.__shr5Management_MetaType

    @shr5Management_MetaType.setter
    def shr5Management_MetaType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_MetaType__shr5Management_MetaType", None)
        self.__shr5Management_MetaType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Spezies"):
                opp_val = getattr(old_value, "shr5Management_Spezies", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Spezies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Spezies"):
                opp_val = getattr(value, "shr5Management_Spezies", None)
                setattr(value, "shr5Management_Spezies", self)

    def calcSpecialPointsSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcSpecialPointsSpend method
        pass

class shr5Management_EClass:

    pass
class SpecialType:

    pass
class shr5Management_Adept(SpecialType):

    def __init__(self, magic: int):
        self.magic = magic
        
    @property
    def magic(self) -> int:
        return self.__magic

    @magic.setter
    def magic(self, magic: int):
        self.__magic = magic

    def calcPowerPointsSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcPowerPointsSpend method
        pass

class shr5Management_Mudan(SpecialType):

    pass
class shr5Management_Technomancer(SpecialType):

    def __init__(self, resonanz: int, complexForms: int):
        self.resonanz = resonanz
        self.complexForms = complexForms
        
    @property
    def resonanz(self) -> int:
        return self.__resonanz

    @resonanz.setter
    def resonanz(self, resonanz: int):
        self.__resonanz = resonanz

    @property
    def complexForms(self) -> int:
        return self.__complexForms

    @complexForms.setter
    def complexForms(self, complexForms: int):
        self.__complexForms = complexForms

    def calcComplexFormsSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcComplexFormsSpend method
        pass

class shr5Management_FertigkeitsGruppe:

    pass
class shr5Management_Fertigkeit:

    pass
class shr5Management_SpecialType(PriorityCategorie):

    def __init__(self, skillValue: int, skillNumber: int, shr5Management_SpecialType: "shr5Management_EClass" = None, shr5Management_SpecialType28: set["shr5Management_Fertigkeit"] = None, shr5Management_SpecialType30: set["shr5Management_FertigkeitsGruppe"] = None, shr5Management_SpecialType54: "shr5Management_Shr5Generator" = None, shr5Management_SpecialType89: "shr5Management_KarmaGenerator" = None):
        self.skillValue = skillValue
        self.skillNumber = skillNumber
        self.shr5Management_SpecialType = shr5Management_SpecialType
        self.shr5Management_SpecialType28 = shr5Management_SpecialType28 if shr5Management_SpecialType28 is not None else set()
        self.shr5Management_SpecialType30 = shr5Management_SpecialType30 if shr5Management_SpecialType30 is not None else set()
        self.shr5Management_SpecialType54 = shr5Management_SpecialType54
        self.shr5Management_SpecialType89 = shr5Management_SpecialType89
        
    @property
    def skillNumber(self) -> int:
        return self.__skillNumber

    @skillNumber.setter
    def skillNumber(self, skillNumber: int):
        self.__skillNumber = skillNumber

    @property
    def skillValue(self) -> int:
        return self.__skillValue

    @skillValue.setter
    def skillValue(self, skillValue: int):
        self.__skillValue = skillValue

    @property
    def shr5Management_SpecialType(self):
        return self.__shr5Management_SpecialType

    @shr5Management_SpecialType.setter
    def shr5Management_SpecialType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_SpecialType__shr5Management_SpecialType", None)
        self.__shr5Management_SpecialType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_EClass26"):
                opp_val = getattr(old_value, "shr5Management_EClass26", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_EClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_EClass26"):
                opp_val = getattr(value, "shr5Management_EClass26", None)
                setattr(value, "shr5Management_EClass26", self)

    @property
    def shr5Management_SpecialType89(self):
        return self.__shr5Management_SpecialType89

    @shr5Management_SpecialType89.setter
    def shr5Management_SpecialType89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_SpecialType__shr5Management_SpecialType89", None)
        self.__shr5Management_SpecialType89 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_KarmaGenerator88"):
                opp_val = getattr(old_value, "shr5Management_KarmaGenerator88", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_KarmaGenerator88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_KarmaGenerator88"):
                opp_val = getattr(value, "shr5Management_KarmaGenerator88", None)
                setattr(value, "shr5Management_KarmaGenerator88", self)

    @property
    def shr5Management_SpecialType28(self):
        return self.__shr5Management_SpecialType28

    @shr5Management_SpecialType28.setter
    def shr5Management_SpecialType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_SpecialType__shr5Management_SpecialType28", None)
        self.__shr5Management_SpecialType28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Fertigkeit"):
                    opp_val = getattr(item, "shr5Management_Fertigkeit", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Fertigkeit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Fertigkeit"):
                    opp_val = getattr(item, "shr5Management_Fertigkeit", None)
                    
                    setattr(item, "shr5Management_Fertigkeit", self)
                    

    @property
    def shr5Management_SpecialType30(self):
        return self.__shr5Management_SpecialType30

    @shr5Management_SpecialType30.setter
    def shr5Management_SpecialType30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_SpecialType__shr5Management_SpecialType30", None)
        self.__shr5Management_SpecialType30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_FertigkeitsGruppe"):
                    opp_val = getattr(item, "shr5Management_FertigkeitsGruppe", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_FertigkeitsGruppe", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_FertigkeitsGruppe"):
                    opp_val = getattr(item, "shr5Management_FertigkeitsGruppe", None)
                    
                    setattr(item, "shr5Management_FertigkeitsGruppe", self)
                    

    @property
    def shr5Management_SpecialType54(self):
        return self.__shr5Management_SpecialType54

    @shr5Management_SpecialType54.setter
    def shr5Management_SpecialType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_SpecialType__shr5Management_SpecialType54", None)
        self.__shr5Management_SpecialType54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Shr5Generator53"):
                opp_val = getattr(old_value, "shr5Management_Shr5Generator53", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Shr5Generator53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Shr5Generator53"):
                opp_val = getattr(value, "shr5Management_Shr5Generator53", None)
                setattr(value, "shr5Management_Shr5Generator53", self)

    def calcSkillsSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcSkillsSpend method
        pass

class shr5Management_Resourcen(PriorityCategorie):

    def __init__(self, resource: int, shr5Management_Resourcen: "shr5Management_Shr5Generator" = None):
        self.resource = resource
        self.shr5Management_Resourcen = shr5Management_Resourcen
        
    @property
    def resource(self) -> int:
        return self.__resource

    @resource.setter
    def resource(self, resource: int):
        self.__resource = resource

    @property
    def shr5Management_Resourcen(self):
        return self.__shr5Management_Resourcen

    @shr5Management_Resourcen.setter
    def shr5Management_Resourcen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Resourcen__shr5Management_Resourcen", None)
        self.__shr5Management_Resourcen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Shr5Generator"):
                opp_val = getattr(old_value, "shr5Management_Shr5Generator", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Shr5Generator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Shr5Generator"):
                opp_val = getattr(value, "shr5Management_Shr5Generator", None)
                setattr(value, "shr5Management_Shr5Generator", self)

    def calcResourceSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcResourceSpend method
        pass

class shr5Management_Skill(PriorityCategorie):

    def __init__(self, skillPoints: int, groupPoints: int, shr5Management_Skill: "shr5Management_Shr5Generator" = None):
        self.skillPoints = skillPoints
        self.groupPoints = groupPoints
        self.shr5Management_Skill = shr5Management_Skill
        
    @property
    def groupPoints(self) -> int:
        return self.__groupPoints

    @groupPoints.setter
    def groupPoints(self, groupPoints: int):
        self.__groupPoints = groupPoints

    @property
    def skillPoints(self) -> int:
        return self.__skillPoints

    @skillPoints.setter
    def skillPoints(self, skillPoints: int):
        self.__skillPoints = skillPoints

    @property
    def shr5Management_Skill(self):
        return self.__shr5Management_Skill

    @shr5Management_Skill.setter
    def shr5Management_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Skill__shr5Management_Skill", None)
        self.__shr5Management_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Shr5Generator46"):
                opp_val = getattr(old_value, "shr5Management_Shr5Generator46", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Shr5Generator46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Shr5Generator46"):
                opp_val = getattr(value, "shr5Management_Shr5Generator46", None)
                setattr(value, "shr5Management_Shr5Generator46", self)

    def calcSkillSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcSkillSpend method
        pass

    def calcGroupSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcGroupSpend method
        pass

    def calcKnowledgeSkillPoints(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcKnowledgeSkillPoints method
        pass

    def calcKnowledgeSkillSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcKnowledgeSkillSpend method
        pass

class shr5Management_Attributes(PriorityCategorie):

    def __init__(self, attibutePoints: int, shr5Management_Attributes: "shr5Management_Shr5Generator" = None):
        self.attibutePoints = attibutePoints
        self.shr5Management_Attributes = shr5Management_Attributes
        
    @property
    def attibutePoints(self) -> int:
        return self.__attibutePoints

    @attibutePoints.setter
    def attibutePoints(self, attibutePoints: int):
        self.__attibutePoints = attibutePoints

    @property
    def shr5Management_Attributes(self):
        return self.__shr5Management_Attributes

    @shr5Management_Attributes.setter
    def shr5Management_Attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Attributes__shr5Management_Attributes", None)
        self.__shr5Management_Attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Shr5Generator48"):
                opp_val = getattr(old_value, "shr5Management_Shr5Generator48", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Shr5Generator48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Shr5Generator48"):
                opp_val = getattr(value, "shr5Management_Shr5Generator48", None)
                setattr(value, "shr5Management_Shr5Generator48", self)

    def calcAttributesSpend(self, context: ManagedCharacter) -> int:
        # TODO: Implement calcAttributesSpend method
        pass

class shr5Management_Spezies:

    pass
class ManagedCharacter:

    pass
class shr5Management_PlayerCharacter(ManagedCharacter):

    def __init__(self, age: int, shr5Management_PlayerCharacter: "shr5Management_CharacterDiary" = None):
        self.age = age
        self.shr5Management_PlayerCharacter = shr5Management_PlayerCharacter
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def shr5Management_PlayerCharacter(self):
        return self.__shr5Management_PlayerCharacter

    @shr5Management_PlayerCharacter.setter
    def shr5Management_PlayerCharacter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_PlayerCharacter__shr5Management_PlayerCharacter", None)
        self.__shr5Management_PlayerCharacter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterDiary"):
                opp_val = getattr(old_value, "shr5Management_CharacterDiary", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_CharacterDiary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterDiary"):
                opp_val = getattr(value, "shr5Management_CharacterDiary", None)
                setattr(value, "shr5Management_CharacterDiary", self)

class shr5Management_NonPlayerCharacter(ManagedCharacter):

    pass
class shr5Management_PriorityCategorie(ABC):

    def __init__(self, categorieName: str, cost: int, shr5Management_PriorityCategorie: "shr5Management_PrioritySystem" = None):
        self.categorieName = categorieName
        self.cost = cost
        self.shr5Management_PriorityCategorie = shr5Management_PriorityCategorie
        
    @property
    def cost(self) -> int:
        return self.__cost

    @cost.setter
    def cost(self, cost: int):
        self.__cost = cost

    @property
    def categorieName(self) -> str:
        return self.__categorieName

    @categorieName.setter
    def categorieName(self, categorieName: str):
        self.__categorieName = categorieName

    @property
    def shr5Management_PriorityCategorie(self):
        return self.__shr5Management_PriorityCategorie

    @shr5Management_PriorityCategorie.setter
    def shr5Management_PriorityCategorie(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_PriorityCategorie__shr5Management_PriorityCategorie", None)
        self.__shr5Management_PriorityCategorie = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_PrioritySystem"):
                opp_val = getattr(old_value, "shr5Management_PrioritySystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_PrioritySystem"):
                opp_val = getattr(value, "shr5Management_PrioritySystem", None)
                if opp_val is None:
                    setattr(value, "shr5Management_PrioritySystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CharacterGeneratorSystem:

    pass
class shr5Management_PrioritySystem(CharacterGeneratorSystem):

    def __init__(self, karmaPoints: int, shr5Management_PrioritySystem: set["shr5Management_PriorityCategorie"] = None):
        self.karmaPoints = karmaPoints
        self.shr5Management_PrioritySystem = shr5Management_PrioritySystem if shr5Management_PrioritySystem is not None else set()
        
    @property
    def karmaPoints(self) -> int:
        return self.__karmaPoints

    @karmaPoints.setter
    def karmaPoints(self, karmaPoints: int):
        self.__karmaPoints = karmaPoints

    @property
    def shr5Management_PrioritySystem(self):
        return self.__shr5Management_PrioritySystem

    @shr5Management_PrioritySystem.setter
    def shr5Management_PrioritySystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_PrioritySystem__shr5Management_PrioritySystem", None)
        self.__shr5Management_PrioritySystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_PriorityCategorie"):
                    opp_val = getattr(item, "shr5Management_PriorityCategorie", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_PriorityCategorie", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_PriorityCategorie"):
                    opp_val = getattr(item, "shr5Management_PriorityCategorie", None)
                    
                    setattr(item, "shr5Management_PriorityCategorie", self)
                    

class PrioritySystem:

    pass
class shr5Management_Shr5System(PrioritySystem):

    def __init__(self, karmaToResourceFactor: int, karmaToMagicFactor: int, numberOfMaxAttributes: int, knowlegeSkillFactor: int, charismaToConnectionFactor: int, maxResourceToKeep: int, maxKarmaToResources: int, maxKarmaToKeep: int, skillMax: int, numberOfSpecalism: int, karmaToConnectionFactor: int, boundSprititServiceCost: int, maxConnectionRating: int, freeMartialArtTechniques: int, maxMartialArtStyles: int, sumToTenValue: int, shr5Management_Shr5System: set["shr5Management_EClass"] = None):
        self.karmaToResourceFactor = karmaToResourceFactor
        self.karmaToMagicFactor = karmaToMagicFactor
        self.numberOfMaxAttributes = numberOfMaxAttributes
        self.knowlegeSkillFactor = knowlegeSkillFactor
        self.charismaToConnectionFactor = charismaToConnectionFactor
        self.maxResourceToKeep = maxResourceToKeep
        self.maxKarmaToResources = maxKarmaToResources
        self.maxKarmaToKeep = maxKarmaToKeep
        self.skillMax = skillMax
        self.numberOfSpecalism = numberOfSpecalism
        self.karmaToConnectionFactor = karmaToConnectionFactor
        self.boundSprititServiceCost = boundSprititServiceCost
        self.maxConnectionRating = maxConnectionRating
        self.freeMartialArtTechniques = freeMartialArtTechniques
        self.maxMartialArtStyles = maxMartialArtStyles
        self.sumToTenValue = sumToTenValue
        self.shr5Management_Shr5System = shr5Management_Shr5System if shr5Management_Shr5System is not None else set()
        
    @property
    def charismaToConnectionFactor(self) -> int:
        return self.__charismaToConnectionFactor

    @charismaToConnectionFactor.setter
    def charismaToConnectionFactor(self, charismaToConnectionFactor: int):
        self.__charismaToConnectionFactor = charismaToConnectionFactor

    @property
    def maxResourceToKeep(self) -> int:
        return self.__maxResourceToKeep

    @maxResourceToKeep.setter
    def maxResourceToKeep(self, maxResourceToKeep: int):
        self.__maxResourceToKeep = maxResourceToKeep

    @property
    def maxConnectionRating(self) -> int:
        return self.__maxConnectionRating

    @maxConnectionRating.setter
    def maxConnectionRating(self, maxConnectionRating: int):
        self.__maxConnectionRating = maxConnectionRating

    @property
    def numberOfSpecalism(self) -> int:
        return self.__numberOfSpecalism

    @numberOfSpecalism.setter
    def numberOfSpecalism(self, numberOfSpecalism: int):
        self.__numberOfSpecalism = numberOfSpecalism

    @property
    def numberOfMaxAttributes(self) -> int:
        return self.__numberOfMaxAttributes

    @numberOfMaxAttributes.setter
    def numberOfMaxAttributes(self, numberOfMaxAttributes: int):
        self.__numberOfMaxAttributes = numberOfMaxAttributes

    @property
    def maxKarmaToKeep(self) -> int:
        return self.__maxKarmaToKeep

    @maxKarmaToKeep.setter
    def maxKarmaToKeep(self, maxKarmaToKeep: int):
        self.__maxKarmaToKeep = maxKarmaToKeep

    @property
    def freeMartialArtTechniques(self) -> int:
        return self.__freeMartialArtTechniques

    @freeMartialArtTechniques.setter
    def freeMartialArtTechniques(self, freeMartialArtTechniques: int):
        self.__freeMartialArtTechniques = freeMartialArtTechniques

    @property
    def maxMartialArtStyles(self) -> int:
        return self.__maxMartialArtStyles

    @maxMartialArtStyles.setter
    def maxMartialArtStyles(self, maxMartialArtStyles: int):
        self.__maxMartialArtStyles = maxMartialArtStyles

    @property
    def maxKarmaToResources(self) -> int:
        return self.__maxKarmaToResources

    @maxKarmaToResources.setter
    def maxKarmaToResources(self, maxKarmaToResources: int):
        self.__maxKarmaToResources = maxKarmaToResources

    @property
    def boundSprititServiceCost(self) -> int:
        return self.__boundSprititServiceCost

    @boundSprititServiceCost.setter
    def boundSprititServiceCost(self, boundSprititServiceCost: int):
        self.__boundSprititServiceCost = boundSprititServiceCost

    @property
    def karmaToConnectionFactor(self) -> int:
        return self.__karmaToConnectionFactor

    @karmaToConnectionFactor.setter
    def karmaToConnectionFactor(self, karmaToConnectionFactor: int):
        self.__karmaToConnectionFactor = karmaToConnectionFactor

    @property
    def knowlegeSkillFactor(self) -> int:
        return self.__knowlegeSkillFactor

    @knowlegeSkillFactor.setter
    def knowlegeSkillFactor(self, knowlegeSkillFactor: int):
        self.__knowlegeSkillFactor = knowlegeSkillFactor

    @property
    def karmaToMagicFactor(self) -> int:
        return self.__karmaToMagicFactor

    @karmaToMagicFactor.setter
    def karmaToMagicFactor(self, karmaToMagicFactor: int):
        self.__karmaToMagicFactor = karmaToMagicFactor

    @property
    def sumToTenValue(self) -> int:
        return self.__sumToTenValue

    @sumToTenValue.setter
    def sumToTenValue(self, sumToTenValue: int):
        self.__sumToTenValue = sumToTenValue

    @property
    def skillMax(self) -> int:
        return self.__skillMax

    @skillMax.setter
    def skillMax(self, skillMax: int):
        self.__skillMax = skillMax

    @property
    def karmaToResourceFactor(self) -> int:
        return self.__karmaToResourceFactor

    @karmaToResourceFactor.setter
    def karmaToResourceFactor(self, karmaToResourceFactor: int):
        self.__karmaToResourceFactor = karmaToResourceFactor

    @property
    def shr5Management_Shr5System(self):
        return self.__shr5Management_Shr5System

    @shr5Management_Shr5System.setter
    def shr5Management_Shr5System(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Shr5System__shr5Management_Shr5System", None)
        self.__shr5Management_Shr5System = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_EClass"):
                    opp_val = getattr(item, "shr5Management_EClass", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_EClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_EClass"):
                    opp_val = getattr(item, "shr5Management_EClass", None)
                    
                    setattr(item, "shr5Management_EClass", self)
                    

class shr5Management_FreeStyle(CharacterGeneratorSystem):

    pass
class Changes:

    pass
class shr5Management_PersonaValueChange(Changes):

    def __init__(self, from: int, to: int):
        self.from = from
        self.to = to
        
    @property
    def from(self) -> int:
        return self.__from

    @from.setter
    def from(self, from: int):
        self.__from = from

    @property
    def to(self) -> int:
        return self.__to

    @to.setter
    def to(self, to: int):
        self.__to = to

class shr5Management_KarmaGaint(Changes):

    def __init__(self, karma: int):
        self.karma = karma
        
    @property
    def karma(self) -> int:
        return self.__karma

    @karma.setter
    def karma(self, karma: int):
        self.__karma = karma

class shr5Management_Sprachfertigkeit:

    pass
class shr5Management_Lifestyle:

    pass
class shr5Management_Fahrzeug:

    pass
class shr5Management_Connection:

    def __init__(self, influence: int, loyality: int, shr5Management_Connection: "shr5Management_ManagedCharacter" = None, shr5Management_Connection61: "shr5Management_ManagedCharacter" = None):
        self.influence = influence
        self.loyality = loyality
        self.shr5Management_Connection = shr5Management_Connection
        self.shr5Management_Connection61 = shr5Management_Connection61
        
    @property
    def loyality(self) -> int:
        return self.__loyality

    @loyality.setter
    def loyality(self, loyality: int):
        self.__loyality = loyality

    @property
    def influence(self) -> int:
        return self.__influence

    @influence.setter
    def influence(self, influence: int):
        self.__influence = influence

    @property
    def shr5Management_Connection(self):
        return self.__shr5Management_Connection

    @shr5Management_Connection.setter
    def shr5Management_Connection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Connection__shr5Management_Connection", None)
        self.__shr5Management_Connection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_ManagedCharacter7"):
                opp_val = getattr(old_value, "shr5Management_ManagedCharacter7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_ManagedCharacter7"):
                opp_val = getattr(value, "shr5Management_ManagedCharacter7", None)
                if opp_val is None:
                    setattr(value, "shr5Management_ManagedCharacter7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_Connection61(self):
        return self.__shr5Management_Connection61

    @shr5Management_Connection61.setter
    def shr5Management_Connection61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Connection__shr5Management_Connection61", None)
        self.__shr5Management_Connection61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_ManagedCharacter62"):
                opp_val = getattr(old_value, "shr5Management_ManagedCharacter62", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_ManagedCharacter62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_ManagedCharacter62"):
                opp_val = getattr(value, "shr5Management_ManagedCharacter62", None)
                setattr(value, "shr5Management_ManagedCharacter62", self)

class shr5Management_Vertrag:

    pass
class shr5Management_AbstraktGegenstand:

    pass
class shr5Management_QuellenConstrain:

    def __init__(self, constrainType: str, shr5Management_QuellenConstrain: "shr5Management_CharacterGeneratorSystem" = None, shr5Management_QuellenConstrain91: "shr5Management_Quelle" = None, shr5Management_QuellenConstrain93: set["shr5Management_Quelle"] = None):
        self.constrainType = constrainType
        self.shr5Management_QuellenConstrain = shr5Management_QuellenConstrain
        self.shr5Management_QuellenConstrain91 = shr5Management_QuellenConstrain91
        self.shr5Management_QuellenConstrain93 = shr5Management_QuellenConstrain93 if shr5Management_QuellenConstrain93 is not None else set()
        
    @property
    def constrainType(self) -> str:
        return self.__constrainType

    @constrainType.setter
    def constrainType(self, constrainType: str):
        self.__constrainType = constrainType

    @property
    def shr5Management_QuellenConstrain91(self):
        return self.__shr5Management_QuellenConstrain91

    @shr5Management_QuellenConstrain91.setter
    def shr5Management_QuellenConstrain91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_QuellenConstrain__shr5Management_QuellenConstrain91", None)
        self.__shr5Management_QuellenConstrain91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Quelle"):
                opp_val = getattr(old_value, "shr5Management_Quelle", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Quelle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Quelle"):
                opp_val = getattr(value, "shr5Management_Quelle", None)
                setattr(value, "shr5Management_Quelle", self)

    @property
    def shr5Management_QuellenConstrain93(self):
        return self.__shr5Management_QuellenConstrain93

    @shr5Management_QuellenConstrain93.setter
    def shr5Management_QuellenConstrain93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_QuellenConstrain__shr5Management_QuellenConstrain93", None)
        self.__shr5Management_QuellenConstrain93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Quelle94"):
                    opp_val = getattr(item, "shr5Management_Quelle94", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Quelle94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Quelle94"):
                    opp_val = getattr(item, "shr5Management_Quelle94", None)
                    
                    setattr(item, "shr5Management_Quelle94", self)
                    

    @property
    def shr5Management_QuellenConstrain(self):
        return self.__shr5Management_QuellenConstrain

    @shr5Management_QuellenConstrain.setter
    def shr5Management_QuellenConstrain(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_QuellenConstrain__shr5Management_QuellenConstrain", None)
        self.__shr5Management_QuellenConstrain = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterGeneratorSystem20"):
                opp_val = getattr(old_value, "shr5Management_CharacterGeneratorSystem20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterGeneratorSystem20"):
                opp_val = getattr(value, "shr5Management_CharacterGeneratorSystem20", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterGeneratorSystem20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5Management_LifestyleToStartMoney:

    def __init__(self, numberOfW: int, moneyFactor: int, shr5Management_LifestyleToStartMoney: "shr5Management_CharacterGeneratorSystem" = None, shr5Management_LifestyleToStartMoney67: set["shr5Management_Lifestyle"] = None):
        self.numberOfW = numberOfW
        self.moneyFactor = moneyFactor
        self.shr5Management_LifestyleToStartMoney = shr5Management_LifestyleToStartMoney
        self.shr5Management_LifestyleToStartMoney67 = shr5Management_LifestyleToStartMoney67 if shr5Management_LifestyleToStartMoney67 is not None else set()
        
    @property
    def numberOfW(self) -> int:
        return self.__numberOfW

    @numberOfW.setter
    def numberOfW(self, numberOfW: int):
        self.__numberOfW = numberOfW

    @property
    def moneyFactor(self) -> int:
        return self.__moneyFactor

    @moneyFactor.setter
    def moneyFactor(self, moneyFactor: int):
        self.__moneyFactor = moneyFactor

    @property
    def shr5Management_LifestyleToStartMoney(self):
        return self.__shr5Management_LifestyleToStartMoney

    @shr5Management_LifestyleToStartMoney.setter
    def shr5Management_LifestyleToStartMoney(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifestyleToStartMoney__shr5Management_LifestyleToStartMoney", None)
        self.__shr5Management_LifestyleToStartMoney = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterGeneratorSystem16"):
                opp_val = getattr(old_value, "shr5Management_CharacterGeneratorSystem16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterGeneratorSystem16"):
                opp_val = getattr(value, "shr5Management_CharacterGeneratorSystem16", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterGeneratorSystem16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_LifestyleToStartMoney67(self):
        return self.__shr5Management_LifestyleToStartMoney67

    @shr5Management_LifestyleToStartMoney67.setter
    def shr5Management_LifestyleToStartMoney67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifestyleToStartMoney__shr5Management_LifestyleToStartMoney67", None)
        self.__shr5Management_LifestyleToStartMoney67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Lifestyle68"):
                    opp_val = getattr(item, "shr5Management_Lifestyle68", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Lifestyle68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Lifestyle68"):
                    opp_val = getattr(item, "shr5Management_Lifestyle68", None)
                    
                    setattr(item, "shr5Management_Lifestyle68", self)
                    

class shr5Management_GeneratorStateToEStringMapEntry:

    def __init__(self, key: str, value: str, shr5Management_GeneratorStateToEStringMapEntry: "shr5Management_CharacterGeneratorSystem" = None):
        self.key = key
        self.value = value
        self.shr5Management_GeneratorStateToEStringMapEntry = shr5Management_GeneratorStateToEStringMapEntry
        
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
    def shr5Management_GeneratorStateToEStringMapEntry(self):
        return self.__shr5Management_GeneratorStateToEStringMapEntry

    @shr5Management_GeneratorStateToEStringMapEntry.setter
    def shr5Management_GeneratorStateToEStringMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GeneratorStateToEStringMapEntry__shr5Management_GeneratorStateToEStringMapEntry", None)
        self.__shr5Management_GeneratorStateToEStringMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterGeneratorSystem"):
                opp_val = getattr(old_value, "shr5Management_CharacterGeneratorSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterGeneratorSystem"):
                opp_val = getattr(value, "shr5Management_CharacterGeneratorSystem", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterGeneratorSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Quelle:

    pass
class Beschreibbar:

    pass
class shr5Management_GruntGroup(Beschreibbar):

    def __init__(self, professionalRating: int, shr5Management_GruntGroup: set["shr5Management_GruntMembers"] = None, shr5Management_GruntGroup71: "shr5Management_GruntMembers" = None, shr5Management_GruntGroup81: "shr5Management_GamemasterManagement" = None):
        self.professionalRating = professionalRating
        self.shr5Management_GruntGroup = shr5Management_GruntGroup if shr5Management_GruntGroup is not None else set()
        self.shr5Management_GruntGroup71 = shr5Management_GruntGroup71
        self.shr5Management_GruntGroup81 = shr5Management_GruntGroup81
        
    @property
    def professionalRating(self) -> int:
        return self.__professionalRating

    @professionalRating.setter
    def professionalRating(self, professionalRating: int):
        self.__professionalRating = professionalRating

    @property
    def shr5Management_GruntGroup(self):
        return self.__shr5Management_GruntGroup

    @shr5Management_GruntGroup.setter
    def shr5Management_GruntGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntGroup__shr5Management_GruntGroup", None)
        self.__shr5Management_GruntGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_GruntMembers"):
                    opp_val = getattr(item, "shr5Management_GruntMembers", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_GruntMembers", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_GruntMembers"):
                    opp_val = getattr(item, "shr5Management_GruntMembers", None)
                    
                    setattr(item, "shr5Management_GruntMembers", self)
                    

    @property
    def shr5Management_GruntGroup71(self):
        return self.__shr5Management_GruntGroup71

    @shr5Management_GruntGroup71.setter
    def shr5Management_GruntGroup71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntGroup__shr5Management_GruntGroup71", None)
        self.__shr5Management_GruntGroup71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_GruntMembers72"):
                opp_val = getattr(old_value, "shr5Management_GruntMembers72", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_GruntMembers72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_GruntMembers72"):
                opp_val = getattr(value, "shr5Management_GruntMembers72", None)
                setattr(value, "shr5Management_GruntMembers72", self)

    @property
    def shr5Management_GruntGroup81(self):
        return self.__shr5Management_GruntGroup81

    @shr5Management_GruntGroup81.setter
    def shr5Management_GruntGroup81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_GruntGroup__shr5Management_GruntGroup81", None)
        self.__shr5Management_GruntGroup81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_GamemasterManagement"):
                opp_val = getattr(old_value, "shr5Management_GamemasterManagement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_GamemasterManagement"):
                opp_val = getattr(value, "shr5Management_GamemasterManagement", None)
                if opp_val is None:
                    setattr(value, "shr5Management_GamemasterManagement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shr5Management_CharacterGroup(Beschreibbar):

    pass
class shr5Management_Pack(Quelle, GeldWert, Beschreibbar):

    pass
class shr5Management_LifeModule(Quelle, Beschreibbar):

    def __init__(self, karmaCost: int, moduleType: str, time: int, shr5Management_LifeModule114: "shr5Management_LifeModulesGenerator" = None, shr5Management_LifeModule116: "shr5Management_LifeModulesSystem" = None, shr5Management_LifeModule118: set["shr5Management_ModuleChange"] = None, shr5Management_LifeModule: "shr5Management_LifeModulesGenerator" = None, shr5Management_LifeModule105: "shr5Management_LifeModulesGenerator" = None, shr5Management_LifeModule108: "shr5Management_LifeModulesGenerator" = None, shr5Management_LifeModule111: "shr5Management_LifeModulesGenerator" = None):
        self.karmaCost = karmaCost
        self.moduleType = moduleType
        self.time = time
        self.shr5Management_LifeModule114 = shr5Management_LifeModule114
        self.shr5Management_LifeModule116 = shr5Management_LifeModule116
        self.shr5Management_LifeModule118 = shr5Management_LifeModule118 if shr5Management_LifeModule118 is not None else set()
        self.shr5Management_LifeModule = shr5Management_LifeModule
        self.shr5Management_LifeModule105 = shr5Management_LifeModule105
        self.shr5Management_LifeModule108 = shr5Management_LifeModule108
        self.shr5Management_LifeModule111 = shr5Management_LifeModule111
        
    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def moduleType(self) -> str:
        return self.__moduleType

    @moduleType.setter
    def moduleType(self, moduleType: str):
        self.__moduleType = moduleType

    @property
    def karmaCost(self) -> int:
        return self.__karmaCost

    @karmaCost.setter
    def karmaCost(self, karmaCost: int):
        self.__karmaCost = karmaCost

    @property
    def shr5Management_LifeModule(self):
        return self.__shr5Management_LifeModule

    @shr5Management_LifeModule.setter
    def shr5Management_LifeModule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule", None)
        self.__shr5Management_LifeModule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesGenerator"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesGenerator", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModulesGenerator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesGenerator"):
                opp_val = getattr(value, "shr5Management_LifeModulesGenerator", None)
                setattr(value, "shr5Management_LifeModulesGenerator", self)

    @property
    def shr5Management_LifeModule114(self):
        return self.__shr5Management_LifeModule114

    @shr5Management_LifeModule114.setter
    def shr5Management_LifeModule114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule114", None)
        self.__shr5Management_LifeModule114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesGenerator113"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesGenerator113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesGenerator113"):
                opp_val = getattr(value, "shr5Management_LifeModulesGenerator113", None)
                if opp_val is None:
                    setattr(value, "shr5Management_LifeModulesGenerator113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_LifeModule118(self):
        return self.__shr5Management_LifeModule118

    @shr5Management_LifeModule118.setter
    def shr5Management_LifeModule118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule118", None)
        self.__shr5Management_LifeModule118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_ModuleChange"):
                    opp_val = getattr(item, "shr5Management_ModuleChange", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_ModuleChange", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_ModuleChange"):
                    opp_val = getattr(item, "shr5Management_ModuleChange", None)
                    
                    setattr(item, "shr5Management_ModuleChange", self)
                    

    @property
    def shr5Management_LifeModule111(self):
        return self.__shr5Management_LifeModule111

    @shr5Management_LifeModule111.setter
    def shr5Management_LifeModule111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule111", None)
        self.__shr5Management_LifeModule111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesGenerator110"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesGenerator110", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModulesGenerator110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesGenerator110"):
                opp_val = getattr(value, "shr5Management_LifeModulesGenerator110", None)
                setattr(value, "shr5Management_LifeModulesGenerator110", self)

    @property
    def shr5Management_LifeModule116(self):
        return self.__shr5Management_LifeModule116

    @shr5Management_LifeModule116.setter
    def shr5Management_LifeModule116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule116", None)
        self.__shr5Management_LifeModule116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesSystem"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesSystem"):
                opp_val = getattr(value, "shr5Management_LifeModulesSystem", None)
                if opp_val is None:
                    setattr(value, "shr5Management_LifeModulesSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_LifeModule105(self):
        return self.__shr5Management_LifeModule105

    @shr5Management_LifeModule105.setter
    def shr5Management_LifeModule105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule105", None)
        self.__shr5Management_LifeModule105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesGenerator104"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesGenerator104", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModulesGenerator104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesGenerator104"):
                opp_val = getattr(value, "shr5Management_LifeModulesGenerator104", None)
                setattr(value, "shr5Management_LifeModulesGenerator104", self)

    @property
    def shr5Management_LifeModule108(self):
        return self.__shr5Management_LifeModule108

    @shr5Management_LifeModule108.setter
    def shr5Management_LifeModule108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_LifeModule__shr5Management_LifeModule108", None)
        self.__shr5Management_LifeModule108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_LifeModulesGenerator107"):
                opp_val = getattr(old_value, "shr5Management_LifeModulesGenerator107", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_LifeModulesGenerator107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_LifeModulesGenerator107"):
                opp_val = getattr(value, "shr5Management_LifeModulesGenerator107", None)
                setattr(value, "shr5Management_LifeModulesGenerator107", self)

class shr5Management_CharacterAdvancementSystem(Beschreibbar):

    pass
class shr5Management_PlayerManagement(Beschreibbar):

    pass
class shr5Management_CharacterGeneratorSystem(Quelle, Beschreibbar):

    pass
class shr5Management_Changes(ABC):

    def __init__(self, changeApplied: bool, dateApplied: str, date: str, karmaCost: int, Changes: "shr5Management_ManagedCharacter" = None, changes: "shr5Management_ManagedCharacter" = None, shr5Management_Changes: "shr5Management_CharacterChange" = None):
        self.changeApplied = changeApplied
        self.dateApplied = dateApplied
        self.date = date
        self.karmaCost = karmaCost
        self.Changes = Changes
        self.changes = changes
        self.shr5Management_Changes = shr5Management_Changes
        
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def changeApplied(self) -> bool:
        return self.__changeApplied

    @changeApplied.setter
    def changeApplied(self, changeApplied: bool):
        self.__changeApplied = changeApplied

    @property
    def dateApplied(self) -> str:
        return self.__dateApplied

    @dateApplied.setter
    def dateApplied(self, dateApplied: str):
        self.__dateApplied = dateApplied

    @property
    def karmaCost(self) -> int:
        return self.__karmaCost

    @karmaCost.setter
    def karmaCost(self, karmaCost: int):
        self.__karmaCost = karmaCost

    @property
    def Changes(self):
        return self.__Changes

    @Changes.setter
    def Changes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Changes__Changes", None)
        self.__Changes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "character"):
                opp_val = getattr(old_value, "character", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "character"):
                opp_val = getattr(value, "character", None)
                if opp_val is None:
                    setattr(value, "character", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_Changes(self):
        return self.__shr5Management_Changes

    @shr5Management_Changes.setter
    def shr5Management_Changes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Changes__shr5Management_Changes", None)
        self.__shr5Management_Changes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterChange"):
                opp_val = getattr(old_value, "shr5Management_CharacterChange", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_CharacterChange", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterChange"):
                opp_val = getattr(value, "shr5Management_CharacterChange", None)
                setattr(value, "shr5Management_CharacterChange", self)

    @property
    def changes(self):
        return self.__changes

    @changes.setter
    def changes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_Changes__changes", None)
        self.__changes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ManagedCharacter"):
                opp_val = getattr(old_value, "ManagedCharacter", None)
                if opp_val == self:
                    setattr(old_value, "ManagedCharacter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ManagedCharacter"):
                opp_val = getattr(value, "ManagedCharacter", None)
                setattr(value, "ManagedCharacter", self)

    def applyChanges(self):
        # TODO: Implement applyChanges method
        pass

class shr5Management_AbstraktPersona:

    pass
class shr5Management_ManagedCharacter(ABC):

    def __init__(self, sex: str, streetCred: int, notoriety: int, notorietyBasic: int, publicAwareness: int, karmaGaint: int, currentKarma: int, height: int, dateofbirth: str, weight: int, shr5Management_ManagedCharacter: "shr5Management_AbstraktPersona" = None, character: set["shr5Management_Changes"] = None, shr5Management_ManagedCharacter3: set["shr5Management_AbstraktGegenstand"] = None, shr5Management_ManagedCharacter5: set["shr5Management_Vertrag"] = None, shr5Management_ManagedCharacter7: set["shr5Management_Connection"] = None, shr5Management_ManagedCharacter9: set["shr5Management_Fahrzeug"] = None, shr5Management_ManagedCharacter11: "shr5Management_Lifestyle" = None, shr5Management_ManagedCharacter13: "shr5Management_Sprachfertigkeit" = None, ManagedCharacter: "shr5Management_Changes" = None, ManagedCharacter32: "shr5Management_CharacterGenerator" = None, shr5Management_ManagedCharacter59: "shr5Management_CharacterGroup" = None, shr5Management_ManagedCharacter62: "shr5Management_Connection" = None):
        self.sex = sex
        self.streetCred = streetCred
        self.notoriety = notoriety
        self.notorietyBasic = notorietyBasic
        self.publicAwareness = publicAwareness
        self.karmaGaint = karmaGaint
        self.currentKarma = currentKarma
        self.height = height
        self.dateofbirth = dateofbirth
        self.weight = weight
        self.shr5Management_ManagedCharacter = shr5Management_ManagedCharacter
        self.character = character if character is not None else set()
        self.shr5Management_ManagedCharacter3 = shr5Management_ManagedCharacter3 if shr5Management_ManagedCharacter3 is not None else set()
        self.shr5Management_ManagedCharacter5 = shr5Management_ManagedCharacter5 if shr5Management_ManagedCharacter5 is not None else set()
        self.shr5Management_ManagedCharacter7 = shr5Management_ManagedCharacter7 if shr5Management_ManagedCharacter7 is not None else set()
        self.shr5Management_ManagedCharacter9 = shr5Management_ManagedCharacter9 if shr5Management_ManagedCharacter9 is not None else set()
        self.shr5Management_ManagedCharacter11 = shr5Management_ManagedCharacter11
        self.shr5Management_ManagedCharacter13 = shr5Management_ManagedCharacter13
        self.ManagedCharacter = ManagedCharacter
        self.ManagedCharacter32 = ManagedCharacter32
        self.shr5Management_ManagedCharacter59 = shr5Management_ManagedCharacter59
        self.shr5Management_ManagedCharacter62 = shr5Management_ManagedCharacter62
        
    @property
    def publicAwareness(self) -> int:
        return self.__publicAwareness

    @publicAwareness.setter
    def publicAwareness(self, publicAwareness: int):
        self.__publicAwareness = publicAwareness

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def notoriety(self) -> int:
        return self.__notoriety

    @notoriety.setter
    def notoriety(self, notoriety: int):
        self.__notoriety = notoriety

    @property
    def sex(self) -> str:
        return self.__sex

    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def karmaGaint(self) -> int:
        return self.__karmaGaint

    @karmaGaint.setter
    def karmaGaint(self, karmaGaint: int):
        self.__karmaGaint = karmaGaint

    @property
    def streetCred(self) -> int:
        return self.__streetCred

    @streetCred.setter
    def streetCred(self, streetCred: int):
        self.__streetCred = streetCred

    @property
    def dateofbirth(self) -> str:
        return self.__dateofbirth

    @dateofbirth.setter
    def dateofbirth(self, dateofbirth: str):
        self.__dateofbirth = dateofbirth

    @property
    def notorietyBasic(self) -> int:
        return self.__notorietyBasic

    @notorietyBasic.setter
    def notorietyBasic(self, notorietyBasic: int):
        self.__notorietyBasic = notorietyBasic

    @property
    def currentKarma(self) -> int:
        return self.__currentKarma

    @currentKarma.setter
    def currentKarma(self, currentKarma: int):
        self.__currentKarma = currentKarma

    @property
    def shr5Management_ManagedCharacter7(self):
        return self.__shr5Management_ManagedCharacter7

    @shr5Management_ManagedCharacter7.setter
    def shr5Management_ManagedCharacter7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter7", None)
        self.__shr5Management_ManagedCharacter7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Connection"):
                    opp_val = getattr(item, "shr5Management_Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Connection"):
                    opp_val = getattr(item, "shr5Management_Connection", None)
                    
                    setattr(item, "shr5Management_Connection", self)
                    

    @property
    def ManagedCharacter(self):
        return self.__ManagedCharacter

    @ManagedCharacter.setter
    def ManagedCharacter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__ManagedCharacter", None)
        self.__ManagedCharacter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "changes"):
                opp_val = getattr(old_value, "changes", None)
                if opp_val == self:
                    setattr(old_value, "changes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "changes"):
                opp_val = getattr(value, "changes", None)
                setattr(value, "changes", self)

    @property
    def shr5Management_ManagedCharacter5(self):
        return self.__shr5Management_ManagedCharacter5

    @shr5Management_ManagedCharacter5.setter
    def shr5Management_ManagedCharacter5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter5", None)
        self.__shr5Management_ManagedCharacter5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Vertrag"):
                    opp_val = getattr(item, "shr5Management_Vertrag", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Vertrag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Vertrag"):
                    opp_val = getattr(item, "shr5Management_Vertrag", None)
                    
                    setattr(item, "shr5Management_Vertrag", self)
                    

    @property
    def character(self):
        return self.__character

    @character.setter
    def character(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__character", None)
        self.__character = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Changes"):
                    opp_val = getattr(item, "Changes", None)
                    
                    if opp_val == self:
                        setattr(item, "Changes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Changes"):
                    opp_val = getattr(item, "Changes", None)
                    
                    setattr(item, "Changes", self)
                    

    @property
    def shr5Management_ManagedCharacter62(self):
        return self.__shr5Management_ManagedCharacter62

    @shr5Management_ManagedCharacter62.setter
    def shr5Management_ManagedCharacter62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter62", None)
        self.__shr5Management_ManagedCharacter62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Connection61"):
                opp_val = getattr(old_value, "shr5Management_Connection61", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Connection61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Connection61"):
                opp_val = getattr(value, "shr5Management_Connection61", None)
                setattr(value, "shr5Management_Connection61", self)

    @property
    def ManagedCharacter32(self):
        return self.__ManagedCharacter32

    @ManagedCharacter32.setter
    def ManagedCharacter32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__ManagedCharacter32", None)
        self.__ManagedCharacter32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chracterSource"):
                opp_val = getattr(old_value, "chracterSource", None)
                if opp_val == self:
                    setattr(old_value, "chracterSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chracterSource"):
                opp_val = getattr(value, "chracterSource", None)
                setattr(value, "chracterSource", self)

    @property
    def shr5Management_ManagedCharacter9(self):
        return self.__shr5Management_ManagedCharacter9

    @shr5Management_ManagedCharacter9.setter
    def shr5Management_ManagedCharacter9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter9", None)
        self.__shr5Management_ManagedCharacter9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_Fahrzeug"):
                    opp_val = getattr(item, "shr5Management_Fahrzeug", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_Fahrzeug", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_Fahrzeug"):
                    opp_val = getattr(item, "shr5Management_Fahrzeug", None)
                    
                    setattr(item, "shr5Management_Fahrzeug", self)
                    

    @property
    def shr5Management_ManagedCharacter59(self):
        return self.__shr5Management_ManagedCharacter59

    @shr5Management_ManagedCharacter59.setter
    def shr5Management_ManagedCharacter59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter59", None)
        self.__shr5Management_ManagedCharacter59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_CharacterGroup58"):
                opp_val = getattr(old_value, "shr5Management_CharacterGroup58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_CharacterGroup58"):
                opp_val = getattr(value, "shr5Management_CharacterGroup58", None)
                if opp_val is None:
                    setattr(value, "shr5Management_CharacterGroup58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shr5Management_ManagedCharacter11(self):
        return self.__shr5Management_ManagedCharacter11

    @shr5Management_ManagedCharacter11.setter
    def shr5Management_ManagedCharacter11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter11", None)
        self.__shr5Management_ManagedCharacter11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Lifestyle"):
                opp_val = getattr(old_value, "shr5Management_Lifestyle", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Lifestyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Lifestyle"):
                opp_val = getattr(value, "shr5Management_Lifestyle", None)
                setattr(value, "shr5Management_Lifestyle", self)

    @property
    def shr5Management_ManagedCharacter(self):
        return self.__shr5Management_ManagedCharacter

    @shr5Management_ManagedCharacter.setter
    def shr5Management_ManagedCharacter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter", None)
        self.__shr5Management_ManagedCharacter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_AbstraktPersona"):
                opp_val = getattr(old_value, "shr5Management_AbstraktPersona", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_AbstraktPersona", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_AbstraktPersona"):
                opp_val = getattr(value, "shr5Management_AbstraktPersona", None)
                setattr(value, "shr5Management_AbstraktPersona", self)

    @property
    def shr5Management_ManagedCharacter13(self):
        return self.__shr5Management_ManagedCharacter13

    @shr5Management_ManagedCharacter13.setter
    def shr5Management_ManagedCharacter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter13", None)
        self.__shr5Management_ManagedCharacter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shr5Management_Sprachfertigkeit"):
                opp_val = getattr(old_value, "shr5Management_Sprachfertigkeit", None)
                if opp_val == self:
                    setattr(old_value, "shr5Management_Sprachfertigkeit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shr5Management_Sprachfertigkeit"):
                opp_val = getattr(value, "shr5Management_Sprachfertigkeit", None)
                setattr(value, "shr5Management_Sprachfertigkeit", self)

    @property
    def shr5Management_ManagedCharacter3(self):
        return self.__shr5Management_ManagedCharacter3

    @shr5Management_ManagedCharacter3.setter
    def shr5Management_ManagedCharacter3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shr5Management_ManagedCharacter__shr5Management_ManagedCharacter3", None)
        self.__shr5Management_ManagedCharacter3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shr5Management_AbstraktGegenstand"):
                    opp_val = getattr(item, "shr5Management_AbstraktGegenstand", None)
                    
                    if opp_val == self:
                        setattr(item, "shr5Management_AbstraktGegenstand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shr5Management_AbstraktGegenstand"):
                    opp_val = getattr(item, "shr5Management_AbstraktGegenstand", None)
                    
                    setattr(item, "shr5Management_AbstraktGegenstand", self)
                    
