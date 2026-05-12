from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Eclass5:

    pass
class ecoreTest_EClass3(Eclass5):

    pass
class ecoreTest_EClass2:

    def __init__(self, eAttribute3: str, eAttribute4: str, ecoreTest_EClass2: "ecoreTest_Eclass1" = None, ecoreTest_EClass22: set["ecoreTest_EClass3"] = None):
        self.eAttribute3 = eAttribute3
        self.eAttribute4 = eAttribute4
        self.ecoreTest_EClass2 = ecoreTest_EClass2
        self.ecoreTest_EClass22 = ecoreTest_EClass22 if ecoreTest_EClass22 is not None else set()
        
        pass
    @property
    def eAttribute3(self):
        return self.__eAttribute3

    @eAttribute3.setter
    def eAttribute3(self, eAttribute3: str):
        self.__eAttribute3 = eAttribute3


    @property
    def eAttribute4(self):
        return self.__eAttribute4

    @eAttribute4.setter
    def eAttribute4(self, eAttribute4: str):
        self.__eAttribute4 = eAttribute4


    @property
    def ecoreTest_EClass22(self):
        return self.__ecoreTest_EClass22

    @ecoreTest_EClass22.setter
    def ecoreTest_EClass22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreTest_EClass2__ecoreTest_EClass22", None)
        self.__ecoreTest_EClass22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreTest_EClass3"):
                    opp_val = getattr(item, "ecoreTest_EClass3", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreTest_EClass3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreTest_EClass3"):
                    opp_val = getattr(item, "ecoreTest_EClass3", None)
                    
                    setattr(item, "ecoreTest_EClass3", self)
                    

    @property
    def ecoreTest_EClass2(self):
        return self.__ecoreTest_EClass2

    @ecoreTest_EClass2.setter
    def ecoreTest_EClass2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreTest_EClass2__ecoreTest_EClass2", None)
        self.__ecoreTest_EClass2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ecoreTest_Eclass1"):
                opp_val = getattr(old_value, "ecoreTest_Eclass1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ecoreTest_Eclass1"):
                opp_val = getattr(value, "ecoreTest_Eclass1", None)
                if opp_val is None:
                    setattr(value, "ecoreTest_Eclass1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ecoreTest_Eclass1:

    def __init__(self, eAttribute1: str, eAttribute2: str, ecoreTest_Eclass1: set["ecoreTest_EClass2"] = None):
        self.eAttribute1 = eAttribute1
        self.eAttribute2 = eAttribute2
        self.ecoreTest_Eclass1 = ecoreTest_Eclass1 if ecoreTest_Eclass1 is not None else set()
        
        pass
    @property
    def eAttribute1(self):
        return self.__eAttribute1

    @eAttribute1.setter
    def eAttribute1(self, eAttribute1: str):
        self.__eAttribute1 = eAttribute1


    @property
    def eAttribute2(self):
        return self.__eAttribute2

    @eAttribute2.setter
    def eAttribute2(self, eAttribute2: str):
        self.__eAttribute2 = eAttribute2


    @property
    def ecoreTest_Eclass1(self):
        return self.__ecoreTest_Eclass1

    @ecoreTest_Eclass1.setter
    def ecoreTest_Eclass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ecoreTest_Eclass1__ecoreTest_Eclass1", None)
        self.__ecoreTest_Eclass1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ecoreTest_EClass2"):
                    opp_val = getattr(item, "ecoreTest_EClass2", None)
                    
                    if opp_val == self:
                        setattr(item, "ecoreTest_EClass2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ecoreTest_EClass2"):
                    opp_val = getattr(item, "ecoreTest_EClass2", None)
                    
                    setattr(item, "ecoreTest_EClass2", self)
                    
