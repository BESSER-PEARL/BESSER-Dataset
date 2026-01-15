from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class prosjekt_CourseCoordinator:

    pass
class prosjekt_Semester:

    def __init__(self, name: str, averageGrade: float, amountA: int, amountB: int, amountC: int, amountD: int, amountE: int, amountF: int, Semester: "prosjekt_Course" = None, semester: "prosjekt_Course" = None):
        self.name = name
        self.averageGrade = averageGrade
        self.amountA = amountA
        self.amountB = amountB
        self.amountC = amountC
        self.amountD = amountD
        self.amountE = amountE
        self.amountF = amountF
        self.Semester = Semester
        self.semester = semester
        
    @property
    def averageGrade(self) -> float:
        return self.__averageGrade

    @averageGrade.setter
    def averageGrade(self, averageGrade: float):
        self.__averageGrade = averageGrade

    @property
    def amountE(self) -> int:
        return self.__amountE

    @amountE.setter
    def amountE(self, amountE: int):
        self.__amountE = amountE

    @property
    def amountF(self) -> int:
        return self.__amountF

    @amountF.setter
    def amountF(self, amountF: int):
        self.__amountF = amountF

    @property
    def amountB(self) -> int:
        return self.__amountB

    @amountB.setter
    def amountB(self, amountB: int):
        self.__amountB = amountB

    @property
    def amountA(self) -> int:
        return self.__amountA

    @amountA.setter
    def amountA(self, amountA: int):
        self.__amountA = amountA

    @property
    def amountD(self) -> int:
        return self.__amountD

    @amountD.setter
    def amountD(self, amountD: int):
        self.__amountD = amountD

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def amountC(self) -> int:
        return self.__amountC

    @amountC.setter
    def amountC(self, amountC: int):
        self.__amountC = amountC

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course7"):
                opp_val = getattr(old_value, "course7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course7"):
                opp_val = getattr(value, "course7", None)
                if opp_val is None:
                    setattr(value, "course7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Semester__semester", None)
        self.__semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course9"):
                opp_val = getattr(old_value, "Course9", None)
                if opp_val == self:
                    setattr(old_value, "Course9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course9"):
                opp_val = getattr(value, "Course9", None)
                setattr(value, "Course9", self)

class prosjekt_Person:

    def __init__(self, name: str, Person: "prosjekt_Department" = None, staff: "prosjekt_Department" = None, person: set["prosjekt_CourseCoordinator"] = None, Person15: "prosjekt_CourseCoordinator" = None):
        self.name = name
        self.Person = Person
        self.staff = staff
        self.person = person if person is not None else set()
        self.Person15 = Person15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def staff(self):
        return self.__staff

    @staff.setter
    def staff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Person__staff", None)
        self.__staff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department11"):
                opp_val = getattr(old_value, "Department11", None)
                if opp_val == self:
                    setattr(old_value, "Department11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department11"):
                opp_val = getattr(value, "Department11", None)
                setattr(value, "Department11", self)

    @property
    def Person15(self):
        return self.__Person15

    @Person15.setter
    def Person15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Person__Person15", None)
        self.__Person15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles"):
                opp_val = getattr(old_value, "roles", None)
                if opp_val == self:
                    setattr(old_value, "roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles"):
                opp_val = getattr(value, "roles", None)
                setattr(value, "roles", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "worksForDepartment"):
                opp_val = getattr(old_value, "worksForDepartment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "worksForDepartment"):
                opp_val = getattr(value, "worksForDepartment", None)
                if opp_val is None:
                    setattr(value, "worksForDepartment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseCoordinator"):
                    opp_val = getattr(item, "CourseCoordinator", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseCoordinator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseCoordinator"):
                    opp_val = getattr(item, "CourseCoordinator", None)
                    
                    setattr(item, "CourseCoordinator", self)
                    

class prosjekt_Course:

    def __init__(self, name: str, code: str, studyPoints: float, Course: "prosjekt_Department" = None, course7: set["prosjekt_Semester"] = None, course: "prosjekt_Department" = None, Course9: "prosjekt_Semester" = None, prosjekt_Course: "prosjekt_CourseCoordinator" = None):
        self.name = name
        self.code = code
        self.studyPoints = studyPoints
        self.Course = Course
        self.course7 = course7 if course7 is not None else set()
        self.course = course
        self.Course9 = Course9
        self.prosjekt_Course = prosjekt_Course
        
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
    def studyPoints(self) -> float:
        return self.__studyPoints

    @studyPoints.setter
    def studyPoints(self, studyPoints: float):
        self.__studyPoints = studyPoints

    @property
    def prosjekt_Course(self):
        return self.__prosjekt_Course

    @prosjekt_Course.setter
    def prosjekt_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__prosjekt_Course", None)
        self.__prosjekt_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "prosjekt_CourseCoordinator"):
                opp_val = getattr(old_value, "prosjekt_CourseCoordinator", None)
                if opp_val == self:
                    setattr(old_value, "prosjekt_CourseCoordinator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "prosjekt_CourseCoordinator"):
                opp_val = getattr(value, "prosjekt_CourseCoordinator", None)
                setattr(value, "prosjekt_CourseCoordinator", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course7(self):
        return self.__course7

    @course7.setter
    def course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__course7", None)
        self.__course7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    setattr(item, "Semester", self)
                    

    @property
    def Course9(self):
        return self.__Course9

    @Course9.setter
    def Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__Course9", None)
        self.__Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester"):
                opp_val = getattr(old_value, "semester", None)
                if opp_val == self:
                    setattr(old_value, "semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester"):
                opp_val = getattr(value, "semester", None)
                setattr(value, "semester", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department5"):
                opp_val = getattr(old_value, "Department5", None)
                if opp_val == self:
                    setattr(old_value, "Department5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department5"):
                opp_val = getattr(value, "Department5", None)
                setattr(value, "Department5", self)

class prosjekt_University:

    def __init__(self, shortName: str, name: str, university: set["prosjekt_Department"] = None, University: "prosjekt_Department" = None):
        self.shortName = shortName
        self.name = name
        self.university = university if university is not None else set()
        self.University = University
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_University__university", None)
        self.__university = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    if opp_val == self:
                        setattr(item, "Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    setattr(item, "Department", self)
                    

    @property
    def University(self):
        return self.__University

    @University.setter
    def University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_University__University", None)
        self.__University = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departments"):
                opp_val = getattr(old_value, "departments", None)
                if opp_val == self:
                    setattr(old_value, "departments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departments"):
                opp_val = getattr(value, "departments", None)
                setattr(value, "departments", self)

class prosjekt_Department:

    def __init__(self, name: str, shortName: str, Department: "prosjekt_University" = None, departments: "prosjekt_University" = None, department: set["prosjekt_Course"] = None, worksForDepartment: set["prosjekt_Person"] = None, Department5: "prosjekt_Course" = None, Department11: "prosjekt_Person" = None):
        self.name = name
        self.shortName = shortName
        self.Department = Department
        self.departments = departments
        self.department = department if department is not None else set()
        self.worksForDepartment = worksForDepartment if worksForDepartment is not None else set()
        self.Department5 = Department5
        self.Department11 = Department11
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def Department11(self):
        return self.__Department11

    @Department11.setter
    def Department11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__Department11", None)
        self.__Department11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff"):
                opp_val = getattr(old_value, "staff", None)
                if opp_val == self:
                    setattr(old_value, "staff", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff"):
                opp_val = getattr(value, "staff", None)
                setattr(value, "staff", self)

    @property
    def Department5(self):
        return self.__Department5

    @Department5.setter
    def Department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__Department5", None)
        self.__Department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if opp_val == self:
                    setattr(old_value, "course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                setattr(value, "course", self)

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__department", None)
        self.__department = value if value is not None else set()
        
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
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university"):
                opp_val = getattr(old_value, "university", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university"):
                opp_val = getattr(value, "university", None)
                if opp_val is None:
                    setattr(value, "university", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def worksForDepartment(self):
        return self.__worksForDepartment

    @worksForDepartment.setter
    def worksForDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__worksForDepartment", None)
        self.__worksForDepartment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Department__departments", None)
        self.__departments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University"):
                opp_val = getattr(old_value, "University", None)
                if opp_val == self:
                    setattr(old_value, "University", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University"):
                opp_val = getattr(value, "University", None)
                setattr(value, "University", self)
