





import java.util.List;
import java.util.ArrayList;

public class itculiacan_Alumno  {

    private int numeroControl;
    private String nombre;



    public itculiacan_Alumno(
        int numeroControl,        String nombre    ) {
        this.numeroControl = numeroControl;
        this.nombre = nombre;
    }


    public int getNumerocontrol() {
        return numeroControl;
    }

    public void setNumerocontrol(int numeroControl) {
        this.numeroControl = numeroControl;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}