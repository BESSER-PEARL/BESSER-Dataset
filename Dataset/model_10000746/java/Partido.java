





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private String Cod_partido;
    private String Ganador;
    private String Hora;
    private String Visita;
    private String Fecha;
    private String Local;
    private String Cod_liga;
    private String GolVisita;
    private String GolLocal;





    private Equipo equipo;




    private Equipo equipo;


    public Partido(
        String Cod_partido,        String Ganador,        String Hora,        String Visita,        String Fecha,        String Local,        String Cod_liga,        String GolVisita,        String GolLocal    ) {
        this.Cod_partido = Cod_partido;
        this.Ganador = Ganador;
        this.Hora = Hora;
        this.Visita = Visita;
        this.Fecha = Fecha;
        this.Local = Local;
        this.Cod_liga = Cod_liga;
        this.GolVisita = GolVisita;
        this.GolLocal = GolLocal;
    }


    public String getCod_partido() {
        return Cod_partido;
    }

    public void setCod_partido(String Cod_partido) {
        this.Cod_partido = Cod_partido;
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
    public String getLocal() {
        return Local;
    }

    public void setLocal(String Local) {
        this.Local = Local;
    }
    public String getCod_liga() {
        return Cod_liga;
    }

    public void setCod_liga(String Cod_liga) {
        this.Cod_liga = Cod_liga;
    }
    public String getGolvisita() {
        return GolVisita;
    }

    public void setGolvisita(String GolVisita) {
        this.GolVisita = GolVisita;
    }
    public String getGollocal() {
        return GolLocal;
    }

    public void setGollocal(String GolLocal) {
        this.GolLocal = GolLocal;
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