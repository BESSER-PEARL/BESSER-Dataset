from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class automaticexperiment_EStructuralFeature:

    pass
class automaticexperiment_ModifiableParameter:

    def __init__(self, initialValue: float, step: float, featureName: str, lowerBound: float, upperBound: float, targetURI: str, automaticexperiment_ModifiableParameter: "automaticexperiment_AutomaticExperiment" = None, automaticexperiment_ModifiableParameter4: "automaticexperiment_EStructuralFeature" = None):
        self.initialValue = initialValue
        self.step = step
        self.featureName = featureName
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.targetURI = targetURI
        self.automaticexperiment_ModifiableParameter = automaticexperiment_ModifiableParameter
        self.automaticexperiment_ModifiableParameter4 = automaticexperiment_ModifiableParameter4
        
    @property
    def targetURI(self) -> str:
        return self.__targetURI

    @targetURI.setter
    def targetURI(self, targetURI: str):
        self.__targetURI = targetURI

    @property
    def step(self) -> float:
        return self.__step

    @step.setter
    def step(self, step: float):
        self.__step = step

    @property
    def lowerBound(self) -> float:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: float):
        self.__lowerBound = lowerBound

    @property
    def featureName(self) -> str:
        return self.__featureName

    @featureName.setter
    def featureName(self, featureName: str):
        self.__featureName = featureName

    @property
    def upperBound(self) -> float:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: float):
        self.__upperBound = upperBound

    @property
    def initialValue(self) -> float:
        return self.__initialValue

    @initialValue.setter
    def initialValue(self, initialValue: float):
        self.__initialValue = initialValue

    @property
    def automaticexperiment_ModifiableParameter4(self):
        return self.__automaticexperiment_ModifiableParameter4

    @automaticexperiment_ModifiableParameter4.setter
    def automaticexperiment_ModifiableParameter4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaticexperiment_ModifiableParameter__automaticexperiment_ModifiableParameter4", None)
        self.__automaticexperiment_ModifiableParameter4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaticexperiment_EStructuralFeature"):
                opp_val = getattr(old_value, "automaticexperiment_EStructuralFeature", None)
                if opp_val == self:
                    setattr(old_value, "automaticexperiment_EStructuralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaticexperiment_EStructuralFeature"):
                opp_val = getattr(value, "automaticexperiment_EStructuralFeature", None)
                setattr(value, "automaticexperiment_EStructuralFeature", self)

    @property
    def automaticexperiment_ModifiableParameter(self):
        return self.__automaticexperiment_ModifiableParameter

    @automaticexperiment_ModifiableParameter.setter
    def automaticexperiment_ModifiableParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaticexperiment_ModifiableParameter__automaticexperiment_ModifiableParameter", None)
        self.__automaticexperiment_ModifiableParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaticexperiment_AutomaticExperiment2"):
                opp_val = getattr(old_value, "automaticexperiment_AutomaticExperiment2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaticexperiment_AutomaticExperiment2"):
                opp_val = getattr(value, "automaticexperiment_AutomaticExperiment2", None)
                if opp_val is None:
                    setattr(value, "automaticexperiment_AutomaticExperiment2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class automaticexperiment_Scenario:

    pass
class Identifiable:

    pass
class automaticexperiment_AutomaticExperiment(Identifiable):

    def __init__(self, errorAnalysisAlgorithm: str, errorFunction: str, tolerance: float, referanceDataDir: str, maximumNumberOfIterations: str, reInit: bool, automaticexperiment_AutomaticExperiment: "automaticexperiment_Scenario" = None, automaticexperiment_AutomaticExperiment2: set["automaticexperiment_ModifiableParameter"] = None):
        self.errorAnalysisAlgorithm = errorAnalysisAlgorithm
        self.errorFunction = errorFunction
        self.tolerance = tolerance
        self.referanceDataDir = referanceDataDir
        self.maximumNumberOfIterations = maximumNumberOfIterations
        self.reInit = reInit
        self.automaticexperiment_AutomaticExperiment = automaticexperiment_AutomaticExperiment
        self.automaticexperiment_AutomaticExperiment2 = automaticexperiment_AutomaticExperiment2 if automaticexperiment_AutomaticExperiment2 is not None else set()
        
    @property
    def referanceDataDir(self) -> str:
        return self.__referanceDataDir

    @referanceDataDir.setter
    def referanceDataDir(self, referanceDataDir: str):
        self.__referanceDataDir = referanceDataDir

    @property
    def reInit(self) -> bool:
        return self.__reInit

    @reInit.setter
    def reInit(self, reInit: bool):
        self.__reInit = reInit

    @property
    def maximumNumberOfIterations(self) -> str:
        return self.__maximumNumberOfIterations

    @maximumNumberOfIterations.setter
    def maximumNumberOfIterations(self, maximumNumberOfIterations: str):
        self.__maximumNumberOfIterations = maximumNumberOfIterations

    @property
    def errorAnalysisAlgorithm(self) -> str:
        return self.__errorAnalysisAlgorithm

    @errorAnalysisAlgorithm.setter
    def errorAnalysisAlgorithm(self, errorAnalysisAlgorithm: str):
        self.__errorAnalysisAlgorithm = errorAnalysisAlgorithm

    @property
    def errorFunction(self) -> str:
        return self.__errorFunction

    @errorFunction.setter
    def errorFunction(self, errorFunction: str):
        self.__errorFunction = errorFunction

    @property
    def tolerance(self) -> float:
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance: float):
        self.__tolerance = tolerance

    @property
    def automaticexperiment_AutomaticExperiment2(self):
        return self.__automaticexperiment_AutomaticExperiment2

    @automaticexperiment_AutomaticExperiment2.setter
    def automaticexperiment_AutomaticExperiment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaticexperiment_AutomaticExperiment__automaticexperiment_AutomaticExperiment2", None)
        self.__automaticexperiment_AutomaticExperiment2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "automaticexperiment_ModifiableParameter"):
                    opp_val = getattr(item, "automaticexperiment_ModifiableParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "automaticexperiment_ModifiableParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "automaticexperiment_ModifiableParameter"):
                    opp_val = getattr(item, "automaticexperiment_ModifiableParameter", None)
                    
                    setattr(item, "automaticexperiment_ModifiableParameter", self)
                    

    @property
    def automaticexperiment_AutomaticExperiment(self):
        return self.__automaticexperiment_AutomaticExperiment

    @automaticexperiment_AutomaticExperiment.setter
    def automaticexperiment_AutomaticExperiment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_automaticexperiment_AutomaticExperiment__automaticexperiment_AutomaticExperiment", None)
        self.__automaticexperiment_AutomaticExperiment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "automaticexperiment_Scenario"):
                opp_val = getattr(old_value, "automaticexperiment_Scenario", None)
                if opp_val == self:
                    setattr(old_value, "automaticexperiment_Scenario", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "automaticexperiment_Scenario"):
                opp_val = getattr(value, "automaticexperiment_Scenario", None)
                setattr(value, "automaticexperiment_Scenario", self)
