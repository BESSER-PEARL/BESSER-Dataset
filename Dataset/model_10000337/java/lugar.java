





import java.util.List;
import java.util.ArrayList;

public class lugar  {

    private int nombre;
    private int Id_lugar;
    private String attribute;



    public lugar(
        int nombre,        int Id_lugar,        String attribute    ) {
        this.nombre = nombre;
        this.Id_lugar = Id_lugar;
        this.attribute = attribute;
    }


    public int getNombre() {
        return nombre;
    }

    public void setNombre(int nombre) {
        this.nombre = nombre;
    }
    public int getId_lugar() {
        return Id_lugar;
    }

    public void setId_lugar(int Id_lugar) {
        this.Id_lugar = Id_lugar;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}