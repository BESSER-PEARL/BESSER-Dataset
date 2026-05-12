





import java.util.List;
import java.util.ArrayList;

public class BancniRacun  {

    private String lastnik;
    private boolean aktiven;
    private float stanje;



    public BancniRacun(
        String lastnik,        boolean aktiven,        float stanje    ) {
        this.lastnik = lastnik;
        this.aktiven = aktiven;
        this.stanje = stanje;
    }


    public String getLastnik() {
        return lastnik;
    }

    public void setLastnik(String lastnik) {
        this.lastnik = lastnik;
    }
    public boolean getAktiven() {
        return aktiven;
    }

    public void setAktiven(boolean aktiven) {
        this.aktiven = aktiven;
    }
    public float getStanje() {
        return stanje;
    }

    public void setStanje(float stanje) {
        this.stanje = stanje;
    }


}