





import java.util.List;
import java.util.ArrayList;

public class Ventas  {

    private String Producto;
    private None Monto;
    private String Fecha;
    private String Cantidad;





    private Producto producto;


    public Ventas(
        String Producto,        None Monto,        String Fecha,        String Cantidad    ) {
        this.Producto = Producto;
        this.Monto = Monto;
        this.Fecha = Fecha;
        this.Cantidad = Cantidad;
    }


    public String getProducto() {
        return Producto;
    }

    public void setProducto(String Producto) {
        this.Producto = Producto;
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
    public String getCantidad() {
        return Cantidad;
    }

    public void setCantidad(String Cantidad) {
        this.Cantidad = Cantidad;
    }

    public Producto getProducto() {
        return producto;
    }

    public void setProducto(Producto producto) {
        this.producto = producto;
    }

}