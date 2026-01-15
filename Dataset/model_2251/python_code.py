from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class e2_EClass0:

    pass
class e2_University:

    def __init__(self, Name: str, e2_University: set["e2_Person"] = None, e2_University39: set["e2_Course"] = None):
        self.Name = Name
        self.e2_University = e2_University if e2_University is not None else set()
        self.e2_University39 = e2_University39 if e2_University39 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
                if hasattr(item, "e2_Person37"):
                    opp_val = getattr(item, "e2_Person37", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person37"):
                    opp_val = getattr(item, "e2_Person37", None)
                    
                    setattr(item, "e2_Person37", self)
                    

    @property
    def e2_University39(self):
        return self.__e2_University39

    @e2_University39.setter
    def e2_University39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_University__e2_University39", None)
        self.__e2_University39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Course40"):
                    opp_val = getattr(item, "e2_Course40", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Course40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Course40"):
                    opp_val = getattr(item, "e2_Course40", None)
                    
                    setattr(item, "e2_Course40", self)
                    

class e2_Goal:

    def __init__(self, GoalID: str, GoalText: str, e2_Goal: "e2_Course" = None, e2_Goal45: set["e2_SubGoal"] = None):
        self.GoalID = GoalID
        self.GoalText = GoalText
        self.e2_Goal = e2_Goal
        self.e2_Goal45 = e2_Goal45 if e2_Goal45 is not None else set()
        
    @property
    def GoalText(self) -> str:
        return self.__GoalText

    @GoalText.setter
    def GoalText(self, GoalText: str):
        self.__GoalText = GoalText

    @property
    def GoalID(self) -> str:
        return self.__GoalID

    @GoalID.setter
    def GoalID(self, GoalID: str):
        self.__GoalID = GoalID

    @property
    def e2_Goal(self):
        return self.__e2_Goal

    @e2_Goal.setter
    def e2_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Goal__e2_Goal", None)
        self.__e2_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course23"):
                opp_val = getattr(old_value, "e2_Course23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course23"):
                opp_val = getattr(value, "e2_Course23", None)
                if opp_val is None:
                    setattr(value, "e2_Course23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Goal45(self):
        return self.__e2_Goal45

    @e2_Goal45.setter
    def e2_Goal45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Goal__e2_Goal45", None)
        self.__e2_Goal45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_SubGoal46"):
                    opp_val = getattr(item, "e2_SubGoal46", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_SubGoal46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_SubGoal46"):
                    opp_val = getattr(item, "e2_SubGoal46", None)
                    
                    setattr(item, "e2_SubGoal46", self)
                    

class e2_Group:

    def __init__(self, Name: str, e2_Group: "e2_Course" = None, e2_Group25: set["e2_Person"] = None, e2_Group28: set["e2_AssignmentSubmission"] = None):
        self.Name = Name
        self.e2_Group = e2_Group
        self.e2_Group25 = e2_Group25 if e2_Group25 is not None else set()
        self.e2_Group28 = e2_Group28 if e2_Group28 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_Group28(self):
        return self.__e2_Group28

    @e2_Group28.setter
    def e2_Group28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Group__e2_Group28", None)
        self.__e2_Group28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_AssignmentSubmission29"):
                    opp_val = getattr(item, "e2_AssignmentSubmission29", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_AssignmentSubmission29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_AssignmentSubmission29"):
                    opp_val = getattr(item, "e2_AssignmentSubmission29", None)
                    
                    setattr(item, "e2_AssignmentSubmission29", self)
                    

    @property
    def e2_Group25(self):
        return self.__e2_Group25

    @e2_Group25.setter
    def e2_Group25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Group__e2_Group25", None)
        self.__e2_Group25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person26"):
                    opp_val = getattr(item, "e2_Person26", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person26"):
                    opp_val = getattr(item, "e2_Person26", None)
                    
                    setattr(item, "e2_Person26", self)
                    

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
            if hasattr(old_value, "e2_Course18"):
                opp_val = getattr(old_value, "e2_Course18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course18"):
                opp_val = getattr(value, "e2_Course18", None)
                if opp_val is None:
                    setattr(value, "e2_Course18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class e2_Assingnment:

    def __init__(self, isMandatory: bool, Deadline: date, StartDate: date, Title: str, Content: str, Type: str, e2_Assingnment: set["e2_SubGoal"] = None, e2_Assingnment13: "e2_Course" = None, e2_Assingnment32: "e2_AssignmentSubmission" = None, e2_Assingnment43: "e2_LectureContent" = None):
        self.isMandatory = isMandatory
        self.Deadline = Deadline
        self.StartDate = StartDate
        self.Title = Title
        self.Content = Content
        self.Type = Type
        self.e2_Assingnment = e2_Assingnment if e2_Assingnment is not None else set()
        self.e2_Assingnment13 = e2_Assingnment13
        self.e2_Assingnment32 = e2_Assingnment32
        self.e2_Assingnment43 = e2_Assingnment43
        
    @property
    def Deadline(self) -> date:
        return self.__Deadline

    @Deadline.setter
    def Deadline(self, Deadline: date):
        self.__Deadline = Deadline

    @property
    def StartDate(self) -> date:
        return self.__StartDate

    @StartDate.setter
    def StartDate(self, StartDate: date):
        self.__StartDate = StartDate

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

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
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

    @property
    def e2_Assingnment(self):
        return self.__e2_Assingnment

    @e2_Assingnment.setter
    def e2_Assingnment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment", None)
        self.__e2_Assingnment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_SubGoal5"):
                    opp_val = getattr(item, "e2_SubGoal5", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_SubGoal5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_SubGoal5"):
                    opp_val = getattr(item, "e2_SubGoal5", None)
                    
                    setattr(item, "e2_SubGoal5", self)
                    

    @property
    def e2_Assingnment13(self):
        return self.__e2_Assingnment13

    @e2_Assingnment13.setter
    def e2_Assingnment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment13", None)
        self.__e2_Assingnment13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course12"):
                opp_val = getattr(old_value, "e2_Course12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course12"):
                opp_val = getattr(value, "e2_Course12", None)
                if opp_val is None:
                    setattr(value, "e2_Course12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Assingnment43(self):
        return self.__e2_Assingnment43

    @e2_Assingnment43.setter
    def e2_Assingnment43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment43", None)
        self.__e2_Assingnment43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_LectureContent42"):
                opp_val = getattr(old_value, "e2_LectureContent42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_LectureContent42"):
                opp_val = getattr(value, "e2_LectureContent42", None)
                if opp_val is None:
                    setattr(value, "e2_LectureContent42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Assingnment32(self):
        return self.__e2_Assingnment32

    @e2_Assingnment32.setter
    def e2_Assingnment32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Assingnment__e2_Assingnment32", None)
        self.__e2_Assingnment32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_AssignmentSubmission31"):
                opp_val = getattr(old_value, "e2_AssignmentSubmission31", None)
                if opp_val == self:
                    setattr(old_value, "e2_AssignmentSubmission31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_AssignmentSubmission31"):
                opp_val = getattr(value, "e2_AssignmentSubmission31", None)
                setattr(value, "e2_AssignmentSubmission31", self)

class e2_AssignmentSubmission:

    def __init__(self, Comments: str, assessment: int, e2_AssignmentSubmission: "e2_Person" = None, e2_AssignmentSubmission31: "e2_Assingnment" = None, e2_AssignmentSubmission34: "e2_Person" = None, e2_AssignmentSubmission29: "e2_Group" = None):
        self.Comments = Comments
        self.assessment = assessment
        self.e2_AssignmentSubmission = e2_AssignmentSubmission
        self.e2_AssignmentSubmission31 = e2_AssignmentSubmission31
        self.e2_AssignmentSubmission34 = e2_AssignmentSubmission34
        self.e2_AssignmentSubmission29 = e2_AssignmentSubmission29
        
    @property
    def Comments(self) -> str:
        return self.__Comments

    @Comments.setter
    def Comments(self, Comments: str):
        self.__Comments = Comments

    @property
    def assessment(self) -> int:
        return self.__assessment

    @assessment.setter
    def assessment(self, assessment: int):
        self.__assessment = assessment

    @property
    def e2_AssignmentSubmission34(self):
        return self.__e2_AssignmentSubmission34

    @e2_AssignmentSubmission34.setter
    def e2_AssignmentSubmission34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission34", None)
        self.__e2_AssignmentSubmission34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Person35"):
                opp_val = getattr(old_value, "e2_Person35", None)
                if opp_val == self:
                    setattr(old_value, "e2_Person35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Person35"):
                opp_val = getattr(value, "e2_Person35", None)
                setattr(value, "e2_Person35", self)

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

    @property
    def e2_AssignmentSubmission29(self):
        return self.__e2_AssignmentSubmission29

    @e2_AssignmentSubmission29.setter
    def e2_AssignmentSubmission29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission29", None)
        self.__e2_AssignmentSubmission29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Group28"):
                opp_val = getattr(old_value, "e2_Group28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Group28"):
                opp_val = getattr(value, "e2_Group28", None)
                if opp_val is None:
                    setattr(value, "e2_Group28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_AssignmentSubmission31(self):
        return self.__e2_AssignmentSubmission31

    @e2_AssignmentSubmission31.setter
    def e2_AssignmentSubmission31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_AssignmentSubmission__e2_AssignmentSubmission31", None)
        self.__e2_AssignmentSubmission31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Assingnment32"):
                opp_val = getattr(old_value, "e2_Assingnment32", None)
                if opp_val == self:
                    setattr(old_value, "e2_Assingnment32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Assingnment32"):
                opp_val = getattr(value, "e2_Assingnment32", None)
                setattr(value, "e2_Assingnment32", self)

class e2_Person:

    def __init__(self, Name: str, e2_Person7: "e2_Course" = None, e2_Person10: "e2_Course" = None, e2_Person: set["e2_AssignmentSubmission"] = None, e2_Person35: "e2_AssignmentSubmission" = None, e2_Person21: "e2_Course" = None, e2_Person26: "e2_Group" = None, e2_Person37: "e2_University" = None):
        self.Name = Name
        self.e2_Person7 = e2_Person7
        self.e2_Person10 = e2_Person10
        self.e2_Person = e2_Person if e2_Person is not None else set()
        self.e2_Person35 = e2_Person35
        self.e2_Person21 = e2_Person21
        self.e2_Person26 = e2_Person26
        self.e2_Person37 = e2_Person37
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def e2_Person26(self):
        return self.__e2_Person26

    @e2_Person26.setter
    def e2_Person26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person26", None)
        self.__e2_Person26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Group25"):
                opp_val = getattr(old_value, "e2_Group25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Group25"):
                opp_val = getattr(value, "e2_Group25", None)
                if opp_val is None:
                    setattr(value, "e2_Group25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person35(self):
        return self.__e2_Person35

    @e2_Person35.setter
    def e2_Person35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person35", None)
        self.__e2_Person35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_AssignmentSubmission34"):
                opp_val = getattr(old_value, "e2_AssignmentSubmission34", None)
                if opp_val == self:
                    setattr(old_value, "e2_AssignmentSubmission34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_AssignmentSubmission34"):
                opp_val = getattr(value, "e2_AssignmentSubmission34", None)
                setattr(value, "e2_AssignmentSubmission34", self)

    @property
    def e2_Person21(self):
        return self.__e2_Person21

    @e2_Person21.setter
    def e2_Person21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person21", None)
        self.__e2_Person21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course20"):
                opp_val = getattr(old_value, "e2_Course20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course20"):
                opp_val = getattr(value, "e2_Course20", None)
                if opp_val is None:
                    setattr(value, "e2_Course20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def e2_Person10(self):
        return self.__e2_Person10

    @e2_Person10.setter
    def e2_Person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person10", None)
        self.__e2_Person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Course9"):
                opp_val = getattr(old_value, "e2_Course9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Course9"):
                opp_val = getattr(value, "e2_Course9", None)
                if opp_val is None:
                    setattr(value, "e2_Course9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Person7(self):
        return self.__e2_Person7

    @e2_Person7.setter
    def e2_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person7", None)
        self.__e2_Person7 = value
        
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

    @property
    def e2_Person37(self):
        return self.__e2_Person37

    @e2_Person37.setter
    def e2_Person37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Person__e2_Person37", None)
        self.__e2_Person37 = value
        
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

class e2_SubGoal:

    def __init__(self, GoalID: str, GoalText: str, e2_SubGoal5: "e2_Assingnment" = None, e2_SubGoal: "e2_Lecture" = None, e2_SubGoal46: "e2_Goal" = None):
        self.GoalID = GoalID
        self.GoalText = GoalText
        self.e2_SubGoal5 = e2_SubGoal5
        self.e2_SubGoal = e2_SubGoal
        self.e2_SubGoal46 = e2_SubGoal46
        
    @property
    def GoalID(self) -> str:
        return self.__GoalID

    @GoalID.setter
    def GoalID(self, GoalID: str):
        self.__GoalID = GoalID

    @property
    def GoalText(self) -> str:
        return self.__GoalText

    @GoalText.setter
    def GoalText(self, GoalText: str):
        self.__GoalText = GoalText

    @property
    def e2_SubGoal(self):
        return self.__e2_SubGoal

    @e2_SubGoal.setter
    def e2_SubGoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_SubGoal__e2_SubGoal", None)
        self.__e2_SubGoal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Lecture2"):
                opp_val = getattr(old_value, "e2_Lecture2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Lecture2"):
                opp_val = getattr(value, "e2_Lecture2", None)
                if opp_val is None:
                    setattr(value, "e2_Lecture2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_SubGoal5(self):
        return self.__e2_SubGoal5

    @e2_SubGoal5.setter
    def e2_SubGoal5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_SubGoal__e2_SubGoal5", None)
        self.__e2_SubGoal5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Assingnment"):
                opp_val = getattr(old_value, "e2_Assingnment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Assingnment"):
                opp_val = getattr(value, "e2_Assingnment", None)
                if opp_val is None:
                    setattr(value, "e2_Assingnment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_SubGoal46(self):
        return self.__e2_SubGoal46

    @e2_SubGoal46.setter
    def e2_SubGoal46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_SubGoal__e2_SubGoal46", None)
        self.__e2_SubGoal46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_Goal45"):
                opp_val = getattr(old_value, "e2_Goal45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_Goal45"):
                opp_val = getattr(value, "e2_Goal45", None)
                if opp_val is None:
                    setattr(value, "e2_Goal45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class e2_LectureContent:

    def __init__(self, Type: str, Material: str, e2_LectureContent: "e2_Lecture" = None, e2_LectureContent42: set["e2_Assingnment"] = None):
        self.Type = Type
        self.Material = Material
        self.e2_LectureContent = e2_LectureContent
        self.e2_LectureContent42 = e2_LectureContent42 if e2_LectureContent42 is not None else set()
        
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
    def e2_LectureContent42(self):
        return self.__e2_LectureContent42

    @e2_LectureContent42.setter
    def e2_LectureContent42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_LectureContent__e2_LectureContent42", None)
        self.__e2_LectureContent42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Assingnment43"):
                    opp_val = getattr(item, "e2_Assingnment43", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Assingnment43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Assingnment43"):
                    opp_val = getattr(item, "e2_Assingnment43", None)
                    
                    setattr(item, "e2_Assingnment43", self)
                    

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

class e2_Lecture:

    def __init__(self, Date: date, length: int, e2_Lecture: set["e2_LectureContent"] = None, e2_Lecture2: set["e2_SubGoal"] = None, e2_Lecture16: "e2_Course" = None):
        self.Date = Date
        self.length = length
        self.e2_Lecture = e2_Lecture if e2_Lecture is not None else set()
        self.e2_Lecture2 = e2_Lecture2 if e2_Lecture2 is not None else set()
        self.e2_Lecture16 = e2_Lecture16
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def Date(self) -> date:
        return self.__Date

    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def e2_Lecture2(self):
        return self.__e2_Lecture2

    @e2_Lecture2.setter
    def e2_Lecture2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Lecture__e2_Lecture2", None)
        self.__e2_Lecture2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_SubGoal"):
                    opp_val = getattr(item, "e2_SubGoal", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_SubGoal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_SubGoal"):
                    opp_val = getattr(item, "e2_SubGoal", None)
                    
                    setattr(item, "e2_SubGoal", self)
                    

    @property
    def e2_Lecture16(self):
        return self.__e2_Lecture16

    @e2_Lecture16.setter
    def e2_Lecture16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Lecture__e2_Lecture16", None)
        self.__e2_Lecture16 = value
        
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
                    

class e2_Course:

    def __init__(self, ID: str, Name: str, credit: float, e2_Course: set["e2_Person"] = None, e2_Course9: set["e2_Person"] = None, e2_Course12: set["e2_Assingnment"] = None, e2_Course15: set["e2_Lecture"] = None, e2_Course18: set["e2_Group"] = None, e2_Course20: set["e2_Person"] = None, e2_Course23: set["e2_Goal"] = None, e2_Course40: "e2_University" = None):
        self.ID = ID
        self.Name = Name
        self.credit = credit
        self.e2_Course = e2_Course if e2_Course is not None else set()
        self.e2_Course9 = e2_Course9 if e2_Course9 is not None else set()
        self.e2_Course12 = e2_Course12 if e2_Course12 is not None else set()
        self.e2_Course15 = e2_Course15 if e2_Course15 is not None else set()
        self.e2_Course18 = e2_Course18 if e2_Course18 is not None else set()
        self.e2_Course20 = e2_Course20 if e2_Course20 is not None else set()
        self.e2_Course23 = e2_Course23 if e2_Course23 is not None else set()
        self.e2_Course40 = e2_Course40
        
    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

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
                if hasattr(item, "e2_Person7"):
                    opp_val = getattr(item, "e2_Person7", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person7"):
                    opp_val = getattr(item, "e2_Person7", None)
                    
                    setattr(item, "e2_Person7", self)
                    

    @property
    def e2_Course18(self):
        return self.__e2_Course18

    @e2_Course18.setter
    def e2_Course18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course18", None)
        self.__e2_Course18 = value if value is not None else set()
        
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
                if hasattr(item, "e2_Lecture16"):
                    opp_val = getattr(item, "e2_Lecture16", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Lecture16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Lecture16"):
                    opp_val = getattr(item, "e2_Lecture16", None)
                    
                    setattr(item, "e2_Lecture16", self)
                    

    @property
    def e2_Course20(self):
        return self.__e2_Course20

    @e2_Course20.setter
    def e2_Course20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course20", None)
        self.__e2_Course20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person21"):
                    opp_val = getattr(item, "e2_Person21", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person21"):
                    opp_val = getattr(item, "e2_Person21", None)
                    
                    setattr(item, "e2_Person21", self)
                    

    @property
    def e2_Course12(self):
        return self.__e2_Course12

    @e2_Course12.setter
    def e2_Course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course12", None)
        self.__e2_Course12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Assingnment13"):
                    opp_val = getattr(item, "e2_Assingnment13", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Assingnment13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Assingnment13"):
                    opp_val = getattr(item, "e2_Assingnment13", None)
                    
                    setattr(item, "e2_Assingnment13", self)
                    

    @property
    def e2_Course40(self):
        return self.__e2_Course40

    @e2_Course40.setter
    def e2_Course40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course40", None)
        self.__e2_Course40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e2_University39"):
                opp_val = getattr(old_value, "e2_University39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e2_University39"):
                opp_val = getattr(value, "e2_University39", None)
                if opp_val is None:
                    setattr(value, "e2_University39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e2_Course9(self):
        return self.__e2_Course9

    @e2_Course9.setter
    def e2_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course9", None)
        self.__e2_Course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Person10"):
                    opp_val = getattr(item, "e2_Person10", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Person10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Person10"):
                    opp_val = getattr(item, "e2_Person10", None)
                    
                    setattr(item, "e2_Person10", self)
                    

    @property
    def e2_Course23(self):
        return self.__e2_Course23

    @e2_Course23.setter
    def e2_Course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e2_Course__e2_Course23", None)
        self.__e2_Course23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e2_Goal"):
                    opp_val = getattr(item, "e2_Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "e2_Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e2_Goal"):
                    opp_val = getattr(item, "e2_Goal", None)
                    
                    setattr(item, "e2_Goal", self)
                    
