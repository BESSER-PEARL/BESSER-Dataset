





import java.util.List;
import java.util.ArrayList;

public class Premio  {

    private int Puntos;
    private int Dinero;
    private int Puesto;





    private Torneo torneo;


    public Premio(
        int Puntos,        int Dinero,        int Puesto    ) {
        this.Puntos = Puntos;
        this.Dinero = Dinero;
        this.Puesto = Puesto;
    }


    public int getPuntos() {
        return Puntos;
    }

    public void setPuntos(int Puntos) {
        this.Puntos = Puntos;
    }
    public int getDinero() {
        return Dinero;
    }

    public void setDinero(int Dinero) {
        this.Dinero = Dinero;
    }
    public int getPuesto() {
        return Puesto;
    }

    public void setPuesto(int Puesto) {
        this.Puesto = Puesto;
    }

    public Torneo getTorneo() {
        return torneo;
    }

    public void setTorneo(Torneo torneo) {
        this.torneo = torneo;
    }

}