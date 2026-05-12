





import java.util.List;
import java.util.ArrayList;

public class Facturas  {

    private String nif;
    private String codigo;
    private String direccionPostal;
    private String nombre;



    public Facturas(
        String nif,        String codigo,        String direccionPostal,        String nombre    ) {
        this.nif = nif;
        this.codigo = codigo;
        this.direccionPostal = direccionPostal;
        this.nombre = nombre;
    }


    public String getNif() {
        return nif;
    }

    public void setNif(String nif) {
        this.nif = nif;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getDireccionpostal() {
        return direccionPostal;
    }

    public void setDireccionpostal(String direccionPostal) {
        this.direccionPostal = direccionPostal;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}