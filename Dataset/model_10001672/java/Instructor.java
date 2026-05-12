





import java.util.List;
import java.util.ArrayList;

public class Instructor  {

    private String Nombre;





    private List<Asistencia> asistencias;


    public Instructor(
        String Nombre    ) {
        this.Nombre = Nombre;
        this.asistencias = new ArrayList<>();
    }

    public Instructor(
        String Nombre        ArrayList<Asistencia> asistencias    ) {
        this.Nombre = Nombre;
        this.asistencias = asistencias;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public List<Asistencia> getAsistencias() {
        return asistencias;
    }

    public void addAsistencia(Asistencia asistencia) {
        this.asistencias.add(asistencia);
    }

}