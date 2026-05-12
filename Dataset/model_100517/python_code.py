from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class story_Parameter:

    def __init__(self, name: str, type: str, description: str, story_Parameter: "story_Story" = None):
        self.name = name
        self.type = type
        self.description = description
        self.story_Parameter = story_Parameter
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def story_Parameter(self):
        return self.__story_Parameter

    @story_Parameter.setter
    def story_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Parameter__story_Parameter", None)
        self.__story_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Story32"):
                opp_val = getattr(old_value, "story_Story32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Story32"):
                opp_val = getattr(value, "story_Story32", None)
                if opp_val is None:
                    setattr(value, "story_Story32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class story_ConditionalProtagonist:

    def __init__(self, condition: str, story_ConditionalProtagonist: "story_Story" = None, story_ConditionalProtagonist37: set["story_Protagonist"] = None):
        self.condition = condition
        self.story_ConditionalProtagonist = story_ConditionalProtagonist
        self.story_ConditionalProtagonist37 = story_ConditionalProtagonist37 if story_ConditionalProtagonist37 is not None else set()
        
        pass
    @property
    def condition(self):
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition


    @property
    def story_ConditionalProtagonist(self):
        return self.__story_ConditionalProtagonist

    @story_ConditionalProtagonist.setter
    def story_ConditionalProtagonist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_ConditionalProtagonist__story_ConditionalProtagonist", None)
        self.__story_ConditionalProtagonist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Story30"):
                opp_val = getattr(old_value, "story_Story30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Story30"):
                opp_val = getattr(value, "story_Story30", None)
                if opp_val is None:
                    setattr(value, "story_Story30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def story_ConditionalProtagonist37(self):
        return self.__story_ConditionalProtagonist37

    @story_ConditionalProtagonist37.setter
    def story_ConditionalProtagonist37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_ConditionalProtagonist__story_ConditionalProtagonist37", None)
        self.__story_ConditionalProtagonist37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Protagonist38"):
                    opp_val = getattr(item, "story_Protagonist38", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Protagonist38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Protagonist38"):
                    opp_val = getattr(item, "story_Protagonist38", None)
                    
                    setattr(item, "story_Protagonist38", self)
                    

class story_Goal:

    def __init__(self, name: str, details: str, story_Goal: "story_Persona" = None, story_Goal35: "story_Story" = None):
        self.name = name
        self.details = details
        self.story_Goal = story_Goal
        self.story_Goal35 = story_Goal35
        
        pass
    @property
    def details(self):
        return self.__details

    @details.setter
    def details(self, details: str):
        self.__details = details


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def story_Goal(self):
        return self.__story_Goal

    @story_Goal.setter
    def story_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Goal__story_Goal", None)
        self.__story_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Persona"):
                opp_val = getattr(old_value, "story_Persona", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Persona"):
                opp_val = getattr(value, "story_Persona", None)
                if opp_val is None:
                    setattr(value, "story_Persona", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def story_Goal35(self):
        return self.__story_Goal35

    @story_Goal35.setter
    def story_Goal35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Goal__story_Goal35", None)
        self.__story_Goal35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Story34"):
                opp_val = getattr(old_value, "story_Story34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Story34"):
                opp_val = getattr(value, "story_Story34", None)
                if opp_val is None:
                    setattr(value, "story_Story34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StoryBase:

    pass
class story_Story(StoryBase):

    def __init__(self, goal: str, benefit: str, completed: bool, story_Story: set["story_Scenario"] = None, story_Story22: "story_Story" = None, story_Story20: set["story_Story"] = None, story_Story27: set["story_Protagonist"] = None, story_Story30: set["story_ConditionalProtagonist"] = None, story_Story32: set["story_Parameter"] = None, story_Story24: set["story_Theme"] = None, story_Story34: set["story_Goal"] = None):
        self.goal = goal
        self.benefit = benefit
        self.completed = completed
        self.story_Story = story_Story if story_Story is not None else set()
        self.story_Story22 = story_Story22
        self.story_Story20 = story_Story20 if story_Story20 is not None else set()
        self.story_Story27 = story_Story27 if story_Story27 is not None else set()
        self.story_Story30 = story_Story30 if story_Story30 is not None else set()
        self.story_Story32 = story_Story32 if story_Story32 is not None else set()
        self.story_Story24 = story_Story24 if story_Story24 is not None else set()
        self.story_Story34 = story_Story34 if story_Story34 is not None else set()
        
        pass
    @property
    def goal(self):
        return self.__goal

    @goal.setter
    def goal(self, goal: str):
        self.__goal = goal


    @property
    def benefit(self):
        return self.__benefit

    @benefit.setter
    def benefit(self, benefit: str):
        self.__benefit = benefit


    @property
    def completed(self):
        return self.__completed

    @completed.setter
    def completed(self, completed: bool):
        self.__completed = completed


    @property
    def story_Story32(self):
        return self.__story_Story32

    @story_Story32.setter
    def story_Story32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story32", None)
        self.__story_Story32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Parameter"):
                    opp_val = getattr(item, "story_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Parameter"):
                    opp_val = getattr(item, "story_Parameter", None)
                    
                    setattr(item, "story_Parameter", self)
                    

    @property
    def story_Story34(self):
        return self.__story_Story34

    @story_Story34.setter
    def story_Story34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story34", None)
        self.__story_Story34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Goal35"):
                    opp_val = getattr(item, "story_Goal35", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Goal35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Goal35"):
                    opp_val = getattr(item, "story_Goal35", None)
                    
                    setattr(item, "story_Goal35", self)
                    

    @property
    def story_Story22(self):
        return self.__story_Story22

    @story_Story22.setter
    def story_Story22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story22", None)
        self.__story_Story22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Story20"):
                opp_val = getattr(old_value, "story_Story20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Story20"):
                opp_val = getattr(value, "story_Story20", None)
                if opp_val is None:
                    setattr(value, "story_Story20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def story_Story20(self):
        return self.__story_Story20

    @story_Story20.setter
    def story_Story20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story20", None)
        self.__story_Story20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Story22"):
                    opp_val = getattr(item, "story_Story22", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Story22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Story22"):
                    opp_val = getattr(item, "story_Story22", None)
                    
                    setattr(item, "story_Story22", self)
                    

    @property
    def story_Story24(self):
        return self.__story_Story24

    @story_Story24.setter
    def story_Story24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story24", None)
        self.__story_Story24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Theme25"):
                    opp_val = getattr(item, "story_Theme25", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Theme25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Theme25"):
                    opp_val = getattr(item, "story_Theme25", None)
                    
                    setattr(item, "story_Theme25", self)
                    

    @property
    def story_Story30(self):
        return self.__story_Story30

    @story_Story30.setter
    def story_Story30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story30", None)
        self.__story_Story30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_ConditionalProtagonist"):
                    opp_val = getattr(item, "story_ConditionalProtagonist", None)
                    
                    if opp_val == self:
                        setattr(item, "story_ConditionalProtagonist", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_ConditionalProtagonist"):
                    opp_val = getattr(item, "story_ConditionalProtagonist", None)
                    
                    setattr(item, "story_ConditionalProtagonist", self)
                    

    @property
    def story_Story(self):
        return self.__story_Story

    @story_Story.setter
    def story_Story(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story", None)
        self.__story_Story = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Scenario"):
                    opp_val = getattr(item, "story_Scenario", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Scenario", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Scenario"):
                    opp_val = getattr(item, "story_Scenario", None)
                    
                    setattr(item, "story_Scenario", self)
                    

    @property
    def story_Story27(self):
        return self.__story_Story27

    @story_Story27.setter
    def story_Story27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Story__story_Story27", None)
        self.__story_Story27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Protagonist28"):
                    opp_val = getattr(item, "story_Protagonist28", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Protagonist28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Protagonist28"):
                    opp_val = getattr(item, "story_Protagonist28", None)
                    
                    setattr(item, "story_Protagonist28", self)
                    

class User:

    pass
class story_Persona(User):

    def __init__(self, picture: str, story_Persona: set["story_Goal"] = None):
        self.picture = picture
        self.story_Persona = story_Persona if story_Persona is not None else set()
        
        pass
    @property
    def picture(self):
        return self.__picture

    @picture.setter
    def picture(self, picture: str):
        self.__picture = picture


    @property
    def story_Persona(self):
        return self.__story_Persona

    @story_Persona.setter
    def story_Persona(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Persona__story_Persona", None)
        self.__story_Persona = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "story_Goal"):
                    opp_val = getattr(item, "story_Goal", None)
                    
                    if opp_val == self:
                        setattr(item, "story_Goal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "story_Goal"):
                    opp_val = getattr(item, "story_Goal", None)
                    
                    setattr(item, "story_Goal", self)
                    

class Actor:

    pass
class story_System(Actor):

    pass
class story_User(Actor):

    pass
class Protagonist:

    pass
class story_Actor(Protagonist):

    pass
class story_Role(Protagonist):

    pass
class story_EClass:

    pass
class StoryContainer:

    pass
class story_Epic(StoryBase, StoryContainer):

    pass
class story_Protagonist(StoryContainer):

    pass
class story_CatalogElement(ABC):

    def __init__(self, id: str, name: str, description: str, story_CatalogElement: "story_Catalog" = None):
        self.id = id
        self.name = name
        self.description = description
        self.story_CatalogElement = story_CatalogElement
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def story_CatalogElement(self):
        return self.__story_CatalogElement

    @story_CatalogElement.setter
    def story_CatalogElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_CatalogElement__story_CatalogElement", None)
        self.__story_CatalogElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Catalog"):
                opp_val = getattr(old_value, "story_Catalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Catalog"):
                opp_val = getattr(value, "story_Catalog", None)
                if opp_val is None:
                    setattr(value, "story_Catalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CatalogElement:

    pass
class story_Scenario(CatalogElement):

    def __init__(self, action: str, outcome: str, context: str, story_Scenario: "story_Story" = None):
        self.action = action
        self.outcome = outcome
        self.context = context
        self.story_Scenario = story_Scenario
        
        pass
    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


    @property
    def outcome(self):
        return self.__outcome

    @outcome.setter
    def outcome(self, outcome: str):
        self.__outcome = outcome


    @property
    def context(self):
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context


    @property
    def story_Scenario(self):
        return self.__story_Scenario

    @story_Scenario.setter
    def story_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_story_Scenario__story_Scenario", None)
        self.__story_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_Story"):
                opp_val = getattr(old_value, "story_Story", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_Story"):
                opp_val = getattr(value, "story_Story", None)
                if opp_val is None:
                    setattr(value, "story_Story", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class story_StoryBase(CatalogElement):

    pass
class story_StoryContainer(CatalogElement):

    pass
class story_Theme(CatalogElement):

    pass
class story_Catalog(CatalogElement):

    pass