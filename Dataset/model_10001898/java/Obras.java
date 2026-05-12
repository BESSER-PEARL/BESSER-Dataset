





import java.util.List;
import java.util.ArrayList;

public class Obras  {

    private String direccion;
    private String codigo;



    public Obras(
        String direccion,        String codigo    ) {
        this.direccion = direccion;
        this.codigo = codigo;
    }


    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }


}