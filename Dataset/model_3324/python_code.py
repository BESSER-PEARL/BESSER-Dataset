from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sample_Register:

    def __init__(self, Name: str, sample_Register: set["sample_Story"] = None):
        self.Name = Name
        self.sample_Register = sample_Register if sample_Register is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def sample_Register(self):
        return self.__sample_Register

    @sample_Register.setter
    def sample_Register(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Register__sample_Register", None)
        self.__sample_Register = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Story20"):
                    opp_val = getattr(item, "sample_Story20", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Story20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Story20"):
                    opp_val = getattr(item, "sample_Story20", None)
                    
                    setattr(item, "sample_Story20", self)
                    

class sample_Annotation:

    def __init__(self, Text: str, Type: str, sample_Annotation: "sample_Sentence" = None):
        self.Text = Text
        self.Type = Type
        self.sample_Annotation = sample_Annotation
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def sample_Annotation(self):
        return self.__sample_Annotation

    @sample_Annotation.setter
    def sample_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Annotation__sample_Annotation", None)
        self.__sample_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Sentence18"):
                opp_val = getattr(old_value, "sample_Sentence18", None)
                if opp_val == self:
                    setattr(old_value, "sample_Sentence18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Sentence18"):
                opp_val = getattr(value, "sample_Sentence18", None)
                setattr(value, "sample_Sentence18", self)

class sample_Variable:

    def __init__(self, Name: str, Type: str, Value: str, sample_Variable: "sample_Sentence" = None):
        self.Name = Name
        self.Type = Type
        self.Value = Value
        self.sample_Variable = sample_Variable
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def sample_Variable(self):
        return self.__sample_Variable

    @sample_Variable.setter
    def sample_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Variable__sample_Variable", None)
        self.__sample_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Sentence16"):
                opp_val = getattr(old_value, "sample_Sentence16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Sentence16"):
                opp_val = getattr(value, "sample_Sentence16", None)
                if opp_val is None:
                    setattr(value, "sample_Sentence16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Given:

    pass
class sample_When:

    pass
class sample_Sentence:

    def __init__(self, Text: str, sample_Sentence: "sample_When" = None, sample_Sentence16: set["sample_Variable"] = None, sample_Sentence18: "sample_Annotation" = None, sample_Sentence11: "sample_Given" = None, sample_Sentence14: "sample_Then" = None):
        self.Text = Text
        self.sample_Sentence = sample_Sentence
        self.sample_Sentence16 = sample_Sentence16 if sample_Sentence16 is not None else set()
        self.sample_Sentence18 = sample_Sentence18
        self.sample_Sentence11 = sample_Sentence11
        self.sample_Sentence14 = sample_Sentence14
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

    @property
    def sample_Sentence16(self):
        return self.__sample_Sentence16

    @sample_Sentence16.setter
    def sample_Sentence16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Sentence__sample_Sentence16", None)
        self.__sample_Sentence16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Variable"):
                    opp_val = getattr(item, "sample_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Variable"):
                    opp_val = getattr(item, "sample_Variable", None)
                    
                    setattr(item, "sample_Variable", self)
                    

    @property
    def sample_Sentence18(self):
        return self.__sample_Sentence18

    @sample_Sentence18.setter
    def sample_Sentence18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Sentence__sample_Sentence18", None)
        self.__sample_Sentence18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Annotation"):
                opp_val = getattr(old_value, "sample_Annotation", None)
                if opp_val == self:
                    setattr(old_value, "sample_Annotation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Annotation"):
                opp_val = getattr(value, "sample_Annotation", None)
                setattr(value, "sample_Annotation", self)

    @property
    def sample_Sentence(self):
        return self.__sample_Sentence

    @sample_Sentence.setter
    def sample_Sentence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Sentence__sample_Sentence", None)
        self.__sample_Sentence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_When8"):
                opp_val = getattr(old_value, "sample_When8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_When8"):
                opp_val = getattr(value, "sample_When8", None)
                if opp_val is None:
                    setattr(value, "sample_When8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Sentence11(self):
        return self.__sample_Sentence11

    @sample_Sentence11.setter
    def sample_Sentence11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Sentence__sample_Sentence11", None)
        self.__sample_Sentence11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Given10"):
                opp_val = getattr(old_value, "sample_Given10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Given10"):
                opp_val = getattr(value, "sample_Given10", None)
                if opp_val is None:
                    setattr(value, "sample_Given10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Sentence14(self):
        return self.__sample_Sentence14

    @sample_Sentence14.setter
    def sample_Sentence14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Sentence__sample_Sentence14", None)
        self.__sample_Sentence14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Then13"):
                opp_val = getattr(old_value, "sample_Then13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Then13"):
                opp_val = getattr(value, "sample_Then13", None)
                if opp_val is None:
                    setattr(value, "sample_Then13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Then:

    pass
class sample_Scenario:

    def __init__(self, Title: str, sample_Scenario: "sample_Story" = None, sample_Scenario6: "sample_Then" = None, sample_Scenario2: "sample_When" = None, sample_Scenario4: "sample_Given" = None):
        self.Title = Title
        self.sample_Scenario = sample_Scenario
        self.sample_Scenario6 = sample_Scenario6
        self.sample_Scenario2 = sample_Scenario2
        self.sample_Scenario4 = sample_Scenario4
        
    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def sample_Scenario(self):
        return self.__sample_Scenario

    @sample_Scenario.setter
    def sample_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario", None)
        self.__sample_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Story"):
                opp_val = getattr(old_value, "sample_Story", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Story"):
                opp_val = getattr(value, "sample_Story", None)
                if opp_val is None:
                    setattr(value, "sample_Story", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Scenario4(self):
        return self.__sample_Scenario4

    @sample_Scenario4.setter
    def sample_Scenario4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario4", None)
        self.__sample_Scenario4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Given"):
                opp_val = getattr(old_value, "sample_Given", None)
                if opp_val == self:
                    setattr(old_value, "sample_Given", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Given"):
                opp_val = getattr(value, "sample_Given", None)
                setattr(value, "sample_Given", self)

    @property
    def sample_Scenario2(self):
        return self.__sample_Scenario2

    @sample_Scenario2.setter
    def sample_Scenario2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario2", None)
        self.__sample_Scenario2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_When"):
                opp_val = getattr(old_value, "sample_When", None)
                if opp_val == self:
                    setattr(old_value, "sample_When", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_When"):
                opp_val = getattr(value, "sample_When", None)
                setattr(value, "sample_When", self)

    @property
    def sample_Scenario6(self):
        return self.__sample_Scenario6

    @sample_Scenario6.setter
    def sample_Scenario6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario6", None)
        self.__sample_Scenario6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Then"):
                opp_val = getattr(old_value, "sample_Then", None)
                if opp_val == self:
                    setattr(old_value, "sample_Then", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Then"):
                opp_val = getattr(value, "sample_Then", None)
                setattr(value, "sample_Then", self)

class sample_Story:

    def __init__(self, Role: str, Feature: str, Benefit: str, Title: str, sample_Story: set["sample_Scenario"] = None, sample_Story20: "sample_Register" = None):
        self.Role = Role
        self.Feature = Feature
        self.Benefit = Benefit
        self.Title = Title
        self.sample_Story = sample_Story if sample_Story is not None else set()
        self.sample_Story20 = sample_Story20
        
    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def Feature(self) -> str:
        return self.__Feature

    @Feature.setter
    def Feature(self, Feature: str):
        self.__Feature = Feature

    @property
    def Benefit(self) -> str:
        return self.__Benefit

    @Benefit.setter
    def Benefit(self, Benefit: str):
        self.__Benefit = Benefit

    @property
    def Role(self) -> str:
        return self.__Role

    @Role.setter
    def Role(self, Role: str):
        self.__Role = Role

    @property
    def sample_Story20(self):
        return self.__sample_Story20

    @sample_Story20.setter
    def sample_Story20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Story__sample_Story20", None)
        self.__sample_Story20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sample_Register"):
                opp_val = getattr(old_value, "sample_Register", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sample_Register"):
                opp_val = getattr(value, "sample_Register", None)
                if opp_val is None:
                    setattr(value, "sample_Register", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sample_Story(self):
        return self.__sample_Story

    @sample_Story.setter
    def sample_Story(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Story__sample_Story", None)
        self.__sample_Story = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Scenario"):
                    opp_val = getattr(item, "sample_Scenario", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Scenario", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Scenario"):
                    opp_val = getattr(item, "sample_Scenario", None)
                    
                    setattr(item, "sample_Scenario", self)
                    
