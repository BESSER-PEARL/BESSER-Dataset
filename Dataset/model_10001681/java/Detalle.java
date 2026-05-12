





import java.util.List;
import java.util.ArrayList;

public class Detalle  {

    private String Producto;
    private None Precio;
    private String Cantidad;





    private Pedido pedido;


    public Detalle(
        String Producto,        None Precio,        String Cantidad    ) {
        this.Producto = Producto;
        this.Precio = Precio;
        this.Cantidad = Cantidad;
    }


    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
    }
    public None getPrecio() {
        return Precio;
    }

    public void setPrecio(None Precio) {
        this.Precio = Precio;
    }
    public String getCantidad() {
        return Cantidad;
    }

    public void setCantidad(String Cantidad) {
        this.Cantidad = Cantidad;
    }

    public Pedido getPedido() {
        return pedido;
    }

    public void setPedido(Pedido pedido) {
        this.pedido = pedido;
    }

}