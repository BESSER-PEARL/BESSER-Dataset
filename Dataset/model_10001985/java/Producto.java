





import java.util.List;
import java.util.ArrayList;

public class Producto  {

    private int Codigo;
    private int Cantidad;
    private int CalcularCosto;
    private String Nombre;
    private int Precio;





    private Venta venta;


    public Producto(
        int Codigo,        int Cantidad,        int CalcularCosto,        String Nombre,        int Precio    ) {
        this.Codigo = Codigo;
        this.Cantidad = Cantidad;
        this.CalcularCosto = CalcularCosto;
        this.Nombre = Nombre;
        this.Precio = Precio;
    }


    public int getCodigo() {
        return Codigo;
    }

    public void setCodigo(int Codigo) {
        this.Codigo = Codigo;
    }
    public int getCantidad() {
        return Cantidad;
    }

    public void setCantidad(int Cantidad) {
        this.Cantidad = Cantidad;
    }
    public int getCalcularcosto() {
        return CalcularCosto;
    }

    public void setCalcularcosto(int CalcularCosto) {
        this.CalcularCosto = CalcularCosto;
    }
    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }
    public int getPrecio() {
        return Precio;
    }

    public void setPrecio(int Precio) {
        this.Precio = Precio;
    }

    public Venta getVenta() {
        return venta;
    }

    public void setVenta(Venta venta) {
        this.venta = venta;
    }

}