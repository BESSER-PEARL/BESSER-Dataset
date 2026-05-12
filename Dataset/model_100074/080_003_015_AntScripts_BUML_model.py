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
AntScripts_NamedElement = Class(name="AntScripts_NamedElement", is_abstract=True)
AntScripts_DescribableElement = Class(name="AntScripts_DescribableElement", is_abstract=True)
AntScripts_Target = Class(name="AntScripts_Target")
Task = Class(name="Task")
AntScripts_CommentableElement = Class(name="AntScripts_CommentableElement", is_abstract=True)
AntScripts_Project = Class(name="AntScripts_Project")
NamedElement = Class(name="NamedElement")
DescribableElement = Class(name="DescribableElement")
CommentableElement = Class(name="CommentableElement")
Property_ = Class(name="Property")
Target = Class(name="Target")
AntScripts_Property = Class(name="AntScripts_Property")
AntScripts_TaskElement = Class(name="AntScripts_TaskElement", is_abstract=True)
Attribute = Class(name="Attribute")
TaskElement = Class(name="TaskElement")
AntScripts_Attribute = Class(name="AntScripts_Attribute")
AntScripts_Task = Class(name="AntScripts_Task")
AntScripts_TaskParameter = Class(name="AntScripts_TaskParameter")

# AntScripts_NamedElement class attributes and methods
AntScripts_NamedElement_name: Property = Property(name="name", type=StringType)
AntScripts_NamedElement.attributes={AntScripts_NamedElement_name}

# AntScripts_DescribableElement class attributes and methods
AntScripts_DescribableElement_description: Property = Property(name="description", type=StringType)
AntScripts_DescribableElement.attributes={AntScripts_DescribableElement_description}

# AntScripts_Target class attributes and methods
AntScripts_Target_if_: Property = Property(name="if_", type=StringType)
AntScripts_Target_unless: Property = Property(name="unless", type=StringType)
AntScripts_Target.attributes={AntScripts_Target_unless, AntScripts_Target_if_}

# Task class attributes and methods

# AntScripts_CommentableElement class attributes and methods
AntScripts_CommentableElement_comment: Property = Property(name="comment", type=StringType)
AntScripts_CommentableElement.attributes={AntScripts_CommentableElement_comment}

# AntScripts_Project class attributes and methods

# NamedElement class attributes and methods

# DescribableElement class attributes and methods

# CommentableElement class attributes and methods

# Property class attributes and methods

# Target class attributes and methods

# AntScripts_Property class attributes and methods
AntScripts_Property_name: Property = Property(name="name", type=StringType)
AntScripts_Property_value: Property = Property(name="value", type=StringType)
AntScripts_Property_location: Property = Property(name="location", type=StringType)
AntScripts_Property_refid: Property = Property(name="refid", type=StringType)
AntScripts_Property_resource: Property = Property(name="resource", type=StringType)
AntScripts_Property_file: Property = Property(name="file", type=StringType)
AntScripts_Property_url: Property = Property(name="url", type=StringType)
AntScripts_Property_environment: Property = Property(name="environment", type=StringType)
AntScripts_Property_classpath: Property = Property(name="classpath", type=StringType)
AntScripts_Property_classpathref: Property = Property(name="classpathref", type=StringType)
AntScripts_Property_prefix: Property = Property(name="prefix", type=StringType)
AntScripts_Property.attributes={AntScripts_Property_file, AntScripts_Property_location, AntScripts_Property_url, AntScripts_Property_classpath, AntScripts_Property_resource, AntScripts_Property_name, AntScripts_Property_prefix, AntScripts_Property_classpathref, AntScripts_Property_value, AntScripts_Property_environment, AntScripts_Property_refid}

# AntScripts_TaskElement class attributes and methods

# Attribute class attributes and methods

# TaskElement class attributes and methods

# AntScripts_Attribute class attributes and methods
AntScripts_Attribute_value: Property = Property(name="value", type=StringType)
AntScripts_Attribute.attributes={AntScripts_Attribute_value}

# AntScripts_Task class attributes and methods

# AntScripts_TaskParameter class attributes and methods

# Relationships
tasks6: BinaryAssociation = BinaryAssociation(
    name="tasks6",
    ends={
        Property(name="Task", type=AntScripts_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_Target", type=Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="Property", type=AntScripts_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_Project", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targets1: BinaryAssociation = BinaryAssociation(
    name="targets1",
    ends={
        Property(name="Target", type=AntScripts_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_Project2", type=Target, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultTarget3: BinaryAssociation = BinaryAssociation(
    name="defaultTarget3",
    ends={
        Property(name="Target5", type=AntScripts_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_Project4", type=Target, multiplicity=Multiplicity(0, 1))
    }
)
depends7: BinaryAssociation = BinaryAssociation(
    name="depends7",
    ends={
        Property(name="Target9", type=AntScripts_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_Target8", type=Target, multiplicity=Multiplicity(0, 9999))
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="Attribute", type=AntScripts_TaskElement, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_TaskElement", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements11: BinaryAssociation = BinaryAssociation(
    name="elements11",
    ends={
        Property(name="TaskElement", type=AntScripts_TaskElement, multiplicity=Multiplicity(1, 1)),
        Property(name="AntScripts_TaskElement12", type=TaskElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_AntScripts_Target_NamedElement = Generalization(general=NamedElement, specific=AntScripts_Target)
gen_AntScripts_Target_DescribableElement = Generalization(general=DescribableElement, specific=AntScripts_Target)
gen_AntScripts_Target_CommentableElement = Generalization(general=CommentableElement, specific=AntScripts_Target)
gen_AntScripts_Project_NamedElement = Generalization(general=NamedElement, specific=AntScripts_Project)
gen_AntScripts_Project_DescribableElement = Generalization(general=DescribableElement, specific=AntScripts_Project)
gen_AntScripts_Project_CommentableElement = Generalization(general=CommentableElement, specific=AntScripts_Project)
gen_AntScripts_TaskElement_NamedElement = Generalization(general=NamedElement, specific=AntScripts_TaskElement)
gen_AntScripts_TaskElement_CommentableElement = Generalization(general=CommentableElement, specific=AntScripts_TaskElement)
gen_AntScripts_Attribute_NamedElement = Generalization(general=NamedElement, specific=AntScripts_Attribute)
gen_AntScripts_Task_TaskElement = Generalization(general=TaskElement, specific=AntScripts_Task)
gen_AntScripts_TaskParameter_TaskElement = Generalization(general=TaskElement, specific=AntScripts_TaskParameter)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={AntScripts_NamedElement, AntScripts_DescribableElement, AntScripts_Target, Task, AntScripts_CommentableElement, AntScripts_Project, NamedElement, DescribableElement, CommentableElement, Property_, Target, AntScripts_Property, AntScripts_TaskElement, Attribute, TaskElement, AntScripts_Attribute, AntScripts_Task, AntScripts_TaskParameter},
    associations={tasks6, properties0, targets1, defaultTarget3, depends7, attributes10, elements11},
    generalizations={gen_AntScripts_Target_NamedElement, gen_AntScripts_Target_DescribableElement, gen_AntScripts_Target_CommentableElement, gen_AntScripts_Project_NamedElement, gen_AntScripts_Project_DescribableElement, gen_AntScripts_Project_CommentableElement, gen_AntScripts_TaskElement_NamedElement, gen_AntScripts_TaskElement_CommentableElement, gen_AntScripts_Attribute_NamedElement, gen_AntScripts_Task_TaskElement, gen_AntScripts_TaskParameter_TaskElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)