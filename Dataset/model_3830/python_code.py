from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class UnserializableEnumTest(Enum):
    name1 = "name1"
    name2 = "name2"
class SerializableEnumTest(Enum):
    name3 = "name3"
    name4 = "name4"


############################################
# Definition of Classes
############################################

class exhaustive_GenericTest:

    def __init__(self, genericAttr: str):
        self.genericAttr = genericAttr
        
    @property
    def genericAttr(self) -> str:
        return self.__genericAttr

    @genericAttr.setter
    def genericAttr(self, genericAttr: str):
        self.__genericAttr = genericAttr

    def genericOperationThrow(self):
        # TODO: Implement genericOperationThrow method
        pass

    def genericOperationParameters(self, foo: str, bar: str):
        # TODO: Implement genericOperationParameters method
        pass

    def genericOperationReturn(self):
        # TODO: Implement genericOperationReturn method
        pass

class exhaustive_OperationsTest:

    def __init__(self):
        
    def orderedNo(self):
        # TODO: Implement orderedNo method
        pass

    def lowerBound2(self) -> InterfaceTest:
        # TODO: Implement lowerBound2 method
        pass

    def upperBound2(self) -> str:
        # TODO: Implement upperBound2 method
        pass

    def empty(self):
        # TODO: Implement empty method
        pass

    def uniqueNo(self):
        # TODO: Implement uniqueNo method
        pass

    def lowerBound1(self) -> str:
        # TODO: Implement lowerBound1 method
        pass

    def upperBoundN(self) -> str:
        # TODO: Implement upperBoundN method
        pass

    def manyParameters(self, p2: int, p1: AbstractTest):
        # TODO: Implement manyParameters method
        pass

class MultipleSuperTest:

    pass
class AbstractTest:

    pass
class OperationsTest:

    pass
class exhaustive_InterfaceTest(OperationsTest):

    pass
class exhaustive_AbstractTest(OperationsTest):

    pass
class exhaustive_ReferencesTest(AbstractTest):

    pass
class InterfaceTest:

    pass
class exhaustive_AttributesTest(MultipleSuperTest, InterfaceTest):

    def __init__(self, changeableYes: float, changeableNo: str, defaultValue: str, derivedYes: str, derivedNo: str, idYes: str, idNo: str, lowerBound0: int, lowerBound1: str, lowerBound2: str, lowerBoundN: str, upperBound0: str, upperBound1: date, upperBound2: str, upperBoundN: str, orderedYes: str, volatileYes: str, volatileNo: str, orderenedNo: str, transientYes: float, transientNo: str, uniqueYes: str, uniqueNo: str, unsettableYes: str, unsettableNo: str, AttributesTest: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest17: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest20: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest23: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest26: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest29: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest32: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest35: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest11: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest14: "exhaustive_ReferencesTest" = None, exhaustive_AttributesTest38: "exhaustive_ReferencesTest" = None, opposite1: "exhaustive_ReferencesTest" = None):
        self.changeableYes = changeableYes
        self.changeableNo = changeableNo
        self.defaultValue = defaultValue
        self.derivedYes = derivedYes
        self.derivedNo = derivedNo
        self.idYes = idYes
        self.idNo = idNo
        self.lowerBound0 = lowerBound0
        self.lowerBound1 = lowerBound1
        self.lowerBound2 = lowerBound2
        self.lowerBoundN = lowerBoundN
        self.upperBound0 = upperBound0
        self.upperBound1 = upperBound1
        self.upperBound2 = upperBound2
        self.upperBoundN = upperBoundN
        self.orderedYes = orderedYes
        self.volatileYes = volatileYes
        self.volatileNo = volatileNo
        self.orderenedNo = orderenedNo
        self.transientYes = transientYes
        self.transientNo = transientNo
        self.uniqueYes = uniqueYes
        self.uniqueNo = uniqueNo
        self.unsettableYes = unsettableYes
        self.unsettableNo = unsettableNo
        self.AttributesTest = AttributesTest
        self.exhaustive_AttributesTest17 = exhaustive_AttributesTest17
        self.exhaustive_AttributesTest20 = exhaustive_AttributesTest20
        self.exhaustive_AttributesTest23 = exhaustive_AttributesTest23
        self.exhaustive_AttributesTest26 = exhaustive_AttributesTest26
        self.exhaustive_AttributesTest29 = exhaustive_AttributesTest29
        self.exhaustive_AttributesTest32 = exhaustive_AttributesTest32
        self.exhaustive_AttributesTest35 = exhaustive_AttributesTest35
        self.exhaustive_AttributesTest = exhaustive_AttributesTest
        self.exhaustive_AttributesTest11 = exhaustive_AttributesTest11
        self.exhaustive_AttributesTest14 = exhaustive_AttributesTest14
        self.exhaustive_AttributesTest38 = exhaustive_AttributesTest38
        self.opposite1 = opposite1
        
    @property
    def changeableYes(self) -> float:
        return self.__changeableYes

    @changeableYes.setter
    def changeableYes(self, changeableYes: float):
        self.__changeableYes = changeableYes

    @property
    def volatileYes(self) -> str:
        return self.__volatileYes

    @volatileYes.setter
    def volatileYes(self, volatileYes: str):
        self.__volatileYes = volatileYes

    @property
    def idYes(self) -> str:
        return self.__idYes

    @idYes.setter
    def idYes(self, idYes: str):
        self.__idYes = idYes

    @property
    def lowerBound1(self) -> str:
        return self.__lowerBound1

    @lowerBound1.setter
    def lowerBound1(self, lowerBound1: str):
        self.__lowerBound1 = lowerBound1

    @property
    def derivedNo(self) -> str:
        return self.__derivedNo

    @derivedNo.setter
    def derivedNo(self, derivedNo: str):
        self.__derivedNo = derivedNo

    @property
    def upperBound0(self) -> str:
        return self.__upperBound0

    @upperBound0.setter
    def upperBound0(self, upperBound0: str):
        self.__upperBound0 = upperBound0

    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def transientNo(self) -> str:
        return self.__transientNo

    @transientNo.setter
    def transientNo(self, transientNo: str):
        self.__transientNo = transientNo

    @property
    def upperBoundN(self) -> str:
        return self.__upperBoundN

    @upperBoundN.setter
    def upperBoundN(self, upperBoundN: str):
        self.__upperBoundN = upperBoundN

    @property
    def unsettableYes(self) -> str:
        return self.__unsettableYes

    @unsettableYes.setter
    def unsettableYes(self, unsettableYes: str):
        self.__unsettableYes = unsettableYes

    @property
    def orderenedNo(self) -> str:
        return self.__orderenedNo

    @orderenedNo.setter
    def orderenedNo(self, orderenedNo: str):
        self.__orderenedNo = orderenedNo

    @property
    def volatileNo(self) -> str:
        return self.__volatileNo

    @volatileNo.setter
    def volatileNo(self, volatileNo: str):
        self.__volatileNo = volatileNo

    @property
    def lowerBoundN(self) -> str:
        return self.__lowerBoundN

    @lowerBoundN.setter
    def lowerBoundN(self, lowerBoundN: str):
        self.__lowerBoundN = lowerBoundN

    @property
    def idNo(self) -> str:
        return self.__idNo

    @idNo.setter
    def idNo(self, idNo: str):
        self.__idNo = idNo

    @property
    def uniqueYes(self) -> str:
        return self.__uniqueYes

    @uniqueYes.setter
    def uniqueYes(self, uniqueYes: str):
        self.__uniqueYes = uniqueYes

    @property
    def lowerBound0(self) -> int:
        return self.__lowerBound0

    @lowerBound0.setter
    def lowerBound0(self, lowerBound0: int):
        self.__lowerBound0 = lowerBound0

    @property
    def changeableNo(self) -> str:
        return self.__changeableNo

    @changeableNo.setter
    def changeableNo(self, changeableNo: str):
        self.__changeableNo = changeableNo

    @property
    def upperBound2(self) -> str:
        return self.__upperBound2

    @upperBound2.setter
    def upperBound2(self, upperBound2: str):
        self.__upperBound2 = upperBound2

    @property
    def uniqueNo(self) -> str:
        return self.__uniqueNo

    @uniqueNo.setter
    def uniqueNo(self, uniqueNo: str):
        self.__uniqueNo = uniqueNo

    @property
    def derivedYes(self) -> str:
        return self.__derivedYes

    @derivedYes.setter
    def derivedYes(self, derivedYes: str):
        self.__derivedYes = derivedYes

    @property
    def transientYes(self) -> float:
        return self.__transientYes

    @transientYes.setter
    def transientYes(self, transientYes: float):
        self.__transientYes = transientYes

    @property
    def unsettableNo(self) -> str:
        return self.__unsettableNo

    @unsettableNo.setter
    def unsettableNo(self, unsettableNo: str):
        self.__unsettableNo = unsettableNo

    @property
    def upperBound1(self) -> date:
        return self.__upperBound1

    @upperBound1.setter
    def upperBound1(self, upperBound1: date):
        self.__upperBound1 = upperBound1

    @property
    def orderedYes(self) -> str:
        return self.__orderedYes

    @orderedYes.setter
    def orderedYes(self, orderedYes: str):
        self.__orderedYes = orderedYes

    @property
    def lowerBound2(self) -> str:
        return self.__lowerBound2

    @lowerBound2.setter
    def lowerBound2(self, lowerBound2: str):
        self.__lowerBound2 = lowerBound2

    @property
    def AttributesTest(self):
        return self.__AttributesTest

    @AttributesTest.setter
    def AttributesTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__AttributesTest", None)
        self.__AttributesTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opposite2"):
                opp_val = getattr(old_value, "opposite2", None)
                if opp_val == self:
                    setattr(old_value, "opposite2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opposite2"):
                opp_val = getattr(value, "opposite2", None)
                setattr(value, "opposite2", self)

    @property
    def exhaustive_AttributesTest38(self):
        return self.__exhaustive_AttributesTest38

    @exhaustive_AttributesTest38.setter
    def exhaustive_AttributesTest38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest38", None)
        self.__exhaustive_AttributesTest38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest37"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest37"):
                opp_val = getattr(value, "exhaustive_ReferencesTest37", None)
                if opp_val is None:
                    setattr(value, "exhaustive_ReferencesTest37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exhaustive_AttributesTest17(self):
        return self.__exhaustive_AttributesTest17

    @exhaustive_AttributesTest17.setter
    def exhaustive_AttributesTest17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest17", None)
        self.__exhaustive_AttributesTest17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest16"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest16", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest16"):
                opp_val = getattr(value, "exhaustive_ReferencesTest16", None)
                setattr(value, "exhaustive_ReferencesTest16", self)

    @property
    def exhaustive_AttributesTest23(self):
        return self.__exhaustive_AttributesTest23

    @exhaustive_AttributesTest23.setter
    def exhaustive_AttributesTest23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest23", None)
        self.__exhaustive_AttributesTest23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest22"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest22", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest22"):
                opp_val = getattr(value, "exhaustive_ReferencesTest22", None)
                setattr(value, "exhaustive_ReferencesTest22", self)

    @property
    def exhaustive_AttributesTest11(self):
        return self.__exhaustive_AttributesTest11

    @exhaustive_AttributesTest11.setter
    def exhaustive_AttributesTest11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest11", None)
        self.__exhaustive_AttributesTest11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest10"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest10", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest10"):
                opp_val = getattr(value, "exhaustive_ReferencesTest10", None)
                setattr(value, "exhaustive_ReferencesTest10", self)

    @property
    def exhaustive_AttributesTest(self):
        return self.__exhaustive_AttributesTest

    @exhaustive_AttributesTest.setter
    def exhaustive_AttributesTest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest", None)
        self.__exhaustive_AttributesTest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest8"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest8", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest8"):
                opp_val = getattr(value, "exhaustive_ReferencesTest8", None)
                setattr(value, "exhaustive_ReferencesTest8", self)

    @property
    def opposite1(self):
        return self.__opposite1

    @opposite1.setter
    def opposite1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__opposite1", None)
        self.__opposite1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ReferencesTest"):
                opp_val = getattr(old_value, "ReferencesTest", None)
                if opp_val == self:
                    setattr(old_value, "ReferencesTest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ReferencesTest"):
                opp_val = getattr(value, "ReferencesTest", None)
                setattr(value, "ReferencesTest", self)

    @property
    def exhaustive_AttributesTest35(self):
        return self.__exhaustive_AttributesTest35

    @exhaustive_AttributesTest35.setter
    def exhaustive_AttributesTest35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest35", None)
        self.__exhaustive_AttributesTest35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest34"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest34", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest34"):
                opp_val = getattr(value, "exhaustive_ReferencesTest34", None)
                setattr(value, "exhaustive_ReferencesTest34", self)

    @property
    def exhaustive_AttributesTest29(self):
        return self.__exhaustive_AttributesTest29

    @exhaustive_AttributesTest29.setter
    def exhaustive_AttributesTest29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest29", None)
        self.__exhaustive_AttributesTest29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest28"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest28"):
                opp_val = getattr(value, "exhaustive_ReferencesTest28", None)
                if opp_val is None:
                    setattr(value, "exhaustive_ReferencesTest28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exhaustive_AttributesTest14(self):
        return self.__exhaustive_AttributesTest14

    @exhaustive_AttributesTest14.setter
    def exhaustive_AttributesTest14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest14", None)
        self.__exhaustive_AttributesTest14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest13"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest13", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest13"):
                opp_val = getattr(value, "exhaustive_ReferencesTest13", None)
                setattr(value, "exhaustive_ReferencesTest13", self)

    @property
    def exhaustive_AttributesTest32(self):
        return self.__exhaustive_AttributesTest32

    @exhaustive_AttributesTest32.setter
    def exhaustive_AttributesTest32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest32", None)
        self.__exhaustive_AttributesTest32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest31"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest31"):
                opp_val = getattr(value, "exhaustive_ReferencesTest31", None)
                if opp_val is None:
                    setattr(value, "exhaustive_ReferencesTest31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exhaustive_AttributesTest26(self):
        return self.__exhaustive_AttributesTest26

    @exhaustive_AttributesTest26.setter
    def exhaustive_AttributesTest26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest26", None)
        self.__exhaustive_AttributesTest26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest25"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest25", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest25"):
                opp_val = getattr(value, "exhaustive_ReferencesTest25", None)
                setattr(value, "exhaustive_ReferencesTest25", self)

    @property
    def exhaustive_AttributesTest20(self):
        return self.__exhaustive_AttributesTest20

    @exhaustive_AttributesTest20.setter
    def exhaustive_AttributesTest20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exhaustive_AttributesTest__exhaustive_AttributesTest20", None)
        self.__exhaustive_AttributesTest20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exhaustive_ReferencesTest19"):
                opp_val = getattr(old_value, "exhaustive_ReferencesTest19", None)
                if opp_val == self:
                    setattr(old_value, "exhaustive_ReferencesTest19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exhaustive_ReferencesTest19"):
                opp_val = getattr(value, "exhaustive_ReferencesTest19", None)
                setattr(value, "exhaustive_ReferencesTest19", self)

class exhaustive_MultipleSuperTest(AbstractTest, InterfaceTest):

    pass