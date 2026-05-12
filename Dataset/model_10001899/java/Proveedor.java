





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String direccion;
    private String telefonos;
    private String razonSocial;
    private String nit;





    private List<Ordenes_Pedidos> ordenes_pedidoss;


    public Proveedor(
        String direccion,        String telefonos,        String razonSocial,        String nit    ) {
        this.direccion = direccion;
        this.telefonos = telefonos;
        this.razonSocial = razonSocial;
        this.nit = nit;
        this.ordenes_pedidoss = new ArrayList<>();
    }

    public Proveedor(
        String direccion,        String telefonos,        String razonSocial,        String nit        ArrayList<Ordenes_Pedidos> ordenes_pedidoss    ) {
        this.direccion = direccion;
        this.telefonos = telefonos;
        this.razonSocial = razonSocial;
        this.nit = nit;
        this.ordenes_pedidoss = ordenes_pedidoss;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public String getTelefonos() {
        return telefonos;
    }

    public void setTelefonos(String telefonos) {
        this.telefonos = telefonos;
    }
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getNit() {
        return nit;
    }

    public void setNit(String nit) {
        this.nit = nit;
    }

    public List<Ordenes_Pedidos> getOrdenes_pedidoss() {
        return ordenes_pedidoss;
    }

    public void addOrdenes_pedidos(Ordenes_pedidos ordenes_pedidos) {
        this.ordenes_pedidoss.add(ordenes_pedidos);
    }

}