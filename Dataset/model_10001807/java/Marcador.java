





import java.util.List;
import java.util.ArrayList;

public class Marcador  {

    private int tiempoSet;
    private int equipo1;
    private int equipo2;





    private Partido partido;


    public Marcador(
        int tiempoSet,        int equipo1,        int equipo2    ) {
        this.tiempoSet = tiempoSet;
        this.equipo1 = equipo1;
        this.equipo2 = equipo2;
    }


    public int getTiemposet() {
        return tiempoSet;
    }

    public void setTiemposet(int tiempoSet) {
        this.tiempoSet = tiempoSet;
    }
    public int getEquipo1() {
        return equipo1;
    }

    public void setEquipo1(int equipo1) {
        this.equipo1 = equipo1;
    }
    public int getEquipo2() {
        return equipo2;
    }

    public void setEquipo2(int equipo2) {
        this.equipo2 = equipo2;
    }

    public Partido getPartido() {
        return partido;
    }

    public void setPartido(Partido partido) {
        this.partido = partido;
    }

}