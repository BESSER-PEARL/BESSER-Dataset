





import java.util.List;
import java.util.ArrayList;

public class _reasConocimiento  {






    private Departamento departamento;




    private List<Profesores> profesoress;


    public _reasConocimiento(
    ) {
        this.profesoress = new ArrayList<>();
    }

    public _reasConocimiento(
        ArrayList<Profesores> profesoress    ) {
        this.profesoress = profesoress;
    }


    public Departamento getDepartamento() {
        return departamento;
    }

    public void setDepartamento(Departamento departamento) {
        this.departamento = departamento;
    }
    public List<Profesores> getProfesoress() {
        return profesoress;
    }

    public void addProfesores(Profesores profesores) {
        this.profesoress.add(profesores);
    }

}