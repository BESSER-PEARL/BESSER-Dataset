





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String Fecha;
    private String Producto;





    private Cliente cliente;




    private Articulo2 articulo2;


    public Consulta(
        String Fecha,        String Producto    ) {
        this.Fecha = Fecha;
        this.Producto = Producto;
    }


    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public Articulo2 getArticulo2() {
        return articulo2;
    }

    public void setArticulo2(Articulo2 articulo2) {
        this.articulo2 = articulo2;
    }

}