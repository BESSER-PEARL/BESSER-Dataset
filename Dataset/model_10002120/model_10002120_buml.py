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
User = Class(name="User")
Login = Class(name="Login")
System = Class(name="System")
Light = Class(name="Light")
Fan = Class(name="Fan")
Security_System = Class(name="Security_System")
Fire_Alarm = Class(name="Fire_Alarm")
TV = Class(name="TV")

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User.attributes={User_Name}

# Login class attributes and methods
Login_Name: Property = Property(name="Name", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Password, Login_Name}

# System class attributes and methods
System_status: Property = Property(name="status", type=BooleanType)
System.attributes={System_status}

# Light class attributes and methods

# Fan class attributes and methods

# Security_System class attributes and methods
Security_System_systemOn: Property = Property(name="systemOn", type=BooleanType)
Security_System_systemOff: Property = Property(name="systemOff", type=BooleanType)
Security_System.attributes={Security_System_systemOff, Security_System_systemOn}

# Fire_Alarm class attributes and methods
Fire_Alarm_systemOn: Property = Property(name="systemOn", type=BooleanType)
Fire_Alarm_systemOff: Property = Property(name="systemOff", type=BooleanType)
Fire_Alarm.attributes={Fire_Alarm_systemOff, Fire_Alarm_systemOn}

# TV class attributes and methods

# Relationships
Login_System: BinaryAssociation = BinaryAssociation(
    name="Login_System",
    ends={
        Property(name="_handle0", type=System, multiplicity=Multiplicity(1, 1)),
        Property(name="_user1", type=Login, multiplicity=Multiplicity(1, 1))
    }
)
Login_User: BinaryAssociation = BinaryAssociation(
    name="Login_User",
    ends={
        Property(name="_user2", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="_access3", type=Login, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_pl114NaaEeehRMl7r1_c5g",
    types={User, Login, System, Light, Fan, Security_System, Fire_Alarm, TV},
    associations={Login_System, Login_User},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)