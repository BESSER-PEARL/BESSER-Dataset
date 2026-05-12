from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class rqsDsl_RAnnotation:

    def __init__(self, num: int, id: int, type: str, aa: int, ab: int, ba: int, bb: int):
        self.num = num
        self.id = id
        self.type = type
        self.aa = aa
        self.ab = ab
        self.ba = ba
        self.bb = bb
        
        pass
    @property
    def aa(self):
        return self.__aa

    @aa.setter
    def aa(self, aa: int):
        self.__aa = aa


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def ab(self):
        return self.__ab

    @ab.setter
    def ab(self, ab: int):
        self.__ab = ab


    @property
    def bb(self):
        return self.__bb

    @bb.setter
    def bb(self, bb: int):
        self.__bb = bb


    @property
    def ba(self):
        return self.__ba

    @ba.setter
    def ba(self, ba: int):
        self.__ba = ba


class rqsDsl_EObject:

    pass
class rqsDsl_Requirement:

    def __init__(self, text: str, rqsDsl_Requirement: "rqsDsl_Model" = None):
        self.text = text
        self.rqsDsl_Requirement = rqsDsl_Requirement
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def rqsDsl_Requirement(self):
        return self.__rqsDsl_Requirement

    @rqsDsl_Requirement.setter
    def rqsDsl_Requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_rqsDsl_Requirement__rqsDsl_Requirement", None)
        self.__rqsDsl_Requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rqsDsl_Model"):
                opp_val = getattr(old_value, "rqsDsl_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rqsDsl_Model"):
                opp_val = getattr(value, "rqsDsl_Model", None)
                if opp_val is None:
                    setattr(value, "rqsDsl_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class rqsDsl_TAnnotation:

    def __init__(self, text: str, num: int, id: int, type: str, a: int, b: int):
        self.text = text
        self.num = num
        self.id = id
        self.type = type
        self.a = a
        self.b = b
        
        pass
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num: int):
        self.__num = num


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a


    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b


class rqsDsl_Model:

    pass