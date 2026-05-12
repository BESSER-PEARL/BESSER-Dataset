





import java.util.List;
import java.util.ArrayList;

public class Pedidos  {

    private String Codigo;
    private String Fecha;





    private Proveedor proveedor;


    public Pedidos(
        String Codigo,        String Fecha    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
    }


    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }

    public Proveedor getProveedor() {
        return proveedor;
    }

    public void setProveedor(Proveedor proveedor) {
        this.proveedor = proveedor;
    }

}