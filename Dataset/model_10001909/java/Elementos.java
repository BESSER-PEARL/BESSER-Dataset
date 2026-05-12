





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String clasificaci_n;
    private String referencia;





    private List<OrdenesPedido> ordenespedidos;


    public Elementos(
        String clasificaci_n,        String referencia    ) {
        this.clasificaci_n = clasificaci_n;
        this.referencia = referencia;
        this.ordenespedidos = new ArrayList<>();
    }

    public Elementos(
        String clasificaci_n,        String referencia        ArrayList<OrdenesPedido> ordenespedidos    ) {
        this.clasificaci_n = clasificaci_n;
        this.referencia = referencia;
        this.ordenespedidos = ordenespedidos;
    }

    public String getClasificaci_n() {
        return clasificaci_n;
    }

    public void setClasificaci_n(String clasificaci_n) {
        this.clasificaci_n = clasificaci_n;
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