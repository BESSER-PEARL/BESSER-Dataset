





import java.util.List;
import java.util.ArrayList;

public class shr5_FahrzeugModifikation extends Quelle, Beschreibbar, GeldWert {

    private int capacityUsed;





    private shr5_Fahrzeug shr5_fahrzeug;


    public shr5_FahrzeugModifikation(
        int capacityUsed    ) {
        super(
        );
        this.capacityUsed = capacityUsed;
    }


    public int getCapacityused() {
        return capacityUsed;
    }

    public void setCapacityused(int capacityUsed) {
        this.capacityUsed = capacityUsed;
    }

    public shr5_Fahrzeug getShr5_fahrzeug() {
        return shr5_fahrzeug;
    }

    public void setShr5_fahrzeug(shr5_Fahrzeug shr5_fahrzeug) {
        this.shr5_fahrzeug = shr5_fahrzeug;
    }

}