from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class delete_UseCase:

    pass


class registerCourse_UseCase:

    pass


class add_UseCase:

    pass


class publishCalender___UseCase:

    pass


class modifyCalender4_UseCase:

    pass


class providedCourse___UseCase:

    pass


class course_Actor:

    pass


class organisation_Actor:

    pass


class user_Actor:

    pass


class courseCalendar_Actor:

    pass


class student_Actor:

    pass


class admin_Actor:

    pass


class searchCourse_UseCase:

    pass


class viewCourse_UseCase:

    pass





class CourseCalendar:

    def __init__(self, startTime: int, endTime: int, courses5: "Courses" = None):
        self.startTime = startTime
        self.endTime = endTime
        self.courses5 = courses5
        
        pass
    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: int):
        self.__startTime = startTime

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: int):
        self.__endTime = endTime

    @property
    def courses5(self):
        return self.__courses5
    @courses5.setter
    def courses5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CourseCalendar__courses5", None)
        self.__courses5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseCalendar4"):
                opp_val = getattr(old_value, "courseCalendar4", None)
                if opp_val == self:
                    setattr(old_value, "courseCalendar4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseCalendar4"):
                opp_val = getattr(value, "courseCalendar4", None)
                setattr(value, "courseCalendar4", self)



class Courses:

    def __init__(self, courseName: str, courseId: int, coursecode: int, credithour: int, _attr: str, student1: set["student"] = None, student2: set["Student"] = None, courseCalendar4: "CourseCalendar" = None, teacher7: set["teacher"] = None):
        self.courseName = courseName
        self.courseId = courseId
        self.coursecode = coursecode
        self.credithour = credithour
        self._attr = _attr
        self.student1 = student1 if student1 is not None else set()
        self.student2 = student2 if student2 is not None else set()
        self.courseCalendar4 = courseCalendar4
        self.teacher7 = teacher7 if teacher7 is not None else set()
        
        pass
    @property
    def coursecode(self):
        return self.__coursecode
    @coursecode.setter
    def coursecode(self, coursecode: int):
        self.__coursecode = coursecode

    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def credithour(self):
        return self.__credithour
    @credithour.setter
    def credithour(self, credithour: int):
        self.__credithour = credithour

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId

    @property
    def student2(self):
        return self.__student2
    @student2.setter
    def student2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses__student2", None)
        self.__student2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses3"):
                    opp_val = getattr(item, "courses3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses3"):
                    opp_val = getattr(item, "courses3", None)
                    
                    if opp_val is None:
                        setattr(item, "courses3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student1(self):
        return self.__student1
    @student1.setter
    def student1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses__student1", None)
        self.__student1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "courses0"):
                    opp_val = getattr(item, "courses0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "courses0"):
                    opp_val = getattr(item, "courses0", None)
                    
                    if opp_val is None:
                        setattr(item, "courses0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def teacher7(self):
        return self.__teacher7
    @teacher7.setter
    def teacher7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses__teacher7", None)
        self.__teacher7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "teacher_Courses_06"):
                    opp_val = getattr(item, "teacher_Courses_06", None)
                    
                    if opp_val == self:
                        setattr(item, "teacher_Courses_06", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "teacher_Courses_06"):
                    opp_val = getattr(item, "teacher_Courses_06", None)
                    
                    setattr(item, "teacher_Courses_06", self)
                    

    @property
    def courseCalendar4(self):
        return self.__courseCalendar4
    @courseCalendar4.setter
    def courseCalendar4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses__courseCalendar4", None)
        self.__courseCalendar4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses5"):
                opp_val = getattr(old_value, "courses5", None)
                if opp_val == self:
                    setattr(old_value, "courses5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses5"):
                opp_val = getattr(value, "courses5", None)
                setattr(value, "courses5", self)



class Student:

    def __init__(self, courseName: str, courseId: int, courses3: set["Courses"] = None):
        self.courseName = courseName
        self.courseId = courseId
        self.courses3 = courses3 if courses3 is not None else set()
        
        pass
    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId

    @property
    def courses3(self):
        return self.__courses3
    @courses3.setter
    def courses3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Student__courses3", None)
        self.__courses3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student2"):
                    opp_val = getattr(item, "student2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student2"):
                    opp_val = getattr(item, "student2", None)
                    
                    if opp_val is None:
                        setattr(item, "student2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class student:

    def __init__(self, managestudent: str, result: str, _attr: str, attribute: str, _attr1: str, e: str, timetable9: set["timetable"] = None, quiz11: set["Quiz"] = None, assignment12: set["Assignment"] = None, events14: set["Events"] = None, attendance16: set["attendance"] = None, result18: set["result"] = None, chatbox20: set["chatbox"] = None, dropbox22: set["dropbox"] = None, courses0: set["Courses"] = None):
        self.managestudent = managestudent
        self.result = result
        self._attr = _attr
        self.attribute = attribute
        self._attr1 = _attr1
        self.e = e
        self.timetable9 = timetable9 if timetable9 is not None else set()
        self.quiz11 = quiz11 if quiz11 is not None else set()
        self.assignment12 = assignment12 if assignment12 is not None else set()
        self.events14 = events14 if events14 is not None else set()
        self.attendance16 = attendance16 if attendance16 is not None else set()
        self.result18 = result18 if result18 is not None else set()
        self.chatbox20 = chatbox20 if chatbox20 is not None else set()
        self.dropbox22 = dropbox22 if dropbox22 is not None else set()
        self.courses0 = courses0 if courses0 is not None else set()
        
        pass
    @property
    def result(self):
        return self.__result
    @result.setter
    def result(self, result: str):
        self.__result = result

    @property
    def e(self):
        return self.__e
    @e.setter
    def e(self, e: str):
        self.__e = e

    @property
    def _attr1(self):
        return self.___attr1
    @_attr1.setter
    def _attr1(self, _attr1: str):
        self.___attr1 = _attr1

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def managestudent(self):
        return self.__managestudent
    @managestudent.setter
    def managestudent(self, managestudent: str):
        self.__managestudent = managestudent

    @property
    def courses0(self):
        return self.__courses0
    @courses0.setter
    def courses0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__courses0", None)
        self.__courses0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student1"):
                    opp_val = getattr(item, "student1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student1"):
                    opp_val = getattr(item, "student1", None)
                    
                    if opp_val is None:
                        setattr(item, "student1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def assignment12(self):
        return self.__assignment12
    @assignment12.setter
    def assignment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__assignment12", None)
        self.__assignment12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student13"):
                    opp_val = getattr(item, "student13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student13"):
                    opp_val = getattr(item, "student13", None)
                    
                    if opp_val is None:
                        setattr(item, "student13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def chatbox20(self):
        return self.__chatbox20
    @chatbox20.setter
    def chatbox20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__chatbox20", None)
        self.__chatbox20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "teacher21"):
                    opp_val = getattr(item, "teacher21", None)
                    
                    if opp_val == self:
                        setattr(item, "teacher21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "teacher21"):
                    opp_val = getattr(item, "teacher21", None)
                    
                    setattr(item, "teacher21", self)
                    

    @property
    def attendance16(self):
        return self.__attendance16
    @attendance16.setter
    def attendance16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__attendance16", None)
        self.__attendance16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Teacher_attendance_117"):
                    opp_val = getattr(item, "Teacher_attendance_117", None)
                    
                    if opp_val == self:
                        setattr(item, "Teacher_attendance_117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Teacher_attendance_117"):
                    opp_val = getattr(item, "Teacher_attendance_117", None)
                    
                    setattr(item, "Teacher_attendance_117", self)
                    

    @property
    def quiz11(self):
        return self.__quiz11
    @quiz11.setter
    def quiz11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__quiz11", None)
        self.__quiz11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student10"):
                    opp_val = getattr(item, "student10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student10"):
                    opp_val = getattr(item, "student10", None)
                    
                    if opp_val is None:
                        setattr(item, "student10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def events14(self):
        return self.__events14
    @events14.setter
    def events14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__events14", None)
        self.__events14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student15"):
                    opp_val = getattr(item, "student15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student15"):
                    opp_val = getattr(item, "student15", None)
                    
                    if opp_val is None:
                        setattr(item, "student15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def timetable9(self):
        return self.__timetable9
    @timetable9.setter
    def timetable9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__timetable9", None)
        self.__timetable9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student8"):
                    opp_val = getattr(item, "student8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student8"):
                    opp_val = getattr(item, "student8", None)
                    
                    if opp_val is None:
                        setattr(item, "student8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def dropbox22(self):
        return self.__dropbox22
    @dropbox22.setter
    def dropbox22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__dropbox22", None)
        self.__dropbox22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student23"):
                    opp_val = getattr(item, "student23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student23"):
                    opp_val = getattr(item, "student23", None)
                    
                    if opp_val is None:
                        setattr(item, "student23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def result18(self):
        return self.__result18
    @result18.setter
    def result18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__result18", None)
        self.__result18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "teacher19"):
                    opp_val = getattr(item, "teacher19", None)
                    
                    if opp_val == self:
                        setattr(item, "teacher19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "teacher19"):
                    opp_val = getattr(item, "teacher19", None)
                    
                    setattr(item, "teacher19", self)
                    



class User:

    def __init__(self, id: int, name: str, address: str, email: str, phnNo: int):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.phnNo = phnNo
        
        pass
    @property
    def phnNo(self):
        return self.__phnNo
    @phnNo.setter
    def phnNo(self, phnNo: int):
        self.__phnNo = phnNo

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address



class dropbox:

    def __init__(self, filetype: str, file: str, date: int, class1: int, _attr: str, _attr1: int, program: str, department: str, session: int, section: str, student23: set["student"] = None):
        self.filetype = filetype
        self.file = file
        self.date = date
        self.class1 = class1
        self._attr = _attr
        self._attr1 = _attr1
        self.program = program
        self.department = department
        self.session = session
        self.section = section
        self.student23 = student23 if student23 is not None else set()
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: int):
        self.__class1 = class1

    @property
    def session(self):
        return self.__session
    @session.setter
    def session(self, session: int):
        self.__session = session

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def filetype(self):
        return self.__filetype
    @filetype.setter
    def filetype(self, filetype: str):
        self.__filetype = filetype

    @property
    def program(self):
        return self.__program
    @program.setter
    def program(self, program: str):
        self.__program = program

    @property
    def _attr1(self):
        return self.___attr1
    @_attr1.setter
    def _attr1(self, _attr1: int):
        self.___attr1 = _attr1

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def student23(self):
        return self.__student23
    @student23.setter
    def student23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dropbox__student23", None)
        self.__student23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dropbox22"):
                    opp_val = getattr(item, "dropbox22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dropbox22"):
                    opp_val = getattr(item, "dropbox22", None)
                    
                    if opp_val is None:
                        setattr(item, "dropbox22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class chatbox:

    def __init__(self, class1: str, messagetype: int, messagetitle: str, messagedcription: int, _attr: str, teacher21: "student" = None):
        self.class1 = class1
        self.messagetype = messagetype
        self.messagetitle = messagetitle
        self.messagedcription = messagedcription
        self._attr = _attr
        self.teacher21 = teacher21
        
        pass
    @property
    def messagetype(self):
        return self.__messagetype
    @messagetype.setter
    def messagetype(self, messagetype: int):
        self.__messagetype = messagetype

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class = class1

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def messagetitle(self):
        return self.__messagetitle
    @messagetitle.setter
    def messagetitle(self, messagetitle: str):
        self.__messagetitle = messagetitle

    @property
    def messagedcription(self):
        return self.__messagedcription
    @messagedcription.setter
    def messagedcription(self, messagedcription: int):
        self.__messagedcription = messagedcription

    @property
    def teacher21(self):
        return self.__teacher21
    @teacher21.setter
    def teacher21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chatbox__teacher21", None)
        self.__teacher21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chatbox20"):
                opp_val = getattr(old_value, "chatbox20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chatbox20"):
                opp_val = getattr(value, "chatbox20", None)
                if opp_val is None:
                    setattr(value, "chatbox20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class result:

    def __init__(self, class1: str, midmarks: int, finalmarks: int, practical: int, _attr: str, sessional: int, subject: str, totalmarks: int, class2: str, attribute: str, obtainedmarks: int, teacher19: "student" = None):
        self.class1 = class1
        self.midmarks = midmarks
        self.finalmarks = finalmarks
        self.practical = practical
        self._attr = _attr
        self.sessional = sessional
        self.subject = subject
        self.totalmarks = totalmarks
        self.class2 = class2
        self.attribute = attribute
        self.obtainedmarks = obtainedmarks
        self.teacher19 = teacher19
        
        pass
    @property
    def practical(self):
        return self.__practical
    @practical.setter
    def practical(self, practical: int):
        self.__practical = practical

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class1 = class1

    @property
    def totalmarks(self):
        return self.__totalmarks
    @totalmarks.setter
    def totalmarks(self, totalmarks: int):
        self.__totalmarks = totalmarks

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def obtainedmarks(self):
        return self.__obtainedmarks
    @obtainedmarks.setter
    def obtainedmarks(self, obtainedmarks: int):
        self.__obtainedmarks = obtainedmarks

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def finalmarks(self):
        return self.__finalmarks
    @finalmarks.setter
    def finalmarks(self, finalmarks: int):
        self.__finalmarks = finalmarks

    @property
    def midmarks(self):
        return self.__midmarks
    @midmarks.setter
    def midmarks(self, midmarks: int):
        self.__midmarks = midmarks

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def sessional(self):
        return self.__sessional
    @sessional.setter
    def sessional(self, sessional: int):
        self.__sessional = sessional

    @property
    def class2(self):
        return self.__class2
    @class2.setter
    def class1(self, class2: str):
        self.__class2 = class2

    @property
    def teacher19(self):
        return self.__teacher19
    @teacher19.setter
    def teacher19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_result__teacher19", None)
        self.__teacher19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "result18"):
                opp_val = getattr(old_value, "result18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "result18"):
                opp_val = getattr(value, "result18", None)
                if opp_val is None:
                    setattr(value, "result18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class attendance:

    def __init__(self, class1: str, present: str, absent: str, leave: str, _attr: str, lecture: int, day: str, date: int, class1: str, attribute: str, Teacher_attendance_117: "student" = None):
        self.class1 = class1
        self.present = present
        self.absent = absent
        self.leave = leave
        self._attr = _attr
        self.lecture = lecture
        self.day = day
        self.date = date
        self.class1 = class1
        self.attribute = attribute
        self.Teacher_attendance_117 = Teacher_attendance_117
        
        pass
    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class = class1

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: str):
        self.__class1 = class1

    @property
    def present(self):
        return self.__present
    @present.setter
    def present(self, present: str):
        self.__present = present

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def absent(self):
        return self.__absent
    @absent.setter
    def absent(self, absent: str):
        self.__absent = absent

    @property
    def leave(self):
        return self.__leave
    @leave.setter
    def leave(self, leave: str):
        self.__leave = leave

    @property
    def lecture(self):
        return self.__lecture
    @lecture.setter
    def lecture(self, lecture: int):
        self.__lecture = lecture

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def Teacher_attendance_117(self):
        return self.__Teacher_attendance_117
    @Teacher_attendance_117.setter
    def Teacher_attendance_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attendance__Teacher_attendance_117", None)
        self.__Teacher_attendance_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance16"):
                opp_val = getattr(old_value, "attendance16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance16"):
                opp_val = getattr(value, "attendance16", None)
                if opp_val is None:
                    setattr(value, "attendance16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Events:

    def __init__(self, Evantname: str, eventId: int, eventtitle: int, eventdescription: int, _attr: str, student15: set["student"] = None):
        self.Evantname = Evantname
        self.eventId = eventId
        self.eventtitle = eventtitle
        self.eventdescription = eventdescription
        self._attr = _attr
        self.student15 = student15 if student15 is not None else set()
        
        pass
    @property
    def eventdescription(self):
        return self.__eventdescription
    @eventdescription.setter
    def eventdescription(self, eventdescription: int):
        self.__eventdescription = eventdescription

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def eventId(self):
        return self.__eventId
    @eventId.setter
    def eventId(self, eventId: int):
        self.__eventId = eventId

    @property
    def eventtitle(self):
        return self.__eventtitle
    @eventtitle.setter
    def eventtitle(self, eventtitle: int):
        self.__eventtitle = eventtitle

    @property
    def Evantname(self):
        return self.__Evantname
    @Evantname.setter
    def Evantname(self, Evantname: str):
        self.__Evantname = Evantname

    @property
    def student15(self):
        return self.__student15
    @student15.setter
    def student15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Events__student15", None)
        self.__student15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "events14"):
                    opp_val = getattr(item, "events14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "events14"):
                    opp_val = getattr(item, "events14", None)
                    
                    if opp_val is None:
                        setattr(item, "events14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Assignment:

    def __init__(self, assignmenttitle: str, assignmentfile: str, duedate: int, class1: int, _attr: str, _attr1: int, program: str, department: str, session: int, section: str, student13: set["student"] = None):
        self.assignmenttitle = assignmenttitle
        self.assignmentfile = assignmentfile
        self.duedate = duedate
        self.class1 = class1
        self._attr = _attr
        self._attr1 = _attr1
        self.program = program
        self.department = department
        self.session = session
        self.section = section
        self.student13 = student13 if student13 is not None else set()
        
        pass
    @property
    def assignmentfile(self):
        return self.__assignmentfile
    @assignmentfile.setter
    def assignmentfile(self, assignmentfile: str):
        self.__assignmentfile = assignmentfile

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def program(self):
        return self.__program
    @program.setter
    def program(self, program: str):
        self.__program = program

    @property
    def session(self):
        return self.__session
    @session.setter
    def session(self, session: int):
        self.__session = session

    @property
    def class1(self):
        return self.__class1
    @class1.setter
    def class1(self, class1: int):
        self.__class1 = class1

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def _attr1(self):
        return self.___attr1
    @_attr1.setter
    def _attr1(self, _attr1: int):
        self.___attr1 = _attr1

    @property
    def assignmenttitle(self):
        return self.__assignmenttitle
    @assignmenttitle.setter
    def assignmenttitle(self, assignmenttitle: str):
        self.__assignmenttitle = assignmenttitle

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def duedate(self):
        return self.__duedate
    @duedate.setter
    def duedate(self, duedate: int):
        self.__duedate = duedate

    @property
    def student13(self):
        return self.__student13
    @student13.setter
    def student13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assignment__student13", None)
        self.__student13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment12"):
                    opp_val = getattr(item, "assignment12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment12"):
                    opp_val = getattr(item, "assignment12", None)
                    
                    if opp_val is None:
                        setattr(item, "assignment12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Quiz:

    def __init__(self, quiztitle: str, quizfile: str, subject: str, timeduration: int, _attr: str, scale: int, date: int, department: str, student10: set["student"] = None):
        self.quiztitle = quiztitle
        self.quizfile = quizfile
        self.subject = subject
        self.timeduration = timeduration
        self._attr = _attr
        self.scale = scale
        self.date = date
        self.department = department
        self.student10 = student10 if student10 is not None else set()
        
        pass
    @property
    def scale(self):
        return self.__scale
    @scale.setter
    def scale(self, scale: int):
        self.__scale = scale

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def quiztitle(self):
        return self.__quiztitle
    @quiztitle.setter
    def quiztitle(self, quiztitle: str):
        self.__quiztitle = quiztitle

    @property
    def quizfile(self):
        return self.__quizfile
    @quizfile.setter
    def quizfile(self, quizfile: str):
        self.__quizfile = quizfile

    @property
    def timeduration(self):
        return self.__timeduration
    @timeduration.setter
    def timeduration(self, timeduration: int):
        self.__timeduration = timeduration

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def student10(self):
        return self.__student10
    @student10.setter
    def student10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Quiz__student10", None)
        self.__student10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "quiz11"):
                    opp_val = getattr(item, "quiz11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "quiz11"):
                    opp_val = getattr(item, "quiz11", None)
                    
                    if opp_val is None:
                        setattr(item, "quiz11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class timetable:

    def __init__(self, courseName: str, courseId: int, coursecode: int, credithour: int, _attr: str, lectime: int, day: str, date: int, teacher: str, student8: set["student"] = None):
        self.courseName = courseName
        self.courseId = courseId
        self.coursecode = coursecode
        self.credithour = credithour
        self._attr = _attr
        self.lectime = lectime
        self.day = day
        self.date = date
        self.teacher = teacher
        self.student8 = student8 if student8 is not None else set()
        
        pass
    @property
    def credithour(self):
        return self.__credithour
    @credithour.setter
    def credithour(self, credithour: int):
        self.__credithour = credithour

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def lectime(self):
        return self.__lectime
    @lectime.setter
    def lectime(self, lectime: int):
        self.__lectime = lectime

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId

    @property
    def teacher(self):
        return self.__teacher
    @teacher.setter
    def teacher(self, teacher: str):
        self.__teacher = teacher

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def coursecode(self):
        return self.__coursecode
    @coursecode.setter
    def coursecode(self, coursecode: int):
        self.__coursecode = coursecode

    @property
    def student8(self):
        return self.__student8
    @student8.setter
    def student8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_timetable__student8", None)
        self.__student8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "timetable9"):
                    opp_val = getattr(item, "timetable9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "timetable9"):
                    opp_val = getattr(item, "timetable9", None)
                    
                    if opp_val is None:
                        setattr(item, "timetable9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class teacher:

    pass


class Student4:

    def __init__(self, courseName: str, courseId: int):
        self.courseName = courseName
        self.courseId = courseId
        
        pass
    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId



class Student3:

    def __init__(self, courseName: str, courseId: int):
        self.courseName = courseName
        self.courseId = courseId
        
        pass
    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId



class Student2:

    def __init__(self, courseName: str, courseId: int):
        self.courseName = courseName
        self.courseId = courseId
        
        pass
    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId

    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName



class Teacher:

    def __init__(self, courseName: str, courseId: int):
        self.courseName = courseName
        self.courseId = courseId
        
        pass
    @property
    def courseName(self):
        return self.__courseName
    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def courseId(self):
        return self.__courseId
    @courseId.setter
    def courseId(self, courseId: int):
        self.__courseId = courseId

