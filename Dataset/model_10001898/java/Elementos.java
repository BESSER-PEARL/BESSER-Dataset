





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String clasificacion;
    private String referencia;





    private List<OrdenesPedido> ordenespedidos;


    public Elementos(
        String clasificacion,        String referencia    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.ordenespedidos = new ArrayList<>();
    }

    public Elementos(
        String clasificacion,        String referencia        ArrayList<OrdenesPedido> ordenespedidos    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.ordenespedidos = ordenespedidos;
    }

    public String getClasificacion() {
        return clasificacion;
    }

    public void setClasificacion(String clasificacion) {
        this.clasificacion = clasificacion;
    }
    public String getReferencia() {
        return referencia;
    }

    public void setReferencia(String referencia) {
        this.referencia = referencia;
    }

    public List<OrdenesPedido> getOrdenespedidos() {
        return ordenespedidos;
    }

    public void addOrdenespedido(Ordenespedido ordenespedido) {
        this.ordenespedidos.add(ordenespedido);
    }

}