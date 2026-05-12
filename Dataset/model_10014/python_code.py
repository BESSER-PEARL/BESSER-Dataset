from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    black = "black"
    red = "red"
    green = "green"
    yellow = "yellow"
    orange = "orange"
    brown = "brown"
    pink = "pink"


############################################
# Definition of Classes
############################################

class OclTest_Tree:

    def __init__(self, name: str, OclTest_Tree: set["OclTest_Fruit"] = None, OclTest_Tree17: set["OclTest_Fruit"] = None):
        self.name = name
        self.OclTest_Tree = OclTest_Tree if OclTest_Tree is not None else set()
        self.OclTest_Tree17 = OclTest_Tree17 if OclTest_Tree17 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def OclTest_Tree(self):
        return self.__OclTest_Tree

    @OclTest_Tree.setter
    def OclTest_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Tree__OclTest_Tree", None)
        self.__OclTest_Tree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit15"):
                    opp_val = getattr(item, "OclTest_Fruit15", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit15"):
                    opp_val = getattr(item, "OclTest_Fruit15", None)
                    
                    setattr(item, "OclTest_Fruit15", self)
                    

    @property
    def OclTest_Tree17(self):
        return self.__OclTest_Tree17

    @OclTest_Tree17.setter
    def OclTest_Tree17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Tree__OclTest_Tree17", None)
        self.__OclTest_Tree17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit18"):
                    opp_val = getattr(item, "OclTest_Fruit18", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit18"):
                    opp_val = getattr(item, "OclTest_Fruit18", None)
                    
                    setattr(item, "OclTest_Fruit18", self)
                    

class OclTest_Stem:

    pass
class Fruit:

    pass
class OclTest_Apple(Fruit):

    def __init__(self, label: str, OclTest_Apple: "OclTest_Stem" = None):
        self.label = label
        self.OclTest_Apple = OclTest_Apple
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def OclTest_Apple(self):
        return self.__OclTest_Apple

    @OclTest_Apple.setter
    def OclTest_Apple(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Apple__OclTest_Apple", None)
        self.__OclTest_Apple = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_Stem"):
                opp_val = getattr(old_value, "OclTest_Stem", None)
                if opp_val == self:
                    setattr(old_value, "OclTest_Stem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_Stem"):
                opp_val = getattr(value, "OclTest_Stem", None)
                setattr(value, "OclTest_Stem", self)

    def preferredLabel(self, OclTest_text) :
        # TODO: Implement preferredLabel method
        pass

    def label(self, OclTest_text):
        # TODO: Implement label method
        pass

    def newApple(self) :
        # TODO: Implement newApple method
        pass

class OclTest_Fruit(ABC):

    def __init__(self, color: str, name: str, OclTest_Fruit: "OclTest_Fruit" = None, OclTest_Fruit0: set["OclTest_Fruit"] = None, OclTest_Fruit4: "OclTest_FruitUtil" = None, OclTest_Fruit7: "OclTest_FruitUtil" = None, OclTest_Fruit10: "OclTest_FruitUtil" = None, OclTest_Fruit13: "OclTest_FruitUtil" = None, OclTest_Fruit15: "OclTest_Tree" = None, OclTest_Fruit18: "OclTest_Tree" = None):
        self.color = color
        self.name = name
        self.OclTest_Fruit = OclTest_Fruit
        self.OclTest_Fruit0 = OclTest_Fruit0 if OclTest_Fruit0 is not None else set()
        self.OclTest_Fruit4 = OclTest_Fruit4
        self.OclTest_Fruit7 = OclTest_Fruit7
        self.OclTest_Fruit10 = OclTest_Fruit10
        self.OclTest_Fruit13 = OclTest_Fruit13
        self.OclTest_Fruit15 = OclTest_Fruit15
        self.OclTest_Fruit18 = OclTest_Fruit18
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def OclTest_Fruit10(self):
        return self.__OclTest_Fruit10

    @OclTest_Fruit10.setter
    def OclTest_Fruit10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit10", None)
        self.__OclTest_Fruit10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_FruitUtil9"):
                opp_val = getattr(old_value, "OclTest_FruitUtil9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_FruitUtil9"):
                opp_val = getattr(value, "OclTest_FruitUtil9", None)
                if opp_val is None:
                    setattr(value, "OclTest_FruitUtil9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit7(self):
        return self.__OclTest_Fruit7

    @OclTest_Fruit7.setter
    def OclTest_Fruit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit7", None)
        self.__OclTest_Fruit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_FruitUtil6"):
                opp_val = getattr(old_value, "OclTest_FruitUtil6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_FruitUtil6"):
                opp_val = getattr(value, "OclTest_FruitUtil6", None)
                if opp_val is None:
                    setattr(value, "OclTest_FruitUtil6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit18(self):
        return self.__OclTest_Fruit18

    @OclTest_Fruit18.setter
    def OclTest_Fruit18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit18", None)
        self.__OclTest_Fruit18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_Tree17"):
                opp_val = getattr(old_value, "OclTest_Tree17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_Tree17"):
                opp_val = getattr(value, "OclTest_Tree17", None)
                if opp_val is None:
                    setattr(value, "OclTest_Tree17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit4(self):
        return self.__OclTest_Fruit4

    @OclTest_Fruit4.setter
    def OclTest_Fruit4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit4", None)
        self.__OclTest_Fruit4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_FruitUtil"):
                opp_val = getattr(old_value, "OclTest_FruitUtil", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_FruitUtil"):
                opp_val = getattr(value, "OclTest_FruitUtil", None)
                if opp_val is None:
                    setattr(value, "OclTest_FruitUtil", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit0(self):
        return self.__OclTest_Fruit0

    @OclTest_Fruit0.setter
    def OclTest_Fruit0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit0", None)
        self.__OclTest_Fruit0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit"):
                    opp_val = getattr(item, "OclTest_Fruit", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit"):
                    opp_val = getattr(item, "OclTest_Fruit", None)
                    
                    setattr(item, "OclTest_Fruit", self)
                    

    @property
    def OclTest_Fruit13(self):
        return self.__OclTest_Fruit13

    @OclTest_Fruit13.setter
    def OclTest_Fruit13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit13", None)
        self.__OclTest_Fruit13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_FruitUtil12"):
                opp_val = getattr(old_value, "OclTest_FruitUtil12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_FruitUtil12"):
                opp_val = getattr(value, "OclTest_FruitUtil12", None)
                if opp_val is None:
                    setattr(value, "OclTest_FruitUtil12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit15(self):
        return self.__OclTest_Fruit15

    @OclTest_Fruit15.setter
    def OclTest_Fruit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit15", None)
        self.__OclTest_Fruit15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_Tree"):
                opp_val = getattr(old_value, "OclTest_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_Tree"):
                opp_val = getattr(value, "OclTest_Tree", None)
                if opp_val is None:
                    setattr(value, "OclTest_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def OclTest_Fruit(self):
        return self.__OclTest_Fruit

    @OclTest_Fruit.setter
    def OclTest_Fruit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_Fruit__OclTest_Fruit", None)
        self.__OclTest_Fruit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OclTest_Fruit0"):
                opp_val = getattr(old_value, "OclTest_Fruit0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OclTest_Fruit0"):
                opp_val = getattr(value, "OclTest_Fruit0", None)
                if opp_val is None:
                    setattr(value, "OclTest_Fruit0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def ripen(self, OclTest_color) :
        # TODO: Implement ripen method
        pass

    def setColor(self, OclTest_newColor, OclTest_fruit):
        # TODO: Implement setColor method
        pass

    def preferredColor(self) :
        # TODO: Implement preferredColor method
        pass

    def newFruit(self) :
        # TODO: Implement newFruit method
        pass

class OclTest_FruitUtil:

    def __init__(self, OclTest_FruitUtil: set["OclTest_Fruit"] = None, OclTest_FruitUtil6: set["OclTest_Fruit"] = None, OclTest_FruitUtil9: set["OclTest_Fruit"] = None, OclTest_FruitUtil12: set["OclTest_Fruit"] = None):
        self.OclTest_FruitUtil = OclTest_FruitUtil if OclTest_FruitUtil is not None else set()
        self.OclTest_FruitUtil6 = OclTest_FruitUtil6 if OclTest_FruitUtil6 is not None else set()
        self.OclTest_FruitUtil9 = OclTest_FruitUtil9 if OclTest_FruitUtil9 is not None else set()
        self.OclTest_FruitUtil12 = OclTest_FruitUtil12 if OclTest_FruitUtil12 is not None else set()
        
        pass
    @property
    def OclTest_FruitUtil(self):
        return self.__OclTest_FruitUtil

    @OclTest_FruitUtil.setter
    def OclTest_FruitUtil(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_FruitUtil__OclTest_FruitUtil", None)
        self.__OclTest_FruitUtil = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit4"):
                    opp_val = getattr(item, "OclTest_Fruit4", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit4"):
                    opp_val = getattr(item, "OclTest_Fruit4", None)
                    
                    setattr(item, "OclTest_Fruit4", self)
                    

    @property
    def OclTest_FruitUtil12(self):
        return self.__OclTest_FruitUtil12

    @OclTest_FruitUtil12.setter
    def OclTest_FruitUtil12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_FruitUtil__OclTest_FruitUtil12", None)
        self.__OclTest_FruitUtil12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit13"):
                    opp_val = getattr(item, "OclTest_Fruit13", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit13"):
                    opp_val = getattr(item, "OclTest_Fruit13", None)
                    
                    setattr(item, "OclTest_Fruit13", self)
                    

    @property
    def OclTest_FruitUtil6(self):
        return self.__OclTest_FruitUtil6

    @OclTest_FruitUtil6.setter
    def OclTest_FruitUtil6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_FruitUtil__OclTest_FruitUtil6", None)
        self.__OclTest_FruitUtil6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit7"):
                    opp_val = getattr(item, "OclTest_Fruit7", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit7"):
                    opp_val = getattr(item, "OclTest_Fruit7", None)
                    
                    setattr(item, "OclTest_Fruit7", self)
                    

    @property
    def OclTest_FruitUtil9(self):
        return self.__OclTest_FruitUtil9

    @OclTest_FruitUtil9.setter
    def OclTest_FruitUtil9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OclTest_FruitUtil__OclTest_FruitUtil9", None)
        self.__OclTest_FruitUtil9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OclTest_Fruit10"):
                    opp_val = getattr(item, "OclTest_Fruit10", None)
                    
                    if opp_val == self:
                        setattr(item, "OclTest_Fruit10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OclTest_Fruit10"):
                    opp_val = getattr(item, "OclTest_Fruit10", None)
                    
                    setattr(item, "OclTest_Fruit10", self)
                    

    def processBag(self, OclTest_fruits) :
        # TODO: Implement processBag method
        pass

    def processSet(self, OclTest_fruits) :
        # TODO: Implement processSet method
        pass

    def processOrderedSet(self, OclTest_fruits) :
        # TODO: Implement processOrderedSet method
        pass

    def processSequence(self, OclTest_fruits) :
        # TODO: Implement processSequence method
        pass
