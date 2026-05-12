from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase2_UseCase:

    pass


class UseCase_UseCase:

    pass


class Administrator_Actor:

    pass


class Teacher_Actor:

    pass


class Package_UseCase:

    pass


class Package_getResult_UseCase:

    pass


class Student_Actor:

    pass





class ELibrary:

    pass


class Administrator:

    def __init__(self, name: str, administratorID: int, academicRecords17: "AcademicRecords" = None):
        self.name = name
        self.administratorID = administratorID
        self.academicRecords17 = academicRecords17
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def administratorID(self):
        return self.__administratorID
    @administratorID.setter
    def administratorID(self, administratorID: int):
        self.__administratorID = administratorID

    @property
    def academicRecords17(self):
        return self.__academicRecords17
    @academicRecords17.setter
    def academicRecords17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__academicRecords17", None)
        self.__academicRecords17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator16"):
                opp_val = getattr(old_value, "administrator16", None)
                if opp_val == self:
                    setattr(old_value, "administrator16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator16"):
                opp_val = getattr(value, "administrator16", None)
                setattr(value, "administrator16", self)



class Dues:

    def __init__(self, student: Student, amount: int, portal8: "Portal" = None):
        self.student = student
        self.amount = amount
        self.portal8 = portal8
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student):
        self.__student = student

    @property
    def portal8(self):
        return self.__portal8
    @portal8.setter
    def portal8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dues__portal8", None)
        self.__portal8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dues9"):
                opp_val = getattr(old_value, "dues9", None)
                if opp_val == self:
                    setattr(old_value, "dues9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dues9"):
                opp_val = getattr(value, "dues9", None)
                setattr(value, "dues9", self)



class Course:

    def __init__(self, courseName: str, subjectCode: str, department11: "Department" = None):
        self.courseName = courseName
        self.subjectCode = subjectCode
        self.department11 = department11
        
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

    def __init__(self, name: str, scholarNo: int, branch: Department, semester: int, department19: "Department" = None, academicRecords21: "AcademicRecords" = None):
        self.name = name
        self.scholarNo = scholarNo
        self.branch = branch
        self.semester = semester
        self.department19 = department19
        self.academicRecords21 = academicRecords21
        
        pass
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
    def scholarNo(self):
        return self.__scholarNo
    @scholarNo.setter
    def scholarNo(self, scholarNo: int):
        self.__scholarNo = scholarNo

    @property
    def department19(self):
        return self.__department19
    @department19.setter
    def department19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__department19", None)
        self.__department19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student18"):
                opp_val = getattr(old_value, "student18", None)
                if opp_val == self:
                    setattr(old_value, "student18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student18"):
                opp_val = getattr(value, "student18", None)
                setattr(value, "student18", self)

    @property
    def academicRecords21(self):
        return self.__academicRecords21
    @academicRecords21.setter
    def academicRecords21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__academicRecords21", None)
        self.__academicRecords21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student220"):
                opp_val = getattr(old_value, "student220", None)
                if opp_val == self:
                    setattr(old_value, "student220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student220"):
                opp_val = getattr(value, "student220", None)
                setattr(value, "student220", self)



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



class Attendance:

    def __init__(self, student: Student, course: Course, academicRecords4: "AcademicRecords" = None):
        self.student = student
        self.course = course
        self.academicRecords4 = academicRecords4
        
        pass
    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student):
        self.__student = student

    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def academicRecords4(self):
        return self.__academicRecords4
    @academicRecords4.setter
    def academicRecords4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__academicRecords4", None)
        self.__academicRecords4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance5"):
                opp_val = getattr(old_value, "attendance5", None)
                if opp_val == self:
                    setattr(old_value, "attendance5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance5"):
                opp_val = getattr(value, "attendance5", None)
                setattr(value, "attendance5", self)



class Department:

    def __init__(self, name: str, course: Course, course10: "Course" = None, facultyInfo13: "FacultyInfo" = None, student18: "Student" = None):
        self.name = name
        self.course = course
        self.course10 = course10
        self.facultyInfo13 = facultyInfo13
        self.student18 = student18
        
        pass
    @property
    def course(self):
        return self.__course
    @course.setter
    def course(self, course: Course):
        self.__course = course

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def student18(self):
        return self.__student18
    @student18.setter
    def student18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__student18", None)
        self.__student18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department19"):
                opp_val = getattr(old_value, "department19", None)
                if opp_val == self:
                    setattr(old_value, "department19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department19"):
                opp_val = getattr(value, "department19", None)
                setattr(value, "department19", self)

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

    @property
    def facultyInfo13(self):
        return self.__facultyInfo13
    @facultyInfo13.setter
    def facultyInfo13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__facultyInfo13", None)
        self.__facultyInfo13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department212"):
                opp_val = getattr(old_value, "department212", None)
                if opp_val == self:
                    setattr(old_value, "department212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department212"):
                opp_val = getattr(value, "department212", None)
                setattr(value, "department212", self)



class FacultyInfo:

    def __init__(self, facultyID: str, facultyName: str, department: Department, department212: "Department" = None):
        self.facultyID = facultyID
        self.facultyName = facultyName
        self.department = department
        self.department212 = department212
        
        pass
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
    def facultyID(self):
        return self.__facultyID
    @facultyID.setter
    def facultyID(self, facultyID: str):
        self.__facultyID = facultyID

    @property
    def department212(self):
        return self.__department212
    @department212.setter
    def department212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FacultyInfo__department212", None)
        self.__department212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "facultyInfo13"):
                opp_val = getattr(old_value, "facultyInfo13", None)
                if opp_val == self:
                    setattr(old_value, "facultyInfo13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "facultyInfo13"):
                opp_val = getattr(value, "facultyInfo13", None)
                setattr(value, "facultyInfo13", self)



class AcademicRecords:

    def __init__(self, student: Student, attendance: Attendance, result: AcademicResult, dues: int, portal3: "Portal" = None, administrator16: "Administrator" = None, student220: "Student" = None, attendance5: "Attendance" = None, academicResult6: "AcademicResult" = None):
        self.student = student
        self.attendance = attendance
        self.result = result
        self.dues = dues
        self.portal3 = portal3
        self.administrator16 = administrator16
        self.student220 = student220
        self.attendance5 = attendance5
        self.academicResult6 = academicResult6
        
        pass
    @property
    def student(self):
        return self.__student
    @student.setter
    def student(self, student: Student):
        self.__student = student

    @property
    def result(self):
        return self.__result
    @result.setter
    def result(self, result: AcademicResult):
        self.__result = result

    @property
    def dues(self):
        return self.__dues
    @dues.setter
    def dues(self, dues: int):
        self.__dues = dues

    @property
    def attendance(self):
        return self.__attendance
    @attendance.setter
    def attendance(self, attendance: Attendance):
        self.__attendance = attendance

    @property
    def student220(self):
        return self.__student220
    @student220.setter
    def student220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__student220", None)
        self.__student220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords21"):
                opp_val = getattr(old_value, "academicRecords21", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords21"):
                opp_val = getattr(value, "academicRecords21", None)
                setattr(value, "academicRecords21", self)

    @property
    def portal3(self):
        return self.__portal3
    @portal3.setter
    def portal3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__portal3", None)
        self.__portal3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords2"):
                opp_val = getattr(old_value, "academicRecords2", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords2"):
                opp_val = getattr(value, "academicRecords2", None)
                setattr(value, "academicRecords2", self)

    @property
    def attendance5(self):
        return self.__attendance5
    @attendance5.setter
    def attendance5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__attendance5", None)
        self.__attendance5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords4"):
                opp_val = getattr(old_value, "academicRecords4", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords4"):
                opp_val = getattr(value, "academicRecords4", None)
                setattr(value, "academicRecords4", self)

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

    @property
    def administrator16(self):
        return self.__administrator16
    @administrator16.setter
    def administrator16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AcademicRecords__administrator16", None)
        self.__administrator16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "academicRecords17"):
                opp_val = getattr(old_value, "academicRecords17", None)
                if opp_val == self:
                    setattr(old_value, "academicRecords17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "academicRecords17"):
                opp_val = getattr(value, "academicRecords17", None)
                setattr(value, "academicRecords17", self)



class Portal:

    pass


class StudentPortal:

    pass
