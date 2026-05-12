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

# Classes
LRBAC_Session = Class(name="LRBAC_Session")
LRBAC_Role = Class(name="LRBAC_Role")
LRBAC_User = Class(name="LRBAC_User")
LRBAC_Location = Class(name="LRBAC_Location")
LRBAC_Object = Class(name="LRBAC_Object")
LRBAC_Permission = Class(name="LRBAC_Permission")
LRBAC_Operation = Class(name="LRBAC_Operation")
LRBAC_Banker = Class(name="LRBAC_Banker")
User = Class(name="User")
LRBAC_Coder = Class(name="LRBAC_Coder")
LRBAC_Read = Class(name="LRBAC_Read")
Operation = Class(name="Operation")
LRBAC_EClass0 = Class(name="LRBAC_EClass0")
LRBAC_Write = Class(name="LRBAC_Write")
LRBAC_Execute = Class(name="LRBAC_Execute")
LRBAC_EClass1 = Class(name="LRBAC_EClass1")

# LRBAC_Session class attributes and methods
LRBAC_Session_MaxRoles: Property = Property(name="MaxRoles", type=IntegerType)
LRBAC_Session_m_UpdateMaxRoles: Method = Method(name="UpdateMaxRoles", parameters={Parameter(name='LRBAC_NoOfRoles', type=StringType)})
LRBAC_Session.attributes={LRBAC_Session_MaxRoles}
LRBAC_Session.methods={LRBAC_Session_m_UpdateMaxRoles}

# LRBAC_Role class attributes and methods
LRBAC_Role_RoleName: Property = Property(name="RoleName", type=StringType)
LRBAC_Role_m_UpdateRoleName: Method = Method(name="UpdateRoleName", parameters={Parameter(name='LRBAC_name', type=StringType)})
LRBAC_Role_m_AddAssignLoc: Method = Method(name="AddAssignLoc", parameters={Parameter(name='LRBAC_l', type=StringType)})
LRBAC_Role.attributes={LRBAC_Role_RoleName}
LRBAC_Role.methods={LRBAC_Role_m_AddAssignLoc, LRBAC_Role_m_UpdateRoleName}

# LRBAC_User class attributes and methods
LRBAC_User_Gender: Property = Property(name="Gender", type=StringType)
LRBAC_User_UserName: Property = Property(name="UserName", type=StringType)
LRBAC_User_UserID: Property = Property(name="UserID", type=IntegerType)
LRBAC_User_Age: Property = Property(name="Age", type=IntegerType)
LRBAC_User_m_UpdateAge: Method = Method(name="UpdateAge", parameters={Parameter(name='LRBAC_age', type=StringType)}, type=StringType)
LRBAC_User_m_UpdateLoc: Method = Method(name="UpdateLoc", parameters={Parameter(name='LRBAC_l', type=StringType)})
LRBAC_User_m_AssignRole: Method = Method(name="AssignRole", parameters={Parameter(name='LRBAC_r', type=StringType)})
LRBAC_User_m_UpdateUserID: Method = Method(name="UpdateUserID", parameters={Parameter(name='LRBAC_id', type=StringType)})
LRBAC_User_m_UpdateUserName: Method = Method(name="UpdateUserName", parameters={Parameter(name='LRBAC_name', type=StringType)}, type=StringType)
LRBAC_User.attributes={LRBAC_User_Age, LRBAC_User_Gender, LRBAC_User_UserID, LRBAC_User_UserName}
LRBAC_User.methods={LRBAC_User_m_UpdateLoc, LRBAC_User_m_AssignRole, LRBAC_User_m_UpdateUserName, LRBAC_User_m_UpdateAge, LRBAC_User_m_UpdateUserID}

# LRBAC_Location class attributes and methods
LRBAC_Location_LocName: Property = Property(name="LocName", type=StringType)
LRBAC_Location_m_UpdateLocName: Method = Method(name="UpdateLocName", parameters={Parameter(name='LRBAC_name', type=StringType)})
LRBAC_Location.attributes={LRBAC_Location_LocName}
LRBAC_Location.methods={LRBAC_Location_m_UpdateLocName}

# LRBAC_Object class attributes and methods
LRBAC_Object_ObjID: Property = Property(name="ObjID", type=IntegerType)
LRBAC_Object_m_UpdateObjID: Method = Method(name="UpdateObjID", parameters={Parameter(name='LRBAC_id', type=StringType)})
LRBAC_Object.attributes={LRBAC_Object_ObjID}
LRBAC_Object.methods={LRBAC_Object_m_UpdateObjID}

# LRBAC_Permission class attributes and methods
LRBAC_Permission_PermName: Property = Property(name="PermName", type=StringType)
LRBAC_Permission_m_UpdatePermName: Method = Method(name="UpdatePermName", parameters={Parameter(name='LRBAC_name', type=StringType)})
LRBAC_Permission.attributes={LRBAC_Permission_PermName}
LRBAC_Permission.methods={LRBAC_Permission_m_UpdatePermName}

# LRBAC_Operation class attributes and methods

# LRBAC_Banker class attributes and methods

# User class attributes and methods

# LRBAC_Coder class attributes and methods

# LRBAC_Read class attributes and methods

# Operation class attributes and methods

# LRBAC_EClass0 class attributes and methods

# LRBAC_Write class attributes and methods

# LRBAC_Execute class attributes and methods

# LRBAC_EClass1 class attributes and methods

# Relationships
UserSess0: BinaryAssociation = BinaryAssociation(
    name="UserSess0",
    ends={
        Property(name="Session", type=LRBAC_User, multiplicity=Multiplicity(1, 1)),
        Property(name="SessUser", type=LRBAC_Session, multiplicity=Multiplicity(0, 9999))
    }
)
AssignedRoles1: BinaryAssociation = BinaryAssociation(
    name="AssignedRoles1",
    ends={
        Property(name="Role", type=LRBAC_User, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignUser", type=LRBAC_Role, multiplicity=Multiplicity(0, 9999))
    }
)
SessRole3: BinaryAssociation = BinaryAssociation(
    name="SessRole3",
    ends={
        Property(name="Role4", type=LRBAC_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="RoleSess", type=LRBAC_Role, multiplicity=Multiplicity(0, 9999))
    }
)
SessUser5: BinaryAssociation = BinaryAssociation(
    name="SessUser5",
    ends={
        Property(name="User", type=LRBAC_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="UserSess", type=LRBAC_User, multiplicity=Multiplicity(1, 1))
    }
)
AssignUser6: BinaryAssociation = BinaryAssociation(
    name="AssignUser6",
    ends={
        Property(name="User7", type=LRBAC_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignedRoles", type=LRBAC_User, multiplicity=Multiplicity(0, 9999))
    }
)
UserLoc2: BinaryAssociation = BinaryAssociation(
    name="UserLoc2",
    ends={
        Property(name="Location", type=LRBAC_User, multiplicity=Multiplicity(1, 1)),
        Property(name="LocUser", type=LRBAC_Location, multiplicity=Multiplicity(1, 1))
    }
)
LocUser13: BinaryAssociation = BinaryAssociation(
    name="LocUser13",
    ends={
        Property(name="User14", type=LRBAC_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="UserLoc", type=LRBAC_User, multiplicity=Multiplicity(0, 9999))
    }
)
LocAssign15: BinaryAssociation = BinaryAssociation(
    name="LocAssign15",
    ends={
        Property(name="Role16", type=LRBAC_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="AssignLoc", type=LRBAC_Role, multiplicity=Multiplicity(0, 9999))
    }
)
LocObj17: BinaryAssociation = BinaryAssociation(
    name="LocObj17",
    ends={
        Property(name="Object", type=LRBAC_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjLoc", type=LRBAC_Object, multiplicity=Multiplicity(0, 9999))
    }
)
PermRoleLoc18: BinaryAssociation = BinaryAssociation(
    name="PermRoleLoc18",
    ends={
        Property(name="Permission19", type=LRBAC_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="RoleLocPerm", type=LRBAC_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
PermObjLoc20: BinaryAssociation = BinaryAssociation(
    name="PermObjLoc20",
    ends={
        Property(name="Permission21", type=LRBAC_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjLocPerm", type=LRBAC_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
AssignLoc8: BinaryAssociation = BinaryAssociation(
    name="AssignLoc8",
    ends={
        Property(name="Location9", type=LRBAC_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="LocAssign", type=LRBAC_Location, multiplicity=Multiplicity(0, 9999))
    }
)
RoleSess10: BinaryAssociation = BinaryAssociation(
    name="RoleSess10",
    ends={
        Property(name="Session11", type=LRBAC_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="SessRole", type=LRBAC_Session, multiplicity=Multiplicity(0, 9999))
    }
)
RolePerm12: BinaryAssociation = BinaryAssociation(
    name="RolePerm12",
    ends={
        Property(name="Permission", type=LRBAC_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="PermRole", type=LRBAC_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
RoleLocPerm27: BinaryAssociation = BinaryAssociation(
    name="RoleLocPerm27",
    ends={
        Property(name="Location28", type=LRBAC_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="PermRoleLoc", type=LRBAC_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjLocPerm29: BinaryAssociation = BinaryAssociation(
    name="ObjLocPerm29",
    ends={
        Property(name="Location30", type=LRBAC_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="PermObjLoc", type=LRBAC_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjLoc31: BinaryAssociation = BinaryAssociation(
    name="ObjLoc31",
    ends={
        Property(name="Location32", type=LRBAC_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="LocObj", type=LRBAC_Location, multiplicity=Multiplicity(1, 1))
    }
)
ObjPerm33: BinaryAssociation = BinaryAssociation(
    name="ObjPerm33",
    ends={
        Property(name="Permission34", type=LRBAC_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="PermObj", type=LRBAC_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
OperPerm35: BinaryAssociation = BinaryAssociation(
    name="OperPerm35",
    ends={
        Property(name="Permission36", type=LRBAC_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="PermOper", type=LRBAC_Permission, multiplicity=Multiplicity(0, 9999))
    }
)
PermOper22: BinaryAssociation = BinaryAssociation(
    name="PermOper22",
    ends={
        Property(name="Operation", type=LRBAC_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="OperPerm", type=LRBAC_Operation, multiplicity=Multiplicity(1, 1))
    }
)
PermObj23: BinaryAssociation = BinaryAssociation(
    name="PermObj23",
    ends={
        Property(name="Object24", type=LRBAC_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjPerm", type=LRBAC_Object, multiplicity=Multiplicity(1, 1))
    }
)
PermRole25: BinaryAssociation = BinaryAssociation(
    name="PermRole25",
    ends={
        Property(name="Role26", type=LRBAC_Permission, multiplicity=Multiplicity(1, 1)),
        Property(name="RolePerm", type=LRBAC_Role, multiplicity=Multiplicity(1, 1))
    }
)
EReference038: BinaryAssociation = BinaryAssociation(
    name="EReference038",
    ends={
        Property(name="LRBAC_EClass1", type=LRBAC_Read, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="LRBAC_Read39", type=LRBAC_EClass1, multiplicity=Multiplicity(1, 1))
    }
)
EReference037: BinaryAssociation = BinaryAssociation(
    name="EReference037",
    ends={
        Property(name="LRBAC_EClass0", type=LRBAC_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="LRBAC_Read", type=LRBAC_EClass0, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_LRBAC_Banker_User = Generalization(general=User, specific=LRBAC_Banker)
gen_LRBAC_Coder_User = Generalization(general=User, specific=LRBAC_Coder)
gen_LRBAC_Read_Operation = Generalization(general=Operation, specific=LRBAC_Read)
gen_LRBAC_Write_Operation = Generalization(general=Operation, specific=LRBAC_Write)
gen_LRBAC_Execute_Operation = Generalization(general=Operation, specific=LRBAC_Execute)

# Domain Model
domain_model = DomainModel(
    name="LRBAC",
    types={LRBAC_Session, LRBAC_Role, LRBAC_User, LRBAC_Location, LRBAC_Object, LRBAC_Permission, LRBAC_Operation, LRBAC_Banker, User, LRBAC_Coder, LRBAC_Read, Operation, LRBAC_EClass0, LRBAC_Write, LRBAC_Execute, LRBAC_EClass1},
    associations={UserSess0, AssignedRoles1, SessRole3, SessUser5, AssignUser6, UserLoc2, LocUser13, LocAssign15, LocObj17, PermRoleLoc18, PermObjLoc20, AssignLoc8, RoleSess10, RolePerm12, RoleLocPerm27, ObjLocPerm29, ObjLoc31, ObjPerm33, OperPerm35, PermOper22, PermObj23, PermRole25, EReference038, EReference037},
    generalizations={gen_LRBAC_Banker_User, gen_LRBAC_Coder_User, gen_LRBAC_Read_Operation, gen_LRBAC_Write_Operation, gen_LRBAC_Execute_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)