from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class university_Student:

    def __init__(self, semester: int, MNR: str, Student: "university_Certificate" = None, university_Student: "university_University" = None, student: set["university_Certificate"] = None):
        self.semester = semester
        self.MNR = MNR
        self.Student = Student
        self.university_Student = university_Student
        self.student = student if student is not None else set()
        
    @property
    def semester(self) -> int:
        return self.__semester

    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester

    @property
    def MNR(self) -> str:
        return self.__MNR

    @MNR.setter
    def MNR(self, MNR: str):
        self.__MNR = MNR

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__student", None)
        self.__student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Certificate11"):
                    opp_val = getattr(item, "Certificate11", None)
                    
                    if opp_val == self:
                        setattr(item, "Certificate11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Certificate11"):
                    opp_val = getattr(item, "Certificate11", None)
                    
                    setattr(item, "Certificate11", self)
                    

    @property
    def university_Student(self):
        return self.__university_Student

    @university_Student.setter
    def university_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__university_Student", None)
        self.__university_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University7"):
                opp_val = getattr(old_value, "university_University7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University7"):
                opp_val = getattr(value, "university_University7", None)
                if opp_val is None:
                    setattr(value, "university_University7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studentCertificates"):
                opp_val = getattr(old_value, "studentCertificates", None)
                if opp_val == self:
                    setattr(old_value, "studentCertificates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studentCertificates"):
                opp_val = getattr(value, "studentCertificates", None)
                setattr(value, "studentCertificates", self)

class university_Certificate:

    def __init__(self, note: int, Certificate: "university_Course" = None, studentCertificates: "university_Student" = None, courseCertificates: "university_Course" = None, university_Certificate: "university_University" = None, Certificate11: "university_Student" = None):
        self.note = note
        self.Certificate = Certificate
        self.studentCertificates = studentCertificates
        self.courseCertificates = courseCertificates
        self.university_Certificate = university_Certificate
        self.Certificate11 = Certificate11
        
    @property
    def note(self) -> int:
        return self.__note

    @note.setter
    def note(self, note: int):
        self.__note = note

    @property
    def Certificate(self):
        return self.__Certificate

    @Certificate.setter
    def Certificate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Certificate__Certificate", None)
        self.__Certificate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                if opp_val is None:
                    setattr(value, "course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studentCertificates(self):
        return self.__studentCertificates

    @studentCertificates.setter
    def studentCertificates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Certificate__studentCertificates", None)
        self.__studentCertificates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student"):
                opp_val = getattr(old_value, "Student", None)
                if opp_val == self:
                    setattr(old_value, "Student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student"):
                opp_val = getattr(value, "Student", None)
                setattr(value, "Student", self)

    @property
    def Certificate11(self):
        return self.__Certificate11

    @Certificate11.setter
    def Certificate11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Certificate__Certificate11", None)
        self.__Certificate11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student"):
                opp_val = getattr(old_value, "student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student"):
                opp_val = getattr(value, "student", None)
                if opp_val is None:
                    setattr(value, "student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courseCertificates(self):
        return self.__courseCertificates

    @courseCertificates.setter
    def courseCertificates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Certificate__courseCertificates", None)
        self.__courseCertificates = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course14"):
                opp_val = getattr(old_value, "Course14", None)
                if opp_val == self:
                    setattr(old_value, "Course14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course14"):
                opp_val = getattr(value, "Course14", None)
                setattr(value, "Course14", self)

    @property
    def university_Certificate(self):
        return self.__university_Certificate

    @university_Certificate.setter
    def university_Certificate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Certificate__university_Certificate", None)
        self.__university_Certificate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University9"):
                opp_val = getattr(old_value, "university_University9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University9"):
                opp_val = getattr(value, "university_University9", None)
                if opp_val is None:
                    setattr(value, "university_University9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Professor:

    def __init__(self, name: str, professor: set["university_Course"] = None, university_Professor: "university_University" = None, Professor: "university_Course" = None):
        self.name = name
        self.professor = professor if professor is not None else set()
        self.university_Professor = university_Professor
        self.Professor = Professor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__professor", None)
        self.__professor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    if opp_val == self:
                        setattr(item, "Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    setattr(item, "Course", self)
                    

    @property
    def university_Professor(self):
        return self.__university_Professor

    @university_Professor.setter
    def university_Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__university_Professor", None)
        self.__university_Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University"):
                opp_val = getattr(old_value, "university_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University"):
                opp_val = getattr(value, "university_University", None)
                if opp_val is None:
                    setattr(value, "university_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Professor(self):
        return self.__Professor

    @Professor.setter
    def Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__Professor", None)
        self.__Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses"):
                opp_val = getattr(old_value, "courses", None)
                if opp_val == self:
                    setattr(old_value, "courses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses"):
                opp_val = getattr(value, "courses", None)
                setattr(value, "courses", self)

class university_University:

    def __init__(self, name: str, averageLength: float, numberOfStudents: int, university_University: set["university_Professor"] = None, university_University5: set["university_Course"] = None, university_University7: set["university_Student"] = None, university_University9: set["university_Certificate"] = None):
        self.name = name
        self.averageLength = averageLength
        self.numberOfStudents = numberOfStudents
        self.university_University = university_University if university_University is not None else set()
        self.university_University5 = university_University5 if university_University5 is not None else set()
        self.university_University7 = university_University7 if university_University7 is not None else set()
        self.university_University9 = university_University9 if university_University9 is not None else set()
        
    @property
    def averageLength(self) -> float:
        return self.__averageLength

    @averageLength.setter
    def averageLength(self, averageLength: float):
        self.__averageLength = averageLength

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfStudents(self) -> int:
        return self.__numberOfStudents

    @numberOfStudents.setter
    def numberOfStudents(self, numberOfStudents: int):
        self.__numberOfStudents = numberOfStudents

    @property
    def university_University9(self):
        return self.__university_University9

    @university_University9.setter
    def university_University9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University9", None)
        self.__university_University9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Certificate"):
                    opp_val = getattr(item, "university_Certificate", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Certificate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Certificate"):
                    opp_val = getattr(item, "university_Certificate", None)
                    
                    setattr(item, "university_Certificate", self)
                    

    @property
    def university_University(self):
        return self.__university_University

    @university_University.setter
    def university_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University", None)
        self.__university_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Professor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    setattr(item, "university_Professor", self)
                    

    @property
    def university_University5(self):
        return self.__university_University5

    @university_University5.setter
    def university_University5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University5", None)
        self.__university_University5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Course"):
                    opp_val = getattr(item, "university_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Course"):
                    opp_val = getattr(item, "university_Course", None)
                    
                    setattr(item, "university_Course", self)
                    

    @property
    def university_University7(self):
        return self.__university_University7

    @university_University7.setter
    def university_University7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University7", None)
        self.__university_University7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Student"):
                    opp_val = getattr(item, "university_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Student"):
                    opp_val = getattr(item, "university_Student", None)
                    
                    setattr(item, "university_Student", self)
                    

class university_Course:

    def __init__(self, name: str, gradeAverage: float, numberOfAttendants: int, Course: "university_Professor" = None, university_Course: "university_University" = None, courses: "university_Professor" = None, course: set["university_Certificate"] = None, Course14: "university_Certificate" = None):
        self.name = name
        self.gradeAverage = gradeAverage
        self.numberOfAttendants = numberOfAttendants
        self.Course = Course
        self.university_Course = university_Course
        self.courses = courses
        self.course = course if course is not None else set()
        self.Course14 = Course14
        
    @property
    def gradeAverage(self) -> float:
        return self.__gradeAverage

    @gradeAverage.setter
    def gradeAverage(self, gradeAverage: float):
        self.__gradeAverage = gradeAverage

    @property
    def numberOfAttendants(self) -> int:
        return self.__numberOfAttendants

    @numberOfAttendants.setter
    def numberOfAttendants(self, numberOfAttendants: int):
        self.__numberOfAttendants = numberOfAttendants

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Course14(self):
        return self.__Course14

    @Course14.setter
    def Course14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__Course14", None)
        self.__Course14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseCertificates"):
                opp_val = getattr(old_value, "courseCertificates", None)
                if opp_val == self:
                    setattr(old_value, "courseCertificates", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseCertificates"):
                opp_val = getattr(value, "courseCertificates", None)
                setattr(value, "courseCertificates", self)

    @property
    def university_Course(self):
        return self.__university_Course

    @university_Course.setter
    def university_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__university_Course", None)
        self.__university_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University5"):
                opp_val = getattr(old_value, "university_University5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University5"):
                opp_val = getattr(value, "university_University5", None)
                if opp_val is None:
                    setattr(value, "university_University5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professor"):
                opp_val = getattr(old_value, "professor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professor"):
                opp_val = getattr(value, "professor", None)
                if opp_val is None:
                    setattr(value, "professor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Certificate"):
                    opp_val = getattr(item, "Certificate", None)
                    
                    if opp_val == self:
                        setattr(item, "Certificate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Certificate"):
                    opp_val = getattr(item, "Certificate", None)
                    
                    setattr(item, "Certificate", self)
                    

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Professor"):
                opp_val = getattr(old_value, "Professor", None)
                if opp_val == self:
                    setattr(old_value, "Professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Professor"):
                opp_val = getattr(value, "Professor", None)
                setattr(value, "Professor", self)
