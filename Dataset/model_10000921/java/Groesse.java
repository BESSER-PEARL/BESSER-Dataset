





import java.util.List;
import java.util.ArrayList;

public class Groesse  {

    private int laenge;
    private None name1;
    private int breite;
    private String name;





    private PlaetzchenForm plaetzchenform;


    public Groesse(
        int laenge,        None name1,        int breite,        String name    ) {
        this.laenge = laenge;
        this.name1 = name1;
        this.breite = breite;
        this.name = name;
    }


    public int getLaenge() {
        return laenge;
    }

    public void setLaenge(int laenge) {
        this.laenge = laenge;
    }
    public None getName1() {
        return name1;
    }

    public void setName1(None name1) {
        this.name1 = name1;
    }
    public int getBreite() {
        return breite;
    }

    public void setBreite(int breite) {
        this.breite = breite;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PlaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(PlaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }

}