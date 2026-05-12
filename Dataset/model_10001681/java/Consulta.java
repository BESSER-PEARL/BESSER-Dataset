





import java.util.List;
import java.util.ArrayList;

public class Consulta  {

    private String Producto;
    private String Fecha;





    private Cliente cliente;




    private List<Articulo2> articulo2s;


    public Consulta(
        String Producto,        String Fecha    ) {
        this.Producto = Producto;
        this.Fecha = Fecha;
        this.articulo2s = new ArrayList<>();
    }

    public Consulta(
        String Producto,        String Fecha        ArrayList<Articulo2> articulo2s    ) {
        this.Producto = Producto;
        this.Fecha = Fecha;
        this.articulo2s = articulo2s;
    }

    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public List<Articulo2> getArticulo2s() {
        return articulo2s;
    }

    public void addArticulo2(Articulo2 articulo2) {
        this.articulo2s.add(articulo2);
    }

}