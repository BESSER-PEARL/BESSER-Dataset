from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class MultiPopulationSIRDiseaseModel:

    pass
class multipopulation_MultiPopulationSEIRDiseaseModel(MultiPopulationSIRDiseaseModel):

    pass
class MultiPopulationSIDiseaseModel:

    pass
class multipopulation_MultiPopulationSIRDiseaseModel(MultiPopulationSIDiseaseModel):

    pass
class StandardDiseaseModel:

    pass
class multipopulation_MultiPopulationSIDiseaseModel(StandardDiseaseModel):

    def __init__(self, physicallyAdjacentInfectiousProportion: float, roadNetworkInfectiousProportion: float, characteristicMixingDistance: float, multipopulation_MultiPopulationSIDiseaseModel: "multipopulation_StringValueList" = None, multipopulation_MultiPopulationSIDiseaseModel2: "multipopulation_DoubleValueMatrix" = None, multipopulation_MultiPopulationSIDiseaseModel4: "multipopulation_DoubleValueList" = None, multipopulation_MultiPopulationSIDiseaseModel6: "multipopulation_DoubleValueList" = None):
        self.physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion
        self.roadNetworkInfectiousProportion = roadNetworkInfectiousProportion
        self.characteristicMixingDistance = characteristicMixingDistance
        self.multipopulation_MultiPopulationSIDiseaseModel = multipopulation_MultiPopulationSIDiseaseModel
        self.multipopulation_MultiPopulationSIDiseaseModel2 = multipopulation_MultiPopulationSIDiseaseModel2
        self.multipopulation_MultiPopulationSIDiseaseModel4 = multipopulation_MultiPopulationSIDiseaseModel4
        self.multipopulation_MultiPopulationSIDiseaseModel6 = multipopulation_MultiPopulationSIDiseaseModel6
        
    @property
    def physicallyAdjacentInfectiousProportion(self) -> float:
        return self.__physicallyAdjacentInfectiousProportion

    @physicallyAdjacentInfectiousProportion.setter
    def physicallyAdjacentInfectiousProportion(self, physicallyAdjacentInfectiousProportion: float):
        self.__physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion

    @property
    def characteristicMixingDistance(self) -> float:
        return self.__characteristicMixingDistance

    @characteristicMixingDistance.setter
    def characteristicMixingDistance(self, characteristicMixingDistance: float):
        self.__characteristicMixingDistance = characteristicMixingDistance

    @property
    def roadNetworkInfectiousProportion(self) -> float:
        return self.__roadNetworkInfectiousProportion

    @roadNetworkInfectiousProportion.setter
    def roadNetworkInfectiousProportion(self, roadNetworkInfectiousProportion: float):
        self.__roadNetworkInfectiousProportion = roadNetworkInfectiousProportion

    @property
    def multipopulation_MultiPopulationSIDiseaseModel2(self):
        return self.__multipopulation_MultiPopulationSIDiseaseModel2

    @multipopulation_MultiPopulationSIDiseaseModel2.setter
    def multipopulation_MultiPopulationSIDiseaseModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multipopulation_MultiPopulationSIDiseaseModel__multipopulation_MultiPopulationSIDiseaseModel2", None)
        self.__multipopulation_MultiPopulationSIDiseaseModel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multipopulation_DoubleValueMatrix"):
                opp_val = getattr(old_value, "multipopulation_DoubleValueMatrix", None)
                if opp_val == self:
                    setattr(old_value, "multipopulation_DoubleValueMatrix", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multipopulation_DoubleValueMatrix"):
                opp_val = getattr(value, "multipopulation_DoubleValueMatrix", None)
                setattr(value, "multipopulation_DoubleValueMatrix", self)

    @property
    def multipopulation_MultiPopulationSIDiseaseModel6(self):
        return self.__multipopulation_MultiPopulationSIDiseaseModel6

    @multipopulation_MultiPopulationSIDiseaseModel6.setter
    def multipopulation_MultiPopulationSIDiseaseModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multipopulation_MultiPopulationSIDiseaseModel__multipopulation_MultiPopulationSIDiseaseModel6", None)
        self.__multipopulation_MultiPopulationSIDiseaseModel6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multipopulation_DoubleValueList7"):
                opp_val = getattr(old_value, "multipopulation_DoubleValueList7", None)
                if opp_val == self:
                    setattr(old_value, "multipopulation_DoubleValueList7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multipopulation_DoubleValueList7"):
                opp_val = getattr(value, "multipopulation_DoubleValueList7", None)
                setattr(value, "multipopulation_DoubleValueList7", self)

    @property
    def multipopulation_MultiPopulationSIDiseaseModel4(self):
        return self.__multipopulation_MultiPopulationSIDiseaseModel4

    @multipopulation_MultiPopulationSIDiseaseModel4.setter
    def multipopulation_MultiPopulationSIDiseaseModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multipopulation_MultiPopulationSIDiseaseModel__multipopulation_MultiPopulationSIDiseaseModel4", None)
        self.__multipopulation_MultiPopulationSIDiseaseModel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multipopulation_DoubleValueList"):
                opp_val = getattr(old_value, "multipopulation_DoubleValueList", None)
                if opp_val == self:
                    setattr(old_value, "multipopulation_DoubleValueList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multipopulation_DoubleValueList"):
                opp_val = getattr(value, "multipopulation_DoubleValueList", None)
                setattr(value, "multipopulation_DoubleValueList", self)

    @property
    def multipopulation_MultiPopulationSIDiseaseModel(self):
        return self.__multipopulation_MultiPopulationSIDiseaseModel

    @multipopulation_MultiPopulationSIDiseaseModel.setter
    def multipopulation_MultiPopulationSIDiseaseModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_multipopulation_MultiPopulationSIDiseaseModel__multipopulation_MultiPopulationSIDiseaseModel", None)
        self.__multipopulation_MultiPopulationSIDiseaseModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "multipopulation_StringValueList"):
                opp_val = getattr(old_value, "multipopulation_StringValueList", None)
                if opp_val == self:
                    setattr(old_value, "multipopulation_StringValueList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "multipopulation_StringValueList"):
                opp_val = getattr(value, "multipopulation_StringValueList", None)
                setattr(value, "multipopulation_StringValueList", self)

class multipopulation_DoubleValueList:

    pass
class multipopulation_DoubleValueMatrix:

    pass
class multipopulation_StringValueList:

    pass