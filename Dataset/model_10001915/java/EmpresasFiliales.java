





import java.util.List;
import java.util.ArrayList;

public class EmpresasFiliales  {

    private String razonSocial;
    private int codigo;





    private List<Trabajador> trabajadors;


    public EmpresasFiliales(
        String razonSocial,        int codigo    ) {
        this.razonSocial = razonSocial;
        this.codigo = codigo;
        this.trabajadors = new ArrayList<>();
    }

    public EmpresasFiliales(
        String razonSocial,        int codigo        ArrayList<Trabajador> trabajadors    ) {
        this.razonSocial = razonSocial;
        this.codigo = codigo;
        this.trabajadors = trabajadors;
    }

    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public List<Trabajador> getTrabajadors() {
        return trabajadors;
    }

    public void addTrabajador(Trabajador trabajador) {
        this.trabajadors.add(trabajador);
    }

}