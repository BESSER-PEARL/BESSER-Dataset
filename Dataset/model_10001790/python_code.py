from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Calculate_caloriesBurnt:

    def __init__(self, Name: str, CaloriesBurnt: str, Steps: int, count_Steps_and_Calories3: "Count_Steps_and_Calories" = None):
        self.Name = Name
        self.CaloriesBurnt = CaloriesBurnt
        self.Steps = Steps
        self.count_Steps_and_Calories3 = count_Steps_and_Calories3
        
        pass
    @property
    def CaloriesBurnt(self):
        return self.__CaloriesBurnt
    @CaloriesBurnt.setter
    def CaloriesBurnt(self, CaloriesBurnt: str):
        self.__CaloriesBurnt = CaloriesBurnt

    @property
    def Steps(self):
        return self.__Steps
    @Steps.setter
    def Steps(self, Steps: int):
        self.__Steps = Steps

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def count_Steps_and_Calories3(self):
        return self.__count_Steps_and_Calories3
    @count_Steps_and_Calories3.setter
    def count_Steps_and_Calories3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Calculate_caloriesBurnt__count_Steps_and_Calories3", None)
        self.__count_Steps_and_Calories3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "calculate_caloriesBurnt2"):
                opp_val = getattr(old_value, "calculate_caloriesBurnt2", None)
                if opp_val == self:
                    setattr(old_value, "calculate_caloriesBurnt2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "calculate_caloriesBurnt2"):
                opp_val = getattr(value, "calculate_caloriesBurnt2", None)
                setattr(value, "calculate_caloriesBurnt2", self)



class Count_Steps:

    def __init__(self, Steps: int, count_Steps_and_Calories1: "Count_Steps_and_Calories" = None):
        self.Steps = Steps
        self.count_Steps_and_Calories1 = count_Steps_and_Calories1
        
        pass
    @property
    def Steps(self):
        return self.__Steps
    @Steps.setter
    def Steps(self, Steps: int):
        self.__Steps = Steps

    @property
    def count_Steps_and_Calories1(self):
        return self.__count_Steps_and_Calories1
    @count_Steps_and_Calories1.setter
    def count_Steps_and_Calories1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Count_Steps__count_Steps_and_Calories1", None)
        self.__count_Steps_and_Calories1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "count_Steps0"):
                opp_val = getattr(old_value, "count_Steps0", None)
                if opp_val == self:
                    setattr(old_value, "count_Steps0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "count_Steps0"):
                opp_val = getattr(value, "count_Steps0", None)
                setattr(value, "count_Steps0", self)



class Give_Weight:

    def __init__(self, Weight: int, update_Data7: "Update_Data" = None):
        self.Weight = Weight
        self.update_Data7 = update_Data7
        
        pass
    @property
    def Weight(self):
        return self.__Weight
    @Weight.setter
    def Weight(self, Weight: int):
        self.__Weight = Weight

    @property
    def update_Data7(self):
        return self.__update_Data7
    @update_Data7.setter
    def update_Data7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Give_Weight__update_Data7", None)
        self.__update_Data7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "give_Weight6"):
                opp_val = getattr(old_value, "give_Weight6", None)
                if opp_val == self:
                    setattr(old_value, "give_Weight6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "give_Weight6"):
                opp_val = getattr(value, "give_Weight6", None)
                setattr(value, "give_Weight6", self)



class Give_Name:

    def __init__(self, Name: str, update_Data5: "Update_Data" = None):
        self.Name = Name
        self.update_Data5 = update_Data5
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def update_Data5(self):
        return self.__update_Data5
    @update_Data5.setter
    def update_Data5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Give_Name__update_Data5", None)
        self.__update_Data5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "give_Name4"):
                opp_val = getattr(old_value, "give_Name4", None)
                if opp_val == self:
                    setattr(old_value, "give_Name4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "give_Name4"):
                opp_val = getattr(value, "give_Name4", None)
                setattr(value, "give_Name4", self)



class Weekly_Chart:

    def __init__(self, Name: str, CaloriesBurnt: str, Steps: int):
        self.Name = Name
        self.CaloriesBurnt = CaloriesBurnt
        self.Steps = Steps
        
        pass
    @property
    def Steps(self):
        return self.__Steps
    @Steps.setter
    def Steps(self, Steps: int):
        self.__Steps = Steps

    @property
    def CaloriesBurnt(self):
        return self.__CaloriesBurnt
    @CaloriesBurnt.setter
    def CaloriesBurnt(self, CaloriesBurnt: str):
        self.__CaloriesBurnt = CaloriesBurnt

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Update_Data:

    def __init__(self, Name: str, Weight: int, give_Name4: "Give_Name" = None, give_Weight6: "Give_Weight" = None):
        self.Name = Name
        self.Weight = Weight
        self.give_Name4 = give_Name4
        self.give_Weight6 = give_Weight6
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Weight(self):
        return self.__Weight
    @Weight.setter
    def Weight(self, Weight: int):
        self.__Weight = Weight

    @property
    def give_Weight6(self):
        return self.__give_Weight6
    @give_Weight6.setter
    def give_Weight6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Update_Data__give_Weight6", None)
        self.__give_Weight6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "update_Data7"):
                opp_val = getattr(old_value, "update_Data7", None)
                if opp_val == self:
                    setattr(old_value, "update_Data7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "update_Data7"):
                opp_val = getattr(value, "update_Data7", None)
                setattr(value, "update_Data7", self)

    @property
    def give_Name4(self):
        return self.__give_Name4
    @give_Name4.setter
    def give_Name4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Update_Data__give_Name4", None)
        self.__give_Name4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "update_Data5"):
                opp_val = getattr(old_value, "update_Data5", None)
                if opp_val == self:
                    setattr(old_value, "update_Data5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "update_Data5"):
                opp_val = getattr(value, "update_Data5", None)
                setattr(value, "update_Data5", self)



class Draw_Path:

    def __init__(self, Name: str, Route: str):
        self.Name = Name
        self.Route = Route
        
        pass
    @property
    def Route(self):
        return self.__Route
    @Route.setter
    def Route(self, Route: str):
        self.__Route = Route

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class Count_Steps_and_Calories:

    def __init__(self, Name: str, Steps: int, CaloriesBurnt: str, count_Steps0: "Count_Steps" = None, calculate_caloriesBurnt2: "Calculate_caloriesBurnt" = None):
        self.Name = Name
        self.Steps = Steps
        self.CaloriesBurnt = CaloriesBurnt
        self.count_Steps0 = count_Steps0
        self.calculate_caloriesBurnt2 = calculate_caloriesBurnt2
        
        pass
    @property
    def Steps(self):
        return self.__Steps
    @Steps.setter
    def Steps(self, Steps: int):
        self.__Steps = Steps

    @property
    def CaloriesBurnt(self):
        return self.__CaloriesBurnt
    @CaloriesBurnt.setter
    def CaloriesBurnt(self, CaloriesBurnt: str):
        self.__CaloriesBurnt = CaloriesBurnt

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def calculate_caloriesBurnt2(self):
        return self.__calculate_caloriesBurnt2
    @calculate_caloriesBurnt2.setter
    def calculate_caloriesBurnt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Count_Steps_and_Calories__calculate_caloriesBurnt2", None)
        self.__calculate_caloriesBurnt2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "count_Steps_and_Calories3"):
                opp_val = getattr(old_value, "count_Steps_and_Calories3", None)
                if opp_val == self:
                    setattr(old_value, "count_Steps_and_Calories3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "count_Steps_and_Calories3"):
                opp_val = getattr(value, "count_Steps_and_Calories3", None)
                setattr(value, "count_Steps_and_Calories3", self)

    @property
    def count_Steps0(self):
        return self.__count_Steps0
    @count_Steps0.setter
    def count_Steps0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Count_Steps_and_Calories__count_Steps0", None)
        self.__count_Steps0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "count_Steps_and_Calories1"):
                opp_val = getattr(old_value, "count_Steps_and_Calories1", None)
                if opp_val == self:
                    setattr(old_value, "count_Steps_and_Calories1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "count_Steps_and_Calories1"):
                opp_val = getattr(value, "count_Steps_and_Calories1", None)
                setattr(value, "count_Steps_and_Calories1", self)



class User:

    def __init__(self, Name: str, Weight: int, Steps: int, Calories_Burnt: str, Path_Drawn: str):
        self.Name = Name
        self.Weight = Weight
        self.Steps = Steps
        self.Calories_Burnt = Calories_Burnt
        self.Path_Drawn = Path_Drawn
        
        pass
    @property
    def Path_Drawn(self):
        return self.__Path_Drawn
    @Path_Drawn.setter
    def Path_Drawn(self, Path_Drawn: str):
        self.__Path_Drawn = Path_Drawn

    @property
    def Calories_Burnt(self):
        return self.__Calories_Burnt
    @Calories_Burnt.setter
    def Calories_Burnt(self, Calories_Burnt: str):
        self.__Calories_Burnt = Calories_Burnt

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Steps(self):
        return self.__Steps
    @Steps.setter
    def Steps(self, Steps: int):
        self.__Steps = Steps

    @property
    def Weight(self):
        return self.__Weight
    @Weight.setter
    def Weight(self, Weight: int):
        self.__Weight = Weight

