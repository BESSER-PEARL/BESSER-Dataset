





import java.util.List;
import java.util.ArrayList;

public class Envio  {

    private String Codigo;
    private String Fecha;





    private List<Articulo2> articulo2s;




    private Cliente cliente;




    private Cliente cliente;




    private Pedido pedido;


    public Envio(
        String Codigo,        String Fecha    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.articulo2s = new ArrayList<>();
    }

    public Envio(
        String Codigo,        String Fecha        ArrayList<Articulo2> articulo2s    ) {
        this.Codigo = Codigo;
        this.Fecha = Fecha;
        this.articulo2s = articulo2s;
    }

    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }

    public List<Articulo2> getArticulo2s() {
        return articulo2s;
    }

    public void addArticulo2(Articulo2 articulo2) {
        this.articulo2s.add(articulo2);
    }
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public Pedido getPedido() {
        return pedido;
    }

    public void setPedido(Pedido pedido) {
        this.pedido = pedido;
    }

}