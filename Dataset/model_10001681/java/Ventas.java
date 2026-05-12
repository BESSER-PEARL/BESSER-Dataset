





import java.util.List;
import java.util.ArrayList;

public class Ventas  {

    private String Cantidad;
    private None Monto;
    private String Fecha;
    private String Producto;





    private List<Producto> productos;


    public Ventas(
        String Cantidad,        None Monto,        String Fecha,        String Producto    ) {
        this.Cantidad = Cantidad;
        this.Monto = Monto;
        this.Fecha = Fecha;
        this.Producto = Producto;
        this.productos = new ArrayList<>();
    }

    public Ventas(
        String Cantidad,        None Monto,        String Fecha,        String Producto        ArrayList<Producto> productos    ) {
        this.Cantidad = Cantidad;
        this.Monto = Monto;
        this.Fecha = Fecha;
        this.Producto = Producto;
        this.productos = productos;
    }

    public String getCantidad() {
        return Cantidad;
    }

    public void setCantidad(String Cantidad) {
        this.Cantidad = Cantidad;
    }
    public None getMonto() {
        return Monto;
    }

    public void setMonto(None Monto) {
        this.Monto = Monto;
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

    public List<Producto> getProductos() {
        return productos;
    }

    public void addProducto(Producto producto) {
        this.productos.add(producto);
    }

}