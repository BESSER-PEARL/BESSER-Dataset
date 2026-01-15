from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class e2_University:

    def __init__(self, Name: str, e2_University: set["e2_Person"] = None, e2_University32: set["e2_Course"] = None):
        self.Name = Name
        self.e2_University = e2_University if e2_University is not None else set()
        self.e2_University32 = e2_University32 if e2_University32 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_University32(self):
        return self.__e2_University32

    @e2_University32.setter
    def e2_University32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_University__e2_University32", None)
        self.__e2_University32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Course33"):
                    opp_val = getattr(item, "e2_Course33", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Course33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Course33"):
                    opp_val = getattr(item, "e2_Course33", None)
                    
                    setattr(item, "e2_Course33", self)
                    

    @property
    def e2_University(self):
        return self.__e2_University

    @e2_University.setter
    def e2_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_University__e2_University", None)
        self.__e2_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person30"):
                    opp_val = getattr(item, "e2_Person30", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person30"):
                    opp_val = getattr(item, "e2_Person30", None)
                    
                    setattr(item, "e2_Person30", self)
                    

class e2_Group:

    def __init__(self, Name: str, e2_Group: "e2_Course" = None, e2_Group18: set["e2_Person"] = None, e2_Group21: set["e2_AssignmentSubmission"] = None):
        self.Name = Name
        self.e2_Group = e2_Group
        self.e2_Group18 = e2_Group18 if e2_Group18 is not None else set()
        self.e2_Group21 = e2_Group21 if e2_Group21 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_Group21(self):
        return self.__e2_Group21

    @e2_Group21.setter
    def e2_Group21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Group__e2_Group21", None)
        self.__e2_Group21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_AssignmentSubmission22"):
                    opp_val = getattr(item, "e2_AssignmentSubmission22", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_AssignmentSubmission22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_AssignmentSubmission22"):
                    opp_val = getattr(item, "e2_AssignmentSubmission22", None)
                    
                    setattr(item, "e2_AssignmentSubmission22", self)
                    

    @property
    def e2_Group(self):
        return self.__e2_Group

    @e2_Group.setter
    def e2_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Group__e2_Group", None)
        self.__e2_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course13"):
                opp_val = getattr(old_value, "e2_Course13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course13"):
                opp_val = getattr(value, "e2_Course13", None)
                if opp_val is None:
                    setattr(value, "e2_Course13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Group18(self):
        return self.__e2_Group18

    @e2_Group18.setter
    def e2_Group18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Group__e2_Group18", None)
        self.__e2_Group18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person19"):
                    opp_val = getattr(item, "e2_Person19", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person19"):
                    opp_val = getattr(item, "e2_Person19", None)
                    
                    setattr(item, "e2_Person19", self)
                    

class e2_Course:

    def __init__(self, ID: str, Name: str, Credit: float, e2_Course: set["e2_Person"] = None, e2_Course5: set["e2_Person"] = None, e2_Course8: set["e2_Assingnment"] = None, e2_Course10: set["e2_Lecture"] = None, e2_Course13: set["e2_Group"] = None, e2_Course15: set["e2_Person"] = None, e2_Course33: "e2_University" = None):
        self.ID = ID
        self.Name = Name
        self.Credit = Credit
        self.e2_Course = e2_Course if e2_Course is not None else set()
        self.e2_Course5 = e2_Course5 if e2_Course5 is not None else set()
        self.e2_Course8 = e2_Course8 if e2_Course8 is not None else set()
        self.e2_Course10 = e2_Course10 if e2_Course10 is not None else set()
        self.e2_Course13 = e2_Course13 if e2_Course13 is not None else set()
        self.e2_Course15 = e2_Course15 if e2_Course15 is not None else set()
        self.e2_Course33 = e2_Course33
        
    @property
    def Credit(self) -> float:
        return self.__Credit

    @Credit.setter
    def Credit(self, Credit: float):
        self.__Credit = Credit

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_Course15(self):
        return self.__e2_Course15

    @e2_Course15.setter
    def e2_Course15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course15", None)
        self.__e2_Course15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person16"):
                    opp_val = getattr(item, "e2_Person16", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person16"):
                    opp_val = getattr(item, "e2_Person16", None)
                    
                    setattr(item, "e2_Person16", self)
                    

    @property
    def e2_Course(self):
        return self.__e2_Course

    @e2_Course.setter
    def e2_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course", None)
        self.__e2_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person3"):
                    opp_val = getattr(item, "e2_Person3", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person3"):
                    opp_val = getattr(item, "e2_Person3", None)
                    
                    setattr(item, "e2_Person3", self)
                    

    @property
    def e2_Course10(self):
        return self.__e2_Course10

    @e2_Course10.setter
    def e2_Course10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course10", None)
        self.__e2_Course10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Lecture11"):
                    opp_val = getattr(item, "e2_Lecture11", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Lecture11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Lecture11"):
                    opp_val = getattr(item, "e2_Lecture11", None)
                    
                    setattr(item, "e2_Lecture11", self)
                    

    @property
    def e2_Course8(self):
        return self.__e2_Course8

    @e2_Course8.setter
    def e2_Course8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course8", None)
        self.__e2_Course8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Assingnment"):
                    opp_val = getattr(item, "e2_Assingnment", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Assingnment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Assingnment"):
                    opp_val = getattr(item, "e2_Assingnment", None)
                    
                    setattr(item, "e2_Assingnment", self)
                    

    @property
    def e2_Course5(self):
        return self.__e2_Course5

    @e2_Course5.setter
    def e2_Course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course5", None)
        self.__e2_Course5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person6"):
                    opp_val = getattr(item, "e2_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person6"):
                    opp_val = getattr(item, "e2_Person6", None)
                    
                    setattr(item, "e2_Person6", self)
                    

    @property
    def e2_Course33(self):
        return self.__e2_Course33

    @e2_Course33.setter
    def e2_Course33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course33", None)
        self.__e2_Course33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_University32"):
                opp_val = getattr(old_value, "e2_University32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_University32"):
                opp_val = getattr(value, "e2_University32", None)
                if opp_val is None:
                    setattr(value, "e2_University32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Course13(self):
        return self.__e2_Course13

    @e2_Course13.setter
    def e2_Course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course13", None)
        self.__e2_Course13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Group"):
                    opp_val = getattr(item, "e2_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Group"):
                    opp_val = getattr(item, "e2_Group", None)
                    
                    setattr(item, "e2_Group", self)
                    

class e2_Assingnment:

    def __init__(self, Type: str, isMandatory: bool, Deadline: date, StartDate: date, Title: str, Content: str, e2_Assingnment25: "e2_AssignmentSubmission" = None, e2_Assingnment: "e2_Course" = None, e2_Assingnment36: "e2_LectureContent" = None):
        self.Type = Type
        self.isMandatory = isMandatory
        self.Deadline = Deadline
        self.StartDate = StartDate
        self.Title = Title
        self.Content = Content
        self.e2_Assingnment25 = e2_Assingnment25
        self.e2_Assingnment = e2_Assingnment
        self.e2_Assingnment36 = e2_Assingnment36
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def Content(self) -> str:
        return self.__Content

    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content

    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Deadline(self) -> date:
        return self.__Deadline

    @Deadline.setter
    def Deadline(self, Deadline: date):
        self.__Deadline = Deadline

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def StartDate(self) -> date:
        return self.__StartDate

    @StartDate.setter
    def StartDate(self, StartDate: date):
        self.__StartDate = StartDate

    @property
    def e2_Assingnment(self):
        return self.__e2_Assingnment

    @e2_Assingnment.setter
    def e2_Assingnment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment", None)
        self.__e2_Assingnment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course8"):
                opp_val = getattr(old_value, "e2_Course8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course8"):
                opp_val = getattr(value, "e2_Course8", None)
                if opp_val is None:
                    setattr(value, "e2_Course8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Assingnment36(self):
        return self.__e2_Assingnment36

    @e2_Assingnment36.setter
    def e2_Assingnment36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment36", None)
        self.__e2_Assingnment36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_LectureContent35"):
                opp_val = getattr(old_value, "e2_LectureContent35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_LectureContent35"):
                opp_val = getattr(value, "e2_LectureContent35", None)
                if opp_val is None:
                    setattr(value, "e2_LectureContent35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Assingnment25(self):
        return self.__e2_Assingnment25

    @e2_Assingnment25.setter
    def e2_Assingnment25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment25", None)
        self.__e2_Assingnment25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_AssignmentSubmission24"):
                opp_val = getattr(old_value, "e2_AssignmentSubmission24", None)
                if opp_val == self:
                    setattr(old_value, "e2_AssignmentSubmission24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_AssignmentSubmission24"):
                opp_val = getattr(value, "e2_AssignmentSubmission24", None)
                setattr(value, "e2_AssignmentSubmission24", self)

class e2_LectureContent:

    def __init__(self, Type: str, Material: str, e2_LectureContent: "e2_Lecture" = None, e2_LectureContent35: set["e2_Assingnment"] = None):
        self.Type = Type
        self.Material = Material
        self.e2_LectureContent = e2_LectureContent
        self.e2_LectureContent35 = e2_LectureContent35 if e2_LectureContent35 is not None else set()
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Material(self) -> str:
        return self.__Material

    @Material.setter
    def Material(self, Material: str):
        self.__Material = Material

    @property
    def e2_LectureContent(self):
        return self.__e2_LectureContent

    @e2_LectureContent.setter
    def e2_LectureContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_LectureContent__e2_LectureContent", None)
        self.__e2_LectureContent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Lecture"):
                opp_val = getattr(old_value, "e2_Lecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Lecture"):
                opp_val = getattr(value, "e2_Lecture", None)
                if opp_val is None:
                    setattr(value, "e2_Lecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_LectureContent35(self):
        return self.__e2_LectureContent35

    @e2_LectureContent35.setter
    def e2_LectureContent35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_LectureContent__e2_LectureContent35", None)
        self.__e2_LectureContent35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Assingnment36"):
                    opp_val = getattr(item, "e2_Assingnment36", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Assingnment36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Assingnment36"):
                    opp_val = getattr(item, "e2_Assingnment36", None)
                    
                    setattr(item, "e2_Assingnment36", self)
                    

class e2_Lecture:

    def __init__(self, Date: date, Length: int, e2_Lecture: set["e2_LectureContent"] = None, e2_Lecture11: "e2_Course" = None):
        self.Date = Date
        self.Length = Length
        self.e2_Lecture = e2_Lecture if e2_Lecture is not None else set()
        self.e2_Lecture11 = e2_Lecture11
        
    @property
    def Date(self) -> date:
        return self.__Date

    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def Length(self) -> int:
        return self.__Length

    @Length.setter
    def Length(self, Length: int):
        self.__Length = Length

    @property
    def e2_Lecture(self):
        return self.__e2_Lecture

    @e2_Lecture.setter
    def e2_Lecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Lecture__e2_Lecture", None)
        self.__e2_Lecture = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_LectureContent"):
                    opp_val = getattr(item, "e2_LectureContent", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_LectureContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_LectureContent"):
                    opp_val = getattr(item, "e2_LectureContent", None)
                    
                    setattr(item, "e2_LectureContent", self)
                    

    @property
    def e2_Lecture11(self):
        return self.__e2_Lecture11

    @e2_Lecture11.setter
    def e2_Lecture11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Lecture__e2_Lecture11", None)
        self.__e2_Lecture11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course10"):
                opp_val = getattr(old_value, "e2_Course10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course10"):
                opp_val = getattr(value, "e2_Course10", None)
                if opp_val is None:
                    setattr(value, "e2_Course10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class e2_AssignmentSubmission:

    def __init__(self, Comments: str, Assessment: int, e2_AssignmentSubmission: "e2_Person" = None, e2_AssignmentSubmission24: "e2_Assingnment" = None, e2_AssignmentSubmission27: "e2_Person" = None, e2_AssignmentSubmission22: "e2_Group" = None):
        self.Comments = Comments
        self.Assessment = Assessment
        self.e2_AssignmentSubmission = e2_AssignmentSubmission
        self.e2_AssignmentSubmission24 = e2_AssignmentSubmission24
        self.e2_AssignmentSubmission27 = e2_AssignmentSubmission27
        self.e2_AssignmentSubmission22 = e2_AssignmentSubmission22
        
    @property
    def Comments(self) -> str:
        return self.__Comments

    @Comments.setter
    def Comments(self, Comments: str):
        self.__Comments = Comments

    @property
    def Assessment(self) -> int:
        return self.__Assessment

    @Assessment.setter
    def Assessment(self, Assessment: int):
        self.__Assessment = Assessment

    @property
    def e2_AssignmentSubmission22(self):
        return self.__e2_AssignmentSubmission22

    @e2_AssignmentSubmission22.setter
    def e2_AssignmentSubmission22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission22", None)
        self.__e2_AssignmentSubmission22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Group21"):
                opp_val = getattr(old_value, "e2_Group21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Group21"):
                opp_val = getattr(value, "e2_Group21", None)
                if opp_val is None:
                    setattr(value, "e2_Group21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_AssignmentSubmission24(self):
        return self.__e2_AssignmentSubmission24

    @e2_AssignmentSubmission24.setter
    def e2_AssignmentSubmission24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission24", None)
        self.__e2_AssignmentSubmission24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Assingnment25"):
                opp_val = getattr(old_value, "e2_Assingnment25", None)
                if opp_val == self:
                    setattr(old_value, "e2_Assingnment25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Assingnment25"):
                opp_val = getattr(value, "e2_Assingnment25", None)
                setattr(value, "e2_Assingnment25", self)

    @property
    def e2_AssignmentSubmission27(self):
        return self.__e2_AssignmentSubmission27

    @e2_AssignmentSubmission27.setter
    def e2_AssignmentSubmission27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission27", None)
        self.__e2_AssignmentSubmission27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Person28"):
                opp_val = getattr(old_value, "e2_Person28", None)
                if opp_val == self:
                    setattr(old_value, "e2_Person28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Person28"):
                opp_val = getattr(value, "e2_Person28", None)
                setattr(value, "e2_Person28", self)

    @property
    def e2_AssignmentSubmission(self):
        return self.__e2_AssignmentSubmission

    @e2_AssignmentSubmission.setter
    def e2_AssignmentSubmission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission", None)
        self.__e2_AssignmentSubmission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Person"):
                opp_val = getattr(old_value, "e2_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Person"):
                opp_val = getattr(value, "e2_Person", None)
                if opp_val is None:
                    setattr(value, "e2_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class e2_Person:

    def __init__(self, Name: str, e2_Person: set["e2_AssignmentSubmission"] = None, e2_Person3: "e2_Course" = None, e2_Person6: "e2_Course" = None, e2_Person28: "e2_AssignmentSubmission" = None, e2_Person16: "e2_Course" = None, e2_Person19: "e2_Group" = None, e2_Person30: "e2_University" = None):
        self.Name = Name
        self.e2_Person = e2_Person if e2_Person is not None else set()
        self.e2_Person3 = e2_Person3
        self.e2_Person6 = e2_Person6
        self.e2_Person28 = e2_Person28
        self.e2_Person16 = e2_Person16
        self.e2_Person19 = e2_Person19
        self.e2_Person30 = e2_Person30
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_Person19(self):
        return self.__e2_Person19

    @e2_Person19.setter
    def e2_Person19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person19", None)
        self.__e2_Person19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Group18"):
                opp_val = getattr(old_value, "e2_Group18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Group18"):
                opp_val = getattr(value, "e2_Group18", None)
                if opp_val is None:
                    setattr(value, "e2_Group18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person16(self):
        return self.__e2_Person16

    @e2_Person16.setter
    def e2_Person16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person16", None)
        self.__e2_Person16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course15"):
                opp_val = getattr(old_value, "e2_Course15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course15"):
                opp_val = getattr(value, "e2_Course15", None)
                if opp_val is None:
                    setattr(value, "e2_Course15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person30(self):
        return self.__e2_Person30

    @e2_Person30.setter
    def e2_Person30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person30", None)
        self.__e2_Person30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_University"):
                opp_val = getattr(old_value, "e2_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_University"):
                opp_val = getattr(value, "e2_University", None)
                if opp_val is None:
                    setattr(value, "e2_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person28(self):
        return self.__e2_Person28

    @e2_Person28.setter
    def e2_Person28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person28", None)
        self.__e2_Person28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_AssignmentSubmission27"):
                opp_val = getattr(old_value, "e2_AssignmentSubmission27", None)
                if opp_val == self:
                    setattr(old_value, "e2_AssignmentSubmission27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_AssignmentSubmission27"):
                opp_val = getattr(value, "e2_AssignmentSubmission27", None)
                setattr(value, "e2_AssignmentSubmission27", self)

    @property
    def e2_Person(self):
        return self.__e2_Person

    @e2_Person.setter
    def e2_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person", None)
        self.__e2_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_AssignmentSubmission"):
                    opp_val = getattr(item, "e2_AssignmentSubmission", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_AssignmentSubmission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_AssignmentSubmission"):
                    opp_val = getattr(item, "e2_AssignmentSubmission", None)
                    
                    setattr(item, "e2_AssignmentSubmission", self)
                    

    @property
    def e2_Person6(self):
        return self.__e2_Person6

    @e2_Person6.setter
    def e2_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person6", None)
        self.__e2_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course5"):
                opp_val = getattr(old_value, "e2_Course5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course5"):
                opp_val = getattr(value, "e2_Course5", None)
                if opp_val is None:
                    setattr(value, "e2_Course5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person3(self):
        return self.__e2_Person3

    @e2_Person3.setter
    def e2_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person3", None)
        self.__e2_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course"):
                opp_val = getattr(old_value, "e2_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course"):
                opp_val = getattr(value, "e2_Course", None)
                if opp_val is None:
                    setattr(value, "e2_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
