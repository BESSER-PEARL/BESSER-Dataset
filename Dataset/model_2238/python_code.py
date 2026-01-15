from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DayOfWeek(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
class TypeOfInstruction(Enum):
    Lab = "Lab"
    Lecture = "Lecture"


############################################
# Definition of Classes
############################################

class course_TimetableEntry:

    def __init__(self, day: str, room: str, time: str, type: str, course_TimetableEntry: "course_Timetable" = None, course_TimetableEntry47: set["course_StudyProgram"] = None):
        self.day = day
        self.room = room
        self.time = time
        self.type = type
        self.course_TimetableEntry = course_TimetableEntry
        self.course_TimetableEntry47 = course_TimetableEntry47 if course_TimetableEntry47 is not None else set()
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def room(self) -> str:
        return self.__room

    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def course_TimetableEntry(self):
        return self.__course_TimetableEntry

    @course_TimetableEntry.setter
    def course_TimetableEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_TimetableEntry__course_TimetableEntry", None)
        self.__course_TimetableEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_Timetable"):
                opp_val = getattr(old_value, "course_Timetable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_Timetable"):
                opp_val = getattr(value, "course_Timetable", None)
                if opp_val is None:
                    setattr(value, "course_Timetable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course_TimetableEntry47(self):
        return self.__course_TimetableEntry47

    @course_TimetableEntry47.setter
    def course_TimetableEntry47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_TimetableEntry__course_TimetableEntry47", None)
        self.__course_TimetableEntry47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_StudyProgram48"):
                    opp_val = getattr(item, "course_StudyProgram48", None)
                    
                    if opp_val == self:
                        setattr(item, "course_StudyProgram48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_StudyProgram48"):
                    opp_val = getattr(item, "course_StudyProgram48", None)
                    
                    setattr(item, "course_StudyProgram48", self)
                    

class Person:

    pass
class course_Person:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class course_Timetable:

    pass
class course_CourseWork:

    def __init__(self, lectureHours: int, labHours: int, CourseWork: "course_CourseInstance" = None, courseWork: "course_CourseInstance" = None):
        self.lectureHours = lectureHours
        self.labHours = labHours
        self.CourseWork = CourseWork
        self.courseWork = courseWork
        
    @property
    def labHours(self) -> int:
        return self.__labHours

    @labHours.setter
    def labHours(self, labHours: int):
        self.__labHours = labHours

    @property
    def lectureHours(self) -> int:
        return self.__lectureHours

    @lectureHours.setter
    def lectureHours(self, lectureHours: int):
        self.__lectureHours = lectureHours

    @property
    def CourseWork(self):
        return self.__CourseWork

    @CourseWork.setter
    def CourseWork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_CourseWork__CourseWork", None)
        self.__CourseWork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstance18"):
                opp_val = getattr(old_value, "courseInstance18", None)
                if opp_val == self:
                    setattr(old_value, "courseInstance18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstance18"):
                opp_val = getattr(value, "courseInstance18", None)
                setattr(value, "courseInstance18", self)

    @property
    def courseWork(self):
        return self.__courseWork

    @courseWork.setter
    def courseWork(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_CourseWork__courseWork", None)
        self.__courseWork = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance42"):
                opp_val = getattr(old_value, "CourseInstance42", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance42"):
                opp_val = getattr(value, "CourseInstance42", None)
                setattr(value, "CourseInstance42", self)

class course_Evaluation:

    def __init__(self, project: int, assigments: int, exam: int, evaluation: "course_CourseInstance" = None, evaluation30: set["course_Student"] = None, Evaluation: "course_CourseInstance" = None, Evaluation51: "course_Student" = None):
        self.project = project
        self.assigments = assigments
        self.exam = exam
        self.evaluation = evaluation
        self.evaluation30 = evaluation30 if evaluation30 is not None else set()
        self.Evaluation = Evaluation
        self.Evaluation51 = Evaluation51
        
    @property
    def project(self) -> int:
        return self.__project

    @project.setter
    def project(self, project: int):
        self.__project = project

    @property
    def exam(self) -> int:
        return self.__exam

    @exam.setter
    def exam(self, exam: int):
        self.__exam = exam

    @property
    def assigments(self) -> int:
        return self.__assigments

    @assigments.setter
    def assigments(self, assigments: int):
        self.__assigments = assigments

    @property
    def Evaluation(self):
        return self.__Evaluation

    @Evaluation.setter
    def Evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Evaluation__Evaluation", None)
        self.__Evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstance16"):
                opp_val = getattr(old_value, "courseInstance16", None)
                if opp_val == self:
                    setattr(old_value, "courseInstance16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstance16"):
                opp_val = getattr(value, "courseInstance16", None)
                setattr(value, "courseInstance16", self)

    @property
    def Evaluation51(self):
        return self.__Evaluation51

    @Evaluation51.setter
    def Evaluation51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Evaluation__Evaluation51", None)
        self.__Evaluation51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registeredStudents"):
                opp_val = getattr(old_value, "registeredStudents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registeredStudents"):
                opp_val = getattr(value, "registeredStudents", None)
                if opp_val is None:
                    setattr(value, "registeredStudents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def evaluation30(self):
        return self.__evaluation30

    @evaluation30.setter
    def evaluation30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Evaluation__evaluation30", None)
        self.__evaluation30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    if opp_val == self:
                        setattr(item, "Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    setattr(item, "Student", self)
                    

    @property
    def evaluation(self):
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Evaluation__evaluation", None)
        self.__evaluation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance28"):
                opp_val = getattr(old_value, "CourseInstance28", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance28"):
                opp_val = getattr(value, "CourseInstance28", None)
                setattr(value, "CourseInstance28", self)

class course_Organisation:

    pass
class course_TA(Person):

    pass
class course_Lecturer(Person):

    pass
class course_CourseCoordinator(Person):

    pass
class course_Student(Person):

    pass
class course_Course:

    def __init__(self, content: str, credits: float, code: str, name: str, course_Course: "course_Course" = None, course_Course3: set["course_Course"] = None, course_Course7: "course_Course" = None, course_Course5: set["course_Course"] = None, course_Course9: set["course_StudyProgram"] = None, course: set["course_CourseInstance"] = None, courses: "course_Department" = None, Course: "course_CourseInstance" = None, Course22: "course_Department" = None):
        self.content = content
        self.credits = credits
        self.code = code
        self.name = name
        self.course_Course = course_Course
        self.course_Course3 = course_Course3 if course_Course3 is not None else set()
        self.course_Course7 = course_Course7
        self.course_Course5 = course_Course5 if course_Course5 is not None else set()
        self.course_Course9 = course_Course9 if course_Course9 is not None else set()
        self.course = course if course is not None else set()
        self.courses = courses
        self.Course = Course
        self.Course22 = Course22
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

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
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def course_Course3(self):
        return self.__course_Course3

    @course_Course3.setter
    def course_Course3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course_Course3", None)
        self.__course_Course3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_Course"):
                    opp_val = getattr(item, "course_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "course_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_Course"):
                    opp_val = getattr(item, "course_Course", None)
                    
                    setattr(item, "course_Course", self)
                    

    @property
    def course_Course9(self):
        return self.__course_Course9

    @course_Course9.setter
    def course_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course_Course9", None)
        self.__course_Course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_StudyProgram"):
                    opp_val = getattr(item, "course_StudyProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "course_StudyProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_StudyProgram"):
                    opp_val = getattr(item, "course_StudyProgram", None)
                    
                    setattr(item, "course_StudyProgram", self)
                    

    @property
    def course_Course(self):
        return self.__course_Course

    @course_Course.setter
    def course_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course_Course", None)
        self.__course_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_Course3"):
                opp_val = getattr(old_value, "course_Course3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_Course3"):
                opp_val = getattr(value, "course_Course3", None)
                if opp_val is None:
                    setattr(value, "course_Course3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course22(self):
        return self.__Course22

    @Course22.setter
    def Course22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__Course22", None)
        self.__Course22 = value
        
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
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department12"):
                opp_val = getattr(old_value, "Department12", None)
                if opp_val == self:
                    setattr(old_value, "Department12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department12"):
                opp_val = getattr(value, "Department12", None)
                setattr(value, "Department12", self)

    @property
    def course_Course7(self):
        return self.__course_Course7

    @course_Course7.setter
    def course_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course_Course7", None)
        self.__course_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_Course5"):
                opp_val = getattr(old_value, "course_Course5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_Course5"):
                opp_val = getattr(value, "course_Course5", None)
                if opp_val is None:
                    setattr(value, "course_Course5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstances"):
                opp_val = getattr(old_value, "courseInstances", None)
                if opp_val == self:
                    setattr(old_value, "courseInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstances"):
                opp_val = getattr(value, "courseInstances", None)
                setattr(value, "courseInstances", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    setattr(item, "CourseInstance", self)
                    

    @property
    def course_Course5(self):
        return self.__course_Course5

    @course_Course5.setter
    def course_Course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Course__course_Course5", None)
        self.__course_Course5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_Course7"):
                    opp_val = getattr(item, "course_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "course_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_Course7"):
                    opp_val = getattr(item, "course_Course7", None)
                    
                    setattr(item, "course_Course7", self)
                    

class course_Department:

    def __init__(self, name: str, shortName: str, Department: "course_Faculty" = None, Department12: "course_Course" = None, department: set["course_Course"] = None, course_Department: set["course_StudyProgram"] = None, departments: "course_Faculty" = None):
        self.name = name
        self.shortName = shortName
        self.Department = Department
        self.Department12 = Department12
        self.department = department if department is not None else set()
        self.course_Department = course_Department if course_Department is not None else set()
        self.departments = departments
        
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
    def course_Department(self):
        return self.__course_Department

    @course_Department.setter
    def course_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Department__course_Department", None)
        self.__course_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "course_StudyProgram24"):
                    opp_val = getattr(item, "course_StudyProgram24", None)
                    
                    if opp_val == self:
                        setattr(item, "course_StudyProgram24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "course_StudyProgram24"):
                    opp_val = getattr(item, "course_StudyProgram24", None)
                    
                    setattr(item, "course_StudyProgram24", self)
                    

    @property
    def Department12(self):
        return self.__Department12

    @Department12.setter
    def Department12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Department__Department12", None)
        self.__Department12 = value
        
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

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course22"):
                    opp_val = getattr(item, "Course22", None)
                    
                    if opp_val == self:
                        setattr(item, "Course22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course22"):
                    opp_val = getattr(item, "Course22", None)
                    
                    setattr(item, "Course22", self)
                    

    @property
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Department__departments", None)
        self.__departments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty26"):
                opp_val = getattr(old_value, "Faculty26", None)
                if opp_val == self:
                    setattr(old_value, "Faculty26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty26"):
                opp_val = getattr(value, "Faculty26", None)
                setattr(value, "Faculty26", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faculty"):
                opp_val = getattr(old_value, "faculty", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faculty"):
                opp_val = getattr(value, "faculty", None)
                if opp_val is None:
                    setattr(value, "faculty", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class course_Faculty:

    def __init__(self, name: str, shortName: str, Faculty: "course_University" = None, faculties: "course_University" = None, faculty: set["course_Department"] = None, Faculty26: "course_Department" = None):
        self.name = name
        self.shortName = shortName
        self.Faculty = Faculty
        self.faculties = faculties
        self.faculty = faculty if faculty is not None else set()
        self.Faculty26 = Faculty26
        
    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Faculty26(self):
        return self.__Faculty26

    @Faculty26.setter
    def Faculty26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Faculty__Faculty26", None)
        self.__Faculty26 = value
        
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

    @property
    def faculties(self):
        return self.__faculties

    @faculties.setter
    def faculties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Faculty__faculties", None)
        self.__faculties = value
        
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

    @property
    def Faculty(self):
        return self.__Faculty

    @Faculty.setter
    def Faculty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Faculty__Faculty", None)
        self.__Faculty = value
        
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
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_Faculty__faculty", None)
        self.__faculty = value if value is not None else set()
        
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
                    

class course_University:

    def __init__(self, name: str, university: set["course_Faculty"] = None, University: "course_Faculty" = None):
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
    def University(self):
        return self.__University

    @University.setter
    def University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_University__University", None)
        self.__University = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faculties"):
                opp_val = getattr(old_value, "faculties", None)
                if opp_val == self:
                    setattr(old_value, "faculties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faculties"):
                opp_val = getattr(value, "faculties", None)
                setattr(value, "faculties", self)

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_University__university", None)
        self.__university = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Faculty"):
                    opp_val = getattr(item, "Faculty", None)
                    
                    if opp_val == self:
                        setattr(item, "Faculty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Faculty"):
                    opp_val = getattr(item, "Faculty", None)
                    
                    setattr(item, "Faculty", self)
                    

class course_CourseInstance:

    pass
class course_StudyProgram:

    def __init__(self, code: str, course_StudyProgram: "course_Course" = None, course_StudyProgram24: "course_Department" = None, StudyProgram: "course_Student" = None, studyProgram: set["course_Student"] = None, course_StudyProgram48: "course_TimetableEntry" = None):
        self.code = code
        self.course_StudyProgram = course_StudyProgram
        self.course_StudyProgram24 = course_StudyProgram24
        self.StudyProgram = StudyProgram
        self.studyProgram = studyProgram if studyProgram is not None else set()
        self.course_StudyProgram48 = course_StudyProgram48
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def studyProgram(self):
        return self.__studyProgram

    @studyProgram.setter
    def studyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_StudyProgram__studyProgram", None)
        self.__studyProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student40"):
                    opp_val = getattr(item, "Student40", None)
                    
                    if opp_val == self:
                        setattr(item, "Student40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student40"):
                    opp_val = getattr(item, "Student40", None)
                    
                    setattr(item, "Student40", self)
                    

    @property
    def course_StudyProgram(self):
        return self.__course_StudyProgram

    @course_StudyProgram.setter
    def course_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_StudyProgram__course_StudyProgram", None)
        self.__course_StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_Course9"):
                opp_val = getattr(old_value, "course_Course9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_Course9"):
                opp_val = getattr(value, "course_Course9", None)
                if opp_val is None:
                    setattr(value, "course_Course9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students"):
                opp_val = getattr(old_value, "students", None)
                if opp_val == self:
                    setattr(old_value, "students", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students"):
                opp_val = getattr(value, "students", None)
                setattr(value, "students", self)

    @property
    def course_StudyProgram24(self):
        return self.__course_StudyProgram24

    @course_StudyProgram24.setter
    def course_StudyProgram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_StudyProgram__course_StudyProgram24", None)
        self.__course_StudyProgram24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_Department"):
                opp_val = getattr(old_value, "course_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_Department"):
                opp_val = getattr(value, "course_Department", None)
                if opp_val is None:
                    setattr(value, "course_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course_StudyProgram48(self):
        return self.__course_StudyProgram48

    @course_StudyProgram48.setter
    def course_StudyProgram48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course_StudyProgram__course_StudyProgram48", None)
        self.__course_StudyProgram48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course_TimetableEntry47"):
                opp_val = getattr(old_value, "course_TimetableEntry47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course_TimetableEntry47"):
                opp_val = getattr(value, "course_TimetableEntry47", None)
                if opp_val is None:
                    setattr(value, "course_TimetableEntry47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
