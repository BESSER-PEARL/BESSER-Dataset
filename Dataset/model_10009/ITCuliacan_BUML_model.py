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
Nombramiento: Enumeration = Enumeration(
    name="Nombramiento",
    literals={
            EnumerationLiteral(name="medioTiempo"),
			EnumerationLiteral(name="tiempoCompleto")
    }
)

# Classes
itculiacan_Alumno = Class(name="itculiacan_Alumno")
itculiacan_Generacion = Class(name="itculiacan_Generacion")
itculiacan_PlanEstudio = Class(name="itculiacan_PlanEstudio")
itculiacan_Grupo = Class(name="itculiacan_Grupo")
itculiacan_Aula = Class(name="itculiacan_Aula")
itculiacan_Materia = Class(name="itculiacan_Materia")
itculiacan_Profesor = Class(name="itculiacan_Profesor")
itculiacan_Universidad = Class(name="itculiacan_Universidad")

# itculiacan_Alumno class attributes and methods
itculiacan_Alumno_nombre: Property = Property(name="nombre", type=StringType)
itculiacan_Alumno_numeroControl: Property = Property(name="numeroControl", type=IntegerType)
itculiacan_Alumno.attributes={itculiacan_Alumno_numeroControl, itculiacan_Alumno_nombre}

# itculiacan_Generacion class attributes and methods
itculiacan_Generacion_fechaInicio: Property = Property(name="fechaInicio", type=DateType)
itculiacan_Generacion_fechaFin: Property = Property(name="fechaFin", type=DateType)
itculiacan_Generacion.attributes={itculiacan_Generacion_fechaFin, itculiacan_Generacion_fechaInicio}

# itculiacan_PlanEstudio class attributes and methods
itculiacan_PlanEstudio_clave: Property = Property(name="clave", type=IntegerType)
itculiacan_PlanEstudio_nombre: Property = Property(name="nombre", type=StringType)
itculiacan_PlanEstudio.attributes={itculiacan_PlanEstudio_nombre, itculiacan_PlanEstudio_clave}

# itculiacan_Grupo class attributes and methods
itculiacan_Grupo_clave: Property = Property(name="clave", type=IntegerType)
itculiacan_Grupo.attributes={itculiacan_Grupo_clave}

# itculiacan_Aula class attributes and methods
itculiacan_Aula_clave: Property = Property(name="clave", type=IntegerType)
itculiacan_Aula_capacidad: Property = Property(name="capacidad", type=IntegerType)
itculiacan_Aula.attributes={itculiacan_Aula_clave, itculiacan_Aula_capacidad}

# itculiacan_Materia class attributes and methods
itculiacan_Materia_clave: Property = Property(name="clave", type=IntegerType)
itculiacan_Materia_nombre: Property = Property(name="nombre", type=StringType)
itculiacan_Materia.attributes={itculiacan_Materia_clave, itculiacan_Materia_nombre}

# itculiacan_Profesor class attributes and methods
itculiacan_Profesor_clave: Property = Property(name="clave", type=IntegerType)
itculiacan_Profesor_nombre: Property = Property(name="nombre", type=StringType)
itculiacan_Profesor_numeroMaterias: Property = Property(name="numeroMaterias", type=IntegerType)
itculiacan_Profesor_nombramiento: Property = Property(name="nombramiento", type=StringType)
itculiacan_Profesor.attributes={itculiacan_Profesor_nombramiento, itculiacan_Profesor_nombre, itculiacan_Profesor_clave, itculiacan_Profesor_numeroMaterias}

# itculiacan_Universidad class attributes and methods

# Relationships
generacion0: BinaryAssociation = BinaryAssociation(
    name="generacion0",
    ends={
        Property(name="Generacion", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 1)),
        Property(name="alumnos", type=itculiacan_Generacion, multiplicity=Multiplicity(1, 1))
    }
)
cursa1: BinaryAssociation = BinaryAssociation(
    name="cursa1",
    ends={
        Property(name="PlanEstudio", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 1)),
        Property(name="alumnos2", type=itculiacan_PlanEstudio, multiplicity=Multiplicity(1, 1))
    }
)
grupos3: BinaryAssociation = BinaryAssociation(
    name="grupos3",
    ends={
        Property(name="Grupo", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 1)),
        Property(name="alumnos4", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 9999))
    }
)
alumnos5: BinaryAssociation = BinaryAssociation(
    name="alumnos5",
    ends={
        Property(name="Alumno", type=itculiacan_Generacion, multiplicity=Multiplicity(1, 1)),
        Property(name="generacion", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 9999))
    }
)
aula6: BinaryAssociation = BinaryAssociation(
    name="aula6",
    ends={
        Property(name="Aula", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 1)),
        Property(name="grupos", type=itculiacan_Aula, multiplicity=Multiplicity(1, 1))
    }
)
materia7: BinaryAssociation = BinaryAssociation(
    name="materia7",
    ends={
        Property(name="Materia", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 1)),
        Property(name="grupos8", type=itculiacan_Materia, multiplicity=Multiplicity(1, 1))
    }
)
profesor9: BinaryAssociation = BinaryAssociation(
    name="profesor9",
    ends={
        Property(name="Profesor", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 1)),
        Property(name="grupos10", type=itculiacan_Profesor, multiplicity=Multiplicity(1, 1))
    }
)
alumnos11: BinaryAssociation = BinaryAssociation(
    name="alumnos11",
    ends={
        Property(name="Alumno13", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 1)),
        Property(name="grupos12", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 9999))
    }
)
grupos14: BinaryAssociation = BinaryAssociation(
    name="grupos14",
    ends={
        Property(name="Grupo15", type=itculiacan_Aula, multiplicity=Multiplicity(1, 1)),
        Property(name="aula", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 9999))
    }
)
grupos16: BinaryAssociation = BinaryAssociation(
    name="grupos16",
    ends={
        Property(name="Grupo17", type=itculiacan_Materia, multiplicity=Multiplicity(1, 1)),
        Property(name="materia", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 9999))
    }
)
planesEstudio18: BinaryAssociation = BinaryAssociation(
    name="planesEstudio18",
    ends={
        Property(name="PlanEstudio19", type=itculiacan_Materia, multiplicity=Multiplicity(1, 1)),
        Property(name="materias", type=itculiacan_PlanEstudio, multiplicity=Multiplicity(1, 9999))
    }
)
grupos20: BinaryAssociation = BinaryAssociation(
    name="grupos20",
    ends={
        Property(name="Grupo21", type=itculiacan_Profesor, multiplicity=Multiplicity(1, 1)),
        Property(name="profesor", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 9999))
    }
)
alumnos22: BinaryAssociation = BinaryAssociation(
    name="alumnos22",
    ends={
        Property(name="Alumno23", type=itculiacan_PlanEstudio, multiplicity=Multiplicity(1, 1)),
        Property(name="cursa", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 9999))
    }
)
materias24: BinaryAssociation = BinaryAssociation(
    name="materias24",
    ends={
        Property(name="Materia25", type=itculiacan_PlanEstudio, multiplicity=Multiplicity(1, 1)),
        Property(name="planesEstudio", type=itculiacan_Materia, multiplicity=Multiplicity(1, 9999))
    }
)
refProfesor26: BinaryAssociation = BinaryAssociation(
    name="refProfesor26",
    ends={
        Property(name="itculiacan_Profesor", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad", type=itculiacan_Profesor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refAulas27: BinaryAssociation = BinaryAssociation(
    name="refAulas27",
    ends={
        Property(name="itculiacan_Aula", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad28", type=itculiacan_Aula, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refPlanEstudio29: BinaryAssociation = BinaryAssociation(
    name="refPlanEstudio29",
    ends={
        Property(name="itculiacan_PlanEstudio", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad30", type=itculiacan_PlanEstudio, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refAlumno31: BinaryAssociation = BinaryAssociation(
    name="refAlumno31",
    ends={
        Property(name="itculiacan_Alumno", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad32", type=itculiacan_Alumno, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refGeneracion33: BinaryAssociation = BinaryAssociation(
    name="refGeneracion33",
    ends={
        Property(name="itculiacan_Generacion", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad34", type=itculiacan_Generacion, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refMateria35: BinaryAssociation = BinaryAssociation(
    name="refMateria35",
    ends={
        Property(name="itculiacan_Materia", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad36", type=itculiacan_Materia, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refGrupo37: BinaryAssociation = BinaryAssociation(
    name="refGrupo37",
    ends={
        Property(name="itculiacan_Grupo", type=itculiacan_Universidad, multiplicity=Multiplicity(1, 1)),
        Property(name="itculiacan_Universidad38", type=itculiacan_Grupo, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)


# OCL Constraints
numeroControl: Constraint = Constraint(
    name="numeroControl",
    context=itculiacan_Alumno,
    expression="context Alumno inv: numeroControl > 0",
    language="OCL"
)
clave: Constraint = Constraint(
    name="clave",
    context=itculiacan_Grupo,
    expression="context Grupo inv: clave > 0",
    language="OCL"
)
clave1: Constraint = Constraint(
    name="clave1",
    context=itculiacan_Materia,
    expression="context Materia inv: clave > 0",
    language="OCL"
)
clave2: Constraint = Constraint(
    name="clave2",
    context=itculiacan_PlanEstudio,
    expression="context PlanEstudio inv: clave > 0",
    language="OCL"
)
clave3: Constraint = Constraint(
    name="clave3",
    context=itculiacan_Aula,
    expression="context Aula inv: clave > 0",
    language="OCL"
)
clave4: Constraint = Constraint(
    name="clave4",
    context=itculiacan_Profesor,
    expression="context Profesor inv: clave > 0",
    language="OCL"
)
capacidadMaximaGrupo: Constraint = Constraint(
    name="capacidadMaximaGrupo",
    context=itculiacan_Grupo,
    expression="context Grupo inv: self.alumnos->size() <= 40",
    language="OCL"
)
grupoMenorACapacidadAula: Constraint = Constraint(
    name="grupoMenorACapacidadAula",
    context=itculiacan_Grupo,
    expression="context Grupo inv: alumnos->asSet()->size() <= aula.capacidad",
    language="OCL"
)
materiasMaximasProfesor: Constraint = Constraint(
    name="materiasMaximasProfesor",
    context=itculiacan_Profesor,
    expression="context Profesor inv: grupos->asSet()->size() <= numeroMaterias",
    language="OCL"
)
materiasDePlanEstudio: Constraint = Constraint(
    name="materiasDePlanEstudio",
    context=itculiacan_Alumno,
    expression="context Alumno inv: grupos.materia->forAll(m | self.cursa.materias->includes(m))",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="itculiacan",
    types={itculiacan_Alumno, itculiacan_Generacion, itculiacan_PlanEstudio, itculiacan_Grupo, itculiacan_Aula, itculiacan_Materia, itculiacan_Profesor, itculiacan_Universidad, Nombramiento},
    associations={generacion0, cursa1, grupos3, alumnos5, aula6, materia7, profesor9, alumnos11, grupos14, grupos16, planesEstudio18, grupos20, alumnos22, materias24, refProfesor26, refAulas27, refPlanEstudio29, refAlumno31, refGeneracion33, refMateria35, refGrupo37},
    constraints={numeroControl, clave, clave1, clave2, clave3, clave4, capacidadMaximaGrupo, grupoMenorACapacidadAula, materiasMaximasProfesor, materiasDePlanEstudio},
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