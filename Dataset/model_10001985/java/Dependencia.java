





import java.util.List;
import java.util.ArrayList;

public class Dependencia  {

    private String Nombre;
    private String Codigo;
    private String Responsable;



    public Dependencia(
        String Nombre,        String Codigo,        String Responsable    ) {
        this.Nombre = Nombre;
        this.Codigo = Codigo;
        this.Responsable = Responsable;
    }


    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getResponsable() {
        return Responsable;
    }

    public void setResponsable(String Responsable) {
        this.Responsable = Responsable;
    }


}