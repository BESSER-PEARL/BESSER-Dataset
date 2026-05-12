





import java.util.List;
import java.util.ArrayList;

public class Lesion  {

    private String Cod_jugador;
    private String Condicion;
    private String FechaLesion;
    private String TiempoLesion;





    private Jugador jugador;


    public Lesion(
        String Cod_jugador,        String Condicion,        String FechaLesion,        String TiempoLesion    ) {
        this.Cod_jugador = Cod_jugador;
        this.Condicion = Condicion;
        this.FechaLesion = FechaLesion;
        this.TiempoLesion = TiempoLesion;
    }


    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }
    public String getCondicion() {
        return Condicion;
    }

    public void setCondicion(String Condicion) {
        this.Condicion = Condicion;
    }
    public String getFechalesion() {
        return FechaLesion;
    }

    public void setFechalesion(String FechaLesion) {
        this.FechaLesion = FechaLesion;
    }
    public String getTiempolesion() {
        return TiempoLesion;
    }

    public void setTiempolesion(String TiempoLesion) {
        this.TiempoLesion = TiempoLesion;
    }

    public Jugador getJugador() {
        return jugador;
    }

    public void setJugador(Jugador jugador) {
        this.jugador = jugador;
    }

}