from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scrShYQYaSD_ak:

    def __init__(self, CXmvqzTe: str, zBIcb: str, MHQpVCYtERyk: str, scrShYQYaSD_ak: "scrShYQYaSD_xvHXdRr" = None, scrShYQYaSD_ak5: "scrShYQYaSD_xvHXdRr" = None, scrShYQYaSD_ak8: "scrShYQYaSD_xvHXdRr" = None, scrShYQYaSD_ak14: "scrShYQYaSD_ak" = None, scrShYQYaSD_ak12: set["scrShYQYaSD_ak"] = None, scrShYQYaSD_ak16: "scrShYQYaSD_xvHXdRr" = None, scrShYQYaSD_ak19: "scrShYQYaSD_xvHXdRr" = None, scrShYQYaSD_ak11: "scrShYQYaSD_xvHXdRr" = None):
        self.CXmvqzTe = CXmvqzTe
        self.zBIcb = zBIcb
        self.MHQpVCYtERyk = MHQpVCYtERyk
        self.scrShYQYaSD_ak = scrShYQYaSD_ak
        self.scrShYQYaSD_ak5 = scrShYQYaSD_ak5
        self.scrShYQYaSD_ak8 = scrShYQYaSD_ak8
        self.scrShYQYaSD_ak14 = scrShYQYaSD_ak14
        self.scrShYQYaSD_ak12 = scrShYQYaSD_ak12 if scrShYQYaSD_ak12 is not None else set()
        self.scrShYQYaSD_ak16 = scrShYQYaSD_ak16
        self.scrShYQYaSD_ak19 = scrShYQYaSD_ak19
        self.scrShYQYaSD_ak11 = scrShYQYaSD_ak11
        
    @property
    def MHQpVCYtERyk(self) -> str:
        return self.__MHQpVCYtERyk

    @MHQpVCYtERyk.setter
    def MHQpVCYtERyk(self, MHQpVCYtERyk: str):
        self.__MHQpVCYtERyk = MHQpVCYtERyk

    @property
    def CXmvqzTe(self) -> str:
        return self.__CXmvqzTe

    @CXmvqzTe.setter
    def CXmvqzTe(self, CXmvqzTe: str):
        self.__CXmvqzTe = CXmvqzTe

    @property
    def zBIcb(self) -> str:
        return self.__zBIcb

    @zBIcb.setter
    def zBIcb(self, zBIcb: str):
        self.__zBIcb = zBIcb

    @property
    def scrShYQYaSD_ak12(self):
        return self.__scrShYQYaSD_ak12

    @scrShYQYaSD_ak12.setter
    def scrShYQYaSD_ak12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak12", None)
        self.__scrShYQYaSD_ak12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scrShYQYaSD_ak14"):
                    opp_val = getattr(item, "scrShYQYaSD_ak14", None)
                    
                    if opp_val == self:
                        setattr(item, "scrShYQYaSD_ak14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scrShYQYaSD_ak14"):
                    opp_val = getattr(item, "scrShYQYaSD_ak14", None)
                    
                    setattr(item, "scrShYQYaSD_ak14", self)
                    

    @property
    def scrShYQYaSD_ak5(self):
        return self.__scrShYQYaSD_ak5

    @scrShYQYaSD_ak5.setter
    def scrShYQYaSD_ak5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak5", None)
        self.__scrShYQYaSD_ak5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr4"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr4"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr4", None)
                if opp_val is None:
                    setattr(value, "scrShYQYaSD_xvHXdRr4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scrShYQYaSD_ak16(self):
        return self.__scrShYQYaSD_ak16

    @scrShYQYaSD_ak16.setter
    def scrShYQYaSD_ak16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak16", None)
        self.__scrShYQYaSD_ak16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr17"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr17", None)
                if opp_val == self:
                    setattr(old_value, "scrShYQYaSD_xvHXdRr17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr17"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr17", None)
                setattr(value, "scrShYQYaSD_xvHXdRr17", self)

    @property
    def scrShYQYaSD_ak19(self):
        return self.__scrShYQYaSD_ak19

    @scrShYQYaSD_ak19.setter
    def scrShYQYaSD_ak19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak19", None)
        self.__scrShYQYaSD_ak19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr20"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr20", None)
                if opp_val == self:
                    setattr(old_value, "scrShYQYaSD_xvHXdRr20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr20"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr20", None)
                setattr(value, "scrShYQYaSD_xvHXdRr20", self)

    @property
    def scrShYQYaSD_ak8(self):
        return self.__scrShYQYaSD_ak8

    @scrShYQYaSD_ak8.setter
    def scrShYQYaSD_ak8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak8", None)
        self.__scrShYQYaSD_ak8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr7"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr7", None)
                if opp_val == self:
                    setattr(old_value, "scrShYQYaSD_xvHXdRr7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr7"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr7", None)
                setattr(value, "scrShYQYaSD_xvHXdRr7", self)

    @property
    def scrShYQYaSD_ak11(self):
        return self.__scrShYQYaSD_ak11

    @scrShYQYaSD_ak11.setter
    def scrShYQYaSD_ak11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak11", None)
        self.__scrShYQYaSD_ak11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr10"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr10"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr10", None)
                if opp_val is None:
                    setattr(value, "scrShYQYaSD_xvHXdRr10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scrShYQYaSD_ak14(self):
        return self.__scrShYQYaSD_ak14

    @scrShYQYaSD_ak14.setter
    def scrShYQYaSD_ak14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak14", None)
        self.__scrShYQYaSD_ak14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_ak12"):
                opp_val = getattr(old_value, "scrShYQYaSD_ak12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_ak12"):
                opp_val = getattr(value, "scrShYQYaSD_ak12", None)
                if opp_val is None:
                    setattr(value, "scrShYQYaSD_ak12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scrShYQYaSD_ak(self):
        return self.__scrShYQYaSD_ak

    @scrShYQYaSD_ak.setter
    def scrShYQYaSD_ak(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_ak__scrShYQYaSD_ak", None)
        self.__scrShYQYaSD_ak = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr2"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr2"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr2", None)
                if opp_val is None:
                    setattr(value, "scrShYQYaSD_xvHXdRr2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scrShYQYaSD_HVOwDYkMdHvynG:

    def __init__(self, vdjNPHX: str, scrShYQYaSD_HVOwDYkMdHvynG: "scrShYQYaSD_xvHXdRr" = None):
        self.vdjNPHX = vdjNPHX
        self.scrShYQYaSD_HVOwDYkMdHvynG = scrShYQYaSD_HVOwDYkMdHvynG
        
    @property
    def vdjNPHX(self) -> str:
        return self.__vdjNPHX

    @vdjNPHX.setter
    def vdjNPHX(self, vdjNPHX: str):
        self.__vdjNPHX = vdjNPHX

    @property
    def scrShYQYaSD_HVOwDYkMdHvynG(self):
        return self.__scrShYQYaSD_HVOwDYkMdHvynG

    @scrShYQYaSD_HVOwDYkMdHvynG.setter
    def scrShYQYaSD_HVOwDYkMdHvynG(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scrShYQYaSD_HVOwDYkMdHvynG__scrShYQYaSD_HVOwDYkMdHvynG", None)
        self.__scrShYQYaSD_HVOwDYkMdHvynG = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scrShYQYaSD_xvHXdRr"):
                opp_val = getattr(old_value, "scrShYQYaSD_xvHXdRr", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scrShYQYaSD_xvHXdRr"):
                opp_val = getattr(value, "scrShYQYaSD_xvHXdRr", None)
                if opp_val is None:
                    setattr(value, "scrShYQYaSD_xvHXdRr", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scrShYQYaSD_xvHXdRr:

    pass