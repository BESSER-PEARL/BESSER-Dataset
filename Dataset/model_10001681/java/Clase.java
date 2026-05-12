





import java.util.List;
import java.util.ArrayList;

public class Clase  {

    private String Nombre;
    private String Asistencia;





    private Asistencia asistencia;


    public Clase(
        String Nombre,        String Asistencia    ) {
        this.Nombre = Nombre;
        this.Asistencia = Asistencia;
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

    public Asistencia getAsistencia() {
        return asistencia;
    }

    public void setAsistencia(Asistencia asistencia) {
        this.asistencia = asistencia;
    }

}