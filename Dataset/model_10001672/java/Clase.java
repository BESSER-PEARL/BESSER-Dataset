





import java.util.List;
import java.util.ArrayList;

public class Clase  {

    private String Nombre;
    private String Asistencia;





    private List<Asistencia> asistencias;


    public Clase(
        String Nombre,        String Asistencia    ) {
        this.Nombre = Nombre;
        this.Asistencia = Asistencia;
        this.asistencias = new ArrayList<>();
    }

    public Clase(
        String Nombre,        String Asistencia        ArrayList<Asistencia> asistencias    ) {
        this.Nombre = Nombre;
        this.Asistencia = Asistencia;
        this.asistencias = asistencias;
    }

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getAsistencia() {
        return Asistencia;
    }

    public void setAsistencia(String Asistencia) {
        this.Asistencia = Asistencia;
    }

    public List<Asistencia> getAsistencias() {
        return asistencias;
    }

    public void addAsistencia(Asistencia asistencia) {
        this.asistencias.add(asistencia);
    }

}