





import java.util.List;
import java.util.ArrayList;

public class Zutat  {

    private String menge;
    private String name;
    private String einheit;





    private Zutaten zutaten;


    public Zutat(
        String menge,        String name,        String einheit    ) {
        this.menge = menge;
        this.name = name;
        this.einheit = einheit;
    }


    public String getMenge() {
        return menge;
    }

    public void setMenge(String menge) {
        this.menge = menge;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEinheit() {
        return einheit;
    }

    public void setEinheit(String einheit) {
        this.einheit = einheit;
    }

    public Zutaten getZutaten() {
        return zutaten;
    }

    public void setZutaten(Zutaten zutaten) {
        this.zutaten = zutaten;
    }

}