from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sample_Sentence:

    def __init__(self, Text: str, sample_Sentence: "sample_When" = None, sample_Sentence11: "sample_Given" = None, sample_Sentence14: "sample_Then" = None):
        self.Text = Text
        self.sample_Sentence = sample_Sentence
        self.sample_Sentence11 = sample_Sentence11
        self.sample_Sentence14 = sample_Sentence14
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

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
class sample_Given:

    pass
class sample_When:

    pass
class sample_Scenario:

    def __init__(self, Title: str, sample_Scenario: "sample_Story" = None, sample_Scenario2: set["sample_When"] = None, sample_Scenario4: set["sample_Given"] = None, sample_Scenario6: set["sample_Then"] = None):
        self.Title = Title
        self.sample_Scenario = sample_Scenario
        self.sample_Scenario2 = sample_Scenario2 if sample_Scenario2 is not None else set()
        self.sample_Scenario4 = sample_Scenario4 if sample_Scenario4 is not None else set()
        self.sample_Scenario6 = sample_Scenario6 if sample_Scenario6 is not None else set()
        
    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def sample_Scenario4(self):
        return self.__sample_Scenario4

    @sample_Scenario4.setter
    def sample_Scenario4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario4", None)
        self.__sample_Scenario4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Given"):
                    opp_val = getattr(item, "sample_Given", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Given", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Given"):
                    opp_val = getattr(item, "sample_Given", None)
                    
                    setattr(item, "sample_Given", self)
                    

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
    def sample_Scenario6(self):
        return self.__sample_Scenario6

    @sample_Scenario6.setter
    def sample_Scenario6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario6", None)
        self.__sample_Scenario6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_Then"):
                    opp_val = getattr(item, "sample_Then", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_Then", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_Then"):
                    opp_val = getattr(item, "sample_Then", None)
                    
                    setattr(item, "sample_Then", self)
                    

    @property
    def sample_Scenario2(self):
        return self.__sample_Scenario2

    @sample_Scenario2.setter
    def sample_Scenario2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Scenario__sample_Scenario2", None)
        self.__sample_Scenario2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sample_When"):
                    opp_val = getattr(item, "sample_When", None)
                    
                    if opp_val == self:
                        setattr(item, "sample_When", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sample_When"):
                    opp_val = getattr(item, "sample_When", None)
                    
                    setattr(item, "sample_When", self)
                    

class sample_Story:

    def __init__(self, Role: str, Feature: str, Benefit: str, sample_Story: set["sample_Scenario"] = None):
        self.Role = Role
        self.Feature = Feature
        self.Benefit = Benefit
        self.sample_Story = sample_Story if sample_Story is not None else set()
        
    @property
    def Feature(self) -> str:
        return self.__Feature

    @Feature.setter
    def Feature(self, Feature: str):
        self.__Feature = Feature

    @property
    def Role(self) -> str:
        return self.__Role

    @Role.setter
    def Role(self, Role: str):
        self.__Role = Role

    @property
    def Benefit(self) -> str:
        return self.__Benefit

    @Benefit.setter
    def Benefit(self, Benefit: str):
        self.__Benefit = Benefit

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
                    
