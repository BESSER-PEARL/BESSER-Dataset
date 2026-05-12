####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
Sex: Enumeration = Enumeration(
    name="Sex",
    literals={
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
Paper_User = Class(name="Paper_User")
Paper_Role = Class(name="Paper_Role")
Paper_Location = Class(name="Paper_Location")
Paper_Session = Class(name="Paper_Session")
Paper_Permission = Class(name="Paper_Permission")
Paper_Object = Class(name="Paper_Object")
Paper_Operation = Class(name="Paper_Operation")
Paper_Read = Class(name="Paper_Read")
Operation = Class(name="Operation")
Paper_Write = Class(name="Paper_Write")
Paper_Execute = Class(name="Paper_Execute")

# Paper_User class attributes and methods
Paper_User_Gender: Property = Property(name="Gender", type=StringType)
Paper_User_UserName: Property = Property(name="UserName", type=StringType)
Paper_User_UserID: Property = Property(name="UserID", type=IntegerType)
Paper_User_Age: Property = Property(name="Age", type=IntegerType)
Paper_User_m_UpdateUserName: Method = Method(name="UpdateUserName", parameters={Parameter(name='Paper_name', type=StringType)})
Paper_User_m_UpdateAge: Method = Method(name="UpdateAge", parameters={Parameter(name='Paper_age', type=StringType)})
Paper_User_m_UpdateLoc: Method = Method(name="UpdateLoc", parameters={Parameter(name='Paper_l', type=StringType)})
Paper_User_m_AssignRole: Method = Method(name="AssignRole", parameters={Parameter(name='Paper_r', type=StringType)})
Paper_User_m_UpdateUserID: Method = Method(name="UpdateUserID", parameters={Parameter(name='Paper_id', type=StringType)})
Paper_User_m_UpdateGender: Method = Method(name="UpdateGender", parameters={Parameter(name='Paper_gender', type=StringType)})
Paper_User.attributes={Paper_User_Age, Paper_User_UserID, Paper_User_UserName, Paper_User_Gender}
Paper_User.methods={Paper_User_m_UpdateAge, Paper_User_m_AssignRole, Paper_User_m_UpdateGender, Paper_User_m_UpdateUserID, Paper_User_m_UpdateUserName, Paper_User_m_UpdateLoc}

# Paper_Role class attributes and methods
Paper_Role_RoleName: Property = Property(name="RoleName", type=StringType)
Paper_Role_m_UpdateRoleName: Method = Method(name="UpdateRoleName", parameters={Parameter(name='Paper_name', type=StringType)})
Paper_Role_m_AddAssignLoc: Method = Method(name="AddAssignLoc", parameters={Parameter(name='Paper_l', type=StringType)})
Paper_Role.attributes={Paper_Role_RoleName}
Paper_Role.methods={Paper_Role_m_UpdateRoleName, Paper_Role_m_AddAssignLoc}

# Paper_Location class attributes and methods
Paper_Location_LocName: Property = Property(name="LocName", type=StringType)
Paper_Location_m_UpdateLocName: Method = Method(name="UpdateLocName", parameters={Parameter(name='Paper_name', type=StringType)})
Paper_Location.attributes={Paper_Location_LocName}
Paper_Location.methods={Paper_Location_m_UpdateLocName}

# Paper_Session class attributes and methods
Paper_Session_MaxRoles: Property = Property(name="MaxRoles", type=IntegerType)
Paper_Session_m_UpdateMaxRoles: Method = Method(name="UpdateMaxRoles", parameters={Parameter(name='Paper_NoOfRoles', type=StringType)})
Paper_Session.attributes={Paper_Session_MaxRoles}
Paper_Session.methods={Paper_Session_m_UpdateMaxRoles}

# Paper_Permission class attributes and methods
Paper_Permission_PermName: Property = Property(name="PermName", type=StringType)
Paper_Permission_m_UpdatePermName: Method = Method(name="UpdatePermName", parameters={Parameter(name='Paper_name', type=StringType)})
Paper_Permission.attributes={Paper_Permission_PermName}
Paper_Permission.methods={Paper_Permission_m_UpdatePermName}

# Paper_Object class attributes and methods
Paper_Object_ObjID: Property = Property(name="ObjID", type=IntegerType)
Paper_Object_m_UpdateObjID: Method = Method(name="UpdateObjID", parameters={Parameter(name='Paper_id', type=StringType)})
Paper_Object.attributes={Paper_Object_ObjID}
Paper_Object.methods={Paper_Object_m_UpdateObjID}

# Paper_Operation class attributes and methods

# Paper_Read class attributes and methods

# Operation class attributes and methods

# Paper_Write class attributes and methods

# Paper_Execute class attributes and methods

# Relationships
UserSess0: BinaryAssociation = BinaryAssociation(
    name="UserSess0",
    ends={
        Property(name="Session", type=Paper_User, multiplicity=Multiplicity(1, 1)),
        Property(name="SessUser", type=Paper_Session, multiplicity=Multiplicity(0, 9999))
    }
)
AssignedRoles1: BinaryAssociation = BinaryAssociation(
    name="AssignedRoles1",
    ends={
        Property(name="Role", type=Paper_User, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignUser", type=Paper_Role, multiplicity=Multiplicity(0, 9999))
    }
)
UserLoc2: BinaryAssociation = BinaryAssociation(
    name="UserLoc2",
    ends={
        Property(name="Location", type=Paper_User, multiplicity=Multiplicity(1, 1)),
        Property(name="LocUser", type=Paper_Location, multiplicity=Multiplicity(1, 1))
    }
)
SessRole3: BinaryAssociation = BinaryAssociation(
    name="SessRole3",
    ends={
        Property(name="Role4", type=Paper_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="RoleSess", type=Paper_Role, multiplicity=Multiplicity(0, 9999))
    }
)
SessUser5: BinaryAssociation = BinaryAssociation(
    name="SessUser5",
    ends={
        Property(name="User", type=Paper_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="UserSess", type=Paper_User, multiplicity=Multiplicity(1, 1))
    }
)
PermObjLoc20: BinaryAssociation = BinaryAssociation(
    name="PermObjLoc20",
    ends={
        Property(name="Permission21", type=Paper_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjLocPerm", type=Paper_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
AssignUser6: BinaryAssociation = BinaryAssociation(
    name="AssignUser6",
    ends={
        Property(name="User7", type=Paper_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignedRoles", type=Paper_User, multiplicity=Multiplicity(0, 9999))
    }
)
AssignLoc8: BinaryAssociation = BinaryAssociation(
    name="AssignLoc8",
    ends={
        Property(name="Location9", type=Paper_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="LocAssign", type=Paper_Location, multiplicity=Multiplicity(0, 9999))
    }
)
RoleSess10: BinaryAssociation = BinaryAssociation(
    name="RoleSess10",
    ends={
        Property(name="Session11", type=Paper_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="SessRole", type=Paper_Session, multiplicity=Multiplicity(0, 9999))
    }
)
RolePerm12: BinaryAssociation = BinaryAssociation(
    name="RolePerm12",
    ends={
        Property(name="Permission", type=Paper_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="PermRole", type=Paper_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
LocUser13: BinaryAssociation = BinaryAssociation(
    name="LocUser13",
    ends={
        Property(name="User14", type=Paper_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="UserLoc", type=Paper_User, multiplicity=Multiplicity(0, 9999))
    }
)
LocAssign15: BinaryAssociation = BinaryAssociation(
    name="LocAssign15",
    ends={
        Property(name="Role16", type=Paper_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignLoc", type=Paper_Role, multiplicity=Multiplicity(0, 9999))
    }
)
LocObj17: BinaryAssociation = BinaryAssociation(
    name="LocObj17",
    ends={
        Property(name="Object", type=Paper_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjLoc", type=Paper_Object, multiplicity=Multiplicity(0, 9999))
    }
)
PermRoleLoc18: BinaryAssociation = BinaryAssociation(
    name="PermRoleLoc18",
    ends={
        Property(name="Permission19", type=Paper_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="RoleLocPerm", type=Paper_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
PermOper22: BinaryAssociation = BinaryAssociation(
    name="PermOper22",
    ends={
        Property(name="Operation", type=Paper_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="OperPerm", type=Paper_Operation, multiplicity=Multiplicity(1, 1))
    }
)
PermObj23: BinaryAssociation = BinaryAssociation(
    name="PermObj23",
    ends={
        Property(name="Object24", type=Paper_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjPerm", type=Paper_Object, multiplicity=Multiplicity(1, 1))
    }
)
PermRole25: BinaryAssociation = BinaryAssociation(
    name="PermRole25",
    ends={
        Property(name="Role26", type=Paper_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="RolePerm", type=Paper_Role, multiplicity=Multiplicity(1, 1))
    }
)
RoleLocPerm27: BinaryAssociation = BinaryAssociation(
    name="RoleLocPerm27",
    ends={
        Property(name="Location28", type=Paper_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="PermRoleLoc", type=Paper_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjLocPerm29: BinaryAssociation = BinaryAssociation(
    name="ObjLocPerm29",
    ends={
        Property(name="Location30", type=Paper_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="PermObjLoc", type=Paper_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjLoc31: BinaryAssociation = BinaryAssociation(
    name="ObjLoc31",
    ends={
        Property(name="Location32", type=Paper_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="LocObj", type=Paper_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjPerm33: BinaryAssociation = BinaryAssociation(
    name="ObjPerm33",
    ends={
        Property(name="Permission34", type=Paper_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="PermObj", type=Paper_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
OperPerm35: BinaryAssociation = BinaryAssociation(
    name="OperPerm35",
    ends={
        Property(name="Permission36", type=Paper_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="PermOper", type=Paper_Permission, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Paper_Read_Operation = Generalization(general=Operation, specific=Paper_Read)
gen_Paper_Write_Operation = Generalization(general=Operation, specific=Paper_Write)
gen_Paper_Execute_Operation = Generalization(general=Operation, specific=Paper_Execute)

# Domain Model
domain_model = DomainModel(
    name="Paper",
    types={Paper_User, Paper_Role, Paper_Location, Paper_Session, Paper_Permission, Paper_Object, Paper_Operation, Paper_Read, Operation, Paper_Write, Paper_Execute, Sex},
    associations={UserSess0, AssignedRoles1, UserLoc2, SessRole3, SessUser5, PermObjLoc20, AssignUser6, AssignLoc8, RoleSess10, RolePerm12, LocUser13, LocAssign15, LocObj17, PermRoleLoc18, PermOper22, PermObj23, PermRole25, RoleLocPerm27, ObjLocPerm29, ObjLoc31, ObjPerm33, OperPerm35},
    generalizations={gen_Paper_Read_Operation, gen_Paper_Write_Operation, gen_Paper_Execute_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)