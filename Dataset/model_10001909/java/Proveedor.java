





import java.util.List;
import java.util.ArrayList;

public class Proveedor  {

    private String razonSocial;
    private String tel_fonos;
    private String nit;
    private String direcci_n;





    private List<OrdenesPedido> ordenespedidos;




    private List<Pedidos> pedidoss;


    public Proveedor(
        String razonSocial,        String tel_fonos,        String nit,        String direcci_n    ) {
        this.razonSocial = razonSocial;
        this.tel_fonos = tel_fonos;
        this.nit = nit;
        this.direcci_n = direcci_n;
        this.ordenespedidos = new ArrayList<>();
        this.pedidoss = new ArrayList<>();
    }

    public Proveedor(
        String razonSocial,        String tel_fonos,        String nit,        String direcci_n        ArrayList<OrdenesPedido> ordenespedidos,        ArrayList<Pedidos> pedidoss    ) {
        this.razonSocial = razonSocial;
        this.tel_fonos = tel_fonos;
        this.nit = nit;
        this.direcci_n = direcci_n;
        this.ordenespedidos = ordenespedidos;
        this.pedidoss = pedidoss;
    }

    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public String getTel_fonos() {
        return tel_fonos;
    }

    public void setTel_fonos(String tel_fonos) {
        this.tel_fonos = tel_fonos;
    }
    public String getNit() {
        return nit;
    }

    public void setNit(String nit) {
        this.nit = nit;
    }
    public String getDirecci_n() {
        return direcci_n;
    }

    public void setDirecci_n(String direcci_n) {
        this.direcci_n = direcci_n;
    }

    public List<OrdenesPedido> getOrdenespedidos() {
        return ordenespedidos;
    }

    public void addOrdenespedido(Ordenespedido ordenespedido) {
        this.ordenespedidos.add(ordenespedido);
    }
    public List<Pedidos> getPedidoss() {
        return pedidoss;
    }

    public void addPedidos(Pedidos pedidos) {
        this.pedidoss.add(pedidos);
    }

}