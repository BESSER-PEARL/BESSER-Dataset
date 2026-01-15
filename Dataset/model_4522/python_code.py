from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class vmlogo_StackFrame:

    def __init__(self, variables: str, vmlogo_StackFrame: "vmlogo_CallStack" = None):
        self.variables = variables
        self.vmlogo_StackFrame = vmlogo_StackFrame
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def vmlogo_StackFrame(self):
        return self.__vmlogo_StackFrame

    @vmlogo_StackFrame.setter
    def vmlogo_StackFrame(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_StackFrame__vmlogo_StackFrame", None)
        self.__vmlogo_StackFrame = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_CallStack14"):
                opp_val = getattr(old_value, "vmlogo_CallStack14", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_CallStack14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_CallStack14"):
                opp_val = getattr(value, "vmlogo_CallStack14", None)
                setattr(value, "vmlogo_CallStack14", self)

class vmlogo_Segment:

    pass
class vmlogo_Point:

    def __init__(self, x: float, y: float, vmlogo_Point: "vmlogo_Turtle" = None, vmlogo_Point9: "vmlogo_Segment" = None, vmlogo_Point12: "vmlogo_Segment" = None):
        self.x = x
        self.y = y
        self.vmlogo_Point = vmlogo_Point
        self.vmlogo_Point9 = vmlogo_Point9
        self.vmlogo_Point12 = vmlogo_Point12
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def vmlogo_Point(self):
        return self.__vmlogo_Point

    @vmlogo_Point.setter
    def vmlogo_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point", None)
        self.__vmlogo_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Turtle4"):
                opp_val = getattr(old_value, "vmlogo_Turtle4", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Turtle4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Turtle4"):
                opp_val = getattr(value, "vmlogo_Turtle4", None)
                setattr(value, "vmlogo_Turtle4", self)

    @property
    def vmlogo_Point12(self):
        return self.__vmlogo_Point12

    @vmlogo_Point12.setter
    def vmlogo_Point12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point12", None)
        self.__vmlogo_Point12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Segment11"):
                opp_val = getattr(old_value, "vmlogo_Segment11", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Segment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Segment11"):
                opp_val = getattr(value, "vmlogo_Segment11", None)
                setattr(value, "vmlogo_Segment11", self)

    @property
    def vmlogo_Point9(self):
        return self.__vmlogo_Point9

    @vmlogo_Point9.setter
    def vmlogo_Point9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point9", None)
        self.__vmlogo_Point9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Segment8"):
                opp_val = getattr(old_value, "vmlogo_Segment8", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Segment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Segment8"):
                opp_val = getattr(value, "vmlogo_Segment8", None)
                setattr(value, "vmlogo_Segment8", self)

class vmlogo_CallStack:

    pass
class vmlogo_Turtle:

    def __init__(self, heading: float, penUp: bool, vmlogo_Turtle: "vmlogo_Context" = None, vmlogo_Turtle4: "vmlogo_Point" = None, vmlogo_Turtle6: "vmlogo_Segment" = None):
        self.heading = heading
        self.penUp = penUp
        self.vmlogo_Turtle = vmlogo_Turtle
        self.vmlogo_Turtle4 = vmlogo_Turtle4
        self.vmlogo_Turtle6 = vmlogo_Turtle6
        
    @property
    def penUp(self) -> bool:
        return self.__penUp

    @penUp.setter
    def penUp(self, penUp: bool):
        self.__penUp = penUp

    @property
    def heading(self) -> float:
        return self.__heading

    @heading.setter
    def heading(self, heading: float):
        self.__heading = heading

    @property
    def vmlogo_Turtle(self):
        return self.__vmlogo_Turtle

    @vmlogo_Turtle.setter
    def vmlogo_Turtle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle", None)
        self.__vmlogo_Turtle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Context"):
                opp_val = getattr(old_value, "vmlogo_Context", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Context", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Context"):
                opp_val = getattr(value, "vmlogo_Context", None)
                setattr(value, "vmlogo_Context", self)

    @property
    def vmlogo_Turtle4(self):
        return self.__vmlogo_Turtle4

    @vmlogo_Turtle4.setter
    def vmlogo_Turtle4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle4", None)
        self.__vmlogo_Turtle4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Point"):
                opp_val = getattr(old_value, "vmlogo_Point", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Point"):
                opp_val = getattr(value, "vmlogo_Point", None)
                setattr(value, "vmlogo_Point", self)

    @property
    def vmlogo_Turtle6(self):
        return self.__vmlogo_Turtle6

    @vmlogo_Turtle6.setter
    def vmlogo_Turtle6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle6", None)
        self.__vmlogo_Turtle6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Segment"):
                opp_val = getattr(old_value, "vmlogo_Segment", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Segment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Segment"):
                opp_val = getattr(value, "vmlogo_Segment", None)
                setattr(value, "vmlogo_Segment", self)

class vmlogo_Context:

    pass