





import java.util.List;
import java.util.ArrayList;

public class Evento  {

    private String Cod_jugador;
    private String Cod_partido;
    private String Cod_TipodeEvento;





    private Jugador jugador;




    private Partido partido;


    public Evento(
        String Cod_jugador,        String Cod_partido,        String Cod_TipodeEvento    ) {
        this.Cod_jugador = Cod_jugador;
        this.Cod_partido = Cod_partido;
        this.Cod_TipodeEvento = Cod_TipodeEvento;
    }


    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }
    public String getCod_partido() {
        return Cod_partido;
    }

    public void setCod_partido(String Cod_partido) {
        this.Cod_partido = Cod_partido;
    }
    public String getCod_tipodeevento() {
        return Cod_TipodeEvento;
    }

    public void setCod_tipodeevento(String Cod_TipodeEvento) {
        this.Cod_TipodeEvento = Cod_TipodeEvento;
    }

    public Jugador getJugador() {
        return jugador;
    }

    public void setJugador(Jugador jugador) {
        this.jugador = jugador;
    }
    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }

}