from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class classmate_Friend:

    def __init__(self, fromDate: str, toDate: str, classmate_Friend: "classmate_ClassmateSystem" = None, classmate_Friend8: "classmate_Student" = None, classmate_Friend11: "classmate_Student" = None):
        self.fromDate = fromDate
        self.toDate = toDate
        self.classmate_Friend = classmate_Friend
        self.classmate_Friend8 = classmate_Friend8
        self.classmate_Friend11 = classmate_Friend11
        
    @property
    def toDate(self) -> str:
        return self.__toDate

    @toDate.setter
    def toDate(self, toDate: str):
        self.__toDate = toDate

    @property
    def fromDate(self) -> str:
        return self.__fromDate

    @fromDate.setter
    def fromDate(self, fromDate: str):
        self.__fromDate = fromDate

    @property
    def classmate_Friend(self):
        return self.__classmate_Friend

    @classmate_Friend.setter
    def classmate_Friend(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Friend__classmate_Friend", None)
        self.__classmate_Friend = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_ClassmateSystem3"):
                opp_val = getattr(old_value, "classmate_ClassmateSystem3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_ClassmateSystem3"):
                opp_val = getattr(value, "classmate_ClassmateSystem3", None)
                if opp_val is None:
                    setattr(value, "classmate_ClassmateSystem3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classmate_Friend11(self):
        return self.__classmate_Friend11

    @classmate_Friend11.setter
    def classmate_Friend11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Friend__classmate_Friend11", None)
        self.__classmate_Friend11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_Student12"):
                opp_val = getattr(old_value, "classmate_Student12", None)
                if opp_val == self:
                    setattr(old_value, "classmate_Student12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_Student12"):
                opp_val = getattr(value, "classmate_Student12", None)
                setattr(value, "classmate_Student12", self)

    @property
    def classmate_Friend8(self):
        return self.__classmate_Friend8

    @classmate_Friend8.setter
    def classmate_Friend8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Friend__classmate_Friend8", None)
        self.__classmate_Friend8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_Student9"):
                opp_val = getattr(old_value, "classmate_Student9", None)
                if opp_val == self:
                    setattr(old_value, "classmate_Student9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_Student9"):
                opp_val = getattr(value, "classmate_Student9", None)
                setattr(value, "classmate_Student9", self)

class classmate_School:

    def __init__(self, name: str, classmate_School5: set["classmate_Classroom"] = None, classmate_School: "classmate_ClassmateSystem" = None):
        self.name = name
        self.classmate_School5 = classmate_School5 if classmate_School5 is not None else set()
        self.classmate_School = classmate_School
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classmate_School5(self):
        return self.__classmate_School5

    @classmate_School5.setter
    def classmate_School5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_School__classmate_School5", None)
        self.__classmate_School5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmate_Classroom6"):
                    opp_val = getattr(item, "classmate_Classroom6", None)
                    
                    if opp_val == self:
                        setattr(item, "classmate_Classroom6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmate_Classroom6"):
                    opp_val = getattr(item, "classmate_Classroom6", None)
                    
                    setattr(item, "classmate_Classroom6", self)
                    

    @property
    def classmate_School(self):
        return self.__classmate_School

    @classmate_School.setter
    def classmate_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_School__classmate_School", None)
        self.__classmate_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_ClassmateSystem"):
                opp_val = getattr(old_value, "classmate_ClassmateSystem", None)
                if opp_val == self:
                    setattr(old_value, "classmate_ClassmateSystem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_ClassmateSystem"):
                opp_val = getattr(value, "classmate_ClassmateSystem", None)
                setattr(value, "classmate_ClassmateSystem", self)

class classmate_ClassmateSystem:

    pass
class classmate_Student:

    def __init__(self, name: str, classmate_Student: "classmate_Classroom" = None, classmate_Student9: "classmate_Friend" = None, classmate_Student12: "classmate_Friend" = None):
        self.name = name
        self.classmate_Student = classmate_Student
        self.classmate_Student9 = classmate_Student9
        self.classmate_Student12 = classmate_Student12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classmate_Student12(self):
        return self.__classmate_Student12

    @classmate_Student12.setter
    def classmate_Student12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Student__classmate_Student12", None)
        self.__classmate_Student12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_Friend11"):
                opp_val = getattr(old_value, "classmate_Friend11", None)
                if opp_val == self:
                    setattr(old_value, "classmate_Friend11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_Friend11"):
                opp_val = getattr(value, "classmate_Friend11", None)
                setattr(value, "classmate_Friend11", self)

    @property
    def classmate_Student(self):
        return self.__classmate_Student

    @classmate_Student.setter
    def classmate_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Student__classmate_Student", None)
        self.__classmate_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_Classroom"):
                opp_val = getattr(old_value, "classmate_Classroom", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_Classroom"):
                opp_val = getattr(value, "classmate_Classroom", None)
                if opp_val is None:
                    setattr(value, "classmate_Classroom", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def classmate_Student9(self):
        return self.__classmate_Student9

    @classmate_Student9.setter
    def classmate_Student9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Student__classmate_Student9", None)
        self.__classmate_Student9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_Friend8"):
                opp_val = getattr(old_value, "classmate_Friend8", None)
                if opp_val == self:
                    setattr(old_value, "classmate_Friend8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_Friend8"):
                opp_val = getattr(value, "classmate_Friend8", None)
                setattr(value, "classmate_Friend8", self)

class classmate_Classroom:

    def __init__(self, name: str, classmate_Classroom6: "classmate_School" = None, classmate_Classroom: set["classmate_Student"] = None):
        self.name = name
        self.classmate_Classroom6 = classmate_Classroom6
        self.classmate_Classroom = classmate_Classroom if classmate_Classroom is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def classmate_Classroom(self):
        return self.__classmate_Classroom

    @classmate_Classroom.setter
    def classmate_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Classroom__classmate_Classroom", None)
        self.__classmate_Classroom = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "classmate_Student"):
                    opp_val = getattr(item, "classmate_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "classmate_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "classmate_Student"):
                    opp_val = getattr(item, "classmate_Student", None)
                    
                    setattr(item, "classmate_Student", self)
                    

    @property
    def classmate_Classroom6(self):
        return self.__classmate_Classroom6

    @classmate_Classroom6.setter
    def classmate_Classroom6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_classmate_Classroom__classmate_Classroom6", None)
        self.__classmate_Classroom6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "classmate_School5"):
                opp_val = getattr(old_value, "classmate_School5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "classmate_School5"):
                opp_val = getattr(value, "classmate_School5", None)
                if opp_val is None:
                    setattr(value, "classmate_School5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
