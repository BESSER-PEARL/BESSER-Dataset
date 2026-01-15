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
testall_AbstractComponent = Class(name="testall::AbstractComponent", is_abstract=True)
testall_Content = Class(name="testall::Content")
testall_Required = Class(name="testall::Required")
testall_Provided = Class(name="testall::Provided")
testall_Interface = Class(name="testall::Interface", is_abstract=True)
testall_Binding = Class(name="testall::Binding")
Interface = Class(name="Interface")
testall_Component = Class(name="testall::Component")
AbstractComponent = Class(name="AbstractComponent")

# testall_AbstractComponent class attributes and methods
testall_AbstractComponent_name: Property = Property(name="name", type=StringType)
testall_AbstractComponent.attributes={testall_AbstractComponent_name}

# testall_Content class attributes and methods
testall_Content_expression: Property = Property(name="expression", type=StringType)
testall_Content_language: Property = Property(name="language", type=StringType)
testall_Content.attributes={testall_Content_language, testall_Content_expression}

# testall_Required class attributes and methods

# testall_Provided class attributes and methods

# testall_Interface class attributes and methods
testall_Interface_name: Property = Property(name="name", type=StringType)
testall_Interface_signature: Property = Property(name="signature", type=StringType)
testall_Interface.attributes={testall_Interface_name, testall_Interface_signature}

# testall_Binding class attributes and methods

# Interface class attributes and methods

# testall_Component class attributes and methods

# AbstractComponent class attributes and methods

# Relationships
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="testall_Interface8", type=testall_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_Binding7", type=testall_Interface, multiplicity=Multiplicity(0, 1))
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="testall_Content", type=testall_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_AbstractComponent", type=testall_Content, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
requiredInterfaces1: BinaryAssociation = BinaryAssociation(
    name="requiredInterfaces1",
    ends={
        Property(name="testall_Required", type=testall_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_AbstractComponent2", type=testall_Required, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedInterfaces3: BinaryAssociation = BinaryAssociation(
    name="providedInterfaces3",
    ends={
        Property(name="testall_Provided", type=testall_AbstractComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_AbstractComponent4", type=testall_Provided, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings5: BinaryAssociation = BinaryAssociation(
    name="bindings5",
    ends={
        Property(name="testall_Binding", type=testall_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_Interface", type=testall_Binding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="testall_Interface11", type=testall_Binding, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_Binding10", type=testall_Interface, multiplicity=Multiplicity(0, 1))
    }
)
contentParent12: BinaryAssociation = BinaryAssociation(
    name="contentParent12",
    ends={
        Property(name="testall_AbstractComponent14", type=testall_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_Content13", type=testall_AbstractComponent, multiplicity=Multiplicity(1, 1))
    }
)
subComponents16: BinaryAssociation = BinaryAssociation(
    name="subComponents16",
    ends={
        Property(name="testall_Component", type=testall_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="testall_Component15", type=testall_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_testall_Required_Interface = Generalization(general=Interface, specific=testall_Required)
gen_testall_Provided_Interface = Generalization(general=Interface, specific=testall_Provided)
gen_testall_Component_AbstractComponent = Generalization(general=AbstractComponent, specific=testall_Component)

# Domain Model
domain_model = DomainModel(
    name="testall",
    types={testall_AbstractComponent, testall_Content, testall_Required, testall_Provided, testall_Interface, testall_Binding, Interface, testall_Component, AbstractComponent},
    associations={from6, content0, requiredInterfaces1, providedInterfaces3, bindings5, to9, contentParent12, subComponents16},
    generalizations={gen_testall_Required_Interface, gen_testall_Provided_Interface, gen_testall_Component_AbstractComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)