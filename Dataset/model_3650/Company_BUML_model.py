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
company_Company = Class(name="company::Company")
company_Employee = Class(name="company::Employee")

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company_size: Property = Property(name="size", type=StringType)
company_Company_m_dummyInvariant: Method = Method(name="dummyInvariant", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
company_Company.attributes={company_Company_name, company_Company_size}
company_Company.methods={company_Company_m_dummyInvariant}

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee_hasNameAsAttribute: Property = Property(name="hasNameAsAttribute", type=BooleanType)
company_Employee_m_reportsTo: Method = Method(name="reportsTo", parameters={Parameter(name='manager')}, type=BooleanType)
company_Employee_m_noManagerImpliesDirectReports: Method = Method(name="noManagerImpliesDirectReports", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
company_Employee_m_hasNameAsOperation: Method = Method(name="hasNameAsOperation", parameters={}, type=BooleanType)
company_Employee.attributes={company_Employee_hasNameAsAttribute, company_Employee_name}
company_Employee.methods={company_Employee_m_reportsTo, company_Employee_m_hasNameAsOperation, company_Employee_m_noManagerImpliesDirectReports}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="Employee", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allReports8: BinaryAssociation = BinaryAssociation(
    name="allReports8",
    ends={
        Property(name="company_Employee9", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee7", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
manager2: BinaryAssociation = BinaryAssociation(
    name="manager2",
    ends={
        Property(name="company_Employee", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee1", type=company_Employee, multiplicity=Multiplicity(0, 1))
    }
)
company3: BinaryAssociation = BinaryAssociation(
    name="company3",
    ends={
        Property(name="Company", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=company_Company, multiplicity=Multiplicity(1, 1))
    }
)
directReports5: BinaryAssociation = BinaryAssociation(
    name="directReports5",
    ends={
        Property(name="company_Employee6", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee4", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
reportingChain11: BinaryAssociation = BinaryAssociation(
    name="reportingChain11",
    ends={
        Property(name="company_Employee12", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee10", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Company, company_Employee, CompanySizeKind},
    associations={employees0, allReports8, manager2, company3, directReports5, reportingChain11},
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