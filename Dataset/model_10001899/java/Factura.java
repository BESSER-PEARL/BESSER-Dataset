





import java.util.List;
import java.util.ArrayList;

public class Factura  {

    private String codigo;
    private String fecha;





    private Proveedor proveedor;


    public Factura(
        String codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
    }


    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public Proveedor getProveedor() {
        return proveedor;
    }

    public void setProveedor(Proveedor proveedor) {
        this.proveedor = proveedor;
    }

}