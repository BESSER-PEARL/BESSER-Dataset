





import java.util.List;
import java.util.ArrayList;

public class Caja  {

    private None Dinero_Inicio;
    private None Arqueo;
    private String Fecha;
    private None moto_final;





    private Supervisor supervisor;




    private List<Ventas> ventass;




    private List<Jornada> jornadas;


    public Caja(
        None Dinero_Inicio,        None Arqueo,        String Fecha,        None moto_final    ) {
        this.Dinero_Inicio = Dinero_Inicio;
        this.Arqueo = Arqueo;
        this.Fecha = Fecha;
        this.moto_final = moto_final;
        this.ventass = new ArrayList<>();
        this.jornadas = new ArrayList<>();
    }

    public Caja(
        None Dinero_Inicio,        None Arqueo,        String Fecha,        None moto_final        ArrayList<Ventas> ventass,        ArrayList<Jornada> jornadas    ) {
        this.Dinero_Inicio = Dinero_Inicio;
        this.Arqueo = Arqueo;
        this.Fecha = Fecha;
        this.moto_final = moto_final;
        this.ventass = ventass;
        this.jornadas = jornadas;
    }

    public None getDinero_inicio() {
        return Dinero_Inicio;
    }

    public void setDinero_inicio(None Dinero_Inicio) {
        this.Dinero_Inicio = Dinero_Inicio;
    }
    public None getArqueo() {
        return Arqueo;
    }

    public void setArqueo(None Arqueo) {
        this.Arqueo = Arqueo;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public None getMoto_final() {
        return moto_final;
    }

    public void setMoto_final(None moto_final) {
        this.moto_final = moto_final;
    }

    public Supervisor getSupervisor() {
        return supervisor;
    }

    public void setSupervisor(Supervisor supervisor) {
        this.supervisor = supervisor;
    }
    public List<Ventas> getVentass() {
        return ventass;
    }

    public void addVentas(Ventas ventas) {
        this.ventass.add(ventas);
    }
    public List<Jornada> getJornadas() {
        return jornadas;
    }

    public void addJornada(Jornada jornada) {
        this.jornadas.add(jornada);
    }

}