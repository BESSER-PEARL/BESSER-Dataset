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
beans_BeanLibrary = Class(name="beans_BeanLibrary")
NamedElement = Class(name="NamedElement")
beans_Bean = Class(name="beans_Bean")
beans_BeanProperty = Class(name="beans_BeanProperty")
beans_NamedElement = Class(name="beans_NamedElement", is_abstract=True)

# beans_BeanLibrary class attributes and methods
beans_BeanLibrary_packageName: Property = Property(name="packageName", type=StringType)
beans_BeanLibrary.attributes={beans_BeanLibrary_packageName}

# NamedElement class attributes and methods

# beans_Bean class attributes and methods

# beans_BeanProperty class attributes and methods
beans_BeanProperty_typeName: Property = Property(name="typeName", type=StringType)
beans_BeanProperty_changeable: Property = Property(name="changeable", type=BooleanType)
beans_BeanProperty.attributes={beans_BeanProperty_typeName, beans_BeanProperty_changeable}

# beans_NamedElement class attributes and methods
beans_NamedElement_name: Property = Property(name="name", type=StringType)
beans_NamedElement.attributes={beans_NamedElement_name}

# Relationships
beans0: BinaryAssociation = BinaryAssociation(
    name="beans0",
    ends={
        Property(name="Bean", type=beans_BeanLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="beanLibrary", type=beans_Bean, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
beanLibrary1: BinaryAssociation = BinaryAssociation(
    name="beanLibrary1",
    ends={
        Property(name="BeanLibrary", type=beans_Bean, multiplicity=Multiplicity(1, 1)),
        Property(name="beans", type=beans_BeanLibrary, multiplicity=Multiplicity(1, 1))
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="BeanProperty", type=beans_Bean, multiplicity=Multiplicity(1, 1)),
        Property(name="bean", type=beans_BeanProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bean3: BinaryAssociation = BinaryAssociation(
    name="bean3",
    ends={
        Property(name="Bean4", type=beans_BeanProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="properties", type=beans_Bean, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_beans_BeanLibrary_NamedElement = Generalization(general=NamedElement, specific=beans_BeanLibrary)
gen_beans_Bean_NamedElement = Generalization(general=NamedElement, specific=beans_Bean)
gen_beans_BeanProperty_NamedElement = Generalization(general=NamedElement, specific=beans_BeanProperty)

# Domain Model
domain_model = DomainModel(
    name="beans",
    types={beans_BeanLibrary, NamedElement, beans_Bean, beans_BeanProperty, beans_NamedElement},
    associations={beans0, beanLibrary1, properties2, bean3},
    generalizations={gen_beans_BeanLibrary_NamedElement, gen_beans_Bean_NamedElement, gen_beans_BeanProperty_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)