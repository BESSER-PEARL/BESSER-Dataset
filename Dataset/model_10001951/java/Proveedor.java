





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String telefono;
    private String nombre;
    private String direccion;
    private String nit;





    private List<OrdenesPedidos> ordenespedidoss;


    public Proveedor(
        String telefono,        String nombre,        String direccion,        String nit    ) {
        this.telefono = telefono;
        this.nombre = nombre;
        this.direccion = direccion;
        this.nit = nit;
        this.ordenespedidoss = new ArrayList<>();
    }

    public Proveedor(
        String telefono,        String nombre,        String direccion,        String nit        ArrayList<OrdenesPedidos> ordenespedidoss    ) {
        this.telefono = telefono;
        this.nombre = nombre;
        this.direccion = direccion;
        this.nit = nit;
        this.ordenespedidoss = ordenespedidoss;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public String getNit() {
        return nit;
    }

    public void setNit(String nit) {
        this.nit = nit;
    }

    public List<OrdenesPedidos> getOrdenespedidoss() {
        return ordenespedidoss;
    }

    public void addOrdenespedidos(Ordenespedidos ordenespedidos) {
        this.ordenespedidoss.add(ordenespedidos);
    }

}