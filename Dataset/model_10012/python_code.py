from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class LRBAC_Permission:

    def __init__(self, PermName: str, Permission19: "LRBAC_Location" = None, Permission21: "LRBAC_Location" = None, Permission: "LRBAC_Role" = None, PermRoleLoc: "LRBAC_Location" = None, PermObjLoc: "LRBAC_Location" = None, Permission34: "LRBAC_Object" = None, Permission36: "LRBAC_Operation" = None, OperPerm: "LRBAC_Operation" = None, ObjPerm: "LRBAC_Object" = None, RolePerm: "LRBAC_Role" = None):
        self.PermName = PermName
        self.Permission19 = Permission19
        self.Permission21 = Permission21
        self.Permission = Permission
        self.PermRoleLoc = PermRoleLoc
        self.PermObjLoc = PermObjLoc
        self.Permission34 = Permission34
        self.Permission36 = Permission36
        self.OperPerm = OperPerm
        self.ObjPerm = ObjPerm
        self.RolePerm = RolePerm
        
        pass
    @property
    def PermName(self):
        return self.__PermName

    @PermName.setter
    def PermName(self, PermName: str):
        self.__PermName = PermName


    @property
    def PermObjLoc(self):
        return self.__PermObjLoc

    @PermObjLoc.setter
    def PermObjLoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__PermObjLoc", None)
        self.__PermObjLoc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location30"):
                opp_val = getattr(old_value, "Location30", None)
                if opp_val == self:
                    setattr(old_value, "Location30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location30"):
                opp_val = getattr(value, "Location30", None)
                setattr(value, "Location30", self)

    @property
    def Permission19(self):
        return self.__Permission19

    @Permission19.setter
    def Permission19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__Permission19", None)
        self.__Permission19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoleLocPerm"):
                opp_val = getattr(old_value, "RoleLocPerm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoleLocPerm"):
                opp_val = getattr(value, "RoleLocPerm", None)
                if opp_val is None:
                    setattr(value, "RoleLocPerm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RolePerm(self):
        return self.__RolePerm

    @RolePerm.setter
    def RolePerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__RolePerm", None)
        self.__RolePerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role26"):
                opp_val = getattr(old_value, "Role26", None)
                if opp_val == self:
                    setattr(old_value, "Role26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role26"):
                opp_val = getattr(value, "Role26", None)
                setattr(value, "Role26", self)

    @property
    def OperPerm(self):
        return self.__OperPerm

    @OperPerm.setter
    def OperPerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__OperPerm", None)
        self.__OperPerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Operation"):
                opp_val = getattr(old_value, "Operation", None)
                if opp_val == self:
                    setattr(old_value, "Operation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Operation"):
                opp_val = getattr(value, "Operation", None)
                setattr(value, "Operation", self)

    @property
    def PermRoleLoc(self):
        return self.__PermRoleLoc

    @PermRoleLoc.setter
    def PermRoleLoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__PermRoleLoc", None)
        self.__PermRoleLoc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location28"):
                opp_val = getattr(old_value, "Location28", None)
                if opp_val == self:
                    setattr(old_value, "Location28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location28"):
                opp_val = getattr(value, "Location28", None)
                setattr(value, "Location28", self)

    @property
    def Permission34(self):
        return self.__Permission34

    @Permission34.setter
    def Permission34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__Permission34", None)
        self.__Permission34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PermObj"):
                opp_val = getattr(old_value, "PermObj", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PermObj"):
                opp_val = getattr(value, "PermObj", None)
                if opp_val is None:
                    setattr(value, "PermObj", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Permission36(self):
        return self.__Permission36

    @Permission36.setter
    def Permission36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__Permission36", None)
        self.__Permission36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PermOper"):
                opp_val = getattr(old_value, "PermOper", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PermOper"):
                opp_val = getattr(value, "PermOper", None)
                if opp_val is None:
                    setattr(value, "PermOper", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Permission(self):
        return self.__Permission

    @Permission.setter
    def Permission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__Permission", None)
        self.__Permission = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PermRole"):
                opp_val = getattr(old_value, "PermRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PermRole"):
                opp_val = getattr(value, "PermRole", None)
                if opp_val is None:
                    setattr(value, "PermRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ObjPerm(self):
        return self.__ObjPerm

    @ObjPerm.setter
    def ObjPerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__ObjPerm", None)
        self.__ObjPerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Object24"):
                opp_val = getattr(old_value, "Object24", None)
                if opp_val == self:
                    setattr(old_value, "Object24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Object24"):
                opp_val = getattr(value, "Object24", None)
                setattr(value, "Object24", self)

    @property
    def Permission21(self):
        return self.__Permission21

    @Permission21.setter
    def Permission21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Permission__Permission21", None)
        self.__Permission21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjLocPerm"):
                opp_val = getattr(old_value, "ObjLocPerm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjLocPerm"):
                opp_val = getattr(value, "ObjLocPerm", None)
                if opp_val is None:
                    setattr(value, "ObjLocPerm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def UpdatePermName(self, LRBAC_name):
        # TODO: Implement UpdatePermName method
        pass

class LRBAC_Object:

    def __init__(self, ObjID: int, Object: "LRBAC_Location" = None, LocObj: "LRBAC_Location" = None, PermObj: set["LRBAC_Permission"] = None, Object24: "LRBAC_Permission" = None):
        self.ObjID = ObjID
        self.Object = Object
        self.LocObj = LocObj
        self.PermObj = PermObj if PermObj is not None else set()
        self.Object24 = Object24
        
        pass
    @property
    def ObjID(self):
        return self.__ObjID

    @ObjID.setter
    def ObjID(self, ObjID: int):
        self.__ObjID = ObjID


    @property
    def LocObj(self):
        return self.__LocObj

    @LocObj.setter
    def LocObj(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Object__LocObj", None)
        self.__LocObj = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location32"):
                opp_val = getattr(old_value, "Location32", None)
                if opp_val == self:
                    setattr(old_value, "Location32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location32"):
                opp_val = getattr(value, "Location32", None)
                setattr(value, "Location32", self)

    @property
    def Object(self):
        return self.__Object

    @Object.setter
    def Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Object__Object", None)
        self.__Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjLoc"):
                opp_val = getattr(old_value, "ObjLoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjLoc"):
                opp_val = getattr(value, "ObjLoc", None)
                if opp_val is None:
                    setattr(value, "ObjLoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PermObj(self):
        return self.__PermObj

    @PermObj.setter
    def PermObj(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Object__PermObj", None)
        self.__PermObj = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission34"):
                    opp_val = getattr(item, "Permission34", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission34"):
                    opp_val = getattr(item, "Permission34", None)
                    
                    setattr(item, "Permission34", self)
                    

    @property
    def Object24(self):
        return self.__Object24

    @Object24.setter
    def Object24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Object__Object24", None)
        self.__Object24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObjPerm"):
                opp_val = getattr(old_value, "ObjPerm", None)
                if opp_val == self:
                    setattr(old_value, "ObjPerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObjPerm"):
                opp_val = getattr(value, "ObjPerm", None)
                setattr(value, "ObjPerm", self)

    def UpdateObjID(self, LRBAC_id):
        # TODO: Implement UpdateObjID method
        pass

class LRBAC_Location:

    def __init__(self, LocName: str, Location: "LRBAC_User" = None, UserLoc: set["LRBAC_User"] = None, AssignLoc: set["LRBAC_Role"] = None, ObjLoc: set["LRBAC_Object"] = None, RoleLocPerm: set["LRBAC_Permission"] = None, ObjLocPerm: set["LRBAC_Permission"] = None, Location9: "LRBAC_Role" = None, Location28: "LRBAC_Permission" = None, Location30: "LRBAC_Permission" = None, Location32: "LRBAC_Object" = None):
        self.LocName = LocName
        self.Location = Location
        self.UserLoc = UserLoc if UserLoc is not None else set()
        self.AssignLoc = AssignLoc if AssignLoc is not None else set()
        self.ObjLoc = ObjLoc if ObjLoc is not None else set()
        self.RoleLocPerm = RoleLocPerm if RoleLocPerm is not None else set()
        self.ObjLocPerm = ObjLocPerm if ObjLocPerm is not None else set()
        self.Location9 = Location9
        self.Location28 = Location28
        self.Location30 = Location30
        self.Location32 = Location32
        
        pass
    @property
    def LocName(self):
        return self.__LocName

    @LocName.setter
    def LocName(self, LocName: str):
        self.__LocName = LocName


    @property
    def ObjLocPerm(self):
        return self.__ObjLocPerm

    @ObjLocPerm.setter
    def ObjLocPerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__ObjLocPerm", None)
        self.__ObjLocPerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission21"):
                    opp_val = getattr(item, "Permission21", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission21"):
                    opp_val = getattr(item, "Permission21", None)
                    
                    setattr(item, "Permission21", self)
                    

    @property
    def Location30(self):
        return self.__Location30

    @Location30.setter
    def Location30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__Location30", None)
        self.__Location30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PermObjLoc"):
                opp_val = getattr(old_value, "PermObjLoc", None)
                if opp_val == self:
                    setattr(old_value, "PermObjLoc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PermObjLoc"):
                opp_val = getattr(value, "PermObjLoc", None)
                setattr(value, "PermObjLoc", self)

    @property
    def ObjLoc(self):
        return self.__ObjLoc

    @ObjLoc.setter
    def ObjLoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__ObjLoc", None)
        self.__ObjLoc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Object"):
                    opp_val = getattr(item, "Object", None)
                    
                    if opp_val == self:
                        setattr(item, "Object", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Object"):
                    opp_val = getattr(item, "Object", None)
                    
                    setattr(item, "Object", self)
                    

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__Location", None)
        self.__Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LocUser"):
                opp_val = getattr(old_value, "LocUser", None)
                if opp_val == self:
                    setattr(old_value, "LocUser", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LocUser"):
                opp_val = getattr(value, "LocUser", None)
                setattr(value, "LocUser", self)

    @property
    def Location32(self):
        return self.__Location32

    @Location32.setter
    def Location32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__Location32", None)
        self.__Location32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LocObj"):
                opp_val = getattr(old_value, "LocObj", None)
                if opp_val == self:
                    setattr(old_value, "LocObj", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LocObj"):
                opp_val = getattr(value, "LocObj", None)
                setattr(value, "LocObj", self)

    @property
    def AssignLoc(self):
        return self.__AssignLoc

    @AssignLoc.setter
    def AssignLoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__AssignLoc", None)
        self.__AssignLoc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role16"):
                    opp_val = getattr(item, "Role16", None)
                    
                    if opp_val == self:
                        setattr(item, "Role16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role16"):
                    opp_val = getattr(item, "Role16", None)
                    
                    setattr(item, "Role16", self)
                    

    @property
    def Location9(self):
        return self.__Location9

    @Location9.setter
    def Location9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__Location9", None)
        self.__Location9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LocAssign"):
                opp_val = getattr(old_value, "LocAssign", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LocAssign"):
                opp_val = getattr(value, "LocAssign", None)
                if opp_val is None:
                    setattr(value, "LocAssign", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UserLoc(self):
        return self.__UserLoc

    @UserLoc.setter
    def UserLoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__UserLoc", None)
        self.__UserLoc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User14"):
                    opp_val = getattr(item, "User14", None)
                    
                    if opp_val == self:
                        setattr(item, "User14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User14"):
                    opp_val = getattr(item, "User14", None)
                    
                    setattr(item, "User14", self)
                    

    @property
    def Location28(self):
        return self.__Location28

    @Location28.setter
    def Location28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__Location28", None)
        self.__Location28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PermRoleLoc"):
                opp_val = getattr(old_value, "PermRoleLoc", None)
                if opp_val == self:
                    setattr(old_value, "PermRoleLoc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PermRoleLoc"):
                opp_val = getattr(value, "PermRoleLoc", None)
                setattr(value, "PermRoleLoc", self)

    @property
    def RoleLocPerm(self):
        return self.__RoleLocPerm

    @RoleLocPerm.setter
    def RoleLocPerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Location__RoleLocPerm", None)
        self.__RoleLocPerm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission19"):
                    opp_val = getattr(item, "Permission19", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission19"):
                    opp_val = getattr(item, "Permission19", None)
                    
                    setattr(item, "Permission19", self)
                    

    def UpdateLocName(self, LRBAC_name):
        # TODO: Implement UpdateLocName method
        pass

class LRBAC_User:

    def __init__(self, Gender: str, UserName: str, UserID: int, Age: int, SessUser: set["LRBAC_Session"] = None, AssignUser: set["LRBAC_Role"] = None, User: "LRBAC_Session" = None, User7: "LRBAC_Role" = None, LocUser: "LRBAC_Location" = None, User14: "LRBAC_Location" = None):
        self.Gender = Gender
        self.UserName = UserName
        self.UserID = UserID
        self.Age = Age
        self.SessUser = SessUser if SessUser is not None else set()
        self.AssignUser = AssignUser if AssignUser is not None else set()
        self.User = User
        self.User7 = User7
        self.LocUser = LocUser
        self.User14 = User14
        
        pass
    @property
    def UserName(self):
        return self.__UserName

    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName


    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age


    @property
    def UserID(self):
        return self.__UserID

    @UserID.setter
    def UserID(self, UserID: int):
        self.__UserID = UserID


    @property
    def Gender(self):
        return self.__Gender

    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender


    @property
    def User14(self):
        return self.__User14

    @User14.setter
    def User14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__User14", None)
        self.__User14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserLoc"):
                opp_val = getattr(old_value, "UserLoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserLoc"):
                opp_val = getattr(value, "UserLoc", None)
                if opp_val is None:
                    setattr(value, "UserLoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SessUser(self):
        return self.__SessUser

    @SessUser.setter
    def SessUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__SessUser", None)
        self.__SessUser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Session"):
                    opp_val = getattr(item, "Session", None)
                    
                    if opp_val == self:
                        setattr(item, "Session", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Session"):
                    opp_val = getattr(item, "Session", None)
                    
                    setattr(item, "Session", self)
                    

    @property
    def User(self):
        return self.__User

    @User.setter
    def User(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__User", None)
        self.__User = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UserSess"):
                opp_val = getattr(old_value, "UserSess", None)
                if opp_val == self:
                    setattr(old_value, "UserSess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UserSess"):
                opp_val = getattr(value, "UserSess", None)
                setattr(value, "UserSess", self)

    @property
    def LocUser(self):
        return self.__LocUser

    @LocUser.setter
    def LocUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__LocUser", None)
        self.__LocUser = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

    @property
    def AssignUser(self):
        return self.__AssignUser

    @AssignUser.setter
    def AssignUser(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__AssignUser", None)
        self.__AssignUser = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    if opp_val == self:
                        setattr(item, "Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    setattr(item, "Role", self)
                    

    @property
    def User7(self):
        return self.__User7

    @User7.setter
    def User7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_User__User7", None)
        self.__User7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssignedRoles"):
                opp_val = getattr(old_value, "AssignedRoles", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssignedRoles"):
                opp_val = getattr(value, "AssignedRoles", None)
                if opp_val is None:
                    setattr(value, "AssignedRoles", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def UpdateUserName(self, LRBAC_name) :
        # TODO: Implement UpdateUserName method
        pass

    def AssignRole(self, LRBAC_r):
        # TODO: Implement AssignRole method
        pass

    def UpdateUserID(self, LRBAC_id):
        # TODO: Implement UpdateUserID method
        pass

    def UpdateLoc(self, LRBAC_l):
        # TODO: Implement UpdateLoc method
        pass

    def UpdateAge(self, LRBAC_age) :
        # TODO: Implement UpdateAge method
        pass

class LRBAC_Role:

    def __init__(self, RoleName: str, Role: "LRBAC_User" = None, Role4: "LRBAC_Session" = None, AssignedRoles: set["LRBAC_User"] = None, Role16: "LRBAC_Location" = None, LocAssign: set["LRBAC_Location"] = None, SessRole: set["LRBAC_Session"] = None, PermRole: set["LRBAC_Permission"] = None, Role26: "LRBAC_Permission" = None):
        self.RoleName = RoleName
        self.Role = Role
        self.Role4 = Role4
        self.AssignedRoles = AssignedRoles if AssignedRoles is not None else set()
        self.Role16 = Role16
        self.LocAssign = LocAssign if LocAssign is not None else set()
        self.SessRole = SessRole if SessRole is not None else set()
        self.PermRole = PermRole if PermRole is not None else set()
        self.Role26 = Role26
        
        pass
    @property
    def RoleName(self):
        return self.__RoleName

    @RoleName.setter
    def RoleName(self, RoleName: str):
        self.__RoleName = RoleName


    @property
    def PermRole(self):
        return self.__PermRole

    @PermRole.setter
    def PermRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__PermRole", None)
        self.__PermRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    if opp_val == self:
                        setattr(item, "Permission", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Permission"):
                    opp_val = getattr(item, "Permission", None)
                    
                    setattr(item, "Permission", self)
                    

    @property
    def AssignedRoles(self):
        return self.__AssignedRoles

    @AssignedRoles.setter
    def AssignedRoles(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__AssignedRoles", None)
        self.__AssignedRoles = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "User7"):
                    opp_val = getattr(item, "User7", None)
                    
                    if opp_val == self:
                        setattr(item, "User7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "User7"):
                    opp_val = getattr(item, "User7", None)
                    
                    setattr(item, "User7", self)
                    

    @property
    def Role4(self):
        return self.__Role4

    @Role4.setter
    def Role4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__Role4", None)
        self.__Role4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoleSess"):
                opp_val = getattr(old_value, "RoleSess", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoleSess"):
                opp_val = getattr(value, "RoleSess", None)
                if opp_val is None:
                    setattr(value, "RoleSess", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Role(self):
        return self.__Role

    @Role.setter
    def Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__Role", None)
        self.__Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssignUser"):
                opp_val = getattr(old_value, "AssignUser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssignUser"):
                opp_val = getattr(value, "AssignUser", None)
                if opp_val is None:
                    setattr(value, "AssignUser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Role16(self):
        return self.__Role16

    @Role16.setter
    def Role16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__Role16", None)
        self.__Role16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssignLoc"):
                opp_val = getattr(old_value, "AssignLoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssignLoc"):
                opp_val = getattr(value, "AssignLoc", None)
                if opp_val is None:
                    setattr(value, "AssignLoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SessRole(self):
        return self.__SessRole

    @SessRole.setter
    def SessRole(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__SessRole", None)
        self.__SessRole = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Session11"):
                    opp_val = getattr(item, "Session11", None)
                    
                    if opp_val == self:
                        setattr(item, "Session11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Session11"):
                    opp_val = getattr(item, "Session11", None)
                    
                    setattr(item, "Session11", self)
                    

    @property
    def LocAssign(self):
        return self.__LocAssign

    @LocAssign.setter
    def LocAssign(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__LocAssign", None)
        self.__LocAssign = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Location9"):
                    opp_val = getattr(item, "Location9", None)
                    
                    if opp_val == self:
                        setattr(item, "Location9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Location9"):
                    opp_val = getattr(item, "Location9", None)
                    
                    setattr(item, "Location9", self)
                    

    @property
    def Role26(self):
        return self.__Role26

    @Role26.setter
    def Role26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Role__Role26", None)
        self.__Role26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RolePerm"):
                opp_val = getattr(old_value, "RolePerm", None)
                if opp_val == self:
                    setattr(old_value, "RolePerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RolePerm"):
                opp_val = getattr(value, "RolePerm", None)
                setattr(value, "RolePerm", self)

    def AddAssignLoc(self, LRBAC_l):
        # TODO: Implement AddAssignLoc method
        pass

    def UpdateRoleName(self, LRBAC_name):
        # TODO: Implement UpdateRoleName method
        pass

class LRBAC_Session:

    def __init__(self, MaxRoles: int, Session: "LRBAC_User" = None, RoleSess: set["LRBAC_Role"] = None, UserSess: "LRBAC_User" = None, Session11: "LRBAC_Role" = None):
        self.MaxRoles = MaxRoles
        self.Session = Session
        self.RoleSess = RoleSess if RoleSess is not None else set()
        self.UserSess = UserSess
        self.Session11 = Session11
        
        pass
    @property
    def MaxRoles(self):
        return self.__MaxRoles

    @MaxRoles.setter
    def MaxRoles(self, MaxRoles: int):
        self.__MaxRoles = MaxRoles


    @property
    def Session(self):
        return self.__Session

    @Session.setter
    def Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Session__Session", None)
        self.__Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SessUser"):
                opp_val = getattr(old_value, "SessUser", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SessUser"):
                opp_val = getattr(value, "SessUser", None)
                if opp_val is None:
                    setattr(value, "SessUser", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UserSess(self):
        return self.__UserSess

    @UserSess.setter
    def UserSess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Session__UserSess", None)
        self.__UserSess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User"):
                opp_val = getattr(old_value, "User", None)
                if opp_val == self:
                    setattr(old_value, "User", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User"):
                opp_val = getattr(value, "User", None)
                setattr(value, "User", self)

    @property
    def RoleSess(self):
        return self.__RoleSess

    @RoleSess.setter
    def RoleSess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Session__RoleSess", None)
        self.__RoleSess = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role4"):
                    opp_val = getattr(item, "Role4", None)
                    
                    if opp_val == self:
                        setattr(item, "Role4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role4"):
                    opp_val = getattr(item, "Role4", None)
                    
                    setattr(item, "Role4", self)
                    

    @property
    def Session11(self):
        return self.__Session11

    @Session11.setter
    def Session11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_LRBAC_Session__Session11", None)
        self.__Session11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SessRole"):
                opp_val = getattr(old_value, "SessRole", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SessRole"):
                opp_val = getattr(value, "SessRole", None)
                if opp_val is None:
                    setattr(value, "SessRole", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def UpdateMaxRoles(self, LRBAC_NoOfRoles):
        # TODO: Implement UpdateMaxRoles method
        pass

class LRBAC_EClass1:

    pass
class LRBAC_EClass0:

    pass
class Operation:

    pass
class LRBAC_Write(Operation):

    pass
class LRBAC_Execute(Operation):

    pass
class LRBAC_Read(Operation):

    pass
class User:

    pass
class LRBAC_Coder(User):

    pass
class LRBAC_Banker(User):

    pass
class LRBAC_Operation:

    pass