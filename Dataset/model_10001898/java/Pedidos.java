





import java.util.List;
import java.util.ArrayList;

public class Pedidos  {

    private String fecha;
    private String codigo;





    private Proveedores proveedores;


    public Pedidos(
        String fecha,        String codigo    ) {
        this.fecha = fecha;
        this.codigo = codigo;
    }


    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public Proveedores getProveedores() {
        return proveedores;
    }

    public void setProveedores(Proveedores proveedores) {
        this.proveedores = proveedores;
    }

}