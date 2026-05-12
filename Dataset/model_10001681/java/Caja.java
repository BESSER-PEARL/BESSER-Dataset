





import java.util.List;
import java.util.ArrayList;

public class Caja  {

    private String Fecha;
    private None Dinero_Inicio;
    private None Arqueo;





    private List<Ventas> ventass;




    private Supervisor supervisor;




    private List<Jornada> jornadas;


    public Caja(
        String Fecha,        None Dinero_Inicio,        None Arqueo    ) {
        this.Fecha = Fecha;
        this.Dinero_Inicio = Dinero_Inicio;
        this.Arqueo = Arqueo;
        this.ventass = new ArrayList<>();
        this.jornadas = new ArrayList<>();
    }

    public Caja(
        String Fecha,        None Dinero_Inicio,        None Arqueo        ArrayList<Ventas> ventass,        ArrayList<Jornada> jornadas    ) {
        this.Fecha = Fecha;
        this.Dinero_Inicio = Dinero_Inicio;
        this.Arqueo = Arqueo;
        this.ventass = ventass;
        this.jornadas = jornadas;
    }

    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
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

    public List<Ventas> getVentass() {
        return ventass;
    }

    public void addVentas(Ventas ventas) {
        this.ventass.add(ventas);
    }
    public Supervisor getSupervisor() {
        return supervisor;
    }

    public void setSupervisor(Supervisor supervisor) {
        this.supervisor = supervisor;
    }
    public List<Jornada> getJornadas() {
        return jornadas;
    }

    public void addJornada(Jornada jornada) {
        this.jornadas.add(jornada);
    }

}