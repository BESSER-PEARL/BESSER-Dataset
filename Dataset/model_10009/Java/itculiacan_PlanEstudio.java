





import java.util.List;
import java.util.ArrayList;

public class itculiacan_PlanEstudio  {

    private String nombre;
    private int clave;





    private List<itculiacan_Alumno> itculiacan_alumnos;




    private itculiacan_Alumno itculiacan_alumno;


    public itculiacan_PlanEstudio(
        String nombre,        int clave    ) {
        this.nombre = nombre;
        this.clave = clave;
        this.itculiacan_alumnos = new ArrayList<>();
    }

    public itculiacan_PlanEstudio(
        String nombre,        int clave        ArrayList<itculiacan_Alumno> itculiacan_alumnos    ) {
        this.nombre = nombre;
        this.clave = clave;
        this.itculiacan_alumnos = itculiacan_alumnos;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getClave() {
        return clave;
    }

    public void setClave(int clave) {
        this.clave = clave;
    }

    public List<itculiacan_Alumno> getItculiacan_alumnos() {
        return itculiacan_alumnos;
    }

    public void addItculiacan_alumno(Itculiacan_alumno itculiacan_alumno) {
        this.itculiacan_alumnos.add(itculiacan_alumno);
    }
    public itculiacan_Alumno getItculiacan_alumno() {
        return itculiacan_alumno;
    }

    public void setItculiacan_alumno(itculiacan_Alumno itculiacan_alumno) {
        this.itculiacan_alumno = itculiacan_alumno;
    }

}