





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private String Visita;
    private String Fecha;
    private String Ganador;
    private String Hora;
    private String GolLocal;
    private String GolVisita;
    private String Local;
    private String Cod_partido;
    private String Cod_liga;





    private Equipo equipo;




    private Estadio estadio;




    private Liga liga;




    private Equipo equipo;


    public Partido(
        String Visita,        String Fecha,        String Ganador,        String Hora,        String GolLocal,        String GolVisita,        String Local,        String Cod_partido,        String Cod_liga    ) {
        this.Visita = Visita;
        this.Fecha = Fecha;
        this.Ganador = Ganador;
        this.Hora = Hora;
        this.GolLocal = GolLocal;
        this.GolVisita = GolVisita;
        this.Local = Local;
        this.Cod_partido = Cod_partido;
        this.Cod_liga = Cod_liga;
    }


    public String getVisita() {
        return Visita;
    }

    public void setVisita(String Visita) {
        this.Visita = Visita;
    }
    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getGanador() {
        return Ganador;
    }

    public void setGanador(String Ganador) {
        this.Ganador = Ganador;
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
    public String getLocal() {
        return Local;
    }

    public void setLocal(String Local) {
        this.Local = Local;
    }
    public String getCod_partido() {
        return Cod_partido;
    }

    public void setCod_partido(String Cod_partido) {
        this.Cod_partido = Cod_partido;
    }
    public String getCod_liga() {
        return Cod_liga;
    }

    public void setCod_liga(String Cod_liga) {
        this.Cod_liga = Cod_liga;
    }

    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }
    public Estadio getEstadio() {
        return estadio;
    }

    public void setEstadio(Estadio estadio) {
        this.estadio = estadio;
    }
    public Liga getLiga() {
        return liga;
    }

    public void setLiga(Liga liga) {
        this.liga = liga;
    }
    public Equipo getEquipo() {
        return equipo;
    }

    public void setEquipo(Equipo equipo) {
        this.equipo = equipo;
    }

}