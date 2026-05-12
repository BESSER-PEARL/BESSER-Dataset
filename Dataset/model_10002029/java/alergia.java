





import java.util.List;
import java.util.ArrayList;

public class alergia  {

    private int alergiaID;
    private String nombre;



    public alergia(
        int alergiaID,        String nombre    ) {
        this.alergiaID = alergiaID;
        this.nombre = nombre;
    }


    public int getAlergiaid() {
        return alergiaID;
    }

    public void setAlergiaid(int alergiaID) {
        this.alergiaID = alergiaID;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}