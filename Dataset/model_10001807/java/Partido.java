





import java.util.List;
import java.util.ArrayList;

public class Partido  {

    private String ronda;
    private int id;





    private Torneo torneo;


    public Partido(
        String ronda,        int id    ) {
        this.ronda = ronda;
        this.id = id;
    }


    public String getRonda() {
        return ronda;
    }

    public void setRonda(String ronda) {
        this.ronda = ronda;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Torneo getTorneo() {
        return torneo;
    }

    public void setTorneo(Torneo torneo) {
        this.torneo = torneo;
    }

}