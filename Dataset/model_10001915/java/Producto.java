





import java.util.List;
import java.util.ArrayList;

public class Producto  {

    private int cantidad;
    private int codigo;
    private String nombre;
    private float precio;





    private List<Venta> ventas;


    public Producto(
        int cantidad,        int codigo,        String nombre,        float precio    ) {
        this.cantidad = cantidad;
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.ventas = new ArrayList<>();
    }

    public Producto(
        int cantidad,        int codigo,        String nombre,        float precio        ArrayList<Venta> ventas    ) {
        this.cantidad = cantidad;
        this.codigo = codigo;
        this.nombre = nombre;
        this.precio = precio;
        this.ventas = ventas;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public float getPrecio() {
        return precio;
    }

    public void setPrecio(float precio) {
        this.precio = precio;
    }

    public List<Venta> getVentas() {
        return ventas;
    }

    public void addVenta(Venta venta) {
        this.ventas.add(venta);
    }

}