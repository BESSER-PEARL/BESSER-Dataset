





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private String Local;
    private String Ganador;
    private String Cod_liga;
    private String Fecha;
    private String Cod_partido;
    private String Visita;
    private String Hora;
    private String GolLocal;
    private String GolVisita;





    private Equipo equipo;




    private Equipo equipo;


    public Partido(
        String Local,        String Ganador,        String Cod_liga,        String Fecha,        String Cod_partido,        String Visita,        String Hora,        String GolLocal,        String GolVisita    ) {
        this.Local = Local;
        this.Ganador = Ganador;
        this.Cod_liga = Cod_liga;
        this.Fecha = Fecha;
        this.Cod_partido = Cod_partido;
        this.Visita = Visita;
        this.Hora = Hora;
        this.GolLocal = GolLocal;
        this.GolVisita = GolVisita;
    }


    public String getLocal() {
        return Local;
    }

    public void setLocal(String Local) {
        this.Local = Local;
    }
    public String getGanador() {
        return Ganador;
    }

    public void setGanador(String Ganador) {
        this.Ganador = Ganador;
    }
    public String getCod_liga() {
        return Cod_liga;
    }

    public void setCod_liga(String Cod_liga) {
        this.Cod_liga = Cod_liga;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getCod_partido() {
        return Cod_partido;
    }

    public void setCod_partido(String Cod_partido) {
        this.Cod_partido = Cod_partido;
    }
    public String getVisita() {
        return Visita;
    }

    public void setVisita(String Visita) {
        this.Visita = Visita;
    }
    public String getHora() {
        return Hora;
    }

    public void setHora(String Hora) {
        this.Hora = Hora;
    }
    public String getGollocal() {
        return GolLocal;
    }

    public void setGollocal(String GolLocal) {
        this.GolLocal = GolLocal;
    }
    public String getGolvisita() {
        return GolVisita;
    }

    public void setGolvisita(String GolVisita) {
        this.GolVisita = GolVisita;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }
    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}