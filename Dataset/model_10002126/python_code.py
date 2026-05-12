from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Administrator:

    def __init__(self, name: str, administratorID: int):
        self.name = name
        self.administratorID = administratorID
        
        pass
    @property
    def administratorID(self):
        return self.__administratorID
    @administratorID.setter
    def administratorID(self, administratorID: int):
        self.__administratorID = administratorID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Course:

    def __init__(self, courseName: str, subjectCode: str, department3: "Department" = None):
        self.courseName = courseName
        self.subjectCode = subjectCode
        self.department3 = department3
        
        pass
    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: str):
        self.__subjectCode = subjectCode

    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def department3(self):
        return self.__department3
    @department3.setter
    def department3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__department3", None)
        self.__department3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course2"):
                opp_val = getattr(old_value, "course2", None)
                if opp_val == self:
                    setattr(old_value, "course2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course2"):
                opp_val = getattr(value, "course2", None)
                setattr(value, "course2", self)



class Student:

    def __init__(self, name: str, scholarNo: int, branch: Department, semester: int, department5: "Department" = None):
        self.name = name
        self.scholarNo = scholarNo
        self.branch = branch
        self.semester = semester
        self.department5 = department5
        
        pass
    @property
    def scholarNo(self):
        return self.__scholarNo
    @scholarNo.setter
    def scholarNo(self, scholarNo: int):
        self.__scholarNo = scholarNo

    @property
    def branch(self):
        return self.__branch
    @branch.setter
    def branch(self, branch: Department):
        self.__branch = branch

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester

    @property
    def department5(self):
        return self.__department5
    @department5.setter
    def department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__department5", None)
        self.__department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student4"):
                opp_val = getattr(old_value, "student4", None)
                if opp_val == self:
                    setattr(old_value, "student4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student4"):
                opp_val = getattr(value, "student4", None)
                setattr(value, "student4", self)



class AcademicResult:

    def __init__(self, semester: int):
        self.semester = semester
        
        pass
    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester



class Department:

    def __init__(self, name: str, course: Course, facultyInfo1: "FacultyInfo" = None, course2: "Course" = None, student4: "Student" = None):
        self.name = name
        self.course = course
        self.facultyInfo1 = facultyInfo1
        self.course2 = course2
        self.student4 = student4
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def student4(self):
        return self.__student4
    @student4.setter
    def student4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student4", None)
        self.__student4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department5"):
                opp_val = getattr(old_value, "department5", None)
                if opp_val == self:
                    setattr(old_value, "department5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department5"):
                opp_val = getattr(value, "department5", None)
                setattr(value, "department5", self)

    @property
    def facultyInfo1(self):
        return self.__facultyInfo1
    @facultyInfo1.setter
    def facultyInfo1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__facultyInfo1", None)
        self.__facultyInfo1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department20"):
                opp_val = getattr(old_value, "department20", None)
                if opp_val == self:
                    setattr(old_value, "department20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department20"):
                opp_val = getattr(value, "department20", None)
                setattr(value, "department20", self)

    @property
    def course2(self):
        return self.__course2
    @course2.setter
    def course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course2", None)
        self.__course2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department3"):
                opp_val = getattr(old_value, "department3", None)
                if opp_val == self:
                    setattr(old_value, "department3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department3"):
                opp_val = getattr(value, "department3", None)
                setattr(value, "department3", self)



class FacultyInfo:

    def __init__(self, facultyID: str, facultyName: str, department: Department, department20: "Department" = None):
        self.facultyID = facultyID
        self.facultyName = facultyName
        self.department = department
        self.department20 = department20
        
        pass
    @property
    def facultyID(self):
        return self.__facultyID
    @facultyID.setter
    def facultyID(self, facultyID: str):
        self.__facultyID = facultyID

    @property
    def facultyName(self):
        return self.__facultyName
    @facultyName.setter
    def facultyName(self, facultyName: str):
        self.__facultyName = facultyName

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: Department):
        self.__department = department

    @property
    def department20(self):
        return self.__department20
    @department20.setter
    def department20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FacultyInfo__department20", None)
        self.__department20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facultyInfo1"):
                opp_val = getattr(old_value, "facultyInfo1", None)
                if opp_val == self:
                    setattr(old_value, "facultyInfo1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facultyInfo1"):
                opp_val = getattr(value, "facultyInfo1", None)
                setattr(value, "facultyInfo1", self)



class Portal:

    pass
