from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mytest_MyRoot:

    pass
class mytest_B:

    pass
class EModelElement:

    pass
class mytest_A(EModelElement):

    def __init__(self, name: str, a: "mytest_B" = None, A: "mytest_B" = None, mytest_A: "mytest_MyRoot" = None):
        self.name = name
        self.a = a
        self.A = A
        self.mytest_A = mytest_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mytest_A(self):
        return self.__mytest_A

    @mytest_A.setter
    def mytest_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_A__mytest_A", None)
        self.__mytest_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytest_MyRoot"):
                opp_val = getattr(old_value, "mytest_MyRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytest_MyRoot"):
                opp_val = getattr(value, "mytest_MyRoot", None)
                if opp_val is None:
                    setattr(value, "mytest_MyRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def A(self):
        return self.__A

    @A.setter
    def A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_A__A", None)
        self.__A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b"):
                opp_val = getattr(old_value, "b", None)
                if opp_val == self:
                    setattr(old_value, "b", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b"):
                opp_val = getattr(value, "b", None)
                setattr(value, "b", self)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_A__a", None)
        self.__a = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B"):
                opp_val = getattr(old_value, "B", None)
                if opp_val == self:
                    setattr(old_value, "B", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B"):
                opp_val = getattr(value, "B", None)
                setattr(value, "B", self)
