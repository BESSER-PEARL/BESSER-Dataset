





import java.util.List;
import java.util.ArrayList;

public class Detalle  {

    private String Producto;
    private String Cantidad;
    private None Precio;





    private Pedido pedido;




    private List<Articulo2> articulo2s;


    public Detalle(
        String Producto,        String Cantidad,        None Precio    ) {
        this.Producto = Producto;
        this.Cantidad = Cantidad;
        this.Precio = Precio;
        this.articulo2s = new ArrayList<>();
    }

    public Detalle(
        String Producto,        String Cantidad,        None Precio        ArrayList<Articulo2> articulo2s    ) {
        this.Producto = Producto;
        this.Cantidad = Cantidad;
        this.Precio = Precio;
        this.articulo2s = articulo2s;
    }

    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
    }
    public String getCantidad() {
        return Cantidad;
    }

    public void setCantidad(String Cantidad) {
        this.Cantidad = Cantidad;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }

    public Pedido getPedido() {
        return pedido;
    }

    public void setPedido(Pedido pedido) {
        this.pedido = pedido;
    }
    public List<Articulo2> getArticulo2s() {
        return articulo2s;
    }

    public void addArticulo2(Articulo2 articulo2) {
        this.articulo2s.add(articulo2);
    }

}