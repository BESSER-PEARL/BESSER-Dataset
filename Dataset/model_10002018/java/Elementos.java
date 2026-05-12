





import java.util.List;
import java.util.ArrayList;

public class Elementos  {

    private String clasificacion;
    private String referencia;





    private List<OrdenesPedidos> ordenespedidoss;


    public Elementos(
        String clasificacion,        String referencia    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.ordenespedidoss = new ArrayList<>();
    }

    public Elementos(
        String clasificacion,        String referencia        ArrayList<OrdenesPedidos> ordenespedidoss    ) {
        this.clasificacion = clasificacion;
        this.referencia = referencia;
        this.ordenespedidoss = ordenespedidoss;
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

    public List<OrdenesPedidos> getOrdenespedidoss() {
        return ordenespedidoss;
    }

    public void addOrdenespedidos(Ordenespedidos ordenespedidos) {
        this.ordenespedidoss.add(ordenespedidos);
    }

}