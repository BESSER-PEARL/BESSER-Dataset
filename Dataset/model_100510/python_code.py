from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Taxonomy(Enum):
    Proportion = "Proportion"
    Location = "Location"
    Comparison = "Comparison"
    Part_to_a_whole = "Part_to_a_whole"
    Relationship = "Relationship"
    Over_time = "Over_time"
    Distribution = "Distribution"
    Hierarchy = "Hierarchy"
    Reference_tool = "Reference_tool"
    Range = "Range"
    Pattern = "Pattern"
class DataType(Enum):
    Temperature = "Temperature"
    Luminosity = "Luminosity"
    Humidity = "Humidity"
    Cardiac_frequency = "Cardiac_frequency"
    Occupancy = "Occupancy"
    Pressure = "Pressure"
class Reaction(Enum):
    Synchronize = "Synchronize"
    GoTo = "GoTo"
    Enable = "Enable"
    Disable = "Disable"
class State(Enum):
    Over = "Over"
    Current = "Current"
    Expected = "Expected"
class Quantifier(Enum):
    All = "All"
    Some = "Some"
    One = "One"
class ContainerType(Enum):
    Building = "Building"
    Floor = "Floor"
    Corridor = "Corridor"
    Room = "Room"
    Furniture = "Furniture"
    Wall = "Wall"
    Window = "Window"
class Action(Enum):
    next = "next"
    previous = "previous"
    range = "range"
    element = "element"


############################################
# Definition of Classes
############################################

class Then:

    pass
class requirementEngineeringLanguage_Goal(Then):

    def __init__(self, function: str, data: str):
        self.function = function
        self.data = data
        
        pass
    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


class requirementEngineeringLanguage_Update(Then):

    def __init__(self, do: str, requirementEngineeringLanguage_Update: "requirementEngineeringLanguage_View" = None):
        self.do = do
        self.requirementEngineeringLanguage_Update = requirementEngineeringLanguage_Update
        
        pass
    @property
    def do(self):
        return self.__do

    @do.setter
    def do(self, do: str):
        self.__do = do


    @property
    def requirementEngineeringLanguage_Update(self):
        return self.__requirementEngineeringLanguage_Update

    @requirementEngineeringLanguage_Update.setter
    def requirementEngineeringLanguage_Update(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Update__requirementEngineeringLanguage_Update", None)
        self.__requirementEngineeringLanguage_Update = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_View13"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_View13", None)
                if opp_val == self:
                    setattr(old_value, "requirementEngineeringLanguage_View13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_View13"):
                opp_val = getattr(value, "requirementEngineeringLanguage_View13", None)
                setattr(value, "requirementEngineeringLanguage_View13", self)

class requirementEngineeringLanguage_Background:

    def __init__(self, dashboard: str, requirementEngineeringLanguage_Background: "requirementEngineeringLanguage_Project" = None, requirementEngineeringLanguage_Background18: set["requirementEngineeringLanguage_View"] = None):
        self.dashboard = dashboard
        self.requirementEngineeringLanguage_Background = requirementEngineeringLanguage_Background
        self.requirementEngineeringLanguage_Background18 = requirementEngineeringLanguage_Background18 if requirementEngineeringLanguage_Background18 is not None else set()
        
        pass
    @property
    def dashboard(self):
        return self.__dashboard

    @dashboard.setter
    def dashboard(self, dashboard: str):
        self.__dashboard = dashboard


    @property
    def requirementEngineeringLanguage_Background(self):
        return self.__requirementEngineeringLanguage_Background

    @requirementEngineeringLanguage_Background.setter
    def requirementEngineeringLanguage_Background(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Background__requirementEngineeringLanguage_Background", None)
        self.__requirementEngineeringLanguage_Background = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Project11"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Project11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Project11"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Project11", None)
                if opp_val is None:
                    setattr(value, "requirementEngineeringLanguage_Project11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirementEngineeringLanguage_Background18(self):
        return self.__requirementEngineeringLanguage_Background18

    @requirementEngineeringLanguage_Background18.setter
    def requirementEngineeringLanguage_Background18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Background__requirementEngineeringLanguage_Background18", None)
        self.__requirementEngineeringLanguage_Background18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_View19"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_View19", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_View19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_View19"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_View19", None)
                    
                    setattr(item, "requirementEngineeringLanguage_View19", self)
                    

class requirementEngineeringLanguage_Feature:

    def __init__(self, name: str, desc: str, requirementEngineeringLanguage_Feature: "requirementEngineeringLanguage_Project" = None, requirementEngineeringLanguage_Feature15: set["requirementEngineeringLanguage_Scenario"] = None):
        self.name = name
        self.desc = desc
        self.requirementEngineeringLanguage_Feature = requirementEngineeringLanguage_Feature
        self.requirementEngineeringLanguage_Feature15 = requirementEngineeringLanguage_Feature15 if requirementEngineeringLanguage_Feature15 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc


    @property
    def requirementEngineeringLanguage_Feature15(self):
        return self.__requirementEngineeringLanguage_Feature15

    @requirementEngineeringLanguage_Feature15.setter
    def requirementEngineeringLanguage_Feature15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Feature__requirementEngineeringLanguage_Feature15", None)
        self.__requirementEngineeringLanguage_Feature15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_Scenario16"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Scenario16", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_Scenario16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_Scenario16"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Scenario16", None)
                    
                    setattr(item, "requirementEngineeringLanguage_Scenario16", self)
                    

    @property
    def requirementEngineeringLanguage_Feature(self):
        return self.__requirementEngineeringLanguage_Feature

    @requirementEngineeringLanguage_Feature.setter
    def requirementEngineeringLanguage_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Feature__requirementEngineeringLanguage_Feature", None)
        self.__requirementEngineeringLanguage_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Project"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Project"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Project", None)
                if opp_val is None:
                    setattr(value, "requirementEngineeringLanguage_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class requirementEngineeringLanguage_Project:

    def __init__(self, name: str, requirementEngineeringLanguage_Project: set["requirementEngineeringLanguage_Feature"] = None, requirementEngineeringLanguage_Project11: set["requirementEngineeringLanguage_Background"] = None):
        self.name = name
        self.requirementEngineeringLanguage_Project = requirementEngineeringLanguage_Project if requirementEngineeringLanguage_Project is not None else set()
        self.requirementEngineeringLanguage_Project11 = requirementEngineeringLanguage_Project11 if requirementEngineeringLanguage_Project11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def requirementEngineeringLanguage_Project(self):
        return self.__requirementEngineeringLanguage_Project

    @requirementEngineeringLanguage_Project.setter
    def requirementEngineeringLanguage_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Project__requirementEngineeringLanguage_Project", None)
        self.__requirementEngineeringLanguage_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_Feature"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_Feature"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Feature", None)
                    
                    setattr(item, "requirementEngineeringLanguage_Feature", self)
                    

    @property
    def requirementEngineeringLanguage_Project11(self):
        return self.__requirementEngineeringLanguage_Project11

    @requirementEngineeringLanguage_Project11.setter
    def requirementEngineeringLanguage_Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Project__requirementEngineeringLanguage_Project11", None)
        self.__requirementEngineeringLanguage_Project11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_Background"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Background", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_Background", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_Background"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Background", None)
                    
                    setattr(item, "requirementEngineeringLanguage_Background", self)
                    

class When:

    pass
class requirementEngineeringLanguage_Interaction(When):

    def __init__(self, action: str, target: str):
        self.action = action
        self.target = target
        
        pass
    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target


    @property
    def action(self):
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action


class requirementEngineeringLanguage_Loading(When):

    def __init__(self, new: str):
        self.new = new
        
        pass
    @property
    def new(self):
        return self.__new

    @new.setter
    def new(self, new: str):
        self.__new = new


class requirementEngineeringLanguage_View:

    def __init__(self, name: str, desc: str, requirementEngineeringLanguage_View: "requirementEngineeringLanguage_When" = None, requirementEngineeringLanguage_View13: "requirementEngineeringLanguage_Update" = None, requirementEngineeringLanguage_View19: "requirementEngineeringLanguage_Background" = None):
        self.name = name
        self.desc = desc
        self.requirementEngineeringLanguage_View = requirementEngineeringLanguage_View
        self.requirementEngineeringLanguage_View13 = requirementEngineeringLanguage_View13
        self.requirementEngineeringLanguage_View19 = requirementEngineeringLanguage_View19
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, desc: str):
        self.__desc = desc


    @property
    def requirementEngineeringLanguage_View13(self):
        return self.__requirementEngineeringLanguage_View13

    @requirementEngineeringLanguage_View13.setter
    def requirementEngineeringLanguage_View13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_View__requirementEngineeringLanguage_View13", None)
        self.__requirementEngineeringLanguage_View13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Update"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Update", None)
                if opp_val == self:
                    setattr(old_value, "requirementEngineeringLanguage_Update", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Update"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Update", None)
                setattr(value, "requirementEngineeringLanguage_Update", self)

    @property
    def requirementEngineeringLanguage_View19(self):
        return self.__requirementEngineeringLanguage_View19

    @requirementEngineeringLanguage_View19.setter
    def requirementEngineeringLanguage_View19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_View__requirementEngineeringLanguage_View19", None)
        self.__requirementEngineeringLanguage_View19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Background18"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Background18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Background18"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Background18", None)
                if opp_val is None:
                    setattr(value, "requirementEngineeringLanguage_Background18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirementEngineeringLanguage_View(self):
        return self.__requirementEngineeringLanguage_View

    @requirementEngineeringLanguage_View.setter
    def requirementEngineeringLanguage_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_View__requirementEngineeringLanguage_View", None)
        self.__requirementEngineeringLanguage_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_When8"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_When8", None)
                if opp_val == self:
                    setattr(old_value, "requirementEngineeringLanguage_When8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_When8"):
                opp_val = getattr(value, "requirementEngineeringLanguage_When8", None)
                setattr(value, "requirementEngineeringLanguage_When8", self)

class requirementEngineeringLanguage_Data:

    def __init__(self, type: str, locationType: str, quantifier: str, location: str, requirementEngineeringLanguage_Data: "requirementEngineeringLanguage_Given" = None):
        self.type = type
        self.locationType = locationType
        self.quantifier = quantifier
        self.location = location
        self.requirementEngineeringLanguage_Data = requirementEngineeringLanguage_Data
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def locationType(self):
        return self.__locationType

    @locationType.setter
    def locationType(self, locationType: str):
        self.__locationType = locationType


    @property
    def quantifier(self):
        return self.__quantifier

    @quantifier.setter
    def quantifier(self, quantifier: str):
        self.__quantifier = quantifier


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def requirementEngineeringLanguage_Data(self):
        return self.__requirementEngineeringLanguage_Data

    @requirementEngineeringLanguage_Data.setter
    def requirementEngineeringLanguage_Data(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Data__requirementEngineeringLanguage_Data", None)
        self.__requirementEngineeringLanguage_Data = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Given6"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Given6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Given6"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Given6", None)
                if opp_val is None:
                    setattr(value, "requirementEngineeringLanguage_Given6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class requirementEngineeringLanguage_Given:

    def __init__(self, dashboard: str, requirementEngineeringLanguage_Given: "requirementEngineeringLanguage_Scenario" = None, requirementEngineeringLanguage_Given6: set["requirementEngineeringLanguage_Data"] = None):
        self.dashboard = dashboard
        self.requirementEngineeringLanguage_Given = requirementEngineeringLanguage_Given
        self.requirementEngineeringLanguage_Given6 = requirementEngineeringLanguage_Given6 if requirementEngineeringLanguage_Given6 is not None else set()
        
        pass
    @property
    def dashboard(self):
        return self.__dashboard

    @dashboard.setter
    def dashboard(self, dashboard: str):
        self.__dashboard = dashboard


    @property
    def requirementEngineeringLanguage_Given6(self):
        return self.__requirementEngineeringLanguage_Given6

    @requirementEngineeringLanguage_Given6.setter
    def requirementEngineeringLanguage_Given6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Given__requirementEngineeringLanguage_Given6", None)
        self.__requirementEngineeringLanguage_Given6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_Data"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Data", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_Data", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_Data"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Data", None)
                    
                    setattr(item, "requirementEngineeringLanguage_Data", self)
                    

    @property
    def requirementEngineeringLanguage_Given(self):
        return self.__requirementEngineeringLanguage_Given

    @requirementEngineeringLanguage_Given.setter
    def requirementEngineeringLanguage_Given(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Given__requirementEngineeringLanguage_Given", None)
        self.__requirementEngineeringLanguage_Given = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Scenario4"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Scenario4", None)
                if opp_val == self:
                    setattr(old_value, "requirementEngineeringLanguage_Scenario4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Scenario4"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Scenario4", None)
                setattr(value, "requirementEngineeringLanguage_Scenario4", self)

class requirementEngineeringLanguage_Then(ABC):

    pass
class requirementEngineeringLanguage_When(ABC):

    pass
class requirementEngineeringLanguage_Scenario:

    def __init__(self, name: str, requirementEngineeringLanguage_Scenario: set["requirementEngineeringLanguage_When"] = None, requirementEngineeringLanguage_Scenario2: set["requirementEngineeringLanguage_Then"] = None, requirementEngineeringLanguage_Scenario4: "requirementEngineeringLanguage_Given" = None, requirementEngineeringLanguage_Scenario16: "requirementEngineeringLanguage_Feature" = None):
        self.name = name
        self.requirementEngineeringLanguage_Scenario = requirementEngineeringLanguage_Scenario if requirementEngineeringLanguage_Scenario is not None else set()
        self.requirementEngineeringLanguage_Scenario2 = requirementEngineeringLanguage_Scenario2 if requirementEngineeringLanguage_Scenario2 is not None else set()
        self.requirementEngineeringLanguage_Scenario4 = requirementEngineeringLanguage_Scenario4
        self.requirementEngineeringLanguage_Scenario16 = requirementEngineeringLanguage_Scenario16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def requirementEngineeringLanguage_Scenario2(self):
        return self.__requirementEngineeringLanguage_Scenario2

    @requirementEngineeringLanguage_Scenario2.setter
    def requirementEngineeringLanguage_Scenario2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Scenario__requirementEngineeringLanguage_Scenario2", None)
        self.__requirementEngineeringLanguage_Scenario2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_Then"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Then", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_Then", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_Then"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_Then", None)
                    
                    setattr(item, "requirementEngineeringLanguage_Then", self)
                    

    @property
    def requirementEngineeringLanguage_Scenario16(self):
        return self.__requirementEngineeringLanguage_Scenario16

    @requirementEngineeringLanguage_Scenario16.setter
    def requirementEngineeringLanguage_Scenario16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Scenario__requirementEngineeringLanguage_Scenario16", None)
        self.__requirementEngineeringLanguage_Scenario16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Feature15"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Feature15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Feature15"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Feature15", None)
                if opp_val is None:
                    setattr(value, "requirementEngineeringLanguage_Feature15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def requirementEngineeringLanguage_Scenario(self):
        return self.__requirementEngineeringLanguage_Scenario

    @requirementEngineeringLanguage_Scenario.setter
    def requirementEngineeringLanguage_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Scenario__requirementEngineeringLanguage_Scenario", None)
        self.__requirementEngineeringLanguage_Scenario = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "requirementEngineeringLanguage_When"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_When", None)
                    
                    if opp_val == self:
                        setattr(item, "requirementEngineeringLanguage_When", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "requirementEngineeringLanguage_When"):
                    opp_val = getattr(item, "requirementEngineeringLanguage_When", None)
                    
                    setattr(item, "requirementEngineeringLanguage_When", self)
                    

    @property
    def requirementEngineeringLanguage_Scenario4(self):
        return self.__requirementEngineeringLanguage_Scenario4

    @requirementEngineeringLanguage_Scenario4.setter
    def requirementEngineeringLanguage_Scenario4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_requirementEngineeringLanguage_Scenario__requirementEngineeringLanguage_Scenario4", None)
        self.__requirementEngineeringLanguage_Scenario4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirementEngineeringLanguage_Given"):
                opp_val = getattr(old_value, "requirementEngineeringLanguage_Given", None)
                if opp_val == self:
                    setattr(old_value, "requirementEngineeringLanguage_Given", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirementEngineeringLanguage_Given"):
                opp_val = getattr(value, "requirementEngineeringLanguage_Given", None)
                setattr(value, "requirementEngineeringLanguage_Given", self)
