





import java.util.List;
import java.util.ArrayList;

public class Lesion  {

    private String FechaLesion;
    private String Condicion;
    private String TiempoLesion;
    private String Cod_jugador;



    public Lesion(
        String FechaLesion,        String Condicion,        String TiempoLesion,        String Cod_jugador    ) {
        this.FechaLesion = FechaLesion;
        this.Condicion = Condicion;
        this.TiempoLesion = TiempoLesion;
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


}