from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class UpdateWeight:

    def __init__(self, Weights: float, BiasesWeigths: float, backpropagation3: "Backpropagation" = None):
        self.Weights = Weights
        self.BiasesWeigths = BiasesWeigths
        self.backpropagation3 = backpropagation3
        
        pass
    @property
    def BiasesWeigths(self):
        return self.__BiasesWeigths
    @BiasesWeigths.setter
    def BiasesWeigths(self, BiasesWeigths: float):
        self.__BiasesWeigths = BiasesWeigths

    @property
    def Weights(self):
        return self.__Weights
    @Weights.setter
    def Weights(self, Weights: float):
        self.__Weights = Weights

    @property
    def backpropagation3(self):
        return self.__backpropagation3
    @backpropagation3.setter
    def backpropagation3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UpdateWeight__backpropagation3", None)
        self.__backpropagation3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "updateWeigths2"):
                opp_val = getattr(old_value, "updateWeigths2", None)
                if opp_val == self:
                    setattr(old_value, "updateWeigths2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "updateWeigths2"):
                opp_val = getattr(value, "updateWeigths2", None)
                setattr(value, "updateWeigths2", self)



class NeuralNetwork:

    pass


class Backpropagation:

    def __init__(self, output: float, target: float, Weigths: float, BiasesWeigths: float, updateWeigths2: "UpdateWeight" = None, forward4: "Forward" = None):
        self.output = output
        self.target = target
        self.Weigths = Weigths
        self.BiasesWeigths = BiasesWeigths
        self.updateWeigths2 = updateWeigths2
        self.forward4 = forward4
        
        pass
    @property
    def Weigths(self):
        return self.__Weigths
    @Weigths.setter
    def Weigths(self, Weigths: float):
        self.__Weigths = Weigths

    @property
    def BiasesWeigths(self):
        return self.__BiasesWeigths
    @BiasesWeigths.setter
    def BiasesWeigths(self, BiasesWeigths: float):
        self.__BiasesWeigths = BiasesWeigths

    @property
    def target(self):
        return self.__target
    @target.setter
    def target(self, target: float):
        self.__target = target

    @property
    def output(self):
        return self.__output
    @output.setter
    def output(self, output: float):
        self.__output = output

    @property
    def updateWeigths2(self):
        return self.__updateWeigths2
    @updateWeigths2.setter
    def updateWeigths2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Backpropagation__updateWeigths2", None)
        self.__updateWeigths2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backpropagation3"):
                opp_val = getattr(old_value, "backpropagation3", None)
                if opp_val == self:
                    setattr(old_value, "backpropagation3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backpropagation3"):
                opp_val = getattr(value, "backpropagation3", None)
                setattr(value, "backpropagation3", self)

    @property
    def forward4(self):
        return self.__forward4
    @forward4.setter
    def forward4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Backpropagation__forward4", None)
        self.__forward4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backpropagation5"):
                opp_val = getattr(old_value, "backpropagation5", None)
                if opp_val == self:
                    setattr(old_value, "backpropagation5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backpropagation5"):
                opp_val = getattr(value, "backpropagation5", None)
                setattr(value, "backpropagation5", self)



class Forward:

    def __init__(self, Input: float, Weights: float, BiasesWeigths: float, neuralNetwork1: "NeuralNetwork" = None, backpropagation5: "Backpropagation" = None):
        self.Input = Input
        self.Weights = Weights
        self.BiasesWeigths = BiasesWeigths
        self.neuralNetwork1 = neuralNetwork1
        self.backpropagation5 = backpropagation5
        
        pass
    @property
    def BiasesWeigths(self):
        return self.__BiasesWeigths
    @BiasesWeigths.setter
    def BiasesWeigths(self, BiasesWeigths: float):
        self.__BiasesWeigths = BiasesWeigths

    @property
    def Input(self):
        return self.__Input
    @Input.setter
    def Input(self, Input: float):
        self.__Input = Input

    @property
    def Weights(self):
        return self.__Weights
    @Weights.setter
    def Weights(self, Weights: float):
        self.__Weights = Weights

    @property
    def neuralNetwork1(self):
        return self.__neuralNetwork1
    @neuralNetwork1.setter
    def neuralNetwork1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Forward__neuralNetwork1", None)
        self.__neuralNetwork1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forward0"):
                opp_val = getattr(old_value, "forward0", None)
                if opp_val == self:
                    setattr(old_value, "forward0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forward0"):
                opp_val = getattr(value, "forward0", None)
                setattr(value, "forward0", self)

    @property
    def backpropagation5(self):
        return self.__backpropagation5
    @backpropagation5.setter
    def backpropagation5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Forward__backpropagation5", None)
        self.__backpropagation5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forward4"):
                opp_val = getattr(old_value, "forward4", None)
                if opp_val == self:
                    setattr(old_value, "forward4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forward4"):
                opp_val = getattr(value, "forward4", None)
                setattr(value, "forward4", self)

