from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Administrator:

    def __init__(self, name: str, administratorID: int, academicRecords3: "AcademicRecords" = None):
        self.name = name
        self.administratorID = administratorID
        self.academicRecords3 = academicRecords3
        
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

    @property
    def academicRecords3(self):
        return self.__academicRecords3
    @academicRecords3.setter
    def academicRecords3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__academicRecords3", None)
        self.__academicRecords3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator2"):
                opp_val = getattr(old_value, "administrator2", None)
                if opp_val == self:
                    setattr(old_value, "administrator2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator2"):
                opp_val = getattr(value, "administrator2", None)
                setattr(value, "administrator2", self)



class Course:

    def __init__(self, courseName: str, subjectCode: str, department11: "Department" = None):
        self.courseName = courseName
        self.subjectCode = subjectCode
        self.department11 = department11
        
        pass
    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: str):
        self.__subjectCode = subjectCode

    @property
    def department11(self):
        return self.__department11
    @department11.setter
    def department11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__department11", None)
        self.__department11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course10"):
                opp_val = getattr(old_value, "course10", None)
                if opp_val == self:
                    setattr(old_value, "course10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course10"):
                opp_val = getattr(value, "course10", None)
                setattr(value, "course10", self)



class Student:

    def __init__(self, name: str, scholarNo: int, branch: Department, semester: int, academicRecords5: "AcademicRecords" = None, department13: "Department" = None):
        self.name = name
        self.scholarNo = scholarNo
        self.branch = branch
        self.semester = semester
        self.academicRecords5 = academicRecords5
        self.department13 = department13
        
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
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department13(self):
        return self.__department13
    @department13.setter
    def department13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__department13", None)
        self.__department13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student12"):
                opp_val = getattr(old_value, "student12", None)
                if opp_val == self:
                    setattr(old_value, "student12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student12"):
                opp_val = getattr(value, "student12", None)
                setattr(value, "student12", self)

    @property
    def academicRecords5(self):
        return self.__academicRecords5
    @academicRecords5.setter
    def academicRecords5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__academicRecords5", None)
        self.__academicRecords5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student24"):
                opp_val = getattr(old_value, "student24", None)
                if opp_val == self:
                    setattr(old_value, "student24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student24"):
                opp_val = getattr(value, "student24", None)
                setattr(value, "student24", self)



class AcademicResult:

    def __init__(self, semester: int, academicRecords7: "AcademicRecords" = None):
        self.semester = semester
        self.academicRecords7 = academicRecords7
        
        pass
    @property
    def semester(self):
        return self.__semester
    @semester.setter
    def semester(self, semester: int):
        self.__semester = semester

    @property
    def academicRecords7(self):
        return self.__academicRecords7
    @academicRecords7.setter
    def academicRecords7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicResult__academicRecords7", None)
        self.__academicRecords7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicResult6"):
                opp_val = getattr(old_value, "academicResult6", None)
                if opp_val == self:
                    setattr(old_value, "academicResult6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicResult6"):
                opp_val = getattr(value, "academicResult6", None)
                setattr(value, "academicResult6", self)



class Department:

    def __init__(self, name: str, course: Course, facultyInfo9: "FacultyInfo" = None, course10: "Course" = None, student12: "Student" = None):
        self.name = name
        self.course = course
        self.facultyInfo9 = facultyInfo9
        self.course10 = course10
        self.student12 = student12
        
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
    def student12(self):
        return self.__student12
    @student12.setter
    def student12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student12", None)
        self.__student12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department13"):
                opp_val = getattr(old_value, "department13", None)
                if opp_val == self:
                    setattr(old_value, "department13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department13"):
                opp_val = getattr(value, "department13", None)
                setattr(value, "department13", self)

    @property
    def facultyInfo9(self):
        return self.__facultyInfo9
    @facultyInfo9.setter
    def facultyInfo9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__facultyInfo9", None)
        self.__facultyInfo9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department28"):
                opp_val = getattr(old_value, "department28", None)
                if opp_val == self:
                    setattr(old_value, "department28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department28"):
                opp_val = getattr(value, "department28", None)
                setattr(value, "department28", self)

    @property
    def course10(self):
        return self.__course10
    @course10.setter
    def course10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course10", None)
        self.__course10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department11"):
                opp_val = getattr(old_value, "department11", None)
                if opp_val == self:
                    setattr(old_value, "department11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department11"):
                opp_val = getattr(value, "department11", None)
                setattr(value, "department11", self)



class FacultyInfo:

    def __init__(self, facultyID: str, facultyName: str, department: Department, department28: "Department" = None):
        self.facultyID = facultyID
        self.facultyName = facultyName
        self.department = department
        self.department28 = department28
        
        pass
    @property
    def facultyName(self):
        return self.__facultyName
    @facultyName.setter
    def facultyName(self, facultyName: str):
        self.__facultyName = facultyName

    @property
    def facultyID(self):
        return self.__facultyID
    @facultyID.setter
    def facultyID(self, facultyID: str):
        self.__facultyID = facultyID

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: Department):
        self.__department = department

    @property
    def department28(self):
        return self.__department28
    @department28.setter
    def department28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FacultyInfo__department28", None)
        self.__department28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facultyInfo9"):
                opp_val = getattr(old_value, "facultyInfo9", None)
                if opp_val == self:
                    setattr(old_value, "facultyInfo9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facultyInfo9"):
                opp_val = getattr(value, "facultyInfo9", None)
                setattr(value, "facultyInfo9", self)



class AcademicRecords:

    def __init__(self, student: Student, attendance: str, result: AcademicResult, dues: int, portal1: "Portal" = None, administrator2: "Administrator" = None, student24: "Student" = None, academicResult6: "AcademicResult" = None):
        self.student = student
        self.attendance = attendance
        self.result = result
        self.dues = dues
        self.portal1 = portal1
        self.administrator2 = administrator2
        self.student24 = student24
        self.academicResult6 = academicResult6
        
        pass
    @property
    def result(self):
        return self.__result
    @result.setter
    def result(self, result: AcademicResult):
        self.__result = result

    @property
    def attendance(self):
        return self.__attendance
    @attendance.setter
    def attendance(self, attendance: str):
        self.__attendance = attendance

    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student):
        self.__student = student

    @property
    def dues(self):
        return self.__dues
    @dues.setter
    def dues(self, dues: int):
        self.__dues = dues

    @property
    def administrator2(self):
        return self.__administrator2
    @administrator2.setter
    def administrator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__administrator2", None)
        self.__administrator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords3"):
                opp_val = getattr(old_value, "academicRecords3", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords3"):
                opp_val = getattr(value, "academicRecords3", None)
                setattr(value, "academicRecords3", self)

    @property
    def portal1(self):
        return self.__portal1
    @portal1.setter
    def portal1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__portal1", None)
        self.__portal1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords0"):
                opp_val = getattr(old_value, "academicRecords0", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords0"):
                opp_val = getattr(value, "academicRecords0", None)
                setattr(value, "academicRecords0", self)

    @property
    def student24(self):
        return self.__student24
    @student24.setter
    def student24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__student24", None)
        self.__student24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords5"):
                opp_val = getattr(old_value, "academicRecords5", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords5"):
                opp_val = getattr(value, "academicRecords5", None)
                setattr(value, "academicRecords5", self)

    @property
    def academicResult6(self):
        return self.__academicResult6
    @academicResult6.setter
    def academicResult6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__academicResult6", None)
        self.__academicResult6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords7"):
                opp_val = getattr(old_value, "academicRecords7", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords7"):
                opp_val = getattr(value, "academicRecords7", None)
                setattr(value, "academicRecords7", self)



class Portal:

    pass
