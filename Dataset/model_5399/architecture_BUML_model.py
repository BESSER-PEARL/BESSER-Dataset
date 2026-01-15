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
architectureTool_Component = Class(name="architectureTool::Component")
architectureTool_Port = Class(name="architectureTool::Port", is_abstract=True)
architectureTool_Class = Class(name="architectureTool::Class")
architectureTool_Interface = Class(name="architectureTool::Interface")
architectureTool_System = Class(name="architectureTool::System")
classMember = Class(name="classMember")
architectureTool_classMember = Class(name="architectureTool::classMember", is_abstract=True)
architectureTool_Attribute = Class(name="architectureTool::Attribute")
architectureTool_Method = Class(name="architectureTool::Method")

# architectureTool_Component class attributes and methods
architectureTool_Component_name: Property = Property(name="name", type=StringType)
architectureTool_Component.attributes={architectureTool_Component_name}

# architectureTool_Port class attributes and methods
architectureTool_Port_type: Property = Property(name="type", type=StringType)
architectureTool_Port_simple: Property = Property(name="simple", type=StringType)
architectureTool_Port_provided: Property = Property(name="provided", type=StringType)
architectureTool_Port_required: Property = Property(name="required", type=StringType)
architectureTool_Port_name: Property = Property(name="name", type=StringType)
architectureTool_Port.attributes={architectureTool_Port_name, architectureTool_Port_type, architectureTool_Port_required, architectureTool_Port_simple, architectureTool_Port_provided}

# architectureTool_Class class attributes and methods

# architectureTool_Interface class attributes and methods

# architectureTool_System class attributes and methods
architectureTool_System_name: Property = Property(name="name", type=StringType)
architectureTool_System.attributes={architectureTool_System_name}

# classMember class attributes and methods

# architectureTool_classMember class attributes and methods
architectureTool_classMember_name: Property = Property(name="name", type=StringType)
architectureTool_classMember.attributes={architectureTool_classMember_name}

# architectureTool_Attribute class attributes and methods
architectureTool_Attribute_name: Property = Property(name="name", type=StringType)
architectureTool_Attribute_type: Property = Property(name="type", type=StringType)
architectureTool_Attribute_Visable: Property = Property(name="Visable", type=StringType)
architectureTool_Attribute.attributes={architectureTool_Attribute_name, architectureTool_Attribute_Visable, architectureTool_Attribute_type}

# architectureTool_Method class attributes and methods
architectureTool_Method_name: Property = Property(name="name", type=StringType)
architectureTool_Method_returnType: Property = Property(name="returnType", type=StringType)
architectureTool_Method_visable: Property = Property(name="visable", type=StringType)
architectureTool_Method_parameter: Property = Property(name="parameter", type=StringType)
architectureTool_Method.attributes={architectureTool_Method_name, architectureTool_Method_returnType, architectureTool_Method_parameter, architectureTool_Method_visable}

# Relationships
portOfComponent0: BinaryAssociation = BinaryAssociation(
    name="portOfComponent0",
    ends={
        Property(name="architectureTool_Port", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Component", type=architectureTool_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentDependence2: BinaryAssociation = BinaryAssociation(
    name="componentDependence2",
    ends={
        Property(name="architectureTool_Component3", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Component1", type=architectureTool_Component, multiplicity=Multiplicity(0, 9999))
    }
)
class4: BinaryAssociation = BinaryAssociation(
    name="class4",
    ends={
        Property(name="architectureTool_Class", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Component5", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentOfComponent7: BinaryAssociation = BinaryAssociation(
    name="componentOfComponent7",
    ends={
        Property(name="architectureTool_Component8", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Component6", type=architectureTool_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceOfComponent9: BinaryAssociation = BinaryAssociation(
    name="interfaceOfComponent9",
    ends={
        Property(name="architectureTool_Interface", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Component10", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Aggregation25: BinaryAssociation = BinaryAssociation(
    name="Aggregation25",
    ends={
        Property(name="architectureTool_Class26", type=architectureTool_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Class24", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999))
    }
)
SystemDependence28: BinaryAssociation = BinaryAssociation(
    name="SystemDependence28",
    ends={
        Property(name="architectureTool_System", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_System27", type=architectureTool_System, multiplicity=Multiplicity(0, 9999))
    }
)
componentOfSystem29: BinaryAssociation = BinaryAssociation(
    name="componentOfSystem29",
    ends={
        Property(name="architectureTool_Component31", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_System30", type=architectureTool_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
portOfSystem32: BinaryAssociation = BinaryAssociation(
    name="portOfSystem32",
    ends={
        Property(name="architectureTool_Port34", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_System33", type=architectureTool_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
System36: BinaryAssociation = BinaryAssociation(
    name="System36",
    ends={
        Property(name="architectureTool_System37", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_System35", type=architectureTool_System, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaceOfSystem38: BinaryAssociation = BinaryAssociation(
    name="interfaceOfSystem38",
    ends={
        Property(name="architectureTool_Interface40", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_System39", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ComponentDependence41: BinaryAssociation = BinaryAssociation(
    name="ComponentDependence41",
    ends={
        Property(name="Component", type=architectureTool_System, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentDependence42", type=architectureTool_Component, multiplicity=Multiplicity(0, 9999))
    }
)
providedRealize43: BinaryAssociation = BinaryAssociation(
    name="providedRealize43",
    ends={
        Property(name="architectureTool_Interface45", type=architectureTool_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Port44", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
portDependence47: BinaryAssociation = BinaryAssociation(
    name="portDependence47",
    ends={
        Property(name="architectureTool_Port48", type=architectureTool_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Port46", type=architectureTool_Port, multiplicity=Multiplicity(0, 9999))
    }
)
requiredRealize49: BinaryAssociation = BinaryAssociation(
    name="requiredRealize49",
    ends={
        Property(name="architectureTool_Interface51", type=architectureTool_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Port50", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
ComponentDependence11: BinaryAssociation = BinaryAssociation(
    name="ComponentDependence11",
    ends={
        Property(name="System", type=architectureTool_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="ComponentDependence", type=architectureTool_System, multiplicity=Multiplicity(0, 9999))
    }
)
Association13: BinaryAssociation = BinaryAssociation(
    name="Association13",
    ends={
        Property(name="architectureTool_Class14", type=architectureTool_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Class12", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999))
    }
)
InterfaceAbstract15: BinaryAssociation = BinaryAssociation(
    name="InterfaceAbstract15",
    ends={
        Property(name="architectureTool_Interface17", type=architectureTool_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Class16", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
Generalization19: BinaryAssociation = BinaryAssociation(
    name="Generalization19",
    ends={
        Property(name="architectureTool_Class20", type=architectureTool_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Class18", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999))
    }
)
composition22: BinaryAssociation = BinaryAssociation(
    name="composition22",
    ends={
        Property(name="architectureTool_Class23", type=architectureTool_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Class21", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attribute64: BinaryAssociation = BinaryAssociation(
    name="attribute64",
    ends={
        Property(name="architectureTool_Attribute", type=architectureTool_classMember, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_classMember", type=architectureTool_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method65: BinaryAssociation = BinaryAssociation(
    name="method65",
    ends={
        Property(name="architectureTool_Method", type=architectureTool_classMember, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_classMember66", type=architectureTool_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
providedRealize52: BinaryAssociation = BinaryAssociation(
    name="providedRealize52",
    ends={
        Property(name="architectureTool_Port54", type=architectureTool_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Interface53", type=architectureTool_Port, multiplicity=Multiplicity(0, 9999))
    }
)
InterfaceRealize55: BinaryAssociation = BinaryAssociation(
    name="InterfaceRealize55",
    ends={
        Property(name="architectureTool_Class57", type=architectureTool_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Interface56", type=architectureTool_Class, multiplicity=Multiplicity(0, 9999))
    }
)
InterfaceDependence59: BinaryAssociation = BinaryAssociation(
    name="InterfaceDependence59",
    ends={
        Property(name="architectureTool_Interface60", type=architectureTool_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Interface58", type=architectureTool_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
requiredRealize61: BinaryAssociation = BinaryAssociation(
    name="requiredRealize61",
    ends={
        Property(name="architectureTool_Port63", type=architectureTool_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="architectureTool_Interface62", type=architectureTool_Port, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_architectureTool_Interface_classMember = Generalization(general=classMember, specific=architectureTool_Interface)
gen_architectureTool_Class_classMember = Generalization(general=classMember, specific=architectureTool_Class)

# Domain Model
domain_model = DomainModel(
    name="architectureTool",
    types={architectureTool_Component, architectureTool_Port, architectureTool_Class, architectureTool_Interface, architectureTool_System, classMember, architectureTool_classMember, architectureTool_Attribute, architectureTool_Method},
    associations={portOfComponent0, componentDependence2, class4, componentOfComponent7, interfaceOfComponent9, Aggregation25, SystemDependence28, componentOfSystem29, portOfSystem32, System36, interfaceOfSystem38, ComponentDependence41, providedRealize43, portDependence47, requiredRealize49, ComponentDependence11, Association13, InterfaceAbstract15, Generalization19, composition22, attribute64, method65, providedRealize52, InterfaceRealize55, InterfaceDependence59, requiredRealize61},
    generalizations={gen_architectureTool_Interface_classMember, gen_architectureTool_Class_classMember},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)