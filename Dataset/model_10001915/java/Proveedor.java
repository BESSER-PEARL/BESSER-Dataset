





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String razonSocial;
    private String telefono;
    private String direccion;
    private String nit;





    private List<OrdenesPedidos> ordenespedidoss;


    public Proveedor(
        String razonSocial,        String telefono,        String direccion,        String nit    ) {
        this.razonSocial = razonSocial;
        this.telefono = telefono;
        this.direccion = direccion;
        this.nit = nit;
        this.ordenespedidoss = new ArrayList<>();
    }

    public Proveedor(
        String razonSocial,        String telefono,        String direccion,        String nit        ArrayList<OrdenesPedidos> ordenespedidoss    ) {
        this.razonSocial = razonSocial;
        this.telefono = telefono;
        this.direccion = direccion;
        this.nit = nit;
        this.ordenespedidoss = ordenespedidoss;
    }

    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
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