from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Courses_Answer:

    def __init__(self, id: int, text: str, pass: bool, Courses_Answer: "Courses_Person" = None, Courses_Answer7: "Courses_Assignment" = None):
        self.id = id
        self.text = text
        self.pass = pass
        self.Courses_Answer = Courses_Answer
        self.Courses_Answer7 = Courses_Answer7
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def pass(self) -> bool:
        return self.__pass

    @pass.setter
    def pass(self, pass: bool):
        self.__pass = pass

    @property
    def Courses_Answer(self):
        return self.__Courses_Answer

    @Courses_Answer.setter
    def Courses_Answer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Answer__Courses_Answer", None)
        self.__Courses_Answer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Courses_Person4"):
                opp_val = getattr(old_value, "Courses_Person4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Courses_Person4"):
                opp_val = getattr(value, "Courses_Person4", None)
                if opp_val is None:
                    setattr(value, "Courses_Person4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Courses_Answer7(self):
        return self.__Courses_Answer7

    @Courses_Answer7.setter
    def Courses_Answer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Answer__Courses_Answer7", None)
        self.__Courses_Answer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Courses_Assignment6"):
                opp_val = getattr(old_value, "Courses_Assignment6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Courses_Assignment6"):
                opp_val = getattr(value, "Courses_Assignment6", None)
                if opp_val is None:
                    setattr(value, "Courses_Assignment6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Courses_Person:

    def __init__(self, name: str, id: int, role: str, Courses_Person: "Courses_Course" = None, Courses_Person4: set["Courses_Answer"] = None):
        self.name = name
        self.id = id
        self.role = role
        self.Courses_Person = Courses_Person
        self.Courses_Person4 = Courses_Person4 if Courses_Person4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Courses_Person4(self):
        return self.__Courses_Person4

    @Courses_Person4.setter
    def Courses_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Person__Courses_Person4", None)
        self.__Courses_Person4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Courses_Answer"):
                    opp_val = getattr(item, "Courses_Answer", None)
                    
                    if opp_val == self:
                        setattr(item, "Courses_Answer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Courses_Answer"):
                    opp_val = getattr(item, "Courses_Answer", None)
                    
                    setattr(item, "Courses_Answer", self)
                    

    @property
    def Courses_Person(self):
        return self.__Courses_Person

    @Courses_Person.setter
    def Courses_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Person__Courses_Person", None)
        self.__Courses_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Courses_Course"):
                opp_val = getattr(old_value, "Courses_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Courses_Course"):
                opp_val = getattr(value, "Courses_Course", None)
                if opp_val is None:
                    setattr(value, "Courses_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Courses_Course:

    def __init__(self, name: str, id: str, credit: float, Courses_Course2: set["Courses_Assignment"] = None, Courses_Course: set["Courses_Person"] = None):
        self.name = name
        self.id = id
        self.credit = credit
        self.Courses_Course2 = Courses_Course2 if Courses_Course2 is not None else set()
        self.Courses_Course = Courses_Course if Courses_Course is not None else set()
        
    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Courses_Course2(self):
        return self.__Courses_Course2

    @Courses_Course2.setter
    def Courses_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Course__Courses_Course2", None)
        self.__Courses_Course2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Courses_Assignment"):
                    opp_val = getattr(item, "Courses_Assignment", None)
                    
                    if opp_val == self:
                        setattr(item, "Courses_Assignment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Courses_Assignment"):
                    opp_val = getattr(item, "Courses_Assignment", None)
                    
                    setattr(item, "Courses_Assignment", self)
                    

    @property
    def Courses_Course(self):
        return self.__Courses_Course

    @Courses_Course.setter
    def Courses_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Course__Courses_Course", None)
        self.__Courses_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Courses_Person"):
                    opp_val = getattr(item, "Courses_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Courses_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Courses_Person"):
                    opp_val = getattr(item, "Courses_Person", None)
                    
                    setattr(item, "Courses_Person", self)
                    

class Courses_Assignment:

    def __init__(self, description: str, mandatory: bool, name: str, Courses_Assignment: "Courses_Course" = None, Courses_Assignment6: set["Courses_Answer"] = None):
        self.description = description
        self.mandatory = mandatory
        self.name = name
        self.Courses_Assignment = Courses_Assignment
        self.Courses_Assignment6 = Courses_Assignment6 if Courses_Assignment6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Courses_Assignment(self):
        return self.__Courses_Assignment

    @Courses_Assignment.setter
    def Courses_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Assignment__Courses_Assignment", None)
        self.__Courses_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Courses_Course2"):
                opp_val = getattr(old_value, "Courses_Course2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Courses_Course2"):
                opp_val = getattr(value, "Courses_Course2", None)
                if opp_val is None:
                    setattr(value, "Courses_Course2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Courses_Assignment6(self):
        return self.__Courses_Assignment6

    @Courses_Assignment6.setter
    def Courses_Assignment6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Courses_Assignment__Courses_Assignment6", None)
        self.__Courses_Assignment6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Courses_Answer7"):
                    opp_val = getattr(item, "Courses_Answer7", None)
                    
                    if opp_val == self:
                        setattr(item, "Courses_Answer7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Courses_Answer7"):
                    opp_val = getattr(item, "Courses_Answer7", None)
                    
                    setattr(item, "Courses_Answer7", self)
                    
