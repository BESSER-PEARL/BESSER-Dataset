





import java.util.List;
import java.util.ArrayList;

public class Kabine  {

    private boolean tuerZustand;





    private TurboliftSchacht turboliftschacht;


    public Kabine(
        boolean tuerZustand    ) {
        this.tuerZustand = tuerZustand;
    }


    public boolean getTuerzustand() {
        return tuerZustand;
    }

    public void setTuerzustand(boolean tuerZustand) {
        this.tuerZustand = tuerZustand;
    }

    public TurboliftSchacht getTurboliftschacht() {
        return turboliftschacht;
    }

    public void setTurboliftschacht(TurboliftSchacht turboliftschacht) {
        this.turboliftschacht = turboliftschacht;
    }

}