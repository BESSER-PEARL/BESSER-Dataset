from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class dft_GalileoNodeType:

    pass
class GalileoNodeType:

    pass
class dft_Observer(GalileoNodeType):

    def __init__(self, observationRate: str, dft_Observer: set["dft_GalileoFaultTreeNode"] = None):
        self.observationRate = observationRate
        self.dft_Observer = dft_Observer if dft_Observer is not None else set()
        
    @property
    def observationRate(self) -> str:
        return self.__observationRate

    @observationRate.setter
    def observationRate(self, observationRate: str):
        self.__observationRate = observationRate

    @property
    def dft_Observer(self):
        return self.__dft_Observer

    @dft_Observer.setter
    def dft_Observer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_Observer__dft_Observer", None)
        self.__dft_Observer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dft_GalileoFaultTreeNode13"):
                    opp_val = getattr(item, "dft_GalileoFaultTreeNode13", None)
                    
                    if opp_val == self:
                        setattr(item, "dft_GalileoFaultTreeNode13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dft_GalileoFaultTreeNode13"):
                    opp_val = getattr(item, "dft_GalileoFaultTreeNode13", None)
                    
                    setattr(item, "dft_GalileoFaultTreeNode13", self)
                    

class dft_Parametrized(GalileoNodeType):

    def __init__(self, typeName: str, parameter: str):
        self.typeName = typeName
        self.parameter = parameter
        
    @property
    def parameter(self) -> str:
        return self.__parameter

    @parameter.setter
    def parameter(self, parameter: str):
        self.__parameter = parameter

    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class dft_Named(GalileoNodeType):

    def __init__(self, typeName: str):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class dft_GalileoDft:

    pass
class dft_GalileoFaultTreeNode:

    def __init__(self, name: str, lambda: str, dorm: str, repair: str, dft_GalileoFaultTreeNode: "dft_GalileoDft" = None, dft_GalileoFaultTreeNode3: "dft_GalileoDft" = None, dft_GalileoFaultTreeNode6: "dft_GalileoDft" = None, dft_GalileoFaultTreeNode13: "dft_Observer" = None, dft_GalileoFaultTreeNode8: "dft_GalileoNodeType" = None, dft_GalileoFaultTreeNode11: "dft_GalileoFaultTreeNode" = None, dft_GalileoFaultTreeNode9: set["dft_GalileoFaultTreeNode"] = None):
        self.name = name
        self.lambda = lambda
        self.dorm = dorm
        self.repair = repair
        self.dft_GalileoFaultTreeNode = dft_GalileoFaultTreeNode
        self.dft_GalileoFaultTreeNode3 = dft_GalileoFaultTreeNode3
        self.dft_GalileoFaultTreeNode6 = dft_GalileoFaultTreeNode6
        self.dft_GalileoFaultTreeNode13 = dft_GalileoFaultTreeNode13
        self.dft_GalileoFaultTreeNode8 = dft_GalileoFaultTreeNode8
        self.dft_GalileoFaultTreeNode11 = dft_GalileoFaultTreeNode11
        self.dft_GalileoFaultTreeNode9 = dft_GalileoFaultTreeNode9 if dft_GalileoFaultTreeNode9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lambda(self) -> str:
        return self.__lambda

    @lambda.setter
    def lambda(self, lambda: str):
        self.__lambda = lambda

    @property
    def repair(self) -> str:
        return self.__repair

    @repair.setter
    def repair(self, repair: str):
        self.__repair = repair

    @property
    def dorm(self) -> str:
        return self.__dorm

    @dorm.setter
    def dorm(self, dorm: str):
        self.__dorm = dorm

    @property
    def dft_GalileoFaultTreeNode8(self):
        return self.__dft_GalileoFaultTreeNode8

    @dft_GalileoFaultTreeNode8.setter
    def dft_GalileoFaultTreeNode8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode8", None)
        self.__dft_GalileoFaultTreeNode8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_GalileoNodeType"):
                opp_val = getattr(old_value, "dft_GalileoNodeType", None)
                if opp_val == self:
                    setattr(old_value, "dft_GalileoNodeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_GalileoNodeType"):
                opp_val = getattr(value, "dft_GalileoNodeType", None)
                setattr(value, "dft_GalileoNodeType", self)

    @property
    def dft_GalileoFaultTreeNode9(self):
        return self.__dft_GalileoFaultTreeNode9

    @dft_GalileoFaultTreeNode9.setter
    def dft_GalileoFaultTreeNode9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode9", None)
        self.__dft_GalileoFaultTreeNode9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dft_GalileoFaultTreeNode11"):
                    opp_val = getattr(item, "dft_GalileoFaultTreeNode11", None)
                    
                    if opp_val == self:
                        setattr(item, "dft_GalileoFaultTreeNode11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dft_GalileoFaultTreeNode11"):
                    opp_val = getattr(item, "dft_GalileoFaultTreeNode11", None)
                    
                    setattr(item, "dft_GalileoFaultTreeNode11", self)
                    

    @property
    def dft_GalileoFaultTreeNode(self):
        return self.__dft_GalileoFaultTreeNode

    @dft_GalileoFaultTreeNode.setter
    def dft_GalileoFaultTreeNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode", None)
        self.__dft_GalileoFaultTreeNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_GalileoDft"):
                opp_val = getattr(old_value, "dft_GalileoDft", None)
                if opp_val == self:
                    setattr(old_value, "dft_GalileoDft", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_GalileoDft"):
                opp_val = getattr(value, "dft_GalileoDft", None)
                setattr(value, "dft_GalileoDft", self)

    @property
    def dft_GalileoFaultTreeNode13(self):
        return self.__dft_GalileoFaultTreeNode13

    @dft_GalileoFaultTreeNode13.setter
    def dft_GalileoFaultTreeNode13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode13", None)
        self.__dft_GalileoFaultTreeNode13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_Observer"):
                opp_val = getattr(old_value, "dft_Observer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_Observer"):
                opp_val = getattr(value, "dft_Observer", None)
                if opp_val is None:
                    setattr(value, "dft_Observer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dft_GalileoFaultTreeNode11(self):
        return self.__dft_GalileoFaultTreeNode11

    @dft_GalileoFaultTreeNode11.setter
    def dft_GalileoFaultTreeNode11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode11", None)
        self.__dft_GalileoFaultTreeNode11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_GalileoFaultTreeNode9"):
                opp_val = getattr(old_value, "dft_GalileoFaultTreeNode9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_GalileoFaultTreeNode9"):
                opp_val = getattr(value, "dft_GalileoFaultTreeNode9", None)
                if opp_val is None:
                    setattr(value, "dft_GalileoFaultTreeNode9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dft_GalileoFaultTreeNode6(self):
        return self.__dft_GalileoFaultTreeNode6

    @dft_GalileoFaultTreeNode6.setter
    def dft_GalileoFaultTreeNode6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode6", None)
        self.__dft_GalileoFaultTreeNode6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_GalileoDft5"):
                opp_val = getattr(old_value, "dft_GalileoDft5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_GalileoDft5"):
                opp_val = getattr(value, "dft_GalileoDft5", None)
                if opp_val is None:
                    setattr(value, "dft_GalileoDft5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dft_GalileoFaultTreeNode3(self):
        return self.__dft_GalileoFaultTreeNode3

    @dft_GalileoFaultTreeNode3.setter
    def dft_GalileoFaultTreeNode3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dft_GalileoFaultTreeNode__dft_GalileoFaultTreeNode3", None)
        self.__dft_GalileoFaultTreeNode3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dft_GalileoDft2"):
                opp_val = getattr(old_value, "dft_GalileoDft2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dft_GalileoDft2"):
                opp_val = getattr(value, "dft_GalileoDft2", None)
                if opp_val is None:
                    setattr(value, "dft_GalileoDft2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
