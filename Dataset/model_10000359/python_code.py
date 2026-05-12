from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Assessment__Self_Assessment:

    def __init__(self, Name: str, Question: str, Score: str, assessment22: "Assessment" = None):
        self.Name = Name
        self.Question = Question
        self.Score = Score
        self.assessment22 = assessment22
        
        pass
    @property
    def Question(self):
        return self.__Question
    @Question.setter
    def Question(self, Question: str):
        self.__Question = Question

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Score(self):
        return self.__Score
    @Score.setter
    def Score(self, Score: str):
        self.__Score = Score

    @property
    def assessment22(self):
        return self.__assessment22
    @assessment22.setter
    def assessment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assessment__Self_Assessment__assessment22", None)
        self.__assessment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment__Self_Assessment23"):
                opp_val = getattr(old_value, "assessment__Self_Assessment23", None)
                if opp_val == self:
                    setattr(old_value, "assessment__Self_Assessment23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment__Self_Assessment23"):
                opp_val = getattr(value, "assessment__Self_Assessment23", None)
                setattr(value, "assessment__Self_Assessment23", self)



class Assessment:

    def __init__(self, Name: str, Type_of_Assessment: str, Total_Score: str, attendance21: "Attendance" = None, assessment__Self_Assessment23: "Assessment__Self_Assessment" = None, survey25: "Survey" = None, performance27: "Performance" = None):
        self.Name = Name
        self.Type_of_Assessment = Type_of_Assessment
        self.Total_Score = Total_Score
        self.attendance21 = attendance21
        self.assessment__Self_Assessment23 = assessment__Self_Assessment23
        self.survey25 = survey25
        self.performance27 = performance27
        
        pass
    @property
    def Total_Score(self):
        return self.__Total_Score
    @Total_Score.setter
    def Total_Score(self, Total_Score: str):
        self.__Total_Score = Total_Score

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Type_of_Assessment(self):
        return self.__Type_of_Assessment
    @Type_of_Assessment.setter
    def Type_of_Assessment(self, Type_of_Assessment: str):
        self.__Type_of_Assessment = Type_of_Assessment

    @property
    def performance27(self):
        return self.__performance27
    @performance27.setter
    def performance27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assessment__performance27", None)
        self.__performance27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment26"):
                opp_val = getattr(old_value, "assessment26", None)
                if opp_val == self:
                    setattr(old_value, "assessment26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment26"):
                opp_val = getattr(value, "assessment26", None)
                setattr(value, "assessment26", self)

    @property
    def assessment__Self_Assessment23(self):
        return self.__assessment__Self_Assessment23
    @assessment__Self_Assessment23.setter
    def assessment__Self_Assessment23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assessment__assessment__Self_Assessment23", None)
        self.__assessment__Self_Assessment23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment22"):
                opp_val = getattr(old_value, "assessment22", None)
                if opp_val == self:
                    setattr(old_value, "assessment22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment22"):
                opp_val = getattr(value, "assessment22", None)
                setattr(value, "assessment22", self)

    @property
    def attendance21(self):
        return self.__attendance21
    @attendance21.setter
    def attendance21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assessment__attendance21", None)
        self.__attendance21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment20"):
                opp_val = getattr(old_value, "assessment20", None)
                if opp_val == self:
                    setattr(old_value, "assessment20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment20"):
                opp_val = getattr(value, "assessment20", None)
                setattr(value, "assessment20", self)

    @property
    def survey25(self):
        return self.__survey25
    @survey25.setter
    def survey25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assessment__survey25", None)
        self.__survey25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assessment24"):
                opp_val = getattr(old_value, "assessment24", None)
                if opp_val == self:
                    setattr(old_value, "assessment24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assessment24"):
                opp_val = getattr(value, "assessment24", None)
                setattr(value, "assessment24", self)



class Performance:

    def __init__(self, Name: str, Punctuality: str, Target: str, Coordination: str, assessment26: "Assessment" = None):
        self.Name = Name
        self.Punctuality = Punctuality
        self.Target = Target
        self.Coordination = Coordination
        self.assessment26 = assessment26
        
        pass
    @property
    def Target(self):
        return self.__Target
    @Target.setter
    def Target(self, Target: str):
        self.__Target = Target

    @property
    def Punctuality(self):
        return self.__Punctuality
    @Punctuality.setter
    def Punctuality(self, Punctuality: str):
        self.__Punctuality = Punctuality

    @property
    def Coordination(self):
        return self.__Coordination
    @Coordination.setter
    def Coordination(self, Coordination: str):
        self.__Coordination = Coordination

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def assessment26(self):
        return self.__assessment26
    @assessment26.setter
    def assessment26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Performance__assessment26", None)
        self.__assessment26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performance27"):
                opp_val = getattr(old_value, "performance27", None)
                if opp_val == self:
                    setattr(old_value, "performance27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performance27"):
                opp_val = getattr(value, "performance27", None)
                setattr(value, "performance27", self)



class Survey:

    def __init__(self, Name: str, Question: str, Score: str, assessment24: "Assessment" = None):
        self.Name = Name
        self.Question = Question
        self.Score = Score
        self.assessment24 = assessment24
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Question(self):
        return self.__Question
    @Question.setter
    def Question(self, Question: str):
        self.__Question = Question

    @property
    def Score(self):
        return self.__Score
    @Score.setter
    def Score(self, Score: str):
        self.__Score = Score

    @property
    def assessment24(self):
        return self.__assessment24
    @assessment24.setter
    def assessment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Survey__assessment24", None)
        self.__assessment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "survey25"):
                opp_val = getattr(old_value, "survey25", None)
                if opp_val == self:
                    setattr(old_value, "survey25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "survey25"):
                opp_val = getattr(value, "survey25", None)
                setattr(value, "survey25", self)



class New_Employee:

    def __init__(self, Name: str, Position: str, Division: str, Date_of_Birth: str, Place_of_Birth: str, Working_Since: str, registration11: "Registration" = None, applicant13: "Applicant" = None, task15: "Task" = None, attendance16: "Attendance" = None):
        self.Name = Name
        self.Position = Position
        self.Division = Division
        self.Date_of_Birth = Date_of_Birth
        self.Place_of_Birth = Place_of_Birth
        self.Working_Since = Working_Since
        self.registration11 = registration11
        self.applicant13 = applicant13
        self.task15 = task15
        self.attendance16 = attendance16
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Working_Since(self):
        return self.__Working_Since
    @Working_Since.setter
    def Working_Since(self, Working_Since: str):
        self.__Working_Since = Working_Since

    @property
    def Place_of_Birth(self):
        return self.__Place_of_Birth
    @Place_of_Birth.setter
    def Place_of_Birth(self, Place_of_Birth: str):
        self.__Place_of_Birth = Place_of_Birth

    @property
    def Division(self):
        return self.__Division
    @Division.setter
    def Division(self, Division: str):
        self.__Division = Division

    @property
    def Date_of_Birth(self):
        return self.__Date_of_Birth
    @Date_of_Birth.setter
    def Date_of_Birth(self, Date_of_Birth: str):
        self.__Date_of_Birth = Date_of_Birth

    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: str):
        self.__Position = Position

    @property
    def registration11(self):
        return self.__registration11
    @registration11.setter
    def registration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_Employee__registration11", None)
        self.__registration11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_Employee10"):
                opp_val = getattr(old_value, "new_Employee10", None)
                if opp_val == self:
                    setattr(old_value, "new_Employee10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_Employee10"):
                opp_val = getattr(value, "new_Employee10", None)
                setattr(value, "new_Employee10", self)

    @property
    def applicant13(self):
        return self.__applicant13
    @applicant13.setter
    def applicant13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_Employee__applicant13", None)
        self.__applicant13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_Employee12"):
                opp_val = getattr(old_value, "new_Employee12", None)
                if opp_val == self:
                    setattr(old_value, "new_Employee12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_Employee12"):
                opp_val = getattr(value, "new_Employee12", None)
                setattr(value, "new_Employee12", self)

    @property
    def attendance16(self):
        return self.__attendance16
    @attendance16.setter
    def attendance16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_Employee__attendance16", None)
        self.__attendance16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_Employee17"):
                opp_val = getattr(old_value, "new_Employee17", None)
                if opp_val == self:
                    setattr(old_value, "new_Employee17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_Employee17"):
                opp_val = getattr(value, "new_Employee17", None)
                setattr(value, "new_Employee17", self)

    @property
    def task15(self):
        return self.__task15
    @task15.setter
    def task15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_New_Employee__task15", None)
        self.__task15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "new_Employee14"):
                opp_val = getattr(old_value, "new_Employee14", None)
                if opp_val == self:
                    setattr(old_value, "new_Employee14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "new_Employee14"):
                opp_val = getattr(value, "new_Employee14", None)
                setattr(value, "new_Employee14", self)



class Task:

    def __init__(self, Task_Name: str, Task_Detail: str, Name: str, Deadline: str, new_Employee14: "New_Employee" = None):
        self.Task_Name = Task_Name
        self.Task_Detail = Task_Detail
        self.Name = Name
        self.Deadline = Deadline
        self.new_Employee14 = new_Employee14
        
        pass
    @property
    def Task_Detail(self):
        return self.__Task_Detail
    @Task_Detail.setter
    def Task_Detail(self, Task_Detail: str):
        self.__Task_Detail = Task_Detail

    @property
    def Deadline(self):
        return self.__Deadline
    @Deadline.setter
    def Deadline(self, Deadline: str):
        self.__Deadline = Deadline

    @property
    def Task_Name(self):
        return self.__Task_Name
    @Task_Name.setter
    def Task_Name(self, Task_Name: str):
        self.__Task_Name = Task_Name

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def new_Employee14(self):
        return self.__new_Employee14
    @new_Employee14.setter
    def new_Employee14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task__new_Employee14", None)
        self.__new_Employee14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task15"):
                opp_val = getattr(old_value, "task15", None)
                if opp_val == self:
                    setattr(old_value, "task15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task15"):
                opp_val = getattr(value, "task15", None)
                setattr(value, "task15", self)



class Requirement:

    def __init__(self, ID_Card: str, Curriculum_Vitae: str, Diploma: str, Transcript: str, Photo: str, registration18: "Registration" = None):
        self.ID_Card = ID_Card
        self.Curriculum_Vitae = Curriculum_Vitae
        self.Diploma = Diploma
        self.Transcript = Transcript
        self.Photo = Photo
        self.registration18 = registration18
        
        pass
    @property
    def Transcript(self):
        return self.__Transcript
    @Transcript.setter
    def Transcript(self, Transcript: str):
        self.__Transcript = Transcript

    @property
    def Photo(self):
        return self.__Photo
    @Photo.setter
    def Photo(self, Photo: str):
        self.__Photo = Photo

    @property
    def Diploma(self):
        return self.__Diploma
    @Diploma.setter
    def Diploma(self, Diploma: str):
        self.__Diploma = Diploma

    @property
    def ID_Card(self):
        return self.__ID_Card
    @ID_Card.setter
    def ID_Card(self, ID_Card: str):
        self.__ID_Card = ID_Card

    @property
    def Curriculum_Vitae(self):
        return self.__Curriculum_Vitae
    @Curriculum_Vitae.setter
    def Curriculum_Vitae(self, Curriculum_Vitae: str):
        self.__Curriculum_Vitae = Curriculum_Vitae

    @property
    def registration18(self):
        return self.__registration18
    @registration18.setter
    def registration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requirement__registration18", None)
        self.__registration18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement19"):
                opp_val = getattr(old_value, "requirement19", None)
                if opp_val == self:
                    setattr(old_value, "requirement19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement19"):
                opp_val = getattr(value, "requirement19", None)
                setattr(value, "requirement19", self)



class Attendance:

    def __init__(self, Name: str, Date___Time: str, Position: str, Details: str, assessment20: "Assessment" = None, new_Employee17: "New_Employee" = None):
        self.Name = Name
        self.Date___Time = Date___Time
        self.Position = Position
        self.Details = Details
        self.assessment20 = assessment20
        self.new_Employee17 = new_Employee17
        
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

    @property
    def Date___Time(self):
        return self.__Date___Time
    @Date___Time.setter
    def Date___Time(self, Date___Time: str):
        self.__Date___Time = Date___Time

    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details

    @property
    def assessment20(self):
        return self.__assessment20
    @assessment20.setter
    def assessment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__assessment20", None)
        self.__assessment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance21"):
                opp_val = getattr(old_value, "attendance21", None)
                if opp_val == self:
                    setattr(old_value, "attendance21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance21"):
                opp_val = getattr(value, "attendance21", None)
                setattr(value, "attendance21", self)

    @property
    def new_Employee17(self):
        return self.__new_Employee17
    @new_Employee17.setter
    def new_Employee17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__new_Employee17", None)
        self.__new_Employee17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance16"):
                opp_val = getattr(old_value, "attendance16", None)
                if opp_val == self:
                    setattr(old_value, "attendance16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance16"):
                opp_val = getattr(value, "attendance16", None)
                setattr(value, "attendance16", self)



class Login:

    def __init__(self, userid: str, password: str, admin1: "Admin" = None, applicant3: "Applicant" = None):
        self.userid = userid
        self.password = password
        self.admin1 = admin1
        self.applicant3 = applicant3
        
        pass
    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, userid: str):
        self.__userid = userid

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def admin1(self):
        return self.__admin1
    @admin1.setter
    def admin1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__admin1", None)
        self.__admin1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login0"):
                opp_val = getattr(old_value, "login0", None)
                if opp_val == self:
                    setattr(old_value, "login0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login0"):
                opp_val = getattr(value, "login0", None)
                setattr(value, "login0", self)

    @property
    def applicant3(self):
        return self.__applicant3
    @applicant3.setter
    def applicant3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__applicant3", None)
        self.__applicant3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login2"):
                opp_val = getattr(old_value, "login2", None)
                if opp_val == self:
                    setattr(old_value, "login2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login2"):
                opp_val = getattr(value, "login2", None)
                setattr(value, "login2", self)



class Position:

    def __init__(self, positionID: int, positionName: str, divisionName: str, jobID: str, applicant9: "Applicant" = None):
        self.positionID = positionID
        self.positionName = positionName
        self.divisionName = divisionName
        self.jobID = jobID
        self.applicant9 = applicant9
        
        pass
    @property
    def positionName(self):
        return self.__positionName
    @positionName.setter
    def positionName(self, positionName: str):
        self.__positionName = positionName

    @property
    def jobID(self):
        return self.__jobID
    @jobID.setter
    def jobID(self, jobID: str):
        self.__jobID = jobID

    @property
    def divisionName(self):
        return self.__divisionName
    @divisionName.setter
    def divisionName(self, divisionName: str):
        self.__divisionName = divisionName

    @property
    def positionID(self):
        return self.__positionID
    @positionID.setter
    def positionID(self, positionID: int):
        self.__positionID = positionID

    @property
    def applicant9(self):
        return self.__applicant9
    @applicant9.setter
    def applicant9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Position__applicant9", None)
        self.__applicant9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "position8"):
                opp_val = getattr(old_value, "position8", None)
                if opp_val == self:
                    setattr(old_value, "position8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "position8"):
                opp_val = getattr(value, "position8", None)
                setattr(value, "position8", self)



class Registration:

    def __init__(self, Date: str, Name: str, Address: str, Phone: str, Email: str, Applied_Position: str, Position_Type: str, Skills___Requirement: str, applicant5: "Applicant" = None, admin7: "Admin" = None, new_Employee10: "New_Employee" = None, requirement19: "Requirement" = None):
        self.Date = Date
        self.Name = Name
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Applied_Position = Applied_Position
        self.Position_Type = Position_Type
        self.Skills___Requirement = Skills___Requirement
        self.applicant5 = applicant5
        self.admin7 = admin7
        self.new_Employee10 = new_Employee10
        self.requirement19 = requirement19
        
        pass
    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Skills___Requirement(self):
        return self.__Skills___Requirement
    @Skills___Requirement.setter
    def Skills___Requirement(self, Skills___Requirement: str):
        self.__Skills___Requirement = Skills___Requirement

    @property
    def Position_Type(self):
        return self.__Position_Type
    @Position_Type.setter
    def Position_Type(self, Position_Type: str):
        self.__Position_Type = Position_Type

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Applied_Position(self):
        return self.__Applied_Position
    @Applied_Position.setter
    def Applied_Position(self, Applied_Position: str):
        self.__Applied_Position = Applied_Position

    @property
    def admin7(self):
        return self.__admin7
    @admin7.setter
    def admin7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__admin7", None)
        self.__admin7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration6"):
                opp_val = getattr(old_value, "registration6", None)
                if opp_val == self:
                    setattr(old_value, "registration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration6"):
                opp_val = getattr(value, "registration6", None)
                setattr(value, "registration6", self)

    @property
    def requirement19(self):
        return self.__requirement19
    @requirement19.setter
    def requirement19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__requirement19", None)
        self.__requirement19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration18"):
                opp_val = getattr(old_value, "registration18", None)
                if opp_val == self:
                    setattr(old_value, "registration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration18"):
                opp_val = getattr(value, "registration18", None)
                setattr(value, "registration18", self)

    @property
    def new_Employee10(self):
        return self.__new_Employee10
    @new_Employee10.setter
    def new_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__new_Employee10", None)
        self.__new_Employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration11"):
                opp_val = getattr(old_value, "registration11", None)
                if opp_val == self:
                    setattr(old_value, "registration11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration11"):
                opp_val = getattr(value, "registration11", None)
                setattr(value, "registration11", self)

    @property
    def applicant5(self):
        return self.__applicant5
    @applicant5.setter
    def applicant5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Registration__applicant5", None)
        self.__applicant5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "registration4"):
                opp_val = getattr(old_value, "registration4", None)
                if opp_val == self:
                    setattr(old_value, "registration4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "registration4"):
                opp_val = getattr(value, "registration4", None)
                setattr(value, "registration4", self)



class Admin:

    def __init__(self, name: str, qualification: str, address: str, login0: "Login" = None, registration6: "Registration" = None):
        self.name = name
        self.qualification = qualification
        self.address = address
        self.login0 = login0
        self.registration6 = registration6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def qualification(self):
        return self.__qualification
    @qualification.setter
    def qualification(self, qualification: str):
        self.__qualification = qualification

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def login0(self):
        return self.__login0
    @login0.setter
    def login0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__login0", None)
        self.__login0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin1"):
                opp_val = getattr(old_value, "admin1", None)
                if opp_val == self:
                    setattr(old_value, "admin1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin1"):
                opp_val = getattr(value, "admin1", None)
                setattr(value, "admin1", self)

    @property
    def registration6(self):
        return self.__registration6
    @registration6.setter
    def registration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__registration6", None)
        self.__registration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin7"):
                opp_val = getattr(old_value, "admin7", None)
                if opp_val == self:
                    setattr(old_value, "admin7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin7"):
                opp_val = getattr(value, "admin7", None)
                setattr(value, "admin7", self)



class Applicant:

    def __init__(self, First_Name: str, Last_Name: str, Applied_Position: str, Email: str, Password: str, Date_of_Birth: str, Phone: str, Address: str, login2: "Login" = None, registration4: "Registration" = None, position8: "Position" = None, new_Employee12: "New_Employee" = None):
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Applied_Position = Applied_Position
        self.Email = Email
        self.Password = Password
        self.Date_of_Birth = Date_of_Birth
        self.Phone = Phone
        self.Address = Address
        self.login2 = login2
        self.registration4 = registration4
        self.position8 = position8
        self.new_Employee12 = new_Employee12
        
        pass
    @property
    def Date_of_Birth(self):
        return self.__Date_of_Birth
    @Date_of_Birth.setter
    def Date_of_Birth(self, Date_of_Birth: str):
        self.__Date_of_Birth = Date_of_Birth

    @property
    def Applied_Position(self):
        return self.__Applied_Position
    @Applied_Position.setter
    def Applied_Position(self, Applied_Position: str):
        self.__Applied_Position = Applied_Position

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def First_Name(self):
        return self.__First_Name
    @First_Name.setter
    def First_Name(self, First_Name: str):
        self.__First_Name = First_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: str):
        self.__Phone = Phone

    @property
    def Last_Name(self):
        return self.__Last_Name
    @Last_Name.setter
    def Last_Name(self, Last_Name: str):
        self.__Last_Name = Last_Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def registration4(self):
        return self.__registration4
    @registration4.setter
    def registration4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Applicant__registration4", None)
        self.__registration4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicant5"):
                opp_val = getattr(old_value, "applicant5", None)
                if opp_val == self:
                    setattr(old_value, "applicant5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicant5"):
                opp_val = getattr(value, "applicant5", None)
                setattr(value, "applicant5", self)

    @property
    def login2(self):
        return self.__login2
    @login2.setter
    def login2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Applicant__login2", None)
        self.__login2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicant3"):
                opp_val = getattr(old_value, "applicant3", None)
                if opp_val == self:
                    setattr(old_value, "applicant3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicant3"):
                opp_val = getattr(value, "applicant3", None)
                setattr(value, "applicant3", self)

    @property
    def new_Employee12(self):
        return self.__new_Employee12
    @new_Employee12.setter
    def new_Employee12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Applicant__new_Employee12", None)
        self.__new_Employee12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicant13"):
                opp_val = getattr(old_value, "applicant13", None)
                if opp_val == self:
                    setattr(old_value, "applicant13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicant13"):
                opp_val = getattr(value, "applicant13", None)
                setattr(value, "applicant13", self)

    @property
    def position8(self):
        return self.__position8
    @position8.setter
    def position8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Applicant__position8", None)
        self.__position8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "applicant9"):
                opp_val = getattr(old_value, "applicant9", None)
                if opp_val == self:
                    setattr(old_value, "applicant9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "applicant9"):
                opp_val = getattr(value, "applicant9", None)
                setattr(value, "applicant9", self)

