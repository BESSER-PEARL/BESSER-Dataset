





import java.util.List;
import java.util.ArrayList;

public class Pedidos1  {

    private String codigo;
    private String fecha;





    private Empresa empresa;




    private List<Compa_ia> compa_ias;


    public Pedidos1(
        String codigo,        String fecha    ) {
        this.codigo = codigo;
        this.fecha = fecha;
        this.compa_ias = new ArrayList<>();
    }

    public Pedidos1(
        String codigo,        String fecha        ArrayList<Compa_ia> compa_ias    ) {
        this.codigo = codigo;
        this.fecha = fecha;
        this.compa_ias = compa_ias;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }
    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public Empresa getEmpresa() {
        return empresa;
    }

    public void setEmpresa(Empresa empresa) {
        this.empresa = empresa;
    }
    public List<Compa_ia> getCompa_ias() {
        return compa_ias;
    }

    public void addCompa_ia(Compa_ia compa_ia) {
        this.compa_ias.add(compa_ia);
    }

}