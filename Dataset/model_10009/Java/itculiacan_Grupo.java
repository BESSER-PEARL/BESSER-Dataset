





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Grupo  {

    private int clave;





    private List<itculiacan_Alumno> itculiacan_alumnos;




    private itculiacan_Alumno itculiacan_alumno;


    public itculiacan_Grupo(
        int clave    ) {
        this.clave = clave;
        this.itculiacan_alumnos = new ArrayList<>();
    }

    public itculiacan_Grupo(
        int clave        ArrayList<itculiacan_Alumno> itculiacan_alumnos    ) {
        this.clave = clave;
        this.itculiacan_alumnos = itculiacan_alumnos;
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