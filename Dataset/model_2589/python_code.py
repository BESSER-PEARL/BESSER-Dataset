from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class testSubpackages1_root_testSubpackages1_subpackage2_class3:

    pass
class testSubpackages1_root_testSubpackages1_subpackage3_class4:

    pass
class testSubpackages1_root_testSubpackages1_subpackage1_class2:

    pass
class class3:

    pass
class testSubpackages1_root_class1:

    def __init__(self, a: date, testSubpackages1_root_class1: "class3" = None):
        self.a = a
        self.testSubpackages1_root_class1 = testSubpackages1_root_class1
        
    @property
    def a(self) -> date:
        return self.__a

    @a.setter
    def a(self, a: date):
        self.__a = a

    @property
    def testSubpackages1_root_class1(self):
        return self.__testSubpackages1_root_class1

    @testSubpackages1_root_class1.setter
    def testSubpackages1_root_class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testSubpackages1_root_class1__testSubpackages1_root_class1", None)
        self.__testSubpackages1_root_class1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "class3"):
                opp_val = getattr(old_value, "class3", None)
                if opp_val == self:
                    setattr(old_value, "class3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "class3"):
                opp_val = getattr(value, "class3", None)
                setattr(value, "class3", self)
