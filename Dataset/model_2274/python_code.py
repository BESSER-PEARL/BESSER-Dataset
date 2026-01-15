from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class education_School:

    def __init__(self, name: str, address: str, phone: str, education_School: set["education_Student"] = None, education_School2: set["education_Course"] = None, education_School5: "education_Student" = None, education_School14: "education_Course" = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.education_School = education_School if education_School is not None else set()
        self.education_School2 = education_School2 if education_School2 is not None else set()
        self.education_School5 = education_School5
        self.education_School14 = education_School14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def education_School5(self):
        return self.__education_School5

    @education_School5.setter
    def education_School5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_School__education_School5", None)
        self.__education_School5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_Student4"):
                opp_val = getattr(old_value, "education_Student4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_Student4"):
                opp_val = getattr(value, "education_Student4", None)
                if opp_val is None:
                    setattr(value, "education_Student4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def education_School14(self):
        return self.__education_School14

    @education_School14.setter
    def education_School14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_School__education_School14", None)
        self.__education_School14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_Course13"):
                opp_val = getattr(old_value, "education_Course13", None)
                if opp_val == self:
                    setattr(old_value, "education_Course13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_Course13"):
                opp_val = getattr(value, "education_Course13", None)
                setattr(value, "education_Course13", self)

    @property
    def education_School(self):
        return self.__education_School

    @education_School.setter
    def education_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_School__education_School", None)
        self.__education_School = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_Student"):
                    opp_val = getattr(item, "education_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "education_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_Student"):
                    opp_val = getattr(item, "education_Student", None)
                    
                    setattr(item, "education_Student", self)
                    

    @property
    def education_School2(self):
        return self.__education_School2

    @education_School2.setter
    def education_School2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_School__education_School2", None)
        self.__education_School2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_Course"):
                    opp_val = getattr(item, "education_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "education_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_Course"):
                    opp_val = getattr(item, "education_Course", None)
                    
                    setattr(item, "education_Course", self)
                    

class education_Course:

    def __init__(self, name: str, education_Course: "education_School" = None, education_Course8: "education_Student" = None, education_Course10: set["education_Student"] = None, education_Course13: "education_School" = None):
        self.name = name
        self.education_Course = education_Course
        self.education_Course8 = education_Course8
        self.education_Course10 = education_Course10 if education_Course10 is not None else set()
        self.education_Course13 = education_Course13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def education_Course10(self):
        return self.__education_Course10

    @education_Course10.setter
    def education_Course10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course10", None)
        self.__education_Course10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_Student11"):
                    opp_val = getattr(item, "education_Student11", None)
                    
                    if opp_val == self:
                        setattr(item, "education_Student11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_Student11"):
                    opp_val = getattr(item, "education_Student11", None)
                    
                    setattr(item, "education_Student11", self)
                    

    @property
    def education_Course13(self):
        return self.__education_Course13

    @education_Course13.setter
    def education_Course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course13", None)
        self.__education_Course13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_School14"):
                opp_val = getattr(old_value, "education_School14", None)
                if opp_val == self:
                    setattr(old_value, "education_School14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_School14"):
                opp_val = getattr(value, "education_School14", None)
                setattr(value, "education_School14", self)

    @property
    def education_Course(self):
        return self.__education_Course

    @education_Course.setter
    def education_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course", None)
        self.__education_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_School2"):
                opp_val = getattr(old_value, "education_School2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_School2"):
                opp_val = getattr(value, "education_School2", None)
                if opp_val is None:
                    setattr(value, "education_School2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def education_Course8(self):
        return self.__education_Course8

    @education_Course8.setter
    def education_Course8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course8", None)
        self.__education_Course8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_Student7"):
                opp_val = getattr(old_value, "education_Student7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_Student7"):
                opp_val = getattr(value, "education_Student7", None)
                if opp_val is None:
                    setattr(value, "education_Student7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class education_Student:

    def __init__(self, name: str, education_Student: "education_School" = None, education_Student4: set["education_School"] = None, education_Student7: set["education_Course"] = None, education_Student11: "education_Course" = None):
        self.name = name
        self.education_Student = education_Student
        self.education_Student4 = education_Student4 if education_Student4 is not None else set()
        self.education_Student7 = education_Student7 if education_Student7 is not None else set()
        self.education_Student11 = education_Student11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def education_Student11(self):
        return self.__education_Student11

    @education_Student11.setter
    def education_Student11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Student__education_Student11", None)
        self.__education_Student11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_Course10"):
                opp_val = getattr(old_value, "education_Course10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_Course10"):
                opp_val = getattr(value, "education_Course10", None)
                if opp_val is None:
                    setattr(value, "education_Course10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def education_Student(self):
        return self.__education_Student

    @education_Student.setter
    def education_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Student__education_Student", None)
        self.__education_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_School"):
                opp_val = getattr(old_value, "education_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_School"):
                opp_val = getattr(value, "education_School", None)
                if opp_val is None:
                    setattr(value, "education_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def education_Student4(self):
        return self.__education_Student4

    @education_Student4.setter
    def education_Student4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Student__education_Student4", None)
        self.__education_Student4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_School5"):
                    opp_val = getattr(item, "education_School5", None)
                    
                    if opp_val == self:
                        setattr(item, "education_School5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_School5"):
                    opp_val = getattr(item, "education_School5", None)
                    
                    setattr(item, "education_School5", self)
                    

    @property
    def education_Student7(self):
        return self.__education_Student7

    @education_Student7.setter
    def education_Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Student__education_Student7", None)
        self.__education_Student7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_Course8"):
                    opp_val = getattr(item, "education_Course8", None)
                    
                    if opp_val == self:
                        setattr(item, "education_Course8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_Course8"):
                    opp_val = getattr(item, "education_Course8", None)
                    
                    setattr(item, "education_Course8", self)
                    
