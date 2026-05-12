





import java.util.List;
import java.util.ArrayList;

public class Envio  {

    private String Fecha;
    private String Codigo;





    private Cliente cliente;




    private Pedido pedido;




    private List<Articulo2> articulo2s;


    public Envio(
        String Fecha,        String Codigo    ) {
        this.Fecha = Fecha;
        this.Codigo = Codigo;
        this.articulo2s = new ArrayList<>();
    }

    public Envio(
        String Fecha,        String Codigo        ArrayList<Articulo2> articulo2s    ) {
        this.Fecha = Fecha;
        this.Codigo = Codigo;
        this.articulo2s = articulo2s;
    }

    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getCodigo() {
        return Codigo;
    }

    public void setCodigo(String Codigo) {
        this.Codigo = Codigo;
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
    public List<Articulo2> getArticulo2s() {
        return articulo2s;
    }

    public void addArticulo2(Articulo2 articulo2) {
        this.articulo2s.add(articulo2);
    }

}