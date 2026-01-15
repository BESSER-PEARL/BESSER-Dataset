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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean")
    }
)

# Classes
soopl_Class = Class(name="soopl::Class")
soopl_NamedElement = Class(name="soopl::NamedElement", is_abstract=True)
soopl_Package = Class(name="soopl::Package")
NamedElement = Class(name="NamedElement")
soopl_Action = Class(name="soopl::Action", is_abstract=True)
soopl_Method = Class(name="soopl::Method")
soopl_Property = Class(name="soopl::Property", is_abstract=True)
soopl_StatefulClass = Class(name="soopl::StatefulClass")
Class_ = Class(name="Class")
soopl_StateImplementationClass = Class(name="soopl::StateImplementationClass")
soopl_StateClass = Class(name="soopl::StateClass")
soopl_SimpleTypeProperty = Class(name="soopl::SimpleTypeProperty")
Property_ = Class(name="Property")
soopl_ComplexTypeProperty = Class(name="soopl::ComplexTypeProperty")
soopl_Parameter = Class(name="soopl::Parameter")
soopl_TransitionMethod = Class(name="soopl::TransitionMethod")
Method_ = Class(name="Method")
soopl_Transition = Class(name="soopl::Transition")
soopl_AssignProperty = Class(name="soopl::AssignProperty")
soopl_Guard = Class(name="soopl::Guard", is_abstract=True)
soopl_SimpleTypeParameter = Class(name="soopl::SimpleTypeParameter")
Parameter_ = Class(name="Parameter")
soopl_ComplexTypeParameter = Class(name="soopl::ComplexTypeParameter")
soopl_CallMethodAction = Class(name="soopl::CallMethodAction", is_abstract=True)
Action = Class(name="Action")
soopl_ParameterBinding = Class(name="soopl::ParameterBinding")
soopl_IsInStateCondition = Class(name="soopl::IsInStateCondition", is_abstract=True)
Guard = Class(name="Guard")
soopl_PropertyIsInState = Class(name="soopl::PropertyIsInState")
IsInStateCondition = Class(name="IsInStateCondition")
soopl_ParameterIsInState = Class(name="soopl::ParameterIsInState")
soopl_CallMethodOfProperty = Class(name="soopl::CallMethodOfProperty")
CallMethodAction = Class(name="CallMethodAction")
soopl_CallMethodOfParameter = Class(name="soopl::CallMethodOfParameter")

# soopl_Class class attributes and methods
soopl_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
soopl_Class.attributes={soopl_Class_isAbstract}

# soopl_NamedElement class attributes and methods
soopl_NamedElement_name: Property = Property(name="name", type=StringType)
soopl_NamedElement.attributes={soopl_NamedElement_name}

# soopl_Package class attributes and methods

# NamedElement class attributes and methods

# soopl_Action class attributes and methods

# soopl_Method class attributes and methods

# soopl_Property class attributes and methods
soopl_Property_upperBound: Property = Property(name="upperBound", type=IntegerType)
soopl_Property_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
soopl_Property_multiValued: Property = Property(name="multiValued", type=BooleanType)
soopl_Property.attributes={soopl_Property_multiValued, soopl_Property_lowerBound, soopl_Property_upperBound}

# soopl_StatefulClass class attributes and methods

# Class class attributes and methods

# soopl_StateImplementationClass class attributes and methods

# soopl_StateClass class attributes and methods

# soopl_SimpleTypeProperty class attributes and methods
soopl_SimpleTypeProperty_dataType: Property = Property(name="dataType", type=StringType)
soopl_SimpleTypeProperty.attributes={soopl_SimpleTypeProperty_dataType}

# Property class attributes and methods

# soopl_ComplexTypeProperty class attributes and methods

# soopl_Parameter class attributes and methods

# soopl_TransitionMethod class attributes and methods

# Method class attributes and methods

# soopl_Transition class attributes and methods

# soopl_AssignProperty class attributes and methods

# soopl_Guard class attributes and methods

# soopl_SimpleTypeParameter class attributes and methods
soopl_SimpleTypeParameter_dataType: Property = Property(name="dataType", type=StringType)
soopl_SimpleTypeParameter.attributes={soopl_SimpleTypeParameter_dataType}

# Parameter class attributes and methods

# soopl_ComplexTypeParameter class attributes and methods

# soopl_CallMethodAction class attributes and methods

# Action class attributes and methods

# soopl_ParameterBinding class attributes and methods

# soopl_IsInStateCondition class attributes and methods

# Guard class attributes and methods

# soopl_PropertyIsInState class attributes and methods

# IsInStateCondition class attributes and methods

# soopl_ParameterIsInState class attributes and methods

# soopl_CallMethodOfProperty class attributes and methods

# CallMethodAction class attributes and methods

# soopl_CallMethodOfParameter class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="soopl_Class", type=soopl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Package", type=soopl_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages2: BinaryAssociation = BinaryAssociation(
    name="packages2",
    ends={
        Property(name="Package", type=soopl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="parentPackage", type=soopl_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentPackage4: BinaryAssociation = BinaryAssociation(
    name="parentPackage4",
    ends={
        Property(name="Package5", type=soopl_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=soopl_Package, multiplicity=Multiplicity(0, 1))
    }
)
actions33: BinaryAssociation = BinaryAssociation(
    name="actions33",
    ends={
        Property(name="soopl_Action", type=soopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Transition34", type=soopl_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods6: BinaryAssociation = BinaryAssociation(
    name="methods6",
    ends={
        Property(name="soopl_Method", type=soopl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Class7", type=soopl_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties8: BinaryAssociation = BinaryAssociation(
    name="properties8",
    ends={
        Property(name="soopl_Property", type=soopl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Class9", type=soopl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass11: BinaryAssociation = BinaryAssociation(
    name="superClass11",
    ends={
        Property(name="soopl_Class12", type=soopl_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Class10", type=soopl_Class, multiplicity=Multiplicity(0, 1))
    }
)
initialState13: BinaryAssociation = BinaryAssociation(
    name="initialState13",
    ends={
        Property(name="soopl_StateImplementationClass", type=soopl_StatefulClass, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_StatefulClass", type=soopl_StateImplementationClass, multiplicity=Multiplicity(1, 1))
    }
)
stateClass14: BinaryAssociation = BinaryAssociation(
    name="stateClass14",
    ends={
        Property(name="soopl_StateClass", type=soopl_StatefulClass, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_StatefulClass15", type=soopl_StateClass, multiplicity=Multiplicity(1, 1))
    }
)
statefulClass16: BinaryAssociation = BinaryAssociation(
    name="statefulClass16",
    ends={
        Property(name="soopl_StatefulClass18", type=soopl_StateClass, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_StateClass17", type=soopl_StatefulClass, multiplicity=Multiplicity(1, 1))
    }
)
entryMethod19: BinaryAssociation = BinaryAssociation(
    name="entryMethod19",
    ends={
        Property(name="soopl_Method21", type=soopl_StateImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_StateImplementationClass20", type=soopl_Method, multiplicity=Multiplicity(0, 9999))
    }
)
stateClass22: BinaryAssociation = BinaryAssociation(
    name="stateClass22",
    ends={
        Property(name="soopl_StateClass24", type=soopl_StateImplementationClass, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_StateImplementationClass23", type=soopl_StateClass, multiplicity=Multiplicity(1, 1))
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="soopl_Class26", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ComplexTypeProperty", type=soopl_Class, multiplicity=Multiplicity(1, 1))
    }
)
opposite28: BinaryAssociation = BinaryAssociation(
    name="opposite28",
    ends={
        Property(name="soopl_ComplexTypeProperty29", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ComplexTypeProperty27", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(0, 1))
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="soopl_Parameter", type=soopl_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Method31", type=soopl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions32: BinaryAssociation = BinaryAssociation(
    name="transitions32",
    ends={
        Property(name="soopl_Transition", type=soopl_TransitionMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_TransitionMethod", type=soopl_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter60: BinaryAssociation = BinaryAssociation(
    name="parameter60",
    ends={
        Property(name="soopl_Parameter61", type=soopl_CallMethodOfParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_CallMethodOfParameter", type=soopl_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
parameter62: BinaryAssociation = BinaryAssociation(
    name="parameter62",
    ends={
        Property(name="soopl_Parameter63", type=soopl_AssignProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_AssignProperty", type=soopl_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
property64: BinaryAssociation = BinaryAssociation(
    name="property64",
    ends={
        Property(name="soopl_ComplexTypeProperty66", type=soopl_AssignProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_AssignProperty65", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(1, 1))
    }
)
guard35: BinaryAssociation = BinaryAssociation(
    name="guard35",
    ends={
        Property(name="soopl_Guard", type=soopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Transition36", type=soopl_Guard, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
targetState37: BinaryAssociation = BinaryAssociation(
    name="targetState37",
    ends={
        Property(name="soopl_StateImplementationClass39", type=soopl_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_Transition38", type=soopl_StateImplementationClass, multiplicity=Multiplicity(1, 1))
    }
)
classType40: BinaryAssociation = BinaryAssociation(
    name="classType40",
    ends={
        Property(name="soopl_Class41", type=soopl_ComplexTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ComplexTypeParameter", type=soopl_Class, multiplicity=Multiplicity(1, 1))
    }
)
calledMethod42: BinaryAssociation = BinaryAssociation(
    name="calledMethod42",
    ends={
        Property(name="soopl_Method43", type=soopl_CallMethodAction, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_CallMethodAction", type=soopl_Method, multiplicity=Multiplicity(1, 1))
    }
)
parameterBinding44: BinaryAssociation = BinaryAssociation(
    name="parameterBinding44",
    ends={
        Property(name="soopl_ParameterBinding", type=soopl_CallMethodAction, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_CallMethodAction45", type=soopl_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structuralFeatureBinding46: BinaryAssociation = BinaryAssociation(
    name="structuralFeatureBinding46",
    ends={
        Property(name="soopl_Property48", type=soopl_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ParameterBinding47", type=soopl_Property, multiplicity=Multiplicity(0, 1))
    }
)
parameter49: BinaryAssociation = BinaryAssociation(
    name="parameter49",
    ends={
        Property(name="soopl_Parameter51", type=soopl_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ParameterBinding50", type=soopl_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
inState52: BinaryAssociation = BinaryAssociation(
    name="inState52",
    ends={
        Property(name="soopl_StateImplementationClass53", type=soopl_IsInStateCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_IsInStateCondition", type=soopl_StateImplementationClass, multiplicity=Multiplicity(1, 1))
    }
)
property54: BinaryAssociation = BinaryAssociation(
    name="property54",
    ends={
        Property(name="soopl_ComplexTypeProperty55", type=soopl_PropertyIsInState, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_PropertyIsInState", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(1, 1))
    }
)
parameter56: BinaryAssociation = BinaryAssociation(
    name="parameter56",
    ends={
        Property(name="soopl_Parameter57", type=soopl_ParameterIsInState, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_ParameterIsInState", type=soopl_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
property58: BinaryAssociation = BinaryAssociation(
    name="property58",
    ends={
        Property(name="soopl_ComplexTypeProperty59", type=soopl_CallMethodOfProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="soopl_CallMethodOfProperty", type=soopl_ComplexTypeProperty, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_soopl_Package_NamedElement = Generalization(general=NamedElement, specific=soopl_Package)
gen_soopl_Property_NamedElement = Generalization(general=NamedElement, specific=soopl_Property)
gen_soopl_Class_NamedElement = Generalization(general=NamedElement, specific=soopl_Class)
gen_soopl_StatefulClass_Class = Generalization(general=Class_, specific=soopl_StatefulClass)
gen_soopl_StateClass_Class = Generalization(general=Class_, specific=soopl_StateClass)
gen_soopl_StateImplementationClass_Class = Generalization(general=Class_, specific=soopl_StateImplementationClass)
gen_soopl_SimpleTypeProperty_Property = Generalization(general=Property_, specific=soopl_SimpleTypeProperty)
gen_soopl_ComplexTypeProperty_Property = Generalization(general=Property_, specific=soopl_ComplexTypeProperty)
gen_soopl_Method_NamedElement = Generalization(general=NamedElement, specific=soopl_Method)
gen_soopl_TransitionMethod_Method = Generalization(general=Method_, specific=soopl_TransitionMethod)
gen_soopl_AssignProperty_Action = Generalization(general=Action, specific=soopl_AssignProperty)
gen_soopl_Parameter_NamedElement = Generalization(general=NamedElement, specific=soopl_Parameter)
gen_soopl_SimpleTypeParameter_Parameter = Generalization(general=Parameter_, specific=soopl_SimpleTypeParameter)
gen_soopl_ComplexTypeParameter_Parameter = Generalization(general=Parameter_, specific=soopl_ComplexTypeParameter)
gen_soopl_CallMethodAction_Action = Generalization(general=Action, specific=soopl_CallMethodAction)
gen_soopl_IsInStateCondition_Guard = Generalization(general=Guard, specific=soopl_IsInStateCondition)
gen_soopl_PropertyIsInState_IsInStateCondition = Generalization(general=IsInStateCondition, specific=soopl_PropertyIsInState)
gen_soopl_ParameterIsInState_IsInStateCondition = Generalization(general=IsInStateCondition, specific=soopl_ParameterIsInState)
gen_soopl_CallMethodOfProperty_CallMethodAction = Generalization(general=CallMethodAction, specific=soopl_CallMethodOfProperty)
gen_soopl_CallMethodOfParameter_CallMethodAction = Generalization(general=CallMethodAction, specific=soopl_CallMethodOfParameter)

# Domain Model
domain_model = DomainModel(
    name="soopl",
    types={soopl_Class, soopl_NamedElement, soopl_Package, NamedElement, soopl_Action, soopl_Method, soopl_Property, soopl_StatefulClass, Class_, soopl_StateImplementationClass, soopl_StateClass, soopl_SimpleTypeProperty, Property_, soopl_ComplexTypeProperty, soopl_Parameter, soopl_TransitionMethod, Method_, soopl_Transition, soopl_AssignProperty, soopl_Guard, soopl_SimpleTypeParameter, Parameter_, soopl_ComplexTypeParameter, soopl_CallMethodAction, Action, soopl_ParameterBinding, soopl_IsInStateCondition, Guard, soopl_PropertyIsInState, IsInStateCondition, soopl_ParameterIsInState, soopl_CallMethodOfProperty, CallMethodAction, soopl_CallMethodOfParameter, DataType},
    associations={classes0, packages2, parentPackage4, actions33, methods6, properties8, superClass11, initialState13, stateClass14, statefulClass16, entryMethod19, stateClass22, type25, opposite28, parameters30, transitions32, parameter60, parameter62, property64, guard35, targetState37, classType40, calledMethod42, parameterBinding44, structuralFeatureBinding46, parameter49, inState52, property54, parameter56, property58},
    generalizations={gen_soopl_Package_NamedElement, gen_soopl_Property_NamedElement, gen_soopl_Class_NamedElement, gen_soopl_StatefulClass_Class, gen_soopl_StateClass_Class, gen_soopl_StateImplementationClass_Class, gen_soopl_SimpleTypeProperty_Property, gen_soopl_ComplexTypeProperty_Property, gen_soopl_Method_NamedElement, gen_soopl_TransitionMethod_Method, gen_soopl_AssignProperty_Action, gen_soopl_Parameter_NamedElement, gen_soopl_SimpleTypeParameter_Parameter, gen_soopl_ComplexTypeParameter_Parameter, gen_soopl_CallMethodAction_Action, gen_soopl_IsInStateCondition_Guard, gen_soopl_PropertyIsInState_IsInStateCondition, gen_soopl_ParameterIsInState_IsInStateCondition, gen_soopl_CallMethodOfProperty_CallMethodAction, gen_soopl_CallMethodOfParameter_CallMethodAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)