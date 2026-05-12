





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String telefonos;
    private String direccion;
    private String nit;
    private String razonSocial;





    private List<OrdenesPedidos> ordenespedidoss;


    public Proveedor(
        String telefonos,        String direccion,        String nit,        String razonSocial    ) {
        this.telefonos = telefonos;
        this.direccion = direccion;
        this.nit = nit;
        this.razonSocial = razonSocial;
        this.ordenespedidoss = new ArrayList<>();
    }

    public Proveedor(
        String telefonos,        String direccion,        String nit,        String razonSocial        ArrayList<OrdenesPedidos> ordenespedidoss    ) {
        this.telefonos = telefonos;
        this.direccion = direccion;
        this.nit = nit;
        this.razonSocial = razonSocial;
        this.ordenespedidoss = ordenespedidoss;
    }

    public String getTelefonos() {
        return telefonos;
    }

    public void setTelefonos(String telefonos) {
        this.telefonos = telefonos;
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
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }

    public List<OrdenesPedidos> getOrdenespedidoss() {
        return ordenespedidoss;
    }

    public void addOrdenespedidos(Ordenespedidos ordenespedidos) {
        this.ordenespedidoss.add(ordenespedidos);
    }

}