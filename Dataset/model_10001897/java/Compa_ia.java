





import java.util.List;
import java.util.ArrayList;

public class Compa_ia  {

    private String codigo;
    private String zona;





    private List<Comerciales> comercialess;




    private List<Facturas> facturass;


    public Compa_ia(
        String codigo,        String zona    ) {
        this.codigo = codigo;
        this.zona = zona;
        this.comercialess = new ArrayList<>();
        this.facturass = new ArrayList<>();
    }

    public Compa_ia(
        String codigo,        String zona        ArrayList<Comerciales> comercialess,        ArrayList<Facturas> facturass    ) {
        this.codigo = codigo;
        this.zona = zona;
        this.comercialess = comercialess;
        this.facturass = facturass;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getZona() {
        return zona;
    }

    public void setZona(String zona) {
        this.zona = zona;
    }

    public List<Comerciales> getComercialess() {
        return comercialess;
    }

    public void addComerciales(Comerciales comerciales) {
        this.comercialess.add(comerciales);
    }
    public List<Facturas> getFacturass() {
        return facturass;
    }

    public void addFacturas(Facturas facturas) {
        this.facturass.add(facturas);
    }

}