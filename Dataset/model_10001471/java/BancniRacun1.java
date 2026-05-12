





import java.util.List;
import java.util.ArrayList;

public class BancniRacun1  {

    private float stanje;
    private boolean aktiven;
    private String lastnik;



    public BancniRacun1(
        float stanje,        boolean aktiven,        String lastnik    ) {
        this.stanje = stanje;
        this.aktiven = aktiven;
        this.lastnik = lastnik;
    }


    public float getStanje() {
        return stanje;
    }

    public void setStanje(float stanje) {
        this.stanje = stanje;
    }
    public boolean getAktiven() {
        return aktiven;
    }

    public void setAktiven(boolean aktiven) {
        this.aktiven = aktiven;
    }
    public String getLastnik() {
        return lastnik;
    }

    public void setLastnik(String lastnik) {
        this.lastnik = lastnik;
    }


}