from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Statement:

    pass
class textualusecase_LoopStatement(Statement):

    pass
class textualusecase_ConditionalStatement(Statement):

    pass
class Step:

    pass
class Agent:

    pass
class textualusecase_Statement(Step):

    pass
class textualusecase_FlowOfEvents(ABC):

    def __init__(self, name: str, FlowOfEvents: "textualusecase_Step" = None, flowOfEvents: set["textualusecase_Step"] = None):
        self.name = name
        self.FlowOfEvents = FlowOfEvents
        self.flowOfEvents = flowOfEvents if flowOfEvents is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def FlowOfEvents(self):
        return self.__FlowOfEvents

    @FlowOfEvents.setter
    def FlowOfEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_FlowOfEvents__FlowOfEvents", None)
        self.__FlowOfEvents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "steps30"):
                opp_val = getattr(old_value, "steps30", None)
                if opp_val == self:
                    setattr(old_value, "steps30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "steps30"):
                opp_val = getattr(value, "steps30", None)
                setattr(value, "steps30", self)

    @property
    def flowOfEvents(self):
        return self.__flowOfEvents

    @flowOfEvents.setter
    def flowOfEvents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_FlowOfEvents__flowOfEvents", None)
        self.__flowOfEvents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Step25"):
                    opp_val = getattr(item, "Step25", None)
                    
                    if opp_val == self:
                        setattr(item, "Step25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Step25"):
                    opp_val = getattr(item, "Step25", None)
                    
                    setattr(item, "Step25", self)
                    

class textualusecase_Action(Step):

    def __init__(self, description: str, Action: "textualusecase_Agent" = None, actions: "textualusecase_Agent" = None):
        self.description = description
        self.Action = Action
        self.actions = actions
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def actions(self):
        return self.__actions

    @actions.setter
    def actions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Action__actions", None)
        self.__actions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Agent"):
                opp_val = getattr(old_value, "Agent", None)
                if opp_val == self:
                    setattr(old_value, "Agent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Agent"):
                opp_val = getattr(value, "Agent", None)
                setattr(value, "Agent", self)

    @property
    def Action(self):
        return self.__Action

    @Action.setter
    def Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Action__Action", None)
        self.__Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agent"):
                opp_val = getattr(old_value, "agent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agent"):
                opp_val = getattr(value, "agent", None)
                if opp_val is None:
                    setattr(value, "agent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class textualusecase_Agent(ABC):

    def __init__(self, name: str, agent: set["textualusecase_Action"] = None, Agent: "textualusecase_Action" = None):
        self.name = name
        self.agent = agent if agent is not None else set()
        self.Agent = Agent
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def agent(self):
        return self.__agent

    @agent.setter
    def agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Agent__agent", None)
        self.__agent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    if opp_val == self:
                        setattr(item, "Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Action"):
                    opp_val = getattr(item, "Action", None)
                    
                    setattr(item, "Action", self)
                    

    @property
    def Agent(self):
        return self.__Agent

    @Agent.setter
    def Agent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Agent__Agent", None)
        self.__Agent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actions"):
                opp_val = getattr(old_value, "actions", None)
                if opp_val == self:
                    setattr(old_value, "actions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actions"):
                opp_val = getattr(value, "actions", None)
                setattr(value, "actions", self)

class FlowOfEvents:

    pass
class textualusecase_Include(Step):

    pass
class textualusecase_Condition:

    def __init__(self, expression: str, textualusecase_Condition33: "textualusecase_Statement" = None, textualusecase_Condition20: "textualusecase_AlternativeFlow" = None, textualusecase_Condition: "textualusecase_UseCase" = None, textualusecase_Condition13: "textualusecase_UseCase" = None):
        self.expression = expression
        self.textualusecase_Condition33 = textualusecase_Condition33
        self.textualusecase_Condition20 = textualusecase_Condition20
        self.textualusecase_Condition = textualusecase_Condition
        self.textualusecase_Condition13 = textualusecase_Condition13
        
        pass
    @property
    def expression(self):
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression


    @property
    def textualusecase_Condition13(self):
        return self.__textualusecase_Condition13

    @textualusecase_Condition13.setter
    def textualusecase_Condition13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Condition__textualusecase_Condition13", None)
        self.__textualusecase_Condition13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_UseCase12"):
                opp_val = getattr(old_value, "textualusecase_UseCase12", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_UseCase12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_UseCase12"):
                opp_val = getattr(value, "textualusecase_UseCase12", None)
                setattr(value, "textualusecase_UseCase12", self)

    @property
    def textualusecase_Condition20(self):
        return self.__textualusecase_Condition20

    @textualusecase_Condition20.setter
    def textualusecase_Condition20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Condition__textualusecase_Condition20", None)
        self.__textualusecase_Condition20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_AlternativeFlow"):
                opp_val = getattr(old_value, "textualusecase_AlternativeFlow", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_AlternativeFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_AlternativeFlow"):
                opp_val = getattr(value, "textualusecase_AlternativeFlow", None)
                setattr(value, "textualusecase_AlternativeFlow", self)

    @property
    def textualusecase_Condition(self):
        return self.__textualusecase_Condition

    @textualusecase_Condition.setter
    def textualusecase_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Condition__textualusecase_Condition", None)
        self.__textualusecase_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_UseCase"):
                opp_val = getattr(old_value, "textualusecase_UseCase", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_UseCase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_UseCase"):
                opp_val = getattr(value, "textualusecase_UseCase", None)
                setattr(value, "textualusecase_UseCase", self)

    @property
    def textualusecase_Condition33(self):
        return self.__textualusecase_Condition33

    @textualusecase_Condition33.setter
    def textualusecase_Condition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Condition__textualusecase_Condition33", None)
        self.__textualusecase_Condition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_Statement"):
                opp_val = getattr(old_value, "textualusecase_Statement", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_Statement"):
                opp_val = getattr(value, "textualusecase_Statement", None)
                setattr(value, "textualusecase_Statement", self)

class textualusecase_Step(ABC):

    def __init__(self, name: str, Step35: "textualusecase_Statement" = None, Step: "textualusecase_AlternativeFlow" = None, steps30: "textualusecase_FlowOfEvents" = None, Step25: "textualusecase_FlowOfEvents" = None, branchingStep: set["textualusecase_AlternativeFlow"] = None, steps: "textualusecase_Statement" = None):
        self.name = name
        self.Step35 = Step35
        self.Step = Step
        self.steps30 = steps30
        self.Step25 = Step25
        self.branchingStep = branchingStep if branchingStep is not None else set()
        self.steps = steps
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def steps(self):
        return self.__steps

    @steps.setter
    def steps(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__steps", None)
        self.__steps = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement"):
                opp_val = getattr(old_value, "Statement", None)
                if opp_val == self:
                    setattr(old_value, "Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement"):
                opp_val = getattr(value, "Statement", None)
                setattr(value, "Statement", self)

    @property
    def steps30(self):
        return self.__steps30

    @steps30.setter
    def steps30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__steps30", None)
        self.__steps30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FlowOfEvents"):
                opp_val = getattr(old_value, "FlowOfEvents", None)
                if opp_val == self:
                    setattr(old_value, "FlowOfEvents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FlowOfEvents"):
                opp_val = getattr(value, "FlowOfEvents", None)
                setattr(value, "FlowOfEvents", self)

    @property
    def Step(self):
        return self.__Step

    @Step.setter
    def Step(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__Step", None)
        self.__Step = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternativeFlow"):
                opp_val = getattr(old_value, "alternativeFlow", None)
                if opp_val == self:
                    setattr(old_value, "alternativeFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternativeFlow"):
                opp_val = getattr(value, "alternativeFlow", None)
                setattr(value, "alternativeFlow", self)

    @property
    def Step35(self):
        return self.__Step35

    @Step35.setter
    def Step35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__Step35", None)
        self.__Step35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statement"):
                opp_val = getattr(old_value, "statement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statement"):
                opp_val = getattr(value, "statement", None)
                if opp_val is None:
                    setattr(value, "statement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def branchingStep(self):
        return self.__branchingStep

    @branchingStep.setter
    def branchingStep(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__branchingStep", None)
        self.__branchingStep = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AlternativeFlow27"):
                    opp_val = getattr(item, "AlternativeFlow27", None)
                    
                    if opp_val == self:
                        setattr(item, "AlternativeFlow27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AlternativeFlow27"):
                    opp_val = getattr(item, "AlternativeFlow27", None)
                    
                    setattr(item, "AlternativeFlow27", self)
                    

    @property
    def Step25(self):
        return self.__Step25

    @Step25.setter
    def Step25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_Step__Step25", None)
        self.__Step25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "flowOfEvents"):
                opp_val = getattr(old_value, "flowOfEvents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "flowOfEvents"):
                opp_val = getattr(value, "flowOfEvents", None)
                if opp_val is None:
                    setattr(value, "flowOfEvents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class textualusecase_AlternativeFlow(FlowOfEvents):

    pass
class textualusecase_Subject(Agent):

    pass
class textualusecase_Actor(Agent):

    pass
class textualusecase_UseCase:

    def __init__(self, name: str, description: str, UseCase47: "textualusecase_Include" = None, UseCase42: "textualusecase_Actor" = None, useCase6: "textualusecase_BasicFlow" = None, useCase8: set["textualusecase_Actor"] = None, UseCase: "textualusecase_UseCaseModel" = None, useCase: set["textualusecase_AlternativeFlow"] = None, UseCase23: "textualusecase_AlternativeFlow" = None, textualusecase_UseCase: "textualusecase_Condition" = None, textualusecase_UseCase12: "textualusecase_Condition" = None, useCase15: "textualusecase_UseCaseModel" = None, useCase17: set["textualusecase_Include"] = None, UseCase37: "textualusecase_BasicFlow" = None):
        self.name = name
        self.description = description
        self.UseCase47 = UseCase47
        self.UseCase42 = UseCase42
        self.useCase6 = useCase6
        self.useCase8 = useCase8 if useCase8 is not None else set()
        self.UseCase = UseCase
        self.useCase = useCase if useCase is not None else set()
        self.UseCase23 = UseCase23
        self.textualusecase_UseCase = textualusecase_UseCase
        self.textualusecase_UseCase12 = textualusecase_UseCase12
        self.useCase15 = useCase15
        self.useCase17 = useCase17 if useCase17 is not None else set()
        self.UseCase37 = UseCase37
        
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
    def UseCase37(self):
        return self.__UseCase37

    @UseCase37.setter
    def UseCase37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__UseCase37", None)
        self.__UseCase37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "basicFlow"):
                opp_val = getattr(old_value, "basicFlow", None)
                if opp_val == self:
                    setattr(old_value, "basicFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "basicFlow"):
                opp_val = getattr(value, "basicFlow", None)
                setattr(value, "basicFlow", self)

    @property
    def UseCase47(self):
        return self.__UseCase47

    @UseCase47.setter
    def UseCase47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__UseCase47", None)
        self.__UseCase47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "includes"):
                opp_val = getattr(old_value, "includes", None)
                if opp_val == self:
                    setattr(old_value, "includes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "includes"):
                opp_val = getattr(value, "includes", None)
                setattr(value, "includes", self)

    @property
    def useCase15(self):
        return self.__useCase15

    @useCase15.setter
    def useCase15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__useCase15", None)
        self.__useCase15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UseCaseModel"):
                opp_val = getattr(old_value, "UseCaseModel", None)
                if opp_val == self:
                    setattr(old_value, "UseCaseModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UseCaseModel"):
                opp_val = getattr(value, "UseCaseModel", None)
                setattr(value, "UseCaseModel", self)

    @property
    def UseCase23(self):
        return self.__UseCase23

    @UseCase23.setter
    def UseCase23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__UseCase23", None)
        self.__UseCase23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alternativeFlow22"):
                opp_val = getattr(old_value, "alternativeFlow22", None)
                if opp_val == self:
                    setattr(old_value, "alternativeFlow22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alternativeFlow22"):
                opp_val = getattr(value, "alternativeFlow22", None)
                setattr(value, "alternativeFlow22", self)

    @property
    def useCase(self):
        return self.__useCase

    @useCase.setter
    def useCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__useCase", None)
        self.__useCase = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AlternativeFlow"):
                    opp_val = getattr(item, "AlternativeFlow", None)
                    
                    if opp_val == self:
                        setattr(item, "AlternativeFlow", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AlternativeFlow"):
                    opp_val = getattr(item, "AlternativeFlow", None)
                    
                    setattr(item, "AlternativeFlow", self)
                    

    @property
    def UseCase42(self):
        return self.__UseCase42

    @UseCase42.setter
    def UseCase42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__UseCase42", None)
        self.__UseCase42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "actor41"):
                opp_val = getattr(old_value, "actor41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "actor41"):
                opp_val = getattr(value, "actor41", None)
                if opp_val is None:
                    setattr(value, "actor41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def textualusecase_UseCase12(self):
        return self.__textualusecase_UseCase12

    @textualusecase_UseCase12.setter
    def textualusecase_UseCase12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__textualusecase_UseCase12", None)
        self.__textualusecase_UseCase12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_Condition13"):
                opp_val = getattr(old_value, "textualusecase_Condition13", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_Condition13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_Condition13"):
                opp_val = getattr(value, "textualusecase_Condition13", None)
                setattr(value, "textualusecase_Condition13", self)

    @property
    def useCase17(self):
        return self.__useCase17

    @useCase17.setter
    def useCase17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__useCase17", None)
        self.__useCase17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    if opp_val == self:
                        setattr(item, "Include", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Include"):
                    opp_val = getattr(item, "Include", None)
                    
                    setattr(item, "Include", self)
                    

    @property
    def useCase8(self):
        return self.__useCase8

    @useCase8.setter
    def useCase8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__useCase8", None)
        self.__useCase8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Actor9"):
                    opp_val = getattr(item, "Actor9", None)
                    
                    if opp_val == self:
                        setattr(item, "Actor9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Actor9"):
                    opp_val = getattr(item, "Actor9", None)
                    
                    setattr(item, "Actor9", self)
                    

    @property
    def textualusecase_UseCase(self):
        return self.__textualusecase_UseCase

    @textualusecase_UseCase.setter
    def textualusecase_UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__textualusecase_UseCase", None)
        self.__textualusecase_UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "textualusecase_Condition"):
                opp_val = getattr(old_value, "textualusecase_Condition", None)
                if opp_val == self:
                    setattr(old_value, "textualusecase_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "textualusecase_Condition"):
                opp_val = getattr(value, "textualusecase_Condition", None)
                setattr(value, "textualusecase_Condition", self)

    @property
    def useCase6(self):
        return self.__useCase6

    @useCase6.setter
    def useCase6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__useCase6", None)
        self.__useCase6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BasicFlow"):
                opp_val = getattr(old_value, "BasicFlow", None)
                if opp_val == self:
                    setattr(old_value, "BasicFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BasicFlow"):
                opp_val = getattr(value, "BasicFlow", None)
                setattr(value, "BasicFlow", self)

    @property
    def UseCase(self):
        return self.__UseCase

    @UseCase.setter
    def UseCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_textualusecase_UseCase__UseCase", None)
        self.__UseCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "useCaseModel"):
                opp_val = getattr(old_value, "useCaseModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "useCaseModel"):
                opp_val = getattr(value, "useCaseModel", None)
                if opp_val is None:
                    setattr(value, "useCaseModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class textualusecase_BasicFlow(FlowOfEvents):

    pass
class textualusecase_UseCaseModel:

    pass