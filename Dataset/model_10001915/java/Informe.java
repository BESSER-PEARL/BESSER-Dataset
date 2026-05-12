





import java.util.List;
import java.util.ArrayList;

public class Informe  {

    private String FilialesTrabajados;
    private String HrsExtrasFiliales;
    private String nombreTrabajador;
    private int HrsTrabajadas;
    private int mesesTrabajadosFiliales;
    private int codigo;





    private List<Trabajador> trabajadors;


    public Informe(
        String FilialesTrabajados,        String HrsExtrasFiliales,        String nombreTrabajador,        int HrsTrabajadas,        int mesesTrabajadosFiliales,        int codigo    ) {
        this.FilialesTrabajados = FilialesTrabajados;
        this.HrsExtrasFiliales = HrsExtrasFiliales;
        this.nombreTrabajador = nombreTrabajador;
        this.HrsTrabajadas = HrsTrabajadas;
        this.mesesTrabajadosFiliales = mesesTrabajadosFiliales;
        this.codigo = codigo;
        this.trabajadors = new ArrayList<>();
    }

    public Informe(
        String FilialesTrabajados,        String HrsExtrasFiliales,        String nombreTrabajador,        int HrsTrabajadas,        int mesesTrabajadosFiliales,        int codigo        ArrayList<Trabajador> trabajadors    ) {
        this.FilialesTrabajados = FilialesTrabajados;
        this.HrsExtrasFiliales = HrsExtrasFiliales;
        this.nombreTrabajador = nombreTrabajador;
        this.HrsTrabajadas = HrsTrabajadas;
        this.mesesTrabajadosFiliales = mesesTrabajadosFiliales;
        this.codigo = codigo;
        this.trabajadors = trabajadors;
    }

    public String getFilialestrabajados() {
        return FilialesTrabajados;
    }

    public void setFilialestrabajados(String FilialesTrabajados) {
        this.FilialesTrabajados = FilialesTrabajados;
    }
    public String getHrsextrasfiliales() {
        return HrsExtrasFiliales;
    }

    public void setHrsextrasfiliales(String HrsExtrasFiliales) {
        this.HrsExtrasFiliales = HrsExtrasFiliales;
    }
    public String getNombretrabajador() {
        return nombreTrabajador;
    }

    public void setNombretrabajador(String nombreTrabajador) {
        this.nombreTrabajador = nombreTrabajador;
    }
    public int getHrstrabajadas() {
        return HrsTrabajadas;
    }

    public void setHrstrabajadas(int HrsTrabajadas) {
        this.HrsTrabajadas = HrsTrabajadas;
    }
    public int getMesestrabajadosfiliales() {
        return mesesTrabajadosFiliales;
    }

    public void setMesestrabajadosfiliales(int mesesTrabajadosFiliales) {
        this.mesesTrabajadosFiliales = mesesTrabajadosFiliales;
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