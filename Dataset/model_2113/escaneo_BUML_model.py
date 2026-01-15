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
ESeverity: Enumeration = Enumeration(
    name="ESeverity",
    literals={
            EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Low"),
			EnumerationLiteral(name="High")
    }
)

EAttackMethod: Enumeration = Enumeration(
    name="EAttackMethod",
    literals={
            EnumerationLiteral(name="SQLInjection"),
			EnumerationLiteral(name="XSS"),
			EnumerationLiteral(name="Authentication"),
			EnumerationLiteral(name="Authorization"),
			EnumerationLiteral(name="PrivilegeScalation")
    }
)

# Classes
securityTest_Note = Class(name="securityTest::Note")
securityTest_Test = Class(name="securityTest::Test")
securityTest_TargetOfEvaluation = Class(name="securityTest::TargetOfEvaluation")
securityTest_Attack = Class(name="securityTest::Attack")
securityTest_Input = Class(name="securityTest::Input")
securityTest_AuthSetting = Class(name="securityTest::AuthSetting")
securityTest_WebComponent = Class(name="securityTest::WebComponent")

# securityTest_Note class attributes and methods
securityTest_Note_noteText: Property = Property(name="noteText", type=StringType)
securityTest_Note.attributes={securityTest_Note_noteText}

# securityTest_Test class attributes and methods
securityTest_Test_date: Property = Property(name="date", type=DateType)
securityTest_Test_name: Property = Property(name="name", type=StringType)
securityTest_Test_severity: Property = Property(name="severity", type=StringType)
securityTest_Test_id: Property = Property(name="id", type=StringType)
securityTest_Test.attributes={securityTest_Test_severity, securityTest_Test_id, securityTest_Test_date, securityTest_Test_name}

# securityTest_TargetOfEvaluation class attributes and methods
securityTest_TargetOfEvaluation_domain: Property = Property(name="domain", type=StringType)
securityTest_TargetOfEvaluation_ip: Property = Property(name="ip", type=StringType)
securityTest_TargetOfEvaluation_protocol: Property = Property(name="protocol", type=StringType)
securityTest_TargetOfEvaluation_port: Property = Property(name="port", type=StringType)
securityTest_TargetOfEvaluation.attributes={securityTest_TargetOfEvaluation_protocol, securityTest_TargetOfEvaluation_port, securityTest_TargetOfEvaluation_domain, securityTest_TargetOfEvaluation_ip}

# securityTest_Attack class attributes and methods
securityTest_Attack_name: Property = Property(name="name", type=StringType)
securityTest_Attack_severity: Property = Property(name="severity", type=StringType)
securityTest_Attack.attributes={securityTest_Attack_name, securityTest_Attack_severity}

# securityTest_Input class attributes and methods
securityTest_Input_name: Property = Property(name="name", type=StringType)
securityTest_Input.attributes={securityTest_Input_name}

# securityTest_AuthSetting class attributes and methods
securityTest_AuthSetting_roles: Property = Property(name="roles", type=StringType)
securityTest_AuthSetting_usernameParam: Property = Property(name="usernameParam", type=StringType)
securityTest_AuthSetting_passwordParam: Property = Property(name="passwordParam", type=StringType)
securityTest_AuthSetting_loginTargetURL: Property = Property(name="loginTargetURL", type=StringType)
securityTest_AuthSetting_loginMessagePattern: Property = Property(name="loginMessagePattern", type=StringType)
securityTest_AuthSetting_logoutMessagePattern: Property = Property(name="logoutMessagePattern", type=StringType)
securityTest_AuthSetting.attributes={securityTest_AuthSetting_loginTargetURL, securityTest_AuthSetting_passwordParam, securityTest_AuthSetting_loginMessagePattern, securityTest_AuthSetting_logoutMessagePattern, securityTest_AuthSetting_roles, securityTest_AuthSetting_usernameParam}

# securityTest_WebComponent class attributes and methods
securityTest_WebComponent_path: Property = Property(name="path", type=StringType)
securityTest_WebComponent.attributes={securityTest_WebComponent_path}

# Relationships
note3: BinaryAssociation = BinaryAssociation(
    name="note3",
    ends={
        Property(name="securityTest_Note", type=securityTest_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_Test4", type=securityTest_Note, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope0: BinaryAssociation = BinaryAssociation(
    name="scope0",
    ends={
        Property(name="securityTest_TargetOfEvaluation", type=securityTest_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_Test", type=securityTest_TargetOfEvaluation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
possibleAttacks1: BinaryAssociation = BinaryAssociation(
    name="possibleAttacks1",
    ends={
        Property(name="securityTest_Attack", type=securityTest_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_Test2", type=securityTest_Attack, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
targetLinks10: BinaryAssociation = BinaryAssociation(
    name="targetLinks10",
    ends={
        Property(name="securityTest_WebComponent11", type=securityTest_WebComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_WebComponent9", type=securityTest_WebComponent, multiplicity=Multiplicity(0, 9999))
    }
)
inputs12: BinaryAssociation = BinaryAssociation(
    name="inputs12",
    ends={
        Property(name="securityTest_Input", type=securityTest_WebComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_WebComponent13", type=securityTest_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authSetting5: BinaryAssociation = BinaryAssociation(
    name="authSetting5",
    ends={
        Property(name="securityTest_AuthSetting", type=securityTest_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_Test6", type=securityTest_AuthSetting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components7: BinaryAssociation = BinaryAssociation(
    name="components7",
    ends={
        Property(name="securityTest_WebComponent", type=securityTest_TargetOfEvaluation, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_TargetOfEvaluation8", type=securityTest_WebComponent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attacks14: BinaryAssociation = BinaryAssociation(
    name="attacks14",
    ends={
        Property(name="securityTest_Attack16", type=securityTest_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="securityTest_Input15", type=securityTest_Attack, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="securityTest",
    types={securityTest_Note, securityTest_Test, securityTest_TargetOfEvaluation, securityTest_Attack, securityTest_Input, securityTest_AuthSetting, securityTest_WebComponent, ESeverity, EAttackMethod},
    associations={note3, scope0, possibleAttacks1, targetLinks10, inputs12, authSetting5, components7, attacks14},
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