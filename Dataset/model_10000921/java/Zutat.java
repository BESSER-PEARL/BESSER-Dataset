





import java.util.List;
import java.util.ArrayList;

public class Zutat  {

    private None einheit;
    private int menge;
    private None name;



    public Zutat(
        None einheit,        int menge,        None name    ) {
        this.einheit = einheit;
        this.menge = menge;
        this.name = name;
    }


    public None getEinheit() {
        return einheit;
    }

    public void setEinheit(None einheit) {
        this.einheit = einheit;
    }
    public int getMenge() {
        return menge;
    }

    public void setMenge(int menge) {
        this.menge = menge;
    }
    public None getName() {
        return name;
    }

    public void setName(None name) {
        this.name = name;
    }


}