





import java.util.List;
import java.util.ArrayList;

public class groesse  {

    private String laenge;
    private String name;
    private String breite;
    private String name1;





    private plaetzchenForm plaetzchenform;


    public groesse(
        String laenge,        String name,        String breite,        String name1    ) {
        this.laenge = laenge;
        this.name = name;
        this.breite = breite;
        this.name1 = name1;
    }


    public String getLaenge() {
        return laenge;
    }

    public void setLaenge(String laenge) {
        this.laenge = laenge;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBreite() {
        return breite;
    }

    public void setBreite(String breite) {
        this.breite = breite;
    }
    public String getName1() {
        return name1;
    }

    public void setName1(String name1) {
        this.name1 = name1;
    }

    public plaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(plaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }

}