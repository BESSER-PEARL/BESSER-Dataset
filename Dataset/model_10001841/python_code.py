from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Other_employees:

    def __init__(self, Name: str, Position: str):
        self.Name = Name
        self.Position = Position
        
        pass
    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: str):
        self.__Position = Position

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Dean:

    def __init__(self, Employees: Dean, news_in_Dl2: "News_in_Dl" = None, administrator5: "Administrator" = None):
        self.Employees = Employees
        self.news_in_Dl2 = news_in_Dl2
        self.administrator5 = administrator5
        
        pass
    @property
    def Employees(self):
        return self.__Employees
    @Employees.setter
    def Employees(self, Employees: Dean):
        self.__Employees = Employees

    @property
    def news_in_Dl2(self):
        return self.__news_in_Dl2
    @news_in_Dl2.setter
    def news_in_Dl2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dean__news_in_Dl2", None)
        self.__news_in_Dl2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dean3"):
                opp_val = getattr(old_value, "dean3", None)
                if opp_val == self:
                    setattr(old_value, "dean3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dean3"):
                opp_val = getattr(value, "dean3", None)
                setattr(value, "dean3", self)

    @property
    def administrator5(self):
        return self.__administrator5
    @administrator5.setter
    def administrator5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dean__administrator5", None)
        self.__administrator5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dean4"):
                opp_val = getattr(old_value, "dean4", None)
                if opp_val == self:
                    setattr(old_value, "dean4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dean4"):
                opp_val = getattr(value, "dean4", None)
                setattr(value, "dean4", self)



class Moderator:

    def __init__(self, Name: Moderator, administrator11: "Administrator" = None):
        self.Name = Name
        self.administrator11 = administrator11
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: Moderator):
        self.__Name = Name

    @property
    def administrator11(self):
        return self.__administrator11
    @administrator11.setter
    def administrator11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Moderator__administrator11", None)
        self.__administrator11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "moderator10"):
                opp_val = getattr(old_value, "moderator10", None)
                if opp_val == self:
                    setattr(old_value, "moderator10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "moderator10"):
                opp_val = getattr(value, "moderator10", None)
                setattr(value, "moderator10", self)



class Questionnaire_survey:

    def __init__(self, Teachers: str, Students: str):
        self.Teachers = Teachers
        self.Students = Students
        
        pass
    @property
    def Teachers(self):
        return self.__Teachers
    @Teachers.setter
    def Teachers(self, Teachers: str):
        self.__Teachers = Teachers

    @property
    def Students(self):
        return self.__Students
    @Students.setter
    def Students(self, Students: str):
        self.__Students = Students



class Library:

    def __init__(self, Books: Library, Materials: Library):
        self.Books = Books
        self.Materials = Materials
        
        pass
    @property
    def Books(self):
        return self.__Books
    @Books.setter
    def Books(self, Books: Library):
        self.__Books = Books

    @property
    def Materials(self):
        return self.__Materials
    @Materials.setter
    def Materials(self, Materials: Library):
        self.__Materials = Materials



class Schedule:

    def __init__(self, Teacher: Schedule, Course: Schedule, teachers19: "Teachers" = None):
        self.Teacher = Teacher
        self.Course = Course
        self.teachers19 = teachers19
        
        pass
    @property
    def Course(self):
        return self.__Course
    @Course.setter
    def Course(self, Course: Schedule):
        self.__Course = Course

    @property
    def Teacher(self):
        return self.__Teacher
    @Teacher.setter
    def Teacher(self, Teacher: Schedule):
        self.__Teacher = Teacher

    @property
    def teachers19(self):
        return self.__teachers19
    @teachers19.setter
    def teachers19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Schedule__teachers19", None)
        self.__teachers19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schedule18"):
                opp_val = getattr(old_value, "schedule18", None)
                if opp_val == self:
                    setattr(old_value, "schedule18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schedule18"):
                opp_val = getattr(value, "schedule18", None)
                setattr(value, "schedule18", self)



class Training_materials_IITU:

    def __init__(self, Materials: str):
        self.Materials = Materials
        
        pass
    @property
    def Materials(self):
        return self.__Materials
    @Materials.setter
    def Materials(self, Materials: str):
        self.__Materials = Materials



class News_in_Dl:

    def __init__(self, Opens_news: Moderator, Update_news: Moderator, Hyperlink: str, dean3: "Dean" = None):
        self.Opens_news = Opens_news
        self.Update_news = Update_news
        self.Hyperlink = Hyperlink
        self.dean3 = dean3
        
        pass
    @property
    def Opens_news(self):
        return self.__Opens_news
    @Opens_news.setter
    def Opens_news(self, Opens_news: Moderator):
        self.__Opens_news = Opens_news

    @property
    def Hyperlink(self):
        return self.__Hyperlink
    @Hyperlink.setter
    def Hyperlink(self, Hyperlink: str):
        self.__Hyperlink = Hyperlink

    @property
    def Update_news(self):
        return self.__Update_news
    @Update_news.setter
    def Update_news(self, Update_news: Moderator):
        self.__Update_news = Update_news

    @property
    def dean3(self):
        return self.__dean3
    @dean3.setter
    def dean3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_News_in_Dl__dean3", None)
        self.__dean3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "news_in_Dl2"):
                opp_val = getattr(old_value, "news_in_Dl2", None)
                if opp_val == self:
                    setattr(old_value, "news_in_Dl2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "news_in_Dl2"):
                opp_val = getattr(value, "news_in_Dl2", None)
                setattr(value, "news_in_Dl2", self)



class Team:

    def __init__(self, Robotric_teams: Students, Footballs_teams: Students, Ministry: str, President: str, students14: "Students" = None):
        self.Robotric_teams = Robotric_teams
        self.Footballs_teams = Footballs_teams
        self.Ministry = Ministry
        self.President = President
        self.students14 = students14
        
        pass
    @property
    def Footballs_teams(self):
        return self.__Footballs_teams
    @Footballs_teams.setter
    def Footballs_teams(self, Footballs_teams: Students):
        self.__Footballs_teams = Footballs_teams

    @property
    def Ministry(self):
        return self.__Ministry
    @Ministry.setter
    def Ministry(self, Ministry: str):
        self.__Ministry = Ministry

    @property
    def Robotric_teams(self):
        return self.__Robotric_teams
    @Robotric_teams.setter
    def Robotric_teams(self, Robotric_teams: Students):
        self.__Robotric_teams = Robotric_teams

    @property
    def President(self):
        return self.__President
    @President.setter
    def President(self, President: str):
        self.__President = President

    @property
    def students14(self):
        return self.__students14
    @students14.setter
    def students14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__students14", None)
        self.__students14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team15"):
                opp_val = getattr(old_value, "team15", None)
                if opp_val == self:
                    setattr(old_value, "team15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team15"):
                opp_val = getattr(value, "team15", None)
                setattr(value, "team15", self)



class Course:

    def __init__(self, _1_Course: Department, _2_Course: Department, _3_Course: Department, _4_Course: Department, department0: "Department" = None, administrator7: "Administrator" = None, teachers21: "Teachers" = None, students22: "Students" = None):
        self._1_Course = _1_Course
        self._2_Course = _2_Course
        self._3_Course = _3_Course
        self._4_Course = _4_Course
        self.department0 = department0
        self.administrator7 = administrator7
        self.teachers21 = teachers21
        self.students22 = students22
        
        pass
    @property
    def _2_Course(self):
        return self.___2_Course
    @_2_Course.setter
    def _2_Course(self, _2_Course: Department):
        self.___2_Course = _2_Course

    @property
    def _3_Course(self):
        return self.___3_Course
    @_3_Course.setter
    def _3_Course(self, _3_Course: Department):
        self.___3_Course = _3_Course

    @property
    def _1_Course(self):
        return self.___1_Course
    @_1_Course.setter
    def _1_Course(self, _1_Course: Department):
        self.___1_Course = _1_Course

    @property
    def _4_Course(self):
        return self.___4_Course
    @_4_Course.setter
    def _4_Course(self, _4_Course: Department):
        self.___4_Course = _4_Course

    @property
    def administrator7(self):
        return self.__administrator7
    @administrator7.setter
    def administrator7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__administrator7", None)
        self.__administrator7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course6"):
                opp_val = getattr(old_value, "course6", None)
                if opp_val == self:
                    setattr(old_value, "course6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course6"):
                opp_val = getattr(value, "course6", None)
                setattr(value, "course6", self)

    @property
    def students22(self):
        return self.__students22
    @students22.setter
    def students22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__students22", None)
        self.__students22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course23"):
                opp_val = getattr(old_value, "course23", None)
                if opp_val == self:
                    setattr(old_value, "course23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course23"):
                opp_val = getattr(value, "course23", None)
                setattr(value, "course23", self)

    @property
    def department0(self):
        return self.__department0
    @department0.setter
    def department0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__department0", None)
        self.__department0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course1"):
                opp_val = getattr(old_value, "course1", None)
                if opp_val == self:
                    setattr(old_value, "course1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course1"):
                opp_val = getattr(value, "course1", None)
                setattr(value, "course1", self)

    @property
    def teachers21(self):
        return self.__teachers21
    @teachers21.setter
    def teachers21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Course__teachers21", None)
        self.__teachers21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course20"):
                opp_val = getattr(old_value, "course20", None)
                if opp_val == self:
                    setattr(old_value, "course20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course20"):
                opp_val = getattr(value, "course20", None)
                setattr(value, "course20", self)



class Department:

    def __init__(self, IS: str, MCM: str, CSSE: str, CS: str, JUR: str, ITM: str, course1: "Course" = None, students12: "Students" = None):
        self.IS = IS
        self.MCM = MCM
        self.CSSE = CSSE
        self.CS = CS
        self.JUR = JUR
        self.ITM = ITM
        self.course1 = course1
        self.students12 = students12
        
        pass
    @property
    def MCM(self):
        return self.__MCM
    @MCM.setter
    def MCM(self, MCM: str):
        self.__MCM = MCM

    @property
    def JUR(self):
        return self.__JUR
    @JUR.setter
    def JUR(self, JUR: str):
        self.__JUR = JUR

    @property
    def CSSE(self):
        return self.__CSSE
    @CSSE.setter
    def CSSE(self, CSSE: str):
        self.__CSSE = CSSE

    @property
    def ITM(self):
        return self.__ITM
    @ITM.setter
    def ITM(self, ITM: str):
        self.__ITM = ITM

    @property
    def CS(self):
        return self.__CS
    @CS.setter
    def CS(self, CS: str):
        self.__CS = CS

    @property
    def IS(self):
        return self.__IS
    @IS.setter
    def IS(self, IS: str):
        self.__IS = IS

    @property
    def course1(self):
        return self.__course1
    @course1.setter
    def course1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__course1", None)
        self.__course1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department0"):
                opp_val = getattr(old_value, "department0", None)
                if opp_val == self:
                    setattr(old_value, "department0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department0"):
                opp_val = getattr(value, "department0", None)
                setattr(value, "department0", self)

    @property
    def students12(self):
        return self.__students12
    @students12.setter
    def students12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__students12", None)
        self.__students12 = value
        
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



class Students:

    def __init__(self, ID: Students, Name: str, Course: Course, department13: "Department" = None, team15: "Team" = None, teachers17: "Teachers" = None, course23: "Course" = None):
        self.ID = ID
        self.Name = Name
        self.Course = Course
        self.department13 = department13
        self.team15 = team15
        self.teachers17 = teachers17
        self.course23 = course23
        
        pass
    @property
    def Course(self):
        return self.__Course
    @Course.setter
    def Course(self, Course: Course):
        self.__Course = Course

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: Students):
        self.__ID = ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def team15(self):
        return self.__team15
    @team15.setter
    def team15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Students__team15", None)
        self.__team15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students14"):
                opp_val = getattr(old_value, "students14", None)
                if opp_val == self:
                    setattr(old_value, "students14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students14"):
                opp_val = getattr(value, "students14", None)
                setattr(value, "students14", self)

    @property
    def teachers17(self):
        return self.__teachers17
    @teachers17.setter
    def teachers17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Students__teachers17", None)
        self.__teachers17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students16"):
                opp_val = getattr(old_value, "students16", None)
                if opp_val == self:
                    setattr(old_value, "students16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students16"):
                opp_val = getattr(value, "students16", None)
                setattr(value, "students16", self)

    @property
    def course23(self):
        return self.__course23
    @course23.setter
    def course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Students__course23", None)
        self.__course23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students22"):
                opp_val = getattr(old_value, "students22", None)
                if opp_val == self:
                    setattr(old_value, "students22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students22"):
                opp_val = getattr(value, "students22", None)
                setattr(value, "students22", self)

    @property
    def department13(self):
        return self.__department13
    @department13.setter
    def department13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Students__department13", None)
        self.__department13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students12"):
                opp_val = getattr(old_value, "students12", None)
                if opp_val == self:
                    setattr(old_value, "students12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students12"):
                opp_val = getattr(value, "students12", None)
                setattr(value, "students12", self)



class Teachers:

    def __init__(self, ID: Teachers, Name: str, Rank: Teachers, Department: Department, Course: Course, Info: Teachers, administrator9: "Administrator" = None, students16: "Students" = None, schedule18: "Schedule" = None, course20: "Course" = None):
        self.ID = ID
        self.Name = Name
        self.Rank = Rank
        self.Department = Department
        self.Course = Course
        self.Info = Info
        self.administrator9 = administrator9
        self.students16 = students16
        self.schedule18 = schedule18
        self.course20 = course20
        
        pass
    @property
    def Info(self):
        return self.__Info
    @Info.setter
    def Info(self, Info: Teachers):
        self.__Info = Info

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: Department):
        self.__Department = Department

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Course(self):
        return self.__Course
    @Course.setter
    def Course(self, Course: Course):
        self.__Course = Course

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: Teachers):
        self.__ID = ID

    @property
    def Rank(self):
        return self.__Rank
    @Rank.setter
    def Rank(self, Rank: Teachers):
        self.__Rank = Rank

    @property
    def administrator9(self):
        return self.__administrator9
    @administrator9.setter
    def administrator9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teachers__administrator9", None)
        self.__administrator9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachers8"):
                opp_val = getattr(old_value, "teachers8", None)
                if opp_val == self:
                    setattr(old_value, "teachers8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachers8"):
                opp_val = getattr(value, "teachers8", None)
                setattr(value, "teachers8", self)

    @property
    def course20(self):
        return self.__course20
    @course20.setter
    def course20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teachers__course20", None)
        self.__course20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachers21"):
                opp_val = getattr(old_value, "teachers21", None)
                if opp_val == self:
                    setattr(old_value, "teachers21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachers21"):
                opp_val = getattr(value, "teachers21", None)
                setattr(value, "teachers21", self)

    @property
    def schedule18(self):
        return self.__schedule18
    @schedule18.setter
    def schedule18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teachers__schedule18", None)
        self.__schedule18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachers19"):
                opp_val = getattr(old_value, "teachers19", None)
                if opp_val == self:
                    setattr(old_value, "teachers19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachers19"):
                opp_val = getattr(value, "teachers19", None)
                setattr(value, "teachers19", self)

    @property
    def students16(self):
        return self.__students16
    @students16.setter
    def students16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Teachers__students16", None)
        self.__students16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachers17"):
                opp_val = getattr(old_value, "teachers17", None)
                if opp_val == self:
                    setattr(old_value, "teachers17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachers17"):
                opp_val = getattr(value, "teachers17", None)
                setattr(value, "teachers17", self)



class Administrator:

    def __init__(self, Name: Administrator, Privilege: str, dean4: "Dean" = None, course6: "Course" = None, teachers8: "Teachers" = None, moderator10: "Moderator" = None):
        self.Name = Name
        self.Privilege = Privilege
        self.dean4 = dean4
        self.course6 = course6
        self.teachers8 = teachers8
        self.moderator10 = moderator10
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: Administrator):
        self.__Name = Name

    @property
    def Privilege(self):
        return self.__Privilege
    @Privilege.setter
    def Privilege(self, Privilege: str):
        self.__Privilege = Privilege

    @property
    def dean4(self):
        return self.__dean4
    @dean4.setter
    def dean4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__dean4", None)
        self.__dean4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator5"):
                opp_val = getattr(old_value, "administrator5", None)
                if opp_val == self:
                    setattr(old_value, "administrator5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator5"):
                opp_val = getattr(value, "administrator5", None)
                setattr(value, "administrator5", self)

    @property
    def teachers8(self):
        return self.__teachers8
    @teachers8.setter
    def teachers8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__teachers8", None)
        self.__teachers8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator9"):
                opp_val = getattr(old_value, "administrator9", None)
                if opp_val == self:
                    setattr(old_value, "administrator9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator9"):
                opp_val = getattr(value, "administrator9", None)
                setattr(value, "administrator9", self)

    @property
    def moderator10(self):
        return self.__moderator10
    @moderator10.setter
    def moderator10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__moderator10", None)
        self.__moderator10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator11"):
                opp_val = getattr(old_value, "administrator11", None)
                if opp_val == self:
                    setattr(old_value, "administrator11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator11"):
                opp_val = getattr(value, "administrator11", None)
                setattr(value, "administrator11", self)

    @property
    def course6(self):
        return self.__course6
    @course6.setter
    def course6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__course6", None)
        self.__course6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator7"):
                opp_val = getattr(old_value, "administrator7", None)
                if opp_val == self:
                    setattr(old_value, "administrator7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator7"):
                opp_val = getattr(value, "administrator7", None)
                setattr(value, "administrator7", self)

