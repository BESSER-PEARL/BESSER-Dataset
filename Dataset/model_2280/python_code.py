from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Response:

    def __init__(self, ID: int, ok: bool, comment: str, model_Response: "model_Delivery" = None):
        self.ID = ID
        self.ok = ok
        self.comment = comment
        self.model_Response = model_Response
        
    @property
    def ok(self) -> bool:
        return self.__ok

    @ok.setter
    def ok(self, ok: bool):
        self.__ok = ok

    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def model_Response(self):
        return self.__model_Response

    @model_Response.setter
    def model_Response(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Response__model_Response", None)
        self.__model_Response = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Delivery20"):
                opp_val = getattr(old_value, "model_Delivery20", None)
                if opp_val == self:
                    setattr(old_value, "model_Delivery20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Delivery20"):
                opp_val = getattr(value, "model_Delivery20", None)
                setattr(value, "model_Delivery20", self)

class model_Exercise:

    def __init__(self, deadline_date: date, ID: int, model_Exercise18: "model_Course" = None, model_Exercise: set["model_Delivery"] = None, model_Exercise14: set["model_Student"] = None):
        self.deadline_date = deadline_date
        self.ID = ID
        self.model_Exercise18 = model_Exercise18
        self.model_Exercise = model_Exercise if model_Exercise is not None else set()
        self.model_Exercise14 = model_Exercise14 if model_Exercise14 is not None else set()
        
    @property
    def deadline_date(self) -> date:
        return self.__deadline_date

    @deadline_date.setter
    def deadline_date(self, deadline_date: date):
        self.__deadline_date = deadline_date

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def model_Exercise(self):
        return self.__model_Exercise

    @model_Exercise.setter
    def model_Exercise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Exercise__model_Exercise", None)
        self.__model_Exercise = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Delivery12"):
                    opp_val = getattr(item, "model_Delivery12", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Delivery12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Delivery12"):
                    opp_val = getattr(item, "model_Delivery12", None)
                    
                    setattr(item, "model_Delivery12", self)
                    

    @property
    def model_Exercise14(self):
        return self.__model_Exercise14

    @model_Exercise14.setter
    def model_Exercise14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Exercise__model_Exercise14", None)
        self.__model_Exercise14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Student15"):
                    opp_val = getattr(item, "model_Student15", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Student15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Student15"):
                    opp_val = getattr(item, "model_Student15", None)
                    
                    setattr(item, "model_Student15", self)
                    

    @property
    def model_Exercise18(self):
        return self.__model_Exercise18

    @model_Exercise18.setter
    def model_Exercise18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Exercise__model_Exercise18", None)
        self.__model_Exercise18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Course17"):
                opp_val = getattr(old_value, "model_Course17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Course17"):
                opp_val = getattr(value, "model_Course17", None)
                if opp_val is None:
                    setattr(value, "model_Course17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Course:

    def __init__(self, ID: int, name: str, model_Course: "model_root" = None, model_Course17: set["model_Exercise"] = None, model_Course7: "model_Student" = None):
        self.ID = ID
        self.name = name
        self.model_Course = model_Course
        self.model_Course17 = model_Course17 if model_Course17 is not None else set()
        self.model_Course7 = model_Course7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def model_Course17(self):
        return self.__model_Course17

    @model_Course17.setter
    def model_Course17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course17", None)
        self.__model_Course17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Exercise18"):
                    opp_val = getattr(item, "model_Exercise18", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Exercise18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Exercise18"):
                    opp_val = getattr(item, "model_Exercise18", None)
                    
                    setattr(item, "model_Exercise18", self)
                    

    @property
    def model_Course(self):
        return self.__model_Course

    @model_Course.setter
    def model_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course", None)
        self.__model_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_root2"):
                opp_val = getattr(old_value, "model_root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_root2"):
                opp_val = getattr(value, "model_root2", None)
                if opp_val is None:
                    setattr(value, "model_root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Course7(self):
        return self.__model_Course7

    @model_Course7.setter
    def model_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course7", None)
        self.__model_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Student6"):
                opp_val = getattr(old_value, "model_Student6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Student6"):
                opp_val = getattr(value, "model_Student6", None)
                if opp_val is None:
                    setattr(value, "model_Student6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Student:

    def __init__(self, ID: int, name: str, model_Student: "model_root" = None, model_Student6: set["model_Course"] = None, model_Student9: set["model_Delivery"] = None, model_Student15: "model_Exercise" = None):
        self.ID = ID
        self.name = name
        self.model_Student = model_Student
        self.model_Student6 = model_Student6 if model_Student6 is not None else set()
        self.model_Student9 = model_Student9 if model_Student9 is not None else set()
        self.model_Student15 = model_Student15
        
    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Student6(self):
        return self.__model_Student6

    @model_Student6.setter
    def model_Student6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Student__model_Student6", None)
        self.__model_Student6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Course7"):
                    opp_val = getattr(item, "model_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Course7"):
                    opp_val = getattr(item, "model_Course7", None)
                    
                    setattr(item, "model_Course7", self)
                    

    @property
    def model_Student(self):
        return self.__model_Student

    @model_Student.setter
    def model_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Student__model_Student", None)
        self.__model_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_root"):
                opp_val = getattr(old_value, "model_root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_root"):
                opp_val = getattr(value, "model_root", None)
                if opp_val is None:
                    setattr(value, "model_root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Student9(self):
        return self.__model_Student9

    @model_Student9.setter
    def model_Student9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Student__model_Student9", None)
        self.__model_Student9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Delivery10"):
                    opp_val = getattr(item, "model_Delivery10", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Delivery10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Delivery10"):
                    opp_val = getattr(item, "model_Delivery10", None)
                    
                    setattr(item, "model_Delivery10", self)
                    

    @property
    def model_Student15(self):
        return self.__model_Student15

    @model_Student15.setter
    def model_Student15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Student__model_Student15", None)
        self.__model_Student15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Exercise14"):
                opp_val = getattr(old_value, "model_Exercise14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Exercise14"):
                opp_val = getattr(value, "model_Exercise14", None)
                if opp_val is None:
                    setattr(value, "model_Exercise14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_root:

    pass
class model_Delivery:

    def __init__(self, ID: int, group_number: int, answer: str, submission_date: date, model_Delivery: "model_root" = None, model_Delivery10: "model_Student" = None, model_Delivery12: "model_Exercise" = None, model_Delivery20: "model_Response" = None):
        self.ID = ID
        self.group_number = group_number
        self.answer = answer
        self.submission_date = submission_date
        self.model_Delivery = model_Delivery
        self.model_Delivery10 = model_Delivery10
        self.model_Delivery12 = model_Delivery12
        self.model_Delivery20 = model_Delivery20
        
    @property
    def submission_date(self) -> date:
        return self.__submission_date

    @submission_date.setter
    def submission_date(self, submission_date: date):
        self.__submission_date = submission_date

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def group_number(self) -> int:
        return self.__group_number

    @group_number.setter
    def group_number(self, group_number: int):
        self.__group_number = group_number

    @property
    def answer(self) -> str:
        return self.__answer

    @answer.setter
    def answer(self, answer: str):
        self.__answer = answer

    @property
    def model_Delivery20(self):
        return self.__model_Delivery20

    @model_Delivery20.setter
    def model_Delivery20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Delivery__model_Delivery20", None)
        self.__model_Delivery20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Response"):
                opp_val = getattr(old_value, "model_Response", None)
                if opp_val == self:
                    setattr(old_value, "model_Response", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Response"):
                opp_val = getattr(value, "model_Response", None)
                setattr(value, "model_Response", self)

    @property
    def model_Delivery10(self):
        return self.__model_Delivery10

    @model_Delivery10.setter
    def model_Delivery10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Delivery__model_Delivery10", None)
        self.__model_Delivery10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Student9"):
                opp_val = getattr(old_value, "model_Student9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Student9"):
                opp_val = getattr(value, "model_Student9", None)
                if opp_val is None:
                    setattr(value, "model_Student9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Delivery(self):
        return self.__model_Delivery

    @model_Delivery.setter
    def model_Delivery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Delivery__model_Delivery", None)
        self.__model_Delivery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_root4"):
                opp_val = getattr(old_value, "model_root4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_root4"):
                opp_val = getattr(value, "model_root4", None)
                if opp_val is None:
                    setattr(value, "model_root4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Delivery12(self):
        return self.__model_Delivery12

    @model_Delivery12.setter
    def model_Delivery12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Delivery__model_Delivery12", None)
        self.__model_Delivery12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Exercise"):
                opp_val = getattr(old_value, "model_Exercise", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Exercise"):
                opp_val = getattr(value, "model_Exercise", None)
                if opp_val is None:
                    setattr(value, "model_Exercise", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
