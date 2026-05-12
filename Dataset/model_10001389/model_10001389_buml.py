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
Course = Class(name="Course")
ServiceCourse = Class(name="ServiceCourse")
asdfa = Class(name="asdfa")
MyClass = Class(name="MyClass")
c = Class(name="c")
c1 = Class(name="c1")
Course2 = Class(name="Course2")
ServiceCourse2 = Class(name="ServiceCourse2")
asdfa2 = Class(name="asdfa2")
MyClass2 = Class(name="MyClass2")
c2 = Class(name="c2")
c21 = Class(name="c21")
Course3 = Class(name="Course3")
ServiceCourse3 = Class(name="ServiceCourse3")
asdfa3 = Class(name="asdfa3")
MyClass3 = Class(name="MyClass3")
c3 = Class(name="c3")
c31 = Class(name="c31")

# Course class attributes and methods
Course_Id: Property = Property(name="Id", type=IntegerType)
Course_Name: Property = Property(name="Name", type=StringType)
Course_StartDate: Property = Property(name="StartDate", type=StringType)
Course.attributes={Course_Name, Course_StartDate, Course_Id}

# ServiceCourse class attributes and methods
ServiceCourse_attribute: Property = Property(name="attribute", type=StringType)
ServiceCourse_attribute2: Property = Property(name="attribute2", type=StringType)
ServiceCourse_attribute3: Property = Property(name="attribute3", type=StringType)
ServiceCourse_attribute4: Property = Property(name="attribute4", type=StringType)
ServiceCourse_attribute5: Property = Property(name="attribute5", type=StringType)
ServiceCourse_attribute6: Property = Property(name="attribute6", type=StringType)
ServiceCourse_attribute7: Property = Property(name="attribute7", type=StringType)
ServiceCourse_attribute8: Property = Property(name="attribute8", type=StringType)
ServiceCourse.attributes={ServiceCourse_attribute, ServiceCourse_attribute7, ServiceCourse_attribute8, ServiceCourse_attribute4, ServiceCourse_attribute5, ServiceCourse_attribute2, ServiceCourse_attribute3, ServiceCourse_attribute6}

# asdfa class attributes and methods

# MyClass class attributes and methods

# c class attributes and methods

# c1 class attributes and methods

# Course2 class attributes and methods
Course2_StartDate: Property = Property(name="StartDate", type=StringType)
Course2_Id: Property = Property(name="Id", type=IntegerType)
Course2_Name: Property = Property(name="Name", type=StringType)
Course2.attributes={Course2_StartDate, Course2_Id, Course2_Name}

# ServiceCourse2 class attributes and methods
ServiceCourse2_attribute: Property = Property(name="attribute", type=StringType)
ServiceCourse2_attribute2: Property = Property(name="attribute2", type=StringType)
ServiceCourse2_attribute3: Property = Property(name="attribute3", type=StringType)
ServiceCourse2_attribute4: Property = Property(name="attribute4", type=StringType)
ServiceCourse2_attribute5: Property = Property(name="attribute5", type=StringType)
ServiceCourse2_attribute6: Property = Property(name="attribute6", type=StringType)
ServiceCourse2_attribute7: Property = Property(name="attribute7", type=StringType)
ServiceCourse2_attribute8: Property = Property(name="attribute8", type=StringType)
ServiceCourse2.attributes={ServiceCourse2_attribute5, ServiceCourse2_attribute7, ServiceCourse2_attribute, ServiceCourse2_attribute6, ServiceCourse2_attribute3, ServiceCourse2_attribute8, ServiceCourse2_attribute2, ServiceCourse2_attribute4}

# asdfa2 class attributes and methods

# MyClass2 class attributes and methods

# c2 class attributes and methods

# c21 class attributes and methods

# Course3 class attributes and methods
Course3_Id: Property = Property(name="Id", type=IntegerType)
Course3_Name: Property = Property(name="Name", type=StringType)
Course3_StartDate: Property = Property(name="StartDate", type=StringType)
Course3.attributes={Course3_Id, Course3_Name, Course3_StartDate}

# ServiceCourse3 class attributes and methods
ServiceCourse3_attribute: Property = Property(name="attribute", type=StringType)
ServiceCourse3_attribute2: Property = Property(name="attribute2", type=StringType)
ServiceCourse3_attribute3: Property = Property(name="attribute3", type=StringType)
ServiceCourse3_attribute4: Property = Property(name="attribute4", type=StringType)
ServiceCourse3_attribute5: Property = Property(name="attribute5", type=StringType)
ServiceCourse3_attribute6: Property = Property(name="attribute6", type=StringType)
ServiceCourse3_attribute7: Property = Property(name="attribute7", type=StringType)
ServiceCourse3_attribute8: Property = Property(name="attribute8", type=StringType)
ServiceCourse3.attributes={ServiceCourse3_attribute5, ServiceCourse3_attribute2, ServiceCourse3_attribute3, ServiceCourse3_attribute4, ServiceCourse3_attribute6, ServiceCourse3_attribute, ServiceCourse3_attribute8, ServiceCourse3_attribute7}

# asdfa3 class attributes and methods

# MyClass3 class attributes and methods

# c3 class attributes and methods

# c31 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_4_G0wLyNEeedTfUoC_GfaA",
    types={Course, ServiceCourse, asdfa, MyClass, c, c1, Course2, ServiceCourse2, asdfa2, MyClass2, c2, c21, Course3, ServiceCourse3, asdfa3, MyClass3, c3, c31},
    associations={},
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