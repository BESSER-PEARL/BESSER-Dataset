from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class raas_small_test_#30911270:

    pass
class raas_small_test_FourthLevelClassK:

    def __init__(self, multi2lowerAttrInt: int, singleAttrInt: int, optionalAttrInt: int, raasRef: str):
        self.multi2lowerAttrInt = multi2lowerAttrInt
        self.singleAttrInt = singleAttrInt
        self.optionalAttrInt = optionalAttrInt
        self.raasRef = raasRef
        
    @property
    def multi2lowerAttrInt(self) -> int:
        return self.__multi2lowerAttrInt

    @multi2lowerAttrInt.setter
    def multi2lowerAttrInt(self, multi2lowerAttrInt: int):
        self.__multi2lowerAttrInt = multi2lowerAttrInt

    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def optionalAttrInt(self) -> int:
        return self.__optionalAttrInt

    @optionalAttrInt.setter
    def optionalAttrInt(self, optionalAttrInt: int):
        self.__optionalAttrInt = optionalAttrInt

class raas_small_test_#10382437:

    pass
class raas_small_test_ThirdLevelClassJ:

    def __init__(self, raasRef: str, multi2lowerAttrInt: int, singleAttrInt: int, optionalAttrInt: int, raas_small_test_ThirdLevelClassJ: "raas_small_test_#10382437" = None):
        self.raasRef = raasRef
        self.multi2lowerAttrInt = multi2lowerAttrInt
        self.singleAttrInt = singleAttrInt
        self.optionalAttrInt = optionalAttrInt
        self.raas_small_test_ThirdLevelClassJ = raas_small_test_ThirdLevelClassJ
        
    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def multi2lowerAttrInt(self) -> int:
        return self.__multi2lowerAttrInt

    @multi2lowerAttrInt.setter
    def multi2lowerAttrInt(self, multi2lowerAttrInt: int):
        self.__multi2lowerAttrInt = multi2lowerAttrInt

    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def optionalAttrInt(self) -> int:
        return self.__optionalAttrInt

    @optionalAttrInt.setter
    def optionalAttrInt(self, optionalAttrInt: int):
        self.__optionalAttrInt = optionalAttrInt

    @property
    def raas_small_test_ThirdLevelClassJ(self):
        return self.__raas_small_test_ThirdLevelClassJ

    @raas_small_test_ThirdLevelClassJ.setter
    def raas_small_test_ThirdLevelClassJ(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ThirdLevelClassJ__raas_small_test_ThirdLevelClassJ", None)
        self.__raas_small_test_ThirdLevelClassJ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#10382437"):
                opp_val = getattr(old_value, "raas_small_test_#10382437", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#10382437", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#10382437"):
                opp_val = getattr(value, "raas_small_test_#10382437", None)
                setattr(value, "raas_small_test_#10382437", self)

class raas_small_test_UnderClassF:

    def __init__(self, raasRef: str, singleAttrInt: int):
        self.raasRef = raasRef
        self.singleAttrInt = singleAttrInt
        
    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

class raas_small_test_UnderClassE:

    def __init__(self, raasRef: str):
        self.raasRef = raasRef
        
    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

class raas_small_test_DerivedUnderClassE1(raas_small_test_UnderClassE):

    def __init__(self, raasRef: str, raas_small_test_DerivedUnderClassE1: "raas_small_test_#11832905" = None):
        super().__init__(raasRef)
        self.raas_small_test_DerivedUnderClassE1 = raas_small_test_DerivedUnderClassE1
        
    @property
    def raas_small_test_DerivedUnderClassE1(self):
        return self.__raas_small_test_DerivedUnderClassE1

    @raas_small_test_DerivedUnderClassE1.setter
    def raas_small_test_DerivedUnderClassE1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_DerivedUnderClassE1__raas_small_test_DerivedUnderClassE1", None)
        self.__raas_small_test_DerivedUnderClassE1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#1183290518"):
                opp_val = getattr(old_value, "raas_small_test_#1183290518", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#1183290518", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#1183290518"):
                opp_val = getattr(value, "raas_small_test_#1183290518", None)
                setattr(value, "raas_small_test_#1183290518", self)

class raas_small_test_DerivedUnderClassE2(raas_small_test_UnderClassE):

    def __init__(self, raasRef: str, raas_small_test_DerivedUnderClassE2: set["raas_small_test_#30911270"] = None):
        super().__init__(raasRef)
        self.raas_small_test_DerivedUnderClassE2 = raas_small_test_DerivedUnderClassE2 if raas_small_test_DerivedUnderClassE2 is not None else set()
        
    @property
    def raas_small_test_DerivedUnderClassE2(self):
        return self.__raas_small_test_DerivedUnderClassE2

    @raas_small_test_DerivedUnderClassE2.setter
    def raas_small_test_DerivedUnderClassE2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_DerivedUnderClassE2__raas_small_test_DerivedUnderClassE2", None)
        self.__raas_small_test_DerivedUnderClassE2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raas_small_test_#30911270"):
                    opp_val = getattr(item, "raas_small_test_#30911270", None)
                    
                    if opp_val == self:
                        setattr(item, "raas_small_test_#30911270", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raas_small_test_#30911270"):
                    opp_val = getattr(item, "raas_small_test_#30911270", None)
                    
                    setattr(item, "raas_small_test_#30911270", self)
                    

class raas_small_test_MergingE1AndE2(raas_small_test_DerivedUnderClassE2, raas_small_test_DerivedUnderClassE1):

    def __init__(self, raasRef: str, optionalAttrString: str, raas_small_test_DerivedUnderClassE1: "raas_small_test_#11832905", raas_small_test_DerivedUnderClassE2: set["raas_small_test_#30911270"] = None):
        super().__init__(raasRef, raas_small_test_DerivedUnderClassE1, raas_small_test_DerivedUnderClassE2)
        self.optionalAttrString = optionalAttrString
        
    @property
    def optionalAttrString(self) -> str:
        return self.__optionalAttrString

    @optionalAttrString.setter
    def optionalAttrString(self, optionalAttrString: str):
        self.__optionalAttrString = optionalAttrString

class raas_small_test_TopClassD:

    def __init__(self, singleAttrInt: int, optionalAttrInt: int, optionalTimeZone: str, raasRef: str, multi2lowerAttrInt: int):
        self.singleAttrInt = singleAttrInt
        self.optionalAttrInt = optionalAttrInt
        self.optionalTimeZone = optionalTimeZone
        self.raasRef = raasRef
        self.multi2lowerAttrInt = multi2lowerAttrInt
        
    @property
    def optionalTimeZone(self) -> str:
        return self.__optionalTimeZone

    @optionalTimeZone.setter
    def optionalTimeZone(self, optionalTimeZone: str):
        self.__optionalTimeZone = optionalTimeZone

    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def optionalAttrInt(self) -> int:
        return self.__optionalAttrInt

    @optionalAttrInt.setter
    def optionalAttrInt(self, optionalAttrInt: int):
        self.__optionalAttrInt = optionalAttrInt

    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def multi2lowerAttrInt(self) -> int:
        return self.__multi2lowerAttrInt

    @multi2lowerAttrInt.setter
    def multi2lowerAttrInt(self, multi2lowerAttrInt: int):
        self.__multi2lowerAttrInt = multi2lowerAttrInt

class raas_small_test_TopClassC:

    def __init__(self, raasRef: str, multi2lowerAttrInt: int, singleAttrInt: int, optionalAttrInt: int, raas_small_test_TopClassC: "raas_small_test_#16551649" = None):
        self.raasRef = raasRef
        self.multi2lowerAttrInt = multi2lowerAttrInt
        self.singleAttrInt = singleAttrInt
        self.optionalAttrInt = optionalAttrInt
        self.raas_small_test_TopClassC = raas_small_test_TopClassC
        
    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def multi2lowerAttrInt(self) -> int:
        return self.__multi2lowerAttrInt

    @multi2lowerAttrInt.setter
    def multi2lowerAttrInt(self, multi2lowerAttrInt: int):
        self.__multi2lowerAttrInt = multi2lowerAttrInt

    @property
    def optionalAttrInt(self) -> int:
        return self.__optionalAttrInt

    @optionalAttrInt.setter
    def optionalAttrInt(self, optionalAttrInt: int):
        self.__optionalAttrInt = optionalAttrInt

    @property
    def raas_small_test_TopClassC(self):
        return self.__raas_small_test_TopClassC

    @raas_small_test_TopClassC.setter
    def raas_small_test_TopClassC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_TopClassC__raas_small_test_TopClassC", None)
        self.__raas_small_test_TopClassC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#1655164915"):
                opp_val = getattr(old_value, "raas_small_test_#1655164915", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#1655164915", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#1655164915"):
                opp_val = getattr(value, "raas_small_test_#1655164915", None)
                setattr(value, "raas_small_test_#1655164915", self)

class raas_small_test_#16551649:

    pass
class raas_small_test_#5656663:

    pass
class raas_small_test_TopClassA:

    def __init__(self, raasRef: str, raas_small_test_TopClassA: set["raas_small_test_#5656663"] = None, raas_small_test_TopClassA11: "raas_small_test_#16551649" = None):
        self.raasRef = raasRef
        self.raas_small_test_TopClassA = raas_small_test_TopClassA if raas_small_test_TopClassA is not None else set()
        self.raas_small_test_TopClassA11 = raas_small_test_TopClassA11
        
    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def raas_small_test_TopClassA(self):
        return self.__raas_small_test_TopClassA

    @raas_small_test_TopClassA.setter
    def raas_small_test_TopClassA(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_TopClassA__raas_small_test_TopClassA", None)
        self.__raas_small_test_TopClassA = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raas_small_test_#5656663"):
                    opp_val = getattr(item, "raas_small_test_#5656663", None)
                    
                    if opp_val == self:
                        setattr(item, "raas_small_test_#5656663", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raas_small_test_#5656663"):
                    opp_val = getattr(item, "raas_small_test_#5656663", None)
                    
                    setattr(item, "raas_small_test_#5656663", self)
                    

    @property
    def raas_small_test_TopClassA11(self):
        return self.__raas_small_test_TopClassA11

    @raas_small_test_TopClassA11.setter
    def raas_small_test_TopClassA11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_TopClassA__raas_small_test_TopClassA11", None)
        self.__raas_small_test_TopClassA11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#16551649"):
                opp_val = getattr(old_value, "raas_small_test_#16551649", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#16551649", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#16551649"):
                opp_val = getattr(value, "raas_small_test_#16551649", None)
                setattr(value, "raas_small_test_#16551649", self)

class raas_small_test_TopClassM(raas_small_test_UnderClassE):

    def __init__(self, raasRef: str, singleAttrInt: int, raas_small_test_TopClassM: "raas_small_test_ReposRoot" = None):
        super().__init__(raasRef)
        self.singleAttrInt = singleAttrInt
        self.raas_small_test_TopClassM = raas_small_test_TopClassM
        
    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def raas_small_test_TopClassM(self):
        return self.__raas_small_test_TopClassM

    @raas_small_test_TopClassM.setter
    def raas_small_test_TopClassM(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_TopClassM__raas_small_test_TopClassM", None)
        self.__raas_small_test_TopClassM = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_ReposRoot8"):
                opp_val = getattr(old_value, "raas_small_test_ReposRoot8", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_ReposRoot8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_ReposRoot8"):
                opp_val = getattr(value, "raas_small_test_ReposRoot8", None)
                setattr(value, "raas_small_test_ReposRoot8", self)

class raas_small_test_#11832905:

    pass
class raas_small_test_#7345254:

    pass
class raas_small_test_TopClassB:

    def __init__(self, raasRef: str, multi2lowerAttrInt: int, singleAttrInt: int, optionalAttrInt: int, raas_small_test_TopClassB: set["raas_small_test_#5656663"] = None):
        self.raasRef = raasRef
        self.multi2lowerAttrInt = multi2lowerAttrInt
        self.singleAttrInt = singleAttrInt
        self.optionalAttrInt = optionalAttrInt
        self.raas_small_test_TopClassB = raas_small_test_TopClassB if raas_small_test_TopClassB is not None else set()
        
    @property
    def singleAttrInt(self) -> int:
        return self.__singleAttrInt

    @singleAttrInt.setter
    def singleAttrInt(self, singleAttrInt: int):
        self.__singleAttrInt = singleAttrInt

    @property
    def optionalAttrInt(self) -> int:
        return self.__optionalAttrInt

    @optionalAttrInt.setter
    def optionalAttrInt(self, optionalAttrInt: int):
        self.__optionalAttrInt = optionalAttrInt

    @property
    def multi2lowerAttrInt(self) -> int:
        return self.__multi2lowerAttrInt

    @multi2lowerAttrInt.setter
    def multi2lowerAttrInt(self, multi2lowerAttrInt: int):
        self.__multi2lowerAttrInt = multi2lowerAttrInt

    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def raas_small_test_TopClassB(self):
        return self.__raas_small_test_TopClassB

    @raas_small_test_TopClassB.setter
    def raas_small_test_TopClassB(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_TopClassB__raas_small_test_TopClassB", None)
        self.__raas_small_test_TopClassB = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raas_small_test_#565666313"):
                    opp_val = getattr(item, "raas_small_test_#565666313", None)
                    
                    if opp_val == self:
                        setattr(item, "raas_small_test_#565666313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raas_small_test_#565666313"):
                    opp_val = getattr(item, "raas_small_test_#565666313", None)
                    
                    setattr(item, "raas_small_test_#565666313", self)
                    

class raas_small_test_#29373817:

    pass
class raas_small_test_ReposRoot:

    def __init__(self, raasRef: str, singleAttrString: str, multiAttrString: str, raas_small_test_ReposRoot2: "raas_small_test_#19723516" = None, raas_small_test_ReposRoot: set["raas_small_test_#29373817"] = None, raas_small_test_ReposRoot4: "raas_small_test_#7345254" = None, raas_small_test_ReposRoot6: set["raas_small_test_#11832905"] = None, raas_small_test_ReposRoot8: "raas_small_test_TopClassM" = None):
        self.raasRef = raasRef
        self.singleAttrString = singleAttrString
        self.multiAttrString = multiAttrString
        self.raas_small_test_ReposRoot2 = raas_small_test_ReposRoot2
        self.raas_small_test_ReposRoot = raas_small_test_ReposRoot if raas_small_test_ReposRoot is not None else set()
        self.raas_small_test_ReposRoot4 = raas_small_test_ReposRoot4
        self.raas_small_test_ReposRoot6 = raas_small_test_ReposRoot6 if raas_small_test_ReposRoot6 is not None else set()
        self.raas_small_test_ReposRoot8 = raas_small_test_ReposRoot8
        
    @property
    def singleAttrString(self) -> str:
        return self.__singleAttrString

    @singleAttrString.setter
    def singleAttrString(self, singleAttrString: str):
        self.__singleAttrString = singleAttrString

    @property
    def raasRef(self) -> str:
        return self.__raasRef

    @raasRef.setter
    def raasRef(self, raasRef: str):
        self.__raasRef = raasRef

    @property
    def multiAttrString(self) -> str:
        return self.__multiAttrString

    @multiAttrString.setter
    def multiAttrString(self, multiAttrString: str):
        self.__multiAttrString = multiAttrString

    @property
    def raas_small_test_ReposRoot(self):
        return self.__raas_small_test_ReposRoot

    @raas_small_test_ReposRoot.setter
    def raas_small_test_ReposRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ReposRoot__raas_small_test_ReposRoot", None)
        self.__raas_small_test_ReposRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raas_small_test_#29373817"):
                    opp_val = getattr(item, "raas_small_test_#29373817", None)
                    
                    if opp_val == self:
                        setattr(item, "raas_small_test_#29373817", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raas_small_test_#29373817"):
                    opp_val = getattr(item, "raas_small_test_#29373817", None)
                    
                    setattr(item, "raas_small_test_#29373817", self)
                    

    @property
    def raas_small_test_ReposRoot2(self):
        return self.__raas_small_test_ReposRoot2

    @raas_small_test_ReposRoot2.setter
    def raas_small_test_ReposRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ReposRoot__raas_small_test_ReposRoot2", None)
        self.__raas_small_test_ReposRoot2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#19723516"):
                opp_val = getattr(old_value, "raas_small_test_#19723516", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#19723516", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#19723516"):
                opp_val = getattr(value, "raas_small_test_#19723516", None)
                setattr(value, "raas_small_test_#19723516", self)

    @property
    def raas_small_test_ReposRoot4(self):
        return self.__raas_small_test_ReposRoot4

    @raas_small_test_ReposRoot4.setter
    def raas_small_test_ReposRoot4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ReposRoot__raas_small_test_ReposRoot4", None)
        self.__raas_small_test_ReposRoot4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_#7345254"):
                opp_val = getattr(old_value, "raas_small_test_#7345254", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_#7345254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_#7345254"):
                opp_val = getattr(value, "raas_small_test_#7345254", None)
                setattr(value, "raas_small_test_#7345254", self)

    @property
    def raas_small_test_ReposRoot8(self):
        return self.__raas_small_test_ReposRoot8

    @raas_small_test_ReposRoot8.setter
    def raas_small_test_ReposRoot8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ReposRoot__raas_small_test_ReposRoot8", None)
        self.__raas_small_test_ReposRoot8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "raas_small_test_TopClassM"):
                opp_val = getattr(old_value, "raas_small_test_TopClassM", None)
                if opp_val == self:
                    setattr(old_value, "raas_small_test_TopClassM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "raas_small_test_TopClassM"):
                opp_val = getattr(value, "raas_small_test_TopClassM", None)
                setattr(value, "raas_small_test_TopClassM", self)

    @property
    def raas_small_test_ReposRoot6(self):
        return self.__raas_small_test_ReposRoot6

    @raas_small_test_ReposRoot6.setter
    def raas_small_test_ReposRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_raas_small_test_ReposRoot__raas_small_test_ReposRoot6", None)
        self.__raas_small_test_ReposRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "raas_small_test_#11832905"):
                    opp_val = getattr(item, "raas_small_test_#11832905", None)
                    
                    if opp_val == self:
                        setattr(item, "raas_small_test_#11832905", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "raas_small_test_#11832905"):
                    opp_val = getattr(item, "raas_small_test_#11832905", None)
                    
                    setattr(item, "raas_small_test_#11832905", self)
                    

class raas_small_test_#19723516:

    pass