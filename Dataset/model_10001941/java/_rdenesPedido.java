





import java.util.List;
import java.util.ArrayList;

public class _rdenesPedido  {

    private String fecha;
    private String codigo;





    private Proveedor proveedor;


    public _rdenesPedido(
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

    public Proveedor getProveedor() {
        return proveedor;
    }

    public void setProveedor(Proveedor proveedor) {
        this.proveedor = proveedor;
    }

}