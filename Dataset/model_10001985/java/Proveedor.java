





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String Direccion;
    private String Nit;
    private String Razonsocial;
    private String Telefonos;





    private List<Factura> facturas;




    private List<OrdenesPedidos> ordenespedidoss;


    public Proveedor(
        String Direccion,        String Nit,        String Razonsocial,        String Telefonos    ) {
        this.Direccion = Direccion;
        this.Nit = Nit;
        this.Razonsocial = Razonsocial;
        this.Telefonos = Telefonos;
        this.facturas = new ArrayList<>();
        this.ordenespedidoss = new ArrayList<>();
    }

    public Proveedor(
        String Direccion,        String Nit,        String Razonsocial,        String Telefonos        ArrayList<Factura> facturas,        ArrayList<OrdenesPedidos> ordenespedidoss    ) {
        this.Direccion = Direccion;
        this.Nit = Nit;
        this.Razonsocial = Razonsocial;
        this.Telefonos = Telefonos;
        this.facturas = facturas;
        this.ordenespedidoss = ordenespedidoss;
    }

    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
    }
    public String getNit() {
        return Nit;
    }

    public void setNit(String Nit) {
        this.Nit = Nit;
    }
    public String getRazonsocial() {
        return Razonsocial;
    }

    public void setRazonsocial(String Razonsocial) {
        this.Razonsocial = Razonsocial;
    }
    public String getTelefonos() {
        return Telefonos;
    }

    public void setTelefonos(String Telefonos) {
        this.Telefonos = Telefonos;
    }

    public List<Factura> getFacturas() {
        return facturas;
    }

    public void addFactura(Factura factura) {
        this.facturas.add(factura);
    }
    public List<OrdenesPedidos> getOrdenespedidoss() {
        return ordenespedidoss;
    }

    public void addOrdenespedidos(Ordenespedidos ordenespedidos) {
        this.ordenespedidoss.add(ordenespedidos);
    }

}