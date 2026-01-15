from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class kmLogo_VM_Segment:

    pass
class kmLogo_VM_Point:

    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

class Segment:

    pass
class Point:

    pass
class kmLogo_VM_Turtle:

    def __init__(self, heading: str, penUp: str, kmLogo_VM_Turtle: "Point" = None, kmLogo_VM_Turtle2: set["Segment"] = None, kmLogo_VM_Turtle4: set["Point"] = None):
        self.heading = heading
        self.penUp = penUp
        self.kmLogo_VM_Turtle = kmLogo_VM_Turtle
        self.kmLogo_VM_Turtle2 = kmLogo_VM_Turtle2 if kmLogo_VM_Turtle2 is not None else set()
        self.kmLogo_VM_Turtle4 = kmLogo_VM_Turtle4 if kmLogo_VM_Turtle4 is not None else set()
        
    @property
    def penUp(self) -> str:
        return self.__penUp

    @penUp.setter
    def penUp(self, penUp: str):
        self.__penUp = penUp

    @property
    def heading(self) -> str:
        return self.__heading

    @heading.setter
    def heading(self, heading: str):
        self.__heading = heading

    @property
    def kmLogo_VM_Turtle(self):
        return self.__kmLogo_VM_Turtle

    @kmLogo_VM_Turtle.setter
    def kmLogo_VM_Turtle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_VM_Turtle__kmLogo_VM_Turtle", None)
        self.__kmLogo_VM_Turtle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Point"):
                opp_val = getattr(old_value, "Point", None)
                if opp_val == self:
                    setattr(old_value, "Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Point"):
                opp_val = getattr(value, "Point", None)
                setattr(value, "Point", self)

    @property
    def kmLogo_VM_Turtle2(self):
        return self.__kmLogo_VM_Turtle2

    @kmLogo_VM_Turtle2.setter
    def kmLogo_VM_Turtle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_VM_Turtle__kmLogo_VM_Turtle2", None)
        self.__kmLogo_VM_Turtle2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Segment"):
                    opp_val = getattr(item, "Segment", None)
                    
                    if opp_val == self:
                        setattr(item, "Segment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Segment"):
                    opp_val = getattr(item, "Segment", None)
                    
                    setattr(item, "Segment", self)
                    

    @property
    def kmLogo_VM_Turtle4(self):
        return self.__kmLogo_VM_Turtle4

    @kmLogo_VM_Turtle4.setter
    def kmLogo_VM_Turtle4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kmLogo_VM_Turtle__kmLogo_VM_Turtle4", None)
        self.__kmLogo_VM_Turtle4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Point5"):
                    opp_val = getattr(item, "Point5", None)
                    
                    if opp_val == self:
                        setattr(item, "Point5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Point5"):
                    opp_val = getattr(item, "Point5", None)
                    
                    setattr(item, "Point5", self)
                    
