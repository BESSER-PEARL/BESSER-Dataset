





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Universidad  {






    private List<itculiacan_Profesor> itculiacan_profesors;




    private List<itculiacan_Aula> itculiacan_aulas;




    private List<itculiacan_PlanEstudio> itculiacan_planestudios;




    private List<itculiacan_Alumno> itculiacan_alumnos;




    private List<itculiacan_Materia> itculiacan_materias;




    private List<itculiacan_Grupo> itculiacan_grupos;




    private List<itculiacan_Generacion> itculiacan_generacions;


    public itculiacan_Universidad(
    ) {
        this.itculiacan_profesors = new ArrayList<>();
        this.itculiacan_aulas = new ArrayList<>();
        this.itculiacan_planestudios = new ArrayList<>();
        this.itculiacan_alumnos = new ArrayList<>();
        this.itculiacan_materias = new ArrayList<>();
        this.itculiacan_grupos = new ArrayList<>();
        this.itculiacan_generacions = new ArrayList<>();
    }

    public itculiacan_Universidad(
        ArrayList<itculiacan_Profesor> itculiacan_profesors,        ArrayList<itculiacan_Aula> itculiacan_aulas,        ArrayList<itculiacan_PlanEstudio> itculiacan_planestudios,        ArrayList<itculiacan_Alumno> itculiacan_alumnos,        ArrayList<itculiacan_Materia> itculiacan_materias,        ArrayList<itculiacan_Grupo> itculiacan_grupos,        ArrayList<itculiacan_Generacion> itculiacan_generacions    ) {
        this.itculiacan_profesors = itculiacan_profesors;
        this.itculiacan_aulas = itculiacan_aulas;
        this.itculiacan_planestudios = itculiacan_planestudios;
        this.itculiacan_alumnos = itculiacan_alumnos;
        this.itculiacan_materias = itculiacan_materias;
        this.itculiacan_grupos = itculiacan_grupos;
        this.itculiacan_generacions = itculiacan_generacions;
    }


    public List<itculiacan_Profesor> getItculiacan_profesors() {
        return itculiacan_profesors;
    }

    public void addItculiacan_profesor(Itculiacan_profesor itculiacan_profesor) {
        this.itculiacan_profesors.add(itculiacan_profesor);
    }
    public List<itculiacan_Aula> getItculiacan_aulas() {
        return itculiacan_aulas;
    }

    public void addItculiacan_aula(Itculiacan_aula itculiacan_aula) {
        this.itculiacan_aulas.add(itculiacan_aula);
    }
    public List<itculiacan_PlanEstudio> getItculiacan_planestudios() {
        return itculiacan_planestudios;
    }

    public void addItculiacan_planestudio(Itculiacan_planestudio itculiacan_planestudio) {
        this.itculiacan_planestudios.add(itculiacan_planestudio);
    }
    public List<itculiacan_Alumno> getItculiacan_alumnos() {
        return itculiacan_alumnos;
    }

    public void addItculiacan_alumno(Itculiacan_alumno itculiacan_alumno) {
        this.itculiacan_alumnos.add(itculiacan_alumno);
    }
    public List<itculiacan_Materia> getItculiacan_materias() {
        return itculiacan_materias;
    }

    public void addItculiacan_materia(Itculiacan_materia itculiacan_materia) {
        this.itculiacan_materias.add(itculiacan_materia);
    }
    public List<itculiacan_Grupo> getItculiacan_grupos() {
        return itculiacan_grupos;
    }

    public void addItculiacan_grupo(Itculiacan_grupo itculiacan_grupo) {
        this.itculiacan_grupos.add(itculiacan_grupo);
    }
    public List<itculiacan_Generacion> getItculiacan_generacions() {
        return itculiacan_generacions;
    }

    public void addItculiacan_generacion(Itculiacan_generacion itculiacan_generacion) {
        this.itculiacan_generacions.add(itculiacan_generacion);
    }

}