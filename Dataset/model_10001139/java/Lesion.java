





import java.util.List;
import java.util.ArrayList;

public class Lesion  {

    private String TiempoLesion;
    private String Cod_jugador;
    private String FechaLesion;
    private String Condicion;





    private Jugador jugador;


    public Lesion(
        String TiempoLesion,        String Cod_jugador,        String FechaLesion,        String Condicion    ) {
        this.TiempoLesion = TiempoLesion;
        this.Cod_jugador = Cod_jugador;
        this.FechaLesion = FechaLesion;
        this.Condicion = Condicion;
    }


    public String getTiempolesion() {
        return TiempoLesion;
    }

    public void setTiempolesion(String TiempoLesion) {
        this.TiempoLesion = TiempoLesion;
    }
    public String getCod_jugador() {
        return Cod_jugador;
    }

    public void setCod_jugador(String Cod_jugador) {
        this.Cod_jugador = Cod_jugador;
    }
    public String getFechalesion() {
        return FechaLesion;
    }

    public void setFechalesion(String FechaLesion) {
        this.FechaLesion = FechaLesion;
    }
    public String getCondicion() {
        return Condicion;
    }

    public void setCondicion(String Condicion) {
        this.Condicion = Condicion;
    }

    public Jugador getJugador() {
        return jugador;
    }

    public void setJugador(Jugador jugador) {
        this.jugador = jugador;
    }

}