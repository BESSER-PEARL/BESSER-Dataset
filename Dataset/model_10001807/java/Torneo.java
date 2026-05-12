





import java.util.List;
import java.util.ArrayList;

public class Torneo  {

    private String Nombre;
    private String Pais;



    public Torneo(
        String Nombre,        String Pais    ) {
        this.Nombre = Nombre;
        this.Pais = Pais;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getPais() {
        return Pais;
    }

    public void setPais(String Pais) {
        this.Pais = Pais;
    }


}