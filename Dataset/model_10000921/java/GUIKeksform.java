





import java.util.List;
import java.util.ArrayList;

public class GUIKeksform  {

    private String name;
    private int breite;
    private int laenge;
    private None pl__f;





    private PlaetzchenForm plaetzchenform;




    private GUI gui;


    public GUIKeksform(
        String name,        int breite,        int laenge,        None pl__f    ) {
        this.name = name;
        this.breite = breite;
        this.laenge = laenge;
        this.pl__f = pl__f;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBreite() {
        return breite;
    }

    public void setBreite(int breite) {
        this.breite = breite;
    }
    public int getLaenge() {
        return laenge;
    }

    public void setLaenge(int laenge) {
        this.laenge = laenge;
    }
    public None getPl__f() {
        return pl__f;
    }

    public void setPl__f(None pl__f) {
        this.pl__f = pl__f;
    }

    public PlaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(PlaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }
    public GUI getGui() {
        return gui;
    }

    public void setGui(GUI gui) {
        this.gui = gui;
    }

}