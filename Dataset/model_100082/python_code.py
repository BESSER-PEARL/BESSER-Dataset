from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ShellCmd:

    pass
class kbuild_Include(ShellCmd):

    pass
class BuildEntry:

    pass
class kbuild_HostProgram(BuildEntry):

    def __init__(self, name: str, kbuild_HostProgram: "kbuild_Variable" = None, kbuild_HostProgram24: "kbuild_Assign" = None):
        self.name = name
        self.kbuild_HostProgram = kbuild_HostProgram
        self.kbuild_HostProgram24 = kbuild_HostProgram24
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kbuild_HostProgram(self):
        return self.__kbuild_HostProgram

    @kbuild_HostProgram.setter
    def kbuild_HostProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_HostProgram__kbuild_HostProgram", None)
        self.__kbuild_HostProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_Variable22"):
                opp_val = getattr(old_value, "kbuild_Variable22", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_Variable22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_Variable22"):
                opp_val = getattr(value, "kbuild_Variable22", None)
                setattr(value, "kbuild_Variable22", self)

    @property
    def kbuild_HostProgram24(self):
        return self.__kbuild_HostProgram24

    @kbuild_HostProgram24.setter
    def kbuild_HostProgram24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_HostProgram__kbuild_HostProgram24", None)
        self.__kbuild_HostProgram24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_Assign"):
                opp_val = getattr(old_value, "kbuild_Assign", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_Assign", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_Assign"):
                opp_val = getattr(value, "kbuild_Assign", None)
                setattr(value, "kbuild_Assign", self)

class kbuild_Object(BuildEntry):

    pass
class kbuild_IfNEq(BuildEntry):

    pass
class kbuild_Ifndef(BuildEntry):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class kbuild_IfEq(BuildEntry):

    pass
class Value:

    pass
class kbuild_ObjectSingleFile(Value):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class kbuild_ObjectString(Value):

    pass
class kbuild_ObjectShellCmd(Value):

    pass
class kbuild_ObjectDir(Value):

    pass
class kbuild_ObjectShellChar(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class kbuild_ObjectVariable(Value):

    def __init__(self, additional: str, kbuild_ObjectVariable: "kbuild_Variable" = None):
        self.additional = additional
        self.kbuild_ObjectVariable = kbuild_ObjectVariable
        
        pass
    @property
    def additional(self):
        return self.__additional

    @additional.setter
    def additional(self, additional: str):
        self.__additional = additional


    @property
    def kbuild_ObjectVariable(self):
        return self.__kbuild_ObjectVariable

    @kbuild_ObjectVariable.setter
    def kbuild_ObjectVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_ObjectVariable__kbuild_ObjectVariable", None)
        self.__kbuild_ObjectVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_Variable37"):
                opp_val = getattr(old_value, "kbuild_Variable37", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_Variable37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_Variable37"):
                opp_val = getattr(value, "kbuild_Variable37", None)
                setattr(value, "kbuild_Variable37", self)

class kbuild_ObjectFile(Value):

    pass
class Object_M:

    pass
class kbuild_Obj_m(Object_M):

    pass
class Object_Y:

    pass
class kbuild_Obj_y(Object_Y):

    pass
class kbuild_MyVariable(BuildEntry):

    def __init__(self, name: str, kbuild_MyVariable: "kbuild_Variable" = None):
        self.name = name
        self.kbuild_MyVariable = kbuild_MyVariable
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kbuild_MyVariable(self):
        return self.__kbuild_MyVariable

    @kbuild_MyVariable.setter
    def kbuild_MyVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_MyVariable__kbuild_MyVariable", None)
        self.__kbuild_MyVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_Variable31"):
                opp_val = getattr(old_value, "kbuild_Variable31", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_Variable31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_Variable31"):
                opp_val = getattr(value, "kbuild_Variable31", None)
                setattr(value, "kbuild_Variable31", self)

class kbuild_Target(BuildEntry):

    pass
class kbuild_ShellCmd:

    def __init__(self, name: str, kbuild_ShellCmd15: set["kbuild_ShellPart"] = None, kbuild_ShellCmd: "kbuild_If" = None, kbuild_ShellCmd20: "kbuild_ShellPart" = None, kbuild_ShellCmd39: "kbuild_ObjectShellCmd" = None):
        self.name = name
        self.kbuild_ShellCmd15 = kbuild_ShellCmd15 if kbuild_ShellCmd15 is not None else set()
        self.kbuild_ShellCmd = kbuild_ShellCmd
        self.kbuild_ShellCmd20 = kbuild_ShellCmd20
        self.kbuild_ShellCmd39 = kbuild_ShellCmd39
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kbuild_ShellCmd15(self):
        return self.__kbuild_ShellCmd15

    @kbuild_ShellCmd15.setter
    def kbuild_ShellCmd15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_ShellCmd__kbuild_ShellCmd15", None)
        self.__kbuild_ShellCmd15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kbuild_ShellPart"):
                    opp_val = getattr(item, "kbuild_ShellPart", None)
                    
                    if opp_val == self:
                        setattr(item, "kbuild_ShellPart", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kbuild_ShellPart"):
                    opp_val = getattr(item, "kbuild_ShellPart", None)
                    
                    setattr(item, "kbuild_ShellPart", self)
                    

    @property
    def kbuild_ShellCmd20(self):
        return self.__kbuild_ShellCmd20

    @kbuild_ShellCmd20.setter
    def kbuild_ShellCmd20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_ShellCmd__kbuild_ShellCmd20", None)
        self.__kbuild_ShellCmd20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_ShellPart19"):
                opp_val = getattr(old_value, "kbuild_ShellPart19", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_ShellPart19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_ShellPart19"):
                opp_val = getattr(value, "kbuild_ShellPart19", None)
                setattr(value, "kbuild_ShellPart19", self)

    @property
    def kbuild_ShellCmd(self):
        return self.__kbuild_ShellCmd

    @kbuild_ShellCmd.setter
    def kbuild_ShellCmd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_ShellCmd__kbuild_ShellCmd", None)
        self.__kbuild_ShellCmd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_If"):
                opp_val = getattr(old_value, "kbuild_If", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_If", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_If"):
                opp_val = getattr(value, "kbuild_If", None)
                setattr(value, "kbuild_If", self)

    @property
    def kbuild_ShellCmd39(self):
        return self.__kbuild_ShellCmd39

    @kbuild_ShellCmd39.setter
    def kbuild_ShellCmd39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_ShellCmd__kbuild_ShellCmd39", None)
        self.__kbuild_ShellCmd39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_ObjectShellCmd"):
                opp_val = getattr(old_value, "kbuild_ObjectShellCmd", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_ObjectShellCmd", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_ObjectShellCmd"):
                opp_val = getattr(value, "kbuild_ObjectShellCmd", None)
                setattr(value, "kbuild_ObjectShellCmd", self)

class kbuild_If:

    pass
class kbuild_AssignExtra:

    pass
class kbuild_Entry:

    pass
class kbuild_EObject:

    pass
class kbuild_BuildEntry:

    pass
class kbuild_VarSlashSym:

    def __init__(self, name: str, kbuild_VarSlashSym: "kbuild_ShellPart" = None):
        self.name = name
        self.kbuild_VarSlashSym = kbuild_VarSlashSym
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kbuild_VarSlashSym(self):
        return self.__kbuild_VarSlashSym

    @kbuild_VarSlashSym.setter
    def kbuild_VarSlashSym(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kbuild_VarSlashSym__kbuild_VarSlashSym", None)
        self.__kbuild_VarSlashSym = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kbuild_ShellPart17"):
                opp_val = getattr(old_value, "kbuild_ShellPart17", None)
                if opp_val == self:
                    setattr(old_value, "kbuild_ShellPart17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kbuild_ShellPart17"):
                opp_val = getattr(value, "kbuild_ShellPart17", None)
                setattr(value, "kbuild_ShellPart17", self)

class kbuild_ShellPart:

    pass
class VarSlashSym:

    pass
class If:

    pass
class kbuild_Variable(VarSlashSym, If):

    pass
class kbuild_Value:

    pass
class Assign:

    pass
class kbuild_Values(Assign):

    pass
class AssignExtra:

    pass
class kbuild_Assign(AssignExtra):

    pass
class kbuild_Object_M:

    pass
class kbuild_Object_Y:

    pass
class kbuild_Model:

    pass