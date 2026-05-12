





import java.util.List;
import java.util.ArrayList;

public class Equipo  {

    private String jugadores;
    private String nombre;
    private String porcentajeFavoritismo;





    private Partido partido;




    private Partido partido;


    public Equipo(
        String jugadores,        String nombre,        String porcentajeFavoritismo    ) {
        this.jugadores = jugadores;
        this.nombre = nombre;
        this.porcentajeFavoritismo = porcentajeFavoritismo;
    }


    public String getJugadores() {
        return jugadores;
    }

    public void setJugadores(String jugadores) {
        this.jugadores = jugadores;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getPorcentajefavoritismo() {
        return porcentajeFavoritismo;
    }

    public void setPorcentajefavoritismo(String porcentajeFavoritismo) {
        this.porcentajeFavoritismo = porcentajeFavoritismo;
    }

    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }
    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }

}