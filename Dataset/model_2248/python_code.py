from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tdt4250_StudyProgram:

    def __init__(self, number_of_semesters: int, name: str, tdt4250_StudyProgram: set["tdt4250_Student"] = None, tdt4250_StudyProgram2: set["tdt4250_Specialisation"] = None, tdt4250_StudyProgram4: set["tdt4250_Course"] = None):
        self.number_of_semesters = number_of_semesters
        self.name = name
        self.tdt4250_StudyProgram = tdt4250_StudyProgram if tdt4250_StudyProgram is not None else set()
        self.tdt4250_StudyProgram2 = tdt4250_StudyProgram2 if tdt4250_StudyProgram2 is not None else set()
        self.tdt4250_StudyProgram4 = tdt4250_StudyProgram4 if tdt4250_StudyProgram4 is not None else set()
        
    @property
    def number_of_semesters(self) -> int:
        return self.__number_of_semesters

    @number_of_semesters.setter
    def number_of_semesters(self, number_of_semesters: int):
        self.__number_of_semesters = number_of_semesters

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250_StudyProgram2(self):
        return self.__tdt4250_StudyProgram2

    @tdt4250_StudyProgram2.setter
    def tdt4250_StudyProgram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram2", None)
        self.__tdt4250_StudyProgram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Specialisation"):
                    opp_val = getattr(item, "tdt4250_Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Specialisation"):
                    opp_val = getattr(item, "tdt4250_Specialisation", None)
                    
                    setattr(item, "tdt4250_Specialisation", self)
                    

    @property
    def tdt4250_StudyProgram(self):
        return self.__tdt4250_StudyProgram

    @tdt4250_StudyProgram.setter
    def tdt4250_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram", None)
        self.__tdt4250_StudyProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Student"):
                    opp_val = getattr(item, "tdt4250_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Student"):
                    opp_val = getattr(item, "tdt4250_Student", None)
                    
                    setattr(item, "tdt4250_Student", self)
                    

    @property
    def tdt4250_StudyProgram4(self):
        return self.__tdt4250_StudyProgram4

    @tdt4250_StudyProgram4.setter
    def tdt4250_StudyProgram4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram4", None)
        self.__tdt4250_StudyProgram4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course"):
                    opp_val = getattr(item, "tdt4250_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course"):
                    opp_val = getattr(item, "tdt4250_Course", None)
                    
                    setattr(item, "tdt4250_Course", self)
                    

class tdt4250_Course:

    def __init__(self, code: str, name: str, study_points: float, level: str, tdt4250_Course: "tdt4250_StudyProgram" = None, tdt4250_Course16: "tdt4250_Specialisation" = None, tdt4250_Course7: "tdt4250_Student" = None, tdt4250_Course13: "tdt4250_Specialisation" = None):
        self.code = code
        self.name = name
        self.study_points = study_points
        self.level = level
        self.tdt4250_Course = tdt4250_Course
        self.tdt4250_Course16 = tdt4250_Course16
        self.tdt4250_Course7 = tdt4250_Course7
        self.tdt4250_Course13 = tdt4250_Course13
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def study_points(self) -> float:
        return self.__study_points

    @study_points.setter
    def study_points(self, study_points: float):
        self.__study_points = study_points

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def tdt4250_Course13(self):
        return self.__tdt4250_Course13

    @tdt4250_Course13.setter
    def tdt4250_Course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course13", None)
        self.__tdt4250_Course13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation12"):
                opp_val = getattr(old_value, "tdt4250_Specialisation12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation12"):
                opp_val = getattr(value, "tdt4250_Specialisation12", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Specialisation12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Course16(self):
        return self.__tdt4250_Course16

    @tdt4250_Course16.setter
    def tdt4250_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course16", None)
        self.__tdt4250_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation15"):
                opp_val = getattr(old_value, "tdt4250_Specialisation15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation15"):
                opp_val = getattr(value, "tdt4250_Specialisation15", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Specialisation15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Course7(self):
        return self.__tdt4250_Course7

    @tdt4250_Course7.setter
    def tdt4250_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course7", None)
        self.__tdt4250_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Student6"):
                opp_val = getattr(old_value, "tdt4250_Student6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Student6"):
                opp_val = getattr(value, "tdt4250_Student6", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Student6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Course(self):
        return self.__tdt4250_Course

    @tdt4250_Course.setter
    def tdt4250_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course", None)
        self.__tdt4250_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram4"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram4"):
                opp_val = getattr(value, "tdt4250_StudyProgram4", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250_Specialisation:

    def __init__(self, name: str, tdt4250_Specialisation: "tdt4250_StudyProgram" = None, tdt4250_Specialisation12: set["tdt4250_Course"] = None, tdt4250_Specialisation15: set["tdt4250_Course"] = None, tdt4250_Specialisation9: set["tdt4250_Student"] = None):
        self.name = name
        self.tdt4250_Specialisation = tdt4250_Specialisation
        self.tdt4250_Specialisation12 = tdt4250_Specialisation12 if tdt4250_Specialisation12 is not None else set()
        self.tdt4250_Specialisation15 = tdt4250_Specialisation15 if tdt4250_Specialisation15 is not None else set()
        self.tdt4250_Specialisation9 = tdt4250_Specialisation9 if tdt4250_Specialisation9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250_Specialisation(self):
        return self.__tdt4250_Specialisation

    @tdt4250_Specialisation.setter
    def tdt4250_Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation", None)
        self.__tdt4250_Specialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram2"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram2"):
                opp_val = getattr(value, "tdt4250_StudyProgram2", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Specialisation12(self):
        return self.__tdt4250_Specialisation12

    @tdt4250_Specialisation12.setter
    def tdt4250_Specialisation12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation12", None)
        self.__tdt4250_Specialisation12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course13"):
                    opp_val = getattr(item, "tdt4250_Course13", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course13"):
                    opp_val = getattr(item, "tdt4250_Course13", None)
                    
                    setattr(item, "tdt4250_Course13", self)
                    

    @property
    def tdt4250_Specialisation9(self):
        return self.__tdt4250_Specialisation9

    @tdt4250_Specialisation9.setter
    def tdt4250_Specialisation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation9", None)
        self.__tdt4250_Specialisation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Student10"):
                    opp_val = getattr(item, "tdt4250_Student10", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Student10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Student10"):
                    opp_val = getattr(item, "tdt4250_Student10", None)
                    
                    setattr(item, "tdt4250_Student10", self)
                    

    @property
    def tdt4250_Specialisation15(self):
        return self.__tdt4250_Specialisation15

    @tdt4250_Specialisation15.setter
    def tdt4250_Specialisation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation15", None)
        self.__tdt4250_Specialisation15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course16"):
                    opp_val = getattr(item, "tdt4250_Course16", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course16"):
                    opp_val = getattr(item, "tdt4250_Course16", None)
                    
                    setattr(item, "tdt4250_Course16", self)
                    

class tdt4250_Student:

    def __init__(self, studentID: int, current_semester: int, tdt4250_Student: "tdt4250_StudyProgram" = None, tdt4250_Student6: set["tdt4250_Course"] = None, tdt4250_Student10: "tdt4250_Specialisation" = None):
        self.studentID = studentID
        self.current_semester = current_semester
        self.tdt4250_Student = tdt4250_Student
        self.tdt4250_Student6 = tdt4250_Student6 if tdt4250_Student6 is not None else set()
        self.tdt4250_Student10 = tdt4250_Student10
        
    @property
    def current_semester(self) -> int:
        return self.__current_semester

    @current_semester.setter
    def current_semester(self, current_semester: int):
        self.__current_semester = current_semester

    @property
    def studentID(self) -> int:
        return self.__studentID

    @studentID.setter
    def studentID(self, studentID: int):
        self.__studentID = studentID

    @property
    def tdt4250_Student6(self):
        return self.__tdt4250_Student6

    @tdt4250_Student6.setter
    def tdt4250_Student6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student6", None)
        self.__tdt4250_Student6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course7"):
                    opp_val = getattr(item, "tdt4250_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course7"):
                    opp_val = getattr(item, "tdt4250_Course7", None)
                    
                    setattr(item, "tdt4250_Course7", self)
                    

    @property
    def tdt4250_Student10(self):
        return self.__tdt4250_Student10

    @tdt4250_Student10.setter
    def tdt4250_Student10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student10", None)
        self.__tdt4250_Student10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation9"):
                opp_val = getattr(old_value, "tdt4250_Specialisation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation9"):
                opp_val = getattr(value, "tdt4250_Specialisation9", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Specialisation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Student(self):
        return self.__tdt4250_Student

    @tdt4250_Student.setter
    def tdt4250_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student", None)
        self.__tdt4250_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram"):
                opp_val = getattr(value, "tdt4250_StudyProgram", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
