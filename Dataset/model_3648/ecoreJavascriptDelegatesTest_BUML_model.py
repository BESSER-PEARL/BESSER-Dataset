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
CompanySizeKind: Enumeration = Enumeration(
    name="CompanySizeKind",
    literals={
            EnumerationLiteral(name="small"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="large")
    }
)

# Classes
ecoreJavascriptDelegatesTest_Company = Class(name="ecoreJavascriptDelegatesTest::Company")
ecoreJavascriptDelegatesTest_Employee = Class(name="ecoreJavascriptDelegatesTest::Employee")

# ecoreJavascriptDelegatesTest_Company class attributes and methods
ecoreJavascriptDelegatesTest_Company_name: Property = Property(name="name", type=StringType)
ecoreJavascriptDelegatesTest_Company_size: Property = Property(name="size", type=StringType)
ecoreJavascriptDelegatesTest_Company.attributes={ecoreJavascriptDelegatesTest_Company_name, ecoreJavascriptDelegatesTest_Company_size}

# ecoreJavascriptDelegatesTest_Employee class attributes and methods
ecoreJavascriptDelegatesTest_Employee_name: Property = Property(name="name", type=StringType)
ecoreJavascriptDelegatesTest_Employee_m_reportsTo: Method = Method(name="reportsTo", parameters={Parameter(name='manager')}, type=BooleanType)
ecoreJavascriptDelegatesTest_Employee_m_checkNameLength: Method = Method(name="checkNameLength", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
ecoreJavascriptDelegatesTest_Employee.attributes={ecoreJavascriptDelegatesTest_Employee_name}
ecoreJavascriptDelegatesTest_Employee.methods={ecoreJavascriptDelegatesTest_Employee_m_checkNameLength, ecoreJavascriptDelegatesTest_Employee_m_reportsTo}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="Employee", type=ecoreJavascriptDelegatesTest_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager2: BinaryAssociation = BinaryAssociation(
    name="manager2",
    ends={
        Property(name="ecoreJavascriptDelegatesTest_Employee", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreJavascriptDelegatesTest_Employee1", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(0, 1))
    }
)
company3: BinaryAssociation = BinaryAssociation(
    name="company3",
    ends={
        Property(name="Company", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=ecoreJavascriptDelegatesTest_Company, multiplicity=Multiplicity(1, 1))
    }
)
directReports5: BinaryAssociation = BinaryAssociation(
    name="directReports5",
    ends={
        Property(name="ecoreJavascriptDelegatesTest_Employee6", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreJavascriptDelegatesTest_Employee4", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
allReports8: BinaryAssociation = BinaryAssociation(
    name="allReports8",
    ends={
        Property(name="ecoreJavascriptDelegatesTest_Employee9", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreJavascriptDelegatesTest_Employee7", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
reportingChain11: BinaryAssociation = BinaryAssociation(
    name="reportingChain11",
    ends={
        Property(name="ecoreJavascriptDelegatesTest_Employee12", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="ecoreJavascriptDelegatesTest_Employee10", type=ecoreJavascriptDelegatesTest_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ecoreJavascriptDelegatesTest",
    types={ecoreJavascriptDelegatesTest_Company, ecoreJavascriptDelegatesTest_Employee, CompanySizeKind},
    associations={employees0, manager2, company3, directReports5, allReports8, reportingChain11},
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