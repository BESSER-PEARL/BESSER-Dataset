





import java.util.List;
import java.util.ArrayList;

public class Proveedores  {

    private String direccion;
    private int telefonos;
    private String razonSocial;
    private String nit;





    private List<OrdenesPedido> ordenespedidos;


    public Proveedores(
        String direccion,        int telefonos,        String razonSocial,        String nit    ) {
        this.direccion = direccion;
        this.telefonos = telefonos;
        this.razonSocial = razonSocial;
        this.nit = nit;
        this.ordenespedidos = new ArrayList<>();
    }

    public Proveedores(
        String direccion,        int telefonos,        String razonSocial,        String nit        ArrayList<OrdenesPedido> ordenespedidos    ) {
        this.direccion = direccion;
        this.telefonos = telefonos;
        this.razonSocial = razonSocial;
        this.nit = nit;
        this.ordenespedidos = ordenespedidos;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
    public int getTelefonos() {
        return telefonos;
    }

    public void setTelefonos(int telefonos) {
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

    public List<OrdenesPedido> getOrdenespedidos() {
        return ordenespedidos;
    }

    public void addOrdenespedido(Ordenespedido ordenespedido) {
        this.ordenespedidos.add(ordenespedido);
    }

}