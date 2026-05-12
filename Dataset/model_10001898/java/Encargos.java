





import java.util.List;
import java.util.ArrayList;

public class Encargos  {

    private String codigo;
    private String detalles;





    private Comprador comprador;




    private List<Obras> obrass;


    public Encargos(
        String codigo,        String detalles    ) {
        this.codigo = codigo;
        this.detalles = detalles;
        this.obrass = new ArrayList<>();
    }

    public Encargos(
        String codigo,        String detalles        ArrayList<Obras> obrass    ) {
        this.codigo = codigo;
        this.detalles = detalles;
        this.obrass = obrass;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getDetalles() {
        return detalles;
    }

    public void setDetalles(String detalles) {
        this.detalles = detalles;
    }

    public Comprador getComprador() {
        return comprador;
    }

    public void setComprador(Comprador comprador) {
        this.comprador = comprador;
    }
    public List<Obras> getObrass() {
        return obrass;
    }

    public void addObras(Obras obras) {
        this.obrass.add(obras);
    }

}